# PopInitializeHeteroProcessors

- RVA: `0x00A53570`–`0x00A5391F` (길이 `943` bytes)
- VA: `0x0000000140A53570`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B0E24`
- 디코드: `253`개 명령, `943/943` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **29**; 고유 호출 대상: **23**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **26**

### Outgoing calls
- `0x00A535F0` → [KeQueryActiveProcessorCountEx](../../text/24/KeQueryActiveProcessorCountEx_function_00249EF0.md) (function, `0x00249EF0`)
- `0x00A5364A` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00A5364F` → [PpmHeteroComputeRelativePerformance](../A7/PpmHeteroComputeRelativePerformance_function_00A7E038.md) (function, `0x00A7E038`)
- `0x00A53654` → [PpmHeteroUpdateHgsConfiguration](../../text/3B/PpmHeteroUpdateHgsConfiguration_function_003BF344.md) (function, `0x003BF344`)
- `0x00A5365F` → [PpmHeteroDetectHgsCores](../../text/48/PpmHeteroDetectHgsCores_function_0048E980.md) (function, `0x0048E980`)
- `0x00A5367B` → [PopIsSimulatedArchitecturalHeteroPresent](../AD/PopIsSimulatedArchitecturalHeteroPresent_function_00AD2FA8.md) (function, `0x00AD2FA8`)
- `0x00A5368E` → [PpmHeteroDetectFavoredCores](../AD/PpmHeteroDetectFavoredCores_function_00AD1760.md) (function, `0x00AD1760`)
- `0x00A5369E` → [KeDetectHeterogeneousSets](../74/KeDetectHeterogeneousSets_function_00744FA8.md) (function, `0x00744FA8`)
- `0x00A536AE` → [PpmHeteroDetectFavoredCores](../AD/PpmHeteroDetectFavoredCores_function_00AD1760.md) (function, `0x00AD1760`)
- `0x00A536D6` → [PpmHeteroDetectFavoredCores](../AD/PpmHeteroDetectFavoredCores_function_00AD1760.md) (function, `0x00AD1760`)
- `0x00A5372E` → [RtlCompareMemory](../../text/6B/RtlCompareMemory_function_006BA670.md) (function, `0x006BA670`)
- `0x00A5374A` → [RtlCompareMemory](../../text/6B/RtlCompareMemory_function_006BA670.md) (function, `0x006BA670`)
- `0x00A53796` → [PpmHeteroReevaluateMultiCoreFeatures](../../text/4D/PpmHeteroReevaluateMultiCoreFeatures_function_004DFE74.md) (function, `0x004DFE74`)
- `0x00A5379B` → [PpmHeteroComputeMinRelativePerformane](PpmHeteroComputeMinRelativePerformane_function_00A56A90.md) (function, `0x00A56A90`)
- `0x00A537AF` → [PopConfigureHeteroPolicies](../A3/PopConfigureHeteroPolicies_function_00A35B30.md) (function, `0x00A35B30`)
- `0x00A537D6` → [KeConfigureHeteroProcessors](../../text/42/KeConfigureHeteroProcessors_function_00427338.md) (function, `0x00427338`)
- `0x00A5380B` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00A53819` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00A53827` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00A5384D` → [PopHeteroCapabilityDeepCopy](../A9/PopHeteroCapabilityDeepCopy_function_00A90B6C.md) (function, `0x00A90B6C`)
- `0x00A53857` → [PpmIdleEnableIdleDurationExpirationTimeout](../../text/4B/PpmIdleEnableIdleDurationExpirationTimeout_function_004B2C8C.md) (function, `0x004B2C8C`)
- `0x00A53896` → [KeNotifyHeteroParkingPolicyChange](../AA/KeNotifyHeteroParkingPolicyChange_function_00AA3EA4.md) (function, `0x00AA3EA4`)
- `0x00A538B3` → [PpmHeteroGetHgsPlusParkingEnablementStatus](../../text/4B/PpmHeteroGetHgsPlusParkingEnablementStatus_function_004B2680.md) (function, `0x004B2680`)
- `0x00A538C5` → [Feature_UnparkPCoresOnUnimportantUtility__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_UnparkPCoresOnUnimportantUtility__private_IsEnabledDeviceUsageNoInline_function_004F4E1C.md) (function, `0x004F4E1C`)
- `0x00A538CE` → [PopGetUnparkOnUnimportantUtilityEnablementStatus](../../pagelk/B5/PopGetUnparkOnUnimportantUtilityEnablementStatus_function_00B5B008.md) (function, `0x00B5B008`)
- `0x00A538D9` → [Feature_UnparkPCoresOnUnimportantUtility__private_GetVariant](../../text/5D/Feature_UnparkPCoresOnUnimportantUtility__private_GetVariant_function_005D9444.md) (function, `0x005D9444`)
- `0x00A538E4` → [PpmEventHeteroConfigUpdate](../A7/PpmEventHeteroConfigUpdate_function_00A77430.md) (function, `0x00A77430`)
- `0x00A538EB` → [PpmEventHeteroPolicy](../A9/PpmEventHeteroPolicy_function_00A97794.md) (function, `0x00A97794`)
- `0x00A538F2` → [PpmEventTraceHeteroSets](../../text/42/PpmEventTraceHeteroSets_function_00426DB4.md) (function, `0x00426DB4`)

### Direct callers
- [PpmReapplyPerfPolicy](PpmReapplyPerfPolicy_function_00A53148.md) at `0x00A531A9`
- [PoInitSystem](../../init/C7/PoInitSystem_function_00C72358.md) at `0x00C72E16`

### Static image references
- `0x00A5358C` → RVA `0x00FC72F0` (`ALMOSTRO`; read)
- `0x00A535A6` → RVA `0x00F07798` (`.data`; read)
- `0x00A535B8` → RVA `0x00F077A0` (`.data`; read)
- `0x00A535C1` → RVA `0x00F07788` (`.data`; read)
- `0x00A535CA` → RVA `0x00F07790` (`.data`; read)
- `0x00A535D3` → RVA `0x00F07780` (`.data`; read)
- `0x00A535DC` → RVA `0x00FC6FAC` (`ALMOSTRO`; read)
- `0x00A535E5` → RVA `0x00FC6ADC` (`ALMOSTRO`; read)
- `0x00A535FB` → RVA `0x00FC6AED` (`ALMOSTRO`; read)
- `0x00A5360E` → RVA `0x00FC6DA8` (`ALMOSTRO`; read)
- `0x00A53633` → RVA `0x00E0B804` (`.data`; read)
- `0x00A536FB` → RVA `0x00FC6B40` (`ALMOSTRO`; read)
- `0x00A53708` → RVA `0x00FC6BC8` (`ALMOSTRO`; read)
- `0x00A5378E` → RVA `0x00FC5003` (`ALMOSTRO`; read)
- `0x00A537A0` → RVA `0x00E0B800` (`.data`; read)
- `0x00A537C1` → RVA `0x00FC6B6F` (`ALMOSTRO`; read)
- `0x00A537E9` → RVA `0x00FC6B40` (`ALMOSTRO`; write)
- `0x00A5385C` → RVA `0x00FC6B6C` (`ALMOSTRO`; write)
- `0x00A53874` → RVA `0x00FC5038` (`ALMOSTRO`; write)
- `0x00A53880` → RVA `0x00FC5274` (`ALMOSTRO`; read)
- `0x00A5389B` → RVA `0x00FC5194` (`ALMOSTRO`; read)
- `0x00A538AD` → RVA `0x00FC6CD4` (`ALMOSTRO`; write)
- `0x00A538B8` → RVA `0x00FC6A86` (`ALMOSTRO`; write)
- `0x00A538BE` → RVA `0x00F09168` (`.data`; write)
- `0x00A538DE` → RVA `0x00E678A0` (`.data`; write)
- `0x00A538F7` → RVA `0x00FC6B6F` (`ALMOSTRO`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **17**
  - `0x00A535F0` → [KeQueryActiveProcessorCountEx](../../text/24/KeQueryActiveProcessorCountEx_function_00249EF0.md) (`PAGE` → `.text`)
  - `0x00A5364A` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00A53654` → [PpmHeteroUpdateHgsConfiguration](../../text/3B/PpmHeteroUpdateHgsConfiguration_function_003BF344.md) (`PAGE` → `.text`)
  - `0x00A5365F` → [PpmHeteroDetectHgsCores](../../text/48/PpmHeteroDetectHgsCores_function_0048E980.md) (`PAGE` → `.text`)
  - `0x00A5372E` → [RtlCompareMemory](../../text/6B/RtlCompareMemory_function_006BA670.md) (`PAGE` → `.text`)
  - `0x00A5374A` → [RtlCompareMemory](../../text/6B/RtlCompareMemory_function_006BA670.md) (`PAGE` → `.text`)
  - `0x00A53796` → [PpmHeteroReevaluateMultiCoreFeatures](../../text/4D/PpmHeteroReevaluateMultiCoreFeatures_function_004DFE74.md) (`PAGE` → `.text`)
  - `0x00A537D6` → [KeConfigureHeteroProcessors](../../text/42/KeConfigureHeteroProcessors_function_00427338.md) (`PAGE` → `.text`)
  - `0x00A5380B` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00A53819` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00A53827` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00A53857` → [PpmIdleEnableIdleDurationExpirationTimeout](../../text/4B/PpmIdleEnableIdleDurationExpirationTimeout_function_004B2C8C.md) (`PAGE` → `.text`)
  - `0x00A538B3` → [PpmHeteroGetHgsPlusParkingEnablementStatus](../../text/4B/PpmHeteroGetHgsPlusParkingEnablementStatus_function_004B2680.md) (`PAGE` → `.text`)
  - `0x00A538C5` → [Feature_UnparkPCoresOnUnimportantUtility__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_UnparkPCoresOnUnimportantUtility__private_IsEnabledDeviceUsageNoInline_function_004F4E1C.md) (`PAGE` → `.text`)
  - `0x00A538CE` → [PopGetUnparkOnUnimportantUtilityEnablementStatus](../../pagelk/B5/PopGetUnparkOnUnimportantUtilityEnablementStatus_function_00B5B008.md) (`PAGE` → `PAGELK`)
  - `0x00A538D9` → [Feature_UnparkPCoresOnUnimportantUtility__private_GetVariant](../../text/5D/Feature_UnparkPCoresOnUnimportantUtility__private_GetVariant_function_005D9444.md) (`PAGE` → `.text`)
  - `0x00A538F2` → [PpmEventTraceHeteroSets](../../text/42/PpmEventTraceHeteroSets_function_00426DB4.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A53570  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00A53575  48 89 6C 24 18                  mov qword ptr [rsp + 0x18], rbp
00A5357A  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00A5357F  57                              push rdi
00A53580  41 54                           push r12
00A53582  41 55                           push r13
00A53584  41 56                           push r14
00A53586  41 57                           push r15
00A53588  48 83 EC 20                     sub rsp, 0x20
00A5358C  48 8B 35 5D 3D 57 00            mov rsi, qword ptr [rip + 0x573d5d]
00A53593  45 33 E4                        xor r12d, r12d
00A53596  44 8A E9                        mov r13b, cl
00A53599  48 85 F6                        test rsi, rsi
00A5359C  75 08                           jne 0x140a535a6
00A5359E  45 8A F4                        mov r14b, r12b
00A535A1  E9 58 03 00 00                  jmp 0x140a538fe
00A535A6  4C 39 25 EB 41 4B 00            cmp qword ptr [rip + 0x4b41eb], r12
00A535AD  BB 01 00 00 00                  mov ebx, 1
00A535B2  41 0F B6 EC                     movzx ebp, r12b
00A535B6  75 2D                           jne 0x140a535e5
00A535B8  4C 39 25 E1 41 4B 00            cmp qword ptr [rip + 0x4b41e1], r12
00A535BF  75 24                           jne 0x140a535e5
00A535C1  4C 39 25 C0 41 4B 00            cmp qword ptr [rip + 0x4b41c0], r12
00A535C8  75 1B                           jne 0x140a535e5
00A535CA  4C 39 25 BF 41 4B 00            cmp qword ptr [rip + 0x4b41bf], r12
00A535D1  75 12                           jne 0x140a535e5
00A535D3  4C 39 25 A6 41 4B 00            cmp qword ptr [rip + 0x4b41a6], r12
00A535DA  75 09                           jne 0x140a535e5
00A535DC  44 39 25 C9 39 57 00            cmp dword ptr [rip + 0x5739c9], r12d
00A535E3  74 16                           je 0x140a535fb
00A535E5  44 38 25 F0 34 57 00            cmp byte ptr [rip + 0x5734f0], r12b
00A535EC  74 0D                           je 0x140a535fb
00A535EE  33 C9                           xor ecx, ecx
00A535F0  E8 FB 68 7F FF                  call 0x140249ef0
00A535F5  83 F8 02                        cmp eax, 2
00A535F8  0F 43 EB                        cmovae ebp, ebx
00A535FB  44 38 25 EB 34 57 00            cmp byte ptr [rip + 0x5734eb], r12b
00A53602  74 05                           je 0x140a53609
00A53604  40 8A EB                        mov bpl, bl
00A53607  EB 05                           jmp 0x140a5360e
00A53609  40 84 ED                        test bpl, bpl
00A5360C  74 0C                           je 0x140a5361a
00A5360E  44 39 25 93 37 57 00            cmp dword ptr [rip + 0x573793], r12d
00A53615  44 8A FB                        mov r15b, bl
00A53618  74 03                           je 0x140a5361d
00A5361A  45 8A FC                        mov r15b, r12b
00A5361D  41 BE 06 00 00 00               mov r14d, 6
00A53623  45 84 ED                        test r13b, r13b
00A53626  0F 84 32 01 00 00               je 0x140a5375e
00A5362C  44 8B 06                        mov r8d, dword ptr [rsi]
00A5362F  48 8D 4E 18                     lea rcx, [rsi + 0x18]
00A53633  8B 05 CB 81 3B 00               mov eax, dword ptr [rip + 0x3b81cb]
00A53639  33 D2                           xor edx, edx
00A5363B  89 46 04                        mov dword ptr [rsi + 4], eax
00A5363E  44 0F AF 05 BE 81 3B 00         imul r8d, dword ptr [rip + 0x3b81be]
00A53646  49 C1 E0 02                     shl r8, 2
00A5364A  E8 F1 35 C7 FF                  call 0x1406c6c40
00A5364F  E8 E4 A9 02 00                  call 0x140a7e038
00A53654  E8 EB BC 96 FF                  call 0x1403bf344
00A53659  48 8B CE                        mov rcx, rsi
00A5365C  41 8B FC                        mov edi, r12d
00A5365F  E8 1C B3 A3 FF                  call 0x14048e980
00A53664  0F B6 C0                        movzx eax, al
00A53667  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
00A5366B  85 C0                           test eax, eax
00A5366D  74 09                           je 0x140a53678
00A5366F  41 8D 7E FF                     lea edi, [r14 - 1]
00A53673  E9 83 00 00 00                  jmp 0x140a536fb
00A53678  48 8B CE                        mov rcx, rsi
00A5367B  E8 28 F9 07 00                  call 0x140ad2fa8
00A53680  0F B6 C0                        movzx eax, al
00A53683  48 8B CE                        mov rcx, rsi
00A53686  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
00A5368A  85 C0                           test eax, eax
00A5368C  74 10                           je 0x140a5369e
00A5368E  E8 CD E0 07 00                  call 0x140ad1760
00A53693  F6 D8                           neg al
00A53695  1B FF                           sbb edi, edi
00A53697  83 E7 05                        and edi, 5
00A5369A  03 FB                           add edi, ebx
00A5369C  EB 5D                           jmp 0x140a536fb
00A5369E  E8 05 19 CF FF                  call 0x140744fa8
00A536A3  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
00A536A7  48 8B CE                        mov rcx, rsi
00A536AA  85 C0                           test eax, eax
00A536AC  74 28                           je 0x140a536d6
00A536AE  E8 AD E0 07 00                  call 0x140ad1760
00A536B3  84 C0                           test al, al
00A536B5  74 05                           je 0x140a536bc
00A536B7  41 8B FE                        mov edi, r14d
00A536BA  EB 3F                           jmp 0x140a536fb
00A536BC  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
00A536C5  BF 02 00 00 00                  mov edi, 2
00A536CA  38 98 8D 00 00 00               cmp byte ptr [rax + 0x8d], bl
00A536D0  41 0F 44 FE                     cmove edi, r14d
00A536D4  EB 25                           jmp 0x140a536fb
00A536D6  E8 85 E0 07 00                  call 0x140ad1760
00A536DB  0F B6 C0                        movzx eax, al
00A536DE  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
00A536E2  85 C0                           test eax, eax
00A536E4  74 07                           je 0x140a536ed
00A536E6  BF 03 00 00 00                  mov edi, 3
00A536EB  EB 0E                           jmp 0x140a536fb
00A536ED  45 84 FF                        test r15b, r15b
00A536F0  74 09                           je 0x140a536fb
00A536F2  89 5C 24 58                     mov dword ptr [rsp + 0x58], ebx
00A536F6  BF 04 00 00 00                  mov edi, 4
00A536FB  3B 3D 3F 34 57 00               cmp edi, dword ptr [rip + 0x57343f]
00A53701  74 05                           je 0x140a53708
00A53703  44 8A F3                        mov r14b, bl
00A53706  EB 7C                           jmp 0x140a53784
00A53708  48 8B 15 B9 34 57 00            mov rdx, qword ptr [rip + 0x5734b9]
00A5370F  48 8D 4E 18                     lea rcx, [rsi + 0x18]
00A53713  45 8A F4                        mov r14b, r12b
00A53716  48 83 C2 18                     add rdx, 0x18
00A5371A  44 8B 66 04                     mov r12d, dword ptr [rsi + 4]
00A5371E  41 8B DC                        mov ebx, r12d
00A53721  4D 03 E4                        add r12, r12
00A53724  0F AF 1E                        imul ebx, dword ptr [rsi]
00A53727  48 C1 E3 02                     shl rbx, 2
00A5372B  4C 8B C3                        mov r8, rbx
00A5372E  E8 3D 6F C6 FF                  call 0x1406ba670
00A53733  48 3B C3                        cmp rax, rbx
00A53736  75 1C                           jne 0x140a53754
00A53738  48 8B 15 89 34 57 00            mov rdx, qword ptr [rip + 0x573489]
00A5373F  4D 8B C4                        mov r8, r12
00A53742  48 8B 4E 10                     mov rcx, qword ptr [rsi + 0x10]
00A53746  48 8B 52 10                     mov rdx, qword ptr [rdx + 0x10]
00A5374A  E8 21 6F C6 FF                  call 0x1406ba670
00A5374F  49 3B C4                        cmp rax, r12
00A53752  74 28                           je 0x140a5377c
00A53754  BB 01 00 00 00                  mov ebx, 1
00A53759  44 8A F3                        mov r14b, bl
00A5375C  EB 23                           jmp 0x140a53781
00A5375E  8B 3D DC 33 57 00               mov edi, dword ptr [rip + 0x5733dc]
00A53764  41 8B C4                        mov eax, r12d
00A53767  48 8B 35 5A 34 57 00            mov rsi, qword ptr [rip + 0x57345a]
00A5376E  85 FF                           test edi, edi
00A53770  45 8A F4                        mov r14b, r12b
00A53773  0F 95 C0                        setne al
00A53776  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
00A5377A  EB 08                           jmp 0x140a53784
00A5377C  BB 01 00 00 00                  mov ebx, 1
00A53781  45 33 E4                        xor r12d, r12d
00A53784  83 FF 06                        cmp edi, 6
00A53787  74 0D                           je 0x140a53796
00A53789  83 FF 05                        cmp edi, 5
00A5378C  75 0D                           jne 0x140a5379b
00A5378E  38 1D 6F 18 57 00               cmp byte ptr [rip + 0x57186f], bl
00A53794  75 05                           jne 0x140a5379b
00A53796  E8 D9 C6 A8 FF                  call 0x1404dfe74
00A5379B  E8 F0 32 00 00                  call 0x140a56a90
00A537A0  44 8A 05 59 80 3B 00            mov r8b, byte ptr [rip + 0x3b8059]
00A537A7  41 8A D5                        mov dl, r13b
00A537AA  44 2A C3                        sub r8b, bl
00A537AD  8B CF                           mov ecx, edi
00A537AF  E8 7C 23 FE FF                  call 0x140a35b30
00A537B4  45 84 F6                        test r14b, r14b
00A537B7  75 11                           jne 0x140a537ca
00A537B9  85 FF                           test edi, edi
00A537BB  74 04                           je 0x140a537c1
00A537BD  84 C0                           test al, al
00A537BF  75 09                           jne 0x140a537ca
00A537C1  44 38 3D A7 33 57 00            cmp byte ptr [rip + 0x5733a7], r15b
00A537C8  74 11                           je 0x140a537db
00A537CA  41 0F B6 D7                     movzx edx, r15b
00A537CE  4C 8D 44 24 58                  lea r8, [rsp + 0x58]
00A537D3  48 8B CE                        mov rcx, rsi
00A537D6  E8 5D 3B 9D FF                  call 0x140427338
00A537DB  44 39 64 24 58                  cmp dword ptr [rsp + 0x58], r12d
00A537E0  75 56                           jne 0x140a53838
00A537E2  48 8B 35 DF 33 57 00            mov rsi, qword ptr [rip + 0x5733df]
00A537E9  44 89 25 50 33 57 00            mov dword ptr [rip + 0x573350], r12d
00A537F0  8B 56 04                        mov edx, dword ptr [rsi + 4]
00A537F3  48 8D 4E 18                     lea rcx, [rsi + 0x18]
00A537F7  8B 3E                           mov edi, dword ptr [rsi]
00A537F9  8B DA                           mov ebx, edx
00A537FB  44 8B C7                        mov r8d, edi
00A537FE  48 03 DB                        add rbx, rbx
00A53801  44 0F AF C2                     imul r8d, edx
00A53805  33 D2                           xor edx, edx
00A53807  49 C1 E0 02                     shl r8, 2
00A5380B  E8 30 34 C7 FF                  call 0x1406c6c40
00A53810  48 8B 4E 10                     mov rcx, qword ptr [rsi + 0x10]
00A53814  4C 8B C3                        mov r8, rbx
00A53817  33 D2                           xor edx, edx
00A53819  E8 22 34 C7 FF                  call 0x1406c6c40
00A5381E  48 8B 4E 08                     mov rcx, qword ptr [rsi + 8]
00A53822  44 8B C7                        mov r8d, edi
00A53825  33 D2                           xor edx, edx
00A53827  E8 14 34 C7 FF                  call 0x1406c6c40
00A5382C  BB 01 00 00 00                  mov ebx, 1
00A53831  40 84 ED                        test bpl, bpl
00A53834  74 2C                           je 0x140a53862
00A53836  EB 24                           jmp 0x140a5385c
00A53838  48 8B 0D 89 33 57 00            mov rcx, qword ptr [rip + 0x573389]
00A5383F  89 3D FB 32 57 00               mov dword ptr [rip + 0x5732fb], edi
00A53845  48 3B F1                        cmp rsi, rcx
00A53848  74 08                           je 0x140a53852
00A5384A  48 8B D6                        mov rdx, rsi
00A5384D  E8 1A D3 03 00                  call 0x140a90b6c
00A53852  45 84 FF                        test r15b, r15b
00A53855  74 05                           je 0x140a5385c
00A53857  E8 30 F4 A5 FF                  call 0x1404b2c8c
00A5385C  88 1D 0A 33 57 00               mov byte ptr [rip + 0x57330a], bl
00A53862  44 8B 05 D7 32 57 00            mov r8d, dword ptr [rip + 0x5732d7]
00A53869  41 8D 40 FF                     lea eax, [r8 - 1]
00A5386D  A9 FA FF FF FF                  test eax, 0xfffffffa
00A53872  74 0C                           je 0x140a53880
00A53874  44 89 25 BD 17 57 00            mov dword ptr [rip + 0x5717bd], r12d
00A5387B  41 8B C4                        mov eax, r12d
00A5387E  EB 0C                           jmp 0x140a5388c
00A53880  8B 05 EE 19 57 00               mov eax, dword ptr [rip + 0x5719ee]
00A53886  89 05 AC 17 57 00               mov dword ptr [rip + 0x5717ac], eax
00A5388C  45 84 ED                        test r13b, r13b
00A5388F  74 0A                           je 0x140a5389b
00A53891  85 C0                           test eax, eax
00A53893  0F 95 C1                        setne cl
00A53896  E8 09 06 05 00                  call 0x140aa3ea4
00A5389B  83 3D F2 18 57 00 FF            cmp dword ptr [rip + 0x5718f2], -1
00A538A2  75 0F                           jne 0x140a538b3
00A538A4  41 8B C4                        mov eax, r12d
00A538A7  45 85 C0                        test r8d, r8d
00A538AA  0F 95 C0                        setne al
00A538AD  89 05 21 34 57 00               mov dword ptr [rip + 0x573421], eax
00A538B3  E8 C8 ED A5 FF                  call 0x1404b2680
00A538B8  88 05 C8 31 57 00               mov byte ptr [rip + 0x5731c8], al
00A538BE  44 88 25 A3 58 4B 00            mov byte ptr [rip + 0x4b58a3], r12b
00A538C5  E8 52 15 AA FF                  call 0x1404f4e1c
00A538CA  85 C0                           test eax, eax
00A538CC  74 16                           je 0x140a538e4
00A538CE  E8 35 77 10 00                  call 0x140b5b008
00A538D3  88 05 8F 58 4B 00               mov byte ptr [rip + 0x4b588f], al
00A538D9  E8 66 5B B8 FF                  call 0x1405d9444
00A538DE  89 05 BC 3F 41 00               mov dword ptr [rip + 0x413fbc], eax
00A538E4  E8 47 3B 02 00                  call 0x140a77430
00A538E9  33 C9                           xor ecx, ecx
00A538EB  E8 A4 3E 04 00                  call 0x140a97794
00A538F0  8B CB                           mov ecx, ebx
00A538F2  E8 BD 34 9D FF                  call 0x140426db4
00A538F7  44 88 3D 71 32 57 00            mov byte ptr [rip + 0x573271], r15b
00A538FE  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
00A53903  41 8A C6                        mov al, r14b
00A53906  48 8B 6C 24 60                  mov rbp, qword ptr [rsp + 0x60]
00A5390B  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
00A53910  48 83 C4 20                     add rsp, 0x20
00A53914  41 5F                           pop r15
00A53916  41 5E                           pop r14
00A53918  41 5D                           pop r13
00A5391A  41 5C                           pop r12
00A5391C  5F                              pop rdi
00A5391D  C3                              ret
00A5391E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopInitializeHeteroProcessors(int a1, int a2)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned int v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p18 = v_rbp;
    v_stack_p20 = v_rsi;
    v_rsp = (v_rsp) - (32);
    v_r12 = 0;
    if (*(unsigned __int64 *)(v_rip + 5717341) != 0) goto loc_00A535A6;
    goto loc_00A538FE;
loc_00A535A6:
    if ((*(unsigned __int64 *)(v_rip + 4932075)) != 0) goto loc_00A535E5;
    if ((*(unsigned __int64 *)(v_rip + 4932065)) != 0) goto loc_00A535E5;
    if ((*(unsigned __int64 *)(v_rip + 4932032)) != 0) goto loc_00A535E5;
    if ((*(unsigned __int64 *)(v_rip + 4932031)) != 0) goto loc_00A535E5;
    if ((*(unsigned __int64 *)(v_rip + 4932006)) != 0) goto loc_00A535E5;
    if ((*(unsigned int *)(v_rip + 5716425)) == 0) goto loc_00A535FB;
loc_00A535E5:
    v_rbp = 0;
    if ((*(unsigned __int8 *)(v_rip + 5715184)) != 0) {
        a1 = 0;
        result = KeQueryActiveProcessorCountEx(a1, a2, a3, a4);
        v_rbp = 0;
        if (((unsigned int)(result)) >= 2) { v_rbp = 1; }
    }
    if ((*(unsigned __int8 *)(v_rip + 5715179)) == 0) goto loc_00A53609;
    goto loc_00A5360E;
loc_00A53609:
    if (1 == 0) goto loc_00A5361A;
loc_00A5360E:
    v_r15 = 1;
    if ((*(unsigned int *)(v_rip + 5715859)) != 0) {
        v_r15 = 0;
    }
    if ((unsigned __int8)((unsigned __int8)(a1)) == 0) goto loc_00A5375E;
    a2 = 0;
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 5717341) + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3899851)));
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 5717341)))) * (*(unsigned int *)(v_rip + 3899838)));
    a3 = (a3) << (2);
    result = memset(*(unsigned __int64 *)(v_rip + 5717341) + 24, a2, a3, a4);
    result = PpmHeteroComputeRelativePerformance(*(unsigned __int64 *)(v_rip + 5717341) + 24, a2, a3, a4);
    result = PpmHeteroUpdateHgsConfiguration(*(unsigned __int64 *)(v_rip + 5717341) + 24, a2, a3, a4);
    result = PpmHeteroDetectHgsCores(*(unsigned __int64 *)(v_rip + 5717341), a2, a3, a4);
    v_stack_p10 = (unsigned int)((unsigned __int8)(result));
    if ((unsigned int)((unsigned __int8)(result)) == 0) goto loc_00A53678;
    goto loc_00A536FB;
loc_00A53678:
    result = PopIsSimulatedArchitecturalHeteroPresent(*(unsigned __int64 *)(v_rip + 5717341), a2, a3, a4);
    v_stack_p10 = (unsigned int)((unsigned __int8)(result));
    if ((unsigned int)((unsigned __int8)(result)) == 0) goto loc_00A5369E;
    result = PpmHeteroDetectFavoredCores(*(unsigned __int64 *)(v_rip + 5717341), a2, a3, a4);
    result = (unsigned __int8)(-(result));
    v_rdi = (unsigned int)((6 - 1) & (5));
    v_rdi = (unsigned int)((v_rdi) + (1));
    goto loc_00A536FB;
loc_00A5369E:
    result = KeDetectHeterogeneousSets(*(unsigned __int64 *)(v_rip + 5717341), a2, a3, a4);
    v_stack_p10 = (unsigned int)(result);
    if ((unsigned int)(result) == 0) goto loc_00A536D6;
    result = PpmHeteroDetectFavoredCores(*(unsigned __int64 *)(v_rip + 5717341), a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00A536BC;
    goto loc_00A536FB;
loc_00A536BC:
    v_rdi = 2;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 141)) == 1) { v_rdi = 6; }
    goto loc_00A536FB;
loc_00A536D6:
    result = PpmHeteroDetectFavoredCores(*(unsigned __int64 *)(v_rip + 5717341), a2, a3, a4);
    v_stack_p10 = (unsigned int)((unsigned __int8)(result));
    if ((unsigned int)((unsigned __int8)(result)) == 0) goto loc_00A536ED;
    goto loc_00A536FB;
loc_00A536ED:
    v_rdi = 3;
    if ((unsigned __int8)(v_r15) != 0) {
        v_stack_p10 = 1;
        v_rdi = 4;
    }
    if (((unsigned int)(v_rdi)) == (*(unsigned int *)(v_rip + 5715007))) goto loc_00A53708;
    goto loc_00A53784;
loc_00A53708:
    a2 = (*(unsigned __int64 *)(v_rip + 5715129)) + (24);
    v_r12 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 5717341) + 4))) + ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 5717341) + 4)));
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 5717341) + 4))))) * (*(unsigned int *)(*(unsigned __int64 *)(v_rip + 5717341))));
    v_rbx = (v_rbx) << (2);
    result = RtlCompareMemory(*(unsigned __int64 *)(v_rip + 5717341) + 24, a2, v_rbx, a4);
    if (result != v_rbx) goto loc_00A53754;
    result = RtlCompareMemory(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 5717341) + 16), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 5715081) + 16), v_r12, a4);
    if (result == v_r12) goto loc_00A5377C;
loc_00A53754:
    goto loc_00A53781;
loc_00A5375E:
    result = ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5714908))) != 0) ? 1 : 0;
    v_stack_p10 = (unsigned int)(result);
    goto loc_00A53784;
loc_00A5377C:
loc_00A53781:
    v_r12 = 0;
loc_00A53784:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5714908)))) == 6) goto loc_00A53796;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5714908)))) != 5) goto loc_00A5379B;
    if ((*(unsigned __int8 *)(v_rip + 5707887)) == 1) {
        result = PpmHeteroReevaluateMultiCoreFeatures(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 5717341) + 16), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 5715081) + 16), v_r12, a4);
    }
    result = PpmHeteroComputeMinRelativePerformane(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 5717341) + 16), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 5715081) + 16), v_r12, a4);
    a3 = (unsigned __int8)((*(unsigned __int8 *)(v_rip + 3899481)) - (1));
    result = PopConfigureHeteroPolicies((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5714908)))), (unsigned __int8)((unsigned __int8)(a1)), a3, a4);
    if ((unsigned __int8)((unsigned __int8)(v_r12)) != 0) goto loc_00A537CA;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5714908))) == 0) goto loc_00A537C1;
    if ((unsigned __int8)(result) != 0) goto loc_00A537CA;
loc_00A537C1:
    if ((*(unsigned __int8 *)(v_rip + 5714855)) != ((unsigned __int8)(v_r15))) {
        a2 = (unsigned __int8)(v_r15);
        a3 = v_stack_p10;
        a1 = *(unsigned __int64 *)(v_rip + 5715034);
        result = KeConfigureHeteroProcessors(a1, a2, a3, a4);
    }
    if (v_stack_p10 != 0) goto loc_00A53838;
    *(unsigned int *)(v_rip + 5714768) = 0;
    v_rbx = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 5714911) + 4))))) + ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 5714911) + 4)))));
    a3 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 5714911)))))) * ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 5714911) + 4)))));
    a2 = 0;
    a3 = (a3) << (2);
    result = memset(*(unsigned __int64 *)(v_rip + 5714911) + 24, a2, a3, a4);
    a2 = 0;
    result = memset(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 5714911) + 16), a2, v_rbx, a4);
    a2 = 0;
    result = memset(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 5714911) + 8), a2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 5714911))))), a4);
    if (1 == 0) goto loc_00A53862;
    goto loc_00A5385C;
loc_00A53838:
    *(unsigned int *)(v_rip + 5714683) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 5714911))));
    if ((*(unsigned __int64 *)(v_rip + 5714911)) != (*(unsigned __int64 *)(v_rip + 5714825))) {
        a2 = *(unsigned __int64 *)(v_rip + 5714911);
        result = PopHeteroCapabilityDeepCopy(*(unsigned __int64 *)(v_rip + 5714825), a2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 5714911))))), a4);
    }
    if ((unsigned __int8)(v_r15) != 0) {
        result = PpmIdleEnableIdleDurationExpirationTimeout(*(unsigned __int64 *)(v_rip + 5714825), a2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 5714911))))), a4);
    }
    *(unsigned __int8 *)(v_rip + 5714698) = 1;
loc_00A53862:
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5714647)) - 1)) & (0xFFFFFFFAULL)) == 0) goto loc_00A53880;
    *(unsigned int *)(v_rip + 5707709) = 0;
    goto loc_00A5388C;
loc_00A53880:
    *(unsigned int *)(v_rip + 5707692) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5708270)));
loc_00A5388C:
    result = (unsigned int)(*(unsigned int *)(v_rip + 5708270));
    if ((unsigned __int8)((unsigned __int8)(a1)) != 0) {
        a1 = ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5708270))) != 0) ? 1 : 0;
        result = KeNotifyHeteroParkingPolicyChange(a1, a2, (unsigned int)(*(unsigned int *)(v_rip + 5714647)), a4);
    }
    if ((*(unsigned int *)(v_rip + 5708018)) == -1) {
        result = 0;
        result = ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5714647))) != 0) ? 1 : 0;
        *(unsigned int *)(v_rip + 5714977) = (unsigned int)(result);
    }
    result = PpmHeteroGetHgsPlusParkingEnablementStatus(a1, a2, (unsigned int)(*(unsigned int *)(v_rip + 5714647)), a4);
    *(unsigned __int8 *)(v_rip + 5714376) = (unsigned __int8)(result);
    *(unsigned __int8 *)(v_rip + 4937891) = 0;
    result = Feature_UnparkPCoresOnUnimportantUtility__private_IsEnabledDeviceUsageNoInline(a1, a2, (unsigned int)(*(unsigned int *)(v_rip + 5714647)), a4);
    if ((unsigned int)(result) != 0) {
        result = PopGetUnparkOnUnimportantUtilityEnablementStatus(a1, a2, (unsigned int)(*(unsigned int *)(v_rip + 5714647)), a4);
        *(unsigned __int8 *)(v_rip + 4937871) = (unsigned __int8)(result);
        result = Feature_UnparkPCoresOnUnimportantUtility__private_GetVariant(a1, a2, (unsigned int)(*(unsigned int *)(v_rip + 5714647)), a4);
        *(unsigned int *)(v_rip + 4276156) = (unsigned int)(result);
    }
    result = PpmEventHeteroConfigUpdate(a1, a2, (unsigned int)(*(unsigned int *)(v_rip + 5714647)), a4);
    a1 = 0;
    result = PpmEventHeteroPolicy(a1, a2, (unsigned int)(*(unsigned int *)(v_rip + 5714647)), a4);
    result = PpmEventTraceHeteroSets(1, a2, (unsigned int)(*(unsigned int *)(v_rip + 5714647)), a4);
    *(unsigned __int8 *)(v_rip + 5714545) = (unsigned __int8)(v_r15);
loc_00A538FE:
    v_rsp = (v_rsp) + (32);
    return (unsigned __int8)((unsigned __int8)(v_r12));
}
```

## 5. (Beta) C Style

```c
int64_t PopInitializeHeteroProcessors(int32_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_r12;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint32_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p18 = local_rbp;
    v_stack_p20 = local_rsi;
    local_rsp = (local_rsp) - (32);
    local_r12 = 0;
    if (*(uint64_t *)(v_rip + 0x573D5D) != 0) goto loc_00A535A6;
    goto loc_00A538FE;
loc_00A535A6:
    if ((*(uint64_t *)(v_rip + 0x4B41EB)) != 0) goto loc_00A535E5;
    if ((*(uint64_t *)(v_rip + 0x4B41E1)) != 0) goto loc_00A535E5;
    if ((*(uint64_t *)(v_rip + 0x4B41C0)) != 0) goto loc_00A535E5;
    if ((*(uint64_t *)(v_rip + 0x4B41BF)) != 0) goto loc_00A535E5;
    if ((*(uint64_t *)(v_rip + 0x4B41A6)) != 0) goto loc_00A535E5;
    if ((*(uint32_t *)(v_rip + 0x5739C9)) == 0) goto loc_00A535FB;
loc_00A535E5:
    local_rbp = 0;
    if ((*(uint8_t *)(v_rip + 0x5734F0)) != 0) {
        Arg1 = 0;
        result = KeQueryActiveProcessorCountEx(Arg1, Arg2, a3, a4);
        local_rbp = 0;
        if (((uint32_t)(result)) >= 2) { local_rbp = 1; }
    }
    if ((*(uint8_t *)(v_rip + 0x5734EB)) == 0) goto loc_00A53609;
    goto loc_00A5360E;
loc_00A53609:
    if (1 == 0) goto loc_00A5361A;
loc_00A5360E:
    local_r15 = 1;
    if ((*(uint32_t *)(v_rip + 0x573793)) != 0) {
        local_r15 = 0;
    }
    if ((uint8_t)((uint8_t)(Arg1)) == 0) goto loc_00A5375E;
    Arg2 = 0;
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x573D5D) + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x3B81CB)));
    a3 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x573D5D)))) * (*(uint32_t *)(v_rip + 0x3B81BE)));
    a3 = (a3) << (2);
    result = memset(*(uint64_t *)(v_rip + 0x573D5D) + 24, Arg2, a3, a4);
    result = PpmHeteroComputeRelativePerformance(*(uint64_t *)(v_rip + 0x573D5D) + 24, Arg2, a3, a4);
    result = PpmHeteroUpdateHgsConfiguration(*(uint64_t *)(v_rip + 0x573D5D) + 24, Arg2, a3, a4);
    result = PpmHeteroDetectHgsCores(*(uint64_t *)(v_rip + 0x573D5D), Arg2, a3, a4);
    v_stack_p10 = (uint32_t)((uint8_t)(result));
    if ((uint32_t)((uint8_t)(result)) == 0) goto loc_00A53678;
    goto loc_00A536FB;
loc_00A53678:
    result = PopIsSimulatedArchitecturalHeteroPresent(*(uint64_t *)(v_rip + 0x573D5D), Arg2, a3, a4);
    v_stack_p10 = (uint32_t)((uint8_t)(result));
    if ((uint32_t)((uint8_t)(result)) == 0) goto loc_00A5369E;
    result = PpmHeteroDetectFavoredCores(*(uint64_t *)(v_rip + 0x573D5D), Arg2, a3, a4);
    result = (uint8_t)(-(result));
    local_rdi = (uint32_t)((6 - 1) & (5));
    local_rdi = (uint32_t)((local_rdi) + (1));
    goto loc_00A536FB;
loc_00A5369E:
    result = KeDetectHeterogeneousSets(*(uint64_t *)(v_rip + 0x573D5D), Arg2, a3, a4);
    v_stack_p10 = (uint32_t)(result);
    if ((uint32_t)(result) == 0) goto loc_00A536D6;
    result = PpmHeteroDetectFavoredCores(*(uint64_t *)(v_rip + 0x573D5D), Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00A536BC;
    goto loc_00A536FB;
loc_00A536BC:
    local_rdi = 2;
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8D)) == 1) { local_rdi = 6; }
    goto loc_00A536FB;
loc_00A536D6:
    result = PpmHeteroDetectFavoredCores(*(uint64_t *)(v_rip + 0x573D5D), Arg2, a3, a4);
    v_stack_p10 = (uint32_t)((uint8_t)(result));
    if ((uint32_t)((uint8_t)(result)) == 0) goto loc_00A536ED;
    goto loc_00A536FB;
loc_00A536ED:
    local_rdi = 3;
    if ((uint8_t)(local_r15) != 0) {
        v_stack_p10 = 1;
        local_rdi = 4;
    }
    if (((uint32_t)(local_rdi)) == (*(uint32_t *)(v_rip + 0x57343F))) goto loc_00A53708;
    goto loc_00A53784;
loc_00A53708:
    Arg2 = (*(uint64_t *)(v_rip + 0x5734B9)) + (24);
    local_r12 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x573D5D) + 0x4))) + ((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x573D5D) + 0x4)));
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x573D5D) + 0x4))))) * (*(uint32_t *)(*(uint64_t *)(v_rip + 0x573D5D))));
    local_rbx = (local_rbx) << (2);
    result = RtlCompareMemory(*(uint64_t *)(v_rip + 0x573D5D) + 24, Arg2, local_rbx, a4);
    if (result != local_rbx) goto loc_00A53754;
    result = RtlCompareMemory(*(uint64_t *)(*(uint64_t *)(v_rip + 0x573D5D) + 0x10), *(uint64_t *)(*(uint64_t *)(v_rip + 0x573489) + 0x10), local_r12, a4);
    if (result == local_r12) goto loc_00A5377C;
loc_00A53754:
    goto loc_00A53781;
loc_00A5375E:
    result = ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x5733DC))) != 0) ? 1 : 0;
    v_stack_p10 = (uint32_t)(result);
    goto loc_00A53784;
loc_00A5377C:
loc_00A53781:
    local_r12 = 0;
loc_00A53784:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x5733DC)))) == 6) goto loc_00A53796;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x5733DC)))) != 5) goto loc_00A5379B;
    if ((*(uint8_t *)(v_rip + 0x57186F)) == 1) {
        result = PpmHeteroReevaluateMultiCoreFeatures(*(uint64_t *)(*(uint64_t *)(v_rip + 0x573D5D) + 0x10), *(uint64_t *)(*(uint64_t *)(v_rip + 0x573489) + 0x10), local_r12, a4);
    }
    result = PpmHeteroComputeMinRelativePerformane(*(uint64_t *)(*(uint64_t *)(v_rip + 0x573D5D) + 0x10), *(uint64_t *)(*(uint64_t *)(v_rip + 0x573489) + 0x10), local_r12, a4);
    a3 = (uint8_t)((*(uint8_t *)(v_rip + 0x3B8059)) - (1));
    result = PopConfigureHeteroPolicies((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x5733DC)))), (uint8_t)((uint8_t)(Arg1)), a3, a4);
    if ((uint8_t)((uint8_t)(local_r12)) != 0) goto loc_00A537CA;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x5733DC))) == 0) goto loc_00A537C1;
    if ((uint8_t)(result) != 0) goto loc_00A537CA;
loc_00A537C1:
    if ((*(uint8_t *)(v_rip + 0x5733A7)) != ((uint8_t)(local_r15))) {
        Arg2 = (uint8_t)(local_r15);
        a3 = v_stack_p10;
        Arg1 = *(uint64_t *)(v_rip + 0x57345A);
        result = KeConfigureHeteroProcessors(Arg1, Arg2, a3, a4);
    }
    if (v_stack_p10 != 0) goto loc_00A53838;
    *(uint32_t *)(v_rip + 0x573350) = 0;
    local_rbx = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x5733DF) + 0x4))))) + ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x5733DF) + 0x4)))));
    a3 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x5733DF)))))) * ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x5733DF) + 0x4)))));
    Arg2 = 0;
    a3 = (a3) << (2);
    result = memset(*(uint64_t *)(v_rip + 0x5733DF) + 24, Arg2, a3, a4);
    Arg2 = 0;
    result = memset(*(uint64_t *)(*(uint64_t *)(v_rip + 0x5733DF) + 0x10), Arg2, local_rbx, a4);
    Arg2 = 0;
    result = memset(*(uint64_t *)(*(uint64_t *)(v_rip + 0x5733DF) + 0x8), Arg2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x5733DF))))), a4);
    if (1 == 0) goto loc_00A53862;
    goto loc_00A5385C;
loc_00A53838:
    *(uint32_t *)(v_rip + 0x5732FB) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x5733DF))));
    if ((*(uint64_t *)(v_rip + 0x5733DF)) != (*(uint64_t *)(v_rip + 0x573389))) {
        Arg2 = *(uint64_t *)(v_rip + 0x5733DF);
        result = PopHeteroCapabilityDeepCopy(*(uint64_t *)(v_rip + 0x573389), Arg2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x5733DF))))), a4);
    }
    if ((uint8_t)(local_r15) != 0) {
        result = PpmIdleEnableIdleDurationExpirationTimeout(*(uint64_t *)(v_rip + 0x573389), Arg2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x5733DF))))), a4);
    }
    *(uint8_t *)(v_rip + 0x57330A) = 1;
loc_00A53862:
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x5732D7)) - 1)) & (0xFFFFFFFAULL)) == 0) goto loc_00A53880;
    *(uint32_t *)(v_rip + 0x5717BD) = 0;
    goto loc_00A5388C;
loc_00A53880:
    *(uint32_t *)(v_rip + 0x5717AC) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x5719EE)));
loc_00A5388C:
    result = (uint32_t)(*(uint32_t *)(v_rip + 0x5719EE));
    if ((uint8_t)((uint8_t)(Arg1)) != 0) {
        Arg1 = ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x5719EE))) != 0) ? 1 : 0;
        result = KeNotifyHeteroParkingPolicyChange(Arg1, Arg2, (uint32_t)(*(uint32_t *)(v_rip + 0x5732D7)), a4);
    }
    if ((*(uint32_t *)(v_rip + 0x5718F2)) == -1) {
        result = 0;
        result = ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x5732D7))) != 0) ? 1 : 0;
        *(uint32_t *)(v_rip + 0x573421) = (uint32_t)(result);
    }
    result = PpmHeteroGetHgsPlusParkingEnablementStatus(Arg1, Arg2, (uint32_t)(*(uint32_t *)(v_rip + 0x5732D7)), a4);
    *(uint8_t *)(v_rip + 0x5731C8) = (uint8_t)(result);
    *(uint8_t *)(v_rip + 0x4B58A3) = 0;
    result = Feature_UnparkPCoresOnUnimportantUtility__private_IsEnabledDeviceUsageNoInline(Arg1, Arg2, (uint32_t)(*(uint32_t *)(v_rip + 0x5732D7)), a4);
    if ((uint32_t)(result) != 0) {
        result = PopGetUnparkOnUnimportantUtilityEnablementStatus(Arg1, Arg2, (uint32_t)(*(uint32_t *)(v_rip + 0x5732D7)), a4);
        *(uint8_t *)(v_rip + 0x4B588F) = (uint8_t)(result);
        result = Feature_UnparkPCoresOnUnimportantUtility__private_GetVariant(Arg1, Arg2, (uint32_t)(*(uint32_t *)(v_rip + 0x5732D7)), a4);
        *(uint32_t *)(v_rip + 0x413FBC) = (uint32_t)(result);
    }
    result = PpmEventHeteroConfigUpdate(Arg1, Arg2, (uint32_t)(*(uint32_t *)(v_rip + 0x5732D7)), a4);
    Arg1 = 0;
    result = PpmEventHeteroPolicy(Arg1, Arg2, (uint32_t)(*(uint32_t *)(v_rip + 0x5732D7)), a4);
    result = PpmEventTraceHeteroSets(1, Arg2, (uint32_t)(*(uint32_t *)(v_rip + 0x5732D7)), a4);
    *(uint8_t *)(v_rip + 0x573271) = (uint8_t)(local_r15);
loc_00A538FE:
    local_rsp = (local_rsp) + (32);
    return (uint8_t)((uint8_t)(local_r12));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A53570&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
