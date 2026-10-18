# PiDevCfgLogDeviceConfigured

- RVA: `0x00ADCDD4`–`0x00ADE11F` (길이 `4,939` bytes)
- VA: `0x0000000140ADCDD4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C8C94`
- 디코드: `1,160`개 명령, `4,939/4,939` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **82**; 고유 호출 대상: **19**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **26**

### Outgoing calls
- `0x00ADCEDD` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00ADCFA5` → [PiDevCfgQueryObjectProperties](../97/PiDevCfgQueryObjectProperties_function_0097776C.md) (function, `0x0097776C`)
- `0x00ADCFC0` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00ADCFD3` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00ADD044` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x00ADD04F` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00ADD062` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00ADD084` → [RtlEqualUnicodeString](../93/RtlEqualUnicodeString_function_00932A20.md) (function, `0x00932A20`)
- `0x00ADD09A` → [RtlTimeToTimeFields](../../text/42/RtlTimeToTimeFields_function_0042E0F0.md) (function, `0x0042E0F0`)
- `0x00ADD0C7` → [RtlStringCchPrintfW](../../text/48/RtlStringCchPrintfW_function_00482D5C.md) (function, `0x00482D5C`)
- `0x00ADD10F` → [RtlStringCchPrintfW](../../text/48/RtlStringCchPrintfW_function_00482D5C.md) (function, `0x00482D5C`)
- `0x00ADD12B` → [Feature_KernelPnP_LogBlockedDrivers__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_KernelPnP_LogBlockedDrivers__private_IsEnabledDeviceUsageNoInline_function_004F7944.md) (function, `0x004F7944`)
- `0x00ADD1C1` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00ADD205` → [RtlUnicodeStringCopyStringEx](../../text/5A/RtlUnicodeStringCopyStringEx_function_005A4FC0.md) (function, `0x005A4FC0`)
- `0x00ADD240` → [RtlUnicodeStringPrintfEx](../../text/4A/RtlUnicodeStringPrintfEx_function_004A8FD0.md) (function, `0x004A8FD0`)
- `0x00ADD286` → [RtlUnicodeStringPrintfEx](../../text/4A/RtlUnicodeStringPrintfEx_function_004A8FD0.md) (function, `0x004A8FD0`)
- `0x00ADD2B7` → [Feature_KernelPnP_LogBlockedDrivers__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_KernelPnP_LogBlockedDrivers__private_IsEnabledDeviceUsageNoInline_function_004F7944.md) (function, `0x004F7944`)
- `0x00ADD348` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00ADD392` → [RtlUnicodeStringCopyStringEx](../../text/5A/RtlUnicodeStringCopyStringEx_function_005A4FC0.md) (function, `0x005A4FC0`)
- `0x00ADD3CD` → [RtlUnicodeStringPrintfEx](../../text/4A/RtlUnicodeStringPrintfEx_function_004A8FD0.md) (function, `0x004A8FD0`)
- `0x00ADD413` → [RtlUnicodeStringPrintfEx](../../text/4A/RtlUnicodeStringPrintfEx_function_004A8FD0.md) (function, `0x004A8FD0`)
- `0x00ADD4B5` → [PnpGetLogString](../../text/4C/PnpGetLogString_function_004C26F4.md) (function, `0x004C26F4`)
- `0x00ADD4C1` → [PnpGetLogString](../../text/4C/PnpGetLogString_function_004C26F4.md) (function, `0x004C26F4`)
- `0x00ADD4CC` → [PnpGetLogString](../../text/4C/PnpGetLogString_function_004C26F4.md) (function, `0x004C26F4`)
- `0x00ADD4D7` → [PnpGetLogString](../../text/4C/PnpGetLogString_function_004C26F4.md) (function, `0x004C26F4`)
- `0x00ADD4E2` → [PnpGetLogString](../../text/4C/PnpGetLogString_function_004C26F4.md) (function, `0x004C26F4`)
- `0x00ADD596` → [PnpGetLogString](../../text/4C/PnpGetLogString_function_004C26F4.md) (function, `0x004C26F4`)
- `0x00ADD5A2` → [PnpGetLogString](../../text/4C/PnpGetLogString_function_004C26F4.md) (function, `0x004C26F4`)
- `0x00ADD5AD` → [PnpGetLogString](../../text/4C/PnpGetLogString_function_004C26F4.md) (function, `0x004C26F4`)
- `0x00ADD5B8` → [PnpGetLogString](../../text/4C/PnpGetLogString_function_004C26F4.md) (function, `0x004C26F4`)
- `0x00ADD5C3` → [PnpGetLogString](../../text/4C/PnpGetLogString_function_004C26F4.md) (function, `0x004C26F4`)
- `0x00ADD639` → [McTemplateK0zzjzzztzdzztdzz_EtwWriteTransfer](../../text/42/McTemplateK0zzjzzztzdzztdzz_EtwWriteTransfer_function_00424C50.md) (function, `0x00424C50`)
- `0x00ADD6BD` → [PnpGetLogString](../../text/4C/PnpGetLogString_function_004C26F4.md) (function, `0x004C26F4`)
- `0x00ADD6C9` → [PnpGetLogString](../../text/4C/PnpGetLogString_function_004C26F4.md) (function, `0x004C26F4`)
- `0x00ADD6D4` → [PnpGetLogString](../../text/4C/PnpGetLogString_function_004C26F4.md) (function, `0x004C26F4`)
- `0x00ADD6DF` → [PnpGetLogString](../../text/4C/PnpGetLogString_function_004C26F4.md) (function, `0x004C26F4`)
- `0x00ADD6EA` → [PnpGetLogString](../../text/4C/PnpGetLogString_function_004C26F4.md) (function, `0x004C26F4`)
- `0x00ADD75C` → [McTemplateK0zzjzzztzdzztdzz_EtwWriteTransfer](../../text/42/McTemplateK0zzjzzztzdzztdzz_EtwWriteTransfer_function_00424C50.md) (function, `0x00424C50`)
- `0x00ADD7E2` → [PnpGetLogString](../../text/4C/PnpGetLogString_function_004C26F4.md) (function, `0x004C26F4`)
- `0x00ADD7EE` → [PnpGetLogString](../../text/4C/PnpGetLogString_function_004C26F4.md) (function, `0x004C26F4`)
- `0x00ADD7F9` → [PnpGetLogString](../../text/4C/PnpGetLogString_function_004C26F4.md) (function, `0x004C26F4`)
- `0x00ADD804` → [PnpGetLogString](../../text/4C/PnpGetLogString_function_004C26F4.md) (function, `0x004C26F4`)
- `0x00ADD80F` → [PnpGetLogString](../../text/4C/PnpGetLogString_function_004C26F4.md) (function, `0x004C26F4`)
- `0x00ADD8C2` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00ADD8DC` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00ADD951` → [PiDevCfgLogDeviceConfigured](PiDevCfgLogDeviceConfigured_function_00ADCDD4.md) (function, `0x00ADCDD4`)
- `0x00ADD965` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00ADDA3B` → [PiDevCfgQueryObjectProperties](../97/PiDevCfgQueryObjectProperties_function_0097776C.md) (function, `0x0097776C`)
- `0x00ADDA5B` → [RtlCreateUnicodeString](../9B/RtlCreateUnicodeString_function_009BD860.md) (function, `0x009BD860`)
- `0x00ADDA6D` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00ADDA88` → [RtlStringFromGUIDEx](../91/RtlStringFromGUIDEx_function_00915450.md) (function, `0x00915450`)
- `0x00ADDA97` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00ADDAAA` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00ADDB1A` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x00ADDB25` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00ADDB3B` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00ADDBB7` → [RtlUnicodeStringPrintfEx](../../text/4A/RtlUnicodeStringPrintfEx_function_004A8FD0.md) (function, `0x004A8FD0`)
- `0x00ADDBC2` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x00ADDBCB` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x00ADDBD7` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x00ADDBE3` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x00ADDC99` → [PnpDuplicateUnicodeString](../../text/4C/PnpDuplicateUnicodeString_function_004CC044.md) (function, `0x004CC044`)
- `0x00ADDD05` → [PnpDuplicateUnicodeString](../../text/4C/PnpDuplicateUnicodeString_function_004CC044.md) (function, `0x004CC044`)
- `0x00ADDD71` → [PnpDuplicateUnicodeString](../../text/4C/PnpDuplicateUnicodeString_function_004CC044.md) (function, `0x004CC044`)
- `0x00ADDDE4` → [PnpDuplicateUnicodeString](../../text/4C/PnpDuplicateUnicodeString_function_004CC044.md) (function, `0x004CC044`)
- `0x00ADDE48` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00ADDEC1` → [PiDevCfgQueryObjectProperties](../97/PiDevCfgQueryObjectProperties_function_0097776C.md) (function, `0x0097776C`)
- `0x00ADDEE0` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00ADDF55` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x00ADDF60` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00ADE09C` → [PnpTraceDeviceConfig](../70/PnpTraceDeviceConfig_function_00700CC0.md) (function, `0x00700CC0`)
- `0x00ADE0A5` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x00ADE0AE` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x00ADE0B7` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x00ADE0C0` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x00ADE0C9` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x00ADE0D2` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x00ADE0DB` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x00ADE0E4` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x00ADE0ED` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x00ADE0F6` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x00ADE105` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PiDevCfgProcessDevice](../97/PiDevCfgProcessDevice_function_00976D34.md) at `0x009770BC`
- [PiDevCfgLogDeviceConfigured](PiDevCfgLogDeviceConfigured_function_00ADCDD4.md) at `0x00ADD951`

### Static image references
- `0x00ADCDF0` → RVA `0x00E0A740` (`.data`; read)
- `0x00ADCE14` → RVA `0x00EF012A` (`.data`; read)
- `0x00ADCEF2` → RVA `0x00022D18` (`.rdata`; read)
- `0x00ADCF1F` → RVA `0x000235E0` (`.rdata`; read)
- `0x00ADCF38` → RVA `0x00022C40` (`.rdata`; read)
- `0x00ADCF51` → RVA `0x00021950` (`.rdata`; read)
- `0x00ADD0A3` → RVA `0x00AFEA20` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00ADD104` → RVA `0x00AFE8B0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00ADD1FA` → RVA `0x00AFCA30` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00ADD226` → RVA `0x00AFE8D0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00ADD25A` → RVA `0x00AFE8F0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00ADD271` → RVA `0x00AFE900` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00ADD456` → RVA `0x00B53AB8` (` ?? ::LBKOJDO::`string'`; read)
- `0x00ADD49A` → RVA `0x00B4AFF8` (`PiDevCfgNullGuid`; read)
- `0x00ADD51B` → RVA `0x00027330` (`.rdata`; read)
- `0x00ADD5FC` → RVA `0x00027180` (`.rdata`; read)
- `0x00ADD72A` → RVA `0x00026DF0` (`.rdata`; read)
- `0x00ADD848` → RVA `0x00027240` (`.rdata`; read)
- `0x00ADD997` → RVA `0x00020E70` (`.rdata`; read)
- `0x00ADDB47` → RVA `0x00B4AD08` (`PiDevCfgEmptyString`; read)
- `0x00ADDB4E` → RVA `0x00AFCAD0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00ADDB68` → RVA `0x00AFEAF0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00ADDBA7` → RVA `0x00AFEB00` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00ADDE51` → RVA `0x000221D0` (`.rdata`; read)
- `0x00ADDE70` → RVA `0x00021B60` (`.rdata`; read)
- `0x00ADDF84` → RVA `0x00E66245` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **57**
  - `0x00ADCEDD` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00ADCFC0` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00ADCFD3` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00ADD04F` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00ADD062` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00ADD09A` → [RtlTimeToTimeFields](../../text/42/RtlTimeToTimeFields_function_0042E0F0.md) (`PAGE` → `.text`)
  - `0x00ADD0C7` → [RtlStringCchPrintfW](../../text/48/RtlStringCchPrintfW_function_00482D5C.md) (`PAGE` → `.text`)
  - `0x00ADD10F` → [RtlStringCchPrintfW](../../text/48/RtlStringCchPrintfW_function_00482D5C.md) (`PAGE` → `.text`)
  - `0x00ADD12B` → [Feature_KernelPnP_LogBlockedDrivers__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_KernelPnP_LogBlockedDrivers__private_IsEnabledDeviceUsageNoInline_function_004F7944.md) (`PAGE` → `.text`)
  - `0x00ADD1C1` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00ADD205` → [RtlUnicodeStringCopyStringEx](../../text/5A/RtlUnicodeStringCopyStringEx_function_005A4FC0.md) (`PAGE` → `.text`)
  - `0x00ADD240` → [RtlUnicodeStringPrintfEx](../../text/4A/RtlUnicodeStringPrintfEx_function_004A8FD0.md) (`PAGE` → `.text`)
  - `0x00ADD286` → [RtlUnicodeStringPrintfEx](../../text/4A/RtlUnicodeStringPrintfEx_function_004A8FD0.md) (`PAGE` → `.text`)
  - `0x00ADD2B7` → [Feature_KernelPnP_LogBlockedDrivers__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_KernelPnP_LogBlockedDrivers__private_IsEnabledDeviceUsageNoInline_function_004F7944.md) (`PAGE` → `.text`)
  - `0x00ADD348` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00ADD392` → [RtlUnicodeStringCopyStringEx](../../text/5A/RtlUnicodeStringCopyStringEx_function_005A4FC0.md) (`PAGE` → `.text`)
  - `0x00ADD3CD` → [RtlUnicodeStringPrintfEx](../../text/4A/RtlUnicodeStringPrintfEx_function_004A8FD0.md) (`PAGE` → `.text`)
  - `0x00ADD413` → [RtlUnicodeStringPrintfEx](../../text/4A/RtlUnicodeStringPrintfEx_function_004A8FD0.md) (`PAGE` → `.text`)
  - `0x00ADD4B5` → [PnpGetLogString](../../text/4C/PnpGetLogString_function_004C26F4.md) (`PAGE` → `.text`)
  - `0x00ADD4C1` → [PnpGetLogString](../../text/4C/PnpGetLogString_function_004C26F4.md) (`PAGE` → `.text`)
  - `0x00ADD4CC` → [PnpGetLogString](../../text/4C/PnpGetLogString_function_004C26F4.md) (`PAGE` → `.text`)
  - `0x00ADD4D7` → [PnpGetLogString](../../text/4C/PnpGetLogString_function_004C26F4.md) (`PAGE` → `.text`)
  - `0x00ADD4E2` → [PnpGetLogString](../../text/4C/PnpGetLogString_function_004C26F4.md) (`PAGE` → `.text`)
  - `0x00ADD596` → [PnpGetLogString](../../text/4C/PnpGetLogString_function_004C26F4.md) (`PAGE` → `.text`)
  - `0x00ADD5A2` → [PnpGetLogString](../../text/4C/PnpGetLogString_function_004C26F4.md) (`PAGE` → `.text`)
  - `0x00ADD5AD` → [PnpGetLogString](../../text/4C/PnpGetLogString_function_004C26F4.md) (`PAGE` → `.text`)
  - `0x00ADD5B8` → [PnpGetLogString](../../text/4C/PnpGetLogString_function_004C26F4.md) (`PAGE` → `.text`)
  - `0x00ADD5C3` → [PnpGetLogString](../../text/4C/PnpGetLogString_function_004C26F4.md) (`PAGE` → `.text`)
  - `0x00ADD639` → [McTemplateK0zzjzzztzdzztdzz_EtwWriteTransfer](../../text/42/McTemplateK0zzjzzztzdzztdzz_EtwWriteTransfer_function_00424C50.md) (`PAGE` → `.text`)
  - `0x00ADD6BD` → [PnpGetLogString](../../text/4C/PnpGetLogString_function_004C26F4.md) (`PAGE` → `.text`)
  - `0x00ADD6C9` → [PnpGetLogString](../../text/4C/PnpGetLogString_function_004C26F4.md) (`PAGE` → `.text`)
  - `0x00ADD6D4` → [PnpGetLogString](../../text/4C/PnpGetLogString_function_004C26F4.md) (`PAGE` → `.text`)
  - `0x00ADD6DF` → [PnpGetLogString](../../text/4C/PnpGetLogString_function_004C26F4.md) (`PAGE` → `.text`)
  - `0x00ADD6EA` → [PnpGetLogString](../../text/4C/PnpGetLogString_function_004C26F4.md) (`PAGE` → `.text`)
  - `0x00ADD75C` → [McTemplateK0zzjzzztzdzztdzz_EtwWriteTransfer](../../text/42/McTemplateK0zzjzzztzdzztdzz_EtwWriteTransfer_function_00424C50.md) (`PAGE` → `.text`)
  - `0x00ADD7E2` → [PnpGetLogString](../../text/4C/PnpGetLogString_function_004C26F4.md) (`PAGE` → `.text`)
  - `0x00ADD7EE` → [PnpGetLogString](../../text/4C/PnpGetLogString_function_004C26F4.md) (`PAGE` → `.text`)
  - `0x00ADD7F9` → [PnpGetLogString](../../text/4C/PnpGetLogString_function_004C26F4.md) (`PAGE` → `.text`)
  - `0x00ADD804` → [PnpGetLogString](../../text/4C/PnpGetLogString_function_004C26F4.md) (`PAGE` → `.text`)
  - `0x00ADD80F` → [PnpGetLogString](../../text/4C/PnpGetLogString_function_004C26F4.md) (`PAGE` → `.text`)
  - `0x00ADD8C2` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00ADD8DC` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00ADD965` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00ADDA6D` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00ADDA97` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00ADDAAA` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00ADDB25` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00ADDB3B` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00ADDBB7` → [RtlUnicodeStringPrintfEx](../../text/4A/RtlUnicodeStringPrintfEx_function_004A8FD0.md) (`PAGE` → `.text`)
  - `0x00ADDC99` → [PnpDuplicateUnicodeString](../../text/4C/PnpDuplicateUnicodeString_function_004CC044.md) (`PAGE` → `.text`)
  - `0x00ADDD05` → [PnpDuplicateUnicodeString](../../text/4C/PnpDuplicateUnicodeString_function_004CC044.md) (`PAGE` → `.text`)
  - `0x00ADDD71` → [PnpDuplicateUnicodeString](../../text/4C/PnpDuplicateUnicodeString_function_004CC044.md) (`PAGE` → `.text`)
  - `0x00ADDDE4` → [PnpDuplicateUnicodeString](../../text/4C/PnpDuplicateUnicodeString_function_004CC044.md) (`PAGE` → `.text`)
  - `0x00ADDE48` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00ADDEE0` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00ADDF60` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00ADE105` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00ADCDD4  40 55                           push rbp
00ADCDD6  53                              push rbx
00ADCDD7  56                              push rsi
00ADCDD8  57                              push rdi
00ADCDD9  41 54                           push r12
00ADCDDB  41 55                           push r13
00ADCDDD  41 56                           push r14
00ADCDDF  41 57                           push r15
00ADCDE1  48 8D AC 24 48 FE FF FF         lea rbp, [rsp - 0x1b8]
00ADCDE9  48 81 EC 18 03 00 00            sub rsp, 0x318
00ADCDF0  48 8B 05 49 D9 32 00            mov rax, qword ptr [rip + 0x32d949]
00ADCDF7  48 33 C4                        xor rax, rsp
00ADCDFA  48 89 85 A8 01 00 00            mov qword ptr [rbp + 0x1a8], rax
00ADCE01  48 8B 85 30 02 00 00            mov rax, qword ptr [rbp + 0x230]
00ADCE08  33 F6                           xor esi, esi
00ADCE0A  0F 57 C0                        xorps xmm0, xmm0
00ADCE0D  48 89 85 88 00 00 00            mov qword ptr [rbp + 0x88], rax
00ADCE14  8A 05 10 33 41 00               mov al, byte ptr [rip + 0x413310]
00ADCE1A  0F 57 C9                        xorps xmm1, xmm1
00ADCE1D  24 30                           and al, 0x30
00ADCE1F  44 89 4D A4                     mov dword ptr [rbp - 0x5c], r9d
00ADCE23  48 89 55 C0                     mov qword ptr [rbp - 0x40], rdx
00ADCE27  44 8D 6E 01                     lea r13d, [rsi + 1]
00ADCE2B  48 89 4D E8                     mov qword ptr [rbp - 0x18], rcx
00ADCE2F  41 8B DD                        mov ebx, r13d
00ADCE32  89 5D 84                        mov dword ptr [rbp - 0x7c], ebx
00ADCE35  45 8B E1                        mov r12d, r9d
00ADCE38  48 89 75 10                     mov qword ptr [rbp + 0x10], rsi
00ADCE3C  49 8B F8                        mov rdi, r8
00ADCE3F  48 89 75 18                     mov qword ptr [rbp + 0x18], rsi
00ADCE43  4C 8B F2                        mov r14, rdx
00ADCE46  48 89 75 C8                     mov qword ptr [rbp - 0x38], rsi
00ADCE4A  44 8B FE                        mov r15d, esi
00ADCE4D  48 89 75 D0                     mov qword ptr [rbp - 0x30], rsi
00ADCE51  48 89 75 70                     mov qword ptr [rbp + 0x70], rsi
00ADCE55  48 89 75 78                     mov qword ptr [rbp + 0x78], rsi
00ADCE59  40 88 75 80                     mov byte ptr [rbp - 0x80], sil
00ADCE5D  48 89 75 20                     mov qword ptr [rbp + 0x20], rsi
00ADCE61  48 89 75 28                     mov qword ptr [rbp + 0x28], rsi
00ADCE65  48 89 75 30                     mov qword ptr [rbp + 0x30], rsi
00ADCE69  48 89 75 38                     mov qword ptr [rbp + 0x38], rsi
00ADCE6D  48 89 75 40                     mov qword ptr [rbp + 0x40], rsi
00ADCE71  48 89 75 48                     mov qword ptr [rbp + 0x48], rsi
00ADCE75  48 89 75 D8                     mov qword ptr [rbp - 0x28], rsi
00ADCE79  48 89 75 E0                     mov qword ptr [rbp - 0x20], rsi
00ADCE7D  48 89 75 50                     mov qword ptr [rbp + 0x50], rsi
00ADCE81  48 89 75 58                     mov qword ptr [rbp + 0x58], rsi
00ADCE85  48 89 75 B0                     mov qword ptr [rbp - 0x50], rsi
00ADCE89  48 89 75 B8                     mov qword ptr [rbp - 0x48], rsi
00ADCE8D  48 89 75 60                     mov qword ptr [rbp + 0x60], rsi
00ADCE91  48 89 75 68                     mov qword ptr [rbp + 0x68], rsi
00ADCE95  89 75 A0                        mov dword ptr [rbp - 0x60], esi
00ADCE98  48 89 75 00                     mov qword ptr [rbp], rsi
00ADCE9C  48 89 75 08                     mov qword ptr [rbp + 8], rsi
00ADCEA0  0F 11 45 90                     movups xmmword ptr [rbp - 0x70], xmm0
00ADCEA4  0F 11 85 90 00 00 00            movups xmmword ptr [rbp + 0x90], xmm0
00ADCEAB  0F 11 8D B0 00 00 00            movups xmmword ptr [rbp + 0xb0], xmm1
00ADCEB2  0F 11 45 F0                     movups xmmword ptr [rbp - 0x10], xmm0
00ADCEB6  0F 11 8D A0 00 00 00            movups xmmword ptr [rbp + 0xa0], xmm1
00ADCEBD  3C 30                           cmp al, 0x30
00ADCEBF  0F 85 DC 11 00 00               jne 0x140ade0a1
00ADCEC5  4D 85 C0                        test r8, r8
00ADCEC8  0F 84 D5 03 00 00               je 0x140add2a3
00ADCECE  33 D2                           xor edx, edx
00ADCED0  48 8D 8D C0 00 00 00            lea rcx, [rbp + 0xc0]
00ADCED7  41 B8 A0 00 00 00               mov r8d, 0xa0
00ADCEDD  E8 5E 9D BE FF                  call 0x1406c6c40
00ADCEE2  4C 8B 4F 10                     mov r9, qword ptr [rdi + 0x10]
00ADCEE6  8D 56 06                        lea edx, [rsi + 6]
00ADCEE9  8D 4E 12                        lea ecx, [rsi + 0x12]
00ADCEEC  89 95 DC 00 00 00               mov dword ptr [rbp + 0xdc], edx
00ADCEF2  48 8D 05 1F 5E 54 FF            lea rax, [rip - 0xaba1e1]
00ADCEF9  89 95 04 01 00 00               mov dword ptr [rbp + 0x104], edx
00ADCEFF  48 89 85 C0 00 00 00            mov qword ptr [rbp + 0xc0], rax
00ADCF06  44 8D 46 08                     lea r8d, [rsi + 8]
00ADCF0A  48 8D 45 10                     lea rax, [rbp + 0x10]
00ADCF0E  89 95 2C 01 00 00               mov dword ptr [rbp + 0x12c], edx
00ADCF14  48 8B 57 40                     mov rdx, qword ptr [rdi + 0x40]
00ADCF18  48 89 85 D0 00 00 00            mov qword ptr [rbp + 0xd0], rax
00ADCF1F  48 8D 05 BA 66 54 FF            lea rax, [rip - 0xab9946]
00ADCF26  48 89 85 E8 00 00 00            mov qword ptr [rbp + 0xe8], rax
00ADCF2D  48 8D 45 C8                     lea rax, [rbp - 0x38]
00ADCF31  48 89 85 F8 00 00 00            mov qword ptr [rbp + 0xf8], rax
00ADCF38  48 8D 05 01 5D 54 FF            lea rax, [rip - 0xaba2ff]
00ADCF3F  48 89 85 10 01 00 00            mov qword ptr [rbp + 0x110], rax
00ADCF46  48 8D 45 70                     lea rax, [rbp + 0x70]
00ADCF4A  48 89 85 20 01 00 00            mov qword ptr [rbp + 0x120], rax
00ADCF51  48 8D 05 F8 49 54 FF            lea rax, [rip - 0xabb608]
00ADCF58  48 89 85 38 01 00 00            mov qword ptr [rbp + 0x138], rax
00ADCF5F  48 8D 45 80                     lea rax, [rbp - 0x80]
00ADCF63  48 89 85 48 01 00 00            mov qword ptr [rbp + 0x148], rax
00ADCF6A  48 8D 85 C0 00 00 00            lea rax, [rbp + 0xc0]
00ADCF71  C7 44 24 28 04 00 00 00         mov dword ptr [rsp + 0x28], 4
00ADCF79  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00ADCF7E  89 8D C8 00 00 00               mov dword ptr [rbp + 0xc8], ecx
00ADCF84  C7 85 F0 00 00 00 12 20 00 00   mov dword ptr [rbp + 0xf0], 0x2012
00ADCF8E  89 8D 18 01 00 00               mov dword ptr [rbp + 0x118], ecx
00ADCF94  C7 85 40 01 00 00 11 00 00 00   mov dword ptr [rbp + 0x140], 0x11
00ADCF9E  44 89 AD 50 01 00 00            mov dword ptr [rbp + 0x150], r13d
00ADCFA5  E8 C2 A7 E9 FF                  call 0x14097776c
00ADCFAA  85 C0                           test eax, eax
00ADCFAC  0F 88 EF 10 00 00               js 0x140ade0a1
00ADCFB2  39 B5 E0 00 00 00               cmp dword ptr [rbp + 0xe0], esi
00ADCFB8  7D 0B                           jge 0x140adcfc5
00ADCFBA  33 D2                           xor edx, edx
00ADCFBC  48 8D 4D 10                     lea rcx, [rbp + 0x10]
00ADCFC0  E8 BB D7 94 FF                  call 0x14042a780
00ADCFC5  39 B5 08 01 00 00               cmp dword ptr [rbp + 0x108], esi
00ADCFCB  7D 0B                           jge 0x140adcfd8
00ADCFCD  33 D2                           xor edx, edx
00ADCFCF  48 8D 4D C8                     lea rcx, [rbp - 0x38]
00ADCFD3  E8 A8 D7 94 FF                  call 0x14042a780
00ADCFD8  4C 8B 45 D0                     mov r8, qword ptr [rbp - 0x30]
00ADCFDC  4D 85 C0                        test r8, r8
00ADCFDF  74 5F                           je 0x140add040
00ADCFE1  0F B7 4D C8                     movzx ecx, word ptr [rbp - 0x38]
00ADCFE5  B8 04 00 00 00                  mov eax, 4
00ADCFEA  66 3B C8                        cmp cx, ax
00ADCFED  76 51                           jbe 0x140add040
00ADCFEF  8B C1                           mov eax, ecx
00ADCFF1  41 BA 02 00 00 00               mov r10d, 2
00ADCFF7  48 D1 E8                        shr rax, 1
00ADCFFA  44 8B CE                        mov r9d, esi
00ADCFFD  49 3B C2                        cmp rax, r10
00ADD000  74 30                           je 0x140add032
00ADD002  48 8B D6                        mov rdx, rsi
00ADD005  66 41 39 34 50                  cmp word ptr [r8 + rdx*2], si
00ADD00A  75 0F                           jne 0x140add01b
00ADD00C  66 41 C7 04 50 3B 00            mov word ptr [r8 + rdx*2], 0x3b
00ADD013  4C 8B 45 D0                     mov r8, qword ptr [rbp - 0x30]
00ADD017  0F B7 4D C8                     movzx ecx, word ptr [rbp - 0x38]
00ADD01B  45 03 CD                        add r9d, r13d
00ADD01E  0F B7 C1                        movzx eax, cx
00ADD021  48 D1 E8                        shr rax, 1
00ADD024  49 2B C2                        sub rax, r10
00ADD027  41 8B D1                        mov edx, r9d
00ADD02A  48 3B D0                        cmp rdx, rax
00ADD02D  72 D6                           jb 0x140add005
00ADD02F  44 8B FE                        mov r15d, esi
00ADD032  B8 FE FF 00 00                  mov eax, 0xfffe
00ADD037  66 03 C8                        add cx, ax
00ADD03A  66 89 4D C8                     mov word ptr [rbp - 0x38], cx
00ADD03E  EB 14                           jmp 0x140add054
00ADD040  48 8D 4D C8                     lea rcx, [rbp - 0x38]
00ADD044  E8 B7 37 EE FF                  call 0x1409c0800
00ADD049  33 D2                           xor edx, edx
00ADD04B  48 8D 4D C8                     lea rcx, [rbp - 0x38]
00ADD04F  E8 2C D7 94 FF                  call 0x14042a780
00ADD054  39 B5 30 01 00 00               cmp dword ptr [rbp + 0x130], esi
00ADD05A  7D 0B                           jge 0x140add067
00ADD05C  33 D2                           xor edx, edx
00ADD05E  48 8D 4D 70                     lea rcx, [rbp + 0x70]
00ADD062  E8 19 D7 94 FF                  call 0x14042a780
00ADD067  39 B5 58 01 00 00               cmp dword ptr [rbp + 0x158], esi
00ADD06D  7D 04                           jge 0x140add073
00ADD06F  40 88 75 80                     mov byte ptr [rbp - 0x80], sil
00ADD073  48 39 75 18                     cmp qword ptr [rbp + 0x18], rsi
00ADD077  74 19                           je 0x140add092
00ADD079  48 8D 4F 28                     lea rcx, [rdi + 0x28]
00ADD07D  45 8A C5                        mov r8b, r13b
00ADD080  48 8D 55 10                     lea rdx, [rbp + 0x10]
00ADD084  E8 97 59 E5 FF                  call 0x140932a20
00ADD089  F6 D8                           neg al
00ADD08B  1B C9                           sbb ecx, ecx
00ADD08D  23 CB                           and ecx, ebx
00ADD08F  89 4D 84                        mov dword ptr [rbp - 0x7c], ecx
00ADD092  48 8D 4F 70                     lea rcx, [rdi + 0x70]
00ADD096  48 8D 55 90                     lea rdx, [rbp - 0x70]
00ADD09A  E8 51 10 95 FF                  call 0x14042e0f0
00ADD09F  0F BF 45 90                     movsx eax, word ptr [rbp - 0x70]
00ADD0A3  4C 8D 05 76 19 02 00            lea r8, [rip + 0x21976]
00ADD0AA  0F BF 4D 94                     movsx ecx, word ptr [rbp - 0x6c]
00ADD0AE  BA 0B 00 00 00                  mov edx, 0xb
00ADD0B3  44 0F BF 4D 92                  movsx r9d, word ptr [rbp - 0x6e]
00ADD0B8  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
00ADD0BC  89 4C 24 20                     mov dword ptr [rsp + 0x20], ecx
00ADD0C0  48 8D 8D 60 01 00 00            lea rcx, [rbp + 0x160]
00ADD0C7  E8 90 5C 9A FF                  call 0x140482d5c
00ADD0CC  85 C0                           test eax, eax
00ADD0CE  79 07                           jns 0x140add0d7
00ADD0D0  66 89 B5 60 01 00 00            mov word ptr [rbp + 0x160], si
00ADD0D7  0F B7 4F 78                     movzx ecx, word ptr [rdi + 0x78]
00ADD0DB  0F B7 57 7A                     movzx edx, word ptr [rdi + 0x7a]
00ADD0DF  44 0F B7 47 7C                  movzx r8d, word ptr [rdi + 0x7c]
00ADD0E4  8B 47 7C                        mov eax, dword ptr [rdi + 0x7c]
00ADD0E7  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
00ADD0EB  48 8D 8D 78 01 00 00            lea rcx, [rbp + 0x178]
00ADD0F2  89 54 24 28                     mov dword ptr [rsp + 0x28], edx
00ADD0F6  BA 18 00 00 00                  mov edx, 0x18
00ADD0FB  48 C1 E8 10                     shr rax, 0x10
00ADD0FF  44 89 44 24 20                  mov dword ptr [rsp + 0x20], r8d
00ADD104  4C 8D 05 A5 17 02 00            lea r8, [rip + 0x217a5]
00ADD10B  44 0F B7 C8                     movzx r9d, ax
00ADD10F  E8 48 5C 9A FF                  call 0x140482d5c
00ADD114  85 C0                           test eax, eax
00ADD116  79 07                           jns 0x140add11f
00ADD118  66 89 B5 78 01 00 00            mov word ptr [rbp + 0x178], si
00ADD11F  44 8B 6F 6C                     mov r13d, dword ptr [rdi + 0x6c]
00ADD123  41 83 FD FF                     cmp r13d, -1
00ADD127  44 0F 44 EE                     cmove r13d, esi
00ADD12B  E8 14 A8 A1 FF                  call 0x1404f7944
00ADD130  85 C0                           test eax, eax
00ADD132  0F 85 7F 01 00 00               jne 0x140add2b7
00ADD138  48 8D B7 E0 00 00 00            lea rsi, [rdi + 0xe0]
00ADD13F  48 8B 16                        mov rdx, qword ptr [rsi]
00ADD142  48 3B D6                        cmp rdx, rsi
00ADD145  0F 84 54 01 00 00               je 0x140add29f
00ADD14B  33 DB                           xor ebx, ebx
00ADD14D  44 8B C3                        mov r8d, ebx
00ADD150  0F B7 4A 48                     movzx ecx, word ptr [rdx + 0x48]
00ADD154  0F B7 42 28                     movzx eax, word ptr [rdx + 0x28]
00ADD158  41 03 C0                        add eax, r8d
00ADD15B  44 8D 41 16                     lea r8d, [rcx + 0x16]
00ADD15F  48 8B 8A B0 00 00 00            mov rcx, qword ptr [rdx + 0xb0]
00ADD166  44 03 C0                        add r8d, eax
00ADD169  48 85 C9                        test rcx, rcx
00ADD16C  74 17                           je 0x140add185
00ADD16E  48 83 C8 FF                     or rax, 0xffffffffffffffff
00ADD172  48 FF C0                        inc rax
00ADD175  66 39 1C 41                     cmp word ptr [rcx + rax*2], bx
00ADD179  75 F7                           jne 0x140add172
00ADD17B  45 8D 04 40                     lea r8d, [r8 + rax*2]
00ADD17F  41 83 C0 02                     add r8d, 2
00ADD183  EB 0C                           jmp 0x140add191
00ADD185  39 9A C0 01 00 00               cmp dword ptr [rdx + 0x1c0], ebx
00ADD18B  7D 04                           jge 0x140add191
00ADD18D  41 83 C0 16                     add r8d, 0x16
00ADD191  48 8B 12                        mov rdx, qword ptr [rdx]
00ADD194  48 3B D6                        cmp rdx, rsi
00ADD197  75 B7                           jne 0x140add150
00ADD199  41 8D 40 02                     lea eax, [r8 + 2]
00ADD19D  B9 FE FF 00 00                  mov ecx, 0xfffe
00ADD1A2  3B C1                           cmp eax, ecx
00ADD1A4  76 09                           jbe 0x140add1af
00ADD1A6  0F B7 C1                        movzx eax, cx
00ADD1A9  66 89 4D B2                     mov word ptr [rbp - 0x4e], cx
00ADD1AD  EB 04                           jmp 0x140add1b3
00ADD1AF  66 89 45 B2                     mov word ptr [rbp - 0x4e], ax
00ADD1B3  0F B7 D0                        movzx edx, ax
00ADD1B6  B9 00 01 00 00                  mov ecx, 0x100
00ADD1BB  41 B8 53 74 72 67               mov r8d, 0x67727453
00ADD1C1  E8 2A 4F 0A 00                  call 0x140b820f0
00ADD1C6  48 89 45 B8                     mov qword ptr [rbp - 0x48], rax
00ADD1CA  48 85 C0                        test rax, rax
00ADD1CD  0F 84 CE 0E 00 00               je 0x140ade0a1
00ADD1D3  0F 28 45 B0                     movaps xmm0, xmmword ptr [rbp - 0x50]
00ADD1D7  66 89 18                        mov word ptr [rax], bx
00ADD1DA  48 8B 1E                        mov rbx, qword ptr [rsi]
00ADD1DD  66 0F 7F 45 90                  movdqa xmmword ptr [rbp - 0x70], xmm0
00ADD1E2  48 3B DE                        cmp rbx, rsi
00ADD1E5  0F 84 B4 00 00 00               je 0x140add29f
00ADD1EB  48 3B 1E                        cmp rbx, qword ptr [rsi]
00ADD1EE  74 22                           je 0x140add212
00ADD1F0  41 B9 00 08 00 00               mov r9d, 0x800
00ADD1F6  4C 8D 45 90                     lea r8, [rbp - 0x70]
00ADD1FA  48 8D 15 2F F8 01 00            lea rdx, [rip + 0x1f82f]
00ADD201  48 8D 4D 90                     lea rcx, [rbp - 0x70]
00ADD205  E8 B6 7D AC FF                  call 0x1405a4fc0
00ADD20A  85 C0                           test eax, eax
00ADD20C  0F 88 89 00 00 00               js 0x140add29b
00ADD212  8B 43 6C                        mov eax, dword ptr [rbx + 0x6c]
00ADD215  48 8D 4B 48                     lea rcx, [rbx + 0x48]
00ADD219  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00ADD21D  48 8D 53 28                     lea rdx, [rbx + 0x28]
00ADD221  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
00ADD226  4C 8D 0D A3 16 02 00            lea r9, [rip + 0x216a3]
00ADD22D  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00ADD232  48 8D 4D 90                     lea rcx, [rbp - 0x70]
00ADD236  48 8D 55 90                     lea rdx, [rbp - 0x70]
00ADD23A  41 B8 00 08 00 00               mov r8d, 0x800
00ADD240  E8 8B BD 9C FF                  call 0x1404a8fd0
00ADD245  85 C0                           test eax, eax
00ADD247  78 52                           js 0x140add29b
00ADD249  48 8B 83 B0 00 00 00            mov rax, qword ptr [rbx + 0xb0]
00ADD250  48 85 C0                        test rax, rax
00ADD253  74 0E                           je 0x140add263
00ADD255  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00ADD25A  4C 8D 0D 8F 16 02 00            lea r9, [rip + 0x2168f]
00ADD261  EB 15                           jmp 0x140add278
00ADD263  8B 83 C0 01 00 00               mov eax, dword ptr [rbx + 0x1c0]
00ADD269  85 C0                           test eax, eax
00ADD26B  79 22                           jns 0x140add28f
00ADD26D  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00ADD271  4C 8D 0D 88 16 02 00            lea r9, [rip + 0x21688]
00ADD278  41 B8 00 08 00 00               mov r8d, 0x800
00ADD27E  48 8D 55 90                     lea rdx, [rbp - 0x70]
00ADD282  48 8D 4D 90                     lea rcx, [rbp - 0x70]
00ADD286  E8 45 BD 9C FF                  call 0x1404a8fd0
00ADD28B  85 C0                           test eax, eax
00ADD28D  78 0C                           js 0x140add29b
00ADD28F  48 8B 1B                        mov rbx, qword ptr [rbx]
00ADD292  48 3B DE                        cmp rbx, rsi
00ADD295  0F 85 50 FF FF FF               jne 0x140add1eb
00ADD29B  44 8B 65 A4                     mov r12d, dword ptr [rbp - 0x5c]
00ADD29F  33 F6                           xor esi, esi
00ADD2A1  EB 14                           jmp 0x140add2b7
00ADD2A3  66 89 B5 60 01 00 00            mov word ptr [rbp + 0x160], si
00ADD2AA  44 8B EE                        mov r13d, esi
00ADD2AD  66 89 B5 78 01 00 00            mov word ptr [rbp + 0x178], si
00ADD2B4  89 75 84                        mov dword ptr [rbp - 0x7c], esi
00ADD2B7  E8 88 A6 A1 FF                  call 0x1404f7944
00ADD2BC  85 C0                           test eax, eax
00ADD2BE  0F 84 6A 01 00 00               je 0x140add42e
00ADD2C4  4D 8D 4E 18                     lea r9, [r14 + 0x18]
00ADD2C8  49 8B 11                        mov rdx, qword ptr [r9]
00ADD2CB  49 3B D1                        cmp rdx, r9
00ADD2CE  0F 84 5A 01 00 00               je 0x140add42e
00ADD2D4  44 8B C6                        mov r8d, esi
00ADD2D7  0F B7 4A 48                     movzx ecx, word ptr [rdx + 0x48]
00ADD2DB  0F B7 42 28                     movzx eax, word ptr [rdx + 0x28]
00ADD2DF  41 03 C0                        add eax, r8d
00ADD2E2  44 8D 41 16                     lea r8d, [rcx + 0x16]
00ADD2E6  48 8B 8A B0 00 00 00            mov rcx, qword ptr [rdx + 0xb0]
00ADD2ED  44 03 C0                        add r8d, eax
00ADD2F0  48 85 C9                        test rcx, rcx
00ADD2F3  74 17                           je 0x140add30c
00ADD2F5  48 83 C8 FF                     or rax, 0xffffffffffffffff
00ADD2F9  48 FF C0                        inc rax
00ADD2FC  66 39 34 41                     cmp word ptr [rcx + rax*2], si
00ADD300  75 F7                           jne 0x140add2f9
00ADD302  45 8D 04 40                     lea r8d, [r8 + rax*2]
00ADD306  41 83 C0 02                     add r8d, 2
00ADD30A  EB 0C                           jmp 0x140add318
00ADD30C  39 B2 C0 01 00 00               cmp dword ptr [rdx + 0x1c0], esi
00ADD312  7D 04                           jge 0x140add318
00ADD314  41 83 C0 16                     add r8d, 0x16
00ADD318  48 8B 12                        mov rdx, qword ptr [rdx]
00ADD31B  49 3B D1                        cmp rdx, r9
00ADD31E  75 B7                           jne 0x140add2d7
00ADD320  41 8D 40 02                     lea eax, [r8 + 2]
00ADD324  B9 FE FF 00 00                  mov ecx, 0xfffe
00ADD329  3B C1                           cmp eax, ecx
00ADD32B  76 09                           jbe 0x140add336
00ADD32D  0F B7 C1                        movzx eax, cx
00ADD330  66 89 4D B2                     mov word ptr [rbp - 0x4e], cx
00ADD334  EB 04                           jmp 0x140add33a
00ADD336  66 89 45 B2                     mov word ptr [rbp - 0x4e], ax
00ADD33A  0F B7 D0                        movzx edx, ax
00ADD33D  B9 00 01 00 00                  mov ecx, 0x100
00ADD342  41 B8 53 74 72 67               mov r8d, 0x67727453
00ADD348  E8 A3 4D 0A 00                  call 0x140b820f0
00ADD34D  48 89 45 B8                     mov qword ptr [rbp - 0x48], rax
00ADD351  48 85 C0                        test rax, rax
00ADD354  0F 84 47 0D 00 00               je 0x140ade0a1
00ADD35A  0F 28 45 B0                     movaps xmm0, xmmword ptr [rbp - 0x50]
00ADD35E  66 89 30                        mov word ptr [rax], si
00ADD361  49 8D 76 18                     lea rsi, [r14 + 0x18]
00ADD365  49 8B 5E 18                     mov rbx, qword ptr [r14 + 0x18]
00ADD369  66 0F 7F 45 90                  movdqa xmmword ptr [rbp - 0x70], xmm0
00ADD36E  48 3B DE                        cmp rbx, rsi
00ADD371  0F 84 B5 00 00 00               je 0x140add42c
00ADD377  49 3B 5E 18                     cmp rbx, qword ptr [r14 + 0x18]
00ADD37B  74 22                           je 0x140add39f
00ADD37D  41 B9 00 08 00 00               mov r9d, 0x800
00ADD383  4C 8D 45 90                     lea r8, [rbp - 0x70]
00ADD387  48 8D 15 A2 F6 01 00            lea rdx, [rip + 0x1f6a2]
00ADD38E  48 8D 4D 90                     lea rcx, [rbp - 0x70]
00ADD392  E8 29 7C AC FF                  call 0x1405a4fc0
00ADD397  85 C0                           test eax, eax
00ADD399  0F 88 89 00 00 00               js 0x140add428
00ADD39F  8B 43 6C                        mov eax, dword ptr [rbx + 0x6c]
00ADD3A2  48 8D 4B 48                     lea rcx, [rbx + 0x48]
00ADD3A6  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00ADD3AA  48 8D 53 28                     lea rdx, [rbx + 0x28]
00ADD3AE  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
00ADD3B3  4C 8D 0D 16 15 02 00            lea r9, [rip + 0x21516]
00ADD3BA  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00ADD3BF  48 8D 4D 90                     lea rcx, [rbp - 0x70]
00ADD3C3  48 8D 55 90                     lea rdx, [rbp - 0x70]
00ADD3C7  41 B8 00 08 00 00               mov r8d, 0x800
00ADD3CD  E8 FE BB 9C FF                  call 0x1404a8fd0
00ADD3D2  85 C0                           test eax, eax
00ADD3D4  78 52                           js 0x140add428
00ADD3D6  48 8B 83 B0 00 00 00            mov rax, qword ptr [rbx + 0xb0]
00ADD3DD  48 85 C0                        test rax, rax
00ADD3E0  74 0E                           je 0x140add3f0
00ADD3E2  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00ADD3E7  4C 8D 0D 02 15 02 00            lea r9, [rip + 0x21502]
00ADD3EE  EB 15                           jmp 0x140add405
00ADD3F0  8B 83 C0 01 00 00               mov eax, dword ptr [rbx + 0x1c0]
00ADD3F6  85 C0                           test eax, eax
00ADD3F8  79 22                           jns 0x140add41c
00ADD3FA  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00ADD3FE  4C 8D 0D FB 14 02 00            lea r9, [rip + 0x214fb]
00ADD405  41 B8 00 08 00 00               mov r8d, 0x800
00ADD40B  48 8D 55 90                     lea rdx, [rbp - 0x70]
00ADD40F  48 8D 4D 90                     lea rcx, [rbp - 0x70]
00ADD413  E8 B8 BB 9C FF                  call 0x1404a8fd0
00ADD418  85 C0                           test eax, eax
00ADD41A  78 0C                           js 0x140add428
00ADD41C  48 8B 1B                        mov rbx, qword ptr [rbx]
00ADD41F  48 3B DE                        cmp rbx, rsi
00ADD422  0F 85 4F FF FF FF               jne 0x140add377
00ADD428  44 8B 65 A4                     mov r12d, dword ptr [rbp - 0x5c]
00ADD42C  33 F6                           xor esi, esi
00ADD42E  8B 85 20 02 00 00               mov eax, dword ptr [rbp + 0x220]
00ADD434  85 C0                           test eax, eax
00ADD436  0F 88 07 02 00 00               js 0x140add643
00ADD43C  41 F6 C4 70                     test r12b, 0x70
00ADD440  0F 85 E1 00 00 00               jne 0x140add527
00ADD446  F6 05 DD 2C 41 00 10            test byte ptr [rip + 0x412cdd], 0x10
00ADD44D  0F 84 01 04 00 00               je 0x140add854
00ADD453  41 8B DC                        mov ebx, r12d
00ADD456  4C 8D 1D 5B 66 07 00            lea r11, [rip + 0x7665b]
00ADD45D  83 E3 01                        and ebx, 1
00ADD460  48 85 FF                        test rdi, rdi
00ADD463  74 10                           je 0x140add475
00ADD465  83 7F 6C FF                     cmp dword ptr [rdi + 0x6c], -1
00ADD469  4C 8B 77 40                     mov r14, qword ptr [rdi + 0x40]
00ADD46D  74 09                           je 0x140add478
00ADD46F  48 8D 57 48                     lea rdx, [rdi + 0x48]
00ADD473  EB 0B                           jmp 0x140add480
00ADD475  4D 8B F3                        mov r14, r11
00ADD478  48 8B D6                        mov rdx, rsi
00ADD47B  48 85 FF                        test rdi, rdi
00ADD47E  74 18                           je 0x140add498
00ADD480  4C 8B 5F 30                     mov r11, qword ptr [rdi + 0x30]
00ADD484  48 8D B7 F0 00 00 00            lea rsi, [rdi + 0xf0]
00ADD48B  4C 8D BF 10 01 00 00            lea r15, [rdi + 0x110]
00ADD492  4C 8D 67 58                     lea r12, [rdi + 0x58]
00ADD496  EB 11                           jmp 0x140add4a9
00ADD498  33 C0                           xor eax, eax
00ADD49A  48 8D 35 57 DB 06 00            lea rsi, [rip + 0x6db57]
00ADD4A1  44 8B F8                        mov r15d, eax
00ADD4A4  44 8B E0                        mov r12d, eax
00ADD4A7  8B D0                           mov edx, eax
00ADD4A9  48 8B 4D E8                     mov rcx, qword ptr [rbp - 0x18]
00ADD4AD  48 8B 49 10                     mov rcx, qword ptr [rcx + 0x10]
00ADD4B1  48 83 C1 28                     add rcx, 0x28
00ADD4B5  E8 3A 52 9E FF                  call 0x1404c26f4
00ADD4BA  48 8D 4D B0                     lea rcx, [rbp - 0x50]
00ADD4BE  4C 8B C8                        mov r9, rax
00ADD4C1  E8 2E 52 9E FF                  call 0x1404c26f4
00ADD4C6  48 8B CA                        mov rcx, rdx
00ADD4C9  4C 8B D0                        mov r10, rax
00ADD4CC  E8 23 52 9E FF                  call 0x1404c26f4
00ADD4D1  49 8B CC                        mov rcx, r12
00ADD4D4  4C 8B C0                        mov r8, rax
00ADD4D7  E8 18 52 9E FF                  call 0x1404c26f4
00ADD4DC  49 8B CF                        mov rcx, r15
00ADD4DF  48 8B D0                        mov rdx, rax
00ADD4E2  E8 0D 52 9E FF                  call 0x1404c26f4
00ADD4E7  4C 89 B4 24 88 00 00 00         mov qword ptr [rsp + 0x88], r14
00ADD4EF  44 8B B5 20 02 00 00            mov r14d, dword ptr [rbp + 0x220]
00ADD4F6  4C 89 8C 24 80 00 00 00         mov qword ptr [rsp + 0x80], r9
00ADD4FE  44 89 74 24 78                  mov dword ptr [rsp + 0x78], r14d
00ADD503  89 5C 24 70                     mov dword ptr [rsp + 0x70], ebx
00ADD507  4C 89 54 24 68                  mov qword ptr [rsp + 0x68], r10
00ADD50C  4C 89 44 24 60                  mov qword ptr [rsp + 0x60], r8
00ADD511  44 89 6C 24 58                  mov dword ptr [rsp + 0x58], r13d
00ADD516  48 89 54 24 50                  mov qword ptr [rsp + 0x50], rdx
00ADD51B  48 8D 15 0E 9E 54 FF            lea rdx, [rip - 0xab61f2]
00ADD522  E9 DC 00 00 00                  jmp 0x140add603
00ADD527  F6 05 FC 2B 41 00 40            test byte ptr [rip + 0x412bfc], 0x40
00ADD52E  0F 84 20 03 00 00               je 0x140add854
00ADD534  41 8B DC                        mov ebx, r12d
00ADD537  4C 8D 1D 7A 65 07 00            lea r11, [rip + 0x7657a]
00ADD53E  83 E3 01                        and ebx, 1
00ADD541  48 85 FF                        test rdi, rdi
00ADD544  74 10                           je 0x140add556
00ADD546  83 7F 6C FF                     cmp dword ptr [rdi + 0x6c], -1
00ADD54A  4C 8B 77 40                     mov r14, qword ptr [rdi + 0x40]
00ADD54E  74 09                           je 0x140add559
00ADD550  48 8D 57 48                     lea rdx, [rdi + 0x48]
00ADD554  EB 0B                           jmp 0x140add561
00ADD556  4D 8B F3                        mov r14, r11
00ADD559  48 8B D6                        mov rdx, rsi
00ADD55C  48 85 FF                        test rdi, rdi
00ADD55F  74 18                           je 0x140add579
00ADD561  4C 8B 5F 30                     mov r11, qword ptr [rdi + 0x30]
00ADD565  48 8D B7 F0 00 00 00            lea rsi, [rdi + 0xf0]
00ADD56C  4C 8D BF 10 01 00 00            lea r15, [rdi + 0x110]
00ADD573  4C 8D 67 58                     lea r12, [rdi + 0x58]
00ADD577  EB 11                           jmp 0x140add58a
00ADD579  33 C0                           xor eax, eax
00ADD57B  48 8D 35 76 DA 06 00            lea rsi, [rip + 0x6da76]
00ADD582  44 8B F8                        mov r15d, eax
00ADD585  44 8B E0                        mov r12d, eax
00ADD588  8B D0                           mov edx, eax
00ADD58A  48 8B 4D E8                     mov rcx, qword ptr [rbp - 0x18]
00ADD58E  48 8B 49 10                     mov rcx, qword ptr [rcx + 0x10]
00ADD592  48 83 C1 28                     add rcx, 0x28
00ADD596  E8 59 51 9E FF                  call 0x1404c26f4
00ADD59B  48 8D 4D B0                     lea rcx, [rbp - 0x50]
00ADD59F  4C 8B C8                        mov r9, rax
00ADD5A2  E8 4D 51 9E FF                  call 0x1404c26f4
00ADD5A7  48 8B CA                        mov rcx, rdx
00ADD5AA  4C 8B D0                        mov r10, rax
00ADD5AD  E8 42 51 9E FF                  call 0x1404c26f4
00ADD5B2  49 8B CC                        mov rcx, r12
00ADD5B5  4C 8B C0                        mov r8, rax
00ADD5B8  E8 37 51 9E FF                  call 0x1404c26f4
00ADD5BD  49 8B CF                        mov rcx, r15
00ADD5C0  48 8B D0                        mov rdx, rax
00ADD5C3  E8 2C 51 9E FF                  call 0x1404c26f4
00ADD5C8  4C 89 B4 24 88 00 00 00         mov qword ptr [rsp + 0x88], r14
00ADD5D0  44 8B B5 20 02 00 00            mov r14d, dword ptr [rbp + 0x220]
00ADD5D7  4C 89 8C 24 80 00 00 00         mov qword ptr [rsp + 0x80], r9
00ADD5DF  44 89 74 24 78                  mov dword ptr [rsp + 0x78], r14d
00ADD5E4  89 5C 24 70                     mov dword ptr [rsp + 0x70], ebx
00ADD5E8  4C 89 54 24 68                  mov qword ptr [rsp + 0x68], r10
00ADD5ED  4C 89 44 24 60                  mov qword ptr [rsp + 0x60], r8
00ADD5F2  44 89 6C 24 58                  mov dword ptr [rsp + 0x58], r13d
00ADD5F7  48 89 54 24 50                  mov qword ptr [rsp + 0x50], rdx
00ADD5FC  48 8D 15 7D 9B 54 FF            lea rdx, [rip - 0xab6483]
00ADD603  8B 4D 84                        mov ecx, dword ptr [rbp - 0x7c]
00ADD606  4C 8B 4D C0                     mov r9, qword ptr [rbp - 0x40]
00ADD60A  89 4C 24 48                     mov dword ptr [rsp + 0x48], ecx
00ADD60E  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00ADD613  48 8D 85 78 01 00 00            lea rax, [rbp + 0x178]
00ADD61A  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00ADD61F  48 8D 85 60 01 00 00            lea rax, [rbp + 0x160]
00ADD626  4D 8B 49 08                     mov r9, qword ptr [r9 + 8]
00ADD62A  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00ADD62F  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
00ADD634  4C 89 5C 24 20                  mov qword ptr [rsp + 0x20], r11
00ADD639  E8 12 76 94 FF                  call 0x140424c50
00ADD63E  E9 25 01 00 00                  jmp 0x140add768
00ADD643  3D 61 03 00 C0                  cmp eax, 0xc0000361
00ADD648  0F 85 25 01 00 00               jne 0x140add773
00ADD64E  F6 05 D5 2A 41 00 40            test byte ptr [rip + 0x412ad5], 0x40
00ADD655  0F 84 F9 01 00 00               je 0x140add854
00ADD65B  41 8B DC                        mov ebx, r12d
00ADD65E  4C 8D 1D 53 64 07 00            lea r11, [rip + 0x76453]
00ADD665  83 E3 01                        and ebx, 1
00ADD668  48 85 FF                        test rdi, rdi
00ADD66B  74 10                           je 0x140add67d
00ADD66D  83 7F 6C FF                     cmp dword ptr [rdi + 0x6c], -1
00ADD671  4C 8B 77 40                     mov r14, qword ptr [rdi + 0x40]
00ADD675  74 09                           je 0x140add680
00ADD677  48 8D 57 48                     lea rdx, [rdi + 0x48]
00ADD67B  EB 0B                           jmp 0x140add688
00ADD67D  4D 8B F3                        mov r14, r11
00ADD680  48 8B D6                        mov rdx, rsi
00ADD683  48 85 FF                        test rdi, rdi
00ADD686  74 18                           je 0x140add6a0
00ADD688  4C 8B 5F 30                     mov r11, qword ptr [rdi + 0x30]
00ADD68C  48 8D B7 F0 00 00 00            lea rsi, [rdi + 0xf0]
00ADD693  4C 8D BF 10 01 00 00            lea r15, [rdi + 0x110]
00ADD69A  4C 8D 67 58                     lea r12, [rdi + 0x58]
00ADD69E  EB 11                           jmp 0x140add6b1
00ADD6A0  33 C0                           xor eax, eax
00ADD6A2  48 8D 35 4F D9 06 00            lea rsi, [rip + 0x6d94f]
00ADD6A9  44 8B F8                        mov r15d, eax
00ADD6AC  44 8B E0                        mov r12d, eax
00ADD6AF  8B D0                           mov edx, eax
00ADD6B1  48 8B 4D E8                     mov rcx, qword ptr [rbp - 0x18]
00ADD6B5  48 8B 49 10                     mov rcx, qword ptr [rcx + 0x10]
00ADD6B9  48 83 C1 28                     add rcx, 0x28
00ADD6BD  E8 32 50 9E FF                  call 0x1404c26f4
00ADD6C2  48 8D 4D B0                     lea rcx, [rbp - 0x50]
00ADD6C6  4C 8B C8                        mov r9, rax
00ADD6C9  E8 26 50 9E FF                  call 0x1404c26f4
00ADD6CE  48 8B CA                        mov rcx, rdx
00ADD6D1  4C 8B D0                        mov r10, rax
00ADD6D4  E8 1B 50 9E FF                  call 0x1404c26f4
00ADD6D9  49 8B CC                        mov rcx, r12
00ADD6DC  4C 8B C0                        mov r8, rax
00ADD6DF  E8 10 50 9E FF                  call 0x1404c26f4
00ADD6E4  49 8B CF                        mov rcx, r15
00ADD6E7  48 8B D0                        mov rdx, rax
00ADD6EA  E8 05 50 9E FF                  call 0x1404c26f4
00ADD6EF  8B 4D 84                        mov ecx, dword ptr [rbp - 0x7c]
00ADD6F2  4C 89 B4 24 88 00 00 00         mov qword ptr [rsp + 0x88], r14
00ADD6FA  4C 89 8C 24 80 00 00 00         mov qword ptr [rsp + 0x80], r9
00ADD702  4C 8B 4D C0                     mov r9, qword ptr [rbp - 0x40]
00ADD706  C7 44 24 78 61 03 00 C0         mov dword ptr [rsp + 0x78], 0xc0000361
00ADD70E  89 5C 24 70                     mov dword ptr [rsp + 0x70], ebx
00ADD712  4C 89 54 24 68                  mov qword ptr [rsp + 0x68], r10
00ADD717  4D 8B 49 08                     mov r9, qword ptr [r9 + 8]
00ADD71B  4C 89 44 24 60                  mov qword ptr [rsp + 0x60], r8
00ADD720  44 89 6C 24 58                  mov dword ptr [rsp + 0x58], r13d
00ADD725  48 89 54 24 50                  mov qword ptr [rsp + 0x50], rdx
00ADD72A  48 8D 15 BF 96 54 FF            lea rdx, [rip - 0xab6941]
00ADD731  89 4C 24 48                     mov dword ptr [rsp + 0x48], ecx
00ADD735  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00ADD73A  48 8D 85 78 01 00 00            lea rax, [rbp + 0x178]
00ADD741  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00ADD746  48 8D 85 60 01 00 00            lea rax, [rbp + 0x160]
00ADD74D  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00ADD752  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
00ADD757  4C 89 5C 24 20                  mov qword ptr [rsp + 0x20], r11
00ADD75C  E8 EF 74 94 FF                  call 0x140424c50
00ADD761  44 8B B5 20 02 00 00            mov r14d, dword ptr [rbp + 0x220]
00ADD768  44 8B 7D A0                     mov r15d, dword ptr [rbp - 0x60]
00ADD76C  33 F6                           xor esi, esi
00ADD76E  E9 E4 00 00 00                  jmp 0x140add857
00ADD773  F6 05 B0 29 41 00 20            test byte ptr [rip + 0x4129b0], 0x20
00ADD77A  0F 84 D4 00 00 00               je 0x140add854
00ADD780  41 8B DC                        mov ebx, r12d
00ADD783  4C 8D 1D 2E 63 07 00            lea r11, [rip + 0x7632e]
00ADD78A  83 E3 01                        and ebx, 1
00ADD78D  48 85 FF                        test rdi, rdi
00ADD790  74 10                           je 0x140add7a2
00ADD792  83 7F 6C FF                     cmp dword ptr [rdi + 0x6c], -1
00ADD796  4C 8B 77 40                     mov r14, qword ptr [rdi + 0x40]
00ADD79A  74 09                           je 0x140add7a5
00ADD79C  48 8D 57 48                     lea rdx, [rdi + 0x48]
00ADD7A0  EB 0B                           jmp 0x140add7ad
00ADD7A2  4D 8B F3                        mov r14, r11
00ADD7A5  48 8B D6                        mov rdx, rsi
00ADD7A8  48 85 FF                        test rdi, rdi
00ADD7AB  74 18                           je 0x140add7c5
00ADD7AD  4C 8B 5F 30                     mov r11, qword ptr [rdi + 0x30]
00ADD7B1  48 8D B7 F0 00 00 00            lea rsi, [rdi + 0xf0]
00ADD7B8  4C 8D BF 10 01 00 00            lea r15, [rdi + 0x110]
00ADD7BF  4C 8D 67 58                     lea r12, [rdi + 0x58]
00ADD7C3  EB 11                           jmp 0x140add7d6
00ADD7C5  33 C0                           xor eax, eax
00ADD7C7  48 8D 35 2A D8 06 00            lea rsi, [rip + 0x6d82a]
00ADD7CE  44 8B F8                        mov r15d, eax
00ADD7D1  44 8B E0                        mov r12d, eax
00ADD7D4  8B D0                           mov edx, eax
00ADD7D6  48 8B 4D E8                     mov rcx, qword ptr [rbp - 0x18]
00ADD7DA  48 8B 49 10                     mov rcx, qword ptr [rcx + 0x10]
00ADD7DE  48 83 C1 28                     add rcx, 0x28
00ADD7E2  E8 0D 4F 9E FF                  call 0x1404c26f4
00ADD7E7  48 8D 4D B0                     lea rcx, [rbp - 0x50]
00ADD7EB  4C 8B C8                        mov r9, rax
00ADD7EE  E8 01 4F 9E FF                  call 0x1404c26f4
00ADD7F3  48 8B CA                        mov rcx, rdx
00ADD7F6  4C 8B D0                        mov r10, rax
00ADD7F9  E8 F6 4E 9E FF                  call 0x1404c26f4
00ADD7FE  49 8B CC                        mov rcx, r12
00ADD801  4C 8B C0                        mov r8, rax
00ADD804  E8 EB 4E 9E FF                  call 0x1404c26f4
00ADD809  49 8B CF                        mov rcx, r15
00ADD80C  48 8B D0                        mov rdx, rax
00ADD80F  E8 E0 4E 9E FF                  call 0x1404c26f4
00ADD814  4C 89 B4 24 88 00 00 00         mov qword ptr [rsp + 0x88], r14
00ADD81C  44 8B B5 20 02 00 00            mov r14d, dword ptr [rbp + 0x220]
00ADD823  4C 89 8C 24 80 00 00 00         mov qword ptr [rsp + 0x80], r9
00ADD82B  44 89 74 24 78                  mov dword ptr [rsp + 0x78], r14d
00ADD830  89 5C 24 70                     mov dword ptr [rsp + 0x70], ebx
00ADD834  4C 89 54 24 68                  mov qword ptr [rsp + 0x68], r10
00ADD839  4C 89 44 24 60                  mov qword ptr [rsp + 0x60], r8
00ADD83E  44 89 6C 24 58                  mov dword ptr [rsp + 0x58], r13d
00ADD843  48 89 54 24 50                  mov qword ptr [rsp + 0x50], rdx
00ADD848  48 8D 15 F1 99 54 FF            lea rdx, [rip - 0xab660f]
00ADD84F  E9 AF FD FF FF                  jmp 0x140add603
00ADD854  44 8B F0                        mov r14d, eax
00ADD857  48 85 FF                        test rdi, rdi
00ADD85A  0F 84 41 08 00 00               je 0x140ade0a1
00ADD860  4C 8B AD 28 02 00 00            mov r13, qword ptr [rbp + 0x228]
00ADD867  48 8D 8F D0 00 00 00            lea rcx, [rdi + 0xd0]
00ADD86E  48 8B 01                        mov rax, qword ptr [rcx]
00ADD871  48 3B C1                        cmp rax, rcx
00ADD874  0F 84 89 03 00 00               je 0x140addc03
00ADD87A  48 8B 00                        mov rax, qword ptr [rax]
00ADD87D  41 FF C7                        inc r15d
00ADD880  48 3B C1                        cmp rax, rcx
00ADD883  75 F5                           jne 0x140add87a
00ADD885  45 85 FF                        test r15d, r15d
00ADD888  0F 84 75 03 00 00               je 0x140addc03
00ADD88E  41 69 C7 6E 06 00 00            imul eax, r15d, 0x66e
00ADD895  BB FF 7F 00 00                  mov ebx, 0x7fff
00ADD89A  83 C0 02                        add eax, 2
00ADD89D  3B C3                           cmp eax, ebx
00ADD89F  76 06                           jbe 0x140add8a7
00ADD8A1  66 89 5D 02                     mov word ptr [rbp + 2], bx
00ADD8A5  EB 07                           jmp 0x140add8ae
00ADD8A7  0F B7 D8                        movzx ebx, ax
00ADD8AA  66 89 45 02                     mov word ptr [rbp + 2], ax
00ADD8AE  66 89 75 00                     mov word ptr [rbp], si
00ADD8B2  41 B8 53 74 72 67               mov r8d, 0x67727453
00ADD8B8  0F B7 F3                        movzx esi, bx
00ADD8BB  B9 00 01 00 00                  mov ecx, 0x100
00ADD8C0  8B D6                           mov edx, esi
00ADD8C2  E8 29 48 0A 00                  call 0x140b820f0
00ADD8C7  48 89 45 08                     mov qword ptr [rbp + 8], rax
00ADD8CB  48 85 C0                        test rax, rax
00ADD8CE  0F 84 CD 07 00 00               je 0x140ade0a1
00ADD8D4  44 8B C6                        mov r8d, esi
00ADD8D7  33 D2                           xor edx, edx
00ADD8D9  48 8B C8                        mov rcx, rax
00ADD8DC  E8 5F 93 BE FF                  call 0x1406c6c40
00ADD8E1  48 8B B7 D0 00 00 00            mov rsi, qword ptr [rdi + 0xd0]
00ADD8E8  4C 8D A7 D0 00 00 00            lea r12, [rdi + 0xd0]
00ADD8EF  B8 FE FF 00 00                  mov eax, 0xfffe
00ADD8F4  66 03 D8                        add bx, ax
00ADD8F7  66 89 5D 02                     mov word ptr [rbp + 2], bx
00ADD8FB  0F 28 45 00                     movaps xmm0, xmmword ptr [rbp]
00ADD8FF  66 0F 7F 45 90                  movdqa xmmword ptr [rbp - 0x70], xmm0
00ADD904  49 3B F4                        cmp rsi, r12
00ADD907  0F 84 F4 02 00 00               je 0x140addc01
00ADD90D  44 8B 75 A4                     mov r14d, dword ptr [rbp - 0x5c]
00ADD911  41 83 E6 01                     and r14d, 1
00ADD915  45 8B FE                        mov r15d, r14d
00ADD918  41 83 CF 10                     or r15d, 0x10
00ADD91C  33 DB                           xor ebx, ebx
00ADD91E  48 8B 85 88 00 00 00            mov rax, qword ptr [rbp + 0x88]
00ADD925  45 8B CF                        mov r9d, r15d
00ADD928  39 9E A4 01 00 00               cmp dword ptr [rsi + 0x1a4], ebx
00ADD92E  4C 8B C6                        mov r8, rsi
00ADD931  48 8B 55 C0                     mov rdx, qword ptr [rbp - 0x40]
00ADD935  48 8B 4D E8                     mov rcx, qword ptr [rbp - 0x18]
00ADD939  45 0F 44 CE                     cmove r9d, r14d
00ADD93D  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00ADD942  8B 85 20 02 00 00               mov eax, dword ptr [rbp + 0x220]
00ADD948  4C 89 6C 24 28                  mov qword ptr [rsp + 0x28], r13
00ADD94D  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00ADD951  E8 7E F4 FF FF                  call 0x140adcdd4
00ADD956  33 D2                           xor edx, edx
00ADD958  48 8D 8D C0 00 00 00            lea rcx, [rbp + 0xc0]
00ADD95F  41 B8 A0 00 00 00               mov r8d, 0xa0
00ADD965  E8 D6 92 BE FF                  call 0x1406c6c40
00ADD96A  4C 8B 4E 10                     mov r9, qword ptr [rsi + 0x10]
00ADD96E  48 8D 05 A3 53 54 FF            lea rax, [rip - 0xabac5d]
00ADD975  48 89 85 C0 00 00 00            mov qword ptr [rbp + 0xc0], rax
00ADD97C  B9 12 00 00 00                  mov ecx, 0x12
00ADD981  48 8D 85 90 00 00 00            lea rax, [rbp + 0x90]
00ADD988  C7 44 24 28 04 00 00 00         mov dword ptr [rsp + 0x28], 4
00ADD990  48 89 85 D0 00 00 00            mov qword ptr [rbp + 0xd0], rax
00ADD997  48 8D 05 D2 34 54 FF            lea rax, [rip - 0xabcb2e]
00ADD99E  48 89 85 E8 00 00 00            mov qword ptr [rbp + 0xe8], rax
00ADD9A5  48 8D 85 B0 00 00 00            lea rax, [rbp + 0xb0]
00ADD9AC  48 89 85 F8 00 00 00            mov qword ptr [rbp + 0xf8], rax
00ADD9B3  8D 51 F4                        lea edx, [rcx - 0xc]
00ADD9B6  48 8D 05 23 5C 54 FF            lea rax, [rip - 0xaba3dd]
00ADD9BD  89 95 DC 00 00 00               mov dword ptr [rbp + 0xdc], edx
00ADD9C3  48 89 85 10 01 00 00            mov qword ptr [rbp + 0x110], rax
00ADD9CA  44 8D 41 F6                     lea r8d, [rcx - 0xa]
00ADD9CE  48 8D 45 F0                     lea rax, [rbp - 0x10]
00ADD9D2  89 95 2C 01 00 00               mov dword ptr [rbp + 0x12c], edx
00ADD9D8  48 89 85 20 01 00 00            mov qword ptr [rbp + 0x120], rax
00ADD9DF  48 8D 05 5A 52 54 FF            lea rax, [rip - 0xabada6]
00ADD9E6  48 89 85 38 01 00 00            mov qword ptr [rbp + 0x138], rax
00ADD9ED  48 8D 85 A0 00 00 00            lea rax, [rbp + 0xa0]
00ADD9F4  48 89 85 48 01 00 00            mov qword ptr [rbp + 0x148], rax
00ADD9FB  48 8D 85 C0 00 00 00            lea rax, [rbp + 0xc0]
00ADDA02  89 95 54 01 00 00               mov dword ptr [rbp + 0x154], edx
00ADDA08  48 8B 56 40                     mov rdx, qword ptr [rsi + 0x40]
00ADDA0C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00ADDA11  89 8D C8 00 00 00               mov dword ptr [rbp + 0xc8], ecx
00ADDA17  C7 85 F0 00 00 00 0D 00 00 00   mov dword ptr [rbp + 0xf0], 0xd
00ADDA21  C7 85 00 01 00 00 10 00 00 00   mov dword ptr [rbp + 0x100], 0x10
00ADDA2B  C7 85 18 01 00 00 12 20 00 00   mov dword ptr [rbp + 0x118], 0x2012
00ADDA35  89 8D 40 01 00 00               mov dword ptr [rbp + 0x140], ecx
00ADDA3B  E8 2C 9D E9 FF                  call 0x14097776c
00ADDA40  85 C0                           test eax, eax
00ADDA42  0F 88 A6 01 00 00               js 0x140addbee
00ADDA48  39 9D E0 00 00 00               cmp dword ptr [rbp + 0xe0], ebx
00ADDA4E  7D 22                           jge 0x140adda72
00ADDA50  48 8B 56 30                     mov rdx, qword ptr [rsi + 0x30]
00ADDA54  48 8D 8D 90 00 00 00            lea rcx, [rbp + 0x90]
00ADDA5B  E8 00 FE ED FF                  call 0x1409bd860
00ADDA60  84 C0                           test al, al
00ADDA62  75 0E                           jne 0x140adda72
00ADDA64  33 D2                           xor edx, edx
00ADDA66  48 8D 8D 90 00 00 00            lea rcx, [rbp + 0x90]
00ADDA6D  E8 0E CD 94 FF                  call 0x14042a780
00ADDA72  39 9D 08 01 00 00               cmp dword ptr [rbp + 0x108], ebx
00ADDA78  7C 17                           jl 0x140adda91
00ADDA7A  41 B0 01                        mov r8b, 1
00ADDA7D  48 8D 55 60                     lea rdx, [rbp + 0x60]
00ADDA81  48 8D 8D B0 00 00 00            lea rcx, [rbp + 0xb0]
00ADDA88  E8 C3 79 E3 FF                  call 0x140915450
00ADDA8D  85 C0                           test eax, eax
00ADDA8F  79 0B                           jns 0x140adda9c
00ADDA91  33 D2                           xor edx, edx
00ADDA93  48 8D 4D 60                     lea rcx, [rbp + 0x60]
00ADDA97  E8 E4 CC 94 FF                  call 0x14042a780
00ADDA9C  39 9D 30 01 00 00               cmp dword ptr [rbp + 0x130], ebx
00ADDAA2  7D 0B                           jge 0x140addaaf
00ADDAA4  33 D2                           xor edx, edx
00ADDAA6  48 8D 4D F0                     lea rcx, [rbp - 0x10]
00ADDAAA  E8 D1 CC 94 FF                  call 0x14042a780
00ADDAAF  48 39 5D F8                     cmp qword ptr [rbp - 8], rbx
00ADDAB3  74 61                           je 0x140addb16
00ADDAB5  0F B7 4D F0                     movzx ecx, word ptr [rbp - 0x10]
00ADDAB9  B8 04 00 00 00                  mov eax, 4
00ADDABE  66 3B C8                        cmp cx, ax
00ADDAC1  76 53                           jbe 0x140addb16
00ADDAC3  8B C1                           mov eax, ecx
00ADDAC5  41 B9 02 00 00 00               mov r9d, 2
00ADDACB  48 D1 E8                        shr rax, 1
00ADDACE  44 8B C3                        mov r8d, ebx
00ADDAD1  49 3B C1                        cmp rax, r9
00ADDAD4  74 32                           je 0x140addb08
00ADDAD6  48 8B D3                        mov rdx, rbx
00ADDAD9  48 8B 45 F8                     mov rax, qword ptr [rbp - 8]
00ADDADD  66 39 1C 50                     cmp word ptr [rax + rdx*2], bx
00ADDAE1  75 0A                           jne 0x140addaed
00ADDAE3  66 C7 04 50 3B 00               mov word ptr [rax + rdx*2], 0x3b
00ADDAE9  0F B7 4D F0                     movzx ecx, word ptr [rbp - 0x10]
00ADDAED  41 FF C0                        inc r8d
00ADDAF0  0F B7 C1                        movzx eax, cx
00ADDAF3  48 D1 E8                        shr rax, 1
00ADDAF6  49 2B C1                        sub rax, r9
00ADDAF9  41 8B D0                        mov edx, r8d
00ADDAFC  48 3B D0                        cmp rdx, rax
00ADDAFF  72 D8                           jb 0x140addad9
00ADDB01  4C 8B AD 28 02 00 00            mov r13, qword ptr [rbp + 0x228]
00ADDB08  B8 FE FF 00 00                  mov eax, 0xfffe
00ADDB0D  66 03 C8                        add cx, ax
00ADDB10  66 89 4D F0                     mov word ptr [rbp - 0x10], cx
00ADDB14  EB 14                           jmp 0x140addb2a
00ADDB16  48 8D 4D F0                     lea rcx, [rbp - 0x10]
00ADDB1A  E8 E1 2C EE FF                  call 0x1409c0800
00ADDB1F  33 D2                           xor edx, edx
00ADDB21  48 8D 4D F0                     lea rcx, [rbp - 0x10]
00ADDB25  E8 56 CC 94 FF                  call 0x14042a780
00ADDB2A  39 9D 58 01 00 00               cmp dword ptr [rbp + 0x158], ebx
00ADDB30  7D 0E                           jge 0x140addb40
00ADDB32  33 D2                           xor edx, edx
00ADDB34  48 8D 8D A0 00 00 00            lea rcx, [rbp + 0xa0]
00ADDB3B  E8 40 CC 94 FF                  call 0x14042a780
00ADDB40  48 39 9D A8 00 00 00            cmp qword ptr [rbp + 0xa8], rbx
00ADDB47  48 8D 05 BA D1 06 00            lea rax, [rip + 0x6d1ba]
00ADDB4E  4C 8D 0D 7B EF 01 00            lea r9, [rip + 0x1ef7b]
00ADDB55  4C 8D 85 A0 00 00 00            lea r8, [rbp + 0xa0]
00ADDB5C  4C 0F 44 C0                     cmove r8, rax
00ADDB60  48 8D 55 F0                     lea rdx, [rbp - 0x10]
00ADDB64  48 39 5D F8                     cmp qword ptr [rbp - 8], rbx
00ADDB68  48 8D 0D 81 0F 02 00            lea rcx, [rip + 0x20f81]
00ADDB6F  4C 89 44 24 40                  mov qword ptr [rsp + 0x40], r8
00ADDB74  41 B8 00 08 00 00               mov r8d, 0x800
00ADDB7A  48 0F 44 D0                     cmove rdx, rax
00ADDB7E  48 3B B7 D0 00 00 00            cmp rsi, qword ptr [rdi + 0xd0]
00ADDB85  48 89 54 24 38                  mov qword ptr [rsp + 0x38], rdx
00ADDB8A  48 8D 45 60                     lea rax, [rbp + 0x60]
00ADDB8E  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00ADDB93  48 8D 55 90                     lea rdx, [rbp - 0x70]
00ADDB97  49 0F 44 C9                     cmove rcx, r9
00ADDB9B  48 8D 85 90 00 00 00            lea rax, [rbp + 0x90]
00ADDBA2  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00ADDBA7  4C 8D 0D 52 0F 02 00            lea r9, [rip + 0x20f52]
00ADDBAE  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00ADDBB3  48 8D 4D 90                     lea rcx, [rbp - 0x70]
00ADDBB7  E8 14 B4 9C FF                  call 0x1404a8fd0
00ADDBBC  48 8D 4D 60                     lea rcx, [rbp + 0x60]
00ADDBC0  8B D8                           mov ebx, eax
00ADDBC2  E8 39 2C EE FF                  call 0x1409c0800
00ADDBC7  48 8D 4D F0                     lea rcx, [rbp - 0x10]
00ADDBCB  E8 30 2C EE FF                  call 0x1409c0800
00ADDBD0  48 8D 8D 90 00 00 00            lea rcx, [rbp + 0x90]
00ADDBD7  E8 24 2C EE FF                  call 0x1409c0800
00ADDBDC  48 8D 8D A0 00 00 00            lea rcx, [rbp + 0xa0]
00ADDBE3  E8 18 2C EE FF                  call 0x1409c0800
00ADDBE8  85 DB                           test ebx, ebx
00ADDBEA  78 0E                           js 0x140addbfa
00ADDBEC  33 DB                           xor ebx, ebx
00ADDBEE  48 8B 36                        mov rsi, qword ptr [rsi]
00ADDBF1  49 3B F4                        cmp rsi, r12
00ADDBF4  0F 85 24 FD FF FF               jne 0x140add91e
00ADDBFA  44 8B B5 20 02 00 00            mov r14d, dword ptr [rbp + 0x220]
00ADDC01  33 F6                           xor esi, esi
00ADDC03  4C 8B 7D C0                     mov r15, qword ptr [rbp - 0x40]
00ADDC07  45 33 D2                        xor r10d, r10d
00ADDC0A  49 8B 47 30                     mov rax, qword ptr [r15 + 0x30]
00ADDC0E  48 85 C0                        test rax, rax
00ADDC11  48 0F 45 F0                     cmovne rsi, rax
00ADDC15  49 8B 47 40                     mov rax, qword ptr [r15 + 0x40]
00ADDC19  48 85 C0                        test rax, rax
00ADDC1C  74 4D                           je 0x140addc6b
00ADDC1E  41 8D 4A 02                     lea ecx, [r10 + 2]
00ADDC22  66 41 39 4F 38                  cmp word ptr [r15 + 0x38], cx
00ADDC27  76 42                           jbe 0x140addc6b
00ADDC29  48 83 C9 FF                     or rcx, 0xffffffffffffffff
00ADDC2D  4C 8B E0                        mov r12, rax
00ADDC30  48 8B C1                        mov rax, rcx
00ADDC33  48 FF C0                        inc rax
00ADDC36  66 45 39 14 44                  cmp word ptr [r12 + rax*2], r10w
00ADDC3B  75 F6                           jne 0x140addc33
00ADDC3D  EB 22                           jmp 0x140addc61
00ADDC3F  48 8B C1                        mov rax, rcx
00ADDC42  48 FF C0                        inc rax
00ADDC45  66 45 39 14 44                  cmp word ptr [r12 + rax*2], r10w
00ADDC4A  75 F6                           jne 0x140addc42
00ADDC4C  4D 8D 24 44                     lea r12, [r12 + rax*2]
00ADDC50  48 8B C1                        mov rax, rcx
00ADDC53  49 83 C4 02                     add r12, 2
00ADDC57  48 FF C0                        inc rax
00ADDC5A  66 45 39 14 44                  cmp word ptr [r12 + rax*2], r10w
00ADDC5F  75 F6                           jne 0x140addc57
00ADDC61  66 45 39 54 44 02               cmp word ptr [r12 + rax*2 + 2], r10w
00ADDC67  75 D6                           jne 0x140addc3f
00ADDC69  EB 03                           jmp 0x140addc6e
00ADDC6B  4D 8B E2                        mov r12, r10
00ADDC6E  48 8B 5D 18                     mov rbx, qword ptr [rbp + 0x18]
00ADDC72  48 85 DB                        test rbx, rbx
00ADDC75  75 04                           jne 0x140addc7b
00ADDC77  48 8B 5F 30                     mov rbx, qword ptr [rdi + 0x30]
00ADDC7B  B8 04 00 00 00                  mov eax, 4
00ADDC80  4C 39 97 38 01 00 00            cmp qword ptr [rdi + 0x138], r10
00ADDC87  74 63                           je 0x140addcec
00ADDC89  48 8D 97 30 01 00 00            lea rdx, [rdi + 0x130]
00ADDC90  66 39 02                        cmp word ptr [rdx], ax
00ADDC93  76 57                           jbe 0x140addcec
00ADDC95  48 8D 4D 20                     lea rcx, [rbp + 0x20]
00ADDC99  E8 A6 E3 9E FF                  call 0x1404cc044
00ADDC9E  45 33 D2                        xor r10d, r10d
00ADDCA1  84 C0                           test al, al
00ADDCA3  0F 84 F8 03 00 00               je 0x140ade0a1
00ADDCA9  0F B7 55 20                     movzx edx, word ptr [rbp + 0x20]
00ADDCAD  45 8B C2                        mov r8d, r10d
00ADDCB0  8B C2                           mov eax, edx
00ADDCB2  48 D1 E8                        shr rax, 1
00ADDCB5  48 83 E8 02                     sub rax, 2
00ADDCB9  74 20                           je 0x140addcdb
00ADDCBB  4C 8B 4D 28                     mov r9, qword ptr [rbp + 0x28]
00ADDCBF  41 8B CA                        mov ecx, r10d
00ADDCC2  66 45 39 14 49                  cmp word ptr [r9 + rcx*2], r10w
00ADDCC7  75 07                           jne 0x140addcd0
00ADDCC9  66 41 C7 04 49 3B 00            mov word ptr [r9 + rcx*2], 0x3b
00ADDCD0  41 FF C0                        inc r8d
00ADDCD3  41 8B C8                        mov ecx, r8d
00ADDCD6  48 3B C8                        cmp rcx, rax
00ADDCD9  72 E7                           jb 0x140addcc2
00ADDCDB  B8 FE FF 00 00                  mov eax, 0xfffe
00ADDCE0  66 03 D0                        add dx, ax
00ADDCE3  B8 04 00 00 00                  mov eax, 4
00ADDCE8  66 89 55 20                     mov word ptr [rbp + 0x20], dx
00ADDCEC  4C 39 97 48 01 00 00            cmp qword ptr [rdi + 0x148], r10
00ADDCF3  74 5E                           je 0x140addd53
00ADDCF5  48 8D 97 40 01 00 00            lea rdx, [rdi + 0x140]
00ADDCFC  66 39 02                        cmp word ptr [rdx], ax
00ADDCFF  76 52                           jbe 0x140addd53
00ADDD01  48 8D 4D 30                     lea rcx, [rbp + 0x30]
00ADDD05  E8 3A E3 9E FF                  call 0x1404cc044
00ADDD0A  45 33 D2                        xor r10d, r10d
00ADDD0D  84 C0                           test al, al
00ADDD0F  0F 84 8C 03 00 00               je 0x140ade0a1
00ADDD15  0F B7 55 30                     movzx edx, word ptr [rbp + 0x30]
00ADDD19  45 8B C2                        mov r8d, r10d
00ADDD1C  8B C2                           mov eax, edx
00ADDD1E  48 D1 E8                        shr rax, 1
00ADDD21  48 83 E8 02                     sub rax, 2
00ADDD25  74 20                           je 0x140addd47
00ADDD27  4C 8B 4D 38                     mov r9, qword ptr [rbp + 0x38]
00ADDD2B  41 8B CA                        mov ecx, r10d
00ADDD2E  66 45 39 14 49                  cmp word ptr [r9 + rcx*2], r10w
00ADDD33  75 07                           jne 0x140addd3c
00ADDD35  66 41 C7 04 49 3B 00            mov word ptr [r9 + rcx*2], 0x3b
00ADDD3C  41 FF C0                        inc r8d
00ADDD3F  41 8B C8                        mov ecx, r8d
00ADDD42  48 3B C8                        cmp rcx, rax
00ADDD45  72 E7                           jb 0x140addd2e
00ADDD47  B8 FE FF 00 00                  mov eax, 0xfffe
00ADDD4C  66 03 D0                        add dx, ax
00ADDD4F  66 89 55 30                     mov word ptr [rbp + 0x30], dx
00ADDD53  B8 04 00 00 00                  mov eax, 4
00ADDD58  4C 39 97 58 01 00 00            cmp qword ptr [rdi + 0x158], r10
00ADDD5F  74 6A                           je 0x140adddcb
00ADDD61  48 8D 97 50 01 00 00            lea rdx, [rdi + 0x150]
00ADDD68  66 39 02                        cmp word ptr [rdx], ax
00ADDD6B  76 5E                           jbe 0x140adddcb
00ADDD6D  48 8D 4D 40                     lea rcx, [rbp + 0x40]
00ADDD71  E8 CE E2 9E FF                  call 0x1404cc044
00ADDD76  45 33 D2                        xor r10d, r10d
00ADDD79  84 C0                           test al, al
00ADDD7B  0F 84 20 03 00 00               je 0x140ade0a1
00ADDD81  0F B7 55 40                     movzx edx, word ptr [rbp + 0x40]
00ADDD85  45 8B C2                        mov r8d, r10d
00ADDD88  8B C2                           mov eax, edx
00ADDD8A  48 D1 E8                        shr rax, 1
00ADDD8D  48 83 E8 02                     sub rax, 2
00ADDD91  74 27                           je 0x140adddba
00ADDD93  4C 8B 4D 48                     mov r9, qword ptr [rbp + 0x48]
00ADDD97  41 8B CA                        mov ecx, r10d
00ADDD9A  66 45 39 14 49                  cmp word ptr [r9 + rcx*2], r10w
00ADDD9F  75 07                           jne 0x140addda8
00ADDDA1  66 41 C7 04 49 3B 00            mov word ptr [r9 + rcx*2], 0x3b
00ADDDA8  41 FF C0                        inc r8d
00ADDDAB  41 8B C8                        mov ecx, r8d
00ADDDAE  48 3B C8                        cmp rcx, rax
00ADDDB1  72 E7                           jb 0x140addd9a
00ADDDB3  4C 8B AD 28 02 00 00            mov r13, qword ptr [rbp + 0x228]
00ADDDBA  B8 FE FF 00 00                  mov eax, 0xfffe
00ADDDBF  66 03 D0                        add dx, ax
00ADDDC2  B8 04 00 00 00                  mov eax, 4
00ADDDC7  66 89 55 40                     mov word ptr [rbp + 0x40], dx
00ADDDCB  4C 39 97 98 01 00 00            cmp qword ptr [rdi + 0x198], r10
00ADDDD2  74 65                           je 0x140adde39
00ADDDD4  48 8D 97 90 01 00 00            lea rdx, [rdi + 0x190]
00ADDDDB  66 39 02                        cmp word ptr [rdx], ax
00ADDDDE  76 59                           jbe 0x140adde39
00ADDDE0  48 8D 4D 50                     lea rcx, [rbp + 0x50]
00ADDDE4  E8 5B E2 9E FF                  call 0x1404cc044
00ADDDE9  45 33 D2                        xor r10d, r10d
00ADDDEC  84 C0                           test al, al
00ADDDEE  0F 84 AD 02 00 00               je 0x140ade0a1
00ADDDF4  0F B7 55 50                     movzx edx, word ptr [rbp + 0x50]
00ADDDF8  45 8B CA                        mov r9d, r10d
00ADDDFB  8B C2                           mov eax, edx
00ADDDFD  48 D1 E8                        shr rax, 1
00ADDE00  48 83 E8 02                     sub rax, 2
00ADDE04  74 27                           je 0x140adde2d
00ADDE06  4C 8B 45 58                     mov r8, qword ptr [rbp + 0x58]
00ADDE0A  41 8B CA                        mov ecx, r10d
00ADDE0D  66 45 39 14 48                  cmp word ptr [r8 + rcx*2], r10w
00ADDE12  75 07                           jne 0x140adde1b
00ADDE14  66 41 C7 04 48 3B 00            mov word ptr [r8 + rcx*2], 0x3b
00ADDE1B  41 FF C1                        inc r9d
00ADDE1E  41 8B C9                        mov ecx, r9d
00ADDE21  48 3B C8                        cmp rcx, rax
00ADDE24  72 E7                           jb 0x140adde0d
00ADDE26  44 8B B5 20 02 00 00            mov r14d, dword ptr [rbp + 0x220]
00ADDE2D  B8 FE FF 00 00                  mov eax, 0xfffe
00ADDE32  66 03 D0                        add dx, ax
00ADDE35  66 89 55 50                     mov word ptr [rbp + 0x50], dx
00ADDE39  33 D2                           xor edx, edx
00ADDE3B  48 8D 8D C0 00 00 00            lea rcx, [rbp + 0xc0]
00ADDE42  41 B8 A0 00 00 00               mov r8d, 0xa0
00ADDE48  E8 F3 8D BE FF                  call 0x1406c6c40
00ADDE4D  4D 8B 4F 10                     mov r9, qword ptr [r15 + 0x10]
00ADDE51  48 8D 05 78 43 54 FF            lea rax, [rip - 0xabbc88]
00ADDE58  49 8B 57 08                     mov rdx, qword ptr [r15 + 8]
00ADDE5C  33 C9                           xor ecx, ecx
00ADDE5E  48 89 85 C0 00 00 00            mov qword ptr [rbp + 0xc0], rax
00ADDE65  48 8D 45 D8                     lea rax, [rbp - 0x28]
00ADDE69  48 89 85 D0 00 00 00            mov qword ptr [rbp + 0xd0], rax
00ADDE70  48 8D 05 E9 3C 54 FF            lea rax, [rip - 0xabc317]
00ADDE77  48 89 85 E8 00 00 00            mov qword ptr [rbp + 0xe8], rax
00ADDE7E  48 8D 85 C0 00 00 00            lea rax, [rbp + 0xc0]
00ADDE85  C7 44 24 28 02 00 00 00         mov dword ptr [rsp + 0x28], 2
00ADDE8D  44 8D 41 01                     lea r8d, [rcx + 1]
00ADDE91  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00ADDE96  C7 85 C8 00 00 00 12 20 00 00   mov dword ptr [rbp + 0xc8], 0x2012
00ADDEA0  C7 85 DC 00 00 00 06 00 00 00   mov dword ptr [rbp + 0xdc], 6
00ADDEAA  C7 85 F0 00 00 00 11 00 00 00   mov dword ptr [rbp + 0xf0], 0x11
00ADDEB4  48 89 8D F8 00 00 00            mov qword ptr [rbp + 0xf8], rcx
00ADDEBB  89 8D 00 01 00 00               mov dword ptr [rbp + 0x100], ecx
00ADDEC1  E8 A6 98 E9 FF                  call 0x14097776c
00ADDEC6  45 33 FF                        xor r15d, r15d
00ADDEC9  85 C0                           test eax, eax
00ADDECB  0F 88 D0 01 00 00               js 0x140ade0a1
00ADDED1  44 39 BD E0 00 00 00            cmp dword ptr [rbp + 0xe0], r15d
00ADDED8  7D 0B                           jge 0x140addee5
00ADDEDA  33 D2                           xor edx, edx
00ADDEDC  48 8D 4D D8                     lea rcx, [rbp - 0x28]
00ADDEE0  E8 9B C8 94 FF                  call 0x14042a780
00ADDEE5  4C 8B 5D E0                     mov r11, qword ptr [rbp - 0x20]
00ADDEE9  4D 85 DB                        test r11, r11
00ADDEEC  74 63                           je 0x140addf51
00ADDEEE  0F B7 4D D8                     movzx ecx, word ptr [rbp - 0x28]
00ADDEF2  B8 04 00 00 00                  mov eax, 4
00ADDEF7  66 3B C8                        cmp cx, ax
00ADDEFA  76 55                           jbe 0x140addf51
00ADDEFC  8B C1                           mov eax, ecx
00ADDEFE  41 B9 02 00 00 00               mov r9d, 2
00ADDF04  48 D1 E8                        shr rax, 1
00ADDF07  45 8B C7                        mov r8d, r15d
00ADDF0A  49 3B C1                        cmp rax, r9
00ADDF0D  74 34                           je 0x140addf43
00ADDF0F  49 8B D7                        mov rdx, r15
00ADDF12  66 45 39 3C 53                  cmp word ptr [r11 + rdx*2], r15w
00ADDF17  75 0F                           jne 0x140addf28
00ADDF19  66 41 C7 04 53 3B 00            mov word ptr [r11 + rdx*2], 0x3b
00ADDF20  4C 8B 5D E0                     mov r11, qword ptr [rbp - 0x20]
00ADDF24  0F B7 4D D8                     movzx ecx, word ptr [rbp - 0x28]
00ADDF28  41 FF C0                        inc r8d
00ADDF2B  0F B7 C1                        movzx eax, cx
00ADDF2E  48 D1 E8                        shr rax, 1
00ADDF31  49 2B C1                        sub rax, r9
00ADDF34  41 8B D0                        mov edx, r8d
00ADDF37  48 3B D0                        cmp rdx, rax
00ADDF3A  72 D6                           jb 0x140addf12
00ADDF3C  4C 8B AD 28 02 00 00            mov r13, qword ptr [rbp + 0x228]
00ADDF43  B8 FE FF 00 00                  mov eax, 0xfffe
00ADDF48  66 03 C8                        add cx, ax
00ADDF4B  66 89 4D D8                     mov word ptr [rbp - 0x28], cx
00ADDF4F  EB 18                           jmp 0x140addf69
00ADDF51  48 8D 4D D8                     lea rcx, [rbp - 0x28]
00ADDF55  E8 A6 28 EE FF                  call 0x1409c0800
00ADDF5A  33 D2                           xor edx, edx
00ADDF5C  48 8D 4D D8                     lea rcx, [rbp - 0x28]
00ADDF60  E8 1B C8 94 FF                  call 0x14042a780
00ADDF65  4C 8B 5D E0                     mov r11, qword ptr [rbp - 0x20]
00ADDF69  81 BD 08 01 00 00 23 00 00 C0   cmp dword ptr [rbp + 0x108], 0xc0000023
00ADDF73  B8 01 00 00 00                  mov eax, 1
00ADDF78  48 8B 4D E8                     mov rcx, qword ptr [rbp - 0x18]
00ADDF7C  45 0F B6 CF                     movzx r9d, r15b
00ADDF80  44 0F 44 C8                     cmove r9d, eax
00ADDF84  44 38 3D BA 82 38 00            cmp byte ptr [rip + 0x3882ba], r15b
00ADDF8B  4C 8B 51 10                     mov r10, qword ptr [rcx + 0x10]
00ADDF8F  0F 95 C2                        setne dl
00ADDF92  44 38 7D 80                     cmp byte ptr [rbp - 0x80], r15b
00ADDF96  4C 8B BD 88 00 00 00            mov r15, qword ptr [rbp + 0x88]
00ADDF9D  4C 89 BC 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], r15
00ADDFA5  41 0F 95 C0                     setne r8b
00ADDFA9  F7 45 A4 70 00 00 00            test dword ptr [rbp - 0x5c], 0x70
00ADDFB0  44 89 B4 24 D0 00 00 00         mov dword ptr [rsp + 0xd0], r14d
00ADDFB8  4C 89 AC 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], r13
00ADDFC0  0F 95 C0                        setne al
00ADDFC3  88 84 24 C0 00 00 00            mov byte ptr [rsp + 0xc0], al
00ADDFCA  48 83 C1 28                     add rcx, 0x28
00ADDFCE  88 94 24 B8 00 00 00            mov byte ptr [rsp + 0xb8], dl
00ADDFD5  48 8D 45 C8                     lea rax, [rbp - 0x38]
00ADDFD9  48 89 84 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rax
00ADDFE1  49 8D 52 28                     lea rdx, [r10 + 0x28]
00ADDFE5  8B 45 84                        mov eax, dword ptr [rbp - 0x7c]
00ADDFE8  44 88 84 24 A8 00 00 00         mov byte ptr [rsp + 0xa8], r8b
00ADDFF0  4C 8B C6                        mov r8, rsi
00ADDFF3  88 84 24 A0 00 00 00            mov byte ptr [rsp + 0xa0], al
00ADDFFA  48 8B 45 58                     mov rax, qword ptr [rbp + 0x58]
00ADDFFE  48 89 84 24 98 00 00 00         mov qword ptr [rsp + 0x98], rax
00ADE006  48 8B 45 08                     mov rax, qword ptr [rbp + 8]
00ADE00A  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
00ADE012  48 8B 45 48                     mov rax, qword ptr [rbp + 0x48]
00ADE016  44 88 8C 24 88 00 00 00         mov byte ptr [rsp + 0x88], r9b
00ADE01E  4D 8B CC                        mov r9, r12
00ADE021  4C 89 9C 24 80 00 00 00         mov qword ptr [rsp + 0x80], r11
00ADE029  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
00ADE02E  48 8B 45 38                     mov rax, qword ptr [rbp + 0x38]
00ADE032  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00ADE037  48 8B 45 28                     mov rax, qword ptr [rbp + 0x28]
00ADE03B  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00ADE040  48 8B 87 28 01 00 00            mov rax, qword ptr [rdi + 0x128]
00ADE047  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00ADE04C  48 8B 47 50                     mov rax, qword ptr [rdi + 0x50]
00ADE050  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
00ADE055  48 8B 45 78                     mov rax, qword ptr [rbp + 0x78]
00ADE059  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00ADE05E  48 8D 85 78 01 00 00            lea rax, [rbp + 0x178]
00ADE065  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00ADE06A  48 8D 85 60 01 00 00            lea rax, [rbp + 0x160]
00ADE071  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00ADE076  48 8B 87 18 01 00 00            mov rax, qword ptr [rdi + 0x118]
00ADE07D  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00ADE082  48 8B 47 40                     mov rax, qword ptr [rdi + 0x40]
00ADE086  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
00ADE08B  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00ADE090  48 8B 87 08 01 00 00            mov rax, qword ptr [rdi + 0x108]
00ADE097  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00ADE09C  E8 1F 2C C2 FF                  call 0x140700cc0
00ADE0A1  48 8D 4D 10                     lea rcx, [rbp + 0x10]
00ADE0A5  E8 56 27 EE FF                  call 0x1409c0800
00ADE0AA  48 8D 4D B0                     lea rcx, [rbp - 0x50]
00ADE0AE  E8 4D 27 EE FF                  call 0x1409c0800
00ADE0B3  48 8D 4D C8                     lea rcx, [rbp - 0x38]
00ADE0B7  E8 44 27 EE FF                  call 0x1409c0800
00ADE0BC  48 8D 4D 70                     lea rcx, [rbp + 0x70]
00ADE0C0  E8 3B 27 EE FF                  call 0x1409c0800
00ADE0C5  48 8D 4D 00                     lea rcx, [rbp]
00ADE0C9  E8 32 27 EE FF                  call 0x1409c0800
00ADE0CE  48 8D 4D 20                     lea rcx, [rbp + 0x20]
00ADE0D2  E8 29 27 EE FF                  call 0x1409c0800
00ADE0D7  48 8D 4D 30                     lea rcx, [rbp + 0x30]
00ADE0DB  E8 20 27 EE FF                  call 0x1409c0800
00ADE0E0  48 8D 4D 40                     lea rcx, [rbp + 0x40]
00ADE0E4  E8 17 27 EE FF                  call 0x1409c0800
00ADE0E9  48 8D 4D D8                     lea rcx, [rbp - 0x28]
00ADE0ED  E8 0E 27 EE FF                  call 0x1409c0800
00ADE0F2  48 8D 4D 50                     lea rcx, [rbp + 0x50]
00ADE0F6  E8 05 27 EE FF                  call 0x1409c0800
00ADE0FB  48 8B 8D A8 01 00 00            mov rcx, qword ptr [rbp + 0x1a8]
00ADE102  48 33 CC                        xor rcx, rsp
00ADE105  E8 36 E5 BC FF                  call 0x1406ac640
00ADE10A  48 81 C4 18 03 00 00            add rsp, 0x318
00ADE111  41 5F                           pop r15
00ADE113  41 5E                           pop r14
00ADE115  41 5D                           pop r13
00ADE117  41 5C                           pop r12
00ADE119  5F                              pop rdi
00ADE11A  5E                              pop rsi
00ADE11B  5B                              pop rbx
00ADE11C  5D                              pop rbp
00ADE11D  C3                              ret
00ADE11E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiDevCfgLogDeviceConfigured(__int64 a1, __int64 a2, __int64 a3, int a4, unsigned int a5, __int64 a6, __int64 a7)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned int v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned int v_stack_m118;
    unsigned int v_stack_m11C;
    unsigned __int64 v_stack_m128;
    unsigned int v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned __int64 v_stack_m180;
    unsigned __int64 v_stack_m188;
    unsigned __int64 v_stack_m190;
    unsigned __int64 v_stack_m198;
    unsigned __int64 v_stack_m1A0;
    unsigned __int64 v_stack_m1A8;
    unsigned __int64 v_stack_m1B0;
    unsigned __int64 v_stack_m1B8;
    unsigned __int64 v_stack_m1C0;
    unsigned __int64 v_stack_m1C8;
    unsigned __int64 v_stack_m1D0;
    unsigned __int64 v_stack_m1D8;
    unsigned __int64 v_stack_m1E0;
    unsigned __int64 v_stack_m1E8;
    unsigned __int64 v_stack_m1F0;
    unsigned __int16 v_stack_m1F6;
    unsigned __int64 v_stack_m1F8;
    unsigned __int64 v_stack_m200;
    unsigned __int64 v_stack_m208;
    unsigned __int64 v_stack_m210;
    unsigned __int64 v_stack_m218;
    unsigned __int64 v_stack_m220;
    unsigned __int64 v_stack_m228;
    unsigned __int64 v_stack_m230;
    unsigned __int64 v_stack_m238;
    unsigned __int64 v_stack_m240;
    unsigned __int16 v_stack_m246;
    unsigned __int64 v_stack_m248;
    unsigned int v_stack_m254;
    unsigned int v_stack_m258;
    unsigned __int16 v_stack_m264;
    unsigned __int16 v_stack_m266;
    unsigned __int64 v_stack_m268;
    unsigned int v_stack_m274;
    unsigned __int8 v_stack_m278;
    unsigned __int64 v_stack_m280;
    unsigned int v_stack_m288;
    unsigned __int64 v_stack_m290;
    unsigned __int8 v_stack_m298;
    unsigned __int8 v_stack_m2A0;
    unsigned __int64 v_stack_m2A8;
    unsigned __int8 v_stack_m2B0;
    unsigned __int8 v_stack_m2B8;
    unsigned __int64 v_stack_m2C0;
    unsigned __int64 v_stack_m2C8;
    unsigned __int64 v_stack_m2D0;
    unsigned __int64 v_stack_m2D8;
    unsigned int v_stack_m2E0;
    unsigned int v_stack_m2E8;
    unsigned __int64 v_stack_m2F0;
    unsigned __int64 v_stack_m2F8;
    unsigned int v_stack_m300;
    unsigned __int64 v_stack_m308;
    unsigned int v_stack_m310;
    unsigned __int64 v_stack_m318;
    unsigned __int64 v_stack_m320;
    unsigned int v_stack_m328;
    unsigned int v_stack_m330;
    unsigned __int64 v_stack_m338;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m98;
    unsigned int v_stack_mA0;
    unsigned int v_stack_mA4;
    unsigned int v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned int v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned int v_stack_mC8;
    unsigned int v_stack_mCC;
    unsigned __int64 v_stack_mD8;
    unsigned int v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned int v_stack_mF0;
    unsigned int v_stack_mF4;
    unsigned int v_stack_mF8;

    v_rsp = (v_rsp) - (792);
    result = (*(unsigned __int64 *)(v_rip + 3332425)) ^ (v_rsp);
    v_stack_m50 = result;
    v_rsi = 0;
    v_stack_m170 = a7;
    result = (unsigned __int8)((*(unsigned __int8 *)(v_rip + 4272912)) & (48));
    v_stack_m254 = a4;
    v_stack_m238 = a2;
    v_stack_m210 = a1;
    v_stack_m274 = (unsigned int)((unsigned int)((unsigned int)(v_rsi + 1)));
    v_stack_m1E8 = 0;
    v_stack_m1E0 = 0;
    v_stack_m230 = 0;
    v_stack_m228 = 0;
    v_stack_m188 = 0;
    v_stack_m180 = 0;
    v_stack_m278 = 0;
    v_stack_m1D8 = 0;
    v_stack_m1D0 = 0;
    v_stack_m1C8 = 0;
    v_stack_m1C0 = 0;
    v_stack_m1B8 = 0;
    v_stack_m1B0 = 0;
    v_stack_m220 = 0;
    v_stack_m218 = 0;
    v_stack_m1A8 = 0;
    v_stack_m1A0 = 0;
    v_stack_m248 = 0;
    v_stack_m240 = 0;
    v_stack_m198 = 0;
    v_stack_m190 = 0;
    v_stack_m258 = 0;
    v_stack_m1F8 = 0;
    v_stack_m1F0 = 0;
    v_stack_m268 = v_xmm0;
    v_stack_m168 = v_xmm0;
    v_stack_m148 = v_xmm1;
    v_stack_m208 = v_xmm0;
    v_stack_m158 = v_xmm1;
    if (((unsigned __int8)(result)) != 48) goto loc_00ADE0A1;
    if (a3 == 0) goto loc_00ADD2A3;
    a2 = 0;
    result = memset(v_stack_m138, a2, 160, a4);
    v_stack_m11C = (unsigned int)(v_rsi + 6);
    v_stack_mF4 = (unsigned int)(v_rsi + 6);
    v_stack_m138 = v_rip - 11248097;
    v_stack_mCC = (unsigned int)(v_rsi + 6);
    v_stack_m128 = v_stack_m1E8;
    v_stack_m110 = v_rip - 11245894;
    v_stack_m100 = v_stack_m230;
    v_stack_mE8 = v_rip - 11248383;
    v_stack_mD8 = v_stack_m188;
    v_stack_mC0 = v_rip - 11253256;
    v_stack_mB0 = v_stack_m278;
    v_stack_m330 = 4;
    v_stack_m338 = v_stack_m138;
    v_stack_m130 = (unsigned int)(v_rsi + 18);
    v_stack_m108 = 0x2012ULL;
    v_stack_mE0 = (unsigned int)(v_rsi + 18);
    v_stack_mB8 = 17;
    v_stack_mA8 = (unsigned int)(v_rsi + 1);
    result = PiDevCfgQueryObjectProperties(v_rsi + 18, *(unsigned __int64 *)(a3 + 64), v_rsi + 8, *(unsigned __int64 *)(a3 + 16));
    if (sign_flag) goto loc_00ADE0A1;
    if (v_stack_m118 < 0) {
        a2 = 0;
        a1 = v_stack_m1E8;
        result = RtlInitUnicodeString(a1, a2, v_rsi + 8, *(unsigned __int64 *)(a3 + 16));
    }
    if (v_stack_mF0 < 0) {
        a2 = 0;
        a1 = v_stack_m230;
        result = RtlInitUnicodeString(a1, a2, v_rsi + 8, *(unsigned __int64 *)(a3 + 16));
    }
    if (v_stack_m228 == 0) goto loc_00ADD040;
    if (((unsigned __int16)(v_stack_m230)) <= 4) goto loc_00ADD040;
    result = ((unsigned int)((unsigned int)(v_stack_m230))) >> (1);
    if (result == 2) goto loc_00ADD032;
loc_00ADD005:
    if ((*(unsigned __int16 *)(v_stack_m228 + 0 * 2)) == 0) {
        *(unsigned __int16 *)(v_stack_m228 + 0 * 2) = 59;
        a3 = v_stack_m228;
        a1 = v_stack_m230;
    }
    a4 = (unsigned int)((0) + ((unsigned int)(v_rsi + 1)));
    result = ((unsigned __int16)(a1)) >> (1);
    result = (result) - (2);
    if (((unsigned int)(a4)) < result) goto loc_00ADD005;
loc_00ADD032:
    a1 = (unsigned __int16)((a1) + ((unsigned __int16)((unsigned int)(0xFFFEULL))));
    v_stack_m230 = (unsigned __int16)(a1);
    goto loc_00ADD054;
loc_00ADD040:
    result = RtlFreeAnsiString(v_stack_m230, (unsigned int)(a4), a3, a4);
    a2 = 0;
    result = RtlInitUnicodeString(v_stack_m230, a2, a3, a4);
loc_00ADD054:
    if (v_stack_mC8 < 0) {
        a2 = 0;
        a1 = v_stack_m188;
        result = RtlInitUnicodeString(a1, a2, a3, a4);
    }
    if (v_stack_mA0 < 0) {
        v_stack_m278 = 0;
    }
    if (v_stack_m1E0 != 0) {
        a1 = a3 + 40;
        a3 = (unsigned __int8)(v_rsi + 1);
        a2 = v_stack_m1E8;
        result = RtlEqualUnicodeString(a1, a2, a3, a4);
        result = (unsigned __int8)(-(result));
        a1 = (unsigned int)((a1) & ((unsigned int)((unsigned int)((unsigned int)(v_rsi + 1)))));
        v_stack_m274 = (unsigned int)(a1);
    }
    result = RtlTimeToTimeFields(a3 + 112, v_stack_m268, a3, a4);
    v_stack_m330 = (unsigned int)((__int16)(v_stack_m268));
    v_stack_m338 = (unsigned int)((__int16)(v_stack_m264));
    result = RtlStringCchPrintfW(v_stack_m98, 11, v_rip + 137590, (__int16)(v_stack_m266));
    if (sign_flag) {
        v_stack_m98 = 0;
    }
    v_stack_m328 = (unsigned int)(*(unsigned __int16 *)(a3 + 120));
    v_stack_m330 = (unsigned int)(*(unsigned __int16 *)(a3 + 122));
    result = ((unsigned int)(*(unsigned int *)(a3 + 124))) >> (16);
    v_stack_m338 = (unsigned int)(*(unsigned __int16 *)(a3 + 124));
    result = RtlStringCchPrintfW(v_stack_m80, 24, v_rip + 137125, (unsigned __int16)(result));
    if (sign_flag) {
        v_stack_m80 = 0;
    }
    v_r13 = (unsigned int)(*(unsigned int *)(a3 + 108));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 108)))) == -1) { v_r13 = 0; }
    result = Feature_KernelPnP_LogBlockedDrivers__private_IsEnabledDeviceUsageNoInline(v_stack_m80, 24, v_rip + 137125, (unsigned __int16)(result));
    if ((unsigned int)(result) != 0) goto loc_00ADD2B7;
    if ((*(unsigned __int64 *)(a3 + 224)) == (a3 + 224)) goto loc_00ADD29F;
    v_rbx = 0;
loc_00ADD150:
    result = (unsigned int)((*(unsigned __int16 *)(*(unsigned __int64 *)(a3 + 224) + 40)) + (0));
    a3 = (unsigned int)((*(unsigned __int16 *)(*(unsigned __int64 *)(a3 + 224) + 72) + 22) + ((unsigned int)(result)));
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 224) + 176) == 0) goto loc_00ADD185;
    result = (result) | (-1);
loc_00ADD172:
    result = (result) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 224) + 176) + result * 2)) != 0) goto loc_00ADD172;
    a3 = (unsigned int)((a3 + result * 2) + (2));
    goto loc_00ADD191;
loc_00ADD185:
    if ((*(unsigned int *)(*(unsigned __int64 *)(a3 + 224) + 448)) < 0) {
        a3 = (unsigned int)((a3) + (22));
    }
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 224))) != (a3 + 224)) goto loc_00ADD150;
    if (((unsigned int)(a3 + 2)) <= ((unsigned int)((unsigned int)(0xFFFEULL)))) goto loc_00ADD1AF;
    v_stack_m246 = (unsigned __int16)((unsigned int)(0xFFFEULL));
    goto loc_00ADD1B3;
loc_00ADD1AF:
    v_stack_m246 = (unsigned __int16)((unsigned __int16)((unsigned int)(0xFFFEULL)));
loc_00ADD1B3:
    result = ExAllocatePool2(256, (unsigned __int16)((unsigned __int16)((unsigned int)(0xFFFEULL))), (unsigned int)(0x67727453ULL), (unsigned __int16)(result));
    v_stack_m240 = result;
    if (result == 0) goto loc_00ADE0A1;
    *(unsigned __int16 *)(result) = 0;
    v_stack_m268 = v_xmm0;
    if ((*(unsigned __int64 *)(a3 + 224)) == (a3 + 224)) goto loc_00ADD29F;
loc_00ADD1EB:
    if ((*(unsigned __int64 *)(a3 + 224)) == (*(unsigned __int64 *)(a3 + 224))) goto loc_00ADD212;
    result = RtlUnicodeStringCopyStringEx(v_stack_m268, v_rip + 129071, v_stack_m268, (unsigned int)(0x800ULL));
    if (sign_flag) goto loc_00ADD29B;
loc_00ADD212:
    v_stack_m328 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a3 + 224) + 108)));
    v_stack_m330 = *(unsigned __int64 *)(a3 + 224) + 72;
    v_stack_m338 = *(unsigned __int64 *)(a3 + 224) + 40;
    result = RtlUnicodeStringPrintfEx(v_stack_m268, v_stack_m268, (unsigned int)(0x800ULL), v_rip + 136867);
    if (sign_flag) goto loc_00ADD29B;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 224) + 176) == 0) goto loc_00ADD263;
    v_stack_m338 = *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 224) + 176);
    goto loc_00ADD278;
loc_00ADD263:
    if (!sign_flag) goto loc_00ADD28F;
    v_stack_m338 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a3 + 224) + 448)));
loc_00ADD278:
    result = RtlUnicodeStringPrintfEx(v_stack_m268, v_stack_m268, (unsigned int)(0x800ULL), v_rip + 136840);
    if (sign_flag) goto loc_00ADD29B;
loc_00ADD28F:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 224))) != (a3 + 224)) goto loc_00ADD1EB;
loc_00ADD29B:
loc_00ADD29F:
    v_rsi = 0;
    goto loc_00ADD2B7;
loc_00ADD2A3:
    v_stack_m98 = 0;
    v_stack_m80 = 0;
    v_stack_m274 = 0;
loc_00ADD2B7:
    result = Feature_KernelPnP_LogBlockedDrivers__private_IsEnabledDeviceUsageNoInline(v_stack_m268, v_stack_m268, (unsigned int)(0x800ULL), v_rip + 136840);
    if ((unsigned int)(result) == 0) goto loc_00ADD42E;
    if ((*(unsigned __int64 *)(a2 + 24)) == (a2 + 24)) goto loc_00ADD42E;
loc_00ADD2D7:
    result = (unsigned int)((*(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 24) + 40)) + (0));
    a3 = (unsigned int)((*(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 24) + 72) + 22) + ((unsigned int)(result)));
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 24) + 176) == 0) goto loc_00ADD30C;
    result = (result) | (-1);
loc_00ADD2F9:
    result = (result) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 24) + 176) + result * 2)) != 0) goto loc_00ADD2F9;
    a3 = (unsigned int)((a3 + result * 2) + (2));
    goto loc_00ADD318;
loc_00ADD30C:
    if ((*(unsigned int *)(*(unsigned __int64 *)(a2 + 24) + 448)) < 0) {
        a3 = (unsigned int)((a3) + (22));
    }
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 24))) != (a2 + 24)) goto loc_00ADD2D7;
    if (((unsigned int)(a3 + 2)) <= ((unsigned int)((unsigned int)(0xFFFEULL)))) goto loc_00ADD336;
    v_stack_m246 = (unsigned __int16)((unsigned int)(0xFFFEULL));
    goto loc_00ADD33A;
loc_00ADD336:
    v_stack_m246 = (unsigned __int16)((unsigned __int16)((unsigned int)(0xFFFEULL)));
loc_00ADD33A:
    result = ExAllocatePool2(256, (unsigned __int16)((unsigned __int16)((unsigned int)(0xFFFEULL))), (unsigned int)(0x67727453ULL), a2 + 24);
    v_stack_m240 = result;
    if (result == 0) goto loc_00ADE0A1;
    *(unsigned __int16 *)(result) = 0;
    v_stack_m268 = v_xmm0;
    if ((*(unsigned __int64 *)(a2 + 24)) == (a2 + 24)) goto loc_00ADD42C;
loc_00ADD377:
    if ((*(unsigned __int64 *)(a2 + 24)) == (*(unsigned __int64 *)(a2 + 24))) goto loc_00ADD39F;
    result = RtlUnicodeStringCopyStringEx(v_stack_m268, v_rip + 128674, v_stack_m268, (unsigned int)(0x800ULL));
    if (sign_flag) goto loc_00ADD428;
loc_00ADD39F:
    v_stack_m328 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 24) + 108)));
    v_stack_m330 = *(unsigned __int64 *)(a2 + 24) + 72;
    v_stack_m338 = *(unsigned __int64 *)(a2 + 24) + 40;
    result = RtlUnicodeStringPrintfEx(v_stack_m268, v_stack_m268, (unsigned int)(0x800ULL), v_rip + 136470);
    if (sign_flag) goto loc_00ADD428;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 24) + 176) == 0) goto loc_00ADD3F0;
    v_stack_m338 = *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 24) + 176);
    goto loc_00ADD405;
loc_00ADD3F0:
    if (!sign_flag) goto loc_00ADD41C;
    v_stack_m338 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 24) + 448)));
loc_00ADD405:
    result = RtlUnicodeStringPrintfEx(v_stack_m268, v_stack_m268, (unsigned int)(0x800ULL), v_rip + 136443);
    if (sign_flag) goto loc_00ADD428;
loc_00ADD41C:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 24))) != (a2 + 24)) goto loc_00ADD377;
loc_00ADD428:
loc_00ADD42C:
    v_rsi = 0;
loc_00ADD42E:
    if (sign_flag) goto loc_00ADD643;
    if ((((unsigned __int8)((unsigned int)(v_stack_m254))) & (112)) != 0) goto loc_00ADD527;
    if (((*(unsigned __int8 *)(v_rip + 4271325)) & (16)) == 0) goto loc_00ADD854;
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m254)))) & (1));
    if (a3 == 0) goto loc_00ADD475;
    if ((*(unsigned int *)(a3 + 108)) == -1) goto loc_00ADD478;
    goto loc_00ADD480;
loc_00ADD475:
loc_00ADD478:
    if (a3 == 0) goto loc_00ADD498;
loc_00ADD480:
    goto loc_00ADD4A9;
loc_00ADD498:
    result = 0;
loc_00ADD4A9:
    a1 = (*(unsigned __int64 *)(v_stack_m210 + 16)) + (40);
    result = PnpGetLogString(a1, 0, (unsigned int)(0x800ULL), v_rip + 136443);
    result = PnpGetLogString(v_stack_m248, 0, (unsigned int)(0x800ULL), result);
    result = PnpGetLogString(0, 0, (unsigned int)(0x800ULL), result);
    result = PnpGetLogString(0, 0, result, result);
    result = PnpGetLogString(0, result, result, result);
    v_stack_m2D0 = v_rip + 484955;
    v_stack_m2D8 = result;
    v_stack_m2E0 = (unsigned int)((unsigned int)(a5));
    v_stack_m2E8 = (unsigned int)(v_rbx);
    v_stack_m2F0 = result;
    v_stack_m2F8 = result;
    v_stack_m300 = 0;
    v_stack_m308 = result;
    goto loc_00ADD603;
loc_00ADD527:
    if (((*(unsigned __int8 *)(v_rip + 4271100)) & (64)) == 0) goto loc_00ADD854;
    v_rbx = (unsigned int)((0) & (1));
    if (a3 == 0) goto loc_00ADD556;
    if ((*(unsigned int *)(a3 + 108)) == -1) goto loc_00ADD559;
    goto loc_00ADD561;
loc_00ADD556:
loc_00ADD559:
    if (a3 == 0) goto loc_00ADD579;
loc_00ADD561:
    goto loc_00ADD58A;
loc_00ADD579:
    result = 0;
loc_00ADD58A:
    a1 = (*(unsigned __int64 *)(v_stack_m210 + 16)) + (40);
    result = PnpGetLogString(a1, 0, result, result);
    result = PnpGetLogString(v_stack_m248, 0, result, result);
    result = PnpGetLogString(0, 0, result, result);
    result = PnpGetLogString(0, 0, result, result);
    result = PnpGetLogString(0, result, result, result);
    v_stack_m2D0 = v_rip + 484730;
    v_stack_m2D8 = result;
    v_stack_m2E0 = (unsigned int)((unsigned int)(a5));
    v_stack_m2E8 = (unsigned int)(v_rbx);
    v_stack_m2F0 = result;
    v_stack_m2F8 = result;
    v_stack_m300 = 0;
    v_stack_m308 = result;
loc_00ADD603:
    v_stack_m310 = (unsigned int)((unsigned int)(v_stack_m274));
    v_stack_m318 = result;
    v_stack_m320 = v_stack_m80;
    v_stack_m328 = v_stack_m98;
    v_stack_m330 = v_rip + 449142;
    v_stack_m338 = *(unsigned __int64 *)(a3 + 48);
    result = McTemplateK0zzjzzztzdzztdzz_EtwWriteTransfer((unsigned int)(v_stack_m274), v_rip - 11232387, result, *(unsigned __int64 *)(v_stack_m238 + 8));
    goto loc_00ADD768;
loc_00ADD643:
    if (((unsigned int)(result)) != 0xC0000361ULL) goto loc_00ADD773;
    if (((*(unsigned __int8 *)(v_rip + 4270805)) & (64)) == 0) goto loc_00ADD854;
    v_rbx = (unsigned int)((0) & (1));
    if (a3 == 0) goto loc_00ADD67D;
    if ((*(unsigned int *)(a3 + 108)) == -1) goto loc_00ADD680;
    goto loc_00ADD688;
loc_00ADD67D:
loc_00ADD680:
    if (a3 == 0) goto loc_00ADD6A0;
loc_00ADD688:
    goto loc_00ADD6B1;
loc_00ADD6A0:
    result = 0;
loc_00ADD6B1:
    a1 = (*(unsigned __int64 *)(v_stack_m210 + 16)) + (40);
    result = PnpGetLogString(a1, 0, result, *(unsigned __int64 *)(v_stack_m238 + 8));
    result = PnpGetLogString(v_stack_m248, 0, result, result);
    result = PnpGetLogString(0, 0, result, result);
    result = PnpGetLogString(0, 0, result, result);
    result = PnpGetLogString(0, result, result, result);
    v_stack_m2D0 = v_rip + 484435;
    v_stack_m2D8 = result;
    v_stack_m2E0 = 0xC0000361ULL;
    v_stack_m2E8 = (unsigned int)(v_rbx);
    v_stack_m2F0 = result;
    v_stack_m2F8 = result;
    v_stack_m300 = 0;
    v_stack_m308 = result;
    v_stack_m310 = (unsigned int)((unsigned int)(v_stack_m274));
    v_stack_m318 = result;
    v_stack_m320 = v_stack_m80;
    v_stack_m328 = v_stack_m98;
    v_stack_m330 = v_rip + 448847;
    v_stack_m338 = *(unsigned __int64 *)(a3 + 48);
    result = McTemplateK0zzjzzztzdzztdzz_EtwWriteTransfer((unsigned int)(v_stack_m274), v_rip - 11233601, result, *(unsigned __int64 *)(v_stack_m238 + 8));
loc_00ADD768:
    v_rsi = 0;
    goto loc_00ADD857;
loc_00ADD773:
    if (((*(unsigned __int8 *)(v_rip + 4270512)) & (32)) == 0) goto loc_00ADD854;
    v_rbx = (unsigned int)((0) & (1));
    if (a3 == 0) goto loc_00ADD7A2;
    if ((*(unsigned int *)(a3 + 108)) == -1) goto loc_00ADD7A5;
    goto loc_00ADD7AD;
loc_00ADD7A2:
loc_00ADD7A5:
    if (a3 == 0) goto loc_00ADD7C5;
loc_00ADD7AD:
    goto loc_00ADD7D6;
loc_00ADD7C5:
    result = 0;
loc_00ADD7D6:
    a1 = (*(unsigned __int64 *)(v_stack_m210 + 16)) + (40);
    result = PnpGetLogString(a1, 0, result, *(unsigned __int64 *)(v_stack_m238 + 8));
    result = PnpGetLogString(v_stack_m248, 0, result, result);
    result = PnpGetLogString(0, 0, result, result);
    result = PnpGetLogString(0, 0, result, result);
    result = PnpGetLogString(0, result, result, result);
    v_stack_m2D0 = v_rip + 484142;
    v_stack_m2D8 = result;
    v_stack_m2E0 = (unsigned int)((unsigned int)(a5));
    v_stack_m2E8 = (unsigned int)(v_rbx);
    v_stack_m2F0 = result;
    v_stack_m2F8 = result;
    v_stack_m300 = 0;
    v_stack_m308 = result;
    goto loc_00ADD603;
loc_00ADD854:
loc_00ADD857:
    if (a3 == 0) goto loc_00ADE0A1;
    if ((*(unsigned __int64 *)(a3 + 208)) == (a3 + 208)) goto loc_00ADDC03;
loc_00ADD87A:
    v_r15 = (unsigned int)((0) + 1);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 208))) != (a3 + 208)) goto loc_00ADD87A;
    if ((unsigned int)(v_r15) == 0) goto loc_00ADDC03;
    result = (unsigned int)((*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 208))) * ((unsigned int)(v_r15)));
    result = (unsigned int)((result) + (2));
    if (((unsigned int)(result)) <= ((unsigned int)((unsigned int)(0x7FFFULL)))) goto loc_00ADD8A7;
    v_stack_m1F6 = (unsigned __int16)((unsigned int)(0x7FFFULL));
    goto loc_00ADD8AE;
loc_00ADD8A7:
    v_stack_m1F6 = (unsigned __int16)(result);
loc_00ADD8AE:
    v_stack_m1F8 = (unsigned __int16)(v_rip + 448554);
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)((unsigned __int16)((unsigned __int16)(result)))), (unsigned int)(0x67727453ULL), result);
    v_stack_m1F0 = result;
    if (result == 0) goto loc_00ADE0A1;
    a2 = 0;
    result = memset(result, a2, (unsigned int)((unsigned int)((unsigned __int16)((unsigned __int16)(result)))), result);
    v_rbx = (unsigned __int16)(((unsigned __int16)(result)) + ((unsigned __int16)((unsigned int)(0xFFFEULL))));
    v_stack_m1F6 = (unsigned __int16)(v_rbx);
    v_stack_m268 = v_xmm0;
    if ((*(unsigned __int64 *)(a3 + 208)) == (a3 + 208)) goto loc_00ADDC01;
    v_r14 = (unsigned int)(((unsigned int)(v_stack_m254)) & (1));
    v_r15 = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) | (16));
    v_rbx = 0;
loc_00ADD91E:
    a4 = (unsigned int)((unsigned int)(v_r15));
    if ((*(unsigned int *)(*(unsigned __int64 *)(a3 + 208) + 420)) == 0) { a4 = (unsigned int)(v_r14); }
    v_stack_m328 = v_stack_m170;
    v_stack_m330 = a6;
    v_stack_m338 = (unsigned int)((unsigned int)(a5));
    result = PiDevCfgLogDeviceConfigured(v_stack_m210, v_stack_m238, *(unsigned __int64 *)(a3 + 208), a4);
    a2 = 0;
    result = memset(v_stack_m138, a2, 160, a4);
    v_stack_m138 = v_rip - 11250781;
    v_stack_m330 = 4;
    v_stack_m128 = v_stack_m168;
    v_stack_m110 = v_rip - 11258670;
    v_stack_m100 = v_stack_m148;
    v_stack_m11C = (unsigned int)(18 - 12);
    v_stack_mE8 = v_rip - 11248605;
    v_stack_mCC = (unsigned int)(18 - 12);
    v_stack_mD8 = v_stack_m208;
    v_stack_mC0 = v_rip - 11251110;
    v_stack_mB0 = v_stack_m158;
    v_stack_mA4 = (unsigned int)(18 - 12);
    v_stack_m338 = v_stack_m138;
    v_stack_m130 = 18;
    v_stack_m108 = 13;
    v_stack_mF8 = 16;
    v_stack_mE0 = 0x2012ULL;
    v_stack_mB8 = 18;
    result = PiDevCfgQueryObjectProperties(18, *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 208) + 64), 18 - 10, *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 208) + 16));
    if (sign_flag) goto loc_00ADDBEE;
    if (v_stack_m118 >= 0) goto loc_00ADDA72;
    result = RtlCreateUnicodeString(v_stack_m168, *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 208) + 48), 18 - 10, *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 208) + 16));
    if ((unsigned __int8)(result) == 0) {
        a2 = 0;
        a1 = v_stack_m168;
        result = RtlInitUnicodeString(a1, a2, 18 - 10, *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 208) + 16));
    }
    if (v_stack_mF0 < 0) goto loc_00ADDA91;
    result = RtlStringFromGUIDEx(v_stack_m148, v_stack_m198, 1, *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 208) + 16));
    if (sign_flag) {
        a2 = 0;
        a1 = v_stack_m198;
        result = RtlInitUnicodeString(a1, a2, 1, *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 208) + 16));
    }
    if (v_stack_mC8 < 0) {
        a2 = 0;
        a1 = v_stack_m208;
        result = RtlInitUnicodeString(a1, a2, 1, *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 208) + 16));
    }
    if (v_stack_m200 == 0) goto loc_00ADDB16;
    if (((unsigned __int16)(v_stack_m208)) <= 4) goto loc_00ADDB16;
    result = ((unsigned int)((unsigned int)(v_stack_m208))) >> (1);
    if (result == 2) goto loc_00ADDB08;
loc_00ADDAD9:
    if ((*(unsigned __int16 *)(v_stack_m200 + 0 * 2)) == 0) {
        *(unsigned __int16 *)(v_stack_m200 + 0 * 2) = 59;
        a1 = v_stack_m208;
    }
    a3 = (unsigned int)((0) + 1);
    result = ((unsigned __int16)(a1)) >> (1);
    result = (result) - (2);
    if (((unsigned int)((unsigned int)(a3))) < result) goto loc_00ADDAD9;
loc_00ADDB08:
    a1 = (unsigned __int16)((a1) + ((unsigned __int16)((unsigned int)(0xFFFEULL))));
    v_stack_m208 = (unsigned __int16)(a1);
    goto loc_00ADDB2A;
loc_00ADDB16:
    result = RtlFreeAnsiString(v_stack_m208, (unsigned int)((unsigned int)(a3)), a3, 2);
    a2 = 0;
    result = RtlInitUnicodeString(v_stack_m208, a2, a3, 2);
loc_00ADDB2A:
    if (v_stack_mA0 < 0) {
        a2 = 0;
        a1 = v_stack_m158;
        result = RtlInitUnicodeString(a1, a2, a3, 2);
    }
    a3 = v_stack_m158;
    if (v_stack_m150 == 0) { a3 = v_rip + 446906; }
    v_stack_m318 = a3;
    a2 = v_stack_m208;
    if (v_stack_m200 == 0) { a2 = v_rip + 446906; }
    v_stack_m320 = a2;
    v_stack_m328 = v_stack_m198;
    a1 = v_rip + 135041;
    if ((*(unsigned __int64 *)(a3 + 208)) == (*(unsigned __int64 *)(a3 + 208))) { a1 = v_rip + 126843; }
    v_stack_m330 = v_stack_m168;
    v_stack_m338 = a1;
    result = RtlUnicodeStringPrintfEx(v_stack_m268, v_stack_m268, (unsigned int)(0x800ULL), v_rip + 134994);
    result = RtlFreeAnsiString(v_stack_m198, v_stack_m268, (unsigned int)(0x800ULL), v_rip + 134994);
    result = RtlFreeAnsiString(v_stack_m208, v_stack_m268, (unsigned int)(0x800ULL), v_rip + 134994);
    result = RtlFreeAnsiString(v_stack_m168, v_stack_m268, (unsigned int)(0x800ULL), v_rip + 134994);
    result = RtlFreeAnsiString(v_stack_m158, v_stack_m268, (unsigned int)(0x800ULL), v_rip + 134994);
    if (sign_flag) goto loc_00ADDBFA;
    v_rbx = 0;
loc_00ADDBEE:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 208))) != (a3 + 208)) goto loc_00ADD91E;
loc_00ADDBFA:
loc_00ADDC01:
    v_rsi = 0;
loc_00ADDC03:
    v_r10 = 0;
    if (*(unsigned __int64 *)(v_stack_m238 + 48) != 0) { v_rsi = *(unsigned __int64 *)(v_stack_m238 + 48); }
    if (*(unsigned __int64 *)(v_stack_m238 + 64) == 0) goto loc_00ADDC6B;
    if ((*(unsigned __int16 *)(v_stack_m238 + 56)) <= ((unsigned __int16)(v_r10 + 2))) goto loc_00ADDC6B;
    a1 = (v_r10 + 2) | (-1);
loc_00ADDC33:
    result = (a1) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m238 + 64) + result * 2)) != 0) goto loc_00ADDC33;
    goto loc_00ADDC61;
loc_00ADDC3F:
loc_00ADDC42:
    result = (a1) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m238 + 64) + result * 2)) != 0) goto loc_00ADDC42;
    v_r12 = (*(unsigned __int64 *)(v_stack_m238 + 64) + result * 2) + (2);
loc_00ADDC57:
    result = (a1) + 1;
    if ((*(unsigned __int16 *)(v_r12 + result * 2)) != 0) goto loc_00ADDC57;
loc_00ADDC61:
    if ((*(unsigned __int16 *)(v_r12 + result * 2 + 2)) != 0) goto loc_00ADDC3F;
    goto loc_00ADDC6E;
loc_00ADDC6B:
loc_00ADDC6E:
    v_rbx = v_stack_m1E0;
    if (v_stack_m1E0 == 0) {
        v_rbx = *(unsigned __int64 *)(a3 + 48);
    }
    if ((*(unsigned __int64 *)(a3 + 312)) == 0) goto loc_00ADDCEC;
    if ((*(unsigned __int16 *)(a3 + 304)) <= 4) goto loc_00ADDCEC;
    result = PnpDuplicateUnicodeString(v_stack_m1D8, a3 + 304, (unsigned int)(0x800ULL), v_rip + 134994);
    v_r10 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_00ADE0A1;
    result = ((unsigned int)((unsigned int)(v_stack_m1D8))) >> (1);
    result = (result) - (2);
    if (condition_is_equal) goto loc_00ADDCDB;
loc_00ADDCC2:
    if ((*(unsigned __int16 *)(v_stack_m1D0 + 0 * 2)) == 0) {
        *(unsigned __int16 *)(v_stack_m1D0 + 0 * 2) = 59;
    }
    a3 = (unsigned int)((0) + 1);
    if (((unsigned int)((unsigned int)(a3))) < result) goto loc_00ADDCC2;
loc_00ADDCDB:
    a2 = (unsigned __int16)((v_stack_m1D8) + ((unsigned __int16)((unsigned int)(0xFFFEULL))));
    v_stack_m1D8 = (unsigned __int16)(a2);
loc_00ADDCEC:
    if ((*(unsigned __int64 *)(a3 + 328)) == 0) goto loc_00ADDD53;
    if ((*(unsigned __int16 *)(a3 + 320)) <= 4) goto loc_00ADDD53;
    result = PnpDuplicateUnicodeString(v_stack_m1C8, a3 + 320, a3, v_stack_m1D0);
    v_r10 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_00ADE0A1;
    result = ((unsigned int)((unsigned int)(v_stack_m1C8))) >> (1);
    result = (result) - (2);
    if (condition_is_equal) goto loc_00ADDD47;
loc_00ADDD2E:
    if ((*(unsigned __int16 *)(v_stack_m1C0 + 0 * 2)) == 0) {
        *(unsigned __int16 *)(v_stack_m1C0 + 0 * 2) = 59;
    }
    a3 = (unsigned int)((0) + 1);
    if (((unsigned int)((unsigned int)(a3))) < result) goto loc_00ADDD2E;
loc_00ADDD47:
    a2 = (unsigned __int16)((v_stack_m1C8) + ((unsigned __int16)((unsigned int)(0xFFFEULL))));
    v_stack_m1C8 = (unsigned __int16)(a2);
loc_00ADDD53:
    if ((*(unsigned __int64 *)(a3 + 344)) == 0) goto loc_00ADDDCB;
    if ((*(unsigned __int16 *)(a3 + 336)) <= 4) goto loc_00ADDDCB;
    result = PnpDuplicateUnicodeString(v_stack_m1B8, a3 + 336, a3, v_stack_m1C0);
    v_r10 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_00ADE0A1;
    result = ((unsigned int)((unsigned int)(v_stack_m1B8))) >> (1);
    result = (result) - (2);
    if (condition_is_equal) goto loc_00ADDDBA;
loc_00ADDD9A:
    if ((*(unsigned __int16 *)(v_stack_m1B0 + 0 * 2)) == 0) {
        *(unsigned __int16 *)(v_stack_m1B0 + 0 * 2) = 59;
    }
    a3 = (unsigned int)((0) + 1);
    if (((unsigned int)((unsigned int)(a3))) < result) goto loc_00ADDD9A;
loc_00ADDDBA:
    a2 = (unsigned __int16)((v_stack_m1B8) + ((unsigned __int16)((unsigned int)(0xFFFEULL))));
    v_stack_m1B8 = (unsigned __int16)(a2);
loc_00ADDDCB:
    if ((*(unsigned __int64 *)(a3 + 408)) == 0) goto loc_00ADDE39;
    if ((*(unsigned __int16 *)(a3 + 400)) <= 4) goto loc_00ADDE39;
    result = PnpDuplicateUnicodeString(v_stack_m1A8, a3 + 400, a3, v_stack_m1B0);
    v_r10 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_00ADE0A1;
    result = ((unsigned int)((unsigned int)(v_stack_m1A8))) >> (1);
    result = (result) - (2);
    if (condition_is_equal) goto loc_00ADDE2D;
loc_00ADDE0D:
    if ((*(unsigned __int16 *)(v_stack_m1A0 + 0 * 2)) == 0) {
        *(unsigned __int16 *)(v_stack_m1A0 + 0 * 2) = 59;
    }
    a4 = (unsigned int)((0) + 1);
    if (((unsigned int)(a4)) < result) goto loc_00ADDE0D;
loc_00ADDE2D:
    a2 = (unsigned __int16)((v_stack_m1A8) + ((unsigned __int16)((unsigned int)(0xFFFEULL))));
    v_stack_m1A8 = (unsigned __int16)(a2);
loc_00ADDE39:
    a2 = 0;
    result = memset(v_stack_m138, a2, 160, a4);
    a1 = 0;
    v_stack_m138 = v_rip - 11254920;
    v_stack_m128 = v_stack_m220;
    v_stack_m110 = v_rip - 11256599;
    v_stack_m330 = 2;
    v_stack_m338 = v_stack_m138;
    v_stack_m130 = 0x2012ULL;
    v_stack_m11C = 6;
    v_stack_m108 = 17;
    v_stack_m100 = 0;
    v_stack_mF8 = 0;
    result = PiDevCfgQueryObjectProperties(a1, *(unsigned __int64 *)(v_stack_m238 + 8), a1 + 1, *(unsigned __int64 *)(v_stack_m238 + 16));
    v_r15 = 0;
    if (sign_flag) goto loc_00ADE0A1;
    if (v_stack_m118 < 0) {
        a2 = 0;
        a1 = v_stack_m220;
        result = RtlInitUnicodeString(a1, a2, a1 + 1, *(unsigned __int64 *)(v_stack_m238 + 16));
    }
    if (v_stack_m218 == 0) goto loc_00ADDF51;
    if (((unsigned __int16)(v_stack_m220)) <= 4) goto loc_00ADDF51;
    result = ((unsigned int)((unsigned int)(v_stack_m220))) >> (1);
    if (result == 2) goto loc_00ADDF43;
loc_00ADDF12:
    v_r11 = v_stack_m218;
    if ((*(unsigned __int16 *)(v_stack_m218 + 0 * 2)) == 0) {
        *(unsigned __int16 *)(v_stack_m218 + 0 * 2) = 59;
        v_r11 = v_stack_m218;
        a1 = v_stack_m220;
    }
    a3 = (unsigned int)((0) + 1);
    result = ((unsigned __int16)(a1)) >> (1);
    result = (result) - (2);
    if (((unsigned int)((unsigned int)(a3))) < result) goto loc_00ADDF12;
loc_00ADDF43:
    a1 = (unsigned __int16)((a1) + ((unsigned __int16)((unsigned int)(0xFFFEULL))));
    v_stack_m220 = (unsigned __int16)(a1);
    goto loc_00ADDF69;
loc_00ADDF51:
    result = RtlFreeAnsiString(v_stack_m220, (unsigned int)((unsigned int)(a3)), a3, 2);
    a2 = 0;
    result = RtlInitUnicodeString(v_stack_m220, a2, a3, 2);
loc_00ADDF69:
    a4 = 0;
    if (v_stack_mF0 == 0xC0000023ULL) { a4 = 1; }
    a2 = ((*(unsigned __int8 *)(v_rip + 3703482)) != 0) ? 1 : 0;
    v_stack_m280 = v_stack_m170;
    a3 = (v_stack_m278 != 0) ? 1 : 0;
    v_stack_m288 = (unsigned int)((unsigned int)(a5));
    v_stack_m290 = a6;
    result = (((v_stack_m254) & (112)) != 0) ? 1 : 0;
    v_stack_m298 = (unsigned __int8)(result);
    a1 = (v_stack_m210) + (40);
    v_stack_m2A0 = (unsigned __int8)(a2);
    v_stack_m2A8 = v_stack_m230;
    v_stack_m2B0 = (unsigned __int8)(a3);
    v_stack_m2B8 = (unsigned __int8)((unsigned int)(v_stack_m274));
    v_stack_m2C0 = v_stack_m1A0;
    v_stack_m2C8 = v_stack_m1F0;
    v_stack_m2D0 = (unsigned __int8)(a4);
    v_stack_m2D8 = v_stack_m218;
    v_stack_m2E0 = v_stack_m1B0;
    v_stack_m2E8 = v_stack_m1C0;
    v_stack_m2F0 = v_stack_m1D0;
    v_stack_m2F8 = *(unsigned __int64 *)(a3 + 296);
    v_stack_m300 = *(unsigned __int64 *)(a3 + 80);
    v_stack_m308 = v_stack_m180;
    v_stack_m310 = v_stack_m80;
    v_stack_m318 = v_stack_m98;
    v_stack_m320 = *(unsigned __int64 *)(a3 + 280);
    v_stack_m328 = v_rbx;
    v_stack_m330 = *(unsigned __int64 *)(a3 + 64);
    v_stack_m338 = *(unsigned __int64 *)(a3 + 264);
    result = PnpTraceDeviceConfig(a1, *(unsigned __int64 *)(v_stack_m210 + 16) + 40, v_rsi, 0);
loc_00ADE0A1:
    result = RtlFreeAnsiString(v_stack_m1E8, *(unsigned __int64 *)(v_stack_m210 + 16) + 40, v_rsi, 0);
    result = RtlFreeAnsiString(v_stack_m248, *(unsigned __int64 *)(v_stack_m210 + 16) + 40, v_rsi, 0);
    result = RtlFreeAnsiString(v_stack_m230, *(unsigned __int64 *)(v_stack_m210 + 16) + 40, v_rsi, 0);
    result = RtlFreeAnsiString(v_stack_m188, *(unsigned __int64 *)(v_stack_m210 + 16) + 40, v_rsi, 0);
    result = RtlFreeAnsiString(v_stack_m1F8, *(unsigned __int64 *)(v_stack_m210 + 16) + 40, v_rsi, 0);
    result = RtlFreeAnsiString(v_stack_m1D8, *(unsigned __int64 *)(v_stack_m210 + 16) + 40, v_rsi, 0);
    result = RtlFreeAnsiString(v_stack_m1C8, *(unsigned __int64 *)(v_stack_m210 + 16) + 40, v_rsi, 0);
    result = RtlFreeAnsiString(v_stack_m1B8, *(unsigned __int64 *)(v_stack_m210 + 16) + 40, v_rsi, 0);
    result = RtlFreeAnsiString(v_stack_m220, *(unsigned __int64 *)(v_stack_m210 + 16) + 40, v_rsi, 0);
    result = RtlFreeAnsiString(v_stack_m1A8, *(unsigned __int64 *)(v_stack_m210 + 16) + 40, v_rsi, 0);
    a1 = (v_stack_m50) ^ (v_rsp);
    result = _security_check_cookie(a1, *(unsigned __int64 *)(v_stack_m210 + 16) + 40, v_rsi, 0);
    v_rsp = (v_rsp) + (792);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PiDevCfgLogDeviceConfigured(int64_t Arg1, void *Arg2, void *Arg3, int32_t Arg4, uint32_t Arg5, int64_t Arg6, int64_t Arg7)
{
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint32_t v_stack_m108;
    uint64_t v_stack_m110;
    uint32_t v_stack_m118;
    uint32_t v_stack_m11C;
    uint64_t v_stack_m128;
    uint32_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m148;
    uint64_t v_stack_m150;
    uint64_t v_stack_m158;
    uint64_t v_stack_m168;
    uint64_t v_stack_m170;
    uint64_t v_stack_m180;
    uint64_t v_stack_m188;
    uint64_t v_stack_m190;
    uint64_t v_stack_m198;
    uint64_t v_stack_m1A0;
    uint64_t v_stack_m1A8;
    uint64_t v_stack_m1B0;
    uint64_t v_stack_m1B8;
    uint64_t v_stack_m1C0;
    uint64_t v_stack_m1C8;
    uint64_t v_stack_m1D0;
    uint64_t v_stack_m1D8;
    uint64_t v_stack_m1E0;
    uint64_t v_stack_m1E8;
    uint64_t v_stack_m1F0;
    uint16_t v_stack_m1F6;
    uint64_t v_stack_m1F8;
    uint64_t v_stack_m200;
    uint64_t v_stack_m208;
    uint64_t v_stack_m210;
    uint64_t v_stack_m218;
    uint64_t v_stack_m220;
    uint64_t v_stack_m228;
    uint64_t v_stack_m230;
    uint64_t v_stack_m238;
    uint64_t v_stack_m240;
    uint16_t v_stack_m246;
    uint64_t v_stack_m248;
    uint32_t v_stack_m254;
    uint32_t v_stack_m258;
    uint16_t v_stack_m264;
    uint16_t v_stack_m266;
    uint64_t v_stack_m268;
    uint32_t v_stack_m274;
    uint8_t v_stack_m278;
    uint64_t v_stack_m280;
    uint32_t v_stack_m288;
    uint64_t v_stack_m290;
    uint8_t v_stack_m298;
    uint8_t v_stack_m2A0;
    uint64_t v_stack_m2A8;
    uint8_t v_stack_m2B0;
    uint8_t v_stack_m2B8;
    uint64_t v_stack_m2C0;
    uint64_t v_stack_m2C8;
    uint64_t v_stack_m2D0;
    uint64_t v_stack_m2D8;
    uint32_t v_stack_m2E0;
    uint32_t v_stack_m2E8;
    uint64_t v_stack_m2F0;
    uint64_t v_stack_m2F8;
    uint32_t v_stack_m300;
    uint64_t v_stack_m308;
    uint32_t v_stack_m310;
    uint64_t v_stack_m318;
    uint64_t v_stack_m320;
    uint32_t v_stack_m328;
    uint32_t v_stack_m330;
    uint64_t v_stack_m338;
    uint64_t v_stack_m50;
    uint64_t v_stack_m80;
    uint64_t v_stack_m98;
    uint32_t v_stack_mA0;
    uint32_t v_stack_mA4;
    uint32_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint32_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint32_t v_stack_mC8;
    uint32_t v_stack_mCC;
    uint64_t v_stack_mD8;
    uint32_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint32_t v_stack_mF0;
    uint32_t v_stack_mF4;
    uint32_t v_stack_mF8;

    local_rsp = (local_rsp) - (792);
    result = (*(uint64_t *)(v_rip + 0x32D949)) ^ (local_rsp);
    v_stack_m50 = result;
    local_rsi = 0;
    v_stack_m170 = Arg7;
    result = (uint8_t)((*(uint8_t *)(v_rip + 0x413310)) & (48));
    v_stack_m254 = Arg4;
    v_stack_m238 = Arg2;
    v_stack_m210 = Arg1;
    v_stack_m274 = (uint32_t)((uint32_t)((uint32_t)(local_rsi + 1)));
    v_stack_m1E8 = 0;
    v_stack_m1E0 = 0;
    v_stack_m230 = 0;
    v_stack_m228 = 0;
    v_stack_m188 = 0;
    v_stack_m180 = 0;
    v_stack_m278 = 0;
    v_stack_m1D8 = 0;
    v_stack_m1D0 = 0;
    v_stack_m1C8 = 0;
    v_stack_m1C0 = 0;
    v_stack_m1B8 = 0;
    v_stack_m1B0 = 0;
    v_stack_m220 = 0;
    v_stack_m218 = 0;
    v_stack_m1A8 = 0;
    v_stack_m1A0 = 0;
    v_stack_m248 = 0;
    v_stack_m240 = 0;
    v_stack_m198 = 0;
    v_stack_m190 = 0;
    v_stack_m258 = 0;
    v_stack_m1F8 = 0;
    v_stack_m1F0 = 0;
    v_stack_m268 = v_xmm0;
    v_stack_m168 = v_xmm0;
    v_stack_m148 = v_xmm1;
    v_stack_m208 = v_xmm0;
    v_stack_m158 = v_xmm1;
    if (((uint8_t)(result)) != 48) goto loc_00ADE0A1;
    if (Arg3 == NULL) goto loc_00ADD2A3;
    Arg2 = 0;
    result = memset(v_stack_m138, Arg2, 160, Arg4);
    v_stack_m11C = (uint32_t)(local_rsi + 6);
    v_stack_mF4 = (uint32_t)(local_rsi + 6);
    v_stack_m138 = v_rip - 11248097;
    v_stack_mCC = (uint32_t)(local_rsi + 6);
    v_stack_m128 = v_stack_m1E8;
    v_stack_m110 = v_rip - 11245894;
    v_stack_m100 = v_stack_m230;
    v_stack_mE8 = v_rip - 11248383;
    v_stack_mD8 = v_stack_m188;
    v_stack_mC0 = v_rip - 11253256;
    v_stack_mB0 = v_stack_m278;
    v_stack_m330 = 4;
    v_stack_m338 = v_stack_m138;
    v_stack_m130 = (uint32_t)(local_rsi + 18);
    v_stack_m108 = 0x2012ULL;
    v_stack_mE0 = (uint32_t)(local_rsi + 18);
    v_stack_mB8 = 17;
    v_stack_mA8 = (uint32_t)(local_rsi + 1);
    result = PiDevCfgQueryObjectProperties(local_rsi + 18, *(uint64_t *)(arg3 + 0x40), local_rsi + 8, *(uint64_t *)(arg3 + 0x10));
    if (sign_flag) goto loc_00ADE0A1;
    if (v_stack_m118 < 0) {
        Arg2 = 0;
        Arg1 = v_stack_m1E8;
        result = RtlInitUnicodeString(Arg1, Arg2, local_rsi + 8, *(uint64_t *)(arg3 + 0x10));
    }
    if (v_stack_mF0 < 0) {
        Arg2 = 0;
        Arg1 = v_stack_m230;
        result = RtlInitUnicodeString(Arg1, Arg2, local_rsi + 8, *(uint64_t *)(arg3 + 0x10));
    }
    if (v_stack_m228 == 0) goto loc_00ADD040;
    if (((uint16_t)(v_stack_m230)) <= 4) goto loc_00ADD040;
    result = ((uint32_t)((uint32_t)(v_stack_m230))) >> (1);
    if (result == 2) goto loc_00ADD032;
loc_00ADD005:
    if ((*(uint16_t *)(v_stack_m228 + 0x0 * 2)) == 0) {
        *(uint16_t *)(v_stack_m228 + 0x0 * 2) = 59;
        Arg3 = v_stack_m228;
        Arg1 = v_stack_m230;
    }
    Arg4 = (uint32_t)((0) + ((uint32_t)(local_rsi + 1)));
    result = ((uint16_t)(Arg1)) >> (1);
    result = (result) - (2);
    if (((uint32_t)(Arg4)) < result) goto loc_00ADD005;
loc_00ADD032:
    Arg1 = (uint16_t)((Arg1) + ((uint16_t)((uint32_t)(0xFFFEULL))));
    v_stack_m230 = (uint16_t)(Arg1);
    goto loc_00ADD054;
loc_00ADD040:
    result = RtlFreeAnsiString(v_stack_m230, (uint32_t)(Arg4), Arg3, Arg4);
    Arg2 = 0;
    result = RtlInitUnicodeString(v_stack_m230, Arg2, Arg3, Arg4);
loc_00ADD054:
    if (v_stack_mC8 < 0) {
        Arg2 = 0;
        Arg1 = v_stack_m188;
        result = RtlInitUnicodeString(Arg1, Arg2, Arg3, Arg4);
    }
    if (v_stack_mA0 < 0) {
        v_stack_m278 = 0;
    }
    if (v_stack_m1E0 != 0) {
        Arg1 = Arg3 + 40;
        Arg3 = (uint8_t)(local_rsi + 1);
        Arg2 = v_stack_m1E8;
        result = RtlEqualUnicodeString(Arg1, Arg2, Arg3, Arg4);
        result = (uint8_t)(-(result));
        Arg1 = (uint32_t)((Arg1) & ((uint32_t)((uint32_t)((uint32_t)(local_rsi + 1)))));
        v_stack_m274 = (uint32_t)(Arg1);
    }
    result = RtlTimeToTimeFields(Arg3 + 112, v_stack_m268, Arg3, Arg4);
    v_stack_m330 = (uint32_t)((int16_t)(v_stack_m268));
    v_stack_m338 = (uint32_t)((int16_t)(v_stack_m264));
    result = RtlStringCchPrintfW(v_stack_m98, 11, v_rip + 137590, (int16_t)(v_stack_m266));
    if (sign_flag) {
        v_stack_m98 = 0;
    }
    v_stack_m328 = (uint32_t)(*(uint16_t *)(arg3 + 0x78));
    v_stack_m330 = (uint32_t)(*(uint16_t *)(arg3 + 0x7A));
    result = ((uint32_t)(*(uint32_t *)(arg3 + 0x7C))) >> (16);
    v_stack_m338 = (uint32_t)(*(uint16_t *)(arg3 + 0x7C));
    result = RtlStringCchPrintfW(v_stack_m80, 24, v_rip + 137125, (uint16_t)(result));
    if (sign_flag) {
        v_stack_m80 = 0;
    }
    local_r13 = (uint32_t)(*(uint32_t *)(arg3 + 0x6C));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0x6C)))) == -1) { local_r13 = 0; }
    result = Feature_KernelPnP_LogBlockedDrivers__private_IsEnabledDeviceUsageNoInline(v_stack_m80, 24, v_rip + 137125, (uint16_t)(result));
    if ((uint32_t)(result) != 0) goto loc_00ADD2B7;
    if ((*(uint64_t *)(arg3 + 0xE0)) == (Arg3 + 224)) goto loc_00ADD29F;
    local_rbx = 0;
loc_00ADD150:
    result = (uint32_t)((*(uint16_t *)(*(uint64_t *)(arg3 + 0xE0) + 0x28)) + (0));
    Arg3 = (uint32_t)((*(uint16_t *)(*(uint64_t *)(arg3 + 0xE0) + 0x48) + 22) + ((uint32_t)(result)));
    if (*(uint64_t *)(*(uint64_t *)(arg3 + 0xE0) + 0xB0) == 0) goto loc_00ADD185;
    result = (result) | (-1);
loc_00ADD172:
    result = (result) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(arg3 + 0xE0) + 0xB0) + result * 2)) != 0) goto loc_00ADD172;
    Arg3 = (uint32_t)((Arg3 + result * 2) + (2));
    goto loc_00ADD191;
loc_00ADD185:
    if ((*(uint32_t *)(*(uint64_t *)(arg3 + 0xE0) + 0x1C0)) < 0) {
        Arg3 = (uint32_t)((Arg3) + (22));
    }
    if ((*(uint64_t *)(*(uint64_t *)(arg3 + 0xE0))) != (Arg3 + 224)) goto loc_00ADD150;
    if (((uint32_t)(Arg3 + 2)) <= ((uint32_t)((uint32_t)(0xFFFEULL)))) goto loc_00ADD1AF;
    v_stack_m246 = (uint16_t)((uint32_t)(0xFFFEULL));
    goto loc_00ADD1B3;
loc_00ADD1AF:
    v_stack_m246 = (uint16_t)((uint16_t)((uint32_t)(0xFFFEULL)));
loc_00ADD1B3:
    result = ExAllocatePool2(256, (uint16_t)((uint16_t)((uint32_t)(0xFFFEULL))), (uint32_t)(0x67727453ULL), (uint16_t)(result));
    v_stack_m240 = result;
    if (result == 0) goto loc_00ADE0A1;
    *(uint16_t *)(result) = 0;
    v_stack_m268 = v_xmm0;
    if ((*(uint64_t *)(arg3 + 0xE0)) == (Arg3 + 224)) goto loc_00ADD29F;
loc_00ADD1EB:
    if ((*(uint64_t *)(arg3 + 0xE0)) == (*(uint64_t *)(arg3 + 0xE0))) goto loc_00ADD212;
    result = RtlUnicodeStringCopyStringEx(v_stack_m268, v_rip + 129071, v_stack_m268, (uint32_t)(0x800ULL));
    if (sign_flag) goto loc_00ADD29B;
loc_00ADD212:
    v_stack_m328 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg3 + 0xE0) + 0x6C)));
    v_stack_m330 = *(uint64_t *)(arg3 + 0xE0) + 72;
    v_stack_m338 = *(uint64_t *)(arg3 + 0xE0) + 40;
    result = RtlUnicodeStringPrintfEx(v_stack_m268, v_stack_m268, (uint32_t)(0x800ULL), v_rip + 136867);
    if (sign_flag) goto loc_00ADD29B;
    if (*(uint64_t *)(*(uint64_t *)(arg3 + 0xE0) + 0xB0) == 0) goto loc_00ADD263;
    v_stack_m338 = *(uint64_t *)(*(uint64_t *)(arg3 + 0xE0) + 0xB0);
    goto loc_00ADD278;
loc_00ADD263:
    if (!sign_flag) goto loc_00ADD28F;
    v_stack_m338 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg3 + 0xE0) + 0x1C0)));
loc_00ADD278:
    result = RtlUnicodeStringPrintfEx(v_stack_m268, v_stack_m268, (uint32_t)(0x800ULL), v_rip + 136840);
    if (sign_flag) goto loc_00ADD29B;
loc_00ADD28F:
    if ((*(uint64_t *)(*(uint64_t *)(arg3 + 0xE0))) != (Arg3 + 224)) goto loc_00ADD1EB;
loc_00ADD29B:
loc_00ADD29F:
    local_rsi = 0;
    goto loc_00ADD2B7;
loc_00ADD2A3:
    v_stack_m98 = 0;
    v_stack_m80 = 0;
    v_stack_m274 = 0;
loc_00ADD2B7:
    result = Feature_KernelPnP_LogBlockedDrivers__private_IsEnabledDeviceUsageNoInline(v_stack_m268, v_stack_m268, (uint32_t)(0x800ULL), v_rip + 136840);
    if ((uint32_t)(result) == 0) goto loc_00ADD42E;
    if ((*(uint64_t *)(arg2 + 0x18)) == (Arg2 + 24)) goto loc_00ADD42E;
loc_00ADD2D7:
    result = (uint32_t)((*(uint16_t *)(*(uint64_t *)(arg2 + 0x18) + 0x28)) + (0));
    Arg3 = (uint32_t)((*(uint16_t *)(*(uint64_t *)(arg2 + 0x18) + 0x48) + 22) + ((uint32_t)(result)));
    if (*(uint64_t *)(*(uint64_t *)(arg2 + 0x18) + 0xB0) == 0) goto loc_00ADD30C;
    result = (result) | (-1);
loc_00ADD2F9:
    result = (result) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x18) + 0xB0) + result * 2)) != 0) goto loc_00ADD2F9;
    Arg3 = (uint32_t)((Arg3 + result * 2) + (2));
    goto loc_00ADD318;
loc_00ADD30C:
    if ((*(uint32_t *)(*(uint64_t *)(arg2 + 0x18) + 0x1C0)) < 0) {
        Arg3 = (uint32_t)((Arg3) + (22));
    }
    if ((*(uint64_t *)(*(uint64_t *)(arg2 + 0x18))) != (Arg2 + 24)) goto loc_00ADD2D7;
    if (((uint32_t)(Arg3 + 2)) <= ((uint32_t)((uint32_t)(0xFFFEULL)))) goto loc_00ADD336;
    v_stack_m246 = (uint16_t)((uint32_t)(0xFFFEULL));
    goto loc_00ADD33A;
loc_00ADD336:
    v_stack_m246 = (uint16_t)((uint16_t)((uint32_t)(0xFFFEULL)));
loc_00ADD33A:
    result = ExAllocatePool2(256, (uint16_t)((uint16_t)((uint32_t)(0xFFFEULL))), (uint32_t)(0x67727453ULL), Arg2 + 24);
    v_stack_m240 = result;
    if (result == 0) goto loc_00ADE0A1;
    *(uint16_t *)(result) = 0;
    v_stack_m268 = v_xmm0;
    if ((*(uint64_t *)(arg2 + 0x18)) == (Arg2 + 24)) goto loc_00ADD42C;
loc_00ADD377:
    if ((*(uint64_t *)(arg2 + 0x18)) == (*(uint64_t *)(arg2 + 0x18))) goto loc_00ADD39F;
    result = RtlUnicodeStringCopyStringEx(v_stack_m268, v_rip + 128674, v_stack_m268, (uint32_t)(0x800ULL));
    if (sign_flag) goto loc_00ADD428;
loc_00ADD39F:
    v_stack_m328 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x18) + 0x6C)));
    v_stack_m330 = *(uint64_t *)(arg2 + 0x18) + 72;
    v_stack_m338 = *(uint64_t *)(arg2 + 0x18) + 40;
    result = RtlUnicodeStringPrintfEx(v_stack_m268, v_stack_m268, (uint32_t)(0x800ULL), v_rip + 136470);
    if (sign_flag) goto loc_00ADD428;
    if (*(uint64_t *)(*(uint64_t *)(arg2 + 0x18) + 0xB0) == 0) goto loc_00ADD3F0;
    v_stack_m338 = *(uint64_t *)(*(uint64_t *)(arg2 + 0x18) + 0xB0);
    goto loc_00ADD405;
loc_00ADD3F0:
    if (!sign_flag) goto loc_00ADD41C;
    v_stack_m338 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x18) + 0x1C0)));
loc_00ADD405:
    result = RtlUnicodeStringPrintfEx(v_stack_m268, v_stack_m268, (uint32_t)(0x800ULL), v_rip + 136443);
    if (sign_flag) goto loc_00ADD428;
loc_00ADD41C:
    if ((*(uint64_t *)(*(uint64_t *)(arg2 + 0x18))) != (Arg2 + 24)) goto loc_00ADD377;
loc_00ADD428:
loc_00ADD42C:
    local_rsi = 0;
loc_00ADD42E:
    if (sign_flag) goto loc_00ADD643;
    if ((((uint8_t)((uint32_t)(v_stack_m254))) & (112)) != 0) goto loc_00ADD527;
    if (((*(uint8_t *)(v_rip + 0x412CDD)) & (16)) == 0) goto loc_00ADD854;
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m254)))) & (1));
    if (Arg3 == NULL) goto loc_00ADD475;
    if ((*(uint32_t *)(arg3 + 0x6C)) == -1) goto loc_00ADD478;
    goto loc_00ADD480;
loc_00ADD475:
loc_00ADD478:
    if (Arg3 == NULL) goto loc_00ADD498;
loc_00ADD480:
    goto loc_00ADD4A9;
loc_00ADD498:
    result = 0;
loc_00ADD4A9:
    Arg1 = (*(uint64_t *)(v_stack_m210 + 0x10)) + (40);
    result = PnpGetLogString(Arg1, 0, (uint32_t)(0x800ULL), v_rip + 136443);
    result = PnpGetLogString(v_stack_m248, 0, (uint32_t)(0x800ULL), result);
    result = PnpGetLogString(0, 0, (uint32_t)(0x800ULL), result);
    result = PnpGetLogString(0, 0, result, result);
    result = PnpGetLogString(0, result, result, result);
    v_stack_m2D0 = v_rip + 484955;
    v_stack_m2D8 = result;
    v_stack_m2E0 = (uint32_t)((uint32_t)(Arg5));
    v_stack_m2E8 = (uint32_t)(local_rbx);
    v_stack_m2F0 = result;
    v_stack_m2F8 = result;
    v_stack_m300 = 0;
    v_stack_m308 = result;
    goto loc_00ADD603;
loc_00ADD527:
    if (((*(uint8_t *)(v_rip + 0x412BFC)) & (64)) == 0) goto loc_00ADD854;
    local_rbx = (uint32_t)((0) & (1));
    if (Arg3 == NULL) goto loc_00ADD556;
    if ((*(uint32_t *)(arg3 + 0x6C)) == -1) goto loc_00ADD559;
    goto loc_00ADD561;
loc_00ADD556:
loc_00ADD559:
    if (Arg3 == NULL) goto loc_00ADD579;
loc_00ADD561:
    goto loc_00ADD58A;
loc_00ADD579:
    result = 0;
loc_00ADD58A:
    Arg1 = (*(uint64_t *)(v_stack_m210 + 0x10)) + (40);
    result = PnpGetLogString(Arg1, 0, result, result);
    result = PnpGetLogString(v_stack_m248, 0, result, result);
    result = PnpGetLogString(0, 0, result, result);
    result = PnpGetLogString(0, 0, result, result);
    result = PnpGetLogString(0, result, result, result);
    v_stack_m2D0 = v_rip + 484730;
    v_stack_m2D8 = result;
    v_stack_m2E0 = (uint32_t)((uint32_t)(Arg5));
    v_stack_m2E8 = (uint32_t)(local_rbx);
    v_stack_m2F0 = result;
    v_stack_m2F8 = result;
    v_stack_m300 = 0;
    v_stack_m308 = result;
loc_00ADD603:
    v_stack_m310 = (uint32_t)((uint32_t)(v_stack_m274));
    v_stack_m318 = result;
    v_stack_m320 = v_stack_m80;
    v_stack_m328 = v_stack_m98;
    v_stack_m330 = v_rip + 449142;
    v_stack_m338 = *(uint64_t *)(arg3 + 0x30);
    result = McTemplateK0zzjzzztzdzztdzz_EtwWriteTransfer((uint32_t)(v_stack_m274), v_rip - 11232387, result, *(uint64_t *)(v_stack_m238 + 0x8));
    goto loc_00ADD768;
loc_00ADD643:
    if (((uint32_t)(result)) != 0xC0000361ULL) goto loc_00ADD773;
    if (((*(uint8_t *)(v_rip + 0x412AD5)) & (64)) == 0) goto loc_00ADD854;
    local_rbx = (uint32_t)((0) & (1));
    if (Arg3 == NULL) goto loc_00ADD67D;
    if ((*(uint32_t *)(arg3 + 0x6C)) == -1) goto loc_00ADD680;
    goto loc_00ADD688;
loc_00ADD67D:
loc_00ADD680:
    if (Arg3 == NULL) goto loc_00ADD6A0;
loc_00ADD688:
    goto loc_00ADD6B1;
loc_00ADD6A0:
    result = 0;
loc_00ADD6B1:
    Arg1 = (*(uint64_t *)(v_stack_m210 + 0x10)) + (40);
    result = PnpGetLogString(Arg1, 0, result, *(uint64_t *)(v_stack_m238 + 0x8));
    result = PnpGetLogString(v_stack_m248, 0, result, result);
    result = PnpGetLogString(0, 0, result, result);
    result = PnpGetLogString(0, 0, result, result);
    result = PnpGetLogString(0, result, result, result);
    v_stack_m2D0 = v_rip + 484435;
    v_stack_m2D8 = result;
    v_stack_m2E0 = 0xC0000361ULL;
    v_stack_m2E8 = (uint32_t)(local_rbx);
    v_stack_m2F0 = result;
    v_stack_m2F8 = result;
    v_stack_m300 = 0;
    v_stack_m308 = result;
    v_stack_m310 = (uint32_t)((uint32_t)(v_stack_m274));
    v_stack_m318 = result;
    v_stack_m320 = v_stack_m80;
    v_stack_m328 = v_stack_m98;
    v_stack_m330 = v_rip + 448847;
    v_stack_m338 = *(uint64_t *)(arg3 + 0x30);
    result = McTemplateK0zzjzzztzdzztdzz_EtwWriteTransfer((uint32_t)(v_stack_m274), v_rip - 11233601, result, *(uint64_t *)(v_stack_m238 + 0x8));
loc_00ADD768:
    local_rsi = 0;
    goto loc_00ADD857;
loc_00ADD773:
    if (((*(uint8_t *)(v_rip + 0x4129B0)) & (32)) == 0) goto loc_00ADD854;
    local_rbx = (uint32_t)((0) & (1));
    if (Arg3 == NULL) goto loc_00ADD7A2;
    if ((*(uint32_t *)(arg3 + 0x6C)) == -1) goto loc_00ADD7A5;
    goto loc_00ADD7AD;
loc_00ADD7A2:
loc_00ADD7A5:
    if (Arg3 == NULL) goto loc_00ADD7C5;
loc_00ADD7AD:
    goto loc_00ADD7D6;
loc_00ADD7C5:
    result = 0;
loc_00ADD7D6:
    Arg1 = (*(uint64_t *)(v_stack_m210 + 0x10)) + (40);
    result = PnpGetLogString(Arg1, 0, result, *(uint64_t *)(v_stack_m238 + 0x8));
    result = PnpGetLogString(v_stack_m248, 0, result, result);
    result = PnpGetLogString(0, 0, result, result);
    result = PnpGetLogString(0, 0, result, result);
    result = PnpGetLogString(0, result, result, result);
    v_stack_m2D0 = v_rip + 484142;
    v_stack_m2D8 = result;
    v_stack_m2E0 = (uint32_t)((uint32_t)(Arg5));
    v_stack_m2E8 = (uint32_t)(local_rbx);
    v_stack_m2F0 = result;
    v_stack_m2F8 = result;
    v_stack_m300 = 0;
    v_stack_m308 = result;
    goto loc_00ADD603;
loc_00ADD854:
loc_00ADD857:
    if (Arg3 == NULL) goto loc_00ADE0A1;
    if ((*(uint64_t *)(arg3 + 0xD0)) == (Arg3 + 208)) goto loc_00ADDC03;
loc_00ADD87A:
    local_r15 = (uint32_t)((0) + 1);
    if ((*(uint64_t *)(*(uint64_t *)(arg3 + 0xD0))) != (Arg3 + 208)) goto loc_00ADD87A;
    if ((uint32_t)(local_r15) == 0) goto loc_00ADDC03;
    result = (uint32_t)((*(uint64_t *)(*(uint64_t *)(arg3 + 0xD0))) * ((uint32_t)(local_r15)));
    result = (uint32_t)((result) + (2));
    if (((uint32_t)(result)) <= ((uint32_t)((uint32_t)(0x7FFFULL)))) goto loc_00ADD8A7;
    v_stack_m1F6 = (uint16_t)((uint32_t)(0x7FFFULL));
    goto loc_00ADD8AE;
loc_00ADD8A7:
    v_stack_m1F6 = (uint16_t)(result);
loc_00ADD8AE:
    v_stack_m1F8 = (uint16_t)(v_rip + 448554);
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)((uint16_t)((uint16_t)(result)))), (uint32_t)(0x67727453ULL), result);
    v_stack_m1F0 = result;
    if (result == 0) goto loc_00ADE0A1;
    Arg2 = 0;
    result = memset(result, Arg2, (uint32_t)((uint32_t)((uint16_t)((uint16_t)(result)))), result);
    local_rbx = (uint16_t)(((uint16_t)(result)) + ((uint16_t)((uint32_t)(0xFFFEULL))));
    v_stack_m1F6 = (uint16_t)(local_rbx);
    v_stack_m268 = v_xmm0;
    if ((*(uint64_t *)(arg3 + 0xD0)) == (Arg3 + 208)) goto loc_00ADDC01;
    local_r14 = (uint32_t)(((uint32_t)(v_stack_m254)) & (1));
    local_r15 = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) | (16));
    local_rbx = 0;
loc_00ADD91E:
    Arg4 = (uint32_t)((uint32_t)(local_r15));
    if ((*(uint32_t *)(*(uint64_t *)(arg3 + 0xD0) + 0x1A4)) == 0) { Arg4 = (uint32_t)(local_r14); }
    v_stack_m328 = v_stack_m170;
    v_stack_m330 = Arg6;
    v_stack_m338 = (uint32_t)((uint32_t)(Arg5));
    result = PiDevCfgLogDeviceConfigured(v_stack_m210, v_stack_m238, *(uint64_t *)(arg3 + 0xD0), Arg4);
    Arg2 = 0;
    result = memset(v_stack_m138, Arg2, 160, Arg4);
    v_stack_m138 = v_rip - 11250781;
    v_stack_m330 = 4;
    v_stack_m128 = v_stack_m168;
    v_stack_m110 = v_rip - 11258670;
    v_stack_m100 = v_stack_m148;
    v_stack_m11C = (uint32_t)(18 - 12);
    v_stack_mE8 = v_rip - 11248605;
    v_stack_mCC = (uint32_t)(18 - 12);
    v_stack_mD8 = v_stack_m208;
    v_stack_mC0 = v_rip - 11251110;
    v_stack_mB0 = v_stack_m158;
    v_stack_mA4 = (uint32_t)(18 - 12);
    v_stack_m338 = v_stack_m138;
    v_stack_m130 = 18;
    v_stack_m108 = 13;
    v_stack_mF8 = 16;
    v_stack_mE0 = 0x2012ULL;
    v_stack_mB8 = 18;
    result = PiDevCfgQueryObjectProperties(18, *(uint64_t *)(*(uint64_t *)(arg3 + 0xD0) + 0x40), 18 - 10, *(uint64_t *)(*(uint64_t *)(arg3 + 0xD0) + 0x10));
    if (sign_flag) goto loc_00ADDBEE;
    if (v_stack_m118 >= 0) goto loc_00ADDA72;
    result = RtlCreateUnicodeString(v_stack_m168, *(uint64_t *)(*(uint64_t *)(arg3 + 0xD0) + 0x30), 18 - 10, *(uint64_t *)(*(uint64_t *)(arg3 + 0xD0) + 0x10));
    if ((uint8_t)(result) == 0) {
        Arg2 = 0;
        Arg1 = v_stack_m168;
        result = RtlInitUnicodeString(Arg1, Arg2, 18 - 10, *(uint64_t *)(*(uint64_t *)(arg3 + 0xD0) + 0x10));
    }
    if (v_stack_mF0 < 0) goto loc_00ADDA91;
    result = RtlStringFromGUIDEx(v_stack_m148, v_stack_m198, 1, *(uint64_t *)(*(uint64_t *)(arg3 + 0xD0) + 0x10));
    if (sign_flag) {
        Arg2 = 0;
        Arg1 = v_stack_m198;
        result = RtlInitUnicodeString(Arg1, Arg2, 1, *(uint64_t *)(*(uint64_t *)(arg3 + 0xD0) + 0x10));
    }
    if (v_stack_mC8 < 0) {
        Arg2 = 0;
        Arg1 = v_stack_m208;
        result = RtlInitUnicodeString(Arg1, Arg2, 1, *(uint64_t *)(*(uint64_t *)(arg3 + 0xD0) + 0x10));
    }
    if (v_stack_m200 == 0) goto loc_00ADDB16;
    if (((uint16_t)(v_stack_m208)) <= 4) goto loc_00ADDB16;
    result = ((uint32_t)((uint32_t)(v_stack_m208))) >> (1);
    if (result == 2) goto loc_00ADDB08;
loc_00ADDAD9:
    if ((*(uint16_t *)(v_stack_m200 + 0x0 * 2)) == 0) {
        *(uint16_t *)(v_stack_m200 + 0x0 * 2) = 59;
        Arg1 = v_stack_m208;
    }
    Arg3 = (uint32_t)((0) + 1);
    result = ((uint16_t)(Arg1)) >> (1);
    result = (result) - (2);
    if (((uint32_t)((uint32_t)(Arg3))) < result) goto loc_00ADDAD9;
loc_00ADDB08:
    Arg1 = (uint16_t)((Arg1) + ((uint16_t)((uint32_t)(0xFFFEULL))));
    v_stack_m208 = (uint16_t)(Arg1);
    goto loc_00ADDB2A;
loc_00ADDB16:
    result = RtlFreeAnsiString(v_stack_m208, (uint32_t)((uint32_t)(Arg3)), Arg3, 2);
    Arg2 = 0;
    result = RtlInitUnicodeString(v_stack_m208, Arg2, Arg3, 2);
loc_00ADDB2A:
    if (v_stack_mA0 < 0) {
        Arg2 = 0;
        Arg1 = v_stack_m158;
        result = RtlInitUnicodeString(Arg1, Arg2, Arg3, 2);
    }
    Arg3 = v_stack_m158;
    if (v_stack_m150 == 0) { Arg3 = v_rip + 446906; }
    v_stack_m318 = Arg3;
    Arg2 = v_stack_m208;
    if (v_stack_m200 == 0) { Arg2 = v_rip + 446906; }
    v_stack_m320 = Arg2;
    v_stack_m328 = v_stack_m198;
    Arg1 = v_rip + 135041;
    if ((*(uint64_t *)(arg3 + 0xD0)) == (*(uint64_t *)(arg3 + 0xD0))) { Arg1 = v_rip + 126843; }
    v_stack_m330 = v_stack_m168;
    v_stack_m338 = Arg1;
    result = RtlUnicodeStringPrintfEx(v_stack_m268, v_stack_m268, (uint32_t)(0x800ULL), v_rip + 134994);
    result = RtlFreeAnsiString(v_stack_m198, v_stack_m268, (uint32_t)(0x800ULL), v_rip + 134994);
    result = RtlFreeAnsiString(v_stack_m208, v_stack_m268, (uint32_t)(0x800ULL), v_rip + 134994);
    result = RtlFreeAnsiString(v_stack_m168, v_stack_m268, (uint32_t)(0x800ULL), v_rip + 134994);
    result = RtlFreeAnsiString(v_stack_m158, v_stack_m268, (uint32_t)(0x800ULL), v_rip + 134994);
    if (sign_flag) goto loc_00ADDBFA;
    local_rbx = 0;
loc_00ADDBEE:
    if ((*(uint64_t *)(*(uint64_t *)(arg3 + 0xD0))) != (Arg3 + 208)) goto loc_00ADD91E;
loc_00ADDBFA:
loc_00ADDC01:
    local_rsi = 0;
loc_00ADDC03:
    local_r10 = 0;
    if (*(uint64_t *)(v_stack_m238 + 0x30) != 0) { local_rsi = *(uint64_t *)(v_stack_m238 + 0x30); }
    if (*(uint64_t *)(v_stack_m238 + 0x40) == 0) goto loc_00ADDC6B;
    if ((*(uint16_t *)(v_stack_m238 + 0x38)) <= ((uint16_t)(local_r10 + 2))) goto loc_00ADDC6B;
    Arg1 = (local_r10 + 2) | (-1);
loc_00ADDC33:
    result = (Arg1) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(v_stack_m238 + 0x40) + result * 2)) != 0) goto loc_00ADDC33;
    goto loc_00ADDC61;
loc_00ADDC3F:
loc_00ADDC42:
    result = (Arg1) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(v_stack_m238 + 0x40) + result * 2)) != 0) goto loc_00ADDC42;
    local_r12 = (*(uint64_t *)(v_stack_m238 + 0x40) + result * 2) + (2);
loc_00ADDC57:
    result = (Arg1) + 1;
    if ((*(uint16_t *)(local_r12 + result * 2)) != 0) goto loc_00ADDC57;
loc_00ADDC61:
    if ((*(uint16_t *)(local_r12 + result * 2 + 0x2)) != 0) goto loc_00ADDC3F;
    goto loc_00ADDC6E;
loc_00ADDC6B:
loc_00ADDC6E:
    local_rbx = v_stack_m1E0;
    if (v_stack_m1E0 == 0) {
        local_rbx = *(uint64_t *)(arg3 + 0x30);
    }
    if ((*(uint64_t *)(arg3 + 0x138)) == 0) goto loc_00ADDCEC;
    if ((*(uint16_t *)(arg3 + 0x130)) <= 4) goto loc_00ADDCEC;
    result = PnpDuplicateUnicodeString(v_stack_m1D8, Arg3 + 304, (uint32_t)(0x800ULL), v_rip + 134994);
    local_r10 = 0;
    if ((uint8_t)(result) == 0) goto loc_00ADE0A1;
    result = ((uint32_t)((uint32_t)(v_stack_m1D8))) >> (1);
    result = (result) - (2);
    if (condition_is_equal) goto loc_00ADDCDB;
loc_00ADDCC2:
    if ((*(uint16_t *)(v_stack_m1D0 + 0x0 * 2)) == 0) {
        *(uint16_t *)(v_stack_m1D0 + 0x0 * 2) = 59;
    }
    Arg3 = (uint32_t)((0) + 1);
    if (((uint32_t)((uint32_t)(Arg3))) < result) goto loc_00ADDCC2;
loc_00ADDCDB:
    Arg2 = (uint16_t)((v_stack_m1D8) + ((uint16_t)((uint32_t)(0xFFFEULL))));
    v_stack_m1D8 = (uint16_t)(Arg2);
loc_00ADDCEC:
    if ((*(uint64_t *)(arg3 + 0x148)) == 0) goto loc_00ADDD53;
    if ((*(uint16_t *)(arg3 + 0x140)) <= 4) goto loc_00ADDD53;
    result = PnpDuplicateUnicodeString(v_stack_m1C8, Arg3 + 320, Arg3, v_stack_m1D0);
    local_r10 = 0;
    if ((uint8_t)(result) == 0) goto loc_00ADE0A1;
    result = ((uint32_t)((uint32_t)(v_stack_m1C8))) >> (1);
    result = (result) - (2);
    if (condition_is_equal) goto loc_00ADDD47;
loc_00ADDD2E:
    if ((*(uint16_t *)(v_stack_m1C0 + 0x0 * 2)) == 0) {
        *(uint16_t *)(v_stack_m1C0 + 0x0 * 2) = 59;
    }
    Arg3 = (uint32_t)((0) + 1);
    if (((uint32_t)((uint32_t)(Arg3))) < result) goto loc_00ADDD2E;
loc_00ADDD47:
    Arg2 = (uint16_t)((v_stack_m1C8) + ((uint16_t)((uint32_t)(0xFFFEULL))));
    v_stack_m1C8 = (uint16_t)(Arg2);
loc_00ADDD53:
    if ((*(uint64_t *)(arg3 + 0x158)) == 0) goto loc_00ADDDCB;
    if ((*(uint16_t *)(arg3 + 0x150)) <= 4) goto loc_00ADDDCB;
    result = PnpDuplicateUnicodeString(v_stack_m1B8, Arg3 + 336, Arg3, v_stack_m1C0);
    local_r10 = 0;
    if ((uint8_t)(result) == 0) goto loc_00ADE0A1;
    result = ((uint32_t)((uint32_t)(v_stack_m1B8))) >> (1);
    result = (result) - (2);
    if (condition_is_equal) goto loc_00ADDDBA;
loc_00ADDD9A:
    if ((*(uint16_t *)(v_stack_m1B0 + 0x0 * 2)) == 0) {
        *(uint16_t *)(v_stack_m1B0 + 0x0 * 2) = 59;
    }
    Arg3 = (uint32_t)((0) + 1);
    if (((uint32_t)((uint32_t)(Arg3))) < result) goto loc_00ADDD9A;
loc_00ADDDBA:
    Arg2 = (uint16_t)((v_stack_m1B8) + ((uint16_t)((uint32_t)(0xFFFEULL))));
    v_stack_m1B8 = (uint16_t)(Arg2);
loc_00ADDDCB:
    if ((*(uint64_t *)(arg3 + 0x198)) == 0) goto loc_00ADDE39;
    if ((*(uint16_t *)(arg3 + 0x190)) <= 4) goto loc_00ADDE39;
    result = PnpDuplicateUnicodeString(v_stack_m1A8, Arg3 + 400, Arg3, v_stack_m1B0);
    local_r10 = 0;
    if ((uint8_t)(result) == 0) goto loc_00ADE0A1;
    result = ((uint32_t)((uint32_t)(v_stack_m1A8))) >> (1);
    result = (result) - (2);
    if (condition_is_equal) goto loc_00ADDE2D;
loc_00ADDE0D:
    if ((*(uint16_t *)(v_stack_m1A0 + 0x0 * 2)) == 0) {
        *(uint16_t *)(v_stack_m1A0 + 0x0 * 2) = 59;
    }
    Arg4 = (uint32_t)((0) + 1);
    if (((uint32_t)(Arg4)) < result) goto loc_00ADDE0D;
loc_00ADDE2D:
    Arg2 = (uint16_t)((v_stack_m1A8) + ((uint16_t)((uint32_t)(0xFFFEULL))));
    v_stack_m1A8 = (uint16_t)(Arg2);
loc_00ADDE39:
    Arg2 = 0;
    result = memset(v_stack_m138, Arg2, 160, Arg4);
    Arg1 = 0;
    v_stack_m138 = v_rip - 11254920;
    v_stack_m128 = v_stack_m220;
    v_stack_m110 = v_rip - 11256599;
    v_stack_m330 = 2;
    v_stack_m338 = v_stack_m138;
    v_stack_m130 = 0x2012ULL;
    v_stack_m11C = 6;
    v_stack_m108 = 17;
    v_stack_m100 = 0;
    v_stack_mF8 = 0;
    result = PiDevCfgQueryObjectProperties(Arg1, *(uint64_t *)(v_stack_m238 + 0x8), Arg1 + 1, *(uint64_t *)(v_stack_m238 + 0x10));
    local_r15 = 0;
    if (sign_flag) goto loc_00ADE0A1;
    if (v_stack_m118 < 0) {
        Arg2 = 0;
        Arg1 = v_stack_m220;
        result = RtlInitUnicodeString(Arg1, Arg2, Arg1 + 1, *(uint64_t *)(v_stack_m238 + 0x10));
    }
    if (v_stack_m218 == 0) goto loc_00ADDF51;
    if (((uint16_t)(v_stack_m220)) <= 4) goto loc_00ADDF51;
    result = ((uint32_t)((uint32_t)(v_stack_m220))) >> (1);
    if (result == 2) goto loc_00ADDF43;
loc_00ADDF12:
    local_r11 = v_stack_m218;
    if ((*(uint16_t *)(v_stack_m218 + 0x0 * 2)) == 0) {
        *(uint16_t *)(v_stack_m218 + 0x0 * 2) = 59;
        local_r11 = v_stack_m218;
        Arg1 = v_stack_m220;
    }
    Arg3 = (uint32_t)((0) + 1);
    result = ((uint16_t)(Arg1)) >> (1);
    result = (result) - (2);
    if (((uint32_t)((uint32_t)(Arg3))) < result) goto loc_00ADDF12;
loc_00ADDF43:
    Arg1 = (uint16_t)((Arg1) + ((uint16_t)((uint32_t)(0xFFFEULL))));
    v_stack_m220 = (uint16_t)(Arg1);
    goto loc_00ADDF69;
loc_00ADDF51:
    result = RtlFreeAnsiString(v_stack_m220, (uint32_t)((uint32_t)(Arg3)), Arg3, 2);
    Arg2 = 0;
    result = RtlInitUnicodeString(v_stack_m220, Arg2, Arg3, 2);
loc_00ADDF69:
    Arg4 = 0;
    if (v_stack_mF0 == 0xC0000023ULL) { Arg4 = 1; }
    Arg2 = ((*(uint8_t *)(v_rip + 0x3882BA)) != 0) ? 1 : 0;
    v_stack_m280 = v_stack_m170;
    Arg3 = (v_stack_m278 != 0) ? 1 : 0;
    v_stack_m288 = (uint32_t)((uint32_t)(Arg5));
    v_stack_m290 = Arg6;
    result = (((v_stack_m254) & (112)) != 0) ? 1 : 0;
    v_stack_m298 = (uint8_t)(result);
    Arg1 = (v_stack_m210) + (40);
    v_stack_m2A0 = (uint8_t)(Arg2);
    v_stack_m2A8 = v_stack_m230;
    v_stack_m2B0 = (uint8_t)(Arg3);
    v_stack_m2B8 = (uint8_t)((uint32_t)(v_stack_m274));
    v_stack_m2C0 = v_stack_m1A0;
    v_stack_m2C8 = v_stack_m1F0;
    v_stack_m2D0 = (uint8_t)(Arg4);
    v_stack_m2D8 = v_stack_m218;
    v_stack_m2E0 = v_stack_m1B0;
    v_stack_m2E8 = v_stack_m1C0;
    v_stack_m2F0 = v_stack_m1D0;
    v_stack_m2F8 = *(uint64_t *)(arg3 + 0x128);
    v_stack_m300 = *(uint64_t *)(arg3 + 0x50);
    v_stack_m308 = v_stack_m180;
    v_stack_m310 = v_stack_m80;
    v_stack_m318 = v_stack_m98;
    v_stack_m320 = *(uint64_t *)(arg3 + 0x118);
    v_stack_m328 = local_rbx;
    v_stack_m330 = *(uint64_t *)(arg3 + 0x40);
    v_stack_m338 = *(uint64_t *)(arg3 + 0x108);
    result = PnpTraceDeviceConfig(Arg1, *(uint64_t *)(v_stack_m210 + 0x10) + 40, local_rsi, 0);
loc_00ADE0A1:
    result = RtlFreeAnsiString(v_stack_m1E8, *(uint64_t *)(v_stack_m210 + 0x10) + 40, local_rsi, 0);
    result = RtlFreeAnsiString(v_stack_m248, *(uint64_t *)(v_stack_m210 + 0x10) + 40, local_rsi, 0);
    result = RtlFreeAnsiString(v_stack_m230, *(uint64_t *)(v_stack_m210 + 0x10) + 40, local_rsi, 0);
    result = RtlFreeAnsiString(v_stack_m188, *(uint64_t *)(v_stack_m210 + 0x10) + 40, local_rsi, 0);
    result = RtlFreeAnsiString(v_stack_m1F8, *(uint64_t *)(v_stack_m210 + 0x10) + 40, local_rsi, 0);
    result = RtlFreeAnsiString(v_stack_m1D8, *(uint64_t *)(v_stack_m210 + 0x10) + 40, local_rsi, 0);
    result = RtlFreeAnsiString(v_stack_m1C8, *(uint64_t *)(v_stack_m210 + 0x10) + 40, local_rsi, 0);
    result = RtlFreeAnsiString(v_stack_m1B8, *(uint64_t *)(v_stack_m210 + 0x10) + 40, local_rsi, 0);
    result = RtlFreeAnsiString(v_stack_m220, *(uint64_t *)(v_stack_m210 + 0x10) + 40, local_rsi, 0);
    result = RtlFreeAnsiString(v_stack_m1A8, *(uint64_t *)(v_stack_m210 + 0x10) + 40, local_rsi, 0);
    Arg1 = (v_stack_m50) ^ (local_rsp);
    result = _security_check_cookie(Arg1, *(uint64_t *)(v_stack_m210 + 0x10) + 40, local_rsi, 0);
    local_rsp = (local_rsp) + (792);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x18` | `64` | `R` |
| `Arg3` | `+ 0x0` | `64` | `R` |
| `Arg3` | `+ 0x10` | `64` | `R` |
| `Arg3` | `+ 0x28` | `64` | `R` |
| `Arg3` | `+ 0x40` | `64` | `R` |
| `Arg3` | `+ 0x6C` | `32` | `R` |
| `Arg3` | `+ 0x70` | `64` | `R` |
| `Arg3` | `+ 0x78` | `16` | `R` |
| `Arg3` | `+ 0x7A` | `16` | `R` |
| `Arg3` | `+ 0x7C` | `16` | `R` |
| `Arg3` | `+ 0x7C` | `32` | `R` |
| `Arg3` | `+ 0xE0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00ADCDD4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
