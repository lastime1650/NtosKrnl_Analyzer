# MmQueryVirtualMemory

- RVA: `0x009D9280`–`0x009DA2A8` (길이 `4,136` bytes)
- VA: `0x00000001409D9280`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A2F2C`
- 디코드: `1,001`개 명령, `4,136/4,136` bytes 표시
- 미해석 바이트: `1` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **58**; 고유 호출 대상: **34**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x009D9440` → [MiIsUserQueryVmCallerTrusted](../9F/MiIsUserQueryVmCallerTrusted_function_009FE378.md) (function, `0x009FE378`)
- `0x009D949B` → [ProbeForWrite](../8E/ProbeForWrite_function_008E91C0.md) (function, `0x008E91C0`)
- `0x009D9538` → [RtlCompareMemoryUlong](../../text/6B/RtlCompareMemoryUlong_function_006BA6F0.md) (function, `0x006BA6F0`)
- `0x009D9608` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x009D962E` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x009D9657` → [MiQueryMemoryPhysicalContiguity](../AD/MiQueryMemoryPhysicalContiguity_function_00AD5B98.md) (function, `0x00AD5B98`)
- `0x009D966E` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x009D96A1` → [MmQueryBadAddresses](../AD/MmQueryBadAddresses_function_00AD5430.md) (function, `0x00AD5430`)
- `0x009D96B8` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x009D96D7` → [MiGetWorkingSetInfoList](../../text/2A/MiGetWorkingSetInfoList_function_002AF770.md) (function, `0x002AF770`)
- `0x009D96EE` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x009D972A` → [MiGetWorkingSetInfo](../../text/29/MiGetWorkingSetInfo_function_0029E498.md) (function, `0x0029E498`)
- `0x009D9741` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x009D978E` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x009D97AE` → [Feature_605966648__private_IsEnabledDeviceUsageNoInline](../../text/68/Feature_605966648__private_IsEnabledDeviceUsageNoInline_function_006872AC.md) (function, `0x006872AC`)
- `0x009D97D4` → [MiQueryImageExtensionInformation](../../text/4E/MiQueryImageExtensionInformation_function_004EE3C8.md) (function, `0x004EE3C8`)
- `0x009D97F3` → [KiStackAttachProcess](../../text/21/KiStackAttachProcess_function_00216820.md) (function, `0x00216820`)
- `0x009D982A` → [VslQueryVirtualMemory](../../text/4B/VslQueryVirtualMemory_function_004BBFD8.md) (function, `0x004BBFD8`)
- `0x009D9847` → [MiGetProcessPartition](../../text/44/MiGetProcessPartition_function_00443B10.md) (function, `0x00443B10`)
- `0x009D9871` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (function, `0x00217D30`)
- `0x009D987E` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x009D98EB` → [MiQueryImageExtensionInformationOld](../../text/68/MiQueryImageExtensionInformationOld_function_00687384.md) (function, `0x00687384`)
- `0x009D9901` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (function, `0x00217D30`)
- `0x009D990E` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x009D992F` → [MiReturnLockedVadOrNextVa](../../text/31/MiReturnLockedVadOrNextVa_function_00316980.md) (function, `0x00316980`)
- `0x009D994A` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (function, `0x00217D30`)
- `0x009D9957` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x009D9981` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (function, `0x00217D30`)
- `0x009D998E` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x009D99DE` → [MiSetBasicInfoPartitionId](../../text/48/MiSetBasicInfoPartitionId_function_00487EC4.md) (function, `0x00487EC4`)
- `0x009D9A54` → [MI_GET_GRAPHICS_PROTECTION_FROM_VAD](../../text/43/MI_GET_GRAPHICS_PROTECTION_FROM_VAD_function_00438CA0.md) (function, `0x00438CA0`)
- `0x009D9A95` → [MiIsSoftwareEnclave](../../text/45/MiIsSoftwareEnclave_function_00456B2C.md) (function, `0x00456B2C`)
- `0x009D9BA3` → [MiReferenceControlAreaFile](../../text/43/MiReferenceControlAreaFile_function_00431554.md) (function, `0x00431554`)
- `0x009D9CA5` → [MiVadMapsLargeImage](../../text/2A/MiVadMapsLargeImage_function_002A70F0.md) (function, `0x002A70F0`)
- `0x009D9CB3` → [MiLocateLockedVadEvent](../../text/2A/MiLocateLockedVadEvent_function_002A7A0C.md) (function, `0x002A7A0C`)
- `0x009D9D1D` → [MiReadVadFlags2](../../text/45/MiReadVadFlags2_function_00452C1C.md) (function, `0x00452C1C`)
- `0x009D9D3E` → [MiUnlockAndDereferenceVadShared](../../text/2A/MiUnlockAndDereferenceVadShared_function_002AEF10.md) (function, `0x002AEF10`)
- `0x009D9D52` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (function, `0x00217D30`)
- `0x009D9D5F` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x009D9DD0` → [MiQueryAddressSpan](../../text/45/MiQueryAddressSpan_function_0045CF14.md) (function, `0x0045CF14`)
- `0x009D9DE8` → [MiUnlockAndDereferenceVadShared](../../text/2A/MiUnlockAndDereferenceVadShared_function_002AEF10.md) (function, `0x002AEF10`)
- `0x009D9DFC` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (function, `0x00217D30`)
- `0x009D9E09` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x009D9EA7` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x009D9ECA` → [ObQueryNameStringMode](../8A/ObQueryNameStringMode_function_008A7ED0.md) (function, `0x008A7ED0`)
- `0x009D9ED9` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x009D9F79` → [MiGetVadPageSize](../../text/42/MiGetVadPageSize_function_0042F0E0.md) (function, `0x0042F0E0`)
- `0x009D9F8B` → [MiGetProcessPartition](../../text/44/MiGetProcessPartition_function_00443B10.md) (function, `0x00443B10`)
- `0x009D9FAC` → [MiGetAweVadPartition](../../text/2A/MiGetAweVadPartition_function_002A94E8.md) (function, `0x002A94E8`)
- `0x009D9FB7` → [MiGetAweVadPageSize](../AD/MiGetAweVadPageSize_function_00AD58F8.md) (function, `0x00AD58F8`)
- `0x009D9FE5` → [MiLocateLockedVadEvent](../../text/2A/MiLocateLockedVadEvent_function_002A7A0C.md) (function, `0x002A7A0C`)
- `0x009D9FFE` → [PsReferencePartitionSafe](../../text/3B/PsReferencePartitionSafe_function_003BA6C0.md) (function, `0x003BA6C0`)
- `0x009DA026` → [MiGetControlAreaPartition](../../text/43/MiGetControlAreaPartition_function_0043E560.md) (function, `0x0043E560`)
- `0x009DA04D` → [PsDereferencePartition](../../text/34/PsDereferencePartition_function_00342E70.md) (function, `0x00342E70`)
- `0x009DA05F` → [MiUnlockAndDereferenceVadShared](../../text/2A/MiUnlockAndDereferenceVadShared_function_002AEF10.md) (function, `0x002AEF10`)
- `0x009DA073` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (function, `0x00217D30`)
- `0x009DA082` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x009DA251` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [SMKM_STORE&lt;SM_TRAITS&gt;::SmStCompareRegionDataCallback](../../text/34/SMKM_STORE_SM_TRAITS_SmStCompareRegionDataCallback_function_0034D390.md) at `0x0034D4EA`
- [NtPssCaptureVaSpaceBulk](../7D/NtPssCaptureVaSpaceBulk_function_007D4EA0.md) at `0x007D5226`
- [PfpVirtualQuery](../90/PfpVirtualQuery_function_00901C1C.md) at `0x00901CE3`
- [NtQueryVirtualMemory](NtQueryVirtualMemory_function_009D9240.md) at `0x009D9260`

### Static image references
- `0x009D9295` → RVA `0x00E0A740` (`.data`; read)
- `0x009D9360` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x009D95C7` → RVA `0x00FC6A98` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **51**
  - `0x009D9538` → [RtlCompareMemoryUlong](../../text/6B/RtlCompareMemoryUlong_function_006BA6F0.md) (`PAGE` → `.text`)
  - `0x009D962E` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x009D966E` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x009D96B8` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x009D96D7` → [MiGetWorkingSetInfoList](../../text/2A/MiGetWorkingSetInfoList_function_002AF770.md) (`PAGE` → `.text`)
  - `0x009D96EE` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x009D972A` → [MiGetWorkingSetInfo](../../text/29/MiGetWorkingSetInfo_function_0029E498.md) (`PAGE` → `.text`)
  - `0x009D9741` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x009D978E` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x009D97AE` → [Feature_605966648__private_IsEnabledDeviceUsageNoInline](../../text/68/Feature_605966648__private_IsEnabledDeviceUsageNoInline_function_006872AC.md) (`PAGE` → `.text`)
  - `0x009D97D4` → [MiQueryImageExtensionInformation](../../text/4E/MiQueryImageExtensionInformation_function_004EE3C8.md) (`PAGE` → `.text`)
  - `0x009D97F3` → [KiStackAttachProcess](../../text/21/KiStackAttachProcess_function_00216820.md) (`PAGE` → `.text`)
  - `0x009D982A` → [VslQueryVirtualMemory](../../text/4B/VslQueryVirtualMemory_function_004BBFD8.md) (`PAGE` → `.text`)
  - `0x009D9847` → [MiGetProcessPartition](../../text/44/MiGetProcessPartition_function_00443B10.md) (`PAGE` → `.text`)
  - `0x009D9871` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (`PAGE` → `.text`)
  - `0x009D987E` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x009D98EB` → [MiQueryImageExtensionInformationOld](../../text/68/MiQueryImageExtensionInformationOld_function_00687384.md) (`PAGE` → `.text`)
  - `0x009D9901` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (`PAGE` → `.text`)
  - `0x009D990E` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x009D992F` → [MiReturnLockedVadOrNextVa](../../text/31/MiReturnLockedVadOrNextVa_function_00316980.md) (`PAGE` → `.text`)
  - `0x009D994A` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (`PAGE` → `.text`)
  - `0x009D9957` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x009D9981` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (`PAGE` → `.text`)
  - `0x009D998E` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x009D99DE` → [MiSetBasicInfoPartitionId](../../text/48/MiSetBasicInfoPartitionId_function_00487EC4.md) (`PAGE` → `.text`)
  - `0x009D9A54` → [MI_GET_GRAPHICS_PROTECTION_FROM_VAD](../../text/43/MI_GET_GRAPHICS_PROTECTION_FROM_VAD_function_00438CA0.md) (`PAGE` → `.text`)
  - `0x009D9A95` → [MiIsSoftwareEnclave](../../text/45/MiIsSoftwareEnclave_function_00456B2C.md) (`PAGE` → `.text`)
  - `0x009D9BA3` → [MiReferenceControlAreaFile](../../text/43/MiReferenceControlAreaFile_function_00431554.md) (`PAGE` → `.text`)
  - `0x009D9CA5` → [MiVadMapsLargeImage](../../text/2A/MiVadMapsLargeImage_function_002A70F0.md) (`PAGE` → `.text`)
  - `0x009D9CB3` → [MiLocateLockedVadEvent](../../text/2A/MiLocateLockedVadEvent_function_002A7A0C.md) (`PAGE` → `.text`)
  - `0x009D9D1D` → [MiReadVadFlags2](../../text/45/MiReadVadFlags2_function_00452C1C.md) (`PAGE` → `.text`)
  - `0x009D9D3E` → [MiUnlockAndDereferenceVadShared](../../text/2A/MiUnlockAndDereferenceVadShared_function_002AEF10.md) (`PAGE` → `.text`)
  - `0x009D9D52` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (`PAGE` → `.text`)
  - `0x009D9D5F` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x009D9DD0` → [MiQueryAddressSpan](../../text/45/MiQueryAddressSpan_function_0045CF14.md) (`PAGE` → `.text`)
  - `0x009D9DE8` → [MiUnlockAndDereferenceVadShared](../../text/2A/MiUnlockAndDereferenceVadShared_function_002AEF10.md) (`PAGE` → `.text`)
  - `0x009D9DFC` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (`PAGE` → `.text`)
  - `0x009D9E09` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x009D9EA7` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x009D9ED9` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x009D9F79` → [MiGetVadPageSize](../../text/42/MiGetVadPageSize_function_0042F0E0.md) (`PAGE` → `.text`)
  - `0x009D9F8B` → [MiGetProcessPartition](../../text/44/MiGetProcessPartition_function_00443B10.md) (`PAGE` → `.text`)
  - `0x009D9FAC` → [MiGetAweVadPartition](../../text/2A/MiGetAweVadPartition_function_002A94E8.md) (`PAGE` → `.text`)
  - `0x009D9FE5` → [MiLocateLockedVadEvent](../../text/2A/MiLocateLockedVadEvent_function_002A7A0C.md) (`PAGE` → `.text`)
  - `0x009D9FFE` → [PsReferencePartitionSafe](../../text/3B/PsReferencePartitionSafe_function_003BA6C0.md) (`PAGE` → `.text`)
  - `0x009DA026` → [MiGetControlAreaPartition](../../text/43/MiGetControlAreaPartition_function_0043E560.md) (`PAGE` → `.text`)
  - `0x009DA04D` → [PsDereferencePartition](../../text/34/PsDereferencePartition_function_00342E70.md) (`PAGE` → `.text`)
  - `0x009DA05F` → [MiUnlockAndDereferenceVadShared](../../text/2A/MiUnlockAndDereferenceVadShared_function_002AEF10.md) (`PAGE` → `.text`)
  - `0x009DA073` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (`PAGE` → `.text`)
  - `0x009DA082` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x009DA251` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009D9280  4C 8B DC                        mov r11, rsp
009D9283  53                              push rbx
009D9284  56                              push rsi
009D9285  57                              push rdi
009D9286  41 54                           push r12
009D9288  41 55                           push r13
009D928A  41 56                           push r14
009D928C  41 57                           push r15
009D928E  48 81 EC 60 01 00 00            sub rsp, 0x160
009D9295  48 8B 05 A4 14 43 00            mov rax, qword ptr [rip + 0x4314a4]
009D929C  48 33 C4                        xor rax, rsp
009D929F  48 89 84 24 50 01 00 00         mov qword ptr [rsp + 0x150], rax
009D92A7  49 8B F1                        mov rsi, r9
009D92AA  4D 63 E8                        movsxd r13, r8d
009D92AD  44 89 6C 24 48                  mov dword ptr [rsp + 0x48], r13d
009D92B2  48 8B FA                        mov rdi, rdx
009D92B5  48 89 94 24 90 00 00 00         mov qword ptr [rsp + 0x90], rdx
009D92BD  48 89 4C 24 70                  mov qword ptr [rsp + 0x70], rcx
009D92C2  4C 8B A4 24 C8 01 00 00         mov r12, qword ptr [rsp + 0x1c8]
009D92CA  45 33 FF                        xor r15d, r15d
009D92CD  44 89 7C 24 50                  mov dword ptr [rsp + 0x50], r15d
009D92D2  4C 89 7C 24 60                  mov qword ptr [rsp + 0x60], r15
009D92D7  4C 89 7C 24 58                  mov qword ptr [rsp + 0x58], r15
009D92DC  4D 89 BB 48 FF FF FF            mov qword ptr [r11 - 0xb8], r15
009D92E3  0F 57 C0                        xorps xmm0, xmm0
009D92E6  0F 11 84 24 98 00 00 00         movups xmmword ptr [rsp + 0x98], xmm0
009D92EE  0F 11 84 24 A8 00 00 00         movups xmmword ptr [rsp + 0xa8], xmm0
009D92F6  0F 11 84 24 B8 00 00 00         movups xmmword ptr [rsp + 0xb8], xmm0
009D92FE  33 C0                           xor eax, eax
009D9300  0F 11 84 24 C8 00 00 00         movups xmmword ptr [rsp + 0xc8], xmm0
009D9308  49 89 83 40 FF FF FF            mov qword ptr [r11 - 0xc0], rax
009D930F  0F 57 C9                        xorps xmm1, xmm1
009D9312  41 0F 11 4B 88                  movups xmmword ptr [r11 - 0x78], xmm1
009D9317  41 0F 11 4B 98                  movups xmmword ptr [r11 - 0x68], xmm1
009D931C  41 0F 11 4B A8                  movups xmmword ptr [r11 - 0x58], xmm1
009D9321  44 89 7C 24 40                  mov dword ptr [rsp + 0x40], r15d
009D9326  4C 89 BC 24 88 00 00 00         mov qword ptr [rsp + 0x88], r15
009D932E  4C 89 BC 24 80 00 00 00         mov qword ptr [rsp + 0x80], r15
009D9336  4D 89 BB 50 FF FF FF            mov qword ptr [r11 - 0xb0], r15
009D933D  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
009D9346  48 89 4C 24 78                  mov qword ptr [rsp + 0x78], rcx
009D934B  0F B6 91 32 02 00 00            movzx edx, byte ptr [rcx + 0x232]
009D9352  88 54 24 44                     mov byte ptr [rsp + 0x44], dl
009D9356  41 83 FD 0E                     cmp r13d, 0xe
009D935A  0F 87 E1 0E 00 00               ja 0x1409da241
009D9360  4C 8D 05 99 6C 62 FF            lea r8, [rip - 0x9d9367]
009D9367  43 8B 84 A8 6C A2 9D 00         mov eax, dword ptr [r8 + r13*4 + 0x9da26c]
009D936F  49 03 C0                        add rax, r8
009D9372  FF E0                           jmp rax
009D9374  CC                              int3
009D9375  CC                              int3
009D9376  CC                              int3
009D9377  CC                              int3
009D9378  4C 8B B4 24 C0 01 00 00         mov r14, qword ptr [rsp + 0x1c0]
009D9380  49 83 FE 30                     cmp r14, 0x30
009D9384  0F 82 DA 00 00 00               jb 0x1409d9464
009D938A  E9 A1 00 00 00                  jmp 0x1409d9430
009D938F  4C 8B B4 24 C0 01 00 00         mov r14, qword ptr [rsp + 0x1c0]
009D9397  49 83 FE 08                     cmp r14, 8
009D939B  0F 82 C3 00 00 00               jb 0x1409d9464
009D93A1  BB 00 01 00 00                  mov ebx, 0x100
009D93A6  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
009D93AA  E9 85 00 00 00                  jmp 0x1409d9434
009D93AF  4C 8B B4 24 C0 01 00 00         mov r14, qword ptr [rsp + 0x1c0]
009D93B7  49 83 FE 10                     cmp r14, 0x10
009D93BB  0F 82 A3 00 00 00               jb 0x1409d9464
009D93C1  BB 00 01 00 00                  mov ebx, 0x100
009D93C6  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
009D93CA  EB 68                           jmp 0x1409d9434
009D93CC  4C 8B B4 24 C0 01 00 00         mov r14, qword ptr [rsp + 0x1c0]
009D93D4  49 83 FE 18                     cmp r14, 0x18
009D93D8  0F 82 86 00 00 00               jb 0x1409d9464
009D93DE  EB 50                           jmp 0x1409d9430
009D93E0  4C 8B B4 24 C0 01 00 00         mov r14, qword ptr [rsp + 0x1c0]
009D93E8  49 83 FE 20                     cmp r14, 0x20
009D93EC  72 76                           jb 0x1409d9464
009D93EE  EB 40                           jmp 0x1409d9430
009D93F0  4C 8B B4 24 C0 01 00 00         mov r14, qword ptr [rsp + 0x1c0]
009D93F8  49 83 FE 08                     cmp r14, 8
009D93FC  72 66                           jb 0x1409d9464
009D93FE  EB 30                           jmp 0x1409d9430
009D9400  4C 8B B4 24 C0 01 00 00         mov r14, qword ptr [rsp + 0x1c0]
009D9408  49 83 FE 28                     cmp r14, 0x28
009D940C  72 56                           jb 0x1409d9464
009D940E  BB 00 01 00 00                  mov ebx, 0x100
009D9413  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
009D9417  EB 1B                           jmp 0x1409d9434
009D9419  B8 BB 00 00 C0                  mov eax, 0xc00000bb
009D941E  E9 23 0E 00 00                  jmp 0x1409da246
009D9423  48 85 FF                        test rdi, rdi
009D9426  75 4B                           jne 0x1409d9473
009D9428  4C 8B B4 24 C0 01 00 00         mov r14, qword ptr [rsp + 0x1c0]
009D9430  8B 5C 24 40                     mov ebx, dword ptr [rsp + 0x40]
009D9434  81 FB 00 01 00 00               cmp ebx, 0x100
009D943A  75 41                           jne 0x1409d947d
009D943C  84 D2                           test dl, dl
009D943E  74 3D                           je 0x1409d947d
009D9440  E8 33 4F 02 00                  call 0x1409fe378
009D9445  85 C0                           test eax, eax
009D9447  75 34                           jne 0x1409d947d
009D9449  8B 84 24 D0 01 00 00            mov eax, dword ptr [rsp + 0x1d0]
009D9450  0F BA E8 1E                     bts eax, 0x1e
009D9454  EB 2E                           jmp 0x1409d9484
009D9456  4C 8B B4 24 C0 01 00 00         mov r14, qword ptr [rsp + 0x1c0]
009D945E  49 83 FE 18                     cmp r14, 0x18
009D9462  73 0A                           jae 0x1409d946e
009D9464  B8 04 00 00 C0                  mov eax, 0xc0000004
009D9469  E9 D8 0D 00 00                  jmp 0x1409da246
009D946E  48 85 FF                        test rdi, rdi
009D9471  75 BD                           jne 0x1409d9430
009D9473  B8 0D 00 00 C0                  mov eax, 0xc000000d
009D9478  E9 C9 0D 00 00                  jmp 0x1409da246
009D947D  8B 84 24 D0 01 00 00            mov eax, dword ptr [rsp + 0x1d0]
009D9484  89 44 24 54                     mov dword ptr [rsp + 0x54], eax
009D9488  44 38 7C 24 44                  cmp byte ptr [rsp + 0x44], r15b
009D948D  74 38                           je 0x1409d94c7
009D948F  41 B8 08 00 00 00               mov r8d, 8
009D9495  49 8B D6                        mov rdx, r14
009D9498  48 8B CE                        mov rcx, rsi
009D949B  E8 20 FD F0 FF                  call 0x1408e91c0
009D94A0  4D 85 E4                        test r12, r12
009D94A3  74 1B                           je 0x1409d94c0
009D94A5  48 B9 00 00 FF FF FF 7F 00 00   movabs rcx, 0x7fffffff0000
009D94AF  4C 3B E1                        cmp r12, rcx
009D94B2  49 0F 42 CC                     cmovb rcx, r12
009D94B6  48 8B 01                        mov rax, qword ptr [rcx]
009D94B9  48 89 01                        mov qword ptr [rcx], rax
009D94BC  8B 5C 24 40                     mov ebx, dword ptr [rsp + 0x40]
009D94C0  EB 05                           jmp 0x1409d94c7
009D94C2  E9 7F 0D 00 00                  jmp 0x1409da246
009D94C7  48 B8 FF FF FE FF FF 7F 00 00   movabs rax, 0x7ffffffeffff
009D94D1  48 3B F8                        cmp rdi, rax
009D94D4  77 9D                           ja 0x1409d9473
009D94D6  48 8B C7                        mov rax, rdi
009D94D9  48 25 00 F0 FF FF               and rax, 0xfffffffffffff000
009D94DF  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
009D94E4  41 83 FD 0A                     cmp r13d, 0xa
009D94E8  0F 85 BB 00 00 00               jne 0x1409d95a9
009D94EE  0F 10 06                        movups xmm0, xmmword ptr [rsi]
009D94F1  0F 11 84 24 F0 00 00 00         movups xmmword ptr [rsp + 0xf0], xmm0
009D94F9  0F 10 4E 10                     movups xmm1, xmmword ptr [rsi + 0x10]
009D94FD  0F 11 8C 24 00 01 00 00         movups xmmword ptr [rsp + 0x100], xmm1
009D9505  0F 10 46 20                     movups xmm0, xmmword ptr [rsi + 0x20]
009D9509  0F 11 84 24 10 01 00 00         movups xmmword ptr [rsp + 0x110], xmm0
009D9511  48 8B 84 24 08 01 00 00         mov rax, qword ptr [rsp + 0x108]
009D9519  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
009D9521  4C 89 BC 24 08 01 00 00         mov qword ptr [rsp + 0x108], r15
009D9529  45 33 C0                        xor r8d, r8d
009D952C  41 8D 50 30                     lea edx, [r8 + 0x30]
009D9530  48 8D 8C 24 F0 00 00 00         lea rcx, [rsp + 0xf0]
009D9538  E8 B3 11 CE FF                  call 0x1406ba6f0
009D953D  48 83 F8 30                     cmp rax, 0x30
009D9541  0F 85 2C FF FF FF               jne 0x1409d9473
009D9547  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
009D954F  48 8D 51 FF                     lea rdx, [rcx - 1]
009D9553  48 85 C9                        test rcx, rcx
009D9556  49 0F 44 D7                     cmove rdx, r15
009D955A  48 03 D7                        add rdx, rdi
009D955D  48 3B D7                        cmp rdx, rdi
009D9560  0F 82 0D FF FF FF               jb 0x1409d9473
009D9566  48 B8 FF FF FE FF FF 7F 00 00   movabs rax, 0x7ffffffeffff
009D9570  48 3B D0                        cmp rdx, rax
009D9573  0F 87 FA FE FF FF               ja 0x1409d9473
009D9579  48 8B C7                        mov rax, rdi
009D957C  25 FF 0F 00 00                  and eax, 0xfff
009D9581  48 81 C1 FF 0F 00 00            add rcx, 0xfff
009D9588  48 03 C8                        add rcx, rax
009D958B  48 81 E1 00 F0 FF FF            and rcx, 0xfffffffffffff000
009D9592  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
009D9597  48 03 C1                        add rax, rcx
009D959A  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
009D95A2  EB 05                           jmp 0x1409d95a9
009D95A4  E9 9D 0C 00 00                  jmp 0x1409da246
009D95A9  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
009D95AE  48 83 F8 FF                     cmp rax, -1
009D95B2  75 13                           jne 0x1409d95c7
009D95B4  48 8B 7C 24 78                  mov rdi, qword ptr [rsp + 0x78]
009D95B9  48 8B BF B8 00 00 00            mov rdi, qword ptr [rdi + 0xb8]
009D95C0  48 89 7C 24 60                  mov qword ptr [rsp + 0x60], rdi
009D95C5  EB 7B                           jmp 0x1409d9642
009D95C7  4C 8B 05 CA D4 5E 00            mov r8, qword ptr [rip + 0x5ed4ca]
009D95CE  F7 44 24 54 00 00 00 40         test dword ptr [rsp + 0x54], 0x40000000
009D95D6  BA 00 04 00 00                  mov edx, 0x400
009D95DB  B9 00 10 00 00                  mov ecx, 0x1000
009D95E0  0F 44 D1                        cmove edx, ecx
009D95E3  4C 89 7C 24 38                  mov qword ptr [rsp + 0x38], r15
009D95E8  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
009D95ED  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
009D95F2  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
009D95F7  C7 44 24 20 4D 6D 56 6D         mov dword ptr [rsp + 0x20], 0x6d566d4d
009D95FF  44 0F B6 4C 24 44               movzx r9d, byte ptr [rsp + 0x44]
009D9605  48 8B C8                        mov rcx, rax
009D9608  E8 43 00 E9 FF                  call 0x140869650
009D960D  85 C0                           test eax, eax
009D960F  0F 88 31 0C 00 00               js 0x1409da246
009D9615  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
009D961A  F7 87 FC 05 00 00 00 10 00 00   test dword ptr [rdi + 0x5fc], 0x1000
009D9624  74 17                           je 0x1409d963d
009D9626  BA 4D 6D 56 6D                  mov edx, 0x6d566d4d
009D962B  48 8B CF                        mov rcx, rdi
009D962E  E8 AD E2 91 FF                  call 0x1402f78e0
009D9633  B8 22 00 00 C0                  mov eax, 0xc0000022
009D9638  E9 09 0C 00 00                  jmp 0x1409da246
009D963D  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
009D9642  41 83 FD 0B                     cmp r13d, 0xb
009D9646  75 42                           jne 0x1409d968a
009D9648  44 0F B6 4C 24 44               movzx r9d, byte ptr [rsp + 0x44]
009D964E  4D 8B C6                        mov r8, r14
009D9651  48 8B D6                        mov rdx, rsi
009D9654  48 8B CF                        mov rcx, rdi
009D9657  E8 3C C5 0F 00                  call 0x140ad5b98
009D965C  8B D8                           mov ebx, eax
009D965E  48 83 7C 24 70 FF               cmp qword ptr [rsp + 0x70], -1
009D9664  74 0D                           je 0x1409d9673
009D9666  BA 4D 6D 56 6D                  mov edx, 0x6d566d4d
009D966B  48 8B CF                        mov rcx, rdi
009D966E  E8 6D E2 91 FF                  call 0x1402f78e0
009D9673  85 DB                           test ebx, ebx
009D9675  78 46                           js 0x1409d96bd
009D9677  4D 85 E4                        test r12, r12
009D967A  74 04                           je 0x1409d9680
009D967C  4D 89 34 24                     mov qword ptr [r12], r14
009D9680  E9 B8 0B 00 00                  jmp 0x1409da23d
009D9685  E9 B3 0B 00 00                  jmp 0x1409da23d
009D968A  41 83 FD 0C                     cmp r13d, 0xc
009D968E  75 34                           jne 0x1409d96c4
009D9690  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
009D9695  4D 8B CE                        mov r9, r14
009D9698  4C 8B C6                        mov r8, rsi
009D969B  41 8B D5                        mov edx, r13d
009D969E  48 8B CF                        mov rcx, rdi
009D96A1  E8 8A BD 0F 00                  call 0x140ad5430
009D96A6  8B D8                           mov ebx, eax
009D96A8  48 83 7C 24 70 FF               cmp qword ptr [rsp + 0x70], -1
009D96AE  74 0D                           je 0x1409d96bd
009D96B0  BA 4D 6D 56 6D                  mov edx, 0x6d566d4d
009D96B5  48 8B CF                        mov rcx, rdi
009D96B8  E8 23 E2 91 FF                  call 0x1402f78e0
009D96BD  8B C3                           mov eax, ebx
009D96BF  E9 82 0B 00 00                  jmp 0x1409da246
009D96C4  41 83 FD 04                     cmp r13d, 4
009D96C8  75 40                           jne 0x1409d970a
009D96CA  4D 8B CE                        mov r9, r14
009D96CD  4C 8B C6                        mov r8, rsi
009D96D0  8B 54 24 54                     mov edx, dword ptr [rsp + 0x54]
009D96D4  48 8B CF                        mov rcx, rdi
009D96D7  E8 94 60 8D FF                  call 0x1402af770
009D96DC  8B D8                           mov ebx, eax
009D96DE  48 83 7C 24 70 FF               cmp qword ptr [rsp + 0x70], -1
009D96E4  74 0D                           je 0x1409d96f3
009D96E6  BA 4D 6D 56 6D                  mov edx, 0x6d566d4d
009D96EB  48 8B CF                        mov rcx, rdi
009D96EE  E8 ED E1 91 FF                  call 0x1402f78e0
009D96F3  85 DB                           test ebx, ebx
009D96F5  78 C6                           js 0x1409d96bd
009D96F7  4D 85 E4                        test r12, r12
009D96FA  74 04                           je 0x1409d9700
009D96FC  4D 89 34 24                     mov qword ptr [r12], r14
009D9700  E9 38 0B 00 00                  jmp 0x1409da23d
009D9705  E9 33 0B 00 00                  jmp 0x1409da23d
009D970A  41 83 FD 01                     cmp r13d, 1
009D970E  75 61                           jne 0x1409d9771
009D9710  48 8D 84 24 E0 00 00 00         lea rax, [rsp + 0xe0]
009D9718  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
009D971D  4D 8B CE                        mov r9, r14
009D9720  4C 8B C6                        mov r8, rsi
009D9723  8B 54 24 54                     mov edx, dword ptr [rsp + 0x54]
009D9727  48 8B CF                        mov rcx, rdi
009D972A  E8 69 4D 8C FF                  call 0x14029e498
009D972F  8B D8                           mov ebx, eax
009D9731  48 83 7C 24 70 FF               cmp qword ptr [rsp + 0x70], -1
009D9737  74 0D                           je 0x1409d9746
009D9739  BA 4D 6D 56 6D                  mov edx, 0x6d566d4d
009D973E  48 8B CF                        mov rcx, rdi
009D9741  E8 9A E1 91 FF                  call 0x1402f78e0
009D9746  85 DB                           test ebx, ebx
009D9748  0F 88 6F FF FF FF               js 0x1409d96bd
009D974E  4D 85 E4                        test r12, r12
009D9751  74 14                           je 0x1409d9767
009D9753  48 8B 84 24 E0 00 00 00         mov rax, qword ptr [rsp + 0xe0]
009D975B  48 8D 04 C5 08 00 00 00         lea rax, [rax*8 + 8]
009D9763  49 89 04 24                     mov qword ptr [r12], rax
009D9767  E9 D1 0A 00 00                  jmp 0x1409da23d
009D976C  E9 CC 0A 00 00                  jmp 0x1409da23d
009D9771  41 83 FD 05                     cmp r13d, 5
009D9775  75 37                           jne 0x1409d97ae
009D9777  48 8B 9F A8 06 00 00            mov rbx, qword ptr [rdi + 0x6a8]
009D977E  48 83 F8 FF                     cmp rax, -1
009D9782  74 10                           je 0x1409d9794
009D9784  BA 4D 6D 56 6D                  mov edx, 0x6d566d4d
009D9789  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
009D978E  E8 4D E1 91 FF                  call 0x1402f78e0
009D9793  90                              nop
009D9794  48 89 1E                        mov qword ptr [rsi], rbx
009D9797  4D 85 E4                        test r12, r12
009D979A  74 08                           je 0x1409d97a4
009D979C  49 C7 04 24 08 00 00 00         mov qword ptr [r12], 8
009D97A4  E9 94 0A 00 00                  jmp 0x1409da23d
009D97A9  E9 8F 0A 00 00                  jmp 0x1409da23d
009D97AE  E8 F9 DA CA FF                  call 0x1406872ac
009D97B3  89 44 24 78                     mov dword ptr [rsp + 0x78], eax
009D97B7  85 C0                           test eax, eax
009D97B9  74 23                           je 0x1409d97de
009D97BB  41 83 FD 0E                     cmp r13d, 0xe
009D97BF  75 1D                           jne 0x1409d97de
009D97C1  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
009D97C6  4C 8B 8C 24 90 00 00 00         mov r9, qword ptr [rsp + 0x90]
009D97CE  48 8B D6                        mov rdx, rsi
009D97D1  48 8B CF                        mov rcx, rdi
009D97D4  E8 EF 4B B1 FF                  call 0x1404ee3c8
009D97D9  E9 C8 FE FF FF                  jmp 0x1409d96a6
009D97DE  48 83 7C 24 70 FF               cmp qword ptr [rsp + 0x70], -1
009D97E4  74 19                           je 0x1409d97ff
009D97E6  4C 8D 84 24 20 01 00 00         lea r8, [rsp + 0x120]
009D97EE  33 D2                           xor edx, edx
009D97F0  48 8B CF                        mov rcx, rdi
009D97F3  E8 28 D0 83 FF                  call 0x140216820
009D97F8  83 CB 01                        or ebx, 1
009D97FB  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
009D97FF  41 83 FD 08                     cmp r13d, 8
009D9803  0F 85 C7 00 00 00               jne 0x1409d98d0
009D9809  48 83 BF 70 01 00 00 00         cmp qword ptr [rdi + 0x170], 0
009D9811  0F 84 B9 00 00 00               je 0x1409d98d0
009D9817  4C 8D 84 24 98 00 00 00         lea r8, [rsp + 0x98]
009D981F  48 8B 94 24 90 00 00 00         mov rdx, qword ptr [rsp + 0x90]
009D9827  48 8B CF                        mov rcx, rdi
009D982A  E8 A9 27 AE FF                  call 0x1404bbfd8
009D982F  85 C0                           test eax, eax
009D9831  0F 88 99 00 00 00               js 0x1409d98d0
009D9837  81 BC 24 B8 00 00 00 00 10 00 00  cmp dword ptr [rsp + 0xb8], 0x1000
009D9842  75 15                           jne 0x1409d9859
009D9844  48 8B CF                        mov rcx, rdi
009D9847  E8 C4 A2 A6 FF                  call 0x140443b10
009D984C  0F B7 08                        movzx ecx, word ptr [rax]
009D984F  66 89 8C 24 AC 00 00 00         mov word ptr [rsp + 0xac], cx
009D9857  EB 09                           jmp 0x1409d9862
009D9859  66 44 89 BC 24 AC 00 00 00      mov word ptr [rsp + 0xac], r15w
009D9862  F6 C3 01                        test bl, 1
009D9865  74 1D                           je 0x1409d9884
009D9867  33 D2                           xor edx, edx
009D9869  48 8D 8C 24 20 01 00 00         lea rcx, [rsp + 0x120]
009D9871  E8 BA E4 83 FF                  call 0x140217d30
009D9876  BA 4D 6D 56 6D                  mov edx, 0x6d566d4d
009D987B  48 8B CF                        mov rcx, rdi
009D987E  E8 5D E0 91 FF                  call 0x1402f78e0
009D9883  90                              nop
009D9884  0F 10 84 24 98 00 00 00         movups xmm0, xmmword ptr [rsp + 0x98]
009D988C  0F 11 06                        movups xmmword ptr [rsi], xmm0
009D988F  0F 10 8C 24 A8 00 00 00         movups xmm1, xmmword ptr [rsp + 0xa8]
009D9897  0F 11 4E 10                     movups xmmword ptr [rsi + 0x10], xmm1
009D989B  0F 10 84 24 B8 00 00 00         movups xmm0, xmmword ptr [rsp + 0xb8]
009D98A3  0F 11 46 20                     movups xmmword ptr [rsi + 0x20], xmm0
009D98A7  83 CB 02                        or ebx, 2
009D98AA  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
009D98AE  4D 85 E4                        test r12, r12
009D98B1  74 08                           je 0x1409d98bb
009D98B3  49 C7 04 24 30 00 00 00         mov qword ptr [r12], 0x30
009D98BB  E9 7D 09 00 00                  jmp 0x1409da23d
009D98C0  F6 44 24 40 02                  test byte ptr [rsp + 0x40], 2
009D98C5  0F 84 7B 09 00 00               je 0x1409da246
009D98CB  E9 6D 09 00 00                  jmp 0x1409da23d
009D98D0  83 7C 24 78 00                  cmp dword ptr [rsp + 0x78], 0
009D98D5  75 43                           jne 0x1409d991a
009D98D7  41 83 FD 0E                     cmp r13d, 0xe
009D98DB  75 3D                           jne 0x1409d991a
009D98DD  4D 8B CC                        mov r9, r12
009D98E0  4C 8B 84 24 90 00 00 00         mov r8, qword ptr [rsp + 0x90]
009D98E8  48 8B CE                        mov rcx, rsi
009D98EB  E8 94 DA CA FF                  call 0x140687384
009D98F0  8B F0                           mov esi, eax
009D98F2  F6 C3 01                        test bl, 1
009D98F5  74 1C                           je 0x1409d9913
009D98F7  33 D2                           xor edx, edx
009D98F9  48 8D 8C 24 20 01 00 00         lea rcx, [rsp + 0x120]
009D9901  E8 2A E4 83 FF                  call 0x140217d30
009D9906  BA 4D 6D 56 6D                  mov edx, 0x6d566d4d
009D990B  48 8B CF                        mov rcx, rdi
009D990E  E8 CD DF 91 FF                  call 0x1402f78e0
009D9913  8B C6                           mov eax, esi
009D9915  E9 2C 09 00 00                  jmp 0x1409da246
009D991A  4C 8D 84 24 E8 00 00 00         lea r8, [rsp + 0xe8]
009D9922  48 8D 54 24 58                  lea rdx, [rsp + 0x58]
009D9927  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
009D992F  E8 4C D0 93 FF                  call 0x140316980
009D9934  44 8B E8                        mov r13d, eax
009D9937  85 C0                           test eax, eax
009D9939  79 29                           jns 0x1409d9964
009D993B  F6 C3 01                        test bl, 1
009D993E  74 1C                           je 0x1409d995c
009D9940  33 D2                           xor edx, edx
009D9942  48 8D 8C 24 20 01 00 00         lea rcx, [rsp + 0x120]
009D994A  E8 E1 E3 83 FF                  call 0x140217d30
009D994F  BA 4D 6D 56 6D                  mov edx, 0x6d566d4d
009D9954  48 8B CF                        mov rcx, rdi
009D9957  E8 84 DF 91 FF                  call 0x1402f78e0
009D995C  41 8B C5                        mov eax, r13d
009D995F  E9 E2 08 00 00                  jmp 0x1409da246
009D9964  4C 8B 6C 24 58                  mov r13, qword ptr [rsp + 0x58]
009D9969  4D 85 ED                        test r13, r13
009D996C  0F 85 9A 00 00 00               jne 0x1409d9a0c
009D9972  F6 C3 01                        test bl, 1
009D9975  74 1C                           je 0x1409d9993
009D9977  33 D2                           xor edx, edx
009D9979  48 8D 8C 24 20 01 00 00         lea rcx, [rsp + 0x120]
009D9981  E8 AA E3 83 FF                  call 0x140217d30
009D9986  BA 4D 6D 56 6D                  mov edx, 0x6d566d4d
009D998B  48 8B CF                        mov rcx, rdi
009D998E  E8 4D DF 91 FF                  call 0x1402f78e0
009D9993  8B 44 24 48                     mov eax, dword ptr [rsp + 0x48]
009D9997  A9 F5 FF FF FF                  test eax, 0xfffffff5
009D999C  0F 85 DB 04 00 00               jne 0x1409d9e7d
009D99A2  83 F8 02                        cmp eax, 2
009D99A5  0F 84 D2 04 00 00               je 0x1409d9e7d
009D99AB  48 8B 84 24 E8 00 00 00         mov rax, qword ptr [rsp + 0xe8]
009D99B3  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
009D99B8  48 2B C1                        sub rax, rcx
009D99BB  4C 89 7E 08                     mov qword ptr [rsi + 8], r15
009D99BF  44 89 7E 10                     mov dword ptr [rsi + 0x10], r15d
009D99C3  48 89 0E                        mov qword ptr [rsi], rcx
009D99C6  48 89 46 18                     mov qword ptr [rsi + 0x18], rax
009D99CA  C7 46 20 00 00 01 00            mov dword ptr [rsi + 0x20], 0x10000
009D99D1  48 C7 46 24 01 00 00 00         mov qword ptr [rsi + 0x24], 1
009D99D9  33 D2                           xor edx, edx
009D99DB  48 8B CE                        mov rcx, rsi
009D99DE  E8 E1 E4 AA FF                  call 0x140487ec4
009D99E3  83 CB 02                        or ebx, 2
009D99E6  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
009D99EA  4D 85 E4                        test r12, r12
009D99ED  74 08                           je 0x1409d99f7
009D99EF  49 C7 04 24 30 00 00 00         mov qword ptr [r12], 0x30
009D99F7  E9 41 08 00 00                  jmp 0x1409da23d
009D99FC  F6 44 24 40 02                  test byte ptr [rsp + 0x40], 2
009D9A01  0F 84 3F 08 00 00               je 0x1409da246
009D9A07  E9 31 08 00 00                  jmp 0x1409da23d
009D9A0C  0F 57 C0                        xorps xmm0, xmm0
009D9A0F  F3 0F 7F 84 24 AC 00 00 00      movdqu xmmword ptr [rsp + 0xac], xmm0
009D9A18  44 89 BC 24 BC 00 00 00         mov dword ptr [rsp + 0xbc], r15d
009D9A20  44 89 BC 24 C4 00 00 00         mov dword ptr [rsp + 0xc4], r15d
009D9A28  4C 8B 54 24 68                  mov r10, qword ptr [rsp + 0x68]
009D9A2D  4C 89 94 24 98 00 00 00         mov qword ptr [rsp + 0x98], r10
009D9A35  41 0F B6 4D 20                  movzx ecx, byte ptr [r13 + 0x20]
009D9A3A  48 C1 E1 20                     shl rcx, 0x20
009D9A3E  41 8B 45 18                     mov eax, dword ptr [r13 + 0x18]
009D9A42  48 0B C8                        or rcx, rax
009D9A45  48 C1 E1 0C                     shl rcx, 0xc
009D9A49  48 89 8C 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rcx
009D9A51  49 8B CD                        mov rcx, r13
009D9A54  E8 47 F2 A5 FF                  call 0x140438ca0
009D9A59  41 8B 4D 30                     mov ecx, dword ptr [r13 + 0x30]
009D9A5D  48 C1 E9 07                     shr rcx, 7
009D9A61  83 E1 1F                        and ecx, 0x1f
009D9A64  48 8D 15 95 65 62 FF            lea rdx, [rip - 0x9d9a6b]
009D9A6B  0B 84 8A 30 46 01 00            or eax, dword ptr [rdx + rcx*4 + 0x14630]
009D9A72  89 84 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], eax
009D9A79  41 8B 45 30                     mov eax, dword ptr [r13 + 0x30]
009D9A7D  0F BA E0 15                     bt eax, 0x15
009D9A81  0F 83 8A 00 00 00               jae 0x1409d9b11
009D9A87  C7 84 24 C0 00 00 00 00 00 02 00  mov dword ptr [rsp + 0xc0], 0x20000
009D9A92  49 8B CD                        mov rcx, r13
009D9A95  E8 92 D0 A7 FF                  call 0x140456b2c
009D9A9A  85 C0                           test eax, eax
009D9A9C  74 07                           je 0x1409d9aa5
009D9A9E  83 CB 40                        or ebx, 0x40
009D9AA1  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
009D9AA5  41 8B 4D 34                     mov ecx, dword ptr [r13 + 0x34]
009D9AA9  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
009D9AAE  0F B6 50 22                     movzx edx, byte ptr [rax + 0x22]
009D9AB2  48 C1 E2 20                     shl rdx, 0x20
009D9AB6  48 0B D1                        or rdx, rcx
009D9AB9  8B 4C 24 40                     mov ecx, dword ptr [rsp + 0x40]
009D9ABD  0F BA E9 07                     bts ecx, 7
009D9AC1  49 B9 FD FF FF FF 07 00 00 00   movabs r9, 0x7fffffffd
009D9ACB  49 3B D1                        cmp rdx, r9
009D9ACE  0F 45 CB                        cmovne ecx, ebx
009D9AD1  4C 8B 6C 24 58                  mov r13, qword ptr [rsp + 0x58]
009D9AD6  41 8B 55 30                     mov edx, dword ptr [r13 + 0x30]
009D9ADA  83 E2 70                        and edx, 0x70
009D9ADD  8B C1                           mov eax, ecx
009D9ADF  83 C8 08                        or eax, 8
009D9AE2  83 FA 10                        cmp edx, 0x10
009D9AE5  0F 45 C1                        cmovne eax, ecx
009D9AE8  8B C8                           mov ecx, eax
009D9AEA  83 C9 10                        or ecx, 0x10
009D9AED  83 FA 30                        cmp edx, 0x30
009D9AF0  0F 45 C8                        cmovne ecx, eax
009D9AF3  8B D9                           mov ebx, ecx
009D9AF5  83 CB 20                        or ebx, 0x20
009D9AF8  41 F7 45 30 00 00 40 00         test dword ptr [r13 + 0x30], 0x400000
009D9B00  0F 44 D9                        cmove ebx, ecx
009D9B03  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
009D9B07  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
009D9B0C  E9 C7 00 00 00                  jmp 0x1409d9bd8
009D9B11  24 70                           and al, 0x70
009D9B13  3C 20                           cmp al, 0x20
009D9B15  75 1B                           jne 0x1409d9b32
009D9B17  C7 84 24 C0 00 00 00 00 00 00 01  mov dword ptr [rsp + 0xc0], 0x1000000
009D9B22  83 7C 24 48 07                  cmp dword ptr [rsp + 0x48], 7
009D9B27  75 62                           jne 0x1409d9b8b
009D9B29  49 8B 45 48                     mov rax, qword ptr [r13 + 0x48]
009D9B2D  48 8B 08                        mov rcx, qword ptr [rax]
009D9B30  EB 48                           jmp 0x1409d9b7a
009D9B32  C7 84 24 C0 00 00 00 00 00 04 00  mov dword ptr [rsp + 0xc0], 0x40000
009D9B3D  8B 44 24 48                     mov eax, dword ptr [rsp + 0x48]
009D9B41  83 F8 03                        cmp eax, 3
009D9B44  75 06                           jne 0x1409d9b4c
009D9B46  49 83 FE 30                     cmp r14, 0x30
009D9B4A  73 05                           jae 0x1409d9b51
009D9B4C  83 F8 07                        cmp eax, 7
009D9B4F  75 3A                           jne 0x1409d9b8b
009D9B51  49 8B 45 48                     mov rax, qword ptr [r13 + 0x48]
009D9B55  48 8B 08                        mov rcx, qword ptr [rax]
009D9B58  41 8B C7                        mov eax, r15d
009D9B5B  48 39 41 40                     cmp qword ptr [rcx + 0x40], rax
009D9B5F  0F 95 C0                        setne al
009D9B62  85 C0                           test eax, eax
009D9B64  75 0D                           jne 0x1409d9b73
009D9B66  C7 84 24 C0 00 00 00 00 00 00 08  mov dword ptr [rsp + 0xc0], 0x8000000
009D9B71  EB 18                           jmp 0x1409d9b8b
009D9B73  83 7C 24 48 07                  cmp dword ptr [rsp + 0x48], 7
009D9B78  75 11                           jne 0x1409d9b8b
009D9B7A  0F B6 41 3E                     movzx eax, byte ptr [rcx + 0x3e]
009D9B7E  24 0C                           and al, 0xc
009D9B80  3C 04                           cmp al, 4
009D9B82  75 07                           jne 0x1409d9b8b
009D9B84  83 CB 04                        or ebx, 4
009D9B87  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
009D9B8B  83 7C 24 48 02                  cmp dword ptr [rsp + 0x48], 2
009D9B90  75 3C                           jne 0x1409d9bce
009D9B92  49 8B 45 48                     mov rax, qword ptr [r13 + 0x48]
009D9B96  48 8B 08                        mov rcx, qword ptr [rax]
009D9B99  48 8B 41 40                     mov rax, qword ptr [rcx + 0x40]
009D9B9D  48 83 E0 F0                     and rax, 0xfffffffffffffff0
009D9BA1  74 0A                           je 0x1409d9bad
009D9BA3  E8 AC 79 A5 FF                  call 0x140431554
009D9BA8  4C 8B 54 24 68                  mov r10, qword ptr [rsp + 0x68]
009D9BAD  41 BF 01 00 00 00               mov r15d, 1
009D9BB3  48 85 C0                        test rax, rax
009D9BB6  49 0F 44 C7                     cmove rax, r15
009D9BBA  48 89 84 24 88 00 00 00         mov qword ptr [rsp + 0x88], rax
009D9BC2  49 B9 FD FF FF FF 07 00 00 00   movabs r9, 0x7fffffffd
009D9BCC  EB 10                           jmp 0x1409d9bde
009D9BCE  49 B9 FD FF FF FF 07 00 00 00   movabs r9, 0x7fffffffd
009D9BD8  41 BF 01 00 00 00               mov r15d, 1
009D9BDE  8B 44 24 48                     mov eax, dword ptr [rsp + 0x48]
009D9BE2  83 C0 FD                        add eax, -3
009D9BE5  A9 FB FF FF FF                  test eax, 0xfffffffb
009D9BEA  0F 84 06 03 00 00               je 0x1409d9ef6
009D9BF0  44 8B 7C 24 48                  mov r15d, dword ptr [rsp + 0x48]
009D9BF5  41 83 FF 06                     cmp r15d, 6
009D9BF9  0F 85 AC 01 00 00               jne 0x1409d9dab
009D9BFF  41 8B 45 30                     mov eax, dword ptr [r13 + 0x30]
009D9C03  0F BA E0 15                     bt eax, 0x15
009D9C07  0F 82 2E 01 00 00               jb 0x1409d9d3b
009D9C0D  24 70                           and al, 0x70
009D9C0F  3C 20                           cmp al, 0x20
009D9C11  0F 85 24 01 00 00               jne 0x1409d9d3b
009D9C17  49 8B 45 48                     mov rax, qword ptr [r13 + 0x48]
009D9C1B  48 8B 08                        mov rcx, qword ptr [rax]
009D9C1E  48 8B 11                        mov rdx, qword ptr [rcx]
009D9C21  0F B6 4A 0F                     movzx ecx, byte ptr [rdx + 0xf]
009D9C25  4C 8B 5C 24 58                  mov r11, qword ptr [rsp + 0x58]
009D9C2A  45 0F B6 53 20                  movzx r10d, byte ptr [r11 + 0x20]
009D9C2F  49 C1 E2 20                     shl r10, 0x20
009D9C33  41 8B 43 18                     mov eax, dword ptr [r11 + 0x18]
009D9C37  4C 0B D0                        or r10, rax
009D9C3A  49 C1 E2 0C                     shl r10, 0xc
009D9C3E  4C 89 94 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], r10
009D9C46  49 C7 C0 FF FF FF FF            mov r8, 0xffffffffffffffff
009D9C4D  49 8B C0                        mov rax, r8
009D9C50  F0 4C 0F B1 42 18               lock cmpxchg qword ptr [rdx + 0x18], r8
009D9C56  4C 8B C8                        mov r9, rax
009D9C59  48 89 84 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], rax
009D9C61  44 8B C1                        mov r8d, ecx
009D9C64  41 83 E0 0F                     and r8d, 0xf
009D9C68  41 C1 E0 02                     shl r8d, 2
009D9C6C  8B 8C 24 D8 00 00 00            mov ecx, dword ptr [rsp + 0xd8]
009D9C73  83 E1 C3                        and ecx, 0xffffffc3
009D9C76  44 0B C1                        or r8d, ecx
009D9C79  44 89 84 24 D8 00 00 00         mov dword ptr [rsp + 0xd8], r8d
009D9C81  4C 8B 6C 24 58                  mov r13, qword ptr [rsp + 0x58]
009D9C86  41 8B 45 30                     mov eax, dword ptr [r13 + 0x30]
009D9C8A  25 80 0F 00 00                  and eax, 0xf80
009D9C8F  3D 80 00 00 00                  cmp eax, 0x80
009D9C94  75 0C                           jne 0x1409d9ca2
009D9C96  41 83 C8 02                     or r8d, 2
009D9C9A  44 89 84 24 D8 00 00 00         mov dword ptr [rsp + 0xd8], r8d
009D9CA2  49 8B CD                        mov rcx, r13
009D9CA5  E8 46 D4 8C FF                  call 0x1402a70f0
009D9CAA  85 C0                           test eax, eax
009D9CAC  74 25                           je 0x1409d9cd3
009D9CAE  BA 10 00 00 00                  mov edx, 0x10
009D9CB3  E8 54 DD 8C FF                  call 0x1402a7a0c
009D9CB8  0F B6 48 08                     movzx ecx, byte ptr [rax + 8]
009D9CBC  48 8B 50 10                     mov rdx, qword ptr [rax + 0x10]
009D9CC0  8B C1                           mov eax, ecx
009D9CC2  48 C1 E0 10                     shl rax, 0x10
009D9CC6  49 03 C2                        add rax, r10
009D9CC9  48 89 84 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], rax
009D9CD1  EB 26                           jmp 0x1409d9cf9
009D9CD3  41 0F B6 55 21                  movzx edx, byte ptr [r13 + 0x21]
009D9CD8  48 C1 E2 20                     shl rdx, 0x20
009D9CDC  41 8B 45 1C                     mov eax, dword ptr [r13 + 0x1c]
009D9CE0  48 0B D0                        or rdx, rax
009D9CE3  41 0F B6 4B 20                  movzx ecx, byte ptr [r11 + 0x20]
009D9CE8  48 C1 E1 20                     shl rcx, 0x20
009D9CEC  41 8B 43 18                     mov eax, dword ptr [r11 + 0x18]
009D9CF0  48 0B C8                        or rcx, rax
009D9CF3  48 2B D1                        sub rdx, rcx
009D9CF6  48 FF C2                        inc rdx
009D9CF9  49 F7 C1 FF 0F 00 00            test r9, 0xfff
009D9D00  B8 00 00 00 00                  mov eax, 0
009D9D05  0F 95 C0                        setne al
009D9D08  49 C1 E9 0C                     shr r9, 0xc
009D9D0C  49 03 C1                        add rax, r9
009D9D0F  48 3B D0                        cmp rdx, rax
009D9D12  73 06                           jae 0x1409d9d1a
009D9D14  41 83 C8 01                     or r8d, 1
009D9D18  EB 10                           jmp 0x1409d9d2a
009D9D1A  49 8B CD                        mov rcx, r13
009D9D1D  E8 FA 8E A7 FF                  call 0x140452c1c
009D9D22  A8 20                           test al, 0x20
009D9D24  74 0C                           je 0x1409d9d32
009D9D26  41 83 C8 40                     or r8d, 0x40
009D9D2A  44 89 84 24 D8 00 00 00         mov dword ptr [rsp + 0xd8], r8d
009D9D32  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
009D9D37  8B 5C 24 40                     mov ebx, dword ptr [rsp + 0x40]
009D9D3B  49 8B CD                        mov rcx, r13
009D9D3E  E8 CD 51 8D FF                  call 0x1402aef10
009D9D43  F6 C3 01                        test bl, 1
009D9D46  74 1C                           je 0x1409d9d64
009D9D48  33 D2                           xor edx, edx
009D9D4A  48 8D 8C 24 20 01 00 00         lea rcx, [rsp + 0x120]
009D9D52  E8 D9 DF 83 FF                  call 0x140217d30
009D9D57  BA 4D 6D 56 6D                  mov edx, 0x6d566d4d
009D9D5C  48 8B CF                        mov rcx, rdi
009D9D5F  E8 7C DB 91 FF                  call 0x1402f78e0
009D9D64  B8 18 00 00 00                  mov eax, 0x18
009D9D69  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
009D9D6D  0F 10 84 24 C8 00 00 00         movups xmm0, xmmword ptr [rsp + 0xc8]
009D9D75  0F 11 06                        movups xmmword ptr [rsi], xmm0
009D9D78  F2 0F 10 8C 24 D8 00 00 00      movsd xmm1, qword ptr [rsp + 0xd8]
009D9D81  F2 0F 11 4E 10                  movsd qword ptr [rsi + 0x10], xmm1
009D9D86  83 CB 02                        or ebx, 2
009D9D89  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
009D9D8D  4D 85 E4                        test r12, r12
009D9D90  74 04                           je 0x1409d9d96
009D9D92  49 89 04 24                     mov qword ptr [r12], rax
009D9D96  E9 A2 04 00 00                  jmp 0x1409da23d
009D9D9B  F6 44 24 40 02                  test byte ptr [rsp + 0x40], 2
009D9DA0  0F 84 A0 04 00 00               je 0x1409da246
009D9DA6  E9 92 04 00 00                  jmp 0x1409da23d
009D9DAB  41 F7 C7 F5 FF FF FF            test r15d, 0xfffffff5
009D9DB2  75 31                           jne 0x1409d9de5
009D9DB4  41 83 FF 02                     cmp r15d, 2
009D9DB8  74 2B                           je 0x1409d9de5
009D9DBA  4D 8B CD                        mov r9, r13
009D9DBD  4C 8B 84 24 80 00 00 00         mov r8, qword ptr [rsp + 0x80]
009D9DC5  49 8B D2                        mov rdx, r10
009D9DC8  48 8D 8C 24 98 00 00 00         lea rcx, [rsp + 0x98]
009D9DD0  E8 3F 31 A8 FF                  call 0x14045cf14
009D9DD5  48 2B 84 24 98 00 00 00         sub rax, qword ptr [rsp + 0x98]
009D9DDD  48 89 84 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rax
009D9DE5  49 8B CD                        mov rcx, r13
009D9DE8  E8 23 51 8D FF                  call 0x1402aef10
009D9DED  F6 C3 01                        test bl, 1
009D9DF0  74 1C                           je 0x1409d9e0e
009D9DF2  33 D2                           xor edx, edx
009D9DF4  48 8D 8C 24 20 01 00 00         lea rcx, [rsp + 0x120]
009D9DFC  E8 2F DF 83 FF                  call 0x140217d30
009D9E01  BA 4D 6D 56 6D                  mov edx, 0x6d566d4d
009D9E06  48 8B CF                        mov rcx, rdi
009D9E09  E8 D2 DA 91 FF                  call 0x1402f78e0
009D9E0E  41 F7 C7 F5 FF FF FF            test r15d, 0xfffffff5
009D9E15  75 59                           jne 0x1409d9e70
009D9E17  41 83 FF 02                     cmp r15d, 2
009D9E1B  74 53                           je 0x1409d9e70
009D9E1D  83 E3 FD                        and ebx, 0xfffffffd
009D9E20  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
009D9E24  0F 10 84 24 98 00 00 00         movups xmm0, xmmword ptr [rsp + 0x98]
009D9E2C  0F 11 06                        movups xmmword ptr [rsi], xmm0
009D9E2F  0F 10 8C 24 A8 00 00 00         movups xmm1, xmmword ptr [rsp + 0xa8]
009D9E37  0F 11 4E 10                     movups xmmword ptr [rsi + 0x10], xmm1
009D9E3B  0F 10 84 24 B8 00 00 00         movups xmm0, xmmword ptr [rsp + 0xb8]
009D9E43  0F 11 46 20                     movups xmmword ptr [rsi + 0x20], xmm0
009D9E47  83 CB 02                        or ebx, 2
009D9E4A  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
009D9E4E  4D 85 E4                        test r12, r12
009D9E51  74 08                           je 0x1409d9e5b
009D9E53  49 C7 04 24 30 00 00 00         mov qword ptr [r12], 0x30
009D9E5B  E9 DD 03 00 00                  jmp 0x1409da23d
009D9E60  F6 44 24 40 02                  test byte ptr [rsp + 0x40], 2
009D9E65  0F 84 DB 03 00 00               je 0x1409da246
009D9E6B  E9 CD 03 00 00                  jmp 0x1409da23d
009D9E70  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
009D9E78  48 85 DB                        test rbx, rbx
009D9E7B  75 0A                           jne 0x1409d9e87
009D9E7D  B8 41 01 00 C0                  mov eax, 0xc0000141
009D9E82  E9 BF 03 00 00                  jmp 0x1409da246
009D9E87  48 83 FB 01                     cmp rbx, 1
009D9E8B  75 0A                           jne 0x1409d9e97
009D9E8D  B8 98 00 00 C0                  mov eax, 0xc0000098
009D9E92  E9 AF 03 00 00                  jmp 0x1409da246
009D9E97  41 8B C6                        mov eax, r14d
009D9E9A  48 8B CB                        mov rcx, rbx
009D9E9D  49 3B C6                        cmp rax, r14
009D9EA0  73 14                           jae 0x1409d9eb6
009D9EA2  BA 4D 6D 53 63                  mov edx, 0x63536d4d
009D9EA7  E8 34 DA 91 FF                  call 0x1402f78e0
009D9EAC  B8 F3 00 00 C0                  mov eax, 0xc00000f3
009D9EB1  E9 90 03 00 00                  jmp 0x1409da246
009D9EB6  0F B6 44 24 44                  movzx eax, byte ptr [rsp + 0x44]
009D9EBB  88 44 24 20                     mov byte ptr [rsp + 0x20], al
009D9EBF  4C 8D 4C 24 50                  lea r9, [rsp + 0x50]
009D9EC4  45 8B C6                        mov r8d, r14d
009D9EC7  48 8B D6                        mov rdx, rsi
009D9ECA  E8 01 E0 EC FF                  call 0x1408a7ed0
009D9ECF  8B F8                           mov edi, eax
009D9ED1  BA 4D 6D 53 63                  mov edx, 0x63536d4d
009D9ED6  48 8B CB                        mov rcx, rbx
009D9ED9  E8 02 DA 91 FF                  call 0x1402f78e0
009D9EDE  4D 85 E4                        test r12, r12
009D9EE1  74 0C                           je 0x1409d9eef
009D9EE3  8B 4C 24 50                     mov ecx, dword ptr [rsp + 0x50]
009D9EE7  49 89 0C 24                     mov qword ptr [r12], rcx
009D9EEB  EB 02                           jmp 0x1409d9eef
009D9EED  8B F8                           mov edi, eax
009D9EEF  8B C7                           mov eax, edi
009D9EF1  E9 50 03 00 00                  jmp 0x1409da246
009D9EF6  45 33 C0                        xor r8d, r8d
009D9EF9  41 8B F8                        mov edi, r8d
009D9EFC  44 89 44 24 54                  mov dword ptr [rsp + 0x54], r8d
009D9F01  41 0F B6 55 21                  movzx edx, byte ptr [r13 + 0x21]
009D9F06  48 C1 E2 20                     shl rdx, 0x20
009D9F0A  41 8B 45 1C                     mov eax, dword ptr [r13 + 0x1c]
009D9F0E  48 0B D0                        or rdx, rax
009D9F11  41 0F B6 4D 20                  movzx ecx, byte ptr [r13 + 0x20]
009D9F16  48 C1 E1 20                     shl rcx, 0x20
009D9F1A  41 8B 45 18                     mov eax, dword ptr [r13 + 0x18]
009D9F1E  48 0B C8                        or rcx, rax
009D9F21  48 2B D1                        sub rdx, rcx
009D9F24  48 FF C2                        inc rdx
009D9F27  48 C1 E2 0C                     shl rdx, 0xc
009D9F2B  48 89 94 24 80 00 00 00         mov qword ptr [rsp + 0x80], rdx
009D9F33  41 8B 4D 34                     mov ecx, dword ptr [r13 + 0x34]
009D9F37  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
009D9F3C  0F B6 50 22                     movzx edx, byte ptr [rax + 0x22]
009D9F40  48 C1 E2 20                     shl rdx, 0x20
009D9F44  48 0B D1                        or rdx, rcx
009D9F47  49 3B D1                        cmp rdx, r9
009D9F4A  72 07                           jb 0x1409d9f53
009D9F4C  4C 89 44 24 68                  mov qword ptr [rsp + 0x68], r8
009D9F51  EB 1E                           jmp 0x1409d9f71
009D9F53  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
009D9F58  8B 48 34                        mov ecx, dword ptr [rax + 0x34]
009D9F5B  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
009D9F60  44 0F B6 48 22                  movzx r9d, byte ptr [rax + 0x22]
009D9F65  49 C1 E1 20                     shl r9, 0x20
009D9F69  4C 0B C9                        or r9, rcx
009D9F6C  4C 89 4C 24 68                  mov qword ptr [rsp + 0x68], r9
009D9F71  4C 8B 6C 24 58                  mov r13, qword ptr [rsp + 0x58]
009D9F76  49 8B CD                        mov rcx, r13
009D9F79  E8 62 51 A5 FF                  call 0x14042f0e0
009D9F7E  48 89 84 24 88 00 00 00         mov qword ptr [rsp + 0x88], rax
009D9F86  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
009D9F8B  E8 80 9B A6 FF                  call 0x140443b10
009D9F90  4C 8B D8                        mov r11, rax
009D9F93  4D 8B D0                        mov r10, r8
009D9F96  41 8B 4D 30                     mov ecx, dword ptr [r13 + 0x30]
009D9F9A  0F BA E1 15                     bt ecx, 0x15
009D9F9E  73 75                           jae 0x1409da015
009D9FA0  8B 5C 24 40                     mov ebx, dword ptr [rsp + 0x40]
009D9FA4  F6 C3 10                        test bl, 0x10
009D9FA7  74 20                           je 0x1409d9fc9
009D9FA9  49 8B CD                        mov rcx, r13
009D9FAC  E8 37 F5 8C FF                  call 0x1402a94e8
009D9FB1  4C 8B D8                        mov r11, rax
009D9FB4  49 8B CD                        mov rcx, r13
009D9FB7  E8 3C B9 0F 00                  call 0x140ad58f8
009D9FBC  48 89 84 24 88 00 00 00         mov qword ptr [rsp + 0x88], rax
009D9FC4  45 33 C0                        xor r8d, r8d
009D9FC7  EB 69                           jmp 0x1409da032
009D9FC9  0F BA E1 17                     bt ecx, 0x17
009D9FCD  72 0E                           jb 0x1409d9fdd
009D9FCF  81 E1 00 00 18 00               and ecx, 0x180000
009D9FD5  81 F9 00 00 10 00               cmp ecx, 0x100000
009D9FDB  72 55                           jb 0x1409da032
009D9FDD  BA 10 00 00 00                  mov edx, 0x10
009D9FE2  49 8B CD                        mov rcx, r13
009D9FE5  E8 22 DA 8C FF                  call 0x1402a7a0c
009D9FEA  48 85 C0                        test rax, rax
009D9FED  74 43                           je 0x1409da032
009D9FEF  4C 8B 50 18                     mov r10, qword ptr [rax + 0x18]
009D9FF3  4D 85 D2                        test r10, r10
009D9FF6  74 3A                           je 0x1409da032
009D9FF8  4D 8B 1A                        mov r11, qword ptr [r10]
009D9FFB  49 8B CA                        mov rcx, r10
009D9FFE  E8 BD 06 9E FF                  call 0x1403ba6c0
009DA003  84 C0                           test al, al
009DA005  75 2B                           jne 0x1409da032
009DA007  BF A0 04 00 C0                  mov edi, 0xc00004a0
009DA00C  89 7C 24 54                     mov dword ptr [rsp + 0x54], edi
009DA010  4D 8B D0                        mov r10, r8
009DA013  EB 1D                           jmp 0x1409da032
009DA015  49 8B 45 48                     mov rax, qword ptr [r13 + 0x48]
009DA019  48 85 C0                        test rax, rax
009DA01C  74 10                           je 0x1409da02e
009DA01E  48 8B 08                        mov rcx, qword ptr [rax]
009DA021  48 85 C9                        test rcx, rcx
009DA024  74 08                           je 0x1409da02e
009DA026  E8 35 45 A6 FF                  call 0x14043e560
009DA02B  4C 8B D8                        mov r11, rax
009DA02E  8B 5C 24 40                     mov ebx, dword ptr [rsp + 0x40]
009DA032  85 FF                           test edi, edi
009DA034  78 0A                           js 0x1409da040
009DA036  41 0F B7 03                     movzx eax, word ptr [r11]
009DA03A  89 44 24 78                     mov dword ptr [rsp + 0x78], eax
009DA03E  EB 05                           jmp 0x1409da045
009DA040  44 89 44 24 78                  mov dword ptr [rsp + 0x78], r8d
009DA045  4D 85 D2                        test r10, r10
009DA048  74 08                           je 0x1409da052
009DA04A  49 8B CA                        mov rcx, r10
009DA04D  E8 1E 8E 96 FF                  call 0x140342e70
009DA052  41 8B 7D 30                     mov edi, dword ptr [r13 + 0x30]
009DA056  C1 EF 0C                        shr edi, 0xc
009DA059  83 E7 7F                        and edi, 0x7f
009DA05C  49 8B CD                        mov rcx, r13
009DA05F  E8 AC 4E 8D FF                  call 0x1402aef10
009DA064  F6 C3 01                        test bl, 1
009DA067  74 1E                           je 0x1409da087
009DA069  33 D2                           xor edx, edx
009DA06B  48 8D 8C 24 20 01 00 00         lea rcx, [rsp + 0x120]
009DA073  E8 B8 DC 83 FF                  call 0x140217d30
009DA078  BA 4D 6D 56 6D                  mov edx, 0x6d566d4d
009DA07D  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
009DA082  E8 59 D8 91 FF                  call 0x1402f78e0
009DA087  8B 44 24 54                     mov eax, dword ptr [rsp + 0x54]
009DA08B  85 C0                           test eax, eax
009DA08D  0F 88 B3 01 00 00               js 0x1409da246
009DA093  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
009DA098  48 C1 E1 0C                     shl rcx, 0xc
009DA09C  48 89 4C 24 68                  mov qword ptr [rsp + 0x68], rcx
009DA0A1  83 E3 FD                        and ebx, 0xfffffffd
009DA0A4  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
009DA0A8  48 8B 84 24 A0 00 00 00         mov rax, qword ptr [rsp + 0xa0]
009DA0B0  48 89 06                        mov qword ptr [rsi], rax
009DA0B3  8B 84 24 A8 00 00 00            mov eax, dword ptr [rsp + 0xa8]
009DA0BA  89 46 08                        mov dword ptr [rsi + 8], eax
009DA0BD  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
009DA0C5  48 89 46 10                     mov qword ptr [rsi + 0x10], rax
009DA0C9  83 7C 24 48 07                  cmp dword ptr [rsp + 0x48], 7
009DA0CE  0F 85 ED 00 00 00               jne 0x1409da1c1
009DA0D4  33 C0                           xor eax, eax
009DA0D6  89 46 0C                        mov dword ptr [rsi + 0xc], eax
009DA0D9  8B 8C 24 C0 00 00 00            mov ecx, dword ptr [rsp + 0xc0]
009DA0E0  81 F9 00 00 02 00               cmp ecx, 0x20000
009DA0E6  75 06                           jne 0x1409da0ee
009DA0E8  44 89 7E 0C                     mov dword ptr [rsi + 0xc], r15d
009DA0EC  EB 5A                           jmp 0x1409da148
009DA0EE  F6 C3 08                        test bl, 8
009DA0F1  74 0F                           je 0x1409da102
009DA0F3  C7 46 0C 10 00 00 00            mov dword ptr [rsi + 0xc], 0x10
009DA0FA  41 BF 10 00 00 00               mov r15d, 0x10
009DA100  EB 46                           jmp 0x1409da148
009DA102  81 F9 00 00 04 00               cmp ecx, 0x40000
009DA108  75 0F                           jne 0x1409da119
009DA10A  C7 46 0C 02 00 00 00            mov dword ptr [rsi + 0xc], 2
009DA111  41 BF 02 00 00 00               mov r15d, 2
009DA117  EB 2F                           jmp 0x1409da148
009DA119  81 F9 00 00 00 01               cmp ecx, 0x1000000
009DA11F  75 0F                           jne 0x1409da130
009DA121  C7 46 0C 04 00 00 00            mov dword ptr [rsi + 0xc], 4
009DA128  41 BF 04 00 00 00               mov r15d, 4
009DA12E  EB 18                           jmp 0x1409da148
009DA130  44 8B F8                        mov r15d, eax
009DA133  81 F9 00 00 00 08               cmp ecx, 0x8000000
009DA139  75 0D                           jne 0x1409da148
009DA13B  C7 46 0C 08 00 00 00            mov dword ptr [rsi + 0xc], 8
009DA142  41 BF 08 00 00 00               mov r15d, 8
009DA148  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009DA150  48 83 F8 10                     cmp rax, 0x10
009DA154  75 07                           jne 0x1409da15d
009DA156  41 0F BA EF 07                  bts r15d, 7
009DA15B  EB 1C                           jmp 0x1409da179
009DA15D  48 3D 00 02 00 00               cmp rax, 0x200
009DA163  75 07                           jne 0x1409da16c
009DA165  41 0F BA EF 0B                  bts r15d, 0xb
009DA16A  EB 0D                           jmp 0x1409da179
009DA16C  48 3D 00 00 04 00               cmp rax, 0x40000
009DA172  75 09                           jne 0x1409da17d
009DA174  41 0F BA EF 0C                  bts r15d, 0xc
009DA179  44 89 7E 0C                     mov dword ptr [rsi + 0xc], r15d
009DA17D  8B C3                           mov eax, ebx
009DA17F  83 E0 20                        and eax, 0x20
009DA182  C1 E0 05                        shl eax, 5
009DA185  41 0B C7                        or eax, r15d
009DA188  89 46 0C                        mov dword ptr [rsi + 0xc], eax
009DA18B  8B CB                           mov ecx, ebx
009DA18D  83 E1 10                        and ecx, 0x10
009DA190  C1 E1 05                        shl ecx, 5
009DA193  0B C8                           or ecx, eax
009DA195  89 4E 0C                        mov dword ptr [rsi + 0xc], ecx
009DA198  8B C3                           mov eax, ebx
009DA19A  83 E0 04                        and eax, 4
009DA19D  C1 E0 03                        shl eax, 3
009DA1A0  0B C1                           or eax, ecx
009DA1A2  89 46 0C                        mov dword ptr [rsi + 0xc], eax
009DA1A5  8B CB                           mov ecx, ebx
009DA1A7  83 E1 40                        and ecx, 0x40
009DA1AA  0B C8                           or ecx, eax
009DA1AC  89 4E 0C                        mov dword ptr [rsi + 0xc], ecx
009DA1AF  8B C3                           mov eax, ebx
009DA1B1  25 80 00 00 00                  and eax, 0x80
009DA1B6  03 C0                           add eax, eax
009DA1B8  0B C1                           or eax, ecx
009DA1BA  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
009DA1BF  EB 07                           jmp 0x1409da1c8
009DA1C1  8B 84 24 C0 00 00 00            mov eax, dword ptr [rsp + 0xc0]
009DA1C8  89 46 0C                        mov dword ptr [rsi + 0xc], eax
009DA1CB  B8 18 00 00 00                  mov eax, 0x18
009DA1D0  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
009DA1D4  49 83 FE 20                     cmp r14, 0x20
009DA1D8  72 0D                           jb 0x1409da1e7
009DA1DA  48 89 4E 18                     mov qword ptr [rsi + 0x18], rcx
009DA1DE  B8 20 00 00 00                  mov eax, 0x20
009DA1E3  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
009DA1E7  49 83 FE 28                     cmp r14, 0x28
009DA1EB  72 12                           jb 0x1409da1ff
009DA1ED  0F B7 44 24 78                  movzx eax, word ptr [rsp + 0x78]
009DA1F2  48 89 46 20                     mov qword ptr [rsi + 0x20], rax
009DA1F6  B8 28 00 00 00                  mov eax, 0x28
009DA1FB  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
009DA1FF  49 83 FE 30                     cmp r14, 0x30
009DA203  72 1F                           jb 0x1409da224
009DA205  85 FF                           test edi, edi
009DA207  75 07                           jne 0x1409da210
009DA209  B8 FF FF FF FF                  mov eax, 0xffffffff
009DA20E  EB 03                           jmp 0x1409da213
009DA210  8D 47 FF                        lea eax, [rdi - 1]
009DA213  48 89 46 28                     mov qword ptr [rsi + 0x28], rax
009DA217  C7 44 24 50 30 00 00 00         mov dword ptr [rsp + 0x50], 0x30
009DA21F  B8 30 00 00 00                  mov eax, 0x30
009DA224  83 CB 02                        or ebx, 2
009DA227  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
009DA22B  4D 85 E4                        test r12, r12
009DA22E  74 04                           je 0x1409da234
009DA230  49 89 04 24                     mov qword ptr [r12], rax
009DA234  EB 07                           jmp 0x1409da23d
009DA236  F6 44 24 40 02                  test byte ptr [rsp + 0x40], 2
009DA23B  74 09                           je 0x1409da246
009DA23D  33 C0                           xor eax, eax
009DA23F  EB 05                           jmp 0x1409da246
009DA241  B8 03 00 00 C0                  mov eax, 0xc0000003
009DA246  48 8B 8C 24 50 01 00 00         mov rcx, qword ptr [rsp + 0x150]
009DA24E  48 33 CC                        xor rcx, rsp
009DA251  E8 EA 23 CD FF                  call 0x1406ac640
009DA256  48 81 C4 60 01 00 00            add rsp, 0x160
009DA25D  41 5F                           pop r15
009DA25F  41 5E                           pop r14
009DA261  41 5D                           pop r13
009DA263  41 5C                           pop r12
009DA265  5F                              pop rdi
009DA266  5E                              pop rsi
009DA267  5B                              pop rbx
009DA268  C3                              ret
009DA269  CC                              int3
009DA26A  66 90                           nop
009DA26C  78 93                           js 0x1409da201
009DA26E  9D                              popfq
009DA26F  00 8F 93 9D 00 28               add byte ptr [rdi + 0x28009d93], cl
009DA275  94                              xchg esp, eax
009DA276  9D                              popfq
009DA277  00 CC                           add ah, cl
009DA279  93                              xchg ebx, eax
009DA27A  9D                              popfq
009DA27B  00 AF 93 9D 00 F0               add byte ptr [rdi - 0xfff626d], ch
009DA281  93                              xchg ebx, eax
009DA282  9D                              popfq
009DA283  00 CC                           add ah, cl
009DA285  93                              xchg ebx, eax
009DA286  9D                              popfq
009DA287  00 E0                           add al, ah
009DA289  93                              xchg ebx, eax
009DA28A  9D                              popfq
009DA28B  00 78 93                        add byte ptr [rax - 0x6d], bh
009DA28E  9D                              popfq
009DA28F  00 41 A2                        add byte ptr [rcx - 0x5e], al
009DA292  9D                              popfq
009DA293  00 41 A2                        add byte ptr [rcx - 0x5e], al
009DA296  9D                              popfq
009DA297  00 00                           add byte ptr [rax], al
009DA299  94                              xchg esp, eax
009DA29A  9D                              popfq
009DA29B  00 23                           add byte ptr [rbx], ah
009DA29D  94                              xchg esp, eax
009DA29E  9D                              popfq
009DA29F  00 19                           add byte ptr [rcx], bl
009DA2A1  94                              xchg esp, eax
009DA2A2  9D                              popfq
009DA2A3  00 56 94                        add byte ptr [rsi - 0x6c], dl
009DA2A6  9D                              popfq
009DA2A7  00                              .byte 0x00
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MmQueryVirtualMemory(__int64 a1, __int64 a2, int a3, __int64 a4, __int64 a5, __int64 a6)
{
    __int64 result;
    __int64 v_r15;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned int v_stack_m144;
    unsigned int v_stack_m148;
    unsigned int v_stack_m150;
    unsigned __int8 v_stack_m154;
    unsigned int v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned int v_stack_m178;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned int v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned int v_stack_mD4;
    unsigned int v_stack_mD8;
    unsigned int v_stack_mDC;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int16 v_stack_mEC;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p28;
    unsigned int v_stack_p38;

    v_rsp = (v_rsp) - (352);
    result = (*(unsigned __int64 *)(v_rip + 4396196)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m150 = (unsigned int)((int)(a3));
    v_stack_m108 = a2;
    v_stack_m128 = a1;
    v_r15 = 0;
    v_stack_m148 = 0;
    v_stack_m138 = 0;
    v_stack_m140 = 0;
    *(unsigned __int64 *)(v_rsp - 184) = 0;
    v_stack_m100 = v_xmm0;
    v_stack_mF0 = v_xmm0;
    v_stack_mE0 = v_xmm0;
    result = 0;
    v_stack_mD0 = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 192) = 0;
    *(unsigned __int64 *)(v_rsp - 120) = v_xmm1;
    *(unsigned __int64 *)(v_rsp - 104) = v_xmm1;
    *(unsigned __int64 *)(v_rsp - 88) = v_xmm1;
    v_stack_m158 = 0;
    v_stack_m110 = 0;
    v_stack_m118 = 0;
    *(unsigned __int64 *)(v_rsp - 176) = 0;
    v_stack_m120 = *(unsigned __int64 *)(gs_base + (0 + 392));
    v_stack_m154 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    if (((unsigned int)((int)(a3))) > 14) goto loc_009DA241;
    result = ((unsigned int)(*(unsigned int *)(v_rip - 10326887 + (int)(a3) * 4 + 10330732))) + (v_rip - 10326887);
loc_009DA241:
loc_009DA246:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562), v_rip - 10326887, a4);
    v_rsp = (v_rsp) + (352);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MmQueryVirtualMemory(int64_t Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4, uint64_t Arg5, int64_t Arg6)
{
    int64_t result;
    int64_t local_r15;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint32_t v_stack_m144;
    uint32_t v_stack_m148;
    uint32_t v_stack_m150;
    uint8_t v_stack_m154;
    uint32_t v_stack_m158;
    uint64_t v_stack_m160;
    uint64_t v_stack_m168;
    uint64_t v_stack_m170;
    uint32_t v_stack_m178;
    uint64_t v_stack_m48;
    uint64_t v_stack_m78;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint32_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint32_t v_stack_mD4;
    uint32_t v_stack_mD8;
    uint32_t v_stack_mDC;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint16_t v_stack_mEC;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p28;
    uint32_t v_stack_p38;

    local_rsp = (local_rsp) - (352);
    result = (*(uint64_t *)(v_rip + 0x4314A4)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m150 = (uint32_t)((int32_t)(Arg3));
    v_stack_m108 = Arg2;
    v_stack_m128 = Arg1;
    local_r15 = 0;
    v_stack_m148 = 0;
    v_stack_m138 = 0;
    v_stack_m140 = 0;
    *(uint64_t *)(local_rsp - 0xB8) = 0;
    v_stack_m100 = v_xmm0;
    v_stack_mF0 = v_xmm0;
    v_stack_mE0 = v_xmm0;
    result = 0;
    v_stack_mD0 = v_xmm0;
    *(uint64_t *)(local_rsp - 0xC0) = 0;
    *(uint64_t *)(local_rsp - 0x78) = v_xmm1;
    *(uint64_t *)(local_rsp - 0x68) = v_xmm1;
    *(uint64_t *)(local_rsp - 0x58) = v_xmm1;
    v_stack_m158 = 0;
    v_stack_m110 = 0;
    v_stack_m118 = 0;
    *(uint64_t *)(local_rsp - 0xB0) = 0;
    v_stack_m120 = *(uint64_t *)(gs_base + (0 + 0x188));
    v_stack_m154 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    if (((uint32_t)((int32_t)(Arg3))) > 14) goto loc_009DA241;
    result = ((uint32_t)(*(uint32_t *)(v_rip - 0x9D9367 + (int32_t)(Arg3) * 4 + 0x9DA26C))) + (v_rip - 10326887);
loc_009DA241:
loc_009DA246:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232), v_rip - 10326887, Arg4);
    local_rsp = (local_rsp) + (352);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009D9280&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
