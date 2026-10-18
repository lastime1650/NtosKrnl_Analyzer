# KiSystemCall64

- RVA: `0x006C4A40`–`0x006C5852` (길이 `3,602` bytes)
- VA: `0x00000001406C4A40`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C1E30`
- 디코드: `787`개 명령, `3,602/3,602` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **123**; 고유 호출 대상: **115**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **11**

### Outgoing calls
- `0x006C4B67` → [KiSystemCall64 + 0x23A](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C4C7A`)
- `0x006C4B70` → [KiSystemCall64 + 0x243](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C4C83`)
- `0x006C4B79` → [KiSystemCall64 + 0x12C](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C4B6C`)
- `0x006C4B82` → [KiSystemCall64 + 0x135](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C4B75`)
- `0x006C4B8B` → [KiSystemCall64 + 0x13E](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C4B7E`)
- `0x006C4B94` → [KiSystemCall64 + 0x147](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C4B87`)
- `0x006C4B9D` → [KiSystemCall64 + 0x150](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C4B90`)
- `0x006C4BA6` → [KiSystemCall64 + 0x159](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C4B99`)
- `0x006C4BAF` → [KiSystemCall64 + 0x162](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C4BA2`)
- `0x006C4BB8` → [KiSystemCall64 + 0x16B](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C4BAB`)
- `0x006C4BC1` → [KiSystemCall64 + 0x174](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C4BB4`)
- `0x006C4BCA` → [KiSystemCall64 + 0x17D](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C4BBD`)
- `0x006C4BD3` → [KiSystemCall64 + 0x186](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C4BC6`)
- `0x006C4BDC` → [KiSystemCall64 + 0x18F](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C4BCF`)
- `0x006C4BE5` → [KiSystemCall64 + 0x198](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C4BD8`)
- `0x006C4BEE` → [KiSystemCall64 + 0x1A1](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C4BE1`)
- `0x006C4BF7` → [KiSystemCall64 + 0x1AA](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C4BEA`)
- `0x006C4C00` → [KiSystemCall64 + 0x1B3](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C4BF3`)
- `0x006C4C09` → [KiSystemCall64 + 0x1BC](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C4BFC`)
- `0x006C4C12` → [KiSystemCall64 + 0x1C5](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C4C05`)
- `0x006C4C1B` → [KiSystemCall64 + 0x1CE](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C4C0E`)
- `0x006C4C24` → [KiSystemCall64 + 0x1D7](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C4C17`)
- `0x006C4C2D` → [KiSystemCall64 + 0x1E0](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C4C20`)
- `0x006C4C36` → [KiSystemCall64 + 0x1E9](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C4C29`)
- `0x006C4C3F` → [KiSystemCall64 + 0x1F2](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C4C32`)
- `0x006C4C48` → [KiSystemCall64 + 0x1FB](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C4C3B`)
- `0x006C4C51` → [KiSystemCall64 + 0x204](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C4C44`)
- `0x006C4C5A` → [KiSystemCall64 + 0x20D](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C4C4D`)
- `0x006C4C63` → [KiSystemCall64 + 0x216](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C4C56`)
- `0x006C4C6C` → [KiSystemCall64 + 0x21F](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C4C5F`)
- `0x006C4C75` → [KiSystemCall64 + 0x228](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C4C68`)
- `0x006C4C7E` → [KiSystemCall64 + 0x231](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C4C71`)
- `0x006C4CA9` → [KiFlushBhbDuringTrapEntryOrExit](KiFlushBhbDuringTrapEntryOrExit_function_006C6340.md) (function, `0x006C6340`)
- `0x006C4D36` → [KiSynchronizeUserIsolationDomainExit](../41/KiSynchronizeUserIsolationDomainExit_function_0041BFA0.md) (function, `0x0041BFA0`)
- `0x006C4D50` → [KiSaveDebugRegisterState](../4F/KiSaveDebugRegisterState_function_004FD960.md) (function, `0x004FD960`)
- `0x006C4D66` → [PsSyscallProviderDispatch](../../page/AB/PsSyscallProviderDispatch_function_00AB3D80.md) (function, `0x00AB3D80`)
- `0x006C4D83` → [KiExceptionDispatch](KiExceptionDispatch_function_006C5900.md) (function, `0x006C5900`)
- `0x006C4E53` → [PsInvokeWin32Callout](../../page/91/PsInvokeWin32Callout_function_009133C0.md) (function, `0x009133C0`)
- `0x006C4F53` → `indirect target` (indirect, 간접 대상)
- `0x006C5008` → [KiInitiateUserApc](../6B/KiInitiateUserApc_function_006B6540.md) (function, `0x006B6540`)
- `0x006C5021` → [KiSynchronizeUserIsolationDomainEntry](../26/KiSynchronizeUserIsolationDomainEntry_function_00263F60.md) (function, `0x00263F60`)
- `0x006C503F` → [KiUpdateStibpPairing](../3E/KiUpdateStibpPairing_function_003E71C0.md) (function, `0x003E71C0`)
- `0x006C5093` → [KiRestoreSetContextState](../6B/KiRestoreSetContextState_function_006B1CA0.md) (function, `0x006B1CA0`)
- `0x006C50B3` → [KiCopyCounters](../5C/KiCopyCounters_function_005C0710.md) (function, `0x005C0710`)
- `0x006C50DA` → [KiRestoreDebugRegisterState](../4F/KiRestoreDebugRegisterState_function_004FD8E0.md) (function, `0x004FD8E0`)
- `0x006C51B0` → [KiSystemCall64 + 0x883](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C52C3`)
- `0x006C51B9` → [KiSystemCall64 + 0x88C](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C52CC`)
- `0x006C51C2` → [KiSystemCall64 + 0x775](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C51B5`)
- `0x006C51CB` → [KiSystemCall64 + 0x77E](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C51BE`)
- `0x006C51D4` → [KiSystemCall64 + 0x787](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C51C7`)
- `0x006C51DD` → [KiSystemCall64 + 0x790](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C51D0`)
- `0x006C51E6` → [KiSystemCall64 + 0x799](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C51D9`)
- `0x006C51EF` → [KiSystemCall64 + 0x7A2](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C51E2`)
- `0x006C51F8` → [KiSystemCall64 + 0x7AB](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C51EB`)
- `0x006C5201` → [KiSystemCall64 + 0x7B4](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C51F4`)
- `0x006C520A` → [KiSystemCall64 + 0x7BD](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C51FD`)
- `0x006C5213` → [KiSystemCall64 + 0x7C6](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C5206`)
- `0x006C521C` → [KiSystemCall64 + 0x7CF](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C520F`)
- `0x006C5225` → [KiSystemCall64 + 0x7D8](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C5218`)
- `0x006C522E` → [KiSystemCall64 + 0x7E1](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C5221`)
- `0x006C5237` → [KiSystemCall64 + 0x7EA](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C522A`)
- `0x006C5240` → [KiSystemCall64 + 0x7F3](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C5233`)
- `0x006C5249` → [KiSystemCall64 + 0x7FC](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C523C`)
- `0x006C5252` → [KiSystemCall64 + 0x805](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C5245`)
- `0x006C525B` → [KiSystemCall64 + 0x80E](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C524E`)
- `0x006C5264` → [KiSystemCall64 + 0x817](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C5257`)
- `0x006C526D` → [KiSystemCall64 + 0x820](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C5260`)
- `0x006C5276` → [KiSystemCall64 + 0x829](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C5269`)
- `0x006C527F` → [KiSystemCall64 + 0x832](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C5272`)
- `0x006C5288` → [KiSystemCall64 + 0x83B](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C527B`)
- `0x006C5291` → [KiSystemCall64 + 0x844](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C5284`)
- `0x006C529A` → [KiSystemCall64 + 0x84D](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C528D`)
- `0x006C52A3` → [KiSystemCall64 + 0x856](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C5296`)
- `0x006C52AC` → [KiSystemCall64 + 0x85F](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C529F`)
- `0x006C52B5` → [KiSystemCall64 + 0x868](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C52A8`)
- `0x006C52BE` → [KiSystemCall64 + 0x871](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C52B1`)
- `0x006C52C7` → [KiSystemCall64 + 0x87A](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C52BA`)
- `0x006C53FA` → [KiInitiateUserApc](../6B/KiInitiateUserApc_function_006B6540.md) (function, `0x006B6540`)
- `0x006C5418` → [KiUpdateStibpPairing](../3E/KiUpdateStibpPairing_function_003E71C0.md) (function, `0x003E71C0`)
- `0x006C542E` → [KiRestoreSetContextState](../6B/KiRestoreSetContextState_function_006B1CA0.md) (function, `0x006B1CA0`)
- `0x006C5442` → [KiCopyCounters](../5C/KiCopyCounters_function_005C0710.md) (function, `0x005C0710`)
- `0x006C545A` → [KiRestoreDebugRegisterState](../4F/KiRestoreDebugRegisterState_function_004FD8E0.md) (function, `0x004FD8E0`)
- `0x006C54F4` → [KiSystemCall64 + 0xBC7](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C5607`)
- `0x006C54FD` → [KiSystemCall64 + 0xBD0](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C5610`)
- `0x006C5506` → [KiSystemCall64 + 0xAB9](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C54F9`)
- `0x006C550F` → [KiSystemCall64 + 0xAC2](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C5502`)
- `0x006C5518` → [KiSystemCall64 + 0xACB](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C550B`)
- `0x006C5521` → [KiSystemCall64 + 0xAD4](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C5514`)
- `0x006C552A` → [KiSystemCall64 + 0xADD](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C551D`)
- `0x006C5533` → [KiSystemCall64 + 0xAE6](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C5526`)
- `0x006C553C` → [KiSystemCall64 + 0xAEF](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C552F`)
- `0x006C5545` → [KiSystemCall64 + 0xAF8](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C5538`)
- `0x006C554E` → [KiSystemCall64 + 0xB01](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C5541`)
- `0x006C5557` → [KiSystemCall64 + 0xB0A](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C554A`)
- `0x006C5560` → [KiSystemCall64 + 0xB13](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C5553`)
- `0x006C5569` → [KiSystemCall64 + 0xB1C](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C555C`)
- `0x006C5572` → [KiSystemCall64 + 0xB25](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C5565`)
- `0x006C557B` → [KiSystemCall64 + 0xB2E](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C556E`)
- `0x006C5584` → [KiSystemCall64 + 0xB37](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C5577`)
- `0x006C558D` → [KiSystemCall64 + 0xB40](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C5580`)
- `0x006C5596` → [KiSystemCall64 + 0xB49](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C5589`)
- `0x006C559F` → [KiSystemCall64 + 0xB52](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C5592`)
- `0x006C55A8` → [KiSystemCall64 + 0xB5B](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C559B`)
- `0x006C55B1` → [KiSystemCall64 + 0xB64](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C55A4`)
- `0x006C55BA` → [KiSystemCall64 + 0xB6D](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C55AD`)
- `0x006C55C3` → [KiSystemCall64 + 0xB76](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C55B6`)
- `0x006C55CC` → [KiSystemCall64 + 0xB7F](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C55BF`)
- `0x006C55D5` → [KiSystemCall64 + 0xB88](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C55C8`)
- `0x006C55DE` → [KiSystemCall64 + 0xB91](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C55D1`)
- `0x006C55E7` → [KiSystemCall64 + 0xB9A](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C55DA`)
- `0x006C55F0` → [KiSystemCall64 + 0xBA3](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C55E3`)
- `0x006C55F9` → [KiSystemCall64 + 0xBAC](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C55EC`)
- `0x006C5602` → [KiSystemCall64 + 0xBB5](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C55F5`)
- `0x006C560B` → [KiSystemCall64 + 0xBBE](KiSystemCall64_function_006C4A40.md) (inside-function, `0x006C55FE`)
- `0x006C56DF` → [KiConvertToGuiThread](../6B/KiConvertToGuiThread_function_006B3290.md) (function, `0x006B3290`)
- `0x006C5760` → [KiBugCheckDispatch](KiBugCheckDispatch_function_006C5880.md) (function, `0x006C5880`)
- `0x006C5780` → [KiBugCheckDispatch](KiBugCheckDispatch_function_006C5880.md) (function, `0x006C5880`)
- `0x006C57BB` → [KiTrackSystemCallEntry](../../page/74/KiTrackSystemCallEntry_function_00747D40.md) (function, `0x00747D40`)
- `0x006C57E4` → `indirect target` (indirect, 간접 대상)
- `0x006C57F0` → [KiTrackSystemCallExit](../../page/74/KiTrackSystemCallExit_function_00747E60.md) (function, `0x00747E60`)
- `0x006C581A` → [PerfInfoLogSysCallEntry](../22/PerfInfoLogSysCallEntry_function_002255C0.md) (function, `0x002255C0`)
- `0x006C583F` → `indirect target` (indirect, 간접 대상)
- `0x006C5847` → [PerfInfoLogSysCallExit](../22/PerfInfoLogSysCallExit_function_00225470.md) (function, `0x00225470`)

### Direct callers
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C4B67`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C4B70`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C4B79`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C4B82`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C4B8B`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C4B94`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C4B9D`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C4BA6`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C4BAF`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C4BB8`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C4BC1`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C4BCA`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C4BD3`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C4BDC`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C4BE5`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C4BEE`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C4BF7`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C4C00`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C4C09`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C4C12`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C4C1B`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C4C24`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C4C2D`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C4C36`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C4C3F`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C4C48`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C4C51`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C4C5A`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C4C63`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C4C6C`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C4C75`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C4C7E`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C51B0`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C51B9`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C51C2`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C51CB`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C51D4`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C51DD`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C51E6`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C51EF`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C51F8`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C5201`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C520A`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C5213`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C521C`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C5225`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C522E`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C5237`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C5240`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C5249`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C5252`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C525B`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C5264`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C526D`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C5276`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C527F`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C5288`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C5291`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C529A`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C52A3`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C52AC`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C52B5`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C52BE`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C52C7`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C54F4`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C54FD`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C5506`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C550F`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C5518`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C5521`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C552A`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C5533`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C553C`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C5545`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C554E`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C5557`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C5560`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C5569`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C5572`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C557B`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C5584`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C558D`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C5596`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C559F`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C55A8`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C55B1`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C55BA`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C55C3`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C55CC`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C55D5`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C55DE`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C55E7`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C55F0`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C55F9`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C5602`
- [KiSystemCall64](KiSystemCall64_function_006C4A40.md) at `0x006C560B`

### Static image references
- `0x006C4AAA` → RVA `0x00FC6BF0` (`ALMOSTRO`; read)
- `0x006C4CBA` → RVA `0x00FC7264` (`ALMOSTRO`; read)
- `0x006C4DD4` → RVA `0x012018C0` (`CFGRO`; read)
- `0x006C4DDB` → RVA `0x00FC7280` (`ALMOSTRO`; read)
- `0x006C4DF4` → RVA `0x00FC73C0` (`ALMOSTRO`; read)
- `0x006C4E9A` → RVA `0x0003AF68` (`.rdata`; read)
- `0x006C4EB0` → RVA `0x006C4F30` (`KiSystemServiceCopyEnd`; read)
- `0x006C4F30` → RVA `0x00FC6D00` (`ALMOSTRO`; read)
- `0x006C4F40` → RVA `0x00FC6B08` (`ALMOSTRO`; read)
- `0x006C533A` → RVA `0x01201840` (`CFGRO`; read)
- `0x006C5706` → RVA `0x00FC72A0` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x006C4D66` → [PsSyscallProviderDispatch](../../page/AB/PsSyscallProviderDispatch_function_00AB3D80.md) (`.text` → `PAGE`)
  - `0x006C4E53` → [PsInvokeWin32Callout](../../page/91/PsInvokeWin32Callout_function_009133C0.md) (`.text` → `PAGE`)
  - `0x006C57BB` → [KiTrackSystemCallEntry](../../page/74/KiTrackSystemCallEntry_function_00747D40.md) (`.text` → `PAGE`)
  - `0x006C57F0` → [KiTrackSystemCallExit](../../page/74/KiTrackSystemCallExit_function_00747E60.md) (`.text` → `PAGE`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x006C5341` → [KiKernelSysretExit](../../kvascode/BC/KiKernelSysretExit_function_00BCCDC0.md) (`tail-transfer`)
  - `0x006C56AB` → [KiKernelExit](../../kvascode/BC/KiKernelExit_function_00BCCB80.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006C4A40  0F 01 F8                        swapgs
006C4A43  65 48 89 24 25 10 00 00 00      mov qword ptr gs:[0x10], rsp
006C4A4C  65 48 8B 24 25 A8 01 00 00      mov rsp, qword ptr gs:[0x1a8]
006C4A55  6A 2B                           push 0x2b
006C4A57  65 FF 34 25 10 00 00 00         push qword ptr gs:[0x10]
006C4A5F  41 53                           push r11
006C4A61  6A 33                           push 0x33
006C4A63  51                              push rcx
006C4A64  65 48 8B 0C 25 28 9D 00 00      mov rcx, qword ptr gs:[0x9d28]
006C4A6D  48 85 C9                        test rcx, rcx
006C4A70  74 0C                           je 0x1406c4a7e
006C4A72  F3 0F 01 E8                     setssbsy
006C4A76  F3 0F 01 29                     rstorssp dword ptr [rcx]
006C4A7A  F3 0F 01 EA                     saveprevssp
006C4A7E  49 8B CA                        mov rcx, r10
006C4A81  48 83 EC 08                     sub rsp, 8
006C4A85  55                              push rbp
006C4A86  48 81 EC 58 01 00 00            sub rsp, 0x158
006C4A8D  48 8D AC 24 80 00 00 00         lea rbp, [rsp + 0x80]
006C4A95  48 89 9D C0 00 00 00            mov qword ptr [rbp + 0xc0], rbx
006C4A9C  48 89 BD C8 00 00 00            mov qword ptr [rbp + 0xc8], rdi
006C4AA3  48 89 B5 D0 00 00 00            mov qword ptr [rbp + 0xd0], rsi
006C4AAA  F6 05 3F 21 90 00 FF            test byte ptr [rip + 0x90213f], 0xff
006C4AB1  74 0C                           je 0x1406c4abf
006C4AB3  F6 85 F0 00 00 00 01            test byte ptr [rbp + 0xf0], 1
006C4ABA  74 03                           je 0x1406c4abf
006C4ABC  0F 01 CB                        stac
006C4ABF  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
006C4AC3  48 89 4D B8                     mov qword ptr [rbp - 0x48], rcx
006C4AC7  48 89 55 C0                     mov qword ptr [rbp - 0x40], rdx
006C4ACB  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006C4AD4  48 8B 89 20 02 00 00            mov rcx, qword ptr [rcx + 0x220]
006C4ADB  48 8B 89 60 07 00 00            mov rcx, qword ptr [rcx + 0x760]
006C4AE2  65 48 89 0C 25 50 08 00 00      mov qword ptr gs:[0x850], rcx
006C4AEB  66 65 8B 0C 25 62 08 00 00      mov cx, word ptr gs:[0x862]
006C4AF4  66 65 89 0C 25 64 08 00 00      mov word ptr gs:[0x864], cx
006C4AFD  65 8A 0C 25 58 08 00 00         mov cl, byte ptr gs:[0x858]
006C4B05  65 88 0C 25 5A 08 00 00         mov byte ptr gs:[0x85a], cl
006C4B0D  65 0F B7 04 25 68 08 00 00      movzx eax, word ptr gs:[0x868]
006C4B16  66 65 39 04 25 66 08 00 00      cmp word ptr gs:[0x866], ax
006C4B1F  74 12                           je 0x1406c4b33
006C4B21  66 65 89 04 25 66 08 00 00      mov word ptr gs:[0x866], ax
006C4B2A  B9 48 00 00 00                  mov ecx, 0x48
006C4B2F  33 D2                           xor edx, edx
006C4B31  0F 30                           wrmsr
006C4B33  65 0F B6 14 25 58 08 00 00      movzx edx, byte ptr gs:[0x858]
006C4B3C  F7 C2 08 00 00 00               test edx, 8
006C4B42  74 17                           je 0x1406c4b5b
006C4B44  B8 01 00 00 00                  mov eax, 1
006C4B49  33 D2                           xor edx, edx
006C4B4B  B9 49 00 00 00                  mov ecx, 0x49
006C4B50  0F 30                           wrmsr
006C4B52  65 0F B6 14 25 58 08 00 00      movzx edx, byte ptr gs:[0x858]
006C4B5B  F7 C2 02 00 00 00               test edx, 2
006C4B61  0F 84 37 01 00 00               je 0x1406c4c9e
006C4B67  E8 0E 01 00 00                  call 0x1406c4c7a
006C4B6C  48 83 C4 08                     add rsp, 8
006C4B70  E8 0E 01 00 00                  call 0x1406c4c83
006C4B75  48 83 C4 08                     add rsp, 8
006C4B79  E8 EE FF FF FF                  call 0x1406c4b6c
006C4B7E  48 83 C4 08                     add rsp, 8
006C4B82  E8 EE FF FF FF                  call 0x1406c4b75
006C4B87  48 83 C4 08                     add rsp, 8
006C4B8B  E8 EE FF FF FF                  call 0x1406c4b7e
006C4B90  48 83 C4 08                     add rsp, 8
006C4B94  E8 EE FF FF FF                  call 0x1406c4b87
006C4B99  48 83 C4 08                     add rsp, 8
006C4B9D  E8 EE FF FF FF                  call 0x1406c4b90
006C4BA2  48 83 C4 08                     add rsp, 8
006C4BA6  E8 EE FF FF FF                  call 0x1406c4b99
006C4BAB  48 83 C4 08                     add rsp, 8
006C4BAF  E8 EE FF FF FF                  call 0x1406c4ba2
006C4BB4  48 83 C4 08                     add rsp, 8
006C4BB8  E8 EE FF FF FF                  call 0x1406c4bab
006C4BBD  48 83 C4 08                     add rsp, 8
006C4BC1  E8 EE FF FF FF                  call 0x1406c4bb4
006C4BC6  48 83 C4 08                     add rsp, 8
006C4BCA  E8 EE FF FF FF                  call 0x1406c4bbd
006C4BCF  48 83 C4 08                     add rsp, 8
006C4BD3  E8 EE FF FF FF                  call 0x1406c4bc6
006C4BD8  48 83 C4 08                     add rsp, 8
006C4BDC  E8 EE FF FF FF                  call 0x1406c4bcf
006C4BE1  48 83 C4 08                     add rsp, 8
006C4BE5  E8 EE FF FF FF                  call 0x1406c4bd8
006C4BEA  48 83 C4 08                     add rsp, 8
006C4BEE  E8 EE FF FF FF                  call 0x1406c4be1
006C4BF3  48 83 C4 08                     add rsp, 8
006C4BF7  E8 EE FF FF FF                  call 0x1406c4bea
006C4BFC  48 83 C4 08                     add rsp, 8
006C4C00  E8 EE FF FF FF                  call 0x1406c4bf3
006C4C05  48 83 C4 08                     add rsp, 8
006C4C09  E8 EE FF FF FF                  call 0x1406c4bfc
006C4C0E  48 83 C4 08                     add rsp, 8
006C4C12  E8 EE FF FF FF                  call 0x1406c4c05
006C4C17  48 83 C4 08                     add rsp, 8
006C4C1B  E8 EE FF FF FF                  call 0x1406c4c0e
006C4C20  48 83 C4 08                     add rsp, 8
006C4C24  E8 EE FF FF FF                  call 0x1406c4c17
006C4C29  48 83 C4 08                     add rsp, 8
006C4C2D  E8 EE FF FF FF                  call 0x1406c4c20
006C4C32  48 83 C4 08                     add rsp, 8
006C4C36  E8 EE FF FF FF                  call 0x1406c4c29
006C4C3B  48 83 C4 08                     add rsp, 8
006C4C3F  E8 EE FF FF FF                  call 0x1406c4c32
006C4C44  48 83 C4 08                     add rsp, 8
006C4C48  E8 EE FF FF FF                  call 0x1406c4c3b
006C4C4D  48 83 C4 08                     add rsp, 8
006C4C51  E8 EE FF FF FF                  call 0x1406c4c44
006C4C56  48 83 C4 08                     add rsp, 8
006C4C5A  E8 EE FF FF FF                  call 0x1406c4c4d
006C4C5F  48 83 C4 08                     add rsp, 8
006C4C63  E8 EE FF FF FF                  call 0x1406c4c56
006C4C68  48 83 C4 08                     add rsp, 8
006C4C6C  E8 EE FF FF FF                  call 0x1406c4c5f
006C4C71  48 83 C4 08                     add rsp, 8
006C4C75  E8 EE FF FF FF                  call 0x1406c4c68
006C4C7A  48 83 C4 08                     add rsp, 8
006C4C7E  E8 EE FF FF FF                  call 0x1406c4c71
006C4C83  48 83 C4 08                     add rsp, 8
006C4C87  B8 DA DA 00 00                  mov eax, 0xdada
006C4C8C  65 F6 04 25 5C 08 00 00 08      test byte ptr gs:[0x85c], 8
006C4C95  74 07                           je 0x1406c4c9e
006C4C97  B0 20                           mov al, 0x20
006C4C99  F3 48 0F AE E8                  incsspq rax
006C4C9E  F7 C2 80 00 00 00               test edx, 0x80
006C4CA4  74 08                           je 0x1406c4cae
006C4CA6  0F AE E8                        lfence
006C4CA9  E8 92 16 00 00                  call 0x1406c6340
006C4CAE  0F AE E8                        lfence
006C4CB1  65 C6 04 25 5E 08 00 00 00      mov byte ptr gs:[0x85e], 0
006C4CBA  83 3D A3 25 90 00 00            cmp dword ptr [rip + 0x9025a3], 0
006C4CC1  74 1F                           je 0x1406c4ce2
006C4CC3  B9 A7 06 00 00                  mov ecx, 0x6a7
006C4CC8  0F 32                           rdmsr
006C4CCA  83 FA 00                        cmp edx, 0
006C4CCD  74 13                           je 0x1406c4ce2
006C4CCF  8B CA                           mov ecx, edx
006C4CD1  23 15 8D 25 90 00               and edx, dword ptr [rip + 0x90258d]
006C4CD7  3B D1                           cmp edx, ecx
006C4CD9  74 07                           je 0x1406c4ce2
006C4CDB  B9 A7 06 00 00                  mov ecx, 0x6a7
006C4CE0  0F 30                           wrmsr
006C4CE2  C6 45 AB 02                     mov byte ptr [rbp - 0x55], 2
006C4CE6  C6 45 A8 01                     mov byte ptr [rbp - 0x58], 1
006C4CEA  65 48 8B 1C 25 88 01 00 00      mov rbx, qword ptr gs:[0x188]
006C4CF3  C6 83 32 02 00 00 01            mov byte ptr [rbx + 0x232], 1
006C4CFA  0F 0D 8B 90 00 00 00            prefetchw byte ptr [rbx + 0x90]
006C4D01  0F AE 5D AC                     stmxcsr dword ptr [rbp - 0x54]
006C4D05  65 0F AE 14 25 80 01 00 00      ldmxcsr dword ptr gs:[0x180]
006C4D0E  4C 89 45 C8                     mov qword ptr [rbp - 0x38], r8
006C4D12  4C 89 4D D0                     mov qword ptr [rbp - 0x30], r9
006C4D16  4C 89 55 E0                     mov qword ptr [rbp - 0x20], r10
006C4D1A  4C 89 55 D8                     mov qword ptr [rbp - 0x28], r10
006C4D1E  0F 29 45 F0                     movaps xmmword ptr [rbp - 0x10], xmm0
006C4D22  0F 29 4D 00                     movaps xmmword ptr [rbp], xmm1
006C4D26  0F 29 55 10                     movaps xmmword ptr [rbp + 0x10], xmm2
006C4D2A  0F 29 5D 20                     movaps xmmword ptr [rbp + 0x20], xmm3
006C4D2E  0F 29 65 30                     movaps xmmword ptr [rbp + 0x30], xmm4
006C4D32  0F 29 6D 40                     movaps xmmword ptr [rbp + 0x40], xmm5
006C4D36  E8 65 72 D5 FF                  call 0x14041bfa0
006C4D3B  80 7B 03 00                     cmp byte ptr [rbx + 3], 0
006C4D3F  66 C7 85 80 00 00 00 00 00      mov word ptr [rbp + 0x80], 0
006C4D48  74 4E                           je 0x1406c4d98
006C4D4A  F6 43 03 03                     test byte ptr [rbx + 3], 3
006C4D4E  74 05                           je 0x1406c4d55
006C4D50  E8 0B 8C E3 FF                  call 0x1404fd960
006C4D55  F6 43 03 24                     test byte ptr [rbx + 3], 0x24
006C4D59  74 3D                           je 0x1406c4d98
006C4D5B  FB                              sti
006C4D5C  48 89 A3 90 00 00 00            mov qword ptr [rbx + 0x90], rsp
006C4D63  48 8B CC                        mov rcx, rsp
006C4D66  E8 15 F0 3E 00                  call 0x140ab3d80
006C4D6B  3C 01                           cmp al, 1
006C4D6D  74 29                           je 0x1406c4d98
006C4D6F  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
006C4D73  7C 14                           jl 0x1406c4d89
006C4D75  B9 1C 00 00 C0                  mov ecx, 0xc000001c
006C4D7A  33 D2                           xor edx, edx
006C4D7C  4C 8B 85 E8 00 00 00            mov r8, qword ptr [rbp + 0xe8]
006C4D83  E8 78 0B 00 00                  call 0x1406c5900
006C4D88  CC                              int3
006C4D89  F6 43 03 04                     test byte ptr [rbx + 3], 4
006C4D8D  0F 84 CD 01 00 00               je 0x1406c4f60
006C4D93  E9 13 06 00 00                  jmp 0x1406c53ab
006C4D98  4C 8B 45 C8                     mov r8, qword ptr [rbp - 0x38]
006C4D9C  4C 8B 4D D0                     mov r9, qword ptr [rbp - 0x30]
006C4DA0  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
006C4DA4  48 8B 4D B8                     mov rcx, qword ptr [rbp - 0x48]
006C4DA8  48 8B 55 C0                     mov rdx, qword ptr [rbp - 0x40]
006C4DAC  FB                              sti
006C4DAD  48 89 8B 88 00 00 00            mov qword ptr [rbx + 0x88], rcx
006C4DB4  89 83 80 00 00 00               mov dword ptr [rbx + 0x80], eax
006C4DBA  66 0F 1F 44 00 00               nop word ptr [rax + rax]
006C4DC0  48 89 A3 90 00 00 00            mov qword ptr [rbx + 0x90], rsp
006C4DC7  8B F8                           mov edi, eax
006C4DC9  C1 EF 07                        shr edi, 7
006C4DCC  83 E7 20                        and edi, 0x20
006C4DCF  25 FF 0F 00 00                  and eax, 0xfff
006C4DD4  4C 8D 15 E5 CA B3 00            lea r10, [rip + 0xb3cae5]
006C4DDB  4C 8D 1D 9E 24 90 00            lea r11, [rip + 0x90249e]
006C4DE2  F7 43 78 80 00 00 00            test dword ptr [rbx + 0x78], 0x80
006C4DE9  74 13                           je 0x1406c4dfe
006C4DEB  F7 43 78 00 00 20 00            test dword ptr [rbx + 0x78], 0x200000
006C4DF2  74 07                           je 0x1406c4dfb
006C4DF4  4C 8D 1D C5 25 90 00            lea r11, [rip + 0x9025c5]
006C4DFB  4D 8B D3                        mov r10, r11
006C4DFE  41 3B 44 3A 10                  cmp eax, dword ptr [r10 + rdi + 0x10]
006C4E03  0F 83 BE 08 00 00               jae 0x1406c56c7
006C4E09  4D 8B 14 3A                     mov r10, qword ptr [r10 + rdi]
006C4E0D  4D 63 1C 82                     movsxd r11, dword ptr [r10 + rax*4]
006C4E11  49 8B C3                        mov rax, r11
006C4E14  49 C1 FB 04                     sar r11, 4
006C4E18  4D 03 D3                        add r10, r11
006C4E1B  83 FF 20                        cmp edi, 0x20
006C4E1E  75 50                           jne 0x1406c4e70
006C4E20  4C 8B 9B F0 00 00 00            mov r11, qword ptr [rbx + 0xf0]
006C4E27  41 83 BB 40 17 00 00 00         cmp dword ptr [r11 + 0x1740], 0
006C4E2F  74 3F                           je 0x1406c4e70
006C4E31  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
006C4E35  48 89 4D B8                     mov qword ptr [rbp - 0x48], rcx
006C4E39  48 89 55 C0                     mov qword ptr [rbp - 0x40], rdx
006C4E3D  49 8B D8                        mov rbx, r8
006C4E40  49 8B F9                        mov rdi, r9
006C4E43  49 8B F2                        mov rsi, r10
006C4E46  B9 07 00 00 00                  mov ecx, 7
006C4E4B  33 D2                           xor edx, edx
006C4E4D  4D 33 C0                        xor r8, r8
006C4E50  4D 33 C9                        xor r9, r9
006C4E53  E8 68 E5 24 00                  call 0x1409133c0
006C4E58  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
006C4E5C  48 8B 4D B8                     mov rcx, qword ptr [rbp - 0x48]
006C4E60  48 8B 55 C0                     mov rdx, qword ptr [rbp - 0x40]
006C4E64  4C 8B C3                        mov r8, rbx
006C4E67  4C 8B CF                        mov r9, rdi
006C4E6A  4C 8B D6                        mov r10, rsi
006C4E6D  0F 1F 00                        nop dword ptr [rax]
006C4E70  83 E0 0F                        and eax, 0xf
006C4E73  0F 84 B7 00 00 00               je 0x1406c4f30
006C4E79  C1 E0 03                        shl eax, 3
006C4E7C  48 8D 64 24 90                  lea rsp, [rsp - 0x70]
006C4E81  48 8D 7C 24 18                  lea rdi, [rsp + 0x18]
006C4E86  48 8B B5 00 01 00 00            mov rsi, qword ptr [rbp + 0x100]
006C4E8D  48 8D 76 20                     lea rsi, [rsi + 0x20]
006C4E91  F6 85 F0 00 00 00 01            test byte ptr [rbp + 0xf0], 1
006C4E98  74 16                           je 0x1406c4eb0
006C4E9A  48 3B 35 C7 60 97 FF            cmp rsi, qword ptr [rip - 0x689f39]
006C4EA1  48 0F 43 35 BF 60 97 FF         cmovae rsi, qword ptr [rip - 0x689f41]
006C4EA9  0F 1F 80 00 00 00 00            nop dword ptr [rax]
006C4EB0  4C 8D 1D 79 00 00 00            lea r11, [rip + 0x79]
006C4EB7  4C 2B D8                        sub r11, rax
006C4EBA  41 FF E3                        jmp r11
006C4EBD  CC                              int3
006C4EBE  CC                              int3
006C4EBF  CC                              int3
006C4EC0  48 8B 46 70                     mov rax, qword ptr [rsi + 0x70]
006C4EC4  48 89 47 70                     mov qword ptr [rdi + 0x70], rax
006C4EC8  48 8B 46 68                     mov rax, qword ptr [rsi + 0x68]
006C4ECC  48 89 47 68                     mov qword ptr [rdi + 0x68], rax
006C4ED0  48 8B 46 60                     mov rax, qword ptr [rsi + 0x60]
006C4ED4  48 89 47 60                     mov qword ptr [rdi + 0x60], rax
006C4ED8  48 8B 46 58                     mov rax, qword ptr [rsi + 0x58]
006C4EDC  48 89 47 58                     mov qword ptr [rdi + 0x58], rax
006C4EE0  48 8B 46 50                     mov rax, qword ptr [rsi + 0x50]
006C4EE4  48 89 47 50                     mov qword ptr [rdi + 0x50], rax
006C4EE8  48 8B 46 48                     mov rax, qword ptr [rsi + 0x48]
006C4EEC  48 89 47 48                     mov qword ptr [rdi + 0x48], rax
006C4EF0  48 8B 46 40                     mov rax, qword ptr [rsi + 0x40]
006C4EF4  48 89 47 40                     mov qword ptr [rdi + 0x40], rax
006C4EF8  48 8B 46 38                     mov rax, qword ptr [rsi + 0x38]
006C4EFC  48 89 47 38                     mov qword ptr [rdi + 0x38], rax
006C4F00  48 8B 46 30                     mov rax, qword ptr [rsi + 0x30]
006C4F04  48 89 47 30                     mov qword ptr [rdi + 0x30], rax
006C4F08  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
006C4F0C  48 89 47 28                     mov qword ptr [rdi + 0x28], rax
006C4F10  48 8B 46 20                     mov rax, qword ptr [rsi + 0x20]
006C4F14  48 89 47 20                     mov qword ptr [rdi + 0x20], rax
006C4F18  48 8B 46 18                     mov rax, qword ptr [rsi + 0x18]
006C4F1C  48 89 47 18                     mov qword ptr [rdi + 0x18], rax
006C4F20  48 8B 46 10                     mov rax, qword ptr [rsi + 0x10]
006C4F24  48 89 47 10                     mov qword ptr [rdi + 0x10], rax
006C4F28  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
006C4F2C  48 89 47 08                     mov qword ptr [rdi + 8], rax
006C4F30  F7 05 C6 1D 90 00 01 00 00 00   test dword ptr [rip + 0x901dc6], 1
006C4F3A  0F 85 46 08 00 00               jne 0x1406c5786
006C4F40  F7 05 BE 1B 90 00 40 00 00 00   test dword ptr [rip + 0x901bbe], 0x40
006C4F4A  0F 85 AA 08 00 00               jne 0x1406c57fa
006C4F50  49 8B C2                        mov rax, r10
006C4F53  FF D0                           call rax
006C4F55  0F 1F 00                        nop dword ptr [rax]
006C4F58  65 FF 04 25 B8 2E 00 00         inc dword ptr gs:[0x2eb8]
006C4F60  48 8B 9D C0 00 00 00            mov rbx, qword ptr [rbp + 0xc0]
006C4F67  48 8B BD C8 00 00 00            mov rdi, qword ptr [rbp + 0xc8]
006C4F6E  48 8B B5 D0 00 00 00            mov rsi, qword ptr [rbp + 0xd0]
006C4F75  65 4C 8B 1C 25 88 01 00 00      mov r11, qword ptr gs:[0x188]
006C4F7E  F6 85 F0 00 00 00 01            test byte ptr [rbp + 0xf0], 1
006C4F85  0F 84 F3 03 00 00               je 0x1406c537e
006C4F8B  44 0F 20 C1                     mov rcx, cr8
006C4F8F  41 0A 8B 4A 02 00 00            or cl, byte ptr [r11 + 0x24a]
006C4F96  41 0B 8B E4 01 00 00            or ecx, dword ptr [r11 + 0x1e4]
006C4F9D  0F 85 8E 07 00 00               jne 0x1406c5731
006C4FA3  41 80 BB 32 02 00 00 01         cmp byte ptr [r11 + 0x232], 1
006C4FAB  0F 85 B5 07 00 00               jne 0x1406c5766
006C4FB1  FA                              cli
006C4FB2  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006C4FBB  F6 81 C2 00 00 00 03            test byte ptr [rcx + 0xc2], 3
006C4FC2  74 59                           je 0x1406c501d
006C4FC4  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
006C4FC8  33 C0                           xor eax, eax
006C4FCA  48 89 45 B8                     mov qword ptr [rbp - 0x48], rax
006C4FCE  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
006C4FD2  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
006C4FD6  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
006C4FDA  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
006C4FDE  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
006C4FE2  66 0F EF C0                     pxor xmm0, xmm0
006C4FE6  0F 29 45 F0                     movaps xmmword ptr [rbp - 0x10], xmm0
006C4FEA  0F 29 45 00                     movaps xmmword ptr [rbp], xmm0
006C4FEE  0F 29 45 10                     movaps xmmword ptr [rbp + 0x10], xmm0
006C4FF2  0F 29 45 20                     movaps xmmword ptr [rbp + 0x20], xmm0
006C4FF6  0F 29 45 30                     movaps xmmword ptr [rbp + 0x30], xmm0
006C4FFA  0F 29 45 40                     movaps xmmword ptr [rbp + 0x40], xmm0
006C4FFE  B9 01 00 00 00                  mov ecx, 1
006C5003  44 0F 22 C1                     mov cr8, rcx
006C5007  FB                              sti
006C5008  E8 33 15 FF FF                  call 0x1406b6540
006C500D  FA                              cli
006C500E  B9 00 00 00 00                  mov ecx, 0
006C5013  44 0F 22 C1                     mov cr8, rcx
006C5017  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
006C501B  EB 95                           jmp 0x1406c4fb2
006C501D  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
006C5021  E8 3A EF B9 FF                  call 0x140263f60
006C5026  85 C0                           test eax, eax
006C5028  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
006C502C  75 84                           jne 0x1406c4fb2
006C502E  65 F6 04 25 60 08 00 00 02      test byte ptr gs:[0x860], 2
006C5037  74 0F                           je 0x1406c5048
006C5039  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
006C503D  33 C9                           xor ecx, ecx
006C503F  E8 7C 21 D2 FF                  call 0x1403e71c0
006C5044  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
006C5048  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006C5051  F7 01 00 00 00 08               test dword ptr [rcx], 0x8000000
006C5057  74 3F                           je 0x1406c5098
006C5059  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
006C505D  33 C0                           xor eax, eax
006C505F  48 89 45 B8                     mov qword ptr [rbp - 0x48], rax
006C5063  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
006C5067  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
006C506B  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
006C506F  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
006C5073  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
006C5077  66 0F EF C0                     pxor xmm0, xmm0
006C507B  0F 29 45 F0                     movaps xmmword ptr [rbp - 0x10], xmm0
006C507F  0F 29 45 00                     movaps xmmword ptr [rbp], xmm0
006C5083  0F 29 45 10                     movaps xmmword ptr [rbp + 0x10], xmm0
006C5087  0F 29 45 20                     movaps xmmword ptr [rbp + 0x20], xmm0
006C508B  0F 29 45 30                     movaps xmmword ptr [rbp + 0x30], xmm0
006C508F  0F 29 45 40                     movaps xmmword ptr [rbp + 0x40], xmm0
006C5093  E8 08 CC FE FF                  call 0x1406b1ca0
006C5098  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006C50A1  F7 01 00 00 01 00               test dword ptr [rcx], 0x10000
006C50A7  74 1C                           je 0x1406c50c5
006C50A9  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
006C50AD  F6 41 02 01                     test byte ptr [rcx + 2], 1
006C50B1  74 0E                           je 0x1406c50c1
006C50B3  E8 58 B6 EF FF                  call 0x1405c0710
006C50B8  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006C50C1  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
006C50C5  0F AE 55 AC                     ldmxcsr dword ptr [rbp - 0x54]
006C50C9  4D 33 D2                        xor r10, r10
006C50CC  66 83 BD 80 00 00 00 00         cmp word ptr [rbp + 0x80], 0
006C50D4  74 41                           je 0x1406c5117
006C50D6  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
006C50DA  E8 01 88 E3 FF                  call 0x1404fd8e0
006C50DF  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
006C50E8  48 8B 80 B8 00 00 00            mov rax, qword ptr [rax + 0xb8]
006C50EF  48 8B 80 68 01 00 00            mov rax, qword ptr [rax + 0x168]
006C50F6  48 0B C0                        or rax, rax
006C50F9  74 18                           je 0x1406c5113
006C50FB  66 83 BD F0 00 00 00 33         cmp word ptr [rbp + 0xf0], 0x33
006C5103  75 0E                           jne 0x1406c5113
006C5105  4C 8B 95 E8 00 00 00            mov r10, qword ptr [rbp + 0xe8]
006C510C  48 89 85 E8 00 00 00            mov qword ptr [rbp + 0xe8], rax
006C5113  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
006C5117  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006C5120  0F BA 61 74 16                  bt dword ptr [rcx + 0x74], 0x16
006C5125  73 2A                           jae 0x1406c5151
006C5127  33 C9                           xor ecx, ecx
006C5129  F3 48 0F 1E C9                  rdsspq rcx
006C512E  65 4C 8B 04 25 28 9D 00 00      mov r8, qword ptr gs:[0x9d28]
006C5137  49 83 C0 08                     add r8, 8
006C513B  49 3B C8                        cmp rcx, r8
006C513E  75 11                           jne 0x1406c5151
006C5140  65 48 8B 0C 25 20 9D 00 00      mov rcx, qword ptr gs:[0x9d20]
006C5149  F3 0F 01 29                     rstorssp dword ptr [rcx]
006C514D  F3 0F 01 EA                     saveprevssp
006C5151  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
006C5155  65 C6 04 25 5E 08 00 00 00      mov byte ptr gs:[0x85e], 0
006C515E  65 0F B7 04 25 6C 08 00 00      movzx eax, word ptr gs:[0x86c]
006C5167  66 65 39 04 25 66 08 00 00      cmp word ptr gs:[0x866], ax
006C5170  74 12                           je 0x1406c5184
006C5172  66 65 89 04 25 66 08 00 00      mov word ptr gs:[0x866], ax
006C517B  B9 48 00 00 00                  mov ecx, 0x48
006C5180  33 D2                           xor edx, edx
006C5182  0F 30                           wrmsr
006C5184  66 65 0F BA 34 25 58 08 00 00 02  btr word ptr gs:[0x858], 2
006C518F  73 0E                           jae 0x1406c519f
006C5191  B8 01 00 00 00                  mov eax, 1
006C5196  33 D2                           xor edx, edx
006C5198  B9 49 00 00 00                  mov ecx, 0x49
006C519D  0F 30                           wrmsr
006C519F  66 65 0F BA 34 25 58 08 00 00 05  btr word ptr gs:[0x858], 5
006C51AA  0F 83 37 01 00 00               jae 0x1406c52e7
006C51B0  E8 0E 01 00 00                  call 0x1406c52c3
006C51B5  48 83 C4 08                     add rsp, 8
006C51B9  E8 0E 01 00 00                  call 0x1406c52cc
006C51BE  48 83 C4 08                     add rsp, 8
006C51C2  E8 EE FF FF FF                  call 0x1406c51b5
006C51C7  48 83 C4 08                     add rsp, 8
006C51CB  E8 EE FF FF FF                  call 0x1406c51be
006C51D0  48 83 C4 08                     add rsp, 8
006C51D4  E8 EE FF FF FF                  call 0x1406c51c7
006C51D9  48 83 C4 08                     add rsp, 8
006C51DD  E8 EE FF FF FF                  call 0x1406c51d0
006C51E2  48 83 C4 08                     add rsp, 8
006C51E6  E8 EE FF FF FF                  call 0x1406c51d9
006C51EB  48 83 C4 08                     add rsp, 8
006C51EF  E8 EE FF FF FF                  call 0x1406c51e2
006C51F4  48 83 C4 08                     add rsp, 8
006C51F8  E8 EE FF FF FF                  call 0x1406c51eb
006C51FD  48 83 C4 08                     add rsp, 8
006C5201  E8 EE FF FF FF                  call 0x1406c51f4
006C5206  48 83 C4 08                     add rsp, 8
006C520A  E8 EE FF FF FF                  call 0x1406c51fd
006C520F  48 83 C4 08                     add rsp, 8
006C5213  E8 EE FF FF FF                  call 0x1406c5206
006C5218  48 83 C4 08                     add rsp, 8
006C521C  E8 EE FF FF FF                  call 0x1406c520f
006C5221  48 83 C4 08                     add rsp, 8
006C5225  E8 EE FF FF FF                  call 0x1406c5218
006C522A  48 83 C4 08                     add rsp, 8
006C522E  E8 EE FF FF FF                  call 0x1406c5221
006C5233  48 83 C4 08                     add rsp, 8
006C5237  E8 EE FF FF FF                  call 0x1406c522a
006C523C  48 83 C4 08                     add rsp, 8
006C5240  E8 EE FF FF FF                  call 0x1406c5233
006C5245  48 83 C4 08                     add rsp, 8
006C5249  E8 EE FF FF FF                  call 0x1406c523c
006C524E  48 83 C4 08                     add rsp, 8
006C5252  E8 EE FF FF FF                  call 0x1406c5245
006C5257  48 83 C4 08                     add rsp, 8
006C525B  E8 EE FF FF FF                  call 0x1406c524e
006C5260  48 83 C4 08                     add rsp, 8
006C5264  E8 EE FF FF FF                  call 0x1406c5257
006C5269  48 83 C4 08                     add rsp, 8
006C526D  E8 EE FF FF FF                  call 0x1406c5260
006C5272  48 83 C4 08                     add rsp, 8
006C5276  E8 EE FF FF FF                  call 0x1406c5269
006C527B  48 83 C4 08                     add rsp, 8
006C527F  E8 EE FF FF FF                  call 0x1406c5272
006C5284  48 83 C4 08                     add rsp, 8
006C5288  E8 EE FF FF FF                  call 0x1406c527b
006C528D  48 83 C4 08                     add rsp, 8
006C5291  E8 EE FF FF FF                  call 0x1406c5284
006C5296  48 83 C4 08                     add rsp, 8
006C529A  E8 EE FF FF FF                  call 0x1406c528d
006C529F  48 83 C4 08                     add rsp, 8
006C52A3  E8 EE FF FF FF                  call 0x1406c5296
006C52A8  48 83 C4 08                     add rsp, 8
006C52AC  E8 EE FF FF FF                  call 0x1406c529f
006C52B1  48 83 C4 08                     add rsp, 8
006C52B5  E8 EE FF FF FF                  call 0x1406c52a8
006C52BA  48 83 C4 08                     add rsp, 8
006C52BE  E8 EE FF FF FF                  call 0x1406c52b1
006C52C3  48 83 C4 08                     add rsp, 8
006C52C7  E8 EE FF FF FF                  call 0x1406c52ba
006C52CC  48 83 C4 08                     add rsp, 8
006C52D0  B8 DA DA 00 00                  mov eax, 0xdada
006C52D5  65 F6 04 25 5C 08 00 00 08      test byte ptr gs:[0x85c], 8
006C52DE  74 07                           je 0x1406c52e7
006C52E0  B0 20                           mov al, 0x20
006C52E2  F3 48 0F AE E8                  incsspq rax
006C52E7  66 65 F7 04 25 58 08 00 00 00 01  test word ptr gs:[0x858], 0x100
006C52F2  74 0C                           je 0x1406c5300
006C52F4  33 C0                           xor eax, eax
006C52F6  33 D2                           xor edx, edx
006C52F8  B9 01 00 00 00                  mov ecx, 1
006C52FD  48 F7 F1                        div rcx
006C5300  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
006C5304  4C 8B 85 00 01 00 00            mov r8, qword ptr [rbp + 0x100]
006C530B  4C 8B 8D D8 00 00 00            mov r9, qword ptr [rbp + 0xd8]
006C5312  33 D2                           xor edx, edx
006C5314  66 0F EF C0                     pxor xmm0, xmm0
006C5318  66 0F EF C9                     pxor xmm1, xmm1
006C531C  66 0F EF D2                     pxor xmm2, xmm2
006C5320  66 0F EF DB                     pxor xmm3, xmm3
006C5324  66 0F EF E4                     pxor xmm4, xmm4
006C5328  66 0F EF ED                     pxor xmm5, xmm5
006C532C  48 8B 8D E8 00 00 00            mov rcx, qword ptr [rbp + 0xe8]
006C5333  4C 8B 9D F8 00 00 00            mov r11, qword ptr [rbp + 0xf8]
006C533A  F6 05 FF C4 B3 00 01            test byte ptr [rip + 0xb3c4ff], 1
006C5341  0F 85 79 7A 50 00               jne 0x140bccdc0
006C5347  49 8B E9                        mov rbp, r9
006C534A  49 8B E0                        mov rsp, r8
006C534D  4D 33 C9                        xor r9, r9
006C5350  F3 49 0F 1E C9                  rdsspq r9
006C5355  4D 85 C9                        test r9, r9
006C5358  74 08                           je 0x1406c5362
006C535A  F3 41 0F AE 31                  clrssbsy dword ptr [r9]
006C535F  4D 33 C9                        xor r9, r9
006C5362  66 65 F7 04 25 58 08 00 00 00 02  test word ptr gs:[0x858], 0x200
006C536D  74 09                           je 0x1406c5378
006C536F  65 0F 00 2C 25 2A B0 00 00      verw word ptr gs:[0xb02a]
006C5378  0F 01 F8                        swapgs
006C537B  48 0F 07                        sysretq
006C537E  48 8B 95 B8 00 00 00            mov rdx, qword ptr [rbp + 0xb8]
006C5385  49 89 93 90 00 00 00            mov qword ptr [r11 + 0x90], rdx
006C538C  8A 55 A8                        mov dl, byte ptr [rbp - 0x58]
006C538F  41 88 93 32 02 00 00            mov byte ptr [r11 + 0x232], dl
006C5396  FA                              cli
006C5397  48 8B E5                        mov rsp, rbp
006C539A  48 8B AD D8 00 00 00            mov rbp, qword ptr [rbp + 0xd8]
006C53A1  48 8B A4 24 00 01 00 00         mov rsp, qword ptr [rsp + 0x100]
006C53A9  FB                              sti
006C53AA  C3                              ret
006C53AB  65 4C 8B 1C 25 88 01 00 00      mov r11, qword ptr gs:[0x188]
006C53B4  44 0F 20 C1                     mov rcx, cr8
006C53B8  41 0A 8B 4A 02 00 00            or cl, byte ptr [r11 + 0x24a]
006C53BF  41 0B 8B E4 01 00 00            or ecx, dword ptr [r11 + 0x1e4]
006C53C6  0F 85 65 03 00 00               jne 0x1406c5731
006C53CC  80 BB 32 02 00 00 01            cmp byte ptr [rbx + 0x232], 1
006C53D3  0F 85 8D 03 00 00               jne 0x1406c5766
006C53D9  FA                              cli
006C53DA  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
006C53DE  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006C53E7  F6 81 C2 00 00 00 03            test byte ptr [rcx + 0xc2], 3
006C53EE  74 1B                           je 0x1406c540b
006C53F0  B9 01 00 00 00                  mov ecx, 1
006C53F5  44 0F 22 C1                     mov cr8, rcx
006C53F9  FB                              sti
006C53FA  E8 41 11 FF FF                  call 0x1406b6540
006C53FF  B9 00 00 00 00                  mov ecx, 0
006C5404  44 0F 22 C1                     mov cr8, rcx
006C5408  FA                              cli
006C5409  EB D3                           jmp 0x1406c53de
006C540B  65 F6 04 25 60 08 00 00 02      test byte ptr gs:[0x860], 2
006C5414  74 07                           je 0x1406c541d
006C5416  33 C9                           xor ecx, ecx
006C5418  E8 A3 1D D2 FF                  call 0x1403e71c0
006C541D  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006C5426  F7 01 00 00 00 08               test dword ptr [rcx], 0x8000000
006C542C  74 05                           je 0x1406c5433
006C542E  E8 6D C8 FE FF                  call 0x1406b1ca0
006C5433  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006C543C  F6 41 02 01                     test byte ptr [rcx + 2], 1
006C5440  74 0E                           je 0x1406c5450
006C5442  E8 C9 B2 EF FF                  call 0x1405c0710
006C5447  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006C5450  66 83 BD 80 00 00 00 00         cmp word ptr [rbp + 0x80], 0
006C5458  74 05                           je 0x1406c545f
006C545A  E8 81 84 E3 FF                  call 0x1404fd8e0
006C545F  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006C5468  0F BA 61 74 16                  bt dword ptr [rcx + 0x74], 0x16
006C546D  73 2A                           jae 0x1406c5499
006C546F  33 C9                           xor ecx, ecx
006C5471  F3 48 0F 1E C9                  rdsspq rcx
006C5476  65 4C 8B 04 25 28 9D 00 00      mov r8, qword ptr gs:[0x9d28]
006C547F  49 83 C0 08                     add r8, 8
006C5483  49 3B C8                        cmp rcx, r8
006C5486  75 11                           jne 0x1406c5499
006C5488  65 48 8B 0C 25 20 9D 00 00      mov rcx, qword ptr gs:[0x9d20]
006C5491  F3 0F 01 29                     rstorssp dword ptr [rcx]
006C5495  F3 0F 01 EA                     saveprevssp
006C5499  65 C6 04 25 5E 08 00 00 00      mov byte ptr gs:[0x85e], 0
006C54A2  65 0F B7 04 25 6C 08 00 00      movzx eax, word ptr gs:[0x86c]
006C54AB  66 65 39 04 25 66 08 00 00      cmp word ptr gs:[0x866], ax
006C54B4  74 12                           je 0x1406c54c8
006C54B6  66 65 89 04 25 66 08 00 00      mov word ptr gs:[0x866], ax
006C54BF  B9 48 00 00 00                  mov ecx, 0x48
006C54C4  33 D2                           xor edx, edx
006C54C6  0F 30                           wrmsr
006C54C8  66 65 0F BA 34 25 58 08 00 00 02  btr word ptr gs:[0x858], 2
006C54D3  73 0E                           jae 0x1406c54e3
006C54D5  B8 01 00 00 00                  mov eax, 1
006C54DA  33 D2                           xor edx, edx
006C54DC  B9 49 00 00 00                  mov ecx, 0x49
006C54E1  0F 30                           wrmsr
006C54E3  66 65 0F BA 34 25 58 08 00 00 05  btr word ptr gs:[0x858], 5
006C54EE  0F 83 37 01 00 00               jae 0x1406c562b
006C54F4  E8 0E 01 00 00                  call 0x1406c5607
006C54F9  48 83 C4 08                     add rsp, 8
006C54FD  E8 0E 01 00 00                  call 0x1406c5610
006C5502  48 83 C4 08                     add rsp, 8
006C5506  E8 EE FF FF FF                  call 0x1406c54f9
006C550B  48 83 C4 08                     add rsp, 8
006C550F  E8 EE FF FF FF                  call 0x1406c5502
006C5514  48 83 C4 08                     add rsp, 8
006C5518  E8 EE FF FF FF                  call 0x1406c550b
006C551D  48 83 C4 08                     add rsp, 8
006C5521  E8 EE FF FF FF                  call 0x1406c5514
006C5526  48 83 C4 08                     add rsp, 8
006C552A  E8 EE FF FF FF                  call 0x1406c551d
006C552F  48 83 C4 08                     add rsp, 8
006C5533  E8 EE FF FF FF                  call 0x1406c5526
006C5538  48 83 C4 08                     add rsp, 8
006C553C  E8 EE FF FF FF                  call 0x1406c552f
006C5541  48 83 C4 08                     add rsp, 8
006C5545  E8 EE FF FF FF                  call 0x1406c5538
006C554A  48 83 C4 08                     add rsp, 8
006C554E  E8 EE FF FF FF                  call 0x1406c5541
006C5553  48 83 C4 08                     add rsp, 8
006C5557  E8 EE FF FF FF                  call 0x1406c554a
006C555C  48 83 C4 08                     add rsp, 8
006C5560  E8 EE FF FF FF                  call 0x1406c5553
006C5565  48 83 C4 08                     add rsp, 8
006C5569  E8 EE FF FF FF                  call 0x1406c555c
006C556E  48 83 C4 08                     add rsp, 8
006C5572  E8 EE FF FF FF                  call 0x1406c5565
006C5577  48 83 C4 08                     add rsp, 8
006C557B  E8 EE FF FF FF                  call 0x1406c556e
006C5580  48 83 C4 08                     add rsp, 8
006C5584  E8 EE FF FF FF                  call 0x1406c5577
006C5589  48 83 C4 08                     add rsp, 8
006C558D  E8 EE FF FF FF                  call 0x1406c5580
006C5592  48 83 C4 08                     add rsp, 8
006C5596  E8 EE FF FF FF                  call 0x1406c5589
006C559B  48 83 C4 08                     add rsp, 8
006C559F  E8 EE FF FF FF                  call 0x1406c5592
006C55A4  48 83 C4 08                     add rsp, 8
006C55A8  E8 EE FF FF FF                  call 0x1406c559b
006C55AD  48 83 C4 08                     add rsp, 8
006C55B1  E8 EE FF FF FF                  call 0x1406c55a4
006C55B6  48 83 C4 08                     add rsp, 8
006C55BA  E8 EE FF FF FF                  call 0x1406c55ad
006C55BF  48 83 C4 08                     add rsp, 8
006C55C3  E8 EE FF FF FF                  call 0x1406c55b6
006C55C8  48 83 C4 08                     add rsp, 8
006C55CC  E8 EE FF FF FF                  call 0x1406c55bf
006C55D1  48 83 C4 08                     add rsp, 8
006C55D5  E8 EE FF FF FF                  call 0x1406c55c8
006C55DA  48 83 C4 08                     add rsp, 8
006C55DE  E8 EE FF FF FF                  call 0x1406c55d1
006C55E3  48 83 C4 08                     add rsp, 8
006C55E7  E8 EE FF FF FF                  call 0x1406c55da
006C55EC  48 83 C4 08                     add rsp, 8
006C55F0  E8 EE FF FF FF                  call 0x1406c55e3
006C55F5  48 83 C4 08                     add rsp, 8
006C55F9  E8 EE FF FF FF                  call 0x1406c55ec
006C55FE  48 83 C4 08                     add rsp, 8
006C5602  E8 EE FF FF FF                  call 0x1406c55f5
006C5607  48 83 C4 08                     add rsp, 8
006C560B  E8 EE FF FF FF                  call 0x1406c55fe
006C5610  48 83 C4 08                     add rsp, 8
006C5614  B8 DA DA 00 00                  mov eax, 0xdada
006C5619  65 F6 04 25 5C 08 00 00 08      test byte ptr gs:[0x85c], 8
006C5622  74 07                           je 0x1406c562b
006C5624  B0 20                           mov al, 0x20
006C5626  F3 48 0F AE E8                  incsspq rax
006C562B  66 65 F7 04 25 58 08 00 00 00 01  test word ptr gs:[0x858], 0x100
006C5636  74 0C                           je 0x1406c5644
006C5638  33 C0                           xor eax, eax
006C563A  33 D2                           xor edx, edx
006C563C  B9 01 00 00 00                  mov ecx, 1
006C5641  48 F7 F1                        div rcx
006C5644  0F AE 55 AC                     ldmxcsr dword ptr [rbp - 0x54]
006C5648  0F 28 45 F0                     movaps xmm0, xmmword ptr [rbp - 0x10]
006C564C  0F 28 4D 00                     movaps xmm1, xmmword ptr [rbp]
006C5650  0F 28 55 10                     movaps xmm2, xmmword ptr [rbp + 0x10]
006C5654  0F 28 5D 20                     movaps xmm3, xmmword ptr [rbp + 0x20]
006C5658  0F 28 65 30                     movaps xmm4, xmmword ptr [rbp + 0x30]
006C565C  0F 28 6D 40                     movaps xmm5, xmmword ptr [rbp + 0x40]
006C5660  4C 8B 5D E0                     mov r11, qword ptr [rbp - 0x20]
006C5664  4C 8B 55 D8                     mov r10, qword ptr [rbp - 0x28]
006C5668  4C 8B 4D D0                     mov r9, qword ptr [rbp - 0x30]
006C566C  4C 8B 45 C8                     mov r8, qword ptr [rbp - 0x38]
006C5670  48 8B 55 C0                     mov rdx, qword ptr [rbp - 0x40]
006C5674  48 8B 4D B8                     mov rcx, qword ptr [rbp - 0x48]
006C5678  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
006C567C  48 8B B5 D0 00 00 00            mov rsi, qword ptr [rbp + 0xd0]
006C5683  48 8B BD C8 00 00 00            mov rdi, qword ptr [rbp + 0xc8]
006C568A  48 8B 9D C0 00 00 00            mov rbx, qword ptr [rbp + 0xc0]
006C5691  48 8B E5                        mov rsp, rbp
006C5694  48 8B AD D8 00 00 00            mov rbp, qword ptr [rbp + 0xd8]
006C569B  48 81 C4 E8 00 00 00            add rsp, 0xe8
006C56A2  F6 05 97 C1 B3 00 01            test byte ptr [rip + 0xb3c197], 1
006C56A9  74 05                           je 0x1406c56b0
006C56AB  E9 D0 74 50 00                  jmp 0x140bccb80
006C56B0  66 65 F7 04 25 58 08 00 00 00 02  test word ptr gs:[0x858], 0x200
006C56BB  74 05                           je 0x1406c56c2
006C56BD  0F 00 6C 24 20                  verw word ptr [rsp + 0x20]
006C56C2  0F 01 F8                        swapgs
006C56C5  48 CF                           iretq
006C56C7  83 FF 20                        cmp edi, 0x20
006C56CA  75 5B                           jne 0x1406c5727
006C56CC  89 45 80                        mov dword ptr [rbp - 0x80], eax
006C56CF  48 89 4D 88                     mov qword ptr [rbp - 0x78], rcx
006C56D3  48 89 55 90                     mov qword ptr [rbp - 0x70], rdx
006C56D7  4C 89 45 98                     mov qword ptr [rbp - 0x68], r8
006C56DB  4C 89 4D A0                     mov qword ptr [rbp - 0x60], r9
006C56DF  E8 AC DB FE FF                  call 0x1406b3290
006C56E4  0B C0                           or eax, eax
006C56E6  8B 45 80                        mov eax, dword ptr [rbp - 0x80]
006C56E9  48 8B 4D 88                     mov rcx, qword ptr [rbp - 0x78]
006C56ED  48 8B 55 90                     mov rdx, qword ptr [rbp - 0x70]
006C56F1  4C 8B 45 98                     mov r8, qword ptr [rbp - 0x68]
006C56F5  4C 8B 4D A0                     mov r9, qword ptr [rbp - 0x60]
006C56F9  48 89 A3 90 00 00 00            mov qword ptr [rbx + 0x90], rsp
006C5700  0F 84 CE F6 FF FF               je 0x1406c4dd4
006C5706  48 8D 3D 93 1B 90 00            lea rdi, [rip + 0x901b93]
006C570D  8B 77 10                        mov esi, dword ptr [rdi + 0x10]
006C5710  48 8B 3F                        mov rdi, qword ptr [rdi]
006C5713  3B C6                           cmp eax, esi
006C5715  73 10                           jae 0x1406c5727
006C5717  48 8D 3C B7                     lea rdi, [rdi + rsi*4]
006C571B  0F BE 04 07                     movsx eax, byte ptr [rdi + rax]
006C571F  0B C0                           or eax, eax
006C5721  0F 8E 39 F8 FF FF               jle 0x1406c4f60
006C5727  B8 1C 00 00 C0                  mov eax, 0xc000001c
006C572C  E9 2F F8 FF FF                  jmp 0x1406c4f60
006C5731  B9 4A 00 00 00                  mov ecx, 0x4a
006C5736  45 33 C9                        xor r9d, r9d
006C5739  45 0F 20 C0                     mov r8, cr8
006C573D  45 0B C0                        or r8d, r8d
006C5740  75 14                           jne 0x1406c5756
006C5742  B9 01 00 00 00                  mov ecx, 1
006C5747  45 0F B6 83 4A 02 00 00         movzx r8d, byte ptr [r11 + 0x24a]
006C574F  45 8B 8B E4 01 00 00            mov r9d, dword ptr [r11 + 0x1e4]
006C5756  48 8B 95 E8 00 00 00            mov rdx, qword ptr [rbp + 0xe8]
006C575D  4C 8B D5                        mov r10, rbp
006C5760  E8 1B 01 00 00                  call 0x1406c5880
006C5765  CC                              int3
006C5766  B9 F9 01 00 00                  mov ecx, 0x1f9
006C576B  48 8B 95 E8 00 00 00            mov rdx, qword ptr [rbp + 0xe8]
006C5772  45 0F B6 83 32 02 00 00         movzx r8d, byte ptr [r11 + 0x232]
006C577A  45 33 C9                        xor r9d, r9d
006C577D  45 33 D2                        xor r10d, r10d
006C5780  E8 FB 00 00 00                  call 0x1406c5880
006C5785  CC                              int3
006C5786  48 83 EC 50                     sub rsp, 0x50
006C578A  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
006C578F  48 89 54 24 28                  mov qword ptr [rsp + 0x28], rdx
006C5794  4C 89 44 24 30                  mov qword ptr [rsp + 0x30], r8
006C5799  4C 89 4C 24 38                  mov qword ptr [rsp + 0x38], r9
006C579E  4C 89 54 24 40                  mov qword ptr [rsp + 0x40], r10
006C57A3  49 8B CA                        mov rcx, r10
006C57A6  48 8B D4                        mov rdx, rsp
006C57A9  48 83 C2 20                     add rdx, 0x20
006C57AD  49 C7 C0 04 00 00 00            mov r8, 4
006C57B4  4C 8B CC                        mov r9, rsp
006C57B7  49 83 C1 70                     add r9, 0x70
006C57BB  E8 80 25 08 00                  call 0x140747d40
006C57C0  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
006C57C4  48 8B 4C 24 20                  mov rcx, qword ptr [rsp + 0x20]
006C57C9  48 8B 54 24 28                  mov rdx, qword ptr [rsp + 0x28]
006C57CE  4C 8B 44 24 30                  mov r8, qword ptr [rsp + 0x30]
006C57D3  4C 8B 4C 24 38                  mov r9, qword ptr [rsp + 0x38]
006C57D8  4C 8B 54 24 40                  mov r10, qword ptr [rsp + 0x40]
006C57DD  48 83 C4 50                     add rsp, 0x50
006C57E1  49 8B C2                        mov rax, r10
006C57E4  FF D0                           call rax
006C57E6  0F 1F 00                        nop dword ptr [rax]
006C57E9  48 8B 4D A0                     mov rcx, qword ptr [rbp - 0x60]
006C57ED  48 8B D0                        mov rdx, rax
006C57F0  E8 6B 26 08 00                  call 0x140747e60
006C57F5  E9 5E F7 FF FF                  jmp 0x1406c4f58
006C57FA  48 83 EC 50                     sub rsp, 0x50
006C57FE  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
006C5803  48 89 54 24 28                  mov qword ptr [rsp + 0x28], rdx
006C5808  4C 89 44 24 30                  mov qword ptr [rsp + 0x30], r8
006C580D  4C 89 4C 24 38                  mov qword ptr [rsp + 0x38], r9
006C5812  4C 89 54 24 40                  mov qword ptr [rsp + 0x40], r10
006C5817  49 8B CA                        mov rcx, r10
006C581A  E8 A1 FD B5 FF                  call 0x1402255c0
006C581F  48 8B 4C 24 20                  mov rcx, qword ptr [rsp + 0x20]
006C5824  48 8B 54 24 28                  mov rdx, qword ptr [rsp + 0x28]
006C5829  4C 8B 44 24 30                  mov r8, qword ptr [rsp + 0x30]
006C582E  4C 8B 4C 24 38                  mov r9, qword ptr [rsp + 0x38]
006C5833  4C 8B 54 24 40                  mov r10, qword ptr [rsp + 0x40]
006C5838  48 83 C4 50                     add rsp, 0x50
006C583C  49 8B C2                        mov rax, r10
006C583F  FF D0                           call rax
006C5841  0F 1F 00                        nop dword ptr [rax]
006C5844  48 8B C8                        mov rcx, rax
006C5847  E8 24 FC B5 FF                  call 0x140225470
006C584C  E9 07 F7 FF FF                  jmp 0x1406c4f58
006C5851  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiSystemCall64(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned int v_stack_m164;
    unsigned __int8 v_stack_m165;
    unsigned __int8 v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m180;
    unsigned __int64 v_stack_m188;
    unsigned int v_stack_m190;
    unsigned __int8 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int16 v_stack_m8;
    unsigned __int16 v_stack_m90;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;

    *(unsigned __int64 *)(gs_base + (0 + 16)) = v_rsp;
    if (*(unsigned __int64 *)(gs_base + (0 + 40232)) != 0) {
    }
    v_rsp = (*(unsigned __int64 *)(gs_base + (0 + 424))) - (8);
    v_rsp = (v_rsp) - (344);
    v_stack_m50 = v_rbx;
    v_stack_m48 = v_rdi;
    v_stack_m40 = v_rsi;
    if (((*(unsigned __int8 *)(v_rip + 9445695)) & (255)) == 0) goto loc_006C4ABF;
    if (((v_stack_m20) & (1)) != 0) {
    }
    v_stack_m160 = result;
    v_stack_m158 = v_r10;
    v_stack_m150 = a2;
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
    if ((((unsigned int)(a2)) & (2)) == 0) goto loc_006C4C9E;
    result = KiSystemCall64___0x23A(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0x243(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0x12C(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0x135(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0x13E(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0x147(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0x150(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0x159(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0x162(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0x16B(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0x174(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0x17D(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0x186(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0x18F(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0x198(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0x1A1(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0x1AA(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0x1B3(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0x1BC(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0x1C5(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0x1CE(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0x1D7(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0x1E0(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0x1E9(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0x1F2(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0x1FB(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0x204(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0x20D(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0x216(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0x21F(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0x228(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0x231(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = (unsigned int)(0xDADAULL);
    if (((*(unsigned __int8 *)(gs_base + (0 + 2140))) & (8)) != 0) {
        result = 32;
    }
    if ((((unsigned int)(a2)) & (128)) != 0) {
        result = KiFlushBhbDuringTrapEntryOrExit(a1, a2, a3, a4);
    }
    *(unsigned __int8 *)(gs_base + (0 + 2142)) = 0;
    if ((*(unsigned int *)(v_rip + 9446819)) == 0) goto loc_006C4CE2;
    if (((unsigned int)(a2)) == 0) goto loc_006C4CE2;
    a2 = (unsigned int)((a2) & (*(unsigned int *)(v_rip + 9446797)));
    if (((unsigned int)(a2)) != ((unsigned int)((unsigned int)((unsigned int)(a2))))) {
        a1 = 0x6A7ULL;
    }
    v_stack_m165 = 2;
    v_stack_m168 = 1;
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562) = 1;
    v_stack_m148 = a3;
    v_stack_m140 = a4;
    v_stack_m130 = v_r10;
    v_stack_m138 = v_r10;
    v_stack_m120 = v_xmm0;
    v_stack_m110 = v_xmm1;
    v_stack_m100 = v_xmm2;
    v_stack_mF0 = v_xmm3;
    v_stack_mE0 = v_xmm4;
    v_stack_mD0 = v_xmm5;
    result = KiSynchronizeUserIsolationDomainExit(a1, a2, a3, a4);
    v_stack_m90 = 0;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 3)) == 0) goto loc_006C4D98;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 3)) & (3)) != 0) {
        result = KiSaveDebugRegisterState(a1, a2, a3, a4);
    }
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 3)) & (36)) == 0) goto loc_006C4D98;
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 144) = v_rsp;
    result = PsSyscallProviderDispatch(v_rsp, a2, a3, a4);
    if (((unsigned __int8)(result)) == 1) goto loc_006C4D98;
    result = v_stack_m160;
    if (((unsigned __int8)(result)) >= 1) {
        a1 = 0xC000001CULL;
        a2 = 0;
        a3 = v_stack_m28;
        result = KiExceptionDispatch(a1, a2, a3, a4);
    }
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 3)) & (4)) == 0) goto loc_006C4F60;
    goto loc_006C53AB;
loc_006C4D98:
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 136) = v_stack_m158;
    *(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 128) = (unsigned int)(v_stack_m160);
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 144) = v_rsp;
    v_rdi = (unsigned int)(((unsigned int)((unsigned int)(v_stack_m160))) >> (7));
    v_rdi = (unsigned int)((v_rdi) & (32));
    result = (unsigned int)((v_stack_m160) & (0xFFFULL));
loc_006C4DD4:
    if (((*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 120)) & (128)) == 0) goto loc_006C4DFE;
    v_r11 = v_rip + 9446558;
    if (((*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 120)) & (0x200000ULL)) != 0) {
        v_r11 = v_rip + 9446853;
    }
loc_006C4DFE:
    if (((unsigned int)(result)) >= (*(unsigned int *)(v_r11 + v_rdi * 1 + 16))) goto loc_006C56C7;
    v_r11 = ((int)(*(unsigned int *)(*(unsigned __int64 *)(v_r11 + v_rdi * 1) + result * 4))) >> (4);
    v_r10 = (*(unsigned __int64 *)(v_r11 + v_rdi * 1)) + (v_r11);
    if (((unsigned int)(v_rdi)) != 32) goto loc_006C4E70;
    result = (int)(*(unsigned int *)(*(unsigned __int64 *)(v_r11 + v_rdi * 1) + result * 4));
    v_rbx = *(unsigned __int64 *)(gs_base + (0 + 392));
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 240) + 5952)) != 0) {
        v_stack_m160 = (int)(*(unsigned int *)(*(unsigned __int64 *)(v_r11 + v_rdi * 1) + result * 4));
        v_stack_m158 = v_stack_m158;
        v_stack_m150 = v_stack_m150;
        v_rbx = v_stack_m148;
        v_rdi = v_stack_m140;
        v_rsi = v_r10;
        a1 = 7;
        a2 = 0;
        a3 = 0;
        a4 = 0;
        result = PsInvokeWin32Callout(a1, a2, a3, a4);
        result = v_stack_m160;
        a1 = v_stack_m158;
        a2 = v_stack_m150;
        a3 = v_rbx;
        a4 = v_rdi;
        v_r10 = v_rsi;
    }
    result = (unsigned int)((result) & (15));
    if (condition_is_equal) goto loc_006C4F30;
    result = (unsigned int)((result) << (3));
    v_rsi = v_stack_m10 + 32;
    if (((v_stack_m20) & (1)) != 0) {
        v_rsi = v_stack_m10 + 32;
        if ((v_stack_m10 + 32) >= (*(unsigned __int64 *)(v_rip - 6856505))) { v_rsi = *(unsigned __int64 *)(v_rip - 6856513); }
    }
    v_r11 = (v_rip + 121) - (result);
loc_006C4F30:
    if (((*(unsigned int *)(v_rip + 9444806)) & (1)) != 0) goto loc_006C5786;
    if (((*(unsigned int *)(v_rip + 9444286)) & (64)) != 0) goto loc_006C57FA;
    result = kernel_indirect_call(a1, a2, a3, a4);
loc_006C4F58:
loc_006C4F60:
    if (((v_stack_m20) & (1)) == 0) goto loc_006C537E;
    a1 = (unsigned __int8)((v_cr8) | (*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 586)));
    a1 = (unsigned int)((a1) | (*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 484)));
    if (condition_is_not_equal) goto loc_006C5731;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) != 1) goto loc_006C5766;
loc_006C4FB2:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 194)) & (3)) == 0) goto loc_006C501D;
    v_stack_m160 = result;
    result = 0;
    v_stack_m158 = 0;
    v_stack_m150 = 0;
    v_stack_m148 = 0;
    v_stack_m140 = 0;
    v_stack_m138 = 0;
    v_stack_m130 = 0;
    v_stack_m120 = v_xmm0;
    v_stack_m110 = v_xmm0;
    v_stack_m100 = v_xmm0;
    v_stack_mF0 = v_xmm0;
    v_stack_mE0 = v_xmm0;
    v_stack_mD0 = v_xmm0;
    result = KiInitiateUserApc(1, a2, a3, a4);
    goto loc_006C4FB2;
loc_006C501D:
    v_stack_m160 = v_stack_m160;
    result = KiSynchronizeUserIsolationDomainEntry(0, a2, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_006C4FB2;
    result = v_stack_m160;
    if (((*(unsigned __int8 *)(gs_base + (0 + 2144))) & (2)) != 0) {
        v_stack_m160 = v_stack_m160;
        a1 = 0;
        result = KiUpdateStibpPairing(a1, a2, a3, a4);
        result = v_stack_m160;
    }
    if (((*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)))) & (0x8000000ULL)) != 0) {
        v_stack_m160 = result;
        result = 0;
        v_stack_m158 = 0;
        v_stack_m150 = 0;
        v_stack_m148 = 0;
        v_stack_m140 = 0;
        v_stack_m138 = 0;
        v_stack_m130 = 0;
        v_stack_m120 = v_xmm0;
        v_stack_m110 = v_xmm0;
        v_stack_m100 = v_xmm0;
        v_stack_mF0 = v_xmm0;
        v_stack_mE0 = v_xmm0;
        v_stack_mD0 = v_xmm0;
        result = KiRestoreSetContextState(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, a4);
    }
    if (((*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)))) & (0x10000ULL)) == 0) goto loc_006C50C5;
    v_stack_m160 = result;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 2)) & (1)) != 0) {
        result = KiCopyCounters(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, a4);
        a1 = *(unsigned __int64 *)(gs_base + (0 + 392));
    }
loc_006C50C5:
    v_r10 = 0;
    if (v_stack_m90 == 0) goto loc_006C5117;
    v_stack_m160 = v_stack_m160;
    result = KiRestoreDebugRegisterState(a1, a2, a3, a4);
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 360)) | (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 360));
    if (condition_is_equal) goto loc_006C5113;
    if (v_stack_m20 == 51) {
        v_r10 = v_stack_m28;
        v_stack_m28 = result;
    }
loc_006C5117:
    if (v_stack_m20 >= 51) goto loc_006C5151;
    a1 = 0;
    a3 = (*(unsigned __int64 *)(gs_base + (0 + 40232))) + (8);
    if (0 == a3) {
        a1 = *(unsigned __int64 *)(gs_base + (0 + 40224));
    }
    v_stack_m160 = v_stack_m160;
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
    if (condition_is_above_or_equal) goto loc_006C52E7;
    result = KiSystemCall64___0x883(a1, a2, a3, a4);
    v_rsp = (v_stack_m100) + (8);
    result = KiSystemCall64___0x88C(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0x775(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0x77E(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0x787(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0x790(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0x799(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0x7A2(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0x7AB(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0x7B4(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0x7BD(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0x7C6(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0x7CF(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0x7D8(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0x7E1(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0x7EA(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0x7F3(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0x7FC(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0x805(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0x80E(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0x817(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0x820(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0x829(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0x832(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0x83B(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0x844(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0x84D(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0x856(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0x85F(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0x868(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0x871(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0x87A(a1, a2, a3, a4);
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
    a2 = 0;
    a4 = 0;
    if (0 != 0) {
        a4 = 0;
    }
    if (((*(unsigned __int16 *)(gs_base + (0 + 2136))) & (512)) != 0) {
    }
loc_006C537E:
    *(unsigned __int64 *)(v_stack_m18 + 144) = v_stack_m58;
    *(unsigned __int8 *)(v_stack_m18 + 562) = (unsigned __int8)(v_stack_m168);
    return v_stack_m160;
loc_006C53AB:
    a1 = (unsigned __int8)((0) | (*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 586)));
    a1 = (unsigned int)((a1) | (*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 484)));
    if (condition_is_not_equal) goto loc_006C5731;
    if ((*(unsigned __int8 *)(v_stack_m50 + 562)) != 1) goto loc_006C5766;
    v_stack_m160 = v_stack_m160;
loc_006C53DE:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 194)) & (3)) == 0) goto loc_006C540B;
    result = KiInitiateUserApc(1, v_stack_m168, v_stack_m10, a4);
    goto loc_006C53DE;
loc_006C540B:
    if (((*(unsigned __int8 *)(gs_base + (0 + 2144))) & (2)) != 0) {
        a1 = 0;
        result = KiUpdateStibpPairing(a1, v_stack_m168, v_stack_m10, a4);
    }
    if (((*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)))) & (0x8000000ULL)) != 0) {
        result = KiRestoreSetContextState(*(unsigned __int64 *)(gs_base + (0 + 392)), v_stack_m168, v_stack_m10, a4);
    }
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 2)) & (1)) != 0) {
        result = KiCopyCounters(*(unsigned __int64 *)(gs_base + (0 + 392)), v_stack_m168, v_stack_m10, a4);
        a1 = *(unsigned __int64 *)(gs_base + (0 + 392));
    }
    if (v_stack_m90 != 0) {
        result = KiRestoreDebugRegisterState(a1, v_stack_m168, v_stack_m10, a4);
    }
    if (v_stack_m90 >= 0) goto loc_006C5499;
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
    if (condition_is_above_or_equal) goto loc_006C562B;
    result = KiSystemCall64___0xBC7(a1, a2, a3, a4);
    v_rsp = (v_stack_m10) + (8);
    result = KiSystemCall64___0xBD0(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0xAB9(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0xAC2(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0xACB(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0xAD4(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0xADD(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0xAE6(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0xAEF(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0xAF8(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0xB01(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0xB0A(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0xB13(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0xB1C(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0xB25(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0xB2E(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0xB37(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0xB40(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0xB49(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0xB52(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0xB5B(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0xB64(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0xB6D(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0xB76(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0xB7F(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0xB88(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0xB91(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0xB9A(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0xBA3(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0xBAC(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0xBB5(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSystemCall64___0xBBE(a1, a2, a3, a4);
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
    v_rsp = (v_stack_m38) + (232);
    if (((*(unsigned __int8 *)(v_rip + 11780503)) & (1)) == 0) goto loc_006C56B0;
loc_006C56B0:
    if (((*(unsigned __int16 *)(gs_base + (0 + 2136))) & (512)) != 0) {
    }
loc_006C56C7:
    if (((unsigned int)(v_stack_m48)) != 32) goto loc_006C5727;
    v_stack_m190 = (unsigned int)(v_stack_m160);
    v_stack_m188 = v_stack_m158;
    v_stack_m180 = v_stack_m150;
    v_stack_m178 = v_stack_m148;
    v_stack_m170 = v_stack_m140;
    result = KiConvertToGuiThread(v_stack_m158, v_stack_m150, v_stack_m148, v_stack_m140);
    result = (unsigned int)((result) | ((unsigned int)(result)));
    *(unsigned __int64 *)(v_stack_m50 + 144) = v_rsp;
    if (condition_is_equal) goto loc_006C4DD4;
    if (((unsigned int)((unsigned int)(v_stack_m190))) >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 9444243 + 16))))) goto loc_006C5727;
    result = (unsigned int)(((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 9444243) + (unsigned int)(*(unsigned int *)(v_rip + 9444243 + 16)) * 4 + (unsigned int)(v_stack_m190) * 1))) | ((unsigned int)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 9444243) + (unsigned int)(*(unsigned int *)(v_rip + 9444243 + 16)) * 4 + (unsigned int)(v_stack_m190) * 1)))));
    if (condition_is_less_or_equal) goto loc_006C4F60;
loc_006C5727:
    goto loc_006C4F60;
loc_006C5731:
    a4 = 0;
    a3 = (unsigned int)((0) | (0));
    if (!(condition_is_not_equal)) {
        a1 = 1;
        a3 = *(unsigned __int8 *)(v_stack_m130 + 586);
        a4 = *(unsigned int *)(v_stack_m130 + 484);
    }
    result = KiBugCheckDispatch(a1, v_stack_m28, a3, a4);
loc_006C5766:
    a4 = 0;
    v_r10 = 0;
    result = KiBugCheckDispatch(505, v_stack_m28, *(unsigned __int8 *)(v_stack_m130 + 562), a4);
loc_006C5786:
    v_rsp = (v_rsp) - (80);
    v_stack_m58 = 505;
    v_stack_m50 = v_stack_m28;
    v_stack_m48 = *(unsigned __int8 *)(v_stack_m130 + 562);
    v_stack_m40 = 0;
    v_stack_m38 = 0;
    a2 = (v_rsp) + (32);
    a4 = (v_rsp) + (112);
    result = KiTrackSystemCallEntry(0, a2, 4, a4);
    v_stack_m170 = result;
    v_rsp = (v_rsp) + (80);
    result = kernel_indirect_call(v_stack_m58, v_stack_m50, v_stack_m48, v_stack_m40);
    result = KiTrackSystemCallExit(v_stack_m170, result, v_stack_m48, v_stack_m40);
    goto loc_006C4F58;
loc_006C57FA:
    v_rsp = (v_rsp) - (80);
    v_stack_m58 = v_stack_m170;
    v_stack_m50 = result;
    v_stack_m48 = v_stack_m48;
    v_stack_m40 = v_stack_m40;
    v_stack_m38 = v_stack_m38;
    result = PerfInfoLogSysCallEntry(v_stack_m38, result, v_stack_m48, v_stack_m40);
    v_rsp = (v_rsp) + (80);
    result = kernel_indirect_call(v_stack_m58, v_stack_m50, v_stack_m48, v_stack_m40);
    result = PerfInfoLogSysCallExit(result, v_stack_m50, v_stack_m48, v_stack_m40);
    goto loc_006C4F58;
}
```

## 5. (Beta) C Style

```c
int64_t KiSystemCall64(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint64_t v_stack_m100;
    uint64_t v_stack_m110;
    uint64_t v_stack_m120;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint64_t v_stack_m148;
    uint64_t v_stack_m150;
    uint64_t v_stack_m158;
    uint64_t v_stack_m160;
    uint32_t v_stack_m164;
    uint8_t v_stack_m165;
    uint8_t v_stack_m168;
    uint64_t v_stack_m170;
    uint64_t v_stack_m178;
    uint64_t v_stack_m18;
    uint64_t v_stack_m180;
    uint64_t v_stack_m188;
    uint32_t v_stack_m190;
    uint8_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint16_t v_stack_m8;
    uint16_t v_stack_m90;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;

    *(uint64_t *)(gs_base + (0 + 0x10)) = local_rsp;
    if (*(uint64_t *)(gs_base + (0 + 0x9D28)) != 0) {
    }
    local_rsp = (*(uint64_t *)(gs_base + (0 + 0x1A8))) - (8);
    local_rsp = (local_rsp) - (344);
    v_stack_m50 = local_rbx;
    v_stack_m48 = local_rdi;
    v_stack_m40 = local_rsi;
    if (((*(uint8_t *)(v_rip + 0x90213F)) & (255)) == 0) goto loc_006C4ABF;
    if (((v_stack_m20) & (1)) != 0) {
    }
    v_stack_m160 = result;
    v_stack_m158 = local_r10;
    v_stack_m150 = Arg2;
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
    if ((((uint32_t)(Arg2)) & (2)) == 0) goto loc_006C4C9E;
    result = KiSystemCall64___0x23A(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0x243(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0x12C(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0x135(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0x13E(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0x147(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0x150(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0x159(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0x162(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0x16B(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0x174(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0x17D(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0x186(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0x18F(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0x198(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0x1A1(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0x1AA(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0x1B3(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0x1BC(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0x1C5(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0x1CE(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0x1D7(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0x1E0(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0x1E9(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0x1F2(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0x1FB(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0x204(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0x20D(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0x216(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0x21F(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0x228(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0x231(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = (uint32_t)(0xDADAULL);
    if (((*(uint8_t *)(gs_base + (0 + 0x85C))) & (8)) != 0) {
        result = 32;
    }
    if ((((uint32_t)(Arg2)) & (128)) != 0) {
        result = KiFlushBhbDuringTrapEntryOrExit(Arg1, Arg2, Arg3, Arg4);
    }
    *(uint8_t *)(gs_base + (0 + 0x85E)) = 0;
    if ((*(uint32_t *)(v_rip + 0x9025A3)) == 0) goto loc_006C4CE2;
    if (((uint32_t)(Arg2)) == 0) goto loc_006C4CE2;
    Arg2 = (uint32_t)((Arg2) & (*(uint32_t *)(v_rip + 0x90258D)));
    if (((uint32_t)(Arg2)) != ((uint32_t)((uint32_t)((uint32_t)(Arg2))))) {
        Arg1 = 0x6A7ULL;
    }
    v_stack_m165 = 2;
    v_stack_m168 = 1;
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232) = 1;
    v_stack_m148 = Arg3;
    v_stack_m140 = Arg4;
    v_stack_m130 = local_r10;
    v_stack_m138 = local_r10;
    v_stack_m120 = v_xmm0;
    v_stack_m110 = v_xmm1;
    v_stack_m100 = v_xmm2;
    v_stack_mF0 = v_xmm3;
    v_stack_mE0 = v_xmm4;
    v_stack_mD0 = v_xmm5;
    result = KiSynchronizeUserIsolationDomainExit(Arg1, Arg2, Arg3, Arg4);
    v_stack_m90 = 0;
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x3)) == 0) goto loc_006C4D98;
    if (((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x3)) & (3)) != 0) {
        result = KiSaveDebugRegisterState(Arg1, Arg2, Arg3, Arg4);
    }
    if (((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x3)) & (36)) == 0) goto loc_006C4D98;
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x90) = local_rsp;
    result = PsSyscallProviderDispatch(local_rsp, Arg2, Arg3, Arg4);
    if (((uint8_t)(result)) == 1) goto loc_006C4D98;
    result = v_stack_m160;
    if (((uint8_t)(result)) >= 1) {
        Arg1 = 0xC000001CULL;
        Arg2 = 0;
        Arg3 = v_stack_m28;
        result = KiExceptionDispatch(Arg1, Arg2, Arg3, Arg4);
    }
    if (((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x3)) & (4)) == 0) goto loc_006C4F60;
    goto loc_006C53AB;
loc_006C4D98:
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x88) = v_stack_m158;
    *(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x80) = (uint32_t)(v_stack_m160);
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x90) = local_rsp;
    local_rdi = (uint32_t)(((uint32_t)((uint32_t)(v_stack_m160))) >> (7));
    local_rdi = (uint32_t)((local_rdi) & (32));
    result = (uint32_t)((v_stack_m160) & (0xFFFULL));
loc_006C4DD4:
    if (((*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x78)) & (128)) == 0) goto loc_006C4DFE;
    local_r11 = v_rip + 9446558;
    if (((*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x78)) & (0x200000ULL)) != 0) {
        local_r11 = v_rip + 9446853;
    }
loc_006C4DFE:
    if (((uint32_t)(result)) >= (*(uint32_t *)(local_r11 + local_rdi * 1 + 0x10))) goto loc_006C56C7;
    local_r11 = ((int32_t)(*(uint32_t *)(*(uint64_t *)(local_r11 + local_rdi * 1) + result * 4))) >> (4);
    local_r10 = (*(uint64_t *)(local_r11 + local_rdi * 1)) + (local_r11);
    if (((uint32_t)(local_rdi)) != 32) goto loc_006C4E70;
    result = (int32_t)(*(uint32_t *)(*(uint64_t *)(local_r11 + local_rdi * 1) + result * 4));
    local_rbx = *(uint64_t *)(gs_base + (0 + 0x188));
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xF0) + 0x1740)) != 0) {
        v_stack_m160 = (int32_t)(*(uint32_t *)(*(uint64_t *)(local_r11 + local_rdi * 1) + result * 4));
        v_stack_m158 = v_stack_m158;
        v_stack_m150 = v_stack_m150;
        local_rbx = v_stack_m148;
        local_rdi = v_stack_m140;
        local_rsi = local_r10;
        Arg1 = 7;
        Arg2 = 0;
        Arg3 = 0;
        Arg4 = 0;
        result = PsInvokeWin32Callout(Arg1, Arg2, Arg3, Arg4);
        result = v_stack_m160;
        Arg1 = v_stack_m158;
        Arg2 = v_stack_m150;
        Arg3 = local_rbx;
        Arg4 = local_rdi;
        local_r10 = local_rsi;
    }
    result = (uint32_t)((result) & (15));
    if (condition_is_equal) goto loc_006C4F30;
    result = (uint32_t)((result) << (3));
    local_rsi = v_stack_m10 + 32;
    if (((v_stack_m20) & (1)) != 0) {
        local_rsi = v_stack_m10 + 32;
        if ((v_stack_m10 + 32) >= (*(uint64_t *)(v_rip - 0x689F39))) { local_rsi = *(uint64_t *)(v_rip - 0x689F41); }
    }
    local_r11 = (v_rip + 121) - (result);
loc_006C4F30:
    if (((*(uint32_t *)(v_rip + 0x901DC6)) & (1)) != 0) goto loc_006C5786;
    if (((*(uint32_t *)(v_rip + 0x901BBE)) & (64)) != 0) goto loc_006C57FA;
    result = kernel_indirect_call(Arg1, Arg2, Arg3, Arg4);
loc_006C4F58:
loc_006C4F60:
    if (((v_stack_m20) & (1)) == 0) goto loc_006C537E;
    Arg1 = (uint8_t)((v_cr8) | (*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x24A)));
    Arg1 = (uint32_t)((Arg1) | (*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x1E4)));
    if (condition_is_not_equal) goto loc_006C5731;
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) != 1) goto loc_006C5766;
loc_006C4FB2:
    if (((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xC2)) & (3)) == 0) goto loc_006C501D;
    v_stack_m160 = result;
    result = 0;
    v_stack_m158 = 0;
    v_stack_m150 = 0;
    v_stack_m148 = 0;
    v_stack_m140 = 0;
    v_stack_m138 = 0;
    v_stack_m130 = 0;
    v_stack_m120 = v_xmm0;
    v_stack_m110 = v_xmm0;
    v_stack_m100 = v_xmm0;
    v_stack_mF0 = v_xmm0;
    v_stack_mE0 = v_xmm0;
    v_stack_mD0 = v_xmm0;
    result = KiInitiateUserApc(1, Arg2, Arg3, Arg4);
    goto loc_006C4FB2;
loc_006C501D:
    v_stack_m160 = v_stack_m160;
    result = KiSynchronizeUserIsolationDomainEntry(0, Arg2, Arg3, Arg4);
    if ((uint32_t)(result) != 0) goto loc_006C4FB2;
    result = v_stack_m160;
    if (((*(uint8_t *)(gs_base + (0 + 0x860))) & (2)) != 0) {
        v_stack_m160 = v_stack_m160;
        Arg1 = 0;
        result = KiUpdateStibpPairing(Arg1, Arg2, Arg3, Arg4);
        result = v_stack_m160;
    }
    if (((*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)))) & (0x8000000ULL)) != 0) {
        v_stack_m160 = result;
        result = 0;
        v_stack_m158 = 0;
        v_stack_m150 = 0;
        v_stack_m148 = 0;
        v_stack_m140 = 0;
        v_stack_m138 = 0;
        v_stack_m130 = 0;
        v_stack_m120 = v_xmm0;
        v_stack_m110 = v_xmm0;
        v_stack_m100 = v_xmm0;
        v_stack_mF0 = v_xmm0;
        v_stack_mE0 = v_xmm0;
        v_stack_mD0 = v_xmm0;
        result = KiRestoreSetContextState(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, Arg3, Arg4);
    }
    if (((*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)))) & (0x10000ULL)) == 0) goto loc_006C50C5;
    v_stack_m160 = result;
    if (((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x2)) & (1)) != 0) {
        result = KiCopyCounters(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, Arg3, Arg4);
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x188));
    }
loc_006C50C5:
    local_r10 = 0;
    if (v_stack_m90 == 0) goto loc_006C5117;
    v_stack_m160 = v_stack_m160;
    result = KiRestoreDebugRegisterState(Arg1, Arg2, Arg3, Arg4);
    result = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x168)) | (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x168));
    if (condition_is_equal) goto loc_006C5113;
    if (v_stack_m20 == 51) {
        local_r10 = v_stack_m28;
        v_stack_m28 = result;
    }
loc_006C5117:
    if (v_stack_m20 >= 51) goto loc_006C5151;
    Arg1 = 0;
    Arg3 = (*(uint64_t *)(gs_base + (0 + 0x9D28))) + (8);
    if (0 == Arg3) {
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x9D20));
    }
    v_stack_m160 = v_stack_m160;
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
    if (condition_is_above_or_equal) goto loc_006C52E7;
    result = KiSystemCall64___0x883(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (v_stack_m100) + (8);
    result = KiSystemCall64___0x88C(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0x775(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0x77E(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0x787(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0x790(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0x799(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0x7A2(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0x7AB(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0x7B4(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0x7BD(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0x7C6(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0x7CF(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0x7D8(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0x7E1(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0x7EA(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0x7F3(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0x7FC(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0x805(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0x80E(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0x817(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0x820(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0x829(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0x832(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0x83B(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0x844(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0x84D(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0x856(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0x85F(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0x868(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0x871(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0x87A(Arg1, Arg2, Arg3, Arg4);
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
    Arg2 = 0;
    Arg4 = 0;
    if (0 != 0) {
        Arg4 = 0;
    }
    if (((*(uint16_t *)(gs_base + (0 + 0x858))) & (512)) != 0) {
    }
loc_006C537E:
    *(uint64_t *)(v_stack_m18 + 0x90) = v_stack_m58;
    *(uint8_t *)(v_stack_m18 + 0x232) = (uint8_t)(v_stack_m168);
    return v_stack_m160;
loc_006C53AB:
    Arg1 = (uint8_t)((0) | (*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x24A)));
    Arg1 = (uint32_t)((Arg1) | (*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x1E4)));
    if (condition_is_not_equal) goto loc_006C5731;
    if ((*(uint8_t *)(v_stack_m50 + 0x232)) != 1) goto loc_006C5766;
    v_stack_m160 = v_stack_m160;
loc_006C53DE:
    if (((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xC2)) & (3)) == 0) goto loc_006C540B;
    result = KiInitiateUserApc(1, v_stack_m168, v_stack_m10, Arg4);
    goto loc_006C53DE;
loc_006C540B:
    if (((*(uint8_t *)(gs_base + (0 + 0x860))) & (2)) != 0) {
        Arg1 = 0;
        result = KiUpdateStibpPairing(Arg1, v_stack_m168, v_stack_m10, Arg4);
    }
    if (((*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)))) & (0x8000000ULL)) != 0) {
        result = KiRestoreSetContextState(*(uint64_t *)(gs_base + (0 + 0x188)), v_stack_m168, v_stack_m10, Arg4);
    }
    if (((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x2)) & (1)) != 0) {
        result = KiCopyCounters(*(uint64_t *)(gs_base + (0 + 0x188)), v_stack_m168, v_stack_m10, Arg4);
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x188));
    }
    if (v_stack_m90 != 0) {
        result = KiRestoreDebugRegisterState(Arg1, v_stack_m168, v_stack_m10, Arg4);
    }
    if (v_stack_m90 >= 0) goto loc_006C5499;
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
    if (condition_is_above_or_equal) goto loc_006C562B;
    result = KiSystemCall64___0xBC7(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (v_stack_m10) + (8);
    result = KiSystemCall64___0xBD0(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0xAB9(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0xAC2(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0xACB(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0xAD4(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0xADD(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0xAE6(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0xAEF(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0xAF8(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0xB01(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0xB0A(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0xB13(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0xB1C(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0xB25(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0xB2E(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0xB37(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0xB40(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0xB49(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0xB52(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0xB5B(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0xB64(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0xB6D(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0xB76(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0xB7F(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0xB88(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0xB91(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0xB9A(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0xBA3(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0xBAC(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0xBB5(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSystemCall64___0xBBE(Arg1, Arg2, Arg3, Arg4);
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
    local_rsp = (v_stack_m38) + (232);
    if (((*(uint8_t *)(v_rip + 0xB3C197)) & (1)) == 0) goto loc_006C56B0;
loc_006C56B0:
    if (((*(uint16_t *)(gs_base + (0 + 0x858))) & (512)) != 0) {
    }
loc_006C56C7:
    if (((uint32_t)(v_stack_m48)) != 32) goto loc_006C5727;
    v_stack_m190 = (uint32_t)(v_stack_m160);
    v_stack_m188 = v_stack_m158;
    v_stack_m180 = v_stack_m150;
    v_stack_m178 = v_stack_m148;
    v_stack_m170 = v_stack_m140;
    result = KiConvertToGuiThread(v_stack_m158, v_stack_m150, v_stack_m148, v_stack_m140);
    result = (uint32_t)((result) | ((uint32_t)(result)));
    *(uint64_t *)(v_stack_m50 + 0x90) = local_rsp;
    if (condition_is_equal) goto loc_006C4DD4;
    if (((uint32_t)((uint32_t)(v_stack_m190))) >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x901B93 + 0x10))))) goto loc_006C5727;
    result = (uint32_t)(((int8_t)(*(uint8_t *)(*(uint64_t *)(v_rip + 0x901B93) + (uint32_t)(*(uint32_t *)(v_rip + 0x901B93 + 0x10)) * 4 + (uint32_t)(v_stack_m190) * 1))) | ((uint32_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(v_rip + 0x901B93) + (uint32_t)(*(uint32_t *)(v_rip + 0x901B93 + 0x10)) * 4 + (uint32_t)(v_stack_m190) * 1)))));
    if (condition_is_less_or_equal) goto loc_006C4F60;
loc_006C5727:
    goto loc_006C4F60;
loc_006C5731:
    Arg4 = 0;
    Arg3 = (uint32_t)((0) | (0));
    if (!(condition_is_not_equal)) {
        Arg1 = 1;
        Arg3 = *(uint8_t *)(v_stack_m130 + 0x24A);
        Arg4 = *(uint32_t *)(v_stack_m130 + 0x1E4);
    }
    result = KiBugCheckDispatch(Arg1, v_stack_m28, Arg3, Arg4);
loc_006C5766:
    Arg4 = 0;
    local_r10 = 0;
    result = KiBugCheckDispatch(505, v_stack_m28, *(uint8_t *)(v_stack_m130 + 0x232), Arg4);
loc_006C5786:
    local_rsp = (local_rsp) - (80);
    v_stack_m58 = 505;
    v_stack_m50 = v_stack_m28;
    v_stack_m48 = *(uint8_t *)(v_stack_m130 + 0x232);
    v_stack_m40 = 0;
    v_stack_m38 = 0;
    Arg2 = (local_rsp) + (32);
    Arg4 = (local_rsp) + (112);
    result = KiTrackSystemCallEntry(0, Arg2, 4, Arg4);
    v_stack_m170 = result;
    local_rsp = (local_rsp) + (80);
    result = kernel_indirect_call(v_stack_m58, v_stack_m50, v_stack_m48, v_stack_m40);
    result = KiTrackSystemCallExit(v_stack_m170, result, v_stack_m48, v_stack_m40);
    goto loc_006C4F58;
loc_006C57FA:
    local_rsp = (local_rsp) - (80);
    v_stack_m58 = v_stack_m170;
    v_stack_m50 = result;
    v_stack_m48 = v_stack_m48;
    v_stack_m40 = v_stack_m40;
    v_stack_m38 = v_stack_m38;
    result = PerfInfoLogSysCallEntry(v_stack_m38, result, v_stack_m48, v_stack_m40);
    local_rsp = (local_rsp) + (80);
    result = kernel_indirect_call(v_stack_m58, v_stack_m50, v_stack_m48, v_stack_m40);
    result = PerfInfoLogSysCallExit(result, v_stack_m50, v_stack_m48, v_stack_m40);
    goto loc_006C4F58;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006C4A40&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
