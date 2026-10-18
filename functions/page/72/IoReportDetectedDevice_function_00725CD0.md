# IoReportDetectedDevice

- RVA: `0x00725CD0`–`0x0072676D` (길이 `2,717` bytes)
- VA: `0x0000000140725CD0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C8308`
- 디코드: `689`개 명령, `2,717/2,717` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **77**; 고유 호출 대상: **54**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **11**

### Outgoing calls
- `0x00725E17` → [IopGetRootDeviceId](IopGetRootDeviceId_function_00726BD4.md) (function, `0x00726BD4`)
- `0x00725E28` → [PiPnpRtlBeginOperation](../8E/PiPnpRtlBeginOperation_function_008E033C.md) (function, `0x008E033C`)
- `0x00725E3E` → [PpDevNodeLockTree](../A1/PpDevNodeLockTree_function_00A19310.md) (function, `0x00A19310`)
- `0x00725E63` → [IopDuplicateDetection](IopDuplicateDetection_function_0072E4AC.md) (function, `0x0072E4AC`)
- `0x00725EA8` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)
- `0x00725ECC` → [RtlAppendUnicodeToString](../../text/40/RtlAppendUnicodeToString_function_0040F990.md) (function, `0x0040F990`)
- `0x00725F2C` → [RtlStringCchPrintfExW](../../text/42/RtlStringCchPrintfExW_function_0042B390.md) (function, `0x0042B390`)
- `0x00725F8C` → [CmCreateDevice](../8F/CmCreateDevice_function_008FFABC.md) (function, `0x008FFABC`)
- `0x00725FC5` → [IopIsReportedAlready](IopIsReportedAlready_function_00726C6C.md) (function, `0x00726C6C`)
- `0x00725FD3` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x00725FF6` → [PnpDeviceObjectFromDeviceInstanceWithTag](../8E/PnpDeviceObjectFromDeviceInstanceWithTag_function_008E7490.md) (function, `0x008E7490`)
- `0x00726023` → [ZwDeleteKey](../../text/6A/ZwDeleteKey_function_006AEC50.md) (function, `0x006AEC50`)
- `0x00726031` → [ZwDeleteKey](../../text/6A/ZwDeleteKey_function_006AEC50.md) (function, `0x006AEC50`)
- `0x00726040` → [ZwDeleteKey](../../text/6A/ZwDeleteKey_function_006AEC50.md) (function, `0x006AEC50`)
- `0x00726049` → [PnpCleanupDeviceRegistryValues](../A0/PnpCleanupDeviceRegistryValues_function_00A0797C.md) (function, `0x00A0797C`)
- `0x00726051` → [PpDevNodeRemoveFromTree](../../text/4A/PpDevNodeRemoveFromTree_function_004AD5A0.md) (function, `0x004AD5A0`)
- `0x0072605A` → [IoDeleteDevice](../../text/26/IoDeleteDevice_function_0026FE90.md) (function, `0x0026FE90`)
- `0x00726063` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x0072606F` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00726074` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x0072607E` → [PpDevNodeUnlockTree](../A2/PpDevNodeUnlockTree_function_00A21290.md) (function, `0x00A21290`)
- `0x0072608C` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x0072609A` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x007260A9` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x007260B7` → [PiPnpRtlEndOperation](../8E/PiPnpRtlEndOperation_function_008E0518.md) (function, `0x008E0518`)
- `0x007260C8` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00726104` → [IopCreateRootEnumeratedDeviceObject](../73/IopCreateRootEnumeratedDeviceObject_function_00737D1C.md) (function, `0x00737D1C`)
- `0x0072612B` → [PipAllocateDeviceNode](../A9/PipAllocateDeviceNode_function_00A9C8F8.md) (function, `0x00A9C8F8`)
- `0x00726163` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00726182` → [PipSetDevNodeProblem](../8F/PipSetDevNodeProblem_function_008FDE0C.md) (function, `0x008FDE0C`)
- `0x0072619E` → [RtlUpcaseUnicodeString](../96/RtlUpcaseUnicodeString_function_00960780.md) (function, `0x00960780`)
- `0x007261B9` → [PnpAllocateDeviceInstancePath](PnpAllocateDeviceInstancePath_function_0072DC30.md) (function, `0x0072DC30`)
- `0x007261D0` → [RtlUpcaseUnicodeString](../96/RtlUpcaseUnicodeString_function_00960780.md) (function, `0x00960780`)
- `0x007261E6` → [PipSetDevNodeProblem](../8F/PipSetDevNodeProblem_function_008FDE0C.md) (function, `0x008FDE0C`)
- `0x0072623B` → [CmSetDeviceRegProp](../8F/CmSetDeviceRegProp_function_008FD68C.md) (function, `0x008FD68C`)
- `0x00726299` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x007262B0` → [PnpUnicodeStringToWstr](../9D/PnpUnicodeStringToWstr_function_009D90C0.md) (function, `0x009D90C0`)
- `0x007262CA` → [RtlStringCbLengthW](../../text/45/RtlStringCbLengthW_function_004575EC.md) (function, `0x004575EC`)
- `0x007262DD` → [PnpUnicodeStringToWstrFree](../8F/PnpUnicodeStringToWstrFree_function_008F59F0.md) (function, `0x008F59F0`)
- `0x0072631F` → [CmSetDeviceRegProp](../8F/CmSetDeviceRegProp_function_008FD68C.md) (function, `0x008FD68C`)
- `0x0072632C` → [PnpUnicodeStringToWstrFree](../8F/PnpUnicodeStringToWstrFree_function_008F59F0.md) (function, `0x008F59F0`)
- `0x00726370` → [_CmOpenDeviceRegKey](../8E/_CmOpenDeviceRegKey_function_008EE540.md) (function, `0x008EE540`)
- `0x0072638A` → [PnpSetRegistryDword](PnpSetRegistryDword_function_0072C2AC.md) (function, `0x0072C2AC`)
- `0x007263B6` → [PpDeviceRegistration](../A0/PpDeviceRegistration_function_00A079D4.md) (function, `0x00A079D4`)
- `0x007263E8` → [IopGetOriginalServiceName](IopGetOriginalServiceName_function_00726B48.md) (function, `0x00726B48`)
- `0x0072641F` → [IopCreateLegacyDeviceIds](../73/IopCreateLegacyDeviceIds_function_0073D3E4.md) (function, `0x0073D3E4`)
- `0x0072643C` → [PipSetDevNodeFlags](../8F/PipSetDevNodeFlags_function_008FC048.md) (function, `0x008FC048`)
- `0x0072645C` → [PipSetDevNodeState](../../text/47/PipSetDevNodeState_function_00470708.md) (function, `0x00470708`)
- `0x0072646B` → [PpDevNodeInsertIntoTree](../../text/4C/PpDevNodeInsertIntoTree_function_004CA274.md) (function, `0x004CA274`)
- `0x00726477` → [PnpMapDeviceObjectToDeviceInstance](../A9/PnpMapDeviceObjectToDeviceInstance_function_00A9D884.md) (function, `0x00A9D884`)
- `0x00726489` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (function, `0x0020FA20`)
- `0x00726496` → [IoDeleteDevice](../../text/26/IoDeleteDevice_function_0026FE90.md) (function, `0x0026FE90`)
- `0x007264AF` → [PipAreDriversLoaded](../../text/47/PipAreDriversLoaded_function_004708D4.md) (function, `0x004708D4`)
- `0x007264EE` → [PipClearDevNodeProblem](../A2/PipClearDevNodeProblem_function_00A27C8C.md) (function, `0x00A27C8C`)
- `0x00726509` → [PnpDeviceObjectToDeviceInstance](../8F/PnpDeviceObjectToDeviceInstance_function_008FD630.md) (function, `0x008FD630`)
- `0x00726557` → [_CmOpenDeviceRegKey](../8E/_CmOpenDeviceRegKey_function_008EE540.md) (function, `0x008EE540`)
- `0x00726581` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00726589` → [PnpDetermineResourceListSize](../8F/PnpDetermineResourceListSize_function_008FC6F8.md) (function, `0x008FC6F8`)
- `0x007265A7` → [ZwSetValueKey](../../text/6A/ZwSetValueKey_function_006ADCD0.md) (function, `0x006ADCD0`)
- `0x007265D1` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x007265F2` → [ZwSetValueKey](../../text/6A/ZwSetValueKey_function_006ADCD0.md) (function, `0x006ADCD0`)
- `0x00726612` → [PipSetDevNodeFlags](../8F/PipSetDevNodeFlags_function_008FC048.md) (function, `0x008FC048`)
- `0x00726623` → [PnpSetRegistryDword](PnpSetRegistryDword_function_0072C2AC.md) (function, `0x0072C2AC`)
- `0x0072662B` → [PnpDetermineResourceListSize](../8F/PnpDetermineResourceListSize_function_008FC6F8.md) (function, `0x008FC6F8`)
- `0x00726639` → [IopWriteAllocatedResourcesToRegistry](../AA/IopWriteAllocatedResourcesToRegistry_function_00AA54E4.md) (function, `0x00AA54E4`)
- `0x00726647` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00726675` → [PnpDetermineResourceListSize](../8F/PnpDetermineResourceListSize_function_008FC6F8.md) (function, `0x008FC6F8`)
- `0x0072668C` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x007266A6` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x007266D1` → [IoReportResourceUsageInternal](IoReportResourceUsageInternal_function_0072A398.md) (function, `0x0072A398`)
- `0x007266DE` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007266F1` → [PipIsDevNodeDNStarted](../../text/47/PipIsDevNodeDNStarted_function_00470870.md) (function, `0x00470870`)
- `0x00726703` → [PipSetDevNodeProblem](../8F/PipSetDevNodeProblem_function_008FDE0C.md) (function, `0x008FDE0C`)
- `0x00726717` → [PipSetDevNodeFlags](../8F/PipSetDevNodeFlags_function_008FC048.md) (function, `0x008FC048`)
- `0x00726737` → [IopDoDeferredSetInterfaceState](../94/IopDoDeferredSetInterfaceState_function_0094EF68.md) (function, `0x0094EF68`)
- `0x00726744` → [PipSetDevNodeState](../../text/47/PipSetDevNodeState_function_00470708.md) (function, `0x00470708`)
- `0x00726758` → [PipSetDevNodeFlags](../8F/PipSetDevNodeFlags_function_008FC048.md) (function, `0x008FC048`)

### Direct callers
- [HalpDriverEntry](../70/HalpDriverEntry_function_00708370.md) at `0x007083E4`

### Static image references
- `0x00725CEC` → RVA `0x00E0A740` (`.data`; read)
- `0x00725EA0` → RVA `0x00F8C600` (`.data`; read)
- `0x00725EC0` → RVA `0x00AFC990` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00725F08` → RVA `0x00AFD4D0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00725F70` → RVA `0x00E66398` (`.data`; read)
- `0x00726277` → RVA `0x00014428` (`.rdata`; read)
- `0x00726383` → RVA `0x00AFD4E0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00726441` → RVA `0x00F8C438` (`.data`; read)
- `0x0072656F` → RVA `0x00AFD500` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007265BF` → RVA `0x00AFD520` (` ?? ::NNGAKEGL::`string'`; read)
- `0x0072661C` → RVA `0x00AFD590` (` ?? ::NNGAKEGL::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **33**
  - `0x00725EA8` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (`PAGE` → `.text`)
  - `0x00725ECC` → [RtlAppendUnicodeToString](../../text/40/RtlAppendUnicodeToString_function_0040F990.md) (`PAGE` → `.text`)
  - `0x00725F2C` → [RtlStringCchPrintfExW](../../text/42/RtlStringCchPrintfExW_function_0042B390.md) (`PAGE` → `.text`)
  - `0x00725FD3` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x00726023` → [ZwDeleteKey](../../text/6A/ZwDeleteKey_function_006AEC50.md) (`PAGE` → `.text`)
  - `0x00726031` → [ZwDeleteKey](../../text/6A/ZwDeleteKey_function_006AEC50.md) (`PAGE` → `.text`)
  - `0x00726040` → [ZwDeleteKey](../../text/6A/ZwDeleteKey_function_006AEC50.md) (`PAGE` → `.text`)
  - `0x00726051` → [PpDevNodeRemoveFromTree](../../text/4A/PpDevNodeRemoveFromTree_function_004AD5A0.md) (`PAGE` → `.text`)
  - `0x0072605A` → [IoDeleteDevice](../../text/26/IoDeleteDevice_function_0026FE90.md) (`PAGE` → `.text`)
  - `0x00726063` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x0072606F` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00726074` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x0072608C` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x0072609A` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x007260A9` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x007260C8` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x00726163` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x007262CA` → [RtlStringCbLengthW](../../text/45/RtlStringCbLengthW_function_004575EC.md) (`PAGE` → `.text`)
  - `0x0072645C` → [PipSetDevNodeState](../../text/47/PipSetDevNodeState_function_00470708.md) (`PAGE` → `.text`)
  - `0x0072646B` → [PpDevNodeInsertIntoTree](../../text/4C/PpDevNodeInsertIntoTree_function_004CA274.md) (`PAGE` → `.text`)
  - `0x00726489` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (`PAGE` → `.text`)
  - `0x00726496` → [IoDeleteDevice](../../text/26/IoDeleteDevice_function_0026FE90.md) (`PAGE` → `.text`)
  - `0x007264AF` → [PipAreDriversLoaded](../../text/47/PipAreDriversLoaded_function_004708D4.md) (`PAGE` → `.text`)
  - `0x00726581` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x007265A7` → [ZwSetValueKey](../../text/6A/ZwSetValueKey_function_006ADCD0.md) (`PAGE` → `.text`)
  - `0x007265D1` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x007265F2` → [ZwSetValueKey](../../text/6A/ZwSetValueKey_function_006ADCD0.md) (`PAGE` → `.text`)
  - `0x00726647` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x0072668C` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x007266A6` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x007266DE` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x007266F1` → [PipIsDevNodeDNStarted](../../text/47/PipIsDevNodeDNStarted_function_00470870.md) (`PAGE` → `.text`)
  - `0x00726744` → [PipSetDevNodeState](../../text/47/PipSetDevNodeState_function_00470708.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00725CD0  40 55                           push rbp
00725CD2  53                              push rbx
00725CD3  56                              push rsi
00725CD4  57                              push rdi
00725CD5  41 54                           push r12
00725CD7  41 55                           push r13
00725CD9  41 56                           push r14
00725CDB  41 57                           push r15
00725CDD  48 8D AC 24 48 FE FF FF         lea rbp, [rsp - 0x1b8]
00725CE5  48 81 EC B8 02 00 00            sub rsp, 0x2b8
00725CEC  48 8B 05 4D 4A 6E 00            mov rax, qword ptr [rip + 0x6e4a4d]
00725CF3  48 33 C4                        xor rax, rsp
00725CF6  48 89 85 A0 01 00 00            mov qword ptr [rbp + 0x1a0], rax
00725CFD  48 8B 85 28 02 00 00            mov rax, qword ptr [rbp + 0x228]
00725D04  33 DB                           xor ebx, ebx
00725D06  4C 8B 79 30                     mov r15, qword ptr [rcx + 0x30]
00725D0A  8B F2                           mov esi, edx
00725D0C  4C 8B B5 20 02 00 00            mov r14, qword ptr [rbp + 0x220]
00725D13  48 8D 55 10                     lea rdx, [rbp + 0x10]
00725D17  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
00725D1B  49 83 C7 18                     add r15, 0x18
00725D1F  48 8B 85 38 02 00 00            mov rax, qword ptr [rbp + 0x238]
00725D26  0F 57 C0                        xorps xmm0, xmm0
00725D29  48 89 45 08                     mov qword ptr [rbp + 8], rax
00725D2D  0F 57 C9                        xorps xmm1, xmm1
00725D30  45 8B E0                        mov r12d, r8d
00725D33  48 89 4D A8                     mov qword ptr [rbp - 0x58], rcx
00725D37  45 8B E9                        mov r13d, r9d
00725D3A  88 5C 24 51                     mov byte ptr [rsp + 0x51], bl
00725D3E  48 8B 00                        mov rax, qword ptr [rax]
00725D41  44 8D 43 02                     lea r8d, [rbx + 2]
00725D45  48 C7 44 24 68 00 00 90 01      mov qword ptr [rsp + 0x68], 0x1900000
00725D4E  8B FB                           mov edi, ebx
00725D50  48 89 5D C8                     mov qword ptr [rbp - 0x38], rbx
00725D54  89 5C 24 54                     mov dword ptr [rsp + 0x54], ebx
00725D58  48 89 5D D0                     mov qword ptr [rbp - 0x30], rbx
00725D5C  89 5D 80                        mov dword ptr [rbp - 0x80], ebx
00725D5F  48 89 5D 90                     mov qword ptr [rbp - 0x70], rbx
00725D63  88 5C 24 50                     mov byte ptr [rsp + 0x50], bl
00725D67  48 89 5C 24 78                  mov qword ptr [rsp + 0x78], rbx
00725D6C  89 5C 24 60                     mov dword ptr [rsp + 0x60], ebx
00725D70  48 89 5C 24 58                  mov qword ptr [rsp + 0x58], rbx
00725D75  48 89 54 24 70                  mov qword ptr [rsp + 0x70], rdx
00725D7A  48 89 5D 88                     mov qword ptr [rbp - 0x78], rbx
00725D7E  88 5C 24 53                     mov byte ptr [rsp + 0x53], bl
00725D82  48 89 5D 98                     mov qword ptr [rbp - 0x68], rbx
00725D86  48 89 5D E0                     mov qword ptr [rbp - 0x20], rbx
00725D8A  0F 11 45 E8                     movups xmmword ptr [rbp - 0x18], xmm0
00725D8E  0F 11 4D F8                     movups xmmword ptr [rbp - 8], xmm1
00725D92  48 85 C0                        test rax, rax
00725D95  74 1F                           je 0x140725db6
00725D97  48 8B 80 38 01 00 00            mov rax, qword ptr [rax + 0x138]
00725D9E  48 8B 78 28                     mov rdi, qword ptr [rax + 0x28]
00725DA2  48 89 7C 24 78                  mov qword ptr [rsp + 0x78], rdi
00725DA7  48 85 FF                        test rdi, rdi
00725DAA  75 78                           jne 0x140725e24
00725DAC  B8 F6 00 00 C0                  mov eax, 0xc00000f6
00725DB1  E9 08 03 00 00                  jmp 0x1407260be
00725DB6  8B 41 10                        mov eax, dword ptr [rcx + 0x10]
00725DB9  A8 04                           test al, 4
00725DBB  74 52                           je 0x140725e0f
00725DBD  41 0F B7 0F                     movzx ecx, word ptr [r15]
00725DC1  49 8B 57 08                     mov rdx, qword ptr [r15 + 8]
00725DC5  48 D1 E9                        shr rcx, 1
00725DC8  48 FF C9                        dec rcx
00725DCB  48 8D 0C 4A                     lea rcx, [rdx + rcx*2]
00725DCF  48 3B CA                        cmp rcx, rdx
00725DD2  74 31                           je 0x140725e05
00725DD4  66 83 39 5C                     cmp word ptr [rcx], 0x5c
00725DD8  74 05                           je 0x140725ddf
00725DDA  49 2B C8                        sub rcx, r8
00725DDD  EB F0                           jmp 0x140725dcf
00725DDF  49 03 C8                        add rcx, r8
00725DE2  48 89 4D F0                     mov qword ptr [rbp - 0x10], rcx
00725DE6  41 2B 4F 08                     sub ecx, dword ptr [r15 + 8]
00725DEA  41 0F B7 07                     movzx eax, word ptr [r15]
00725DEE  48 D1 F9                        sar rcx, 1
00725DF1  66 03 C9                        add cx, cx
00725DF4  66 2B C1                        sub ax, cx
00725DF7  48 8D 4D E8                     lea rcx, [rbp - 0x18]
00725DFB  66 89 45 E8                     mov word ptr [rbp - 0x18], ax
00725DFF  66 89 45 EA                     mov word ptr [rbp - 0x16], ax
00725E03  EB 0D                           jmp 0x140725e12
00725E05  B8 EF 00 00 C0                  mov eax, 0xc00000ef
00725E0A  E9 AF 02 00 00                  jmp 0x1407260be
00725E0F  49 8B CF                        mov rcx, r15
00725E12  48 8D 54 24 68                  lea rdx, [rsp + 0x68]
00725E17  E8 B8 0D 00 00                  call 0x140726bd4
00725E1C  85 C0                           test eax, eax
00725E1E  0F 88 9A 02 00 00               js 0x1407260be
00725E24  48 8D 4D E0                     lea rcx, [rbp - 0x20]
00725E28  E8 0F A5 1B 00                  call 0x1408e033c
00725E2D  8B D8                           mov ebx, eax
00725E2F  B8 01 00 00 00                  mov eax, 1
00725E34  85 DB                           test ebx, ebx
00725E36  0F 88 2C 02 00 00               js 0x140726068
00725E3C  8B C8                           mov ecx, eax
00725E3E  E8 CD 34 2F 00                  call 0x140a19310
00725E43  48 85 FF                        test rdi, rdi
00725E46  75 3D                           jne 0x140725e85
00725E48  4C 8B 4D A8                     mov r9, qword ptr [rbp - 0x58]
00725E4C  45 8B 49 10                     mov r9d, dword ptr [r9 + 0x10]
00725E50  41 F6 C1 04                     test r9b, 4
00725E54  75 2F                           jne 0x140725e85
00725E56  4C 8D 4C 24 78                  lea r9, [rsp + 0x78]
00725E5B  45 8B C5                        mov r8d, r13d
00725E5E  41 8B D4                        mov edx, r12d
00725E61  8B CE                           mov ecx, esi
00725E63  E8 44 86 00 00                  call 0x14072e4ac
00725E68  45 33 ED                        xor r13d, r13d
00725E6B  8D 57 01                        lea edx, [rdi + 1]
00725E6E  8B D8                           mov ebx, eax
00725E70  85 C0                           test eax, eax
00725E72  78 19                           js 0x140725e8d
00725E74  4C 39 6C 24 78                  cmp qword ptr [rsp + 0x78], r13
00725E79  41 8B C5                        mov eax, r13d
00725E7C  0F 45 C2                        cmovne eax, edx
00725E7F  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
00725E83  EB 08                           jmp 0x140725e8d
00725E85  BA 01 00 00 00                  mov edx, 1
00725E8A  45 33 ED                        xor r13d, r13d
00725E8D  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00725E96  83 C9 FF                        or ecx, 0xffffffff
00725E99  66 01 88 E4 01 00 00            add word ptr [rax + 0x1e4], cx
00725EA0  48 8D 0D 59 67 86 00            lea rcx, [rip + 0x866759]
00725EA7  90                              nop
00725EA8  E8 73 EF AE FF                  call 0x140214e20
00725EAD  48 8B 7C 24 78                  mov rdi, qword ptr [rsp + 0x78]
00725EB2  BE 13 00 00 00                  mov esi, 0x13
00725EB7  48 85 FF                        test rdi, rdi
00725EBA  0F 85 E5 05 00 00               jne 0x1407264a5
00725EC0  48 8D 15 C9 6A 3D 00            lea rdx, [rip + 0x3d6ac9]
00725EC7  48 8D 4C 24 68                  lea rcx, [rsp + 0x68]
00725ECC  E8 BF 9A CE FF                  call 0x14040f990
00725ED1  8B D8                           mov ebx, eax
00725ED3  85 C0                           test eax, eax
00725ED5  0F 88 8D 01 00 00               js 0x140726068
00725EDB  0F B7 4C 24 68                  movzx ecx, word ptr [rsp + 0x68]
00725EE0  BB 90 01 00 00                  mov ebx, 0x190
00725EE5  44 8B E3                        mov r12d, ebx
00725EE8  89 4D A0                        mov dword ptr [rbp - 0x60], ecx
00725EEB  4C 2B E1                        sub r12, rcx
00725EEE  8B C1                           mov eax, ecx
00725EF0  49 D1 EC                        shr r12, 1
00725EF3  48 D1 E8                        shr rax, 1
00725EF6  48 8D 44 45 10                  lea rax, [rbp + rax*2 + 0x10]
00725EFB  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
00725EFF  66 89 4C 24 68                  mov word ptr [rsp + 0x68], cx
00725F04  4C 8D 45 C0                     lea r8, [rbp - 0x40]
00725F08  48 8D 0D C1 75 3D 00            lea rcx, [rip + 0x3d75c1]
00725F0F  44 89 6C 24 30                  mov dword ptr [rsp + 0x30], r13d
00725F14  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
00725F19  45 33 C9                        xor r9d, r9d
00725F1C  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
00725F22  48 8B C8                        mov rcx, rax
00725F25  49 8B D4                        mov rdx, r12
00725F28  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
00725F2C  E8 5F 54 D0 FF                  call 0x14042b390
00725F31  0F B7 54 24 68                  movzx edx, word ptr [rsp + 0x68]
00725F36  48 8B 4D C0                     mov rcx, qword ptr [rbp - 0x40]
00725F3A  8B C2                           mov eax, edx
00725F3C  48 D1 E8                        shr rax, 1
00725F3F  48 03 C0                        add rax, rax
00725F42  48 2B C8                        sub rcx, rax
00725F45  48 8D 45 10                     lea rax, [rbp + 0x10]
00725F49  48 2B C8                        sub rcx, rax
00725F4C  48 D1 F9                        sar rcx, 1
00725F4F  83 F9 FF                        cmp ecx, -1
00725F52  75 07                           jne 0x140725f5b
00725F54  8B CB                           mov ecx, ebx
00725F56  66 2B CA                        sub cx, dx
00725F59  EB 03                           jmp 0x140725f5e
00725F5B  66 03 C9                        add cx, cx
00725F5E  83 64 24 28 00                  and dword ptr [rsp + 0x28], 0
00725F63  48 8D 44 24 50                  lea rax, [rsp + 0x50]
00725F68  66 03 D1                        add dx, cx
00725F6B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00725F70  48 8B 0D 21 04 74 00            mov rcx, qword ptr [rip + 0x740421]
00725F77  4C 8D 4C 24 58                  lea r9, [rsp + 0x58]
00725F7C  66 89 54 24 68                  mov word ptr [rsp + 0x68], dx
00725F81  41 B8 3F 00 0F 00               mov r8d, 0xf003f
00725F87  48 8B 54 24 70                  mov rdx, qword ptr [rsp + 0x70]
00725F8C  E8 2B 9B 1D 00                  call 0x1408ffabc
00725F91  8B D8                           mov ebx, eax
00725F93  33 C0                           xor eax, eax
00725F95  85 DB                           test ebx, ebx
00725F97  0F 88 4E 02 00 00               js 0x1407261eb
00725F9D  38 44 24 50                     cmp byte ptr [rsp + 0x50], al
00725FA1  0F 85 4D 01 00 00               jne 0x1407260f4
00725FA7  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
00725FAC  48 8D 4C 24 68                  lea rcx, [rsp + 0x68]
00725FB1  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
00725FB5  4D 8B CE                        mov r9, r14
00725FB8  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00725FBD  4D 8B C7                        mov r8, r15
00725FC0  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00725FC5  E8 A2 0C 00 00                  call 0x140726c6c
00725FCA  84 C0                           test al, al
00725FCC  75 1E                           jne 0x140725fec
00725FCE  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00725FD3  E8 D8 72 F8 FF                  call 0x1406ad2b0
00725FD8  8B 4D A0                        mov ecx, dword ptr [rbp - 0x60]
00725FDB  41 FF C5                        inc r13d
00725FDE  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
00725FE2  BB 90 01 00 00                  mov ebx, 0x190
00725FE7  E9 13 FF FF FF                  jmp 0x140725eff
00725FEC  BA 44 66 6C 74                  mov edx, 0x746c6644
00725FF1  48 8D 4C 24 68                  lea rcx, [rsp + 0x68]
00725FF6  E8 95 14 1C 00                  call 0x1408e7490
00725FFB  45 33 ED                        xor r13d, r13d
00725FFE  48 89 45 98                     mov qword ptr [rbp - 0x68], rax
00726002  48 85 C0                        test rax, rax
00726005  0F 85 D7 00 00 00               jne 0x1407260e2
0072600B  BB 01 00 00 C0                  mov ebx, 0xc0000001
00726010  41 8B FD                        mov edi, r13d
00726013  44 38 6C 24 50                  cmp byte ptr [rsp + 0x50], r13b
00726018  74 4E                           je 0x140726068
0072601A  48 8B 4D 88                     mov rcx, qword ptr [rbp - 0x78]
0072601E  48 85 C9                        test rcx, rcx
00726021  74 05                           je 0x140726028
00726023  E8 28 8C F8 FF                  call 0x1406aec50
00726028  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
0072602C  48 85 C9                        test rcx, rcx
0072602F  74 05                           je 0x140726036
00726031  E8 1A 8C F8 FF                  call 0x1406aec50
00726036  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
0072603B  48 85 C9                        test rcx, rcx
0072603E  74 05                           je 0x140726045
00726040  E8 0B 8C F8 FF                  call 0x1406aec50
00726045  48 8D 4F 28                     lea rcx, [rdi + 0x28]
00726049  E8 2E 19 2E 00                  call 0x140a0797c
0072604E  48 8B CF                        mov rcx, rdi
00726051  E8 4A 75 D8 FF                  call 0x1404ad5a0
00726056  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
0072605A  E8 31 9E B4 FF                  call 0x14026fe90
0072605F  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
00726063  E8 E8 32 BD FF                  call 0x1402f9350
00726068  48 8D 0D 91 65 86 00            lea rcx, [rip + 0x866591]
0072606F  E8 9C 99 B3 FF                  call 0x14025fa10
00726074  E8 37 78 B3 FF                  call 0x14025d8b0
00726079  B9 01 00 00 00                  mov ecx, 1
0072607E  E8 0D B2 2F 00                  call 0x140a21290
00726083  48 8B 4D 88                     mov rcx, qword ptr [rbp - 0x78]
00726087  48 85 C9                        test rcx, rcx
0072608A  74 05                           je 0x140726091
0072608C  E8 1F 72 F8 FF                  call 0x1406ad2b0
00726091  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
00726095  48 85 C9                        test rcx, rcx
00726098  74 05                           je 0x14072609f
0072609A  E8 11 72 F8 FF                  call 0x1406ad2b0
0072609F  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
007260A4  48 85 C9                        test rcx, rcx
007260A7  74 05                           je 0x1407260ae
007260A9  E8 02 72 F8 FF                  call 0x1406ad2b0
007260AE  48 8B 4D E0                     mov rcx, qword ptr [rbp - 0x20]
007260B2  48 85 C9                        test rcx, rcx
007260B5  74 05                           je 0x1407260bc
007260B7  E8 5C A4 1B 00                  call 0x1408e0518
007260BC  8B C3                           mov eax, ebx
007260BE  48 8B 8D A0 01 00 00            mov rcx, qword ptr [rbp + 0x1a0]
007260C5  48 33 CC                        xor rcx, rsp
007260C8  E8 73 65 F8 FF                  call 0x1406ac640
007260CD  48 81 C4 B8 02 00 00            add rsp, 0x2b8
007260D4  41 5F                           pop r15
007260D6  41 5E                           pop r14
007260D8  41 5D                           pop r13
007260DA  41 5C                           pop r12
007260DC  5F                              pop rdi
007260DD  5E                              pop rsi
007260DE  5B                              pop rbx
007260DF  5D                              pop rbp
007260E0  C3                              ret
007260E1  CC                              int3
007260E2  48 8B 80 38 01 00 00            mov rax, qword ptr [rax + 0x138]
007260E9  48 8B 78 28                     mov rdi, qword ptr [rax + 0x28]
007260ED  48 89 7C 24 78                  mov qword ptr [rsp + 0x78], rdi
007260F2  EB 03                           jmp 0x1407260f7
007260F4  45 33 ED                        xor r13d, r13d
007260F7  48 85 FF                        test rdi, rdi
007260FA  0F 85 A5 03 00 00               jne 0x1407264a5
00726100  48 8D 4D 98                     lea rcx, [rbp - 0x68]
00726104  E8 13 1C 01 00                  call 0x140737d1c
00726109  8B D8                           mov ebx, eax
0072610B  85 C0                           test eax, eax
0072610D  0F 88 00 FF FF FF               js 0x140726013
00726113  4C 8B 65 98                     mov r12, qword ptr [rbp - 0x68]
00726117  48 8D 54 24 78                  lea rdx, [rsp + 0x78]
0072611C  49 8B CC                        mov rcx, r12
0072611F  C6 44 24 53 01                  mov byte ptr [rsp + 0x53], 1
00726124  41 0F BA 6C 24 30 0C            bts dword ptr [r12 + 0x30], 0xc
0072612B  E8 C8 67 37 00                  call 0x140a9c8f8
00726130  48 8B 7C 24 78                  mov rdi, qword ptr [rsp + 0x78]
00726135  3D 6E 03 00 C0                  cmp eax, 0xc000036e
0072613A  0F 84 53 03 00 00               je 0x140726493
00726140  48 85 FF                        test rdi, rdi
00726143  0F 84 4A 03 00 00               je 0x140726493
00726149  48 8B 45 A8                     mov rax, qword ptr [rbp - 0x58]
0072614D  8B 40 10                        mov eax, dword ptr [rax + 0x10]
00726150  A8 04                           test al, 4
00726152  75 5A                           jne 0x1407261ae
00726154  41 0F B7 17                     movzx edx, word ptr [r15]
00726158  B9 00 01 00 00                  mov ecx, 0x100
0072615D  41 B8 50 6E 70 48               mov r8d, 0x48706e50
00726163  E8 88 BF 45 00                  call 0x140b820f0
00726168  48 89 47 40                     mov qword ptr [rdi + 0x40], rax
0072616C  48 85 C0                        test rax, rax
0072616F  75 1B                           jne 0x14072618c
00726171  41 B8 9A 00 00 C0               mov r8d, 0xc000009a
00726177  41 8B D8                        mov ebx, r8d
0072617A  BA 03 00 00 00                  mov edx, 3
0072617F  48 8B CF                        mov rcx, rdi
00726182  E8 85 7C 1D 00                  call 0x1408fde0c
00726187  E9 87 FE FF FF                  jmp 0x140726013
0072618C  41 0F B7 07                     movzx eax, word ptr [r15]
00726190  48 8D 4F 38                     lea rcx, [rdi + 0x38]
00726194  45 33 C0                        xor r8d, r8d
00726197  66 89 47 3A                     mov word ptr [rdi + 0x3a], ax
0072619B  49 8B D7                        mov rdx, r15
0072619E  E8 DD A5 23 00                  call 0x140960780
007261A3  8B D8                           mov ebx, eax
007261A5  85 C0                           test eax, eax
007261A7  79 05                           jns 0x1407261ae
007261A9  44 8B C0                        mov r8d, eax
007261AC  EB CC                           jmp 0x14072617a
007261AE  0F B7 54 24 68                  movzx edx, word ptr [rsp + 0x68]
007261B3  48 8B CF                        mov rcx, rdi
007261B6  83 C2 02                        add edx, 2
007261B9  E8 72 7A 00 00                  call 0x14072dc30
007261BE  8B D8                           mov ebx, eax
007261C0  85 C0                           test eax, eax
007261C2  78 E5                           js 0x1407261a9
007261C4  45 33 C0                        xor r8d, r8d
007261C7  48 8D 54 24 68                  lea rdx, [rsp + 0x68]
007261CC  48 8D 4F 28                     lea rcx, [rdi + 0x28]
007261D0  E8 AB A5 23 00                  call 0x140960780
007261D5  8B D8                           mov ebx, eax
007261D7  85 C0                           test eax, eax
007261D9  79 18                           jns 0x1407261f3
007261DB  44 8B C0                        mov r8d, eax
007261DE  BA 03 00 00 00                  mov edx, 3
007261E3  48 8B CF                        mov rcx, rdi
007261E6  E8 21 7C 1D 00                  call 0x1408fde0c
007261EB  45 33 ED                        xor r13d, r13d
007261EE  E9 20 FE FF FF                  jmp 0x140726013
007261F3  0F B7 4F 28                     movzx ecx, word ptr [rdi + 0x28]
007261F7  45 33 ED                        xor r13d, r13d
007261FA  48 8B 47 30                     mov rax, qword ptr [rdi + 0x30]
007261FE  48 D1 E9                        shr rcx, 1
00726201  44 89 6C 24 38                  mov dword ptr [rsp + 0x38], r13d
00726206  45 8D 4D 0B                     lea r9d, [r13 + 0xb]
0072620A  66 44 89 2C 48                  mov word ptr [rax + rcx*2], r13w
0072620F  41 8D 4D 04                     lea ecx, [r13 + 4]
00726213  4C 8B 44 24 58                  mov r8, qword ptr [rsp + 0x58]
00726218  48 8D 45 80                     lea rax, [rbp - 0x80]
0072621C  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
00726220  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00726225  89 4C 24 20                     mov dword ptr [rsp + 0x20], ecx
00726229  48 8B 0D 68 01 74 00            mov rcx, qword ptr [rip + 0x740168]
00726230  C7 45 80 20 00 00 00            mov dword ptr [rbp - 0x80], 0x20
00726237  48 8B 57 30                     mov rdx, qword ptr [rdi + 0x30]
0072623B  E8 4C 74 1D 00                  call 0x1408fd68c
00726240  8B D8                           mov ebx, eax
00726242  85 C0                           test eax, eax
00726244  79 0A                           jns 0x140726250
00726246  44 8B C0                        mov r8d, eax
00726249  8B D6                           mov edx, esi
0072624B  E9 2F FF FF FF                  jmp 0x14072617f
00726250  4C 8B 4C 24 58                  mov r9, qword ptr [rsp + 0x58]
00726255  48 8D 44 24 51                  lea rax, [rsp + 0x51]
0072625A  44 89 6C 24 48                  mov dword ptr [rsp + 0x48], r13d
0072625F  B9 01 00 00 00                  mov ecx, 1
00726264  89 4C 24 40                     mov dword ptr [rsp + 0x40], ecx
00726268  44 8B C1                        mov r8d, ecx
0072626B  48 8B 0D 26 01 74 00            mov rcx, qword ptr [rip + 0x740126]
00726272  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00726277  48 8D 05 AA E1 8E FF            lea rax, [rip - 0x711e56]
0072627E  C6 44 24 51 FF                  mov byte ptr [rsp + 0x51], 0xff
00726283  48 8B 57 30                     mov rdx, qword ptr [rdi + 0x30]
00726287  C7 44 24 30 11 00 00 00         mov dword ptr [rsp + 0x30], 0x11
0072628F  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00726294  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00726299  E8 4A 04 1D 00                  call 0x1408f66e8
0072629E  8B D8                           mov ebx, eax
007262A0  85 C0                           test eax, eax
007262A2  78 A2                           js 0x140726246
007262A4  4D 8B C7                        mov r8, r15
007262A7  48 8D 54 24 54                  lea rdx, [rsp + 0x54]
007262AC  48 8D 4D C8                     lea rcx, [rbp - 0x38]
007262B0  E8 0B 2E 2B 00                  call 0x1409d90c0
007262B5  8B D8                           mov ebx, eax
007262B7  85 C0                           test eax, eax
007262B9  78 8B                           js 0x140726246
007262BB  4C 8B 6D C8                     mov r13, qword ptr [rbp - 0x38]
007262BF  4C 8D 45 D0                     lea r8, [rbp - 0x30]
007262C3  8B 54 24 54                     mov edx, dword ptr [rsp + 0x54]
007262C7  49 8B CD                        mov rcx, r13
007262CA  E8 1D 13 D3 FF                  call 0x1404575ec
007262CF  33 C9                           xor ecx, ecx
007262D1  8B D8                           mov ebx, eax
007262D3  85 C0                           test eax, eax
007262D5  79 15                           jns 0x1407262ec
007262D7  49 8B D7                        mov rdx, r15
007262DA  49 8B CD                        mov rcx, r13
007262DD  E8 0E F7 1C 00                  call 0x1408f59f0
007262E2  44 8B C3                        mov r8d, ebx
007262E5  8B D6                           mov edx, esi
007262E7  E9 F7 FE FF FF                  jmp 0x1407261e3
007262EC  48 8B 45 D0                     mov rax, qword ptr [rbp - 0x30]
007262F0  41 B9 05 00 00 00               mov r9d, 5
007262F6  4C 8B 44 24 58                  mov r8, qword ptr [rsp + 0x58]
007262FB  48 83 C0 02                     add rax, 2
007262FF  48 8B 57 30                     mov rdx, qword ptr [rdi + 0x30]
00726303  89 4C 24 38                     mov dword ptr [rsp + 0x38], ecx
00726307  48 8B 0D 8A 00 74 00            mov rcx, qword ptr [rip + 0x74008a]
0072630E  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00726312  4C 89 6C 24 28                  mov qword ptr [rsp + 0x28], r13
00726317  C7 44 24 20 01 00 00 00         mov dword ptr [rsp + 0x20], 1
0072631F  E8 68 73 1D 00                  call 0x1408fd68c
00726324  49 8B D7                        mov rdx, r15
00726327  49 8B CD                        mov rcx, r13
0072632A  8B D8                           mov ebx, eax
0072632C  E8 BF F6 1C 00                  call 0x1408f59f0
00726331  45 33 ED                        xor r13d, r13d
00726334  85 DB                           test ebx, ebx
00726336  79 08                           jns 0x140726340
00726338  44 8B C3                        mov r8d, ebx
0072633B  E9 09 FF FF FF                  jmp 0x140726249
00726340  48 8B 0D 51 00 74 00            mov rcx, qword ptr [rip + 0x740051]
00726347  48 8D 45 90                     lea rax, [rbp - 0x70]
0072634B  4C 89 6C 24 38                  mov qword ptr [rsp + 0x38], r13
00726350  45 33 C9                        xor r9d, r9d
00726353  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00726358  44 8B C6                        mov r8d, esi
0072635B  4C 89 6D 90                     mov qword ptr [rbp - 0x70], r13
0072635F  48 8B 57 30                     mov rdx, qword ptr [rdi + 0x30]
00726363  C6 44 24 28 01                  mov byte ptr [rsp + 0x28], 1
00726368  C7 44 24 20 3F 00 0F 00         mov dword ptr [rsp + 0x20], 0xf003f
00726370  E8 CB 81 1C 00                  call 0x1408ee540
00726375  8B D8                           mov ebx, eax
00726377  85 C0                           test eax, eax
00726379  0F 88 C7 FE FF FF               js 0x140726246
0072637F  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
00726383  48 8D 15 56 71 3D 00            lea rdx, [rip + 0x3d7156]
0072638A  E8 1D 5F 00 00                  call 0x14072c2ac
0072638F  8B D8                           mov ebx, eax
00726391  85 C0                           test eax, eax
00726393  0F 88 AD FE FF FF               js 0x140726246
00726399  48 8B 5D A8                     mov rbx, qword ptr [rbp - 0x58]
0072639D  8B 43 10                        mov eax, dword ptr [rbx + 0x10]
007263A0  A8 04                           test al, 4
007263A2  75 17                           jne 0x1407263bb
007263A4  B8 01 00 00 00                  mov eax, 1
007263A9  48 8D 4C 24 68                  lea rcx, [rsp + 0x68]
007263AE  44 8A C8                        mov r9b, al
007263B1  8A D0                           mov dl, al
007263B3  45 33 C0                        xor r8d, r8d
007263B6  E8 19 16 2E 00                  call 0x140a079d4
007263BB  F6 43 10 04                     test byte ptr [rbx + 0x10], 4
007263BF  4C 8D 44 24 54                  lea r8, [rsp + 0x54]
007263C4  48 8D 5D E8                     lea rbx, [rbp - 0x18]
007263C8  4C 89 6C 24 70                  mov qword ptr [rsp + 0x70], r13
007263CD  49 0F 44 DF                     cmove rbx, r15
007263D1  44 89 6C 24 68                  mov dword ptr [rsp + 0x68], r13d
007263D6  41 BF 90 01 00 00               mov r15d, 0x190
007263DC  48 8D 55 10                     lea rdx, [rbp + 0x10]
007263E0  48 8B CB                        mov rcx, rbx
007263E3  44 89 7C 24 54                  mov dword ptr [rsp + 0x54], r15d
007263E8  E8 5B 07 00 00                  call 0x140726b48
007263ED  85 C0                           test eax, eax
007263EF  78 25                           js 0x140726416
007263F1  8B 44 24 54                     mov eax, dword ptr [rsp + 0x54]
007263F5  BA 02 00 00 00                  mov edx, 2
007263FA  3B C2                           cmp eax, edx
007263FC  76 18                           jbe 0x140726416
007263FE  48 8D 4D 10                     lea rcx, [rbp + 0x10]
00726402  66 44 89 7D FA                  mov word ptr [rbp - 6], r15w
00726407  66 2B C2                        sub ax, dx
0072640A  48 89 4D 00                     mov qword ptr [rbp], rcx
0072640E  66 89 45 F8                     mov word ptr [rbp - 8], ax
00726412  48 8D 5D F8                     lea rbx, [rbp - 8]
00726416  4D 8B C6                        mov r8, r14
00726419  48 8B D3                        mov rdx, rbx
0072641C  49 8B CC                        mov rcx, r12
0072641F  E8 C0 6F 01 00                  call 0x14073d3e4
00726424  8B D8                           mov ebx, eax
00726426  48 8B CF                        mov rcx, rdi
00726429  85 C0                           test eax, eax
0072642B  79 0A                           jns 0x140726437
0072642D  44 8B C0                        mov r8d, eax
00726430  8B D6                           mov edx, esi
00726432  E9 4B FD FF FF                  jmp 0x140726182
00726437  BA 11 00 00 00                  mov edx, 0x11
0072643C  E8 07 5C 1D 00                  call 0x1408fc048
00726441  48 8B 05 F0 5F 86 00            mov rax, qword ptr [rip + 0x865ff0]
00726448  BA 04 03 00 00                  mov edx, 0x304
0072644D  8B 88 94 02 00 00               mov ecx, dword ptr [rax + 0x294]
00726453  89 8F 94 02 00 00               mov dword ptr [rdi + 0x294], ecx
00726459  48 8B CF                        mov rcx, rdi
0072645C  E8 A7 A2 D4 FF                  call 0x140470708
00726461  48 8B 0D D0 5F 86 00            mov rcx, qword ptr [rip + 0x865fd0]
00726468  48 8B D7                        mov rdx, rdi
0072646B  E8 04 3E DA FF                  call 0x1404ca274
00726470  48 8D 57 28                     lea rdx, [rdi + 0x28]
00726474  49 8B CC                        mov rcx, r12
00726477  E8 08 74 37 00                  call 0x140a9d884
0072647C  8B D8                           mov ebx, eax
0072647E  85 C0                           test eax, eax
00726480  0F 88 23 FD FF FF               js 0x1407261a9
00726486  49 8B CC                        mov rcx, r12
00726489  E8 92 95 AE FF                  call 0x14020fa20
0072648E  E9 85 00 00 00                  jmp 0x140726518
00726493  49 8B CC                        mov rcx, r12
00726496  E8 F5 99 B4 FF                  call 0x14026fe90
0072649B  BB 9A 00 00 C0                  mov ebx, 0xc000009a
007264A0  E9 6E FB FF FF                  jmp 0x140726013
007264A5  44 39 6C 24 60                  cmp dword ptr [rsp + 0x60], r13d
007264AA  74 47                           je 0x1407264f3
007264AC  48 8B CF                        mov rcx, rdi
007264AF  E8 20 A4 D4 FF                  call 0x1404708d4
007264B4  85 C0                           test eax, eax
007264B6  0F 85 87 01 00 00               jne 0x140726643
007264BC  F7 87 8C 01 00 00 00 60 00 00   test dword ptr [rdi + 0x18c], 0x6000
007264C6  74 1D                           je 0x1407264e5
007264C8  8B 87 94 01 00 00               mov eax, dword ptr [rdi + 0x194]
007264CE  83 F8 1C                        cmp eax, 0x1c
007264D1  0F 87 6C 01 00 00               ja 0x140726643
007264D7  B9 02 00 04 10                  mov ecx, 0x10040002
007264DC  0F A3 C1                        bt ecx, eax
007264DF  0F 83 5E 01 00 00               jae 0x140726643
007264E5  4C 39 6D 98                     cmp qword ptr [rbp - 0x68], r13
007264E9  75 08                           jne 0x1407264f3
007264EB  48 8B CF                        mov rcx, rdi
007264EE  E8 99 17 30 00                  call 0x140a27c8c
007264F3  4C 39 6C 24 58                  cmp qword ptr [rsp + 0x58], r13
007264F8  75 1E                           jne 0x140726518
007264FA  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
007264FE  48 8D 54 24 58                  lea rdx, [rsp + 0x58]
00726503  41 B8 3F 00 0F 00               mov r8d, 0xf003f
00726509  E8 22 71 1D 00                  call 0x1408fd630
0072650E  8B D8                           mov ebx, eax
00726510  85 C0                           test eax, eax
00726512  0F 88 FB FA FF FF               js 0x140726013
00726518  4C 8B 7D D8                     mov r15, qword ptr [rbp - 0x28]
0072651C  4D 85 F6                        test r14, r14
0072651F  75 09                           jne 0x14072652a
00726521  4D 85 FF                        test r15, r15
00726524  0F 84 D7 00 00 00               je 0x140726601
0072652A  48 8B 57 30                     mov rdx, qword ptr [rdi + 0x30]
0072652E  48 8D 45 88                     lea rax, [rbp - 0x78]
00726532  48 8B 0D 5F FE 73 00            mov rcx, qword ptr [rip + 0x73fe5f]
00726539  45 33 C9                        xor r9d, r9d
0072653C  4C 89 6C 24 38                  mov qword ptr [rsp + 0x38], r13
00726541  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00726546  C6 44 24 28 01                  mov byte ptr [rsp + 0x28], 1
0072654B  45 8D 41 14                     lea r8d, [r9 + 0x14]
0072654F  C7 44 24 20 3F 00 0F 00         mov dword ptr [rsp + 0x20], 0xf003f
00726557  E8 E4 7F 1C 00                  call 0x1408ee540
0072655C  8B D8                           mov ebx, eax
0072655E  85 C0                           test eax, eax
00726560  0F 88 E0 FC FF FF               js 0x140726246
00726566  4D 85 F6                        test r14, r14
00726569  74 4B                           je 0x1407265b6
0072656B  48 8B 5D 88                     mov rbx, qword ptr [rbp - 0x78]
0072656F  48 8D 15 8A 6F 3D 00            lea rdx, [rip + 0x3d6f8a]
00726576  0F 57 C0                        xorps xmm0, xmm0
00726579  48 8D 4D B0                     lea rcx, [rbp - 0x50]
0072657D  0F 11 45 B0                     movups xmmword ptr [rbp - 0x50], xmm0
00726581  E8 FA 41 D0 FF                  call 0x14042a780
00726586  49 8B CE                        mov rcx, r14
00726589  E8 6A 61 1D 00                  call 0x1408fc6f8
0072658E  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
00726592  48 8D 55 B0                     lea rdx, [rbp - 0x50]
00726596  41 B9 08 00 00 00               mov r9d, 8
0072659C  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
007265A1  45 33 C0                        xor r8d, r8d
007265A4  48 8B CB                        mov rcx, rbx
007265A7  E8 24 77 F8 FF                  call 0x1406adcd0
007265AC  8B D8                           mov ebx, eax
007265AE  85 C0                           test eax, eax
007265B0  0F 88 90 FC FF FF               js 0x140726246
007265B6  4D 85 FF                        test r15, r15
007265B9  74 46                           je 0x140726601
007265BB  48 8B 5D 88                     mov rbx, qword ptr [rbp - 0x78]
007265BF  48 8D 15 5A 6F 3D 00            lea rdx, [rip + 0x3d6f5a]
007265C6  0F 57 C0                        xorps xmm0, xmm0
007265C9  48 8D 4D B0                     lea rcx, [rbp - 0x50]
007265CD  0F 11 45 B0                     movups xmmword ptr [rbp - 0x50], xmm0
007265D1  E8 AA 41 D0 FF                  call 0x14042a780
007265D6  41 8B 07                        mov eax, dword ptr [r15]
007265D9  48 8D 55 B0                     lea rdx, [rbp - 0x50]
007265DD  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
007265E1  41 B9 0A 00 00 00               mov r9d, 0xa
007265E7  45 33 C0                        xor r8d, r8d
007265EA  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
007265EF  48 8B CB                        mov rcx, rbx
007265F2  E8 D9 76 F8 FF                  call 0x1406adcd0
007265F7  8B D8                           mov ebx, eax
007265F9  85 C0                           test eax, eax
007265FB  0F 88 45 FC FF FF               js 0x140726246
00726601  44 38 AD 30 02 00 00            cmp byte ptr [rbp + 0x230], r13b
00726608  74 4C                           je 0x140726656
0072660A  BA 00 01 00 00                  mov edx, 0x100
0072660F  48 8B CF                        mov rcx, rdi
00726612  E8 31 5A 1D 00                  call 0x1408fc048
00726617  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
0072661C  48 8D 15 6D 6F 3D 00            lea rdx, [rip + 0x3d6f6d]
00726623  E8 84 5C 00 00                  call 0x14072c2ac
00726628  49 8B CE                        mov rcx, r14
0072662B  E8 C8 60 1D 00                  call 0x1408fc6f8
00726630  44 8B C0                        mov r8d, eax
00726633  49 8B D6                        mov rdx, r14
00726636  48 8B CF                        mov rcx, rdi
00726639  E8 A6 EE 37 00                  call 0x140aa54e4
0072663E  E9 D9 00 00 00                  jmp 0x14072671c
00726643  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
00726647  E8 04 2D BD FF                  call 0x1402f9350
0072664C  BB 0E 00 00 C0                  mov ebx, 0xc000000e
00726651  E9 BD F9 FF FF                  jmp 0x140726013
00726656  4D 85 F6                        test r14, r14
00726659  0F 84 B0 00 00 00               je 0x14072670f
0072665F  45 39 2E                        cmp dword ptr [r14], r13d
00726662  0F 84 A7 00 00 00               je 0x14072670f
00726668  45 39 6E 10                     cmp dword ptr [r14 + 0x10], r13d
0072666C  0F 84 9D 00 00 00               je 0x14072670f
00726672  49 8B CE                        mov rcx, r14
00726675  E8 7E 60 1D 00                  call 0x1408fc6f8
0072667A  41 BF 50 6E 70 47               mov r15d, 0x47706e50
00726680  8B D0                           mov edx, eax
00726682  45 8B C7                        mov r8d, r15d
00726685  8B D8                           mov ebx, eax
00726687  B9 00 01 00 00                  mov ecx, 0x100
0072668C  E8 5F BA 45 00                  call 0x140b820f0
00726691  48 8B F0                        mov rsi, rax
00726694  48 85 C0                        test rax, rax
00726697  0F 84 D4 FA FF FF               je 0x140726171
0072669D  44 8B C3                        mov r8d, ebx
007266A0  49 8B D6                        mov rdx, r14
007266A3  48 8B C8                        mov rcx, rax
007266A6  E8 95 01 FA FF                  call 0x1406c6840
007266AB  4C 8B 47 20                     mov r8, qword ptr [rdi + 0x20]
007266AF  48 8D 44 24 52                  lea rax, [rsp + 0x52]
007266B4  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
007266B9  45 33 C9                        xor r9d, r9d
007266BC  48 89 74 24 30                  mov qword ptr [rsp + 0x30], rsi
007266C1  33 C9                           xor ecx, ecx
007266C3  4C 89 44 24 28                  mov qword ptr [rsp + 0x28], r8
007266C8  4D 8B 40 08                     mov r8, qword ptr [r8 + 8]
007266CC  44 88 6C 24 52                  mov byte ptr [rsp + 0x52], r13b
007266D1  E8 C2 3C 00 00                  call 0x14072a398
007266D6  41 8B D7                        mov edx, r15d
007266D9  48 8B CE                        mov rcx, rsi
007266DC  8B D8                           mov ebx, eax
007266DE  E8 8D C1 45 00                  call 0x140b82870
007266E3  85 DB                           test ebx, ebx
007266E5  78 07                           js 0x1407266ee
007266E7  44 38 6C 24 52                  cmp byte ptr [rsp + 0x52], r13b
007266EC  74 36                           je 0x140726724
007266EE  48 8B CF                        mov rcx, rdi
007266F1  E8 7A A1 D4 FF                  call 0x140470870
007266F6  85 C0                           test eax, eax
007266F8  75 0E                           jne 0x140726708
007266FA  44 8B C3                        mov r8d, ebx
007266FD  8D 50 0C                        lea edx, [rax + 0xc]
00726700  48 8B CF                        mov rcx, rdi
00726703  E8 04 77 1D 00                  call 0x1408fde0c
00726708  BB 18 00 00 C0                  mov ebx, 0xc0000018
0072670D  EB 0D                           jmp 0x14072671c
0072670F  BA 00 01 00 00                  mov edx, 0x100
00726714  48 8B CF                        mov rcx, rdi
00726717  E8 2C 59 1D 00                  call 0x1408fc048
0072671C  85 DB                           test ebx, ebx
0072671E  0F 88 EF F8 FF FF               js 0x140726013
00726724  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
00726728  8B 88 94 02 00 00               mov ecx, dword ptr [rax + 0x294]
0072672E  89 8F 94 02 00 00               mov dword ptr [rdi + 0x294], ecx
00726734  48 8B CF                        mov rcx, rdi
00726737  E8 2C 88 22 00                  call 0x14094ef68
0072673C  BA 09 03 00 00                  mov edx, 0x309
00726741  48 8B CF                        mov rcx, rdi
00726744  E8 BF 9F D4 FF                  call 0x140470708
00726749  44 38 6C 24 53                  cmp byte ptr [rsp + 0x53], r13b
0072674E  74 0D                           je 0x14072675d
00726750  BA 00 00 00 80                  mov edx, 0x80000000
00726755  48 8B CF                        mov rcx, rdi
00726758  E8 EB 58 1D 00                  call 0x1408fc048
0072675D  48 8B 4D 08                     mov rcx, qword ptr [rbp + 8]
00726761  48 8B 47 20                     mov rax, qword ptr [rdi + 0x20]
00726765  48 89 01                        mov qword ptr [rcx], rax
00726768  E9 FB F8 FF FF                  jmp 0x140726068
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IoReportDetectedDevice(__int64 a1, int a2, int a3, int a4, __int64 a5, __int64 a6, unsigned __int8 a7, __int64 a8)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m1E8;
    unsigned __int64 v_stack_m1F0;
    unsigned __int64 v_stack_m1F8;
    unsigned __int16 v_stack_m1FE;
    unsigned __int64 v_stack_m200;
    unsigned __int64 v_stack_m208;
    unsigned __int16 v_stack_m20E;
    unsigned __int64 v_stack_m210;
    unsigned __int64 v_stack_m218;
    unsigned __int64 v_stack_m220;
    unsigned __int64 v_stack_m228;
    unsigned __int64 v_stack_m230;
    unsigned __int64 v_stack_m238;
    unsigned __int64 v_stack_m248;
    unsigned __int64 v_stack_m250;
    unsigned int v_stack_m258;
    unsigned __int64 v_stack_m260;
    unsigned __int64 v_stack_m268;
    unsigned __int64 v_stack_m270;
    unsigned int v_stack_m278;
    unsigned __int64 v_stack_m280;
    unsigned __int64 v_stack_m288;
    unsigned __int64 v_stack_m290;
    unsigned int v_stack_m298;
    unsigned __int64 v_stack_m2A0;
    unsigned int v_stack_m2A4;
    unsigned __int8 v_stack_m2A5;
    unsigned __int8 v_stack_m2A7;
    unsigned __int8 v_stack_m2A8;
    unsigned int v_stack_m2C8;
    unsigned __int64 v_stack_m2D0;
    unsigned __int64 v_stack_m2D8;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned int v_stack_p30;
    unsigned int v_stack_p38;
    unsigned int v_stack_p40;
    unsigned int v_stack_p48;
    unsigned __int64 v_stack_p51;
    unsigned __int64 v_stack_p52;
    unsigned __int8 v_stack_p53;
    unsigned __int64 v_stack_p54;
    unsigned __int64 v_stack_p58;
    unsigned int v_stack_p60;
    unsigned __int16 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;

    v_rsp = (v_rsp) - (696);
    result = (*(unsigned __int64 *)(v_rip + 7227981)) ^ (v_rsp);
    v_stack_m58 = result;
    v_rbx = 0;
    v_stack_m220 = a6;
    v_r15 = (*(unsigned __int64 *)(a1 + 48)) + (24);
    v_stack_m1F0 = a8;
    v_stack_m250 = a1;
    v_stack_m2A7 = 0;
    v_stack_m290 = 0x1900000ULL;
    v_stack_m230 = 0;
    v_stack_m2A4 = 0;
    v_stack_m228 = 0;
    v_stack_m278 = 0;
    v_stack_m268 = 0;
    v_stack_m2A8 = 0;
    v_stack_m280 = 0;
    v_stack_m298 = 0;
    v_stack_m2A0 = 0;
    v_stack_m288 = v_stack_m1E8;
    v_stack_m270 = 0;
    v_stack_m2A5 = 0;
    v_stack_m260 = 0;
    v_stack_m218 = 0;
    v_stack_m210 = v_xmm0;
    v_stack_m200 = v_xmm1;
    if (*(unsigned __int64 *)(a8) == 0) goto loc_00725DB6;
    v_stack_m280 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a8) + 312) + 40);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a8) + 312) + 40) != 0) goto loc_00725E24;
    goto loc_007260BE;
loc_00725DB6:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 16)))) & (4)) == 0) goto loc_00725E0F;
    a1 = (*(unsigned __int16 *)(v_r15)) >> (1);
    a1 = (a1) - 1;
loc_00725DCF:
    if ((*(unsigned __int64 *)(v_r15 + 8) + a1 * 2) == (*(unsigned __int64 *)(v_r15 + 8))) goto loc_00725E05;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_r15 + 8) + a1 * 2)) == 92) goto loc_00725DDF;
    a1 = (*(unsigned __int64 *)(v_r15 + 8) + a1 * 2) - (v_rbx + 2);
    goto loc_00725DCF;
loc_00725DDF:
    a1 = (a1) + (v_rbx + 2);
    v_stack_m208 = a1;
    a1 = (unsigned int)((a1) - (*(unsigned int *)(v_r15 + 8)));
    a1 = (a1) >> (1);
    a1 = (unsigned __int16)((a1) + ((unsigned __int16)(a1)));
    result = (unsigned __int16)((*(unsigned __int16 *)(v_r15)) - ((unsigned __int16)(a1)));
    v_stack_m210 = (unsigned __int16)(result);
    v_stack_m20E = (unsigned __int16)(result);
    goto loc_00725E12;
loc_00725E05:
    goto loc_007260BE;
loc_00725E0F:
loc_00725E12:
    result = IopGetRootDeviceId(v_r15, v_stack_m290, v_rbx + 2, a4);
    if (sign_flag) goto loc_007260BE;
loc_00725E24:
    result = PiPnpRtlBeginOperation(v_stack_m218, v_stack_m290, v_rbx + 2, a4);
    if (sign_flag) goto loc_00726068;
    result = PpDevNodeLockTree(1, v_stack_m290, v_rbx + 2, a4);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a8) + 312) + 40) != 0) goto loc_00725E85;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m250 + 16)))) & (4)) != 0) goto loc_00725E85;
    result = IopDuplicateDetection((unsigned int)((unsigned int)((unsigned int)(a2))), (unsigned int)((unsigned int)((unsigned int)(a3))), (unsigned int)((unsigned int)((unsigned int)(a4))), v_stack_m280);
    v_r13 = 0;
    if (sign_flag) goto loc_00725E8D;
    result = 0;
    if (v_stack_m280 != 0) { result = (unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a8) + 312) + 40) + 1); }
    v_stack_m298 = (unsigned int)(result);
    goto loc_00725E8D;
loc_00725E85:
    v_r13 = 0;
loc_00725E8D:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a2)))) | (0xFFFFFFFFULL));
    result = ExAcquireResourceExclusiveLite(v_rip + 8808281, 1, (unsigned int)((unsigned int)((unsigned int)(a4))), v_stack_m280);
    if (v_stack_m280 != 0) goto loc_007264A5;
    result = RtlAppendUnicodeToString(v_stack_m290, v_rip + 4025033, (unsigned int)((unsigned int)((unsigned int)(a4))), v_stack_m280);
    if (sign_flag) goto loc_00726068;
    v_stack_m258 = (unsigned int)(v_stack_m290);
    v_r12 = (400) - (v_stack_m290);
    v_r12 = (v_r12) >> (1);
    result = ((unsigned int)((unsigned int)(v_stack_m290))) >> (1);
    v_stack_m248 = v_stack_m1F8 + result * 2 + 16;
loc_00725EFF:
    v_stack_m290 = (unsigned __int16)(v_stack_m290);
    v_stack_m2C8 = 0;
    v_stack_m2D0 = v_rip + 4027841;
    a4 = 0;
    v_stack_m238 = v_stack_m1F8 + result * 2 + 16;
    result = RtlStringCchPrintfExW(v_stack_m1F8 + result * 2 + 16, v_r12, v_stack_m238, a4);
    result = ((unsigned int)((unsigned int)(v_stack_m290))) >> (1);
    result = (result) + (result);
    a1 = (v_stack_m238) - (result);
    a1 = (a1) - (v_stack_m1E8);
    a1 = (a1) >> (1);
    if (((unsigned int)(a1)) != -1) goto loc_00725F5B;
    a1 = (unsigned __int16)((400) - ((unsigned __int16)(v_stack_m290)));
    goto loc_00725F5E;
loc_00725F5B:
    a1 = (unsigned __int16)((a1) + ((unsigned __int16)(a1)));
loc_00725F5E:
    a2 = (unsigned __int16)((v_stack_m290) + ((unsigned __int16)(a1)));
    v_stack_m2D8 = v_stack_m2A8;
    v_stack_m290 = (unsigned __int16)(a2);
    result = CmCreateDevice(*(unsigned __int64 *)(v_rip + 7603233), v_stack_m288, (unsigned int)(0xF003FULL), v_stack_m2A0);
    result = 0;
    if (sign_flag) goto loc_007261EB;
    if (v_stack_m2A8 != 0) goto loc_007260F4;
    v_stack_m298 = 0;
    v_stack_m2D8 = v_stack_m298;
    result = IopIsReportedAlready(v_stack_m290, v_stack_m2A0, v_r15, a5);
    if ((unsigned __int8)(result) != 0) goto loc_00725FEC;
    result = ZwClose(v_stack_m2A0, v_stack_m2A0, v_r15, a5);
    v_r13 = (unsigned int)((v_r13) + 1);
    goto loc_00725EFF;
loc_00725FEC:
    result = PnpDeviceObjectFromDeviceInstanceWithTag(v_stack_m290, (unsigned int)(0x746C6644ULL), v_r15, a5);
    v_r13 = 0;
    v_stack_m260 = result;
    if (result != 0) goto loc_007260E2;
loc_00726013:
    if (v_stack_m2A8 == 0) goto loc_00726068;
    if (v_stack_m270 != 0) {
        result = ZwDeleteKey(v_stack_m270, (unsigned int)(0x746C6644ULL), v_r15, a5);
    }
    if (v_stack_m268 != 0) {
        result = ZwDeleteKey(v_stack_m268, (unsigned int)(0x746C6644ULL), v_r15, a5);
    }
    if (v_stack_m2A0 != 0) {
        result = ZwDeleteKey(v_stack_m2A0, (unsigned int)(0x746C6644ULL), v_r15, a5);
    }
    result = PnpCleanupDeviceRegistryValues(0 + 40, (unsigned int)(0x746C6644ULL), v_r15, a5);
    result = PpDevNodeRemoveFromTree(0, (unsigned int)(0x746C6644ULL), v_r15, a5);
    result = IoDeleteDevice(*(unsigned __int64 *)(0 + 32), (unsigned int)(0x746C6644ULL), v_r15, a5);
    result = ObfDereferenceObject(*(unsigned __int64 *)(0 + 32), (unsigned int)(0x746C6644ULL), v_r15, a5);
loc_00726068:
    result = ExReleaseResourceLite(v_rip + 8807825, (unsigned int)(0x746C6644ULL), v_r15, a5);
    result = KeLeaveCriticalRegion(v_rip + 8807825, (unsigned int)(0x746C6644ULL), v_r15, a5);
    result = PpDevNodeUnlockTree(1, (unsigned int)(0x746C6644ULL), v_r15, a5);
    if (v_stack_m270 != 0) {
        result = ZwClose(v_stack_m270, (unsigned int)(0x746C6644ULL), v_r15, a5);
    }
    if (v_stack_m268 != 0) {
        result = ZwClose(v_stack_m268, (unsigned int)(0x746C6644ULL), v_r15, a5);
    }
    if (v_stack_m2A0 != 0) {
        result = ZwClose(v_stack_m2A0, (unsigned int)(0x746C6644ULL), v_r15, a5);
    }
    if (v_stack_m218 != 0) {
        result = PiPnpRtlEndOperation(v_stack_m218, (unsigned int)(0x746C6644ULL), v_r15, a5);
    }
loc_007260BE:
    a1 = (v_stack_m58) ^ (v_rsp);
    result = _security_check_cookie(a1, (unsigned int)(0x746C6644ULL), v_r15, a5);
    v_rsp = (v_rsp) + (696);
    return result;
loc_007260E2:
    v_stack_p78 = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 312) + 40);
    goto loc_007260F7;
loc_007260F4:
    v_r13 = 0;
loc_007260F7:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(result + 312) + 40) != 0) goto loc_007264A5;
    result = IopCreateRootEnumeratedDeviceObject(v_stack_m260, (unsigned int)(0x746C6644ULL), v_r15, a5);
    if (sign_flag) goto loc_00726013;
    v_stack_p53 = 1;
    result = PipAllocateDeviceNode(v_stack_m260, v_stack_p78, v_r15, a5);
    if (((unsigned int)(result)) == 0xC000036EULL) goto loc_00726493;
    if (v_stack_p78 == 0) goto loc_00726493;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m250 + 16)))) & (4)) != 0) goto loc_007261AE;
    result = ExAllocatePool2(256, *(unsigned __int16 *)(v_r15), (unsigned int)(0x48706E50ULL), a5);
    *(unsigned __int64 *)(v_stack_p78 + 64) = result;
    if (result != 0) goto loc_0072618C;
loc_00726171:
loc_0072617A:
loc_0072617F:
loc_00726182:
    result = PipSetDevNodeProblem(v_stack_p78, 3, (unsigned int)(0xC000009AULL), a5);
    goto loc_00726013;
loc_0072618C:
    a3 = 0;
    *(unsigned __int16 *)(v_stack_p78 + 58) = (unsigned __int16)(*(unsigned __int16 *)(v_r15));
    result = RtlUpcaseUnicodeString(v_stack_p78 + 56, v_r15, a3, a5);
    if (!sign_flag) goto loc_007261AE;
loc_007261A9:
    goto loc_0072617A;
loc_007261AE:
    a2 = (unsigned int)((v_stack_p68) + (2));
    result = PnpAllocateDeviceInstancePath(v_stack_p78, a2, (unsigned int)((unsigned int)(result)), a5);
    if (sign_flag) goto loc_007261A9;
    a3 = 0;
    result = RtlUpcaseUnicodeString(v_stack_p78 + 40, v_stack_p68, a3, a5);
    if (!sign_flag) goto loc_007261F3;
loc_007261E3:
    result = PipSetDevNodeProblem(v_stack_p78, 3, (unsigned int)((unsigned int)(result)), a5);
loc_007261EB:
    v_r13 = 0;
    goto loc_00726013;
loc_007261F3:
    v_r13 = 0;
    a1 = (*(unsigned __int16 *)(v_stack_p78 + 40)) >> (1);
    v_stack_p38 = 0;
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p78 + 48) + a1 * 2) = 0;
    v_stack_p30 = (unsigned int)(v_r13 + 4);
    v_stack_p28 = v_stack_m278;
    v_stack_p20 = (unsigned int)(v_r13 + 4);
    v_stack_m278 = 32;
    result = CmSetDeviceRegProp(*(unsigned __int64 *)(v_rip + 7602536), *(unsigned __int64 *)(v_stack_p78 + 48), v_stack_p58, v_r13 + 11);
    if (!sign_flag) goto loc_00726250;
loc_00726246:
loc_00726249:
    goto loc_0072617F;
loc_00726250:
    v_stack_p48 = 0;
    v_stack_p40 = 1;
    v_stack_p38 = v_stack_p51;
    v_stack_p51 = 255;
    v_stack_p30 = 17;
    v_stack_p28 = v_rip - 7413334;
    v_stack_p20 = 0;
    result = PnpSetObjectProperty(*(unsigned __int64 *)(v_rip + 7602470), *(unsigned __int64 *)(v_stack_p78 + 48), 1, v_stack_p58);
    if (sign_flag) goto loc_00726246;
    result = PnpUnicodeStringToWstr(v_stack_m230, v_stack_p54, v_r15, v_stack_p58);
    if (sign_flag) goto loc_00726246;
    result = RtlStringCbLengthW(v_stack_m230, (unsigned int)(v_stack_p54), v_stack_m228, v_stack_p58);
    a1 = 0;
    if (!sign_flag) goto loc_007262EC;
    result = PnpUnicodeStringToWstrFree(v_stack_m230, v_r15, v_stack_m228, v_stack_p58);
    goto loc_007261E3;
loc_007262EC:
    result = (v_stack_m228) + (2);
    v_stack_p38 = (unsigned int)(v_stack_m230);
    v_stack_p30 = (unsigned int)(result);
    v_stack_p28 = v_stack_m230;
    v_stack_p20 = 1;
    result = CmSetDeviceRegProp(*(unsigned __int64 *)(v_rip + 7602314), *(unsigned __int64 *)(v_stack_p78 + 48), v_stack_p58, 5);
    result = PnpUnicodeStringToWstrFree(v_stack_m230, v_r15, v_stack_p58, 5);
    v_r13 = 0;
    if (!sign_flag) goto loc_00726340;
    goto loc_00726249;
loc_00726340:
    v_stack_p38 = 0;
    a4 = 0;
    v_stack_p30 = v_stack_m268;
    v_stack_m268 = 0;
    v_stack_p28 = 1;
    v_stack_p20 = 0xF003FULL;
    result = _CmOpenDeviceRegKey(*(unsigned __int64 *)(v_rip + 7602257), *(unsigned __int64 *)(v_stack_p78 + 48), 19, a4);
    if (sign_flag) goto loc_00726246;
    result = PnpSetRegistryDword(v_stack_m268, v_rip + 4026710, 19, a4);
    if (sign_flag) goto loc_00726246;
    result = (unsigned int)(*(unsigned int *)(v_stack_m250 + 16));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m250 + 16)))) & (4)) == 0) {
        result = 1;
        a1 = v_stack_p68;
        a4 = (unsigned __int8)(result);
        a2 = (unsigned __int8)(result);
        a3 = 0;
        result = PpDeviceRegistration(a1, a2, a3, a4);
    }
    v_stack_p70 = 0;
    v_rbx = v_stack_m210;
    if (((*(unsigned __int8 *)(v_stack_m250 + 16)) & (4)) == 0) { v_rbx = v_r15; }
    v_stack_p68 = 0;
    v_stack_p54 = 400;
    result = IopGetOriginalServiceName(v_rbx, v_stack_m1E8, v_stack_p54, a4);
    if (sign_flag) goto loc_00726416;
    result = (unsigned int)(v_stack_p54);
    if (((unsigned int)((unsigned int)(v_stack_p54))) >= = 2) {
        a1 = v_stack_m1E8;
        v_stack_m1FE = 400;
        result = (unsigned __int16)(((unsigned int)(v_stack_p54)) - (2));
        v_stack_m1F8 = a1;
        v_stack_m200 = (unsigned __int16)(result);
        v_rbx = v_stack_m200;
    }
    result = IopCreateLegacyDeviceIds(v_stack_m260, v_rbx, a5, a4);
    if (!sign_flag) goto loc_00726437;
    goto loc_00726182;
loc_00726437:
    result = PipSetDevNodeFlags(v_stack_p78, 17, (unsigned int)((unsigned int)(result)), a4);
    *(unsigned int *)(v_stack_p78 + 660) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 8806384) + 660)));
    result = PipSetDevNodeState(v_stack_p78, 772, (unsigned int)((unsigned int)(result)), a4);
    result = PpDevNodeInsertIntoTree(*(unsigned __int64 *)(v_rip + 8806352), v_stack_p78, (unsigned int)((unsigned int)(result)), a4);
    result = PnpMapDeviceObjectToDeviceInstance(v_stack_m260, v_stack_p78 + 40, (unsigned int)((unsigned int)(result)), a4);
    if (sign_flag) goto loc_007261A9;
    result = ObfReferenceObject(v_stack_m260, v_stack_p78 + 40, (unsigned int)((unsigned int)(result)), a4);
    goto loc_00726518;
loc_00726493:
    result = IoDeleteDevice(v_stack_m260, v_stack_p78 + 40, (unsigned int)((unsigned int)(result)), a4);
    goto loc_00726013;
loc_007264A5:
    if (v_stack_p60 == 0) goto loc_007264F3;
    result = PipAreDriversLoaded(v_stack_p78, v_stack_p78 + 40, (unsigned int)((unsigned int)(result)), a4);
    if ((unsigned int)(result) != 0) goto loc_00726643;
    if (((*(unsigned int *)(v_stack_p78 + 396)) & (0x6000ULL)) == 0) goto loc_007264E5;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p78 + 404)))) > 28) goto loc_00726643;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p78 + 404)))) >= 28) goto loc_00726643;
loc_007264E5:
    result = (unsigned int)(*(unsigned int *)(v_stack_p78 + 404));
    if (v_stack_m260 == 0) {
        a1 = v_stack_p78;
        result = PipClearDevNodeProblem(a1, v_stack_p78 + 40, (unsigned int)((unsigned int)(result)), a4);
    }
    if (v_stack_p58 != 0) goto loc_00726518;
    result = PnpDeviceObjectToDeviceInstance(*(unsigned __int64 *)(v_stack_p78 + 32), v_stack_p58, (unsigned int)(0xF003FULL), a4);
    if (sign_flag) goto loc_00726013;
loc_00726518:
    if (a5 != 0) goto loc_0072652A;
    if (v_stack_m220 == 0) goto loc_00726601;
loc_0072652A:
    a4 = 0;
    v_stack_p38 = 0;
    v_stack_p30 = v_stack_m270;
    v_stack_p28 = 1;
    v_stack_p20 = 0xF003FULL;
    result = _CmOpenDeviceRegKey(*(unsigned __int64 *)(v_rip + 7601759), *(unsigned __int64 *)(v_stack_p78 + 48), a4 + 20, a4);
    if (sign_flag) goto loc_00726246;
    if (a5 == 0) goto loc_007265B6;
    v_stack_m248 = v_xmm0;
    result = RtlInitUnicodeString(v_stack_m248, v_rip + 4026250, a4 + 20, a4);
    result = PnpDetermineResourceListSize(a5, v_rip + 4026250, a4 + 20, a4);
    v_stack_p28 = (unsigned int)(result);
    v_stack_p20 = a5;
    a3 = 0;
    result = ZwSetValueKey(v_stack_m270, v_stack_m248, a3, 8);
    if (sign_flag) goto loc_00726246;
loc_007265B6:
    if (v_stack_m220 == 0) goto loc_00726601;
    v_stack_m248 = v_xmm0;
    result = RtlInitUnicodeString(v_stack_m248, v_rip + 4026202, a3, 8);
    v_stack_p28 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m220)));
    a3 = 0;
    v_stack_p20 = v_stack_m220;
    result = ZwSetValueKey(v_stack_m270, v_stack_m248, a3, 10);
    if (sign_flag) goto loc_00726246;
loc_00726601:
    if (a7 == 0) goto loc_00726656;
    result = PipSetDevNodeFlags(v_stack_p78, 256, a3, 10);
    result = PnpSetRegistryDword(v_stack_p58, v_rip + 4026221, a3, 10);
    result = PnpDetermineResourceListSize(a5, v_rip + 4026221, a3, 10);
    result = IopWriteAllocatedResourcesToRegistry(v_stack_p78, a5, (unsigned int)((unsigned int)(result)), 10);
    goto loc_0072671C;
loc_00726643:
    result = ObfDereferenceObject(*(unsigned __int64 *)(v_stack_p78 + 32), a5, (unsigned int)((unsigned int)(result)), 10);
    goto loc_00726013;
loc_00726656:
    if (a5 == 0) goto loc_0072670F;
    if ((*(unsigned int *)(a5)) == 0) goto loc_0072670F;
    if ((*(unsigned int *)(a5 + 16)) == 0) goto loc_0072670F;
    result = PnpDetermineResourceListSize(a5, a5, (unsigned int)((unsigned int)(result)), 10);
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(result)), (unsigned int)((unsigned int)((unsigned int)(0x47706E50ULL))), 10);
    if (result == 0) goto loc_00726171;
    result = memcpy(result, a5, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), 10);
    v_stack_p48 = v_stack_p52;
    a4 = 0;
    v_stack_p30 = result;
    a1 = 0;
    v_stack_p28 = *(unsigned __int64 *)(v_stack_p78 + 32);
    v_stack_p52 = 0;
    result = IoReportResourceUsageInternal(a1, a5, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p78 + 32) + 8), a4);
    result = ExFreePoolWithTag(result, (unsigned int)((unsigned int)((unsigned int)(0x47706E50ULL))), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p78 + 32) + 8), a4);
    if (sign_flag) goto loc_007266EE;
    if (v_stack_p52 == 0) goto loc_00726724;
loc_007266EE:
    result = PipIsDevNodeDNStarted(v_stack_p78, (unsigned int)((unsigned int)((unsigned int)(0x47706E50ULL))), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p78 + 32) + 8), a4);
    if ((unsigned int)(result) == 0) {
        a3 = (unsigned int)((unsigned int)((unsigned int)(result)));
        a2 = result + 12;
        a1 = v_stack_p78;
        result = PipSetDevNodeProblem(a1, a2, a3, a4);
    }
    goto loc_0072671C;
loc_0072670F:
    result = PipSetDevNodeFlags(v_stack_p78, 256, a3, a4);
loc_0072671C:
    if (sign_flag) goto loc_00726013;
loc_00726724:
    *(unsigned int *)(v_stack_p78 + 660) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p78 + 16) + 660)));
    result = IopDoDeferredSetInterfaceState(v_stack_p78, 256, a3, a4);
    result = PipSetDevNodeState(v_stack_p78, 777, a3, a4);
    if (v_stack_p53 != 0) {
        a2 = 0x80000000ULL;
        a1 = v_stack_p78;
        result = PipSetDevNodeFlags(a1, a2, a3, a4);
    }
    *(unsigned __int64 *)(v_stack_m1F0) = *(unsigned __int64 *)(v_stack_p78 + 32);
    goto loc_00726068;
}
```

## 5. (Beta) C Style

```c
int64_t IoReportDetectedDevice(void *Arg1, int32_t Arg2, int32_t Arg3, int32_t Arg4, int64_t Arg5, int64_t Arg6, uint8_t Arg7, void *Arg8)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg8 = (uint8_t *)Arg8;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m1E8;
    uint64_t v_stack_m1F0;
    uint64_t v_stack_m1F8;
    uint16_t v_stack_m1FE;
    uint64_t v_stack_m200;
    uint64_t v_stack_m208;
    uint16_t v_stack_m20E;
    uint64_t v_stack_m210;
    uint64_t v_stack_m218;
    uint64_t v_stack_m220;
    uint64_t v_stack_m228;
    uint64_t v_stack_m230;
    uint64_t v_stack_m238;
    uint64_t v_stack_m248;
    uint64_t v_stack_m250;
    uint32_t v_stack_m258;
    uint64_t v_stack_m260;
    uint64_t v_stack_m268;
    uint64_t v_stack_m270;
    uint32_t v_stack_m278;
    uint64_t v_stack_m280;
    uint64_t v_stack_m288;
    uint64_t v_stack_m290;
    uint32_t v_stack_m298;
    uint64_t v_stack_m2A0;
    uint32_t v_stack_m2A4;
    uint8_t v_stack_m2A5;
    uint8_t v_stack_m2A7;
    uint8_t v_stack_m2A8;
    uint32_t v_stack_m2C8;
    uint64_t v_stack_m2D0;
    uint64_t v_stack_m2D8;
    uint64_t v_stack_m58;
    uint32_t v_stack_p20;
    uint64_t v_stack_p28;
    uint32_t v_stack_p30;
    uint32_t v_stack_p38;
    uint32_t v_stack_p40;
    uint32_t v_stack_p48;
    uint64_t v_stack_p51;
    uint64_t v_stack_p52;
    uint8_t v_stack_p53;
    uint64_t v_stack_p54;
    uint64_t v_stack_p58;
    uint32_t v_stack_p60;
    uint16_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;

    local_rsp = (local_rsp) - (696);
    result = (*(uint64_t *)(v_rip + 0x6E4A4D)) ^ (local_rsp);
    v_stack_m58 = result;
    local_rbx = 0;
    v_stack_m220 = Arg6;
    local_r15 = (*(uint64_t *)(arg1 + 0x30)) + (24);
    v_stack_m1F0 = Arg8;
    v_stack_m250 = Arg1;
    v_stack_m2A7 = 0;
    v_stack_m290 = 0x1900000ULL;
    v_stack_m230 = 0;
    v_stack_m2A4 = 0;
    v_stack_m228 = 0;
    v_stack_m278 = 0;
    v_stack_m268 = 0;
    v_stack_m2A8 = 0;
    v_stack_m280 = 0;
    v_stack_m298 = 0;
    v_stack_m2A0 = 0;
    v_stack_m288 = v_stack_m1E8;
    v_stack_m270 = 0;
    v_stack_m2A5 = 0;
    v_stack_m260 = 0;
    v_stack_m218 = 0;
    v_stack_m210 = v_xmm0;
    v_stack_m200 = v_xmm1;
    if (*(uint64_t *)(arg8) == 0) goto loc_00725DB6;
    v_stack_m280 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg8) + 0x138) + 0x28);
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg8) + 0x138) + 0x28) != 0) goto loc_00725E24;
    goto loc_007260BE;
loc_00725DB6:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x10)))) & (4)) == 0) goto loc_00725E0F;
    Arg1 = (*(uint16_t *)(local_r15)) >> (1);
    Arg1 = (Arg1) - 1;
loc_00725DCF:
    if ((*(uint64_t *)(local_r15 + 0x8) + Arg1 * 2) == (*(uint64_t *)(local_r15 + 0x8))) goto loc_00725E05;
    if ((*(uint16_t *)(*(uint64_t *)(local_r15 + 0x8) + arg1 * 2)) == 92) goto loc_00725DDF;
    Arg1 = (*(uint64_t *)(local_r15 + 0x8) + Arg1 * 2) - (local_rbx + 2);
    goto loc_00725DCF;
loc_00725DDF:
    Arg1 = (Arg1) + (local_rbx + 2);
    v_stack_m208 = Arg1;
    Arg1 = (uint32_t)((Arg1) - (*(uint32_t *)(local_r15 + 0x8)));
    Arg1 = (Arg1) >> (1);
    Arg1 = (uint16_t)((Arg1) + ((uint16_t)(Arg1)));
    result = (uint16_t)((*(uint16_t *)(local_r15)) - ((uint16_t)(Arg1)));
    v_stack_m210 = (uint16_t)(result);
    v_stack_m20E = (uint16_t)(result);
    goto loc_00725E12;
loc_00725E05:
    goto loc_007260BE;
loc_00725E0F:
loc_00725E12:
    result = IopGetRootDeviceId(local_r15, v_stack_m290, local_rbx + 2, Arg4);
    if (sign_flag) goto loc_007260BE;
loc_00725E24:
    result = PiPnpRtlBeginOperation(v_stack_m218, v_stack_m290, local_rbx + 2, Arg4);
    if (sign_flag) goto loc_00726068;
    result = PpDevNodeLockTree(1, v_stack_m290, local_rbx + 2, Arg4);
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg8) + 0x138) + 0x28) != 0) goto loc_00725E85;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m250 + 0x10)))) & (4)) != 0) goto loc_00725E85;
    result = IopDuplicateDetection((uint32_t)((uint32_t)((uint32_t)(Arg2))), (uint32_t)((uint32_t)((uint32_t)(Arg3))), (uint32_t)((uint32_t)((uint32_t)(Arg4))), v_stack_m280);
    local_r13 = 0;
    if (sign_flag) goto loc_00725E8D;
    result = 0;
    if (v_stack_m280 != 0) { result = (uint32_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg8) + 0x138) + 0x28) + 1); }
    v_stack_m298 = (uint32_t)(result);
    goto loc_00725E8D;
loc_00725E85:
    local_r13 = 0;
loc_00725E8D:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg2)))) | (0xFFFFFFFFULL));
    result = ExAcquireResourceExclusiveLite(v_rip + 8808281, 1, (uint32_t)((uint32_t)((uint32_t)(Arg4))), v_stack_m280);
    if (v_stack_m280 != 0) goto loc_007264A5;
    result = RtlAppendUnicodeToString(v_stack_m290, v_rip + 4025033, (uint32_t)((uint32_t)((uint32_t)(Arg4))), v_stack_m280);
    if (sign_flag) goto loc_00726068;
    v_stack_m258 = (uint32_t)(v_stack_m290);
    local_r12 = (400) - (v_stack_m290);
    local_r12 = (local_r12) >> (1);
    result = ((uint32_t)((uint32_t)(v_stack_m290))) >> (1);
    v_stack_m248 = v_stack_m1F8 + result * 2 + 16;
loc_00725EFF:
    v_stack_m290 = (uint16_t)(v_stack_m290);
    v_stack_m2C8 = 0;
    v_stack_m2D0 = v_rip + 4027841;
    Arg4 = 0;
    v_stack_m238 = v_stack_m1F8 + result * 2 + 16;
    result = RtlStringCchPrintfExW(v_stack_m1F8 + result * 2 + 16, local_r12, v_stack_m238, Arg4);
    result = ((uint32_t)((uint32_t)(v_stack_m290))) >> (1);
    result = (result) + (result);
    Arg1 = (v_stack_m238) - (result);
    Arg1 = (Arg1) - (v_stack_m1E8);
    Arg1 = (Arg1) >> (1);
    if (((uint32_t)(Arg1)) != -1) goto loc_00725F5B;
    Arg1 = (uint16_t)((400) - ((uint16_t)(v_stack_m290)));
    goto loc_00725F5E;
loc_00725F5B:
    Arg1 = (uint16_t)((Arg1) + ((uint16_t)(Arg1)));
loc_00725F5E:
    Arg2 = (uint16_t)((v_stack_m290) + ((uint16_t)(Arg1)));
    v_stack_m2D8 = v_stack_m2A8;
    v_stack_m290 = (uint16_t)(Arg2);
    result = CmCreateDevice(*(uint64_t *)(v_rip + 0x740421), v_stack_m288, (uint32_t)(0xF003FULL), v_stack_m2A0);
    result = 0;
    if (sign_flag) goto loc_007261EB;
    if (v_stack_m2A8 != 0) goto loc_007260F4;
    v_stack_m298 = 0;
    v_stack_m2D8 = v_stack_m298;
    result = IopIsReportedAlready(v_stack_m290, v_stack_m2A0, local_r15, Arg5);
    if ((uint8_t)(result) != 0) goto loc_00725FEC;
    result = ZwClose(v_stack_m2A0, v_stack_m2A0, local_r15, Arg5);
    local_r13 = (uint32_t)((local_r13) + 1);
    goto loc_00725EFF;
loc_00725FEC:
    result = PnpDeviceObjectFromDeviceInstanceWithTag(v_stack_m290, (uint32_t)(0x746C6644ULL), local_r15, Arg5);
    local_r13 = 0;
    v_stack_m260 = result;
    if (result != 0) goto loc_007260E2;
loc_00726013:
    if (v_stack_m2A8 == 0) goto loc_00726068;
    if (v_stack_m270 != 0) {
        result = ZwDeleteKey(v_stack_m270, (uint32_t)(0x746C6644ULL), local_r15, Arg5);
    }
    if (v_stack_m268 != 0) {
        result = ZwDeleteKey(v_stack_m268, (uint32_t)(0x746C6644ULL), local_r15, Arg5);
    }
    if (v_stack_m2A0 != 0) {
        result = ZwDeleteKey(v_stack_m2A0, (uint32_t)(0x746C6644ULL), local_r15, Arg5);
    }
    result = PnpCleanupDeviceRegistryValues(0 + 40, (uint32_t)(0x746C6644ULL), local_r15, Arg5);
    result = PpDevNodeRemoveFromTree(0, (uint32_t)(0x746C6644ULL), local_r15, Arg5);
    result = IoDeleteDevice(*(uint64_t *)(0 + 0x20), (uint32_t)(0x746C6644ULL), local_r15, Arg5);
    result = ObfDereferenceObject(*(uint64_t *)(0 + 0x20), (uint32_t)(0x746C6644ULL), local_r15, Arg5);
loc_00726068:
    result = ExReleaseResourceLite(v_rip + 8807825, (uint32_t)(0x746C6644ULL), local_r15, Arg5);
    result = KeLeaveCriticalRegion(v_rip + 8807825, (uint32_t)(0x746C6644ULL), local_r15, Arg5);
    result = PpDevNodeUnlockTree(1, (uint32_t)(0x746C6644ULL), local_r15, Arg5);
    if (v_stack_m270 != 0) {
        result = ZwClose(v_stack_m270, (uint32_t)(0x746C6644ULL), local_r15, Arg5);
    }
    if (v_stack_m268 != 0) {
        result = ZwClose(v_stack_m268, (uint32_t)(0x746C6644ULL), local_r15, Arg5);
    }
    if (v_stack_m2A0 != 0) {
        result = ZwClose(v_stack_m2A0, (uint32_t)(0x746C6644ULL), local_r15, Arg5);
    }
    if (v_stack_m218 != 0) {
        result = PiPnpRtlEndOperation(v_stack_m218, (uint32_t)(0x746C6644ULL), local_r15, Arg5);
    }
loc_007260BE:
    Arg1 = (v_stack_m58) ^ (local_rsp);
    result = _security_check_cookie(Arg1, (uint32_t)(0x746C6644ULL), local_r15, Arg5);
    local_rsp = (local_rsp) + (696);
    return result;
loc_007260E2:
    v_stack_p78 = *(uint64_t *)(*(uint64_t *)(result + 0x138) + 0x28);
    goto loc_007260F7;
loc_007260F4:
    local_r13 = 0;
loc_007260F7:
    if (*(uint64_t *)(*(uint64_t *)(result + 0x138) + 0x28) != 0) goto loc_007264A5;
    result = IopCreateRootEnumeratedDeviceObject(v_stack_m260, (uint32_t)(0x746C6644ULL), local_r15, Arg5);
    if (sign_flag) goto loc_00726013;
    v_stack_p53 = 1;
    result = PipAllocateDeviceNode(v_stack_m260, v_stack_p78, local_r15, Arg5);
    if (((uint32_t)(result)) == 0xC000036EULL) goto loc_00726493;
    if (v_stack_p78 == 0) goto loc_00726493;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m250 + 0x10)))) & (4)) != 0) goto loc_007261AE;
    result = ExAllocatePool2(256, *(uint16_t *)(local_r15), (uint32_t)(0x48706E50ULL), Arg5);
    *(uint64_t *)(v_stack_p78 + 0x40) = result;
    if (result != 0) goto loc_0072618C;
loc_00726171:
loc_0072617A:
loc_0072617F:
loc_00726182:
    result = PipSetDevNodeProblem(v_stack_p78, 3, (uint32_t)(0xC000009AULL), Arg5);
    goto loc_00726013;
loc_0072618C:
    Arg3 = 0;
    *(uint16_t *)(v_stack_p78 + 0x3A) = (uint16_t)(*(uint16_t *)(local_r15));
    result = RtlUpcaseUnicodeString(v_stack_p78 + 56, local_r15, Arg3, Arg5);
    if (!sign_flag) goto loc_007261AE;
loc_007261A9:
    goto loc_0072617A;
loc_007261AE:
    Arg2 = (uint32_t)((v_stack_p68) + (2));
    result = PnpAllocateDeviceInstancePath(v_stack_p78, Arg2, (uint32_t)((uint32_t)(result)), Arg5);
    if (sign_flag) goto loc_007261A9;
    Arg3 = 0;
    result = RtlUpcaseUnicodeString(v_stack_p78 + 40, v_stack_p68, Arg3, Arg5);
    if (!sign_flag) goto loc_007261F3;
loc_007261E3:
    result = PipSetDevNodeProblem(v_stack_p78, 3, (uint32_t)((uint32_t)(result)), Arg5);
loc_007261EB:
    local_r13 = 0;
    goto loc_00726013;
loc_007261F3:
    local_r13 = 0;
    Arg1 = (*(uint16_t *)(v_stack_p78 + 0x28)) >> (1);
    v_stack_p38 = 0;
    *(uint16_t *)(*(uint64_t *)(v_stack_p78 + 0x30) + arg1 * 2) = 0;
    v_stack_p30 = (uint32_t)(local_r13 + 4);
    v_stack_p28 = v_stack_m278;
    v_stack_p20 = (uint32_t)(local_r13 + 4);
    v_stack_m278 = 32;
    result = CmSetDeviceRegProp(*(uint64_t *)(v_rip + 0x740168), *(uint64_t *)(v_stack_p78 + 0x30), v_stack_p58, local_r13 + 11);
    if (!sign_flag) goto loc_00726250;
loc_00726246:
loc_00726249:
    goto loc_0072617F;
loc_00726250:
    v_stack_p48 = 0;
    v_stack_p40 = 1;
    v_stack_p38 = v_stack_p51;
    v_stack_p51 = 255;
    v_stack_p30 = 17;
    v_stack_p28 = v_rip - 7413334;
    v_stack_p20 = 0;
    result = PnpSetObjectProperty(*(uint64_t *)(v_rip + 0x740126), *(uint64_t *)(v_stack_p78 + 0x30), 1, v_stack_p58);
    if (sign_flag) goto loc_00726246;
    result = PnpUnicodeStringToWstr(v_stack_m230, v_stack_p54, local_r15, v_stack_p58);
    if (sign_flag) goto loc_00726246;
    result = RtlStringCbLengthW(v_stack_m230, (uint32_t)(v_stack_p54), v_stack_m228, v_stack_p58);
    Arg1 = 0;
    if (!sign_flag) goto loc_007262EC;
    result = PnpUnicodeStringToWstrFree(v_stack_m230, local_r15, v_stack_m228, v_stack_p58);
    goto loc_007261E3;
loc_007262EC:
    result = (v_stack_m228) + (2);
    v_stack_p38 = (uint32_t)(v_stack_m230);
    v_stack_p30 = (uint32_t)(result);
    v_stack_p28 = v_stack_m230;
    v_stack_p20 = 1;
    result = CmSetDeviceRegProp(*(uint64_t *)(v_rip + 0x74008A), *(uint64_t *)(v_stack_p78 + 0x30), v_stack_p58, 5);
    result = PnpUnicodeStringToWstrFree(v_stack_m230, local_r15, v_stack_p58, 5);
    local_r13 = 0;
    if (!sign_flag) goto loc_00726340;
    goto loc_00726249;
loc_00726340:
    v_stack_p38 = 0;
    Arg4 = 0;
    v_stack_p30 = v_stack_m268;
    v_stack_m268 = 0;
    v_stack_p28 = 1;
    v_stack_p20 = 0xF003FULL;
    result = _CmOpenDeviceRegKey(*(uint64_t *)(v_rip + 0x740051), *(uint64_t *)(v_stack_p78 + 0x30), 19, Arg4);
    if (sign_flag) goto loc_00726246;
    result = PnpSetRegistryDword(v_stack_m268, v_rip + 4026710, 19, Arg4);
    if (sign_flag) goto loc_00726246;
    result = (uint32_t)(*(uint32_t *)(v_stack_m250 + 0x10));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m250 + 0x10)))) & (4)) == 0) {
        result = 1;
        Arg1 = v_stack_p68;
        Arg4 = (uint8_t)(result);
        Arg2 = (uint8_t)(result);
        Arg3 = 0;
        result = PpDeviceRegistration(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_p70 = 0;
    local_rbx = v_stack_m210;
    if (((*(uint8_t *)(v_stack_m250 + 0x10)) & (4)) == 0) { local_rbx = local_r15; }
    v_stack_p68 = 0;
    v_stack_p54 = 400;
    result = IopGetOriginalServiceName(local_rbx, v_stack_m1E8, v_stack_p54, Arg4);
    if (sign_flag) goto loc_00726416;
    result = (uint32_t)(v_stack_p54);
    if (((uint32_t)((uint32_t)(v_stack_p54))) >= = 2) {
        Arg1 = v_stack_m1E8;
        v_stack_m1FE = 400;
        result = (uint16_t)(((uint32_t)(v_stack_p54)) - (2));
        v_stack_m1F8 = Arg1;
        v_stack_m200 = (uint16_t)(result);
        local_rbx = v_stack_m200;
    }
    result = IopCreateLegacyDeviceIds(v_stack_m260, local_rbx, Arg5, Arg4);
    if (!sign_flag) goto loc_00726437;
    goto loc_00726182;
loc_00726437:
    result = PipSetDevNodeFlags(v_stack_p78, 17, (uint32_t)((uint32_t)(result)), Arg4);
    *(uint32_t *)(v_stack_p78 + 0x294) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x865FF0) + 0x294)));
    result = PipSetDevNodeState(v_stack_p78, 772, (uint32_t)((uint32_t)(result)), Arg4);
    result = PpDevNodeInsertIntoTree(*(uint64_t *)(v_rip + 0x865FD0), v_stack_p78, (uint32_t)((uint32_t)(result)), Arg4);
    result = PnpMapDeviceObjectToDeviceInstance(v_stack_m260, v_stack_p78 + 40, (uint32_t)((uint32_t)(result)), Arg4);
    if (sign_flag) goto loc_007261A9;
    result = ObfReferenceObject(v_stack_m260, v_stack_p78 + 40, (uint32_t)((uint32_t)(result)), Arg4);
    goto loc_00726518;
loc_00726493:
    result = IoDeleteDevice(v_stack_m260, v_stack_p78 + 40, (uint32_t)((uint32_t)(result)), Arg4);
    goto loc_00726013;
loc_007264A5:
    if (v_stack_p60 == 0) goto loc_007264F3;
    result = PipAreDriversLoaded(v_stack_p78, v_stack_p78 + 40, (uint32_t)((uint32_t)(result)), Arg4);
    if ((uint32_t)(result) != 0) goto loc_00726643;
    if (((*(uint32_t *)(v_stack_p78 + 0x18C)) & (0x6000ULL)) == 0) goto loc_007264E5;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p78 + 0x194)))) > 28) goto loc_00726643;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p78 + 0x194)))) >= 28) goto loc_00726643;
loc_007264E5:
    result = (uint32_t)(*(uint32_t *)(v_stack_p78 + 0x194));
    if (v_stack_m260 == 0) {
        Arg1 = v_stack_p78;
        result = PipClearDevNodeProblem(Arg1, v_stack_p78 + 40, (uint32_t)((uint32_t)(result)), Arg4);
    }
    if (v_stack_p58 != 0) goto loc_00726518;
    result = PnpDeviceObjectToDeviceInstance(*(uint64_t *)(v_stack_p78 + 0x20), v_stack_p58, (uint32_t)(0xF003FULL), Arg4);
    if (sign_flag) goto loc_00726013;
loc_00726518:
    if (Arg5 != 0) goto loc_0072652A;
    if (v_stack_m220 == 0) goto loc_00726601;
loc_0072652A:
    Arg4 = 0;
    v_stack_p38 = 0;
    v_stack_p30 = v_stack_m270;
    v_stack_p28 = 1;
    v_stack_p20 = 0xF003FULL;
    result = _CmOpenDeviceRegKey(*(uint64_t *)(v_rip + 0x73FE5F), *(uint64_t *)(v_stack_p78 + 0x30), Arg4 + 20, Arg4);
    if (sign_flag) goto loc_00726246;
    if (Arg5 == 0) goto loc_007265B6;
    v_stack_m248 = v_xmm0;
    result = RtlInitUnicodeString(v_stack_m248, v_rip + 4026250, Arg4 + 20, Arg4);
    result = PnpDetermineResourceListSize(Arg5, v_rip + 4026250, Arg4 + 20, Arg4);
    v_stack_p28 = (uint32_t)(result);
    v_stack_p20 = Arg5;
    Arg3 = 0;
    result = ZwSetValueKey(v_stack_m270, v_stack_m248, Arg3, 8);
    if (sign_flag) goto loc_00726246;
loc_007265B6:
    if (v_stack_m220 == 0) goto loc_00726601;
    v_stack_m248 = v_xmm0;
    result = RtlInitUnicodeString(v_stack_m248, v_rip + 4026202, Arg3, 8);
    v_stack_p28 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m220)));
    Arg3 = 0;
    v_stack_p20 = v_stack_m220;
    result = ZwSetValueKey(v_stack_m270, v_stack_m248, Arg3, 10);
    if (sign_flag) goto loc_00726246;
loc_00726601:
    if (Arg7 == 0) goto loc_00726656;
    result = PipSetDevNodeFlags(v_stack_p78, 256, Arg3, 10);
    result = PnpSetRegistryDword(v_stack_p58, v_rip + 4026221, Arg3, 10);
    result = PnpDetermineResourceListSize(Arg5, v_rip + 4026221, Arg3, 10);
    result = IopWriteAllocatedResourcesToRegistry(v_stack_p78, Arg5, (uint32_t)((uint32_t)(result)), 10);
    goto loc_0072671C;
loc_00726643:
    result = ObfDereferenceObject(*(uint64_t *)(v_stack_p78 + 0x20), Arg5, (uint32_t)((uint32_t)(result)), 10);
    goto loc_00726013;
loc_00726656:
    if (Arg5 == 0) goto loc_0072670F;
    if ((*(uint32_t *)(Arg5)) == 0) goto loc_0072670F;
    if ((*(uint32_t *)(Arg5 + 0x10)) == 0) goto loc_0072670F;
    result = PnpDetermineResourceListSize(Arg5, Arg5, (uint32_t)((uint32_t)(result)), 10);
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(result)), (uint32_t)((uint32_t)((uint32_t)(0x47706E50ULL))), 10);
    if (result == 0) goto loc_00726171;
    result = memcpy(result, Arg5, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), 10);
    v_stack_p48 = v_stack_p52;
    Arg4 = 0;
    v_stack_p30 = result;
    Arg1 = 0;
    v_stack_p28 = *(uint64_t *)(v_stack_p78 + 0x20);
    v_stack_p52 = 0;
    result = IoReportResourceUsageInternal(Arg1, Arg5, *(uint64_t *)(*(uint64_t *)(v_stack_p78 + 0x20) + 0x8), Arg4);
    result = ExFreePoolWithTag(result, (uint32_t)((uint32_t)((uint32_t)(0x47706E50ULL))), *(uint64_t *)(*(uint64_t *)(v_stack_p78 + 0x20) + 0x8), Arg4);
    if (sign_flag) goto loc_007266EE;
    if (v_stack_p52 == 0) goto loc_00726724;
loc_007266EE:
    result = PipIsDevNodeDNStarted(v_stack_p78, (uint32_t)((uint32_t)((uint32_t)(0x47706E50ULL))), *(uint64_t *)(*(uint64_t *)(v_stack_p78 + 0x20) + 0x8), Arg4);
    if ((uint32_t)(result) == 0) {
        Arg3 = (uint32_t)((uint32_t)((uint32_t)(result)));
        Arg2 = result + 12;
        Arg1 = v_stack_p78;
        result = PipSetDevNodeProblem(Arg1, Arg2, Arg3, Arg4);
    }
    goto loc_0072671C;
loc_0072670F:
    result = PipSetDevNodeFlags(v_stack_p78, 256, Arg3, Arg4);
loc_0072671C:
    if (sign_flag) goto loc_00726013;
loc_00726724:
    *(uint32_t *)(v_stack_p78 + 0x294) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p78 + 0x10) + 0x294)));
    result = IopDoDeferredSetInterfaceState(v_stack_p78, 256, Arg3, Arg4);
    result = PipSetDevNodeState(v_stack_p78, 777, Arg3, Arg4);
    if (v_stack_p53 != 0) {
        Arg2 = 0x80000000ULL;
        Arg1 = v_stack_p78;
        result = PipSetDevNodeFlags(Arg1, Arg2, Arg3, Arg4);
    }
    *(uint64_t *)(v_stack_m1F0) = *(uint64_t *)(v_stack_p78 + 0x20);
    goto loc_00726068;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x10` | `32` | `R` |
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg8` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00725CD0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
