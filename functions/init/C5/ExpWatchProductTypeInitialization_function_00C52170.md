# ExpWatchProductTypeInitialization

- RVA: `0x00C52170`–`0x00C52C1F` (길이 `2,735` bytes)
- VA: `0x0000000140C52170`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000D4AC0`
- 디코드: `629`개 명령, `2,735/2,735` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **66**; 고유 호출 대상: **19**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **38**

### Outgoing calls
- `0x00C521FC` → [ExpGetNtProductTypeFromLicenseValue](../../page/7C/ExpGetNtProductTypeFromLicenseValue_function_007C699C.md) (function, `0x007C699C`)
- `0x00C5220C` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00C52246` → [NtOpenKey](../../page/A4/NtOpenKey_function_00A45CA0.md) (function, `0x00A45CA0`)
- `0x00C5227A` → [ObReferenceObjectByHandle](../../page/86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x00C5229C` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C522AE` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00C522DF` → [NtQueryValueKey](../../page/8B/NtQueryValueKey_function_008B2A00.md) (function, `0x008B2A00`)
- `0x00C52315` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00C52329` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00C52350` → [NtQueryValueKey](../../page/8B/NtQueryValueKey_function_008B2A00.md) (function, `0x008B2A00`)
- `0x00C5236A` → [ExpLicenseWatchInitWorker](../C6/ExpLicenseWatchInitWorker_function_00C6CEE0.md) (function, `0x00C6CEE0`)
- `0x00C52389` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00C523D7` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00C5240D` → [NtOpenKey](../../page/A4/NtOpenKey_function_00A45CA0.md) (function, `0x00A45CA0`)
- `0x00C52437` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C5246D` → [ObReferenceObjectByHandle](../../page/86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x00C5248F` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C524A3` → [ExpUpdateProductSuiteTypeInRegistry](ExpUpdateProductSuiteTypeInRegistry_function_00C51BC0.md) (function, `0x00C51BC0`)
- `0x00C524B4` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00C524D1` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C52506` → [NtQueryValueKey](../../page/8B/NtQueryValueKey_function_008B2A00.md) (function, `0x008B2A00`)
- `0x00C5252D` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C5253F` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00C52569` → [NtQueryValueKey](../../page/8B/NtQueryValueKey_function_008B2A00.md) (function, `0x008B2A00`)
- `0x00C5258C` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C525B5` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C525DC` → [NtQueryValueKey](../../page/8B/NtQueryValueKey_function_008B2A00.md) (function, `0x008B2A00`)
- `0x00C525EE` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00C5262A` → [wcsncmp](../../text/50/wcsncmp_function_00501CA0.md) (function, `0x00501CA0`)
- `0x00C526A9` → [NtNotifyChangeKey](../../page/9D/NtNotifyChangeKey_function_009DC640.md) (function, `0x009DC640`)
- `0x00C526D3` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C526E4` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00C52718` → [NtOpenKey](../../page/A4/NtOpenKey_function_00A45CA0.md) (function, `0x00A45CA0`)
- `0x00C52779` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C5279D` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C527BB` → [NtQueryKey](../../page/86/NtQueryKey_function_008676E0.md) (function, `0x008676E0`)
- `0x00C527D9` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C5280C` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C5284E` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C52897` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C528C9` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C528DA` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00C528FF` → [NtEnumerateKey](../../page/8B/NtEnumerateKey_function_008B1F70.md) (function, `0x008B1F70`)
- `0x00C52936` → [wcscpy_s](../../text/50/wcscpy_s_function_005064B0.md) (function, `0x005064B0`)
- `0x00C5294F` → [wcscat_s](../../text/50/wcscat_s_function_00506410.md) (function, `0x00506410`)
- `0x00C52965` → [wcscat_s](../../text/50/wcscat_s_function_00506410.md) (function, `0x00506410`)
- `0x00C529C7` → [NtOpenKey](../../page/A4/NtOpenKey_function_00A45CA0.md) (function, `0x00A45CA0`)
- `0x00C529F8` → [NtQueryValueKey](../../page/8B/NtQueryValueKey_function_008B2A00.md) (function, `0x008B2A00`)
- `0x00C52A15` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C52A3F` → [wcscpy_s](../../text/50/wcscpy_s_function_005064B0.md) (function, `0x005064B0`)
- `0x00C52AA2` → [NtNotifyChangeKey](../../page/9D/NtNotifyChangeKey_function_009DC640.md) (function, `0x009DC640`)
- `0x00C52AC9` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C52AE9` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C52B05` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C52B22` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C52B3C` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C52B47` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00C52B51` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00C52B5D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00C52B67` → [NtClose](../../page/86/NtClose_function_00868870.md) (function, `0x00868870`)
- `0x00C52B8A` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C52BA7` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C52BC4` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C52BE5` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C52BFF` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C52C19` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)

### Direct callers
- [Phase1InitializationDiscard](../C1/Phase1InitializationDiscard_function_00C1C728.md) at `0x00C1D994`

### Static image references
- `0x00C52194` → RVA `0x00E0A740` (`.data`; read)
- `0x00C521A2` → RVA `0x00FC5008` (`ALMOSTRO`; read)
- `0x00C521E9` → RVA `0x00EF0139` (`.data`; write)
- `0x00C521F5` → RVA `0x00EF0138` (`.data`; write)
- `0x00C52201` → RVA `0x00B4AD60` (`PAGE`; read)
- `0x00C5223A` → RVA `0x00EF0130` (`.data`; read)
- `0x00C52253` → RVA `0x00FC6AC0` (`ALMOSTRO`; read)
- `0x00C522A2` → RVA `0x00B4AD68` (`PAGE`; read)
- `0x00C5231D` → RVA `0x00B4AE30` (`PAGE`; read)
- `0x00C5236F` → RVA `0x00FC4148` (`.data`; read)
- `0x00C52378` → RVA `0x00EFEE20` (`.data`; write)
- `0x00C523B0` → RVA `0x00B4AD78` (`PAGE`; read)
- `0x00C523B7` → RVA `0x006FFCA0` (`ExpWatchProductTypeWork`; read)
- `0x00C523C2` → RVA `0x00EFEDF0` (`.data`; write)
- `0x00C523C9` → RVA `0x00EFEDF8` (`.data`; write)
- `0x00C523D0` → RVA `0x00EFEDE0` (`.data`; write)
- `0x00C52401` → RVA `0x00EFEE18` (`.data`; read)
- `0x00C52416` → RVA `0x00EF0139` (`.data`; read)
- `0x00C5249C` → RVA `0x00EFEE28` (`.data`; write)
- `0x00C524A8` → RVA `0x00B4AD80` (`PAGE`; read)
- `0x00C524D6` → RVA `0x00EFEE00` (`.data`; write)
- `0x00C52533` → RVA `0x00B4ADA0` (`PAGE`; read)
- `0x00C52591` → RVA `0x00E61EA8` (`.data`; write)
- `0x00C525E5` → RVA `0x00E61EA8` (`.data`; read)
- `0x00C52607` → RVA `0x00B4AD88` (`PAGE`; read)
- `0x00C5261F` → RVA `0x00EFEE00` (`.data`; read)
- `0x00C52633` → RVA `0x00FC41C4` (`.data`; read)
- `0x00C5266B` → RVA `0x00EFEE08` (`.data`; read)
- `0x00C52677` → RVA `0x00EFEDE0` (`.data`; read)
- `0x00C52695` → RVA `0x00EFEDC0` (`.data`; read)
- `0x00C526D9` → RVA `0x00B4ADA8` (`PAGE`; read)
- `0x00C52872` → RVA `0x00EFEE0C` (`.data`; write)
- `0x00C5289E` → RVA `0x00EFEDD0` (`.data`; write)
- `0x00C528AA` → RVA `0x00EFEE0C` (`.data`; read)
- `0x00C528CF` → RVA `0x00B4ADB0` (`PAGE`; read)
- `0x00C52940` → RVA `0x00C7DCE0` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C5297C` → RVA `0x00EFEDD0` (`.data`; read)
- `0x00C52A6F` → RVA `0x007C6DB0` (`ExpWatchLicenseInfoWork`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **64**
  - `0x00C521FC` → [ExpGetNtProductTypeFromLicenseValue](../../page/7C/ExpGetNtProductTypeFromLicenseValue_function_007C699C.md) (`INIT` → `PAGE`)
  - `0x00C5220C` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`INIT` → `.text`)
  - `0x00C52246` → [NtOpenKey](../../page/A4/NtOpenKey_function_00A45CA0.md) (`INIT` → `PAGE`)
  - `0x00C5227A` → [ObReferenceObjectByHandle](../../page/86/ObReferenceObjectByHandle_function_00868DB0.md) (`INIT` → `PAGE`)
  - `0x00C5229C` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C522AE` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`INIT` → `.text`)
  - `0x00C522DF` → [NtQueryValueKey](../../page/8B/NtQueryValueKey_function_008B2A00.md) (`INIT` → `PAGE`)
  - `0x00C52315` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`INIT` → `.text`)
  - `0x00C52329` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`INIT` → `.text`)
  - `0x00C52350` → [NtQueryValueKey](../../page/8B/NtQueryValueKey_function_008B2A00.md) (`INIT` → `PAGE`)
  - `0x00C52389` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`INIT` → `.text`)
  - `0x00C523D7` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`INIT` → `.text`)
  - `0x00C5240D` → [NtOpenKey](../../page/A4/NtOpenKey_function_00A45CA0.md) (`INIT` → `PAGE`)
  - `0x00C52437` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C5246D` → [ObReferenceObjectByHandle](../../page/86/ObReferenceObjectByHandle_function_00868DB0.md) (`INIT` → `PAGE`)
  - `0x00C5248F` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C524B4` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`INIT` → `.text`)
  - `0x00C524D1` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C52506` → [NtQueryValueKey](../../page/8B/NtQueryValueKey_function_008B2A00.md) (`INIT` → `PAGE`)
  - `0x00C5252D` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C5253F` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`INIT` → `.text`)
  - `0x00C52569` → [NtQueryValueKey](../../page/8B/NtQueryValueKey_function_008B2A00.md) (`INIT` → `PAGE`)
  - `0x00C5258C` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C525B5` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C525DC` → [NtQueryValueKey](../../page/8B/NtQueryValueKey_function_008B2A00.md) (`INIT` → `PAGE`)
  - `0x00C525EE` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`INIT` → `POOLCODE`)
  - `0x00C5262A` → [wcsncmp](../../text/50/wcsncmp_function_00501CA0.md) (`INIT` → `.text`)
  - `0x00C526A9` → [NtNotifyChangeKey](../../page/9D/NtNotifyChangeKey_function_009DC640.md) (`INIT` → `PAGE`)
  - `0x00C526D3` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C526E4` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`INIT` → `.text`)
  - `0x00C52718` → [NtOpenKey](../../page/A4/NtOpenKey_function_00A45CA0.md) (`INIT` → `PAGE`)
  - `0x00C52779` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C5279D` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C527BB` → [NtQueryKey](../../page/86/NtQueryKey_function_008676E0.md) (`INIT` → `PAGE`)
  - `0x00C527D9` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C5280C` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C5284E` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C52897` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C528C9` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C528DA` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`INIT` → `.text`)
  - `0x00C528FF` → [NtEnumerateKey](../../page/8B/NtEnumerateKey_function_008B1F70.md) (`INIT` → `PAGE`)
  - `0x00C52936` → [wcscpy_s](../../text/50/wcscpy_s_function_005064B0.md) (`INIT` → `.text`)
  - `0x00C5294F` → [wcscat_s](../../text/50/wcscat_s_function_00506410.md) (`INIT` → `.text`)
  - `0x00C52965` → [wcscat_s](../../text/50/wcscat_s_function_00506410.md) (`INIT` → `.text`)
  - `0x00C529C7` → [NtOpenKey](../../page/A4/NtOpenKey_function_00A45CA0.md) (`INIT` → `PAGE`)
  - `0x00C529F8` → [NtQueryValueKey](../../page/8B/NtQueryValueKey_function_008B2A00.md) (`INIT` → `PAGE`)
  - `0x00C52A15` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C52A3F` → [wcscpy_s](../../text/50/wcscpy_s_function_005064B0.md) (`INIT` → `.text`)
  - `0x00C52AA2` → [NtNotifyChangeKey](../../page/9D/NtNotifyChangeKey_function_009DC640.md) (`INIT` → `PAGE`)
  - `0x00C52AC9` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C52AE9` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C52B05` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C52B22` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C52B3C` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C52B47` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`INIT` → `POOLCODE`)
  - `0x00C52B51` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`INIT` → `POOLCODE`)
  - `0x00C52B5D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`INIT` → `POOLCODE`)
  - `0x00C52B67` → [NtClose](../../page/86/NtClose_function_00868870.md) (`INIT` → `PAGE`)
  - `0x00C52B8A` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C52BA7` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C52BC4` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C52BE5` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C52BFF` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C52C19` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C52170  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00C52175  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
00C5217A  48 89 7C 24 18                  mov qword ptr [rsp + 0x18], rdi
00C5217F  55                              push rbp
00C52180  41 54                           push r12
00C52182  41 55                           push r13
00C52184  41 56                           push r14
00C52186  41 57                           push r15
00C52188  48 8D 6C 24 90                  lea rbp, [rsp - 0x70]
00C5218D  48 81 EC 70 01 00 00            sub rsp, 0x170
00C52194  48 8B 05 A5 85 1B 00            mov rax, qword ptr [rip + 0x1b85a5]
00C5219B  48 33 C4                        xor rax, rsp
00C5219E  48 89 45 60                     mov qword ptr [rbp + 0x60], rax
00C521A2  48 8B 05 5F 2E 37 00            mov rax, qword ptr [rip + 0x372e5f]
00C521A9  45 33 FF                        xor r15d, r15d
00C521AC  0F 57 C0                        xorps xmm0, xmm0
00C521AF  44 89 7C 24 7C                  mov dword ptr [rsp + 0x7c], r15d
00C521B4  0F 11 45 A8                     movups xmmword ptr [rbp - 0x58], xmm0
00C521B8  44 89 7D 94                     mov dword ptr [rbp - 0x6c], r15d
00C521BC  41 8B F7                        mov esi, r15d
00C521BF  44 89 7C 24 50                  mov dword ptr [rsp + 0x50], r15d
00C521C4  0F 57 C9                        xorps xmm1, xmm1
00C521C7  4C 89 7C 24 70                  mov qword ptr [rsp + 0x70], r15
00C521CC  45 8D 6F 01                     lea r13d, [r15 + 1]
00C521D0  0F 11 45 F8                     movups xmmword ptr [rbp - 8], xmm0
00C521D4  44 88 A8 68 02 00 00            mov byte ptr [rax + 0x268], r13b
00C521DB  48 8B 0D 26 2E 37 00            mov rcx, qword ptr [rip + 0x372e26]
00C521E2  48 81 C1 64 02 00 00            add rcx, 0x264
00C521E9  44 88 3D 49 DF 29 00            mov byte ptr [rip + 0x29df49], r15b
00C521F0  0F 11 4C 24 58                  movups xmmword ptr [rsp + 0x58], xmm1
00C521F5  44 88 3D 3C DF 29 00            mov byte ptr [rip + 0x29df3c], r15b
00C521FC  E8 9B 47 B7 FF                  call 0x1407c699c
00C52201  48 8B 15 58 8B EF FF            mov rdx, qword ptr [rip - 0x1074a8]
00C52208  48 8D 4D A8                     lea rcx, [rbp - 0x58]
00C5220C  E8 6F 85 7D FF                  call 0x14042a780
00C52211  48 8D 45 A8                     lea rax, [rbp - 0x58]
00C52215  4C 89 7D 80                     mov qword ptr [rbp - 0x80], r15
00C52219  0F 57 C0                        xorps xmm0, xmm0
00C5221C  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
00C52220  45 8D 67 30                     lea r12d, [r15 + 0x30]
00C52224  C7 45 90 40 02 00 00            mov dword ptr [rbp - 0x70], 0x240
00C5222B  4C 8D 44 24 78                  lea r8, [rsp + 0x78]
00C52230  44 89 64 24 78                  mov dword ptr [rsp + 0x78], r12d
00C52235  BA 1F 00 02 00                  mov edx, 0x2001f
00C5223A  48 8D 0D EF DE 29 00            lea rcx, [rip + 0x29deef]
00C52241  F3 0F 7F 45 98                  movdqu xmmword ptr [rbp - 0x68], xmm0
00C52246  E8 55 3A DF FF                  call 0x140a45ca0
00C5224B  85 C0                           test eax, eax
00C5224D  0F 88 B2 09 00 00               js 0x140c52c05
00C52253  4C 8B 05 66 48 37 00            mov r8, qword ptr [rip + 0x374866]
00C5225A  48 8D 44 24 68                  lea rax, [rsp + 0x68]
00C5225F  48 8B 0D CA DE 29 00            mov rcx, qword ptr [rip + 0x29deca]
00C52266  45 33 C9                        xor r9d, r9d
00C52269  4C 89 7C 24 28                  mov qword ptr [rsp + 0x28], r15
00C5226E  33 D2                           xor edx, edx
00C52270  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00C52275  4C 89 7C 24 68                  mov qword ptr [rsp + 0x68], r15
00C5227A  E8 31 6B C1 FF                  call 0x140868db0
00C5227F  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
00C52284  85 C0                           test eax, eax
00C52286  79 1A                           jns 0x140c522a2
00C52288  44 8B C0                        mov r8d, eax
00C5228B  41 8D 57 0B                     lea edx, [r15 + 0xb]
00C5228F  45 33 C9                        xor r9d, r9d
00C52292  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00C52297  41 8D 4C 24 6A                  lea ecx, [r12 + 0x6a]
00C5229C  E8 BF B3 8A FF                  call 0x1404fd660
00C522A1  CC                              int3
00C522A2  48 8B 15 BF 8A EF FF            mov rdx, qword ptr [rip - 0x107541]
00C522A9  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
00C522AE  E8 CD 84 7D FF                  call 0x14042a780
00C522B3  48 8B 0D 76 DE 29 00            mov rcx, qword ptr [rip + 0x29de76]
00C522BA  48 8D 44 24 50                  lea rax, [rsp + 0x50]
00C522BF  41 BE 48 00 00 00               mov r14d, 0x48
00C522C5  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00C522CA  4C 8D 4D 10                     lea r9, [rbp + 0x10]
00C522CE  44 89 74 24 20                  mov dword ptr [rsp + 0x20], r14d
00C522D3  48 8D 54 24 58                  lea rdx, [rsp + 0x58]
00C522D8  41 8D 5E BA                     lea ebx, [r14 - 0x46]
00C522DC  44 8B C3                        mov r8d, ebx
00C522DF  E8 1C 07 C6 FF                  call 0x1408b2a00
00C522E4  85 C0                           test eax, eax
00C522E6  0F 88 FF 08 00 00               js 0x140c52beb
00C522EC  44 39 6D 1C                     cmp dword ptr [rbp + 0x1c], r13d
00C522F0  74 06                           je 0x140c522f8
00C522F2  83 7D 1C 04                     cmp dword ptr [rbp + 0x1c], 4
00C522F6  75 25                           jne 0x140c5231d
00C522F8  48 8B 05 09 2D 37 00            mov rax, qword ptr [rip + 0x372d09]
00C522FF  BA 44 66 6C 74                  mov edx, 0x746c6644
00C52304  48 8B CF                        mov rcx, rdi
00C52307  44 88 2D 2B DE 29 00            mov byte ptr [rip + 0x29de2b], r13b
00C5230E  44 88 B8 68 02 00 00            mov byte ptr [rax + 0x268], r15b
00C52315  E8 C6 55 6A FF                  call 0x1402f78e0
00C5231A  49 8B FF                        mov rdi, r15
00C5231D  48 8B 15 0C 8B EF FF            mov rdx, qword ptr [rip - 0x1074f4]
00C52324  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
00C52329  E8 52 84 7D FF                  call 0x14042a780
00C5232E  48 8B 0D FB DD 29 00            mov rcx, qword ptr [rip + 0x29ddfb]
00C52335  48 8D 44 24 50                  lea rax, [rsp + 0x50]
00C5233A  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00C5233F  4C 8D 4D 10                     lea r9, [rbp + 0x10]
00C52343  44 8B C3                        mov r8d, ebx
00C52346  44 89 74 24 20                  mov dword ptr [rsp + 0x20], r14d
00C5234B  48 8D 54 24 58                  lea rdx, [rsp + 0x58]
00C52350  E8 AB 06 C6 FF                  call 0x1408b2a00
00C52355  85 C0                           test eax, eax
00C52357  0F 88 74 08 00 00               js 0x140c52bd1
00C5235D  44 39 6D 1C                     cmp dword ptr [rbp + 0x1c], r13d
00C52361  75 07                           jne 0x140c5236a
00C52363  44 88 2D CE DD 29 00            mov byte ptr [rip + 0x29ddce], r13b
00C5236A  E8 71 AB 01 00                  call 0x140c6cee0
00C5236F  44 38 3D D2 1D 37 00            cmp byte ptr [rip + 0x371dd2], r15b
00C52376  74 38                           je 0x140c523b0
00C52378  48 89 3D A1 CA 2A 00            mov qword ptr [rip + 0x2acaa1], rdi
00C5237F  41 8A C5                        mov al, r13b
00C52382  48 8B 4D 60                     mov rcx, qword ptr [rbp + 0x60]
00C52386  48 33 CC                        xor rcx, rsp
00C52389  E8 B2 A2 A5 FF                  call 0x1406ac640
00C5238E  4C 8D 9C 24 70 01 00 00         lea r11, [rsp + 0x170]
00C52396  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
00C5239A  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
00C5239E  49 8B 7B 40                     mov rdi, qword ptr [r11 + 0x40]
00C523A2  49 8B E3                        mov rsp, r11
00C523A5  41 5F                           pop r15
00C523A7  41 5E                           pop r14
00C523A9  41 5D                           pop r13
00C523AB  41 5C                           pop r12
00C523AD  5D                              pop rbp
00C523AE  C3                              ret
00C523AF  CC                              int3
00C523B0  48 8B 15 C1 89 EF FF            mov rdx, qword ptr [rip - 0x10763f]
00C523B7  48 8D 05 E2 D8 AA FF            lea rax, [rip - 0x55271e]
00C523BE  48 8D 4D A8                     lea rcx, [rbp - 0x58]
00C523C2  48 89 05 27 CA 2A 00            mov qword ptr [rip + 0x2aca27], rax
00C523C9  4C 89 3D 28 CA 2A 00            mov qword ptr [rip + 0x2aca28], r15
00C523D0  4C 89 3D 09 CA 2A 00            mov qword ptr [rip + 0x2aca09], r15
00C523D7  E8 A4 83 7D FF                  call 0x14042a780
00C523DC  48 8D 45 A8                     lea rax, [rbp - 0x58]
00C523E0  44 89 64 24 78                  mov dword ptr [rsp + 0x78], r12d
00C523E5  0F 57 C0                        xorps xmm0, xmm0
00C523E8  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
00C523EC  4C 8D 44 24 78                  lea r8, [rsp + 0x78]
00C523F1  4C 89 7D 80                     mov qword ptr [rbp - 0x80], r15
00C523F5  BA 1F 00 02 00                  mov edx, 0x2001f
00C523FA  C7 45 90 40 02 00 00            mov dword ptr [rbp - 0x70], 0x240
00C52401  48 8D 0D 10 CA 2A 00            lea rcx, [rip + 0x2aca10]
00C52408  F3 0F 7F 45 98                  movdqu xmmword ptr [rbp - 0x68], xmm0
00C5240D  E8 8E 38 DF FF                  call 0x140a45ca0
00C52412  85 C0                           test eax, eax
00C52414  79 27                           jns 0x140c5243d
00C52416  44 38 3D 1C DD 29 00            cmp byte ptr [rip + 0x29dd1c], r15b
00C5241D  0F 85 A7 07 00 00               jne 0x140c52bca
00C52423  45 33 C9                        xor r9d, r9d
00C52426  44 8B C0                        mov r8d, eax
00C52429  B9 9A 00 00 00                  mov ecx, 0x9a
00C5242E  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00C52433  41 8D 51 06                     lea edx, [r9 + 6]
00C52437  E8 24 B2 8A FF                  call 0x1404fd660
00C5243C  CC                              int3
00C5243D  44 38 3D F5 DC 29 00            cmp byte ptr [rip + 0x29dcf5], r15b
00C52444  75 4F                           jne 0x140c52495
00C52446  4C 8B 05 73 46 37 00            mov r8, qword ptr [rip + 0x374673]
00C5244D  48 8D 44 24 68                  lea rax, [rsp + 0x68]
00C52452  48 8B 0D BF C9 2A 00            mov rcx, qword ptr [rip + 0x2ac9bf]
00C52459  45 33 C9                        xor r9d, r9d
00C5245C  4C 89 7C 24 28                  mov qword ptr [rsp + 0x28], r15
00C52461  33 D2                           xor edx, edx
00C52463  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00C52468  4C 89 7C 24 68                  mov qword ptr [rsp + 0x68], r15
00C5246D  E8 3E 69 C1 FF                  call 0x140868db0
00C52472  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
00C52477  85 C0                           test eax, eax
00C52479  79 1A                           jns 0x140c52495
00C5247B  45 33 C9                        xor r9d, r9d
00C5247E  44 8B C0                        mov r8d, eax
00C52481  B9 9A 00 00 00                  mov ecx, 0x9a
00C52486  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00C5248B  41 8D 51 0C                     lea edx, [r9 + 0xc]
00C5248F  E8 CC B1 8A FF                  call 0x1404fd660
00C52494  CC                              int3
00C52495  48 89 3D 84 C9 2A 00            mov qword ptr [rip + 0x2ac984], rdi
00C5249C  48 89 35 85 C9 2A 00            mov qword ptr [rip + 0x2ac985], rsi
00C524A3  E8 18 F7 FF FF                  call 0x140c51bc0
00C524A8  48 8B 15 D1 88 EF FF            mov rdx, qword ptr [rip - 0x10772f]
00C524AF  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
00C524B4  E8 C7 82 7D FF                  call 0x14042a780
00C524B9  BF 4B 65 79 20                  mov edi, 0x2079654b
00C524BE  BE 22 00 00 00                  mov esi, 0x22
00C524C3  41 BE 00 01 00 00               mov r14d, 0x100
00C524C9  44 8B C7                        mov r8d, edi
00C524CC  8B D6                           mov edx, esi
00C524CE  41 8B CE                        mov ecx, r14d
00C524D1  E8 1A FC F2 FF                  call 0x140b820f0
00C524D6  48 89 05 23 C9 2A 00            mov qword ptr [rip + 0x2ac923], rax
00C524DD  48 85 C0                        test rax, rax
00C524E0  0F 84 E4 06 00 00               je 0x140c52bca
00C524E6  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
00C524EB  4C 8B C8                        mov r9, rax
00C524EE  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
00C524F3  48 8D 54 24 58                  lea rdx, [rsp + 0x58]
00C524F8  48 8B 0D 19 C9 2A 00            mov rcx, qword ptr [rip + 0x2ac919]
00C524FF  44 8B C3                        mov r8d, ebx
00C52502  89 74 24 20                     mov dword ptr [rsp + 0x20], esi
00C52506  E8 F5 04 C6 FF                  call 0x1408b2a00
00C5250B  85 C0                           test eax, eax
00C5250D  79 24                           jns 0x140c52533
00C5250F  44 38 3D 23 DC 29 00            cmp byte ptr [rip + 0x29dc23], r15b
00C52516  0F 85 AE 06 00 00               jne 0x140c52bca
00C5251C  44 8B C0                        mov r8d, eax
00C5251F  8D 56 E5                        lea edx, [rsi - 0x1b]
00C52522  45 33 C9                        xor r9d, r9d
00C52525  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00C5252A  8D 4E 78                        lea ecx, [rsi + 0x78]
00C5252D  E8 2E B1 8A FF                  call 0x1404fd660
00C52532  CC                              int3
00C52533  48 8B 15 66 88 EF FF            mov rdx, qword ptr [rip - 0x10779a]
00C5253A  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
00C5253F  E8 3C 82 7D FF                  call 0x14042a780
00C52544  48 8B 0D CD C8 2A 00            mov rcx, qword ptr [rip + 0x2ac8cd]
00C5254B  48 8D 44 24 50                  lea rax, [rsp + 0x50]
00C52550  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00C52555  4C 8D 4D F8                     lea r9, [rbp - 8]
00C52559  44 8B C3                        mov r8d, ebx
00C5255C  C7 44 24 20 10 00 00 00         mov dword ptr [rsp + 0x20], 0x10
00C52564  48 8D 54 24 58                  lea rdx, [rsp + 0x58]
00C52569  E8 92 04 C6 FF                  call 0x1408b2a00
00C5256E  3D 05 00 00 80                  cmp eax, 0x80000005
00C52573  0F 85 8E 00 00 00               jne 0x140c52607
00C52579  8B 44 24 50                     mov eax, dword ptr [rsp + 0x50]
00C5257D  44 8B C7                        mov r8d, edi
00C52580  83 C0 10                        add eax, 0x10
00C52583  49 8B CE                        mov rcx, r14
00C52586  8B D0                           mov edx, eax
00C52588  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
00C5258C  E8 5F FB F2 FF                  call 0x140b820f0
00C52591  48 89 05 10 F9 20 00            mov qword ptr [rip + 0x20f910], rax
00C52598  4C 8B C8                        mov r9, rax
00C5259B  48 85 C0                        test rax, rax
00C5259E  75 1B                           jne 0x140c525bb
00C525A0  44 8B 44 24 50                  mov r8d, dword ptr [rsp + 0x50]
00C525A5  8D 50 14                        lea edx, [rax + 0x14]
00C525A8  4C 8B CB                        mov r9, rbx
00C525AB  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00C525B0  B9 9A 00 00 00                  mov ecx, 0x9a
00C525B5  E8 A6 B0 8A FF                  call 0x1404fd660
00C525BA  CC                              int3
00C525BB  48 8B 0D 56 C8 2A 00            mov rcx, qword ptr [rip + 0x2ac856]
00C525C2  48 8D 44 24 50                  lea rax, [rsp + 0x50]
00C525C7  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00C525CC  48 8D 54 24 58                  lea rdx, [rsp + 0x58]
00C525D1  8B 44 24 50                     mov eax, dword ptr [rsp + 0x50]
00C525D5  44 8B C3                        mov r8d, ebx
00C525D8  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00C525DC  E8 1F 04 C6 FF                  call 0x1408b2a00
00C525E1  85 C0                           test eax, eax
00C525E3  79 22                           jns 0x140c52607
00C525E5  48 8B 0D BC F8 20 00            mov rcx, qword ptr [rip + 0x20f8bc]
00C525EC  33 D2                           xor edx, edx
00C525EE  E8 7D 02 F3 FF                  call 0x140b82870
00C525F3  44 38 3D 3F DB 29 00            cmp byte ptr [rip + 0x29db3f], r15b
00C525FA  4C 89 3D A7 F8 20 00            mov qword ptr [rip + 0x20f8a7], r15
00C52601  0F 85 C3 05 00 00               jne 0x140c52bca
00C52607  48 8B 0D 7A 87 EF FF            mov rcx, qword ptr [rip - 0x107886]
00C5260E  48 83 CE FF                     or rsi, 0xffffffffffffffff
00C52612  4C 8B C6                        mov r8, rsi
00C52615  49 FF C0                        inc r8
00C52618  66 46 39 3C 41                  cmp word ptr [rcx + r8*2], r15w
00C5261D  75 F6                           jne 0x140c52615
00C5261F  48 8B 15 DA C7 2A 00            mov rdx, qword ptr [rip + 0x2ac7da]
00C52626  48 83 C2 0C                     add rdx, 0xc
00C5262A  E8 71 F6 8A FF                  call 0x140501ca0
00C5262F  85 C0                           test eax, eax
00C52631  75 31                           jne 0x140c52664
00C52633  83 3D 8A 1B 37 00 03            cmp dword ptr [rip + 0x371b8a], 3
00C5263A  75 28                           jne 0x140c52664
00C5263C  44 38 3D F6 DA 29 00            cmp byte ptr [rip + 0x29daf6], r15b
00C52643  75 1F                           jne 0x140c52664
00C52645  48 8B 05 BC 29 37 00            mov rax, qword ptr [rip + 0x3729bc]
00C5264C  44 88 A8 68 02 00 00            mov byte ptr [rax + 0x268], r13b
00C52653  48 8B 05 AE 29 37 00            mov rax, qword ptr [rip + 0x3729ae]
00C5265A  C7 80 64 02 00 00 03 00 00 00   mov dword ptr [rax + 0x264], 3
00C52664  48 8B 0D AD C7 2A 00            mov rcx, qword ptr [rip + 0x2ac7ad]
00C5266B  48 8D 05 96 C7 2A 00            lea rax, [rip + 0x2ac796]
00C52672  44 88 6C 24 48                  mov byte ptr [rsp + 0x48], r13b
00C52677  4C 8D 05 62 C7 2A 00            lea r8, [rip + 0x2ac762]
00C5267E  C7 44 24 40 04 00 00 00         mov dword ptr [rsp + 0x40], 4
00C52686  4D 8B CD                        mov r9, r13
00C52689  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00C5268E  33 D2                           xor edx, edx
00C52690  44 88 7C 24 30                  mov byte ptr [rsp + 0x30], r15b
00C52695  48 8D 05 24 C7 2A 00            lea rax, [rip + 0x2ac724]
00C5269C  C7 44 24 28 05 00 00 10         mov dword ptr [rsp + 0x28], 0x10000005
00C526A4  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00C526A9  E8 92 9F D8 FF                  call 0x1409dc640
00C526AE  85 C0                           test eax, eax
00C526B0  79 27                           jns 0x140c526d9
00C526B2  44 38 3D 80 DA 29 00            cmp byte ptr [rip + 0x29da80], r15b
00C526B9  0F 85 0B 05 00 00               jne 0x140c52bca
00C526BF  45 33 C9                        xor r9d, r9d
00C526C2  44 8B C0                        mov r8d, eax
00C526C5  B9 9A 00 00 00                  mov ecx, 0x9a
00C526CA  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00C526CF  41 8D 51 08                     lea edx, [r9 + 8]
00C526D3  E8 88 AF 8A FF                  call 0x1404fd660
00C526D8  CC                              int3
00C526D9  48 8B 15 C8 86 EF FF            mov rdx, qword ptr [rip - 0x107938]
00C526E0  48 8D 4D A8                     lea rcx, [rbp - 0x58]
00C526E4  E8 97 80 7D FF                  call 0x14042a780
00C526E9  48 8D 45 A8                     lea rax, [rbp - 0x58]
00C526ED  44 89 64 24 78                  mov dword ptr [rsp + 0x78], r12d
00C526F2  0F 57 C0                        xorps xmm0, xmm0
00C526F5  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
00C526F9  4C 8D 44 24 78                  lea r8, [rsp + 0x78]
00C526FE  4C 89 7D 80                     mov qword ptr [rbp - 0x80], r15
00C52702  BA 19 00 02 00                  mov edx, 0x20019
00C52707  C7 45 90 40 02 00 00            mov dword ptr [rbp - 0x70], 0x240
00C5270E  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
00C52713  F3 0F 7F 45 98                  movdqu xmmword ptr [rbp - 0x68], xmm0
00C52718  E8 83 35 DF FF                  call 0x140a45ca0
00C5271D  85 C0                           test eax, eax
00C5271F  0F 88 5A FC FF FF               js 0x140c5237f
00C52725  48 8B 0D 7C 86 EF FF            mov rcx, qword ptr [rip - 0x107984]
00C5272C  0F 57 C0                        xorps xmm0, xmm0
00C5272F  0F 57 C9                        xorps xmm1, xmm1
00C52732  44 89 7C 24 68                  mov dword ptr [rsp + 0x68], r15d
00C52737  0F 11 45 C8                     movups xmmword ptr [rbp - 0x38], xmm0
00C5273B  45 8A F7                        mov r14b, r15b
00C5273E  48 8B C6                        mov rax, rsi
00C52741  0F 11 45 D8                     movups xmmword ptr [rbp - 0x28], xmm0
00C52745  0F 11 45 E8                     movups xmmword ptr [rbp - 0x18], xmm0
00C52749  0F 11 44 24 58                  movups xmmword ptr [rsp + 0x58], xmm0
00C5274E  0F 11 4D B8                     movups xmmword ptr [rbp - 0x48], xmm1
00C52752  48 FF C0                        inc rax
00C52755  66 44 39 3C 41                  cmp word ptr [rcx + rax*2], r15w
00C5275A  75 F6                           jne 0x140c52752
00C5275C  BE 40 00 00 00                  mov esi, 0x40
00C52761  44 8B C7                        mov r8d, edi
00C52764  66 03 C6                        add ax, si
00C52767  8B CE                           mov ecx, esi
00C52769  66 03 C0                        add ax, ax
00C5276C  0F B7 D0                        movzx edx, ax
00C5276F  66 89 54 24 58                  mov word ptr [rsp + 0x58], dx
00C52774  66 89 54 24 5A                  mov word ptr [rsp + 0x5a], dx
00C52779  E8 72 F9 F2 FF                  call 0x140b820f0
00C5277E  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00C52783  48 85 C0                        test rax, rax
00C52786  75 1B                           jne 0x140c527a3
00C52788  44 0F B7 44 24 58               movzx r8d, word ptr [rsp + 0x58]
00C5278E  8D 56 D4                        lea edx, [rsi - 0x2c]
00C52791  8D 4E 5A                        lea ecx, [rsi + 0x5a]
00C52794  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00C52799  44 8D 4E C3                     lea r9d, [rsi - 0x3d]
00C5279D  E8 BE AE 8A FF                  call 0x1404fd660
00C527A2  CC                              int3
00C527A3  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
00C527A8  48 8D 44 24 68                  lea rax, [rsp + 0x68]
00C527AD  45 8B CC                        mov r9d, r12d
00C527B0  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00C527B5  4C 8D 45 C8                     lea r8, [rbp - 0x38]
00C527B9  8B D3                           mov edx, ebx
00C527BB  E8 20 4F C1 FF                  call 0x1408676e0
00C527C0  85 C0                           test eax, eax
00C527C2  79 1B                           jns 0x140c527df
00C527C4  4C 63 C0                        movsxd r8, eax
00C527C7  4D 8B CD                        mov r9, r13
00C527CA  BA 13 00 00 00                  mov edx, 0x13
00C527CF  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00C527D4  B9 9A 00 00 00                  mov ecx, 0x9a
00C527D9  E8 82 AE 8A FF                  call 0x1404fd660
00C527DE  CC                              int3
00C527DF  8B 45 E0                        mov eax, dword ptr [rbp - 0x20]
00C527E2  44 8D 24 45 38 00 00 00         lea r12d, [rax*2 + 0x38]
00C527EA  41 8B FC                        mov edi, r12d
00C527ED  44 3B E0                        cmp r12d, eax
00C527F0  72 0B                           jb 0x140c527fd
00C527F2  8D 48 10                        lea ecx, [rax + 0x10]
00C527F5  48 03 C9                        add rcx, rcx
00C527F8  48 3B F9                        cmp rdi, rcx
00C527FB  73 03                           jae 0x140c52800
00C527FD  45 8A F5                        mov r14b, r13b
00C52800  41 B8 4B 65 79 20               mov r8d, 0x2079654b
00C52806  48 8B D7                        mov rdx, rdi
00C52809  48 8B CE                        mov rcx, rsi
00C5280C  E8 DF F8 F2 FF                  call 0x140b820f0
00C52811  48 8B F0                        mov rsi, rax
00C52814  48 85 C0                        test rax, rax
00C52817  0F 84 90 03 00 00               je 0x140c52bad
00C5281D  45 84 F6                        test r14b, r14b
00C52820  0F 85 87 03 00 00               jne 0x140c52bad
00C52826  8B 4D F0                        mov ecx, dword ptr [rbp - 0x10]
00C52829  41 B9 01 00 00 00               mov r9d, 1
00C5282F  41 0F B6 FE                     movzx edi, r14b
00C52833  41 B8 4B 65 79 20               mov r8d, 0x2079654b
00C52839  44 8D 69 20                     lea r13d, [rcx + 0x20]
00C5283D  44 3B E9                        cmp r13d, ecx
00C52840  41 8B D5                        mov edx, r13d
00C52843  41 8D 49 3F                     lea ecx, [r9 + 0x3f]
00C52847  45 8B F5                        mov r14d, r13d
00C5284A  41 0F 42 F9                     cmovb edi, r9d
00C5284E  E8 9D F8 F2 FF                  call 0x140b820f0
00C52853  33 D2                           xor edx, edx
00C52855  4C 8B F8                        mov r15, rax
00C52858  48 85 C0                        test rax, rax
00C5285B  0F 84 2F 03 00 00               je 0x140c52b90
00C52861  40 84 FF                        test dil, dil
00C52864  0F 85 26 03 00 00               jne 0x140c52b90
00C5286A  8B 4D DC                        mov ecx, dword ptr [rbp - 0x24]
00C5286D  B8 FF FF FF FF                  mov eax, 0xffffffff
00C52872  89 0D 94 C5 2A 00               mov dword ptr [rip + 0x2ac594], ecx
00C52878  4C 8D 04 89                     lea r8, [rcx + rcx*4]
00C5287C  49 C1 E0 04                     shl r8, 4
00C52880  4C 3B C0                        cmp r8, rax
00C52883  0F 87 EE 02 00 00               ja 0x140c52b77
00C52889  41 8B D0                        mov edx, r8d
00C5288C  B9 40 00 00 00                  mov ecx, 0x40
00C52891  41 B8 4B 65 79 20               mov r8d, 0x2079654b
00C52897  E8 54 F8 F2 FF                  call 0x140b820f0
00C5289C  33 FF                           xor edi, edi
00C5289E  48 89 05 2B C5 2A 00            mov qword ptr [rip + 0x2ac52b], rax
00C528A5  48 85 C0                        test rax, rax
00C528A8  75 25                           jne 0x140c528cf
00C528AA  8B 05 5C C5 2A 00               mov eax, dword ptr [rip + 0x2ac55c]
00C528B0  8D 57 14                        lea edx, [rdi + 0x14]
00C528B3  B9 9A 00 00 00                  mov ecx, 0x9a
00C528B8  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00C528BD  44 8D 4F 06                     lea r9d, [rdi + 6]
00C528C1  4C 8D 04 80                     lea r8, [rax + rax*4]
00C528C5  49 C1 E0 04                     shl r8, 4
00C528C9  E8 92 AD 8A FF                  call 0x1404fd660
00C528CE  CC                              int3
00C528CF  48 8B 15 DA 84 EF FF            mov rdx, qword ptr [rip - 0x107b26]
00C528D6  48 8D 4D B8                     lea rcx, [rbp - 0x48]
00C528DA  E8 A1 7E 7D FF                  call 0x14042a780
00C528DF  44 8B F7                        mov r14d, edi
00C528E2  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
00C528E7  48 8D 44 24 68                  lea rax, [rsp + 0x68]
00C528EC  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00C528F1  4C 8B CE                        mov r9, rsi
00C528F4  45 33 C0                        xor r8d, r8d
00C528F7  44 89 64 24 20                  mov dword ptr [rsp + 0x20], r12d
00C528FC  41 8B D6                        mov edx, r14d
00C528FF  E8 6C F6 C5 FF                  call 0x1408b1f70
00C52904  3D 1A 00 00 80                  cmp eax, 0x8000001a
00C52909  0F 84 33 02 00 00               je 0x140c52b42
00C5290F  85 C0                           test eax, eax
00C52911  0F 88 11 02 00 00               js 0x140c52b28
00C52917  8B 46 0C                        mov eax, dword ptr [rsi + 0xc]
00C5291A  4C 8B 05 87 84 EF FF            mov r8, qword ptr [rip - 0x107b79]
00C52921  48 D1 E8                        shr rax, 1
00C52924  66 89 7C 46 10                  mov word ptr [rsi + rax*2 + 0x10], di
00C52929  0F B7 54 24 5A                  movzx edx, word ptr [rsp + 0x5a]
00C5292E  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
00C52933  48 D1 EA                        shr rdx, 1
00C52936  E8 75 3B 8B FF                  call 0x1405064b0
00C5293B  0F B7 54 24 5A                  movzx edx, word ptr [rsp + 0x5a]
00C52940  4C 8D 05 99 B3 02 00            lea r8, [rip + 0x2b399]
00C52947  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
00C5294C  48 D1 EA                        shr rdx, 1
00C5294F  E8 BC 3A 8B FF                  call 0x140506410
00C52954  0F B7 54 24 5A                  movzx edx, word ptr [rsp + 0x5a]
00C52959  4C 8D 46 10                     lea r8, [rsi + 0x10]
00C5295D  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
00C52962  48 D1 EA                        shr rdx, 1
00C52965  E8 A6 3A 8B FF                  call 0x140506410
00C5296A  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
00C5296F  48 83 C8 FF                     or rax, 0xffffffffffffffff
00C52973  48 FF C0                        inc rax
00C52976  66 39 3C 41                     cmp word ptr [rcx + rax*2], di
00C5297A  75 F7                           jne 0x140c52973
00C5297C  48 8B 0D 4D C4 2A 00            mov rcx, qword ptr [rip + 0x2ac44d]
00C52983  4C 8D 44 24 78                  lea r8, [rsp + 0x78]
00C52988  66 03 C0                        add ax, ax
00C5298B  48 89 7D 80                     mov qword ptr [rbp - 0x80], rdi
00C5298F  66 89 44 24 58                  mov word ptr [rsp + 0x58], ax
00C52994  0F 57 C0                        xorps xmm0, xmm0
00C52997  48 8D 44 24 58                  lea rax, [rsp + 0x58]
00C5299C  C7 44 24 78 30 00 00 00         mov dword ptr [rsp + 0x78], 0x30
00C529A4  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
00C529A8  BA 1F 00 02 00                  mov edx, 0x2001f
00C529AD  41 8B C6                        mov eax, r14d
00C529B0  C7 45 90 40 02 00 00            mov dword ptr [rbp - 0x70], 0x240
00C529B7  F3 0F 7F 45 98                  movdqu xmmword ptr [rbp - 0x68], xmm0
00C529BC  48 8D 3C 80                     lea rdi, [rax + rax*4]
00C529C0  48 C1 E7 04                     shl rdi, 4
00C529C4  48 03 CF                        add rcx, rdi
00C529C7  E8 D4 32 DF FF                  call 0x140a45ca0
00C529CC  85 C0                           test eax, eax
00C529CE  0F 88 37 01 00 00               js 0x140c52b0b
00C529D4  48 8B 0D F5 C3 2A 00            mov rcx, qword ptr [rip + 0x2ac3f5]
00C529DB  48 8D 44 24 68                  lea rax, [rsp + 0x68]
00C529E0  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00C529E5  48 8D 55 B8                     lea rdx, [rbp - 0x48]
00C529E9  4D 8B CF                        mov r9, r15
00C529EC  44 89 6C 24 20                  mov dword ptr [rsp + 0x20], r13d
00C529F1  44 8B C3                        mov r8d, ebx
00C529F4  48 8B 0C 0F                     mov rcx, qword ptr [rdi + rcx]
00C529F8  E8 03 00 C6 FF                  call 0x1408b2a00
00C529FD  85 C0                           test eax, eax
00C529FF  0F 88 EA 00 00 00               js 0x140c52aef
00C52A05  0F B7 54 24 58                  movzx edx, word ptr [rsp + 0x58]
00C52A0A  B9 40 00 00 00                  mov ecx, 0x40
00C52A0F  41 B8 4B 65 79 20               mov r8d, 0x2079654b
00C52A15  E8 D6 F6 F2 FF                  call 0x140b820f0
00C52A1A  48 8B 0D AF C3 2A 00            mov rcx, qword ptr [rip + 0x2ac3af]
00C52A21  48 89 44 0F 10                  mov qword ptr [rdi + rcx + 0x10], rax
00C52A26  48 85 C0                        test rax, rax
00C52A29  0F 84 A0 00 00 00               je 0x140c52acf
00C52A2F  0F B7 54 24 58                  movzx edx, word ptr [rsp + 0x58]
00C52A34  48 8B C8                        mov rcx, rax
00C52A37  4C 8B 44 24 60                  mov r8, qword ptr [rsp + 0x60]
00C52A3C  48 D1 EA                        shr rdx, 1
00C52A3F  E8 6C 3A 8B FF                  call 0x1405064b0
00C52A44  41 8B 47 0C                     mov eax, dword ptr [r15 + 0xc]
00C52A48  48 8B 0D 81 C3 2A 00            mov rcx, qword ptr [rip + 0x2ac381]
00C52A4F  48 03 CF                        add rcx, rdi
00C52A52  33 FF                           xor edi, edi
00C52A54  89 41 08                        mov dword ptr [rcx + 8], eax
00C52A57  4C 8D 41 18                     lea r8, [rcx + 0x18]
00C52A5B  48 8D 51 38                     lea rdx, [rcx + 0x38]
00C52A5F  49 89 48 18                     mov qword ptr [r8 + 0x18], rcx
00C52A63  44 8D 4F 01                     lea r9d, [rdi + 1]
00C52A67  49 89 38                        mov qword ptr [r8], rdi
00C52A6A  44 88 4C 24 48                  mov byte ptr [rsp + 0x48], r9b
00C52A6F  48 8D 05 3A 43 B7 FF            lea rax, [rip - 0x48bcc6]
00C52A76  C7 44 24 40 04 00 00 00         mov dword ptr [rsp + 0x40], 4
00C52A7E  49 89 40 10                     mov qword ptr [r8 + 0x10], rax
00C52A82  48 8D 41 48                     lea rax, [rcx + 0x48]
00C52A86  48 8B 09                        mov rcx, qword ptr [rcx]
00C52A89  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00C52A8E  44 88 4C 24 30                  mov byte ptr [rsp + 0x30], r9b
00C52A93  C7 44 24 28 05 00 00 10         mov dword ptr [rsp + 0x28], 0x10000005
00C52A9B  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00C52AA0  33 D2                           xor edx, edx
00C52AA2  E8 99 9B D8 FF                  call 0x1409dc640
00C52AA7  85 C0                           test eax, eax
00C52AA9  78 08                           js 0x140c52ab3
00C52AAB  41 FF C6                        inc r14d
00C52AAE  E9 2F FE FF FF                  jmp 0x140c528e2
00C52AB3  BA 18 00 00 00                  mov edx, 0x18
00C52AB8  4C 63 C0                        movsxd r8, eax
00C52ABB  B9 9A 00 00 00                  mov ecx, 0x9a
00C52AC0  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00C52AC5  44 8D 4A E9                     lea r9d, [rdx - 0x17]
00C52AC9  E8 92 AB 8A FF                  call 0x1404fd660
00C52ACE  CC                              int3
00C52ACF  44 0F B7 44 24 58               movzx r8d, word ptr [rsp + 0x58]
00C52AD5  BA 14 00 00 00                  mov edx, 0x14
00C52ADA  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
00C52AE0  B9 9A 00 00 00                  mov ecx, 0x9a
00C52AE5  44 8D 4A F3                     lea r9d, [rdx - 0xd]
00C52AE9  E8 72 AB 8A FF                  call 0x1404fd660
00C52AEE  CC                              int3
00C52AEF  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
00C52AF5  4C 8B CB                        mov r9, rbx
00C52AF8  4C 63 C0                        movsxd r8, eax
00C52AFB  BA 13 00 00 00                  mov edx, 0x13
00C52B00  B9 9A 00 00 00                  mov ecx, 0x9a
00C52B05  E8 56 AB 8A FF                  call 0x1404fd660
00C52B0A  CC                              int3
00C52B0B  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
00C52B11  BA 16 00 00 00                  mov edx, 0x16
00C52B16  4C 63 C0                        movsxd r8, eax
00C52B19  B9 9A 00 00 00                  mov ecx, 0x9a
00C52B1E  44 8D 4A EB                     lea r9d, [rdx - 0x15]
00C52B22  E8 39 AB 8A FF                  call 0x1404fd660
00C52B27  CC                              int3
00C52B28  45 33 C9                        xor r9d, r9d
00C52B2B  4C 63 C0                        movsxd r8, eax
00C52B2E  B9 9A 00 00 00                  mov ecx, 0x9a
00C52B33  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00C52B38  41 8D 51 1A                     lea edx, [r9 + 0x1a]
00C52B3C  E8 1F AB 8A FF                  call 0x1404fd660
00C52B41  CC                              int3
00C52B42  33 D2                           xor edx, edx
00C52B44  48 8B CE                        mov rcx, rsi
00C52B47  E8 24 FD F2 FF                  call 0x140b82870
00C52B4C  33 D2                           xor edx, edx
00C52B4E  49 8B CF                        mov rcx, r15
00C52B51  E8 1A FD F2 FF                  call 0x140b82870
00C52B56  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
00C52B5B  33 D2                           xor edx, edx
00C52B5D  E8 0E FD F2 FF                  call 0x140b82870
00C52B62  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
00C52B67  E8 04 5D C1 FF                  call 0x140868870
00C52B6C  41 BD 01 00 00 00               mov r13d, 1
00C52B72  E9 08 F8 FF FF                  jmp 0x140c5237f
00C52B77  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00C52B7C  B9 9A 00 00 00                  mov ecx, 0x9a
00C52B81  BA 14 00 00 00                  mov edx, 0x14
00C52B86  44 8D 4A F2                     lea r9d, [rdx - 0xe]
00C52B8A  E8 D1 AA 8A FF                  call 0x1404fd660
00C52B8F  CC                              int3
00C52B90  41 B9 05 00 00 00               mov r9d, 5
00C52B96  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00C52B9B  4D 8B C6                        mov r8, r14
00C52B9E  B9 9A 00 00 00                  mov ecx, 0x9a
00C52BA3  41 8D 51 0F                     lea edx, [r9 + 0xf]
00C52BA7  E8 B4 AA 8A FF                  call 0x1404fd660
00C52BAC  CC                              int3
00C52BAD  41 B9 04 00 00 00               mov r9d, 4
00C52BB3  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00C52BB8  4C 8B C7                        mov r8, rdi
00C52BBB  B9 9A 00 00 00                  mov ecx, 0x9a
00C52BC0  41 8D 51 10                     lea edx, [r9 + 0x10]
00C52BC4  E8 97 AA 8A FF                  call 0x1404fd660
00C52BC9  CC                              int3
00C52BCA  32 C0                           xor al, al
00C52BCC  E9 B1 F7 FF FF                  jmp 0x140c52382
00C52BD1  45 33 C9                        xor r9d, r9d
00C52BD4  44 8B C0                        mov r8d, eax
00C52BD7  B9 9A 00 00 00                  mov ecx, 0x9a
00C52BDC  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00C52BE1  41 8D 51 03                     lea edx, [r9 + 3]
00C52BE5  E8 76 AA 8A FF                  call 0x1404fd660
00C52BEA  CC                              int3
00C52BEB  45 33 C9                        xor r9d, r9d
00C52BEE  44 8B C0                        mov r8d, eax
00C52BF1  B9 9A 00 00 00                  mov ecx, 0x9a
00C52BF6  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00C52BFB  41 8D 51 03                     lea edx, [r9 + 3]
00C52BFF  E8 5C AA 8A FF                  call 0x1404fd660
00C52C04  CC                              int3
00C52C05  45 33 C9                        xor r9d, r9d
00C52C08  44 8B C0                        mov r8d, eax
00C52C0B  B9 9A 00 00 00                  mov ecx, 0x9a
00C52C10  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00C52C15  41 8D 51 02                     lea edx, [r9 + 2]
00C52C19  E8 42 AA 8A FF                  call 0x1404fd660
00C52C1E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpWatchProductTypeInitialization(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned int v_stack_m104;
    unsigned int v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int16 v_stack_m116;
    unsigned __int64 v_stack_m118;
    unsigned int v_stack_m11C;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned int v_stack_m148;
    unsigned __int64 v_stack_m150;
    unsigned __int64 v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned int v_stack_m7C;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned int v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned int v_stack_mB8;
    unsigned int v_stack_mBC;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mF0;
    unsigned int v_stack_mF8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_stack_p18 = v_rdi;
    v_rsp = (v_rsp) - (368);
    result = (*(unsigned __int64 *)(v_rip + 1803685)) ^ (v_rsp);
    v_stack_m38 = result;
    v_r15 = 0;
    v_stack_m11C = 0;
    v_stack_mF0 = v_xmm0;
    v_stack_m104 = 0;
    v_stack_m148 = 0;
    v_stack_m128 = 0;
    v_stack_mA0 = v_xmm0;
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3616351) + 616) = (unsigned __int8)(v_r15 + 1);
    a1 = (*(unsigned __int64 *)(v_rip + 3616294)) + (612);
    *(unsigned __int8 *)(v_rip + 2744137) = 0;
    v_stack_m140 = v_xmm1;
    *(unsigned __int8 *)(v_rip + 2744124) = 0;
    result = ExpGetNtProductTypeFromLicenseValue(a1, a2, a3, a4);
    result = RtlInitUnicodeString(v_stack_mF0, *(unsigned __int64 *)(v_rip - 1078440), a3, a4);
    v_stack_m118 = 0;
    v_stack_m110 = v_stack_mF0;
    v_stack_m108 = 576;
    v_stack_m120 = (unsigned int)(v_r15 + 48);
    v_stack_m100 = v_xmm0;
    result = NtOpenKey(v_rip + 2744047, (unsigned int)(0x2001FULL), v_stack_m120, a4);
    if (sign_flag) goto loc_00C52C05;
    a4 = 0;
    v_stack_m170 = 0;
    a2 = 0;
    v_stack_m178 = v_stack_m130;
    v_stack_m130 = 0;
    result = ObReferenceObjectByHandle(*(unsigned __int64 *)(v_rip + 2744010), a2, *(unsigned __int64 *)(v_rip + 3623014), a4);
    if (sign_flag) {
        a3 = (unsigned int)(result);
        a2 = v_r15 + 11;
        a4 = 0;
        v_stack_m178 = 0;
        a1 = v_r15 + 48 + 106;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    result = RtlInitUnicodeString(v_stack_m140, *(unsigned __int64 *)(v_rip - 1078593), a3, a4);
    v_stack_m170 = v_stack_m148;
    v_stack_m178 = 72;
    result = NtQueryValueKey(*(unsigned __int64 *)(v_rip + 2743926), v_stack_m140, (unsigned int)((unsigned int)(72 - 70)), v_stack_m88);
    if (sign_flag) goto loc_00C52BEB;
    if (v_stack_m7C == ((unsigned int)(v_r15 + 1))) goto loc_00C522F8;
    v_rdi = v_stack_m130;
    if (v_stack_m7C == 4) {
        result = *(unsigned __int64 *)(v_rip + 3616009);
        a2 = 0x746C6644ULL;
        a1 = v_stack_m130;
        *(unsigned __int8 *)(v_rip + 2743851) = (unsigned __int8)(v_r15 + 1);
        *(unsigned __int8 *)(result + 616) = 0;
        result = ObfDereferenceObjectWithTag(a1, a2, (unsigned int)((unsigned int)(72 - 70)), v_stack_m88);
        v_rdi = 0;
    }
    result = RtlInitUnicodeString(v_stack_m140, *(unsigned __int64 *)(v_rip - 1078516), (unsigned int)((unsigned int)(72 - 70)), v_stack_m88);
    v_stack_m170 = v_stack_m148;
    v_stack_m178 = 72;
    result = NtQueryValueKey(*(unsigned __int64 *)(v_rip + 2743803), v_stack_m140, (unsigned int)((unsigned int)(72 - 70)), v_stack_m88);
    if (sign_flag) goto loc_00C52BD1;
    if (v_stack_m7C == ((unsigned int)(v_r15 + 1))) {
        *(unsigned __int8 *)(v_rip + 2743758) = (unsigned __int8)(v_r15 + 1);
    }
    result = ExpLicenseWatchInitWorker(*(unsigned __int64 *)(v_rip + 2743803), v_stack_m140, (unsigned int)((unsigned int)(72 - 70)), v_stack_m88);
    if ((*(unsigned __int8 *)(v_rip + 3612114)) == 0) goto loc_00C523B0;
    *(unsigned __int64 *)(v_rip + 2804385) = v_rdi;
loc_00C5237F:
loc_00C52382:
    a1 = (v_stack_m38) ^ (v_rsp);
    result = _security_check_cookie(a1, v_stack_m140, (unsigned int)((unsigned int)(72 - 70)), v_stack_m88);
    return result;
loc_00C523B0:
    *(unsigned __int64 *)(v_rip + 2804263) = v_rip - 5580574;
    *(unsigned __int64 *)(v_rip + 2804264) = 0;
    *(unsigned __int64 *)(v_rip + 2804233) = 0;
    result = RtlInitUnicodeString(v_stack_mF0, *(unsigned __int64 *)(v_rip - 1078847), (unsigned int)((unsigned int)(72 - 70)), v_stack_m88);
    v_stack_mF8 = (unsigned int)(v_r15 + 48);
    v_stack_m110 = v_stack_mF0;
    v_stack_m118 = 0;
    v_stack_m108 = 576;
    v_stack_m100 = v_xmm0;
    result = NtOpenKey(v_rip + 2804240, (unsigned int)(0x2001FULL), v_stack_mF8, v_stack_m88);
    if (!sign_flag) goto loc_00C5243D;
    if ((*(unsigned __int8 *)(v_rip + 2743580)) != 0) goto loc_00C52BCA;
    a4 = 0;
    v_stack_m150 = 0;
    result = KeBugCheckEx(154, a4 + 6, (unsigned int)((unsigned int)(result)), a4);
loc_00C5243D:
    if ((*(unsigned __int8 *)(v_rip + 2743541)) != 0) goto loc_00C52495;
    a4 = 0;
    v_stack_m148 = 0;
    a2 = 0;
    v_stack_m150 = v_stack_m108;
    v_stack_m108 = 0;
    result = ObReferenceObjectByHandle(*(unsigned __int64 *)(v_rip + 2804159), a2, *(unsigned __int64 *)(v_rip + 3622515), a4);
    if (sign_flag) {
        a4 = 0;
        a3 = (unsigned int)(result);
        a1 = 154;
        v_stack_m150 = 0;
        a2 = a4 + 12;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    *(unsigned __int64 *)(v_rip + 2804100) = *(unsigned __int64 *)(v_stack_m28 + 64);
    *(unsigned __int64 *)(v_rip + 2804101) = v_stack_m108;
    result = ExpUpdateProductSuiteTypeInRegistry(a1, a2, a3, a4);
    result = RtlInitUnicodeString(v_stack_m118, *(unsigned __int64 *)(v_rip - 1079087), a3, a4);
    result = ExAllocatePool2(256, 34, (unsigned int)((unsigned int)((unsigned int)(0x2079654BULL))), a4);
    *(unsigned __int64 *)(v_rip + 2804003) = result;
    if (result == 0) goto loc_00C52BCA;
    v_stack_m148 = v_stack_m120;
    v_stack_m150 = 34;
    result = NtQueryValueKey(*(unsigned __int64 *)(v_rip + 2803993), v_stack_m118, (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 48))), result);
    if (!sign_flag) goto loc_00C52533;
    if ((*(unsigned __int8 *)(v_rip + 2743331)) != 0) goto loc_00C52BCA;
    a4 = 0;
    v_stack_m150 = 0;
    result = KeBugCheckEx(34 + 120, 34 - 27, (unsigned int)((unsigned int)(result)), a4);
loc_00C52533:
    result = RtlInitUnicodeString(v_stack_m118, *(unsigned __int64 *)(v_rip - 1079194), (unsigned int)((unsigned int)(result)), a4);
    v_stack_m148 = v_stack_m120;
    v_stack_m150 = 16;
    result = NtQueryValueKey(*(unsigned __int64 *)(v_rip + 2803917), v_stack_m118, (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 48))), v_stack_mA0);
    if (((unsigned int)(result)) != 0x80000005ULL) goto loc_00C52607;
    result = (unsigned int)(((unsigned int)(v_stack_m120)) + (16));
    v_stack_m120 = (unsigned int)(result);
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(result)), (unsigned int)((unsigned int)((unsigned int)(0x2079654BULL))), v_stack_mA0);
    *(unsigned __int64 *)(v_rip + 2160912) = result;
    if (result == 0) {
        a3 = v_stack_m120;
        a2 = result + 20;
        a4 = *(unsigned __int64 *)(v_stack_m28 + 48);
        v_stack_m150 = 0;
        a1 = 154;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    v_stack_m148 = v_stack_m120;
    v_stack_m150 = (unsigned int)((unsigned int)(v_stack_m120));
    result = NtQueryValueKey(*(unsigned __int64 *)(v_rip + 2803798), v_stack_m118, (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 48))), a4);
    if (!sign_flag) goto loc_00C52607;
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(v_rip + 2160828), a2, (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 48))), a4);
    *(unsigned __int64 *)(v_rip + 2160807) = 0;
    if ((*(unsigned __int8 *)(v_rip + 2743103)) != 0) goto loc_00C52BCA;
loc_00C52607:
    v_rsi = (34) | (-1);
loc_00C52615:
    a3 = (v_rsi) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip - 1079430) + a3 * 2)) != 0) goto loc_00C52615;
    a2 = (*(unsigned __int64 *)(v_rip + 2803674)) + (12);
    result = wcsncmp(*(unsigned __int64 *)(v_rip - 1079430), a2, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_00C52664;
    if ((*(unsigned int *)(v_rip + 3611530)) != 3) goto loc_00C52664;
    if ((*(unsigned __int8 *)(v_rip + 2743030)) == 0) {
        result = *(unsigned __int64 *)(v_rip + 3615164);
        *(unsigned __int8 *)(result + 616) = (unsigned __int8)(v_r15 + 1);
        result = *(unsigned __int64 *)(v_rip + 3615150);
        *(unsigned int *)(result + 612) = 3;
    }
    v_stack_m128 = (unsigned __int8)(v_r15 + 1);
    v_stack_m130 = 4;
    v_stack_m138 = v_rip + 2803606;
    a2 = 0;
    v_stack_m140 = 0;
    v_stack_m148 = 0x10000005ULL;
    v_stack_m150 = v_rip + 2803492;
    result = NtNotifyChangeKey(*(unsigned __int64 *)(v_rip + 2803629), a2, v_rip + 2803554, v_r15 + 1);
    if (!sign_flag) goto loc_00C526D9;
    if ((*(unsigned __int8 *)(v_rip + 2742912)) != 0) goto loc_00C52BCA;
    a4 = 0;
    v_stack_m150 = 0;
    result = KeBugCheckEx(154, a4 + 8, (unsigned int)((unsigned int)(result)), a4);
loc_00C526D9:
    result = RtlInitUnicodeString(v_stack_mF0, *(unsigned __int64 *)(v_rip - 1079608), (unsigned int)((unsigned int)(result)), a4);
    v_stack_mF8 = (unsigned int)(v_r15 + 48);
    v_stack_m110 = v_stack_mF0;
    v_stack_m118 = 0;
    v_stack_m108 = 576;
    v_stack_m100 = v_xmm0;
    result = NtOpenKey(v_stack_m100, (unsigned int)(0x20019ULL), v_stack_mF8, a4);
    if (sign_flag) goto loc_00C5237F;
    v_stack_m108 = 0;
    v_stack_mD0 = v_xmm0;
    v_stack_mC0 = v_xmm0;
    v_stack_mB0 = v_xmm0;
    v_stack_m118 = v_xmm0;
    v_stack_mE0 = v_xmm1;
loc_00C52752:
    result = (v_rsi) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip - 1079684) + result * 2)) != 0) goto loc_00C52752;
    result = (unsigned __int16)((result) + (64));
    result = (unsigned __int16)((result) + ((unsigned __int16)(result)));
    v_stack_m118 = (unsigned __int16)((unsigned __int16)(result));
    v_stack_m116 = (unsigned __int16)((unsigned __int16)(result));
    result = ExAllocatePool2(64, (unsigned __int16)(result), (unsigned int)((unsigned int)((unsigned int)(0x2079654BULL))), a4);
    v_stack_m110 = result;
    if (result == 0) {
        a3 = v_stack_m118;
        a2 = 64 - 44;
        a1 = 64 + 90;
        v_stack_m150 = 0;
        a4 = 64 - 61;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    v_stack_m150 = v_stack_m108;
    result = NtQueryKey(v_stack_m100, (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 48))), v_stack_mD0, (unsigned int)((unsigned int)(v_r15 + 48)));
    if (sign_flag) {
        a3 = (int)((unsigned int)(result));
        a4 = v_r15 + 1;
        a2 = 19;
        v_stack_m150 = 0;
        a1 = 154;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    if (((unsigned int)((unsigned int)(v_stack_mB8) * 2 + 56)) < ((unsigned int)((unsigned int)(v_stack_mB8)))) goto loc_00C527FD;
    a1 = ((unsigned int)(v_stack_mB8) + 16) + ((unsigned int)(v_stack_mB8) + 16);
    v_r14 = 0;
    if (((unsigned int)((unsigned int)((unsigned int)(v_stack_mB8) * 2 + 56))) < a1) {
        v_r14 = (unsigned __int8)(v_r15 + 1);
    }
    result = ExAllocatePool2(64, (unsigned int)((unsigned int)((unsigned int)(v_stack_mB8) * 2 + 56)), (unsigned int)(0x2079654BULL), a4);
    if (result == 0) goto loc_00C52BAD;
    if ((unsigned __int8)(v_r14) != 0) goto loc_00C52BAD;
    v_rdi = (unsigned __int8)(v_r14);
    if (((unsigned int)((unsigned int)(v_stack_mA8) + 32)) < ((unsigned int)((unsigned int)(v_stack_mA8)))) { v_rdi = 1; }
    result = ExAllocatePool2(1 + 63, (unsigned int)((unsigned int)((unsigned int)(v_stack_mA8) + 32)), (unsigned int)(0x2079654BULL), 1);
    a2 = 0;
    if (result == 0) goto loc_00C52B90;
    if ((unsigned __int8)(v_rdi) != 0) goto loc_00C52B90;
    *(unsigned int *)(v_rip + 2803092) = (unsigned int)((unsigned int)(v_stack_mBC));
    a3 = ((unsigned int)(v_stack_mBC) + (unsigned int)(v_stack_mBC) * 4) << (4);
    if (a3 > ((unsigned int)(0xFFFFFFFFULL))) goto loc_00C52B77;
    result = ExAllocatePool2(64, (unsigned int)((unsigned int)(a3)), (unsigned int)(0x2079654BULL), 1);
    v_rdi = 0;
    *(unsigned __int64 *)(v_rip + 2802987) = result;
    if (result == 0) {
        result = *(unsigned int *)(v_rip + 2803036);
        a2 = v_rdi + 20;
        a1 = 154;
        v_stack_m150 = 0;
        a4 = v_rdi + 6;
        a3 = result + result * 4;
        a3 = (a3) << (4);
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    result = RtlInitUnicodeString(v_stack_mE0, *(unsigned __int64 *)(v_rip - 1080102), a3, a4);
loc_00C528E2:
    v_stack_m148 = v_stack_m108;
    a3 = 0;
    v_stack_m150 = (unsigned int)((unsigned int)(v_stack_mB8) * 2 + 56);
    result = NtEnumerateKey(v_stack_m100, 0, a3, result);
    if (((unsigned int)(result)) == 0x8000001AULL) goto loc_00C52B42;
    if (sign_flag) goto loc_00C52B28;
    result = ((unsigned int)(*(unsigned int *)(result + 12))) >> (1);
    *(unsigned __int16 *)(result + result * 2 + 16) = 0;
    a2 = (v_stack_m116) >> (1);
    result = wcscpy_s(v_stack_m110, a2, *(unsigned __int64 *)(v_rip - 1080185), result);
    a2 = (v_stack_m116) >> (1);
    result = wcscat_s(v_stack_m110, a2, v_rip + 177049, result);
    a2 = (v_stack_m116) >> (1);
    result = wcscat_s(v_stack_m110, a2, result + 16, result);
    result = (result) | (-1);
loc_00C52973:
    result = (result) + 1;
    if ((*(unsigned __int16 *)(v_stack_m110 + result * 2)) != 0) goto loc_00C52973;
    result = (unsigned __int16)((result) + ((unsigned __int16)(result)));
    v_stack_m118 = 0;
    v_stack_m118 = (unsigned __int16)(result);
    v_stack_mF8 = 48;
    v_stack_m110 = v_stack_m118;
    v_stack_m108 = 576;
    v_stack_m100 = v_xmm0;
    v_rdi = (0 + 0 * 4) << (4);
    a1 = (*(unsigned __int64 *)(v_rip + 2802765)) + (v_rdi);
    result = NtOpenKey(a1, (unsigned int)(0x2001FULL), v_stack_mF8, result);
    if (sign_flag) goto loc_00C52B0B;
    v_stack_m148 = v_stack_m108;
    v_stack_m150 = (unsigned int)((unsigned int)(v_stack_mA8) + 32);
    result = NtQueryValueKey(*(unsigned __int64 *)(v_rdi + *(unsigned __int64 *)(v_rip + 2802677) * 1), v_stack_mE0, (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 48))), result);
    if (sign_flag) goto loc_00C52AEF;
    result = ExAllocatePool2(64, v_stack_m118, (unsigned int)(0x2079654BULL), result);
    *(unsigned __int64 *)(v_rdi + *(unsigned __int64 *)(v_rip + 2802607) * 1 + 16) = result;
    if (result == 0) goto loc_00C52ACF;
    a2 = (v_stack_m118) >> (1);
    result = wcscpy_s(result, a2, v_stack_m110, result);
    a1 = (*(unsigned __int64 *)(v_rip + 2802561)) + (v_rdi);
    v_rdi = 0;
    *(unsigned int *)(a1 + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 12)));
    *(unsigned __int64 *)(a1 + 24 + 24) = a1;
    *(unsigned __int64 *)(a1 + 24) = 0;
    v_stack_m128 = (unsigned __int8)(v_rdi + 1);
    v_stack_m130 = 4;
    *(unsigned __int64 *)(a1 + 24 + 16) = v_rip - 4766918;
    v_stack_m138 = a1 + 72;
    v_stack_m140 = (unsigned __int8)(v_rdi + 1);
    v_stack_m148 = 0x10000005ULL;
    v_stack_m150 = a1 + 56;
    a2 = 0;
    result = NtNotifyChangeKey(*(unsigned __int64 *)(a1), a2, a1 + 24, v_rdi + 1);
    if (sign_flag) goto loc_00C52AB3;
    v_r14 = (unsigned int)((0) + 1);
    goto loc_00C528E2;
loc_00C52AB3:
    v_stack_m150 = 0;
    result = KeBugCheckEx(154, 24, (int)((unsigned int)(result)), 24 - 23);
loc_00C52ACF:
    result = KeBugCheckEx(154, 20, v_stack_m118, 20 - 13);
loc_00C52AEF:
    result = KeBugCheckEx(154, 19, (int)((unsigned int)(result)), *(unsigned __int64 *)(v_stack_m28 + 48));
loc_00C52B0B:
    result = KeBugCheckEx(154, 22, (int)((unsigned int)(result)), 22 - 21);
loc_00C52B28:
    a4 = 0;
    v_stack_m150 = 0;
    result = KeBugCheckEx(154, a4 + 26, (int)((unsigned int)(result)), a4);
loc_00C52B42:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, (int)((unsigned int)(result)), a4);
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, (int)((unsigned int)(result)), a4);
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m110, a2, (int)((unsigned int)(result)), a4);
    result = NtClose(v_stack_m100, a2, (int)((unsigned int)(result)), a4);
    goto loc_00C5237F;
loc_00C52B77:
    v_stack_m150 = 0;
    result = KeBugCheckEx(154, 20, (int)((unsigned int)(result)), 20 - 14);
loc_00C52B90:
    v_stack_m150 = 20;
    result = KeBugCheckEx(154, 5 + 15, v_r14, 5);
loc_00C52BAD:
    v_stack_m150 = result;
    result = KeBugCheckEx(154, 4 + 16, 0, 4);
loc_00C52BCA:
    result = 0;
    goto loc_00C52382;
loc_00C52BD1:
    a4 = 0;
    v_stack_m150 = 0;
    result = KeBugCheckEx(154, a4 + 3, 0, a4);
loc_00C52BEB:
    a4 = 0;
    v_stack_m150 = result;
    result = KeBugCheckEx(154, a4 + 3, (unsigned int)((unsigned int)(result)), a4);
loc_00C52C05:
    a4 = 0;
    v_stack_m150 = result;
    result = KeBugCheckEx(154, a4 + 2, (unsigned int)((unsigned int)(result)), a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ExpWatchProductTypeInitialization(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint32_t v_stack_m104;
    uint32_t v_stack_m108;
    uint64_t v_stack_m110;
    uint16_t v_stack_m116;
    uint64_t v_stack_m118;
    uint32_t v_stack_m11C;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint32_t v_stack_m148;
    uint64_t v_stack_m150;
    uint64_t v_stack_m170;
    uint64_t v_stack_m178;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint32_t v_stack_m7C;
    uint64_t v_stack_m88;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint32_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint32_t v_stack_mB8;
    uint32_t v_stack_mBC;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mF0;
    uint32_t v_stack_mF8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    v_stack_p18 = local_rdi;
    local_rsp = (local_rsp) - (368);
    result = (*(uint64_t *)(v_rip + 0x1B85A5)) ^ (local_rsp);
    v_stack_m38 = result;
    local_r15 = 0;
    v_stack_m11C = 0;
    v_stack_mF0 = v_xmm0;
    v_stack_m104 = 0;
    v_stack_m148 = 0;
    v_stack_m128 = 0;
    v_stack_mA0 = v_xmm0;
    *(uint8_t *)(*(uint64_t *)(v_rip + 0x372E5F) + 0x268) = (uint8_t)(local_r15 + 1);
    Arg1 = (*(uint64_t *)(v_rip + 0x372E26)) + (612);
    *(uint8_t *)(v_rip + 0x29DF49) = 0;
    v_stack_m140 = v_xmm1;
    *(uint8_t *)(v_rip + 0x29DF3C) = 0;
    result = ExpGetNtProductTypeFromLicenseValue(Arg1, Arg2, Arg3, Arg4);
    result = RtlInitUnicodeString(v_stack_mF0, *(uint64_t *)(v_rip - 0x1074A8), Arg3, Arg4);
    v_stack_m118 = 0;
    v_stack_m110 = v_stack_mF0;
    v_stack_m108 = 576;
    v_stack_m120 = (uint32_t)(local_r15 + 48);
    v_stack_m100 = v_xmm0;
    result = NtOpenKey(v_rip + 2744047, (uint32_t)(0x2001FULL), v_stack_m120, Arg4);
    if (sign_flag) goto loc_00C52C05;
    Arg4 = 0;
    v_stack_m170 = 0;
    Arg2 = 0;
    v_stack_m178 = v_stack_m130;
    v_stack_m130 = 0;
    result = ObReferenceObjectByHandle(*(uint64_t *)(v_rip + 0x29DECA), Arg2, *(uint64_t *)(v_rip + 0x374866), Arg4);
    if (sign_flag) {
        Arg3 = (uint32_t)(result);
        Arg2 = local_r15 + 11;
        Arg4 = 0;
        v_stack_m178 = 0;
        Arg1 = local_r15 + 48 + 106;
        result = KeBugCheckEx(Arg1, Arg2, Arg3, Arg4);
    }
    result = RtlInitUnicodeString(v_stack_m140, *(uint64_t *)(v_rip - 0x107541), Arg3, Arg4);
    v_stack_m170 = v_stack_m148;
    v_stack_m178 = 72;
    result = NtQueryValueKey(*(uint64_t *)(v_rip + 0x29DE76), v_stack_m140, (uint32_t)((uint32_t)(72 - 70)), v_stack_m88);
    if (sign_flag) goto loc_00C52BEB;
    if (v_stack_m7C == ((uint32_t)(local_r15 + 1))) goto loc_00C522F8;
    local_rdi = v_stack_m130;
    if (v_stack_m7C == 4) {
        result = *(uint64_t *)(v_rip + 0x372D09);
        Arg2 = 0x746C6644ULL;
        Arg1 = v_stack_m130;
        *(uint8_t *)(v_rip + 0x29DE2B) = (uint8_t)(local_r15 + 1);
        *(uint8_t *)(result + 0x268) = 0;
        result = ObfDereferenceObjectWithTag(Arg1, Arg2, (uint32_t)((uint32_t)(72 - 70)), v_stack_m88);
        local_rdi = 0;
    }
    result = RtlInitUnicodeString(v_stack_m140, *(uint64_t *)(v_rip - 0x1074F4), (uint32_t)((uint32_t)(72 - 70)), v_stack_m88);
    v_stack_m170 = v_stack_m148;
    v_stack_m178 = 72;
    result = NtQueryValueKey(*(uint64_t *)(v_rip + 0x29DDFB), v_stack_m140, (uint32_t)((uint32_t)(72 - 70)), v_stack_m88);
    if (sign_flag) goto loc_00C52BD1;
    if (v_stack_m7C == ((uint32_t)(local_r15 + 1))) {
        *(uint8_t *)(v_rip + 0x29DDCE) = (uint8_t)(local_r15 + 1);
    }
    result = ExpLicenseWatchInitWorker(*(uint64_t *)(v_rip + 0x29DDFB), v_stack_m140, (uint32_t)((uint32_t)(72 - 70)), v_stack_m88);
    if ((*(uint8_t *)(v_rip + 0x371DD2)) == 0) goto loc_00C523B0;
    *(uint64_t *)(v_rip + 0x2ACAA1) = local_rdi;
loc_00C5237F:
loc_00C52382:
    Arg1 = (v_stack_m38) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_stack_m140, (uint32_t)((uint32_t)(72 - 70)), v_stack_m88);
    return result;
loc_00C523B0:
    *(uint64_t *)(v_rip + 0x2ACA27) = v_rip - 5580574;
    *(uint64_t *)(v_rip + 0x2ACA28) = 0;
    *(uint64_t *)(v_rip + 0x2ACA09) = 0;
    result = RtlInitUnicodeString(v_stack_mF0, *(uint64_t *)(v_rip - 0x10763F), (uint32_t)((uint32_t)(72 - 70)), v_stack_m88);
    v_stack_mF8 = (uint32_t)(local_r15 + 48);
    v_stack_m110 = v_stack_mF0;
    v_stack_m118 = 0;
    v_stack_m108 = 576;
    v_stack_m100 = v_xmm0;
    result = NtOpenKey(v_rip + 2804240, (uint32_t)(0x2001FULL), v_stack_mF8, v_stack_m88);
    if (!sign_flag) goto loc_00C5243D;
    if ((*(uint8_t *)(v_rip + 0x29DD1C)) != 0) goto loc_00C52BCA;
    Arg4 = 0;
    v_stack_m150 = 0;
    result = KeBugCheckEx(154, Arg4 + 6, (uint32_t)((uint32_t)(result)), Arg4);
loc_00C5243D:
    if ((*(uint8_t *)(v_rip + 0x29DCF5)) != 0) goto loc_00C52495;
    Arg4 = 0;
    v_stack_m148 = 0;
    Arg2 = 0;
    v_stack_m150 = v_stack_m108;
    v_stack_m108 = 0;
    result = ObReferenceObjectByHandle(*(uint64_t *)(v_rip + 0x2AC9BF), Arg2, *(uint64_t *)(v_rip + 0x374673), Arg4);
    if (sign_flag) {
        Arg4 = 0;
        Arg3 = (uint32_t)(result);
        Arg1 = 154;
        v_stack_m150 = 0;
        Arg2 = Arg4 + 12;
        result = KeBugCheckEx(Arg1, Arg2, Arg3, Arg4);
    }
    *(uint64_t *)(v_rip + 0x2AC984) = *(uint64_t *)(v_stack_m28 + 0x40);
    *(uint64_t *)(v_rip + 0x2AC985) = v_stack_m108;
    result = ExpUpdateProductSuiteTypeInRegistry(Arg1, Arg2, Arg3, Arg4);
    result = RtlInitUnicodeString(v_stack_m118, *(uint64_t *)(v_rip - 0x10772F), Arg3, Arg4);
    result = ExAllocatePool2(256, 34, (uint32_t)((uint32_t)((uint32_t)(0x2079654BULL))), Arg4);
    *(uint64_t *)(v_rip + 0x2AC923) = result;
    if (result == 0) goto loc_00C52BCA;
    v_stack_m148 = v_stack_m120;
    v_stack_m150 = 34;
    result = NtQueryValueKey(*(uint64_t *)(v_rip + 0x2AC919), v_stack_m118, (uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x30))), result);
    if (!sign_flag) goto loc_00C52533;
    if ((*(uint8_t *)(v_rip + 0x29DC23)) != 0) goto loc_00C52BCA;
    Arg4 = 0;
    v_stack_m150 = 0;
    result = KeBugCheckEx(34 + 120, 34 - 27, (uint32_t)((uint32_t)(result)), Arg4);
loc_00C52533:
    result = RtlInitUnicodeString(v_stack_m118, *(uint64_t *)(v_rip - 0x10779A), (uint32_t)((uint32_t)(result)), Arg4);
    v_stack_m148 = v_stack_m120;
    v_stack_m150 = 16;
    result = NtQueryValueKey(*(uint64_t *)(v_rip + 0x2AC8CD), v_stack_m118, (uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x30))), v_stack_mA0);
    if (((uint32_t)(result)) != 0x80000005ULL) goto loc_00C52607;
    result = (uint32_t)(((uint32_t)(v_stack_m120)) + (16));
    v_stack_m120 = (uint32_t)(result);
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(result)), (uint32_t)((uint32_t)((uint32_t)(0x2079654BULL))), v_stack_mA0);
    *(uint64_t *)(v_rip + 0x20F910) = result;
    if (result == 0) {
        Arg3 = v_stack_m120;
        Arg2 = result + 20;
        Arg4 = *(uint64_t *)(v_stack_m28 + 0x30);
        v_stack_m150 = 0;
        Arg1 = 154;
        result = KeBugCheckEx(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_m148 = v_stack_m120;
    v_stack_m150 = (uint32_t)((uint32_t)(v_stack_m120));
    result = NtQueryValueKey(*(uint64_t *)(v_rip + 0x2AC856), v_stack_m118, (uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x30))), Arg4);
    if (!sign_flag) goto loc_00C52607;
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(v_rip + 0x20F8BC), Arg2, (uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x30))), Arg4);
    *(uint64_t *)(v_rip + 0x20F8A7) = 0;
    if ((*(uint8_t *)(v_rip + 0x29DB3F)) != 0) goto loc_00C52BCA;
loc_00C52607:
    local_rsi = (34) | (-1);
loc_00C52615:
    Arg3 = (local_rsi) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(v_rip - 0x107886) + Arg3 * 2)) != 0) goto loc_00C52615;
    Arg2 = (*(uint64_t *)(v_rip + 0x2AC7DA)) + (12);
    result = wcsncmp(*(uint64_t *)(v_rip - 0x107886), Arg2, Arg3, Arg4);
    if ((uint32_t)(result) != 0) goto loc_00C52664;
    if ((*(uint32_t *)(v_rip + 0x371B8A)) != 3) goto loc_00C52664;
    if ((*(uint8_t *)(v_rip + 0x29DAF6)) == 0) {
        result = *(uint64_t *)(v_rip + 0x3729BC);
        *(uint8_t *)(result + 0x268) = (uint8_t)(local_r15 + 1);
        result = *(uint64_t *)(v_rip + 0x3729AE);
        *(uint32_t *)(result + 0x264) = 3;
    }
    v_stack_m128 = (uint8_t)(local_r15 + 1);
    v_stack_m130 = 4;
    v_stack_m138 = v_rip + 2803606;
    Arg2 = 0;
    v_stack_m140 = 0;
    v_stack_m148 = 0x10000005ULL;
    v_stack_m150 = v_rip + 2803492;
    result = NtNotifyChangeKey(*(uint64_t *)(v_rip + 0x2AC7AD), Arg2, v_rip + 2803554, local_r15 + 1);
    if (!sign_flag) goto loc_00C526D9;
    if ((*(uint8_t *)(v_rip + 0x29DA80)) != 0) goto loc_00C52BCA;
    Arg4 = 0;
    v_stack_m150 = 0;
    result = KeBugCheckEx(154, Arg4 + 8, (uint32_t)((uint32_t)(result)), Arg4);
loc_00C526D9:
    result = RtlInitUnicodeString(v_stack_mF0, *(uint64_t *)(v_rip - 0x107938), (uint32_t)((uint32_t)(result)), Arg4);
    v_stack_mF8 = (uint32_t)(local_r15 + 48);
    v_stack_m110 = v_stack_mF0;
    v_stack_m118 = 0;
    v_stack_m108 = 576;
    v_stack_m100 = v_xmm0;
    result = NtOpenKey(v_stack_m100, (uint32_t)(0x20019ULL), v_stack_mF8, Arg4);
    if (sign_flag) goto loc_00C5237F;
    v_stack_m108 = 0;
    v_stack_mD0 = v_xmm0;
    v_stack_mC0 = v_xmm0;
    v_stack_mB0 = v_xmm0;
    v_stack_m118 = v_xmm0;
    v_stack_mE0 = v_xmm1;
loc_00C52752:
    result = (local_rsi) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(v_rip - 0x107984) + result * 2)) != 0) goto loc_00C52752;
    result = (uint16_t)((result) + (64));
    result = (uint16_t)((result) + ((uint16_t)(result)));
    v_stack_m118 = (uint16_t)((uint16_t)(result));
    v_stack_m116 = (uint16_t)((uint16_t)(result));
    result = ExAllocatePool2(64, (uint16_t)(result), (uint32_t)((uint32_t)((uint32_t)(0x2079654BULL))), Arg4);
    v_stack_m110 = result;
    if (result == 0) {
        Arg3 = v_stack_m118;
        Arg2 = 64 - 44;
        Arg1 = 64 + 90;
        v_stack_m150 = 0;
        Arg4 = 64 - 61;
        result = KeBugCheckEx(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_m150 = v_stack_m108;
    result = NtQueryKey(v_stack_m100, (uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x30))), v_stack_mD0, (uint32_t)((uint32_t)(local_r15 + 48)));
    if (sign_flag) {
        Arg3 = (int32_t)((uint32_t)(result));
        Arg4 = local_r15 + 1;
        Arg2 = 19;
        v_stack_m150 = 0;
        Arg1 = 154;
        result = KeBugCheckEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (((uint32_t)((uint32_t)(v_stack_mB8) * 2 + 56)) < ((uint32_t)((uint32_t)(v_stack_mB8)))) goto loc_00C527FD;
    Arg1 = ((uint32_t)(v_stack_mB8) + 16) + ((uint32_t)(v_stack_mB8) + 16);
    local_r14 = 0;
    if (((uint32_t)((uint32_t)((uint32_t)(v_stack_mB8) * 2 + 56))) < Arg1) {
        local_r14 = (uint8_t)(local_r15 + 1);
    }
    result = ExAllocatePool2(64, (uint32_t)((uint32_t)((uint32_t)(v_stack_mB8) * 2 + 56)), (uint32_t)(0x2079654BULL), Arg4);
    if (result == 0) goto loc_00C52BAD;
    if ((uint8_t)(local_r14) != 0) goto loc_00C52BAD;
    local_rdi = (uint8_t)(local_r14);
    if (((uint32_t)((uint32_t)(v_stack_mA8) + 32)) < ((uint32_t)((uint32_t)(v_stack_mA8)))) { local_rdi = 1; }
    result = ExAllocatePool2(1 + 63, (uint32_t)((uint32_t)((uint32_t)(v_stack_mA8) + 32)), (uint32_t)(0x2079654BULL), 1);
    Arg2 = 0;
    if (result == 0) goto loc_00C52B90;
    if ((uint8_t)(local_rdi) != 0) goto loc_00C52B90;
    *(uint32_t *)(v_rip + 0x2AC594) = (uint32_t)((uint32_t)(v_stack_mBC));
    Arg3 = ((uint32_t)(v_stack_mBC) + (uint32_t)(v_stack_mBC) * 4) << (4);
    if (Arg3 > ((uint32_t)(0xFFFFFFFFULL))) goto loc_00C52B77;
    result = ExAllocatePool2(64, (uint32_t)((uint32_t)(Arg3)), (uint32_t)(0x2079654BULL), 1);
    local_rdi = 0;
    *(uint64_t *)(v_rip + 0x2AC52B) = result;
    if (result == 0) {
        result = *(uint32_t *)(v_rip + 0x2AC55C);
        Arg2 = local_rdi + 20;
        Arg1 = 154;
        v_stack_m150 = 0;
        Arg4 = local_rdi + 6;
        Arg3 = result + result * 4;
        Arg3 = (Arg3) << (4);
        result = KeBugCheckEx(Arg1, Arg2, Arg3, Arg4);
    }
    result = RtlInitUnicodeString(v_stack_mE0, *(uint64_t *)(v_rip - 0x107B26), Arg3, Arg4);
loc_00C528E2:
    v_stack_m148 = v_stack_m108;
    Arg3 = 0;
    v_stack_m150 = (uint32_t)((uint32_t)(v_stack_mB8) * 2 + 56);
    result = NtEnumerateKey(v_stack_m100, 0, Arg3, result);
    if (((uint32_t)(result)) == 0x8000001AULL) goto loc_00C52B42;
    if (sign_flag) goto loc_00C52B28;
    result = ((uint32_t)(*(uint32_t *)(result + 0xC))) >> (1);
    *(uint16_t *)(result + result * 2 + 0x10) = 0;
    Arg2 = (v_stack_m116) >> (1);
    result = wcscpy_s(v_stack_m110, Arg2, *(uint64_t *)(v_rip - 0x107B79), result);
    Arg2 = (v_stack_m116) >> (1);
    result = wcscat_s(v_stack_m110, Arg2, v_rip + 177049, result);
    Arg2 = (v_stack_m116) >> (1);
    result = wcscat_s(v_stack_m110, Arg2, result + 16, result);
    result = (result) | (-1);
loc_00C52973:
    result = (result) + 1;
    if ((*(uint16_t *)(v_stack_m110 + result * 2)) != 0) goto loc_00C52973;
    result = (uint16_t)((result) + ((uint16_t)(result)));
    v_stack_m118 = 0;
    v_stack_m118 = (uint16_t)(result);
    v_stack_mF8 = 48;
    v_stack_m110 = v_stack_m118;
    v_stack_m108 = 576;
    v_stack_m100 = v_xmm0;
    local_rdi = (0 + 0 * 4) << (4);
    Arg1 = (*(uint64_t *)(v_rip + 0x2AC44D)) + (local_rdi);
    result = NtOpenKey(Arg1, (uint32_t)(0x2001FULL), v_stack_mF8, result);
    if (sign_flag) goto loc_00C52B0B;
    v_stack_m148 = v_stack_m108;
    v_stack_m150 = (uint32_t)((uint32_t)(v_stack_mA8) + 32);
    result = NtQueryValueKey(*(uint64_t *)(local_rdi + *(uint64_t *)(v_rip + 0x2AC3F5) * 1), v_stack_mE0, (uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x30))), result);
    if (sign_flag) goto loc_00C52AEF;
    result = ExAllocatePool2(64, v_stack_m118, (uint32_t)(0x2079654BULL), result);
    *(uint64_t *)(local_rdi + *(uint64_t *)(v_rip + 0x2AC3AF) * 1 + 0x10) = result;
    if (result == 0) goto loc_00C52ACF;
    Arg2 = (v_stack_m118) >> (1);
    result = wcscpy_s(result, Arg2, v_stack_m110, result);
    Arg1 = (*(uint64_t *)(v_rip + 0x2AC381)) + (local_rdi);
    local_rdi = 0;
    *(uint32_t *)(Arg1 + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0xC)));
    *(uint64_t *)(Arg1 + 0x18 + 0x18) = Arg1;
    *(uint64_t *)(Arg1 + 0x18) = 0;
    v_stack_m128 = (uint8_t)(local_rdi + 1);
    v_stack_m130 = 4;
    *(uint64_t *)(Arg1 + 0x18 + 0x10) = v_rip - 4766918;
    v_stack_m138 = Arg1 + 72;
    v_stack_m140 = (uint8_t)(local_rdi + 1);
    v_stack_m148 = 0x10000005ULL;
    v_stack_m150 = Arg1 + 56;
    Arg2 = 0;
    result = NtNotifyChangeKey(*(uint64_t *)(Arg1), Arg2, Arg1 + 24, local_rdi + 1);
    if (sign_flag) goto loc_00C52AB3;
    local_r14 = (uint32_t)((0) + 1);
    goto loc_00C528E2;
loc_00C52AB3:
    v_stack_m150 = 0;
    result = KeBugCheckEx(154, 24, (int32_t)((uint32_t)(result)), 24 - 23);
loc_00C52ACF:
    result = KeBugCheckEx(154, 20, v_stack_m118, 20 - 13);
loc_00C52AEF:
    result = KeBugCheckEx(154, 19, (int32_t)((uint32_t)(result)), *(uint64_t *)(v_stack_m28 + 0x30));
loc_00C52B0B:
    result = KeBugCheckEx(154, 22, (int32_t)((uint32_t)(result)), 22 - 21);
loc_00C52B28:
    Arg4 = 0;
    v_stack_m150 = 0;
    result = KeBugCheckEx(154, Arg4 + 26, (int32_t)((uint32_t)(result)), Arg4);
loc_00C52B42:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, (int32_t)((uint32_t)(result)), Arg4);
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, (int32_t)((uint32_t)(result)), Arg4);
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m110, Arg2, (int32_t)((uint32_t)(result)), Arg4);
    result = NtClose(v_stack_m100, Arg2, (int32_t)((uint32_t)(result)), Arg4);
    goto loc_00C5237F;
loc_00C52B77:
    v_stack_m150 = 0;
    result = KeBugCheckEx(154, 20, (int32_t)((uint32_t)(result)), 20 - 14);
loc_00C52B90:
    v_stack_m150 = 20;
    result = KeBugCheckEx(154, 5 + 15, local_r14, 5);
loc_00C52BAD:
    v_stack_m150 = result;
    result = KeBugCheckEx(154, 4 + 16, 0, 4);
loc_00C52BCA:
    result = 0;
    goto loc_00C52382;
loc_00C52BD1:
    Arg4 = 0;
    v_stack_m150 = 0;
    result = KeBugCheckEx(154, Arg4 + 3, 0, Arg4);
loc_00C52BEB:
    Arg4 = 0;
    v_stack_m150 = result;
    result = KeBugCheckEx(154, Arg4 + 3, (uint32_t)((uint32_t)(result)), Arg4);
loc_00C52C05:
    Arg4 = 0;
    v_stack_m150 = result;
    result = KeBugCheckEx(154, Arg4 + 2, (uint32_t)((uint32_t)(result)), Arg4);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C52170&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
