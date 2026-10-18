# KxIsrLinkage

- RVA: `0x006B5680`–`0x006B5E0C` (길이 `1,932` bytes)
- VA: `0x00000001406B5680`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C2090`
- 디코드: `418`개 명령, `1,932/1,932` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **83**; 고유 호출 대상: **82**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **8**

### Outgoing calls
- `0x006B57D3` → [KxIsrLinkage + 0x266](KxIsrLinkage_function_006B5680.md) (inside-function, `0x006B58E6`)
- `0x006B57DC` → [KxIsrLinkage + 0x26F](KxIsrLinkage_function_006B5680.md) (inside-function, `0x006B58EF`)
- `0x006B57E5` → [KxIsrLinkage + 0x158](KxIsrLinkage_function_006B5680.md) (inside-function, `0x006B57D8`)
- `0x006B57EE` → [KxIsrLinkage + 0x161](KxIsrLinkage_function_006B5680.md) (inside-function, `0x006B57E1`)
- `0x006B57F7` → [KxIsrLinkage + 0x16A](KxIsrLinkage_function_006B5680.md) (inside-function, `0x006B57EA`)
- `0x006B5800` → [KxIsrLinkage + 0x173](KxIsrLinkage_function_006B5680.md) (inside-function, `0x006B57F3`)
- `0x006B5809` → [KxIsrLinkage + 0x17C](KxIsrLinkage_function_006B5680.md) (inside-function, `0x006B57FC`)
- `0x006B5812` → [KxIsrLinkage + 0x185](KxIsrLinkage_function_006B5680.md) (inside-function, `0x006B5805`)
- `0x006B581B` → [KxIsrLinkage + 0x18E](KxIsrLinkage_function_006B5680.md) (inside-function, `0x006B580E`)
- `0x006B5824` → [KxIsrLinkage + 0x197](KxIsrLinkage_function_006B5680.md) (inside-function, `0x006B5817`)
- `0x006B582D` → [KxIsrLinkage + 0x1A0](KxIsrLinkage_function_006B5680.md) (inside-function, `0x006B5820`)
- `0x006B5836` → [KxIsrLinkage + 0x1A9](KxIsrLinkage_function_006B5680.md) (inside-function, `0x006B5829`)
- `0x006B583F` → [KxIsrLinkage + 0x1B2](KxIsrLinkage_function_006B5680.md) (inside-function, `0x006B5832`)
- `0x006B5848` → [KxIsrLinkage + 0x1BB](KxIsrLinkage_function_006B5680.md) (inside-function, `0x006B583B`)
- `0x006B5851` → [KxIsrLinkage + 0x1C4](KxIsrLinkage_function_006B5680.md) (inside-function, `0x006B5844`)
- `0x006B585A` → [KxIsrLinkage + 0x1CD](KxIsrLinkage_function_006B5680.md) (inside-function, `0x006B584D`)
- `0x006B5863` → [KxIsrLinkage + 0x1D6](KxIsrLinkage_function_006B5680.md) (inside-function, `0x006B5856`)
- `0x006B586C` → [KxIsrLinkage + 0x1DF](KxIsrLinkage_function_006B5680.md) (inside-function, `0x006B585F`)
- `0x006B5875` → [KxIsrLinkage + 0x1E8](KxIsrLinkage_function_006B5680.md) (inside-function, `0x006B5868`)
- `0x006B587E` → [KxIsrLinkage + 0x1F1](KxIsrLinkage_function_006B5680.md) (inside-function, `0x006B5871`)
- `0x006B5887` → [KxIsrLinkage + 0x1FA](KxIsrLinkage_function_006B5680.md) (inside-function, `0x006B587A`)
- `0x006B5890` → [KxIsrLinkage + 0x203](KxIsrLinkage_function_006B5680.md) (inside-function, `0x006B5883`)
- `0x006B5899` → [KxIsrLinkage + 0x20C](KxIsrLinkage_function_006B5680.md) (inside-function, `0x006B588C`)
- `0x006B58A2` → [KxIsrLinkage + 0x215](KxIsrLinkage_function_006B5680.md) (inside-function, `0x006B5895`)
- `0x006B58AB` → [KxIsrLinkage + 0x21E](KxIsrLinkage_function_006B5680.md) (inside-function, `0x006B589E`)
- `0x006B58B4` → [KxIsrLinkage + 0x227](KxIsrLinkage_function_006B5680.md) (inside-function, `0x006B58A7`)
- `0x006B58BD` → [KxIsrLinkage + 0x230](KxIsrLinkage_function_006B5680.md) (inside-function, `0x006B58B0`)
- `0x006B58C6` → [KxIsrLinkage + 0x239](KxIsrLinkage_function_006B5680.md) (inside-function, `0x006B58B9`)
- `0x006B58CF` → [KxIsrLinkage + 0x242](KxIsrLinkage_function_006B5680.md) (inside-function, `0x006B58C2`)
- `0x006B58D8` → [KxIsrLinkage + 0x24B](KxIsrLinkage_function_006B5680.md) (inside-function, `0x006B58CB`)
- `0x006B58E1` → [KxIsrLinkage + 0x254](KxIsrLinkage_function_006B5680.md) (inside-function, `0x006B58D4`)
- `0x006B58EA` → [KxIsrLinkage + 0x25D](KxIsrLinkage_function_006B5680.md) (inside-function, `0x006B58DD`)
- `0x006B5915` → [KiFlushBhbDuringTrapEntryOrExit](../6C/KiFlushBhbDuringTrapEntryOrExit_function_006C6340.md) (function, `0x006C6340`)
- `0x006B595E` → [KiSaveDebugRegisterState](../4F/KiSaveDebugRegisterState_function_004FD960.md) (function, `0x004FD960`)
- `0x006B5992` → [KiSynchronizeUserIsolationDomainExit](../41/KiSynchronizeUserIsolationDomainExit_function_0041BFA0.md) (function, `0x0041BFA0`)
- `0x006B59A2` → [KeWakeProcessor](../5B/KeWakeProcessor_function_005BE080.md) (function, `0x005BE080`)
- `0x006B59CB` → [KiCheckForSListAddress](../40/KiCheckForSListAddress_function_0040B810.md) (function, `0x0040B810`)
- `0x006B5A18` → [KzSetIrqlUnsafe](../5B/KzSetIrqlUnsafe_function_005B8AE0.md) (function, `0x005B8AE0`)
- `0x006B5A35` → [KiStartInterruptCycleAccumulation](../37/KiStartInterruptCycleAccumulation_function_0037B410.md) (function, `0x0037B410`)
- `0x006B5A4E` → [PerfInfoLogUnexpectedInterrupt](../65/PerfInfoLogUnexpectedInterrupt_function_006513E0.md) (function, `0x006513E0`)
- `0x006B5A76` → [KiBugCheckDispatch](../6C/KiBugCheckDispatch_function_006C5880.md) (function, `0x006C5880`)
- `0x006B5A7F` → [HalPerformEndOfInterrupt](../41/HalPerformEndOfInterrupt_function_00418E20.md) (function, `0x00418E20`)
- `0x006B5A91` → [KiEndInterruptCycleAccumulation](../3F/KiEndInterruptCycleAccumulation_function_003FAAE0.md) (function, `0x003FAAE0`)
- `0x006B5A9A` → [KiDpcInterruptBypass](KiDpcInterruptBypass_function_006B8EE0.md) (function, `0x006B8EE0`)
- `0x006B5AAC` → [KzSetIrqlUnsafe](../5B/KzSetIrqlUnsafe_function_005B8AE0.md) (function, `0x005B8AE0`)
- `0x006B5AF4` → [KiInitiateUserApc](KiInitiateUserApc_function_006B6540.md) (function, `0x006B6540`)
- `0x006B5B05` → [KiSynchronizeUserIsolationDomainEntry](../26/KiSynchronizeUserIsolationDomainEntry_function_00263F60.md) (function, `0x00263F60`)
- `0x006B5B1F` → [KiUpdateStibpPairing](../3E/KiUpdateStibpPairing_function_003E71C0.md) (function, `0x003E71C0`)
- `0x006B5B35` → [KiRestoreSetContextState](KiRestoreSetContextState_function_006B1CA0.md) (function, `0x006B1CA0`)
- `0x006B5B51` → [KiCopyCounters](../5C/KiCopyCounters_function_005C0710.md) (function, `0x005C0710`)
- `0x006B5B6D` → [KiRestoreDebugRegisterState](../4F/KiRestoreDebugRegisterState_function_004FD8E0.md) (function, `0x004FD8E0`)
- `0x006B5C07` → [KxIsrLinkage + 0x69A](KxIsrLinkage_function_006B5680.md) (inside-function, `0x006B5D1A`)
- `0x006B5C10` → [KxIsrLinkage + 0x6A3](KxIsrLinkage_function_006B5680.md) (inside-function, `0x006B5D23`)
- `0x006B5C19` → [KxIsrLinkage + 0x58C](KxIsrLinkage_function_006B5680.md) (inside-function, `0x006B5C0C`)
- `0x006B5C22` → [KxIsrLinkage + 0x595](KxIsrLinkage_function_006B5680.md) (inside-function, `0x006B5C15`)
- `0x006B5C2B` → [KxIsrLinkage + 0x59E](KxIsrLinkage_function_006B5680.md) (inside-function, `0x006B5C1E`)
- `0x006B5C34` → [KxIsrLinkage + 0x5A7](KxIsrLinkage_function_006B5680.md) (inside-function, `0x006B5C27`)
- `0x006B5C3D` → [KxIsrLinkage + 0x5B0](KxIsrLinkage_function_006B5680.md) (inside-function, `0x006B5C30`)
- `0x006B5C46` → [KxIsrLinkage + 0x5B9](KxIsrLinkage_function_006B5680.md) (inside-function, `0x006B5C39`)
- `0x006B5C4F` → [KxIsrLinkage + 0x5C2](KxIsrLinkage_function_006B5680.md) (inside-function, `0x006B5C42`)
- `0x006B5C58` → [KxIsrLinkage + 0x5CB](KxIsrLinkage_function_006B5680.md) (inside-function, `0x006B5C4B`)
- `0x006B5C61` → [KxIsrLinkage + 0x5D4](KxIsrLinkage_function_006B5680.md) (inside-function, `0x006B5C54`)
- `0x006B5C6A` → [KxIsrLinkage + 0x5DD](KxIsrLinkage_function_006B5680.md) (inside-function, `0x006B5C5D`)
- `0x006B5C73` → [KxIsrLinkage + 0x5E6](KxIsrLinkage_function_006B5680.md) (inside-function, `0x006B5C66`)
- `0x006B5C7C` → [KxIsrLinkage + 0x5EF](KxIsrLinkage_function_006B5680.md) (inside-function, `0x006B5C6F`)
- `0x006B5C85` → [KxIsrLinkage + 0x5F8](KxIsrLinkage_function_006B5680.md) (inside-function, `0x006B5C78`)
- `0x006B5C8E` → [KxIsrLinkage + 0x601](KxIsrLinkage_function_006B5680.md) (inside-function, `0x006B5C81`)
- `0x006B5C97` → [KxIsrLinkage + 0x60A](KxIsrLinkage_function_006B5680.md) (inside-function, `0x006B5C8A`)
- `0x006B5CA0` → [KxIsrLinkage + 0x613](KxIsrLinkage_function_006B5680.md) (inside-function, `0x006B5C93`)
- `0x006B5CA9` → [KxIsrLinkage + 0x61C](KxIsrLinkage_function_006B5680.md) (inside-function, `0x006B5C9C`)
- `0x006B5CB2` → [KxIsrLinkage + 0x625](KxIsrLinkage_function_006B5680.md) (inside-function, `0x006B5CA5`)
- `0x006B5CBB` → [KxIsrLinkage + 0x62E](KxIsrLinkage_function_006B5680.md) (inside-function, `0x006B5CAE`)
- `0x006B5CC4` → [KxIsrLinkage + 0x637](KxIsrLinkage_function_006B5680.md) (inside-function, `0x006B5CB7`)
- `0x006B5CCD` → [KxIsrLinkage + 0x640](KxIsrLinkage_function_006B5680.md) (inside-function, `0x006B5CC0`)
- `0x006B5CD6` → [KxIsrLinkage + 0x649](KxIsrLinkage_function_006B5680.md) (inside-function, `0x006B5CC9`)
- `0x006B5CDF` → [KxIsrLinkage + 0x652](KxIsrLinkage_function_006B5680.md) (inside-function, `0x006B5CD2`)
- `0x006B5CE8` → [KxIsrLinkage + 0x65B](KxIsrLinkage_function_006B5680.md) (inside-function, `0x006B5CDB`)
- `0x006B5CF1` → [KxIsrLinkage + 0x664](KxIsrLinkage_function_006B5680.md) (inside-function, `0x006B5CE4`)
- `0x006B5CFA` → [KxIsrLinkage + 0x66D](KxIsrLinkage_function_006B5680.md) (inside-function, `0x006B5CED`)
- `0x006B5D03` → [KxIsrLinkage + 0x676](KxIsrLinkage_function_006B5680.md) (inside-function, `0x006B5CF6`)
- `0x006B5D0C` → [KxIsrLinkage + 0x67F](KxIsrLinkage_function_006B5680.md) (inside-function, `0x006B5CFF`)
- `0x006B5D15` → [KxIsrLinkage + 0x688](KxIsrLinkage_function_006B5680.md) (inside-function, `0x006B5D08`)
- `0x006B5D1E` → [KxIsrLinkage + 0x691](KxIsrLinkage_function_006B5680.md) (inside-function, `0x006B5D11`)

### Direct callers
- [KxIsrLinkage](KxIsrLinkage_function_006B5680.md) at `0x006B57D3`
- [KxIsrLinkage](KxIsrLinkage_function_006B5680.md) at `0x006B57DC`
- [KxIsrLinkage](KxIsrLinkage_function_006B5680.md) at `0x006B57E5`
- [KxIsrLinkage](KxIsrLinkage_function_006B5680.md) at `0x006B57EE`
- [KxIsrLinkage](KxIsrLinkage_function_006B5680.md) at `0x006B57F7`
- [KxIsrLinkage](KxIsrLinkage_function_006B5680.md) at `0x006B5800`
- [KxIsrLinkage](KxIsrLinkage_function_006B5680.md) at `0x006B5809`
- [KxIsrLinkage](KxIsrLinkage_function_006B5680.md) at `0x006B5812`
- [KxIsrLinkage](KxIsrLinkage_function_006B5680.md) at `0x006B581B`
- [KxIsrLinkage](KxIsrLinkage_function_006B5680.md) at `0x006B5824`
- [KxIsrLinkage](KxIsrLinkage_function_006B5680.md) at `0x006B582D`
- [KxIsrLinkage](KxIsrLinkage_function_006B5680.md) at `0x006B5836`
- [KxIsrLinkage](KxIsrLinkage_function_006B5680.md) at `0x006B583F`
- [KxIsrLinkage](KxIsrLinkage_function_006B5680.md) at `0x006B5848`
- [KxIsrLinkage](KxIsrLinkage_function_006B5680.md) at `0x006B5851`
- [KxIsrLinkage](KxIsrLinkage_function_006B5680.md) at `0x006B585A`
- [KxIsrLinkage](KxIsrLinkage_function_006B5680.md) at `0x006B5863`
- [KxIsrLinkage](KxIsrLinkage_function_006B5680.md) at `0x006B586C`
- [KxIsrLinkage](KxIsrLinkage_function_006B5680.md) at `0x006B5875`
- [KxIsrLinkage](KxIsrLinkage_function_006B5680.md) at `0x006B587E`
- [KxIsrLinkage](KxIsrLinkage_function_006B5680.md) at `0x006B5887`
- [KxIsrLinkage](KxIsrLinkage_function_006B5680.md) at `0x006B5890`
- [KxIsrLinkage](KxIsrLinkage_function_006B5680.md) at `0x006B5899`
- [KxIsrLinkage](KxIsrLinkage_function_006B5680.md) at `0x006B58A2`
- [KxIsrLinkage](KxIsrLinkage_function_006B5680.md) at `0x006B58AB`
- [KxIsrLinkage](KxIsrLinkage_function_006B5680.md) at `0x006B58B4`
- [KxIsrLinkage](KxIsrLinkage_function_006B5680.md) at `0x006B58BD`
- [KxIsrLinkage](KxIsrLinkage_function_006B5680.md) at `0x006B58C6`
- [KxIsrLinkage](KxIsrLinkage_function_006B5680.md) at `0x006B58CF`
- [KxIsrLinkage](KxIsrLinkage_function_006B5680.md) at `0x006B58D8`
- [KxIsrLinkage](KxIsrLinkage_function_006B5680.md) at `0x006B58E1`
- [KxIsrLinkage](KxIsrLinkage_function_006B5680.md) at `0x006B58EA`
- [KxIsrLinkage](KxIsrLinkage_function_006B5680.md) at `0x006B5C07`
- [KxIsrLinkage](KxIsrLinkage_function_006B5680.md) at `0x006B5C10`
- [KxIsrLinkage](KxIsrLinkage_function_006B5680.md) at `0x006B5C19`
- [KxIsrLinkage](KxIsrLinkage_function_006B5680.md) at `0x006B5C22`
- [KxIsrLinkage](KxIsrLinkage_function_006B5680.md) at `0x006B5C2B`
- [KxIsrLinkage](KxIsrLinkage_function_006B5680.md) at `0x006B5C34`
- [KxIsrLinkage](KxIsrLinkage_function_006B5680.md) at `0x006B5C3D`
- [KxIsrLinkage](KxIsrLinkage_function_006B5680.md) at `0x006B5C46`
- [KxIsrLinkage](KxIsrLinkage_function_006B5680.md) at `0x006B5C4F`
- [KxIsrLinkage](KxIsrLinkage_function_006B5680.md) at `0x006B5C58`
- [KxIsrLinkage](KxIsrLinkage_function_006B5680.md) at `0x006B5C61`
- [KxIsrLinkage](KxIsrLinkage_function_006B5680.md) at `0x006B5C6A`
- [KxIsrLinkage](KxIsrLinkage_function_006B5680.md) at `0x006B5C73`
- [KxIsrLinkage](KxIsrLinkage_function_006B5680.md) at `0x006B5C7C`
- [KxIsrLinkage](KxIsrLinkage_function_006B5680.md) at `0x006B5C85`
- [KxIsrLinkage](KxIsrLinkage_function_006B5680.md) at `0x006B5C8E`
- [KxIsrLinkage](KxIsrLinkage_function_006B5680.md) at `0x006B5C97`
- [KxIsrLinkage](KxIsrLinkage_function_006B5680.md) at `0x006B5CA0`
- [KxIsrLinkage](KxIsrLinkage_function_006B5680.md) at `0x006B5CA9`
- [KxIsrLinkage](KxIsrLinkage_function_006B5680.md) at `0x006B5CB2`
- [KxIsrLinkage](KxIsrLinkage_function_006B5680.md) at `0x006B5CBB`
- [KxIsrLinkage](KxIsrLinkage_function_006B5680.md) at `0x006B5CC4`
- [KxIsrLinkage](KxIsrLinkage_function_006B5680.md) at `0x006B5CCD`
- [KxIsrLinkage](KxIsrLinkage_function_006B5680.md) at `0x006B5CD6`
- [KxIsrLinkage](KxIsrLinkage_function_006B5680.md) at `0x006B5CDF`
- [KxIsrLinkage](KxIsrLinkage_function_006B5680.md) at `0x006B5CE8`
- [KxIsrLinkage](KxIsrLinkage_function_006B5680.md) at `0x006B5CF1`
- [KxIsrLinkage](KxIsrLinkage_function_006B5680.md) at `0x006B5CFA`
- [KxIsrLinkage](KxIsrLinkage_function_006B5680.md) at `0x006B5D03`
- [KxIsrLinkage](KxIsrLinkage_function_006B5680.md) at `0x006B5D0C`
- [KxIsrLinkage](KxIsrLinkage_function_006B5680.md) at `0x006B5D15`
- [KxIsrLinkage](KxIsrLinkage_function_006B5680.md) at `0x006B5D1E`

### Static image references
- `0x006B56F2` → RVA `0x01201840` (`CFGRO`; read)
- `0x006B5926` → RVA `0x00FC7264` (`ALMOSTRO`; read)
- `0x006B59A7` → RVA `0x006BA577` (`ExpInterlockedPopEntrySListResume`; read)
- `0x006B59B7` → RVA `0x006BA590` (`ExpInterlockedPopEntrySListEnd`; read)
- `0x006B59F0` → RVA `0x00FC6BF0` (`ALMOSTRO`; read)
- `0x006B5A0F` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x006B5A3B` → RVA `0x00FC6B04` (`ALMOSTRO`; read)
- `0x006B5A53` → RVA `0x00E668FC` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x006B5A05` → [guard_dispatch_icall](guard_dispatch_icall_function_006BAAD0.md) (`tail-transfer`)
  - `0x006B5DA5` → [KiKernelExit](../../kvascode/BC/KiKernelExit_function_00BCCB80.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006B5680  55                              push rbp
006B5681  56                              push rsi
006B5682  48 81 EC 50 01 00 00            sub rsp, 0x150
006B5689  48 8D AC 24 80 00 00 00         lea rbp, [rsp + 0x80]
006B5691  C6 45 AB 00                     mov byte ptr [rbp - 0x55], 0
006B5695  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
006B5699  48 89 4D B8                     mov qword ptr [rbp - 0x48], rcx
006B569D  48 89 55 C0                     mov qword ptr [rbp - 0x40], rdx
006B56A1  4C 89 45 C8                     mov qword ptr [rbp - 0x38], r8
006B56A5  4C 89 4D D0                     mov qword ptr [rbp - 0x30], r9
006B56A9  4C 89 55 D8                     mov qword ptr [rbp - 0x28], r10
006B56AD  4C 89 5D E0                     mov qword ptr [rbp - 0x20], r11
006B56B1  F6 85 F0 00 00 00 01            test byte ptr [rbp + 0xf0], 1
006B56B8  75 38                           jne 0x1406b56f2
006B56BA  33 D2                           xor edx, edx
006B56BC  F3 48 0F 1E CA                  rdsspq rdx
006B56C1  48 89 55 58                     mov qword ptr [rbp + 0x58], rdx
006B56C5  0F AE E8                        lfence
006B56C8  65 F6 04 25 58 08 00 00 01      test byte ptr gs:[0x858], 1
006B56D1  75 08                           jne 0x1406b56db
006B56D3  0F AE E8                        lfence
006B56D6  E9 88 02 00 00                  jmp 0x1406b5963
006B56DB  65 0F B7 04 25 66 08 00 00      movzx eax, word ptr gs:[0x866]
006B56E4  B9 48 00 00 00                  mov ecx, 0x48
006B56E9  33 D2                           xor edx, edx
006B56EB  0F 30                           wrmsr
006B56ED  E9 71 02 00 00                  jmp 0x1406b5963
006B56F2  F6 05 47 C1 B4 00 01            test byte ptr [rip + 0xb4c147], 1
006B56F9  75 03                           jne 0x1406b56fe
006B56FB  0F 01 F8                        swapgs
006B56FE  0F AE E8                        lfence
006B5701  65 48 8B 0C 25 28 9D 00 00      mov rcx, qword ptr gs:[0x9d28]
006B570A  48 85 C9                        test rcx, rcx
006B570D  74 1F                           je 0x1406b572e
006B570F  F3 48 0F 1E CA                  rdsspq rdx
006B5714  65 4C 8B 14 25 20 9D 00 00      mov r10, qword ptr gs:[0x9d20]
006B571D  49 83 C2 08                     add r10, 8
006B5721  49 3B D2                        cmp rdx, r10
006B5724  75 08                           jne 0x1406b572e
006B5726  F3 0F 01 29                     rstorssp dword ptr [rcx]
006B572A  F3 0F 01 EA                     saveprevssp
006B572E  65 4C 8B 14 25 88 01 00 00      mov r10, qword ptr gs:[0x188]
006B5737  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006B5740  48 8B 89 20 02 00 00            mov rcx, qword ptr [rcx + 0x220]
006B5747  48 8B 89 60 07 00 00            mov rcx, qword ptr [rcx + 0x760]
006B574E  65 48 89 0C 25 50 08 00 00      mov qword ptr gs:[0x850], rcx
006B5757  66 65 8B 0C 25 62 08 00 00      mov cx, word ptr gs:[0x862]
006B5760  66 65 89 0C 25 64 08 00 00      mov word ptr gs:[0x864], cx
006B5769  65 8A 0C 25 58 08 00 00         mov cl, byte ptr gs:[0x858]
006B5771  65 88 0C 25 5A 08 00 00         mov byte ptr gs:[0x85a], cl
006B5779  65 0F B7 04 25 68 08 00 00      movzx eax, word ptr gs:[0x868]
006B5782  66 65 39 04 25 66 08 00 00      cmp word ptr gs:[0x866], ax
006B578B  74 12                           je 0x1406b579f
006B578D  66 65 89 04 25 66 08 00 00      mov word ptr gs:[0x866], ax
006B5796  B9 48 00 00 00                  mov ecx, 0x48
006B579B  33 D2                           xor edx, edx
006B579D  0F 30                           wrmsr
006B579F  65 0F B6 14 25 58 08 00 00      movzx edx, byte ptr gs:[0x858]
006B57A8  F7 C2 08 00 00 00               test edx, 8
006B57AE  74 17                           je 0x1406b57c7
006B57B0  B8 01 00 00 00                  mov eax, 1
006B57B5  33 D2                           xor edx, edx
006B57B7  B9 49 00 00 00                  mov ecx, 0x49
006B57BC  0F 30                           wrmsr
006B57BE  65 0F B6 14 25 58 08 00 00      movzx edx, byte ptr gs:[0x858]
006B57C7  F7 C2 02 00 00 00               test edx, 2
006B57CD  0F 84 37 01 00 00               je 0x1406b590a
006B57D3  E8 0E 01 00 00                  call 0x1406b58e6
006B57D8  48 83 C4 08                     add rsp, 8
006B57DC  E8 0E 01 00 00                  call 0x1406b58ef
006B57E1  48 83 C4 08                     add rsp, 8
006B57E5  E8 EE FF FF FF                  call 0x1406b57d8
006B57EA  48 83 C4 08                     add rsp, 8
006B57EE  E8 EE FF FF FF                  call 0x1406b57e1
006B57F3  48 83 C4 08                     add rsp, 8
006B57F7  E8 EE FF FF FF                  call 0x1406b57ea
006B57FC  48 83 C4 08                     add rsp, 8
006B5800  E8 EE FF FF FF                  call 0x1406b57f3
006B5805  48 83 C4 08                     add rsp, 8
006B5809  E8 EE FF FF FF                  call 0x1406b57fc
006B580E  48 83 C4 08                     add rsp, 8
006B5812  E8 EE FF FF FF                  call 0x1406b5805
006B5817  48 83 C4 08                     add rsp, 8
006B581B  E8 EE FF FF FF                  call 0x1406b580e
006B5820  48 83 C4 08                     add rsp, 8
006B5824  E8 EE FF FF FF                  call 0x1406b5817
006B5829  48 83 C4 08                     add rsp, 8
006B582D  E8 EE FF FF FF                  call 0x1406b5820
006B5832  48 83 C4 08                     add rsp, 8
006B5836  E8 EE FF FF FF                  call 0x1406b5829
006B583B  48 83 C4 08                     add rsp, 8
006B583F  E8 EE FF FF FF                  call 0x1406b5832
006B5844  48 83 C4 08                     add rsp, 8
006B5848  E8 EE FF FF FF                  call 0x1406b583b
006B584D  48 83 C4 08                     add rsp, 8
006B5851  E8 EE FF FF FF                  call 0x1406b5844
006B5856  48 83 C4 08                     add rsp, 8
006B585A  E8 EE FF FF FF                  call 0x1406b584d
006B585F  48 83 C4 08                     add rsp, 8
006B5863  E8 EE FF FF FF                  call 0x1406b5856
006B5868  48 83 C4 08                     add rsp, 8
006B586C  E8 EE FF FF FF                  call 0x1406b585f
006B5871  48 83 C4 08                     add rsp, 8
006B5875  E8 EE FF FF FF                  call 0x1406b5868
006B587A  48 83 C4 08                     add rsp, 8
006B587E  E8 EE FF FF FF                  call 0x1406b5871
006B5883  48 83 C4 08                     add rsp, 8
006B5887  E8 EE FF FF FF                  call 0x1406b587a
006B588C  48 83 C4 08                     add rsp, 8
006B5890  E8 EE FF FF FF                  call 0x1406b5883
006B5895  48 83 C4 08                     add rsp, 8
006B5899  E8 EE FF FF FF                  call 0x1406b588c
006B589E  48 83 C4 08                     add rsp, 8
006B58A2  E8 EE FF FF FF                  call 0x1406b5895
006B58A7  48 83 C4 08                     add rsp, 8
006B58AB  E8 EE FF FF FF                  call 0x1406b589e
006B58B0  48 83 C4 08                     add rsp, 8
006B58B4  E8 EE FF FF FF                  call 0x1406b58a7
006B58B9  48 83 C4 08                     add rsp, 8
006B58BD  E8 EE FF FF FF                  call 0x1406b58b0
006B58C2  48 83 C4 08                     add rsp, 8
006B58C6  E8 EE FF FF FF                  call 0x1406b58b9
006B58CB  48 83 C4 08                     add rsp, 8
006B58CF  E8 EE FF FF FF                  call 0x1406b58c2
006B58D4  48 83 C4 08                     add rsp, 8
006B58D8  E8 EE FF FF FF                  call 0x1406b58cb
006B58DD  48 83 C4 08                     add rsp, 8
006B58E1  E8 EE FF FF FF                  call 0x1406b58d4
006B58E6  48 83 C4 08                     add rsp, 8
006B58EA  E8 EE FF FF FF                  call 0x1406b58dd
006B58EF  48 83 C4 08                     add rsp, 8
006B58F3  B8 DA DA 00 00                  mov eax, 0xdada
006B58F8  65 F6 04 25 5C 08 00 00 08      test byte ptr gs:[0x85c], 8
006B5901  74 07                           je 0x1406b590a
006B5903  B0 20                           mov al, 0x20
006B5905  F3 48 0F AE E8                  incsspq rax
006B590A  F7 C2 80 00 00 00               test edx, 0x80
006B5910  74 08                           je 0x1406b591a
006B5912  0F AE E8                        lfence
006B5915  E8 26 0A 01 00                  call 0x1406c6340
006B591A  0F AE E8                        lfence
006B591D  65 C6 04 25 5E 08 00 00 00      mov byte ptr gs:[0x85e], 0
006B5926  83 3D 37 19 91 00 00            cmp dword ptr [rip + 0x911937], 0
006B592D  74 1F                           je 0x1406b594e
006B592F  B9 A7 06 00 00                  mov ecx, 0x6a7
006B5934  0F 32                           rdmsr
006B5936  83 FA 00                        cmp edx, 0
006B5939  74 13                           je 0x1406b594e
006B593B  8B CA                           mov ecx, edx
006B593D  23 15 21 19 91 00               and edx, dword ptr [rip + 0x911921]
006B5943  3B D1                           cmp edx, ecx
006B5945  74 07                           je 0x1406b594e
006B5947  B9 A7 06 00 00                  mov ecx, 0x6a7
006B594C  0F 30                           wrmsr
006B594E  41 F6 42 03 03                  test byte ptr [r10 + 3], 3
006B5953  66 C7 85 80 00 00 00 00 00      mov word ptr [rbp + 0x80], 0
006B595C  74 05                           je 0x1406b5963
006B595E  E8 FD 7F E4 FF                  call 0x1404fd960
006B5963  FC                              cld
006B5964  0F AE 5D AC                     stmxcsr dword ptr [rbp - 0x54]
006B5968  65 0F AE 14 25 80 01 00 00      ldmxcsr dword ptr gs:[0x180]
006B5971  0F 29 45 F0                     movaps xmmword ptr [rbp - 0x10], xmm0
006B5975  0F 29 4D 00                     movaps xmmword ptr [rbp], xmm1
006B5979  0F 29 55 10                     movaps xmmword ptr [rbp + 0x10], xmm2
006B597D  0F 29 5D 20                     movaps xmmword ptr [rbp + 0x20], xmm3
006B5981  0F 29 65 30                     movaps xmmword ptr [rbp + 0x30], xmm4
006B5985  0F 29 6D 40                     movaps xmmword ptr [rbp + 0x40], xmm5
006B5989  F6 85 F0 00 00 00 01            test byte ptr [rbp + 0xf0], 1
006B5990  74 05                           je 0x1406b5997
006B5992  E8 09 66 D6 FF                  call 0x14041bfa0
006B5997  65 80 3C 25 DA 87 00 00 00      cmp byte ptr gs:[0x87da], 0
006B59A0  74 05                           je 0x1406b59a7
006B59A2  E8 D9 86 F0 FF                  call 0x1405be080
006B59A7  48 8D 05 C9 4B 00 00            lea rax, [rip + 0x4bc9]
006B59AE  48 3B 85 E8 00 00 00            cmp rax, qword ptr [rbp + 0xe8]
006B59B5  73 19                           jae 0x1406b59d0
006B59B7  48 8D 05 D2 4B 00 00            lea rax, [rip + 0x4bd2]
006B59BE  48 3B 85 E8 00 00 00            cmp rax, qword ptr [rbp + 0xe8]
006B59C5  72 09                           jb 0x1406b59d0
006B59C7  48 8D 4D 80                     lea rcx, [rbp - 0x80]
006B59CB  E8 40 5E D5 FF                  call 0x14040b810
006B59D0  0F B6 85 E0 00 00 00            movzx eax, byte ptr [rbp + 0xe0]
006B59D7  65 48 8B 34 25 20 00 00 00      mov rsi, qword ptr gs:[0x20]
006B59E0  48 8B B4 C6 00 39 00 00         mov rsi, qword ptr [rsi + rax*8 + 0x3900]
006B59E8  65 FF 04 25 C0 87 00 00         inc dword ptr gs:[0x87c0]
006B59F0  F6 05 F9 11 91 00 FF            test byte ptr [rip + 0x9111f9], 0xff
006B59F7  74 03                           je 0x1406b59fc
006B59F9  0F 01 CA                        clac
006B59FC  48 85 F6                        test rsi, rsi
006B59FF  74 09                           je 0x1406b5a0a
006B5A01  48 8B 46 50                     mov rax, qword ptr [rsi + 0x50]
006B5A05  E9 C6 50 00 00                  jmp 0x1406baad0
006B5A0A  8B C8                           mov ecx, eax
006B5A0C  C1 E9 04                        shr ecx, 4
006B5A0F  83 3D 0A 13 91 00 00            cmp dword ptr [rip + 0x91130a], 0
006B5A16  74 07                           je 0x1406b5a1f
006B5A18  E8 C3 30 F0 FF                  call 0x1405b8ae0
006B5A1D  EB 08                           jmp 0x1406b5a27
006B5A1F  44 0F 20 C0                     mov rax, cr8
006B5A23  44 0F 22 C1                     mov cr8, rcx
006B5A27  88 45 A9                        mov byte ptr [rbp - 0x57], al
006B5A2A  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
006B5A33  33 D2                           xor edx, edx
006B5A35  E8 D6 59 CC FF                  call 0x14037b410
006B5A3A  FB                              sti
006B5A3B  F7 05 BF 10 91 00 00 40 00 00   test dword ptr [rip + 0x9110bf], 0x4000
006B5A45  74 0C                           je 0x1406b5a53
006B5A47  0F B6 8D E0 00 00 00            movzx ecx, byte ptr [rbp + 0xe0]
006B5A4E  E8 8D B9 F9 FF                  call 0x1406513e0
006B5A53  80 3D A2 0E 7B 00 00            cmp byte ptr [rip + 0x7b0ea2], 0
006B5A5A  74 1F                           je 0x1406b5a7b
006B5A5C  48 83 65 A0 00                  and qword ptr [rbp - 0x60], 0
006B5A61  4D 33 C9                        xor r9, r9
006B5A64  44 0F B6 85 E0 00 00 00         movzx r8d, byte ptr [rbp + 0xe0]
006B5A6C  BA 01 00 00 00                  mov edx, 1
006B5A71  B9 12 00 00 00                  mov ecx, 0x12
006B5A76  E8 05 FE 00 00                  call 0x1406c5880
006B5A7B  FA                              cli
006B5A7C  48 8B CE                        mov rcx, rsi
006B5A7F  E8 9C 33 D6 FF                  call 0x140418e20
006B5A84  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
006B5A8D  0F B6 55 A9                     movzx edx, byte ptr [rbp - 0x57]
006B5A91  E8 4A 50 D4 FF                  call 0x1403faae0
006B5A96  84 C0                           test al, al
006B5A98  74 05                           je 0x1406b5a9f
006B5A9A  E8 41 34 00 00                  call 0x1406b8ee0
006B5A9F  0F B6 4D A9                     movzx ecx, byte ptr [rbp - 0x57]
006B5AA3  83 3D 76 12 91 00 00            cmp dword ptr [rip + 0x911276], 0
006B5AAA  74 07                           je 0x1406b5ab3
006B5AAC  E8 2F 30 F0 FF                  call 0x1405b8ae0
006B5AB1  EB 04                           jmp 0x1406b5ab7
006B5AB3  44 0F 22 C1                     mov cr8, rcx
006B5AB7  48 8B B5 D0 00 00 00            mov rsi, qword ptr [rbp + 0xd0]
006B5ABE  FA                              cli
006B5ABF  F6 85 F0 00 00 00 01            test byte ptr [rbp + 0xf0], 1
006B5AC6  0F 84 F5 02 00 00               je 0x1406b5dc1
006B5ACC  F6 05 1D 11 91 00 FF            test byte ptr [rip + 0x91111d], 0xff
006B5AD3  74 03                           je 0x1406b5ad8
006B5AD5  0F 01 CB                        stac
006B5AD8  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006B5AE1  F6 81 C2 00 00 00 03            test byte ptr [rcx + 0xc2], 3
006B5AE8  74 1B                           je 0x1406b5b05
006B5AEA  B9 01 00 00 00                  mov ecx, 1
006B5AEF  44 0F 22 C1                     mov cr8, rcx
006B5AF3  FB                              sti
006B5AF4  E8 47 0A 00 00                  call 0x1406b6540
006B5AF9  FA                              cli
006B5AFA  B9 00 00 00 00                  mov ecx, 0
006B5AFF  44 0F 22 C1                     mov cr8, rcx
006B5B03  EB D3                           jmp 0x1406b5ad8
006B5B05  E8 56 E4 BA FF                  call 0x140263f60
006B5B0A  85 C0                           test eax, eax
006B5B0C  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
006B5B10  75 C6                           jne 0x1406b5ad8
006B5B12  65 F6 04 25 60 08 00 00 02      test byte ptr gs:[0x860], 2
006B5B1B  74 07                           je 0x1406b5b24
006B5B1D  33 C9                           xor ecx, ecx
006B5B1F  E8 9C 16 D3 FF                  call 0x1403e71c0
006B5B24  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006B5B2D  F7 01 00 00 00 08               test dword ptr [rcx], 0x8000000
006B5B33  74 05                           je 0x1406b5b3a
006B5B35  E8 66 C1 FF FF                  call 0x1406b1ca0
006B5B3A  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006B5B43  F7 01 00 00 01 00               test dword ptr [rcx], 0x10000
006B5B49  74 14                           je 0x1406b5b5f
006B5B4B  F6 41 02 01                     test byte ptr [rcx + 2], 1
006B5B4F  74 0E                           je 0x1406b5b5f
006B5B51  E8 BA AB F0 FF                  call 0x1405c0710
006B5B56  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006B5B5F  0F AE 55 AC                     ldmxcsr dword ptr [rbp - 0x54]
006B5B63  66 83 BD 80 00 00 00 00         cmp word ptr [rbp + 0x80], 0
006B5B6B  74 05                           je 0x1406b5b72
006B5B6D  E8 6E 7D E4 FF                  call 0x1404fd8e0
006B5B72  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006B5B7B  0F BA 61 74 16                  bt dword ptr [rcx + 0x74], 0x16
006B5B80  73 2A                           jae 0x1406b5bac
006B5B82  33 C9                           xor ecx, ecx
006B5B84  F3 48 0F 1E C9                  rdsspq rcx
006B5B89  65 4C 8B 04 25 28 9D 00 00      mov r8, qword ptr gs:[0x9d28]
006B5B92  49 83 C0 08                     add r8, 8
006B5B96  49 3B C8                        cmp rcx, r8
006B5B99  75 11                           jne 0x1406b5bac
006B5B9B  65 48 8B 0C 25 20 9D 00 00      mov rcx, qword ptr gs:[0x9d20]
006B5BA4  F3 0F 01 29                     rstorssp dword ptr [rcx]
006B5BA8  F3 0F 01 EA                     saveprevssp
006B5BAC  65 C6 04 25 5E 08 00 00 00      mov byte ptr gs:[0x85e], 0
006B5BB5  65 0F B7 04 25 6C 08 00 00      movzx eax, word ptr gs:[0x86c]
006B5BBE  66 65 39 04 25 66 08 00 00      cmp word ptr gs:[0x866], ax
006B5BC7  74 12                           je 0x1406b5bdb
006B5BC9  66 65 89 04 25 66 08 00 00      mov word ptr gs:[0x866], ax
006B5BD2  B9 48 00 00 00                  mov ecx, 0x48
006B5BD7  33 D2                           xor edx, edx
006B5BD9  0F 30                           wrmsr
006B5BDB  66 65 0F BA 34 25 58 08 00 00 02  btr word ptr gs:[0x858], 2
006B5BE6  73 0E                           jae 0x1406b5bf6
006B5BE8  B8 01 00 00 00                  mov eax, 1
006B5BED  33 D2                           xor edx, edx
006B5BEF  B9 49 00 00 00                  mov ecx, 0x49
006B5BF4  0F 30                           wrmsr
006B5BF6  66 65 0F BA 34 25 58 08 00 00 05  btr word ptr gs:[0x858], 5
006B5C01  0F 83 37 01 00 00               jae 0x1406b5d3e
006B5C07  E8 0E 01 00 00                  call 0x1406b5d1a
006B5C0C  48 83 C4 08                     add rsp, 8
006B5C10  E8 0E 01 00 00                  call 0x1406b5d23
006B5C15  48 83 C4 08                     add rsp, 8
006B5C19  E8 EE FF FF FF                  call 0x1406b5c0c
006B5C1E  48 83 C4 08                     add rsp, 8
006B5C22  E8 EE FF FF FF                  call 0x1406b5c15
006B5C27  48 83 C4 08                     add rsp, 8
006B5C2B  E8 EE FF FF FF                  call 0x1406b5c1e
006B5C30  48 83 C4 08                     add rsp, 8
006B5C34  E8 EE FF FF FF                  call 0x1406b5c27
006B5C39  48 83 C4 08                     add rsp, 8
006B5C3D  E8 EE FF FF FF                  call 0x1406b5c30
006B5C42  48 83 C4 08                     add rsp, 8
006B5C46  E8 EE FF FF FF                  call 0x1406b5c39
006B5C4B  48 83 C4 08                     add rsp, 8
006B5C4F  E8 EE FF FF FF                  call 0x1406b5c42
006B5C54  48 83 C4 08                     add rsp, 8
006B5C58  E8 EE FF FF FF                  call 0x1406b5c4b
006B5C5D  48 83 C4 08                     add rsp, 8
006B5C61  E8 EE FF FF FF                  call 0x1406b5c54
006B5C66  48 83 C4 08                     add rsp, 8
006B5C6A  E8 EE FF FF FF                  call 0x1406b5c5d
006B5C6F  48 83 C4 08                     add rsp, 8
006B5C73  E8 EE FF FF FF                  call 0x1406b5c66
006B5C78  48 83 C4 08                     add rsp, 8
006B5C7C  E8 EE FF FF FF                  call 0x1406b5c6f
006B5C81  48 83 C4 08                     add rsp, 8
006B5C85  E8 EE FF FF FF                  call 0x1406b5c78
006B5C8A  48 83 C4 08                     add rsp, 8
006B5C8E  E8 EE FF FF FF                  call 0x1406b5c81
006B5C93  48 83 C4 08                     add rsp, 8
006B5C97  E8 EE FF FF FF                  call 0x1406b5c8a
006B5C9C  48 83 C4 08                     add rsp, 8
006B5CA0  E8 EE FF FF FF                  call 0x1406b5c93
006B5CA5  48 83 C4 08                     add rsp, 8
006B5CA9  E8 EE FF FF FF                  call 0x1406b5c9c
006B5CAE  48 83 C4 08                     add rsp, 8
006B5CB2  E8 EE FF FF FF                  call 0x1406b5ca5
006B5CB7  48 83 C4 08                     add rsp, 8
006B5CBB  E8 EE FF FF FF                  call 0x1406b5cae
006B5CC0  48 83 C4 08                     add rsp, 8
006B5CC4  E8 EE FF FF FF                  call 0x1406b5cb7
006B5CC9  48 83 C4 08                     add rsp, 8
006B5CCD  E8 EE FF FF FF                  call 0x1406b5cc0
006B5CD2  48 83 C4 08                     add rsp, 8
006B5CD6  E8 EE FF FF FF                  call 0x1406b5cc9
006B5CDB  48 83 C4 08                     add rsp, 8
006B5CDF  E8 EE FF FF FF                  call 0x1406b5cd2
006B5CE4  48 83 C4 08                     add rsp, 8
006B5CE8  E8 EE FF FF FF                  call 0x1406b5cdb
006B5CED  48 83 C4 08                     add rsp, 8
006B5CF1  E8 EE FF FF FF                  call 0x1406b5ce4
006B5CF6  48 83 C4 08                     add rsp, 8
006B5CFA  E8 EE FF FF FF                  call 0x1406b5ced
006B5CFF  48 83 C4 08                     add rsp, 8
006B5D03  E8 EE FF FF FF                  call 0x1406b5cf6
006B5D08  48 83 C4 08                     add rsp, 8
006B5D0C  E8 EE FF FF FF                  call 0x1406b5cff
006B5D11  48 83 C4 08                     add rsp, 8
006B5D15  E8 EE FF FF FF                  call 0x1406b5d08
006B5D1A  48 83 C4 08                     add rsp, 8
006B5D1E  E8 EE FF FF FF                  call 0x1406b5d11
006B5D23  48 83 C4 08                     add rsp, 8
006B5D27  B8 DA DA 00 00                  mov eax, 0xdada
006B5D2C  65 F6 04 25 5C 08 00 00 08      test byte ptr gs:[0x85c], 8
006B5D35  74 07                           je 0x1406b5d3e
006B5D37  B0 20                           mov al, 0x20
006B5D39  F3 48 0F AE E8                  incsspq rax
006B5D3E  66 65 F7 04 25 58 08 00 00 00 01  test word ptr gs:[0x858], 0x100
006B5D49  74 0C                           je 0x1406b5d57
006B5D4B  33 C0                           xor eax, eax
006B5D4D  33 D2                           xor edx, edx
006B5D4F  B9 01 00 00 00                  mov ecx, 1
006B5D54  48 F7 F1                        div rcx
006B5D57  0F 28 45 F0                     movaps xmm0, xmmword ptr [rbp - 0x10]
006B5D5B  0F 28 4D 00                     movaps xmm1, xmmword ptr [rbp]
006B5D5F  0F 28 55 10                     movaps xmm2, xmmword ptr [rbp + 0x10]
006B5D63  0F 28 5D 20                     movaps xmm3, xmmword ptr [rbp + 0x20]
006B5D67  0F 28 65 30                     movaps xmm4, xmmword ptr [rbp + 0x30]
006B5D6B  0F 28 6D 40                     movaps xmm5, xmmword ptr [rbp + 0x40]
006B5D6F  4C 8B 5D E0                     mov r11, qword ptr [rbp - 0x20]
006B5D73  4C 8B 55 D8                     mov r10, qword ptr [rbp - 0x28]
006B5D77  4C 8B 4D D0                     mov r9, qword ptr [rbp - 0x30]
006B5D7B  4C 8B 45 C8                     mov r8, qword ptr [rbp - 0x38]
006B5D7F  48 8B 55 C0                     mov rdx, qword ptr [rbp - 0x40]
006B5D83  48 8B 4D B8                     mov rcx, qword ptr [rbp - 0x48]
006B5D87  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
006B5D8B  48 8B E5                        mov rsp, rbp
006B5D8E  48 8B AD D8 00 00 00            mov rbp, qword ptr [rbp + 0xd8]
006B5D95  48 81 C4 E8 00 00 00            add rsp, 0xe8
006B5D9C  F6 05 9D BA B4 00 01            test byte ptr [rip + 0xb4ba9d], 1
006B5DA3  74 05                           je 0x1406b5daa
006B5DA5  E9 D6 6D 51 00                  jmp 0x140bccb80
006B5DAA  66 65 F7 04 25 58 08 00 00 00 02  test word ptr gs:[0x858], 0x200
006B5DB5  74 05                           je 0x1406b5dbc
006B5DB7  0F 00 6C 24 20                  verw word ptr [rsp + 0x20]
006B5DBC  0F 01 F8                        swapgs
006B5DBF  48 CF                           iretq
006B5DC1  0F AE 55 AC                     ldmxcsr dword ptr [rbp - 0x54]
006B5DC5  0F 28 45 F0                     movaps xmm0, xmmword ptr [rbp - 0x10]
006B5DC9  0F 28 4D 00                     movaps xmm1, xmmword ptr [rbp]
006B5DCD  0F 28 55 10                     movaps xmm2, xmmword ptr [rbp + 0x10]
006B5DD1  0F 28 5D 20                     movaps xmm3, xmmword ptr [rbp + 0x20]
006B5DD5  0F 28 65 30                     movaps xmm4, xmmword ptr [rbp + 0x30]
006B5DD9  0F 28 6D 40                     movaps xmm5, xmmword ptr [rbp + 0x40]
006B5DDD  4C 8B 5D E0                     mov r11, qword ptr [rbp - 0x20]
006B5DE1  4C 8B 55 D8                     mov r10, qword ptr [rbp - 0x28]
006B5DE5  4C 8B 4D D0                     mov r9, qword ptr [rbp - 0x30]
006B5DE9  4C 8B 45 C8                     mov r8, qword ptr [rbp - 0x38]
006B5DED  48 8B 55 C0                     mov rdx, qword ptr [rbp - 0x40]
006B5DF1  48 8B 4D B8                     mov rcx, qword ptr [rbp - 0x48]
006B5DF5  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
006B5DF9  48 8B E5                        mov rsp, rbp
006B5DFC  48 8B AD D8 00 00 00            mov rbp, qword ptr [rbp + 0xd8]
006B5E03  48 81 C4 E8 00 00 00            add rsp, 0xe8
006B5E0A  48 CF                           iretq
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KxIsrLinkage(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned __int16 a5)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned int v_stack_m134;
    unsigned __int8 v_stack_m135;
    unsigned __int8 v_stack_m137;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m160;
    unsigned __int16 v_stack_m60;
    unsigned __int64 v_stack_m8;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mF0;
    unsigned __int8 v_stack_p0;
    unsigned __int8 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (336);
    v_stack_m135 = 0;
    v_stack_m130 = result;
    v_stack_m128 = a1;
    v_stack_m120 = a2;
    v_stack_m118 = a3;
    v_stack_m110 = a4;
    v_stack_m108 = v_r10;
    v_stack_m100 = v_r11;
    if (((v_stack_p10) & (1)) != 0) goto loc_006B56F2;
    a2 = 0;
    v_stack_m88 = 0;
    if (((*(unsigned __int8 *)(gs_base + (0 + 2136))) & (1)) != 0) goto loc_006B56DB;
    goto loc_006B5963;
loc_006B56DB:
    a2 = 0;
    goto loc_006B5963;
loc_006B56F2:
    if (((*(unsigned __int8 *)(v_rip + 11845959)) & (1)) == 0) {
    }
    if (*(unsigned __int64 *)(gs_base + (0 + 40232)) == 0) goto loc_006B572E;
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
    if ((((unsigned int)(a2)) & (2)) == 0) goto loc_006B590A;
    result = KxIsrLinkage___0x266(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxIsrLinkage___0x26F(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxIsrLinkage___0x158(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxIsrLinkage___0x161(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxIsrLinkage___0x16A(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxIsrLinkage___0x173(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxIsrLinkage___0x17C(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxIsrLinkage___0x185(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxIsrLinkage___0x18E(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxIsrLinkage___0x197(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxIsrLinkage___0x1A0(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxIsrLinkage___0x1A9(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxIsrLinkage___0x1B2(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxIsrLinkage___0x1BB(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxIsrLinkage___0x1C4(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxIsrLinkage___0x1CD(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxIsrLinkage___0x1D6(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxIsrLinkage___0x1DF(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxIsrLinkage___0x1E8(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxIsrLinkage___0x1F1(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxIsrLinkage___0x1FA(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxIsrLinkage___0x203(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxIsrLinkage___0x20C(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxIsrLinkage___0x215(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxIsrLinkage___0x21E(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxIsrLinkage___0x227(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxIsrLinkage___0x230(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxIsrLinkage___0x239(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxIsrLinkage___0x242(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxIsrLinkage___0x24B(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxIsrLinkage___0x254(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxIsrLinkage___0x25D(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = (unsigned int)(0xDADAULL);
    if (((*(unsigned __int8 *)(gs_base + (0 + 2140))) & (8)) != 0) {
        result = 32;
    }
    if ((((unsigned int)(a2)) & (128)) != 0) {
        result = KiFlushBhbDuringTrapEntryOrExit(a1, a2, a3, a4);
    }
    *(unsigned __int8 *)(gs_base + (0 + 2142)) = 0;
    if ((*(unsigned int *)(v_rip + 9509175)) == 0) goto loc_006B594E;
    if (((unsigned int)(a2)) == 0) goto loc_006B594E;
    a2 = (unsigned int)((a2) & (*(unsigned int *)(v_rip + 9509153)));
    if (((unsigned int)(a2)) != ((unsigned int)((unsigned int)((unsigned int)(a2))))) {
        a1 = 0x6A7ULL;
    }
    v_stack_m60 = 0;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 3)) & (3)) != 0) {
        result = KiSaveDebugRegisterState(a1, a2, a3, a4);
    }
    v_stack_mF0 = v_xmm0;
    v_stack_mE0 = v_xmm1;
    v_stack_mD0 = v_xmm2;
    v_stack_mC0 = v_xmm3;
    v_stack_mB0 = v_xmm4;
    v_stack_mA0 = v_xmm5;
    if (((v_stack_p10) & (1)) != 0) {
        result = KiSynchronizeUserIsolationDomainExit(a1, a2, a3, a4);
    }
    if ((*(unsigned __int8 *)(gs_base + (0 + 34778))) != 0) {
        result = KeWakeProcessor(a1, a2, a3, a4);
    }
    if ((v_rip + 19401) >= v_stack_p8) goto loc_006B59D0;
    result = v_rip + 19410;
    if ((v_rip + 19410) >= v_stack_p8) {
        a1 = v_stack_m160;
        result = KiCheckForSListAddress(a1, a2, a3, a4);
    }
    if (((*(unsigned __int8 *)(v_rip + 9507321)) & (255)) != 0) {
    }
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + v_stack_p0 * 8 + 14592) == 0) goto loc_006B5A0A;
loc_006B5A0A:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + v_stack_p0 * 8 + 14592) + 80)))) >> (4));
    if ((*(unsigned int *)(v_rip + 9507594)) == 0) goto loc_006B5A1F;
    result = KzSetIrqlUnsafe(a1, a2, a3, a4);
    goto loc_006B5A27;
loc_006B5A1F:
loc_006B5A27:
    v_stack_m137 = (unsigned __int8)(v_cr8);
    a2 = 0;
    result = KiStartInterruptCycleAccumulation(*(unsigned __int64 *)(gs_base + (0 + 32)), a2, a3, a4);
    if (((*(unsigned int *)(v_rip + 9507007)) & (0x4000ULL)) != 0) {
        a1 = v_stack_p0;
        result = PerfInfoLogUnexpectedInterrupt(a1, a2, a3, a4);
    }
    if ((*(unsigned __int8 *)(v_rip + 8064674)) != 0) {
        a4 = 0;
        a3 = v_stack_p0;
        a2 = 1;
        a1 = 18;
        result = KiBugCheckDispatch(a1, a2, a3, a4);
    }
    result = HalPerformEndOfInterrupt(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + v_stack_p0 * 8 + 14592), a2, a3, a4);
    result = KiEndInterruptCycleAccumulation(*(unsigned __int64 *)(gs_base + (0 + 32)), v_stack_m137, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        result = KiDpcInterruptBypass(*(unsigned __int64 *)(gs_base + (0 + 32)), v_stack_m137, a3, a4);
    }
    if ((*(unsigned int *)(v_rip + 9507446)) == 0) goto loc_006B5AB3;
    result = KzSetIrqlUnsafe(v_stack_m137, v_stack_m137, a3, a4);
    goto loc_006B5AB7;
loc_006B5AB3:
loc_006B5AB7:
    if (((v_stack_p10) & (1)) == 0) goto loc_006B5DC1;
    if (((*(unsigned __int8 *)(v_rip + 9507101)) & (255)) != 0) {
    }
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 194)) & (3)) == 0) goto loc_006B5B05;
    result = KiInitiateUserApc(1, v_stack_m137, a3, a4);
    goto loc_006B5AD8;
loc_006B5B05:
    result = KiSynchronizeUserIsolationDomainEntry(0, v_stack_m137, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_006B5AD8;
    result = v_stack_m130;
    if (((*(unsigned __int8 *)(gs_base + (0 + 2144))) & (2)) != 0) {
        a1 = 0;
        result = KiUpdateStibpPairing(a1, v_stack_m137, a3, a4);
    }
    if (((*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)))) & (0x8000000ULL)) != 0) {
        result = KiRestoreSetContextState(*(unsigned __int64 *)(gs_base + (0 + 392)), v_stack_m137, a3, a4);
    }
    if (((*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)))) & (0x10000ULL)) == 0) goto loc_006B5B5F;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 2)) & (1)) != 0) {
        result = KiCopyCounters(*(unsigned __int64 *)(gs_base + (0 + 392)), v_stack_m137, a3, a4);
        a1 = *(unsigned __int64 *)(gs_base + (0 + 392));
    }
    if (v_stack_m60 != 0) {
        result = KiRestoreDebugRegisterState(a1, v_stack_m137, a3, a4);
    }
    if (v_stack_m60 >= 0) goto loc_006B5BAC;
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
    if (condition_is_above_or_equal) goto loc_006B5D3E;
    result = KxIsrLinkage___0x69A(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxIsrLinkage___0x6A3(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxIsrLinkage___0x58C(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxIsrLinkage___0x595(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxIsrLinkage___0x59E(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxIsrLinkage___0x5A7(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxIsrLinkage___0x5B0(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxIsrLinkage___0x5B9(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxIsrLinkage___0x5C2(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxIsrLinkage___0x5CB(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxIsrLinkage___0x5D4(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxIsrLinkage___0x5DD(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxIsrLinkage___0x5E6(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxIsrLinkage___0x5EF(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxIsrLinkage___0x5F8(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxIsrLinkage___0x601(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxIsrLinkage___0x60A(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxIsrLinkage___0x613(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxIsrLinkage___0x61C(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxIsrLinkage___0x625(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxIsrLinkage___0x62E(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxIsrLinkage___0x637(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxIsrLinkage___0x640(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxIsrLinkage___0x649(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxIsrLinkage___0x652(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxIsrLinkage___0x65B(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxIsrLinkage___0x664(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxIsrLinkage___0x66D(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxIsrLinkage___0x676(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxIsrLinkage___0x67F(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxIsrLinkage___0x688(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KxIsrLinkage___0x691(a1, a2, a3, a4);
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
    v_rsp = (v_stack_mE0) + (232);
    if (((*(unsigned __int8 *)(v_rip + 11844253)) & (1)) == 0) goto loc_006B5DAA;
loc_006B5DAA:
    if (((*(unsigned __int16 *)(gs_base + (0 + 2136))) & (512)) != 0) {
    }
loc_006B5DC1:
    v_rsp = (v_stack_m8) + (232);
    return v_stack_m130;
}
```

## 5. (Beta) C Style

```c
int64_t KxIsrLinkage(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint16_t Arg5)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint32_t v_stack_m134;
    uint8_t v_stack_m135;
    uint8_t v_stack_m137;
    uint64_t v_stack_m140;
    uint64_t v_stack_m160;
    uint16_t v_stack_m60;
    uint64_t v_stack_m8;
    uint64_t v_stack_m88;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mF0;
    uint8_t v_stack_p0;
    uint8_t v_stack_p10;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (336);
    v_stack_m135 = 0;
    v_stack_m130 = result;
    v_stack_m128 = Arg1;
    v_stack_m120 = Arg2;
    v_stack_m118 = Arg3;
    v_stack_m110 = Arg4;
    v_stack_m108 = local_r10;
    v_stack_m100 = local_r11;
    if (((v_stack_p10) & (1)) != 0) goto loc_006B56F2;
    Arg2 = 0;
    v_stack_m88 = 0;
    if (((*(uint8_t *)(gs_base + (0 + 0x858))) & (1)) != 0) goto loc_006B56DB;
    goto loc_006B5963;
loc_006B56DB:
    Arg2 = 0;
    goto loc_006B5963;
loc_006B56F2:
    if (((*(uint8_t *)(v_rip + 0xB4C147)) & (1)) == 0) {
    }
    if (*(uint64_t *)(gs_base + (0 + 0x9D28)) == 0) goto loc_006B572E;
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
    if ((((uint32_t)(Arg2)) & (2)) == 0) goto loc_006B590A;
    result = KxIsrLinkage___0x266(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxIsrLinkage___0x26F(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxIsrLinkage___0x158(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxIsrLinkage___0x161(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxIsrLinkage___0x16A(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxIsrLinkage___0x173(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxIsrLinkage___0x17C(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxIsrLinkage___0x185(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxIsrLinkage___0x18E(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxIsrLinkage___0x197(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxIsrLinkage___0x1A0(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxIsrLinkage___0x1A9(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxIsrLinkage___0x1B2(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxIsrLinkage___0x1BB(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxIsrLinkage___0x1C4(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxIsrLinkage___0x1CD(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxIsrLinkage___0x1D6(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxIsrLinkage___0x1DF(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxIsrLinkage___0x1E8(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxIsrLinkage___0x1F1(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxIsrLinkage___0x1FA(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxIsrLinkage___0x203(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxIsrLinkage___0x20C(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxIsrLinkage___0x215(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxIsrLinkage___0x21E(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxIsrLinkage___0x227(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxIsrLinkage___0x230(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxIsrLinkage___0x239(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxIsrLinkage___0x242(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxIsrLinkage___0x24B(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxIsrLinkage___0x254(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxIsrLinkage___0x25D(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = (uint32_t)(0xDADAULL);
    if (((*(uint8_t *)(gs_base + (0 + 0x85C))) & (8)) != 0) {
        result = 32;
    }
    if ((((uint32_t)(Arg2)) & (128)) != 0) {
        result = KiFlushBhbDuringTrapEntryOrExit(Arg1, Arg2, Arg3, Arg4);
    }
    *(uint8_t *)(gs_base + (0 + 0x85E)) = 0;
    if ((*(uint32_t *)(v_rip + 0x911937)) == 0) goto loc_006B594E;
    if (((uint32_t)(Arg2)) == 0) goto loc_006B594E;
    Arg2 = (uint32_t)((Arg2) & (*(uint32_t *)(v_rip + 0x911921)));
    if (((uint32_t)(Arg2)) != ((uint32_t)((uint32_t)((uint32_t)(Arg2))))) {
        Arg1 = 0x6A7ULL;
    }
    v_stack_m60 = 0;
    if (((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x3)) & (3)) != 0) {
        result = KiSaveDebugRegisterState(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_mF0 = v_xmm0;
    v_stack_mE0 = v_xmm1;
    v_stack_mD0 = v_xmm2;
    v_stack_mC0 = v_xmm3;
    v_stack_mB0 = v_xmm4;
    v_stack_mA0 = v_xmm5;
    if (((v_stack_p10) & (1)) != 0) {
        result = KiSynchronizeUserIsolationDomainExit(Arg1, Arg2, Arg3, Arg4);
    }
    if ((*(uint8_t *)(gs_base + (0 + 0x87DA))) != 0) {
        result = KeWakeProcessor(Arg1, Arg2, Arg3, Arg4);
    }
    if ((v_rip + 19401) >= v_stack_p8) goto loc_006B59D0;
    result = v_rip + 19410;
    if ((v_rip + 19410) >= v_stack_p8) {
        Arg1 = v_stack_m160;
        result = KiCheckForSListAddress(Arg1, Arg2, Arg3, Arg4);
    }
    if (((*(uint8_t *)(v_rip + 0x9111F9)) & (255)) != 0) {
    }
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + v_stack_p0 * 8 + 0x3900) == 0) goto loc_006B5A0A;
loc_006B5A0A:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + v_stack_p0 * 8 + 0x3900) + 0x50)))) >> (4));
    if ((*(uint32_t *)(v_rip + 0x91130A)) == 0) goto loc_006B5A1F;
    result = KzSetIrqlUnsafe(Arg1, Arg2, Arg3, Arg4);
    goto loc_006B5A27;
loc_006B5A1F:
loc_006B5A27:
    v_stack_m137 = (uint8_t)(v_cr8);
    Arg2 = 0;
    result = KiStartInterruptCycleAccumulation(*(uint64_t *)(gs_base + (0 + 0x20)), Arg2, Arg3, Arg4);
    if (((*(uint32_t *)(v_rip + 0x9110BF)) & (0x4000ULL)) != 0) {
        Arg1 = v_stack_p0;
        result = PerfInfoLogUnexpectedInterrupt(Arg1, Arg2, Arg3, Arg4);
    }
    if ((*(uint8_t *)(v_rip + 0x7B0EA2)) != 0) {
        Arg4 = 0;
        Arg3 = v_stack_p0;
        Arg2 = 1;
        Arg1 = 18;
        result = KiBugCheckDispatch(Arg1, Arg2, Arg3, Arg4);
    }
    result = HalPerformEndOfInterrupt(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + v_stack_p0 * 8 + 0x3900), Arg2, Arg3, Arg4);
    result = KiEndInterruptCycleAccumulation(*(uint64_t *)(gs_base + (0 + 0x20)), v_stack_m137, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        result = KiDpcInterruptBypass(*(uint64_t *)(gs_base + (0 + 0x20)), v_stack_m137, Arg3, Arg4);
    }
    if ((*(uint32_t *)(v_rip + 0x911276)) == 0) goto loc_006B5AB3;
    result = KzSetIrqlUnsafe(v_stack_m137, v_stack_m137, Arg3, Arg4);
    goto loc_006B5AB7;
loc_006B5AB3:
loc_006B5AB7:
    if (((v_stack_p10) & (1)) == 0) goto loc_006B5DC1;
    if (((*(uint8_t *)(v_rip + 0x91111D)) & (255)) != 0) {
    }
    if (((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xC2)) & (3)) == 0) goto loc_006B5B05;
    result = KiInitiateUserApc(1, v_stack_m137, Arg3, Arg4);
    goto loc_006B5AD8;
loc_006B5B05:
    result = KiSynchronizeUserIsolationDomainEntry(0, v_stack_m137, Arg3, Arg4);
    if ((uint32_t)(result) != 0) goto loc_006B5AD8;
    result = v_stack_m130;
    if (((*(uint8_t *)(gs_base + (0 + 0x860))) & (2)) != 0) {
        Arg1 = 0;
        result = KiUpdateStibpPairing(Arg1, v_stack_m137, Arg3, Arg4);
    }
    if (((*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)))) & (0x8000000ULL)) != 0) {
        result = KiRestoreSetContextState(*(uint64_t *)(gs_base + (0 + 0x188)), v_stack_m137, Arg3, Arg4);
    }
    if (((*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)))) & (0x10000ULL)) == 0) goto loc_006B5B5F;
    if (((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x2)) & (1)) != 0) {
        result = KiCopyCounters(*(uint64_t *)(gs_base + (0 + 0x188)), v_stack_m137, Arg3, Arg4);
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x188));
    }
    if (v_stack_m60 != 0) {
        result = KiRestoreDebugRegisterState(Arg1, v_stack_m137, Arg3, Arg4);
    }
    if (v_stack_m60 >= 0) goto loc_006B5BAC;
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
    if (condition_is_above_or_equal) goto loc_006B5D3E;
    result = KxIsrLinkage___0x69A(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxIsrLinkage___0x6A3(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxIsrLinkage___0x58C(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxIsrLinkage___0x595(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxIsrLinkage___0x59E(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxIsrLinkage___0x5A7(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxIsrLinkage___0x5B0(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxIsrLinkage___0x5B9(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxIsrLinkage___0x5C2(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxIsrLinkage___0x5CB(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxIsrLinkage___0x5D4(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxIsrLinkage___0x5DD(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxIsrLinkage___0x5E6(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxIsrLinkage___0x5EF(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxIsrLinkage___0x5F8(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxIsrLinkage___0x601(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxIsrLinkage___0x60A(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxIsrLinkage___0x613(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxIsrLinkage___0x61C(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxIsrLinkage___0x625(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxIsrLinkage___0x62E(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxIsrLinkage___0x637(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxIsrLinkage___0x640(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxIsrLinkage___0x649(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxIsrLinkage___0x652(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxIsrLinkage___0x65B(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxIsrLinkage___0x664(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxIsrLinkage___0x66D(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxIsrLinkage___0x676(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxIsrLinkage___0x67F(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxIsrLinkage___0x688(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KxIsrLinkage___0x691(Arg1, Arg2, Arg3, Arg4);
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
    local_rsp = (v_stack_mE0) + (232);
    if (((*(uint8_t *)(v_rip + 0xB4BA9D)) & (1)) == 0) goto loc_006B5DAA;
loc_006B5DAA:
    if (((*(uint16_t *)(gs_base + (0 + 0x858))) & (512)) != 0) {
    }
loc_006B5DC1:
    local_rsp = (v_stack_m8) + (232);
    return v_stack_m130;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006B5680&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
