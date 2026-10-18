# PspBuildCreateProcessContext

- RVA: `0x009ED6E0`–`0x009EF02C` (길이 `6,476` bytes)
- VA: `0x00000001409ED6E0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A5C24`
- 디코드: `1,379`개 명령, `6,476/6,476` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **81**; 고유 호출 대상: **26**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x009EDB0F` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x009EDB31` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x009EDBBD` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x009EDBF9` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x009EDE2A` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x009EDE49` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x009EDEF8` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x009EE053` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x009EE0C8` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x009EE16F` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x009EE18E` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x009EE1A6` → [IsTrustletCreateAttributeWellFormed](../../text/4D/IsTrustletCreateAttributeWellFormed_function_004DC1A4.md) (function, `0x004DC1A4`)
- `0x009EE1FD` → [RtlCopyVolatileMemory](../../text/6B/RtlCopyVolatileMemory_function_006BC9D0.md) (function, `0x006BC9D0`)
- `0x009EE204` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x009EE235` → [PspValidateMitigationOptions](../A2/PspValidateMitigationOptions_function_00A2D34C.md) (function, `0x00A2D34C`)
- `0x009EE2C2` → [KeIsEmptyGroupMask](../../text/25/KeIsEmptyGroupMask_function_002553B0.md) (function, `0x002553B0`)
- `0x009EE338` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x009EE357` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x009EE42D` → [KeGetProcessorIndexFromNumber](../../text/2D/KeGetProcessorIndexFromNumber_function_002DD2D0.md) (function, `0x002DD2D0`)
- `0x009EE494` → [KeVerifyGroupAffinity](../../text/47/KeVerifyGroupAffinity_function_0047B1F0.md) (function, `0x0047B1F0`)
- `0x009EE49E` → [Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline](../../text/5C/Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline_function_005CD968.md) (function, `0x005CD968`)
- `0x009EE4DF` → [RtlCopyFromUser](../../text/4F/RtlCopyFromUser_function_004FDAE8.md) (function, `0x004FDAE8`)
- `0x009EE4F1` → [RtlCopyVolatileMemory](../../text/6B/RtlCopyVolatileMemory_function_006BC9D0.md) (function, `0x006BC9D0`)
- `0x009EE536` → [RtlCopyFromUser](../../text/4F/RtlCopyFromUser_function_004FDAE8.md) (function, `0x004FDAE8`)
- `0x009EE54B` → [RtlCopyVolatileMemory](../../text/6B/RtlCopyVolatileMemory_function_006BC9D0.md) (function, `0x006BC9D0`)
- `0x009EE5EB` → [Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline](../../text/4E/Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline_function_004EF788.md) (function, `0x004EF788`)
- `0x009EE630` → [RtlCopyFromUser](../../text/4F/RtlCopyFromUser_function_004FDAE8.md) (function, `0x004FDAE8`)
- `0x009EE645` → [RtlCopyVolatileMemory](../../text/6B/RtlCopyVolatileMemory_function_006BC9D0.md) (function, `0x006BC9D0`)
- `0x009EE686` → [RtlCopyFromUser](../../text/4F/RtlCopyFromUser_function_004FDAE8.md) (function, `0x004FDAE8`)
- `0x009EE6A3` → [RtlCopyVolatileMemory](../../text/6B/RtlCopyVolatileMemory_function_006BC9D0.md) (function, `0x006BC9D0`)
- `0x009EE704` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x009EE78E` → [SeCaptureSid](../92/SeCaptureSid_function_009276D4.md) (function, `0x009276D4`)
- `0x009EE7DD` → [SeCaptureSidAndAttributesArray](../9C/SeCaptureSidAndAttributesArray_function_009C9D70.md) (function, `0x009C9D70`)
- `0x009EE819` → [SeCaptureHandles](../../text/60/SeCaptureHandles_function_00609FEC.md) (function, `0x00609FEC`)
- `0x009EE8E8` → [RtlCopyVolatileMemory](../../text/6B/RtlCopyVolatileMemory_function_006BC9D0.md) (function, `0x006BC9D0`)
- `0x009EE8EF` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x009EE91E` → [PspValidateMitigationAuditOptions](../AB/PspValidateMitigationAuditOptions_function_00AB2694.md) (function, `0x00AB2694`)
- `0x009EE9F0` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x009EEA18` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x009EEBE6` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x009EEC0D` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x009EEC4A` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x009EEC57` → [Feature_CreateProcessSegmentHeapEnablement__private_IsEnabledDeviceUsageNoInline](../../text/5E/Feature_CreateProcessSegmentHeapEnablement__private_IsEnabledDeviceUsageNoInline_function_005E33C0.md) (function, `0x005E33C0`)
- `0x009EEC7F` → [PspProcessUserCopyAttribute](../../text/5E/PspProcessUserCopyAttribute_function_005E3610.md) (function, `0x005E3610`)
- `0x009EED70` → [Feature_CreateProcessSegmentHeapEnablement__private_IsEnabledDeviceUsageNoInline](../../text/5E/Feature_CreateProcessSegmentHeapEnablement__private_IsEnabledDeviceUsageNoInline_function_005E33C0.md) (function, `0x005E33C0`)
- `0x009EED88` → [PspIsAttributeRemoved](../../text/5E/PspIsAttributeRemoved_function_005E34F8.md) (function, `0x005E34F8`)
- `0x009EEDAE` → [PspGetAttributeValueSize](../../text/5E/PspGetAttributeValueSize_function_005E34C8.md) (function, `0x005E34C8`)
- `0x009EEDBA` → [PspGetFullAttribute](../../text/5E/PspGetFullAttribute_function_005E34E0.md) (function, `0x005E34E0`)
- `0x009EEE5D` → [RtlValidProcessProtection](../A9/RtlValidProcessProtection_function_00A995A0.md) (function, `0x00A995A0`)
- `0x009EEF3D` → [qsort](../../text/50/qsort_function_005009F0.md) (function, `0x005009F0`)
- `0x009EEF6E` → [PspDeleteCreateProcessContext](PspDeleteCreateProcessContext_function_009EF4C4.md) (function, `0x009EF4C4`)
- `0x009EEF80` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x009EEF99` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x009EEF9E` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x009EEFA3` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x009EEFA8` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x009EEFAD` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x009EEFB2` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x009EEFB7` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x009EEFBC` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x009EEFC1` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x009EEFC6` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x009EEFCB` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x009EEFD0` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x009EEFD5` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x009EEFDA` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x009EEFDF` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x009EEFE4` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x009EEFE9` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x009EEFEE` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x009EEFF3` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x009EEFF8` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x009EEFFD` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x009EF002` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x009EF007` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x009EF00C` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x009EF011` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x009EF016` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x009EF01B` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x009EF020` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x009EF025` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)

### Direct callers
- [PsCreateMinimalProcess](../78/PsCreateMinimalProcess_function_00786D14.md) at `0x00786E5F`
- [NtCreateThreadEx](NtCreateThreadEx_function_009ED3D0.md) at `0x009ED4AE`
- [NtCreateUserProcess](../AE/NtCreateUserProcess_function_00AEA680.md) at `0x00AEA910`

### Static image references
- `0x009ED6FD` → RVA `0x00E0A740` (`.data`; read)
- `0x009EE091` → RVA `0x00FC6C58` (`ALMOSTRO`; read)
- `0x009EE2A6` → RVA `0x00FC5000` (`ALMOSTRO`; read)
- `0x009EE2B3` → RVA `0x00FCF6C0` (`CACHEALI`; read)
- `0x009EEF28` → RVA `0x00A899B0` (`PspSortHandleList`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **45**
  - `0x009EDB0F` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x009EDB31` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x009EDBBD` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x009EDBF9` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x009EDE2A` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x009EDE49` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x009EDEF8` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x009EE053` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x009EE16F` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x009EE18E` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x009EE1A6` → [IsTrustletCreateAttributeWellFormed](../../text/4D/IsTrustletCreateAttributeWellFormed_function_004DC1A4.md) (`PAGE` → `.text`)
  - `0x009EE1FD` → [RtlCopyVolatileMemory](../../text/6B/RtlCopyVolatileMemory_function_006BC9D0.md) (`PAGE` → `.text`)
  - `0x009EE204` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x009EE2C2` → [KeIsEmptyGroupMask](../../text/25/KeIsEmptyGroupMask_function_002553B0.md) (`PAGE` → `.text`)
  - `0x009EE338` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x009EE357` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x009EE42D` → [KeGetProcessorIndexFromNumber](../../text/2D/KeGetProcessorIndexFromNumber_function_002DD2D0.md) (`PAGE` → `.text`)
  - `0x009EE494` → [KeVerifyGroupAffinity](../../text/47/KeVerifyGroupAffinity_function_0047B1F0.md) (`PAGE` → `.text`)
  - `0x009EE49E` → [Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline](../../text/5C/Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline_function_005CD968.md) (`PAGE` → `.text`)
  - `0x009EE4DF` → [RtlCopyFromUser](../../text/4F/RtlCopyFromUser_function_004FDAE8.md) (`PAGE` → `.text`)
  - `0x009EE4F1` → [RtlCopyVolatileMemory](../../text/6B/RtlCopyVolatileMemory_function_006BC9D0.md) (`PAGE` → `.text`)
  - `0x009EE536` → [RtlCopyFromUser](../../text/4F/RtlCopyFromUser_function_004FDAE8.md) (`PAGE` → `.text`)
  - `0x009EE54B` → [RtlCopyVolatileMemory](../../text/6B/RtlCopyVolatileMemory_function_006BC9D0.md) (`PAGE` → `.text`)
  - `0x009EE5EB` → [Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline](../../text/4E/Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline_function_004EF788.md) (`PAGE` → `.text`)
  - `0x009EE630` → [RtlCopyFromUser](../../text/4F/RtlCopyFromUser_function_004FDAE8.md) (`PAGE` → `.text`)
  - `0x009EE645` → [RtlCopyVolatileMemory](../../text/6B/RtlCopyVolatileMemory_function_006BC9D0.md) (`PAGE` → `.text`)
  - `0x009EE686` → [RtlCopyFromUser](../../text/4F/RtlCopyFromUser_function_004FDAE8.md) (`PAGE` → `.text`)
  - `0x009EE6A3` → [RtlCopyVolatileMemory](../../text/6B/RtlCopyVolatileMemory_function_006BC9D0.md) (`PAGE` → `.text`)
  - `0x009EE704` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x009EE819` → [SeCaptureHandles](../../text/60/SeCaptureHandles_function_00609FEC.md) (`PAGE` → `.text`)
  - `0x009EE8E8` → [RtlCopyVolatileMemory](../../text/6B/RtlCopyVolatileMemory_function_006BC9D0.md) (`PAGE` → `.text`)
  - `0x009EE8EF` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x009EE9F0` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x009EEA18` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x009EEBE6` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x009EEC0D` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x009EEC4A` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x009EEC57` → [Feature_CreateProcessSegmentHeapEnablement__private_IsEnabledDeviceUsageNoInline](../../text/5E/Feature_CreateProcessSegmentHeapEnablement__private_IsEnabledDeviceUsageNoInline_function_005E33C0.md) (`PAGE` → `.text`)
  - `0x009EEC7F` → [PspProcessUserCopyAttribute](../../text/5E/PspProcessUserCopyAttribute_function_005E3610.md) (`PAGE` → `.text`)
  - `0x009EED70` → [Feature_CreateProcessSegmentHeapEnablement__private_IsEnabledDeviceUsageNoInline](../../text/5E/Feature_CreateProcessSegmentHeapEnablement__private_IsEnabledDeviceUsageNoInline_function_005E33C0.md) (`PAGE` → `.text`)
  - `0x009EED88` → [PspIsAttributeRemoved](../../text/5E/PspIsAttributeRemoved_function_005E34F8.md) (`PAGE` → `.text`)
  - `0x009EEDAE` → [PspGetAttributeValueSize](../../text/5E/PspGetAttributeValueSize_function_005E34C8.md) (`PAGE` → `.text`)
  - `0x009EEDBA` → [PspGetFullAttribute](../../text/5E/PspGetFullAttribute_function_005E34E0.md) (`PAGE` → `.text`)
  - `0x009EEF3D` → [qsort](../../text/50/qsort_function_005009F0.md) (`PAGE` → `.text`)
  - `0x009EEF80` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009ED6E0  4C 8B DC                        mov r11, rsp
009ED6E3  45 89 43 18                     mov dword ptr [r11 + 0x18], r8d
009ED6E7  88 54 24 10                     mov byte ptr [rsp + 0x10], dl
009ED6EB  53                              push rbx
009ED6EC  56                              push rsi
009ED6ED  57                              push rdi
009ED6EE  41 54                           push r12
009ED6F0  41 55                           push r13
009ED6F2  41 56                           push r14
009ED6F4  41 57                           push r15
009ED6F6  48 81 EC D0 02 00 00            sub rsp, 0x2d0
009ED6FD  48 8B 05 3C D0 41 00            mov rax, qword ptr [rip + 0x41d03c]
009ED704  48 33 C4                        xor rax, rsp
009ED707  48 89 84 24 C0 02 00 00         mov qword ptr [rsp + 0x2c0], rax
009ED70F  49 8B C1                        mov rax, r9
009ED712  48 89 84 24 10 01 00 00         mov qword ptr [rsp + 0x110], rax
009ED71A  44 8A FA                        mov r15b, dl
009ED71D  44 89 84 24 90 00 00 00         mov dword ptr [rsp + 0x90], r8d
009ED725  4D 8B E1                        mov r12, r9
009ED728  4C 89 8C 24 48 01 00 00         mov qword ptr [rsp + 0x148], r9
009ED730  4D 8B D1                        mov r10, r9
009ED733  48 89 84 24 40 01 00 00         mov qword ptr [rsp + 0x140], rax
009ED73B  0F 57 C0                        xorps xmm0, xmm0
009ED73E  0F 11 84 24 D0 00 00 00         movups xmmword ptr [rsp + 0xd0], xmm0
009ED746  0F 11 84 24 E0 00 00 00         movups xmmword ptr [rsp + 0xe0], xmm0
009ED74E  0F 11 84 24 F0 00 00 00         movups xmmword ptr [rsp + 0xf0], xmm0
009ED756  33 C0                           xor eax, eax
009ED758  0F 11 84 24 A0 00 00 00         movups xmmword ptr [rsp + 0xa0], xmm0
009ED760  49 89 83 A8 FD FF FF            mov qword ptr [r11 - 0x258], rax
009ED767  89 84 24 B8 00 00 00            mov dword ptr [rsp + 0xb8], eax
009ED76E  0F 11 84 24 70 02 00 00         movups xmmword ptr [rsp + 0x270], xmm0
009ED776  49 89 83 78 FF FF FF            mov qword ptr [r11 - 0x88], rax
009ED77D  41 89 43 80                     mov dword ptr [r11 - 0x80], eax
009ED781  49 89 83 BC FD FF FF            mov qword ptr [r11 - 0x244], rax
009ED788  49 89 83 B8 FD FF FF            mov qword ptr [r11 - 0x248], rax
009ED78F  41 0F 11 43 A0                  movups xmmword ptr [r11 - 0x60], xmm0
009ED794  49 89 43 B0                     mov qword ptr [r11 - 0x50], rax
009ED798  0F 57 C9                        xorps xmm1, xmm1
009ED79B  41 0F 11 4B 88                  movups xmmword ptr [r11 - 0x78], xmm1
009ED7A0  49 89 43 98                     mov qword ptr [r11 - 0x68], rax
009ED7A4  33 F6                           xor esi, esi
009ED7A6  89 74 24 70                     mov dword ptr [rsp + 0x70], esi
009ED7AA  89 B4 24 88 00 00 00            mov dword ptr [rsp + 0x88], esi
009ED7B1  49 89 B3 00 FE FF FF            mov qword ptr [r11 - 0x200], rsi
009ED7B8  48 89 74 24 60                  mov qword ptr [rsp + 0x60], rsi
009ED7BD  49 89 B3 F8 FD FF FF            mov qword ptr [r11 - 0x208], rsi
009ED7C4  89 B4 24 84 00 00 00            mov dword ptr [rsp + 0x84], esi
009ED7CB  41 88 11                        mov byte ptr [r9], dl
009ED7CE  44 8D 70 03                     lea r14d, [rax + 3]
009ED7D2  84 D2                           test dl, dl
009ED7D4  74 22                           je 0x1409ed7f8
009ED7D6  41 84 CE                        test r14b, cl
009ED7D9  0F 85 BA 17 00 00               jne 0x1409eef99
009ED7DF  49 BD 00 00 FF FF FF 7F 00 00   movabs r13, 0x7fffffff0000
009ED7E9  49 8B C5                        mov rax, r13
009ED7EC  49 3B CD                        cmp rcx, r13
009ED7EF  48 0F 42 C1                     cmovb rax, rcx
009ED7F3  90                              nop
009ED7F4  8A 00                           mov al, byte ptr [rax]
009ED7F6  EB 0A                           jmp 0x1409ed802
009ED7F8  49 BD 00 00 FF FF FF 7F 00 00   movabs r13, 0x7fffffff0000
009ED802  48 8B 01                        mov rax, qword ptr [rcx]
009ED805  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
009ED80A  48 83 F8 28                     cmp rax, 0x28
009ED80E  73 0A                           jae 0x1409ed81a
009ED810  B8 0D 00 00 C0                  mov eax, 0xc000000d
009ED815  E9 5B 17 00 00                  jmp 0x1409eef75
009ED81A  84 D2                           test dl, dl
009ED81C  74 2E                           je 0x1409ed84c
009ED81E  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
009ED823  48 83 C0 D8                     add rax, -0x28
009ED827  74 23                           je 0x1409ed84c
009ED829  41 84 CE                        test r14b, cl
009ED82C  0F 85 6C 17 00 00               jne 0x1409eef9e
009ED832  48 8B 54 24 68                  mov rdx, qword ptr [rsp + 0x68]
009ED837  48 03 D1                        add rdx, rcx
009ED83A  49 3B D5                        cmp rdx, r13
009ED83D  77 09                           ja 0x1409ed848
009ED83F  48 8D 41 28                     lea rax, [rcx + 0x28]
009ED843  48 3B D0                        cmp rdx, rax
009ED846  73 04                           jae 0x1409ed84c
009ED848  41 8A 45 00                     mov al, byte ptr [r13]
009ED84C  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
009ED851  48 83 E8 08                     sub rax, 8
009ED855  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
009ED85A  A8 1F                           test al, 0x1f
009ED85C  74 0A                           je 0x1409ed868
009ED85E  B8 0D 00 00 C0                  mov eax, 0xc000000d
009ED863  E9 0D 17 00 00                  jmp 0x1409eef75
009ED868  48 C1 6C 24 68 05               shr qword ptr [rsp + 0x68], 5
009ED86E  48 8D 79 08                     lea rdi, [rcx + 8]
009ED872  48 89 7C 24 58                  mov qword ptr [rsp + 0x58], rdi
009ED877  49 BB F8 FF FF FF 07 00 00 00   movabs r11, 0x7fffffff8
009ED881  41 B9 41 00 00 00               mov r9d, 0x41
009ED887  41 8D 59 CF                     lea ebx, [r9 - 0x31]
009ED88B  48 39 74 24 68                  cmp qword ptr [rsp + 0x68], rsi
009ED890  0F 86 58 16 00 00               jbe 0x1409eeeee
009ED896  48 8B 07                        mov rax, qword ptr [rdi]
009ED899  48 89 84 24 38 01 00 00         mov qword ptr [rsp + 0x138], rax
009ED8A1  45 85 C0                        test r8d, r8d
009ED8A4  74 13                           je 0x1409ed8b9
009ED8A6  48 0F BA E0 10                  bt rax, 0x10
009ED8AB  72 0C                           jb 0x1409ed8b9
009ED8AD  BF 0D 00 00 C0                  mov edi, 0xc000000d
009ED8B2  8B DF                           mov ebx, edi
009ED8B4  E9 3C 16 00 00                  jmp 0x1409eeef5
009ED8B9  48 0F BA E0 11                  bt rax, 0x11
009ED8BE  73 06                           jae 0x1409ed8c6
009ED8C0  48 39 77 18                     cmp qword ptr [rdi + 0x18], rsi
009ED8C4  75 E7                           jne 0x1409ed8ad
009ED8C6  8A C8                           mov cl, al
009ED8C8  BA 01 00 00 00                  mov edx, 1
009ED8CD  48 D3 E2                        shl rdx, cl
009ED8D0  48 89 94 24 18 02 00 00         mov qword ptr [rsp + 0x218], rdx
009ED8D8  49 8B 4C 24 08                  mov rcx, qword ptr [r12 + 8]
009ED8DD  48 85 CA                        test rdx, rcx
009ED8E0  75 CB                           jne 0x1409ed8ad
009ED8E2  48 0B CA                        or rcx, rdx
009ED8E5  49 89 4C 24 08                  mov qword ptr [r12 + 8], rcx
009ED8EA  48 3D 17 00 02 00               cmp rax, 0x20017
009ED8F0  0F 87 86 0A 00 00               ja 0x1409ee37c
009ED8F6  0F 84 E1 09 00 00               je 0x1409ee2dd
009ED8FC  48 3D 0B 00 02 00               cmp rax, 0x2000b
009ED902  0F 87 57 05 00 00               ja 0x1409ede5f
009ED908  0F 84 A6 04 00 00               je 0x1409eddb4
009ED90E  48 83 E8 06                     sub rax, 6
009ED912  0F 84 0D 04 00 00               je 0x1409edd25
009ED918  48 2D FD FF 00 00               sub rax, 0xfffd
009ED91E  0F 84 77 03 00 00               je 0x1409edc9b
009ED924  48 83 E8 01                     sub rax, 1
009ED928  0F 84 DE 02 00 00               je 0x1409edc0c
009ED92E  48 2D 01 00 01 00               sub rax, 0x10001
009ED934  0F 84 1A 02 00 00               je 0x1409edb54
009ED93A  48 83 E8 02                     sub rax, 2
009ED93E  0F 84 4F 01 00 00               je 0x1409eda93
009ED944  48 83 E8 01                     sub rax, 1
009ED948  0F 84 06 01 00 00               je 0x1409eda54
009ED94E  48 83 E8 01                     sub rax, 1
009ED952  0F 84 B1 00 00 00               je 0x1409eda09
009ED958  48 83 F8 01                     cmp rax, 1
009ED95C  0F 85 0E 14 00 00               jne 0x1409eed70
009ED962  48 83 7F 08 08                  cmp qword ptr [rdi + 8], 8
009ED967  0F 85 40 FF FF FF               jne 0x1409ed8ad
009ED96D  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
009ED971  48 89 84 24 58 01 00 00         mov qword ptr [rsp + 0x158], rax
009ED979  45 84 FF                        test r15b, r15b
009ED97C  74 20                           je 0x1409ed99e
009ED97E  41 84 C6                        test r14b, al
009ED981  0F 85 1C 16 00 00               jne 0x1409eefa3
009ED987  49 3B C5                        cmp rax, r13
009ED98A  49 0F 43 C5                     cmovae rax, r13
009ED98E  90                              nop
009ED98F  8A 00                           mov al, byte ptr [rax]
009ED991  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
009ED996  48 8B 84 24 58 01 00 00         mov rax, qword ptr [rsp + 0x158]
009ED99E  48 89 B4 24 00 01 00 00         mov qword ptr [rsp + 0x100], rsi
009ED9A6  48 8B 00                        mov rax, qword ptr [rax]
009ED9A9  48 89 84 24 00 01 00 00         mov qword ptr [rsp + 0x100], rax
009ED9B1  A8 1C                           test al, 0x1c
009ED9B3  74 0A                           je 0x1409ed9bf
009ED9B5  BB BB 00 00 C0                  mov ebx, 0xc00000bb
009ED9BA  E9 31 15 00 00                  jmp 0x1409eeef0
009ED9BF  44 8B C0                        mov r8d, eax
009ED9C2  45 23 C6                        and r8d, r14d
009ED9C5  44 89 84 24 84 00 00 00         mov dword ptr [rsp + 0x84], r8d
009ED9CD  45 3A C6                        cmp r8b, r14b
009ED9D0  0F 83 D7 FE FF FF               jae 0x1409ed8ad
009ED9D6  41 8A D0                        mov dl, r8b
009ED9D9  41 22 D6                        and dl, r14b
009ED9DC  C0 E2 02                        shl dl, 2
009ED9DF  41 8A 4C 24 11                  mov cl, byte ptr [r12 + 0x11]
009ED9E4  80 E1 F3                        and cl, 0xf3
009ED9E7  0A D1                           or dl, cl
009ED9E9  41 88 54 24 11                  mov byte ptr [r12 + 0x11], dl
009ED9EE  41 83 F8 01                     cmp r8d, 1
009ED9F2  0F 85 5F 12 00 00               jne 0x1409eec57
009ED9F8  48 C1 E8 20                     shr rax, 0x20
009ED9FC  41 89 84 24 20 01 00 00         mov dword ptr [r12 + 0x120], eax
009EDA04  E9 4E 12 00 00                  jmp 0x1409eec57
009EDA09  48 83 7F 08 04                  cmp qword ptr [rdi + 8], 4
009EDA0E  0F 85 99 FE FF FF               jne 0x1409ed8ad
009EDA14  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
009EDA18  48 89 84 24 60 01 00 00         mov qword ptr [rsp + 0x160], rax
009EDA20  45 84 FF                        test r15b, r15b
009EDA23  74 20                           je 0x1409eda45
009EDA25  41 84 C6                        test r14b, al
009EDA28  0F 85 7A 15 00 00               jne 0x1409eefa8
009EDA2E  49 3B C5                        cmp rax, r13
009EDA31  49 0F 43 C5                     cmovae rax, r13
009EDA35  90                              nop
009EDA36  8A 00                           mov al, byte ptr [rax]
009EDA38  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
009EDA3D  48 8B 84 24 60 01 00 00         mov rax, qword ptr [rsp + 0x160]
009EDA45  8B 00                           mov eax, dword ptr [rax]
009EDA47  41 89 84 24 3C 01 00 00         mov dword ptr [r12 + 0x13c], eax
009EDA4F  E9 03 12 00 00                  jmp 0x1409eec57
009EDA54  48 83 7F 08 01                  cmp qword ptr [rdi + 8], 1
009EDA59  0F 85 4E FE FF FF               jne 0x1409ed8ad
009EDA5F  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
009EDA63  48 89 84 24 68 01 00 00         mov qword ptr [rsp + 0x168], rax
009EDA6B  45 84 FF                        test r15b, r15b
009EDA6E  74 17                           je 0x1409eda87
009EDA70  49 3B C5                        cmp rax, r13
009EDA73  49 0F 43 C5                     cmovae rax, r13
009EDA77  90                              nop
009EDA78  8A 00                           mov al, byte ptr [rax]
009EDA7A  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
009EDA7F  48 8B 84 24 68 01 00 00         mov rax, qword ptr [rsp + 0x168]
009EDA87  8A 00                           mov al, byte ptr [rax]
009EDA89  41 88 44 24 02                  mov byte ptr [r12 + 2], al
009EDA8E  E9 C4 11 00 00                  jmp 0x1409eec57
009EDA93  48 8B 5F 08                     mov rbx, qword ptr [rdi + 8]
009EDA97  48 89 5C 24 60                  mov qword ptr [rsp + 0x60], rbx
009EDA9C  48 85 DB                        test rbx, rbx
009EDA9F  0F 84 08 FE FF FF               je 0x1409ed8ad
009EDAA5  F6 C3 0F                        test bl, 0xf
009EDAA8  0F 85 FF FD FF FF               jne 0x1409ed8ad
009EDAAE  4C 8B 77 10                     mov r14, qword ptr [rdi + 0x10]
009EDAB2  4C 89 B4 24 70 01 00 00         mov qword ptr [rsp + 0x170], r14
009EDABA  45 84 FF                        test r15b, r15b
009EDABD  74 32                           je 0x1409edaf1
009EDABF  41 F6 C6 03                     test r14b, 3
009EDAC3  0F 85 E4 14 00 00               jne 0x1409eefad
009EDAC9  4A 8D 0C 33                     lea rcx, [rbx + r14]
009EDACD  4A 8D 04 33                     lea rax, [rbx + r14]
009EDAD1  49 3B C5                        cmp rax, r13
009EDAD4  77 05                           ja 0x1409edadb
009EDAD6  49 3B CE                        cmp rcx, r14
009EDAD9  73 16                           jae 0x1409edaf1
009EDADB  41 8A 45 00                     mov al, byte ptr [r13]
009EDADF  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
009EDAE4  4C 8B B4 24 70 01 00 00         mov r14, qword ptr [rsp + 0x170]
009EDAEC  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
009EDAF1  48 83 FB 10                     cmp rbx, 0x10
009EDAF5  77 2E                           ja 0x1409edb25
009EDAF7  49 8D 84 24 08 01 00 00         lea rax, [r12 + 0x108]
009EDAFF  49 89 82 18 01 00 00            mov qword ptr [r10 + 0x118], rax
009EDB06  4C 8B C3                        mov r8, rbx
009EDB09  49 8B D6                        mov rdx, r14
009EDB0C  48 8B C8                        mov rcx, rax
009EDB0F  E8 2C 8D CD FF                  call 0x1406c6840
009EDB14  48 C1 EB 04                     shr rbx, 4
009EDB18  49 89 9C 24 00 01 00 00         mov qword ptr [r12 + 0x100], rbx
009EDB20  E9 32 11 00 00                  jmp 0x1409eec57
009EDB25  41 B8 50 73 52 6C               mov r8d, 0x6c527350
009EDB2B  48 8B D3                        mov rdx, rbx
009EDB2E  49 8B C9                        mov rcx, r9
009EDB31  E8 BA 45 19 00                  call 0x140b820f0
009EDB36  48 8B 8C 24 40 01 00 00         mov rcx, qword ptr [rsp + 0x140]
009EDB3E  48 89 81 18 01 00 00            mov qword ptr [rcx + 0x118], rax
009EDB45  48 85 C0                        test rax, rax
009EDB48  75 BC                           jne 0x1409edb06
009EDB4A  BB 9A 00 00 C0                  mov ebx, 0xc000009a
009EDB4F  E9 9C 13 00 00                  jmp 0x1409eeef0
009EDB54  48 8B 5F 08                     mov rbx, qword ptr [rdi + 8]
009EDB58  48 89 5C 24 60                  mov qword ptr [rsp + 0x60], rbx
009EDB5D  48 85 DB                        test rbx, rbx
009EDB60  0F 84 47 FD FF FF               je 0x1409ed8ad
009EDB66  F6 C3 01                        test bl, 1
009EDB69  0F 85 3E FD FF FF               jne 0x1409ed8ad
009EDB6F  48 81 FB FF FF 00 00            cmp rbx, 0xffff
009EDB76  0F 87 31 FD FF FF               ja 0x1409ed8ad
009EDB7C  4C 8B 77 10                     mov r14, qword ptr [rdi + 0x10]
009EDB80  4C 89 B4 24 F8 01 00 00         mov qword ptr [rsp + 0x1f8], r14
009EDB88  45 84 FF                        test r15b, r15b
009EDB8B  74 24                           je 0x1409edbb1
009EDB8D  4A 8D 04 33                     lea rax, [rbx + r14]
009EDB91  49 3B C5                        cmp rax, r13
009EDB94  77 05                           ja 0x1409edb9b
009EDB96  49 3B C6                        cmp rax, r14
009EDB99  73 16                           jae 0x1409edbb1
009EDB9B  41 8A 45 00                     mov al, byte ptr [r13]
009EDB9F  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
009EDBA4  4C 8B B4 24 F8 01 00 00         mov r14, qword ptr [rsp + 0x1f8]
009EDBAC  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
009EDBB1  41 B8 50 73 46 6E               mov r8d, 0x6e467350
009EDBB7  48 8B D3                        mov rdx, rbx
009EDBBA  49 8B C9                        mov rcx, r9
009EDBBD  E8 2E 45 19 00                  call 0x140b820f0
009EDBC2  48 89 84 24 60 02 00 00         mov qword ptr [rsp + 0x260], rax
009EDBCA  48 85 C0                        test rax, rax
009EDBCD  0F 84 77 FF FF FF               je 0x1409edb4a
009EDBD3  0F 57 C0                        xorps xmm0, xmm0
009EDBD6  41 0F 11 84 24 F0 00 00 00      movups xmmword ptr [r12 + 0xf0], xmm0
009EDBDF  66 41 89 9C 24 F2 00 00 00      mov word ptr [r12 + 0xf2], bx
009EDBE8  49 89 84 24 F8 00 00 00         mov qword ptr [r12 + 0xf8], rax
009EDBF0  4C 8B C3                        mov r8, rbx
009EDBF3  49 8B D6                        mov rdx, r14
009EDBF6  48 8B C8                        mov rcx, rax
009EDBF9  E8 42 8C CD FF                  call 0x1406c6840
009EDBFE  66 41 89 9C 24 F0 00 00 00      mov word ptr [r12 + 0xf0], bx
009EDC07  E9 4B 10 00 00                  jmp 0x1409eec57
009EDC0C  48 83 7F 08 08                  cmp qword ptr [rdi + 8], 8
009EDC11  0F 85 96 FC FF FF               jne 0x1409ed8ad
009EDC17  48 8B 4F 10                     mov rcx, qword ptr [rdi + 0x10]
009EDC1B  48 89 8C 24 E0 01 00 00         mov qword ptr [rsp + 0x1e0], rcx
009EDC23  45 84 FF                        test r15b, r15b
009EDC26  74 27                           je 0x1409edc4f
009EDC28  41 84 CE                        test r14b, cl
009EDC2B  0F 85 81 13 00 00               jne 0x1409eefb2
009EDC31  49 3B CD                        cmp rcx, r13
009EDC34  49 0F 43 CD                     cmovae rcx, r13
009EDC38  8A 01                           mov al, byte ptr [rcx]
009EDC3A  88 01                           mov byte ptr [rcx], al
009EDC3C  8A 41 07                        mov al, byte ptr [rcx + 7]
009EDC3F  88 41 07                        mov byte ptr [rcx + 7], al
009EDC42  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
009EDC47  48 8B 8C 24 E0 01 00 00         mov rcx, qword ptr [rsp + 0x1e0]
009EDC4F  49 89 4C 24 20                  mov qword ptr [r12 + 0x20], rcx
009EDC54  48 8B 4F 18                     mov rcx, qword ptr [rdi + 0x18]
009EDC58  48 89 4C 24 78                  mov qword ptr [rsp + 0x78], rcx
009EDC5D  48 85 C9                        test rcx, rcx
009EDC60  0F 84 F1 0F 00 00               je 0x1409eec57
009EDC66  45 84 FF                        test r15b, r15b
009EDC69  74 24                           je 0x1409edc8f
009EDC6B  41 84 CE                        test r14b, cl
009EDC6E  0F 85 43 13 00 00               jne 0x1409eefb7
009EDC74  49 3B CD                        cmp rcx, r13
009EDC77  49 0F 43 CD                     cmovae rcx, r13
009EDC7B  8A 01                           mov al, byte ptr [rcx]
009EDC7D  88 01                           mov byte ptr [rcx], al
009EDC7F  8A 41 07                        mov al, byte ptr [rcx + 7]
009EDC82  88 41 07                        mov byte ptr [rcx + 7], al
009EDC85  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
009EDC8A  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
009EDC8F  48 C7 01 08 00 00 00            mov qword ptr [rcx], 8
009EDC96  E9 BC 0F 00 00                  jmp 0x1409eec57
009EDC9B  48 39 5F 08                     cmp qword ptr [rdi + 8], rbx
009EDC9F  0F 85 08 FC FF FF               jne 0x1409ed8ad
009EDCA5  48 8B 4F 10                     mov rcx, qword ptr [rdi + 0x10]
009EDCA9  48 89 8C 24 F0 01 00 00         mov qword ptr [rsp + 0x1f0], rcx
009EDCB1  45 84 FF                        test r15b, r15b
009EDCB4  74 27                           je 0x1409edcdd
009EDCB6  41 84 CE                        test r14b, cl
009EDCB9  0F 85 FD 12 00 00               jne 0x1409eefbc
009EDCBF  49 3B CD                        cmp rcx, r13
009EDCC2  49 0F 43 CD                     cmovae rcx, r13
009EDCC6  8A 01                           mov al, byte ptr [rcx]
009EDCC8  88 01                           mov byte ptr [rcx], al
009EDCCA  8A 41 0F                        mov al, byte ptr [rcx + 0xf]
009EDCCD  88 41 0F                        mov byte ptr [rcx + 0xf], al
009EDCD0  48 8B 8C 24 F0 01 00 00         mov rcx, qword ptr [rsp + 0x1f0]
009EDCD8  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
009EDCDD  49 89 4C 24 18                  mov qword ptr [r12 + 0x18], rcx
009EDCE2  48 8B 4F 18                     mov rcx, qword ptr [rdi + 0x18]
009EDCE6  48 89 4C 24 78                  mov qword ptr [rsp + 0x78], rcx
009EDCEB  48 85 C9                        test rcx, rcx
009EDCEE  0F 84 63 0F 00 00               je 0x1409eec57
009EDCF4  45 84 FF                        test r15b, r15b
009EDCF7  74 24                           je 0x1409edd1d
009EDCF9  41 84 CE                        test r14b, cl
009EDCFC  0F 85 BF 12 00 00               jne 0x1409eefc1
009EDD02  49 3B CD                        cmp rcx, r13
009EDD05  49 0F 43 CD                     cmovae rcx, r13
009EDD09  8A 01                           mov al, byte ptr [rcx]
009EDD0B  88 01                           mov byte ptr [rcx], al
009EDD0D  8A 41 07                        mov al, byte ptr [rcx + 7]
009EDD10  88 41 07                        mov byte ptr [rcx + 7], al
009EDD13  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
009EDD18  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
009EDD1D  48 89 19                        mov qword ptr [rcx], rbx
009EDD20  E9 32 0F 00 00                  jmp 0x1409eec57
009EDD25  48 83 7F 08 40                  cmp qword ptr [rdi + 8], 0x40
009EDD2A  0F 85 7D FB FF FF               jne 0x1409ed8ad
009EDD30  48 8B 4F 10                     mov rcx, qword ptr [rdi + 0x10]
009EDD34  48 89 8C 24 78 01 00 00         mov qword ptr [rsp + 0x178], rcx
009EDD3C  45 84 FF                        test r15b, r15b
009EDD3F  74 27                           je 0x1409edd68
009EDD41  41 84 CE                        test r14b, cl
009EDD44  0F 85 7C 12 00 00               jne 0x1409eefc6
009EDD4A  49 3B CD                        cmp rcx, r13
009EDD4D  49 0F 43 CD                     cmovae rcx, r13
009EDD51  8A 01                           mov al, byte ptr [rcx]
009EDD53  88 01                           mov byte ptr [rcx], al
009EDD55  8A 41 3F                        mov al, byte ptr [rcx + 0x3f]
009EDD58  88 41 3F                        mov byte ptr [rcx + 0x3f], al
009EDD5B  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
009EDD60  48 8B 8C 24 78 01 00 00         mov rcx, qword ptr [rsp + 0x178]
009EDD68  49 89 4C 24 28                  mov qword ptr [r12 + 0x28], rcx
009EDD6D  48 8B 4F 18                     mov rcx, qword ptr [rdi + 0x18]
009EDD71  48 89 4C 24 78                  mov qword ptr [rsp + 0x78], rcx
009EDD76  48 85 C9                        test rcx, rcx
009EDD79  0F 84 D8 0E 00 00               je 0x1409eec57
009EDD7F  45 84 FF                        test r15b, r15b
009EDD82  74 24                           je 0x1409edda8
009EDD84  41 84 CE                        test r14b, cl
009EDD87  0F 85 3E 12 00 00               jne 0x1409eefcb
009EDD8D  49 3B CD                        cmp rcx, r13
009EDD90  49 0F 43 CD                     cmovae rcx, r13
009EDD94  8A 01                           mov al, byte ptr [rcx]
009EDD96  88 01                           mov byte ptr [rcx], al
009EDD98  8A 41 07                        mov al, byte ptr [rcx + 7]
009EDD9B  88 41 07                        mov byte ptr [rcx + 7], al
009EDD9E  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
009EDDA3  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
009EDDA8  48 C7 01 40 00 00 00            mov qword ptr [rcx], 0x40
009EDDAF  E9 A3 0E 00 00                  jmp 0x1409eec57
009EDDB4  48 8B 5F 08                     mov rbx, qword ptr [rdi + 8]
009EDDB8  48 89 5C 24 60                  mov qword ptr [rsp + 0x60], rbx
009EDDBD  48 85 DB                        test rbx, rbx
009EDDC0  0F 84 E7 FA FF FF               je 0x1409ed8ad
009EDDC6  F6 C3 07                        test bl, 7
009EDDC9  0F 85 DE FA FF FF               jne 0x1409ed8ad
009EDDCF  48 8B C3                        mov rax, rbx
009EDDD2  48 83 E0 F8                     and rax, 0xfffffffffffffff8
009EDDD6  49 3B C3                        cmp rax, r11
009EDDD9  0F 87 CE FA FF FF               ja 0x1409ed8ad
009EDDDF  4C 8B 77 10                     mov r14, qword ptr [rdi + 0x10]
009EDDE3  4C 89 B4 24 98 00 00 00         mov qword ptr [rsp + 0x98], r14
009EDDEB  45 84 FF                        test r15b, r15b
009EDDEE  74 2E                           je 0x1409ede1e
009EDDF0  41 F6 C6 03                     test r14b, 3
009EDDF4  0F 85 D6 11 00 00               jne 0x1409eefd0
009EDDFA  49 8D 04 1E                     lea rax, [r14 + rbx]
009EDDFE  49 3B C5                        cmp rax, r13
009EDE01  77 05                           ja 0x1409ede08
009EDE03  49 3B C6                        cmp rax, r14
009EDE06  73 16                           jae 0x1409ede1e
009EDE08  41 8A 45 00                     mov al, byte ptr [r13]
009EDE0C  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
009EDE11  4C 8B B4 24 98 00 00 00         mov r14, qword ptr [rsp + 0x98]
009EDE19  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
009EDE1E  41 B8 50 73 48 6C               mov r8d, 0x6c487350
009EDE24  48 8B D3                        mov rdx, rbx
009EDE27  49 8B C9                        mov rcx, r9
009EDE2A  E8 C1 42 19 00                  call 0x140b820f0
009EDE2F  49 89 84 24 28 01 00 00         mov qword ptr [r12 + 0x128], rax
009EDE37  48 85 C0                        test rax, rax
009EDE3A  0F 84 0A FD FF FF               je 0x1409edb4a
009EDE40  4C 8B C3                        mov r8, rbx
009EDE43  49 8B D6                        mov rdx, r14
009EDE46  48 8B C8                        mov rcx, rax
009EDE49  E8 F2 89 CD FF                  call 0x1406c6840
009EDE4E  48 C1 EB 03                     shr rbx, 3
009EDE52  41 89 9C 24 24 01 00 00         mov dword ptr [r12 + 0x124], ebx
009EDE5A  E9 F8 0D 00 00                  jmp 0x1409eec57
009EDE5F  48 2D 0D 00 02 00               sub rax, 0x2000d
009EDE65  0F 84 F5 03 00 00               je 0x1409ee260
009EDE6B  49 2B C6                        sub rax, r14
009EDE6E  0F 84 44 03 00 00               je 0x1409ee1b8
009EDE74  48 83 E8 02                     sub rax, 2
009EDE78  0F 84 7E 02 00 00               je 0x1409ee0fc
009EDE7E  48 83 E8 01                     sub rax, 1
009EDE82  0F 84 51 01 00 00               je 0x1409edfd9
009EDE88  48 83 E8 01                     sub rax, 1
009EDE8C  0F 84 FC 00 00 00               je 0x1409edf8e
009EDE92  48 83 E8 01                     sub rax, 1
009EDE96  0F 84 A7 00 00 00               je 0x1409edf43
009EDE9C  48 83 F8 01                     cmp rax, 1
009EDEA0  0F 85 CA 0E 00 00               jne 0x1409eed70
009EDEA6  48 83 7F 08 08                  cmp qword ptr [rdi + 8], 8
009EDEAB  0F 85 FC F9 FF FF               jne 0x1409ed8ad
009EDEB1  48 8B 5F 10                     mov rbx, qword ptr [rdi + 0x10]
009EDEB5  48 89 9C 24 80 01 00 00         mov qword ptr [rsp + 0x180], rbx
009EDEBD  45 84 FF                        test r15b, r15b
009EDEC0  74 28                           je 0x1409edeea
009EDEC2  41 84 DE                        test r14b, bl
009EDEC5  0F 85 0A 11 00 00               jne 0x1409eefd5
009EDECB  48 8D 43 08                     lea rax, [rbx + 8]
009EDECF  49 3B C5                        cmp rax, r13
009EDED2  77 05                           ja 0x1409eded9
009EDED4  48 3B C3                        cmp rax, rbx
009EDED7  73 11                           jae 0x1409edeea
009EDED9  41 8A 45 00                     mov al, byte ptr [r13]
009EDEDD  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
009EDEE2  48 8B 9C 24 80 01 00 00         mov rbx, qword ptr [rsp + 0x180]
009EDEEA  BA 08 00 00 00                  mov edx, 8
009EDEEF  41 B8 50 63 73 77               mov r8d, 0x77736350
009EDEF5  49 8B C9                        mov rcx, r9
009EDEF8  E8 F3 41 19 00                  call 0x140b820f0
009EDEFD  48 8B C8                        mov rcx, rax
009EDF00  49 89 84 24 B0 01 00 00         mov qword ptr [r12 + 0x1b0], rax
009EDF08  48 85 C0                        test rax, rax
009EDF0B  75 0A                           jne 0x1409edf17
009EDF0D  BB 17 00 00 C0                  mov ebx, 0xc0000017
009EDF12  E9 D9 0F 00 00                  jmp 0x1409eeef0
009EDF17  48 8B 03                        mov rax, qword ptr [rbx]
009EDF1A  48 89 01                        mov qword ptr [rcx], rax
009EDF1D  49 8B 8C 24 B0 01 00 00         mov rcx, qword ptr [r12 + 0x1b0]
009EDF25  8B 01                           mov eax, dword ptr [rcx]
009EDF27  41 84 C6                        test r14b, al
009EDF2A  0F 84 7D F9 FF FF               je 0x1409ed8ad
009EDF30  8B 41 04                        mov eax, dword ptr [rcx + 4]
009EDF33  FF C8                           dec eax
009EDF35  83 F8 05                        cmp eax, 5
009EDF38  0F 86 19 0D 00 00               jbe 0x1409eec57
009EDF3E  E9 6A F9 FF FF                  jmp 0x1409ed8ad
009EDF43  48 83 7F 08 04                  cmp qword ptr [rdi + 8], 4
009EDF48  0F 85 5F F9 FF FF               jne 0x1409ed8ad
009EDF4E  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
009EDF52  48 89 84 24 88 01 00 00         mov qword ptr [rsp + 0x188], rax
009EDF5A  45 84 FF                        test r15b, r15b
009EDF5D  74 20                           je 0x1409edf7f
009EDF5F  41 84 C6                        test r14b, al
009EDF62  0F 85 72 10 00 00               jne 0x1409eefda
009EDF68  49 3B C5                        cmp rax, r13
009EDF6B  49 0F 43 C5                     cmovae rax, r13
009EDF6F  90                              nop
009EDF70  8A 00                           mov al, byte ptr [rax]
009EDF72  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
009EDF77  48 8B 84 24 88 01 00 00         mov rax, qword ptr [rsp + 0x188]
009EDF7F  8B 00                           mov eax, dword ptr [rax]
009EDF81  41 89 84 24 84 01 00 00         mov dword ptr [r12 + 0x184], eax
009EDF89  E9 C9 0C 00 00                  jmp 0x1409eec57
009EDF8E  48 83 7F 08 04                  cmp qword ptr [rdi + 8], 4
009EDF93  0F 85 14 F9 FF FF               jne 0x1409ed8ad
009EDF99  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
009EDF9D  48 89 84 24 90 01 00 00         mov qword ptr [rsp + 0x190], rax
009EDFA5  45 84 FF                        test r15b, r15b
009EDFA8  74 20                           je 0x1409edfca
009EDFAA  41 84 C6                        test r14b, al
009EDFAD  0F 85 2C 10 00 00               jne 0x1409eefdf
009EDFB3  49 3B C5                        cmp rax, r13
009EDFB6  49 0F 43 C5                     cmovae rax, r13
009EDFBA  90                              nop
009EDFBB  8A 00                           mov al, byte ptr [rax]
009EDFBD  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
009EDFC2  48 8B 84 24 90 01 00 00         mov rax, qword ptr [rsp + 0x190]
009EDFCA  8B 00                           mov eax, dword ptr [rax]
009EDFCC  41 89 84 24 80 01 00 00         mov dword ptr [r12 + 0x180], eax
009EDFD4  E9 7E 0C 00 00                  jmp 0x1409eec57
009EDFD9  48 8B 5F 08                     mov rbx, qword ptr [rdi + 8]
009EDFDD  48 89 5C 24 60                  mov qword ptr [rsp + 0x60], rbx
009EDFE2  48 85 DB                        test rbx, rbx
009EDFE5  0F 84 C2 F8 FF FF               je 0x1409ed8ad
009EDFEB  F6 C3 07                        test bl, 7
009EDFEE  0F 85 B9 F8 FF FF               jne 0x1409ed8ad
009EDFF4  48 8B C3                        mov rax, rbx
009EDFF7  48 83 E0 F8                     and rax, 0xfffffffffffffff8
009EDFFB  49 3B C3                        cmp rax, r11
009EDFFE  0F 87 A9 F8 FF FF               ja 0x1409ed8ad
009EE004  4C 8B 7F 10                     mov r15, qword ptr [rdi + 0x10]
009EE008  4C 89 BC 24 98 00 00 00         mov qword ptr [rsp + 0x98], r15
009EE010  40 38 B4 24 18 03 00 00         cmp byte ptr [rsp + 0x318], sil
009EE018  74 2D                           je 0x1409ee047
009EE01A  45 84 FE                        test r14b, r15b
009EE01D  0F 85 C1 0F 00 00               jne 0x1409eefe4
009EE023  4A 8D 04 3B                     lea rax, [rbx + r15]
009EE027  49 3B C5                        cmp rax, r13
009EE02A  77 05                           ja 0x1409ee031
009EE02C  49 3B C7                        cmp rax, r15
009EE02F  73 16                           jae 0x1409ee047
009EE031  41 8A 45 00                     mov al, byte ptr [r13]
009EE035  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
009EE03A  4C 8B BC 24 98 00 00 00         mov r15, qword ptr [rsp + 0x98]
009EE042  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
009EE047  41 B8 50 73 4A 6C               mov r8d, 0x6c4a7350
009EE04D  48 8B D3                        mov rdx, rbx
009EE050  49 8B C9                        mov rcx, r9
009EE053  E8 98 40 19 00                  call 0x140b820f0
009EE058  49 89 84 24 70 01 00 00         mov qword ptr [r12 + 0x170], rax
009EE060  48 85 C0                        test rax, rax
009EE063  0F 84 E1 FA FF FF               je 0x1409edb4a
009EE069  48 C1 EB 03                     shr rbx, 3
009EE06D  41 89 9C 24 7C 01 00 00         mov dword ptr [r12 + 0x17c], ebx
009EE075  4C 8B F6                        mov r14, rsi
009EE078  48 89 B4 24 98 01 00 00         mov qword ptr [rsp + 0x198], rsi
009EE080  41 8B 84 24 7C 01 00 00         mov eax, dword ptr [r12 + 0x17c]
009EE088  4C 3B F0                        cmp r14, rax
009EE08B  0F 83 BE 0B 00 00               jae 0x1409eec4f
009EE091  4C 8B 05 C0 8B 5D 00            mov r8, qword ptr [rip + 0x5d8bc0]
009EE098  4B 8B 0C F7                     mov rcx, qword ptr [r15 + r14*8]
009EE09C  48 89 74 24 38                  mov qword ptr [rsp + 0x38], rsi
009EE0A1  48 89 74 24 30                  mov qword ptr [rsp + 0x30], rsi
009EE0A6  48 8D 84 24 08 01 00 00         lea rax, [rsp + 0x108]
009EE0AE  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009EE0B3  C7 44 24 20 50 73 4A 6C         mov dword ptr [rsp + 0x20], 0x6c4a7350
009EE0BB  44 8A 8C 24 18 03 00 00         mov r9b, byte ptr [rsp + 0x318]
009EE0C3  BA 01 00 00 00                  mov edx, 1
009EE0C8  E8 83 B5 E7 FF                  call 0x140869650
009EE0CD  8B D8                           mov ebx, eax
009EE0CF  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
009EE0D3  85 C0                           test eax, eax
009EE0D5  0F 88 B7 0B 00 00               js 0x1409eec92
009EE0DB  49 8B 8C 24 70 01 00 00         mov rcx, qword ptr [r12 + 0x170]
009EE0E3  48 8B 84 24 08 01 00 00         mov rax, qword ptr [rsp + 0x108]
009EE0EB  4A 89 04 F1                     mov qword ptr [rcx + r14*8], rax
009EE0EF  49 FF C6                        inc r14
009EE0F2  4C 89 B4 24 98 01 00 00         mov qword ptr [rsp + 0x198], r14
009EE0FA  EB 84                           jmp 0x1409ee080
009EE0FC  48 8B 5F 08                     mov rbx, qword ptr [rdi + 8]
009EE100  48 89 5C 24 60                  mov qword ptr [rsp + 0x60], rbx
009EE105  48 85 DB                        test rbx, rbx
009EE108  0F 84 9F F7 FF FF               je 0x1409ed8ad
009EE10E  F6 C3 07                        test bl, 7
009EE111  0F 85 96 F7 FF FF               jne 0x1409ed8ad
009EE117  48 81 FB 88 00 00 00            cmp rbx, 0x88
009EE11E  0F 87 89 F7 FF FF               ja 0x1409ed8ad
009EE124  4C 8B 77 10                     mov r14, qword ptr [rdi + 0x10]
009EE128  4C 89 B4 24 A0 01 00 00         mov qword ptr [rsp + 0x1a0], r14
009EE130  45 84 FF                        test r15b, r15b
009EE133  74 2E                           je 0x1409ee163
009EE135  41 F6 C6 03                     test r14b, 3
009EE139  0F 85 AA 0E 00 00               jne 0x1409eefe9
009EE13F  49 8D 04 1E                     lea rax, [r14 + rbx]
009EE143  49 3B C5                        cmp rax, r13
009EE146  77 05                           ja 0x1409ee14d
009EE148  49 3B C6                        cmp rax, r14
009EE14B  73 16                           jae 0x1409ee163
009EE14D  41 8A 45 00                     mov al, byte ptr [r13]
009EE151  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
009EE156  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
009EE15B  4C 8B B4 24 A0 01 00 00         mov r14, qword ptr [rsp + 0x1a0]
009EE163  41 B8 50 73 54 61               mov r8d, 0x61547350
009EE169  48 8B D3                        mov rdx, rbx
009EE16C  49 8B C9                        mov rcx, r9
009EE16F  E8 7C 3F 19 00                  call 0x140b820f0
009EE174  49 89 84 24 68 01 00 00         mov qword ptr [r12 + 0x168], rax
009EE17C  48 85 C0                        test rax, rax
009EE17F  0F 84 C5 F9 FF FF               je 0x1409edb4a
009EE185  4C 8B C3                        mov r8, rbx
009EE188  49 8B D6                        mov rdx, r14
009EE18B  48 8B C8                        mov rcx, rax
009EE18E  E8 AD 86 CD FF                  call 0x1406c6840
009EE193  41 89 9C 24 78 01 00 00         mov dword ptr [r12 + 0x178], ebx
009EE19B  48 8B D3                        mov rdx, rbx
009EE19E  49 8B 8C 24 68 01 00 00         mov rcx, qword ptr [r12 + 0x168]
009EE1A6  E8 F9 DF AE FF                  call 0x1404dc1a4
009EE1AB  84 C0                           test al, al
009EE1AD  0F 85 A4 0A 00 00               jne 0x1409eec57
009EE1B3  E9 F5 F6 FF FF                  jmp 0x1409ed8ad
009EE1B8  4C 8B 47 08                     mov r8, qword ptr [rdi + 8]
009EE1BC  4C 89 44 24 60                  mov qword ptr [rsp + 0x60], r8
009EE1C1  49 83 F8 18                     cmp r8, 0x18
009EE1C5  0F 87 E2 F6 FF FF               ja 0x1409ed8ad
009EE1CB  0F 57 C0                        xorps xmm0, xmm0
009EE1CE  33 C0                           xor eax, eax
009EE1D0  0F 11 84 24 90 02 00 00         movups xmmword ptr [rsp + 0x290], xmm0
009EE1D8  48 89 84 24 A0 02 00 00         mov qword ptr [rsp + 0x2a0], rax
009EE1E0  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
009EE1E5  48 8D 8C 24 90 02 00 00         lea rcx, [rsp + 0x290]
009EE1ED  48 8B 57 10                     mov rdx, qword ptr [rdi + 0x10]
009EE1F1  45 84 FF                        test r15b, r15b
009EE1F4  74 0E                           je 0x1409ee204
009EE1F6  49 3B D5                        cmp rdx, r13
009EE1F9  49 0F 43 D5                     cmovae rdx, r13
009EE1FD  E8 CE E7 CC FF                  call 0x1406bc9d0
009EE202  EB 05                           jmp 0x1409ee209
009EE204  E8 37 86 CD FF                  call 0x1406c6840
009EE209  0F 10 94 24 90 02 00 00         movups xmm2, xmmword ptr [rsp + 0x290]
009EE211  0F 29 94 24 20 02 00 00         movaps xmmword ptr [rsp + 0x220], xmm2
009EE219  F2 0F 10 9C 24 A0 02 00 00      movsd xmm3, qword ptr [rsp + 0x2a0]
009EE222  F2 0F 11 9C 24 30 02 00 00      movsd qword ptr [rsp + 0x230], xmm3
009EE22B  33 D2                           xor edx, edx
009EE22D  48 8D 8C 24 20 02 00 00         lea rcx, [rsp + 0x220]
009EE235  E8 12 F1 03 00                  call 0x140a2d34c
009EE23A  8B D8                           mov ebx, eax
009EE23C  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
009EE240  85 C0                           test eax, eax
009EE242  0F 88 4A 0A 00 00               js 0x1409eec92
009EE248  41 0F 11 94 24 50 01 00 00      movups xmmword ptr [r12 + 0x150], xmm2
009EE251  F2 41 0F 11 9C 24 60 01 00 00   movsd qword ptr [r12 + 0x160], xmm3
009EE25B  E9 F7 09 00 00                  jmp 0x1409eec57
009EE260  48 83 7F 08 02                  cmp qword ptr [rdi + 8], 2
009EE265  0F 85 42 F6 FF FF               jne 0x1409ed8ad
009EE26B  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
009EE26F  48 89 84 24 A8 01 00 00         mov qword ptr [rsp + 0x1a8], rax
009EE277  45 84 FF                        test r15b, r15b
009EE27A  74 1F                           je 0x1409ee29b
009EE27C  A8 01                           test al, 1
009EE27E  0F 85 6A 0D 00 00               jne 0x1409eefee
009EE284  49 3B C5                        cmp rax, r13
009EE287  49 0F 43 C5                     cmovae rax, r13
009EE28B  90                              nop
009EE28C  8A 00                           mov al, byte ptr [rax]
009EE28E  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
009EE293  48 8B 84 24 A8 01 00 00         mov rax, qword ptr [rsp + 0x1a8]
009EE29B  0F B7 18                        movzx ebx, word ptr [rax]
009EE29E  66 89 9C 24 80 00 00 00         mov word ptr [rsp + 0x80], bx
009EE2A6  66 3B 1D 53 6D 5D 00            cmp bx, word ptr [rip + 0x5d6d53]
009EE2AD  0F 83 FA F5 FF FF               jae 0x1409ed8ad
009EE2B3  48 8D 05 06 14 5E 00            lea rax, [rip + 0x5e1406]
009EE2BA  48 8B 0C D8                     mov rcx, qword ptr [rax + rbx*8]
009EE2BE  48 83 C1 10                     add rcx, 0x10
009EE2C2  E8 E9 70 86 FF                  call 0x1402553b0
009EE2C7  85 C0                           test eax, eax
009EE2C9  0F 85 DE F5 FF FF               jne 0x1409ed8ad
009EE2CF  66 41 89 9C 24 AA 00 00 00      mov word ptr [r12 + 0xaa], bx
009EE2D8  E9 7A 09 00 00                  jmp 0x1409eec57
009EE2DD  48 8B 5F 08                     mov rbx, qword ptr [rdi + 8]
009EE2E1  48 89 5C 24 60                  mov qword ptr [rsp + 0x60], rbx
009EE2E6  48 81 FB 0C 02 00 00            cmp rbx, 0x20c
009EE2ED  0F 85 BA F5 FF FF               jne 0x1409ed8ad
009EE2F3  4C 8B 77 10                     mov r14, qword ptr [rdi + 0x10]
009EE2F7  4C 89 B4 24 B0 01 00 00         mov qword ptr [rsp + 0x1b0], r14
009EE2FF  45 84 FF                        test r15b, r15b
009EE302  74 28                           je 0x1409ee32c
009EE304  49 8D 0C 1E                     lea rcx, [r14 + rbx]
009EE308  4A 8D 04 33                     lea rax, [rbx + r14]
009EE30C  49 3B C5                        cmp rax, r13
009EE30F  77 05                           ja 0x1409ee316
009EE311  49 3B CE                        cmp rcx, r14
009EE314  73 16                           jae 0x1409ee32c
009EE316  41 8A 45 00                     mov al, byte ptr [r13]
009EE31A  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
009EE31F  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
009EE324  4C 8B B4 24 B0 01 00 00         mov r14, qword ptr [rsp + 0x1b0]
009EE32C  41 B8 50 73 4F 63               mov r8d, 0x634f7350
009EE332  48 8B D3                        mov rdx, rbx
009EE335  49 8B C9                        mov rcx, r9
009EE338  E8 B3 3D 19 00                  call 0x140b820f0
009EE33D  49 89 84 24 90 01 00 00         mov qword ptr [r12 + 0x190], rax
009EE345  48 85 C0                        test rax, rax
009EE348  0F 84 FC F7 FF FF               je 0x1409edb4a
009EE34E  4C 8B C3                        mov r8, rbx
009EE351  49 8B D6                        mov rdx, r14
009EE354  48 8B C8                        mov rcx, rax
009EE357  E8 E4 84 CD FF                  call 0x1406c6840
009EE35C  41 89 9C 24 8C 01 00 00         mov dword ptr [r12 + 0x18c], ebx
009EE364  49 8B 84 24 90 01 00 00         mov rax, qword ptr [r12 + 0x190]
009EE36C  8B 08                           mov ecx, dword ptr [rax]
009EE36E  F6 C1 40                        test cl, 0x40
009EE371  0F 84 E0 08 00 00               je 0x1409eec57
009EE377  E9 31 F5 FF FF                  jmp 0x1409ed8ad
009EE37C  48 3D 1E 00 03 00               cmp rax, 0x3001e
009EE382  0F 87 A5 09 00 00               ja 0x1409eed2d
009EE388  0F 84 0E 09 00 00               je 0x1409eec9c
009EE38E  48 2D 18 00 02 00               sub rax, 0x20018
009EE394  0F 84 FA 05 00 00               je 0x1409ee994
009EE39A  48 83 E8 01                     sub rax, 1
009EE39E  0F 84 A5 05 00 00               je 0x1409ee949
009EE3A4  48 83 E8 02                     sub rax, 2
009EE3A8  0F 84 F5 04 00 00               je 0x1409ee8a3
009EE3AE  48 83 E8 02                     sub rax, 2
009EE3B2  0F 84 88 04 00 00               je 0x1409ee840
009EE3B8  48 83 E8 06                     sub rax, 6
009EE3BC  0F 84 29 02 00 00               je 0x1409ee5eb
009EE3C2  48 83 E8 01                     sub rax, 1
009EE3C6  0F 84 D2 00 00 00               je 0x1409ee49e
009EE3CC  48 2D E8 FF 00 00               sub rax, 0xffe8
009EE3D2  74 6B                           je 0x1409ee43f
009EE3D4  48 83 F8 02                     cmp rax, 2
009EE3D8  0F 85 92 09 00 00               jne 0x1409eed70
009EE3DE  45 85 C0                        test r8d, r8d
009EE3E1  0F 84 C6 F4 FF FF               je 0x1409ed8ad
009EE3E7  48 83 7F 08 04                  cmp qword ptr [rdi + 8], 4
009EE3EC  0F 85 BB F4 FF FF               jne 0x1409ed8ad
009EE3F2  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
009EE3F6  48 89 84 24 B8 01 00 00         mov qword ptr [rsp + 0x1b8], rax
009EE3FE  45 84 FF                        test r15b, r15b
009EE401  74 1F                           je 0x1409ee422
009EE403  A8 01                           test al, 1
009EE405  0F 85 E8 0B 00 00               jne 0x1409eeff3
009EE40B  49 3B C5                        cmp rax, r13
009EE40E  49 0F 43 C5                     cmovae rax, r13
009EE412  90                              nop
009EE413  8A 00                           mov al, byte ptr [rax]
009EE415  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
009EE41A  48 8B 84 24 B8 01 00 00         mov rax, qword ptr [rsp + 0x1b8]
009EE422  8B 00                           mov eax, dword ptr [rax]
009EE424  89 44 24 70                     mov dword ptr [rsp + 0x70], eax
009EE428  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
009EE42D  E8 9E EE 8E FF                  call 0x1402dd2d0
009EE432  41 89 44 24 14                  mov dword ptr [r12 + 0x14], eax
009EE437  83 F8 FF                        cmp eax, -1
009EE43A  E9 6E FD FF FF                  jmp 0x1409ee1ad
009EE43F  45 85 C0                        test r8d, r8d
009EE442  0F 84 65 F4 FF FF               je 0x1409ed8ad
009EE448  48 39 5F 08                     cmp qword ptr [rdi + 8], rbx
009EE44C  0F 85 5B F4 FF FF               jne 0x1409ed8ad
009EE452  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
009EE456  48 89 84 24 C0 01 00 00         mov qword ptr [rsp + 0x1c0], rax
009EE45E  45 84 FF                        test r15b, r15b
009EE461  74 20                           je 0x1409ee483
009EE463  41 84 C6                        test r14b, al
009EE466  0F 85 8C 0B 00 00               jne 0x1409eeff8
009EE46C  49 3B C5                        cmp rax, r13
009EE46F  49 0F 43 C5                     cmovae rax, r13
009EE473  90                              nop
009EE474  8A 00                           mov al, byte ptr [rax]
009EE476  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
009EE47B  48 8B 84 24 C0 01 00 00         mov rax, qword ptr [rsp + 0x1c0]
009EE483  49 8D 8C 24 40 01 00 00         lea rcx, [r12 + 0x140]
009EE48B  0F 10 00                        movups xmm0, xmmword ptr [rax]
009EE48E  F3 0F 7F 01                     movdqu xmmword ptr [rcx], xmm0
009EE492  B2 01                           mov dl, 1
009EE494  E8 57 CD A8 FF                  call 0x14047b1f0
009EE499  E9 0D FD FF FF                  jmp 0x1409ee1ab
009EE49E  E8 C5 F4 BD FF                  call 0x1405cd968
009EE4A3  85 C0                           test eax, eax
009EE4A5  0F 84 02 F4 FF FF               je 0x1409ed8ad
009EE4AB  48 39 5F 08                     cmp qword ptr [rdi + 8], rbx
009EE4AF  0F 85 F8 F3 FF FF               jne 0x1409ed8ad
009EE4B5  48 8B 57 10                     mov rdx, qword ptr [rdi + 0x10]
009EE4B9  48 89 94 24 68 02 00 00         mov qword ptr [rsp + 0x268], rdx
009EE4C1  45 84 FF                        test r15b, r15b
009EE4C4  74 20                           je 0x1409ee4e6
009EE4C6  41 84 D6                        test r14b, dl
009EE4C9  0F 85 2E 0B 00 00               jne 0x1409eeffd
009EE4CF  45 84 FF                        test r15b, r15b
009EE4D2  74 12                           je 0x1409ee4e6
009EE4D4  4C 8B C3                        mov r8, rbx
009EE4D7  48 8D 8C 24 C0 00 00 00         lea rcx, [rsp + 0xc0]
009EE4DF  E8 04 F6 B0 FF                  call 0x1404fdae8
009EE4E4  EB 10                           jmp 0x1409ee4f6
009EE4E6  4C 8B C3                        mov r8, rbx
009EE4E9  48 8D 8C 24 C0 00 00 00         lea rcx, [rsp + 0xc0]
009EE4F1  E8 DA E4 CC FF                  call 0x1406bc9d0
009EE4F6  83 BC 24 C0 00 00 00 01         cmp dword ptr [rsp + 0xc0], 1
009EE4FE  0F 85 A9 F3 FF FF               jne 0x1409ed8ad
009EE504  48 8B 94 24 C8 00 00 00         mov rdx, qword ptr [rsp + 0xc8]
009EE50C  48 85 D2                        test rdx, rdx
009EE50F  0F 84 98 F3 FF FF               je 0x1409ed8ad
009EE515  45 84 FF                        test r15b, r15b
009EE518  74 23                           je 0x1409ee53d
009EE51A  41 84 D6                        test r14b, dl
009EE51D  0F 85 DF 0A 00 00               jne 0x1409ef002
009EE523  45 84 FF                        test r15b, r15b
009EE526  74 15                           je 0x1409ee53d
009EE528  41 B8 1C 00 00 00               mov r8d, 0x1c
009EE52E  48 8D 8C 24 70 02 00 00         lea rcx, [rsp + 0x270]
009EE536  E8 AD F5 B0 FF                  call 0x1404fdae8
009EE53B  EB 13                           jmp 0x1409ee550
009EE53D  41 B8 1C 00 00 00               mov r8d, 0x1c
009EE543  48 8D 8C 24 70 02 00 00         lea rcx, [rsp + 0x270]
009EE54B  E8 80 E4 CC FF                  call 0x1406bc9d0
009EE550  83 BC 24 70 02 00 00 1C         cmp dword ptr [rsp + 0x270], 0x1c
009EE558  0F 85 4F F3 FF FF               jne 0x1409ed8ad
009EE55E  F7 84 24 74 02 00 00 FE FF FF FF  test dword ptr [rsp + 0x274], 0xfffffffe
009EE569  0F 85 3E F3 FF FF               jne 0x1409ed8ad
009EE56F  F7 84 24 78 02 00 00 FE FF FF FF  test dword ptr [rsp + 0x278], 0xfffffffe
009EE57A  0F 85 2D F3 FF FF               jne 0x1409ed8ad
009EE580  F7 84 24 7C 02 00 00 E0 FF FF FF  test dword ptr [rsp + 0x27c], 0xffffffe0
009EE58B  0F 85 1C F3 FF FF               jne 0x1409ed8ad
009EE591  F7 84 24 80 02 00 00 F8 FF FF FF  test dword ptr [rsp + 0x280], 0xfffffff8
009EE59C  0F 85 0B F3 FF FF               jne 0x1409ed8ad
009EE5A2  F7 84 24 84 02 00 00 FC FF FF FF  test dword ptr [rsp + 0x284], 0xfffffffc
009EE5AD  0F 85 FA F2 FF FF               jne 0x1409ed8ad
009EE5B3  0F 10 84 24 70 02 00 00         movups xmm0, xmmword ptr [rsp + 0x270]
009EE5BB  41 0F 11 84 24 10 02 00 00      movups xmmword ptr [r12 + 0x210], xmm0
009EE5C4  F2 0F 10 84 24 80 02 00 00      movsd xmm0, qword ptr [rsp + 0x280]
009EE5CD  F2 41 0F 11 84 24 20 02 00 00   movsd qword ptr [r12 + 0x220], xmm0
009EE5D7  8B 84 24 88 02 00 00            mov eax, dword ptr [rsp + 0x288]
009EE5DE  41 89 84 24 28 02 00 00         mov dword ptr [r12 + 0x228], eax
009EE5E6  E9 6C 06 00 00                  jmp 0x1409eec57
009EE5EB  E8 98 11 B0 FF                  call 0x1404ef788
009EE5F0  85 C0                           test eax, eax
009EE5F2  0F 84 B5 F2 FF FF               je 0x1409ed8ad
009EE5F8  48 83 7F 08 20                  cmp qword ptr [rdi + 8], 0x20
009EE5FD  0F 82 AA F2 FF FF               jb 0x1409ed8ad
009EE603  48 8B 57 10                     mov rdx, qword ptr [rdi + 0x10]
009EE607  48 89 94 24 08 02 00 00         mov qword ptr [rsp + 0x208], rdx
009EE60F  45 84 FF                        test r15b, r15b
009EE612  74 23                           je 0x1409ee637
009EE614  41 84 D6                        test r14b, dl
009EE617  0F 85 EA 09 00 00               jne 0x1409ef007
009EE61D  45 84 FF                        test r15b, r15b
009EE620  74 15                           je 0x1409ee637
009EE622  41 B8 20 00 00 00               mov r8d, 0x20
009EE628  48 8D 8C 24 A0 00 00 00         lea rcx, [rsp + 0xa0]
009EE630  E8 B3 F4 B0 FF                  call 0x1404fdae8
009EE635  EB 13                           jmp 0x1409ee64a
009EE637  41 B8 20 00 00 00               mov r8d, 0x20
009EE63D  48 8D 8C 24 A0 00 00 00         lea rcx, [rsp + 0xa0]
009EE645  E8 86 E3 CC FF                  call 0x1406bc9d0
009EE64A  83 BC 24 A0 00 00 00 01         cmp dword ptr [rsp + 0xa0], 1
009EE652  0F 82 55 F2 FF FF               jb 0x1409ed8ad
009EE658  45 84 FF                        test r15b, r15b
009EE65B  74 30                           je 0x1409ee68d
009EE65D  44 84 B4 24 A8 00 00 00         test byte ptr [rsp + 0xa8], r14b
009EE665  0F 85 A1 09 00 00               jne 0x1409ef00c
009EE66B  45 84 FF                        test r15b, r15b
009EE66E  74 1D                           je 0x1409ee68d
009EE670  41 B8 30 00 00 00               mov r8d, 0x30
009EE676  48 8B 94 24 A8 00 00 00         mov rdx, qword ptr [rsp + 0xa8]
009EE67E  48 8D 8C 24 D0 00 00 00         lea rcx, [rsp + 0xd0]
009EE686  E8 5D F4 B0 FF                  call 0x1404fdae8
009EE68B  EB 1B                           jmp 0x1409ee6a8
009EE68D  41 B8 30 00 00 00               mov r8d, 0x30
009EE693  48 8B 94 24 A8 00 00 00         mov rdx, qword ptr [rsp + 0xa8]
009EE69B  48 8D 8C 24 D0 00 00 00         lea rcx, [rsp + 0xd0]
009EE6A3  E8 28 E3 CC FF                  call 0x1406bc9d0
009EE6A8  83 BC 24 D0 00 00 00 30         cmp dword ptr [rsp + 0xd0], 0x30
009EE6B0  0F 87 F7 F1 FF FF               ja 0x1409ed8ad
009EE6B6  48 39 B4 24 E0 00 00 00         cmp qword ptr [rsp + 0xe0], rsi
009EE6BE  0F 84 E9 F1 FF FF               je 0x1409ed8ad
009EE6C4  39 B4 24 F0 00 00 00            cmp dword ptr [rsp + 0xf0], esi
009EE6CB  75 13                           jne 0x1409ee6e0
009EE6CD  48 39 B4 24 E8 00 00 00         cmp qword ptr [rsp + 0xe8], rsi
009EE6D5  75 13                           jne 0x1409ee6ea
009EE6D7  39 B4 24 F0 00 00 00            cmp dword ptr [rsp + 0xf0], esi
009EE6DE  74 14                           je 0x1409ee6f4
009EE6E0  48 39 B4 24 E8 00 00 00         cmp qword ptr [rsp + 0xe8], rsi
009EE6E8  75 0A                           jne 0x1409ee6f4
009EE6EA  BB 30 00 00 C0                  mov ebx, 0xc0000030
009EE6EF  E9 FC 07 00 00                  jmp 0x1409eeef0
009EE6F4  BA 30 00 00 00                  mov edx, 0x30
009EE6F9  B9 00 01 00 00                  mov ecx, 0x100
009EE6FE  41 B8 50 73 43 63               mov r8d, 0x63437350
009EE704  E8 E7 39 19 00                  call 0x140b820f0
009EE709  48 8B C8                        mov rcx, rax
009EE70C  49 89 84 24 F8 01 00 00         mov qword ptr [r12 + 0x1f8], rax
009EE714  48 85 C0                        test rax, rax
009EE717  0F 84 F0 F7 FF FF               je 0x1409edf0d
009EE71D  8B 84 24 A0 00 00 00            mov eax, dword ptr [rsp + 0xa0]
009EE724  41 89 84 24 F0 01 00 00         mov dword ptr [r12 + 0x1f0], eax
009EE72C  48 8B 84 24 D0 00 00 00         mov rax, qword ptr [rsp + 0xd0]
009EE734  89 01                           mov dword ptr [rcx], eax
009EE736  49 8B 8C 24 F8 01 00 00         mov rcx, qword ptr [r12 + 0x1f8]
009EE73E  8B 84 24 D4 00 00 00            mov eax, dword ptr [rsp + 0xd4]
009EE745  89 41 04                        mov dword ptr [rcx + 4], eax
009EE748  49 8B 8C 24 F8 01 00 00         mov rcx, qword ptr [r12 + 0x1f8]
009EE750  48 8B 84 24 D8 00 00 00         mov rax, qword ptr [rsp + 0xd8]
009EE758  48 89 41 08                     mov qword ptr [rcx + 8], rax
009EE75C  49 8B 8C 24 F8 01 00 00         mov rcx, qword ptr [r12 + 0x1f8]
009EE764  8B 84 24 F8 00 00 00            mov eax, dword ptr [rsp + 0xf8]
009EE76B  89 41 28                        mov dword ptr [rcx + 0x28], eax
009EE76E  49 8B 84 24 F8 01 00 00         mov rax, qword ptr [r12 + 0x1f8]
009EE776  48 03 C3                        add rax, rbx
009EE779  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
009EE77E  C6 44 24 28 01                  mov byte ptr [rsp + 0x28], 1
009EE783  41 8A D7                        mov dl, r15b
009EE786  48 8B 8C 24 E0 00 00 00         mov rcx, qword ptr [rsp + 0xe0]
009EE78E  E8 41 8F F3 FF                  call 0x1409276d4
009EE793  8B D8                           mov ebx, eax
009EE795  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
009EE799  85 C0                           test eax, eax
009EE79B  0F 88 F1 04 00 00               js 0x1409eec92
009EE7A1  48 8B 8C 24 E8 00 00 00         mov rcx, qword ptr [rsp + 0xe8]
009EE7A9  48 85 C9                        test rcx, rcx
009EE7AC  74 54                           je 0x1409ee802
009EE7AE  49 8B 84 24 F8 01 00 00         mov rax, qword ptr [r12 + 0x1f8]
009EE7B6  48 83 C0 18                     add rax, 0x18
009EE7BA  48 8D 94 24 88 00 00 00         lea rdx, [rsp + 0x88]
009EE7C2  48 89 54 24 40                  mov qword ptr [rsp + 0x40], rdx
009EE7C7  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
009EE7CC  89 74 24 20                     mov dword ptr [rsp + 0x20], esi
009EE7D0  45 33 C9                        xor r9d, r9d
009EE7D3  45 8A C7                        mov r8b, r15b
009EE7D6  8B 94 24 F0 00 00 00            mov edx, dword ptr [rsp + 0xf0]
009EE7DD  E8 8E B5 FD FF                  call 0x1409c9d70
009EE7E2  8B D8                           mov ebx, eax
009EE7E4  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
009EE7E8  85 C0                           test eax, eax
009EE7EA  0F 88 A2 04 00 00               js 0x1409eec92
009EE7F0  49 8B 8C 24 F8 01 00 00         mov rcx, qword ptr [r12 + 0x1f8]
009EE7F8  8B 84 24 F0 00 00 00            mov eax, dword ptr [rsp + 0xf0]
009EE7FF  89 41 20                        mov dword ptr [rcx + 0x20], eax
009EE802  4D 8D 84 24 00 02 00 00         lea r8, [r12 + 0x200]
009EE80A  48 8B 94 24 B0 00 00 00         mov rdx, qword ptr [rsp + 0xb0]
009EE812  8B 8C 24 B8 00 00 00            mov ecx, dword ptr [rsp + 0xb8]
009EE819  E8 CE B7 C1 FF                  call 0x140609fec
009EE81E  8B D8                           mov ebx, eax
009EE820  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
009EE824  85 C0                           test eax, eax
009EE826  0F 88 66 04 00 00               js 0x1409eec92
009EE82C  8B 84 24 B8 00 00 00            mov eax, dword ptr [rsp + 0xb8]
009EE833  41 89 84 24 08 02 00 00         mov dword ptr [r12 + 0x208], eax
009EE83B  E9 17 04 00 00                  jmp 0x1409eec57
009EE840  48 83 7F 08 04                  cmp qword ptr [rdi + 8], 4
009EE845  0F 85 62 F0 FF FF               jne 0x1409ed8ad
009EE84B  48 8B 4F 10                     mov rcx, qword ptr [rdi + 0x10]
009EE84F  48 89 8C 24 C8 01 00 00         mov qword ptr [rsp + 0x1c8], rcx
009EE857  45 84 FF                        test r15b, r15b
009EE85A  74 28                           je 0x1409ee884
009EE85C  41 84 CE                        test r14b, cl
009EE85F  0F 85 AC 07 00 00               jne 0x1409ef011
009EE865  48 8D 41 04                     lea rax, [rcx + 4]
009EE869  49 3B C5                        cmp rax, r13
009EE86C  77 05                           ja 0x1409ee873
009EE86E  48 3B C1                        cmp rax, rcx
009EE871  73 11                           jae 0x1409ee884
009EE873  41 8A 45 00                     mov al, byte ptr [r13]
009EE877  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
009EE87C  48 8B 8C 24 C8 01 00 00         mov rcx, qword ptr [rsp + 0x1c8]
009EE884  F7 01 FE FF FF FF               test dword ptr [rcx], 0xfffffffe
009EE88A  74 0A                           je 0x1409ee896
009EE88C  B8 0D 00 00 C0                  mov eax, 0xc000000d
009EE891  E9 DF 06 00 00                  jmp 0x1409eef75
009EE896  49 89 8C 24 B8 01 00 00         mov qword ptr [r12 + 0x1b8], rcx
009EE89E  E9 B4 03 00 00                  jmp 0x1409eec57
009EE8A3  4C 8B 47 08                     mov r8, qword ptr [rdi + 8]
009EE8A7  4C 89 44 24 60                  mov qword ptr [rsp + 0x60], r8
009EE8AC  49 83 F8 18                     cmp r8, 0x18
009EE8B0  0F 87 F7 EF FF FF               ja 0x1409ed8ad
009EE8B6  0F 57 C0                        xorps xmm0, xmm0
009EE8B9  33 C0                           xor eax, eax
009EE8BB  0F 11 84 24 A8 02 00 00         movups xmmword ptr [rsp + 0x2a8], xmm0
009EE8C3  48 89 84 24 B8 02 00 00         mov qword ptr [rsp + 0x2b8], rax
009EE8CB  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
009EE8D0  48 8D 8C 24 A8 02 00 00         lea rcx, [rsp + 0x2a8]
009EE8D8  48 8B 57 10                     mov rdx, qword ptr [rdi + 0x10]
009EE8DC  45 84 FF                        test r15b, r15b
009EE8DF  74 0E                           je 0x1409ee8ef
009EE8E1  49 3B D5                        cmp rdx, r13
009EE8E4  49 0F 43 D5                     cmovae rdx, r13
009EE8E8  E8 E3 E0 CC FF                  call 0x1406bc9d0
009EE8ED  EB 05                           jmp 0x1409ee8f4
009EE8EF  E8 4C 7F CD FF                  call 0x1406c6840
009EE8F4  0F 10 94 24 A8 02 00 00         movups xmm2, xmmword ptr [rsp + 0x2a8]
009EE8FC  0F 29 94 24 40 02 00 00         movaps xmmword ptr [rsp + 0x240], xmm2
009EE904  F2 0F 10 9C 24 B8 02 00 00      movsd xmm3, qword ptr [rsp + 0x2b8]
009EE90D  F2 0F 11 9C 24 50 02 00 00      movsd qword ptr [rsp + 0x250], xmm3
009EE916  48 8D 8C 24 40 02 00 00         lea rcx, [rsp + 0x240]
009EE91E  E8 71 3D 0C 00                  call 0x140ab2694
009EE923  8B D8                           mov ebx, eax
009EE925  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
009EE929  85 C0                           test eax, eax
009EE92B  0F 88 61 03 00 00               js 0x1409eec92
009EE931  41 0F 11 94 24 C0 01 00 00      movups xmmword ptr [r12 + 0x1c0], xmm2
009EE93A  F2 41 0F 11 9C 24 D0 01 00 00   movsd qword ptr [r12 + 0x1d0], xmm3
009EE944  E9 0E 03 00 00                  jmp 0x1409eec57
009EE949  48 83 7F 08 04                  cmp qword ptr [rdi + 8], 4
009EE94E  0F 85 59 EF FF FF               jne 0x1409ed8ad
009EE954  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
009EE958  48 89 84 24 D0 01 00 00         mov qword ptr [rsp + 0x1d0], rax
009EE960  45 84 FF                        test r15b, r15b
009EE963  74 20                           je 0x1409ee985
009EE965  41 84 C6                        test r14b, al
009EE968  0F 85 A8 06 00 00               jne 0x1409ef016
009EE96E  49 3B C5                        cmp rax, r13
009EE971  49 0F 43 C5                     cmovae rax, r13
009EE975  90                              nop
009EE976  8A 00                           mov al, byte ptr [rax]
009EE978  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
009EE97D  48 8B 84 24 D0 01 00 00         mov rax, qword ptr [rsp + 0x1d0]
009EE985  8B 00                           mov eax, dword ptr [rax]
009EE987  41 89 84 24 88 01 00 00         mov dword ptr [r12 + 0x188], eax
009EE98F  E9 C3 02 00 00                  jmp 0x1409eec57
009EE994  4C 8B 7F 08                     mov r15, qword ptr [rdi + 8]
009EE998  4C 89 7C 24 60                  mov qword ptr [rsp + 0x60], r15
009EE99D  49 83 FF 28                     cmp r15, 0x28
009EE9A1  0F 85 06 EF FF FF               jne 0x1409ed8ad
009EE9A7  4C 8B 77 10                     mov r14, qword ptr [rdi + 0x10]
009EE9AB  4C 89 B4 24 D8 01 00 00         mov qword ptr [rsp + 0x1d8], r14
009EE9B3  40 38 B4 24 18 03 00 00         cmp byte ptr [rsp + 0x318], sil
009EE9BB  74 27                           je 0x1409ee9e4
009EE9BD  41 F6 C6 03                     test r14b, 3
009EE9C1  0F 85 54 06 00 00               jne 0x1409ef01b
009EE9C7  4D 3B F5                        cmp r14, r13
009EE9CA  4D 0F 43 F5                     cmovae r14, r13
009EE9CE  90                              nop
009EE9CF  41 8A 06                        mov al, byte ptr [r14]
009EE9D2  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
009EE9D7  4C 8B 7C 24 60                  mov r15, qword ptr [rsp + 0x60]
009EE9DC  4C 8B B4 24 D8 01 00 00         mov r14, qword ptr [rsp + 0x1d8]
009EE9E4  41 B8 50 6E 42 70               mov r8d, 0x70426e50
009EE9EA  49 8B D7                        mov rdx, r15
009EE9ED  49 8B C9                        mov rcx, r9
009EE9F0  E8 FB 36 19 00                  call 0x140b820f0
009EE9F5  49 89 84 24 98 01 00 00         mov qword ptr [r12 + 0x198], rax
009EE9FD  48 85 C0                        test rax, rax
009EEA00  0F 84 44 F1 FF FF               je 0x1409edb4a
009EEA06  8B DE                           mov ebx, esi
009EEA08  89 9C 24 8C 00 00 00            mov dword ptr [rsp + 0x8c], ebx
009EEA0F  4D 8B C7                        mov r8, r15
009EEA12  49 8B D6                        mov rdx, r14
009EEA15  48 8B C8                        mov rcx, rax
009EEA18  E8 23 7E CD FF                  call 0x1406c6840
009EEA1D  49 B8 00 00 FF FF FF 7F 00 00   movabs r8, 0x7fffffff0000
009EEA27  4C 8B 94 24 10 01 00 00         mov r10, qword ptr [rsp + 0x110]
009EEA2F  EB 4E                           jmp 0x1409eea7f
009EEA31  8B D8                           mov ebx, eax
009EEA33  89 84 24 50 01 00 00            mov dword ptr [rsp + 0x150], eax
009EEA3A  89 84 24 8C 00 00 00            mov dword ptr [rsp + 0x8c], eax
009EEA41  4C 8B A4 24 48 01 00 00         mov r12, qword ptr [rsp + 0x148]
009EEA49  49 8B 84 24 98 01 00 00         mov rax, qword ptr [r12 + 0x198]
009EEA51  48 83 60 08 00                  and qword ptr [rax + 8], 0
009EEA56  49 8B 84 24 98 01 00 00         mov rax, qword ptr [r12 + 0x198]
009EEA5E  48 83 60 18 00                  and qword ptr [rax + 0x18], 0
009EEA63  33 F6                           xor esi, esi
009EEA65  49 B8 00 00 FF FF FF 7F 00 00   movabs r8, 0x7fffffff0000
009EEA6F  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
009EEA74  4D 8B D4                        mov r10, r12
009EEA77  4C 89 A4 24 10 01 00 00         mov qword ptr [rsp + 0x110], r12
009EEA7F  85 DB                           test ebx, ebx
009EEA81  0F 88 69 04 00 00               js 0x1409eeef0
009EEA87  4D 8B B4 24 98 01 00 00         mov r14, qword ptr [r12 + 0x198]
009EEA8F  4C 89 B4 24 28 01 00 00         mov qword ptr [rsp + 0x128], r14
009EEA97  4D 8B 6E 08                     mov r13, qword ptr [r14 + 8]
009EEA9B  4C 89 AC 24 18 01 00 00         mov qword ptr [rsp + 0x118], r13
009EEAA3  4D 8B 7E 18                     mov r15, qword ptr [r14 + 0x18]
009EEAA7  4C 89 BC 24 20 01 00 00         mov qword ptr [rsp + 0x120], r15
009EEAAF  49 89 76 08                     mov qword ptr [r14 + 8], rsi
009EEAB3  49 8B 84 24 98 01 00 00         mov rax, qword ptr [r12 + 0x198]
009EEABB  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
009EEABF  41 0F B7 46 02                  movzx eax, word ptr [r14 + 2]
009EEAC4  66 85 C0                        test ax, ax
009EEAC7  74 72                           je 0x1409eeb3b
009EEAC9  41 0F B7 0E                     movzx ecx, word ptr [r14]
009EEACD  66 3B C8                        cmp cx, ax
009EEAD0  0F 87 D7 ED FF FF               ja 0x1409ed8ad
009EEAD6  F6 C1 01                        test cl, 1
009EEAD9  0F 85 CE ED FF FF               jne 0x1409ed8ad
009EEADF  A8 01                           test al, 1
009EEAE1  0F 85 C6 ED FF FF               jne 0x1409ed8ad
009EEAE7  B9 FE FF 00 00                  mov ecx, 0xfffe
009EEAEC  66 3B C1                        cmp ax, cx
009EEAEF  0F 87 B8 ED FF FF               ja 0x1409ed8ad
009EEAF5  4D 85 ED                        test r13, r13
009EEAF8  0F 84 AF ED FF FF               je 0x1409ed8ad
009EEAFE  44 8A 8C 24 18 03 00 00         mov r9b, byte ptr [rsp + 0x318]
009EEB06  45 84 C9                        test r9b, r9b
009EEB09  74 38                           je 0x1409eeb43
009EEB0B  4A 8D 0C 28                     lea rcx, [rax + r13]
009EEB0F  49 3B C8                        cmp rcx, r8
009EEB12  77 05                           ja 0x1409eeb19
009EEB14  49 3B CD                        cmp rcx, r13
009EEB17  73 2A                           jae 0x1409eeb43
009EEB19  41 8A 00                        mov al, byte ptr [r8]
009EEB1C  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
009EEB21  4C 8B AC 24 18 01 00 00         mov r13, qword ptr [rsp + 0x118]
009EEB29  4C 8B BC 24 20 01 00 00         mov r15, qword ptr [rsp + 0x120]
009EEB31  4C 8B B4 24 28 01 00 00         mov r14, qword ptr [rsp + 0x128]
009EEB39  EB 08                           jmp 0x1409eeb43
009EEB3B  44 8A 8C 24 18 03 00 00         mov r9b, byte ptr [rsp + 0x318]
009EEB43  49 8B 8C 24 98 01 00 00         mov rcx, qword ptr [r12 + 0x198]
009EEB4B  8B 51 10                        mov edx, dword ptr [rcx + 0x10]
009EEB4E  48 8B C1                        mov rax, rcx
009EEB51  85 D2                           test edx, edx
009EEB53  74 65                           je 0x1409eebba
009EEB55  4D 85 FF                        test r15, r15
009EEB58  0F 84 4F ED FF FF               je 0x1409ed8ad
009EEB5E  81 FA FF FF 00 00               cmp edx, 0xffff
009EEB64  0F 87 43 ED FF FF               ja 0x1409ed8ad
009EEB6A  45 84 C9                        test r9b, r9b
009EEB6D  74 4B                           je 0x1409eebba
009EEB6F  48 8D 14 D5 00 00 00 00         lea rdx, [rdx*8]
009EEB77  48 85 D2                        test rdx, rdx
009EEB7A  74 3E                           je 0x1409eebba
009EEB7C  41 F6 C7 03                     test r15b, 3
009EEB80  0F 85 9A 04 00 00               jne 0x1409ef020
009EEB86  49 03 D7                        add rdx, r15
009EEB89  49 3B D0                        cmp rdx, r8
009EEB8C  77 05                           ja 0x1409eeb93
009EEB8E  49 3B D7                        cmp rdx, r15
009EEB91  73 27                           jae 0x1409eebba
009EEB93  41 8A 00                        mov al, byte ptr [r8]
009EEB96  49 8B 82 98 01 00 00            mov rax, qword ptr [r10 + 0x198]
009EEB9D  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
009EEBA2  4C 8B AC 24 18 01 00 00         mov r13, qword ptr [rsp + 0x118]
009EEBAA  4C 8B BC 24 20 01 00 00         mov r15, qword ptr [rsp + 0x120]
009EEBB2  4C 8B B4 24 28 01 00 00         mov r14, qword ptr [rsp + 0x128]
009EEBBA  48 8B DE                        mov rbx, rsi
009EEBBD  48 89 9C 24 30 01 00 00         mov qword ptr [rsp + 0x130], rbx
009EEBC5  41 0F B7 56 02                  movzx edx, word ptr [r14 + 2]
009EEBCA  66 85 D2                        test dx, dx
009EEBCD  75 05                           jne 0x1409eebd4
009EEBCF  39 70 10                        cmp dword ptr [rax + 0x10], esi
009EEBD2  76 22                           jbe 0x1409eebf6
009EEBD4  8B 48 10                        mov ecx, dword ptr [rax + 0x10]
009EEBD7  48 8D 14 CA                     lea rdx, [rdx + rcx*8]
009EEBDB  B9 41 00 00 00                  mov ecx, 0x41
009EEBE0  41 B8 50 6E 42 70               mov r8d, 0x70426e50
009EEBE6  E8 05 35 19 00                  call 0x140b820f0
009EEBEB  48 8B D8                        mov rbx, rax
009EEBEE  48 89 84 24 30 01 00 00         mov qword ptr [rsp + 0x130], rax
009EEBF6  41 0F B7 46 02                  movzx eax, word ptr [r14 + 2]
009EEBFB  66 85 C0                        test ax, ax
009EEBFE  74 22                           je 0x1409eec22
009EEC00  49 89 5E 08                     mov qword ptr [r14 + 8], rbx
009EEC04  44 8B C0                        mov r8d, eax
009EEC07  49 8B D5                        mov rdx, r13
009EEC0A  48 8B CB                        mov rcx, rbx
009EEC0D  E8 2E 7C CD FF                  call 0x1406c6840
009EEC12  41 0F B7 4E 02                  movzx ecx, word ptr [r14 + 2]
009EEC17  48 03 D9                        add rbx, rcx
009EEC1A  48 89 9C 24 30 01 00 00         mov qword ptr [rsp + 0x130], rbx
009EEC22  49 8B 84 24 98 01 00 00         mov rax, qword ptr [r12 + 0x198]
009EEC2A  39 70 10                        cmp dword ptr [rax + 0x10], esi
009EEC2D  76 20                           jbe 0x1409eec4f
009EEC2F  48 89 58 18                     mov qword ptr [rax + 0x18], rbx
009EEC33  49 8B 8C 24 98 01 00 00         mov rcx, qword ptr [r12 + 0x198]
009EEC3B  44 8B 41 10                     mov r8d, dword ptr [rcx + 0x10]
009EEC3F  49 C1 E0 03                     shl r8, 3
009EEC43  49 8B D7                        mov rdx, r15
009EEC46  48 8B 49 18                     mov rcx, qword ptr [rcx + 0x18]
009EEC4A  E8 F1 7B CD FF                  call 0x1406c6840
009EEC4F  44 8A BC 24 18 03 00 00         mov r15b, byte ptr [rsp + 0x318]
009EEC57  E8 64 47 BF FF                  call 0x1405e33c0
009EEC5C  85 C0                           test eax, eax
009EEC5E  0F 84 57 02 00 00               je 0x1409eeebb
009EEC64  48 F7 84 24 38 01 00 00 00 00 08 00  test qword ptr [rsp + 0x138], 0x80000
009EEC70  0F 84 45 02 00 00               je 0x1409eeebb
009EEC76  4D 8B C4                        mov r8, r12
009EEC79  41 8A D7                        mov dl, r15b
009EEC7C  48 8B CF                        mov rcx, rdi
009EEC7F  E8 8C 49 BF FF                  call 0x1405e3610
009EEC84  8B D8                           mov ebx, eax
009EEC86  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
009EEC8A  85 C0                           test eax, eax
009EEC8C  0F 89 29 02 00 00               jns 0x1409eeebb
009EEC92  BF 0D 00 00 C0                  mov edi, 0xc000000d
009EEC97  E9 5D 02 00 00                  jmp 0x1409eeef9
009EEC9C  45 85 C0                        test r8d, r8d
009EEC9F  0F 84 08 EC FF FF               je 0x1409ed8ad
009EECA5  48 83 7F 08 08                  cmp qword ptr [rdi + 8], 8
009EECAA  0F 85 FD EB FF FF               jne 0x1409ed8ad
009EECB0  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
009EECB4  48 89 84 24 E8 01 00 00         mov qword ptr [rsp + 0x1e8], rax
009EECBC  45 84 FF                        test r15b, r15b
009EECBF  74 20                           je 0x1409eece1
009EECC1  41 84 C6                        test r14b, al
009EECC4  0F 85 5B 03 00 00               jne 0x1409ef025
009EECCA  49 3B C5                        cmp rax, r13
009EECCD  49 0F 43 C5                     cmovae rax, r13
009EECD1  90                              nop
009EECD2  8A 00                           mov al, byte ptr [rax]
009EECD4  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
009EECD9  48 8B 84 24 E8 01 00 00         mov rax, qword ptr [rsp + 0x1e8]
009EECE1  48 8B 10                        mov rdx, qword ptr [rax]
009EECE4  49 89 94 24 E0 01 00 00         mov qword ptr [r12 + 0x1e0], rdx
009EECEC  48 B9 08 07 00 00 80 F7 FF FF   movabs rcx, 0xfffff78000000708
009EECF6  48 B8 D8 03 00 00 80 F7 FF FF   movabs rax, 0xfffff780000003d8
009EED00  48 8B 09                        mov rcx, qword ptr [rcx]
009EED03  48 0B 08                        or rcx, qword ptr [rax]
009EED06  48 89 8C 24 10 02 00 00         mov qword ptr [rsp + 0x210], rcx
009EED0E  48 F7 D1                        not rcx
009EED11  48 85 CA                        test rdx, rcx
009EED14  0F 85 93 EB FF FF               jne 0x1409ed8ad
009EED1A  81 E2 00 00 04 00               and edx, 0x40000
009EED20  49 89 94 24 E0 01 00 00         mov qword ptr [r12 + 0x1e0], rdx
009EED28  E9 2A FF FF FF                  jmp 0x1409eec57
009EED2D  48 2D 00 00 06 00               sub rax, 0x60000
009EED33  0F 84 66 01 00 00               je 0x1409eee9f
009EED39  48 83 E8 01                     sub rax, 1
009EED3D  0F 84 40 01 00 00               je 0x1409eee83
009EED43  48 83 E8 01                     sub rax, 1
009EED47  0F 84 1A 01 00 00               je 0x1409eee67
009EED4D  48 83 E8 0F                     sub rax, 0xf
009EED51  0F 84 F3 00 00 00               je 0x1409eee4a
009EED57  48 83 E8 09                     sub rax, 9
009EED5B  0F 84 BF 00 00 00               je 0x1409eee20
009EED61  48 83 E8 02                     sub rax, 2
009EED65  0F 84 98 00 00 00               je 0x1409eee03
009EED6B  49 3B C6                        cmp rax, r14
009EED6E  74 6A                           je 0x1409eedda
009EED70  E8 4B 46 BF FF                  call 0x1405e33c0
009EED75  85 C0                           test eax, eax
009EED77  0F 84 30 EB FF FF               je 0x1409ed8ad
009EED7D  4C 8B 84 24 38 01 00 00         mov r8, qword ptr [rsp + 0x138]
009EED85  49 8B C8                        mov rcx, r8
009EED88  E8 6B 47 BF FF                  call 0x1405e34f8
009EED8D  66 41 83 F8 25                  cmp r8w, 0x25
009EED92  0F 83 15 EB FF FF               jae 0x1409ed8ad
009EED98  49 0F BA E0 13                  bt r8, 0x13
009EED9D  0F 83 0A EB FF FF               jae 0x1409ed8ad
009EEDA3  85 C0                           test eax, eax
009EEDA5  0F 85 02 EB FF FF               jne 0x1409ed8ad
009EEDAB  49 8B C8                        mov rcx, r8
009EEDAE  E8 15 47 BF FF                  call 0x1405e34c8
009EEDB3  48 8B D0                        mov rdx, rax
009EEDB6  41 0F B7 C8                     movzx ecx, r8w
009EEDBA  E8 21 47 BF FF                  call 0x1405e34e0
009EEDBF  48 85 D2                        test rdx, rdx
009EEDC2  0F 84 E5 EA FF FF               je 0x1409ed8ad
009EEDC8  48 39 57 08                     cmp qword ptr [rdi + 8], rdx
009EEDCC  0F 85 DB EA FF FF               jne 0x1409ed8ad
009EEDD2  48 39 07                        cmp qword ptr [rdi], rax
009EEDD5  E9 97 F5 FF FF                  jmp 0x1409ee371
009EEDDA  48 83 7F 08 04                  cmp qword ptr [rdi + 8], 4
009EEDDF  0F 85 C8 EA FF FF               jne 0x1409ed8ad
009EEDE5  48 F7 47 10 F8 FF FF FF         test qword ptr [rdi + 0x10], -8
009EEDED  0F 85 BA EA FF FF               jne 0x1409ed8ad
009EEDF3  8B 47 10                        mov eax, dword ptr [rdi + 0x10]
009EEDF6  41 89 84 24 E8 01 00 00         mov dword ptr [r12 + 0x1e8], eax
009EEDFE  E9 54 FE FF FF                  jmp 0x1409eec57
009EEE03  48 83 7F 08 02                  cmp qword ptr [rdi + 8], 2
009EEE08  0F 85 9F EA FF FF               jne 0x1409ed8ad
009EEE0E  0F B7 47 10                     movzx eax, word ptr [rdi + 0x10]
009EEE12  66 41 89 84 24 A8 00 00 00      mov word ptr [r12 + 0xa8], ax
009EEE1B  E9 37 FE FF FF                  jmp 0x1409eec57
009EEE20  48 83 7F 08 01                  cmp qword ptr [rdi + 8], 1
009EEE25  0F 85 82 EA FF FF               jne 0x1409ed8ad
009EEE2B  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
009EEE2F  48 F7 D8                        neg rax
009EEE32  1A C9                           sbb cl, cl
009EEE34  80 E1 80                        and cl, 0x80
009EEE37  41 8A 44 24 11                  mov al, byte ptr [r12 + 0x11]
009EEE3C  24 7F                           and al, 0x7f
009EEE3E  0A C8                           or cl, al
009EEE40  41 88 4C 24 11                  mov byte ptr [r12 + 0x11], cl
009EEE45  E9 0D FE FF FF                  jmp 0x1409eec57
009EEE4A  48 83 7F 08 01                  cmp qword ptr [rdi + 8], 1
009EEE4F  0F 85 58 EA FF FF               jne 0x1409ed8ad
009EEE55  8A 4F 10                        mov cl, byte ptr [rdi + 0x10]
009EEE58  41 88 4C 24 01                  mov byte ptr [r12 + 1], cl
009EEE5D  E8 3E A7 0A 00                  call 0x140a995a0
009EEE62  E9 44 F3 FF FF                  jmp 0x1409ee1ab
009EEE67  48 83 7F 08 08                  cmp qword ptr [rdi + 8], 8
009EEE6C  0F 85 3B EA FF FF               jne 0x1409ed8ad
009EEE72  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
009EEE76  49 89 84 24 98 00 00 00         mov qword ptr [r12 + 0x98], rax
009EEE7E  E9 D4 FD FF FF                  jmp 0x1409eec57
009EEE83  48 83 7F 08 08                  cmp qword ptr [rdi + 8], 8
009EEE88  0F 85 1F EA FF FF               jne 0x1409ed8ad
009EEE8E  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
009EEE92  49 89 84 24 90 00 00 00         mov qword ptr [r12 + 0x90], rax
009EEE9A  E9 B8 FD FF FF                  jmp 0x1409eec57
009EEE9F  48 83 7F 08 08                  cmp qword ptr [rdi + 8], 8
009EEEA4  0F 85 03 EA FF FF               jne 0x1409ed8ad
009EEEAA  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
009EEEAE  49 89 84 24 80 00 00 00         mov qword ptr [r12 + 0x80], rax
009EEEB6  E9 9C FD FF FF                  jmp 0x1409eec57
009EEEBB  48 83 C7 20                     add rdi, 0x20
009EEEBF  48 89 7C 24 58                  mov qword ptr [rsp + 0x58], rdi
009EEEC4  48 FF 4C 24 68                  dec qword ptr [rsp + 0x68]
009EEEC9  49 BD 00 00 FF FF FF 7F 00 00   movabs r13, 0x7fffffff0000
009EEED3  41 BE 03 00 00 00               mov r14d, 3
009EEED9  44 8B 84 24 20 03 00 00         mov r8d, dword ptr [rsp + 0x320]
009EEEE1  4C 8B 94 24 40 01 00 00         mov r10, qword ptr [rsp + 0x140]
009EEEE9  E9 89 E9 FF FF                  jmp 0x1409ed877
009EEEEE  8B DE                           mov ebx, esi
009EEEF0  BF 0D 00 00 C0                  mov edi, 0xc000000d
009EEEF5  89 5C 24 50                     mov dword ptr [rsp + 0x50], ebx
009EEEF9  EB 15                           jmp 0x1409eef10
009EEEFB  8B D8                           mov ebx, eax
009EEEFD  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
009EEF01  33 F6                           xor esi, esi
009EEF03  BF 0D 00 00 C0                  mov edi, 0xc000000d
009EEF08  4C 8B A4 24 48 01 00 00         mov r12, qword ptr [rsp + 0x148]
009EEF10  85 DB                           test ebx, ebx
009EEF12  78 57                           js 0x1409eef6b
009EEF14  41 8B 44 24 08                  mov eax, dword ptr [r12 + 8]
009EEF19  48 0F BA E0 0B                  bt rax, 0xb
009EEF1E  73 47                           jae 0x1409eef67
009EEF20  41 8B 94 24 24 01 00 00         mov edx, dword ptr [r12 + 0x124]
009EEF28  4C 8D 0D 81 AA 09 00            lea r9, [rip + 0x9aa81]
009EEF2F  41 B8 08 00 00 00               mov r8d, 8
009EEF35  49 8B 8C 24 28 01 00 00         mov rcx, qword ptr [r12 + 0x128]
009EEF3D  E8 AE 1A B1 FF                  call 0x1405009f0
009EEF42  49 8B 84 24 28 01 00 00         mov rax, qword ptr [r12 + 0x128]
009EEF4A  39 30                           cmp dword ptr [rax], esi
009EEF4C  0F 4C DF                        cmovl ebx, edi
009EEF4F  39 B4 24 90 00 00 00            cmp dword ptr [rsp + 0x90], esi
009EEF56  0F 95 C2                        setne dl
009EEF59  41 8A 44 24 10                  mov al, byte ptr [r12 + 0x10]
009EEF5E  24 FE                           and al, 0xfe
009EEF60  0A D0                           or dl, al
009EEF62  41 88 54 24 10                  mov byte ptr [r12 + 0x10], dl
009EEF67  85 DB                           test ebx, ebx
009EEF69  79 08                           jns 0x1409eef73
009EEF6B  49 8B CC                        mov rcx, r12
009EEF6E  E8 51 05 00 00                  call 0x1409ef4c4
009EEF73  8B C3                           mov eax, ebx
009EEF75  48 8B 8C 24 C0 02 00 00         mov rcx, qword ptr [rsp + 0x2c0]
009EEF7D  48 33 CC                        xor rcx, rsp
009EEF80  E8 BB D6 CB FF                  call 0x1406ac640
009EEF85  48 81 C4 D0 02 00 00            add rsp, 0x2d0
009EEF8C  41 5F                           pop r15
009EEF8E  41 5E                           pop r14
009EEF90  41 5D                           pop r13
009EEF92  41 5C                           pop r12
009EEF94  5F                              pop rdi
009EEF95  5E                              pop rsi
009EEF96  5B                              pop rbx
009EEF97  C3                              ret
009EEF98  CC                              int3
009EEF99  E8 32 B0 EA FF                  call 0x140899fd0
009EEF9E  E8 2D B0 EA FF                  call 0x140899fd0
009EEFA3  E8 28 B0 EA FF                  call 0x140899fd0
009EEFA8  E8 23 B0 EA FF                  call 0x140899fd0
009EEFAD  E8 1E B0 EA FF                  call 0x140899fd0
009EEFB2  E8 19 B0 EA FF                  call 0x140899fd0
009EEFB7  E8 14 B0 EA FF                  call 0x140899fd0
009EEFBC  E8 0F B0 EA FF                  call 0x140899fd0
009EEFC1  E8 0A B0 EA FF                  call 0x140899fd0
009EEFC6  E8 05 B0 EA FF                  call 0x140899fd0
009EEFCB  E8 00 B0 EA FF                  call 0x140899fd0
009EEFD0  E8 FB AF EA FF                  call 0x140899fd0
009EEFD5  E8 F6 AF EA FF                  call 0x140899fd0
009EEFDA  E8 F1 AF EA FF                  call 0x140899fd0
009EEFDF  E8 EC AF EA FF                  call 0x140899fd0
009EEFE4  E8 E7 AF EA FF                  call 0x140899fd0
009EEFE9  E8 E2 AF EA FF                  call 0x140899fd0
009EEFEE  E8 DD AF EA FF                  call 0x140899fd0
009EEFF3  E8 D8 AF EA FF                  call 0x140899fd0
009EEFF8  E8 D3 AF EA FF                  call 0x140899fd0
009EEFFD  E8 CE AF EA FF                  call 0x140899fd0
009EF002  E8 C9 AF EA FF                  call 0x140899fd0
009EF007  E8 C4 AF EA FF                  call 0x140899fd0
009EF00C  E8 BF AF EA FF                  call 0x140899fd0
009EF011  E8 BA AF EA FF                  call 0x140899fd0
009EF016  E8 B5 AF EA FF                  call 0x140899fd0
009EF01B  E8 B0 AF EA FF                  call 0x140899fd0
009EF020  E8 AB AF EA FF                  call 0x140899fd0
009EF025  E8 A6 AF EA FF                  call 0x140899fd0
009EF02A  90                              nop
009EF02B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PspBuildCreateProcessContext(__int64 a1, unsigned __int8 a2, int a3, __int64 a4)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m180;
    unsigned __int64 v_stack_m188;
    unsigned __int64 v_stack_m190;
    unsigned __int64 v_stack_m198;
    unsigned __int64 v_stack_m1A0;
    unsigned __int64 v_stack_m1A8;
    unsigned __int64 v_stack_m1B0;
    unsigned int v_stack_m1B8;
    unsigned __int64 v_stack_m1C0;
    unsigned __int64 v_stack_m1C8;
    unsigned __int64 v_stack_m1D0;
    unsigned __int64 v_stack_m1D8;
    unsigned __int64 v_stack_m1E0;
    unsigned __int64 v_stack_m1E8;
    unsigned __int64 v_stack_m1F0;
    unsigned __int64 v_stack_m1F8;
    unsigned __int64 v_stack_m200;
    unsigned __int64 v_stack_m208;
    unsigned int v_stack_m210;
    unsigned __int64 v_stack_m218;
    unsigned __int64 v_stack_m220;
    unsigned __int64 v_stack_m228;
    unsigned __int64 v_stack_m230;
    unsigned int v_stack_m234;
    unsigned __int64 v_stack_m238;
    unsigned __int64 v_stack_m240;
    unsigned __int64 v_stack_m248;
    unsigned int v_stack_m250;
    unsigned __int64 v_stack_m258;
    unsigned __int8 v_stack_m260;
    unsigned __int64 v_stack_m268;
    unsigned __int64 v_stack_m270;
    unsigned int v_stack_m278;
    unsigned int v_stack_m27C;
    unsigned int v_stack_m280;
    unsigned int v_stack_m284;
    unsigned __int16 v_stack_m288;
    unsigned __int64 v_stack_m290;
    unsigned int v_stack_m298;
    unsigned __int64 v_stack_m2A0;
    unsigned __int64 v_stack_m2A8;
    unsigned __int64 v_stack_m2B0;
    unsigned int v_stack_m2B8;
    unsigned __int64 v_stack_m2C8;
    unsigned __int64 v_stack_m2D0;
    unsigned __int64 v_stack_m2D8;
    unsigned __int64 v_stack_m2E0;
    unsigned int v_stack_m2E8;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned int v_stack_m80;
    unsigned int v_stack_m84;
    unsigned int v_stack_m88;
    unsigned int v_stack_m8C;
    unsigned int v_stack_m90;
    unsigned int v_stack_m94;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int8 v_stack_p10;
    unsigned int v_stack_p18;

    *(unsigned int *)(v_rsp + 24) = a3;
    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (720);
    result = (*(unsigned __int64 *)(v_rip + 4313148)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m1F8 = a4;
    v_stack_m278 = a3;
    v_stack_m1C0 = a4;
    v_stack_m1C8 = a4;
    v_stack_m238 = v_xmm0;
    v_stack_m228 = v_xmm0;
    v_stack_m218 = v_xmm0;
    result = 0;
    v_stack_m268 = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 600) = 0;
    v_stack_m250 = 0;
    v_stack_m98 = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 136) = 0;
    *(unsigned int *)(v_rsp - 128) = 0;
    *(unsigned __int64 *)(v_rsp - 580) = 0;
    *(unsigned __int64 *)(v_rsp - 584) = 0;
    *(unsigned __int64 *)(v_rsp - 96) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 80) = 0;
    *(unsigned __int64 *)(v_rsp - 120) = v_xmm1;
    *(unsigned __int64 *)(v_rsp - 104) = 0;
    v_rsi = 0;
    v_stack_m298 = 0;
    v_stack_m280 = 0;
    *(unsigned __int64 *)(v_rsp - 512) = 0;
    v_stack_m2A8 = 0;
    *(unsigned __int64 *)(v_rsp - 520) = 0;
    v_stack_m284 = 0;
    *(unsigned __int8 *)(a4) = a2;
    if (a2 == 0) goto loc_009ED7F8;
    if ((((unsigned __int8)(result + 3)) & ((unsigned __int8)(a1))) != 0) goto loc_009EEF99;
    result = v_r13;
    if (a1 < v_r13) { result = a1; }
    goto loc_009ED802;
loc_009ED7F8:
loc_009ED802:
    v_stack_m2A0 = *(unsigned __int64 *)(a1);
    if ((*(unsigned __int64 *)(a1)) >= 40) goto loc_009ED81A;
    goto loc_009EEF75;
loc_009ED81A:
    if (a2 == 0) goto loc_009ED84C;
    result = (v_stack_m2A0) + (-40);
    if (condition_is_equal) goto loc_009ED84C;
    if ((((unsigned __int8)(result + 3)) & ((unsigned __int8)(a1))) != 0) goto loc_009EEF9E;
    a2 = (v_stack_m2A0) + (a1);
    if (a2 > v_r13) goto loc_009ED848;
    result = a1 + 40;
    if (a2 < (a1 + 40)) {
        result = *(unsigned __int8 *)(v_r13);
    }
    result = (v_stack_m2A0) - (8);
    v_stack_m2A0 = result;
    if ((((unsigned __int8)(result)) & (31)) == 0) goto loc_009ED868;
    goto loc_009EEF75;
loc_009ED868:
    v_stack_m2B0 = a1 + 8;
loc_009ED877:
    if (v_stack_m2A0 <= 0) goto loc_009EEEEE;
    v_stack_m1D0 = *(unsigned __int64 *)(a1 + 8);
    if (a3 == 0) goto loc_009ED8B9;
    if (condition_is_below) goto loc_009ED8B9;
loc_009ED8AD:
    goto loc_009EEEF5;
loc_009ED8B9:
    if (condition_is_above_or_equal) goto loc_009ED8C6;
    if ((*(unsigned __int64 *)((unsigned int)(0xC000000DULL) + 24)) != 0) goto loc_009ED8AD;
loc_009ED8C6:
    a2 = (1) << ((unsigned __int8)((unsigned __int8)(*(unsigned __int64 *)(a1 + 8))));
    v_stack_mF0 = a2;
    if (((a2) & (*(unsigned __int64 *)(a4 + 8))) != 0) goto loc_009ED8AD;
    a1 = (*(unsigned __int64 *)(a4 + 8)) | (a2);
    *(unsigned __int64 *)(a4 + 8) = a1;
    if ((*(unsigned __int64 *)(a1 + 8)) > 0x20017ULL) goto loc_009EE37C;
    if ((*(unsigned __int64 *)(a1 + 8)) == 0x20017ULL) goto loc_009EE2DD;
    if ((*(unsigned __int64 *)(a1 + 8)) > 0x2000BULL) goto loc_009EDE5F;
    if ((*(unsigned __int64 *)(a1 + 8)) == 0x2000BULL) goto loc_009EDDB4;
    result = (*(unsigned __int64 *)(a1 + 8)) - (6);
    if (condition_is_equal) goto loc_009EDD25;
    result = (result) - (0xFFFDULL);
    if (condition_is_equal) goto loc_009EDC9B;
    result = (result) - (1);
    if (condition_is_equal) goto loc_009EDC0C;
    result = (result) - (0x10001ULL);
    if (condition_is_equal) goto loc_009EDB54;
    result = (result) - (2);
    if (condition_is_equal) goto loc_009EDA93;
    result = (result) - (1);
    if (condition_is_equal) goto loc_009EDA54;
    result = (result) - (1);
    if (condition_is_equal) goto loc_009EDA09;
    if (result != 1) goto loc_009EED70;
    if ((*(unsigned __int64 *)((unsigned int)(0xC000000DULL) + 8)) != 8) goto loc_009ED8AD;
    v_stack_m1B0 = *(unsigned __int64 *)((unsigned int)(0xC000000DULL) + 16);
    if (a2 == 0) goto loc_009ED99E;
    if ((((unsigned __int8)(result + 3)) & ((unsigned __int8)(*(unsigned __int64 *)((unsigned int)(0xC000000DULL) + 16)))) != 0) goto loc_009EEFA3;
    result = *(unsigned __int64 *)((unsigned int)(0xC000000DULL) + 16);
    if ((*(unsigned __int64 *)((unsigned int)(0xC000000DULL) + 16)) >= v_r13) { result = v_r13; }
loc_009ED99E:
    v_stack_m208 = 0;
    v_stack_m208 = *(unsigned __int64 *)(v_stack_m1B0);
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_m1B0))) & (28)) == 0) goto loc_009ED9BF;
    goto loc_009EEEF0;
loc_009ED9BF:
    a3 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m1B0)))) & ((unsigned int)(result + 3)));
    v_stack_m284 = a3;
    if (((unsigned __int8)(a3)) >= ((unsigned __int8)(result + 3))) goto loc_009ED8AD;
    a2 = (unsigned __int8)(((unsigned __int8)(a3)) & ((unsigned __int8)(result + 3)));
    a2 = (unsigned __int8)((a2) << (2));
    a1 = (unsigned __int8)((*(unsigned __int8 *)(a4 + 17)) & (243));
    a2 = (unsigned __int8)((a2) | ((unsigned __int8)(a1)));
    *(unsigned __int8 *)(a4 + 17) = a2;
    if (a3 != 1) goto loc_009EEC57;
    result = (*(unsigned __int64 *)(v_stack_m1B0)) >> (32);
    *(unsigned int *)(a4 + 288) = (unsigned int)(result);
    goto loc_009EEC57;
loc_009EDA09:
    if ((*(unsigned __int64 *)(v_stack_m2B0 + 8)) != 4) goto loc_009ED8AD;
    v_stack_m1A8 = *(unsigned __int64 *)(v_stack_m2B0 + 16);
    if (a2 == 0) goto loc_009EDA45;
    if ((((unsigned __int8)(result + 3)) & ((unsigned __int8)(*(unsigned __int64 *)(v_stack_m2B0 + 16)))) != 0) goto loc_009EEFA8;
    result = *(unsigned __int64 *)(v_stack_m2B0 + 16);
    if ((*(unsigned __int64 *)(v_stack_m2B0 + 16)) >= v_r13) { result = v_r13; }
loc_009EDA45:
    *(unsigned int *)(a4 + 316) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m1A8)));
    goto loc_009EEC57;
loc_009EDA54:
    if ((*(unsigned __int64 *)(v_stack_m2B0 + 8)) != 1) goto loc_009ED8AD;
    v_stack_m1A0 = *(unsigned __int64 *)(v_stack_m2B0 + 16);
    result = *(unsigned __int64 *)(v_stack_m2B0 + 16);
    v_rdi = v_stack_m2B0;
    if (a2 != 0) {
        result = *(unsigned __int64 *)(v_stack_m2B0 + 16);
        if ((*(unsigned __int64 *)(v_stack_m2B0 + 16)) >= v_r13) { result = v_r13; }
        result = *(unsigned __int8 *)(result);
        v_rdi = v_stack_m2B0;
        result = v_stack_m1A0;
    }
    *(unsigned __int8 *)(a4 + 2) = (unsigned __int8)(*(unsigned __int8 *)(result));
    goto loc_009EEC57;
loc_009EDA93:
    v_stack_m2A8 = *(unsigned __int64 *)(v_rdi + 8);
    if (*(unsigned __int64 *)(v_rdi + 8) == 0) goto loc_009ED8AD;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rdi + 8))) & (15)) != 0) goto loc_009ED8AD;
    v_stack_m198 = *(unsigned __int64 *)(v_rdi + 16);
    if (a2 == 0) goto loc_009EDAF1;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rdi + 16))) & (3)) != 0) goto loc_009EEFAD;
    if ((*(unsigned __int64 *)(v_rdi + 8) + *(unsigned __int64 *)(v_rdi + 16) * 1) > v_r13) goto loc_009EDADB;
    result = *(unsigned __int64 *)(v_rdi + 8) + *(unsigned __int64 *)(v_rdi + 16) * 1;
    v_rbx = *(unsigned __int64 *)(v_rdi + 8);
    v_r14 = *(unsigned __int64 *)(v_rdi + 16);
    if ((*(unsigned __int64 *)(v_rdi + 8) + *(unsigned __int64 *)(v_rdi + 16) * 1) < (*(unsigned __int64 *)(v_rdi + 16))) {
        result = *(unsigned __int8 *)(v_r13);
        v_rdi = v_stack_m2B0;
        v_r14 = v_stack_m198;
        v_rbx = v_stack_m2A8;
    }
    if (v_rbx > 16) goto loc_009EDB25;
    *(unsigned __int64 *)(a4 + 280) = a4 + 264;
loc_009EDB06:
    result = memcpy(a4 + 264, v_r14, v_rbx, 65);
    v_rbx = (v_rbx) >> (4);
    *(unsigned __int64 *)(a4 + 256) = v_rbx;
    goto loc_009EEC57;
loc_009EDB25:
    result = ExAllocatePool2(65, v_rbx, (unsigned int)(0x6C527350ULL), 65);
    *(unsigned __int64 *)(v_stack_m1C8 + 280) = result;
    if (result != 0) goto loc_009EDB06;
loc_009EDB4A:
    goto loc_009EEEF0;
loc_009EDB54:
    v_stack_m2A8 = *(unsigned __int64 *)(v_rdi + 8);
    if (*(unsigned __int64 *)(v_rdi + 8) == 0) goto loc_009ED8AD;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rdi + 8))) & (1)) != 0) goto loc_009ED8AD;
    if ((*(unsigned __int64 *)(v_rdi + 8)) > 0xFFFFULL) goto loc_009ED8AD;
    v_stack_m110 = *(unsigned __int64 *)(v_rdi + 16);
    if (a2 == 0) goto loc_009EDBB1;
    if ((*(unsigned __int64 *)(v_rdi + 8) + *(unsigned __int64 *)(v_rdi + 16) * 1) > v_r13) goto loc_009EDB9B;
    result = *(unsigned __int64 *)(v_rdi + 8) + *(unsigned __int64 *)(v_rdi + 16) * 1;
    v_rbx = *(unsigned __int64 *)(v_rdi + 8);
    v_r14 = *(unsigned __int64 *)(v_rdi + 16);
    if ((*(unsigned __int64 *)(v_rdi + 8) + *(unsigned __int64 *)(v_rdi + 16) * 1) < (*(unsigned __int64 *)(v_rdi + 16))) {
        result = *(unsigned __int8 *)(v_r13);
        v_rdi = v_stack_m2B0;
        v_r14 = v_stack_m110;
        v_rbx = v_stack_m2A8;
    }
    result = ExAllocatePool2(65, v_rbx, (unsigned int)(0x6E467350ULL), 65);
    v_stack_mA8 = result;
    if (result == 0) goto loc_009EDB4A;
    *(unsigned __int64 *)(a4 + 240) = v_xmm0;
    *(unsigned __int16 *)(a4 + 242) = (unsigned __int16)(v_rbx);
    *(unsigned __int64 *)(a4 + 248) = result;
    result = memcpy(result, v_r14, v_rbx, 65);
    *(unsigned __int16 *)(a4 + 240) = (unsigned __int16)(v_rbx);
    goto loc_009EEC57;
loc_009EDC0C:
    if ((*(unsigned __int64 *)(v_rdi + 8)) != 8) goto loc_009ED8AD;
    v_stack_m128 = *(unsigned __int64 *)(v_rdi + 16);
    if (a2 == 0) goto loc_009EDC4F;
    if ((((unsigned __int8)(v_r14)) & ((unsigned __int8)(*(unsigned __int64 *)(v_rdi + 16)))) != 0) goto loc_009EEFB2;
    a1 = *(unsigned __int64 *)(v_rdi + 16);
    if ((*(unsigned __int64 *)(v_rdi + 16)) >= v_r13) { a1 = v_r13; }
    *(unsigned __int8 *)(a1) = (unsigned __int8)(*(unsigned __int8 *)(a1));
    *(unsigned __int8 *)(a1 + 7) = (unsigned __int8)(*(unsigned __int8 *)(a1 + 7));
loc_009EDC4F:
    *(unsigned __int64 *)(a4 + 32) = v_stack_m128;
    v_stack_m290 = *(unsigned __int64 *)(v_stack_m2B0 + 24);
    if (*(unsigned __int64 *)(v_stack_m2B0 + 24) == 0) goto loc_009EEC57;
    if (a2 == 0) goto loc_009EDC8F;
    if ((((unsigned __int8)(v_r14)) & ((unsigned __int8)(*(unsigned __int64 *)(v_stack_m2B0 + 24)))) != 0) goto loc_009EEFB7;
    a1 = *(unsigned __int64 *)(v_stack_m2B0 + 24);
    if ((*(unsigned __int64 *)(v_stack_m2B0 + 24)) >= v_r13) { a1 = v_r13; }
    *(unsigned __int8 *)(a1) = (unsigned __int8)(*(unsigned __int8 *)(a1));
    *(unsigned __int8 *)(a1 + 7) = (unsigned __int8)(*(unsigned __int8 *)(a1 + 7));
loc_009EDC8F:
    *(unsigned __int64 *)(v_stack_m290) = 8;
    goto loc_009EEC57;
loc_009EDC9B:
    if ((*(unsigned __int64 *)(v_stack_m2B0 + 8)) != v_rbx) goto loc_009ED8AD;
    v_stack_m118 = *(unsigned __int64 *)(v_stack_m2B0 + 16);
    if (a2 == 0) goto loc_009EDCDD;
    if ((((unsigned __int8)(v_r14)) & ((unsigned __int8)(*(unsigned __int64 *)(v_stack_m2B0 + 16)))) != 0) goto loc_009EEFBC;
    a1 = *(unsigned __int64 *)(v_stack_m2B0 + 16);
    if ((*(unsigned __int64 *)(v_stack_m2B0 + 16)) >= v_r13) { a1 = v_r13; }
    *(unsigned __int8 *)(a1) = (unsigned __int8)(*(unsigned __int8 *)(a1));
    *(unsigned __int8 *)(a1 + 15) = (unsigned __int8)(*(unsigned __int8 *)(a1 + 15));
loc_009EDCDD:
    *(unsigned __int64 *)(a4 + 24) = v_stack_m118;
    v_stack_m290 = *(unsigned __int64 *)(v_stack_m2B0 + 24);
    if (*(unsigned __int64 *)(v_stack_m2B0 + 24) == 0) goto loc_009EEC57;
    if (a2 == 0) goto loc_009EDD1D;
    if ((((unsigned __int8)(v_r14)) & ((unsigned __int8)(*(unsigned __int64 *)(v_stack_m2B0 + 24)))) != 0) goto loc_009EEFC1;
    a1 = *(unsigned __int64 *)(v_stack_m2B0 + 24);
    if ((*(unsigned __int64 *)(v_stack_m2B0 + 24)) >= v_r13) { a1 = v_r13; }
    *(unsigned __int8 *)(a1) = (unsigned __int8)(*(unsigned __int8 *)(a1));
    *(unsigned __int8 *)(a1 + 7) = (unsigned __int8)(*(unsigned __int8 *)(a1 + 7));
loc_009EDD1D:
    *(unsigned __int64 *)(v_stack_m290) = v_rbx;
    goto loc_009EEC57;
loc_009EDD25:
    if ((*(unsigned __int64 *)(v_stack_m2B0 + 8)) != 64) goto loc_009ED8AD;
    v_stack_m190 = *(unsigned __int64 *)(v_stack_m2B0 + 16);
    if (a2 == 0) goto loc_009EDD68;
    if ((((unsigned __int8)(v_r14)) & ((unsigned __int8)(*(unsigned __int64 *)(v_stack_m2B0 + 16)))) != 0) goto loc_009EEFC6;
    a1 = *(unsigned __int64 *)(v_stack_m2B0 + 16);
    if ((*(unsigned __int64 *)(v_stack_m2B0 + 16)) >= v_r13) { a1 = v_r13; }
    *(unsigned __int8 *)(a1) = (unsigned __int8)(*(unsigned __int8 *)(a1));
    *(unsigned __int8 *)(a1 + 63) = (unsigned __int8)(*(unsigned __int8 *)(a1 + 63));
loc_009EDD68:
    *(unsigned __int64 *)(a4 + 40) = v_stack_m190;
    v_stack_m290 = *(unsigned __int64 *)(v_stack_m2B0 + 24);
    if (*(unsigned __int64 *)(v_stack_m2B0 + 24) == 0) goto loc_009EEC57;
    if (a2 == 0) goto loc_009EDDA8;
    if ((((unsigned __int8)(v_r14)) & ((unsigned __int8)(*(unsigned __int64 *)(v_stack_m2B0 + 24)))) != 0) goto loc_009EEFCB;
    a1 = *(unsigned __int64 *)(v_stack_m2B0 + 24);
    if ((*(unsigned __int64 *)(v_stack_m2B0 + 24)) >= v_r13) { a1 = v_r13; }
    *(unsigned __int8 *)(a1) = (unsigned __int8)(*(unsigned __int8 *)(a1));
    *(unsigned __int8 *)(a1 + 7) = (unsigned __int8)(*(unsigned __int8 *)(a1 + 7));
loc_009EDDA8:
    *(unsigned __int64 *)(v_stack_m290) = 64;
    goto loc_009EEC57;
loc_009EDDB4:
    v_stack_m2A8 = *(unsigned __int64 *)(v_stack_m2B0 + 8);
    if (*(unsigned __int64 *)(v_stack_m2B0 + 8) == 0) goto loc_009ED8AD;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_m2B0 + 8))) & (7)) != 0) goto loc_009ED8AD;
    result = (*(unsigned __int64 *)(v_stack_m2B0 + 8)) & (-8);
    if (result > v_rsp) goto loc_009ED8AD;
    v_stack_m270 = *(unsigned __int64 *)(v_stack_m2B0 + 16);
    if (a2 == 0) goto loc_009EDE1E;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_m2B0 + 16))) & (3)) != 0) goto loc_009EEFD0;
    if ((*(unsigned __int64 *)(v_stack_m2B0 + 16) + *(unsigned __int64 *)(v_stack_m2B0 + 8) * 1) > v_r13) goto loc_009EDE08;
    result = *(unsigned __int64 *)(v_stack_m2B0 + 16) + *(unsigned __int64 *)(v_stack_m2B0 + 8) * 1;
    v_rbx = *(unsigned __int64 *)(v_stack_m2B0 + 8);
    v_rdi = v_stack_m2B0;
    v_r14 = *(unsigned __int64 *)(v_stack_m2B0 + 16);
    if ((*(unsigned __int64 *)(v_stack_m2B0 + 16) + *(unsigned __int64 *)(v_stack_m2B0 + 8) * 1) < (*(unsigned __int64 *)(v_stack_m2B0 + 16))) {
        result = *(unsigned __int8 *)(v_r13);
        v_rdi = v_stack_m2B0;
        v_r14 = v_stack_m270;
        v_rbx = v_stack_m2A8;
    }
    result = ExAllocatePool2(65, v_rbx, (unsigned int)(0x6C487350ULL), 65);
    *(unsigned __int64 *)(a4 + 296) = result;
    if (result == 0) goto loc_009EDB4A;
    result = memcpy(result, v_r14, v_rbx, 65);
    v_rbx = (v_rbx) >> (3);
    *(unsigned int *)(a4 + 292) = (unsigned int)(v_rbx);
    goto loc_009EEC57;
loc_009EDE5F:
    result = (result) - (0x2000DULL);
    if (condition_is_equal) goto loc_009EE260;
    result = (result) - (v_r14);
    if (condition_is_equal) goto loc_009EE1B8;
    result = (result) - (2);
    if (condition_is_equal) goto loc_009EE0FC;
    result = (result) - (1);
    if (condition_is_equal) goto loc_009EDFD9;
    result = (result) - (1);
    if (condition_is_equal) goto loc_009EDF8E;
    result = (result) - (1);
    if (condition_is_equal) goto loc_009EDF43;
    if (result != 1) goto loc_009EED70;
    if ((*(unsigned __int64 *)(v_rdi + 8)) != 8) goto loc_009ED8AD;
    v_stack_m188 = *(unsigned __int64 *)(v_rdi + 16);
    if (a2 == 0) goto loc_009EDEEA;
    if ((((unsigned __int8)(v_r14)) & ((unsigned __int8)(*(unsigned __int64 *)(v_rdi + 16)))) != 0) goto loc_009EEFD5;
    if ((*(unsigned __int64 *)(v_rdi + 16) + 8) > v_r13) goto loc_009EDED9;
    result = *(unsigned __int64 *)(v_rdi + 16) + 8;
    v_rbx = *(unsigned __int64 *)(v_rdi + 16);
    if ((*(unsigned __int64 *)(v_rdi + 16) + 8) < (*(unsigned __int64 *)(v_rdi + 16))) {
        result = *(unsigned __int8 *)(v_r13);
        v_rdi = v_stack_m2B0;
        v_rbx = v_stack_m188;
    }
    result = ExAllocatePool2(65, 8, (unsigned int)(0x77736350ULL), 65);
    *(unsigned __int64 *)(a4 + 432) = result;
    if (result != 0) goto loc_009EDF17;
loc_009EDF0D:
    goto loc_009EEEF0;
loc_009EDF17:
    *(unsigned __int64 *)(result) = *(unsigned __int64 *)((unsigned int)(0xC0000017ULL));
    if ((((unsigned __int8)(v_r14)) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 432)))))) == 0) goto loc_009ED8AD;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 432) + 4))) - 1);
    if (((unsigned int)(result)) <= 5) goto loc_009EEC57;
    goto loc_009ED8AD;
loc_009EDF43:
    if ((*(unsigned __int64 *)(v_rdi + 8)) != 4) goto loc_009ED8AD;
    v_stack_m180 = *(unsigned __int64 *)(v_rdi + 16);
    if (a2 == 0) goto loc_009EDF7F;
    if ((((unsigned __int8)(v_r14)) & ((unsigned __int8)(*(unsigned __int64 *)(v_rdi + 16)))) != 0) goto loc_009EEFDA;
    result = *(unsigned __int64 *)(v_rdi + 16);
    if ((*(unsigned __int64 *)(v_rdi + 16)) >= v_r13) { result = v_r13; }
loc_009EDF7F:
    *(unsigned int *)(a4 + 388) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m180)));
    goto loc_009EEC57;
loc_009EDF8E:
    if ((*(unsigned __int64 *)(v_stack_m2B0 + 8)) != 4) goto loc_009ED8AD;
    v_stack_m178 = *(unsigned __int64 *)(v_stack_m2B0 + 16);
    if (a2 == 0) goto loc_009EDFCA;
    if ((((unsigned __int8)(v_r14)) & ((unsigned __int8)(*(unsigned __int64 *)(v_stack_m2B0 + 16)))) != 0) goto loc_009EEFDF;
    result = *(unsigned __int64 *)(v_stack_m2B0 + 16);
    if ((*(unsigned __int64 *)(v_stack_m2B0 + 16)) >= v_r13) { result = v_r13; }
loc_009EDFCA:
    *(unsigned int *)(a4 + 384) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m178)));
    goto loc_009EEC57;
loc_009EDFD9:
    v_stack_m2A8 = *(unsigned __int64 *)(v_stack_m2B0 + 8);
    if (*(unsigned __int64 *)(v_stack_m2B0 + 8) == 0) goto loc_009ED8AD;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_m2B0 + 8))) & (7)) != 0) goto loc_009ED8AD;
    result = (*(unsigned __int64 *)(v_stack_m2B0 + 8)) & (-8);
    if (result > v_rsp) goto loc_009ED8AD;
    v_stack_m270 = *(unsigned __int64 *)(v_stack_m2B0 + 16);
    if (v_stack_p10 == 0) goto loc_009EE047;
    if ((((unsigned __int8)(v_r14)) & ((unsigned __int8)(*(unsigned __int64 *)(v_stack_m2B0 + 16)))) != 0) goto loc_009EEFE4;
    if ((*(unsigned __int64 *)(v_stack_m2B0 + 8) + *(unsigned __int64 *)(v_stack_m2B0 + 16) * 1) > v_r13) goto loc_009EE031;
    result = *(unsigned __int64 *)(v_stack_m2B0 + 8) + *(unsigned __int64 *)(v_stack_m2B0 + 16) * 1;
    v_rbx = *(unsigned __int64 *)(v_stack_m2B0 + 8);
    v_rdi = v_stack_m2B0;
    v_r15 = *(unsigned __int64 *)(v_stack_m2B0 + 16);
    if ((*(unsigned __int64 *)(v_stack_m2B0 + 8) + *(unsigned __int64 *)(v_stack_m2B0 + 16) * 1) < (*(unsigned __int64 *)(v_stack_m2B0 + 16))) {
        result = *(unsigned __int8 *)(v_r13);
        v_rdi = v_stack_m2B0;
        v_r15 = v_stack_m270;
        v_rbx = v_stack_m2A8;
    }
    result = ExAllocatePool2(65, v_rbx, (unsigned int)(0x6C4A7350ULL), 65);
    *(unsigned __int64 *)(a4 + 368) = result;
    if (result == 0) goto loc_009EDB4A;
    v_rbx = (v_rbx) >> (3);
    *(unsigned int *)(a4 + 380) = (unsigned int)(v_rbx);
    v_stack_m170 = 0;
loc_009EE080:
    if (0 >= ((unsigned int)(*(unsigned int *)(a4 + 380)))) goto loc_009EEC4F;
    v_stack_m2D0 = 0;
    v_stack_m2D8 = 0;
    v_stack_m2E0 = v_stack_m200;
    v_stack_m2E8 = 0x6C4A7350ULL;
    result = ObpReferenceObjectByHandleWithTag(*(unsigned __int64 *)(v_r15 + 0 * 8), 1, *(unsigned __int64 *)(v_rip + 6130624), v_stack_p10);
    v_stack_m2B8 = (unsigned int)(result);
    if (sign_flag) goto loc_009EEC92;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 368) + 0 * 8) = v_stack_m200;
    v_r14 = (0) + 1;
    v_stack_m170 = v_r14;
    goto loc_009EE080;
loc_009EE0FC:
    v_stack_m2A8 = *(unsigned __int64 *)(v_rdi + 8);
    if (*(unsigned __int64 *)(v_rdi + 8) == 0) goto loc_009ED8AD;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rdi + 8))) & (7)) != 0) goto loc_009ED8AD;
    if ((*(unsigned __int64 *)(v_rdi + 8)) > 136) goto loc_009ED8AD;
    v_stack_m168 = *(unsigned __int64 *)(v_rdi + 16);
    if ((unsigned __int8)(v_r15) == 0) goto loc_009EE163;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rdi + 16))) & (3)) != 0) goto loc_009EEFE9;
    if ((*(unsigned __int64 *)(v_rdi + 16) + *(unsigned __int64 *)(v_rdi + 8) * 1) > v_r13) goto loc_009EE14D;
    result = *(unsigned __int64 *)(v_rdi + 16) + *(unsigned __int64 *)(v_rdi + 8) * 1;
    v_rbx = *(unsigned __int64 *)(v_rdi + 8);
    v_r14 = *(unsigned __int64 *)(v_rdi + 16);
    if ((*(unsigned __int64 *)(v_rdi + 16) + *(unsigned __int64 *)(v_rdi + 8) * 1) < (*(unsigned __int64 *)(v_rdi + 16))) {
        result = *(unsigned __int8 *)(v_r13);
        v_rdi = v_stack_m2B0;
        v_rbx = v_stack_m2A8;
        v_r14 = v_stack_m168;
    }
    result = ExAllocatePool2(v_stack_p10, v_rbx, (unsigned int)(0x61547350ULL), v_stack_p10);
    *(unsigned __int64 *)(a4 + 360) = result;
    if (result == 0) goto loc_009EDB4A;
    result = memcpy(result, v_r14, v_rbx, v_stack_p10);
    *(unsigned int *)(a4 + 376) = (unsigned int)(v_rbx);
    result = IsTrustletCreateAttributeWellFormed(*(unsigned __int64 *)(a4 + 360), v_rbx, v_rbx, v_stack_p10);
loc_009EE1AB:
loc_009EE1AD:
    if ((unsigned __int8)(result) != 0) goto loc_009EEC57;
    goto loc_009ED8AD;
loc_009EE1B8:
    v_stack_m2A8 = *(unsigned __int64 *)(v_rdi + 8);
    if ((*(unsigned __int64 *)(v_rdi + 8)) > 24) goto loc_009ED8AD;
    result = 0;
    v_stack_m78 = v_xmm0;
    v_stack_m68 = 0;
    if ((unsigned __int8)(v_r15) == 0) goto loc_009EE204;
    a2 = *(unsigned __int64 *)(v_stack_m2B0 + 16);
    if ((*(unsigned __int64 *)(v_stack_m2B0 + 16)) >= v_r13) { a2 = v_r13; }
    result = RtlCopyVolatileMemory(v_stack_m78, a2, *(unsigned __int64 *)(v_rdi + 8), v_stack_p10);
    goto loc_009EE209;
loc_009EE204:
    result = memcpy(v_stack_m78, a2, *(unsigned __int64 *)(v_rdi + 8), v_stack_p10);
loc_009EE209:
    v_stack_mE8 = v_xmm2;
    v_stack_mD8 = v_xmm3;
    a2 = 0;
    result = PspValidateMitigationOptions(v_stack_mE8, a2, *(unsigned __int64 *)(v_rdi + 8), v_stack_p10);
    v_stack_m2B8 = (unsigned int)(result);
    if (sign_flag) goto loc_009EEC92;
    *(unsigned __int64 *)(a4 + 336) = v_xmm2;
    *(unsigned __int64 *)(a4 + 352) = v_xmm3;
    goto loc_009EEC57;
loc_009EE260:
    if ((*(unsigned __int64 *)(v_stack_m2B0 + 8)) != 2) goto loc_009ED8AD;
    v_stack_m160 = *(unsigned __int64 *)(v_stack_m2B0 + 16);
    if ((unsigned __int8)(v_r15) == 0) goto loc_009EE29B;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_m2B0 + 16))) & (1)) != 0) goto loc_009EEFEE;
    result = *(unsigned __int64 *)(v_stack_m2B0 + 16);
    if ((*(unsigned __int64 *)(v_stack_m2B0 + 16)) >= v_r13) { result = v_r13; }
loc_009EE29B:
    v_stack_m288 = (unsigned __int16)(*(unsigned __int16 *)(v_stack_m160));
    if (((unsigned __int16)(*(unsigned __int16 *)(v_stack_m160))) >= (*(unsigned __int16 *)(v_rip + 6122835))) goto loc_009ED8AD;
    a1 = (*(unsigned __int64 *)(v_rip + 6165510 + *(unsigned __int16 *)(v_stack_m160) * 8)) + (16);
    result = KeIsEmptyGroupMask(a1, a2, *(unsigned __int64 *)(v_rdi + 8), v_stack_p10);
    if ((unsigned int)(result) != 0) goto loc_009ED8AD;
    *(unsigned __int16 *)(a4 + 170) = (unsigned __int16)(*(unsigned __int16 *)(v_stack_m160));
    goto loc_009EEC57;
loc_009EE2DD:
    v_stack_m2A8 = *(unsigned __int64 *)(v_stack_m2B0 + 8);
    if ((*(unsigned __int64 *)(v_stack_m2B0 + 8)) != 524) goto loc_009ED8AD;
    v_stack_m158 = *(unsigned __int64 *)(v_stack_m2B0 + 16);
    if ((unsigned __int8)(v_r15) == 0) goto loc_009EE32C;
    if ((*(unsigned __int64 *)(v_stack_m2B0 + 8) + *(unsigned __int64 *)(v_stack_m2B0 + 16) * 1) > v_r13) goto loc_009EE316;
    result = *(unsigned __int64 *)(v_stack_m2B0 + 8) + *(unsigned __int64 *)(v_stack_m2B0 + 16) * 1;
    v_rbx = *(unsigned __int64 *)(v_stack_m2B0 + 8);
    v_rdi = v_stack_m2B0;
    v_r14 = *(unsigned __int64 *)(v_stack_m2B0 + 16);
    if ((*(unsigned __int64 *)(v_stack_m2B0 + 16) + *(unsigned __int64 *)(v_stack_m2B0 + 8) * 1) < (*(unsigned __int64 *)(v_stack_m2B0 + 16))) {
        result = *(unsigned __int8 *)(v_r13);
        v_rdi = v_stack_m2B0;
        v_rbx = v_stack_m2A8;
        v_r14 = v_stack_m158;
    }
    result = ExAllocatePool2(v_stack_p10, v_rbx, (unsigned int)(0x634F7350ULL), v_stack_p10);
    *(unsigned __int64 *)(a4 + 400) = result;
    if (result == 0) goto loc_009EDB4A;
    result = memcpy(result, v_r14, v_rbx, v_stack_p10);
    *(unsigned int *)(a4 + 396) = (unsigned int)(v_rbx);
loc_009EE371:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 400))))) & (64)) == 0) goto loc_009EEC57;
    goto loc_009ED8AD;
loc_009EE37C:
    if ((*(unsigned __int64 *)(a4 + 400)) > 0x3001EULL) goto loc_009EED2D;
    if ((*(unsigned __int64 *)(a4 + 400)) == 0x3001EULL) goto loc_009EEC9C;
    result = (*(unsigned __int64 *)(a4 + 400)) - (0x20018ULL);
    if (condition_is_equal) goto loc_009EE994;
    result = (result) - (1);
    if (condition_is_equal) goto loc_009EE949;
    result = (result) - (2);
    if (condition_is_equal) goto loc_009EE8A3;
    result = (result) - (2);
    if (condition_is_equal) goto loc_009EE840;
    result = (result) - (6);
    if (condition_is_equal) goto loc_009EE5EB;
    result = (result) - (1);
    if (condition_is_equal) goto loc_009EE49E;
    result = (result) - (0xFFE8ULL);
    if (condition_is_equal) goto loc_009EE43F;
    if (result != 2) goto loc_009EED70;
    if ((unsigned int)(v_rbx) == 0) goto loc_009ED8AD;
    if ((*(unsigned __int64 *)(v_rdi + 8)) != 4) goto loc_009ED8AD;
    v_stack_m150 = *(unsigned __int64 *)(v_rdi + 16);
    if ((unsigned __int8)(v_r15) == 0) goto loc_009EE422;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rdi + 16))) & (1)) != 0) goto loc_009EEFF3;
    result = *(unsigned __int64 *)(v_rdi + 16);
    if ((*(unsigned __int64 *)(v_rdi + 16)) >= v_r13) { result = v_r13; }
loc_009EE422:
    v_stack_m298 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m150)));
    result = KeGetProcessorIndexFromNumber(v_stack_m298, v_r14, v_rbx, v_stack_p10);
    *(unsigned int *)(a4 + 20) = (unsigned int)(result);
    goto loc_009EE1AD;
loc_009EE43F:
    if ((unsigned int)(v_rbx) == 0) goto loc_009ED8AD;
    if ((*(unsigned __int64 *)(v_stack_m2B0 + 8)) != v_rbx) goto loc_009ED8AD;
    v_stack_m148 = *(unsigned __int64 *)(v_stack_m2B0 + 16);
    if ((unsigned __int8)(v_r15) == 0) goto loc_009EE483;
    if ((((unsigned __int8)(v_r14)) & ((unsigned __int8)(*(unsigned __int64 *)(v_stack_m2B0 + 16)))) != 0) goto loc_009EEFF8;
    result = *(unsigned __int64 *)(v_stack_m2B0 + 16);
    if ((*(unsigned __int64 *)(v_stack_m2B0 + 16)) >= v_r13) { result = v_r13; }
loc_009EE483:
    *(unsigned __int64 *)(a4 + 320) = v_xmm0;
    result = KeVerifyGroupAffinity(a4 + 320, 1, v_rbx, v_stack_p10);
    goto loc_009EE1AB;
loc_009EE49E:
    result = Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline(a4 + 320, 1, v_rbx, v_stack_p10);
    if ((unsigned int)(result) == 0) goto loc_009ED8AD;
    if ((*(unsigned __int64 *)(v_stack_m2B0 + 8)) != v_rbx) goto loc_009ED8AD;
    v_stack_mA0 = *(unsigned __int64 *)(v_stack_m2B0 + 16);
    if ((unsigned __int8)(v_r15) == 0) goto loc_009EE4E6;
    if ((((unsigned __int8)(v_r14)) & ((unsigned __int8)(*(unsigned __int64 *)(v_stack_m2B0 + 16)))) != 0) goto loc_009EEFFD;
    if ((unsigned __int8)(v_r15) == 0) goto loc_009EE4E6;
    result = RtlCopyFromUser(v_stack_m248, *(unsigned __int64 *)(v_stack_m2B0 + 16), v_rbx, v_stack_p10);
    goto loc_009EE4F6;
loc_009EE4E6:
    result = RtlCopyVolatileMemory(v_stack_m248, *(unsigned __int64 *)(v_stack_m2B0 + 16), v_rbx, v_stack_p10);
loc_009EE4F6:
    if (v_stack_m248 != 1) goto loc_009ED8AD;
    if (v_stack_m240 == 0) goto loc_009ED8AD;
    if ((unsigned __int8)(v_r15) == 0) goto loc_009EE53D;
    if ((((unsigned __int8)(v_r14)) & ((unsigned __int8)(v_stack_m240))) != 0) goto loc_009EF002;
    if ((unsigned __int8)(v_r15) == 0) goto loc_009EE53D;
    result = RtlCopyFromUser(v_stack_m98, v_stack_m240, 28, v_stack_p10);
    goto loc_009EE550;
loc_009EE53D:
    result = RtlCopyVolatileMemory(v_stack_m98, v_stack_m240, 28, v_stack_p10);
loc_009EE550:
    if (v_stack_m98 != 28) goto loc_009ED8AD;
    if (((v_stack_m94) & (0xFFFFFFFEULL)) != 0) goto loc_009ED8AD;
    if (((v_stack_m90) & (0xFFFFFFFEULL)) != 0) goto loc_009ED8AD;
    if (((v_stack_m8C) & (0xFFFFFFE0ULL)) != 0) goto loc_009ED8AD;
    if (((v_stack_m88) & (0xFFFFFFF8ULL)) != 0) goto loc_009ED8AD;
    if (((v_stack_m84) & (0xFFFFFFFCULL)) != 0) goto loc_009ED8AD;
    *(unsigned __int64 *)(a4 + 528) = v_xmm0;
    *(unsigned __int64 *)(a4 + 544) = v_xmm0;
    *(unsigned int *)(a4 + 552) = (unsigned int)((unsigned int)(v_stack_m80));
    goto loc_009EEC57;
loc_009EE5EB:
    result = Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline(v_stack_m98, v_stack_m240, 28, v_stack_p10);
    if ((unsigned int)(result) == 0) goto loc_009ED8AD;
    if ((*(unsigned __int64 *)(v_stack_m2B0 + 8)) < 32) goto loc_009ED8AD;
    v_stack_m100 = *(unsigned __int64 *)(v_stack_m2B0 + 16);
    if ((unsigned __int8)(v_r15) == 0) goto loc_009EE637;
    if ((((unsigned __int8)(v_r14)) & ((unsigned __int8)(*(unsigned __int64 *)(v_stack_m2B0 + 16)))) != 0) goto loc_009EF007;
    if ((unsigned __int8)(v_r15) == 0) goto loc_009EE637;
    result = RtlCopyFromUser(v_stack_m268, *(unsigned __int64 *)(v_stack_m2B0 + 16), 32, v_stack_p10);
    goto loc_009EE64A;
loc_009EE637:
    result = RtlCopyVolatileMemory(v_stack_m268, *(unsigned __int64 *)(v_stack_m2B0 + 16), 32, v_stack_p10);
loc_009EE64A:
    if (v_stack_m268 < 1) goto loc_009ED8AD;
    if ((unsigned __int8)(v_r15) == 0) goto loc_009EE68D;
    if (((v_stack_m260) & ((unsigned __int8)(v_r14))) != 0) goto loc_009EF00C;
    if ((unsigned __int8)(v_r15) == 0) goto loc_009EE68D;
    result = RtlCopyFromUser(v_stack_m238, v_stack_m260, 48, v_stack_p10);
    goto loc_009EE6A8;
loc_009EE68D:
    result = RtlCopyVolatileMemory(v_stack_m238, v_stack_m260, 48, v_stack_p10);
loc_009EE6A8:
    if (v_stack_m238 > 48) goto loc_009ED8AD;
    if (v_stack_m228 == 0) goto loc_009ED8AD;
    if (v_stack_m218 != 0) goto loc_009EE6E0;
    if (v_stack_m220 != 0) goto loc_009EE6EA;
    if (v_stack_m218 == 0) goto loc_009EE6F4;
loc_009EE6E0:
    if (v_stack_m220 != 0) goto loc_009EE6F4;
loc_009EE6EA:
    goto loc_009EEEF0;
loc_009EE6F4:
    result = ExAllocatePool2(256, 48, (unsigned int)(0x63437350ULL), v_stack_p10);
    *(unsigned __int64 *)(a4 + 504) = result;
    if (result == 0) goto loc_009EDF0D;
    *(unsigned int *)(a4 + 496) = (unsigned int)((unsigned int)(v_stack_m268));
    *(unsigned int *)(result) = (unsigned int)(v_stack_m238);
    *(unsigned int *)(*(unsigned __int64 *)(a4 + 504) + 4) = (unsigned int)((unsigned int)(v_stack_m234));
    *(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 504) + 8) = v_stack_m230;
    *(unsigned int *)(*(unsigned __int64 *)(a4 + 504) + 40) = (unsigned int)((unsigned int)(v_stack_m210));
    result = (*(unsigned __int64 *)(a4 + 504)) + ((unsigned int)(0xC0000030ULL));
    v_stack_m2D8 = result;
    v_stack_m2E0 = 1;
    result = SeCaptureSid(v_stack_m228, (unsigned __int8)(v_r15), (unsigned int)(0x63437350ULL), v_stack_p10);
    v_stack_m2B8 = (unsigned int)(result);
    if (sign_flag) goto loc_009EEC92;
    if (v_stack_m220 == 0) goto loc_009EE802;
    result = (*(unsigned __int64 *)(a4 + 504)) + (24);
    v_stack_m2C8 = v_stack_m280;
    v_stack_m2D0 = result;
    v_stack_m2E8 = 0;
    a4 = 0;
    result = SeCaptureSidAndAttributesArray(v_stack_m220, (unsigned int)(v_stack_m218), (unsigned __int8)(v_r15), a4);
    v_stack_m2B8 = (unsigned int)(result);
    if (sign_flag) goto loc_009EEC92;
    *(unsigned int *)(*(unsigned __int64 *)(a4 + 504) + 32) = (unsigned int)((unsigned int)(v_stack_m218));
loc_009EE802:
    result = SeCaptureHandles((unsigned int)(v_stack_m250), v_stack_m258, a4 + 512, a4);
    v_stack_m2B8 = (unsigned int)(result);
    if (sign_flag) goto loc_009EEC92;
    *(unsigned int *)(a4 + 520) = (unsigned int)((unsigned int)(v_stack_m250));
    goto loc_009EEC57;
loc_009EE840:
    if ((*(unsigned __int64 *)(v_stack_m2B0 + 8)) != 4) goto loc_009ED8AD;
    v_stack_m140 = *(unsigned __int64 *)(v_stack_m2B0 + 16);
    if ((unsigned __int8)(v_r15) == 0) goto loc_009EE884;
    if ((((unsigned __int8)(v_r14)) & ((unsigned __int8)(*(unsigned __int64 *)(v_stack_m2B0 + 16)))) != 0) goto loc_009EF011;
    if ((*(unsigned __int64 *)(v_stack_m2B0 + 16) + 4) > v_r13) goto loc_009EE873;
    result = *(unsigned __int64 *)(v_stack_m2B0 + 16) + 4;
    v_rdi = v_stack_m2B0;
    if ((*(unsigned __int64 *)(v_stack_m2B0 + 16) + 4) < (*(unsigned __int64 *)(v_stack_m2B0 + 16))) {
        result = *(unsigned __int8 *)(v_r13);
        v_rdi = v_stack_m2B0;
        a1 = v_stack_m140;
    }
    if (((*(unsigned int *)(a1)) & (0xFFFFFFFEULL)) == 0) goto loc_009EE896;
    goto loc_009EEF75;
loc_009EE896:
    *(unsigned __int64 *)(a4 + 440) = a1;
    goto loc_009EEC57;
loc_009EE8A3:
    v_stack_m2A8 = *(unsigned __int64 *)(v_rdi + 8);
    if ((*(unsigned __int64 *)(v_rdi + 8)) > 24) goto loc_009ED8AD;
    result = 0;
    v_stack_m60 = v_xmm0;
    v_stack_m50 = 0;
    if ((unsigned __int8)(v_r15) == 0) goto loc_009EE8EF;
    a2 = *(unsigned __int64 *)(v_stack_m2B0 + 16);
    if ((*(unsigned __int64 *)(v_stack_m2B0 + 16)) >= v_r13) { a2 = v_r13; }
    result = RtlCopyVolatileMemory(v_stack_m60, a2, *(unsigned __int64 *)(v_rdi + 8), a4);
    goto loc_009EE8F4;
loc_009EE8EF:
    result = memcpy(v_stack_m60, a2, *(unsigned __int64 *)(v_rdi + 8), a4);
loc_009EE8F4:
    v_stack_mC8 = v_xmm2;
    v_stack_mB8 = v_xmm3;
    result = PspValidateMitigationAuditOptions(v_stack_mC8, a2, *(unsigned __int64 *)(v_rdi + 8), a4);
    v_stack_m2B8 = (unsigned int)(result);
    if (sign_flag) goto loc_009EEC92;
    *(unsigned __int64 *)(a4 + 448) = v_xmm2;
    *(unsigned __int64 *)(a4 + 464) = v_xmm3;
    goto loc_009EEC57;
loc_009EE949:
    if ((*(unsigned __int64 *)(v_stack_m2B0 + 8)) != 4) goto loc_009ED8AD;
    v_stack_m138 = *(unsigned __int64 *)(v_stack_m2B0 + 16);
    if ((unsigned __int8)(v_r15) == 0) goto loc_009EE985;
    if ((((unsigned __int8)(v_r14)) & ((unsigned __int8)(*(unsigned __int64 *)(v_stack_m2B0 + 16)))) != 0) goto loc_009EF016;
    result = *(unsigned __int64 *)(v_stack_m2B0 + 16);
    if ((*(unsigned __int64 *)(v_stack_m2B0 + 16)) >= v_r13) { result = v_r13; }
loc_009EE985:
    *(unsigned int *)(a4 + 392) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m138)));
    goto loc_009EEC57;
loc_009EE994:
    v_stack_m2A8 = *(unsigned __int64 *)(v_stack_m2B0 + 8);
    if ((*(unsigned __int64 *)(v_stack_m2B0 + 8)) != 40) goto loc_009ED8AD;
    v_stack_m130 = *(unsigned __int64 *)(v_stack_m2B0 + 16);
    if (v_stack_p10 == 0) goto loc_009EE9E4;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_m2B0 + 16))) & (3)) != 0) goto loc_009EF01B;
    v_r14 = *(unsigned __int64 *)(v_stack_m2B0 + 16);
    if ((*(unsigned __int64 *)(v_stack_m2B0 + 16)) >= v_r13) { v_r14 = v_r13; }
loc_009EE9E4:
    result = ExAllocatePool2(0, v_stack_m2A8, (unsigned int)(0x70426E50ULL), a4);
    *(unsigned __int64 *)(a4 + 408) = result;
    if (result == 0) goto loc_009EDB4A;
    v_stack_m27C = 0;
    result = memcpy(result, v_stack_m130, v_stack_m2A8, a4);
    goto loc_009EEA7F;
loc_009EEA7F:
    if (sign_flag) goto loc_009EEEF0;
    v_stack_m1E0 = *(unsigned __int64 *)(a4 + 408);
    v_stack_m1F0 = *(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 408) + 8);
    v_stack_m1E8 = *(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 408) + 24);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 408) + 8) = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 408) + 24) = 0;
    if ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a4 + 408) + 2)) == 0) goto loc_009EEB3B;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a4 + 408)))) > ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a4 + 408) + 2)))) goto loc_009ED8AD;
    if ((((unsigned __int8)(*(unsigned __int16 *)(*(unsigned __int64 *)(a4 + 408)))) & (1)) != 0) goto loc_009ED8AD;
    if ((((unsigned __int8)(*(unsigned __int16 *)(*(unsigned __int64 *)(a4 + 408) + 2))) & (1)) != 0) goto loc_009ED8AD;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a4 + 408) + 2))) > ((unsigned __int16)((unsigned int)(0xFFFEULL)))) goto loc_009ED8AD;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 408) + 8) == 0) goto loc_009ED8AD;
    if ((unsigned __int8)(v_stack_p10) == 0) goto loc_009EEB43;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a4 + 408) + 2) + *(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 408) + 8) * 1) > v_stack_m2A8) goto loc_009EEB19;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a4 + 408) + 2) + *(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 408) + 8) * 1) >= (*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 408) + 8))) goto loc_009EEB43;
loc_009EEB19:
    goto loc_009EEB43;
loc_009EEB3B:
loc_009EEB43:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 408) + 16))) == 0) goto loc_009EEBBA;
    if (v_stack_m1E8 == 0) goto loc_009ED8AD;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 408) + 16)))) > 0xFFFFULL) goto loc_009ED8AD;
    if ((unsigned __int8)(v_stack_p10) == 0) goto loc_009EEBBA;
    if ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 408) + 16)) * 8 == 0) goto loc_009EEBBA;
    if ((((unsigned __int8)(v_stack_m1E8)) & (3)) != 0) goto loc_009EF020;
    a2 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 408) + 16)) * 8) + (v_stack_m1E8);
    if (a2 > v_stack_m2A8) goto loc_009EEB93;
    result = *(unsigned __int64 *)(a4 + 408);
    v_rdi = v_stack_m2B0;
    v_r13 = v_stack_m1F0;
    v_r14 = v_stack_m1E0;
    v_r15 = v_stack_m1E8;
    if (a2 < v_stack_m1E8) {
        result = *(unsigned __int8 *)(v_stack_m2A8);
        result = *(unsigned __int64 *)(v_stack_m1F8 + 408);
        v_rdi = v_stack_m2B0;
        v_r13 = v_stack_m1F0;
        v_r15 = v_stack_m1E8;
        v_r14 = v_stack_m1E0;
    }
    v_stack_m1D8 = 0;
    if ((unsigned __int16)(*(unsigned __int16 *)(v_r14 + 2)) != 0) goto loc_009EEBD4;
    v_rbx = 0;
    if ((*(unsigned int *)(result + 16)) >= = 0) {
        a1 = *(unsigned int *)(result + 16);
        a2 = *(unsigned __int16 *)(v_r14 + 2) + a1 * 8;
        a1 = 65;
        a3 = 0x70426E50ULL;
        result = ExAllocatePool2(a1, a2, a3, v_stack_p10);
        v_rbx = result;
        v_stack_m1D8 = result;
    }
    result = *(unsigned __int16 *)(v_r14 + 2);
    if ((unsigned __int16)(*(unsigned __int16 *)(v_r14 + 2)) != 0) {
        *(unsigned __int64 *)(v_r14 + 8) = v_rbx;
        a3 = (unsigned int)(*(unsigned __int16 *)(v_r14 + 2));
        a2 = v_r13;
        a1 = v_rbx;
        result = memcpy(a1, a2, a3, v_stack_p10);
        a1 = *(unsigned __int16 *)(v_r14 + 2);
        v_rbx = (v_rbx) + (a1);
        v_stack_m1D8 = v_rbx;
    }
    result = *(unsigned __int64 *)(a4 + 408);
    if ((*(unsigned int *)(*(unsigned __int64 *)(a4 + 408) + 16)) >= = 0) {
        *(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 408) + 24) = v_rbx;
        a1 = *(unsigned __int64 *)(a4 + 408);
        a3 = *(unsigned int *)(a1 + 16);
        a3 = (a3) << (3);
        a2 = v_r15;
        a1 = *(unsigned __int64 *)(a1 + 24);
        result = memcpy(a1, a2, a3, v_stack_p10);
    }
loc_009EEC57:
    result = Feature_CreateProcessSegmentHeapEnablement__private_IsEnabledDeviceUsageNoInline(a1, a2, a3, v_stack_p10);
    if ((unsigned int)(result) == 0) goto loc_009EEEBB;
    if (((v_stack_m1D0) & (0x80000ULL)) == 0) goto loc_009EEEBB;
    result = PspProcessUserCopyAttribute(v_rdi, (unsigned __int8)(v_stack_p10), 0, v_stack_p10);
    v_stack_m2B8 = (unsigned int)(result);
    if (!sign_flag) goto loc_009EEEBB;
loc_009EEC92:
    goto loc_009EEEF9;
loc_009EEC9C:
    if (0 == 0) goto loc_009ED8AD;
    if ((*(unsigned __int64 *)((unsigned int)(0xC000000DULL) + 8)) != 8) goto loc_009ED8AD;
    v_stack_m120 = *(unsigned __int64 *)((unsigned int)(0xC000000DULL) + 16);
    if ((unsigned __int8)(v_stack_p10) == 0) goto loc_009EECE1;
    if ((((unsigned __int8)(v_r14)) & ((unsigned __int8)(*(unsigned __int64 *)((unsigned int)(0xC000000DULL) + 16)))) != 0) goto loc_009EF025;
    result = *(unsigned __int64 *)((unsigned int)(0xC000000DULL) + 16);
    if ((*(unsigned __int64 *)((unsigned int)(0xC000000DULL) + 16)) >= v_r13) { result = v_r13; }
loc_009EECE1:
    *(unsigned __int64 *)(a4 + 480) = *(unsigned __int64 *)(v_stack_m120);
    a1 = (*(unsigned __int64 *)(v_rdi)) | (*(unsigned __int64 *)(v_stack_m120));
    v_stack_mF8 = a1;
    a1 = ~(a1);
    if (((*(unsigned __int64 *)(v_stack_m120)) & (a1)) != 0) goto loc_009ED8AD;
    a2 = (unsigned int)((*(unsigned __int64 *)(v_stack_m120)) & (0x40000ULL));
    *(unsigned __int64 *)(a4 + 480) = a2;
    goto loc_009EEC57;
loc_009EED2D:
    result = (v_stack_m120) - (0x60000ULL);
    if (condition_is_equal) goto loc_009EEE9F;
    result = (result) - (1);
    if (condition_is_equal) goto loc_009EEE83;
    result = (result) - (1);
    if (condition_is_equal) goto loc_009EEE67;
    result = (result) - (15);
    if (condition_is_equal) goto loc_009EEE4A;
    result = (result) - (9);
    if (condition_is_equal) goto loc_009EEE20;
    result = (result) - (2);
    if (condition_is_equal) goto loc_009EEE03;
    if (result == v_r14) goto loc_009EEDDA;
loc_009EED70:
    result = Feature_CreateProcessSegmentHeapEnablement__private_IsEnabledDeviceUsageNoInline(a1, a2, 0, v_stack_p10);
    if ((unsigned int)(result) == 0) goto loc_009ED8AD;
    result = PspIsAttributeRemoved(v_stack_m1D0, a2, v_stack_m1D0, v_stack_p10);
    if (((unsigned __int16)(v_stack_m1D0)) >= 37) goto loc_009ED8AD;
    if (((unsigned __int16)(v_stack_m1D0)) >= 37) goto loc_009ED8AD;
    if ((unsigned int)(result) != 0) goto loc_009ED8AD;
    result = PspGetAttributeValueSize(v_stack_m1D0, a2, v_stack_m1D0, v_stack_p10);
    result = PspGetFullAttribute((unsigned __int16)(v_stack_m1D0), result, v_stack_m1D0, v_stack_p10);
    if (result == 0) goto loc_009ED8AD;
    if ((*(unsigned __int64 *)(v_stack_m2B0 + 8)) != result) goto loc_009ED8AD;
    goto loc_009EE371;
loc_009EEDDA:
    if ((*(unsigned __int64 *)(v_stack_m2B0 + 8)) != 4) goto loc_009ED8AD;
    if (((*(unsigned __int64 *)(v_stack_m2B0 + 16)) & (-8)) != 0) goto loc_009ED8AD;
    *(unsigned int *)(a4 + 488) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m2B0 + 16)));
    goto loc_009EEC57;
loc_009EEE03:
    if ((*(unsigned __int64 *)(v_stack_m2B0 + 8)) != 2) goto loc_009ED8AD;
    *(unsigned __int16 *)(a4 + 168) = (unsigned __int16)(*(unsigned __int16 *)(v_stack_m2B0 + 16));
    goto loc_009EEC57;
loc_009EEE20:
    if ((*(unsigned __int64 *)(v_stack_m2B0 + 8)) != 1) goto loc_009ED8AD;
    result = -(*(unsigned __int64 *)(v_stack_m2B0 + 16));
    a1 = (unsigned __int8)(((unsigned __int16)(v_stack_m1D0)) & (128));
    result = (unsigned __int8)((*(unsigned __int8 *)(a4 + 17)) & (127));
    a1 = (unsigned __int8)((a1) | ((unsigned __int8)(result)));
    *(unsigned __int8 *)(a4 + 17) = (unsigned __int8)(a1);
    goto loc_009EEC57;
loc_009EEE4A:
    if ((*(unsigned __int64 *)(v_stack_m2B0 + 8)) != 1) goto loc_009ED8AD;
    *(unsigned __int8 *)(a4 + 1) = (unsigned __int8)(*(unsigned __int8 *)(v_stack_m2B0 + 16));
    result = RtlValidProcessProtection(*(unsigned __int8 *)(v_stack_m2B0 + 16), result, v_stack_m1D0, v_stack_p10);
    goto loc_009EE1AB;
loc_009EEE67:
    if ((*(unsigned __int64 *)(v_stack_m2B0 + 8)) != 8) goto loc_009ED8AD;
    *(unsigned __int64 *)(a4 + 152) = *(unsigned __int64 *)(v_stack_m2B0 + 16);
    goto loc_009EEC57;
loc_009EEE83:
    if ((*(unsigned __int64 *)(v_stack_m2B0 + 8)) != 8) goto loc_009ED8AD;
    *(unsigned __int64 *)(a4 + 144) = *(unsigned __int64 *)(v_stack_m2B0 + 16);
    goto loc_009EEC57;
loc_009EEE9F:
    if ((*(unsigned __int64 *)(v_stack_m2B0 + 8)) != 8) goto loc_009ED8AD;
    *(unsigned __int64 *)(a4 + 128) = *(unsigned __int64 *)(v_stack_m2B0 + 16);
    goto loc_009EEC57;
loc_009EEEBB:
    v_rdi = (v_stack_m2B0) + (32);
    v_stack_m2B0 = v_rdi;
    goto loc_009ED877;
loc_009EEEEE:
loc_009EEEF0:
loc_009EEEF5:
    v_stack_m2B8 = 0;
loc_009EEEF9:
    goto loc_009EEF10;
loc_009EEF10:
    if (sign_flag) goto loc_009EEF6B;
    result = (unsigned int)(*(unsigned int *)(a4 + 8));
    v_rbx = 0;
    if (!(condition_is_above_or_equal)) {
        a2 = *(unsigned int *)(a4 + 292);
        a4 = v_rip + 633473;
        a3 = 8;
        a1 = *(unsigned __int64 *)(a4 + 296);
        result = qsort(a1, a2, a3, a4);
        result = *(unsigned __int64 *)(a4 + 296);
        v_rbx = 0;
        if ((*(unsigned int *)(result)) < 0) { v_rbx = (unsigned int)((unsigned int)(0xC000000DULL)); }
        a2 = (v_stack_m278 != 0) ? 1 : 0;
        result = *(unsigned __int8 *)(a4 + 16);
        result = (unsigned __int8)((result) & (254));
        a2 = (unsigned __int8)((a2) | ((unsigned __int8)(result)));
        *(unsigned __int8 *)(a4 + 16) = a2;
    }
    if (sign_flag) {
        a1 = a4;
        result = PspDeleteCreateProcessContext(a1, a2, a3, a4);
    }
loc_009EEF75:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (720);
    return result;
loc_009EEF99:
    result = ExRaiseDatatypeMisalignment(a1, a2, a3, a4);
loc_009EEF9E:
    result = ExRaiseDatatypeMisalignment(a1, a2, a3, a4);
loc_009EEFA3:
    result = ExRaiseDatatypeMisalignment(a1, a2, a3, a4);
loc_009EEFA8:
    result = ExRaiseDatatypeMisalignment(a1, a2, a3, a4);
loc_009EEFAD:
    result = ExRaiseDatatypeMisalignment(a1, a2, a3, a4);
loc_009EEFB2:
    result = ExRaiseDatatypeMisalignment(a1, a2, a3, a4);
loc_009EEFB7:
    result = ExRaiseDatatypeMisalignment(a1, a2, a3, a4);
loc_009EEFBC:
    result = ExRaiseDatatypeMisalignment(a1, a2, a3, a4);
loc_009EEFC1:
    result = ExRaiseDatatypeMisalignment(a1, a2, a3, a4);
loc_009EEFC6:
    result = ExRaiseDatatypeMisalignment(a1, a2, a3, a4);
loc_009EEFCB:
    result = ExRaiseDatatypeMisalignment(a1, a2, a3, a4);
loc_009EEFD0:
    result = ExRaiseDatatypeMisalignment(a1, a2, a3, a4);
loc_009EEFD5:
    result = ExRaiseDatatypeMisalignment(a1, a2, a3, a4);
loc_009EEFDA:
    result = ExRaiseDatatypeMisalignment(a1, a2, a3, a4);
loc_009EEFDF:
    result = ExRaiseDatatypeMisalignment(a1, a2, a3, a4);
loc_009EEFE4:
    result = ExRaiseDatatypeMisalignment(a1, a2, a3, a4);
loc_009EEFE9:
    result = ExRaiseDatatypeMisalignment(a1, a2, a3, a4);
loc_009EEFEE:
    result = ExRaiseDatatypeMisalignment(a1, a2, a3, a4);
loc_009EEFF3:
    result = ExRaiseDatatypeMisalignment(a1, a2, a3, a4);
loc_009EEFF8:
    result = ExRaiseDatatypeMisalignment(a1, a2, a3, a4);
loc_009EEFFD:
    result = ExRaiseDatatypeMisalignment(a1, a2, a3, a4);
loc_009EF002:
    result = ExRaiseDatatypeMisalignment(a1, a2, a3, a4);
loc_009EF007:
    result = ExRaiseDatatypeMisalignment(a1, a2, a3, a4);
loc_009EF00C:
    result = ExRaiseDatatypeMisalignment(a1, a2, a3, a4);
loc_009EF011:
    result = ExRaiseDatatypeMisalignment(a1, a2, a3, a4);
loc_009EF016:
    result = ExRaiseDatatypeMisalignment(a1, a2, a3, a4);
loc_009EF01B:
    result = ExRaiseDatatypeMisalignment(a1, a2, a3, a4);
loc_009EF020:
    result = ExRaiseDatatypeMisalignment(a1, a2, a3, a4);
loc_009EF025:
    result = ExRaiseDatatypeMisalignment(a1, a2, a3, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PspBuildCreateProcessContext(int64_t Arg1, uint8_t Arg2, int32_t Arg3, void *Arg4)
{
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint64_t v_stack_m148;
    uint64_t v_stack_m150;
    uint64_t v_stack_m158;
    uint64_t v_stack_m160;
    uint64_t v_stack_m168;
    uint64_t v_stack_m170;
    uint64_t v_stack_m178;
    uint64_t v_stack_m180;
    uint64_t v_stack_m188;
    uint64_t v_stack_m190;
    uint64_t v_stack_m198;
    uint64_t v_stack_m1A0;
    uint64_t v_stack_m1A8;
    uint64_t v_stack_m1B0;
    uint32_t v_stack_m1B8;
    uint64_t v_stack_m1C0;
    uint64_t v_stack_m1C8;
    uint64_t v_stack_m1D0;
    uint64_t v_stack_m1D8;
    uint64_t v_stack_m1E0;
    uint64_t v_stack_m1E8;
    uint64_t v_stack_m1F0;
    uint64_t v_stack_m1F8;
    uint64_t v_stack_m200;
    uint64_t v_stack_m208;
    uint32_t v_stack_m210;
    uint64_t v_stack_m218;
    uint64_t v_stack_m220;
    uint64_t v_stack_m228;
    uint64_t v_stack_m230;
    uint32_t v_stack_m234;
    uint64_t v_stack_m238;
    uint64_t v_stack_m240;
    uint64_t v_stack_m248;
    uint32_t v_stack_m250;
    uint64_t v_stack_m258;
    uint8_t v_stack_m260;
    uint64_t v_stack_m268;
    uint64_t v_stack_m270;
    uint32_t v_stack_m278;
    uint32_t v_stack_m27C;
    uint32_t v_stack_m280;
    uint32_t v_stack_m284;
    uint16_t v_stack_m288;
    uint64_t v_stack_m290;
    uint32_t v_stack_m298;
    uint64_t v_stack_m2A0;
    uint64_t v_stack_m2A8;
    uint64_t v_stack_m2B0;
    uint32_t v_stack_m2B8;
    uint64_t v_stack_m2C8;
    uint64_t v_stack_m2D0;
    uint64_t v_stack_m2D8;
    uint64_t v_stack_m2E0;
    uint32_t v_stack_m2E8;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m78;
    uint32_t v_stack_m80;
    uint32_t v_stack_m84;
    uint32_t v_stack_m88;
    uint32_t v_stack_m8C;
    uint32_t v_stack_m90;
    uint32_t v_stack_m94;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint8_t v_stack_p10;
    uint32_t v_stack_p18;

    *(uint32_t *)(local_rsp + 0x18) = Arg3;
    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (720);
    result = (*(uint64_t *)(v_rip + 0x41D03C)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m1F8 = Arg4;
    v_stack_m278 = Arg3;
    v_stack_m1C0 = Arg4;
    v_stack_m1C8 = Arg4;
    v_stack_m238 = v_xmm0;
    v_stack_m228 = v_xmm0;
    v_stack_m218 = v_xmm0;
    result = 0;
    v_stack_m268 = v_xmm0;
    *(uint64_t *)(local_rsp - 0x258) = 0;
    v_stack_m250 = 0;
    v_stack_m98 = v_xmm0;
    *(uint64_t *)(local_rsp - 0x88) = 0;
    *(uint32_t *)(local_rsp - 0x80) = 0;
    *(uint64_t *)(local_rsp - 0x244) = 0;
    *(uint64_t *)(local_rsp - 0x248) = 0;
    *(uint64_t *)(local_rsp - 0x60) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x50) = 0;
    *(uint64_t *)(local_rsp - 0x78) = v_xmm1;
    *(uint64_t *)(local_rsp - 0x68) = 0;
    local_rsi = 0;
    v_stack_m298 = 0;
    v_stack_m280 = 0;
    *(uint64_t *)(local_rsp - 0x200) = 0;
    v_stack_m2A8 = 0;
    *(uint64_t *)(local_rsp - 0x208) = 0;
    v_stack_m284 = 0;
    *(uint8_t *)(arg4) = Arg2;
    if (Arg2 == 0) goto loc_009ED7F8;
    if ((((uint8_t)(result + 3)) & ((uint8_t)(Arg1))) != 0) goto loc_009EEF99;
    result = local_r13;
    if (Arg1 < local_r13) { result = Arg1; }
    goto loc_009ED802;
loc_009ED7F8:
loc_009ED802:
    v_stack_m2A0 = *(uint64_t *)(Arg1);
    if ((*(uint64_t *)(Arg1)) >= 40) goto loc_009ED81A;
    goto loc_009EEF75;
loc_009ED81A:
    if (Arg2 == 0) goto loc_009ED84C;
    result = (v_stack_m2A0) + (-40);
    if (condition_is_equal) goto loc_009ED84C;
    if ((((uint8_t)(result + 3)) & ((uint8_t)(Arg1))) != 0) goto loc_009EEF9E;
    Arg2 = (v_stack_m2A0) + (Arg1);
    if (Arg2 > local_r13) goto loc_009ED848;
    result = Arg1 + 40;
    if (Arg2 < (Arg1 + 40)) {
        result = *(uint8_t *)(local_r13);
    }
    result = (v_stack_m2A0) - (8);
    v_stack_m2A0 = result;
    if ((((uint8_t)(result)) & (31)) == 0) goto loc_009ED868;
    goto loc_009EEF75;
loc_009ED868:
    v_stack_m2B0 = Arg1 + 8;
loc_009ED877:
    if (v_stack_m2A0 <= 0) goto loc_009EEEEE;
    v_stack_m1D0 = *(uint64_t *)(Arg1 + 0x8);
    if (Arg3 == 0) goto loc_009ED8B9;
    if (condition_is_below) goto loc_009ED8B9;
loc_009ED8AD:
    goto loc_009EEEF5;
loc_009ED8B9:
    if (condition_is_above_or_equal) goto loc_009ED8C6;
    if ((*(uint64_t *)((uint32_t)(0xC000000DULL) + 0x18)) != 0) goto loc_009ED8AD;
loc_009ED8C6:
    Arg2 = (1) << ((uint8_t)((uint8_t)(*(uint64_t *)(Arg1 + 0x8))));
    v_stack_mF0 = Arg2;
    if (((Arg2) & (*(uint64_t *)(arg4 + 0x8))) != 0) goto loc_009ED8AD;
    Arg1 = (*(uint64_t *)(arg4 + 0x8)) | (Arg2);
    *(uint64_t *)(arg4 + 0x8) = Arg1;
    if ((*(uint64_t *)(Arg1 + 0x8)) > 0x20017ULL) goto loc_009EE37C;
    if ((*(uint64_t *)(Arg1 + 0x8)) == 0x20017ULL) goto loc_009EE2DD;
    if ((*(uint64_t *)(Arg1 + 0x8)) > 0x2000BULL) goto loc_009EDE5F;
    if ((*(uint64_t *)(Arg1 + 0x8)) == 0x2000BULL) goto loc_009EDDB4;
    result = (*(uint64_t *)(Arg1 + 0x8)) - (6);
    if (condition_is_equal) goto loc_009EDD25;
    result = (result) - (0xFFFDULL);
    if (condition_is_equal) goto loc_009EDC9B;
    result = (result) - (1);
    if (condition_is_equal) goto loc_009EDC0C;
    result = (result) - (0x10001ULL);
    if (condition_is_equal) goto loc_009EDB54;
    result = (result) - (2);
    if (condition_is_equal) goto loc_009EDA93;
    result = (result) - (1);
    if (condition_is_equal) goto loc_009EDA54;
    result = (result) - (1);
    if (condition_is_equal) goto loc_009EDA09;
    if (result != 1) goto loc_009EED70;
    if ((*(uint64_t *)((uint32_t)(0xC000000DULL) + 0x8)) != 8) goto loc_009ED8AD;
    v_stack_m1B0 = *(uint64_t *)((uint32_t)(0xC000000DULL) + 0x10);
    if (Arg2 == 0) goto loc_009ED99E;
    if ((((uint8_t)(result + 3)) & ((uint8_t)(*(uint64_t *)((uint32_t)(0xC000000DULL) + 0x10)))) != 0) goto loc_009EEFA3;
    result = *(uint64_t *)((uint32_t)(0xC000000DULL) + 0x10);
    if ((*(uint64_t *)((uint32_t)(0xC000000DULL) + 0x10)) >= local_r13) { result = local_r13; }
loc_009ED99E:
    v_stack_m208 = 0;
    v_stack_m208 = *(uint64_t *)(v_stack_m1B0);
    if ((((uint8_t)(*(uint64_t *)(v_stack_m1B0))) & (28)) == 0) goto loc_009ED9BF;
    goto loc_009EEEF0;
loc_009ED9BF:
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m1B0)))) & ((uint32_t)(result + 3)));
    v_stack_m284 = Arg3;
    if (((uint8_t)(Arg3)) >= ((uint8_t)(result + 3))) goto loc_009ED8AD;
    Arg2 = (uint8_t)(((uint8_t)(Arg3)) & ((uint8_t)(result + 3)));
    Arg2 = (uint8_t)((Arg2) << (2));
    Arg1 = (uint8_t)((*(uint8_t *)(arg4 + 0x11)) & (243));
    Arg2 = (uint8_t)((Arg2) | ((uint8_t)(Arg1)));
    *(uint8_t *)(arg4 + 0x11) = Arg2;
    if (Arg3 != 1) goto loc_009EEC57;
    result = (*(uint64_t *)(v_stack_m1B0)) >> (32);
    *(uint32_t *)(arg4 + 0x120) = (uint32_t)(result);
    goto loc_009EEC57;
loc_009EDA09:
    if ((*(uint64_t *)(v_stack_m2B0 + 0x8)) != 4) goto loc_009ED8AD;
    v_stack_m1A8 = *(uint64_t *)(v_stack_m2B0 + 0x10);
    if (Arg2 == 0) goto loc_009EDA45;
    if ((((uint8_t)(result + 3)) & ((uint8_t)(*(uint64_t *)(v_stack_m2B0 + 0x10)))) != 0) goto loc_009EEFA8;
    result = *(uint64_t *)(v_stack_m2B0 + 0x10);
    if ((*(uint64_t *)(v_stack_m2B0 + 0x10)) >= local_r13) { result = local_r13; }
loc_009EDA45:
    *(uint32_t *)(arg4 + 0x13C) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m1A8)));
    goto loc_009EEC57;
loc_009EDA54:
    if ((*(uint64_t *)(v_stack_m2B0 + 0x8)) != 1) goto loc_009ED8AD;
    v_stack_m1A0 = *(uint64_t *)(v_stack_m2B0 + 0x10);
    result = *(uint64_t *)(v_stack_m2B0 + 0x10);
    local_rdi = v_stack_m2B0;
    if (Arg2 != 0) {
        result = *(uint64_t *)(v_stack_m2B0 + 0x10);
        if ((*(uint64_t *)(v_stack_m2B0 + 0x10)) >= local_r13) { result = local_r13; }
        result = *(uint8_t *)(result);
        local_rdi = v_stack_m2B0;
        result = v_stack_m1A0;
    }
    *(uint8_t *)(arg4 + 0x2) = (uint8_t)(*(uint8_t *)(result));
    goto loc_009EEC57;
loc_009EDA93:
    v_stack_m2A8 = *(uint64_t *)(local_rdi + 0x8);
    if (*(uint64_t *)(local_rdi + 0x8) == 0) goto loc_009ED8AD;
    if ((((uint8_t)(*(uint64_t *)(local_rdi + 0x8))) & (15)) != 0) goto loc_009ED8AD;
    v_stack_m198 = *(uint64_t *)(local_rdi + 0x10);
    if (Arg2 == 0) goto loc_009EDAF1;
    if ((((uint8_t)(*(uint64_t *)(local_rdi + 0x10))) & (3)) != 0) goto loc_009EEFAD;
    if ((*(uint64_t *)(local_rdi + 0x8) + *(uint64_t *)(local_rdi + 0x10) * 1) > local_r13) goto loc_009EDADB;
    result = *(uint64_t *)(local_rdi + 0x8) + *(uint64_t *)(local_rdi + 0x10) * 1;
    local_rbx = *(uint64_t *)(local_rdi + 0x8);
    local_r14 = *(uint64_t *)(local_rdi + 0x10);
    if ((*(uint64_t *)(local_rdi + 0x8) + *(uint64_t *)(local_rdi + 0x10) * 1) < (*(uint64_t *)(local_rdi + 0x10))) {
        result = *(uint8_t *)(local_r13);
        local_rdi = v_stack_m2B0;
        local_r14 = v_stack_m198;
        local_rbx = v_stack_m2A8;
    }
    if (local_rbx > 16) goto loc_009EDB25;
    *(void **)(arg4 + 0x118) = Arg4 + 264;
loc_009EDB06:
    result = memcpy(Arg4 + 264, local_r14, local_rbx, 65);
    local_rbx = (local_rbx) >> (4);
    *(uint64_t *)(arg4 + 0x100) = local_rbx;
    goto loc_009EEC57;
loc_009EDB25:
    result = ExAllocatePool2(65, local_rbx, (uint32_t)(0x6C527350ULL), 65);
    *(uint64_t *)(v_stack_m1C8 + 0x118) = result;
    if (result != 0) goto loc_009EDB06;
loc_009EDB4A:
    goto loc_009EEEF0;
loc_009EDB54:
    v_stack_m2A8 = *(uint64_t *)(local_rdi + 0x8);
    if (*(uint64_t *)(local_rdi + 0x8) == 0) goto loc_009ED8AD;
    if ((((uint8_t)(*(uint64_t *)(local_rdi + 0x8))) & (1)) != 0) goto loc_009ED8AD;
    if ((*(uint64_t *)(local_rdi + 0x8)) > 0xFFFFULL) goto loc_009ED8AD;
    v_stack_m110 = *(uint64_t *)(local_rdi + 0x10);
    if (Arg2 == 0) goto loc_009EDBB1;
    if ((*(uint64_t *)(local_rdi + 0x8) + *(uint64_t *)(local_rdi + 0x10) * 1) > local_r13) goto loc_009EDB9B;
    result = *(uint64_t *)(local_rdi + 0x8) + *(uint64_t *)(local_rdi + 0x10) * 1;
    local_rbx = *(uint64_t *)(local_rdi + 0x8);
    local_r14 = *(uint64_t *)(local_rdi + 0x10);
    if ((*(uint64_t *)(local_rdi + 0x8) + *(uint64_t *)(local_rdi + 0x10) * 1) < (*(uint64_t *)(local_rdi + 0x10))) {
        result = *(uint8_t *)(local_r13);
        local_rdi = v_stack_m2B0;
        local_r14 = v_stack_m110;
        local_rbx = v_stack_m2A8;
    }
    result = ExAllocatePool2(65, local_rbx, (uint32_t)(0x6E467350ULL), 65);
    v_stack_mA8 = result;
    if (result == 0) goto loc_009EDB4A;
    *(uint64_t *)(arg4 + 0xF0) = v_xmm0;
    *(uint16_t *)(arg4 + 0xF2) = (uint16_t)(local_rbx);
    *(uint64_t *)(arg4 + 0xF8) = result;
    result = memcpy(result, local_r14, local_rbx, 65);
    *(uint16_t *)(arg4 + 0xF0) = (uint16_t)(local_rbx);
    goto loc_009EEC57;
loc_009EDC0C:
    if ((*(uint64_t *)(local_rdi + 0x8)) != 8) goto loc_009ED8AD;
    v_stack_m128 = *(uint64_t *)(local_rdi + 0x10);
    if (Arg2 == 0) goto loc_009EDC4F;
    if ((((uint8_t)(local_r14)) & ((uint8_t)(*(uint64_t *)(local_rdi + 0x10)))) != 0) goto loc_009EEFB2;
    Arg1 = *(uint64_t *)(local_rdi + 0x10);
    if ((*(uint64_t *)(local_rdi + 0x10)) >= local_r13) { Arg1 = local_r13; }
    *(uint8_t *)(Arg1) = (uint8_t)(*(uint8_t *)(Arg1));
    *(uint8_t *)(Arg1 + 0x7) = (uint8_t)(*(uint8_t *)(Arg1 + 0x7));
loc_009EDC4F:
    *(uint64_t *)(arg4 + 0x20) = v_stack_m128;
    v_stack_m290 = *(uint64_t *)(v_stack_m2B0 + 0x18);
    if (*(uint64_t *)(v_stack_m2B0 + 0x18) == 0) goto loc_009EEC57;
    if (Arg2 == 0) goto loc_009EDC8F;
    if ((((uint8_t)(local_r14)) & ((uint8_t)(*(uint64_t *)(v_stack_m2B0 + 0x18)))) != 0) goto loc_009EEFB7;
    Arg1 = *(uint64_t *)(v_stack_m2B0 + 0x18);
    if ((*(uint64_t *)(v_stack_m2B0 + 0x18)) >= local_r13) { Arg1 = local_r13; }
    *(uint8_t *)(Arg1) = (uint8_t)(*(uint8_t *)(Arg1));
    *(uint8_t *)(Arg1 + 0x7) = (uint8_t)(*(uint8_t *)(Arg1 + 0x7));
loc_009EDC8F:
    *(uint64_t *)(v_stack_m290) = 8;
    goto loc_009EEC57;
loc_009EDC9B:
    if ((*(uint64_t *)(v_stack_m2B0 + 0x8)) != local_rbx) goto loc_009ED8AD;
    v_stack_m118 = *(uint64_t *)(v_stack_m2B0 + 0x10);
    if (Arg2 == 0) goto loc_009EDCDD;
    if ((((uint8_t)(local_r14)) & ((uint8_t)(*(uint64_t *)(v_stack_m2B0 + 0x10)))) != 0) goto loc_009EEFBC;
    Arg1 = *(uint64_t *)(v_stack_m2B0 + 0x10);
    if ((*(uint64_t *)(v_stack_m2B0 + 0x10)) >= local_r13) { Arg1 = local_r13; }
    *(uint8_t *)(Arg1) = (uint8_t)(*(uint8_t *)(Arg1));
    *(uint8_t *)(Arg1 + 0xF) = (uint8_t)(*(uint8_t *)(Arg1 + 0xF));
loc_009EDCDD:
    *(uint64_t *)(arg4 + 0x18) = v_stack_m118;
    v_stack_m290 = *(uint64_t *)(v_stack_m2B0 + 0x18);
    if (*(uint64_t *)(v_stack_m2B0 + 0x18) == 0) goto loc_009EEC57;
    if (Arg2 == 0) goto loc_009EDD1D;
    if ((((uint8_t)(local_r14)) & ((uint8_t)(*(uint64_t *)(v_stack_m2B0 + 0x18)))) != 0) goto loc_009EEFC1;
    Arg1 = *(uint64_t *)(v_stack_m2B0 + 0x18);
    if ((*(uint64_t *)(v_stack_m2B0 + 0x18)) >= local_r13) { Arg1 = local_r13; }
    *(uint8_t *)(Arg1) = (uint8_t)(*(uint8_t *)(Arg1));
    *(uint8_t *)(Arg1 + 0x7) = (uint8_t)(*(uint8_t *)(Arg1 + 0x7));
loc_009EDD1D:
    *(uint64_t *)(v_stack_m290) = local_rbx;
    goto loc_009EEC57;
loc_009EDD25:
    if ((*(uint64_t *)(v_stack_m2B0 + 0x8)) != 64) goto loc_009ED8AD;
    v_stack_m190 = *(uint64_t *)(v_stack_m2B0 + 0x10);
    if (Arg2 == 0) goto loc_009EDD68;
    if ((((uint8_t)(local_r14)) & ((uint8_t)(*(uint64_t *)(v_stack_m2B0 + 0x10)))) != 0) goto loc_009EEFC6;
    Arg1 = *(uint64_t *)(v_stack_m2B0 + 0x10);
    if ((*(uint64_t *)(v_stack_m2B0 + 0x10)) >= local_r13) { Arg1 = local_r13; }
    *(uint8_t *)(Arg1) = (uint8_t)(*(uint8_t *)(Arg1));
    *(uint8_t *)(Arg1 + 0x3F) = (uint8_t)(*(uint8_t *)(Arg1 + 0x3F));
loc_009EDD68:
    *(uint64_t *)(arg4 + 0x28) = v_stack_m190;
    v_stack_m290 = *(uint64_t *)(v_stack_m2B0 + 0x18);
    if (*(uint64_t *)(v_stack_m2B0 + 0x18) == 0) goto loc_009EEC57;
    if (Arg2 == 0) goto loc_009EDDA8;
    if ((((uint8_t)(local_r14)) & ((uint8_t)(*(uint64_t *)(v_stack_m2B0 + 0x18)))) != 0) goto loc_009EEFCB;
    Arg1 = *(uint64_t *)(v_stack_m2B0 + 0x18);
    if ((*(uint64_t *)(v_stack_m2B0 + 0x18)) >= local_r13) { Arg1 = local_r13; }
    *(uint8_t *)(Arg1) = (uint8_t)(*(uint8_t *)(Arg1));
    *(uint8_t *)(Arg1 + 0x7) = (uint8_t)(*(uint8_t *)(Arg1 + 0x7));
loc_009EDDA8:
    *(uint64_t *)(v_stack_m290) = 64;
    goto loc_009EEC57;
loc_009EDDB4:
    v_stack_m2A8 = *(uint64_t *)(v_stack_m2B0 + 0x8);
    if (*(uint64_t *)(v_stack_m2B0 + 0x8) == 0) goto loc_009ED8AD;
    if ((((uint8_t)(*(uint64_t *)(v_stack_m2B0 + 0x8))) & (7)) != 0) goto loc_009ED8AD;
    result = (*(uint64_t *)(v_stack_m2B0 + 0x8)) & (-8);
    if (result > local_rsp) goto loc_009ED8AD;
    v_stack_m270 = *(uint64_t *)(v_stack_m2B0 + 0x10);
    if (Arg2 == 0) goto loc_009EDE1E;
    if ((((uint8_t)(*(uint64_t *)(v_stack_m2B0 + 0x10))) & (3)) != 0) goto loc_009EEFD0;
    if ((*(uint64_t *)(v_stack_m2B0 + 0x10) + *(uint64_t *)(v_stack_m2B0 + 0x8) * 1) > local_r13) goto loc_009EDE08;
    result = *(uint64_t *)(v_stack_m2B0 + 0x10) + *(uint64_t *)(v_stack_m2B0 + 0x8) * 1;
    local_rbx = *(uint64_t *)(v_stack_m2B0 + 0x8);
    local_rdi = v_stack_m2B0;
    local_r14 = *(uint64_t *)(v_stack_m2B0 + 0x10);
    if ((*(uint64_t *)(v_stack_m2B0 + 0x10) + *(uint64_t *)(v_stack_m2B0 + 0x8) * 1) < (*(uint64_t *)(v_stack_m2B0 + 0x10))) {
        result = *(uint8_t *)(local_r13);
        local_rdi = v_stack_m2B0;
        local_r14 = v_stack_m270;
        local_rbx = v_stack_m2A8;
    }
    result = ExAllocatePool2(65, local_rbx, (uint32_t)(0x6C487350ULL), 65);
    *(uint64_t *)(arg4 + 0x128) = result;
    if (result == 0) goto loc_009EDB4A;
    result = memcpy(result, local_r14, local_rbx, 65);
    local_rbx = (local_rbx) >> (3);
    *(uint32_t *)(arg4 + 0x124) = (uint32_t)(local_rbx);
    goto loc_009EEC57;
loc_009EDE5F:
    result = (result) - (0x2000DULL);
    if (condition_is_equal) goto loc_009EE260;
    result = (result) - (local_r14);
    if (condition_is_equal) goto loc_009EE1B8;
    result = (result) - (2);
    if (condition_is_equal) goto loc_009EE0FC;
    result = (result) - (1);
    if (condition_is_equal) goto loc_009EDFD9;
    result = (result) - (1);
    if (condition_is_equal) goto loc_009EDF8E;
    result = (result) - (1);
    if (condition_is_equal) goto loc_009EDF43;
    if (result != 1) goto loc_009EED70;
    if ((*(uint64_t *)(local_rdi + 0x8)) != 8) goto loc_009ED8AD;
    v_stack_m188 = *(uint64_t *)(local_rdi + 0x10);
    if (Arg2 == 0) goto loc_009EDEEA;
    if ((((uint8_t)(local_r14)) & ((uint8_t)(*(uint64_t *)(local_rdi + 0x10)))) != 0) goto loc_009EEFD5;
    if ((*(uint64_t *)(local_rdi + 0x10) + 8) > local_r13) goto loc_009EDED9;
    result = *(uint64_t *)(local_rdi + 0x10) + 8;
    local_rbx = *(uint64_t *)(local_rdi + 0x10);
    if ((*(uint64_t *)(local_rdi + 0x10) + 8) < (*(uint64_t *)(local_rdi + 0x10))) {
        result = *(uint8_t *)(local_r13);
        local_rdi = v_stack_m2B0;
        local_rbx = v_stack_m188;
    }
    result = ExAllocatePool2(65, 8, (uint32_t)(0x77736350ULL), 65);
    *(uint64_t *)(arg4 + 0x1B0) = result;
    if (result != 0) goto loc_009EDF17;
loc_009EDF0D:
    goto loc_009EEEF0;
loc_009EDF17:
    *(uint64_t *)(result) = *(uint64_t *)((uint32_t)(0xC0000017ULL));
    if ((((uint8_t)(local_r14)) & ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg4 + 0x1B0)))))) == 0) goto loc_009ED8AD;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg4 + 0x1B0) + 0x4))) - 1);
    if (((uint32_t)(result)) <= 5) goto loc_009EEC57;
    goto loc_009ED8AD;
loc_009EDF43:
    if ((*(uint64_t *)(local_rdi + 0x8)) != 4) goto loc_009ED8AD;
    v_stack_m180 = *(uint64_t *)(local_rdi + 0x10);
    if (Arg2 == 0) goto loc_009EDF7F;
    if ((((uint8_t)(local_r14)) & ((uint8_t)(*(uint64_t *)(local_rdi + 0x10)))) != 0) goto loc_009EEFDA;
    result = *(uint64_t *)(local_rdi + 0x10);
    if ((*(uint64_t *)(local_rdi + 0x10)) >= local_r13) { result = local_r13; }
loc_009EDF7F:
    *(uint32_t *)(arg4 + 0x184) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m180)));
    goto loc_009EEC57;
loc_009EDF8E:
    if ((*(uint64_t *)(v_stack_m2B0 + 0x8)) != 4) goto loc_009ED8AD;
    v_stack_m178 = *(uint64_t *)(v_stack_m2B0 + 0x10);
    if (Arg2 == 0) goto loc_009EDFCA;
    if ((((uint8_t)(local_r14)) & ((uint8_t)(*(uint64_t *)(v_stack_m2B0 + 0x10)))) != 0) goto loc_009EEFDF;
    result = *(uint64_t *)(v_stack_m2B0 + 0x10);
    if ((*(uint64_t *)(v_stack_m2B0 + 0x10)) >= local_r13) { result = local_r13; }
loc_009EDFCA:
    *(uint32_t *)(arg4 + 0x180) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m178)));
    goto loc_009EEC57;
loc_009EDFD9:
    v_stack_m2A8 = *(uint64_t *)(v_stack_m2B0 + 0x8);
    if (*(uint64_t *)(v_stack_m2B0 + 0x8) == 0) goto loc_009ED8AD;
    if ((((uint8_t)(*(uint64_t *)(v_stack_m2B0 + 0x8))) & (7)) != 0) goto loc_009ED8AD;
    result = (*(uint64_t *)(v_stack_m2B0 + 0x8)) & (-8);
    if (result > local_rsp) goto loc_009ED8AD;
    v_stack_m270 = *(uint64_t *)(v_stack_m2B0 + 0x10);
    if (v_stack_p10 == 0) goto loc_009EE047;
    if ((((uint8_t)(local_r14)) & ((uint8_t)(*(uint64_t *)(v_stack_m2B0 + 0x10)))) != 0) goto loc_009EEFE4;
    if ((*(uint64_t *)(v_stack_m2B0 + 0x8) + *(uint64_t *)(v_stack_m2B0 + 0x10) * 1) > local_r13) goto loc_009EE031;
    result = *(uint64_t *)(v_stack_m2B0 + 0x8) + *(uint64_t *)(v_stack_m2B0 + 0x10) * 1;
    local_rbx = *(uint64_t *)(v_stack_m2B0 + 0x8);
    local_rdi = v_stack_m2B0;
    local_r15 = *(uint64_t *)(v_stack_m2B0 + 0x10);
    if ((*(uint64_t *)(v_stack_m2B0 + 0x8) + *(uint64_t *)(v_stack_m2B0 + 0x10) * 1) < (*(uint64_t *)(v_stack_m2B0 + 0x10))) {
        result = *(uint8_t *)(local_r13);
        local_rdi = v_stack_m2B0;
        local_r15 = v_stack_m270;
        local_rbx = v_stack_m2A8;
    }
    result = ExAllocatePool2(65, local_rbx, (uint32_t)(0x6C4A7350ULL), 65);
    *(uint64_t *)(arg4 + 0x170) = result;
    if (result == 0) goto loc_009EDB4A;
    local_rbx = (local_rbx) >> (3);
    *(uint32_t *)(arg4 + 0x17C) = (uint32_t)(local_rbx);
    v_stack_m170 = 0;
loc_009EE080:
    if (0 >= ((uint32_t)(*(uint32_t *)(arg4 + 0x17C)))) goto loc_009EEC4F;
    v_stack_m2D0 = 0;
    v_stack_m2D8 = 0;
    v_stack_m2E0 = v_stack_m200;
    v_stack_m2E8 = 0x6C4A7350ULL;
    result = ObpReferenceObjectByHandleWithTag(*(uint64_t *)(local_r15 + 0x0 * 8), 1, *(uint64_t *)(v_rip + 0x5D8BC0), v_stack_p10);
    v_stack_m2B8 = (uint32_t)(result);
    if (sign_flag) goto loc_009EEC92;
    *(uint64_t *)(*(uint64_t *)(arg4 + 0x170) + 0x0 * 8) = v_stack_m200;
    local_r14 = (0) + 1;
    v_stack_m170 = local_r14;
    goto loc_009EE080;
loc_009EE0FC:
    v_stack_m2A8 = *(uint64_t *)(local_rdi + 0x8);
    if (*(uint64_t *)(local_rdi + 0x8) == 0) goto loc_009ED8AD;
    if ((((uint8_t)(*(uint64_t *)(local_rdi + 0x8))) & (7)) != 0) goto loc_009ED8AD;
    if ((*(uint64_t *)(local_rdi + 0x8)) > 136) goto loc_009ED8AD;
    v_stack_m168 = *(uint64_t *)(local_rdi + 0x10);
    if ((uint8_t)(local_r15) == 0) goto loc_009EE163;
    if ((((uint8_t)(*(uint64_t *)(local_rdi + 0x10))) & (3)) != 0) goto loc_009EEFE9;
    if ((*(uint64_t *)(local_rdi + 0x10) + *(uint64_t *)(local_rdi + 0x8) * 1) > local_r13) goto loc_009EE14D;
    result = *(uint64_t *)(local_rdi + 0x10) + *(uint64_t *)(local_rdi + 0x8) * 1;
    local_rbx = *(uint64_t *)(local_rdi + 0x8);
    local_r14 = *(uint64_t *)(local_rdi + 0x10);
    if ((*(uint64_t *)(local_rdi + 0x10) + *(uint64_t *)(local_rdi + 0x8) * 1) < (*(uint64_t *)(local_rdi + 0x10))) {
        result = *(uint8_t *)(local_r13);
        local_rdi = v_stack_m2B0;
        local_rbx = v_stack_m2A8;
        local_r14 = v_stack_m168;
    }
    result = ExAllocatePool2(v_stack_p10, local_rbx, (uint32_t)(0x61547350ULL), v_stack_p10);
    *(uint64_t *)(arg4 + 0x168) = result;
    if (result == 0) goto loc_009EDB4A;
    result = memcpy(result, local_r14, local_rbx, v_stack_p10);
    *(uint32_t *)(arg4 + 0x178) = (uint32_t)(local_rbx);
    result = IsTrustletCreateAttributeWellFormed(*(uint64_t *)(arg4 + 0x168), local_rbx, local_rbx, v_stack_p10);
loc_009EE1AB:
loc_009EE1AD:
    if ((uint8_t)(result) != 0) goto loc_009EEC57;
    goto loc_009ED8AD;
loc_009EE1B8:
    v_stack_m2A8 = *(uint64_t *)(local_rdi + 0x8);
    if ((*(uint64_t *)(local_rdi + 0x8)) > 24) goto loc_009ED8AD;
    result = 0;
    v_stack_m78 = v_xmm0;
    v_stack_m68 = 0;
    if ((uint8_t)(local_r15) == 0) goto loc_009EE204;
    Arg2 = *(uint64_t *)(v_stack_m2B0 + 0x10);
    if ((*(uint64_t *)(v_stack_m2B0 + 0x10)) >= local_r13) { Arg2 = local_r13; }
    result = RtlCopyVolatileMemory(v_stack_m78, Arg2, *(uint64_t *)(local_rdi + 0x8), v_stack_p10);
    goto loc_009EE209;
loc_009EE204:
    result = memcpy(v_stack_m78, Arg2, *(uint64_t *)(local_rdi + 0x8), v_stack_p10);
loc_009EE209:
    v_stack_mE8 = v_xmm2;
    v_stack_mD8 = v_xmm3;
    Arg2 = 0;
    result = PspValidateMitigationOptions(v_stack_mE8, Arg2, *(uint64_t *)(local_rdi + 0x8), v_stack_p10);
    v_stack_m2B8 = (uint32_t)(result);
    if (sign_flag) goto loc_009EEC92;
    *(uint64_t *)(arg4 + 0x150) = v_xmm2;
    *(uint64_t *)(arg4 + 0x160) = v_xmm3;
    goto loc_009EEC57;
loc_009EE260:
    if ((*(uint64_t *)(v_stack_m2B0 + 0x8)) != 2) goto loc_009ED8AD;
    v_stack_m160 = *(uint64_t *)(v_stack_m2B0 + 0x10);
    if ((uint8_t)(local_r15) == 0) goto loc_009EE29B;
    if ((((uint8_t)(*(uint64_t *)(v_stack_m2B0 + 0x10))) & (1)) != 0) goto loc_009EEFEE;
    result = *(uint64_t *)(v_stack_m2B0 + 0x10);
    if ((*(uint64_t *)(v_stack_m2B0 + 0x10)) >= local_r13) { result = local_r13; }
loc_009EE29B:
    v_stack_m288 = (uint16_t)(*(uint16_t *)(v_stack_m160));
    if (((uint16_t)(*(uint16_t *)(v_stack_m160))) >= (*(uint16_t *)(v_rip + 0x5D6D53))) goto loc_009ED8AD;
    Arg1 = (*(uint64_t *)(v_rip + 0x5E1406 + *(uint16_t *)(v_stack_m160) * 8)) + (16);
    result = KeIsEmptyGroupMask(Arg1, Arg2, *(uint64_t *)(local_rdi + 0x8), v_stack_p10);
    if ((uint32_t)(result) != 0) goto loc_009ED8AD;
    *(uint16_t *)(arg4 + 0xAA) = (uint16_t)(*(uint16_t *)(v_stack_m160));
    goto loc_009EEC57;
loc_009EE2DD:
    v_stack_m2A8 = *(uint64_t *)(v_stack_m2B0 + 0x8);
    if ((*(uint64_t *)(v_stack_m2B0 + 0x8)) != 524) goto loc_009ED8AD;
    v_stack_m158 = *(uint64_t *)(v_stack_m2B0 + 0x10);
    if ((uint8_t)(local_r15) == 0) goto loc_009EE32C;
    if ((*(uint64_t *)(v_stack_m2B0 + 0x8) + *(uint64_t *)(v_stack_m2B0 + 0x10) * 1) > local_r13) goto loc_009EE316;
    result = *(uint64_t *)(v_stack_m2B0 + 0x8) + *(uint64_t *)(v_stack_m2B0 + 0x10) * 1;
    local_rbx = *(uint64_t *)(v_stack_m2B0 + 0x8);
    local_rdi = v_stack_m2B0;
    local_r14 = *(uint64_t *)(v_stack_m2B0 + 0x10);
    if ((*(uint64_t *)(v_stack_m2B0 + 0x10) + *(uint64_t *)(v_stack_m2B0 + 0x8) * 1) < (*(uint64_t *)(v_stack_m2B0 + 0x10))) {
        result = *(uint8_t *)(local_r13);
        local_rdi = v_stack_m2B0;
        local_rbx = v_stack_m2A8;
        local_r14 = v_stack_m158;
    }
    result = ExAllocatePool2(v_stack_p10, local_rbx, (uint32_t)(0x634F7350ULL), v_stack_p10);
    *(uint64_t *)(arg4 + 0x190) = result;
    if (result == 0) goto loc_009EDB4A;
    result = memcpy(result, local_r14, local_rbx, v_stack_p10);
    *(uint32_t *)(arg4 + 0x18C) = (uint32_t)(local_rbx);
loc_009EE371:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg4 + 0x190))))) & (64)) == 0) goto loc_009EEC57;
    goto loc_009ED8AD;
loc_009EE37C:
    if ((*(uint64_t *)(arg4 + 0x190)) > 0x3001EULL) goto loc_009EED2D;
    if ((*(uint64_t *)(arg4 + 0x190)) == 0x3001EULL) goto loc_009EEC9C;
    result = (*(uint64_t *)(arg4 + 0x190)) - (0x20018ULL);
    if (condition_is_equal) goto loc_009EE994;
    result = (result) - (1);
    if (condition_is_equal) goto loc_009EE949;
    result = (result) - (2);
    if (condition_is_equal) goto loc_009EE8A3;
    result = (result) - (2);
    if (condition_is_equal) goto loc_009EE840;
    result = (result) - (6);
    if (condition_is_equal) goto loc_009EE5EB;
    result = (result) - (1);
    if (condition_is_equal) goto loc_009EE49E;
    result = (result) - (0xFFE8ULL);
    if (condition_is_equal) goto loc_009EE43F;
    if (result != 2) goto loc_009EED70;
    if ((uint32_t)(local_rbx) == 0) goto loc_009ED8AD;
    if ((*(uint64_t *)(local_rdi + 0x8)) != 4) goto loc_009ED8AD;
    v_stack_m150 = *(uint64_t *)(local_rdi + 0x10);
    if ((uint8_t)(local_r15) == 0) goto loc_009EE422;
    if ((((uint8_t)(*(uint64_t *)(local_rdi + 0x10))) & (1)) != 0) goto loc_009EEFF3;
    result = *(uint64_t *)(local_rdi + 0x10);
    if ((*(uint64_t *)(local_rdi + 0x10)) >= local_r13) { result = local_r13; }
loc_009EE422:
    v_stack_m298 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m150)));
    result = KeGetProcessorIndexFromNumber(v_stack_m298, local_r14, local_rbx, v_stack_p10);
    *(uint32_t *)(arg4 + 0x14) = (uint32_t)(result);
    goto loc_009EE1AD;
loc_009EE43F:
    if ((uint32_t)(local_rbx) == 0) goto loc_009ED8AD;
    if ((*(uint64_t *)(v_stack_m2B0 + 0x8)) != local_rbx) goto loc_009ED8AD;
    v_stack_m148 = *(uint64_t *)(v_stack_m2B0 + 0x10);
    if ((uint8_t)(local_r15) == 0) goto loc_009EE483;
    if ((((uint8_t)(local_r14)) & ((uint8_t)(*(uint64_t *)(v_stack_m2B0 + 0x10)))) != 0) goto loc_009EEFF8;
    result = *(uint64_t *)(v_stack_m2B0 + 0x10);
    if ((*(uint64_t *)(v_stack_m2B0 + 0x10)) >= local_r13) { result = local_r13; }
loc_009EE483:
    *(uint64_t *)(arg4 + 0x140) = v_xmm0;
    result = KeVerifyGroupAffinity(Arg4 + 320, 1, local_rbx, v_stack_p10);
    goto loc_009EE1AB;
loc_009EE49E:
    result = Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline(Arg4 + 320, 1, local_rbx, v_stack_p10);
    if ((uint32_t)(result) == 0) goto loc_009ED8AD;
    if ((*(uint64_t *)(v_stack_m2B0 + 0x8)) != local_rbx) goto loc_009ED8AD;
    v_stack_mA0 = *(uint64_t *)(v_stack_m2B0 + 0x10);
    if ((uint8_t)(local_r15) == 0) goto loc_009EE4E6;
    if ((((uint8_t)(local_r14)) & ((uint8_t)(*(uint64_t *)(v_stack_m2B0 + 0x10)))) != 0) goto loc_009EEFFD;
    if ((uint8_t)(local_r15) == 0) goto loc_009EE4E6;
    result = RtlCopyFromUser(v_stack_m248, *(uint64_t *)(v_stack_m2B0 + 0x10), local_rbx, v_stack_p10);
    goto loc_009EE4F6;
loc_009EE4E6:
    result = RtlCopyVolatileMemory(v_stack_m248, *(uint64_t *)(v_stack_m2B0 + 0x10), local_rbx, v_stack_p10);
loc_009EE4F6:
    if (v_stack_m248 != 1) goto loc_009ED8AD;
    if (v_stack_m240 == 0) goto loc_009ED8AD;
    if ((uint8_t)(local_r15) == 0) goto loc_009EE53D;
    if ((((uint8_t)(local_r14)) & ((uint8_t)(v_stack_m240))) != 0) goto loc_009EF002;
    if ((uint8_t)(local_r15) == 0) goto loc_009EE53D;
    result = RtlCopyFromUser(v_stack_m98, v_stack_m240, 28, v_stack_p10);
    goto loc_009EE550;
loc_009EE53D:
    result = RtlCopyVolatileMemory(v_stack_m98, v_stack_m240, 28, v_stack_p10);
loc_009EE550:
    if (v_stack_m98 != 28) goto loc_009ED8AD;
    if (((v_stack_m94) & (0xFFFFFFFEULL)) != 0) goto loc_009ED8AD;
    if (((v_stack_m90) & (0xFFFFFFFEULL)) != 0) goto loc_009ED8AD;
    if (((v_stack_m8C) & (0xFFFFFFE0ULL)) != 0) goto loc_009ED8AD;
    if (((v_stack_m88) & (0xFFFFFFF8ULL)) != 0) goto loc_009ED8AD;
    if (((v_stack_m84) & (0xFFFFFFFCULL)) != 0) goto loc_009ED8AD;
    *(uint64_t *)(arg4 + 0x210) = v_xmm0;
    *(uint64_t *)(arg4 + 0x220) = v_xmm0;
    *(uint32_t *)(arg4 + 0x228) = (uint32_t)((uint32_t)(v_stack_m80));
    goto loc_009EEC57;
loc_009EE5EB:
    result = Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline(v_stack_m98, v_stack_m240, 28, v_stack_p10);
    if ((uint32_t)(result) == 0) goto loc_009ED8AD;
    if ((*(uint64_t *)(v_stack_m2B0 + 0x8)) < 32) goto loc_009ED8AD;
    v_stack_m100 = *(uint64_t *)(v_stack_m2B0 + 0x10);
    if ((uint8_t)(local_r15) == 0) goto loc_009EE637;
    if ((((uint8_t)(local_r14)) & ((uint8_t)(*(uint64_t *)(v_stack_m2B0 + 0x10)))) != 0) goto loc_009EF007;
    if ((uint8_t)(local_r15) == 0) goto loc_009EE637;
    result = RtlCopyFromUser(v_stack_m268, *(uint64_t *)(v_stack_m2B0 + 0x10), 32, v_stack_p10);
    goto loc_009EE64A;
loc_009EE637:
    result = RtlCopyVolatileMemory(v_stack_m268, *(uint64_t *)(v_stack_m2B0 + 0x10), 32, v_stack_p10);
loc_009EE64A:
    if (v_stack_m268 < 1) goto loc_009ED8AD;
    if ((uint8_t)(local_r15) == 0) goto loc_009EE68D;
    if (((v_stack_m260) & ((uint8_t)(local_r14))) != 0) goto loc_009EF00C;
    if ((uint8_t)(local_r15) == 0) goto loc_009EE68D;
    result = RtlCopyFromUser(v_stack_m238, v_stack_m260, 48, v_stack_p10);
    goto loc_009EE6A8;
loc_009EE68D:
    result = RtlCopyVolatileMemory(v_stack_m238, v_stack_m260, 48, v_stack_p10);
loc_009EE6A8:
    if (v_stack_m238 > 48) goto loc_009ED8AD;
    if (v_stack_m228 == 0) goto loc_009ED8AD;
    if (v_stack_m218 != 0) goto loc_009EE6E0;
    if (v_stack_m220 != 0) goto loc_009EE6EA;
    if (v_stack_m218 == 0) goto loc_009EE6F4;
loc_009EE6E0:
    if (v_stack_m220 != 0) goto loc_009EE6F4;
loc_009EE6EA:
    goto loc_009EEEF0;
loc_009EE6F4:
    result = ExAllocatePool2(256, 48, (uint32_t)(0x63437350ULL), v_stack_p10);
    *(uint64_t *)(arg4 + 0x1F8) = result;
    if (result == 0) goto loc_009EDF0D;
    *(uint32_t *)(arg4 + 0x1F0) = (uint32_t)((uint32_t)(v_stack_m268));
    *(uint32_t *)(result) = (uint32_t)(v_stack_m238);
    *(uint32_t *)(*(uint64_t *)(arg4 + 0x1F8) + 0x4) = (uint32_t)((uint32_t)(v_stack_m234));
    *(uint64_t *)(*(uint64_t *)(arg4 + 0x1F8) + 0x8) = v_stack_m230;
    *(uint32_t *)(*(uint64_t *)(arg4 + 0x1F8) + 0x28) = (uint32_t)((uint32_t)(v_stack_m210));
    result = (*(uint64_t *)(arg4 + 0x1F8)) + ((uint32_t)(0xC0000030ULL));
    v_stack_m2D8 = result;
    v_stack_m2E0 = 1;
    result = SeCaptureSid(v_stack_m228, (uint8_t)(local_r15), (uint32_t)(0x63437350ULL), v_stack_p10);
    v_stack_m2B8 = (uint32_t)(result);
    if (sign_flag) goto loc_009EEC92;
    if (v_stack_m220 == 0) goto loc_009EE802;
    result = (*(uint64_t *)(arg4 + 0x1F8)) + (24);
    v_stack_m2C8 = v_stack_m280;
    v_stack_m2D0 = result;
    v_stack_m2E8 = 0;
    Arg4 = 0;
    result = SeCaptureSidAndAttributesArray(v_stack_m220, (uint32_t)(v_stack_m218), (uint8_t)(local_r15), Arg4);
    v_stack_m2B8 = (uint32_t)(result);
    if (sign_flag) goto loc_009EEC92;
    *(uint32_t *)(*(uint64_t *)(arg4 + 0x1F8) + 0x20) = (uint32_t)((uint32_t)(v_stack_m218));
loc_009EE802:
    result = SeCaptureHandles((uint32_t)(v_stack_m250), v_stack_m258, Arg4 + 512, Arg4);
    v_stack_m2B8 = (uint32_t)(result);
    if (sign_flag) goto loc_009EEC92;
    *(uint32_t *)(arg4 + 0x208) = (uint32_t)((uint32_t)(v_stack_m250));
    goto loc_009EEC57;
loc_009EE840:
    if ((*(uint64_t *)(v_stack_m2B0 + 0x8)) != 4) goto loc_009ED8AD;
    v_stack_m140 = *(uint64_t *)(v_stack_m2B0 + 0x10);
    if ((uint8_t)(local_r15) == 0) goto loc_009EE884;
    if ((((uint8_t)(local_r14)) & ((uint8_t)(*(uint64_t *)(v_stack_m2B0 + 0x10)))) != 0) goto loc_009EF011;
    if ((*(uint64_t *)(v_stack_m2B0 + 0x10) + 4) > local_r13) goto loc_009EE873;
    result = *(uint64_t *)(v_stack_m2B0 + 0x10) + 4;
    local_rdi = v_stack_m2B0;
    if ((*(uint64_t *)(v_stack_m2B0 + 0x10) + 4) < (*(uint64_t *)(v_stack_m2B0 + 0x10))) {
        result = *(uint8_t *)(local_r13);
        local_rdi = v_stack_m2B0;
        Arg1 = v_stack_m140;
    }
    if (((*(uint32_t *)(Arg1)) & (0xFFFFFFFEULL)) == 0) goto loc_009EE896;
    goto loc_009EEF75;
loc_009EE896:
    *(uint64_t *)(arg4 + 0x1B8) = Arg1;
    goto loc_009EEC57;
loc_009EE8A3:
    v_stack_m2A8 = *(uint64_t *)(local_rdi + 0x8);
    if ((*(uint64_t *)(local_rdi + 0x8)) > 24) goto loc_009ED8AD;
    result = 0;
    v_stack_m60 = v_xmm0;
    v_stack_m50 = 0;
    if ((uint8_t)(local_r15) == 0) goto loc_009EE8EF;
    Arg2 = *(uint64_t *)(v_stack_m2B0 + 0x10);
    if ((*(uint64_t *)(v_stack_m2B0 + 0x10)) >= local_r13) { Arg2 = local_r13; }
    result = RtlCopyVolatileMemory(v_stack_m60, Arg2, *(uint64_t *)(local_rdi + 0x8), Arg4);
    goto loc_009EE8F4;
loc_009EE8EF:
    result = memcpy(v_stack_m60, Arg2, *(uint64_t *)(local_rdi + 0x8), Arg4);
loc_009EE8F4:
    v_stack_mC8 = v_xmm2;
    v_stack_mB8 = v_xmm3;
    result = PspValidateMitigationAuditOptions(v_stack_mC8, Arg2, *(uint64_t *)(local_rdi + 0x8), Arg4);
    v_stack_m2B8 = (uint32_t)(result);
    if (sign_flag) goto loc_009EEC92;
    *(uint64_t *)(arg4 + 0x1C0) = v_xmm2;
    *(uint64_t *)(arg4 + 0x1D0) = v_xmm3;
    goto loc_009EEC57;
loc_009EE949:
    if ((*(uint64_t *)(v_stack_m2B0 + 0x8)) != 4) goto loc_009ED8AD;
    v_stack_m138 = *(uint64_t *)(v_stack_m2B0 + 0x10);
    if ((uint8_t)(local_r15) == 0) goto loc_009EE985;
    if ((((uint8_t)(local_r14)) & ((uint8_t)(*(uint64_t *)(v_stack_m2B0 + 0x10)))) != 0) goto loc_009EF016;
    result = *(uint64_t *)(v_stack_m2B0 + 0x10);
    if ((*(uint64_t *)(v_stack_m2B0 + 0x10)) >= local_r13) { result = local_r13; }
loc_009EE985:
    *(uint32_t *)(arg4 + 0x188) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m138)));
    goto loc_009EEC57;
loc_009EE994:
    v_stack_m2A8 = *(uint64_t *)(v_stack_m2B0 + 0x8);
    if ((*(uint64_t *)(v_stack_m2B0 + 0x8)) != 40) goto loc_009ED8AD;
    v_stack_m130 = *(uint64_t *)(v_stack_m2B0 + 0x10);
    if (v_stack_p10 == 0) goto loc_009EE9E4;
    if ((((uint8_t)(*(uint64_t *)(v_stack_m2B0 + 0x10))) & (3)) != 0) goto loc_009EF01B;
    local_r14 = *(uint64_t *)(v_stack_m2B0 + 0x10);
    if ((*(uint64_t *)(v_stack_m2B0 + 0x10)) >= local_r13) { local_r14 = local_r13; }
loc_009EE9E4:
    result = ExAllocatePool2(0, v_stack_m2A8, (uint32_t)(0x70426E50ULL), Arg4);
    *(uint64_t *)(arg4 + 0x198) = result;
    if (result == 0) goto loc_009EDB4A;
    v_stack_m27C = 0;
    result = memcpy(result, v_stack_m130, v_stack_m2A8, Arg4);
    goto loc_009EEA7F;
loc_009EEA7F:
    if (sign_flag) goto loc_009EEEF0;
    v_stack_m1E0 = *(uint64_t *)(arg4 + 0x198);
    v_stack_m1F0 = *(uint64_t *)(*(uint64_t *)(arg4 + 0x198) + 0x8);
    v_stack_m1E8 = *(uint64_t *)(*(uint64_t *)(arg4 + 0x198) + 0x18);
    *(uint64_t *)(*(uint64_t *)(arg4 + 0x198) + 0x8) = 0;
    *(uint64_t *)(*(uint64_t *)(arg4 + 0x198) + 0x18) = 0;
    if ((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg4 + 0x198) + 0x2)) == 0) goto loc_009EEB3B;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg4 + 0x198)))) > ((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg4 + 0x198) + 0x2)))) goto loc_009ED8AD;
    if ((((uint8_t)(*(uint16_t *)(*(uint64_t *)(arg4 + 0x198)))) & (1)) != 0) goto loc_009ED8AD;
    if ((((uint8_t)(*(uint16_t *)(*(uint64_t *)(arg4 + 0x198) + 0x2))) & (1)) != 0) goto loc_009ED8AD;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg4 + 0x198) + 0x2))) > ((uint16_t)((uint32_t)(0xFFFEULL)))) goto loc_009ED8AD;
    if (*(uint64_t *)(*(uint64_t *)(arg4 + 0x198) + 0x8) == 0) goto loc_009ED8AD;
    if ((uint8_t)(v_stack_p10) == 0) goto loc_009EEB43;
    if ((*(uint16_t *)(*(uint64_t *)(arg4 + 0x198) + 0x2) + *(uint64_t *)(*(uint64_t *)(arg4 + 0x198) + 0x8) * 1) > v_stack_m2A8) goto loc_009EEB19;
    if ((*(uint16_t *)(*(uint64_t *)(arg4 + 0x198) + 0x2) + *(uint64_t *)(*(uint64_t *)(arg4 + 0x198) + 0x8) * 1) >= (*(uint64_t *)(*(uint64_t *)(arg4 + 0x198) + 0x8))) goto loc_009EEB43;
loc_009EEB19:
    goto loc_009EEB43;
loc_009EEB3B:
loc_009EEB43:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg4 + 0x198) + 0x10))) == 0) goto loc_009EEBBA;
    if (v_stack_m1E8 == 0) goto loc_009ED8AD;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg4 + 0x198) + 0x10)))) > 0xFFFFULL) goto loc_009ED8AD;
    if ((uint8_t)(v_stack_p10) == 0) goto loc_009EEBBA;
    if ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg4 + 0x198) + 0x10)) * 8 == 0) goto loc_009EEBBA;
    if ((((uint8_t)(v_stack_m1E8)) & (3)) != 0) goto loc_009EF020;
    Arg2 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg4 + 0x198) + 0x10)) * 8) + (v_stack_m1E8);
    if (Arg2 > v_stack_m2A8) goto loc_009EEB93;
    result = *(uint64_t *)(arg4 + 0x198);
    local_rdi = v_stack_m2B0;
    local_r13 = v_stack_m1F0;
    local_r14 = v_stack_m1E0;
    local_r15 = v_stack_m1E8;
    if (Arg2 < v_stack_m1E8) {
        result = *(uint8_t *)(v_stack_m2A8);
        result = *(uint64_t *)(v_stack_m1F8 + 0x198);
        local_rdi = v_stack_m2B0;
        local_r13 = v_stack_m1F0;
        local_r15 = v_stack_m1E8;
        local_r14 = v_stack_m1E0;
    }
    v_stack_m1D8 = 0;
    if ((uint16_t)(*(uint16_t *)(local_r14 + 0x2)) != 0) goto loc_009EEBD4;
    local_rbx = 0;
    if ((*(uint32_t *)(result + 0x10)) >= = 0) {
        Arg1 = *(uint32_t *)(result + 0x10);
        Arg2 = *(uint16_t *)(local_r14 + 0x2) + Arg1 * 8;
        Arg1 = 65;
        Arg3 = 0x70426E50ULL;
        result = ExAllocatePool2(Arg1, Arg2, Arg3, v_stack_p10);
        local_rbx = result;
        v_stack_m1D8 = result;
    }
    result = *(uint16_t *)(local_r14 + 0x2);
    if ((uint16_t)(*(uint16_t *)(local_r14 + 0x2)) != 0) {
        *(uint64_t *)(local_r14 + 0x8) = local_rbx;
        Arg3 = (uint32_t)(*(uint16_t *)(local_r14 + 0x2));
        Arg2 = local_r13;
        Arg1 = local_rbx;
        result = memcpy(Arg1, Arg2, Arg3, v_stack_p10);
        Arg1 = *(uint16_t *)(local_r14 + 0x2);
        local_rbx = (local_rbx) + (Arg1);
        v_stack_m1D8 = local_rbx;
    }
    result = *(uint64_t *)(arg4 + 0x198);
    if ((*(uint32_t *)(*(uint64_t *)(arg4 + 0x198) + 0x10)) >= = 0) {
        *(uint64_t *)(*(uint64_t *)(arg4 + 0x198) + 0x18) = local_rbx;
        Arg1 = *(uint64_t *)(arg4 + 0x198);
        Arg3 = *(uint32_t *)(Arg1 + 0x10);
        Arg3 = (Arg3) << (3);
        Arg2 = local_r15;
        Arg1 = *(uint64_t *)(Arg1 + 0x18);
        result = memcpy(Arg1, Arg2, Arg3, v_stack_p10);
    }
loc_009EEC57:
    result = Feature_CreateProcessSegmentHeapEnablement__private_IsEnabledDeviceUsageNoInline(Arg1, Arg2, Arg3, v_stack_p10);
    if ((uint32_t)(result) == 0) goto loc_009EEEBB;
    if (((v_stack_m1D0) & (0x80000ULL)) == 0) goto loc_009EEEBB;
    result = PspProcessUserCopyAttribute(local_rdi, (uint8_t)(v_stack_p10), 0, v_stack_p10);
    v_stack_m2B8 = (uint32_t)(result);
    if (!sign_flag) goto loc_009EEEBB;
loc_009EEC92:
    goto loc_009EEEF9;
loc_009EEC9C:
    if (0 == 0) goto loc_009ED8AD;
    if ((*(uint64_t *)((uint32_t)(0xC000000DULL) + 0x8)) != 8) goto loc_009ED8AD;
    v_stack_m120 = *(uint64_t *)((uint32_t)(0xC000000DULL) + 0x10);
    if ((uint8_t)(v_stack_p10) == 0) goto loc_009EECE1;
    if ((((uint8_t)(local_r14)) & ((uint8_t)(*(uint64_t *)((uint32_t)(0xC000000DULL) + 0x10)))) != 0) goto loc_009EF025;
    result = *(uint64_t *)((uint32_t)(0xC000000DULL) + 0x10);
    if ((*(uint64_t *)((uint32_t)(0xC000000DULL) + 0x10)) >= local_r13) { result = local_r13; }
loc_009EECE1:
    *(uint64_t *)(arg4 + 0x1E0) = *(uint64_t *)(v_stack_m120);
    Arg1 = (*(uint64_t *)(local_rdi)) | (*(uint64_t *)(v_stack_m120));
    v_stack_mF8 = Arg1;
    Arg1 = ~(Arg1);
    if (((*(uint64_t *)(v_stack_m120)) & (Arg1)) != 0) goto loc_009ED8AD;
    Arg2 = (uint32_t)((*(uint64_t *)(v_stack_m120)) & (0x40000ULL));
    *(uint64_t *)(arg4 + 0x1E0) = Arg2;
    goto loc_009EEC57;
loc_009EED2D:
    result = (v_stack_m120) - (0x60000ULL);
    if (condition_is_equal) goto loc_009EEE9F;
    result = (result) - (1);
    if (condition_is_equal) goto loc_009EEE83;
    result = (result) - (1);
    if (condition_is_equal) goto loc_009EEE67;
    result = (result) - (15);
    if (condition_is_equal) goto loc_009EEE4A;
    result = (result) - (9);
    if (condition_is_equal) goto loc_009EEE20;
    result = (result) - (2);
    if (condition_is_equal) goto loc_009EEE03;
    if (result == local_r14) goto loc_009EEDDA;
loc_009EED70:
    result = Feature_CreateProcessSegmentHeapEnablement__private_IsEnabledDeviceUsageNoInline(Arg1, Arg2, 0, v_stack_p10);
    if ((uint32_t)(result) == 0) goto loc_009ED8AD;
    result = PspIsAttributeRemoved(v_stack_m1D0, Arg2, v_stack_m1D0, v_stack_p10);
    if (((uint16_t)(v_stack_m1D0)) >= 37) goto loc_009ED8AD;
    if (((uint16_t)(v_stack_m1D0)) >= 37) goto loc_009ED8AD;
    if ((uint32_t)(result) != 0) goto loc_009ED8AD;
    result = PspGetAttributeValueSize(v_stack_m1D0, Arg2, v_stack_m1D0, v_stack_p10);
    result = PspGetFullAttribute((uint16_t)(v_stack_m1D0), result, v_stack_m1D0, v_stack_p10);
    if (result == 0) goto loc_009ED8AD;
    if ((*(uint64_t *)(v_stack_m2B0 + 0x8)) != result) goto loc_009ED8AD;
    goto loc_009EE371;
loc_009EEDDA:
    if ((*(uint64_t *)(v_stack_m2B0 + 0x8)) != 4) goto loc_009ED8AD;
    if (((*(uint64_t *)(v_stack_m2B0 + 0x10)) & (-8)) != 0) goto loc_009ED8AD;
    *(uint32_t *)(arg4 + 0x1E8) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m2B0 + 0x10)));
    goto loc_009EEC57;
loc_009EEE03:
    if ((*(uint64_t *)(v_stack_m2B0 + 0x8)) != 2) goto loc_009ED8AD;
    *(uint16_t *)(arg4 + 0xA8) = (uint16_t)(*(uint16_t *)(v_stack_m2B0 + 0x10));
    goto loc_009EEC57;
loc_009EEE20:
    if ((*(uint64_t *)(v_stack_m2B0 + 0x8)) != 1) goto loc_009ED8AD;
    result = -(*(uint64_t *)(v_stack_m2B0 + 0x10));
    Arg1 = (uint8_t)(((uint16_t)(v_stack_m1D0)) & (128));
    result = (uint8_t)((*(uint8_t *)(arg4 + 0x11)) & (127));
    Arg1 = (uint8_t)((Arg1) | ((uint8_t)(result)));
    *(uint8_t *)(arg4 + 0x11) = (uint8_t)(Arg1);
    goto loc_009EEC57;
loc_009EEE4A:
    if ((*(uint64_t *)(v_stack_m2B0 + 0x8)) != 1) goto loc_009ED8AD;
    *(uint8_t *)(arg4 + 0x1) = (uint8_t)(*(uint8_t *)(v_stack_m2B0 + 0x10));
    result = RtlValidProcessProtection(*(uint8_t *)(v_stack_m2B0 + 0x10), result, v_stack_m1D0, v_stack_p10);
    goto loc_009EE1AB;
loc_009EEE67:
    if ((*(uint64_t *)(v_stack_m2B0 + 0x8)) != 8) goto loc_009ED8AD;
    *(uint64_t *)(arg4 + 0x98) = *(uint64_t *)(v_stack_m2B0 + 0x10);
    goto loc_009EEC57;
loc_009EEE83:
    if ((*(uint64_t *)(v_stack_m2B0 + 0x8)) != 8) goto loc_009ED8AD;
    *(uint64_t *)(arg4 + 0x90) = *(uint64_t *)(v_stack_m2B0 + 0x10);
    goto loc_009EEC57;
loc_009EEE9F:
    if ((*(uint64_t *)(v_stack_m2B0 + 0x8)) != 8) goto loc_009ED8AD;
    *(uint64_t *)(arg4 + 0x80) = *(uint64_t *)(v_stack_m2B0 + 0x10);
    goto loc_009EEC57;
loc_009EEEBB:
    local_rdi = (v_stack_m2B0) + (32);
    v_stack_m2B0 = local_rdi;
    goto loc_009ED877;
loc_009EEEEE:
loc_009EEEF0:
loc_009EEEF5:
    v_stack_m2B8 = 0;
loc_009EEEF9:
    goto loc_009EEF10;
loc_009EEF10:
    if (sign_flag) goto loc_009EEF6B;
    result = (uint32_t)(*(uint32_t *)(arg4 + 0x8));
    local_rbx = 0;
    if (!(condition_is_above_or_equal)) {
        Arg2 = *(uint32_t *)(arg4 + 0x124);
        Arg4 = v_rip + 633473;
        Arg3 = 8;
        Arg1 = *(uint64_t *)(arg4 + 0x128);
        result = qsort(Arg1, Arg2, Arg3, Arg4);
        result = *(uint64_t *)(arg4 + 0x128);
        local_rbx = 0;
        if ((*(uint32_t *)(result)) < 0) { local_rbx = (uint32_t)((uint32_t)(0xC000000DULL)); }
        Arg2 = (v_stack_m278 != 0) ? 1 : 0;
        result = *(uint8_t *)(arg4 + 0x10);
        result = (uint8_t)((result) & (254));
        Arg2 = (uint8_t)((Arg2) | ((uint8_t)(result)));
        *(uint8_t *)(arg4 + 0x10) = Arg2;
    }
    if (sign_flag) {
        Arg1 = Arg4;
        result = PspDeleteCreateProcessContext(Arg1, Arg2, Arg3, Arg4);
    }
loc_009EEF75:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (720);
    return result;
loc_009EEF99:
    result = ExRaiseDatatypeMisalignment(Arg1, Arg2, Arg3, Arg4);
loc_009EEF9E:
    result = ExRaiseDatatypeMisalignment(Arg1, Arg2, Arg3, Arg4);
loc_009EEFA3:
    result = ExRaiseDatatypeMisalignment(Arg1, Arg2, Arg3, Arg4);
loc_009EEFA8:
    result = ExRaiseDatatypeMisalignment(Arg1, Arg2, Arg3, Arg4);
loc_009EEFAD:
    result = ExRaiseDatatypeMisalignment(Arg1, Arg2, Arg3, Arg4);
loc_009EEFB2:
    result = ExRaiseDatatypeMisalignment(Arg1, Arg2, Arg3, Arg4);
loc_009EEFB7:
    result = ExRaiseDatatypeMisalignment(Arg1, Arg2, Arg3, Arg4);
loc_009EEFBC:
    result = ExRaiseDatatypeMisalignment(Arg1, Arg2, Arg3, Arg4);
loc_009EEFC1:
    result = ExRaiseDatatypeMisalignment(Arg1, Arg2, Arg3, Arg4);
loc_009EEFC6:
    result = ExRaiseDatatypeMisalignment(Arg1, Arg2, Arg3, Arg4);
loc_009EEFCB:
    result = ExRaiseDatatypeMisalignment(Arg1, Arg2, Arg3, Arg4);
loc_009EEFD0:
    result = ExRaiseDatatypeMisalignment(Arg1, Arg2, Arg3, Arg4);
loc_009EEFD5:
    result = ExRaiseDatatypeMisalignment(Arg1, Arg2, Arg3, Arg4);
loc_009EEFDA:
    result = ExRaiseDatatypeMisalignment(Arg1, Arg2, Arg3, Arg4);
loc_009EEFDF:
    result = ExRaiseDatatypeMisalignment(Arg1, Arg2, Arg3, Arg4);
loc_009EEFE4:
    result = ExRaiseDatatypeMisalignment(Arg1, Arg2, Arg3, Arg4);
loc_009EEFE9:
    result = ExRaiseDatatypeMisalignment(Arg1, Arg2, Arg3, Arg4);
loc_009EEFEE:
    result = ExRaiseDatatypeMisalignment(Arg1, Arg2, Arg3, Arg4);
loc_009EEFF3:
    result = ExRaiseDatatypeMisalignment(Arg1, Arg2, Arg3, Arg4);
loc_009EEFF8:
    result = ExRaiseDatatypeMisalignment(Arg1, Arg2, Arg3, Arg4);
loc_009EEFFD:
    result = ExRaiseDatatypeMisalignment(Arg1, Arg2, Arg3, Arg4);
loc_009EF002:
    result = ExRaiseDatatypeMisalignment(Arg1, Arg2, Arg3, Arg4);
loc_009EF007:
    result = ExRaiseDatatypeMisalignment(Arg1, Arg2, Arg3, Arg4);
loc_009EF00C:
    result = ExRaiseDatatypeMisalignment(Arg1, Arg2, Arg3, Arg4);
loc_009EF011:
    result = ExRaiseDatatypeMisalignment(Arg1, Arg2, Arg3, Arg4);
loc_009EF016:
    result = ExRaiseDatatypeMisalignment(Arg1, Arg2, Arg3, Arg4);
loc_009EF01B:
    result = ExRaiseDatatypeMisalignment(Arg1, Arg2, Arg3, Arg4);
loc_009EF020:
    result = ExRaiseDatatypeMisalignment(Arg1, Arg2, Arg3, Arg4);
loc_009EF025:
    result = ExRaiseDatatypeMisalignment(Arg1, Arg2, Arg3, Arg4);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg4` | `+ 0x0` | `8` | `W` |
| `Arg4` | `+ 0x0` | `128` | `W` |
| `Arg4` | `+ 0x1` | `8` | `W` |
| `Arg4` | `+ 0x2` | `8` | `W` |
| `Arg4` | `+ 0x8` | `32` | `R` |
| `Arg4` | `+ 0x8` | `64` | `R` |
| `Arg4` | `+ 0x8` | `64` | `W` |
| `Arg4` | `+ 0x10` | `8` | `R` |
| `Arg4` | `+ 0x10` | `8` | `W` |
| `Arg4` | `+ 0x11` | `8` | `R` |
| `Arg4` | `+ 0x11` | `8` | `W` |
| `Arg4` | `+ 0x14` | `32` | `W` |
| `Arg4` | `+ 0x18` | `64` | `W` |
| `Arg4` | `+ 0x20` | `64` | `W` |
| `Arg4` | `+ 0x28` | `64` | `W` |
| `Arg4` | `+ 0x80` | `64` | `W` |
| `Arg4` | `+ 0x90` | `64` | `W` |
| `Arg4` | `+ 0x98` | `64` | `W` |
| `Arg4` | `+ 0xA8` | `16` | `W` |
| `Arg4` | `+ 0xAA` | `16` | `W` |
| `Arg4` | `+ 0xF0` | `16` | `W` |
| `Arg4` | `+ 0xF0` | `128` | `R` |
| `Arg4` | `+ 0xF2` | `16` | `W` |
| `Arg4` | `+ 0xF8` | `64` | `W` |
| `Arg4` | `+ 0x100` | `64` | `W` |
| `Arg4` | `+ 0x108` | `64` | `R` |
| `Arg4` | `+ 0x120` | `32` | `W` |
| `Arg4` | `+ 0x124` | `32` | `R` |
| `Arg4` | `+ 0x124` | `32` | `W` |
| `Arg4` | `+ 0x128` | `64` | `R` |
| `Arg4` | `+ 0x128` | `64` | `W` |
| `Arg4` | `+ 0x13C` | `32` | `W` |

추가 오프셋 33개는 표에서 생략했습니다.

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009ED6E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
