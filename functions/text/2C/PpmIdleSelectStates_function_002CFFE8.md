# PpmIdleSelectStates

- RVA: `0x002CFFE8`–`0x002D091D` (길이 `2,357` bytes)
- VA: `0x00000001402CFFE8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006F6F0`
- 디코드: `597`개 명령, `2,357/2,357` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **34**; 고유 호출 대상: **21**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **9**

### Outgoing calls
- `0x002D006B` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x002D00F3` → [PpmIdleEvaluateConstraints](../4C/PpmIdleEvaluateConstraints_function_004CD400.md) (function, `0x004CD400`)
- `0x002D0119` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x002D011E` → [Feature_PpmDynamicHintAdjust__private_IsEnabledNoReportingNoInline](../4F/Feature_PpmDynamicHintAdjust__private_IsEnabledNoReportingNoInline_function_004FC610.md) (function, `0x004FC610`)
- `0x002D016D` → [PpmComputeIdleDurationHint](../4C/PpmComputeIdleDurationHint_function_004C7920.md) (function, `0x004C7920`)
- `0x002D01C1` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x002D0202` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x002D020A` → [PoCopyDeepIdleMask](../3C/PoCopyDeepIdleMask_function_003C04C8.md) (function, `0x003C04C8`)
- `0x002D0216` → [KeAddProcessorAffinityEx](../25/KeAddProcessorAffinityEx_function_0025B6F0.md) (function, `0x0025B6F0`)
- `0x002D0244` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x002D029A` → [PpmCheckPreConditionsForDeepSleep](../5C/PpmCheckPreConditionsForDeepSleep_function_005CF588.md) (function, `0x005CF588`)
- `0x002D0332` → [PpmEstimateIdleDuration](../4C/PpmEstimateIdleDuration_function_004C79DC.md) (function, `0x004C79DC`)
- `0x002D038F` → [PpmIdleCheckCoordinatedStateEligibility](../5C/PpmIdleCheckCoordinatedStateEligibility_function_005CFACC.md) (function, `0x005CFACC`)
- `0x002D03C2` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x002D03E3` → [PpmIdleUpdateSelectionStatistics](../5D/PpmIdleUpdateSelectionStatistics_function_005D04D4.md) (function, `0x005D04D4`)
- `0x002D0421` → [KeStallExecutionProcessor](../44/KeStallExecutionProcessor_function_0044F620.md) (function, `0x0044F620`)
- `0x002D0437` → [PpmIdleRecheckSecondaryProcessors](../5D/PpmIdleRecheckSecondaryProcessors_function_005D0204.md) (function, `0x005D0204`)
- `0x002D0497` → [PpmIdleUpdateIdleReevaluationDuration](../5D/PpmIdleUpdateIdleReevaluationDuration_function_005D0430.md) (function, `0x005D0430`)
- `0x002D04C1` → [PpmIdleRollbackCoordinatedSelection](../5D/PpmIdleRollbackCoordinatedSelection_function_005D02A4.md) (function, `0x005D02A4`)
- `0x002D0540` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x002D0564` → [KiSubtractAffinityEx](../2D/KiSubtractAffinityEx_function_002D61E8.md) (function, `0x002D61E8`)
- `0x002D0574` → [PpmUnlockProcessors](../2D/PpmUnlockProcessors_function_002D15B0.md) (function, `0x002D15B0`)
- `0x002D05A0` → [PpmUnlockProcessors](../2D/PpmUnlockProcessors_function_002D15B0.md) (function, `0x002D15B0`)
- `0x002D05C4` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x002D0614` → [PpmCheckPreConditionsForDeepSleep](../5C/PpmCheckPreConditionsForDeepSleep_function_005CF588.md) (function, `0x005CF588`)
- `0x002D0689` → [PpmEstimateIdleDuration](../4C/PpmEstimateIdleDuration_function_004C79DC.md) (function, `0x004C79DC`)
- `0x002D06CC` → [PpmIdleCheckProcessorStateEligibility](../5C/PpmIdleCheckProcessorStateEligibility_function_005CFD54.md) (function, `0x005CFD54`)
- `0x002D06F3` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x002D071B` → [PpmIdleUpdateSelectionStatistics](../5D/PpmIdleUpdateSelectionStatistics_function_005D04D4.md) (function, `0x005D04D4`)
- `0x002D0758` → [PpmIdleUpdateIdleReevaluationDuration](../5D/PpmIdleUpdateIdleReevaluationDuration_function_005D0430.md) (function, `0x005D0430`)
- `0x002D07EE` → [PpmIdleSetSynchronizationState](../4D/PpmIdleSetSynchronizationState_function_004D9958.md) (function, `0x004D9958`)
- `0x002D0844` → [EtwTraceKernelEvent](../23/EtwTraceKernelEvent_function_00235350.md) (function, `0x00235350`)
- `0x002D088C` → [EtwTraceKernelEvent](../23/EtwTraceKernelEvent_function_00235350.md) (function, `0x00235350`)
- `0x002D08FC` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PoIdle](PoIdle_function_002CFB40.md) at `0x002CFC56`

### Static image references
- `0x002D0007` → RVA `0x00E0A740` (`.data`; read)
- `0x002D009D` → RVA `0x00FC6AD0` (`ALMOSTRO`; read)
- `0x002D012D` → RVA `0x00FC6AA0` (`ALMOSTRO`; read)
- `0x002D0177` → RVA `0x00FC6A85` (`ALMOSTRO`; read)
- `0x002D0186` → RVA `0x00FC6F58` (`ALMOSTRO`; read)
- `0x002D025F` → RVA `0x00E0B3B0` (`.data`; read)
- `0x002D0288` → RVA `0x00E0B3B4` (`.data`; read)
- `0x002D02AD` → RVA `0x00E27E1C` (`.data`; read)
- `0x002D080B` → RVA `0x00FC6B08` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002CFFE8  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
002CFFED  55                              push rbp
002CFFEE  56                              push rsi
002CFFEF  57                              push rdi
002CFFF0  41 54                           push r12
002CFFF2  41 55                           push r13
002CFFF4  41 56                           push r14
002CFFF6  41 57                           push r15
002CFFF8  48 8D AC 24 B0 FE FF FF         lea rbp, [rsp - 0x150]
002D0000  48 81 EC 50 02 00 00            sub rsp, 0x250
002D0007  48 8B 05 32 A7 B3 00            mov rax, qword ptr [rip + 0xb3a732]
002D000E  48 33 C4                        xor rax, rsp
002D0011  48 89 85 40 01 00 00            mov qword ptr [rbp + 0x140], rax
002D0018  48 8B 85 B0 01 00 00            mov rax, qword ptr [rbp + 0x1b0]
002D001F  49 8B D8                        mov rbx, r8
002D0022  48 89 45 08                     mov qword ptr [rbp + 8], rax
002D0026  40 8A F2                        mov sil, dl
002D0029  48 8B 85 B8 01 00 00            mov rax, qword ptr [rbp + 0x1b8]
002D0030  4C 8B E9                        mov r13, rcx
002D0033  48 89 45 F8                     mov qword ptr [rbp - 8], rax
002D0037  48 8D 4D 30                     lea rcx, [rbp + 0x30]
002D003B  48 8B 85 C0 01 00 00            mov rax, qword ptr [rbp + 0x1c0]
002D0042  33 D2                           xor edx, edx
002D0044  48 89 45 00                     mov qword ptr [rbp], rax
002D0048  41 B8 08 01 00 00               mov r8d, 0x108
002D004E  48 8B 85 C8 01 00 00            mov rax, qword ptr [rbp + 0x1c8]
002D0055  4D 8B F1                        mov r14, r9
002D0058  48 89 45 10                     mov qword ptr [rbp + 0x10], rax
002D005C  48 8B 85 D0 01 00 00            mov rax, qword ptr [rbp + 0x1d0]
002D0063  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
002D0067  4C 89 4D A8                     mov qword ptr [rbp - 0x58], r9
002D006B  E8 D0 6B 3F 00                  call 0x1406c6c40
002D0070  49 8B BD 40 88 00 00            mov rdi, qword ptr [r13 + 0x8840]
002D0077  33 C9                           xor ecx, ecx
002D0079  49 8B 85 48 88 00 00            mov rax, qword ptr [r13 + 0x8848]
002D0080  44 8B F9                        mov r15d, ecx
002D0083  48 89 45 18                     mov qword ptr [rbp + 0x18], rax
002D0087  49 8B D6                        mov rdx, r14
002D008A  89 4C 24 54                     mov dword ptr [rsp + 0x54], ecx
002D008E  48 8B 87 98 02 00 00            mov rax, qword ptr [rdi + 0x298]
002D0095  44 8D 61 01                     lea r12d, [rcx + 1]
002D0099  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
002D009D  48 8B 05 2C 6A CF 00            mov rax, qword ptr [rip + 0xcf6a2c]
002D00A4  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
002D00A9  8A 07                           mov al, byte ptr [rdi]
002D00AB  84 C0                           test al, al
002D00AD  48 89 4D D8                     mov qword ptr [rbp - 0x28], rcx
002D00B1  89 4C 24 58                     mov dword ptr [rsp + 0x58], ecx
002D00B5  48 89 4D 88                     mov qword ptr [rbp - 0x78], rcx
002D00B9  0F 94 44 24 5D                  sete byte ptr [rsp + 0x5d]
002D00BE  89 4C 24 6C                     mov dword ptr [rsp + 0x6c], ecx
002D00C2  48 89 4D 98                     mov qword ptr [rbp - 0x68], rcx
002D00C6  89 4D 80                        mov dword ptr [rbp - 0x80], ecx
002D00C9  89 4C 24 60                     mov dword ptr [rsp + 0x60], ecx
002D00CD  89 4C 24 68                     mov dword ptr [rsp + 0x68], ecx
002D00D1  48 89 4D B8                     mov qword ptr [rbp - 0x48], rcx
002D00D5  48 89 4D C0                     mov qword ptr [rbp - 0x40], rcx
002D00D9  48 89 4D B0                     mov qword ptr [rbp - 0x50], rcx
002D00DD  48 89 4D C8                     mov qword ptr [rbp - 0x38], rcx
002D00E1  89 4D 84                        mov dword ptr [rbp - 0x7c], ecx
002D00E4  88 4C 24 50                     mov byte ptr [rsp + 0x50], cl
002D00E8  89 4C 24 64                     mov dword ptr [rsp + 0x64], ecx
002D00EC  49 8B CD                        mov rcx, r13
002D00EF  88 44 24 5E                     mov byte ptr [rsp + 0x5e], al
002D00F3  E8 08 D3 1F 00                  call 0x1404cd400
002D00F8  4C 8D B7 50 01 00 00            lea r14, [rdi + 0x150]
002D00FF  48 89 03                        mov qword ptr [rbx], rax
002D0102  45 21 7E 04                     and dword ptr [r14 + 4], r15d
002D0106  49 8D 4E 08                     lea rcx, [r14 + 8]
002D010A  33 D2                           xor edx, edx
002D010C  41 C7 06 01 00 20 00            mov dword ptr [r14], 0x200001
002D0113  41 B8 00 01 00 00               mov r8d, 0x100
002D0119  E8 22 6B 3F 00                  call 0x1406c6c40
002D011E  E8 ED C4 22 00                  call 0x1404fc610
002D0123  85 C0                           test eax, eax
002D0125  74 32                           je 0x1402d0159
002D0127  48 8B 45 A8                     mov rax, qword ptr [rbp - 0x58]
002D012B  33 D2                           xor edx, edx
002D012D  44 8B 0D 6C 69 CF 00            mov r9d, dword ptr [rip + 0xcf696c]
002D0134  4C 8B 00                        mov r8, qword ptr [rax]
002D0137  49 8B C0                        mov rax, r8
002D013A  49 F7 F1                        div r9
002D013D  41 3B 85 C0 38 00 00            cmp eax, dword ptr [r13 + 0x38c0]
002D0144  75 0F                           jne 0x1402d0155
002D0146  FF C0                           inc eax
002D0148  41 0F AF C1                     imul eax, r9d
002D014C  41 2B C0                        sub eax, r8d
002D014F  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
002D0153  EB 07                           jmp 0x1402d015c
002D0155  33 C0                           xor eax, eax
002D0157  EB F6                           jmp 0x1402d014f
002D0159  41 8B C7                        mov eax, r15d
002D015C  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
002D0160  44 8A CE                        mov r9b, sil
002D0163  48 8B 45 A8                     mov rax, qword ptr [rbp - 0x58]
002D0167  49 8B CD                        mov rcx, r13
002D016A  4C 8B 00                        mov r8, qword ptr [rax]
002D016D  E8 AE 77 1F 00                  call 0x1404c7920
002D0172  40 84 F6                        test sil, sil
002D0175  74 20                           je 0x1402d0197
002D0177  44 38 3D 07 69 CF 00            cmp byte ptr [rip + 0xcf6907], r15b
002D017E  75 17                           jne 0x1402d0197
002D0180  45 38 7D 21                     cmp byte ptr [r13 + 0x21], r15b
002D0184  75 11                           jne 0x1402d0197
002D0186  48 8B 15 CB 6D CF 00            mov rdx, qword ptr [rip + 0xcf6dcb]
002D018D  48 89 55 90                     mov qword ptr [rbp - 0x70], rdx
002D0191  48 89 55 D0                     mov qword ptr [rbp - 0x30], rdx
002D0195  EB 0C                           jmp 0x1402d01a3
002D0197  48 83 C8 FF                     or rax, 0xffffffffffffffff
002D019B  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
002D019F  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
002D01A3  48 8B 87 68 02 00 00            mov rax, qword ptr [rdi + 0x268]
002D01AA  BE FF FF FF FF                  mov esi, 0xffffffff
002D01AF  8B CE                           mov ecx, esi
002D01B1  48 85 C0                        test rax, rax
002D01B4  74 12                           je 0x1402d01c8
002D01B6  48 8B 4D E0                     mov rcx, qword ptr [rbp - 0x20]
002D01BA  48 8D 97 A0 02 00 00            lea rdx, [rdi + 0x2a0]
002D01C1  E8 0A A9 3E 00                  call 0x1406baad0
002D01C6  8B C8                           mov ecx, eax
002D01C8  4C 8B 74 24 70                  mov r14, qword ptr [rsp + 0x70]
002D01CD  33 C0                           xor eax, eax
002D01CF  41 38 85 89 88 00 00            cmp byte ptr [r13 + 0x8889], al
002D01D6  0F 44 C1                        cmove eax, ecx
002D01D9  89 45 A4                        mov dword ptr [rbp - 0x5c], eax
002D01DC  4D 85 F6                        test r14, r14
002D01DF  0F 84 C0 03 00 00               je 0x1402d05a5
002D01E5  48 8D 9F D0 02 00 00            lea rbx, [rdi + 0x2d0]
002D01EC  33 D2                           xor edx, edx
002D01EE  44 21 7B 04                     and dword ptr [rbx + 4], r15d
002D01F2  48 8D 4B 08                     lea rcx, [rbx + 8]
002D01F6  41 B8 00 01 00 00               mov r8d, 0x100
002D01FC  C7 03 01 00 20 00               mov dword ptr [rbx], 0x200001
002D0202  E8 39 6A 3F 00                  call 0x1406c6c40
002D0207  48 8B CB                        mov rcx, rbx
002D020A  E8 B9 02 0F 00                  call 0x1403c04c8
002D020F  41 8B 55 24                     mov edx, dword ptr [r13 + 0x24]
002D0213  48 8B CB                        mov rcx, rbx
002D0216  E8 D5 B4 F8 FF                  call 0x14025b6f0
002D021B  49 8B 46 30                     mov rax, qword ptr [r14 + 0x30]
002D021F  48 8D 9F 08 04 00 00            lea rbx, [rdi + 0x408]
002D0226  48 8B 8F E0 03 00 00            mov rcx, qword ptr [rdi + 0x3e0]
002D022D  33 D2                           xor edx, edx
002D022F  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
002D0233  41 8B 06                        mov eax, dword ptr [r14]
002D0236  48 89 4D 88                     mov qword ptr [rbp - 0x78], rcx
002D023A  8D 04 85 08 00 00 00            lea eax, [rax*4 + 8]
002D0241  4C 63 C0                        movsxd r8, eax
002D0244  E8 F7 69 3F 00                  call 0x1406c6c40
002D0249  33 C0                           xor eax, eax
002D024B  8B D0                           mov edx, eax
002D024D  8D 48 01                        lea ecx, [rax + 1]
002D0250  89 45 A0                        mov dword ptr [rbp - 0x60], eax
002D0253  3B 87 F8 03 00 00               cmp eax, dword ptr [rdi + 0x3f8]
002D0259  0F 83 2A 03 00 00               jae 0x1402d0589
002D025F  80 3D 4A B1 B3 00 00            cmp byte ptr [rip + 0xb3b14a], 0
002D0266  0F 85 68 02 00 00               jne 0x1402d04d4
002D026C  4C 8D 34 40                     lea r14, [rax + rax*2]
002D0270  48 8B 87 00 04 00 00            mov rax, qword ptr [rdi + 0x400]
002D0277  42 80 7C F0 01 00               cmp byte ptr [rax + r14*8 + 1], 0
002D027D  0F 84 51 02 00 00               je 0x1402d04d4
002D0283  46 8B 74 F0 04                  mov r14d, dword ptr [rax + r14*8 + 4]
002D0288  8B 05 26 B1 B3 00               mov eax, dword ptr [rip + 0xb3b126]
002D028E  3B C6                           cmp eax, esi
002D0290  74 33                           je 0x1402d02c5
002D0292  44 3B F0                        cmp r14d, eax
002D0295  72 2E                           jb 0x1402d02c5
002D0297  49 8B CD                        mov rcx, r13
002D029A  E8 E9 F2 2F 00                  call 0x1405cf588
002D029F  B9 01 00 00 00                  mov ecx, 1
002D02A4  84 C0                           test al, al
002D02A6  74 1D                           je 0x1402d02c5
002D02A8  83 7C 24 54 00                  cmp dword ptr [rsp + 0x54], 0
002D02AD  8B 05 69 7B B5 00               mov eax, dword ptr [rip + 0xb57b69]
002D02B3  45 0F B6 E4                     movzx r12d, r12b
002D02B7  44 0F 44 E1                     cmove r12d, ecx
002D02BB  F7 D8                           neg eax
002D02BD  1B C0                           sbb eax, eax
002D02BF  F7 D8                           neg eax
002D02C1  03 C1                           add eax, ecx
002D02C3  EB 0F                           jmp 0x1402d02d4
002D02C5  83 7C 24 54 00                  cmp dword ptr [rsp + 0x54], 0
002D02CA  45 0F B6 E4                     movzx r12d, r12b
002D02CE  44 0F 45 E1                     cmovne r12d, ecx
002D02D2  33 C0                           xor eax, eax
002D02D4  89 44 24 54                     mov dword ptr [rsp + 0x54], eax
002D02D8  44 89 64 24 78                  mov dword ptr [rsp + 0x78], r12d
002D02DD  45 84 E4                        test r12b, r12b
002D02E0  74 6D                           je 0x1402d034f
002D02E2  8B 4C 24 64                     mov ecx, dword ptr [rsp + 0x64]
002D02E6  45 32 E4                        xor r12b, r12b
002D02E9  4C 8B 4D A8                     mov r9, qword ptr [rbp - 0x58]
002D02ED  85 C0                           test eax, eax
002D02EF  89 4C 24 48                     mov dword ptr [rsp + 0x48], ecx
002D02F3  8B D0                           mov edx, eax
002D02F5  48 8D 4C 24 68                  lea rcx, [rsp + 0x68]
002D02FA  44 89 64 24 78                  mov dword ptr [rsp + 0x78], r12d
002D02FF  48 89 4C 24 40                  mov qword ptr [rsp + 0x40], rcx
002D0304  41 0F 95 C0                     setne r8b
002D0308  4D 8B 09                        mov r9, qword ptr [r9]
002D030B  48 8D 4D 84                     lea rcx, [rbp - 0x7c]
002D030F  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
002D0314  48 8D 4D C8                     lea rcx, [rbp - 0x38]
002D0318  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
002D031D  48 8D 4D C0                     lea rcx, [rbp - 0x40]
002D0321  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
002D0326  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
002D032A  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
002D032F  49 8B CD                        mov rcx, r13
002D0332  E8 A5 76 1F 00                  call 0x1404c79dc
002D0337  48 8B 45 C0                     mov rax, qword ptr [rbp - 0x40]
002D033B  48 89 45 B8                     mov qword ptr [rbp - 0x48], rax
002D033F  8B 44 24 68                     mov eax, dword ptr [rsp + 0x68]
002D0343  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
002D0347  48 8B 45 C8                     mov rax, qword ptr [rbp - 0x38]
002D034B  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
002D034F  48 83 64 24 48 00               and qword ptr [rsp + 0x48], 0
002D0355  48 8D 44 24 58                  lea rax, [rsp + 0x58]
002D035A  83 63 04 00                     and dword ptr [rbx + 4], 0
002D035E  45 33 C0                        xor r8d, r8d
002D0361  4C 8B 4D B8                     mov r9, qword ptr [rbp - 0x48]
002D0365  49 8B CD                        mov rcx, r13
002D0368  8B 55 A4                        mov edx, dword ptr [rbp - 0x5c]
002D036B  48 89 5C 24 40                  mov qword ptr [rsp + 0x40], rbx
002D0370  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
002D0375  48 8B 45 A8                     mov rax, qword ptr [rbp - 0x58]
002D0379  44 89 74 24 30                  mov dword ptr [rsp + 0x30], r14d
002D037E  44 89 74 24 28                  mov dword ptr [rsp + 0x28], r14d
002D0383  89 74 24 58                     mov dword ptr [rsp + 0x58], esi
002D0387  48 8B 00                        mov rax, qword ptr [rax]
002D038A  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
002D038F  E8 38 F7 2F 00                  call 0x1405cfacc
002D0394  4C 8B 54 24 70                  mov r10, qword ptr [rsp + 0x70]
002D0399  48 8B D8                        mov rbx, rax
002D039C  8B 4C 24 58                     mov ecx, dword ptr [rsp + 0x58]
002D03A0  89 4C 24 58                     mov dword ptr [rsp + 0x58], ecx
002D03A4  41 80 7A 08 00                  cmp byte ptr [r10 + 8], 0
002D03A9  75 23                           jne 0x1402d03ce
002D03AB  48 85 C0                        test rax, rax
002D03AE  75 1E                           jne 0x1402d03ce
002D03B0  49 8B 42 10                     mov rax, qword ptr [r10 + 0x10]
002D03B4  48 85 C0                        test rax, rax
002D03B7  74 15                           je 0x1402d03ce
002D03B9  8B D1                           mov edx, ecx
002D03BB  45 8B C6                        mov r8d, r14d
002D03BE  48 8B 4D E0                     mov rcx, qword ptr [rbp - 0x20]
002D03C2  E8 09 A7 3E 00                  call 0x1406baad0
002D03C7  4C 8B 54 24 70                  mov r10, qword ptr [rsp + 0x70]
002D03CC  8B D8                           mov ebx, eax
002D03CE  48 8B 55 F0                     mov rdx, qword ptr [rbp - 0x10]
002D03D2  49 8B C6                        mov rax, r14
002D03D5  48 C1 E0 0A                     shl rax, 0xa
002D03D9  48 83 C2 58                     add rdx, 0x58
002D03DD  48 03 D0                        add rdx, rax
002D03E0  48 8B CB                        mov rcx, rbx
002D03E3  E8 EC 00 30 00                  call 0x1405d04d4
002D03E8  B8 FF FF FF FF                  mov eax, 0xffffffff
002D03ED  49 69 F6 C0 01 00 00            imul rsi, r14, 0x1c0
002D03F4  48 3B D8                        cmp rbx, rax
002D03F7  74 59                           je 0x1402d0452
002D03F9  4E 8B 7C 16 40                  mov r15, qword ptr [rsi + r10 + 0x40]
002D03FE  48 85 DB                        test rbx, rbx
002D0401  75 4F                           jne 0x1402d0452
002D0403  0F B6 47 41                     movzx eax, byte ptr [rdi + 0x41]
002D0407  4D 8B E7                        mov r12, r15
002D040A  84 C0                           test al, al
002D040C  0F 84 F5 00 00 00               je 0x1402d0507
002D0412  38 5C 24 50                     cmp byte ptr [rsp + 0x50], bl
002D0416  0F 85 EB 00 00 00               jne 0x1402d0507
002D041C  8D 0C 80                        lea ecx, [rax + rax*4]
002D041F  03 C9                           add ecx, ecx
002D0421  E8 FA F1 17 00                  call 0x14044f620
002D0426  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
002D042B  48 83 E9 80                     sub rcx, -0x80
002D042F  C6 44 24 50 01                  mov byte ptr [rsp + 0x50], 1
002D0434  48 03 CE                        add rcx, rsi
002D0437  E8 C8 FD 2F 00                  call 0x1405d0204
002D043C  84 C0                           test al, al
002D043E  0F 85 BE 00 00 00               jne 0x1402d0502
002D0444  44 8B 64 24 78                  mov r12d, dword ptr [rsp + 0x78]
002D0449  BE FF FF FF FF                  mov esi, 0xffffffff
002D044E  8B DE                           mov ebx, esi
002D0450  EB 66                           jmp 0x1402d04b8
002D0452  8A 4C 24 50                     mov cl, byte ptr [rsp + 0x50]
002D0456  BA 03 00 00 80                  mov edx, 0x80000003
002D045B  88 4C 24 50                     mov byte ptr [rsp + 0x50], cl
002D045F  48 8B C3                        mov rax, rbx
002D0462  48 89 5C 24 78                  mov qword ptr [rsp + 0x78], rbx
002D0467  48 3B DA                        cmp rbx, rdx
002D046A  74 13                           je 0x1402d047f
002D046C  88 4C 24 50                     mov byte ptr [rsp + 0x50], cl
002D0470  B9 08 00 00 80                  mov ecx, 0x80000008
002D0475  48 89 5C 24 78                  mov qword ptr [rsp + 0x78], rbx
002D047A  48 3B C1                        cmp rax, rcx
002D047D  75 34                           jne 0x1402d04b3
002D047F  4C 8B 4D B0                     mov r9, qword ptr [rbp - 0x50]
002D0483  48 8D 45 D0                     lea rax, [rbp - 0x30]
002D0487  44 8B 44 24 60                  mov r8d, dword ptr [rsp + 0x60]
002D048C  48 8B D3                        mov rdx, rbx
002D048F  49 8B CD                        mov rcx, r13
002D0492  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
002D0497  E8 94 FF 2F 00                  call 0x1405d0430
002D049C  84 C0                           test al, al
002D049E  45 0F B6 E4                     movzx r12d, r12b
002D04A2  B8 01 00 00 00                  mov eax, 1
002D04A7  44 0F 45 E0                     cmovne r12d, eax
002D04AB  48 8B 45 D0                     mov rax, qword ptr [rbp - 0x30]
002D04AF  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
002D04B3  BE FF FF FF FF                  mov esi, 0xffffffff
002D04B8  33 D2                           xor edx, edx
002D04BA  48 8D 8F 08 04 00 00            lea rcx, [rdi + 0x408]
002D04C1  E8 DE FD 2F 00                  call 0x1405d02a4
002D04C6  8B 54 24 6C                     mov edx, dword ptr [rsp + 0x6c]
002D04CA  48 8B 4D 88                     mov rcx, qword ptr [rbp - 0x78]
002D04CE  48 8D 0C 91                     lea rcx, [rcx + rdx*4]
002D04D2  EB 0F                           jmp 0x1402d04e3
002D04D4  48 8B 4D 88                     mov rcx, qword ptr [rbp - 0x78]
002D04D8  BB FE FF FF FF                  mov ebx, 0xfffffffe
002D04DD  8B C2                           mov eax, edx
002D04DF  48 8D 0C 81                     lea rcx, [rcx + rax*4]
002D04E3  8B 45 A0                        mov eax, dword ptr [rbp - 0x60]
002D04E6  89 59 08                        mov dword ptr [rcx + 8], ebx
002D04E9  B9 01 00 00 00                  mov ecx, 1
002D04EE  03 C1                           add eax, ecx
002D04F0  48 8D 9F 08 04 00 00            lea rbx, [rdi + 0x408]
002D04F7  03 D1                           add edx, ecx
002D04F9  89 54 24 6C                     mov dword ptr [rsp + 0x6c], edx
002D04FD  E9 4E FD FF FF                  jmp 0x1402d0250
002D0502  4C 8B 54 24 70                  mov r10, qword ptr [rsp + 0x70]
002D0507  48 8B 4D E8                     mov rcx, qword ptr [rbp - 0x18]
002D050B  BA 01 00 00 00                  mov edx, 1
002D0510  48 8B 45 88                     mov rax, qword ptr [rbp - 0x78]
002D0514  41 BF FF FF FF FF               mov r15d, 0xffffffff
002D051A  41 B8 00 01 00 00               mov r8d, 0x100
002D0520  88 11                           mov byte ptr [rcx], dl
002D0522  48 8D 4D 38                     lea rcx, [rbp + 0x38]
002D0526  44 89 30                        mov dword ptr [rax], r14d
002D0529  42 80 7C 16 79 00               cmp byte ptr [rsi + r10 + 0x79], 0
002D052F  C7 45 30 01 00 20 00            mov dword ptr [rbp + 0x30], 0x200001
002D0536  45 0F 45 FE                     cmovne r15d, r14d
002D053A  83 65 34 00                     and dword ptr [rbp + 0x34], 0
002D053E  33 D2                           xor edx, edx
002D0540  E8 FB 66 3F 00                  call 0x1406c6c40
002D0545  48 8B 54 24 70                  mov rdx, qword ptr [rsp + 0x70]
002D054A  48 8D 9F 50 01 00 00            lea rbx, [rdi + 0x150]
002D0551  44 0F B7 4D 32                  movzx r9d, word ptr [rbp + 0x32]
002D0556  4C 8D 45 30                     lea r8, [rbp + 0x30]
002D055A  48 83 EA 80                     sub rdx, -0x80
002D055E  48 8B CB                        mov rcx, rbx
002D0561  48 03 D6                        add rdx, rsi
002D0564  E8 7F 5C 00 00                  call 0x1402d61e8
002D0569  85 C0                           test eax, eax
002D056B  74 0C                           je 0x1402d0579
002D056D  48 8D 55 30                     lea rdx, [rbp + 0x30]
002D0571  48 8B CB                        mov rcx, rbx
002D0574  E8 37 10 00 00                  call 0x1402d15b0
002D0579  48 8B 75 98                     mov rsi, qword ptr [rbp - 0x68]
002D057D  8B 5C 24 54                     mov ebx, dword ptr [rsp + 0x54]
002D0581  44 8B F6                        mov r14d, esi
002D0584  E9 4C 02 00 00                  jmp 0x1402d07d5
002D0589  83 63 04 00                     and dword ptr [rbx + 4], 0
002D058D  48 8D 9F 50 01 00 00            lea rbx, [rdi + 0x150]
002D0594  48 8B 45 88                     mov rax, qword ptr [rbp - 0x78]
002D0598  48 8B D3                        mov rdx, rbx
002D059B  48 8B CB                        mov rcx, rbx
002D059E  89 30                           mov dword ptr [rax], esi
002D05A0  E8 0B 10 00 00                  call 0x1402d15b0
002D05A5  8B 47 28                        mov eax, dword ptr [rdi + 0x28]
002D05A8  33 DB                           xor ebx, ebx
002D05AA  48 8B 8F D8 03 00 00            mov rcx, qword ptr [rdi + 0x3d8]
002D05B1  33 D2                           xor edx, edx
002D05B3  48 89 4D 98                     mov qword ptr [rbp - 0x68], rcx
002D05B7  8D 04 85 08 00 00 00            lea eax, [rax*4 + 8]
002D05BE  4C 63 C0                        movsxd r8, eax
002D05C1  8D 73 01                        lea esi, [rbx + 1]
002D05C4  E8 77 66 3F 00                  call 0x1406c6c40
002D05C9  4C 8B 67 30                     mov r12, qword ptr [rdi + 0x30]
002D05CD  45 33 F6                        xor r14d, r14d
002D05D0  44 3B B7 E8 03 00 00            cmp r14d, dword ptr [rdi + 0x3e8]
002D05D7  0F 83 EA 01 00 00               jae 0x1402d07c7
002D05DD  48 83 7C 24 70 00               cmp qword ptr [rsp + 0x70], 0
002D05E3  4B 8D 0C 76                     lea rcx, [r14 + r14*2]
002D05E7  48 8B 87 F0 03 00 00            mov rax, qword ptr [rdi + 0x3f0]
002D05EE  41 B8 01 00 00 00               mov r8d, 1
002D05F4  8B 4C C8 04                     mov ecx, dword ptr [rax + rcx*8 + 4]
002D05F8  89 4C 24 58                     mov dword ptr [rsp + 0x58], ecx
002D05FC  75 2E                           jne 0x1402d062c
002D05FE  8B 47 28                        mov eax, dword ptr [rdi + 0x28]
002D0601  41 2B C0                        sub eax, r8d
002D0604  3B C8                           cmp ecx, eax
002D0606  75 24                           jne 0x1402d062c
002D0608  80 BF CC 02 00 00 00            cmp byte ptr [rdi + 0x2cc], 0
002D060F  74 1B                           je 0x1402d062c
002D0611  49 8B CD                        mov rcx, r13
002D0614  E8 6F EF 2F 00                  call 0x1405cf588
002D0619  84 C0                           test al, al
002D061B  74 0F                           je 0x1402d062c
002D061D  85 DB                           test ebx, ebx
002D061F  40 0F B6 F6                     movzx esi, sil
002D0623  41 8B C0                        mov eax, r8d
002D0626  41 0F 44 F0                     cmove esi, r8d
002D062A  EB 0C                           jmp 0x1402d0638
002D062C  85 DB                           test ebx, ebx
002D062E  40 0F B6 F6                     movzx esi, sil
002D0632  41 0F 45 F0                     cmovne esi, r8d
002D0636  33 C0                           xor eax, eax
002D0638  89 44 24 54                     mov dword ptr [rsp + 0x54], eax
002D063C  40 84 F6                        test sil, sil
002D063F  74 67                           je 0x1402d06a8
002D0641  8B 4C 24 64                     mov ecx, dword ptr [rsp + 0x64]
002D0645  40 32 F6                        xor sil, sil
002D0648  89 4C 24 48                     mov dword ptr [rsp + 0x48], ecx
002D064C  45 33 C0                        xor r8d, r8d
002D064F  48 8D 4C 24 68                  lea rcx, [rsp + 0x68]
002D0654  8B D0                           mov edx, eax
002D0656  48 89 4C 24 40                  mov qword ptr [rsp + 0x40], rcx
002D065B  48 8D 4D 84                     lea rcx, [rbp - 0x7c]
002D065F  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
002D0664  48 8D 4D C8                     lea rcx, [rbp - 0x38]
002D0668  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
002D066D  48 8D 4D C0                     lea rcx, [rbp - 0x40]
002D0671  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
002D0676  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
002D067A  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
002D067F  48 8B 4D A8                     mov rcx, qword ptr [rbp - 0x58]
002D0683  4C 8B 09                        mov r9, qword ptr [rcx]
002D0686  49 8B CD                        mov rcx, r13
002D0689  E8 4E 73 1F 00                  call 0x1404c79dc
002D068E  8B 44 24 68                     mov eax, dword ptr [rsp + 0x68]
002D0692  48 8B 4D C0                     mov rcx, qword ptr [rbp - 0x40]
002D0696  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
002D069A  48 8B 45 C8                     mov rax, qword ptr [rbp - 0x38]
002D069E  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
002D06A2  48 89 4D B8                     mov qword ptr [rbp - 0x48], rcx
002D06A6  EB 04                           jmp 0x1402d06ac
002D06A8  48 8B 4D B8                     mov rcx, qword ptr [rbp - 0x48]
002D06AC  8B 5C 24 58                     mov ebx, dword ptr [rsp + 0x58]
002D06B0  85 DB                           test ebx, ebx
002D06B2  74 48                           je 0x1402d06fc
002D06B4  8A 44 24 5D                     mov al, byte ptr [rsp + 0x5d]
002D06B8  4C 8B C9                        mov r9, rcx
002D06BB  8B 55 A4                        mov edx, dword ptr [rbp - 0x5c]
002D06BE  45 33 C0                        xor r8d, r8d
002D06C1  88 44 24 28                     mov byte ptr [rsp + 0x28], al
002D06C5  49 8B CD                        mov rcx, r13
002D06C8  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
002D06CC  E8 83 F6 2F 00                  call 0x1405cfd54
002D06D1  48 8B D8                        mov rbx, rax
002D06D4  48 85 C0                        test rax, rax
002D06D7  75 25                           jne 0x1402d06fe
002D06D9  48 8B 87 70 02 00 00            mov rax, qword ptr [rdi + 0x270]
002D06E0  48 85 C0                        test rax, rax
002D06E3  74 19                           je 0x1402d06fe
002D06E5  8B 54 24 58                     mov edx, dword ptr [rsp + 0x58]
002D06E9  41 B8 FF FF FF FF               mov r8d, 0xffffffff
002D06EF  48 8B 4D E0                     mov rcx, qword ptr [rbp - 0x20]
002D06F3  E8 D8 A3 3E 00                  call 0x1406baad0
002D06F8  8B D8                           mov ebx, eax
002D06FA  EB 02                           jmp 0x1402d06fe
002D06FC  33 DB                           xor ebx, ebx
002D06FE  44 8B 54 24 58                  mov r10d, dword ptr [rsp + 0x58]
002D0703  48 8B CB                        mov rcx, rbx
002D0706  48 8B 55 18                     mov rdx, qword ptr [rbp + 0x18]
002D070A  45 8B CA                        mov r9d, r10d
002D070D  49 69 C2 F8 03 00 00            imul rax, r10, 0x3f8
002D0714  48 83 C2 50                     add rdx, 0x50
002D0718  48 03 D0                        add rdx, rax
002D071B  E8 B4 FD 2F 00                  call 0x1405d04d4
002D0720  48 85 DB                        test rbx, rbx
002D0723  74 63                           je 0x1402d0788
002D0725  80 7C 24 5E 00                  cmp byte ptr [rsp + 0x5e], 0
002D072A  74 47                           je 0x1402d0773
002D072C  B8 03 00 00 80                  mov eax, 0x80000003
002D0731  48 3B D8                        cmp rbx, rax
002D0734  74 0A                           je 0x1402d0740
002D0736  B8 08 00 00 80                  mov eax, 0x80000008
002D073B  48 3B D8                        cmp rbx, rax
002D073E  75 33                           jne 0x1402d0773
002D0740  4C 8B 4D B0                     mov r9, qword ptr [rbp - 0x50]
002D0744  48 8D 45 D0                     lea rax, [rbp - 0x30]
002D0748  44 8B 44 24 60                  mov r8d, dword ptr [rsp + 0x60]
002D074D  48 8B D3                        mov rdx, rbx
002D0750  49 8B CD                        mov rcx, r13
002D0753  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
002D0758  E8 D3 FC 2F 00                  call 0x1405d0430
002D075D  84 C0                           test al, al
002D075F  40 0F B6 F6                     movzx esi, sil
002D0763  B8 01 00 00 00                  mov eax, 1
002D0768  0F 45 F0                        cmovne esi, eax
002D076B  48 8B 45 D0                     mov rax, qword ptr [rbp - 0x30]
002D076F  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
002D0773  48 8B 45 98                     mov rax, qword ptr [rbp - 0x68]
002D0777  42 89 5C B0 08                  mov dword ptr [rax + r14*4 + 8], ebx
002D077C  41 FF C6                        inc r14d
002D077F  8B 5C 24 54                     mov ebx, dword ptr [rsp + 0x54]
002D0783  E9 48 FE FF FF                  jmp 0x1402d05d0
002D0788  48 8B 75 98                     mov rsi, qword ptr [rbp - 0x68]
002D078C  49 69 C1 58 01 00 00            imul rax, r9, 0x158
002D0793  44 89 16                        mov dword ptr [rsi], r10d
002D0796  80 BC 38 72 05 00 00 00         cmp byte ptr [rax + rdi + 0x572], 0
002D079E  74 16                           je 0x1402d07b6
002D07A0  48 83 7C 24 70 00               cmp qword ptr [rsp + 0x70], 0
002D07A6  74 0A                           je 0x1402d07b2
002D07A8  80 BC 38 71 05 00 00 00         cmp byte ptr [rax + rdi + 0x571], 0
002D07B0  74 04                           je 0x1402d07b6
002D07B2  32 C0                           xor al, al
002D07B4  EB 05                           jmp 0x1402d07bb
002D07B6  B8 01 00 00 00                  mov eax, 1
002D07BB  48 8B 4D E8                     mov rcx, qword ptr [rbp - 0x18]
002D07BF  8B 5C 24 54                     mov ebx, dword ptr [rsp + 0x54]
002D07C3  88 01                           mov byte ptr [rcx], al
002D07C5  EB 08                           jmp 0x1402d07cf
002D07C7  48 8B 75 98                     mov rsi, qword ptr [rbp - 0x68]
002D07CB  44 8B 75 80                     mov r14d, dword ptr [rbp - 0x80]
002D07CF  41 BF FF FF FF FF               mov r15d, 0xffffffff
002D07D5  48 8B 45 E8                     mov rax, qword ptr [rbp - 0x18]
002D07D9  80 38 00                        cmp byte ptr [rax], 0
002D07DC  74 17                           je 0x1402d07f5
002D07DE  49 8D 8D 8C 88 00 00            lea rcx, [r13 + 0x888c]
002D07E5  41 BD 01 00 00 00               mov r13d, 1
002D07EB  41 8A D5                        mov dl, r13b
002D07EE  E8 65 91 20 00                  call 0x1404d9958
002D07F3  EB 06                           jmp 0x1402d07fb
002D07F5  41 BD 01 00 00 00               mov r13d, 1
002D07FB  48 8B 4D 88                     mov rcx, qword ptr [rbp - 0x78]
002D07FF  48 85 C9                        test rcx, rcx
002D0802  74 45                           je 0x1402d0849
002D0804  8B 54 24 6C                     mov edx, dword ptr [rsp + 0x6c]
002D0808  89 51 04                        mov dword ptr [rcx + 4], edx
002D080B  F7 05 F3 62 CF 00 00 00 20 00   test dword ptr [rip + 0xcf62f3], 0x200000
002D0815  74 32                           je 0x1402d0849
002D0817  83 65 24 00                     and dword ptr [rbp + 0x24], 0
002D081B  8D 04 95 08 00 00 00            lea eax, [rdx*4 + 8]
002D0822  48 89 4D 18                     mov qword ptr [rbp + 0x18], rcx
002D0826  41 8B D5                        mov edx, r13d
002D0829  48 8D 4D 18                     lea rcx, [rbp + 0x18]
002D082D  89 45 20                        mov dword ptr [rbp + 0x20], eax
002D0830  41 B9 3E 12 00 00               mov r9d, 0x123e
002D0836  C7 44 24 20 02 06 00 00         mov dword ptr [rsp + 0x20], 0x602
002D083E  41 B8 00 00 20 40               mov r8d, 0x40200000
002D0844  E8 07 4B F6 FF                  call 0x140235350
002D0849  48 85 F6                        test rsi, rsi
002D084C  74 43                           je 0x1402d0891
002D084E  44 89 76 04                     mov dword ptr [rsi + 4], r14d
002D0852  F7 05 AC 62 CF 00 00 00 20 00   test dword ptr [rip + 0xcf62ac], 0x200000
002D085C  74 33                           je 0x1402d0891
002D085E  83 65 24 00                     and dword ptr [rbp + 0x24], 0
002D0862  42 8D 04 B5 08 00 00 00         lea eax, [r14*4 + 8]
002D086A  41 B9 3D 12 00 00               mov r9d, 0x123d
002D0870  89 45 20                        mov dword ptr [rbp + 0x20], eax
002D0873  41 B8 00 00 20 40               mov r8d, 0x40200000
002D0879  48 89 75 18                     mov qword ptr [rbp + 0x18], rsi
002D087D  41 8B D5                        mov edx, r13d
002D0880  C7 44 24 20 02 06 00 00         mov dword ptr [rsp + 0x20], 0x602
002D0888  48 8D 4D 18                     lea rcx, [rbp + 0x18]
002D088C  E8 BF 4A F6 FF                  call 0x140235350
002D0891  80 7C 24 50 00                  cmp byte ptr [rsp + 0x50], 0
002D0896  8B 44 24 60                     mov eax, dword ptr [rsp + 0x60]
002D089A  74 03                           je 0x1402d089f
002D089C  83 C8 02                        or eax, 2
002D089F  66 09 47 38                     or word ptr [rdi + 0x38], ax
002D08A3  48 8D 8F A0 02 00 00            lea rcx, [rdi + 0x2a0]
002D08AA  8A 45 D8                        mov al, byte ptr [rbp - 0x28]
002D08AD  88 47 07                        mov byte ptr [rdi + 7], al
002D08B0  8A 45 D9                        mov al, byte ptr [rbp - 0x27]
002D08B3  88 47 06                        mov byte ptr [rdi + 6], al
002D08B6  48 8B 45 90                     mov rax, qword ptr [rbp - 0x70]
002D08BA  48 89 47 08                     mov qword ptr [rdi + 8], rax
002D08BE  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
002D08C2  48 89 41 18                     mov qword ptr [rcx + 0x18], rax
002D08C6  48 8B 45 B8                     mov rax, qword ptr [rbp - 0x48]
002D08CA  48 89 41 10                     mov qword ptr [rcx + 0x10], rax
002D08CE  8A 45 84                        mov al, byte ptr [rbp - 0x7c]
002D08D1  88 41 2D                        mov byte ptr [rcx + 0x2d], al
002D08D4  48 8B 45 F8                     mov rax, qword ptr [rbp - 8]
002D08D8  8B 4C 24 58                     mov ecx, dword ptr [rsp + 0x58]
002D08DC  89 08                           mov dword ptr [rax], ecx
002D08DE  48 8B 45 00                     mov rax, qword ptr [rbp]
002D08E2  44 89 38                        mov dword ptr [rax], r15d
002D08E5  48 8B 45 08                     mov rax, qword ptr [rbp + 8]
002D08E9  89 18                           mov dword ptr [rax], ebx
002D08EB  48 8B 45 10                     mov rax, qword ptr [rbp + 0x10]
002D08EF  4C 89 20                        mov qword ptr [rax], r12
002D08F2  48 8B 8D 40 01 00 00            mov rcx, qword ptr [rbp + 0x140]
002D08F9  48 33 CC                        xor rcx, rsp
002D08FC  E8 3F BD 3D 00                  call 0x1406ac640
002D0901  48 8B 9C 24 98 02 00 00         mov rbx, qword ptr [rsp + 0x298]
002D0909  48 81 C4 50 02 00 00            add rsp, 0x250
002D0910  41 5F                           pop r15
002D0912  41 5E                           pop r14
002D0914  41 5D                           pop r13
002D0916  41 5C                           pop r12
002D0918  5F                              pop rdi
002D0919  5E                              pop rsi
002D091A  5D                              pop rbp
002D091B  C3                              ret
002D091C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PpmIdleSelectStates(__int64 a1, int a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m150;
    unsigned int v_stack_m154;
    unsigned __int16 v_stack_m156;
    unsigned __int64 v_stack_m158;
    unsigned int v_stack_m164;
    unsigned int v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m180;
    unsigned __int64 v_stack_m188;
    unsigned __int64 v_stack_m190;
    unsigned __int64 v_stack_m198;
    unsigned __int64 v_stack_m1A0;
    unsigned __int64 v_stack_m1A8;
    unsigned __int8 v_stack_m1AF;
    unsigned __int64 v_stack_m1B0;
    unsigned __int64 v_stack_m1B8;
    unsigned __int64 v_stack_m1C0;
    unsigned __int64 v_stack_m1C8;
    unsigned __int64 v_stack_m1D0;
    unsigned __int64 v_stack_m1D8;
    unsigned __int64 v_stack_m1E0;
    unsigned int v_stack_m1E4;
    unsigned int v_stack_m1E8;
    unsigned __int64 v_stack_m1F0;
    unsigned __int64 v_stack_m1F8;
    unsigned __int64 v_stack_m200;
    unsigned int v_stack_m204;
    unsigned int v_stack_m208;
    unsigned int v_stack_m210;
    unsigned __int64 v_stack_m218;
    unsigned int v_stack_m21C;
    unsigned int v_stack_m220;
    unsigned int v_stack_m224;
    unsigned int v_stack_m228;
    unsigned __int8 v_stack_m22A;
    unsigned __int8 v_stack_m22B;
    unsigned int v_stack_m230;
    unsigned int v_stack_m234;
    unsigned __int8 v_stack_m238;
    unsigned int v_stack_m240;
    unsigned __int64 v_stack_m248;
    unsigned __int64 v_stack_m250;
    unsigned __int64 v_stack_m258;
    unsigned __int64 v_stack_m260;
    unsigned int v_stack_m268;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_p10;

    v_stack_p10 = v_rbx;
    v_rsp = (v_rsp) - (592);
    result = (*(unsigned __int64 *)(v_rip + 11773746)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m180 = a5;
    v_stack_m190 = a6;
    a2 = 0;
    v_stack_m188 = a7;
    v_stack_m178 = a8;
    v_stack_m1A0 = a9;
    v_stack_m1E0 = a4;
    result = memset(v_stack_m158, a2, 264, a4);
    a1 = 0;
    v_stack_m170 = *(unsigned __int64 *)(a1 + 34888);
    v_stack_m234 = 0;
    v_stack_m1A8 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 34880) + 664);
    v_stack_m218 = *(unsigned __int64 *)(v_rip + 13593132);
    v_stack_m1B0 = 0;
    v_stack_m230 = 0;
    v_stack_m200 = 0;
    v_stack_m21C = 0;
    v_stack_m1F0 = 0;
    v_stack_m208 = 0;
    v_stack_m228 = 0;
    v_stack_m220 = 0;
    v_stack_m1D0 = 0;
    v_stack_m1C8 = 0;
    v_stack_m1D8 = 0;
    v_stack_m1C0 = 0;
    v_stack_m204 = 0;
    v_stack_m238 = 0;
    v_stack_m224 = 0;
    v_stack_m22A = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 34880)));
    result = PpmIdleEvaluateConstraints(0, a4, 264, a4);
    *(unsigned __int64 *)(a3) = result;
    a2 = 0;
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 34880) + 336) = 0x200001ULL;
    result = memset(*(unsigned __int64 *)(a1 + 34880) + 336 + 8, a2, 256, a4);
    result = Feature_PpmDynamicHintAdjust__private_IsEnabledNoReportingNoInline(*(unsigned __int64 *)(a1 + 34880) + 336 + 8, a2, 256, a4);
    if ((unsigned int)(result) == 0) goto loc_002D0159;
    a2 = 0;
    if (((unsigned int)(*(unsigned __int64 *)(v_stack_m1E0))) != (*(unsigned int *)(a1 + 14528))) goto loc_002D0155;
    result = (unsigned int)((*(unsigned __int64 *)(v_stack_m1E0)) + 1);
    result = (unsigned int)((result) * ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13592940)))));
    result = (unsigned int)((result) - ((unsigned int)(*(unsigned __int64 *)(v_stack_m1E0))));
loc_002D014F:
    v_stack_m224 = (unsigned int)(result);
    goto loc_002D015C;
loc_002D0155:
    result = 0;
    goto loc_002D014F;
loc_002D0159:
loc_002D015C:
    v_stack_m268 = 0;
    result = PpmComputeIdleDurationHint(0, a2, *(unsigned __int64 *)(v_stack_m1E0), (unsigned __int8)((unsigned __int8)(a2)));
    if ((unsigned __int8)((unsigned __int8)(a2)) == 0) goto loc_002D0197;
    if ((*(unsigned __int8 *)(v_rip + 13592839)) != 0) goto loc_002D0197;
    if ((*(unsigned __int8 *)(a1 + 33)) != 0) goto loc_002D0197;
    v_stack_m1F8 = *(unsigned __int64 *)(v_rip + 13594059);
    v_stack_m1B8 = *(unsigned __int64 *)(v_rip + 13594059);
    goto loc_002D01A3;
loc_002D0197:
    result = (result) | (-1);
    v_stack_m1F8 = result;
    v_stack_m1B8 = result;
loc_002D01A3:
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 34880) + 616);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 34880) + 616) != 0) {
        a1 = v_stack_m1A8;
        a2 = *(unsigned __int64 *)(a1 + 34880) + 672;
        result = guard_dispatch_icall(a1, a2, *(unsigned __int64 *)(v_stack_m1E0), (unsigned __int8)((unsigned __int8)(a2)));
        a1 = (unsigned int)(result);
    }
    result = 0;
    if ((*(unsigned __int8 *)(a1 + 34953)) == 0) { result = (unsigned int)(a1); }
    v_stack_m1E4 = (unsigned int)(result);
    if (v_stack_m218 == 0) goto loc_002D05A5;
    a2 = 0;
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 34880) + 720) = 0x200001ULL;
    result = memset(*(unsigned __int64 *)(a1 + 34880) + 720 + 8, a2, 256, (unsigned __int8)((unsigned __int8)(a2)));
    result = PoCopyDeepIdleMask(*(unsigned __int64 *)(a1 + 34880) + 720, a2, 256, (unsigned __int8)((unsigned __int8)(a2)));
    result = KeAddProcessorAffinityEx(*(unsigned __int64 *)(a1 + 34880) + 720, (unsigned int)(*(unsigned int *)(a1 + 36)), 256, (unsigned __int8)((unsigned __int8)(a2)));
    a2 = 0;
    v_stack_m198 = *(unsigned __int64 *)(v_stack_m218 + 48);
    v_stack_m200 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 34880) + 992);
    result = memset(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 34880) + 992), a2, (int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m218)) * 4 + 8)), (unsigned __int8)((unsigned __int8)(a2)));
    result = 0;
loc_002D0250:
    v_stack_m1E8 = 0;
    if (0 >= (*(unsigned int *)(*(unsigned __int64 *)(a1 + 34880) + 1016))) goto loc_002D0589;
    if ((*(unsigned __int8 *)(v_rip + 11776330)) != 0) goto loc_002D04D4;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 34880) + 1024) + result + result * 2 * 8 + 1)) == 0) goto loc_002D04D4;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11776294)))) == ((unsigned int)((unsigned int)(0xFFFFFFFFULL)))) goto loc_002D02C5;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 34880) + 1024) + result + result * 2 * 8 + 4)))) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11776294))))) goto loc_002D02C5;
    result = PpmCheckPreConditionsForDeepSleep(a1, 0, (int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m218)) * 4 + 8)), (unsigned __int8)((unsigned __int8)(a2)));
    if ((unsigned __int8)(result) == 0) goto loc_002D02C5;
    v_r12 = (unsigned __int8)(a1 + 1);
    if (v_stack_m234 == 0) { v_r12 = 1; }
    result = (unsigned int)(-((unsigned int)(*(unsigned int *)(v_rip + 11893609))));
    result = (unsigned int)(-(result));
    result = (unsigned int)((result) + (1));
    goto loc_002D02D4;
loc_002D02C5:
    v_r12 = (unsigned __int8)(v_r12);
    if (v_stack_m234 != 0) { v_r12 = 1; }
    result = 0;
loc_002D02D4:
    v_stack_m234 = 0;
    v_stack_m210 = (unsigned int)(v_r12);
    if ((unsigned __int8)(v_r12) != 0) {
        a1 = v_stack_m224;
        v_r12 = 0;
        a4 = v_stack_m1E0;
        v_stack_m240 = (unsigned int)(a1);
        a2 = 0;
        a1 = v_stack_m220;
        v_stack_m210 = 0;
        v_stack_m248 = a1;
        a3 = (0 != 0) ? 1 : 0;
        a4 = *(unsigned __int64 *)(a4);
        a1 = v_stack_m204;
        v_stack_m250 = a1;
        a1 = v_stack_m1C0;
        v_stack_m258 = a1;
        a1 = v_stack_m1C8;
        v_stack_m260 = a1;
        a1 = v_stack_m1F8;
        v_stack_m268 = a1;
        a1 = a1;
        result = PpmEstimateIdleDuration(a1, a2, a3, a4);
        result = v_stack_m1C8;
        v_stack_m1D0 = result;
        result = v_stack_m220;
        v_stack_m228 = (unsigned int)(result);
        result = v_stack_m1C0;
        v_stack_m1D8 = result;
    }
    a3 = 0;
    v_stack_m248 = *(unsigned __int64 *)(a1 + 34880) + 1032;
    v_stack_m250 = v_stack_m230;
    v_stack_m258 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 34880) + 1024) + result + result * 2 * 8 + 4)));
    v_stack_m260 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 34880) + 1024) + result + result * 2 * 8 + 4)));
    v_stack_m230 = (unsigned int)((unsigned int)(0xFFFFFFFFULL));
    v_stack_m268 = *(unsigned __int64 *)(v_stack_m1E0);
    result = PpmIdleCheckCoordinatedStateEligibility(a1, (unsigned int)(v_stack_m1E4), a3, v_stack_m1D0);
    v_stack_m230 = (unsigned int)((unsigned int)(v_stack_m230));
    if ((*(unsigned __int8 *)(v_stack_m218 + 8)) != 0) goto loc_002D03CE;
    if (result != 0) goto loc_002D03CE;
    result = *(unsigned __int64 *)(v_stack_m218 + 16);
    v_rbx = result;
    v_r10 = v_stack_m218;
    if (*(unsigned __int64 *)(v_stack_m218 + 16) != 0) {
        a2 = (unsigned int)((unsigned int)(v_stack_m230));
        a3 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 34880) + 1024) + result + result * 2 * 8 + 4)));
        a1 = v_stack_m1A8;
        result = guard_dispatch_icall(a1, a2, a3, v_stack_m1D0);
        v_r10 = v_stack_m218;
        v_rbx = (unsigned int)(result);
    }
    result = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 34880) + 1024) + result + result * 2 * 8 + 4))) << (10);
    a2 = (v_stack_m198) + (88);
    a2 = (a2) + (result);
    result = PpmIdleUpdateSelectionStatistics(v_rbx, a2, a3, v_stack_m1D0);
    v_rsi = ((unsigned int)(0xFFFFFFFFULL)) * ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 34880) + 1024) + result + result * 2 * 8 + 4)));
    if (v_rbx == ((unsigned int)(0xFFFFFFFFULL))) goto loc_002D0452;
    if (v_rbx != 0) goto loc_002D0452;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 34880) + 65)) == 0) goto loc_002D0507;
    if (v_stack_m238 != ((unsigned __int8)(v_rbx))) goto loc_002D0507;
    a1 = (unsigned int)((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 34880) + 65) + *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 34880) + 65) * 4) + ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 34880) + 65) + *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 34880) + 65) * 4)));
    result = KeStallExecutionProcessor(a1, a2, a3, v_stack_m1D0);
    a1 = (v_stack_m218) - (-128);
    v_stack_m238 = 1;
    a1 = (a1) + (v_rsi);
    result = PpmIdleRecheckSecondaryProcessors(a1, a2, a3, v_stack_m1D0);
    if ((unsigned __int8)(result) != 0) goto loc_002D0502;
    goto loc_002D04B8;
loc_002D0452:
    v_stack_m238 = (unsigned __int8)(v_stack_m238);
    v_stack_m210 = (unsigned int)((unsigned int)((unsigned int)(0xFFFFFFFFULL)));
    if (((unsigned int)((unsigned int)((unsigned int)(0xFFFFFFFFULL)))) == ((unsigned int)(0x80000003ULL))) goto loc_002D047F;
    v_stack_m238 = (unsigned __int8)(v_stack_m238);
    v_stack_m210 = (unsigned int)((unsigned int)((unsigned int)(0xFFFFFFFFULL)));
    result = (unsigned int)((unsigned int)((unsigned int)(0xFFFFFFFFULL)));
    v_r12 = (unsigned int)(v_stack_m210);
    if (((unsigned int)((unsigned int)((unsigned int)(0xFFFFFFFFULL)))) == ((unsigned int)(0x80000008ULL))) {
        a4 = v_stack_m1D8;
        result = v_stack_m1B8;
        a3 = v_stack_m228;
        a2 = (unsigned int)((unsigned int)((unsigned int)(0xFFFFFFFFULL)));
        a1 = a1;
        v_stack_m268 = result;
        result = PpmIdleUpdateIdleReevaluationDuration(a1, a2, a3, a4);
        v_r12 = (unsigned __int8)((unsigned int)(v_stack_m210));
        result = 1;
        if ((unsigned __int8)(result) != 0) { v_r12 = (unsigned int)(result); }
        result = v_stack_m1B8;
        v_stack_m1F8 = result;
    }
loc_002D04B8:
    a2 = 0;
    result = PpmIdleRollbackCoordinatedSelection(*(unsigned __int64 *)(a1 + 34880) + 1032, a2, a3, a4);
    goto loc_002D04E3;
loc_002D04D4:
loc_002D04E3:
    *(unsigned int *)(v_stack_m200 + (unsigned int)((unsigned int)((unsigned int)(v_stack_m21C))) * 4 + 8) = (unsigned int)((unsigned int)(0xFFFFFFFEULL));
    result = (unsigned int)(((unsigned int)(v_stack_m1E8)) + (1));
    a2 = (unsigned int)(((unsigned int)(v_stack_m21C)) + (1));
    v_stack_m21C = a2;
    goto loc_002D0250;
loc_002D0502:
loc_002D0507:
    *(unsigned __int8 *)(v_stack_m1A0) = 1;
    *(unsigned int *)(v_stack_m200) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 34880) + 1024) + result + result * 2 * 8 + 4)));
    v_stack_m158 = 0x200001ULL;
    v_r15 = (unsigned int)(0xFFFFFFFFULL);
    if ((*(unsigned __int8 *)((unsigned int)(0xFFFFFFFFULL) + v_stack_m218 * 1 + 121)) != 0) { v_r15 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 34880) + 1024) + result + result * 2 * 8 + 4))); }
    a2 = 0;
    result = memset(v_stack_m150, a2, 256, a4);
    a2 = (v_stack_m218) - (-128);
    a2 = (a2) + ((unsigned int)(0xFFFFFFFFULL));
    result = KiSubtractAffinityEx(*(unsigned __int64 *)(a1 + 34880) + 336, a2, v_stack_m158, v_stack_m156);
    if ((unsigned int)(result) != 0) {
        a2 = v_stack_m158;
        a1 = *(unsigned __int64 *)(a1 + 34880) + 336;
        result = PpmUnlockProcessors(a1, a2, v_stack_m158, v_stack_m156);
    }
    goto loc_002D07D5;
loc_002D0589:
    *(unsigned int *)(v_stack_m200) = (unsigned int)(v_stack_m1F0);
    result = PpmUnlockProcessors(*(unsigned __int64 *)(a1 + 34880) + 336, *(unsigned __int64 *)(a1 + 34880) + 336, v_stack_m158, v_stack_m156);
loc_002D05A5:
    v_rbx = 0;
    a2 = 0;
    v_stack_m1F0 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 34880) + 984);
    result = memset(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 34880) + 984), a2, (int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 34880) + 40)) * 4 + 8)), v_stack_m156);
    v_r14 = 0;
loc_002D05D0:
    if (0 >= (*(unsigned int *)(*(unsigned __int64 *)(a1 + 34880) + 1000))) goto loc_002D07C7;
    v_stack_m230 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 34880) + 1008) + v_r14 + v_r14 * 2 * 8 + 4)));
    if (v_stack_m218 != 0) goto loc_002D062C;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 34880) + 40))) - (1));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 34880) + 1008) + v_r14 + v_r14 * 2 * 8 + 4)))) != ((unsigned int)(result))) goto loc_002D062C;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 34880) + 716)) == 0) goto loc_002D062C;
    result = PpmCheckPreConditionsForDeepSleep(a1, a2, 1, v_stack_m156);
    if ((unsigned __int8)(result) == 0) goto loc_002D062C;
    v_rsi = (unsigned __int8)(v_rbx + 1);
    if (0 == 0) { v_rsi = 1; }
    goto loc_002D0638;
loc_002D062C:
    v_rsi = (unsigned __int8)(v_rsi);
    if (0 != 0) { v_rsi = 1; }
    result = 0;
loc_002D0638:
    v_stack_m234 = 0;
    if ((unsigned __int8)(v_rsi) == 0) goto loc_002D06A8;
    v_rsi = 0;
    v_stack_m240 = (unsigned int)((unsigned int)(v_stack_m224));
    a3 = 0;
    v_stack_m248 = v_stack_m220;
    v_stack_m250 = v_stack_m204;
    v_stack_m258 = v_stack_m1C0;
    v_stack_m260 = v_stack_m1C8;
    v_stack_m268 = v_stack_m1F8;
    result = PpmEstimateIdleDuration(a1, 0, a3, *(unsigned __int64 *)(v_stack_m1E0));
    v_stack_m228 = (unsigned int)((unsigned int)(v_stack_m220));
    v_stack_m1D8 = v_stack_m1C0;
    v_stack_m1D0 = v_stack_m1C8;
    goto loc_002D06AC;
loc_002D06A8:
loc_002D06AC:
    if ((unsigned int)((unsigned int)(v_stack_m230)) == 0) goto loc_002D06FC;
    a3 = 0;
    v_stack_m260 = (unsigned __int8)(v_stack_m22B);
    v_stack_m268 = (unsigned int)((unsigned int)(v_stack_m230));
    result = PpmIdleCheckProcessorStateEligibility(a1, (unsigned int)(v_stack_m1E4), a3, v_stack_m1D0);
    if (result != 0) goto loc_002D06FE;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 34880) + 624) == 0) goto loc_002D06FE;
    result = guard_dispatch_icall(v_stack_m1A8, (unsigned int)(v_stack_m230), (unsigned int)(0xFFFFFFFFULL), v_stack_m1D0);
    goto loc_002D06FE;
loc_002D06FC:
    v_rbx = 0;
loc_002D06FE:
    result = (result) * ((unsigned int)(v_stack_m230));
    a2 = (v_stack_m170) + (80);
    a2 = (a2) + (result);
    result = PpmIdleUpdateSelectionStatistics(0, a2, (unsigned int)(0xFFFFFFFFULL), (unsigned int)((unsigned int)((unsigned int)(v_stack_m230))));
    if (0 == 0) goto loc_002D0788;
    if (v_stack_m22A == 0) goto loc_002D0773;
    if (0 == ((unsigned int)(0x80000003ULL))) goto loc_002D0740;
    result = (unsigned int)(0x80000008ULL);
    if (0 == ((unsigned int)(0x80000008ULL))) {
        a4 = v_stack_m1D8;
        result = v_stack_m1B8;
        a3 = v_stack_m228;
        a2 = 0;
        a1 = a1;
        v_stack_m268 = result;
        result = PpmIdleUpdateIdleReevaluationDuration(a1, a2, a3, a4);
        v_rsi = 0;
        result = 1;
        if ((unsigned __int8)(result) != 0) { v_rsi = (unsigned int)(result); }
        result = v_stack_m1B8;
        v_stack_m1F8 = result;
    }
    *(unsigned int *)(v_stack_m1F0 + v_r14 * 4 + 8) = 0;
    v_r14 = (unsigned int)((v_r14) + 1);
    goto loc_002D05D0;
loc_002D0788:
    result = (v_stack_m1F0) * (a4);
    *(unsigned int *)(v_stack_m1F0) = (unsigned int)((unsigned int)(v_stack_m230));
    if ((*(unsigned __int8 *)(result + *(unsigned __int64 *)(a1 + 34880) * 1 + 1394)) == 0) goto loc_002D07B6;
    if (v_stack_m218 == 0) goto loc_002D07B2;
    if ((*(unsigned __int8 *)(result + *(unsigned __int64 *)(a1 + 34880) * 1 + 1393)) == 0) goto loc_002D07B6;
loc_002D07B2:
    result = 0;
    goto loc_002D07BB;
loc_002D07B6:
loc_002D07BB:
    *(unsigned __int8 *)(v_stack_m1A0) = 1;
    goto loc_002D07CF;
loc_002D07C7:
loc_002D07CF:
loc_002D07D5:
    if ((*(unsigned __int8 *)(v_stack_m1A0)) == 0) goto loc_002D07F5;
    result = PpmIdleSetSynchronizationState(a1 + 34956, 1, a3, a4);
    goto loc_002D07FB;
loc_002D07F5:
loc_002D07FB:
    if (v_stack_m200 == 0) goto loc_002D0849;
    *(unsigned int *)(v_stack_m200 + 4) = (unsigned int)((unsigned int)(v_stack_m21C));
    if (((*(unsigned int *)(v_rip + 13591283)) & (0x200000ULL)) != 0) {
        result = (unsigned int)(v_stack_m21C) * 4 + 8;
        v_stack_m170 = v_stack_m200;
        a2 = 1;
        a1 = v_stack_m170;
        v_stack_m168 = (unsigned int)(result);
        a4 = 0x123EULL;
        v_stack_m268 = 0x602ULL;
        a3 = 0x40200000ULL;
        result = EtwTraceKernelEvent(a1, a2, a3, a4);
    }
    if (v_stack_m1F0 == 0) goto loc_002D0891;
    *(unsigned int *)(v_stack_m1F0 + 4) = (unsigned int)((unsigned int)(v_stack_m208));
    if (((*(unsigned int *)(v_rip + 13591212)) & (0x200000ULL)) != 0) {
        result = (unsigned int)(v_stack_m208) * 4 + 8;
        a4 = 0x123DULL;
        v_stack_m168 = (unsigned int)(result);
        a3 = 0x40200000ULL;
        v_stack_m170 = v_stack_m1F0;
        a2 = 1;
        v_stack_m268 = 0x602ULL;
        a1 = v_stack_m170;
        result = EtwTraceKernelEvent(a1, a2, a3, a4);
    }
    result = (unsigned int)(v_stack_m228);
    if (v_stack_m238 != 0) {
        result = (unsigned int)(((unsigned int)(v_stack_m228)) | (2));
    }
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 34880) + 7) = (unsigned __int8)(v_stack_m1B0);
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 34880) + 6) = (unsigned __int8)(v_stack_m1AF);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 34880) + 8) = v_stack_m1F8;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 34880) + 672 + 24) = v_stack_m1D8;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 34880) + 672 + 16) = v_stack_m1D0;
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 34880) + 672 + 45) = (unsigned __int8)(v_stack_m204);
    *(unsigned int *)(v_stack_m190) = (unsigned int)((unsigned int)(v_stack_m230));
    *(unsigned int *)(v_stack_m188) = (unsigned int)((unsigned int)(0xFFFFFFFFULL));
    *(unsigned int *)(v_stack_m180) = (unsigned int)((unsigned int)(v_stack_m234));
    *(unsigned __int64 *)(v_stack_m178) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 34880) + 48);
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (592);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PpmIdleSelectStates(void *Arg1, int32_t Arg2, void *Arg3, int64_t Arg4, int64_t Arg5, int64_t Arg6, int64_t Arg7, int64_t Arg8, int64_t Arg9)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m150;
    uint32_t v_stack_m154;
    uint16_t v_stack_m156;
    uint64_t v_stack_m158;
    uint32_t v_stack_m164;
    uint32_t v_stack_m168;
    uint64_t v_stack_m170;
    uint64_t v_stack_m178;
    uint64_t v_stack_m180;
    uint64_t v_stack_m188;
    uint64_t v_stack_m190;
    uint64_t v_stack_m198;
    uint64_t v_stack_m1A0;
    uint64_t v_stack_m1A8;
    uint8_t v_stack_m1AF;
    uint64_t v_stack_m1B0;
    uint64_t v_stack_m1B8;
    uint64_t v_stack_m1C0;
    uint64_t v_stack_m1C8;
    uint64_t v_stack_m1D0;
    uint64_t v_stack_m1D8;
    uint64_t v_stack_m1E0;
    uint32_t v_stack_m1E4;
    uint32_t v_stack_m1E8;
    uint64_t v_stack_m1F0;
    uint64_t v_stack_m1F8;
    uint64_t v_stack_m200;
    uint32_t v_stack_m204;
    uint32_t v_stack_m208;
    uint32_t v_stack_m210;
    uint64_t v_stack_m218;
    uint32_t v_stack_m21C;
    uint32_t v_stack_m220;
    uint32_t v_stack_m224;
    uint32_t v_stack_m228;
    uint8_t v_stack_m22A;
    uint8_t v_stack_m22B;
    uint32_t v_stack_m230;
    uint32_t v_stack_m234;
    uint8_t v_stack_m238;
    uint32_t v_stack_m240;
    uint64_t v_stack_m248;
    uint64_t v_stack_m250;
    uint64_t v_stack_m258;
    uint64_t v_stack_m260;
    uint32_t v_stack_m268;
    uint64_t v_stack_m48;
    uint64_t v_stack_p10;

    v_stack_p10 = local_rbx;
    local_rsp = (local_rsp) - (592);
    result = (*(uint64_t *)(v_rip + 0xB3A732)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m180 = Arg5;
    v_stack_m190 = Arg6;
    Arg2 = 0;
    v_stack_m188 = Arg7;
    v_stack_m178 = Arg8;
    v_stack_m1A0 = Arg9;
    v_stack_m1E0 = Arg4;
    result = memset(v_stack_m158, Arg2, 264, Arg4);
    Arg1 = 0;
    v_stack_m170 = *(uint64_t *)(arg1 + 0x8848);
    v_stack_m234 = 0;
    v_stack_m1A8 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x8840) + 0x298);
    v_stack_m218 = *(uint64_t *)(v_rip + 0xCF6A2C);
    v_stack_m1B0 = 0;
    v_stack_m230 = 0;
    v_stack_m200 = 0;
    v_stack_m21C = 0;
    v_stack_m1F0 = 0;
    v_stack_m208 = 0;
    v_stack_m228 = 0;
    v_stack_m220 = 0;
    v_stack_m1D0 = 0;
    v_stack_m1C8 = 0;
    v_stack_m1D8 = 0;
    v_stack_m1C0 = 0;
    v_stack_m204 = 0;
    v_stack_m238 = 0;
    v_stack_m224 = 0;
    v_stack_m22A = (uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x8840)));
    result = PpmIdleEvaluateConstraints(0, Arg4, 264, Arg4);
    *(uint64_t *)(arg3) = result;
    Arg2 = 0;
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x8840) + 0x150) = 0x200001ULL;
    result = memset(*(uint64_t *)(arg1 + 0x8840) + 336 + 8, Arg2, 256, Arg4);
    result = Feature_PpmDynamicHintAdjust__private_IsEnabledNoReportingNoInline(*(uint64_t *)(arg1 + 0x8840) + 336 + 8, Arg2, 256, Arg4);
    if ((uint32_t)(result) == 0) goto loc_002D0159;
    Arg2 = 0;
    if (((uint32_t)(*(uint64_t *)(v_stack_m1E0))) != (*(uint32_t *)(arg1 + 0x38C0))) goto loc_002D0155;
    result = (uint32_t)((*(uint64_t *)(v_stack_m1E0)) + 1);
    result = (uint32_t)((result) * ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCF696C)))));
    result = (uint32_t)((result) - ((uint32_t)(*(uint64_t *)(v_stack_m1E0))));
loc_002D014F:
    v_stack_m224 = (uint32_t)(result);
    goto loc_002D015C;
loc_002D0155:
    result = 0;
    goto loc_002D014F;
loc_002D0159:
loc_002D015C:
    v_stack_m268 = 0;
    result = PpmComputeIdleDurationHint(0, Arg2, *(uint64_t *)(v_stack_m1E0), (uint8_t)((uint8_t)(Arg2)));
    if ((uint8_t)((uint8_t)(Arg2)) == 0) goto loc_002D0197;
    if ((*(uint8_t *)(v_rip + 0xCF6907)) != 0) goto loc_002D0197;
    if ((*(uint8_t *)(arg1 + 0x21)) != 0) goto loc_002D0197;
    v_stack_m1F8 = *(uint64_t *)(v_rip + 0xCF6DCB);
    v_stack_m1B8 = *(uint64_t *)(v_rip + 0xCF6DCB);
    goto loc_002D01A3;
loc_002D0197:
    result = (result) | (-1);
    v_stack_m1F8 = result;
    v_stack_m1B8 = result;
loc_002D01A3:
    result = *(uint64_t *)(*(uint64_t *)(arg1 + 0x8840) + 0x268);
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x8840) + 0x268) != 0) {
        Arg1 = v_stack_m1A8;
        Arg2 = *(uint64_t *)(arg1 + 0x8840) + 672;
        result = guard_dispatch_icall(Arg1, Arg2, *(uint64_t *)(v_stack_m1E0), (uint8_t)((uint8_t)(Arg2)));
        Arg1 = (uint32_t)(result);
    }
    result = 0;
    if ((*(uint8_t *)(arg1 + 0x8889)) == 0) { result = (uint32_t)(Arg1); }
    v_stack_m1E4 = (uint32_t)(result);
    if (v_stack_m218 == 0) goto loc_002D05A5;
    Arg2 = 0;
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x8840) + 0x2D0) = 0x200001ULL;
    result = memset(*(uint64_t *)(arg1 + 0x8840) + 720 + 8, Arg2, 256, (uint8_t)((uint8_t)(Arg2)));
    result = PoCopyDeepIdleMask(*(uint64_t *)(arg1 + 0x8840) + 720, Arg2, 256, (uint8_t)((uint8_t)(Arg2)));
    result = KeAddProcessorAffinityEx(*(uint64_t *)(arg1 + 0x8840) + 720, (uint32_t)(*(uint32_t *)(arg1 + 0x24)), 256, (uint8_t)((uint8_t)(Arg2)));
    Arg2 = 0;
    v_stack_m198 = *(uint64_t *)(v_stack_m218 + 0x30);
    v_stack_m200 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x8840) + 0x3E0);
    result = memset(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8840) + 0x3E0), Arg2, (int32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m218)) * 4 + 8)), (uint8_t)((uint8_t)(Arg2)));
    result = 0;
loc_002D0250:
    v_stack_m1E8 = 0;
    if (0 >= (*(uint32_t *)(*(uint64_t *)(arg1 + 0x8840) + 0x3F8))) goto loc_002D0589;
    if ((*(uint8_t *)(v_rip + 0xB3B14A)) != 0) goto loc_002D04D4;
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8840) + 0x400) + result + result * 2 * 8 + 0x1)) == 0) goto loc_002D04D4;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB3B126)))) == ((uint32_t)((uint32_t)(0xFFFFFFFFULL)))) goto loc_002D02C5;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8840) + 0x400) + result + result * 2 * 8 + 0x4)))) < ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB3B126))))) goto loc_002D02C5;
    result = PpmCheckPreConditionsForDeepSleep(Arg1, 0, (int32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m218)) * 4 + 8)), (uint8_t)((uint8_t)(Arg2)));
    if ((uint8_t)(result) == 0) goto loc_002D02C5;
    local_r12 = (uint8_t)(Arg1 + 1);
    if (v_stack_m234 == 0) { local_r12 = 1; }
    result = (uint32_t)(-((uint32_t)(*(uint32_t *)(v_rip + 0xB57B69))));
    result = (uint32_t)(-(result));
    result = (uint32_t)((result) + (1));
    goto loc_002D02D4;
loc_002D02C5:
    local_r12 = (uint8_t)(local_r12);
    if (v_stack_m234 != 0) { local_r12 = 1; }
    result = 0;
loc_002D02D4:
    v_stack_m234 = 0;
    v_stack_m210 = (uint32_t)(local_r12);
    if ((uint8_t)(local_r12) != 0) {
        Arg1 = v_stack_m224;
        local_r12 = 0;
        Arg4 = v_stack_m1E0;
        v_stack_m240 = (uint32_t)(Arg1);
        Arg2 = 0;
        Arg1 = v_stack_m220;
        v_stack_m210 = 0;
        v_stack_m248 = Arg1;
        Arg3 = (0 != 0) ? 1 : 0;
        Arg4 = *(uint64_t *)(Arg4);
        Arg1 = v_stack_m204;
        v_stack_m250 = Arg1;
        Arg1 = v_stack_m1C0;
        v_stack_m258 = Arg1;
        Arg1 = v_stack_m1C8;
        v_stack_m260 = Arg1;
        Arg1 = v_stack_m1F8;
        v_stack_m268 = Arg1;
        Arg1 = Arg1;
        result = PpmEstimateIdleDuration(Arg1, Arg2, Arg3, Arg4);
        result = v_stack_m1C8;
        v_stack_m1D0 = result;
        result = v_stack_m220;
        v_stack_m228 = (uint32_t)(result);
        result = v_stack_m1C0;
        v_stack_m1D8 = result;
    }
    Arg3 = 0;
    v_stack_m248 = *(uint64_t *)(arg1 + 0x8840) + 1032;
    v_stack_m250 = v_stack_m230;
    v_stack_m258 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8840) + 0x400) + result + result * 2 * 8 + 0x4)));
    v_stack_m260 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8840) + 0x400) + result + result * 2 * 8 + 0x4)));
    v_stack_m230 = (uint32_t)((uint32_t)(0xFFFFFFFFULL));
    v_stack_m268 = *(uint64_t *)(v_stack_m1E0);
    result = PpmIdleCheckCoordinatedStateEligibility(Arg1, (uint32_t)(v_stack_m1E4), Arg3, v_stack_m1D0);
    v_stack_m230 = (uint32_t)((uint32_t)(v_stack_m230));
    if ((*(uint8_t *)(v_stack_m218 + 0x8)) != 0) goto loc_002D03CE;
    if (result != 0) goto loc_002D03CE;
    result = *(uint64_t *)(v_stack_m218 + 0x10);
    local_rbx = result;
    local_r10 = v_stack_m218;
    if (*(uint64_t *)(v_stack_m218 + 0x10) != 0) {
        Arg2 = (uint32_t)((uint32_t)(v_stack_m230));
        Arg3 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8840) + 0x400) + result + result * 2 * 8 + 0x4)));
        Arg1 = v_stack_m1A8;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, v_stack_m1D0);
        local_r10 = v_stack_m218;
        local_rbx = (uint32_t)(result);
    }
    result = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8840) + 0x400) + result + result * 2 * 8 + 0x4))) << (10);
    Arg2 = (v_stack_m198) + (88);
    Arg2 = (Arg2) + (result);
    result = PpmIdleUpdateSelectionStatistics(local_rbx, Arg2, Arg3, v_stack_m1D0);
    local_rsi = ((uint32_t)(0xFFFFFFFFULL)) * ((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8840) + 0x400) + result + result * 2 * 8 + 0x4)));
    if (local_rbx == ((uint32_t)(0xFFFFFFFFULL))) goto loc_002D0452;
    if (local_rbx != 0) goto loc_002D0452;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x8840) + 0x41)) == 0) goto loc_002D0507;
    if (v_stack_m238 != ((uint8_t)(local_rbx))) goto loc_002D0507;
    Arg1 = (uint32_t)((*(uint8_t *)(*(uint64_t *)(arg1 + 0x8840) + 0x41) + *(uint8_t *)(*(uint64_t *)(arg1 + 0x8840) + 0x41) * 4) + ((uint32_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x8840) + 0x41) + *(uint8_t *)(*(uint64_t *)(arg1 + 0x8840) + 0x41) * 4)));
    result = KeStallExecutionProcessor(Arg1, Arg2, Arg3, v_stack_m1D0);
    Arg1 = (v_stack_m218) - (-128);
    v_stack_m238 = 1;
    Arg1 = (Arg1) + (local_rsi);
    result = PpmIdleRecheckSecondaryProcessors(Arg1, Arg2, Arg3, v_stack_m1D0);
    if ((uint8_t)(result) != 0) goto loc_002D0502;
    goto loc_002D04B8;
loc_002D0452:
    v_stack_m238 = (uint8_t)(v_stack_m238);
    v_stack_m210 = (uint32_t)((uint32_t)((uint32_t)(0xFFFFFFFFULL)));
    if (((uint32_t)((uint32_t)((uint32_t)(0xFFFFFFFFULL)))) == ((uint32_t)(0x80000003ULL))) goto loc_002D047F;
    v_stack_m238 = (uint8_t)(v_stack_m238);
    v_stack_m210 = (uint32_t)((uint32_t)((uint32_t)(0xFFFFFFFFULL)));
    result = (uint32_t)((uint32_t)((uint32_t)(0xFFFFFFFFULL)));
    local_r12 = (uint32_t)(v_stack_m210);
    if (((uint32_t)((uint32_t)((uint32_t)(0xFFFFFFFFULL)))) == ((uint32_t)(0x80000008ULL))) {
        Arg4 = v_stack_m1D8;
        result = v_stack_m1B8;
        Arg3 = v_stack_m228;
        Arg2 = (uint32_t)((uint32_t)((uint32_t)(0xFFFFFFFFULL)));
        Arg1 = Arg1;
        v_stack_m268 = result;
        result = PpmIdleUpdateIdleReevaluationDuration(Arg1, Arg2, Arg3, Arg4);
        local_r12 = (uint8_t)((uint32_t)(v_stack_m210));
        result = 1;
        if ((uint8_t)(result) != 0) { local_r12 = (uint32_t)(result); }
        result = v_stack_m1B8;
        v_stack_m1F8 = result;
    }
loc_002D04B8:
    Arg2 = 0;
    result = PpmIdleRollbackCoordinatedSelection(*(uint64_t *)(arg1 + 0x8840) + 1032, Arg2, Arg3, Arg4);
    goto loc_002D04E3;
loc_002D04D4:
loc_002D04E3:
    *(uint32_t *)(v_stack_m200 + (uint32_t)((uint32_t)((uint32_t)(v_stack_m21C))) * 4 + 0x8) = (uint32_t)((uint32_t)(0xFFFFFFFEULL));
    result = (uint32_t)(((uint32_t)(v_stack_m1E8)) + (1));
    Arg2 = (uint32_t)(((uint32_t)(v_stack_m21C)) + (1));
    v_stack_m21C = Arg2;
    goto loc_002D0250;
loc_002D0502:
loc_002D0507:
    *(uint8_t *)(v_stack_m1A0) = 1;
    *(uint32_t *)(v_stack_m200) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8840) + 0x400) + result + result * 2 * 8 + 0x4)));
    v_stack_m158 = 0x200001ULL;
    local_r15 = (uint32_t)(0xFFFFFFFFULL);
    if ((*(uint8_t *)((uint32_t)(0xFFFFFFFFULL) + v_stack_m218 * 1 + 0x79)) != 0) { local_r15 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8840) + 0x400) + result + result * 2 * 8 + 0x4))); }
    Arg2 = 0;
    result = memset(v_stack_m150, Arg2, 256, Arg4);
    Arg2 = (v_stack_m218) - (-128);
    Arg2 = (Arg2) + ((uint32_t)(0xFFFFFFFFULL));
    result = KiSubtractAffinityEx(*(uint64_t *)(arg1 + 0x8840) + 336, Arg2, v_stack_m158, v_stack_m156);
    if ((uint32_t)(result) != 0) {
        Arg2 = v_stack_m158;
        Arg1 = *(uint64_t *)(arg1 + 0x8840) + 336;
        result = PpmUnlockProcessors(Arg1, Arg2, v_stack_m158, v_stack_m156);
    }
    goto loc_002D07D5;
loc_002D0589:
    *(uint32_t *)(v_stack_m200) = (uint32_t)(v_stack_m1F0);
    result = PpmUnlockProcessors(*(uint64_t *)(arg1 + 0x8840) + 336, *(uint64_t *)(arg1 + 0x8840) + 336, v_stack_m158, v_stack_m156);
loc_002D05A5:
    local_rbx = 0;
    Arg2 = 0;
    v_stack_m1F0 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x8840) + 0x3D8);
    result = memset(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8840) + 0x3D8), Arg2, (int32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8840) + 0x28)) * 4 + 8)), v_stack_m156);
    local_r14 = 0;
loc_002D05D0:
    if (0 >= (*(uint32_t *)(*(uint64_t *)(arg1 + 0x8840) + 0x3E8))) goto loc_002D07C7;
    v_stack_m230 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8840) + 0x3F0) + local_r14 + local_r14 * 2 * 8 + 0x4)));
    if (v_stack_m218 != 0) goto loc_002D062C;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8840) + 0x28))) - (1));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8840) + 0x3F0) + local_r14 + local_r14 * 2 * 8 + 0x4)))) != ((uint32_t)(result))) goto loc_002D062C;
    if ((*(uint8_t *)(*(uint64_t *)(arg1 + 0x8840) + 0x2CC)) == 0) goto loc_002D062C;
    result = PpmCheckPreConditionsForDeepSleep(Arg1, Arg2, 1, v_stack_m156);
    if ((uint8_t)(result) == 0) goto loc_002D062C;
    local_rsi = (uint8_t)(local_rbx + 1);
    if (0 == 0) { local_rsi = 1; }
    goto loc_002D0638;
loc_002D062C:
    local_rsi = (uint8_t)(local_rsi);
    if (0 != 0) { local_rsi = 1; }
    result = 0;
loc_002D0638:
    v_stack_m234 = 0;
    if ((uint8_t)(local_rsi) == 0) goto loc_002D06A8;
    local_rsi = 0;
    v_stack_m240 = (uint32_t)((uint32_t)(v_stack_m224));
    Arg3 = 0;
    v_stack_m248 = v_stack_m220;
    v_stack_m250 = v_stack_m204;
    v_stack_m258 = v_stack_m1C0;
    v_stack_m260 = v_stack_m1C8;
    v_stack_m268 = v_stack_m1F8;
    result = PpmEstimateIdleDuration(Arg1, 0, Arg3, *(uint64_t *)(v_stack_m1E0));
    v_stack_m228 = (uint32_t)((uint32_t)(v_stack_m220));
    v_stack_m1D8 = v_stack_m1C0;
    v_stack_m1D0 = v_stack_m1C8;
    goto loc_002D06AC;
loc_002D06A8:
loc_002D06AC:
    if ((uint32_t)((uint32_t)(v_stack_m230)) == 0) goto loc_002D06FC;
    Arg3 = 0;
    v_stack_m260 = (uint8_t)(v_stack_m22B);
    v_stack_m268 = (uint32_t)((uint32_t)(v_stack_m230));
    result = PpmIdleCheckProcessorStateEligibility(Arg1, (uint32_t)(v_stack_m1E4), Arg3, v_stack_m1D0);
    if (result != 0) goto loc_002D06FE;
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x8840) + 0x270) == 0) goto loc_002D06FE;
    result = guard_dispatch_icall(v_stack_m1A8, (uint32_t)(v_stack_m230), (uint32_t)(0xFFFFFFFFULL), v_stack_m1D0);
    goto loc_002D06FE;
loc_002D06FC:
    local_rbx = 0;
loc_002D06FE:
    result = (result) * ((uint32_t)(v_stack_m230));
    Arg2 = (v_stack_m170) + (80);
    Arg2 = (Arg2) + (result);
    result = PpmIdleUpdateSelectionStatistics(0, Arg2, (uint32_t)(0xFFFFFFFFULL), (uint32_t)((uint32_t)((uint32_t)(v_stack_m230))));
    if (0 == 0) goto loc_002D0788;
    if (v_stack_m22A == 0) goto loc_002D0773;
    if (0 == ((uint32_t)(0x80000003ULL))) goto loc_002D0740;
    result = (uint32_t)(0x80000008ULL);
    if (0 == ((uint32_t)(0x80000008ULL))) {
        Arg4 = v_stack_m1D8;
        result = v_stack_m1B8;
        Arg3 = v_stack_m228;
        Arg2 = 0;
        Arg1 = Arg1;
        v_stack_m268 = result;
        result = PpmIdleUpdateIdleReevaluationDuration(Arg1, Arg2, Arg3, Arg4);
        local_rsi = 0;
        result = 1;
        if ((uint8_t)(result) != 0) { local_rsi = (uint32_t)(result); }
        result = v_stack_m1B8;
        v_stack_m1F8 = result;
    }
    *(uint32_t *)(v_stack_m1F0 + local_r14 * 4 + 0x8) = 0;
    local_r14 = (uint32_t)((local_r14) + 1);
    goto loc_002D05D0;
loc_002D0788:
    result = (v_stack_m1F0) * (Arg4);
    *(uint32_t *)(v_stack_m1F0) = (uint32_t)((uint32_t)(v_stack_m230));
    if ((*(uint8_t *)(result + *(uint64_t *)(arg1 + 0x8840) * 1 + 0x572)) == 0) goto loc_002D07B6;
    if (v_stack_m218 == 0) goto loc_002D07B2;
    if ((*(uint8_t *)(result + *(uint64_t *)(arg1 + 0x8840) * 1 + 0x571)) == 0) goto loc_002D07B6;
loc_002D07B2:
    result = 0;
    goto loc_002D07BB;
loc_002D07B6:
loc_002D07BB:
    *(uint8_t *)(v_stack_m1A0) = 1;
    goto loc_002D07CF;
loc_002D07C7:
loc_002D07CF:
loc_002D07D5:
    if ((*(uint8_t *)(v_stack_m1A0)) == 0) goto loc_002D07F5;
    result = PpmIdleSetSynchronizationState(Arg1 + 34956, 1, Arg3, Arg4);
    goto loc_002D07FB;
loc_002D07F5:
loc_002D07FB:
    if (v_stack_m200 == 0) goto loc_002D0849;
    *(uint32_t *)(v_stack_m200 + 0x4) = (uint32_t)((uint32_t)(v_stack_m21C));
    if (((*(uint32_t *)(v_rip + 0xCF62F3)) & (0x200000ULL)) != 0) {
        result = (uint32_t)(v_stack_m21C) * 4 + 8;
        v_stack_m170 = v_stack_m200;
        Arg2 = 1;
        Arg1 = v_stack_m170;
        v_stack_m168 = (uint32_t)(result);
        Arg4 = 0x123EULL;
        v_stack_m268 = 0x602ULL;
        Arg3 = 0x40200000ULL;
        result = EtwTraceKernelEvent(Arg1, Arg2, Arg3, Arg4);
    }
    if (v_stack_m1F0 == 0) goto loc_002D0891;
    *(uint32_t *)(v_stack_m1F0 + 0x4) = (uint32_t)((uint32_t)(v_stack_m208));
    if (((*(uint32_t *)(v_rip + 0xCF62AC)) & (0x200000ULL)) != 0) {
        result = (uint32_t)(v_stack_m208) * 4 + 8;
        Arg4 = 0x123DULL;
        v_stack_m168 = (uint32_t)(result);
        Arg3 = 0x40200000ULL;
        v_stack_m170 = v_stack_m1F0;
        Arg2 = 1;
        v_stack_m268 = 0x602ULL;
        Arg1 = v_stack_m170;
        result = EtwTraceKernelEvent(Arg1, Arg2, Arg3, Arg4);
    }
    result = (uint32_t)(v_stack_m228);
    if (v_stack_m238 != 0) {
        result = (uint32_t)(((uint32_t)(v_stack_m228)) | (2));
    }
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x8840) + 0x7) = (uint8_t)(v_stack_m1B0);
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x8840) + 0x6) = (uint8_t)(v_stack_m1AF);
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x8840) + 0x8) = v_stack_m1F8;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x8840) + 0x2A0 + 0x18) = v_stack_m1D8;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x8840) + 0x2A0 + 0x10) = v_stack_m1D0;
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x8840) + 0x2A0 + 0x2D) = (uint8_t)(v_stack_m204);
    *(uint32_t *)(v_stack_m190) = (uint32_t)((uint32_t)(v_stack_m230));
    *(uint32_t *)(v_stack_m188) = (uint32_t)((uint32_t)(0xFFFFFFFFULL));
    *(uint32_t *)(v_stack_m180) = (uint32_t)((uint32_t)(v_stack_m234));
    *(uint64_t *)(v_stack_m178) = *(uint64_t *)(*(uint64_t *)(arg1 + 0x8840) + 0x30);
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (592);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x21` | `8` | `R` |
| `Arg1` | `+ 0x24` | `32` | `R` |
| `Arg1` | `+ 0x38C0` | `32` | `R` |
| `Arg1` | `+ 0x8840` | `64` | `R` |
| `Arg1` | `+ 0x8848` | `64` | `R` |
| `Arg1` | `+ 0x8889` | `8` | `R` |
| `Arg1` | `+ 0x888C` | `64` | `R` |
| `Arg3` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002CFFE8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
