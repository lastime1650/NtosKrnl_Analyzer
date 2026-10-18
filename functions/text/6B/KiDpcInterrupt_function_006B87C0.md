# KiDpcInterrupt

- RVA: `0x006B87C0`–`0x006B8ECD` (길이 `1,805` bytes)
- VA: `0x00000001406B87C0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C22A8`
- 디코드: `395`개 명령, `1,805/1,805` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **77**; 고유 호출 대상: **76**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x006B8917` → [KiDpcInterrupt + 0x26A](KiDpcInterrupt_function_006B87C0.md) (inside-function, `0x006B8A2A`)
- `0x006B8920` → [KiDpcInterrupt + 0x273](KiDpcInterrupt_function_006B87C0.md) (inside-function, `0x006B8A33`)
- `0x006B8929` → [KiDpcInterrupt + 0x15C](KiDpcInterrupt_function_006B87C0.md) (inside-function, `0x006B891C`)
- `0x006B8932` → [KiDpcInterrupt + 0x165](KiDpcInterrupt_function_006B87C0.md) (inside-function, `0x006B8925`)
- `0x006B893B` → [KiDpcInterrupt + 0x16E](KiDpcInterrupt_function_006B87C0.md) (inside-function, `0x006B892E`)
- `0x006B8944` → [KiDpcInterrupt + 0x177](KiDpcInterrupt_function_006B87C0.md) (inside-function, `0x006B8937`)
- `0x006B894D` → [KiDpcInterrupt + 0x180](KiDpcInterrupt_function_006B87C0.md) (inside-function, `0x006B8940`)
- `0x006B8956` → [KiDpcInterrupt + 0x189](KiDpcInterrupt_function_006B87C0.md) (inside-function, `0x006B8949`)
- `0x006B895F` → [KiDpcInterrupt + 0x192](KiDpcInterrupt_function_006B87C0.md) (inside-function, `0x006B8952`)
- `0x006B8968` → [KiDpcInterrupt + 0x19B](KiDpcInterrupt_function_006B87C0.md) (inside-function, `0x006B895B`)
- `0x006B8971` → [KiDpcInterrupt + 0x1A4](KiDpcInterrupt_function_006B87C0.md) (inside-function, `0x006B8964`)
- `0x006B897A` → [KiDpcInterrupt + 0x1AD](KiDpcInterrupt_function_006B87C0.md) (inside-function, `0x006B896D`)
- `0x006B8983` → [KiDpcInterrupt + 0x1B6](KiDpcInterrupt_function_006B87C0.md) (inside-function, `0x006B8976`)
- `0x006B898C` → [KiDpcInterrupt + 0x1BF](KiDpcInterrupt_function_006B87C0.md) (inside-function, `0x006B897F`)
- `0x006B8995` → [KiDpcInterrupt + 0x1C8](KiDpcInterrupt_function_006B87C0.md) (inside-function, `0x006B8988`)
- `0x006B899E` → [KiDpcInterrupt + 0x1D1](KiDpcInterrupt_function_006B87C0.md) (inside-function, `0x006B8991`)
- `0x006B89A7` → [KiDpcInterrupt + 0x1DA](KiDpcInterrupt_function_006B87C0.md) (inside-function, `0x006B899A`)
- `0x006B89B0` → [KiDpcInterrupt + 0x1E3](KiDpcInterrupt_function_006B87C0.md) (inside-function, `0x006B89A3`)
- `0x006B89B9` → [KiDpcInterrupt + 0x1EC](KiDpcInterrupt_function_006B87C0.md) (inside-function, `0x006B89AC`)
- `0x006B89C2` → [KiDpcInterrupt + 0x1F5](KiDpcInterrupt_function_006B87C0.md) (inside-function, `0x006B89B5`)
- `0x006B89CB` → [KiDpcInterrupt + 0x1FE](KiDpcInterrupt_function_006B87C0.md) (inside-function, `0x006B89BE`)
- `0x006B89D4` → [KiDpcInterrupt + 0x207](KiDpcInterrupt_function_006B87C0.md) (inside-function, `0x006B89C7`)
- `0x006B89DD` → [KiDpcInterrupt + 0x210](KiDpcInterrupt_function_006B87C0.md) (inside-function, `0x006B89D0`)
- `0x006B89E6` → [KiDpcInterrupt + 0x219](KiDpcInterrupt_function_006B87C0.md) (inside-function, `0x006B89D9`)
- `0x006B89EF` → [KiDpcInterrupt + 0x222](KiDpcInterrupt_function_006B87C0.md) (inside-function, `0x006B89E2`)
- `0x006B89F8` → [KiDpcInterrupt + 0x22B](KiDpcInterrupt_function_006B87C0.md) (inside-function, `0x006B89EB`)
- `0x006B8A01` → [KiDpcInterrupt + 0x234](KiDpcInterrupt_function_006B87C0.md) (inside-function, `0x006B89F4`)
- `0x006B8A0A` → [KiDpcInterrupt + 0x23D](KiDpcInterrupt_function_006B87C0.md) (inside-function, `0x006B89FD`)
- `0x006B8A13` → [KiDpcInterrupt + 0x246](KiDpcInterrupt_function_006B87C0.md) (inside-function, `0x006B8A06`)
- `0x006B8A1C` → [KiDpcInterrupt + 0x24F](KiDpcInterrupt_function_006B87C0.md) (inside-function, `0x006B8A0F`)
- `0x006B8A25` → [KiDpcInterrupt + 0x258](KiDpcInterrupt_function_006B87C0.md) (inside-function, `0x006B8A18`)
- `0x006B8A2E` → [KiDpcInterrupt + 0x261](KiDpcInterrupt_function_006B87C0.md) (inside-function, `0x006B8A21`)
- `0x006B8A59` → [KiFlushBhbDuringTrapEntryOrExit](../6C/KiFlushBhbDuringTrapEntryOrExit_function_006C6340.md) (function, `0x006C6340`)
- `0x006B8AA2` → [KiSaveDebugRegisterState](../4F/KiSaveDebugRegisterState_function_004FD960.md) (function, `0x004FD960`)
- `0x006B8AD6` → [KiSynchronizeUserIsolationDomainExit](../41/KiSynchronizeUserIsolationDomainExit_function_0041BFA0.md) (function, `0x0041BFA0`)
- `0x006B8B2C` → [KzSetIrqlUnsafe](../5B/KzSetIrqlUnsafe_function_005B8AE0.md) (function, `0x005B8AE0`)
- `0x006B8B41` → [HalPerformEndOfInterrupt](../41/HalPerformEndOfInterrupt_function_00418E20.md) (function, `0x00418E20`)
- `0x006B8B5A` → [KiDispatchInterrupt](../21/KiDispatchInterrupt_function_0021B7F0.md) (function, `0x0021B7F0`)
- `0x006B8B6D` → [KzSetIrqlUnsafe](../5B/KzSetIrqlUnsafe_function_005B8AE0.md) (function, `0x005B8AE0`)
- `0x006B8BB5` → [KiInitiateUserApc](KiInitiateUserApc_function_006B6540.md) (function, `0x006B6540`)
- `0x006B8BC6` → [KiSynchronizeUserIsolationDomainEntry](../26/KiSynchronizeUserIsolationDomainEntry_function_00263F60.md) (function, `0x00263F60`)
- `0x006B8BE0` → [KiUpdateStibpPairing](../3E/KiUpdateStibpPairing_function_003E71C0.md) (function, `0x003E71C0`)
- `0x006B8BF6` → [KiRestoreSetContextState](KiRestoreSetContextState_function_006B1CA0.md) (function, `0x006B1CA0`)
- `0x006B8C12` → [KiCopyCounters](../5C/KiCopyCounters_function_005C0710.md) (function, `0x005C0710`)
- `0x006B8C2E` → [KiRestoreDebugRegisterState](../4F/KiRestoreDebugRegisterState_function_004FD8E0.md) (function, `0x004FD8E0`)
- `0x006B8CC8` → [KiDpcInterrupt + 0x61B](KiDpcInterrupt_function_006B87C0.md) (inside-function, `0x006B8DDB`)
- `0x006B8CD1` → [KiDpcInterrupt + 0x624](KiDpcInterrupt_function_006B87C0.md) (inside-function, `0x006B8DE4`)
- `0x006B8CDA` → [KiDpcInterrupt + 0x50D](KiDpcInterrupt_function_006B87C0.md) (inside-function, `0x006B8CCD`)
- `0x006B8CE3` → [KiDpcInterrupt + 0x516](KiDpcInterrupt_function_006B87C0.md) (inside-function, `0x006B8CD6`)
- `0x006B8CEC` → [KiDpcInterrupt + 0x51F](KiDpcInterrupt_function_006B87C0.md) (inside-function, `0x006B8CDF`)
- `0x006B8CF5` → [KiDpcInterrupt + 0x528](KiDpcInterrupt_function_006B87C0.md) (inside-function, `0x006B8CE8`)
- `0x006B8CFE` → [KiDpcInterrupt + 0x531](KiDpcInterrupt_function_006B87C0.md) (inside-function, `0x006B8CF1`)
- `0x006B8D07` → [KiDpcInterrupt + 0x53A](KiDpcInterrupt_function_006B87C0.md) (inside-function, `0x006B8CFA`)
- `0x006B8D10` → [KiDpcInterrupt + 0x543](KiDpcInterrupt_function_006B87C0.md) (inside-function, `0x006B8D03`)
- `0x006B8D19` → [KiDpcInterrupt + 0x54C](KiDpcInterrupt_function_006B87C0.md) (inside-function, `0x006B8D0C`)
- `0x006B8D22` → [KiDpcInterrupt + 0x555](KiDpcInterrupt_function_006B87C0.md) (inside-function, `0x006B8D15`)
- `0x006B8D2B` → [KiDpcInterrupt + 0x55E](KiDpcInterrupt_function_006B87C0.md) (inside-function, `0x006B8D1E`)
- `0x006B8D34` → [KiDpcInterrupt + 0x567](KiDpcInterrupt_function_006B87C0.md) (inside-function, `0x006B8D27`)
- `0x006B8D3D` → [KiDpcInterrupt + 0x570](KiDpcInterrupt_function_006B87C0.md) (inside-function, `0x006B8D30`)
- `0x006B8D46` → [KiDpcInterrupt + 0x579](KiDpcInterrupt_function_006B87C0.md) (inside-function, `0x006B8D39`)
- `0x006B8D4F` → [KiDpcInterrupt + 0x582](KiDpcInterrupt_function_006B87C0.md) (inside-function, `0x006B8D42`)
- `0x006B8D58` → [KiDpcInterrupt + 0x58B](KiDpcInterrupt_function_006B87C0.md) (inside-function, `0x006B8D4B`)
- `0x006B8D61` → [KiDpcInterrupt + 0x594](KiDpcInterrupt_function_006B87C0.md) (inside-function, `0x006B8D54`)
- `0x006B8D6A` → [KiDpcInterrupt + 0x59D](KiDpcInterrupt_function_006B87C0.md) (inside-function, `0x006B8D5D`)
- `0x006B8D73` → [KiDpcInterrupt + 0x5A6](KiDpcInterrupt_function_006B87C0.md) (inside-function, `0x006B8D66`)
- `0x006B8D7C` → [KiDpcInterrupt + 0x5AF](KiDpcInterrupt_function_006B87C0.md) (inside-function, `0x006B8D6F`)
- `0x006B8D85` → [KiDpcInterrupt + 0x5B8](KiDpcInterrupt_function_006B87C0.md) (inside-function, `0x006B8D78`)
- `0x006B8D8E` → [KiDpcInterrupt + 0x5C1](KiDpcInterrupt_function_006B87C0.md) (inside-function, `0x006B8D81`)
- `0x006B8D97` → [KiDpcInterrupt + 0x5CA](KiDpcInterrupt_function_006B87C0.md) (inside-function, `0x006B8D8A`)
- `0x006B8DA0` → [KiDpcInterrupt + 0x5D3](KiDpcInterrupt_function_006B87C0.md) (inside-function, `0x006B8D93`)
- `0x006B8DA9` → [KiDpcInterrupt + 0x5DC](KiDpcInterrupt_function_006B87C0.md) (inside-function, `0x006B8D9C`)
- `0x006B8DB2` → [KiDpcInterrupt + 0x5E5](KiDpcInterrupt_function_006B87C0.md) (inside-function, `0x006B8DA5`)
- `0x006B8DBB` → [KiDpcInterrupt + 0x5EE](KiDpcInterrupt_function_006B87C0.md) (inside-function, `0x006B8DAE`)
- `0x006B8DC4` → [KiDpcInterrupt + 0x5F7](KiDpcInterrupt_function_006B87C0.md) (inside-function, `0x006B8DB7`)
- `0x006B8DCD` → [KiDpcInterrupt + 0x600](KiDpcInterrupt_function_006B87C0.md) (inside-function, `0x006B8DC0`)
- `0x006B8DD6` → [KiDpcInterrupt + 0x609](KiDpcInterrupt_function_006B87C0.md) (inside-function, `0x006B8DC9`)
- `0x006B8DDF` → [KiDpcInterrupt + 0x612](KiDpcInterrupt_function_006B87C0.md) (inside-function, `0x006B8DD2`)

### Direct callers
- [KiDpcInterrupt](KiDpcInterrupt_function_006B87C0.md) at `0x006B8917`
- [KiDpcInterrupt](KiDpcInterrupt_function_006B87C0.md) at `0x006B8920`
- [KiDpcInterrupt](KiDpcInterrupt_function_006B87C0.md) at `0x006B8929`
- [KiDpcInterrupt](KiDpcInterrupt_function_006B87C0.md) at `0x006B8932`
- [KiDpcInterrupt](KiDpcInterrupt_function_006B87C0.md) at `0x006B893B`
- [KiDpcInterrupt](KiDpcInterrupt_function_006B87C0.md) at `0x006B8944`
- [KiDpcInterrupt](KiDpcInterrupt_function_006B87C0.md) at `0x006B894D`
- [KiDpcInterrupt](KiDpcInterrupt_function_006B87C0.md) at `0x006B8956`
- [KiDpcInterrupt](KiDpcInterrupt_function_006B87C0.md) at `0x006B895F`
- [KiDpcInterrupt](KiDpcInterrupt_function_006B87C0.md) at `0x006B8968`
- [KiDpcInterrupt](KiDpcInterrupt_function_006B87C0.md) at `0x006B8971`
- [KiDpcInterrupt](KiDpcInterrupt_function_006B87C0.md) at `0x006B897A`
- [KiDpcInterrupt](KiDpcInterrupt_function_006B87C0.md) at `0x006B8983`
- [KiDpcInterrupt](KiDpcInterrupt_function_006B87C0.md) at `0x006B898C`
- [KiDpcInterrupt](KiDpcInterrupt_function_006B87C0.md) at `0x006B8995`
- [KiDpcInterrupt](KiDpcInterrupt_function_006B87C0.md) at `0x006B899E`
- [KiDpcInterrupt](KiDpcInterrupt_function_006B87C0.md) at `0x006B89A7`
- [KiDpcInterrupt](KiDpcInterrupt_function_006B87C0.md) at `0x006B89B0`
- [KiDpcInterrupt](KiDpcInterrupt_function_006B87C0.md) at `0x006B89B9`
- [KiDpcInterrupt](KiDpcInterrupt_function_006B87C0.md) at `0x006B89C2`
- [KiDpcInterrupt](KiDpcInterrupt_function_006B87C0.md) at `0x006B89CB`
- [KiDpcInterrupt](KiDpcInterrupt_function_006B87C0.md) at `0x006B89D4`
- [KiDpcInterrupt](KiDpcInterrupt_function_006B87C0.md) at `0x006B89DD`
- [KiDpcInterrupt](KiDpcInterrupt_function_006B87C0.md) at `0x006B89E6`
- [KiDpcInterrupt](KiDpcInterrupt_function_006B87C0.md) at `0x006B89EF`
- [KiDpcInterrupt](KiDpcInterrupt_function_006B87C0.md) at `0x006B89F8`
- [KiDpcInterrupt](KiDpcInterrupt_function_006B87C0.md) at `0x006B8A01`
- [KiDpcInterrupt](KiDpcInterrupt_function_006B87C0.md) at `0x006B8A0A`
- [KiDpcInterrupt](KiDpcInterrupt_function_006B87C0.md) at `0x006B8A13`
- [KiDpcInterrupt](KiDpcInterrupt_function_006B87C0.md) at `0x006B8A1C`
- [KiDpcInterrupt](KiDpcInterrupt_function_006B87C0.md) at `0x006B8A25`
- [KiDpcInterrupt](KiDpcInterrupt_function_006B87C0.md) at `0x006B8A2E`
- [KiDpcInterrupt](KiDpcInterrupt_function_006B87C0.md) at `0x006B8CC8`
- [KiDpcInterrupt](KiDpcInterrupt_function_006B87C0.md) at `0x006B8CD1`
- [KiDpcInterrupt](KiDpcInterrupt_function_006B87C0.md) at `0x006B8CDA`
- [KiDpcInterrupt](KiDpcInterrupt_function_006B87C0.md) at `0x006B8CE3`
- [KiDpcInterrupt](KiDpcInterrupt_function_006B87C0.md) at `0x006B8CEC`
- [KiDpcInterrupt](KiDpcInterrupt_function_006B87C0.md) at `0x006B8CF5`
- [KiDpcInterrupt](KiDpcInterrupt_function_006B87C0.md) at `0x006B8CFE`
- [KiDpcInterrupt](KiDpcInterrupt_function_006B87C0.md) at `0x006B8D07`
- [KiDpcInterrupt](KiDpcInterrupt_function_006B87C0.md) at `0x006B8D10`
- [KiDpcInterrupt](KiDpcInterrupt_function_006B87C0.md) at `0x006B8D19`
- [KiDpcInterrupt](KiDpcInterrupt_function_006B87C0.md) at `0x006B8D22`
- [KiDpcInterrupt](KiDpcInterrupt_function_006B87C0.md) at `0x006B8D2B`
- [KiDpcInterrupt](KiDpcInterrupt_function_006B87C0.md) at `0x006B8D34`
- [KiDpcInterrupt](KiDpcInterrupt_function_006B87C0.md) at `0x006B8D3D`
- [KiDpcInterrupt](KiDpcInterrupt_function_006B87C0.md) at `0x006B8D46`
- [KiDpcInterrupt](KiDpcInterrupt_function_006B87C0.md) at `0x006B8D4F`
- [KiDpcInterrupt](KiDpcInterrupt_function_006B87C0.md) at `0x006B8D58`
- [KiDpcInterrupt](KiDpcInterrupt_function_006B87C0.md) at `0x006B8D61`
- [KiDpcInterrupt](KiDpcInterrupt_function_006B87C0.md) at `0x006B8D6A`
- [KiDpcInterrupt](KiDpcInterrupt_function_006B87C0.md) at `0x006B8D73`
- [KiDpcInterrupt](KiDpcInterrupt_function_006B87C0.md) at `0x006B8D7C`
- [KiDpcInterrupt](KiDpcInterrupt_function_006B87C0.md) at `0x006B8D85`
- [KiDpcInterrupt](KiDpcInterrupt_function_006B87C0.md) at `0x006B8D8E`
- [KiDpcInterrupt](KiDpcInterrupt_function_006B87C0.md) at `0x006B8D97`
- [KiDpcInterrupt](KiDpcInterrupt_function_006B87C0.md) at `0x006B8DA0`
- [KiDpcInterrupt](KiDpcInterrupt_function_006B87C0.md) at `0x006B8DA9`
- [KiDpcInterrupt](KiDpcInterrupt_function_006B87C0.md) at `0x006B8DB2`
- [KiDpcInterrupt](KiDpcInterrupt_function_006B87C0.md) at `0x006B8DBB`
- [KiDpcInterrupt](KiDpcInterrupt_function_006B87C0.md) at `0x006B8DC4`
- [KiDpcInterrupt](KiDpcInterrupt_function_006B87C0.md) at `0x006B8DCD`
- [KiDpcInterrupt](KiDpcInterrupt_function_006B87C0.md) at `0x006B8DD6`
- [KiDpcInterrupt](KiDpcInterrupt_function_006B87C0.md) at `0x006B8DDF`

### Static image references
- `0x006B8836` → RVA `0x01201840` (`CFGRO`; read)
- `0x006B8A6A` → RVA `0x00FC7264` (`ALMOSTRO`; read)
- `0x006B8AE5` → RVA `0x00FC6BF0` (`ALMOSTRO`; read)
- `0x006B8AF1` → RVA `0x00FC6BC5` (`ALMOSTRO`; read)
- `0x006B8B23` → RVA `0x00FC6D20` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006B8E66` → [KiKernelExit](../../kvascode/BC/KiKernelExit_function_00BCCB80.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006B87C0  48 83 EC 08                     sub rsp, 8
006B87C4  55                              push rbp
006B87C5  56                              push rsi
006B87C6  48 81 EC 50 01 00 00            sub rsp, 0x150
006B87CD  48 8D AC 24 80 00 00 00         lea rbp, [rsp + 0x80]
006B87D5  C6 45 AB 00                     mov byte ptr [rbp - 0x55], 0
006B87D9  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
006B87DD  48 89 4D B8                     mov qword ptr [rbp - 0x48], rcx
006B87E1  48 89 55 C0                     mov qword ptr [rbp - 0x40], rdx
006B87E5  4C 89 45 C8                     mov qword ptr [rbp - 0x38], r8
006B87E9  4C 89 4D D0                     mov qword ptr [rbp - 0x30], r9
006B87ED  4C 89 55 D8                     mov qword ptr [rbp - 0x28], r10
006B87F1  4C 89 5D E0                     mov qword ptr [rbp - 0x20], r11
006B87F5  F6 85 F0 00 00 00 01            test byte ptr [rbp + 0xf0], 1
006B87FC  75 38                           jne 0x1406b8836
006B87FE  33 D2                           xor edx, edx
006B8800  F3 48 0F 1E CA                  rdsspq rdx
006B8805  48 89 55 58                     mov qword ptr [rbp + 0x58], rdx
006B8809  0F AE E8                        lfence
006B880C  65 F6 04 25 58 08 00 00 01      test byte ptr gs:[0x858], 1
006B8815  75 08                           jne 0x1406b881f
006B8817  0F AE E8                        lfence
006B881A  E9 88 02 00 00                  jmp 0x1406b8aa7
006B881F  65 0F B7 04 25 66 08 00 00      movzx eax, word ptr gs:[0x866]
006B8828  B9 48 00 00 00                  mov ecx, 0x48
006B882D  33 D2                           xor edx, edx
006B882F  0F 30                           wrmsr
006B8831  E9 71 02 00 00                  jmp 0x1406b8aa7
006B8836  F6 05 03 90 B4 00 01            test byte ptr [rip + 0xb49003], 1
006B883D  75 03                           jne 0x1406b8842
006B883F  0F 01 F8                        swapgs
006B8842  0F AE E8                        lfence
006B8845  65 48 8B 0C 25 28 9D 00 00      mov rcx, qword ptr gs:[0x9d28]
006B884E  48 85 C9                        test rcx, rcx
006B8851  74 1F                           je 0x1406b8872
006B8853  F3 48 0F 1E CA                  rdsspq rdx
006B8858  65 4C 8B 14 25 20 9D 00 00      mov r10, qword ptr gs:[0x9d20]
006B8861  49 83 C2 08                     add r10, 8
006B8865  49 3B D2                        cmp rdx, r10
006B8868  75 08                           jne 0x1406b8872
006B886A  F3 0F 01 29                     rstorssp dword ptr [rcx]
006B886E  F3 0F 01 EA                     saveprevssp
006B8872  65 4C 8B 14 25 88 01 00 00      mov r10, qword ptr gs:[0x188]
006B887B  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006B8884  48 8B 89 20 02 00 00            mov rcx, qword ptr [rcx + 0x220]
006B888B  48 8B 89 60 07 00 00            mov rcx, qword ptr [rcx + 0x760]
006B8892  65 48 89 0C 25 50 08 00 00      mov qword ptr gs:[0x850], rcx
006B889B  66 65 8B 0C 25 62 08 00 00      mov cx, word ptr gs:[0x862]
006B88A4  66 65 89 0C 25 64 08 00 00      mov word ptr gs:[0x864], cx
006B88AD  65 8A 0C 25 58 08 00 00         mov cl, byte ptr gs:[0x858]
006B88B5  65 88 0C 25 5A 08 00 00         mov byte ptr gs:[0x85a], cl
006B88BD  65 0F B7 04 25 68 08 00 00      movzx eax, word ptr gs:[0x868]
006B88C6  66 65 39 04 25 66 08 00 00      cmp word ptr gs:[0x866], ax
006B88CF  74 12                           je 0x1406b88e3
006B88D1  66 65 89 04 25 66 08 00 00      mov word ptr gs:[0x866], ax
006B88DA  B9 48 00 00 00                  mov ecx, 0x48
006B88DF  33 D2                           xor edx, edx
006B88E1  0F 30                           wrmsr
006B88E3  65 0F B6 14 25 58 08 00 00      movzx edx, byte ptr gs:[0x858]
006B88EC  F7 C2 08 00 00 00               test edx, 8
006B88F2  74 17                           je 0x1406b890b
006B88F4  B8 01 00 00 00                  mov eax, 1
006B88F9  33 D2                           xor edx, edx
006B88FB  B9 49 00 00 00                  mov ecx, 0x49
006B8900  0F 30                           wrmsr
006B8902  65 0F B6 14 25 58 08 00 00      movzx edx, byte ptr gs:[0x858]
006B890B  F7 C2 02 00 00 00               test edx, 2
006B8911  0F 84 37 01 00 00               je 0x1406b8a4e
006B8917  E8 0E 01 00 00                  call 0x1406b8a2a
006B891C  48 83 C4 08                     add rsp, 8
006B8920  E8 0E 01 00 00                  call 0x1406b8a33
006B8925  48 83 C4 08                     add rsp, 8
006B8929  E8 EE FF FF FF                  call 0x1406b891c
006B892E  48 83 C4 08                     add rsp, 8
006B8932  E8 EE FF FF FF                  call 0x1406b8925
006B8937  48 83 C4 08                     add rsp, 8
006B893B  E8 EE FF FF FF                  call 0x1406b892e
006B8940  48 83 C4 08                     add rsp, 8
006B8944  E8 EE FF FF FF                  call 0x1406b8937
006B8949  48 83 C4 08                     add rsp, 8
006B894D  E8 EE FF FF FF                  call 0x1406b8940
006B8952  48 83 C4 08                     add rsp, 8
006B8956  E8 EE FF FF FF                  call 0x1406b8949
006B895B  48 83 C4 08                     add rsp, 8
006B895F  E8 EE FF FF FF                  call 0x1406b8952
006B8964  48 83 C4 08                     add rsp, 8
006B8968  E8 EE FF FF FF                  call 0x1406b895b
006B896D  48 83 C4 08                     add rsp, 8
006B8971  E8 EE FF FF FF                  call 0x1406b8964
006B8976  48 83 C4 08                     add rsp, 8
006B897A  E8 EE FF FF FF                  call 0x1406b896d
006B897F  48 83 C4 08                     add rsp, 8
006B8983  E8 EE FF FF FF                  call 0x1406b8976
006B8988  48 83 C4 08                     add rsp, 8
006B898C  E8 EE FF FF FF                  call 0x1406b897f
006B8991  48 83 C4 08                     add rsp, 8
006B8995  E8 EE FF FF FF                  call 0x1406b8988
006B899A  48 83 C4 08                     add rsp, 8
006B899E  E8 EE FF FF FF                  call 0x1406b8991
006B89A3  48 83 C4 08                     add rsp, 8
006B89A7  E8 EE FF FF FF                  call 0x1406b899a
006B89AC  48 83 C4 08                     add rsp, 8
006B89B0  E8 EE FF FF FF                  call 0x1406b89a3
006B89B5  48 83 C4 08                     add rsp, 8
006B89B9  E8 EE FF FF FF                  call 0x1406b89ac
006B89BE  48 83 C4 08                     add rsp, 8
006B89C2  E8 EE FF FF FF                  call 0x1406b89b5
006B89C7  48 83 C4 08                     add rsp, 8
006B89CB  E8 EE FF FF FF                  call 0x1406b89be
006B89D0  48 83 C4 08                     add rsp, 8
006B89D4  E8 EE FF FF FF                  call 0x1406b89c7
006B89D9  48 83 C4 08                     add rsp, 8
006B89DD  E8 EE FF FF FF                  call 0x1406b89d0
006B89E2  48 83 C4 08                     add rsp, 8
006B89E6  E8 EE FF FF FF                  call 0x1406b89d9
006B89EB  48 83 C4 08                     add rsp, 8
006B89EF  E8 EE FF FF FF                  call 0x1406b89e2
006B89F4  48 83 C4 08                     add rsp, 8
006B89F8  E8 EE FF FF FF                  call 0x1406b89eb
006B89FD  48 83 C4 08                     add rsp, 8
006B8A01  E8 EE FF FF FF                  call 0x1406b89f4
006B8A06  48 83 C4 08                     add rsp, 8
006B8A0A  E8 EE FF FF FF                  call 0x1406b89fd
006B8A0F  48 83 C4 08                     add rsp, 8
006B8A13  E8 EE FF FF FF                  call 0x1406b8a06
006B8A18  48 83 C4 08                     add rsp, 8
006B8A1C  E8 EE FF FF FF                  call 0x1406b8a0f
006B8A21  48 83 C4 08                     add rsp, 8
006B8A25  E8 EE FF FF FF                  call 0x1406b8a18
006B8A2A  48 83 C4 08                     add rsp, 8
006B8A2E  E8 EE FF FF FF                  call 0x1406b8a21
006B8A33  48 83 C4 08                     add rsp, 8
006B8A37  B8 DA DA 00 00                  mov eax, 0xdada
006B8A3C  65 F6 04 25 5C 08 00 00 08      test byte ptr gs:[0x85c], 8
006B8A45  74 07                           je 0x1406b8a4e
006B8A47  B0 20                           mov al, 0x20
006B8A49  F3 48 0F AE E8                  incsspq rax
006B8A4E  F7 C2 80 00 00 00               test edx, 0x80
006B8A54  74 08                           je 0x1406b8a5e
006B8A56  0F AE E8                        lfence
006B8A59  E8 E2 D8 00 00                  call 0x1406c6340
006B8A5E  0F AE E8                        lfence
006B8A61  65 C6 04 25 5E 08 00 00 00      mov byte ptr gs:[0x85e], 0
006B8A6A  83 3D F3 E7 90 00 00            cmp dword ptr [rip + 0x90e7f3], 0
006B8A71  74 1F                           je 0x1406b8a92
006B8A73  B9 A7 06 00 00                  mov ecx, 0x6a7
006B8A78  0F 32                           rdmsr
006B8A7A  83 FA 00                        cmp edx, 0
006B8A7D  74 13                           je 0x1406b8a92
006B8A7F  8B CA                           mov ecx, edx
006B8A81  23 15 DD E7 90 00               and edx, dword ptr [rip + 0x90e7dd]
006B8A87  3B D1                           cmp edx, ecx
006B8A89  74 07                           je 0x1406b8a92
006B8A8B  B9 A7 06 00 00                  mov ecx, 0x6a7
006B8A90  0F 30                           wrmsr
006B8A92  41 F6 42 03 03                  test byte ptr [r10 + 3], 3
006B8A97  66 C7 85 80 00 00 00 00 00      mov word ptr [rbp + 0x80], 0
006B8AA0  74 05                           je 0x1406b8aa7
006B8AA2  E8 B9 4E E4 FF                  call 0x1404fd960
006B8AA7  FC                              cld
006B8AA8  0F AE 5D AC                     stmxcsr dword ptr [rbp - 0x54]
006B8AAC  65 0F AE 14 25 80 01 00 00      ldmxcsr dword ptr gs:[0x180]
006B8AB5  0F 29 45 F0                     movaps xmmword ptr [rbp - 0x10], xmm0
006B8AB9  0F 29 4D 00                     movaps xmmword ptr [rbp], xmm1
006B8ABD  0F 29 55 10                     movaps xmmword ptr [rbp + 0x10], xmm2
006B8AC1  0F 29 5D 20                     movaps xmmword ptr [rbp + 0x20], xmm3
006B8AC5  0F 29 65 30                     movaps xmmword ptr [rbp + 0x30], xmm4
006B8AC9  0F 29 6D 40                     movaps xmmword ptr [rbp + 0x40], xmm5
006B8ACD  F6 85 F0 00 00 00 01            test byte ptr [rbp + 0xf0], 1
006B8AD4  74 05                           je 0x1406b8adb
006B8AD6  E8 C5 34 D6 FF                  call 0x14041bfa0
006B8ADB  33 F6                           xor esi, esi
006B8ADD  65 FF 04 25 C0 87 00 00         inc dword ptr gs:[0x87c0]
006B8AE5  F6 05 04 E1 90 00 FF            test byte ptr [rip + 0x90e104], 0xff
006B8AEC  74 03                           je 0x1406b8af1
006B8AEE  0F 01 CA                        clac
006B8AF1  F6 05 CD E0 90 00 01            test byte ptr [rip + 0x90e0cd], 1
006B8AF8  74 24                           je 0x1406b8b1e
006B8AFA  65 0F BA 34 25 28 02 00 00 02   btr dword ptr gs:[0x228], 2
006B8B04  65 83 3C 25 28 02 00 00 00      cmp dword ptr gs:[0x228], 0
006B8B0D  75 0F                           jne 0x1406b8b1e
006B8B0F  B9 15 00 01 C0                  mov ecx, 0xc0010015
006B8B14  0F 32                           rdmsr
006B8B16  0F BA F2 00                     btr edx, 0
006B8B1A  73 02                           jae 0x1406b8b1e
006B8B1C  0F 30                           wrmsr
006B8B1E  B9 02 00 00 00                  mov ecx, 2
006B8B23  83 3D F6 E1 90 00 00            cmp dword ptr [rip + 0x90e1f6], 0
006B8B2A  74 07                           je 0x1406b8b33
006B8B2C  E8 AF FF EF FF                  call 0x1405b8ae0
006B8B31  EB 08                           jmp 0x1406b8b3b
006B8B33  44 0F 20 C0                     mov rax, cr8
006B8B37  44 0F 22 C1                     mov cr8, rcx
006B8B3B  88 45 A9                        mov byte ptr [rbp - 0x57], al
006B8B3E  48 8B CE                        mov rcx, rsi
006B8B41  E8 DA 02 D6 FF                  call 0x140418e20
006B8B46  FB                              sti
006B8B47  65 80 3C 25 87 01 00 00 00      cmp byte ptr gs:[0x187], 0
006B8B50  75 0D                           jne 0x1406b8b5f
006B8B52  48 8B 4D A9                     mov rcx, qword ptr [rbp - 0x57]
006B8B56  48 8D 55 80                     lea rdx, [rbp - 0x80]
006B8B5A  E8 91 2C B6 FF                  call 0x14021b7f0
006B8B5F  FA                              cli
006B8B60  0F B6 4D A9                     movzx ecx, byte ptr [rbp - 0x57]
006B8B64  83 3D B5 E1 90 00 00            cmp dword ptr [rip + 0x90e1b5], 0
006B8B6B  74 07                           je 0x1406b8b74
006B8B6D  E8 6E FF EF FF                  call 0x1405b8ae0
006B8B72  EB 04                           jmp 0x1406b8b78
006B8B74  44 0F 22 C1                     mov cr8, rcx
006B8B78  48 8B B5 D0 00 00 00            mov rsi, qword ptr [rbp + 0xd0]
006B8B7F  FA                              cli
006B8B80  F6 85 F0 00 00 00 01            test byte ptr [rbp + 0xf0], 1
006B8B87  0F 84 F5 02 00 00               je 0x1406b8e82
006B8B8D  F6 05 5C E0 90 00 FF            test byte ptr [rip + 0x90e05c], 0xff
006B8B94  74 03                           je 0x1406b8b99
006B8B96  0F 01 CB                        stac
006B8B99  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006B8BA2  F6 81 C2 00 00 00 03            test byte ptr [rcx + 0xc2], 3
006B8BA9  74 1B                           je 0x1406b8bc6
006B8BAB  B9 01 00 00 00                  mov ecx, 1
006B8BB0  44 0F 22 C1                     mov cr8, rcx
006B8BB4  FB                              sti
006B8BB5  E8 86 D9 FF FF                  call 0x1406b6540
006B8BBA  FA                              cli
006B8BBB  B9 00 00 00 00                  mov ecx, 0
006B8BC0  44 0F 22 C1                     mov cr8, rcx
006B8BC4  EB D3                           jmp 0x1406b8b99
006B8BC6  E8 95 B3 BA FF                  call 0x140263f60
006B8BCB  85 C0                           test eax, eax
006B8BCD  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
006B8BD1  75 C6                           jne 0x1406b8b99
006B8BD3  65 F6 04 25 60 08 00 00 02      test byte ptr gs:[0x860], 2
006B8BDC  74 07                           je 0x1406b8be5
006B8BDE  33 C9                           xor ecx, ecx
006B8BE0  E8 DB E5 D2 FF                  call 0x1403e71c0
006B8BE5  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006B8BEE  F7 01 00 00 00 08               test dword ptr [rcx], 0x8000000
006B8BF4  74 05                           je 0x1406b8bfb
006B8BF6  E8 A5 90 FF FF                  call 0x1406b1ca0
006B8BFB  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006B8C04  F7 01 00 00 01 00               test dword ptr [rcx], 0x10000
006B8C0A  74 14                           je 0x1406b8c20
006B8C0C  F6 41 02 01                     test byte ptr [rcx + 2], 1
006B8C10  74 0E                           je 0x1406b8c20
006B8C12  E8 F9 7A F0 FF                  call 0x1405c0710
006B8C17  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006B8C20  0F AE 55 AC                     ldmxcsr dword ptr [rbp - 0x54]
006B8C24  66 83 BD 80 00 00 00 00         cmp word ptr [rbp + 0x80], 0
006B8C2C  74 05                           je 0x1406b8c33
006B8C2E  E8 AD 4C E4 FF                  call 0x1404fd8e0
006B8C33  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006B8C3C  0F BA 61 74 16                  bt dword ptr [rcx + 0x74], 0x16
006B8C41  73 2A                           jae 0x1406b8c6d
006B8C43  33 C9                           xor ecx, ecx
006B8C45  F3 48 0F 1E C9                  rdsspq rcx
006B8C4A  65 4C 8B 04 25 28 9D 00 00      mov r8, qword ptr gs:[0x9d28]
006B8C53  49 83 C0 08                     add r8, 8
006B8C57  49 3B C8                        cmp rcx, r8
006B8C5A  75 11                           jne 0x1406b8c6d
006B8C5C  65 48 8B 0C 25 20 9D 00 00      mov rcx, qword ptr gs:[0x9d20]
006B8C65  F3 0F 01 29                     rstorssp dword ptr [rcx]
006B8C69  F3 0F 01 EA                     saveprevssp
006B8C6D  65 C6 04 25 5E 08 00 00 00      mov byte ptr gs:[0x85e], 0
006B8C76  65 0F B7 04 25 6C 08 00 00      movzx eax, word ptr gs:[0x86c]
006B8C7F  66 65 39 04 25 66 08 00 00      cmp word ptr gs:[0x866], ax
006B8C88  74 12                           je 0x1406b8c9c
006B8C8A  66 65 89 04 25 66 08 00 00      mov word ptr gs:[0x866], ax
006B8C93  B9 48 00 00 00                  mov ecx, 0x48
006B8C98  33 D2                           xor edx, edx
006B8C9A  0F 30                           wrmsr
006B8C9C  66 65 0F BA 34 25 58 08 00 00 02  btr word ptr gs:[0x858], 2
006B8CA7  73 0E                           jae 0x1406b8cb7
006B8CA9  B8 01 00 00 00                  mov eax, 1
006B8CAE  33 D2                           xor edx, edx
006B8CB0  B9 49 00 00 00                  mov ecx, 0x49
006B8CB5  0F 30                           wrmsr
006B8CB7  66 65 0F BA 34 25 58 08 00 00 05  btr word ptr gs:[0x858], 5
006B8CC2  0F 83 37 01 00 00               jae 0x1406b8dff
006B8CC8  E8 0E 01 00 00                  call 0x1406b8ddb
006B8CCD  48 83 C4 08                     add rsp, 8
006B8CD1  E8 0E 01 00 00                  call 0x1406b8de4
006B8CD6  48 83 C4 08                     add rsp, 8
006B8CDA  E8 EE FF FF FF                  call 0x1406b8ccd
006B8CDF  48 83 C4 08                     add rsp, 8
006B8CE3  E8 EE FF FF FF                  call 0x1406b8cd6
006B8CE8  48 83 C4 08                     add rsp, 8
006B8CEC  E8 EE FF FF FF                  call 0x1406b8cdf
006B8CF1  48 83 C4 08                     add rsp, 8
006B8CF5  E8 EE FF FF FF                  call 0x1406b8ce8
006B8CFA  48 83 C4 08                     add rsp, 8
006B8CFE  E8 EE FF FF FF                  call 0x1406b8cf1
006B8D03  48 83 C4 08                     add rsp, 8
006B8D07  E8 EE FF FF FF                  call 0x1406b8cfa
006B8D0C  48 83 C4 08                     add rsp, 8
006B8D10  E8 EE FF FF FF                  call 0x1406b8d03
006B8D15  48 83 C4 08                     add rsp, 8
006B8D19  E8 EE FF FF FF                  call 0x1406b8d0c
006B8D1E  48 83 C4 08                     add rsp, 8
006B8D22  E8 EE FF FF FF                  call 0x1406b8d15
006B8D27  48 83 C4 08                     add rsp, 8
006B8D2B  E8 EE FF FF FF                  call 0x1406b8d1e
006B8D30  48 83 C4 08                     add rsp, 8
006B8D34  E8 EE FF FF FF                  call 0x1406b8d27
006B8D39  48 83 C4 08                     add rsp, 8
006B8D3D  E8 EE FF FF FF                  call 0x1406b8d30
006B8D42  48 83 C4 08                     add rsp, 8
006B8D46  E8 EE FF FF FF                  call 0x1406b8d39
006B8D4B  48 83 C4 08                     add rsp, 8
006B8D4F  E8 EE FF FF FF                  call 0x1406b8d42
006B8D54  48 83 C4 08                     add rsp, 8
006B8D58  E8 EE FF FF FF                  call 0x1406b8d4b
006B8D5D  48 83 C4 08                     add rsp, 8
006B8D61  E8 EE FF FF FF                  call 0x1406b8d54
006B8D66  48 83 C4 08                     add rsp, 8
006B8D6A  E8 EE FF FF FF                  call 0x1406b8d5d
006B8D6F  48 83 C4 08                     add rsp, 8
006B8D73  E8 EE FF FF FF                  call 0x1406b8d66
006B8D78  48 83 C4 08                     add rsp, 8
006B8D7C  E8 EE FF FF FF                  call 0x1406b8d6f
006B8D81  48 83 C4 08                     add rsp, 8
006B8D85  E8 EE FF FF FF                  call 0x1406b8d78
006B8D8A  48 83 C4 08                     add rsp, 8
006B8D8E  E8 EE FF FF FF                  call 0x1406b8d81
006B8D93  48 83 C4 08                     add rsp, 8
006B8D97  E8 EE FF FF FF                  call 0x1406b8d8a
006B8D9C  48 83 C4 08                     add rsp, 8
006B8DA0  E8 EE FF FF FF                  call 0x1406b8d93
006B8DA5  48 83 C4 08                     add rsp, 8
006B8DA9  E8 EE FF FF FF                  call 0x1406b8d9c
006B8DAE  48 83 C4 08                     add rsp, 8
006B8DB2  E8 EE FF FF FF                  call 0x1406b8da5
006B8DB7  48 83 C4 08                     add rsp, 8
006B8DBB  E8 EE FF FF FF                  call 0x1406b8dae
006B8DC0  48 83 C4 08                     add rsp, 8
006B8DC4  E8 EE FF FF FF                  call 0x1406b8db7
006B8DC9  48 83 C4 08                     add rsp, 8
006B8DCD  E8 EE FF FF FF                  call 0x1406b8dc0
006B8DD2  48 83 C4 08                     add rsp, 8
006B8DD6  E8 EE FF FF FF                  call 0x1406b8dc9
006B8DDB  48 83 C4 08                     add rsp, 8
006B8DDF  E8 EE FF FF FF                  call 0x1406b8dd2
006B8DE4  48 83 C4 08                     add rsp, 8
006B8DE8  B8 DA DA 00 00                  mov eax, 0xdada
006B8DED  65 F6 04 25 5C 08 00 00 08      test byte ptr gs:[0x85c], 8
006B8DF6  74 07                           je 0x1406b8dff
006B8DF8  B0 20                           mov al, 0x20
006B8DFA  F3 48 0F AE E8                  incsspq rax
006B8DFF  66 65 F7 04 25 58 08 00 00 00 01  test word ptr gs:[0x858], 0x100
006B8E0A  74 0C                           je 0x1406b8e18
006B8E0C  33 C0                           xor eax, eax
006B8E0E  33 D2                           xor edx, edx
006B8E10  B9 01 00 00 00                  mov ecx, 1
006B8E15  48 F7 F1                        div rcx
006B8E18  0F 28 45 F0                     movaps xmm0, xmmword ptr [rbp - 0x10]
006B8E1C  0F 28 4D 00                     movaps xmm1, xmmword ptr [rbp]
006B8E20  0F 28 55 10                     movaps xmm2, xmmword ptr [rbp + 0x10]
006B8E24  0F 28 5D 20                     movaps xmm3, xmmword ptr [rbp + 0x20]
006B8E28  0F 28 65 30                     movaps xmm4, xmmword ptr [rbp + 0x30]
006B8E2C  0F 28 6D 40                     movaps xmm5, xmmword ptr [rbp + 0x40]
006B8E30  4C 8B 5D E0                     mov r11, qword ptr [rbp - 0x20]
006B8E34  4C 8B 55 D8                     mov r10, qword ptr [rbp - 0x28]
006B8E38  4C 8B 4D D0                     mov r9, qword ptr [rbp - 0x30]
006B8E3C  4C 8B 45 C8                     mov r8, qword ptr [rbp - 0x38]
006B8E40  48 8B 55 C0                     mov rdx, qword ptr [rbp - 0x40]
006B8E44  48 8B 4D B8                     mov rcx, qword ptr [rbp - 0x48]
006B8E48  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
006B8E4C  48 8B E5                        mov rsp, rbp
006B8E4F  48 8B AD D8 00 00 00            mov rbp, qword ptr [rbp + 0xd8]
006B8E56  48 81 C4 E8 00 00 00            add rsp, 0xe8
006B8E5D  F6 05 DC 89 B4 00 01            test byte ptr [rip + 0xb489dc], 1
006B8E64  74 05                           je 0x1406b8e6b
006B8E66  E9 15 3D 51 00                  jmp 0x140bccb80
006B8E6B  66 65 F7 04 25 58 08 00 00 00 02  test word ptr gs:[0x858], 0x200
006B8E76  74 05                           je 0x1406b8e7d
006B8E78  0F 00 6C 24 20                  verw word ptr [rsp + 0x20]
006B8E7D  0F 01 F8                        swapgs
006B8E80  48 CF                           iretq
006B8E82  0F AE 55 AC                     ldmxcsr dword ptr [rbp - 0x54]
006B8E86  0F 28 45 F0                     movaps xmm0, xmmword ptr [rbp - 0x10]
006B8E8A  0F 28 4D 00                     movaps xmm1, xmmword ptr [rbp]
006B8E8E  0F 28 55 10                     movaps xmm2, xmmword ptr [rbp + 0x10]
006B8E92  0F 28 5D 20                     movaps xmm3, xmmword ptr [rbp + 0x20]
006B8E96  0F 28 65 30                     movaps xmm4, xmmword ptr [rbp + 0x30]
006B8E9A  0F 28 6D 40                     movaps xmm5, xmmword ptr [rbp + 0x40]
006B8E9E  4C 8B 5D E0                     mov r11, qword ptr [rbp - 0x20]
006B8EA2  4C 8B 55 D8                     mov r10, qword ptr [rbp - 0x28]
006B8EA6  4C 8B 4D D0                     mov r9, qword ptr [rbp - 0x30]
006B8EAA  4C 8B 45 C8                     mov r8, qword ptr [rbp - 0x38]
006B8EAE  48 8B 55 C0                     mov rdx, qword ptr [rbp - 0x40]
006B8EB2  48 8B 4D B8                     mov rcx, qword ptr [rbp - 0x48]
006B8EB6  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
006B8EBA  48 8B E5                        mov rsp, rbp
006B8EBD  48 8B AD D8 00 00 00            mov rbp, qword ptr [rbp + 0xd8]
006B8EC4  48 81 C4 E8 00 00 00            add rsp, 0xe8
006B8ECB  48 CF                           iretq
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiDpcInterrupt(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
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
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF8;
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
    if (((v_stack_p8) & (1)) != 0) goto loc_006B8836;
    a2 = 0;
    v_stack_m90 = 0;
    if (((*(unsigned __int8 *)(gs_base + (0 + 2136))) & (1)) != 0) goto loc_006B881F;
    goto loc_006B8AA7;
loc_006B881F:
    a2 = 0;
    goto loc_006B8AA7;
loc_006B8836:
    if (((*(unsigned __int8 *)(v_rip + 11833347)) & (1)) == 0) {
    }
    if (*(unsigned __int64 *)(gs_base + (0 + 40232)) == 0) goto loc_006B8872;
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
    if ((((unsigned int)(a2)) & (2)) == 0) goto loc_006B8A4E;
    result = KiDpcInterrupt___0x26A(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiDpcInterrupt___0x273(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiDpcInterrupt___0x15C(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiDpcInterrupt___0x165(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiDpcInterrupt___0x16E(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiDpcInterrupt___0x177(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiDpcInterrupt___0x180(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiDpcInterrupt___0x189(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiDpcInterrupt___0x192(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiDpcInterrupt___0x19B(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiDpcInterrupt___0x1A4(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiDpcInterrupt___0x1AD(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiDpcInterrupt___0x1B6(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiDpcInterrupt___0x1BF(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiDpcInterrupt___0x1C8(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiDpcInterrupt___0x1D1(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiDpcInterrupt___0x1DA(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiDpcInterrupt___0x1E3(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiDpcInterrupt___0x1EC(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiDpcInterrupt___0x1F5(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiDpcInterrupt___0x1FE(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiDpcInterrupt___0x207(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiDpcInterrupt___0x210(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiDpcInterrupt___0x219(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiDpcInterrupt___0x222(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiDpcInterrupt___0x22B(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiDpcInterrupt___0x234(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiDpcInterrupt___0x23D(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiDpcInterrupt___0x246(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiDpcInterrupt___0x24F(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiDpcInterrupt___0x258(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiDpcInterrupt___0x261(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = (unsigned int)(0xDADAULL);
    if (((*(unsigned __int8 *)(gs_base + (0 + 2140))) & (8)) != 0) {
        result = 32;
    }
    if ((((unsigned int)(a2)) & (128)) != 0) {
        result = KiFlushBhbDuringTrapEntryOrExit(a1, a2, a3, a4);
    }
    *(unsigned __int8 *)(gs_base + (0 + 2142)) = 0;
    if ((*(unsigned int *)(v_rip + 9496563)) == 0) goto loc_006B8A92;
    if (((unsigned int)(a2)) == 0) goto loc_006B8A92;
    a2 = (unsigned int)((a2) & (*(unsigned int *)(v_rip + 9496541)));
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
    v_rsi = 0;
    if (((*(unsigned __int8 *)(v_rip + 9494788)) & (255)) != 0) {
    }
    if (((*(unsigned __int8 *)(v_rip + 9494733)) & (1)) == 0) goto loc_006B8B1E;
    if ((*(unsigned int *)(gs_base + (0 + 552))) != 0) goto loc_006B8B1E;
    if ((*(unsigned int *)(gs_base + (0 + 552))) < 0) {
    }
    if ((*(unsigned int *)(v_rip + 9495030)) == 0) goto loc_006B8B33;
    result = KzSetIrqlUnsafe(2, a2, a3, a4);
    goto loc_006B8B3B;
loc_006B8B33:
loc_006B8B3B:
    v_stack_m13F = (unsigned __int8)(v_cr8);
    result = HalPerformEndOfInterrupt(0, a2, a3, a4);
    if ((*(unsigned __int8 *)(gs_base + (0 + 391))) == 0) {
        a1 = v_stack_m13F;
        a2 = v_stack_m168;
        result = KiDispatchInterrupt(a1, a2, a3, a4);
    }
    if ((*(unsigned int *)(v_rip + 9494965)) == 0) goto loc_006B8B74;
    result = KzSetIrqlUnsafe(v_stack_m13F, a2, a3, a4);
    goto loc_006B8B78;
loc_006B8B74:
loc_006B8B78:
    if (((v_stack_p8) & (1)) == 0) goto loc_006B8E82;
    if (((*(unsigned __int8 *)(v_rip + 9494620)) & (255)) != 0) {
    }
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 194)) & (3)) == 0) goto loc_006B8BC6;
    result = KiInitiateUserApc(1, a2, a3, a4);
    goto loc_006B8B99;
loc_006B8BC6:
    result = KiSynchronizeUserIsolationDomainEntry(0, a2, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_006B8B99;
    result = v_stack_m138;
    if (((*(unsigned __int8 *)(gs_base + (0 + 2144))) & (2)) != 0) {
        a1 = 0;
        result = KiUpdateStibpPairing(a1, a2, a3, a4);
    }
    if (((*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)))) & (0x8000000ULL)) != 0) {
        result = KiRestoreSetContextState(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, a4);
    }
    if (((*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)))) & (0x10000ULL)) == 0) goto loc_006B8C20;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 2)) & (1)) != 0) {
        result = KiCopyCounters(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, a4);
        a1 = *(unsigned __int64 *)(gs_base + (0 + 392));
    }
    if (v_stack_m68 != 0) {
        result = KiRestoreDebugRegisterState(a1, a2, a3, a4);
    }
    if (v_stack_m68 >= 0) goto loc_006B8C6D;
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
    if (condition_is_above_or_equal) goto loc_006B8DFF;
    result = KiDpcInterrupt___0x61B(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiDpcInterrupt___0x624(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiDpcInterrupt___0x50D(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiDpcInterrupt___0x516(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiDpcInterrupt___0x51F(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiDpcInterrupt___0x528(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiDpcInterrupt___0x531(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiDpcInterrupt___0x53A(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiDpcInterrupt___0x543(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiDpcInterrupt___0x54C(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiDpcInterrupt___0x555(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiDpcInterrupt___0x55E(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiDpcInterrupt___0x567(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiDpcInterrupt___0x570(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiDpcInterrupt___0x579(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiDpcInterrupt___0x582(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiDpcInterrupt___0x58B(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiDpcInterrupt___0x594(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiDpcInterrupt___0x59D(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiDpcInterrupt___0x5A6(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiDpcInterrupt___0x5AF(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiDpcInterrupt___0x5B8(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiDpcInterrupt___0x5C1(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiDpcInterrupt___0x5CA(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiDpcInterrupt___0x5D3(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiDpcInterrupt___0x5DC(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiDpcInterrupt___0x5E5(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiDpcInterrupt___0x5EE(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiDpcInterrupt___0x5F7(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiDpcInterrupt___0x600(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiDpcInterrupt___0x609(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiDpcInterrupt___0x612(a1, a2, a3, a4);
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
    if (((*(unsigned __int8 *)(v_rip + 11831772)) & (1)) == 0) goto loc_006B8E6B;
loc_006B8E6B:
    if (((*(unsigned __int16 *)(gs_base + (0 + 2136))) & (512)) != 0) {
    }
loc_006B8E82:
    v_rsp = (v_stack_m10) + (232);
    return v_stack_m138;
}
```

## 5. (Beta) C Style

```c
int64_t KiDpcInterrupt(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
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
    uint64_t v_stack_m90;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF8;
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
    if (((v_stack_p8) & (1)) != 0) goto loc_006B8836;
    Arg2 = 0;
    v_stack_m90 = 0;
    if (((*(uint8_t *)(gs_base + (0 + 0x858))) & (1)) != 0) goto loc_006B881F;
    goto loc_006B8AA7;
loc_006B881F:
    Arg2 = 0;
    goto loc_006B8AA7;
loc_006B8836:
    if (((*(uint8_t *)(v_rip + 0xB49003)) & (1)) == 0) {
    }
    if (*(uint64_t *)(gs_base + (0 + 0x9D28)) == 0) goto loc_006B8872;
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
    if ((((uint32_t)(Arg2)) & (2)) == 0) goto loc_006B8A4E;
    result = KiDpcInterrupt___0x26A(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiDpcInterrupt___0x273(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiDpcInterrupt___0x15C(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiDpcInterrupt___0x165(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiDpcInterrupt___0x16E(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiDpcInterrupt___0x177(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiDpcInterrupt___0x180(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiDpcInterrupt___0x189(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiDpcInterrupt___0x192(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiDpcInterrupt___0x19B(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiDpcInterrupt___0x1A4(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiDpcInterrupt___0x1AD(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiDpcInterrupt___0x1B6(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiDpcInterrupt___0x1BF(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiDpcInterrupt___0x1C8(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiDpcInterrupt___0x1D1(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiDpcInterrupt___0x1DA(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiDpcInterrupt___0x1E3(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiDpcInterrupt___0x1EC(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiDpcInterrupt___0x1F5(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiDpcInterrupt___0x1FE(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiDpcInterrupt___0x207(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiDpcInterrupt___0x210(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiDpcInterrupt___0x219(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiDpcInterrupt___0x222(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiDpcInterrupt___0x22B(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiDpcInterrupt___0x234(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiDpcInterrupt___0x23D(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiDpcInterrupt___0x246(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiDpcInterrupt___0x24F(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiDpcInterrupt___0x258(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiDpcInterrupt___0x261(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = (uint32_t)(0xDADAULL);
    if (((*(uint8_t *)(gs_base + (0 + 0x85C))) & (8)) != 0) {
        result = 32;
    }
    if ((((uint32_t)(Arg2)) & (128)) != 0) {
        result = KiFlushBhbDuringTrapEntryOrExit(Arg1, Arg2, Arg3, Arg4);
    }
    *(uint8_t *)(gs_base + (0 + 0x85E)) = 0;
    if ((*(uint32_t *)(v_rip + 0x90E7F3)) == 0) goto loc_006B8A92;
    if (((uint32_t)(Arg2)) == 0) goto loc_006B8A92;
    Arg2 = (uint32_t)((Arg2) & (*(uint32_t *)(v_rip + 0x90E7DD)));
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
    local_rsi = 0;
    if (((*(uint8_t *)(v_rip + 0x90E104)) & (255)) != 0) {
    }
    if (((*(uint8_t *)(v_rip + 0x90E0CD)) & (1)) == 0) goto loc_006B8B1E;
    if ((*(uint32_t *)(gs_base + (0 + 0x228))) != 0) goto loc_006B8B1E;
    if ((*(uint32_t *)(gs_base + (0 + 0x228))) < 0) {
    }
    if ((*(uint32_t *)(v_rip + 0x90E1F6)) == 0) goto loc_006B8B33;
    result = KzSetIrqlUnsafe(2, Arg2, Arg3, Arg4);
    goto loc_006B8B3B;
loc_006B8B33:
loc_006B8B3B:
    v_stack_m13F = (uint8_t)(v_cr8);
    result = HalPerformEndOfInterrupt(0, Arg2, Arg3, Arg4);
    if ((*(uint8_t *)(gs_base + (0 + 0x187))) == 0) {
        Arg1 = v_stack_m13F;
        Arg2 = v_stack_m168;
        result = KiDispatchInterrupt(Arg1, Arg2, Arg3, Arg4);
    }
    if ((*(uint32_t *)(v_rip + 0x90E1B5)) == 0) goto loc_006B8B74;
    result = KzSetIrqlUnsafe(v_stack_m13F, Arg2, Arg3, Arg4);
    goto loc_006B8B78;
loc_006B8B74:
loc_006B8B78:
    if (((v_stack_p8) & (1)) == 0) goto loc_006B8E82;
    if (((*(uint8_t *)(v_rip + 0x90E05C)) & (255)) != 0) {
    }
    if (((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xC2)) & (3)) == 0) goto loc_006B8BC6;
    result = KiInitiateUserApc(1, Arg2, Arg3, Arg4);
    goto loc_006B8B99;
loc_006B8BC6:
    result = KiSynchronizeUserIsolationDomainEntry(0, Arg2, Arg3, Arg4);
    if ((uint32_t)(result) != 0) goto loc_006B8B99;
    result = v_stack_m138;
    if (((*(uint8_t *)(gs_base + (0 + 0x860))) & (2)) != 0) {
        Arg1 = 0;
        result = KiUpdateStibpPairing(Arg1, Arg2, Arg3, Arg4);
    }
    if (((*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)))) & (0x8000000ULL)) != 0) {
        result = KiRestoreSetContextState(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, Arg3, Arg4);
    }
    if (((*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)))) & (0x10000ULL)) == 0) goto loc_006B8C20;
    if (((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x2)) & (1)) != 0) {
        result = KiCopyCounters(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, Arg3, Arg4);
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x188));
    }
    if (v_stack_m68 != 0) {
        result = KiRestoreDebugRegisterState(Arg1, Arg2, Arg3, Arg4);
    }
    if (v_stack_m68 >= 0) goto loc_006B8C6D;
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
    if (condition_is_above_or_equal) goto loc_006B8DFF;
    result = KiDpcInterrupt___0x61B(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiDpcInterrupt___0x624(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiDpcInterrupt___0x50D(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiDpcInterrupt___0x516(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiDpcInterrupt___0x51F(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiDpcInterrupt___0x528(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiDpcInterrupt___0x531(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiDpcInterrupt___0x53A(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiDpcInterrupt___0x543(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiDpcInterrupt___0x54C(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiDpcInterrupt___0x555(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiDpcInterrupt___0x55E(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiDpcInterrupt___0x567(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiDpcInterrupt___0x570(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiDpcInterrupt___0x579(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiDpcInterrupt___0x582(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiDpcInterrupt___0x58B(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiDpcInterrupt___0x594(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiDpcInterrupt___0x59D(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiDpcInterrupt___0x5A6(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiDpcInterrupt___0x5AF(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiDpcInterrupt___0x5B8(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiDpcInterrupt___0x5C1(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiDpcInterrupt___0x5CA(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiDpcInterrupt___0x5D3(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiDpcInterrupt___0x5DC(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiDpcInterrupt___0x5E5(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiDpcInterrupt___0x5EE(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiDpcInterrupt___0x5F7(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiDpcInterrupt___0x600(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiDpcInterrupt___0x609(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiDpcInterrupt___0x612(Arg1, Arg2, Arg3, Arg4);
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
    if (((*(uint8_t *)(v_rip + 0xB489DC)) & (1)) == 0) goto loc_006B8E6B;
loc_006B8E6B:
    if (((*(uint16_t *)(gs_base + (0 + 0x858))) & (512)) != 0) {
    }
loc_006B8E82:
    local_rsp = (v_stack_m10) + (232);
    return v_stack_m138;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006B87C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
