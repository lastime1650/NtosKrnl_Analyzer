# KiPageFault

- RVA: `0x006C0740`–`0x006C0F3F` (길이 `2,047` bytes)
- VA: `0x00000001406C0740`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C1C7C`
- 디코드: `453`개 명령, `2,047/2,047` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **78**; 고유 호출 대상: **78**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x006C0892` → [KiPageFault + 0x265](KiPageFault_function_006C0740.md) (inside-function, `0x006C09A5`)
- `0x006C089B` → [KiPageFault + 0x26E](KiPageFault_function_006C0740.md) (inside-function, `0x006C09AE`)
- `0x006C08A4` → [KiPageFault + 0x157](KiPageFault_function_006C0740.md) (inside-function, `0x006C0897`)
- `0x006C08AD` → [KiPageFault + 0x160](KiPageFault_function_006C0740.md) (inside-function, `0x006C08A0`)
- `0x006C08B6` → [KiPageFault + 0x169](KiPageFault_function_006C0740.md) (inside-function, `0x006C08A9`)
- `0x006C08BF` → [KiPageFault + 0x172](KiPageFault_function_006C0740.md) (inside-function, `0x006C08B2`)
- `0x006C08C8` → [KiPageFault + 0x17B](KiPageFault_function_006C0740.md) (inside-function, `0x006C08BB`)
- `0x006C08D1` → [KiPageFault + 0x184](KiPageFault_function_006C0740.md) (inside-function, `0x006C08C4`)
- `0x006C08DA` → [KiPageFault + 0x18D](KiPageFault_function_006C0740.md) (inside-function, `0x006C08CD`)
- `0x006C08E3` → [KiPageFault + 0x196](KiPageFault_function_006C0740.md) (inside-function, `0x006C08D6`)
- `0x006C08EC` → [KiPageFault + 0x19F](KiPageFault_function_006C0740.md) (inside-function, `0x006C08DF`)
- `0x006C08F5` → [KiPageFault + 0x1A8](KiPageFault_function_006C0740.md) (inside-function, `0x006C08E8`)
- `0x006C08FE` → [KiPageFault + 0x1B1](KiPageFault_function_006C0740.md) (inside-function, `0x006C08F1`)
- `0x006C0907` → [KiPageFault + 0x1BA](KiPageFault_function_006C0740.md) (inside-function, `0x006C08FA`)
- `0x006C0910` → [KiPageFault + 0x1C3](KiPageFault_function_006C0740.md) (inside-function, `0x006C0903`)
- `0x006C0919` → [KiPageFault + 0x1CC](KiPageFault_function_006C0740.md) (inside-function, `0x006C090C`)
- `0x006C0922` → [KiPageFault + 0x1D5](KiPageFault_function_006C0740.md) (inside-function, `0x006C0915`)
- `0x006C092B` → [KiPageFault + 0x1DE](KiPageFault_function_006C0740.md) (inside-function, `0x006C091E`)
- `0x006C0934` → [KiPageFault + 0x1E7](KiPageFault_function_006C0740.md) (inside-function, `0x006C0927`)
- `0x006C093D` → [KiPageFault + 0x1F0](KiPageFault_function_006C0740.md) (inside-function, `0x006C0930`)
- `0x006C0946` → [KiPageFault + 0x1F9](KiPageFault_function_006C0740.md) (inside-function, `0x006C0939`)
- `0x006C094F` → [KiPageFault + 0x202](KiPageFault_function_006C0740.md) (inside-function, `0x006C0942`)
- `0x006C0958` → [KiPageFault + 0x20B](KiPageFault_function_006C0740.md) (inside-function, `0x006C094B`)
- `0x006C0961` → [KiPageFault + 0x214](KiPageFault_function_006C0740.md) (inside-function, `0x006C0954`)
- `0x006C096A` → [KiPageFault + 0x21D](KiPageFault_function_006C0740.md) (inside-function, `0x006C095D`)
- `0x006C0973` → [KiPageFault + 0x226](KiPageFault_function_006C0740.md) (inside-function, `0x006C0966`)
- `0x006C097C` → [KiPageFault + 0x22F](KiPageFault_function_006C0740.md) (inside-function, `0x006C096F`)
- `0x006C0985` → [KiPageFault + 0x238](KiPageFault_function_006C0740.md) (inside-function, `0x006C0978`)
- `0x006C098E` → [KiPageFault + 0x241](KiPageFault_function_006C0740.md) (inside-function, `0x006C0981`)
- `0x006C0997` → [KiPageFault + 0x24A](KiPageFault_function_006C0740.md) (inside-function, `0x006C098A`)
- `0x006C09A0` → [KiPageFault + 0x253](KiPageFault_function_006C0740.md) (inside-function, `0x006C0993`)
- `0x006C09A9` → [KiPageFault + 0x25C](KiPageFault_function_006C0740.md) (inside-function, `0x006C099C`)
- `0x006C09D4` → [KiFlushBhbDuringTrapEntryOrExit](KiFlushBhbDuringTrapEntryOrExit_function_006C6340.md) (function, `0x006C6340`)
- `0x006C0A34` → [KiSaveDebugRegisterState](../4F/KiSaveDebugRegisterState_function_004FD960.md) (function, `0x004FD960`)
- `0x006C0A68` → [KiSynchronizeUserIsolationDomainExit](../41/KiSynchronizeUserIsolationDomainExit_function_0041BFA0.md) (function, `0x0041BFA0`)
- `0x006C0AC6` → [MmAccessFault](../27/MmAccessFault_function_0027EE80.md) (function, `0x0027EE80`)
- `0x006C0B7D` → [KiExceptionDispatch](KiExceptionDispatch_function_006C5900.md) (function, `0x006C5900`)
- `0x006C0BA3` → [KiBugCheckDispatch](KiBugCheckDispatch_function_006C5880.md) (function, `0x006C5880`)
- `0x006C0BC4` → [PsWatchWorkingSet](../45/PsWatchWorkingSet_function_00452910.md) (function, `0x00452910`)
- `0x006C0BE1` → [KiCheckForSListAddress](../40/KiCheckForSListAddress_function_0040B810.md) (function, `0x0040B810`)
- `0x006C0C27` → [KiInitiateUserApc](../6B/KiInitiateUserApc_function_006B6540.md) (function, `0x006B6540`)
- `0x006C0C38` → [KiSynchronizeUserIsolationDomainEntry](../26/KiSynchronizeUserIsolationDomainEntry_function_00263F60.md) (function, `0x00263F60`)
- `0x006C0C52` → [KiUpdateStibpPairing](../3E/KiUpdateStibpPairing_function_003E71C0.md) (function, `0x003E71C0`)
- `0x006C0C68` → [KiRestoreSetContextState](../6B/KiRestoreSetContextState_function_006B1CA0.md) (function, `0x006B1CA0`)
- `0x006C0C84` → [KiCopyCounters](../5C/KiCopyCounters_function_005C0710.md) (function, `0x005C0710`)
- `0x006C0CA0` → [KiRestoreDebugRegisterState](../4F/KiRestoreDebugRegisterState_function_004FD8E0.md) (function, `0x004FD8E0`)
- `0x006C0D3A` → [KiPageFault + 0x70D](KiPageFault_function_006C0740.md) (inside-function, `0x006C0E4D`)
- `0x006C0D43` → [KiPageFault + 0x716](KiPageFault_function_006C0740.md) (inside-function, `0x006C0E56`)
- `0x006C0D4C` → [KiPageFault + 0x5FF](KiPageFault_function_006C0740.md) (inside-function, `0x006C0D3F`)
- `0x006C0D55` → [KiPageFault + 0x608](KiPageFault_function_006C0740.md) (inside-function, `0x006C0D48`)
- `0x006C0D5E` → [KiPageFault + 0x611](KiPageFault_function_006C0740.md) (inside-function, `0x006C0D51`)
- `0x006C0D67` → [KiPageFault + 0x61A](KiPageFault_function_006C0740.md) (inside-function, `0x006C0D5A`)
- `0x006C0D70` → [KiPageFault + 0x623](KiPageFault_function_006C0740.md) (inside-function, `0x006C0D63`)
- `0x006C0D79` → [KiPageFault + 0x62C](KiPageFault_function_006C0740.md) (inside-function, `0x006C0D6C`)
- `0x006C0D82` → [KiPageFault + 0x635](KiPageFault_function_006C0740.md) (inside-function, `0x006C0D75`)
- `0x006C0D8B` → [KiPageFault + 0x63E](KiPageFault_function_006C0740.md) (inside-function, `0x006C0D7E`)
- `0x006C0D94` → [KiPageFault + 0x647](KiPageFault_function_006C0740.md) (inside-function, `0x006C0D87`)
- `0x006C0D9D` → [KiPageFault + 0x650](KiPageFault_function_006C0740.md) (inside-function, `0x006C0D90`)
- `0x006C0DA6` → [KiPageFault + 0x659](KiPageFault_function_006C0740.md) (inside-function, `0x006C0D99`)
- `0x006C0DAF` → [KiPageFault + 0x662](KiPageFault_function_006C0740.md) (inside-function, `0x006C0DA2`)
- `0x006C0DB8` → [KiPageFault + 0x66B](KiPageFault_function_006C0740.md) (inside-function, `0x006C0DAB`)
- `0x006C0DC1` → [KiPageFault + 0x674](KiPageFault_function_006C0740.md) (inside-function, `0x006C0DB4`)
- `0x006C0DCA` → [KiPageFault + 0x67D](KiPageFault_function_006C0740.md) (inside-function, `0x006C0DBD`)
- `0x006C0DD3` → [KiPageFault + 0x686](KiPageFault_function_006C0740.md) (inside-function, `0x006C0DC6`)
- `0x006C0DDC` → [KiPageFault + 0x68F](KiPageFault_function_006C0740.md) (inside-function, `0x006C0DCF`)
- `0x006C0DE5` → [KiPageFault + 0x698](KiPageFault_function_006C0740.md) (inside-function, `0x006C0DD8`)
- `0x006C0DEE` → [KiPageFault + 0x6A1](KiPageFault_function_006C0740.md) (inside-function, `0x006C0DE1`)
- `0x006C0DF7` → [KiPageFault + 0x6AA](KiPageFault_function_006C0740.md) (inside-function, `0x006C0DEA`)
- `0x006C0E00` → [KiPageFault + 0x6B3](KiPageFault_function_006C0740.md) (inside-function, `0x006C0DF3`)
- `0x006C0E09` → [KiPageFault + 0x6BC](KiPageFault_function_006C0740.md) (inside-function, `0x006C0DFC`)
- `0x006C0E12` → [KiPageFault + 0x6C5](KiPageFault_function_006C0740.md) (inside-function, `0x006C0E05`)
- `0x006C0E1B` → [KiPageFault + 0x6CE](KiPageFault_function_006C0740.md) (inside-function, `0x006C0E0E`)
- `0x006C0E24` → [KiPageFault + 0x6D7](KiPageFault_function_006C0740.md) (inside-function, `0x006C0E17`)
- `0x006C0E2D` → [KiPageFault + 0x6E0](KiPageFault_function_006C0740.md) (inside-function, `0x006C0E20`)
- `0x006C0E36` → [KiPageFault + 0x6E9](KiPageFault_function_006C0740.md) (inside-function, `0x006C0E29`)
- `0x006C0E3F` → [KiPageFault + 0x6F2](KiPageFault_function_006C0740.md) (inside-function, `0x006C0E32`)
- `0x006C0E48` → [KiPageFault + 0x6FB](KiPageFault_function_006C0740.md) (inside-function, `0x006C0E3B`)
- `0x006C0E51` → [KiPageFault + 0x704](KiPageFault_function_006C0740.md) (inside-function, `0x006C0E44`)

### Direct callers
- [KiPageFault](KiPageFault_function_006C0740.md) at `0x006C0892`
- [KiPageFault](KiPageFault_function_006C0740.md) at `0x006C089B`
- [KiPageFault](KiPageFault_function_006C0740.md) at `0x006C08A4`
- [KiPageFault](KiPageFault_function_006C0740.md) at `0x006C08AD`
- [KiPageFault](KiPageFault_function_006C0740.md) at `0x006C08B6`
- [KiPageFault](KiPageFault_function_006C0740.md) at `0x006C08BF`
- [KiPageFault](KiPageFault_function_006C0740.md) at `0x006C08C8`
- [KiPageFault](KiPageFault_function_006C0740.md) at `0x006C08D1`
- [KiPageFault](KiPageFault_function_006C0740.md) at `0x006C08DA`
- [KiPageFault](KiPageFault_function_006C0740.md) at `0x006C08E3`
- [KiPageFault](KiPageFault_function_006C0740.md) at `0x006C08EC`
- [KiPageFault](KiPageFault_function_006C0740.md) at `0x006C08F5`
- [KiPageFault](KiPageFault_function_006C0740.md) at `0x006C08FE`
- [KiPageFault](KiPageFault_function_006C0740.md) at `0x006C0907`
- [KiPageFault](KiPageFault_function_006C0740.md) at `0x006C0910`
- [KiPageFault](KiPageFault_function_006C0740.md) at `0x006C0919`
- [KiPageFault](KiPageFault_function_006C0740.md) at `0x006C0922`
- [KiPageFault](KiPageFault_function_006C0740.md) at `0x006C092B`
- [KiPageFault](KiPageFault_function_006C0740.md) at `0x006C0934`
- [KiPageFault](KiPageFault_function_006C0740.md) at `0x006C093D`
- [KiPageFault](KiPageFault_function_006C0740.md) at `0x006C0946`
- [KiPageFault](KiPageFault_function_006C0740.md) at `0x006C094F`
- [KiPageFault](KiPageFault_function_006C0740.md) at `0x006C0958`
- [KiPageFault](KiPageFault_function_006C0740.md) at `0x006C0961`
- [KiPageFault](KiPageFault_function_006C0740.md) at `0x006C096A`
- [KiPageFault](KiPageFault_function_006C0740.md) at `0x006C0973`
- [KiPageFault](KiPageFault_function_006C0740.md) at `0x006C097C`
- [KiPageFault](KiPageFault_function_006C0740.md) at `0x006C0985`
- [KiPageFault](KiPageFault_function_006C0740.md) at `0x006C098E`
- [KiPageFault](KiPageFault_function_006C0740.md) at `0x006C0997`
- [KiPageFault](KiPageFault_function_006C0740.md) at `0x006C09A0`
- [KiPageFault](KiPageFault_function_006C0740.md) at `0x006C09A9`
- [KiPageFault](KiPageFault_function_006C0740.md) at `0x006C0D3A`
- [KiPageFault](KiPageFault_function_006C0740.md) at `0x006C0D43`
- [KiPageFault](KiPageFault_function_006C0740.md) at `0x006C0D4C`
- [KiPageFault](KiPageFault_function_006C0740.md) at `0x006C0D55`
- [KiPageFault](KiPageFault_function_006C0740.md) at `0x006C0D5E`
- [KiPageFault](KiPageFault_function_006C0740.md) at `0x006C0D67`
- [KiPageFault](KiPageFault_function_006C0740.md) at `0x006C0D70`
- [KiPageFault](KiPageFault_function_006C0740.md) at `0x006C0D79`
- [KiPageFault](KiPageFault_function_006C0740.md) at `0x006C0D82`
- [KiPageFault](KiPageFault_function_006C0740.md) at `0x006C0D8B`
- [KiPageFault](KiPageFault_function_006C0740.md) at `0x006C0D94`
- [KiPageFault](KiPageFault_function_006C0740.md) at `0x006C0D9D`
- [KiPageFault](KiPageFault_function_006C0740.md) at `0x006C0DA6`
- [KiPageFault](KiPageFault_function_006C0740.md) at `0x006C0DAF`
- [KiPageFault](KiPageFault_function_006C0740.md) at `0x006C0DB8`
- [KiPageFault](KiPageFault_function_006C0740.md) at `0x006C0DC1`
- [KiPageFault](KiPageFault_function_006C0740.md) at `0x006C0DCA`
- [KiPageFault](KiPageFault_function_006C0740.md) at `0x006C0DD3`
- [KiPageFault](KiPageFault_function_006C0740.md) at `0x006C0DDC`
- [KiPageFault](KiPageFault_function_006C0740.md) at `0x006C0DE5`
- [KiPageFault](KiPageFault_function_006C0740.md) at `0x006C0DEE`
- [KiPageFault](KiPageFault_function_006C0740.md) at `0x006C0DF7`
- [KiPageFault](KiPageFault_function_006C0740.md) at `0x006C0E00`
- [KiPageFault](KiPageFault_function_006C0740.md) at `0x006C0E09`
- [KiPageFault](KiPageFault_function_006C0740.md) at `0x006C0E12`
- [KiPageFault](KiPageFault_function_006C0740.md) at `0x006C0E1B`
- [KiPageFault](KiPageFault_function_006C0740.md) at `0x006C0E24`
- [KiPageFault](KiPageFault_function_006C0740.md) at `0x006C0E2D`
- [KiPageFault](KiPageFault_function_006C0740.md) at `0x006C0E36`
- [KiPageFault](KiPageFault_function_006C0740.md) at `0x006C0E3F`
- [KiPageFault](KiPageFault_function_006C0740.md) at `0x006C0E48`
- [KiPageFault](KiPageFault_function_006C0740.md) at `0x006C0E51`

### Static image references
- `0x006C07B1` → RVA `0x01201840` (`CFGRO`; read)
- `0x006C09E5` → RVA `0x00FC7264` (`ALMOSTRO`; read)
- `0x006C0A6D` → RVA `0x00FC6BF0` (`ALMOSTRO`; read)
- `0x006C0BAE` → RVA `0x00F06629` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006C0ED8` → [KiKernelExit](../../kvascode/BC/KiKernelExit_function_00BCCB80.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006C0740  55                              push rbp
006C0741  48 81 EC 58 01 00 00            sub rsp, 0x158
006C0748  48 8D AC 24 80 00 00 00         lea rbp, [rsp + 0x80]
006C0750  C6 45 AB 01                     mov byte ptr [rbp - 0x55], 1
006C0754  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
006C0758  48 89 4D B8                     mov qword ptr [rbp - 0x48], rcx
006C075C  48 89 55 C0                     mov qword ptr [rbp - 0x40], rdx
006C0760  4C 89 45 C8                     mov qword ptr [rbp - 0x38], r8
006C0764  4C 89 4D D0                     mov qword ptr [rbp - 0x30], r9
006C0768  4C 89 55 D8                     mov qword ptr [rbp - 0x28], r10
006C076C  4C 89 5D E0                     mov qword ptr [rbp - 0x20], r11
006C0770  F6 85 F0 00 00 00 01            test byte ptr [rbp + 0xf0], 1
006C0777  75 38                           jne 0x1406c07b1
006C0779  33 D2                           xor edx, edx
006C077B  F3 48 0F 1E CA                  rdsspq rdx
006C0780  48 89 55 58                     mov qword ptr [rbp + 0x58], rdx
006C0784  0F AE E8                        lfence
006C0787  65 F6 04 25 58 08 00 00 01      test byte ptr gs:[0x858], 1
006C0790  75 08                           jne 0x1406c079a
006C0792  0F AE E8                        lfence
006C0795  E9 9F 02 00 00                  jmp 0x1406c0a39
006C079A  65 0F B7 04 25 66 08 00 00      movzx eax, word ptr gs:[0x866]
006C07A3  B9 48 00 00 00                  mov ecx, 0x48
006C07A8  33 D2                           xor edx, edx
006C07AA  0F 30                           wrmsr
006C07AC  E9 88 02 00 00                  jmp 0x1406c0a39
006C07B1  F6 05 88 10 B4 00 01            test byte ptr [rip + 0xb41088], 1
006C07B8  75 03                           jne 0x1406c07bd
006C07BA  0F 01 F8                        swapgs
006C07BD  0F AE E8                        lfence
006C07C0  65 48 8B 0C 25 28 9D 00 00      mov rcx, qword ptr gs:[0x9d28]
006C07C9  48 85 C9                        test rcx, rcx
006C07CC  74 1F                           je 0x1406c07ed
006C07CE  F3 48 0F 1E CA                  rdsspq rdx
006C07D3  65 4C 8B 14 25 20 9D 00 00      mov r10, qword ptr gs:[0x9d20]
006C07DC  49 83 C2 08                     add r10, 8
006C07E0  49 3B D2                        cmp rdx, r10
006C07E3  75 08                           jne 0x1406c07ed
006C07E5  F3 0F 01 29                     rstorssp dword ptr [rcx]
006C07E9  F3 0F 01 EA                     saveprevssp
006C07ED  65 4C 8B 14 25 88 01 00 00      mov r10, qword ptr gs:[0x188]
006C07F6  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006C07FF  48 8B 89 20 02 00 00            mov rcx, qword ptr [rcx + 0x220]
006C0806  48 8B 89 60 07 00 00            mov rcx, qword ptr [rcx + 0x760]
006C080D  65 48 89 0C 25 50 08 00 00      mov qword ptr gs:[0x850], rcx
006C0816  66 65 8B 0C 25 62 08 00 00      mov cx, word ptr gs:[0x862]
006C081F  66 65 89 0C 25 64 08 00 00      mov word ptr gs:[0x864], cx
006C0828  65 8A 0C 25 58 08 00 00         mov cl, byte ptr gs:[0x858]
006C0830  65 88 0C 25 5A 08 00 00         mov byte ptr gs:[0x85a], cl
006C0838  65 0F B7 04 25 68 08 00 00      movzx eax, word ptr gs:[0x868]
006C0841  66 65 39 04 25 66 08 00 00      cmp word ptr gs:[0x866], ax
006C084A  74 12                           je 0x1406c085e
006C084C  66 65 89 04 25 66 08 00 00      mov word ptr gs:[0x866], ax
006C0855  B9 48 00 00 00                  mov ecx, 0x48
006C085A  33 D2                           xor edx, edx
006C085C  0F 30                           wrmsr
006C085E  65 0F B6 14 25 58 08 00 00      movzx edx, byte ptr gs:[0x858]
006C0867  F7 C2 08 00 00 00               test edx, 8
006C086D  74 17                           je 0x1406c0886
006C086F  B8 01 00 00 00                  mov eax, 1
006C0874  33 D2                           xor edx, edx
006C0876  B9 49 00 00 00                  mov ecx, 0x49
006C087B  0F 30                           wrmsr
006C087D  65 0F B6 14 25 58 08 00 00      movzx edx, byte ptr gs:[0x858]
006C0886  F7 C2 02 00 00 00               test edx, 2
006C088C  0F 84 37 01 00 00               je 0x1406c09c9
006C0892  E8 0E 01 00 00                  call 0x1406c09a5
006C0897  48 83 C4 08                     add rsp, 8
006C089B  E8 0E 01 00 00                  call 0x1406c09ae
006C08A0  48 83 C4 08                     add rsp, 8
006C08A4  E8 EE FF FF FF                  call 0x1406c0897
006C08A9  48 83 C4 08                     add rsp, 8
006C08AD  E8 EE FF FF FF                  call 0x1406c08a0
006C08B2  48 83 C4 08                     add rsp, 8
006C08B6  E8 EE FF FF FF                  call 0x1406c08a9
006C08BB  48 83 C4 08                     add rsp, 8
006C08BF  E8 EE FF FF FF                  call 0x1406c08b2
006C08C4  48 83 C4 08                     add rsp, 8
006C08C8  E8 EE FF FF FF                  call 0x1406c08bb
006C08CD  48 83 C4 08                     add rsp, 8
006C08D1  E8 EE FF FF FF                  call 0x1406c08c4
006C08D6  48 83 C4 08                     add rsp, 8
006C08DA  E8 EE FF FF FF                  call 0x1406c08cd
006C08DF  48 83 C4 08                     add rsp, 8
006C08E3  E8 EE FF FF FF                  call 0x1406c08d6
006C08E8  48 83 C4 08                     add rsp, 8
006C08EC  E8 EE FF FF FF                  call 0x1406c08df
006C08F1  48 83 C4 08                     add rsp, 8
006C08F5  E8 EE FF FF FF                  call 0x1406c08e8
006C08FA  48 83 C4 08                     add rsp, 8
006C08FE  E8 EE FF FF FF                  call 0x1406c08f1
006C0903  48 83 C4 08                     add rsp, 8
006C0907  E8 EE FF FF FF                  call 0x1406c08fa
006C090C  48 83 C4 08                     add rsp, 8
006C0910  E8 EE FF FF FF                  call 0x1406c0903
006C0915  48 83 C4 08                     add rsp, 8
006C0919  E8 EE FF FF FF                  call 0x1406c090c
006C091E  48 83 C4 08                     add rsp, 8
006C0922  E8 EE FF FF FF                  call 0x1406c0915
006C0927  48 83 C4 08                     add rsp, 8
006C092B  E8 EE FF FF FF                  call 0x1406c091e
006C0930  48 83 C4 08                     add rsp, 8
006C0934  E8 EE FF FF FF                  call 0x1406c0927
006C0939  48 83 C4 08                     add rsp, 8
006C093D  E8 EE FF FF FF                  call 0x1406c0930
006C0942  48 83 C4 08                     add rsp, 8
006C0946  E8 EE FF FF FF                  call 0x1406c0939
006C094B  48 83 C4 08                     add rsp, 8
006C094F  E8 EE FF FF FF                  call 0x1406c0942
006C0954  48 83 C4 08                     add rsp, 8
006C0958  E8 EE FF FF FF                  call 0x1406c094b
006C095D  48 83 C4 08                     add rsp, 8
006C0961  E8 EE FF FF FF                  call 0x1406c0954
006C0966  48 83 C4 08                     add rsp, 8
006C096A  E8 EE FF FF FF                  call 0x1406c095d
006C096F  48 83 C4 08                     add rsp, 8
006C0973  E8 EE FF FF FF                  call 0x1406c0966
006C0978  48 83 C4 08                     add rsp, 8
006C097C  E8 EE FF FF FF                  call 0x1406c096f
006C0981  48 83 C4 08                     add rsp, 8
006C0985  E8 EE FF FF FF                  call 0x1406c0978
006C098A  48 83 C4 08                     add rsp, 8
006C098E  E8 EE FF FF FF                  call 0x1406c0981
006C0993  48 83 C4 08                     add rsp, 8
006C0997  E8 EE FF FF FF                  call 0x1406c098a
006C099C  48 83 C4 08                     add rsp, 8
006C09A0  E8 EE FF FF FF                  call 0x1406c0993
006C09A5  48 83 C4 08                     add rsp, 8
006C09A9  E8 EE FF FF FF                  call 0x1406c099c
006C09AE  48 83 C4 08                     add rsp, 8
006C09B2  B8 DA DA 00 00                  mov eax, 0xdada
006C09B7  65 F6 04 25 5C 08 00 00 08      test byte ptr gs:[0x85c], 8
006C09C0  74 07                           je 0x1406c09c9
006C09C2  B0 20                           mov al, 0x20
006C09C4  F3 48 0F AE E8                  incsspq rax
006C09C9  F7 C2 80 00 00 00               test edx, 0x80
006C09CF  74 08                           je 0x1406c09d9
006C09D1  0F AE E8                        lfence
006C09D4  E8 67 59 00 00                  call 0x1406c6340
006C09D9  0F AE E8                        lfence
006C09DC  65 C6 04 25 5E 08 00 00 00      mov byte ptr gs:[0x85e], 0
006C09E5  83 3D 78 68 90 00 00            cmp dword ptr [rip + 0x906878], 0
006C09EC  74 1F                           je 0x1406c0a0d
006C09EE  B9 A7 06 00 00                  mov ecx, 0x6a7
006C09F3  0F 32                           rdmsr
006C09F5  83 FA 00                        cmp edx, 0
006C09F8  74 13                           je 0x1406c0a0d
006C09FA  8B CA                           mov ecx, edx
006C09FC  23 15 62 68 90 00               and edx, dword ptr [rip + 0x906862]
006C0A02  3B D1                           cmp edx, ecx
006C0A04  74 07                           je 0x1406c0a0d
006C0A06  B9 A7 06 00 00                  mov ecx, 0x6a7
006C0A0B  0F 30                           wrmsr
006C0A0D  66 83 BD F0 00 00 00 33         cmp word ptr [rbp + 0xf0], 0x33
006C0A15  75 0D                           jne 0x1406c0a24
006C0A17  B9 02 01 00 C0                  mov ecx, 0xc0000102
006C0A1C  0F 32                           rdmsr
006C0A1E  89 45 E8                        mov dword ptr [rbp - 0x18], eax
006C0A21  89 55 EC                        mov dword ptr [rbp - 0x14], edx
006C0A24  41 F6 42 03 03                  test byte ptr [r10 + 3], 3
006C0A29  66 C7 85 80 00 00 00 00 00      mov word ptr [rbp + 0x80], 0
006C0A32  74 05                           je 0x1406c0a39
006C0A34  E8 27 CF E3 FF                  call 0x1404fd960
006C0A39  FC                              cld
006C0A3A  0F AE 5D AC                     stmxcsr dword ptr [rbp - 0x54]
006C0A3E  65 0F AE 14 25 80 01 00 00      ldmxcsr dword ptr gs:[0x180]
006C0A47  0F 29 45 F0                     movaps xmmword ptr [rbp - 0x10], xmm0
006C0A4B  0F 29 4D 00                     movaps xmmword ptr [rbp], xmm1
006C0A4F  0F 29 55 10                     movaps xmmword ptr [rbp + 0x10], xmm2
006C0A53  0F 29 5D 20                     movaps xmmword ptr [rbp + 0x20], xmm3
006C0A57  0F 29 65 30                     movaps xmmword ptr [rbp + 0x30], xmm4
006C0A5B  0F 29 6D 40                     movaps xmmword ptr [rbp + 0x40], xmm5
006C0A5F  F6 85 F0 00 00 00 01            test byte ptr [rbp + 0xf0], 1
006C0A66  74 05                           je 0x1406c0a6d
006C0A68  E8 33 B5 D5 FF                  call 0x14041bfa0
006C0A6D  F6 05 7C 61 90 00 FF            test byte ptr [rip + 0x90617c], 0xff
006C0A74  74 0C                           je 0x1406c0a82
006C0A76  F6 85 F0 00 00 00 01            test byte ptr [rbp + 0xf0], 1
006C0A7D  74 03                           je 0x1406c0a82
006C0A7F  0F 01 CB                        stac
006C0A82  8B 85 E0 00 00 00               mov eax, dword ptr [rbp + 0xe0]
006C0A88  0F 20 D1                        mov rcx, cr2
006C0A8B  F7 85 F8 00 00 00 00 02 00 00   test dword ptr [rbp + 0xf8], 0x200
006C0A95  74 01                           je 0x1406c0a98
006C0A97  FB                              sti
006C0A98  48 89 4D 50                     mov qword ptr [rbp + 0x50], rcx
006C0A9C  0F BA A5 F8 00 00 00 09         bt dword ptr [rbp + 0xf8], 9
006C0AA4  0F 83 FE 00 00 00               jae 0x1406c0ba8
006C0AAA  4C 8D 4D 80                     lea r9, [rbp - 0x80]
006C0AAE  44 8A 85 F0 00 00 00            mov r8b, byte ptr [rbp + 0xf0]
006C0AB5  41 80 E0 01                     and r8b, 1
006C0AB9  48 8B D1                        mov rdx, rcx
006C0ABC  8B C8                           mov ecx, eax
006C0ABE  D1 E8                           shr eax, 1
006C0AC0  83 E0 09                        and eax, 9
006C0AC3  88 45 AA                        mov byte ptr [rbp - 0x56], al
006C0AC6  E8 B5 E3 BB FF                  call 0x14027ee80
006C0ACB  85 C0                           test eax, eax
006C0ACD  0F 8D DB 00 00 00               jge 0x1406c0bae
006C0AD3  F6 85 F0 00 00 00 01            test byte ptr [rbp + 0xf0], 1
006C0ADA  74 56                           je 0x1406c0b32
006C0ADC  66 83 BD F0 00 00 00 33         cmp word ptr [rbp + 0xf0], 0x33
006C0AE4  75 3E                           jne 0x1406c0b24
006C0AE6  65 4C 8B 0C 25 88 01 00 00      mov r9, qword ptr gs:[0x188]
006C0AEF  41 F6 41 03 04                  test byte ptr [r9 + 3], 4
006C0AF4  74 09                           je 0x1406c0aff
006C0AF6  4D 8B 81 80 06 00 00            mov r8, qword ptr [r9 + 0x680]
006C0AFD  EB 09                           jmp 0x1406c0b08
006C0AFF  65 4C 8B 04 25 30 00 00 00      mov r8, qword ptr gs:[0x30]
006C0B08  4C 3B 45 E8                     cmp r8, qword ptr [rbp - 0x18]
006C0B0C  74 24                           je 0x1406c0b32
006C0B0E  B9 02 01 00 C0                  mov ecx, 0xc0000102
006C0B13  41 8B C0                        mov eax, r8d
006C0B16  49 C1 E8 20                     shr r8, 0x20
006C0B1A  41 8B D0                        mov edx, r8d
006C0B1D  0F 30                           wrmsr
006C0B1F  E9 A5 00 00 00                  jmp 0x1406c0bc9
006C0B24  48 8B 4D 50                     mov rcx, qword ptr [rbp + 0x50]
006C0B28  48 C1 E9 20                     shr rcx, 0x20
006C0B2C  0F 85 97 00 00 00               jne 0x1406c0bc9
006C0B32  8B C8                           mov ecx, eax
006C0B34  BA 02 00 00 00                  mov edx, 2
006C0B39  81 F9 06 00 00 D0               cmp ecx, 0xd0000006
006C0B3F  74 41                           je 0x1406c0b82
006C0B41  81 F9 05 00 00 C0               cmp ecx, 0xc0000005
006C0B47  74 1F                           je 0x1406c0b68
006C0B49  81 F9 01 00 00 80               cmp ecx, 0x80000001
006C0B4F  74 1C                           je 0x1406c0b6d
006C0B51  81 F9 FD 00 00 C0               cmp ecx, 0xc00000fd
006C0B57  74 14                           je 0x1406c0b6d
006C0B59  B9 06 00 00 C0                  mov ecx, 0xc0000006
006C0B5E  BA 03 00 00 00                  mov edx, 3
006C0B63  44 8B D8                        mov r11d, eax
006C0B66  EB 05                           jmp 0x1406c0b6d
006C0B68  B9 04 00 00 10                  mov ecx, 0x10000004
006C0B6D  4C 8B 55 50                     mov r10, qword ptr [rbp + 0x50]
006C0B71  4C 0F B6 4D AA                  movzx r9, byte ptr [rbp - 0x56]
006C0B76  4C 8B 85 E8 00 00 00            mov r8, qword ptr [rbp + 0xe8]
006C0B7D  E8 7E 4D 00 00                  call 0x1406c5900
006C0B82  44 0F 20 C0                     mov rax, cr8
006C0B86  4C 8B 95 E8 00 00 00            mov r10, qword ptr [rbp + 0xe8]
006C0B8D  4C 0F B6 4D AA                  movzx r9, byte ptr [rbp - 0x56]
006C0B92  25 FF 00 00 00                  and eax, 0xff
006C0B97  4C 8B C0                        mov r8, rax
006C0B9A  48 8B 55 50                     mov rdx, qword ptr [rbp + 0x50]
006C0B9E  B9 0A 00 00 00                  mov ecx, 0xa
006C0BA3  E8 D8 4C 00 00                  call 0x1406c5880
006C0BA8  33 C0                           xor eax, eax
006C0BAA  B0 FF                           mov al, 0xff
006C0BAC  EB D8                           jmp 0x1406c0b86
006C0BAE  80 3D 74 5A 84 00 00            cmp byte ptr [rip + 0x845a74], 0
006C0BB5  74 12                           je 0x1406c0bc9
006C0BB7  4C 8B 45 50                     mov r8, qword ptr [rbp + 0x50]
006C0BBB  48 8B 95 E8 00 00 00            mov rdx, qword ptr [rbp + 0xe8]
006C0BC2  8B C8                           mov ecx, eax
006C0BC4  E8 47 1D D9 FF                  call 0x140452910
006C0BC9  44 0F 20 C0                     mov rax, cr8
006C0BCD  0B C0                           or eax, eax
006C0BCF  89 45 A0                        mov dword ptr [rbp - 0x60], eax
006C0BD2  75 09                           jne 0x1406c0bdd
006C0BD4  B9 01 00 00 00                  mov ecx, 1
006C0BD9  44 0F 22 C1                     mov cr8, rcx
006C0BDD  48 8D 4D 80                     lea rcx, [rbp - 0x80]
006C0BE1  E8 2A AC D4 FF                  call 0x14040b810
006C0BE6  8B 4D A0                        mov ecx, dword ptr [rbp - 0x60]
006C0BE9  0B C9                           or ecx, ecx
006C0BEB  75 04                           jne 0x1406c0bf1
006C0BED  44 0F 22 C1                     mov cr8, rcx
006C0BF1  FA                              cli
006C0BF2  F6 85 F0 00 00 00 01            test byte ptr [rbp + 0xf0], 1
006C0BF9  0F 84 F5 02 00 00               je 0x1406c0ef4
006C0BFF  F6 05 EA 5F 90 00 FF            test byte ptr [rip + 0x905fea], 0xff
006C0C06  74 03                           je 0x1406c0c0b
006C0C08  0F 01 CB                        stac
006C0C0B  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006C0C14  F6 81 C2 00 00 00 03            test byte ptr [rcx + 0xc2], 3
006C0C1B  74 1B                           je 0x1406c0c38
006C0C1D  B9 01 00 00 00                  mov ecx, 1
006C0C22  44 0F 22 C1                     mov cr8, rcx
006C0C26  FB                              sti
006C0C27  E8 14 59 FF FF                  call 0x1406b6540
006C0C2C  FA                              cli
006C0C2D  B9 00 00 00 00                  mov ecx, 0
006C0C32  44 0F 22 C1                     mov cr8, rcx
006C0C36  EB D3                           jmp 0x1406c0c0b
006C0C38  E8 23 33 BA FF                  call 0x140263f60
006C0C3D  85 C0                           test eax, eax
006C0C3F  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
006C0C43  75 C6                           jne 0x1406c0c0b
006C0C45  65 F6 04 25 60 08 00 00 02      test byte ptr gs:[0x860], 2
006C0C4E  74 07                           je 0x1406c0c57
006C0C50  33 C9                           xor ecx, ecx
006C0C52  E8 69 65 D2 FF                  call 0x1403e71c0
006C0C57  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006C0C60  F7 01 00 00 00 08               test dword ptr [rcx], 0x8000000
006C0C66  74 05                           je 0x1406c0c6d
006C0C68  E8 33 10 FF FF                  call 0x1406b1ca0
006C0C6D  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006C0C76  F7 01 00 00 01 00               test dword ptr [rcx], 0x10000
006C0C7C  74 14                           je 0x1406c0c92
006C0C7E  F6 41 02 01                     test byte ptr [rcx + 2], 1
006C0C82  74 0E                           je 0x1406c0c92
006C0C84  E8 87 FA EF FF                  call 0x1405c0710
006C0C89  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006C0C92  0F AE 55 AC                     ldmxcsr dword ptr [rbp - 0x54]
006C0C96  66 83 BD 80 00 00 00 00         cmp word ptr [rbp + 0x80], 0
006C0C9E  74 05                           je 0x1406c0ca5
006C0CA0  E8 3B CC E3 FF                  call 0x1404fd8e0
006C0CA5  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006C0CAE  0F BA 61 74 16                  bt dword ptr [rcx + 0x74], 0x16
006C0CB3  73 2A                           jae 0x1406c0cdf
006C0CB5  33 C9                           xor ecx, ecx
006C0CB7  F3 48 0F 1E C9                  rdsspq rcx
006C0CBC  65 4C 8B 04 25 28 9D 00 00      mov r8, qword ptr gs:[0x9d28]
006C0CC5  49 83 C0 08                     add r8, 8
006C0CC9  49 3B C8                        cmp rcx, r8
006C0CCC  75 11                           jne 0x1406c0cdf
006C0CCE  65 48 8B 0C 25 20 9D 00 00      mov rcx, qword ptr gs:[0x9d20]
006C0CD7  F3 0F 01 29                     rstorssp dword ptr [rcx]
006C0CDB  F3 0F 01 EA                     saveprevssp
006C0CDF  65 C6 04 25 5E 08 00 00 00      mov byte ptr gs:[0x85e], 0
006C0CE8  65 0F B7 04 25 6C 08 00 00      movzx eax, word ptr gs:[0x86c]
006C0CF1  66 65 39 04 25 66 08 00 00      cmp word ptr gs:[0x866], ax
006C0CFA  74 12                           je 0x1406c0d0e
006C0CFC  66 65 89 04 25 66 08 00 00      mov word ptr gs:[0x866], ax
006C0D05  B9 48 00 00 00                  mov ecx, 0x48
006C0D0A  33 D2                           xor edx, edx
006C0D0C  0F 30                           wrmsr
006C0D0E  66 65 0F BA 34 25 58 08 00 00 02  btr word ptr gs:[0x858], 2
006C0D19  73 0E                           jae 0x1406c0d29
006C0D1B  B8 01 00 00 00                  mov eax, 1
006C0D20  33 D2                           xor edx, edx
006C0D22  B9 49 00 00 00                  mov ecx, 0x49
006C0D27  0F 30                           wrmsr
006C0D29  66 65 0F BA 34 25 58 08 00 00 05  btr word ptr gs:[0x858], 5
006C0D34  0F 83 37 01 00 00               jae 0x1406c0e71
006C0D3A  E8 0E 01 00 00                  call 0x1406c0e4d
006C0D3F  48 83 C4 08                     add rsp, 8
006C0D43  E8 0E 01 00 00                  call 0x1406c0e56
006C0D48  48 83 C4 08                     add rsp, 8
006C0D4C  E8 EE FF FF FF                  call 0x1406c0d3f
006C0D51  48 83 C4 08                     add rsp, 8
006C0D55  E8 EE FF FF FF                  call 0x1406c0d48
006C0D5A  48 83 C4 08                     add rsp, 8
006C0D5E  E8 EE FF FF FF                  call 0x1406c0d51
006C0D63  48 83 C4 08                     add rsp, 8
006C0D67  E8 EE FF FF FF                  call 0x1406c0d5a
006C0D6C  48 83 C4 08                     add rsp, 8
006C0D70  E8 EE FF FF FF                  call 0x1406c0d63
006C0D75  48 83 C4 08                     add rsp, 8
006C0D79  E8 EE FF FF FF                  call 0x1406c0d6c
006C0D7E  48 83 C4 08                     add rsp, 8
006C0D82  E8 EE FF FF FF                  call 0x1406c0d75
006C0D87  48 83 C4 08                     add rsp, 8
006C0D8B  E8 EE FF FF FF                  call 0x1406c0d7e
006C0D90  48 83 C4 08                     add rsp, 8
006C0D94  E8 EE FF FF FF                  call 0x1406c0d87
006C0D99  48 83 C4 08                     add rsp, 8
006C0D9D  E8 EE FF FF FF                  call 0x1406c0d90
006C0DA2  48 83 C4 08                     add rsp, 8
006C0DA6  E8 EE FF FF FF                  call 0x1406c0d99
006C0DAB  48 83 C4 08                     add rsp, 8
006C0DAF  E8 EE FF FF FF                  call 0x1406c0da2
006C0DB4  48 83 C4 08                     add rsp, 8
006C0DB8  E8 EE FF FF FF                  call 0x1406c0dab
006C0DBD  48 83 C4 08                     add rsp, 8
006C0DC1  E8 EE FF FF FF                  call 0x1406c0db4
006C0DC6  48 83 C4 08                     add rsp, 8
006C0DCA  E8 EE FF FF FF                  call 0x1406c0dbd
006C0DCF  48 83 C4 08                     add rsp, 8
006C0DD3  E8 EE FF FF FF                  call 0x1406c0dc6
006C0DD8  48 83 C4 08                     add rsp, 8
006C0DDC  E8 EE FF FF FF                  call 0x1406c0dcf
006C0DE1  48 83 C4 08                     add rsp, 8
006C0DE5  E8 EE FF FF FF                  call 0x1406c0dd8
006C0DEA  48 83 C4 08                     add rsp, 8
006C0DEE  E8 EE FF FF FF                  call 0x1406c0de1
006C0DF3  48 83 C4 08                     add rsp, 8
006C0DF7  E8 EE FF FF FF                  call 0x1406c0dea
006C0DFC  48 83 C4 08                     add rsp, 8
006C0E00  E8 EE FF FF FF                  call 0x1406c0df3
006C0E05  48 83 C4 08                     add rsp, 8
006C0E09  E8 EE FF FF FF                  call 0x1406c0dfc
006C0E0E  48 83 C4 08                     add rsp, 8
006C0E12  E8 EE FF FF FF                  call 0x1406c0e05
006C0E17  48 83 C4 08                     add rsp, 8
006C0E1B  E8 EE FF FF FF                  call 0x1406c0e0e
006C0E20  48 83 C4 08                     add rsp, 8
006C0E24  E8 EE FF FF FF                  call 0x1406c0e17
006C0E29  48 83 C4 08                     add rsp, 8
006C0E2D  E8 EE FF FF FF                  call 0x1406c0e20
006C0E32  48 83 C4 08                     add rsp, 8
006C0E36  E8 EE FF FF FF                  call 0x1406c0e29
006C0E3B  48 83 C4 08                     add rsp, 8
006C0E3F  E8 EE FF FF FF                  call 0x1406c0e32
006C0E44  48 83 C4 08                     add rsp, 8
006C0E48  E8 EE FF FF FF                  call 0x1406c0e3b
006C0E4D  48 83 C4 08                     add rsp, 8
006C0E51  E8 EE FF FF FF                  call 0x1406c0e44
006C0E56  48 83 C4 08                     add rsp, 8
006C0E5A  B8 DA DA 00 00                  mov eax, 0xdada
006C0E5F  65 F6 04 25 5C 08 00 00 08      test byte ptr gs:[0x85c], 8
006C0E68  74 07                           je 0x1406c0e71
006C0E6A  B0 20                           mov al, 0x20
006C0E6C  F3 48 0F AE E8                  incsspq rax
006C0E71  66 65 F7 04 25 58 08 00 00 00 01  test word ptr gs:[0x858], 0x100
006C0E7C  74 0C                           je 0x1406c0e8a
006C0E7E  33 C0                           xor eax, eax
006C0E80  33 D2                           xor edx, edx
006C0E82  B9 01 00 00 00                  mov ecx, 1
006C0E87  48 F7 F1                        div rcx
006C0E8A  0F 28 45 F0                     movaps xmm0, xmmword ptr [rbp - 0x10]
006C0E8E  0F 28 4D 00                     movaps xmm1, xmmword ptr [rbp]
006C0E92  0F 28 55 10                     movaps xmm2, xmmword ptr [rbp + 0x10]
006C0E96  0F 28 5D 20                     movaps xmm3, xmmword ptr [rbp + 0x20]
006C0E9A  0F 28 65 30                     movaps xmm4, xmmword ptr [rbp + 0x30]
006C0E9E  0F 28 6D 40                     movaps xmm5, xmmword ptr [rbp + 0x40]
006C0EA2  4C 8B 5D E0                     mov r11, qword ptr [rbp - 0x20]
006C0EA6  4C 8B 55 D8                     mov r10, qword ptr [rbp - 0x28]
006C0EAA  4C 8B 4D D0                     mov r9, qword ptr [rbp - 0x30]
006C0EAE  4C 8B 45 C8                     mov r8, qword ptr [rbp - 0x38]
006C0EB2  48 8B 55 C0                     mov rdx, qword ptr [rbp - 0x40]
006C0EB6  48 8B 4D B8                     mov rcx, qword ptr [rbp - 0x48]
006C0EBA  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
006C0EBE  48 8B E5                        mov rsp, rbp
006C0EC1  48 8B AD D8 00 00 00            mov rbp, qword ptr [rbp + 0xd8]
006C0EC8  48 81 C4 E8 00 00 00            add rsp, 0xe8
006C0ECF  F6 05 6A 09 B4 00 01            test byte ptr [rip + 0xb4096a], 1
006C0ED6  74 05                           je 0x1406c0edd
006C0ED8  E9 A3 BC 50 00                  jmp 0x140bccb80
006C0EDD  66 65 F7 04 25 58 08 00 00 00 02  test word ptr gs:[0x858], 0x200
006C0EE8  74 05                           je 0x1406c0eef
006C0EEA  0F 00 6C 24 20                  verw word ptr [rsp + 0x20]
006C0EEF  0F 01 F8                        swapgs
006C0EF2  48 CF                           iretq
006C0EF4  0F AE 55 AC                     ldmxcsr dword ptr [rbp - 0x54]
006C0EF8  0F 28 45 F0                     movaps xmm0, xmmword ptr [rbp - 0x10]
006C0EFC  0F 28 4D 00                     movaps xmm1, xmmword ptr [rbp]
006C0F00  0F 28 55 10                     movaps xmm2, xmmword ptr [rbp + 0x10]
006C0F04  0F 28 5D 20                     movaps xmm3, xmmword ptr [rbp + 0x20]
006C0F08  0F 28 65 30                     movaps xmm4, xmmword ptr [rbp + 0x30]
006C0F0C  0F 28 6D 40                     movaps xmm5, xmmword ptr [rbp + 0x40]
006C0F10  4C 8B 5D E0                     mov r11, qword ptr [rbp - 0x20]
006C0F14  4C 8B 55 D8                     mov r10, qword ptr [rbp - 0x28]
006C0F18  4C 8B 4D D0                     mov r9, qword ptr [rbp - 0x30]
006C0F1C  4C 8B 45 C8                     mov r8, qword ptr [rbp - 0x38]
006C0F20  48 8B 55 C0                     mov rdx, qword ptr [rbp - 0x40]
006C0F24  48 8B 4D B8                     mov rcx, qword ptr [rbp - 0x48]
006C0F28  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
006C0F2C  48 8B E5                        mov rsp, rbp
006C0F2F  48 8B AD D8 00 00 00            mov rbp, qword ptr [rbp + 0xd8]
006C0F36  48 81 C4 E8 00 00 00            add rsp, 0xe8
006C0F3D  48 CF                           iretq
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiPageFault(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned __int16 a5)
{
    __int64 result;
    __int64 v_cr8;
    __int64 v_r10;
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
    unsigned __int8 v_stack_m136;
    unsigned int v_stack_m140;
    unsigned __int64 v_stack_m160;
    unsigned __int16 v_stack_m60;
    unsigned __int64 v_stack_m8;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mF0;
    unsigned int v_stack_mF4;
    unsigned int v_stack_mF8;
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
    if (((v_stack_p10) & (1)) != 0) goto loc_006C07B1;
    a2 = 0;
    v_stack_m88 = 0;
    if (((*(unsigned __int8 *)(gs_base + (0 + 2136))) & (1)) != 0) goto loc_006C079A;
    goto loc_006C0A39;
loc_006C079A:
    a2 = 0;
    goto loc_006C0A39;
loc_006C07B1:
    if (((*(unsigned __int8 *)(v_rip + 11800712)) & (1)) == 0) {
    }
    if (*(unsigned __int64 *)(gs_base + (0 + 40232)) == 0) goto loc_006C07ED;
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
    if ((((unsigned int)(a2)) & (2)) == 0) goto loc_006C09C9;
    result = KiPageFault___0x265(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiPageFault___0x26E(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiPageFault___0x157(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiPageFault___0x160(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiPageFault___0x169(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiPageFault___0x172(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiPageFault___0x17B(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiPageFault___0x184(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiPageFault___0x18D(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiPageFault___0x196(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiPageFault___0x19F(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiPageFault___0x1A8(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiPageFault___0x1B1(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiPageFault___0x1BA(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiPageFault___0x1C3(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiPageFault___0x1CC(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiPageFault___0x1D5(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiPageFault___0x1DE(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiPageFault___0x1E7(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiPageFault___0x1F0(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiPageFault___0x1F9(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiPageFault___0x202(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiPageFault___0x20B(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiPageFault___0x214(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiPageFault___0x21D(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiPageFault___0x226(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiPageFault___0x22F(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiPageFault___0x238(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiPageFault___0x241(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiPageFault___0x24A(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiPageFault___0x253(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = KiPageFault___0x25C(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (8);
    result = (unsigned int)(0xDADAULL);
    if (((*(unsigned __int8 *)(gs_base + (0 + 2140))) & (8)) != 0) {
        result = 32;
    }
    if ((((unsigned int)(a2)) & (128)) != 0) {
        result = KiFlushBhbDuringTrapEntryOrExit(a1, a2, a3, a4);
    }
    *(unsigned __int8 *)(gs_base + (0 + 2142)) = 0;
    if ((*(unsigned int *)(v_rip + 9463928)) == 0) goto loc_006C0A0D;
    if (((unsigned int)(a2)) == 0) goto loc_006C0A0D;
    a2 = (unsigned int)((a2) & (*(unsigned int *)(v_rip + 9463906)));
    if (((unsigned int)(a2)) != ((unsigned int)((unsigned int)((unsigned int)(a2))))) {
        a1 = 0x6A7ULL;
    }
    if (v_stack_p10 == 51) {
        a1 = 0xC0000102ULL;
        v_stack_mF8 = (unsigned int)(result);
        v_stack_mF4 = (unsigned int)(a2);
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
    if (((*(unsigned __int8 *)(v_rip + 9462140)) & (255)) == 0) goto loc_006C0A82;
    if (((v_stack_p10) & (1)) != 0) {
    }
    if (((v_stack_p18) & (512)) != 0) {
    }
    v_stack_m90 = v_cr2;
    if (condition_is_above_or_equal) goto loc_006C0BA8;
    a3 = (unsigned __int8)((v_stack_p10) & (1));
    result = (unsigned int)(((unsigned int)(v_stack_p0)) >> (1));
    result = (unsigned int)((result) & (9));
    v_stack_m136 = (unsigned __int8)(result);
    result = MmAccessFault((unsigned int)((unsigned int)((unsigned int)(v_stack_p0))), v_cr2, a3, v_stack_m160);
    if (condition_is_greater_or_equal) goto loc_006C0BAE;
    if (((v_stack_p10) & (1)) == 0) goto loc_006C0B32;
    if (v_stack_p10 != 51) goto loc_006C0B24;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 3)) & (4)) == 0) goto loc_006C0AFF;
    goto loc_006C0B08;
loc_006C0AFF:
loc_006C0B08:
    if ((*(unsigned __int64 *)(gs_base + (0 + 48))) == v_stack_mF8) goto loc_006C0B32;
    a3 = (*(unsigned __int64 *)(gs_base + (0 + 48))) >> (32);
    goto loc_006C0BC9;
loc_006C0B24:
    a1 = (v_stack_m90) >> (32);
    if (condition_is_not_equal) goto loc_006C0BC9;
loc_006C0B32:
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int64 *)(gs_base + (0 + 48)))))))) == 0xD0000006ULL) goto loc_006C0B82;
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int64 *)(gs_base + (0 + 48)))))))) == 0xC0000005ULL) goto loc_006C0B68;
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int64 *)(gs_base + (0 + 48)))))))) == 0x80000001ULL) goto loc_006C0B6D;
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int64 *)(gs_base + (0 + 48)))))))) == 0xC00000FDULL) goto loc_006C0B6D;
    goto loc_006C0B6D;
loc_006C0B68:
loc_006C0B6D:
    result = KiExceptionDispatch((unsigned int)(0x10000004ULL), 3, v_stack_p8, v_stack_m136);
loc_006C0B82:
loc_006C0B86:
    result = (unsigned int)((v_cr8) & (255));
    result = KiBugCheckDispatch(10, v_stack_m90, result, v_stack_m136);
loc_006C0BA8:
    result = 0;
    goto loc_006C0B86;
loc_006C0BAE:
    result = 255;
    if ((*(unsigned __int8 *)(v_rip + 8673908)) != 0) {
        a3 = v_stack_m90;
        a2 = v_stack_p8;
        a1 = 255;
        result = PsWatchWorkingSet(a1, a2, a3, v_stack_m136);
    }
    result = (unsigned int)((v_cr8) | ((unsigned int)(v_cr8)));
    v_stack_m140 = (unsigned int)(result);
    if (!(condition_is_not_equal)) {
        a1 = 1;
        v_cr8 = a1;
    }
    result = KiCheckForSListAddress(v_stack_m160, a2, a3, v_stack_m136);
    a1 = (unsigned int)(((unsigned int)(v_stack_m140)) | ((unsigned int)((unsigned int)(v_stack_m140))));
    if (!(condition_is_not_equal)) {
        v_cr8 = a1;
    }
    if (((v_stack_p10) & (1)) == 0) goto loc_006C0EF4;
    if (((*(unsigned __int8 *)(v_rip + 9461738)) & (255)) != 0) {
    }
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 194)) & (3)) == 0) goto loc_006C0C38;
    result = KiInitiateUserApc(1, a2, a3, v_stack_m136);
    goto loc_006C0C0B;
loc_006C0C38:
    result = KiSynchronizeUserIsolationDomainEntry(0, a2, a3, v_stack_m136);
    if ((unsigned int)(result) != 0) goto loc_006C0C0B;
    result = v_stack_m130;
    if (((*(unsigned __int8 *)(gs_base + (0 + 2144))) & (2)) != 0) {
        a1 = 0;
        result = KiUpdateStibpPairing(a1, a2, a3, v_stack_m136);
    }
    if (((*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)))) & (0x8000000ULL)) != 0) {
        result = KiRestoreSetContextState(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, v_stack_m136);
    }
    if (((*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)))) & (0x10000ULL)) == 0) goto loc_006C0C92;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 2)) & (1)) != 0) {
        result = KiCopyCounters(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, v_stack_m136);
        a1 = *(unsigned __int64 *)(gs_base + (0 + 392));
    }
    if (v_stack_m60 != 0) {
        result = KiRestoreDebugRegisterState(a1, a2, a3, v_stack_m136);
    }
    if (v_stack_m60 >= 0) goto loc_006C0CDF;
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
    if (condition_is_above_or_equal) goto loc_006C0E71;
    result = KiPageFault___0x70D(a1, a2, a3, v_stack_m136);
    v_rsp = (v_rsp) + (8);
    result = KiPageFault___0x716(a1, a2, a3, v_stack_m136);
    v_rsp = (v_rsp) + (8);
    result = KiPageFault___0x5FF(a1, a2, a3, v_stack_m136);
    v_rsp = (v_rsp) + (8);
    result = KiPageFault___0x608(a1, a2, a3, v_stack_m136);
    v_rsp = (v_rsp) + (8);
    result = KiPageFault___0x611(a1, a2, a3, v_stack_m136);
    v_rsp = (v_rsp) + (8);
    result = KiPageFault___0x61A(a1, a2, a3, v_stack_m136);
    v_rsp = (v_rsp) + (8);
    result = KiPageFault___0x623(a1, a2, a3, v_stack_m136);
    v_rsp = (v_rsp) + (8);
    result = KiPageFault___0x62C(a1, a2, a3, v_stack_m136);
    v_rsp = (v_rsp) + (8);
    result = KiPageFault___0x635(a1, a2, a3, v_stack_m136);
    v_rsp = (v_rsp) + (8);
    result = KiPageFault___0x63E(a1, a2, a3, v_stack_m136);
    v_rsp = (v_rsp) + (8);
    result = KiPageFault___0x647(a1, a2, a3, v_stack_m136);
    v_rsp = (v_rsp) + (8);
    result = KiPageFault___0x650(a1, a2, a3, v_stack_m136);
    v_rsp = (v_rsp) + (8);
    result = KiPageFault___0x659(a1, a2, a3, v_stack_m136);
    v_rsp = (v_rsp) + (8);
    result = KiPageFault___0x662(a1, a2, a3, v_stack_m136);
    v_rsp = (v_rsp) + (8);
    result = KiPageFault___0x66B(a1, a2, a3, v_stack_m136);
    v_rsp = (v_rsp) + (8);
    result = KiPageFault___0x674(a1, a2, a3, v_stack_m136);
    v_rsp = (v_rsp) + (8);
    result = KiPageFault___0x67D(a1, a2, a3, v_stack_m136);
    v_rsp = (v_rsp) + (8);
    result = KiPageFault___0x686(a1, a2, a3, v_stack_m136);
    v_rsp = (v_rsp) + (8);
    result = KiPageFault___0x68F(a1, a2, a3, v_stack_m136);
    v_rsp = (v_rsp) + (8);
    result = KiPageFault___0x698(a1, a2, a3, v_stack_m136);
    v_rsp = (v_rsp) + (8);
    result = KiPageFault___0x6A1(a1, a2, a3, v_stack_m136);
    v_rsp = (v_rsp) + (8);
    result = KiPageFault___0x6AA(a1, a2, a3, v_stack_m136);
    v_rsp = (v_rsp) + (8);
    result = KiPageFault___0x6B3(a1, a2, a3, v_stack_m136);
    v_rsp = (v_rsp) + (8);
    result = KiPageFault___0x6BC(a1, a2, a3, v_stack_m136);
    v_rsp = (v_rsp) + (8);
    result = KiPageFault___0x6C5(a1, a2, a3, v_stack_m136);
    v_rsp = (v_rsp) + (8);
    result = KiPageFault___0x6CE(a1, a2, a3, v_stack_m136);
    v_rsp = (v_rsp) + (8);
    result = KiPageFault___0x6D7(a1, a2, a3, v_stack_m136);
    v_rsp = (v_rsp) + (8);
    result = KiPageFault___0x6E0(a1, a2, a3, v_stack_m136);
    v_rsp = (v_rsp) + (8);
    result = KiPageFault___0x6E9(a1, a2, a3, v_stack_m136);
    v_rsp = (v_rsp) + (8);
    result = KiPageFault___0x6F2(a1, a2, a3, v_stack_m136);
    v_rsp = (v_rsp) + (8);
    result = KiPageFault___0x6FB(a1, a2, a3, v_stack_m136);
    v_rsp = (v_rsp) + (8);
    result = KiPageFault___0x704(a1, a2, a3, v_stack_m136);
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
    if (((*(unsigned __int8 *)(v_rip + 11798890)) & (1)) == 0) goto loc_006C0EDD;
loc_006C0EDD:
    if (((*(unsigned __int16 *)(gs_base + (0 + 2136))) & (512)) != 0) {
    }
loc_006C0EF4:
    v_rsp = (v_stack_m8) + (232);
    return v_stack_m130;
}
```

## 5. (Beta) C Style

```c
int64_t KiPageFault(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint16_t Arg5)
{
    int64_t result;
    int64_t v_cr8;
    int64_t local_r10;
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
    uint8_t v_stack_m136;
    uint32_t v_stack_m140;
    uint64_t v_stack_m160;
    uint16_t v_stack_m60;
    uint64_t v_stack_m8;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mF0;
    uint32_t v_stack_mF4;
    uint32_t v_stack_mF8;
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
    if (((v_stack_p10) & (1)) != 0) goto loc_006C07B1;
    Arg2 = 0;
    v_stack_m88 = 0;
    if (((*(uint8_t *)(gs_base + (0 + 0x858))) & (1)) != 0) goto loc_006C079A;
    goto loc_006C0A39;
loc_006C079A:
    Arg2 = 0;
    goto loc_006C0A39;
loc_006C07B1:
    if (((*(uint8_t *)(v_rip + 0xB41088)) & (1)) == 0) {
    }
    if (*(uint64_t *)(gs_base + (0 + 0x9D28)) == 0) goto loc_006C07ED;
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
    if ((((uint32_t)(Arg2)) & (2)) == 0) goto loc_006C09C9;
    result = KiPageFault___0x265(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiPageFault___0x26E(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiPageFault___0x157(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiPageFault___0x160(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiPageFault___0x169(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiPageFault___0x172(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiPageFault___0x17B(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiPageFault___0x184(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiPageFault___0x18D(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiPageFault___0x196(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiPageFault___0x19F(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiPageFault___0x1A8(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiPageFault___0x1B1(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiPageFault___0x1BA(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiPageFault___0x1C3(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiPageFault___0x1CC(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiPageFault___0x1D5(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiPageFault___0x1DE(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiPageFault___0x1E7(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiPageFault___0x1F0(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiPageFault___0x1F9(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiPageFault___0x202(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiPageFault___0x20B(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiPageFault___0x214(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiPageFault___0x21D(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiPageFault___0x226(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiPageFault___0x22F(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiPageFault___0x238(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiPageFault___0x241(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiPageFault___0x24A(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiPageFault___0x253(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = KiPageFault___0x25C(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (8);
    result = (uint32_t)(0xDADAULL);
    if (((*(uint8_t *)(gs_base + (0 + 0x85C))) & (8)) != 0) {
        result = 32;
    }
    if ((((uint32_t)(Arg2)) & (128)) != 0) {
        result = KiFlushBhbDuringTrapEntryOrExit(Arg1, Arg2, Arg3, Arg4);
    }
    *(uint8_t *)(gs_base + (0 + 0x85E)) = 0;
    if ((*(uint32_t *)(v_rip + 0x906878)) == 0) goto loc_006C0A0D;
    if (((uint32_t)(Arg2)) == 0) goto loc_006C0A0D;
    Arg2 = (uint32_t)((Arg2) & (*(uint32_t *)(v_rip + 0x906862)));
    if (((uint32_t)(Arg2)) != ((uint32_t)((uint32_t)((uint32_t)(Arg2))))) {
        Arg1 = 0x6A7ULL;
    }
    if (v_stack_p10 == 51) {
        Arg1 = 0xC0000102ULL;
        v_stack_mF8 = (uint32_t)(result);
        v_stack_mF4 = (uint32_t)(Arg2);
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
    if (((*(uint8_t *)(v_rip + 0x90617C)) & (255)) == 0) goto loc_006C0A82;
    if (((v_stack_p10) & (1)) != 0) {
    }
    if (((v_stack_p18) & (512)) != 0) {
    }
    v_stack_m90 = v_cr2;
    if (condition_is_above_or_equal) goto loc_006C0BA8;
    Arg3 = (uint8_t)((v_stack_p10) & (1));
    result = (uint32_t)(((uint32_t)(v_stack_p0)) >> (1));
    result = (uint32_t)((result) & (9));
    v_stack_m136 = (uint8_t)(result);
    result = MmAccessFault((uint32_t)((uint32_t)((uint32_t)(v_stack_p0))), v_cr2, Arg3, v_stack_m160);
    if (condition_is_greater_or_equal) goto loc_006C0BAE;
    if (((v_stack_p10) & (1)) == 0) goto loc_006C0B32;
    if (v_stack_p10 != 51) goto loc_006C0B24;
    if (((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x3)) & (4)) == 0) goto loc_006C0AFF;
    goto loc_006C0B08;
loc_006C0AFF:
loc_006C0B08:
    if ((*(uint64_t *)(gs_base + (0 + 0x30))) == v_stack_mF8) goto loc_006C0B32;
    Arg3 = (*(uint64_t *)(gs_base + (0 + 0x30))) >> (32);
    goto loc_006C0BC9;
loc_006C0B24:
    Arg1 = (v_stack_m90) >> (32);
    if (condition_is_not_equal) goto loc_006C0BC9;
loc_006C0B32:
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint64_t *)(gs_base + (0 + 0x30)))))))) == 0xD0000006ULL) goto loc_006C0B82;
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint64_t *)(gs_base + (0 + 0x30)))))))) == 0xC0000005ULL) goto loc_006C0B68;
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint64_t *)(gs_base + (0 + 0x30)))))))) == 0x80000001ULL) goto loc_006C0B6D;
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint64_t *)(gs_base + (0 + 0x30)))))))) == 0xC00000FDULL) goto loc_006C0B6D;
    goto loc_006C0B6D;
loc_006C0B68:
loc_006C0B6D:
    result = KiExceptionDispatch((uint32_t)(0x10000004ULL), 3, v_stack_p8, v_stack_m136);
loc_006C0B82:
loc_006C0B86:
    result = (uint32_t)((v_cr8) & (255));
    result = KiBugCheckDispatch(10, v_stack_m90, result, v_stack_m136);
loc_006C0BA8:
    result = 0;
    goto loc_006C0B86;
loc_006C0BAE:
    result = 255;
    if ((*(uint8_t *)(v_rip + 0x845A74)) != 0) {
        Arg3 = v_stack_m90;
        Arg2 = v_stack_p8;
        Arg1 = 255;
        result = PsWatchWorkingSet(Arg1, Arg2, Arg3, v_stack_m136);
    }
    result = (uint32_t)((v_cr8) | ((uint32_t)(v_cr8)));
    v_stack_m140 = (uint32_t)(result);
    if (!(condition_is_not_equal)) {
        Arg1 = 1;
        v_cr8 = Arg1;
    }
    result = KiCheckForSListAddress(v_stack_m160, Arg2, Arg3, v_stack_m136);
    Arg1 = (uint32_t)(((uint32_t)(v_stack_m140)) | ((uint32_t)((uint32_t)(v_stack_m140))));
    if (!(condition_is_not_equal)) {
        v_cr8 = Arg1;
    }
    if (((v_stack_p10) & (1)) == 0) goto loc_006C0EF4;
    if (((*(uint8_t *)(v_rip + 0x905FEA)) & (255)) != 0) {
    }
    if (((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xC2)) & (3)) == 0) goto loc_006C0C38;
    result = KiInitiateUserApc(1, Arg2, Arg3, v_stack_m136);
    goto loc_006C0C0B;
loc_006C0C38:
    result = KiSynchronizeUserIsolationDomainEntry(0, Arg2, Arg3, v_stack_m136);
    if ((uint32_t)(result) != 0) goto loc_006C0C0B;
    result = v_stack_m130;
    if (((*(uint8_t *)(gs_base + (0 + 0x860))) & (2)) != 0) {
        Arg1 = 0;
        result = KiUpdateStibpPairing(Arg1, Arg2, Arg3, v_stack_m136);
    }
    if (((*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)))) & (0x8000000ULL)) != 0) {
        result = KiRestoreSetContextState(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, Arg3, v_stack_m136);
    }
    if (((*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)))) & (0x10000ULL)) == 0) goto loc_006C0C92;
    if (((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x2)) & (1)) != 0) {
        result = KiCopyCounters(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, Arg3, v_stack_m136);
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x188));
    }
    if (v_stack_m60 != 0) {
        result = KiRestoreDebugRegisterState(Arg1, Arg2, Arg3, v_stack_m136);
    }
    if (v_stack_m60 >= 0) goto loc_006C0CDF;
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
    if (condition_is_above_or_equal) goto loc_006C0E71;
    result = KiPageFault___0x70D(Arg1, Arg2, Arg3, v_stack_m136);
    local_rsp = (local_rsp) + (8);
    result = KiPageFault___0x716(Arg1, Arg2, Arg3, v_stack_m136);
    local_rsp = (local_rsp) + (8);
    result = KiPageFault___0x5FF(Arg1, Arg2, Arg3, v_stack_m136);
    local_rsp = (local_rsp) + (8);
    result = KiPageFault___0x608(Arg1, Arg2, Arg3, v_stack_m136);
    local_rsp = (local_rsp) + (8);
    result = KiPageFault___0x611(Arg1, Arg2, Arg3, v_stack_m136);
    local_rsp = (local_rsp) + (8);
    result = KiPageFault___0x61A(Arg1, Arg2, Arg3, v_stack_m136);
    local_rsp = (local_rsp) + (8);
    result = KiPageFault___0x623(Arg1, Arg2, Arg3, v_stack_m136);
    local_rsp = (local_rsp) + (8);
    result = KiPageFault___0x62C(Arg1, Arg2, Arg3, v_stack_m136);
    local_rsp = (local_rsp) + (8);
    result = KiPageFault___0x635(Arg1, Arg2, Arg3, v_stack_m136);
    local_rsp = (local_rsp) + (8);
    result = KiPageFault___0x63E(Arg1, Arg2, Arg3, v_stack_m136);
    local_rsp = (local_rsp) + (8);
    result = KiPageFault___0x647(Arg1, Arg2, Arg3, v_stack_m136);
    local_rsp = (local_rsp) + (8);
    result = KiPageFault___0x650(Arg1, Arg2, Arg3, v_stack_m136);
    local_rsp = (local_rsp) + (8);
    result = KiPageFault___0x659(Arg1, Arg2, Arg3, v_stack_m136);
    local_rsp = (local_rsp) + (8);
    result = KiPageFault___0x662(Arg1, Arg2, Arg3, v_stack_m136);
    local_rsp = (local_rsp) + (8);
    result = KiPageFault___0x66B(Arg1, Arg2, Arg3, v_stack_m136);
    local_rsp = (local_rsp) + (8);
    result = KiPageFault___0x674(Arg1, Arg2, Arg3, v_stack_m136);
    local_rsp = (local_rsp) + (8);
    result = KiPageFault___0x67D(Arg1, Arg2, Arg3, v_stack_m136);
    local_rsp = (local_rsp) + (8);
    result = KiPageFault___0x686(Arg1, Arg2, Arg3, v_stack_m136);
    local_rsp = (local_rsp) + (8);
    result = KiPageFault___0x68F(Arg1, Arg2, Arg3, v_stack_m136);
    local_rsp = (local_rsp) + (8);
    result = KiPageFault___0x698(Arg1, Arg2, Arg3, v_stack_m136);
    local_rsp = (local_rsp) + (8);
    result = KiPageFault___0x6A1(Arg1, Arg2, Arg3, v_stack_m136);
    local_rsp = (local_rsp) + (8);
    result = KiPageFault___0x6AA(Arg1, Arg2, Arg3, v_stack_m136);
    local_rsp = (local_rsp) + (8);
    result = KiPageFault___0x6B3(Arg1, Arg2, Arg3, v_stack_m136);
    local_rsp = (local_rsp) + (8);
    result = KiPageFault___0x6BC(Arg1, Arg2, Arg3, v_stack_m136);
    local_rsp = (local_rsp) + (8);
    result = KiPageFault___0x6C5(Arg1, Arg2, Arg3, v_stack_m136);
    local_rsp = (local_rsp) + (8);
    result = KiPageFault___0x6CE(Arg1, Arg2, Arg3, v_stack_m136);
    local_rsp = (local_rsp) + (8);
    result = KiPageFault___0x6D7(Arg1, Arg2, Arg3, v_stack_m136);
    local_rsp = (local_rsp) + (8);
    result = KiPageFault___0x6E0(Arg1, Arg2, Arg3, v_stack_m136);
    local_rsp = (local_rsp) + (8);
    result = KiPageFault___0x6E9(Arg1, Arg2, Arg3, v_stack_m136);
    local_rsp = (local_rsp) + (8);
    result = KiPageFault___0x6F2(Arg1, Arg2, Arg3, v_stack_m136);
    local_rsp = (local_rsp) + (8);
    result = KiPageFault___0x6FB(Arg1, Arg2, Arg3, v_stack_m136);
    local_rsp = (local_rsp) + (8);
    result = KiPageFault___0x704(Arg1, Arg2, Arg3, v_stack_m136);
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
    if (((*(uint8_t *)(v_rip + 0xB4096A)) & (1)) == 0) goto loc_006C0EDD;
loc_006C0EDD:
    if (((*(uint16_t *)(gs_base + (0 + 0x858))) & (512)) != 0) {
    }
loc_006C0EF4:
    local_rsp = (v_stack_m8) + (232);
    return v_stack_m130;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006C0740&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
