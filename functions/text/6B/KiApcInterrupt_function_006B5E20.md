# KiApcInterrupt

- RVA: `0x006B5E20`–`0x006B6539` (길이 `1,817` bytes)
- VA: `0x00000001406B5E20`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C2158`
- 디코드: `398`개 명령, `1,817/1,817` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **77**; 고유 호출 대상: **76**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x006B5F77` → [KiApcInterrupt + 0x26A](KiApcInterrupt_function_006B5E20.md) (inside-function, `0x006B608A`)
- `0x006B5F80` → [KiApcInterrupt + 0x273](KiApcInterrupt_function_006B5E20.md) (inside-function, `0x006B6093`)
- `0x006B5F89` → [KiApcInterrupt + 0x15C](KiApcInterrupt_function_006B5E20.md) (inside-function, `0x006B5F7C`)
- `0x006B5F92` → [KiApcInterrupt + 0x165](KiApcInterrupt_function_006B5E20.md) (inside-function, `0x006B5F85`)
- `0x006B5F9B` → [KiApcInterrupt + 0x16E](KiApcInterrupt_function_006B5E20.md) (inside-function, `0x006B5F8E`)
- `0x006B5FA4` → [KiApcInterrupt + 0x177](KiApcInterrupt_function_006B5E20.md) (inside-function, `0x006B5F97`)
- `0x006B5FAD` → [KiApcInterrupt + 0x180](KiApcInterrupt_function_006B5E20.md) (inside-function, `0x006B5FA0`)
- `0x006B5FB6` → [KiApcInterrupt + 0x189](KiApcInterrupt_function_006B5E20.md) (inside-function, `0x006B5FA9`)
- `0x006B5FBF` → [KiApcInterrupt + 0x192](KiApcInterrupt_function_006B5E20.md) (inside-function, `0x006B5FB2`)
- `0x006B5FC8` → [KiApcInterrupt + 0x19B](KiApcInterrupt_function_006B5E20.md) (inside-function, `0x006B5FBB`)
- `0x006B5FD1` → [KiApcInterrupt + 0x1A4](KiApcInterrupt_function_006B5E20.md) (inside-function, `0x006B5FC4`)
- `0x006B5FDA` → [KiApcInterrupt + 0x1AD](KiApcInterrupt_function_006B5E20.md) (inside-function, `0x006B5FCD`)
- `0x006B5FE3` → [KiApcInterrupt + 0x1B6](KiApcInterrupt_function_006B5E20.md) (inside-function, `0x006B5FD6`)
- `0x006B5FEC` → [KiApcInterrupt + 0x1BF](KiApcInterrupt_function_006B5E20.md) (inside-function, `0x006B5FDF`)
- `0x006B5FF5` → [KiApcInterrupt + 0x1C8](KiApcInterrupt_function_006B5E20.md) (inside-function, `0x006B5FE8`)
- `0x006B5FFE` → [KiApcInterrupt + 0x1D1](KiApcInterrupt_function_006B5E20.md) (inside-function, `0x006B5FF1`)
- `0x006B6007` → [KiApcInterrupt + 0x1DA](KiApcInterrupt_function_006B5E20.md) (inside-function, `0x006B5FFA`)
- `0x006B6010` → [KiApcInterrupt + 0x1E3](KiApcInterrupt_function_006B5E20.md) (inside-function, `0x006B6003`)
- `0x006B6019` → [KiApcInterrupt + 0x1EC](KiApcInterrupt_function_006B5E20.md) (inside-function, `0x006B600C`)
- `0x006B6022` → [KiApcInterrupt + 0x1F5](KiApcInterrupt_function_006B5E20.md) (inside-function, `0x006B6015`)
- `0x006B602B` → [KiApcInterrupt + 0x1FE](KiApcInterrupt_function_006B5E20.md) (inside-function, `0x006B601E`)
- `0x006B6034` → [KiApcInterrupt + 0x207](KiApcInterrupt_function_006B5E20.md) (inside-function, `0x006B6027`)
- `0x006B603D` → [KiApcInterrupt + 0x210](KiApcInterrupt_function_006B5E20.md) (inside-function, `0x006B6030`)
- `0x006B6046` → [KiApcInterrupt + 0x219](KiApcInterrupt_function_006B5E20.md) (inside-function, `0x006B6039`)
- `0x006B604F` → [KiApcInterrupt + 0x222](KiApcInterrupt_function_006B5E20.md) (inside-function, `0x006B6042`)
- `0x006B6058` → [KiApcInterrupt + 0x22B](KiApcInterrupt_function_006B5E20.md) (inside-function, `0x006B604B`)
- `0x006B6061` → [KiApcInterrupt + 0x234](KiApcInterrupt_function_006B5E20.md) (inside-function, `0x006B6054`)
- `0x006B606A` → [KiApcInterrupt + 0x23D](KiApcInterrupt_function_006B5E20.md) (inside-function, `0x006B605D`)
- `0x006B6073` → [KiApcInterrupt + 0x246](KiApcInterrupt_function_006B5E20.md) (inside-function, `0x006B6066`)
- `0x006B607C` → [KiApcInterrupt + 0x24F](KiApcInterrupt_function_006B5E20.md) (inside-function, `0x006B606F`)
- `0x006B6085` → [KiApcInterrupt + 0x258](KiApcInterrupt_function_006B5E20.md) (inside-function, `0x006B6078`)
- `0x006B608E` → [KiApcInterrupt + 0x261](KiApcInterrupt_function_006B5E20.md) (inside-function, `0x006B6081`)
- `0x006B60B9` → [KiFlushBhbDuringTrapEntryOrExit](../6C/KiFlushBhbDuringTrapEntryOrExit_function_006C6340.md) (function, `0x006C6340`)
- `0x006B6102` → [KiSaveDebugRegisterState](../4F/KiSaveDebugRegisterState_function_004FD960.md) (function, `0x004FD960`)
- `0x006B6136` → [KiSynchronizeUserIsolationDomainExit](../41/KiSynchronizeUserIsolationDomainExit_function_0041BFA0.md) (function, `0x0041BFA0`)
- `0x006B6195` → [KzSetIrqlUnsafe](../5B/KzSetIrqlUnsafe_function_005B8AE0.md) (function, `0x005B8AE0`)
- `0x006B61AA` → [HalPerformEndOfInterrupt](../41/HalPerformEndOfInterrupt_function_00418E20.md) (function, `0x00418E20`)
- `0x006B61C6` → [KiDeliverApc](../25/KiDeliverApc_function_00250F20.md) (function, `0x00250F20`)
- `0x006B61D9` → [KzSetIrqlUnsafe](../5B/KzSetIrqlUnsafe_function_005B8AE0.md) (function, `0x005B8AE0`)
- `0x006B6221` → [KiInitiateUserApc](KiInitiateUserApc_function_006B6540.md) (function, `0x006B6540`)
- `0x006B6232` → [KiSynchronizeUserIsolationDomainEntry](../26/KiSynchronizeUserIsolationDomainEntry_function_00263F60.md) (function, `0x00263F60`)
- `0x006B624C` → [KiUpdateStibpPairing](../3E/KiUpdateStibpPairing_function_003E71C0.md) (function, `0x003E71C0`)
- `0x006B6262` → [KiRestoreSetContextState](KiRestoreSetContextState_function_006B1CA0.md) (function, `0x006B1CA0`)
- `0x006B627E` → [KiCopyCounters](../5C/KiCopyCounters_function_005C0710.md) (function, `0x005C0710`)
- `0x006B629A` → [KiRestoreDebugRegisterState](../4F/KiRestoreDebugRegisterState_function_004FD8E0.md) (function, `0x004FD8E0`)
- `0x006B6334` → [KiApcInterrupt + 0x627](KiApcInterrupt_function_006B5E20.md) (inside-function, `0x006B6447`)
- `0x006B633D` → [KiApcInterrupt + 0x630](KiApcInterrupt_function_006B5E20.md) (inside-function, `0x006B6450`)
- `0x006B6346` → [KiApcInterrupt + 0x519](KiApcInterrupt_function_006B5E20.md) (inside-function, `0x006B6339`)
- `0x006B634F` → [KiApcInterrupt + 0x522](KiApcInterrupt_function_006B5E20.md) (inside-function, `0x006B6342`)
- `0x006B6358` → [KiApcInterrupt + 0x52B](KiApcInterrupt_function_006B5E20.md) (inside-function, `0x006B634B`)
- `0x006B6361` → [KiApcInterrupt + 0x534](KiApcInterrupt_function_006B5E20.md) (inside-function, `0x006B6354`)
- `0x006B636A` → [KiApcInterrupt + 0x53D](KiApcInterrupt_function_006B5E20.md) (inside-function, `0x006B635D`)
- `0x006B6373` → [KiApcInterrupt + 0x546](KiApcInterrupt_function_006B5E20.md) (inside-function, `0x006B6366`)
- `0x006B637C` → [KiApcInterrupt + 0x54F](KiApcInterrupt_function_006B5E20.md) (inside-function, `0x006B636F`)
- `0x006B6385` → [KiApcInterrupt + 0x558](KiApcInterrupt_function_006B5E20.md) (inside-function, `0x006B6378`)
- `0x006B638E` → [KiApcInterrupt + 0x561](KiApcInterrupt_function_006B5E20.md) (inside-function, `0x006B6381`)
- `0x006B6397` → [KiApcInterrupt + 0x56A](KiApcInterrupt_function_006B5E20.md) (inside-function, `0x006B638A`)
- `0x006B63A0` → [KiApcInterrupt + 0x573](KiApcInterrupt_function_006B5E20.md) (inside-function, `0x006B6393`)
- `0x006B63A9` → [KiApcInterrupt + 0x57C](KiApcInterrupt_function_006B5E20.md) (inside-function, `0x006B639C`)
- `0x006B63B2` → [KiApcInterrupt + 0x585](KiApcInterrupt_function_006B5E20.md) (inside-function, `0x006B63A5`)
- `0x006B63BB` → [KiApcInterrupt + 0x58E](KiApcInterrupt_function_006B5E20.md) (inside-function, `0x006B63AE`)
- `0x006B63C4` → [KiApcInterrupt + 0x597](KiApcInterrupt_function_006B5E20.md) (inside-function, `0x006B63B7`)
- `0x006B63CD` → [KiApcInterrupt + 0x5A0](KiApcInterrupt_function_006B5E20.md) (inside-function, `0x006B63C0`)
- `0x006B63D6` → [KiApcInterrupt + 0x5A9](KiApcInterrupt_function_006B5E20.md) (inside-function, `0x006B63C9`)
- `0x006B63DF` → [KiApcInterrupt + 0x5B2](KiApcInterrupt_function_006B5E20.md) (inside-function, `0x006B63D2`)
- `0x006B63E8` → [KiApcInterrupt + 0x5BB](KiApcInterrupt_function_006B5E20.md) (inside-function, `0x006B63DB`)
- `0x006B63F1` → [KiApcInterrupt + 0x5C4](KiApcInterrupt_function_006B5E20.md) (inside-function, `0x006B63E4`)
- `0x006B63FA` → [KiApcInterrupt + 0x5CD](KiApcInterrupt_function_006B5E20.md) (inside-function, `0x006B63ED`)
- `0x006B6403` → [KiApcInterrupt + 0x5D6](KiApcInterrupt_function_006B5E20.md) (inside-function, `0x006B63F6`)
- `0x006B640C` → [KiApcInterrupt + 0x5DF](KiApcInterrupt_function_006B5E20.md) (inside-function, `0x006B63FF`)
- `0x006B6415` → [KiApcInterrupt + 0x5E8](KiApcInterrupt_function_006B5E20.md) (inside-function, `0x006B6408`)
- `0x006B641E` → [KiApcInterrupt + 0x5F1](KiApcInterrupt_function_006B5E20.md) (inside-function, `0x006B6411`)
- `0x006B6427` → [KiApcInterrupt + 0x5FA](KiApcInterrupt_function_006B5E20.md) (inside-function, `0x006B641A`)
- `0x006B6430` → [KiApcInterrupt + 0x603](KiApcInterrupt_function_006B5E20.md) (inside-function, `0x006B6423`)
- `0x006B6439` → [KiApcInterrupt + 0x60C](KiApcInterrupt_function_006B5E20.md) (inside-function, `0x006B642C`)
- `0x006B6442` → [KiApcInterrupt + 0x615](KiApcInterrupt_function_006B5E20.md) (inside-function, `0x006B6435`)
- `0x006B644B` → [KiApcInterrupt + 0x61E](KiApcInterrupt_function_006B5E20.md) (inside-function, `0x006B643E`)

### Direct callers
- [KiApcInterrupt](KiApcInterrupt_function_006B5E20.md) at `0x006B5F77`
- [KiApcInterrupt](KiApcInterrupt_function_006B5E20.md) at `0x006B5F80`
- [KiApcInterrupt](KiApcInterrupt_function_006B5E20.md) at `0x006B5F89`
- [KiApcInterrupt](KiApcInterrupt_function_006B5E20.md) at `0x006B5F92`
- [KiApcInterrupt](KiApcInterrupt_function_006B5E20.md) at `0x006B5F9B`
- [KiApcInterrupt](KiApcInterrupt_function_006B5E20.md) at `0x006B5FA4`
- [KiApcInterrupt](KiApcInterrupt_function_006B5E20.md) at `0x006B5FAD`
- [KiApcInterrupt](KiApcInterrupt_function_006B5E20.md) at `0x006B5FB6`
- [KiApcInterrupt](KiApcInterrupt_function_006B5E20.md) at `0x006B5FBF`
- [KiApcInterrupt](KiApcInterrupt_function_006B5E20.md) at `0x006B5FC8`
- [KiApcInterrupt](KiApcInterrupt_function_006B5E20.md) at `0x006B5FD1`
- [KiApcInterrupt](KiApcInterrupt_function_006B5E20.md) at `0x006B5FDA`
- [KiApcInterrupt](KiApcInterrupt_function_006B5E20.md) at `0x006B5FE3`
- [KiApcInterrupt](KiApcInterrupt_function_006B5E20.md) at `0x006B5FEC`
- [KiApcInterrupt](KiApcInterrupt_function_006B5E20.md) at `0x006B5FF5`
- [KiApcInterrupt](KiApcInterrupt_function_006B5E20.md) at `0x006B5FFE`
- [KiApcInterrupt](KiApcInterrupt_function_006B5E20.md) at `0x006B6007`
- [KiApcInterrupt](KiApcInterrupt_function_006B5E20.md) at `0x006B6010`
- [KiApcInterrupt](KiApcInterrupt_function_006B5E20.md) at `0x006B6019`
- [KiApcInterrupt](KiApcInterrupt_function_006B5E20.md) at `0x006B6022`
- [KiApcInterrupt](KiApcInterrupt_function_006B5E20.md) at `0x006B602B`
- [KiApcInterrupt](KiApcInterrupt_function_006B5E20.md) at `0x006B6034`
- [KiApcInterrupt](KiApcInterrupt_function_006B5E20.md) at `0x006B603D`
- [KiApcInterrupt](KiApcInterrupt_function_006B5E20.md) at `0x006B6046`
- [KiApcInterrupt](KiApcInterrupt_function_006B5E20.md) at `0x006B604F`
- [KiApcInterrupt](KiApcInterrupt_function_006B5E20.md) at `0x006B6058`
- [KiApcInterrupt](KiApcInterrupt_function_006B5E20.md) at `0x006B6061`
- [KiApcInterrupt](KiApcInterrupt_function_006B5E20.md) at `0x006B606A`
- [KiApcInterrupt](KiApcInterrupt_function_006B5E20.md) at `0x006B6073`
- [KiApcInterrupt](KiApcInterrupt_function_006B5E20.md) at `0x006B607C`
- [KiApcInterrupt](KiApcInterrupt_function_006B5E20.md) at `0x006B6085`
- [KiApcInterrupt](KiApcInterrupt_function_006B5E20.md) at `0x006B608E`
- [KiApcInterrupt](KiApcInterrupt_function_006B5E20.md) at `0x006B6334`
- [KiApcInterrupt](KiApcInterrupt_function_006B5E20.md) at `0x006B633D`
- [KiApcInterrupt](KiApcInterrupt_function_006B5E20.md) at `0x006B6346`
- [KiApcInterrupt](KiApcInterrupt_function_006B5E20.md) at `0x006B634F`
- [KiApcInterrupt](KiApcInterrupt_function_006B5E20.md) at `0x006B6358`
- [KiApcInterrupt](KiApcInterrupt_function_006B5E20.md) at `0x006B6361`
- [KiApcInterrupt](KiApcInterrupt_function_006B5E20.md) at `0x006B636A`
- [KiApcInterrupt](KiApcInterrupt_function_006B5E20.md) at `0x006B6373`
- [KiApcInterrupt](KiApcInterrupt_function_006B5E20.md) at `0x006B637C`
- [KiApcInterrupt](KiApcInterrupt_function_006B5E20.md) at `0x006B6385`
- [KiApcInterrupt](KiApcInterrupt_function_006B5E20.md) at `0x006B638E`
- [KiApcInterrupt](KiApcInterrupt_function_006B5E20.md) at `0x006B6397`
- [KiApcInterrupt](KiApcInterrupt_function_006B5E20.md) at `0x006B63A0`
- [KiApcInterrupt](KiApcInterrupt_function_006B5E20.md) at `0x006B63A9`
- [KiApcInterrupt](KiApcInterrupt_function_006B5E20.md) at `0x006B63B2`
- [KiApcInterrupt](KiApcInterrupt_function_006B5E20.md) at `0x006B63BB`
- [KiApcInterrupt](KiApcInterrupt_function_006B5E20.md) at `0x006B63C4`
- [KiApcInterrupt](KiApcInterrupt_function_006B5E20.md) at `0x006B63CD`
- [KiApcInterrupt](KiApcInterrupt_function_006B5E20.md) at `0x006B63D6`
- [KiApcInterrupt](KiApcInterrupt_function_006B5E20.md) at `0x006B63DF`
- [KiApcInterrupt](KiApcInterrupt_function_006B5E20.md) at `0x006B63E8`
- [KiApcInterrupt](KiApcInterrupt_function_006B5E20.md) at `0x006B63F1`
- [KiApcInterrupt](KiApcInterrupt_function_006B5E20.md) at `0x006B63FA`
- [KiApcInterrupt](KiApcInterrupt_function_006B5E20.md) at `0x006B6403`
- [KiApcInterrupt](KiApcInterrupt_function_006B5E20.md) at `0x006B640C`
- [KiApcInterrupt](KiApcInterrupt_function_006B5E20.md) at `0x006B6415`
- [KiApcInterrupt](KiApcInterrupt_function_006B5E20.md) at `0x006B641E`
- [KiApcInterrupt](KiApcInterrupt_function_006B5E20.md) at `0x006B6427`
- [KiApcInterrupt](KiApcInterrupt_function_006B5E20.md) at `0x006B6430`
- [KiApcInterrupt](KiApcInterrupt_function_006B5E20.md) at `0x006B6439`
- [KiApcInterrupt](KiApcInterrupt_function_006B5E20.md) at `0x006B6442`
- [KiApcInterrupt](KiApcInterrupt_function_006B5E20.md) at `0x006B644B`

### Static image references
- `0x006B5E96` → RVA `0x01201840` (`CFGRO`; read)
- `0x006B60CA` → RVA `0x00FC7264` (`ALMOSTRO`; read)
- `0x006B6145` → RVA `0x00FC6BF0` (`ALMOSTRO`; read)
- `0x006B615A` → RVA `0x00FC6BC5` (`ALMOSTRO`; read)
- `0x006B618C` → RVA `0x00FC6D20` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006B64D2` → [KiKernelExit](../../kvascode/BC/KiKernelExit_function_00BCCB80.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006B5E20  48 83 EC 08                     sub rsp, 8
006B5E24  55                              push rbp
006B5E25  56                              push rsi
006B5E26  48 81 EC 50 01 00 00            sub rsp, 0x150
006B5E2D  48 8D AC 24 80 00 00 00         lea rbp, [rsp + 0x80]
006B5E35  C6 45 AB 00                     mov byte ptr [rbp - 0x55], 0
006B5E39  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
006B5E3D  48 89 4D B8                     mov qword ptr [rbp - 0x48], rcx
006B5E41  48 89 55 C0                     mov qword ptr [rbp - 0x40], rdx
006B5E45  4C 89 45 C8                     mov qword ptr [rbp - 0x38], r8
006B5E49  4C 89 4D D0                     mov qword ptr [rbp - 0x30], r9
006B5E4D  4C 89 55 D8                     mov qword ptr [rbp - 0x28], r10
006B5E51  4C 89 5D E0                     mov qword ptr [rbp - 0x20], r11
006B5E55  F6 85 F0 00 00 00 01            test byte ptr [rbp + 0xf0], 1
006B5E5C  75 38                           jne 0x1406b5e96
006B5E5E  33 D2                           xor edx, edx
006B5E60  F3 48 0F 1E CA                  rdsspq rdx
006B5E65  48 89 55 58                     mov qword ptr [rbp + 0x58], rdx
006B5E69  0F AE E8                        lfence
006B5E6C  65 F6 04 25 58 08 00 00 01      test byte ptr gs:[0x858], 1
006B5E75  75 08                           jne 0x1406b5e7f
006B5E77  0F AE E8                        lfence
006B5E7A  E9 88 02 00 00                  jmp 0x1406b6107
006B5E7F  65 0F B7 04 25 66 08 00 00      movzx eax, word ptr gs:[0x866]
006B5E88  B9 48 00 00 00                  mov ecx, 0x48
006B5E8D  33 D2                           xor edx, edx
006B5E8F  0F 30                           wrmsr
006B5E91  E9 71 02 00 00                  jmp 0x1406b6107
006B5E96  F6 05 A3 B9 B4 00 01            test byte ptr [rip + 0xb4b9a3], 1
006B5E9D  75 03                           jne 0x1406b5ea2
006B5E9F  0F 01 F8                        swapgs
006B5EA2  0F AE E8                        lfence
006B5EA5  65 48 8B 0C 25 28 9D 00 00      mov rcx, qword ptr gs:[0x9d28]
006B5EAE  48 85 C9                        test rcx, rcx
006B5EB1  74 1F                           je 0x1406b5ed2
006B5EB3  F3 48 0F 1E CA                  rdsspq rdx
006B5EB8  65 4C 8B 14 25 20 9D 00 00      mov r10, qword ptr gs:[0x9d20]
006B5EC1  49 83 C2 08                     add r10, 8
006B5EC5  49 3B D2                        cmp rdx, r10
006B5EC8  75 08                           jne 0x1406b5ed2
006B5ECA  F3 0F 01 29                     rstorssp dword ptr [rcx]
006B5ECE  F3 0F 01 EA                     saveprevssp
006B5ED2  65 4C 8B 14 25 88 01 00 00      mov r10, qword ptr gs:[0x188]
006B5EDB  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006B5EE4  48 8B 89 20 02 00 00            mov rcx, qword ptr [rcx + 0x220]
006B5EEB  48 8B 89 60 07 00 00            mov rcx, qword ptr [rcx + 0x760]
006B5EF2  65 48 89 0C 25 50 08 00 00      mov qword ptr gs:[0x850], rcx
006B5EFB  66 65 8B 0C 25 62 08 00 00      mov cx, word ptr gs:[0x862]
006B5F04  66 65 89 0C 25 64 08 00 00      mov word ptr gs:[0x864], cx
006B5F0D  65 8A 0C 25 58 08 00 00         mov cl, byte ptr gs:[0x858]
006B5F15  65 88 0C 25 5A 08 00 00         mov byte ptr gs:[0x85a], cl
006B5F1D  65 0F B7 04 25 68 08 00 00      movzx eax, word ptr gs:[0x868]
006B5F26  66 65 39 04 25 66 08 00 00      cmp word ptr gs:[0x866], ax
006B5F2F  74 12                           je 0x1406b5f43
006B5F31  66 65 89 04 25 66 08 00 00      mov word ptr gs:[0x866], ax
006B5F3A  B9 48 00 00 00                  mov ecx, 0x48
006B5F3F  33 D2                           xor edx, edx
006B5F41  0F 30                           wrmsr
006B5F43  65 0F B6 14 25 58 08 00 00      movzx edx, byte ptr gs:[0x858]
006B5F4C  F7 C2 08 00 00 00               test edx, 8
006B5F52  74 17                           je 0x1406b5f6b
006B5F54  B8 01 00 00 00                  mov eax, 1
006B5F59  33 D2                           xor edx, edx
006B5F5B  B9 49 00 00 00                  mov ecx, 0x49
006B5F60  0F 30                           wrmsr
006B5F62  65 0F B6 14 25 58 08 00 00      movzx edx, byte ptr gs:[0x858]
006B5F6B  F7 C2 02 00 00 00               test edx, 2
006B5F71  0F 84 37 01 00 00               je 0x1406b60ae
006B5F77  E8 0E 01 00 00                  call 0x1406b608a
006B5F7C  48 83 C4 08                     add rsp, 8
006B5F80  E8 0E 01 00 00                  call 0x1406b6093
006B5F85  48 83 C4 08                     add rsp, 8
006B5F89  E8 EE FF FF FF                  call 0x1406b5f7c
006B5F8E  48 83 C4 08                     add rsp, 8
006B5F92  E8 EE FF FF FF                  call 0x1406b5f85
006B5F97  48 83 C4 08                     add rsp, 8
006B5F9B  E8 EE FF FF FF                  call 0x1406b5f8e
006B5FA0  48 83 C4 08                     add rsp, 8
006B5FA4  E8 EE FF FF FF                  call 0x1406b5f97
006B5FA9  48 83 C4 08                     add rsp, 8
006B5FAD  E8 EE FF FF FF                  call 0x1406b5fa0
006B5FB2  48 83 C4 08                     add rsp, 8
006B5FB6  E8 EE FF FF FF                  call 0x1406b5fa9
006B5FBB  48 83 C4 08                     add rsp, 8
006B5FBF  E8 EE FF FF FF                  call 0x1406b5fb2
006B5FC4  48 83 C4 08                     add rsp, 8
006B5FC8  E8 EE FF FF FF                  call 0x1406b5fbb
006B5FCD  48 83 C4 08                     add rsp, 8
006B5FD1  E8 EE FF FF FF                  call 0x1406b5fc4
006B5FD6  48 83 C4 08                     add rsp, 8
006B5FDA  E8 EE FF FF FF                  call 0x1406b5fcd
006B5FDF  48 83 C4 08                     add rsp, 8
006B5FE3  E8 EE FF FF FF                  call 0x1406b5fd6
006B5FE8  48 83 C4 08                     add rsp, 8
006B5FEC  E8 EE FF FF FF                  call 0x1406b5fdf
006B5FF1  48 83 C4 08                     add rsp, 8
006B5FF5  E8 EE FF FF FF                  call 0x1406b5fe8
006B5FFA  48 83 C4 08                     add rsp, 8
006B5FFE  E8 EE FF FF FF                  call 0x1406b5ff1
006B6003  48 83 C4 08                     add rsp, 8
006B6007  E8 EE FF FF FF                  call 0x1406b5ffa
006B600C  48 83 C4 08                     add rsp, 8
006B6010  E8 EE FF FF FF                  call 0x1406b6003
006B6015  48 83 C4 08                     add rsp, 8
006B6019  E8 EE FF FF FF                  call 0x1406b600c
006B601E  48 83 C4 08                     add rsp, 8
006B6022  E8 EE FF FF FF                  call 0x1406b6015
006B6027  48 83 C4 08                     add rsp, 8
006B602B  E8 EE FF FF FF                  call 0x1406b601e
006B6030  48 83 C4 08                     add rsp, 8
006B6034  E8 EE FF FF FF                  call 0x1406b6027
006B6039  48 83 C4 08                     add rsp, 8
006B603D  E8 EE FF FF FF                  call 0x1406b6030
006B6042  48 83 C4 08                     add rsp, 8
006B6046  E8 EE FF FF FF                  call 0x1406b6039
006B604B  48 83 C4 08                     add rsp, 8
006B604F  E8 EE FF FF FF                  call 0x1406b6042
006B6054  48 83 C4 08                     add rsp, 8
006B6058  E8 EE FF FF FF                  call 0x1406b604b
006B605D  48 83 C4 08                     add rsp, 8
006B6061  E8 EE FF FF FF                  call 0x1406b6054
006B6066  48 83 C4 08                     add rsp, 8
006B606A  E8 EE FF FF FF                  call 0x1406b605d
006B606F  48 83 C4 08                     add rsp, 8
006B6073  E8 EE FF FF FF                  call 0x1406b6066
006B6078  48 83 C4 08                     add rsp, 8
006B607C  E8 EE FF FF FF                  call 0x1406b606f
006B6081  48 83 C4 08                     add rsp, 8
006B6085  E8 EE FF FF FF                  call 0x1406b6078
006B608A  48 83 C4 08                     add rsp, 8
006B608E  E8 EE FF FF FF                  call 0x1406b6081
006B6093  48 83 C4 08                     add rsp, 8
006B6097  B8 DA DA 00 00                  mov eax, 0xdada
006B609C  65 F6 04 25 5C 08 00 00 08      test byte ptr gs:[0x85c], 8
006B60A5  74 07                           je 0x1406b60ae
006B60A7  B0 20                           mov al, 0x20
006B60A9  F3 48 0F AE E8                  incsspq rax
006B60AE  F7 C2 80 00 00 00               test edx, 0x80
006B60B4  74 08                           je 0x1406b60be
006B60B6  0F AE E8                        lfence
006B60B9  E8 82 02 01 00                  call 0x1406c6340
006B60BE  0F AE E8                        lfence
006B60C1  65 C6 04 25 5E 08 00 00 00      mov byte ptr gs:[0x85e], 0
006B60CA  83 3D 93 11 91 00 00            cmp dword ptr [rip + 0x911193], 0
006B60D1  74 1F                           je 0x1406b60f2
006B60D3  B9 A7 06 00 00                  mov ecx, 0x6a7
006B60D8  0F 32                           rdmsr
006B60DA  83 FA 00                        cmp edx, 0
006B60DD  74 13                           je 0x1406b60f2
006B60DF  8B CA                           mov ecx, edx
006B60E1  23 15 7D 11 91 00               and edx, dword ptr [rip + 0x91117d]
006B60E7  3B D1                           cmp edx, ecx
006B60E9  74 07                           je 0x1406b60f2
006B60EB  B9 A7 06 00 00                  mov ecx, 0x6a7
006B60F0  0F 30                           wrmsr
006B60F2  41 F6 42 03 03                  test byte ptr [r10 + 3], 3
006B60F7  66 C7 85 80 00 00 00 00 00      mov word ptr [rbp + 0x80], 0
006B6100  74 05                           je 0x1406b6107
006B6102  E8 59 78 E4 FF                  call 0x1404fd960
006B6107  FC                              cld
006B6108  0F AE 5D AC                     stmxcsr dword ptr [rbp - 0x54]
006B610C  65 0F AE 14 25 80 01 00 00      ldmxcsr dword ptr gs:[0x180]
006B6115  0F 29 45 F0                     movaps xmmword ptr [rbp - 0x10], xmm0
006B6119  0F 29 4D 00                     movaps xmmword ptr [rbp], xmm1
006B611D  0F 29 55 10                     movaps xmmword ptr [rbp + 0x10], xmm2
006B6121  0F 29 5D 20                     movaps xmmword ptr [rbp + 0x20], xmm3
006B6125  0F 29 65 30                     movaps xmmword ptr [rbp + 0x30], xmm4
006B6129  0F 29 6D 40                     movaps xmmword ptr [rbp + 0x40], xmm5
006B612D  F6 85 F0 00 00 00 01            test byte ptr [rbp + 0xf0], 1
006B6134  74 05                           je 0x1406b613b
006B6136  E8 65 5E D6 FF                  call 0x14041bfa0
006B613B  33 F6                           xor esi, esi
006B613D  65 FF 04 25 C0 87 00 00         inc dword ptr gs:[0x87c0]
006B6145  F6 05 A4 0A 91 00 FF            test byte ptr [rip + 0x910aa4], 0xff
006B614C  74 0C                           je 0x1406b615a
006B614E  F6 85 F0 00 00 00 01            test byte ptr [rbp + 0xf0], 1
006B6155  74 03                           je 0x1406b615a
006B6157  0F 01 CB                        stac
006B615A  F6 05 64 0A 91 00 01            test byte ptr [rip + 0x910a64], 1
006B6161  74 24                           je 0x1406b6187
006B6163  65 0F BA 34 25 28 02 00 00 01   btr dword ptr gs:[0x228], 1
006B616D  65 83 3C 25 28 02 00 00 00      cmp dword ptr gs:[0x228], 0
006B6176  75 0F                           jne 0x1406b6187
006B6178  B9 15 00 01 C0                  mov ecx, 0xc0010015
006B617D  0F 32                           rdmsr
006B617F  0F BA F2 00                     btr edx, 0
006B6183  73 02                           jae 0x1406b6187
006B6185  0F 30                           wrmsr
006B6187  B9 01 00 00 00                  mov ecx, 1
006B618C  83 3D 8D 0B 91 00 00            cmp dword ptr [rip + 0x910b8d], 0
006B6193  74 07                           je 0x1406b619c
006B6195  E8 46 29 F0 FF                  call 0x1405b8ae0
006B619A  EB 08                           jmp 0x1406b61a4
006B619C  44 0F 20 C0                     mov rax, cr8
006B61A0  44 0F 22 C1                     mov cr8, rcx
006B61A4  88 45 A9                        mov byte ptr [rbp - 0x57], al
006B61A7  48 8B CE                        mov rcx, rsi
006B61AA  E8 71 2C D6 FF                  call 0x140418e20
006B61AF  FB                              sti
006B61B0  65 80 3C 25 87 01 00 00 00      cmp byte ptr gs:[0x187], 0
006B61B9  75 10                           jne 0x1406b61cb
006B61BB  B9 00 00 00 00                  mov ecx, 0
006B61C0  33 D2                           xor edx, edx
006B61C2  4C 8D 45 80                     lea r8, [rbp - 0x80]
006B61C6  E8 55 AD B9 FF                  call 0x140250f20
006B61CB  FA                              cli
006B61CC  0F B6 4D A9                     movzx ecx, byte ptr [rbp - 0x57]
006B61D0  83 3D 49 0B 91 00 00            cmp dword ptr [rip + 0x910b49], 0
006B61D7  74 07                           je 0x1406b61e0
006B61D9  E8 02 29 F0 FF                  call 0x1405b8ae0
006B61DE  EB 04                           jmp 0x1406b61e4
006B61E0  44 0F 22 C1                     mov cr8, rcx
006B61E4  48 8B B5 D0 00 00 00            mov rsi, qword ptr [rbp + 0xd0]
006B61EB  FA                              cli
006B61EC  F6 85 F0 00 00 00 01            test byte ptr [rbp + 0xf0], 1
006B61F3  0F 84 F5 02 00 00               je 0x1406b64ee
006B61F9  F6 05 F0 09 91 00 FF            test byte ptr [rip + 0x9109f0], 0xff
006B6200  74 03                           je 0x1406b6205
006B6202  0F 01 CB                        stac
006B6205  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006B620E  F6 81 C2 00 00 00 03            test byte ptr [rcx + 0xc2], 3
006B6215  74 1B                           je 0x1406b6232
006B6217  B9 01 00 00 00                  mov ecx, 1
006B621C  44 0F 22 C1                     mov cr8, rcx
006B6220  FB                              sti
006B6221  E8 1A 03 00 00                  call 0x1406b6540
006B6226  FA                              cli
006B6227  B9 00 00 00 00                  mov ecx, 0
006B622C  44 0F 22 C1                     mov cr8, rcx
006B6230  EB D3                           jmp 0x1406b6205
006B6232  E8 29 DD BA FF                  call 0x140263f60
006B6237  85 C0                           test eax, eax
006B6239  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
006B623D  75 C6                           jne 0x1406b6205
006B623F  65 F6 04 25 60 08 00 00 02      test byte ptr gs:[0x860], 2
006B6248  74 07                           je 0x1406b6251
006B624A  33 C9                           xor ecx, ecx
006B624C  E8 6F 0F D3 FF                  call 0x1403e71c0
006B6251  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006B625A  F7 01 00 00 00 08               test dword ptr [rcx], 0x8000000
006B6260  74 05                           je 0x1406b6267
006B6262  E8 39 BA FF FF                  call 0x1406b1ca0
006B6267  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006B6270  F7 01 00 00 01 00               test dword ptr [rcx], 0x10000
006B6276  74 14                           je 0x1406b628c
006B6278  F6 41 02 01                     test byte ptr [rcx + 2], 1
006B627C  74 0E                           je 0x1406b628c
006B627E  E8 8D A4 F0 FF                  call 0x1405c0710
006B6283  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006B628C  0F AE 55 AC                     ldmxcsr dword ptr [rbp - 0x54]
006B6290  66 83 BD 80 00 00 00 00         cmp word ptr [rbp + 0x80], 0
006B6298  74 05                           je 0x1406b629f
006B629A  E8 41 76 E4 FF                  call 0x1404fd8e0
006B629F  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006B62A8  0F BA 61 74 16                  bt dword ptr [rcx + 0x74], 0x16
006B62AD  73 2A                           jae 0x1406b62d9
006B62AF  33 C9                           xor ecx, ecx
006B62B1  F3 48 0F 1E C9                  rdsspq rcx
006B62B6  65 4C 8B 04 25 28 9D 00 00      mov r8, qword ptr gs:[0x9d28]
006B62BF  49 83 C0 08                     add r8, 8
006B62C3  49 3B C8                        cmp rcx, r8
006B62C6  75 11                           jne 0x1406b62d9
006B62C8  65 48 8B 0C 25 20 9D 00 00      mov rcx, qword ptr gs:[0x9d20]
006B62D1  F3 0F 01 29                     rstorssp dword ptr [rcx]
006B62D5  F3 0F 01 EA                     saveprevssp
006B62D9  65 C6 04 25 5E 08 00 00 00      mov byte ptr gs:[0x85e], 0
006B62E2  65 0F B7 04 25 6C 08 00 00      movzx eax, word ptr gs:[0x86c]
006B62EB  66 65 39 04 25 66 08 00 00      cmp word ptr gs:[0x866], ax
006B62F4  74 12                           je 0x1406b6308
006B62F6  66 65 89 04 25 66 08 00 00      mov word ptr gs:[0x866], ax
006B62FF  B9 48 00 00 00                  mov ecx, 0x48
006B6304  33 D2                           xor edx, edx
006B6306  0F 30                           wrmsr
006B6308  66 65 0F BA 34 25 58 08 00 00 02  btr word ptr gs:[0x858], 2
006B6313  73 0E                           jae 0x1406b6323
006B6315  B8 01 00 00 00                  mov eax, 1
006B631A  33 D2                           xor edx, edx
006B631C  B9 49 00 00 00                  mov ecx, 0x49
006B6321  0F 30                           wrmsr
006B6323  66 65 0F BA 34 25 58 08 00 00 05  btr word ptr gs:[0x858], 5
006B632E  0F 83 37 01 00 00               jae 0x1406b646b
006B6334  E8 0E 01 00 00                  call 0x1406b6447
006B6339  48 83 C4 08                     add rsp, 8
006B633D  E8 0E 01 00 00                  call 0x1406b6450
006B6342  48 83 C4 08                     add rsp, 8
006B6346  E8 EE FF FF FF                  call 0x1406b6339
006B634B  48 83 C4 08                     add rsp, 8
006B634F  E8 EE FF FF FF                  call 0x1406b6342
006B6354  48 83 C4 08                     add rsp, 8
006B6358  E8 EE FF FF FF                  call 0x1406b634b
006B635D  48 83 C4 08                     add rsp, 8
006B6361  E8 EE FF FF FF                  call 0x1406b6354
006B6366  48 83 C4 08                     add rsp, 8
006B636A  E8 EE FF FF FF                  call 0x1406b635d
006B636F  48 83 C4 08                     add rsp, 8
006B6373  E8 EE FF FF FF                  call 0x1406b6366
006B6378  48 83 C4 08                     add rsp, 8
006B637C  E8 EE FF FF FF                  call 0x1406b636f
006B6381  48 83 C4 08                     add rsp, 8
006B6385  E8 EE FF FF FF                  call 0x1406b6378
006B638A  48 83 C4 08                     add rsp, 8
006B638E  E8 EE FF FF FF                  call 0x1406b6381
006B6393  48 83 C4 08                     add rsp, 8
006B6397  E8 EE FF FF FF                  call 0x1406b638a
006B639C  48 83 C4 08                     add rsp, 8
006B63A0  E8 EE FF FF FF                  call 0x1406b6393
006B63A5  48 83 C4 08                     add rsp, 8
006B63A9  E8 EE FF FF FF                  call 0x1406b639c
006B63AE  48 83 C4 08                     add rsp, 8
006B63B2  E8 EE FF FF FF                  call 0x1406b63a5
006B63B7  48 83 C4 08                     add rsp, 8
006B63BB  E8 EE FF FF FF                  call 0x1406b63ae
006B63C0  48 83 C4 08                     add rsp, 8
006B63C4  E8 EE FF FF FF                  call 0x1406b63b7
006B63C9  48 83 C4 08                     add rsp, 8
006B63CD  E8 EE FF FF FF                  call 0x1406b63c0
006B63D2  48 83 C4 08                     add rsp, 8
006B63D6  E8 EE FF FF FF                  call 0x1406b63c9
006B63DB  48 83 C4 08                     add rsp, 8
006B63DF  E8 EE FF FF FF                  call 0x1406b63d2
006B63E4  48 83 C4 08                     add rsp, 8
006B63E8  E8 EE FF FF FF                  call 0x1406b63db
006B63ED  48 83 C4 08                     add rsp, 8
006B63F1  E8 EE FF FF FF                  call 0x1406b63e4
006B63F6  48 83 C4 08                     add rsp, 8
006B63FA  E8 EE FF FF FF                  call 0x1406b63ed
006B63FF  48 83 C4 08                     add rsp, 8
006B6403  E8 EE FF FF FF                  call 0x1406b63f6
006B6408  48 83 C4 08                     add rsp, 8
006B640C  E8 EE FF FF FF                  call 0x1406b63ff
006B6411  48 83 C4 08                     add rsp, 8
006B6415  E8 EE FF FF FF                  call 0x1406b6408
006B641A  48 83 C4 08                     add rsp, 8
006B641E  E8 EE FF FF FF                  call 0x1406b6411
006B6423  48 83 C4 08                     add rsp, 8
006B6427  E8 EE FF FF FF                  call 0x1406b641a
006B642C  48 83 C4 08                     add rsp, 8
006B6430  E8 EE FF FF FF                  call 0x1406b6423
006B6435  48 83 C4 08                     add rsp, 8
006B6439  E8 EE FF FF FF                  call 0x1406b642c
006B643E  48 83 C4 08                     add rsp, 8
006B6442  E8 EE FF FF FF                  call 0x1406b6435
006B6447  48 83 C4 08                     add rsp, 8
006B644B  E8 EE FF FF FF                  call 0x1406b643e
006B6450  48 83 C4 08                     add rsp, 8
006B6454  B8 DA DA 00 00                  mov eax, 0xdada
006B6459  65 F6 04 25 5C 08 00 00 08      test byte ptr gs:[0x85c], 8
006B6462  74 07                           je 0x1406b646b
006B6464  B0 20                           mov al, 0x20
006B6466  F3 48 0F AE E8                  incsspq rax
006B646B  66 65 F7 04 25 58 08 00 00 00 01  test word ptr gs:[0x858], 0x100
006B6476  74 0C                           je 0x1406b6484
006B6478  33 C0                           xor eax, eax
006B647A  33 D2                           xor edx, edx
006B647C  B9 01 00 00 00                  mov ecx, 1
006B6481  48 F7 F1                        div rcx
006B6484  0F 28 45 F0                     movaps xmm0, xmmword ptr [rbp - 0x10]
006B6488  0F 28 4D 00                     movaps xmm1, xmmword ptr [rbp]
006B648C  0F 28 55 10                     movaps xmm2, xmmword ptr [rbp + 0x10]
006B6490  0F 28 5D 20                     movaps xmm3, xmmword ptr [rbp + 0x20]
006B6494  0F 28 65 30                     movaps xmm4, xmmword ptr [rbp + 0x30]
006B6498  0F 28 6D 40                     movaps xmm5, xmmword ptr [rbp + 0x40]
006B649C  4C 8B 5D E0                     mov r11, qword ptr [rbp - 0x20]
006B64A0  4C 8B 55 D8                     mov r10, qword ptr [rbp - 0x28]
006B64A4  4C 8B 4D D0                     mov r9, qword ptr [rbp - 0x30]
006B64A8  4C 8B 45 C8                     mov r8, qword ptr [rbp - 0x38]
006B64AC  48 8B 55 C0                     mov rdx, qword ptr [rbp - 0x40]
006B64B0  48 8B 4D B8                     mov rcx, qword ptr [rbp - 0x48]
006B64B4  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
006B64B8  48 8B E5                        mov rsp, rbp
006B64BB  48 8B AD D8 00 00 00            mov rbp, qword ptr [rbp + 0xd8]
006B64C2  48 81 C4 E8 00 00 00            add rsp, 0xe8
006B64C9  F6 05 70 B3 B4 00 01            test byte ptr [rip + 0xb4b370], 1
006B64D0  74 05                           je 0x1406b64d7
006B64D2  E9 A9 66 51 00                  jmp 0x140bccb80
006B64D7  66 65 F7 04 25 58 08 00 00 00 02  test word ptr gs:[0x858], 0x200
006B64E2  74 05                           je 0x1406b64e9
006B64E4  0F 00 6C 24 20                  verw word ptr [rsp + 0x20]
006B64E9  0F 01 F8                        swapgs
006B64EC  48 CF                           iretq
006B64EE  0F AE 55 AC                     ldmxcsr dword ptr [rbp - 0x54]
006B64F2  0F 28 45 F0                     movaps xmm0, xmmword ptr [rbp - 0x10]
006B64F6  0F 28 4D 00                     movaps xmm1, xmmword ptr [rbp]
006B64FA  0F 28 55 10                     movaps xmm2, xmmword ptr [rbp + 0x10]
006B64FE  0F 28 5D 20                     movaps xmm3, xmmword ptr [rbp + 0x20]
006B6502  0F 28 65 30                     movaps xmm4, xmmword ptr [rbp + 0x30]
006B6506  0F 28 6D 40                     movaps xmm5, xmmword ptr [rbp + 0x40]
006B650A  4C 8B 5D E0                     mov r11, qword ptr [rbp - 0x20]
006B650E  4C 8B 55 D8                     mov r10, qword ptr [rbp - 0x28]
006B6512  4C 8B 4D D0                     mov r9, qword ptr [rbp - 0x30]
006B6516  4C 8B 45 C8                     mov r8, qword ptr [rbp - 0x38]
006B651A  48 8B 55 C0                     mov rdx, qword ptr [rbp - 0x40]
006B651E  48 8B 4D B8                     mov rcx, qword ptr [rbp - 0x48]
006B6522  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
006B6526  48 8B E5                        mov rsp, rbp
006B6529  48 8B AD D8 00 00 00            mov rbp, qword ptr [rbp + 0xd8]
006B6530  48 81 C4 E8 00 00 00            add rsp, 0xe8
006B6537  48 CF                           iretq
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiApcInterrupt(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
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
    if (((v_stack_p8) & (1)) != 0) goto loc_006B5E96;
    a2 = 0;
    v_stack_m90 = 0;
    if (((*(unsigned __int8 *)(gs_base + (0 + 2136))) & (1)) != 0) goto loc_006B5E7F;
    goto loc_006B6107;
loc_006B5E7F:
    a2 = 0;
    goto loc_006B6107;
loc_006B5E96:
    if (((*(unsigned __int8 *)(v_rip + 11844003)) & (1)) == 0) {
    }
    if (*(unsigned __int64 *)(gs_base + (0 + 40232)) == 0) goto loc_006B5ED2;
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
    if ((((unsigned int)(a2)) & (2)) == 0) goto loc_006B60AE;
    result = KiApcInterrupt___0x26A(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiApcInterrupt___0x273(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiApcInterrupt___0x15C(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiApcInterrupt___0x165(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiApcInterrupt___0x16E(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiApcInterrupt___0x177(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiApcInterrupt___0x180(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiApcInterrupt___0x189(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiApcInterrupt___0x192(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiApcInterrupt___0x19B(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiApcInterrupt___0x1A4(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiApcInterrupt___0x1AD(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiApcInterrupt___0x1B6(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiApcInterrupt___0x1BF(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiApcInterrupt___0x1C8(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiApcInterrupt___0x1D1(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiApcInterrupt___0x1DA(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiApcInterrupt___0x1E3(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiApcInterrupt___0x1EC(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiApcInterrupt___0x1F5(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiApcInterrupt___0x1FE(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiApcInterrupt___0x207(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiApcInterrupt___0x210(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiApcInterrupt___0x219(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiApcInterrupt___0x222(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiApcInterrupt___0x22B(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiApcInterrupt___0x234(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiApcInterrupt___0x23D(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiApcInterrupt___0x246(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiApcInterrupt___0x24F(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiApcInterrupt___0x258(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiApcInterrupt___0x261(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = (unsigned int)(0xDADAULL);
    if (((*(unsigned __int8 *)(gs_base + (0 + 2140))) & (8)) != 0) {
        result = 32;
    }
    if ((((unsigned int)(a2)) & (128)) != 0) {
        result = KiFlushBhbDuringTrapEntryOrExit(a1, a2, a3, a4);
    }
    *(unsigned __int8 *)(gs_base + (0 + 2142)) = 0;
    if ((*(unsigned int *)(v_rip + 9507219)) == 0) goto loc_006B60F2;
    if (((unsigned int)(a2)) == 0) goto loc_006B60F2;
    a2 = (unsigned int)((a2) & (*(unsigned int *)(v_rip + 9507197)));
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
    if (((*(unsigned __int8 *)(v_rip + 9505444)) & (255)) == 0) goto loc_006B615A;
    if (((v_stack_p8) & (1)) != 0) {
    }
    if (((*(unsigned __int8 *)(v_rip + 9505380)) & (1)) == 0) goto loc_006B6187;
    if ((*(unsigned int *)(gs_base + (0 + 552))) != 0) goto loc_006B6187;
    if ((*(unsigned int *)(gs_base + (0 + 552))) < 0) {
    }
    if ((*(unsigned int *)(v_rip + 9505677)) == 0) goto loc_006B619C;
    result = KzSetIrqlUnsafe(1, a2, a3, a4);
    goto loc_006B61A4;
loc_006B619C:
loc_006B61A4:
    v_stack_m13F = (unsigned __int8)(v_cr8);
    result = HalPerformEndOfInterrupt(0, a2, a3, a4);
    if ((*(unsigned __int8 *)(gs_base + (0 + 391))) == 0) {
        a1 = 0;
        a2 = 0;
        a3 = v_stack_m168;
        result = KiDeliverApc(a1, a2, a3, a4);
    }
    if ((*(unsigned int *)(v_rip + 9505609)) == 0) goto loc_006B61E0;
    result = KzSetIrqlUnsafe(v_stack_m13F, a2, a3, a4);
    goto loc_006B61E4;
loc_006B61E0:
loc_006B61E4:
    if (((v_stack_p8) & (1)) == 0) goto loc_006B64EE;
    if (((*(unsigned __int8 *)(v_rip + 9505264)) & (255)) != 0) {
    }
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 194)) & (3)) == 0) goto loc_006B6232;
    result = KiInitiateUserApc(1, a2, a3, a4);
    goto loc_006B6205;
loc_006B6232:
    result = KiSynchronizeUserIsolationDomainEntry(0, a2, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_006B6205;
    result = v_stack_m138;
    if (((*(unsigned __int8 *)(gs_base + (0 + 2144))) & (2)) != 0) {
        a1 = 0;
        result = KiUpdateStibpPairing(a1, a2, a3, a4);
    }
    if (((*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)))) & (0x8000000ULL)) != 0) {
        result = KiRestoreSetContextState(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, a4);
    }
    if (((*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)))) & (0x10000ULL)) == 0) goto loc_006B628C;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 2)) & (1)) != 0) {
        result = KiCopyCounters(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, a4);
        a1 = *(unsigned __int64 *)(gs_base + (0 + 392));
    }
    if (v_stack_m68 != 0) {
        result = KiRestoreDebugRegisterState(a1, a2, a3, a4);
    }
    if (v_stack_m68 >= 0) goto loc_006B62D9;
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
    if (condition_is_above_or_equal) goto loc_006B646B;
    result = KiApcInterrupt___0x627(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiApcInterrupt___0x630(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiApcInterrupt___0x519(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiApcInterrupt___0x522(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiApcInterrupt___0x52B(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiApcInterrupt___0x534(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiApcInterrupt___0x53D(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiApcInterrupt___0x546(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiApcInterrupt___0x54F(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiApcInterrupt___0x558(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiApcInterrupt___0x561(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiApcInterrupt___0x56A(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiApcInterrupt___0x573(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiApcInterrupt___0x57C(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiApcInterrupt___0x585(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiApcInterrupt___0x58E(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiApcInterrupt___0x597(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiApcInterrupt___0x5A0(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiApcInterrupt___0x5A9(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiApcInterrupt___0x5B2(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiApcInterrupt___0x5BB(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiApcInterrupt___0x5C4(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiApcInterrupt___0x5CD(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiApcInterrupt___0x5D6(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiApcInterrupt___0x5DF(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiApcInterrupt___0x5E8(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiApcInterrupt___0x5F1(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiApcInterrupt___0x5FA(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiApcInterrupt___0x603(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiApcInterrupt___0x60C(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiApcInterrupt___0x615(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiApcInterrupt___0x61E(a1, a2, a3, a4);
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
    if (((*(unsigned __int8 *)(v_rip + 11842416)) & (1)) == 0) goto loc_006B64D7;
loc_006B64D7:
    if (((*(unsigned __int16 *)(gs_base + (0 + 2136))) & (512)) != 0) {
    }
loc_006B64EE:
    v_rsp = (v_stack_m10) + (232);
    return v_stack_m138;
}
```

## 5. (Beta) C Style

```c
int64_t KiApcInterrupt(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
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
    if (((v_stack_p8) & (1)) != 0) goto loc_006B5E96;
    Arg2 = 0;
    v_stack_m90 = 0;
    if (((*(uint8_t *)(gs_base + (0 + 0x858))) & (1)) != 0) goto loc_006B5E7F;
    goto loc_006B6107;
loc_006B5E7F:
    Arg2 = 0;
    goto loc_006B6107;
loc_006B5E96:
    if (((*(uint8_t *)(v_rip + 0xB4B9A3)) & (1)) == 0) {
    }
    if (*(uint64_t *)(gs_base + (0 + 0x9D28)) == 0) goto loc_006B5ED2;
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
    if ((((uint32_t)(Arg2)) & (2)) == 0) goto loc_006B60AE;
    result = KiApcInterrupt___0x26A(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiApcInterrupt___0x273(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiApcInterrupt___0x15C(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiApcInterrupt___0x165(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiApcInterrupt___0x16E(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiApcInterrupt___0x177(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiApcInterrupt___0x180(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiApcInterrupt___0x189(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiApcInterrupt___0x192(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiApcInterrupt___0x19B(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiApcInterrupt___0x1A4(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiApcInterrupt___0x1AD(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiApcInterrupt___0x1B6(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiApcInterrupt___0x1BF(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiApcInterrupt___0x1C8(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiApcInterrupt___0x1D1(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiApcInterrupt___0x1DA(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiApcInterrupt___0x1E3(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiApcInterrupt___0x1EC(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiApcInterrupt___0x1F5(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiApcInterrupt___0x1FE(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiApcInterrupt___0x207(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiApcInterrupt___0x210(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiApcInterrupt___0x219(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiApcInterrupt___0x222(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiApcInterrupt___0x22B(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiApcInterrupt___0x234(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiApcInterrupt___0x23D(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiApcInterrupt___0x246(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiApcInterrupt___0x24F(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiApcInterrupt___0x258(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiApcInterrupt___0x261(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = (uint32_t)(0xDADAULL);
    if (((*(uint8_t *)(gs_base + (0 + 0x85C))) & (8)) != 0) {
        result = 32;
    }
    if ((((uint32_t)(Arg2)) & (128)) != 0) {
        result = KiFlushBhbDuringTrapEntryOrExit(Arg1, Arg2, Arg3, Arg4);
    }
    *(uint8_t *)(gs_base + (0 + 0x85E)) = 0;
    if ((*(uint32_t *)(v_rip + 0x911193)) == 0) goto loc_006B60F2;
    if (((uint32_t)(Arg2)) == 0) goto loc_006B60F2;
    Arg2 = (uint32_t)((Arg2) & (*(uint32_t *)(v_rip + 0x91117D)));
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
    if (((*(uint8_t *)(v_rip + 0x910AA4)) & (255)) == 0) goto loc_006B615A;
    if (((v_stack_p8) & (1)) != 0) {
    }
    if (((*(uint8_t *)(v_rip + 0x910A64)) & (1)) == 0) goto loc_006B6187;
    if ((*(uint32_t *)(gs_base + (0 + 0x228))) != 0) goto loc_006B6187;
    if ((*(uint32_t *)(gs_base + (0 + 0x228))) < 0) {
    }
    if ((*(uint32_t *)(v_rip + 0x910B8D)) == 0) goto loc_006B619C;
    result = KzSetIrqlUnsafe(1, Arg2, Arg3, Arg4);
    goto loc_006B61A4;
loc_006B619C:
loc_006B61A4:
    v_stack_m13F = (uint8_t)(v_cr8);
    result = HalPerformEndOfInterrupt(0, Arg2, Arg3, Arg4);
    if ((*(uint8_t *)(gs_base + (0 + 0x187))) == 0) {
        Arg1 = 0;
        Arg2 = 0;
        Arg3 = v_stack_m168;
        result = KiDeliverApc(Arg1, Arg2, Arg3, Arg4);
    }
    if ((*(uint32_t *)(v_rip + 0x910B49)) == 0) goto loc_006B61E0;
    result = KzSetIrqlUnsafe(v_stack_m13F, Arg2, Arg3, Arg4);
    goto loc_006B61E4;
loc_006B61E0:
loc_006B61E4:
    if (((v_stack_p8) & (1)) == 0) goto loc_006B64EE;
    if (((*(uint8_t *)(v_rip + 0x9109F0)) & (255)) != 0) {
    }
    if (((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xC2)) & (3)) == 0) goto loc_006B6232;
    result = KiInitiateUserApc(1, Arg2, Arg3, Arg4);
    goto loc_006B6205;
loc_006B6232:
    result = KiSynchronizeUserIsolationDomainEntry(0, Arg2, Arg3, Arg4);
    if ((uint32_t)(result) != 0) goto loc_006B6205;
    result = v_stack_m138;
    if (((*(uint8_t *)(gs_base + (0 + 0x860))) & (2)) != 0) {
        Arg1 = 0;
        result = KiUpdateStibpPairing(Arg1, Arg2, Arg3, Arg4);
    }
    if (((*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)))) & (0x8000000ULL)) != 0) {
        result = KiRestoreSetContextState(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, Arg3, Arg4);
    }
    if (((*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)))) & (0x10000ULL)) == 0) goto loc_006B628C;
    if (((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x2)) & (1)) != 0) {
        result = KiCopyCounters(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, Arg3, Arg4);
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x188));
    }
    if (v_stack_m68 != 0) {
        result = KiRestoreDebugRegisterState(Arg1, Arg2, Arg3, Arg4);
    }
    if (v_stack_m68 >= 0) goto loc_006B62D9;
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
    if (condition_is_above_or_equal) goto loc_006B646B;
    result = KiApcInterrupt___0x627(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiApcInterrupt___0x630(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiApcInterrupt___0x519(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiApcInterrupt___0x522(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiApcInterrupt___0x52B(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiApcInterrupt___0x534(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiApcInterrupt___0x53D(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiApcInterrupt___0x546(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiApcInterrupt___0x54F(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiApcInterrupt___0x558(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiApcInterrupt___0x561(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiApcInterrupt___0x56A(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiApcInterrupt___0x573(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiApcInterrupt___0x57C(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiApcInterrupt___0x585(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiApcInterrupt___0x58E(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiApcInterrupt___0x597(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiApcInterrupt___0x5A0(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiApcInterrupt___0x5A9(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiApcInterrupt___0x5B2(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiApcInterrupt___0x5BB(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiApcInterrupt___0x5C4(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiApcInterrupt___0x5CD(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiApcInterrupt___0x5D6(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiApcInterrupt___0x5DF(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiApcInterrupt___0x5E8(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiApcInterrupt___0x5F1(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiApcInterrupt___0x5FA(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiApcInterrupt___0x603(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiApcInterrupt___0x60C(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiApcInterrupt___0x615(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiApcInterrupt___0x61E(Arg1, Arg2, Arg3, Arg4);
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
    if (((*(uint8_t *)(v_rip + 0xB4B370)) & (1)) == 0) goto loc_006B64D7;
loc_006B64D7:
    if (((*(uint16_t *)(gs_base + (0 + 0x858))) & (512)) != 0) {
    }
loc_006B64EE:
    local_rsp = (v_stack_m10) + (232);
    return v_stack_m138;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006B5E20&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
