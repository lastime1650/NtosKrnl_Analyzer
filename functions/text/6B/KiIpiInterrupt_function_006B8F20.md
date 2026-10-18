# KiIpiInterrupt

- RVA: `0x006B8F20`–`0x006B964E` (길이 `1,838` bytes)
- VA: `0x00000001406B8F20`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C22D0`
- 디코드: `399`개 명령, `1,838/1,838` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **80**; 고유 호출 대상: **80**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **8**

### Outgoing calls
- `0x006B9077` → [KiIpiInterrupt + 0x26A](KiIpiInterrupt_function_006B8F20.md) (inside-function, `0x006B918A`)
- `0x006B9080` → [KiIpiInterrupt + 0x273](KiIpiInterrupt_function_006B8F20.md) (inside-function, `0x006B9193`)
- `0x006B9089` → [KiIpiInterrupt + 0x15C](KiIpiInterrupt_function_006B8F20.md) (inside-function, `0x006B907C`)
- `0x006B9092` → [KiIpiInterrupt + 0x165](KiIpiInterrupt_function_006B8F20.md) (inside-function, `0x006B9085`)
- `0x006B909B` → [KiIpiInterrupt + 0x16E](KiIpiInterrupt_function_006B8F20.md) (inside-function, `0x006B908E`)
- `0x006B90A4` → [KiIpiInterrupt + 0x177](KiIpiInterrupt_function_006B8F20.md) (inside-function, `0x006B9097`)
- `0x006B90AD` → [KiIpiInterrupt + 0x180](KiIpiInterrupt_function_006B8F20.md) (inside-function, `0x006B90A0`)
- `0x006B90B6` → [KiIpiInterrupt + 0x189](KiIpiInterrupt_function_006B8F20.md) (inside-function, `0x006B90A9`)
- `0x006B90BF` → [KiIpiInterrupt + 0x192](KiIpiInterrupt_function_006B8F20.md) (inside-function, `0x006B90B2`)
- `0x006B90C8` → [KiIpiInterrupt + 0x19B](KiIpiInterrupt_function_006B8F20.md) (inside-function, `0x006B90BB`)
- `0x006B90D1` → [KiIpiInterrupt + 0x1A4](KiIpiInterrupt_function_006B8F20.md) (inside-function, `0x006B90C4`)
- `0x006B90DA` → [KiIpiInterrupt + 0x1AD](KiIpiInterrupt_function_006B8F20.md) (inside-function, `0x006B90CD`)
- `0x006B90E3` → [KiIpiInterrupt + 0x1B6](KiIpiInterrupt_function_006B8F20.md) (inside-function, `0x006B90D6`)
- `0x006B90EC` → [KiIpiInterrupt + 0x1BF](KiIpiInterrupt_function_006B8F20.md) (inside-function, `0x006B90DF`)
- `0x006B90F5` → [KiIpiInterrupt + 0x1C8](KiIpiInterrupt_function_006B8F20.md) (inside-function, `0x006B90E8`)
- `0x006B90FE` → [KiIpiInterrupt + 0x1D1](KiIpiInterrupt_function_006B8F20.md) (inside-function, `0x006B90F1`)
- `0x006B9107` → [KiIpiInterrupt + 0x1DA](KiIpiInterrupt_function_006B8F20.md) (inside-function, `0x006B90FA`)
- `0x006B9110` → [KiIpiInterrupt + 0x1E3](KiIpiInterrupt_function_006B8F20.md) (inside-function, `0x006B9103`)
- `0x006B9119` → [KiIpiInterrupt + 0x1EC](KiIpiInterrupt_function_006B8F20.md) (inside-function, `0x006B910C`)
- `0x006B9122` → [KiIpiInterrupt + 0x1F5](KiIpiInterrupt_function_006B8F20.md) (inside-function, `0x006B9115`)
- `0x006B912B` → [KiIpiInterrupt + 0x1FE](KiIpiInterrupt_function_006B8F20.md) (inside-function, `0x006B911E`)
- `0x006B9134` → [KiIpiInterrupt + 0x207](KiIpiInterrupt_function_006B8F20.md) (inside-function, `0x006B9127`)
- `0x006B913D` → [KiIpiInterrupt + 0x210](KiIpiInterrupt_function_006B8F20.md) (inside-function, `0x006B9130`)
- `0x006B9146` → [KiIpiInterrupt + 0x219](KiIpiInterrupt_function_006B8F20.md) (inside-function, `0x006B9139`)
- `0x006B914F` → [KiIpiInterrupt + 0x222](KiIpiInterrupt_function_006B8F20.md) (inside-function, `0x006B9142`)
- `0x006B9158` → [KiIpiInterrupt + 0x22B](KiIpiInterrupt_function_006B8F20.md) (inside-function, `0x006B914B`)
- `0x006B9161` → [KiIpiInterrupt + 0x234](KiIpiInterrupt_function_006B8F20.md) (inside-function, `0x006B9154`)
- `0x006B916A` → [KiIpiInterrupt + 0x23D](KiIpiInterrupt_function_006B8F20.md) (inside-function, `0x006B915D`)
- `0x006B9173` → [KiIpiInterrupt + 0x246](KiIpiInterrupt_function_006B8F20.md) (inside-function, `0x006B9166`)
- `0x006B917C` → [KiIpiInterrupt + 0x24F](KiIpiInterrupt_function_006B8F20.md) (inside-function, `0x006B916F`)
- `0x006B9185` → [KiIpiInterrupt + 0x258](KiIpiInterrupt_function_006B8F20.md) (inside-function, `0x006B9178`)
- `0x006B918E` → [KiIpiInterrupt + 0x261](KiIpiInterrupt_function_006B8F20.md) (inside-function, `0x006B9181`)
- `0x006B91B9` → [KiFlushBhbDuringTrapEntryOrExit](../6C/KiFlushBhbDuringTrapEntryOrExit_function_006C6340.md) (function, `0x006C6340`)
- `0x006B9202` → [KiSaveDebugRegisterState](../4F/KiSaveDebugRegisterState_function_004FD960.md) (function, `0x004FD960`)
- `0x006B9236` → [KiSynchronizeUserIsolationDomainExit](../41/KiSynchronizeUserIsolationDomainExit_function_0041BFA0.md) (function, `0x0041BFA0`)
- `0x006B9246` → [KeWakeProcessor](../5B/KeWakeProcessor_function_005BE080.md) (function, `0x005BE080`)
- `0x006B926F` → [KiCheckForSListAddress](../40/KiCheckForSListAddress_function_0040B810.md) (function, `0x0040B810`)
- `0x006B92B5` → [KiIpiInterruptSubDispatch](KiIpiInterruptSubDispatch_function_006B9660.md) (function, `0x006B9660`)
- `0x006B92C2` → [HalPerformEndOfInterrupt](../41/HalPerformEndOfInterrupt_function_00418E20.md) (function, `0x00418E20`)
- `0x006B92D4` → [KiEndInterruptCycleAccumulation](../3F/KiEndInterruptCycleAccumulation_function_003FAAE0.md) (function, `0x003FAAE0`)
- `0x006B92DD` → [KiDpcInterruptBypass](KiDpcInterruptBypass_function_006B8EE0.md) (function, `0x006B8EE0`)
- `0x006B92EF` → [KzSetIrqlUnsafe](../5B/KzSetIrqlUnsafe_function_005B8AE0.md) (function, `0x005B8AE0`)
- `0x006B9336` → [KiInitiateUserApc](KiInitiateUserApc_function_006B6540.md) (function, `0x006B6540`)
- `0x006B9347` → [KiSynchronizeUserIsolationDomainEntry](../26/KiSynchronizeUserIsolationDomainEntry_function_00263F60.md) (function, `0x00263F60`)
- `0x006B9361` → [KiUpdateStibpPairing](../3E/KiUpdateStibpPairing_function_003E71C0.md) (function, `0x003E71C0`)
- `0x006B9377` → [KiRestoreSetContextState](KiRestoreSetContextState_function_006B1CA0.md) (function, `0x006B1CA0`)
- `0x006B9393` → [KiCopyCounters](../5C/KiCopyCounters_function_005C0710.md) (function, `0x005C0710`)
- `0x006B93AF` → [KiRestoreDebugRegisterState](../4F/KiRestoreDebugRegisterState_function_004FD8E0.md) (function, `0x004FD8E0`)
- `0x006B9449` → [KiIpiInterrupt + 0x63C](KiIpiInterrupt_function_006B8F20.md) (inside-function, `0x006B955C`)
- `0x006B9452` → [KiIpiInterrupt + 0x645](KiIpiInterrupt_function_006B8F20.md) (inside-function, `0x006B9565`)
- `0x006B945B` → [KiIpiInterrupt + 0x52E](KiIpiInterrupt_function_006B8F20.md) (inside-function, `0x006B944E`)
- `0x006B9464` → [KiIpiInterrupt + 0x537](KiIpiInterrupt_function_006B8F20.md) (inside-function, `0x006B9457`)
- `0x006B946D` → [KiIpiInterrupt + 0x540](KiIpiInterrupt_function_006B8F20.md) (inside-function, `0x006B9460`)
- `0x006B9476` → [KiIpiInterrupt + 0x549](KiIpiInterrupt_function_006B8F20.md) (inside-function, `0x006B9469`)
- `0x006B947F` → [KiIpiInterrupt + 0x552](KiIpiInterrupt_function_006B8F20.md) (inside-function, `0x006B9472`)
- `0x006B9488` → [KiIpiInterrupt + 0x55B](KiIpiInterrupt_function_006B8F20.md) (inside-function, `0x006B947B`)
- `0x006B9491` → [KiIpiInterrupt + 0x564](KiIpiInterrupt_function_006B8F20.md) (inside-function, `0x006B9484`)
- `0x006B949A` → [KiIpiInterrupt + 0x56D](KiIpiInterrupt_function_006B8F20.md) (inside-function, `0x006B948D`)
- `0x006B94A3` → [KiIpiInterrupt + 0x576](KiIpiInterrupt_function_006B8F20.md) (inside-function, `0x006B9496`)
- `0x006B94AC` → [KiIpiInterrupt + 0x57F](KiIpiInterrupt_function_006B8F20.md) (inside-function, `0x006B949F`)
- `0x006B94B5` → [KiIpiInterrupt + 0x588](KiIpiInterrupt_function_006B8F20.md) (inside-function, `0x006B94A8`)
- `0x006B94BE` → [KiIpiInterrupt + 0x591](KiIpiInterrupt_function_006B8F20.md) (inside-function, `0x006B94B1`)
- `0x006B94C7` → [KiIpiInterrupt + 0x59A](KiIpiInterrupt_function_006B8F20.md) (inside-function, `0x006B94BA`)
- `0x006B94D0` → [KiIpiInterrupt + 0x5A3](KiIpiInterrupt_function_006B8F20.md) (inside-function, `0x006B94C3`)
- `0x006B94D9` → [KiIpiInterrupt + 0x5AC](KiIpiInterrupt_function_006B8F20.md) (inside-function, `0x006B94CC`)
- `0x006B94E2` → [KiIpiInterrupt + 0x5B5](KiIpiInterrupt_function_006B8F20.md) (inside-function, `0x006B94D5`)
- `0x006B94EB` → [KiIpiInterrupt + 0x5BE](KiIpiInterrupt_function_006B8F20.md) (inside-function, `0x006B94DE`)
- `0x006B94F4` → [KiIpiInterrupt + 0x5C7](KiIpiInterrupt_function_006B8F20.md) (inside-function, `0x006B94E7`)
- `0x006B94FD` → [KiIpiInterrupt + 0x5D0](KiIpiInterrupt_function_006B8F20.md) (inside-function, `0x006B94F0`)
- `0x006B9506` → [KiIpiInterrupt + 0x5D9](KiIpiInterrupt_function_006B8F20.md) (inside-function, `0x006B94F9`)
- `0x006B950F` → [KiIpiInterrupt + 0x5E2](KiIpiInterrupt_function_006B8F20.md) (inside-function, `0x006B9502`)
- `0x006B9518` → [KiIpiInterrupt + 0x5EB](KiIpiInterrupt_function_006B8F20.md) (inside-function, `0x006B950B`)
- `0x006B9521` → [KiIpiInterrupt + 0x5F4](KiIpiInterrupt_function_006B8F20.md) (inside-function, `0x006B9514`)
- `0x006B952A` → [KiIpiInterrupt + 0x5FD](KiIpiInterrupt_function_006B8F20.md) (inside-function, `0x006B951D`)
- `0x006B9533` → [KiIpiInterrupt + 0x606](KiIpiInterrupt_function_006B8F20.md) (inside-function, `0x006B9526`)
- `0x006B953C` → [KiIpiInterrupt + 0x60F](KiIpiInterrupt_function_006B8F20.md) (inside-function, `0x006B952F`)
- `0x006B9545` → [KiIpiInterrupt + 0x618](KiIpiInterrupt_function_006B8F20.md) (inside-function, `0x006B9538`)
- `0x006B954E` → [KiIpiInterrupt + 0x621](KiIpiInterrupt_function_006B8F20.md) (inside-function, `0x006B9541`)
- `0x006B9557` → [KiIpiInterrupt + 0x62A](KiIpiInterrupt_function_006B8F20.md) (inside-function, `0x006B954A`)
- `0x006B9560` → [KiIpiInterrupt + 0x633](KiIpiInterrupt_function_006B8F20.md) (inside-function, `0x006B9553`)

### Direct callers
- [KiIpiInterrupt](KiIpiInterrupt_function_006B8F20.md) at `0x006B9077`
- [KiIpiInterrupt](KiIpiInterrupt_function_006B8F20.md) at `0x006B9080`
- [KiIpiInterrupt](KiIpiInterrupt_function_006B8F20.md) at `0x006B9089`
- [KiIpiInterrupt](KiIpiInterrupt_function_006B8F20.md) at `0x006B9092`
- [KiIpiInterrupt](KiIpiInterrupt_function_006B8F20.md) at `0x006B909B`
- [KiIpiInterrupt](KiIpiInterrupt_function_006B8F20.md) at `0x006B90A4`
- [KiIpiInterrupt](KiIpiInterrupt_function_006B8F20.md) at `0x006B90AD`
- [KiIpiInterrupt](KiIpiInterrupt_function_006B8F20.md) at `0x006B90B6`
- [KiIpiInterrupt](KiIpiInterrupt_function_006B8F20.md) at `0x006B90BF`
- [KiIpiInterrupt](KiIpiInterrupt_function_006B8F20.md) at `0x006B90C8`
- [KiIpiInterrupt](KiIpiInterrupt_function_006B8F20.md) at `0x006B90D1`
- [KiIpiInterrupt](KiIpiInterrupt_function_006B8F20.md) at `0x006B90DA`
- [KiIpiInterrupt](KiIpiInterrupt_function_006B8F20.md) at `0x006B90E3`
- [KiIpiInterrupt](KiIpiInterrupt_function_006B8F20.md) at `0x006B90EC`
- [KiIpiInterrupt](KiIpiInterrupt_function_006B8F20.md) at `0x006B90F5`
- [KiIpiInterrupt](KiIpiInterrupt_function_006B8F20.md) at `0x006B90FE`
- [KiIpiInterrupt](KiIpiInterrupt_function_006B8F20.md) at `0x006B9107`
- [KiIpiInterrupt](KiIpiInterrupt_function_006B8F20.md) at `0x006B9110`
- [KiIpiInterrupt](KiIpiInterrupt_function_006B8F20.md) at `0x006B9119`
- [KiIpiInterrupt](KiIpiInterrupt_function_006B8F20.md) at `0x006B9122`
- [KiIpiInterrupt](KiIpiInterrupt_function_006B8F20.md) at `0x006B912B`
- [KiIpiInterrupt](KiIpiInterrupt_function_006B8F20.md) at `0x006B9134`
- [KiIpiInterrupt](KiIpiInterrupt_function_006B8F20.md) at `0x006B913D`
- [KiIpiInterrupt](KiIpiInterrupt_function_006B8F20.md) at `0x006B9146`
- [KiIpiInterrupt](KiIpiInterrupt_function_006B8F20.md) at `0x006B914F`
- [KiIpiInterrupt](KiIpiInterrupt_function_006B8F20.md) at `0x006B9158`
- [KiIpiInterrupt](KiIpiInterrupt_function_006B8F20.md) at `0x006B9161`
- [KiIpiInterrupt](KiIpiInterrupt_function_006B8F20.md) at `0x006B916A`
- [KiIpiInterrupt](KiIpiInterrupt_function_006B8F20.md) at `0x006B9173`
- [KiIpiInterrupt](KiIpiInterrupt_function_006B8F20.md) at `0x006B917C`
- [KiIpiInterrupt](KiIpiInterrupt_function_006B8F20.md) at `0x006B9185`
- [KiIpiInterrupt](KiIpiInterrupt_function_006B8F20.md) at `0x006B918E`
- [KiIpiInterrupt](KiIpiInterrupt_function_006B8F20.md) at `0x006B9449`
- [KiIpiInterrupt](KiIpiInterrupt_function_006B8F20.md) at `0x006B9452`
- [KiIpiInterrupt](KiIpiInterrupt_function_006B8F20.md) at `0x006B945B`
- [KiIpiInterrupt](KiIpiInterrupt_function_006B8F20.md) at `0x006B9464`
- [KiIpiInterrupt](KiIpiInterrupt_function_006B8F20.md) at `0x006B946D`
- [KiIpiInterrupt](KiIpiInterrupt_function_006B8F20.md) at `0x006B9476`
- [KiIpiInterrupt](KiIpiInterrupt_function_006B8F20.md) at `0x006B947F`
- [KiIpiInterrupt](KiIpiInterrupt_function_006B8F20.md) at `0x006B9488`
- [KiIpiInterrupt](KiIpiInterrupt_function_006B8F20.md) at `0x006B9491`
- [KiIpiInterrupt](KiIpiInterrupt_function_006B8F20.md) at `0x006B949A`
- [KiIpiInterrupt](KiIpiInterrupt_function_006B8F20.md) at `0x006B94A3`
- [KiIpiInterrupt](KiIpiInterrupt_function_006B8F20.md) at `0x006B94AC`
- [KiIpiInterrupt](KiIpiInterrupt_function_006B8F20.md) at `0x006B94B5`
- [KiIpiInterrupt](KiIpiInterrupt_function_006B8F20.md) at `0x006B94BE`
- [KiIpiInterrupt](KiIpiInterrupt_function_006B8F20.md) at `0x006B94C7`
- [KiIpiInterrupt](KiIpiInterrupt_function_006B8F20.md) at `0x006B94D0`
- [KiIpiInterrupt](KiIpiInterrupt_function_006B8F20.md) at `0x006B94D9`
- [KiIpiInterrupt](KiIpiInterrupt_function_006B8F20.md) at `0x006B94E2`
- [KiIpiInterrupt](KiIpiInterrupt_function_006B8F20.md) at `0x006B94EB`
- [KiIpiInterrupt](KiIpiInterrupt_function_006B8F20.md) at `0x006B94F4`
- [KiIpiInterrupt](KiIpiInterrupt_function_006B8F20.md) at `0x006B94FD`
- [KiIpiInterrupt](KiIpiInterrupt_function_006B8F20.md) at `0x006B9506`
- [KiIpiInterrupt](KiIpiInterrupt_function_006B8F20.md) at `0x006B950F`
- [KiIpiInterrupt](KiIpiInterrupt_function_006B8F20.md) at `0x006B9518`
- [KiIpiInterrupt](KiIpiInterrupt_function_006B8F20.md) at `0x006B9521`
- [KiIpiInterrupt](KiIpiInterrupt_function_006B8F20.md) at `0x006B952A`
- [KiIpiInterrupt](KiIpiInterrupt_function_006B8F20.md) at `0x006B9533`
- [KiIpiInterrupt](KiIpiInterrupt_function_006B8F20.md) at `0x006B953C`
- [KiIpiInterrupt](KiIpiInterrupt_function_006B8F20.md) at `0x006B9545`
- [KiIpiInterrupt](KiIpiInterrupt_function_006B8F20.md) at `0x006B954E`
- [KiIpiInterrupt](KiIpiInterrupt_function_006B8F20.md) at `0x006B9557`
- [KiIpiInterrupt](KiIpiInterrupt_function_006B8F20.md) at `0x006B9560`

### Static image references
- `0x006B8F96` → RVA `0x01201840` (`CFGRO`; read)
- `0x006B91CA` → RVA `0x00FC7264` (`ALMOSTRO`; read)
- `0x006B924B` → RVA `0x006BA577` (`ExpInterlockedPopEntrySListResume`; read)
- `0x006B925B` → RVA `0x006BA590` (`ExpInterlockedPopEntrySListEnd`; read)
- `0x006B928A` → RVA `0x00FC505C` (`ALMOSTRO`; read)
- `0x006B92A0` → RVA `0x00F4754C` (`.data`; read)
- `0x006B92E6` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x006B930E` → RVA `0x00FC6BF0` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006B95E7` → [KiKernelExit](../../kvascode/BC/KiKernelExit_function_00BCCB80.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006B8F20  48 83 EC 08                     sub rsp, 8
006B8F24  55                              push rbp
006B8F25  56                              push rsi
006B8F26  48 81 EC 50 01 00 00            sub rsp, 0x150
006B8F2D  48 8D AC 24 80 00 00 00         lea rbp, [rsp + 0x80]
006B8F35  C6 45 AB 00                     mov byte ptr [rbp - 0x55], 0
006B8F39  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
006B8F3D  48 89 4D B8                     mov qword ptr [rbp - 0x48], rcx
006B8F41  48 89 55 C0                     mov qword ptr [rbp - 0x40], rdx
006B8F45  4C 89 45 C8                     mov qword ptr [rbp - 0x38], r8
006B8F49  4C 89 4D D0                     mov qword ptr [rbp - 0x30], r9
006B8F4D  4C 89 55 D8                     mov qword ptr [rbp - 0x28], r10
006B8F51  4C 89 5D E0                     mov qword ptr [rbp - 0x20], r11
006B8F55  F6 85 F0 00 00 00 01            test byte ptr [rbp + 0xf0], 1
006B8F5C  75 38                           jne 0x1406b8f96
006B8F5E  33 D2                           xor edx, edx
006B8F60  F3 48 0F 1E CA                  rdsspq rdx
006B8F65  48 89 55 58                     mov qword ptr [rbp + 0x58], rdx
006B8F69  0F AE E8                        lfence
006B8F6C  65 F6 04 25 58 08 00 00 01      test byte ptr gs:[0x858], 1
006B8F75  75 08                           jne 0x1406b8f7f
006B8F77  0F AE E8                        lfence
006B8F7A  E9 88 02 00 00                  jmp 0x1406b9207
006B8F7F  65 0F B7 04 25 66 08 00 00      movzx eax, word ptr gs:[0x866]
006B8F88  B9 48 00 00 00                  mov ecx, 0x48
006B8F8D  33 D2                           xor edx, edx
006B8F8F  0F 30                           wrmsr
006B8F91  E9 71 02 00 00                  jmp 0x1406b9207
006B8F96  F6 05 A3 88 B4 00 01            test byte ptr [rip + 0xb488a3], 1
006B8F9D  75 03                           jne 0x1406b8fa2
006B8F9F  0F 01 F8                        swapgs
006B8FA2  0F AE E8                        lfence
006B8FA5  65 48 8B 0C 25 28 9D 00 00      mov rcx, qword ptr gs:[0x9d28]
006B8FAE  48 85 C9                        test rcx, rcx
006B8FB1  74 1F                           je 0x1406b8fd2
006B8FB3  F3 48 0F 1E CA                  rdsspq rdx
006B8FB8  65 4C 8B 14 25 20 9D 00 00      mov r10, qword ptr gs:[0x9d20]
006B8FC1  49 83 C2 08                     add r10, 8
006B8FC5  49 3B D2                        cmp rdx, r10
006B8FC8  75 08                           jne 0x1406b8fd2
006B8FCA  F3 0F 01 29                     rstorssp dword ptr [rcx]
006B8FCE  F3 0F 01 EA                     saveprevssp
006B8FD2  65 4C 8B 14 25 88 01 00 00      mov r10, qword ptr gs:[0x188]
006B8FDB  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006B8FE4  48 8B 89 20 02 00 00            mov rcx, qword ptr [rcx + 0x220]
006B8FEB  48 8B 89 60 07 00 00            mov rcx, qword ptr [rcx + 0x760]
006B8FF2  65 48 89 0C 25 50 08 00 00      mov qword ptr gs:[0x850], rcx
006B8FFB  66 65 8B 0C 25 62 08 00 00      mov cx, word ptr gs:[0x862]
006B9004  66 65 89 0C 25 64 08 00 00      mov word ptr gs:[0x864], cx
006B900D  65 8A 0C 25 58 08 00 00         mov cl, byte ptr gs:[0x858]
006B9015  65 88 0C 25 5A 08 00 00         mov byte ptr gs:[0x85a], cl
006B901D  65 0F B7 04 25 68 08 00 00      movzx eax, word ptr gs:[0x868]
006B9026  66 65 39 04 25 66 08 00 00      cmp word ptr gs:[0x866], ax
006B902F  74 12                           je 0x1406b9043
006B9031  66 65 89 04 25 66 08 00 00      mov word ptr gs:[0x866], ax
006B903A  B9 48 00 00 00                  mov ecx, 0x48
006B903F  33 D2                           xor edx, edx
006B9041  0F 30                           wrmsr
006B9043  65 0F B6 14 25 58 08 00 00      movzx edx, byte ptr gs:[0x858]
006B904C  F7 C2 08 00 00 00               test edx, 8
006B9052  74 17                           je 0x1406b906b
006B9054  B8 01 00 00 00                  mov eax, 1
006B9059  33 D2                           xor edx, edx
006B905B  B9 49 00 00 00                  mov ecx, 0x49
006B9060  0F 30                           wrmsr
006B9062  65 0F B6 14 25 58 08 00 00      movzx edx, byte ptr gs:[0x858]
006B906B  F7 C2 02 00 00 00               test edx, 2
006B9071  0F 84 37 01 00 00               je 0x1406b91ae
006B9077  E8 0E 01 00 00                  call 0x1406b918a
006B907C  48 83 C4 08                     add rsp, 8
006B9080  E8 0E 01 00 00                  call 0x1406b9193
006B9085  48 83 C4 08                     add rsp, 8
006B9089  E8 EE FF FF FF                  call 0x1406b907c
006B908E  48 83 C4 08                     add rsp, 8
006B9092  E8 EE FF FF FF                  call 0x1406b9085
006B9097  48 83 C4 08                     add rsp, 8
006B909B  E8 EE FF FF FF                  call 0x1406b908e
006B90A0  48 83 C4 08                     add rsp, 8
006B90A4  E8 EE FF FF FF                  call 0x1406b9097
006B90A9  48 83 C4 08                     add rsp, 8
006B90AD  E8 EE FF FF FF                  call 0x1406b90a0
006B90B2  48 83 C4 08                     add rsp, 8
006B90B6  E8 EE FF FF FF                  call 0x1406b90a9
006B90BB  48 83 C4 08                     add rsp, 8
006B90BF  E8 EE FF FF FF                  call 0x1406b90b2
006B90C4  48 83 C4 08                     add rsp, 8
006B90C8  E8 EE FF FF FF                  call 0x1406b90bb
006B90CD  48 83 C4 08                     add rsp, 8
006B90D1  E8 EE FF FF FF                  call 0x1406b90c4
006B90D6  48 83 C4 08                     add rsp, 8
006B90DA  E8 EE FF FF FF                  call 0x1406b90cd
006B90DF  48 83 C4 08                     add rsp, 8
006B90E3  E8 EE FF FF FF                  call 0x1406b90d6
006B90E8  48 83 C4 08                     add rsp, 8
006B90EC  E8 EE FF FF FF                  call 0x1406b90df
006B90F1  48 83 C4 08                     add rsp, 8
006B90F5  E8 EE FF FF FF                  call 0x1406b90e8
006B90FA  48 83 C4 08                     add rsp, 8
006B90FE  E8 EE FF FF FF                  call 0x1406b90f1
006B9103  48 83 C4 08                     add rsp, 8
006B9107  E8 EE FF FF FF                  call 0x1406b90fa
006B910C  48 83 C4 08                     add rsp, 8
006B9110  E8 EE FF FF FF                  call 0x1406b9103
006B9115  48 83 C4 08                     add rsp, 8
006B9119  E8 EE FF FF FF                  call 0x1406b910c
006B911E  48 83 C4 08                     add rsp, 8
006B9122  E8 EE FF FF FF                  call 0x1406b9115
006B9127  48 83 C4 08                     add rsp, 8
006B912B  E8 EE FF FF FF                  call 0x1406b911e
006B9130  48 83 C4 08                     add rsp, 8
006B9134  E8 EE FF FF FF                  call 0x1406b9127
006B9139  48 83 C4 08                     add rsp, 8
006B913D  E8 EE FF FF FF                  call 0x1406b9130
006B9142  48 83 C4 08                     add rsp, 8
006B9146  E8 EE FF FF FF                  call 0x1406b9139
006B914B  48 83 C4 08                     add rsp, 8
006B914F  E8 EE FF FF FF                  call 0x1406b9142
006B9154  48 83 C4 08                     add rsp, 8
006B9158  E8 EE FF FF FF                  call 0x1406b914b
006B915D  48 83 C4 08                     add rsp, 8
006B9161  E8 EE FF FF FF                  call 0x1406b9154
006B9166  48 83 C4 08                     add rsp, 8
006B916A  E8 EE FF FF FF                  call 0x1406b915d
006B916F  48 83 C4 08                     add rsp, 8
006B9173  E8 EE FF FF FF                  call 0x1406b9166
006B9178  48 83 C4 08                     add rsp, 8
006B917C  E8 EE FF FF FF                  call 0x1406b916f
006B9181  48 83 C4 08                     add rsp, 8
006B9185  E8 EE FF FF FF                  call 0x1406b9178
006B918A  48 83 C4 08                     add rsp, 8
006B918E  E8 EE FF FF FF                  call 0x1406b9181
006B9193  48 83 C4 08                     add rsp, 8
006B9197  B8 DA DA 00 00                  mov eax, 0xdada
006B919C  65 F6 04 25 5C 08 00 00 08      test byte ptr gs:[0x85c], 8
006B91A5  74 07                           je 0x1406b91ae
006B91A7  B0 20                           mov al, 0x20
006B91A9  F3 48 0F AE E8                  incsspq rax
006B91AE  F7 C2 80 00 00 00               test edx, 0x80
006B91B4  74 08                           je 0x1406b91be
006B91B6  0F AE E8                        lfence
006B91B9  E8 82 D1 00 00                  call 0x1406c6340
006B91BE  0F AE E8                        lfence
006B91C1  65 C6 04 25 5E 08 00 00 00      mov byte ptr gs:[0x85e], 0
006B91CA  83 3D 93 E0 90 00 00            cmp dword ptr [rip + 0x90e093], 0
006B91D1  74 1F                           je 0x1406b91f2
006B91D3  B9 A7 06 00 00                  mov ecx, 0x6a7
006B91D8  0F 32                           rdmsr
006B91DA  83 FA 00                        cmp edx, 0
006B91DD  74 13                           je 0x1406b91f2
006B91DF  8B CA                           mov ecx, edx
006B91E1  23 15 7D E0 90 00               and edx, dword ptr [rip + 0x90e07d]
006B91E7  3B D1                           cmp edx, ecx
006B91E9  74 07                           je 0x1406b91f2
006B91EB  B9 A7 06 00 00                  mov ecx, 0x6a7
006B91F0  0F 30                           wrmsr
006B91F2  41 F6 42 03 03                  test byte ptr [r10 + 3], 3
006B91F7  66 C7 85 80 00 00 00 00 00      mov word ptr [rbp + 0x80], 0
006B9200  74 05                           je 0x1406b9207
006B9202  E8 59 47 E4 FF                  call 0x1404fd960
006B9207  FC                              cld
006B9208  0F AE 5D AC                     stmxcsr dword ptr [rbp - 0x54]
006B920C  65 0F AE 14 25 80 01 00 00      ldmxcsr dword ptr gs:[0x180]
006B9215  0F 29 45 F0                     movaps xmmword ptr [rbp - 0x10], xmm0
006B9219  0F 29 4D 00                     movaps xmmword ptr [rbp], xmm1
006B921D  0F 29 55 10                     movaps xmmword ptr [rbp + 0x10], xmm2
006B9221  0F 29 5D 20                     movaps xmmword ptr [rbp + 0x20], xmm3
006B9225  0F 29 65 30                     movaps xmmword ptr [rbp + 0x30], xmm4
006B9229  0F 29 6D 40                     movaps xmmword ptr [rbp + 0x40], xmm5
006B922D  F6 85 F0 00 00 00 01            test byte ptr [rbp + 0xf0], 1
006B9234  74 05                           je 0x1406b923b
006B9236  E8 65 2D D6 FF                  call 0x14041bfa0
006B923B  65 80 3C 25 DA 87 00 00 00      cmp byte ptr gs:[0x87da], 0
006B9244  74 05                           je 0x1406b924b
006B9246  E8 35 4E F0 FF                  call 0x1405be080
006B924B  48 8D 05 25 13 00 00            lea rax, [rip + 0x1325]
006B9252  48 3B 85 E8 00 00 00            cmp rax, qword ptr [rbp + 0xe8]
006B9259  73 19                           jae 0x1406b9274
006B925B  48 8D 05 2E 13 00 00            lea rax, [rip + 0x132e]
006B9262  48 3B 85 E8 00 00 00            cmp rax, qword ptr [rbp + 0xe8]
006B9269  72 09                           jb 0x1406b9274
006B926B  48 8D 4D 80                     lea rcx, [rbp - 0x80]
006B926F  E8 9C 25 D5 FF                  call 0x14040b810
006B9274  33 F6                           xor esi, esi
006B9276  65 FF 04 25 C0 87 00 00         inc dword ptr gs:[0x87c0]
006B927E  65 48 8B 0C 25 58 91 00 00      mov rcx, qword ptr gs:[0x9158]
006B9287  48 8B C1                        mov rax, rcx
006B928A  8B 15 CC BD 90 00               mov edx, dword ptr [rip + 0x90bdcc]
006B9290  48 2B C2                        sub rax, rdx
006B9293  48 8B D4                        mov rdx, rsp
006B9296  48 3B C4                        cmp rax, rsp
006B9299  77 05                           ja 0x1406b92a0
006B929B  48 3B E1                        cmp rsp, rcx
006B929E  72 0C                           jb 0x1406b92ac
006B92A0  83 3D A5 E2 88 00 00            cmp dword ptr [rip + 0x88e2a5], 0
006B92A7  75 03                           jne 0x1406b92ac
006B92A9  48 8B E1                        mov rsp, rcx
006B92AC  48 83 EC 20                     sub rsp, 0x20
006B92B0  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
006B92B5  E8 A6 03 00 00                  call 0x1406b9660
006B92BA  48 8B 64 24 10                  mov rsp, qword ptr [rsp + 0x10]
006B92BF  48 8B CE                        mov rcx, rsi
006B92C2  E8 59 FB D5 FF                  call 0x140418e20
006B92C7  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
006B92D0  0F B6 55 A9                     movzx edx, byte ptr [rbp - 0x57]
006B92D4  E8 07 18 D4 FF                  call 0x1403faae0
006B92D9  84 C0                           test al, al
006B92DB  74 05                           je 0x1406b92e2
006B92DD  E8 FE FB FF FF                  call 0x1406b8ee0
006B92E2  0F B6 4D A9                     movzx ecx, byte ptr [rbp - 0x57]
006B92E6  83 3D 33 DA 90 00 00            cmp dword ptr [rip + 0x90da33], 0
006B92ED  74 07                           je 0x1406b92f6
006B92EF  E8 EC F7 EF FF                  call 0x1405b8ae0
006B92F4  EB 04                           jmp 0x1406b92fa
006B92F6  44 0F 22 C1                     mov cr8, rcx
006B92FA  48 8B B5 D0 00 00 00            mov rsi, qword ptr [rbp + 0xd0]
006B9301  F6 85 F0 00 00 00 01            test byte ptr [rbp + 0xf0], 1
006B9308  0F 84 F5 02 00 00               je 0x1406b9603
006B930E  F6 05 DB D8 90 00 FF            test byte ptr [rip + 0x90d8db], 0xff
006B9315  74 03                           je 0x1406b931a
006B9317  0F 01 CB                        stac
006B931A  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006B9323  F6 81 C2 00 00 00 03            test byte ptr [rcx + 0xc2], 3
006B932A  74 1B                           je 0x1406b9347
006B932C  B9 01 00 00 00                  mov ecx, 1
006B9331  44 0F 22 C1                     mov cr8, rcx
006B9335  FB                              sti
006B9336  E8 05 D2 FF FF                  call 0x1406b6540
006B933B  FA                              cli
006B933C  B9 00 00 00 00                  mov ecx, 0
006B9341  44 0F 22 C1                     mov cr8, rcx
006B9345  EB D3                           jmp 0x1406b931a
006B9347  E8 14 AC BA FF                  call 0x140263f60
006B934C  85 C0                           test eax, eax
006B934E  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
006B9352  75 C6                           jne 0x1406b931a
006B9354  65 F6 04 25 60 08 00 00 02      test byte ptr gs:[0x860], 2
006B935D  74 07                           je 0x1406b9366
006B935F  33 C9                           xor ecx, ecx
006B9361  E8 5A DE D2 FF                  call 0x1403e71c0
006B9366  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006B936F  F7 01 00 00 00 08               test dword ptr [rcx], 0x8000000
006B9375  74 05                           je 0x1406b937c
006B9377  E8 24 89 FF FF                  call 0x1406b1ca0
006B937C  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006B9385  F7 01 00 00 01 00               test dword ptr [rcx], 0x10000
006B938B  74 14                           je 0x1406b93a1
006B938D  F6 41 02 01                     test byte ptr [rcx + 2], 1
006B9391  74 0E                           je 0x1406b93a1
006B9393  E8 78 73 F0 FF                  call 0x1405c0710
006B9398  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006B93A1  0F AE 55 AC                     ldmxcsr dword ptr [rbp - 0x54]
006B93A5  66 83 BD 80 00 00 00 00         cmp word ptr [rbp + 0x80], 0
006B93AD  74 05                           je 0x1406b93b4
006B93AF  E8 2C 45 E4 FF                  call 0x1404fd8e0
006B93B4  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006B93BD  0F BA 61 74 16                  bt dword ptr [rcx + 0x74], 0x16
006B93C2  73 2A                           jae 0x1406b93ee
006B93C4  33 C9                           xor ecx, ecx
006B93C6  F3 48 0F 1E C9                  rdsspq rcx
006B93CB  65 4C 8B 04 25 28 9D 00 00      mov r8, qword ptr gs:[0x9d28]
006B93D4  49 83 C0 08                     add r8, 8
006B93D8  49 3B C8                        cmp rcx, r8
006B93DB  75 11                           jne 0x1406b93ee
006B93DD  65 48 8B 0C 25 20 9D 00 00      mov rcx, qword ptr gs:[0x9d20]
006B93E6  F3 0F 01 29                     rstorssp dword ptr [rcx]
006B93EA  F3 0F 01 EA                     saveprevssp
006B93EE  65 C6 04 25 5E 08 00 00 00      mov byte ptr gs:[0x85e], 0
006B93F7  65 0F B7 04 25 6C 08 00 00      movzx eax, word ptr gs:[0x86c]
006B9400  66 65 39 04 25 66 08 00 00      cmp word ptr gs:[0x866], ax
006B9409  74 12                           je 0x1406b941d
006B940B  66 65 89 04 25 66 08 00 00      mov word ptr gs:[0x866], ax
006B9414  B9 48 00 00 00                  mov ecx, 0x48
006B9419  33 D2                           xor edx, edx
006B941B  0F 30                           wrmsr
006B941D  66 65 0F BA 34 25 58 08 00 00 02  btr word ptr gs:[0x858], 2
006B9428  73 0E                           jae 0x1406b9438
006B942A  B8 01 00 00 00                  mov eax, 1
006B942F  33 D2                           xor edx, edx
006B9431  B9 49 00 00 00                  mov ecx, 0x49
006B9436  0F 30                           wrmsr
006B9438  66 65 0F BA 34 25 58 08 00 00 05  btr word ptr gs:[0x858], 5
006B9443  0F 83 37 01 00 00               jae 0x1406b9580
006B9449  E8 0E 01 00 00                  call 0x1406b955c
006B944E  48 83 C4 08                     add rsp, 8
006B9452  E8 0E 01 00 00                  call 0x1406b9565
006B9457  48 83 C4 08                     add rsp, 8
006B945B  E8 EE FF FF FF                  call 0x1406b944e
006B9460  48 83 C4 08                     add rsp, 8
006B9464  E8 EE FF FF FF                  call 0x1406b9457
006B9469  48 83 C4 08                     add rsp, 8
006B946D  E8 EE FF FF FF                  call 0x1406b9460
006B9472  48 83 C4 08                     add rsp, 8
006B9476  E8 EE FF FF FF                  call 0x1406b9469
006B947B  48 83 C4 08                     add rsp, 8
006B947F  E8 EE FF FF FF                  call 0x1406b9472
006B9484  48 83 C4 08                     add rsp, 8
006B9488  E8 EE FF FF FF                  call 0x1406b947b
006B948D  48 83 C4 08                     add rsp, 8
006B9491  E8 EE FF FF FF                  call 0x1406b9484
006B9496  48 83 C4 08                     add rsp, 8
006B949A  E8 EE FF FF FF                  call 0x1406b948d
006B949F  48 83 C4 08                     add rsp, 8
006B94A3  E8 EE FF FF FF                  call 0x1406b9496
006B94A8  48 83 C4 08                     add rsp, 8
006B94AC  E8 EE FF FF FF                  call 0x1406b949f
006B94B1  48 83 C4 08                     add rsp, 8
006B94B5  E8 EE FF FF FF                  call 0x1406b94a8
006B94BA  48 83 C4 08                     add rsp, 8
006B94BE  E8 EE FF FF FF                  call 0x1406b94b1
006B94C3  48 83 C4 08                     add rsp, 8
006B94C7  E8 EE FF FF FF                  call 0x1406b94ba
006B94CC  48 83 C4 08                     add rsp, 8
006B94D0  E8 EE FF FF FF                  call 0x1406b94c3
006B94D5  48 83 C4 08                     add rsp, 8
006B94D9  E8 EE FF FF FF                  call 0x1406b94cc
006B94DE  48 83 C4 08                     add rsp, 8
006B94E2  E8 EE FF FF FF                  call 0x1406b94d5
006B94E7  48 83 C4 08                     add rsp, 8
006B94EB  E8 EE FF FF FF                  call 0x1406b94de
006B94F0  48 83 C4 08                     add rsp, 8
006B94F4  E8 EE FF FF FF                  call 0x1406b94e7
006B94F9  48 83 C4 08                     add rsp, 8
006B94FD  E8 EE FF FF FF                  call 0x1406b94f0
006B9502  48 83 C4 08                     add rsp, 8
006B9506  E8 EE FF FF FF                  call 0x1406b94f9
006B950B  48 83 C4 08                     add rsp, 8
006B950F  E8 EE FF FF FF                  call 0x1406b9502
006B9514  48 83 C4 08                     add rsp, 8
006B9518  E8 EE FF FF FF                  call 0x1406b950b
006B951D  48 83 C4 08                     add rsp, 8
006B9521  E8 EE FF FF FF                  call 0x1406b9514
006B9526  48 83 C4 08                     add rsp, 8
006B952A  E8 EE FF FF FF                  call 0x1406b951d
006B952F  48 83 C4 08                     add rsp, 8
006B9533  E8 EE FF FF FF                  call 0x1406b9526
006B9538  48 83 C4 08                     add rsp, 8
006B953C  E8 EE FF FF FF                  call 0x1406b952f
006B9541  48 83 C4 08                     add rsp, 8
006B9545  E8 EE FF FF FF                  call 0x1406b9538
006B954A  48 83 C4 08                     add rsp, 8
006B954E  E8 EE FF FF FF                  call 0x1406b9541
006B9553  48 83 C4 08                     add rsp, 8
006B9557  E8 EE FF FF FF                  call 0x1406b954a
006B955C  48 83 C4 08                     add rsp, 8
006B9560  E8 EE FF FF FF                  call 0x1406b9553
006B9565  48 83 C4 08                     add rsp, 8
006B9569  B8 DA DA 00 00                  mov eax, 0xdada
006B956E  65 F6 04 25 5C 08 00 00 08      test byte ptr gs:[0x85c], 8
006B9577  74 07                           je 0x1406b9580
006B9579  B0 20                           mov al, 0x20
006B957B  F3 48 0F AE E8                  incsspq rax
006B9580  66 65 F7 04 25 58 08 00 00 00 01  test word ptr gs:[0x858], 0x100
006B958B  74 0C                           je 0x1406b9599
006B958D  33 C0                           xor eax, eax
006B958F  33 D2                           xor edx, edx
006B9591  B9 01 00 00 00                  mov ecx, 1
006B9596  48 F7 F1                        div rcx
006B9599  0F 28 45 F0                     movaps xmm0, xmmword ptr [rbp - 0x10]
006B959D  0F 28 4D 00                     movaps xmm1, xmmword ptr [rbp]
006B95A1  0F 28 55 10                     movaps xmm2, xmmword ptr [rbp + 0x10]
006B95A5  0F 28 5D 20                     movaps xmm3, xmmword ptr [rbp + 0x20]
006B95A9  0F 28 65 30                     movaps xmm4, xmmword ptr [rbp + 0x30]
006B95AD  0F 28 6D 40                     movaps xmm5, xmmword ptr [rbp + 0x40]
006B95B1  4C 8B 5D E0                     mov r11, qword ptr [rbp - 0x20]
006B95B5  4C 8B 55 D8                     mov r10, qword ptr [rbp - 0x28]
006B95B9  4C 8B 4D D0                     mov r9, qword ptr [rbp - 0x30]
006B95BD  4C 8B 45 C8                     mov r8, qword ptr [rbp - 0x38]
006B95C1  48 8B 55 C0                     mov rdx, qword ptr [rbp - 0x40]
006B95C5  48 8B 4D B8                     mov rcx, qword ptr [rbp - 0x48]
006B95C9  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
006B95CD  48 8B E5                        mov rsp, rbp
006B95D0  48 8B AD D8 00 00 00            mov rbp, qword ptr [rbp + 0xd8]
006B95D7  48 81 C4 E8 00 00 00            add rsp, 0xe8
006B95DE  F6 05 5B 82 B4 00 01            test byte ptr [rip + 0xb4825b], 1
006B95E5  74 05                           je 0x1406b95ec
006B95E7  E9 94 35 51 00                  jmp 0x140bccb80
006B95EC  66 65 F7 04 25 58 08 00 00 00 02  test word ptr gs:[0x858], 0x200
006B95F7  74 05                           je 0x1406b95fe
006B95F9  0F 00 6C 24 20                  verw word ptr [rsp + 0x20]
006B95FE  0F 01 F8                        swapgs
006B9601  48 CF                           iretq
006B9603  0F AE 55 AC                     ldmxcsr dword ptr [rbp - 0x54]
006B9607  0F 28 45 F0                     movaps xmm0, xmmword ptr [rbp - 0x10]
006B960B  0F 28 4D 00                     movaps xmm1, xmmword ptr [rbp]
006B960F  0F 28 55 10                     movaps xmm2, xmmword ptr [rbp + 0x10]
006B9613  0F 28 5D 20                     movaps xmm3, xmmword ptr [rbp + 0x20]
006B9617  0F 28 65 30                     movaps xmm4, xmmword ptr [rbp + 0x30]
006B961B  0F 28 6D 40                     movaps xmm5, xmmword ptr [rbp + 0x40]
006B961F  4C 8B 5D E0                     mov r11, qword ptr [rbp - 0x20]
006B9623  4C 8B 55 D8                     mov r10, qword ptr [rbp - 0x28]
006B9627  4C 8B 4D D0                     mov r9, qword ptr [rbp - 0x30]
006B962B  4C 8B 45 C8                     mov r8, qword ptr [rbp - 0x38]
006B962F  48 8B 55 C0                     mov rdx, qword ptr [rbp - 0x40]
006B9633  48 8B 4D B8                     mov rcx, qword ptr [rbp - 0x48]
006B9637  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
006B963B  48 8B E5                        mov rsp, rbp
006B963E  48 8B AD D8 00 00 00            mov rbp, qword ptr [rbp + 0xd8]
006B9645  48 81 C4 E8 00 00 00            add rsp, 0xe8
006B964C  48 CF                           iretq
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiIpiInterrupt(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_rsi;
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
    unsigned __int8 v_stack_m13F;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m18;
    unsigned __int16 v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p0;
    unsigned __int16 v_stack_p20;
    unsigned __int8 v_stack_p8;

    v_rsp = (v_rsp) - (8);
    v_rsp = (v_rsp) - (336);
    v_stack_m13D = 0;
    v_stack_m138 = result;
    v_stack_m130 = a1;
    v_stack_m128 = a2;
    v_stack_m120 = a3;
    v_stack_m118 = a4;
    v_stack_m110 = v_r10;
    v_stack_m108 = v_r11;
    if (((v_stack_p8) & (1)) != 0) goto loc_006B8F96;
    a2 = 0;
    v_stack_m90 = 0;
    if (((*(unsigned __int8 *)(gs_base + (0 + 2136))) & (1)) != 0) goto loc_006B8F7F;
    goto loc_006B9207;
loc_006B8F7F:
    a2 = 0;
    goto loc_006B9207;
loc_006B8F96:
    if (((*(unsigned __int8 *)(v_rip + 11831459)) & (1)) == 0) {
    }
    if (*(unsigned __int64 *)(gs_base + (0 + 40232)) == 0) goto loc_006B8FD2;
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
    if ((((unsigned int)(a2)) & (2)) == 0) goto loc_006B91AE;
    result = KiIpiInterrupt___0x26A(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiIpiInterrupt___0x273(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiIpiInterrupt___0x15C(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiIpiInterrupt___0x165(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiIpiInterrupt___0x16E(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiIpiInterrupt___0x177(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiIpiInterrupt___0x180(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiIpiInterrupt___0x189(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiIpiInterrupt___0x192(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiIpiInterrupt___0x19B(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiIpiInterrupt___0x1A4(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiIpiInterrupt___0x1AD(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiIpiInterrupt___0x1B6(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiIpiInterrupt___0x1BF(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiIpiInterrupt___0x1C8(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiIpiInterrupt___0x1D1(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiIpiInterrupt___0x1DA(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiIpiInterrupt___0x1E3(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiIpiInterrupt___0x1EC(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiIpiInterrupt___0x1F5(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiIpiInterrupt___0x1FE(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiIpiInterrupt___0x207(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiIpiInterrupt___0x210(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiIpiInterrupt___0x219(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiIpiInterrupt___0x222(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiIpiInterrupt___0x22B(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiIpiInterrupt___0x234(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiIpiInterrupt___0x23D(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiIpiInterrupt___0x246(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiIpiInterrupt___0x24F(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiIpiInterrupt___0x258(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiIpiInterrupt___0x261(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = (unsigned int)(0xDADAULL);
    if (((*(unsigned __int8 *)(gs_base + (0 + 2140))) & (8)) != 0) {
        result = 32;
    }
    if ((((unsigned int)(a2)) & (128)) != 0) {
        result = KiFlushBhbDuringTrapEntryOrExit(a1, a2, a3, a4);
    }
    *(unsigned __int8 *)(gs_base + (0 + 2142)) = 0;
    if ((*(unsigned int *)(v_rip + 9494675)) == 0) goto loc_006B91F2;
    if (((unsigned int)(a2)) == 0) goto loc_006B91F2;
    a2 = (unsigned int)((a2) & (*(unsigned int *)(v_rip + 9494653)));
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
    if ((*(unsigned __int8 *)(gs_base + (0 + 34778))) != 0) {
        result = KeWakeProcessor(a1, a2, a3, a4);
    }
    if ((v_rip + 4901) >= v_stack_p0) goto loc_006B9274;
    result = v_rip + 4910;
    if ((v_rip + 4910) >= v_stack_p0) {
        a1 = v_stack_m168;
        result = KiCheckForSListAddress(a1, a2, a3, a4);
    }
    v_rsi = 0;
    result = (*(unsigned __int64 *)(gs_base + (0 + 37208))) - ((unsigned int)(*(unsigned int *)(v_rip + 9485772)));
    if (result > v_rsp) goto loc_006B92A0;
    if (v_rsp < (*(unsigned __int64 *)(gs_base + (0 + 37208)))) goto loc_006B92AC;
loc_006B92A0:
    if ((*(unsigned int *)(v_rip + 8970917)) == 0) {
        v_rsp = *(unsigned __int64 *)(gs_base + (0 + 37208));
    }
    v_rsp = (v_rsp) - (32);
    v_stack_m78 = v_rsp;
    result = KiIpiInterruptSubDispatch(*(unsigned __int64 *)(gs_base + (0 + 37208)), v_rsp, a3, a4);
    result = HalPerformEndOfInterrupt(0, v_rsp, a3, a4);
    result = KiEndInterruptCycleAccumulation(*(unsigned __int64 *)(gs_base + (0 + 32)), v_stack_m13F, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        result = KiDpcInterruptBypass(*(unsigned __int64 *)(gs_base + (0 + 32)), v_stack_m13F, a3, a4);
    }
    if ((*(unsigned int *)(v_rip + 9493043)) == 0) goto loc_006B92F6;
    result = KzSetIrqlUnsafe(v_stack_m13F, v_stack_m13F, a3, a4);
    goto loc_006B92FA;
loc_006B92F6:
loc_006B92FA:
    if (((v_stack_p8) & (1)) == 0) goto loc_006B9603;
    if (((*(unsigned __int8 *)(v_rip + 9492699)) & (255)) != 0) {
    }
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 194)) & (3)) == 0) goto loc_006B9347;
    result = KiInitiateUserApc(1, v_stack_m13F, a3, a4);
    goto loc_006B931A;
loc_006B9347:
    result = KiSynchronizeUserIsolationDomainEntry(0, v_stack_m13F, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_006B931A;
    result = v_stack_m138;
    if (((*(unsigned __int8 *)(gs_base + (0 + 2144))) & (2)) != 0) {
        a1 = 0;
        result = KiUpdateStibpPairing(a1, v_stack_m13F, a3, a4);
    }
    if (((*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)))) & (0x8000000ULL)) != 0) {
        result = KiRestoreSetContextState(*(unsigned __int64 *)(gs_base + (0 + 392)), v_stack_m13F, a3, a4);
    }
    if (((*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)))) & (0x10000ULL)) == 0) goto loc_006B93A1;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 2)) & (1)) != 0) {
        result = KiCopyCounters(*(unsigned __int64 *)(gs_base + (0 + 392)), v_stack_m13F, a3, a4);
        a1 = *(unsigned __int64 *)(gs_base + (0 + 392));
    }
    if (v_stack_m68 != 0) {
        result = KiRestoreDebugRegisterState(a1, v_stack_m13F, a3, a4);
    }
    if (v_stack_m68 >= 0) goto loc_006B93EE;
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
    if (condition_is_above_or_equal) goto loc_006B9580;
    result = KiIpiInterrupt___0x63C(a1, a2, a3, a4);
    v_rsp = (v_stack_m78) + (8);
    result = KiIpiInterrupt___0x645(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiIpiInterrupt___0x52E(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiIpiInterrupt___0x537(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiIpiInterrupt___0x540(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiIpiInterrupt___0x549(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiIpiInterrupt___0x552(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiIpiInterrupt___0x55B(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiIpiInterrupt___0x564(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiIpiInterrupt___0x56D(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiIpiInterrupt___0x576(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiIpiInterrupt___0x57F(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiIpiInterrupt___0x588(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiIpiInterrupt___0x591(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiIpiInterrupt___0x59A(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiIpiInterrupt___0x5A3(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiIpiInterrupt___0x5AC(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiIpiInterrupt___0x5B5(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiIpiInterrupt___0x5BE(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiIpiInterrupt___0x5C7(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiIpiInterrupt___0x5D0(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiIpiInterrupt___0x5D9(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiIpiInterrupt___0x5E2(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiIpiInterrupt___0x5EB(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiIpiInterrupt___0x5F4(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiIpiInterrupt___0x5FD(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiIpiInterrupt___0x606(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiIpiInterrupt___0x60F(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiIpiInterrupt___0x618(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiIpiInterrupt___0x621(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiIpiInterrupt___0x62A(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiIpiInterrupt___0x633(a1, a2, a3, a4);
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
    if (((*(unsigned __int8 *)(v_rip + 11829851)) & (1)) == 0) goto loc_006B95EC;
loc_006B95EC:
    if (((*(unsigned __int16 *)(gs_base + (0 + 2136))) & (512)) != 0) {
    }
loc_006B9603:
    v_rsp = (v_stack_m10) + (232);
    return v_stack_m138;
}
```

## 5. (Beta) C Style

```c
int64_t KiIpiInterrupt(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_rsi;
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
    uint8_t v_stack_m13F;
    uint64_t v_stack_m168;
    uint64_t v_stack_m18;
    uint16_t v_stack_m68;
    uint64_t v_stack_m78;
    uint64_t v_stack_m90;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p0;
    uint16_t v_stack_p20;
    uint8_t v_stack_p8;

    local_rsp = (local_rsp) - (8);
    local_rsp = (local_rsp) - (336);
    v_stack_m13D = 0;
    v_stack_m138 = result;
    v_stack_m130 = Arg1;
    v_stack_m128 = Arg2;
    v_stack_m120 = Arg3;
    v_stack_m118 = Arg4;
    v_stack_m110 = local_r10;
    v_stack_m108 = local_r11;
    if (((v_stack_p8) & (1)) != 0) goto loc_006B8F96;
    Arg2 = 0;
    v_stack_m90 = 0;
    if (((*(uint8_t *)(gs_base + (0 + 0x858))) & (1)) != 0) goto loc_006B8F7F;
    goto loc_006B9207;
loc_006B8F7F:
    Arg2 = 0;
    goto loc_006B9207;
loc_006B8F96:
    if (((*(uint8_t *)(v_rip + 0xB488A3)) & (1)) == 0) {
    }
    if (*(uint64_t *)(gs_base + (0 + 0x9D28)) == 0) goto loc_006B8FD2;
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
    if ((((uint32_t)(Arg2)) & (2)) == 0) goto loc_006B91AE;
    result = KiIpiInterrupt___0x26A(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiIpiInterrupt___0x273(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiIpiInterrupt___0x15C(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiIpiInterrupt___0x165(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiIpiInterrupt___0x16E(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiIpiInterrupt___0x177(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiIpiInterrupt___0x180(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiIpiInterrupt___0x189(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiIpiInterrupt___0x192(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiIpiInterrupt___0x19B(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiIpiInterrupt___0x1A4(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiIpiInterrupt___0x1AD(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiIpiInterrupt___0x1B6(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiIpiInterrupt___0x1BF(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiIpiInterrupt___0x1C8(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiIpiInterrupt___0x1D1(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiIpiInterrupt___0x1DA(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiIpiInterrupt___0x1E3(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiIpiInterrupt___0x1EC(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiIpiInterrupt___0x1F5(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiIpiInterrupt___0x1FE(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiIpiInterrupt___0x207(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiIpiInterrupt___0x210(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiIpiInterrupt___0x219(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiIpiInterrupt___0x222(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiIpiInterrupt___0x22B(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiIpiInterrupt___0x234(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiIpiInterrupt___0x23D(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiIpiInterrupt___0x246(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiIpiInterrupt___0x24F(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiIpiInterrupt___0x258(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiIpiInterrupt___0x261(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = (uint32_t)(0xDADAULL);
    if (((*(uint8_t *)(gs_base + (0 + 0x85C))) & (8)) != 0) {
        result = 32;
    }
    if ((((uint32_t)(Arg2)) & (128)) != 0) {
        result = KiFlushBhbDuringTrapEntryOrExit(Arg1, Arg2, Arg3, Arg4);
    }
    *(uint8_t *)(gs_base + (0 + 0x85E)) = 0;
    if ((*(uint32_t *)(v_rip + 0x90E093)) == 0) goto loc_006B91F2;
    if (((uint32_t)(Arg2)) == 0) goto loc_006B91F2;
    Arg2 = (uint32_t)((Arg2) & (*(uint32_t *)(v_rip + 0x90E07D)));
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
    if ((*(uint8_t *)(gs_base + (0 + 0x87DA))) != 0) {
        result = KeWakeProcessor(Arg1, Arg2, Arg3, Arg4);
    }
    if ((v_rip + 4901) >= v_stack_p0) goto loc_006B9274;
    result = v_rip + 4910;
    if ((v_rip + 4910) >= v_stack_p0) {
        Arg1 = v_stack_m168;
        result = KiCheckForSListAddress(Arg1, Arg2, Arg3, Arg4);
    }
    local_rsi = 0;
    result = (*(uint64_t *)(gs_base + (0 + 0x9158))) - ((uint32_t)(*(uint32_t *)(v_rip + 0x90BDCC)));
    if (result > local_rsp) goto loc_006B92A0;
    if (local_rsp < (*(uint64_t *)(gs_base + (0 + 0x9158)))) goto loc_006B92AC;
loc_006B92A0:
    if ((*(uint32_t *)(v_rip + 0x88E2A5)) == 0) {
        local_rsp = *(uint64_t *)(gs_base + (0 + 0x9158));
    }
    local_rsp = (local_rsp) - (32);
    v_stack_m78 = local_rsp;
    result = KiIpiInterruptSubDispatch(*(uint64_t *)(gs_base + (0 + 0x9158)), local_rsp, Arg3, Arg4);
    result = HalPerformEndOfInterrupt(0, local_rsp, Arg3, Arg4);
    result = KiEndInterruptCycleAccumulation(*(uint64_t *)(gs_base + (0 + 0x20)), v_stack_m13F, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        result = KiDpcInterruptBypass(*(uint64_t *)(gs_base + (0 + 0x20)), v_stack_m13F, Arg3, Arg4);
    }
    if ((*(uint32_t *)(v_rip + 0x90DA33)) == 0) goto loc_006B92F6;
    result = KzSetIrqlUnsafe(v_stack_m13F, v_stack_m13F, Arg3, Arg4);
    goto loc_006B92FA;
loc_006B92F6:
loc_006B92FA:
    if (((v_stack_p8) & (1)) == 0) goto loc_006B9603;
    if (((*(uint8_t *)(v_rip + 0x90D8DB)) & (255)) != 0) {
    }
    if (((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xC2)) & (3)) == 0) goto loc_006B9347;
    result = KiInitiateUserApc(1, v_stack_m13F, Arg3, Arg4);
    goto loc_006B931A;
loc_006B9347:
    result = KiSynchronizeUserIsolationDomainEntry(0, v_stack_m13F, Arg3, Arg4);
    if ((uint32_t)(result) != 0) goto loc_006B931A;
    result = v_stack_m138;
    if (((*(uint8_t *)(gs_base + (0 + 0x860))) & (2)) != 0) {
        Arg1 = 0;
        result = KiUpdateStibpPairing(Arg1, v_stack_m13F, Arg3, Arg4);
    }
    if (((*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)))) & (0x8000000ULL)) != 0) {
        result = KiRestoreSetContextState(*(uint64_t *)(gs_base + (0 + 0x188)), v_stack_m13F, Arg3, Arg4);
    }
    if (((*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)))) & (0x10000ULL)) == 0) goto loc_006B93A1;
    if (((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x2)) & (1)) != 0) {
        result = KiCopyCounters(*(uint64_t *)(gs_base + (0 + 0x188)), v_stack_m13F, Arg3, Arg4);
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x188));
    }
    if (v_stack_m68 != 0) {
        result = KiRestoreDebugRegisterState(Arg1, v_stack_m13F, Arg3, Arg4);
    }
    if (v_stack_m68 >= 0) goto loc_006B93EE;
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
    if (condition_is_above_or_equal) goto loc_006B9580;
    result = KiIpiInterrupt___0x63C(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (v_stack_m78) + (8);
    result = KiIpiInterrupt___0x645(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiIpiInterrupt___0x52E(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiIpiInterrupt___0x537(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiIpiInterrupt___0x540(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiIpiInterrupt___0x549(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiIpiInterrupt___0x552(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiIpiInterrupt___0x55B(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiIpiInterrupt___0x564(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiIpiInterrupt___0x56D(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiIpiInterrupt___0x576(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiIpiInterrupt___0x57F(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiIpiInterrupt___0x588(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiIpiInterrupt___0x591(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiIpiInterrupt___0x59A(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiIpiInterrupt___0x5A3(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiIpiInterrupt___0x5AC(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiIpiInterrupt___0x5B5(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiIpiInterrupt___0x5BE(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiIpiInterrupt___0x5C7(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiIpiInterrupt___0x5D0(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiIpiInterrupt___0x5D9(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiIpiInterrupt___0x5E2(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiIpiInterrupt___0x5EB(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiIpiInterrupt___0x5F4(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiIpiInterrupt___0x5FD(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiIpiInterrupt___0x606(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiIpiInterrupt___0x60F(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiIpiInterrupt___0x618(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiIpiInterrupt___0x621(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiIpiInterrupt___0x62A(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiIpiInterrupt___0x633(Arg1, Arg2, Arg3, Arg4);
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
    if (((*(uint8_t *)(v_rip + 0xB4825B)) & (1)) == 0) goto loc_006B95EC;
loc_006B95EC:
    if (((*(uint16_t *)(gs_base + (0 + 0x858))) & (512)) != 0) {
    }
loc_006B9603:
    local_rsp = (v_stack_m10) + (232);
    return v_stack_m138;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006B8F20&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
