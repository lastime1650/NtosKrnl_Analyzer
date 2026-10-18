# KiBoundFault

- RVA: `0x006BE040`–`0x006BE728` (길이 `1,768` bytes)
- VA: `0x00000001406BE040`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C1BC0`
- 디코드: `386`개 명령, `1,768/1,768` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **77**; 고유 호출 대상: **77**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x006BE196` → [KiBoundFault + 0x269](KiBoundFault_function_006BE040.md) (inside-function, `0x006BE2A9`)
- `0x006BE19F` → [KiBoundFault + 0x272](KiBoundFault_function_006BE040.md) (inside-function, `0x006BE2B2`)
- `0x006BE1A8` → [KiBoundFault + 0x15B](KiBoundFault_function_006BE040.md) (inside-function, `0x006BE19B`)
- `0x006BE1B1` → [KiBoundFault + 0x164](KiBoundFault_function_006BE040.md) (inside-function, `0x006BE1A4`)
- `0x006BE1BA` → [KiBoundFault + 0x16D](KiBoundFault_function_006BE040.md) (inside-function, `0x006BE1AD`)
- `0x006BE1C3` → [KiBoundFault + 0x176](KiBoundFault_function_006BE040.md) (inside-function, `0x006BE1B6`)
- `0x006BE1CC` → [KiBoundFault + 0x17F](KiBoundFault_function_006BE040.md) (inside-function, `0x006BE1BF`)
- `0x006BE1D5` → [KiBoundFault + 0x188](KiBoundFault_function_006BE040.md) (inside-function, `0x006BE1C8`)
- `0x006BE1DE` → [KiBoundFault + 0x191](KiBoundFault_function_006BE040.md) (inside-function, `0x006BE1D1`)
- `0x006BE1E7` → [KiBoundFault + 0x19A](KiBoundFault_function_006BE040.md) (inside-function, `0x006BE1DA`)
- `0x006BE1F0` → [KiBoundFault + 0x1A3](KiBoundFault_function_006BE040.md) (inside-function, `0x006BE1E3`)
- `0x006BE1F9` → [KiBoundFault + 0x1AC](KiBoundFault_function_006BE040.md) (inside-function, `0x006BE1EC`)
- `0x006BE202` → [KiBoundFault + 0x1B5](KiBoundFault_function_006BE040.md) (inside-function, `0x006BE1F5`)
- `0x006BE20B` → [KiBoundFault + 0x1BE](KiBoundFault_function_006BE040.md) (inside-function, `0x006BE1FE`)
- `0x006BE214` → [KiBoundFault + 0x1C7](KiBoundFault_function_006BE040.md) (inside-function, `0x006BE207`)
- `0x006BE21D` → [KiBoundFault + 0x1D0](KiBoundFault_function_006BE040.md) (inside-function, `0x006BE210`)
- `0x006BE226` → [KiBoundFault + 0x1D9](KiBoundFault_function_006BE040.md) (inside-function, `0x006BE219`)
- `0x006BE22F` → [KiBoundFault + 0x1E2](KiBoundFault_function_006BE040.md) (inside-function, `0x006BE222`)
- `0x006BE238` → [KiBoundFault + 0x1EB](KiBoundFault_function_006BE040.md) (inside-function, `0x006BE22B`)
- `0x006BE241` → [KiBoundFault + 0x1F4](KiBoundFault_function_006BE040.md) (inside-function, `0x006BE234`)
- `0x006BE24A` → [KiBoundFault + 0x1FD](KiBoundFault_function_006BE040.md) (inside-function, `0x006BE23D`)
- `0x006BE253` → [KiBoundFault + 0x206](KiBoundFault_function_006BE040.md) (inside-function, `0x006BE246`)
- `0x006BE25C` → [KiBoundFault + 0x20F](KiBoundFault_function_006BE040.md) (inside-function, `0x006BE24F`)
- `0x006BE265` → [KiBoundFault + 0x218](KiBoundFault_function_006BE040.md) (inside-function, `0x006BE258`)
- `0x006BE26E` → [KiBoundFault + 0x221](KiBoundFault_function_006BE040.md) (inside-function, `0x006BE261`)
- `0x006BE277` → [KiBoundFault + 0x22A](KiBoundFault_function_006BE040.md) (inside-function, `0x006BE26A`)
- `0x006BE280` → [KiBoundFault + 0x233](KiBoundFault_function_006BE040.md) (inside-function, `0x006BE273`)
- `0x006BE289` → [KiBoundFault + 0x23C](KiBoundFault_function_006BE040.md) (inside-function, `0x006BE27C`)
- `0x006BE292` → [KiBoundFault + 0x245](KiBoundFault_function_006BE040.md) (inside-function, `0x006BE285`)
- `0x006BE29B` → [KiBoundFault + 0x24E](KiBoundFault_function_006BE040.md) (inside-function, `0x006BE28E`)
- `0x006BE2A4` → [KiBoundFault + 0x257](KiBoundFault_function_006BE040.md) (inside-function, `0x006BE297`)
- `0x006BE2AD` → [KiBoundFault + 0x260](KiBoundFault_function_006BE040.md) (inside-function, `0x006BE2A0`)
- `0x006BE2D8` → [KiFlushBhbDuringTrapEntryOrExit](../6C/KiFlushBhbDuringTrapEntryOrExit_function_006C6340.md) (function, `0x006C6340`)
- `0x006BE321` → [KiSaveDebugRegisterState](../4F/KiSaveDebugRegisterState_function_004FD960.md) (function, `0x004FD960`)
- `0x006BE355` → [KiSynchronizeUserIsolationDomainExit](../41/KiSynchronizeUserIsolationDomainExit_function_0041BFA0.md) (function, `0x0041BFA0`)
- `0x006BE385` → [KiHandleBound](../5B/KiHandleBound_function_005B1FB0.md) (function, `0x005B1FB0`)
- `0x006BE3A3` → [KiBugCheckDispatch](../6C/KiBugCheckDispatch_function_006C5880.md) (function, `0x006C5880`)
- `0x006BE3C0` → [KiFastFailDispatch](../6C/KiFastFailDispatch_function_006C5E40.md) (function, `0x006C5E40`)
- `0x006BE3D4` → [KiExceptionDispatch](../6C/KiExceptionDispatch_function_006C5900.md) (function, `0x006C5900`)
- `0x006BE410` → [KiInitiateUserApc](KiInitiateUserApc_function_006B6540.md) (function, `0x006B6540`)
- `0x006BE421` → [KiSynchronizeUserIsolationDomainEntry](../26/KiSynchronizeUserIsolationDomainEntry_function_00263F60.md) (function, `0x00263F60`)
- `0x006BE43B` → [KiUpdateStibpPairing](../3E/KiUpdateStibpPairing_function_003E71C0.md) (function, `0x003E71C0`)
- `0x006BE451` → [KiRestoreSetContextState](KiRestoreSetContextState_function_006B1CA0.md) (function, `0x006B1CA0`)
- `0x006BE46D` → [KiCopyCounters](../5C/KiCopyCounters_function_005C0710.md) (function, `0x005C0710`)
- `0x006BE489` → [KiRestoreDebugRegisterState](../4F/KiRestoreDebugRegisterState_function_004FD8E0.md) (function, `0x004FD8E0`)
- `0x006BE523` → [KiBoundFault + 0x5F6](KiBoundFault_function_006BE040.md) (inside-function, `0x006BE636`)
- `0x006BE52C` → [KiBoundFault + 0x5FF](KiBoundFault_function_006BE040.md) (inside-function, `0x006BE63F`)
- `0x006BE535` → [KiBoundFault + 0x4E8](KiBoundFault_function_006BE040.md) (inside-function, `0x006BE528`)
- `0x006BE53E` → [KiBoundFault + 0x4F1](KiBoundFault_function_006BE040.md) (inside-function, `0x006BE531`)
- `0x006BE547` → [KiBoundFault + 0x4FA](KiBoundFault_function_006BE040.md) (inside-function, `0x006BE53A`)
- `0x006BE550` → [KiBoundFault + 0x503](KiBoundFault_function_006BE040.md) (inside-function, `0x006BE543`)
- `0x006BE559` → [KiBoundFault + 0x50C](KiBoundFault_function_006BE040.md) (inside-function, `0x006BE54C`)
- `0x006BE562` → [KiBoundFault + 0x515](KiBoundFault_function_006BE040.md) (inside-function, `0x006BE555`)
- `0x006BE56B` → [KiBoundFault + 0x51E](KiBoundFault_function_006BE040.md) (inside-function, `0x006BE55E`)
- `0x006BE574` → [KiBoundFault + 0x527](KiBoundFault_function_006BE040.md) (inside-function, `0x006BE567`)
- `0x006BE57D` → [KiBoundFault + 0x530](KiBoundFault_function_006BE040.md) (inside-function, `0x006BE570`)
- `0x006BE586` → [KiBoundFault + 0x539](KiBoundFault_function_006BE040.md) (inside-function, `0x006BE579`)
- `0x006BE58F` → [KiBoundFault + 0x542](KiBoundFault_function_006BE040.md) (inside-function, `0x006BE582`)
- `0x006BE598` → [KiBoundFault + 0x54B](KiBoundFault_function_006BE040.md) (inside-function, `0x006BE58B`)
- `0x006BE5A1` → [KiBoundFault + 0x554](KiBoundFault_function_006BE040.md) (inside-function, `0x006BE594`)
- `0x006BE5AA` → [KiBoundFault + 0x55D](KiBoundFault_function_006BE040.md) (inside-function, `0x006BE59D`)
- `0x006BE5B3` → [KiBoundFault + 0x566](KiBoundFault_function_006BE040.md) (inside-function, `0x006BE5A6`)
- `0x006BE5BC` → [KiBoundFault + 0x56F](KiBoundFault_function_006BE040.md) (inside-function, `0x006BE5AF`)
- `0x006BE5C5` → [KiBoundFault + 0x578](KiBoundFault_function_006BE040.md) (inside-function, `0x006BE5B8`)
- `0x006BE5CE` → [KiBoundFault + 0x581](KiBoundFault_function_006BE040.md) (inside-function, `0x006BE5C1`)
- `0x006BE5D7` → [KiBoundFault + 0x58A](KiBoundFault_function_006BE040.md) (inside-function, `0x006BE5CA`)
- `0x006BE5E0` → [KiBoundFault + 0x593](KiBoundFault_function_006BE040.md) (inside-function, `0x006BE5D3`)
- `0x006BE5E9` → [KiBoundFault + 0x59C](KiBoundFault_function_006BE040.md) (inside-function, `0x006BE5DC`)
- `0x006BE5F2` → [KiBoundFault + 0x5A5](KiBoundFault_function_006BE040.md) (inside-function, `0x006BE5E5`)
- `0x006BE5FB` → [KiBoundFault + 0x5AE](KiBoundFault_function_006BE040.md) (inside-function, `0x006BE5EE`)
- `0x006BE604` → [KiBoundFault + 0x5B7](KiBoundFault_function_006BE040.md) (inside-function, `0x006BE5F7`)
- `0x006BE60D` → [KiBoundFault + 0x5C0](KiBoundFault_function_006BE040.md) (inside-function, `0x006BE600`)
- `0x006BE616` → [KiBoundFault + 0x5C9](KiBoundFault_function_006BE040.md) (inside-function, `0x006BE609`)
- `0x006BE61F` → [KiBoundFault + 0x5D2](KiBoundFault_function_006BE040.md) (inside-function, `0x006BE612`)
- `0x006BE628` → [KiBoundFault + 0x5DB](KiBoundFault_function_006BE040.md) (inside-function, `0x006BE61B`)
- `0x006BE631` → [KiBoundFault + 0x5E4](KiBoundFault_function_006BE040.md) (inside-function, `0x006BE624`)
- `0x006BE63A` → [KiBoundFault + 0x5ED](KiBoundFault_function_006BE040.md) (inside-function, `0x006BE62D`)

### Direct callers
- [KiBoundFault](KiBoundFault_function_006BE040.md) at `0x006BE196`
- [KiBoundFault](KiBoundFault_function_006BE040.md) at `0x006BE19F`
- [KiBoundFault](KiBoundFault_function_006BE040.md) at `0x006BE1A8`
- [KiBoundFault](KiBoundFault_function_006BE040.md) at `0x006BE1B1`
- [KiBoundFault](KiBoundFault_function_006BE040.md) at `0x006BE1BA`
- [KiBoundFault](KiBoundFault_function_006BE040.md) at `0x006BE1C3`
- [KiBoundFault](KiBoundFault_function_006BE040.md) at `0x006BE1CC`
- [KiBoundFault](KiBoundFault_function_006BE040.md) at `0x006BE1D5`
- [KiBoundFault](KiBoundFault_function_006BE040.md) at `0x006BE1DE`
- [KiBoundFault](KiBoundFault_function_006BE040.md) at `0x006BE1E7`
- [KiBoundFault](KiBoundFault_function_006BE040.md) at `0x006BE1F0`
- [KiBoundFault](KiBoundFault_function_006BE040.md) at `0x006BE1F9`
- [KiBoundFault](KiBoundFault_function_006BE040.md) at `0x006BE202`
- [KiBoundFault](KiBoundFault_function_006BE040.md) at `0x006BE20B`
- [KiBoundFault](KiBoundFault_function_006BE040.md) at `0x006BE214`
- [KiBoundFault](KiBoundFault_function_006BE040.md) at `0x006BE21D`
- [KiBoundFault](KiBoundFault_function_006BE040.md) at `0x006BE226`
- [KiBoundFault](KiBoundFault_function_006BE040.md) at `0x006BE22F`
- [KiBoundFault](KiBoundFault_function_006BE040.md) at `0x006BE238`
- [KiBoundFault](KiBoundFault_function_006BE040.md) at `0x006BE241`
- [KiBoundFault](KiBoundFault_function_006BE040.md) at `0x006BE24A`
- [KiBoundFault](KiBoundFault_function_006BE040.md) at `0x006BE253`
- [KiBoundFault](KiBoundFault_function_006BE040.md) at `0x006BE25C`
- [KiBoundFault](KiBoundFault_function_006BE040.md) at `0x006BE265`
- [KiBoundFault](KiBoundFault_function_006BE040.md) at `0x006BE26E`
- [KiBoundFault](KiBoundFault_function_006BE040.md) at `0x006BE277`
- [KiBoundFault](KiBoundFault_function_006BE040.md) at `0x006BE280`
- [KiBoundFault](KiBoundFault_function_006BE040.md) at `0x006BE289`
- [KiBoundFault](KiBoundFault_function_006BE040.md) at `0x006BE292`
- [KiBoundFault](KiBoundFault_function_006BE040.md) at `0x006BE29B`
- [KiBoundFault](KiBoundFault_function_006BE040.md) at `0x006BE2A4`
- [KiBoundFault](KiBoundFault_function_006BE040.md) at `0x006BE2AD`
- [KiBoundFault](KiBoundFault_function_006BE040.md) at `0x006BE523`
- [KiBoundFault](KiBoundFault_function_006BE040.md) at `0x006BE52C`
- [KiBoundFault](KiBoundFault_function_006BE040.md) at `0x006BE535`
- [KiBoundFault](KiBoundFault_function_006BE040.md) at `0x006BE53E`
- [KiBoundFault](KiBoundFault_function_006BE040.md) at `0x006BE547`
- [KiBoundFault](KiBoundFault_function_006BE040.md) at `0x006BE550`
- [KiBoundFault](KiBoundFault_function_006BE040.md) at `0x006BE559`
- [KiBoundFault](KiBoundFault_function_006BE040.md) at `0x006BE562`
- [KiBoundFault](KiBoundFault_function_006BE040.md) at `0x006BE56B`
- [KiBoundFault](KiBoundFault_function_006BE040.md) at `0x006BE574`
- [KiBoundFault](KiBoundFault_function_006BE040.md) at `0x006BE57D`
- [KiBoundFault](KiBoundFault_function_006BE040.md) at `0x006BE586`
- [KiBoundFault](KiBoundFault_function_006BE040.md) at `0x006BE58F`
- [KiBoundFault](KiBoundFault_function_006BE040.md) at `0x006BE598`
- [KiBoundFault](KiBoundFault_function_006BE040.md) at `0x006BE5A1`
- [KiBoundFault](KiBoundFault_function_006BE040.md) at `0x006BE5AA`
- [KiBoundFault](KiBoundFault_function_006BE040.md) at `0x006BE5B3`
- [KiBoundFault](KiBoundFault_function_006BE040.md) at `0x006BE5BC`
- [KiBoundFault](KiBoundFault_function_006BE040.md) at `0x006BE5C5`
- [KiBoundFault](KiBoundFault_function_006BE040.md) at `0x006BE5CE`
- [KiBoundFault](KiBoundFault_function_006BE040.md) at `0x006BE5D7`
- [KiBoundFault](KiBoundFault_function_006BE040.md) at `0x006BE5E0`
- [KiBoundFault](KiBoundFault_function_006BE040.md) at `0x006BE5E9`
- [KiBoundFault](KiBoundFault_function_006BE040.md) at `0x006BE5F2`
- [KiBoundFault](KiBoundFault_function_006BE040.md) at `0x006BE5FB`
- [KiBoundFault](KiBoundFault_function_006BE040.md) at `0x006BE604`
- [KiBoundFault](KiBoundFault_function_006BE040.md) at `0x006BE60D`
- [KiBoundFault](KiBoundFault_function_006BE040.md) at `0x006BE616`
- [KiBoundFault](KiBoundFault_function_006BE040.md) at `0x006BE61F`
- [KiBoundFault](KiBoundFault_function_006BE040.md) at `0x006BE628`
- [KiBoundFault](KiBoundFault_function_006BE040.md) at `0x006BE631`
- [KiBoundFault](KiBoundFault_function_006BE040.md) at `0x006BE63A`

### Static image references
- `0x006BE0B5` → RVA `0x01201840` (`CFGRO`; read)
- `0x006BE2E9` → RVA `0x00FC7264` (`ALMOSTRO`; read)
- `0x006BE35A` → RVA `0x00FC6BF0` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006BE6C1` → [KiKernelExit](../../kvascode/BC/KiKernelExit_function_00BCCB80.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006BE040  48 83 EC 08                     sub rsp, 8
006BE044  55                              push rbp
006BE045  48 81 EC 58 01 00 00            sub rsp, 0x158
006BE04C  48 8D AC 24 80 00 00 00         lea rbp, [rsp + 0x80]
006BE054  C6 45 AB 01                     mov byte ptr [rbp - 0x55], 1
006BE058  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
006BE05C  48 89 4D B8                     mov qword ptr [rbp - 0x48], rcx
006BE060  48 89 55 C0                     mov qword ptr [rbp - 0x40], rdx
006BE064  4C 89 45 C8                     mov qword ptr [rbp - 0x38], r8
006BE068  4C 89 4D D0                     mov qword ptr [rbp - 0x30], r9
006BE06C  4C 89 55 D8                     mov qword ptr [rbp - 0x28], r10
006BE070  4C 89 5D E0                     mov qword ptr [rbp - 0x20], r11
006BE074  F6 85 F0 00 00 00 01            test byte ptr [rbp + 0xf0], 1
006BE07B  75 38                           jne 0x1406be0b5
006BE07D  33 D2                           xor edx, edx
006BE07F  F3 48 0F 1E CA                  rdsspq rdx
006BE084  48 89 55 58                     mov qword ptr [rbp + 0x58], rdx
006BE088  0F AE E8                        lfence
006BE08B  65 F6 04 25 58 08 00 00 01      test byte ptr gs:[0x858], 1
006BE094  75 08                           jne 0x1406be09e
006BE096  0F AE E8                        lfence
006BE099  E9 88 02 00 00                  jmp 0x1406be326
006BE09E  65 0F B7 04 25 66 08 00 00      movzx eax, word ptr gs:[0x866]
006BE0A7  B9 48 00 00 00                  mov ecx, 0x48
006BE0AC  33 D2                           xor edx, edx
006BE0AE  0F 30                           wrmsr
006BE0B0  E9 71 02 00 00                  jmp 0x1406be326
006BE0B5  F6 05 84 37 B4 00 01            test byte ptr [rip + 0xb43784], 1
006BE0BC  75 03                           jne 0x1406be0c1
006BE0BE  0F 01 F8                        swapgs
006BE0C1  0F AE E8                        lfence
006BE0C4  65 48 8B 0C 25 28 9D 00 00      mov rcx, qword ptr gs:[0x9d28]
006BE0CD  48 85 C9                        test rcx, rcx
006BE0D0  74 1F                           je 0x1406be0f1
006BE0D2  F3 48 0F 1E CA                  rdsspq rdx
006BE0D7  65 4C 8B 14 25 20 9D 00 00      mov r10, qword ptr gs:[0x9d20]
006BE0E0  49 83 C2 08                     add r10, 8
006BE0E4  49 3B D2                        cmp rdx, r10
006BE0E7  75 08                           jne 0x1406be0f1
006BE0E9  F3 0F 01 29                     rstorssp dword ptr [rcx]
006BE0ED  F3 0F 01 EA                     saveprevssp
006BE0F1  65 4C 8B 14 25 88 01 00 00      mov r10, qword ptr gs:[0x188]
006BE0FA  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006BE103  48 8B 89 20 02 00 00            mov rcx, qword ptr [rcx + 0x220]
006BE10A  48 8B 89 60 07 00 00            mov rcx, qword ptr [rcx + 0x760]
006BE111  65 48 89 0C 25 50 08 00 00      mov qword ptr gs:[0x850], rcx
006BE11A  66 65 8B 0C 25 62 08 00 00      mov cx, word ptr gs:[0x862]
006BE123  66 65 89 0C 25 64 08 00 00      mov word ptr gs:[0x864], cx
006BE12C  65 8A 0C 25 58 08 00 00         mov cl, byte ptr gs:[0x858]
006BE134  65 88 0C 25 5A 08 00 00         mov byte ptr gs:[0x85a], cl
006BE13C  65 0F B7 04 25 68 08 00 00      movzx eax, word ptr gs:[0x868]
006BE145  66 65 39 04 25 66 08 00 00      cmp word ptr gs:[0x866], ax
006BE14E  74 12                           je 0x1406be162
006BE150  66 65 89 04 25 66 08 00 00      mov word ptr gs:[0x866], ax
006BE159  B9 48 00 00 00                  mov ecx, 0x48
006BE15E  33 D2                           xor edx, edx
006BE160  0F 30                           wrmsr
006BE162  65 0F B6 14 25 58 08 00 00      movzx edx, byte ptr gs:[0x858]
006BE16B  F7 C2 08 00 00 00               test edx, 8
006BE171  74 17                           je 0x1406be18a
006BE173  B8 01 00 00 00                  mov eax, 1
006BE178  33 D2                           xor edx, edx
006BE17A  B9 49 00 00 00                  mov ecx, 0x49
006BE17F  0F 30                           wrmsr
006BE181  65 0F B6 14 25 58 08 00 00      movzx edx, byte ptr gs:[0x858]
006BE18A  F7 C2 02 00 00 00               test edx, 2
006BE190  0F 84 37 01 00 00               je 0x1406be2cd
006BE196  E8 0E 01 00 00                  call 0x1406be2a9
006BE19B  48 83 C4 08                     add rsp, 8
006BE19F  E8 0E 01 00 00                  call 0x1406be2b2
006BE1A4  48 83 C4 08                     add rsp, 8
006BE1A8  E8 EE FF FF FF                  call 0x1406be19b
006BE1AD  48 83 C4 08                     add rsp, 8
006BE1B1  E8 EE FF FF FF                  call 0x1406be1a4
006BE1B6  48 83 C4 08                     add rsp, 8
006BE1BA  E8 EE FF FF FF                  call 0x1406be1ad
006BE1BF  48 83 C4 08                     add rsp, 8
006BE1C3  E8 EE FF FF FF                  call 0x1406be1b6
006BE1C8  48 83 C4 08                     add rsp, 8
006BE1CC  E8 EE FF FF FF                  call 0x1406be1bf
006BE1D1  48 83 C4 08                     add rsp, 8
006BE1D5  E8 EE FF FF FF                  call 0x1406be1c8
006BE1DA  48 83 C4 08                     add rsp, 8
006BE1DE  E8 EE FF FF FF                  call 0x1406be1d1
006BE1E3  48 83 C4 08                     add rsp, 8
006BE1E7  E8 EE FF FF FF                  call 0x1406be1da
006BE1EC  48 83 C4 08                     add rsp, 8
006BE1F0  E8 EE FF FF FF                  call 0x1406be1e3
006BE1F5  48 83 C4 08                     add rsp, 8
006BE1F9  E8 EE FF FF FF                  call 0x1406be1ec
006BE1FE  48 83 C4 08                     add rsp, 8
006BE202  E8 EE FF FF FF                  call 0x1406be1f5
006BE207  48 83 C4 08                     add rsp, 8
006BE20B  E8 EE FF FF FF                  call 0x1406be1fe
006BE210  48 83 C4 08                     add rsp, 8
006BE214  E8 EE FF FF FF                  call 0x1406be207
006BE219  48 83 C4 08                     add rsp, 8
006BE21D  E8 EE FF FF FF                  call 0x1406be210
006BE222  48 83 C4 08                     add rsp, 8
006BE226  E8 EE FF FF FF                  call 0x1406be219
006BE22B  48 83 C4 08                     add rsp, 8
006BE22F  E8 EE FF FF FF                  call 0x1406be222
006BE234  48 83 C4 08                     add rsp, 8
006BE238  E8 EE FF FF FF                  call 0x1406be22b
006BE23D  48 83 C4 08                     add rsp, 8
006BE241  E8 EE FF FF FF                  call 0x1406be234
006BE246  48 83 C4 08                     add rsp, 8
006BE24A  E8 EE FF FF FF                  call 0x1406be23d
006BE24F  48 83 C4 08                     add rsp, 8
006BE253  E8 EE FF FF FF                  call 0x1406be246
006BE258  48 83 C4 08                     add rsp, 8
006BE25C  E8 EE FF FF FF                  call 0x1406be24f
006BE261  48 83 C4 08                     add rsp, 8
006BE265  E8 EE FF FF FF                  call 0x1406be258
006BE26A  48 83 C4 08                     add rsp, 8
006BE26E  E8 EE FF FF FF                  call 0x1406be261
006BE273  48 83 C4 08                     add rsp, 8
006BE277  E8 EE FF FF FF                  call 0x1406be26a
006BE27C  48 83 C4 08                     add rsp, 8
006BE280  E8 EE FF FF FF                  call 0x1406be273
006BE285  48 83 C4 08                     add rsp, 8
006BE289  E8 EE FF FF FF                  call 0x1406be27c
006BE28E  48 83 C4 08                     add rsp, 8
006BE292  E8 EE FF FF FF                  call 0x1406be285
006BE297  48 83 C4 08                     add rsp, 8
006BE29B  E8 EE FF FF FF                  call 0x1406be28e
006BE2A0  48 83 C4 08                     add rsp, 8
006BE2A4  E8 EE FF FF FF                  call 0x1406be297
006BE2A9  48 83 C4 08                     add rsp, 8
006BE2AD  E8 EE FF FF FF                  call 0x1406be2a0
006BE2B2  48 83 C4 08                     add rsp, 8
006BE2B6  B8 DA DA 00 00                  mov eax, 0xdada
006BE2BB  65 F6 04 25 5C 08 00 00 08      test byte ptr gs:[0x85c], 8
006BE2C4  74 07                           je 0x1406be2cd
006BE2C6  B0 20                           mov al, 0x20
006BE2C8  F3 48 0F AE E8                  incsspq rax
006BE2CD  F7 C2 80 00 00 00               test edx, 0x80
006BE2D3  74 08                           je 0x1406be2dd
006BE2D5  0F AE E8                        lfence
006BE2D8  E8 63 80 00 00                  call 0x1406c6340
006BE2DD  0F AE E8                        lfence
006BE2E0  65 C6 04 25 5E 08 00 00 00      mov byte ptr gs:[0x85e], 0
006BE2E9  83 3D 74 8F 90 00 00            cmp dword ptr [rip + 0x908f74], 0
006BE2F0  74 1F                           je 0x1406be311
006BE2F2  B9 A7 06 00 00                  mov ecx, 0x6a7
006BE2F7  0F 32                           rdmsr
006BE2F9  83 FA 00                        cmp edx, 0
006BE2FC  74 13                           je 0x1406be311
006BE2FE  8B CA                           mov ecx, edx
006BE300  23 15 5E 8F 90 00               and edx, dword ptr [rip + 0x908f5e]
006BE306  3B D1                           cmp edx, ecx
006BE308  74 07                           je 0x1406be311
006BE30A  B9 A7 06 00 00                  mov ecx, 0x6a7
006BE30F  0F 30                           wrmsr
006BE311  41 F6 42 03 03                  test byte ptr [r10 + 3], 3
006BE316  66 C7 85 80 00 00 00 00 00      mov word ptr [rbp + 0x80], 0
006BE31F  74 05                           je 0x1406be326
006BE321  E8 3A F6 E3 FF                  call 0x1404fd960
006BE326  FC                              cld
006BE327  0F AE 5D AC                     stmxcsr dword ptr [rbp - 0x54]
006BE32B  65 0F AE 14 25 80 01 00 00      ldmxcsr dword ptr gs:[0x180]
006BE334  0F 29 45 F0                     movaps xmmword ptr [rbp - 0x10], xmm0
006BE338  0F 29 4D 00                     movaps xmmword ptr [rbp], xmm1
006BE33C  0F 29 55 10                     movaps xmmword ptr [rbp + 0x10], xmm2
006BE340  0F 29 5D 20                     movaps xmmword ptr [rbp + 0x20], xmm3
006BE344  0F 29 65 30                     movaps xmmword ptr [rbp + 0x30], xmm4
006BE348  0F 29 6D 40                     movaps xmmword ptr [rbp + 0x40], xmm5
006BE34C  F6 85 F0 00 00 00 01            test byte ptr [rbp + 0xf0], 1
006BE353  74 05                           je 0x1406be35a
006BE355  E8 46 DC D5 FF                  call 0x14041bfa0
006BE35A  F6 05 8F 88 90 00 FF            test byte ptr [rip + 0x90888f], 0xff
006BE361  74 0C                           je 0x1406be36f
006BE363  F6 85 F0 00 00 00 01            test byte ptr [rbp + 0xf0], 1
006BE36A  74 03                           je 0x1406be36f
006BE36C  0F 01 CB                        stac
006BE36F  F7 85 F8 00 00 00 00 02 00 00   test dword ptr [rbp + 0xf8], 0x200
006BE379  74 01                           je 0x1406be37c
006BE37B  FB                              sti
006BE37C  F6 85 F0 00 00 00 01            test byte ptr [rbp + 0xf0], 1
006BE383  74 41                           je 0x1406be3c6
006BE385  E8 26 3C EF FF                  call 0x1405b1fb0
006BE38A  83 F8 00                        cmp eax, 0
006BE38D  74 37                           je 0x1406be3c6
006BE38F  83 F8 01                        cmp eax, 1
006BE392  74 46                           je 0x1406be3da
006BE394  83 F8 02                        cmp eax, 2
006BE397  74 0F                           je 0x1406be3a8
006BE399  BA 05 00 00 00                  mov edx, 5
006BE39E  B9 7F 00 00 00                  mov ecx, 0x7f
006BE3A3  E8 D8 74 00 00                  call 0x1406c5880
006BE3A8  49 C7 C1 1C 00 00 00            mov r9, 0x1c
006BE3AF  B9 09 04 00 C0                  mov ecx, 0xc0000409
006BE3B4  BA 01 00 00 00                  mov edx, 1
006BE3B9  4C 8B 85 E8 00 00 00            mov r8, qword ptr [rbp + 0xe8]
006BE3C0  E8 7B 7A 00 00                  call 0x1406c5e40
006BE3C5  90                              nop
006BE3C6  B9 8C 00 00 C0                  mov ecx, 0xc000008c
006BE3CB  33 D2                           xor edx, edx
006BE3CD  4C 8B 85 E8 00 00 00            mov r8, qword ptr [rbp + 0xe8]
006BE3D4  E8 27 75 00 00                  call 0x1406c5900
006BE3D9  90                              nop
006BE3DA  FA                              cli
006BE3DB  F6 85 F0 00 00 00 01            test byte ptr [rbp + 0xf0], 1
006BE3E2  0F 84 F5 02 00 00               je 0x1406be6dd
006BE3E8  F6 05 01 88 90 00 FF            test byte ptr [rip + 0x908801], 0xff
006BE3EF  74 03                           je 0x1406be3f4
006BE3F1  0F 01 CB                        stac
006BE3F4  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006BE3FD  F6 81 C2 00 00 00 03            test byte ptr [rcx + 0xc2], 3
006BE404  74 1B                           je 0x1406be421
006BE406  B9 01 00 00 00                  mov ecx, 1
006BE40B  44 0F 22 C1                     mov cr8, rcx
006BE40F  FB                              sti
006BE410  E8 2B 81 FF FF                  call 0x1406b6540
006BE415  FA                              cli
006BE416  B9 00 00 00 00                  mov ecx, 0
006BE41B  44 0F 22 C1                     mov cr8, rcx
006BE41F  EB D3                           jmp 0x1406be3f4
006BE421  E8 3A 5B BA FF                  call 0x140263f60
006BE426  85 C0                           test eax, eax
006BE428  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
006BE42C  75 C6                           jne 0x1406be3f4
006BE42E  65 F6 04 25 60 08 00 00 02      test byte ptr gs:[0x860], 2
006BE437  74 07                           je 0x1406be440
006BE439  33 C9                           xor ecx, ecx
006BE43B  E8 80 8D D2 FF                  call 0x1403e71c0
006BE440  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006BE449  F7 01 00 00 00 08               test dword ptr [rcx], 0x8000000
006BE44F  74 05                           je 0x1406be456
006BE451  E8 4A 38 FF FF                  call 0x1406b1ca0
006BE456  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006BE45F  F7 01 00 00 01 00               test dword ptr [rcx], 0x10000
006BE465  74 14                           je 0x1406be47b
006BE467  F6 41 02 01                     test byte ptr [rcx + 2], 1
006BE46B  74 0E                           je 0x1406be47b
006BE46D  E8 9E 22 F0 FF                  call 0x1405c0710
006BE472  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006BE47B  0F AE 55 AC                     ldmxcsr dword ptr [rbp - 0x54]
006BE47F  66 83 BD 80 00 00 00 00         cmp word ptr [rbp + 0x80], 0
006BE487  74 05                           je 0x1406be48e
006BE489  E8 52 F4 E3 FF                  call 0x1404fd8e0
006BE48E  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006BE497  0F BA 61 74 16                  bt dword ptr [rcx + 0x74], 0x16
006BE49C  73 2A                           jae 0x1406be4c8
006BE49E  33 C9                           xor ecx, ecx
006BE4A0  F3 48 0F 1E C9                  rdsspq rcx
006BE4A5  65 4C 8B 04 25 28 9D 00 00      mov r8, qword ptr gs:[0x9d28]
006BE4AE  49 83 C0 08                     add r8, 8
006BE4B2  49 3B C8                        cmp rcx, r8
006BE4B5  75 11                           jne 0x1406be4c8
006BE4B7  65 48 8B 0C 25 20 9D 00 00      mov rcx, qword ptr gs:[0x9d20]
006BE4C0  F3 0F 01 29                     rstorssp dword ptr [rcx]
006BE4C4  F3 0F 01 EA                     saveprevssp
006BE4C8  65 C6 04 25 5E 08 00 00 00      mov byte ptr gs:[0x85e], 0
006BE4D1  65 0F B7 04 25 6C 08 00 00      movzx eax, word ptr gs:[0x86c]
006BE4DA  66 65 39 04 25 66 08 00 00      cmp word ptr gs:[0x866], ax
006BE4E3  74 12                           je 0x1406be4f7
006BE4E5  66 65 89 04 25 66 08 00 00      mov word ptr gs:[0x866], ax
006BE4EE  B9 48 00 00 00                  mov ecx, 0x48
006BE4F3  33 D2                           xor edx, edx
006BE4F5  0F 30                           wrmsr
006BE4F7  66 65 0F BA 34 25 58 08 00 00 02  btr word ptr gs:[0x858], 2
006BE502  73 0E                           jae 0x1406be512
006BE504  B8 01 00 00 00                  mov eax, 1
006BE509  33 D2                           xor edx, edx
006BE50B  B9 49 00 00 00                  mov ecx, 0x49
006BE510  0F 30                           wrmsr
006BE512  66 65 0F BA 34 25 58 08 00 00 05  btr word ptr gs:[0x858], 5
006BE51D  0F 83 37 01 00 00               jae 0x1406be65a
006BE523  E8 0E 01 00 00                  call 0x1406be636
006BE528  48 83 C4 08                     add rsp, 8
006BE52C  E8 0E 01 00 00                  call 0x1406be63f
006BE531  48 83 C4 08                     add rsp, 8
006BE535  E8 EE FF FF FF                  call 0x1406be528
006BE53A  48 83 C4 08                     add rsp, 8
006BE53E  E8 EE FF FF FF                  call 0x1406be531
006BE543  48 83 C4 08                     add rsp, 8
006BE547  E8 EE FF FF FF                  call 0x1406be53a
006BE54C  48 83 C4 08                     add rsp, 8
006BE550  E8 EE FF FF FF                  call 0x1406be543
006BE555  48 83 C4 08                     add rsp, 8
006BE559  E8 EE FF FF FF                  call 0x1406be54c
006BE55E  48 83 C4 08                     add rsp, 8
006BE562  E8 EE FF FF FF                  call 0x1406be555
006BE567  48 83 C4 08                     add rsp, 8
006BE56B  E8 EE FF FF FF                  call 0x1406be55e
006BE570  48 83 C4 08                     add rsp, 8
006BE574  E8 EE FF FF FF                  call 0x1406be567
006BE579  48 83 C4 08                     add rsp, 8
006BE57D  E8 EE FF FF FF                  call 0x1406be570
006BE582  48 83 C4 08                     add rsp, 8
006BE586  E8 EE FF FF FF                  call 0x1406be579
006BE58B  48 83 C4 08                     add rsp, 8
006BE58F  E8 EE FF FF FF                  call 0x1406be582
006BE594  48 83 C4 08                     add rsp, 8
006BE598  E8 EE FF FF FF                  call 0x1406be58b
006BE59D  48 83 C4 08                     add rsp, 8
006BE5A1  E8 EE FF FF FF                  call 0x1406be594
006BE5A6  48 83 C4 08                     add rsp, 8
006BE5AA  E8 EE FF FF FF                  call 0x1406be59d
006BE5AF  48 83 C4 08                     add rsp, 8
006BE5B3  E8 EE FF FF FF                  call 0x1406be5a6
006BE5B8  48 83 C4 08                     add rsp, 8
006BE5BC  E8 EE FF FF FF                  call 0x1406be5af
006BE5C1  48 83 C4 08                     add rsp, 8
006BE5C5  E8 EE FF FF FF                  call 0x1406be5b8
006BE5CA  48 83 C4 08                     add rsp, 8
006BE5CE  E8 EE FF FF FF                  call 0x1406be5c1
006BE5D3  48 83 C4 08                     add rsp, 8
006BE5D7  E8 EE FF FF FF                  call 0x1406be5ca
006BE5DC  48 83 C4 08                     add rsp, 8
006BE5E0  E8 EE FF FF FF                  call 0x1406be5d3
006BE5E5  48 83 C4 08                     add rsp, 8
006BE5E9  E8 EE FF FF FF                  call 0x1406be5dc
006BE5EE  48 83 C4 08                     add rsp, 8
006BE5F2  E8 EE FF FF FF                  call 0x1406be5e5
006BE5F7  48 83 C4 08                     add rsp, 8
006BE5FB  E8 EE FF FF FF                  call 0x1406be5ee
006BE600  48 83 C4 08                     add rsp, 8
006BE604  E8 EE FF FF FF                  call 0x1406be5f7
006BE609  48 83 C4 08                     add rsp, 8
006BE60D  E8 EE FF FF FF                  call 0x1406be600
006BE612  48 83 C4 08                     add rsp, 8
006BE616  E8 EE FF FF FF                  call 0x1406be609
006BE61B  48 83 C4 08                     add rsp, 8
006BE61F  E8 EE FF FF FF                  call 0x1406be612
006BE624  48 83 C4 08                     add rsp, 8
006BE628  E8 EE FF FF FF                  call 0x1406be61b
006BE62D  48 83 C4 08                     add rsp, 8
006BE631  E8 EE FF FF FF                  call 0x1406be624
006BE636  48 83 C4 08                     add rsp, 8
006BE63A  E8 EE FF FF FF                  call 0x1406be62d
006BE63F  48 83 C4 08                     add rsp, 8
006BE643  B8 DA DA 00 00                  mov eax, 0xdada
006BE648  65 F6 04 25 5C 08 00 00 08      test byte ptr gs:[0x85c], 8
006BE651  74 07                           je 0x1406be65a
006BE653  B0 20                           mov al, 0x20
006BE655  F3 48 0F AE E8                  incsspq rax
006BE65A  66 65 F7 04 25 58 08 00 00 00 01  test word ptr gs:[0x858], 0x100
006BE665  74 0C                           je 0x1406be673
006BE667  33 C0                           xor eax, eax
006BE669  33 D2                           xor edx, edx
006BE66B  B9 01 00 00 00                  mov ecx, 1
006BE670  48 F7 F1                        div rcx
006BE673  0F 28 45 F0                     movaps xmm0, xmmword ptr [rbp - 0x10]
006BE677  0F 28 4D 00                     movaps xmm1, xmmword ptr [rbp]
006BE67B  0F 28 55 10                     movaps xmm2, xmmword ptr [rbp + 0x10]
006BE67F  0F 28 5D 20                     movaps xmm3, xmmword ptr [rbp + 0x20]
006BE683  0F 28 65 30                     movaps xmm4, xmmword ptr [rbp + 0x30]
006BE687  0F 28 6D 40                     movaps xmm5, xmmword ptr [rbp + 0x40]
006BE68B  4C 8B 5D E0                     mov r11, qword ptr [rbp - 0x20]
006BE68F  4C 8B 55 D8                     mov r10, qword ptr [rbp - 0x28]
006BE693  4C 8B 4D D0                     mov r9, qword ptr [rbp - 0x30]
006BE697  4C 8B 45 C8                     mov r8, qword ptr [rbp - 0x38]
006BE69B  48 8B 55 C0                     mov rdx, qword ptr [rbp - 0x40]
006BE69F  48 8B 4D B8                     mov rcx, qword ptr [rbp - 0x48]
006BE6A3  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
006BE6A7  48 8B E5                        mov rsp, rbp
006BE6AA  48 8B AD D8 00 00 00            mov rbp, qword ptr [rbp + 0xd8]
006BE6B1  48 81 C4 E8 00 00 00            add rsp, 0xe8
006BE6B8  F6 05 81 31 B4 00 01            test byte ptr [rip + 0xb43181], 1
006BE6BF  74 05                           je 0x1406be6c6
006BE6C1  E9 BA E4 50 00                  jmp 0x140bccb80
006BE6C6  66 65 F7 04 25 58 08 00 00 00 02  test word ptr gs:[0x858], 0x200
006BE6D1  74 05                           je 0x1406be6d8
006BE6D3  0F 00 6C 24 20                  verw word ptr [rsp + 0x20]
006BE6D8  0F 01 F8                        swapgs
006BE6DB  48 CF                           iretq
006BE6DD  0F AE 55 AC                     ldmxcsr dword ptr [rbp - 0x54]
006BE6E1  0F 28 45 F0                     movaps xmm0, xmmword ptr [rbp - 0x10]
006BE6E5  0F 28 4D 00                     movaps xmm1, xmmword ptr [rbp]
006BE6E9  0F 28 55 10                     movaps xmm2, xmmword ptr [rbp + 0x10]
006BE6ED  0F 28 5D 20                     movaps xmm3, xmmword ptr [rbp + 0x20]
006BE6F1  0F 28 65 30                     movaps xmm4, xmmword ptr [rbp + 0x30]
006BE6F5  0F 28 6D 40                     movaps xmm5, xmmword ptr [rbp + 0x40]
006BE6F9  4C 8B 5D E0                     mov r11, qword ptr [rbp - 0x20]
006BE6FD  4C 8B 55 D8                     mov r10, qword ptr [rbp - 0x28]
006BE701  4C 8B 4D D0                     mov r9, qword ptr [rbp - 0x30]
006BE705  4C 8B 45 C8                     mov r8, qword ptr [rbp - 0x38]
006BE709  48 8B 55 C0                     mov rdx, qword ptr [rbp - 0x40]
006BE70D  48 8B 4D B8                     mov rcx, qword ptr [rbp - 0x48]
006BE711  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
006BE715  48 8B E5                        mov rsp, rbp
006BE718  48 8B AD D8 00 00 00            mov rbp, qword ptr [rbp + 0xd8]
006BE71F  48 81 C4 E8 00 00 00            add rsp, 0xe8
006BE726  48 CF                           iretq
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiBoundFault(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
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
    if (((v_stack_p8) & (1)) != 0) goto loc_006BE0B5;
    a2 = 0;
    v_stack_m90 = 0;
    if (((*(unsigned __int8 *)(gs_base + (0 + 2136))) & (1)) != 0) goto loc_006BE09E;
    goto loc_006BE326;
loc_006BE09E:
    a2 = 0;
    goto loc_006BE326;
loc_006BE0B5:
    if (((*(unsigned __int8 *)(v_rip + 11810692)) & (1)) == 0) {
    }
    if (*(unsigned __int64 *)(gs_base + (0 + 40232)) == 0) goto loc_006BE0F1;
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
    if ((((unsigned int)(a2)) & (2)) == 0) goto loc_006BE2CD;
    result = KiBoundFault___0x269(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiBoundFault___0x272(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiBoundFault___0x15B(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiBoundFault___0x164(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiBoundFault___0x16D(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiBoundFault___0x176(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiBoundFault___0x17F(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiBoundFault___0x188(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiBoundFault___0x191(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiBoundFault___0x19A(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiBoundFault___0x1A3(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiBoundFault___0x1AC(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiBoundFault___0x1B5(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiBoundFault___0x1BE(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiBoundFault___0x1C7(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiBoundFault___0x1D0(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiBoundFault___0x1D9(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiBoundFault___0x1E2(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiBoundFault___0x1EB(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiBoundFault___0x1F4(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiBoundFault___0x1FD(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiBoundFault___0x206(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiBoundFault___0x20F(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiBoundFault___0x218(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiBoundFault___0x221(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiBoundFault___0x22A(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiBoundFault___0x233(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiBoundFault___0x23C(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiBoundFault___0x245(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiBoundFault___0x24E(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiBoundFault___0x257(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiBoundFault___0x260(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = (unsigned int)(0xDADAULL);
    if (((*(unsigned __int8 *)(gs_base + (0 + 2140))) & (8)) != 0) {
        result = 32;
    }
    if ((((unsigned int)(a2)) & (128)) != 0) {
        result = KiFlushBhbDuringTrapEntryOrExit(a1, a2, a3, a4);
    }
    *(unsigned __int8 *)(gs_base + (0 + 2142)) = 0;
    if ((*(unsigned int *)(v_rip + 9473908)) == 0) goto loc_006BE311;
    if (((unsigned int)(a2)) == 0) goto loc_006BE311;
    a2 = (unsigned int)((a2) & (*(unsigned int *)(v_rip + 9473886)));
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
    if (((*(unsigned __int8 *)(v_rip + 9472143)) & (255)) == 0) goto loc_006BE36F;
    if (((v_stack_p8) & (1)) != 0) {
    }
    if (((v_stack_p10) & (512)) != 0) {
    }
    if (((v_stack_p8) & (1)) == 0) goto loc_006BE3C6;
    result = KiHandleBound(a1, a2, a3, a4);
    if (((unsigned int)(result)) == 0) goto loc_006BE3C6;
    if (((unsigned int)(result)) == 1) goto loc_006BE3DA;
    if (((unsigned int)(result)) != 2) {
        a2 = 5;
        a1 = 127;
        result = KiBugCheckDispatch(a1, a2, a3, a4);
    }
    result = KiFastFailDispatch((unsigned int)(0xC0000409ULL), 1, v_stack_p0, 28);
loc_006BE3C6:
    a2 = 0;
    result = KiExceptionDispatch((unsigned int)(0xC000008CULL), a2, v_stack_p0, 28);
loc_006BE3DA:
    if (((v_stack_p8) & (1)) == 0) goto loc_006BE6DD;
    if (((*(unsigned __int8 *)(v_rip + 9472001)) & (255)) != 0) {
    }
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 194)) & (3)) == 0) goto loc_006BE421;
    result = KiInitiateUserApc(1, a2, v_stack_p0, 28);
    goto loc_006BE3F4;
loc_006BE421:
    result = KiSynchronizeUserIsolationDomainEntry(0, a2, v_stack_p0, 28);
    if ((unsigned int)(result) != 0) goto loc_006BE3F4;
    result = v_stack_m138;
    if (((*(unsigned __int8 *)(gs_base + (0 + 2144))) & (2)) != 0) {
        a1 = 0;
        result = KiUpdateStibpPairing(a1, a2, v_stack_p0, 28);
    }
    if (((*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)))) & (0x8000000ULL)) != 0) {
        result = KiRestoreSetContextState(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, v_stack_p0, 28);
    }
    if (((*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)))) & (0x10000ULL)) == 0) goto loc_006BE47B;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 2)) & (1)) != 0) {
        result = KiCopyCounters(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, v_stack_p0, 28);
        a1 = *(unsigned __int64 *)(gs_base + (0 + 392));
    }
    if (v_stack_m68 != 0) {
        result = KiRestoreDebugRegisterState(a1, a2, v_stack_p0, 28);
    }
    if (v_stack_m68 >= 0) goto loc_006BE4C8;
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
    if (condition_is_above_or_equal) goto loc_006BE65A;
    result = KiBoundFault___0x5F6(a1, a2, a3, 28);
    v_rsp = (v_rsp) + (8);
    result = KiBoundFault___0x5FF(a1, a2, a3, 28);
    v_rsp = (v_rsp) + (8);
    result = KiBoundFault___0x4E8(a1, a2, a3, 28);
    v_rsp = (v_rsp) + (8);
    result = KiBoundFault___0x4F1(a1, a2, a3, 28);
    v_rsp = (v_rsp) + (8);
    result = KiBoundFault___0x4FA(a1, a2, a3, 28);
    v_rsp = (v_rsp) + (8);
    result = KiBoundFault___0x503(a1, a2, a3, 28);
    v_rsp = (v_rsp) + (8);
    result = KiBoundFault___0x50C(a1, a2, a3, 28);
    v_rsp = (v_rsp) + (8);
    result = KiBoundFault___0x515(a1, a2, a3, 28);
    v_rsp = (v_rsp) + (8);
    result = KiBoundFault___0x51E(a1, a2, a3, 28);
    v_rsp = (v_rsp) + (8);
    result = KiBoundFault___0x527(a1, a2, a3, 28);
    v_rsp = (v_rsp) + (8);
    result = KiBoundFault___0x530(a1, a2, a3, 28);
    v_rsp = (v_rsp) + (8);
    result = KiBoundFault___0x539(a1, a2, a3, 28);
    v_rsp = (v_rsp) + (8);
    result = KiBoundFault___0x542(a1, a2, a3, 28);
    v_rsp = (v_rsp) + (8);
    result = KiBoundFault___0x54B(a1, a2, a3, 28);
    v_rsp = (v_rsp) + (8);
    result = KiBoundFault___0x554(a1, a2, a3, 28);
    v_rsp = (v_rsp) + (8);
    result = KiBoundFault___0x55D(a1, a2, a3, 28);
    v_rsp = (v_rsp) + (8);
    result = KiBoundFault___0x566(a1, a2, a3, 28);
    v_rsp = (v_rsp) + (8);
    result = KiBoundFault___0x56F(a1, a2, a3, 28);
    v_rsp = (v_rsp) + (8);
    result = KiBoundFault___0x578(a1, a2, a3, 28);
    v_rsp = (v_rsp) + (8);
    result = KiBoundFault___0x581(a1, a2, a3, 28);
    v_rsp = (v_rsp) + (8);
    result = KiBoundFault___0x58A(a1, a2, a3, 28);
    v_rsp = (v_rsp) + (8);
    result = KiBoundFault___0x593(a1, a2, a3, 28);
    v_rsp = (v_rsp) + (8);
    result = KiBoundFault___0x59C(a1, a2, a3, 28);
    v_rsp = (v_rsp) + (8);
    result = KiBoundFault___0x5A5(a1, a2, a3, 28);
    v_rsp = (v_rsp) + (8);
    result = KiBoundFault___0x5AE(a1, a2, a3, 28);
    v_rsp = (v_rsp) + (8);
    result = KiBoundFault___0x5B7(a1, a2, a3, 28);
    v_rsp = (v_rsp) + (8);
    result = KiBoundFault___0x5C0(a1, a2, a3, 28);
    v_rsp = (v_rsp) + (8);
    result = KiBoundFault___0x5C9(a1, a2, a3, 28);
    v_rsp = (v_rsp) + (8);
    result = KiBoundFault___0x5D2(a1, a2, a3, 28);
    v_rsp = (v_rsp) + (8);
    result = KiBoundFault___0x5DB(a1, a2, a3, 28);
    v_rsp = (v_rsp) + (8);
    result = KiBoundFault___0x5E4(a1, a2, a3, 28);
    v_rsp = (v_rsp) + (8);
    result = KiBoundFault___0x5ED(a1, a2, a3, 28);
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
    if (((*(unsigned __int8 *)(v_rip + 11809153)) & (1)) == 0) goto loc_006BE6C6;
loc_006BE6C6:
    if (((*(unsigned __int16 *)(gs_base + (0 + 2136))) & (512)) != 0) {
    }
loc_006BE6DD:
    v_rsp = (v_stack_m10) + (232);
    return v_stack_m138;
}
```

## 5. (Beta) C Style

```c
int64_t KiBoundFault(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
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
    if (((v_stack_p8) & (1)) != 0) goto loc_006BE0B5;
    Arg2 = 0;
    v_stack_m90 = 0;
    if (((*(uint8_t *)(gs_base + (0 + 0x858))) & (1)) != 0) goto loc_006BE09E;
    goto loc_006BE326;
loc_006BE09E:
    Arg2 = 0;
    goto loc_006BE326;
loc_006BE0B5:
    if (((*(uint8_t *)(v_rip + 0xB43784)) & (1)) == 0) {
    }
    if (*(uint64_t *)(gs_base + (0 + 0x9D28)) == 0) goto loc_006BE0F1;
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
    if ((((uint32_t)(Arg2)) & (2)) == 0) goto loc_006BE2CD;
    result = KiBoundFault___0x269(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiBoundFault___0x272(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiBoundFault___0x15B(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiBoundFault___0x164(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiBoundFault___0x16D(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiBoundFault___0x176(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiBoundFault___0x17F(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiBoundFault___0x188(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiBoundFault___0x191(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiBoundFault___0x19A(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiBoundFault___0x1A3(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiBoundFault___0x1AC(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiBoundFault___0x1B5(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiBoundFault___0x1BE(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiBoundFault___0x1C7(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiBoundFault___0x1D0(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiBoundFault___0x1D9(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiBoundFault___0x1E2(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiBoundFault___0x1EB(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiBoundFault___0x1F4(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiBoundFault___0x1FD(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiBoundFault___0x206(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiBoundFault___0x20F(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiBoundFault___0x218(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiBoundFault___0x221(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiBoundFault___0x22A(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiBoundFault___0x233(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiBoundFault___0x23C(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiBoundFault___0x245(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiBoundFault___0x24E(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiBoundFault___0x257(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiBoundFault___0x260(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = (uint32_t)(0xDADAULL);
    if (((*(uint8_t *)(gs_base + (0 + 0x85C))) & (8)) != 0) {
        result = 32;
    }
    if ((((uint32_t)(Arg2)) & (128)) != 0) {
        result = KiFlushBhbDuringTrapEntryOrExit(Arg1, Arg2, Arg3, Arg4);
    }
    *(uint8_t *)(gs_base + (0 + 0x85E)) = 0;
    if ((*(uint32_t *)(v_rip + 0x908F74)) == 0) goto loc_006BE311;
    if (((uint32_t)(Arg2)) == 0) goto loc_006BE311;
    Arg2 = (uint32_t)((Arg2) & (*(uint32_t *)(v_rip + 0x908F5E)));
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
    if (((*(uint8_t *)(v_rip + 0x90888F)) & (255)) == 0) goto loc_006BE36F;
    if (((v_stack_p8) & (1)) != 0) {
    }
    if (((v_stack_p10) & (512)) != 0) {
    }
    if (((v_stack_p8) & (1)) == 0) goto loc_006BE3C6;
    result = KiHandleBound(Arg1, Arg2, Arg3, Arg4);
    if (((uint32_t)(result)) == 0) goto loc_006BE3C6;
    if (((uint32_t)(result)) == 1) goto loc_006BE3DA;
    if (((uint32_t)(result)) != 2) {
        Arg2 = 5;
        Arg1 = 127;
        result = KiBugCheckDispatch(Arg1, Arg2, Arg3, Arg4);
    }
    result = KiFastFailDispatch((uint32_t)(0xC0000409ULL), 1, v_stack_p0, 28);
loc_006BE3C6:
    Arg2 = 0;
    result = KiExceptionDispatch((uint32_t)(0xC000008CULL), Arg2, v_stack_p0, 28);
loc_006BE3DA:
    if (((v_stack_p8) & (1)) == 0) goto loc_006BE6DD;
    if (((*(uint8_t *)(v_rip + 0x908801)) & (255)) != 0) {
    }
    if (((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xC2)) & (3)) == 0) goto loc_006BE421;
    result = KiInitiateUserApc(1, Arg2, v_stack_p0, 28);
    goto loc_006BE3F4;
loc_006BE421:
    result = KiSynchronizeUserIsolationDomainEntry(0, Arg2, v_stack_p0, 28);
    if ((uint32_t)(result) != 0) goto loc_006BE3F4;
    result = v_stack_m138;
    if (((*(uint8_t *)(gs_base + (0 + 0x860))) & (2)) != 0) {
        Arg1 = 0;
        result = KiUpdateStibpPairing(Arg1, Arg2, v_stack_p0, 28);
    }
    if (((*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)))) & (0x8000000ULL)) != 0) {
        result = KiRestoreSetContextState(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, v_stack_p0, 28);
    }
    if (((*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)))) & (0x10000ULL)) == 0) goto loc_006BE47B;
    if (((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x2)) & (1)) != 0) {
        result = KiCopyCounters(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, v_stack_p0, 28);
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x188));
    }
    if (v_stack_m68 != 0) {
        result = KiRestoreDebugRegisterState(Arg1, Arg2, v_stack_p0, 28);
    }
    if (v_stack_m68 >= 0) goto loc_006BE4C8;
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
    if (condition_is_above_or_equal) goto loc_006BE65A;
    result = KiBoundFault___0x5F6(Arg1, Arg2, Arg3, 28);
    local_rsp = (local_rsp) + (8);
    result = KiBoundFault___0x5FF(Arg1, Arg2, Arg3, 28);
    local_rsp = (local_rsp) + (8);
    result = KiBoundFault___0x4E8(Arg1, Arg2, Arg3, 28);
    local_rsp = (local_rsp) + (8);
    result = KiBoundFault___0x4F1(Arg1, Arg2, Arg3, 28);
    local_rsp = (local_rsp) + (8);
    result = KiBoundFault___0x4FA(Arg1, Arg2, Arg3, 28);
    local_rsp = (local_rsp) + (8);
    result = KiBoundFault___0x503(Arg1, Arg2, Arg3, 28);
    local_rsp = (local_rsp) + (8);
    result = KiBoundFault___0x50C(Arg1, Arg2, Arg3, 28);
    local_rsp = (local_rsp) + (8);
    result = KiBoundFault___0x515(Arg1, Arg2, Arg3, 28);
    local_rsp = (local_rsp) + (8);
    result = KiBoundFault___0x51E(Arg1, Arg2, Arg3, 28);
    local_rsp = (local_rsp) + (8);
    result = KiBoundFault___0x527(Arg1, Arg2, Arg3, 28);
    local_rsp = (local_rsp) + (8);
    result = KiBoundFault___0x530(Arg1, Arg2, Arg3, 28);
    local_rsp = (local_rsp) + (8);
    result = KiBoundFault___0x539(Arg1, Arg2, Arg3, 28);
    local_rsp = (local_rsp) + (8);
    result = KiBoundFault___0x542(Arg1, Arg2, Arg3, 28);
    local_rsp = (local_rsp) + (8);
    result = KiBoundFault___0x54B(Arg1, Arg2, Arg3, 28);
    local_rsp = (local_rsp) + (8);
    result = KiBoundFault___0x554(Arg1, Arg2, Arg3, 28);
    local_rsp = (local_rsp) + (8);
    result = KiBoundFault___0x55D(Arg1, Arg2, Arg3, 28);
    local_rsp = (local_rsp) + (8);
    result = KiBoundFault___0x566(Arg1, Arg2, Arg3, 28);
    local_rsp = (local_rsp) + (8);
    result = KiBoundFault___0x56F(Arg1, Arg2, Arg3, 28);
    local_rsp = (local_rsp) + (8);
    result = KiBoundFault___0x578(Arg1, Arg2, Arg3, 28);
    local_rsp = (local_rsp) + (8);
    result = KiBoundFault___0x581(Arg1, Arg2, Arg3, 28);
    local_rsp = (local_rsp) + (8);
    result = KiBoundFault___0x58A(Arg1, Arg2, Arg3, 28);
    local_rsp = (local_rsp) + (8);
    result = KiBoundFault___0x593(Arg1, Arg2, Arg3, 28);
    local_rsp = (local_rsp) + (8);
    result = KiBoundFault___0x59C(Arg1, Arg2, Arg3, 28);
    local_rsp = (local_rsp) + (8);
    result = KiBoundFault___0x5A5(Arg1, Arg2, Arg3, 28);
    local_rsp = (local_rsp) + (8);
    result = KiBoundFault___0x5AE(Arg1, Arg2, Arg3, 28);
    local_rsp = (local_rsp) + (8);
    result = KiBoundFault___0x5B7(Arg1, Arg2, Arg3, 28);
    local_rsp = (local_rsp) + (8);
    result = KiBoundFault___0x5C0(Arg1, Arg2, Arg3, 28);
    local_rsp = (local_rsp) + (8);
    result = KiBoundFault___0x5C9(Arg1, Arg2, Arg3, 28);
    local_rsp = (local_rsp) + (8);
    result = KiBoundFault___0x5D2(Arg1, Arg2, Arg3, 28);
    local_rsp = (local_rsp) + (8);
    result = KiBoundFault___0x5DB(Arg1, Arg2, Arg3, 28);
    local_rsp = (local_rsp) + (8);
    result = KiBoundFault___0x5E4(Arg1, Arg2, Arg3, 28);
    local_rsp = (local_rsp) + (8);
    result = KiBoundFault___0x5ED(Arg1, Arg2, Arg3, 28);
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
    if (((*(uint8_t *)(v_rip + 0xB43181)) & (1)) == 0) goto loc_006BE6C6;
loc_006BE6C6:
    if (((*(uint16_t *)(gs_base + (0 + 0x858))) & (512)) != 0) {
    }
loc_006BE6DD:
    local_rsp = (v_stack_m10) + (232);
    return v_stack_m138;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006BE040&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
