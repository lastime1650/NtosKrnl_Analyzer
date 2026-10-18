# KiVirtualizationException

- RVA: `0x006C2900`–`0x006C3015` (길이 `1,813` bytes)
- VA: `0x00000001406C2900`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C1D58`
- 디코드: `390`개 명령, `1,813/1,813` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **78**; 고유 호출 대상: **78**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x006C2A56` → [KiVirtualizationException + 0x269](KiVirtualizationException_function_006C2900.md) (inside-function, `0x006C2B69`)
- `0x006C2A5F` → [KiVirtualizationException + 0x272](KiVirtualizationException_function_006C2900.md) (inside-function, `0x006C2B72`)
- `0x006C2A68` → [KiVirtualizationException + 0x15B](KiVirtualizationException_function_006C2900.md) (inside-function, `0x006C2A5B`)
- `0x006C2A71` → [KiVirtualizationException + 0x164](KiVirtualizationException_function_006C2900.md) (inside-function, `0x006C2A64`)
- `0x006C2A7A` → [KiVirtualizationException + 0x16D](KiVirtualizationException_function_006C2900.md) (inside-function, `0x006C2A6D`)
- `0x006C2A83` → [KiVirtualizationException + 0x176](KiVirtualizationException_function_006C2900.md) (inside-function, `0x006C2A76`)
- `0x006C2A8C` → [KiVirtualizationException + 0x17F](KiVirtualizationException_function_006C2900.md) (inside-function, `0x006C2A7F`)
- `0x006C2A95` → [KiVirtualizationException + 0x188](KiVirtualizationException_function_006C2900.md) (inside-function, `0x006C2A88`)
- `0x006C2A9E` → [KiVirtualizationException + 0x191](KiVirtualizationException_function_006C2900.md) (inside-function, `0x006C2A91`)
- `0x006C2AA7` → [KiVirtualizationException + 0x19A](KiVirtualizationException_function_006C2900.md) (inside-function, `0x006C2A9A`)
- `0x006C2AB0` → [KiVirtualizationException + 0x1A3](KiVirtualizationException_function_006C2900.md) (inside-function, `0x006C2AA3`)
- `0x006C2AB9` → [KiVirtualizationException + 0x1AC](KiVirtualizationException_function_006C2900.md) (inside-function, `0x006C2AAC`)
- `0x006C2AC2` → [KiVirtualizationException + 0x1B5](KiVirtualizationException_function_006C2900.md) (inside-function, `0x006C2AB5`)
- `0x006C2ACB` → [KiVirtualizationException + 0x1BE](KiVirtualizationException_function_006C2900.md) (inside-function, `0x006C2ABE`)
- `0x006C2AD4` → [KiVirtualizationException + 0x1C7](KiVirtualizationException_function_006C2900.md) (inside-function, `0x006C2AC7`)
- `0x006C2ADD` → [KiVirtualizationException + 0x1D0](KiVirtualizationException_function_006C2900.md) (inside-function, `0x006C2AD0`)
- `0x006C2AE6` → [KiVirtualizationException + 0x1D9](KiVirtualizationException_function_006C2900.md) (inside-function, `0x006C2AD9`)
- `0x006C2AEF` → [KiVirtualizationException + 0x1E2](KiVirtualizationException_function_006C2900.md) (inside-function, `0x006C2AE2`)
- `0x006C2AF8` → [KiVirtualizationException + 0x1EB](KiVirtualizationException_function_006C2900.md) (inside-function, `0x006C2AEB`)
- `0x006C2B01` → [KiVirtualizationException + 0x1F4](KiVirtualizationException_function_006C2900.md) (inside-function, `0x006C2AF4`)
- `0x006C2B0A` → [KiVirtualizationException + 0x1FD](KiVirtualizationException_function_006C2900.md) (inside-function, `0x006C2AFD`)
- `0x006C2B13` → [KiVirtualizationException + 0x206](KiVirtualizationException_function_006C2900.md) (inside-function, `0x006C2B06`)
- `0x006C2B1C` → [KiVirtualizationException + 0x20F](KiVirtualizationException_function_006C2900.md) (inside-function, `0x006C2B0F`)
- `0x006C2B25` → [KiVirtualizationException + 0x218](KiVirtualizationException_function_006C2900.md) (inside-function, `0x006C2B18`)
- `0x006C2B2E` → [KiVirtualizationException + 0x221](KiVirtualizationException_function_006C2900.md) (inside-function, `0x006C2B21`)
- `0x006C2B37` → [KiVirtualizationException + 0x22A](KiVirtualizationException_function_006C2900.md) (inside-function, `0x006C2B2A`)
- `0x006C2B40` → [KiVirtualizationException + 0x233](KiVirtualizationException_function_006C2900.md) (inside-function, `0x006C2B33`)
- `0x006C2B49` → [KiVirtualizationException + 0x23C](KiVirtualizationException_function_006C2900.md) (inside-function, `0x006C2B3C`)
- `0x006C2B52` → [KiVirtualizationException + 0x245](KiVirtualizationException_function_006C2900.md) (inside-function, `0x006C2B45`)
- `0x006C2B5B` → [KiVirtualizationException + 0x24E](KiVirtualizationException_function_006C2900.md) (inside-function, `0x006C2B4E`)
- `0x006C2B64` → [KiVirtualizationException + 0x257](KiVirtualizationException_function_006C2900.md) (inside-function, `0x006C2B57`)
- `0x006C2B6D` → [KiVirtualizationException + 0x260](KiVirtualizationException_function_006C2900.md) (inside-function, `0x006C2B60`)
- `0x006C2B98` → [KiFlushBhbDuringTrapEntryOrExit](KiFlushBhbDuringTrapEntryOrExit_function_006C6340.md) (function, `0x006C6340`)
- `0x006C2BE1` → [KiSaveDebugRegisterState](../4F/KiSaveDebugRegisterState_function_004FD960.md) (function, `0x004FD960`)
- `0x006C2C15` → [KiSynchronizeUserIsolationDomainExit](../41/KiSynchronizeUserIsolationDomainExit_function_0041BFA0.md) (function, `0x0041BFA0`)
- `0x006C2C70` → [KzRaiseIrql](../40/KzRaiseIrql_function_00400B10.md) (function, `0x00400B10`)
- `0x006C2C8B` → [KiEpfHandleNotification](../5C/KiEpfHandleNotification_function_005C4AF0.md) (function, `0x005C4AF0`)
- `0x006C2C95` → [KiCheckForSListAddress](../40/KiCheckForSListAddress_function_0040B810.md) (function, `0x0040B810`)
- `0x006C2C9D` → [KzLowerIrql](../3F/KzLowerIrql_function_003FCF50.md) (function, `0x003FCF50`)
- `0x006C2CD7` → [KiInitiateUserApc](../6B/KiInitiateUserApc_function_006B6540.md) (function, `0x006B6540`)
- `0x006C2CE8` → [KiSynchronizeUserIsolationDomainEntry](../26/KiSynchronizeUserIsolationDomainEntry_function_00263F60.md) (function, `0x00263F60`)
- `0x006C2D02` → [KiUpdateStibpPairing](../3E/KiUpdateStibpPairing_function_003E71C0.md) (function, `0x003E71C0`)
- `0x006C2D18` → [KiRestoreSetContextState](../6B/KiRestoreSetContextState_function_006B1CA0.md) (function, `0x006B1CA0`)
- `0x006C2D34` → [KiCopyCounters](../5C/KiCopyCounters_function_005C0710.md) (function, `0x005C0710`)
- `0x006C2D50` → [KiRestoreDebugRegisterState](../4F/KiRestoreDebugRegisterState_function_004FD8E0.md) (function, `0x004FD8E0`)
- `0x006C2DEA` → [KiVirtualizationException + 0x5FD](KiVirtualizationException_function_006C2900.md) (inside-function, `0x006C2EFD`)
- `0x006C2DF3` → [KiVirtualizationException + 0x606](KiVirtualizationException_function_006C2900.md) (inside-function, `0x006C2F06`)
- `0x006C2DFC` → [KiVirtualizationException + 0x4EF](KiVirtualizationException_function_006C2900.md) (inside-function, `0x006C2DEF`)
- `0x006C2E05` → [KiVirtualizationException + 0x4F8](KiVirtualizationException_function_006C2900.md) (inside-function, `0x006C2DF8`)
- `0x006C2E0E` → [KiVirtualizationException + 0x501](KiVirtualizationException_function_006C2900.md) (inside-function, `0x006C2E01`)
- `0x006C2E17` → [KiVirtualizationException + 0x50A](KiVirtualizationException_function_006C2900.md) (inside-function, `0x006C2E0A`)
- `0x006C2E20` → [KiVirtualizationException + 0x513](KiVirtualizationException_function_006C2900.md) (inside-function, `0x006C2E13`)
- `0x006C2E29` → [KiVirtualizationException + 0x51C](KiVirtualizationException_function_006C2900.md) (inside-function, `0x006C2E1C`)
- `0x006C2E32` → [KiVirtualizationException + 0x525](KiVirtualizationException_function_006C2900.md) (inside-function, `0x006C2E25`)
- `0x006C2E3B` → [KiVirtualizationException + 0x52E](KiVirtualizationException_function_006C2900.md) (inside-function, `0x006C2E2E`)
- `0x006C2E44` → [KiVirtualizationException + 0x537](KiVirtualizationException_function_006C2900.md) (inside-function, `0x006C2E37`)
- `0x006C2E4D` → [KiVirtualizationException + 0x540](KiVirtualizationException_function_006C2900.md) (inside-function, `0x006C2E40`)
- `0x006C2E56` → [KiVirtualizationException + 0x549](KiVirtualizationException_function_006C2900.md) (inside-function, `0x006C2E49`)
- `0x006C2E5F` → [KiVirtualizationException + 0x552](KiVirtualizationException_function_006C2900.md) (inside-function, `0x006C2E52`)
- `0x006C2E68` → [KiVirtualizationException + 0x55B](KiVirtualizationException_function_006C2900.md) (inside-function, `0x006C2E5B`)
- `0x006C2E71` → [KiVirtualizationException + 0x564](KiVirtualizationException_function_006C2900.md) (inside-function, `0x006C2E64`)
- `0x006C2E7A` → [KiVirtualizationException + 0x56D](KiVirtualizationException_function_006C2900.md) (inside-function, `0x006C2E6D`)
- `0x006C2E83` → [KiVirtualizationException + 0x576](KiVirtualizationException_function_006C2900.md) (inside-function, `0x006C2E76`)
- `0x006C2E8C` → [KiVirtualizationException + 0x57F](KiVirtualizationException_function_006C2900.md) (inside-function, `0x006C2E7F`)
- `0x006C2E95` → [KiVirtualizationException + 0x588](KiVirtualizationException_function_006C2900.md) (inside-function, `0x006C2E88`)
- `0x006C2E9E` → [KiVirtualizationException + 0x591](KiVirtualizationException_function_006C2900.md) (inside-function, `0x006C2E91`)
- `0x006C2EA7` → [KiVirtualizationException + 0x59A](KiVirtualizationException_function_006C2900.md) (inside-function, `0x006C2E9A`)
- `0x006C2EB0` → [KiVirtualizationException + 0x5A3](KiVirtualizationException_function_006C2900.md) (inside-function, `0x006C2EA3`)
- `0x006C2EB9` → [KiVirtualizationException + 0x5AC](KiVirtualizationException_function_006C2900.md) (inside-function, `0x006C2EAC`)
- `0x006C2EC2` → [KiVirtualizationException + 0x5B5](KiVirtualizationException_function_006C2900.md) (inside-function, `0x006C2EB5`)
- `0x006C2ECB` → [KiVirtualizationException + 0x5BE](KiVirtualizationException_function_006C2900.md) (inside-function, `0x006C2EBE`)
- `0x006C2ED4` → [KiVirtualizationException + 0x5C7](KiVirtualizationException_function_006C2900.md) (inside-function, `0x006C2EC7`)
- `0x006C2EDD` → [KiVirtualizationException + 0x5D0](KiVirtualizationException_function_006C2900.md) (inside-function, `0x006C2ED0`)
- `0x006C2EE6` → [KiVirtualizationException + 0x5D9](KiVirtualizationException_function_006C2900.md) (inside-function, `0x006C2ED9`)
- `0x006C2EEF` → [KiVirtualizationException + 0x5E2](KiVirtualizationException_function_006C2900.md) (inside-function, `0x006C2EE2`)
- `0x006C2EF8` → [KiVirtualizationException + 0x5EB](KiVirtualizationException_function_006C2900.md) (inside-function, `0x006C2EEB`)
- `0x006C2F01` → [KiVirtualizationException + 0x5F4](KiVirtualizationException_function_006C2900.md) (inside-function, `0x006C2EF4`)
- `0x006C300E` → [KiBugCheckDispatch](KiBugCheckDispatch_function_006C5880.md) (function, `0x006C5880`)

### Direct callers
- [KiVirtualizationException](KiVirtualizationException_function_006C2900.md) at `0x006C2A56`
- [KiVirtualizationException](KiVirtualizationException_function_006C2900.md) at `0x006C2A5F`
- [KiVirtualizationException](KiVirtualizationException_function_006C2900.md) at `0x006C2A68`
- [KiVirtualizationException](KiVirtualizationException_function_006C2900.md) at `0x006C2A71`
- [KiVirtualizationException](KiVirtualizationException_function_006C2900.md) at `0x006C2A7A`
- [KiVirtualizationException](KiVirtualizationException_function_006C2900.md) at `0x006C2A83`
- [KiVirtualizationException](KiVirtualizationException_function_006C2900.md) at `0x006C2A8C`
- [KiVirtualizationException](KiVirtualizationException_function_006C2900.md) at `0x006C2A95`
- [KiVirtualizationException](KiVirtualizationException_function_006C2900.md) at `0x006C2A9E`
- [KiVirtualizationException](KiVirtualizationException_function_006C2900.md) at `0x006C2AA7`
- [KiVirtualizationException](KiVirtualizationException_function_006C2900.md) at `0x006C2AB0`
- [KiVirtualizationException](KiVirtualizationException_function_006C2900.md) at `0x006C2AB9`
- [KiVirtualizationException](KiVirtualizationException_function_006C2900.md) at `0x006C2AC2`
- [KiVirtualizationException](KiVirtualizationException_function_006C2900.md) at `0x006C2ACB`
- [KiVirtualizationException](KiVirtualizationException_function_006C2900.md) at `0x006C2AD4`
- [KiVirtualizationException](KiVirtualizationException_function_006C2900.md) at `0x006C2ADD`
- [KiVirtualizationException](KiVirtualizationException_function_006C2900.md) at `0x006C2AE6`
- [KiVirtualizationException](KiVirtualizationException_function_006C2900.md) at `0x006C2AEF`
- [KiVirtualizationException](KiVirtualizationException_function_006C2900.md) at `0x006C2AF8`
- [KiVirtualizationException](KiVirtualizationException_function_006C2900.md) at `0x006C2B01`
- [KiVirtualizationException](KiVirtualizationException_function_006C2900.md) at `0x006C2B0A`
- [KiVirtualizationException](KiVirtualizationException_function_006C2900.md) at `0x006C2B13`
- [KiVirtualizationException](KiVirtualizationException_function_006C2900.md) at `0x006C2B1C`
- [KiVirtualizationException](KiVirtualizationException_function_006C2900.md) at `0x006C2B25`
- [KiVirtualizationException](KiVirtualizationException_function_006C2900.md) at `0x006C2B2E`
- [KiVirtualizationException](KiVirtualizationException_function_006C2900.md) at `0x006C2B37`
- [KiVirtualizationException](KiVirtualizationException_function_006C2900.md) at `0x006C2B40`
- [KiVirtualizationException](KiVirtualizationException_function_006C2900.md) at `0x006C2B49`
- [KiVirtualizationException](KiVirtualizationException_function_006C2900.md) at `0x006C2B52`
- [KiVirtualizationException](KiVirtualizationException_function_006C2900.md) at `0x006C2B5B`
- [KiVirtualizationException](KiVirtualizationException_function_006C2900.md) at `0x006C2B64`
- [KiVirtualizationException](KiVirtualizationException_function_006C2900.md) at `0x006C2B6D`
- [KiVirtualizationException](KiVirtualizationException_function_006C2900.md) at `0x006C2DEA`
- [KiVirtualizationException](KiVirtualizationException_function_006C2900.md) at `0x006C2DF3`
- [KiVirtualizationException](KiVirtualizationException_function_006C2900.md) at `0x006C2DFC`
- [KiVirtualizationException](KiVirtualizationException_function_006C2900.md) at `0x006C2E05`
- [KiVirtualizationException](KiVirtualizationException_function_006C2900.md) at `0x006C2E0E`
- [KiVirtualizationException](KiVirtualizationException_function_006C2900.md) at `0x006C2E17`
- [KiVirtualizationException](KiVirtualizationException_function_006C2900.md) at `0x006C2E20`
- [KiVirtualizationException](KiVirtualizationException_function_006C2900.md) at `0x006C2E29`
- [KiVirtualizationException](KiVirtualizationException_function_006C2900.md) at `0x006C2E32`
- [KiVirtualizationException](KiVirtualizationException_function_006C2900.md) at `0x006C2E3B`
- [KiVirtualizationException](KiVirtualizationException_function_006C2900.md) at `0x006C2E44`
- [KiVirtualizationException](KiVirtualizationException_function_006C2900.md) at `0x006C2E4D`
- [KiVirtualizationException](KiVirtualizationException_function_006C2900.md) at `0x006C2E56`
- [KiVirtualizationException](KiVirtualizationException_function_006C2900.md) at `0x006C2E5F`
- [KiVirtualizationException](KiVirtualizationException_function_006C2900.md) at `0x006C2E68`
- [KiVirtualizationException](KiVirtualizationException_function_006C2900.md) at `0x006C2E71`
- [KiVirtualizationException](KiVirtualizationException_function_006C2900.md) at `0x006C2E7A`
- [KiVirtualizationException](KiVirtualizationException_function_006C2900.md) at `0x006C2E83`
- [KiVirtualizationException](KiVirtualizationException_function_006C2900.md) at `0x006C2E8C`
- [KiVirtualizationException](KiVirtualizationException_function_006C2900.md) at `0x006C2E95`
- [KiVirtualizationException](KiVirtualizationException_function_006C2900.md) at `0x006C2E9E`
- [KiVirtualizationException](KiVirtualizationException_function_006C2900.md) at `0x006C2EA7`
- [KiVirtualizationException](KiVirtualizationException_function_006C2900.md) at `0x006C2EB0`
- [KiVirtualizationException](KiVirtualizationException_function_006C2900.md) at `0x006C2EB9`
- [KiVirtualizationException](KiVirtualizationException_function_006C2900.md) at `0x006C2EC2`
- [KiVirtualizationException](KiVirtualizationException_function_006C2900.md) at `0x006C2ECB`
- [KiVirtualizationException](KiVirtualizationException_function_006C2900.md) at `0x006C2ED4`
- [KiVirtualizationException](KiVirtualizationException_function_006C2900.md) at `0x006C2EDD`
- [KiVirtualizationException](KiVirtualizationException_function_006C2900.md) at `0x006C2EE6`
- [KiVirtualizationException](KiVirtualizationException_function_006C2900.md) at `0x006C2EEF`
- [KiVirtualizationException](KiVirtualizationException_function_006C2900.md) at `0x006C2EF8`
- [KiVirtualizationException](KiVirtualizationException_function_006C2900.md) at `0x006C2F01`

### Static image references
- `0x006C2975` → RVA `0x01201840` (`CFGRO`; read)
- `0x006C2BA9` → RVA `0x00FC7264` (`ALMOSTRO`; read)
- `0x006C2C1A` → RVA `0x00FC6BF0` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006C2F88` → [KiKernelExit](../../kvascode/BC/KiKernelExit_function_00BCCB80.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006C2900  48 83 EC 08                     sub rsp, 8
006C2904  55                              push rbp
006C2905  48 81 EC 58 01 00 00            sub rsp, 0x158
006C290C  48 8D AC 24 80 00 00 00         lea rbp, [rsp + 0x80]
006C2914  C6 45 AB 01                     mov byte ptr [rbp - 0x55], 1
006C2918  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
006C291C  48 89 4D B8                     mov qword ptr [rbp - 0x48], rcx
006C2920  48 89 55 C0                     mov qword ptr [rbp - 0x40], rdx
006C2924  4C 89 45 C8                     mov qword ptr [rbp - 0x38], r8
006C2928  4C 89 4D D0                     mov qword ptr [rbp - 0x30], r9
006C292C  4C 89 55 D8                     mov qword ptr [rbp - 0x28], r10
006C2930  4C 89 5D E0                     mov qword ptr [rbp - 0x20], r11
006C2934  F6 85 F0 00 00 00 01            test byte ptr [rbp + 0xf0], 1
006C293B  75 38                           jne 0x1406c2975
006C293D  33 D2                           xor edx, edx
006C293F  F3 48 0F 1E CA                  rdsspq rdx
006C2944  48 89 55 58                     mov qword ptr [rbp + 0x58], rdx
006C2948  0F AE E8                        lfence
006C294B  65 F6 04 25 58 08 00 00 01      test byte ptr gs:[0x858], 1
006C2954  75 08                           jne 0x1406c295e
006C2956  0F AE E8                        lfence
006C2959  E9 88 02 00 00                  jmp 0x1406c2be6
006C295E  65 0F B7 04 25 66 08 00 00      movzx eax, word ptr gs:[0x866]
006C2967  B9 48 00 00 00                  mov ecx, 0x48
006C296C  33 D2                           xor edx, edx
006C296E  0F 30                           wrmsr
006C2970  E9 71 02 00 00                  jmp 0x1406c2be6
006C2975  F6 05 C4 EE B3 00 01            test byte ptr [rip + 0xb3eec4], 1
006C297C  75 03                           jne 0x1406c2981
006C297E  0F 01 F8                        swapgs
006C2981  0F AE E8                        lfence
006C2984  65 48 8B 0C 25 28 9D 00 00      mov rcx, qword ptr gs:[0x9d28]
006C298D  48 85 C9                        test rcx, rcx
006C2990  74 1F                           je 0x1406c29b1
006C2992  F3 48 0F 1E CA                  rdsspq rdx
006C2997  65 4C 8B 14 25 20 9D 00 00      mov r10, qword ptr gs:[0x9d20]
006C29A0  49 83 C2 08                     add r10, 8
006C29A4  49 3B D2                        cmp rdx, r10
006C29A7  75 08                           jne 0x1406c29b1
006C29A9  F3 0F 01 29                     rstorssp dword ptr [rcx]
006C29AD  F3 0F 01 EA                     saveprevssp
006C29B1  65 4C 8B 14 25 88 01 00 00      mov r10, qword ptr gs:[0x188]
006C29BA  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006C29C3  48 8B 89 20 02 00 00            mov rcx, qword ptr [rcx + 0x220]
006C29CA  48 8B 89 60 07 00 00            mov rcx, qword ptr [rcx + 0x760]
006C29D1  65 48 89 0C 25 50 08 00 00      mov qword ptr gs:[0x850], rcx
006C29DA  66 65 8B 0C 25 62 08 00 00      mov cx, word ptr gs:[0x862]
006C29E3  66 65 89 0C 25 64 08 00 00      mov word ptr gs:[0x864], cx
006C29EC  65 8A 0C 25 58 08 00 00         mov cl, byte ptr gs:[0x858]
006C29F4  65 88 0C 25 5A 08 00 00         mov byte ptr gs:[0x85a], cl
006C29FC  65 0F B7 04 25 68 08 00 00      movzx eax, word ptr gs:[0x868]
006C2A05  66 65 39 04 25 66 08 00 00      cmp word ptr gs:[0x866], ax
006C2A0E  74 12                           je 0x1406c2a22
006C2A10  66 65 89 04 25 66 08 00 00      mov word ptr gs:[0x866], ax
006C2A19  B9 48 00 00 00                  mov ecx, 0x48
006C2A1E  33 D2                           xor edx, edx
006C2A20  0F 30                           wrmsr
006C2A22  65 0F B6 14 25 58 08 00 00      movzx edx, byte ptr gs:[0x858]
006C2A2B  F7 C2 08 00 00 00               test edx, 8
006C2A31  74 17                           je 0x1406c2a4a
006C2A33  B8 01 00 00 00                  mov eax, 1
006C2A38  33 D2                           xor edx, edx
006C2A3A  B9 49 00 00 00                  mov ecx, 0x49
006C2A3F  0F 30                           wrmsr
006C2A41  65 0F B6 14 25 58 08 00 00      movzx edx, byte ptr gs:[0x858]
006C2A4A  F7 C2 02 00 00 00               test edx, 2
006C2A50  0F 84 37 01 00 00               je 0x1406c2b8d
006C2A56  E8 0E 01 00 00                  call 0x1406c2b69
006C2A5B  48 83 C4 08                     add rsp, 8
006C2A5F  E8 0E 01 00 00                  call 0x1406c2b72
006C2A64  48 83 C4 08                     add rsp, 8
006C2A68  E8 EE FF FF FF                  call 0x1406c2a5b
006C2A6D  48 83 C4 08                     add rsp, 8
006C2A71  E8 EE FF FF FF                  call 0x1406c2a64
006C2A76  48 83 C4 08                     add rsp, 8
006C2A7A  E8 EE FF FF FF                  call 0x1406c2a6d
006C2A7F  48 83 C4 08                     add rsp, 8
006C2A83  E8 EE FF FF FF                  call 0x1406c2a76
006C2A88  48 83 C4 08                     add rsp, 8
006C2A8C  E8 EE FF FF FF                  call 0x1406c2a7f
006C2A91  48 83 C4 08                     add rsp, 8
006C2A95  E8 EE FF FF FF                  call 0x1406c2a88
006C2A9A  48 83 C4 08                     add rsp, 8
006C2A9E  E8 EE FF FF FF                  call 0x1406c2a91
006C2AA3  48 83 C4 08                     add rsp, 8
006C2AA7  E8 EE FF FF FF                  call 0x1406c2a9a
006C2AAC  48 83 C4 08                     add rsp, 8
006C2AB0  E8 EE FF FF FF                  call 0x1406c2aa3
006C2AB5  48 83 C4 08                     add rsp, 8
006C2AB9  E8 EE FF FF FF                  call 0x1406c2aac
006C2ABE  48 83 C4 08                     add rsp, 8
006C2AC2  E8 EE FF FF FF                  call 0x1406c2ab5
006C2AC7  48 83 C4 08                     add rsp, 8
006C2ACB  E8 EE FF FF FF                  call 0x1406c2abe
006C2AD0  48 83 C4 08                     add rsp, 8
006C2AD4  E8 EE FF FF FF                  call 0x1406c2ac7
006C2AD9  48 83 C4 08                     add rsp, 8
006C2ADD  E8 EE FF FF FF                  call 0x1406c2ad0
006C2AE2  48 83 C4 08                     add rsp, 8
006C2AE6  E8 EE FF FF FF                  call 0x1406c2ad9
006C2AEB  48 83 C4 08                     add rsp, 8
006C2AEF  E8 EE FF FF FF                  call 0x1406c2ae2
006C2AF4  48 83 C4 08                     add rsp, 8
006C2AF8  E8 EE FF FF FF                  call 0x1406c2aeb
006C2AFD  48 83 C4 08                     add rsp, 8
006C2B01  E8 EE FF FF FF                  call 0x1406c2af4
006C2B06  48 83 C4 08                     add rsp, 8
006C2B0A  E8 EE FF FF FF                  call 0x1406c2afd
006C2B0F  48 83 C4 08                     add rsp, 8
006C2B13  E8 EE FF FF FF                  call 0x1406c2b06
006C2B18  48 83 C4 08                     add rsp, 8
006C2B1C  E8 EE FF FF FF                  call 0x1406c2b0f
006C2B21  48 83 C4 08                     add rsp, 8
006C2B25  E8 EE FF FF FF                  call 0x1406c2b18
006C2B2A  48 83 C4 08                     add rsp, 8
006C2B2E  E8 EE FF FF FF                  call 0x1406c2b21
006C2B33  48 83 C4 08                     add rsp, 8
006C2B37  E8 EE FF FF FF                  call 0x1406c2b2a
006C2B3C  48 83 C4 08                     add rsp, 8
006C2B40  E8 EE FF FF FF                  call 0x1406c2b33
006C2B45  48 83 C4 08                     add rsp, 8
006C2B49  E8 EE FF FF FF                  call 0x1406c2b3c
006C2B4E  48 83 C4 08                     add rsp, 8
006C2B52  E8 EE FF FF FF                  call 0x1406c2b45
006C2B57  48 83 C4 08                     add rsp, 8
006C2B5B  E8 EE FF FF FF                  call 0x1406c2b4e
006C2B60  48 83 C4 08                     add rsp, 8
006C2B64  E8 EE FF FF FF                  call 0x1406c2b57
006C2B69  48 83 C4 08                     add rsp, 8
006C2B6D  E8 EE FF FF FF                  call 0x1406c2b60
006C2B72  48 83 C4 08                     add rsp, 8
006C2B76  B8 DA DA 00 00                  mov eax, 0xdada
006C2B7B  65 F6 04 25 5C 08 00 00 08      test byte ptr gs:[0x85c], 8
006C2B84  74 07                           je 0x1406c2b8d
006C2B86  B0 20                           mov al, 0x20
006C2B88  F3 48 0F AE E8                  incsspq rax
006C2B8D  F7 C2 80 00 00 00               test edx, 0x80
006C2B93  74 08                           je 0x1406c2b9d
006C2B95  0F AE E8                        lfence
006C2B98  E8 A3 37 00 00                  call 0x1406c6340
006C2B9D  0F AE E8                        lfence
006C2BA0  65 C6 04 25 5E 08 00 00 00      mov byte ptr gs:[0x85e], 0
006C2BA9  83 3D B4 46 90 00 00            cmp dword ptr [rip + 0x9046b4], 0
006C2BB0  74 1F                           je 0x1406c2bd1
006C2BB2  B9 A7 06 00 00                  mov ecx, 0x6a7
006C2BB7  0F 32                           rdmsr
006C2BB9  83 FA 00                        cmp edx, 0
006C2BBC  74 13                           je 0x1406c2bd1
006C2BBE  8B CA                           mov ecx, edx
006C2BC0  23 15 9E 46 90 00               and edx, dword ptr [rip + 0x90469e]
006C2BC6  3B D1                           cmp edx, ecx
006C2BC8  74 07                           je 0x1406c2bd1
006C2BCA  B9 A7 06 00 00                  mov ecx, 0x6a7
006C2BCF  0F 30                           wrmsr
006C2BD1  41 F6 42 03 03                  test byte ptr [r10 + 3], 3
006C2BD6  66 C7 85 80 00 00 00 00 00      mov word ptr [rbp + 0x80], 0
006C2BDF  74 05                           je 0x1406c2be6
006C2BE1  E8 7A AD E3 FF                  call 0x1404fd960
006C2BE6  FC                              cld
006C2BE7  0F AE 5D AC                     stmxcsr dword ptr [rbp - 0x54]
006C2BEB  65 0F AE 14 25 80 01 00 00      ldmxcsr dword ptr gs:[0x180]
006C2BF4  0F 29 45 F0                     movaps xmmword ptr [rbp - 0x10], xmm0
006C2BF8  0F 29 4D 00                     movaps xmmword ptr [rbp], xmm1
006C2BFC  0F 29 55 10                     movaps xmmword ptr [rbp + 0x10], xmm2
006C2C00  0F 29 5D 20                     movaps xmmword ptr [rbp + 0x20], xmm3
006C2C04  0F 29 65 30                     movaps xmmword ptr [rbp + 0x30], xmm4
006C2C08  0F 29 6D 40                     movaps xmmword ptr [rbp + 0x40], xmm5
006C2C0C  F6 85 F0 00 00 00 01            test byte ptr [rbp + 0xf0], 1
006C2C13  74 05                           je 0x1406c2c1a
006C2C15  E8 86 93 D5 FF                  call 0x14041bfa0
006C2C1A  F6 05 CF 3F 90 00 FF            test byte ptr [rip + 0x903fcf], 0xff
006C2C21  74 0C                           je 0x1406c2c2f
006C2C23  F6 85 F0 00 00 00 01            test byte ptr [rbp + 0xf0], 1
006C2C2A  74 03                           je 0x1406c2c2f
006C2C2C  0F 01 CB                        stac
006C2C2F  65 4C 8B 0C 25 88 8D 00 00      mov r9, qword ptr gs:[0x8d88]
006C2C38  4D 85 C9                        test r9, r9
006C2C3B  0F 84 AE 03 00 00               je 0x1406c2fef
006C2C41  41 83 79 44 01                  cmp dword ptr [r9 + 0x44], 1
006C2C46  0F 85 A3 03 00 00               jne 0x1406c2fef
006C2C4C  F7 85 F8 00 00 00 00 02 00 00   test dword ptr [rbp + 0xf8], 0x200
006C2C56  0F 84 93 03 00 00               je 0x1406c2fef
006C2C5C  44 0F 20 C0                     mov rax, cr8
006C2C60  89 45 A0                        mov dword ptr [rbp - 0x60], eax
006C2C63  3C 02                           cmp al, 2
006C2C65  0F 8D 84 03 00 00               jge 0x1406c2fef
006C2C6B  B9 02 00 00 00                  mov ecx, 2
006C2C70  E8 9B DE D3 FF                  call 0x140400b10
006C2C75  FB                              sti
006C2C76  65 4C 8B 0C 25 88 8D 00 00      mov r9, qword ptr gs:[0x8d88]
006C2C7F  49 8B 49 48                     mov rcx, qword ptr [r9 + 0x48]
006C2C83  41 C7 41 44 00 00 00 00         mov dword ptr [r9 + 0x44], 0
006C2C8B  E8 60 1E F0 FF                  call 0x1405c4af0
006C2C90  FA                              cli
006C2C91  48 8D 4D 80                     lea rcx, [rbp - 0x80]
006C2C95  E8 76 8B D4 FF                  call 0x14040b810
006C2C9A  8B 4D A0                        mov ecx, dword ptr [rbp - 0x60]
006C2C9D  E8 AE A2 D3 FF                  call 0x1403fcf50
006C2CA2  F6 85 F0 00 00 00 01            test byte ptr [rbp + 0xf0], 1
006C2CA9  0F 84 F5 02 00 00               je 0x1406c2fa4
006C2CAF  F6 05 3A 3F 90 00 FF            test byte ptr [rip + 0x903f3a], 0xff
006C2CB6  74 03                           je 0x1406c2cbb
006C2CB8  0F 01 CB                        stac
006C2CBB  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006C2CC4  F6 81 C2 00 00 00 03            test byte ptr [rcx + 0xc2], 3
006C2CCB  74 1B                           je 0x1406c2ce8
006C2CCD  B9 01 00 00 00                  mov ecx, 1
006C2CD2  44 0F 22 C1                     mov cr8, rcx
006C2CD6  FB                              sti
006C2CD7  E8 64 38 FF FF                  call 0x1406b6540
006C2CDC  FA                              cli
006C2CDD  B9 00 00 00 00                  mov ecx, 0
006C2CE2  44 0F 22 C1                     mov cr8, rcx
006C2CE6  EB D3                           jmp 0x1406c2cbb
006C2CE8  E8 73 12 BA FF                  call 0x140263f60
006C2CED  85 C0                           test eax, eax
006C2CEF  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
006C2CF3  75 C6                           jne 0x1406c2cbb
006C2CF5  65 F6 04 25 60 08 00 00 02      test byte ptr gs:[0x860], 2
006C2CFE  74 07                           je 0x1406c2d07
006C2D00  33 C9                           xor ecx, ecx
006C2D02  E8 B9 44 D2 FF                  call 0x1403e71c0
006C2D07  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006C2D10  F7 01 00 00 00 08               test dword ptr [rcx], 0x8000000
006C2D16  74 05                           je 0x1406c2d1d
006C2D18  E8 83 EF FE FF                  call 0x1406b1ca0
006C2D1D  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006C2D26  F7 01 00 00 01 00               test dword ptr [rcx], 0x10000
006C2D2C  74 14                           je 0x1406c2d42
006C2D2E  F6 41 02 01                     test byte ptr [rcx + 2], 1
006C2D32  74 0E                           je 0x1406c2d42
006C2D34  E8 D7 D9 EF FF                  call 0x1405c0710
006C2D39  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006C2D42  0F AE 55 AC                     ldmxcsr dword ptr [rbp - 0x54]
006C2D46  66 83 BD 80 00 00 00 00         cmp word ptr [rbp + 0x80], 0
006C2D4E  74 05                           je 0x1406c2d55
006C2D50  E8 8B AB E3 FF                  call 0x1404fd8e0
006C2D55  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006C2D5E  0F BA 61 74 16                  bt dword ptr [rcx + 0x74], 0x16
006C2D63  73 2A                           jae 0x1406c2d8f
006C2D65  33 C9                           xor ecx, ecx
006C2D67  F3 48 0F 1E C9                  rdsspq rcx
006C2D6C  65 4C 8B 04 25 28 9D 00 00      mov r8, qword ptr gs:[0x9d28]
006C2D75  49 83 C0 08                     add r8, 8
006C2D79  49 3B C8                        cmp rcx, r8
006C2D7C  75 11                           jne 0x1406c2d8f
006C2D7E  65 48 8B 0C 25 20 9D 00 00      mov rcx, qword ptr gs:[0x9d20]
006C2D87  F3 0F 01 29                     rstorssp dword ptr [rcx]
006C2D8B  F3 0F 01 EA                     saveprevssp
006C2D8F  65 C6 04 25 5E 08 00 00 00      mov byte ptr gs:[0x85e], 0
006C2D98  65 0F B7 04 25 6C 08 00 00      movzx eax, word ptr gs:[0x86c]
006C2DA1  66 65 39 04 25 66 08 00 00      cmp word ptr gs:[0x866], ax
006C2DAA  74 12                           je 0x1406c2dbe
006C2DAC  66 65 89 04 25 66 08 00 00      mov word ptr gs:[0x866], ax
006C2DB5  B9 48 00 00 00                  mov ecx, 0x48
006C2DBA  33 D2                           xor edx, edx
006C2DBC  0F 30                           wrmsr
006C2DBE  66 65 0F BA 34 25 58 08 00 00 02  btr word ptr gs:[0x858], 2
006C2DC9  73 0E                           jae 0x1406c2dd9
006C2DCB  B8 01 00 00 00                  mov eax, 1
006C2DD0  33 D2                           xor edx, edx
006C2DD2  B9 49 00 00 00                  mov ecx, 0x49
006C2DD7  0F 30                           wrmsr
006C2DD9  66 65 0F BA 34 25 58 08 00 00 05  btr word ptr gs:[0x858], 5
006C2DE4  0F 83 37 01 00 00               jae 0x1406c2f21
006C2DEA  E8 0E 01 00 00                  call 0x1406c2efd
006C2DEF  48 83 C4 08                     add rsp, 8
006C2DF3  E8 0E 01 00 00                  call 0x1406c2f06
006C2DF8  48 83 C4 08                     add rsp, 8
006C2DFC  E8 EE FF FF FF                  call 0x1406c2def
006C2E01  48 83 C4 08                     add rsp, 8
006C2E05  E8 EE FF FF FF                  call 0x1406c2df8
006C2E0A  48 83 C4 08                     add rsp, 8
006C2E0E  E8 EE FF FF FF                  call 0x1406c2e01
006C2E13  48 83 C4 08                     add rsp, 8
006C2E17  E8 EE FF FF FF                  call 0x1406c2e0a
006C2E1C  48 83 C4 08                     add rsp, 8
006C2E20  E8 EE FF FF FF                  call 0x1406c2e13
006C2E25  48 83 C4 08                     add rsp, 8
006C2E29  E8 EE FF FF FF                  call 0x1406c2e1c
006C2E2E  48 83 C4 08                     add rsp, 8
006C2E32  E8 EE FF FF FF                  call 0x1406c2e25
006C2E37  48 83 C4 08                     add rsp, 8
006C2E3B  E8 EE FF FF FF                  call 0x1406c2e2e
006C2E40  48 83 C4 08                     add rsp, 8
006C2E44  E8 EE FF FF FF                  call 0x1406c2e37
006C2E49  48 83 C4 08                     add rsp, 8
006C2E4D  E8 EE FF FF FF                  call 0x1406c2e40
006C2E52  48 83 C4 08                     add rsp, 8
006C2E56  E8 EE FF FF FF                  call 0x1406c2e49
006C2E5B  48 83 C4 08                     add rsp, 8
006C2E5F  E8 EE FF FF FF                  call 0x1406c2e52
006C2E64  48 83 C4 08                     add rsp, 8
006C2E68  E8 EE FF FF FF                  call 0x1406c2e5b
006C2E6D  48 83 C4 08                     add rsp, 8
006C2E71  E8 EE FF FF FF                  call 0x1406c2e64
006C2E76  48 83 C4 08                     add rsp, 8
006C2E7A  E8 EE FF FF FF                  call 0x1406c2e6d
006C2E7F  48 83 C4 08                     add rsp, 8
006C2E83  E8 EE FF FF FF                  call 0x1406c2e76
006C2E88  48 83 C4 08                     add rsp, 8
006C2E8C  E8 EE FF FF FF                  call 0x1406c2e7f
006C2E91  48 83 C4 08                     add rsp, 8
006C2E95  E8 EE FF FF FF                  call 0x1406c2e88
006C2E9A  48 83 C4 08                     add rsp, 8
006C2E9E  E8 EE FF FF FF                  call 0x1406c2e91
006C2EA3  48 83 C4 08                     add rsp, 8
006C2EA7  E8 EE FF FF FF                  call 0x1406c2e9a
006C2EAC  48 83 C4 08                     add rsp, 8
006C2EB0  E8 EE FF FF FF                  call 0x1406c2ea3
006C2EB5  48 83 C4 08                     add rsp, 8
006C2EB9  E8 EE FF FF FF                  call 0x1406c2eac
006C2EBE  48 83 C4 08                     add rsp, 8
006C2EC2  E8 EE FF FF FF                  call 0x1406c2eb5
006C2EC7  48 83 C4 08                     add rsp, 8
006C2ECB  E8 EE FF FF FF                  call 0x1406c2ebe
006C2ED0  48 83 C4 08                     add rsp, 8
006C2ED4  E8 EE FF FF FF                  call 0x1406c2ec7
006C2ED9  48 83 C4 08                     add rsp, 8
006C2EDD  E8 EE FF FF FF                  call 0x1406c2ed0
006C2EE2  48 83 C4 08                     add rsp, 8
006C2EE6  E8 EE FF FF FF                  call 0x1406c2ed9
006C2EEB  48 83 C4 08                     add rsp, 8
006C2EEF  E8 EE FF FF FF                  call 0x1406c2ee2
006C2EF4  48 83 C4 08                     add rsp, 8
006C2EF8  E8 EE FF FF FF                  call 0x1406c2eeb
006C2EFD  48 83 C4 08                     add rsp, 8
006C2F01  E8 EE FF FF FF                  call 0x1406c2ef4
006C2F06  48 83 C4 08                     add rsp, 8
006C2F0A  B8 DA DA 00 00                  mov eax, 0xdada
006C2F0F  65 F6 04 25 5C 08 00 00 08      test byte ptr gs:[0x85c], 8
006C2F18  74 07                           je 0x1406c2f21
006C2F1A  B0 20                           mov al, 0x20
006C2F1C  F3 48 0F AE E8                  incsspq rax
006C2F21  66 65 F7 04 25 58 08 00 00 00 01  test word ptr gs:[0x858], 0x100
006C2F2C  74 0C                           je 0x1406c2f3a
006C2F2E  33 C0                           xor eax, eax
006C2F30  33 D2                           xor edx, edx
006C2F32  B9 01 00 00 00                  mov ecx, 1
006C2F37  48 F7 F1                        div rcx
006C2F3A  0F 28 45 F0                     movaps xmm0, xmmword ptr [rbp - 0x10]
006C2F3E  0F 28 4D 00                     movaps xmm1, xmmword ptr [rbp]
006C2F42  0F 28 55 10                     movaps xmm2, xmmword ptr [rbp + 0x10]
006C2F46  0F 28 5D 20                     movaps xmm3, xmmword ptr [rbp + 0x20]
006C2F4A  0F 28 65 30                     movaps xmm4, xmmword ptr [rbp + 0x30]
006C2F4E  0F 28 6D 40                     movaps xmm5, xmmword ptr [rbp + 0x40]
006C2F52  4C 8B 5D E0                     mov r11, qword ptr [rbp - 0x20]
006C2F56  4C 8B 55 D8                     mov r10, qword ptr [rbp - 0x28]
006C2F5A  4C 8B 4D D0                     mov r9, qword ptr [rbp - 0x30]
006C2F5E  4C 8B 45 C8                     mov r8, qword ptr [rbp - 0x38]
006C2F62  48 8B 55 C0                     mov rdx, qword ptr [rbp - 0x40]
006C2F66  48 8B 4D B8                     mov rcx, qword ptr [rbp - 0x48]
006C2F6A  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
006C2F6E  48 8B E5                        mov rsp, rbp
006C2F71  48 8B AD D8 00 00 00            mov rbp, qword ptr [rbp + 0xd8]
006C2F78  48 81 C4 E8 00 00 00            add rsp, 0xe8
006C2F7F  F6 05 BA E8 B3 00 01            test byte ptr [rip + 0xb3e8ba], 1
006C2F86  74 05                           je 0x1406c2f8d
006C2F88  E9 F3 9B 50 00                  jmp 0x140bccb80
006C2F8D  66 65 F7 04 25 58 08 00 00 00 02  test word ptr gs:[0x858], 0x200
006C2F98  74 05                           je 0x1406c2f9f
006C2F9A  0F 00 6C 24 20                  verw word ptr [rsp + 0x20]
006C2F9F  0F 01 F8                        swapgs
006C2FA2  48 CF                           iretq
006C2FA4  0F AE 55 AC                     ldmxcsr dword ptr [rbp - 0x54]
006C2FA8  0F 28 45 F0                     movaps xmm0, xmmword ptr [rbp - 0x10]
006C2FAC  0F 28 4D 00                     movaps xmm1, xmmword ptr [rbp]
006C2FB0  0F 28 55 10                     movaps xmm2, xmmword ptr [rbp + 0x10]
006C2FB4  0F 28 5D 20                     movaps xmm3, xmmword ptr [rbp + 0x20]
006C2FB8  0F 28 65 30                     movaps xmm4, xmmword ptr [rbp + 0x30]
006C2FBC  0F 28 6D 40                     movaps xmm5, xmmword ptr [rbp + 0x40]
006C2FC0  4C 8B 5D E0                     mov r11, qword ptr [rbp - 0x20]
006C2FC4  4C 8B 55 D8                     mov r10, qword ptr [rbp - 0x28]
006C2FC8  4C 8B 4D D0                     mov r9, qword ptr [rbp - 0x30]
006C2FCC  4C 8B 45 C8                     mov r8, qword ptr [rbp - 0x38]
006C2FD0  48 8B 55 C0                     mov rdx, qword ptr [rbp - 0x40]
006C2FD4  48 8B 4D B8                     mov rcx, qword ptr [rbp - 0x48]
006C2FD8  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
006C2FDC  48 8B E5                        mov rsp, rbp
006C2FDF  48 8B AD D8 00 00 00            mov rbp, qword ptr [rbp + 0xd8]
006C2FE6  48 81 C4 E8 00 00 00            add rsp, 0xe8
006C2FED  48 CF                           iretq
006C2FEF  4C 8B 95 E8 00 00 00            mov r10, qword ptr [rbp + 0xe8]
006C2FF6  65 4C 8B 0C 25 88 8D 00 00      mov r9, qword ptr gs:[0x8d88]
006C2FFF  4C 0F B6 45 A0                  movzx r8, byte ptr [rbp - 0x60]
006C3004  B9 7F 00 00 00                  mov ecx, 0x7f
006C3009  BA 20 00 00 00                  mov edx, 0x20
006C300E  E8 6D 28 00 00                  call 0x1406c5880
006C3013  90                              nop
006C3014  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiVirtualizationException(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
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
    unsigned int v_stack_m148;
    unsigned __int64 v_stack_m168;
    unsigned __int16 v_stack_m68;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p0;
    unsigned int v_stack_p10;
    unsigned __int16 v_stack_p20;
    unsigned __int8 v_stack_p8;

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
    if (((v_stack_p8) & (1)) != 0) goto loc_006C2975;
    a2 = 0;
    v_stack_m90 = 0;
    if (((*(unsigned __int8 *)(gs_base + (0 + 2136))) & (1)) != 0) goto loc_006C295E;
    goto loc_006C2BE6;
loc_006C295E:
    a2 = 0;
    goto loc_006C2BE6;
loc_006C2975:
    if (((*(unsigned __int8 *)(v_rip + 11792068)) & (1)) == 0) {
    }
    if (*(unsigned __int64 *)(gs_base + (0 + 40232)) == 0) goto loc_006C29B1;
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
    if ((((unsigned int)(a2)) & (2)) == 0) goto loc_006C2B8D;
    result = KiVirtualizationException___0x269(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiVirtualizationException___0x272(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiVirtualizationException___0x15B(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiVirtualizationException___0x164(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiVirtualizationException___0x16D(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiVirtualizationException___0x176(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiVirtualizationException___0x17F(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiVirtualizationException___0x188(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiVirtualizationException___0x191(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiVirtualizationException___0x19A(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiVirtualizationException___0x1A3(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiVirtualizationException___0x1AC(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiVirtualizationException___0x1B5(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiVirtualizationException___0x1BE(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiVirtualizationException___0x1C7(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiVirtualizationException___0x1D0(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiVirtualizationException___0x1D9(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiVirtualizationException___0x1E2(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiVirtualizationException___0x1EB(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiVirtualizationException___0x1F4(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiVirtualizationException___0x1FD(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiVirtualizationException___0x206(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiVirtualizationException___0x20F(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiVirtualizationException___0x218(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiVirtualizationException___0x221(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiVirtualizationException___0x22A(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiVirtualizationException___0x233(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiVirtualizationException___0x23C(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiVirtualizationException___0x245(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiVirtualizationException___0x24E(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiVirtualizationException___0x257(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiVirtualizationException___0x260(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = (unsigned int)(0xDADAULL);
    if (((*(unsigned __int8 *)(gs_base + (0 + 2140))) & (8)) != 0) {
        result = 32;
    }
    if ((((unsigned int)(a2)) & (128)) != 0) {
        result = KiFlushBhbDuringTrapEntryOrExit(a1, a2, a3, a4);
    }
    *(unsigned __int8 *)(gs_base + (0 + 2142)) = 0;
    if ((*(unsigned int *)(v_rip + 9455284)) == 0) goto loc_006C2BD1;
    if (((unsigned int)(a2)) == 0) goto loc_006C2BD1;
    a2 = (unsigned int)((a2) & (*(unsigned int *)(v_rip + 9455262)));
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
    if (((*(unsigned __int8 *)(v_rip + 9453519)) & (255)) == 0) goto loc_006C2C2F;
    if (((v_stack_p8) & (1)) != 0) {
    }
    if (*(unsigned __int64 *)(gs_base + (0 + 36232)) == 0) goto loc_006C2FEF;
    if ((*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 36232)) + 68)) != 1) goto loc_006C2FEF;
    if (((v_stack_p10) & (512)) == 0) goto loc_006C2FEF;
    v_stack_m148 = (unsigned int)(v_cr8);
    if (((unsigned __int8)(v_cr8)) >= 2) goto loc_006C2FEF;
    result = KzRaiseIrql(2, a2, a3, *(unsigned __int64 *)(gs_base + (0 + 36232)));
    *(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 36232)) + 68) = 0;
    result = KiEpfHandleNotification(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 36232)) + 72), a2, a3, *(unsigned __int64 *)(gs_base + (0 + 36232)));
    result = KiCheckForSListAddress(v_stack_m168, a2, a3, *(unsigned __int64 *)(gs_base + (0 + 36232)));
    result = KzLowerIrql((unsigned int)(v_stack_m148), a2, a3, *(unsigned __int64 *)(gs_base + (0 + 36232)));
    if (((v_stack_p8) & (1)) == 0) goto loc_006C2FA4;
    if (((*(unsigned __int8 *)(v_rip + 9453370)) & (255)) != 0) {
    }
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 194)) & (3)) == 0) goto loc_006C2CE8;
    result = KiInitiateUserApc(1, a2, a3, *(unsigned __int64 *)(gs_base + (0 + 36232)));
    goto loc_006C2CBB;
loc_006C2CE8:
    result = KiSynchronizeUserIsolationDomainEntry(0, a2, a3, *(unsigned __int64 *)(gs_base + (0 + 36232)));
    if ((unsigned int)(result) != 0) goto loc_006C2CBB;
    result = v_stack_m138;
    if (((*(unsigned __int8 *)(gs_base + (0 + 2144))) & (2)) != 0) {
        a1 = 0;
        result = KiUpdateStibpPairing(a1, a2, a3, *(unsigned __int64 *)(gs_base + (0 + 36232)));
    }
    if (((*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)))) & (0x8000000ULL)) != 0) {
        result = KiRestoreSetContextState(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, *(unsigned __int64 *)(gs_base + (0 + 36232)));
    }
    if (((*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)))) & (0x10000ULL)) == 0) goto loc_006C2D42;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 2)) & (1)) != 0) {
        result = KiCopyCounters(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, *(unsigned __int64 *)(gs_base + (0 + 36232)));
        a1 = *(unsigned __int64 *)(gs_base + (0 + 392));
    }
    if (v_stack_m68 != 0) {
        result = KiRestoreDebugRegisterState(a1, a2, a3, *(unsigned __int64 *)(gs_base + (0 + 36232)));
    }
    if (v_stack_m68 >= 0) goto loc_006C2D8F;
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
    if (condition_is_above_or_equal) goto loc_006C2F21;
    result = KiVirtualizationException___0x5FD(a1, a2, a3, *(unsigned __int64 *)(gs_base + (0 + 36232)));
    v_rsp = (v_rsp) + (8);
    result = KiVirtualizationException___0x606(a1, a2, a3, *(unsigned __int64 *)(gs_base + (0 + 36232)));
    v_rsp = (v_rsp) + (8);
    result = KiVirtualizationException___0x4EF(a1, a2, a3, *(unsigned __int64 *)(gs_base + (0 + 36232)));
    v_rsp = (v_rsp) + (8);
    result = KiVirtualizationException___0x4F8(a1, a2, a3, *(unsigned __int64 *)(gs_base + (0 + 36232)));
    v_rsp = (v_rsp) + (8);
    result = KiVirtualizationException___0x501(a1, a2, a3, *(unsigned __int64 *)(gs_base + (0 + 36232)));
    v_rsp = (v_rsp) + (8);
    result = KiVirtualizationException___0x50A(a1, a2, a3, *(unsigned __int64 *)(gs_base + (0 + 36232)));
    v_rsp = (v_rsp) + (8);
    result = KiVirtualizationException___0x513(a1, a2, a3, *(unsigned __int64 *)(gs_base + (0 + 36232)));
    v_rsp = (v_rsp) + (8);
    result = KiVirtualizationException___0x51C(a1, a2, a3, *(unsigned __int64 *)(gs_base + (0 + 36232)));
    v_rsp = (v_rsp) + (8);
    result = KiVirtualizationException___0x525(a1, a2, a3, *(unsigned __int64 *)(gs_base + (0 + 36232)));
    v_rsp = (v_rsp) + (8);
    result = KiVirtualizationException___0x52E(a1, a2, a3, *(unsigned __int64 *)(gs_base + (0 + 36232)));
    v_rsp = (v_rsp) + (8);
    result = KiVirtualizationException___0x537(a1, a2, a3, *(unsigned __int64 *)(gs_base + (0 + 36232)));
    v_rsp = (v_rsp) + (8);
    result = KiVirtualizationException___0x540(a1, a2, a3, *(unsigned __int64 *)(gs_base + (0 + 36232)));
    v_rsp = (v_rsp) + (8);
    result = KiVirtualizationException___0x549(a1, a2, a3, *(unsigned __int64 *)(gs_base + (0 + 36232)));
    v_rsp = (v_rsp) + (8);
    result = KiVirtualizationException___0x552(a1, a2, a3, *(unsigned __int64 *)(gs_base + (0 + 36232)));
    v_rsp = (v_rsp) + (8);
    result = KiVirtualizationException___0x55B(a1, a2, a3, *(unsigned __int64 *)(gs_base + (0 + 36232)));
    v_rsp = (v_rsp) + (8);
    result = KiVirtualizationException___0x564(a1, a2, a3, *(unsigned __int64 *)(gs_base + (0 + 36232)));
    v_rsp = (v_rsp) + (8);
    result = KiVirtualizationException___0x56D(a1, a2, a3, *(unsigned __int64 *)(gs_base + (0 + 36232)));
    v_rsp = (v_rsp) + (8);
    result = KiVirtualizationException___0x576(a1, a2, a3, *(unsigned __int64 *)(gs_base + (0 + 36232)));
    v_rsp = (v_rsp) + (8);
    result = KiVirtualizationException___0x57F(a1, a2, a3, *(unsigned __int64 *)(gs_base + (0 + 36232)));
    v_rsp = (v_rsp) + (8);
    result = KiVirtualizationException___0x588(a1, a2, a3, *(unsigned __int64 *)(gs_base + (0 + 36232)));
    v_rsp = (v_rsp) + (8);
    result = KiVirtualizationException___0x591(a1, a2, a3, *(unsigned __int64 *)(gs_base + (0 + 36232)));
    v_rsp = (v_rsp) + (8);
    result = KiVirtualizationException___0x59A(a1, a2, a3, *(unsigned __int64 *)(gs_base + (0 + 36232)));
    v_rsp = (v_rsp) + (8);
    result = KiVirtualizationException___0x5A3(a1, a2, a3, *(unsigned __int64 *)(gs_base + (0 + 36232)));
    v_rsp = (v_rsp) + (8);
    result = KiVirtualizationException___0x5AC(a1, a2, a3, *(unsigned __int64 *)(gs_base + (0 + 36232)));
    v_rsp = (v_rsp) + (8);
    result = KiVirtualizationException___0x5B5(a1, a2, a3, *(unsigned __int64 *)(gs_base + (0 + 36232)));
    v_rsp = (v_rsp) + (8);
    result = KiVirtualizationException___0x5BE(a1, a2, a3, *(unsigned __int64 *)(gs_base + (0 + 36232)));
    v_rsp = (v_rsp) + (8);
    result = KiVirtualizationException___0x5C7(a1, a2, a3, *(unsigned __int64 *)(gs_base + (0 + 36232)));
    v_rsp = (v_rsp) + (8);
    result = KiVirtualizationException___0x5D0(a1, a2, a3, *(unsigned __int64 *)(gs_base + (0 + 36232)));
    v_rsp = (v_rsp) + (8);
    result = KiVirtualizationException___0x5D9(a1, a2, a3, *(unsigned __int64 *)(gs_base + (0 + 36232)));
    v_rsp = (v_rsp) + (8);
    result = KiVirtualizationException___0x5E2(a1, a2, a3, *(unsigned __int64 *)(gs_base + (0 + 36232)));
    v_rsp = (v_rsp) + (8);
    result = KiVirtualizationException___0x5EB(a1, a2, a3, *(unsigned __int64 *)(gs_base + (0 + 36232)));
    v_rsp = (v_rsp) + (8);
    result = KiVirtualizationException___0x5F4(a1, a2, a3, *(unsigned __int64 *)(gs_base + (0 + 36232)));
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
    if (((*(unsigned __int8 *)(v_rip + 11790522)) & (1)) == 0) goto loc_006C2F8D;
loc_006C2F8D:
    if (((*(unsigned __int16 *)(gs_base + (0 + 2136))) & (512)) != 0) {
    }
loc_006C2FA4:
    v_rsp = (v_stack_m10) + (232);
loc_006C2FEF:
    result = KiBugCheckDispatch(127, 32, v_stack_m148, *(unsigned __int64 *)(gs_base + (0 + 36232)));
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KiVirtualizationException(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
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
    uint32_t v_stack_m148;
    uint64_t v_stack_m168;
    uint16_t v_stack_m68;
    uint64_t v_stack_m90;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p0;
    uint32_t v_stack_p10;
    uint16_t v_stack_p20;
    uint8_t v_stack_p8;

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
    if (((v_stack_p8) & (1)) != 0) goto loc_006C2975;
    Arg2 = 0;
    v_stack_m90 = 0;
    if (((*(uint8_t *)(gs_base + (0 + 0x858))) & (1)) != 0) goto loc_006C295E;
    goto loc_006C2BE6;
loc_006C295E:
    Arg2 = 0;
    goto loc_006C2BE6;
loc_006C2975:
    if (((*(uint8_t *)(v_rip + 0xB3EEC4)) & (1)) == 0) {
    }
    if (*(uint64_t *)(gs_base + (0 + 0x9D28)) == 0) goto loc_006C29B1;
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
    if ((((uint32_t)(Arg2)) & (2)) == 0) goto loc_006C2B8D;
    result = KiVirtualizationException___0x269(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiVirtualizationException___0x272(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiVirtualizationException___0x15B(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiVirtualizationException___0x164(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiVirtualizationException___0x16D(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiVirtualizationException___0x176(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiVirtualizationException___0x17F(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiVirtualizationException___0x188(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiVirtualizationException___0x191(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiVirtualizationException___0x19A(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiVirtualizationException___0x1A3(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiVirtualizationException___0x1AC(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiVirtualizationException___0x1B5(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiVirtualizationException___0x1BE(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiVirtualizationException___0x1C7(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiVirtualizationException___0x1D0(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiVirtualizationException___0x1D9(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiVirtualizationException___0x1E2(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiVirtualizationException___0x1EB(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiVirtualizationException___0x1F4(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiVirtualizationException___0x1FD(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiVirtualizationException___0x206(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiVirtualizationException___0x20F(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiVirtualizationException___0x218(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiVirtualizationException___0x221(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiVirtualizationException___0x22A(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiVirtualizationException___0x233(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiVirtualizationException___0x23C(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiVirtualizationException___0x245(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiVirtualizationException___0x24E(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiVirtualizationException___0x257(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiVirtualizationException___0x260(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = (uint32_t)(0xDADAULL);
    if (((*(uint8_t *)(gs_base + (0 + 0x85C))) & (8)) != 0) {
        result = 32;
    }
    if ((((uint32_t)(Arg2)) & (128)) != 0) {
        result = KiFlushBhbDuringTrapEntryOrExit(Arg1, Arg2, Arg3, Arg4);
    }
    *(uint8_t *)(gs_base + (0 + 0x85E)) = 0;
    if ((*(uint32_t *)(v_rip + 0x9046B4)) == 0) goto loc_006C2BD1;
    if (((uint32_t)(Arg2)) == 0) goto loc_006C2BD1;
    Arg2 = (uint32_t)((Arg2) & (*(uint32_t *)(v_rip + 0x90469E)));
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
    if (((*(uint8_t *)(v_rip + 0x903FCF)) & (255)) == 0) goto loc_006C2C2F;
    if (((v_stack_p8) & (1)) != 0) {
    }
    if (*(uint64_t *)(gs_base + (0 + 0x8D88)) == 0) goto loc_006C2FEF;
    if ((*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x8D88)) + 0x44)) != 1) goto loc_006C2FEF;
    if (((v_stack_p10) & (512)) == 0) goto loc_006C2FEF;
    v_stack_m148 = (uint32_t)(v_cr8);
    if (((uint8_t)(v_cr8)) >= 2) goto loc_006C2FEF;
    result = KzRaiseIrql(2, Arg2, Arg3, *(uint64_t *)(gs_base + (0 + 0x8D88)));
    *(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x8D88)) + 0x44) = 0;
    result = KiEpfHandleNotification(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x8D88)) + 0x48), Arg2, Arg3, *(uint64_t *)(gs_base + (0 + 0x8D88)));
    result = KiCheckForSListAddress(v_stack_m168, Arg2, Arg3, *(uint64_t *)(gs_base + (0 + 0x8D88)));
    result = KzLowerIrql((uint32_t)(v_stack_m148), Arg2, Arg3, *(uint64_t *)(gs_base + (0 + 0x8D88)));
    if (((v_stack_p8) & (1)) == 0) goto loc_006C2FA4;
    if (((*(uint8_t *)(v_rip + 0x903F3A)) & (255)) != 0) {
    }
    if (((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xC2)) & (3)) == 0) goto loc_006C2CE8;
    result = KiInitiateUserApc(1, Arg2, Arg3, *(uint64_t *)(gs_base + (0 + 0x8D88)));
    goto loc_006C2CBB;
loc_006C2CE8:
    result = KiSynchronizeUserIsolationDomainEntry(0, Arg2, Arg3, *(uint64_t *)(gs_base + (0 + 0x8D88)));
    if ((uint32_t)(result) != 0) goto loc_006C2CBB;
    result = v_stack_m138;
    if (((*(uint8_t *)(gs_base + (0 + 0x860))) & (2)) != 0) {
        Arg1 = 0;
        result = KiUpdateStibpPairing(Arg1, Arg2, Arg3, *(uint64_t *)(gs_base + (0 + 0x8D88)));
    }
    if (((*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)))) & (0x8000000ULL)) != 0) {
        result = KiRestoreSetContextState(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, Arg3, *(uint64_t *)(gs_base + (0 + 0x8D88)));
    }
    if (((*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)))) & (0x10000ULL)) == 0) goto loc_006C2D42;
    if (((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x2)) & (1)) != 0) {
        result = KiCopyCounters(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, Arg3, *(uint64_t *)(gs_base + (0 + 0x8D88)));
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x188));
    }
    if (v_stack_m68 != 0) {
        result = KiRestoreDebugRegisterState(Arg1, Arg2, Arg3, *(uint64_t *)(gs_base + (0 + 0x8D88)));
    }
    if (v_stack_m68 >= 0) goto loc_006C2D8F;
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
    if (condition_is_above_or_equal) goto loc_006C2F21;
    result = KiVirtualizationException___0x5FD(Arg1, Arg2, Arg3, *(uint64_t *)(gs_base + (0 + 0x8D88)));
    local_rsp = (local_rsp) + (8);
    result = KiVirtualizationException___0x606(Arg1, Arg2, Arg3, *(uint64_t *)(gs_base + (0 + 0x8D88)));
    local_rsp = (local_rsp) + (8);
    result = KiVirtualizationException___0x4EF(Arg1, Arg2, Arg3, *(uint64_t *)(gs_base + (0 + 0x8D88)));
    local_rsp = (local_rsp) + (8);
    result = KiVirtualizationException___0x4F8(Arg1, Arg2, Arg3, *(uint64_t *)(gs_base + (0 + 0x8D88)));
    local_rsp = (local_rsp) + (8);
    result = KiVirtualizationException___0x501(Arg1, Arg2, Arg3, *(uint64_t *)(gs_base + (0 + 0x8D88)));
    local_rsp = (local_rsp) + (8);
    result = KiVirtualizationException___0x50A(Arg1, Arg2, Arg3, *(uint64_t *)(gs_base + (0 + 0x8D88)));
    local_rsp = (local_rsp) + (8);
    result = KiVirtualizationException___0x513(Arg1, Arg2, Arg3, *(uint64_t *)(gs_base + (0 + 0x8D88)));
    local_rsp = (local_rsp) + (8);
    result = KiVirtualizationException___0x51C(Arg1, Arg2, Arg3, *(uint64_t *)(gs_base + (0 + 0x8D88)));
    local_rsp = (local_rsp) + (8);
    result = KiVirtualizationException___0x525(Arg1, Arg2, Arg3, *(uint64_t *)(gs_base + (0 + 0x8D88)));
    local_rsp = (local_rsp) + (8);
    result = KiVirtualizationException___0x52E(Arg1, Arg2, Arg3, *(uint64_t *)(gs_base + (0 + 0x8D88)));
    local_rsp = (local_rsp) + (8);
    result = KiVirtualizationException___0x537(Arg1, Arg2, Arg3, *(uint64_t *)(gs_base + (0 + 0x8D88)));
    local_rsp = (local_rsp) + (8);
    result = KiVirtualizationException___0x540(Arg1, Arg2, Arg3, *(uint64_t *)(gs_base + (0 + 0x8D88)));
    local_rsp = (local_rsp) + (8);
    result = KiVirtualizationException___0x549(Arg1, Arg2, Arg3, *(uint64_t *)(gs_base + (0 + 0x8D88)));
    local_rsp = (local_rsp) + (8);
    result = KiVirtualizationException___0x552(Arg1, Arg2, Arg3, *(uint64_t *)(gs_base + (0 + 0x8D88)));
    local_rsp = (local_rsp) + (8);
    result = KiVirtualizationException___0x55B(Arg1, Arg2, Arg3, *(uint64_t *)(gs_base + (0 + 0x8D88)));
    local_rsp = (local_rsp) + (8);
    result = KiVirtualizationException___0x564(Arg1, Arg2, Arg3, *(uint64_t *)(gs_base + (0 + 0x8D88)));
    local_rsp = (local_rsp) + (8);
    result = KiVirtualizationException___0x56D(Arg1, Arg2, Arg3, *(uint64_t *)(gs_base + (0 + 0x8D88)));
    local_rsp = (local_rsp) + (8);
    result = KiVirtualizationException___0x576(Arg1, Arg2, Arg3, *(uint64_t *)(gs_base + (0 + 0x8D88)));
    local_rsp = (local_rsp) + (8);
    result = KiVirtualizationException___0x57F(Arg1, Arg2, Arg3, *(uint64_t *)(gs_base + (0 + 0x8D88)));
    local_rsp = (local_rsp) + (8);
    result = KiVirtualizationException___0x588(Arg1, Arg2, Arg3, *(uint64_t *)(gs_base + (0 + 0x8D88)));
    local_rsp = (local_rsp) + (8);
    result = KiVirtualizationException___0x591(Arg1, Arg2, Arg3, *(uint64_t *)(gs_base + (0 + 0x8D88)));
    local_rsp = (local_rsp) + (8);
    result = KiVirtualizationException___0x59A(Arg1, Arg2, Arg3, *(uint64_t *)(gs_base + (0 + 0x8D88)));
    local_rsp = (local_rsp) + (8);
    result = KiVirtualizationException___0x5A3(Arg1, Arg2, Arg3, *(uint64_t *)(gs_base + (0 + 0x8D88)));
    local_rsp = (local_rsp) + (8);
    result = KiVirtualizationException___0x5AC(Arg1, Arg2, Arg3, *(uint64_t *)(gs_base + (0 + 0x8D88)));
    local_rsp = (local_rsp) + (8);
    result = KiVirtualizationException___0x5B5(Arg1, Arg2, Arg3, *(uint64_t *)(gs_base + (0 + 0x8D88)));
    local_rsp = (local_rsp) + (8);
    result = KiVirtualizationException___0x5BE(Arg1, Arg2, Arg3, *(uint64_t *)(gs_base + (0 + 0x8D88)));
    local_rsp = (local_rsp) + (8);
    result = KiVirtualizationException___0x5C7(Arg1, Arg2, Arg3, *(uint64_t *)(gs_base + (0 + 0x8D88)));
    local_rsp = (local_rsp) + (8);
    result = KiVirtualizationException___0x5D0(Arg1, Arg2, Arg3, *(uint64_t *)(gs_base + (0 + 0x8D88)));
    local_rsp = (local_rsp) + (8);
    result = KiVirtualizationException___0x5D9(Arg1, Arg2, Arg3, *(uint64_t *)(gs_base + (0 + 0x8D88)));
    local_rsp = (local_rsp) + (8);
    result = KiVirtualizationException___0x5E2(Arg1, Arg2, Arg3, *(uint64_t *)(gs_base + (0 + 0x8D88)));
    local_rsp = (local_rsp) + (8);
    result = KiVirtualizationException___0x5EB(Arg1, Arg2, Arg3, *(uint64_t *)(gs_base + (0 + 0x8D88)));
    local_rsp = (local_rsp) + (8);
    result = KiVirtualizationException___0x5F4(Arg1, Arg2, Arg3, *(uint64_t *)(gs_base + (0 + 0x8D88)));
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
    if (((*(uint8_t *)(v_rip + 0xB3E8BA)) & (1)) == 0) goto loc_006C2F8D;
loc_006C2F8D:
    if (((*(uint16_t *)(gs_base + (0 + 0x858))) & (512)) != 0) {
    }
loc_006C2FA4:
    local_rsp = (v_stack_m10) + (232);
loc_006C2FEF:
    result = KiBugCheckDispatch(127, 32, v_stack_m148, *(uint64_t *)(gs_base + (0 + 0x8D88)));
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006C2900&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
