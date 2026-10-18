# PopExecutePowerAction

- RVA: `0x0075E6B4`–`0x0075EBF4` (길이 `1,344` bytes)
- VA: `0x000000014075E6B4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C9340`
- 디코드: `357`개 명령, `1,344/1,344` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **32**; 고유 호출 대상: **18**
- 직접 호출자로 확인된 함수: **10**
- RIP 상대 이미지 참조: **25**

### Outgoing calls
- `0x0075E750` → [EtwTraceKernelEvent](../../text/23/EtwTraceKernelEvent_function_00235350.md) (function, `0x00235350`)
- `0x0075E761` → [PopCompleteAction](../A9/PopCompleteAction_function_00A9D338.md) (function, `0x00A9D338`)
- `0x0075E772` → [PopVerifySystemPowerState](../A9/PopVerifySystemPowerState_function_00A9537C.md) (function, `0x00A9537C`)
- `0x0075E77B` → [PopVerifyPowerActionPolicy](../91/PopVerifyPowerActionPolicy_function_0091114C.md) (function, `0x0091114C`)
- `0x0075E791` → [PopCompleteAction](../A9/PopCompleteAction_function_00A9D338.md) (function, `0x00A9D338`)
- `0x0075E80E` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x0075E846` → [PopDiagTraceShutdownAction](../../text/5D/PopDiagTraceShutdownAction_function_005D6F08.md) (function, `0x005D6F08`)
- `0x0075E854` → [PopResetActionDefaults](../70/PopResetActionDefaults_function_007058E0.md) (function, `0x007058E0`)
- `0x0075E89A` → [PopCompareActions](../AA/PopCompareActions_function_00AA0CA4.md) (function, `0x00AA0CA4`)
- `0x0075E8B8` → [PopPromoteActionFlag](../AC/PopPromoteActionFlag_function_00AC19C8.md) (function, `0x00AC19C8`)
- `0x0075E8D0` → [PopPromoteActionFlag](../AC/PopPromoteActionFlag_function_00AC19C8.md) (function, `0x00AC19C8`)
- `0x0075E8E8` → [PopPromoteActionFlag](../AC/PopPromoteActionFlag_function_00AC19C8.md) (function, `0x00AC19C8`)
- `0x0075E92D` → [PopPromoteActionFlag](../AC/PopPromoteActionFlag_function_00AC19C8.md) (function, `0x00AC19C8`)
- `0x0075E946` → [PopPromoteActionFlag](../AC/PopPromoteActionFlag_function_00AC19C8.md) (function, `0x00AC19C8`)
- `0x0075E95C` → [PopPromoteActionFlag](../AC/PopPromoteActionFlag_function_00AC19C8.md) (function, `0x00AC19C8`)
- `0x0075E972` → [PopPromoteActionFlag](../AC/PopPromoteActionFlag_function_00AC19C8.md) (function, `0x00AC19C8`)
- `0x0075E988` → [PopPromoteActionFlag](../AC/PopPromoteActionFlag_function_00AC19C8.md) (function, `0x00AC19C8`)
- `0x0075E999` → [PopCompareActions](../AA/PopCompareActions_function_00AA0CA4.md) (function, `0x00AA0CA4`)
- `0x0075E9AD` → [PopCompareActions](../AA/PopCompareActions_function_00AA0CA4.md) (function, `0x00AA0CA4`)
- `0x0075E9C6` → [PopCompareActions](../AA/PopCompareActions_function_00AA0CA4.md) (function, `0x00AA0CA4`)
- `0x0075EA1C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0075EA38` → [PoStoreDiagnosticContext](../../text/23/PoStoreDiagnosticContext_function_0023009C.md) (function, `0x0023009C`)
- `0x0075EA4C` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0075EA68` → [PoStoreDiagnosticContext](../../text/23/PoStoreDiagnosticContext_function_0023009C.md) (function, `0x0023009C`)
- `0x0075EA7D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0075EAA8` → [TtmIsEnabled](../91/TtmIsEnabled_function_009143D8.md) (function, `0x009143D8`)
- `0x0075EAD1` → [PopGetPolicyWorker](../../text/48/PopGetPolicyWorker_function_00482D24.md) (function, `0x00482D24`)
- `0x0075EB02` → [PopSetPowerActionState](../../text/4B/PopSetPowerActionState_function_004BC8A8.md) (function, `0x004BC8A8`)
- `0x0075EB3C` → [PopSetNotificationWork](../../text/48/PopSetNotificationWork_function_00482C78.md) (function, `0x00482C78`)
- `0x0075EB87` → [PopCompleteAction](../A9/PopCompleteAction_function_00A9D338.md) (function, `0x00A9D338`)
- `0x0075EBCE` → [PopDiagTraceExecutePowerAction](../AB/PopDiagTraceExecutePowerAction_function_00AB173C.md) (function, `0x00AB173C`)
- `0x0075EBDA` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PopThermalStateTransitionWorker](PopThermalStateTransitionWorker_function_0075F820.md) at `0x0075F941`
- [NtInitiatePowerAction](NtInitiatePowerAction_function_0075FCB0.md) at `0x0075FE9F`
- [PopPowerAggregatorNotifyPdcPhaseState](../76/PopPowerAggregatorNotifyPdcPhaseState_function_00764C54.md) at `0x00764D58`
- [PopPowerAggregatorScreenOffEnterStateHandler](../76/PopPowerAggregatorScreenOffEnterStateHandler_function_00764E90.md) at `0x00764F81`
- [PopPowerAggregatorTriggerAdaptiveAction](../76/PopPowerAggregatorTriggerAdaptiveAction_function_00765240.md) at `0x0076531C`
- [PopIdleAoAcDozeToS4](../76/PopIdleAoAcDozeToS4_function_00768790.md) at `0x00768843`
- [PdcPoSetPowerAction](../76/PdcPoSetPowerAction_function_00769520.md) at `0x00769557`
- [PoTtmInitiatePowerStateTransition](../76/PoTtmInitiatePowerStateTransition_function_007695E8.md) at `0x007696A3`
- [PopBatteryApplyCompositeState](../AE/PopBatteryApplyCompositeState_function_00AE0CD0.md) at `0x00AE1229`
- [NtSetSystemPowerState](../../pagelk/B7/NtSetSystemPowerState_function_00B70890.md) at `0x00B70A0A`

### Static image references
- `0x0075E6CD` → RVA `0x00E0A740` (`.data`; read)
- `0x0075E6E3` → RVA `0x00FC6B10` (`ALMOSTRO`; read)
- `0x0075E7D2` → RVA `0x00F06628` (`.data`; read)
- `0x0075E7F4` → RVA `0x00F0CE44` (`.data`; read)
- `0x0075E813` → RVA `0x00F0E790` (`.data`; write)
- `0x0075E84B` → RVA `0x00F0BD41` (`.data`; read)
- `0x0075E86A` → RVA `0x00F0BD44` (`.data`; read)
- `0x0075E8F2` → RVA `0x00F0CE68` (`.data`; read)
- `0x0075E904` → RVA `0x00F0BD48` (`.data`; read)
- `0x0075E910` → RVA `0x00F0BD48` (`.data`; write)
- `0x0075E9D3` → RVA `0x00F0BD44` (`.data`; write)
- `0x0075E9DF` → RVA `0x00F0BD58` (`.data`; read/write)
- `0x0075E9E6` → RVA `0x00F0BD54` (`.data`; write)
- `0x0075E9F8` → RVA `0x00F0BD58` (`.data`; write)
- `0x0075EA0B` → RVA `0x00F0BD60` (`.data`; read)
- `0x0075EA21` → RVA `0x00F0BD60` (`.data`; read/write)
- `0x0075EA51` → RVA `0x00F0BD60` (`.data`; write)
- `0x0075EAB1` → RVA `0x00F0D101` (`.data`; write)
- `0x0075EAC5` → RVA `0x00F0BD40` (`.data`; read/write)
- `0x0075EAF0` → RVA `0x00F0C9E0` (`.data`; read/write)
- `0x0075EB07` → RVA `0x00F0BD50` (`.data`; read/write)
- `0x0075EB26` → RVA `0x00F0C9E0` (`.data`; read)
- `0x0075EB4D` → RVA `0x00F0CE78` (`.data`; read)
- `0x0075EB54` → RVA `0x00F0CE70` (`.data`; read)
- `0x0075EB79` → RVA `0x00F0CE78` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **12**
  - `0x0075E750` → [EtwTraceKernelEvent](../../text/23/EtwTraceKernelEvent_function_00235350.md) (`PAGE` → `.text`)
  - `0x0075E80E` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (`PAGE` → `.text`)
  - `0x0075E846` → [PopDiagTraceShutdownAction](../../text/5D/PopDiagTraceShutdownAction_function_005D6F08.md) (`PAGE` → `.text`)
  - `0x0075EA1C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0075EA38` → [PoStoreDiagnosticContext](../../text/23/PoStoreDiagnosticContext_function_0023009C.md) (`PAGE` → `.text`)
  - `0x0075EA4C` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0075EA68` → [PoStoreDiagnosticContext](../../text/23/PoStoreDiagnosticContext_function_0023009C.md) (`PAGE` → `.text`)
  - `0x0075EA7D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0075EAD1` → [PopGetPolicyWorker](../../text/48/PopGetPolicyWorker_function_00482D24.md) (`PAGE` → `.text`)
  - `0x0075EB02` → [PopSetPowerActionState](../../text/4B/PopSetPowerActionState_function_004BC8A8.md) (`PAGE` → `.text`)
  - `0x0075EB3C` → [PopSetNotificationWork](../../text/48/PopSetNotificationWork_function_00482C78.md) (`PAGE` → `.text`)
  - `0x0075EBDA` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0075E6B4  40 55                           push rbp
0075E6B6  53                              push rbx
0075E6B7  56                              push rsi
0075E6B8  57                              push rdi
0075E6B9  41 54                           push r12
0075E6BB  41 55                           push r13
0075E6BD  41 56                           push r14
0075E6BF  41 57                           push r15
0075E6C1  48 8D 6C 24 E9                  lea rbp, [rsp - 0x17]
0075E6C6  48 81 EC B8 00 00 00            sub rsp, 0xb8
0075E6CD  48 8B 05 6C C0 6A 00            mov rax, qword ptr [rip + 0x6ac06c]
0075E6D4  48 33 C4                        xor rax, rsp
0075E6D7  48 89 45 07                     mov qword ptr [rbp + 7], rax
0075E6DB  48 83 65 DF 00                  and qword ptr [rbp - 0x21], 0
0075E6E0  45 33 F6                        xor r14d, r14d
0075E6E3  F7 05 23 84 86 00 00 80 00 00   test dword ptr [rip + 0x868423], 0x8000
0075E6ED  41 8B F1                        mov esi, r9d
0075E6F0  F2 41 0F 10 00                  movsd xmm0, qword ptr [r8]
0075E6F5  4D 8B E8                        mov r13, r8
0075E6F8  41 8B 40 08                     mov eax, dword ptr [r8 + 8]
0075E6FC  44 8B E2                        mov r12d, edx
0075E6FF  F2 0F 11 45 CF                  movsd qword ptr [rbp - 0x31], xmm0
0075E704  48 8B D9                        mov rbx, rcx
0075E707  8B 7D CF                        mov edi, dword ptr [rbp - 0x31]
0075E70A  41 B7 01                        mov r15b, 1
0075E70D  44 89 4D C7                     mov dword ptr [rbp - 0x39], r9d
0075E711  89 45 D7                        mov dword ptr [rbp - 0x29], eax
0075E714  74 3F                           je 0x14075e755
0075E716  44 21 75 03                     and dword ptr [rbp + 3], r14d
0075E71A  48 8D 45 E7                     lea rax, [rbp - 0x19]
0075E71E  44 89 4D F3                     mov dword ptr [rbp - 0xd], r9d
0075E722  41 8D 56 01                     lea edx, [r14 + 1]
0075E726  48 89 4D E7                     mov qword ptr [rbp - 0x19], rcx
0075E72A  41 B9 22 12 00 00               mov r9d, 0x1222
0075E730  48 8D 4D F7                     lea rcx, [rbp - 9]
0075E734  48 89 45 F7                     mov qword ptr [rbp - 9], rax
0075E738  41 B8 00 80 00 80               mov r8d, 0x80008000
0075E73E  89 7D EF                        mov dword ptr [rbp - 0x11], edi
0075E741  C7 45 FF 10 00 00 00            mov dword ptr [rbp - 1], 0x10
0075E748  C7 44 24 20 02 18 50 00         mov dword ptr [rsp + 0x20], 0x501802
0075E750  E8 FB 6B AD FF                  call 0x140235350
0075E755  8B 43 04                        mov eax, dword ptr [rbx + 4]
0075E758  84 C0                           test al, al
0075E75A  78 0F                           js 0x14075e76b
0075E75C  33 D2                           xor edx, edx
0075E75E  48 8B CB                        mov rcx, rbx
0075E761  E8 D2 EB 33 00                  call 0x140a9d338
0075E766  E9 25 04 00 00                  jmp 0x14075eb90
0075E76B  8B 55 7F                        mov edx, dword ptr [rbp + 0x7f]
0075E76E  48 8D 4D C7                     lea rcx, [rbp - 0x39]
0075E772  E8 05 6C 33 00                  call 0x140a9537c
0075E777  48 8D 4D CF                     lea rcx, [rbp - 0x31]
0075E77B  E8 CC 29 1B 00                  call 0x14091114c
0075E780  33 F6                           xor esi, esi
0075E782  88 45 C1                        mov byte ptr [rbp - 0x3f], al
0075E785  84 C0                           test al, al
0075E787  74 18                           je 0x14075e7a1
0075E789  BA BB 00 00 C0                  mov edx, 0xc00000bb
0075E78E  48 8B CB                        mov rcx, rbx
0075E791  E8 A2 EB 33 00                  call 0x140a9d338
0075E796  8B 7D CF                        mov edi, dword ptr [rbp - 0x31]
0075E799  8B 75 C7                        mov esi, dword ptr [rbp - 0x39]
0075E79C  E9 EB 03 00 00                  jmp 0x14075eb8c
0075E7A1  8B 7D CF                        mov edi, dword ptr [rbp - 0x31]
0075E7A4  8D 47 FE                        lea eax, [rdi - 2]
0075E7A7  83 F8 01                        cmp eax, 1
0075E7AA  77 05                           ja 0x14075e7b1
0075E7AC  0F BA 6D D3 1F                  bts dword ptr [rbp - 0x2d], 0x1f
0075E7B1  8B 43 04                        mov eax, dword ptr [rbx + 4]
0075E7B4  44 8A FE                        mov r15b, sil
0075E7B7  40 88 75 C0                     mov byte ptr [rbp - 0x40], sil
0075E7BB  A8 02                           test al, 2
0075E7BD  0F 85 52 03 00 00               jne 0x14075eb15
0075E7C3  83 C8 02                        or eax, 2
0075E7C6  89 43 04                        mov dword ptr [rbx + 4], eax
0075E7C9  B8 06 00 00 00                  mov eax, 6
0075E7CE  3B F8                           cmp edi, eax
0075E7D0  75 64                           jne 0x14075e836
0075E7D2  40 38 35 4F 7E 7A 00            cmp byte ptr [rip + 0x7a7e4f], sil
0075E7D9  74 5B                           je 0x14075e836
0075E7DB  8B 03                           mov eax, dword ptr [rbx]
0075E7DD  83 F8 02                        cmp eax, 2
0075E7E0  75 0E                           jne 0x14075e7f0
0075E7E2  8B 45 D3                        mov eax, dword ptr [rbp - 0x2d]
0075E7E5  8B FE                           mov edi, esi
0075E7E7  24 10                           and al, 0x10
0075E7E9  89 75 CF                        mov dword ptr [rbp - 0x31], esi
0075E7EC  F6 D8                           neg al
0075E7EE  EB 3B                           jmp 0x14075e82b
0075E7F0  85 C0                           test eax, eax
0075E7F2  75 28                           jne 0x14075e81c
0075E7F4  8A 05 4A E6 7A 00               mov al, byte ptr [rip + 0x7ae64a]
0075E7FA  8B FE                           mov edi, esi
0075E7FC  F6 D8                           neg al
0075E7FE  89 75 CF                        mov dword ptr [rbp - 0x31], esi
0075E801  45 1B F6                        sbb r14d, r14d
0075E804  33 C9                           xor ecx, ecx
0075E806  41 83 E6 10                     and r14d, 0x10
0075E80A  41 83 C6 10                     add r14d, 0x10
0075E80E  E8 CD FF C1 FF                  call 0x14037e7e0
0075E813  48 89 05 76 FF 7A 00            mov qword ptr [rip + 0x7aff76], rax
0075E81A  EB 1A                           jmp 0x14075e836
0075E81C  83 F8 0F                        cmp eax, 0xf
0075E81F  75 15                           jne 0x14075e836
0075E821  8B 45 D3                        mov eax, dword ptr [rbp - 0x2d]
0075E824  25 00 00 00 02                  and eax, 0x2000000
0075E829  F7 D8                           neg eax
0075E82B  45 1B F6                        sbb r14d, r14d
0075E82E  41 83 E6 F0                     and r14d, 0xfffffff0
0075E832  41 83 C6 20                     add r14d, 0x20
0075E836  8D 47 FC                        lea eax, [rdi - 4]
0075E839  83 F8 02                        cmp eax, 2
0075E83C  77 0D                           ja 0x14075e84b
0075E83E  44 8B 03                        mov r8d, dword ptr [rbx]
0075E841  41 8B D6                        mov edx, r14d
0075E844  8B CF                           mov ecx, edi
0075E846  E8 BD 86 E7 FF                  call 0x1405d6f08
0075E84B  40 38 35 EF D4 7A 00            cmp byte ptr [rip + 0x7ad4ef], sil
0075E852  75 05                           jne 0x14075e859
0075E854  E8 87 70 FA FF                  call 0x1407058e0
0075E859  85 FF                           test edi, edi
0075E85B  0F 84 B4 02 00 00               je 0x14075eb15
0075E861  44 8B 7D D3                     mov r15d, dword ptr [rbp - 0x2d]
0075E865  B8 05 00 00 00                  mov eax, 5
0075E86A  8B 15 D4 D4 7A 00               mov edx, dword ptr [rip + 0x7ad4d4]
0075E870  41 0F BA EF 1C                  bts r15d, 0x1c
0075E875  83 FF 07                        cmp edi, 7
0075E878  40 88 75 BF                     mov byte ptr [rbp - 0x41], sil
0075E87C  8B 75 C7                        mov esi, dword ptr [rbp - 0x39]
0075E87F  8B CF                           mov ecx, edi
0075E881  44 0F 45 7D D3                  cmovne r15d, dword ptr [rbp - 0x2d]
0075E886  83 FF 03                        cmp edi, 3
0075E889  0F 44 F0                        cmove esi, eax
0075E88C  B8 06 00 00 00                  mov eax, 6
0075E891  83 FF 04                        cmp edi, 4
0075E894  0F 44 F0                        cmove esi, eax
0075E897  89 75 C7                        mov dword ptr [rbp - 0x39], esi
0075E89A  E8 05 24 34 00                  call 0x140aa0ca4
0075E89F  85 C0                           test eax, eax
0075E8A1  78 73                           js 0x14075e916
0075E8A3  B8 01 00 00 00                  mov eax, 1
0075E8A8  48 8D 4D BF                     lea rcx, [rbp - 0x41]
0075E8AC  8B D0                           mov edx, eax
0075E8AE  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
0075E8B2  45 33 C9                        xor r9d, r9d
0075E8B5  45 8B C7                        mov r8d, r15d
0075E8B8  E8 0B 31 36 00                  call 0x140ac19c8
0075E8BD  45 8B C7                        mov r8d, r15d
0075E8C0  C7 44 24 20 02 00 00 00         mov dword ptr [rsp + 0x20], 2
0075E8C8  41 8D 51 01                     lea edx, [r9 + 1]
0075E8CC  48 8D 4D BF                     lea rcx, [rbp - 0x41]
0075E8D0  E8 F3 30 36 00                  call 0x140ac19c8
0075E8D5  45 8B C7                        mov r8d, r15d
0075E8D8  C7 44 24 20 00 00 00 10         mov dword ptr [rsp + 0x20], 0x10000000
0075E8E0  41 8D 51 04                     lea edx, [r9 + 4]
0075E8E4  48 8D 4D BF                     lea rcx, [rbp - 0x41]
0075E8E8  E8 DB 30 36 00                  call 0x140ac19c8
0075E8ED  83 FF 02                        cmp edi, 2
0075E8F0  75 12                           jne 0x14075e904
0075E8F2  48 8B 05 6F E5 7A 00            mov rax, qword ptr [rip + 0x7ae56f]
0075E8F9  8B 48 44                        mov ecx, dword ptr [rax + 0x44]
0075E8FC  3B F1                           cmp esi, ecx
0075E8FE  0F 4C F1                        cmovl esi, ecx
0075E901  89 75 C7                        mov dword ptr [rbp - 0x39], esi
0075E904  3B 35 3E D4 7A 00               cmp esi, dword ptr [rip + 0x7ad43e]
0075E90A  7E 0A                           jle 0x14075e916
0075E90C  80 4D BF 04                     or byte ptr [rbp - 0x41], 4
0075E910  89 35 32 D4 7A 00               mov dword ptr [rip + 0x7ad432], esi
0075E916  41 B1 01                        mov r9b, 1
0075E919  C7 44 24 20 04 00 00 00         mov dword ptr [rsp + 0x20], 4
0075E921  45 8B C7                        mov r8d, r15d
0075E924  48 8D 4D BF                     lea rcx, [rbp - 0x41]
0075E928  BA 01 00 00 00                  mov edx, 1
0075E92D  E8 96 30 36 00                  call 0x140ac19c8
0075E932  45 8B C7                        mov r8d, r15d
0075E935  C7 44 24 20 00 00 00 80         mov dword ptr [rsp + 0x20], 0x80000000
0075E93D  BA 05 00 00 00                  mov edx, 5
0075E942  48 8D 4D BF                     lea rcx, [rbp - 0x41]
0075E946  E8 7D 30 36 00                  call 0x140ac19c8
0075E94B  45 8B C7                        mov r8d, r15d
0075E94E  C7 44 24 20 00 00 00 40         mov dword ptr [rsp + 0x20], 0x40000000
0075E956  33 D2                           xor edx, edx
0075E958  48 8D 4D BF                     lea rcx, [rbp - 0x41]
0075E95C  E8 67 30 36 00                  call 0x140ac19c8
0075E961  45 8B C7                        mov r8d, r15d
0075E964  C7 44 24 20 08 00 00 00         mov dword ptr [rsp + 0x20], 8
0075E96C  33 D2                           xor edx, edx
0075E96E  48 8D 4D BF                     lea rcx, [rbp - 0x41]
0075E972  E8 51 30 36 00                  call 0x140ac19c8
0075E977  45 8B C7                        mov r8d, r15d
0075E97A  C7 44 24 20 20 00 00 00         mov dword ptr [rsp + 0x20], 0x20
0075E982  33 D2                           xor edx, edx
0075E984  48 8D 4D BF                     lea rcx, [rbp - 0x41]
0075E988  E8 3B 30 36 00                  call 0x140ac19c8
0075E98D  44 8B 0D B0 D3 7A 00            mov r9d, dword ptr [rip + 0x7ad3b0]
0075E994  8B CF                           mov ecx, edi
0075E996  41 8B D1                        mov edx, r9d
0075E999  E8 06 23 34 00                  call 0x140aa0ca4
0075E99E  85 C0                           test eax, eax
0075E9A0  0F 8E E6 00 00 00               jle 0x14075ea8c
0075E9A6  BA 03 00 00 00                  mov edx, 3
0075E9AB  8B CF                           mov ecx, edi
0075E9AD  E8 F2 22 34 00                  call 0x140aa0ca4
0075E9B2  44 8A 7D BF                     mov r15b, byte ptr [rbp - 0x41]
0075E9B6  85 C0                           test eax, eax
0075E9B8  78 04                           js 0x14075e9be
0075E9BA  41 80 CF 02                     or r15b, 2
0075E9BE  BA 08 00 00 00                  mov edx, 8
0075E9C3  41 8B C9                        mov ecx, r9d
0075E9C6  E8 D9 22 34 00                  call 0x140aa0ca4
0075E9CB  85 C0                           test eax, eax
0075E9CD  75 04                           jne 0x14075e9d3
0075E9CF  41 80 CF 02                     or r15b, 2
0075E9D3  89 3D 6B D3 7A 00               mov dword ptr [rip + 0x7ad36b], edi
0075E9D9  41 80 CF 05                     or r15b, 5
0075E9DD  8B 03                           mov eax, dword ptr [rbx]
0075E9DF  83 25 72 D3 7A 00 00            and dword ptr [rip + 0x7ad372], 0
0075E9E6  89 05 68 D3 7A 00               mov dword ptr [rip + 0x7ad368], eax
0075E9EC  83 3B 00                        cmp dword ptr [rbx], 0
0075E9EF  44 88 7D BF                     mov byte ptr [rbp - 0x41], r15b
0075E9F3  75 09                           jne 0x14075e9fe
0075E9F5  8B 43 18                        mov eax, dword ptr [rbx + 0x18]
0075E9F8  89 05 5A D3 7A 00               mov dword ptr [rip + 0x7ad35a], eax
0075E9FE  F7 43 04 00 01 00 00            test dword ptr [rbx + 4], 0x100
0075EA05  0F 85 85 00 00 00               jne 0x14075ea90
0075EA0B  48 8B 0D 4E D3 7A 00            mov rcx, qword ptr [rip + 0x7ad34e]
0075EA12  48 85 C9                        test rcx, rcx
0075EA15  74 12                           je 0x14075ea29
0075EA17  BA 50 64 69 67                  mov edx, 0x67696450
0075EA1C  E8 4F 3E 42 00                  call 0x140b82870
0075EA21  48 83 25 37 D3 7A 00 00         and qword ptr [rip + 0x7ad337], 0
0075EA29  48 8B 4B 10                     mov rcx, qword ptr [rbx + 0x10]
0075EA2D  48 85 C9                        test rcx, rcx
0075EA30  74 5E                           je 0x14075ea90
0075EA32  4C 8D 45 DF                     lea r8, [rbp - 0x21]
0075EA36  33 D2                           xor edx, edx
0075EA38  E8 5F 16 AD FF                  call 0x14023009c
0075EA3D  48 8B 55 DF                     mov rdx, qword ptr [rbp - 0x21]
0075EA41  41 B8 50 64 69 67               mov r8d, 0x67696450
0075EA47  B9 00 01 00 00                  mov ecx, 0x100
0075EA4C  E8 9F 36 42 00                  call 0x140b820f0
0075EA51  48 89 05 08 D3 7A 00            mov qword ptr [rip + 0x7ad308], rax
0075EA58  48 85 C0                        test rax, rax
0075EA5B  74 33                           je 0x14075ea90
0075EA5D  48 8B 4B 10                     mov rcx, qword ptr [rbx + 0x10]
0075EA61  4C 8D 45 DF                     lea r8, [rbp - 0x21]
0075EA65  48 8B D0                        mov rdx, rax
0075EA68  E8 2F 16 AD FF                  call 0x14023009c
0075EA6D  85 C0                           test eax, eax
0075EA6F  79 1F                           jns 0x14075ea90
0075EA71  48 8B 0D E8 D2 7A 00            mov rcx, qword ptr [rip + 0x7ad2e8]
0075EA78  BA 50 64 69 67                  mov edx, 0x67696450
0075EA7D  E8 EE 3D 42 00                  call 0x140b82870
0075EA82  48 83 25 D6 D2 7A 00 00         and qword ptr [rip + 0x7ad2d6], 0
0075EA8A  EB 04                           jmp 0x14075ea90
0075EA8C  44 8A 7D BF                     mov r15b, byte ptr [rbp - 0x41]
0075EA90  83 3D AD D2 7A 00 03            cmp dword ptr [rip + 0x7ad2ad], 3
0075EA97  75 0A                           jne 0x14075eaa3
0075EA99  C7 05 A1 D2 7A 00 02 00 00 00   mov dword ptr [rip + 0x7ad2a1], 2
0075EAA3  45 84 FF                        test r15b, r15b
0075EAA6  74 2E                           je 0x14075ead6
0075EAA8  E8 2B 59 1B 00                  call 0x1409143d8
0075EAAD  84 C0                           test al, al
0075EAAF  74 07                           je 0x14075eab8
0075EAB1  C6 05 49 E6 7A 00 01            mov byte ptr [rip + 0x7ae649], 1
0075EAB8  80 3D 82 D2 7A 00 02            cmp byte ptr [rip + 0x7ad282], 2
0075EABF  C6 45 C0 01                     mov byte ptr [rbp - 0x40], 1
0075EAC3  72 3B                           jb 0x14075eb00
0075EAC5  44 08 3D 74 D2 7A 00            or byte ptr [rip + 0x7ad274], r15b
0075EACC  B9 01 00 00 00                  mov ecx, 1
0075EAD1  E8 4E 42 D2 FF                  call 0x140482d24
0075EAD6  44 8A 7D C0                     mov r15b, byte ptr [rbp - 0x40]
0075EADA  8B 43 04                        mov eax, dword ptr [rbx + 4]
0075EADD  A8 01                           test al, 1
0075EADF  75 60                           jne 0x14075eb41
0075EAE1  83 C8 01                        or eax, 1
0075EAE4  89 43 04                        mov dword ptr [rbx + 4], eax
0075EAE7  41 83 FE 20                     cmp r14d, 0x20
0075EAEB  75 2D                           jne 0x14075eb1a
0075EAED  41 8B C6                        mov eax, r14d
0075EAF0  87 05 EA DE 7A 00               xchg dword ptr [rip + 0x7adeea], eax
0075EAF6  85 C0                           test eax, eax
0075EAF8  75 39                           jne 0x14075eb33
0075EAFA  41 83 CC 10                     or r12d, 0x10
0075EAFE  EB 33                           jmp 0x14075eb33
0075EB00  B1 01                           mov cl, 1
0075EB02  E8 A1 DD D5 FF                  call 0x1404bc8a8
0075EB07  83 25 42 D2 7A 00 00            and dword ptr [rip + 0x7ad242], 0
0075EB0E  B9 02 00 00 00                  mov ecx, 2
0075EB13  EB BC                           jmp 0x14075ead1
0075EB15  8B 75 C7                        mov esi, dword ptr [rbp - 0x39]
0075EB18  EB C0                           jmp 0x14075eada
0075EB1A  B9 10 00 00 00                  mov ecx, 0x10
0075EB1F  44 3B F1                        cmp r14d, ecx
0075EB22  75 15                           jne 0x14075eb39
0075EB24  33 C0                           xor eax, eax
0075EB26  F0 0F B1 0D B2 DE 7A 00         lock cmpxchg dword ptr [rip + 0x7adeb2], ecx
0075EB2E  75 03                           jne 0x14075eb33
0075EB30  44 0B E1                        or r12d, ecx
0075EB33  8B 7D CF                        mov edi, dword ptr [rbp - 0x31]
0075EB36  8B 75 C7                        mov esi, dword ptr [rbp - 0x39]
0075EB39  41 8B CC                        mov ecx, r12d
0075EB3C  E8 37 41 D2 FF                  call 0x140482c78
0075EB41  8B 43 04                        mov eax, dword ptr [rbx + 4]
0075EB44  A8 20                           test al, 0x20
0075EB46  74 44                           je 0x14075eb8c
0075EB48  45 84 FF                        test r15b, r15b
0075EB4B  74 35                           je 0x14075eb82
0075EB4D  48 8B 0D 24 E3 7A 00            mov rcx, qword ptr [rip + 0x7ae324]
0075EB54  48 8D 15 15 E3 7A 00            lea rdx, [rip + 0x7ae315]
0075EB5B  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
0075EB5F  48 83 C0 20                     add rax, 0x20
0075EB63  48 39 11                        cmp qword ptr [rcx], rdx
0075EB66  74 07                           je 0x14075eb6f
0075EB68  B9 03 00 00 00                  mov ecx, 3
0075EB6D  CD 29                           int 0x29
0075EB6F  48 89 10                        mov qword ptr [rax], rdx
0075EB72  48 89 48 08                     mov qword ptr [rax + 8], rcx
0075EB76  48 89 01                        mov qword ptr [rcx], rax
0075EB79  48 89 05 F8 E2 7A 00            mov qword ptr [rip + 0x7ae2f8], rax
0075EB80  EB 0A                           jmp 0x14075eb8c
0075EB82  33 D2                           xor edx, edx
0075EB84  48 8B CB                        mov rcx, rbx
0075EB87  E8 AC E7 33 00                  call 0x140a9d338
0075EB8C  44 8A 7D C1                     mov r15b, byte ptr [rbp - 0x3f]
0075EB90  8B 45 D7                        mov eax, dword ptr [rbp - 0x29]
0075EB93  45 8B C4                        mov r8d, r12d
0075EB96  45 8B 4D 00                     mov r9d, dword ptr [r13]
0075EB9A  8B 53 04                        mov edx, dword ptr [rbx + 4]
0075EB9D  8B 0B                           mov ecx, dword ptr [rbx]
0075EB9F  44 88 7C 24 58                  mov byte ptr [rsp + 0x58], r15b
0075EBA4  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
0075EBA8  8B 45 D3                        mov eax, dword ptr [rbp - 0x2d]
0075EBAB  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
0075EBAF  8B 45 7F                        mov eax, dword ptr [rbp + 0x7f]
0075EBB2  89 7C 24 40                     mov dword ptr [rsp + 0x40], edi
0075EBB6  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
0075EBBA  41 8B 45 08                     mov eax, dword ptr [r13 + 8]
0075EBBE  89 74 24 30                     mov dword ptr [rsp + 0x30], esi
0075EBC2  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
0075EBC6  41 8B 45 04                     mov eax, dword ptr [r13 + 4]
0075EBCA  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
0075EBCE  E8 69 2B 35 00                  call 0x140ab173c
0075EBD3  48 8B 4D 07                     mov rcx, qword ptr [rbp + 7]
0075EBD7  48 33 CC                        xor rcx, rsp
0075EBDA  E8 61 DA F4 FF                  call 0x1406ac640
0075EBDF  48 81 C4 B8 00 00 00            add rsp, 0xb8
0075EBE6  41 5F                           pop r15
0075EBE8  41 5E                           pop r14
0075EBEA  41 5D                           pop r13
0075EBEC  41 5C                           pop r12
0075EBEE  5F                              pop rdi
0075EBEF  5E                              pop rsi
0075EBF0  5B                              pop rbx
0075EBF1  5D                              pop rbp
0075EBF2  C3                              ret
0075EBF3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopExecutePowerAction(__int64 a1, int a2, __int64 a3, int a4, unsigned int a5)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m50;
    unsigned int v_stack_m54;
    unsigned __int64 v_stack_m57;
    unsigned int v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned int v_stack_m64;
    unsigned int v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned int v_stack_m80;
    unsigned int v_stack_m84;
    unsigned __int64 v_stack_m88;
    unsigned int v_stack_m90;
    unsigned __int8 v_stack_m96;
    unsigned __int8 v_stack_m97;
    unsigned __int8 v_stack_m98;
    unsigned __int8 v_stack_mA0;
    unsigned int v_stack_mA8;
    unsigned int v_stack_mB0;
    unsigned int v_stack_mB8;
    unsigned int v_stack_mC0;
    unsigned int v_stack_mC8;
    unsigned int v_stack_mD0;
    unsigned int v_stack_mD8;

    v_rsp = (v_rsp) - (184);
    result = (*(unsigned __int64 *)(v_rip + 6996076)) ^ (v_rsp);
    v_stack_m50 = result;
    v_r14 = 0;
    v_stack_m88 = v_xmm0;
    v_stack_m90 = a4;
    v_stack_m80 = (unsigned int)((unsigned int)(*(unsigned int *)(a3 + 8)));
    result = (unsigned int)(*(unsigned int *)(a3 + 8));
    if (((*(unsigned int *)(v_rip + 8815651)) & (0x8000ULL)) != 0) {
        result = v_stack_m70;
        v_stack_m64 = a4;
        a2 = v_r14 + 1;
        v_stack_m70 = a1;
        a4 = 0x1222ULL;
        a1 = v_stack_m60;
        v_stack_m60 = result;
        a3 = 0x80008000ULL;
        v_stack_m68 = (unsigned int)((unsigned int)(v_stack_m88));
        v_stack_m58 = 16;
        v_stack_mD8 = 0x501802ULL;
        result = EtwTraceKernelEvent(a1, a2, a3, a4);
    }
    if (sign_flag) goto loc_0075E76B;
    a2 = 0;
    result = PopCompleteAction(a1, a2, a3, a4);
    goto loc_0075EB90;
loc_0075E76B:
    result = PopVerifySystemPowerState(v_stack_m90, (unsigned int)(a5), a3, a4);
    result = PopVerifyPowerActionPolicy(v_stack_m88, (unsigned int)(a5), a3, a4);
    v_rsi = 0;
    v_stack_m96 = (unsigned __int8)(result);
    if ((unsigned __int8)(result) == 0) goto loc_0075E7A1;
    result = PopCompleteAction(a1, (unsigned int)(0xC00000BBULL), a3, a4);
    goto loc_0075EB8C;
loc_0075E7A1:
    if (((unsigned int)((unsigned int)(v_stack_m88) - 2)) <= 1) {
    }
    v_stack_m97 = (unsigned __int8)((unsigned int)(v_stack_m90));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 4)))) & (2)) != 0) goto loc_0075EB15;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 4))) | (2));
    *(unsigned int *)(a1 + 4) = (unsigned int)(result);
    if (((unsigned int)((unsigned int)(v_stack_m88))) != 6) goto loc_0075E836;
    if ((*(unsigned __int8 *)(v_rip + 8027727)) == ((unsigned __int8)((unsigned int)(v_stack_m90)))) goto loc_0075E836;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1)))) != 2) goto loc_0075E7F0;
    result = (unsigned __int8)(((unsigned int)(v_stack_m84)) & (16));
    v_stack_m88 = (unsigned int)((unsigned int)(v_stack_m90));
    result = (unsigned __int8)(-(result));
    goto loc_0075E82B;
loc_0075E7F0:
    if ((unsigned int)(result) != 0) goto loc_0075E81C;
    result = (unsigned __int8)(-(*(unsigned __int8 *)(v_rip + 8054346)));
    v_stack_m88 = (unsigned int)((unsigned int)(v_stack_m90));
    a1 = 0;
    v_r14 = (unsigned int)((v_r14) & (16));
    v_r14 = (unsigned int)((v_r14) + (16));
    result = KeQueryPerformanceCounter(a1, (unsigned int)(0xC00000BBULL), a3, a4);
    *(unsigned __int64 *)(v_rip + 8060790) = result;
    goto loc_0075E836;
loc_0075E81C:
    if (((unsigned int)(result)) != 15) goto loc_0075E836;
    result = (unsigned int)(((unsigned int)(v_stack_m84)) & (0x2000000ULL));
    result = (unsigned int)(-(result));
loc_0075E82B:
    v_r14 = (unsigned int)((v_r14) & (0xFFFFFFF0ULL));
    v_r14 = (unsigned int)((v_r14) + (32));
loc_0075E836:
    result = (unsigned int)((unsigned int)((unsigned int)(v_stack_m90))) - 4;
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m90))) - 4)) <= 2) {
        a3 = *(unsigned int *)(a1);
        a2 = (unsigned int)(v_r14);
        a1 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m90))));
        result = PopDiagTraceShutdownAction(a1, a2, a3, a4);
    }
    if ((*(unsigned __int8 *)(v_rip + 8049903)) == ((unsigned __int8)((unsigned int)(v_stack_m90)))) {
        result = PopResetActionDefaults(a1, a2, a3, a4);
    }
    if ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m90)))) == 0) goto loc_0075EB15;
    v_stack_m98 = (unsigned __int8)((unsigned int)(v_stack_m90));
    v_r15 = (unsigned int)(v_stack_m84);
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m90))))) != 7) { v_r15 = v_stack_m84; }
    v_rsi = (unsigned int)(v_stack_m90);
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m90))))) == 3) { v_rsi = 5; }
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m90))))) == 4) { v_rsi = 6; }
    v_stack_m90 = (unsigned int)(v_rsi);
    result = PopCompareActions((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m90))))), (unsigned int)(*(unsigned int *)(v_rip + 8049876)), a3, a4);
    if (sign_flag) goto loc_0075E916;
    v_stack_mD8 = 1;
    a4 = 0;
    result = PopPromoteActionFlag(v_stack_m98, 1, (unsigned int)((unsigned int)(v_r15)), a4);
    v_stack_mD8 = 2;
    result = PopPromoteActionFlag(v_stack_m98, a4 + 1, (unsigned int)((unsigned int)(v_r15)), a4);
    v_stack_mD8 = 0x10000000ULL;
    result = PopPromoteActionFlag(v_stack_m98, a4 + 4, (unsigned int)((unsigned int)(v_r15)), a4);
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m90))))) == 2) {
        result = *(unsigned __int64 *)(v_rip + 8054127);
        a1 = *(unsigned int *)(result + 68);
        if (((unsigned int)(v_rsi)) < ((unsigned int)(a1))) { v_rsi = (unsigned int)(a1); }
        v_stack_m90 = (unsigned int)(v_rsi);
    }
    if (((unsigned int)(v_rsi)) >= = (*(unsigned int *)(v_rip + 8049726))) {
        *(unsigned int *)(v_rip + 8049714) = (unsigned int)(v_rsi);
    }
    v_stack_mD8 = 4;
    result = PopPromoteActionFlag(v_stack_m98, 1, (unsigned int)((unsigned int)(v_r15)), 1);
    v_stack_mD8 = 0x80000000ULL;
    result = PopPromoteActionFlag(v_stack_m98, 5, (unsigned int)((unsigned int)(v_r15)), 1);
    v_stack_mD8 = 0x40000000ULL;
    a2 = 0;
    result = PopPromoteActionFlag(v_stack_m98, a2, (unsigned int)((unsigned int)(v_r15)), 1);
    v_stack_mD8 = 8;
    a2 = 0;
    result = PopPromoteActionFlag(v_stack_m98, a2, (unsigned int)((unsigned int)(v_r15)), 1);
    v_stack_mD8 = 32;
    a2 = 0;
    result = PopPromoteActionFlag(v_stack_m98, a2, (unsigned int)((unsigned int)(v_r15)), 1);
    result = PopCompareActions((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m90))))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 8049584)))), (unsigned int)((unsigned int)(v_r15)), (unsigned int)(*(unsigned int *)(v_rip + 8049584)));
    if (condition_is_less_or_equal) goto loc_0075EA8C;
    result = PopCompareActions((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m90))))), 3, (unsigned int)((unsigned int)(v_r15)), (unsigned int)(*(unsigned int *)(v_rip + 8049584)));
    v_r15 = v_stack_m98;
    if (!(sign_flag)) {
        v_r15 = (unsigned __int8)((v_stack_m98) | (2));
    }
    result = PopCompareActions((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 8049584)))), 8, (unsigned int)((unsigned int)(v_r15)), (unsigned int)(*(unsigned int *)(v_rip + 8049584)));
    if ((unsigned int)(result) == 0) {
        v_r15 = (unsigned __int8)((v_r15) | (2));
    }
    *(unsigned int *)(v_rip + 8049515) = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m90))));
    v_r15 = (unsigned __int8)((v_r15) | (5));
    *(unsigned int *)(v_rip + 8049512) = (unsigned int)((unsigned int)(*(unsigned int *)(a1)));
    v_stack_m98 = (unsigned __int8)(v_r15);
    result = (unsigned int)(*(unsigned int *)(a1));
    if ((*(unsigned int *)(a1)) == 0) {
        result = *(unsigned int *)(a1 + 24);
        *(unsigned int *)(v_rip + 8049498) = (unsigned int)(result);
    }
    if (((*(unsigned int *)(a1 + 4)) & (256)) != 0) goto loc_0075EA90;
    if (*(unsigned __int64 *)(v_rip + 8049486) != 0) {
        a2 = 0x67696450ULL;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(v_rip + 8049486), a2, (unsigned int)((unsigned int)(v_r15)), (unsigned int)(*(unsigned int *)(v_rip + 8049584)));
    }
    if (*(unsigned __int64 *)(a1 + 16) == 0) goto loc_0075EA90;
    a2 = 0;
    result = PoStoreDiagnosticContext(*(unsigned __int64 *)(a1 + 16), a2, v_stack_m78, (unsigned int)(*(unsigned int *)(v_rip + 8049584)));
    result = ExAllocatePool2(256, v_stack_m78, (unsigned int)(0x67696450ULL), (unsigned int)(*(unsigned int *)(v_rip + 8049584)));
    *(unsigned __int64 *)(v_rip + 8049416) = result;
    if (result == 0) goto loc_0075EA90;
    result = PoStoreDiagnosticContext(*(unsigned __int64 *)(a1 + 16), result, v_stack_m78, (unsigned int)(*(unsigned int *)(v_rip + 8049584)));
    if (!sign_flag) goto loc_0075EA90;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(v_rip + 8049384), (unsigned int)(0x67696450ULL), v_stack_m78, (unsigned int)(*(unsigned int *)(v_rip + 8049584)));
    goto loc_0075EA90;
loc_0075EA8C:
loc_0075EA90:
    if ((*(unsigned int *)(v_rip + 8049325)) == 3) {
        *(unsigned int *)(v_rip + 8049313) = 2;
    }
    if ((unsigned __int8)(v_stack_m98) == 0) goto loc_0075EAD6;
    result = TtmIsEnabled(*(unsigned __int64 *)(v_rip + 8049384), (unsigned int)(0x67696450ULL), v_stack_m78, (unsigned int)(*(unsigned int *)(v_rip + 8049584)));
    if ((unsigned __int8)(result) != 0) {
        *(unsigned __int8 *)(v_rip + 8054345) = 1;
    }
    v_stack_m97 = 1;
    if ((*(unsigned __int8 *)(v_rip + 8049282)) < 2) goto loc_0075EB00;
loc_0075EAD1:
    result = PopGetPolicyWorker(1, (unsigned int)(0x67696450ULL), v_stack_m78, (unsigned int)(*(unsigned int *)(v_rip + 8049584)));
loc_0075EAD6:
loc_0075EADA:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 4)))) & (1)) != 0) goto loc_0075EB41;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 4))) | (1));
    *(unsigned int *)(a1 + 4) = (unsigned int)(result);
    if (((unsigned int)(v_r14)) != 32) goto loc_0075EB1A;
    if ((unsigned int)((unsigned int)((unsigned int)(v_r14))) != 0) goto loc_0075EB33;
    v_r12 = (unsigned int)(((unsigned int)(a2)) | (16));
    goto loc_0075EB33;
loc_0075EB00:
    result = PopSetPowerActionState(1, (unsigned int)(0x67696450ULL), v_stack_m78, (unsigned int)(*(unsigned int *)(v_rip + 8049584)));
    goto loc_0075EAD1;
loc_0075EB15:
    goto loc_0075EADA;
loc_0075EB1A:
    if (((unsigned int)(v_r14)) != 16) goto loc_0075EB39;
    result = 0;
    if (!(condition_is_not_equal)) {
        v_r12 = (unsigned int)((v_r12) | (16));
    }
loc_0075EB39:
    result = PopSetNotificationWork((unsigned int)((unsigned int)(v_r12)), (unsigned int)(0x67696450ULL), v_stack_m78, (unsigned int)(*(unsigned int *)(v_rip + 8049584)));
loc_0075EB41:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 4)))) & (32)) == 0) goto loc_0075EB8C;
    if ((unsigned __int8)(v_stack_m97) == 0) goto loc_0075EB82;
    result = (*(unsigned __int64 *)(a1 + 8)) + (32);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 8053540))) != (v_rip + 8053525)) {
        a1 = 3;
    }
    *(unsigned __int64 *)(result) = v_rip + 8053525;
    *(unsigned __int64 *)(result + 8) = a1;
    *(unsigned __int64 *)(a1) = result;
    *(unsigned __int64 *)(v_rip + 8053496) = result;
    goto loc_0075EB8C;
loc_0075EB82:
    a2 = 0;
    result = PopCompleteAction(a1, a2, v_stack_m78, (unsigned int)(*(unsigned int *)(v_rip + 8049584)));
loc_0075EB8C:
loc_0075EB90:
    v_stack_mA0 = (unsigned __int8)(v_stack_m96);
    v_stack_mA8 = (unsigned int)((unsigned int)(v_stack_m80));
    v_stack_mB0 = (unsigned int)((unsigned int)(v_stack_m84));
    v_stack_mB8 = (unsigned int)((unsigned int)(v_stack_m88));
    v_stack_mC0 = (unsigned int)((unsigned int)(a5));
    v_stack_mC8 = (unsigned int)((unsigned int)(v_stack_m90));
    v_stack_mD0 = (unsigned int)((unsigned int)(*(unsigned int *)(a3 + 8)));
    v_stack_mD8 = (unsigned int)((unsigned int)(*(unsigned int *)(a3 + 4)));
    result = PopDiagTraceExecutePowerAction((unsigned int)(*(unsigned int *)(a1)), (unsigned int)(*(unsigned int *)(a1 + 4)), (unsigned int)((unsigned int)(v_r12)), (unsigned int)(*(unsigned int *)(a3)));
    a1 = (v_stack_m50) ^ (v_rsp);
    result = _security_check_cookie(a1, (unsigned int)(*(unsigned int *)(a1 + 4)), (unsigned int)((unsigned int)(v_r12)), (unsigned int)(*(unsigned int *)(a3)));
    v_rsp = (v_rsp) + (184);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopExecutePowerAction(void *Arg1, int32_t Arg2, void *Arg3, int32_t Arg4, uint32_t Arg5)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m50;
    uint32_t v_stack_m54;
    uint64_t v_stack_m57;
    uint32_t v_stack_m58;
    uint64_t v_stack_m60;
    uint32_t v_stack_m64;
    uint32_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint32_t v_stack_m80;
    uint32_t v_stack_m84;
    uint64_t v_stack_m88;
    uint32_t v_stack_m90;
    uint8_t v_stack_m96;
    uint8_t v_stack_m97;
    uint8_t v_stack_m98;
    uint8_t v_stack_mA0;
    uint32_t v_stack_mA8;
    uint32_t v_stack_mB0;
    uint32_t v_stack_mB8;
    uint32_t v_stack_mC0;
    uint32_t v_stack_mC8;
    uint32_t v_stack_mD0;
    uint32_t v_stack_mD8;

    local_rsp = (local_rsp) - (184);
    result = (*(uint64_t *)(v_rip + 0x6AC06C)) ^ (local_rsp);
    v_stack_m50 = result;
    local_r14 = 0;
    v_stack_m88 = v_xmm0;
    v_stack_m90 = Arg4;
    v_stack_m80 = (uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0x8)));
    result = (uint32_t)(*(uint32_t *)(arg3 + 0x8));
    if (((*(uint32_t *)(v_rip + 0x868423)) & (0x8000ULL)) != 0) {
        result = v_stack_m70;
        v_stack_m64 = Arg4;
        Arg2 = local_r14 + 1;
        v_stack_m70 = Arg1;
        Arg4 = 0x1222ULL;
        Arg1 = v_stack_m60;
        v_stack_m60 = result;
        Arg3 = 0x80008000ULL;
        v_stack_m68 = (uint32_t)((uint32_t)(v_stack_m88));
        v_stack_m58 = 16;
        v_stack_mD8 = 0x501802ULL;
        result = EtwTraceKernelEvent(Arg1, Arg2, Arg3, Arg4);
    }
    if (sign_flag) goto loc_0075E76B;
    Arg2 = 0;
    result = PopCompleteAction(Arg1, Arg2, Arg3, Arg4);
    goto loc_0075EB90;
loc_0075E76B:
    result = PopVerifySystemPowerState(v_stack_m90, (uint32_t)(Arg5), Arg3, Arg4);
    result = PopVerifyPowerActionPolicy(v_stack_m88, (uint32_t)(Arg5), Arg3, Arg4);
    local_rsi = 0;
    v_stack_m96 = (uint8_t)(result);
    if ((uint8_t)(result) == 0) goto loc_0075E7A1;
    result = PopCompleteAction(Arg1, (uint32_t)(0xC00000BBULL), Arg3, Arg4);
    goto loc_0075EB8C;
loc_0075E7A1:
    if (((uint32_t)((uint32_t)(v_stack_m88) - 2)) <= 1) {
    }
    v_stack_m97 = (uint8_t)((uint32_t)(v_stack_m90));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)))) & (2)) != 0) goto loc_0075EB15;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x4))) | (2));
    *(uint32_t *)(arg1 + 0x4) = (uint32_t)(result);
    if (((uint32_t)((uint32_t)(v_stack_m88))) != 6) goto loc_0075E836;
    if ((*(uint8_t *)(v_rip + 0x7A7E4F)) == ((uint8_t)((uint32_t)(v_stack_m90)))) goto loc_0075E836;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1)))) != 2) goto loc_0075E7F0;
    result = (uint8_t)(((uint32_t)(v_stack_m84)) & (16));
    v_stack_m88 = (uint32_t)((uint32_t)(v_stack_m90));
    result = (uint8_t)(-(result));
    goto loc_0075E82B;
loc_0075E7F0:
    if ((uint32_t)(result) != 0) goto loc_0075E81C;
    result = (uint8_t)(-(*(uint8_t *)(v_rip + 0x7AE64A)));
    v_stack_m88 = (uint32_t)((uint32_t)(v_stack_m90));
    Arg1 = 0;
    local_r14 = (uint32_t)((local_r14) & (16));
    local_r14 = (uint32_t)((local_r14) + (16));
    result = KeQueryPerformanceCounter(Arg1, (uint32_t)(0xC00000BBULL), Arg3, Arg4);
    *(uint64_t *)(v_rip + 0x7AFF76) = result;
    goto loc_0075E836;
loc_0075E81C:
    if (((uint32_t)(result)) != 15) goto loc_0075E836;
    result = (uint32_t)(((uint32_t)(v_stack_m84)) & (0x2000000ULL));
    result = (uint32_t)(-(result));
loc_0075E82B:
    local_r14 = (uint32_t)((local_r14) & (0xFFFFFFF0ULL));
    local_r14 = (uint32_t)((local_r14) + (32));
loc_0075E836:
    result = (uint32_t)((uint32_t)((uint32_t)(v_stack_m90))) - 4;
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m90))) - 4)) <= 2) {
        Arg3 = *(uint32_t *)(arg1);
        Arg2 = (uint32_t)(local_r14);
        Arg1 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m90))));
        result = PopDiagTraceShutdownAction(Arg1, Arg2, Arg3, Arg4);
    }
    if ((*(uint8_t *)(v_rip + 0x7AD4EF)) == ((uint8_t)((uint32_t)(v_stack_m90)))) {
        result = PopResetActionDefaults(Arg1, Arg2, Arg3, Arg4);
    }
    if ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m90)))) == 0) goto loc_0075EB15;
    v_stack_m98 = (uint8_t)((uint32_t)(v_stack_m90));
    local_r15 = (uint32_t)(v_stack_m84);
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m90))))) != 7) { local_r15 = v_stack_m84; }
    local_rsi = (uint32_t)(v_stack_m90);
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m90))))) == 3) { local_rsi = 5; }
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m90))))) == 4) { local_rsi = 6; }
    v_stack_m90 = (uint32_t)(local_rsi);
    result = PopCompareActions((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m90))))), (uint32_t)(*(uint32_t *)(v_rip + 0x7AD4D4)), Arg3, Arg4);
    if (sign_flag) goto loc_0075E916;
    v_stack_mD8 = 1;
    Arg4 = 0;
    result = PopPromoteActionFlag(v_stack_m98, 1, (uint32_t)((uint32_t)(local_r15)), Arg4);
    v_stack_mD8 = 2;
    result = PopPromoteActionFlag(v_stack_m98, Arg4 + 1, (uint32_t)((uint32_t)(local_r15)), Arg4);
    v_stack_mD8 = 0x10000000ULL;
    result = PopPromoteActionFlag(v_stack_m98, Arg4 + 4, (uint32_t)((uint32_t)(local_r15)), Arg4);
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m90))))) == 2) {
        result = *(uint64_t *)(v_rip + 0x7AE56F);
        Arg1 = *(uint32_t *)(result + 0x44);
        if (((uint32_t)(local_rsi)) < ((uint32_t)(Arg1))) { local_rsi = (uint32_t)(Arg1); }
        v_stack_m90 = (uint32_t)(local_rsi);
    }
    if (((uint32_t)(local_rsi)) >= = (*(uint32_t *)(v_rip + 0x7AD43E))) {
        *(uint32_t *)(v_rip + 0x7AD432) = (uint32_t)(local_rsi);
    }
    v_stack_mD8 = 4;
    result = PopPromoteActionFlag(v_stack_m98, 1, (uint32_t)((uint32_t)(local_r15)), 1);
    v_stack_mD8 = 0x80000000ULL;
    result = PopPromoteActionFlag(v_stack_m98, 5, (uint32_t)((uint32_t)(local_r15)), 1);
    v_stack_mD8 = 0x40000000ULL;
    Arg2 = 0;
    result = PopPromoteActionFlag(v_stack_m98, Arg2, (uint32_t)((uint32_t)(local_r15)), 1);
    v_stack_mD8 = 8;
    Arg2 = 0;
    result = PopPromoteActionFlag(v_stack_m98, Arg2, (uint32_t)((uint32_t)(local_r15)), 1);
    v_stack_mD8 = 32;
    Arg2 = 0;
    result = PopPromoteActionFlag(v_stack_m98, Arg2, (uint32_t)((uint32_t)(local_r15)), 1);
    result = PopCompareActions((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m90))))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x7AD3B0)))), (uint32_t)((uint32_t)(local_r15)), (uint32_t)(*(uint32_t *)(v_rip + 0x7AD3B0)));
    if (condition_is_less_or_equal) goto loc_0075EA8C;
    result = PopCompareActions((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m90))))), 3, (uint32_t)((uint32_t)(local_r15)), (uint32_t)(*(uint32_t *)(v_rip + 0x7AD3B0)));
    local_r15 = v_stack_m98;
    if (!(sign_flag)) {
        local_r15 = (uint8_t)((v_stack_m98) | (2));
    }
    result = PopCompareActions((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x7AD3B0)))), 8, (uint32_t)((uint32_t)(local_r15)), (uint32_t)(*(uint32_t *)(v_rip + 0x7AD3B0)));
    if ((uint32_t)(result) == 0) {
        local_r15 = (uint8_t)((local_r15) | (2));
    }
    *(uint32_t *)(v_rip + 0x7AD36B) = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m90))));
    local_r15 = (uint8_t)((local_r15) | (5));
    *(uint32_t *)(v_rip + 0x7AD368) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1)));
    v_stack_m98 = (uint8_t)(local_r15);
    result = (uint32_t)(*(uint32_t *)(arg1));
    if ((*(uint32_t *)(arg1)) == 0) {
        result = *(uint32_t *)(arg1 + 0x18);
        *(uint32_t *)(v_rip + 0x7AD35A) = (uint32_t)(result);
    }
    if (((*(uint32_t *)(arg1 + 0x4)) & (256)) != 0) goto loc_0075EA90;
    if (*(uint64_t *)(v_rip + 0x7AD34E) != 0) {
        Arg2 = 0x67696450ULL;
        result = ExFreePoolWithTag(*(uint64_t *)(v_rip + 0x7AD34E), Arg2, (uint32_t)((uint32_t)(local_r15)), (uint32_t)(*(uint32_t *)(v_rip + 0x7AD3B0)));
    }
    if (*(uint64_t *)(arg1 + 0x10) == 0) goto loc_0075EA90;
    Arg2 = 0;
    result = PoStoreDiagnosticContext(*(uint64_t *)(arg1 + 0x10), Arg2, v_stack_m78, (uint32_t)(*(uint32_t *)(v_rip + 0x7AD3B0)));
    result = ExAllocatePool2(256, v_stack_m78, (uint32_t)(0x67696450ULL), (uint32_t)(*(uint32_t *)(v_rip + 0x7AD3B0)));
    *(uint64_t *)(v_rip + 0x7AD308) = result;
    if (result == 0) goto loc_0075EA90;
    result = PoStoreDiagnosticContext(*(uint64_t *)(arg1 + 0x10), result, v_stack_m78, (uint32_t)(*(uint32_t *)(v_rip + 0x7AD3B0)));
    if (!sign_flag) goto loc_0075EA90;
    result = ExFreePoolWithTag(*(uint64_t *)(v_rip + 0x7AD2E8), (uint32_t)(0x67696450ULL), v_stack_m78, (uint32_t)(*(uint32_t *)(v_rip + 0x7AD3B0)));
    goto loc_0075EA90;
loc_0075EA8C:
loc_0075EA90:
    if ((*(uint32_t *)(v_rip + 0x7AD2AD)) == 3) {
        *(uint32_t *)(v_rip + 0x7AD2A1) = 2;
    }
    if ((uint8_t)(v_stack_m98) == 0) goto loc_0075EAD6;
    result = TtmIsEnabled(*(uint64_t *)(v_rip + 0x7AD2E8), (uint32_t)(0x67696450ULL), v_stack_m78, (uint32_t)(*(uint32_t *)(v_rip + 0x7AD3B0)));
    if ((uint8_t)(result) != 0) {
        *(uint8_t *)(v_rip + 0x7AE649) = 1;
    }
    v_stack_m97 = 1;
    if ((*(uint8_t *)(v_rip + 0x7AD282)) < 2) goto loc_0075EB00;
loc_0075EAD1:
    result = PopGetPolicyWorker(1, (uint32_t)(0x67696450ULL), v_stack_m78, (uint32_t)(*(uint32_t *)(v_rip + 0x7AD3B0)));
loc_0075EAD6:
loc_0075EADA:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)))) & (1)) != 0) goto loc_0075EB41;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x4))) | (1));
    *(uint32_t *)(arg1 + 0x4) = (uint32_t)(result);
    if (((uint32_t)(local_r14)) != 32) goto loc_0075EB1A;
    if ((uint32_t)((uint32_t)((uint32_t)(local_r14))) != 0) goto loc_0075EB33;
    local_r12 = (uint32_t)(((uint32_t)(Arg2)) | (16));
    goto loc_0075EB33;
loc_0075EB00:
    result = PopSetPowerActionState(1, (uint32_t)(0x67696450ULL), v_stack_m78, (uint32_t)(*(uint32_t *)(v_rip + 0x7AD3B0)));
    goto loc_0075EAD1;
loc_0075EB15:
    goto loc_0075EADA;
loc_0075EB1A:
    if (((uint32_t)(local_r14)) != 16) goto loc_0075EB39;
    result = 0;
    if (!(condition_is_not_equal)) {
        local_r12 = (uint32_t)((local_r12) | (16));
    }
loc_0075EB39:
    result = PopSetNotificationWork((uint32_t)((uint32_t)(local_r12)), (uint32_t)(0x67696450ULL), v_stack_m78, (uint32_t)(*(uint32_t *)(v_rip + 0x7AD3B0)));
loc_0075EB41:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)))) & (32)) == 0) goto loc_0075EB8C;
    if ((uint8_t)(v_stack_m97) == 0) goto loc_0075EB82;
    result = (*(uint64_t *)(arg1 + 0x8)) + (32);
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x7AE324))) != (v_rip + 8053525)) {
        Arg1 = 3;
    }
    *(uint64_t *)(result) = v_rip + 8053525;
    *(void **)(result + 0x8) = Arg1;
    *(uint64_t *)(arg1) = result;
    *(uint64_t *)(v_rip + 0x7AE2F8) = result;
    goto loc_0075EB8C;
loc_0075EB82:
    Arg2 = 0;
    result = PopCompleteAction(Arg1, Arg2, v_stack_m78, (uint32_t)(*(uint32_t *)(v_rip + 0x7AD3B0)));
loc_0075EB8C:
loc_0075EB90:
    v_stack_mA0 = (uint8_t)(v_stack_m96);
    v_stack_mA8 = (uint32_t)((uint32_t)(v_stack_m80));
    v_stack_mB0 = (uint32_t)((uint32_t)(v_stack_m84));
    v_stack_mB8 = (uint32_t)((uint32_t)(v_stack_m88));
    v_stack_mC0 = (uint32_t)((uint32_t)(Arg5));
    v_stack_mC8 = (uint32_t)((uint32_t)(v_stack_m90));
    v_stack_mD0 = (uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0x8)));
    v_stack_mD8 = (uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0x4)));
    result = PopDiagTraceExecutePowerAction((uint32_t)(*(uint32_t *)(arg1)), (uint32_t)(*(uint32_t *)(arg1 + 0x4)), (uint32_t)((uint32_t)(local_r12)), (uint32_t)(*(uint32_t *)(arg3)));
    Arg1 = (v_stack_m50) ^ (local_rsp);
    result = _security_check_cookie(Arg1, (uint32_t)(*(uint32_t *)(arg1 + 0x4)), (uint32_t)((uint32_t)(local_r12)), (uint32_t)(*(uint32_t *)(arg3)));
    local_rsp = (local_rsp) + (184);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x4` | `32` | `R` |
| `Arg1` | `+ 0x4` | `32` | `W` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x18` | `32` | `R` |
| `Arg3` | `+ 0x0` | `32` | `R` |
| `Arg3` | `+ 0x0` | `64` | `R` |
| `Arg3` | `+ 0x4` | `32` | `R` |
| `Arg3` | `+ 0x8` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0075E6B4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
