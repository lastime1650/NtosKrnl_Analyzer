# PopHandleNextState

- RVA: `0x00B77350`–`0x00B776F4` (길이 `932` bytes)
- VA: `0x0000000140B77350`
- 실행 섹션: `PAGELK`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A1170`
- 디코드: `241`개 명령, `932/932` bytes 표시
- 미해석 바이트: `2` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **29**; 고유 호출 대상: **25**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **11**

### Outgoing calls
- `0x00B773A3` → [KeResumeClockTimer](../../text/4F/KeResumeClockTimer_function_004F6408.md) (function, `0x004F6408`)
- `0x00B773AD` → [PpmResetPerfEngineForProcessor](../../text/44/PpmResetPerfEngineForProcessor_function_0044F7D0.md) (function, `0x0044F7D0`)
- `0x00B773D0` → [KiLowerIrqlProcessIrqlFlags](../../text/4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x00B77403` → [KiCheckVpBackingLongSpinWaitHypercall](../../text/30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00B7740E` → [HvlNotifyLongSpinWait](../../text/30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00B77437` → [KeSaveIptStateBeforeProcessorGoesOffline](../../text/4D/KeSaveIptStateBeforeProcessorGoesOffline_function_004D9D40.md) (function, `0x004D9D40`)
- `0x00B77464` → [KeSaveExtendedAndSupervisorState](../../text/4F/KeSaveExtendedAndSupervisorState_function_004FC74C.md) (function, `0x004FC74C`)
- `0x00B77475` → [KeSaveProcessorSpecificFeatures](../../text/4F/KeSaveProcessorSpecificFeatures_function_004FAFBC.md) (function, `0x004FAFBC`)
- `0x00B774C4` → [KiRemoveSystemWorkPriorityKick](../../text/26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x00B774EC` → [KdPowerTransition](../../text/4F/KdPowerTransition_function_004F9AC0.md) (function, `0x004F9AC0`)
- `0x00B77511` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00B7752D` → [KdPowerTransition](../../text/4F/KdPowerTransition_function_004F9AC0.md) (function, `0x004F9AC0`)
- `0x00B77538` → [PopSstDiagInitializeResumeTimer](PopSstDiagInitializeResumeTimer_function_00B776FC.md) (function, `0x00B776FC`)
- `0x00B77545` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x00B7756D` → [PopFxNotifySystemStateTransition](../../text/4B/PopFxNotifySystemStateTransition_function_004B230C.md) (function, `0x004B230C`)
- `0x00B77583` → [PopFxNotifySystemStateTransition](../../text/4B/PopFxNotifySystemStateTransition_function_004B230C.md) (function, `0x004B230C`)
- `0x00B775BF` → [KeForceAttachProcess](../../text/21/KeForceAttachProcess_function_00216650.md) (function, `0x00216650`)
- `0x00B775E7` → [PopRestoreHiberContext](PopRestoreHiberContext_function_00B777F0.md) (function, `0x00B777F0`)
- `0x00B77604` → [KeForceDetachProcess](../../text/3C/KeForceDetachProcess_function_003C7770.md) (function, `0x003C7770`)
- `0x00B7762E` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00B7763A` → [HvlEnlightenProcessor](../../text/4D/HvlEnlightenProcessor_function_004DCD9C.md) (function, `0x004DCD9C`)
- `0x00B77648` → [KeRestoreProcessorSpecificFeatures](../../text/4D/KeRestoreProcessorSpecificFeatures_function_004D4C90.md) (function, `0x004D4C90`)
- `0x00B77652` → [KeFlushCurrentTbImmediately](../../text/4B/KeFlushCurrentTbImmediately_function_004B7F20.md) (function, `0x004B7F20`)
- `0x00B77665` → [KeRestoreIptStateAfterProcessorComesOnline](../../text/4B/KeRestoreIptStateAfterProcessorComesOnline_function_004BE824.md) (function, `0x004BE824`)
- `0x00B7766F` → [PpmResetPerfEngineForProcessor](../../text/44/PpmResetPerfEngineForProcessor_function_0044F7D0.md) (function, `0x0044F7D0`)
- `0x00B77692` → [KeDisableInterrupts](../../text/21/KeDisableInterrupts_function_00217BE0.md) (function, `0x00217BE0`)
- `0x00B7769A` → [KeSuspendClockTimer](../../text/4C/KeSuspendClockTimer_function_004CAA60.md) (function, `0x004CAA60`)
- `0x00B776AA` → [KiRaiseIrqlProcessIrqlFlags](../../text/4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x00B776B5` → [KeRestoreExtendedAndSupervisorState](../../text/3D/KeRestoreExtendedAndSupervisorState_function_003D60D0.md) (function, `0x003D60D0`)

### Direct callers
- [PopInvokeStateHandlerTargetProcessor](PopInvokeStateHandlerTargetProcessor_function_00B77270.md) at `0x00B772BE`
- [PopIssueNextState](PopIssueNextState_function_00B772EC.md) at `0x00B77305`

### Static image references
- `0x00B77388` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x00B773BC` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x00B773F9` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x00B77420` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x00B774CB` → RVA `0x00F0CF0C` (`.data`; read)
- `0x00B7751F` → RVA `0x00F0C680` (`.data`; read)
- `0x00B7754A` → RVA `0x00F07770` (`.data`; read)
- `0x00B77551` → RVA `0x00F0C480` (`.data`; write)
- `0x00B77561` → RVA `0x00F0BD6C` (`.data`; read)
- `0x00B77596` → RVA `0x00FC6AB0` (`ALMOSTRO`; read)
- `0x00B775D3` → RVA `0x00F0C680` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **27**
  - `0x00B773A3` → [KeResumeClockTimer](../../text/4F/KeResumeClockTimer_function_004F6408.md) (`PAGELK` → `.text`)
  - `0x00B773AD` → [PpmResetPerfEngineForProcessor](../../text/44/PpmResetPerfEngineForProcessor_function_0044F7D0.md) (`PAGELK` → `.text`)
  - `0x00B773D0` → [KiLowerIrqlProcessIrqlFlags](../../text/4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (`PAGELK` → `.text`)
  - `0x00B77403` → [KiCheckVpBackingLongSpinWaitHypercall](../../text/30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (`PAGELK` → `.text`)
  - `0x00B7740E` → [HvlNotifyLongSpinWait](../../text/30/HvlNotifyLongSpinWait_function_0030F460.md) (`PAGELK` → `.text`)
  - `0x00B77437` → [KeSaveIptStateBeforeProcessorGoesOffline](../../text/4D/KeSaveIptStateBeforeProcessorGoesOffline_function_004D9D40.md) (`PAGELK` → `.text`)
  - `0x00B77464` → [KeSaveExtendedAndSupervisorState](../../text/4F/KeSaveExtendedAndSupervisorState_function_004FC74C.md) (`PAGELK` → `.text`)
  - `0x00B77475` → [KeSaveProcessorSpecificFeatures](../../text/4F/KeSaveProcessorSpecificFeatures_function_004FAFBC.md) (`PAGELK` → `.text`)
  - `0x00B774C4` → [KiRemoveSystemWorkPriorityKick](../../text/26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (`PAGELK` → `.text`)
  - `0x00B774EC` → [KdPowerTransition](../../text/4F/KdPowerTransition_function_004F9AC0.md) (`PAGELK` → `.text`)
  - `0x00B77511` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGELK` → `.text`)
  - `0x00B7752D` → [KdPowerTransition](../../text/4F/KdPowerTransition_function_004F9AC0.md) (`PAGELK` → `.text`)
  - `0x00B77545` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (`PAGELK` → `.text`)
  - `0x00B7756D` → [PopFxNotifySystemStateTransition](../../text/4B/PopFxNotifySystemStateTransition_function_004B230C.md) (`PAGELK` → `.text`)
  - `0x00B77583` → [PopFxNotifySystemStateTransition](../../text/4B/PopFxNotifySystemStateTransition_function_004B230C.md) (`PAGELK` → `.text`)
  - `0x00B775BF` → [KeForceAttachProcess](../../text/21/KeForceAttachProcess_function_00216650.md) (`PAGELK` → `.text`)
  - `0x00B77604` → [KeForceDetachProcess](../../text/3C/KeForceDetachProcess_function_003C7770.md) (`PAGELK` → `.text`)
  - `0x00B7762E` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGELK` → `.text`)
  - `0x00B7763A` → [HvlEnlightenProcessor](../../text/4D/HvlEnlightenProcessor_function_004DCD9C.md) (`PAGELK` → `.text`)
  - `0x00B77648` → [KeRestoreProcessorSpecificFeatures](../../text/4D/KeRestoreProcessorSpecificFeatures_function_004D4C90.md) (`PAGELK` → `.text`)
  - `0x00B77652` → [KeFlushCurrentTbImmediately](../../text/4B/KeFlushCurrentTbImmediately_function_004B7F20.md) (`PAGELK` → `.text`)
  - `0x00B77665` → [KeRestoreIptStateAfterProcessorComesOnline](../../text/4B/KeRestoreIptStateAfterProcessorComesOnline_function_004BE824.md) (`PAGELK` → `.text`)
  - `0x00B7766F` → [PpmResetPerfEngineForProcessor](../../text/44/PpmResetPerfEngineForProcessor_function_0044F7D0.md) (`PAGELK` → `.text`)
  - `0x00B77692` → [KeDisableInterrupts](../../text/21/KeDisableInterrupts_function_00217BE0.md) (`PAGELK` → `.text`)
  - `0x00B7769A` → [KeSuspendClockTimer](../../text/4C/KeSuspendClockTimer_function_004CAA60.md) (`PAGELK` → `.text`)
  - `0x00B776AA` → [KiRaiseIrqlProcessIrqlFlags](../../text/4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (`PAGELK` → `.text`)
  - `0x00B776B5` → [KeRestoreExtendedAndSupervisorState](../../text/3D/KeRestoreExtendedAndSupervisorState_function_003D60D0.md) (`PAGELK` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00B776BC` → [PopSstDiagInitializeResumeTimer + 0x37](PopSstDiagInitializeResumeTimer_function_00B776FC.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B77350  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00B77355  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
00B7735A  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
00B7735F  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00B77364  41 56                           push r14
00B77366  48 83 EC 30                     sub rsp, 0x30
00B7736A  65 48 8B 2C 25 20 00 00 00      mov rbp, qword ptr gs:[0x20]
00B77373  45 33 F6                        xor r14d, r14d
00B77376  8B 41 38                        mov eax, dword ptr [rcx + 0x38]
00B77379  48 8B FA                        mov rdi, rdx
00B7737C  48 8B F1                        mov rsi, rcx
00B7737F  41 8B DE                        mov ebx, r14d
00B77382  3B 02                           cmp eax, dword ptr [rdx]
00B77384  75 13                           jne 0x140b77399
00B77386  FF C3                           inc ebx
00B77388  85 1D 1E DF 44 00               test dword ptr [rip + 0x44df1e], ebx
00B7738E  74 69                           je 0x140b773f9
00B77390  F3 90                           pause
00B77392  8B 46 38                        mov eax, dword ptr [rsi + 0x38]
00B77395  3B 07                           cmp eax, dword ptr [rdi]
00B77397  74 ED                           je 0x140b77386
00B77399  8B 46 38                        mov eax, dword ptr [rsi + 0x38]
00B7739C  89 07                           mov dword ptr [rdi], eax
00B7739E  83 F8 0D                        cmp eax, 0xd
00B773A1  75 75                           jne 0x140b77418
00B773A3  E8 60 F0 97 FF                  call 0x1404f6408
00B773A8  33 D2                           xor edx, edx
00B773AA  48 8B CD                        mov rcx, rbp
00B773AD  E8 1E 84 8D FF                  call 0x14044f7d0
00B773B2  44 38 77 04                     cmp byte ptr [rdi + 4], r14b
00B773B6  0F 85 D3 00 00 00               jne 0x140b7748f
00B773BC  44 39 35 5D F9 44 00            cmp dword ptr [rip + 0x44f95d], r14d
00B773C3  0F B6 5F 07                     movzx ebx, byte ptr [rdi + 7]
00B773C7  74 0C                           je 0x140b773d5
00B773C9  44 0F 20 C1                     mov rcx, cr8
00B773CD  0F B6 D3                        movzx edx, bl
00B773D0  E8 C3 E2 97 FF                  call 0x1404f5698
00B773D5  44 0F 22 C3                     mov cr8, rbx
00B773D9  F0 FF 46 34                     lock inc dword ptr [rsi + 0x34]
00B773DD  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
00B773E2  48 8B 6C 24 48                  mov rbp, qword ptr [rsp + 0x48]
00B773E7  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
00B773EC  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
00B773F1  48 83 C4 30                     add rsp, 0x30
00B773F5  41 5E                           pop r14
00B773F7  C3                              ret
00B773F8  CC                              int3
00B773F9  8B 05 B9 F6 44 00               mov eax, dword ptr [rip + 0x44f6b9]
00B773FF  A8 40                           test al, 0x40
00B77401  74 8D                           je 0x140b77390
00B77403  E8 88 80 79 FF                  call 0x14030f490
00B77408  84 C0                           test al, al
00B7740A  74 84                           je 0x140b77390
00B7740C  8B CB                           mov ecx, ebx
00B7740E  E8 4D 80 79 FF                  call 0x14030f460
00B77413  E9 7A FF FF FF                  jmp 0x140b77392
00B77418  83 C0 FE                        add eax, -2
00B7741B  83 F8 0D                        cmp eax, 0xd
00B7741E  77 B9                           ja 0x140b773d9
00B77420  48 8D 0D D9 8B 48 FF            lea rcx, [rip - 0xb77427]
00B77427  8B 94 81 BC 76 B7 00            mov edx, dword ptr [rcx + rax*4 + 0xb776bc]
00B7742E  48 03 D1                        add rdx, rcx
00B77431  FF E2                           jmp rdx
00B77433  CC                              int3
00B77434  CC                              int3
00B77435  CC                              int3
00B77436  CC                              int3
00B77437  E8 04 29 96 FF                  call 0x1404d9d40
00B7743C  44 88 77 05                     mov byte ptr [rdi + 5], r14b
00B77440  48 B9 F0 05 00 00 80 F7 FF FF   movabs rcx, 0xfffff780000005f0
00B7744A  48 B8 D8 03 00 00 80 F7 FF FF   movabs rax, 0xfffff780000003d8
00B77454  48 8B 09                        mov rcx, qword ptr [rcx]
00B77457  48 0B 08                        or rcx, qword ptr [rax]
00B7745A  48 83 E1 FC                     and rcx, 0xfffffffffffffffc
00B7745E  74 11                           je 0x140b77471
00B77460  48 8D 57 08                     lea rdx, [rdi + 8]
00B77464  E8 E3 52 98 FF                  call 0x1404fc74c
00B77469  C1 E8 1F                        shr eax, 0x1f
00B7746C  34 01                           xor al, 1
00B7746E  88 47 05                        mov byte ptr [rdi + 5], al
00B77471  48 8D 4F 70                     lea rcx, [rdi + 0x70]
00B77475  E8 42 3B 98 FF                  call 0x1404fafbc
00B7747A  65 4C 8B 0C 25 18 00 00 00      mov r9, qword ptr gs:[0x18]
00B77483  4C 89 8F 80 00 00 00            mov qword ptr [rdi + 0x80], r9
00B7748A  E9 4A FF FF FF                  jmp 0x140b773d9
00B7748F  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
00B77498  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
00B7749F  4D 85 C0                        test r8, r8
00B774A2  75 06                           jne 0x140b774aa
00B774A4  FB                              sti
00B774A5  E9 12 FF FF FF                  jmp 0x140b773bc
00B774AA  41 0F 0D 08                     prefetchw byte ptr [r8]
00B774AE  41 8B 00                        mov eax, dword ptr [r8]
00B774B1  8B D0                           mov edx, eax
00B774B3  0F BA F2 15                     btr edx, 0x15
00B774B7  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
00B774BC  75 F3                           jne 0x140b774b1
00B774BE  0F BA E0 15                     bt eax, 0x15
00B774C2  73 E0                           jae 0x140b774a4
00B774C4  E8 07 BD 6E FF                  call 0x1402631d0
00B774C9  EB D9                           jmp 0x140b774a4
00B774CB  F7 05 37 5A 39 00 00 00 80 00   test dword ptr [rip + 0x395a37], 0x800000
00B774D5  0F 85 EE 00 00 00               jne 0x140b775c9
00B774DB  44 39 75 24                     cmp dword ptr [rbp + 0x24], r14d
00B774DF  75 10                           jne 0x140b774f1
00B774E1  4C 39 76 08                     cmp qword ptr [rsi + 8], r14
00B774E5  75 0A                           jne 0x140b774f1
00B774E7  B9 04 00 00 00                  mov ecx, 4
00B774EC  E8 CF 25 98 FF                  call 0x1404f9ac0
00B774F1  48 8B 0E                        mov rcx, qword ptr [rsi]
00B774F4  48 8D 56 3C                     lea rdx, [rsi + 0x3c]
00B774F8  44 8B 4E 30                     mov r9d, dword ptr [rsi + 0x30]
00B774FC  4C 8B 46 10                     mov r8, qword ptr [rsi + 0x10]
00B77500  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00B77505  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
00B77509  48 8B 49 10                     mov rcx, qword ptr [rcx + 0x10]
00B7750D  48 8B 56 08                     mov rdx, qword ptr [rsi + 8]
00B77511  E8 BA 35 B4 FF                  call 0x1406baad0
00B77516  83 7D 24 00                     cmp dword ptr [rbp + 0x24], 0
00B7751A  44 8B F0                        mov r14d, eax
00B7751D  75 39                           jne 0x140b77558
00B7751F  80 3D 5A 51 39 00 00            cmp byte ptr [rip + 0x39515a], 0
00B77526  75 0A                           jne 0x140b77532
00B77528  B9 01 00 00 00                  mov ecx, 1
00B7752D  E8 8E 25 98 FF                  call 0x1404f9ac0
00B77532  83 7D 24 00                     cmp dword ptr [rbp + 0x24], 0
00B77536  75 20                           jne 0x140b77558
00B77538  E8 BF 01 00 00                  call 0x140b776fc
00B7753D  83 7D 24 00                     cmp dword ptr [rbp + 0x24], 0
00B77541  75 15                           jne 0x140b77558
00B77543  33 C9                           xor ecx, ecx
00B77545  E8 96 72 80 FF                  call 0x14037e7e0
00B7754A  48 2B 05 1F 02 39 00            sub rax, qword ptr [rip + 0x39021f]
00B77551  48 89 05 28 4F 39 00            mov qword ptr [rip + 0x394f28], rax
00B77558  44 89 77 78                     mov dword ptr [rdi + 0x78], r14d
00B7755C  E9 78 FE FF FF                  jmp 0x140b773d9
00B77561  44 8B 05 04 48 39 00            mov r8d, dword ptr [rip + 0x394804]
00B77568  33 D2                           xor edx, edx
00B7756A  48 8B CD                        mov rcx, rbp
00B7756D  E8 9A AD 93 FF                  call 0x1404b230c
00B77572  E9 62 FE FF FF                  jmp 0x140b773d9
00B77577  44 8B 05 EE 47 39 00            mov r8d, dword ptr [rip + 0x3947ee]
00B7757E  B2 01                           mov dl, 1
00B77580  48 8B CD                        mov rcx, rbp
00B77583  E8 84 AD 93 FF                  call 0x1404b230c
00B77588  E9 4C FE FF FF                  jmp 0x140b773d9
00B7758D  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00B77596  48 8B 05 13 F5 44 00            mov rax, qword ptr [rip + 0x44f513]
00B7759D  48 39 81 B8 00 00 00            cmp qword ptr [rcx + 0xb8], rax
00B775A4  0F 84 2F FE FF FF               je 0x140b773d9
00B775AA  C6 47 06 01                     mov byte ptr [rdi + 6], 1
00B775AE  48 8D 57 40                     lea rdx, [rdi + 0x40]
00B775B2  48 8B 0D F7 F4 44 00            mov rcx, qword ptr [rip + 0x44f4f7]
00B775B9  41 B8 01 00 00 00               mov r8d, 1
00B775BF  E8 8C F0 69 FF                  call 0x140216650
00B775C4  E9 10 FE FF FF                  jmp 0x140b773d9
00B775C9  4C 39 76 08                     cmp qword ptr [rsi + 8], r14
00B775CD  0F 84 08 FF FF FF               je 0x140b774db
00B775D3  C6 05 A6 50 39 00 01            mov byte ptr [rip + 0x3950a6], 1
00B775DA  44 89 77 78                     mov dword ptr [rdi + 0x78], r14d
00B775DE  E9 F6 FD FF FF                  jmp 0x140b773d9
00B775E3  48 8B 4E 18                     mov rcx, qword ptr [rsi + 0x18]
00B775E7  E8 04 02 00 00                  call 0x140b777f0
00B775EC  E9 E8 FD FF FF                  jmp 0x140b773d9
00B775F1  44 38 77 06                     cmp byte ptr [rdi + 6], r14b
00B775F5  0F 84 DE FD FF FF               je 0x140b773d9
00B775FB  48 8D 4F 40                     lea rcx, [rdi + 0x40]
00B775FF  BA 01 00 00 00                  mov edx, 1
00B77604  E8 67 01 85 FF                  call 0x1403c7770
00B77609  44 88 77 06                     mov byte ptr [rdi + 6], r14b
00B7760D  E9 C7 FD FF FF                  jmp 0x140b773d9
00B77612  48 8B 56 20                     mov rdx, qword ptr [rsi + 0x20]
00B77616  48 8B 02                        mov rax, qword ptr [rdx]
00B77619  48 85 C0                        test rax, rax
00B7761C  0F 84 B7 FD FF FF               je 0x140b773d9
00B77622  44 0F B6 46 2C                  movzx r8d, byte ptr [rsi + 0x2c]
00B77627  48 8B 52 08                     mov rdx, qword ptr [rdx + 8]
00B7762B  8B 4E 28                        mov ecx, dword ptr [rsi + 0x28]
00B7762E  E8 9D 34 B4 FF                  call 0x1406baad0
00B77633  E9 A1 FD FF FF                  jmp 0x140b773d9
00B77638  B1 01                           mov cl, 1
00B7763A  E8 5D 57 96 FF                  call 0x1404dcd9c
00B7763F  E9 95 FD FF FF                  jmp 0x140b773d9
00B77644  48 8D 4F 70                     lea rcx, [rdi + 0x70]
00B77648  E8 43 D6 95 FF                  call 0x1404d4c90
00B7764D  E9 87 FD FF FF                  jmp 0x140b773d9
00B77652  E8 C9 08 94 FF                  call 0x1404b7f20
00B77657  90                              nop
00B77658  0F 09                           wbinvd
00B7765A  E9 7A FD FF FF                  jmp 0x140b773d9
00B7765F  44 38 77 05                     cmp byte ptr [rdi + 5], r14b
00B77663  75 4C                           jne 0x140b776b1
00B77665  E8 BA 71 94 FF                  call 0x1404be824
00B7766A  B2 01                           mov dl, 1
00B7766C  48 8B CD                        mov rcx, rbp
00B7766F  E8 5C 81 8D FF                  call 0x14044f7d0
00B77674  E9 60 FD FF FF                  jmp 0x140b773d9
00B77679  44 0F 20 C3                     mov rbx, cr8
00B7767D  B8 0F 00 00 00                  mov eax, 0xf
00B77682  44 0F 22 C0                     mov cr8, rax
00B77686  44 39 35 93 F6 44 00            cmp dword ptr [rip + 0x44f693], r14d
00B7768D  75 15                           jne 0x140b776a4
00B7768F  88 5F 07                        mov byte ptr [rdi + 7], bl
00B77692  E8 49 05 6A FF                  call 0x140217be0
00B77697  88 47 04                        mov byte ptr [rdi + 4], al
00B7769A  E8 C1 33 95 FF                  call 0x1404caa60
00B7769F  E9 35 FD FF FF                  jmp 0x140b773d9
00B776A4  0F B6 D0                        movzx edx, al
00B776A7  0F B6 CB                        movzx ecx, bl
00B776AA  E8 4D E0 97 FF                  call 0x1404f56fc
00B776AF  EB DE                           jmp 0x140b7768f
00B776B1  48 8D 4F 08                     lea rcx, [rdi + 8]
00B776B5  E8 16 EA 85 FF                  call 0x1403d60d0
00B776BA  EB A9                           jmp 0x140b77665
00B776BC  77 75                           ja 0x140b77733
00B776BE  B7 00                           mov bh, 0
00B776C0  37                              .byte 0x37
00B776C1  74 B7                           je 0x140b7767a
00B776C3  00 79 76                        add byte ptr [rcx + 0x76], bh
00B776C6  B7 00                           mov bh, 0
00B776C8  8D 75 B7                        lea esi, [rbp - 0x49]
00B776CB  00 CB                           add bl, cl
00B776CD  74 B7                           je 0x140b77686
00B776CF  00 38                           add byte ptr [rax], bh
00B776D1  76 B7                           jbe 0x140b7768a
00B776D3  00 44 76 B7                     add byte ptr [rsi + rsi*2 - 0x49], al
00B776D7  00 E3                           add bl, ah
00B776D9  75 B7                           jne 0x140b77692
00B776DB  00 52 76                        add byte ptr [rdx + 0x76], dl
00B776DE  B7 00                           mov bh, 0
00B776E0  F1                              int1
00B776E1  75 B7                           jne 0x140b7769a
00B776E3  00 12                           add byte ptr [rdx], dl
00B776E5  76 B7                           jbe 0x140b7769e
00B776E7  00 D9                           add cl, bl
00B776E9  73 B7                           jae 0x140b776a2
00B776EB  00 61 75                        add byte ptr [rcx + 0x75], ah
00B776EE  B7 00                           mov bh, 0
00B776F0  5F                              pop rdi
00B776F1  76 B7                           jbe 0x140b776aa
00B776F3  00                              .byte 0x00
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopHandleNextState(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_stack_p20 = v_rdi;
    v_rsp = (v_rsp) - (48);
    v_r14 = 0;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 56)))) != (*(unsigned int *)(a2))) goto loc_00B77399;
loc_00B77386:
    v_rbx = (unsigned int)((0) + 1);
    if (((*(unsigned int *)(v_rip + 4513566)) & ((unsigned int)(v_rbx))) == 0) goto loc_00B773F9;
loc_00B77390:
loc_00B77392:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 56)))) == (*(unsigned int *)(a2))) goto loc_00B77386;
loc_00B77399:
    *(unsigned int *)(a2) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 56)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 56)))) != 13) goto loc_00B77418;
    result = KeResumeClockTimer(a1, a2, a3, a4);
    a2 = 0;
    result = PpmResetPerfEngineForProcessor(*(unsigned __int64 *)(gs_base + (0 + 32)), a2, a3, a4);
    if ((*(unsigned __int8 *)(a2 + 4)) != 0) goto loc_00B7748F;
loc_00B773BC:
    if ((*(unsigned int *)(v_rip + 4520285)) != 0) {
        a1 = v_cr8;
        a2 = (unsigned __int8)(*(unsigned __int8 *)(a2 + 7));
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, a3, a4);
    }
loc_00B773D9:
    v_rsp = (v_rsp) + (48);
    return result;
loc_00B773F9:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 4519609)))) & (64)) == 0) goto loc_00B77390;
    result = KiCheckVpBackingLongSpinWaitHypercall(a1, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00B77390;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_stack_p8)), a2, a3, a4);
    goto loc_00B77392;
loc_00B77418:
    result = (unsigned int)((result) + (-2));
    if (((unsigned int)(result)) > 13) goto loc_00B773D9;
    a2 = ((unsigned int)(*(unsigned int *)(v_rip - 12022823 + result * 4 + 12023484))) + (v_rip - 12022823);
loc_00B7748F:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) != 0) goto loc_00B774AA;
loc_00B774A4:
    goto loc_00B773BC;
loc_00B774AA:
loc_00B774B1:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) != 0) goto loc_00B774B1;
    if (condition_is_above_or_equal) goto loc_00B774A4;
    result = KiRemoveSystemWorkPriorityKick(*(unsigned __int64 *)(gs_base + (0 + 32)), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536))))), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), a4);
    goto loc_00B774A4;
}
```

## 5. (Beta) C Style

```c
int64_t PopHandleNextState(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    v_stack_p20 = local_rdi;
    local_rsp = (local_rsp) - (48);
    local_r14 = 0;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x38)))) != (*(uint32_t *)(arg2))) goto loc_00B77399;
loc_00B77386:
    local_rbx = (uint32_t)((0) + 1);
    if (((*(uint32_t *)(v_rip + 0x44DF1E)) & ((uint32_t)(local_rbx))) == 0) goto loc_00B773F9;
loc_00B77390:
loc_00B77392:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x38)))) == (*(uint32_t *)(arg2))) goto loc_00B77386;
loc_00B77399:
    *(uint32_t *)(arg2) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x38)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x38)))) != 13) goto loc_00B77418;
    result = KeResumeClockTimer(Arg1, Arg2, a3, a4);
    Arg2 = 0;
    result = PpmResetPerfEngineForProcessor(*(uint64_t *)(gs_base + (0 + 0x20)), Arg2, a3, a4);
    if ((*(uint8_t *)(arg2 + 0x4)) != 0) goto loc_00B7748F;
loc_00B773BC:
    if ((*(uint32_t *)(v_rip + 0x44F95D)) != 0) {
        Arg1 = v_cr8;
        Arg2 = (uint8_t)(*(uint8_t *)(arg2 + 0x7));
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, a3, a4);
    }
loc_00B773D9:
    local_rsp = (local_rsp) + (48);
    return result;
loc_00B773F9:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x44F6B9)))) & (64)) == 0) goto loc_00B77390;
    result = KiCheckVpBackingLongSpinWaitHypercall(Arg1, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00B77390;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(v_stack_p8)), Arg2, a3, a4);
    goto loc_00B77392;
loc_00B77418:
    result = (uint32_t)((result) + (-2));
    if (((uint32_t)(result)) > 13) goto loc_00B773D9;
    Arg2 = ((uint32_t)(*(uint32_t *)(v_rip - 0xB77427 + result * 4 + 0xB776BC))) + (v_rip - 12022823);
loc_00B7748F:
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) != 0) goto loc_00B774AA;
loc_00B774A4:
    goto loc_00B773BC;
loc_00B774AA:
loc_00B774B1:
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) != 0) goto loc_00B774B1;
    if (condition_is_above_or_equal) goto loc_00B774A4;
    result = KiRemoveSystemWorkPriorityKick(*(uint64_t *)(gs_base + (0 + 0x20)), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8))))), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), a4);
    goto loc_00B774A4;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x34` | `32` | `R/W` |
| `Arg1` | `+ 0x38` | `32` | `R` |
| `Arg2` | `+ 0x0` | `32` | `R` |
| `Arg2` | `+ 0x0` | `32` | `W` |
| `Arg2` | `+ 0x4` | `8` | `R` |
| `Arg2` | `+ 0x7` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagelk&rva=0x00B77350&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
