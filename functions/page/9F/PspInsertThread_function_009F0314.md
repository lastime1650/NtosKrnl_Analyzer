# PspInsertThread

- RVA: `0x009F0314`–`0x009F0CF7` (길이 `2,531` bytes)
- VA: `0x00000001409F0314`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A5D38`
- 디코드: `619`개 명령, `2,531/2,531` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **63**; 고유 호출 대상: **43**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x009F039E` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x009F03B9` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x009F0407` → [KeQueryMaximumGroupCount](../../text/48/KeQueryMaximumGroupCount_function_0048B760.md) (function, `0x0048B760`)
- `0x009F0422` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x009F043F` → [KeQueryMaximumGroupCount](../../text/48/KeQueryMaximumGroupCount_function_0048B760.md) (function, `0x0048B760`)
- `0x009F0463` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x009F0479` → [KeAddGroupAffinityEx](../../text/25/KeAddGroupAffinityEx_function_0025B6C0.md) (function, `0x0025B6C0`)
- `0x009F04E0` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x009F04F8` → [PspCheckForJobAffinityViolation](../A7/PspCheckForJobAffinityViolation_function_00A79648.md) (function, `0x00A79648`)
- `0x009F0582` → [PspCreateSecureThread](../A8/PspCreateSecureThread_function_00A89160.md) (function, `0x00A89160`)
- `0x009F059E` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x009F05BF` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x009F05C7` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x009F05E3` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x009F05EB` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x009F05F3` → [KeUninitThread](../A2/KeUninitThread_function_00A25D2C.md) (function, `0x00A25D2C`)
- `0x009F0615` → [MmDeleteTeb](../87/MmDeleteTeb_function_0087FAC0.md) (function, `0x0087FAC0`)
- `0x009F062D` → [PspDeleteUserStack](../A7/PspDeleteUserStack_function_00A78D18.md) (function, `0x00A78D18`)
- `0x009F063C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x009F0669` → [KeStartThread](../../text/3C/KeStartThread_function_003C21B8.md) (function, `0x003C21B8`)
- `0x009F0677` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x009F06B0` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x009F077A` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x009F0794` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x009F07E4` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x009F07EC` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x009F0828` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x009F0830` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x009F0845` → [Feature_ProcesDirectSwap__private_IsEnabledDeviceUsageNoInline](../../text/5E/Feature_ProcesDirectSwap__private_IsEnabledDeviceUsageNoInline_function_005E3264.md) (function, `0x005E3264`)
- `0x009F0851` → [PspChangeProcessExecutionState](../AE/PspChangeProcessExecutionState_function_00AEC594.md) (function, `0x00AEC594`)
- `0x009F0858` → [PspChangeProcessExecutionStateLegacy](../../text/5E/PspChangeProcessExecutionStateLegacy_function_005E4098.md) (function, `0x005E4098`)
- `0x009F086B` → [ObReferenceObjectExWithTag](../../text/41/ObReferenceObjectExWithTag_function_0041FDB0.md) (function, `0x0041FDB0`)
- `0x009F0880` → [Feature_SuspendThread2__private_IsEnabledNoReportingNoInline](../../text/5C/Feature_SuspendThread2__private_IsEnabledNoReportingNoInline_function_005C357C.md) (function, `0x005C357C`)
- `0x009F0891` → [KeSuspendThread](../../text/4E/KeSuspendThread_function_004E8B9C.md) (function, `0x004E8B9C`)
- `0x009F089B` → [KeSuspendThreadOld](../../text/5B/KeSuspendThreadOld_function_005B9000.md) (function, `0x005B9000`)
- `0x009F08E3` → [KeForceResumeThread](../../text/20/KeForceResumeThread_function_0020292C.md) (function, `0x0020292C`)
- `0x009F08F7` → [KeEnableCoreIsolationMitigationPolicyThread](../../text/5C/KeEnableCoreIsolationMitigationPolicyThread_function_005C35B4.md) (function, `0x005C35B4`)
- `0x009F0902` → [PspRecheckThreadOptionalXStateFeatures](../A2/PspRecheckThreadOptionalXStateFeatures_function_00A2B4B0.md) (function, `0x00A2B4B0`)
- `0x009F0914` → [PspRecheckThreadPasidMsrState](../A5/PspRecheckThreadPasidMsrState_function_00A5EA5C.md) (function, `0x00A5EA5C`)
- `0x009F097E` → [SeCreateAccessStateEx](../94/SeCreateAccessStateEx_function_00947A80.md) (function, `0x00947A80`)
- `0x009F09B9` → [ObInsertObjectEx](../8B/ObInsertObjectEx_function_008B97A0.md) (function, `0x008B97A0`)
- `0x009F09C8` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x009F0A50` → [SeDeleteAccessState](../8C/SeDeleteAccessState_function_008C5F70.md) (function, `0x008C5F70`)
- `0x009F0A5A` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x009F0A84` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x009F0A90` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x009F0AA4` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x009F0AB0` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x009F0AC7` → [KeForceResumeThread](../../text/20/KeForceResumeThread_function_0020292C.md) (function, `0x0020292C`)
- `0x009F0AEC` → [PspDeleteUserStack](../A7/PspDeleteUserStack_function_00A78D18.md) (function, `0x00A78D18`)
- `0x009F0B0C` → [EtwTraceProcess](../8A/EtwTraceProcess_function_008A4004.md) (function, `0x008A4004`)
- `0x009F0B1D` → [PoEnergyContextStart](../98/PoEnergyContextStart_function_0098EAD4.md) (function, `0x0098EAD4`)
- `0x009F0B45` → [PspCallProcessNotifyRoutines](../90/PspCallProcessNotifyRoutines_function_00904928.md) (function, `0x00904928`)
- `0x009F0B65` → [EtwTraceThread](../90/EtwTraceThread_function_00905700.md) (function, `0x00905700`)
- `0x009F0B88` → [PspCallThreadNotifyRoutines](../90/PspCallThreadNotifyRoutines_function_00905530.md) (function, `0x00905530`)
- `0x009F0BAF` → [PspCreateObjectHandle](../A1/PspCreateObjectHandle_function_00A1E51C.md) (function, `0x00A1E51C`)
- `0x009F0BC7` → [SeDeleteAccessState](../8C/SeDeleteAccessState_function_008C5F70.md) (function, `0x008C5F70`)
- `0x009F0BFD` → [PspAssignProcessToJobList](../A2/PspAssignProcessToJobList_function_00A22F14.md) (function, `0x00A22F14`)
- `0x009F0C6E` → [ObCloseHandle](../8A/ObCloseHandle_function_008A1870.md) (function, `0x008A1870`)
- `0x009F0C88` → [KeRaiseUserException](../../text/4D/KeRaiseUserException_function_004D7750.md) (function, `0x004D7750`)
- `0x009F0CBA` → [KeRequestTerminationThread](../../text/48/KeRequestTerminationThread_function_00489A58.md) (function, `0x00489A58`)
- `0x009F0CD3` → [KeForceResumeThread](../../text/20/KeForceResumeThread_function_0020292C.md) (function, `0x0020292C`)
- `0x009F0CDB` → [KeReadyThread](../../text/39/KeReadyThread_function_00398AB4.md) (function, `0x00398AB4`)

### Direct callers
- [PspCreateThread](../9E/PspCreateThread_function_009EF034.md) at `0x009EF319`
- [PspCreatePicoThread](PspCreatePicoThread_function_009F0D70.md) at `0x009F10DE`
- [NtCreateUserProcess](../AE/NtCreateUserProcess_function_00AEA680.md) at `0x00AEB648`

### Static image references
- `0x009F0957` → RVA `0x00FC6AC8` (`ALMOSTRO`; read)
- `0x009F0AF9` → RVA `0x00FC6B00` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **42**
  - `0x009F039E` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x009F03B9` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x009F0407` → [KeQueryMaximumGroupCount](../../text/48/KeQueryMaximumGroupCount_function_0048B760.md) (`PAGE` → `.text`)
  - `0x009F0422` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x009F043F` → [KeQueryMaximumGroupCount](../../text/48/KeQueryMaximumGroupCount_function_0048B760.md) (`PAGE` → `.text`)
  - `0x009F0463` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x009F0479` → [KeAddGroupAffinityEx](../../text/25/KeAddGroupAffinityEx_function_0025B6C0.md) (`PAGE` → `.text`)
  - `0x009F04E0` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x009F059E` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x009F05BF` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x009F05C7` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x009F05E3` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x009F05EB` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x009F063C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x009F0669` → [KeStartThread](../../text/3C/KeStartThread_function_003C21B8.md) (`PAGE` → `.text`)
  - `0x009F0677` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x009F06B0` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x009F077A` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x009F0794` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x009F07E4` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x009F07EC` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x009F0828` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x009F0830` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x009F0845` → [Feature_ProcesDirectSwap__private_IsEnabledDeviceUsageNoInline](../../text/5E/Feature_ProcesDirectSwap__private_IsEnabledDeviceUsageNoInline_function_005E3264.md) (`PAGE` → `.text`)
  - `0x009F0858` → [PspChangeProcessExecutionStateLegacy](../../text/5E/PspChangeProcessExecutionStateLegacy_function_005E4098.md) (`PAGE` → `.text`)
  - `0x009F086B` → [ObReferenceObjectExWithTag](../../text/41/ObReferenceObjectExWithTag_function_0041FDB0.md) (`PAGE` → `.text`)
  - `0x009F0880` → [Feature_SuspendThread2__private_IsEnabledNoReportingNoInline](../../text/5C/Feature_SuspendThread2__private_IsEnabledNoReportingNoInline_function_005C357C.md) (`PAGE` → `.text`)
  - `0x009F0891` → [KeSuspendThread](../../text/4E/KeSuspendThread_function_004E8B9C.md) (`PAGE` → `.text`)
  - `0x009F089B` → [KeSuspendThreadOld](../../text/5B/KeSuspendThreadOld_function_005B9000.md) (`PAGE` → `.text`)
  - `0x009F08E3` → [KeForceResumeThread](../../text/20/KeForceResumeThread_function_0020292C.md) (`PAGE` → `.text`)
  - `0x009F08F7` → [KeEnableCoreIsolationMitigationPolicyThread](../../text/5C/KeEnableCoreIsolationMitigationPolicyThread_function_005C35B4.md) (`PAGE` → `.text`)
  - `0x009F09C8` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x009F0A5A` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x009F0A84` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x009F0A90` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x009F0AA4` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x009F0AB0` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x009F0AC7` → [KeForceResumeThread](../../text/20/KeForceResumeThread_function_0020292C.md) (`PAGE` → `.text`)
  - `0x009F0C88` → [KeRaiseUserException](../../text/4D/KeRaiseUserException_function_004D7750.md) (`PAGE` → `.text`)
  - `0x009F0CBA` → [KeRequestTerminationThread](../../text/48/KeRequestTerminationThread_function_00489A58.md) (`PAGE` → `.text`)
  - `0x009F0CD3` → [KeForceResumeThread](../../text/20/KeForceResumeThread_function_0020292C.md) (`PAGE` → `.text`)
  - `0x009F0CDB` → [KeReadyThread](../../text/39/KeReadyThread_function_00398AB4.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009F0314  48 8B C4                        mov rax, rsp
009F0317  4C 89 48 20                     mov qword ptr [rax + 0x20], r9
009F031B  4C 89 40 18                     mov qword ptr [rax + 0x18], r8
009F031F  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
009F0323  48 89 48 08                     mov qword ptr [rax + 8], rcx
009F0327  53                              push rbx
009F0328  56                              push rsi
009F0329  57                              push rdi
009F032A  41 54                           push r12
009F032C  41 55                           push r13
009F032E  41 56                           push r14
009F0330  41 57                           push r15
009F0332  48 81 EC A0 00 00 00            sub rsp, 0xa0
009F0339  4D 8B D1                        mov r10, r9
009F033C  4C 8B F2                        mov r14, rdx
009F033F  4C 8B F9                        mov r15, rcx
009F0342  48 8B 94 24 10 01 00 00         mov rdx, qword ptr [rsp + 0x110]
009F034A  48 89 94 24 88 00 00 00         mov qword ptr [rsp + 0x88], rdx
009F0352  33 F6                           xor esi, esi
009F0354  8B FE                           mov edi, esi
009F0356  89 74 24 40                     mov dword ptr [rsp + 0x40], esi
009F035A  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
009F0363  4C 8B 88 B8 00 00 00            mov r9, qword ptr [rax + 0xb8]
009F036A  4C 89 4C 24 68                  mov qword ptr [rsp + 0x68], r9
009F036F  48 8B 81 F0 00 00 00            mov rax, qword ptr [rcx + 0xf0]
009F0376  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
009F037B  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
009F0380  48 89 74 24 48                  mov qword ptr [rsp + 0x48], rsi
009F0385  44 8B E6                        mov r12d, esi
009F0388  41 8B 02                        mov eax, dword ptr [r10]
009F038B  A8 20                           test al, 0x20
009F038D  75 45                           jne 0x1409f03d4
009F038F  49 8D 9E C8 01 00 00            lea rbx, [r14 + 0x1c8]
009F0396  45 33 C0                        xor r8d, r8d
009F0399  33 D2                           xor edx, edx
009F039B  48 8B CB                        mov rcx, rbx
009F039E  E8 8D FE 81 FF                  call 0x140210230
009F03A3  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
009F03A8  F0 48 0F BA 2B 00               lock bts qword ptr [rbx], 0
009F03AE  73 13                           jae 0x1409f03c3
009F03B0  4C 8B C3                        mov r8, rbx
009F03B3  48 8B D0                        mov rdx, rax
009F03B6  48 8B CB                        mov rcx, rbx
009F03B9  E8 D2 F8 81 FF                  call 0x14020fc90
009F03BE  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
009F03C3  48 85 C0                        test rax, rax
009F03C6  74 0C                           je 0x1409f03d4
009F03C8  41 BD 01 00 00 00               mov r13d, 1
009F03CE  44 88 68 0A                     mov byte ptr [rax + 0xa], r13b
009F03D2  EB 06                           jmp 0x1409f03da
009F03D4  41 BD 01 00 00 00               mov r13d, 1
009F03DA  48 8B 9C 24 10 01 00 00         mov rbx, qword ptr [rsp + 0x110]
009F03E2  48 85 DB                        test rbx, rbx
009F03E5  0F 84 CB 00 00 00               je 0x1409f04b6
009F03EB  48 8B 53 20                     mov rdx, qword ptr [rbx + 0x20]
009F03EF  48 89 54 24 58                  mov qword ptr [rsp + 0x58], rdx
009F03F4  48 89 54 24 50                  mov qword ptr [rsp + 0x50], rdx
009F03F9  8B 43 08                        mov eax, dword ptr [rbx + 8]
009F03FC  48 0F BA E0 0C                  bt rax, 0xc
009F0401  0F 83 92 00 00 00               jae 0x1409f0499
009F0407  E8 54 B3 A9 FF                  call 0x14048b760
009F040C  0F B7 D0                        movzx edx, ax
009F040F  48 8D 14 D5 08 00 00 00         lea rdx, [rdx*8 + 8]
009F0417  B9 40 00 00 00                  mov ecx, 0x40
009F041C  41 B8 50 73 20 20               mov r8d, 0x20207350
009F0422  E8 C9 1C 19 00                  call 0x140b820f0
009F0427  4C 8B E0                        mov r12, rax
009F042A  48 85 C0                        test rax, rax
009F042D  75 10                           jne 0x1409f043f
009F042F  C7 44 24 44 9A 00 00 C0         mov dword ptr [rsp + 0x44], 0xc000009a
009F0437  48 8B DE                        mov rbx, rsi
009F043A  E9 56 01 00 00                  jmp 0x1409f0595
009F043F  E8 1C B3 A9 FF                  call 0x14048b760
009F0444  66 45 89 2C 24                  mov word ptr [r12], r13w
009F0449  66 41 89 44 24 02               mov word ptr [r12 + 2], ax
009F044F  41 89 74 24 04                  mov dword ptr [r12 + 4], esi
009F0454  44 0F B7 C0                     movzx r8d, ax
009F0458  49 C1 E0 03                     shl r8, 3
009F045C  49 8D 4C 24 08                  lea rcx, [r12 + 8]
009F0461  33 D2                           xor edx, edx
009F0463  E8 D8 67 CD FF                  call 0x1406c6c40
009F0468  4C 8B 83 40 01 00 00            mov r8, qword ptr [rbx + 0x140]
009F046F  0F B7 93 48 01 00 00            movzx edx, word ptr [rbx + 0x148]
009F0476  49 8B CC                        mov rcx, r12
009F0479  E8 42 B2 86 FF                  call 0x14025b6c0
009F047E  0F B7 83 48 01 00 00            movzx eax, word ptr [rbx + 0x148]
009F0485  66 41 39 86 A0 01 00 00         cmp word ptr [r14 + 0x1a0], ax
009F048D  74 0A                           je 0x1409f0499
009F048F  F0 41 0F BA AE 88 00 00 00 0C   lock bts dword ptr [r14 + 0x88], 0xc
009F0499  8B 4B 08                        mov ecx, dword ptr [rbx + 8]
009F049C  81 E1 00 40 00 00               and ecx, 0x4000
009F04A2  48 8D 43 14                     lea rax, [rbx + 0x14]
009F04A6  48 F7 D9                        neg rcx
009F04A9  48 1B C9                        sbb rcx, rcx
009F04AC  48 23 C8                        and rcx, rax
009F04AF  48 89 4C 24 48                  mov qword ptr [rsp + 0x48], rcx
009F04B4  EB 0D                           jmp 0x1409f04c3
009F04B6  48 8B C6                        mov rax, rsi
009F04B9  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
009F04BE  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
009F04C3  49 8B 9E A0 02 00 00            mov rbx, qword ptr [r14 + 0x2a0]
009F04CA  48 85 DB                        test rbx, rbx
009F04CD  74 3C                           je 0x1409f050b
009F04CF  41 F7 47 74 00 04 00 00         test dword ptr [r15 + 0x74], 0x400
009F04D7  75 32                           jne 0x1409f050b
009F04D9  48 8D 4B 38                     lea rcx, [rbx + 0x38]
009F04DD  41 8A D5                        mov dl, r13b
009F04E0  E8 DB 16 82 FF                  call 0x140211bc0
009F04E5  41 8B FD                        mov edi, r13d
009F04E8  44 89 6C 24 40                  mov dword ptr [rsp + 0x40], r13d
009F04ED  4D 85 E4                        test r12, r12
009F04F0  74 19                           je 0x1409f050b
009F04F2  49 8B D4                        mov rdx, r12
009F04F5  48 8B CB                        mov rcx, rbx
009F04F8  E8 4B 91 08 00                  call 0x140a79648
009F04FD  B9 05 00 00 00                  mov ecx, 5
009F0502  85 C0                           test eax, eax
009F0504  0F 48 F9                        cmovs edi, ecx
009F0507  89 7C 24 40                     mov dword ptr [rsp + 0x40], edi
009F050B  83 FF 04                        cmp edi, 4
009F050E  73 41                           jae 0x1409f0551
009F0510  41 8B 8E F4 01 00 00            mov ecx, dword ptr [r14 + 0x1f4]
009F0517  8B C1                           mov eax, ecx
009F0519  25 08 00 00 04                  and eax, 0x4000008
009F051E  3D 00 00 00 04                  cmp eax, 0x4000000
009F0523  75 2C                           jne 0x1409f0551
009F0525  0F BA E1 1E                     bt ecx, 0x1e
009F0529  73 1A                           jae 0x1409f0545
009F052B  41 F7 47 74 00 04 00 00         test dword ptr [r15 + 0x74], 0x400
009F0533  75 10                           jne 0x1409f0545
009F0535  48 8B 94 24 F8 00 00 00         mov rdx, qword ptr [rsp + 0xf8]
009F053D  8B 02                           mov eax, dword ptr [rdx]
009F053F  A8 02                           test al, 2
009F0541  74 16                           je 0x1409f0559
009F0543  EB 08                           jmp 0x1409f054d
009F0545  48 8B 94 24 F8 00 00 00         mov rdx, qword ptr [rsp + 0xf8]
009F054D  8B CE                           mov ecx, esi
009F054F  EB 0D                           jmp 0x1409f055e
009F0551  48 8B 94 24 F8 00 00 00         mov rdx, qword ptr [rsp + 0xf8]
009F0559  B9 01 00 00 C0                  mov ecx, 0xc0000001
009F055E  89 4C 24 44                     mov dword ptr [rsp + 0x44], ecx
009F0562  85 C9                           test ecx, ecx
009F0564  78 2F                           js 0x1409f0595
009F0566  45 84 AE 70 01 00 00            test byte ptr [r14 + 0x170], r13b
009F056D  74 1E                           je 0x1409f058d
009F056F  F7 02 00 04 00 00               test dword ptr [rdx], 0x400
009F0575  74 16                           je 0x1409f058d
009F0577  48 8B 94 24 18 01 00 00         mov rdx, qword ptr [rsp + 0x118]
009F057F  49 8B CF                        mov rcx, r15
009F0582  E8 D9 8B 09 00                  call 0x140a89160
009F0587  8B C8                           mov ecx, eax
009F0589  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
009F058D  85 C9                           test ecx, ecx
009F058F  0F 89 C9 00 00 00               jns 0x1409f065e
009F0595  41 84 FD                        test r13b, dil
009F0598  74 09                           je 0x1409f05a3
009F059A  48 8D 4B 38                     lea rcx, [rbx + 0x38]
009F059E  E8 6D F4 86 FF                  call 0x14025fa10
009F05A3  49 8D BE C8 01 00 00            lea rdi, [r14 + 0x1c8]
009F05AA  48 83 CB FF                     or rbx, 0xffffffffffffffff
009F05AE  48 8B C3                        mov rax, rbx
009F05B1  F0 48 0F C1 07                  lock xadd qword ptr [rdi], rax
009F05B6  24 06                           and al, 6
009F05B8  3C 02                           cmp al, 2
009F05BA  75 08                           jne 0x1409f05c4
009F05BC  48 8B CF                        mov rcx, rdi
009F05BF  E8 0C 58 87 FF                  call 0x140265dd0
009F05C4  48 8B CF                        mov rcx, rdi
009F05C7  E8 34 10 8F FF                  call 0x1402e1600
009F05CC  49 8D BF 90 05 00 00            lea rdi, [r15 + 0x590]
009F05D3  F0 48 0F C1 1F                  lock xadd qword ptr [rdi], rbx
009F05D8  80 E3 06                        and bl, 6
009F05DB  80 FB 02                        cmp bl, 2
009F05DE  75 08                           jne 0x1409f05e8
009F05E0  48 8B CF                        mov rcx, rdi
009F05E3  E8 E8 57 87 FF                  call 0x140265dd0
009F05E8  48 8B CF                        mov rcx, rdi
009F05EB  E8 10 10 8F FF                  call 0x1402e1600
009F05F0  49 8B CF                        mov rcx, r15
009F05F3  E8 34 57 03 00                  call 0x140a25d2c
009F05F8  48 8B 9C 24 08 01 00 00         mov rbx, qword ptr [rsp + 0x108]
009F0600  48 85 DB                        test rbx, rbx
009F0603  74 2D                           je 0x1409f0632
009F0605  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
009F060A  48 85 C9                        test rcx, rcx
009F060D  74 0B                           je 0x1409f061a
009F060F  48 8B D1                        mov rdx, rcx
009F0612  49 8B CE                        mov rcx, r14
009F0615  E8 A6 F4 E8 FF                  call 0x14087fac0
009F061A  40 38 33                        cmp byte ptr [rbx], sil
009F061D  74 13                           je 0x1409f0632
009F061F  4C 8B CB                        mov r9, rbx
009F0622  4C 8B 84 24 F0 00 00 00         mov r8, qword ptr [rsp + 0xf0]
009F062A  49 8B CE                        mov rcx, r14
009F062D  E8 E6 86 08 00                  call 0x140a78d18
009F0632  4D 85 E4                        test r12, r12
009F0635  74 0A                           je 0x1409f0641
009F0637  33 D2                           xor edx, edx
009F0639  49 8B CC                        mov rcx, r12
009F063C  E8 2F 22 19 00                  call 0x140b82870
009F0641  41 8B 86 F4 01 00 00            mov eax, dword ptr [r14 + 0x1f4]
009F0648  A9 08 00 00 40                  test eax, 0x40000008
009F064D  B9 0A 01 00 C0                  mov ecx, 0xc000010a
009F0652  8B 44 24 44                     mov eax, dword ptr [rsp + 0x44]
009F0656  0F 45 C1                        cmovne eax, ecx
009F0659  E9 85 06 00 00                  jmp 0x1409f0ce3
009F065E  4C 8B 44 24 48                  mov r8, qword ptr [rsp + 0x48]
009F0663  49 8B D4                        mov rdx, r12
009F0666  49 8B CF                        mov rcx, r15
009F0669  E8 4A 1B 9D FF                  call 0x1403c21b8
009F066E  41 84 FD                        test r13b, dil
009F0671  74 10                           je 0x1409f0683
009F0673  48 8D 4B 38                     lea rcx, [rbx + 0x38]
009F0677  E8 94 F3 86 FF                  call 0x14025fa10
009F067C  83 E7 FE                        and edi, 0xfffffffe
009F067F  89 7C 24 40                     mov dword ptr [rsp + 0x40], edi
009F0683  41 F7 86 F4 01 00 00 00 00 00 40  test dword ptr [r14 + 0x1f4], 0x40000000
009F068E  74 16                           je 0x1409f06a6
009F0690  48 8B 8C 24 F8 00 00 00         mov rcx, qword ptr [rsp + 0xf8]
009F0698  8B 01                           mov eax, dword ptr [rcx]
009F069A  A8 02                           test al, 2
009F069C  74 08                           je 0x1409f06a6
009F069E  41 83 8F A4 05 00 00 40         or dword ptr [r15 + 0x5a4], 0x40
009F06A6  4D 85 E4                        test r12, r12
009F06A9  74 0A                           je 0x1409f06b5
009F06AB  33 D2                           xor edx, edx
009F06AD  49 8B CC                        mov rcx, r12
009F06B0  E8 BB 21 19 00                  call 0x140b82870
009F06B5  49 8D 97 A0 05 00 00            lea rdx, [r15 + 0x5a0]
009F06BC  48 89 54 24 48                  mov qword ptr [rsp + 0x48], rdx
009F06C1  48 89 94 24 80 00 00 00         mov qword ptr [rsp + 0x80], rdx
009F06C9  8B 02                           mov eax, dword ptr [rdx]
009F06CB  41 8B 8E F4 01 00 00            mov ecx, dword ptr [r14 + 0x1f4]
009F06D2  C1 E9 12                        shr ecx, 0x12
009F06D5  33 C8                           xor ecx, eax
009F06D7  81 E1 00 0E 00 00               and ecx, 0xe00
009F06DD  33 C8                           xor ecx, eax
009F06DF  89 0A                           mov dword ptr [rdx], ecx
009F06E1  8B C1                           mov eax, ecx
009F06E3  41 33 86 F0 01 00 00            xor eax, dword ptr [r14 + 0x1f0]
009F06EA  25 00 70 00 00                  and eax, 0x7000
009F06EF  33 C1                           xor eax, ecx
009F06F1  89 02                           mov dword ptr [rdx], eax
009F06F3  41 8B 86 80 03 00 00            mov eax, dword ptr [r14 + 0x380]
009F06FA  41 03 C5                        add eax, r13d
009F06FD  41 89 86 80 03 00 00            mov dword ptr [r14 + 0x380], eax
009F0704  41 8B 86 80 03 00 00            mov eax, dword ptr [r14 + 0x380]
009F070B  41 3B 86 D8 05 00 00            cmp eax, dword ptr [r14 + 0x5d8]
009F0712  76 0E                           jbe 0x1409f0722
009F0714  41 8B 86 80 03 00 00            mov eax, dword ptr [r14 + 0x380]
009F071B  41 89 86 D8 05 00 00            mov dword ptr [r14 + 0x5d8], eax
009F0722  F0 41 0F BA AE DC 07 00 00 00   lock bts dword ptr [r14 + 0x7dc], 0
009F072C  0F 92 C1                        setb cl
009F072F  41 8B 86 80 03 00 00            mov eax, dword ptr [r14 + 0x380]
009F0736  41 3B C5                        cmp eax, r13d
009F0739  75 0D                           jne 0x1409f0748
009F073B  84 C9                           test cl, cl
009F073D  75 09                           jne 0x1409f0748
009F073F  83 CF 02                        or edi, 2
009F0742  89 7C 24 40                     mov dword ptr [rsp + 0x40], edi
009F0746  EB 23                           jmp 0x1409f076b
009F0748  41 8B 86 80 03 00 00            mov eax, dword ptr [r14 + 0x380]
009F074F  83 F8 02                        cmp eax, 2
009F0752  75 17                           jne 0x1409f076b
009F0754  41 F7 86 F0 01 00 00 00 80 00 00  test dword ptr [r14 + 0x1f0], 0x8000
009F075F  75 0A                           jne 0x1409f076b
009F0761  F0 41 0F BA AE F0 01 00 00 0F   lock bts dword ptr [r14 + 0x1f0], 0xf
009F076B  4D 8D A6 E0 05 00 00            lea r12, [r14 + 0x5e0]
009F0772  45 33 C0                        xor r8d, r8d
009F0775  33 D2                           xor edx, edx
009F0777  49 8B CC                        mov rcx, r12
009F077A  E8 B1 FA 81 FF                  call 0x140210230
009F077F  48 8B D8                        mov rbx, rax
009F0782  F0 49 0F BA 2C 24 00            lock bts qword ptr [r12], 0
009F0789  73 0E                           jae 0x1409f0799
009F078B  4D 8B C4                        mov r8, r12
009F078E  48 8B D0                        mov rdx, rax
009F0791  49 8B CC                        mov rcx, r12
009F0794  E8 F7 F4 81 FF                  call 0x14020fc90
009F0799  48 85 DB                        test rbx, rbx
009F079C  74 04                           je 0x1409f07a2
009F079E  44 88 6B 0A                     mov byte ptr [rbx + 0xa], r13b
009F07A2  49 8D 8F 78 05 00 00            lea rcx, [r15 + 0x578]
009F07A9  49 8D 86 70 03 00 00            lea rax, [r14 + 0x370]
009F07B0  48 8B 50 08                     mov rdx, qword ptr [rax + 8]
009F07B4  48 39 02                        cmp qword ptr [rdx], rax
009F07B7  74 07                           je 0x1409f07c0
009F07B9  B9 03 00 00 00                  mov ecx, 3
009F07BE  CD 29                           int 0x29
009F07C0  48 89 01                        mov qword ptr [rcx], rax
009F07C3  48 89 51 08                     mov qword ptr [rcx + 8], rdx
009F07C7  48 89 0A                        mov qword ptr [rdx], rcx
009F07CA  48 89 48 08                     mov qword ptr [rax + 8], rcx
009F07CE  48 83 CB FF                     or rbx, 0xffffffffffffffff
009F07D2  48 8B C3                        mov rax, rbx
009F07D5  F0 49 0F C1 04 24               lock xadd qword ptr [r12], rax
009F07DB  24 06                           and al, 6
009F07DD  3C 02                           cmp al, 2
009F07DF  75 08                           jne 0x1409f07e9
009F07E1  49 8B CC                        mov rcx, r12
009F07E4  E8 E7 55 87 FF                  call 0x140265dd0
009F07E9  49 8B CC                        mov rcx, r12
009F07EC  E8 0F 0E 8F FF                  call 0x1402e1600
009F07F1  49 39 B6 68 01 00 00            cmp qword ptr [r14 + 0x168], rsi
009F07F8  74 06                           je 0x1409f0800
009F07FA  F0 41 0F BA 2F 19               lock bts dword ptr [r15], 0x19
009F0800  49 39 B6 B8 07 00 00            cmp qword ptr [r14 + 0x7b8], rsi
009F0807  74 06                           je 0x1409f080f
009F0809  F0 41 0F BA 2F 1D               lock bts dword ptr [r15], 0x1d
009F080F  4D 8D A6 C8 01 00 00            lea r12, [r14 + 0x1c8]
009F0816  48 8B C3                        mov rax, rbx
009F0819  F0 49 0F C1 04 24               lock xadd qword ptr [r12], rax
009F081F  24 06                           and al, 6
009F0821  3C 02                           cmp al, 2
009F0823  75 08                           jne 0x1409f082d
009F0825  49 8B CC                        mov rcx, r12
009F0828  E8 A3 55 87 FF                  call 0x140265dd0
009F082D  49 8B CC                        mov rcx, r12
009F0830  E8 CB 0D 8F FF                  call 0x1402e1600
009F0835  4C 8B A4 24 F8 00 00 00         mov r12, qword ptr [rsp + 0xf8]
009F083D  41 8B 04 24                     mov eax, dword ptr [r12]
009F0841  A8 40                           test al, 0x40
009F0843  74 18                           je 0x1409f085d
009F0845  E8 1A 2A BF FF                  call 0x1405e3264
009F084A  49 8B CE                        mov rcx, r14
009F084D  85 C0                           test eax, eax
009F084F  74 07                           je 0x1409f0858
009F0851  E8 3E BD 0F 00                  call 0x140aec594
009F0856  EB 05                           jmp 0x1409f085d
009F0858  E8 3B 38 BF FF                  call 0x1405e4098
009F085D  BA 02 00 00 00                  mov edx, 2
009F0862  41 B8 44 66 6C 74               mov r8d, 0x746c6644
009F0868  49 8B CF                        mov rcx, r15
009F086B  E8 40 F5 A2 FF                  call 0x14041fdb0
009F0870  45 89 AF EC 05 00 00            mov dword ptr [r15 + 0x5ec], r13d
009F0877  41 8B 04 24                     mov eax, dword ptr [r12]
009F087B  41 84 C5                        test r13b, al
009F087E  74 68                           je 0x1409f08e8
009F0880  E8 F7 2C BD FF                  call 0x1405c357c
009F0885  85 C0                           test eax, eax
009F0887  74 0F                           je 0x1409f0898
009F0889  45 33 C0                        xor r8d, r8d
009F088C  33 D2                           xor edx, edx
009F088E  49 8B CF                        mov rcx, r15
009F0891  E8 06 83 AF FF                  call 0x1404e8b9c
009F0896  EB 3C                           jmp 0x1409f08d4
009F0898  49 8B CF                        mov rcx, r15
009F089B  E8 60 87 BC FF                  call 0x1405b9000
009F08A0  EB 32                           jmp 0x1409f08d4
009F08A2  33 F6                           xor esi, esi
009F08A4  44 8D 6E 01                     lea r13d, [rsi + 1]
009F08A8  48 83 CB FF                     or rbx, 0xffffffffffffffff
009F08AC  4C 8B B4 24 E8 00 00 00         mov r14, qword ptr [rsp + 0xe8]
009F08B4  4C 8B BC 24 E0 00 00 00         mov r15, qword ptr [rsp + 0xe0]
009F08BC  8B 7C 24 40                     mov edi, dword ptr [rsp + 0x40]
009F08C0  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
009F08C5  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
009F08CA  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
009F08CF  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
009F08D4  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
009F08D9  8B 00                           mov eax, dword ptr [rax]
009F08DB  41 84 C5                        test r13b, al
009F08DE  74 08                           je 0x1409f08e8
009F08E0  49 8B CF                        mov rcx, r15
009F08E3  E8 44 20 81 FF                  call 0x14020292c
009F08E8  41 8B 86 D8 07 00 00            mov eax, dword ptr [r14 + 0x7d8]
009F08EF  41 84 C5                        test r13b, al
009F08F2  74 08                           je 0x1409f08fc
009F08F4  49 8B CF                        mov rcx, r15
009F08F7  E8 B8 2C BD FF                  call 0x1405c35b4
009F08FC  49 8B D7                        mov rdx, r15
009F08FF  49 8B CE                        mov rcx, r14
009F0902  E8 A9 AB 03 00                  call 0x140a2b4b0
009F0907  44 8B E0                        mov r12d, eax
009F090A  85 C0                           test eax, eax
009F090C  78 0E                           js 0x1409f091c
009F090E  49 8B D7                        mov rdx, r15
009F0911  49 8B CE                        mov rcx, r14
009F0914  E8 43 E1 06 00                  call 0x140a5ea5c
009F0919  44 8B E0                        mov r12d, eax
009F091C  89 74 24 44                     mov dword ptr [rsp + 0x44], esi
009F0920  48 8B 8C 24 20 01 00 00         mov rcx, qword ptr [rsp + 0x120]
009F0928  40 38 B1 84 01 00 00            cmp byte ptr [rcx + 0x184], sil
009F092F  74 15                           je 0x1409f0946
009F0931  48 8B 84 24 F8 00 00 00         mov rax, qword ptr [rsp + 0xf8]
009F0939  8B 00                           mov eax, dword ptr [rax]
009F093B  A8 10                           test al, 0x10
009F093D  75 07                           jne 0x1409f0946
009F093F  48 8B 54 24 68                  mov rdx, qword ptr [rsp + 0x68]
009F0944  EB 08                           jmp 0x1409f094e
009F0946  49 8B D6                        mov rdx, r14
009F0949  44 89 6C 24 44                  mov dword ptr [rsp + 0x44], r13d
009F094E  45 85 E4                        test r12d, r12d
009F0951  0F 88 00 01 00 00               js 0x1409f0a57
009F0957  48 8B 05 6A 61 5D 00            mov rax, qword ptr [rip + 0x5d616a]
009F095E  48 83 C0 4C                     add rax, 0x4c
009F0962  4C 8D 89 A0 00 00 00            lea r9, [rcx + 0xa0]
009F0969  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009F096E  8B 84 24 00 01 00 00            mov eax, dword ptr [rsp + 0x100]
009F0975  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
009F0979  4C 8B C1                        mov r8, rcx
009F097C  33 C9                           xor ecx, ecx
009F097E  E8 FD 70 F5 FF                  call 0x140947a80
009F0983  44 8B E0                        mov r12d, eax
009F0986  48 8B 8C 24 20 01 00 00         mov rcx, qword ptr [rsp + 0x120]
009F098E  85 C0                           test eax, eax
009F0990  0F 88 C1 00 00 00               js 0x1409f0a57
009F0996  48 89 74 24 30                  mov qword ptr [rsp + 0x30], rsi
009F099B  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
009F09A0  8B 44 24 44                     mov eax, dword ptr [rsp + 0x44]
009F09A4  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
009F09A8  45 33 C9                        xor r9d, r9d
009F09AB  44 8B 84 24 00 01 00 00         mov r8d, dword ptr [rsp + 0x100]
009F09B3  48 8B D1                        mov rdx, rcx
009F09B6  49 8B CF                        mov rcx, r15
009F09B9  E8 E2 8D EC FF                  call 0x1408b97a0
009F09BE  44 8B E0                        mov r12d, eax
009F09C1  85 C0                           test eax, eax
009F09C3  78 7E                           js 0x1409f0a43
009F09C5  49 8B CF                        mov rcx, r15
009F09C8  E8 83 89 90 FF                  call 0x1402f9350
009F09CD  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
009F09D2  48 85 C0                        test rax, rax
009F09D5  74 2B                           je 0x1409f0a02
009F09D7  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
009F09DC  48 89 08                        mov qword ptr [rax], rcx
009F09DF  EB 21                           jmp 0x1409f0a02
009F09E1  44 8B E0                        mov r12d, eax
009F09E4  33 F6                           xor esi, esi
009F09E6  44 8D 6E 01                     lea r13d, [rsi + 1]
009F09EA  48 83 CB FF                     or rbx, 0xffffffffffffffff
009F09EE  4C 8B B4 24 E8 00 00 00         mov r14, qword ptr [rsp + 0xe8]
009F09F6  4C 8B BC 24 E0 00 00 00         mov r15, qword ptr [rsp + 0xe0]
009F09FE  8B 7C 24 40                     mov edi, dword ptr [rsp + 0x40]
009F0A02  45 85 E4                        test r12d, r12d
009F0A05  78 41                           js 0x1409f0a48
009F0A07  48 8B 84 24 30 01 00 00         mov rax, qword ptr [rsp + 0x130]
009F0A0F  48 85 C0                        test rax, rax
009F0A12  74 2F                           je 0x1409f0a43
009F0A14  41 0F 10 87 08 05 00 00         movups xmm0, xmmword ptr [r15 + 0x508]
009F0A1C  F3 0F 7F 00                     movdqu xmmword ptr [rax], xmm0
009F0A20  EB 21                           jmp 0x1409f0a43
009F0A22  44 8B E0                        mov r12d, eax
009F0A25  33 F6                           xor esi, esi
009F0A27  44 8D 6E 01                     lea r13d, [rsi + 1]
009F0A2B  48 83 CB FF                     or rbx, 0xffffffffffffffff
009F0A2F  4C 8B B4 24 E8 00 00 00         mov r14, qword ptr [rsp + 0xe8]
009F0A37  4C 8B BC 24 E0 00 00 00         mov r15, qword ptr [rsp + 0xe0]
009F0A3F  8B 7C 24 40                     mov edi, dword ptr [rsp + 0x40]
009F0A43  45 85 E4                        test r12d, r12d
009F0A46  79 17                           jns 0x1409f0a5f
009F0A48  48 8B 8C 24 20 01 00 00         mov rcx, qword ptr [rsp + 0x120]
009F0A50  E8 1B 55 ED FF                  call 0x1408c5f70
009F0A55  EB 08                           jmp 0x1409f0a5f
009F0A57  49 8B CF                        mov rcx, r15
009F0A5A  E8 F1 88 90 FF                  call 0x1402f9350
009F0A5F  49 8D 8F 90 05 00 00            lea rcx, [r15 + 0x590]
009F0A66  45 85 E4                        test r12d, r12d
009F0A69  78 2C                           js 0x1409f0a97
009F0A6B  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
009F0A73  F0 83 08 02                     lock or dword ptr [rax], 2
009F0A77  F0 48 0F C1 19                  lock xadd qword ptr [rcx], rbx
009F0A7C  80 E3 06                        and bl, 6
009F0A7F  80 FB 02                        cmp bl, 2
009F0A82  75 0C                           jne 0x1409f0a90
009F0A84  E8 47 53 87 FF                  call 0x140265dd0
009F0A89  49 8D 8F 90 05 00 00            lea rcx, [r15 + 0x590]
009F0A90  E8 6B 0B 8F FF                  call 0x1402e1600
009F0A95  EB 5A                           jmp 0x1409f0af1
009F0A97  F0 48 0F C1 19                  lock xadd qword ptr [rcx], rbx
009F0A9C  80 E3 06                        and bl, 6
009F0A9F  80 FB 02                        cmp bl, 2
009F0AA2  75 0C                           jne 0x1409f0ab0
009F0AA4  E8 27 53 87 FF                  call 0x140265dd0
009F0AA9  49 8D 8F 90 05 00 00            lea rcx, [r15 + 0x590]
009F0AB0  E8 4B 0B 8F FF                  call 0x1402e1600
009F0AB5  48 8B 8C 24 F8 00 00 00         mov rcx, qword ptr [rsp + 0xf8]
009F0ABD  8B 01                           mov eax, dword ptr [rcx]
009F0ABF  41 84 C5                        test r13b, al
009F0AC2  74 08                           je 0x1409f0acc
009F0AC4  49 8B CF                        mov rcx, r15
009F0AC7  E8 60 1E 81 FF                  call 0x14020292c
009F0ACC  48 8B 84 24 08 01 00 00         mov rax, qword ptr [rsp + 0x108]
009F0AD4  48 85 C0                        test rax, rax
009F0AD7  74 18                           je 0x1409f0af1
009F0AD9  40 38 30                        cmp byte ptr [rax], sil
009F0ADC  74 13                           je 0x1409f0af1
009F0ADE  4C 8B C8                        mov r9, rax
009F0AE1  4C 8B 84 24 F0 00 00 00         mov r8, qword ptr [rsp + 0xf0]
009F0AE9  49 8B CE                        mov rcx, r14
009F0AEC  E8 27 82 08 00                  call 0x140a78d18
009F0AF1  8B DE                           mov ebx, esi
009F0AF3  40 F6 C7 02                     test dil, 2
009F0AF7  74 53                           je 0x1409f0b4c
009F0AF9  8B 05 01 60 5D 00               mov eax, dword ptr [rip + 0x5d6001]
009F0AFF  41 84 C5                        test r13b, al
009F0B02  74 0D                           je 0x1409f0b11
009F0B04  BA 01 03 00 00                  mov edx, 0x301
009F0B09  49 8B CE                        mov rcx, r14
009F0B0C  E8 F3 34 EB FF                  call 0x1408a4004
009F0B11  49 39 B6 68 06 00 00            cmp qword ptr [r14 + 0x668], rsi
009F0B18  74 08                           je 0x1409f0b22
009F0B1A  49 8B CE                        mov rcx, r14
009F0B1D  E8 B2 DF F9 FF                  call 0x14098ead4
009F0B22  41 8B 86 FC 05 00 00            mov eax, dword ptr [r14 + 0x5fc]
009F0B29  41 84 C5                        test r13b, al
009F0B2C  74 09                           je 0x1409f0b37
009F0B2E  49 39 B6 40 06 00 00            cmp qword ptr [r14 + 0x640], rsi
009F0B35  74 15                           je 0x1409f0b4c
009F0B37  45 8A C5                        mov r8b, r13b
009F0B3A  48 8B 94 24 10 01 00 00         mov rdx, qword ptr [rsp + 0x110]
009F0B42  49 8B CE                        mov rcx, r14
009F0B45  E8 DE 3D F1 FF                  call 0x140904928
009F0B4A  8B D8                           mov ebx, eax
009F0B4C  8B 0D AE 5F 5D 00               mov ecx, dword ptr [rip + 0x5d5fae]
009F0B52  F6 C1 02                        test cl, 2
009F0B55  74 13                           je 0x1409f0b6a
009F0B57  45 8A C5                        mov r8b, r13b
009F0B5A  48 8B 94 24 F0 00 00 00         mov rdx, qword ptr [rsp + 0xf0]
009F0B62  49 8B CF                        mov rcx, r15
009F0B65  E8 96 4B F1 FF                  call 0x140905700
009F0B6A  41 8B 8E FC 05 00 00            mov ecx, dword ptr [r14 + 0x5fc]
009F0B71  41 84 CD                        test r13b, cl
009F0B74  74 09                           je 0x1409f0b7f
009F0B76  49 39 B6 40 06 00 00            cmp qword ptr [r14 + 0x640], rsi
009F0B7D  74 0E                           je 0x1409f0b8d
009F0B7F  45 33 C0                        xor r8d, r8d
009F0B82  41 8A D5                        mov dl, r13b
009F0B85  49 8B CF                        mov rcx, r15
009F0B88  E8 A3 49 F1 FF                  call 0x140905530
009F0B8D  45 85 E4                        test r12d, r12d
009F0B90  0F 88 42 01 00 00               js 0x1409f0cd8
009F0B96  85 DB                           test ebx, ebx
009F0B98  78 1F                           js 0x1409f0bb9
009F0B9A  4C 8B 05 27 5F 5D 00            mov r8, qword ptr [rip + 0x5d5f27]
009F0BA1  48 8B 9C 24 20 01 00 00         mov rbx, qword ptr [rsp + 0x120]
009F0BA9  48 8B D3                        mov rdx, rbx
009F0BAC  49 8B CF                        mov rcx, r15
009F0BAF  E8 68 D9 02 00                  call 0x140a1e51c
009F0BB4  44 8B E0                        mov r12d, eax
009F0BB7  EB 0B                           jmp 0x1409f0bc4
009F0BB9  44 8B E3                        mov r12d, ebx
009F0BBC  48 8B 9C 24 20 01 00 00         mov rbx, qword ptr [rsp + 0x120]
009F0BC4  48 8B CB                        mov rcx, rbx
009F0BC7  E8 A4 53 ED FF                  call 0x1408c5f70
009F0BCC  45 85 E4                        test r12d, r12d
009F0BCF  0F 88 BD 00 00 00               js 0x1409f0c92
009F0BD5  48 39 B4 24 88 00 00 00         cmp qword ptr [rsp + 0x88], rsi
009F0BDD  74 26                           je 0x1409f0c05
009F0BDF  48 8B 84 24 10 01 00 00         mov rax, qword ptr [rsp + 0x110]
009F0BE7  48 8B 90 70 01 00 00            mov rdx, qword ptr [rax + 0x170]
009F0BEE  48 85 D2                        test rdx, rdx
009F0BF1  74 12                           je 0x1409f0c05
009F0BF3  44 8B 80 7C 01 00 00            mov r8d, dword ptr [rax + 0x17c]
009F0BFA  49 8B CE                        mov rcx, r14
009F0BFD  E8 12 23 03 00                  call 0x140a22f14
009F0C02  44 8B E0                        mov r12d, eax
009F0C05  45 85 E4                        test r12d, r12d
009F0C08  78 3A                           js 0x1409f0c44
009F0C0A  48 8B 8B 88 01 00 00            mov rcx, qword ptr [rbx + 0x188]
009F0C11  48 8B 84 24 28 01 00 00         mov rax, qword ptr [rsp + 0x128]
009F0C19  48 89 08                        mov qword ptr [rax], rcx
009F0C1C  EB 1D                           jmp 0x1409f0c3b
009F0C1E  44 8B E0                        mov r12d, eax
009F0C21  33 F6                           xor esi, esi
009F0C23  44 8D 6E 01                     lea r13d, [rsi + 1]
009F0C27  4C 8B BC 24 E0 00 00 00         mov r15, qword ptr [rsp + 0xe0]
009F0C2F  8B 7C 24 40                     mov edi, dword ptr [rsp + 0x40]
009F0C33  48 8B 9C 24 20 01 00 00         mov rbx, qword ptr [rsp + 0x120]
009F0C3B  45 85 E4                        test r12d, r12d
009F0C3E  0F 89 94 00 00 00               jns 0x1409f0cd8
009F0C44  F7 83 80 01 00 00 00 02 00 00   test dword ptr [rbx + 0x180], 0x200
009F0C4E  75 14                           jne 0x1409f0c64
009F0C50  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
009F0C55  F7 80 FC 05 00 00 00 10 00 00   test dword ptr [rax + 0x5fc], 0x1000
009F0C5F  41 8A D5                        mov dl, r13b
009F0C62  74 03                           je 0x1409f0c67
009F0C64  40 8A D6                        mov dl, sil
009F0C67  48 8B 8B 88 01 00 00            mov rcx, qword ptr [rbx + 0x188]
009F0C6E  E8 FD 0B EB FF                  call 0x1408a1870
009F0C73  48 8B 84 24 08 01 00 00         mov rax, qword ptr [rsp + 0x108]
009F0C7B  48 85 C0                        test rax, rax
009F0C7E  74 0D                           je 0x1409f0c8d
009F0C80  44 84 28                        test byte ptr [rax], r13b
009F0C83  74 08                           je 0x1409f0c8d
009F0C85  41 8B CC                        mov ecx, r12d
009F0C88  E8 C3 6A AE FF                  call 0x1404d7750
009F0C8D  45 85 E4                        test r12d, r12d
009F0C90  79 46                           jns 0x1409f0cd8
009F0C92  F0 41 0F BA AF A0 05 00 00 00   lock bts dword ptr [r15 + 0x5a0], 0
009F0C9C  72 03                           jb 0x1409f0ca1
009F0C9E  83 CF 08                        or edi, 8
009F0CA1  41 F7 47 74 00 04 00 00         test dword ptr [r15 + 0x74], 0x400
009F0CA9  75 16                           jne 0x1409f0cc1
009F0CAB  83 FF 08                        cmp edi, 8
009F0CAE  72 07                           jb 0x1409f0cb7
009F0CB0  45 89 A7 D8 05 00 00            mov dword ptr [r15 + 0x5d8], r12d
009F0CB7  49 8B CF                        mov rcx, r15
009F0CBA  E8 99 8D A9 FF                  call 0x140489a58
009F0CBF  EB 17                           jmp 0x1409f0cd8
009F0CC1  48 8B 84 24 F8 00 00 00         mov rax, qword ptr [rsp + 0xf8]
009F0CC9  8B 00                           mov eax, dword ptr [rax]
009F0CCB  41 84 C5                        test r13b, al
009F0CCE  74 08                           je 0x1409f0cd8
009F0CD0  49 8B CF                        mov rcx, r15
009F0CD3  E8 54 1C 81 FF                  call 0x14020292c
009F0CD8  49 8B CF                        mov rcx, r15
009F0CDB  E8 D4 7D 9A FF                  call 0x140398ab4
009F0CE0  41 8B C4                        mov eax, r12d
009F0CE3  48 81 C4 A0 00 00 00            add rsp, 0xa0
009F0CEA  41 5F                           pop r15
009F0CEC  41 5E                           pop r14
009F0CEE  41 5D                           pop r13
009F0CF0  41 5C                           pop r12
009F0CF2  5F                              pop rdi
009F0CF3  5E                              pop rsi
009F0CF4  5B                              pop rbx
009F0CF5  C3                              ret
009F0CF6  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PspInsertThread(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned int a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned int v_stack_m94;
    unsigned int v_stack_m98;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned int v_stack_mB8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (160);
    v_stack_m50 = a7;
    v_rsi = 0;
    v_stack_m98 = 0;
    v_stack_m70 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184);
    v_stack_m78 = *(unsigned __int64 *)(a1 + 240);
    v_stack_m60 = *(unsigned __int64 *)(a1 + 240);
    v_stack_m90 = 0;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a4)))) & (32)) != 0) goto loc_009F03D4;
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(a2 + 456, a2, a3, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184));
    v_stack_m88 = result;
    if (!(condition_is_above_or_equal)) {
        a3 = a2 + 456;
        a2 = result;
        a1 = a2 + 456;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184));
        result = v_stack_m88;
    }
    if (result == 0) goto loc_009F03D4;
    *(unsigned __int8 *)(result + 10) = 1;
    goto loc_009F03DA;
loc_009F03D4:
loc_009F03DA:
    if (a7 == 0) goto loc_009F04B6;
    v_stack_m80 = *(unsigned __int64 *)(a7 + 32);
    v_stack_m88 = *(unsigned __int64 *)(a7 + 32);
    if (condition_is_above_or_equal) goto loc_009F0499;
    result = KeQueryMaximumGroupCount(a1, *(unsigned __int64 *)(a7 + 32), a3, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184));
    result = ExAllocatePool2(64, (unsigned __int16)(result) * 8 + 8, (unsigned int)(0x20207350ULL), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184));
    if (result != 0) goto loc_009F043F;
    v_stack_m94 = 0xC000009AULL;
    goto loc_009F0595;
loc_009F043F:
    result = KeQueryMaximumGroupCount(64, (unsigned __int16)(result) * 8 + 8, (unsigned int)(0x20207350ULL), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184));
    *(unsigned __int16 *)(result) = 1;
    *(unsigned __int16 *)(result + 2) = (unsigned __int16)(result);
    *(unsigned int *)(result + 4) = 0;
    a3 = ((unsigned __int16)(result)) << (3);
    a2 = 0;
    result = memset(result + 8, a2, a3, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184));
    result = KeAddGroupAffinityEx(result, *(unsigned __int16 *)(0 + 328), *(unsigned __int64 *)(0 + 320), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184));
    if ((*(unsigned __int16 *)(a2 + 416)) != ((unsigned __int16)(*(unsigned __int16 *)(0 + 328)))) {
    }
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(0 + 8))) & (0x4000ULL));
    a1 = -(a1);
    a1 = (a1) & (0 + 20);
    v_stack_m90 = a1;
    goto loc_009F04C3;
loc_009F04B6:
    v_stack_m80 = 0;
    v_stack_m88 = 0;
loc_009F04C3:
    if (*(unsigned __int64 *)(a2 + 672) == 0) goto loc_009F050B;
    if (((*(unsigned int *)(a1 + 116)) & (0x400ULL)) != 0) goto loc_009F050B;
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)(a2 + 672) + 56, 1, *(unsigned __int64 *)(0 + 320), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184));
    v_stack_m98 = 1;
    v_rdi = 1;
    if (result != 0) {
        a2 = result;
        a1 = *(unsigned __int64 *)(a2 + 672);
        result = PspCheckForJobAffinityViolation(a1, a2, *(unsigned __int64 *)(0 + 320), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184));
        a1 = 5;
        v_rdi = 1;
        if (sign_flag) { v_rdi = (unsigned int)(a1); }
        v_stack_m98 = (unsigned int)(v_rdi);
    }
    if (((unsigned int)(v_rdi)) >= 4) goto loc_009F0551;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 500))))) & (0x4000008ULL));
    if (((unsigned int)(result)) != 0x4000000ULL) goto loc_009F0551;
    if (((unsigned int)(result)) >= 0x4000000ULL) goto loc_009F0545;
    if (((*(unsigned int *)(a1 + 116)) & (0x400ULL)) != 0) goto loc_009F0545;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p20)))) & (2)) == 0) goto loc_009F0559;
    goto loc_009F054D;
loc_009F0545:
loc_009F054D:
    goto loc_009F055E;
loc_009F0551:
loc_009F0559:
loc_009F055E:
    v_stack_m94 = (unsigned int)((unsigned int)(0xC0000001ULL));
    if (sign_flag) goto loc_009F0595;
    if (((*(unsigned __int8 *)(a2 + 368)) & (1)) == 0) goto loc_009F058D;
    result = (unsigned int)(*(unsigned int *)(v_stack_p20));
    if (((*(unsigned int *)(v_stack_p20)) & (0x400ULL)) != 0) {
        a2 = a8;
        a1 = a1;
        result = PspCreateSecureThread(a1, a2, *(unsigned __int64 *)(0 + 320), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184));
        a1 = (unsigned int)(result);
        v_stack_m94 = (unsigned int)(result);
    }
    if (!sign_flag) goto loc_009F065E;
loc_009F0595:
    if (((1) & ((unsigned __int8)(v_rdi))) != 0) {
        a1 = *(unsigned __int64 *)(a2 + 672) + 56;
        result = ExReleaseResourceLite(a1, a2, *(unsigned __int64 *)(0 + 320), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184));
    }
    v_rbx = (*(unsigned __int64 *)(a2 + 672)) | (-1);
    result = (unsigned __int8)((v_rbx) & (6));
    if (((unsigned __int8)(result)) == 2) {
        a1 = a2 + 456;
        result = ExfTryToWakePushLock(a1, a2, *(unsigned __int64 *)(0 + 320), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184));
    }
    result = KeAbPostRelease(a2 + 456, a2, *(unsigned __int64 *)(0 + 320), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184));
    v_rbx = (unsigned __int8)((v_rbx) & (6));
    if (((unsigned __int8)(v_rbx)) == 2) {
        a1 = a1 + 1424;
        result = ExfTryToWakePushLock(a1, a2, *(unsigned __int64 *)(0 + 320), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184));
    }
    result = KeAbPostRelease(a1 + 1424, a2, *(unsigned __int64 *)(0 + 320), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184));
    result = KeUninitThread(a1, a2, *(unsigned __int64 *)(0 + 320), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184));
    if (a6 == 0) goto loc_009F0632;
    if (v_stack_m78 != 0) {
        a2 = v_stack_m78;
        a1 = a2;
        result = MmDeleteTeb(a1, a2, *(unsigned __int64 *)(0 + 320), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184));
    }
    if ((*(unsigned __int8 *)(a6)) != 0) {
        a4 = a6;
        a3 = v_stack_p18;
        a1 = a2;
        result = PspDeleteUserStack(a1, a2, a3, a4);
    }
    if (result != 0) {
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    result = (unsigned int)(v_stack_m94);
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 500)))) & (0x40000008ULL)) != 0) { result = (unsigned int)((unsigned int)(0xC000010AULL)); }
    goto loc_009F0CE3;
loc_009F065E:
    result = KeStartThread(a1, result, v_stack_m90, a4);
    v_rdi = a1 + 1424;
    if (((1) & ((unsigned __int8)(a1 + 1424))) != 0) {
        a1 = a6 + 56;
        result = ExReleaseResourceLite(a1, result, v_stack_m90, a4);
        v_rdi = (unsigned int)((a1 + 1424) & (0xFFFFFFFEULL));
        v_stack_m98 = (unsigned int)(v_rdi);
    }
    if (((*(unsigned int *)(a2 + 500)) & (0x40000000ULL)) == 0) goto loc_009F06A6;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p20)))) & (2)) != 0) {
    }
    result = (unsigned int)(*(unsigned int *)(v_stack_p20));
    if (result != 0) {
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, v_stack_m90, a4);
    }
    v_stack_m90 = a1 + 1440;
    v_stack_m58 = a1 + 1440;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 500))) >> (18));
    a1 = (unsigned int)((a1) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 1440)))));
    a1 = (unsigned int)((a1) & (0xE00ULL));
    a1 = (unsigned int)((a1) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 1440)))));
    *(unsigned int *)(a1 + 1440) = (unsigned int)(a1);
    result = (unsigned int)(((unsigned int)((unsigned int)(a1))) ^ (*(unsigned int *)(a2 + 496)));
    result = (unsigned int)((result) & (0x7000ULL));
    result = (unsigned int)((result) ^ ((unsigned int)(a1)));
    *(unsigned int *)(a1 + 1440) = (unsigned int)(result);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 896))) + (1));
    *(unsigned int *)(a2 + 896) = (unsigned int)(result);
    result = (unsigned int)(*(unsigned int *)(a2 + 896));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 896)))) >= = (*(unsigned int *)(a2 + 1496))) {
        result = *(unsigned int *)(a2 + 896);
        *(unsigned int *)(a2 + 1496) = (unsigned int)(result);
    }
    a1 = (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 896)))) < (*(unsigned int *)(a2 + 1496))) ? 1 : 0;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 896)))) != 1) goto loc_009F0748;
    if ((unsigned __int8)(a1) != 0) goto loc_009F0748;
    v_rdi = (unsigned int)((v_rdi) | (2));
    v_stack_m98 = (unsigned int)(v_rdi);
    goto loc_009F076B;
loc_009F0748:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 896)))) != 2) goto loc_009F076B;
    if (((*(unsigned int *)(a2 + 496)) & (0x8000ULL)) == 0) {
    }
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(a2 + 1504, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = a2 + 1504;
        a2 = result;
        a1 = a2 + 1504;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 880 + 8))) != (a2 + 880)) {
        a1 = 3;
    }
    *(unsigned __int64 *)(a1) = a2 + 880;
    *(unsigned __int64 *)(a1 + 8) = *(unsigned __int64 *)(a2 + 880 + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 880 + 8)) = a1;
    *(unsigned __int64 *)(a2 + 880 + 8) = a1;
    v_rbx = (result) | (-1);
    result = (unsigned __int8)((v_rbx) & (6));
    if (((unsigned __int8)(result)) == 2) {
        a1 = a2 + 1504;
        result = ExfTryToWakePushLock(a1, *(unsigned __int64 *)(a2 + 880 + 8), a3, a4);
    }
    result = KeAbPostRelease(a2 + 1504, *(unsigned __int64 *)(a2 + 880 + 8), a3, a4);
    if ((*(unsigned __int64 *)(a2 + 360)) != 0) {
    }
    if ((*(unsigned __int64 *)(a2 + 1976)) != 0) {
    }
    result = (unsigned __int8)((v_rbx) & (6));
    if (((unsigned __int8)(result)) == 2) {
        a1 = a2 + 456;
        result = ExfTryToWakePushLock(a1, *(unsigned __int64 *)(a2 + 880 + 8), a3, a4);
    }
    result = KeAbPostRelease(a2 + 456, *(unsigned __int64 *)(a2 + 880 + 8), a3, a4);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p20)))) & (64)) == 0) goto loc_009F085D;
    result = Feature_ProcesDirectSwap__private_IsEnabledDeviceUsageNoInline(a2 + 456, *(unsigned __int64 *)(a2 + 880 + 8), a3, a4);
    if ((unsigned int)(result) == 0) goto loc_009F0858;
    result = PspChangeProcessExecutionState(a2, *(unsigned __int64 *)(a2 + 880 + 8), a3, a4);
    goto loc_009F085D;
loc_009F0858:
    result = PspChangeProcessExecutionStateLegacy(a2, *(unsigned __int64 *)(a2 + 880 + 8), a3, a4);
loc_009F085D:
    result = ObReferenceObjectExWithTag(a1, 2, (unsigned int)(0x746C6644ULL), a4);
    *(unsigned int *)(a1 + 1516) = 1;
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p20))))) == 0) goto loc_009F08E8;
    result = Feature_SuspendThread2__private_IsEnabledNoReportingNoInline(a1, 2, (unsigned int)(0x746C6644ULL), a4);
    if ((unsigned int)(result) == 0) goto loc_009F0898;
    a3 = 0;
    a2 = 0;
    result = KeSuspendThread(a1, a2, a3, a4);
    goto loc_009F08D4;
loc_009F0898:
    result = KeSuspendThreadOld(a1, a2, a3, a4);
    goto loc_009F08D4;
loc_009F08D4:
    result = (unsigned int)(*(unsigned int *)(v_stack_m90));
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m90))))) != 0) {
        a1 = a1;
        result = KeForceResumeThread(a1, a2, a3, a4);
    }
    result = (unsigned int)(*(unsigned int *)(a2 + 2008));
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 2008))))) != 0) {
        a1 = a1;
        result = KeEnableCoreIsolationMitigationPolicyThread(a1, a2, a3, a4);
    }
    result = PspRecheckThreadOptionalXStateFeatures(0, a1, a3, a4);
    v_r12 = (unsigned int)((unsigned int)(result));
    if (!(sign_flag)) {
        a2 = a1;
        a1 = a2;
        result = PspRecheckThreadPasidMsrState(a1, a2, a3, a4);
        v_r12 = (unsigned int)(result);
    }
    v_stack_m94 = 0;
    if ((*(unsigned __int8 *)(a9 + 388)) == 0) goto loc_009F0946;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p20)))) & (16)) != 0) goto loc_009F0946;
    goto loc_009F094E;
loc_009F0946:
    v_stack_m94 = 1;
loc_009F094E:
    if (sign_flag) goto loc_009F0A57;
    result = (*(unsigned __int64 *)(v_rip + 6119786)) + (76);
    v_stack_mB0 = result;
    v_stack_mB8 = (unsigned int)((unsigned int)(a5));
    a1 = 0;
    result = SeCreateAccessStateEx(a1, a2, a9, a9 + 160);
    if (sign_flag) goto loc_009F0A57;
    v_stack_mA8 = 0;
    v_stack_mB0 = 0;
    v_stack_mB8 = (unsigned int)((unsigned int)(v_stack_m94));
    a4 = 0;
    result = ObInsertObjectEx(0, a9, (unsigned int)(a5), a4);
    if (sign_flag) goto loc_009F0A43;
    result = ObfDereferenceObject(0, a9, (unsigned int)(a5), a4);
    if (v_stack_m80 == 0) goto loc_009F0A02;
    *(unsigned __int64 *)(v_stack_m80) = v_stack_m78;
    goto loc_009F0A02;
loc_009F0A02:
    if (sign_flag) goto loc_009F0A48;
    if (a11 == 0) goto loc_009F0A43;
    *(unsigned __int64 *)(a11) = v_xmm0;
    goto loc_009F0A43;
loc_009F0A43:
    if (!sign_flag) goto loc_009F0A5F;
loc_009F0A48:
    result = SeDeleteAccessState(a9, a9, (unsigned int)(a5), a4);
    goto loc_009F0A5F;
loc_009F0A57:
    result = ObfDereferenceObject(0, a9, (unsigned int)(a5), a4);
loc_009F0A5F:
    if (sign_flag) goto loc_009F0A97;
    v_rbx = (unsigned __int8)((v_rbx) & (6));
    result = v_stack_m58;
    if (((unsigned __int8)(v_rbx)) == 2) {
        result = ExfTryToWakePushLock(a1 + 1424, a9, (unsigned int)(a5), a4);
        a1 = a1 + 1424;
    }
    result = KeAbPostRelease(a1, a9, (unsigned int)(a5), a4);
    goto loc_009F0AF1;
loc_009F0A97:
    v_rbx = (unsigned __int8)((v_rbx) & (6));
    if (((unsigned __int8)(v_rbx)) == 2) {
        result = ExfTryToWakePushLock(a1, a9, (unsigned int)(a5), a4);
        a1 = a1 + 1424;
    }
    result = KeAbPostRelease(a1, a9, (unsigned int)(a5), a4);
    result = (unsigned int)(*(unsigned int *)(v_stack_p20));
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p20))))) != 0) {
        a1 = a1;
        result = KeForceResumeThread(a1, a9, (unsigned int)(a5), a4);
    }
    if (a6 == 0) goto loc_009F0AF1;
    result = a6;
    if ((*(unsigned __int8 *)(a6)) != 0) {
        a4 = a6;
        a3 = v_stack_p18;
        a1 = a2;
        result = PspDeleteUserStack(a1, a9, a3, a4);
    }
    if ((((unsigned __int8)(v_rdi)) & (2)) == 0) goto loc_009F0B4C;
    result = (unsigned int)(*(unsigned int *)(v_rip + 6119425));
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 6119425))))) != 0) {
        a2 = 769;
        a1 = a2;
        result = EtwTraceProcess(a1, a2, a3, a4);
    }
    if ((*(unsigned __int64 *)(a2 + 1640)) != 0) {
        a1 = a2;
        result = PoEnergyContextStart(a1, a2, a3, a4);
    }
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 1532))))) == 0) goto loc_009F0B37;
    result = (unsigned int)(*(unsigned int *)(a2 + 1532));
    v_rbx = 0;
    if ((*(unsigned __int64 *)(a2 + 1600)) != 0) {
        a3 = 1;
        a2 = a7;
        a1 = a2;
        result = PspCallProcessNotifyRoutines(a1, a2, a3, a4);
        v_rbx = (unsigned int)(result);
    }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 6119342)))) & (2)) != 0) {
        a3 = 1;
        a2 = v_stack_p18;
        a1 = a1;
        result = EtwTraceThread(a1, a2, a3, a4);
    }
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 1532))))) == 0) goto loc_009F0B7F;
    if ((*(unsigned __int64 *)(a2 + 1600)) != 0) {
        a3 = 0;
        a2 = 1;
        a1 = a1;
        result = PspCallThreadNotifyRoutines(a1, a2, a3, a4);
    }
    if (sign_flag) goto loc_009F0CD8;
    if (sign_flag) goto loc_009F0BB9;
    result = PspCreateObjectHandle(a1, a9, *(unsigned __int64 *)(v_rip + 6119207), a4);
    goto loc_009F0BC4;
loc_009F0BB9:
loc_009F0BC4:
    result = SeDeleteAccessState(a9, a9, *(unsigned __int64 *)(v_rip + 6119207), a4);
    if (sign_flag) goto loc_009F0C92;
    if (v_stack_m50 == 0) goto loc_009F0C05;
    result = a7;
    v_r12 = (unsigned int)((unsigned int)(a9));
    if (*(unsigned __int64 *)(a7 + 368) != 0) {
        a3 = *(unsigned int *)(a7 + 380);
        a1 = a2;
        result = PspAssignProcessToJobList(a1, *(unsigned __int64 *)(a7 + 368), a3, a4);
        v_r12 = (unsigned int)(result);
    }
    if (sign_flag) goto loc_009F0C44;
    *(unsigned __int64 *)(a10) = *(unsigned __int64 *)(a9 + 392);
    goto loc_009F0C3B;
loc_009F0C3B:
    if (!sign_flag) goto loc_009F0CD8;
loc_009F0C44:
    if (((*(unsigned int *)(a9 + 384)) & (512)) != 0) goto loc_009F0C64;
    if (((*(unsigned int *)(v_stack_m70 + 1532)) & (0x1000ULL)) != 0) {
        a2 = 0;
    }
    result = ObCloseHandle(*(unsigned __int64 *)(a9 + 392), a2, a3, a4);
    if (a6 == 0) goto loc_009F0C8D;
    result = a6;
    if (((*(unsigned __int8 *)(a6)) & (1)) != 0) {
        a1 = (unsigned int)(v_r12);
        result = KeRaiseUserException(a1, a2, a3, a4);
    }
    if (!sign_flag) goto loc_009F0CD8;
loc_009F0C92:
    if (!(condition_is_below)) {
        v_rdi = (unsigned int)((v_rdi) | (8));
    }
    if (((*(unsigned int *)(a1 + 116)) & (0x400ULL)) != 0) goto loc_009F0CC1;
    if (((unsigned int)(v_rdi)) >= 8) {
        *(unsigned int *)(a1 + 1496) = (unsigned int)(v_r12);
    }
    result = KeRequestTerminationThread(a1, a2, a3, a4);
    goto loc_009F0CD8;
loc_009F0CC1:
    result = (unsigned int)(*(unsigned int *)(v_stack_p20));
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p20))))) != 0) {
        a1 = a1;
        result = KeForceResumeThread(a1, a2, a3, a4);
    }
    result = KeReadyThread(a1, a2, a3, a4);
loc_009F0CE3:
    v_rsp = (v_rsp) + (160);
    return (unsigned int)((unsigned int)(v_r12));
}
```

## 5. (Beta) C Style

```c
int64_t PspInsertThread(void *Arg1, void *Arg2, int64_t Arg3, void *Arg4, uint32_t Arg5, int64_t Arg6, void *Arg7, int64_t Arg8, void *Arg9, void *Arg10, int64_t Arg11)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg4 = (uint8_t *)Arg4;
    uint8_t *arg7 = (uint8_t *)Arg7;
    uint8_t *arg9 = (uint8_t *)Arg9;
    uint8_t *arg10 = (uint8_t *)Arg10;

    int64_t result;
    int64_t local_r12;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint32_t v_stack_m94;
    uint32_t v_stack_m98;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint32_t v_stack_mB8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p48;
    uint64_t v_stack_p8;

    *(void **)(local_rsp + 0x20) = Arg4;
    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    *(void **)(local_rsp + 0x10) = Arg2;
    *(void **)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (160);
    v_stack_m50 = Arg7;
    local_rsi = 0;
    v_stack_m98 = 0;
    v_stack_m70 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8);
    v_stack_m78 = *(uint64_t *)(arg1 + 0xF0);
    v_stack_m60 = *(uint64_t *)(arg1 + 0xF0);
    v_stack_m90 = 0;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg4)))) & (32)) != 0) goto loc_009F03D4;
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(Arg2 + 456, Arg2, Arg3, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8));
    v_stack_m88 = result;
    if (!(condition_is_above_or_equal)) {
        Arg3 = Arg2 + 456;
        Arg2 = result;
        Arg1 = Arg2 + 456;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8));
        result = v_stack_m88;
    }
    if (result == 0) goto loc_009F03D4;
    *(uint8_t *)(result + 0xA) = 1;
    goto loc_009F03DA;
loc_009F03D4:
loc_009F03DA:
    if (Arg7 == NULL) goto loc_009F04B6;
    v_stack_m80 = *(uint64_t *)(arg7 + 0x20);
    v_stack_m88 = *(uint64_t *)(arg7 + 0x20);
    if (condition_is_above_or_equal) goto loc_009F0499;
    result = KeQueryMaximumGroupCount(Arg1, *(uint64_t *)(arg7 + 0x20), Arg3, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8));
    result = ExAllocatePool2(64, (uint16_t)(result) * 8 + 8, (uint32_t)(0x20207350ULL), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8));
    if (result != 0) goto loc_009F043F;
    v_stack_m94 = 0xC000009AULL;
    goto loc_009F0595;
loc_009F043F:
    result = KeQueryMaximumGroupCount(64, (uint16_t)(result) * 8 + 8, (uint32_t)(0x20207350ULL), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8));
    *(uint16_t *)(result) = 1;
    *(uint16_t *)(result + 0x2) = (uint16_t)(result);
    *(uint32_t *)(result + 0x4) = 0;
    Arg3 = ((uint16_t)(result)) << (3);
    Arg2 = 0;
    result = memset(result + 8, Arg2, Arg3, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8));
    result = KeAddGroupAffinityEx(result, *(uint16_t *)(0 + 0x148), *(uint64_t *)(0 + 0x140), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8));
    if ((*(uint16_t *)(arg2 + 0x1A0)) != ((uint16_t)(*(uint16_t *)(0 + 0x148)))) {
    }
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(0 + 0x8))) & (0x4000ULL));
    Arg1 = -(Arg1);
    Arg1 = (Arg1) & (0 + 20);
    v_stack_m90 = Arg1;
    goto loc_009F04C3;
loc_009F04B6:
    v_stack_m80 = 0;
    v_stack_m88 = 0;
loc_009F04C3:
    if (*(uint64_t *)(arg2 + 0x2A0) == 0) goto loc_009F050B;
    if (((*(uint32_t *)(arg1 + 0x74)) & (0x400ULL)) != 0) goto loc_009F050B;
    result = ExAcquireResourceSharedLite(*(uint64_t *)(arg2 + 0x2A0) + 56, 1, *(uint64_t *)(0 + 0x140), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8));
    v_stack_m98 = 1;
    local_rdi = 1;
    if (result != 0) {
        Arg2 = result;
        Arg1 = *(uint64_t *)(arg2 + 0x2A0);
        result = PspCheckForJobAffinityViolation(Arg1, Arg2, *(uint64_t *)(0 + 0x140), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8));
        Arg1 = 5;
        local_rdi = 1;
        if (sign_flag) { local_rdi = (uint32_t)(Arg1); }
        v_stack_m98 = (uint32_t)(local_rdi);
    }
    if (((uint32_t)(local_rdi)) >= 4) goto loc_009F0551;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x1F4))))) & (0x4000008ULL));
    if (((uint32_t)(result)) != 0x4000000ULL) goto loc_009F0551;
    if (((uint32_t)(result)) >= 0x4000000ULL) goto loc_009F0545;
    if (((*(uint32_t *)(arg1 + 0x74)) & (0x400ULL)) != 0) goto loc_009F0545;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p20)))) & (2)) == 0) goto loc_009F0559;
    goto loc_009F054D;
loc_009F0545:
loc_009F054D:
    goto loc_009F055E;
loc_009F0551:
loc_009F0559:
loc_009F055E:
    v_stack_m94 = (uint32_t)((uint32_t)(0xC0000001ULL));
    if (sign_flag) goto loc_009F0595;
    if (((*(uint8_t *)(arg2 + 0x170)) & (1)) == 0) goto loc_009F058D;
    result = (uint32_t)(*(uint32_t *)(v_stack_p20));
    if (((*(uint32_t *)(v_stack_p20)) & (0x400ULL)) != 0) {
        Arg2 = Arg8;
        Arg1 = Arg1;
        result = PspCreateSecureThread(Arg1, Arg2, *(uint64_t *)(0 + 0x140), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8));
        Arg1 = (uint32_t)(result);
        v_stack_m94 = (uint32_t)(result);
    }
    if (!sign_flag) goto loc_009F065E;
loc_009F0595:
    if (((1) & ((uint8_t)(local_rdi))) != 0) {
        Arg1 = *(uint64_t *)(arg2 + 0x2A0) + 56;
        result = ExReleaseResourceLite(Arg1, Arg2, *(uint64_t *)(0 + 0x140), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8));
    }
    local_rbx = (*(uint64_t *)(arg2 + 0x2A0)) | (-1);
    result = (uint8_t)((local_rbx) & (6));
    if (((uint8_t)(result)) == 2) {
        Arg1 = Arg2 + 456;
        result = ExfTryToWakePushLock(Arg1, Arg2, *(uint64_t *)(0 + 0x140), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8));
    }
    result = KeAbPostRelease(Arg2 + 456, Arg2, *(uint64_t *)(0 + 0x140), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8));
    local_rbx = (uint8_t)((local_rbx) & (6));
    if (((uint8_t)(local_rbx)) == 2) {
        Arg1 = Arg1 + 1424;
        result = ExfTryToWakePushLock(Arg1, Arg2, *(uint64_t *)(0 + 0x140), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8));
    }
    result = KeAbPostRelease(Arg1 + 1424, Arg2, *(uint64_t *)(0 + 0x140), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8));
    result = KeUninitThread(Arg1, Arg2, *(uint64_t *)(0 + 0x140), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8));
    if (Arg6 == 0) goto loc_009F0632;
    if (v_stack_m78 != 0) {
        Arg2 = v_stack_m78;
        Arg1 = Arg2;
        result = MmDeleteTeb(Arg1, Arg2, *(uint64_t *)(0 + 0x140), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8));
    }
    if ((*(uint8_t *)(Arg6)) != 0) {
        Arg4 = Arg6;
        Arg3 = v_stack_p18;
        Arg1 = Arg2;
        result = PspDeleteUserStack(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, Arg4);
    }
    result = (uint32_t)(v_stack_m94);
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x1F4)))) & (0x40000008ULL)) != 0) { result = (uint32_t)((uint32_t)(0xC000010AULL)); }
    goto loc_009F0CE3;
loc_009F065E:
    result = KeStartThread(Arg1, result, v_stack_m90, Arg4);
    local_rdi = Arg1 + 1424;
    if (((1) & ((uint8_t)(Arg1 + 1424))) != 0) {
        Arg1 = Arg6 + 56;
        result = ExReleaseResourceLite(Arg1, result, v_stack_m90, Arg4);
        local_rdi = (uint32_t)((Arg1 + 1424) & (0xFFFFFFFEULL));
        v_stack_m98 = (uint32_t)(local_rdi);
    }
    if (((*(uint32_t *)(arg2 + 0x1F4)) & (0x40000000ULL)) == 0) goto loc_009F06A6;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p20)))) & (2)) != 0) {
    }
    result = (uint32_t)(*(uint32_t *)(v_stack_p20));
    if (result != 0) {
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, v_stack_m90, Arg4);
    }
    v_stack_m90 = Arg1 + 1440;
    v_stack_m58 = Arg1 + 1440;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x1F4))) >> (18));
    Arg1 = (uint32_t)((Arg1) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x5A0)))));
    Arg1 = (uint32_t)((Arg1) & (0xE00ULL));
    Arg1 = (uint32_t)((Arg1) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x5A0)))));
    *(uint32_t *)(arg1 + 0x5A0) = (uint32_t)(Arg1);
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) ^ (*(uint32_t *)(arg2 + 0x1F0)));
    result = (uint32_t)((result) & (0x7000ULL));
    result = (uint32_t)((result) ^ ((uint32_t)(Arg1)));
    *(uint32_t *)(arg1 + 0x5A0) = (uint32_t)(result);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x380))) + (1));
    *(uint32_t *)(arg2 + 0x380) = (uint32_t)(result);
    result = (uint32_t)(*(uint32_t *)(arg2 + 0x380));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x380)))) >= = (*(uint32_t *)(arg2 + 0x5D8))) {
        result = *(uint32_t *)(arg2 + 0x380);
        *(uint32_t *)(arg2 + 0x5D8) = (uint32_t)(result);
    }
    Arg1 = (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x380)))) < (*(uint32_t *)(arg2 + 0x5D8))) ? 1 : 0;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x380)))) != 1) goto loc_009F0748;
    if ((uint8_t)(Arg1) != 0) goto loc_009F0748;
    local_rdi = (uint32_t)((local_rdi) | (2));
    v_stack_m98 = (uint32_t)(local_rdi);
    goto loc_009F076B;
loc_009F0748:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x380)))) != 2) goto loc_009F076B;
    if (((*(uint32_t *)(arg2 + 0x1F0)) & (0x8000ULL)) == 0) {
    }
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(Arg2 + 1504, Arg2, Arg3, Arg4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = Arg2 + 1504;
        Arg2 = result;
        Arg1 = Arg2 + 1504;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    if ((*(uint64_t *)(*(uint64_t *)(arg2 + 0x370 + 0x8))) != (Arg2 + 880)) {
        Arg1 = 3;
    }
    *(void **)(arg1) = Arg2 + 880;
    *(uint64_t *)(arg1 + 0x8) = *(uint64_t *)(arg2 + 0x370 + 0x8);
    *(void **)(*(uint64_t *)(arg2 + 0x370 + 0x8)) = Arg1;
    *(void **)(arg2 + 0x370 + 0x8) = Arg1;
    local_rbx = (result) | (-1);
    result = (uint8_t)((local_rbx) & (6));
    if (((uint8_t)(result)) == 2) {
        Arg1 = Arg2 + 1504;
        result = ExfTryToWakePushLock(Arg1, *(uint64_t *)(arg2 + 0x370 + 0x8), Arg3, Arg4);
    }
    result = KeAbPostRelease(Arg2 + 1504, *(uint64_t *)(arg2 + 0x370 + 0x8), Arg3, Arg4);
    if ((*(uint64_t *)(arg2 + 0x168)) != 0) {
    }
    if ((*(uint64_t *)(arg2 + 0x7B8)) != 0) {
    }
    result = (uint8_t)((local_rbx) & (6));
    if (((uint8_t)(result)) == 2) {
        Arg1 = Arg2 + 456;
        result = ExfTryToWakePushLock(Arg1, *(uint64_t *)(arg2 + 0x370 + 0x8), Arg3, Arg4);
    }
    result = KeAbPostRelease(Arg2 + 456, *(uint64_t *)(arg2 + 0x370 + 0x8), Arg3, Arg4);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p20)))) & (64)) == 0) goto loc_009F085D;
    result = Feature_ProcesDirectSwap__private_IsEnabledDeviceUsageNoInline(Arg2 + 456, *(uint64_t *)(arg2 + 0x370 + 0x8), Arg3, Arg4);
    if ((uint32_t)(result) == 0) goto loc_009F0858;
    result = PspChangeProcessExecutionState(Arg2, *(uint64_t *)(arg2 + 0x370 + 0x8), Arg3, Arg4);
    goto loc_009F085D;
loc_009F0858:
    result = PspChangeProcessExecutionStateLegacy(Arg2, *(uint64_t *)(arg2 + 0x370 + 0x8), Arg3, Arg4);
loc_009F085D:
    result = ObReferenceObjectExWithTag(Arg1, 2, (uint32_t)(0x746C6644ULL), Arg4);
    *(uint32_t *)(arg1 + 0x5EC) = 1;
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p20))))) == 0) goto loc_009F08E8;
    result = Feature_SuspendThread2__private_IsEnabledNoReportingNoInline(Arg1, 2, (uint32_t)(0x746C6644ULL), Arg4);
    if ((uint32_t)(result) == 0) goto loc_009F0898;
    Arg3 = 0;
    Arg2 = 0;
    result = KeSuspendThread(Arg1, Arg2, Arg3, Arg4);
    goto loc_009F08D4;
loc_009F0898:
    result = KeSuspendThreadOld(Arg1, Arg2, Arg3, Arg4);
    goto loc_009F08D4;
loc_009F08D4:
    result = (uint32_t)(*(uint32_t *)(v_stack_m90));
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m90))))) != 0) {
        Arg1 = Arg1;
        result = KeForceResumeThread(Arg1, Arg2, Arg3, Arg4);
    }
    result = (uint32_t)(*(uint32_t *)(arg2 + 0x7D8));
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0x7D8))))) != 0) {
        Arg1 = Arg1;
        result = KeEnableCoreIsolationMitigationPolicyThread(Arg1, Arg2, Arg3, Arg4);
    }
    result = PspRecheckThreadOptionalXStateFeatures(0, Arg1, Arg3, Arg4);
    local_r12 = (uint32_t)((uint32_t)(result));
    if (!(sign_flag)) {
        Arg2 = Arg1;
        Arg1 = Arg2;
        result = PspRecheckThreadPasidMsrState(Arg1, Arg2, Arg3, Arg4);
        local_r12 = (uint32_t)(result);
    }
    v_stack_m94 = 0;
    if ((*(uint8_t *)(arg9 + 0x184)) == 0) goto loc_009F0946;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p20)))) & (16)) != 0) goto loc_009F0946;
    goto loc_009F094E;
loc_009F0946:
    v_stack_m94 = 1;
loc_009F094E:
    if (sign_flag) goto loc_009F0A57;
    result = (*(uint64_t *)(v_rip + 0x5D616A)) + (76);
    v_stack_mB0 = result;
    v_stack_mB8 = (uint32_t)((uint32_t)(Arg5));
    Arg1 = 0;
    result = SeCreateAccessStateEx(Arg1, Arg2, Arg9, Arg9 + 160);
    if (sign_flag) goto loc_009F0A57;
    v_stack_mA8 = 0;
    v_stack_mB0 = 0;
    v_stack_mB8 = (uint32_t)((uint32_t)(v_stack_m94));
    Arg4 = 0;
    result = ObInsertObjectEx(0, Arg9, (uint32_t)(Arg5), Arg4);
    if (sign_flag) goto loc_009F0A43;
    result = ObfDereferenceObject(0, Arg9, (uint32_t)(Arg5), Arg4);
    if (v_stack_m80 == 0) goto loc_009F0A02;
    *(uint64_t *)(v_stack_m80) = v_stack_m78;
    goto loc_009F0A02;
loc_009F0A02:
    if (sign_flag) goto loc_009F0A48;
    if (Arg11 == 0) goto loc_009F0A43;
    *(uint64_t *)(Arg11) = v_xmm0;
    goto loc_009F0A43;
loc_009F0A43:
    if (!sign_flag) goto loc_009F0A5F;
loc_009F0A48:
    result = SeDeleteAccessState(Arg9, Arg9, (uint32_t)(Arg5), Arg4);
    goto loc_009F0A5F;
loc_009F0A57:
    result = ObfDereferenceObject(0, Arg9, (uint32_t)(Arg5), Arg4);
loc_009F0A5F:
    if (sign_flag) goto loc_009F0A97;
    local_rbx = (uint8_t)((local_rbx) & (6));
    result = v_stack_m58;
    if (((uint8_t)(local_rbx)) == 2) {
        result = ExfTryToWakePushLock(Arg1 + 1424, Arg9, (uint32_t)(Arg5), Arg4);
        Arg1 = Arg1 + 1424;
    }
    result = KeAbPostRelease(Arg1, Arg9, (uint32_t)(Arg5), Arg4);
    goto loc_009F0AF1;
loc_009F0A97:
    local_rbx = (uint8_t)((local_rbx) & (6));
    if (((uint8_t)(local_rbx)) == 2) {
        result = ExfTryToWakePushLock(Arg1, Arg9, (uint32_t)(Arg5), Arg4);
        Arg1 = Arg1 + 1424;
    }
    result = KeAbPostRelease(Arg1, Arg9, (uint32_t)(Arg5), Arg4);
    result = (uint32_t)(*(uint32_t *)(v_stack_p20));
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p20))))) != 0) {
        Arg1 = Arg1;
        result = KeForceResumeThread(Arg1, Arg9, (uint32_t)(Arg5), Arg4);
    }
    if (Arg6 == 0) goto loc_009F0AF1;
    result = Arg6;
    if ((*(uint8_t *)(Arg6)) != 0) {
        Arg4 = Arg6;
        Arg3 = v_stack_p18;
        Arg1 = Arg2;
        result = PspDeleteUserStack(Arg1, Arg9, Arg3, Arg4);
    }
    if ((((uint8_t)(local_rdi)) & (2)) == 0) goto loc_009F0B4C;
    result = (uint32_t)(*(uint32_t *)(v_rip + 0x5D6001));
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x5D6001))))) != 0) {
        Arg2 = 769;
        Arg1 = Arg2;
        result = EtwTraceProcess(Arg1, Arg2, Arg3, Arg4);
    }
    if ((*(uint64_t *)(arg2 + 0x668)) != 0) {
        Arg1 = Arg2;
        result = PoEnergyContextStart(Arg1, Arg2, Arg3, Arg4);
    }
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0x5FC))))) == 0) goto loc_009F0B37;
    result = (uint32_t)(*(uint32_t *)(arg2 + 0x5FC));
    local_rbx = 0;
    if ((*(uint64_t *)(arg2 + 0x640)) != 0) {
        Arg3 = 1;
        Arg2 = Arg7;
        Arg1 = Arg2;
        result = PspCallProcessNotifyRoutines(Arg1, Arg2, Arg3, Arg4);
        local_rbx = (uint32_t)(result);
    }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x5D5FAE)))) & (2)) != 0) {
        Arg3 = 1;
        Arg2 = v_stack_p18;
        Arg1 = Arg1;
        result = EtwTraceThread(Arg1, Arg2, Arg3, Arg4);
    }
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0x5FC))))) == 0) goto loc_009F0B7F;
    if ((*(uint64_t *)(arg2 + 0x640)) != 0) {
        Arg3 = 0;
        Arg2 = 1;
        Arg1 = Arg1;
        result = PspCallThreadNotifyRoutines(Arg1, Arg2, Arg3, Arg4);
    }
    if (sign_flag) goto loc_009F0CD8;
    if (sign_flag) goto loc_009F0BB9;
    result = PspCreateObjectHandle(Arg1, Arg9, *(uint64_t *)(v_rip + 0x5D5F27), Arg4);
    goto loc_009F0BC4;
loc_009F0BB9:
loc_009F0BC4:
    result = SeDeleteAccessState(Arg9, Arg9, *(uint64_t *)(v_rip + 0x5D5F27), Arg4);
    if (sign_flag) goto loc_009F0C92;
    if (v_stack_m50 == 0) goto loc_009F0C05;
    result = Arg7;
    local_r12 = (uint32_t)((uint32_t)(Arg9));
    if (*(uint64_t *)(arg7 + 0x170) != 0) {
        Arg3 = *(uint32_t *)(arg7 + 0x17C);
        Arg1 = Arg2;
        result = PspAssignProcessToJobList(Arg1, *(uint64_t *)(arg7 + 0x170), Arg3, Arg4);
        local_r12 = (uint32_t)(result);
    }
    if (sign_flag) goto loc_009F0C44;
    *(uint64_t *)(arg10) = *(uint64_t *)(arg9 + 0x188);
    goto loc_009F0C3B;
loc_009F0C3B:
    if (!sign_flag) goto loc_009F0CD8;
loc_009F0C44:
    if (((*(uint32_t *)(arg9 + 0x180)) & (512)) != 0) goto loc_009F0C64;
    if (((*(uint32_t *)(v_stack_m70 + 0x5FC)) & (0x1000ULL)) != 0) {
        Arg2 = 0;
    }
    result = ObCloseHandle(*(uint64_t *)(arg9 + 0x188), Arg2, Arg3, Arg4);
    if (Arg6 == 0) goto loc_009F0C8D;
    result = Arg6;
    if (((*(uint8_t *)(Arg6)) & (1)) != 0) {
        Arg1 = (uint32_t)(local_r12);
        result = KeRaiseUserException(Arg1, Arg2, Arg3, Arg4);
    }
    if (!sign_flag) goto loc_009F0CD8;
loc_009F0C92:
    if (!(condition_is_below)) {
        local_rdi = (uint32_t)((local_rdi) | (8));
    }
    if (((*(uint32_t *)(arg1 + 0x74)) & (0x400ULL)) != 0) goto loc_009F0CC1;
    if (((uint32_t)(local_rdi)) >= 8) {
        *(uint32_t *)(arg1 + 0x5D8) = (uint32_t)(local_r12);
    }
    result = KeRequestTerminationThread(Arg1, Arg2, Arg3, Arg4);
    goto loc_009F0CD8;
loc_009F0CC1:
    result = (uint32_t)(*(uint32_t *)(v_stack_p20));
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p20))))) != 0) {
        Arg1 = Arg1;
        result = KeForceResumeThread(Arg1, Arg2, Arg3, Arg4);
    }
    result = KeReadyThread(Arg1, Arg2, Arg3, Arg4);
loc_009F0CE3:
    local_rsp = (local_rsp) + (160);
    return (uint32_t)((uint32_t)(local_r12));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x0` | `32` | `R/W` |
| `Arg1` | `+ 0x0` | `32` | `W` |
| `Arg1` | `+ 0x0` | `64` | `R/W` |
| `Arg1` | `+ 0x74` | `32` | `R` |
| `Arg1` | `+ 0xF0` | `64` | `R` |
| `Arg1` | `+ 0x508` | `128` | `R` |
| `Arg1` | `+ 0x578` | `64` | `R` |
| `Arg1` | `+ 0x590` | `64` | `R` |
| `Arg1` | `+ 0x5A0` | `32` | `R/W` |
| `Arg1` | `+ 0x5A0` | `64` | `R` |
| `Arg1` | `+ 0x5A4` | `32` | `R/W` |
| `Arg1` | `+ 0x5D8` | `32` | `W` |
| `Arg1` | `+ 0x5EC` | `32` | `W` |
| `Arg2` | `+ 0x0` | `64` | `R/W` |
| `Arg2` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0x8` | `64` | `W` |
| `Arg2` | `+ 0x88` | `32` | `R/W` |
| `Arg2` | `+ 0x168` | `64` | `R` |
| `Arg2` | `+ 0x170` | `8` | `R` |
| `Arg2` | `+ 0x1A0` | `16` | `R` |
| `Arg2` | `+ 0x1C8` | `64` | `R` |
| `Arg2` | `+ 0x1F0` | `32` | `R` |
| `Arg2` | `+ 0x1F0` | `32` | `R/W` |
| `Arg2` | `+ 0x1F4` | `32` | `R` |
| `Arg2` | `+ 0x2A0` | `64` | `R` |
| `Arg2` | `+ 0x370` | `64` | `R` |
| `Arg2` | `+ 0x380` | `32` | `R` |
| `Arg2` | `+ 0x380` | `32` | `W` |
| `Arg2` | `+ 0x5D8` | `32` | `R` |
| `Arg2` | `+ 0x5D8` | `32` | `W` |
| `Arg2` | `+ 0x5E0` | `64` | `R` |

추가 오프셋 14개는 표에서 생략했습니다.

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009F0314&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
