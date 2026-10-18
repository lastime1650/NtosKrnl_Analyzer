# KiInvalidOpcodeFault

- RVA: `0x006BE740`–`0x006BEDDE` (길이 `1,694` bytes)
- VA: `0x00000001406BE740`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C1BD8`
- 디코드: `368`개 명령, `1,694/1,694` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **74**; 고유 호출 대상: **74**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x006BE896` → [KiInvalidOpcodeFault + 0x269](KiInvalidOpcodeFault_function_006BE740.md) (inside-function, `0x006BE9A9`)
- `0x006BE89F` → [KiInvalidOpcodeFault + 0x272](KiInvalidOpcodeFault_function_006BE740.md) (inside-function, `0x006BE9B2`)
- `0x006BE8A8` → [KiInvalidOpcodeFault + 0x15B](KiInvalidOpcodeFault_function_006BE740.md) (inside-function, `0x006BE89B`)
- `0x006BE8B1` → [KiInvalidOpcodeFault + 0x164](KiInvalidOpcodeFault_function_006BE740.md) (inside-function, `0x006BE8A4`)
- `0x006BE8BA` → [KiInvalidOpcodeFault + 0x16D](KiInvalidOpcodeFault_function_006BE740.md) (inside-function, `0x006BE8AD`)
- `0x006BE8C3` → [KiInvalidOpcodeFault + 0x176](KiInvalidOpcodeFault_function_006BE740.md) (inside-function, `0x006BE8B6`)
- `0x006BE8CC` → [KiInvalidOpcodeFault + 0x17F](KiInvalidOpcodeFault_function_006BE740.md) (inside-function, `0x006BE8BF`)
- `0x006BE8D5` → [KiInvalidOpcodeFault + 0x188](KiInvalidOpcodeFault_function_006BE740.md) (inside-function, `0x006BE8C8`)
- `0x006BE8DE` → [KiInvalidOpcodeFault + 0x191](KiInvalidOpcodeFault_function_006BE740.md) (inside-function, `0x006BE8D1`)
- `0x006BE8E7` → [KiInvalidOpcodeFault + 0x19A](KiInvalidOpcodeFault_function_006BE740.md) (inside-function, `0x006BE8DA`)
- `0x006BE8F0` → [KiInvalidOpcodeFault + 0x1A3](KiInvalidOpcodeFault_function_006BE740.md) (inside-function, `0x006BE8E3`)
- `0x006BE8F9` → [KiInvalidOpcodeFault + 0x1AC](KiInvalidOpcodeFault_function_006BE740.md) (inside-function, `0x006BE8EC`)
- `0x006BE902` → [KiInvalidOpcodeFault + 0x1B5](KiInvalidOpcodeFault_function_006BE740.md) (inside-function, `0x006BE8F5`)
- `0x006BE90B` → [KiInvalidOpcodeFault + 0x1BE](KiInvalidOpcodeFault_function_006BE740.md) (inside-function, `0x006BE8FE`)
- `0x006BE914` → [KiInvalidOpcodeFault + 0x1C7](KiInvalidOpcodeFault_function_006BE740.md) (inside-function, `0x006BE907`)
- `0x006BE91D` → [KiInvalidOpcodeFault + 0x1D0](KiInvalidOpcodeFault_function_006BE740.md) (inside-function, `0x006BE910`)
- `0x006BE926` → [KiInvalidOpcodeFault + 0x1D9](KiInvalidOpcodeFault_function_006BE740.md) (inside-function, `0x006BE919`)
- `0x006BE92F` → [KiInvalidOpcodeFault + 0x1E2](KiInvalidOpcodeFault_function_006BE740.md) (inside-function, `0x006BE922`)
- `0x006BE938` → [KiInvalidOpcodeFault + 0x1EB](KiInvalidOpcodeFault_function_006BE740.md) (inside-function, `0x006BE92B`)
- `0x006BE941` → [KiInvalidOpcodeFault + 0x1F4](KiInvalidOpcodeFault_function_006BE740.md) (inside-function, `0x006BE934`)
- `0x006BE94A` → [KiInvalidOpcodeFault + 0x1FD](KiInvalidOpcodeFault_function_006BE740.md) (inside-function, `0x006BE93D`)
- `0x006BE953` → [KiInvalidOpcodeFault + 0x206](KiInvalidOpcodeFault_function_006BE740.md) (inside-function, `0x006BE946`)
- `0x006BE95C` → [KiInvalidOpcodeFault + 0x20F](KiInvalidOpcodeFault_function_006BE740.md) (inside-function, `0x006BE94F`)
- `0x006BE965` → [KiInvalidOpcodeFault + 0x218](KiInvalidOpcodeFault_function_006BE740.md) (inside-function, `0x006BE958`)
- `0x006BE96E` → [KiInvalidOpcodeFault + 0x221](KiInvalidOpcodeFault_function_006BE740.md) (inside-function, `0x006BE961`)
- `0x006BE977` → [KiInvalidOpcodeFault + 0x22A](KiInvalidOpcodeFault_function_006BE740.md) (inside-function, `0x006BE96A`)
- `0x006BE980` → [KiInvalidOpcodeFault + 0x233](KiInvalidOpcodeFault_function_006BE740.md) (inside-function, `0x006BE973`)
- `0x006BE989` → [KiInvalidOpcodeFault + 0x23C](KiInvalidOpcodeFault_function_006BE740.md) (inside-function, `0x006BE97C`)
- `0x006BE992` → [KiInvalidOpcodeFault + 0x245](KiInvalidOpcodeFault_function_006BE740.md) (inside-function, `0x006BE985`)
- `0x006BE99B` → [KiInvalidOpcodeFault + 0x24E](KiInvalidOpcodeFault_function_006BE740.md) (inside-function, `0x006BE98E`)
- `0x006BE9A4` → [KiInvalidOpcodeFault + 0x257](KiInvalidOpcodeFault_function_006BE740.md) (inside-function, `0x006BE997`)
- `0x006BE9AD` → [KiInvalidOpcodeFault + 0x260](KiInvalidOpcodeFault_function_006BE740.md) (inside-function, `0x006BE9A0`)
- `0x006BE9D8` → [KiFlushBhbDuringTrapEntryOrExit](../6C/KiFlushBhbDuringTrapEntryOrExit_function_006C6340.md) (function, `0x006C6340`)
- `0x006BEA21` → [KiSaveDebugRegisterState](../4F/KiSaveDebugRegisterState_function_004FD960.md) (function, `0x004FD960`)
- `0x006BEA55` → [KiSynchronizeUserIsolationDomainExit](../41/KiSynchronizeUserIsolationDomainExit_function_0041BFA0.md) (function, `0x0041BFA0`)
- `0x006BEA8A` → [KiExceptionDispatch](../6C/KiExceptionDispatch_function_006C5900.md) (function, `0x006C5900`)
- `0x006BEAC6` → [KiInitiateUserApc](KiInitiateUserApc_function_006B6540.md) (function, `0x006B6540`)
- `0x006BEAD7` → [KiSynchronizeUserIsolationDomainEntry](../26/KiSynchronizeUserIsolationDomainEntry_function_00263F60.md) (function, `0x00263F60`)
- `0x006BEAF1` → [KiUpdateStibpPairing](../3E/KiUpdateStibpPairing_function_003E71C0.md) (function, `0x003E71C0`)
- `0x006BEB07` → [KiRestoreSetContextState](KiRestoreSetContextState_function_006B1CA0.md) (function, `0x006B1CA0`)
- `0x006BEB23` → [KiCopyCounters](../5C/KiCopyCounters_function_005C0710.md) (function, `0x005C0710`)
- `0x006BEB3F` → [KiRestoreDebugRegisterState](../4F/KiRestoreDebugRegisterState_function_004FD8E0.md) (function, `0x004FD8E0`)
- `0x006BEBD9` → [KiInvalidOpcodeFault + 0x5AC](KiInvalidOpcodeFault_function_006BE740.md) (inside-function, `0x006BECEC`)
- `0x006BEBE2` → [KiInvalidOpcodeFault + 0x5B5](KiInvalidOpcodeFault_function_006BE740.md) (inside-function, `0x006BECF5`)
- `0x006BEBEB` → [KiInvalidOpcodeFault + 0x49E](KiInvalidOpcodeFault_function_006BE740.md) (inside-function, `0x006BEBDE`)
- `0x006BEBF4` → [KiInvalidOpcodeFault + 0x4A7](KiInvalidOpcodeFault_function_006BE740.md) (inside-function, `0x006BEBE7`)
- `0x006BEBFD` → [KiInvalidOpcodeFault + 0x4B0](KiInvalidOpcodeFault_function_006BE740.md) (inside-function, `0x006BEBF0`)
- `0x006BEC06` → [KiInvalidOpcodeFault + 0x4B9](KiInvalidOpcodeFault_function_006BE740.md) (inside-function, `0x006BEBF9`)
- `0x006BEC0F` → [KiInvalidOpcodeFault + 0x4C2](KiInvalidOpcodeFault_function_006BE740.md) (inside-function, `0x006BEC02`)
- `0x006BEC18` → [KiInvalidOpcodeFault + 0x4CB](KiInvalidOpcodeFault_function_006BE740.md) (inside-function, `0x006BEC0B`)
- `0x006BEC21` → [KiInvalidOpcodeFault + 0x4D4](KiInvalidOpcodeFault_function_006BE740.md) (inside-function, `0x006BEC14`)
- `0x006BEC2A` → [KiInvalidOpcodeFault + 0x4DD](KiInvalidOpcodeFault_function_006BE740.md) (inside-function, `0x006BEC1D`)
- `0x006BEC33` → [KiInvalidOpcodeFault + 0x4E6](KiInvalidOpcodeFault_function_006BE740.md) (inside-function, `0x006BEC26`)
- `0x006BEC3C` → [KiInvalidOpcodeFault + 0x4EF](KiInvalidOpcodeFault_function_006BE740.md) (inside-function, `0x006BEC2F`)
- `0x006BEC45` → [KiInvalidOpcodeFault + 0x4F8](KiInvalidOpcodeFault_function_006BE740.md) (inside-function, `0x006BEC38`)
- `0x006BEC4E` → [KiInvalidOpcodeFault + 0x501](KiInvalidOpcodeFault_function_006BE740.md) (inside-function, `0x006BEC41`)
- `0x006BEC57` → [KiInvalidOpcodeFault + 0x50A](KiInvalidOpcodeFault_function_006BE740.md) (inside-function, `0x006BEC4A`)
- `0x006BEC60` → [KiInvalidOpcodeFault + 0x513](KiInvalidOpcodeFault_function_006BE740.md) (inside-function, `0x006BEC53`)
- `0x006BEC69` → [KiInvalidOpcodeFault + 0x51C](KiInvalidOpcodeFault_function_006BE740.md) (inside-function, `0x006BEC5C`)
- `0x006BEC72` → [KiInvalidOpcodeFault + 0x525](KiInvalidOpcodeFault_function_006BE740.md) (inside-function, `0x006BEC65`)
- `0x006BEC7B` → [KiInvalidOpcodeFault + 0x52E](KiInvalidOpcodeFault_function_006BE740.md) (inside-function, `0x006BEC6E`)
- `0x006BEC84` → [KiInvalidOpcodeFault + 0x537](KiInvalidOpcodeFault_function_006BE740.md) (inside-function, `0x006BEC77`)
- `0x006BEC8D` → [KiInvalidOpcodeFault + 0x540](KiInvalidOpcodeFault_function_006BE740.md) (inside-function, `0x006BEC80`)
- `0x006BEC96` → [KiInvalidOpcodeFault + 0x549](KiInvalidOpcodeFault_function_006BE740.md) (inside-function, `0x006BEC89`)
- `0x006BEC9F` → [KiInvalidOpcodeFault + 0x552](KiInvalidOpcodeFault_function_006BE740.md) (inside-function, `0x006BEC92`)
- `0x006BECA8` → [KiInvalidOpcodeFault + 0x55B](KiInvalidOpcodeFault_function_006BE740.md) (inside-function, `0x006BEC9B`)
- `0x006BECB1` → [KiInvalidOpcodeFault + 0x564](KiInvalidOpcodeFault_function_006BE740.md) (inside-function, `0x006BECA4`)
- `0x006BECBA` → [KiInvalidOpcodeFault + 0x56D](KiInvalidOpcodeFault_function_006BE740.md) (inside-function, `0x006BECAD`)
- `0x006BECC3` → [KiInvalidOpcodeFault + 0x576](KiInvalidOpcodeFault_function_006BE740.md) (inside-function, `0x006BECB6`)
- `0x006BECCC` → [KiInvalidOpcodeFault + 0x57F](KiInvalidOpcodeFault_function_006BE740.md) (inside-function, `0x006BECBF`)
- `0x006BECD5` → [KiInvalidOpcodeFault + 0x588](KiInvalidOpcodeFault_function_006BE740.md) (inside-function, `0x006BECC8`)
- `0x006BECDE` → [KiInvalidOpcodeFault + 0x591](KiInvalidOpcodeFault_function_006BE740.md) (inside-function, `0x006BECD1`)
- `0x006BECE7` → [KiInvalidOpcodeFault + 0x59A](KiInvalidOpcodeFault_function_006BE740.md) (inside-function, `0x006BECDA`)
- `0x006BECF0` → [KiInvalidOpcodeFault + 0x5A3](KiInvalidOpcodeFault_function_006BE740.md) (inside-function, `0x006BECE3`)

### Direct callers
- [KiInvalidOpcodeFault](KiInvalidOpcodeFault_function_006BE740.md) at `0x006BE896`
- [KiInvalidOpcodeFault](KiInvalidOpcodeFault_function_006BE740.md) at `0x006BE89F`
- [KiInvalidOpcodeFault](KiInvalidOpcodeFault_function_006BE740.md) at `0x006BE8A8`
- [KiInvalidOpcodeFault](KiInvalidOpcodeFault_function_006BE740.md) at `0x006BE8B1`
- [KiInvalidOpcodeFault](KiInvalidOpcodeFault_function_006BE740.md) at `0x006BE8BA`
- [KiInvalidOpcodeFault](KiInvalidOpcodeFault_function_006BE740.md) at `0x006BE8C3`
- [KiInvalidOpcodeFault](KiInvalidOpcodeFault_function_006BE740.md) at `0x006BE8CC`
- [KiInvalidOpcodeFault](KiInvalidOpcodeFault_function_006BE740.md) at `0x006BE8D5`
- [KiInvalidOpcodeFault](KiInvalidOpcodeFault_function_006BE740.md) at `0x006BE8DE`
- [KiInvalidOpcodeFault](KiInvalidOpcodeFault_function_006BE740.md) at `0x006BE8E7`
- [KiInvalidOpcodeFault](KiInvalidOpcodeFault_function_006BE740.md) at `0x006BE8F0`
- [KiInvalidOpcodeFault](KiInvalidOpcodeFault_function_006BE740.md) at `0x006BE8F9`
- [KiInvalidOpcodeFault](KiInvalidOpcodeFault_function_006BE740.md) at `0x006BE902`
- [KiInvalidOpcodeFault](KiInvalidOpcodeFault_function_006BE740.md) at `0x006BE90B`
- [KiInvalidOpcodeFault](KiInvalidOpcodeFault_function_006BE740.md) at `0x006BE914`
- [KiInvalidOpcodeFault](KiInvalidOpcodeFault_function_006BE740.md) at `0x006BE91D`
- [KiInvalidOpcodeFault](KiInvalidOpcodeFault_function_006BE740.md) at `0x006BE926`
- [KiInvalidOpcodeFault](KiInvalidOpcodeFault_function_006BE740.md) at `0x006BE92F`
- [KiInvalidOpcodeFault](KiInvalidOpcodeFault_function_006BE740.md) at `0x006BE938`
- [KiInvalidOpcodeFault](KiInvalidOpcodeFault_function_006BE740.md) at `0x006BE941`
- [KiInvalidOpcodeFault](KiInvalidOpcodeFault_function_006BE740.md) at `0x006BE94A`
- [KiInvalidOpcodeFault](KiInvalidOpcodeFault_function_006BE740.md) at `0x006BE953`
- [KiInvalidOpcodeFault](KiInvalidOpcodeFault_function_006BE740.md) at `0x006BE95C`
- [KiInvalidOpcodeFault](KiInvalidOpcodeFault_function_006BE740.md) at `0x006BE965`
- [KiInvalidOpcodeFault](KiInvalidOpcodeFault_function_006BE740.md) at `0x006BE96E`
- [KiInvalidOpcodeFault](KiInvalidOpcodeFault_function_006BE740.md) at `0x006BE977`
- [KiInvalidOpcodeFault](KiInvalidOpcodeFault_function_006BE740.md) at `0x006BE980`
- [KiInvalidOpcodeFault](KiInvalidOpcodeFault_function_006BE740.md) at `0x006BE989`
- [KiInvalidOpcodeFault](KiInvalidOpcodeFault_function_006BE740.md) at `0x006BE992`
- [KiInvalidOpcodeFault](KiInvalidOpcodeFault_function_006BE740.md) at `0x006BE99B`
- [KiInvalidOpcodeFault](KiInvalidOpcodeFault_function_006BE740.md) at `0x006BE9A4`
- [KiInvalidOpcodeFault](KiInvalidOpcodeFault_function_006BE740.md) at `0x006BE9AD`
- [KiInvalidOpcodeFault](KiInvalidOpcodeFault_function_006BE740.md) at `0x006BEBD9`
- [KiInvalidOpcodeFault](KiInvalidOpcodeFault_function_006BE740.md) at `0x006BEBE2`
- [KiInvalidOpcodeFault](KiInvalidOpcodeFault_function_006BE740.md) at `0x006BEBEB`
- [KiInvalidOpcodeFault](KiInvalidOpcodeFault_function_006BE740.md) at `0x006BEBF4`
- [KiInvalidOpcodeFault](KiInvalidOpcodeFault_function_006BE740.md) at `0x006BEBFD`
- [KiInvalidOpcodeFault](KiInvalidOpcodeFault_function_006BE740.md) at `0x006BEC06`
- [KiInvalidOpcodeFault](KiInvalidOpcodeFault_function_006BE740.md) at `0x006BEC0F`
- [KiInvalidOpcodeFault](KiInvalidOpcodeFault_function_006BE740.md) at `0x006BEC18`
- [KiInvalidOpcodeFault](KiInvalidOpcodeFault_function_006BE740.md) at `0x006BEC21`
- [KiInvalidOpcodeFault](KiInvalidOpcodeFault_function_006BE740.md) at `0x006BEC2A`
- [KiInvalidOpcodeFault](KiInvalidOpcodeFault_function_006BE740.md) at `0x006BEC33`
- [KiInvalidOpcodeFault](KiInvalidOpcodeFault_function_006BE740.md) at `0x006BEC3C`
- [KiInvalidOpcodeFault](KiInvalidOpcodeFault_function_006BE740.md) at `0x006BEC45`
- [KiInvalidOpcodeFault](KiInvalidOpcodeFault_function_006BE740.md) at `0x006BEC4E`
- [KiInvalidOpcodeFault](KiInvalidOpcodeFault_function_006BE740.md) at `0x006BEC57`
- [KiInvalidOpcodeFault](KiInvalidOpcodeFault_function_006BE740.md) at `0x006BEC60`
- [KiInvalidOpcodeFault](KiInvalidOpcodeFault_function_006BE740.md) at `0x006BEC69`
- [KiInvalidOpcodeFault](KiInvalidOpcodeFault_function_006BE740.md) at `0x006BEC72`
- [KiInvalidOpcodeFault](KiInvalidOpcodeFault_function_006BE740.md) at `0x006BEC7B`
- [KiInvalidOpcodeFault](KiInvalidOpcodeFault_function_006BE740.md) at `0x006BEC84`
- [KiInvalidOpcodeFault](KiInvalidOpcodeFault_function_006BE740.md) at `0x006BEC8D`
- [KiInvalidOpcodeFault](KiInvalidOpcodeFault_function_006BE740.md) at `0x006BEC96`
- [KiInvalidOpcodeFault](KiInvalidOpcodeFault_function_006BE740.md) at `0x006BEC9F`
- [KiInvalidOpcodeFault](KiInvalidOpcodeFault_function_006BE740.md) at `0x006BECA8`
- [KiInvalidOpcodeFault](KiInvalidOpcodeFault_function_006BE740.md) at `0x006BECB1`
- [KiInvalidOpcodeFault](KiInvalidOpcodeFault_function_006BE740.md) at `0x006BECBA`
- [KiInvalidOpcodeFault](KiInvalidOpcodeFault_function_006BE740.md) at `0x006BECC3`
- [KiInvalidOpcodeFault](KiInvalidOpcodeFault_function_006BE740.md) at `0x006BECCC`
- [KiInvalidOpcodeFault](KiInvalidOpcodeFault_function_006BE740.md) at `0x006BECD5`
- [KiInvalidOpcodeFault](KiInvalidOpcodeFault_function_006BE740.md) at `0x006BECDE`
- [KiInvalidOpcodeFault](KiInvalidOpcodeFault_function_006BE740.md) at `0x006BECE7`
- [KiInvalidOpcodeFault](KiInvalidOpcodeFault_function_006BE740.md) at `0x006BECF0`

### Static image references
- `0x006BE7B5` → RVA `0x01201840` (`CFGRO`; read)
- `0x006BE9E9` → RVA `0x00FC7264` (`ALMOSTRO`; read)
- `0x006BEA5A` → RVA `0x00FC6BF0` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006BED77` → [KiKernelExit](../../kvascode/BC/KiKernelExit_function_00BCCB80.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006BE740  48 83 EC 08                     sub rsp, 8
006BE744  55                              push rbp
006BE745  48 81 EC 58 01 00 00            sub rsp, 0x158
006BE74C  48 8D AC 24 80 00 00 00         lea rbp, [rsp + 0x80]
006BE754  C6 45 AB 01                     mov byte ptr [rbp - 0x55], 1
006BE758  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
006BE75C  48 89 4D B8                     mov qword ptr [rbp - 0x48], rcx
006BE760  48 89 55 C0                     mov qword ptr [rbp - 0x40], rdx
006BE764  4C 89 45 C8                     mov qword ptr [rbp - 0x38], r8
006BE768  4C 89 4D D0                     mov qword ptr [rbp - 0x30], r9
006BE76C  4C 89 55 D8                     mov qword ptr [rbp - 0x28], r10
006BE770  4C 89 5D E0                     mov qword ptr [rbp - 0x20], r11
006BE774  F6 85 F0 00 00 00 01            test byte ptr [rbp + 0xf0], 1
006BE77B  75 38                           jne 0x1406be7b5
006BE77D  33 D2                           xor edx, edx
006BE77F  F3 48 0F 1E CA                  rdsspq rdx
006BE784  48 89 55 58                     mov qword ptr [rbp + 0x58], rdx
006BE788  0F AE E8                        lfence
006BE78B  65 F6 04 25 58 08 00 00 01      test byte ptr gs:[0x858], 1
006BE794  75 08                           jne 0x1406be79e
006BE796  0F AE E8                        lfence
006BE799  E9 88 02 00 00                  jmp 0x1406bea26
006BE79E  65 0F B7 04 25 66 08 00 00      movzx eax, word ptr gs:[0x866]
006BE7A7  B9 48 00 00 00                  mov ecx, 0x48
006BE7AC  33 D2                           xor edx, edx
006BE7AE  0F 30                           wrmsr
006BE7B0  E9 71 02 00 00                  jmp 0x1406bea26
006BE7B5  F6 05 84 30 B4 00 01            test byte ptr [rip + 0xb43084], 1
006BE7BC  75 03                           jne 0x1406be7c1
006BE7BE  0F 01 F8                        swapgs
006BE7C1  0F AE E8                        lfence
006BE7C4  65 48 8B 0C 25 28 9D 00 00      mov rcx, qword ptr gs:[0x9d28]
006BE7CD  48 85 C9                        test rcx, rcx
006BE7D0  74 1F                           je 0x1406be7f1
006BE7D2  F3 48 0F 1E CA                  rdsspq rdx
006BE7D7  65 4C 8B 14 25 20 9D 00 00      mov r10, qword ptr gs:[0x9d20]
006BE7E0  49 83 C2 08                     add r10, 8
006BE7E4  49 3B D2                        cmp rdx, r10
006BE7E7  75 08                           jne 0x1406be7f1
006BE7E9  F3 0F 01 29                     rstorssp dword ptr [rcx]
006BE7ED  F3 0F 01 EA                     saveprevssp
006BE7F1  65 4C 8B 14 25 88 01 00 00      mov r10, qword ptr gs:[0x188]
006BE7FA  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006BE803  48 8B 89 20 02 00 00            mov rcx, qword ptr [rcx + 0x220]
006BE80A  48 8B 89 60 07 00 00            mov rcx, qword ptr [rcx + 0x760]
006BE811  65 48 89 0C 25 50 08 00 00      mov qword ptr gs:[0x850], rcx
006BE81A  66 65 8B 0C 25 62 08 00 00      mov cx, word ptr gs:[0x862]
006BE823  66 65 89 0C 25 64 08 00 00      mov word ptr gs:[0x864], cx
006BE82C  65 8A 0C 25 58 08 00 00         mov cl, byte ptr gs:[0x858]
006BE834  65 88 0C 25 5A 08 00 00         mov byte ptr gs:[0x85a], cl
006BE83C  65 0F B7 04 25 68 08 00 00      movzx eax, word ptr gs:[0x868]
006BE845  66 65 39 04 25 66 08 00 00      cmp word ptr gs:[0x866], ax
006BE84E  74 12                           je 0x1406be862
006BE850  66 65 89 04 25 66 08 00 00      mov word ptr gs:[0x866], ax
006BE859  B9 48 00 00 00                  mov ecx, 0x48
006BE85E  33 D2                           xor edx, edx
006BE860  0F 30                           wrmsr
006BE862  65 0F B6 14 25 58 08 00 00      movzx edx, byte ptr gs:[0x858]
006BE86B  F7 C2 08 00 00 00               test edx, 8
006BE871  74 17                           je 0x1406be88a
006BE873  B8 01 00 00 00                  mov eax, 1
006BE878  33 D2                           xor edx, edx
006BE87A  B9 49 00 00 00                  mov ecx, 0x49
006BE87F  0F 30                           wrmsr
006BE881  65 0F B6 14 25 58 08 00 00      movzx edx, byte ptr gs:[0x858]
006BE88A  F7 C2 02 00 00 00               test edx, 2
006BE890  0F 84 37 01 00 00               je 0x1406be9cd
006BE896  E8 0E 01 00 00                  call 0x1406be9a9
006BE89B  48 83 C4 08                     add rsp, 8
006BE89F  E8 0E 01 00 00                  call 0x1406be9b2
006BE8A4  48 83 C4 08                     add rsp, 8
006BE8A8  E8 EE FF FF FF                  call 0x1406be89b
006BE8AD  48 83 C4 08                     add rsp, 8
006BE8B1  E8 EE FF FF FF                  call 0x1406be8a4
006BE8B6  48 83 C4 08                     add rsp, 8
006BE8BA  E8 EE FF FF FF                  call 0x1406be8ad
006BE8BF  48 83 C4 08                     add rsp, 8
006BE8C3  E8 EE FF FF FF                  call 0x1406be8b6
006BE8C8  48 83 C4 08                     add rsp, 8
006BE8CC  E8 EE FF FF FF                  call 0x1406be8bf
006BE8D1  48 83 C4 08                     add rsp, 8
006BE8D5  E8 EE FF FF FF                  call 0x1406be8c8
006BE8DA  48 83 C4 08                     add rsp, 8
006BE8DE  E8 EE FF FF FF                  call 0x1406be8d1
006BE8E3  48 83 C4 08                     add rsp, 8
006BE8E7  E8 EE FF FF FF                  call 0x1406be8da
006BE8EC  48 83 C4 08                     add rsp, 8
006BE8F0  E8 EE FF FF FF                  call 0x1406be8e3
006BE8F5  48 83 C4 08                     add rsp, 8
006BE8F9  E8 EE FF FF FF                  call 0x1406be8ec
006BE8FE  48 83 C4 08                     add rsp, 8
006BE902  E8 EE FF FF FF                  call 0x1406be8f5
006BE907  48 83 C4 08                     add rsp, 8
006BE90B  E8 EE FF FF FF                  call 0x1406be8fe
006BE910  48 83 C4 08                     add rsp, 8
006BE914  E8 EE FF FF FF                  call 0x1406be907
006BE919  48 83 C4 08                     add rsp, 8
006BE91D  E8 EE FF FF FF                  call 0x1406be910
006BE922  48 83 C4 08                     add rsp, 8
006BE926  E8 EE FF FF FF                  call 0x1406be919
006BE92B  48 83 C4 08                     add rsp, 8
006BE92F  E8 EE FF FF FF                  call 0x1406be922
006BE934  48 83 C4 08                     add rsp, 8
006BE938  E8 EE FF FF FF                  call 0x1406be92b
006BE93D  48 83 C4 08                     add rsp, 8
006BE941  E8 EE FF FF FF                  call 0x1406be934
006BE946  48 83 C4 08                     add rsp, 8
006BE94A  E8 EE FF FF FF                  call 0x1406be93d
006BE94F  48 83 C4 08                     add rsp, 8
006BE953  E8 EE FF FF FF                  call 0x1406be946
006BE958  48 83 C4 08                     add rsp, 8
006BE95C  E8 EE FF FF FF                  call 0x1406be94f
006BE961  48 83 C4 08                     add rsp, 8
006BE965  E8 EE FF FF FF                  call 0x1406be958
006BE96A  48 83 C4 08                     add rsp, 8
006BE96E  E8 EE FF FF FF                  call 0x1406be961
006BE973  48 83 C4 08                     add rsp, 8
006BE977  E8 EE FF FF FF                  call 0x1406be96a
006BE97C  48 83 C4 08                     add rsp, 8
006BE980  E8 EE FF FF FF                  call 0x1406be973
006BE985  48 83 C4 08                     add rsp, 8
006BE989  E8 EE FF FF FF                  call 0x1406be97c
006BE98E  48 83 C4 08                     add rsp, 8
006BE992  E8 EE FF FF FF                  call 0x1406be985
006BE997  48 83 C4 08                     add rsp, 8
006BE99B  E8 EE FF FF FF                  call 0x1406be98e
006BE9A0  48 83 C4 08                     add rsp, 8
006BE9A4  E8 EE FF FF FF                  call 0x1406be997
006BE9A9  48 83 C4 08                     add rsp, 8
006BE9AD  E8 EE FF FF FF                  call 0x1406be9a0
006BE9B2  48 83 C4 08                     add rsp, 8
006BE9B6  B8 DA DA 00 00                  mov eax, 0xdada
006BE9BB  65 F6 04 25 5C 08 00 00 08      test byte ptr gs:[0x85c], 8
006BE9C4  74 07                           je 0x1406be9cd
006BE9C6  B0 20                           mov al, 0x20
006BE9C8  F3 48 0F AE E8                  incsspq rax
006BE9CD  F7 C2 80 00 00 00               test edx, 0x80
006BE9D3  74 08                           je 0x1406be9dd
006BE9D5  0F AE E8                        lfence
006BE9D8  E8 63 79 00 00                  call 0x1406c6340
006BE9DD  0F AE E8                        lfence
006BE9E0  65 C6 04 25 5E 08 00 00 00      mov byte ptr gs:[0x85e], 0
006BE9E9  83 3D 74 88 90 00 00            cmp dword ptr [rip + 0x908874], 0
006BE9F0  74 1F                           je 0x1406bea11
006BE9F2  B9 A7 06 00 00                  mov ecx, 0x6a7
006BE9F7  0F 32                           rdmsr
006BE9F9  83 FA 00                        cmp edx, 0
006BE9FC  74 13                           je 0x1406bea11
006BE9FE  8B CA                           mov ecx, edx
006BEA00  23 15 5E 88 90 00               and edx, dword ptr [rip + 0x90885e]
006BEA06  3B D1                           cmp edx, ecx
006BEA08  74 07                           je 0x1406bea11
006BEA0A  B9 A7 06 00 00                  mov ecx, 0x6a7
006BEA0F  0F 30                           wrmsr
006BEA11  41 F6 42 03 03                  test byte ptr [r10 + 3], 3
006BEA16  66 C7 85 80 00 00 00 00 00      mov word ptr [rbp + 0x80], 0
006BEA1F  74 05                           je 0x1406bea26
006BEA21  E8 3A EF E3 FF                  call 0x1404fd960
006BEA26  FC                              cld
006BEA27  0F AE 5D AC                     stmxcsr dword ptr [rbp - 0x54]
006BEA2B  65 0F AE 14 25 80 01 00 00      ldmxcsr dword ptr gs:[0x180]
006BEA34  0F 29 45 F0                     movaps xmmword ptr [rbp - 0x10], xmm0
006BEA38  0F 29 4D 00                     movaps xmmword ptr [rbp], xmm1
006BEA3C  0F 29 55 10                     movaps xmmword ptr [rbp + 0x10], xmm2
006BEA40  0F 29 5D 20                     movaps xmmword ptr [rbp + 0x20], xmm3
006BEA44  0F 29 65 30                     movaps xmmword ptr [rbp + 0x30], xmm4
006BEA48  0F 29 6D 40                     movaps xmmword ptr [rbp + 0x40], xmm5
006BEA4C  F6 85 F0 00 00 00 01            test byte ptr [rbp + 0xf0], 1
006BEA53  74 05                           je 0x1406bea5a
006BEA55  E8 46 D5 D5 FF                  call 0x14041bfa0
006BEA5A  F6 05 8F 81 90 00 FF            test byte ptr [rip + 0x90818f], 0xff
006BEA61  74 0C                           je 0x1406bea6f
006BEA63  F6 85 F0 00 00 00 01            test byte ptr [rbp + 0xf0], 1
006BEA6A  74 03                           je 0x1406bea6f
006BEA6C  0F 01 CB                        stac
006BEA6F  F7 85 F8 00 00 00 00 02 00 00   test dword ptr [rbp + 0xf8], 0x200
006BEA79  74 01                           je 0x1406bea7c
006BEA7B  FB                              sti
006BEA7C  B9 02 00 00 10                  mov ecx, 0x10000002
006BEA81  33 D2                           xor edx, edx
006BEA83  4C 8B 85 E8 00 00 00            mov r8, qword ptr [rbp + 0xe8]
006BEA8A  E8 71 6E 00 00                  call 0x1406c5900
006BEA8F  90                              nop
006BEA90  FA                              cli
006BEA91  F6 85 F0 00 00 00 01            test byte ptr [rbp + 0xf0], 1
006BEA98  0F 84 F5 02 00 00               je 0x1406bed93
006BEA9E  F6 05 4B 81 90 00 FF            test byte ptr [rip + 0x90814b], 0xff
006BEAA5  74 03                           je 0x1406beaaa
006BEAA7  0F 01 CB                        stac
006BEAAA  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006BEAB3  F6 81 C2 00 00 00 03            test byte ptr [rcx + 0xc2], 3
006BEABA  74 1B                           je 0x1406bead7
006BEABC  B9 01 00 00 00                  mov ecx, 1
006BEAC1  44 0F 22 C1                     mov cr8, rcx
006BEAC5  FB                              sti
006BEAC6  E8 75 7A FF FF                  call 0x1406b6540
006BEACB  FA                              cli
006BEACC  B9 00 00 00 00                  mov ecx, 0
006BEAD1  44 0F 22 C1                     mov cr8, rcx
006BEAD5  EB D3                           jmp 0x1406beaaa
006BEAD7  E8 84 54 BA FF                  call 0x140263f60
006BEADC  85 C0                           test eax, eax
006BEADE  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
006BEAE2  75 C6                           jne 0x1406beaaa
006BEAE4  65 F6 04 25 60 08 00 00 02      test byte ptr gs:[0x860], 2
006BEAED  74 07                           je 0x1406beaf6
006BEAEF  33 C9                           xor ecx, ecx
006BEAF1  E8 CA 86 D2 FF                  call 0x1403e71c0
006BEAF6  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006BEAFF  F7 01 00 00 00 08               test dword ptr [rcx], 0x8000000
006BEB05  74 05                           je 0x1406beb0c
006BEB07  E8 94 31 FF FF                  call 0x1406b1ca0
006BEB0C  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006BEB15  F7 01 00 00 01 00               test dword ptr [rcx], 0x10000
006BEB1B  74 14                           je 0x1406beb31
006BEB1D  F6 41 02 01                     test byte ptr [rcx + 2], 1
006BEB21  74 0E                           je 0x1406beb31
006BEB23  E8 E8 1B F0 FF                  call 0x1405c0710
006BEB28  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006BEB31  0F AE 55 AC                     ldmxcsr dword ptr [rbp - 0x54]
006BEB35  66 83 BD 80 00 00 00 00         cmp word ptr [rbp + 0x80], 0
006BEB3D  74 05                           je 0x1406beb44
006BEB3F  E8 9C ED E3 FF                  call 0x1404fd8e0
006BEB44  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006BEB4D  0F BA 61 74 16                  bt dword ptr [rcx + 0x74], 0x16
006BEB52  73 2A                           jae 0x1406beb7e
006BEB54  33 C9                           xor ecx, ecx
006BEB56  F3 48 0F 1E C9                  rdsspq rcx
006BEB5B  65 4C 8B 04 25 28 9D 00 00      mov r8, qword ptr gs:[0x9d28]
006BEB64  49 83 C0 08                     add r8, 8
006BEB68  49 3B C8                        cmp rcx, r8
006BEB6B  75 11                           jne 0x1406beb7e
006BEB6D  65 48 8B 0C 25 20 9D 00 00      mov rcx, qword ptr gs:[0x9d20]
006BEB76  F3 0F 01 29                     rstorssp dword ptr [rcx]
006BEB7A  F3 0F 01 EA                     saveprevssp
006BEB7E  65 C6 04 25 5E 08 00 00 00      mov byte ptr gs:[0x85e], 0
006BEB87  65 0F B7 04 25 6C 08 00 00      movzx eax, word ptr gs:[0x86c]
006BEB90  66 65 39 04 25 66 08 00 00      cmp word ptr gs:[0x866], ax
006BEB99  74 12                           je 0x1406bebad
006BEB9B  66 65 89 04 25 66 08 00 00      mov word ptr gs:[0x866], ax
006BEBA4  B9 48 00 00 00                  mov ecx, 0x48
006BEBA9  33 D2                           xor edx, edx
006BEBAB  0F 30                           wrmsr
006BEBAD  66 65 0F BA 34 25 58 08 00 00 02  btr word ptr gs:[0x858], 2
006BEBB8  73 0E                           jae 0x1406bebc8
006BEBBA  B8 01 00 00 00                  mov eax, 1
006BEBBF  33 D2                           xor edx, edx
006BEBC1  B9 49 00 00 00                  mov ecx, 0x49
006BEBC6  0F 30                           wrmsr
006BEBC8  66 65 0F BA 34 25 58 08 00 00 05  btr word ptr gs:[0x858], 5
006BEBD3  0F 83 37 01 00 00               jae 0x1406bed10
006BEBD9  E8 0E 01 00 00                  call 0x1406becec
006BEBDE  48 83 C4 08                     add rsp, 8
006BEBE2  E8 0E 01 00 00                  call 0x1406becf5
006BEBE7  48 83 C4 08                     add rsp, 8
006BEBEB  E8 EE FF FF FF                  call 0x1406bebde
006BEBF0  48 83 C4 08                     add rsp, 8
006BEBF4  E8 EE FF FF FF                  call 0x1406bebe7
006BEBF9  48 83 C4 08                     add rsp, 8
006BEBFD  E8 EE FF FF FF                  call 0x1406bebf0
006BEC02  48 83 C4 08                     add rsp, 8
006BEC06  E8 EE FF FF FF                  call 0x1406bebf9
006BEC0B  48 83 C4 08                     add rsp, 8
006BEC0F  E8 EE FF FF FF                  call 0x1406bec02
006BEC14  48 83 C4 08                     add rsp, 8
006BEC18  E8 EE FF FF FF                  call 0x1406bec0b
006BEC1D  48 83 C4 08                     add rsp, 8
006BEC21  E8 EE FF FF FF                  call 0x1406bec14
006BEC26  48 83 C4 08                     add rsp, 8
006BEC2A  E8 EE FF FF FF                  call 0x1406bec1d
006BEC2F  48 83 C4 08                     add rsp, 8
006BEC33  E8 EE FF FF FF                  call 0x1406bec26
006BEC38  48 83 C4 08                     add rsp, 8
006BEC3C  E8 EE FF FF FF                  call 0x1406bec2f
006BEC41  48 83 C4 08                     add rsp, 8
006BEC45  E8 EE FF FF FF                  call 0x1406bec38
006BEC4A  48 83 C4 08                     add rsp, 8
006BEC4E  E8 EE FF FF FF                  call 0x1406bec41
006BEC53  48 83 C4 08                     add rsp, 8
006BEC57  E8 EE FF FF FF                  call 0x1406bec4a
006BEC5C  48 83 C4 08                     add rsp, 8
006BEC60  E8 EE FF FF FF                  call 0x1406bec53
006BEC65  48 83 C4 08                     add rsp, 8
006BEC69  E8 EE FF FF FF                  call 0x1406bec5c
006BEC6E  48 83 C4 08                     add rsp, 8
006BEC72  E8 EE FF FF FF                  call 0x1406bec65
006BEC77  48 83 C4 08                     add rsp, 8
006BEC7B  E8 EE FF FF FF                  call 0x1406bec6e
006BEC80  48 83 C4 08                     add rsp, 8
006BEC84  E8 EE FF FF FF                  call 0x1406bec77
006BEC89  48 83 C4 08                     add rsp, 8
006BEC8D  E8 EE FF FF FF                  call 0x1406bec80
006BEC92  48 83 C4 08                     add rsp, 8
006BEC96  E8 EE FF FF FF                  call 0x1406bec89
006BEC9B  48 83 C4 08                     add rsp, 8
006BEC9F  E8 EE FF FF FF                  call 0x1406bec92
006BECA4  48 83 C4 08                     add rsp, 8
006BECA8  E8 EE FF FF FF                  call 0x1406bec9b
006BECAD  48 83 C4 08                     add rsp, 8
006BECB1  E8 EE FF FF FF                  call 0x1406beca4
006BECB6  48 83 C4 08                     add rsp, 8
006BECBA  E8 EE FF FF FF                  call 0x1406becad
006BECBF  48 83 C4 08                     add rsp, 8
006BECC3  E8 EE FF FF FF                  call 0x1406becb6
006BECC8  48 83 C4 08                     add rsp, 8
006BECCC  E8 EE FF FF FF                  call 0x1406becbf
006BECD1  48 83 C4 08                     add rsp, 8
006BECD5  E8 EE FF FF FF                  call 0x1406becc8
006BECDA  48 83 C4 08                     add rsp, 8
006BECDE  E8 EE FF FF FF                  call 0x1406becd1
006BECE3  48 83 C4 08                     add rsp, 8
006BECE7  E8 EE FF FF FF                  call 0x1406becda
006BECEC  48 83 C4 08                     add rsp, 8
006BECF0  E8 EE FF FF FF                  call 0x1406bece3
006BECF5  48 83 C4 08                     add rsp, 8
006BECF9  B8 DA DA 00 00                  mov eax, 0xdada
006BECFE  65 F6 04 25 5C 08 00 00 08      test byte ptr gs:[0x85c], 8
006BED07  74 07                           je 0x1406bed10
006BED09  B0 20                           mov al, 0x20
006BED0B  F3 48 0F AE E8                  incsspq rax
006BED10  66 65 F7 04 25 58 08 00 00 00 01  test word ptr gs:[0x858], 0x100
006BED1B  74 0C                           je 0x1406bed29
006BED1D  33 C0                           xor eax, eax
006BED1F  33 D2                           xor edx, edx
006BED21  B9 01 00 00 00                  mov ecx, 1
006BED26  48 F7 F1                        div rcx
006BED29  0F 28 45 F0                     movaps xmm0, xmmword ptr [rbp - 0x10]
006BED2D  0F 28 4D 00                     movaps xmm1, xmmword ptr [rbp]
006BED31  0F 28 55 10                     movaps xmm2, xmmword ptr [rbp + 0x10]
006BED35  0F 28 5D 20                     movaps xmm3, xmmword ptr [rbp + 0x20]
006BED39  0F 28 65 30                     movaps xmm4, xmmword ptr [rbp + 0x30]
006BED3D  0F 28 6D 40                     movaps xmm5, xmmword ptr [rbp + 0x40]
006BED41  4C 8B 5D E0                     mov r11, qword ptr [rbp - 0x20]
006BED45  4C 8B 55 D8                     mov r10, qword ptr [rbp - 0x28]
006BED49  4C 8B 4D D0                     mov r9, qword ptr [rbp - 0x30]
006BED4D  4C 8B 45 C8                     mov r8, qword ptr [rbp - 0x38]
006BED51  48 8B 55 C0                     mov rdx, qword ptr [rbp - 0x40]
006BED55  48 8B 4D B8                     mov rcx, qword ptr [rbp - 0x48]
006BED59  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
006BED5D  48 8B E5                        mov rsp, rbp
006BED60  48 8B AD D8 00 00 00            mov rbp, qword ptr [rbp + 0xd8]
006BED67  48 81 C4 E8 00 00 00            add rsp, 0xe8
006BED6E  F6 05 CB 2A B4 00 01            test byte ptr [rip + 0xb42acb], 1
006BED75  74 05                           je 0x1406bed7c
006BED77  E9 04 DE 50 00                  jmp 0x140bccb80
006BED7C  66 65 F7 04 25 58 08 00 00 00 02  test word ptr gs:[0x858], 0x200
006BED87  74 05                           je 0x1406bed8e
006BED89  0F 00 6C 24 20                  verw word ptr [rsp + 0x20]
006BED8E  0F 01 F8                        swapgs
006BED91  48 CF                           iretq
006BED93  0F AE 55 AC                     ldmxcsr dword ptr [rbp - 0x54]
006BED97  0F 28 45 F0                     movaps xmm0, xmmword ptr [rbp - 0x10]
006BED9B  0F 28 4D 00                     movaps xmm1, xmmword ptr [rbp]
006BED9F  0F 28 55 10                     movaps xmm2, xmmword ptr [rbp + 0x10]
006BEDA3  0F 28 5D 20                     movaps xmm3, xmmword ptr [rbp + 0x20]
006BEDA7  0F 28 65 30                     movaps xmm4, xmmword ptr [rbp + 0x30]
006BEDAB  0F 28 6D 40                     movaps xmm5, xmmword ptr [rbp + 0x40]
006BEDAF  4C 8B 5D E0                     mov r11, qword ptr [rbp - 0x20]
006BEDB3  4C 8B 55 D8                     mov r10, qword ptr [rbp - 0x28]
006BEDB7  4C 8B 4D D0                     mov r9, qword ptr [rbp - 0x30]
006BEDBB  4C 8B 45 C8                     mov r8, qword ptr [rbp - 0x38]
006BEDBF  48 8B 55 C0                     mov rdx, qword ptr [rbp - 0x40]
006BEDC3  48 8B 4D B8                     mov rcx, qword ptr [rbp - 0x48]
006BEDC7  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
006BEDCB  48 8B E5                        mov rsp, rbp
006BEDCE  48 8B AD D8 00 00 00            mov rbp, qword ptr [rbp + 0xd8]
006BEDD5  48 81 C4 E8 00 00 00            add rsp, 0xe8
006BEDDC  48 CF                           iretq
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiInvalidOpcodeFault(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
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
    if (((v_stack_p8) & (1)) != 0) goto loc_006BE7B5;
    a2 = 0;
    v_stack_m90 = 0;
    if (((*(unsigned __int8 *)(gs_base + (0 + 2136))) & (1)) != 0) goto loc_006BE79E;
    goto loc_006BEA26;
loc_006BE79E:
    a2 = 0;
    goto loc_006BEA26;
loc_006BE7B5:
    if (((*(unsigned __int8 *)(v_rip + 11808900)) & (1)) == 0) {
    }
    if (*(unsigned __int64 *)(gs_base + (0 + 40232)) == 0) goto loc_006BE7F1;
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
    if ((((unsigned int)(a2)) & (2)) == 0) goto loc_006BE9CD;
    result = KiInvalidOpcodeFault___0x269(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiInvalidOpcodeFault___0x272(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiInvalidOpcodeFault___0x15B(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiInvalidOpcodeFault___0x164(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiInvalidOpcodeFault___0x16D(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiInvalidOpcodeFault___0x176(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiInvalidOpcodeFault___0x17F(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiInvalidOpcodeFault___0x188(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiInvalidOpcodeFault___0x191(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiInvalidOpcodeFault___0x19A(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiInvalidOpcodeFault___0x1A3(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiInvalidOpcodeFault___0x1AC(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiInvalidOpcodeFault___0x1B5(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiInvalidOpcodeFault___0x1BE(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiInvalidOpcodeFault___0x1C7(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiInvalidOpcodeFault___0x1D0(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiInvalidOpcodeFault___0x1D9(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiInvalidOpcodeFault___0x1E2(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiInvalidOpcodeFault___0x1EB(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiInvalidOpcodeFault___0x1F4(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiInvalidOpcodeFault___0x1FD(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiInvalidOpcodeFault___0x206(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiInvalidOpcodeFault___0x20F(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiInvalidOpcodeFault___0x218(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiInvalidOpcodeFault___0x221(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiInvalidOpcodeFault___0x22A(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiInvalidOpcodeFault___0x233(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiInvalidOpcodeFault___0x23C(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiInvalidOpcodeFault___0x245(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiInvalidOpcodeFault___0x24E(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiInvalidOpcodeFault___0x257(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiInvalidOpcodeFault___0x260(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = (unsigned int)(0xDADAULL);
    if (((*(unsigned __int8 *)(gs_base + (0 + 2140))) & (8)) != 0) {
        result = 32;
    }
    if ((((unsigned int)(a2)) & (128)) != 0) {
        result = KiFlushBhbDuringTrapEntryOrExit(a1, a2, a3, a4);
    }
    *(unsigned __int8 *)(gs_base + (0 + 2142)) = 0;
    if ((*(unsigned int *)(v_rip + 9472116)) == 0) goto loc_006BEA11;
    if (((unsigned int)(a2)) == 0) goto loc_006BEA11;
    a2 = (unsigned int)((a2) & (*(unsigned int *)(v_rip + 9472094)));
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
    if (((*(unsigned __int8 *)(v_rip + 9470351)) & (255)) == 0) goto loc_006BEA6F;
    if (((v_stack_p8) & (1)) != 0) {
    }
    if (((v_stack_p10) & (512)) != 0) {
    }
    a2 = 0;
    result = KiExceptionDispatch((unsigned int)(0x10000002ULL), a2, v_stack_p0, a4);
    if (((v_stack_p8) & (1)) == 0) goto loc_006BED93;
    if (((*(unsigned __int8 *)(v_rip + 9470283)) & (255)) != 0) {
    }
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 194)) & (3)) == 0) goto loc_006BEAD7;
    result = KiInitiateUserApc(1, a2, v_stack_p0, a4);
    goto loc_006BEAAA;
loc_006BEAD7:
    result = KiSynchronizeUserIsolationDomainEntry(0, a2, v_stack_p0, a4);
    if ((unsigned int)(result) != 0) goto loc_006BEAAA;
    result = v_stack_m138;
    if (((*(unsigned __int8 *)(gs_base + (0 + 2144))) & (2)) != 0) {
        a1 = 0;
        result = KiUpdateStibpPairing(a1, a2, v_stack_p0, a4);
    }
    if (((*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)))) & (0x8000000ULL)) != 0) {
        result = KiRestoreSetContextState(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, v_stack_p0, a4);
    }
    if (((*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)))) & (0x10000ULL)) == 0) goto loc_006BEB31;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 2)) & (1)) != 0) {
        result = KiCopyCounters(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, v_stack_p0, a4);
        a1 = *(unsigned __int64 *)(gs_base + (0 + 392));
    }
    if (v_stack_m68 != 0) {
        result = KiRestoreDebugRegisterState(a1, a2, v_stack_p0, a4);
    }
    if (v_stack_m68 >= 0) goto loc_006BEB7E;
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
    if (condition_is_above_or_equal) goto loc_006BED10;
    result = KiInvalidOpcodeFault___0x5AC(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiInvalidOpcodeFault___0x5B5(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiInvalidOpcodeFault___0x49E(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiInvalidOpcodeFault___0x4A7(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiInvalidOpcodeFault___0x4B0(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiInvalidOpcodeFault___0x4B9(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiInvalidOpcodeFault___0x4C2(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiInvalidOpcodeFault___0x4CB(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiInvalidOpcodeFault___0x4D4(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiInvalidOpcodeFault___0x4DD(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiInvalidOpcodeFault___0x4E6(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiInvalidOpcodeFault___0x4EF(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiInvalidOpcodeFault___0x4F8(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiInvalidOpcodeFault___0x501(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiInvalidOpcodeFault___0x50A(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiInvalidOpcodeFault___0x513(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiInvalidOpcodeFault___0x51C(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiInvalidOpcodeFault___0x525(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiInvalidOpcodeFault___0x52E(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiInvalidOpcodeFault___0x537(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiInvalidOpcodeFault___0x540(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiInvalidOpcodeFault___0x549(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiInvalidOpcodeFault___0x552(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiInvalidOpcodeFault___0x55B(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiInvalidOpcodeFault___0x564(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiInvalidOpcodeFault___0x56D(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiInvalidOpcodeFault___0x576(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiInvalidOpcodeFault___0x57F(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiInvalidOpcodeFault___0x588(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiInvalidOpcodeFault___0x591(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiInvalidOpcodeFault___0x59A(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiInvalidOpcodeFault___0x5A3(a1, a2, a3, a4);
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
    if (((*(unsigned __int8 *)(v_rip + 11807435)) & (1)) == 0) goto loc_006BED7C;
loc_006BED7C:
    if (((*(unsigned __int16 *)(gs_base + (0 + 2136))) & (512)) != 0) {
    }
loc_006BED93:
    v_rsp = (v_stack_m10) + (232);
    return v_stack_m138;
}
```

## 5. (Beta) C Style

```c
int64_t KiInvalidOpcodeFault(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
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
    if (((v_stack_p8) & (1)) != 0) goto loc_006BE7B5;
    Arg2 = 0;
    v_stack_m90 = 0;
    if (((*(uint8_t *)(gs_base + (0 + 0x858))) & (1)) != 0) goto loc_006BE79E;
    goto loc_006BEA26;
loc_006BE79E:
    Arg2 = 0;
    goto loc_006BEA26;
loc_006BE7B5:
    if (((*(uint8_t *)(v_rip + 0xB43084)) & (1)) == 0) {
    }
    if (*(uint64_t *)(gs_base + (0 + 0x9D28)) == 0) goto loc_006BE7F1;
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
    if ((((uint32_t)(Arg2)) & (2)) == 0) goto loc_006BE9CD;
    result = KiInvalidOpcodeFault___0x269(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiInvalidOpcodeFault___0x272(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiInvalidOpcodeFault___0x15B(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiInvalidOpcodeFault___0x164(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiInvalidOpcodeFault___0x16D(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiInvalidOpcodeFault___0x176(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiInvalidOpcodeFault___0x17F(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiInvalidOpcodeFault___0x188(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiInvalidOpcodeFault___0x191(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiInvalidOpcodeFault___0x19A(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiInvalidOpcodeFault___0x1A3(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiInvalidOpcodeFault___0x1AC(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiInvalidOpcodeFault___0x1B5(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiInvalidOpcodeFault___0x1BE(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiInvalidOpcodeFault___0x1C7(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiInvalidOpcodeFault___0x1D0(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiInvalidOpcodeFault___0x1D9(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiInvalidOpcodeFault___0x1E2(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiInvalidOpcodeFault___0x1EB(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiInvalidOpcodeFault___0x1F4(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiInvalidOpcodeFault___0x1FD(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiInvalidOpcodeFault___0x206(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiInvalidOpcodeFault___0x20F(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiInvalidOpcodeFault___0x218(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiInvalidOpcodeFault___0x221(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiInvalidOpcodeFault___0x22A(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiInvalidOpcodeFault___0x233(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiInvalidOpcodeFault___0x23C(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiInvalidOpcodeFault___0x245(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiInvalidOpcodeFault___0x24E(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiInvalidOpcodeFault___0x257(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiInvalidOpcodeFault___0x260(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = (uint32_t)(0xDADAULL);
    if (((*(uint8_t *)(gs_base + (0 + 0x85C))) & (8)) != 0) {
        result = 32;
    }
    if ((((uint32_t)(Arg2)) & (128)) != 0) {
        result = KiFlushBhbDuringTrapEntryOrExit(Arg1, Arg2, Arg3, Arg4);
    }
    *(uint8_t *)(gs_base + (0 + 0x85E)) = 0;
    if ((*(uint32_t *)(v_rip + 0x908874)) == 0) goto loc_006BEA11;
    if (((uint32_t)(Arg2)) == 0) goto loc_006BEA11;
    Arg2 = (uint32_t)((Arg2) & (*(uint32_t *)(v_rip + 0x90885E)));
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
    if (((*(uint8_t *)(v_rip + 0x90818F)) & (255)) == 0) goto loc_006BEA6F;
    if (((v_stack_p8) & (1)) != 0) {
    }
    if (((v_stack_p10) & (512)) != 0) {
    }
    Arg2 = 0;
    result = KiExceptionDispatch((uint32_t)(0x10000002ULL), Arg2, v_stack_p0, Arg4);
    if (((v_stack_p8) & (1)) == 0) goto loc_006BED93;
    if (((*(uint8_t *)(v_rip + 0x90814B)) & (255)) != 0) {
    }
    if (((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xC2)) & (3)) == 0) goto loc_006BEAD7;
    result = KiInitiateUserApc(1, Arg2, v_stack_p0, Arg4);
    goto loc_006BEAAA;
loc_006BEAD7:
    result = KiSynchronizeUserIsolationDomainEntry(0, Arg2, v_stack_p0, Arg4);
    if ((uint32_t)(result) != 0) goto loc_006BEAAA;
    result = v_stack_m138;
    if (((*(uint8_t *)(gs_base + (0 + 0x860))) & (2)) != 0) {
        Arg1 = 0;
        result = KiUpdateStibpPairing(Arg1, Arg2, v_stack_p0, Arg4);
    }
    if (((*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)))) & (0x8000000ULL)) != 0) {
        result = KiRestoreSetContextState(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, v_stack_p0, Arg4);
    }
    if (((*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)))) & (0x10000ULL)) == 0) goto loc_006BEB31;
    if (((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x2)) & (1)) != 0) {
        result = KiCopyCounters(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, v_stack_p0, Arg4);
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x188));
    }
    if (v_stack_m68 != 0) {
        result = KiRestoreDebugRegisterState(Arg1, Arg2, v_stack_p0, Arg4);
    }
    if (v_stack_m68 >= 0) goto loc_006BEB7E;
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
    if (condition_is_above_or_equal) goto loc_006BED10;
    result = KiInvalidOpcodeFault___0x5AC(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiInvalidOpcodeFault___0x5B5(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiInvalidOpcodeFault___0x49E(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiInvalidOpcodeFault___0x4A7(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiInvalidOpcodeFault___0x4B0(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiInvalidOpcodeFault___0x4B9(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiInvalidOpcodeFault___0x4C2(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiInvalidOpcodeFault___0x4CB(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiInvalidOpcodeFault___0x4D4(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiInvalidOpcodeFault___0x4DD(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiInvalidOpcodeFault___0x4E6(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiInvalidOpcodeFault___0x4EF(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiInvalidOpcodeFault___0x4F8(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiInvalidOpcodeFault___0x501(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiInvalidOpcodeFault___0x50A(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiInvalidOpcodeFault___0x513(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiInvalidOpcodeFault___0x51C(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiInvalidOpcodeFault___0x525(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiInvalidOpcodeFault___0x52E(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiInvalidOpcodeFault___0x537(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiInvalidOpcodeFault___0x540(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiInvalidOpcodeFault___0x549(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiInvalidOpcodeFault___0x552(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiInvalidOpcodeFault___0x55B(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiInvalidOpcodeFault___0x564(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiInvalidOpcodeFault___0x56D(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiInvalidOpcodeFault___0x576(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiInvalidOpcodeFault___0x57F(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiInvalidOpcodeFault___0x588(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiInvalidOpcodeFault___0x591(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiInvalidOpcodeFault___0x59A(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiInvalidOpcodeFault___0x5A3(Arg1, Arg2, Arg3, Arg4);
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
    if (((*(uint8_t *)(v_rip + 0xB42ACB)) & (1)) == 0) goto loc_006BED7C;
loc_006BED7C:
    if (((*(uint16_t *)(gs_base + (0 + 0x858))) & (512)) != 0) {
    }
loc_006BED93:
    local_rsp = (v_stack_m10) + (232);
    return v_stack_m138;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006BE740&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
