# KxMcheckAlternateReturn

- RVA: `0x006C1E00`–`0x006C24CD` (길이 `1,741` bytes)
- VA: `0x00000001406C1E00`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C1D2C`
- 디코드: `378`개 명령, `1,741/1,741` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **74**; 고유 호출 대상: **74**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x006C1F6F` → [KxMcheckAlternateReturn + 0x282](KxMcheckAlternateReturn_function_006C1E00.md) (inside-function, `0x006C2082`)
- `0x006C1F78` → [KxMcheckAlternateReturn + 0x28B](KxMcheckAlternateReturn_function_006C1E00.md) (inside-function, `0x006C208B`)
- `0x006C1F81` → [KxMcheckAlternateReturn + 0x174](KxMcheckAlternateReturn_function_006C1E00.md) (inside-function, `0x006C1F74`)
- `0x006C1F8A` → [KxMcheckAlternateReturn + 0x17D](KxMcheckAlternateReturn_function_006C1E00.md) (inside-function, `0x006C1F7D`)
- `0x006C1F93` → [KxMcheckAlternateReturn + 0x186](KxMcheckAlternateReturn_function_006C1E00.md) (inside-function, `0x006C1F86`)
- `0x006C1F9C` → [KxMcheckAlternateReturn + 0x18F](KxMcheckAlternateReturn_function_006C1E00.md) (inside-function, `0x006C1F8F`)
- `0x006C1FA5` → [KxMcheckAlternateReturn + 0x198](KxMcheckAlternateReturn_function_006C1E00.md) (inside-function, `0x006C1F98`)
- `0x006C1FAE` → [KxMcheckAlternateReturn + 0x1A1](KxMcheckAlternateReturn_function_006C1E00.md) (inside-function, `0x006C1FA1`)
- `0x006C1FB7` → [KxMcheckAlternateReturn + 0x1AA](KxMcheckAlternateReturn_function_006C1E00.md) (inside-function, `0x006C1FAA`)
- `0x006C1FC0` → [KxMcheckAlternateReturn + 0x1B3](KxMcheckAlternateReturn_function_006C1E00.md) (inside-function, `0x006C1FB3`)
- `0x006C1FC9` → [KxMcheckAlternateReturn + 0x1BC](KxMcheckAlternateReturn_function_006C1E00.md) (inside-function, `0x006C1FBC`)
- `0x006C1FD2` → [KxMcheckAlternateReturn + 0x1C5](KxMcheckAlternateReturn_function_006C1E00.md) (inside-function, `0x006C1FC5`)
- `0x006C1FDB` → [KxMcheckAlternateReturn + 0x1CE](KxMcheckAlternateReturn_function_006C1E00.md) (inside-function, `0x006C1FCE`)
- `0x006C1FE4` → [KxMcheckAlternateReturn + 0x1D7](KxMcheckAlternateReturn_function_006C1E00.md) (inside-function, `0x006C1FD7`)
- `0x006C1FED` → [KxMcheckAlternateReturn + 0x1E0](KxMcheckAlternateReturn_function_006C1E00.md) (inside-function, `0x006C1FE0`)
- `0x006C1FF6` → [KxMcheckAlternateReturn + 0x1E9](KxMcheckAlternateReturn_function_006C1E00.md) (inside-function, `0x006C1FE9`)
- `0x006C1FFF` → [KxMcheckAlternateReturn + 0x1F2](KxMcheckAlternateReturn_function_006C1E00.md) (inside-function, `0x006C1FF2`)
- `0x006C2008` → [KxMcheckAlternateReturn + 0x1FB](KxMcheckAlternateReturn_function_006C1E00.md) (inside-function, `0x006C1FFB`)
- `0x006C2011` → [KxMcheckAlternateReturn + 0x204](KxMcheckAlternateReturn_function_006C1E00.md) (inside-function, `0x006C2004`)
- `0x006C201A` → [KxMcheckAlternateReturn + 0x20D](KxMcheckAlternateReturn_function_006C1E00.md) (inside-function, `0x006C200D`)
- `0x006C2023` → [KxMcheckAlternateReturn + 0x216](KxMcheckAlternateReturn_function_006C1E00.md) (inside-function, `0x006C2016`)
- `0x006C202C` → [KxMcheckAlternateReturn + 0x21F](KxMcheckAlternateReturn_function_006C1E00.md) (inside-function, `0x006C201F`)
- `0x006C2035` → [KxMcheckAlternateReturn + 0x228](KxMcheckAlternateReturn_function_006C1E00.md) (inside-function, `0x006C2028`)
- `0x006C203E` → [KxMcheckAlternateReturn + 0x231](KxMcheckAlternateReturn_function_006C1E00.md) (inside-function, `0x006C2031`)
- `0x006C2047` → [KxMcheckAlternateReturn + 0x23A](KxMcheckAlternateReturn_function_006C1E00.md) (inside-function, `0x006C203A`)
- `0x006C2050` → [KxMcheckAlternateReturn + 0x243](KxMcheckAlternateReturn_function_006C1E00.md) (inside-function, `0x006C2043`)
- `0x006C2059` → [KxMcheckAlternateReturn + 0x24C](KxMcheckAlternateReturn_function_006C1E00.md) (inside-function, `0x006C204C`)
- `0x006C2062` → [KxMcheckAlternateReturn + 0x255](KxMcheckAlternateReturn_function_006C1E00.md) (inside-function, `0x006C2055`)
- `0x006C206B` → [KxMcheckAlternateReturn + 0x25E](KxMcheckAlternateReturn_function_006C1E00.md) (inside-function, `0x006C205E`)
- `0x006C2074` → [KxMcheckAlternateReturn + 0x267](KxMcheckAlternateReturn_function_006C1E00.md) (inside-function, `0x006C2067`)
- `0x006C207D` → [KxMcheckAlternateReturn + 0x270](KxMcheckAlternateReturn_function_006C1E00.md) (inside-function, `0x006C2070`)
- `0x006C2086` → [KxMcheckAlternateReturn + 0x279](KxMcheckAlternateReturn_function_006C1E00.md) (inside-function, `0x006C2079`)
- `0x006C20B1` → [KiFlushBhbDuringTrapEntryOrExit](KiFlushBhbDuringTrapEntryOrExit_function_006C6340.md) (function, `0x006C6340`)
- `0x006C20FA` → [KiSaveDebugRegisterState](../4F/KiSaveDebugRegisterState_function_004FD960.md) (function, `0x004FD960`)
- `0x006C212E` → [KiSynchronizeUserIsolationDomainExit](../41/KiSynchronizeUserIsolationDomainExit_function_0041BFA0.md) (function, `0x0041BFA0`)
- `0x006C217A` → [KiMcheckAlternateReturn](../5C/KiMcheckAlternateReturn_function_005CB180.md) (function, `0x005CB180`)
- `0x006C21B5` → [KiInitiateUserApc](../6B/KiInitiateUserApc_function_006B6540.md) (function, `0x006B6540`)
- `0x006C21C6` → [KiSynchronizeUserIsolationDomainEntry](../26/KiSynchronizeUserIsolationDomainEntry_function_00263F60.md) (function, `0x00263F60`)
- `0x006C21E0` → [KiUpdateStibpPairing](../3E/KiUpdateStibpPairing_function_003E71C0.md) (function, `0x003E71C0`)
- `0x006C21F6` → [KiRestoreSetContextState](../6B/KiRestoreSetContextState_function_006B1CA0.md) (function, `0x006B1CA0`)
- `0x006C2212` → [KiCopyCounters](../5C/KiCopyCounters_function_005C0710.md) (function, `0x005C0710`)
- `0x006C222E` → [KiRestoreDebugRegisterState](../4F/KiRestoreDebugRegisterState_function_004FD8E0.md) (function, `0x004FD8E0`)
- `0x006C22C8` → [KxMcheckAlternateReturn + 0x5DB](KxMcheckAlternateReturn_function_006C1E00.md) (inside-function, `0x006C23DB`)
- `0x006C22D1` → [KxMcheckAlternateReturn + 0x5E4](KxMcheckAlternateReturn_function_006C1E00.md) (inside-function, `0x006C23E4`)
- `0x006C22DA` → [KxMcheckAlternateReturn + 0x4CD](KxMcheckAlternateReturn_function_006C1E00.md) (inside-function, `0x006C22CD`)
- `0x006C22E3` → [KxMcheckAlternateReturn + 0x4D6](KxMcheckAlternateReturn_function_006C1E00.md) (inside-function, `0x006C22D6`)
- `0x006C22EC` → [KxMcheckAlternateReturn + 0x4DF](KxMcheckAlternateReturn_function_006C1E00.md) (inside-function, `0x006C22DF`)
- `0x006C22F5` → [KxMcheckAlternateReturn + 0x4E8](KxMcheckAlternateReturn_function_006C1E00.md) (inside-function, `0x006C22E8`)
- `0x006C22FE` → [KxMcheckAlternateReturn + 0x4F1](KxMcheckAlternateReturn_function_006C1E00.md) (inside-function, `0x006C22F1`)
- `0x006C2307` → [KxMcheckAlternateReturn + 0x4FA](KxMcheckAlternateReturn_function_006C1E00.md) (inside-function, `0x006C22FA`)
- `0x006C2310` → [KxMcheckAlternateReturn + 0x503](KxMcheckAlternateReturn_function_006C1E00.md) (inside-function, `0x006C2303`)
- `0x006C2319` → [KxMcheckAlternateReturn + 0x50C](KxMcheckAlternateReturn_function_006C1E00.md) (inside-function, `0x006C230C`)
- `0x006C2322` → [KxMcheckAlternateReturn + 0x515](KxMcheckAlternateReturn_function_006C1E00.md) (inside-function, `0x006C2315`)
- `0x006C232B` → [KxMcheckAlternateReturn + 0x51E](KxMcheckAlternateReturn_function_006C1E00.md) (inside-function, `0x006C231E`)
- `0x006C2334` → [KxMcheckAlternateReturn + 0x527](KxMcheckAlternateReturn_function_006C1E00.md) (inside-function, `0x006C2327`)
- `0x006C233D` → [KxMcheckAlternateReturn + 0x530](KxMcheckAlternateReturn_function_006C1E00.md) (inside-function, `0x006C2330`)
- `0x006C2346` → [KxMcheckAlternateReturn + 0x539](KxMcheckAlternateReturn_function_006C1E00.md) (inside-function, `0x006C2339`)
- `0x006C234F` → [KxMcheckAlternateReturn + 0x542](KxMcheckAlternateReturn_function_006C1E00.md) (inside-function, `0x006C2342`)
- `0x006C2358` → [KxMcheckAlternateReturn + 0x54B](KxMcheckAlternateReturn_function_006C1E00.md) (inside-function, `0x006C234B`)
- `0x006C2361` → [KxMcheckAlternateReturn + 0x554](KxMcheckAlternateReturn_function_006C1E00.md) (inside-function, `0x006C2354`)
- `0x006C236A` → [KxMcheckAlternateReturn + 0x55D](KxMcheckAlternateReturn_function_006C1E00.md) (inside-function, `0x006C235D`)
- `0x006C2373` → [KxMcheckAlternateReturn + 0x566](KxMcheckAlternateReturn_function_006C1E00.md) (inside-function, `0x006C2366`)
- `0x006C237C` → [KxMcheckAlternateReturn + 0x56F](KxMcheckAlternateReturn_function_006C1E00.md) (inside-function, `0x006C236F`)
- `0x006C2385` → [KxMcheckAlternateReturn + 0x578](KxMcheckAlternateReturn_function_006C1E00.md) (inside-function, `0x006C2378`)
- `0x006C238E` → [KxMcheckAlternateReturn + 0x581](KxMcheckAlternateReturn_function_006C1E00.md) (inside-function, `0x006C2381`)
- `0x006C2397` → [KxMcheckAlternateReturn + 0x58A](KxMcheckAlternateReturn_function_006C1E00.md) (inside-function, `0x006C238A`)
- `0x006C23A0` → [KxMcheckAlternateReturn + 0x593](KxMcheckAlternateReturn_function_006C1E00.md) (inside-function, `0x006C2393`)
- `0x006C23A9` → [KxMcheckAlternateReturn + 0x59C](KxMcheckAlternateReturn_function_006C1E00.md) (inside-function, `0x006C239C`)
- `0x006C23B2` → [KxMcheckAlternateReturn + 0x5A5](KxMcheckAlternateReturn_function_006C1E00.md) (inside-function, `0x006C23A5`)
- `0x006C23BB` → [KxMcheckAlternateReturn + 0x5AE](KxMcheckAlternateReturn_function_006C1E00.md) (inside-function, `0x006C23AE`)
- `0x006C23C4` → [KxMcheckAlternateReturn + 0x5B7](KxMcheckAlternateReturn_function_006C1E00.md) (inside-function, `0x006C23B7`)
- `0x006C23CD` → [KxMcheckAlternateReturn + 0x5C0](KxMcheckAlternateReturn_function_006C1E00.md) (inside-function, `0x006C23C0`)
- `0x006C23D6` → [KxMcheckAlternateReturn + 0x5C9](KxMcheckAlternateReturn_function_006C1E00.md) (inside-function, `0x006C23C9`)
- `0x006C23DF` → [KxMcheckAlternateReturn + 0x5D2](KxMcheckAlternateReturn_function_006C1E00.md) (inside-function, `0x006C23D2`)

### Direct callers
- [KxMcheckAlternateReturn](KxMcheckAlternateReturn_function_006C1E00.md) at `0x006C1F6F`
- [KxMcheckAlternateReturn](KxMcheckAlternateReturn_function_006C1E00.md) at `0x006C1F78`
- [KxMcheckAlternateReturn](KxMcheckAlternateReturn_function_006C1E00.md) at `0x006C1F81`
- [KxMcheckAlternateReturn](KxMcheckAlternateReturn_function_006C1E00.md) at `0x006C1F8A`
- [KxMcheckAlternateReturn](KxMcheckAlternateReturn_function_006C1E00.md) at `0x006C1F93`
- [KxMcheckAlternateReturn](KxMcheckAlternateReturn_function_006C1E00.md) at `0x006C1F9C`
- [KxMcheckAlternateReturn](KxMcheckAlternateReturn_function_006C1E00.md) at `0x006C1FA5`
- [KxMcheckAlternateReturn](KxMcheckAlternateReturn_function_006C1E00.md) at `0x006C1FAE`
- [KxMcheckAlternateReturn](KxMcheckAlternateReturn_function_006C1E00.md) at `0x006C1FB7`
- [KxMcheckAlternateReturn](KxMcheckAlternateReturn_function_006C1E00.md) at `0x006C1FC0`
- [KxMcheckAlternateReturn](KxMcheckAlternateReturn_function_006C1E00.md) at `0x006C1FC9`
- [KxMcheckAlternateReturn](KxMcheckAlternateReturn_function_006C1E00.md) at `0x006C1FD2`
- [KxMcheckAlternateReturn](KxMcheckAlternateReturn_function_006C1E00.md) at `0x006C1FDB`
- [KxMcheckAlternateReturn](KxMcheckAlternateReturn_function_006C1E00.md) at `0x006C1FE4`
- [KxMcheckAlternateReturn](KxMcheckAlternateReturn_function_006C1E00.md) at `0x006C1FED`
- [KxMcheckAlternateReturn](KxMcheckAlternateReturn_function_006C1E00.md) at `0x006C1FF6`
- [KxMcheckAlternateReturn](KxMcheckAlternateReturn_function_006C1E00.md) at `0x006C1FFF`
- [KxMcheckAlternateReturn](KxMcheckAlternateReturn_function_006C1E00.md) at `0x006C2008`
- [KxMcheckAlternateReturn](KxMcheckAlternateReturn_function_006C1E00.md) at `0x006C2011`
- [KxMcheckAlternateReturn](KxMcheckAlternateReturn_function_006C1E00.md) at `0x006C201A`
- [KxMcheckAlternateReturn](KxMcheckAlternateReturn_function_006C1E00.md) at `0x006C2023`
- [KxMcheckAlternateReturn](KxMcheckAlternateReturn_function_006C1E00.md) at `0x006C202C`
- [KxMcheckAlternateReturn](KxMcheckAlternateReturn_function_006C1E00.md) at `0x006C2035`
- [KxMcheckAlternateReturn](KxMcheckAlternateReturn_function_006C1E00.md) at `0x006C203E`
- [KxMcheckAlternateReturn](KxMcheckAlternateReturn_function_006C1E00.md) at `0x006C2047`
- [KxMcheckAlternateReturn](KxMcheckAlternateReturn_function_006C1E00.md) at `0x006C2050`
- [KxMcheckAlternateReturn](KxMcheckAlternateReturn_function_006C1E00.md) at `0x006C2059`
- [KxMcheckAlternateReturn](KxMcheckAlternateReturn_function_006C1E00.md) at `0x006C2062`
- [KxMcheckAlternateReturn](KxMcheckAlternateReturn_function_006C1E00.md) at `0x006C206B`
- [KxMcheckAlternateReturn](KxMcheckAlternateReturn_function_006C1E00.md) at `0x006C2074`
- [KxMcheckAlternateReturn](KxMcheckAlternateReturn_function_006C1E00.md) at `0x006C207D`
- [KxMcheckAlternateReturn](KxMcheckAlternateReturn_function_006C1E00.md) at `0x006C2086`
- [KxMcheckAlternateReturn](KxMcheckAlternateReturn_function_006C1E00.md) at `0x006C22C8`
- [KxMcheckAlternateReturn](KxMcheckAlternateReturn_function_006C1E00.md) at `0x006C22D1`
- [KxMcheckAlternateReturn](KxMcheckAlternateReturn_function_006C1E00.md) at `0x006C22DA`
- [KxMcheckAlternateReturn](KxMcheckAlternateReturn_function_006C1E00.md) at `0x006C22E3`
- [KxMcheckAlternateReturn](KxMcheckAlternateReturn_function_006C1E00.md) at `0x006C22EC`
- [KxMcheckAlternateReturn](KxMcheckAlternateReturn_function_006C1E00.md) at `0x006C22F5`
- [KxMcheckAlternateReturn](KxMcheckAlternateReturn_function_006C1E00.md) at `0x006C22FE`
- [KxMcheckAlternateReturn](KxMcheckAlternateReturn_function_006C1E00.md) at `0x006C2307`
- [KxMcheckAlternateReturn](KxMcheckAlternateReturn_function_006C1E00.md) at `0x006C2310`
- [KxMcheckAlternateReturn](KxMcheckAlternateReturn_function_006C1E00.md) at `0x006C2319`
- [KxMcheckAlternateReturn](KxMcheckAlternateReturn_function_006C1E00.md) at `0x006C2322`
- [KxMcheckAlternateReturn](KxMcheckAlternateReturn_function_006C1E00.md) at `0x006C232B`
- [KxMcheckAlternateReturn](KxMcheckAlternateReturn_function_006C1E00.md) at `0x006C2334`
- [KxMcheckAlternateReturn](KxMcheckAlternateReturn_function_006C1E00.md) at `0x006C233D`
- [KxMcheckAlternateReturn](KxMcheckAlternateReturn_function_006C1E00.md) at `0x006C2346`
- [KxMcheckAlternateReturn](KxMcheckAlternateReturn_function_006C1E00.md) at `0x006C234F`
- [KxMcheckAlternateReturn](KxMcheckAlternateReturn_function_006C1E00.md) at `0x006C2358`
- [KxMcheckAlternateReturn](KxMcheckAlternateReturn_function_006C1E00.md) at `0x006C2361`
- [KxMcheckAlternateReturn](KxMcheckAlternateReturn_function_006C1E00.md) at `0x006C236A`
- [KxMcheckAlternateReturn](KxMcheckAlternateReturn_function_006C1E00.md) at `0x006C2373`
- [KxMcheckAlternateReturn](KxMcheckAlternateReturn_function_006C1E00.md) at `0x006C237C`
- [KxMcheckAlternateReturn](KxMcheckAlternateReturn_function_006C1E00.md) at `0x006C2385`
- [KxMcheckAlternateReturn](KxMcheckAlternateReturn_function_006C1E00.md) at `0x006C238E`
- [KxMcheckAlternateReturn](KxMcheckAlternateReturn_function_006C1E00.md) at `0x006C2397`
- [KxMcheckAlternateReturn](KxMcheckAlternateReturn_function_006C1E00.md) at `0x006C23A0`
- [KxMcheckAlternateReturn](KxMcheckAlternateReturn_function_006C1E00.md) at `0x006C23A9`
- [KxMcheckAlternateReturn](KxMcheckAlternateReturn_function_006C1E00.md) at `0x006C23B2`
- [KxMcheckAlternateReturn](KxMcheckAlternateReturn_function_006C1E00.md) at `0x006C23BB`
- [KxMcheckAlternateReturn](KxMcheckAlternateReturn_function_006C1E00.md) at `0x006C23C4`
- [KxMcheckAlternateReturn](KxMcheckAlternateReturn_function_006C1E00.md) at `0x006C23CD`
- [KxMcheckAlternateReturn](KxMcheckAlternateReturn_function_006C1E00.md) at `0x006C23D6`
- [KxMcheckAlternateReturn](KxMcheckAlternateReturn_function_006C1E00.md) at `0x006C23DF`

### Static image references
- `0x006C1E00` → RVA `0x01201841` (`CFGRO`; read)
- `0x006C1E8E` → RVA `0x01201840` (`CFGRO`; read)
- `0x006C20C2` → RVA `0x00FC7264` (`ALMOSTRO`; read)
- `0x006C2133` → RVA `0x00FC6BF0` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006C2466` → [KiKernelExit](../../kvascode/BC/KiKernelExit_function_00BCCB80.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006C1E00  F6 05 3A FA B3 00 01            test byte ptr [rip + 0xb3fa3a], 1
006C1E07  74 10                           je 0x1406c1e19
006C1E09  52                              push rdx
006C1E0A  F3 48 0F 1E CA                  rdsspq rdx
006C1E0F  48 85 D2                        test rdx, rdx
006C1E12  5A                              pop rdx
006C1E13  75 04                           jne 0x1406c1e19
006C1E15  F3 0F 01 E8                     setssbsy
006C1E19  48 83 EC 08                     sub rsp, 8
006C1E1D  55                              push rbp
006C1E1E  48 81 EC 58 01 00 00            sub rsp, 0x158
006C1E25  48 8D AC 24 80 00 00 00         lea rbp, [rsp + 0x80]
006C1E2D  C6 45 AB 01                     mov byte ptr [rbp - 0x55], 1
006C1E31  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
006C1E35  48 89 4D B8                     mov qword ptr [rbp - 0x48], rcx
006C1E39  48 89 55 C0                     mov qword ptr [rbp - 0x40], rdx
006C1E3D  4C 89 45 C8                     mov qword ptr [rbp - 0x38], r8
006C1E41  4C 89 4D D0                     mov qword ptr [rbp - 0x30], r9
006C1E45  4C 89 55 D8                     mov qword ptr [rbp - 0x28], r10
006C1E49  4C 89 5D E0                     mov qword ptr [rbp - 0x20], r11
006C1E4D  F6 85 F0 00 00 00 01            test byte ptr [rbp + 0xf0], 1
006C1E54  75 38                           jne 0x1406c1e8e
006C1E56  33 D2                           xor edx, edx
006C1E58  F3 48 0F 1E CA                  rdsspq rdx
006C1E5D  48 89 55 58                     mov qword ptr [rbp + 0x58], rdx
006C1E61  0F AE E8                        lfence
006C1E64  65 F6 04 25 58 08 00 00 01      test byte ptr gs:[0x858], 1
006C1E6D  75 08                           jne 0x1406c1e77
006C1E6F  0F AE E8                        lfence
006C1E72  E9 88 02 00 00                  jmp 0x1406c20ff
006C1E77  65 0F B7 04 25 66 08 00 00      movzx eax, word ptr gs:[0x866]
006C1E80  B9 48 00 00 00                  mov ecx, 0x48
006C1E85  33 D2                           xor edx, edx
006C1E87  0F 30                           wrmsr
006C1E89  E9 71 02 00 00                  jmp 0x1406c20ff
006C1E8E  F6 05 AB F9 B3 00 01            test byte ptr [rip + 0xb3f9ab], 1
006C1E95  75 03                           jne 0x1406c1e9a
006C1E97  0F 01 F8                        swapgs
006C1E9A  0F AE E8                        lfence
006C1E9D  65 48 8B 0C 25 28 9D 00 00      mov rcx, qword ptr gs:[0x9d28]
006C1EA6  48 85 C9                        test rcx, rcx
006C1EA9  74 1F                           je 0x1406c1eca
006C1EAB  F3 48 0F 1E CA                  rdsspq rdx
006C1EB0  65 4C 8B 14 25 20 9D 00 00      mov r10, qword ptr gs:[0x9d20]
006C1EB9  49 83 C2 08                     add r10, 8
006C1EBD  49 3B D2                        cmp rdx, r10
006C1EC0  75 08                           jne 0x1406c1eca
006C1EC2  F3 0F 01 29                     rstorssp dword ptr [rcx]
006C1EC6  F3 0F 01 EA                     saveprevssp
006C1ECA  65 4C 8B 14 25 88 01 00 00      mov r10, qword ptr gs:[0x188]
006C1ED3  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006C1EDC  48 8B 89 20 02 00 00            mov rcx, qword ptr [rcx + 0x220]
006C1EE3  48 8B 89 60 07 00 00            mov rcx, qword ptr [rcx + 0x760]
006C1EEA  65 48 89 0C 25 50 08 00 00      mov qword ptr gs:[0x850], rcx
006C1EF3  66 65 8B 0C 25 62 08 00 00      mov cx, word ptr gs:[0x862]
006C1EFC  66 65 89 0C 25 64 08 00 00      mov word ptr gs:[0x864], cx
006C1F05  65 8A 0C 25 58 08 00 00         mov cl, byte ptr gs:[0x858]
006C1F0D  65 88 0C 25 5A 08 00 00         mov byte ptr gs:[0x85a], cl
006C1F15  65 0F B7 04 25 68 08 00 00      movzx eax, word ptr gs:[0x868]
006C1F1E  66 65 39 04 25 66 08 00 00      cmp word ptr gs:[0x866], ax
006C1F27  74 12                           je 0x1406c1f3b
006C1F29  66 65 89 04 25 66 08 00 00      mov word ptr gs:[0x866], ax
006C1F32  B9 48 00 00 00                  mov ecx, 0x48
006C1F37  33 D2                           xor edx, edx
006C1F39  0F 30                           wrmsr
006C1F3B  65 0F B6 14 25 58 08 00 00      movzx edx, byte ptr gs:[0x858]
006C1F44  F7 C2 08 00 00 00               test edx, 8
006C1F4A  74 17                           je 0x1406c1f63
006C1F4C  B8 01 00 00 00                  mov eax, 1
006C1F51  33 D2                           xor edx, edx
006C1F53  B9 49 00 00 00                  mov ecx, 0x49
006C1F58  0F 30                           wrmsr
006C1F5A  65 0F B6 14 25 58 08 00 00      movzx edx, byte ptr gs:[0x858]
006C1F63  F7 C2 02 00 00 00               test edx, 2
006C1F69  0F 84 37 01 00 00               je 0x1406c20a6
006C1F6F  E8 0E 01 00 00                  call 0x1406c2082
006C1F74  48 83 C4 08                     add rsp, 8
006C1F78  E8 0E 01 00 00                  call 0x1406c208b
006C1F7D  48 83 C4 08                     add rsp, 8
006C1F81  E8 EE FF FF FF                  call 0x1406c1f74
006C1F86  48 83 C4 08                     add rsp, 8
006C1F8A  E8 EE FF FF FF                  call 0x1406c1f7d
006C1F8F  48 83 C4 08                     add rsp, 8
006C1F93  E8 EE FF FF FF                  call 0x1406c1f86
006C1F98  48 83 C4 08                     add rsp, 8
006C1F9C  E8 EE FF FF FF                  call 0x1406c1f8f
006C1FA1  48 83 C4 08                     add rsp, 8
006C1FA5  E8 EE FF FF FF                  call 0x1406c1f98
006C1FAA  48 83 C4 08                     add rsp, 8
006C1FAE  E8 EE FF FF FF                  call 0x1406c1fa1
006C1FB3  48 83 C4 08                     add rsp, 8
006C1FB7  E8 EE FF FF FF                  call 0x1406c1faa
006C1FBC  48 83 C4 08                     add rsp, 8
006C1FC0  E8 EE FF FF FF                  call 0x1406c1fb3
006C1FC5  48 83 C4 08                     add rsp, 8
006C1FC9  E8 EE FF FF FF                  call 0x1406c1fbc
006C1FCE  48 83 C4 08                     add rsp, 8
006C1FD2  E8 EE FF FF FF                  call 0x1406c1fc5
006C1FD7  48 83 C4 08                     add rsp, 8
006C1FDB  E8 EE FF FF FF                  call 0x1406c1fce
006C1FE0  48 83 C4 08                     add rsp, 8
006C1FE4  E8 EE FF FF FF                  call 0x1406c1fd7
006C1FE9  48 83 C4 08                     add rsp, 8
006C1FED  E8 EE FF FF FF                  call 0x1406c1fe0
006C1FF2  48 83 C4 08                     add rsp, 8
006C1FF6  E8 EE FF FF FF                  call 0x1406c1fe9
006C1FFB  48 83 C4 08                     add rsp, 8
006C1FFF  E8 EE FF FF FF                  call 0x1406c1ff2
006C2004  48 83 C4 08                     add rsp, 8
006C2008  E8 EE FF FF FF                  call 0x1406c1ffb
006C200D  48 83 C4 08                     add rsp, 8
006C2011  E8 EE FF FF FF                  call 0x1406c2004
006C2016  48 83 C4 08                     add rsp, 8
006C201A  E8 EE FF FF FF                  call 0x1406c200d
006C201F  48 83 C4 08                     add rsp, 8
006C2023  E8 EE FF FF FF                  call 0x1406c2016
006C2028  48 83 C4 08                     add rsp, 8
006C202C  E8 EE FF FF FF                  call 0x1406c201f
006C2031  48 83 C4 08                     add rsp, 8
006C2035  E8 EE FF FF FF                  call 0x1406c2028
006C203A  48 83 C4 08                     add rsp, 8
006C203E  E8 EE FF FF FF                  call 0x1406c2031
006C2043  48 83 C4 08                     add rsp, 8
006C2047  E8 EE FF FF FF                  call 0x1406c203a
006C204C  48 83 C4 08                     add rsp, 8
006C2050  E8 EE FF FF FF                  call 0x1406c2043
006C2055  48 83 C4 08                     add rsp, 8
006C2059  E8 EE FF FF FF                  call 0x1406c204c
006C205E  48 83 C4 08                     add rsp, 8
006C2062  E8 EE FF FF FF                  call 0x1406c2055
006C2067  48 83 C4 08                     add rsp, 8
006C206B  E8 EE FF FF FF                  call 0x1406c205e
006C2070  48 83 C4 08                     add rsp, 8
006C2074  E8 EE FF FF FF                  call 0x1406c2067
006C2079  48 83 C4 08                     add rsp, 8
006C207D  E8 EE FF FF FF                  call 0x1406c2070
006C2082  48 83 C4 08                     add rsp, 8
006C2086  E8 EE FF FF FF                  call 0x1406c2079
006C208B  48 83 C4 08                     add rsp, 8
006C208F  B8 DA DA 00 00                  mov eax, 0xdada
006C2094  65 F6 04 25 5C 08 00 00 08      test byte ptr gs:[0x85c], 8
006C209D  74 07                           je 0x1406c20a6
006C209F  B0 20                           mov al, 0x20
006C20A1  F3 48 0F AE E8                  incsspq rax
006C20A6  F7 C2 80 00 00 00               test edx, 0x80
006C20AC  74 08                           je 0x1406c20b6
006C20AE  0F AE E8                        lfence
006C20B1  E8 8A 42 00 00                  call 0x1406c6340
006C20B6  0F AE E8                        lfence
006C20B9  65 C6 04 25 5E 08 00 00 00      mov byte ptr gs:[0x85e], 0
006C20C2  83 3D 9B 51 90 00 00            cmp dword ptr [rip + 0x90519b], 0
006C20C9  74 1F                           je 0x1406c20ea
006C20CB  B9 A7 06 00 00                  mov ecx, 0x6a7
006C20D0  0F 32                           rdmsr
006C20D2  83 FA 00                        cmp edx, 0
006C20D5  74 13                           je 0x1406c20ea
006C20D7  8B CA                           mov ecx, edx
006C20D9  23 15 85 51 90 00               and edx, dword ptr [rip + 0x905185]
006C20DF  3B D1                           cmp edx, ecx
006C20E1  74 07                           je 0x1406c20ea
006C20E3  B9 A7 06 00 00                  mov ecx, 0x6a7
006C20E8  0F 30                           wrmsr
006C20EA  41 F6 42 03 03                  test byte ptr [r10 + 3], 3
006C20EF  66 C7 85 80 00 00 00 00 00      mov word ptr [rbp + 0x80], 0
006C20F8  74 05                           je 0x1406c20ff
006C20FA  E8 61 B8 E3 FF                  call 0x1404fd960
006C20FF  FC                              cld
006C2100  0F AE 5D AC                     stmxcsr dword ptr [rbp - 0x54]
006C2104  65 0F AE 14 25 80 01 00 00      ldmxcsr dword ptr gs:[0x180]
006C210D  0F 29 45 F0                     movaps xmmword ptr [rbp - 0x10], xmm0
006C2111  0F 29 4D 00                     movaps xmmword ptr [rbp], xmm1
006C2115  0F 29 55 10                     movaps xmmword ptr [rbp + 0x10], xmm2
006C2119  0F 29 5D 20                     movaps xmmword ptr [rbp + 0x20], xmm3
006C211D  0F 29 65 30                     movaps xmmword ptr [rbp + 0x30], xmm4
006C2121  0F 29 6D 40                     movaps xmmword ptr [rbp + 0x40], xmm5
006C2125  F6 85 F0 00 00 00 01            test byte ptr [rbp + 0xf0], 1
006C212C  74 05                           je 0x1406c2133
006C212E  E8 6D 9E D5 FF                  call 0x14041bfa0
006C2133  F6 05 B6 4A 90 00 FF            test byte ptr [rip + 0x904ab6], 0xff
006C213A  74 0C                           je 0x1406c2148
006C213C  F6 85 F0 00 00 00 01            test byte ptr [rbp + 0xf0], 1
006C2143  74 03                           je 0x1406c2148
006C2145  0F 01 CB                        stac
006C2148  48 83 EC 30                     sub rsp, 0x30
006C214C  66 65 0F 6F 04 25 60 88 00 00   movdqa xmm0, xmmword ptr gs:[0x8860]
006C2156  66 0F 7F 44 24 20               movdqa xmmword ptr [rsp + 0x20], xmm0
006C215C  66 0F EF C0                     pxor xmm0, xmm0
006C2160  66 65 0F 7F 04 25 60 88 00 00   movdqa xmmword ptr gs:[0x8860], xmm0
006C216A  0F BA A5 F8 00 00 00 09         bt dword ptr [rbp + 0xf8], 9
006C2172  73 01                           jae 0x1406c2175
006C2174  FB                              sti
006C2175  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
006C217A  E8 01 90 F0 FF                  call 0x1405cb180
006C217F  FA                              cli
006C2180  F6 85 F0 00 00 00 01            test byte ptr [rbp + 0xf0], 1
006C2187  0F 84 F5 02 00 00               je 0x1406c2482
006C218D  F6 05 5C 4A 90 00 FF            test byte ptr [rip + 0x904a5c], 0xff
006C2194  74 03                           je 0x1406c2199
006C2196  0F 01 CB                        stac
006C2199  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006C21A2  F6 81 C2 00 00 00 03            test byte ptr [rcx + 0xc2], 3
006C21A9  74 1B                           je 0x1406c21c6
006C21AB  B9 01 00 00 00                  mov ecx, 1
006C21B0  44 0F 22 C1                     mov cr8, rcx
006C21B4  FB                              sti
006C21B5  E8 86 43 FF FF                  call 0x1406b6540
006C21BA  FA                              cli
006C21BB  B9 00 00 00 00                  mov ecx, 0
006C21C0  44 0F 22 C1                     mov cr8, rcx
006C21C4  EB D3                           jmp 0x1406c2199
006C21C6  E8 95 1D BA FF                  call 0x140263f60
006C21CB  85 C0                           test eax, eax
006C21CD  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
006C21D1  75 C6                           jne 0x1406c2199
006C21D3  65 F6 04 25 60 08 00 00 02      test byte ptr gs:[0x860], 2
006C21DC  74 07                           je 0x1406c21e5
006C21DE  33 C9                           xor ecx, ecx
006C21E0  E8 DB 4F D2 FF                  call 0x1403e71c0
006C21E5  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006C21EE  F7 01 00 00 00 08               test dword ptr [rcx], 0x8000000
006C21F4  74 05                           je 0x1406c21fb
006C21F6  E8 A5 FA FE FF                  call 0x1406b1ca0
006C21FB  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006C2204  F7 01 00 00 01 00               test dword ptr [rcx], 0x10000
006C220A  74 14                           je 0x1406c2220
006C220C  F6 41 02 01                     test byte ptr [rcx + 2], 1
006C2210  74 0E                           je 0x1406c2220
006C2212  E8 F9 E4 EF FF                  call 0x1405c0710
006C2217  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006C2220  0F AE 55 AC                     ldmxcsr dword ptr [rbp - 0x54]
006C2224  66 83 BD 80 00 00 00 00         cmp word ptr [rbp + 0x80], 0
006C222C  74 05                           je 0x1406c2233
006C222E  E8 AD B6 E3 FF                  call 0x1404fd8e0
006C2233  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006C223C  0F BA 61 74 16                  bt dword ptr [rcx + 0x74], 0x16
006C2241  73 2A                           jae 0x1406c226d
006C2243  33 C9                           xor ecx, ecx
006C2245  F3 48 0F 1E C9                  rdsspq rcx
006C224A  65 4C 8B 04 25 28 9D 00 00      mov r8, qword ptr gs:[0x9d28]
006C2253  49 83 C0 08                     add r8, 8
006C2257  49 3B C8                        cmp rcx, r8
006C225A  75 11                           jne 0x1406c226d
006C225C  65 48 8B 0C 25 20 9D 00 00      mov rcx, qword ptr gs:[0x9d20]
006C2265  F3 0F 01 29                     rstorssp dword ptr [rcx]
006C2269  F3 0F 01 EA                     saveprevssp
006C226D  65 C6 04 25 5E 08 00 00 00      mov byte ptr gs:[0x85e], 0
006C2276  65 0F B7 04 25 6C 08 00 00      movzx eax, word ptr gs:[0x86c]
006C227F  66 65 39 04 25 66 08 00 00      cmp word ptr gs:[0x866], ax
006C2288  74 12                           je 0x1406c229c
006C228A  66 65 89 04 25 66 08 00 00      mov word ptr gs:[0x866], ax
006C2293  B9 48 00 00 00                  mov ecx, 0x48
006C2298  33 D2                           xor edx, edx
006C229A  0F 30                           wrmsr
006C229C  66 65 0F BA 34 25 58 08 00 00 02  btr word ptr gs:[0x858], 2
006C22A7  73 0E                           jae 0x1406c22b7
006C22A9  B8 01 00 00 00                  mov eax, 1
006C22AE  33 D2                           xor edx, edx
006C22B0  B9 49 00 00 00                  mov ecx, 0x49
006C22B5  0F 30                           wrmsr
006C22B7  66 65 0F BA 34 25 58 08 00 00 05  btr word ptr gs:[0x858], 5
006C22C2  0F 83 37 01 00 00               jae 0x1406c23ff
006C22C8  E8 0E 01 00 00                  call 0x1406c23db
006C22CD  48 83 C4 08                     add rsp, 8
006C22D1  E8 0E 01 00 00                  call 0x1406c23e4
006C22D6  48 83 C4 08                     add rsp, 8
006C22DA  E8 EE FF FF FF                  call 0x1406c22cd
006C22DF  48 83 C4 08                     add rsp, 8
006C22E3  E8 EE FF FF FF                  call 0x1406c22d6
006C22E8  48 83 C4 08                     add rsp, 8
006C22EC  E8 EE FF FF FF                  call 0x1406c22df
006C22F1  48 83 C4 08                     add rsp, 8
006C22F5  E8 EE FF FF FF                  call 0x1406c22e8
006C22FA  48 83 C4 08                     add rsp, 8
006C22FE  E8 EE FF FF FF                  call 0x1406c22f1
006C2303  48 83 C4 08                     add rsp, 8
006C2307  E8 EE FF FF FF                  call 0x1406c22fa
006C230C  48 83 C4 08                     add rsp, 8
006C2310  E8 EE FF FF FF                  call 0x1406c2303
006C2315  48 83 C4 08                     add rsp, 8
006C2319  E8 EE FF FF FF                  call 0x1406c230c
006C231E  48 83 C4 08                     add rsp, 8
006C2322  E8 EE FF FF FF                  call 0x1406c2315
006C2327  48 83 C4 08                     add rsp, 8
006C232B  E8 EE FF FF FF                  call 0x1406c231e
006C2330  48 83 C4 08                     add rsp, 8
006C2334  E8 EE FF FF FF                  call 0x1406c2327
006C2339  48 83 C4 08                     add rsp, 8
006C233D  E8 EE FF FF FF                  call 0x1406c2330
006C2342  48 83 C4 08                     add rsp, 8
006C2346  E8 EE FF FF FF                  call 0x1406c2339
006C234B  48 83 C4 08                     add rsp, 8
006C234F  E8 EE FF FF FF                  call 0x1406c2342
006C2354  48 83 C4 08                     add rsp, 8
006C2358  E8 EE FF FF FF                  call 0x1406c234b
006C235D  48 83 C4 08                     add rsp, 8
006C2361  E8 EE FF FF FF                  call 0x1406c2354
006C2366  48 83 C4 08                     add rsp, 8
006C236A  E8 EE FF FF FF                  call 0x1406c235d
006C236F  48 83 C4 08                     add rsp, 8
006C2373  E8 EE FF FF FF                  call 0x1406c2366
006C2378  48 83 C4 08                     add rsp, 8
006C237C  E8 EE FF FF FF                  call 0x1406c236f
006C2381  48 83 C4 08                     add rsp, 8
006C2385  E8 EE FF FF FF                  call 0x1406c2378
006C238A  48 83 C4 08                     add rsp, 8
006C238E  E8 EE FF FF FF                  call 0x1406c2381
006C2393  48 83 C4 08                     add rsp, 8
006C2397  E8 EE FF FF FF                  call 0x1406c238a
006C239C  48 83 C4 08                     add rsp, 8
006C23A0  E8 EE FF FF FF                  call 0x1406c2393
006C23A5  48 83 C4 08                     add rsp, 8
006C23A9  E8 EE FF FF FF                  call 0x1406c239c
006C23AE  48 83 C4 08                     add rsp, 8
006C23B2  E8 EE FF FF FF                  call 0x1406c23a5
006C23B7  48 83 C4 08                     add rsp, 8
006C23BB  E8 EE FF FF FF                  call 0x1406c23ae
006C23C0  48 83 C4 08                     add rsp, 8
006C23C4  E8 EE FF FF FF                  call 0x1406c23b7
006C23C9  48 83 C4 08                     add rsp, 8
006C23CD  E8 EE FF FF FF                  call 0x1406c23c0
006C23D2  48 83 C4 08                     add rsp, 8
006C23D6  E8 EE FF FF FF                  call 0x1406c23c9
006C23DB  48 83 C4 08                     add rsp, 8
006C23DF  E8 EE FF FF FF                  call 0x1406c23d2
006C23E4  48 83 C4 08                     add rsp, 8
006C23E8  B8 DA DA 00 00                  mov eax, 0xdada
006C23ED  65 F6 04 25 5C 08 00 00 08      test byte ptr gs:[0x85c], 8
006C23F6  74 07                           je 0x1406c23ff
006C23F8  B0 20                           mov al, 0x20
006C23FA  F3 48 0F AE E8                  incsspq rax
006C23FF  66 65 F7 04 25 58 08 00 00 00 01  test word ptr gs:[0x858], 0x100
006C240A  74 0C                           je 0x1406c2418
006C240C  33 C0                           xor eax, eax
006C240E  33 D2                           xor edx, edx
006C2410  B9 01 00 00 00                  mov ecx, 1
006C2415  48 F7 F1                        div rcx
006C2418  0F 28 45 F0                     movaps xmm0, xmmword ptr [rbp - 0x10]
006C241C  0F 28 4D 00                     movaps xmm1, xmmword ptr [rbp]
006C2420  0F 28 55 10                     movaps xmm2, xmmword ptr [rbp + 0x10]
006C2424  0F 28 5D 20                     movaps xmm3, xmmword ptr [rbp + 0x20]
006C2428  0F 28 65 30                     movaps xmm4, xmmword ptr [rbp + 0x30]
006C242C  0F 28 6D 40                     movaps xmm5, xmmword ptr [rbp + 0x40]
006C2430  4C 8B 5D E0                     mov r11, qword ptr [rbp - 0x20]
006C2434  4C 8B 55 D8                     mov r10, qword ptr [rbp - 0x28]
006C2438  4C 8B 4D D0                     mov r9, qword ptr [rbp - 0x30]
006C243C  4C 8B 45 C8                     mov r8, qword ptr [rbp - 0x38]
006C2440  48 8B 55 C0                     mov rdx, qword ptr [rbp - 0x40]
006C2444  48 8B 4D B8                     mov rcx, qword ptr [rbp - 0x48]
006C2448  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
006C244C  48 8B E5                        mov rsp, rbp
006C244F  48 8B AD D8 00 00 00            mov rbp, qword ptr [rbp + 0xd8]
006C2456  48 81 C4 E8 00 00 00            add rsp, 0xe8
006C245D  F6 05 DC F3 B3 00 01            test byte ptr [rip + 0xb3f3dc], 1
006C2464  74 05                           je 0x1406c246b
006C2466  E9 15 A7 50 00                  jmp 0x140bccb80
006C246B  66 65 F7 04 25 58 08 00 00 00 02  test word ptr gs:[0x858], 0x200
006C2476  74 05                           je 0x1406c247d
006C2478  0F 00 6C 24 20                  verw word ptr [rsp + 0x20]
006C247D  0F 01 F8                        swapgs
006C2480  48 CF                           iretq
006C2482  0F AE 55 AC                     ldmxcsr dword ptr [rbp - 0x54]
006C2486  0F 28 45 F0                     movaps xmm0, xmmword ptr [rbp - 0x10]
006C248A  0F 28 4D 00                     movaps xmm1, xmmword ptr [rbp]
006C248E  0F 28 55 10                     movaps xmm2, xmmword ptr [rbp + 0x10]
006C2492  0F 28 5D 20                     movaps xmm3, xmmword ptr [rbp + 0x20]
006C2496  0F 28 65 30                     movaps xmm4, xmmword ptr [rbp + 0x30]
006C249A  0F 28 6D 40                     movaps xmm5, xmmword ptr [rbp + 0x40]
006C249E  4C 8B 5D E0                     mov r11, qword ptr [rbp - 0x20]
006C24A2  4C 8B 55 D8                     mov r10, qword ptr [rbp - 0x28]
006C24A6  4C 8B 4D D0                     mov r9, qword ptr [rbp - 0x30]
006C24AA  4C 8B 45 C8                     mov r8, qword ptr [rbp - 0x38]
006C24AE  48 8B 55 C0                     mov rdx, qword ptr [rbp - 0x40]
006C24B2  48 8B 4D B8                     mov rcx, qword ptr [rbp - 0x48]
006C24B6  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
006C24BA  48 8B E5                        mov rsp, rbp
006C24BD  48 8B AD D8 00 00 00            mov rbp, qword ptr [rbp + 0xd8]
006C24C4  48 81 C4 E8 00 00 00            add rsp, 0xe8
006C24CB  48 CF                           iretq
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KxMcheckAlternateReturn(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned int v_stack_m13C;
    unsigned __int8 v_stack_m13D;
    unsigned __int16 v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF8;
    unsigned int v_stack_p10;
    unsigned __int16 v_stack_p20;
    unsigned __int8 v_stack_p8;

    if (((*(unsigned __int8 *)(v_rip + 11795002)) & (1)) == 0) goto loc_006C1E19;
    if (a2 == 0) {
    }
    v_rsp = (v_rsp) - (8);
    v_rsp = (v_rsp) - (344);
    v_stack_m13D = 1;
    v_stack_m138 = result;
    v_stack_m130 = a1;
    v_stack_m128 = a2;
    v_stack_m120 = a3;
    v_stack_m118 = a4;
    v_stack_m110 = v_r10;
    v_stack_m108 = v_r11;
    if (((v_stack_p8) & (1)) != 0) goto loc_006C1E8E;
    a2 = 0;
    v_stack_m90 = 0;
    if (((*(unsigned __int8 *)(gs_base + (0 + 2136))) & (1)) != 0) goto loc_006C1E77;
    goto loc_006C20FF;
loc_006C1E77:
    a2 = 0;
    goto loc_006C20FF;
loc_006C1E8E:
    if (((*(unsigned __int8 *)(v_rip + 11794859)) & (1)) == 0) {
    }
    if (*(unsigned __int64 *)(gs_base + (0 + 40232)) == 0) goto loc_006C1ECA;
    v_r10 = (*(unsigned __int64 *)(gs_base + (0 + 40224))) + (8);
    if (0 == v_r10) {
    }
    *(unsigned __int64 *)(gs_base + (0 + 2128)) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544) + 1888);
    *(unsigned __int16 *)(gs_base + (0 + 2148)) = (unsigned __int16)(*(unsigned __int16 *)(gs_base + (0 + 2146)));
    *(unsigned __int8 *)(gs_base + (0 + 2138)) = (unsigned __int8)(*(unsigned __int8 *)(gs_base + (0 + 2136)));
    if ((*(unsigned __int16 *)(gs_base + (0 + 2150))) != ((unsigned __int16)(*(unsigned __int16 *)(gs_base + (0 + 2152))))) {
        *(unsigned __int16 *)(gs_base + (0 + 2150)) = (unsigned __int16)(*(unsigned __int16 *)(gs_base + (0 + 2152)));
        a1 = 72;
        a2 = 0;
    }
    result = *(unsigned __int16 *)(gs_base + (0 + 2152));
    if ((((unsigned int)(*(unsigned __int8 *)(gs_base + (0 + 2136)))) & (8)) != 0) {
        result = 1;
        a2 = 0;
        a1 = 73;
        a2 = *(unsigned __int8 *)(gs_base + (0 + 2136));
    }
    if ((((unsigned int)(a2)) & (2)) == 0) goto loc_006C20A6;
    result = KxMcheckAlternateReturn___0x282(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxMcheckAlternateReturn___0x28B(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxMcheckAlternateReturn___0x174(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxMcheckAlternateReturn___0x17D(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxMcheckAlternateReturn___0x186(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxMcheckAlternateReturn___0x18F(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxMcheckAlternateReturn___0x198(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxMcheckAlternateReturn___0x1A1(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxMcheckAlternateReturn___0x1AA(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxMcheckAlternateReturn___0x1B3(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxMcheckAlternateReturn___0x1BC(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxMcheckAlternateReturn___0x1C5(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxMcheckAlternateReturn___0x1CE(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxMcheckAlternateReturn___0x1D7(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxMcheckAlternateReturn___0x1E0(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxMcheckAlternateReturn___0x1E9(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxMcheckAlternateReturn___0x1F2(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxMcheckAlternateReturn___0x1FB(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxMcheckAlternateReturn___0x204(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxMcheckAlternateReturn___0x20D(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxMcheckAlternateReturn___0x216(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxMcheckAlternateReturn___0x21F(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxMcheckAlternateReturn___0x228(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxMcheckAlternateReturn___0x231(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxMcheckAlternateReturn___0x23A(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxMcheckAlternateReturn___0x243(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxMcheckAlternateReturn___0x24C(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxMcheckAlternateReturn___0x255(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxMcheckAlternateReturn___0x25E(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxMcheckAlternateReturn___0x267(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxMcheckAlternateReturn___0x270(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxMcheckAlternateReturn___0x279(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = (unsigned int)(0xDADAULL);
    if (((*(unsigned __int8 *)(gs_base + (0 + 2140))) & (8)) != 0) {
        result = 32;
    }
    if ((((unsigned int)(a2)) & (128)) != 0) {
        result = KiFlushBhbDuringTrapEntryOrExit(a1, a2, a3, a4);
    }
    *(unsigned __int8 *)(gs_base + (0 + 2142)) = 0;
    if ((*(unsigned int *)(v_rip + 9458075)) == 0) goto loc_006C20EA;
    if (((unsigned int)(a2)) == 0) goto loc_006C20EA;
    a2 = (unsigned int)((a2) & (*(unsigned int *)(v_rip + 9458053)));
    if (((unsigned int)(a2)) != ((unsigned int)((unsigned int)((unsigned int)(a2))))) {
        a1 = 0x6A7ULL;
    }
    v_stack_m68 = 0;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 3)) & (3)) != 0) {
        result = KiSaveDebugRegisterState(a1, a2, a3, a4);
    }
    v_stack_mF8 = v_xmm0;
    v_stack_mE8 = v_xmm1;
    v_stack_mD8 = v_xmm2;
    v_stack_mC8 = v_xmm3;
    v_stack_mB8 = v_xmm4;
    v_stack_mA8 = v_xmm5;
    if (((v_stack_p8) & (1)) != 0) {
        result = KiSynchronizeUserIsolationDomainExit(a1, a2, a3, a4);
    }
    if (((*(unsigned __int8 *)(v_rip + 9456310)) & (255)) == 0) goto loc_006C2148;
    if (((v_stack_p8) & (1)) != 0) {
    }
    v_rsp = (v_rsp) - (48);
    v_stack_m78 = v_xmm0;
    *(unsigned __int64 *)(gs_base + (0 + 34912)) = v_xmm0;
    if (!(condition_is_above_or_equal)) {
    }
    result = KiMcheckAlternateReturn(v_stack_m78, a2, a3, a4);
    if (((v_stack_p8) & (1)) == 0) goto loc_006C2482;
    if (((*(unsigned __int8 *)(v_rip + 9456220)) & (255)) != 0) {
    }
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 194)) & (3)) == 0) goto loc_006C21C6;
    result = KiInitiateUserApc(1, a2, a3, a4);
    goto loc_006C2199;
loc_006C21C6:
    result = KiSynchronizeUserIsolationDomainEntry(0, a2, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_006C2199;
    result = v_stack_m138;
    if (((*(unsigned __int8 *)(gs_base + (0 + 2144))) & (2)) != 0) {
        a1 = 0;
        result = KiUpdateStibpPairing(a1, a2, a3, a4);
    }
    if (((*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)))) & (0x8000000ULL)) != 0) {
        result = KiRestoreSetContextState(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, a4);
    }
    if (((*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)))) & (0x10000ULL)) == 0) goto loc_006C2220;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 2)) & (1)) != 0) {
        result = KiCopyCounters(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, a4);
        a1 = *(unsigned __int64 *)(gs_base + (0 + 392));
    }
    if (v_stack_m68 != 0) {
        result = KiRestoreDebugRegisterState(a1, a2, a3, a4);
    }
    if (v_stack_m68 >= 0) goto loc_006C226D;
    a1 = 0;
    a3 = (*(unsigned __int64 *)(gs_base + (0 + 40232))) + (8);
    if (0 == a3) {
        a1 = *(unsigned __int64 *)(gs_base + (0 + 40224));
    }
    *(unsigned __int8 *)(gs_base + (0 + 2142)) = 0;
    if ((*(unsigned __int16 *)(gs_base + (0 + 2150))) != ((unsigned __int16)(*(unsigned __int16 *)(gs_base + (0 + 2156))))) {
        *(unsigned __int16 *)(gs_base + (0 + 2150)) = (unsigned __int16)(*(unsigned __int16 *)(gs_base + (0 + 2156)));
        a1 = 72;
        a2 = 0;
    }
    result = *(unsigned __int16 *)(gs_base + (0 + 2156));
    if (!(condition_is_above_or_equal)) {
        result = 1;
        a2 = 0;
        a1 = 73;
    }
    if (condition_is_above_or_equal) goto loc_006C23FF;
    result = KxMcheckAlternateReturn___0x5DB(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxMcheckAlternateReturn___0x5E4(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxMcheckAlternateReturn___0x4CD(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxMcheckAlternateReturn___0x4D6(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxMcheckAlternateReturn___0x4DF(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxMcheckAlternateReturn___0x4E8(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxMcheckAlternateReturn___0x4F1(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxMcheckAlternateReturn___0x4FA(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxMcheckAlternateReturn___0x503(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxMcheckAlternateReturn___0x50C(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxMcheckAlternateReturn___0x515(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxMcheckAlternateReturn___0x51E(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxMcheckAlternateReturn___0x527(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxMcheckAlternateReturn___0x530(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxMcheckAlternateReturn___0x539(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxMcheckAlternateReturn___0x542(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxMcheckAlternateReturn___0x54B(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxMcheckAlternateReturn___0x554(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxMcheckAlternateReturn___0x55D(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxMcheckAlternateReturn___0x566(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxMcheckAlternateReturn___0x56F(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxMcheckAlternateReturn___0x578(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxMcheckAlternateReturn___0x581(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxMcheckAlternateReturn___0x58A(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxMcheckAlternateReturn___0x593(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxMcheckAlternateReturn___0x59C(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxMcheckAlternateReturn___0x5A5(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxMcheckAlternateReturn___0x5AE(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxMcheckAlternateReturn___0x5B7(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxMcheckAlternateReturn___0x5C0(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxMcheckAlternateReturn___0x5C9(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxMcheckAlternateReturn___0x5D2(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = (unsigned int)(0xDADAULL);
    if (((*(unsigned __int8 *)(gs_base + (0 + 2140))) & (8)) != 0) {
        result = 32;
    }
    if (((*(unsigned __int16 *)(gs_base + (0 + 2136))) & (256)) != 0) {
        result = 0;
        a2 = 0;
        a1 = 1;
    }
    v_rsp = (v_stack_mE8) + (232);
    if (((*(unsigned __int8 *)(v_rip + 11793372)) & (1)) == 0) goto loc_006C246B;
loc_006C246B:
    if (((*(unsigned __int16 *)(gs_base + (0 + 2136))) & (512)) != 0) {
    }
loc_006C2482:
    v_rsp = (v_stack_m10) + (232);
    return v_stack_m138;
}
```

## 5. (Beta) C Style

```c
int64_t KxMcheckAlternateReturn(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint32_t v_stack_m13C;
    uint8_t v_stack_m13D;
    uint16_t v_stack_m68;
    uint64_t v_stack_m78;
    uint64_t v_stack_m90;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF8;
    uint32_t v_stack_p10;
    uint16_t v_stack_p20;
    uint8_t v_stack_p8;

    if (((*(uint8_t *)(v_rip + 0xB3FA3A)) & (1)) == 0) goto loc_006C1E19;
    if (Arg2 == 0) {
    }
    local_rsp = (local_rsp) - (8);
    local_rsp = (local_rsp) - (344);
    v_stack_m13D = 1;
    v_stack_m138 = result;
    v_stack_m130 = Arg1;
    v_stack_m128 = Arg2;
    v_stack_m120 = Arg3;
    v_stack_m118 = Arg4;
    v_stack_m110 = local_r10;
    v_stack_m108 = local_r11;
    if (((v_stack_p8) & (1)) != 0) goto loc_006C1E8E;
    Arg2 = 0;
    v_stack_m90 = 0;
    if (((*(uint8_t *)(gs_base + (0 + 0x858))) & (1)) != 0) goto loc_006C1E77;
    goto loc_006C20FF;
loc_006C1E77:
    Arg2 = 0;
    goto loc_006C20FF;
loc_006C1E8E:
    if (((*(uint8_t *)(v_rip + 0xB3F9AB)) & (1)) == 0) {
    }
    if (*(uint64_t *)(gs_base + (0 + 0x9D28)) == 0) goto loc_006C1ECA;
    local_r10 = (*(uint64_t *)(gs_base + (0 + 0x9D20))) + (8);
    if (0 == local_r10) {
    }
    *(uint64_t *)(gs_base + (0 + 0x850)) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220) + 0x760);
    *(uint16_t *)(gs_base + (0 + 0x864)) = (uint16_t)(*(uint16_t *)(gs_base + (0 + 0x862)));
    *(uint8_t *)(gs_base + (0 + 0x85A)) = (uint8_t)(*(uint8_t *)(gs_base + (0 + 0x858)));
    if ((*(uint16_t *)(gs_base + (0 + 0x866))) != ((uint16_t)(*(uint16_t *)(gs_base + (0 + 0x868))))) {
        *(uint16_t *)(gs_base + (0 + 0x866)) = (uint16_t)(*(uint16_t *)(gs_base + (0 + 0x868)));
        Arg1 = 72;
        Arg2 = 0;
    }
    result = *(uint16_t *)(gs_base + (0 + 0x868));
    if ((((uint32_t)(*(uint8_t *)(gs_base + (0 + 0x858)))) & (8)) != 0) {
        result = 1;
        Arg2 = 0;
        Arg1 = 73;
        Arg2 = *(uint8_t *)(gs_base + (0 + 0x858));
    }
    if ((((uint32_t)(Arg2)) & (2)) == 0) goto loc_006C20A6;
    result = KxMcheckAlternateReturn___0x282(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxMcheckAlternateReturn___0x28B(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxMcheckAlternateReturn___0x174(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxMcheckAlternateReturn___0x17D(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxMcheckAlternateReturn___0x186(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxMcheckAlternateReturn___0x18F(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxMcheckAlternateReturn___0x198(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxMcheckAlternateReturn___0x1A1(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxMcheckAlternateReturn___0x1AA(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxMcheckAlternateReturn___0x1B3(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxMcheckAlternateReturn___0x1BC(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxMcheckAlternateReturn___0x1C5(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxMcheckAlternateReturn___0x1CE(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxMcheckAlternateReturn___0x1D7(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxMcheckAlternateReturn___0x1E0(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxMcheckAlternateReturn___0x1E9(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxMcheckAlternateReturn___0x1F2(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxMcheckAlternateReturn___0x1FB(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxMcheckAlternateReturn___0x204(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxMcheckAlternateReturn___0x20D(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxMcheckAlternateReturn___0x216(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxMcheckAlternateReturn___0x21F(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxMcheckAlternateReturn___0x228(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxMcheckAlternateReturn___0x231(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxMcheckAlternateReturn___0x23A(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxMcheckAlternateReturn___0x243(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxMcheckAlternateReturn___0x24C(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxMcheckAlternateReturn___0x255(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxMcheckAlternateReturn___0x25E(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxMcheckAlternateReturn___0x267(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxMcheckAlternateReturn___0x270(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxMcheckAlternateReturn___0x279(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = (uint32_t)(0xDADAULL);
    if (((*(uint8_t *)(gs_base + (0 + 0x85C))) & (8)) != 0) {
        result = 32;
    }
    if ((((uint32_t)(Arg2)) & (128)) != 0) {
        result = KiFlushBhbDuringTrapEntryOrExit(Arg1, Arg2, Arg3, Arg4);
    }
    *(uint8_t *)(gs_base + (0 + 0x85E)) = 0;
    if ((*(uint32_t *)(v_rip + 0x90519B)) == 0) goto loc_006C20EA;
    if (((uint32_t)(Arg2)) == 0) goto loc_006C20EA;
    Arg2 = (uint32_t)((Arg2) & (*(uint32_t *)(v_rip + 0x905185)));
    if (((uint32_t)(Arg2)) != ((uint32_t)((uint32_t)((uint32_t)(Arg2))))) {
        Arg1 = 0x6A7ULL;
    }
    v_stack_m68 = 0;
    if (((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x3)) & (3)) != 0) {
        result = KiSaveDebugRegisterState(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_mF8 = v_xmm0;
    v_stack_mE8 = v_xmm1;
    v_stack_mD8 = v_xmm2;
    v_stack_mC8 = v_xmm3;
    v_stack_mB8 = v_xmm4;
    v_stack_mA8 = v_xmm5;
    if (((v_stack_p8) & (1)) != 0) {
        result = KiSynchronizeUserIsolationDomainExit(Arg1, Arg2, Arg3, Arg4);
    }
    if (((*(uint8_t *)(v_rip + 0x904AB6)) & (255)) == 0) goto loc_006C2148;
    if (((v_stack_p8) & (1)) != 0) {
    }
    local_rsp = (local_rsp) - (48);
    v_stack_m78 = v_xmm0;
    *(uint64_t *)(gs_base + (0 + 0x8860)) = v_xmm0;
    if (!(condition_is_above_or_equal)) {
    }
    result = KiMcheckAlternateReturn(v_stack_m78, Arg2, Arg3, Arg4);
    if (((v_stack_p8) & (1)) == 0) goto loc_006C2482;
    if (((*(uint8_t *)(v_rip + 0x904A5C)) & (255)) != 0) {
    }
    if (((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xC2)) & (3)) == 0) goto loc_006C21C6;
    result = KiInitiateUserApc(1, Arg2, Arg3, Arg4);
    goto loc_006C2199;
loc_006C21C6:
    result = KiSynchronizeUserIsolationDomainEntry(0, Arg2, Arg3, Arg4);
    if ((uint32_t)(result) != 0) goto loc_006C2199;
    result = v_stack_m138;
    if (((*(uint8_t *)(gs_base + (0 + 0x860))) & (2)) != 0) {
        Arg1 = 0;
        result = KiUpdateStibpPairing(Arg1, Arg2, Arg3, Arg4);
    }
    if (((*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)))) & (0x8000000ULL)) != 0) {
        result = KiRestoreSetContextState(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, Arg3, Arg4);
    }
    if (((*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)))) & (0x10000ULL)) == 0) goto loc_006C2220;
    if (((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x2)) & (1)) != 0) {
        result = KiCopyCounters(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, Arg3, Arg4);
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x188));
    }
    if (v_stack_m68 != 0) {
        result = KiRestoreDebugRegisterState(Arg1, Arg2, Arg3, Arg4);
    }
    if (v_stack_m68 >= 0) goto loc_006C226D;
    Arg1 = 0;
    Arg3 = (*(uint64_t *)(gs_base + (0 + 0x9D28))) + (8);
    if (0 == Arg3) {
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x9D20));
    }
    *(uint8_t *)(gs_base + (0 + 0x85E)) = 0;
    if ((*(uint16_t *)(gs_base + (0 + 0x866))) != ((uint16_t)(*(uint16_t *)(gs_base + (0 + 0x86C))))) {
        *(uint16_t *)(gs_base + (0 + 0x866)) = (uint16_t)(*(uint16_t *)(gs_base + (0 + 0x86C)));
        Arg1 = 72;
        Arg2 = 0;
    }
    result = *(uint16_t *)(gs_base + (0 + 0x86C));
    if (!(condition_is_above_or_equal)) {
        result = 1;
        Arg2 = 0;
        Arg1 = 73;
    }
    if (condition_is_above_or_equal) goto loc_006C23FF;
    result = KxMcheckAlternateReturn___0x5DB(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxMcheckAlternateReturn___0x5E4(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxMcheckAlternateReturn___0x4CD(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxMcheckAlternateReturn___0x4D6(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxMcheckAlternateReturn___0x4DF(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxMcheckAlternateReturn___0x4E8(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxMcheckAlternateReturn___0x4F1(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxMcheckAlternateReturn___0x4FA(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxMcheckAlternateReturn___0x503(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxMcheckAlternateReturn___0x50C(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxMcheckAlternateReturn___0x515(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxMcheckAlternateReturn___0x51E(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxMcheckAlternateReturn___0x527(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxMcheckAlternateReturn___0x530(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxMcheckAlternateReturn___0x539(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxMcheckAlternateReturn___0x542(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxMcheckAlternateReturn___0x54B(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxMcheckAlternateReturn___0x554(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxMcheckAlternateReturn___0x55D(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxMcheckAlternateReturn___0x566(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxMcheckAlternateReturn___0x56F(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxMcheckAlternateReturn___0x578(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxMcheckAlternateReturn___0x581(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxMcheckAlternateReturn___0x58A(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxMcheckAlternateReturn___0x593(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxMcheckAlternateReturn___0x59C(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxMcheckAlternateReturn___0x5A5(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxMcheckAlternateReturn___0x5AE(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxMcheckAlternateReturn___0x5B7(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxMcheckAlternateReturn___0x5C0(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxMcheckAlternateReturn___0x5C9(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxMcheckAlternateReturn___0x5D2(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = (uint32_t)(0xDADAULL);
    if (((*(uint8_t *)(gs_base + (0 + 0x85C))) & (8)) != 0) {
        result = 32;
    }
    if (((*(uint16_t *)(gs_base + (0 + 0x858))) & (256)) != 0) {
        result = 0;
        Arg2 = 0;
        Arg1 = 1;
    }
    local_rsp = (v_stack_mE8) + (232);
    if (((*(uint8_t *)(v_rip + 0xB3F3DC)) & (1)) == 0) goto loc_006C246B;
loc_006C246B:
    if (((*(uint16_t *)(gs_base + (0 + 0x858))) & (512)) != 0) {
    }
loc_006C2482:
    local_rsp = (v_stack_m10) + (232);
    return v_stack_m138;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006C1E00&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
