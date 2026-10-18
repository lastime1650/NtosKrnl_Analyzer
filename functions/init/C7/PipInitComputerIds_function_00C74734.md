# PipInitComputerIds

- RVA: `0x00C74734`–`0x00C75C68` (길이 `5,428` bytes)
- VA: `0x0000000140C74734`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BCA14`
- 디코드: `1,342`개 명령, `5,428/5,428` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **76**; 고유 호출 대상: **29**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **25**

### Outgoing calls
- `0x00C747D7` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00C747E5` → [PipHardwareConfigOpenKey](../../page/AD/PipHardwareConfigOpenKey_function_00AD8848.md) (function, `0x00AD8848`)
- `0x00C7480C` → [PnpCtxRegDeleteTree](../../page/96/PnpCtxRegDeleteTree_function_00965CC8.md) (function, `0x00965CC8`)
- `0x00C7483C` → [IopCreateRegistryKeyEx](../../page/A8/IopCreateRegistryKeyEx_function_00A89038.md) (function, `0x00A89038`)
- `0x00C7485B` → [PnpCtxRegDeleteTree](../../page/96/PnpCtxRegDeleteTree_function_00965CC8.md) (function, `0x00965CC8`)
- `0x00C74888` → [IopCreateRegistryKeyEx](../../page/A8/IopCreateRegistryKeyEx_function_00A89038.md) (function, `0x00A89038`)
- `0x00C748BB` → [RtlFreeAnsiString](../../page/9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x00C748DC` → [MiUnmapContiguousMemory](../../text/3F/MiUnmapContiguousMemory_function_003F7908.md) (function, `0x003F7908`)
- `0x00C748E9` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x00C748FA` → [PnpCtxRegCloseKey](../../page/A2/PnpCtxRegCloseKey_function_00A22E0C.md) (function, `0x00A22E0C`)
- `0x00C74922` → [MmMapIoSpaceEx](../../text/32/MmMapIoSpaceEx_function_00327830.md) (function, `0x00327830`)
- `0x00C7494E` → [PipSmBiosFindStruct](../C3/PipSmBiosFindStruct_function_00C32528.md) (function, `0x00C32528`)
- `0x00C74984` → [PipSmBiosGetString](../C3/PipSmBiosGetString_function_00C3259C.md) (function, `0x00C3259C`)
- `0x00C749C7` → [PipSmBiosGetString](../C3/PipSmBiosGetString_function_00C3259C.md) (function, `0x00C3259C`)
- `0x00C74A06` → [PipSmBiosGetString](../C3/PipSmBiosGetString_function_00C3259C.md) (function, `0x00C3259C`)
- `0x00C74A53` → [PipSmBiosGetString](../C3/PipSmBiosGetString_function_00C3259C.md) (function, `0x00C3259C`)
- `0x00C74A92` → [PipSmBiosGetString](../C3/PipSmBiosGetString_function_00C3259C.md) (function, `0x00C3259C`)
- `0x00C74ABA` → [PipSmBiosFindStruct](../C3/PipSmBiosFindStruct_function_00C32528.md) (function, `0x00C32528`)
- `0x00C74AF3` → [PipSmBiosGetString](../C3/PipSmBiosGetString_function_00C3259C.md) (function, `0x00C3259C`)
- `0x00C74B36` → [PipSmBiosGetString](../C3/PipSmBiosGetString_function_00C3259C.md) (function, `0x00C3259C`)
- `0x00C74B5B` → [PipSmBiosFindStruct](../C3/PipSmBiosFindStruct_function_00C32528.md) (function, `0x00C32528`)
- `0x00C74B94` → [PipSmBiosGetString](../C3/PipSmBiosGetString_function_00C3259C.md) (function, `0x00C3259C`)
- `0x00C74BD7` → [PipSmBiosGetString](../C3/PipSmBiosGetString_function_00C3259C.md) (function, `0x00C3259C`)
- `0x00C74C1A` → [PipSmBiosGetString](../C3/PipSmBiosGetString_function_00C3259C.md) (function, `0x00C3259C`)
- `0x00C74C64` → [PipSmBiosFindStruct](../C3/PipSmBiosFindStruct_function_00C32528.md) (function, `0x00C32528`)
- `0x00C74CC8` → [ZwSetValueKey](../../text/6A/ZwSetValueKey_function_006ADCD0.md) (function, `0x006ADCD0`)
- `0x00C74CF7` → [RtlFreeAnsiString](../../page/9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x00C74D28` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00C74D3C` → [ZwDeleteValueKey](../../text/6A/ZwDeleteValueKey_function_006AECB0.md) (function, `0x006AECB0`)
- `0x00C74D59` → [PnpUnicodeStringToWstr](../../page/9D/PnpUnicodeStringToWstr_function_009D90C0.md) (function, `0x009D90C0`)
- `0x00C74D95` → [ZwSetValueKey](../../text/6A/ZwSetValueKey_function_006ADCD0.md) (function, `0x006ADCD0`)
- `0x00C74DA0` → [PnpUnicodeStringToWstrFree](../../page/8F/PnpUnicodeStringToWstrFree_function_008F59F0.md) (function, `0x008F59F0`)
- `0x00C74E28` → [RtlStringCchPrintfW](../../text/48/RtlStringCchPrintfW_function_00482D5C.md) (function, `0x00482D5C`)
- `0x00C74E42` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00C74EAC` → [PipCreateComputerId](../C3/PipCreateComputerId_function_00C305F4.md) (function, `0x00C305F4`)
- `0x00C74F35` → [PipCreateComputerId](../C3/PipCreateComputerId_function_00C305F4.md) (function, `0x00C305F4`)
- `0x00C74FA9` → [PipCreateComputerId](../C3/PipCreateComputerId_function_00C305F4.md) (function, `0x00C305F4`)
- `0x00C75094` → [PipCreateComputerId](../C3/PipCreateComputerId_function_00C305F4.md) (function, `0x00C305F4`)
- `0x00C7510B` → [PipCreateComputerId](../C3/PipCreateComputerId_function_00C305F4.md) (function, `0x00C305F4`)
- `0x00C7516C` → [PipCreateComputerId](../C3/PipCreateComputerId_function_00C305F4.md) (function, `0x00C305F4`)
- `0x00C75210` → [PipCreateComputerId](../C3/PipCreateComputerId_function_00C305F4.md) (function, `0x00C305F4`)
- `0x00C75266` → [PipCreateComputerId](../C3/PipCreateComputerId_function_00C305F4.md) (function, `0x00C305F4`)
- `0x00C75301` → [PipCreateComputerId](../C3/PipCreateComputerId_function_00C305F4.md) (function, `0x00C305F4`)
- `0x00C75357` → [PipCreateComputerId](../C3/PipCreateComputerId_function_00C305F4.md) (function, `0x00C305F4`)
- `0x00C753F9` → [PipCreateComputerId](../C3/PipCreateComputerId_function_00C305F4.md) (function, `0x00C305F4`)
- `0x00C7544F` → [PipCreateComputerId](../C3/PipCreateComputerId_function_00C305F4.md) (function, `0x00C305F4`)
- `0x00C7548D` → [RtlStringCchPrintfW](../../text/48/RtlStringCchPrintfW_function_00482D5C.md) (function, `0x00482D5C`)
- `0x00C754A7` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00C754EF` → [PipCreateComputerId](../C3/PipCreateComputerId_function_00C305F4.md) (function, `0x00C305F4`)
- `0x00C7557F` → [PipCreateComputerId](../C3/PipCreateComputerId_function_00C305F4.md) (function, `0x00C305F4`)
- `0x00C755C6` → [PipCreateComputerId](../C3/PipCreateComputerId_function_00C305F4.md) (function, `0x00C305F4`)
- `0x00C755E6` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C75635` → [RtlUnicodeStringCopyStringEx](../../text/5A/RtlUnicodeStringCopyStringEx_function_005A4FC0.md) (function, `0x005A4FC0`)
- `0x00C7565F` → [RtlStringFromGUIDEx](../../page/91/RtlStringFromGUIDEx_function_00915450.md) (function, `0x00915450`)
- `0x00C7567D` → [RtlUpcaseUnicodeString](../../page/96/RtlUpcaseUnicodeString_function_00960780.md) (function, `0x00960780`)
- `0x00C75700` → [PnpSetObjectProperty](../../page/8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00C75727` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C75795` → [RtlUnicodeStringCopyStringEx](../../text/5A/RtlUnicodeStringCopyStringEx_function_005A4FC0.md) (function, `0x005A4FC0`)
- `0x00C757BE` → [RtlStringFromGUIDEx](../../page/91/RtlStringFromGUIDEx_function_00915450.md) (function, `0x00915450`)
- `0x00C757DC` → [RtlUpcaseUnicodeString](../../page/96/RtlUpcaseUnicodeString_function_00960780.md) (function, `0x00960780`)
- `0x00C75831` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C75899` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00C758CA` → [RtlStringCchPrintfExW](../../text/42/RtlStringCchPrintfExW_function_0042B390.md) (function, `0x0042B390`)
- `0x00C75940` → [RtlStringCchPrintfExW](../../text/42/RtlStringCchPrintfExW_function_0042B390.md) (function, `0x0042B390`)
- `0x00C759B6` → [RtlStringCchPrintfExW](../../text/42/RtlStringCchPrintfExW_function_0042B390.md) (function, `0x0042B390`)
- `0x00C75A33` → [RtlStringCchPrintfExW](../../text/42/RtlStringCchPrintfExW_function_0042B390.md) (function, `0x0042B390`)
- `0x00C75AA0` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C75AD1` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00C75B17` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00C75BBA` → [PiSwStartCreate](../../page/73/PiSwStartCreate_function_0073B2CC.md) (function, `0x0073B2CC`)
- `0x00C75BD6` → [McTemplateK0d_EtwWriteTransfer](../../text/42/McTemplateK0d_EtwWriteTransfer_function_00423380.md) (function, `0x00423380`)
- `0x00C75BF9` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00C75C0C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00C75C1B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00C75C2E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00C75C42` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PipInitializeCoreDriversAndElam](PipInitializeCoreDriversAndElam_function_00C73F84.md) at `0x00C7406F`

### Static image references
- `0x00C7475A` → RVA `0x00E0A740` (`.data`; read)
- `0x00C747F8` → RVA `0x00E66398` (`.data`; read)
- `0x00C747FF` → RVA `0x00C7A650` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C7484E` → RVA `0x00C7A670` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C74C9D` → RVA `0x00C7A690` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C74D14` → RVA `0x00009F20` (`.rdata`; read)
- `0x00C74E0E` → RVA `0x00C7A710` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C7547A` → RVA `0x00C7A730` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C7562E` → RVA `0x00C7A740` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C756BC` → RVA `0x00C79F00` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C756D7` → RVA `0x00011550` (`.rdata`; read)
- `0x00C7576A` → RVA `0x00027AF0` (`.rdata`; read)
- `0x00C75789` → RVA `0x00C7A770` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C7588D` → RVA `0x00C7A6B0` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C758AF` → RVA `0x00C7A6C0` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C7592C` → RVA `0x00C7A6D0` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C759A2` → RVA `0x00C7A6F0` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C75A1F` → RVA `0x00C7A7E0` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C75B39` → RVA `0x000140A8` (`.rdata`; read)
- `0x00C75B42` → RVA `0x00014098` (`.rdata`; read)
- `0x00C75B49` → RVA `0x00F8C438` (`.data`; read)
- `0x00C75B8B` → RVA `0x00C7A800` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C75BAE` → RVA `0x00C7A830` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C75BC3` → RVA `0x00EF012C` (`.data`; read)
- `0x00C75BCF` → RVA `0x000272A0` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **47**
  - `0x00C747D7` → [memset](../../text/6C/memset_function_006C6C40.md) (`INIT` → `.text`)
  - `0x00C747E5` → [PipHardwareConfigOpenKey](../../page/AD/PipHardwareConfigOpenKey_function_00AD8848.md) (`INIT` → `PAGE`)
  - `0x00C7480C` → [PnpCtxRegDeleteTree](../../page/96/PnpCtxRegDeleteTree_function_00965CC8.md) (`INIT` → `PAGE`)
  - `0x00C7483C` → [IopCreateRegistryKeyEx](../../page/A8/IopCreateRegistryKeyEx_function_00A89038.md) (`INIT` → `PAGE`)
  - `0x00C7485B` → [PnpCtxRegDeleteTree](../../page/96/PnpCtxRegDeleteTree_function_00965CC8.md) (`INIT` → `PAGE`)
  - `0x00C74888` → [IopCreateRegistryKeyEx](../../page/A8/IopCreateRegistryKeyEx_function_00A89038.md) (`INIT` → `PAGE`)
  - `0x00C748BB` → [RtlFreeAnsiString](../../page/9C/RtlFreeAnsiString_function_009C0800.md) (`INIT` → `PAGE`)
  - `0x00C748DC` → [MiUnmapContiguousMemory](../../text/3F/MiUnmapContiguousMemory_function_003F7908.md) (`INIT` → `.text`)
  - `0x00C748E9` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`INIT` → `.text`)
  - `0x00C748FA` → [PnpCtxRegCloseKey](../../page/A2/PnpCtxRegCloseKey_function_00A22E0C.md) (`INIT` → `PAGE`)
  - `0x00C74922` → [MmMapIoSpaceEx](../../text/32/MmMapIoSpaceEx_function_00327830.md) (`INIT` → `.text`)
  - `0x00C74CC8` → [ZwSetValueKey](../../text/6A/ZwSetValueKey_function_006ADCD0.md) (`INIT` → `.text`)
  - `0x00C74CF7` → [RtlFreeAnsiString](../../page/9C/RtlFreeAnsiString_function_009C0800.md) (`INIT` → `PAGE`)
  - `0x00C74D28` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`INIT` → `.text`)
  - `0x00C74D3C` → [ZwDeleteValueKey](../../text/6A/ZwDeleteValueKey_function_006AECB0.md) (`INIT` → `.text`)
  - `0x00C74D59` → [PnpUnicodeStringToWstr](../../page/9D/PnpUnicodeStringToWstr_function_009D90C0.md) (`INIT` → `PAGE`)
  - `0x00C74D95` → [ZwSetValueKey](../../text/6A/ZwSetValueKey_function_006ADCD0.md) (`INIT` → `.text`)
  - `0x00C74DA0` → [PnpUnicodeStringToWstrFree](../../page/8F/PnpUnicodeStringToWstrFree_function_008F59F0.md) (`INIT` → `PAGE`)
  - `0x00C74E28` → [RtlStringCchPrintfW](../../text/48/RtlStringCchPrintfW_function_00482D5C.md) (`INIT` → `.text`)
  - `0x00C74E42` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`INIT` → `.text`)
  - `0x00C7548D` → [RtlStringCchPrintfW](../../text/48/RtlStringCchPrintfW_function_00482D5C.md) (`INIT` → `.text`)
  - `0x00C754A7` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`INIT` → `.text`)
  - `0x00C755E6` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C75635` → [RtlUnicodeStringCopyStringEx](../../text/5A/RtlUnicodeStringCopyStringEx_function_005A4FC0.md) (`INIT` → `.text`)
  - `0x00C7565F` → [RtlStringFromGUIDEx](../../page/91/RtlStringFromGUIDEx_function_00915450.md) (`INIT` → `PAGE`)
  - `0x00C7567D` → [RtlUpcaseUnicodeString](../../page/96/RtlUpcaseUnicodeString_function_00960780.md) (`INIT` → `PAGE`)
  - `0x00C75700` → [PnpSetObjectProperty](../../page/8F/PnpSetObjectProperty_function_008F66E8.md) (`INIT` → `PAGE`)
  - `0x00C75727` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C75795` → [RtlUnicodeStringCopyStringEx](../../text/5A/RtlUnicodeStringCopyStringEx_function_005A4FC0.md) (`INIT` → `.text`)
  - `0x00C757BE` → [RtlStringFromGUIDEx](../../page/91/RtlStringFromGUIDEx_function_00915450.md) (`INIT` → `PAGE`)
  - `0x00C757DC` → [RtlUpcaseUnicodeString](../../page/96/RtlUpcaseUnicodeString_function_00960780.md) (`INIT` → `PAGE`)
  - `0x00C75831` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C75899` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`INIT` → `.text`)
  - `0x00C758CA` → [RtlStringCchPrintfExW](../../text/42/RtlStringCchPrintfExW_function_0042B390.md) (`INIT` → `.text`)
  - `0x00C75940` → [RtlStringCchPrintfExW](../../text/42/RtlStringCchPrintfExW_function_0042B390.md) (`INIT` → `.text`)
  - `0x00C759B6` → [RtlStringCchPrintfExW](../../text/42/RtlStringCchPrintfExW_function_0042B390.md) (`INIT` → `.text`)
  - `0x00C75A33` → [RtlStringCchPrintfExW](../../text/42/RtlStringCchPrintfExW_function_0042B390.md) (`INIT` → `.text`)
  - `0x00C75AA0` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C75AD1` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`INIT` → `.text`)
  - `0x00C75B17` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`INIT` → `.text`)
  - `0x00C75BBA` → [PiSwStartCreate](../../page/73/PiSwStartCreate_function_0073B2CC.md) (`INIT` → `PAGE`)
  - `0x00C75BD6` → [McTemplateK0d_EtwWriteTransfer](../../text/42/McTemplateK0d_EtwWriteTransfer_function_00423380.md) (`INIT` → `.text`)
  - `0x00C75BF9` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`INIT` → `POOLCODE`)
  - `0x00C75C0C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`INIT` → `POOLCODE`)
  - `0x00C75C1B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`INIT` → `POOLCODE`)
  - `0x00C75C2E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`INIT` → `POOLCODE`)
  - `0x00C75C42` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`INIT` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C74734  48 8B C4                        mov rax, rsp
00C74737  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00C7473B  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
00C7473F  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
00C74743  55                              push rbp
00C74744  41 54                           push r12
00C74746  41 55                           push r13
00C74748  41 56                           push r14
00C7474A  41 57                           push r15
00C7474C  48 8D A8 98 FD FF FF            lea rbp, [rax - 0x268]
00C74753  48 81 EC 40 03 00 00            sub rsp, 0x340
00C7475A  48 8B 05 DF 5F 19 00            mov rax, qword ptr [rip + 0x195fdf]
00C74761  48 33 C4                        xor rax, rsp
00C74764  48 89 85 38 02 00 00            mov qword ptr [rbp + 0x238], rax
00C7476B  0F 57 C0                        xorps xmm0, xmm0
00C7476E  48 8B F9                        mov rdi, rcx
00C74771  33 C9                           xor ecx, ecx
00C74773  0F 57 C9                        xorps xmm1, xmm1
00C74776  48 89 4D C0                     mov qword ptr [rbp - 0x40], rcx
00C7477A  44 8B F1                        mov r14d, ecx
00C7477D  48 89 4D B8                     mov qword ptr [rbp - 0x48], rcx
00C74781  44 8B E1                        mov r12d, ecx
00C74784  48 89 4D D8                     mov qword ptr [rbp - 0x28], rcx
00C74788  33 C0                           xor eax, eax
00C7478A  88 4D 91                        mov byte ptr [rbp - 0x6f], cl
00C7478D  33 D2                           xor edx, edx
00C7478F  88 4D 90                        mov byte ptr [rbp - 0x70], cl
00C74792  41 B8 A0 00 00 00               mov r8d, 0xa0
00C74798  89 4D B0                        mov dword ptr [rbp - 0x50], ecx
00C7479B  89 4D C8                        mov dword ptr [rbp - 0x38], ecx
00C7479E  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
00C747A2  48 89 4D A0                     mov qword ptr [rbp - 0x60], rcx
00C747A6  48 89 4D A8                     mov qword ptr [rbp - 0x58], rcx
00C747AA  48 8D 4D 70                     lea rcx, [rbp + 0x70]
00C747AE  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
00C747B2  48 89 45 60                     mov qword ptr [rbp + 0x60], rax
00C747B6  0F 11 4D F0                     movups xmmword ptr [rbp - 0x10], xmm1
00C747BA  0F 11 45 30                     movups xmmword ptr [rbp + 0x30], xmm0
00C747BE  0F 11 45 40                     movups xmmword ptr [rbp + 0x40], xmm0
00C747C2  0F 11 45 50                     movups xmmword ptr [rbp + 0x50], xmm0
00C747C6  0F 11 45 00                     movups xmmword ptr [rbp], xmm0
00C747CA  0F 11 45 10                     movups xmmword ptr [rbp + 0x10], xmm0
00C747CE  0F 11 45 20                     movups xmmword ptr [rbp + 0x20], xmm0
00C747D2  0F 11 44 24 78                  movups xmmword ptr [rsp + 0x78], xmm0
00C747D7  E8 64 24 A5 FF                  call 0x1406c6c40
00C747DC  4C 8D 45 C0                     lea r8, [rbp - 0x40]
00C747E0  BA 3F 00 0F 00                  mov edx, 0xf003f
00C747E5  E8 5E 40 E6 FF                  call 0x140ad8848
00C747EA  4C 8B 6D C0                     mov r13, qword ptr [rbp - 0x40]
00C747EE  8B D8                           mov ebx, eax
00C747F0  85 C0                           test eax, eax
00C747F2  0F 88 B0 00 00 00               js 0x140c748a8
00C747F8  48 8B 0D 99 1B 1F 00            mov rcx, qword ptr [rip + 0x1f1b99]
00C747FF  48 8D 1D 4A 5E 00 00            lea rbx, [rip + 0x5e4a]
00C74806  4C 8B C3                        mov r8, rbx
00C74809  49 8B D5                        mov rdx, r13
00C7480C  E8 B7 14 CF FF                  call 0x140965cc8
00C74811  45 33 FF                        xor r15d, r15d
00C74814  C7 44 24 78 16 00 18 00         mov dword ptr [rsp + 0x78], 0x180016
00C7481C  4C 89 7C 24 28                  mov qword ptr [rsp + 0x28], r15
00C74821  4C 8D 44 24 78                  lea r8, [rsp + 0x78]
00C74826  41 B9 3F 00 0F 00               mov r9d, 0xf003f
00C7482C  44 89 7C 24 20                  mov dword ptr [rsp + 0x20], r15d
00C74831  49 8B D5                        mov rdx, r13
00C74834  48 89 5D 80                     mov qword ptr [rbp - 0x80], rbx
00C74838  48 8D 4D B8                     lea rcx, [rbp - 0x48]
00C7483C  E8 F7 47 E1 FF                  call 0x140a89038
00C74841  8B D8                           mov ebx, eax
00C74843  85 C0                           test eax, eax
00C74845  78 61                           js 0x140c748a8
00C74847  48 8B 0D 4A 1B 1F 00            mov rcx, qword ptr [rip + 0x1f1b4a]
00C7484E  48 8D 1D 1B 5E 00 00            lea rbx, [rip + 0x5e1b]
00C74855  4C 8B C3                        mov r8, rbx
00C74858  49 8B D5                        mov rdx, r13
00C7485B  E8 68 14 CF FF                  call 0x140965cc8
00C74860  41 B9 3F 00 0F 00               mov r9d, 0xf003f
00C74866  4C 89 7C 24 28                  mov qword ptr [rsp + 0x28], r15
00C7486B  4C 8D 44 24 78                  lea r8, [rsp + 0x78]
00C74870  C7 44 24 78 14 00 16 00         mov dword ptr [rsp + 0x78], 0x160014
00C74878  49 8B D5                        mov rdx, r13
00C7487B  48 89 5D 80                     mov qword ptr [rbp - 0x80], rbx
00C7487F  48 8D 4D D8                     lea rcx, [rbp - 0x28]
00C74883  44 89 7C 24 20                  mov dword ptr [rsp + 0x20], r15d
00C74888  E8 AB 47 E1 FF                  call 0x140a89038
00C7488D  8B D8                           mov ebx, eax
00C7488F  85 C0                           test eax, eax
00C74891  78 15                           js 0x140c748a8
00C74893  48 8B 87 F0 00 00 00            mov rax, qword ptr [rdi + 0xf0]
00C7489A  48 8B 50 38                     mov rdx, qword ptr [rax + 0x38]
00C7489E  48 85 D2                        test rdx, rdx
00C748A1  75 64                           jne 0x140c74907
00C748A3  BB BB 00 00 C0                  mov ebx, 0xc00000bb
00C748A8  41 BD 0A 00 00 00               mov r13d, 0xa
00C748AE  48 8D 7D 70                     lea rdi, [rbp + 0x70]
00C748B2  41 BF 01 00 00 00               mov r15d, 1
00C748B8  48 8B CF                        mov rcx, rdi
00C748BB  E8 40 BF D4 FF                  call 0x1409c0800
00C748C0  48 83 C7 10                     add rdi, 0x10
00C748C4  4D 2B EF                        sub r13, r15
00C748C7  75 EF                           jne 0x140c748b8
00C748C9  4C 8B 7D B8                     mov r15, qword ptr [rbp - 0x48]
00C748CD  4D 85 F6                        test r14, r14
00C748D0  74 0F                           je 0x140c748e1
00C748D2  41 8B D4                        mov edx, r12d
00C748D5  45 8D 45 01                     lea r8d, [r13 + 1]
00C748D9  49 8B CE                        mov rcx, r14
00C748DC  E8 27 30 78 FF                  call 0x1403f7908
00C748E1  4D 85 FF                        test r15, r15
00C748E4  74 08                           je 0x140c748ee
00C748E6  49 8B CF                        mov rcx, r15
00C748E9  E8 C2 89 A3 FF                  call 0x1406ad2b0
00C748EE  48 8B 45 C0                     mov rax, qword ptr [rbp - 0x40]
00C748F2  48 85 C0                        test rax, rax
00C748F5  74 08                           je 0x140c748ff
00C748F7  48 8B D0                        mov rdx, rax
00C748FA  E8 0D E5 DA FF                  call 0x140a22e0c
00C748FF  8B C3                           mov eax, ebx
00C74901  E9 32 13 00 00                  jmp 0x140c75c38
00C74906  CC                              int3
00C74907  48 8B 4A 10                     mov rcx, qword ptr [rdx + 0x10]
00C7490B  48 85 C9                        test rcx, rcx
00C7490E  74 93                           je 0x140c748a3
00C74910  44 8B 6A 0C                     mov r13d, dword ptr [rdx + 0xc]
00C74914  41 B8 02 00 00 00               mov r8d, 2
00C7491A  41 8B D5                        mov edx, r13d
00C7491D  44 89 6C 24 70                  mov dword ptr [rsp + 0x70], r13d
00C74922  E8 09 2F 6B FF                  call 0x140327830
00C74927  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
00C7492B  4C 8B E0                        mov r12, rax
00C7492E  48 85 C0                        test rax, rax
00C74931  75 10                           jne 0x140c74943
00C74933  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00C74938  4C 8B F0                        mov r14, rax
00C7493B  45 8B E5                        mov r12d, r13d
00C7493E  E9 65 FF FF FF                  jmp 0x140c748a8
00C74943  33 D2                           xor edx, edx
00C74945  45 8B CD                        mov r9d, r13d
00C74948  4D 8B C4                        mov r8, r12
00C7494B  8D 4A 01                        lea ecx, [rdx + 1]
00C7494E  E8 D5 DB FB FF                  call 0x140c32528
00C74953  48 8B F8                        mov rdi, rax
00C74956  48 85 C0                        test rax, rax
00C74959  0F 84 4E 01 00 00               je 0x140c74aad
00C7495F  0F B6 48 01                     movzx ecx, byte ptr [rax + 1]
00C74963  4C 8D 78 05                     lea r15, [rax + 5]
00C74967  48 03 C8                        add rcx, rax
00C7496A  4C 3B F9                        cmp r15, rcx
00C7496D  77 30                           ja 0x140c7499f
00C7496F  8A 57 04                        mov dl, byte ptr [rdi + 4]
00C74972  48 8D 45 70                     lea rax, [rbp + 0x70]
00C74976  45 8B CD                        mov r9d, r13d
00C74979  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00C7497E  4D 8B C4                        mov r8, r12
00C74981  48 8B CF                        mov rcx, rdi
00C74984  E8 13 DC FB FF                  call 0x140c3259c
00C74989  8B D8                           mov ebx, eax
00C7498B  3D 25 02 00 C0                  cmp eax, 0xc0000225
00C74990  75 05                           jne 0x140c74997
00C74992  41 8B DE                        mov ebx, r14d
00C74995  EB 08                           jmp 0x140c7499f
00C74997  85 C0                           test eax, eax
00C74999  0F 88 81 00 00 00               js 0x140c74a20
00C7499F  0F B6 4F 01                     movzx ecx, byte ptr [rdi + 1]
00C749A3  48 8D 47 1B                     lea rax, [rdi + 0x1b]
00C749A7  48 03 CF                        add rcx, rdi
00C749AA  48 3B C1                        cmp rax, rcx
00C749AD  77 2F                           ja 0x140c749de
00C749AF  8A 57 1A                        mov dl, byte ptr [rdi + 0x1a]
00C749B2  48 8D 85 80 00 00 00            lea rax, [rbp + 0x80]
00C749B9  45 8B CD                        mov r9d, r13d
00C749BC  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00C749C1  4D 8B C4                        mov r8, r12
00C749C4  48 8B CF                        mov rcx, rdi
00C749C7  E8 D0 DB FB FF                  call 0x140c3259c
00C749CC  8B D8                           mov ebx, eax
00C749CE  3D 25 02 00 C0                  cmp eax, 0xc0000225
00C749D3  75 05                           jne 0x140c749da
00C749D5  41 8B DE                        mov ebx, r14d
00C749D8  EB 04                           jmp 0x140c749de
00C749DA  85 C0                           test eax, eax
00C749DC  78 42                           js 0x140c74a20
00C749DE  0F B6 47 01                     movzx eax, byte ptr [rdi + 1]
00C749E2  4C 8D 77 06                     lea r14, [rdi + 6]
00C749E6  48 03 C7                        add rax, rdi
00C749E9  4C 3B F0                        cmp r14, rax
00C749EC  77 3A                           ja 0x140c74a28
00C749EE  41 8A 17                        mov dl, byte ptr [r15]
00C749F1  48 8D 85 90 00 00 00            lea rax, [rbp + 0x90]
00C749F8  45 8B CD                        mov r9d, r13d
00C749FB  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00C74A00  4D 8B C4                        mov r8, r12
00C74A03  48 8B CF                        mov rcx, rdi
00C74A06  E8 91 DB FB FF                  call 0x140c3259c
00C74A0B  45 33 FF                        xor r15d, r15d
00C74A0E  8B D8                           mov ebx, eax
00C74A10  3D 25 02 00 C0                  cmp eax, 0xc0000225
00C74A15  75 05                           jne 0x140c74a1c
00C74A17  41 8B DF                        mov ebx, r15d
00C74A1A  EB 0F                           jmp 0x140c74a2b
00C74A1C  85 C0                           test eax, eax
00C74A1E  79 0B                           jns 0x140c74a2b
00C74A20  4D 8B F4                        mov r14, r12
00C74A23  E9 13 FF FF FF                  jmp 0x140c7493b
00C74A28  45 33 FF                        xor r15d, r15d
00C74A2B  0F B6 4F 01                     movzx ecx, byte ptr [rdi + 1]
00C74A2F  48 8D 47 1A                     lea rax, [rdi + 0x1a]
00C74A33  48 03 CF                        add rcx, rdi
00C74A36  48 3B C1                        cmp rax, rcx
00C74A39  77 2F                           ja 0x140c74a6a
00C74A3B  8A 57 19                        mov dl, byte ptr [rdi + 0x19]
00C74A3E  48 8D 85 A0 00 00 00            lea rax, [rbp + 0xa0]
00C74A45  45 8B CD                        mov r9d, r13d
00C74A48  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00C74A4D  4D 8B C4                        mov r8, r12
00C74A50  48 8B CF                        mov rcx, rdi
00C74A53  E8 44 DB FB FF                  call 0x140c3259c
00C74A58  8B D8                           mov ebx, eax
00C74A5A  3D 25 02 00 C0                  cmp eax, 0xc0000225
00C74A5F  75 05                           jne 0x140c74a66
00C74A61  41 8B DF                        mov ebx, r15d
00C74A64  EB 04                           jmp 0x140c74a6a
00C74A66  85 C0                           test eax, eax
00C74A68  78 B6                           js 0x140c74a20
00C74A6A  0F B6 4F 01                     movzx ecx, byte ptr [rdi + 1]
00C74A6E  48 8D 47 07                     lea rax, [rdi + 7]
00C74A72  48 03 CF                        add rcx, rdi
00C74A75  48 3B C1                        cmp rax, rcx
00C74A78  77 33                           ja 0x140c74aad
00C74A7A  41 8A 16                        mov dl, byte ptr [r14]
00C74A7D  48 8D 85 00 01 00 00            lea rax, [rbp + 0x100]
00C74A84  45 8B CD                        mov r9d, r13d
00C74A87  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00C74A8C  4D 8B C4                        mov r8, r12
00C74A8F  48 8B CF                        mov rcx, rdi
00C74A92  E8 05 DB FB FF                  call 0x140c3259c
00C74A97  8B D8                           mov ebx, eax
00C74A99  3D 25 02 00 C0                  cmp eax, 0xc0000225
00C74A9E  75 05                           jne 0x140c74aa5
00C74AA0  41 8B DF                        mov ebx, r15d
00C74AA3  EB 08                           jmp 0x140c74aad
00C74AA5  85 C0                           test eax, eax
00C74AA7  0F 88 73 FF FF FF               js 0x140c74a20
00C74AAD  45 8B CD                        mov r9d, r13d
00C74AB0  4D 8B C4                        mov r8, r12
00C74AB3  B2 0A                           mov dl, 0xa
00C74AB5  B9 02 00 00 00                  mov ecx, 2
00C74ABA  E8 69 DA FB FF                  call 0x140c32528
00C74ABF  48 8B F8                        mov rdi, rax
00C74AC2  48 85 C0                        test rax, rax
00C74AC5  0F 84 86 00 00 00               je 0x140c74b51
00C74ACB  0F B6 48 01                     movzx ecx, byte ptr [rax + 1]
00C74ACF  4C 8D 70 05                     lea r14, [rax + 5]
00C74AD3  48 03 C8                        add rcx, rax
00C74AD6  4C 3B F1                        cmp r14, rcx
00C74AD9  77 33                           ja 0x140c74b0e
00C74ADB  8A 57 04                        mov dl, byte ptr [rdi + 4]
00C74ADE  48 8D 85 D0 00 00 00            lea rax, [rbp + 0xd0]
00C74AE5  45 8B CD                        mov r9d, r13d
00C74AE8  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00C74AED  4D 8B C4                        mov r8, r12
00C74AF0  48 8B CF                        mov rcx, rdi
00C74AF3  E8 A4 DA FB FF                  call 0x140c3259c
00C74AF8  8B D8                           mov ebx, eax
00C74AFA  3D 25 02 00 C0                  cmp eax, 0xc0000225
00C74AFF  75 05                           jne 0x140c74b06
00C74B01  41 8B DF                        mov ebx, r15d
00C74B04  EB 08                           jmp 0x140c74b0e
00C74B06  85 C0                           test eax, eax
00C74B08  0F 88 12 FF FF FF               js 0x140c74a20
00C74B0E  0F B6 4F 01                     movzx ecx, byte ptr [rdi + 1]
00C74B12  48 8D 47 06                     lea rax, [rdi + 6]
00C74B16  48 03 CF                        add rcx, rdi
00C74B19  48 3B C1                        cmp rax, rcx
00C74B1C  77 33                           ja 0x140c74b51
00C74B1E  41 8A 16                        mov dl, byte ptr [r14]
00C74B21  48 8D 85 E0 00 00 00            lea rax, [rbp + 0xe0]
00C74B28  45 8B CD                        mov r9d, r13d
00C74B2B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00C74B30  4D 8B C4                        mov r8, r12
00C74B33  48 8B CF                        mov rcx, rdi
00C74B36  E8 61 DA FB FF                  call 0x140c3259c
00C74B3B  8B D8                           mov ebx, eax
00C74B3D  3D 25 02 00 C0                  cmp eax, 0xc0000225
00C74B42  75 05                           jne 0x140c74b49
00C74B44  41 8B DF                        mov ebx, r15d
00C74B47  EB 08                           jmp 0x140c74b51
00C74B49  85 C0                           test eax, eax
00C74B4B  0F 88 CF FE FF FF               js 0x140c74a20
00C74B51  45 8B CD                        mov r9d, r13d
00C74B54  4D 8B C4                        mov r8, r12
00C74B57  33 D2                           xor edx, edx
00C74B59  33 C9                           xor ecx, ecx
00C74B5B  E8 C8 D9 FB FF                  call 0x140c32528
00C74B60  48 8B F8                        mov rdi, rax
00C74B63  48 85 C0                        test rax, rax
00C74B66  0F 84 ED 00 00 00               je 0x140c74c59
00C74B6C  0F B6 48 01                     movzx ecx, byte ptr [rax + 1]
00C74B70  4C 8D 70 05                     lea r14, [rax + 5]
00C74B74  48 03 C8                        add rcx, rax
00C74B77  4C 3B F1                        cmp r14, rcx
00C74B7A  77 33                           ja 0x140c74baf
00C74B7C  8A 57 04                        mov dl, byte ptr [rdi + 4]
00C74B7F  48 8D 85 B0 00 00 00            lea rax, [rbp + 0xb0]
00C74B86  45 8B CD                        mov r9d, r13d
00C74B89  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00C74B8E  4D 8B C4                        mov r8, r12
00C74B91  48 8B CF                        mov rcx, rdi
00C74B94  E8 03 DA FB FF                  call 0x140c3259c
00C74B99  8B D8                           mov ebx, eax
00C74B9B  3D 25 02 00 C0                  cmp eax, 0xc0000225
00C74BA0  75 05                           jne 0x140c74ba7
00C74BA2  41 8B DF                        mov ebx, r15d
00C74BA5  EB 08                           jmp 0x140c74baf
00C74BA7  85 C0                           test eax, eax
00C74BA9  0F 88 71 FE FF FF               js 0x140c74a20
00C74BAF  0F B6 4F 01                     movzx ecx, byte ptr [rdi + 1]
00C74BB3  48 8D 47 06                     lea rax, [rdi + 6]
00C74BB7  48 03 CF                        add rcx, rdi
00C74BBA  48 3B C1                        cmp rax, rcx
00C74BBD  77 33                           ja 0x140c74bf2
00C74BBF  41 8A 16                        mov dl, byte ptr [r14]
00C74BC2  48 8D 85 C0 00 00 00            lea rax, [rbp + 0xc0]
00C74BC9  45 8B CD                        mov r9d, r13d
00C74BCC  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00C74BD1  4D 8B C4                        mov r8, r12
00C74BD4  48 8B CF                        mov rcx, rdi
00C74BD7  E8 C0 D9 FB FF                  call 0x140c3259c
00C74BDC  8B D8                           mov ebx, eax
00C74BDE  3D 25 02 00 C0                  cmp eax, 0xc0000225
00C74BE3  75 05                           jne 0x140c74bea
00C74BE5  41 8B DF                        mov ebx, r15d
00C74BE8  EB 08                           jmp 0x140c74bf2
00C74BEA  85 C0                           test eax, eax
00C74BEC  0F 88 2E FE FF FF               js 0x140c74a20
00C74BF2  0F B6 4F 01                     movzx ecx, byte ptr [rdi + 1]
00C74BF6  48 8D 47 09                     lea rax, [rdi + 9]
00C74BFA  48 03 CF                        add rcx, rdi
00C74BFD  48 3B C1                        cmp rax, rcx
00C74C00  77 33                           ja 0x140c74c35
00C74C02  8A 57 08                        mov dl, byte ptr [rdi + 8]
00C74C05  48 8D 85 F0 00 00 00            lea rax, [rbp + 0xf0]
00C74C0C  45 8B CD                        mov r9d, r13d
00C74C0F  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00C74C14  4D 8B C4                        mov r8, r12
00C74C17  48 8B CF                        mov rcx, rdi
00C74C1A  E8 7D D9 FB FF                  call 0x140c3259c
00C74C1F  8B D8                           mov ebx, eax
00C74C21  3D 25 02 00 C0                  cmp eax, 0xc0000225
00C74C26  75 05                           jne 0x140c74c2d
00C74C28  41 8B DF                        mov ebx, r15d
00C74C2B  EB 08                           jmp 0x140c74c35
00C74C2D  85 C0                           test eax, eax
00C74C2F  0F 88 EB FD FF FF               js 0x140c74a20
00C74C35  0F B6 57 01                     movzx edx, byte ptr [rdi + 1]
00C74C39  48 8D 4F 15                     lea rcx, [rdi + 0x15]
00C74C3D  48 03 D7                        add rdx, rdi
00C74C40  48 3B CA                        cmp rcx, rdx
00C74C43  77 06                           ja 0x140c74c4b
00C74C45  8A 47 14                        mov al, byte ptr [rdi + 0x14]
00C74C48  88 45 91                        mov byte ptr [rbp - 0x6f], al
00C74C4B  48 8D 47 16                     lea rax, [rdi + 0x16]
00C74C4F  48 3B C2                        cmp rax, rdx
00C74C52  77 05                           ja 0x140c74c59
00C74C54  8A 01                           mov al, byte ptr [rcx]
00C74C56  88 45 90                        mov byte ptr [rbp - 0x70], al
00C74C59  33 D2                           xor edx, edx
00C74C5B  45 8B CD                        mov r9d, r13d
00C74C5E  4D 8B C4                        mov r8, r12
00C74C61  8D 4A 03                        lea ecx, [rdx + 3]
00C74C64  E8 BF D8 FB FF                  call 0x140c32528
00C74C69  45 33 E4                        xor r12d, r12d
00C74C6C  48 85 C0                        test rax, rax
00C74C6F  74 1C                           je 0x140c74c8d
00C74C71  0F B6 50 01                     movzx edx, byte ptr [rax + 1]
00C74C75  48 8D 48 06                     lea rcx, [rax + 6]
00C74C79  48 03 D0                        add rdx, rax
00C74C7C  48 3B CA                        cmp rcx, rdx
00C74C7F  77 0C                           ja 0x140c74c8d
00C74C81  0F B6 40 05                     movzx eax, byte ptr [rax + 5]
00C74C85  83 E0 7F                        and eax, 0x7f
00C74C88  89 45 B0                        mov dword ptr [rbp - 0x50], eax
00C74C8B  EB 03                           jmp 0x140c74c90
00C74C8D  8B 45 B0                        mov eax, dword ptr [rbp - 0x50]
00C74C90  B9 04 00 00 00                  mov ecx, 4
00C74C95  85 C0                           test eax, eax
00C74C97  74 34                           je 0x140c74ccd
00C74C99  89 4C 24 28                     mov dword ptr [rsp + 0x28], ecx
00C74C9D  48 8D 05 EC 59 00 00            lea rax, [rip + 0x59ec]
00C74CA4  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
00C74CA8  48 8D 54 24 78                  lea rdx, [rsp + 0x78]
00C74CAD  48 8D 45 B0                     lea rax, [rbp - 0x50]
00C74CB1  C7 44 24 78 1A 00 1C 00         mov dword ptr [rsp + 0x78], 0x1c001a
00C74CB9  44 8B C9                        mov r9d, ecx
00C74CBC  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00C74CC1  48 8B 4D C0                     mov rcx, qword ptr [rbp - 0x40]
00C74CC5  45 33 C0                        xor r8d, r8d
00C74CC8  E8 03 90 A3 FF                  call 0x1406adcd0
00C74CCD  B8 01 00 00 00                  mov eax, 1
00C74CD2  48 8D 7D 70                     lea rdi, [rbp + 0x70]
00C74CD6  45 8B F4                        mov r14d, r12d
00C74CD9  44 8D 68 09                     lea r13d, [rax + 9]
00C74CDD  4C 39 67 08                     cmp qword ptr [rdi + 8], r12
00C74CE1  74 1E                           je 0x140c74d01
00C74CE3  66 44 39 27                     cmp word ptr [rdi], r12w
00C74CE7  75 18                           jne 0x140c74d01
00C74CE9  41 8B C6                        mov eax, r14d
00C74CEC  48 8D 4D 70                     lea rcx, [rbp + 0x70]
00C74CF0  48 C1 E0 04                     shl rax, 4
00C74CF4  48 03 C8                        add rcx, rax
00C74CF7  E8 04 BB D4 FF                  call 0x1409c0800
00C74CFC  B8 01 00 00 00                  mov eax, 1
00C74D01  44 03 F0                        add r14d, eax
00C74D04  48 83 C7 10                     add rdi, 0x10
00C74D08  45 3B F5                        cmp r14d, r13d
00C74D0B  72 D0                           jb 0x140c74cdd
00C74D0D  41 8B FC                        mov edi, r12d
00C74D10  4C 8D 75 70                     lea r14, [rbp + 0x70]
00C74D14  4C 8D 3D 05 52 39 FF            lea r15, [rip - 0xc6adfb]
00C74D1B  BE 01 00 00 00                  mov esi, 1
00C74D20  49 8B 17                        mov rdx, qword ptr [r15]
00C74D23  48 8D 4C 24 78                  lea rcx, [rsp + 0x78]
00C74D28  E8 53 5A 7B FF                  call 0x14042a780
00C74D2D  66 45 39 26                     cmp word ptr [r14], r12w
00C74D31  75 10                           jne 0x140c74d43
00C74D33  48 8B 4D C0                     mov rcx, qword ptr [rbp - 0x40]
00C74D37  48 8D 54 24 78                  lea rdx, [rsp + 0x78]
00C74D3C  E8 6F 9F A3 FF                  call 0x1406aecb0
00C74D41  EB 6B                           jmp 0x140c74dae
00C74D43  8B C7                           mov eax, edi
00C74D45  4C 8D 6D 70                     lea r13, [rbp + 0x70]
00C74D49  48 C1 E0 04                     shl rax, 4
00C74D4D  48 8D 4D A8                     lea rcx, [rbp - 0x58]
00C74D51  4C 03 E8                        add r13, rax
00C74D54  33 D2                           xor edx, edx
00C74D56  4D 8B C5                        mov r8, r13
00C74D59  E8 62 43 D6 FF                  call 0x1409d90c0
00C74D5E  85 C0                           test eax, eax
00C74D60  78 46                           js 0x140c74da8
00C74D62  4C 8B 65 A8                     mov r12, qword ptr [rbp - 0x58]
00C74D66  48 83 C8 FF                     or rax, 0xffffffffffffffff
00C74D6A  33 C9                           xor ecx, ecx
00C74D6C  48 FF C0                        inc rax
00C74D6F  66 41 39 0C 44                  cmp word ptr [r12 + rax*2], cx
00C74D74  75 F6                           jne 0x140c74d6c
00C74D76  48 8B 4D C0                     mov rcx, qword ptr [rbp - 0x40]
00C74D7A  8D 04 45 02 00 00 00            lea eax, [rax*2 + 2]
00C74D81  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
00C74D85  48 8D 54 24 78                  lea rdx, [rsp + 0x78]
00C74D8A  44 8B CE                        mov r9d, esi
00C74D8D  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00C74D92  45 33 C0                        xor r8d, r8d
00C74D95  E8 36 8F A3 FF                  call 0x1406adcd0
00C74D9A  49 8B D5                        mov rdx, r13
00C74D9D  49 8B CC                        mov rcx, r12
00C74DA0  E8 4B 0C C8 FF                  call 0x1408f59f0
00C74DA5  45 33 E4                        xor r12d, r12d
00C74DA8  41 BD 0A 00 00 00               mov r13d, 0xa
00C74DAE  03 FE                           add edi, esi
00C74DB0  49 83 C7 08                     add r15, 8
00C74DB4  49 83 C6 10                     add r14, 0x10
00C74DB8  41 3B FD                        cmp edi, r13d
00C74DBB  0F 82 5F FF FF FF               jb 0x140c74d20
00C74DC1  48 8B 45 78                     mov rax, qword ptr [rbp + 0x78]
00C74DC5  4C 8B 7D B8                     mov r15, qword ptr [rbp - 0x48]
00C74DC9  8B 75 C8                        mov esi, dword ptr [rbp - 0x38]
00C74DCC  48 85 C0                        test rax, rax
00C74DCF  0F 84 FE 07 00 00               je 0x140c755d3
00C74DD5  41 BA 06 00 00 00               mov r10d, 6
00C74DDB  48 8B 7D D8                     mov rdi, qword ptr [rbp - 0x28]
00C74DDF  4C 39 A5 98 00 00 00            cmp qword ptr [rbp + 0x98], r12
00C74DE6  0F 84 DF 01 00 00               je 0x140c74fcb
00C74DEC  4C 39 A5 B8 00 00 00            cmp qword ptr [rbp + 0xb8], r12
00C74DF3  0F 84 D2 01 00 00               je 0x140c74fcb
00C74DF9  45 8D 72 02                     lea r14d, [r10 + 2]
00C74DFD  4C 39 A5 C8 00 00 00            cmp qword ptr [rbp + 0xc8], r12
00C74E04  0F 84 C7 01 00 00               je 0x140c74fd1
00C74E0A  0F B6 45 90                     movzx eax, byte ptr [rbp - 0x70]
00C74E0E  4C 8D 05 FB 58 00 00            lea r8, [rip + 0x58fb]
00C74E15  44 0F B6 4D 91                  movzx r9d, byte ptr [rbp - 0x6f]
00C74E1A  48 8D 8D 28 02 00 00            lea rcx, [rbp + 0x228]
00C74E21  41 8B D6                        mov edx, r14d
00C74E24  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00C74E28  E8 2F DF 80 FF                  call 0x140482d5c
00C74E2D  8B D8                           mov ebx, eax
00C74E2F  85 C0                           test eax, eax
00C74E31  0F 88 C3 07 00 00               js 0x140c755fa
00C74E37  48 8D 95 28 02 00 00            lea rdx, [rbp + 0x228]
00C74E3E  48 8D 4D E0                     lea rcx, [rbp - 0x20]
00C74E42  E8 39 59 7B FF                  call 0x14042a780
00C74E47  4C 39 A5 A8 00 00 00            cmp qword ptr [rbp + 0xa8], r12
00C74E4E  74 75                           je 0x140c74ec5
00C74E50  48 8D 45 70                     lea rax, [rbp + 0x70]
00C74E54  48 89 45 30                     mov qword ptr [rbp + 0x30], rax
00C74E58  48 8D 8D 90 00 00 00            lea rcx, [rbp + 0x90]
00C74E5F  48 8D 85 80 00 00 00            lea rax, [rbp + 0x80]
00C74E66  48 89 45 38                     mov qword ptr [rbp + 0x38], rax
00C74E6A  41 8D 56 FC                     lea edx, [r14 - 4]
00C74E6E  48 8D 45 40                     lea rax, [rbp + 0x40]
00C74E72  48 89 08                        mov qword ptr [rax], rcx
00C74E75  48 83 C1 10                     add rcx, 0x10
00C74E79  49 03 C6                        add rax, r14
00C74E7C  48 83 EA 01                     sub rdx, 1
00C74E80  75 F0                           jne 0x140c74e72
00C74E82  48 8D 45 E0                     lea rax, [rbp - 0x20]
00C74E86  66 44 89 A5 00 02 00 00         mov word ptr [rbp + 0x200], r12w
00C74E8E  48 89 45 60                     mov qword ptr [rbp + 0x60], rax
00C74E92  44 8D 4A 07                     lea r9d, [rdx + 7]
00C74E96  48 8D 85 10 01 00 00            lea rax, [rbp + 0x110]
00C74E9D  48 8B D7                        mov rdx, rdi
00C74EA0  4C 8D 45 30                     lea r8, [rbp + 0x30]
00C74EA4  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00C74EA9  49 8B CF                        mov rcx, r15
00C74EAC  E8 43 B7 FB FF                  call 0x140c305f4
00C74EB1  41 B9 01 00 00 00               mov r9d, 1
00C74EB7  8B D8                           mov ebx, eax
00C74EB9  41 8B F1                        mov esi, r9d
00C74EBC  85 C0                           test eax, eax
00C74EBE  79 0B                           jns 0x140c74ecb
00C74EC0  E9 35 07 00 00                  jmp 0x140c755fa
00C74EC5  41 B9 01 00 00 00               mov r9d, 1
00C74ECB  48 8D 45 70                     lea rax, [rbp + 0x70]
00C74ECF  48 8B D7                        mov rdx, rdi
00C74ED2  48 89 45 30                     mov qword ptr [rbp + 0x30], rax
00C74ED6  48 8D 8D 10 01 00 00            lea rcx, [rbp + 0x110]
00C74EDD  48 8D 85 80 00 00 00            lea rax, [rbp + 0x80]
00C74EE4  48 89 45 38                     mov qword ptr [rbp + 0x38], rax
00C74EE8  4C 8D 45 30                     lea r8, [rbp + 0x30]
00C74EEC  48 8D 85 90 00 00 00            lea rax, [rbp + 0x90]
00C74EF3  48 89 45 40                     mov qword ptr [rbp + 0x40], rax
00C74EF7  48 8D 85 B0 00 00 00            lea rax, [rbp + 0xb0]
00C74EFE  48 89 45 48                     mov qword ptr [rbp + 0x48], rax
00C74F02  48 8D 85 C0 00 00 00            lea rax, [rbp + 0xc0]
00C74F09  48 89 45 50                     mov qword ptr [rbp + 0x50], rax
00C74F0D  48 8D 45 E0                     lea rax, [rbp - 0x20]
00C74F11  48 89 45 58                     mov qword ptr [rbp + 0x58], rax
00C74F15  8B C6                           mov eax, esi
00C74F17  66 44 89 8C 45 00 02 00 00      mov word ptr [rbp + rax*2 + 0x200], r9w
00C74F20  41 B9 06 00 00 00               mov r9d, 6
00C74F26  48 C1 E0 04                     shl rax, 4
00C74F2A  48 03 C1                        add rax, rcx
00C74F2D  49 8B CF                        mov rcx, r15
00C74F30  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00C74F35  E8 BA B6 FB FF                  call 0x140c305f4
00C74F3A  FF C6                           inc esi
00C74F3C  8B D8                           mov ebx, eax
00C74F3E  85 C0                           test eax, eax
00C74F40  0F 88 B4 06 00 00               js 0x140c755fa
00C74F46  48 8D 45 70                     lea rax, [rbp + 0x70]
00C74F4A  B9 02 00 00 00                  mov ecx, 2
00C74F4F  48 89 45 30                     mov qword ptr [rbp + 0x30], rax
00C74F53  4C 8D 45 30                     lea r8, [rbp + 0x30]
00C74F57  66 89 8C 75 00 02 00 00         mov word ptr [rbp + rsi*2 + 0x200], cx
00C74F5F  48 8D 85 90 00 00 00            lea rax, [rbp + 0x90]
00C74F66  48 89 45 38                     mov qword ptr [rbp + 0x38], rax
00C74F6A  48 8D 8D 10 01 00 00            lea rcx, [rbp + 0x110]
00C74F71  48 8D 85 B0 00 00 00            lea rax, [rbp + 0xb0]
00C74F78  41 B9 05 00 00 00               mov r9d, 5
00C74F7E  48 89 45 40                     mov qword ptr [rbp + 0x40], rax
00C74F82  48 8B D7                        mov rdx, rdi
00C74F85  48 8D 85 C0 00 00 00            lea rax, [rbp + 0xc0]
00C74F8C  48 89 45 48                     mov qword ptr [rbp + 0x48], rax
00C74F90  48 8D 45 E0                     lea rax, [rbp - 0x20]
00C74F94  48 89 45 50                     mov qword ptr [rbp + 0x50], rax
00C74F98  8B C6                           mov eax, esi
00C74F9A  48 C1 E0 04                     shl rax, 4
00C74F9E  48 03 C1                        add rax, rcx
00C74FA1  49 8B CF                        mov rcx, r15
00C74FA4  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00C74FA9  E8 46 B6 FB FF                  call 0x140c305f4
00C74FAE  41 B9 01 00 00 00               mov r9d, 1
00C74FB4  8B D8                           mov ebx, eax
00C74FB6  41 03 F1                        add esi, r9d
00C74FB9  85 C0                           test eax, eax
00C74FBB  0F 88 39 06 00 00               js 0x140c755fa
00C74FC1  48 8B 45 78                     mov rax, qword ptr [rbp + 0x78]
00C74FC5  45 8D 51 05                     lea r10d, [r9 + 5]
00C74FC9  EB 0C                           jmp 0x140c74fd7
00C74FCB  41 BE 08 00 00 00               mov r14d, 8
00C74FD1  41 B9 01 00 00 00               mov r9d, 1
00C74FD7  48 85 C0                        test rax, rax
00C74FDA  0F 84 F3 05 00 00               je 0x140c755d3
00C74FE0  4C 39 A5 98 00 00 00            cmp qword ptr [rbp + 0x98], r12
00C74FE7  0F 84 9B 01 00 00               je 0x140c75188
00C74FED  4C 39 A5 A8 00 00 00            cmp qword ptr [rbp + 0xa8], r12
00C74FF4  0F 84 22 01 00 00               je 0x140c7511c
00C74FFA  4C 39 A5 D8 00 00 00            cmp qword ptr [rbp + 0xd8], r12
00C75001  0F 84 A5 00 00 00               je 0x140c750ac
00C75007  4C 39 A5 E8 00 00 00            cmp qword ptr [rbp + 0xe8], r12
00C7500E  0F 84 98 00 00 00               je 0x140c750ac
00C75014  48 8D 45 70                     lea rax, [rbp + 0x70]
00C75018  41 B8 02 00 00 00               mov r8d, 2
00C7501E  48 89 45 30                     mov qword ptr [rbp + 0x30], rax
00C75022  48 8D 8D 90 00 00 00            lea rcx, [rbp + 0x90]
00C75029  48 8D 85 80 00 00 00            lea rax, [rbp + 0x80]
00C75030  41 8B D0                        mov edx, r8d
00C75033  48 89 45 38                     mov qword ptr [rbp + 0x38], rax
00C75037  48 8D 45 40                     lea rax, [rbp + 0x40]
00C7503B  48 89 08                        mov qword ptr [rax], rcx
00C7503E  48 83 C1 10                     add rcx, 0x10
00C75042  49 03 C6                        add rax, r14
00C75045  49 2B D1                        sub rdx, r9
00C75048  75 F1                           jne 0x140c7503b
00C7504A  48 8D 45 50                     lea rax, [rbp + 0x50]
00C7504E  49 8B D0                        mov rdx, r8
00C75051  48 8D 8D D0 00 00 00            lea rcx, [rbp + 0xd0]
00C75058  48 89 08                        mov qword ptr [rax], rcx
00C7505B  48 83 C1 10                     add rcx, 0x10
00C7505F  49 03 C6                        add rax, r14
00C75062  49 2B D1                        sub rdx, r9
00C75065  75 F1                           jne 0x140c75058
00C75067  8D 4A 03                        lea ecx, [rdx + 3]
00C7506A  8B C6                           mov eax, esi
00C7506C  45 8B CA                        mov r9d, r10d
00C7506F  4C 8D 45 30                     lea r8, [rbp + 0x30]
00C75073  48 8B D7                        mov rdx, rdi
00C75076  66 89 8C 45 00 02 00 00         mov word ptr [rbp + rax*2 + 0x200], cx
00C7507E  48 8D 8D 10 01 00 00            lea rcx, [rbp + 0x110]
00C75085  48 C1 E0 04                     shl rax, 4
00C75089  48 03 C1                        add rax, rcx
00C7508C  49 8B CF                        mov rcx, r15
00C7508F  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00C75094  E8 5B B5 FB FF                  call 0x140c305f4
00C75099  41 B9 01 00 00 00               mov r9d, 1
00C7509F  8B D8                           mov ebx, eax
00C750A1  41 03 F1                        add esi, r9d
00C750A4  85 C0                           test eax, eax
00C750A6  0F 88 4E 05 00 00               js 0x140c755fa
00C750AC  48 8D 45 70                     lea rax, [rbp + 0x70]
00C750B0  BA 02 00 00 00                  mov edx, 2
00C750B5  48 89 45 30                     mov qword ptr [rbp + 0x30], rax
00C750B9  48 8D 8D 90 00 00 00            lea rcx, [rbp + 0x90]
00C750C0  48 8D 85 80 00 00 00            lea rax, [rbp + 0x80]
00C750C7  48 89 45 38                     mov qword ptr [rbp + 0x38], rax
00C750CB  48 8D 45 40                     lea rax, [rbp + 0x40]
00C750CF  48 89 08                        mov qword ptr [rax], rcx
00C750D2  48 83 C1 10                     add rcx, 0x10
00C750D6  49 03 C6                        add rax, r14
00C750D9  49 2B D1                        sub rdx, r9
00C750DC  75 F1                           jne 0x140c750cf
00C750DE  8D 4A 04                        lea ecx, [rdx + 4]
00C750E1  8B C6                           mov eax, esi
00C750E3  48 8D 95 10 01 00 00            lea rdx, [rbp + 0x110]
00C750EA  44 8B C9                        mov r9d, ecx
00C750ED  4C 8D 45 30                     lea r8, [rbp + 0x30]
00C750F1  66 89 8C 45 00 02 00 00         mov word ptr [rbp + rax*2 + 0x200], cx
00C750F9  49 8B CF                        mov rcx, r15
00C750FC  48 C1 E0 04                     shl rax, 4
00C75100  48 03 C2                        add rax, rdx
00C75103  48 8B D7                        mov rdx, rdi
00C75106  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00C7510B  E8 E4 B4 FB FF                  call 0x140c305f4
00C75110  FF C6                           inc esi
00C75112  8B D8                           mov ebx, eax
00C75114  85 C0                           test eax, eax
00C75116  0F 88 DE 04 00 00               js 0x140c755fa
00C7511C  48 8D 45 70                     lea rax, [rbp + 0x70]
00C75120  B9 05 00 00 00                  mov ecx, 5
00C75125  48 89 45 30                     mov qword ptr [rbp + 0x30], rax
00C75129  4C 8D 45 30                     lea r8, [rbp + 0x30]
00C7512D  48 8D 85 80 00 00 00            lea rax, [rbp + 0x80]
00C75134  41 B9 03 00 00 00               mov r9d, 3
00C7513A  48 89 45 38                     mov qword ptr [rbp + 0x38], rax
00C7513E  48 8B D7                        mov rdx, rdi
00C75141  48 8D 85 90 00 00 00            lea rax, [rbp + 0x90]
00C75148  48 89 45 40                     mov qword ptr [rbp + 0x40], rax
00C7514C  8B C6                           mov eax, esi
00C7514E  66 89 8C 45 00 02 00 00         mov word ptr [rbp + rax*2 + 0x200], cx
00C75156  48 8D 8D 10 01 00 00            lea rcx, [rbp + 0x110]
00C7515D  48 C1 E0 04                     shl rax, 4
00C75161  48 03 C1                        add rax, rcx
00C75164  49 8B CF                        mov rcx, r15
00C75167  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00C7516C  E8 83 B4 FB FF                  call 0x140c305f4
00C75171  41 B9 01 00 00 00               mov r9d, 1
00C75177  8B D8                           mov ebx, eax
00C75179  41 03 F1                        add esi, r9d
00C7517C  85 C0                           test eax, eax
00C7517E  0F 88 76 04 00 00               js 0x140c755fa
00C75184  48 8B 45 78                     mov rax, qword ptr [rbp + 0x78]
00C75188  48 85 C0                        test rax, rax
00C7518B  0F 84 42 04 00 00               je 0x140c755d3
00C75191  4C 39 A5 A8 00 00 00            cmp qword ptr [rbp + 0xa8], r12
00C75198  0F 84 E4 00 00 00               je 0x140c75282
00C7519E  4C 39 A5 D8 00 00 00            cmp qword ptr [rbp + 0xd8], r12
00C751A5  74 7A                           je 0x140c75221
00C751A7  4C 39 A5 E8 00 00 00            cmp qword ptr [rbp + 0xe8], r12
00C751AE  74 71                           je 0x140c75221
00C751B0  48 8D 45 70                     lea rax, [rbp + 0x70]
00C751B4  BA 02 00 00 00                  mov edx, 2
00C751B9  48 89 45 30                     mov qword ptr [rbp + 0x30], rax
00C751BD  48 8D 8D D0 00 00 00            lea rcx, [rbp + 0xd0]
00C751C4  48 8D 85 A0 00 00 00            lea rax, [rbp + 0xa0]
00C751CB  48 89 45 38                     mov qword ptr [rbp + 0x38], rax
00C751CF  48 8D 45 40                     lea rax, [rbp + 0x40]
00C751D3  48 89 08                        mov qword ptr [rax], rcx
00C751D6  48 83 C1 10                     add rcx, 0x10
00C751DA  49 03 C6                        add rax, r14
00C751DD  49 2B D1                        sub rdx, r9
00C751E0  75 F1                           jne 0x140c751d3
00C751E2  8D 4A 06                        lea ecx, [rdx + 6]
00C751E5  8B C6                           mov eax, esi
00C751E7  44 8D 4A 04                     lea r9d, [rdx + 4]
00C751EB  48 8B D7                        mov rdx, rdi
00C751EE  4C 8D 45 30                     lea r8, [rbp + 0x30]
00C751F2  66 89 8C 45 00 02 00 00         mov word ptr [rbp + rax*2 + 0x200], cx
00C751FA  48 8D 8D 10 01 00 00            lea rcx, [rbp + 0x110]
00C75201  48 C1 E0 04                     shl rax, 4
00C75205  48 03 C1                        add rax, rcx
00C75208  49 8B CF                        mov rcx, r15
00C7520B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00C75210  E8 DF B3 FB FF                  call 0x140c305f4
00C75215  FF C6                           inc esi
00C75217  8B D8                           mov ebx, eax
00C75219  85 C0                           test eax, eax
00C7521B  0F 88 D9 03 00 00               js 0x140c755fa
00C75221  48 8D 45 70                     lea rax, [rbp + 0x70]
00C75225  B9 07 00 00 00                  mov ecx, 7
00C7522A  48 89 45 30                     mov qword ptr [rbp + 0x30], rax
00C7522E  4C 8D 45 30                     lea r8, [rbp + 0x30]
00C75232  48 8D 85 A0 00 00 00            lea rax, [rbp + 0xa0]
00C75239  41 B9 02 00 00 00               mov r9d, 2
00C7523F  48 89 45 38                     mov qword ptr [rbp + 0x38], rax
00C75243  48 8B D7                        mov rdx, rdi
00C75246  8B C6                           mov eax, esi
00C75248  66 89 8C 45 00 02 00 00         mov word ptr [rbp + rax*2 + 0x200], cx
00C75250  48 8D 8D 10 01 00 00            lea rcx, [rbp + 0x110]
00C75257  48 C1 E0 04                     shl rax, 4
00C7525B  48 03 C1                        add rax, rcx
00C7525E  49 8B CF                        mov rcx, r15
00C75261  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00C75266  E8 89 B3 FB FF                  call 0x140c305f4
00C7526B  41 B9 01 00 00 00               mov r9d, 1
00C75271  8B D8                           mov ebx, eax
00C75273  41 03 F1                        add esi, r9d
00C75276  85 C0                           test eax, eax
00C75278  0F 88 7C 03 00 00               js 0x140c755fa
00C7527E  48 8B 45 78                     mov rax, qword ptr [rbp + 0x78]
00C75282  48 85 C0                        test rax, rax
00C75285  0F 84 48 03 00 00               je 0x140c755d3
00C7528B  4C 39 A5 98 00 00 00            cmp qword ptr [rbp + 0x98], r12
00C75292  0F 84 DB 00 00 00               je 0x140c75373
00C75298  4C 39 A5 D8 00 00 00            cmp qword ptr [rbp + 0xd8], r12
00C7529F  74 71                           je 0x140c75312
00C752A1  4C 39 A5 E8 00 00 00            cmp qword ptr [rbp + 0xe8], r12
00C752A8  74 68                           je 0x140c75312
00C752AA  48 8D 45 70                     lea rax, [rbp + 0x70]
00C752AE  41 B9 04 00 00 00               mov r9d, 4
00C752B4  48 89 45 30                     mov qword ptr [rbp + 0x30], rax
00C752B8  48 8D 8D 10 01 00 00            lea rcx, [rbp + 0x110]
00C752BF  48 8D 85 90 00 00 00            lea rax, [rbp + 0x90]
00C752C6  48 8B D7                        mov rdx, rdi
00C752C9  48 89 45 38                     mov qword ptr [rbp + 0x38], rax
00C752CD  4C 8D 45 30                     lea r8, [rbp + 0x30]
00C752D1  48 8D 85 D0 00 00 00            lea rax, [rbp + 0xd0]
00C752D8  48 89 45 40                     mov qword ptr [rbp + 0x40], rax
00C752DC  48 8D 85 E0 00 00 00            lea rax, [rbp + 0xe0]
00C752E3  48 89 45 48                     mov qword ptr [rbp + 0x48], rax
00C752E7  8B C6                           mov eax, esi
00C752E9  66 44 89 B4 45 00 02 00 00      mov word ptr [rbp + rax*2 + 0x200], r14w
00C752F2  48 C1 E0 04                     shl rax, 4
00C752F6  48 03 C1                        add rax, rcx
00C752F9  49 8B CF                        mov rcx, r15
00C752FC  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00C75301  E8 EE B2 FB FF                  call 0x140c305f4
00C75306  FF C6                           inc esi
00C75308  8B D8                           mov ebx, eax
00C7530A  85 C0                           test eax, eax
00C7530C  0F 88 E8 02 00 00               js 0x140c755fa
00C75312  48 8D 45 70                     lea rax, [rbp + 0x70]
00C75316  B9 09 00 00 00                  mov ecx, 9
00C7531B  48 89 45 30                     mov qword ptr [rbp + 0x30], rax
00C7531F  4C 8D 45 30                     lea r8, [rbp + 0x30]
00C75323  48 8D 85 90 00 00 00            lea rax, [rbp + 0x90]
00C7532A  41 B9 02 00 00 00               mov r9d, 2
00C75330  48 89 45 38                     mov qword ptr [rbp + 0x38], rax
00C75334  48 8B D7                        mov rdx, rdi
00C75337  8B C6                           mov eax, esi
00C75339  66 89 8C 45 00 02 00 00         mov word ptr [rbp + rax*2 + 0x200], cx
00C75341  48 8D 8D 10 01 00 00            lea rcx, [rbp + 0x110]
00C75348  48 C1 E0 04                     shl rax, 4
00C7534C  48 03 C1                        add rax, rcx
00C7534F  49 8B CF                        mov rcx, r15
00C75352  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00C75357  E8 98 B2 FB FF                  call 0x140c305f4
00C7535C  41 B9 01 00 00 00               mov r9d, 1
00C75362  8B D8                           mov ebx, eax
00C75364  41 03 F1                        add esi, r9d
00C75367  85 C0                           test eax, eax
00C75369  0F 88 8B 02 00 00               js 0x140c755fa
00C7536F  48 8B 45 78                     mov rax, qword ptr [rbp + 0x78]
00C75373  48 85 C0                        test rax, rax
00C75376  0F 84 57 02 00 00               je 0x140c755d3
00C7537C  4C 39 A5 88 00 00 00            cmp qword ptr [rbp + 0x88], r12
00C75383  0F 84 DB 00 00 00               je 0x140c75464
00C75389  4C 39 A5 E8 00 00 00            cmp qword ptr [rbp + 0xe8], r12
00C75390  74 78                           je 0x140c7540a
00C75392  4C 39 A5 D8 00 00 00            cmp qword ptr [rbp + 0xd8], r12
00C75399  74 6F                           je 0x140c7540a
00C7539B  48 8D 45 70                     lea rax, [rbp + 0x70]
00C7539F  BA 02 00 00 00                  mov edx, 2
00C753A4  48 89 45 30                     mov qword ptr [rbp + 0x30], rax
00C753A8  48 8D 8D D0 00 00 00            lea rcx, [rbp + 0xd0]
00C753AF  48 8D 85 80 00 00 00            lea rax, [rbp + 0x80]
00C753B6  48 89 45 38                     mov qword ptr [rbp + 0x38], rax
00C753BA  48 8D 45 40                     lea rax, [rbp + 0x40]
00C753BE  48 89 08                        mov qword ptr [rax], rcx
00C753C1  48 83 C1 10                     add rcx, 0x10
00C753C5  49 03 C6                        add rax, r14
00C753C8  49 2B D1                        sub rdx, r9
00C753CB  75 F1                           jne 0x140c753be
00C753CD  8B C6                           mov eax, esi
00C753CF  48 8D 8D 10 01 00 00            lea rcx, [rbp + 0x110]
00C753D6  44 8D 4A 04                     lea r9d, [rdx + 4]
00C753DA  48 8B D7                        mov rdx, rdi
00C753DD  4C 8D 45 30                     lea r8, [rbp + 0x30]
00C753E1  66 44 89 AC 45 00 02 00 00      mov word ptr [rbp + rax*2 + 0x200], r13w
00C753EA  48 C1 E0 04                     shl rax, 4
00C753EE  48 03 C1                        add rax, rcx
00C753F1  49 8B CF                        mov rcx, r15
00C753F4  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00C753F9  E8 F6 B1 FB FF                  call 0x140c305f4
00C753FE  FF C6                           inc esi
00C75400  8B D8                           mov ebx, eax
00C75402  85 C0                           test eax, eax
00C75404  0F 88 F0 01 00 00               js 0x140c755fa
00C7540A  48 8D 45 70                     lea rax, [rbp + 0x70]
00C7540E  B9 0B 00 00 00                  mov ecx, 0xb
00C75413  48 89 45 30                     mov qword ptr [rbp + 0x30], rax
00C75417  4C 8D 45 30                     lea r8, [rbp + 0x30]
00C7541B  48 8D 85 80 00 00 00            lea rax, [rbp + 0x80]
00C75422  41 B9 02 00 00 00               mov r9d, 2
00C75428  48 89 45 38                     mov qword ptr [rbp + 0x38], rax
00C7542C  48 8B D7                        mov rdx, rdi
00C7542F  8B C6                           mov eax, esi
00C75431  66 89 8C 45 00 02 00 00         mov word ptr [rbp + rax*2 + 0x200], cx
00C75439  48 8D 8D 10 01 00 00            lea rcx, [rbp + 0x110]
00C75440  48 C1 E0 04                     shl rax, 4
00C75444  48 03 C1                        add rax, rcx
00C75447  49 8B CF                        mov rcx, r15
00C7544A  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00C7544F  E8 A0 B1 FB FF                  call 0x140c305f4
00C75454  FF C6                           inc esi
00C75456  8B D8                           mov ebx, eax
00C75458  85 C0                           test eax, eax
00C7545A  0F 88 9A 01 00 00               js 0x140c755fa
00C75460  48 8B 45 78                     mov rax, qword ptr [rbp + 0x78]
00C75464  48 85 C0                        test rax, rax
00C75467  0F 84 66 01 00 00               je 0x140c755d3
00C7546D  44 8B 4D B0                     mov r9d, dword ptr [rbp - 0x50]
00C75471  45 85 C9                        test r9d, r9d
00C75474  0F 84 91 00 00 00               je 0x140c7550b
00C7547A  4C 8D 05 AF 52 00 00            lea r8, [rip + 0x52af]
00C75481  BA 04 00 00 00                  mov edx, 4
00C75486  48 8D 8D 20 02 00 00            lea rcx, [rbp + 0x220]
00C7548D  E8 CA D8 80 FF                  call 0x140482d5c
00C75492  8B D8                           mov ebx, eax
00C75494  85 C0                           test eax, eax
00C75496  0F 88 5E 01 00 00               js 0x140c755fa
00C7549C  48 8D 95 20 02 00 00            lea rdx, [rbp + 0x220]
00C754A3  48 8D 4D F0                     lea rcx, [rbp - 0x10]
00C754A7  E8 D4 52 7B FF                  call 0x14042a780
00C754AC  48 8D 45 70                     lea rax, [rbp + 0x70]
00C754B0  B9 0C 00 00 00                  mov ecx, 0xc
00C754B5  48 89 45 30                     mov qword ptr [rbp + 0x30], rax
00C754B9  4C 8D 45 30                     lea r8, [rbp + 0x30]
00C754BD  48 8D 45 F0                     lea rax, [rbp - 0x10]
00C754C1  BF 02 00 00 00                  mov edi, 2
00C754C6  48 89 45 38                     mov qword ptr [rbp + 0x38], rax
00C754CA  44 8B CF                        mov r9d, edi
00C754CD  8B C6                           mov eax, esi
00C754CF  33 D2                           xor edx, edx
00C754D1  66 89 8C 45 00 02 00 00         mov word ptr [rbp + rax*2 + 0x200], cx
00C754D9  48 8D 8D 10 01 00 00            lea rcx, [rbp + 0x110]
00C754E0  48 C1 E0 04                     shl rax, 4
00C754E4  48 03 C1                        add rax, rcx
00C754E7  49 8B CF                        mov rcx, r15
00C754EA  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00C754EF  E8 00 B1 FB FF                  call 0x140c305f4
00C754F4  44 8D 4F FF                     lea r9d, [rdi - 1]
00C754F8  8B D8                           mov ebx, eax
00C754FA  41 03 F1                        add esi, r9d
00C754FD  85 C0                           test eax, eax
00C754FF  0F 88 F5 00 00 00               js 0x140c755fa
00C75505  48 8B 45 78                     mov rax, qword ptr [rbp + 0x78]
00C75509  EB 09                           jmp 0x140c75514
00C7550B  BF 02 00 00 00                  mov edi, 2
00C75510  44 8D 4F FF                     lea r9d, [rdi - 1]
00C75514  48 85 C0                        test rax, rax
00C75517  0F 84 B6 00 00 00               je 0x140c755d3
00C7551D  4C 39 A5 E8 00 00 00            cmp qword ptr [rbp + 0xe8], r12
00C75524  74 6D                           je 0x140c75593
00C75526  4C 39 A5 D8 00 00 00            cmp qword ptr [rbp + 0xd8], r12
00C7552D  74 64                           je 0x140c75593
00C7552F  48 8D 45 70                     lea rax, [rbp + 0x70]
00C75533  48 8B D7                        mov rdx, rdi
00C75536  48 89 45 30                     mov qword ptr [rbp + 0x30], rax
00C7553A  48 8D 8D D0 00 00 00            lea rcx, [rbp + 0xd0]
00C75541  48 8D 45 38                     lea rax, [rbp + 0x38]
00C75545  48 89 08                        mov qword ptr [rax], rcx
00C75548  48 83 C1 10                     add rcx, 0x10
00C7554C  49 03 C6                        add rax, r14
00C7554F  49 2B D1                        sub rdx, r9
00C75552  75 F1                           jne 0x140c75545
00C75554  8D 4A 0D                        lea ecx, [rdx + 0xd]
00C75557  8B C6                           mov eax, esi
00C75559  44 8D 4A 03                     lea r9d, [rdx + 3]
00C7555D  4C 8D 45 30                     lea r8, [rbp + 0x30]
00C75561  66 89 8C 45 00 02 00 00         mov word ptr [rbp + rax*2 + 0x200], cx
00C75569  48 8D 8D 10 01 00 00            lea rcx, [rbp + 0x110]
00C75570  48 C1 E0 04                     shl rax, 4
00C75574  48 03 C1                        add rax, rcx
00C75577  49 8B CF                        mov rcx, r15
00C7557A  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00C7557F  E8 70 B0 FB FF                  call 0x140c305f4
00C75584  41 B9 01 00 00 00               mov r9d, 1
00C7558A  8B D8                           mov ebx, eax
00C7558C  41 03 F1                        add esi, r9d
00C7558F  85 C0                           test eax, eax
00C75591  78 67                           js 0x140c755fa
00C75593  48 8D 45 70                     lea rax, [rbp + 0x70]
00C75597  B9 0E 00 00 00                  mov ecx, 0xe
00C7559C  48 89 45 30                     mov qword ptr [rbp + 0x30], rax
00C755A0  4C 8D 45 30                     lea r8, [rbp + 0x30]
00C755A4  8B C6                           mov eax, esi
00C755A6  33 D2                           xor edx, edx
00C755A8  66 89 8C 45 00 02 00 00         mov word ptr [rbp + rax*2 + 0x200], cx
00C755B0  48 8D 8D 10 01 00 00            lea rcx, [rbp + 0x110]
00C755B7  48 C1 E0 04                     shl rax, 4
00C755BB  48 03 C1                        add rax, rcx
00C755BE  49 8B CF                        mov rcx, r15
00C755C1  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00C755C6  E8 29 B0 FB FF                  call 0x140c305f4
00C755CB  FF C6                           inc esi
00C755CD  8B D8                           mov ebx, eax
00C755CF  85 C0                           test eax, eax
00C755D1  78 27                           js 0x140c755fa
00C755D3  6B FE 70                        imul edi, esi, 0x70
00C755D6  B9 00 01 00 00                  mov ecx, 0x100
00C755DB  41 B8 50 70 69 6E               mov r8d, 0x6e697050
00C755E1  83 C7 02                        add edi, 2
00C755E4  8B D7                           mov edx, edi
00C755E6  E8 05 CB F0 FF                  call 0x140b820f0
00C755EB  33 C9                           xor ecx, ecx
00C755ED  4C 8B E0                        mov r12, rax
00C755F0  48 85 C0                        test rax, rax
00C755F3  75 13                           jne 0x140c75608
00C755F5  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00C755FA  4C 8B 75 88                     mov r14, qword ptr [rbp - 0x78]
00C755FE  44 8B 64 24 70                  mov r12d, dword ptr [rsp + 0x70]
00C75603  E9 A6 F2 FF FF                  jmp 0x140c748ae
00C75608  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
00C7560C  44 8B F1                        mov r14d, ecx
00C7560F  66 89 7C 24 7A                  mov word ptr [rsp + 0x7a], di
00C75614  85 F6                           test esi, esi
00C75616  0F 84 94 00 00 00               je 0x140c756b0
00C7561C  66 89 4C 24 78                  mov word ptr [rsp + 0x78], cx
00C75621  4C 8D 44 24 78                  lea r8, [rsp + 0x78]
00C75626  48 8D 4C 24 78                  lea rcx, [rsp + 0x78]
00C7562B  45 33 C9                        xor r9d, r9d
00C7562E  48 8D 15 0B 51 00 00            lea rdx, [rip + 0x510b]
00C75635  E8 86 F9 92 FF                  call 0x1405a4fc0
00C7563A  33 C9                           xor ecx, ecx
00C7563C  8B D8                           mov ebx, eax
00C7563E  85 C0                           test eax, eax
00C75640  0F 88 97 05 00 00               js 0x140c75bdd
00C75646  41 8B C6                        mov eax, r14d
00C75649  48 8D 8D 10 01 00 00            lea rcx, [rbp + 0x110]
00C75650  48 C1 E0 04                     shl rax, 4
00C75654  48 8D 54 24 78                  lea rdx, [rsp + 0x78]
00C75659  48 03 C8                        add rcx, rax
00C7565C  45 33 C0                        xor r8d, r8d
00C7565F  E8 EC FD C9 FF                  call 0x140915450
00C75664  8B D8                           mov ebx, eax
00C75666  33 C0                           xor eax, eax
00C75668  85 DB                           test ebx, ebx
00C7566A  0F 88 75 05 00 00               js 0x140c75be5
00C75670  45 33 C0                        xor r8d, r8d
00C75673  48 8D 54 24 78                  lea rdx, [rsp + 0x78]
00C75678  48 8D 4C 24 78                  lea rcx, [rsp + 0x78]
00C7567D  E8 FE B0 CE FF                  call 0x140960780
00C75682  33 C9                           xor ecx, ecx
00C75684  8B D8                           mov ebx, eax
00C75686  85 C0                           test eax, eax
00C75688  0F 88 4F 05 00 00               js 0x140c75bdd
00C7568E  48 8B 45 80                     mov rax, qword ptr [rbp - 0x80]
00C75692  BA B2 FF 00 00                  mov edx, 0xffb2
00C75697  66 01 54 24 7A                  add word ptr [rsp + 0x7a], dx
00C7569C  48 83 C0 4E                     add rax, 0x4e
00C756A0  41 FF C6                        inc r14d
00C756A3  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
00C756A7  44 3B F6                        cmp r14d, esi
00C756AA  0F 82 6C FF FF FF               jb 0x140c7561c
00C756B0  85 DB                           test ebx, ebx
00C756B2  0F 88 35 05 00 00               js 0x140c75bed
00C756B8  89 4C 24 48                     mov dword ptr [rsp + 0x48], ecx
00C756BC  48 8D 15 3D 48 00 00            lea rdx, [rip + 0x483d]
00C756C3  89 7C 24 40                     mov dword ptr [rsp + 0x40], edi
00C756C7  41 BE 02 00 00 00               mov r14d, 2
00C756CD  66 89 08                        mov word ptr [rax], cx
00C756D0  45 33 C9                        xor r9d, r9d
00C756D3  4C 01 75 80                     add qword ptr [rbp - 0x80], r14
00C756D7  48 8D 05 72 BE 39 FF            lea rax, [rip - 0xc6418e]
00C756DE  4C 89 64 24 38                  mov qword ptr [rsp + 0x38], r12
00C756E3  C7 44 24 30 12 20 00 00         mov dword ptr [rsp + 0x30], 0x2012
00C756EB  45 8D 46 03                     lea r8d, [r14 + 3]
00C756EF  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00C756F4  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00C756F9  48 8B 0D 98 0C 1F 00            mov rcx, qword ptr [rip + 0x1f0c98]
00C75700  E8 E3 0F C8 FF                  call 0x1408f66e8
00C75705  8B D8                           mov ebx, eax
00C75707  33 C0                           xor eax, eax
00C75709  85 DB                           test ebx, ebx
00C7570B  0F 88 D4 04 00 00               js 0x140c75be5
00C75711  8D 1C 76                        lea ebx, [rsi + rsi*2]
00C75714  B9 00 01 00 00                  mov ecx, 0x100
00C75719  C1 E3 05                        shl ebx, 5
00C7571C  41 B8 50 70 69 6E               mov r8d, 0x6e697050
00C75722  41 03 DE                        add ebx, r14d
00C75725  8B D3                           mov edx, ebx
00C75727  E8 C4 C9 F0 FF                  call 0x140b820f0
00C7572C  45 33 C0                        xor r8d, r8d
00C7572F  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
00C75733  48 85 C0                        test rax, rax
00C75736  75 10                           jne 0x140c75748
00C75738  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00C7573D  49 8B F0                        mov rsi, r8
00C75740  4D 8B F0                        mov r14, r8
00C75743  E9 AC 04 00 00                  jmp 0x140c75bf4
00C75748  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
00C7574C  48 8B C8                        mov rcx, rax
00C7574F  66 89 5C 24 7A                  mov word ptr [rsp + 0x7a], bx
00C75754  41 8B F8                        mov edi, r8d
00C75757  85 F6                           test esi, esi
00C75759  0F 84 B9 00 00 00               je 0x140c75818
00C7575F  4C 8D B5 00 02 00 00            lea r14, [rbp + 0x200]
00C75766  41 0F B7 06                     movzx eax, word ptr [r14]
00C7576A  48 8D 15 7F 23 3B FF            lea rdx, [rip - 0xc4dc81]
00C75771  66 44 89 44 24 78               mov word ptr [rsp + 0x78], r8w
00C75777  44 38 04 10                     cmp byte ptr [rax + rdx], r8b
00C7577B  0F 84 83 00 00 00               je 0x140c75804
00C75781  45 33 C9                        xor r9d, r9d
00C75784  4C 8D 44 24 78                  lea r8, [rsp + 0x78]
00C75789  48 8D 15 E0 4F 00 00            lea rdx, [rip + 0x4fe0]
00C75790  48 8D 4C 24 78                  lea rcx, [rsp + 0x78]
00C75795  E8 26 F8 92 FF                  call 0x1405a4fc0
00C7579A  8B D8                           mov ebx, eax
00C7579C  33 C0                           xor eax, eax
00C7579E  85 DB                           test ebx, ebx
00C757A0  0F 88 3F 04 00 00               js 0x140c75be5
00C757A6  8B C7                           mov eax, edi
00C757A8  48 8D 8D 10 01 00 00            lea rcx, [rbp + 0x110]
00C757AF  48 C1 E0 04                     shl rax, 4
00C757B3  48 8D 54 24 78                  lea rdx, [rsp + 0x78]
00C757B8  48 03 C8                        add rcx, rax
00C757BB  45 33 C0                        xor r8d, r8d
00C757BE  E8 8D FC C9 FF                  call 0x140915450
00C757C3  8B D8                           mov ebx, eax
00C757C5  33 C0                           xor eax, eax
00C757C7  85 DB                           test ebx, ebx
00C757C9  0F 88 16 04 00 00               js 0x140c75be5
00C757CF  45 33 C0                        xor r8d, r8d
00C757D2  48 8D 54 24 78                  lea rdx, [rsp + 0x78]
00C757D7  48 8D 4C 24 78                  lea rcx, [rsp + 0x78]
00C757DC  E8 9F AF CE FF                  call 0x140960780
00C757E1  45 33 C0                        xor r8d, r8d
00C757E4  8B D8                           mov ebx, eax
00C757E6  85 C0                           test eax, eax
00C757E8  0F 88 4F FF FF FF               js 0x140c7573d
00C757EE  48 8B 4D 80                     mov rcx, qword ptr [rbp - 0x80]
00C757F2  B8 B2 FF 00 00                  mov eax, 0xffb2
00C757F7  48 83 C1 4E                     add rcx, 0x4e
00C757FB  66 01 44 24 7A                  add word ptr [rsp + 0x7a], ax
00C75800  48 89 4D 80                     mov qword ptr [rbp - 0x80], rcx
00C75804  FF C7                           inc edi
00C75806  49 83 C6 02                     add r14, 2
00C7580A  3B FE                           cmp edi, esi
00C7580C  0F 82 54 FF FF FF               jb 0x140c75766
00C75812  41 BE 02 00 00 00               mov r14d, 2
00C75818  33 FF                           xor edi, edi
00C7581A  BA 90 01 00 00                  mov edx, 0x190
00C7581F  66 89 39                        mov word ptr [rcx], di
00C75822  41 B8 50 70 69 6E               mov r8d, 0x6e697050
00C75828  4C 01 75 80                     add qword ptr [rbp - 0x80], r14
00C7582C  B9 00 01 00 00                  mov ecx, 0x100
00C75831  E8 BA C8 F0 FF                  call 0x140b820f0
00C75836  4C 8B F0                        mov r14, rax
00C75839  48 85 C0                        test rax, rax
00C7583C  75 0D                           jne 0x140c7584b
00C7583E  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00C75843  48 8B F7                        mov rsi, rdi
00C75846  E9 A9 03 00 00                  jmp 0x140c75bf4
00C7584B  0F B7 4D 70                     movzx ecx, word ptr [rbp + 0x70]
00C7584F  BE 46 00 00 00                  mov esi, 0x46
00C75854  BB C8 00 00 00                  mov ebx, 0xc8
00C75859  4C 89 75 A8                     mov qword ptr [rbp - 0x58], r14
00C7585D  48 89 5D 98                     mov qword ptr [rbp - 0x68], rbx
00C75861  8D 46 BC                        lea eax, [rsi - 0x44]
00C75864  66 3B C8                        cmp cx, ax
00C75867  76 24                           jbe 0x140c7588d
00C75869  48 8B 45 78                     mov rax, qword ptr [rbp + 0x78]
00C7586D  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
00C75871  0F B7 45 72                     movzx eax, word ptr [rbp + 0x72]
00C75875  66 89 44 24 7A                  mov word ptr [rsp + 0x7a], ax
00C7587A  66 3B CE                        cmp cx, si
00C7587D  76 07                           jbe 0x140c75886
00C7587F  66 89 74 24 78                  mov word ptr [rsp + 0x78], si
00C75884  EB 18                           jmp 0x140c7589e
00C75886  66 89 4C 24 78                  mov word ptr [rsp + 0x78], cx
00C7588B  EB 11                           jmp 0x140c7589e
00C7588D  48 8D 15 1C 4E 00 00            lea rdx, [rip + 0x4e1c]
00C75894  48 8D 4C 24 78                  lea rcx, [rsp + 0x78]
00C75899  E8 E2 4E 7B FF                  call 0x14042a780
00C7589E  48 8D 44 24 78                  lea rax, [rsp + 0x78]
00C758A3  48 8B D3                        mov rdx, rbx
00C758A6  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00C758AB  4C 8D 4D 98                     lea r9, [rbp - 0x68]
00C758AF  48 8D 05 0A 4E 00 00            lea rax, [rip + 0x4e0a]
00C758B6  49 8B CE                        mov rcx, r14
00C758B9  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00C758BE  4C 8D 45 A8                     lea r8, [rbp - 0x58]
00C758C2  C7 44 24 20 00 08 00 00         mov dword ptr [rsp + 0x20], 0x800
00C758CA  E8 C1 5A 7B FF                  call 0x14042b390
00C758CF  8B D8                           mov ebx, eax
00C758D1  85 C0                           test eax, eax
00C758D3  0F 88 6A FF FF FF               js 0x140c75843
00C758D9  0F B7 8D 80 00 00 00            movzx ecx, word ptr [rbp + 0x80]
00C758E0  41 B9 02 00 00 00               mov r9d, 2
00C758E6  66 41 3B C9                     cmp cx, r9w
00C758EA  76 69                           jbe 0x140c75955
00C758EC  48 8B 85 88 00 00 00            mov rax, qword ptr [rbp + 0x88]
00C758F3  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
00C758F7  0F B7 85 82 00 00 00            movzx eax, word ptr [rbp + 0x82]
00C758FE  66 89 44 24 7A                  mov word ptr [rsp + 0x7a], ax
00C75903  66 89 74 24 78                  mov word ptr [rsp + 0x78], si
00C75908  66 3B CE                        cmp cx, si
00C7590B  77 05                           ja 0x140c75912
00C7590D  66 89 4C 24 78                  mov word ptr [rsp + 0x78], cx
00C75912  48 8B 55 98                     mov rdx, qword ptr [rbp - 0x68]
00C75916  48 8D 44 24 78                  lea rax, [rsp + 0x78]
00C7591B  48 8B 4D A8                     mov rcx, qword ptr [rbp - 0x58]
00C7591F  4C 8D 4D 98                     lea r9, [rbp - 0x68]
00C75923  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00C75928  4C 8D 45 A8                     lea r8, [rbp - 0x58]
00C7592C  48 8D 05 9D 4D 00 00            lea rax, [rip + 0x4d9d]
00C75933  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00C75938  C7 44 24 20 00 08 00 00         mov dword ptr [rsp + 0x20], 0x800
00C75940  E8 4B 5A 7B FF                  call 0x14042b390
00C75945  8B D8                           mov ebx, eax
00C75947  85 C0                           test eax, eax
00C75949  0F 88 F4 FE FF FF               js 0x140c75843
00C7594F  41 B9 02 00 00 00               mov r9d, 2
00C75955  0F B7 8D 90 00 00 00            movzx ecx, word ptr [rbp + 0x90]
00C7595C  66 41 3B C9                     cmp cx, r9w
00C75960  76 70                           jbe 0x140c759d2
00C75962  48 8B 85 98 00 00 00            mov rax, qword ptr [rbp + 0x98]
00C75969  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
00C7596D  0F B7 85 92 00 00 00            movzx eax, word ptr [rbp + 0x92]
00C75974  66 89 44 24 7A                  mov word ptr [rsp + 0x7a], ax
00C75979  66 89 74 24 78                  mov word ptr [rsp + 0x78], si
00C7597E  66 3B CE                        cmp cx, si
00C75981  77 05                           ja 0x140c75988
00C75983  66 89 4C 24 78                  mov word ptr [rsp + 0x78], cx
00C75988  48 8B 55 98                     mov rdx, qword ptr [rbp - 0x68]
00C7598C  48 8D 44 24 78                  lea rax, [rsp + 0x78]
00C75991  48 8B 4D A8                     mov rcx, qword ptr [rbp - 0x58]
00C75995  4C 8D 4D 98                     lea r9, [rbp - 0x68]
00C75999  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00C7599E  4C 8D 45 A8                     lea r8, [rbp - 0x58]
00C759A2  48 8D 05 47 4D 00 00            lea rax, [rip + 0x4d47]
00C759A9  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00C759AE  C7 44 24 20 00 08 00 00         mov dword ptr [rsp + 0x20], 0x800
00C759B6  E8 D5 59 7B FF                  call 0x14042b390
00C759BB  8B D8                           mov ebx, eax
00C759BD  85 C0                           test eax, eax
00C759BF  0F 88 7E FE FF FF               js 0x140c75843
00C759C5  0F B7 8D 90 00 00 00            movzx ecx, word ptr [rbp + 0x90]
00C759CC  41 B9 02 00 00 00               mov r9d, 2
00C759D2  0F B7 95 A0 00 00 00            movzx edx, word ptr [rbp + 0xa0]
00C759D9  66 41 3B D1                     cmp dx, r9w
00C759DD  76 70                           jbe 0x140c75a4f
00C759DF  48 8B 85 A8 00 00 00            mov rax, qword ptr [rbp + 0xa8]
00C759E6  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
00C759EA  0F B7 85 A2 00 00 00            movzx eax, word ptr [rbp + 0xa2]
00C759F1  66 89 44 24 7A                  mov word ptr [rsp + 0x7a], ax
00C759F6  66 89 74 24 78                  mov word ptr [rsp + 0x78], si
00C759FB  66 3B D6                        cmp dx, si
00C759FE  77 05                           ja 0x140c75a05
00C75A00  66 89 54 24 78                  mov word ptr [rsp + 0x78], dx
00C75A05  48 8B 55 98                     mov rdx, qword ptr [rbp - 0x68]
00C75A09  48 8D 44 24 78                  lea rax, [rsp + 0x78]
00C75A0E  48 8B 4D A8                     mov rcx, qword ptr [rbp - 0x58]
00C75A12  4C 8D 4D 98                     lea r9, [rbp - 0x68]
00C75A16  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00C75A1B  4C 8D 45 A8                     lea r8, [rbp - 0x58]
00C75A1F  48 8D 05 BA 4D 00 00            lea rax, [rip + 0x4dba]
00C75A26  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00C75A2B  C7 44 24 20 00 08 00 00         mov dword ptr [rsp + 0x20], 0x800
00C75A33  E8 58 59 7B FF                  call 0x14042b390
00C75A38  8B D8                           mov ebx, eax
00C75A3A  85 C0                           test eax, eax
00C75A3C  0F 88 01 FE FF FF               js 0x140c75843
00C75A42  0F B7 8D 90 00 00 00            movzx ecx, word ptr [rbp + 0x90]
00C75A49  41 B9 02 00 00 00               mov r9d, 2
00C75A4F  41 0F B7 16                     movzx edx, word ptr [r14]
00C75A53  4D 8B C6                        mov r8, r14
00C75A56  66 85 D2                        test dx, dx
00C75A59  74 2E                           je 0x140c75a89
00C75A5B  8D 42 DF                        lea eax, [rdx - 0x21]
00C75A5E  66 83 F8 5E                     cmp ax, 0x5e
00C75A62  77 0C                           ja 0x140c75a70
00C75A64  66 83 FA 2C                     cmp dx, 0x2c
00C75A68  74 06                           je 0x140c75a70
00C75A6A  66 83 FA 5C                     cmp dx, 0x5c
00C75A6E  75 06                           jne 0x140c75a76
00C75A70  66 41 C7 00 5F 00               mov word ptr [r8], 0x5f
00C75A76  4D 03 C1                        add r8, r9
00C75A79  41 0F B7 10                     movzx edx, word ptr [r8]
00C75A7D  66 85 D2                        test dx, dx
00C75A80  75 D9                           jne 0x140c75a5b
00C75A82  0F B7 8D 90 00 00 00            movzx ecx, word ptr [rbp + 0x90]
00C75A89  0F B7 45 70                     movzx eax, word ptr [rbp + 0x70]
00C75A8D  41 B8 50 70 69 6E               mov r8d, 0x6e697050
00C75A93  0F B7 D1                        movzx edx, cx
00C75A96  83 C0 04                        add eax, 4
00C75A99  03 D0                           add edx, eax
00C75A9B  B9 00 01 00 00                  mov ecx, 0x100
00C75AA0  E8 4B C6 F0 FF                  call 0x140b820f0
00C75AA5  48 8B F0                        mov rsi, rax
00C75AA8  48 85 C0                        test rax, rax
00C75AAB  75 0A                           jne 0x140c75ab7
00C75AAD  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00C75AB2  E9 3D 01 00 00                  jmp 0x140c75bf4
00C75AB7  B9 02 00 00 00                  mov ecx, 2
00C75ABC  48 8B FE                        mov rdi, rsi
00C75ABF  66 39 4D 70                     cmp word ptr [rbp + 0x70], cx
00C75AC3  72 1F                           jb 0x140c75ae4
00C75AC5  44 0F B7 45 70                  movzx r8d, word ptr [rbp + 0x70]
00C75ACA  48 8B CE                        mov rcx, rsi
00C75ACD  48 8B 55 78                     mov rdx, qword ptr [rbp + 0x78]
00C75AD1  E8 6A 0D A5 FF                  call 0x1406c6840
00C75AD6  0F B7 45 70                     movzx eax, word ptr [rbp + 0x70]
00C75ADA  48 D1 E8                        shr rax, 1
00C75ADD  48 8D 04 46                     lea rax, [rsi + rax*2]
00C75AE1  48 8B F8                        mov rdi, rax
00C75AE4  0F B7 8D 90 00 00 00            movzx ecx, word ptr [rbp + 0x90]
00C75AEB  BA 02 00 00 00                  mov edx, 2
00C75AF0  66 3B CA                        cmp cx, dx
00C75AF3  72 38                           jb 0x140c75b2d
00C75AF5  48 3B FE                        cmp rdi, rsi
00C75AF8  74 0F                           je 0x140c75b09
00C75AFA  66 C7 00 20 00                  mov word ptr [rax], 0x20
00C75AFF  48 03 FA                        add rdi, rdx
00C75B02  0F B7 8D 90 00 00 00            movzx ecx, word ptr [rbp + 0x90]
00C75B09  48 8B 95 98 00 00 00            mov rdx, qword ptr [rbp + 0x98]
00C75B10  44 0F B7 C1                     movzx r8d, cx
00C75B14  48 8B CF                        mov rcx, rdi
00C75B17  E8 24 0D A5 FF                  call 0x1406c6840
00C75B1C  0F B7 85 90 00 00 00            movzx eax, word ptr [rbp + 0x90]
00C75B23  48 D1 E8                        shr rax, 1
00C75B26  48 8D 04 47                     lea rax, [rdi + rax*2]
00C75B2A  48 8B F8                        mov rdi, rax
00C75B2D  4C 8B 4D D0                     mov r9, qword ptr [rbp - 0x30]
00C75B31  33 C9                           xor ecx, ecx
00C75B33  66 89 08                        mov word ptr [rax], cx
00C75B36  48 2B FE                        sub rdi, rsi
00C75B39  8B 05 69 E5 39 FF               mov eax, dword ptr [rip - 0xc61a97]
00C75B3F  4D 8B C6                        mov r8, r14
00C75B42  0F 10 05 4F E5 39 FF            movups xmm0, xmmword ptr [rip - 0xc61ab1]
00C75B49  48 8B 15 E8 68 31 00            mov rdx, qword ptr [rip + 0x3168e8]
00C75B50  C7 44 24 60 01 00 00 00         mov dword ptr [rsp + 0x60], 1
00C75B58  89 45 10                        mov dword ptr [rbp + 0x10], eax
00C75B5B  89 4D 14                        mov dword ptr [rbp + 0x14], ecx
00C75B5E  48 89 4D 18                     mov qword ptr [rbp + 0x18], rcx
00C75B62  0F 11 45 00                     movups xmmword ptr [rbp], xmm0
00C75B66  C7 45 20 12 00 00 00            mov dword ptr [rbp + 0x20], 0x12
00C75B6D  48 89 75 28                     mov qword ptr [rbp + 0x28], rsi
00C75B71  48 D1 FF                        sar rdi, 1
00C75B74  8D 04 7D 02 00 00 00            lea eax, [rdi*2 + 2]
00C75B7B  89 45 24                        mov dword ptr [rbp + 0x24], eax
00C75B7E  48 8D 45 00                     lea rax, [rbp]
00C75B82  48 8B 52 30                     mov rdx, qword ptr [rdx + 0x30]
00C75B86  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
00C75B8B  48 8D 05 6E 4C 00 00            lea rax, [rip + 0x4c6e]
00C75B92  89 4C 24 50                     mov dword ptr [rsp + 0x50], ecx
00C75B96  48 89 4C 24 48                  mov qword ptr [rsp + 0x48], rcx
00C75B9B  48 89 4C 24 40                  mov qword ptr [rsp + 0x40], rcx
00C75BA0  48 89 74 24 38                  mov qword ptr [rsp + 0x38], rsi
00C75BA5  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
00C75BA9  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
00C75BAE  48 8D 0D 7B 4C 00 00            lea rcx, [rip + 0x4c7b]
00C75BB5  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00C75BBA  E8 0D 57 AC FF                  call 0x14073b2cc
00C75BBF  85 C0                           test eax, eax
00C75BC1  79 31                           jns 0x140c75bf4
00C75BC3  F6 05 62 A5 27 00 10            test byte ptr [rip + 0x27a562], 0x10
00C75BCA  74 28                           je 0x140c75bf4
00C75BCC  44 8B C8                        mov r9d, eax
00C75BCF  48 8D 15 CA 16 3B FF            lea rdx, [rip - 0xc4e936]
00C75BD6  E8 A5 D7 7A FF                  call 0x140423380
00C75BDB  EB 17                           jmp 0x140c75bf4
00C75BDD  48 8B F1                        mov rsi, rcx
00C75BE0  4C 8B F1                        mov r14, rcx
00C75BE3  EB 0F                           jmp 0x140c75bf4
00C75BE5  48 8B F0                        mov rsi, rax
00C75BE8  4C 8B F0                        mov r14, rax
00C75BEB  EB 07                           jmp 0x140c75bf4
00C75BED  48 8B 75 A0                     mov rsi, qword ptr [rbp - 0x60]
00C75BF1  4C 8B F6                        mov r14, rsi
00C75BF4  33 D2                           xor edx, edx
00C75BF6  49 8B CC                        mov rcx, r12
00C75BF9  E8 72 CC F0 FF                  call 0x140b82870
00C75BFE  48 8B 45 D0                     mov rax, qword ptr [rbp - 0x30]
00C75C02  48 85 C0                        test rax, rax
00C75C05  74 0A                           je 0x140c75c11
00C75C07  33 D2                           xor edx, edx
00C75C09  48 8B C8                        mov rcx, rax
00C75C0C  E8 5F CC F0 FF                  call 0x140b82870
00C75C11  4D 85 F6                        test r14, r14
00C75C14  74 0A                           je 0x140c75c20
00C75C16  33 D2                           xor edx, edx
00C75C18  49 8B CE                        mov rcx, r14
00C75C1B  E8 50 CC F0 FF                  call 0x140b82870
00C75C20  48 85 F6                        test rsi, rsi
00C75C23  0F 84 D1 F9 FF FF               je 0x140c755fa
00C75C29  33 D2                           xor edx, edx
00C75C2B  48 8B CE                        mov rcx, rsi
00C75C2E  E8 3D CC F0 FF                  call 0x140b82870
00C75C33  E9 C2 F9 FF FF                  jmp 0x140c755fa
00C75C38  48 8B 8D 38 02 00 00            mov rcx, qword ptr [rbp + 0x238]
00C75C3F  48 33 CC                        xor rcx, rsp
00C75C42  E8 F9 69 A3 FF                  call 0x1406ac640
00C75C47  4C 8D 9C 24 40 03 00 00         lea r11, [rsp + 0x340]
00C75C4F  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
00C75C53  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
00C75C57  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
00C75C5B  49 8B E3                        mov rsp, r11
00C75C5E  41 5F                           pop r15
00C75C60  41 5E                           pop r14
00C75C62  41 5D                           pop r13
00C75C64  41 5C                           pop r12
00C75C66  5D                              pop rbp
00C75C67  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PipInitComputerIds(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int16 v_stack_m2EE;
    unsigned __int64 v_stack_m2F0;
    unsigned int v_stack_m2F8;
    unsigned int v_stack_m308;
    unsigned __int64 v_stack_m310;
    unsigned int v_stack_m318;
    unsigned int v_stack_m320;
    unsigned int v_stack_m328;
    unsigned __int64 v_stack_m330;
    unsigned int v_stack_m338;
    unsigned __int64 v_stack_m340;
    unsigned int v_stack_m348;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (832);
    result = (*(unsigned __int64 *)(v_rip + 1662943)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 616 + 568) = result;
    a1 = 0;
    *(unsigned __int64 *)(v_rsp - 616 - 64) = 0;
    *(unsigned __int64 *)(v_rsp - 616 - 72) = 0;
    *(unsigned __int64 *)(v_rsp - 616 - 40) = 0;
    result = 0;
    *(unsigned __int8 *)(v_rsp - 616 - 111) = 0;
    a2 = 0;
    *(unsigned __int8 *)(v_rsp - 616 - 112) = 0;
    *(unsigned int *)(v_rsp - 616 - 80) = 0;
    *(unsigned int *)(v_rsp - 616 - 56) = 0;
    *(unsigned __int64 *)(v_rsp - 616 - 48) = 0;
    *(unsigned __int64 *)(v_rsp - 616 - 96) = 0;
    *(unsigned __int64 *)(v_rsp - 616 - 88) = 0;
    *(unsigned __int64 *)(v_rsp - 616 - 32) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 616 + 96) = 0;
    *(unsigned __int64 *)(v_rsp - 616 - 16) = v_xmm1;
    *(unsigned __int64 *)(v_rsp - 616 + 48) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 616 + 64) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 616 + 80) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 616) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 616 + 16) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 616 + 32) = v_xmm0;
    v_stack_m2F0 = v_xmm0;
    result = memset(v_rsp - 616 + 112, a2, 160, a4);
    result = PipHardwareConfigOpenKey(v_rsp - 616 + 112, (unsigned int)(0xF003FULL), v_rsp - 616 - 64, a4);
    if (sign_flag) goto loc_00C748A8;
    result = PnpCtxRegDeleteTree(*(unsigned __int64 *)(v_rip + 2038681), *(unsigned __int64 *)(v_rsp - 616 - 64), v_rip + 24138, a4);
    v_r15 = 0;
    v_stack_m2F0 = 0x180016ULL;
    v_stack_m340 = 0;
    v_stack_m348 = 0;
    *(unsigned __int64 *)(v_rsp - 616 - 128) = v_rip + 24138;
    result = IopCreateRegistryKeyEx(v_rsp - 616 - 72, *(unsigned __int64 *)(v_rsp - 616 - 64), v_stack_m2F0, (unsigned int)(0xF003FULL));
    if (sign_flag) goto loc_00C748A8;
    result = PnpCtxRegDeleteTree(*(unsigned __int64 *)(v_rip + 2038602), *(unsigned __int64 *)(v_rsp - 616 - 64), v_rip + 24091, (unsigned int)(0xF003FULL));
    v_stack_m340 = 0;
    v_stack_m2F0 = 0x160014ULL;
    *(unsigned __int64 *)(v_rsp - 616 - 128) = v_rip + 24091;
    v_stack_m348 = 0;
    result = IopCreateRegistryKeyEx(v_rsp - 616 - 40, *(unsigned __int64 *)(v_rsp - 616 - 64), v_stack_m2F0, (unsigned int)(0xF003FULL));
    if (sign_flag) goto loc_00C748A8;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 240) + 56) != 0) goto loc_00C74907;
loc_00C748A3:
loc_00C748A8:
loc_00C748AE:
loc_00C748B8:
    result = RtlFreeAnsiString(v_rsp - 616 + 112, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 240) + 56), v_stack_m2F0, (unsigned int)(0xF003FULL));
    v_rdi = (v_rsp - 616 + 112) + (16);
    v_r13 = (10) - (1);
    if (condition_is_not_equal) goto loc_00C748B8;
    if (0 != 0) {
        a2 = 0;
        a3 = v_r13 + 1;
        a1 = 0;
        result = MiUnmapContiguousMemory(a1, a2, a3, (unsigned int)(0xF003FULL));
    }
    if (*(unsigned __int64 *)(v_rsp - 616 - 72) != 0) {
        a1 = *(unsigned __int64 *)(v_rsp - 616 - 72);
        result = ZwClose(a1, a2, a3, (unsigned int)(0xF003FULL));
    }
    result = *(unsigned __int64 *)(v_rsp - 616 - 64);
    if (*(unsigned __int64 *)(v_rsp - 616 - 64) != 0) {
        a2 = *(unsigned __int64 *)(v_rsp - 616 - 64);
        result = PnpCtxRegCloseKey(a1, a2, a3, (unsigned int)(0xF003FULL));
    }
    goto loc_00C75C38;
loc_00C74907:
    if (*(unsigned __int64 *)(a2 + 16) == 0) goto loc_00C748A3;
    v_stack_m2F8 = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 12)));
    result = MmMapIoSpaceEx(*(unsigned __int64 *)(a2 + 16), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 12)))), 2, (unsigned int)(0xF003FULL));
    *(unsigned __int64 *)(v_rsp - 616 - 120) = result;
    if (result != 0) goto loc_00C74943;
loc_00C7493B:
    goto loc_00C748A8;
loc_00C74943:
    a2 = 0;
    result = PipSmBiosFindStruct(a2 + 1, a2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 12)))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 12)))));
    if (result == 0) goto loc_00C74AAD;
    a1 = (*(unsigned __int8 *)(result + 1)) + (result);
    if ((result + 5) > a1) goto loc_00C7499F;
    v_stack_m348 = v_rsp - 616 + 112;
    result = PipSmBiosGetString(result, *(unsigned __int8 *)(result + 4), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 12)))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 12)))));
    if (((unsigned int)(result)) != 0xC0000225ULL) goto loc_00C74997;
    goto loc_00C7499F;
loc_00C74997:
    if (sign_flag) goto loc_00C74A20;
loc_00C7499F:
    a1 = (*(unsigned __int8 *)(result + 1)) + (result);
    if ((result + 27) > a1) goto loc_00C749DE;
    v_stack_m348 = v_rsp - 616 + 128;
    result = PipSmBiosGetString(result, *(unsigned __int8 *)(result + 26), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 12)))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 12)))));
    if (((unsigned int)(result)) != 0xC0000225ULL) goto loc_00C749DA;
    goto loc_00C749DE;
loc_00C749DA:
    if (sign_flag) goto loc_00C74A20;
loc_00C749DE:
    result = (*(unsigned __int8 *)(result + 1)) + (result);
    if ((result + 6) > result) goto loc_00C74A28;
    v_stack_m348 = v_rsp - 616 + 144;
    result = PipSmBiosGetString(result, *(unsigned __int8 *)(result + 5), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 12)))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 12)))));
    v_r15 = 0;
    if (((unsigned int)(result)) != 0xC0000225ULL) goto loc_00C74A1C;
    goto loc_00C74A2B;
loc_00C74A1C:
    if (!sign_flag) goto loc_00C74A2B;
loc_00C74A20:
    goto loc_00C7493B;
loc_00C74A28:
    v_r15 = 0;
loc_00C74A2B:
    a1 = (*(unsigned __int8 *)(result + 1)) + (result);
    if ((result + 26) > a1) goto loc_00C74A6A;
    v_stack_m348 = v_rsp - 616 + 160;
    result = PipSmBiosGetString(result, *(unsigned __int8 *)(result + 25), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 12)))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 12)))));
    if (((unsigned int)(result)) != 0xC0000225ULL) goto loc_00C74A66;
    goto loc_00C74A6A;
loc_00C74A66:
    if (sign_flag) goto loc_00C74A20;
loc_00C74A6A:
    a1 = (*(unsigned __int8 *)(result + 1)) + (result);
    if ((result + 7) > a1) goto loc_00C74AAD;
    v_stack_m348 = v_rsp - 616 + 256;
    result = PipSmBiosGetString(result, *(unsigned __int8 *)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 12))))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 12)))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 12)))));
    if (((unsigned int)(result)) != 0xC0000225ULL) goto loc_00C74AA5;
    goto loc_00C74AAD;
loc_00C74AA5:
    if (sign_flag) goto loc_00C74A20;
loc_00C74AAD:
    result = PipSmBiosFindStruct(2, 10, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 12)))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 12)))));
    if (result == 0) goto loc_00C74B51;
    a1 = (*(unsigned __int8 *)(result + 1)) + (result);
    if ((result + 5) > a1) goto loc_00C74B0E;
    v_stack_m348 = v_rsp - 616 + 208;
    result = PipSmBiosGetString(result, *(unsigned __int8 *)(result + 4), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 12)))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 12)))));
    if (((unsigned int)(result)) != 0xC0000225ULL) goto loc_00C74B06;
    goto loc_00C74B0E;
loc_00C74B06:
    if (sign_flag) goto loc_00C74A20;
loc_00C74B0E:
    a1 = (*(unsigned __int8 *)(result + 1)) + (result);
    if ((result + 6) > a1) goto loc_00C74B51;
    v_stack_m348 = v_rsp - 616 + 224;
    result = PipSmBiosGetString(result, *(unsigned __int8 *)(result + 5), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 12)))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 12)))));
    if (((unsigned int)(result)) != 0xC0000225ULL) goto loc_00C74B49;
    goto loc_00C74B51;
loc_00C74B49:
    if (sign_flag) goto loc_00C74A20;
loc_00C74B51:
    a2 = 0;
    a1 = 0;
    result = PipSmBiosFindStruct(a1, a2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 12)))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 12)))));
    if (result == 0) goto loc_00C74C59;
    a1 = (*(unsigned __int8 *)(result + 1)) + (result);
    if ((result + 5) > a1) goto loc_00C74BAF;
    v_stack_m348 = v_rsp - 616 + 176;
    result = PipSmBiosGetString(result, *(unsigned __int8 *)(result + 4), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 12)))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 12)))));
    if (((unsigned int)(result)) != 0xC0000225ULL) goto loc_00C74BA7;
    goto loc_00C74BAF;
loc_00C74BA7:
    if (sign_flag) goto loc_00C74A20;
loc_00C74BAF:
    a1 = (*(unsigned __int8 *)(result + 1)) + (result);
    if ((result + 6) > a1) goto loc_00C74BF2;
    v_stack_m348 = v_rsp - 616 + 192;
    result = PipSmBiosGetString(result, *(unsigned __int8 *)(result + 5), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 12)))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 12)))));
    if (((unsigned int)(result)) != 0xC0000225ULL) goto loc_00C74BEA;
    goto loc_00C74BF2;
loc_00C74BEA:
    if (sign_flag) goto loc_00C74A20;
loc_00C74BF2:
    a1 = (*(unsigned __int8 *)(result + 1)) + (result);
    if ((result + 9) > a1) goto loc_00C74C35;
    v_stack_m348 = v_rsp - 616 + 240;
    result = PipSmBiosGetString(result, *(unsigned __int8 *)(result + 8), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 12)))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 12)))));
    if (((unsigned int)(result)) != 0xC0000225ULL) goto loc_00C74C2D;
    goto loc_00C74C35;
loc_00C74C2D:
    if (sign_flag) goto loc_00C74A20;
loc_00C74C35:
    a2 = (*(unsigned __int8 *)(result + 1)) + (result);
    if ((result + 21) <= a2) {
        result = *(unsigned __int8 *)(result + 20);
        *(unsigned __int8 *)(v_rsp - 616 - 111) = (unsigned __int8)(result);
    }
    result = result + 22;
    if ((result + 22) <= a2) {
        result = *(unsigned __int8 *)(result + 21);
        *(unsigned __int8 *)(v_rsp - 616 - 112) = (unsigned __int8)(result);
    }
    a2 = 0;
    result = PipSmBiosFindStruct(a2 + 3, a2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 12)))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 12)))));
    v_r12 = 0;
    if (result == 0) goto loc_00C74C8D;
    a2 = (*(unsigned __int8 *)(result + 1)) + (result);
    if ((result + 6) > a2) goto loc_00C74C8D;
    result = (unsigned int)((*(unsigned __int8 *)(result + 5)) & (127));
    *(unsigned int *)(v_rsp - 616 - 80) = (unsigned int)(result);
    goto loc_00C74C90;
loc_00C74C8D:
loc_00C74C90:
    result = (unsigned int)(*(unsigned int *)(v_rsp - 616 - 80));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 616 - 80))) != 0) {
        v_stack_m340 = 4;
        result = v_rip + 23020;
        *(unsigned __int64 *)(v_rsp - 616 - 128) = result;
        a2 = v_stack_m2F0;
        result = v_rsp - 616 - 80;
        v_stack_m2F0 = 0x1C001AULL;
        a4 = 4;
        v_stack_m348 = result;
        a1 = *(unsigned __int64 *)(v_rsp - 616 - 64);
        a3 = 0;
        result = ZwSetValueKey(a1, a2, a3, a4);
    }
loc_00C74CDD:
    if ((*(unsigned __int64 *)(v_rsp - 616 + 112 + 8)) == 0) goto loc_00C74D01;
    result = 1;
    if ((*(unsigned __int16 *)(v_rsp - 616 + 112)) == 0) {
        result = 0;
        a1 = v_rsp - 616 + 112;
        result = (result) << (4);
        a1 = (a1) + (result);
        result = RtlFreeAnsiString(a1, a2, a3, a4);
        result = 1;
    }
    v_r14 = (unsigned int)((0) + ((unsigned int)(result)));
    v_rdi = (v_rsp - 616 + 112) + (16);
    if (((unsigned int)(v_r14)) < ((unsigned int)(1 + 9))) goto loc_00C74CDD;
loc_00C74D20:
    result = RtlInitUnicodeString(v_stack_m2F0, *(unsigned __int64 *)(v_rip - 13020667), a3, a4);
    if ((*(unsigned __int16 *)(v_rsp - 616 + 112)) != 0) goto loc_00C74D43;
    result = ZwDeleteValueKey(*(unsigned __int64 *)(v_rsp - 616 - 64), v_stack_m2F0, a3, a4);
    goto loc_00C74DAE;
loc_00C74D43:
    result = (0) << (4);
    v_r13 = (v_rsp - 616 + 112) + (result);
    a2 = 0;
    result = PnpUnicodeStringToWstr(v_rsp - 616 - 88, a2, v_r13, a4);
    if (sign_flag) goto loc_00C74DA8;
    result = (result) | (-1);
    a1 = 0;
loc_00C74D6C:
    result = (result) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 616 - 88) + result * 2)) != 0) goto loc_00C74D6C;
    v_stack_m340 = (unsigned int)(result * 2 + 2);
    v_stack_m348 = *(unsigned __int64 *)(v_rsp - 616 - 88);
    a3 = 0;
    result = ZwSetValueKey(*(unsigned __int64 *)(v_rsp - 616 - 64), v_stack_m2F0, a3, 1);
    result = PnpUnicodeStringToWstrFree(*(unsigned __int64 *)(v_rsp - 616 - 88), v_r13, a3, 1);
    v_r12 = 0;
loc_00C74DA8:
loc_00C74DAE:
    v_rdi = (unsigned int)((0) + (1));
    v_r15 = (v_rip - 13020667) + (8);
    v_r14 = (v_rsp - 616 + 112) + (16);
    if (((unsigned int)(v_rdi)) < 10) goto loc_00C74D20;
    if (*(unsigned __int64 *)(v_rsp - 616 + 120) == 0) goto loc_00C755D3;
    if ((*(unsigned __int64 *)(v_rsp - 616 + 152)) == 0) goto loc_00C74FCB;
    if ((*(unsigned __int64 *)(v_rsp - 616 + 184)) == 0) goto loc_00C74FCB;
    if ((*(unsigned __int64 *)(v_rsp - 616 + 200)) == 0) goto loc_00C74FD1;
    v_stack_m348 = (unsigned int)(*(unsigned __int8 *)(v_rsp - 616 - 112));
    result = RtlStringCchPrintfW(v_rsp - 616 + 552, (unsigned int)((unsigned int)(6 + 2)), v_rip + 22779, *(unsigned __int8 *)(v_rsp - 616 - 111));
    if (sign_flag) goto loc_00C755FA;
    result = RtlInitUnicodeString(v_rsp - 616 - 32, v_rsp - 616 + 552, v_rip + 22779, *(unsigned __int8 *)(v_rsp - 616 - 111));
    if ((*(unsigned __int64 *)(v_rsp - 616 + 168)) == 0) goto loc_00C74EC5;
    *(unsigned __int64 *)(v_rsp - 616 + 48) = v_rsp - 616 + 112;
    *(unsigned __int64 *)(v_rsp - 616 + 56) = v_rsp - 616 + 128;
loc_00C74E72:
    *(unsigned __int64 *)(v_rsp - 616 + 64) = v_rsp - 616 + 144;
    a1 = (v_rsp - 616 + 144) + (16);
    result = (v_rsp - 616 + 64) + (6 + 2);
    a2 = (6 + 2 - 4) - (1);
    if (condition_is_not_equal) goto loc_00C74E72;
    *(unsigned __int16 *)(v_rsp - 616 + 512) = 0;
    *(unsigned __int64 *)(v_rsp - 616 + 96) = v_rsp - 616 - 32;
    v_stack_m348 = v_rsp - 616 + 272;
    result = PipCreateComputerId(*(unsigned __int64 *)(v_rsp - 616 - 72), *(unsigned __int64 *)(v_rsp - 616 - 40), v_rsp - 616 + 48, a2 + 7);
    if (!sign_flag) goto loc_00C74ECB;
    goto loc_00C755FA;
loc_00C74EC5:
loc_00C74ECB:
    *(unsigned __int64 *)(v_rsp - 616 + 48) = v_rsp - 616 + 112;
    *(unsigned __int64 *)(v_rsp - 616 + 56) = v_rsp - 616 + 128;
    *(unsigned __int64 *)(v_rsp - 616 + 64) = v_rsp - 616 + 144;
    *(unsigned __int64 *)(v_rsp - 616 + 72) = v_rsp - 616 + 176;
    *(unsigned __int64 *)(v_rsp - 616 + 80) = v_rsp - 616 + 192;
    *(unsigned __int64 *)(v_rsp - 616 + 88) = v_rsp - 616 - 32;
    *(unsigned __int16 *)(v_rsp - 616 + 1 * 2 + 512) = 1;
    result = (1) << (4);
    result = (result) + (v_rsp - 616 + 272);
    v_stack_m348 = result;
    result = PipCreateComputerId(*(unsigned __int64 *)(v_rsp - 616 - 72), *(unsigned __int64 *)(v_rsp - 616 - 40), v_rsp - 616 + 48, 6);
    v_rsi = (unsigned int)((1) + 1);
    if (sign_flag) goto loc_00C755FA;
    *(unsigned __int64 *)(v_rsp - 616 + 48) = v_rsp - 616 + 112;
    *(unsigned __int16 *)(v_rsp - 616 + v_rsi * 2 + 512) = 2;
    *(unsigned __int64 *)(v_rsp - 616 + 56) = v_rsp - 616 + 144;
    *(unsigned __int64 *)(v_rsp - 616 + 64) = v_rsp - 616 + 176;
    *(unsigned __int64 *)(v_rsp - 616 + 72) = v_rsp - 616 + 192;
    *(unsigned __int64 *)(v_rsp - 616 + 80) = v_rsp - 616 - 32;
    result = ((unsigned int)((unsigned int)(v_rsi))) << (4);
    result = (result) + (v_rsp - 616 + 272);
    v_stack_m348 = result;
    result = PipCreateComputerId(*(unsigned __int64 *)(v_rsp - 616 - 72), *(unsigned __int64 *)(v_rsp - 616 - 40), v_rsp - 616 + 48, 5);
    v_rsi = (unsigned int)((v_rsi) + (1));
    if (sign_flag) goto loc_00C755FA;
    goto loc_00C74FD7;
loc_00C74FCB:
loc_00C74FD1:
loc_00C74FD7:
    if (*(unsigned __int64 *)(v_rsp - 616 + 120) == 0) goto loc_00C755D3;
    if ((*(unsigned __int64 *)(v_rsp - 616 + 152)) == 0) goto loc_00C75188;
    if ((*(unsigned __int64 *)(v_rsp - 616 + 168)) == 0) goto loc_00C7511C;
    if ((*(unsigned __int64 *)(v_rsp - 616 + 216)) == 0) goto loc_00C750AC;
    if ((*(unsigned __int64 *)(v_rsp - 616 + 232)) == 0) goto loc_00C750AC;
    *(unsigned __int64 *)(v_rsp - 616 + 48) = v_rsp - 616 + 112;
    *(unsigned __int64 *)(v_rsp - 616 + 56) = v_rsp - 616 + 128;
loc_00C7503B:
    *(unsigned __int64 *)(v_rsp - 616 + 64) = v_rsp - 616 + 144;
    a1 = (v_rsp - 616 + 144) + (16);
    result = (v_rsp - 616 + 64) + (8);
    a2 = (2) - (1);
    if (condition_is_not_equal) goto loc_00C7503B;
loc_00C75058:
    *(unsigned __int64 *)(v_rsp - 616 + 80) = v_rsp - 616 + 208;
    a1 = (v_rsp - 616 + 208) + (16);
    result = (v_rsp - 616 + 80) + (8);
    a2 = (2) - (1);
    if (condition_is_not_equal) goto loc_00C75058;
    *(unsigned __int16 *)(v_rsp - 616 + (unsigned int)((unsigned int)(v_rsi)) * 2 + 512) = (unsigned __int16)(a2 + 3);
    result = ((unsigned int)((unsigned int)(v_rsi))) << (4);
    result = (result) + (v_rsp - 616 + 272);
    v_stack_m348 = result;
    result = PipCreateComputerId(*(unsigned __int64 *)(v_rsp - 616 - 72), *(unsigned __int64 *)(v_rsp - 616 - 40), v_rsp - 616 + 48, (unsigned int)((unsigned int)(1 + 5)));
    v_rsi = (unsigned int)((v_rsi) + (1));
    if (sign_flag) goto loc_00C755FA;
loc_00C750AC:
    *(unsigned __int64 *)(v_rsp - 616 + 48) = v_rsp - 616 + 112;
    *(unsigned __int64 *)(v_rsp - 616 + 56) = v_rsp - 616 + 128;
loc_00C750CF:
    *(unsigned __int64 *)(v_rsp - 616 + 64) = v_rsp - 616 + 144;
    a1 = (v_rsp - 616 + 144) + (16);
    result = (v_rsp - 616 + 64) + (8);
    a2 = (2) - (1);
    if (condition_is_not_equal) goto loc_00C750CF;
    *(unsigned __int16 *)(v_rsp - 616 + (unsigned int)((unsigned int)(v_rsi)) * 2 + 512) = (unsigned __int16)(a2 + 4);
    result = ((unsigned int)((unsigned int)(v_rsi))) << (4);
    result = (result) + (v_rsp - 616 + 272);
    v_stack_m348 = result;
    result = PipCreateComputerId(*(unsigned __int64 *)(v_rsp - 616 - 72), *(unsigned __int64 *)(v_rsp - 616 - 40), v_rsp - 616 + 48, (unsigned int)((unsigned int)(a2 + 4)));
    v_rsi = (unsigned int)((v_rsi) + 1);
    if (sign_flag) goto loc_00C755FA;
loc_00C7511C:
    *(unsigned __int64 *)(v_rsp - 616 + 48) = v_rsp - 616 + 112;
    *(unsigned __int64 *)(v_rsp - 616 + 56) = v_rsp - 616 + 128;
    *(unsigned __int64 *)(v_rsp - 616 + 64) = v_rsp - 616 + 144;
    *(unsigned __int16 *)(v_rsp - 616 + (unsigned int)((unsigned int)(v_rsi)) * 2 + 512) = 5;
    result = ((unsigned int)((unsigned int)(v_rsi))) << (4);
    result = (result) + (v_rsp - 616 + 272);
    v_stack_m348 = result;
    result = PipCreateComputerId(*(unsigned __int64 *)(v_rsp - 616 - 72), *(unsigned __int64 *)(v_rsp - 616 - 40), v_rsp - 616 + 48, 3);
    v_rsi = (unsigned int)((v_rsi) + (1));
    if (sign_flag) goto loc_00C755FA;
loc_00C75188:
    if (*(unsigned __int64 *)(v_rsp - 616 + 120) == 0) goto loc_00C755D3;
    if ((*(unsigned __int64 *)(v_rsp - 616 + 168)) == 0) goto loc_00C75282;
    if ((*(unsigned __int64 *)(v_rsp - 616 + 216)) == 0) goto loc_00C75221;
    if ((*(unsigned __int64 *)(v_rsp - 616 + 232)) == 0) goto loc_00C75221;
    *(unsigned __int64 *)(v_rsp - 616 + 48) = v_rsp - 616 + 112;
    *(unsigned __int64 *)(v_rsp - 616 + 56) = v_rsp - 616 + 160;
loc_00C751D3:
    *(unsigned __int64 *)(v_rsp - 616 + 64) = v_rsp - 616 + 208;
    a1 = (v_rsp - 616 + 208) + (16);
    result = (v_rsp - 616 + 64) + (8);
    a2 = (2) - (1);
    if (condition_is_not_equal) goto loc_00C751D3;
    *(unsigned __int16 *)(v_rsp - 616 + (unsigned int)((unsigned int)(v_rsi)) * 2 + 512) = (unsigned __int16)(a2 + 6);
    result = ((unsigned int)((unsigned int)(v_rsi))) << (4);
    result = (result) + (v_rsp - 616 + 272);
    v_stack_m348 = result;
    result = PipCreateComputerId(*(unsigned __int64 *)(v_rsp - 616 - 72), *(unsigned __int64 *)(v_rsp - 616 - 40), v_rsp - 616 + 48, a2 + 4);
    v_rsi = (unsigned int)((v_rsi) + 1);
    if (sign_flag) goto loc_00C755FA;
loc_00C75221:
    *(unsigned __int64 *)(v_rsp - 616 + 48) = v_rsp - 616 + 112;
    *(unsigned __int64 *)(v_rsp - 616 + 56) = v_rsp - 616 + 160;
    *(unsigned __int16 *)(v_rsp - 616 + (unsigned int)((unsigned int)(v_rsi)) * 2 + 512) = 7;
    result = ((unsigned int)((unsigned int)(v_rsi))) << (4);
    result = (result) + (v_rsp - 616 + 272);
    v_stack_m348 = result;
    result = PipCreateComputerId(*(unsigned __int64 *)(v_rsp - 616 - 72), *(unsigned __int64 *)(v_rsp - 616 - 40), v_rsp - 616 + 48, 2);
    v_rsi = (unsigned int)((v_rsi) + (1));
    if (sign_flag) goto loc_00C755FA;
loc_00C75282:
    if (*(unsigned __int64 *)(v_rsp - 616 + 120) == 0) goto loc_00C755D3;
    if ((*(unsigned __int64 *)(v_rsp - 616 + 152)) == 0) goto loc_00C75373;
    if ((*(unsigned __int64 *)(v_rsp - 616 + 216)) == 0) goto loc_00C75312;
    if ((*(unsigned __int64 *)(v_rsp - 616 + 232)) == 0) goto loc_00C75312;
    *(unsigned __int64 *)(v_rsp - 616 + 48) = v_rsp - 616 + 112;
    *(unsigned __int64 *)(v_rsp - 616 + 56) = v_rsp - 616 + 144;
    *(unsigned __int64 *)(v_rsp - 616 + 64) = v_rsp - 616 + 208;
    *(unsigned __int64 *)(v_rsp - 616 + 72) = v_rsp - 616 + 224;
    *(unsigned __int16 *)(v_rsp - 616 + (unsigned int)((unsigned int)(v_rsi)) * 2 + 512) = 8;
    result = ((unsigned int)((unsigned int)(v_rsi))) << (4);
    result = (result) + (v_rsp - 616 + 272);
    v_stack_m348 = result;
    result = PipCreateComputerId(*(unsigned __int64 *)(v_rsp - 616 - 72), *(unsigned __int64 *)(v_rsp - 616 - 40), v_rsp - 616 + 48, 4);
    v_rsi = (unsigned int)((v_rsi) + 1);
    if (sign_flag) goto loc_00C755FA;
loc_00C75312:
    *(unsigned __int64 *)(v_rsp - 616 + 48) = v_rsp - 616 + 112;
    *(unsigned __int64 *)(v_rsp - 616 + 56) = v_rsp - 616 + 144;
    *(unsigned __int16 *)(v_rsp - 616 + (unsigned int)((unsigned int)(v_rsi)) * 2 + 512) = 9;
    result = ((unsigned int)((unsigned int)(v_rsi))) << (4);
    result = (result) + (v_rsp - 616 + 272);
    v_stack_m348 = result;
    result = PipCreateComputerId(*(unsigned __int64 *)(v_rsp - 616 - 72), *(unsigned __int64 *)(v_rsp - 616 - 40), v_rsp - 616 + 48, 2);
    v_rsi = (unsigned int)((v_rsi) + (1));
    if (sign_flag) goto loc_00C755FA;
loc_00C75373:
    if (*(unsigned __int64 *)(v_rsp - 616 + 120) == 0) goto loc_00C755D3;
    if ((*(unsigned __int64 *)(v_rsp - 616 + 136)) == 0) goto loc_00C75464;
    if ((*(unsigned __int64 *)(v_rsp - 616 + 232)) == 0) goto loc_00C7540A;
    if ((*(unsigned __int64 *)(v_rsp - 616 + 216)) == 0) goto loc_00C7540A;
    *(unsigned __int64 *)(v_rsp - 616 + 48) = v_rsp - 616 + 112;
    *(unsigned __int64 *)(v_rsp - 616 + 56) = v_rsp - 616 + 128;
loc_00C753BE:
    *(unsigned __int64 *)(v_rsp - 616 + 64) = v_rsp - 616 + 208;
    a1 = (v_rsp - 616 + 208) + (16);
    result = (v_rsp - 616 + 64) + (8);
    a2 = (2) - (1);
    if (condition_is_not_equal) goto loc_00C753BE;
    *(unsigned __int16 *)(v_rsp - 616 + (unsigned int)((unsigned int)(v_rsi)) * 2 + 512) = 10;
    result = ((unsigned int)((unsigned int)(v_rsi))) << (4);
    result = (result) + (v_rsp - 616 + 272);
    v_stack_m348 = result;
    result = PipCreateComputerId(*(unsigned __int64 *)(v_rsp - 616 - 72), *(unsigned __int64 *)(v_rsp - 616 - 40), v_rsp - 616 + 48, a2 + 4);
    v_rsi = (unsigned int)((v_rsi) + 1);
    if (sign_flag) goto loc_00C755FA;
loc_00C7540A:
    *(unsigned __int64 *)(v_rsp - 616 + 48) = v_rsp - 616 + 112;
    *(unsigned __int64 *)(v_rsp - 616 + 56) = v_rsp - 616 + 128;
    *(unsigned __int16 *)(v_rsp - 616 + (unsigned int)((unsigned int)(v_rsi)) * 2 + 512) = 11;
    result = ((unsigned int)((unsigned int)(v_rsi))) << (4);
    result = (result) + (v_rsp - 616 + 272);
    v_stack_m348 = result;
    result = PipCreateComputerId(*(unsigned __int64 *)(v_rsp - 616 - 72), *(unsigned __int64 *)(v_rsp - 616 - 40), v_rsp - 616 + 48, 2);
    v_rsi = (unsigned int)((v_rsi) + 1);
    if (sign_flag) goto loc_00C755FA;
loc_00C75464:
    if (*(unsigned __int64 *)(v_rsp - 616 + 120) == 0) goto loc_00C755D3;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 616 - 80))) == 0) goto loc_00C7550B;
    result = RtlStringCchPrintfW(v_rsp - 616 + 544, 4, v_rip + 21167, (unsigned int)(*(unsigned int *)(v_rsp - 616 - 80)));
    if (sign_flag) goto loc_00C755FA;
    result = RtlInitUnicodeString(v_rsp - 616 - 16, v_rsp - 616 + 544, v_rip + 21167, (unsigned int)(*(unsigned int *)(v_rsp - 616 - 80)));
    *(unsigned __int64 *)(v_rsp - 616 + 48) = v_rsp - 616 + 112;
    *(unsigned __int64 *)(v_rsp - 616 + 56) = v_rsp - 616 - 16;
    a2 = 0;
    *(unsigned __int16 *)(v_rsp - 616 + (unsigned int)((unsigned int)(v_rsi)) * 2 + 512) = 12;
    result = ((unsigned int)((unsigned int)(v_rsi))) << (4);
    result = (result) + (v_rsp - 616 + 272);
    v_stack_m348 = result;
    result = PipCreateComputerId(*(unsigned __int64 *)(v_rsp - 616 - 72), a2, v_rsp - 616 + 48, 2);
    v_rsi = (unsigned int)((v_rsi) + ((unsigned int)(2 - 1)));
    if (sign_flag) goto loc_00C755FA;
    goto loc_00C75514;
loc_00C7550B:
loc_00C75514:
    if (*(unsigned __int64 *)(v_rsp - 616 + 120) == 0) goto loc_00C755D3;
    if ((*(unsigned __int64 *)(v_rsp - 616 + 232)) == 0) goto loc_00C75593;
    if ((*(unsigned __int64 *)(v_rsp - 616 + 216)) == 0) goto loc_00C75593;
    *(unsigned __int64 *)(v_rsp - 616 + 48) = v_rsp - 616 + 112;
loc_00C75545:
    *(unsigned __int64 *)(v_rsp - 616 + 56) = v_rsp - 616 + 208;
    a1 = (v_rsp - 616 + 208) + (16);
    result = (v_rsp - 616 + 56) + (8);
    a2 = (2) - (2 - 1);
    if (condition_is_not_equal) goto loc_00C75545;
    *(unsigned __int16 *)(v_rsp - 616 + (unsigned int)((unsigned int)(v_rsi)) * 2 + 512) = (unsigned __int16)(a2 + 13);
    result = ((unsigned int)((unsigned int)(v_rsi))) << (4);
    result = (result) + (v_rsp - 616 + 272);
    v_stack_m348 = result;
    result = PipCreateComputerId(*(unsigned __int64 *)(v_rsp - 616 - 72), a2, v_rsp - 616 + 48, a2 + 3);
    v_rsi = (unsigned int)((v_rsi) + (1));
    if (sign_flag) goto loc_00C755FA;
loc_00C75593:
    *(unsigned __int64 *)(v_rsp - 616 + 48) = v_rsp - 616 + 112;
    a2 = 0;
    *(unsigned __int16 *)(v_rsp - 616 + (unsigned int)((unsigned int)(v_rsi)) * 2 + 512) = 14;
    result = ((unsigned int)((unsigned int)(v_rsi))) << (4);
    result = (result) + (v_rsp - 616 + 272);
    v_stack_m348 = result;
    result = PipCreateComputerId(*(unsigned __int64 *)(v_rsp - 616 - 72), a2, v_rsp - 616 + 48, 1);
    v_rsi = (unsigned int)((v_rsi) + 1);
    if (sign_flag) goto loc_00C755FA;
loc_00C755D3:
    v_rdi = (unsigned int)((2) * ((unsigned int)(v_rsi)));
    v_rdi = (unsigned int)((v_rdi) + (2));
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(v_rdi)), (unsigned int)(0x6E697050ULL), 1);
    a1 = 0;
    if (result != 0) goto loc_00C75608;
loc_00C755FA:
    goto loc_00C748AE;
loc_00C75608:
    *(unsigned __int64 *)(v_rsp - 616 - 128) = result;
    v_stack_m2EE = (unsigned __int16)(v_rdi);
    if ((unsigned int)(v_rsi) == 0) goto loc_00C756B0;
loc_00C7561C:
    v_stack_m2F0 = 0;
    a4 = 0;
    result = RtlUnicodeStringCopyStringEx(v_stack_m2F0, v_rip + 20747, v_stack_m2F0, a4);
    a1 = 0;
    if (sign_flag) goto loc_00C75BDD;
    result = (0) << (4);
    a1 = (v_rsp - 616 + 272) + (result);
    a3 = 0;
    result = RtlStringFromGUIDEx(a1, v_stack_m2F0, a3, a4);
    result = 0;
    if (sign_flag) goto loc_00C75BE5;
    a3 = 0;
    result = RtlUpcaseUnicodeString(v_stack_m2F0, v_stack_m2F0, a3, a4);
    a1 = 0;
    if (sign_flag) goto loc_00C75BDD;
    result = (*(unsigned __int64 *)(v_rsp - 616 - 128)) + (78);
    v_r14 = (unsigned int)((0) + 1);
    *(unsigned __int64 *)(v_rsp - 616 - 128) = result;
    if (((unsigned int)(v_r14)) < ((unsigned int)(v_rsi))) goto loc_00C7561C;
loc_00C756B0:
    if (sign_flag) goto loc_00C75BED;
    v_stack_m320 = 0;
    v_stack_m328 = (unsigned int)(v_rdi);
    *(unsigned __int16 *)(result) = 0;
    a4 = 0;
    v_stack_m330 = (unsigned int)(v_stack_m2F8);
    v_stack_m338 = 0x2012ULL;
    v_stack_m340 = v_rip - 12992910;
    v_stack_m348 = 0;
    result = PnpSetObjectProperty(*(unsigned __int64 *)(v_rip + 2034840), v_rip + 18493, 2 + 3, a4);
    result = 0;
    if (sign_flag) goto loc_00C75BE5;
    v_rbx = (unsigned int)((v_rsi + v_rsi * 2) << (5));
    v_rbx = (unsigned int)((v_rbx) + (2));
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(v_rbx)), (unsigned int)(0x6E697050ULL), a4);
    a3 = 0;
    *(unsigned __int64 *)(v_rsp - 616 - 48) = result;
    if (result != 0) goto loc_00C75748;
loc_00C7573D:
    goto loc_00C75BF4;
loc_00C75748:
    *(unsigned __int64 *)(v_rsp - 616 - 128) = result;
    v_stack_m2EE = (unsigned __int16)((unsigned int)(0xC000009AULL));
    if (0 == 0) goto loc_00C75818;
loc_00C75766:
    v_stack_m2F0 = 0;
    if ((*(unsigned __int8 *)(*(unsigned __int16 *)(v_rsp - 616 + 512) + v_rip - 12901505 * 1)) == 0) goto loc_00C75804;
    a4 = 0;
    result = RtlUnicodeStringCopyStringEx(v_stack_m2F0, v_rip + 20448, v_stack_m2F0, a4);
    result = 0;
    if (sign_flag) goto loc_00C75BE5;
    result = (0) << (4);
    a1 = (v_rsp - 616 + 272) + (result);
    a3 = 0;
    result = RtlStringFromGUIDEx(a1, v_stack_m2F0, a3, a4);
    result = 0;
    if (sign_flag) goto loc_00C75BE5;
    a3 = 0;
    result = RtlUpcaseUnicodeString(v_stack_m2F0, v_stack_m2F0, a3, a4);
    a3 = 0;
    if (sign_flag) goto loc_00C7573D;
    a1 = (*(unsigned __int64 *)(v_rsp - 616 - 128)) + (78);
    *(unsigned __int64 *)(v_rsp - 616 - 128) = a1;
loc_00C75804:
    v_rdi = (unsigned int)((0) + 1);
    v_r14 = (v_rsp - 616 + 512) + (2);
    if (((unsigned int)(v_rdi)) < 0) goto loc_00C75766;
loc_00C75818:
    v_rdi = 0;
    *(unsigned __int16 *)(a1) = 0;
    result = ExAllocatePool2(256, 400, (unsigned int)(0x6E697050ULL), a4);
    if (result != 0) goto loc_00C7584B;
loc_00C75843:
    goto loc_00C75BF4;
loc_00C7584B:
    *(unsigned __int64 *)(v_rsp - 616 - 88) = result;
    *(unsigned __int64 *)(v_rsp - 616 - 104) = 200;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rsp - 616 + 112))) <= ((unsigned __int16)(70 - 68))) goto loc_00C7588D;
    *(unsigned __int64 *)(v_rsp - 616 - 128) = *(unsigned __int64 *)(v_rsp - 616 + 120);
    v_stack_m2EE = (unsigned __int16)(*(unsigned __int16 *)(v_rsp - 616 + 114));
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rsp - 616 + 112))) <= 70) goto loc_00C75886;
    v_stack_m2F0 = 70;
    goto loc_00C7589E;
loc_00C75886:
    v_stack_m2F0 = (unsigned __int16)(*(unsigned __int16 *)(v_rsp - 616 + 112));
    goto loc_00C7589E;
loc_00C7588D:
    result = RtlInitUnicodeString(v_stack_m2F0, v_rip + 19996, (unsigned int)(0x6E697050ULL), a4);
loc_00C7589E:
    v_stack_m338 = v_stack_m2F0;
    v_stack_m340 = v_rip + 19978;
    v_stack_m348 = 0x800ULL;
    result = RtlStringCchPrintfExW(result, 200, v_rsp - 616 - 88, v_rsp - 616 - 104);
    if (sign_flag) goto loc_00C75843;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rsp - 616 + 128))) <= 2) goto loc_00C75955;
    *(unsigned __int64 *)(v_rsp - 616 - 128) = *(unsigned __int64 *)(v_rsp - 616 + 136);
    v_stack_m2EE = (unsigned __int16)(*(unsigned __int16 *)(v_rsp - 616 + 130));
    v_stack_m2F0 = 70;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rsp - 616 + 128))) <= 70) {
        v_stack_m2F0 = (unsigned __int16)(*(unsigned __int16 *)(v_rsp - 616 + 128));
    }
    v_stack_m338 = v_stack_m2F0;
    v_stack_m340 = v_rip + 19869;
    v_stack_m348 = 0x800ULL;
    result = RtlStringCchPrintfExW(*(unsigned __int64 *)(v_rsp - 616 - 88), *(unsigned __int64 *)(v_rsp - 616 - 104), v_rsp - 616 - 88, v_rsp - 616 - 104);
    if (sign_flag) goto loc_00C75843;
loc_00C75955:
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rsp - 616 + 144))) <= 2) goto loc_00C759D2;
    *(unsigned __int64 *)(v_rsp - 616 - 128) = *(unsigned __int64 *)(v_rsp - 616 + 152);
    v_stack_m2EE = (unsigned __int16)(*(unsigned __int16 *)(v_rsp - 616 + 146));
    v_stack_m2F0 = 70;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rsp - 616 + 144))) <= 70) {
        v_stack_m2F0 = (unsigned __int16)(*(unsigned __int16 *)(v_rsp - 616 + 144));
    }
    v_stack_m338 = v_stack_m2F0;
    v_stack_m340 = v_rip + 19783;
    v_stack_m348 = 0x800ULL;
    result = RtlStringCchPrintfExW(*(unsigned __int64 *)(v_rsp - 616 - 88), *(unsigned __int64 *)(v_rsp - 616 - 104), v_rsp - 616 - 88, v_rsp - 616 - 104);
    if (sign_flag) goto loc_00C75843;
loc_00C759D2:
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rsp - 616 + 160))) <= 2) goto loc_00C75A4F;
    *(unsigned __int64 *)(v_rsp - 616 - 128) = *(unsigned __int64 *)(v_rsp - 616 + 168);
    v_stack_m2EE = (unsigned __int16)(*(unsigned __int16 *)(v_rsp - 616 + 162));
    v_stack_m2F0 = 70;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rsp - 616 + 160))) <= 70) {
        v_stack_m2F0 = (unsigned __int16)(*(unsigned __int16 *)(v_rsp - 616 + 160));
    }
    v_stack_m338 = v_stack_m2F0;
    v_stack_m340 = v_rip + 19898;
    v_stack_m348 = 0x800ULL;
    result = RtlStringCchPrintfExW(*(unsigned __int64 *)(v_rsp - 616 - 88), *(unsigned __int64 *)(v_rsp - 616 - 104), v_rsp - 616 - 88, v_rsp - 616 - 104);
    if (sign_flag) goto loc_00C75843;
loc_00C75A4F:
    if ((unsigned __int16)(*(unsigned __int16 *)(result)) == 0) goto loc_00C75A89;
loc_00C75A5B:
    if (((unsigned __int16)(*(unsigned __int16 *)(result) - 33)) > 94) goto loc_00C75A70;
    if (((unsigned __int16)(*(unsigned __int16 *)(result))) == 44) goto loc_00C75A70;
    if (((unsigned __int16)(*(unsigned __int16 *)(result))) == 92) {
        *(unsigned __int16 *)(result) = 95;
    }
    a3 = (result) + (2);
    if ((unsigned __int16)(*(unsigned __int16 *)(a3)) != 0) goto loc_00C75A5B;
loc_00C75A89:
    result = (unsigned int)((*(unsigned __int16 *)(v_rsp - 616 + 112)) + (4));
    a2 = (unsigned int)(((unsigned __int16)(*(unsigned __int16 *)(v_rsp - 616 + 144))) + ((unsigned int)(result)));
    result = ExAllocatePool2(256, a2, (unsigned int)(0x6E697050ULL), 2);
    if (result != 0) goto loc_00C75AB7;
    goto loc_00C75BF4;
loc_00C75AB7:
    v_rdi = result;
    if ((*(unsigned __int16 *)(v_rsp - 616 + 112)) >= 2) {
        a3 = *(unsigned __int16 *)(v_rsp - 616 + 112);
        a1 = result;
        a2 = *(unsigned __int64 *)(v_rsp - 616 + 120);
        result = memcpy(a1, a2, a3, 2);
        result = *(unsigned __int16 *)(v_rsp - 616 + 112);
        result = (result) >> (1);
        result = result + result * 2;
        v_rdi = result;
    }
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rsp - 616 + 144))) < 2) goto loc_00C75B2D;
    if (v_rdi != result) {
        *(unsigned __int16 *)(result) = 32;
        v_rdi = (v_rdi) + (2);
        a1 = *(unsigned __int16 *)(v_rsp - 616 + 144);
    }
    result = memcpy(v_rdi, *(unsigned __int64 *)(v_rsp - 616 + 152), (unsigned __int16)(a1), 2);
    result = (*(unsigned __int16 *)(v_rsp - 616 + 144)) >> (1);
loc_00C75B2D:
    a1 = 0;
    *(unsigned __int16 *)(v_rdi + result * 2) = 0;
    v_rdi = (v_rdi + result * 2) - (result);
    v_stack_m308 = 1;
    *(unsigned int *)(v_rsp - 616 + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 12982935)));
    *(unsigned int *)(v_rsp - 616 + 20) = 0;
    *(unsigned __int64 *)(v_rsp - 616 + 24) = 0;
    *(unsigned __int64 *)(v_rsp - 616) = v_xmm0;
    *(unsigned int *)(v_rsp - 616 + 32) = 18;
    *(unsigned __int64 *)(v_rsp - 616 + 40) = result;
    v_rdi = (v_rdi) >> (1);
    *(unsigned int *)(v_rsp - 616 + 36) = (unsigned int)(v_rdi * 2 + 2);
    v_stack_m310 = v_rsp - 616;
    v_stack_m318 = 0;
    v_stack_m320 = 0;
    v_stack_m328 = 0;
    v_stack_m330 = result;
    v_stack_m338 = 0;
    v_stack_m340 = 0;
    v_stack_m348 = v_rip + 19566;
    result = PiSwStartCreate(v_rip + 19579, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3238120) + 48), result, *(unsigned __int64 *)(v_rsp - 616 - 48));
    if (!sign_flag) goto loc_00C75BF4;
    if (((*(unsigned __int8 *)(v_rip + 2598242)) & (16)) == 0) goto loc_00C75BF4;
    result = McTemplateK0d_EtwWriteTransfer(v_rip + 19579, v_rip - 12904758, result, (unsigned int)((unsigned int)(result)));
    goto loc_00C75BF4;
loc_00C75BDD:
    goto loc_00C75BF4;
loc_00C75BE5:
    goto loc_00C75BF4;
loc_00C75BED:
loc_00C75BF4:
    a2 = 0;
    result = ExFreePoolWithTag((unsigned int)(v_stack_m2F8), a2, result, (unsigned int)((unsigned int)(result)));
    result = *(unsigned __int64 *)(v_rsp - 616 - 48);
    if (*(unsigned __int64 *)(v_rsp - 616 - 48) != 0) {
        a2 = 0;
        a1 = *(unsigned __int64 *)(v_rsp - 616 - 48);
        result = ExFreePoolWithTag(a1, a2, result, (unsigned int)((unsigned int)(result)));
    }
    if (*(unsigned __int64 *)(v_rsp - 616 - 96) != 0) {
        a2 = 0;
        a1 = *(unsigned __int64 *)(v_rsp - 616 - 96);
        result = ExFreePoolWithTag(a1, a2, result, (unsigned int)((unsigned int)(result)));
    }
    if (*(unsigned __int64 *)(v_rsp - 616 - 96) == 0) goto loc_00C755FA;
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(v_rsp - 616 - 96), a2, result, (unsigned int)((unsigned int)(result)));
    goto loc_00C755FA;
loc_00C75C38:
    a1 = (*(unsigned __int64 *)(v_rsp - 616 + 568)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, result, (unsigned int)((unsigned int)(result)));
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PipInitComputerIds(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint16_t v_stack_m2EE;
    uint64_t v_stack_m2F0;
    uint32_t v_stack_m2F8;
    uint32_t v_stack_m308;
    uint64_t v_stack_m310;
    uint32_t v_stack_m318;
    uint32_t v_stack_m320;
    uint32_t v_stack_m328;
    uint64_t v_stack_m330;
    uint32_t v_stack_m338;
    uint64_t v_stack_m340;
    uint32_t v_stack_m348;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (832);
    result = (*(uint64_t *)(v_rip + 0x195FDF)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x268 + 0x238) = result;
    Arg1 = 0;
    *(uint64_t *)(local_rsp - 0x268 - 0x40) = 0;
    *(uint64_t *)(local_rsp - 0x268 - 0x48) = 0;
    *(uint64_t *)(local_rsp - 0x268 - 0x28) = 0;
    result = 0;
    *(uint8_t *)(local_rsp - 0x268 - 0x6F) = 0;
    Arg2 = 0;
    *(uint8_t *)(local_rsp - 0x268 - 0x70) = 0;
    *(uint32_t *)(local_rsp - 0x268 - 0x50) = 0;
    *(uint32_t *)(local_rsp - 0x268 - 0x38) = 0;
    *(uint64_t *)(local_rsp - 0x268 - 0x30) = 0;
    *(uint64_t *)(local_rsp - 0x268 - 0x60) = 0;
    *(uint64_t *)(local_rsp - 0x268 - 0x58) = 0;
    *(uint64_t *)(local_rsp - 0x268 - 0x20) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x268 + 0x60) = 0;
    *(uint64_t *)(local_rsp - 0x268 - 0x10) = v_xmm1;
    *(uint64_t *)(local_rsp - 0x268 + 0x30) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x268 + 0x40) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x268 + 0x50) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x268) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x268 + 0x10) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x268 + 0x20) = v_xmm0;
    v_stack_m2F0 = v_xmm0;
    result = memset(local_rsp - 616 + 112, Arg2, 160, a4);
    result = PipHardwareConfigOpenKey(local_rsp - 616 + 112, (uint32_t)(0xF003FULL), local_rsp - 616 - 64, a4);
    if (sign_flag) goto loc_00C748A8;
    result = PnpCtxRegDeleteTree(*(uint64_t *)(v_rip + 0x1F1B99), *(uint64_t *)(local_rsp - 0x268 - 0x40), v_rip + 24138, a4);
    local_r15 = 0;
    v_stack_m2F0 = 0x180016ULL;
    v_stack_m340 = 0;
    v_stack_m348 = 0;
    *(uint64_t *)(local_rsp - 0x268 - 0x80) = v_rip + 24138;
    result = IopCreateRegistryKeyEx(local_rsp - 616 - 72, *(uint64_t *)(local_rsp - 0x268 - 0x40), v_stack_m2F0, (uint32_t)(0xF003FULL));
    if (sign_flag) goto loc_00C748A8;
    result = PnpCtxRegDeleteTree(*(uint64_t *)(v_rip + 0x1F1B4A), *(uint64_t *)(local_rsp - 0x268 - 0x40), v_rip + 24091, (uint32_t)(0xF003FULL));
    v_stack_m340 = 0;
    v_stack_m2F0 = 0x160014ULL;
    *(uint64_t *)(local_rsp - 0x268 - 0x80) = v_rip + 24091;
    v_stack_m348 = 0;
    result = IopCreateRegistryKeyEx(local_rsp - 616 - 40, *(uint64_t *)(local_rsp - 0x268 - 0x40), v_stack_m2F0, (uint32_t)(0xF003FULL));
    if (sign_flag) goto loc_00C748A8;
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0xF0) + 0x38) != 0) goto loc_00C74907;
loc_00C748A3:
loc_00C748A8:
loc_00C748AE:
loc_00C748B8:
    result = RtlFreeAnsiString(local_rsp - 616 + 112, *(uint64_t *)(*(uint64_t *)(arg1 + 0xF0) + 0x38), v_stack_m2F0, (uint32_t)(0xF003FULL));
    local_rdi = (local_rsp - 616 + 112) + (16);
    local_r13 = (10) - (1);
    if (condition_is_not_equal) goto loc_00C748B8;
    if (0 != 0) {
        Arg2 = 0;
        a3 = local_r13 + 1;
        Arg1 = 0;
        result = MiUnmapContiguousMemory(Arg1, Arg2, a3, (uint32_t)(0xF003FULL));
    }
    if (*(uint64_t *)(local_rsp - 0x268 - 0x48) != 0) {
        Arg1 = *(uint64_t *)(local_rsp - 0x268 - 0x48);
        result = ZwClose(Arg1, Arg2, a3, (uint32_t)(0xF003FULL));
    }
    result = *(uint64_t *)(local_rsp - 0x268 - 0x40);
    if (*(uint64_t *)(local_rsp - 0x268 - 0x40) != 0) {
        Arg2 = *(uint64_t *)(local_rsp - 0x268 - 0x40);
        result = PnpCtxRegCloseKey(Arg1, Arg2, a3, (uint32_t)(0xF003FULL));
    }
    goto loc_00C75C38;
loc_00C74907:
    if (*(uint64_t *)(Arg2 + 0x10) == 0) goto loc_00C748A3;
    v_stack_m2F8 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0xC)));
    result = MmMapIoSpaceEx(*(uint64_t *)(Arg2 + 0x10), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0xC)))), 2, (uint32_t)(0xF003FULL));
    *(uint64_t *)(local_rsp - 0x268 - 0x78) = result;
    if (result != 0) goto loc_00C74943;
loc_00C7493B:
    goto loc_00C748A8;
loc_00C74943:
    Arg2 = 0;
    result = PipSmBiosFindStruct(Arg2 + 1, Arg2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0xC)))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0xC)))));
    if (result == 0) goto loc_00C74AAD;
    Arg1 = (*(uint8_t *)(result + 0x1)) + (result);
    if ((result + 5) > Arg1) goto loc_00C7499F;
    v_stack_m348 = local_rsp - 616 + 112;
    result = PipSmBiosGetString(result, *(uint8_t *)(result + 0x4), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0xC)))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0xC)))));
    if (((uint32_t)(result)) != 0xC0000225ULL) goto loc_00C74997;
    goto loc_00C7499F;
loc_00C74997:
    if (sign_flag) goto loc_00C74A20;
loc_00C7499F:
    Arg1 = (*(uint8_t *)(result + 0x1)) + (result);
    if ((result + 27) > Arg1) goto loc_00C749DE;
    v_stack_m348 = local_rsp - 616 + 128;
    result = PipSmBiosGetString(result, *(uint8_t *)(result + 0x1A), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0xC)))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0xC)))));
    if (((uint32_t)(result)) != 0xC0000225ULL) goto loc_00C749DA;
    goto loc_00C749DE;
loc_00C749DA:
    if (sign_flag) goto loc_00C74A20;
loc_00C749DE:
    result = (*(uint8_t *)(result + 0x1)) + (result);
    if ((result + 6) > result) goto loc_00C74A28;
    v_stack_m348 = local_rsp - 616 + 144;
    result = PipSmBiosGetString(result, *(uint8_t *)(result + 0x5), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0xC)))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0xC)))));
    local_r15 = 0;
    if (((uint32_t)(result)) != 0xC0000225ULL) goto loc_00C74A1C;
    goto loc_00C74A2B;
loc_00C74A1C:
    if (!sign_flag) goto loc_00C74A2B;
loc_00C74A20:
    goto loc_00C7493B;
loc_00C74A28:
    local_r15 = 0;
loc_00C74A2B:
    Arg1 = (*(uint8_t *)(result + 0x1)) + (result);
    if ((result + 26) > Arg1) goto loc_00C74A6A;
    v_stack_m348 = local_rsp - 616 + 160;
    result = PipSmBiosGetString(result, *(uint8_t *)(result + 0x19), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0xC)))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0xC)))));
    if (((uint32_t)(result)) != 0xC0000225ULL) goto loc_00C74A66;
    goto loc_00C74A6A;
loc_00C74A66:
    if (sign_flag) goto loc_00C74A20;
loc_00C74A6A:
    Arg1 = (*(uint8_t *)(result + 0x1)) + (result);
    if ((result + 7) > Arg1) goto loc_00C74AAD;
    v_stack_m348 = local_rsp - 616 + 256;
    result = PipSmBiosGetString(result, *(uint8_t *)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0xC))))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0xC)))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0xC)))));
    if (((uint32_t)(result)) != 0xC0000225ULL) goto loc_00C74AA5;
    goto loc_00C74AAD;
loc_00C74AA5:
    if (sign_flag) goto loc_00C74A20;
loc_00C74AAD:
    result = PipSmBiosFindStruct(2, 10, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0xC)))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0xC)))));
    if (result == 0) goto loc_00C74B51;
    Arg1 = (*(uint8_t *)(result + 0x1)) + (result);
    if ((result + 5) > Arg1) goto loc_00C74B0E;
    v_stack_m348 = local_rsp - 616 + 208;
    result = PipSmBiosGetString(result, *(uint8_t *)(result + 0x4), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0xC)))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0xC)))));
    if (((uint32_t)(result)) != 0xC0000225ULL) goto loc_00C74B06;
    goto loc_00C74B0E;
loc_00C74B06:
    if (sign_flag) goto loc_00C74A20;
loc_00C74B0E:
    Arg1 = (*(uint8_t *)(result + 0x1)) + (result);
    if ((result + 6) > Arg1) goto loc_00C74B51;
    v_stack_m348 = local_rsp - 616 + 224;
    result = PipSmBiosGetString(result, *(uint8_t *)(result + 0x5), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0xC)))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0xC)))));
    if (((uint32_t)(result)) != 0xC0000225ULL) goto loc_00C74B49;
    goto loc_00C74B51;
loc_00C74B49:
    if (sign_flag) goto loc_00C74A20;
loc_00C74B51:
    Arg2 = 0;
    Arg1 = 0;
    result = PipSmBiosFindStruct(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0xC)))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0xC)))));
    if (result == 0) goto loc_00C74C59;
    Arg1 = (*(uint8_t *)(result + 0x1)) + (result);
    if ((result + 5) > Arg1) goto loc_00C74BAF;
    v_stack_m348 = local_rsp - 616 + 176;
    result = PipSmBiosGetString(result, *(uint8_t *)(result + 0x4), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0xC)))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0xC)))));
    if (((uint32_t)(result)) != 0xC0000225ULL) goto loc_00C74BA7;
    goto loc_00C74BAF;
loc_00C74BA7:
    if (sign_flag) goto loc_00C74A20;
loc_00C74BAF:
    Arg1 = (*(uint8_t *)(result + 0x1)) + (result);
    if ((result + 6) > Arg1) goto loc_00C74BF2;
    v_stack_m348 = local_rsp - 616 + 192;
    result = PipSmBiosGetString(result, *(uint8_t *)(result + 0x5), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0xC)))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0xC)))));
    if (((uint32_t)(result)) != 0xC0000225ULL) goto loc_00C74BEA;
    goto loc_00C74BF2;
loc_00C74BEA:
    if (sign_flag) goto loc_00C74A20;
loc_00C74BF2:
    Arg1 = (*(uint8_t *)(result + 0x1)) + (result);
    if ((result + 9) > Arg1) goto loc_00C74C35;
    v_stack_m348 = local_rsp - 616 + 240;
    result = PipSmBiosGetString(result, *(uint8_t *)(result + 0x8), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0xC)))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0xC)))));
    if (((uint32_t)(result)) != 0xC0000225ULL) goto loc_00C74C2D;
    goto loc_00C74C35;
loc_00C74C2D:
    if (sign_flag) goto loc_00C74A20;
loc_00C74C35:
    Arg2 = (*(uint8_t *)(result + 0x1)) + (result);
    if ((result + 21) <= Arg2) {
        result = *(uint8_t *)(result + 0x14);
        *(uint8_t *)(local_rsp - 0x268 - 0x6F) = (uint8_t)(result);
    }
    result = result + 22;
    if ((result + 22) <= Arg2) {
        result = *(uint8_t *)(result + 0x15);
        *(uint8_t *)(local_rsp - 0x268 - 0x70) = (uint8_t)(result);
    }
    Arg2 = 0;
    result = PipSmBiosFindStruct(Arg2 + 3, Arg2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0xC)))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0xC)))));
    local_r12 = 0;
    if (result == 0) goto loc_00C74C8D;
    Arg2 = (*(uint8_t *)(result + 0x1)) + (result);
    if ((result + 6) > Arg2) goto loc_00C74C8D;
    result = (uint32_t)((*(uint8_t *)(result + 0x5)) & (127));
    *(uint32_t *)(local_rsp - 0x268 - 0x50) = (uint32_t)(result);
    goto loc_00C74C90;
loc_00C74C8D:
loc_00C74C90:
    result = (uint32_t)(*(uint32_t *)(local_rsp - 0x268 - 0x50));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x268 - 0x50))) != 0) {
        v_stack_m340 = 4;
        result = v_rip + 23020;
        *(uint64_t *)(local_rsp - 0x268 - 0x80) = result;
        Arg2 = v_stack_m2F0;
        result = local_rsp - 616 - 80;
        v_stack_m2F0 = 0x1C001AULL;
        a4 = 4;
        v_stack_m348 = result;
        Arg1 = *(uint64_t *)(local_rsp - 0x268 - 0x40);
        a3 = 0;
        result = ZwSetValueKey(Arg1, Arg2, a3, a4);
    }
loc_00C74CDD:
    if ((*(uint64_t *)(local_rsp - 0x268 + 0x70 + 0x8)) == 0) goto loc_00C74D01;
    result = 1;
    if ((*(uint16_t *)(local_rsp - 0x268 + 0x70)) == 0) {
        result = 0;
        Arg1 = local_rsp - 616 + 112;
        result = (result) << (4);
        Arg1 = (Arg1) + (result);
        result = RtlFreeAnsiString(Arg1, Arg2, a3, a4);
        result = 1;
    }
    local_r14 = (uint32_t)((0) + ((uint32_t)(result)));
    local_rdi = (local_rsp - 616 + 112) + (16);
    if (((uint32_t)(local_r14)) < ((uint32_t)(1 + 9))) goto loc_00C74CDD;
loc_00C74D20:
    result = RtlInitUnicodeString(v_stack_m2F0, *(uint64_t *)(v_rip - 0xC6ADFB), a3, a4);
    if ((*(uint16_t *)(local_rsp - 0x268 + 0x70)) != 0) goto loc_00C74D43;
    result = ZwDeleteValueKey(*(uint64_t *)(local_rsp - 0x268 - 0x40), v_stack_m2F0, a3, a4);
    goto loc_00C74DAE;
loc_00C74D43:
    result = (0) << (4);
    local_r13 = (local_rsp - 616 + 112) + (result);
    Arg2 = 0;
    result = PnpUnicodeStringToWstr(local_rsp - 616 - 88, Arg2, local_r13, a4);
    if (sign_flag) goto loc_00C74DA8;
    result = (result) | (-1);
    Arg1 = 0;
loc_00C74D6C:
    result = (result) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(local_rsp - 0x268 - 0x58) + result * 2)) != 0) goto loc_00C74D6C;
    v_stack_m340 = (uint32_t)(result * 2 + 2);
    v_stack_m348 = *(uint64_t *)(local_rsp - 0x268 - 0x58);
    a3 = 0;
    result = ZwSetValueKey(*(uint64_t *)(local_rsp - 0x268 - 0x40), v_stack_m2F0, a3, 1);
    result = PnpUnicodeStringToWstrFree(*(uint64_t *)(local_rsp - 0x268 - 0x58), local_r13, a3, 1);
    local_r12 = 0;
loc_00C74DA8:
loc_00C74DAE:
    local_rdi = (uint32_t)((0) + (1));
    local_r15 = (v_rip - 13020667) + (8);
    local_r14 = (local_rsp - 616 + 112) + (16);
    if (((uint32_t)(local_rdi)) < 10) goto loc_00C74D20;
    if (*(uint64_t *)(local_rsp - 0x268 + 0x78) == 0) goto loc_00C755D3;
    if ((*(uint64_t *)(local_rsp - 0x268 + 0x98)) == 0) goto loc_00C74FCB;
    if ((*(uint64_t *)(local_rsp - 0x268 + 0xB8)) == 0) goto loc_00C74FCB;
    if ((*(uint64_t *)(local_rsp - 0x268 + 0xC8)) == 0) goto loc_00C74FD1;
    v_stack_m348 = (uint32_t)(*(uint8_t *)(local_rsp - 0x268 - 0x70));
    result = RtlStringCchPrintfW(local_rsp - 616 + 552, (uint32_t)((uint32_t)(6 + 2)), v_rip + 22779, *(uint8_t *)(local_rsp - 0x268 - 0x6F));
    if (sign_flag) goto loc_00C755FA;
    result = RtlInitUnicodeString(local_rsp - 616 - 32, local_rsp - 616 + 552, v_rip + 22779, *(uint8_t *)(local_rsp - 0x268 - 0x6F));
    if ((*(uint64_t *)(local_rsp - 0x268 + 0xA8)) == 0) goto loc_00C74EC5;
    *(uint64_t *)(local_rsp - 0x268 + 0x30) = local_rsp - 616 + 112;
    *(uint64_t *)(local_rsp - 0x268 + 0x38) = local_rsp - 616 + 128;
loc_00C74E72:
    *(uint64_t *)(local_rsp - 0x268 + 0x40) = local_rsp - 616 + 144;
    Arg1 = (local_rsp - 616 + 144) + (16);
    result = (local_rsp - 616 + 64) + (6 + 2);
    Arg2 = (6 + 2 - 4) - (1);
    if (condition_is_not_equal) goto loc_00C74E72;
    *(uint16_t *)(local_rsp - 0x268 + 0x200) = 0;
    *(uint64_t *)(local_rsp - 0x268 + 0x60) = local_rsp - 616 - 32;
    v_stack_m348 = local_rsp - 616 + 272;
    result = PipCreateComputerId(*(uint64_t *)(local_rsp - 0x268 - 0x48), *(uint64_t *)(local_rsp - 0x268 - 0x28), local_rsp - 616 + 48, Arg2 + 7);
    if (!sign_flag) goto loc_00C74ECB;
    goto loc_00C755FA;
loc_00C74EC5:
loc_00C74ECB:
    *(uint64_t *)(local_rsp - 0x268 + 0x30) = local_rsp - 616 + 112;
    *(uint64_t *)(local_rsp - 0x268 + 0x38) = local_rsp - 616 + 128;
    *(uint64_t *)(local_rsp - 0x268 + 0x40) = local_rsp - 616 + 144;
    *(uint64_t *)(local_rsp - 0x268 + 0x48) = local_rsp - 616 + 176;
    *(uint64_t *)(local_rsp - 0x268 + 0x50) = local_rsp - 616 + 192;
    *(uint64_t *)(local_rsp - 0x268 + 0x58) = local_rsp - 616 - 32;
    *(uint16_t *)(local_rsp - 0x268 + 0x1 * 2 + 0x200) = 1;
    result = (1) << (4);
    result = (result) + (local_rsp - 616 + 272);
    v_stack_m348 = result;
    result = PipCreateComputerId(*(uint64_t *)(local_rsp - 0x268 - 0x48), *(uint64_t *)(local_rsp - 0x268 - 0x28), local_rsp - 616 + 48, 6);
    local_rsi = (uint32_t)((1) + 1);
    if (sign_flag) goto loc_00C755FA;
    *(uint64_t *)(local_rsp - 0x268 + 0x30) = local_rsp - 616 + 112;
    *(uint16_t *)(local_rsp - 0x268 + local_rsi * 2 + 0x200) = 2;
    *(uint64_t *)(local_rsp - 0x268 + 0x38) = local_rsp - 616 + 144;
    *(uint64_t *)(local_rsp - 0x268 + 0x40) = local_rsp - 616 + 176;
    *(uint64_t *)(local_rsp - 0x268 + 0x48) = local_rsp - 616 + 192;
    *(uint64_t *)(local_rsp - 0x268 + 0x50) = local_rsp - 616 - 32;
    result = ((uint32_t)((uint32_t)(local_rsi))) << (4);
    result = (result) + (local_rsp - 616 + 272);
    v_stack_m348 = result;
    result = PipCreateComputerId(*(uint64_t *)(local_rsp - 0x268 - 0x48), *(uint64_t *)(local_rsp - 0x268 - 0x28), local_rsp - 616 + 48, 5);
    local_rsi = (uint32_t)((local_rsi) + (1));
    if (sign_flag) goto loc_00C755FA;
    goto loc_00C74FD7;
loc_00C74FCB:
loc_00C74FD1:
loc_00C74FD7:
    if (*(uint64_t *)(local_rsp - 0x268 + 0x78) == 0) goto loc_00C755D3;
    if ((*(uint64_t *)(local_rsp - 0x268 + 0x98)) == 0) goto loc_00C75188;
    if ((*(uint64_t *)(local_rsp - 0x268 + 0xA8)) == 0) goto loc_00C7511C;
    if ((*(uint64_t *)(local_rsp - 0x268 + 0xD8)) == 0) goto loc_00C750AC;
    if ((*(uint64_t *)(local_rsp - 0x268 + 0xE8)) == 0) goto loc_00C750AC;
    *(uint64_t *)(local_rsp - 0x268 + 0x30) = local_rsp - 616 + 112;
    *(uint64_t *)(local_rsp - 0x268 + 0x38) = local_rsp - 616 + 128;
loc_00C7503B:
    *(uint64_t *)(local_rsp - 0x268 + 0x40) = local_rsp - 616 + 144;
    Arg1 = (local_rsp - 616 + 144) + (16);
    result = (local_rsp - 616 + 64) + (8);
    Arg2 = (2) - (1);
    if (condition_is_not_equal) goto loc_00C7503B;
loc_00C75058:
    *(uint64_t *)(local_rsp - 0x268 + 0x50) = local_rsp - 616 + 208;
    Arg1 = (local_rsp - 616 + 208) + (16);
    result = (local_rsp - 616 + 80) + (8);
    Arg2 = (2) - (1);
    if (condition_is_not_equal) goto loc_00C75058;
    *(uint16_t *)(local_rsp - 0x268 + (uint32_t)((uint32_t)(local_rsi)) * 2 + 0x200) = (uint16_t)(Arg2 + 3);
    result = ((uint32_t)((uint32_t)(local_rsi))) << (4);
    result = (result) + (local_rsp - 616 + 272);
    v_stack_m348 = result;
    result = PipCreateComputerId(*(uint64_t *)(local_rsp - 0x268 - 0x48), *(uint64_t *)(local_rsp - 0x268 - 0x28), local_rsp - 616 + 48, (uint32_t)((uint32_t)(1 + 5)));
    local_rsi = (uint32_t)((local_rsi) + (1));
    if (sign_flag) goto loc_00C755FA;
loc_00C750AC:
    *(uint64_t *)(local_rsp - 0x268 + 0x30) = local_rsp - 616 + 112;
    *(uint64_t *)(local_rsp - 0x268 + 0x38) = local_rsp - 616 + 128;
loc_00C750CF:
    *(uint64_t *)(local_rsp - 0x268 + 0x40) = local_rsp - 616 + 144;
    Arg1 = (local_rsp - 616 + 144) + (16);
    result = (local_rsp - 616 + 64) + (8);
    Arg2 = (2) - (1);
    if (condition_is_not_equal) goto loc_00C750CF;
    *(uint16_t *)(local_rsp - 0x268 + (uint32_t)((uint32_t)(local_rsi)) * 2 + 0x200) = (uint16_t)(Arg2 + 4);
    result = ((uint32_t)((uint32_t)(local_rsi))) << (4);
    result = (result) + (local_rsp - 616 + 272);
    v_stack_m348 = result;
    result = PipCreateComputerId(*(uint64_t *)(local_rsp - 0x268 - 0x48), *(uint64_t *)(local_rsp - 0x268 - 0x28), local_rsp - 616 + 48, (uint32_t)((uint32_t)(Arg2 + 4)));
    local_rsi = (uint32_t)((local_rsi) + 1);
    if (sign_flag) goto loc_00C755FA;
loc_00C7511C:
    *(uint64_t *)(local_rsp - 0x268 + 0x30) = local_rsp - 616 + 112;
    *(uint64_t *)(local_rsp - 0x268 + 0x38) = local_rsp - 616 + 128;
    *(uint64_t *)(local_rsp - 0x268 + 0x40) = local_rsp - 616 + 144;
    *(uint16_t *)(local_rsp - 0x268 + (uint32_t)((uint32_t)(local_rsi)) * 2 + 0x200) = 5;
    result = ((uint32_t)((uint32_t)(local_rsi))) << (4);
    result = (result) + (local_rsp - 616 + 272);
    v_stack_m348 = result;
    result = PipCreateComputerId(*(uint64_t *)(local_rsp - 0x268 - 0x48), *(uint64_t *)(local_rsp - 0x268 - 0x28), local_rsp - 616 + 48, 3);
    local_rsi = (uint32_t)((local_rsi) + (1));
    if (sign_flag) goto loc_00C755FA;
loc_00C75188:
    if (*(uint64_t *)(local_rsp - 0x268 + 0x78) == 0) goto loc_00C755D3;
    if ((*(uint64_t *)(local_rsp - 0x268 + 0xA8)) == 0) goto loc_00C75282;
    if ((*(uint64_t *)(local_rsp - 0x268 + 0xD8)) == 0) goto loc_00C75221;
    if ((*(uint64_t *)(local_rsp - 0x268 + 0xE8)) == 0) goto loc_00C75221;
    *(uint64_t *)(local_rsp - 0x268 + 0x30) = local_rsp - 616 + 112;
    *(uint64_t *)(local_rsp - 0x268 + 0x38) = local_rsp - 616 + 160;
loc_00C751D3:
    *(uint64_t *)(local_rsp - 0x268 + 0x40) = local_rsp - 616 + 208;
    Arg1 = (local_rsp - 616 + 208) + (16);
    result = (local_rsp - 616 + 64) + (8);
    Arg2 = (2) - (1);
    if (condition_is_not_equal) goto loc_00C751D3;
    *(uint16_t *)(local_rsp - 0x268 + (uint32_t)((uint32_t)(local_rsi)) * 2 + 0x200) = (uint16_t)(Arg2 + 6);
    result = ((uint32_t)((uint32_t)(local_rsi))) << (4);
    result = (result) + (local_rsp - 616 + 272);
    v_stack_m348 = result;
    result = PipCreateComputerId(*(uint64_t *)(local_rsp - 0x268 - 0x48), *(uint64_t *)(local_rsp - 0x268 - 0x28), local_rsp - 616 + 48, Arg2 + 4);
    local_rsi = (uint32_t)((local_rsi) + 1);
    if (sign_flag) goto loc_00C755FA;
loc_00C75221:
    *(uint64_t *)(local_rsp - 0x268 + 0x30) = local_rsp - 616 + 112;
    *(uint64_t *)(local_rsp - 0x268 + 0x38) = local_rsp - 616 + 160;
    *(uint16_t *)(local_rsp - 0x268 + (uint32_t)((uint32_t)(local_rsi)) * 2 + 0x200) = 7;
    result = ((uint32_t)((uint32_t)(local_rsi))) << (4);
    result = (result) + (local_rsp - 616 + 272);
    v_stack_m348 = result;
    result = PipCreateComputerId(*(uint64_t *)(local_rsp - 0x268 - 0x48), *(uint64_t *)(local_rsp - 0x268 - 0x28), local_rsp - 616 + 48, 2);
    local_rsi = (uint32_t)((local_rsi) + (1));
    if (sign_flag) goto loc_00C755FA;
loc_00C75282:
    if (*(uint64_t *)(local_rsp - 0x268 + 0x78) == 0) goto loc_00C755D3;
    if ((*(uint64_t *)(local_rsp - 0x268 + 0x98)) == 0) goto loc_00C75373;
    if ((*(uint64_t *)(local_rsp - 0x268 + 0xD8)) == 0) goto loc_00C75312;
    if ((*(uint64_t *)(local_rsp - 0x268 + 0xE8)) == 0) goto loc_00C75312;
    *(uint64_t *)(local_rsp - 0x268 + 0x30) = local_rsp - 616 + 112;
    *(uint64_t *)(local_rsp - 0x268 + 0x38) = local_rsp - 616 + 144;
    *(uint64_t *)(local_rsp - 0x268 + 0x40) = local_rsp - 616 + 208;
    *(uint64_t *)(local_rsp - 0x268 + 0x48) = local_rsp - 616 + 224;
    *(uint16_t *)(local_rsp - 0x268 + (uint32_t)((uint32_t)(local_rsi)) * 2 + 0x200) = 8;
    result = ((uint32_t)((uint32_t)(local_rsi))) << (4);
    result = (result) + (local_rsp - 616 + 272);
    v_stack_m348 = result;
    result = PipCreateComputerId(*(uint64_t *)(local_rsp - 0x268 - 0x48), *(uint64_t *)(local_rsp - 0x268 - 0x28), local_rsp - 616 + 48, 4);
    local_rsi = (uint32_t)((local_rsi) + 1);
    if (sign_flag) goto loc_00C755FA;
loc_00C75312:
    *(uint64_t *)(local_rsp - 0x268 + 0x30) = local_rsp - 616 + 112;
    *(uint64_t *)(local_rsp - 0x268 + 0x38) = local_rsp - 616 + 144;
    *(uint16_t *)(local_rsp - 0x268 + (uint32_t)((uint32_t)(local_rsi)) * 2 + 0x200) = 9;
    result = ((uint32_t)((uint32_t)(local_rsi))) << (4);
    result = (result) + (local_rsp - 616 + 272);
    v_stack_m348 = result;
    result = PipCreateComputerId(*(uint64_t *)(local_rsp - 0x268 - 0x48), *(uint64_t *)(local_rsp - 0x268 - 0x28), local_rsp - 616 + 48, 2);
    local_rsi = (uint32_t)((local_rsi) + (1));
    if (sign_flag) goto loc_00C755FA;
loc_00C75373:
    if (*(uint64_t *)(local_rsp - 0x268 + 0x78) == 0) goto loc_00C755D3;
    if ((*(uint64_t *)(local_rsp - 0x268 + 0x88)) == 0) goto loc_00C75464;
    if ((*(uint64_t *)(local_rsp - 0x268 + 0xE8)) == 0) goto loc_00C7540A;
    if ((*(uint64_t *)(local_rsp - 0x268 + 0xD8)) == 0) goto loc_00C7540A;
    *(uint64_t *)(local_rsp - 0x268 + 0x30) = local_rsp - 616 + 112;
    *(uint64_t *)(local_rsp - 0x268 + 0x38) = local_rsp - 616 + 128;
loc_00C753BE:
    *(uint64_t *)(local_rsp - 0x268 + 0x40) = local_rsp - 616 + 208;
    Arg1 = (local_rsp - 616 + 208) + (16);
    result = (local_rsp - 616 + 64) + (8);
    Arg2 = (2) - (1);
    if (condition_is_not_equal) goto loc_00C753BE;
    *(uint16_t *)(local_rsp - 0x268 + (uint32_t)((uint32_t)(local_rsi)) * 2 + 0x200) = 10;
    result = ((uint32_t)((uint32_t)(local_rsi))) << (4);
    result = (result) + (local_rsp - 616 + 272);
    v_stack_m348 = result;
    result = PipCreateComputerId(*(uint64_t *)(local_rsp - 0x268 - 0x48), *(uint64_t *)(local_rsp - 0x268 - 0x28), local_rsp - 616 + 48, Arg2 + 4);
    local_rsi = (uint32_t)((local_rsi) + 1);
    if (sign_flag) goto loc_00C755FA;
loc_00C7540A:
    *(uint64_t *)(local_rsp - 0x268 + 0x30) = local_rsp - 616 + 112;
    *(uint64_t *)(local_rsp - 0x268 + 0x38) = local_rsp - 616 + 128;
    *(uint16_t *)(local_rsp - 0x268 + (uint32_t)((uint32_t)(local_rsi)) * 2 + 0x200) = 11;
    result = ((uint32_t)((uint32_t)(local_rsi))) << (4);
    result = (result) + (local_rsp - 616 + 272);
    v_stack_m348 = result;
    result = PipCreateComputerId(*(uint64_t *)(local_rsp - 0x268 - 0x48), *(uint64_t *)(local_rsp - 0x268 - 0x28), local_rsp - 616 + 48, 2);
    local_rsi = (uint32_t)((local_rsi) + 1);
    if (sign_flag) goto loc_00C755FA;
loc_00C75464:
    if (*(uint64_t *)(local_rsp - 0x268 + 0x78) == 0) goto loc_00C755D3;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x268 - 0x50))) == 0) goto loc_00C7550B;
    result = RtlStringCchPrintfW(local_rsp - 616 + 544, 4, v_rip + 21167, (uint32_t)(*(uint32_t *)(local_rsp - 0x268 - 0x50)));
    if (sign_flag) goto loc_00C755FA;
    result = RtlInitUnicodeString(local_rsp - 616 - 16, local_rsp - 616 + 544, v_rip + 21167, (uint32_t)(*(uint32_t *)(local_rsp - 0x268 - 0x50)));
    *(uint64_t *)(local_rsp - 0x268 + 0x30) = local_rsp - 616 + 112;
    *(uint64_t *)(local_rsp - 0x268 + 0x38) = local_rsp - 616 - 16;
    Arg2 = 0;
    *(uint16_t *)(local_rsp - 0x268 + (uint32_t)((uint32_t)(local_rsi)) * 2 + 0x200) = 12;
    result = ((uint32_t)((uint32_t)(local_rsi))) << (4);
    result = (result) + (local_rsp - 616 + 272);
    v_stack_m348 = result;
    result = PipCreateComputerId(*(uint64_t *)(local_rsp - 0x268 - 0x48), Arg2, local_rsp - 616 + 48, 2);
    local_rsi = (uint32_t)((local_rsi) + ((uint32_t)(2 - 1)));
    if (sign_flag) goto loc_00C755FA;
    goto loc_00C75514;
loc_00C7550B:
loc_00C75514:
    if (*(uint64_t *)(local_rsp - 0x268 + 0x78) == 0) goto loc_00C755D3;
    if ((*(uint64_t *)(local_rsp - 0x268 + 0xE8)) == 0) goto loc_00C75593;
    if ((*(uint64_t *)(local_rsp - 0x268 + 0xD8)) == 0) goto loc_00C75593;
    *(uint64_t *)(local_rsp - 0x268 + 0x30) = local_rsp - 616 + 112;
loc_00C75545:
    *(uint64_t *)(local_rsp - 0x268 + 0x38) = local_rsp - 616 + 208;
    Arg1 = (local_rsp - 616 + 208) + (16);
    result = (local_rsp - 616 + 56) + (8);
    Arg2 = (2) - (2 - 1);
    if (condition_is_not_equal) goto loc_00C75545;
    *(uint16_t *)(local_rsp - 0x268 + (uint32_t)((uint32_t)(local_rsi)) * 2 + 0x200) = (uint16_t)(Arg2 + 13);
    result = ((uint32_t)((uint32_t)(local_rsi))) << (4);
    result = (result) + (local_rsp - 616 + 272);
    v_stack_m348 = result;
    result = PipCreateComputerId(*(uint64_t *)(local_rsp - 0x268 - 0x48), Arg2, local_rsp - 616 + 48, Arg2 + 3);
    local_rsi = (uint32_t)((local_rsi) + (1));
    if (sign_flag) goto loc_00C755FA;
loc_00C75593:
    *(uint64_t *)(local_rsp - 0x268 + 0x30) = local_rsp - 616 + 112;
    Arg2 = 0;
    *(uint16_t *)(local_rsp - 0x268 + (uint32_t)((uint32_t)(local_rsi)) * 2 + 0x200) = 14;
    result = ((uint32_t)((uint32_t)(local_rsi))) << (4);
    result = (result) + (local_rsp - 616 + 272);
    v_stack_m348 = result;
    result = PipCreateComputerId(*(uint64_t *)(local_rsp - 0x268 - 0x48), Arg2, local_rsp - 616 + 48, 1);
    local_rsi = (uint32_t)((local_rsi) + 1);
    if (sign_flag) goto loc_00C755FA;
loc_00C755D3:
    local_rdi = (uint32_t)((2) * ((uint32_t)(local_rsi)));
    local_rdi = (uint32_t)((local_rdi) + (2));
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(local_rdi)), (uint32_t)(0x6E697050ULL), 1);
    Arg1 = 0;
    if (result != 0) goto loc_00C75608;
loc_00C755FA:
    goto loc_00C748AE;
loc_00C75608:
    *(uint64_t *)(local_rsp - 0x268 - 0x80) = result;
    v_stack_m2EE = (uint16_t)(local_rdi);
    if ((uint32_t)(local_rsi) == 0) goto loc_00C756B0;
loc_00C7561C:
    v_stack_m2F0 = 0;
    a4 = 0;
    result = RtlUnicodeStringCopyStringEx(v_stack_m2F0, v_rip + 20747, v_stack_m2F0, a4);
    Arg1 = 0;
    if (sign_flag) goto loc_00C75BDD;
    result = (0) << (4);
    Arg1 = (local_rsp - 616 + 272) + (result);
    a3 = 0;
    result = RtlStringFromGUIDEx(Arg1, v_stack_m2F0, a3, a4);
    result = 0;
    if (sign_flag) goto loc_00C75BE5;
    a3 = 0;
    result = RtlUpcaseUnicodeString(v_stack_m2F0, v_stack_m2F0, a3, a4);
    Arg1 = 0;
    if (sign_flag) goto loc_00C75BDD;
    result = (*(uint64_t *)(local_rsp - 0x268 - 0x80)) + (78);
    local_r14 = (uint32_t)((0) + 1);
    *(uint64_t *)(local_rsp - 0x268 - 0x80) = result;
    if (((uint32_t)(local_r14)) < ((uint32_t)(local_rsi))) goto loc_00C7561C;
loc_00C756B0:
    if (sign_flag) goto loc_00C75BED;
    v_stack_m320 = 0;
    v_stack_m328 = (uint32_t)(local_rdi);
    *(uint16_t *)(result) = 0;
    a4 = 0;
    v_stack_m330 = (uint32_t)(v_stack_m2F8);
    v_stack_m338 = 0x2012ULL;
    v_stack_m340 = v_rip - 12992910;
    v_stack_m348 = 0;
    result = PnpSetObjectProperty(*(uint64_t *)(v_rip + 0x1F0C98), v_rip + 18493, 2 + 3, a4);
    result = 0;
    if (sign_flag) goto loc_00C75BE5;
    local_rbx = (uint32_t)((local_rsi + local_rsi * 2) << (5));
    local_rbx = (uint32_t)((local_rbx) + (2));
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(local_rbx)), (uint32_t)(0x6E697050ULL), a4);
    a3 = 0;
    *(uint64_t *)(local_rsp - 0x268 - 0x30) = result;
    if (result != 0) goto loc_00C75748;
loc_00C7573D:
    goto loc_00C75BF4;
loc_00C75748:
    *(uint64_t *)(local_rsp - 0x268 - 0x80) = result;
    v_stack_m2EE = (uint16_t)((uint32_t)(0xC000009AULL));
    if (0 == 0) goto loc_00C75818;
loc_00C75766:
    v_stack_m2F0 = 0;
    if ((*(uint8_t *)(*(uint16_t *)(local_rsp - 0x268 + 0x200) + v_rip - 0xC4DC81 * 1)) == 0) goto loc_00C75804;
    a4 = 0;
    result = RtlUnicodeStringCopyStringEx(v_stack_m2F0, v_rip + 20448, v_stack_m2F0, a4);
    result = 0;
    if (sign_flag) goto loc_00C75BE5;
    result = (0) << (4);
    Arg1 = (local_rsp - 616 + 272) + (result);
    a3 = 0;
    result = RtlStringFromGUIDEx(Arg1, v_stack_m2F0, a3, a4);
    result = 0;
    if (sign_flag) goto loc_00C75BE5;
    a3 = 0;
    result = RtlUpcaseUnicodeString(v_stack_m2F0, v_stack_m2F0, a3, a4);
    a3 = 0;
    if (sign_flag) goto loc_00C7573D;
    Arg1 = (*(uint64_t *)(local_rsp - 0x268 - 0x80)) + (78);
    *(void **)(local_rsp - 0x268 - 0x80) = Arg1;
loc_00C75804:
    local_rdi = (uint32_t)((0) + 1);
    local_r14 = (local_rsp - 616 + 512) + (2);
    if (((uint32_t)(local_rdi)) < 0) goto loc_00C75766;
loc_00C75818:
    local_rdi = 0;
    *(uint16_t *)(arg1) = 0;
    result = ExAllocatePool2(256, 400, (uint32_t)(0x6E697050ULL), a4);
    if (result != 0) goto loc_00C7584B;
loc_00C75843:
    goto loc_00C75BF4;
loc_00C7584B:
    *(uint64_t *)(local_rsp - 0x268 - 0x58) = result;
    *(uint64_t *)(local_rsp - 0x268 - 0x68) = 200;
    if (((uint16_t)(*(uint16_t *)(local_rsp - 0x268 + 0x70))) <= ((uint16_t)(70 - 68))) goto loc_00C7588D;
    *(uint64_t *)(local_rsp - 0x268 - 0x80) = *(uint64_t *)(local_rsp - 0x268 + 0x78);
    v_stack_m2EE = (uint16_t)(*(uint16_t *)(local_rsp - 0x268 + 0x72));
    if (((uint16_t)(*(uint16_t *)(local_rsp - 0x268 + 0x70))) <= 70) goto loc_00C75886;
    v_stack_m2F0 = 70;
    goto loc_00C7589E;
loc_00C75886:
    v_stack_m2F0 = (uint16_t)(*(uint16_t *)(local_rsp - 0x268 + 0x70));
    goto loc_00C7589E;
loc_00C7588D:
    result = RtlInitUnicodeString(v_stack_m2F0, v_rip + 19996, (uint32_t)(0x6E697050ULL), a4);
loc_00C7589E:
    v_stack_m338 = v_stack_m2F0;
    v_stack_m340 = v_rip + 19978;
    v_stack_m348 = 0x800ULL;
    result = RtlStringCchPrintfExW(result, 200, local_rsp - 616 - 88, local_rsp - 616 - 104);
    if (sign_flag) goto loc_00C75843;
    if (((uint16_t)(*(uint16_t *)(local_rsp - 0x268 + 0x80))) <= 2) goto loc_00C75955;
    *(uint64_t *)(local_rsp - 0x268 - 0x80) = *(uint64_t *)(local_rsp - 0x268 + 0x88);
    v_stack_m2EE = (uint16_t)(*(uint16_t *)(local_rsp - 0x268 + 0x82));
    v_stack_m2F0 = 70;
    if (((uint16_t)(*(uint16_t *)(local_rsp - 0x268 + 0x80))) <= 70) {
        v_stack_m2F0 = (uint16_t)(*(uint16_t *)(local_rsp - 0x268 + 0x80));
    }
    v_stack_m338 = v_stack_m2F0;
    v_stack_m340 = v_rip + 19869;
    v_stack_m348 = 0x800ULL;
    result = RtlStringCchPrintfExW(*(uint64_t *)(local_rsp - 0x268 - 0x58), *(uint64_t *)(local_rsp - 0x268 - 0x68), local_rsp - 616 - 88, local_rsp - 616 - 104);
    if (sign_flag) goto loc_00C75843;
loc_00C75955:
    if (((uint16_t)(*(uint16_t *)(local_rsp - 0x268 + 0x90))) <= 2) goto loc_00C759D2;
    *(uint64_t *)(local_rsp - 0x268 - 0x80) = *(uint64_t *)(local_rsp - 0x268 + 0x98);
    v_stack_m2EE = (uint16_t)(*(uint16_t *)(local_rsp - 0x268 + 0x92));
    v_stack_m2F0 = 70;
    if (((uint16_t)(*(uint16_t *)(local_rsp - 0x268 + 0x90))) <= 70) {
        v_stack_m2F0 = (uint16_t)(*(uint16_t *)(local_rsp - 0x268 + 0x90));
    }
    v_stack_m338 = v_stack_m2F0;
    v_stack_m340 = v_rip + 19783;
    v_stack_m348 = 0x800ULL;
    result = RtlStringCchPrintfExW(*(uint64_t *)(local_rsp - 0x268 - 0x58), *(uint64_t *)(local_rsp - 0x268 - 0x68), local_rsp - 616 - 88, local_rsp - 616 - 104);
    if (sign_flag) goto loc_00C75843;
loc_00C759D2:
    if (((uint16_t)(*(uint16_t *)(local_rsp - 0x268 + 0xA0))) <= 2) goto loc_00C75A4F;
    *(uint64_t *)(local_rsp - 0x268 - 0x80) = *(uint64_t *)(local_rsp - 0x268 + 0xA8);
    v_stack_m2EE = (uint16_t)(*(uint16_t *)(local_rsp - 0x268 + 0xA2));
    v_stack_m2F0 = 70;
    if (((uint16_t)(*(uint16_t *)(local_rsp - 0x268 + 0xA0))) <= 70) {
        v_stack_m2F0 = (uint16_t)(*(uint16_t *)(local_rsp - 0x268 + 0xA0));
    }
    v_stack_m338 = v_stack_m2F0;
    v_stack_m340 = v_rip + 19898;
    v_stack_m348 = 0x800ULL;
    result = RtlStringCchPrintfExW(*(uint64_t *)(local_rsp - 0x268 - 0x58), *(uint64_t *)(local_rsp - 0x268 - 0x68), local_rsp - 616 - 88, local_rsp - 616 - 104);
    if (sign_flag) goto loc_00C75843;
loc_00C75A4F:
    if ((uint16_t)(*(uint16_t *)(result)) == 0) goto loc_00C75A89;
loc_00C75A5B:
    if (((uint16_t)(*(uint16_t *)(result) - 33)) > 94) goto loc_00C75A70;
    if (((uint16_t)(*(uint16_t *)(result))) == 44) goto loc_00C75A70;
    if (((uint16_t)(*(uint16_t *)(result))) == 92) {
        *(uint16_t *)(result) = 95;
    }
    a3 = (result) + (2);
    if ((uint16_t)(*(uint16_t *)(a3)) != 0) goto loc_00C75A5B;
loc_00C75A89:
    result = (uint32_t)((*(uint16_t *)(local_rsp - 0x268 + 0x70)) + (4));
    Arg2 = (uint32_t)(((uint16_t)(*(uint16_t *)(local_rsp - 0x268 + 0x90))) + ((uint32_t)(result)));
    result = ExAllocatePool2(256, Arg2, (uint32_t)(0x6E697050ULL), 2);
    if (result != 0) goto loc_00C75AB7;
    goto loc_00C75BF4;
loc_00C75AB7:
    local_rdi = result;
    if ((*(uint16_t *)(local_rsp - 0x268 + 0x70)) >= 2) {
        a3 = *(uint16_t *)(local_rsp - 0x268 + 0x70);
        Arg1 = result;
        Arg2 = *(uint64_t *)(local_rsp - 0x268 + 0x78);
        result = memcpy(Arg1, Arg2, a3, 2);
        result = *(uint16_t *)(local_rsp - 0x268 + 0x70);
        result = (result) >> (1);
        result = result + result * 2;
        local_rdi = result;
    }
    if (((uint16_t)(*(uint16_t *)(local_rsp - 0x268 + 0x90))) < 2) goto loc_00C75B2D;
    if (local_rdi != result) {
        *(uint16_t *)(result) = 32;
        local_rdi = (local_rdi) + (2);
        Arg1 = *(uint16_t *)(local_rsp - 0x268 + 0x90);
    }
    result = memcpy(local_rdi, *(uint64_t *)(local_rsp - 0x268 + 0x98), (uint16_t)(Arg1), 2);
    result = (*(uint16_t *)(local_rsp - 0x268 + 0x90)) >> (1);
loc_00C75B2D:
    Arg1 = 0;
    *(uint16_t *)(local_rdi + result * 2) = 0;
    local_rdi = (local_rdi + result * 2) - (result);
    v_stack_m308 = 1;
    *(uint32_t *)(local_rsp - 0x268 + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0xC61A97)));
    *(uint32_t *)(local_rsp - 0x268 + 0x14) = 0;
    *(uint64_t *)(local_rsp - 0x268 + 0x18) = 0;
    *(uint64_t *)(local_rsp - 0x268) = v_xmm0;
    *(uint32_t *)(local_rsp - 0x268 + 0x20) = 18;
    *(uint64_t *)(local_rsp - 0x268 + 0x28) = result;
    local_rdi = (local_rdi) >> (1);
    *(uint32_t *)(local_rsp - 0x268 + 0x24) = (uint32_t)(local_rdi * 2 + 2);
    v_stack_m310 = local_rsp - 616;
    v_stack_m318 = 0;
    v_stack_m320 = 0;
    v_stack_m328 = 0;
    v_stack_m330 = result;
    v_stack_m338 = 0;
    v_stack_m340 = 0;
    v_stack_m348 = v_rip + 19566;
    result = PiSwStartCreate(v_rip + 19579, *(uint64_t *)(*(uint64_t *)(v_rip + 0x3168E8) + 0x30), result, *(uint64_t *)(local_rsp - 0x268 - 0x30));
    if (!sign_flag) goto loc_00C75BF4;
    if (((*(uint8_t *)(v_rip + 0x27A562)) & (16)) == 0) goto loc_00C75BF4;
    result = McTemplateK0d_EtwWriteTransfer(v_rip + 19579, v_rip - 12904758, result, (uint32_t)((uint32_t)(result)));
    goto loc_00C75BF4;
loc_00C75BDD:
    goto loc_00C75BF4;
loc_00C75BE5:
    goto loc_00C75BF4;
loc_00C75BED:
loc_00C75BF4:
    Arg2 = 0;
    result = ExFreePoolWithTag((uint32_t)(v_stack_m2F8), Arg2, result, (uint32_t)((uint32_t)(result)));
    result = *(uint64_t *)(local_rsp - 0x268 - 0x30);
    if (*(uint64_t *)(local_rsp - 0x268 - 0x30) != 0) {
        Arg2 = 0;
        Arg1 = *(uint64_t *)(local_rsp - 0x268 - 0x30);
        result = ExFreePoolWithTag(Arg1, Arg2, result, (uint32_t)((uint32_t)(result)));
    }
    if (*(uint64_t *)(local_rsp - 0x268 - 0x60) != 0) {
        Arg2 = 0;
        Arg1 = *(uint64_t *)(local_rsp - 0x268 - 0x60);
        result = ExFreePoolWithTag(Arg1, Arg2, result, (uint32_t)((uint32_t)(result)));
    }
    if (*(uint64_t *)(local_rsp - 0x268 - 0x60) == 0) goto loc_00C755FA;
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(local_rsp - 0x268 - 0x60), Arg2, result, (uint32_t)((uint32_t)(result)));
    goto loc_00C755FA;
loc_00C75C38:
    Arg1 = (*(uint64_t *)(local_rsp - 0x268 + 0x238)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, result, (uint32_t)((uint32_t)(result)));
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xF0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C74734&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
