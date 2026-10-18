# IvtInitializeIommu

- RVA: `0x00B61FE0`–`0x00B6293B` (길이 `2,395` bytes)
- VA: `0x0000000140B61FE0`
- 실행 섹션: `PAGELK`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C5294`
- 디코드: `607`개 명령, `2,395/2,395` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **57**; 고유 호출 대상: **30**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **9**

### Outgoing calls
- `0x00B6207F` → [IvtInvalidateRemappingTableEntries](../../text/46/IvtInvalidateRemappingTableEntries_function_0046A520.md) (function, `0x0046A520`)
- `0x00B6208F` → [IvtUpdateGlobalCommand](../../text/57/IvtUpdateGlobalCommand_function_00572854.md) (function, `0x00572854`)
- `0x00B6209D` → [Feature_Test57481295__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_Test57481295__private_IsEnabledDeviceUsageNoInline_function_004F7B90.md) (function, `0x004F7B90`)
- `0x00B620A9` → [IvtInvalidateAllContextEntries](../../text/57/IvtInvalidateAllContextEntries_function_00570858.md) (function, `0x00570858`)
- `0x00B620B0` → [IvtInvalidateAllContextEntries](../../text/57/IvtInvalidateAllContextEntries_function_00570858.md) (function, `0x00570858`)
- `0x00B620D8` → [IvtInvalidateScalableModePasidCache](../../text/57/IvtInvalidateScalableModePasidCache_function_005709B8.md) (function, `0x005709B8`)
- `0x00B620DD` → [Feature_Test57481295__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_Test57481295__private_IsEnabledDeviceUsageNoInline_function_004F7B90.md) (function, `0x004F7B90`)
- `0x00B62104` → [IvtLegacyFlushTbInternal](../../text/57/IvtLegacyFlushTbInternal_function_005714E8.md) (function, `0x005714E8`)
- `0x00B62129` → [IvtFlushTbInternal](../../text/2D/IvtFlushTbInternal_function_002D2548.md) (function, `0x002D2548`)
- `0x00B6214E` → [HalSocRequestApi](../../text/4B/HalSocRequestApi_function_004B848C.md) (function, `0x004B848C`)
- `0x00B6216F` → [HalMapIoSpace](../../text/4F/HalMapIoSpace_function_004FCD40.md) (function, `0x004FCD40`)
- `0x00B6219A` → [IvtUpdateGlobalCommand](../../text/57/IvtUpdateGlobalCommand_function_00572854.md) (function, `0x00572854`)
- `0x00B6220D` → [IvtUpdateGlobalCommand](../../text/57/IvtUpdateGlobalCommand_function_00572854.md) (function, `0x00572854`)
- `0x00B62230` → [IvtUpdateGlobalCommand](../../text/57/IvtUpdateGlobalCommand_function_00572854.md) (function, `0x00572854`)
- `0x00B62259` → [IvtInitializeIdentityMappings](../../text/57/IvtInitializeIdentityMappings_function_005702A8.md) (function, `0x005702A8`)
- `0x00B6227D` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00B622A2` → [HalMapIoSpace](../../text/4F/HalMapIoSpace_function_004FCD40.md) (function, `0x004FCD40`)
- `0x00B622B4` → [Feature_Test57481295__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_Test57481295__private_IsEnabledDeviceUsageNoInline_function_004F7B90.md) (function, `0x004F7B90`)
- `0x00B622C6` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00B622E1` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00B62303` → [HalMapIoSpace](../../text/4F/HalMapIoSpace_function_004FCD40.md) (function, `0x004FCD40`)
- `0x00B62320` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00B62340` → [IvtGetIdentityMappedDomain](../../text/56/IvtGetIdentityMappedDomain_function_0056FB58.md) (function, `0x0056FB58`)
- `0x00B62359` → [IvtGetBlockedDomain](../../text/4D/IvtGetBlockedDomain_function_004D2204.md) (function, `0x004D2204`)
- `0x00B62373` → [IvtGetPasidGranularTranslationType](../../text/4F/IvtGetPasidGranularTranslationType_function_004FC2FC.md) (function, `0x004FC2FC`)
- `0x00B6237B` → [Feature_Test57481295__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_Test57481295__private_IsEnabledDeviceUsageNoInline_function_004F7B90.md) (function, `0x004F7B90`)
- `0x00B62391` → [IvtLegacySetupScalableModeDefaultPasidTables](IvtLegacySetupScalableModeDefaultPasidTables_function_00B62A5C.md) (function, `0x00B62A5C`)
- `0x00B623B1` → [IvtLegacyBuildScalableModeContextEntry](../../text/57/IvtLegacyBuildScalableModeContextEntry_function_00571198.md) (function, `0x00571198`)
- `0x00B623B8` → [IvtSetupScalableModeDefaultPasidTables](IvtSetupScalableModeDefaultPasidTables_function_00B62E78.md) (function, `0x00B62E78`)
- `0x00B623D8` → [IvtBuildScalableModeContextEntry](../../text/4F/IvtBuildScalableModeContextEntry_function_004FA57C.md) (function, `0x004FA57C`)
- `0x00B623EA` → [Feature_Test57481295__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_Test57481295__private_IsEnabledDeviceUsageNoInline_function_004F7B90.md) (function, `0x004F7B90`)
- `0x00B623FA` → [IvtLegacySetScalableModeContextEntry](../../text/57/IvtLegacySetScalableModeContextEntry_function_00572178.md) (function, `0x00572178`)
- `0x00B62401` → [IvtSetScalableModeContextEntry](../../text/57/IvtSetScalableModeContextEntry_function_00572814.md) (function, `0x00572814`)
- `0x00B62411` → [IvtGetContextEntryType](../../text/4F/IvtGetContextEntryType_function_004FC598.md) (function, `0x004FC598`)
- `0x00B6242C` → [IvtBuildContextEntry](../../text/4E/IvtBuildContextEntry_function_004E31F4.md) (function, `0x004E31F4`)
- `0x00B6248A` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00B624AF` → [HalMapIoSpace](../../text/4F/HalMapIoSpace_function_004FCD40.md) (function, `0x004FCD40`)
- `0x00B6251B` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00B62532` → [HalMapIoSpace](../../text/4F/HalMapIoSpace_function_004FCD40.md) (function, `0x004FCD40`)
- `0x00B6254C` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00B6255C` → [Feature_Test57481295__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_Test57481295__private_IsEnabledDeviceUsageNoInline_function_004F7B90.md) (function, `0x004F7B90`)
- `0x00B62568` → [IvtLegacyProcessDeviceExceptions](IvtLegacyProcessDeviceExceptions_function_00B62944.md) (function, `0x00B62944`)
- `0x00B6256F` → [IvtProcessDeviceExceptions](IvtProcessDeviceExceptions_function_00B62C34.md) (function, `0x00B62C34`)
- `0x00B625B4` → [IvtUpdateGlobalCommand](../../text/57/IvtUpdateGlobalCommand_function_00572854.md) (function, `0x00572854`)
- `0x00B62648` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00B62663` → [HalMapIoSpace](../../text/4F/HalMapIoSpace_function_004FCD40.md) (function, `0x004FCD40`)
- `0x00B62682` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00B62760` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00B62781` → [HalMapIoSpace](../../text/4F/HalMapIoSpace_function_004FCD40.md) (function, `0x004FCD40`)
- `0x00B6279A` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00B62822` → [KeStallExecutionProcessor](../../text/44/KeStallExecutionProcessor_function_0044F620.md) (function, `0x0044F620`)
- `0x00B6284C` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00B6285D` → [IvtUpdateGlobalCommand](../../text/57/IvtUpdateGlobalCommand_function_00572854.md) (function, `0x00572854`)
- `0x00B628AD` → [IvtInitializeMTRR](../../text/57/IvtInitializeMTRR_function_0057053C.md) (function, `0x0057053C`)
- `0x00B628C2` → [MmGetPhysicalAddress](../../text/23/MmGetPhysicalAddress_function_0023A500.md) (function, `0x0023A500`)
- `0x00B62906` → [IvtUpdateGlobalCommand](../../text/57/IvtUpdateGlobalCommand_function_00572854.md) (function, `0x00572854`)
- `0x00B62914` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00B62003` → RVA `0x00E0A740` (`.data`; read)
- `0x00B6213A` → RVA `0x00F8F7D0` (`.data`; read)
- `0x00B622CB` → RVA `0x00E65AC0` (`.data`; read)
- `0x00B622E6` → RVA `0x00F8F7B8` (`.data`; write)
- `0x00B62308` → RVA `0x00E65AC0` (`.data`; write)
- `0x00B62711` → RVA `0x00F8F7C0` (`.data`; read)
- `0x00B6271F` → RVA `0x00F8F7C8` (`.data`; read)
- `0x00B627BD` → RVA `0x00F8F7C0` (`.data`; write)
- `0x00B627CB` → RVA `0x00F8F7C8` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **53**
  - `0x00B6207F` → [IvtInvalidateRemappingTableEntries](../../text/46/IvtInvalidateRemappingTableEntries_function_0046A520.md) (`PAGELK` → `.text`)
  - `0x00B6208F` → [IvtUpdateGlobalCommand](../../text/57/IvtUpdateGlobalCommand_function_00572854.md) (`PAGELK` → `.text`)
  - `0x00B6209D` → [Feature_Test57481295__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_Test57481295__private_IsEnabledDeviceUsageNoInline_function_004F7B90.md) (`PAGELK` → `.text`)
  - `0x00B620A9` → [IvtInvalidateAllContextEntries](../../text/57/IvtInvalidateAllContextEntries_function_00570858.md) (`PAGELK` → `.text`)
  - `0x00B620B0` → [IvtInvalidateAllContextEntries](../../text/57/IvtInvalidateAllContextEntries_function_00570858.md) (`PAGELK` → `.text`)
  - `0x00B620D8` → [IvtInvalidateScalableModePasidCache](../../text/57/IvtInvalidateScalableModePasidCache_function_005709B8.md) (`PAGELK` → `.text`)
  - `0x00B620DD` → [Feature_Test57481295__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_Test57481295__private_IsEnabledDeviceUsageNoInline_function_004F7B90.md) (`PAGELK` → `.text`)
  - `0x00B62104` → [IvtLegacyFlushTbInternal](../../text/57/IvtLegacyFlushTbInternal_function_005714E8.md) (`PAGELK` → `.text`)
  - `0x00B62129` → [IvtFlushTbInternal](../../text/2D/IvtFlushTbInternal_function_002D2548.md) (`PAGELK` → `.text`)
  - `0x00B6214E` → [HalSocRequestApi](../../text/4B/HalSocRequestApi_function_004B848C.md) (`PAGELK` → `.text`)
  - `0x00B6216F` → [HalMapIoSpace](../../text/4F/HalMapIoSpace_function_004FCD40.md) (`PAGELK` → `.text`)
  - `0x00B6219A` → [IvtUpdateGlobalCommand](../../text/57/IvtUpdateGlobalCommand_function_00572854.md) (`PAGELK` → `.text`)
  - `0x00B6220D` → [IvtUpdateGlobalCommand](../../text/57/IvtUpdateGlobalCommand_function_00572854.md) (`PAGELK` → `.text`)
  - `0x00B62230` → [IvtUpdateGlobalCommand](../../text/57/IvtUpdateGlobalCommand_function_00572854.md) (`PAGELK` → `.text`)
  - `0x00B62259` → [IvtInitializeIdentityMappings](../../text/57/IvtInitializeIdentityMappings_function_005702A8.md) (`PAGELK` → `.text`)
  - `0x00B6227D` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGELK` → `.text`)
  - `0x00B622A2` → [HalMapIoSpace](../../text/4F/HalMapIoSpace_function_004FCD40.md) (`PAGELK` → `.text`)
  - `0x00B622B4` → [Feature_Test57481295__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_Test57481295__private_IsEnabledDeviceUsageNoInline_function_004F7B90.md) (`PAGELK` → `.text`)
  - `0x00B622C6` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGELK` → `.text`)
  - `0x00B622E1` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGELK` → `.text`)
  - `0x00B62303` → [HalMapIoSpace](../../text/4F/HalMapIoSpace_function_004FCD40.md) (`PAGELK` → `.text`)
  - `0x00B62320` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGELK` → `.text`)
  - `0x00B62340` → [IvtGetIdentityMappedDomain](../../text/56/IvtGetIdentityMappedDomain_function_0056FB58.md) (`PAGELK` → `.text`)
  - `0x00B62359` → [IvtGetBlockedDomain](../../text/4D/IvtGetBlockedDomain_function_004D2204.md) (`PAGELK` → `.text`)
  - `0x00B62373` → [IvtGetPasidGranularTranslationType](../../text/4F/IvtGetPasidGranularTranslationType_function_004FC2FC.md) (`PAGELK` → `.text`)
  - `0x00B6237B` → [Feature_Test57481295__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_Test57481295__private_IsEnabledDeviceUsageNoInline_function_004F7B90.md) (`PAGELK` → `.text`)
  - `0x00B623B1` → [IvtLegacyBuildScalableModeContextEntry](../../text/57/IvtLegacyBuildScalableModeContextEntry_function_00571198.md) (`PAGELK` → `.text`)
  - `0x00B623D8` → [IvtBuildScalableModeContextEntry](../../text/4F/IvtBuildScalableModeContextEntry_function_004FA57C.md) (`PAGELK` → `.text`)
  - `0x00B623EA` → [Feature_Test57481295__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_Test57481295__private_IsEnabledDeviceUsageNoInline_function_004F7B90.md) (`PAGELK` → `.text`)
  - `0x00B623FA` → [IvtLegacySetScalableModeContextEntry](../../text/57/IvtLegacySetScalableModeContextEntry_function_00572178.md) (`PAGELK` → `.text`)
  - `0x00B62401` → [IvtSetScalableModeContextEntry](../../text/57/IvtSetScalableModeContextEntry_function_00572814.md) (`PAGELK` → `.text`)
  - `0x00B62411` → [IvtGetContextEntryType](../../text/4F/IvtGetContextEntryType_function_004FC598.md) (`PAGELK` → `.text`)
  - `0x00B6242C` → [IvtBuildContextEntry](../../text/4E/IvtBuildContextEntry_function_004E31F4.md) (`PAGELK` → `.text`)
  - `0x00B6248A` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGELK` → `.text`)
  - `0x00B624AF` → [HalMapIoSpace](../../text/4F/HalMapIoSpace_function_004FCD40.md) (`PAGELK` → `.text`)
  - `0x00B6251B` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGELK` → `.text`)
  - `0x00B62532` → [HalMapIoSpace](../../text/4F/HalMapIoSpace_function_004FCD40.md) (`PAGELK` → `.text`)
  - `0x00B6254C` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGELK` → `.text`)
  - `0x00B6255C` → [Feature_Test57481295__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_Test57481295__private_IsEnabledDeviceUsageNoInline_function_004F7B90.md) (`PAGELK` → `.text`)
  - `0x00B625B4` → [IvtUpdateGlobalCommand](../../text/57/IvtUpdateGlobalCommand_function_00572854.md) (`PAGELK` → `.text`)
  - `0x00B62648` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGELK` → `.text`)
  - `0x00B62663` → [HalMapIoSpace](../../text/4F/HalMapIoSpace_function_004FCD40.md) (`PAGELK` → `.text`)
  - `0x00B62682` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGELK` → `.text`)
  - `0x00B62760` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGELK` → `.text`)
  - `0x00B62781` → [HalMapIoSpace](../../text/4F/HalMapIoSpace_function_004FCD40.md) (`PAGELK` → `.text`)
  - `0x00B6279A` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGELK` → `.text`)
  - `0x00B62822` → [KeStallExecutionProcessor](../../text/44/KeStallExecutionProcessor_function_0044F620.md) (`PAGELK` → `.text`)
  - `0x00B6284C` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGELK` → `.text`)
  - `0x00B6285D` → [IvtUpdateGlobalCommand](../../text/57/IvtUpdateGlobalCommand_function_00572854.md) (`PAGELK` → `.text`)
  - `0x00B628AD` → [IvtInitializeMTRR](../../text/57/IvtInitializeMTRR_function_0057053C.md) (`PAGELK` → `.text`)
  - `0x00B628C2` → [MmGetPhysicalAddress](../../text/23/MmGetPhysicalAddress_function_0023A500.md) (`PAGELK` → `.text`)
  - `0x00B62906` → [IvtUpdateGlobalCommand](../../text/57/IvtUpdateGlobalCommand_function_00572854.md) (`PAGELK` → `.text`)
  - `0x00B62914` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGELK` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B61FE0  48 8B C4                        mov rax, rsp
00B61FE3  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00B61FE7  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
00B61FEB  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
00B61FEF  55                              push rbp
00B61FF0  41 54                           push r12
00B61FF2  41 55                           push r13
00B61FF4  41 56                           push r14
00B61FF6  41 57                           push r15
00B61FF8  48 8D 68 A1                     lea rbp, [rax - 0x5f]
00B61FFC  48 81 EC D0 00 00 00            sub rsp, 0xd0
00B62003  48 8B 05 36 87 2A 00            mov rax, qword ptr [rip + 0x2a8736]
00B6200A  48 33 C4                        xor rax, rsp
00B6200D  48 89 45 27                     mov qword ptr [rbp + 0x27], rax
00B62011  8B 81 30 01 00 00               mov eax, dword ptr [rcx + 0x130]
00B62017  33 FF                           xor edi, edi
00B62019  44 8B A9 34 01 00 00            mov r13d, dword ptr [rcx + 0x134]
00B62020  0F 57 C0                        xorps xmm0, xmm0
00B62023  0F 57 C9                        xorps xmm1, xmm1
00B62026  89 45 BB                        mov dword ptr [rbp - 0x45], eax
00B62029  8B 81 38 01 00 00               mov eax, dword ptr [rcx + 0x138]
00B6202F  48 83 CB FF                     or rbx, 0xffffffffffffffff
00B62033  89 45 D3                        mov dword ptr [rbp - 0x2d], eax
00B62036  45 8A F8                        mov r15b, r8b
00B62039  44 88 45 B7                     mov byte ptr [rbp - 0x49], r8b
00B6203D  48 8B F1                        mov rsi, rcx
00B62040  89 7D BF                        mov dword ptr [rbp - 0x41], edi
00B62043  41 BC 00 00 01 00               mov r12d, 0x10000
00B62049  89 7D D7                        mov dword ptr [rbp - 0x29], edi
00B6204C  44 89 6D CF                     mov dword ptr [rbp - 0x31], r13d
00B62050  48 89 7D C7                     mov qword ptr [rbp - 0x39], rdi
00B62054  0F 11 45 DF                     movups xmmword ptr [rbp - 0x21], xmm0
00B62058  0F 11 45 F7                     movups xmmword ptr [rbp - 9], xmm0
00B6205C  0F 11 4D 07                     movups xmmword ptr [rbp + 7], xmm1
00B62060  0F 11 4D 17                     movups xmmword ptr [rbp + 0x17], xmm1
00B62064  85 D2                           test edx, edx
00B62066  0F 84 CC 00 00 00               je 0x140b62138
00B6206C  83 FA 03                        cmp edx, 3
00B6206F  0F 85 96 08 00 00               jne 0x140b6290b
00B62075  44 8D 77 01                     lea r14d, [rdi + 1]
00B62079  85 C0                           test eax, eax
00B6207B  74 17                           je 0x140b62094
00B6207D  33 D2                           xor edx, edx
00B6207F  E8 9C 84 90 FF                  call 0x14046a520
00B62084  45 8A C6                        mov r8b, r14b
00B62087  BA 00 00 00 02                  mov edx, 0x2000000
00B6208C  48 8B CE                        mov rcx, rsi
00B6208F  E8 C0 07 A1 FF                  call 0x140572854
00B62094  45 85 ED                        test r13d, r13d
00B62097  0F 84 6E 08 00 00               je 0x140b6290b
00B6209D  E8 EE 5A 99 FF                  call 0x1404f7b90
00B620A2  48 8B CE                        mov rcx, rsi
00B620A5  85 C0                           test eax, eax
00B620A7  75 07                           jne 0x140b620b0
00B620A9  E8 AA E7 A0 FF                  call 0x140570858
00B620AE  EB 05                           jmp 0x140b620b5
00B620B0  E8 A3 E7 A0 FF                  call 0x140570858
00B620B5  40 38 BE 40 01 00 00            cmp byte ptr [rsi + 0x140], dil
00B620BC  74 1F                           je 0x140b620dd
00B620BE  83 CA FF                        or edx, 0xffffffff
00B620C1  40 88 7C 24 30                  mov byte ptr [rsp + 0x30], dil
00B620C6  44 8B CA                        mov r9d, edx
00B620C9  40 88 7C 24 28                  mov byte ptr [rsp + 0x28], dil
00B620CE  4D 8B C4                        mov r8, r12
00B620D1  89 7C 24 20                     mov dword ptr [rsp + 0x20], edi
00B620D5  48 8B CE                        mov rcx, rsi
00B620D8  E8 DB E8 A0 FF                  call 0x1405709b8
00B620DD  E8 AE 5A 99 FF                  call 0x1404f7b90
00B620E2  33 D2                           xor edx, edx
00B620E4  48 8B CE                        mov rcx, rsi
00B620E7  85 C0                           test eax, eax
00B620E9  75 20                           jne 0x140b6210b
00B620EB  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
00B620F0  45 8A CE                        mov r9b, r14b
00B620F3  89 7C 24 30                     mov dword ptr [rsp + 0x30], edi
00B620F7  45 33 C0                        xor r8d, r8d
00B620FA  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
00B620FF  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00B62104  E8 DF F3 A0 FF                  call 0x1405714e8
00B62109  EB 23                           jmp 0x140b6212e
00B6210B  48 89 7C 24 40                  mov qword ptr [rsp + 0x40], rdi
00B62110  45 33 C9                        xor r9d, r9d
00B62113  89 7C 24 38                     mov dword ptr [rsp + 0x38], edi
00B62117  45 33 C0                        xor r8d, r8d
00B6211A  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
00B6211F  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
00B62124  44 88 74 24 20                  mov byte ptr [rsp + 0x20], r14b
00B62129  E8 1A 04 77 FF                  call 0x1402d2548
00B6212E  BA 00 00 00 80                  mov edx, 0x80000000
00B62133  E9 C8 07 00 00                  jmp 0x140b62900
00B62138  33 D2                           xor edx, edx
00B6213A  48 8D 05 8F D6 42 00            lea rax, [rip + 0x42d68f]
00B62141  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00B62146  44 8D 4A 08                     lea r9d, [rdx + 8]
00B6214A  44 8D 42 04                     lea r8d, [rdx + 4]
00B6214E  E8 39 63 95 FF                  call 0x1404b848c
00B62153  85 C0                           test eax, eax
00B62155  0F 88 B2 07 00 00               js 0x140b6290d
00B6215B  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
00B6215F  48 85 C0                        test rax, rax
00B62162  75 1D                           jne 0x140b62181
00B62164  48 8B 0E                        mov rcx, qword ptr [rsi]
00B62167  45 33 C0                        xor r8d, r8d
00B6216A  BA 20 02 00 00                  mov edx, 0x220
00B6216F  E8 CC AB 99 FF                  call 0x1404fcd40
00B62174  48 89 46 08                     mov qword ptr [rsi + 8], rax
00B62178  48 85 C0                        test rax, rax
00B6217B  0F 84 53 06 00 00               je 0x140b627d4
00B62181  41 BE 00 00 00 80               mov r14d, 0x80000000
00B62187  44 89 70 38                     mov dword ptr [rax + 0x38], r14d
00B6218B  F0 09 3C 24                     lock or dword ptr [rsp], edi
00B6218F  45 33 C0                        xor r8d, r8d
00B62192  BA 00 00 00 04                  mov edx, 0x4000000
00B62197  48 8B CE                        mov rcx, rsi
00B6219A  E8 B5 06 A1 FF                  call 0x140572854
00B6219F  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
00B621A3  90                              nop
00B621A4  8B 40 34                        mov eax, dword ptr [rax + 0x34]
00B621A7  85 C0                           test eax, eax
00B621A9  74 0B                           je 0x140b621b6
00B621AB  48 8B 4E 08                     mov rcx, qword ptr [rsi + 8]
00B621AF  89 41 34                        mov dword ptr [rcx + 0x34], eax
00B621B2  F0 09 3C 24                     lock or dword ptr [rsp], edi
00B621B6  40 38 BE 40 01 00 00            cmp byte ptr [rsi + 0x140], dil
00B621BD  74 43                           je 0x140b62202
00B621BF  8B 86 E0 00 00 00               mov eax, dword ptr [rsi + 0xe0]
00B621C5  48 0F BA E0 1D                  bt rax, 0x1d
00B621CA  73 36                           jae 0x140b62202
00B621CC  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
00B621D0  BA E0 00 00 00                  mov edx, 0xe0
00B621D5  90                              nop
00B621D6  8B 0C 10                        mov ecx, dword ptr [rax + rdx]
00B621D9  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
00B621DD  41 0B CE                        or ecx, r14d
00B621E0  89 0C 10                        mov dword ptr [rax + rdx], ecx
00B621E3  F0 09 3C 24                     lock or dword ptr [rsp], edi
00B621E7  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
00B621EB  BA DC 00 00 00                  mov edx, 0xdc
00B621F0  90                              nop
00B621F1  8B 0C 10                        mov ecx, dword ptr [rax + rdx]
00B621F4  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
00B621F8  83 C9 03                        or ecx, 3
00B621FB  89 0C 10                        mov dword ptr [rax + rdx], ecx
00B621FE  F0 09 3C 24                     lock or dword ptr [rsp], edi
00B62202  45 33 C0                        xor r8d, r8d
00B62205  BA 00 00 00 02                  mov edx, 0x2000000
00B6220A  48 8B CE                        mov rcx, rsi
00B6220D  E8 42 06 A1 FF                  call 0x140572854
00B62212  40 38 BE 40 01 00 00            cmp byte ptr [rsi + 0x140], dil
00B62219  74 1A                           je 0x140b62235
00B6221B  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
00B6221F  90                              nop
00B62220  8B 40 1C                        mov eax, dword ptr [rax + 0x1c]
00B62223  85 C0                           test eax, eax
00B62225  79 0E                           jns 0x140b62235
00B62227  45 33 C0                        xor r8d, r8d
00B6222A  41 8B D6                        mov edx, r14d
00B6222D  48 8B CE                        mov rcx, rsi
00B62230  E8 1F 06 A1 FF                  call 0x140572854
00B62235  41 BE 01 00 00 00               mov r14d, 1
00B6223B  45 85 ED                        test r13d, r13d
00B6223E  0F 84 77 03 00 00               je 0x140b625bb
00B62244  40 38 BE 3F 01 00 00            cmp byte ptr [rsi + 0x13f], dil
00B6224B  74 19                           je 0x140b62266
00B6224D  48 39 BE 50 01 00 00            cmp qword ptr [rsi + 0x150], rdi
00B62254  75 10                           jne 0x140b62266
00B62256  48 8B CE                        mov rcx, rsi
00B62259  E8 4A E0 A0 FF                  call 0x1405702a8
00B6225E  85 C0                           test eax, eax
00B62260  0F 88 6E 05 00 00               js 0x140b627d4
00B62266  48 39 7E 28                     cmp qword ptr [rsi + 0x28], rdi
00B6226A  0F 85 03 02 00 00               jne 0x140b62473
00B62270  48 8B 05 59 D5 42 00            mov rax, qword ptr [rip + 0x42d559]
00B62277  41 8B D6                        mov edx, r14d
00B6227A  48 8B CB                        mov rcx, rbx
00B6227D  E8 4E 88 B5 FF                  call 0x1406baad0
00B62282  48 89 46 30                     mov qword ptr [rsi + 0x30], rax
00B62286  48 85 C0                        test rax, rax
00B62289  0F 84 45 05 00 00               je 0x140b627d4
00B6228F  44 8B 86 10 01 00 00            mov r8d, dword ptr [rsi + 0x110]
00B62296  41 BF 00 10 00 00               mov r15d, 0x1000
00B6229C  41 8B D7                        mov edx, r15d
00B6229F  48 8B C8                        mov rcx, rax
00B622A2  E8 99 AA 99 FF                  call 0x1404fcd40
00B622A7  48 89 46 28                     mov qword ptr [rsi + 0x28], rax
00B622AB  48 85 C0                        test rax, rax
00B622AE  0F 84 20 05 00 00               je 0x140b627d4
00B622B4  E8 D7 58 99 FF                  call 0x1404f7b90
00B622B9  85 C0                           test eax, eax
00B622BB  74 0E                           je 0x140b622cb
00B622BD  48 8B 4E 28                     mov rcx, qword ptr [rsi + 0x28]
00B622C1  45 8B C7                        mov r8d, r15d
00B622C4  33 D2                           xor edx, edx
00B622C6  E8 75 49 B6 FF                  call 0x1406c6c40
00B622CB  48 39 3D EE 37 30 00            cmp qword ptr [rip + 0x3037ee], rdi
00B622D2  75 51                           jne 0x140b62325
00B622D4  48 8B 05 F5 D4 42 00            mov rax, qword ptr [rip + 0x42d4f5]
00B622DB  41 8B D6                        mov edx, r14d
00B622DE  48 8B CB                        mov rcx, rbx
00B622E1  E8 EA 87 B5 FF                  call 0x1406baad0
00B622E6  48 89 05 CB D4 42 00            mov qword ptr [rip + 0x42d4cb], rax
00B622ED  48 85 C0                        test rax, rax
00B622F0  0F 84 DE 04 00 00               je 0x140b627d4
00B622F6  44 8B 86 10 01 00 00            mov r8d, dword ptr [rsi + 0x110]
00B622FD  49 8B D7                        mov rdx, r15
00B62300  48 8B C8                        mov rcx, rax
00B62303  E8 38 AA 99 FF                  call 0x1404fcd40
00B62308  48 89 05 B1 37 30 00            mov qword ptr [rip + 0x3037b1], rax
00B6230F  48 85 C0                        test rax, rax
00B62312  0F 84 BC 04 00 00               je 0x140b627d4
00B62318  4D 8B C7                        mov r8, r15
00B6231B  33 D2                           xor edx, edx
00B6231D  48 8B C8                        mov rcx, rax
00B62320  E8 1B 49 B6 FF                  call 0x1406c6c40
00B62325  44 8A FF                        mov r15b, dil
00B62328  45 3B EE                        cmp r13d, r14d
00B6232B  75 1A                           jne 0x140b62347
00B6232D  40 38 BE 3F 01 00 00            cmp byte ptr [rsi + 0x13f], dil
00B62334  74 2B                           je 0x140b62361
00B62336  48 8D 55 C7                     lea rdx, [rbp - 0x39]
00B6233A  48 8B CE                        mov rcx, rsi
00B6233D  45 8A FE                        mov r15b, r14b
00B62340  E8 13 D8 A0 FF                  call 0x14056fb58
00B62345  EB 17                           jmp 0x140b6235e
00B62347  41 83 FD 02                     cmp r13d, 2
00B6234B  75 14                           jne 0x140b62361
00B6234D  4C 8D 45 C7                     lea r8, [rbp - 0x39]
00B62351  33 D2                           xor edx, edx
00B62353  48 8B CE                        mov rcx, rsi
00B62356  45 8A FE                        mov r15b, r14b
00B62359  E8 A6 FE 96 FF                  call 0x1404d2204
00B6235E  4C 8B E0                        mov r12, rax
00B62361  45 8A C7                        mov r8b, r15b
00B62364  40 38 BE 40 01 00 00            cmp byte ptr [rsi + 0x140], dil
00B6236B  0F 84 A0 00 00 00               je 0x140b62411
00B62371  33 D2                           xor edx, edx
00B62373  E8 84 9F 99 FF                  call 0x1404fc2fc
00B62378  44 8B F8                        mov r15d, eax
00B6237B  E8 10 58 99 FF                  call 0x1404f7b90
00B62380  4C 8B 4D C7                     mov r9, qword ptr [rbp - 0x39]
00B62384  4D 8B C4                        mov r8, r12
00B62387  41 8B D7                        mov edx, r15d
00B6238A  48 8B CE                        mov rcx, rsi
00B6238D  85 C0                           test eax, eax
00B6238F  75 27                           jne 0x140b623b8
00B62391  E8 C6 06 00 00                  call 0x140b62a5c
00B62396  85 C0                           test eax, eax
00B62398  0F 88 6F 05 00 00               js 0x140b6290d
00B6239E  48 8B 56 68                     mov rdx, qword ptr [rsi + 0x68]
00B623A2  48 8D 45 07                     lea rax, [rbp + 7]
00B623A6  45 33 C9                        xor r9d, r9d
00B623A9  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B623AE  45 33 C0                        xor r8d, r8d
00B623B1  E8 E2 ED A0 FF                  call 0x140571198
00B623B6  EB 25                           jmp 0x140b623dd
00B623B8  E8 BB 0A 00 00                  call 0x140b62e78
00B623BD  85 C0                           test eax, eax
00B623BF  0F 88 48 05 00 00               js 0x140b6290d
00B623C5  48 8B 56 68                     mov rdx, qword ptr [rsi + 0x68]
00B623C9  48 8D 45 07                     lea rax, [rbp + 7]
00B623CD  45 33 C9                        xor r9d, r9d
00B623D0  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B623D5  45 33 C0                        xor r8d, r8d
00B623D8  E8 9F 81 99 FF                  call 0x1404fa57c
00B623DD  4C 8B 7E 28                     mov r15, qword ptr [rsi + 0x28]
00B623E1  4D 8D A7 00 10 00 00            lea r12, [r15 + 0x1000]
00B623E8  EB 20                           jmp 0x140b6240a
00B623EA  E8 A1 57 99 FF                  call 0x1404f7b90
00B623EF  48 8D 55 07                     lea rdx, [rbp + 7]
00B623F3  4D 8B C7                        mov r8, r15
00B623F6  85 C0                           test eax, eax
00B623F8  75 07                           jne 0x140b62401
00B623FA  E8 79 FD A0 FF                  call 0x140572178
00B623FF  EB 05                           jmp 0x140b62406
00B62401  E8 0E 04 A1 FF                  call 0x140572814
00B62406  49 83 C7 20                     add r15, 0x20
00B6240A  4D 3B FC                        cmp r15, r12
00B6240D  72 DB                           jb 0x140b623ea
00B6240F  EB 5E                           jmp 0x140b6246f
00B62411  E8 82 A1 99 FF                  call 0x1404fc598
00B62416  4C 8B 4D C7                     mov r9, qword ptr [rbp - 0x39]
00B6241A  48 8D 4D F7                     lea rcx, [rbp - 9]
00B6241E  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00B62423  4D 8B C4                        mov r8, r12
00B62426  48 8B CE                        mov rcx, rsi
00B62429  48 8B D0                        mov rdx, rax
00B6242C  E8 C3 0D 98 FF                  call 0x1404e31f4
00B62431  48 8B 56 28                     mov rdx, qword ptr [rsi + 0x28]
00B62435  4C 8D 8A 00 10 00 00            lea r9, [rdx + 0x1000]
00B6243C  49 3B D1                        cmp rdx, r9
00B6243F  73 2E                           jae 0x140b6246f
00B62441  48 8B 4D F7                     mov rcx, qword ptr [rbp - 9]
00B62445  4C 8B 45 FF                     mov r8, qword ptr [rbp - 1]
00B62449  48 8B C1                        mov rax, rcx
00B6244C  49 23 C6                        and rax, r14
00B6244F  48 85 C0                        test rax, rax
00B62452  74 0A                           je 0x140b6245e
00B62454  4C 89 42 08                     mov qword ptr [rdx + 8], r8
00B62458  90                              nop
00B62459  48 89 0A                        mov qword ptr [rdx], rcx
00B6245C  EB 08                           jmp 0x140b62466
00B6245E  48 89 3A                        mov qword ptr [rdx], rdi
00B62461  90                              nop
00B62462  48 89 7A 08                     mov qword ptr [rdx + 8], rdi
00B62466  48 83 C2 10                     add rdx, 0x10
00B6246A  49 3B D1                        cmp rdx, r9
00B6246D  72 E0                           jb 0x140b6244f
00B6246F  44 8A 7D B7                     mov r15b, byte ptr [rbp - 0x49]
00B62473  48 39 7E 10                     cmp qword ptr [rsi + 0x10], rdi
00B62477  0F 85 85 00 00 00               jne 0x140b62502
00B6247D  48 8B 05 4C D3 42 00            mov rax, qword ptr [rip + 0x42d34c]
00B62484  41 8B D6                        mov edx, r14d
00B62487  48 8B CB                        mov rcx, rbx
00B6248A  E8 41 86 B5 FF                  call 0x1406baad0
00B6248F  48 89 46 18                     mov qword ptr [rsi + 0x18], rax
00B62493  48 85 C0                        test rax, rax
00B62496  0F 84 38 03 00 00               je 0x140b627d4
00B6249C  44 8B 86 10 01 00 00            mov r8d, dword ptr [rsi + 0x110]
00B624A3  41 BC 00 10 00 00               mov r12d, 0x1000
00B624A9  41 8B D4                        mov edx, r12d
00B624AC  48 8B C8                        mov rcx, rax
00B624AF  E8 8C A8 99 FF                  call 0x1404fcd40
00B624B4  48 89 46 10                     mov qword ptr [rsi + 0x10], rax
00B624B8  4C 8B C0                        mov r8, rax
00B624BB  48 85 C0                        test rax, rax
00B624BE  0F 84 10 03 00 00               je 0x140b627d4
00B624C4  48 8B 46 30                     mov rax, qword ptr [rsi + 0x30]
00B624C8  49 8D 88 00 10 00 00            lea rcx, [r8 + 0x1000]
00B624CF  48 99                           cqo
00B624D1  49 F7 FC                        idiv r12
00B624D4  48 C1 E0 0C                     shl rax, 0xc
00B624D8  49 0B C6                        or rax, r14
00B624DB  EB 1E                           jmp 0x140b624fb
00B624DD  49 89 00                        mov qword ptr [r8], rax
00B624E0  40 38 BE 40 01 00 00            cmp byte ptr [rsi + 0x140], dil
00B624E7  75 07                           jne 0x140b624f0
00B624E9  49 83 C0 08                     add r8, 8
00B624ED  49 89 38                        mov qword ptr [r8], rdi
00B624F0  48 8B 4E 10                     mov rcx, qword ptr [rsi + 0x10]
00B624F4  49 83 C0 08                     add r8, 8
00B624F8  49 03 CC                        add rcx, r12
00B624FB  4C 3B C1                        cmp r8, rcx
00B624FE  72 DD                           jb 0x140b624dd
00B62500  EB 06                           jmp 0x140b62508
00B62502  41 BC 00 10 00 00               mov r12d, 0x1000
00B62508  48 39 7E 20                     cmp qword ptr [rsi + 0x20], rdi
00B6250C  75 43                           jne 0x140b62551
00B6250E  48 8B 05 BB D2 42 00            mov rax, qword ptr [rip + 0x42d2bb]
00B62515  41 8B D6                        mov edx, r14d
00B62518  48 8B CB                        mov rcx, rbx
00B6251B  E8 B0 85 B5 FF                  call 0x1406baad0
00B62520  48 85 C0                        test rax, rax
00B62523  0F 84 AB 02 00 00               je 0x140b627d4
00B62529  45 8B C6                        mov r8d, r14d
00B6252C  49 8B D4                        mov rdx, r12
00B6252F  48 8B C8                        mov rcx, rax
00B62532  E8 09 A8 99 FF                  call 0x1404fcd40
00B62537  48 89 46 20                     mov qword ptr [rsi + 0x20], rax
00B6253B  48 85 C0                        test rax, rax
00B6253E  0F 84 90 02 00 00               je 0x140b627d4
00B62544  4D 8B C4                        mov r8, r12
00B62547  33 D2                           xor edx, edx
00B62549  48 8B C8                        mov rcx, rax
00B6254C  E8 EF 46 B6 FF                  call 0x1406c6c40
00B62551  41 83 FD 02                     cmp r13d, 2
00B62555  75 25                           jne 0x140b6257c
00B62557  45 84 FF                        test r15b, r15b
00B6255A  75 20                           jne 0x140b6257c
00B6255C  E8 2F 56 99 FF                  call 0x1404f7b90
00B62561  48 8B CE                        mov rcx, rsi
00B62564  85 C0                           test eax, eax
00B62566  75 07                           jne 0x140b6256f
00B62568  E8 D7 03 00 00                  call 0x140b62944
00B6256D  EB 05                           jmp 0x140b62574
00B6256F  E8 C0 06 00 00                  call 0x140b62c34
00B62574  85 C0                           test eax, eax
00B62576  0F 88 58 02 00 00               js 0x140b627d4
00B6257C  48 8B 46 18                     mov rax, qword ptr [rsi + 0x18]
00B62580  8A 8E 40 01 00 00               mov cl, byte ptr [rsi + 0x140]
00B62586  48 99                           cqo
00B62588  49 F7 FC                        idiv r12
00B6258B  48 C1 E0 0C                     shl rax, 0xc
00B6258F  F6 D9                           neg cl
00B62591  48 8B 4E 08                     mov rcx, qword ptr [rsi + 8]
00B62595  48 1B D2                        sbb rdx, rdx
00B62598  81 E2 00 04 00 00               and edx, 0x400
00B6259E  48 0B C2                        or rax, rdx
00B625A1  48 89 41 20                     mov qword ptr [rcx + 0x20], rax
00B625A5  F0 09 3C 24                     lock or dword ptr [rsp], edi
00B625A9  45 8A C6                        mov r8b, r14b
00B625AC  BA 00 00 00 40                  mov edx, 0x40000000
00B625B1  48 8B CE                        mov rcx, rsi
00B625B4  E8 9B 02 A1 FF                  call 0x140572854
00B625B9  EB 06                           jmp 0x140b625c1
00B625BB  41 BC 00 10 00 00               mov r12d, 0x1000
00B625C1  44 8B FF                        mov r15d, edi
00B625C4  41 83 FF 02                     cmp r15d, 2
00B625C8  0F 83 FD 00 00 00               jae 0x140b626cb
00B625CE  45 3B FE                        cmp r15d, r14d
00B625D1  75 23                           jne 0x140b625f6
00B625D3  45 85 ED                        test r13d, r13d
00B625D6  0F 84 E7 00 00 00               je 0x140b626c3
00B625DC  40 38 BE 40 01 00 00            cmp byte ptr [rsi + 0x140], dil
00B625E3  0F 84 DA 00 00 00               je 0x140b626c3
00B625E9  40 38 BE 3C 01 00 00            cmp byte ptr [rsi + 0x13c], dil
00B625F0  0F 84 CD 00 00 00               je 0x140b626c3
00B625F6  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
00B625FA  45 3B FE                        cmp r15d, r14d
00B625FD  90                              nop
00B625FE  45 8B CF                        mov r9d, r15d
00B62601  8B 00                           mov eax, dword ptr [rax]
00B62603  B8 00 80 00 00                  mov eax, 0x8000
00B62608  41 0F 45 C4                     cmovne eax, r12d
00B6260C  44 8B E0                        mov r12d, eax
00B6260F  41 0F BD C4                     bsr eax, r12d
00B62613  89 45 BF                        mov dword ptr [rbp - 0x41], eax
00B62616  49 8D 41 04                     lea rax, [r9 + 4]
00B6261A  48 C1 E0 05                     shl rax, 5
00B6261E  4C 89 24 30                     mov qword ptr [rax + rsi], r12
00B62622  41 8B C7                        mov eax, r15d
00B62625  48 C1 E0 05                     shl rax, 5
00B62629  48 89 45 EF                     mov qword ptr [rbp - 0x11], rax
00B6262D  4C 8D 2C 30                     lea r13, [rax + rsi]
00B62631  48 39 7C 30 70                  cmp qword ptr [rax + rsi + 0x70], rdi
00B62636  75 52                           jne 0x140b6268a
00B62638  48 8B 05 91 D1 42 00            mov rax, qword ptr [rip + 0x42d191]
00B6263F  41 8B D4                        mov edx, r12d
00B62642  C1 EA 0C                        shr edx, 0xc
00B62645  48 8B CB                        mov rcx, rbx
00B62648  E8 83 84 B5 FF                  call 0x1406baad0
00B6264D  49 89 45 78                     mov qword ptr [r13 + 0x78], rax
00B62651  48 85 C0                        test rax, rax
00B62654  0F 84 7A 01 00 00               je 0x140b627d4
00B6265A  45 8B C6                        mov r8d, r14d
00B6265D  41 8B D4                        mov edx, r12d
00B62660  48 8B C8                        mov rcx, rax
00B62663  E8 D8 A6 99 FF                  call 0x1404fcd40
00B62668  48 8B 4D EF                     mov rcx, qword ptr [rbp - 0x11]
00B6266C  48 89 44 31 70                  mov qword ptr [rcx + rsi + 0x70], rax
00B62671  48 85 C0                        test rax, rax
00B62674  0F 84 5A 01 00 00               je 0x140b627d4
00B6267A  45 8B C4                        mov r8d, r12d
00B6267D  33 D2                           xor edx, edx
00B6267F  48 8B C8                        mov rcx, rax
00B62682  E8 B9 45 B6 FF                  call 0x1406c6c40
00B62687  45 8B CF                        mov r9d, r15d
00B6268A  49 8B 45 78                     mov rax, qword ptr [r13 + 0x78]
00B6268E  41 BC 00 10 00 00               mov r12d, 0x1000
00B62694  42 8B 4C CD DF                  mov ecx, dword ptr [rbp + r9*8 - 0x21]
00B62699  48 99                           cqo
00B6269B  44 8B 45 BF                     mov r8d, dword ptr [rbp - 0x41]
00B6269F  81 E1 F8 0F 00 00               and ecx, 0xff8
00B626A5  44 8B 6D CF                     mov r13d, dword ptr [rbp - 0x31]
00B626A9  41 83 C0 FC                     add r8d, -4
00B626AD  49 F7 FC                        idiv r12
00B626B0  41 83 E0 07                     and r8d, 7
00B626B4  48 C1 E0 0C                     shl rax, 0xc
00B626B8  48 0B C1                        or rax, rcx
00B626BB  49 33 C0                        xor rax, r8
00B626BE  4A 89 44 CD DF                  mov qword ptr [rbp + r9*8 - 0x21], rax
00B626C3  45 03 FE                        add r15d, r14d
00B626C6  E9 F9 FE FF FF                  jmp 0x140b625c4
00B626CB  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
00B626CF  48 89 B8 88 00 00 00            mov qword ptr [rax + 0x88], rdi
00B626D6  F0 09 3C 24                     lock or dword ptr [rsp], edi
00B626DA  48 8B 4D DF                     mov rcx, qword ptr [rbp - 0x21]
00B626DE  40 38 BE 40 01 00 00            cmp byte ptr [rsi + 0x140], dil
00B626E5  74 09                           je 0x140b626f0
00B626E7  48 0F BA E9 0B                  bts rcx, 0xb
00B626EC  48 89 4D DF                     mov qword ptr [rbp - 0x21], rcx
00B626F0  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
00B626F4  48 89 88 90 00 00 00            mov qword ptr [rax + 0x90], rcx
00B626FB  F0 09 3C 24                     lock or dword ptr [rsp], edi
00B626FF  44 8B 65 D3                     mov r12d, dword ptr [rbp - 0x2d]
00B62703  45 85 E4                        test r12d, r12d
00B62706  0F 84 56 01 00 00               je 0x140b62862
00B6270C  45 3B E6                        cmp r12d, r14d
00B6270F  75 1C                           jne 0x140b6272d
00B62711  48 8B 05 A8 D0 42 00            mov rax, qword ptr [rip + 0x42d0a8]
00B62718  48 89 86 20 01 00 00            mov qword ptr [rsi + 0x120], rax
00B6271F  48 8B 05 A2 D0 42 00            mov rax, qword ptr [rip + 0x42d0a2]
00B62726  48 89 86 28 01 00 00            mov qword ptr [rsi + 0x128], rax
00B6272D  48 39 BE 20 01 00 00            cmp qword ptr [rsi + 0x120], rdi
00B62734  0F 85 A4 00 00 00               jne 0x140b627de
00B6273A  44 8B 7D BB                     mov r15d, dword ptr [rbp - 0x45]
00B6273E  48 8B CB                        mov rcx, rbx
00B62741  48 8B 05 88 D0 42 00            mov rax, qword ptr [rip + 0x42d088]
00B62748  41 C1 E7 04                     shl r15d, 4
00B6274C  41 81 C7 FF 0F 00 00            add r15d, 0xfff
00B62753  41 81 E7 00 F0 FF FF            and r15d, 0xfffff000
00B6275A  41 8B D7                        mov edx, r15d
00B6275D  C1 EA 0C                        shr edx, 0xc
00B62760  E8 6B 83 B5 FF                  call 0x1406baad0
00B62765  48 89 86 28 01 00 00            mov qword ptr [rsi + 0x128], rax
00B6276C  48 85 C0                        test rax, rax
00B6276F  74 63                           je 0x140b627d4
00B62771  44 8B 86 10 01 00 00            mov r8d, dword ptr [rsi + 0x110]
00B62778  48 8B C8                        mov rcx, rax
00B6277B  41 8B D7                        mov edx, r15d
00B6277E  41 8B DF                        mov ebx, r15d
00B62781  E8 BA A5 99 FF                  call 0x1404fcd40
00B62786  48 89 86 20 01 00 00            mov qword ptr [rsi + 0x120], rax
00B6278D  48 85 C0                        test rax, rax
00B62790  74 42                           je 0x140b627d4
00B62792  44 8B C3                        mov r8d, ebx
00B62795  33 D2                           xor edx, edx
00B62797  48 8B C8                        mov rcx, rax
00B6279A  E8 A1 44 B6 FF                  call 0x1406c6c40
00B6279F  8B 4D BB                        mov ecx, dword ptr [rbp - 0x45]
00B627A2  89 8E 30 01 00 00               mov dword ptr [rsi + 0x130], ecx
00B627A8  45 3B E6                        cmp r12d, r14d
00B627AB  75 34                           jne 0x140b627e1
00B627AD  48 39 3D 0C D0 42 00            cmp qword ptr [rip + 0x42d00c], rdi
00B627B4  75 2B                           jne 0x140b627e1
00B627B6  48 8B 86 20 01 00 00            mov rax, qword ptr [rsi + 0x120]
00B627BD  48 89 05 FC CF 42 00            mov qword ptr [rip + 0x42cffc], rax
00B627C4  48 8B 86 28 01 00 00            mov rax, qword ptr [rsi + 0x128]
00B627CB  48 89 05 F6 CF 42 00            mov qword ptr [rip + 0x42cff6], rax
00B627D2  EB 0D                           jmp 0x140b627e1
00B627D4  B8 01 00 00 C0                  mov eax, 0xc0000001
00B627D9  E9 2F 01 00 00                  jmp 0x140b6290d
00B627DE  8B 4D BB                        mov ecx, dword ptr [rbp - 0x45]
00B627E1  48 8B 86 28 01 00 00            mov rax, qword ptr [rsi + 0x128]
00B627E8  41 B8 00 10 00 00               mov r8d, 0x1000
00B627EE  48 99                           cqo
00B627F0  49 F7 F8                        idiv r8
00B627F3  0F BD C9                        bsr ecx, ecx
00B627F6  48 8B D8                        mov rbx, rax
00B627F9  48 C1 E3 0C                     shl rbx, 0xc
00B627FD  89 4D D7                        mov dword ptr [rbp - 0x29], ecx
00B62800  8D 41 FF                        lea eax, [rcx - 1]
00B62803  83 E0 0F                        and eax, 0xf
00B62806  48 0B D8                        or rbx, rax
00B62809  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
00B6280D  48 0F BA EB 0B                  bts rbx, 0xb
00B62812  48 89 98 B8 00 00 00            mov qword ptr [rax + 0xb8], rbx
00B62819  F0 09 3C 24                     lock or dword ptr [rsp], edi
00B6281D  B9 64 00 00 00                  mov ecx, 0x64
00B62822  E8 F9 CD 8E FF                  call 0x14044f620
00B62827  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
00B6282B  90                              nop
00B6282C  48 8B 80 B8 00 00 00            mov rax, qword ptr [rax + 0xb8]
00B62833  48 3B C3                        cmp rax, rbx
00B62836  74 1A                           je 0x140b62852
00B62838  45 33 C9                        xor r9d, r9d
00B6283B  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00B62840  45 33 C0                        xor r8d, r8d
00B62843  BA 00 70 00 00                  mov edx, 0x7000
00B62848  41 8D 49 5C                     lea ecx, [r9 + 0x5c]
00B6284C  E8 0F AE 99 FF                  call 0x1404fd660
00B62851  CC                              int3
00B62852  45 8A C6                        mov r8b, r14b
00B62855  BA 00 00 00 01                  mov edx, 0x1000000
00B6285A  48 8B CE                        mov rcx, rsi
00B6285D  E8 F2 FF A0 FF                  call 0x140572854
00B62862  45 85 ED                        test r13d, r13d
00B62865  74 4B                           je 0x140b628b2
00B62867  40 38 BE 40 01 00 00            cmp byte ptr [rsi + 0x140], dil
00B6286E  74 3A                           je 0x140b628aa
00B62870  40 38 BE 3C 01 00 00            cmp byte ptr [rsi + 0x13c], dil
00B62877  74 31                           je 0x140b628aa
00B62879  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
00B6287D  48 89 B8 C0 00 00 00            mov qword ptr [rax + 0xc0], rdi
00B62884  F0 09 3C 24                     lock or dword ptr [rsp], edi
00B62888  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
00B6288C  48 89 B8 C8 00 00 00            mov qword ptr [rax + 0xc8], rdi
00B62893  F0 09 3C 24                     lock or dword ptr [rsp], edi
00B62897  48 8B 4E 08                     mov rcx, qword ptr [rsi + 8]
00B6289B  48 8B 45 E7                     mov rax, qword ptr [rbp - 0x19]
00B6289F  48 89 81 D0 00 00 00            mov qword ptr [rcx + 0xd0], rax
00B628A6  F0 09 3C 24                     lock or dword ptr [rsp], edi
00B628AA  48 8B CE                        mov rcx, rsi
00B628AD  E8 8A DC A0 FF                  call 0x14057053c
00B628B2  48 39 BE B8 00 00 00            cmp qword ptr [rsi + 0xb8], rdi
00B628B9  75 40                           jne 0x140b628fb
00B628BB  48 8D 8E B0 00 00 00            lea rcx, [rsi + 0xb0]
00B628C2  E8 39 7C 6D FF                  call 0x14023a500
00B628C7  8B 8E C8 00 00 00               mov ecx, dword ptr [rsi + 0xc8]
00B628CD  48 89 86 B8 00 00 00            mov qword ptr [rsi + 0xb8], rax
00B628D4  83 E1 03                        and ecx, 3
00B628D7  48 83 E0 FC                     and rax, 0xfffffffffffffffc
00B628DB  48 0B C1                        or rax, rcx
00B628DE  48 89 86 C8 00 00 00            mov qword ptr [rsi + 0xc8], rax
00B628E5  48 8B 86 C0 00 00 00            mov rax, qword ptr [rsi + 0xc0]
00B628EC  48 83 E0 F5                     and rax, 0xfffffffffffffff5
00B628F0  48 83 C8 65                     or rax, 0x65
00B628F4  48 89 86 C0 00 00 00            mov qword ptr [rsi + 0xc0], rax
00B628FB  BA 00 00 00 04                  mov edx, 0x4000000
00B62900  45 8A C6                        mov r8b, r14b
00B62903  48 8B CE                        mov rcx, rsi
00B62906  E8 49 FF A0 FF                  call 0x140572854
00B6290B  33 C0                           xor eax, eax
00B6290D  48 8B 4D 27                     mov rcx, qword ptr [rbp + 0x27]
00B62911  48 33 CC                        xor rcx, rsp
00B62914  E8 27 9D B4 FF                  call 0x1406ac640
00B62919  4C 8D 9C 24 D0 00 00 00         lea r11, [rsp + 0xd0]
00B62921  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
00B62925  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
00B62929  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
00B6292D  49 8B E3                        mov rsp, r11
00B62930  41 5F                           pop r15
00B62932  41 5E                           pop r14
00B62934  41 5D                           pop r13
00B62936  41 5C                           pop r12
00B62938  5D                              pop rbp
00B62939  C3                              ret
00B6293A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IvtInitializeIommu(__int64 a1, int a2, unsigned __int8 a3)
{
    __int64 result;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int8 v_stack_mC8;
    unsigned __int8 v_stack_mD0;
    unsigned int v_stack_mD8;
    unsigned int v_stack_mF8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (208);
    result = (*(unsigned __int64 *)(v_rip + 2787126)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 95 + 39) = result;
    v_rdi = 0;
    *(unsigned int *)(v_rsp - 95 - 69) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 304)));
    v_rbx = (v_rbx) | (-1);
    *(unsigned int *)(v_rsp - 95 - 45) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 312)));
    *(unsigned __int8 *)(v_rsp - 95 - 73) = a3;
    *(unsigned int *)(v_rsp - 95 - 65) = 0;
    *(unsigned int *)(v_rsp - 95 - 41) = 0;
    *(unsigned int *)(v_rsp - 95 - 49) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 308)));
    *(unsigned __int64 *)(v_rsp - 95 - 57) = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 33) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 95 - 9) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 95 + 7) = v_xmm1;
    *(unsigned __int64 *)(v_rsp - 95 + 23) = v_xmm1;
    if (a2 == 0) goto loc_00B62138;
    if (a2 != 3) goto loc_00B6290B;
    result = (unsigned int)(*(unsigned int *)(a1 + 312));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 312))) != 0) {
        a2 = 0;
        result = IvtInvalidateRemappingTableEntries(a1, a2, a3, a4);
        a3 = (unsigned __int8)(v_rdi + 1);
        a2 = 0x2000000ULL;
        a1 = a1;
        result = IvtUpdateGlobalCommand(a1, a2, a3, a4);
    }
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 308))) == 0) goto loc_00B6290B;
    result = Feature_Test57481295__private_IsEnabledDeviceUsageNoInline(a1, a2, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_00B620B0;
    result = IvtInvalidateAllContextEntries(a1, a2, a3, a4);
    goto loc_00B620B5;
loc_00B620B0:
    result = IvtInvalidateAllContextEntries(a1, a2, a3, a4);
loc_00B620B5:
    if ((*(unsigned __int8 *)(a1 + 320)) != 0) {
        a2 = (unsigned int)((a2) | (0xFFFFFFFFULL));
        v_stack_mC8 = 0;
        a4 = a2;
        v_stack_mD0 = 0;
        a3 = (unsigned int)(0x10000ULL);
        v_stack_mD8 = 0;
        a1 = a1;
        result = IvtInvalidateScalableModePasidCache(a1, a2, a3, a4);
    }
    result = Feature_Test57481295__private_IsEnabledDeviceUsageNoInline(a1, a2, a3, a4);
    a2 = 0;
    if ((unsigned int)(result) != 0) goto loc_00B6210B;
    v_stack_mC0 = 0;
    v_stack_mC8 = 0;
    a3 = 0;
    v_stack_mD0 = 0;
    v_stack_mD8 = 0;
    result = IvtLegacyFlushTbInternal(a1, a2, a3, (unsigned __int8)(v_rdi + 1));
    goto loc_00B6212E;
loc_00B6210B:
    v_stack_mB8 = 0;
    a4 = 0;
    v_stack_mC0 = 0;
    a3 = 0;
    v_stack_mC8 = 0;
    v_stack_mD0 = 0;
    v_stack_mD8 = (unsigned __int8)(v_rdi + 1);
    result = IvtFlushTbInternal(a1, a2, a3, a4);
loc_00B6212E:
    goto loc_00B62900;
loc_00B62138:
    a2 = 0;
    v_stack_mD8 = v_rip + 4380303;
    result = HalSocRequestApi(a1, a2, a2 + 4, a2 + 8);
    if (sign_flag) goto loc_00B6290D;
    if (*(unsigned __int64 *)(a1 + 8) != 0) goto loc_00B62181;
    a3 = 0;
    result = HalMapIoSpace(*(unsigned __int64 *)(a1), 544, a3, a2 + 8);
    *(unsigned __int64 *)(a1 + 8) = result;
    if (result == 0) goto loc_00B627D4;
loc_00B62181:
    *(unsigned int *)(result + 56) = (unsigned int)((unsigned int)(0x80000000ULL));
    a3 = 0;
    result = IvtUpdateGlobalCommand(a1, (unsigned int)(0x4000000ULL), a3, a2 + 8);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 52))) != 0) {
        a1 = *(unsigned __int64 *)(a1 + 8);
        *(unsigned int *)(a1 + 52) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 52)));
    }
    if ((*(unsigned __int8 *)(a1 + 320)) == 0) goto loc_00B62202;
    result = (unsigned int)(*(unsigned int *)(a1 + 224));
    if ((*(unsigned __int8 *)(a1 + 320)) < 0) {
        result = *(unsigned __int64 *)(a1 + 8);
        a2 = 224;
        a1 = *(unsigned int *)(result + a2 * 1);
        result = *(unsigned __int64 *)(a1 + 8);
        a1 = (unsigned int)((a1) | ((unsigned int)((unsigned int)(0x80000000ULL))));
        *(unsigned int *)(result + a2 * 1) = (unsigned int)(a1);
        result = *(unsigned __int64 *)(a1 + 8);
        a2 = 220;
        a1 = *(unsigned int *)(result + a2 * 1);
        result = *(unsigned __int64 *)(a1 + 8);
        a1 = (unsigned int)((a1) | (3));
        *(unsigned int *)(result + a2 * 1) = (unsigned int)(a1);
    }
    a3 = 0;
    result = IvtUpdateGlobalCommand(a1, (unsigned int)(0x2000000ULL), a3, a2 + 8);
    if ((*(unsigned __int8 *)(a1 + 320)) == 0) goto loc_00B62235;
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 28));
    if (sign_flag) {
        a3 = 0;
        a2 = (unsigned int)((unsigned int)(0x80000000ULL));
        a1 = a1;
        result = IvtUpdateGlobalCommand(a1, a2, a3, a2 + 8);
    }
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 308))) == 0) goto loc_00B625BB;
    if ((*(unsigned __int8 *)(a1 + 319)) == 0) goto loc_00B62266;
    if ((*(unsigned __int64 *)(a1 + 336)) != 0) goto loc_00B62266;
    result = IvtInitializeIdentityMappings(a1, a2, a3, a2 + 8);
    if (sign_flag) goto loc_00B627D4;
loc_00B62266:
    if ((*(unsigned __int64 *)(a1 + 40)) != 0) goto loc_00B62473;
    result = guard_dispatch_icall(v_rbx, 1, a3, a2 + 8);
    *(unsigned __int64 *)(a1 + 48) = result;
    if (result == 0) goto loc_00B627D4;
    result = HalMapIoSpace(result, (unsigned int)((unsigned int)((unsigned int)(0x1000ULL))), (unsigned int)(*(unsigned int *)(a1 + 272)), a2 + 8);
    *(unsigned __int64 *)(a1 + 40) = result;
    if (result == 0) goto loc_00B627D4;
    result = Feature_Test57481295__private_IsEnabledDeviceUsageNoInline(result, (unsigned int)((unsigned int)((unsigned int)(0x1000ULL))), (unsigned int)(*(unsigned int *)(a1 + 272)), a2 + 8);
    if ((unsigned int)(result) != 0) {
        a1 = *(unsigned __int64 *)(a1 + 40);
        a3 = (unsigned int)((unsigned int)(0x1000ULL));
        a2 = 0;
        result = memset(a1, a2, a3, a2 + 8);
    }
    if ((*(unsigned __int64 *)(v_rip + 3160046)) != 0) goto loc_00B62325;
    result = guard_dispatch_icall(v_rbx, 1, a3, a2 + 8);
    *(unsigned __int64 *)(v_rip + 4379851) = result;
    if (result == 0) goto loc_00B627D4;
    result = HalMapIoSpace(result, (unsigned int)(0x1000ULL), (unsigned int)(*(unsigned int *)(a1 + 272)), a2 + 8);
    *(unsigned __int64 *)(v_rip + 3159985) = result;
    if (result == 0) goto loc_00B627D4;
    a2 = 0;
    result = memset(result, a2, (unsigned int)(0x1000ULL), a2 + 8);
loc_00B62325:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 308)))) != 1) goto loc_00B62347;
    if ((*(unsigned __int8 *)(a1 + 319)) == 0) goto loc_00B62361;
    result = IvtGetIdentityMappedDomain(a1, v_rsp - 95 - 57, (unsigned int)(0x1000ULL), a2 + 8);
    goto loc_00B6235E;
loc_00B62347:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 308)))) != 2) goto loc_00B62361;
    a2 = 0;
    result = IvtGetBlockedDomain(a1, a2, v_rsp - 95 - 57, a2 + 8);
loc_00B6235E:
loc_00B62361:
    if ((*(unsigned __int8 *)(a1 + 320)) == 0) goto loc_00B62411;
    a2 = 0;
    result = IvtGetPasidGranularTranslationType(a1, a2, 1, a2 + 8);
    result = Feature_Test57481295__private_IsEnabledDeviceUsageNoInline(a1, a2, 1, a2 + 8);
    if ((unsigned int)(result) != 0) goto loc_00B623B8;
    result = IvtLegacySetupScalableModeDefaultPasidTables(a1, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), result, *(unsigned __int64 *)(v_rsp - 95 - 57));
    if (sign_flag) goto loc_00B6290D;
    a4 = 0;
    v_stack_mD0 = v_rsp - 95 + 7;
    a3 = 0;
    result = IvtLegacyBuildScalableModeContextEntry(a1, *(unsigned __int64 *)(a1 + 104), a3, a4);
    goto loc_00B623DD;
loc_00B623B8:
    result = IvtSetupScalableModeDefaultPasidTables(a1, *(unsigned __int64 *)(a1 + 104), a3, a4);
    if (sign_flag) goto loc_00B6290D;
    a4 = 0;
    v_stack_mD0 = v_rsp - 95 + 7;
    a3 = 0;
    result = IvtBuildScalableModeContextEntry(a1, *(unsigned __int64 *)(a1 + 104), a3, a4);
loc_00B623DD:
    goto loc_00B6240A;
loc_00B623EA:
    result = Feature_Test57481295__private_IsEnabledDeviceUsageNoInline(a1, *(unsigned __int64 *)(a1 + 104), a3, a4);
    if ((unsigned int)(result) != 0) goto loc_00B62401;
    result = IvtLegacySetScalableModeContextEntry(a1, v_rsp - 95 + 7, *(unsigned __int64 *)(a1 + 40), a4);
    goto loc_00B62406;
loc_00B62401:
    result = IvtSetScalableModeContextEntry(a1, v_rsp - 95 + 7, *(unsigned __int64 *)(a1 + 40), a4);
loc_00B62406:
    v_r15 = (*(unsigned __int64 *)(a1 + 40)) + (32);
loc_00B6240A:
    if (v_r15 < (*(unsigned __int64 *)(a1 + 40) + 4096)) goto loc_00B623EA;
    goto loc_00B6246F;
loc_00B62411:
    result = IvtGetContextEntryType(a1, v_rsp - 95 + 7, *(unsigned __int64 *)(a1 + 40), a4);
    v_stack_mD8 = v_rsp - 95 - 9;
    result = IvtBuildContextEntry(a1, result, *(unsigned __int64 *)(a1 + 40) + 4096, *(unsigned __int64 *)(v_rsp - 95 - 57));
    if ((*(unsigned __int64 *)(a1 + 40)) >= (*(unsigned __int64 *)(a1 + 40) + 4096)) goto loc_00B6246F;
    result = (*(unsigned __int64 *)(v_rsp - 95 - 9)) & (1);
loc_00B6244F:
    if (result == 0) goto loc_00B6245E;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8) = *(unsigned __int64 *)(v_rsp - 95 - 1);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40)) = *(unsigned __int64 *)(v_rsp - 95 - 9);
    goto loc_00B62466;
loc_00B6245E:
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40)) = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8) = 0;
loc_00B62466:
    a2 = (*(unsigned __int64 *)(a1 + 40)) + (16);
    if (a2 < (*(unsigned __int64 *)(a1 + 40) + 4096)) goto loc_00B6244F;
loc_00B6246F:
loc_00B62473:
    if ((*(unsigned __int64 *)(a1 + 16)) != 0) goto loc_00B62502;
    result = guard_dispatch_icall(v_rbx, 1, *(unsigned __int64 *)(v_rsp - 95 - 1), *(unsigned __int64 *)(a1 + 40) + 4096);
    *(unsigned __int64 *)(a1 + 24) = result;
    if (result == 0) goto loc_00B627D4;
    result = HalMapIoSpace(result, (unsigned int)((unsigned int)((unsigned int)(0x1000ULL))), (unsigned int)(*(unsigned int *)(a1 + 272)), *(unsigned __int64 *)(a1 + 40) + 4096);
    *(unsigned __int64 *)(a1 + 16) = result;
    if (result == 0) goto loc_00B627D4;
    result = (*(unsigned __int64 *)(a1 + 48)) << (12);
    result = (result) | (1);
    goto loc_00B624FB;
loc_00B624DD:
    *(unsigned __int64 *)(result) = result;
    if ((*(unsigned __int8 *)(a1 + 320)) == 0) {
        a3 = (result) + (8);
        *(unsigned __int64 *)(a3) = 0;
    }
    a3 = (a3) + (8);
    a1 = (*(unsigned __int64 *)(a1 + 16)) + ((unsigned int)(0x1000ULL));
loc_00B624FB:
    if (a3 < a1) goto loc_00B624DD;
    goto loc_00B62508;
loc_00B62502:
loc_00B62508:
    if ((*(unsigned __int64 *)(a1 + 32)) != 0) goto loc_00B62551;
    result = guard_dispatch_icall(v_rbx, 1, a3, *(unsigned __int64 *)(a1 + 40) + 4096);
    if (result == 0) goto loc_00B627D4;
    result = HalMapIoSpace(result, (unsigned int)(0x1000ULL), 1, *(unsigned __int64 *)(a1 + 40) + 4096);
    *(unsigned __int64 *)(a1 + 32) = result;
    if (result == 0) goto loc_00B627D4;
    a2 = 0;
    result = memset(result, a2, (unsigned int)(0x1000ULL), *(unsigned __int64 *)(a1 + 40) + 4096);
loc_00B62551:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 308)))) != 2) goto loc_00B6257C;
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rsp - 95 - 73)) != 0) goto loc_00B6257C;
    result = Feature_Test57481295__private_IsEnabledDeviceUsageNoInline(result, a2, (unsigned int)(0x1000ULL), *(unsigned __int64 *)(a1 + 40) + 4096);
    if ((unsigned int)(result) != 0) goto loc_00B6256F;
    result = IvtLegacyProcessDeviceExceptions(a1, a2, (unsigned int)(0x1000ULL), *(unsigned __int64 *)(a1 + 40) + 4096);
    goto loc_00B62574;
loc_00B6256F:
    result = IvtProcessDeviceExceptions(a1, a2, (unsigned int)(0x1000ULL), *(unsigned __int64 *)(a1 + 40) + 4096);
loc_00B62574:
    if (sign_flag) goto loc_00B627D4;
loc_00B6257C:
    result = (*(unsigned __int64 *)(a1 + 24)) << (12);
    a1 = (unsigned __int8)(-(*(unsigned __int8 *)(a1 + 320)));
    a2 = (unsigned int)((a2) & (0x400ULL));
    result = (result) | (a2);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) = result;
    result = IvtUpdateGlobalCommand(a1, (unsigned int)(0x40000000ULL), 1, *(unsigned __int64 *)(a1 + 40) + 4096);
    goto loc_00B625C1;
loc_00B625BB:
loc_00B625C1:
loc_00B625C4:
    if (0 >= 2) goto loc_00B626CB;
    if (0 != 1) goto loc_00B625F6;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 308))) == 0) goto loc_00B626C3;
    if ((*(unsigned __int8 *)(a1 + 320)) == 0) goto loc_00B626C3;
    if ((*(unsigned __int8 *)(a1 + 316)) == 0) goto loc_00B626C3;
loc_00B625F6:
    result = (unsigned int)(0x8000ULL);
    if (0 != 1) { result = (unsigned int)((unsigned int)(0x1000ULL)); }
    *(unsigned int *)(v_rsp - 95 - 65) = (unsigned int)(result);
    result = (0 + 4) << (5);
    *(unsigned __int64 *)(result + a1 * 1) = (unsigned int)((unsigned int)(result));
    result = (0) << (5);
    *(unsigned __int64 *)(v_rsp - 95 - 17) = result;
    if ((*(unsigned __int64 *)(result + a1 * 1 + 112)) != 0) goto loc_00B6268A;
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))))) >> (12));
    result = guard_dispatch_icall(v_rbx, a2, 1, 0);
    *(unsigned __int64 *)(result + a1 * 1 + 120) = result;
    if (result == 0) goto loc_00B627D4;
    result = HalMapIoSpace(result, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), 1, 0);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 - 17) + a1 * 1 + 112) = result;
    if (result == 0) goto loc_00B627D4;
    a2 = 0;
    result = memset(result, a2, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), 0);
loc_00B6268A:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 95 + 0 * 8 - 33))) & (0xFF8ULL));
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 95 - 65))) + (-4));
    a3 = (unsigned int)((a3) & (7));
    result = (*(unsigned __int64 *)(result + a1 * 1 + 120)) << (12);
    result = (result) | (a1);
    result = (result) ^ (a3);
    *(unsigned __int64 *)(v_rsp - 95 + 0 * 8 - 33) = result;
loc_00B626C3:
    v_r15 = (unsigned int)((0) + (1));
    goto loc_00B625C4;
loc_00B626CB:
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 136) = 0;
    if ((*(unsigned __int8 *)(a1 + 320)) != 0) {
        *(unsigned __int64 *)(v_rsp - 95 - 33) = *(unsigned __int64 *)(v_rsp - 95 - 33);
    }
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 144) = *(unsigned __int64 *)(v_rsp - 95 - 33);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 45))) == 0) goto loc_00B62862;
    result = *(unsigned __int64 *)(a1 + 8);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 45)))) == 1) {
        result = *(unsigned __int64 *)(v_rip + 4378792);
        *(unsigned __int64 *)(a1 + 288) = result;
        result = *(unsigned __int64 *)(v_rip + 4378786);
        *(unsigned __int64 *)(a1 + 296) = result;
    }
    if ((*(unsigned __int64 *)(a1 + 288)) != 0) goto loc_00B627DE;
    v_r15 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 95 - 69))) << (4));
    v_r15 = (unsigned int)((v_r15) + (0xFFFULL));
    v_r15 = (unsigned int)((v_r15) & (0xFFFFF000ULL));
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_r15))) >> (12));
    result = guard_dispatch_icall(v_rbx, a2, a3, 0);
    *(unsigned __int64 *)(a1 + 296) = result;
    if (result == 0) goto loc_00B627D4;
    result = HalMapIoSpace(result, (unsigned int)((unsigned int)(v_r15)), (unsigned int)(*(unsigned int *)(a1 + 272)), 0);
    *(unsigned __int64 *)(a1 + 288) = result;
    if (result == 0) goto loc_00B627D4;
    a2 = 0;
    result = memset(result, a2, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r15)))), 0);
    *(unsigned int *)(a1 + 304) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 69)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 45)))) != 1) goto loc_00B627E1;
    if ((*(unsigned __int64 *)(v_rip + 4378636)) != 0) goto loc_00B627E1;
    *(unsigned __int64 *)(v_rip + 4378620) = *(unsigned __int64 *)(a1 + 288);
    *(unsigned __int64 *)(v_rip + 4378614) = *(unsigned __int64 *)(a1 + 296);
    goto loc_00B627E1;
loc_00B627D4:
    goto loc_00B6290D;
loc_00B627DE:
loc_00B627E1:
    v_rbx = (*(unsigned __int64 *)(a1 + 296)) << (12);
    *(unsigned int *)(v_rsp - 95 - 41) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 69)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 95 - 69)) - 1) & (15));
    v_rbx = (v_rbx) | (result);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 184) = v_rbx;
    result = KeStallExecutionProcessor(100, a2, (unsigned int)(0x1000ULL), 0);
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 184);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 184)) != v_rbx) {
        a4 = 0;
        v_stack_mD8 = 0;
        a3 = 0;
        a2 = 0x7000ULL;
        a1 = a4 + 92;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    result = IvtUpdateGlobalCommand(a1, (unsigned int)(0x1000000ULL), 1, a4);
loc_00B62862:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 49))) == 0) goto loc_00B628B2;
    if ((*(unsigned __int8 *)(a1 + 320)) == 0) goto loc_00B628AA;
    if ((*(unsigned __int8 *)(a1 + 316)) != 0) {
        result = *(unsigned __int64 *)(a1 + 8);
        *(unsigned __int64 *)(result + 192) = 0;
        result = *(unsigned __int64 *)(a1 + 8);
        *(unsigned __int64 *)(result + 200) = 0;
        a1 = *(unsigned __int64 *)(a1 + 8);
        result = *(unsigned __int64 *)(v_rsp - 95 - 25);
        *(unsigned __int64 *)(a1 + 208) = result;
    }
    result = IvtInitializeMTRR(a1, (unsigned int)(0x1000000ULL), 1, a4);
loc_00B628B2:
    if ((*(unsigned __int64 *)(a1 + 184)) == 0) {
        a1 = a1 + 176;
        result = MmGetPhysicalAddress(a1, (unsigned int)(0x1000000ULL), 1, a4);
        a1 = *(unsigned int *)(a1 + 200);
        *(unsigned __int64 *)(a1 + 184) = result;
        a1 = (unsigned int)((a1) & (3));
        result = (result) & (-4);
        result = (result) | (a1);
        *(unsigned __int64 *)(a1 + 200) = result;
        result = *(unsigned __int64 *)(a1 + 192);
        result = (result) & (-11);
        result = (result) | (101);
        *(unsigned __int64 *)(a1 + 192) = result;
    }
loc_00B62900:
    result = IvtUpdateGlobalCommand(a1, (unsigned int)(0x4000000ULL), 1, a4);
loc_00B6290B:
    result = 0;
loc_00B6290D:
    a1 = (*(unsigned __int64 *)(v_rsp - 95 + 39)) ^ (v_rsp);
    result = _security_check_cookie(a1, (unsigned int)(0x4000000ULL), 1, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t IvtInitializeIommu(void *Arg1, int32_t Arg2, uint8_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint8_t v_stack_mC8;
    uint8_t v_stack_mD0;
    uint32_t v_stack_mD8;
    uint32_t v_stack_mF8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (208);
    result = (*(uint64_t *)(v_rip + 0x2A8736)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x5F + 0x27) = result;
    local_rdi = 0;
    *(uint32_t *)(local_rsp - 0x5F - 0x45) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x130)));
    local_rbx = (local_rbx) | (-1);
    *(uint32_t *)(local_rsp - 0x5F - 0x2D) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x138)));
    *(uint8_t *)(local_rsp - 0x5F - 0x49) = Arg3;
    *(uint32_t *)(local_rsp - 0x5F - 0x41) = 0;
    *(uint32_t *)(local_rsp - 0x5F - 0x29) = 0;
    *(uint32_t *)(local_rsp - 0x5F - 0x31) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x134)));
    *(uint64_t *)(local_rsp - 0x5F - 0x39) = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x21) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x5F - 0x9) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x5F + 0x7) = v_xmm1;
    *(uint64_t *)(local_rsp - 0x5F + 0x17) = v_xmm1;
    if (Arg2 == 0) goto loc_00B62138;
    if (Arg2 != 3) goto loc_00B6290B;
    result = (uint32_t)(*(uint32_t *)(arg1 + 0x138));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x138))) != 0) {
        Arg2 = 0;
        result = IvtInvalidateRemappingTableEntries(Arg1, Arg2, Arg3, a4);
        Arg3 = (uint8_t)(local_rdi + 1);
        Arg2 = 0x2000000ULL;
        Arg1 = Arg1;
        result = IvtUpdateGlobalCommand(Arg1, Arg2, Arg3, a4);
    }
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x134))) == 0) goto loc_00B6290B;
    result = Feature_Test57481295__private_IsEnabledDeviceUsageNoInline(Arg1, Arg2, Arg3, a4);
    if ((uint32_t)(result) != 0) goto loc_00B620B0;
    result = IvtInvalidateAllContextEntries(Arg1, Arg2, Arg3, a4);
    goto loc_00B620B5;
loc_00B620B0:
    result = IvtInvalidateAllContextEntries(Arg1, Arg2, Arg3, a4);
loc_00B620B5:
    if ((*(uint8_t *)(arg1 + 0x140)) != 0) {
        Arg2 = (uint32_t)((Arg2) | (0xFFFFFFFFULL));
        v_stack_mC8 = 0;
        a4 = Arg2;
        v_stack_mD0 = 0;
        Arg3 = (uint32_t)(0x10000ULL);
        v_stack_mD8 = 0;
        Arg1 = Arg1;
        result = IvtInvalidateScalableModePasidCache(Arg1, Arg2, Arg3, a4);
    }
    result = Feature_Test57481295__private_IsEnabledDeviceUsageNoInline(Arg1, Arg2, Arg3, a4);
    Arg2 = 0;
    if ((uint32_t)(result) != 0) goto loc_00B6210B;
    v_stack_mC0 = 0;
    v_stack_mC8 = 0;
    Arg3 = 0;
    v_stack_mD0 = 0;
    v_stack_mD8 = 0;
    result = IvtLegacyFlushTbInternal(Arg1, Arg2, Arg3, (uint8_t)(local_rdi + 1));
    goto loc_00B6212E;
loc_00B6210B:
    v_stack_mB8 = 0;
    a4 = 0;
    v_stack_mC0 = 0;
    Arg3 = 0;
    v_stack_mC8 = 0;
    v_stack_mD0 = 0;
    v_stack_mD8 = (uint8_t)(local_rdi + 1);
    result = IvtFlushTbInternal(Arg1, Arg2, Arg3, a4);
loc_00B6212E:
    goto loc_00B62900;
loc_00B62138:
    Arg2 = 0;
    v_stack_mD8 = v_rip + 4380303;
    result = HalSocRequestApi(Arg1, Arg2, Arg2 + 4, Arg2 + 8);
    if (sign_flag) goto loc_00B6290D;
    if (*(uint64_t *)(arg1 + 0x8) != 0) goto loc_00B62181;
    Arg3 = 0;
    result = HalMapIoSpace(*(uint64_t *)(arg1), 544, Arg3, Arg2 + 8);
    *(uint64_t *)(arg1 + 0x8) = result;
    if (result == 0) goto loc_00B627D4;
loc_00B62181:
    *(uint32_t *)(result + 0x38) = (uint32_t)((uint32_t)(0x80000000ULL));
    Arg3 = 0;
    result = IvtUpdateGlobalCommand(Arg1, (uint32_t)(0x4000000ULL), Arg3, Arg2 + 8);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x34))) != 0) {
        Arg1 = *(uint64_t *)(arg1 + 0x8);
        *(uint32_t *)(arg1 + 0x34) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x34)));
    }
    if ((*(uint8_t *)(arg1 + 0x140)) == 0) goto loc_00B62202;
    result = (uint32_t)(*(uint32_t *)(arg1 + 0xE0));
    if ((*(uint8_t *)(arg1 + 0x140)) < 0) {
        result = *(uint64_t *)(arg1 + 0x8);
        Arg2 = 224;
        Arg1 = *(uint32_t *)(result + Arg2 * 1);
        result = *(uint64_t *)(arg1 + 0x8);
        Arg1 = (uint32_t)((Arg1) | ((uint32_t)((uint32_t)(0x80000000ULL))));
        *(uint32_t *)(result + Arg2 * 1) = (uint32_t)(Arg1);
        result = *(uint64_t *)(arg1 + 0x8);
        Arg2 = 220;
        Arg1 = *(uint32_t *)(result + Arg2 * 1);
        result = *(uint64_t *)(arg1 + 0x8);
        Arg1 = (uint32_t)((Arg1) | (3));
        *(uint32_t *)(result + Arg2 * 1) = (uint32_t)(Arg1);
    }
    Arg3 = 0;
    result = IvtUpdateGlobalCommand(Arg1, (uint32_t)(0x2000000ULL), Arg3, Arg2 + 8);
    if ((*(uint8_t *)(arg1 + 0x140)) == 0) goto loc_00B62235;
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x1C));
    if (sign_flag) {
        Arg3 = 0;
        Arg2 = (uint32_t)((uint32_t)(0x80000000ULL));
        Arg1 = Arg1;
        result = IvtUpdateGlobalCommand(Arg1, Arg2, Arg3, Arg2 + 8);
    }
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x134))) == 0) goto loc_00B625BB;
    if ((*(uint8_t *)(arg1 + 0x13F)) == 0) goto loc_00B62266;
    if ((*(uint64_t *)(arg1 + 0x150)) != 0) goto loc_00B62266;
    result = IvtInitializeIdentityMappings(Arg1, Arg2, Arg3, Arg2 + 8);
    if (sign_flag) goto loc_00B627D4;
loc_00B62266:
    if ((*(uint64_t *)(arg1 + 0x28)) != 0) goto loc_00B62473;
    result = guard_dispatch_icall(local_rbx, 1, Arg3, Arg2 + 8);
    *(uint64_t *)(arg1 + 0x30) = result;
    if (result == 0) goto loc_00B627D4;
    result = HalMapIoSpace(result, (uint32_t)((uint32_t)((uint32_t)(0x1000ULL))), (uint32_t)(*(uint32_t *)(arg1 + 0x110)), Arg2 + 8);
    *(uint64_t *)(arg1 + 0x28) = result;
    if (result == 0) goto loc_00B627D4;
    result = Feature_Test57481295__private_IsEnabledDeviceUsageNoInline(result, (uint32_t)((uint32_t)((uint32_t)(0x1000ULL))), (uint32_t)(*(uint32_t *)(arg1 + 0x110)), Arg2 + 8);
    if ((uint32_t)(result) != 0) {
        Arg1 = *(uint64_t *)(arg1 + 0x28);
        Arg3 = (uint32_t)((uint32_t)(0x1000ULL));
        Arg2 = 0;
        result = memset(Arg1, Arg2, Arg3, Arg2 + 8);
    }
    if ((*(uint64_t *)(v_rip + 0x3037EE)) != 0) goto loc_00B62325;
    result = guard_dispatch_icall(local_rbx, 1, Arg3, Arg2 + 8);
    *(uint64_t *)(v_rip + 0x42D4CB) = result;
    if (result == 0) goto loc_00B627D4;
    result = HalMapIoSpace(result, (uint32_t)(0x1000ULL), (uint32_t)(*(uint32_t *)(arg1 + 0x110)), Arg2 + 8);
    *(uint64_t *)(v_rip + 0x3037B1) = result;
    if (result == 0) goto loc_00B627D4;
    Arg2 = 0;
    result = memset(result, Arg2, (uint32_t)(0x1000ULL), Arg2 + 8);
loc_00B62325:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x134)))) != 1) goto loc_00B62347;
    if ((*(uint8_t *)(arg1 + 0x13F)) == 0) goto loc_00B62361;
    result = IvtGetIdentityMappedDomain(Arg1, local_rsp - 95 - 57, (uint32_t)(0x1000ULL), Arg2 + 8);
    goto loc_00B6235E;
loc_00B62347:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x134)))) != 2) goto loc_00B62361;
    Arg2 = 0;
    result = IvtGetBlockedDomain(Arg1, Arg2, local_rsp - 95 - 57, Arg2 + 8);
loc_00B6235E:
loc_00B62361:
    if ((*(uint8_t *)(arg1 + 0x140)) == 0) goto loc_00B62411;
    Arg2 = 0;
    result = IvtGetPasidGranularTranslationType(Arg1, Arg2, 1, Arg2 + 8);
    result = Feature_Test57481295__private_IsEnabledDeviceUsageNoInline(Arg1, Arg2, 1, Arg2 + 8);
    if ((uint32_t)(result) != 0) goto loc_00B623B8;
    result = IvtLegacySetupScalableModeDefaultPasidTables(Arg1, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), result, *(uint64_t *)(local_rsp - 0x5F - 0x39));
    if (sign_flag) goto loc_00B6290D;
    a4 = 0;
    v_stack_mD0 = local_rsp - 95 + 7;
    Arg3 = 0;
    result = IvtLegacyBuildScalableModeContextEntry(Arg1, *(uint64_t *)(arg1 + 0x68), Arg3, a4);
    goto loc_00B623DD;
loc_00B623B8:
    result = IvtSetupScalableModeDefaultPasidTables(Arg1, *(uint64_t *)(arg1 + 0x68), Arg3, a4);
    if (sign_flag) goto loc_00B6290D;
    a4 = 0;
    v_stack_mD0 = local_rsp - 95 + 7;
    Arg3 = 0;
    result = IvtBuildScalableModeContextEntry(Arg1, *(uint64_t *)(arg1 + 0x68), Arg3, a4);
loc_00B623DD:
    goto loc_00B6240A;
loc_00B623EA:
    result = Feature_Test57481295__private_IsEnabledDeviceUsageNoInline(Arg1, *(uint64_t *)(arg1 + 0x68), Arg3, a4);
    if ((uint32_t)(result) != 0) goto loc_00B62401;
    result = IvtLegacySetScalableModeContextEntry(Arg1, local_rsp - 95 + 7, *(uint64_t *)(arg1 + 0x28), a4);
    goto loc_00B62406;
loc_00B62401:
    result = IvtSetScalableModeContextEntry(Arg1, local_rsp - 95 + 7, *(uint64_t *)(arg1 + 0x28), a4);
loc_00B62406:
    local_r15 = (*(uint64_t *)(arg1 + 0x28)) + (32);
loc_00B6240A:
    if (local_r15 < (*(uint64_t *)(arg1 + 0x28) + 4096)) goto loc_00B623EA;
    goto loc_00B6246F;
loc_00B62411:
    result = IvtGetContextEntryType(Arg1, local_rsp - 95 + 7, *(uint64_t *)(arg1 + 0x28), a4);
    v_stack_mD8 = local_rsp - 95 - 9;
    result = IvtBuildContextEntry(Arg1, result, *(uint64_t *)(arg1 + 0x28) + 4096, *(uint64_t *)(local_rsp - 0x5F - 0x39));
    if ((*(uint64_t *)(arg1 + 0x28)) >= (*(uint64_t *)(arg1 + 0x28) + 4096)) goto loc_00B6246F;
    result = (*(uint64_t *)(local_rsp - 0x5F - 0x9)) & (1);
loc_00B6244F:
    if (result == 0) goto loc_00B6245E;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) = *(uint64_t *)(local_rsp - 0x5F - 0x1);
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x28)) = *(uint64_t *)(local_rsp - 0x5F - 0x9);
    goto loc_00B62466;
loc_00B6245E:
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x28)) = 0;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) = 0;
loc_00B62466:
    Arg2 = (*(uint64_t *)(arg1 + 0x28)) + (16);
    if (Arg2 < (*(uint64_t *)(arg1 + 0x28) + 4096)) goto loc_00B6244F;
loc_00B6246F:
loc_00B62473:
    if ((*(uint64_t *)(arg1 + 0x10)) != 0) goto loc_00B62502;
    result = guard_dispatch_icall(local_rbx, 1, *(uint64_t *)(local_rsp - 0x5F - 0x1), *(uint64_t *)(arg1 + 0x28) + 4096);
    *(uint64_t *)(arg1 + 0x18) = result;
    if (result == 0) goto loc_00B627D4;
    result = HalMapIoSpace(result, (uint32_t)((uint32_t)((uint32_t)(0x1000ULL))), (uint32_t)(*(uint32_t *)(arg1 + 0x110)), *(uint64_t *)(arg1 + 0x28) + 4096);
    *(uint64_t *)(arg1 + 0x10) = result;
    if (result == 0) goto loc_00B627D4;
    result = (*(uint64_t *)(arg1 + 0x30)) << (12);
    result = (result) | (1);
    goto loc_00B624FB;
loc_00B624DD:
    *(uint64_t *)(result) = result;
    if ((*(uint8_t *)(arg1 + 0x140)) == 0) {
        Arg3 = (result) + (8);
        *(uint64_t *)(Arg3) = 0;
    }
    Arg3 = (Arg3) + (8);
    Arg1 = (*(uint64_t *)(arg1 + 0x10)) + ((uint32_t)(0x1000ULL));
loc_00B624FB:
    if (Arg3 < Arg1) goto loc_00B624DD;
    goto loc_00B62508;
loc_00B62502:
loc_00B62508:
    if ((*(uint64_t *)(arg1 + 0x20)) != 0) goto loc_00B62551;
    result = guard_dispatch_icall(local_rbx, 1, Arg3, *(uint64_t *)(arg1 + 0x28) + 4096);
    if (result == 0) goto loc_00B627D4;
    result = HalMapIoSpace(result, (uint32_t)(0x1000ULL), 1, *(uint64_t *)(arg1 + 0x28) + 4096);
    *(uint64_t *)(arg1 + 0x20) = result;
    if (result == 0) goto loc_00B627D4;
    Arg2 = 0;
    result = memset(result, Arg2, (uint32_t)(0x1000ULL), *(uint64_t *)(arg1 + 0x28) + 4096);
loc_00B62551:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x134)))) != 2) goto loc_00B6257C;
    if ((uint8_t)(*(uint8_t *)(local_rsp - 0x5F - 0x49)) != 0) goto loc_00B6257C;
    result = Feature_Test57481295__private_IsEnabledDeviceUsageNoInline(result, Arg2, (uint32_t)(0x1000ULL), *(uint64_t *)(arg1 + 0x28) + 4096);
    if ((uint32_t)(result) != 0) goto loc_00B6256F;
    result = IvtLegacyProcessDeviceExceptions(Arg1, Arg2, (uint32_t)(0x1000ULL), *(uint64_t *)(arg1 + 0x28) + 4096);
    goto loc_00B62574;
loc_00B6256F:
    result = IvtProcessDeviceExceptions(Arg1, Arg2, (uint32_t)(0x1000ULL), *(uint64_t *)(arg1 + 0x28) + 4096);
loc_00B62574:
    if (sign_flag) goto loc_00B627D4;
loc_00B6257C:
    result = (*(uint64_t *)(arg1 + 0x18)) << (12);
    Arg1 = (uint8_t)(-(*(uint8_t *)(arg1 + 0x140)));
    Arg2 = (uint32_t)((Arg2) & (0x400ULL));
    result = (result) | (Arg2);
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) = result;
    result = IvtUpdateGlobalCommand(Arg1, (uint32_t)(0x40000000ULL), 1, *(uint64_t *)(arg1 + 0x28) + 4096);
    goto loc_00B625C1;
loc_00B625BB:
loc_00B625C1:
loc_00B625C4:
    if (0 >= 2) goto loc_00B626CB;
    if (0 != 1) goto loc_00B625F6;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x134))) == 0) goto loc_00B626C3;
    if ((*(uint8_t *)(arg1 + 0x140)) == 0) goto loc_00B626C3;
    if ((*(uint8_t *)(arg1 + 0x13C)) == 0) goto loc_00B626C3;
loc_00B625F6:
    result = (uint32_t)(0x8000ULL);
    if (0 != 1) { result = (uint32_t)((uint32_t)(0x1000ULL)); }
    *(uint32_t *)(local_rsp - 0x5F - 0x41) = (uint32_t)(result);
    result = (0 + 4) << (5);
    *(uint64_t *)(result + arg1 * 1) = (uint32_t)((uint32_t)(result));
    result = (0) << (5);
    *(uint64_t *)(local_rsp - 0x5F - 0x11) = result;
    if ((*(uint64_t *)(result + arg1 * 1 + 0x70)) != 0) goto loc_00B6268A;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))))) >> (12));
    result = guard_dispatch_icall(local_rbx, Arg2, 1, 0);
    *(uint64_t *)(result + arg1 * 1 + 0x78) = result;
    if (result == 0) goto loc_00B627D4;
    result = HalMapIoSpace(result, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), 1, 0);
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x11) + arg1 * 1 + 0x70) = result;
    if (result == 0) goto loc_00B627D4;
    Arg2 = 0;
    result = memset(result, Arg2, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), 0);
loc_00B6268A:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x5F + 0x0 * 8 - 0x21))) & (0xFF8ULL));
    Arg3 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x41))) + (-4));
    Arg3 = (uint32_t)((Arg3) & (7));
    result = (*(uint64_t *)(result + arg1 * 1 + 0x78)) << (12);
    result = (result) | (Arg1);
    result = (result) ^ (Arg3);
    *(uint64_t *)(local_rsp - 0x5F + 0x0 * 8 - 0x21) = result;
loc_00B626C3:
    local_r15 = (uint32_t)((0) + (1));
    goto loc_00B625C4;
loc_00B626CB:
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x88) = 0;
    if ((*(uint8_t *)(arg1 + 0x140)) != 0) {
        *(uint64_t *)(local_rsp - 0x5F - 0x21) = *(uint64_t *)(local_rsp - 0x5F - 0x21);
    }
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x90) = *(uint64_t *)(local_rsp - 0x5F - 0x21);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x2D))) == 0) goto loc_00B62862;
    result = *(uint64_t *)(arg1 + 0x8);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x2D)))) == 1) {
        result = *(uint64_t *)(v_rip + 0x42D0A8);
        *(uint64_t *)(arg1 + 0x120) = result;
        result = *(uint64_t *)(v_rip + 0x42D0A2);
        *(uint64_t *)(arg1 + 0x128) = result;
    }
    if ((*(uint64_t *)(arg1 + 0x120)) != 0) goto loc_00B627DE;
    local_r15 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x45))) << (4));
    local_r15 = (uint32_t)((local_r15) + (0xFFFULL));
    local_r15 = (uint32_t)((local_r15) & (0xFFFFF000ULL));
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(local_r15))) >> (12));
    result = guard_dispatch_icall(local_rbx, Arg2, Arg3, 0);
    *(uint64_t *)(arg1 + 0x128) = result;
    if (result == 0) goto loc_00B627D4;
    result = HalMapIoSpace(result, (uint32_t)((uint32_t)(local_r15)), (uint32_t)(*(uint32_t *)(arg1 + 0x110)), 0);
    *(uint64_t *)(arg1 + 0x120) = result;
    if (result == 0) goto loc_00B627D4;
    Arg2 = 0;
    result = memset(result, Arg2, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r15)))), 0);
    *(uint32_t *)(arg1 + 0x130) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x45)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x2D)))) != 1) goto loc_00B627E1;
    if ((*(uint64_t *)(v_rip + 0x42D00C)) != 0) goto loc_00B627E1;
    *(uint64_t *)(v_rip + 0x42CFFC) = *(uint64_t *)(arg1 + 0x120);
    *(uint64_t *)(v_rip + 0x42CFF6) = *(uint64_t *)(arg1 + 0x128);
    goto loc_00B627E1;
loc_00B627D4:
    goto loc_00B6290D;
loc_00B627DE:
loc_00B627E1:
    local_rbx = (*(uint64_t *)(arg1 + 0x128)) << (12);
    *(uint32_t *)(local_rsp - 0x5F - 0x29) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x45)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x45)) - 1) & (15));
    local_rbx = (local_rbx) | (result);
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0xB8) = local_rbx;
    result = KeStallExecutionProcessor(100, Arg2, (uint32_t)(0x1000ULL), 0);
    result = *(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0xB8);
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0xB8)) != local_rbx) {
        a4 = 0;
        v_stack_mD8 = 0;
        Arg3 = 0;
        Arg2 = 0x7000ULL;
        Arg1 = a4 + 92;
        result = KeBugCheckEx(Arg1, Arg2, Arg3, a4);
    }
    result = IvtUpdateGlobalCommand(Arg1, (uint32_t)(0x1000000ULL), 1, a4);
loc_00B62862:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x31))) == 0) goto loc_00B628B2;
    if ((*(uint8_t *)(arg1 + 0x140)) == 0) goto loc_00B628AA;
    if ((*(uint8_t *)(arg1 + 0x13C)) != 0) {
        result = *(uint64_t *)(arg1 + 0x8);
        *(uint64_t *)(result + 0xC0) = 0;
        result = *(uint64_t *)(arg1 + 0x8);
        *(uint64_t *)(result + 0xC8) = 0;
        Arg1 = *(uint64_t *)(arg1 + 0x8);
        result = *(uint64_t *)(local_rsp - 0x5F - 0x19);
        *(uint64_t *)(arg1 + 0xD0) = result;
    }
    result = IvtInitializeMTRR(Arg1, (uint32_t)(0x1000000ULL), 1, a4);
loc_00B628B2:
    if ((*(uint64_t *)(arg1 + 0xB8)) == 0) {
        Arg1 = Arg1 + 176;
        result = MmGetPhysicalAddress(Arg1, (uint32_t)(0x1000000ULL), 1, a4);
        Arg1 = *(uint32_t *)(arg1 + 0xC8);
        *(uint64_t *)(arg1 + 0xB8) = result;
        Arg1 = (uint32_t)((Arg1) & (3));
        result = (result) & (-4);
        result = (result) | (Arg1);
        *(uint64_t *)(arg1 + 0xC8) = result;
        result = *(uint64_t *)(arg1 + 0xC0);
        result = (result) & (-11);
        result = (result) | (101);
        *(uint64_t *)(arg1 + 0xC0) = result;
    }
loc_00B62900:
    result = IvtUpdateGlobalCommand(Arg1, (uint32_t)(0x4000000ULL), 1, a4);
loc_00B6290B:
    result = 0;
loc_00B6290D:
    Arg1 = (*(uint64_t *)(local_rsp - 0x5F + 0x27)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, (uint32_t)(0x4000000ULL), 1, a4);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `W` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `W` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `W` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x20` | `64` | `W` |
| `Arg1` | `+ 0x28` | `64` | `R` |
| `Arg1` | `+ 0x28` | `64` | `W` |
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0x30` | `64` | `W` |
| `Arg1` | `+ 0x68` | `64` | `R` |
| `Arg1` | `+ 0xB0` | `64` | `R` |
| `Arg1` | `+ 0xB8` | `64` | `R` |
| `Arg1` | `+ 0xB8` | `64` | `W` |
| `Arg1` | `+ 0xC0` | `64` | `R` |
| `Arg1` | `+ 0xC0` | `64` | `W` |
| `Arg1` | `+ 0xC8` | `32` | `R` |
| `Arg1` | `+ 0xC8` | `64` | `W` |
| `Arg1` | `+ 0xE0` | `32` | `R` |
| `Arg1` | `+ 0x110` | `32` | `R` |
| `Arg1` | `+ 0x120` | `64` | `R` |
| `Arg1` | `+ 0x120` | `64` | `W` |
| `Arg1` | `+ 0x128` | `64` | `R` |
| `Arg1` | `+ 0x128` | `64` | `W` |
| `Arg1` | `+ 0x130` | `32` | `R` |
| `Arg1` | `+ 0x130` | `32` | `W` |
| `Arg1` | `+ 0x134` | `32` | `R` |
| `Arg1` | `+ 0x138` | `32` | `R` |
| `Arg1` | `+ 0x13C` | `8` | `R` |

추가 오프셋 3개는 표에서 생략했습니다.

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagelk&rva=0x00B61FE0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
