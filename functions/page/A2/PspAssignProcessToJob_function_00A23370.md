# PspAssignProcessToJob

- RVA: `0x00A23370`–`0x00A23938` (길이 `1,480` bytes)
- VA: `0x0000000140A23370`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000AB6C8`
- 디코드: `404`개 명령, `1,480/1,480` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **40**; 고유 호출 대상: **37**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00A233F0` → [PspGetNextJobProcess](../91/PspGetNextJobProcess_function_00918450.md) (function, `0x00918450`)
- `0x00A23400` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (function, `0x00210710`)
- `0x00A23414` → [PspQuitNextJobProcess](../78/PspQuitNextJobProcess_function_00785298.md) (function, `0x00785298`)
- `0x00A23429` → [ExAcquireRundownProtection](../../text/21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00A23458` → [PspGetJobLockHierarchyForAssignment](../A6/PspGetJobLockHierarchyForAssignment_function_00A6FDB4.md) (function, `0x00A6FDB4`)
- `0x00A23463` → [PspLockJobAssignment](../87/PspLockJobAssignment_function_0087DC18.md) (function, `0x0087DC18`)
- `0x00A23478` → [PspLockJobsAndProcessExclusive](../87/PspLockJobsAndProcessExclusive_function_0087D45C.md) (function, `0x0087D45C`)
- `0x00A23485` → [PspIsJobMovable](../78/PspIsJobMovable_function_00785044.md) (function, `0x00785044`)
- `0x00A234CF` → [PspGetJobAssignmentDisposition](PspGetJobAssignmentDisposition_function_00A23218.md) (function, `0x00A23218`)
- `0x00A234EB` → [Feature_3033771320__private_IsEnabledDeviceUsageNoInline](../../text/5E/Feature_3033771320__private_IsEnabledDeviceUsageNoInline_function_005E3730.md) (function, `0x005E3730`)
- `0x00A23531` → [PspValidateJobAssignmentUILimits](../AB/PspValidateJobAssignmentUILimits_function_00AB913C.md) (function, `0x00AB913C`)
- `0x00A2355D` → [PspValidateJobAssignmentSiloPolicy](../A7/PspValidateJobAssignmentSiloPolicy_function_00A71CAC.md) (function, `0x00A71CAC`)
- `0x00A23572` → [PspValidateJobAssignmentMemoryPartition](../A6/PspValidateJobAssignmentMemoryPartition_function_00A67994.md) (function, `0x00A67994`)
- `0x00A235ED` → [PspValidateJobAssignmentDiskIoAttribution](../A8/PspValidateJobAssignmentDiskIoAttribution_function_00A86444.md) (function, `0x00A86444`)
- `0x00A23640` → [PspValidateJobChainLimits](../87/PspValidateJobChainLimits_function_0087DD40.md) (function, `0x0087DD40`)
- `0x00A2365B` → [PspEstablishJobHierarchy](../87/PspEstablishJobHierarchy_function_0087E17C.md) (function, `0x0087E17C`)
- `0x00A236BB` → [PspChargeJobWakeCounter](../9D/PspChargeJobWakeCounter_function_009D5D20.md) (function, `0x009D5D20`)
- `0x00A236FF` → [PspChargeJobWakeCounter](../9D/PspChargeJobWakeCounter_function_009D5D20.md) (function, `0x009D5D20`)
- `0x00A23726` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x00A2372E` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00A2374F` → [PspIncrementJobChainProcessCounts](../87/PspIncrementJobChainProcessCounts_function_0087E0B4.md) (function, `0x0087E0B4`)
- `0x00A2375D` → [PspApplyJobChainLimitsToProcess](../87/PspApplyJobChainLimitsToProcess_function_0087EB5C.md) (function, `0x0087EB5C`)
- `0x00A2376F` → [PspUnlockJobsAndProcessExclusive](../87/PspUnlockJobsAndProcessExclusive_function_0087D750.md) (function, `0x0087D750`)
- `0x00A2378F` → [PsQueryProcessAttributes](../9D/PsQueryProcessAttributes_function_009DB630.md) (function, `0x009DB630`)
- `0x00A237B7` → [PspApplyWorkingSetLimitsToProcess](../87/PspApplyWorkingSetLimitsToProcess_function_0087DE9C.md) (function, `0x0087DE9C`)
- `0x00A237DB` → [MmAssignProcessToJob](../87/MmAssignProcessToJob_function_0087EEF8.md) (function, `0x0087EEF8`)
- `0x00A237F1` → [PspUnlockJobAssignment](../87/PspUnlockJobAssignment_function_0087DBB4.md) (function, `0x0087DBB4`)
- `0x00A23807` → [Feature_ProcesDirectSwap__private_IsEnabledDeviceUsageNoInline](../../text/5E/Feature_ProcesDirectSwap__private_IsEnabledDeviceUsageNoInline_function_005E3264.md) (function, `0x005E3264`)
- `0x00A23813` → [PspChangeProcessExecutionStateLegacy](../../text/5E/PspChangeProcessExecutionStateLegacy_function_005E4098.md) (function, `0x005E4098`)
- `0x00A2381A` → [PspChangeProcessExecutionState](../AE/PspChangeProcessExecutionState_function_00AEC594.md) (function, `0x00AEC594`)
- `0x00A23822` → [KiLeaveCriticalRegionUnsafe](../../text/25/KiLeaveCriticalRegionUnsafe_function_0025F010.md) (function, `0x0025F010`)
- `0x00A23831` → `ext-ms-win-ntos-win32k-l1-1-0.dll!IsWin32kJobNotifyCallOutPresent` (import, 간접 대상; import `ext-ms-win-ntos-win32k-l1-1-0.dll!IsWin32kJobNotifyCallOutPresent`)
- `0x00A23851` → `ext-ms-win-ntos-win32k-l1-1-0.dll!Win32kJobAddProcessNotify` (import, 간접 대상; import `ext-ms-win-ntos-win32k-l1-1-0.dll!Win32kJobAddProcessNotify`)
- `0x00A23885` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00A238B6` → [PspRemoveProcessFromJobChain](../90/PspRemoveProcessFromJobChain_function_00907288.md) (function, `0x00907288`)
- `0x00A238CE` → [PspUnlockJobsAndProcessExclusive](../87/PspUnlockJobsAndProcessExclusive_function_0087D750.md) (function, `0x0087D750`)
- `0x00A238DB` → [PspUnlockJobAssignment](../87/PspUnlockJobAssignment_function_0087DBB4.md) (function, `0x0087DBB4`)
- `0x00A238ED` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00A238FB` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00A23932` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)

### Direct callers
- [PsAssignProcessToJobObject](PsAssignProcessToJobObject_function_00A23190.md) at `0x00A231D8`

### Static image references
- `0x00A2338C` → RVA `0x00E0A740` (`.data`; read)
- `0x00A23831` → RVA `0x00151690` (`ext-ms-win-ntos-win32k-l1-1-0.dll!IsWin32kJobNotifyCallOutPresent (IAT)`; read)
- `0x00A23851` → RVA `0x00151658` (`ext-ms-win-ntos-win32k-l1-1-0.dll!Win32kJobAddProcessNotify (IAT)`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **12**
  - `0x00A23400` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (`PAGE` → `.text`)
  - `0x00A23429` → [ExAcquireRundownProtection](../../text/21/ExAcquireRundownProtection_function_00216620.md) (`PAGE` → `.text`)
  - `0x00A234EB` → [Feature_3033771320__private_IsEnabledDeviceUsageNoInline](../../text/5E/Feature_3033771320__private_IsEnabledDeviceUsageNoInline_function_005E3730.md) (`PAGE` → `.text`)
  - `0x00A23726` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x00A2372E` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00A23807` → [Feature_ProcesDirectSwap__private_IsEnabledDeviceUsageNoInline](../../text/5E/Feature_ProcesDirectSwap__private_IsEnabledDeviceUsageNoInline_function_005E3264.md) (`PAGE` → `.text`)
  - `0x00A23813` → [PspChangeProcessExecutionStateLegacy](../../text/5E/PspChangeProcessExecutionStateLegacy_function_005E4098.md) (`PAGE` → `.text`)
  - `0x00A23822` → [KiLeaveCriticalRegionUnsafe](../../text/25/KiLeaveCriticalRegionUnsafe_function_0025F010.md) (`PAGE` → `.text`)
  - `0x00A23885` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (`PAGE` → `.text`)
  - `0x00A238ED` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00A238FB` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x00A23932` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A23370  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00A23375  55                              push rbp
00A23376  56                              push rsi
00A23377  57                              push rdi
00A23378  41 54                           push r12
00A2337A  41 55                           push r13
00A2337C  41 56                           push r14
00A2337E  41 57                           push r15
00A23380  48 8D 6C 24 D9                  lea rbp, [rsp - 0x27]
00A23385  48 81 EC A0 00 00 00            sub rsp, 0xa0
00A2338C  48 8B 05 AD 73 3E 00            mov rax, qword ptr [rip + 0x3e73ad]
00A23393  48 33 C4                        xor rax, rsp
00A23396  48 89 45 1F                     mov qword ptr [rbp + 0x1f], rax
00A2339A  0F 57 C0                        xorps xmm0, xmm0
00A2339D  C6 45 CB 00                     mov byte ptr [rbp - 0x35], 0
00A233A1  33 C0                           xor eax, eax
00A233A3  45 33 F6                        xor r14d, r14d
00A233A6  0F 11 45 DF                     movups xmmword ptr [rbp - 0x21], xmm0
00A233AA  48 89 45 EF                     mov qword ptr [rbp - 0x11], rax
00A233AE  32 DB                           xor bl, bl
00A233B0  65 4C 8B 24 25 88 01 00 00      mov r12, qword ptr gs:[0x188]
00A233B9  41 8B F9                        mov edi, r9d
00A233BC  4C 89 65 D7                     mov qword ptr [rbp - 0x29], r12
00A233C0  4D 8B E8                        mov r13, r8
00A233C3  48 89 45 17                     mov qword ptr [rbp + 0x17], rax
00A233C7  48 8B F2                        mov rsi, rdx
00A233CA  44 89 75 C7                     mov dword ptr [rbp - 0x39], r14d
00A233CE  4C 8B F9                        mov r15, rcx
00A233D1  0F 11 45 F7                     movups xmmword ptr [rbp - 9], xmm0
00A233D5  0F 11 45 07                     movups xmmword ptr [rbp + 7], xmm0
00A233D9  41 83 F9 05                     cmp r9d, 5
00A233DD  75 3E                           jne 0x140a2341d
00A233DF  4C 8B AA A0 02 00 00            mov r13, qword ptr [rdx + 0x2a0]
00A233E6  4C 8D 45 DF                     lea r8, [rbp - 0x21]
00A233EA  49 8B D4                        mov rdx, r12
00A233ED  45 33 C9                        xor r9d, r9d
00A233F0  E8 5B 50 EF FF                  call 0x140918450
00A233F5  BA 50 73 4A 62                  mov edx, 0x624a7350
00A233FA  48 8B C8                        mov rcx, rax
00A233FD  48 8B F0                        mov rsi, rax
00A23400  E8 0B D3 7E FF                  call 0x140210710
00A23405  4C 8B CE                        mov r9, rsi
00A23408  4C 8D 45 DF                     lea r8, [rbp - 0x21]
00A2340C  49 8B D4                        mov rdx, r12
00A2340F  49 8B CF                        mov rcx, r15
00A23412  B3 01                           mov bl, 1
00A23414  E8 7F 1E D6 FF                  call 0x140785298
00A23419  44 8B 75 C7                     mov r14d, dword ptr [rbp - 0x39]
00A2341D  48 85 F6                        test rsi, rsi
00A23420  74 21                           je 0x140a23443
00A23422  48 8D 8E E8 01 00 00            lea rcx, [rsi + 0x1e8]
00A23429  E8 F2 31 7F FF                  call 0x140216620
00A2342E  84 C0                           test al, al
00A23430  75 0E                           jne 0x140a23440
00A23432  41 BD 0A 01 00 C0               mov r13d, 0xc000010a
00A23438  41 8B FD                        mov edi, r13d
00A2343B  E9 39 04 00 00                  jmp 0x140a23879
00A23440  80 CB 10                        or bl, 0x10
00A23443  48 8D 45 F7                     lea rax, [rbp - 9]
00A23447  44 8B CF                        mov r9d, edi
00A2344A  4D 8B C5                        mov r8, r13
00A2344D  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A23452  48 8B D6                        mov rdx, rsi
00A23455  49 8B CF                        mov rcx, r15
00A23458  E8 57 C9 04 00                  call 0x140a6fdb4
00A2345D  49 8B CC                        mov rcx, r12
00A23460  80 CB 06                        or bl, 6
00A23463  E8 B0 A7 E5 FF                  call 0x14087dc18
00A23468  41 B9 01 00 00 00               mov r9d, 1
00A2346E  48 8D 4D F7                     lea rcx, [rbp - 9]
00A23472  4D 8B C4                        mov r8, r12
00A23475  48 8B D6                        mov rdx, rsi
00A23478  E8 DF 9F E5 FF                  call 0x14087d45c
00A2347D  49 8B CF                        mov rcx, r15
00A23480  83 FF 05                        cmp edi, 5
00A23483  75 40                           jne 0x140a234c5
00A23485  E8 BA 1B D6 FF                  call 0x140785044
00A2348A  84 C0                           test al, al
00A2348C  75 0A                           jne 0x140a23498
00A2348E  BF 22 00 00 C0                  mov edi, 0xc0000022
00A23493  E9 DB 03 00 00                  jmp 0x140a23873
00A23498  48 8B 86 A0 02 00 00            mov rax, qword ptr [rsi + 0x2a0]
00A2349F  C7 45 C7 05 00 00 00            mov dword ptr [rbp - 0x39], 5
00A234A6  49 3B C7                        cmp rax, r15
00A234A9  75 0C                           jne 0x140a234b7
00A234AB  F7 86 FC 05 00 00 00 10 00 00   test dword ptr [rsi + 0x5fc], 0x1000
00A234B5  75 57                           jne 0x140a2350e
00A234B7  BF 22 00 00 C0                  mov edi, 0xc0000022
00A234BC  44 8B 75 C7                     mov r14d, dword ptr [rbp - 0x39]
00A234C0  E9 AE 03 00 00                  jmp 0x140a23873
00A234C5  4C 8D 4D C7                     lea r9, [rbp - 0x39]
00A234C9  4D 8B C5                        mov r8, r13
00A234CC  48 8B D6                        mov rdx, rsi
00A234CF  E8 44 FD FF FF                  call 0x140a23218
00A234D4  44 8B 75 C7                     mov r14d, dword ptr [rbp - 0x39]
00A234D8  85 C0                           test eax, eax
00A234DA  78 B2                           js 0x140a2348e
00A234DC  44 3B F7                        cmp r14d, edi
00A234DF  74 0A                           je 0x140a234eb
00A234E1  BF 2D 02 00 C0                  mov edi, 0xc000022d
00A234E6  E9 88 03 00 00                  jmp 0x140a23873
00A234EB  E8 40 02 BC FF                  call 0x1405e3730
00A234F0  85 C0                           test eax, eax
00A234F2  74 50                           je 0x140a23544
00A234F4  41 83 FE 04                     cmp r14d, 4
00A234F8  75 4A                           jne 0x140a23544
00A234FA  48 8B 86 A0 02 00 00            mov rax, qword ptr [rsi + 0x2a0]
00A23501  48 3B 45 FF                     cmp rax, qword ptr [rbp - 1]
00A23505  74 07                           je 0x140a2350e
00A23507  BF 2D 02 00 C0                  mov edi, 0xc000022d
00A2350C  EB AE                           jmp 0x140a234bc
00A2350E  44 8B 75 C7                     mov r14d, dword ptr [rbp - 0x39]
00A23512  48 85 F6                        test rsi, rsi
00A23515  74 11                           je 0x140a23528
00A23517  41 83 FE 05                     cmp r14d, 5
00A2351B  74 0B                           je 0x140a23528
00A2351D  4C 8B AE A0 02 00 00            mov r13, qword ptr [rsi + 0x2a0]
00A23524  44 8B 75 C7                     mov r14d, dword ptr [rbp - 0x39]
00A23528  45 8B C6                        mov r8d, r14d
00A2352B  49 8B D5                        mov rdx, r13
00A2352E  49 8B CF                        mov rcx, r15
00A23531  E8 06 5C 09 00                  call 0x140ab913c
00A23536  84 C0                           test al, al
00A23538  75 17                           jne 0x140a23551
00A2353A  BF BB 00 00 C0                  mov edi, 0xc00000bb
00A2353F  E9 2F 03 00 00                  jmp 0x140a23873
00A23544  41 83 FE 02                     cmp r14d, 2
00A23548  75 C8                           jne 0x140a23512
00A2354A  33 FF                           xor edi, edi
00A2354C  E9 22 03 00 00                  jmp 0x140a23873
00A23551  45 8B CE                        mov r9d, r14d
00A23554  4C 8B C6                        mov r8, rsi
00A23557  49 8B D5                        mov rdx, r13
00A2355A  49 8B CF                        mov rcx, r15
00A2355D  E8 4A E7 04 00                  call 0x140a71cac
00A23562  84 C0                           test al, al
00A23564  74 D4                           je 0x140a2353a
00A23566  45 8B CE                        mov r9d, r14d
00A23569  4C 8B C6                        mov r8, rsi
00A2356C  49 8B D5                        mov rdx, r13
00A2356F  49 8B CF                        mov rcx, r15
00A23572  E8 1D 44 04 00                  call 0x140a67994
00A23577  84 C0                           test al, al
00A23579  74 BF                           je 0x140a2353a
00A2357B  41 83 FE 05                     cmp r14d, 5
00A2357F  75 0B                           jne 0x140a2358c
00A23581  41 8B 87 20 04 00 00            mov eax, dword ptr [r15 + 0x420]
00A23588  A8 01                           test al, 1
00A2358A  75 AE                           jne 0x140a2353a
00A2358C  41 8D 46 FC                     lea eax, [r14 - 4]
00A23590  B9 FC FF FF FF                  mov ecx, 0xfffffffc
00A23595  85 C1                           test ecx, eax
00A23597  75 15                           jne 0x140a235ae
00A23599  41 83 FE 06                     cmp r14d, 6
00A2359D  74 0F                           je 0x140a235ae
00A2359F  41 0F B6 85 4E 04 00 00         movzx eax, byte ptr [r13 + 0x44e]
00A235A7  FF C0                           inc eax
00A235A9  83 F8 64                        cmp eax, 0x64
00A235AC  77 8C                           ja 0x140a2353a
00A235AE  41 8D 46 FC                     lea eax, [r14 - 4]
00A235B2  85 C1                           test ecx, eax
00A235B4  75 31                           jne 0x140a235e7
00A235B6  41 83 FE 06                     cmp r14d, 6
00A235BA  74 2B                           je 0x140a235e7
00A235BC  33 C9                           xor ecx, ecx
00A235BE  8D 41 FF                        lea eax, [rcx - 1]
00A235C1  83 F8 01                        cmp eax, 1
00A235C4  76 1A                           jbe 0x140a235e0
00A235C6  41 0F BA A7 10 06 00 00 19      bt dword ptr [r15 + 0x610], 0x19
00A235CF  73 0F                           jae 0x140a235e0
00A235D1  41 0F BA A5 10 06 00 00 19      bt dword ptr [r13 + 0x610], 0x19
00A235DA  0F 82 5A FF FF FF               jb 0x140a2353a
00A235E0  FF C1                           inc ecx
00A235E2  83 F9 03                        cmp ecx, 3
00A235E5  7C D7                           jl 0x140a235be
00A235E7  45 8B C6                        mov r8d, r14d
00A235EA  49 8B CF                        mov rcx, r15
00A235ED  E8 52 2E 06 00                  call 0x140a86444
00A235F2  84 C0                           test al, al
00A235F4  0F 84 40 FF FF FF               je 0x140a2353a
00A235FA  41 8B CE                        mov ecx, r14d
00A235FD  83 E9 01                        sub ecx, 1
00A23600  74 23                           je 0x140a23625
00A23602  83 E9 02                        sub ecx, 2
00A23605  74 1E                           je 0x140a23625
00A23607  83 E9 01                        sub ecx, 1
00A2360A  74 15                           je 0x140a23621
00A2360C  83 F9 01                        cmp ecx, 1
00A2360F  74 09                           je 0x140a2361a
00A23611  45 33 E4                        xor r12d, r12d
00A23614  4C 21 65 CF                     and qword ptr [rbp - 0x31], r12
00A23618  EB 35                           jmp 0x140a2364f
00A2361A  4D 8B E5                        mov r12, r13
00A2361D  33 C0                           xor eax, eax
00A2361F  EB 0A                           jmp 0x140a2362b
00A23621  33 C0                           xor eax, eax
00A23623  EB 03                           jmp 0x140a23628
00A23625  49 8B C5                        mov rax, r13
00A23628  4D 8B E7                        mov r12, r15
00A2362B  48 89 45 CF                     mov qword ptr [rbp - 0x31], rax
00A2362F  4D 85 E4                        test r12, r12
00A23632  74 1B                           je 0x140a2364f
00A23634  45 33 C9                        xor r9d, r9d
00A23637  4C 8B C6                        mov r8, rsi
00A2363A  48 8B D0                        mov rdx, rax
00A2363D  49 8B CC                        mov rcx, r12
00A23640  E8 FB A6 E5 FF                  call 0x14087dd40
00A23645  8B F8                           mov edi, eax
00A23647  85 C0                           test eax, eax
00A23649  0F 88 20 02 00 00               js 0x140a2386f
00A2364F  45 8B CE                        mov r9d, r14d
00A23652  4D 8B C5                        mov r8, r13
00A23655  48 8B D6                        mov rdx, rsi
00A23658  49 8B CF                        mov rcx, r15
00A2365B  E8 1C AB E5 FF                  call 0x14087e17c
00A23660  8B F8                           mov edi, eax
00A23662  85 C0                           test eax, eax
00A23664  0F 88 05 02 00 00               js 0x140a2386f
00A2366A  48 85 F6                        test rsi, rsi
00A2366D  0F 84 FA 01 00 00               je 0x140a2386d
00A23673  41 F7 87 10 06 00 00 00 10 00 00  test dword ptr [r15 + 0x610], 0x1000
00A2367E  0F 84 89 00 00 00               je 0x140a2370d
00A23684  33 FF                           xor edi, edi
00A23686  41 BE FF FF FF 7F               mov r14d, 0x7fffffff
00A2368C  48 63 C7                        movsxd rax, edi
00A2368F  8B 8C 86 28 07 00 00            mov ecx, dword ptr [rsi + rax*4 + 0x728]
00A23696  41 23 CE                        and ecx, r14d
00A23699  74 25                           je 0x140a236c0
00A2369B  48 C7 44 24 30 4A 6F 62 00      mov qword ptr [rsp + 0x30], 0x626f4a
00A236A4  44 8B C7                        mov r8d, edi
00A236A7  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
00A236AD  49 8B D5                        mov rdx, r13
00A236B0  83 64 24 20 00                  and dword ptr [rsp + 0x20], 0
00A236B5  44 8B C9                        mov r9d, ecx
00A236B8  49 8B CF                        mov rcx, r15
00A236BB  E8 60 26 FB FF                  call 0x1409d5d20
00A236C0  F0 0F BA AC BE 28 07 00 00 1F   lock bts dword ptr [rsi + rdi*4 + 0x728], 0x1f
00A236CA  FF C7                           inc edi
00A236CC  83 FF 07                        cmp edi, 7
00A236CF  72 BB                           jb 0x140a2368c
00A236D1  8B 86 4C 07 00 00               mov eax, dword ptr [rsi + 0x74c]
00A236D7  41 23 C6                        and eax, r14d
00A236DA  74 28                           je 0x140a23704
00A236DC  48 C7 44 24 30 4A 6F 62 00      mov qword ptr [rsp + 0x30], 0x626f4a
00A236E5  45 33 C0                        xor r8d, r8d
00A236E8  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
00A236EE  49 8B D5                        mov rdx, r13
00A236F1  44 8B C8                        mov r9d, eax
00A236F4  49 8B CF                        mov rcx, r15
00A236F7  C7 44 24 20 04 00 00 00         mov dword ptr [rsp + 0x20], 4
00A236FF  E8 1C 26 FB FF                  call 0x1409d5d20
00A23704  F0 0F BA AE 4C 07 00 00 1F      lock bts dword ptr [rsi + 0x74c], 0x1f
00A2370D  48 8D BE C8 01 00 00            lea rdi, [rsi + 0x1c8]
00A23714  48 83 C8 FF                     or rax, 0xffffffffffffffff
00A23718  F0 48 0F C1 07                  lock xadd qword ptr [rdi], rax
00A2371D  24 06                           and al, 6
00A2371F  3C 02                           cmp al, 2
00A23721  75 08                           jne 0x140a2372b
00A23723  48 8B CF                        mov rcx, rdi
00A23726  E8 A5 26 84 FF                  call 0x140265dd0
00A2372B  48 8B CF                        mov rcx, rdi
00A2372E  E8 CD DE 8B FF                  call 0x1402e1600
00A23733  44 8B 75 C7                     mov r14d, dword ptr [rbp - 0x39]
00A23737  80 CB 08                        or bl, 8
00A2373A  48 8B 55 CF                     mov rdx, qword ptr [rbp - 0x31]
00A2373E  41 83 FE 04                     cmp r14d, 4
00A23742  4C 8B C6                        mov r8, rsi
00A23745  49 8B CC                        mov rcx, r12
00A23748  49 0F 44 D5                     cmove rdx, r13
00A2374C  45 33 C9                        xor r9d, r9d
00A2374F  E8 60 A9 E5 FF                  call 0x14087e0b4
00A23754  4C 8B C6                        mov r8, rsi
00A23757  49 8B D5                        mov rdx, r13
00A2375A  49 8B CF                        mov rcx, r15
00A2375D  E8 FA B3 E5 FF                  call 0x14087eb5c
00A23762  4C 8B 65 D7                     mov r12, qword ptr [rbp - 0x29]
00A23766  48 8D 4D F7                     lea rcx, [rbp - 9]
00A2376A  4D 8B C4                        mov r8, r12
00A2376D  33 D2                           xor edx, edx
00A2376F  E8 DC 9F E5 FF                  call 0x14087d750
00A23774  80 E3 FB                        and bl, 0xfb
00A23777  BF 00 00 00 01                  mov edi, 0x1000000
00A2377C  41 85 BF 10 06 00 00            test dword ptr [r15 + 0x610], edi
00A23783  75 2F                           jne 0x140a237b4
00A23785  45 33 C0                        xor r8d, r8d
00A23788  48 8D 55 CB                     lea rdx, [rbp - 0x35]
00A2378C  48 8B CE                        mov rcx, rsi
00A2378F  E8 9C 7E FB FF                  call 0x1409db630
00A23794  80 7D CB 00                     cmp byte ptr [rbp - 0x35], 0
00A23798  75 0E                           jne 0x140a237a8
00A2379A  F0 41 81 8F 10 06 00 00 00 00 80 01  lock or dword ptr [r15 + 0x610], 0x1800000
00A237A6  EB 08                           jmp 0x140a237b0
00A237A8  F0 41 09 BF 10 06 00 00         lock or dword ptr [r15 + 0x610], edi
00A237B0  44 8B 75 C7                     mov r14d, dword ptr [rbp - 0x39]
00A237B4  48 8B CE                        mov rcx, rsi
00A237B7  E8 E0 A6 E5 FF                  call 0x14087de9c
00A237BC  8B F8                           mov edi, eax
00A237BE  85 C0                           test eax, eax
00A237C0  0F 88 AD 00 00 00               js 0x140a23873
00A237C6  45 33 C0                        xor r8d, r8d
00A237C9  49 8B D5                        mov rdx, r13
00A237CC  41 83 FE 05                     cmp r14d, 5
00A237D0  48 8B CE                        mov rcx, rsi
00A237D3  41 8D 40 04                     lea eax, [r8 + 4]
00A237D7  44 0F 44 C0                     cmove r8d, eax
00A237DB  E8 18 B7 E5 FF                  call 0x14087eef8
00A237E0  85 C0                           test eax, eax
00A237E2  75 0A                           jne 0x140a237ee
00A237E4  BF 44 00 00 C0                  mov edi, 0xc0000044
00A237E9  E9 85 00 00 00                  jmp 0x140a23873
00A237EE  49 8B CC                        mov rcx, r12
00A237F1  E8 BE A3 E5 FF                  call 0x14087dbb4
00A237F6  48 83 C8 FF                     or rax, 0xffffffffffffffff
00A237FA  80 E3 FD                        and bl, 0xfd
00A237FD  66 41 01 84 24 E4 01 00 00      add word ptr [r12 + 0x1e4], ax
00A23806  90                              nop
00A23807  E8 58 FA BB FF                  call 0x1405e3264
00A2380C  48 8B CE                        mov rcx, rsi
00A2380F  85 C0                           test eax, eax
00A23811  75 07                           jne 0x140a2381a
00A23813  E8 80 08 BC FF                  call 0x1405e4098
00A23818  EB 05                           jmp 0x140a2381f
00A2381A  E8 75 8D 0C 00                  call 0x140aec594
00A2381F  49 8B CC                        mov rcx, r12
00A23822  E8 E9 B7 83 FF                  call 0x14025f010
00A23827  41 83 BF 20 02 00 00 00         cmp dword ptr [r15 + 0x220], 0
00A2382F  74 2C                           je 0x140a2385d
00A23831  48 FF 15 58 DE 72 FF            call qword ptr [rip - 0x8d21a8]
00A23838  0F 1F 44 00 00                  nop dword ptr [rax + rax]
00A2383D  84 C0                           test al, al
00A2383F  74 1C                           je 0x140a2385d
00A23841  41 83 BF 40 02 00 00 FD         cmp dword ptr [r15 + 0x240], -3
00A23849  77 12                           ja 0x140a2385d
00A2384B  48 8B D6                        mov rdx, rsi
00A2384E  49 8B CF                        mov rcx, r15
00A23851  48 FF 15 00 DE 72 FF            call qword ptr [rip - 0x8d2200]
00A23858  0F 1F 44 00 00                  nop dword ptr [rax + rax]
00A2385D  41 83 FE 05                     cmp r14d, 5
00A23861  75 10                           jne 0x140a23873
00A23863  BF 2D 02 00 C0                  mov edi, 0xc000022d
00A23868  80 CB 20                        or bl, 0x20
00A2386B  EB 06                           jmp 0x140a23873
00A2386D  33 FF                           xor edi, edi
00A2386F  4C 8B 65 D7                     mov r12, qword ptr [rbp - 0x29]
00A23873  41 BD 0A 01 00 C0               mov r13d, 0xc000010a
00A23879  F6 C3 10                        test bl, 0x10
00A2387C  74 0C                           je 0x140a2388a
00A2387E  48 8D 8E E8 01 00 00            lea rcx, [rsi + 0x1e8]
00A23885  E8 F6 65 92 FF                  call 0x140349e80
00A2388A  F6 C3 20                        test bl, 0x20
00A2388D  75 2C                           jne 0x140a238bb
00A2388F  85 FF                           test edi, edi
00A23891  79 28                           jns 0x140a238bb
00A23893  F6 C3 08                        test bl, 8
00A23896  74 23                           je 0x140a238bb
00A23898  41 83 FE 05                     cmp r14d, 5
00A2389C  74 7E                           je 0x140a2391c
00A2389E  41 3B FD                        cmp edi, r13d
00A238A1  B8 44 00 00 C0                  mov eax, 0xc0000044
00A238A6  48 8B CE                        mov rcx, rsi
00A238A9  44 0F 45 E8                     cmovne r13d, eax
00A238AD  33 D2                           xor edx, edx
00A238AF  45 8B CD                        mov r9d, r13d
00A238B2  44 8D 42 0A                     lea r8d, [rdx + 0xa]
00A238B6  E8 CD 39 EE FF                  call 0x140907288
00A238BB  B8 04 00 00 00                  mov eax, 4
00A238C0  84 D8                           test al, bl
00A238C2  74 0F                           je 0x140a238d3
00A238C4  4D 8B C4                        mov r8, r12
00A238C7  48 8D 4D F7                     lea rcx, [rbp - 9]
00A238CB  48 8B D6                        mov rdx, rsi
00A238CE  E8 7D 9E E5 FF                  call 0x14087d750
00A238D3  F6 C3 02                        test bl, 2
00A238D6  74 08                           je 0x140a238e0
00A238D8  49 8B CC                        mov rcx, r12
00A238DB  E8 D4 A2 E5 FF                  call 0x14087dbb4
00A238E0  F6 C3 01                        test bl, 1
00A238E3  74 0D                           je 0x140a238f2
00A238E5  BA 50 73 4A 62                  mov edx, 0x624a7350
00A238EA  48 8B CE                        mov rcx, rsi
00A238ED  E8 EE 3F 8D FF                  call 0x1402f78e0
00A238F2  8B C7                           mov eax, edi
00A238F4  48 8B 4D 1F                     mov rcx, qword ptr [rbp + 0x1f]
00A238F8  48 33 CC                        xor rcx, rsp
00A238FB  E8 40 8D C8 FF                  call 0x1406ac640
00A23900  48 8B 9C 24 F8 00 00 00         mov rbx, qword ptr [rsp + 0xf8]
00A23908  48 81 C4 A0 00 00 00            add rsp, 0xa0
00A2390F  41 5F                           pop r15
00A23911  41 5E                           pop r14
00A23913  41 5D                           pop r13
00A23915  41 5C                           pop r12
00A23917  5F                              pop rdi
00A23918  5E                              pop rsi
00A23919  5D                              pop rbp
00A2391A  C3                              ret
00A2391B  CC                              int3
00A2391C  48 63 C7                        movsxd rax, edi
00A2391F  4D 8B CF                        mov r9, r15
00A23922  45 33 C0                        xor r8d, r8d
00A23925  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A2392A  48 8B D6                        mov rdx, rsi
00A2392D  B9 EF 00 00 00                  mov ecx, 0xef
00A23932  E8 29 9D AD FF                  call 0x1404fd660
00A23937  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PspAssignProcessToJob(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m5F;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int8 v_stack_m94;
    unsigned int v_stack_m98;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_p20;

    v_stack_p20 = v_rbx;
    v_rsp = (v_rsp) - (160);
    result = (*(unsigned __int64 *)(v_rip + 4092845)) ^ (v_rsp);
    v_stack_m40 = result;
    v_stack_m94 = 0;
    result = 0;
    v_r14 = 0;
    v_stack_m80 = v_xmm0;
    v_stack_m70 = 0;
    v_rbx = 0;
    v_stack_m88 = *(unsigned __int64 *)(gs_base + (0 + 392));
    v_stack_m48 = 0;
    v_stack_m98 = 0;
    v_stack_m68 = v_xmm0;
    v_stack_m58 = v_xmm0;
    v_rsi = a2;
    v_r13 = a3;
    if (a4 == 5) {
        v_r13 = *(unsigned __int64 *)(a2 + 672);
        a3 = v_stack_m80;
        a2 = *(unsigned __int64 *)(gs_base + (0 + 392));
        a4 = 0;
        result = PspGetNextJobProcess(a1, a2, a3, a4);
        a2 = 0x624A7350ULL;
        a1 = result;
        v_rsi = result;
        result = ObfReferenceObjectWithTag(a1, a2, a3, a4);
        a4 = v_rsi;
        a3 = v_stack_m80;
        a2 = *(unsigned __int64 *)(gs_base + (0 + 392));
        a1 = a1;
        v_rbx = 1;
        result = PspQuitNextJobProcess(a1, a2, a3, a4);
        v_r14 = v_stack_m98;
    }
    if (v_rsi == 0) goto loc_00A23443;
    result = ExAcquireRundownProtection(v_rsi + 488, a2, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00A23440;
    goto loc_00A23879;
loc_00A23440:
    v_rbx = (unsigned __int8)((v_rbx) | (16));
loc_00A23443:
    v_stack_mB8 = v_stack_m68;
    result = PspGetJobLockHierarchyForAssignment(a1, v_rsi, (unsigned int)(0xC000010AULL), (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0xC000010AULL))))));
    v_rbx = (unsigned __int8)((v_rbx) | (6));
    result = PspLockJobAssignment(*(unsigned __int64 *)(gs_base + (0 + 392)), v_rsi, (unsigned int)(0xC000010AULL), (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0xC000010AULL))))));
    result = PspLockJobsAndProcessExclusive(v_stack_m68, v_rsi, *(unsigned __int64 *)(gs_base + (0 + 392)), 1);
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0xC000010AULL))))) != 5) goto loc_00A234C5;
    result = PspIsJobMovable(a1, v_rsi, *(unsigned __int64 *)(gs_base + (0 + 392)), 1);
    if ((unsigned __int8)(result) != 0) goto loc_00A23498;
loc_00A2348E:
    goto loc_00A23873;
loc_00A23498:
    v_stack_m98 = 5;
    if ((*(unsigned __int64 *)(v_rsi + 672)) != a1) goto loc_00A234B7;
    if (((*(unsigned int *)(v_rsi + 1532)) & (0x1000ULL)) != 0) goto loc_00A2350E;
loc_00A234B7:
loc_00A234BC:
    goto loc_00A23873;
loc_00A234C5:
    result = PspGetJobAssignmentDisposition(a1, v_rsi, (unsigned int)(0xC000010AULL), v_stack_m98);
    if (sign_flag) goto loc_00A2348E;
    if (((unsigned int)((unsigned int)(v_stack_m98))) == ((unsigned int)((unsigned int)(0xC0000022ULL)))) goto loc_00A234EB;
    goto loc_00A23873;
loc_00A234EB:
    result = Feature_3033771320__private_IsEnabledDeviceUsageNoInline(a1, v_rsi, (unsigned int)(0xC000010AULL), v_stack_m98);
    if ((unsigned int)(result) == 0) goto loc_00A23544;
    if (((unsigned int)((unsigned int)(v_stack_m98))) != 4) goto loc_00A23544;
    if ((*(unsigned __int64 *)(v_rsi + 672)) == v_stack_m60) goto loc_00A2350E;
    goto loc_00A234BC;
loc_00A2350E:
loc_00A23512:
    if (v_rsi == 0) goto loc_00A23528;
    v_r13 = (unsigned int)(0xC000010AULL);
    v_r14 = (unsigned int)(v_stack_m98);
    if (((unsigned int)((unsigned int)(v_stack_m98))) != 5) {
        v_r13 = *(unsigned __int64 *)(v_rsi + 672);
        v_r14 = v_stack_m98;
    }
    result = PspValidateJobAssignmentUILimits(a1, v_r13, (unsigned int)((unsigned int)(v_r14)), v_stack_m98);
    if ((unsigned __int8)(result) != 0) goto loc_00A23551;
loc_00A2353A:
    goto loc_00A23873;
loc_00A23544:
    if (((unsigned int)(v_r14)) != 2) goto loc_00A23512;
    v_rdi = 0;
    goto loc_00A23873;
loc_00A23551:
    result = PspValidateJobAssignmentSiloPolicy(a1, v_r13, v_rsi, (unsigned int)((unsigned int)(v_r14)));
    if ((unsigned __int8)(result) == 0) goto loc_00A2353A;
    result = PspValidateJobAssignmentMemoryPartition(a1, v_r13, v_rsi, (unsigned int)((unsigned int)(v_r14)));
    if ((unsigned __int8)(result) == 0) goto loc_00A2353A;
    if (((unsigned int)(v_r14)) != 5) goto loc_00A2358C;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 1056)))) & (1)) != 0) goto loc_00A2353A;
loc_00A2358C:
    if ((((unsigned int)((unsigned int)(0xFFFFFFFCULL))) & ((unsigned int)(v_r14 - 4))) != 0) goto loc_00A235AE;
    if (((unsigned int)(v_r14)) == 6) goto loc_00A235AE;
    result = (unsigned int)((*(unsigned __int8 *)(v_r13 + 1102)) + 1);
    if (((unsigned int)(result)) > 100) goto loc_00A2353A;
loc_00A235AE:
    if ((((unsigned int)((unsigned int)(0xFFFFFFFCULL))) & ((unsigned int)(v_r14 - 4))) != 0) goto loc_00A235E7;
    if (((unsigned int)(v_r14)) == 6) goto loc_00A235E7;
    a1 = 0;
loc_00A235BE:
    if (((unsigned int)(a1 - 1)) <= 1) goto loc_00A235E0;
    if (((unsigned int)(a1 - 1)) >= 1) goto loc_00A235E0;
    if (((unsigned int)(a1 - 1)) < 1) goto loc_00A2353A;
loc_00A235E0:
    a1 = (unsigned int)((a1) + 1);
    if (((unsigned int)(a1)) < 3) goto loc_00A235BE;
loc_00A235E7:
    result = PspValidateJobAssignmentDiskIoAttribution(a1, v_r13, (unsigned int)((unsigned int)(v_r14)), (unsigned int)((unsigned int)(v_r14)));
    if ((unsigned __int8)(result) == 0) goto loc_00A2353A;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) - (1));
    if (condition_is_equal) goto loc_00A23625;
    a1 = (unsigned int)((a1) - (2));
    if (condition_is_equal) goto loc_00A23625;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A23621;
    if (((unsigned int)(a1)) == 1) goto loc_00A2361A;
    v_r12 = 0;
    goto loc_00A2364F;
loc_00A2361A:
    result = 0;
    goto loc_00A2362B;
loc_00A23621:
    result = 0;
    goto loc_00A23628;
loc_00A23625:
loc_00A23628:
loc_00A2362B:
    v_stack_m90 = v_r13;
    if (a1 == 0) goto loc_00A2364F;
    a4 = 0;
    result = PspValidateJobChainLimits(a1, v_r13, v_rsi, a4);
    if (sign_flag) goto loc_00A2386F;
loc_00A2364F:
    result = PspEstablishJobHierarchy(a1, v_rsi, v_r13, (unsigned int)((unsigned int)(v_r14)));
    if (sign_flag) goto loc_00A2386F;
    if (v_rsi == 0) goto loc_00A2386D;
    if (((*(unsigned int *)(a1 + 1552)) & (0x1000ULL)) == 0) goto loc_00A2370D;
    v_rdi = 0;
loc_00A2368C:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsi + (int)(0) * 4 + 1832))) & ((unsigned int)((unsigned int)(0x7FFFFFFFULL))));
    result = (int)(0);
    if (!(condition_is_equal)) {
        v_stack_mA8 = 0x626F4AULL;
        a3 = 0;
        a2 = v_r13;
        a4 = (unsigned int)(a1);
        a1 = a1;
        result = PspChargeJobWakeCounter(a1, a2, a3, a4);
    }
    v_rdi = (unsigned int)((v_rdi) + 1);
    if (((unsigned int)(v_rdi)) < 7) goto loc_00A2368C;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsi + 1868))) & ((unsigned int)((unsigned int)(0x7FFFFFFFULL))));
    if (!(condition_is_equal)) {
        v_stack_mA8 = 0x626F4AULL;
        a3 = 0;
        a2 = v_r13;
        a4 = (unsigned int)(result);
        a1 = a1;
        v_stack_mB8 = 4;
        result = PspChargeJobWakeCounter(a1, a2, a3, a4);
    }
loc_00A2370D:
    result = (result) | (-1);
    result = (unsigned __int8)((result) & (6));
    if (((unsigned __int8)(result)) == 2) {
        a1 = v_rsi + 456;
        result = ExfTryToWakePushLock(a1, a2, a3, a4);
    }
    result = KeAbPostRelease(v_rsi + 456, a2, a3, a4);
    v_rbx = (unsigned __int8)((v_rbx) | (8));
    a2 = v_stack_m90;
    if (((unsigned int)((unsigned int)(v_stack_m98))) == 4) { a2 = v_r13; }
    a4 = 0;
    result = PspIncrementJobChainProcessCounts(a1, a2, v_rsi, a4);
    result = PspApplyJobChainLimitsToProcess(a1, v_r13, v_rsi, a4);
    a2 = 0;
    result = PspUnlockJobsAndProcessExclusive(v_stack_m68, a2, v_stack_m88, a4);
    v_rbx = (unsigned __int8)((v_rbx) & (251));
    if (((*(unsigned int *)(a1 + 1552)) & ((unsigned int)((unsigned int)(0x1000000ULL)))) != 0) goto loc_00A237B4;
    a3 = 0;
    result = PsQueryProcessAttributes(v_rsi, v_stack_m94, a3, a4);
    if (v_stack_m94 != 0) goto loc_00A237A8;
    goto loc_00A237B0;
loc_00A237A8:
loc_00A237B0:
loc_00A237B4:
    result = PspApplyWorkingSetLimitsToProcess(v_rsi, v_stack_m94, a3, a4);
    if (sign_flag) goto loc_00A23873;
    a3 = 0;
    if (((unsigned int)((unsigned int)(v_stack_m98))) == 5) { a3 = (unsigned int)(a3 + 4); }
    result = MmAssignProcessToJob(v_rsi, v_r13, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_00A237EE;
    goto loc_00A23873;
loc_00A237EE:
    result = PspUnlockJobAssignment(v_stack_m88, v_r13, a3, a4);
    result = (result) | (-1);
    v_rbx = (unsigned __int8)((v_rbx) & (253));
    result = Feature_ProcesDirectSwap__private_IsEnabledDeviceUsageNoInline(v_stack_m88, v_r13, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_00A2381A;
    result = PspChangeProcessExecutionStateLegacy(v_rsi, v_r13, a3, a4);
    goto loc_00A2381F;
loc_00A2381A:
    result = PspChangeProcessExecutionState(v_rsi, v_r13, a3, a4);
loc_00A2381F:
    result = KiLeaveCriticalRegionUnsafe(v_stack_m88, v_r13, a3, a4);
    if ((*(unsigned int *)(a1 + 544)) == 0) goto loc_00A2385D;
    result = ext_ms_win_ntos_win32k_l1_1_0_dll_IsWin32kJobNotifyCallOutPresent(v_stack_m88, v_r13, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00A2385D;
    if ((*(unsigned int *)(a1 + 576)) <= -3) {
        a2 = v_rsi;
        a1 = a1;
        result = ext_ms_win_ntos_win32k_l1_1_0_dll_Win32kJobAddProcessNotify(a1, a2, a3, a4);
    }
    if (((unsigned int)((unsigned int)(v_stack_m98))) != 5) goto loc_00A23873;
    v_rbx = (unsigned __int8)((v_rbx) | (32));
    goto loc_00A23873;
loc_00A2386D:
    v_rdi = 0;
loc_00A2386F:
loc_00A23873:
loc_00A23879:
    if ((((unsigned __int8)(v_rbx)) & (16)) != 0) {
        a1 = v_rsi + 488;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    if ((((unsigned __int8)(v_rbx)) & (32)) != 0) goto loc_00A238BB;
    if (!sign_flag) goto loc_00A238BB;
    if ((((unsigned __int8)(v_rbx)) & (8)) == 0) goto loc_00A238BB;
    if (((unsigned int)((unsigned int)(v_stack_m98))) == 5) goto loc_00A2391C;
    v_r13 = (unsigned int)(0xC000010AULL);
    if (0 != ((unsigned int)((unsigned int)(0xC000010AULL)))) { v_r13 = (unsigned int)((unsigned int)(0xC0000044ULL)); }
    a2 = 0;
    result = PspRemoveProcessFromJobChain(v_rsi, a2, a2 + 10, (unsigned int)((unsigned int)(v_r13)));
loc_00A238BB:
    result = 4;
    if (((4) & ((unsigned __int8)(v_rbx))) != 0) {
        a3 = v_stack_m88;
        a1 = v_stack_m68;
        a2 = v_rsi;
        result = PspUnlockJobsAndProcessExclusive(a1, a2, a3, (unsigned int)((unsigned int)(v_r13)));
    }
    if ((((unsigned __int8)(v_rbx)) & (2)) != 0) {
        a1 = v_stack_m88;
        result = PspUnlockJobAssignment(a1, a2, a3, (unsigned int)((unsigned int)(v_r13)));
    }
    if ((((unsigned __int8)(v_rbx)) & (1)) != 0) {
        a2 = 0x624A7350ULL;
        a1 = v_rsi;
        result = ObfDereferenceObjectWithTag(a1, a2, a3, (unsigned int)((unsigned int)(v_r13)));
    }
    a1 = (v_stack_m40) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, (unsigned int)((unsigned int)(v_r13)));
    v_rsp = (v_rsp) + (160);
    return result;
loc_00A2391C:
    a3 = 0;
    v_stack_p20 = (int)(0);
    result = KeBugCheckEx(239, v_rsi, a3, a1);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PspAssignProcessToJob(void *Arg1, void *Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m58;
    uint64_t v_stack_m5F;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint8_t v_stack_m94;
    uint32_t v_stack_m98;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_p20;

    v_stack_p20 = local_rbx;
    local_rsp = (local_rsp) - (160);
    result = (*(uint64_t *)(v_rip + 0x3E73AD)) ^ (local_rsp);
    v_stack_m40 = result;
    v_stack_m94 = 0;
    result = 0;
    local_r14 = 0;
    v_stack_m80 = v_xmm0;
    v_stack_m70 = 0;
    local_rbx = 0;
    v_stack_m88 = *(uint64_t *)(gs_base + (0 + 0x188));
    v_stack_m48 = 0;
    v_stack_m98 = 0;
    v_stack_m68 = v_xmm0;
    v_stack_m58 = v_xmm0;
    local_rsi = Arg2;
    local_r13 = Arg3;
    if (Arg4 == 5) {
        local_r13 = *(uint64_t *)(arg2 + 0x2A0);
        Arg3 = v_stack_m80;
        Arg2 = *(uint64_t *)(gs_base + (0 + 0x188));
        Arg4 = 0;
        result = PspGetNextJobProcess(Arg1, Arg2, Arg3, Arg4);
        Arg2 = 0x624A7350ULL;
        Arg1 = result;
        local_rsi = result;
        result = ObfReferenceObjectWithTag(Arg1, Arg2, Arg3, Arg4);
        Arg4 = local_rsi;
        Arg3 = v_stack_m80;
        Arg2 = *(uint64_t *)(gs_base + (0 + 0x188));
        Arg1 = Arg1;
        local_rbx = 1;
        result = PspQuitNextJobProcess(Arg1, Arg2, Arg3, Arg4);
        local_r14 = v_stack_m98;
    }
    if (local_rsi == 0) goto loc_00A23443;
    result = ExAcquireRundownProtection(local_rsi + 488, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) != 0) goto loc_00A23440;
    goto loc_00A23879;
loc_00A23440:
    local_rbx = (uint8_t)((local_rbx) | (16));
loc_00A23443:
    v_stack_mB8 = v_stack_m68;
    result = PspGetJobLockHierarchyForAssignment(Arg1, local_rsi, (uint32_t)(0xC000010AULL), (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0xC000010AULL))))));
    local_rbx = (uint8_t)((local_rbx) | (6));
    result = PspLockJobAssignment(*(uint64_t *)(gs_base + (0 + 0x188)), local_rsi, (uint32_t)(0xC000010AULL), (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0xC000010AULL))))));
    result = PspLockJobsAndProcessExclusive(v_stack_m68, local_rsi, *(uint64_t *)(gs_base + (0 + 0x188)), 1);
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0xC000010AULL))))) != 5) goto loc_00A234C5;
    result = PspIsJobMovable(Arg1, local_rsi, *(uint64_t *)(gs_base + (0 + 0x188)), 1);
    if ((uint8_t)(result) != 0) goto loc_00A23498;
loc_00A2348E:
    goto loc_00A23873;
loc_00A23498:
    v_stack_m98 = 5;
    if ((*(uint64_t *)(local_rsi + 0x2A0)) != Arg1) goto loc_00A234B7;
    if (((*(uint32_t *)(local_rsi + 0x5FC)) & (0x1000ULL)) != 0) goto loc_00A2350E;
loc_00A234B7:
loc_00A234BC:
    goto loc_00A23873;
loc_00A234C5:
    result = PspGetJobAssignmentDisposition(Arg1, local_rsi, (uint32_t)(0xC000010AULL), v_stack_m98);
    if (sign_flag) goto loc_00A2348E;
    if (((uint32_t)((uint32_t)(v_stack_m98))) == ((uint32_t)((uint32_t)(0xC0000022ULL)))) goto loc_00A234EB;
    goto loc_00A23873;
loc_00A234EB:
    result = Feature_3033771320__private_IsEnabledDeviceUsageNoInline(Arg1, local_rsi, (uint32_t)(0xC000010AULL), v_stack_m98);
    if ((uint32_t)(result) == 0) goto loc_00A23544;
    if (((uint32_t)((uint32_t)(v_stack_m98))) != 4) goto loc_00A23544;
    if ((*(uint64_t *)(local_rsi + 0x2A0)) == v_stack_m60) goto loc_00A2350E;
    goto loc_00A234BC;
loc_00A2350E:
loc_00A23512:
    if (local_rsi == 0) goto loc_00A23528;
    local_r13 = (uint32_t)(0xC000010AULL);
    local_r14 = (uint32_t)(v_stack_m98);
    if (((uint32_t)((uint32_t)(v_stack_m98))) != 5) {
        local_r13 = *(uint64_t *)(local_rsi + 0x2A0);
        local_r14 = v_stack_m98;
    }
    result = PspValidateJobAssignmentUILimits(Arg1, local_r13, (uint32_t)((uint32_t)(local_r14)), v_stack_m98);
    if ((uint8_t)(result) != 0) goto loc_00A23551;
loc_00A2353A:
    goto loc_00A23873;
loc_00A23544:
    if (((uint32_t)(local_r14)) != 2) goto loc_00A23512;
    local_rdi = 0;
    goto loc_00A23873;
loc_00A23551:
    result = PspValidateJobAssignmentSiloPolicy(Arg1, local_r13, local_rsi, (uint32_t)((uint32_t)(local_r14)));
    if ((uint8_t)(result) == 0) goto loc_00A2353A;
    result = PspValidateJobAssignmentMemoryPartition(Arg1, local_r13, local_rsi, (uint32_t)((uint32_t)(local_r14)));
    if ((uint8_t)(result) == 0) goto loc_00A2353A;
    if (((uint32_t)(local_r14)) != 5) goto loc_00A2358C;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x420)))) & (1)) != 0) goto loc_00A2353A;
loc_00A2358C:
    if ((((uint32_t)((uint32_t)(0xFFFFFFFCULL))) & ((uint32_t)(local_r14 - 4))) != 0) goto loc_00A235AE;
    if (((uint32_t)(local_r14)) == 6) goto loc_00A235AE;
    result = (uint32_t)((*(uint8_t *)(local_r13 + 0x44E)) + 1);
    if (((uint32_t)(result)) > 100) goto loc_00A2353A;
loc_00A235AE:
    if ((((uint32_t)((uint32_t)(0xFFFFFFFCULL))) & ((uint32_t)(local_r14 - 4))) != 0) goto loc_00A235E7;
    if (((uint32_t)(local_r14)) == 6) goto loc_00A235E7;
    Arg1 = 0;
loc_00A235BE:
    if (((uint32_t)(Arg1 - 1)) <= 1) goto loc_00A235E0;
    if (((uint32_t)(Arg1 - 1)) >= 1) goto loc_00A235E0;
    if (((uint32_t)(Arg1 - 1)) < 1) goto loc_00A2353A;
loc_00A235E0:
    Arg1 = (uint32_t)((Arg1) + 1);
    if (((uint32_t)(Arg1)) < 3) goto loc_00A235BE;
loc_00A235E7:
    result = PspValidateJobAssignmentDiskIoAttribution(Arg1, local_r13, (uint32_t)((uint32_t)(local_r14)), (uint32_t)((uint32_t)(local_r14)));
    if ((uint8_t)(result) == 0) goto loc_00A2353A;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) - (1));
    if (condition_is_equal) goto loc_00A23625;
    Arg1 = (uint32_t)((Arg1) - (2));
    if (condition_is_equal) goto loc_00A23625;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A23621;
    if (((uint32_t)(Arg1)) == 1) goto loc_00A2361A;
    local_r12 = 0;
    goto loc_00A2364F;
loc_00A2361A:
    result = 0;
    goto loc_00A2362B;
loc_00A23621:
    result = 0;
    goto loc_00A23628;
loc_00A23625:
loc_00A23628:
loc_00A2362B:
    v_stack_m90 = local_r13;
    if (Arg1 == NULL) goto loc_00A2364F;
    Arg4 = 0;
    result = PspValidateJobChainLimits(Arg1, local_r13, local_rsi, Arg4);
    if (sign_flag) goto loc_00A2386F;
loc_00A2364F:
    result = PspEstablishJobHierarchy(Arg1, local_rsi, local_r13, (uint32_t)((uint32_t)(local_r14)));
    if (sign_flag) goto loc_00A2386F;
    if (local_rsi == 0) goto loc_00A2386D;
    if (((*(uint32_t *)(arg1 + 0x610)) & (0x1000ULL)) == 0) goto loc_00A2370D;
    local_rdi = 0;
loc_00A2368C:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsi + (int32_t)(0) * 4 + 0x728))) & ((uint32_t)((uint32_t)(0x7FFFFFFFULL))));
    result = (int32_t)(0);
    if (!(condition_is_equal)) {
        v_stack_mA8 = 0x626F4AULL;
        Arg3 = 0;
        Arg2 = local_r13;
        Arg4 = (uint32_t)(Arg1);
        Arg1 = Arg1;
        result = PspChargeJobWakeCounter(Arg1, Arg2, Arg3, Arg4);
    }
    local_rdi = (uint32_t)((local_rdi) + 1);
    if (((uint32_t)(local_rdi)) < 7) goto loc_00A2368C;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsi + 0x74C))) & ((uint32_t)((uint32_t)(0x7FFFFFFFULL))));
    if (!(condition_is_equal)) {
        v_stack_mA8 = 0x626F4AULL;
        Arg3 = 0;
        Arg2 = local_r13;
        Arg4 = (uint32_t)(result);
        Arg1 = Arg1;
        v_stack_mB8 = 4;
        result = PspChargeJobWakeCounter(Arg1, Arg2, Arg3, Arg4);
    }
loc_00A2370D:
    result = (result) | (-1);
    result = (uint8_t)((result) & (6));
    if (((uint8_t)(result)) == 2) {
        Arg1 = local_rsi + 456;
        result = ExfTryToWakePushLock(Arg1, Arg2, Arg3, Arg4);
    }
    result = KeAbPostRelease(local_rsi + 456, Arg2, Arg3, Arg4);
    local_rbx = (uint8_t)((local_rbx) | (8));
    Arg2 = v_stack_m90;
    if (((uint32_t)((uint32_t)(v_stack_m98))) == 4) { Arg2 = local_r13; }
    Arg4 = 0;
    result = PspIncrementJobChainProcessCounts(Arg1, Arg2, local_rsi, Arg4);
    result = PspApplyJobChainLimitsToProcess(Arg1, local_r13, local_rsi, Arg4);
    Arg2 = 0;
    result = PspUnlockJobsAndProcessExclusive(v_stack_m68, Arg2, v_stack_m88, Arg4);
    local_rbx = (uint8_t)((local_rbx) & (251));
    if (((*(uint32_t *)(arg1 + 0x610)) & ((uint32_t)((uint32_t)(0x1000000ULL)))) != 0) goto loc_00A237B4;
    Arg3 = 0;
    result = PsQueryProcessAttributes(local_rsi, v_stack_m94, Arg3, Arg4);
    if (v_stack_m94 != 0) goto loc_00A237A8;
    goto loc_00A237B0;
loc_00A237A8:
loc_00A237B0:
loc_00A237B4:
    result = PspApplyWorkingSetLimitsToProcess(local_rsi, v_stack_m94, Arg3, Arg4);
    if (sign_flag) goto loc_00A23873;
    Arg3 = 0;
    if (((uint32_t)((uint32_t)(v_stack_m98))) == 5) { Arg3 = (uint32_t)(Arg3 + 4); }
    result = MmAssignProcessToJob(local_rsi, local_r13, Arg3, Arg4);
    if ((uint32_t)(result) != 0) goto loc_00A237EE;
    goto loc_00A23873;
loc_00A237EE:
    result = PspUnlockJobAssignment(v_stack_m88, local_r13, Arg3, Arg4);
    result = (result) | (-1);
    local_rbx = (uint8_t)((local_rbx) & (253));
    result = Feature_ProcesDirectSwap__private_IsEnabledDeviceUsageNoInline(v_stack_m88, local_r13, Arg3, Arg4);
    if ((uint32_t)(result) != 0) goto loc_00A2381A;
    result = PspChangeProcessExecutionStateLegacy(local_rsi, local_r13, Arg3, Arg4);
    goto loc_00A2381F;
loc_00A2381A:
    result = PspChangeProcessExecutionState(local_rsi, local_r13, Arg3, Arg4);
loc_00A2381F:
    result = KiLeaveCriticalRegionUnsafe(v_stack_m88, local_r13, Arg3, Arg4);
    if ((*(uint32_t *)(arg1 + 0x220)) == 0) goto loc_00A2385D;
    result = kernel_indirect_call(v_stack_m88, local_r13, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00A2385D;
    if ((*(uint32_t *)(arg1 + 0x240)) <= -3) {
        Arg2 = local_rsi;
        Arg1 = Arg1;
        result = kernel_indirect_call(Arg1, Arg2, Arg3, Arg4);
    }
    if (((uint32_t)((uint32_t)(v_stack_m98))) != 5) goto loc_00A23873;
    local_rbx = (uint8_t)((local_rbx) | (32));
    goto loc_00A23873;
loc_00A2386D:
    local_rdi = 0;
loc_00A2386F:
loc_00A23873:
loc_00A23879:
    if ((((uint8_t)(local_rbx)) & (16)) != 0) {
        Arg1 = local_rsi + 488;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    if ((((uint8_t)(local_rbx)) & (32)) != 0) goto loc_00A238BB;
    if (!sign_flag) goto loc_00A238BB;
    if ((((uint8_t)(local_rbx)) & (8)) == 0) goto loc_00A238BB;
    if (((uint32_t)((uint32_t)(v_stack_m98))) == 5) goto loc_00A2391C;
    local_r13 = (uint32_t)(0xC000010AULL);
    if (0 != ((uint32_t)((uint32_t)(0xC000010AULL)))) { local_r13 = (uint32_t)((uint32_t)(0xC0000044ULL)); }
    Arg2 = 0;
    result = PspRemoveProcessFromJobChain(local_rsi, Arg2, Arg2 + 10, (uint32_t)((uint32_t)(local_r13)));
loc_00A238BB:
    result = 4;
    if (((4) & ((uint8_t)(local_rbx))) != 0) {
        Arg3 = v_stack_m88;
        Arg1 = v_stack_m68;
        Arg2 = local_rsi;
        result = PspUnlockJobsAndProcessExclusive(Arg1, Arg2, Arg3, (uint32_t)((uint32_t)(local_r13)));
    }
    if ((((uint8_t)(local_rbx)) & (2)) != 0) {
        Arg1 = v_stack_m88;
        result = PspUnlockJobAssignment(Arg1, Arg2, Arg3, (uint32_t)((uint32_t)(local_r13)));
    }
    if ((((uint8_t)(local_rbx)) & (1)) != 0) {
        Arg2 = 0x624A7350ULL;
        Arg1 = local_rsi;
        result = ObfDereferenceObjectWithTag(Arg1, Arg2, Arg3, (uint32_t)((uint32_t)(local_r13)));
    }
    Arg1 = (v_stack_m40) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, (uint32_t)((uint32_t)(local_r13)));
    local_rsp = (local_rsp) + (160);
    return result;
loc_00A2391C:
    Arg3 = 0;
    v_stack_p20 = (int32_t)(0);
    result = KeBugCheckEx(239, local_rsi, Arg3, Arg1);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x220` | `32` | `R` |
| `Arg1` | `+ 0x240` | `32` | `R` |
| `Arg1` | `+ 0x420` | `32` | `R` |
| `Arg1` | `+ 0x610` | `32` | `R` |
| `Arg1` | `+ 0x610` | `32` | `R/W` |
| `Arg2` | `+ 0x2A0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A23370&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
