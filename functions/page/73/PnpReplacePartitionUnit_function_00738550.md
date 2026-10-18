# PnpReplacePartitionUnit

- RVA: `0x00738550`–`0x00739030` (길이 `2,784` bytes)
- VA: `0x0000000140738550`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C3CE4`
- 디코드: `709`개 명령, `2,784/2,784` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **69**; 고유 호출 대상: **35**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x0073859F` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x007385B6` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x007385C0` → [KeQueryActiveProcessorCountEx](../../text/24/KeQueryActiveProcessorCountEx_function_00249EF0.md) (function, `0x00249EF0`)
- `0x007385E4` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (function, `0x0020E6B0`)
- `0x0073864E` → [PnprLogStartEvent](PnprLogStartEvent_function_0073A2AC.md) (function, `0x0073A2AC`)
- `0x00738663` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00738688` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x0073869D` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x007386B5` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x007386C9` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x007386F7` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00738709` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00738716` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00738754` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x0073877F` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x007387DC` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x0073880F` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00738827` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00738835` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x0073884A` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00738862` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00738876` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x007388A4` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x007388B6` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x007388C3` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00738901` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x0073892C` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00738989` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x007389BC` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x007389D4` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00738A6F` → [IoGetLegacyVetoList](../91/IoGetLegacyVetoList_function_00911300.md) (function, `0x00911300`)
- `0x00738A90` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00738ADE` → [PnprGetMillisecondCounter](../../pagelk/B6/PnprGetMillisecondCounter_function_00B63FD4.md) (function, `0x00B63FD4`)
- `0x00738AE9` → [PnprLockPagesForReplace](PnprLockPagesForReplace_function_0073A150.md) (function, `0x0073A150`)
- `0x00738AF2` → [PnprQuiesceDevices](../../pagelk/B6/PnprQuiesceDevices_function_00B649E4.md) (function, `0x00B649E4`)
- `0x00738AFB` → [PnprWakeDevices](../../pagelk/B6/PnprWakeDevices_function_00B65614.md) (function, `0x00B65614`)
- `0x00738B00` → [PnprUnlockPagesForReplace](PnprUnlockPagesForReplace_function_0073AA5C.md) (function, `0x0073AA5C`)
- `0x00738B1F` → [PnprIdentifyUnits](PnprIdentifyUnits_function_00739B0C.md) (function, `0x00739B0C`)
- `0x00738B6A` → [PnprCollectResources](PnprCollectResources_function_00739550.md) (function, `0x00739550`)
- `0x00738BC1` → [PnprLoadPluginDriver](PnprLoadPluginDriver_function_00739FC4.md) (function, `0x00739FC4`)
- `0x00738BD5` → [PnprQueryReplaceFeatures](../../text/5A/PnprQueryReplaceFeatures_function_005A8D08.md) (function, `0x005A8D08`)
- `0x00738C80` → [PnprMmConstruct](PnprMmConstruct_function_0073A770.md) (function, `0x0073A770`)
- `0x00738CC8` → [PnprAllocateMappingReserves](PnprAllocateMappingReserves_function_007393C4.md) (function, `0x007393C4`)
- `0x00738DA4` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00738DBA` → [KiCopyAffinityEx](../../text/2C/KiCopyAffinityEx_function_002CE860.md) (function, `0x002CE860`)
- `0x00738DF5` → [KeIsEmptyAffinityEx](../../text/2D/KeIsEmptyAffinityEx_function_002D1580.md) (function, `0x002D1580`)
- `0x00738E3C` → [KeCheckProcessorAffinityEx](../../text/30/KeCheckProcessorAffinityEx_function_00305150.md) (function, `0x00305150`)
- `0x00738E4F` → [KeFindFirstSetLeftAffinityEx](../../text/45/KeFindFirstSetLeftAffinityEx_function_004530E0.md) (function, `0x004530E0`)
- `0x00738E93` → [KeSetSystemGroupAffinityThread](../../text/39/KeSetSystemGroupAffinityThread_function_00399140.md) (function, `0x00399140`)
- `0x00738E98` → [PnprInitiateReplaceOperation](../../pagelk/B6/PnprInitiateReplaceOperation_function_00B64034.md) (function, `0x00B64034`)
- `0x00738EA4` → [KeRevertToUserGroupAffinityThread](../../text/39/KeRevertToUserGroupAffinityThread_function_00398EC0.md) (function, `0x00398EC0`)
- `0x00738EB5` → [PnprGetMillisecondCounter](../../pagelk/B6/PnprGetMillisecondCounter_function_00B63FD4.md) (function, `0x00B63FD4`)
- `0x00738EC0` → [PnprLogSuccessEvent](PnprLogSuccessEvent_function_0073A380.md) (function, `0x0073A380`)
- `0x00738ED1` → [PnprLogFailureEvent](PnprLogFailureEvent_function_0073A180.md) (function, `0x0073A180`)
- `0x00738EF7` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00738EFF` → [MmUnloadSystemImage](../AA/MmUnloadSystemImage_function_00AA2F60.md) (function, `0x00AA2F60`)
- `0x00738F28` → [PnprFreeMappingReserve](PnprFreeMappingReserve_function_0073989C.md) (function, `0x0073989C`)
- `0x00738F37` → [PnprFreeMappingReserve](PnprFreeMappingReserve_function_0073989C.md) (function, `0x0073989C`)
- `0x00738F51` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00738F62` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00738F6E` → [PnprMmFree](PnprMmFree_function_0073A874.md) (function, `0x0073A874`)
- `0x00738F81` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00738F98` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00738FAF` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00738FC6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00738FD7` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00738FE8` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x00738FFA` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x00739009` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [IoReplacePartitionUnit](../72/IoReplacePartitionUnit_function_00727FD0.md) at `0x0072803F`

### Static image references
- `0x00738576` → RVA `0x00E0A740` (`.data`; read)
- `0x007385C8` → RVA `0x00F8AC20` (`.data`; read)
- `0x00738A04` → RVA `0x00FC6AA4` (`ALMOSTRO`; read)
- `0x00738A0B` → RVA `0x00F8AC38` (`.data`; write)
- `0x00738A9A` → RVA `0x00F8AC38` (`.data`; read)
- `0x00738DAE` → RVA `0x00FC7120` (`ALMOSTRO`; read)
- `0x00738E61` → RVA `0x00F231B0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **54**
  - `0x0073859F` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x007385B6` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x007385C0` → [KeQueryActiveProcessorCountEx](../../text/24/KeQueryActiveProcessorCountEx_function_00249EF0.md) (`PAGE` → `.text`)
  - `0x007385E4` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (`PAGE` → `.text`)
  - `0x00738663` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00738688` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x0073869D` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x007386B5` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x007386C9` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x007386F7` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00738709` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00738716` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00738754` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x0073877F` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x007387DC` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x0073880F` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00738827` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x00738835` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x0073884A` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00738862` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00738876` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x007388A4` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x007388B6` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x007388C3` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00738901` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x0073892C` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00738989` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x007389BC` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x007389D4` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x00738A90` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00738ADE` → [PnprGetMillisecondCounter](../../pagelk/B6/PnprGetMillisecondCounter_function_00B63FD4.md) (`PAGE` → `PAGELK`)
  - `0x00738AF2` → [PnprQuiesceDevices](../../pagelk/B6/PnprQuiesceDevices_function_00B649E4.md) (`PAGE` → `PAGELK`)
  - `0x00738AFB` → [PnprWakeDevices](../../pagelk/B6/PnprWakeDevices_function_00B65614.md) (`PAGE` → `PAGELK`)
  - `0x00738BD5` → [PnprQueryReplaceFeatures](../../text/5A/PnprQueryReplaceFeatures_function_005A8D08.md) (`PAGE` → `.text`)
  - `0x00738DA4` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00738DBA` → [KiCopyAffinityEx](../../text/2C/KiCopyAffinityEx_function_002CE860.md) (`PAGE` → `.text`)
  - `0x00738DF5` → [KeIsEmptyAffinityEx](../../text/2D/KeIsEmptyAffinityEx_function_002D1580.md) (`PAGE` → `.text`)
  - `0x00738E3C` → [KeCheckProcessorAffinityEx](../../text/30/KeCheckProcessorAffinityEx_function_00305150.md) (`PAGE` → `.text`)
  - `0x00738E4F` → [KeFindFirstSetLeftAffinityEx](../../text/45/KeFindFirstSetLeftAffinityEx_function_004530E0.md) (`PAGE` → `.text`)
  - `0x00738E93` → [KeSetSystemGroupAffinityThread](../../text/39/KeSetSystemGroupAffinityThread_function_00399140.md) (`PAGE` → `.text`)
  - `0x00738E98` → [PnprInitiateReplaceOperation](../../pagelk/B6/PnprInitiateReplaceOperation_function_00B64034.md) (`PAGE` → `PAGELK`)
  - `0x00738EA4` → [KeRevertToUserGroupAffinityThread](../../text/39/KeRevertToUserGroupAffinityThread_function_00398EC0.md) (`PAGE` → `.text`)
  - `0x00738EB5` → [PnprGetMillisecondCounter](../../pagelk/B6/PnprGetMillisecondCounter_function_00B63FD4.md) (`PAGE` → `PAGELK`)
  - `0x00738EF7` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00738F51` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00738F62` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00738F81` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00738F98` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00738FAF` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00738FC6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00738FD7` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00738FE8` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (`PAGE` → `.text`)
  - `0x00738FFA` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (`PAGE` → `.text`)
  - `0x00739009` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00738550  48 8B C4                        mov rax, rsp
00738553  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00738557  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0073855B  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
0073855F  55                              push rbp
00738560  41 54                           push r12
00738562  41 55                           push r13
00738564  41 56                           push r14
00738566  41 57                           push r15
00738568  48 8D A8 08 FF FF FF            lea rbp, [rax - 0xf8]
0073856F  48 81 EC D0 01 00 00            sub rsp, 0x1d0
00738576  48 8B 05 C3 21 6D 00            mov rax, qword ptr [rip + 0x6d21c3]
0073857D  48 33 C4                        xor rax, rsp
00738580  48 89 85 C0 00 00 00            mov qword ptr [rbp + 0xc0], rax
00738587  4C 8B F1                        mov r14, rcx
0073858A  0F 57 C0                        xorps xmm0, xmm0
0073858D  48 8D 4C 24 68                  lea rcx, [rsp + 0x68]
00738592  33 D2                           xor edx, edx
00738594  41 B8 00 01 00 00               mov r8d, 0x100
0073859A  0F 11 44 24 40                  movups xmmword ptr [rsp + 0x40], xmm0
0073859F  E8 9C E6 F8 FF                  call 0x1406c6c40
007385A4  33 D2                           xor edx, edx
007385A6  48 8D 4D 70                     lea rcx, [rbp + 0x70]
007385AA  0F 57 C0                        xorps xmm0, xmm0
007385AD  0F 11 44 24 50                  movups xmmword ptr [rsp + 0x50], xmm0
007385B2  44 8D 42 50                     lea r8d, [rdx + 0x50]
007385B6  E8 85 E6 F8 FF                  call 0x1406c6c40
007385BB  B9 FF FF 00 00                  mov ecx, 0xffff
007385C0  E8 2B 19 B1 FF                  call 0x140249ef0
007385C5  44 8B F8                        mov r15d, eax
007385C8  48 8D 0D 51 26 85 00            lea rcx, [rip + 0x852651]
007385CF  45 33 ED                        xor r13d, r13d
007385D2  44 89 7C 24 30                  mov dword ptr [rsp + 0x30], r15d
007385D7  45 33 C9                        xor r9d, r9d
007385DA  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
007385DF  45 33 C0                        xor r8d, r8d
007385E2  33 D2                           xor edx, edx
007385E4  E8 C7 60 AD FF                  call 0x14020e6b0
007385E9  49 8D 7E 08                     lea rdi, [r14 + 8]
007385ED  45 39 6E 10                     cmp dword ptr [r14 + 0x10], r13d
007385F1  7C 60                           jl 0x140738653
007385F3  4C 8B 07                        mov r8, qword ptr [rdi]
007385F6  41 8D 75 02                     lea esi, [r13 + 2]
007385FA  4D 85 C0                        test r8, r8
007385FD  0F 84 BE 03 00 00               je 0x1407389c1
00738603  49 8B 80 38 01 00 00            mov rax, qword ptr [r8 + 0x138]
0073860A  48 8B 40 28                     mov rax, qword ptr [rax + 0x28]
0073860E  48 85 C0                        test rax, rax
00738611  0F 84 16 02 00 00               je 0x14073882d
00738617  0F BA A0 8C 01 00 00 11         bt dword ptr [rax + 0x18c], 0x11
0073861F  0F 82 08 02 00 00               jb 0x14073882d
00738625  49 8B 0E                        mov rcx, qword ptr [r14]
00738628  48 85 C9                        test rcx, rcx
0073862B  0F 84 E3 01 00 00               je 0x140738814
00738631  48 8B 81 38 01 00 00            mov rax, qword ptr [rcx + 0x138]
00738638  48 8B 40 28                     mov rax, qword ptr [rax + 0x28]
0073863C  48 85 C0                        test rax, rax
0073863F  74 43                           je 0x140738684
00738641  0F BA A0 8C 01 00 00 11         bt dword ptr [rax + 0x18c], 0x11
00738649  72 39                           jb 0x140738684
0073864B  49 8B D0                        mov rdx, r8
0073864E  E8 59 1C 00 00                  call 0x14073a2ac
00738653  BA 48 82 00 00                  mov edx, 0x8248
00738658  B9 40 00 00 00                  mov ecx, 0x40
0073865D  41 B8 50 6E 70 51               mov r8d, 0x51706e50
00738663  E8 88 9A 44 00                  call 0x140b820f0
00738668  48 8B D8                        mov rbx, rax
0073866B  41 BC 01 00 00 00               mov r12d, 1
00738671  48 85 C0                        test rax, rax
00738674  0F 85 60 03 00 00               jne 0x1407389da
0073867A  BF 9A 00 00 C0                  mov edi, 0xc000009a
0073867F  E9 25 08 00 00                  jmp 0x140738ea9
00738684  0F B7 51 02                     movzx edx, word ptr [rcx + 2]
00738688  E8 E7 FC CE FF                  call 0x140428374
0073868D  49 8B 06                        mov rax, qword ptr [r14]
00738690  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
00738694  48 85 C9                        test rcx, rcx
00738697  74 35                           je 0x1407386ce
00738699  0F BF 51 02                     movsx edx, word ptr [rcx + 2]
0073869D  E8 D2 FC CE FF                  call 0x140428374
007386A2  49 8B 06                        mov rax, qword ptr [r14]
007386A5  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
007386A9  48 83 C1 38                     add rcx, 0x38
007386AD  66 44 39 29                     cmp word ptr [rcx], r13w
007386B1  74 1B                           je 0x1407386ce
007386B3  8B D6                           mov edx, esi
007386B5  E8 BA FC CE FF                  call 0x140428374
007386BA  49 8B 06                        mov rax, qword ptr [r14]
007386BD  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
007386C1  0F B7 51 38                     movzx edx, word ptr [rcx + 0x38]
007386C5  48 8B 49 40                     mov rcx, qword ptr [rcx + 0x40]
007386C9  E8 A6 FC CE FF                  call 0x140428374
007386CE  49 8B 0E                        mov rcx, qword ptr [r14]
007386D1  48 85 C9                        test rcx, rcx
007386D4  0F 84 3A 01 00 00               je 0x140738814
007386DA  48 8B 81 38 01 00 00            mov rax, qword ptr [rcx + 0x138]
007386E1  4C 39 68 28                     cmp qword ptr [rax + 0x28], r13
007386E5  0F 84 29 01 00 00               je 0x140738814
007386EB  48 8B 58 28                     mov rbx, qword ptr [rax + 0x28]
007386EF  BA 88 03 00 00                  mov edx, 0x388
007386F4  48 8B CB                        mov rcx, rbx
007386F7  E8 78 FC CE FF                  call 0x140428374
007386FC  66 44 39 6B 28                  cmp word ptr [rbx + 0x28], r13w
00738701  74 18                           je 0x14073871b
00738703  8B D6                           mov edx, esi
00738705  48 8D 4B 28                     lea rcx, [rbx + 0x28]
00738709  E8 66 FC CE FF                  call 0x140428374
0073870E  0F B7 53 28                     movzx edx, word ptr [rbx + 0x28]
00738712  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00738716  E8 59 FC CE FF                  call 0x140428374
0073871B  49 8B 16                        mov rdx, qword ptr [r14]
0073871E  48 8D 8A 38 01 00 00            lea rcx, [rdx + 0x138]
00738725  48 85 D2                        test rdx, rdx
00738728  74 09                           je 0x140738733
0073872A  48 8B 01                        mov rax, qword ptr [rcx]
0073872D  4C 8B 40 28                     mov r8, qword ptr [rax + 0x28]
00738731  EB 03                           jmp 0x140738736
00738733  4D 8B C5                        mov r8, r13
00738736  66 45 39 68 38                  cmp word ptr [r8 + 0x38], r13w
0073873B  74 47                           je 0x140738784
0073873D  48 85 D2                        test rdx, rdx
00738740  74 09                           je 0x14073874b
00738742  48 8B 01                        mov rax, qword ptr [rcx]
00738745  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
00738749  EB 03                           jmp 0x14073874e
0073874B  49 8B CD                        mov rcx, r13
0073874E  48 83 C1 38                     add rcx, 0x38
00738752  8B D6                           mov edx, esi
00738754  E8 1B FC CE FF                  call 0x140428374
00738759  49 8B 0E                        mov rcx, qword ptr [r14]
0073875C  48 85 C9                        test rcx, rcx
0073875F  74 10                           je 0x140738771
00738761  48 8B 81 38 01 00 00            mov rax, qword ptr [rcx + 0x138]
00738768  48 8B 50 28                     mov rdx, qword ptr [rax + 0x28]
0073876C  48 8B CA                        mov rcx, rdx
0073876F  EB 06                           jmp 0x140738777
00738771  49 8B D5                        mov rdx, r13
00738774  49 8B CD                        mov rcx, r13
00738777  0F B7 52 38                     movzx edx, word ptr [rdx + 0x38]
0073877B  48 8B 49 40                     mov rcx, qword ptr [rcx + 0x40]
0073877F  E8 F0 FB CE FF                  call 0x140428374
00738784  49 8B 16                        mov rdx, qword ptr [r14]
00738787  48 8D 8A 38 01 00 00            lea rcx, [rdx + 0x138]
0073878E  48 85 D2                        test rdx, rdx
00738791  74 09                           je 0x14073879c
00738793  48 8B 01                        mov rax, qword ptr [rcx]
00738796  4C 8B 40 28                     mov r8, qword ptr [rax + 0x28]
0073879A  EB 03                           jmp 0x14073879f
0073879C  4D 8B C5                        mov r8, r13
0073879F  4D 39 68 10                     cmp qword ptr [r8 + 0x10], r13
007387A3  74 6F                           je 0x140738814
007387A5  48 85 D2                        test rdx, rdx
007387A8  74 09                           je 0x1407387b3
007387AA  48 8B 01                        mov rax, qword ptr [rcx]
007387AD  48 8B 40 28                     mov rax, qword ptr [rax + 0x28]
007387B1  EB 03                           jmp 0x1407387b6
007387B3  49 8B C5                        mov rax, r13
007387B6  48 8B 40 10                     mov rax, qword ptr [rax + 0x10]
007387BA  66 44 39 68 38                  cmp word ptr [rax + 0x38], r13w
007387BF  74 53                           je 0x140738814
007387C1  48 85 D2                        test rdx, rdx
007387C4  74 09                           je 0x1407387cf
007387C6  48 8B 01                        mov rax, qword ptr [rcx]
007387C9  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
007387CD  EB 03                           jmp 0x1407387d2
007387CF  49 8B CD                        mov rcx, r13
007387D2  48 8B 49 10                     mov rcx, qword ptr [rcx + 0x10]
007387D6  8B D6                           mov edx, esi
007387D8  48 83 C1 38                     add rcx, 0x38
007387DC  E8 93 FB CE FF                  call 0x140428374
007387E1  49 8B 0E                        mov rcx, qword ptr [r14]
007387E4  48 85 C9                        test rcx, rcx
007387E7  74 10                           je 0x1407387f9
007387E9  48 8B 81 38 01 00 00            mov rax, qword ptr [rcx + 0x138]
007387F0  48 8B 50 28                     mov rdx, qword ptr [rax + 0x28]
007387F4  48 8B CA                        mov rcx, rdx
007387F7  EB 06                           jmp 0x1407387ff
007387F9  49 8B D5                        mov rdx, r13
007387FC  49 8B CD                        mov rcx, r13
007387FF  48 8B 42 10                     mov rax, qword ptr [rdx + 0x10]
00738803  48 8B 49 10                     mov rcx, qword ptr [rcx + 0x10]
00738807  0F B7 50 38                     movzx edx, word ptr [rax + 0x38]
0073880B  48 8B 49 40                     mov rcx, qword ptr [rcx + 0x40]
0073880F  E8 60 FB CE FF                  call 0x140428374
00738814  4D 8B 06                        mov r8, qword ptr [r14]
00738817  45 33 C9                        xor r9d, r9d
0073881A  48 8B D6                        mov rdx, rsi
0073881D  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00738822  B9 CA 00 00 00                  mov ecx, 0xca
00738827  E8 34 4E DC FF                  call 0x1404fd660
0073882C  CC                              int3
0073882D  41 0F B7 50 02                  movzx edx, word ptr [r8 + 2]
00738832  49 8B C8                        mov rcx, r8
00738835  E8 3A FB CE FF                  call 0x140428374
0073883A  48 8B 07                        mov rax, qword ptr [rdi]
0073883D  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
00738841  48 85 C9                        test rcx, rcx
00738844  74 35                           je 0x14073887b
00738846  0F BF 51 02                     movsx edx, word ptr [rcx + 2]
0073884A  E8 25 FB CE FF                  call 0x140428374
0073884F  48 8B 07                        mov rax, qword ptr [rdi]
00738852  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
00738856  48 83 C1 38                     add rcx, 0x38
0073885A  66 44 39 29                     cmp word ptr [rcx], r13w
0073885E  74 1B                           je 0x14073887b
00738860  8B D6                           mov edx, esi
00738862  E8 0D FB CE FF                  call 0x140428374
00738867  48 8B 07                        mov rax, qword ptr [rdi]
0073886A  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
0073886E  0F B7 51 38                     movzx edx, word ptr [rcx + 0x38]
00738872  48 8B 49 40                     mov rcx, qword ptr [rcx + 0x40]
00738876  E8 F9 FA CE FF                  call 0x140428374
0073887B  48 8B 0F                        mov rcx, qword ptr [rdi]
0073887E  48 85 C9                        test rcx, rcx
00738881  0F 84 3A 01 00 00               je 0x1407389c1
00738887  48 8B 81 38 01 00 00            mov rax, qword ptr [rcx + 0x138]
0073888E  4C 39 68 28                     cmp qword ptr [rax + 0x28], r13
00738892  0F 84 29 01 00 00               je 0x1407389c1
00738898  48 8B 58 28                     mov rbx, qword ptr [rax + 0x28]
0073889C  BA 88 03 00 00                  mov edx, 0x388
007388A1  48 8B CB                        mov rcx, rbx
007388A4  E8 CB FA CE FF                  call 0x140428374
007388A9  66 44 39 6B 28                  cmp word ptr [rbx + 0x28], r13w
007388AE  74 18                           je 0x1407388c8
007388B0  8B D6                           mov edx, esi
007388B2  48 8D 4B 28                     lea rcx, [rbx + 0x28]
007388B6  E8 B9 FA CE FF                  call 0x140428374
007388BB  0F B7 53 28                     movzx edx, word ptr [rbx + 0x28]
007388BF  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
007388C3  E8 AC FA CE FF                  call 0x140428374
007388C8  48 8B 17                        mov rdx, qword ptr [rdi]
007388CB  48 8D 8A 38 01 00 00            lea rcx, [rdx + 0x138]
007388D2  48 85 D2                        test rdx, rdx
007388D5  74 09                           je 0x1407388e0
007388D7  48 8B 01                        mov rax, qword ptr [rcx]
007388DA  4C 8B 40 28                     mov r8, qword ptr [rax + 0x28]
007388DE  EB 03                           jmp 0x1407388e3
007388E0  4D 8B C5                        mov r8, r13
007388E3  66 45 39 68 38                  cmp word ptr [r8 + 0x38], r13w
007388E8  74 47                           je 0x140738931
007388EA  48 85 D2                        test rdx, rdx
007388ED  74 09                           je 0x1407388f8
007388EF  48 8B 01                        mov rax, qword ptr [rcx]
007388F2  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
007388F6  EB 03                           jmp 0x1407388fb
007388F8  49 8B CD                        mov rcx, r13
007388FB  48 83 C1 38                     add rcx, 0x38
007388FF  8B D6                           mov edx, esi
00738901  E8 6E FA CE FF                  call 0x140428374
00738906  48 8B 0F                        mov rcx, qword ptr [rdi]
00738909  48 85 C9                        test rcx, rcx
0073890C  74 10                           je 0x14073891e
0073890E  48 8B 81 38 01 00 00            mov rax, qword ptr [rcx + 0x138]
00738915  48 8B 50 28                     mov rdx, qword ptr [rax + 0x28]
00738919  48 8B CA                        mov rcx, rdx
0073891C  EB 06                           jmp 0x140738924
0073891E  49 8B D5                        mov rdx, r13
00738921  49 8B CD                        mov rcx, r13
00738924  0F B7 52 38                     movzx edx, word ptr [rdx + 0x38]
00738928  48 8B 49 40                     mov rcx, qword ptr [rcx + 0x40]
0073892C  E8 43 FA CE FF                  call 0x140428374
00738931  48 8B 17                        mov rdx, qword ptr [rdi]
00738934  48 8D 8A 38 01 00 00            lea rcx, [rdx + 0x138]
0073893B  48 85 D2                        test rdx, rdx
0073893E  74 09                           je 0x140738949
00738940  48 8B 01                        mov rax, qword ptr [rcx]
00738943  4C 8B 40 28                     mov r8, qword ptr [rax + 0x28]
00738947  EB 03                           jmp 0x14073894c
00738949  4D 8B C5                        mov r8, r13
0073894C  4D 39 68 10                     cmp qword ptr [r8 + 0x10], r13
00738950  74 6F                           je 0x1407389c1
00738952  48 85 D2                        test rdx, rdx
00738955  74 09                           je 0x140738960
00738957  48 8B 01                        mov rax, qword ptr [rcx]
0073895A  48 8B 40 28                     mov rax, qword ptr [rax + 0x28]
0073895E  EB 03                           jmp 0x140738963
00738960  49 8B C5                        mov rax, r13
00738963  48 8B 40 10                     mov rax, qword ptr [rax + 0x10]
00738967  66 44 39 68 38                  cmp word ptr [rax + 0x38], r13w
0073896C  74 53                           je 0x1407389c1
0073896E  48 85 D2                        test rdx, rdx
00738971  74 09                           je 0x14073897c
00738973  48 8B 01                        mov rax, qword ptr [rcx]
00738976  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
0073897A  EB 03                           jmp 0x14073897f
0073897C  49 8B CD                        mov rcx, r13
0073897F  48 8B 49 10                     mov rcx, qword ptr [rcx + 0x10]
00738983  8B D6                           mov edx, esi
00738985  48 83 C1 38                     add rcx, 0x38
00738989  E8 E6 F9 CE FF                  call 0x140428374
0073898E  48 8B 0F                        mov rcx, qword ptr [rdi]
00738991  48 85 C9                        test rcx, rcx
00738994  74 10                           je 0x1407389a6
00738996  48 8B 81 38 01 00 00            mov rax, qword ptr [rcx + 0x138]
0073899D  48 8B 50 28                     mov rdx, qword ptr [rax + 0x28]
007389A1  48 8B CA                        mov rcx, rdx
007389A4  EB 06                           jmp 0x1407389ac
007389A6  49 8B D5                        mov rdx, r13
007389A9  49 8B CD                        mov rcx, r13
007389AC  48 8B 42 10                     mov rax, qword ptr [rdx + 0x10]
007389B0  48 8B 49 10                     mov rcx, qword ptr [rcx + 0x10]
007389B4  0F B7 50 38                     movzx edx, word ptr [rax + 0x38]
007389B8  48 8B 49 40                     mov rcx, qword ptr [rcx + 0x40]
007389BC  E8 B3 F9 CE FF                  call 0x140428374
007389C1  4C 8B 07                        mov r8, qword ptr [rdi]
007389C4  45 33 C9                        xor r9d, r9d
007389C7  48 8B D6                        mov rdx, rsi
007389CA  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
007389CF  B9 CA 00 00 00                  mov ecx, 0xca
007389D4  E8 87 4C DC FF                  call 0x1404fd660
007389D9  CC                              int3
007389DA  49 8B 06                        mov rax, qword ptr [r14]
007389DD  4C 8D A3 98 00 00 00            lea r12, [rbx + 0x98]
007389E4  48 89 03                        mov qword ptr [rbx], rax
007389E7  4C 8D 6B 20                     lea r13, [rbx + 0x20]
007389EB  48 8B 07                        mov rax, qword ptr [rdi]
007389EE  33 F6                           xor esi, esi
007389F0  49 89 45 00                     mov qword ptr [r13], rax
007389F4  41 8B 46 10                     mov eax, dword ptr [r14 + 0x10]
007389F8  89 43 40                        mov dword ptr [rbx + 0x40], eax
007389FB  4D 89 64 24 08                  mov qword ptr [r12 + 8], r12
00738A00  4D 89 24 24                     mov qword ptr [r12], r12
00738A04  40 38 35 99 E0 88 00            cmp byte ptr [rip + 0x88e099], sil
00738A0B  48 89 1D 26 22 85 00            mov qword ptr [rip + 0x852226], rbx
00738A12  75 44                           jne 0x140738a58
00738A14  41 39 76 10                     cmp dword ptr [r14 + 0x10], esi
00738A18  7C 3E                           jl 0x140738a58
00738A1A  8B 83 08 82 00 00               mov eax, dword ptr [rbx + 0x8208]
00738A20  45 33 ED                        xor r13d, r13d
00738A23  85 C0                           test eax, eax
00738A25  B9 AA 00 00 00                  mov ecx, 0xaa
00738A2A  0F 44 C1                        cmove eax, ecx
00738A2D  89 83 08 82 00 00               mov dword ptr [rbx + 0x8208], eax
00738A33  41 8D 75 02                     lea esi, [r13 + 2]
00738A37  8B 83 0C 82 00 00               mov eax, dword ptr [rbx + 0x820c]
00738A3D  85 C0                           test eax, eax
00738A3F  0F 44 C6                        cmove eax, esi
00738A42  89 83 0C 82 00 00               mov dword ptr [rbx + 0x820c], eax
00738A48  BF BB 00 00 C0                  mov edi, 0xc00000bb
00738A4D  41 BC 01 00 00 00               mov r12d, 1
00738A53  E9 51 04 00 00                  jmp 0x140738ea9
00738A58  48 8D 54 24 34                  lea rdx, [rsp + 0x34]
00738A5D  89 74 24 34                     mov dword ptr [rsp + 0x34], esi
00738A61  48 8D 4C 24 38                  lea rcx, [rsp + 0x38]
00738A66  48 89 74 24 38                  mov qword ptr [rsp + 0x38], rsi
00738A6B  40 0F B6 FE                     movzx edi, sil
00738A6F  E8 8C 88 1D 00                  call 0x140911300
00738A74  85 C0                           test eax, eax
00738A76  78 0C                           js 0x140738a84
00738A78  39 74 24 34                     cmp dword ptr [rsp + 0x34], esi
00738A7C  BA 01 00 00 00                  mov edx, 1
00738A81  0F 45 FA                        cmovne edi, edx
00738A84  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
00738A89  48 85 C9                        test rcx, rcx
00738A8C  74 07                           je 0x140738a95
00738A8E  33 D2                           xor edx, edx
00738A90  E8 DB 9D 44 00                  call 0x140b82870
00738A95  40 84 FF                        test dil, dil
00738A98  74 3F                           je 0x140738ad9
00738A9A  48 8B 0D 97 21 85 00            mov rcx, qword ptr [rip + 0x852197]
00738AA1  45 33 ED                        xor r13d, r13d
00738AA4  BA B6 00 00 00                  mov edx, 0xb6
00738AA9  BF CB 00 00 C0                  mov edi, 0xc00000cb
00738AAE  8B 81 08 82 00 00               mov eax, dword ptr [rcx + 0x8208]
00738AB4  85 C0                           test eax, eax
00738AB6  0F 44 C2                        cmove eax, edx
00738AB9  41 8D 55 07                     lea edx, [r13 + 7]
00738ABD  89 81 08 82 00 00               mov dword ptr [rcx + 0x8208], eax
00738AC3  8B 81 0C 82 00 00               mov eax, dword ptr [rcx + 0x820c]
00738AC9  85 C0                           test eax, eax
00738ACB  0F 44 C2                        cmove eax, edx
00738ACE  89 81 0C 82 00 00               mov dword ptr [rcx + 0x820c], eax
00738AD4  E9 74 FF FF FF                  jmp 0x140738a4d
00738AD9  B9 01 00 00 00                  mov ecx, 1
00738ADE  E8 F1 B4 42 00                  call 0x140b63fd4
00738AE3  41 39 76 10                     cmp dword ptr [r14 + 0x10], esi
00738AE7  7D 27                           jge 0x140738b10
00738AE9  E8 62 16 00 00                  call 0x14073a150
00738AEE  48 8D 4D 70                     lea rcx, [rbp + 0x70]
00738AF2  E8 ED BE 42 00                  call 0x140b649e4
00738AF7  48 8D 4D 70                     lea rcx, [rbp + 0x70]
00738AFB  E8 14 CB 42 00                  call 0x140b65614
00738B00  E8 57 1F 00 00                  call 0x14073aa5c
00738B05  45 33 ED                        xor r13d, r13d
00738B08  41 8B FD                        mov edi, r13d
00738B0B  E9 3D FF FF FF                  jmp 0x140738a4d
00738B10  48 8B 53 20                     mov rdx, qword ptr [rbx + 0x20]
00738B14  4C 8D 4B 28                     lea r9, [rbx + 0x28]
00738B18  48 8B 0B                        mov rcx, qword ptr [rbx]
00738B1B  4C 8D 43 08                     lea r8, [rbx + 8]
00738B1F  E8 E8 0F 00 00                  call 0x140739b0c
00738B24  8B F8                           mov edi, eax
00738B26  85 C0                           test eax, eax
00738B28  79 3A                           jns 0x140738b64
00738B2A  48 8B 15 07 21 85 00            mov rdx, qword ptr [rip + 0x852107]
00738B31  45 33 ED                        xor r13d, r13d
00738B34  B8 DB 00 00 00                  mov eax, 0xdb
00738B39  8B 8A 08 82 00 00               mov ecx, dword ptr [rdx + 0x8208]
00738B3F  85 C9                           test ecx, ecx
00738B41  0F 44 C8                        cmove ecx, eax
00738B44  8B 82 0C 82 00 00               mov eax, dword ptr [rdx + 0x820c]
00738B4A  89 8A 08 82 00 00               mov dword ptr [rdx + 0x8208], ecx
00738B50  85 C0                           test eax, eax
00738B52  41 8D 4D 03                     lea ecx, [r13 + 3]
00738B56  0F 44 C1                        cmove eax, ecx
00738B59  89 82 0C 82 00 00               mov dword ptr [rdx + 0x820c], eax
00738B5F  E9 E9 FE FF FF                  jmp 0x140738a4d
00738B64  49 8B D5                        mov rdx, r13
00738B67  48 8B CB                        mov rcx, rbx
00738B6A  E8 E1 09 00 00                  call 0x140739550
00738B6F  8B F8                           mov edi, eax
00738B71  85 C0                           test eax, eax
00738B73  79 3B                           jns 0x140738bb0
00738B75  48 8B 0D BC 20 85 00            mov rcx, qword ptr [rip + 0x8520bc]
00738B7C  45 33 ED                        xor r13d, r13d
00738B7F  BA E8 00 00 00                  mov edx, 0xe8
00738B84  8B 81 08 82 00 00               mov eax, dword ptr [rcx + 0x8208]
00738B8A  45 8D 65 01                     lea r12d, [r13 + 1]
00738B8E  85 C0                           test eax, eax
00738B90  0F 44 C2                        cmove eax, edx
00738B93  89 81 08 82 00 00               mov dword ptr [rcx + 0x8208], eax
00738B99  8B 81 0C 82 00 00               mov eax, dword ptr [rcx + 0x820c]
00738B9F  85 C0                           test eax, eax
00738BA1  41 0F 44 C4                     cmove eax, r12d
00738BA5  89 81 0C 82 00 00               mov dword ptr [rcx + 0x820c], eax
00738BAB  E9 F9 02 00 00                  jmp 0x140738ea9
00738BB0  48 8D B3 A8 81 00 00            lea rsi, [rbx + 0x81a8]
00738BB7  48 8B D6                        mov rdx, rsi
00738BBA  48 8D 8B 90 81 00 00            lea rcx, [rbx + 0x8190]
00738BC1  E8 FE 13 00 00                  call 0x140739fc4
00738BC6  45 33 FF                        xor r15d, r15d
00738BC9  8B F8                           mov edi, eax
00738BCB  85 C0                           test eax, eax
00738BCD  78 62                           js 0x140738c31
00738BCF  49 8B D5                        mov rdx, r13
00738BD2  48 8B CE                        mov rcx, rsi
00738BD5  E8 2E 01 E7 FF                  call 0x1405a8d08
00738BDA  09 43 40                        or dword ptr [rbx + 0x40], eax
00738BDD  44 8B F8                        mov r15d, eax
00738BE0  45 33 ED                        xor r13d, r13d
00738BE3  48 8B 4B 18                     mov rcx, qword ptr [rbx + 0x18]
00738BE7  BA 20 00 00 00                  mov edx, 0x20
00738BEC  44 39 69 04                     cmp dword ptr [rcx + 4], r13d
00738BF0  0F 84 50 01 00 00               je 0x140738d46
00738BF6  8B 83 B0 81 00 00               mov eax, dword ptr [rbx + 0x81b0]
00738BFC  BA 01 00 00 00                  mov edx, 1
00738C01  84 C2                           test dl, al
00738C03  0F 84 00 01 00 00               je 0x140738d09
00738C09  4C 39 AB D0 81 00 00            cmp qword ptr [rbx + 0x81d0], r13
00738C10  0F 84 F3 00 00 00               je 0x140738d09
00738C16  8D 72 01                        lea esi, [rdx + 1]
00738C19  40 84 C6                        test sil, al
00738C1C  74 5F                           je 0x140738c7d
00738C1E  4C 39 AB D8 81 00 00            cmp qword ptr [rbx + 0x81d8], r13
00738C25  75 56                           jne 0x140738c7d
00738C27  BA 19 01 00 00                  mov edx, 0x119
00738C2C  E9 DD 00 00 00                  jmp 0x140738d0e
00738C31  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
00738C35  45 33 ED                        xor r13d, r13d
00738C38  44 39 68 04                     cmp dword ptr [rax + 4], r13d
00738C3C  74 A5                           je 0x140738be3
00738C3E  BA 02 01 00 00                  mov edx, 0x102
00738C43  48 8B 0D EE 1F 85 00            mov rcx, qword ptr [rip + 0x851fee]
00738C4A  41 BC 01 00 00 00               mov r12d, 1
00738C50  44 8B 7C 24 30                  mov r15d, dword ptr [rsp + 0x30]
00738C55  8B 81 08 82 00 00               mov eax, dword ptr [rcx + 0x8208]
00738C5B  85 C0                           test eax, eax
00738C5D  0F 44 C2                        cmove eax, edx
00738C60  89 81 08 82 00 00               mov dword ptr [rcx + 0x8208], eax
00738C66  8B 81 0C 82 00 00               mov eax, dword ptr [rcx + 0x820c]
00738C6C  85 C0                           test eax, eax
00738C6E  41 0F 44 C4                     cmove eax, r12d
00738C72  89 81 0C 82 00 00               mov dword ptr [rcx + 0x820c], eax
00738C78  E9 2C 02 00 00                  jmp 0x140738ea9
00738C7D  49 8B D4                        mov rdx, r12
00738C80  E8 EB 1A 00 00                  call 0x14073a770
00738C85  8B F8                           mov edi, eax
00738C87  85 C0                           test eax, eax
00738C89  79 07                           jns 0x140738c92
00738C8B  BA 25 01 00 00                  mov edx, 0x125
00738C90  EB B1                           jmp 0x140738c43
00738C92  41 F6 C7 08                     test r15b, 8
00738C96  74 0A                           je 0x140738ca2
00738C98  48 8B 43 38                     mov rax, qword ptr [rbx + 0x38]
00738C9C  44 89 68 04                     mov dword ptr [rax + 4], r13d
00738CA0  EB 10                           jmp 0x140738cb2
00738CA2  4C 39 AB F8 81 00 00            cmp qword ptr [rbx + 0x81f8], r13
00738CA9  74 57                           je 0x140738d02
00738CAB  8B 43 40                        mov eax, dword ptr [rbx + 0x40]
00738CAE  A8 20                           test al, 0x20
00738CB0  75 50                           jne 0x140738d02
00738CB2  44 8B 7C 24 30                  mov r15d, dword ptr [rsp + 0x30]
00738CB7  48 8D 93 90 00 00 00            lea rdx, [rbx + 0x90]
00738CBE  45 8B C7                        mov r8d, r15d
00738CC1  48 8D 8B 88 00 00 00            lea rcx, [rbx + 0x88]
00738CC8  E8 F7 06 00 00                  call 0x1407393c4
00738CCD  8B F8                           mov edi, eax
00738CCF  85 C0                           test eax, eax
00738CD1  79 21                           jns 0x140738cf4
00738CD3  48 8B 0D 5E 1F 85 00            mov rcx, qword ptr [rip + 0x851f5e]
00738CDA  BA 4C 01 00 00                  mov edx, 0x14c
00738CDF  8B 81 08 82 00 00               mov eax, dword ptr [rcx + 0x8208]
00738CE5  85 C0                           test eax, eax
00738CE7  0F 44 C2                        cmove eax, edx
00738CEA  BA 0A 00 00 00                  mov edx, 0xa
00738CEF  E9 C9 FD FF FF                  jmp 0x140738abd
00738CF4  4C 89 AB A8 00 00 00            mov qword ptr [rbx + 0xa8], r13
00738CFB  BA 20 00 00 00                  mov edx, 0x20
00738D00  EB 49                           jmp 0x140738d4b
00738D02  BA 3D 01 00 00                  mov edx, 0x13d
00738D07  EB 05                           jmp 0x140738d0e
00738D09  BA 11 01 00 00                  mov edx, 0x111
00738D0E  48 8B 0D 23 1F 85 00            mov rcx, qword ptr [rip + 0x851f23]
00738D15  44 8B 7C 24 30                  mov r15d, dword ptr [rsp + 0x30]
00738D1A  8B 81 08 82 00 00               mov eax, dword ptr [rcx + 0x8208]
00738D20  85 C0                           test eax, eax
00738D22  0F 44 C2                        cmove eax, edx
00738D25  BA 09 00 00 00                  mov edx, 9
00738D2A  89 81 08 82 00 00               mov dword ptr [rcx + 0x8208], eax
00738D30  8B 81 0C 82 00 00               mov eax, dword ptr [rcx + 0x820c]
00738D36  85 C0                           test eax, eax
00738D38  0F 44 C2                        cmove eax, edx
00738D3B  89 81 0C 82 00 00               mov dword ptr [rcx + 0x820c], eax
00738D41  E9 02 FD FF FF                  jmp 0x140738a48
00738D46  44 8B 7C 24 30                  mov r15d, dword ptr [rsp + 0x30]
00738D4B  8B 43 40                        mov eax, dword ptr [rbx + 0x40]
00738D4E  84 C2                           test dl, al
00738D50  74 2F                           je 0x140738d81
00738D52  4C 39 AB 00 82 00 00            cmp qword ptr [rbx + 0x8200], r13
00738D59  75 26                           jne 0x140738d81
00738D5B  48 8B 0D D6 1E 85 00            mov rcx, qword ptr [rip + 0x851ed6]
00738D62  BA 60 01 00 00                  mov edx, 0x160
00738D67  BF BB 00 00 C0                  mov edi, 0xc00000bb
00738D6C  8B 81 08 82 00 00               mov eax, dword ptr [rcx + 0x8208]
00738D72  85 C0                           test eax, eax
00738D74  0F 44 C2                        cmove eax, edx
00738D77  BA 09 00 00 00                  mov edx, 9
00738D7C  E9 3C FD FF FF                  jmp 0x140738abd
00738D81  33 D2                           xor edx, edx
00738D83  44 89 BB B0 00 00 00            mov dword ptr [rbx + 0xb0], r15d
00738D8A  41 B8 00 01 00 00               mov r8d, 0x100
00738D90  48 C7 44 24 60 01 00 20 00      mov qword ptr [rsp + 0x60], 0x200001
00738D99  48 8D 4C 24 68                  lea rcx, [rsp + 0x68]
00738D9E  41 BC 01 00 00 00               mov r12d, 1
00738DA4  E8 97 DE F8 FF                  call 0x1406c6c40
00738DA9  0F B7 54 24 62                  movzx edx, word ptr [rsp + 0x62]
00738DAE  4C 8D 05 6B E3 88 00            lea r8, [rip + 0x88e36b]
00738DB5  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
00738DBA  E8 A1 5A B9 FF                  call 0x1402ce860
00738DBF  48 8B 53 10                     mov rdx, qword ptr [rbx + 0x10]
00738DC3  8B 42 08                        mov eax, dword ptr [rdx + 8]
00738DC6  85 C0                           test eax, eax
00738DC8  74 26                           je 0x140738df0
00738DCA  48 8B 12                        mov rdx, qword ptr [rdx]
00738DCD  4C 8D 44 24 68                  lea r8, [rsp + 0x68]
00738DD2  49 2B D0                        sub rdx, r8
00738DD5  48 8D 4C 24 68                  lea rcx, [rsp + 0x68]
00738DDA  44 8B C0                        mov r8d, eax
00738DDD  48 8B 04 0A                     mov rax, qword ptr [rdx + rcx]
00738DE1  48 F7 D0                        not rax
00738DE4  48 21 01                        and qword ptr [rcx], rax
00738DE7  48 8D 49 08                     lea rcx, [rcx + 8]
00738DEB  4D 2B C4                        sub r8, r12
00738DEE  75 ED                           jne 0x140738ddd
00738DF0  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
00738DF5  E8 86 87 B9 FF                  call 0x1402d1580
00738DFA  85 C0                           test eax, eax
00738DFC  74 37                           je 0x140738e35
00738DFE  48 8B 0D 33 1E 85 00            mov rcx, qword ptr [rip + 0x851e33]
00738E05  BA 7B 01 00 00                  mov edx, 0x17b
00738E0A  BF CB 00 00 C0                  mov edi, 0xc00000cb
00738E0F  8B 81 08 82 00 00               mov eax, dword ptr [rcx + 0x8208]
00738E15  85 C0                           test eax, eax
00738E17  0F 44 C2                        cmove eax, edx
00738E1A  BA 06 00 00 00                  mov edx, 6
00738E1F  89 81 08 82 00 00               mov dword ptr [rcx + 0x8208], eax
00738E25  8B 81 0C 82 00 00               mov eax, dword ptr [rcx + 0x820c]
00738E2B  85 C0                           test eax, eax
00738E2D  0F 44 C2                        cmove eax, edx
00738E30  E9 70 FD FF FF                  jmp 0x140738ba5
00738E35  33 D2                           xor edx, edx
00738E37  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
00738E3C  E8 0F C3 BC FF                  call 0x140305150
00738E41  85 C0                           test eax, eax
00738E43  74 05                           je 0x140738e4a
00738E45  41 8B C5                        mov eax, r13d
00738E48  EB 0A                           jmp 0x140738e54
00738E4A  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
00738E4F  E8 8C A2 D1 FF                  call 0x1404530e0
00738E54  89 83 B4 00 00 00               mov dword ptr [rbx + 0xb4], eax
00738E5A  48 8D 54 24 50                  lea rdx, [rsp + 0x50]
00738E5F  8B C8                           mov ecx, eax
00738E61  48 8B 05 48 A3 7E 00            mov rax, qword ptr [rip + 0x7ea348]
00738E68  8B 0C 88                        mov ecx, dword ptr [rax + rcx*4]
00738E6B  33 C0                           xor eax, eax
00738E6D  89 44 24 4A                     mov dword ptr [rsp + 0x4a], eax
00738E71  66 89 44 24 4E                  mov word ptr [rsp + 0x4e], ax
00738E76  8B C1                           mov eax, ecx
00738E78  C1 E8 06                        shr eax, 6
00738E7B  83 E1 3F                        and ecx, 0x3f
00738E7E  66 89 44 24 48                  mov word ptr [rsp + 0x48], ax
00738E83  49 8B C4                        mov rax, r12
00738E86  48 D3 E0                        shl rax, cl
00738E89  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
00738E8E  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00738E93  E8 A8 02 C6 FF                  call 0x140399140
00738E98  E8 97 B1 42 00                  call 0x140b64034
00738E9D  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
00738EA2  8B F8                           mov edi, eax
00738EA4  E8 17 00 C6 FF                  call 0x140398ec0
00738EA9  45 39 6E 10                     cmp dword ptr [r14 + 0x10], r13d
00738EAD  7C 27                           jl 0x140738ed6
00738EAF  85 FF                           test edi, edi
00738EB1  78 14                           js 0x140738ec7
00738EB3  33 C9                           xor ecx, ecx
00738EB5  E8 1A B1 42 00                  call 0x140b63fd4
00738EBA  89 83 40 82 00 00               mov dword ptr [rbx + 0x8240], eax
00738EC0  E8 BB 14 00 00                  call 0x14073a380
00738EC5  EB 0F                           jmp 0x140738ed6
00738EC7  49 8B 56 08                     mov rdx, qword ptr [r14 + 8]
00738ECB  44 8B C7                        mov r8d, edi
00738ECE  49 8B 0E                        mov rcx, qword ptr [r14]
00738ED1  E8 AA 12 00 00                  call 0x14073a180
00738ED6  48 85 DB                        test rbx, rbx
00738ED9  0F 84 FD 00 00 00               je 0x140738fdc
00738EDF  48 8B B3 90 81 00 00            mov rsi, qword ptr [rbx + 0x8190]
00738EE6  48 85 F6                        test rsi, rsi
00738EE9  74 19                           je 0x140738f04
00738EEB  48 8B 83 B8 81 00 00            mov rax, qword ptr [rbx + 0x81b8]
00738EF2  48 85 C0                        test rax, rax
00738EF5  74 05                           je 0x140738efc
00738EF7  E8 D4 1B F8 FF                  call 0x1406baad0
00738EFC  48 8B CE                        mov rcx, rsi
00738EFF  E8 5C A0 36 00                  call 0x140aa2f60
00738F04  4C 39 AB 88 00 00 00            cmp qword ptr [rbx + 0x88], r13
00738F0B  74 5A                           je 0x140738f67
00738F0D  4C 39 AB 90 00 00 00            cmp qword ptr [rbx + 0x90], r13
00738F14  74 51                           je 0x140738f67
00738F16  45 85 FF                        test r15d, r15d
00738F19  74 2A                           je 0x140738f45
00738F1B  49 8B F5                        mov rsi, r13
00738F1E  48 8B 8B 88 00 00 00            mov rcx, qword ptr [rbx + 0x88]
00738F25  48 03 CE                        add rcx, rsi
00738F28  E8 6F 09 00 00                  call 0x14073989c
00738F2D  48 8B 8B 90 00 00 00            mov rcx, qword ptr [rbx + 0x90]
00738F34  48 03 CE                        add rcx, rsi
00738F37  E8 60 09 00 00                  call 0x14073989c
00738F3C  48 83 C6 18                     add rsi, 0x18
00738F40  4D 2B FC                        sub r15, r12
00738F43  75 D9                           jne 0x140738f1e
00738F45  48 8B 8B 88 00 00 00            mov rcx, qword ptr [rbx + 0x88]
00738F4C  BA 50 6E 70 51                  mov edx, 0x51706e50
00738F51  E8 1A 99 44 00                  call 0x140b82870
00738F56  48 8B 8B 90 00 00 00            mov rcx, qword ptr [rbx + 0x90]
00738F5D  BA 50 6E 70 51                  mov edx, 0x51706e50
00738F62  E8 09 99 44 00                  call 0x140b82870
00738F67  48 8D 8B 98 00 00 00            lea rcx, [rbx + 0x98]
00738F6E  E8 01 19 00 00                  call 0x14073a874
00738F73  48 8B 4B 10                     mov rcx, qword ptr [rbx + 0x10]
00738F77  48 85 C9                        test rcx, rcx
00738F7A  74 0E                           je 0x140738f8a
00738F7C  BA 50 6E 70 51                  mov edx, 0x51706e50
00738F81  E8 EA 98 44 00                  call 0x140b82870
00738F86  4C 89 6B 10                     mov qword ptr [rbx + 0x10], r13
00738F8A  48 8B 4B 18                     mov rcx, qword ptr [rbx + 0x18]
00738F8E  48 85 C9                        test rcx, rcx
00738F91  74 0E                           je 0x140738fa1
00738F93  BA 50 6E 70 51                  mov edx, 0x51706e50
00738F98  E8 D3 98 44 00                  call 0x140b82870
00738F9D  4C 89 6B 18                     mov qword ptr [rbx + 0x18], r13
00738FA1  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00738FA5  48 85 C9                        test rcx, rcx
00738FA8  74 0E                           je 0x140738fb8
00738FAA  BA 50 6E 70 51                  mov edx, 0x51706e50
00738FAF  E8 BC 98 44 00                  call 0x140b82870
00738FB4  4C 89 6B 30                     mov qword ptr [rbx + 0x30], r13
00738FB8  48 8B 4B 38                     mov rcx, qword ptr [rbx + 0x38]
00738FBC  48 85 C9                        test rcx, rcx
00738FBF  74 0E                           je 0x140738fcf
00738FC1  BA 50 6E 70 51                  mov edx, 0x51706e50
00738FC6  E8 A5 98 44 00                  call 0x140b82870
00738FCB  4C 89 6B 38                     mov qword ptr [rbx + 0x38], r13
00738FCF  BA 50 6E 70 51                  mov edx, 0x51706e50
00738FD4  48 8B CB                        mov rcx, rbx
00738FD7  E8 94 98 44 00                  call 0x140b82870
00738FDC  45 33 C0                        xor r8d, r8d
00738FDF  48 8D 0D 3A 1C 85 00            lea rcx, [rip + 0x851c3a]
00738FE6  33 D2                           xor edx, edx
00738FE8  E8 23 63 C0 FF                  call 0x14033f310
00738FED  49 8D 4E 18                     lea rcx, [r14 + 0x18]
00738FF1  41 89 7E 14                     mov dword ptr [r14 + 0x14], edi
00738FF5  45 33 C0                        xor r8d, r8d
00738FF8  33 D2                           xor edx, edx
00738FFA  E8 11 63 C0 FF                  call 0x14033f310
00738FFF  48 8B 8D C0 00 00 00            mov rcx, qword ptr [rbp + 0xc0]
00739006  48 33 CC                        xor rcx, rsp
00739009  E8 32 36 F7 FF                  call 0x1406ac640
0073900E  4C 8D 9C 24 D0 01 00 00         lea r11, [rsp + 0x1d0]
00739016  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
0073901A  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
0073901E  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
00739022  49 8B E3                        mov rsp, r11
00739025  41 5F                           pop r15
00739027  41 5E                           pop r14
00739029  41 5D                           pop r13
0073902B  41 5C                           pop r12
0073902D  5D                              pop rbp
0073902E  C3                              ret
0073902F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PnpReplacePartitionUnit(__int64 a1, int a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m190;
    unsigned __int16 v_stack_m196;
    unsigned __int64 v_stack_m198;
    unsigned __int64 v_stack_m1A8;
    unsigned __int16 v_stack_m1AA;
    unsigned int v_stack_m1AE;
    unsigned __int16 v_stack_m1B0;
    unsigned __int64 v_stack_m1B8;
    unsigned __int64 v_stack_m1C0;
    unsigned __int64 v_stack_m1C4;
    unsigned int v_stack_m1C8;
    unsigned __int64 v_stack_m1D8;
    unsigned __int64 v_stack_m28;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (464);
    result = (*(unsigned __int64 *)(v_rip + 7152067)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 248 + 192) = result;
    a2 = 0;
    v_stack_m1B8 = v_xmm0;
    result = memset(v_stack_m190, a2, 256, a4);
    a2 = 0;
    v_stack_m1A8 = v_xmm0;
    result = memset(v_rsp - 248 + 112, a2, a2 + 80, a4);
    result = KeQueryActiveProcessorCountEx((unsigned int)(0xFFFFULL), a2, a2 + 80, a4);
    v_r13 = 0;
    v_stack_m1C8 = (unsigned int)((unsigned int)((unsigned int)(result)));
    a4 = 0;
    v_stack_m1D8 = 0;
    a3 = 0;
    a2 = 0;
    result = KeWaitForSingleObject(v_rip + 8726097, a2, a3, a4);
    if ((*(unsigned int *)(a1 + 16)) < 0) goto loc_00738653;
    if (*(unsigned __int64 *)(a1 + 8) == 0) goto loc_007389C1;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 312) + 40) == 0) goto loc_0073882D;
    if (condition_is_below) goto loc_0073882D;
    if (*(unsigned __int64 *)(a1) == 0) goto loc_00738814;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 312) + 40) == 0) goto loc_00738684;
    if (condition_is_below) goto loc_00738684;
    result = PnprLogStartEvent(*(unsigned __int64 *)(a1), *(unsigned __int64 *)(a1 + 8), *(unsigned __int64 *)(a1 + 8), a4);
loc_00738653:
    result = ExAllocatePool2(64, (unsigned int)(0x8248ULL), (unsigned int)(0x51706E50ULL), a4);
    if (result != 0) goto loc_007389DA;
    goto loc_00738EA9;
loc_00738684:
    result = IoAddTriageDumpDataBlock(64, *(unsigned __int16 *)(64 + 2), (unsigned int)(0x51706E50ULL), a4);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 8) == 0) goto loc_007386CE;
    result = IoAddTriageDumpDataBlock(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 8), (__int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 8) + 2)), (unsigned int)(0x51706E50ULL), a4);
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 8)) + (56);
    result = *(unsigned __int64 *)(a1);
    if ((*(unsigned __int16 *)(a1)) != 0) {
        a2 = (unsigned int)(v_r13 + 2);
        result = IoAddTriageDumpDataBlock(a1, a2, (unsigned int)(0x51706E50ULL), a4);
        result = *(unsigned __int64 *)(a1);
        a1 = *(unsigned __int64 *)(result + 8);
        a2 = *(unsigned __int16 *)(a1 + 56);
        a1 = *(unsigned __int64 *)(a1 + 64);
        result = IoAddTriageDumpDataBlock(a1, a2, (unsigned int)(0x51706E50ULL), a4);
    }
    if (*(unsigned __int64 *)(a1) == 0) goto loc_00738814;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 312) + 40)) == 0) goto loc_00738814;
    result = IoAddTriageDumpDataBlock(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 312) + 40), 904, (unsigned int)(0x51706E50ULL), a4);
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 312) + 40) + 40)) != 0) {
        a2 = (unsigned int)(v_r13 + 2);
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 312) + 40) + 40;
        result = IoAddTriageDumpDataBlock(a1, a2, (unsigned int)(0x51706E50ULL), a4);
        a2 = *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 312) + 40) + 40);
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 312) + 40) + 48);
        result = IoAddTriageDumpDataBlock(a1, a2, (unsigned int)(0x51706E50ULL), a4);
    }
    if (*(unsigned __int64 *)(a1) == 0) goto loc_00738733;
    goto loc_00738736;
loc_00738733:
loc_00738736:
    if ((*(unsigned __int16 *)(0 + 56)) == 0) goto loc_00738784;
    if (*(unsigned __int64 *)(a1) == 0) goto loc_0073874B;
    goto loc_0073874E;
loc_0073874B:
loc_0073874E:
    a1 = (0) + (56);
    result = IoAddTriageDumpDataBlock(a1, (unsigned int)((unsigned int)(v_r13 + 2)), 0, a4);
    if (*(unsigned __int64 *)(a1) == 0) goto loc_00738771;
    goto loc_00738777;
loc_00738771:
loc_00738777:
    result = IoAddTriageDumpDataBlock(*(unsigned __int64 *)(0 + 64), *(unsigned __int16 *)(0 + 56), 0, a4);
loc_00738784:
    if (*(unsigned __int64 *)(a1) == 0) goto loc_0073879C;
    goto loc_0073879F;
loc_0073879C:
loc_0073879F:
    if ((*(unsigned __int64 *)(0 + 16)) == 0) goto loc_00738814;
    if (*(unsigned __int64 *)(a1) == 0) goto loc_007387B3;
    goto loc_007387B6;
loc_007387B3:
loc_007387B6:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(0 + 16) + 56)) == 0) goto loc_00738814;
    if (*(unsigned __int64 *)(a1) == 0) goto loc_007387CF;
    goto loc_007387D2;
loc_007387CF:
loc_007387D2:
    a1 = (*(unsigned __int64 *)(0 + 16)) + (56);
    result = IoAddTriageDumpDataBlock(a1, (unsigned int)((unsigned int)(v_r13 + 2)), 0, a4);
    if (*(unsigned __int64 *)(a1) == 0) goto loc_007387F9;
    goto loc_007387FF;
loc_007387F9:
loc_007387FF:
    result = IoAddTriageDumpDataBlock(*(unsigned __int64 *)(*(unsigned __int64 *)(0 + 16) + 64), *(unsigned __int16 *)(*(unsigned __int64 *)(0 + 16) + 56), 0, a4);
loc_00738814:
    a4 = 0;
    v_stack_m1D8 = 0;
    result = KeBugCheckEx(202, v_r13 + 2, *(unsigned __int64 *)(a1), a4);
loc_0073882D:
    result = IoAddTriageDumpDataBlock(*(unsigned __int64 *)(a1), *(unsigned __int16 *)(*(unsigned __int64 *)(a1) + 2), *(unsigned __int64 *)(a1), a4);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 8) == 0) goto loc_0073887B;
    result = IoAddTriageDumpDataBlock(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 8), (__int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 8) + 2)), *(unsigned __int64 *)(a1), a4);
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 8)) + (56);
    result = *(unsigned __int64 *)((unsigned int)(0xC000009AULL));
    if ((*(unsigned __int16 *)(a1)) != 0) {
        a2 = (unsigned int)(v_r13 + 2);
        result = IoAddTriageDumpDataBlock(a1, a2, *(unsigned __int64 *)(a1), a4);
        result = *(unsigned __int64 *)((unsigned int)(0xC000009AULL));
        a1 = *(unsigned __int64 *)(result + 8);
        a2 = *(unsigned __int16 *)(a1 + 56);
        a1 = *(unsigned __int64 *)(a1 + 64);
        result = IoAddTriageDumpDataBlock(a1, a2, *(unsigned __int64 *)(a1), a4);
    }
    if (*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) == 0) goto loc_007389C1;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40)) == 0) goto loc_007389C1;
    result = IoAddTriageDumpDataBlock(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40), 904, *(unsigned __int64 *)(a1), a4);
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 40)) != 0) {
        a2 = (unsigned int)(v_r13 + 2);
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 40;
        result = IoAddTriageDumpDataBlock(a1, a2, *(unsigned __int64 *)(a1), a4);
        a2 = *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 40);
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 48);
        result = IoAddTriageDumpDataBlock(a1, a2, *(unsigned __int64 *)(a1), a4);
    }
    if (*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) == 0) goto loc_007388E0;
    goto loc_007388E3;
loc_007388E0:
loc_007388E3:
    if ((*(unsigned __int16 *)(0 + 56)) == 0) goto loc_00738931;
    if (*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) == 0) goto loc_007388F8;
    goto loc_007388FB;
loc_007388F8:
loc_007388FB:
    a1 = (0) + (56);
    result = IoAddTriageDumpDataBlock(a1, (unsigned int)((unsigned int)(v_r13 + 2)), 0, a4);
    if (*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) == 0) goto loc_0073891E;
    goto loc_00738924;
loc_0073891E:
loc_00738924:
    result = IoAddTriageDumpDataBlock(*(unsigned __int64 *)(0 + 64), *(unsigned __int16 *)(0 + 56), 0, a4);
loc_00738931:
    if (*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) == 0) goto loc_00738949;
    goto loc_0073894C;
loc_00738949:
loc_0073894C:
    if ((*(unsigned __int64 *)(0 + 16)) == 0) goto loc_007389C1;
    if (*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) == 0) goto loc_00738960;
    goto loc_00738963;
loc_00738960:
loc_00738963:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(0 + 16) + 56)) == 0) goto loc_007389C1;
    if (*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) == 0) goto loc_0073897C;
    goto loc_0073897F;
loc_0073897C:
loc_0073897F:
    a1 = (*(unsigned __int64 *)(0 + 16)) + (56);
    result = IoAddTriageDumpDataBlock(a1, (unsigned int)((unsigned int)(v_r13 + 2)), 0, a4);
    if (*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) == 0) goto loc_007389A6;
    goto loc_007389AC;
loc_007389A6:
loc_007389AC:
    result = IoAddTriageDumpDataBlock(*(unsigned __int64 *)(*(unsigned __int64 *)(0 + 16) + 64), *(unsigned __int16 *)(*(unsigned __int64 *)(0 + 16) + 56), 0, a4);
loc_007389C1:
    a4 = 0;
    v_stack_m1D8 = 0;
    result = KeBugCheckEx(202, v_r13 + 2, *(unsigned __int64 *)((unsigned int)(0xC000009AULL)), a4);
loc_007389DA:
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40)) = *(unsigned __int64 *)(a1);
    v_rsi = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 32) = *(unsigned __int64 *)((unsigned int)(0xC000009AULL));
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 64) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 16)));
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 152 + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 152;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 152) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 152;
    *(unsigned __int64 *)(v_rip + 8725030) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40);
    if ((*(unsigned __int8 *)(v_rip + 8970393)) != 0) goto loc_00738A58;
    if ((*(unsigned int *)(a1 + 16)) < 0) goto loc_00738A58;
    v_r13 = 0;
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 33288));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 33288))) == 0) { result = 170; }
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 33288) = (unsigned int)(result);
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 33292));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 33292))) == 0) { result = (unsigned int)(v_r13 + 2); }
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 33292) = (unsigned int)(result);
loc_00738A48:
loc_00738A4D:
    goto loc_00738EA9;
loc_00738A58:
    v_stack_m1C4 = (unsigned int)(v_r13 + 2);
    v_stack_m1C0 = v_r13 + 2;
    result = IoGetLegacyVetoList(v_stack_m1C0, v_stack_m1C4, *(unsigned __int64 *)((unsigned int)(0xC000009AULL)), a4);
    v_rdi = (unsigned __int8)(v_r13 + 2);
    if (!(sign_flag)) {
        a2 = 1;
        v_rdi = (unsigned __int8)(v_r13 + 2);
        if (v_stack_m1C4 != ((unsigned int)(v_r13 + 2))) { v_rdi = a2; }
    }
    if (v_stack_m1C0 != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(v_stack_m1C0, a2, *(unsigned __int64 *)((unsigned int)(0xC000009AULL)), a4);
    }
    if ((unsigned __int8)(v_rdi) == 0) goto loc_00738AD9;
    v_r13 = 0;
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 8724887) + 33288));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 8724887) + 33288))) == 0) { result = 182; }
loc_00738ABD:
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 8724887) + 33288) = (unsigned int)(result);
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 8724887) + 33292));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 8724887) + 33292))) == 0) { result = (unsigned int)(v_r13 + 7); }
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 8724887) + 33292) = (unsigned int)(result);
    goto loc_00738A4D;
loc_00738AD9:
    result = PnprGetMillisecondCounter(1, v_r13 + 7, *(unsigned __int64 *)((unsigned int)(0xC000009AULL)), a4);
    if ((*(unsigned int *)(a1 + 16)) >= ((unsigned int)(v_r13 + 2))) goto loc_00738B10;
    result = PnprLockPagesForReplace(1, v_r13 + 7, *(unsigned __int64 *)((unsigned int)(0xC000009AULL)), a4);
    result = PnprQuiesceDevices(v_rsp - 248 + 112, v_r13 + 7, *(unsigned __int64 *)((unsigned int)(0xC000009AULL)), a4);
    result = PnprWakeDevices(v_rsp - 248 + 112, v_r13 + 7, *(unsigned __int64 *)((unsigned int)(0xC000009AULL)), a4);
    result = PnprUnlockPagesForReplace(v_rsp - 248 + 112, v_r13 + 7, *(unsigned __int64 *)((unsigned int)(0xC000009AULL)), a4);
    v_r13 = 0;
    goto loc_00738A4D;
loc_00738B10:
    result = PnprIdentifyUnits(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40)), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 32), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 8, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 40);
    if (!sign_flag) goto loc_00738B64;
    v_r13 = 0;
    a1 = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 8724743) + 33288));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 8724743) + 33288))) == 0) { a1 = 219; }
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 8724743) + 33288) = (unsigned int)(a1);
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 8724743) + 33292));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 8724743) + 33292))) == 0) { result = (unsigned int)(v_r13 + 3); }
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 8724743) + 33292) = (unsigned int)(result);
    goto loc_00738A4D;
loc_00738B64:
    result = PnprCollectResources(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40), 0, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 8, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 40);
    if (!sign_flag) goto loc_00738BB0;
    v_r13 = 0;
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 8724668) + 33288));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 8724668) + 33288))) == 0) { result = 232; }
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 8724668) + 33288) = (unsigned int)(result);
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 8724668) + 33292));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 8724668) + 33292))) == 0) { result = (unsigned int)(v_r13 + 1); }
loc_00738BA5:
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 8724668) + 33292) = (unsigned int)(result);
    goto loc_00738EA9;
loc_00738BB0:
    result = PnprLoadPluginDriver(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 33168, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 33192, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 8, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 40);
    v_r15 = 0;
    if (sign_flag) goto loc_00738C31;
    result = PnprQueryReplaceFeatures(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 33192, 0, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 8, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 40);
    v_r13 = 0;
loc_00738BE3:
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 24) + 4)) == 0) goto loc_00738D46;
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 33200))))) == 0) goto loc_00738D09;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 33232)) == 0) goto loc_00738D09;
    if ((((unsigned __int8)(1 + 1)) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 33200))))) == 0) goto loc_00738C7D;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 33240)) != 0) goto loc_00738C7D;
    goto loc_00738D0E;
loc_00738C31:
    v_r13 = 0;
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 24) + 4)) == 0) goto loc_00738BE3;
loc_00738C43:
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 8724462) + 33288));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 8724462) + 33288))) == 0) { result = 258; }
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 8724462) + 33288) = (unsigned int)(result);
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 8724462) + 33292));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 8724462) + 33292))) == 0) { result = 1; }
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 8724462) + 33292) = (unsigned int)(result);
    goto loc_00738EA9;
loc_00738C7D:
    result = PnprMmConstruct(*(unsigned __int64 *)(v_rip + 8724462), 1, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 8, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 40);
    if (!sign_flag) goto loc_00738C92;
    goto loc_00738C43;
loc_00738C92:
    if ((((unsigned __int8)((unsigned int)(v_stack_m1C8))) & (8)) == 0) goto loc_00738CA2;
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 56) + 4) = 0;
    goto loc_00738CB2;
loc_00738CA2:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 33272)) == 0) goto loc_00738D02;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 64)))) & (32)) != 0) goto loc_00738D02;
loc_00738CB2:
    result = PnprAllocateMappingReserves(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 136, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 144, (unsigned int)((unsigned int)((unsigned int)(v_stack_m1C8))), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 40);
    if (!sign_flag) goto loc_00738CF4;
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 8724318) + 33288));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 8724318) + 33288))) == 0) { result = 332; }
    goto loc_00738ABD;
loc_00738CF4:
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 168) = 0;
    goto loc_00738D4B;
loc_00738D02:
    goto loc_00738D0E;
loc_00738D09:
loc_00738D0E:
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 8724259) + 33288));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 8724259) + 33288))) == 0) { result = 273; }
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 8724259) + 33288) = (unsigned int)(result);
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 8724259) + 33292));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 8724259) + 33292))) == 0) { result = 9; }
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 8724259) + 33292) = (unsigned int)(result);
    goto loc_00738A48;
loc_00738D46:
loc_00738D4B:
    if (((9) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 64))))) == 0) goto loc_00738D81;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 33280)) != 0) goto loc_00738D81;
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 8724182) + 33288));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 8724182) + 33288))) == 0) { result = 352; }
    goto loc_00738ABD;
loc_00738D81:
    a2 = 0;
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 176) = (unsigned int)((unsigned int)(v_stack_m1C8));
    v_stack_m198 = 0x200001ULL;
    result = memset(v_stack_m190, a2, 256, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 40);
    result = KiCopyAffinityEx(v_stack_m198, v_stack_m196, v_rip + 8971115, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 40);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 16) + 8))) == 0) goto loc_00738DF0;
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 16))) - (v_stack_m190);
loc_00738DDD:
    result = ~(*(unsigned __int64 *)(a2 + v_stack_m190 * 1));
    a3 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 16) + 8))))) - (1);
    if (condition_is_not_equal) goto loc_00738DDD;
loc_00738DF0:
    result = KeIsEmptyAffinityEx(v_stack_m198, a2, a3, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 40);
    if ((unsigned int)(result) == 0) goto loc_00738E35;
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 8724019) + 33288));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 8724019) + 33288))) == 0) { result = 379; }
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 8724019) + 33288) = (unsigned int)(result);
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 8724019) + 33292));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 8724019) + 33292))) == 0) { result = 6; }
    goto loc_00738BA5;
loc_00738E35:
    a2 = 0;
    result = KeCheckProcessorAffinityEx(v_stack_m198, a2, a3, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 40);
    if ((unsigned int)(result) == 0) goto loc_00738E4A;
    goto loc_00738E54;
loc_00738E4A:
    result = KeFindFirstSetLeftAffinityEx(v_stack_m198, a2, a3, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 40);
loc_00738E54:
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 180) = (unsigned int)(result);
    result = 0;
    v_stack_m1AE = 0;
    v_stack_m1AA = 0;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 8299336) + (unsigned int)((unsigned int)(result)) * 4))))) >> (6));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 8299336) + (unsigned int)((unsigned int)(result)) * 4))) & (63));
    v_stack_m1B0 = (unsigned __int16)(result);
    result = (1) << ((unsigned __int8)(a1));
    v_stack_m1B8 = result;
    result = KeSetSystemGroupAffinityThread(v_stack_m1B8, v_stack_m1A8, a3, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 40);
    result = PnprInitiateReplaceOperation(v_stack_m1B8, v_stack_m1A8, a3, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 40);
    result = KeRevertToUserGroupAffinityThread(v_stack_m1A8, v_stack_m1A8, a3, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 40);
loc_00738EA9:
    if ((*(unsigned int *)(a1 + 16)) < 0) goto loc_00738ED6;
    if (sign_flag) goto loc_00738EC7;
    a1 = 0;
    result = PnprGetMillisecondCounter(a1, v_stack_m1A8, a3, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 40);
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 33344) = (unsigned int)(result);
    result = PnprLogSuccessEvent(a1, v_stack_m1A8, a3, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 40);
    goto loc_00738ED6;
loc_00738EC7:
    result = PnprLogFailureEvent(*(unsigned __int64 *)(a1), *(unsigned __int64 *)(a1 + 8), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 40);
loc_00738ED6:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) == 0) goto loc_00738FDC;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 33168) == 0) goto loc_00738F04;
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 33208);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 33208) != 0) {
        result = guard_dispatch_icall(*(unsigned __int64 *)(a1), *(unsigned __int64 *)(a1 + 8), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 40);
    }
    result = MmUnloadSystemImage(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 33168), *(unsigned __int64 *)(a1 + 8), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 40);
loc_00738F04:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 136)) == 0) goto loc_00738F67;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 144)) == 0) goto loc_00738F67;
    if ((unsigned int)((unsigned int)(v_stack_m1C8)) == 0) goto loc_00738F45;
loc_00738F1E:
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 136)) + (0);
    result = PnprFreeMappingReserve(a1, *(unsigned __int64 *)(a1 + 8), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 40);
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 144)) + (0);
    result = PnprFreeMappingReserve(a1, *(unsigned __int64 *)(a1 + 8), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 40);
    v_rsi = (0) + (24);
    v_r15 = ((unsigned int)(v_stack_m1C8)) - (1);
    if (condition_is_not_equal) goto loc_00738F1E;
loc_00738F45:
    result = ExFreePoolWithTag(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 136), (unsigned int)(0x51706E50ULL), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 40);
    result = ExFreePoolWithTag(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 144), (unsigned int)(0x51706E50ULL), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 40);
loc_00738F67:
    result = PnprMmFree(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 152, (unsigned int)(0x51706E50ULL), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 40);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 16) != 0) {
        a2 = 0x51706E50ULL;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 16), a2, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 40);
        *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 16) = 0;
    }
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 24) != 0) {
        a2 = 0x51706E50ULL;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 24), a2, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 40);
        *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 24) = 0;
    }
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 48) != 0) {
        a2 = 0x51706E50ULL;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 48), a2, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 40);
        *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 48) = 0;
    }
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 56) != 0) {
        a2 = 0x51706E50ULL;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 56), a2, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 40);
        *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 56) = 0;
    }
    result = ExFreePoolWithTag(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40), (unsigned int)(0x51706E50ULL), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 40);
loc_00738FDC:
    a3 = 0;
    a2 = 0;
    result = KeSetEvent(v_rip + 8723514, a2, a3, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 40);
    *(unsigned int *)(a1 + 20) = (unsigned int)((unsigned int)((unsigned int)(result)));
    a3 = 0;
    a2 = 0;
    result = KeSetEvent(a1 + 24, a2, a3, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 40);
    a1 = (*(unsigned __int64 *)(v_rsp - 248 + 192)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL)) + 312) + 40) + 40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PnpReplacePartitionUnit(void *Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m190;
    uint16_t v_stack_m196;
    uint64_t v_stack_m198;
    uint64_t v_stack_m1A8;
    uint16_t v_stack_m1AA;
    uint32_t v_stack_m1AE;
    uint16_t v_stack_m1B0;
    uint64_t v_stack_m1B8;
    uint64_t v_stack_m1C0;
    uint64_t v_stack_m1C4;
    uint32_t v_stack_m1C8;
    uint64_t v_stack_m1D8;
    uint64_t v_stack_m28;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (464);
    result = (*(uint64_t *)(v_rip + 0x6D21C3)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0xF8 + 0xC0) = result;
    Arg2 = 0;
    v_stack_m1B8 = v_xmm0;
    result = memset(v_stack_m190, Arg2, 256, Arg4);
    Arg2 = 0;
    v_stack_m1A8 = v_xmm0;
    result = memset(local_rsp - 248 + 112, Arg2, Arg2 + 80, Arg4);
    result = KeQueryActiveProcessorCountEx((uint32_t)(0xFFFFULL), Arg2, Arg2 + 80, Arg4);
    local_r13 = 0;
    v_stack_m1C8 = (uint32_t)((uint32_t)((uint32_t)(result)));
    Arg4 = 0;
    v_stack_m1D8 = 0;
    Arg3 = 0;
    Arg2 = 0;
    result = KeWaitForSingleObject(v_rip + 8726097, Arg2, Arg3, Arg4);
    if ((*(uint32_t *)(arg1 + 0x10)) < 0) goto loc_00738653;
    if (*(uint64_t *)(arg1 + 0x8) == 0) goto loc_007389C1;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x138) + 0x28) == 0) goto loc_0073882D;
    if (condition_is_below) goto loc_0073882D;
    if (*(uint64_t *)(arg1) == 0) goto loc_00738814;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x138) + 0x28) == 0) goto loc_00738684;
    if (condition_is_below) goto loc_00738684;
    result = PnprLogStartEvent(*(uint64_t *)(arg1), *(uint64_t *)(arg1 + 0x8), *(uint64_t *)(arg1 + 0x8), Arg4);
loc_00738653:
    result = ExAllocatePool2(64, (uint32_t)(0x8248ULL), (uint32_t)(0x51706E50ULL), Arg4);
    if (result != 0) goto loc_007389DA;
    goto loc_00738EA9;
loc_00738684:
    result = IoAddTriageDumpDataBlock(64, *(uint16_t *)(64 + 0x2), (uint32_t)(0x51706E50ULL), Arg4);
    if (*(uint64_t *)(*(uint64_t *)(arg1) + 0x8) == 0) goto loc_007386CE;
    result = IoAddTriageDumpDataBlock(*(uint64_t *)(*(uint64_t *)(arg1) + 0x8), (int16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x8) + 0x2)), (uint32_t)(0x51706E50ULL), Arg4);
    Arg1 = (*(uint64_t *)(*(uint64_t *)(arg1) + 0x8)) + (56);
    result = *(uint64_t *)(arg1);
    if ((*(uint16_t *)(arg1)) != 0) {
        Arg2 = (uint32_t)(local_r13 + 2);
        result = IoAddTriageDumpDataBlock(Arg1, Arg2, (uint32_t)(0x51706E50ULL), Arg4);
        result = *(uint64_t *)(arg1);
        Arg1 = *(uint64_t *)(result + 0x8);
        Arg2 = *(uint16_t *)(arg1 + 0x38);
        Arg1 = *(uint64_t *)(arg1 + 0x40);
        result = IoAddTriageDumpDataBlock(Arg1, Arg2, (uint32_t)(0x51706E50ULL), Arg4);
    }
    if (*(uint64_t *)(arg1) == 0) goto loc_00738814;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x138) + 0x28)) == 0) goto loc_00738814;
    result = IoAddTriageDumpDataBlock(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x138) + 0x28), 904, (uint32_t)(0x51706E50ULL), Arg4);
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x138) + 0x28) + 0x28)) != 0) {
        Arg2 = (uint32_t)(local_r13 + 2);
        Arg1 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x138) + 0x28) + 40;
        result = IoAddTriageDumpDataBlock(Arg1, Arg2, (uint32_t)(0x51706E50ULL), Arg4);
        Arg2 = *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x138) + 0x28) + 0x28);
        Arg1 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x138) + 0x28) + 0x30);
        result = IoAddTriageDumpDataBlock(Arg1, Arg2, (uint32_t)(0x51706E50ULL), Arg4);
    }
    if (*(uint64_t *)(arg1) == 0) goto loc_00738733;
    goto loc_00738736;
loc_00738733:
loc_00738736:
    if ((*(uint16_t *)(0 + 0x38)) == 0) goto loc_00738784;
    if (*(uint64_t *)(arg1) == 0) goto loc_0073874B;
    goto loc_0073874E;
loc_0073874B:
loc_0073874E:
    Arg1 = (0) + (56);
    result = IoAddTriageDumpDataBlock(Arg1, (uint32_t)((uint32_t)(local_r13 + 2)), 0, Arg4);
    if (*(uint64_t *)(arg1) == 0) goto loc_00738771;
    goto loc_00738777;
loc_00738771:
loc_00738777:
    result = IoAddTriageDumpDataBlock(*(uint64_t *)(0 + 0x40), *(uint16_t *)(0 + 0x38), 0, Arg4);
loc_00738784:
    if (*(uint64_t *)(arg1) == 0) goto loc_0073879C;
    goto loc_0073879F;
loc_0073879C:
loc_0073879F:
    if ((*(uint64_t *)(0 + 0x10)) == 0) goto loc_00738814;
    if (*(uint64_t *)(arg1) == 0) goto loc_007387B3;
    goto loc_007387B6;
loc_007387B3:
loc_007387B6:
    if ((*(uint16_t *)(*(uint64_t *)(0 + 0x10) + 0x38)) == 0) goto loc_00738814;
    if (*(uint64_t *)(arg1) == 0) goto loc_007387CF;
    goto loc_007387D2;
loc_007387CF:
loc_007387D2:
    Arg1 = (*(uint64_t *)(0 + 0x10)) + (56);
    result = IoAddTriageDumpDataBlock(Arg1, (uint32_t)((uint32_t)(local_r13 + 2)), 0, Arg4);
    if (*(uint64_t *)(arg1) == 0) goto loc_007387F9;
    goto loc_007387FF;
loc_007387F9:
loc_007387FF:
    result = IoAddTriageDumpDataBlock(*(uint64_t *)(*(uint64_t *)(0 + 0x10) + 0x40), *(uint16_t *)(*(uint64_t *)(0 + 0x10) + 0x38), 0, Arg4);
loc_00738814:
    Arg4 = 0;
    v_stack_m1D8 = 0;
    result = KeBugCheckEx(202, local_r13 + 2, *(uint64_t *)(arg1), Arg4);
loc_0073882D:
    result = IoAddTriageDumpDataBlock(*(uint64_t *)(arg1), *(uint16_t *)(*(uint64_t *)(arg1) + 0x2), *(uint64_t *)(arg1), Arg4);
    if (*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x8) == 0) goto loc_0073887B;
    result = IoAddTriageDumpDataBlock(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x8), (int16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x8) + 0x2)), *(uint64_t *)(arg1), Arg4);
    Arg1 = (*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x8)) + (56);
    result = *(uint64_t *)((uint32_t)(0xC000009AULL));
    if ((*(uint16_t *)(arg1)) != 0) {
        Arg2 = (uint32_t)(local_r13 + 2);
        result = IoAddTriageDumpDataBlock(Arg1, Arg2, *(uint64_t *)(arg1), Arg4);
        result = *(uint64_t *)((uint32_t)(0xC000009AULL));
        Arg1 = *(uint64_t *)(result + 0x8);
        Arg2 = *(uint16_t *)(arg1 + 0x38);
        Arg1 = *(uint64_t *)(arg1 + 0x40);
        result = IoAddTriageDumpDataBlock(Arg1, Arg2, *(uint64_t *)(arg1), Arg4);
    }
    if (*(uint64_t *)((uint32_t)(0xC000009AULL)) == 0) goto loc_007389C1;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28)) == 0) goto loc_007389C1;
    result = IoAddTriageDumpDataBlock(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28), 904, *(uint64_t *)(arg1), Arg4);
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 0x28)) != 0) {
        Arg2 = (uint32_t)(local_r13 + 2);
        Arg1 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 40;
        result = IoAddTriageDumpDataBlock(Arg1, Arg2, *(uint64_t *)(arg1), Arg4);
        Arg2 = *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 0x28);
        Arg1 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 0x30);
        result = IoAddTriageDumpDataBlock(Arg1, Arg2, *(uint64_t *)(arg1), Arg4);
    }
    if (*(uint64_t *)((uint32_t)(0xC000009AULL)) == 0) goto loc_007388E0;
    goto loc_007388E3;
loc_007388E0:
loc_007388E3:
    if ((*(uint16_t *)(0 + 0x38)) == 0) goto loc_00738931;
    if (*(uint64_t *)((uint32_t)(0xC000009AULL)) == 0) goto loc_007388F8;
    goto loc_007388FB;
loc_007388F8:
loc_007388FB:
    Arg1 = (0) + (56);
    result = IoAddTriageDumpDataBlock(Arg1, (uint32_t)((uint32_t)(local_r13 + 2)), 0, Arg4);
    if (*(uint64_t *)((uint32_t)(0xC000009AULL)) == 0) goto loc_0073891E;
    goto loc_00738924;
loc_0073891E:
loc_00738924:
    result = IoAddTriageDumpDataBlock(*(uint64_t *)(0 + 0x40), *(uint16_t *)(0 + 0x38), 0, Arg4);
loc_00738931:
    if (*(uint64_t *)((uint32_t)(0xC000009AULL)) == 0) goto loc_00738949;
    goto loc_0073894C;
loc_00738949:
loc_0073894C:
    if ((*(uint64_t *)(0 + 0x10)) == 0) goto loc_007389C1;
    if (*(uint64_t *)((uint32_t)(0xC000009AULL)) == 0) goto loc_00738960;
    goto loc_00738963;
loc_00738960:
loc_00738963:
    if ((*(uint16_t *)(*(uint64_t *)(0 + 0x10) + 0x38)) == 0) goto loc_007389C1;
    if (*(uint64_t *)((uint32_t)(0xC000009AULL)) == 0) goto loc_0073897C;
    goto loc_0073897F;
loc_0073897C:
loc_0073897F:
    Arg1 = (*(uint64_t *)(0 + 0x10)) + (56);
    result = IoAddTriageDumpDataBlock(Arg1, (uint32_t)((uint32_t)(local_r13 + 2)), 0, Arg4);
    if (*(uint64_t *)((uint32_t)(0xC000009AULL)) == 0) goto loc_007389A6;
    goto loc_007389AC;
loc_007389A6:
loc_007389AC:
    result = IoAddTriageDumpDataBlock(*(uint64_t *)(*(uint64_t *)(0 + 0x10) + 0x40), *(uint16_t *)(*(uint64_t *)(0 + 0x10) + 0x38), 0, Arg4);
loc_007389C1:
    Arg4 = 0;
    v_stack_m1D8 = 0;
    result = KeBugCheckEx(202, local_r13 + 2, *(uint64_t *)((uint32_t)(0xC000009AULL)), Arg4);
loc_007389DA:
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28)) = *(uint64_t *)(arg1);
    local_rsi = 0;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 0x20) = *(uint64_t *)((uint32_t)(0xC000009AULL));
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 0x40) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x10)));
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 0x98 + 0x8) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 152;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 0x98) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 152;
    *(uint64_t *)(v_rip + 0x852226) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28);
    if ((*(uint8_t *)(v_rip + 0x88E099)) != 0) goto loc_00738A58;
    if ((*(uint32_t *)(arg1 + 0x10)) < 0) goto loc_00738A58;
    local_r13 = 0;
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 0x8208));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 0x8208))) == 0) { result = 170; }
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 0x8208) = (uint32_t)(result);
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 0x820C));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 0x820C))) == 0) { result = (uint32_t)(local_r13 + 2); }
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 0x820C) = (uint32_t)(result);
loc_00738A48:
loc_00738A4D:
    goto loc_00738EA9;
loc_00738A58:
    v_stack_m1C4 = (uint32_t)(local_r13 + 2);
    v_stack_m1C0 = local_r13 + 2;
    result = IoGetLegacyVetoList(v_stack_m1C0, v_stack_m1C4, *(uint64_t *)((uint32_t)(0xC000009AULL)), Arg4);
    local_rdi = (uint8_t)(local_r13 + 2);
    if (!(sign_flag)) {
        Arg2 = 1;
        local_rdi = (uint8_t)(local_r13 + 2);
        if (v_stack_m1C4 != ((uint32_t)(local_r13 + 2))) { local_rdi = Arg2; }
    }
    if (v_stack_m1C0 != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(v_stack_m1C0, Arg2, *(uint64_t *)((uint32_t)(0xC000009AULL)), Arg4);
    }
    if ((uint8_t)(local_rdi) == 0) goto loc_00738AD9;
    local_r13 = 0;
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x852197) + 0x8208));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x852197) + 0x8208))) == 0) { result = 182; }
loc_00738ABD:
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x852197) + 0x8208) = (uint32_t)(result);
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x852197) + 0x820C));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x852197) + 0x820C))) == 0) { result = (uint32_t)(local_r13 + 7); }
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x852197) + 0x820C) = (uint32_t)(result);
    goto loc_00738A4D;
loc_00738AD9:
    result = PnprGetMillisecondCounter(1, local_r13 + 7, *(uint64_t *)((uint32_t)(0xC000009AULL)), Arg4);
    if ((*(uint32_t *)(arg1 + 0x10)) >= ((uint32_t)(local_r13 + 2))) goto loc_00738B10;
    result = PnprLockPagesForReplace(1, local_r13 + 7, *(uint64_t *)((uint32_t)(0xC000009AULL)), Arg4);
    result = PnprQuiesceDevices(local_rsp - 248 + 112, local_r13 + 7, *(uint64_t *)((uint32_t)(0xC000009AULL)), Arg4);
    result = PnprWakeDevices(local_rsp - 248 + 112, local_r13 + 7, *(uint64_t *)((uint32_t)(0xC000009AULL)), Arg4);
    result = PnprUnlockPagesForReplace(local_rsp - 248 + 112, local_r13 + 7, *(uint64_t *)((uint32_t)(0xC000009AULL)), Arg4);
    local_r13 = 0;
    goto loc_00738A4D;
loc_00738B10:
    result = PnprIdentifyUnits(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28)), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 0x20), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 8, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 40);
    if (!sign_flag) goto loc_00738B64;
    local_r13 = 0;
    Arg1 = (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x852107) + 0x8208));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x852107) + 0x8208))) == 0) { Arg1 = 219; }
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x852107) + 0x8208) = (uint32_t)(Arg1);
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x852107) + 0x820C));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x852107) + 0x820C))) == 0) { result = (uint32_t)(local_r13 + 3); }
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x852107) + 0x820C) = (uint32_t)(result);
    goto loc_00738A4D;
loc_00738B64:
    result = PnprCollectResources(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28), 0, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 8, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 40);
    if (!sign_flag) goto loc_00738BB0;
    local_r13 = 0;
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x8520BC) + 0x8208));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x8520BC) + 0x8208))) == 0) { result = 232; }
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x8520BC) + 0x8208) = (uint32_t)(result);
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x8520BC) + 0x820C));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x8520BC) + 0x820C))) == 0) { result = (uint32_t)(local_r13 + 1); }
loc_00738BA5:
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x8520BC) + 0x820C) = (uint32_t)(result);
    goto loc_00738EA9;
loc_00738BB0:
    result = PnprLoadPluginDriver(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 33168, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 33192, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 8, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 40);
    local_r15 = 0;
    if (sign_flag) goto loc_00738C31;
    result = PnprQueryReplaceFeatures(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 33192, 0, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 8, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 40);
    local_r13 = 0;
loc_00738BE3:
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 0x18) + 0x4)) == 0) goto loc_00738D46;
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 0x81B0))))) == 0) goto loc_00738D09;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 0x81D0)) == 0) goto loc_00738D09;
    if ((((uint8_t)(1 + 1)) & ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 0x81B0))))) == 0) goto loc_00738C7D;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 0x81D8)) != 0) goto loc_00738C7D;
    goto loc_00738D0E;
loc_00738C31:
    local_r13 = 0;
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 0x18) + 0x4)) == 0) goto loc_00738BE3;
loc_00738C43:
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x851FEE) + 0x8208));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x851FEE) + 0x8208))) == 0) { result = 258; }
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x851FEE) + 0x8208) = (uint32_t)(result);
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x851FEE) + 0x820C));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x851FEE) + 0x820C))) == 0) { result = 1; }
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x851FEE) + 0x820C) = (uint32_t)(result);
    goto loc_00738EA9;
loc_00738C7D:
    result = PnprMmConstruct(*(uint64_t *)(v_rip + 0x851FEE), 1, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 8, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 40);
    if (!sign_flag) goto loc_00738C92;
    goto loc_00738C43;
loc_00738C92:
    if ((((uint8_t)((uint32_t)(v_stack_m1C8))) & (8)) == 0) goto loc_00738CA2;
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 0x38) + 0x4) = 0;
    goto loc_00738CB2;
loc_00738CA2:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 0x81F8)) == 0) goto loc_00738D02;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 0x40)))) & (32)) != 0) goto loc_00738D02;
loc_00738CB2:
    result = PnprAllocateMappingReserves(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 136, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 144, (uint32_t)((uint32_t)((uint32_t)(v_stack_m1C8))), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 40);
    if (!sign_flag) goto loc_00738CF4;
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x851F5E) + 0x8208));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x851F5E) + 0x8208))) == 0) { result = 332; }
    goto loc_00738ABD;
loc_00738CF4:
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 0xA8) = 0;
    goto loc_00738D4B;
loc_00738D02:
    goto loc_00738D0E;
loc_00738D09:
loc_00738D0E:
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x851F23) + 0x8208));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x851F23) + 0x8208))) == 0) { result = 273; }
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x851F23) + 0x8208) = (uint32_t)(result);
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x851F23) + 0x820C));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x851F23) + 0x820C))) == 0) { result = 9; }
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x851F23) + 0x820C) = (uint32_t)(result);
    goto loc_00738A48;
loc_00738D46:
loc_00738D4B:
    if (((9) & ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 0x40))))) == 0) goto loc_00738D81;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 0x8200)) != 0) goto loc_00738D81;
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x851ED6) + 0x8208));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x851ED6) + 0x8208))) == 0) { result = 352; }
    goto loc_00738ABD;
loc_00738D81:
    Arg2 = 0;
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 0xB0) = (uint32_t)((uint32_t)(v_stack_m1C8));
    v_stack_m198 = 0x200001ULL;
    result = memset(v_stack_m190, Arg2, 256, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 40);
    result = KiCopyAffinityEx(v_stack_m198, v_stack_m196, v_rip + 8971115, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 40);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 0x10) + 0x8))) == 0) goto loc_00738DF0;
    Arg2 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 0x10))) - (v_stack_m190);
loc_00738DDD:
    result = ~(*(uint64_t *)(Arg2 + v_stack_m190 * 1));
    Arg3 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 0x10) + 0x8))))) - (1);
    if (condition_is_not_equal) goto loc_00738DDD;
loc_00738DF0:
    result = KeIsEmptyAffinityEx(v_stack_m198, Arg2, Arg3, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 40);
    if ((uint32_t)(result) == 0) goto loc_00738E35;
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x851E33) + 0x8208));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x851E33) + 0x8208))) == 0) { result = 379; }
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x851E33) + 0x8208) = (uint32_t)(result);
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x851E33) + 0x820C));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x851E33) + 0x820C))) == 0) { result = 6; }
    goto loc_00738BA5;
loc_00738E35:
    Arg2 = 0;
    result = KeCheckProcessorAffinityEx(v_stack_m198, Arg2, Arg3, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 40);
    if ((uint32_t)(result) == 0) goto loc_00738E4A;
    goto loc_00738E54;
loc_00738E4A:
    result = KeFindFirstSetLeftAffinityEx(v_stack_m198, Arg2, Arg3, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 40);
loc_00738E54:
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 0xB4) = (uint32_t)(result);
    result = 0;
    v_stack_m1AE = 0;
    v_stack_m1AA = 0;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x7EA348) + (uint32_t)((uint32_t)(result)) * 4))))) >> (6));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x7EA348) + (uint32_t)((uint32_t)(result)) * 4))) & (63));
    v_stack_m1B0 = (uint16_t)(result);
    result = (1) << ((uint8_t)(Arg1));
    v_stack_m1B8 = result;
    result = KeSetSystemGroupAffinityThread(v_stack_m1B8, v_stack_m1A8, Arg3, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 40);
    result = PnprInitiateReplaceOperation(v_stack_m1B8, v_stack_m1A8, Arg3, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 40);
    result = KeRevertToUserGroupAffinityThread(v_stack_m1A8, v_stack_m1A8, Arg3, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 40);
loc_00738EA9:
    if ((*(uint32_t *)(arg1 + 0x10)) < 0) goto loc_00738ED6;
    if (sign_flag) goto loc_00738EC7;
    Arg1 = 0;
    result = PnprGetMillisecondCounter(Arg1, v_stack_m1A8, Arg3, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 40);
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 0x8240) = (uint32_t)(result);
    result = PnprLogSuccessEvent(Arg1, v_stack_m1A8, Arg3, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 40);
    goto loc_00738ED6;
loc_00738EC7:
    result = PnprLogFailureEvent(*(uint64_t *)(arg1), *(uint64_t *)(arg1 + 0x8), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 40);
loc_00738ED6:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) == 0) goto loc_00738FDC;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 0x8190) == 0) goto loc_00738F04;
    result = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 0x81B8);
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 0x81B8) != 0) {
        result = guard_dispatch_icall(*(uint64_t *)(arg1), *(uint64_t *)(arg1 + 0x8), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 40);
    }
    result = MmUnloadSystemImage(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 0x8190), *(uint64_t *)(arg1 + 0x8), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 40);
loc_00738F04:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 0x88)) == 0) goto loc_00738F67;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 0x90)) == 0) goto loc_00738F67;
    if ((uint32_t)((uint32_t)(v_stack_m1C8)) == 0) goto loc_00738F45;
loc_00738F1E:
    Arg1 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 0x88)) + (0);
    result = PnprFreeMappingReserve(Arg1, *(uint64_t *)(arg1 + 0x8), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 40);
    Arg1 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 0x90)) + (0);
    result = PnprFreeMappingReserve(Arg1, *(uint64_t *)(arg1 + 0x8), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 40);
    local_rsi = (0) + (24);
    local_r15 = ((uint32_t)(v_stack_m1C8)) - (1);
    if (condition_is_not_equal) goto loc_00738F1E;
loc_00738F45:
    result = ExFreePoolWithTag(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 0x88), (uint32_t)(0x51706E50ULL), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 40);
    result = ExFreePoolWithTag(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 0x90), (uint32_t)(0x51706E50ULL), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 40);
loc_00738F67:
    result = PnprMmFree(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 152, (uint32_t)(0x51706E50ULL), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 40);
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 0x10) != 0) {
        Arg2 = 0x51706E50ULL;
        result = ExFreePoolWithTag(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 0x10), Arg2, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 40);
        *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 0x10) = 0;
    }
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 0x18) != 0) {
        Arg2 = 0x51706E50ULL;
        result = ExFreePoolWithTag(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 0x18), Arg2, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 40);
        *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 0x18) = 0;
    }
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 0x30) != 0) {
        Arg2 = 0x51706E50ULL;
        result = ExFreePoolWithTag(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 0x30), Arg2, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 40);
        *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 0x30) = 0;
    }
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 0x38) != 0) {
        Arg2 = 0x51706E50ULL;
        result = ExFreePoolWithTag(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 0x38), Arg2, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 40);
        *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 0x38) = 0;
    }
    result = ExFreePoolWithTag(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28), (uint32_t)(0x51706E50ULL), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 40);
loc_00738FDC:
    Arg3 = 0;
    Arg2 = 0;
    result = KeSetEvent(v_rip + 8723514, Arg2, Arg3, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 40);
    *(uint32_t *)(arg1 + 0x14) = (uint32_t)((uint32_t)((uint32_t)(result)));
    Arg3 = 0;
    Arg2 = 0;
    result = KeSetEvent(Arg1 + 24, Arg2, Arg3, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 40);
    Arg1 = (*(uint64_t *)(local_rsp - 0xF8 + 0xC0)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL)) + 0x138) + 0x28) + 40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x10` | `32` | `R` |
| `Arg1` | `+ 0x14` | `32` | `W` |
| `Arg1` | `+ 0x18` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00738550&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
