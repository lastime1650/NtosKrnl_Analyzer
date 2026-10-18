# WdipSemLoadScenarioTable

- RVA: `0x007B02D8`–`0x007B081D` (길이 `1,349` bytes)
- VA: `0x00000001407B02D8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D2FCC`
- 디코드: `332`개 명령, `1,349/1,349` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **40**; 고유 호출 대상: **21**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **13**

### Outgoing calls
- `0x007B0351` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x007B0367` → [WdipSemOpenRegistryKey](WdipSemOpenRegistryKey_function_007B17C8.md) (function, `0x007B17C8`)
- `0x007B0383` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x007B0397` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x007B03AB` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x007B03C4` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x007B03ED` → [ZwEnumerateKey](../../text/6A/ZwEnumerateKey_function_006AD710.md) (function, `0x006AD710`)
- `0x007B0435` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x007B0446` → [RtlGUIDFromString](../8F/RtlGUIDFromString_function_008F1EF0.md) (function, `0x008F1EF0`)
- `0x007B04AD` → [WdipSemOpenRegistryKey](WdipSemOpenRegistryKey_function_007B17C8.md) (function, `0x007B17C8`)
- `0x007B04D6` → [WdipSemOpenRegistryKey](WdipSemOpenRegistryKey_function_007B17C8.md) (function, `0x007B17C8`)
- `0x007B050C` → [WdipSemQueryValueFromRegistry](WdipSemQueryValueFromRegistry_function_007B185C.md) (function, `0x007B185C`)
- `0x007B0548` → [WdipSemQueryValueFromRegistry](WdipSemQueryValueFromRegistry_function_007B185C.md) (function, `0x007B185C`)
- `0x007B0564` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x007B057E` → [VerSetConditionMask](../../text/46/VerSetConditionMask_function_0046CC50.md) (function, `0x0046CC50`)
- `0x007B0592` → [RtlVerifyVersionInfo](../../text/45/RtlVerifyVersionInfo_function_00457670.md) (function, `0x00457670`)
- `0x007B05C8` → [WdipSemQueryValueFromRegistry](WdipSemQueryValueFromRegistry_function_007B185C.md) (function, `0x007B185C`)
- `0x007B05ED` → [WdipSemOpenRegistryKey](WdipSemOpenRegistryKey_function_007B17C8.md) (function, `0x007B17C8`)
- `0x007B0605` → [WdipSemFreeScenario](WdipSemFreeScenario_function_007B1060.md) (function, `0x007B1060`)
- `0x007B0616` → [WdipSemFastAllocate](../A5/WdipSemFastAllocate_function_00A5DC04.md) (function, `0x00A5DC04`)
- `0x007B062F` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x007B0646` → [WdipSemLoadNextScenario](../7A/WdipSemLoadNextScenario_function_007AFDE0.md) (function, `0x007AFDE0`)
- `0x007B066D` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x007B0680` → [WdipSemWriteMisconfigEvent](WdipSemWriteMisconfigEvent_function_007B151C.md) (function, `0x007B151C`)
- `0x007B06A0` → [WdipSemUpdateProviderTableWithEvent](WdipSemUpdateProviderTableWithEvent_function_007B09F8.md) (function, `0x007B09F8`)
- `0x007B06B5` → [WdipSemUpdateProviderTableWithEvent](WdipSemUpdateProviderTableWithEvent_function_007B09F8.md) (function, `0x007B09F8`)
- `0x007B06D3` → [WdipSemUpdateProviderTableWithEvent](WdipSemUpdateProviderTableWithEvent_function_007B09F8.md) (function, `0x007B09F8`)
- `0x007B06EC` → [WdipSemAddScenarioToTable](../7A/WdipSemAddScenarioToTable_function_007AF4D0.md) (function, `0x007AF4D0`)
- `0x007B06F7` → [WdipSemRollBackProviderTable](WdipSemRollBackProviderTable_function_007B08E8.md) (function, `0x007B08E8`)
- `0x007B0711` → [WdipSemUpdateProviderEntryForEvent](WdipSemUpdateProviderEntryForEvent_function_007B1C10.md) (function, `0x007B1C10`)
- `0x007B072A` → [WdipSemUpdateProviderEntryForEvent](WdipSemUpdateProviderEntryForEvent_function_007B1C10.md) (function, `0x007B1C10`)
- `0x007B0757` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x007B0773` → [WdipSemWriteScenarioLimitExceededEvent](WdipSemWriteScenarioLimitExceededEvent_function_007B15AC.md) (function, `0x007B15AC`)
- `0x007B078D` → [WdipSemEnableAllProviders](WdipSemEnableAllProviders_function_007B1A1C.md) (function, `0x007B1A1C`)
- `0x007B079C` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x007B07B0` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x007B07C4` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x007B07D8` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x007B07E5` → [WdipSemFreeScenario](WdipSemFreeScenario_function_007B1060.md) (function, `0x007B1060`)
- `0x007B07F6` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [WdipSemCleanStart](../7A/WdipSemCleanStart_function_007AF590.md) at `0x007AF5C2`

### Static image references
- `0x007B02FE` → RVA `0x00E0A740` (`.data`; read)
- `0x007B035D` → RVA `0x00B06C80` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007B0453` → RVA `0x00F01E10` (`.data`; read)
- `0x007B04C4` → RVA `0x00B06BC0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007B04F2` → RVA `0x00B06B80` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007B052E` → RVA `0x00B06C00` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007B05AE` → RVA `0x00B06BD0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007B05E6` → RVA `0x00B06B60` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007B065F` → RVA `0x00F01DD0` (`.data`; read)
- `0x007B0666` → RVA `0x000224F0` (`.rdata`; read)
- `0x007B068A` → RVA `0x00F02020` (`.data`; read)
- `0x007B0697` → RVA `0x00F01DC0` (`.data`; read)
- `0x007B0750` → RVA `0x00023248` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **18**
  - `0x007B0351` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x007B0383` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x007B0397` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x007B03AB` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x007B03C4` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x007B03ED` → [ZwEnumerateKey](../../text/6A/ZwEnumerateKey_function_006AD710.md) (`PAGE` → `.text`)
  - `0x007B0435` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x007B0564` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x007B057E` → [VerSetConditionMask](../../text/46/VerSetConditionMask_function_0046CC50.md) (`PAGE` → `.text`)
  - `0x007B0592` → [RtlVerifyVersionInfo](../../text/45/RtlVerifyVersionInfo_function_00457670.md) (`PAGE` → `.text`)
  - `0x007B062F` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x007B066D` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (`PAGE` → `.text`)
  - `0x007B0757` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (`PAGE` → `.text`)
  - `0x007B079C` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x007B07B0` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x007B07C4` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x007B07D8` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x007B07F6` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007B02D8  48 8B C4                        mov rax, rsp
007B02DB  48 89 58 08                     mov qword ptr [rax + 8], rbx
007B02DF  48 89 70 10                     mov qword ptr [rax + 0x10], rsi
007B02E3  48 89 78 18                     mov qword ptr [rax + 0x18], rdi
007B02E7  55                              push rbp
007B02E8  41 54                           push r12
007B02EA  41 55                           push r13
007B02EC  41 56                           push r14
007B02EE  41 57                           push r15
007B02F0  48 8D A8 88 FE FF FF            lea rbp, [rax - 0x178]
007B02F7  48 81 EC 50 02 00 00            sub rsp, 0x250
007B02FE  48 8B 05 3B A4 65 00            mov rax, qword ptr [rip + 0x65a43b]
007B0305  48 33 C4                        xor rax, rsp
007B0308  48 89 85 48 01 00 00            mov qword ptr [rbp + 0x148], rax
007B030F  33 F6                           xor esi, esi
007B0311  48 8D 4D 80                     lea rcx, [rbp - 0x80]
007B0315  0F 57 C0                        xorps xmm0, xmm0
007B0318  48 89 74 24 58                  mov qword ptr [rsp + 0x58], rsi
007B031D  0F 57 C9                        xorps xmm1, xmm1
007B0320  48 89 74 24 40                  mov qword ptr [rsp + 0x40], rsi
007B0325  33 D2                           xor edx, edx
007B0327  48 89 74 24 38                  mov qword ptr [rsp + 0x38], rsi
007B032C  41 B8 1C 01 00 00               mov r8d, 0x11c
007B0332  48 89 74 24 60                  mov qword ptr [rsp + 0x60], rsi
007B0337  8B DE                           mov ebx, esi
007B0339  89 74 24 30                     mov dword ptr [rsp + 0x30], esi
007B033D  89 74 24 48                     mov dword ptr [rsp + 0x48], esi
007B0341  89 74 24 4C                     mov dword ptr [rsp + 0x4c], esi
007B0345  0F 11 44 24 68                  movups xmmword ptr [rsp + 0x68], xmm0
007B034A  0F 11 8D A0 00 00 00            movups xmmword ptr [rbp + 0xa0], xmm1
007B0351  E8 EA 68 F1 FF                  call 0x1406c6c40
007B0356  4C 8D 44 24 58                  lea r8, [rsp + 0x58]
007B035B  33 D2                           xor edx, edx
007B035D  48 8D 0D 1C 69 35 00            lea rcx, [rip + 0x35691c]
007B0364  44 8B EE                        mov r13d, esi
007B0367  E8 5C 14 00 00                  call 0x1407b17c8
007B036C  8B F8                           mov edi, eax
007B036E  85 C0                           test eax, eax
007B0370  0F 88 1C 04 00 00               js 0x1407b0792
007B0376  44 8B E6                        mov r12d, esi
007B0379  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
007B037E  48 85 C9                        test rcx, rcx
007B0381  74 0A                           je 0x1407b038d
007B0383  E8 28 CF EF FF                  call 0x1406ad2b0
007B0388  48 89 74 24 40                  mov qword ptr [rsp + 0x40], rsi
007B038D  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
007B0392  48 85 C9                        test rcx, rcx
007B0395  74 0A                           je 0x1407b03a1
007B0397  E8 14 CF EF FF                  call 0x1406ad2b0
007B039C  48 89 74 24 38                  mov qword ptr [rsp + 0x38], rsi
007B03A1  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
007B03A6  48 85 C9                        test rcx, rcx
007B03A9  74 0A                           je 0x1407b03b5
007B03AB  E8 00 CF EF FF                  call 0x1406ad2b0
007B03B0  48 89 74 24 60                  mov qword ptr [rsp + 0x60], rsi
007B03B5  33 D2                           xor edx, edx
007B03B7  48 8D 8D B0 00 00 00            lea rcx, [rbp + 0xb0]
007B03BE  41 B8 98 00 00 00               mov r8d, 0x98
007B03C4  E8 77 68 F1 FF                  call 0x1406c6c40
007B03C9  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
007B03CE  48 8D 44 24 30                  lea rax, [rsp + 0x30]
007B03D3  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007B03D8  4C 8D 8D B0 00 00 00            lea r9, [rbp + 0xb0]
007B03DF  45 33 C0                        xor r8d, r8d
007B03E2  C7 44 24 20 96 00 00 00         mov dword ptr [rsp + 0x20], 0x96
007B03EA  41 8B D4                        mov edx, r12d
007B03ED  E8 1E D3 EF FF                  call 0x1406ad710
007B03F2  41 FF C4                        inc r12d
007B03F5  3D 1A 00 00 80                  cmp eax, 0x8000001a
007B03FA  0F 84 8B 03 00 00               je 0x1407b078b
007B0400  85 C0                           test eax, eax
007B0402  0F 88 71 FF FF FF               js 0x1407b0379
007B0408  81 BD BC 00 00 00 80 00 00 00   cmp dword ptr [rbp + 0xbc], 0x80
007B0412  0F 83 6C 03 00 00               jae 0x1407b0784
007B0418  8B 85 BC 00 00 00               mov eax, dword ptr [rbp + 0xbc]
007B041E  48 8D 95 C0 00 00 00            lea rdx, [rbp + 0xc0]
007B0425  48 D1 E8                        shr rax, 1
007B0428  48 8D 4C 24 68                  lea rcx, [rsp + 0x68]
007B042D  66 89 B4 45 C0 00 00 00         mov word ptr [rbp + rax*2 + 0xc0], si
007B0435  E8 46 A3 C7 FF                  call 0x14042a780
007B043A  48 8D 95 A0 00 00 00            lea rdx, [rbp + 0xa0]
007B0441  48 8D 4C 24 68                  lea rcx, [rsp + 0x68]
007B0446  E8 A5 1A 14 00                  call 0x1408f1ef0
007B044B  85 C0                           test eax, eax
007B044D  0F 88 26 FF FF FF               js 0x1407b0379
007B0453  4C 8B 0D B6 19 75 00            mov r9, qword ptr [rip + 0x7519b6]
007B045A  4D 85 C9                        test r9, r9
007B045D  74 3D                           je 0x1407b049c
007B045F  45 8B 91 00 04 00 00            mov r10d, dword ptr [r9 + 0x400]
007B0466  44 8B C6                        mov r8d, esi
007B0469  45 3B C2                        cmp r8d, r10d
007B046C  73 2E                           jae 0x1407b049c
007B046E  48 8B 8D A0 00 00 00            mov rcx, qword ptr [rbp + 0xa0]
007B0475  41 8B D0                        mov edx, r8d
007B0478  48 C1 E2 04                     shl rdx, 4
007B047C  4A 2B 0C 0A                     sub rcx, qword ptr [rdx + r9]
007B0480  75 0C                           jne 0x1407b048e
007B0482  48 8B 8D A8 00 00 00            mov rcx, qword ptr [rbp + 0xa8]
007B0489  4A 2B 4C 0A 08                  sub rcx, qword ptr [rdx + r9 + 8]
007B048E  48 85 C9                        test rcx, rcx
007B0491  0F 84 E2 FE FF FF               je 0x1407b0379
007B0497  41 FF C0                        inc r8d
007B049A  EB CD                           jmp 0x1407b0469
007B049C  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
007B04A1  4C 8D 44 24 40                  lea r8, [rsp + 0x40]
007B04A6  48 8D 8D C0 00 00 00            lea rcx, [rbp + 0xc0]
007B04AD  E8 16 13 00 00                  call 0x1407b17c8
007B04B2  85 C0                           test eax, eax
007B04B4  0F 88 BF FE FF FF               js 0x1407b0379
007B04BA  48 8B 54 24 40                  mov rdx, qword ptr [rsp + 0x40]
007B04BF  4C 8D 44 24 38                  lea r8, [rsp + 0x38]
007B04C4  48 8D 0D F5 66 35 00            lea rcx, [rip + 0x3566f5]
007B04CB  C7 44 24 50 01 00 00 00         mov dword ptr [rsp + 0x50], 1
007B04D3  41 B7 01                        mov r15b, 1
007B04D6  E8 ED 12 00 00                  call 0x1407b17c8
007B04DB  85 C0                           test eax, eax
007B04DD  0F 88 F9 00 00 00               js 0x1407b05dc
007B04E3  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
007B04E8  48 8D 44 24 30                  lea rax, [rsp + 0x30]
007B04ED  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007B04F2  48 8D 15 87 66 35 00            lea rdx, [rip + 0x356687]
007B04F9  41 B9 04 00 00 00               mov r9d, 4
007B04FF  48 8D 44 24 48                  lea rax, [rsp + 0x48]
007B0504  45 8B C1                        mov r8d, r9d
007B0507  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007B050C  E8 4B 13 00 00                  call 0x1407b185c
007B0511  85 C0                           test eax, eax
007B0513  78 0A                           js 0x1407b051f
007B0515  39 74 24 48                     cmp dword ptr [rsp + 0x48], esi
007B0519  0F 84 5A FE FF FF               je 0x1407b0379
007B051F  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
007B0524  48 8D 44 24 30                  lea rax, [rsp + 0x30]
007B0529  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007B052E  48 8D 15 CB 66 35 00            lea rdx, [rip + 0x3566cb]
007B0535  41 B9 04 00 00 00               mov r9d, 4
007B053B  48 8D 44 24 4C                  lea rax, [rsp + 0x4c]
007B0540  45 8B C1                        mov r8d, r9d
007B0543  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007B0548  E8 0F 13 00 00                  call 0x1407b185c
007B054D  85 C0                           test eax, eax
007B054F  78 4E                           js 0x1407b059f
007B0551  44 84 7C 24 4C                  test byte ptr [rsp + 0x4c], r15b
007B0556  74 47                           je 0x1407b059f
007B0558  33 D2                           xor edx, edx
007B055A  48 8D 4D 80                     lea rcx, [rbp - 0x80]
007B055E  41 B8 1C 01 00 00               mov r8d, 0x11c
007B0564  E8 D7 66 F1 FF                  call 0x1406c6c40
007B0569  B8 10 00 00 00                  mov eax, 0x10
007B056E  41 B0 06                        mov r8b, 6
007B0571  49 8B CD                        mov rcx, r13
007B0574  66 89 85 98 00 00 00            mov word ptr [rbp + 0x98], ax
007B057B  8D 50 30                        lea edx, [rax + 0x30]
007B057E  E8 CD C6 CB FF                  call 0x14046cc50
007B0583  4C 8B C0                        mov r8, rax
007B0586  48 8D 4D 80                     lea rcx, [rbp - 0x80]
007B058A  BA 40 00 00 00                  mov edx, 0x40
007B058F  4C 8B E8                        mov r13, rax
007B0592  E8 D9 70 CA FF                  call 0x140457670
007B0597  85 C0                           test eax, eax
007B0599  0F 89 DA FD FF FF               jns 0x1407b0379
007B059F  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
007B05A4  48 8D 44 24 30                  lea rax, [rsp + 0x30]
007B05A9  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007B05AE  48 8D 15 1B 66 35 00            lea rdx, [rip + 0x35661b]
007B05B5  41 B9 04 00 00 00               mov r9d, 4
007B05BB  48 8D 44 24 50                  lea rax, [rsp + 0x50]
007B05C0  45 8B C1                        mov r8d, r9d
007B05C3  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007B05C8  E8 8F 12 00 00                  call 0x1407b185c
007B05CD  85 C0                           test eax, eax
007B05CF  78 0B                           js 0x1407b05dc
007B05D1  8B 44 24 50                     mov eax, dword ptr [rsp + 0x50]
007B05D5  F7 D8                           neg eax
007B05D7  1A C9                           sbb cl, cl
007B05D9  44 22 F9                        and r15b, cl
007B05DC  48 8B 54 24 40                  mov rdx, qword ptr [rsp + 0x40]
007B05E1  4C 8D 44 24 60                  lea r8, [rsp + 0x60]
007B05E6  48 8D 0D 73 65 35 00            lea rcx, [rip + 0x356573]
007B05ED  E8 D6 11 00 00                  call 0x1407b17c8
007B05F2  85 C0                           test eax, eax
007B05F4  0F 88 7F FD FF FF               js 0x1407b0379
007B05FA  44 8B F6                        mov r14d, esi
007B05FD  48 85 DB                        test rbx, rbx
007B0600  74 08                           je 0x1407b060a
007B0602  48 8B CB                        mov rcx, rbx
007B0605  E8 56 0A 00 00                  call 0x1407b1060
007B060A  BF A0 04 00 00                  mov edi, 0x4a0
007B060F  B9 01 00 00 00                  mov ecx, 1
007B0614  8B D7                           mov edx, edi
007B0616  E8 E9 D5 2A 00                  call 0x140a5dc04
007B061B  48 8B D8                        mov rbx, rax
007B061E  48 85 C0                        test rax, rax
007B0621  0F 84 56 01 00 00               je 0x1407b077d
007B0627  44 8B C7                        mov r8d, edi
007B062A  33 D2                           xor edx, edx
007B062C  48 8B C8                        mov rcx, rax
007B062F  E8 0C 66 F1 FF                  call 0x1406c6c40
007B0634  44 88 BB 98 04 00 00            mov byte ptr [rbx + 0x498], r15b
007B063B  4C 8B C3                        mov r8, rbx
007B063E  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
007B0643  41 8B D6                        mov edx, r14d
007B0646  E8 95 F7 FF FF                  call 0x1407afde0
007B064B  41 FF C6                        inc r14d
007B064E  8B F8                           mov edi, eax
007B0650  3D 1A 00 00 80                  cmp eax, 0x8000001a
007B0655  0F 84 1E FD FF FF               je 0x1407b0379
007B065B  85 C0                           test eax, eax
007B065D  79 2B                           jns 0x1407b068a
007B065F  48 8B 0D 6A 17 75 00            mov rcx, qword ptr [rip + 0x75176a]
007B0666  48 8D 15 83 1E 87 FF            lea rdx, [rip - 0x78e17d]
007B066D  E8 DE 1D BE FF                  call 0x140392450
007B0672  84 C0                           test al, al
007B0674  74 87                           je 0x1407b05fd
007B0676  0F B7 53 10                     movzx edx, word ptr [rbx + 0x10]
007B067A  44 8B C7                        mov r8d, edi
007B067D  48 8B CB                        mov rcx, rbx
007B0680  E8 97 0E 00 00                  call 0x1407b151c
007B0685  E9 73 FF FF FF                  jmp 0x1407b05fd
007B068A  83 3D 8F 19 75 00 40            cmp dword ptr [rip + 0x75198f], 0x40
007B0691  0F 83 B2 00 00 00               jae 0x1407b0749
007B0697  8B 35 23 17 75 00               mov esi, dword ptr [rip + 0x751723]
007B069D  48 8B CB                        mov rcx, rbx
007B06A0  E8 53 03 00 00                  call 0x1407b09f8
007B06A5  85 C0                           test eax, eax
007B06A7  78 4C                           js 0x1407b06f5
007B06A9  33 FF                           xor edi, edi
007B06AB  3B 7B 30                        cmp edi, dword ptr [rbx + 0x30]
007B06AE  73 12                           jae 0x1407b06c2
007B06B0  48 8B 4C FB 38                  mov rcx, qword ptr [rbx + rdi*8 + 0x38]
007B06B5  E8 3E 03 00 00                  call 0x1407b09f8
007B06BA  85 C0                           test eax, eax
007B06BC  78 37                           js 0x1407b06f5
007B06BE  FF C7                           inc edi
007B06C0  EB E9                           jmp 0x1407b06ab
007B06C2  8B 43 34                        mov eax, dword ptr [rbx + 0x34]
007B06C5  33 FF                           xor edi, edi
007B06C7  85 C0                           test eax, eax
007B06C9  74 38                           je 0x1407b0703
007B06CB  48 8B 8C FB 18 04 00 00         mov rcx, qword ptr [rbx + rdi*8 + 0x418]
007B06D3  E8 20 03 00 00                  call 0x1407b09f8
007B06D8  85 C0                           test eax, eax
007B06DA  78 19                           js 0x1407b06f5
007B06DC  8B 43 34                        mov eax, dword ptr [rbx + 0x34]
007B06DF  FF C7                           inc edi
007B06E1  3B F8                           cmp edi, eax
007B06E3  72 E6                           jb 0x1407b06cb
007B06E5  85 C0                           test eax, eax
007B06E7  74 1A                           je 0x1407b0703
007B06E9  48 8B CB                        mov rcx, rbx
007B06EC  E8 DF ED FF FF                  call 0x1407af4d0
007B06F1  85 C0                           test eax, eax
007B06F3  79 0E                           jns 0x1407b0703
007B06F5  8B CE                           mov ecx, esi
007B06F7  E8 EC 01 00 00                  call 0x1407b08e8
007B06FC  33 F6                           xor esi, esi
007B06FE  E9 FA FE FF FF                  jmp 0x1407b05fd
007B0703  83 7B 34 00                     cmp dword ptr [rbx + 0x34], 0
007B0707  48 8B CB                        mov rcx, rbx
007B070A  40 0F 97 C6                     seta sil
007B070E  40 8A D6                        mov dl, sil
007B0711  E8 FA 14 00 00                  call 0x1407b1c10
007B0716  8B 43 34                        mov eax, dword ptr [rbx + 0x34]
007B0719  33 FF                           xor edi, edi
007B071B  85 C0                           test eax, eax
007B071D  74 19                           je 0x1407b0738
007B071F  48 8B 8C FB 18 04 00 00         mov rcx, qword ptr [rbx + rdi*8 + 0x418]
007B0727  40 8A D6                        mov dl, sil
007B072A  E8 E1 14 00 00                  call 0x1407b1c10
007B072F  8B 43 34                        mov eax, dword ptr [rbx + 0x34]
007B0732  FF C7                           inc edi
007B0734  3B F8                           cmp edi, eax
007B0736  72 E7                           jb 0x1407b071f
007B0738  33 F6                           xor esi, esi
007B073A  85 C0                           test eax, eax
007B073C  0F 84 BB FE FF FF               je 0x1407b05fd
007B0742  8B DE                           mov ebx, esi
007B0744  E9 B4 FE FF FF                  jmp 0x1407b05fd
007B0749  48 8B 0D 80 16 75 00            mov rcx, qword ptr [rip + 0x751680]
007B0750  48 8D 15 F1 2A 87 FF            lea rdx, [rip - 0x78d50f]
007B0757  E8 F4 1C BE FF                  call 0x140392450
007B075C  84 C0                           test al, al
007B075E  0F 84 15 FC FF FF               je 0x1407b0379
007B0764  44 0F B7 43 10                  movzx r8d, word ptr [rbx + 0x10]
007B0769  48 8D 0D D8 2A 87 FF            lea rcx, [rip - 0x78d528]
007B0770  48 8B D3                        mov rdx, rbx
007B0773  E8 34 0E 00 00                  call 0x1407b15ac
007B0778  E9 FC FB FF FF                  jmp 0x1407b0379
007B077D  BF 9A 00 00 C0                  mov edi, 0xc000009a
007B0782  EB 0E                           jmp 0x1407b0792
007B0784  BF 05 00 00 80                  mov edi, 0x80000005
007B0789  EB 07                           jmp 0x1407b0792
007B078B  8B FE                           mov edi, esi
007B078D  E8 8A 12 00 00                  call 0x1407b1a1c
007B0792  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
007B0797  48 85 C9                        test rcx, rcx
007B079A  74 0A                           je 0x1407b07a6
007B079C  E8 0F CB EF FF                  call 0x1406ad2b0
007B07A1  48 89 74 24 58                  mov qword ptr [rsp + 0x58], rsi
007B07A6  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
007B07AB  48 85 C9                        test rcx, rcx
007B07AE  74 0A                           je 0x1407b07ba
007B07B0  E8 FB CA EF FF                  call 0x1406ad2b0
007B07B5  48 89 74 24 40                  mov qword ptr [rsp + 0x40], rsi
007B07BA  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
007B07BF  48 85 C9                        test rcx, rcx
007B07C2  74 0A                           je 0x1407b07ce
007B07C4  E8 E7 CA EF FF                  call 0x1406ad2b0
007B07C9  48 89 74 24 38                  mov qword ptr [rsp + 0x38], rsi
007B07CE  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
007B07D3  48 85 C9                        test rcx, rcx
007B07D6  74 05                           je 0x1407b07dd
007B07D8  E8 D3 CA EF FF                  call 0x1406ad2b0
007B07DD  48 85 DB                        test rbx, rbx
007B07E0  74 08                           je 0x1407b07ea
007B07E2  48 8B CB                        mov rcx, rbx
007B07E5  E8 76 08 00 00                  call 0x1407b1060
007B07EA  8B C7                           mov eax, edi
007B07EC  48 8B 8D 48 01 00 00            mov rcx, qword ptr [rbp + 0x148]
007B07F3  48 33 CC                        xor rcx, rsp
007B07F6  E8 45 BE EF FF                  call 0x1406ac640
007B07FB  4C 8D 9C 24 50 02 00 00         lea r11, [rsp + 0x250]
007B0803  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
007B0807  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
007B080B  49 8B 7B 40                     mov rdi, qword ptr [r11 + 0x40]
007B080F  49 8B E3                        mov rsp, r11
007B0812  41 5F                           pop r15
007B0814  41 5E                           pop r14
007B0816  41 5D                           pop r13
007B0818  41 5C                           pop r12
007B081A  5D                              pop rbp
007B081B  C3                              ret
007B081C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall WdipSemLoadScenarioTable(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m210;
    unsigned __int64 v_stack_m218;
    unsigned __int64 v_stack_m220;
    unsigned int v_stack_m228;
    unsigned int v_stack_m22C;
    unsigned int v_stack_m230;
    unsigned __int64 v_stack_m238;
    unsigned __int64 v_stack_m240;
    unsigned int v_stack_m248;
    unsigned __int64 v_stack_m250;
    unsigned int v_stack_m258;
    unsigned __int64 v_stack_m28;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 24) = v_rdi;
    v_rsp = (v_rsp) - (592);
    result = (*(unsigned __int64 *)(v_rip + 6661179)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 376 + 328) = result;
    v_rsi = 0;
    v_stack_m220 = 0;
    v_stack_m238 = 0;
    a2 = 0;
    v_stack_m240 = 0;
    v_stack_m218 = 0;
    v_stack_m248 = 0;
    v_stack_m230 = 0;
    v_stack_m22C = 0;
    v_stack_m210 = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 376 + 160) = v_xmm1;
    result = memset(v_rsp - 376 - 128, a2, 284, a4);
    a2 = 0;
    result = WdipSemOpenRegistryKey(v_rip + 3500316, a2, v_stack_m220, a4);
    if (sign_flag) goto loc_007B0792;
loc_007B0379:
    if (v_stack_m238 != 0) {
        result = ZwClose(v_stack_m238, a2, v_stack_m220, a4);
        v_stack_m238 = 0;
    }
    if (v_stack_m240 != 0) {
        result = ZwClose(v_stack_m240, a2, v_stack_m220, a4);
        v_stack_m240 = 0;
    }
    if (v_stack_m218 != 0) {
        result = ZwClose(v_stack_m218, a2, v_stack_m220, a4);
        v_stack_m218 = 0;
    }
    a2 = 0;
    result = memset(v_rsp - 376 + 176, a2, 152, a4);
    v_stack_m250 = v_stack_m248;
    a3 = 0;
    v_stack_m258 = 150;
    result = ZwEnumerateKey(v_stack_m220, 0, a3, v_rsp - 376 + 176);
    v_r12 = (unsigned int)((0) + 1);
    if (((unsigned int)(result)) == 0x8000001AULL) goto loc_007B078B;
    if (sign_flag) goto loc_007B0379;
    if ((*(unsigned int *)(v_rsp - 376 + 188)) >= 128) goto loc_007B0784;
    result = ((unsigned int)(*(unsigned int *)(v_rsp - 376 + 188))) >> (1);
    *(unsigned __int16 *)(v_rsp - 376 + result * 2 + 192) = 0;
    result = RtlInitUnicodeString(v_stack_m210, v_rsp - 376 + 192, a3, v_rsp - 376 + 176);
    result = RtlGUIDFromString(v_stack_m210, v_rsp - 376 + 160, a3, v_rsp - 376 + 176);
    if (sign_flag) goto loc_007B0379;
    if (*(unsigned __int64 *)(v_rip + 7674294) == 0) goto loc_007B049C;
loc_007B0469:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 7674294) + 1024))))) goto loc_007B049C;
    a2 = (0) << (4);
    a1 = (*(unsigned __int64 *)(v_rsp - 376 + 160)) - (*(unsigned __int64 *)(a2 + *(unsigned __int64 *)(v_rip + 7674294) * 1));
    if (!(condition_is_not_equal)) {
        a1 = *(unsigned __int64 *)(v_rsp - 376 + 168);
        a1 = (a1) - (*(unsigned __int64 *)(a2 + *(unsigned __int64 *)(v_rip + 7674294) * 1 + 8));
    }
    if (a1 == 0) goto loc_007B0379;
    a3 = (unsigned int)((0) + 1);
    goto loc_007B0469;
loc_007B049C:
    result = WdipSemOpenRegistryKey(v_rsp - 376 + 192, v_stack_m220, v_stack_m238, *(unsigned __int64 *)(v_rip + 7674294));
    if (sign_flag) goto loc_007B0379;
    v_stack_m228 = 1;
    result = WdipSemOpenRegistryKey(v_rip + 3499765, v_stack_m238, v_stack_m240, *(unsigned __int64 *)(v_rip + 7674294));
    if (sign_flag) goto loc_007B05DC;
    v_stack_m250 = v_stack_m248;
    v_stack_m258 = v_stack_m230;
    result = WdipSemQueryValueFromRegistry(v_stack_m240, v_rip + 3499655, 4, 4);
    if (sign_flag) goto loc_007B051F;
    if (v_stack_m230 == 0) goto loc_007B0379;
loc_007B051F:
    v_stack_m250 = v_stack_m248;
    v_stack_m258 = v_stack_m22C;
    result = WdipSemQueryValueFromRegistry(v_stack_m240, v_rip + 3499723, 4, 4);
    if (sign_flag) goto loc_007B059F;
    if (((v_stack_m22C) & (1)) == 0) goto loc_007B059F;
    a2 = 0;
    result = memset(v_rsp - 376 - 128, a2, 284, 4);
    *(unsigned __int16 *)(v_rsp - 376 + 152) = 16;
    result = VerSetConditionMask(0, 16 + 48, 6, 4);
    result = RtlVerifyVersionInfo(v_rsp - 376 - 128, 64, result, 4);
    if (!sign_flag) goto loc_007B0379;
loc_007B059F:
    v_stack_m250 = v_stack_m248;
    v_stack_m258 = v_stack_m228;
    result = WdipSemQueryValueFromRegistry(v_stack_m240, v_rip + 3499547, 4, 4);
    v_r15 = 1;
    if (!(sign_flag)) {
        result = v_stack_m228;
        result = (unsigned int)(-(result));
        v_r15 = (unsigned __int8)((1) & ((unsigned __int8)(v_stack_m240)));
    }
    result = WdipSemOpenRegistryKey(v_rip + 3499379, v_stack_m238, v_stack_m218, 4);
    if (sign_flag) goto loc_007B0379;
loc_007B05FD:
    if (0 != 0) {
        a1 = 0;
        result = WdipSemFreeScenario(a1, v_stack_m238, v_stack_m218, 4);
    }
    result = WdipSemFastAllocate(1, (unsigned int)((unsigned int)((unsigned int)(0x4A0ULL))), v_stack_m218, 4);
    if (result == 0) goto loc_007B077D;
    a2 = 0;
    result = memset(result, a2, (unsigned int)((unsigned int)((unsigned int)(0x4A0ULL))), 4);
    *(unsigned __int8 *)(result + 1176) = (unsigned __int8)(v_r15);
    result = WdipSemLoadNextScenario(v_stack_m218, 0, result, 4);
    v_r14 = (unsigned int)((0) + 1);
    if (((unsigned int)(result)) == 0x8000001AULL) goto loc_007B0379;
    if (!sign_flag) goto loc_007B068A;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 7673706), v_rip - 7922045, result, 4);
    if ((unsigned __int8)(result) == 0) goto loc_007B05FD;
    result = WdipSemWriteMisconfigEvent(result, *(unsigned __int16 *)(result + 16), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), 4);
    goto loc_007B05FD;
loc_007B068A:
    if ((*(unsigned int *)(v_rip + 7674255)) >= 64) goto loc_007B0749;
    result = WdipSemUpdateProviderTableWithEvent(result, *(unsigned __int16 *)(result + 16), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), 4);
    if (sign_flag) goto loc_007B06F5;
    v_rdi = 0;
loc_007B06AB:
    if (0 >= (*(unsigned int *)(result + 48))) goto loc_007B06C2;
    result = WdipSemUpdateProviderTableWithEvent(*(unsigned __int64 *)(result + v_rdi * 8 + 56), *(unsigned __int16 *)(result + 16), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), 4);
    if (sign_flag) goto loc_007B06F5;
    v_rdi = (unsigned int)((v_rdi) + 1);
    goto loc_007B06AB;
loc_007B06C2:
    v_rdi = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(result + 52))) == 0) goto loc_007B0703;
loc_007B06CB:
    result = WdipSemUpdateProviderTableWithEvent(*(unsigned __int64 *)(result + v_rdi * 8 + 1048), *(unsigned __int16 *)(result + 16), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), 4);
    if (sign_flag) goto loc_007B06F5;
    v_rdi = (unsigned int)((v_rdi) + 1);
    if (((unsigned int)(v_rdi)) < ((unsigned int)((unsigned int)(*(unsigned int *)(result + 52))))) goto loc_007B06CB;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(result + 52))) == 0) goto loc_007B0703;
    result = WdipSemAddScenarioToTable(result, *(unsigned __int16 *)(result + 16), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), 4);
    if (!sign_flag) goto loc_007B0703;
loc_007B06F5:
    result = WdipSemRollBackProviderTable((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 7673635)))), *(unsigned __int16 *)(result + 16), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), 4);
    v_rsi = 0;
    goto loc_007B05FD;
loc_007B0703:
    v_rsi = ((*(unsigned int *)(result + 52)) > 0) ? 1 : 0;
    result = WdipSemUpdateProviderEntryForEvent(result, (unsigned __int8)(v_rsi), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), 4);
    v_rdi = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(result + 52))) == 0) goto loc_007B0738;
loc_007B071F:
    result = WdipSemUpdateProviderEntryForEvent(*(unsigned __int64 *)(result + v_rdi * 8 + 1048), (unsigned __int8)(v_rsi), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), 4);
    v_rdi = (unsigned int)((v_rdi) + 1);
    if (((unsigned int)(v_rdi)) < ((unsigned int)((unsigned int)(*(unsigned int *)(result + 52))))) goto loc_007B071F;
loc_007B0738:
    v_rsi = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(result + 52))) == 0) goto loc_007B05FD;
    goto loc_007B05FD;
loc_007B0749:
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 7673472), v_rip - 7918863, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), 4);
    if ((unsigned __int8)(result) == 0) goto loc_007B0379;
    result = WdipSemWriteScenarioLimitExceededEvent(v_rip - 7918888, 0, *(unsigned __int16 *)(0 + 16), 4);
    goto loc_007B0379;
loc_007B077D:
    goto loc_007B0792;
loc_007B0784:
    goto loc_007B0792;
loc_007B078B:
    result = WdipSemEnableAllProviders(v_rip - 7918888, 0, *(unsigned __int16 *)(0 + 16), 4);
loc_007B0792:
    if (v_stack_m220 != 0) {
        result = ZwClose(v_stack_m220, 0, *(unsigned __int16 *)(0 + 16), 4);
        v_stack_m220 = 0;
    }
    if (v_stack_m238 != 0) {
        result = ZwClose(v_stack_m238, 0, *(unsigned __int16 *)(0 + 16), 4);
        v_stack_m238 = 0;
    }
    if (v_stack_m240 != 0) {
        result = ZwClose(v_stack_m240, 0, *(unsigned __int16 *)(0 + 16), 4);
        v_stack_m240 = 0;
    }
    if (v_stack_m218 != 0) {
        result = ZwClose(v_stack_m218, 0, *(unsigned __int16 *)(0 + 16), 4);
    }
    if (0 != 0) {
        a1 = 0;
        result = WdipSemFreeScenario(a1, 0, *(unsigned __int16 *)(0 + 16), 4);
    }
    a1 = (*(unsigned __int64 *)(v_rsp - 376 + 328)) ^ (v_rsp);
    result = _security_check_cookie(a1, 0, *(unsigned __int16 *)(0 + 16), 4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t WdipSemLoadScenarioTable(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m210;
    uint64_t v_stack_m218;
    uint64_t v_stack_m220;
    uint32_t v_stack_m228;
    uint32_t v_stack_m22C;
    uint32_t v_stack_m230;
    uint64_t v_stack_m238;
    uint64_t v_stack_m240;
    uint32_t v_stack_m248;
    uint64_t v_stack_m250;
    uint32_t v_stack_m258;
    uint64_t v_stack_m28;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    *(uint64_t *)(local_rsp + 0x18) = local_rdi;
    local_rsp = (local_rsp) - (592);
    result = (*(uint64_t *)(v_rip + 0x65A43B)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x178 + 0x148) = result;
    local_rsi = 0;
    v_stack_m220 = 0;
    v_stack_m238 = 0;
    Arg2 = 0;
    v_stack_m240 = 0;
    v_stack_m218 = 0;
    v_stack_m248 = 0;
    v_stack_m230 = 0;
    v_stack_m22C = 0;
    v_stack_m210 = v_xmm0;
    *(uint64_t *)(local_rsp - 0x178 + 0xA0) = v_xmm1;
    result = memset(local_rsp - 376 - 128, Arg2, 284, a4);
    Arg2 = 0;
    result = WdipSemOpenRegistryKey(v_rip + 3500316, Arg2, v_stack_m220, a4);
    if (sign_flag) goto loc_007B0792;
loc_007B0379:
    if (v_stack_m238 != 0) {
        result = ZwClose(v_stack_m238, Arg2, v_stack_m220, a4);
        v_stack_m238 = 0;
    }
    if (v_stack_m240 != 0) {
        result = ZwClose(v_stack_m240, Arg2, v_stack_m220, a4);
        v_stack_m240 = 0;
    }
    if (v_stack_m218 != 0) {
        result = ZwClose(v_stack_m218, Arg2, v_stack_m220, a4);
        v_stack_m218 = 0;
    }
    Arg2 = 0;
    result = memset(local_rsp - 376 + 176, Arg2, 152, a4);
    v_stack_m250 = v_stack_m248;
    a3 = 0;
    v_stack_m258 = 150;
    result = ZwEnumerateKey(v_stack_m220, 0, a3, local_rsp - 376 + 176);
    local_r12 = (uint32_t)((0) + 1);
    if (((uint32_t)(result)) == 0x8000001AULL) goto loc_007B078B;
    if (sign_flag) goto loc_007B0379;
    if ((*(uint32_t *)(local_rsp - 0x178 + 0xBC)) >= 128) goto loc_007B0784;
    result = ((uint32_t)(*(uint32_t *)(local_rsp - 0x178 + 0xBC))) >> (1);
    *(uint16_t *)(local_rsp - 0x178 + result * 2 + 0xC0) = 0;
    result = RtlInitUnicodeString(v_stack_m210, local_rsp - 376 + 192, a3, local_rsp - 376 + 176);
    result = RtlGUIDFromString(v_stack_m210, local_rsp - 376 + 160, a3, local_rsp - 376 + 176);
    if (sign_flag) goto loc_007B0379;
    if (*(uint64_t *)(v_rip + 0x7519B6) == 0) goto loc_007B049C;
loc_007B0469:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x7519B6) + 0x400))))) goto loc_007B049C;
    Arg2 = (0) << (4);
    Arg1 = (*(uint64_t *)(local_rsp - 0x178 + 0xA0)) - (*(uint64_t *)(Arg2 + *(uint64_t *)(v_rip + 0x7519B6) * 1));
    if (!(condition_is_not_equal)) {
        Arg1 = *(uint64_t *)(local_rsp - 0x178 + 0xA8);
        Arg1 = (Arg1) - (*(uint64_t *)(Arg2 + *(uint64_t *)(v_rip + 0x7519B6) * 1 + 0x8));
    }
    if (Arg1 == 0) goto loc_007B0379;
    a3 = (uint32_t)((0) + 1);
    goto loc_007B0469;
loc_007B049C:
    result = WdipSemOpenRegistryKey(local_rsp - 376 + 192, v_stack_m220, v_stack_m238, *(uint64_t *)(v_rip + 0x7519B6));
    if (sign_flag) goto loc_007B0379;
    v_stack_m228 = 1;
    result = WdipSemOpenRegistryKey(v_rip + 3499765, v_stack_m238, v_stack_m240, *(uint64_t *)(v_rip + 0x7519B6));
    if (sign_flag) goto loc_007B05DC;
    v_stack_m250 = v_stack_m248;
    v_stack_m258 = v_stack_m230;
    result = WdipSemQueryValueFromRegistry(v_stack_m240, v_rip + 3499655, 4, 4);
    if (sign_flag) goto loc_007B051F;
    if (v_stack_m230 == 0) goto loc_007B0379;
loc_007B051F:
    v_stack_m250 = v_stack_m248;
    v_stack_m258 = v_stack_m22C;
    result = WdipSemQueryValueFromRegistry(v_stack_m240, v_rip + 3499723, 4, 4);
    if (sign_flag) goto loc_007B059F;
    if (((v_stack_m22C) & (1)) == 0) goto loc_007B059F;
    Arg2 = 0;
    result = memset(local_rsp - 376 - 128, Arg2, 284, 4);
    *(uint16_t *)(local_rsp - 0x178 + 0x98) = 16;
    result = VerSetConditionMask(0, 16 + 48, 6, 4);
    result = RtlVerifyVersionInfo(local_rsp - 376 - 128, 64, result, 4);
    if (!sign_flag) goto loc_007B0379;
loc_007B059F:
    v_stack_m250 = v_stack_m248;
    v_stack_m258 = v_stack_m228;
    result = WdipSemQueryValueFromRegistry(v_stack_m240, v_rip + 3499547, 4, 4);
    local_r15 = 1;
    if (!(sign_flag)) {
        result = v_stack_m228;
        result = (uint32_t)(-(result));
        local_r15 = (uint8_t)((1) & ((uint8_t)(v_stack_m240)));
    }
    result = WdipSemOpenRegistryKey(v_rip + 3499379, v_stack_m238, v_stack_m218, 4);
    if (sign_flag) goto loc_007B0379;
loc_007B05FD:
    if (0 != 0) {
        Arg1 = 0;
        result = WdipSemFreeScenario(Arg1, v_stack_m238, v_stack_m218, 4);
    }
    result = WdipSemFastAllocate(1, (uint32_t)((uint32_t)((uint32_t)(0x4A0ULL))), v_stack_m218, 4);
    if (result == 0) goto loc_007B077D;
    Arg2 = 0;
    result = memset(result, Arg2, (uint32_t)((uint32_t)((uint32_t)(0x4A0ULL))), 4);
    *(uint8_t *)(result + 0x498) = (uint8_t)(local_r15);
    result = WdipSemLoadNextScenario(v_stack_m218, 0, result, 4);
    local_r14 = (uint32_t)((0) + 1);
    if (((uint32_t)(result)) == 0x8000001AULL) goto loc_007B0379;
    if (!sign_flag) goto loc_007B068A;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x75176A), v_rip - 7922045, result, 4);
    if ((uint8_t)(result) == 0) goto loc_007B05FD;
    result = WdipSemWriteMisconfigEvent(result, *(uint16_t *)(result + 0x10), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), 4);
    goto loc_007B05FD;
loc_007B068A:
    if ((*(uint32_t *)(v_rip + 0x75198F)) >= 64) goto loc_007B0749;
    result = WdipSemUpdateProviderTableWithEvent(result, *(uint16_t *)(result + 0x10), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), 4);
    if (sign_flag) goto loc_007B06F5;
    local_rdi = 0;
loc_007B06AB:
    if (0 >= (*(uint32_t *)(result + 0x30))) goto loc_007B06C2;
    result = WdipSemUpdateProviderTableWithEvent(*(uint64_t *)(result + local_rdi * 8 + 0x38), *(uint16_t *)(result + 0x10), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), 4);
    if (sign_flag) goto loc_007B06F5;
    local_rdi = (uint32_t)((local_rdi) + 1);
    goto loc_007B06AB;
loc_007B06C2:
    local_rdi = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x34))) == 0) goto loc_007B0703;
loc_007B06CB:
    result = WdipSemUpdateProviderTableWithEvent(*(uint64_t *)(result + local_rdi * 8 + 0x418), *(uint16_t *)(result + 0x10), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), 4);
    if (sign_flag) goto loc_007B06F5;
    local_rdi = (uint32_t)((local_rdi) + 1);
    if (((uint32_t)(local_rdi)) < ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x34))))) goto loc_007B06CB;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x34))) == 0) goto loc_007B0703;
    result = WdipSemAddScenarioToTable(result, *(uint16_t *)(result + 0x10), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), 4);
    if (!sign_flag) goto loc_007B0703;
loc_007B06F5:
    result = WdipSemRollBackProviderTable((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x751723)))), *(uint16_t *)(result + 0x10), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), 4);
    local_rsi = 0;
    goto loc_007B05FD;
loc_007B0703:
    local_rsi = ((*(uint32_t *)(result + 0x34)) > 0) ? 1 : 0;
    result = WdipSemUpdateProviderEntryForEvent(result, (uint8_t)(local_rsi), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), 4);
    local_rdi = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x34))) == 0) goto loc_007B0738;
loc_007B071F:
    result = WdipSemUpdateProviderEntryForEvent(*(uint64_t *)(result + local_rdi * 8 + 0x418), (uint8_t)(local_rsi), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), 4);
    local_rdi = (uint32_t)((local_rdi) + 1);
    if (((uint32_t)(local_rdi)) < ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x34))))) goto loc_007B071F;
loc_007B0738:
    local_rsi = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x34))) == 0) goto loc_007B05FD;
    goto loc_007B05FD;
loc_007B0749:
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x751680), v_rip - 7918863, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), 4);
    if ((uint8_t)(result) == 0) goto loc_007B0379;
    result = WdipSemWriteScenarioLimitExceededEvent(v_rip - 7918888, 0, *(uint16_t *)(0 + 0x10), 4);
    goto loc_007B0379;
loc_007B077D:
    goto loc_007B0792;
loc_007B0784:
    goto loc_007B0792;
loc_007B078B:
    result = WdipSemEnableAllProviders(v_rip - 7918888, 0, *(uint16_t *)(0 + 0x10), 4);
loc_007B0792:
    if (v_stack_m220 != 0) {
        result = ZwClose(v_stack_m220, 0, *(uint16_t *)(0 + 0x10), 4);
        v_stack_m220 = 0;
    }
    if (v_stack_m238 != 0) {
        result = ZwClose(v_stack_m238, 0, *(uint16_t *)(0 + 0x10), 4);
        v_stack_m238 = 0;
    }
    if (v_stack_m240 != 0) {
        result = ZwClose(v_stack_m240, 0, *(uint16_t *)(0 + 0x10), 4);
        v_stack_m240 = 0;
    }
    if (v_stack_m218 != 0) {
        result = ZwClose(v_stack_m218, 0, *(uint16_t *)(0 + 0x10), 4);
    }
    if (0 != 0) {
        Arg1 = 0;
        result = WdipSemFreeScenario(Arg1, 0, *(uint16_t *)(0 + 0x10), 4);
    }
    Arg1 = (*(uint64_t *)(local_rsp - 0x178 + 0x148)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, 0, *(uint16_t *)(0 + 0x10), 4);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007B02D8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
