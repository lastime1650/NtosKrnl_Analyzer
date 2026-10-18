# KiControlProtectionFault

- RVA: `0x006C3040`–`0x006C3792` (길이 `1,874` bytes)
- VA: `0x00000001406C3040`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C1D70`
- 디코드: `407`개 명령, `1,874/1,874` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **77**; 고유 호출 대상: **77**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x006C3192` → [KiControlProtectionFault + 0x265](KiControlProtectionFault_function_006C3040.md) (inside-function, `0x006C32A5`)
- `0x006C319B` → [KiControlProtectionFault + 0x26E](KiControlProtectionFault_function_006C3040.md) (inside-function, `0x006C32AE`)
- `0x006C31A4` → [KiControlProtectionFault + 0x157](KiControlProtectionFault_function_006C3040.md) (inside-function, `0x006C3197`)
- `0x006C31AD` → [KiControlProtectionFault + 0x160](KiControlProtectionFault_function_006C3040.md) (inside-function, `0x006C31A0`)
- `0x006C31B6` → [KiControlProtectionFault + 0x169](KiControlProtectionFault_function_006C3040.md) (inside-function, `0x006C31A9`)
- `0x006C31BF` → [KiControlProtectionFault + 0x172](KiControlProtectionFault_function_006C3040.md) (inside-function, `0x006C31B2`)
- `0x006C31C8` → [KiControlProtectionFault + 0x17B](KiControlProtectionFault_function_006C3040.md) (inside-function, `0x006C31BB`)
- `0x006C31D1` → [KiControlProtectionFault + 0x184](KiControlProtectionFault_function_006C3040.md) (inside-function, `0x006C31C4`)
- `0x006C31DA` → [KiControlProtectionFault + 0x18D](KiControlProtectionFault_function_006C3040.md) (inside-function, `0x006C31CD`)
- `0x006C31E3` → [KiControlProtectionFault + 0x196](KiControlProtectionFault_function_006C3040.md) (inside-function, `0x006C31D6`)
- `0x006C31EC` → [KiControlProtectionFault + 0x19F](KiControlProtectionFault_function_006C3040.md) (inside-function, `0x006C31DF`)
- `0x006C31F5` → [KiControlProtectionFault + 0x1A8](KiControlProtectionFault_function_006C3040.md) (inside-function, `0x006C31E8`)
- `0x006C31FE` → [KiControlProtectionFault + 0x1B1](KiControlProtectionFault_function_006C3040.md) (inside-function, `0x006C31F1`)
- `0x006C3207` → [KiControlProtectionFault + 0x1BA](KiControlProtectionFault_function_006C3040.md) (inside-function, `0x006C31FA`)
- `0x006C3210` → [KiControlProtectionFault + 0x1C3](KiControlProtectionFault_function_006C3040.md) (inside-function, `0x006C3203`)
- `0x006C3219` → [KiControlProtectionFault + 0x1CC](KiControlProtectionFault_function_006C3040.md) (inside-function, `0x006C320C`)
- `0x006C3222` → [KiControlProtectionFault + 0x1D5](KiControlProtectionFault_function_006C3040.md) (inside-function, `0x006C3215`)
- `0x006C322B` → [KiControlProtectionFault + 0x1DE](KiControlProtectionFault_function_006C3040.md) (inside-function, `0x006C321E`)
- `0x006C3234` → [KiControlProtectionFault + 0x1E7](KiControlProtectionFault_function_006C3040.md) (inside-function, `0x006C3227`)
- `0x006C323D` → [KiControlProtectionFault + 0x1F0](KiControlProtectionFault_function_006C3040.md) (inside-function, `0x006C3230`)
- `0x006C3246` → [KiControlProtectionFault + 0x1F9](KiControlProtectionFault_function_006C3040.md) (inside-function, `0x006C3239`)
- `0x006C324F` → [KiControlProtectionFault + 0x202](KiControlProtectionFault_function_006C3040.md) (inside-function, `0x006C3242`)
- `0x006C3258` → [KiControlProtectionFault + 0x20B](KiControlProtectionFault_function_006C3040.md) (inside-function, `0x006C324B`)
- `0x006C3261` → [KiControlProtectionFault + 0x214](KiControlProtectionFault_function_006C3040.md) (inside-function, `0x006C3254`)
- `0x006C326A` → [KiControlProtectionFault + 0x21D](KiControlProtectionFault_function_006C3040.md) (inside-function, `0x006C325D`)
- `0x006C3273` → [KiControlProtectionFault + 0x226](KiControlProtectionFault_function_006C3040.md) (inside-function, `0x006C3266`)
- `0x006C327C` → [KiControlProtectionFault + 0x22F](KiControlProtectionFault_function_006C3040.md) (inside-function, `0x006C326F`)
- `0x006C3285` → [KiControlProtectionFault + 0x238](KiControlProtectionFault_function_006C3040.md) (inside-function, `0x006C3278`)
- `0x006C328E` → [KiControlProtectionFault + 0x241](KiControlProtectionFault_function_006C3040.md) (inside-function, `0x006C3281`)
- `0x006C3297` → [KiControlProtectionFault + 0x24A](KiControlProtectionFault_function_006C3040.md) (inside-function, `0x006C328A`)
- `0x006C32A0` → [KiControlProtectionFault + 0x253](KiControlProtectionFault_function_006C3040.md) (inside-function, `0x006C3293`)
- `0x006C32A9` → [KiControlProtectionFault + 0x25C](KiControlProtectionFault_function_006C3040.md) (inside-function, `0x006C329C`)
- `0x006C32D4` → [KiFlushBhbDuringTrapEntryOrExit](KiFlushBhbDuringTrapEntryOrExit_function_006C6340.md) (function, `0x006C6340`)
- `0x006C331D` → [KiSaveDebugRegisterState](../4F/KiSaveDebugRegisterState_function_004FD960.md) (function, `0x004FD960`)
- `0x006C3351` → [KiSynchronizeUserIsolationDomainExit](../41/KiSynchronizeUserIsolationDomainExit_function_0041BFA0.md) (function, `0x0041BFA0`)
- `0x006C3391` → [KiProcessControlProtection](../44/KiProcessControlProtection_function_00444750.md) (function, `0x00444750`)
- `0x006C341A` → [KiFastFailDispatch](KiFastFailDispatch_function_006C5E40.md) (function, `0x006C5E40`)
- `0x006C342A` → [KiBugCheckDispatch](KiBugCheckDispatch_function_006C5880.md) (function, `0x006C5880`)
- `0x006C343D` → [KiExceptionDispatch](KiExceptionDispatch_function_006C5900.md) (function, `0x006C5900`)
- `0x006C3479` → [KiInitiateUserApc](../6B/KiInitiateUserApc_function_006B6540.md) (function, `0x006B6540`)
- `0x006C348A` → [KiSynchronizeUserIsolationDomainEntry](../26/KiSynchronizeUserIsolationDomainEntry_function_00263F60.md) (function, `0x00263F60`)
- `0x006C34A4` → [KiUpdateStibpPairing](../3E/KiUpdateStibpPairing_function_003E71C0.md) (function, `0x003E71C0`)
- `0x006C34BA` → [KiRestoreSetContextState](../6B/KiRestoreSetContextState_function_006B1CA0.md) (function, `0x006B1CA0`)
- `0x006C34D6` → [KiCopyCounters](../5C/KiCopyCounters_function_005C0710.md) (function, `0x005C0710`)
- `0x006C34F2` → [KiRestoreDebugRegisterState](../4F/KiRestoreDebugRegisterState_function_004FD8E0.md) (function, `0x004FD8E0`)
- `0x006C358C` → [KiControlProtectionFault + 0x65F](KiControlProtectionFault_function_006C3040.md) (inside-function, `0x006C369F`)
- `0x006C3595` → [KiControlProtectionFault + 0x668](KiControlProtectionFault_function_006C3040.md) (inside-function, `0x006C36A8`)
- `0x006C359E` → [KiControlProtectionFault + 0x551](KiControlProtectionFault_function_006C3040.md) (inside-function, `0x006C3591`)
- `0x006C35A7` → [KiControlProtectionFault + 0x55A](KiControlProtectionFault_function_006C3040.md) (inside-function, `0x006C359A`)
- `0x006C35B0` → [KiControlProtectionFault + 0x563](KiControlProtectionFault_function_006C3040.md) (inside-function, `0x006C35A3`)
- `0x006C35B9` → [KiControlProtectionFault + 0x56C](KiControlProtectionFault_function_006C3040.md) (inside-function, `0x006C35AC`)
- `0x006C35C2` → [KiControlProtectionFault + 0x575](KiControlProtectionFault_function_006C3040.md) (inside-function, `0x006C35B5`)
- `0x006C35CB` → [KiControlProtectionFault + 0x57E](KiControlProtectionFault_function_006C3040.md) (inside-function, `0x006C35BE`)
- `0x006C35D4` → [KiControlProtectionFault + 0x587](KiControlProtectionFault_function_006C3040.md) (inside-function, `0x006C35C7`)
- `0x006C35DD` → [KiControlProtectionFault + 0x590](KiControlProtectionFault_function_006C3040.md) (inside-function, `0x006C35D0`)
- `0x006C35E6` → [KiControlProtectionFault + 0x599](KiControlProtectionFault_function_006C3040.md) (inside-function, `0x006C35D9`)
- `0x006C35EF` → [KiControlProtectionFault + 0x5A2](KiControlProtectionFault_function_006C3040.md) (inside-function, `0x006C35E2`)
- `0x006C35F8` → [KiControlProtectionFault + 0x5AB](KiControlProtectionFault_function_006C3040.md) (inside-function, `0x006C35EB`)
- `0x006C3601` → [KiControlProtectionFault + 0x5B4](KiControlProtectionFault_function_006C3040.md) (inside-function, `0x006C35F4`)
- `0x006C360A` → [KiControlProtectionFault + 0x5BD](KiControlProtectionFault_function_006C3040.md) (inside-function, `0x006C35FD`)
- `0x006C3613` → [KiControlProtectionFault + 0x5C6](KiControlProtectionFault_function_006C3040.md) (inside-function, `0x006C3606`)
- `0x006C361C` → [KiControlProtectionFault + 0x5CF](KiControlProtectionFault_function_006C3040.md) (inside-function, `0x006C360F`)
- `0x006C3625` → [KiControlProtectionFault + 0x5D8](KiControlProtectionFault_function_006C3040.md) (inside-function, `0x006C3618`)
- `0x006C362E` → [KiControlProtectionFault + 0x5E1](KiControlProtectionFault_function_006C3040.md) (inside-function, `0x006C3621`)
- `0x006C3637` → [KiControlProtectionFault + 0x5EA](KiControlProtectionFault_function_006C3040.md) (inside-function, `0x006C362A`)
- `0x006C3640` → [KiControlProtectionFault + 0x5F3](KiControlProtectionFault_function_006C3040.md) (inside-function, `0x006C3633`)
- `0x006C3649` → [KiControlProtectionFault + 0x5FC](KiControlProtectionFault_function_006C3040.md) (inside-function, `0x006C363C`)
- `0x006C3652` → [KiControlProtectionFault + 0x605](KiControlProtectionFault_function_006C3040.md) (inside-function, `0x006C3645`)
- `0x006C365B` → [KiControlProtectionFault + 0x60E](KiControlProtectionFault_function_006C3040.md) (inside-function, `0x006C364E`)
- `0x006C3664` → [KiControlProtectionFault + 0x617](KiControlProtectionFault_function_006C3040.md) (inside-function, `0x006C3657`)
- `0x006C366D` → [KiControlProtectionFault + 0x620](KiControlProtectionFault_function_006C3040.md) (inside-function, `0x006C3660`)
- `0x006C3676` → [KiControlProtectionFault + 0x629](KiControlProtectionFault_function_006C3040.md) (inside-function, `0x006C3669`)
- `0x006C367F` → [KiControlProtectionFault + 0x632](KiControlProtectionFault_function_006C3040.md) (inside-function, `0x006C3672`)
- `0x006C3688` → [KiControlProtectionFault + 0x63B](KiControlProtectionFault_function_006C3040.md) (inside-function, `0x006C367B`)
- `0x006C3691` → [KiControlProtectionFault + 0x644](KiControlProtectionFault_function_006C3040.md) (inside-function, `0x006C3684`)
- `0x006C369A` → [KiControlProtectionFault + 0x64D](KiControlProtectionFault_function_006C3040.md) (inside-function, `0x006C368D`)
- `0x006C36A3` → [KiControlProtectionFault + 0x656](KiControlProtectionFault_function_006C3040.md) (inside-function, `0x006C3696`)

### Direct callers
- [KiControlProtectionFault](KiControlProtectionFault_function_006C3040.md) at `0x006C3192`
- [KiControlProtectionFault](KiControlProtectionFault_function_006C3040.md) at `0x006C319B`
- [KiControlProtectionFault](KiControlProtectionFault_function_006C3040.md) at `0x006C31A4`
- [KiControlProtectionFault](KiControlProtectionFault_function_006C3040.md) at `0x006C31AD`
- [KiControlProtectionFault](KiControlProtectionFault_function_006C3040.md) at `0x006C31B6`
- [KiControlProtectionFault](KiControlProtectionFault_function_006C3040.md) at `0x006C31BF`
- [KiControlProtectionFault](KiControlProtectionFault_function_006C3040.md) at `0x006C31C8`
- [KiControlProtectionFault](KiControlProtectionFault_function_006C3040.md) at `0x006C31D1`
- [KiControlProtectionFault](KiControlProtectionFault_function_006C3040.md) at `0x006C31DA`
- [KiControlProtectionFault](KiControlProtectionFault_function_006C3040.md) at `0x006C31E3`
- [KiControlProtectionFault](KiControlProtectionFault_function_006C3040.md) at `0x006C31EC`
- [KiControlProtectionFault](KiControlProtectionFault_function_006C3040.md) at `0x006C31F5`
- [KiControlProtectionFault](KiControlProtectionFault_function_006C3040.md) at `0x006C31FE`
- [KiControlProtectionFault](KiControlProtectionFault_function_006C3040.md) at `0x006C3207`
- [KiControlProtectionFault](KiControlProtectionFault_function_006C3040.md) at `0x006C3210`
- [KiControlProtectionFault](KiControlProtectionFault_function_006C3040.md) at `0x006C3219`
- [KiControlProtectionFault](KiControlProtectionFault_function_006C3040.md) at `0x006C3222`
- [KiControlProtectionFault](KiControlProtectionFault_function_006C3040.md) at `0x006C322B`
- [KiControlProtectionFault](KiControlProtectionFault_function_006C3040.md) at `0x006C3234`
- [KiControlProtectionFault](KiControlProtectionFault_function_006C3040.md) at `0x006C323D`
- [KiControlProtectionFault](KiControlProtectionFault_function_006C3040.md) at `0x006C3246`
- [KiControlProtectionFault](KiControlProtectionFault_function_006C3040.md) at `0x006C324F`
- [KiControlProtectionFault](KiControlProtectionFault_function_006C3040.md) at `0x006C3258`
- [KiControlProtectionFault](KiControlProtectionFault_function_006C3040.md) at `0x006C3261`
- [KiControlProtectionFault](KiControlProtectionFault_function_006C3040.md) at `0x006C326A`
- [KiControlProtectionFault](KiControlProtectionFault_function_006C3040.md) at `0x006C3273`
- [KiControlProtectionFault](KiControlProtectionFault_function_006C3040.md) at `0x006C327C`
- [KiControlProtectionFault](KiControlProtectionFault_function_006C3040.md) at `0x006C3285`
- [KiControlProtectionFault](KiControlProtectionFault_function_006C3040.md) at `0x006C328E`
- [KiControlProtectionFault](KiControlProtectionFault_function_006C3040.md) at `0x006C3297`
- [KiControlProtectionFault](KiControlProtectionFault_function_006C3040.md) at `0x006C32A0`
- [KiControlProtectionFault](KiControlProtectionFault_function_006C3040.md) at `0x006C32A9`
- [KiControlProtectionFault](KiControlProtectionFault_function_006C3040.md) at `0x006C358C`
- [KiControlProtectionFault](KiControlProtectionFault_function_006C3040.md) at `0x006C3595`
- [KiControlProtectionFault](KiControlProtectionFault_function_006C3040.md) at `0x006C359E`
- [KiControlProtectionFault](KiControlProtectionFault_function_006C3040.md) at `0x006C35A7`
- [KiControlProtectionFault](KiControlProtectionFault_function_006C3040.md) at `0x006C35B0`
- [KiControlProtectionFault](KiControlProtectionFault_function_006C3040.md) at `0x006C35B9`
- [KiControlProtectionFault](KiControlProtectionFault_function_006C3040.md) at `0x006C35C2`
- [KiControlProtectionFault](KiControlProtectionFault_function_006C3040.md) at `0x006C35CB`
- [KiControlProtectionFault](KiControlProtectionFault_function_006C3040.md) at `0x006C35D4`
- [KiControlProtectionFault](KiControlProtectionFault_function_006C3040.md) at `0x006C35DD`
- [KiControlProtectionFault](KiControlProtectionFault_function_006C3040.md) at `0x006C35E6`
- [KiControlProtectionFault](KiControlProtectionFault_function_006C3040.md) at `0x006C35EF`
- [KiControlProtectionFault](KiControlProtectionFault_function_006C3040.md) at `0x006C35F8`
- [KiControlProtectionFault](KiControlProtectionFault_function_006C3040.md) at `0x006C3601`
- [KiControlProtectionFault](KiControlProtectionFault_function_006C3040.md) at `0x006C360A`
- [KiControlProtectionFault](KiControlProtectionFault_function_006C3040.md) at `0x006C3613`
- [KiControlProtectionFault](KiControlProtectionFault_function_006C3040.md) at `0x006C361C`
- [KiControlProtectionFault](KiControlProtectionFault_function_006C3040.md) at `0x006C3625`
- [KiControlProtectionFault](KiControlProtectionFault_function_006C3040.md) at `0x006C362E`
- [KiControlProtectionFault](KiControlProtectionFault_function_006C3040.md) at `0x006C3637`
- [KiControlProtectionFault](KiControlProtectionFault_function_006C3040.md) at `0x006C3640`
- [KiControlProtectionFault](KiControlProtectionFault_function_006C3040.md) at `0x006C3649`
- [KiControlProtectionFault](KiControlProtectionFault_function_006C3040.md) at `0x006C3652`
- [KiControlProtectionFault](KiControlProtectionFault_function_006C3040.md) at `0x006C365B`
- [KiControlProtectionFault](KiControlProtectionFault_function_006C3040.md) at `0x006C3664`
- [KiControlProtectionFault](KiControlProtectionFault_function_006C3040.md) at `0x006C366D`
- [KiControlProtectionFault](KiControlProtectionFault_function_006C3040.md) at `0x006C3676`
- [KiControlProtectionFault](KiControlProtectionFault_function_006C3040.md) at `0x006C367F`
- [KiControlProtectionFault](KiControlProtectionFault_function_006C3040.md) at `0x006C3688`
- [KiControlProtectionFault](KiControlProtectionFault_function_006C3040.md) at `0x006C3691`
- [KiControlProtectionFault](KiControlProtectionFault_function_006C3040.md) at `0x006C369A`
- [KiControlProtectionFault](KiControlProtectionFault_function_006C3040.md) at `0x006C36A3`

### Static image references
- `0x006C30B1` → RVA `0x01201840` (`CFGRO`; read)
- `0x006C32E5` → RVA `0x00FC7264` (`ALMOSTRO`; read)
- `0x006C3356` → RVA `0x00FC6BF0` (`ALMOSTRO`; read)
- `0x006C33E7` → RVA `0x00FC6E80` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006C372A` → [KiKernelExit](../../kvascode/BC/KiKernelExit_function_00BCCB80.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006C3040  55                              push rbp
006C3041  48 81 EC 58 01 00 00            sub rsp, 0x158
006C3048  48 8D AC 24 80 00 00 00         lea rbp, [rsp + 0x80]
006C3050  C6 45 AB 01                     mov byte ptr [rbp - 0x55], 1
006C3054  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
006C3058  48 89 4D B8                     mov qword ptr [rbp - 0x48], rcx
006C305C  48 89 55 C0                     mov qword ptr [rbp - 0x40], rdx
006C3060  4C 89 45 C8                     mov qword ptr [rbp - 0x38], r8
006C3064  4C 89 4D D0                     mov qword ptr [rbp - 0x30], r9
006C3068  4C 89 55 D8                     mov qword ptr [rbp - 0x28], r10
006C306C  4C 89 5D E0                     mov qword ptr [rbp - 0x20], r11
006C3070  F6 85 F0 00 00 00 01            test byte ptr [rbp + 0xf0], 1
006C3077  75 38                           jne 0x1406c30b1
006C3079  33 D2                           xor edx, edx
006C307B  F3 48 0F 1E CA                  rdsspq rdx
006C3080  48 89 55 58                     mov qword ptr [rbp + 0x58], rdx
006C3084  0F AE E8                        lfence
006C3087  65 F6 04 25 58 08 00 00 01      test byte ptr gs:[0x858], 1
006C3090  75 08                           jne 0x1406c309a
006C3092  0F AE E8                        lfence
006C3095  E9 88 02 00 00                  jmp 0x1406c3322
006C309A  65 0F B7 04 25 66 08 00 00      movzx eax, word ptr gs:[0x866]
006C30A3  B9 48 00 00 00                  mov ecx, 0x48
006C30A8  33 D2                           xor edx, edx
006C30AA  0F 30                           wrmsr
006C30AC  E9 71 02 00 00                  jmp 0x1406c3322
006C30B1  F6 05 88 E7 B3 00 01            test byte ptr [rip + 0xb3e788], 1
006C30B8  75 03                           jne 0x1406c30bd
006C30BA  0F 01 F8                        swapgs
006C30BD  0F AE E8                        lfence
006C30C0  65 48 8B 0C 25 28 9D 00 00      mov rcx, qword ptr gs:[0x9d28]
006C30C9  48 85 C9                        test rcx, rcx
006C30CC  74 1F                           je 0x1406c30ed
006C30CE  F3 48 0F 1E CA                  rdsspq rdx
006C30D3  65 4C 8B 14 25 20 9D 00 00      mov r10, qword ptr gs:[0x9d20]
006C30DC  49 83 C2 08                     add r10, 8
006C30E0  49 3B D2                        cmp rdx, r10
006C30E3  75 08                           jne 0x1406c30ed
006C30E5  F3 0F 01 29                     rstorssp dword ptr [rcx]
006C30E9  F3 0F 01 EA                     saveprevssp
006C30ED  65 4C 8B 14 25 88 01 00 00      mov r10, qword ptr gs:[0x188]
006C30F6  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006C30FF  48 8B 89 20 02 00 00            mov rcx, qword ptr [rcx + 0x220]
006C3106  48 8B 89 60 07 00 00            mov rcx, qword ptr [rcx + 0x760]
006C310D  65 48 89 0C 25 50 08 00 00      mov qword ptr gs:[0x850], rcx
006C3116  66 65 8B 0C 25 62 08 00 00      mov cx, word ptr gs:[0x862]
006C311F  66 65 89 0C 25 64 08 00 00      mov word ptr gs:[0x864], cx
006C3128  65 8A 0C 25 58 08 00 00         mov cl, byte ptr gs:[0x858]
006C3130  65 88 0C 25 5A 08 00 00         mov byte ptr gs:[0x85a], cl
006C3138  65 0F B7 04 25 68 08 00 00      movzx eax, word ptr gs:[0x868]
006C3141  66 65 39 04 25 66 08 00 00      cmp word ptr gs:[0x866], ax
006C314A  74 12                           je 0x1406c315e
006C314C  66 65 89 04 25 66 08 00 00      mov word ptr gs:[0x866], ax
006C3155  B9 48 00 00 00                  mov ecx, 0x48
006C315A  33 D2                           xor edx, edx
006C315C  0F 30                           wrmsr
006C315E  65 0F B6 14 25 58 08 00 00      movzx edx, byte ptr gs:[0x858]
006C3167  F7 C2 08 00 00 00               test edx, 8
006C316D  74 17                           je 0x1406c3186
006C316F  B8 01 00 00 00                  mov eax, 1
006C3174  33 D2                           xor edx, edx
006C3176  B9 49 00 00 00                  mov ecx, 0x49
006C317B  0F 30                           wrmsr
006C317D  65 0F B6 14 25 58 08 00 00      movzx edx, byte ptr gs:[0x858]
006C3186  F7 C2 02 00 00 00               test edx, 2
006C318C  0F 84 37 01 00 00               je 0x1406c32c9
006C3192  E8 0E 01 00 00                  call 0x1406c32a5
006C3197  48 83 C4 08                     add rsp, 8
006C319B  E8 0E 01 00 00                  call 0x1406c32ae
006C31A0  48 83 C4 08                     add rsp, 8
006C31A4  E8 EE FF FF FF                  call 0x1406c3197
006C31A9  48 83 C4 08                     add rsp, 8
006C31AD  E8 EE FF FF FF                  call 0x1406c31a0
006C31B2  48 83 C4 08                     add rsp, 8
006C31B6  E8 EE FF FF FF                  call 0x1406c31a9
006C31BB  48 83 C4 08                     add rsp, 8
006C31BF  E8 EE FF FF FF                  call 0x1406c31b2
006C31C4  48 83 C4 08                     add rsp, 8
006C31C8  E8 EE FF FF FF                  call 0x1406c31bb
006C31CD  48 83 C4 08                     add rsp, 8
006C31D1  E8 EE FF FF FF                  call 0x1406c31c4
006C31D6  48 83 C4 08                     add rsp, 8
006C31DA  E8 EE FF FF FF                  call 0x1406c31cd
006C31DF  48 83 C4 08                     add rsp, 8
006C31E3  E8 EE FF FF FF                  call 0x1406c31d6
006C31E8  48 83 C4 08                     add rsp, 8
006C31EC  E8 EE FF FF FF                  call 0x1406c31df
006C31F1  48 83 C4 08                     add rsp, 8
006C31F5  E8 EE FF FF FF                  call 0x1406c31e8
006C31FA  48 83 C4 08                     add rsp, 8
006C31FE  E8 EE FF FF FF                  call 0x1406c31f1
006C3203  48 83 C4 08                     add rsp, 8
006C3207  E8 EE FF FF FF                  call 0x1406c31fa
006C320C  48 83 C4 08                     add rsp, 8
006C3210  E8 EE FF FF FF                  call 0x1406c3203
006C3215  48 83 C4 08                     add rsp, 8
006C3219  E8 EE FF FF FF                  call 0x1406c320c
006C321E  48 83 C4 08                     add rsp, 8
006C3222  E8 EE FF FF FF                  call 0x1406c3215
006C3227  48 83 C4 08                     add rsp, 8
006C322B  E8 EE FF FF FF                  call 0x1406c321e
006C3230  48 83 C4 08                     add rsp, 8
006C3234  E8 EE FF FF FF                  call 0x1406c3227
006C3239  48 83 C4 08                     add rsp, 8
006C323D  E8 EE FF FF FF                  call 0x1406c3230
006C3242  48 83 C4 08                     add rsp, 8
006C3246  E8 EE FF FF FF                  call 0x1406c3239
006C324B  48 83 C4 08                     add rsp, 8
006C324F  E8 EE FF FF FF                  call 0x1406c3242
006C3254  48 83 C4 08                     add rsp, 8
006C3258  E8 EE FF FF FF                  call 0x1406c324b
006C325D  48 83 C4 08                     add rsp, 8
006C3261  E8 EE FF FF FF                  call 0x1406c3254
006C3266  48 83 C4 08                     add rsp, 8
006C326A  E8 EE FF FF FF                  call 0x1406c325d
006C326F  48 83 C4 08                     add rsp, 8
006C3273  E8 EE FF FF FF                  call 0x1406c3266
006C3278  48 83 C4 08                     add rsp, 8
006C327C  E8 EE FF FF FF                  call 0x1406c326f
006C3281  48 83 C4 08                     add rsp, 8
006C3285  E8 EE FF FF FF                  call 0x1406c3278
006C328A  48 83 C4 08                     add rsp, 8
006C328E  E8 EE FF FF FF                  call 0x1406c3281
006C3293  48 83 C4 08                     add rsp, 8
006C3297  E8 EE FF FF FF                  call 0x1406c328a
006C329C  48 83 C4 08                     add rsp, 8
006C32A0  E8 EE FF FF FF                  call 0x1406c3293
006C32A5  48 83 C4 08                     add rsp, 8
006C32A9  E8 EE FF FF FF                  call 0x1406c329c
006C32AE  48 83 C4 08                     add rsp, 8
006C32B2  B8 DA DA 00 00                  mov eax, 0xdada
006C32B7  65 F6 04 25 5C 08 00 00 08      test byte ptr gs:[0x85c], 8
006C32C0  74 07                           je 0x1406c32c9
006C32C2  B0 20                           mov al, 0x20
006C32C4  F3 48 0F AE E8                  incsspq rax
006C32C9  F7 C2 80 00 00 00               test edx, 0x80
006C32CF  74 08                           je 0x1406c32d9
006C32D1  0F AE E8                        lfence
006C32D4  E8 67 30 00 00                  call 0x1406c6340
006C32D9  0F AE E8                        lfence
006C32DC  65 C6 04 25 5E 08 00 00 00      mov byte ptr gs:[0x85e], 0
006C32E5  83 3D 78 3F 90 00 00            cmp dword ptr [rip + 0x903f78], 0
006C32EC  74 1F                           je 0x1406c330d
006C32EE  B9 A7 06 00 00                  mov ecx, 0x6a7
006C32F3  0F 32                           rdmsr
006C32F5  83 FA 00                        cmp edx, 0
006C32F8  74 13                           je 0x1406c330d
006C32FA  8B CA                           mov ecx, edx
006C32FC  23 15 62 3F 90 00               and edx, dword ptr [rip + 0x903f62]
006C3302  3B D1                           cmp edx, ecx
006C3304  74 07                           je 0x1406c330d
006C3306  B9 A7 06 00 00                  mov ecx, 0x6a7
006C330B  0F 30                           wrmsr
006C330D  41 F6 42 03 03                  test byte ptr [r10 + 3], 3
006C3312  66 C7 85 80 00 00 00 00 00      mov word ptr [rbp + 0x80], 0
006C331B  74 05                           je 0x1406c3322
006C331D  E8 3E A6 E3 FF                  call 0x1404fd960
006C3322  FC                              cld
006C3323  0F AE 5D AC                     stmxcsr dword ptr [rbp - 0x54]
006C3327  65 0F AE 14 25 80 01 00 00      ldmxcsr dword ptr gs:[0x180]
006C3330  0F 29 45 F0                     movaps xmmword ptr [rbp - 0x10], xmm0
006C3334  0F 29 4D 00                     movaps xmmword ptr [rbp], xmm1
006C3338  0F 29 55 10                     movaps xmmword ptr [rbp + 0x10], xmm2
006C333C  0F 29 5D 20                     movaps xmmword ptr [rbp + 0x20], xmm3
006C3340  0F 29 65 30                     movaps xmmword ptr [rbp + 0x30], xmm4
006C3344  0F 29 6D 40                     movaps xmmword ptr [rbp + 0x40], xmm5
006C3348  F6 85 F0 00 00 00 01            test byte ptr [rbp + 0xf0], 1
006C334F  74 05                           je 0x1406c3356
006C3351  E8 4A 8C D5 FF                  call 0x14041bfa0
006C3356  F6 05 93 38 90 00 FF            test byte ptr [rip + 0x903893], 0xff
006C335D  74 0C                           je 0x1406c336b
006C335F  F6 85 F0 00 00 00 01            test byte ptr [rbp + 0xf0], 1
006C3366  74 03                           je 0x1406c336b
006C3368  0F 01 CB                        stac
006C336B  8B 85 E0 00 00 00               mov eax, dword ptr [rbp + 0xe0]
006C3371  F7 85 F8 00 00 00 00 02 00 00   test dword ptr [rbp + 0xf8], 0x200
006C337B  74 01                           je 0x1406c337e
006C337D  FB                              sti
006C337E  65 F6 04 25 25 91 00 00 40      test byte ptr gs:[0x9125], 0x40
006C3387  0F 84 93 00 00 00               je 0x1406c3420
006C338D  48 8D 4D 80                     lea rcx, [rbp - 0x80]
006C3391  E8 BA 13 D8 FF                  call 0x140444750
006C3396  83 F8 01                        cmp eax, 1
006C3399  0F 84 A4 00 00 00               je 0x1406c3443
006C339F  83 F8 02                        cmp eax, 2
006C33A2  74 0B                           je 0x1406c33af
006C33A4  83 F8 03                        cmp eax, 3
006C33A7  0F 84 82 00 00 00               je 0x1406c342f
006C33AD  EB 71                           jmp 0x1406c3420
006C33AF  F6 85 F0 00 00 00 01            test byte ptr [rbp + 0xf0], 1
006C33B6  74 43                           je 0x1406c33fb
006C33B8  B9 A7 06 00 00                  mov ecx, 0x6a7
006C33BD  0F 32                           rdmsr
006C33BF  48 C1 E2 20                     shl rdx, 0x20
006C33C3  48 0B C2                        or rax, rdx
006C33C6  4C 8B D0                        mov r10, rax
006C33C9  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006C33D2  48 8B 89 20 02 00 00            mov rcx, qword ptr [rcx + 0x220]
006C33D9  44 8B 99 54 07 00 00            mov r11d, dword ptr [rcx + 0x754]
006C33E0  41 81 E3 00 C0 F6 C0            and r11d, 0xc0f6c000
006C33E7  8B 15 93 3A 90 00               mov edx, dword ptr [rip + 0x903a93]
006C33ED  48 C1 E2 20                     shl rdx, 0x20
006C33F1  4C 0B DA                        or r11, rdx
006C33F4  BA 03 00 00 00                  mov edx, 3
006C33F9  EB 0C                           jmp 0x1406c3407
006C33FB  BA 02 00 00 00                  mov edx, 2
006C3400  4C 8B 55 58                     mov r10, qword ptr [rbp + 0x58]
006C3404  4D 8B 12                        mov r10, qword ptr [r10]
006C3407  49 C7 C1 39 00 00 00            mov r9, 0x39
006C340E  B9 09 04 00 C0                  mov ecx, 0xc0000409
006C3413  4C 8B 85 E8 00 00 00            mov r8, qword ptr [rbp + 0xe8]
006C341A  E8 21 2A 00 00                  call 0x1406c5e40
006C341F  90                              nop
006C3420  BA 15 00 00 00                  mov edx, 0x15
006C3425  B9 7F 00 00 00                  mov ecx, 0x7f
006C342A  E8 51 24 00 00                  call 0x1406c5880
006C342F  B9 33 00 00 80                  mov ecx, 0x80000033
006C3434  33 D2                           xor edx, edx
006C3436  4C 8B 85 E8 00 00 00            mov r8, qword ptr [rbp + 0xe8]
006C343D  E8 BE 24 00 00                  call 0x1406c5900
006C3442  90                              nop
006C3443  FA                              cli
006C3444  F6 85 F0 00 00 00 01            test byte ptr [rbp + 0xf0], 1
006C344B  0F 84 F5 02 00 00               je 0x1406c3746
006C3451  F6 05 98 37 90 00 FF            test byte ptr [rip + 0x903798], 0xff
006C3458  74 03                           je 0x1406c345d
006C345A  0F 01 CB                        stac
006C345D  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006C3466  F6 81 C2 00 00 00 03            test byte ptr [rcx + 0xc2], 3
006C346D  74 1B                           je 0x1406c348a
006C346F  B9 01 00 00 00                  mov ecx, 1
006C3474  44 0F 22 C1                     mov cr8, rcx
006C3478  FB                              sti
006C3479  E8 C2 30 FF FF                  call 0x1406b6540
006C347E  FA                              cli
006C347F  B9 00 00 00 00                  mov ecx, 0
006C3484  44 0F 22 C1                     mov cr8, rcx
006C3488  EB D3                           jmp 0x1406c345d
006C348A  E8 D1 0A BA FF                  call 0x140263f60
006C348F  85 C0                           test eax, eax
006C3491  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
006C3495  75 C6                           jne 0x1406c345d
006C3497  65 F6 04 25 60 08 00 00 02      test byte ptr gs:[0x860], 2
006C34A0  74 07                           je 0x1406c34a9
006C34A2  33 C9                           xor ecx, ecx
006C34A4  E8 17 3D D2 FF                  call 0x1403e71c0
006C34A9  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006C34B2  F7 01 00 00 00 08               test dword ptr [rcx], 0x8000000
006C34B8  74 05                           je 0x1406c34bf
006C34BA  E8 E1 E7 FE FF                  call 0x1406b1ca0
006C34BF  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006C34C8  F7 01 00 00 01 00               test dword ptr [rcx], 0x10000
006C34CE  74 14                           je 0x1406c34e4
006C34D0  F6 41 02 01                     test byte ptr [rcx + 2], 1
006C34D4  74 0E                           je 0x1406c34e4
006C34D6  E8 35 D2 EF FF                  call 0x1405c0710
006C34DB  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006C34E4  0F AE 55 AC                     ldmxcsr dword ptr [rbp - 0x54]
006C34E8  66 83 BD 80 00 00 00 00         cmp word ptr [rbp + 0x80], 0
006C34F0  74 05                           je 0x1406c34f7
006C34F2  E8 E9 A3 E3 FF                  call 0x1404fd8e0
006C34F7  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006C3500  0F BA 61 74 16                  bt dword ptr [rcx + 0x74], 0x16
006C3505  73 2A                           jae 0x1406c3531
006C3507  33 C9                           xor ecx, ecx
006C3509  F3 48 0F 1E C9                  rdsspq rcx
006C350E  65 4C 8B 04 25 28 9D 00 00      mov r8, qword ptr gs:[0x9d28]
006C3517  49 83 C0 08                     add r8, 8
006C351B  49 3B C8                        cmp rcx, r8
006C351E  75 11                           jne 0x1406c3531
006C3520  65 48 8B 0C 25 20 9D 00 00      mov rcx, qword ptr gs:[0x9d20]
006C3529  F3 0F 01 29                     rstorssp dword ptr [rcx]
006C352D  F3 0F 01 EA                     saveprevssp
006C3531  65 C6 04 25 5E 08 00 00 00      mov byte ptr gs:[0x85e], 0
006C353A  65 0F B7 04 25 6C 08 00 00      movzx eax, word ptr gs:[0x86c]
006C3543  66 65 39 04 25 66 08 00 00      cmp word ptr gs:[0x866], ax
006C354C  74 12                           je 0x1406c3560
006C354E  66 65 89 04 25 66 08 00 00      mov word ptr gs:[0x866], ax
006C3557  B9 48 00 00 00                  mov ecx, 0x48
006C355C  33 D2                           xor edx, edx
006C355E  0F 30                           wrmsr
006C3560  66 65 0F BA 34 25 58 08 00 00 02  btr word ptr gs:[0x858], 2
006C356B  73 0E                           jae 0x1406c357b
006C356D  B8 01 00 00 00                  mov eax, 1
006C3572  33 D2                           xor edx, edx
006C3574  B9 49 00 00 00                  mov ecx, 0x49
006C3579  0F 30                           wrmsr
006C357B  66 65 0F BA 34 25 58 08 00 00 05  btr word ptr gs:[0x858], 5
006C3586  0F 83 37 01 00 00               jae 0x1406c36c3
006C358C  E8 0E 01 00 00                  call 0x1406c369f
006C3591  48 83 C4 08                     add rsp, 8
006C3595  E8 0E 01 00 00                  call 0x1406c36a8
006C359A  48 83 C4 08                     add rsp, 8
006C359E  E8 EE FF FF FF                  call 0x1406c3591
006C35A3  48 83 C4 08                     add rsp, 8
006C35A7  E8 EE FF FF FF                  call 0x1406c359a
006C35AC  48 83 C4 08                     add rsp, 8
006C35B0  E8 EE FF FF FF                  call 0x1406c35a3
006C35B5  48 83 C4 08                     add rsp, 8
006C35B9  E8 EE FF FF FF                  call 0x1406c35ac
006C35BE  48 83 C4 08                     add rsp, 8
006C35C2  E8 EE FF FF FF                  call 0x1406c35b5
006C35C7  48 83 C4 08                     add rsp, 8
006C35CB  E8 EE FF FF FF                  call 0x1406c35be
006C35D0  48 83 C4 08                     add rsp, 8
006C35D4  E8 EE FF FF FF                  call 0x1406c35c7
006C35D9  48 83 C4 08                     add rsp, 8
006C35DD  E8 EE FF FF FF                  call 0x1406c35d0
006C35E2  48 83 C4 08                     add rsp, 8
006C35E6  E8 EE FF FF FF                  call 0x1406c35d9
006C35EB  48 83 C4 08                     add rsp, 8
006C35EF  E8 EE FF FF FF                  call 0x1406c35e2
006C35F4  48 83 C4 08                     add rsp, 8
006C35F8  E8 EE FF FF FF                  call 0x1406c35eb
006C35FD  48 83 C4 08                     add rsp, 8
006C3601  E8 EE FF FF FF                  call 0x1406c35f4
006C3606  48 83 C4 08                     add rsp, 8
006C360A  E8 EE FF FF FF                  call 0x1406c35fd
006C360F  48 83 C4 08                     add rsp, 8
006C3613  E8 EE FF FF FF                  call 0x1406c3606
006C3618  48 83 C4 08                     add rsp, 8
006C361C  E8 EE FF FF FF                  call 0x1406c360f
006C3621  48 83 C4 08                     add rsp, 8
006C3625  E8 EE FF FF FF                  call 0x1406c3618
006C362A  48 83 C4 08                     add rsp, 8
006C362E  E8 EE FF FF FF                  call 0x1406c3621
006C3633  48 83 C4 08                     add rsp, 8
006C3637  E8 EE FF FF FF                  call 0x1406c362a
006C363C  48 83 C4 08                     add rsp, 8
006C3640  E8 EE FF FF FF                  call 0x1406c3633
006C3645  48 83 C4 08                     add rsp, 8
006C3649  E8 EE FF FF FF                  call 0x1406c363c
006C364E  48 83 C4 08                     add rsp, 8
006C3652  E8 EE FF FF FF                  call 0x1406c3645
006C3657  48 83 C4 08                     add rsp, 8
006C365B  E8 EE FF FF FF                  call 0x1406c364e
006C3660  48 83 C4 08                     add rsp, 8
006C3664  E8 EE FF FF FF                  call 0x1406c3657
006C3669  48 83 C4 08                     add rsp, 8
006C366D  E8 EE FF FF FF                  call 0x1406c3660
006C3672  48 83 C4 08                     add rsp, 8
006C3676  E8 EE FF FF FF                  call 0x1406c3669
006C367B  48 83 C4 08                     add rsp, 8
006C367F  E8 EE FF FF FF                  call 0x1406c3672
006C3684  48 83 C4 08                     add rsp, 8
006C3688  E8 EE FF FF FF                  call 0x1406c367b
006C368D  48 83 C4 08                     add rsp, 8
006C3691  E8 EE FF FF FF                  call 0x1406c3684
006C3696  48 83 C4 08                     add rsp, 8
006C369A  E8 EE FF FF FF                  call 0x1406c368d
006C369F  48 83 C4 08                     add rsp, 8
006C36A3  E8 EE FF FF FF                  call 0x1406c3696
006C36A8  48 83 C4 08                     add rsp, 8
006C36AC  B8 DA DA 00 00                  mov eax, 0xdada
006C36B1  65 F6 04 25 5C 08 00 00 08      test byte ptr gs:[0x85c], 8
006C36BA  74 07                           je 0x1406c36c3
006C36BC  B0 20                           mov al, 0x20
006C36BE  F3 48 0F AE E8                  incsspq rax
006C36C3  66 65 F7 04 25 58 08 00 00 00 01  test word ptr gs:[0x858], 0x100
006C36CE  74 0C                           je 0x1406c36dc
006C36D0  33 C0                           xor eax, eax
006C36D2  33 D2                           xor edx, edx
006C36D4  B9 01 00 00 00                  mov ecx, 1
006C36D9  48 F7 F1                        div rcx
006C36DC  0F 28 45 F0                     movaps xmm0, xmmword ptr [rbp - 0x10]
006C36E0  0F 28 4D 00                     movaps xmm1, xmmword ptr [rbp]
006C36E4  0F 28 55 10                     movaps xmm2, xmmword ptr [rbp + 0x10]
006C36E8  0F 28 5D 20                     movaps xmm3, xmmword ptr [rbp + 0x20]
006C36EC  0F 28 65 30                     movaps xmm4, xmmword ptr [rbp + 0x30]
006C36F0  0F 28 6D 40                     movaps xmm5, xmmword ptr [rbp + 0x40]
006C36F4  4C 8B 5D E0                     mov r11, qword ptr [rbp - 0x20]
006C36F8  4C 8B 55 D8                     mov r10, qword ptr [rbp - 0x28]
006C36FC  4C 8B 4D D0                     mov r9, qword ptr [rbp - 0x30]
006C3700  4C 8B 45 C8                     mov r8, qword ptr [rbp - 0x38]
006C3704  48 8B 55 C0                     mov rdx, qword ptr [rbp - 0x40]
006C3708  48 8B 4D B8                     mov rcx, qword ptr [rbp - 0x48]
006C370C  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
006C3710  48 8B E5                        mov rsp, rbp
006C3713  48 8B AD D8 00 00 00            mov rbp, qword ptr [rbp + 0xd8]
006C371A  48 81 C4 E8 00 00 00            add rsp, 0xe8
006C3721  F6 05 18 E1 B3 00 01            test byte ptr [rip + 0xb3e118], 1
006C3728  74 05                           je 0x1406c372f
006C372A  E9 51 94 50 00                  jmp 0x140bccb80
006C372F  66 65 F7 04 25 58 08 00 00 00 02  test word ptr gs:[0x858], 0x200
006C373A  74 05                           je 0x1406c3741
006C373C  0F 00 6C 24 20                  verw word ptr [rsp + 0x20]
006C3741  0F 01 F8                        swapgs
006C3744  48 CF                           iretq
006C3746  0F AE 55 AC                     ldmxcsr dword ptr [rbp - 0x54]
006C374A  0F 28 45 F0                     movaps xmm0, xmmword ptr [rbp - 0x10]
006C374E  0F 28 4D 00                     movaps xmm1, xmmword ptr [rbp]
006C3752  0F 28 55 10                     movaps xmm2, xmmword ptr [rbp + 0x10]
006C3756  0F 28 5D 20                     movaps xmm3, xmmword ptr [rbp + 0x20]
006C375A  0F 28 65 30                     movaps xmm4, xmmword ptr [rbp + 0x30]
006C375E  0F 28 6D 40                     movaps xmm5, xmmword ptr [rbp + 0x40]
006C3762  4C 8B 5D E0                     mov r11, qword ptr [rbp - 0x20]
006C3766  4C 8B 55 D8                     mov r10, qword ptr [rbp - 0x28]
006C376A  4C 8B 4D D0                     mov r9, qword ptr [rbp - 0x30]
006C376E  4C 8B 45 C8                     mov r8, qword ptr [rbp - 0x38]
006C3772  48 8B 55 C0                     mov rdx, qword ptr [rbp - 0x40]
006C3776  48 8B 4D B8                     mov rcx, qword ptr [rbp - 0x48]
006C377A  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
006C377E  48 8B E5                        mov rsp, rbp
006C3781  48 8B AD D8 00 00 00            mov rbp, qword ptr [rbp + 0xd8]
006C3788  48 81 C4 E8 00 00 00            add rsp, 0xe8
006C378F  48 CF                           iretq
006C3791  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiControlProtectionFault(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned __int16 a5)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned int v_stack_m134;
    unsigned __int8 v_stack_m135;
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
    unsigned int v_stack_p0;
    unsigned __int8 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (344);
    v_stack_m135 = 1;
    v_stack_m130 = result;
    v_stack_m128 = a1;
    v_stack_m120 = a2;
    v_stack_m118 = a3;
    v_stack_m110 = a4;
    v_stack_m108 = v_r10;
    v_stack_m100 = v_r11;
    if (((v_stack_p10) & (1)) != 0) goto loc_006C30B1;
    a2 = 0;
    v_stack_m88 = 0;
    if (((*(unsigned __int8 *)(gs_base + (0 + 2136))) & (1)) != 0) goto loc_006C309A;
    goto loc_006C3322;
loc_006C309A:
    a2 = 0;
    goto loc_006C3322;
loc_006C30B1:
    if (((*(unsigned __int8 *)(v_rip + 11790216)) & (1)) == 0) {
    }
    if (*(unsigned __int64 *)(gs_base + (0 + 40232)) == 0) goto loc_006C30ED;
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
    if ((((unsigned int)(a2)) & (2)) == 0) goto loc_006C32C9;
    result = KiControlProtectionFault___0x265(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiControlProtectionFault___0x26E(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiControlProtectionFault___0x157(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiControlProtectionFault___0x160(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiControlProtectionFault___0x169(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiControlProtectionFault___0x172(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiControlProtectionFault___0x17B(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiControlProtectionFault___0x184(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiControlProtectionFault___0x18D(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiControlProtectionFault___0x196(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiControlProtectionFault___0x19F(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiControlProtectionFault___0x1A8(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiControlProtectionFault___0x1B1(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiControlProtectionFault___0x1BA(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiControlProtectionFault___0x1C3(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiControlProtectionFault___0x1CC(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiControlProtectionFault___0x1D5(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiControlProtectionFault___0x1DE(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiControlProtectionFault___0x1E7(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiControlProtectionFault___0x1F0(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiControlProtectionFault___0x1F9(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiControlProtectionFault___0x202(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiControlProtectionFault___0x20B(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiControlProtectionFault___0x214(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiControlProtectionFault___0x21D(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiControlProtectionFault___0x226(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiControlProtectionFault___0x22F(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiControlProtectionFault___0x238(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiControlProtectionFault___0x241(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiControlProtectionFault___0x24A(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiControlProtectionFault___0x253(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiControlProtectionFault___0x25C(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = (unsigned int)(0xDADAULL);
    if (((*(unsigned __int8 *)(gs_base + (0 + 2140))) & (8)) != 0) {
        result = 32;
    }
    if ((((unsigned int)(a2)) & (128)) != 0) {
        result = KiFlushBhbDuringTrapEntryOrExit(a1, a2, a3, a4);
    }
    *(unsigned __int8 *)(gs_base + (0 + 2142)) = 0;
    if ((*(unsigned int *)(v_rip + 9453432)) == 0) goto loc_006C330D;
    if (((unsigned int)(a2)) == 0) goto loc_006C330D;
    a2 = (unsigned int)((a2) & (*(unsigned int *)(v_rip + 9453410)));
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
    if (((*(unsigned __int8 *)(v_rip + 9451667)) & (255)) == 0) goto loc_006C336B;
    if (((v_stack_p10) & (1)) != 0) {
    }
    if (((v_stack_p18) & (512)) != 0) {
    }
    if (((*(unsigned __int8 *)(gs_base + (0 + 37157))) & (64)) == 0) goto loc_006C3420;
    result = KiProcessControlProtection(v_stack_m160, a2, a3, a4);
    if (((unsigned int)(result)) == 1) goto loc_006C3443;
    if (((unsigned int)(result)) == 2) goto loc_006C33AF;
    if (((unsigned int)(result)) == 3) goto loc_006C342F;
    goto loc_006C3420;
loc_006C33AF:
    if (((v_stack_p10) & (1)) == 0) goto loc_006C33FB;
    a2 = (a2) << (32);
    result = (result) | (a2);
    v_r11 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544) + 1876))) & (0xC0F6C000ULL));
    a2 = ((unsigned int)(*(unsigned int *)(v_rip + 9452179))) << (32);
    v_r11 = (v_r11) | (a2);
    goto loc_006C3407;
loc_006C33FB:
loc_006C3407:
    result = KiFastFailDispatch((unsigned int)(0xC0000409ULL), 2, v_stack_p8, 57);
loc_006C3420:
    result = KiBugCheckDispatch(127, 21, v_stack_p8, 57);
loc_006C342F:
    a2 = 0;
    result = KiExceptionDispatch((unsigned int)(0x80000033ULL), a2, v_stack_p8, 57);
loc_006C3443:
    if (((v_stack_p10) & (1)) == 0) goto loc_006C3746;
    if (((*(unsigned __int8 *)(v_rip + 9451416)) & (255)) != 0) {
    }
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 194)) & (3)) == 0) goto loc_006C348A;
    result = KiInitiateUserApc(1, a2, v_stack_p8, 57);
    goto loc_006C345D;
loc_006C348A:
    result = KiSynchronizeUserIsolationDomainEntry(0, a2, v_stack_p8, 57);
    if ((unsigned int)(result) != 0) goto loc_006C345D;
    result = v_stack_m130;
    if (((*(unsigned __int8 *)(gs_base + (0 + 2144))) & (2)) != 0) {
        a1 = 0;
        result = KiUpdateStibpPairing(a1, a2, v_stack_p8, 57);
    }
    if (((*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)))) & (0x8000000ULL)) != 0) {
        result = KiRestoreSetContextState(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, v_stack_p8, 57);
    }
    if (((*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)))) & (0x10000ULL)) == 0) goto loc_006C34E4;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 2)) & (1)) != 0) {
        result = KiCopyCounters(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, v_stack_p8, 57);
        a1 = *(unsigned __int64 *)(gs_base + (0 + 392));
    }
    if (v_stack_m60 != 0) {
        result = KiRestoreDebugRegisterState(a1, a2, v_stack_p8, 57);
    }
    if (v_stack_m60 >= 0) goto loc_006C3531;
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
    if (condition_is_above_or_equal) goto loc_006C36C3;
    result = KiControlProtectionFault___0x65F(a1, a2, a3, 57);
    v_rsp = (v_rsp) + (8);
    result = KiControlProtectionFault___0x668(a1, a2, a3, 57);
    v_rsp = (v_rsp) + (8);
    result = KiControlProtectionFault___0x551(a1, a2, a3, 57);
    v_rsp = (v_rsp) + (8);
    result = KiControlProtectionFault___0x55A(a1, a2, a3, 57);
    v_rsp = (v_rsp) + (8);
    result = KiControlProtectionFault___0x563(a1, a2, a3, 57);
    v_rsp = (v_rsp) + (8);
    result = KiControlProtectionFault___0x56C(a1, a2, a3, 57);
    v_rsp = (v_rsp) + (8);
    result = KiControlProtectionFault___0x575(a1, a2, a3, 57);
    v_rsp = (v_rsp) + (8);
    result = KiControlProtectionFault___0x57E(a1, a2, a3, 57);
    v_rsp = (v_rsp) + (8);
    result = KiControlProtectionFault___0x587(a1, a2, a3, 57);
    v_rsp = (v_rsp) + (8);
    result = KiControlProtectionFault___0x590(a1, a2, a3, 57);
    v_rsp = (v_rsp) + (8);
    result = KiControlProtectionFault___0x599(a1, a2, a3, 57);
    v_rsp = (v_rsp) + (8);
    result = KiControlProtectionFault___0x5A2(a1, a2, a3, 57);
    v_rsp = (v_rsp) + (8);
    result = KiControlProtectionFault___0x5AB(a1, a2, a3, 57);
    v_rsp = (v_rsp) + (8);
    result = KiControlProtectionFault___0x5B4(a1, a2, a3, 57);
    v_rsp = (v_rsp) + (8);
    result = KiControlProtectionFault___0x5BD(a1, a2, a3, 57);
    v_rsp = (v_rsp) + (8);
    result = KiControlProtectionFault___0x5C6(a1, a2, a3, 57);
    v_rsp = (v_rsp) + (8);
    result = KiControlProtectionFault___0x5CF(a1, a2, a3, 57);
    v_rsp = (v_rsp) + (8);
    result = KiControlProtectionFault___0x5D8(a1, a2, a3, 57);
    v_rsp = (v_rsp) + (8);
    result = KiControlProtectionFault___0x5E1(a1, a2, a3, 57);
    v_rsp = (v_rsp) + (8);
    result = KiControlProtectionFault___0x5EA(a1, a2, a3, 57);
    v_rsp = (v_rsp) + (8);
    result = KiControlProtectionFault___0x5F3(a1, a2, a3, 57);
    v_rsp = (v_rsp) + (8);
    result = KiControlProtectionFault___0x5FC(a1, a2, a3, 57);
    v_rsp = (v_rsp) + (8);
    result = KiControlProtectionFault___0x605(a1, a2, a3, 57);
    v_rsp = (v_rsp) + (8);
    result = KiControlProtectionFault___0x60E(a1, a2, a3, 57);
    v_rsp = (v_rsp) + (8);
    result = KiControlProtectionFault___0x617(a1, a2, a3, 57);
    v_rsp = (v_rsp) + (8);
    result = KiControlProtectionFault___0x620(a1, a2, a3, 57);
    v_rsp = (v_rsp) + (8);
    result = KiControlProtectionFault___0x629(a1, a2, a3, 57);
    v_rsp = (v_rsp) + (8);
    result = KiControlProtectionFault___0x632(a1, a2, a3, 57);
    v_rsp = (v_rsp) + (8);
    result = KiControlProtectionFault___0x63B(a1, a2, a3, 57);
    v_rsp = (v_rsp) + (8);
    result = KiControlProtectionFault___0x644(a1, a2, a3, 57);
    v_rsp = (v_rsp) + (8);
    result = KiControlProtectionFault___0x64D(a1, a2, a3, 57);
    v_rsp = (v_rsp) + (8);
    result = KiControlProtectionFault___0x656(a1, a2, a3, 57);
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
    if (((*(unsigned __int8 *)(v_rip + 11788568)) & (1)) == 0) goto loc_006C372F;
loc_006C372F:
    if (((*(unsigned __int16 *)(gs_base + (0 + 2136))) & (512)) != 0) {
    }
loc_006C3746:
    v_rsp = (v_stack_m8) + (232);
    return v_stack_m130;
}
```

## 5. (Beta) C Style

```c
int64_t KiControlProtectionFault(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint16_t Arg5)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint32_t v_stack_m134;
    uint8_t v_stack_m135;
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
    uint32_t v_stack_p0;
    uint8_t v_stack_p10;
    uint32_t v_stack_p18;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (344);
    v_stack_m135 = 1;
    v_stack_m130 = result;
    v_stack_m128 = Arg1;
    v_stack_m120 = Arg2;
    v_stack_m118 = Arg3;
    v_stack_m110 = Arg4;
    v_stack_m108 = local_r10;
    v_stack_m100 = local_r11;
    if (((v_stack_p10) & (1)) != 0) goto loc_006C30B1;
    Arg2 = 0;
    v_stack_m88 = 0;
    if (((*(uint8_t *)(gs_base + (0 + 0x858))) & (1)) != 0) goto loc_006C309A;
    goto loc_006C3322;
loc_006C309A:
    Arg2 = 0;
    goto loc_006C3322;
loc_006C30B1:
    if (((*(uint8_t *)(v_rip + 0xB3E788)) & (1)) == 0) {
    }
    if (*(uint64_t *)(gs_base + (0 + 0x9D28)) == 0) goto loc_006C30ED;
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
    if ((((uint32_t)(Arg2)) & (2)) == 0) goto loc_006C32C9;
    result = KiControlProtectionFault___0x265(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiControlProtectionFault___0x26E(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiControlProtectionFault___0x157(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiControlProtectionFault___0x160(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiControlProtectionFault___0x169(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiControlProtectionFault___0x172(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiControlProtectionFault___0x17B(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiControlProtectionFault___0x184(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiControlProtectionFault___0x18D(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiControlProtectionFault___0x196(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiControlProtectionFault___0x19F(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiControlProtectionFault___0x1A8(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiControlProtectionFault___0x1B1(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiControlProtectionFault___0x1BA(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiControlProtectionFault___0x1C3(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiControlProtectionFault___0x1CC(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiControlProtectionFault___0x1D5(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiControlProtectionFault___0x1DE(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiControlProtectionFault___0x1E7(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiControlProtectionFault___0x1F0(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiControlProtectionFault___0x1F9(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiControlProtectionFault___0x202(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiControlProtectionFault___0x20B(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiControlProtectionFault___0x214(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiControlProtectionFault___0x21D(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiControlProtectionFault___0x226(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiControlProtectionFault___0x22F(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiControlProtectionFault___0x238(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiControlProtectionFault___0x241(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiControlProtectionFault___0x24A(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiControlProtectionFault___0x253(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiControlProtectionFault___0x25C(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = (uint32_t)(0xDADAULL);
    if (((*(uint8_t *)(gs_base + (0 + 0x85C))) & (8)) != 0) {
        result = 32;
    }
    if ((((uint32_t)(Arg2)) & (128)) != 0) {
        result = KiFlushBhbDuringTrapEntryOrExit(Arg1, Arg2, Arg3, Arg4);
    }
    *(uint8_t *)(gs_base + (0 + 0x85E)) = 0;
    if ((*(uint32_t *)(v_rip + 0x903F78)) == 0) goto loc_006C330D;
    if (((uint32_t)(Arg2)) == 0) goto loc_006C330D;
    Arg2 = (uint32_t)((Arg2) & (*(uint32_t *)(v_rip + 0x903F62)));
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
    if (((*(uint8_t *)(v_rip + 0x903893)) & (255)) == 0) goto loc_006C336B;
    if (((v_stack_p10) & (1)) != 0) {
    }
    if (((v_stack_p18) & (512)) != 0) {
    }
    if (((*(uint8_t *)(gs_base + (0 + 0x9125))) & (64)) == 0) goto loc_006C3420;
    result = KiProcessControlProtection(v_stack_m160, Arg2, Arg3, Arg4);
    if (((uint32_t)(result)) == 1) goto loc_006C3443;
    if (((uint32_t)(result)) == 2) goto loc_006C33AF;
    if (((uint32_t)(result)) == 3) goto loc_006C342F;
    goto loc_006C3420;
loc_006C33AF:
    if (((v_stack_p10) & (1)) == 0) goto loc_006C33FB;
    Arg2 = (Arg2) << (32);
    result = (result) | (Arg2);
    local_r11 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220) + 0x754))) & (0xC0F6C000ULL));
    Arg2 = ((uint32_t)(*(uint32_t *)(v_rip + 0x903A93))) << (32);
    local_r11 = (local_r11) | (Arg2);
    goto loc_006C3407;
loc_006C33FB:
loc_006C3407:
    result = KiFastFailDispatch((uint32_t)(0xC0000409ULL), 2, v_stack_p8, 57);
loc_006C3420:
    result = KiBugCheckDispatch(127, 21, v_stack_p8, 57);
loc_006C342F:
    Arg2 = 0;
    result = KiExceptionDispatch((uint32_t)(0x80000033ULL), Arg2, v_stack_p8, 57);
loc_006C3443:
    if (((v_stack_p10) & (1)) == 0) goto loc_006C3746;
    if (((*(uint8_t *)(v_rip + 0x903798)) & (255)) != 0) {
    }
    if (((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xC2)) & (3)) == 0) goto loc_006C348A;
    result = KiInitiateUserApc(1, Arg2, v_stack_p8, 57);
    goto loc_006C345D;
loc_006C348A:
    result = KiSynchronizeUserIsolationDomainEntry(0, Arg2, v_stack_p8, 57);
    if ((uint32_t)(result) != 0) goto loc_006C345D;
    result = v_stack_m130;
    if (((*(uint8_t *)(gs_base + (0 + 0x860))) & (2)) != 0) {
        Arg1 = 0;
        result = KiUpdateStibpPairing(Arg1, Arg2, v_stack_p8, 57);
    }
    if (((*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)))) & (0x8000000ULL)) != 0) {
        result = KiRestoreSetContextState(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, v_stack_p8, 57);
    }
    if (((*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)))) & (0x10000ULL)) == 0) goto loc_006C34E4;
    if (((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x2)) & (1)) != 0) {
        result = KiCopyCounters(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, v_stack_p8, 57);
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x188));
    }
    if (v_stack_m60 != 0) {
        result = KiRestoreDebugRegisterState(Arg1, Arg2, v_stack_p8, 57);
    }
    if (v_stack_m60 >= 0) goto loc_006C3531;
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
    if (condition_is_above_or_equal) goto loc_006C36C3;
    result = KiControlProtectionFault___0x65F(Arg1, Arg2, Arg3, 57);
    local_rsp = (local_rsp) + (8);
    result = KiControlProtectionFault___0x668(Arg1, Arg2, Arg3, 57);
    local_rsp = (local_rsp) + (8);
    result = KiControlProtectionFault___0x551(Arg1, Arg2, Arg3, 57);
    local_rsp = (local_rsp) + (8);
    result = KiControlProtectionFault___0x55A(Arg1, Arg2, Arg3, 57);
    local_rsp = (local_rsp) + (8);
    result = KiControlProtectionFault___0x563(Arg1, Arg2, Arg3, 57);
    local_rsp = (local_rsp) + (8);
    result = KiControlProtectionFault___0x56C(Arg1, Arg2, Arg3, 57);
    local_rsp = (local_rsp) + (8);
    result = KiControlProtectionFault___0x575(Arg1, Arg2, Arg3, 57);
    local_rsp = (local_rsp) + (8);
    result = KiControlProtectionFault___0x57E(Arg1, Arg2, Arg3, 57);
    local_rsp = (local_rsp) + (8);
    result = KiControlProtectionFault___0x587(Arg1, Arg2, Arg3, 57);
    local_rsp = (local_rsp) + (8);
    result = KiControlProtectionFault___0x590(Arg1, Arg2, Arg3, 57);
    local_rsp = (local_rsp) + (8);
    result = KiControlProtectionFault___0x599(Arg1, Arg2, Arg3, 57);
    local_rsp = (local_rsp) + (8);
    result = KiControlProtectionFault___0x5A2(Arg1, Arg2, Arg3, 57);
    local_rsp = (local_rsp) + (8);
    result = KiControlProtectionFault___0x5AB(Arg1, Arg2, Arg3, 57);
    local_rsp = (local_rsp) + (8);
    result = KiControlProtectionFault___0x5B4(Arg1, Arg2, Arg3, 57);
    local_rsp = (local_rsp) + (8);
    result = KiControlProtectionFault___0x5BD(Arg1, Arg2, Arg3, 57);
    local_rsp = (local_rsp) + (8);
    result = KiControlProtectionFault___0x5C6(Arg1, Arg2, Arg3, 57);
    local_rsp = (local_rsp) + (8);
    result = KiControlProtectionFault___0x5CF(Arg1, Arg2, Arg3, 57);
    local_rsp = (local_rsp) + (8);
    result = KiControlProtectionFault___0x5D8(Arg1, Arg2, Arg3, 57);
    local_rsp = (local_rsp) + (8);
    result = KiControlProtectionFault___0x5E1(Arg1, Arg2, Arg3, 57);
    local_rsp = (local_rsp) + (8);
    result = KiControlProtectionFault___0x5EA(Arg1, Arg2, Arg3, 57);
    local_rsp = (local_rsp) + (8);
    result = KiControlProtectionFault___0x5F3(Arg1, Arg2, Arg3, 57);
    local_rsp = (local_rsp) + (8);
    result = KiControlProtectionFault___0x5FC(Arg1, Arg2, Arg3, 57);
    local_rsp = (local_rsp) + (8);
    result = KiControlProtectionFault___0x605(Arg1, Arg2, Arg3, 57);
    local_rsp = (local_rsp) + (8);
    result = KiControlProtectionFault___0x60E(Arg1, Arg2, Arg3, 57);
    local_rsp = (local_rsp) + (8);
    result = KiControlProtectionFault___0x617(Arg1, Arg2, Arg3, 57);
    local_rsp = (local_rsp) + (8);
    result = KiControlProtectionFault___0x620(Arg1, Arg2, Arg3, 57);
    local_rsp = (local_rsp) + (8);
    result = KiControlProtectionFault___0x629(Arg1, Arg2, Arg3, 57);
    local_rsp = (local_rsp) + (8);
    result = KiControlProtectionFault___0x632(Arg1, Arg2, Arg3, 57);
    local_rsp = (local_rsp) + (8);
    result = KiControlProtectionFault___0x63B(Arg1, Arg2, Arg3, 57);
    local_rsp = (local_rsp) + (8);
    result = KiControlProtectionFault___0x644(Arg1, Arg2, Arg3, 57);
    local_rsp = (local_rsp) + (8);
    result = KiControlProtectionFault___0x64D(Arg1, Arg2, Arg3, 57);
    local_rsp = (local_rsp) + (8);
    result = KiControlProtectionFault___0x656(Arg1, Arg2, Arg3, 57);
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
    if (((*(uint8_t *)(v_rip + 0xB3E118)) & (1)) == 0) goto loc_006C372F;
loc_006C372F:
    if (((*(uint16_t *)(gs_base + (0 + 0x858))) & (512)) != 0) {
    }
loc_006C3746:
    local_rsp = (v_stack_m8) + (232);
    return v_stack_m130;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006C3040&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
