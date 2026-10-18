# KiSwInterrupt

- RVA: `0x006B8070`–`0x006B87A5` (길이 `1,845` bytes)
- VA: `0x00000001406B8070`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C228C`
- 디코드: `402`개 명령, `1,845/1,845` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **82**; 고유 호출 대상: **81**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x006B81C7` → [KiSwInterrupt + 0x26A](KiSwInterrupt_function_006B8070.md) (inside-function, `0x006B82DA`)
- `0x006B81D0` → [KiSwInterrupt + 0x273](KiSwInterrupt_function_006B8070.md) (inside-function, `0x006B82E3`)
- `0x006B81D9` → [KiSwInterrupt + 0x15C](KiSwInterrupt_function_006B8070.md) (inside-function, `0x006B81CC`)
- `0x006B81E2` → [KiSwInterrupt + 0x165](KiSwInterrupt_function_006B8070.md) (inside-function, `0x006B81D5`)
- `0x006B81EB` → [KiSwInterrupt + 0x16E](KiSwInterrupt_function_006B8070.md) (inside-function, `0x006B81DE`)
- `0x006B81F4` → [KiSwInterrupt + 0x177](KiSwInterrupt_function_006B8070.md) (inside-function, `0x006B81E7`)
- `0x006B81FD` → [KiSwInterrupt + 0x180](KiSwInterrupt_function_006B8070.md) (inside-function, `0x006B81F0`)
- `0x006B8206` → [KiSwInterrupt + 0x189](KiSwInterrupt_function_006B8070.md) (inside-function, `0x006B81F9`)
- `0x006B820F` → [KiSwInterrupt + 0x192](KiSwInterrupt_function_006B8070.md) (inside-function, `0x006B8202`)
- `0x006B8218` → [KiSwInterrupt + 0x19B](KiSwInterrupt_function_006B8070.md) (inside-function, `0x006B820B`)
- `0x006B8221` → [KiSwInterrupt + 0x1A4](KiSwInterrupt_function_006B8070.md) (inside-function, `0x006B8214`)
- `0x006B822A` → [KiSwInterrupt + 0x1AD](KiSwInterrupt_function_006B8070.md) (inside-function, `0x006B821D`)
- `0x006B8233` → [KiSwInterrupt + 0x1B6](KiSwInterrupt_function_006B8070.md) (inside-function, `0x006B8226`)
- `0x006B823C` → [KiSwInterrupt + 0x1BF](KiSwInterrupt_function_006B8070.md) (inside-function, `0x006B822F`)
- `0x006B8245` → [KiSwInterrupt + 0x1C8](KiSwInterrupt_function_006B8070.md) (inside-function, `0x006B8238`)
- `0x006B824E` → [KiSwInterrupt + 0x1D1](KiSwInterrupt_function_006B8070.md) (inside-function, `0x006B8241`)
- `0x006B8257` → [KiSwInterrupt + 0x1DA](KiSwInterrupt_function_006B8070.md) (inside-function, `0x006B824A`)
- `0x006B8260` → [KiSwInterrupt + 0x1E3](KiSwInterrupt_function_006B8070.md) (inside-function, `0x006B8253`)
- `0x006B8269` → [KiSwInterrupt + 0x1EC](KiSwInterrupt_function_006B8070.md) (inside-function, `0x006B825C`)
- `0x006B8272` → [KiSwInterrupt + 0x1F5](KiSwInterrupt_function_006B8070.md) (inside-function, `0x006B8265`)
- `0x006B827B` → [KiSwInterrupt + 0x1FE](KiSwInterrupt_function_006B8070.md) (inside-function, `0x006B826E`)
- `0x006B8284` → [KiSwInterrupt + 0x207](KiSwInterrupt_function_006B8070.md) (inside-function, `0x006B8277`)
- `0x006B828D` → [KiSwInterrupt + 0x210](KiSwInterrupt_function_006B8070.md) (inside-function, `0x006B8280`)
- `0x006B8296` → [KiSwInterrupt + 0x219](KiSwInterrupt_function_006B8070.md) (inside-function, `0x006B8289`)
- `0x006B829F` → [KiSwInterrupt + 0x222](KiSwInterrupt_function_006B8070.md) (inside-function, `0x006B8292`)
- `0x006B82A8` → [KiSwInterrupt + 0x22B](KiSwInterrupt_function_006B8070.md) (inside-function, `0x006B829B`)
- `0x006B82B1` → [KiSwInterrupt + 0x234](KiSwInterrupt_function_006B8070.md) (inside-function, `0x006B82A4`)
- `0x006B82BA` → [KiSwInterrupt + 0x23D](KiSwInterrupt_function_006B8070.md) (inside-function, `0x006B82AD`)
- `0x006B82C3` → [KiSwInterrupt + 0x246](KiSwInterrupt_function_006B8070.md) (inside-function, `0x006B82B6`)
- `0x006B82CC` → [KiSwInterrupt + 0x24F](KiSwInterrupt_function_006B8070.md) (inside-function, `0x006B82BF`)
- `0x006B82D5` → [KiSwInterrupt + 0x258](KiSwInterrupt_function_006B8070.md) (inside-function, `0x006B82C8`)
- `0x006B82DE` → [KiSwInterrupt + 0x261](KiSwInterrupt_function_006B8070.md) (inside-function, `0x006B82D1`)
- `0x006B8309` → [KiFlushBhbDuringTrapEntryOrExit](../6C/KiFlushBhbDuringTrapEntryOrExit_function_006C6340.md) (function, `0x006C6340`)
- `0x006B8352` → [KiSaveDebugRegisterState](../4F/KiSaveDebugRegisterState_function_004FD960.md) (function, `0x004FD960`)
- `0x006B8386` → [KiSynchronizeUserIsolationDomainExit](../41/KiSynchronizeUserIsolationDomainExit_function_0041BFA0.md) (function, `0x0041BFA0`)
- `0x006B8396` → [KeWakeProcessor](../5B/KeWakeProcessor_function_005BE080.md) (function, `0x005BE080`)
- `0x006B83BF` → [KiCheckForSListAddress](../40/KiCheckForSListAddress_function_0040B810.md) (function, `0x0040B810`)
- `0x006B83E8` → [KzSetIrqlUnsafe](../5B/KzSetIrqlUnsafe_function_005B8AE0.md) (function, `0x005B8AE0`)
- `0x006B8405` → [KiStartInterruptCycleAccumulation](../37/KiStartInterruptCycleAccumulation_function_0037B410.md) (function, `0x0037B410`)
- `0x006B840F` → [KiSwInterruptDispatch](../50/KiSwInterruptDispatch_function_0050A5C0.md) (function, `0x0050A5C0`)
- `0x006B8418` → [HalPerformEndOfInterrupt](../41/HalPerformEndOfInterrupt_function_00418E20.md) (function, `0x00418E20`)
- `0x006B842A` → [KiEndInterruptCycleAccumulation](../3F/KiEndInterruptCycleAccumulation_function_003FAAE0.md) (function, `0x003FAAE0`)
- `0x006B8433` → [KiDpcInterruptBypass](KiDpcInterruptBypass_function_006B8EE0.md) (function, `0x006B8EE0`)
- `0x006B8445` → [KzSetIrqlUnsafe](../5B/KzSetIrqlUnsafe_function_005B8AE0.md) (function, `0x005B8AE0`)
- `0x006B848D` → [KiInitiateUserApc](KiInitiateUserApc_function_006B6540.md) (function, `0x006B6540`)
- `0x006B849E` → [KiSynchronizeUserIsolationDomainEntry](../26/KiSynchronizeUserIsolationDomainEntry_function_00263F60.md) (function, `0x00263F60`)
- `0x006B84B8` → [KiUpdateStibpPairing](../3E/KiUpdateStibpPairing_function_003E71C0.md) (function, `0x003E71C0`)
- `0x006B84CE` → [KiRestoreSetContextState](KiRestoreSetContextState_function_006B1CA0.md) (function, `0x006B1CA0`)
- `0x006B84EA` → [KiCopyCounters](../5C/KiCopyCounters_function_005C0710.md) (function, `0x005C0710`)
- `0x006B8506` → [KiRestoreDebugRegisterState](../4F/KiRestoreDebugRegisterState_function_004FD8E0.md) (function, `0x004FD8E0`)
- `0x006B85A0` → [KiSwInterrupt + 0x643](KiSwInterrupt_function_006B8070.md) (inside-function, `0x006B86B3`)
- `0x006B85A9` → [KiSwInterrupt + 0x64C](KiSwInterrupt_function_006B8070.md) (inside-function, `0x006B86BC`)
- `0x006B85B2` → [KiSwInterrupt + 0x535](KiSwInterrupt_function_006B8070.md) (inside-function, `0x006B85A5`)
- `0x006B85BB` → [KiSwInterrupt + 0x53E](KiSwInterrupt_function_006B8070.md) (inside-function, `0x006B85AE`)
- `0x006B85C4` → [KiSwInterrupt + 0x547](KiSwInterrupt_function_006B8070.md) (inside-function, `0x006B85B7`)
- `0x006B85CD` → [KiSwInterrupt + 0x550](KiSwInterrupt_function_006B8070.md) (inside-function, `0x006B85C0`)
- `0x006B85D6` → [KiSwInterrupt + 0x559](KiSwInterrupt_function_006B8070.md) (inside-function, `0x006B85C9`)
- `0x006B85DF` → [KiSwInterrupt + 0x562](KiSwInterrupt_function_006B8070.md) (inside-function, `0x006B85D2`)
- `0x006B85E8` → [KiSwInterrupt + 0x56B](KiSwInterrupt_function_006B8070.md) (inside-function, `0x006B85DB`)
- `0x006B85F1` → [KiSwInterrupt + 0x574](KiSwInterrupt_function_006B8070.md) (inside-function, `0x006B85E4`)
- `0x006B85FA` → [KiSwInterrupt + 0x57D](KiSwInterrupt_function_006B8070.md) (inside-function, `0x006B85ED`)
- `0x006B8603` → [KiSwInterrupt + 0x586](KiSwInterrupt_function_006B8070.md) (inside-function, `0x006B85F6`)
- `0x006B860C` → [KiSwInterrupt + 0x58F](KiSwInterrupt_function_006B8070.md) (inside-function, `0x006B85FF`)
- `0x006B8615` → [KiSwInterrupt + 0x598](KiSwInterrupt_function_006B8070.md) (inside-function, `0x006B8608`)
- `0x006B861E` → [KiSwInterrupt + 0x5A1](KiSwInterrupt_function_006B8070.md) (inside-function, `0x006B8611`)
- `0x006B8627` → [KiSwInterrupt + 0x5AA](KiSwInterrupt_function_006B8070.md) (inside-function, `0x006B861A`)
- `0x006B8630` → [KiSwInterrupt + 0x5B3](KiSwInterrupt_function_006B8070.md) (inside-function, `0x006B8623`)
- `0x006B8639` → [KiSwInterrupt + 0x5BC](KiSwInterrupt_function_006B8070.md) (inside-function, `0x006B862C`)
- `0x006B8642` → [KiSwInterrupt + 0x5C5](KiSwInterrupt_function_006B8070.md) (inside-function, `0x006B8635`)
- `0x006B864B` → [KiSwInterrupt + 0x5CE](KiSwInterrupt_function_006B8070.md) (inside-function, `0x006B863E`)
- `0x006B8654` → [KiSwInterrupt + 0x5D7](KiSwInterrupt_function_006B8070.md) (inside-function, `0x006B8647`)
- `0x006B865D` → [KiSwInterrupt + 0x5E0](KiSwInterrupt_function_006B8070.md) (inside-function, `0x006B8650`)
- `0x006B8666` → [KiSwInterrupt + 0x5E9](KiSwInterrupt_function_006B8070.md) (inside-function, `0x006B8659`)
- `0x006B866F` → [KiSwInterrupt + 0x5F2](KiSwInterrupt_function_006B8070.md) (inside-function, `0x006B8662`)
- `0x006B8678` → [KiSwInterrupt + 0x5FB](KiSwInterrupt_function_006B8070.md) (inside-function, `0x006B866B`)
- `0x006B8681` → [KiSwInterrupt + 0x604](KiSwInterrupt_function_006B8070.md) (inside-function, `0x006B8674`)
- `0x006B868A` → [KiSwInterrupt + 0x60D](KiSwInterrupt_function_006B8070.md) (inside-function, `0x006B867D`)
- `0x006B8693` → [KiSwInterrupt + 0x616](KiSwInterrupt_function_006B8070.md) (inside-function, `0x006B8686`)
- `0x006B869C` → [KiSwInterrupt + 0x61F](KiSwInterrupt_function_006B8070.md) (inside-function, `0x006B868F`)
- `0x006B86A5` → [KiSwInterrupt + 0x628](KiSwInterrupt_function_006B8070.md) (inside-function, `0x006B8698`)
- `0x006B86AE` → [KiSwInterrupt + 0x631](KiSwInterrupt_function_006B8070.md) (inside-function, `0x006B86A1`)
- `0x006B86B7` → [KiSwInterrupt + 0x63A](KiSwInterrupt_function_006B8070.md) (inside-function, `0x006B86AA`)

### Direct callers
- [KiSwInterrupt](KiSwInterrupt_function_006B8070.md) at `0x006B81C7`
- [KiSwInterrupt](KiSwInterrupt_function_006B8070.md) at `0x006B81D0`
- [KiSwInterrupt](KiSwInterrupt_function_006B8070.md) at `0x006B81D9`
- [KiSwInterrupt](KiSwInterrupt_function_006B8070.md) at `0x006B81E2`
- [KiSwInterrupt](KiSwInterrupt_function_006B8070.md) at `0x006B81EB`
- [KiSwInterrupt](KiSwInterrupt_function_006B8070.md) at `0x006B81F4`
- [KiSwInterrupt](KiSwInterrupt_function_006B8070.md) at `0x006B81FD`
- [KiSwInterrupt](KiSwInterrupt_function_006B8070.md) at `0x006B8206`
- [KiSwInterrupt](KiSwInterrupt_function_006B8070.md) at `0x006B820F`
- [KiSwInterrupt](KiSwInterrupt_function_006B8070.md) at `0x006B8218`
- [KiSwInterrupt](KiSwInterrupt_function_006B8070.md) at `0x006B8221`
- [KiSwInterrupt](KiSwInterrupt_function_006B8070.md) at `0x006B822A`
- [KiSwInterrupt](KiSwInterrupt_function_006B8070.md) at `0x006B8233`
- [KiSwInterrupt](KiSwInterrupt_function_006B8070.md) at `0x006B823C`
- [KiSwInterrupt](KiSwInterrupt_function_006B8070.md) at `0x006B8245`
- [KiSwInterrupt](KiSwInterrupt_function_006B8070.md) at `0x006B824E`
- [KiSwInterrupt](KiSwInterrupt_function_006B8070.md) at `0x006B8257`
- [KiSwInterrupt](KiSwInterrupt_function_006B8070.md) at `0x006B8260`
- [KiSwInterrupt](KiSwInterrupt_function_006B8070.md) at `0x006B8269`
- [KiSwInterrupt](KiSwInterrupt_function_006B8070.md) at `0x006B8272`
- [KiSwInterrupt](KiSwInterrupt_function_006B8070.md) at `0x006B827B`
- [KiSwInterrupt](KiSwInterrupt_function_006B8070.md) at `0x006B8284`
- [KiSwInterrupt](KiSwInterrupt_function_006B8070.md) at `0x006B828D`
- [KiSwInterrupt](KiSwInterrupt_function_006B8070.md) at `0x006B8296`
- [KiSwInterrupt](KiSwInterrupt_function_006B8070.md) at `0x006B829F`
- [KiSwInterrupt](KiSwInterrupt_function_006B8070.md) at `0x006B82A8`
- [KiSwInterrupt](KiSwInterrupt_function_006B8070.md) at `0x006B82B1`
- [KiSwInterrupt](KiSwInterrupt_function_006B8070.md) at `0x006B82BA`
- [KiSwInterrupt](KiSwInterrupt_function_006B8070.md) at `0x006B82C3`
- [KiSwInterrupt](KiSwInterrupt_function_006B8070.md) at `0x006B82CC`
- [KiSwInterrupt](KiSwInterrupt_function_006B8070.md) at `0x006B82D5`
- [KiSwInterrupt](KiSwInterrupt_function_006B8070.md) at `0x006B82DE`
- [KiSwInterrupt](KiSwInterrupt_function_006B8070.md) at `0x006B85A0`
- [KiSwInterrupt](KiSwInterrupt_function_006B8070.md) at `0x006B85A9`
- [KiSwInterrupt](KiSwInterrupt_function_006B8070.md) at `0x006B85B2`
- [KiSwInterrupt](KiSwInterrupt_function_006B8070.md) at `0x006B85BB`
- [KiSwInterrupt](KiSwInterrupt_function_006B8070.md) at `0x006B85C4`
- [KiSwInterrupt](KiSwInterrupt_function_006B8070.md) at `0x006B85CD`
- [KiSwInterrupt](KiSwInterrupt_function_006B8070.md) at `0x006B85D6`
- [KiSwInterrupt](KiSwInterrupt_function_006B8070.md) at `0x006B85DF`
- [KiSwInterrupt](KiSwInterrupt_function_006B8070.md) at `0x006B85E8`
- [KiSwInterrupt](KiSwInterrupt_function_006B8070.md) at `0x006B85F1`
- [KiSwInterrupt](KiSwInterrupt_function_006B8070.md) at `0x006B85FA`
- [KiSwInterrupt](KiSwInterrupt_function_006B8070.md) at `0x006B8603`
- [KiSwInterrupt](KiSwInterrupt_function_006B8070.md) at `0x006B860C`
- [KiSwInterrupt](KiSwInterrupt_function_006B8070.md) at `0x006B8615`
- [KiSwInterrupt](KiSwInterrupt_function_006B8070.md) at `0x006B861E`
- [KiSwInterrupt](KiSwInterrupt_function_006B8070.md) at `0x006B8627`
- [KiSwInterrupt](KiSwInterrupt_function_006B8070.md) at `0x006B8630`
- [KiSwInterrupt](KiSwInterrupt_function_006B8070.md) at `0x006B8639`
- [KiSwInterrupt](KiSwInterrupt_function_006B8070.md) at `0x006B8642`
- [KiSwInterrupt](KiSwInterrupt_function_006B8070.md) at `0x006B864B`
- [KiSwInterrupt](KiSwInterrupt_function_006B8070.md) at `0x006B8654`
- [KiSwInterrupt](KiSwInterrupt_function_006B8070.md) at `0x006B865D`
- [KiSwInterrupt](KiSwInterrupt_function_006B8070.md) at `0x006B8666`
- [KiSwInterrupt](KiSwInterrupt_function_006B8070.md) at `0x006B866F`
- [KiSwInterrupt](KiSwInterrupt_function_006B8070.md) at `0x006B8678`
- [KiSwInterrupt](KiSwInterrupt_function_006B8070.md) at `0x006B8681`
- [KiSwInterrupt](KiSwInterrupt_function_006B8070.md) at `0x006B868A`
- [KiSwInterrupt](KiSwInterrupt_function_006B8070.md) at `0x006B8693`
- [KiSwInterrupt](KiSwInterrupt_function_006B8070.md) at `0x006B869C`
- [KiSwInterrupt](KiSwInterrupt_function_006B8070.md) at `0x006B86A5`
- [KiSwInterrupt](KiSwInterrupt_function_006B8070.md) at `0x006B86AE`
- [KiSwInterrupt](KiSwInterrupt_function_006B8070.md) at `0x006B86B7`

### Static image references
- `0x006B80E6` → RVA `0x01201840` (`CFGRO`; read)
- `0x006B831A` → RVA `0x00FC7264` (`ALMOSTRO`; read)
- `0x006B839B` → RVA `0x006BA577` (`ExpInterlockedPopEntrySListResume`; read)
- `0x006B83AB` → RVA `0x006BA590` (`ExpInterlockedPopEntrySListEnd`; read)
- `0x006B83CE` → RVA `0x00FC6BF0` (`ALMOSTRO`; read)
- `0x006B83DF` → RVA `0x00FC6D20` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006B873E` → [KiKernelExit](../../kvascode/BC/KiKernelExit_function_00BCCB80.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006B8070  48 83 EC 08                     sub rsp, 8
006B8074  55                              push rbp
006B8075  56                              push rsi
006B8076  48 81 EC 50 01 00 00            sub rsp, 0x150
006B807D  48 8D AC 24 80 00 00 00         lea rbp, [rsp + 0x80]
006B8085  C6 45 AB 00                     mov byte ptr [rbp - 0x55], 0
006B8089  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
006B808D  48 89 4D B8                     mov qword ptr [rbp - 0x48], rcx
006B8091  48 89 55 C0                     mov qword ptr [rbp - 0x40], rdx
006B8095  4C 89 45 C8                     mov qword ptr [rbp - 0x38], r8
006B8099  4C 89 4D D0                     mov qword ptr [rbp - 0x30], r9
006B809D  4C 89 55 D8                     mov qword ptr [rbp - 0x28], r10
006B80A1  4C 89 5D E0                     mov qword ptr [rbp - 0x20], r11
006B80A5  F6 85 F0 00 00 00 01            test byte ptr [rbp + 0xf0], 1
006B80AC  75 38                           jne 0x1406b80e6
006B80AE  33 D2                           xor edx, edx
006B80B0  F3 48 0F 1E CA                  rdsspq rdx
006B80B5  48 89 55 58                     mov qword ptr [rbp + 0x58], rdx
006B80B9  0F AE E8                        lfence
006B80BC  65 F6 04 25 58 08 00 00 01      test byte ptr gs:[0x858], 1
006B80C5  75 08                           jne 0x1406b80cf
006B80C7  0F AE E8                        lfence
006B80CA  E9 88 02 00 00                  jmp 0x1406b8357
006B80CF  65 0F B7 04 25 66 08 00 00      movzx eax, word ptr gs:[0x866]
006B80D8  B9 48 00 00 00                  mov ecx, 0x48
006B80DD  33 D2                           xor edx, edx
006B80DF  0F 30                           wrmsr
006B80E1  E9 71 02 00 00                  jmp 0x1406b8357
006B80E6  F6 05 53 97 B4 00 01            test byte ptr [rip + 0xb49753], 1
006B80ED  75 03                           jne 0x1406b80f2
006B80EF  0F 01 F8                        swapgs
006B80F2  0F AE E8                        lfence
006B80F5  65 48 8B 0C 25 28 9D 00 00      mov rcx, qword ptr gs:[0x9d28]
006B80FE  48 85 C9                        test rcx, rcx
006B8101  74 1F                           je 0x1406b8122
006B8103  F3 48 0F 1E CA                  rdsspq rdx
006B8108  65 4C 8B 14 25 20 9D 00 00      mov r10, qword ptr gs:[0x9d20]
006B8111  49 83 C2 08                     add r10, 8
006B8115  49 3B D2                        cmp rdx, r10
006B8118  75 08                           jne 0x1406b8122
006B811A  F3 0F 01 29                     rstorssp dword ptr [rcx]
006B811E  F3 0F 01 EA                     saveprevssp
006B8122  65 4C 8B 14 25 88 01 00 00      mov r10, qword ptr gs:[0x188]
006B812B  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006B8134  48 8B 89 20 02 00 00            mov rcx, qword ptr [rcx + 0x220]
006B813B  48 8B 89 60 07 00 00            mov rcx, qword ptr [rcx + 0x760]
006B8142  65 48 89 0C 25 50 08 00 00      mov qword ptr gs:[0x850], rcx
006B814B  66 65 8B 0C 25 62 08 00 00      mov cx, word ptr gs:[0x862]
006B8154  66 65 89 0C 25 64 08 00 00      mov word ptr gs:[0x864], cx
006B815D  65 8A 0C 25 58 08 00 00         mov cl, byte ptr gs:[0x858]
006B8165  65 88 0C 25 5A 08 00 00         mov byte ptr gs:[0x85a], cl
006B816D  65 0F B7 04 25 68 08 00 00      movzx eax, word ptr gs:[0x868]
006B8176  66 65 39 04 25 66 08 00 00      cmp word ptr gs:[0x866], ax
006B817F  74 12                           je 0x1406b8193
006B8181  66 65 89 04 25 66 08 00 00      mov word ptr gs:[0x866], ax
006B818A  B9 48 00 00 00                  mov ecx, 0x48
006B818F  33 D2                           xor edx, edx
006B8191  0F 30                           wrmsr
006B8193  65 0F B6 14 25 58 08 00 00      movzx edx, byte ptr gs:[0x858]
006B819C  F7 C2 08 00 00 00               test edx, 8
006B81A2  74 17                           je 0x1406b81bb
006B81A4  B8 01 00 00 00                  mov eax, 1
006B81A9  33 D2                           xor edx, edx
006B81AB  B9 49 00 00 00                  mov ecx, 0x49
006B81B0  0F 30                           wrmsr
006B81B2  65 0F B6 14 25 58 08 00 00      movzx edx, byte ptr gs:[0x858]
006B81BB  F7 C2 02 00 00 00               test edx, 2
006B81C1  0F 84 37 01 00 00               je 0x1406b82fe
006B81C7  E8 0E 01 00 00                  call 0x1406b82da
006B81CC  48 83 C4 08                     add rsp, 8
006B81D0  E8 0E 01 00 00                  call 0x1406b82e3
006B81D5  48 83 C4 08                     add rsp, 8
006B81D9  E8 EE FF FF FF                  call 0x1406b81cc
006B81DE  48 83 C4 08                     add rsp, 8
006B81E2  E8 EE FF FF FF                  call 0x1406b81d5
006B81E7  48 83 C4 08                     add rsp, 8
006B81EB  E8 EE FF FF FF                  call 0x1406b81de
006B81F0  48 83 C4 08                     add rsp, 8
006B81F4  E8 EE FF FF FF                  call 0x1406b81e7
006B81F9  48 83 C4 08                     add rsp, 8
006B81FD  E8 EE FF FF FF                  call 0x1406b81f0
006B8202  48 83 C4 08                     add rsp, 8
006B8206  E8 EE FF FF FF                  call 0x1406b81f9
006B820B  48 83 C4 08                     add rsp, 8
006B820F  E8 EE FF FF FF                  call 0x1406b8202
006B8214  48 83 C4 08                     add rsp, 8
006B8218  E8 EE FF FF FF                  call 0x1406b820b
006B821D  48 83 C4 08                     add rsp, 8
006B8221  E8 EE FF FF FF                  call 0x1406b8214
006B8226  48 83 C4 08                     add rsp, 8
006B822A  E8 EE FF FF FF                  call 0x1406b821d
006B822F  48 83 C4 08                     add rsp, 8
006B8233  E8 EE FF FF FF                  call 0x1406b8226
006B8238  48 83 C4 08                     add rsp, 8
006B823C  E8 EE FF FF FF                  call 0x1406b822f
006B8241  48 83 C4 08                     add rsp, 8
006B8245  E8 EE FF FF FF                  call 0x1406b8238
006B824A  48 83 C4 08                     add rsp, 8
006B824E  E8 EE FF FF FF                  call 0x1406b8241
006B8253  48 83 C4 08                     add rsp, 8
006B8257  E8 EE FF FF FF                  call 0x1406b824a
006B825C  48 83 C4 08                     add rsp, 8
006B8260  E8 EE FF FF FF                  call 0x1406b8253
006B8265  48 83 C4 08                     add rsp, 8
006B8269  E8 EE FF FF FF                  call 0x1406b825c
006B826E  48 83 C4 08                     add rsp, 8
006B8272  E8 EE FF FF FF                  call 0x1406b8265
006B8277  48 83 C4 08                     add rsp, 8
006B827B  E8 EE FF FF FF                  call 0x1406b826e
006B8280  48 83 C4 08                     add rsp, 8
006B8284  E8 EE FF FF FF                  call 0x1406b8277
006B8289  48 83 C4 08                     add rsp, 8
006B828D  E8 EE FF FF FF                  call 0x1406b8280
006B8292  48 83 C4 08                     add rsp, 8
006B8296  E8 EE FF FF FF                  call 0x1406b8289
006B829B  48 83 C4 08                     add rsp, 8
006B829F  E8 EE FF FF FF                  call 0x1406b8292
006B82A4  48 83 C4 08                     add rsp, 8
006B82A8  E8 EE FF FF FF                  call 0x1406b829b
006B82AD  48 83 C4 08                     add rsp, 8
006B82B1  E8 EE FF FF FF                  call 0x1406b82a4
006B82B6  48 83 C4 08                     add rsp, 8
006B82BA  E8 EE FF FF FF                  call 0x1406b82ad
006B82BF  48 83 C4 08                     add rsp, 8
006B82C3  E8 EE FF FF FF                  call 0x1406b82b6
006B82C8  48 83 C4 08                     add rsp, 8
006B82CC  E8 EE FF FF FF                  call 0x1406b82bf
006B82D1  48 83 C4 08                     add rsp, 8
006B82D5  E8 EE FF FF FF                  call 0x1406b82c8
006B82DA  48 83 C4 08                     add rsp, 8
006B82DE  E8 EE FF FF FF                  call 0x1406b82d1
006B82E3  48 83 C4 08                     add rsp, 8
006B82E7  B8 DA DA 00 00                  mov eax, 0xdada
006B82EC  65 F6 04 25 5C 08 00 00 08      test byte ptr gs:[0x85c], 8
006B82F5  74 07                           je 0x1406b82fe
006B82F7  B0 20                           mov al, 0x20
006B82F9  F3 48 0F AE E8                  incsspq rax
006B82FE  F7 C2 80 00 00 00               test edx, 0x80
006B8304  74 08                           je 0x1406b830e
006B8306  0F AE E8                        lfence
006B8309  E8 32 E0 00 00                  call 0x1406c6340
006B830E  0F AE E8                        lfence
006B8311  65 C6 04 25 5E 08 00 00 00      mov byte ptr gs:[0x85e], 0
006B831A  83 3D 43 EF 90 00 00            cmp dword ptr [rip + 0x90ef43], 0
006B8321  74 1F                           je 0x1406b8342
006B8323  B9 A7 06 00 00                  mov ecx, 0x6a7
006B8328  0F 32                           rdmsr
006B832A  83 FA 00                        cmp edx, 0
006B832D  74 13                           je 0x1406b8342
006B832F  8B CA                           mov ecx, edx
006B8331  23 15 2D EF 90 00               and edx, dword ptr [rip + 0x90ef2d]
006B8337  3B D1                           cmp edx, ecx
006B8339  74 07                           je 0x1406b8342
006B833B  B9 A7 06 00 00                  mov ecx, 0x6a7
006B8340  0F 30                           wrmsr
006B8342  41 F6 42 03 03                  test byte ptr [r10 + 3], 3
006B8347  66 C7 85 80 00 00 00 00 00      mov word ptr [rbp + 0x80], 0
006B8350  74 05                           je 0x1406b8357
006B8352  E8 09 56 E4 FF                  call 0x1404fd960
006B8357  FC                              cld
006B8358  0F AE 5D AC                     stmxcsr dword ptr [rbp - 0x54]
006B835C  65 0F AE 14 25 80 01 00 00      ldmxcsr dword ptr gs:[0x180]
006B8365  0F 29 45 F0                     movaps xmmword ptr [rbp - 0x10], xmm0
006B8369  0F 29 4D 00                     movaps xmmword ptr [rbp], xmm1
006B836D  0F 29 55 10                     movaps xmmword ptr [rbp + 0x10], xmm2
006B8371  0F 29 5D 20                     movaps xmmword ptr [rbp + 0x20], xmm3
006B8375  0F 29 65 30                     movaps xmmword ptr [rbp + 0x30], xmm4
006B8379  0F 29 6D 40                     movaps xmmword ptr [rbp + 0x40], xmm5
006B837D  F6 85 F0 00 00 00 01            test byte ptr [rbp + 0xf0], 1
006B8384  74 05                           je 0x1406b838b
006B8386  E8 15 3C D6 FF                  call 0x14041bfa0
006B838B  65 80 3C 25 DA 87 00 00 00      cmp byte ptr gs:[0x87da], 0
006B8394  74 05                           je 0x1406b839b
006B8396  E8 E5 5C F0 FF                  call 0x1405be080
006B839B  48 8D 05 D5 21 00 00            lea rax, [rip + 0x21d5]
006B83A2  48 3B 85 E8 00 00 00            cmp rax, qword ptr [rbp + 0xe8]
006B83A9  73 19                           jae 0x1406b83c4
006B83AB  48 8D 05 DE 21 00 00            lea rax, [rip + 0x21de]
006B83B2  48 3B 85 E8 00 00 00            cmp rax, qword ptr [rbp + 0xe8]
006B83B9  72 09                           jb 0x1406b83c4
006B83BB  48 8D 4D 80                     lea rcx, [rbp - 0x80]
006B83BF  E8 4C 34 D5 FF                  call 0x14040b810
006B83C4  33 F6                           xor esi, esi
006B83C6  65 FF 04 25 C0 87 00 00         inc dword ptr gs:[0x87c0]
006B83CE  F6 05 1B E8 90 00 FF            test byte ptr [rip + 0x90e81b], 0xff
006B83D5  74 03                           je 0x1406b83da
006B83D7  0F 01 CA                        clac
006B83DA  B9 02 00 00 00                  mov ecx, 2
006B83DF  83 3D 3A E9 90 00 00            cmp dword ptr [rip + 0x90e93a], 0
006B83E6  74 07                           je 0x1406b83ef
006B83E8  E8 F3 06 F0 FF                  call 0x1405b8ae0
006B83ED  EB 08                           jmp 0x1406b83f7
006B83EF  44 0F 20 C0                     mov rax, cr8
006B83F3  44 0F 22 C1                     mov cr8, rcx
006B83F7  88 45 A9                        mov byte ptr [rbp - 0x57], al
006B83FA  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
006B8403  33 D2                           xor edx, edx
006B8405  E8 06 30 CC FF                  call 0x14037b410
006B840A  FB                              sti
006B840B  48 8D 4D 80                     lea rcx, [rbp - 0x80]
006B840F  E8 AC 21 E5 FF                  call 0x14050a5c0
006B8414  FA                              cli
006B8415  48 8B CE                        mov rcx, rsi
006B8418  E8 03 0A D6 FF                  call 0x140418e20
006B841D  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
006B8426  0F B6 55 A9                     movzx edx, byte ptr [rbp - 0x57]
006B842A  E8 B1 26 D4 FF                  call 0x1403faae0
006B842F  84 C0                           test al, al
006B8431  74 05                           je 0x1406b8438
006B8433  E8 A8 0A 00 00                  call 0x1406b8ee0
006B8438  0F B6 4D A9                     movzx ecx, byte ptr [rbp - 0x57]
006B843C  83 3D DD E8 90 00 00            cmp dword ptr [rip + 0x90e8dd], 0
006B8443  74 07                           je 0x1406b844c
006B8445  E8 96 06 F0 FF                  call 0x1405b8ae0
006B844A  EB 04                           jmp 0x1406b8450
006B844C  44 0F 22 C1                     mov cr8, rcx
006B8450  48 8B B5 D0 00 00 00            mov rsi, qword ptr [rbp + 0xd0]
006B8457  FA                              cli
006B8458  F6 85 F0 00 00 00 01            test byte ptr [rbp + 0xf0], 1
006B845F  0F 84 F5 02 00 00               je 0x1406b875a
006B8465  F6 05 84 E7 90 00 FF            test byte ptr [rip + 0x90e784], 0xff
006B846C  74 03                           je 0x1406b8471
006B846E  0F 01 CB                        stac
006B8471  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006B847A  F6 81 C2 00 00 00 03            test byte ptr [rcx + 0xc2], 3
006B8481  74 1B                           je 0x1406b849e
006B8483  B9 01 00 00 00                  mov ecx, 1
006B8488  44 0F 22 C1                     mov cr8, rcx
006B848C  FB                              sti
006B848D  E8 AE E0 FF FF                  call 0x1406b6540
006B8492  FA                              cli
006B8493  B9 00 00 00 00                  mov ecx, 0
006B8498  44 0F 22 C1                     mov cr8, rcx
006B849C  EB D3                           jmp 0x1406b8471
006B849E  E8 BD BA BA FF                  call 0x140263f60
006B84A3  85 C0                           test eax, eax
006B84A5  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
006B84A9  75 C6                           jne 0x1406b8471
006B84AB  65 F6 04 25 60 08 00 00 02      test byte ptr gs:[0x860], 2
006B84B4  74 07                           je 0x1406b84bd
006B84B6  33 C9                           xor ecx, ecx
006B84B8  E8 03 ED D2 FF                  call 0x1403e71c0
006B84BD  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006B84C6  F7 01 00 00 00 08               test dword ptr [rcx], 0x8000000
006B84CC  74 05                           je 0x1406b84d3
006B84CE  E8 CD 97 FF FF                  call 0x1406b1ca0
006B84D3  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006B84DC  F7 01 00 00 01 00               test dword ptr [rcx], 0x10000
006B84E2  74 14                           je 0x1406b84f8
006B84E4  F6 41 02 01                     test byte ptr [rcx + 2], 1
006B84E8  74 0E                           je 0x1406b84f8
006B84EA  E8 21 82 F0 FF                  call 0x1405c0710
006B84EF  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006B84F8  0F AE 55 AC                     ldmxcsr dword ptr [rbp - 0x54]
006B84FC  66 83 BD 80 00 00 00 00         cmp word ptr [rbp + 0x80], 0
006B8504  74 05                           je 0x1406b850b
006B8506  E8 D5 53 E4 FF                  call 0x1404fd8e0
006B850B  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006B8514  0F BA 61 74 16                  bt dword ptr [rcx + 0x74], 0x16
006B8519  73 2A                           jae 0x1406b8545
006B851B  33 C9                           xor ecx, ecx
006B851D  F3 48 0F 1E C9                  rdsspq rcx
006B8522  65 4C 8B 04 25 28 9D 00 00      mov r8, qword ptr gs:[0x9d28]
006B852B  49 83 C0 08                     add r8, 8
006B852F  49 3B C8                        cmp rcx, r8
006B8532  75 11                           jne 0x1406b8545
006B8534  65 48 8B 0C 25 20 9D 00 00      mov rcx, qword ptr gs:[0x9d20]
006B853D  F3 0F 01 29                     rstorssp dword ptr [rcx]
006B8541  F3 0F 01 EA                     saveprevssp
006B8545  65 C6 04 25 5E 08 00 00 00      mov byte ptr gs:[0x85e], 0
006B854E  65 0F B7 04 25 6C 08 00 00      movzx eax, word ptr gs:[0x86c]
006B8557  66 65 39 04 25 66 08 00 00      cmp word ptr gs:[0x866], ax
006B8560  74 12                           je 0x1406b8574
006B8562  66 65 89 04 25 66 08 00 00      mov word ptr gs:[0x866], ax
006B856B  B9 48 00 00 00                  mov ecx, 0x48
006B8570  33 D2                           xor edx, edx
006B8572  0F 30                           wrmsr
006B8574  66 65 0F BA 34 25 58 08 00 00 02  btr word ptr gs:[0x858], 2
006B857F  73 0E                           jae 0x1406b858f
006B8581  B8 01 00 00 00                  mov eax, 1
006B8586  33 D2                           xor edx, edx
006B8588  B9 49 00 00 00                  mov ecx, 0x49
006B858D  0F 30                           wrmsr
006B858F  66 65 0F BA 34 25 58 08 00 00 05  btr word ptr gs:[0x858], 5
006B859A  0F 83 37 01 00 00               jae 0x1406b86d7
006B85A0  E8 0E 01 00 00                  call 0x1406b86b3
006B85A5  48 83 C4 08                     add rsp, 8
006B85A9  E8 0E 01 00 00                  call 0x1406b86bc
006B85AE  48 83 C4 08                     add rsp, 8
006B85B2  E8 EE FF FF FF                  call 0x1406b85a5
006B85B7  48 83 C4 08                     add rsp, 8
006B85BB  E8 EE FF FF FF                  call 0x1406b85ae
006B85C0  48 83 C4 08                     add rsp, 8
006B85C4  E8 EE FF FF FF                  call 0x1406b85b7
006B85C9  48 83 C4 08                     add rsp, 8
006B85CD  E8 EE FF FF FF                  call 0x1406b85c0
006B85D2  48 83 C4 08                     add rsp, 8
006B85D6  E8 EE FF FF FF                  call 0x1406b85c9
006B85DB  48 83 C4 08                     add rsp, 8
006B85DF  E8 EE FF FF FF                  call 0x1406b85d2
006B85E4  48 83 C4 08                     add rsp, 8
006B85E8  E8 EE FF FF FF                  call 0x1406b85db
006B85ED  48 83 C4 08                     add rsp, 8
006B85F1  E8 EE FF FF FF                  call 0x1406b85e4
006B85F6  48 83 C4 08                     add rsp, 8
006B85FA  E8 EE FF FF FF                  call 0x1406b85ed
006B85FF  48 83 C4 08                     add rsp, 8
006B8603  E8 EE FF FF FF                  call 0x1406b85f6
006B8608  48 83 C4 08                     add rsp, 8
006B860C  E8 EE FF FF FF                  call 0x1406b85ff
006B8611  48 83 C4 08                     add rsp, 8
006B8615  E8 EE FF FF FF                  call 0x1406b8608
006B861A  48 83 C4 08                     add rsp, 8
006B861E  E8 EE FF FF FF                  call 0x1406b8611
006B8623  48 83 C4 08                     add rsp, 8
006B8627  E8 EE FF FF FF                  call 0x1406b861a
006B862C  48 83 C4 08                     add rsp, 8
006B8630  E8 EE FF FF FF                  call 0x1406b8623
006B8635  48 83 C4 08                     add rsp, 8
006B8639  E8 EE FF FF FF                  call 0x1406b862c
006B863E  48 83 C4 08                     add rsp, 8
006B8642  E8 EE FF FF FF                  call 0x1406b8635
006B8647  48 83 C4 08                     add rsp, 8
006B864B  E8 EE FF FF FF                  call 0x1406b863e
006B8650  48 83 C4 08                     add rsp, 8
006B8654  E8 EE FF FF FF                  call 0x1406b8647
006B8659  48 83 C4 08                     add rsp, 8
006B865D  E8 EE FF FF FF                  call 0x1406b8650
006B8662  48 83 C4 08                     add rsp, 8
006B8666  E8 EE FF FF FF                  call 0x1406b8659
006B866B  48 83 C4 08                     add rsp, 8
006B866F  E8 EE FF FF FF                  call 0x1406b8662
006B8674  48 83 C4 08                     add rsp, 8
006B8678  E8 EE FF FF FF                  call 0x1406b866b
006B867D  48 83 C4 08                     add rsp, 8
006B8681  E8 EE FF FF FF                  call 0x1406b8674
006B8686  48 83 C4 08                     add rsp, 8
006B868A  E8 EE FF FF FF                  call 0x1406b867d
006B868F  48 83 C4 08                     add rsp, 8
006B8693  E8 EE FF FF FF                  call 0x1406b8686
006B8698  48 83 C4 08                     add rsp, 8
006B869C  E8 EE FF FF FF                  call 0x1406b868f
006B86A1  48 83 C4 08                     add rsp, 8
006B86A5  E8 EE FF FF FF                  call 0x1406b8698
006B86AA  48 83 C4 08                     add rsp, 8
006B86AE  E8 EE FF FF FF                  call 0x1406b86a1
006B86B3  48 83 C4 08                     add rsp, 8
006B86B7  E8 EE FF FF FF                  call 0x1406b86aa
006B86BC  48 83 C4 08                     add rsp, 8
006B86C0  B8 DA DA 00 00                  mov eax, 0xdada
006B86C5  65 F6 04 25 5C 08 00 00 08      test byte ptr gs:[0x85c], 8
006B86CE  74 07                           je 0x1406b86d7
006B86D0  B0 20                           mov al, 0x20
006B86D2  F3 48 0F AE E8                  incsspq rax
006B86D7  66 65 F7 04 25 58 08 00 00 00 01  test word ptr gs:[0x858], 0x100
006B86E2  74 0C                           je 0x1406b86f0
006B86E4  33 C0                           xor eax, eax
006B86E6  33 D2                           xor edx, edx
006B86E8  B9 01 00 00 00                  mov ecx, 1
006B86ED  48 F7 F1                        div rcx
006B86F0  0F 28 45 F0                     movaps xmm0, xmmword ptr [rbp - 0x10]
006B86F4  0F 28 4D 00                     movaps xmm1, xmmword ptr [rbp]
006B86F8  0F 28 55 10                     movaps xmm2, xmmword ptr [rbp + 0x10]
006B86FC  0F 28 5D 20                     movaps xmm3, xmmword ptr [rbp + 0x20]
006B8700  0F 28 65 30                     movaps xmm4, xmmword ptr [rbp + 0x30]
006B8704  0F 28 6D 40                     movaps xmm5, xmmword ptr [rbp + 0x40]
006B8708  4C 8B 5D E0                     mov r11, qword ptr [rbp - 0x20]
006B870C  4C 8B 55 D8                     mov r10, qword ptr [rbp - 0x28]
006B8710  4C 8B 4D D0                     mov r9, qword ptr [rbp - 0x30]
006B8714  4C 8B 45 C8                     mov r8, qword ptr [rbp - 0x38]
006B8718  48 8B 55 C0                     mov rdx, qword ptr [rbp - 0x40]
006B871C  48 8B 4D B8                     mov rcx, qword ptr [rbp - 0x48]
006B8720  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
006B8724  48 8B E5                        mov rsp, rbp
006B8727  48 8B AD D8 00 00 00            mov rbp, qword ptr [rbp + 0xd8]
006B872E  48 81 C4 E8 00 00 00            add rsp, 0xe8
006B8735  F6 05 04 91 B4 00 01            test byte ptr [rip + 0xb49104], 1
006B873C  74 05                           je 0x1406b8743
006B873E  E9 3D 44 51 00                  jmp 0x140bccb80
006B8743  66 65 F7 04 25 58 08 00 00 00 02  test word ptr gs:[0x858], 0x200
006B874E  74 05                           je 0x1406b8755
006B8750  0F 00 6C 24 20                  verw word ptr [rsp + 0x20]
006B8755  0F 01 F8                        swapgs
006B8758  48 CF                           iretq
006B875A  0F AE 55 AC                     ldmxcsr dword ptr [rbp - 0x54]
006B875E  0F 28 45 F0                     movaps xmm0, xmmword ptr [rbp - 0x10]
006B8762  0F 28 4D 00                     movaps xmm1, xmmword ptr [rbp]
006B8766  0F 28 55 10                     movaps xmm2, xmmword ptr [rbp + 0x10]
006B876A  0F 28 5D 20                     movaps xmm3, xmmword ptr [rbp + 0x20]
006B876E  0F 28 65 30                     movaps xmm4, xmmword ptr [rbp + 0x30]
006B8772  0F 28 6D 40                     movaps xmm5, xmmword ptr [rbp + 0x40]
006B8776  4C 8B 5D E0                     mov r11, qword ptr [rbp - 0x20]
006B877A  4C 8B 55 D8                     mov r10, qword ptr [rbp - 0x28]
006B877E  4C 8B 4D D0                     mov r9, qword ptr [rbp - 0x30]
006B8782  4C 8B 45 C8                     mov r8, qword ptr [rbp - 0x38]
006B8786  48 8B 55 C0                     mov rdx, qword ptr [rbp - 0x40]
006B878A  48 8B 4D B8                     mov rcx, qword ptr [rbp - 0x48]
006B878E  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
006B8792  48 8B E5                        mov rsp, rbp
006B8795  48 8B AD D8 00 00 00            mov rbp, qword ptr [rbp + 0xd8]
006B879C  48 81 C4 E8 00 00 00            add rsp, 0xe8
006B87A3  48 CF                           iretq
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiSwInterrupt(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
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
    if (((v_stack_p8) & (1)) != 0) goto loc_006B80E6;
    a2 = 0;
    v_stack_m90 = 0;
    if (((*(unsigned __int8 *)(gs_base + (0 + 2136))) & (1)) != 0) goto loc_006B80CF;
    goto loc_006B8357;
loc_006B80CF:
    a2 = 0;
    goto loc_006B8357;
loc_006B80E6:
    if (((*(unsigned __int8 *)(v_rip + 11835219)) & (1)) == 0) {
    }
    if (*(unsigned __int64 *)(gs_base + (0 + 40232)) == 0) goto loc_006B8122;
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
    if ((((unsigned int)(a2)) & (2)) == 0) goto loc_006B82FE;
    result = KiSwInterrupt___0x26A(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSwInterrupt___0x273(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSwInterrupt___0x15C(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSwInterrupt___0x165(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSwInterrupt___0x16E(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSwInterrupt___0x177(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSwInterrupt___0x180(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSwInterrupt___0x189(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSwInterrupt___0x192(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSwInterrupt___0x19B(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSwInterrupt___0x1A4(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSwInterrupt___0x1AD(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSwInterrupt___0x1B6(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSwInterrupt___0x1BF(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSwInterrupt___0x1C8(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSwInterrupt___0x1D1(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSwInterrupt___0x1DA(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSwInterrupt___0x1E3(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSwInterrupt___0x1EC(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSwInterrupt___0x1F5(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSwInterrupt___0x1FE(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSwInterrupt___0x207(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSwInterrupt___0x210(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSwInterrupt___0x219(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSwInterrupt___0x222(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSwInterrupt___0x22B(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSwInterrupt___0x234(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSwInterrupt___0x23D(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSwInterrupt___0x246(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSwInterrupt___0x24F(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSwInterrupt___0x258(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSwInterrupt___0x261(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = (unsigned int)(0xDADAULL);
    if (((*(unsigned __int8 *)(gs_base + (0 + 2140))) & (8)) != 0) {
        result = 32;
    }
    if ((((unsigned int)(a2)) & (128)) != 0) {
        result = KiFlushBhbDuringTrapEntryOrExit(a1, a2, a3, a4);
    }
    *(unsigned __int8 *)(gs_base + (0 + 2142)) = 0;
    if ((*(unsigned int *)(v_rip + 9498435)) == 0) goto loc_006B8342;
    if (((unsigned int)(a2)) == 0) goto loc_006B8342;
    a2 = (unsigned int)((a2) & (*(unsigned int *)(v_rip + 9498413)));
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
    if ((v_rip + 8661) >= v_stack_p0) goto loc_006B83C4;
    result = v_rip + 8670;
    if ((v_rip + 8670) >= v_stack_p0) {
        a1 = v_stack_m168;
        result = KiCheckForSListAddress(a1, a2, a3, a4);
    }
    v_rsi = 0;
    if (((*(unsigned __int8 *)(v_rip + 9496603)) & (255)) != 0) {
    }
    if ((*(unsigned int *)(v_rip + 9496890)) == 0) goto loc_006B83EF;
    result = KzSetIrqlUnsafe(2, a2, a3, a4);
    goto loc_006B83F7;
loc_006B83EF:
loc_006B83F7:
    v_stack_m13F = (unsigned __int8)(v_cr8);
    a2 = 0;
    result = KiStartInterruptCycleAccumulation(*(unsigned __int64 *)(gs_base + (0 + 32)), a2, a3, a4);
    result = KiSwInterruptDispatch(v_stack_m168, a2, a3, a4);
    result = HalPerformEndOfInterrupt(0, a2, a3, a4);
    result = KiEndInterruptCycleAccumulation(*(unsigned __int64 *)(gs_base + (0 + 32)), v_stack_m13F, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        result = KiDpcInterruptBypass(*(unsigned __int64 *)(gs_base + (0 + 32)), v_stack_m13F, a3, a4);
    }
    if ((*(unsigned int *)(v_rip + 9496797)) == 0) goto loc_006B844C;
    result = KzSetIrqlUnsafe(v_stack_m13F, v_stack_m13F, a3, a4);
    goto loc_006B8450;
loc_006B844C:
loc_006B8450:
    if (((v_stack_p8) & (1)) == 0) goto loc_006B875A;
    if (((*(unsigned __int8 *)(v_rip + 9496452)) & (255)) != 0) {
    }
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 194)) & (3)) == 0) goto loc_006B849E;
    result = KiInitiateUserApc(1, v_stack_m13F, a3, a4);
    goto loc_006B8471;
loc_006B849E:
    result = KiSynchronizeUserIsolationDomainEntry(0, v_stack_m13F, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_006B8471;
    result = v_stack_m138;
    if (((*(unsigned __int8 *)(gs_base + (0 + 2144))) & (2)) != 0) {
        a1 = 0;
        result = KiUpdateStibpPairing(a1, v_stack_m13F, a3, a4);
    }
    if (((*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)))) & (0x8000000ULL)) != 0) {
        result = KiRestoreSetContextState(*(unsigned __int64 *)(gs_base + (0 + 392)), v_stack_m13F, a3, a4);
    }
    if (((*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)))) & (0x10000ULL)) == 0) goto loc_006B84F8;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 2)) & (1)) != 0) {
        result = KiCopyCounters(*(unsigned __int64 *)(gs_base + (0 + 392)), v_stack_m13F, a3, a4);
        a1 = *(unsigned __int64 *)(gs_base + (0 + 392));
    }
    if (v_stack_m68 != 0) {
        result = KiRestoreDebugRegisterState(a1, v_stack_m13F, a3, a4);
    }
    if (v_stack_m68 >= 0) goto loc_006B8545;
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
    if (condition_is_above_or_equal) goto loc_006B86D7;
    result = KiSwInterrupt___0x643(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSwInterrupt___0x64C(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSwInterrupt___0x535(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSwInterrupt___0x53E(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSwInterrupt___0x547(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSwInterrupt___0x550(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSwInterrupt___0x559(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSwInterrupt___0x562(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSwInterrupt___0x56B(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSwInterrupt___0x574(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSwInterrupt___0x57D(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSwInterrupt___0x586(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSwInterrupt___0x58F(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSwInterrupt___0x598(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSwInterrupt___0x5A1(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSwInterrupt___0x5AA(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSwInterrupt___0x5B3(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSwInterrupt___0x5BC(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSwInterrupt___0x5C5(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSwInterrupt___0x5CE(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSwInterrupt___0x5D7(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSwInterrupt___0x5E0(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSwInterrupt___0x5E9(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSwInterrupt___0x5F2(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSwInterrupt___0x5FB(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSwInterrupt___0x604(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSwInterrupt___0x60D(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSwInterrupt___0x616(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSwInterrupt___0x61F(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSwInterrupt___0x628(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSwInterrupt___0x631(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiSwInterrupt___0x63A(a1, a2, a3, a4);
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
    if (((*(unsigned __int8 *)(v_rip + 11833604)) & (1)) == 0) goto loc_006B8743;
loc_006B8743:
    if (((*(unsigned __int16 *)(gs_base + (0 + 2136))) & (512)) != 0) {
    }
loc_006B875A:
    v_rsp = (v_stack_m10) + (232);
    return v_stack_m138;
}
```

## 5. (Beta) C Style

```c
int64_t KiSwInterrupt(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
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
    if (((v_stack_p8) & (1)) != 0) goto loc_006B80E6;
    Arg2 = 0;
    v_stack_m90 = 0;
    if (((*(uint8_t *)(gs_base + (0 + 0x858))) & (1)) != 0) goto loc_006B80CF;
    goto loc_006B8357;
loc_006B80CF:
    Arg2 = 0;
    goto loc_006B8357;
loc_006B80E6:
    if (((*(uint8_t *)(v_rip + 0xB49753)) & (1)) == 0) {
    }
    if (*(uint64_t *)(gs_base + (0 + 0x9D28)) == 0) goto loc_006B8122;
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
    if ((((uint32_t)(Arg2)) & (2)) == 0) goto loc_006B82FE;
    result = KiSwInterrupt___0x26A(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSwInterrupt___0x273(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSwInterrupt___0x15C(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSwInterrupt___0x165(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSwInterrupt___0x16E(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSwInterrupt___0x177(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSwInterrupt___0x180(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSwInterrupt___0x189(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSwInterrupt___0x192(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSwInterrupt___0x19B(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSwInterrupt___0x1A4(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSwInterrupt___0x1AD(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSwInterrupt___0x1B6(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSwInterrupt___0x1BF(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSwInterrupt___0x1C8(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSwInterrupt___0x1D1(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSwInterrupt___0x1DA(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSwInterrupt___0x1E3(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSwInterrupt___0x1EC(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSwInterrupt___0x1F5(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSwInterrupt___0x1FE(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSwInterrupt___0x207(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSwInterrupt___0x210(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSwInterrupt___0x219(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSwInterrupt___0x222(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSwInterrupt___0x22B(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSwInterrupt___0x234(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSwInterrupt___0x23D(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSwInterrupt___0x246(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSwInterrupt___0x24F(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSwInterrupt___0x258(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSwInterrupt___0x261(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = (uint32_t)(0xDADAULL);
    if (((*(uint8_t *)(gs_base + (0 + 0x85C))) & (8)) != 0) {
        result = 32;
    }
    if ((((uint32_t)(Arg2)) & (128)) != 0) {
        result = KiFlushBhbDuringTrapEntryOrExit(Arg1, Arg2, Arg3, Arg4);
    }
    *(uint8_t *)(gs_base + (0 + 0x85E)) = 0;
    if ((*(uint32_t *)(v_rip + 0x90EF43)) == 0) goto loc_006B8342;
    if (((uint32_t)(Arg2)) == 0) goto loc_006B8342;
    Arg2 = (uint32_t)((Arg2) & (*(uint32_t *)(v_rip + 0x90EF2D)));
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
    if ((v_rip + 8661) >= v_stack_p0) goto loc_006B83C4;
    result = v_rip + 8670;
    if ((v_rip + 8670) >= v_stack_p0) {
        Arg1 = v_stack_m168;
        result = KiCheckForSListAddress(Arg1, Arg2, Arg3, Arg4);
    }
    local_rsi = 0;
    if (((*(uint8_t *)(v_rip + 0x90E81B)) & (255)) != 0) {
    }
    if ((*(uint32_t *)(v_rip + 0x90E93A)) == 0) goto loc_006B83EF;
    result = KzSetIrqlUnsafe(2, Arg2, Arg3, Arg4);
    goto loc_006B83F7;
loc_006B83EF:
loc_006B83F7:
    v_stack_m13F = (uint8_t)(v_cr8);
    Arg2 = 0;
    result = KiStartInterruptCycleAccumulation(*(uint64_t *)(gs_base + (0 + 0x20)), Arg2, Arg3, Arg4);
    result = KiSwInterruptDispatch(v_stack_m168, Arg2, Arg3, Arg4);
    result = HalPerformEndOfInterrupt(0, Arg2, Arg3, Arg4);
    result = KiEndInterruptCycleAccumulation(*(uint64_t *)(gs_base + (0 + 0x20)), v_stack_m13F, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        result = KiDpcInterruptBypass(*(uint64_t *)(gs_base + (0 + 0x20)), v_stack_m13F, Arg3, Arg4);
    }
    if ((*(uint32_t *)(v_rip + 0x90E8DD)) == 0) goto loc_006B844C;
    result = KzSetIrqlUnsafe(v_stack_m13F, v_stack_m13F, Arg3, Arg4);
    goto loc_006B8450;
loc_006B844C:
loc_006B8450:
    if (((v_stack_p8) & (1)) == 0) goto loc_006B875A;
    if (((*(uint8_t *)(v_rip + 0x90E784)) & (255)) != 0) {
    }
    if (((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xC2)) & (3)) == 0) goto loc_006B849E;
    result = KiInitiateUserApc(1, v_stack_m13F, Arg3, Arg4);
    goto loc_006B8471;
loc_006B849E:
    result = KiSynchronizeUserIsolationDomainEntry(0, v_stack_m13F, Arg3, Arg4);
    if ((uint32_t)(result) != 0) goto loc_006B8471;
    result = v_stack_m138;
    if (((*(uint8_t *)(gs_base + (0 + 0x860))) & (2)) != 0) {
        Arg1 = 0;
        result = KiUpdateStibpPairing(Arg1, v_stack_m13F, Arg3, Arg4);
    }
    if (((*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)))) & (0x8000000ULL)) != 0) {
        result = KiRestoreSetContextState(*(uint64_t *)(gs_base + (0 + 0x188)), v_stack_m13F, Arg3, Arg4);
    }
    if (((*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)))) & (0x10000ULL)) == 0) goto loc_006B84F8;
    if (((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x2)) & (1)) != 0) {
        result = KiCopyCounters(*(uint64_t *)(gs_base + (0 + 0x188)), v_stack_m13F, Arg3, Arg4);
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x188));
    }
    if (v_stack_m68 != 0) {
        result = KiRestoreDebugRegisterState(Arg1, v_stack_m13F, Arg3, Arg4);
    }
    if (v_stack_m68 >= 0) goto loc_006B8545;
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
    if (condition_is_above_or_equal) goto loc_006B86D7;
    result = KiSwInterrupt___0x643(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSwInterrupt___0x64C(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSwInterrupt___0x535(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSwInterrupt___0x53E(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSwInterrupt___0x547(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSwInterrupt___0x550(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSwInterrupt___0x559(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSwInterrupt___0x562(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSwInterrupt___0x56B(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSwInterrupt___0x574(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSwInterrupt___0x57D(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSwInterrupt___0x586(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSwInterrupt___0x58F(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSwInterrupt___0x598(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSwInterrupt___0x5A1(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSwInterrupt___0x5AA(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSwInterrupt___0x5B3(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSwInterrupt___0x5BC(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSwInterrupt___0x5C5(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSwInterrupt___0x5CE(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSwInterrupt___0x5D7(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSwInterrupt___0x5E0(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSwInterrupt___0x5E9(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSwInterrupt___0x5F2(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSwInterrupt___0x5FB(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSwInterrupt___0x604(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSwInterrupt___0x60D(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSwInterrupt___0x616(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSwInterrupt___0x61F(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSwInterrupt___0x628(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSwInterrupt___0x631(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiSwInterrupt___0x63A(Arg1, Arg2, Arg3, Arg4);
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
    if (((*(uint8_t *)(v_rip + 0xB49104)) & (1)) == 0) goto loc_006B8743;
loc_006B8743:
    if (((*(uint16_t *)(gs_base + (0 + 0x858))) & (512)) != 0) {
    }
loc_006B875A:
    local_rsp = (v_stack_m10) + (232);
    return v_stack_m138;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006B8070&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
