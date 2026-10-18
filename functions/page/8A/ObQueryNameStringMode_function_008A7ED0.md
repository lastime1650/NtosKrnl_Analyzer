# ObQueryNameStringMode

- RVA: `0x008A7ED0`–`0x008A8953` (길이 `2,691` bytes)
- VA: `0x00000001408A7ED0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007F28C`
- 디코드: `579`개 명령, `2,691/2,691` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **45**; 고유 호출 대상: **13**
- 직접 호출자로 확인된 함수: **27**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x008A7FB9` → [CmpQueryKeyName](CmpQueryKeyName_function_008A8960.md) (function, `0x008A8960`)
- `0x008A8028` → [IopQueryName](IopQueryName_function_008A8990.md) (function, `0x008A8990`)
- `0x008A802F` → [PsGetCurrentSilo](../../text/40/PsGetCurrentSilo_function_004094A0.md) (function, `0x004094A0`)
- `0x008A8037` → [OBP_GET_SILO_ROOT_DIRECTORY_FROM_SILO](../../text/40/OBP_GET_SILO_ROOT_DIRECTORY_FROM_SILO_function_00409500.md) (function, `0x00409500`)
- `0x008A808F` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x008A80B8` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x008A80E6` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (function, `0x0020FA20`)
- `0x008A8114` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x008A811D` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x008A8133` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x008A81CA` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x008A81F5` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x008A825A` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (function, `0x0020FA20`)
- `0x008A8270` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x008A827A` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x008A8290` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x008A829A` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008A82C4` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x008A82DA` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x008A839F` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x008A83C6` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008A845A` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x008A848B` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x008A84B4` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x008A84DA` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (function, `0x0020FA20`)
- `0x008A84F5` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x008A84FE` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x008A8514` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x008A85CC` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x008A85F7` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x008A862C` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008A863F` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (function, `0x0020FA20`)
- `0x008A867C` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x008A8695` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x008A869D` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x008A86B3` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x008A870C` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x008A8748` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x008A875E` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x008A87D2` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x008A87DA` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x008A87F0` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x008A87FA` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x008A8853` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008A8949` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [IopGetRelatedFileName](../71/IopGetRelatedFileName_function_0071B4A0.md) at `0x0071B524`
- [AlpcpGetPortNameInformation](../74/AlpcpGetPortNameInformation_function_0074C6CC.md) at `0x0074C6FC`
- [AlpcpGetPortNameInformation](../74/AlpcpGetPortNameInformation_function_0074C6CC.md) at `0x0074C741`
- [PspQueryAndCheckCpuPartitionName](../78/PspQueryAndCheckCpuPartitionName_function_0078445C.md) at `0x00784480`
- [PspQueryAndCheckCpuPartitionName](../78/PspQueryAndCheckCpuPartitionName_function_0078445C.md) at `0x007844CA`
- [SmKmFileInfoGetPath](../7A/SmKmFileInfoGetPath_function_007A83AC.md) at `0x007A8410`
- [SmKmStoreFileOpenVolume](../7A/SmKmStoreFileOpenVolume_function_007A9C14.md) at `0x007A9C9D`
- [EtwpObjectHandleEnumCallback](../7C/EtwpObjectHandleEnumCallback_function_007C0240.md) at `0x007C037E`
- [EtwpTraceHandle](../86/EtwpTraceHandle_function_0086AA44.md) at `0x0086AC2C`
- [IopQueryNameInternal](IopQueryNameInternal_function_008A6770.md) at `0x008A680E`
- [NtQueryObject](NtQueryObject_function_008A6DB0.md) at `0x008A6FE7`
- [EtwpEnumerateAddressSpace](EtwpEnumerateAddressSpace_function_008A7590.md) at `0x008A7837`
- [ObQueryNameString](ObQueryNameString_function_008A7EB0.md) at `0x008A7EB9`
- [ObpParseSymbolicLinkEx](../8B/ObpParseSymbolicLinkEx_function_008B35C0.md) at `0x008B398F`
- [ObpParseSymbolicLinkEx](../8B/ObpParseSymbolicLinkEx_function_008B35C0.md) at `0x008B39D4`
- [SepQueryNameString](../8F/SepQueryNameString_function_008F5DE8.md) at `0x008F5E17`
- [SepQueryNameString](../8F/SepQueryNameString_function_008F5DE8.md) at `0x008F5E56`
- [IoGetDeviceProperty](../8F/IoGetDeviceProperty_function_008FA720.md) at `0x008FA8A9`
- [IoRegisterDeviceInterface](../94/IoRegisterDeviceInterface_function_0094F9A0.md) at `0x0094FA21`
- [AstLogDeviceCreated](../9A/AstLogDeviceCreated_function_009A5398.md) at `0x009A53F9`
- [AstLogDeviceCreated](../9A/AstLogDeviceCreated_function_009A5398.md) at `0x009A547F`
- [CmpQueryNameString](../9B/CmpQueryNameString_function_009BA2AC.md) at `0x009BA32F`
- [MmQueryVirtualMemory](../9D/MmQueryVirtualMemory_function_009D9280.md) at `0x009D9ECA`
- [ObGetObjectInformation](../9D/ObGetObjectInformation_function_009DADE0.md) at `0x009DB23E`
- [ObGetObjectInformation](../9D/ObGetObjectInformation_function_009DADE0.md) at `0x009DB2EA`
- [MmGetFileNameForAddress](../A2/MmGetFileNameForAddress_function_00A2B878.md) at `0x00A2B915`
- [PspInitializeFullProcessImageName](../A4/PspInitializeFullProcessImageName_function_00A4345C.md) at `0x00A434F1`
- [PspInitializeFullProcessImageName](../A4/PspInitializeFullProcessImageName_function_00A4345C.md) at `0x00A435D3`
- [IopErrorLogThread](../A5/IopErrorLogThread_function_00A5DC80.md) at `0x00A5DEA5`
- [IopErrorLogThread](../A5/IopErrorLogThread_function_00A5DC80.md) at `0x00A5DEEA`
- [IopErrorLogThread](../A5/IopErrorLogThread_function_00A5DC80.md) at `0x00A5DF77`
- [IopRaiseHardError](../A6/IopRaiseHardError_function_00A64260.md) at `0x00A642BD`
- [IopRaiseHardError](../A6/IopRaiseHardError_function_00A64260.md) at `0x00A642F4`
- [MmGetFileNameForSection](../A9/MmGetFileNameForSection_function_00A9AEBC.md) at `0x00A9AF34`
- [MmGetFileNameForSection](../A9/MmGetFileNameForSection_function_00A9AEBC.md) at `0x00A9AFD4`
- [PnpBuildCmResourceList](../AA/PnpBuildCmResourceList_function_00AAB034.md) at `0x00AAB3CA`
- [sub_00B39C68](../B3/Unknown_function_00B39C68.md) at `0x00B39CA3`
- [sub_00B40124](../B4/Unknown_function_00B40124.md) at `0x00B40133`

### Static image references
- `0x008A7F3B` → RVA `0x00FC6E4C` (`ALMOSTRO`; read)
- `0x008A7F45` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x008A7F93` → RVA `0x008A8960` (`CmpQueryKeyName`; read)
- `0x008A8004` → RVA `0x008A8990` (`IopQueryName`; read)
- `0x008A8056` → RVA `0x00F0F668` (`.data`; read)
- `0x008A878E` → RVA `0x00B01450` (` ?? ::NNGAKEGL::`string'`; read)
- `0x008A8797` → RVA `0x00B01454` (`PAGE`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **43**
  - `0x008A802F` → [PsGetCurrentSilo](../../text/40/PsGetCurrentSilo_function_004094A0.md) (`PAGE` → `.text`)
  - `0x008A8037` → [OBP_GET_SILO_ROOT_DIRECTORY_FROM_SILO](../../text/40/OBP_GET_SILO_ROOT_DIRECTORY_FROM_SILO_function_00409500.md) (`PAGE` → `.text`)
  - `0x008A808F` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x008A80B8` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x008A80E6` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (`PAGE` → `.text`)
  - `0x008A8114` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x008A811D` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x008A8133` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x008A81CA` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x008A81F5` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x008A825A` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (`PAGE` → `.text`)
  - `0x008A8270` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x008A827A` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x008A8290` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x008A829A` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008A82C4` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x008A82DA` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x008A839F` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x008A83C6` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008A845A` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x008A848B` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x008A84B4` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x008A84DA` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (`PAGE` → `.text`)
  - `0x008A84F5` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x008A84FE` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x008A8514` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x008A85CC` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x008A85F7` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x008A862C` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008A863F` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (`PAGE` → `.text`)
  - `0x008A867C` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x008A8695` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x008A869D` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x008A86B3` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x008A870C` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x008A8748` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x008A875E` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x008A87D2` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x008A87DA` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x008A87F0` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x008A87FA` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x008A8853` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008A8949` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008A7ED0  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
008A7ED5  44 89 44 24 18                  mov dword ptr [rsp + 0x18], r8d
008A7EDA  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
008A7EDF  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
008A7EE4  53                              push rbx
008A7EE5  56                              push rsi
008A7EE6  57                              push rdi
008A7EE7  41 54                           push r12
008A7EE9  41 55                           push r13
008A7EEB  41 56                           push r14
008A7EED  41 57                           push r15
008A7EEF  48 81 EC 20 01 00 00            sub rsp, 0x120
008A7EF6  4D 8B E9                        mov r13, r9
008A7EF9  4C 8B FA                        mov r15, rdx
008A7EFC  48 8B F1                        mov rsi, rcx
008A7EFF  C6 44 24 40 01                  mov byte ptr [rsp + 0x40], 1
008A7F04  C6 44 24 41 00                  mov byte ptr [rsp + 0x41], 0
008A7F09  45 33 F6                        xor r14d, r14d
008A7F0C  44 89 74 24 68                  mov dword ptr [rsp + 0x68], r14d
008A7F11  4C 89 74 24 58                  mov qword ptr [rsp + 0x58], r14
008A7F16  C7 44 24 44 01 00 00 C0         mov dword ptr [rsp + 0x44], 0xc0000001
008A7F1E  48 8D 79 D0                     lea rdi, [rcx - 0x30]
008A7F22  48 89 BC 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rdi
008A7F2A  48 8B C7                        mov rax, rdi
008A7F2D  48 C1 E8 08                     shr rax, 8
008A7F31  0F B6 D0                        movzx edx, al
008A7F34  0F B6 47 18                     movzx eax, byte ptr [rdi + 0x18]
008A7F38  48 33 D0                        xor rdx, rax
008A7F3B  0F B6 05 0A EF 71 00            movzx eax, byte ptr [rip + 0x71ef0a]
008A7F42  48 33 D0                        xor rdx, rax
008A7F45  4C 8D 0D B4 80 75 FF            lea r9, [rip - 0x8a7f4c]
008A7F4C  49 8B 8C D1 00 78 FC 00         mov rcx, qword ptr [r9 + rdx*8 + 0xfc7800]
008A7F54  4C 8D 67 1A                     lea r12, [rdi + 0x1a]
008A7F58  4C 89 A4 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], r12
008A7F60  41 0F B6 04 24                  movzx eax, byte ptr [r12]
008A7F65  A8 02                           test al, 2
008A7F67  0F 85 80 00 00 00               jne 0x1408a7fed
008A7F6D  41 8B DE                        mov ebx, r14d
008A7F70  48 89 9C 24 98 00 00 00         mov qword ptr [rsp + 0x98], rbx
008A7F78  48 8B 81 A0 00 00 00            mov rax, qword ptr [rcx + 0xa0]
008A7F7F  48 85 C0                        test rax, rax
008A7F82  0F 84 A7 00 00 00               je 0x1408a802f
008A7F88  48 85 DB                        test rbx, rbx
008A7F8B  0F 85 92 09 00 00               jne 0x1408a8923
008A7F91  33 D2                           xor edx, edx
008A7F93  48 8D 0D C6 09 00 00            lea rcx, [rip + 0x9c6]
008A7F9A  45 8B C8                        mov r9d, r8d
008A7F9D  4D 8B C7                        mov r8, r15
008A7FA0  48 3B C1                        cmp rax, rcx
008A7FA3  75 5F                           jne 0x1408a8004
008A7FA5  0F B6 84 24 80 01 00 00         movzx eax, byte ptr [rsp + 0x180]
008A7FAD  88 44 24 28                     mov byte ptr [rsp + 0x28], al
008A7FB1  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
008A7FB6  48 8B CE                        mov rcx, rsi
008A7FB9  E8 A2 09 00 00                  call 0x1408a8960
008A7FBE  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
008A7FC2  83 7C 24 44 00                  cmp dword ptr [rsp + 0x44], 0
008A7FC7  7C 0C                           jl 0x1408a7fd5
008A7FC9  33 C0                           xor eax, eax
008A7FCB  41 89 47 04                     mov dword ptr [r15 + 4], eax
008A7FCF  EB 04                           jmp 0x1408a7fd5
008A7FD1  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
008A7FD5  8B 44 24 44                     mov eax, dword ptr [rsp + 0x44]
008A7FD9  48 81 C4 20 01 00 00            add rsp, 0x120
008A7FE0  41 5F                           pop r15
008A7FE2  41 5E                           pop r14
008A7FE4  41 5D                           pop r13
008A7FE6  41 5C                           pop r12
008A7FE8  5F                              pop rdi
008A7FE9  5E                              pop rsi
008A7FEA  5B                              pop rbx
008A7FEB  C3                              ret
008A7FEC  CC                              int3
008A7FED  83 E0 03                        and eax, 3
008A7FF0  42 0F B6 84 08 80 FF F0 00      movzx eax, byte ptr [rax + r9 + 0xf0ff80]
008A7FF9  48 8B DF                        mov rbx, rdi
008A7FFC  48 2B D8                        sub rbx, rax
008A7FFF  E9 6C FF FF FF                  jmp 0x1408a7f70
008A8004  48 8D 0D 85 09 00 00            lea rcx, [rip + 0x985]
008A800B  48 3B C1                        cmp rax, rcx
008A800E  0F 85 21 09 00 00               jne 0x1408a8935
008A8014  0F B6 84 24 80 01 00 00         movzx eax, byte ptr [rsp + 0x180]
008A801C  88 44 24 28                     mov byte ptr [rsp + 0x28], al
008A8020  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
008A8025  48 8B CE                        mov rcx, rsi
008A8028  E8 63 09 00 00                  call 0x1408a8990
008A802D  EB 8F                           jmp 0x1408a7fbe
008A802F  E8 6C 14 B6 FF                  call 0x1404094a0
008A8034  48 8B C8                        mov rcx, rax
008A8037  E8 C4 14 B6 FF                  call 0x140409500
008A803C  48 89 84 24 88 00 00 00         mov qword ptr [rsp + 0x88], rax
008A8044  48 85 DB                        test rbx, rbx
008A8047  0F 84 83 08 00 00               je 0x1408a88d0
008A804D  48 3B F0                        cmp rsi, rax
008A8050  0F 84 58 03 00 00               je 0x1408a83ae
008A8056  48 3B 35 0B 76 66 00            cmp rsi, qword ptr [rip + 0x66760b]
008A805D  0F 84 4B 03 00 00               je 0x1408a83ae
008A8063  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
008A806C  48 89 8C 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], rcx
008A8074  0F B7 81 E4 01 00 00            movzx eax, word ptr [rcx + 0x1e4]
008A807B  66 FF C8                        dec ax
008A807E  66 89 81 E4 01 00 00            mov word ptr [rcx + 0x1e4], ax
008A8085  90                              nop
008A8086  45 33 C0                        xor r8d, r8d
008A8089  33 D2                           xor edx, edx
008A808B  48 8D 4F 10                     lea rcx, [rdi + 0x10]
008A808F  E8 9C 81 96 FF                  call 0x140210230
008A8094  48 8B C8                        mov rcx, rax
008A8097  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
008A809C  33 C0                           xor eax, eax
008A809E  BA 11 00 00 00                  mov edx, 0x11
008A80A3  F0 48 0F B1 57 10               lock cmpxchg qword ptr [rdi + 0x10], rdx
008A80A9  74 17                           je 0x1408a80c2
008A80AB  4C 8D 4F 10                     lea r9, [rdi + 0x10]
008A80AF  4C 8B C1                        mov r8, rcx
008A80B2  33 D2                           xor edx, edx
008A80B4  48 8D 4F 10                     lea rcx, [rdi + 0x10]
008A80B8  E8 8F 83 96 FF                  call 0x14021044c
008A80BD  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
008A80C2  48 85 C9                        test rcx, rcx
008A80C5  74 04                           je 0x1408a80cb
008A80C7  C6 41 0A 01                     mov byte ptr [rcx + 0xa], 1
008A80CB  48 8B 84 24 98 00 00 00         mov rax, qword ptr [rsp + 0x98]
008A80D3  48 8B 18                        mov rbx, qword ptr [rax]
008A80D6  48 89 9C 24 80 00 00 00         mov qword ptr [rsp + 0x80], rbx
008A80DE  48 85 DB                        test rbx, rbx
008A80E1  74 15                           je 0x1408a80f8
008A80E3  48 8B CB                        mov rcx, rbx
008A80E6  E8 35 79 96 FF                  call 0x14020fa20
008A80EB  48 89 5C 24 58                  mov qword ptr [rsp + 0x58], rbx
008A80F0  48 8B 84 24 98 00 00 00         mov rax, qword ptr [rsp + 0x98]
008A80F8  0F B7 40 08                     movzx eax, word ptr [rax + 8]
008A80FC  83 C0 02                        add eax, 2
008A80FF  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
008A8103  B8 11 00 00 00                  mov eax, 0x11
008A8108  F0 4C 0F B1 77 10               lock cmpxchg qword ptr [rdi + 0x10], r14
008A810E  74 09                           je 0x1408a8119
008A8110  48 8D 4F 10                     lea rcx, [rdi + 0x10]
008A8114  E8 27 B3 9B FF                  call 0x140263440
008A8119  48 8D 4F 10                     lea rcx, [rdi + 0x10]
008A811D  E8 DE 94 A3 FF                  call 0x1402e1600
008A8122  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
008A812B  48 89 8C 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], rcx
008A8133  E8 B8 6E 9B FF                  call 0x14025eff0
008A8138  8B 54 24 48                     mov edx, dword ptr [rsp + 0x48]
008A813C  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
008A8144  48 8D 1D B5 7E 75 FF            lea rbx, [rip - 0x8a814b]
008A814B  0F 1F 44 00 00                  nop dword ptr [rax + rax]
008A8150  48 3B 8C 24 88 00 00 00         cmp rcx, qword ptr [rsp + 0x88]
008A8158  0F 84 8C 01 00 00               je 0x1408a82ea
008A815E  48 3B 0D 03 75 66 00            cmp rcx, qword ptr [rip + 0x667503]
008A8165  0F 84 7F 01 00 00               je 0x1408a82ea
008A816B  48 85 C9                        test rcx, rcx
008A816E  0F 84 76 01 00 00               je 0x1408a82ea
008A8174  8B 81 50 01 00 00               mov eax, dword ptr [rcx + 0x150]
008A817A  A8 20                           test al, 0x20
008A817C  0F 85 68 01 00 00               jne 0x1408a82ea
008A8182  48 8D 41 D0                     lea rax, [rcx - 0x30]
008A8186  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
008A818E  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
008A8197  48 89 8C 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], rcx
008A819F  0F B7 81 E4 01 00 00            movzx eax, word ptr [rcx + 0x1e4]
008A81A6  66 FF C8                        dec ax
008A81A9  66 89 81 E4 01 00 00            mov word ptr [rcx + 0x1e4], ax
008A81B0  90                              nop
008A81B1  48 8B 84 24 90 00 00 00         mov rax, qword ptr [rsp + 0x90]
008A81B9  48 83 C0 10                     add rax, 0x10
008A81BD  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
008A81C2  45 33 C0                        xor r8d, r8d
008A81C5  33 D2                           xor edx, edx
008A81C7  48 8B C8                        mov rcx, rax
008A81CA  E8 61 80 96 FF                  call 0x140210230
008A81CF  48 8B C8                        mov rcx, rax
008A81D2  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
008A81D7  33 C0                           xor eax, eax
008A81D9  4C 8B 54 24 60                  mov r10, qword ptr [rsp + 0x60]
008A81DE  BA 11 00 00 00                  mov edx, 0x11
008A81E3  F0 49 0F B1 12                  lock cmpxchg qword ptr [r10], rdx
008A81E8  74 1F                           je 0x1408a8209
008A81EA  4D 8B CA                        mov r9, r10
008A81ED  4C 8B C1                        mov r8, rcx
008A81F0  33 D2                           xor edx, edx
008A81F2  49 8B CA                        mov rcx, r10
008A81F5  E8 52 82 96 FF                  call 0x14021044c
008A81FA  4C 8B 54 24 60                  mov r10, qword ptr [rsp + 0x60]
008A81FF  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
008A8204  BA 11 00 00 00                  mov edx, 0x11
008A8209  48 85 C9                        test rcx, rcx
008A820C  74 04                           je 0x1408a8212
008A820E  C6 41 0A 01                     mov byte ptr [rcx + 0xa], 1
008A8212  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
008A821A  0F B6 41 1A                     movzx eax, byte ptr [rcx + 0x1a]
008A821E  A8 02                           test al, 2
008A8220  0F 85 37 01 00 00               jne 0x1408a835d
008A8226  49 8B CE                        mov rcx, r14
008A8229  48 85 C9                        test rcx, rcx
008A822C  0F 84 5C 01 00 00               je 0x1408a838e
008A8232  4C 8B 01                        mov r8, qword ptr [rcx]
008A8235  4D 85 C0                        test r8, r8
008A8238  0F 84 50 01 00 00               je 0x1408a838e
008A823E  0F B7 51 08                     movzx edx, word ptr [rcx + 8]
008A8242  8B 44 24 48                     mov eax, dword ptr [rsp + 0x48]
008A8246  83 C0 02                        add eax, 2
008A8249  03 D0                           add edx, eax
008A824B  89 54 24 48                     mov dword ptr [rsp + 0x48], edx
008A824F  4C 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], r8
008A8257  49 8B C8                        mov rcx, r8
008A825A  E8 C1 77 96 FF                  call 0x14020fa20
008A825F  B8 11 00 00 00                  mov eax, 0x11
008A8264  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
008A8269  F0 4C 0F B1 31                  lock cmpxchg qword ptr [rcx], r14
008A826E  74 0A                           je 0x1408a827a
008A8270  E8 CB B1 9B FF                  call 0x140263440
008A8275  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
008A827A  E8 81 93 A3 FF                  call 0x1402e1600
008A827F  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
008A8288  48 89 8C 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], rcx
008A8290  E8 5B 6D 9B FF                  call 0x14025eff0
008A8295  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
008A829A  E8 B1 10 A5 FF                  call 0x1402f9350
008A829F  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
008A82A7  48 89 4C 24 58                  mov qword ptr [rsp + 0x58], rcx
008A82AC  8B 54 24 48                     mov edx, dword ptr [rsp + 0x48]
008A82B0  81 FA FF FF 00 00               cmp edx, 0xffff
008A82B6  0F 87 C3 00 00 00               ja 0x1408a837f
008A82BC  E9 8F FE FF FF                  jmp 0x1408a8150
008A82C1  49 8B CA                        mov rcx, r10
008A82C4  E8 37 93 A3 FF                  call 0x1402e1600
008A82C9  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
008A82D2  48 89 8C 24 E8 00 00 00         mov qword ptr [rsp + 0xe8], rcx
008A82DA  E8 11 6D 9B FF                  call 0x14025eff0
008A82DF  8B 54 24 48                     mov edx, dword ptr [rsp + 0x48]
008A82E3  83 C2 08                        add edx, 8
008A82E6  89 54 24 48                     mov dword ptr [rsp + 0x48], edx
008A82EA  81 FA FF FF 00 00               cmp edx, 0xffff
008A82F0  0F 87 89 00 00 00               ja 0x1408a837f
008A82F6  83 C2 12                        add edx, 0x12
008A82F9  89 54 24 68                     mov dword ptr [rsp + 0x68], edx
008A82FD  41 89 55 00                     mov dword ptr [r13], edx
008A8301  EB 44                           jmp 0x1408a8347
008A8303  89 84 24 B8 00 00 00            mov dword ptr [rsp + 0xb8], eax
008A830A  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
008A830E  C6 44 24 40 00                  mov byte ptr [rsp + 0x40], 0
008A8313  45 33 F6                        xor r14d, r14d
008A8316  48 8D 1D E3 7C 75 FF            lea rbx, [rip - 0x8a831d]
008A831D  4C 8B AC 24 78 01 00 00         mov r13, qword ptr [rsp + 0x178]
008A8325  4C 8B BC 24 68 01 00 00         mov r15, qword ptr [rsp + 0x168]
008A832D  48 8B B4 24 60 01 00 00         mov rsi, qword ptr [rsp + 0x160]
008A8335  48 8B BC 24 A8 00 00 00         mov rdi, qword ptr [rsp + 0xa8]
008A833D  4C 8B A4 24 B0 00 00 00         mov r12, qword ptr [rsp + 0xb0]
008A8345  EB 75                           jmp 0x1408a83bc
008A8347  8B 84 24 70 01 00 00            mov eax, dword ptr [rsp + 0x170]
008A834E  3B 44 24 68                     cmp eax, dword ptr [rsp + 0x68]
008A8352  72 1C                           jb 0x1408a8370
008A8354  48 8D 1D A5 7C 75 FF            lea rbx, [rip - 0x8a835b]
008A835B  EB 5F                           jmp 0x1408a83bc
008A835D  83 E0 03                        and eax, 3
008A8360  0F B6 84 18 80 FF F0 00         movzx eax, byte ptr [rax + rbx + 0xf0ff80]
008A8368  48 2B C8                        sub rcx, rax
008A836B  E9 B9 FE FF FF                  jmp 0x1408a8229
008A8370  C7 44 24 44 04 00 00 C0         mov dword ptr [rsp + 0x44], 0xc0000004
008A8378  C6 44 24 40 00                  mov byte ptr [rsp + 0x40], 0
008A837D  EB D5                           jmp 0x1408a8354
008A837F  C7 44 24 44 06 01 00 C0         mov dword ptr [rsp + 0x44], 0xc0000106
008A8387  C6 44 24 40 00                  mov byte ptr [rsp + 0x40], 0
008A838C  EB C6                           jmp 0x1408a8354
008A838E  48 8B C2                        mov rax, rdx
008A8391  F0 4D 0F B1 32                  lock cmpxchg qword ptr [r10], r14
008A8396  0F 84 25 FF FF FF               je 0x1408a82c1
008A839C  49 8B CA                        mov rcx, r10
008A839F  E8 9C B0 9B FF                  call 0x140263440
008A83A4  4C 8B 54 24 60                  mov r10, qword ptr [rsp + 0x60]
008A83A9  E9 13 FF FF FF                  jmp 0x1408a82c1
008A83AE  BA 02 00 00 00                  mov edx, 2
008A83B3  89 54 24 48                     mov dword ptr [rsp + 0x48], edx
008A83B7  E9 3A FF FF FF                  jmp 0x1408a82f6
008A83BC  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
008A83C1  48 85 C9                        test rcx, rcx
008A83C4  74 0A                           je 0x1408a83d0
008A83C6  E8 85 0F A5 FF                  call 0x1402f9350
008A83CB  4C 89 74 24 58                  mov qword ptr [rsp + 0x58], r14
008A83D0  80 7C 24 40 00                  cmp byte ptr [rsp + 0x40], 0
008A83D5  0F 84 E7 FB FF FF               je 0x1408a7fc2
008A83DB  41 0F B6 04 24                  movzx eax, byte ptr [r12]
008A83E0  A8 02                           test al, 2
008A83E2  0F 85 81 04 00 00               jne 0x1408a8869
008A83E8  49 8B DE                        mov rbx, r14
008A83EB  48 89 9C 24 98 00 00 00         mov qword ptr [rsp + 0x98], rbx
008A83F3  48 85 DB                        test rbx, rbx
008A83F6  0F 84 9C 04 00 00               je 0x1408a8898
008A83FC  8B 44 24 68                     mov eax, dword ptr [rsp + 0x68]
008A8400  4A 8D 0C 38                     lea rcx, [rax + r15]
008A8404  48 89 4C 24 50                  mov qword ptr [rsp + 0x50], rcx
008A8409  4D 8D 4F 10                     lea r9, [r15 + 0x10]
008A840D  48 83 C1 FE                     add rcx, -2
008A8411  48 89 4C 24 50                  mov qword ptr [rsp + 0x50], rcx
008A8416  66 44 89 31                     mov word ptr [rcx], r14w
008A841A  48 3B B4 24 88 00 00 00         cmp rsi, qword ptr [rsp + 0x88]
008A8422  0F 84 9E 02 00 00               je 0x1408a86c6
008A8428  48 3B 35 39 72 66 00            cmp rsi, qword ptr [rip + 0x667239]
008A842F  0F 84 91 02 00 00               je 0x1408a86c6
008A8435  48 8D 53 08                     lea rdx, [rbx + 8]
008A8439  48 89 94 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rdx
008A8441  44 0F B7 02                     movzx r8d, word ptr [rdx]
008A8445  49 2B C8                        sub rcx, r8
008A8448  48 89 4C 24 50                  mov qword ptr [rsp + 0x50], rcx
008A844D  49 3B C9                        cmp rcx, r9
008A8450  0F 86 B3 03 00 00               jbe 0x1408a8809
008A8456  48 8B 52 08                     mov rdx, qword ptr [rdx + 8]
008A845A  E8 E1 E3 E1 FF                  call 0x1406c6840
008A845F  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
008A8468  48 89 8C 24 F0 00 00 00         mov qword ptr [rsp + 0xf0], rcx
008A8470  0F B7 81 E4 01 00 00            movzx eax, word ptr [rcx + 0x1e4]
008A8477  66 FF C8                        dec ax
008A847A  66 89 81 E4 01 00 00            mov word ptr [rcx + 0x1e4], ax
008A8481  90                              nop
008A8482  48 8D 4F 10                     lea rcx, [rdi + 0x10]
008A8486  45 33 C0                        xor r8d, r8d
008A8489  33 D2                           xor edx, edx
008A848B  E8 A0 7D 96 FF                  call 0x140210230
008A8490  48 8B C8                        mov rcx, rax
008A8493  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
008A8498  33 C0                           xor eax, eax
008A849A  BA 11 00 00 00                  mov edx, 0x11
008A849F  F0 48 0F B1 57 10               lock cmpxchg qword ptr [rdi + 0x10], rdx
008A84A5  74 17                           je 0x1408a84be
008A84A7  4C 8D 4F 10                     lea r9, [rdi + 0x10]
008A84AB  4C 8B C1                        mov r8, rcx
008A84AE  33 D2                           xor edx, edx
008A84B0  48 8D 4F 10                     lea rcx, [rdi + 0x10]
008A84B4  E8 93 7F 96 FF                  call 0x14021044c
008A84B9  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
008A84BE  48 85 C9                        test rcx, rcx
008A84C1  74 04                           je 0x1408a84c7
008A84C3  C6 41 0A 01                     mov byte ptr [rcx + 0xa], 1
008A84C7  48 8B 1B                        mov rbx, qword ptr [rbx]
008A84CA  48 89 9C 24 80 00 00 00         mov qword ptr [rsp + 0x80], rbx
008A84D2  48 85 DB                        test rbx, rbx
008A84D5  74 0D                           je 0x1408a84e4
008A84D7  48 8B CB                        mov rcx, rbx
008A84DA  E8 41 75 96 FF                  call 0x14020fa20
008A84DF  48 89 5C 24 58                  mov qword ptr [rsp + 0x58], rbx
008A84E4  B8 11 00 00 00                  mov eax, 0x11
008A84E9  F0 4C 0F B1 77 10               lock cmpxchg qword ptr [rdi + 0x10], r14
008A84EF  74 09                           je 0x1408a84fa
008A84F1  48 8D 4F 10                     lea rcx, [rdi + 0x10]
008A84F5  E8 46 AF 9B FF                  call 0x140263440
008A84FA  48 8D 4F 10                     lea rcx, [rdi + 0x10]
008A84FE  E8 FD 90 A3 FF                  call 0x1402e1600
008A8503  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
008A850C  48 89 8C 24 F8 00 00 00         mov qword ptr [rsp + 0xf8], rcx
008A8514  E8 D7 6A 9B FF                  call 0x14025eff0
008A8519  0F 1F 80 00 00 00 00            nop dword ptr [rax]
008A8520  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
008A8528  48 3B 8C 24 88 00 00 00         cmp rcx, qword ptr [rsp + 0x88]
008A8530  0F 84 87 01 00 00               je 0x1408a86bd
008A8536  48 3B 0D 2B 71 66 00            cmp rcx, qword ptr [rip + 0x66712b]
008A853D  0F 84 7A 01 00 00               je 0x1408a86bd
008A8543  48 85 C9                        test rcx, rcx
008A8546  0F 84 71 01 00 00               je 0x1408a86bd
008A854C  8B 81 50 01 00 00               mov eax, dword ptr [rcx + 0x150]
008A8552  A8 20                           test al, 0x20
008A8554  0F 85 63 01 00 00               jne 0x1408a86bd
008A855A  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
008A855F  48 83 E8 02                     sub rax, 2
008A8563  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
008A8568  BA 5C 00 00 00                  mov edx, 0x5c
008A856D  66 89 10                        mov word ptr [rax], dx
008A8570  48 8D 59 D0                     lea rbx, [rcx - 0x30]
008A8574  48 89 9C 24 90 00 00 00         mov qword ptr [rsp + 0x90], rbx
008A857C  0F B6 43 1A                     movzx eax, byte ptr [rbx + 0x1a]
008A8580  A8 02                           test al, 2
008A8582  0F 85 95 01 00 00               jne 0x1408a871d
008A8588  49 8B DE                        mov rbx, r14
008A858B  48 89 5C 24 70                  mov qword ptr [rsp + 0x70], rbx
008A8590  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
008A8599  48 89 8C 24 00 01 00 00         mov qword ptr [rsp + 0x100], rcx
008A85A1  0F B7 81 E4 01 00 00            movzx eax, word ptr [rcx + 0x1e4]
008A85A8  66 FF C8                        dec ax
008A85AB  66 89 81 E4 01 00 00            mov word ptr [rcx + 0x1e4], ax
008A85B2  90                              nop
008A85B3  48 8B 84 24 90 00 00 00         mov rax, qword ptr [rsp + 0x90]
008A85BB  48 83 C0 10                     add rax, 0x10
008A85BF  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
008A85C4  45 33 C0                        xor r8d, r8d
008A85C7  33 D2                           xor edx, edx
008A85C9  48 8B C8                        mov rcx, rax
008A85CC  E8 5F 7C 96 FF                  call 0x140210230
008A85D1  48 8B C8                        mov rcx, rax
008A85D4  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
008A85D9  33 C0                           xor eax, eax
008A85DB  4C 8B 54 24 60                  mov r10, qword ptr [rsp + 0x60]
008A85E0  BA 11 00 00 00                  mov edx, 0x11
008A85E5  F0 49 0F B1 12                  lock cmpxchg qword ptr [r10], rdx
008A85EA  74 1F                           je 0x1408a860b
008A85EC  4D 8B CA                        mov r9, r10
008A85EF  4C 8B C1                        mov r8, rcx
008A85F2  33 D2                           xor edx, edx
008A85F4  49 8B CA                        mov rcx, r10
008A85F7  E8 50 7E 96 FF                  call 0x14021044c
008A85FC  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
008A8601  4C 8B 54 24 60                  mov r10, qword ptr [rsp + 0x60]
008A8606  BA 11 00 00 00                  mov edx, 0x11
008A860B  48 85 C9                        test rcx, rcx
008A860E  74 04                           je 0x1408a8614
008A8610  C6 41 0A 01                     mov byte ptr [rcx + 0xa], 1
008A8614  48 85 DB                        test rbx, rbx
008A8617  0F 84 1A 01 00 00               je 0x1408a8737
008A861D  48 83 3B 00                     cmp qword ptr [rbx], 0
008A8621  0F 84 10 01 00 00               je 0x1408a8737
008A8627  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
008A862C  E8 1F 0D A5 FF                  call 0x1402f9350
008A8631  48 8B 1B                        mov rbx, qword ptr [rbx]
008A8634  48 89 9C 24 80 00 00 00         mov qword ptr [rsp + 0x80], rbx
008A863C  48 8B CB                        mov rcx, rbx
008A863F  E8 DC 73 96 FF                  call 0x14020fa20
008A8644  48 89 5C 24 58                  mov qword ptr [rsp + 0x58], rbx
008A8649  48 8B 54 24 70                  mov rdx, qword ptr [rsp + 0x70]
008A864E  48 83 C2 08                     add rdx, 8
008A8652  48 89 94 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rdx
008A865A  44 0F B7 02                     movzx r8d, word ptr [rdx]
008A865E  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
008A8663  49 2B C8                        sub rcx, r8
008A8666  48 89 4C 24 50                  mov qword ptr [rsp + 0x50], rcx
008A866B  49 8D 47 10                     lea rax, [r15 + 0x10]
008A866F  48 3B C8                        cmp rcx, rax
008A8672  0F 86 41 01 00 00               jbe 0x1408a87b9
008A8678  48 8B 52 08                     mov rdx, qword ptr [rdx + 8]
008A867C  E8 BF E1 E1 FF                  call 0x1406c6840
008A8681  B8 11 00 00 00                  mov eax, 0x11
008A8686  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
008A868B  F0 4C 0F B1 33                  lock cmpxchg qword ptr [rbx], r14
008A8690  74 08                           je 0x1408a869a
008A8692  48 8B CB                        mov rcx, rbx
008A8695  E8 A6 AD 9B FF                  call 0x140263440
008A869A  48 8B CB                        mov rcx, rbx
008A869D  E8 5E 8F A3 FF                  call 0x1402e1600
008A86A2  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
008A86AB  48 89 8C 24 10 01 00 00         mov qword ptr [rsp + 0x110], rcx
008A86B3  E8 38 69 9B FF                  call 0x14025eff0
008A86B8  E9 63 FE FF FF                  jmp 0x1408a8520
008A86BD  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
008A86C2  4D 8D 4F 10                     lea r9, [r15 + 0x10]
008A86C6  48 8D 51 FE                     lea rdx, [rcx - 2]
008A86CA  48 89 54 24 50                  mov qword ptr [rsp + 0x50], rdx
008A86CF  B8 5C 00 00 00                  mov eax, 0x5c
008A86D4  66 89 02                        mov word ptr [rdx], ax
008A86D7  0F B7 44 24 68                  movzx eax, word ptr [rsp + 0x68]
008A86DC  66 2B C2                        sub ax, dx
008A86DF  66 41 03 C7                     add ax, r15w
008A86E3  0F B7 D8                        movzx ebx, ax
008A86E6  89 9C 24 BC 00 00 00            mov dword ptr [rsp + 0xbc], ebx
008A86ED  66 41 89 5F 02                  mov word ptr [r15 + 2], bx
008A86F2  8D 43 FE                        lea eax, [rbx - 2]
008A86F5  66 41 89 07                     mov word ptr [r15], ax
008A86F9  4D 89 4F 08                     mov qword ptr [r15 + 8], r9
008A86FD  4C 3B CA                        cmp r9, rdx
008A8700  0F 84 08 01 00 00               je 0x1408a880e
008A8706  44 8B C3                        mov r8d, ebx
008A8709  49 8B C9                        mov rcx, r9
008A870C  E8 2F E1 E1 FF                  call 0x1406c6840
008A8711  8D 43 10                        lea eax, [rbx + 0x10]
008A8714  41 89 45 00                     mov dword ptr [r13], eax
008A8718  E9 F1 00 00 00                  jmp 0x1408a880e
008A871D  83 E0 03                        and eax, 3
008A8720  48 8D 0D D9 78 75 FF            lea rcx, [rip - 0x8a8727]
008A8727  0F B6 84 08 80 FF F0 00         movzx eax, byte ptr [rax + rcx + 0xf0ff80]
008A872F  48 2B D8                        sub rbx, rax
008A8732  E9 54 FE FF FF                  jmp 0x1408a858b
008A8737  48 8B C2                        mov rax, rdx
008A873A  F0 4D 0F B1 32                  lock cmpxchg qword ptr [r10], r14
008A873F  0F 85 B2 00 00 00               jne 0x1408a87f7
008A8745  49 8B CA                        mov rcx, r10
008A8748  E8 B3 8E A3 FF                  call 0x1402e1600
008A874D  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
008A8756  48 89 8C 24 18 01 00 00         mov qword ptr [rsp + 0x118], rcx
008A875E  E8 8D 68 9B FF                  call 0x14025eff0
008A8763  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
008A8768  48 83 C1 FA                     add rcx, -6
008A876C  48 89 4C 24 50                  mov qword ptr [rsp + 0x50], rcx
008A8771  4C 8B C1                        mov r8, rcx
008A8774  48 8B D1                        mov rdx, rcx
008A8777  4D 8D 4F 10                     lea r9, [r15 + 0x10]
008A877B  49 3B C9                        cmp rcx, r9
008A877E  73 0E                           jae 0x1408a878e
008A8780  49 8B C9                        mov rcx, r9
008A8783  48 89 4C 24 50                  mov qword ptr [rsp + 0x50], rcx
008A8788  4D 8B C1                        mov r8, r9
008A878B  49 8B D1                        mov rdx, r9
008A878E  48 8B 05 BB 8C 25 00            mov rax, qword ptr [rip + 0x258cbb]
008A8795  89 01                           mov dword ptr [rcx], eax
008A8797  0F B7 05 B6 8C 25 00            movzx eax, word ptr [rip + 0x258cb6]
008A879E  66 89 41 04                     mov word ptr [rcx + 4], ax
008A87A2  4D 3B C1                        cmp r8, r9
008A87A5  0F 85 1B FF FF FF               jne 0x1408a86c6
008A87AB  48 8D 4A 02                     lea rcx, [rdx + 2]
008A87AF  48 89 4C 24 50                  mov qword ptr [rsp + 0x50], rcx
008A87B4  E9 0D FF FF FF                  jmp 0x1408a86c6
008A87B9  C6 44 24 41 01                  mov byte ptr [rsp + 0x41], 1
008A87BE  B8 11 00 00 00                  mov eax, 0x11
008A87C3  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
008A87C8  F0 4C 0F B1 33                  lock cmpxchg qword ptr [rbx], r14
008A87CD  74 08                           je 0x1408a87d7
008A87CF  48 8B CB                        mov rcx, rbx
008A87D2  E8 69 AC 9B FF                  call 0x140263440
008A87D7  48 8B CB                        mov rcx, rbx
008A87DA  E8 21 8E A3 FF                  call 0x1402e1600
008A87DF  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
008A87E8  48 89 8C 24 08 01 00 00         mov qword ptr [rsp + 0x108], rcx
008A87F0  E8 FB 67 9B FF                  call 0x14025eff0
008A87F5  EB 17                           jmp 0x1408a880e
008A87F7  49 8B CA                        mov rcx, r10
008A87FA  E8 41 AC 9B FF                  call 0x140263440
008A87FF  4C 8B 54 24 60                  mov r10, qword ptr [rsp + 0x60]
008A8804  E9 3C FF FF FF                  jmp 0x1408a8745
008A8809  C6 44 24 41 01                  mov byte ptr [rsp + 0x41], 1
008A880E  48 8D 1D EB 77 75 FF            lea rbx, [rip - 0x8a8815]
008A8815  EB 32                           jmp 0x1408a8849
008A8817  45 33 F6                        xor r14d, r14d
008A881A  48 8D 1D DF 77 75 FF            lea rbx, [rip - 0x8a8821]
008A8821  4C 8B AC 24 78 01 00 00         mov r13, qword ptr [rsp + 0x178]
008A8829  4C 8B BC 24 68 01 00 00         mov r15, qword ptr [rsp + 0x168]
008A8831  48 8B B4 24 60 01 00 00         mov rsi, qword ptr [rsp + 0x160]
008A8839  48 8B BC 24 A8 00 00 00         mov rdi, qword ptr [rsp + 0xa8]
008A8841  4C 8B A4 24 B0 00 00 00         mov r12, qword ptr [rsp + 0xb0]
008A8849  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
008A884E  48 85 C9                        test rcx, rcx
008A8851  74 05                           je 0x1408a8858
008A8853  E8 F8 0A A5 FF                  call 0x1402f9350
008A8858  80 7C 24 41 00                  cmp byte ptr [rsp + 0x41], 0
008A885D  75 20                           jne 0x1408a887f
008A885F  44 89 74 24 44                  mov dword ptr [rsp + 0x44], r14d
008A8864  E9 60 F7 FF FF                  jmp 0x1408a7fc9
008A8869  83 E0 03                        and eax, 3
008A886C  0F B6 84 18 80 FF F0 00         movzx eax, byte ptr [rax + rbx + 0xf0ff80]
008A8874  48 8B DF                        mov rbx, rdi
008A8877  48 2B D8                        sub rbx, rax
008A887A  E9 6C FB FF FF                  jmp 0x1408a83eb
008A887F  41 0F B6 04 24                  movzx eax, byte ptr [r12]
008A8884  A8 02                           test al, 2
008A8886  75 1D                           jne 0x1408a88a5
008A8888  49 8B DE                        mov rbx, r14
008A888B  48 89 9C 24 98 00 00 00         mov qword ptr [rsp + 0x98], rbx
008A8893  C6 44 24 41 00                  mov byte ptr [rsp + 0x41], 0
008A8898  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
008A88A0  E9 9F F7 FF FF                  jmp 0x1408a8044
008A88A5  83 E0 03                        and eax, 3
008A88A8  0F B6 84 18 80 FF F0 00         movzx eax, byte ptr [rax + rbx + 0xf0ff80]
008A88B0  48 8B DF                        mov rbx, rdi
008A88B3  48 2B D8                        sub rbx, rax
008A88B6  48 89 9C 24 98 00 00 00         mov qword ptr [rsp + 0x98], rbx
008A88BE  C6 44 24 41 00                  mov byte ptr [rsp + 0x41], 0
008A88C3  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
008A88CB  E9 74 F7 FF FF                  jmp 0x1408a8044
008A88D0  41 C7 45 00 10 00 00 00         mov dword ptr [r13], 0x10
008A88D8  EB 11                           jmp 0x1408a88eb
008A88DA  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
008A88DE  4C 8B BC 24 68 01 00 00         mov r15, qword ptr [rsp + 0x168]
008A88E6  E9 D7 F6 FF FF                  jmp 0x1408a7fc2
008A88EB  83 BC 24 70 01 00 00 10         cmp dword ptr [rsp + 0x170], 0x10
008A88F3  72 21                           jb 0x1408a8916
008A88F5  41 C7 07 00 00 00 00            mov dword ptr [r15], 0
008A88FC  4D 89 77 08                     mov qword ptr [r15 + 8], r14
008A8900  E9 5A FF FF FF                  jmp 0x1408a885f
008A8905  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
008A8909  4C 8B BC 24 68 01 00 00         mov r15, qword ptr [rsp + 0x168]
008A8911  E9 AC F6 FF FF                  jmp 0x1408a7fc2
008A8916  C7 44 24 44 04 00 00 C0         mov dword ptr [rsp + 0x44], 0xc0000004
008A891E  E9 B2 F6 FF FF                  jmp 0x1408a7fd5
008A8923  66 44 39 73 08                  cmp word ptr [rbx + 8], r14w
008A8928  0F 84 63 F6 FF FF               je 0x1408a7f91
008A892E  B2 01                           mov dl, 1
008A8930  E9 5E F6 FF FF                  jmp 0x1408a7f93
008A8935  0F B6 8C 24 80 01 00 00         movzx ecx, byte ptr [rsp + 0x180]
008A893D  88 4C 24 28                     mov byte ptr [rsp + 0x28], cl
008A8941  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
008A8946  48 8B CE                        mov rcx, rsi
008A8949  E8 82 21 E1 FF                  call 0x1406baad0
008A894E  E9 6B F6 FF FF                  jmp 0x1408a7fbe
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ObQueryNameStringMode(__int64 a1, __int64 a2, int a3, __int64 a4, unsigned __int8 a5)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned int v_stack_m114;
    unsigned __int8 v_stack_m117;
    unsigned __int8 v_stack_m118;
    unsigned __int8 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mC0;
    unsigned int v_stack_mF0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p100;
    unsigned __int64 v_stack_p108;
    unsigned __int64 v_stack_p110;
    unsigned __int64 v_stack_p118;
    unsigned __int64 v_stack_p160;
    unsigned __int64 v_stack_p168;
    unsigned int v_stack_p170;
    unsigned __int64 v_stack_p178;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int8 v_stack_p28;
    unsigned __int8 v_stack_p40;
    unsigned __int8 v_stack_p41;
    unsigned int v_stack_p44;
    unsigned int v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned int v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;
    unsigned __int64 v_stack_p8;
    unsigned __int64 v_stack_p80;
    unsigned __int64 v_stack_p88;
    unsigned __int64 v_stack_p90;
    unsigned __int64 v_stack_p98;
    unsigned __int64 v_stack_pA8;
    unsigned __int64 v_stack_pB0;
    unsigned int v_stack_pB8;
    unsigned int v_stack_pBC;
    unsigned __int64 v_stack_pC0;
    unsigned __int64 v_stack_pC8;
    unsigned __int64 v_stack_pD0;
    unsigned __int64 v_stack_pD8;
    unsigned __int64 v_stack_pE0;
    unsigned __int64 v_stack_pE8;
    unsigned __int64 v_stack_pF0;
    unsigned __int64 v_stack_pF8;

    v_stack_p20 = a4;
    v_stack_p18 = a3;
    v_stack_p10 = a2;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (288);
    v_stack_m118 = 1;
    v_stack_m117 = 0;
    v_r14 = 0;
    v_stack_mF0 = 0;
    v_stack_m100 = 0;
    v_stack_m114 = 0xC0000001ULL;
    v_stack_mB0 = a1 - 48;
    result = (a1 - 48) >> (8);
    a2 = ((unsigned __int8)(result)) ^ (*(unsigned __int8 *)(a1 - 48 + 24));
    a2 = (a2) ^ (*(unsigned __int8 *)(v_rip + 7466762));
    v_stack_mA8 = a1 - 48 + 26;
    if ((((unsigned __int8)(*(unsigned __int8 *)(a1 - 48 + 26))) & (2)) != 0) goto loc_008A7FED;
loc_008A7F70:
    v_stack_mC0 = 0;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 9076556 + a2 * 8 + 16545792) + 160) == 0) goto loc_008A802F;
    if (0 != 0) goto loc_008A8923;
loc_008A7F91:
    a2 = 0;
loc_008A7F93:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 9076556 + a2 * 8 + 16545792) + 160)) != (v_rip + 2502)) goto loc_008A8004;
    v_stack_m130 = a5;
    v_stack_m138 = a4;
    result = CmpQueryKeyName(a1, a2, 0, (unsigned int)(a3));
loc_008A7FBE:
    v_stack_m114 = (unsigned int)(result);
loc_008A7FC2:
    if (v_stack_m114 < 0) goto loc_008A7FD5;
loc_008A7FC9:
    result = 0;
    *(unsigned int *)(a2 + 4) = 0;
    goto loc_008A7FD5;
loc_008A7FD5:
    v_rsp = (v_rsp) + (288);
    return (unsigned int)(v_stack_m114);
loc_008A7FED:
    result = (unsigned int)(((unsigned int)(v_stack_m114)) & (3));
    v_rbx = (a1 - 48) - (*(unsigned __int8 *)(result + (unsigned int)(a3) * 1 + 15794048));
    goto loc_008A7F70;
loc_008A8004:
    if ((*(unsigned __int8 *)(result + (unsigned int)(a3) * 1 + 15794048)) != (v_rip + 2437)) goto loc_008A8935;
    v_stack_p28 = a5;
    v_stack_p20 = a4;
    result = IopQueryName(a1, a2, 0, (unsigned int)(a3));
    goto loc_008A7FBE;
loc_008A802F:
    result = PsGetCurrentSilo(a1, a2, 0, (unsigned int)(a3));
    result = OBP_GET_SILO_ROOT_DIRECTORY_FROM_SILO(result, a2, 0, (unsigned int)(a3));
    v_stack_p88 = result;
loc_008A8044:
    if (v_rbx == 0) goto loc_008A88D0;
    if (a1 == result) goto loc_008A83AE;
    if (a1 == (*(unsigned __int64 *)(v_rip + 6714891))) goto loc_008A83AE;
    v_stack_pC8 = *(unsigned __int64 *)(gs_base + (0 + 392));
    result = (unsigned __int16)((*(unsigned __int16 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 484)) - 1);
    *(unsigned __int16 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 484) = (unsigned __int16)(result);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(a1 - 48 + 16, a2, a3, (unsigned int)(a3));
    v_stack_p70 = result;
    result = 0;
    if (!(condition_is_equal)) {
        a4 = a1 - 48 + 16;
        a3 = 0;
        a2 = 0;
        a1 = a1 - 48 + 16;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
        a1 = v_stack_p70;
    }
    if (a1 != 0) {
        *(unsigned __int8 *)(a1 + 10) = 1;
    }
    v_stack_p80 = *(unsigned __int64 *)(v_stack_p98);
    result = v_stack_p98;
    if (*(unsigned __int64 *)(v_stack_p98) != 0) {
        a1 = *(unsigned __int64 *)(v_stack_p98);
        result = ObfReferenceObject(a1, a2, a3, a4);
        v_stack_p58 = *(unsigned __int64 *)(v_stack_p98);
        result = v_stack_p98;
    }
    result = (unsigned int)((*(unsigned __int16 *)(result + 8)) + (2));
    v_stack_p48 = (unsigned int)(result);
    result = 17;
    if (!(condition_is_equal)) {
        a1 = a1 - 48 + 16;
        result = ExfReleasePushLockShared(a1, a2, a3, a4);
    }
    result = KeAbPostRelease(a1 - 48 + 16, a2, a3, a4);
    v_stack_pD0 = *(unsigned __int64 *)(gs_base + (0 + 392));
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, a4);
loc_008A8150:
    if (v_stack_p80 == v_stack_p88) goto loc_008A82EA;
    if (v_stack_p80 == (*(unsigned __int64 *)(v_rip + 6714627))) goto loc_008A82EA;
    if (v_stack_p80 == 0) goto loc_008A82EA;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p80 + 336)))) & (32)) != 0) goto loc_008A82EA;
    v_stack_p90 = v_stack_p80 - 48;
    v_stack_pD8 = *(unsigned __int64 *)(gs_base + (0 + 392));
    result = (unsigned __int16)((*(unsigned __int16 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 484)) - 1);
    *(unsigned __int16 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 484) = (unsigned __int16)(result);
    result = (v_stack_p90) + (16);
    v_stack_p60 = result;
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(result, a2, a3, a4);
    v_stack_p70 = result;
    result = 0;
    v_r10 = v_stack_p60;
    if (!(condition_is_equal)) {
        a4 = v_stack_p60;
        a3 = 0;
        a2 = 0;
        a1 = v_stack_p60;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
        v_r10 = v_stack_p60;
        a1 = v_stack_p70;
        a2 = 17;
    }
    if (a1 != 0) {
        *(unsigned __int8 *)(a1 + 10) = 1;
    }
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_stack_p90 + 26))) & (2)) != 0) goto loc_008A835D;
loc_008A8229:
    if (0 == 0) goto loc_008A838E;
    if (*(unsigned __int64 *)(0) == 0) goto loc_008A838E;
    result = (unsigned int)(((unsigned int)(v_stack_p48)) + (2));
    a2 = (unsigned int)((*(unsigned __int16 *)(0 + 8)) + ((unsigned int)(result)));
    v_stack_p48 = (unsigned int)(a2);
    v_stack_p80 = *(unsigned __int64 *)(0);
    result = ObfReferenceObject(*(unsigned __int64 *)(0), a2, *(unsigned __int64 *)(0), a4);
    result = 17;
    if (!(condition_is_equal)) {
        result = ExfReleasePushLockShared(v_stack_p60, a2, *(unsigned __int64 *)(0), a4);
        a1 = v_stack_p60;
    }
    result = KeAbPostRelease(a1, a2, *(unsigned __int64 *)(0), a4);
    v_stack_pE0 = *(unsigned __int64 *)(gs_base + (0 + 392));
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, *(unsigned __int64 *)(0), a4);
    result = ObfDereferenceObject(v_stack_p58, a2, *(unsigned __int64 *)(0), a4);
    v_stack_p58 = v_stack_p80;
    if (((unsigned int)((unsigned int)(v_stack_p48))) > 0xFFFFULL) goto loc_008A837F;
    goto loc_008A8150;
loc_008A82C1:
    result = KeAbPostRelease(v_r10, (unsigned int)(v_stack_p48), *(unsigned __int64 *)(0), a4);
    v_stack_pE8 = *(unsigned __int64 *)(gs_base + (0 + 392));
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), (unsigned int)(v_stack_p48), *(unsigned __int64 *)(0), a4);
    a2 = (unsigned int)(((unsigned int)(v_stack_p48)) + (8));
    v_stack_p48 = (unsigned int)(a2);
loc_008A82EA:
    if (((unsigned int)(a2)) > 0xFFFFULL) goto loc_008A837F;
loc_008A82F6:
    a2 = (unsigned int)((a2) + (18));
    v_stack_p68 = (unsigned int)(a2);
    *(unsigned int *)(a4) = (unsigned int)(a2);
    goto loc_008A8347;
loc_008A8347:
    if (((unsigned int)((unsigned int)(v_stack_p170))) < v_stack_p68) goto loc_008A8370;
loc_008A8354:
    goto loc_008A83BC;
loc_008A835D:
    result = (unsigned int)(((unsigned int)(v_stack_p170)) & (3));
    a1 = (*(unsigned __int64 *)(gs_base + (0 + 392))) - (*(unsigned __int8 *)(result + v_rip - 9077595 * 1 + 15794048));
    goto loc_008A8229;
loc_008A8370:
    v_stack_p44 = 0xC0000004ULL;
    v_stack_p40 = 0;
    goto loc_008A8354;
loc_008A837F:
    v_stack_p44 = 0xC0000106ULL;
    v_stack_p40 = 0;
    goto loc_008A8354;
loc_008A838E:
    if (condition_is_equal) goto loc_008A82C1;
    result = ExfReleasePushLockShared(v_r10, a2, *(unsigned __int64 *)(0), a4);
    goto loc_008A82C1;
loc_008A83AE:
    v_stack_p48 = 2;
    goto loc_008A82F6;
loc_008A83BC:
    if (v_stack_p58 != 0) {
        result = ObfDereferenceObject(v_stack_p58, 2, *(unsigned __int64 *)(0), a4);
        v_stack_p58 = 0;
    }
    if (v_stack_p40 == 0) goto loc_008A7FC2;
    if ((((unsigned __int8)(*(unsigned __int8 *)(a1 - 48 + 26))) & (2)) != 0) goto loc_008A8869;
loc_008A83EB:
    v_stack_p98 = 0;
    if (0 == 0) goto loc_008A8898;
    v_stack_p50 = (unsigned int)(v_stack_p68) + a2 * 1;
    a1 = ((unsigned int)(v_stack_p68) + a2 * 1) + (-2);
    v_stack_p50 = a1;
    *(unsigned __int16 *)(a1) = 0;
    if (a1 == v_stack_p88) goto loc_008A86C6;
    if (a1 == (*(unsigned __int64 *)(v_rip + 6713913))) goto loc_008A86C6;
    v_stack_pC0 = 0 + 8;
    a1 = (a1) - (*(unsigned __int16 *)(0 + 8));
    v_stack_p50 = a1;
    if (a1 <= (a2 + 16)) goto loc_008A8809;
    result = memcpy(a1, *(unsigned __int64 *)(0 + 8 + 8), *(unsigned __int16 *)(0 + 8), a2 + 16);
    v_stack_pF0 = *(unsigned __int64 *)(gs_base + (0 + 392));
    result = (unsigned __int16)((*(unsigned __int16 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 484)) - 1);
    *(unsigned __int16 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 484) = (unsigned __int16)(result);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(a1 - 48 + 16, a2, a3, a2 + 16);
    v_stack_p70 = result;
    result = 0;
    if (!(condition_is_equal)) {
        a4 = a1 - 48 + 16;
        a3 = 0;
        a2 = 0;
        a1 = a1 - 48 + 16;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
        a1 = v_stack_p70;
    }
    if (a1 != 0) {
        *(unsigned __int8 *)(a1 + 10) = 1;
    }
    v_stack_p80 = *(unsigned __int64 *)(0);
    if (*(unsigned __int64 *)(0) != 0) {
        a1 = *(unsigned __int64 *)(0);
        result = ObfReferenceObject(a1, a2, a3, a4);
        v_stack_p58 = *(unsigned __int64 *)(0);
    }
    result = 17;
    if (*(unsigned __int64 *)(0) != 0) {
        a1 = a1 - 48 + 16;
        result = ExfReleasePushLockShared(a1, a2, a3, a4);
    }
    result = KeAbPostRelease(a1 - 48 + 16, a2, a3, a4);
    v_stack_pF8 = *(unsigned __int64 *)(gs_base + (0 + 392));
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, a4);
loc_008A8520:
    if (v_stack_p80 == v_stack_p88) goto loc_008A86BD;
    if (v_stack_p80 == (*(unsigned __int64 *)(v_rip + 6713643))) goto loc_008A86BD;
    if (v_stack_p80 == 0) goto loc_008A86BD;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p80 + 336)))) & (32)) != 0) goto loc_008A86BD;
    result = (v_stack_p50) - (2);
    v_stack_p50 = result;
    *(unsigned __int16 *)(result) = 92;
    v_stack_p90 = v_stack_p80 - 48;
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_stack_p80 - 48 + 26))) & (2)) != 0) goto loc_008A871D;
loc_008A858B:
    v_stack_p70 = 0;
    v_stack_p100 = *(unsigned __int64 *)(gs_base + (0 + 392));
    result = (unsigned __int16)((*(unsigned __int16 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 484)) - 1);
    *(unsigned __int16 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 484) = (unsigned __int16)(result);
    result = (v_stack_p90) + (16);
    v_stack_p60 = result;
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(result, a2, a3, a4);
    v_stack_p78 = result;
    result = 0;
    v_r10 = v_stack_p60;
    if (!(condition_is_equal)) {
        a4 = v_stack_p60;
        a3 = 0;
        a2 = 0;
        a1 = v_stack_p60;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
        a1 = v_stack_p78;
        v_r10 = v_stack_p60;
        a2 = 17;
    }
    if (a1 != 0) {
        *(unsigned __int8 *)(a1 + 10) = 1;
    }
    if (0 == 0) goto loc_008A8737;
    if ((*(unsigned __int64 *)(0)) == 0) goto loc_008A8737;
    result = ObfDereferenceObject(v_stack_p58, a2, a3, a4);
    v_stack_p80 = *(unsigned __int64 *)(0);
    result = ObfReferenceObject(*(unsigned __int64 *)(0), a2, a3, a4);
    v_stack_p58 = *(unsigned __int64 *)(0);
    a2 = (v_stack_p70) + (8);
    v_stack_pC0 = a2;
    a1 = (v_stack_p50) - (*(unsigned __int16 *)(a2));
    v_stack_p50 = a1;
    if (a1 <= (a2 + 16)) goto loc_008A87B9;
    result = memcpy(a1, *(unsigned __int64 *)(a2 + 8), *(unsigned __int16 *)(a2), a4);
    result = 17;
    if (a1 != (a2 + 16)) {
        a1 = v_stack_p60;
        result = ExfReleasePushLockShared(a1, *(unsigned __int64 *)(a2 + 8), *(unsigned __int16 *)(a2), a4);
    }
    result = KeAbPostRelease(v_stack_p60, *(unsigned __int64 *)(a2 + 8), *(unsigned __int16 *)(a2), a4);
    v_stack_p110 = *(unsigned __int64 *)(gs_base + (0 + 392));
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), *(unsigned __int64 *)(a2 + 8), *(unsigned __int16 *)(a2), a4);
    goto loc_008A8520;
loc_008A86BD:
loc_008A86C6:
    v_stack_p50 = v_stack_p50 - 2;
    *(unsigned __int16 *)(v_stack_p50 - 2) = 92;
    result = (unsigned __int16)((v_stack_p68) - ((unsigned __int16)(v_stack_p50 - 2)));
    result = (unsigned __int16)((result) + ((unsigned __int16)(a2)));
    v_stack_pBC = (unsigned int)((unsigned __int16)(result));
    *(unsigned __int16 *)(a2 + 2) = (unsigned __int16)((unsigned __int16)(result));
    *(unsigned __int16 *)(a2) = (unsigned __int16)((unsigned __int16)(result) - 2);
    *(unsigned __int64 *)(a2 + 8) = a2 + 16;
    if ((a2 + 16) == (v_stack_p50 - 2)) goto loc_008A880E;
    result = memcpy(a2 + 16, v_stack_p50 - 2, (unsigned int)((unsigned int)((unsigned __int16)(result))), a2 + 16);
    *(unsigned int *)(a4) = (unsigned int)((unsigned __int16)(result) + 16);
    goto loc_008A880E;
loc_008A871D:
    result = (unsigned int)(((unsigned __int16)(result) + 16) & (3));
    v_rbx = ((unsigned __int16)(result)) - (*(unsigned __int8 *)(result + v_rip - 9078567 * 1 + 15794048));
    goto loc_008A858B;
loc_008A8737:
    if (condition_is_not_equal) goto loc_008A87F7;
loc_008A8745:
    result = KeAbPostRelease(v_r10, v_stack_p50 - 2, (unsigned int)((unsigned int)((unsigned __int16)(result))), a2 + 16);
    v_stack_p118 = *(unsigned __int64 *)(gs_base + (0 + 392));
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), v_stack_p50 - 2, (unsigned int)((unsigned int)((unsigned __int16)(result))), a2 + 16);
    a1 = (v_stack_p50) + (-6);
    v_stack_p50 = a1;
    if (a1 < (a2 + 16)) {
        a1 = a2 + 16;
        v_stack_p50 = a1;
        a3 = a2 + 16;
        a2 = a2 + 16;
    }
    *(unsigned int *)(a1) = (unsigned int)(*(unsigned __int64 *)(v_rip + 2460859));
    *(unsigned __int16 *)(a1 + 4) = (unsigned __int16)(*(unsigned __int16 *)(v_rip + 2460854));
    if (a3 != (a2 + 16)) goto loc_008A86C6;
    v_stack_p50 = a2 + 2;
    goto loc_008A86C6;
loc_008A87B9:
    v_stack_p41 = 1;
    result = 17;
    if (a3 != (a2 + 16)) {
        a1 = v_stack_p60;
        result = ExfReleasePushLockShared(a1, a2, a3, a2 + 16);
    }
    result = KeAbPostRelease(v_stack_p60, a2, a3, a2 + 16);
    v_stack_p108 = *(unsigned __int64 *)(gs_base + (0 + 392));
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, a2 + 16);
    goto loc_008A880E;
loc_008A87F7:
    result = ExfReleasePushLockShared(v_r10, a2, a3, a2 + 16);
    goto loc_008A8745;
loc_008A8809:
    v_stack_p41 = 1;
loc_008A880E:
    goto loc_008A8849;
loc_008A8849:
    if (v_stack_p58 != 0) {
        result = ObfDereferenceObject(v_stack_p58, a2, a3, a2 + 16);
    }
    if (v_stack_p41 != 0) goto loc_008A887F;
loc_008A885F:
    v_stack_p44 = 0;
    goto loc_008A7FC9;
loc_008A8869:
    result = (unsigned int)((result) & (3));
    v_rbx = (a1 - 48) - (*(unsigned __int8 *)(result + v_rip - 9078805 * 1 + 15794048));
    goto loc_008A83EB;
loc_008A887F:
    if ((((unsigned __int8)(*(unsigned __int8 *)(a1 - 48 + 26))) & (2)) != 0) goto loc_008A88A5;
    v_stack_p98 = 0;
    v_stack_p41 = 0;
loc_008A8898:
    goto loc_008A8044;
loc_008A88A5:
    result = (unsigned int)((v_stack_p88) & (3));
    v_rbx = (a1 - 48) - (*(unsigned __int8 *)(result + 0 * 1 + 15794048));
    v_stack_p98 = v_rbx;
    v_stack_p41 = 0;
    goto loc_008A8044;
loc_008A88D0:
    *(unsigned int *)(a4) = 16;
    goto loc_008A88EB;
loc_008A88EB:
    if (v_stack_p170 < 16) goto loc_008A8916;
    *(unsigned int *)(a2) = 0;
    *(unsigned __int64 *)(a2 + 8) = 0;
    goto loc_008A885F;
loc_008A8916:
    v_stack_p44 = 0xC0000004ULL;
    goto loc_008A7FD5;
loc_008A8923:
    if ((*(unsigned __int16 *)(v_rbx + 8)) == 0) goto loc_008A7F91;
    goto loc_008A7F93;
loc_008A8935:
    v_stack_p28 = a5;
    v_stack_p20 = a4;
    result = guard_dispatch_icall(a1, 1, a3, a2 + 16);
    goto loc_008A7FBE;
}
```

## 5. (Beta) C Style

```c
int64_t ObQueryNameStringMode(void *Arg1, void *Arg2, int32_t Arg3, void *Arg4, uint8_t Arg5)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r10;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint32_t v_stack_m114;
    uint8_t v_stack_m117;
    uint8_t v_stack_m118;
    uint8_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mC0;
    uint32_t v_stack_mF0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p100;
    uint64_t v_stack_p108;
    uint64_t v_stack_p110;
    uint64_t v_stack_p118;
    uint64_t v_stack_p160;
    uint64_t v_stack_p168;
    uint32_t v_stack_p170;
    uint64_t v_stack_p178;
    uint32_t v_stack_p18;
    uint64_t v_stack_p20;
    uint8_t v_stack_p28;
    uint8_t v_stack_p40;
    uint8_t v_stack_p41;
    uint32_t v_stack_p44;
    uint32_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint32_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;
    uint64_t v_stack_p8;
    uint64_t v_stack_p80;
    uint64_t v_stack_p88;
    uint64_t v_stack_p90;
    uint64_t v_stack_p98;
    uint64_t v_stack_pA8;
    uint64_t v_stack_pB0;
    uint32_t v_stack_pB8;
    uint32_t v_stack_pBC;
    uint64_t v_stack_pC0;
    uint64_t v_stack_pC8;
    uint64_t v_stack_pD0;
    uint64_t v_stack_pD8;
    uint64_t v_stack_pE0;
    uint64_t v_stack_pE8;
    uint64_t v_stack_pF0;
    uint64_t v_stack_pF8;

    v_stack_p20 = Arg4;
    v_stack_p18 = Arg3;
    v_stack_p10 = Arg2;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (288);
    v_stack_m118 = 1;
    v_stack_m117 = 0;
    local_r14 = 0;
    v_stack_mF0 = 0;
    v_stack_m100 = 0;
    v_stack_m114 = 0xC0000001ULL;
    v_stack_mB0 = Arg1 - 48;
    result = (Arg1 - 48) >> (8);
    Arg2 = ((uint8_t)(result)) ^ (*(uint8_t *)(arg1 - 0x30 + 0x18));
    Arg2 = (Arg2) ^ (*(uint8_t *)(v_rip + 0x71EF0A));
    v_stack_mA8 = Arg1 - 48 + 26;
    if ((((uint8_t)(*(uint8_t *)(arg1 - 0x30 + 0x1A))) & (2)) != 0) goto loc_008A7FED;
loc_008A7F70:
    v_stack_mC0 = 0;
    if (*(uint64_t *)(*(uint64_t *)(v_rip - 0x8A7F4C + arg2 * 8 + 0xFC7800) + 0xA0) == 0) goto loc_008A802F;
    if (0 != 0) goto loc_008A8923;
loc_008A7F91:
    Arg2 = 0;
loc_008A7F93:
    if ((*(uint64_t *)(*(uint64_t *)(v_rip - 0x8A7F4C + arg2 * 8 + 0xFC7800) + 0xA0)) != (v_rip + 2502)) goto loc_008A8004;
    v_stack_m130 = Arg5;
    v_stack_m138 = Arg4;
    result = CmpQueryKeyName(Arg1, Arg2, 0, (uint32_t)(Arg3));
loc_008A7FBE:
    v_stack_m114 = (uint32_t)(result);
loc_008A7FC2:
    if (v_stack_m114 < 0) goto loc_008A7FD5;
loc_008A7FC9:
    result = 0;
    *(uint32_t *)(arg2 + 0x4) = 0;
    goto loc_008A7FD5;
loc_008A7FD5:
    local_rsp = (local_rsp) + (288);
    return (uint32_t)(v_stack_m114);
loc_008A7FED:
    result = (uint32_t)(((uint32_t)(v_stack_m114)) & (3));
    local_rbx = (Arg1 - 48) - (*(uint8_t *)(result + (uint32_t)(Arg3) * 1 + 0xF0FF80));
    goto loc_008A7F70;
loc_008A8004:
    if ((*(uint8_t *)(result + (uint32_t)(Arg3) * 1 + 0xF0FF80)) != (v_rip + 2437)) goto loc_008A8935;
    v_stack_p28 = Arg5;
    v_stack_p20 = Arg4;
    result = IopQueryName(Arg1, Arg2, 0, (uint32_t)(Arg3));
    goto loc_008A7FBE;
loc_008A802F:
    result = PsGetCurrentSilo(Arg1, Arg2, 0, (uint32_t)(Arg3));
    result = OBP_GET_SILO_ROOT_DIRECTORY_FROM_SILO(result, Arg2, 0, (uint32_t)(Arg3));
    v_stack_p88 = result;
loc_008A8044:
    if (local_rbx == 0) goto loc_008A88D0;
    if (Arg1 == result) goto loc_008A83AE;
    if (Arg1 == (*(uint64_t *)(v_rip + 0x66760B))) goto loc_008A83AE;
    v_stack_pC8 = *(uint64_t *)(gs_base + (0 + 0x188));
    result = (uint16_t)((*(uint16_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x1E4)) - 1);
    *(uint16_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x1E4) = (uint16_t)(result);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(Arg1 - 48 + 16, Arg2, Arg3, (uint32_t)(Arg3));
    v_stack_p70 = result;
    result = 0;
    if (!(condition_is_equal)) {
        Arg4 = Arg1 - 48 + 16;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = Arg1 - 48 + 16;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, Arg4);
        Arg1 = v_stack_p70;
    }
    if (Arg1 != NULL) {
        *(uint8_t *)(arg1 + 0xA) = 1;
    }
    v_stack_p80 = *(uint64_t *)(v_stack_p98);
    result = v_stack_p98;
    if (*(uint64_t *)(v_stack_p98) != 0) {
        Arg1 = *(uint64_t *)(v_stack_p98);
        result = ObfReferenceObject(Arg1, Arg2, Arg3, Arg4);
        v_stack_p58 = *(uint64_t *)(v_stack_p98);
        result = v_stack_p98;
    }
    result = (uint32_t)((*(uint16_t *)(result + 0x8)) + (2));
    v_stack_p48 = (uint32_t)(result);
    result = 17;
    if (!(condition_is_equal)) {
        Arg1 = Arg1 - 48 + 16;
        result = ExfReleasePushLockShared(Arg1, Arg2, Arg3, Arg4);
    }
    result = KeAbPostRelease(Arg1 - 48 + 16, Arg2, Arg3, Arg4);
    v_stack_pD0 = *(uint64_t *)(gs_base + (0 + 0x188));
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, Arg3, Arg4);
loc_008A8150:
    if (v_stack_p80 == v_stack_p88) goto loc_008A82EA;
    if (v_stack_p80 == (*(uint64_t *)(v_rip + 0x667503))) goto loc_008A82EA;
    if (v_stack_p80 == 0) goto loc_008A82EA;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p80 + 0x150)))) & (32)) != 0) goto loc_008A82EA;
    v_stack_p90 = v_stack_p80 - 48;
    v_stack_pD8 = *(uint64_t *)(gs_base + (0 + 0x188));
    result = (uint16_t)((*(uint16_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x1E4)) - 1);
    *(uint16_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x1E4) = (uint16_t)(result);
    result = (v_stack_p90) + (16);
    v_stack_p60 = result;
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(result, Arg2, Arg3, Arg4);
    v_stack_p70 = result;
    result = 0;
    local_r10 = v_stack_p60;
    if (!(condition_is_equal)) {
        Arg4 = v_stack_p60;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = v_stack_p60;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, Arg4);
        local_r10 = v_stack_p60;
        Arg1 = v_stack_p70;
        Arg2 = 17;
    }
    if (Arg1 != NULL) {
        *(uint8_t *)(arg1 + 0xA) = 1;
    }
    if ((((uint8_t)(*(uint8_t *)(v_stack_p90 + 0x1A))) & (2)) != 0) goto loc_008A835D;
loc_008A8229:
    if (0 == 0) goto loc_008A838E;
    if (*(uint64_t *)(0) == 0) goto loc_008A838E;
    result = (uint32_t)(((uint32_t)(v_stack_p48)) + (2));
    Arg2 = (uint32_t)((*(uint16_t *)(0 + 0x8)) + ((uint32_t)(result)));
    v_stack_p48 = (uint32_t)(Arg2);
    v_stack_p80 = *(uint64_t *)(0);
    result = ObfReferenceObject(*(uint64_t *)(0), Arg2, *(uint64_t *)(0), Arg4);
    result = 17;
    if (!(condition_is_equal)) {
        result = ExfReleasePushLockShared(v_stack_p60, Arg2, *(uint64_t *)(0), Arg4);
        Arg1 = v_stack_p60;
    }
    result = KeAbPostRelease(Arg1, Arg2, *(uint64_t *)(0), Arg4);
    v_stack_pE0 = *(uint64_t *)(gs_base + (0 + 0x188));
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, *(uint64_t *)(0), Arg4);
    result = ObfDereferenceObject(v_stack_p58, Arg2, *(uint64_t *)(0), Arg4);
    v_stack_p58 = v_stack_p80;
    if (((uint32_t)((uint32_t)(v_stack_p48))) > 0xFFFFULL) goto loc_008A837F;
    goto loc_008A8150;
loc_008A82C1:
    result = KeAbPostRelease(local_r10, (uint32_t)(v_stack_p48), *(uint64_t *)(0), Arg4);
    v_stack_pE8 = *(uint64_t *)(gs_base + (0 + 0x188));
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), (uint32_t)(v_stack_p48), *(uint64_t *)(0), Arg4);
    Arg2 = (uint32_t)(((uint32_t)(v_stack_p48)) + (8));
    v_stack_p48 = (uint32_t)(Arg2);
loc_008A82EA:
    if (((uint32_t)(Arg2)) > 0xFFFFULL) goto loc_008A837F;
loc_008A82F6:
    Arg2 = (uint32_t)((Arg2) + (18));
    v_stack_p68 = (uint32_t)(Arg2);
    *(uint32_t *)(arg4) = (uint32_t)(Arg2);
    goto loc_008A8347;
loc_008A8347:
    if (((uint32_t)((uint32_t)(v_stack_p170))) < v_stack_p68) goto loc_008A8370;
loc_008A8354:
    goto loc_008A83BC;
loc_008A835D:
    result = (uint32_t)(((uint32_t)(v_stack_p170)) & (3));
    Arg1 = (*(uint64_t *)(gs_base + (0 + 0x188))) - (*(uint8_t *)(result + v_rip - 0x8A835B * 1 + 0xF0FF80));
    goto loc_008A8229;
loc_008A8370:
    v_stack_p44 = 0xC0000004ULL;
    v_stack_p40 = 0;
    goto loc_008A8354;
loc_008A837F:
    v_stack_p44 = 0xC0000106ULL;
    v_stack_p40 = 0;
    goto loc_008A8354;
loc_008A838E:
    if (condition_is_equal) goto loc_008A82C1;
    result = ExfReleasePushLockShared(local_r10, Arg2, *(uint64_t *)(0), Arg4);
    goto loc_008A82C1;
loc_008A83AE:
    v_stack_p48 = 2;
    goto loc_008A82F6;
loc_008A83BC:
    if (v_stack_p58 != 0) {
        result = ObfDereferenceObject(v_stack_p58, 2, *(uint64_t *)(0), Arg4);
        v_stack_p58 = 0;
    }
    if (v_stack_p40 == 0) goto loc_008A7FC2;
    if ((((uint8_t)(*(uint8_t *)(arg1 - 0x30 + 0x1A))) & (2)) != 0) goto loc_008A8869;
loc_008A83EB:
    v_stack_p98 = 0;
    if (0 == 0) goto loc_008A8898;
    v_stack_p50 = (uint32_t)(v_stack_p68) + Arg2 * 1;
    Arg1 = ((uint32_t)(v_stack_p68) + Arg2 * 1) + (-2);
    v_stack_p50 = Arg1;
    *(uint16_t *)(arg1) = 0;
    if (Arg1 == v_stack_p88) goto loc_008A86C6;
    if (Arg1 == (*(uint64_t *)(v_rip + 0x667239))) goto loc_008A86C6;
    v_stack_pC0 = 0 + 8;
    Arg1 = (Arg1) - (*(uint16_t *)(0 + 0x8));
    v_stack_p50 = Arg1;
    if (Arg1 <= (Arg2 + 16)) goto loc_008A8809;
    result = memcpy(Arg1, *(uint64_t *)(0 + 0x8 + 0x8), *(uint16_t *)(0 + 0x8), Arg2 + 16);
    v_stack_pF0 = *(uint64_t *)(gs_base + (0 + 0x188));
    result = (uint16_t)((*(uint16_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x1E4)) - 1);
    *(uint16_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x1E4) = (uint16_t)(result);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(Arg1 - 48 + 16, Arg2, Arg3, Arg2 + 16);
    v_stack_p70 = result;
    result = 0;
    if (!(condition_is_equal)) {
        Arg4 = Arg1 - 48 + 16;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = Arg1 - 48 + 16;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, Arg4);
        Arg1 = v_stack_p70;
    }
    if (Arg1 != NULL) {
        *(uint8_t *)(arg1 + 0xA) = 1;
    }
    v_stack_p80 = *(uint64_t *)(0);
    if (*(uint64_t *)(0) != 0) {
        Arg1 = *(uint64_t *)(0);
        result = ObfReferenceObject(Arg1, Arg2, Arg3, Arg4);
        v_stack_p58 = *(uint64_t *)(0);
    }
    result = 17;
    if (*(uint64_t *)(0) != 0) {
        Arg1 = Arg1 - 48 + 16;
        result = ExfReleasePushLockShared(Arg1, Arg2, Arg3, Arg4);
    }
    result = KeAbPostRelease(Arg1 - 48 + 16, Arg2, Arg3, Arg4);
    v_stack_pF8 = *(uint64_t *)(gs_base + (0 + 0x188));
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, Arg3, Arg4);
loc_008A8520:
    if (v_stack_p80 == v_stack_p88) goto loc_008A86BD;
    if (v_stack_p80 == (*(uint64_t *)(v_rip + 0x66712B))) goto loc_008A86BD;
    if (v_stack_p80 == 0) goto loc_008A86BD;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p80 + 0x150)))) & (32)) != 0) goto loc_008A86BD;
    result = (v_stack_p50) - (2);
    v_stack_p50 = result;
    *(uint16_t *)(result) = 92;
    v_stack_p90 = v_stack_p80 - 48;
    if ((((uint8_t)(*(uint8_t *)(v_stack_p80 - 0x30 + 0x1A))) & (2)) != 0) goto loc_008A871D;
loc_008A858B:
    v_stack_p70 = 0;
    v_stack_p100 = *(uint64_t *)(gs_base + (0 + 0x188));
    result = (uint16_t)((*(uint16_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x1E4)) - 1);
    *(uint16_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x1E4) = (uint16_t)(result);
    result = (v_stack_p90) + (16);
    v_stack_p60 = result;
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(result, Arg2, Arg3, Arg4);
    v_stack_p78 = result;
    result = 0;
    local_r10 = v_stack_p60;
    if (!(condition_is_equal)) {
        Arg4 = v_stack_p60;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = v_stack_p60;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, Arg4);
        Arg1 = v_stack_p78;
        local_r10 = v_stack_p60;
        Arg2 = 17;
    }
    if (Arg1 != NULL) {
        *(uint8_t *)(arg1 + 0xA) = 1;
    }
    if (0 == 0) goto loc_008A8737;
    if ((*(uint64_t *)(0)) == 0) goto loc_008A8737;
    result = ObfDereferenceObject(v_stack_p58, Arg2, Arg3, Arg4);
    v_stack_p80 = *(uint64_t *)(0);
    result = ObfReferenceObject(*(uint64_t *)(0), Arg2, Arg3, Arg4);
    v_stack_p58 = *(uint64_t *)(0);
    Arg2 = (v_stack_p70) + (8);
    v_stack_pC0 = Arg2;
    Arg1 = (v_stack_p50) - (*(uint16_t *)(arg2));
    v_stack_p50 = Arg1;
    if (Arg1 <= (Arg2 + 16)) goto loc_008A87B9;
    result = memcpy(Arg1, *(uint64_t *)(arg2 + 0x8), *(uint16_t *)(arg2), Arg4);
    result = 17;
    if (Arg1 != (Arg2 + 16)) {
        Arg1 = v_stack_p60;
        result = ExfReleasePushLockShared(Arg1, *(uint64_t *)(arg2 + 0x8), *(uint16_t *)(arg2), Arg4);
    }
    result = KeAbPostRelease(v_stack_p60, *(uint64_t *)(arg2 + 0x8), *(uint16_t *)(arg2), Arg4);
    v_stack_p110 = *(uint64_t *)(gs_base + (0 + 0x188));
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), *(uint64_t *)(arg2 + 0x8), *(uint16_t *)(arg2), Arg4);
    goto loc_008A8520;
loc_008A86BD:
loc_008A86C6:
    v_stack_p50 = v_stack_p50 - 2;
    *(uint16_t *)(v_stack_p50 - 0x2) = 92;
    result = (uint16_t)((v_stack_p68) - ((uint16_t)(v_stack_p50 - 2)));
    result = (uint16_t)((result) + ((uint16_t)(Arg2)));
    v_stack_pBC = (uint32_t)((uint16_t)(result));
    *(uint16_t *)(arg2 + 0x2) = (uint16_t)((uint16_t)(result));
    *(uint16_t *)(arg2) = (uint16_t)((uint16_t)(result) - 2);
    *(void **)(arg2 + 0x8) = Arg2 + 16;
    if ((Arg2 + 16) == (v_stack_p50 - 2)) goto loc_008A880E;
    result = memcpy(Arg2 + 16, v_stack_p50 - 2, (uint32_t)((uint32_t)((uint16_t)(result))), Arg2 + 16);
    *(uint32_t *)(arg4) = (uint32_t)((uint16_t)(result) + 16);
    goto loc_008A880E;
loc_008A871D:
    result = (uint32_t)(((uint16_t)(result) + 16) & (3));
    local_rbx = ((uint16_t)(result)) - (*(uint8_t *)(result + v_rip - 0x8A8727 * 1 + 0xF0FF80));
    goto loc_008A858B;
loc_008A8737:
    if (condition_is_not_equal) goto loc_008A87F7;
loc_008A8745:
    result = KeAbPostRelease(local_r10, v_stack_p50 - 2, (uint32_t)((uint32_t)((uint16_t)(result))), Arg2 + 16);
    v_stack_p118 = *(uint64_t *)(gs_base + (0 + 0x188));
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), v_stack_p50 - 2, (uint32_t)((uint32_t)((uint16_t)(result))), Arg2 + 16);
    Arg1 = (v_stack_p50) + (-6);
    v_stack_p50 = Arg1;
    if (Arg1 < (Arg2 + 16)) {
        Arg1 = Arg2 + 16;
        v_stack_p50 = Arg1;
        Arg3 = Arg2 + 16;
        Arg2 = Arg2 + 16;
    }
    *(uint32_t *)(arg1) = (uint32_t)(*(uint64_t *)(v_rip + 0x258CBB));
    *(uint16_t *)(arg1 + 0x4) = (uint16_t)(*(uint16_t *)(v_rip + 0x258CB6));
    if (Arg3 != (Arg2 + 16)) goto loc_008A86C6;
    v_stack_p50 = Arg2 + 2;
    goto loc_008A86C6;
loc_008A87B9:
    v_stack_p41 = 1;
    result = 17;
    if (Arg3 != (Arg2 + 16)) {
        Arg1 = v_stack_p60;
        result = ExfReleasePushLockShared(Arg1, Arg2, Arg3, Arg2 + 16);
    }
    result = KeAbPostRelease(v_stack_p60, Arg2, Arg3, Arg2 + 16);
    v_stack_p108 = *(uint64_t *)(gs_base + (0 + 0x188));
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, Arg3, Arg2 + 16);
    goto loc_008A880E;
loc_008A87F7:
    result = ExfReleasePushLockShared(local_r10, Arg2, Arg3, Arg2 + 16);
    goto loc_008A8745;
loc_008A8809:
    v_stack_p41 = 1;
loc_008A880E:
    goto loc_008A8849;
loc_008A8849:
    if (v_stack_p58 != 0) {
        result = ObfDereferenceObject(v_stack_p58, Arg2, Arg3, Arg2 + 16);
    }
    if (v_stack_p41 != 0) goto loc_008A887F;
loc_008A885F:
    v_stack_p44 = 0;
    goto loc_008A7FC9;
loc_008A8869:
    result = (uint32_t)((result) & (3));
    local_rbx = (Arg1 - 48) - (*(uint8_t *)(result + v_rip - 0x8A8815 * 1 + 0xF0FF80));
    goto loc_008A83EB;
loc_008A887F:
    if ((((uint8_t)(*(uint8_t *)(arg1 - 0x30 + 0x1A))) & (2)) != 0) goto loc_008A88A5;
    v_stack_p98 = 0;
    v_stack_p41 = 0;
loc_008A8898:
    goto loc_008A8044;
loc_008A88A5:
    result = (uint32_t)((v_stack_p88) & (3));
    local_rbx = (Arg1 - 48) - (*(uint8_t *)(result + 0x0 * 1 + 0xF0FF80));
    v_stack_p98 = local_rbx;
    v_stack_p41 = 0;
    goto loc_008A8044;
loc_008A88D0:
    *(uint32_t *)(arg4) = 16;
    goto loc_008A88EB;
loc_008A88EB:
    if (v_stack_p170 < 16) goto loc_008A8916;
    *(uint32_t *)(arg2) = 0;
    *(uint64_t *)(arg2 + 0x8) = 0;
    goto loc_008A885F;
loc_008A8916:
    v_stack_p44 = 0xC0000004ULL;
    goto loc_008A7FD5;
loc_008A8923:
    if ((*(uint16_t *)(local_rbx + 0x8)) == 0) goto loc_008A7F91;
    goto loc_008A7F93;
loc_008A8935:
    v_stack_p28 = Arg5;
    v_stack_p20 = Arg4;
    result = guard_dispatch_icall(Arg1, 1, Arg3, Arg2 + 16);
    goto loc_008A7FBE;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `- 0x30` | `64` | `R` |
| `Arg1` | `+ 0x0` | `8` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x18` | `8` | `R` |
| `Arg1` | `+ 0x1A` | `64` | `R` |
| `Arg2` | `+ 0x0` | `16` | `W` |
| `Arg2` | `+ 0x0` | `32` | `W` |
| `Arg2` | `+ 0x2` | `16` | `W` |
| `Arg2` | `+ 0x4` | `32` | `W` |
| `Arg2` | `+ 0x8` | `64` | `W` |
| `Arg2` | `+ 0x10` | `64` | `R` |
| `Arg4` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008A7ED0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
