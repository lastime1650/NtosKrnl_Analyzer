# NtQueryInformationFile

- RVA: `0x008AD630`–`0x008AE432` (길이 `3,586` bytes)
- VA: `0x00000001408AD630`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0007F8F0`
- 디코드: `782`개 명령, `3,586/3,586` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **50**; 고유 호출 대상: **34**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x008AD6FE` → [IopValidateQueryInformationParameters](IopValidateQueryInformationParameters_function_008AE440.md) (function, `0x008AE440`)
- `0x008AD73A` → [IopReferenceFileObject](../../text/29/IopReferenceFileObject_function_0029D530.md) (function, `0x0029D530`)
- `0x008AD778` → [IoGetRelatedDeviceObject](../../text/29/IoGetRelatedDeviceObject_function_0029B120.md) (function, `0x0029B120`)
- `0x008AD7DD` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x008AD808` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (function, `0x0020FA20`)
- `0x008AD86F` → [KeInitializeEvent](../../text/40/KeInitializeEvent_function_0040DD10.md) (function, `0x0040DD10`)
- `0x008AD87F` → [IopResetEvent](../../text/29/IopResetEvent_function_0029D5F0.md) (function, `0x0029D5F0`)
- `0x008AD88F` → [IopAllocateIrpExReturn](../../text/20/IopAllocateIrpExReturn_function_00207720.md) (function, `0x00207720`)
- `0x008AD95F` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008AD9A4` → [IopQueueThreadIrp](../../text/20/IopQueueThreadIrp_function_002075C0.md) (function, `0x002075C0`)
- `0x008ADA7E` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (function, `0x0020FA20`)
- `0x008ADAF2` → [IoGetIoPriorityHint](../../text/41/IoGetIoPriorityHint_function_00411ED0.md) (function, `0x00411ED0`)
- `0x008ADB45` → [IofCallDriver](../../text/29/IofCallDriver_function_0029B4B0.md) (function, `0x0029B4B0`)
- `0x008ADB56` → [ObDereferenceObjectDeferDelete](../../text/3F/ObDereferenceObjectDeferDelete_function_003FCE40.md) (function, `0x003FCE40`)
- `0x008ADBA9` → [IopReleaseFileObjectLock](../../text/25/IopReleaseFileObjectLock_function_00250A90.md) (function, `0x00250A90`)
- `0x008ADBB7` → [KeSetKernelStackSwapEnable](../../text/45/KeSetKernelStackSwapEnable_function_00450760.md) (function, `0x00450760`)
- `0x008ADBC9` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x008ADBEA` → [KeSetKernelStackSwapEnable](../../text/45/KeSetKernelStackSwapEnable_function_00450760.md) (function, `0x00450760`)
- `0x008ADC81` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x008ADC97` → [VfFastIoCheckState](../../pagevrfy/BB/VfFastIoCheckState_function_00BB9440.md) (function, `0x00BB9440`)
- `0x008ADCDA` → [MmIsDriverVerifying](../../text/4A/MmIsDriverVerifying_function_004A8770.md) (function, `0x004A8770`)
- `0x008ADCEC` → [VfFastIoSnapState](../../pagevrfy/BB/VfFastIoSnapState_function_00BB97BC.md) (function, `0x00BB97BC`)
- `0x008ADD6C` → [IopReleaseFileObjectLock](../../text/25/IopReleaseFileObjectLock_function_00250A90.md) (function, `0x00250A90`)
- `0x008ADD74` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008ADDC2` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (function, `0x0020E6B0`)
- `0x008ADE21` → [KiLowerIrqlProcessIrqlFlags](../../text/4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x008ADE41` → [IopCancelAlertedRequest](../A9/IopCancelAlertedRequest_function_00A948F8.md) (function, `0x00A948F8`)
- `0x008ADEF7` → [IopCompleteRequest](../../text/20/IopCompleteRequest_function_0020AF50.md) (function, `0x0020AF50`)
- `0x008ADF0C` → [KiLowerIrqlProcessIrqlFlags](../../text/4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x008ADF45` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (function, `0x0020E6B0`)
- `0x008ADFA6` → [IopGetFileVolumeNameInformation](../../text/4A/IopGetFileVolumeNameInformation_function_004A5EB4.md) (function, `0x004A5EB4`)
- `0x008ADFB0` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008ADFE3` → [IopExceptionCleanupEx](IopExceptionCleanupEx_function_008AE5C8.md) (function, `0x008AE5C8`)
- `0x008AE042` → [KiRaiseIrqlProcessIrqlFlags](../../text/4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x008AE079` → [KiRaiseIrqlProcessIrqlFlags](../../text/4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x008AE087` → [IoGetAttachedDevice](../../text/41/IoGetAttachedDevice_function_00410810.md) (function, `0x00410810`)
- `0x008AE09A` → [IopGetModeInformation](IopGetModeInformation_function_008AE684.md) (function, `0x008AE684`)
- `0x008AE0CF` → [IopWaitAndAcquireFileObjectLock](IopWaitAndAcquireFileObjectLock_function_008AE6D8.md) (function, `0x008AE6D8`)
- `0x008AE142` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008AE212` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008AE242` → [IoSetActivityIdThread](../../text/46/IoSetActivityIdThread_function_00466340.md) (function, `0x00466340`)
- `0x008AE250` → [IofCallDriver](../../text/29/IofCallDriver_function_0029B4B0.md) (function, `0x0029B4B0`)
- `0x008AE25C` → [IoSetActivityIdThread](../../text/46/IoSetActivityIdThread_function_00466340.md) (function, `0x00466340`)
- `0x008AE271` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008AE2C1` → [IopQueryProcessIdsUsingFile](../91/IopQueryProcessIdsUsingFile_function_0091D7A0.md) (function, `0x0091D7A0`)
- `0x008AE2FB` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008AE331` → [IopReleaseFileObjectLock](../../text/25/IopReleaseFileObjectLock_function_00250A90.md) (function, `0x00250A90`)
- `0x008AE33D` → [KeSetKernelStackSwapEnable](../../text/45/KeSetKernelStackSwapEnable_function_00450760.md) (function, `0x00450760`)
- `0x008AE3F9` → [IopGetNumaNodeInformation](../72/IopGetNumaNodeInformation_function_00720F68.md) (function, `0x00720F68`)
- `0x008AE428` → [IopCancelAlertedRequest](../A9/IopCancelAlertedRequest_function_00A948F8.md) (function, `0x00A948F8`)

### Direct callers
- [PfpFileCheckAttributesForPrefetch](../../text/47/PfpFileCheckAttributesForPrefetch_function_0047AF1C.md) at `0x0047AF47`
- [RtlIsPartialPlaceholderFileHandle](../79/RtlIsPartialPlaceholderFileHandle_function_00792C80.md) at `0x00792CAC`
- [SdbpGetFileTimestamp](../81/SdbpGetFileTimestamp_function_00812558.md) at `0x008126C5`
- [PfSnGetPrefetchInstructions](PfSnGetPrefetchInstructions_function_008AEBE4.md) at `0x008AED80`

### Static image references
- `0x008AD645` → RVA `0x00E0A740` (`.data`; read)
- `0x008AD717` → RVA `0x00B4E870` (`IopQueryOperationAccess`; read)
- `0x008ADC3B` → RVA `0x00F04A20` (`.data`; read)
- `0x008ADDF6` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x008AE11A` → RVA `0x00F8D20C` (`.data`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **42**
  - `0x008AD73A` → [IopReferenceFileObject](../../text/29/IopReferenceFileObject_function_0029D530.md) (`PAGE` → `.text`)
  - `0x008AD778` → [IoGetRelatedDeviceObject](../../text/29/IoGetRelatedDeviceObject_function_0029B120.md) (`PAGE` → `.text`)
  - `0x008AD7DD` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x008AD808` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (`PAGE` → `.text`)
  - `0x008AD86F` → [KeInitializeEvent](../../text/40/KeInitializeEvent_function_0040DD10.md) (`PAGE` → `.text`)
  - `0x008AD87F` → [IopResetEvent](../../text/29/IopResetEvent_function_0029D5F0.md) (`PAGE` → `.text`)
  - `0x008AD88F` → [IopAllocateIrpExReturn](../../text/20/IopAllocateIrpExReturn_function_00207720.md) (`PAGE` → `.text`)
  - `0x008AD95F` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008AD9A4` → [IopQueueThreadIrp](../../text/20/IopQueueThreadIrp_function_002075C0.md) (`PAGE` → `.text`)
  - `0x008ADA7E` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (`PAGE` → `.text`)
  - `0x008ADAF2` → [IoGetIoPriorityHint](../../text/41/IoGetIoPriorityHint_function_00411ED0.md) (`PAGE` → `.text`)
  - `0x008ADB45` → [IofCallDriver](../../text/29/IofCallDriver_function_0029B4B0.md) (`PAGE` → `.text`)
  - `0x008ADB56` → [ObDereferenceObjectDeferDelete](../../text/3F/ObDereferenceObjectDeferDelete_function_003FCE40.md) (`PAGE` → `.text`)
  - `0x008ADBA9` → [IopReleaseFileObjectLock](../../text/25/IopReleaseFileObjectLock_function_00250A90.md) (`PAGE` → `.text`)
  - `0x008ADBB7` → [KeSetKernelStackSwapEnable](../../text/45/KeSetKernelStackSwapEnable_function_00450760.md) (`PAGE` → `.text`)
  - `0x008ADBC9` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x008ADBEA` → [KeSetKernelStackSwapEnable](../../text/45/KeSetKernelStackSwapEnable_function_00450760.md) (`PAGE` → `.text`)
  - `0x008ADC81` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x008ADC97` → [VfFastIoCheckState](../../pagevrfy/BB/VfFastIoCheckState_function_00BB9440.md) (`PAGE` → `PAGEVRFY`)
  - `0x008ADCDA` → [MmIsDriverVerifying](../../text/4A/MmIsDriverVerifying_function_004A8770.md) (`PAGE` → `.text`)
  - `0x008ADCEC` → [VfFastIoSnapState](../../pagevrfy/BB/VfFastIoSnapState_function_00BB97BC.md) (`PAGE` → `PAGEVRFY`)
  - `0x008ADD6C` → [IopReleaseFileObjectLock](../../text/25/IopReleaseFileObjectLock_function_00250A90.md) (`PAGE` → `.text`)
  - `0x008ADD74` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008ADDC2` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (`PAGE` → `.text`)
  - `0x008ADE21` → [KiLowerIrqlProcessIrqlFlags](../../text/4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (`PAGE` → `.text`)
  - `0x008ADEF7` → [IopCompleteRequest](../../text/20/IopCompleteRequest_function_0020AF50.md) (`PAGE` → `.text`)
  - `0x008ADF0C` → [KiLowerIrqlProcessIrqlFlags](../../text/4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (`PAGE` → `.text`)
  - `0x008ADF45` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (`PAGE` → `.text`)
  - `0x008ADFA6` → [IopGetFileVolumeNameInformation](../../text/4A/IopGetFileVolumeNameInformation_function_004A5EB4.md) (`PAGE` → `.text`)
  - `0x008ADFB0` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008AE042` → [KiRaiseIrqlProcessIrqlFlags](../../text/4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (`PAGE` → `.text`)
  - `0x008AE079` → [KiRaiseIrqlProcessIrqlFlags](../../text/4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (`PAGE` → `.text`)
  - `0x008AE087` → [IoGetAttachedDevice](../../text/41/IoGetAttachedDevice_function_00410810.md) (`PAGE` → `.text`)
  - `0x008AE142` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008AE212` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008AE242` → [IoSetActivityIdThread](../../text/46/IoSetActivityIdThread_function_00466340.md) (`PAGE` → `.text`)
  - `0x008AE250` → [IofCallDriver](../../text/29/IofCallDriver_function_0029B4B0.md) (`PAGE` → `.text`)
  - `0x008AE25C` → [IoSetActivityIdThread](../../text/46/IoSetActivityIdThread_function_00466340.md) (`PAGE` → `.text`)
  - `0x008AE271` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008AE2FB` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008AE331` → [IopReleaseFileObjectLock](../../text/25/IopReleaseFileObjectLock_function_00250A90.md) (`PAGE` → `.text`)
  - `0x008AE33D` → [KeSetKernelStackSwapEnable](../../text/45/KeSetKernelStackSwapEnable_function_00450760.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x008AE379` → [sub_00B1A566](../B1/Unknown_function_00B1A566.md) (`tail-transfer`)
  - `0x008AE386` → [sub_00B1A566](../B1/Unknown_function_00B1A566.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
008AD630  4C 8B DC                        mov r11, rsp
008AD633  53                              push rbx
008AD634  56                              push rsi
008AD635  57                              push rdi
008AD636  41 54                           push r12
008AD638  41 55                           push r13
008AD63A  41 56                           push r14
008AD63C  41 57                           push r15
008AD63E  48 81 EC 30 01 00 00            sub rsp, 0x130
008AD645  48 8B 05 F4 D0 55 00            mov rax, qword ptr [rip + 0x55d0f4]
008AD64C  48 33 C4                        xor rax, rsp
008AD64F  48 89 84 24 28 01 00 00         mov qword ptr [rsp + 0x128], rax
008AD657  45 8B F1                        mov r14d, r9d
008AD65A  44 89 4C 24 4C                  mov dword ptr [rsp + 0x4c], r9d
008AD65F  4D 8B E8                        mov r13, r8
008AD662  4C 89 44 24 70                  mov qword ptr [rsp + 0x70], r8
008AD667  48 89 54 24 50                  mov qword ptr [rsp + 0x50], rdx
008AD66C  48 8B F9                        mov rdi, rcx
008AD66F  48 89 94 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], rdx
008AD677  48 89 94 24 80 00 00 00         mov qword ptr [rsp + 0x80], rdx
008AD67F  48 89 94 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rdx
008AD687  4C 89 84 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], r8
008AD68F  44 89 4C 24 60                  mov dword ptr [rsp + 0x60], r9d
008AD694  8B 9C 24 90 01 00 00            mov ebx, dword ptr [rsp + 0x190]
008AD69B  89 5C 24 58                     mov dword ptr [rsp + 0x58], ebx
008AD69F  33 F6                           xor esi, esi
008AD6A1  48 89 74 24 40                  mov qword ptr [rsp + 0x40], rsi
008AD6A6  0F 57 C0                        xorps xmm0, xmm0
008AD6A9  33 C0                           xor eax, eax
008AD6AB  41 0F 11 43 98                  movups xmmword ptr [r11 - 0x68], xmm0
008AD6B0  49 89 43 A8                     mov qword ptr [r11 - 0x58], rax
008AD6B4  41 0F 11 43 88                  movups xmmword ptr [r11 - 0x78], xmm0
008AD6B9  49 89 B3 28 FF FF FF            mov qword ptr [r11 - 0xd8], rsi
008AD6C0  88 44 24 34                     mov byte ptr [rsp + 0x34], al
008AD6C4  88 44 24 32                     mov byte ptr [rsp + 0x32], al
008AD6C8  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008AD6D1  48 89 84 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rax
008AD6D9  0F B6 88 32 02 00 00            movzx ecx, byte ptr [rax + 0x232]
008AD6E0  88 4C 24 33                     mov byte ptr [rsp + 0x33], cl
008AD6E4  44 0F B6 E1                     movzx r12d, cl
008AD6E8  88 4C 24 3A                     mov byte ptr [rsp + 0x3a], cl
008AD6EC  89 5C 24 28                     mov dword ptr [rsp + 0x28], ebx
008AD6F0  44 89 4C 24 20                  mov dword ptr [rsp + 0x20], r9d
008AD6F5  4D 8B C8                        mov r9, r8
008AD6F8  4C 8B C2                        mov r8, rdx
008AD6FB  48 8B D0                        mov rdx, rax
008AD6FE  E8 3D 0D 00 00                  call 0x1408ae440
008AD703  85 C0                           test eax, eax
008AD705  0F 88 B3 04 00 00               js 0x1408adbbe
008AD70B  45 84 E4                        test r12b, r12b
008AD70E  0F 84 FC 08 00 00               je 0x1408ae010
008AD714  48 63 D3                        movsxd rdx, ebx
008AD717  48 8D 0D 52 11 2A 00            lea rcx, [rip + 0x2a1152]
008AD71E  48 8D 84 24 90 00 00 00         lea rax, [rsp + 0x90]
008AD726  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008AD72B  4C 8D 4C 24 40                  lea r9, [rsp + 0x40]
008AD730  45 0F B6 C4                     movzx r8d, r12b
008AD734  8B 14 91                        mov edx, dword ptr [rcx + rdx*4]
008AD737  48 8B CF                        mov rcx, rdi
008AD73A  E8 F1 FD 9E FF                  call 0x14029d530
008AD73F  44 8B F8                        mov r15d, eax
008AD742  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
008AD746  85 C0                           test eax, eax
008AD748  0F 88 70 04 00 00               js 0x1408adbbe
008AD74E  83 FB 08                        cmp ebx, 8
008AD751  0F 84 5A 0A 00 00               je 0x1408ae1b1
008AD757  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
008AD75C  4C 8D 77 50                     lea r14, [rdi + 0x50]
008AD760  4C 89 B4 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], r14
008AD768  41 F7 06 00 08 00 00            test dword ptr [r14], 0x800
008AD76F  0F 85 0E 09 00 00               jne 0x1408ae083
008AD775  48 8B CF                        mov rcx, rdi
008AD778  E8 A3 D9 9E FF                  call 0x14029b120
008AD77D  4C 8B E8                        mov r13, rax
008AD780  48 89 84 24 88 00 00 00         mov qword ptr [rsp + 0x88], rax
008AD788  48 8B 40 08                     mov rax, qword ptr [rax + 8]
008AD78C  48 8B 40 50                     mov rax, qword ptr [rax + 0x50]
008AD790  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
008AD795  83 FB 33                        cmp ebx, 0x33
008AD798  0F 84 B3 09 00 00               je 0x1408ae151
008AD79E  83 FB 3A                        cmp ebx, 0x3a
008AD7A1  0F 84 EC 07 00 00               je 0x1408adf93
008AD7A7  41 8B 36                        mov esi, dword ptr [r14]
008AD7AA  45 33 C0                        xor r8d, r8d
008AD7AD  40 F6 C6 02                     test sil, 2
008AD7B1  0F 84 AB 00 00 00               je 0x1408ad862
008AD7B7  C1 EE 02                        shr esi, 2
008AD7BA  40 80 E6 01                     and sil, 1
008AD7BE  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008AD7C7  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
008AD7CE  90                              nop
008AD7CF  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
008AD7D4  48 8D 8F 80 00 00 00            lea rcx, [rdi + 0x80]
008AD7DB  33 D2                           xor edx, edx
008AD7DD  E8 4E 2A 96 FF                  call 0x140210230
008AD7E2  C6 44 24 37 00                  mov byte ptr [rsp + 0x37], 0
008AD7E7  B9 01 00 00 00                  mov ecx, 1
008AD7EC  87 4F 74                        xchg dword ptr [rdi + 0x74], ecx
008AD7EF  85 C9                           test ecx, ecx
008AD7F1  0F 85 BB 08 00 00               jne 0x1408ae0b2
008AD7F7  48 85 C0                        test rax, rax
008AD7FA  74 04                           je 0x1408ad800
008AD7FC  C6 40 0A 01                     mov byte ptr [rax + 0xa], 1
008AD800  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
008AD805  48 8B CF                        mov rcx, rdi
008AD808  E8 13 22 96 FF                  call 0x14020fa20
008AD80D  45 33 FF                        xor r15d, r15d
008AD810  44 89 7C 24 48                  mov dword ptr [rsp + 0x48], r15d
008AD815  80 7C 24 37 00                  cmp byte ptr [rsp + 0x37], 0
008AD81A  0F 85 51 05 00 00               jne 0x1408add71
008AD820  83 FB 0E                        cmp ebx, 0xe
008AD823  0F 84 22 06 00 00               je 0x1408ade4b
008AD829  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
008AD82E  48 85 C0                        test rax, rax
008AD831  74 2A                           je 0x1408ad85d
008AD833  48 8B 70 20                     mov rsi, qword ptr [rax + 0x20]
008AD837  48 89 B4 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rsi
008AD83F  48 8B 40 28                     mov rax, qword ptr [rax + 0x28]
008AD843  48 89 84 24 98 00 00 00         mov qword ptr [rsp + 0x98], rax
008AD84B  83 FB 04                        cmp ebx, 4
008AD84E  0F 84 D8 07 00 00               je 0x1408ae02c
008AD854  83 FB 05                        cmp ebx, 5
008AD857  0F 84 C0 03 00 00               je 0x1408adc1d
008AD85D  41 B7 01                        mov r15b, 1
008AD860  EB 15                           jmp 0x1408ad877
008AD862  BA 01 00 00 00                  mov edx, 1
008AD867  48 8D 8C 24 00 01 00 00         lea rcx, [rsp + 0x100]
008AD86F  E8 9C 04 B6 FF                  call 0x14040dd10
008AD874  45 32 FF                        xor r15b, r15b
008AD877  44 88 7C 24 31                  mov byte ptr [rsp + 0x31], r15b
008AD87C  48 8B CF                        mov rcx, rdi
008AD87F  E8 6C FD 9E FF                  call 0x14029d5f0
008AD884  45 33 C0                        xor r8d, r8d
008AD887  41 0F B6 55 4C                  movzx edx, byte ptr [r13 + 0x4c]
008AD88C  49 8B CD                        mov rcx, r13
008AD88F  E8 8C 9E 95 FF                  call 0x140207720
008AD894  48 8B C8                        mov rcx, rax
008AD897  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
008AD89C  48 8B F0                        mov rsi, rax
008AD89F  48 89 84 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rax
008AD8A7  48 89 84 24 E8 00 00 00         mov qword ptr [rsp + 0xe8], rax
008AD8AF  48 85 C0                        test rax, rax
008AD8B2  0F 84 7C 08 00 00               je 0x1408ae134
008AD8B8  48 89 B8 C0 00 00 00            mov qword ptr [rax + 0xc0], rdi
008AD8BF  48 8D 90 98 00 00 00            lea rdx, [rax + 0x98]
008AD8C6  48 89 54 24 68                  mov qword ptr [rsp + 0x68], rdx
008AD8CB  48 8B 84 24 C0 00 00 00         mov rax, qword ptr [rsp + 0xc0]
008AD8D3  48 89 02                        mov qword ptr [rdx], rax
008AD8D6  48 8D 41 40                     lea rax, [rcx + 0x40]
008AD8DA  48 89 84 24 98 00 00 00         mov qword ptr [rsp + 0x98], rax
008AD8E2  44 88 20                        mov byte ptr [rax], r12b
008AD8E5  45 84 FF                        test r15b, r15b
008AD8E8  0F 84 F4 02 00 00               je 0x1408adbe2
008AD8EE  80 49 47 02                     or byte ptr [rcx + 0x47], 2
008AD8F2  33 D2                           xor edx, edx
008AD8F4  48 8D 41 10                     lea rax, [rcx + 0x10]
008AD8F8  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
008AD8FD  48 89 84 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rax
008AD905  48 89 51 50                     mov qword ptr [rcx + 0x50], rdx
008AD909  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
008AD911  48 89 41 48                     mov qword ptr [rcx + 0x48], rax
008AD915  48 C7 46 58 00 00 00 00         mov qword ptr [rsi + 0x58], 0
008AD91D  48 8B 86 B8 00 00 00            mov rax, qword ptr [rsi + 0xb8]
008AD924  48 83 E8 48                     sub rax, 0x48
008AD928  48 89 84 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rax
008AD930  C6 00 05                        mov byte ptr [rax], 5
008AD933  48 89 78 30                     mov qword ptr [rax + 0x30], rdi
008AD937  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
008AD93C  48 89 46 70                     mov qword ptr [rsi + 0x70], rax
008AD940  48 C7 46 18 00 00 00 00         mov qword ptr [rsi + 0x18], 0
008AD948  48 C7 46 08 00 00 00 00         mov qword ptr [rsi + 8], 0
008AD950  8B 54 24 4C                     mov edx, dword ptr [rsp + 0x4c]
008AD954  B9 41 00 00 00                  mov ecx, 0x41
008AD959  41 B8 49 6F 53 42               mov r8d, 0x42536f49
008AD95F  E8 8C 47 2D 00                  call 0x140b820f0
008AD964  48 89 46 18                     mov qword ptr [rsi + 0x18], rax
008AD968  48 85 C0                        test rax, rax
008AD96B  0F 84 5B 06 00 00               je 0x1408adfcc
008AD971  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
008AD976  48 89 84 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rax
008AD97E  81 08 70 08 00 00               or dword ptr [rax], 0x870
008AD984  48 8B 84 24 C0 00 00 00         mov rax, qword ptr [rsp + 0xc0]
008AD98C  8B 4C 24 4C                     mov ecx, dword ptr [rsp + 0x4c]
008AD990  89 48 08                        mov dword ptr [rax + 8], ecx
008AD993  89 58 10                        mov dword ptr [rax + 0x10], ebx
008AD996  80 7C 24 32 00                  cmp byte ptr [rsp + 0x32], 0
008AD99B  0F 85 A6 09 00 00               jne 0x1408ae347
008AD9A1  48 8B CE                        mov rcx, rsi
008AD9A4  E8 17 9C 95 FF                  call 0x1402075c0
008AD9A9  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008AD9B2  48 FF 80 90 03 00 00            inc qword ptr [rax + 0x390]
008AD9B9  65 FF 04 25 E4 2E 00 00         inc dword ptr gs:[0x2ee4]
008AD9C1  45 32 D2                        xor r10b, r10b
008AD9C4  33 FF                           xor edi, edi
008AD9C6  83 FB 10                        cmp ebx, 0x10
008AD9C9  0F 84 C2 06 00 00               je 0x1408ae091
008AD9CF  83 FB 11                        cmp ebx, 0x11
008AD9D2  0F 84 78 09 00 00               je 0x1408ae350
008AD9D8  83 FB 29                        cmp ebx, 0x29
008AD9DB  0F 84 89 09 00 00               je 0x1408ae36a
008AD9E1  83 FB 2B                        cmp ebx, 0x2b
008AD9E4  0F 84 94 08 00 00               je 0x1408ae27e
008AD9EA  83 FB 2F                        cmp ebx, 0x2f
008AD9ED  0F 84 B7 08 00 00               je 0x1408ae2aa
008AD9F3  83 FB 35                        cmp ebx, 0x35
008AD9F6  0F 84 F4 09 00 00               je 0x1408ae3f0
008AD9FC  83 FB 12                        cmp ebx, 0x12
008AD9FF  75 62                           jne 0x1408ada63
008ADA01  4C 8B 4E 18                     mov r9, qword ptr [rsi + 0x18]
008ADA05  8B 84 24 94 00 00 00            mov eax, dword ptr [rsp + 0x94]
008ADA0C  41 89 41 4C                     mov dword ptr [r9 + 0x4c], eax
008ADA10  45 8B 06                        mov r8d, dword ptr [r14]
008ADA13  41 8B C8                        mov ecx, r8d
008ADA16  C1 E9 03                        shr ecx, 3
008ADA19  83 E1 02                        and ecx, 2
008ADA1C  8B D1                           mov edx, ecx
008ADA1E  83 CA 04                        or edx, 4
008ADA21  41 F6 C0 20                     test r8b, 0x20
008ADA25  0F 44 D1                        cmove edx, ecx
008ADA28  8B CA                           mov ecx, edx
008ADA2A  83 C9 08                        or ecx, 8
008ADA2D  41 F6 C0 08                     test r8b, 8
008ADA31  0F 44 CA                        cmove ecx, edx
008ADA34  41 F6 C0 02                     test r8b, 2
008ADA38  0F 85 4D 03 00 00               jne 0x1408add8b
008ADA3E  8B C1                           mov eax, ecx
008ADA40  0F BA E8 0C                     bts eax, 0xc
008ADA44  41 0F BA E0 10                  bt r8d, 0x10
008ADA49  0F 43 C1                        cmovae eax, ecx
008ADA4C  41 89 41 58                     mov dword ptr [r9 + 0x58], eax
008ADA50  41 8B 85 98 00 00 00            mov eax, dword ptr [r13 + 0x98]
008ADA57  41 89 41 5C                     mov dword ptr [r9 + 0x5c], eax
008ADA5B  48 C7 46 38 0C 00 00 00         mov qword ptr [rsi + 0x38], 0xc
008ADA63  4C 8B 74 24 60                  mov r14, qword ptr [rsp + 0x60]
008ADA68  45 84 D2                        test r10b, r10b
008ADA6B  0F 85 39 06 00 00               jne 0x1408ae0aa
008ADA71  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
008ADA76  45 84 FF                        test r15b, r15b
008ADA79  75 08                           jne 0x1408ada83
008ADA7B  48 8B CF                        mov rcx, rdi
008ADA7E  E8 9D 1F 96 FF                  call 0x14020fa20
008ADA83  48 8B 9F D0 00 00 00            mov rbx, qword ptr [rdi + 0xd0]
008ADA8A  48 85 DB                        test rbx, rbx
008ADA8D  0F 85 6A 05 00 00               jne 0x1408adffd
008ADA93  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
008ADA9C  8B 99 A0 05 00 00               mov ebx, dword ptr [rcx + 0x5a0]
008ADAA2  C1 EB 09                        shr ebx, 9
008ADAA5  83 E3 07                        and ebx, 7
008ADAA8  48 8B 81 20 02 00 00            mov rax, qword ptr [rcx + 0x220]
008ADAAF  48 8B 80 A0 02 00 00            mov rax, qword ptr [rax + 0x2a0]
008ADAB6  48 85 C0                        test rax, rax
008ADAB9  74 0B                           je 0x1408adac6
008ADABB  8B 80 3C 04 00 00               mov eax, dword ptr [rax + 0x43c]
008ADAC1  3B D8                           cmp ebx, eax
008ADAC3  0F 4D D8                        cmovge ebx, eax
008ADAC6  83 FB 02                        cmp ebx, 2
008ADAC9  0F 8C 7D 05 00 00               jl 0x1408ae04c
008ADACF  C1 E3 11                        shl ebx, 0x11
008ADAD2  81 C3 00 00 02 00               add ebx, 0x20000
008ADAD8  41 8B 06                        mov eax, dword ptr [r14]
008ADADB  25 FF FF F1 FF                  and eax, 0xfff1ffff
008ADAE0  0B D8                           or ebx, eax
008ADAE2  41 89 06                        mov dword ptr [r14], eax
008ADAE5  48 8B 84 24 A0 00 00 00         mov rax, qword ptr [rsp + 0xa0]
008ADAED  89 18                           mov dword ptr [rax], ebx
008ADAEF  48 8B CE                        mov rcx, rsi
008ADAF2  E8 D9 43 B6 FF                  call 0x140411ed0
008ADAF7  48 8B 8C 24 98 00 00 00         mov rcx, qword ptr [rsp + 0x98]
008ADAFF  83 F8 02                        cmp eax, 2
008ADB02  0F 8C E1 05 00 00               jl 0x1408ae0e9
008ADB08  80 7E 47 00                     cmp byte ptr [rsi + 0x47], 0
008ADB0C  7C 10                           jl 0x1408adb1e
008ADB0E  48 8B 86 C8 00 00 00            mov rax, qword ptr [rsi + 0xc8]
008ADB15  48 85 C0                        test rax, rax
008ADB18  0F 85 65 04 00 00               jne 0x1408adf83
008ADB1E  32 C9                           xor cl, cl
008ADB20  48 8B 84 24 E8 00 00 00         mov rax, qword ptr [rsp + 0xe8]
008ADB28  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
008ADB2D  B8 C8 00 00 00                  mov eax, 0xc8
008ADB32  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
008ADB37  84 C9                           test cl, cl
008ADB39  0F 85 E0 06 00 00               jne 0x1408ae21f
008ADB3F  48 8B D6                        mov rdx, rsi
008ADB42  49 8B CD                        mov rcx, r13
008ADB45  E8 66 D9 9E FF                  call 0x14029b4b0
008ADB4A  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
008ADB4E  45 84 FF                        test r15b, r15b
008ADB51  75 08                           jne 0x1408adb5b
008ADB53  48 8B CF                        mov rcx, rdi
008ADB56  E8 E5 F2 B4 FF                  call 0x1403fce40
008ADB5B  8B 7C 24 58                     mov edi, dword ptr [rsp + 0x58]
008ADB5F  81 FF 03 01 00 00               cmp edi, 0x103
008ADB65  0F 85 32 03 00 00               jne 0x1408ade9d
008ADB6B  45 84 FF                        test r15b, r15b
008ADB6E  0F 84 B7 03 00 00               je 0x1408adf2b
008ADB74  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
008ADB79  44 8B 77 50                     mov r14d, dword ptr [rdi + 0x50]
008ADB7D  41 83 E6 04                     and r14d, 4
008ADB81  41 BD 01 00 00 00               mov r13d, 1
008ADB87  F6 87 98 00 00 00 7F            test byte ptr [rdi + 0x98], 0x7f
008ADB8E  0F 85 09 02 00 00               jne 0x1408add9d
008ADB94  83 BF 9C 00 00 00 00            cmp dword ptr [rdi + 0x9c], 0
008ADB9B  0F 84 FC 01 00 00               je 0x1408add9d
008ADBA1  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
008ADBA6  8B 79 38                        mov edi, dword ptr [rcx + 0x38]
008ADBA9  E8 E2 2E 9A FF                  call 0x140250a90
008ADBAE  80 7C 24 34 00                  cmp byte ptr [rsp + 0x34], 0
008ADBB3  74 07                           je 0x1408adbbc
008ADBB5  B1 01                           mov cl, 1
008ADBB7  E8 A4 2B BA FF                  call 0x140450760
008ADBBC  8B C7                           mov eax, edi
008ADBBE  48 8B 8C 24 28 01 00 00         mov rcx, qword ptr [rsp + 0x128]
008ADBC6  48 33 CC                        xor rcx, rsp
008ADBC9  E8 72 EA DF FF                  call 0x1406ac640
008ADBCE  48 81 C4 30 01 00 00            add rsp, 0x130
008ADBD5  41 5F                           pop r15
008ADBD7  41 5E                           pop r14
008ADBD9  41 5D                           pop r13
008ADBDB  41 5C                           pop r12
008ADBDD  5F                              pop rdi
008ADBDE  5E                              pop rsi
008ADBDF  5B                              pop rbx
008ADBE0  C3                              ret
008ADBE1  CC                              int3
008ADBE2  41 80 FC 01                     cmp r12b, 1
008ADBE6  75 0E                           jne 0x1408adbf6
008ADBE8  33 C9                           xor ecx, ecx
008ADBEA  E8 71 2B BA FF                  call 0x140450760
008ADBEF  88 44 24 34                     mov byte ptr [rsp + 0x34], al
008ADBF3  48 8B CE                        mov rcx, rsi
008ADBF6  48 8D 46 10                     lea rax, [rsi + 0x10]
008ADBFA  C7 00 04 00 00 00               mov dword ptr [rax], 4
008ADC00  48 8D 94 24 F0 00 00 00         lea rdx, [rsp + 0xf0]
008ADC08  48 89 94 24 80 00 00 00         mov qword ptr [rsp + 0x80], rdx
008ADC10  48 8D 94 24 00 01 00 00         lea rdx, [rsp + 0x100]
008ADC18  E9 DB FC FF FF                  jmp 0x1408ad8f8
008ADC1D  48 85 C0                        test rax, rax
008ADC20  0F 84 37 FC FF FF               je 0x1408ad85d
008ADC26  0F 57 C0                        xorps xmm0, xmm0
008ADC29  0F 11 84 24 D0 00 00 00         movups xmmword ptr [rsp + 0xd0], xmm0
008ADC31  C6 44 24 30 00                  mov byte ptr [rsp + 0x30], 0
008ADC36  C6 44 24 39 00                  mov byte ptr [rsp + 0x39], 0
008ADC3B  8B 05 DF 6D 65 00               mov eax, dword ptr [rip + 0x656ddf]
008ADC41  A8 10                           test al, 0x10
008ADC43  0F 85 85 00 00 00               jne 0x1408adcce
008ADC49  33 C0                           xor eax, eax
008ADC4B  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
008ADC50  48 89 84 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], rax
008ADC58  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
008ADC5D  4C 8D 8C 24 D0 00 00 00         lea r9, [rsp + 0xd0]
008ADC65  4C 8B 44 24 70                  mov r8, qword ptr [rsp + 0x70]
008ADC6A  B2 01                           mov dl, 1
008ADC6C  48 8B CF                        mov rcx, rdi
008ADC6F  83 FB 04                        cmp ebx, 4
008ADC72  74 0A                           je 0x1408adc7e
008ADC74  48 8B 84 24 98 00 00 00         mov rax, qword ptr [rsp + 0x98]
008ADC7C  EB 03                           jmp 0x1408adc81
008ADC7E  48 8B C6                        mov rax, rsi
008ADC81  E8 4A CE E0 FF                  call 0x1406baad0
008ADC86  88 44 24 30                     mov byte ptr [rsp + 0x30], al
008ADC8A  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
008ADC8F  48 85 C9                        test rcx, rcx
008ADC92  74 0D                           je 0x1408adca1
008ADC94  48 8B D6                        mov rdx, rsi
008ADC97  E8 A4 B7 30 00                  call 0x140bb9440
008ADC9C  0F B6 44 24 30                  movzx eax, byte ptr [rsp + 0x30]
008ADCA1  84 C0                           test al, al
008ADCA3  74 51                           je 0x1408adcf6
008ADCA5  44 8B BC 24 D0 00 00 00         mov r15d, dword ptr [rsp + 0xd0]
008ADCAD  44 89 7C 24 48                  mov dword ptr [rsp + 0x48], r15d
008ADCB2  C6 44 24 39 01                  mov byte ptr [rsp + 0x39], 1
008ADCB7  0F 10 84 24 D0 00 00 00         movups xmm0, xmmword ptr [rsp + 0xd0]
008ADCBF  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
008ADCC4  0F 11 00                        movups xmmword ptr [rax], xmm0
008ADCC7  0F B6 44 24 30                  movzx eax, byte ptr [rsp + 0x30]
008ADCCC  EB 28                           jmp 0x1408adcf6
008ADCCE  49 8B 45 08                     mov rax, qword ptr [r13 + 8]
008ADCD2  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
008ADCD7  48 8B C8                        mov rcx, rax
008ADCDA  E8 91 AA BF FF                  call 0x1404a8770
008ADCDF  85 C0                           test eax, eax
008ADCE1  0F 84 62 FF FF FF               je 0x1408adc49
008ADCE7  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
008ADCEC  E8 CB BA 30 00                  call 0x140bb97bc
008ADCF1  E9 55 FF FF FF                  jmp 0x1408adc4b
008ADCF6  EB 69                           jmp 0x1408add61
008ADCF8  44 8B F8                        mov r15d, eax
008ADCFB  80 7C 24 39 00                  cmp byte ptr [rsp + 0x39], 0
008ADD00  75 7F                           jne 0x1408add81
008ADD02  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
008ADD06  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
008ADD0B  4C 8B AC 24 88 00 00 00         mov r13, qword ptr [rsp + 0x88]
008ADD13  44 0F B6 64 24 3A               movzx r12d, byte ptr [rsp + 0x3a]
008ADD19  4C 8B B4 24 A8 00 00 00         mov r14, qword ptr [rsp + 0xa8]
008ADD21  48 8B 84 24 C8 00 00 00         mov rax, qword ptr [rsp + 0xc8]
008ADD29  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
008ADD2E  48 8B 84 24 B0 00 00 00         mov rax, qword ptr [rsp + 0xb0]
008ADD36  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
008ADD3B  8B 44 24 60                     mov eax, dword ptr [rsp + 0x60]
008ADD3F  89 44 24 4C                     mov dword ptr [rsp + 0x4c], eax
008ADD43  8B 5C 24 58                     mov ebx, dword ptr [rsp + 0x58]
008ADD47  48 8B 84 24 B8 00 00 00         mov rax, qword ptr [rsp + 0xb8]
008ADD4F  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
008ADD57  44 88 64 24 33                  mov byte ptr [rsp + 0x33], r12b
008ADD5C  0F B6 44 24 30                  movzx eax, byte ptr [rsp + 0x30]
008ADD61  84 C0                           test al, al
008ADD63  0F 84 F4 FA FF FF               je 0x1408ad85d
008ADD69  48 8B CF                        mov rcx, rdi
008ADD6C  E8 1F 2D 9A FF                  call 0x140250a90
008ADD71  48 8B CF                        mov rcx, rdi
008ADD74  E8 D7 B5 A4 FF                  call 0x1402f9350
008ADD79  41 8B C7                        mov eax, r15d
008ADD7C  E9 3D FE FF FF                  jmp 0x1408adbbe
008ADD81  44 8B 7C 24 48                  mov r15d, dword ptr [rsp + 0x48]
008ADD86  E9 7B FF FF FF                  jmp 0x1408add06
008ADD8B  41 F6 C0 04                     test r8b, 4
008ADD8F  0F 85 14 04 00 00               jne 0x1408ae1a9
008ADD95  83 C9 20                        or ecx, 0x20
008ADD98  E9 A1 FC FF FF                  jmp 0x1408ada3e
008ADD9D  45 33 C0                        xor r8d, r8d
008ADDA0  0F B6 44 24 33                  movzx eax, byte ptr [rsp + 0x33]
008ADDA5  45 85 F6                        test r14d, r14d
008ADDA8  44 0F 45 C0                     cmovne r8d, eax
008ADDAC  48 C7 44 24 20 00 00 00 00      mov qword ptr [rsp + 0x20], 0
008ADDB5  45 0F B6 CD                     movzx r9d, r13b
008ADDB9  33 D2                           xor edx, edx
008ADDBB  48 8D 8F 98 00 00 00            lea rcx, [rdi + 0x98]
008ADDC2  E8 E9 08 96 FF                  call 0x14020e6b0
008ADDC7  3D C0 00 00 00                  cmp eax, 0xc0
008ADDCC  0F 85 EA 01 00 00               jne 0x1408adfbc
008ADDD2  45 85 F6                        test r14d, r14d
008ADDD5  75 60                           jne 0x1408ade37
008ADDD7  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008ADDE0  8B 88 A0 05 00 00               mov ecx, dword ptr [rax + 0x5a0]
008ADDE6  41 84 CD                        test r13b, cl
008ADDE9  75 4C                           jne 0x1408ade37
008ADDEB  45 32 E4                        xor r12b, r12b
008ADDEE  45 0F 20 C7                     mov r15, cr8
008ADDF2  45 0F 22 C5                     mov cr8, r13
008ADDF6  44 39 35 23 8F 71 00            cmp dword ptr [rip + 0x718f23], r14d
008ADDFD  0F 85 37 02 00 00               jne 0x1408ae03a
008ADE03  83 BF 9C 00 00 00 00            cmp dword ptr [rdi + 0x9c], 0
008ADE0A  0F 84 CC 02 00 00               je 0x1408ae0dc
008ADE10  83 3D 09 8F 71 00 00            cmp dword ptr [rip + 0x718f09], 0
008ADE17  74 0D                           je 0x1408ade26
008ADE19  44 0F 20 C1                     mov rcx, cr8
008ADE1D  41 0F B6 D7                     movzx edx, r15b
008ADE21  E8 72 78 C4 FF                  call 0x1404f5698
008ADE26  41 0F B6 C7                     movzx eax, r15b
008ADE2A  44 0F 22 C0                     mov cr8, rax
008ADE2E  45 84 E4                        test r12b, r12b
008ADE31  0F 84 50 FD FF FF               je 0x1408adb87
008ADE37  48 8B D6                        mov rdx, rsi
008ADE3A  48 8D 8F 98 00 00 00            lea rcx, [rdi + 0x98]
008ADE41  E8 B2 6A 1E 00                  call 0x140a948f8
008ADE46  E9 56 FD FF FF                  jmp 0x1408adba1
008ADE4B  C6 44 24 38 01                  mov byte ptr [rsp + 0x38], 1
008ADE50  83 7C 24 4C 08                  cmp dword ptr [rsp + 0x4c], 8
008ADE55  0F 82 C8 04 00 00               jb 0x1408ae323
008ADE5B  48 8B 47 68                     mov rax, qword ptr [rdi + 0x68]
008ADE5F  4C 8B 44 24 70                  mov r8, qword ptr [rsp + 0x70]
008ADE64  49 89 00                        mov qword ptr [r8], rax
008ADE67  C6 44 24 38 00                  mov byte ptr [rsp + 0x38], 0
008ADE6C  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
008ADE71  C7 00 00 00 00 00               mov dword ptr [rax], 0
008ADE77  48 C7 40 08 08 00 00 00         mov qword ptr [rax + 8], 8
008ADE7F  E9 E5 FE FF FF                  jmp 0x1408add69
008ADE84  44 8B F8                        mov r15d, eax
008ADE87  80 7C 24 38 00                  cmp byte ptr [rsp + 0x38], 0
008ADE8C  75 05                           jne 0x1408ade93
008ADE8E  44 8B 7C 24 48                  mov r15d, dword ptr [rsp + 0x48]
008ADE93  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
008ADE98  E9 CC FE FF FF                  jmp 0x1408add69
008ADE9D  48 C7 44 24 78 00 00 00 00      mov qword ptr [rsp + 0x78], 0
008ADEA6  45 84 FF                        test r15b, r15b
008ADEA9  75 08                           jne 0x1408adeb3
008ADEAB  48 C7 46 50 00 00 00 00         mov qword ptr [rsi + 0x50], 0
008ADEB3  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
008ADEB8  48 89 46 48                     mov qword ptr [rsi + 0x48], rax
008ADEBC  44 0F 20 C3                     mov rbx, cr8
008ADEC0  41 BD 01 00 00 00               mov r13d, 1
008ADEC6  45 0F 22 C5                     mov cr8, r13
008ADECA  83 3D 4F 8E 71 00 00            cmp dword ptr [rip + 0x718e4f], 0
008ADED1  0F 85 9B 01 00 00               jne 0x1408ae072
008ADED7  48 8D 4E 78                     lea rcx, [rsi + 0x78]
008ADEDB  48 8D 44 24 78                  lea rax, [rsp + 0x78]
008ADEE0  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008ADEE5  4C 8D 4C 24 40                  lea r9, [rsp + 0x40]
008ADEEA  4C 8D 44 24 78                  lea r8, [rsp + 0x78]
008ADEEF  48 8D 94 24 18 01 00 00         lea rdx, [rsp + 0x118]
008ADEF7  E8 54 D0 95 FF                  call 0x14020af50
008ADEFC  83 3D 1D 8E 71 00 00            cmp dword ptr [rip + 0x718e1d], 0
008ADF03  74 0C                           je 0x1408adf11
008ADF05  44 0F 20 C1                     mov rcx, cr8
008ADF09  0F B6 D3                        movzx edx, bl
008ADF0C  E8 87 77 C4 FF                  call 0x1404f5698
008ADF11  0F B6 C3                        movzx eax, bl
008ADF14  44 0F 22 C0                     mov cr8, rax
008ADF18  45 84 FF                        test r15b, r15b
008ADF1B  0F 84 8D FC FF FF               je 0x1408adbae
008ADF21  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
008ADF26  E9 7E FC FF FF                  jmp 0x1408adba9
008ADF2B  48 C7 44 24 20 00 00 00 00      mov qword ptr [rsp + 0x20], 0
008ADF34  45 33 C9                        xor r9d, r9d
008ADF37  45 0F B6 C4                     movzx r8d, r12b
008ADF3B  33 D2                           xor edx, edx
008ADF3D  48 8D 8C 24 00 01 00 00         lea rcx, [rsp + 0x100]
008ADF45  E8 66 07 96 FF                  call 0x14020e6b0
008ADF4A  3D 01 01 00 00                  cmp eax, 0x101
008ADF4F  0F 84 C8 04 00 00               je 0x1408ae41d
008ADF55  3D C0 00 00 00                  cmp eax, 0xc0
008ADF5A  0F 84 BD 04 00 00               je 0x1408ae41d
008ADF60  8B BC 24 F0 00 00 00            mov edi, dword ptr [rsp + 0xf0]
008ADF67  0F 10 84 24 F0 00 00 00         movups xmm0, xmmword ptr [rsp + 0xf0]
008ADF6F  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
008ADF74  0F 11 00                        movups xmmword ptr [rax], xmm0
008ADF77  E9 32 FC FF FF                  jmp 0x1408adbae
008ADF7C  8B F8                           mov edi, eax
008ADF7E  E9 2B FC FF FF                  jmp 0x1408adbae
008ADF83  F6 00 02                        test byte ptr [rax], 2
008ADF86  0F 84 92 FB FF FF               je 0x1408adb1e
008ADF8C  B1 01                           mov cl, 1
008ADF8E  E9 9A FB FF FF                  jmp 0x1408adb2d
008ADF93  44 8B 4C 24 4C                  mov r9d, dword ptr [rsp + 0x4c]
008ADF98  4C 8B 44 24 70                  mov r8, qword ptr [rsp + 0x70]
008ADF9D  48 8B 54 24 50                  mov rdx, qword ptr [rsp + 0x50]
008ADFA2  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
008ADFA6  E8 09 7F BF FF                  call 0x1404a5eb4
008ADFAB  8B D8                           mov ebx, eax
008ADFAD  48 8B CF                        mov rcx, rdi
008ADFB0  E8 9B B3 A4 FF                  call 0x1402f9350
008ADFB5  8B C3                           mov eax, ebx
008ADFB7  E9 02 FC FF FF                  jmp 0x1408adbbe
008ADFBC  3D 01 01 00 00                  cmp eax, 0x101
008ADFC1  0F 84 0B FE FF FF               je 0x1408addd2
008ADFC7  E9 D5 FB FF FF                  jmp 0x1408adba1
008ADFCC  41 8B 06                        mov eax, dword ptr [r14]
008ADFCF  D1 E8                           shr eax, 1
008ADFD1  24 01                           and al, 1
008ADFD3  88 44 24 20                     mov byte ptr [rsp + 0x20], al
008ADFD7  45 33 C9                        xor r9d, r9d
008ADFDA  45 33 C0                        xor r8d, r8d
008ADFDD  48 8B D6                        mov rdx, rsi
008ADFE0  48 8B CF                        mov rcx, rdi
008ADFE3  E8 E0 05 00 00                  call 0x1408ae5c8
008ADFE8  80 7C 24 34 00                  cmp byte ptr [rsp + 0x34], 0
008ADFED  0F 85 48 03 00 00               jne 0x1408ae33b
008ADFF3  B8 9A 00 00 C0                  mov eax, 0xc000009a
008ADFF8  E9 C1 FB FF FF                  jmp 0x1408adbbe
008ADFFD  8B 5B 58                        mov ebx, dword ptr [rbx + 0x58]
008AE000  85 DB                           test ebx, ebx
008AE002  0F 84 8B FA FF FF               je 0x1408ada93
008AE008  C1 E3 11                        shl ebx, 0x11
008AE00B  E9 C8 FA FF FF                  jmp 0x1408adad8
008AE010  83 FB 4B                        cmp ebx, 0x4b
008AE013  0F 85 FB F6 FF FF               jne 0x1408ad714
008AE019  BB 47 00 00 00                  mov ebx, 0x47
008AE01E  89 5C 24 58                     mov dword ptr [rsp + 0x58], ebx
008AE022  C6 44 24 32 01                  mov byte ptr [rsp + 0x32], 1
008AE027  E9 E8 F6 FF FF                  jmp 0x1408ad714
008AE02C  48 85 F6                        test rsi, rsi
008AE02F  0F 85 F1 FB FF FF               jne 0x1408adc26
008AE035  E9 1A F8 FF FF                  jmp 0x1408ad854
008AE03A  41 0F B6 D5                     movzx edx, r13b
008AE03E  41 0F B6 CF                     movzx ecx, r15b
008AE042  E8 B5 76 C4 FF                  call 0x1404f56fc
008AE047  E9 B7 FD FF FF                  jmp 0x1408ade03
008AE04C  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008AE055  48 3B C8                        cmp rcx, rax
008AE058  0F 85 71 FA FF FF               jne 0x1408adacf
008AE05E  83 B9 E0 05 00 00 00            cmp dword ptr [rcx + 0x5e0], 0
008AE065  B8 02 00 00 00                  mov eax, 2
008AE06A  0F 45 D8                        cmovne ebx, eax
008AE06D  E9 5D FA FF FF                  jmp 0x1408adacf
008AE072  41 0F B6 D5                     movzx edx, r13b
008AE076  0F B6 CB                        movzx ecx, bl
008AE079  E8 7E 76 C4 FF                  call 0x1404f56fc
008AE07E  E9 54 FE FF FF                  jmp 0x1408aded7
008AE083  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
008AE087  E8 84 27 B6 FF                  call 0x140410810
008AE08C  E9 EC F6 FF FF                  jmp 0x1408ad77d
008AE091  4C 8B 4E 18                     mov r9, qword ptr [rsi + 0x18]
008AE095  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
008AE09A  E8 E5 05 00 00                  call 0x1408ae684
008AE09F  41 89 01                        mov dword ptr [r9], eax
008AE0A2  48 C7 46 38 04 00 00 00         mov qword ptr [rsi + 0x38], 4
008AE0AA  89 7E 30                        mov dword ptr [rsi + 0x30], edi
008AE0AD  E9 AD FA FF FF                  jmp 0x1408adb5f
008AE0B2  48 8D 4C 24 37                  lea rcx, [rsp + 0x37]
008AE0B7  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
008AE0BC  4C 8B C8                        mov r9, rax
008AE0BF  44 0F B6 C6                     movzx r8d, sil
008AE0C3  41 0F B6 D4                     movzx edx, r12b
008AE0C7  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
008AE0CC  48 8B CF                        mov rcx, rdi
008AE0CF  E8 04 06 00 00                  call 0x1408ae6d8
008AE0D4  44 8B F8                        mov r15d, eax
008AE0D7  E9 34 F7 FF FF                  jmp 0x1408ad810
008AE0DC  44 38 6E 44                     cmp byte ptr [rsi + 0x44], r13b
008AE0E0  41 0F 94 C4                     sete r12b
008AE0E4  E9 27 FD FF FF                  jmp 0x1408ade10
008AE0E9  80 39 00                        cmp byte ptr [rcx], 0
008AE0EC  0F 85 16 FA FF FF               jne 0x1408adb08
008AE0F2  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
008AE0F7  48 8B 09                        mov rcx, qword ptr [rcx]
008AE0FA  48 85 C9                        test rcx, rcx
008AE0FD  74 1B                           je 0x1408ae11a
008AE0FF  F7 41 74 00 04 00 00            test dword ptr [rcx + 0x74], 0x400
008AE106  0F 85 FC F9 FF FF               jne 0x1408adb08
008AE10C  8B 81 A4 05 00 00               mov eax, dword ptr [rcx + 0x5a4]
008AE112  84 C0                           test al, al
008AE114  0F 88 EE F9 FF FF               js 0x1408adb08
008AE11A  FF 05 EC F0 6D 00               inc dword ptr [rip + 0x6df0ec]
008AE120  81 E3 FF FF F1 FF               and ebx, 0xfff1ffff
008AE126  81 CB 00 00 06 00               or ebx, 0x60000
008AE12C  41 89 1E                        mov dword ptr [r14], ebx
008AE12F  E9 D4 F9 FF FF                  jmp 0x1408adb08
008AE134  41 8B 06                        mov eax, dword ptr [r14]
008AE137  A8 02                           test al, 2
008AE139  0F 85 EF 01 00 00               jne 0x1408ae32e
008AE13F  48 8B CF                        mov rcx, rdi
008AE142  E8 09 B2 A4 FF                  call 0x1402f9350
008AE147  B8 9A 00 00 C0                  mov eax, 0xc000009a
008AE14C  E9 6D FA FF FF                  jmp 0x1408adbbe
008AE151  C6 44 24 36 01                  mov byte ptr [rsp + 0x36], 1
008AE156  83 7C 24 4C 01                  cmp dword ptr [rsp + 0x4c], 1
008AE15B  0F 82 91 01 00 00               jb 0x1408ae2f2
008AE161  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
008AE165  0F B6 48 34                     movzx ecx, byte ptr [rax + 0x34]
008AE169  C0 E9 04                        shr cl, 4
008AE16C  80 E1 01                        and cl, 1
008AE16F  4C 8B 44 24 70                  mov r8, qword ptr [rsp + 0x70]
008AE174  41 88 08                        mov byte ptr [r8], cl
008AE177  C6 44 24 36 00                  mov byte ptr [rsp + 0x36], 0
008AE17C  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
008AE181  89 30                           mov dword ptr [rax], esi
008AE183  48 C7 40 08 01 00 00 00         mov qword ptr [rax + 8], 1
008AE18B  E9 E1 FB FF FF                  jmp 0x1408add71
008AE190  44 8B F8                        mov r15d, eax
008AE193  80 7C 24 36 00                  cmp byte ptr [rsp + 0x36], 0
008AE198  75 05                           jne 0x1408ae19f
008AE19A  44 8B 7C 24 48                  mov r15d, dword ptr [rsp + 0x48]
008AE19F  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
008AE1A4  E9 C8 FB FF FF                  jmp 0x1408add71
008AE1A9  83 C9 10                        or ecx, 0x10
008AE1AC  E9 8D F8 FF FF                  jmp 0x1408ada3e
008AE1B1  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008AE1BA  48 FF 80 90 03 00 00            inc qword ptr [rax + 0x390]
008AE1C1  65 FF 04 25 E4 2E 00 00         inc dword ptr gs:[0x2ee4]
008AE1C9  41 83 FE 04                     cmp r14d, 4
008AE1CD  0F 82 93 00 00 00               jb 0x1408ae266
008AE1D3  C6 44 24 35 01                  mov byte ptr [rsp + 0x35], 1
008AE1D8  8B 84 24 94 00 00 00            mov eax, dword ptr [rsp + 0x94]
008AE1DF  41 89 45 00                     mov dword ptr [r13], eax
008AE1E3  C6 44 24 35 00                  mov byte ptr [rsp + 0x35], 0
008AE1E8  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
008AE1ED  89 30                           mov dword ptr [rax], esi
008AE1EF  48 C7 40 08 04 00 00 00         mov qword ptr [rax + 8], 4
008AE1F7  44 8B 7C 24 48                  mov r15d, dword ptr [rsp + 0x48]
008AE1FC  EB 0F                           jmp 0x1408ae20d
008AE1FE  44 8B F8                        mov r15d, eax
008AE201  80 7C 24 35 00                  cmp byte ptr [rsp + 0x35], 0
008AE206  75 05                           jne 0x1408ae20d
008AE208  44 8B 7C 24 48                  mov r15d, dword ptr [rsp + 0x48]
008AE20D  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
008AE212  E8 39 B1 A4 FF                  call 0x1402f9350
008AE217  41 8B C7                        mov eax, r15d
008AE21A  E9 9F F9 FF FF                  jmp 0x1408adbbe
008AE21F  0F 57 C0                        xorps xmm0, xmm0
008AE222  0F 11 84 24 18 01 00 00         movups xmmword ptr [rsp + 0x118], xmm0
008AE22A  48 8B 04 02                     mov rax, qword ptr [rdx + rax]
008AE22E  0F 10 40 18                     movups xmm0, xmmword ptr [rax + 0x18]
008AE232  0F 11 84 24 18 01 00 00         movups xmmword ptr [rsp + 0x118], xmm0
008AE23A  48 8D 8C 24 18 01 00 00         lea rcx, [rsp + 0x118]
008AE242  E8 F9 80 BB FF                  call 0x140466340
008AE247  48 8B D8                        mov rbx, rax
008AE24A  48 8B D6                        mov rdx, rsi
008AE24D  49 8B CD                        mov rcx, r13
008AE250  E8 5B D2 9E FF                  call 0x14029b4b0
008AE255  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
008AE259  48 8B CB                        mov rcx, rbx
008AE25C  E8 DF 80 BB FF                  call 0x140466340
008AE261  E9 E8 F8 FF FF                  jmp 0x1408adb4e
008AE266  41 BF 04 00 00 C0               mov r15d, 0xc0000004
008AE26C  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
008AE271  E8 DA B0 A4 FF                  call 0x1402f9350
008AE276  41 8B C7                        mov eax, r15d
008AE279  E9 40 F9 FF FF                  jmp 0x1408adbbe
008AE27E  48 8B 4E 18                     mov rcx, qword ptr [rsi + 0x18]
008AE282  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
008AE287  48 8B 80 D0 00 00 00            mov rax, qword ptr [rax + 0xd0]
008AE28E  48 85 C0                        test rax, rax
008AE291  75 75                           jne 0x1408ae308
008AE293  B8 02 00 00 00                  mov eax, 2
008AE298  89 01                           mov dword ptr [rcx], eax
008AE29A  48 C7 46 38 04 00 00 00         mov qword ptr [rsi + 0x38], 4
008AE2A2  89 7E 30                        mov dword ptr [rsi + 0x30], edi
008AE2A5  E9 B5 F8 FF FF                  jmp 0x1408adb5f
008AE2AA  48 8B 56 18                     mov rdx, qword ptr [rsi + 0x18]
008AE2AE  89 7C 24 78                     mov dword ptr [rsp + 0x78], edi
008AE2B2  4C 8D 4C 24 78                  lea r9, [rsp + 0x78]
008AE2B7  44 8B 44 24 4C                  mov r8d, dword ptr [rsp + 0x4c]
008AE2BC  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
008AE2C1  E8 DA F4 06 00                  call 0x14091d7a0
008AE2C6  8B F8                           mov edi, eax
008AE2C8  41 B2 01                        mov r10b, 1
008AE2CB  44 88 54 24 32                  mov byte ptr [rsp + 0x32], r10b
008AE2D0  41 BF 04 00 00 C0               mov r15d, 0xc0000004
008AE2D6  41 3B C7                        cmp eax, r15d
008AE2D9  0F 84 AC 00 00 00               je 0x1408ae38b
008AE2DF  8B 44 24 78                     mov eax, dword ptr [rsp + 0x78]
008AE2E3  48 89 46 38                     mov qword ptr [rsi + 0x38], rax
008AE2E7  44 0F B6 7C 24 31               movzx r15d, byte ptr [rsp + 0x31]
008AE2ED  E9 71 F7 FF FF                  jmp 0x1408ada63
008AE2F2  41 BF 04 00 00 C0               mov r15d, 0xc0000004
008AE2F8  48 8B CF                        mov rcx, rdi
008AE2FB  E8 50 B0 A4 FF                  call 0x1402f9350
008AE300  41 8B C7                        mov eax, r15d
008AE303  E9 B6 F8 FF FF                  jmp 0x1408adbbe
008AE308  8B 40 58                        mov eax, dword ptr [rax + 0x58]
008AE30B  85 C0                           test eax, eax
008AE30D  74 84                           je 0x1408ae293
008AE30F  FF C8                           dec eax
008AE311  89 01                           mov dword ptr [rcx], eax
008AE313  48 C7 46 38 04 00 00 00         mov qword ptr [rsi + 0x38], 4
008AE31B  89 7E 30                        mov dword ptr [rsi + 0x30], edi
008AE31E  E9 3C F8 FF FF                  jmp 0x1408adb5f
008AE323  41 BF 04 00 00 C0               mov r15d, 0xc0000004
008AE329  E9 3B FA FF FF                  jmp 0x1408add69
008AE32E  48 8B CF                        mov rcx, rdi
008AE331  E8 5A 27 9A FF                  call 0x140250a90
008AE336  E9 04 FE FF FF                  jmp 0x1408ae13f
008AE33B  B1 01                           mov cl, 1
008AE33D  E8 1E 24 BA FF                  call 0x140450760
008AE342  E9 AC FC FF FF                  jmp 0x1408adff3
008AE347  80 48 02 01                     or byte ptr [rax + 2], 1
008AE34B  E9 51 F6 FF FF                  jmp 0x1408ad9a1
008AE350  48 8B 4E 18                     mov rcx, qword ptr [rsi + 0x18]
008AE354  41 8B 85 98 00 00 00            mov eax, dword ptr [r13 + 0x98]
008AE35B  89 01                           mov dword ptr [rcx], eax
008AE35D  48 C7 46 38 04 00 00 00         mov qword ptr [rsi + 0x38], 4
008AE365  E9 40 FD FF FF                  jmp 0x1408ae0aa
008AE36A  48 8B 4E 18                     mov rcx, qword ptr [rsi + 0x18]
008AE36E  89 39                           mov dword ptr [rcx], edi
008AE370  33 D2                           xor edx, edx
008AE372  41 F7 06 00 00 00 04            test dword ptr [r14], 0x4000000
008AE379  0F 84 E7 C1 26 00               je 0x140b1a566
008AE37F  BA 02 00 00 00                  mov edx, 2
008AE384  89 11                           mov dword ptr [rcx], edx
008AE386  E9 DB C1 26 00                  jmp 0x140b1a566
008AE38B  8B 4C 24 78                     mov ecx, dword ptr [rsp + 0x78]
008AE38F  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
008AE394  48 89 48 08                     mov qword ptr [rax + 8], rcx
008AE398  44 0F B6 7C 24 31               movzx r15d, byte ptr [rsp + 0x31]
008AE39E  4C 8B 74 24 60                  mov r14, qword ptr [rsp + 0x60]
008AE3A3  E9 C0 F6 FF FF                  jmp 0x1408ada68
008AE3A8  8B F8                           mov edi, eax
008AE3AA  48 8B B4 24 B8 00 00 00         mov rsi, qword ptr [rsp + 0xb8]
008AE3B2  4C 8B AC 24 88 00 00 00         mov r13, qword ptr [rsp + 0x88]
008AE3BA  44 0F B6 64 24 3A               movzx r12d, byte ptr [rsp + 0x3a]
008AE3C0  44 0F B6 54 24 32               movzx r10d, byte ptr [rsp + 0x32]
008AE3C6  4C 8B B4 24 B0 00 00 00         mov r14, qword ptr [rsp + 0xb0]
008AE3CE  48 89 74 24 58                  mov qword ptr [rsp + 0x58], rsi
008AE3D3  48 8B 84 24 C8 00 00 00         mov rax, qword ptr [rsp + 0xc8]
008AE3DB  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
008AE3E0  44 88 64 24 33                  mov byte ptr [rsp + 0x33], r12b
008AE3E5  44 0F B6 7C 24 31               movzx r15d, byte ptr [rsp + 0x31]
008AE3EB  E9 78 F6 FF FF                  jmp 0x1408ada68
008AE3F0  48 8B 56 18                     mov rdx, qword ptr [rsi + 0x18]
008AE3F4  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
008AE3F9  E8 6A 2B E7 FF                  call 0x140720f68
008AE3FE  8B F8                           mov edi, eax
008AE400  41 B2 01                        mov r10b, 1
008AE403  4C 8B 74 24 60                  mov r14, qword ptr [rsp + 0x60]
008AE408  85 C0                           test eax, eax
008AE40A  0F 88 58 F6 FF FF               js 0x1408ada68
008AE410  48 C7 46 38 02 00 00 00         mov qword ptr [rsi + 0x38], 2
008AE418  E9 4B F6 FF FF                  jmp 0x1408ada68
008AE41D  48 8B D6                        mov rdx, rsi
008AE420  48 8D 8C 24 00 01 00 00         lea rcx, [rsp + 0x100]
008AE428  E8 CB 64 1E 00                  call 0x140a948f8
008AE42D  E9 2E FB FF FF                  jmp 0x1408adf60
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtQueryInformationFile(__int64 a1, __int64 a2, __int64 a3, int a4, unsigned int a5)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned int v_stack_m108;
    unsigned int v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned int v_stack_m11C;
    unsigned int v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int8 v_stack_m12E;
    unsigned __int8 v_stack_m131;
    unsigned __int8 v_stack_m134;
    unsigned __int8 v_stack_m135;
    unsigned __int8 v_stack_m136;
    unsigned __int8 v_stack_m137;
    unsigned int v_stack_m140;
    unsigned int v_stack_m148;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned int v_stack_mD4;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p100;
    unsigned __int64 v_stack_p118;
    unsigned __int64 v_stack_p20;
    unsigned __int8 v_stack_p30;
    unsigned __int8 v_stack_p31;
    unsigned __int8 v_stack_p32;
    unsigned __int8 v_stack_p33;
    unsigned __int8 v_stack_p34;
    unsigned __int8 v_stack_p35;
    unsigned __int8 v_stack_p36;
    unsigned __int64 v_stack_p37;
    unsigned __int8 v_stack_p38;
    unsigned __int8 v_stack_p39;
    unsigned __int8 v_stack_p3A;
    unsigned __int64 v_stack_p40;
    unsigned int v_stack_p48;
    unsigned int v_stack_p4C;
    unsigned __int64 v_stack_p50;
    unsigned int v_stack_p58;
    unsigned int v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;
    unsigned __int64 v_stack_p80;
    unsigned __int64 v_stack_p88;
    unsigned int v_stack_p94;
    unsigned __int64 v_stack_p98;
    unsigned __int64 v_stack_pA8;
    unsigned __int64 v_stack_pB0;
    unsigned __int64 v_stack_pB8;
    unsigned __int64 v_stack_pC8;
    unsigned __int64 v_stack_pD0;
    unsigned __int64 v_stack_pE0;
    unsigned __int64 v_stack_pF0;

    v_rsp = (v_rsp) - (304);
    result = (*(unsigned __int64 *)(v_rip + 5624052)) ^ (v_rsp);
    v_stack_m40 = result;
    v_stack_m11C = a4;
    v_stack_mF8 = a3;
    v_stack_m118 = a2;
    v_stack_mA0 = a2;
    v_stack_mE8 = a2;
    v_stack_mB0 = a2;
    v_stack_mB8 = a3;
    v_stack_m108 = a4;
    v_stack_m110 = (unsigned int)((unsigned int)(a5));
    v_rsi = 0;
    v_stack_m128 = 0;
    result = 0;
    *(unsigned __int64 *)(v_rsp - 104) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 88) = 0;
    *(unsigned __int64 *)(v_rsp - 120) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 216) = 0;
    v_stack_m134 = 0;
    v_stack_m136 = 0;
    v_stack_mA8 = *(unsigned __int64 *)(gs_base + (0 + 392));
    v_stack_m135 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    v_stack_m12E = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    v_stack_m140 = (unsigned int)((unsigned int)(a5));
    v_stack_m148 = a4;
    result = IopValidateQueryInformationParameters(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562), *(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3);
    if (sign_flag) goto loc_008ADBBE;
    if ((unsigned __int8)((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562))) == 0) goto loc_008AE010;
loc_008AD714:
    v_stack_m148 = v_stack_mD8;
    result = IopReferenceFileObject(a1, (unsigned int)(*(unsigned int *)(v_rip + 2756946 + (int)((unsigned int)((unsigned int)(a5))) * 4)), (unsigned __int8)((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562))), v_stack_m128);
    v_stack_m120 = (unsigned int)(result);
    if (sign_flag) goto loc_008ADBBE;
    if (((unsigned int)((unsigned int)(a5))) == 8) goto loc_008AE1B1;
    v_stack_mC0 = v_stack_m128 + 80;
    if (((*(unsigned int *)(v_stack_m128 + 80)) & (0x800ULL)) != 0) goto loc_008AE083;
    result = IoGetRelatedDeviceObject(v_stack_m128, (unsigned int)(*(unsigned int *)(v_rip + 2756946 + (int)((unsigned int)((unsigned int)(a5))) * 4)), (unsigned __int8)((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562))), v_stack_m128);
loc_008AD77D:
    v_stack_mE0 = result;
    v_stack_m100 = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 8) + 80);
    if (((unsigned int)((unsigned int)(a5))) == 51) goto loc_008AE151;
    if (((unsigned int)((unsigned int)(a5))) == 58) goto loc_008ADF93;
    a3 = 0;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m128 + 80)))) & (2)) == 0) goto loc_008AD862;
    v_rsi = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m128 + 80))) >> (2));
    v_rsi = (unsigned __int8)((v_rsi) & (1));
    a2 = 0;
    result = KeAbPreAcquire(v_stack_m128 + 128, a2, a3, v_stack_m128);
    v_stack_m131 = 0;
    if (1 != 0) goto loc_008AE0B2;
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    result = ObfReferenceObject(v_stack_m128, a2, a3, v_stack_m128);
    v_r15 = 0;
loc_008AD810:
    v_stack_m120 = 0;
    if (v_stack_m131 != 0) goto loc_008ADD71;
    if (((unsigned int)((unsigned int)(a5))) == 14) goto loc_008ADE4B;
    if (v_stack_m100 == 0) goto loc_008AD85D;
    v_stack_mC8 = *(unsigned __int64 *)(v_stack_m100 + 32);
    v_stack_mD0 = *(unsigned __int64 *)(v_stack_m100 + 40);
    if (((unsigned int)((unsigned int)(a5))) == 4) goto loc_008AE02C;
loc_008AD854:
    if (((unsigned int)((unsigned int)(a5))) == 5) goto loc_008ADC1D;
loc_008AD85D:
    goto loc_008AD877;
loc_008AD862:
    result = KeInitializeEvent(v_stack_m68, 1, a3, v_stack_m128);
    v_r15 = 0;
loc_008AD877:
    v_stack_m137 = 0;
    result = IopResetEvent(v_stack_m128, 1, a3, v_stack_m128);
    a3 = 0;
    result = IopAllocateIrpExReturn(result, *(unsigned __int8 *)(result + 76), a3, v_stack_m128);
    v_stack_m110 = result;
    v_stack_mB0 = result;
    v_stack_m80 = result;
    if (result == 0) goto loc_008AE134;
    *(unsigned __int64 *)(result + 192) = v_stack_m128;
    v_stack_m100 = result + 152;
    *(unsigned __int64 *)(result + 152) = v_stack_mA8;
    v_stack_mD0 = result + 64;
    *(unsigned __int8 *)(result + 64) = (unsigned __int8)((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    if (0 == 0) goto loc_008ADBE2;
    a2 = 0;
loc_008AD8F8:
    v_stack_m108 = result + 16;
    v_stack_mB8 = result + 16;
    *(unsigned __int64 *)(result + 80) = 0;
    *(unsigned __int64 *)(result + 72) = v_stack_mE8;
    *(unsigned __int64 *)(result + 88) = 0;
    result = (*(unsigned __int64 *)(result + 184)) - (72);
    v_stack_mA8 = result;
    *(unsigned __int8 *)(result) = 5;
    *(unsigned __int64 *)(result + 48) = v_stack_m128;
    *(unsigned __int64 *)(result + 112) = v_stack_mF8;
    *(unsigned __int64 *)(result + 24) = 0;
    *(unsigned __int64 *)(result + 8) = 0;
    result = ExAllocatePool2(65, (unsigned int)(v_stack_m11C), (unsigned int)(0x42536F49ULL), v_stack_m128);
    *(unsigned __int64 *)(result + 24) = result;
    if (result == 0) goto loc_008ADFCC;
    v_stack_mC8 = v_stack_m108;
    *(unsigned int *)(v_stack_mA8 + 8) = (unsigned int)((unsigned int)(v_stack_m11C));
    *(unsigned int *)(v_stack_mA8 + 16) = (unsigned int)((unsigned int)(a5));
    if (v_stack_m136 != 0) goto loc_008AE347;
loc_008AD9A1:
    result = IopQueueThreadIrp(result, (unsigned int)(v_stack_m11C), (unsigned int)(0x42536F49ULL), v_stack_m128);
    v_r10 = 0;
    v_rdi = 0;
    if (((unsigned int)((unsigned int)(a5))) == 16) goto loc_008AE091;
    if (((unsigned int)((unsigned int)(a5))) == 17) goto loc_008AE350;
    if (((unsigned int)((unsigned int)(a5))) == 41) goto loc_008AE36A;
    if (((unsigned int)((unsigned int)(a5))) == 43) goto loc_008AE27E;
    if (((unsigned int)((unsigned int)(a5))) == 47) goto loc_008AE2AA;
    if (((unsigned int)((unsigned int)(a5))) == 53) goto loc_008AE3F0;
    if (((unsigned int)((unsigned int)(a5))) != 18) goto loc_008ADA63;
    *(unsigned int *)(*(unsigned __int64 *)(result + 24) + 76) = (unsigned int)((unsigned int)(v_stack_mD4));
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m128 + 80))))) >> (3));
    a1 = (unsigned int)((a1) & (2));
    a2 = (unsigned int)(((unsigned int)((unsigned int)(a1))) | (4));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m128 + 80)))) & (32)) == 0) { a2 = (unsigned int)(a1); }
    a1 = (unsigned int)(((unsigned int)((unsigned int)(a2))) | (8));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m128 + 80)))) & (8)) == 0) { a1 = (unsigned int)(a2); }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m128 + 80)))) & (2)) != 0) goto loc_008ADD8B;
loc_008ADA3E:
    result = (unsigned int)((unsigned int)(a1));
    if (condition_is_above_or_equal) { result = (unsigned int)(a1); }
    *(unsigned int *)(*(unsigned __int64 *)(result + 24) + 88) = (unsigned int)(result);
    *(unsigned int *)(*(unsigned __int64 *)(result + 24) + 92) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 152)));
    *(unsigned __int64 *)(result + 56) = 12;
loc_008ADA63:
loc_008ADA68:
    if (0 != 0) goto loc_008AE0AA;
    result = (unsigned int)(*(unsigned int *)(result + 152));
    if (0 == 0) {
        a1 = v_stack_m128;
        result = ObfReferenceObject(a1, a2, (unsigned int)(*(unsigned int *)(v_stack_m128 + 80)), *(unsigned __int64 *)(result + 24));
    }
    if (*(unsigned __int64 *)(v_stack_m128 + 208) != 0) goto loc_008ADFFD;
loc_008ADA93:
    v_rbx = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1440))) >> (9));
    v_rbx = (unsigned int)((v_rbx) & (7));
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544) + 672);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544) + 672) != 0) {
        result = *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544) + 672) + 1084);
        if (((unsigned int)(v_rbx)) >= ((unsigned int)(result))) { v_rbx = (unsigned int)(result); }
    }
    if (((unsigned int)(v_rbx)) < 2) goto loc_008AE04C;
loc_008ADACF:
    v_rbx = (unsigned int)((v_rbx) << (17));
    v_rbx = (unsigned int)((v_rbx) + (0x20000ULL));
loc_008ADAD8:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m108))) & (0xFFF1FFFFULL));
    v_rbx = (unsigned int)((v_rbx) | ((unsigned int)(result)));
    *(unsigned int *)(v_stack_m108) = (unsigned int)(result);
    *(unsigned int *)(v_stack_mC8) = (unsigned int)(v_rbx);
    result = IoGetIoPriorityHint(result, a2, (unsigned int)(*(unsigned int *)(v_stack_m128 + 80)), *(unsigned __int64 *)(result + 24));
    if (((unsigned int)(result)) < 2) goto loc_008AE0E9;
loc_008ADB08:
    if ((*(unsigned __int8 *)(result + 71)) < 0) goto loc_008ADB1E;
    if (*(unsigned __int64 *)(result + 200) != 0) goto loc_008ADF83;
loc_008ADB1E:
    a1 = 0;
    v_stack_m110 = v_stack_m80;
loc_008ADB2D:
    if (0 != 0) goto loc_008AE21F;
    result = IofCallDriver(result, result, (unsigned int)(*(unsigned int *)(v_stack_m128 + 80)), *(unsigned __int64 *)(result + 24));
    v_stack_m110 = (unsigned int)(result);
loc_008ADB4E:
    if (0 == 0) {
        a1 = v_stack_m128;
        result = ObDereferenceObjectDeferDelete(a1, result, (unsigned int)(*(unsigned int *)(v_stack_m128 + 80)), *(unsigned __int64 *)(result + 24));
    }
loc_008ADB5F:
    if (((unsigned int)((unsigned int)(v_stack_m110))) != 259) goto loc_008ADE9D;
    if (0 == 0) goto loc_008ADF2B;
    v_r14 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m128 + 80))) & (4));
loc_008ADB87:
    if (((*(unsigned __int8 *)(v_stack_m128 + 152)) & (127)) != 0) goto loc_008ADD9D;
    if ((*(unsigned int *)(v_stack_m128 + 156)) == 0) goto loc_008ADD9D;
loc_008ADBA1:
loc_008ADBA9:
    result = IopReleaseFileObjectLock(v_stack_m128, result, (unsigned int)(*(unsigned int *)(v_stack_m128 + 80)), *(unsigned __int64 *)(result + 24));
loc_008ADBAE:
    if (v_stack_m134 != 0) {
        a1 = 1;
        result = KeSetKernelStackSwapEnable(a1, result, (unsigned int)(*(unsigned int *)(v_stack_m128 + 80)), *(unsigned __int64 *)(result + 24));
    }
loc_008ADBBE:
    a1 = (v_stack_m40) ^ (v_rsp);
    result = _security_check_cookie(a1, result, (unsigned int)(*(unsigned int *)(v_stack_m128 + 80)), *(unsigned __int64 *)(result + 24));
    v_rsp = (v_rsp) + (304);
    return result;
loc_008ADBE2:
    if (((unsigned __int8)((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)))) == 1) {
        a1 = 0;
        result = KeSetKernelStackSwapEnable(a1, result, (unsigned int)(*(unsigned int *)(v_stack_m128 + 80)), *(unsigned __int64 *)(result + 24));
        v_stack_p34 = (unsigned __int8)(result);
        a1 = result;
    }
    *(unsigned int *)(result + 16) = 4;
    v_stack_p80 = v_stack_pF0;
    goto loc_008AD8F8;
loc_008ADC1D:
    if (result + 16 == 0) goto loc_008AD85D;
loc_008ADC26:
    v_stack_pD0 = v_xmm0;
    v_stack_p30 = 0;
    v_stack_p39 = 0;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 6647263)))) & (16)) != 0) goto loc_008ADCCE;
loc_008ADC49:
    result = 0;
loc_008ADC4B:
    v_stack_p68 = 0;
    v_stack_pE0 = 0;
    v_stack_p20 = 1;
    if (((unsigned int)(v_rbx)) == 4) goto loc_008ADC7E;
    goto loc_008ADC81;
loc_008ADC7E:
loc_008ADC81:
    result = guard_dispatch_icall((unsigned int)(*(unsigned int *)(v_stack_m128 + 56)), 1, v_stack_p70, v_stack_pD0);
    v_stack_p30 = (unsigned __int8)(result);
    if (v_stack_p68 != 0) {
        a2 = result;
        result = VfFastIoCheckState(v_stack_p68, a2, v_stack_p70, v_stack_pD0);
        result = v_stack_p30;
    }
    if ((unsigned __int8)(result) == 0) goto loc_008ADCF6;
    v_stack_p48 = (unsigned int)((unsigned int)(v_stack_pD0));
    v_stack_p39 = 1;
    *(unsigned __int64 *)(v_stack_p50) = v_xmm0;
    goto loc_008ADCF6;
loc_008ADCCE:
    v_stack_p68 = *(unsigned __int64 *)(1 + 8);
    result = MmIsDriverVerifying(*(unsigned __int64 *)(1 + 8), a2, v_stack_p70, v_stack_pD0);
    if ((unsigned int)(result) == 0) goto loc_008ADC49;
    result = VfFastIoSnapState(v_stack_p68, a2, v_stack_p70, v_stack_pD0);
    goto loc_008ADC4B;
loc_008ADCF6:
    goto loc_008ADD61;
loc_008ADD61:
    if ((unsigned __int8)(result) == 0) goto loc_008AD85D;
loc_008ADD69:
    result = IopReleaseFileObjectLock((unsigned int)(*(unsigned int *)(v_stack_m128 + 56)), a2, v_stack_p70, v_stack_pD0);
loc_008ADD71:
    result = ObfDereferenceObject((unsigned int)(*(unsigned int *)(v_stack_m128 + 56)), a2, v_stack_p70, v_stack_pD0);
    goto loc_008ADBBE;
loc_008ADD8B:
    if ((((unsigned __int8)(v_stack_p70)) & (4)) != 0) goto loc_008AE1A9;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m128 + 56))) | (32));
    goto loc_008ADA3E;
loc_008ADD9D:
    a3 = 0;
    if ((unsigned int)(v_r14) != 0) { a3 = (unsigned int)(v_stack_p33); }
    v_stack_p20 = 0;
    a2 = 0;
    result = KeWaitForSingleObject((unsigned int)(*(unsigned int *)(v_stack_m128 + 56)) + 152, a2, a3, 1);
    if (((unsigned int)(result)) != 192) goto loc_008ADFBC;
loc_008ADDD2:
    if ((unsigned int)(v_r14) != 0) goto loc_008ADE37;
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1440))))) != 0) goto loc_008ADE37;
    v_r12 = 0;
    if ((*(unsigned int *)(v_rip + 7442211)) != ((unsigned int)(v_r14))) goto loc_008AE03A;
loc_008ADE03:
    if ((*(unsigned int *)((unsigned int)(*(unsigned int *)(v_stack_m128 + 56)) + 156)) == 0) goto loc_008AE0DC;
loc_008ADE10:
    result = *(unsigned __int64 *)(gs_base + (0 + 392));
    if ((*(unsigned int *)(v_rip + 7442185)) != 0) {
        a1 = 1;
        a2 = (unsigned __int8)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, a3, 1);
    }
    if (0 == 0) goto loc_008ADB87;
loc_008ADE37:
    result = IopCancelAlertedRequest((unsigned int)(*(unsigned int *)(v_stack_m128 + 56)) + 152, result, a3, 1);
    goto loc_008ADBA1;
loc_008ADE4B:
    v_stack_p38 = 1;
    if (v_stack_p4C < 8) goto loc_008AE323;
    *(unsigned __int64 *)(v_stack_p70) = *(unsigned __int64 *)((unsigned int)(*(unsigned int *)(v_stack_m128 + 56)) + 104);
    v_stack_p38 = 0;
    *(unsigned int *)(v_stack_p50) = 0;
    *(unsigned __int64 *)(v_stack_p50 + 8) = 8;
    goto loc_008ADD69;
loc_008ADE9D:
    v_stack_p78 = 0;
    if ((unsigned __int8)(v_cr8) == 0) {
        *(unsigned __int64 *)(result + 80) = 0;
    }
    *(unsigned __int64 *)(result + 72) = v_stack_p50;
    if ((*(unsigned int *)(v_rip + 7441999)) != 0) goto loc_008AE072;
loc_008ADED7:
    v_stack_p20 = v_stack_p78;
    result = IopCompleteRequest(result + 120, v_stack_p118, v_stack_p78, v_stack_p40);
    if ((*(unsigned int *)(v_rip + 7441949)) != 0) {
        a1 = 1;
        a2 = (unsigned __int8)((unsigned __int8)(v_cr8));
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, v_stack_p78, v_stack_p40);
    }
    if ((unsigned __int8)(v_cr8) == 0) goto loc_008ADBAE;
    goto loc_008ADBA9;
loc_008ADF2B:
    v_stack_p20 = 0;
    a4 = 0;
    a2 = 0;
    result = KeWaitForSingleObject(v_stack_p100, a2, 0, a4);
    if (((unsigned int)(result)) == 257) goto loc_008AE41D;
    if (((unsigned int)(result)) == 192) goto loc_008AE41D;
loc_008ADF60:
    *(unsigned __int64 *)(v_stack_p50) = v_xmm0;
    goto loc_008ADBAE;
loc_008ADF83:
    if (((*(unsigned __int8 *)(v_stack_p50)) & (2)) == 0) goto loc_008ADB1E;
    goto loc_008ADB2D;
loc_008ADF93:
    result = IopGetFileVolumeNameInformation(*(unsigned __int64 *)((unsigned int)(v_stack_pF0) + 8), v_stack_p50, v_stack_p70, (unsigned int)(v_stack_p4C));
    result = ObfDereferenceObject((unsigned int)(v_stack_pF0), v_stack_p50, v_stack_p70, (unsigned int)(v_stack_p4C));
    goto loc_008ADBBE;
loc_008ADFBC:
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))))) == 257) goto loc_008ADDD2;
    goto loc_008ADBA1;
loc_008ADFCC:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r14))) >> (1));
    result = (unsigned __int8)((result) & (1));
    v_stack_p20 = (unsigned __int8)(result);
    a4 = 0;
    a3 = 0;
    result = IopExceptionCleanupEx((unsigned int)(v_stack_pF0), result, a3, a4);
    if (v_stack_p34 != 0) goto loc_008AE33B;
loc_008ADFF3:
    goto loc_008ADBBE;
loc_008ADFFD:
    if ((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)(result)) + 88))) == 0) goto loc_008ADA93;
    v_rbx = (unsigned int)(((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)(result)) + 88))) << (17));
    goto loc_008ADAD8;
loc_008AE010:
    if (((unsigned int)(v_rbx)) != 75) goto loc_008AD714;
    v_stack_p58 = 71;
    v_stack_p32 = 1;
    goto loc_008AD714;
loc_008AE02C:
    if (result != 0) goto loc_008ADC26;
    goto loc_008AD854;
loc_008AE03A:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(v_cr8), 1, a3, a4);
    goto loc_008ADE03;
loc_008AE04C:
    if (((unsigned __int8)(v_cr8)) != (*(unsigned __int64 *)(gs_base + (0 + 392)))) goto loc_008ADACF;
    v_rbx = 71;
    if ((*(unsigned int *)((unsigned __int8)(v_cr8) + 1504)) != 0) { v_rbx = 2; }
    goto loc_008ADACF;
loc_008AE072:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(v_rbx), 1, a3, a4);
    goto loc_008ADED7;
loc_008AE083:
    result = IoGetAttachedDevice(*(unsigned __int64 *)((unsigned int)(v_stack_pF0) + 8), 1, a3, a4);
    goto loc_008AD77D;
loc_008AE091:
    result = IopGetModeInformation(v_stack_p40, 1, a3, *(unsigned __int64 *)(result + 24));
    *(unsigned int *)(*(unsigned __int64 *)(result + 24)) = (unsigned int)(result);
    *(unsigned __int64 *)(result + 56) = 4;
loc_008AE0AA:
    *(unsigned int *)(result + 48) = (unsigned int)((unsigned int)(v_stack_pF0));
    goto loc_008ADB5F;
loc_008AE0B2:
    v_stack_p20 = v_stack_p37;
    result = IopWaitAndAcquireFileObjectLock(v_stack_p40, 0, (unsigned __int8)(result), result);
    goto loc_008AD810;
loc_008AE0DC:
    v_r12 = ((*(unsigned __int8 *)(result + 68)) == 1) ? 1 : 0;
    goto loc_008ADE10;
loc_008AE0E9:
    if ((*(unsigned __int8 *)(v_stack_p40)) != 0) goto loc_008ADB08;
    if (*(unsigned __int64 *)(v_stack_p68) == 0) goto loc_008AE11A;
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_stack_p68) + 116)) & (0x400ULL)) != 0) goto loc_008ADB08;
    if (sign_flag) goto loc_008ADB08;
loc_008AE11A:
    v_rbx = (unsigned int)((v_rbx) & (0xFFF1FFFFULL));
    v_rbx = (unsigned int)((v_rbx) | (0x60000ULL));
    *(unsigned int *)(v_r14) = (unsigned int)(v_rbx);
    goto loc_008ADB08;
loc_008AE134:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_r14)))) & (2)) != 0) goto loc_008AE32E;
loc_008AE13F:
    result = ObfDereferenceObject(v_stack_p40, 0, (unsigned __int8)(result), result);
    goto loc_008ADBBE;
loc_008AE151:
    v_stack_p36 = 1;
    if (v_stack_p4C < 1) goto loc_008AE2F2;
    a1 = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_p40 + 8) + 52)) >> (4));
    a1 = (unsigned __int8)((a1) & (1));
    *(unsigned __int8 *)(v_stack_p70) = (unsigned __int8)(a1);
    v_stack_p36 = 0;
    *(unsigned int *)(v_stack_p50) = (unsigned int)(result);
    *(unsigned __int64 *)(v_stack_p50 + 8) = 1;
    goto loc_008ADD71;
loc_008AE1A9:
    a1 = (unsigned int)((a1) | (16));
    goto loc_008ADA3E;
loc_008AE1B1:
    if (((unsigned int)(v_r14)) < 4) goto loc_008AE266;
    v_stack_p35 = 1;
    *(unsigned int *)(1) = (unsigned int)((unsigned int)(v_stack_p94));
    v_stack_p35 = 0;
    *(unsigned int *)(v_stack_p50) = (unsigned int)(result);
    *(unsigned __int64 *)(v_stack_p50 + 8) = 4;
    goto loc_008AE20D;
loc_008AE20D:
    result = ObfDereferenceObject(v_stack_p40, 0, v_stack_p70, result);
    goto loc_008ADBBE;
loc_008AE21F:
    v_stack_p118 = v_xmm0;
    v_stack_p118 = v_xmm0;
    result = IoSetActivityIdThread(v_stack_p118, 0, v_stack_p70, result);
    result = IofCallDriver(1, result, v_stack_p70, result);
    v_stack_p58 = (unsigned int)(result);
    result = IoSetActivityIdThread(result, result, v_stack_p70, result);
    goto loc_008ADB4E;
loc_008AE266:
    result = ObfDereferenceObject(v_stack_p40, result, v_stack_p70, result);
    goto loc_008ADBBE;
loc_008AE27E:
    if (*(unsigned __int64 *)(v_stack_p40 + 208) != 0) goto loc_008AE308;
loc_008AE293:
    *(unsigned int *)(*(unsigned __int64 *)(result + 24)) = 2;
    *(unsigned __int64 *)(result + 56) = 4;
    *(unsigned int *)(result + 48) = (unsigned int)(v_stack_p40);
    goto loc_008ADB5F;
loc_008AE2AA:
    v_stack_p78 = (unsigned int)(v_stack_p40);
    result = IopQueryProcessIdsUsingFile(v_stack_p40, *(unsigned __int64 *)(result + 24), (unsigned int)(v_stack_p4C), v_stack_p78);
    v_stack_p32 = 1;
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0xC0000004ULL)))) goto loc_008AE38B;
    *(unsigned __int64 *)(result + 56) = (unsigned int)(v_stack_p78);
    goto loc_008ADA63;
loc_008AE2F2:
    result = ObfDereferenceObject((unsigned int)((unsigned int)(result)), *(unsigned __int64 *)(result + 24), (unsigned int)(v_stack_p4C), v_stack_p78);
    goto loc_008ADBBE;
loc_008AE308:
    if ((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)((unsigned int)(0xC0000004ULL))) + 88))) == 0) goto loc_008AE293;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)((unsigned int)(0xC0000004ULL))) + 88))) - 1);
    *(unsigned int *)((unsigned int)((unsigned int)(result))) = (unsigned int)(result);
    *(unsigned __int64 *)(result + 56) = 4;
    *(unsigned int *)(result + 48) = (unsigned int)((unsigned int)((unsigned int)(result)));
    goto loc_008ADB5F;
loc_008AE323:
    goto loc_008ADD69;
loc_008AE32E:
    result = IopReleaseFileObjectLock((unsigned int)((unsigned int)(result)), *(unsigned __int64 *)(result + 24), (unsigned int)(v_stack_p4C), v_stack_p78);
    goto loc_008AE13F;
loc_008AE33B:
    result = KeSetKernelStackSwapEnable(1, *(unsigned __int64 *)(result + 24), (unsigned int)(v_stack_p4C), v_stack_p78);
    goto loc_008ADFF3;
loc_008AE347:
    goto loc_008AD9A1;
loc_008AE350:
    *(unsigned int *)(*(unsigned __int64 *)(result + 24)) = (unsigned int)((unsigned int)(*(unsigned int *)(1 + 152)));
    *(unsigned __int64 *)(result + 56) = 4;
    goto loc_008AE0AA;
loc_008AE36A:
    *(unsigned int *)(*(unsigned __int64 *)(result + 24)) = (unsigned int)((unsigned int)((unsigned int)(result)));
    a2 = 0;
    *(unsigned int *)(*(unsigned __int64 *)(result + 24)) = 2;
loc_008AE38B:
    *(unsigned __int64 *)(v_stack_p50 + 8) = (unsigned int)(v_stack_p78);
    goto loc_008ADA68;
loc_008AE3F0:
    result = IopGetNumaNodeInformation(v_stack_p40, *(unsigned __int64 *)(result + 24), (unsigned int)(v_stack_p4C), v_stack_p78);
    if (sign_flag) goto loc_008ADA68;
    *(unsigned __int64 *)(result + 56) = 2;
    goto loc_008ADA68;
loc_008AE41D:
    result = IopCancelAlertedRequest(v_stack_p100, result, (unsigned int)(v_stack_p4C), v_stack_p78);
    goto loc_008ADF60;
}
```

## 5. (Beta) C Style

```c
int64_t NtQueryInformationFile(int64_t Arg1, int64_t Arg2, void *Arg3, int32_t Arg4, uint32_t Arg5)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint32_t v_stack_m108;
    uint32_t v_stack_m110;
    uint64_t v_stack_m118;
    uint32_t v_stack_m11C;
    uint32_t v_stack_m120;
    uint64_t v_stack_m128;
    uint8_t v_stack_m12E;
    uint8_t v_stack_m131;
    uint8_t v_stack_m134;
    uint8_t v_stack_m135;
    uint8_t v_stack_m136;
    uint8_t v_stack_m137;
    uint32_t v_stack_m140;
    uint32_t v_stack_m148;
    uint64_t v_stack_m40;
    uint64_t v_stack_m68;
    uint64_t v_stack_m80;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint32_t v_stack_mD4;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p100;
    uint64_t v_stack_p118;
    uint64_t v_stack_p20;
    uint8_t v_stack_p30;
    uint8_t v_stack_p31;
    uint8_t v_stack_p32;
    uint8_t v_stack_p33;
    uint8_t v_stack_p34;
    uint8_t v_stack_p35;
    uint8_t v_stack_p36;
    uint64_t v_stack_p37;
    uint8_t v_stack_p38;
    uint8_t v_stack_p39;
    uint8_t v_stack_p3A;
    uint64_t v_stack_p40;
    uint32_t v_stack_p48;
    uint32_t v_stack_p4C;
    uint64_t v_stack_p50;
    uint32_t v_stack_p58;
    uint32_t v_stack_p60;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;
    uint64_t v_stack_p80;
    uint64_t v_stack_p88;
    uint32_t v_stack_p94;
    uint64_t v_stack_p98;
    uint64_t v_stack_pA8;
    uint64_t v_stack_pB0;
    uint64_t v_stack_pB8;
    uint64_t v_stack_pC8;
    uint64_t v_stack_pD0;
    uint64_t v_stack_pE0;
    uint64_t v_stack_pF0;

    local_rsp = (local_rsp) - (304);
    result = (*(uint64_t *)(v_rip + 0x55D0F4)) ^ (local_rsp);
    v_stack_m40 = result;
    v_stack_m11C = Arg4;
    v_stack_mF8 = Arg3;
    v_stack_m118 = Arg2;
    v_stack_mA0 = Arg2;
    v_stack_mE8 = Arg2;
    v_stack_mB0 = Arg2;
    v_stack_mB8 = Arg3;
    v_stack_m108 = Arg4;
    v_stack_m110 = (uint32_t)((uint32_t)(Arg5));
    local_rsi = 0;
    v_stack_m128 = 0;
    result = 0;
    *(uint64_t *)(local_rsp - 0x68) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x58) = 0;
    *(uint64_t *)(local_rsp - 0x78) = v_xmm0;
    *(uint64_t *)(local_rsp - 0xD8) = 0;
    v_stack_m134 = 0;
    v_stack_m136 = 0;
    v_stack_mA8 = *(uint64_t *)(gs_base + (0 + 0x188));
    v_stack_m135 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    v_stack_m12E = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    v_stack_m140 = (uint32_t)((uint32_t)(Arg5));
    v_stack_m148 = Arg4;
    result = IopValidateQueryInformationParameters(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232), *(uint64_t *)(gs_base + (0 + 0x188)), Arg2, Arg3);
    if (sign_flag) goto loc_008ADBBE;
    if ((uint8_t)((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232))) == 0) goto loc_008AE010;
loc_008AD714:
    v_stack_m148 = v_stack_mD8;
    result = IopReferenceFileObject(Arg1, (uint32_t)(*(uint32_t *)(v_rip + 0x2A1152 + (int32_t)((uint32_t)((uint32_t)(Arg5))) * 4)), (uint8_t)((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232))), v_stack_m128);
    v_stack_m120 = (uint32_t)(result);
    if (sign_flag) goto loc_008ADBBE;
    if (((uint32_t)((uint32_t)(Arg5))) == 8) goto loc_008AE1B1;
    v_stack_mC0 = v_stack_m128 + 80;
    if (((*(uint32_t *)(v_stack_m128 + 0x50)) & (0x800ULL)) != 0) goto loc_008AE083;
    result = IoGetRelatedDeviceObject(v_stack_m128, (uint32_t)(*(uint32_t *)(v_rip + 0x2A1152 + (int32_t)((uint32_t)((uint32_t)(Arg5))) * 4)), (uint8_t)((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232))), v_stack_m128);
loc_008AD77D:
    v_stack_mE0 = result;
    v_stack_m100 = *(uint64_t *)(*(uint64_t *)(result + 0x8) + 0x50);
    if (((uint32_t)((uint32_t)(Arg5))) == 51) goto loc_008AE151;
    if (((uint32_t)((uint32_t)(Arg5))) == 58) goto loc_008ADF93;
    Arg3 = 0;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m128 + 0x50)))) & (2)) == 0) goto loc_008AD862;
    local_rsi = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m128 + 0x50))) >> (2));
    local_rsi = (uint8_t)((local_rsi) & (1));
    Arg2 = 0;
    result = KeAbPreAcquire(v_stack_m128 + 128, Arg2, Arg3, v_stack_m128);
    v_stack_m131 = 0;
    if (1 != 0) goto loc_008AE0B2;
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    result = ObfReferenceObject(v_stack_m128, Arg2, Arg3, v_stack_m128);
    local_r15 = 0;
loc_008AD810:
    v_stack_m120 = 0;
    if (v_stack_m131 != 0) goto loc_008ADD71;
    if (((uint32_t)((uint32_t)(Arg5))) == 14) goto loc_008ADE4B;
    if (v_stack_m100 == 0) goto loc_008AD85D;
    v_stack_mC8 = *(uint64_t *)(v_stack_m100 + 0x20);
    v_stack_mD0 = *(uint64_t *)(v_stack_m100 + 0x28);
    if (((uint32_t)((uint32_t)(Arg5))) == 4) goto loc_008AE02C;
loc_008AD854:
    if (((uint32_t)((uint32_t)(Arg5))) == 5) goto loc_008ADC1D;
loc_008AD85D:
    goto loc_008AD877;
loc_008AD862:
    result = KeInitializeEvent(v_stack_m68, 1, Arg3, v_stack_m128);
    local_r15 = 0;
loc_008AD877:
    v_stack_m137 = 0;
    result = IopResetEvent(v_stack_m128, 1, Arg3, v_stack_m128);
    Arg3 = 0;
    result = IopAllocateIrpExReturn(result, *(uint8_t *)(result + 0x4C), Arg3, v_stack_m128);
    v_stack_m110 = result;
    v_stack_mB0 = result;
    v_stack_m80 = result;
    if (result == 0) goto loc_008AE134;
    *(uint64_t *)(result + 0xC0) = v_stack_m128;
    v_stack_m100 = result + 152;
    *(uint64_t *)(result + 0x98) = v_stack_mA8;
    v_stack_mD0 = result + 64;
    *(uint8_t *)(result + 0x40) = (uint8_t)((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    if (0 == 0) goto loc_008ADBE2;
    Arg2 = 0;
loc_008AD8F8:
    v_stack_m108 = result + 16;
    v_stack_mB8 = result + 16;
    *(uint64_t *)(result + 0x50) = 0;
    *(uint64_t *)(result + 0x48) = v_stack_mE8;
    *(uint64_t *)(result + 0x58) = 0;
    result = (*(uint64_t *)(result + 0xB8)) - (72);
    v_stack_mA8 = result;
    *(uint8_t *)(result) = 5;
    *(uint64_t *)(result + 0x30) = v_stack_m128;
    *(uint64_t *)(result + 0x70) = v_stack_mF8;
    *(uint64_t *)(result + 0x18) = 0;
    *(uint64_t *)(result + 0x8) = 0;
    result = ExAllocatePool2(65, (uint32_t)(v_stack_m11C), (uint32_t)(0x42536F49ULL), v_stack_m128);
    *(uint64_t *)(result + 0x18) = result;
    if (result == 0) goto loc_008ADFCC;
    v_stack_mC8 = v_stack_m108;
    *(uint32_t *)(v_stack_mA8 + 0x8) = (uint32_t)((uint32_t)(v_stack_m11C));
    *(uint32_t *)(v_stack_mA8 + 0x10) = (uint32_t)((uint32_t)(Arg5));
    if (v_stack_m136 != 0) goto loc_008AE347;
loc_008AD9A1:
    result = IopQueueThreadIrp(result, (uint32_t)(v_stack_m11C), (uint32_t)(0x42536F49ULL), v_stack_m128);
    local_r10 = 0;
    local_rdi = 0;
    if (((uint32_t)((uint32_t)(Arg5))) == 16) goto loc_008AE091;
    if (((uint32_t)((uint32_t)(Arg5))) == 17) goto loc_008AE350;
    if (((uint32_t)((uint32_t)(Arg5))) == 41) goto loc_008AE36A;
    if (((uint32_t)((uint32_t)(Arg5))) == 43) goto loc_008AE27E;
    if (((uint32_t)((uint32_t)(Arg5))) == 47) goto loc_008AE2AA;
    if (((uint32_t)((uint32_t)(Arg5))) == 53) goto loc_008AE3F0;
    if (((uint32_t)((uint32_t)(Arg5))) != 18) goto loc_008ADA63;
    *(uint32_t *)(*(uint64_t *)(result + 0x18) + 0x4C) = (uint32_t)((uint32_t)(v_stack_mD4));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m128 + 0x50))))) >> (3));
    Arg1 = (uint32_t)((Arg1) & (2));
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) | (4));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m128 + 0x50)))) & (32)) == 0) { Arg2 = (uint32_t)(Arg1); }
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(Arg2))) | (8));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m128 + 0x50)))) & (8)) == 0) { Arg1 = (uint32_t)(Arg2); }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m128 + 0x50)))) & (2)) != 0) goto loc_008ADD8B;
loc_008ADA3E:
    result = (uint32_t)((uint32_t)(Arg1));
    if (condition_is_above_or_equal) { result = (uint32_t)(Arg1); }
    *(uint32_t *)(*(uint64_t *)(result + 0x18) + 0x58) = (uint32_t)(result);
    *(uint32_t *)(*(uint64_t *)(result + 0x18) + 0x5C) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x98)));
    *(uint64_t *)(result + 0x38) = 12;
loc_008ADA63:
loc_008ADA68:
    if (0 != 0) goto loc_008AE0AA;
    result = (uint32_t)(*(uint32_t *)(result + 0x98));
    if (0 == 0) {
        Arg1 = v_stack_m128;
        result = ObfReferenceObject(Arg1, Arg2, (uint32_t)(*(uint32_t *)(v_stack_m128 + 0x50)), *(uint64_t *)(result + 0x18));
    }
    if (*(uint64_t *)(v_stack_m128 + 0xD0) != 0) goto loc_008ADFFD;
loc_008ADA93:
    local_rbx = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5A0))) >> (9));
    local_rbx = (uint32_t)((local_rbx) & (7));
    result = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220) + 0x2A0);
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220) + 0x2A0) != 0) {
        result = *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220) + 0x2A0) + 0x43C);
        if (((uint32_t)(local_rbx)) >= ((uint32_t)(result))) { local_rbx = (uint32_t)(result); }
    }
    if (((uint32_t)(local_rbx)) < 2) goto loc_008AE04C;
loc_008ADACF:
    local_rbx = (uint32_t)((local_rbx) << (17));
    local_rbx = (uint32_t)((local_rbx) + (0x20000ULL));
loc_008ADAD8:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m108))) & (0xFFF1FFFFULL));
    local_rbx = (uint32_t)((local_rbx) | ((uint32_t)(result)));
    *(uint32_t *)(v_stack_m108) = (uint32_t)(result);
    *(uint32_t *)(v_stack_mC8) = (uint32_t)(local_rbx);
    result = IoGetIoPriorityHint(result, Arg2, (uint32_t)(*(uint32_t *)(v_stack_m128 + 0x50)), *(uint64_t *)(result + 0x18));
    if (((uint32_t)(result)) < 2) goto loc_008AE0E9;
loc_008ADB08:
    if ((*(uint8_t *)(result + 0x47)) < 0) goto loc_008ADB1E;
    if (*(uint64_t *)(result + 0xC8) != 0) goto loc_008ADF83;
loc_008ADB1E:
    Arg1 = 0;
    v_stack_m110 = v_stack_m80;
loc_008ADB2D:
    if (0 != 0) goto loc_008AE21F;
    result = IofCallDriver(result, result, (uint32_t)(*(uint32_t *)(v_stack_m128 + 0x50)), *(uint64_t *)(result + 0x18));
    v_stack_m110 = (uint32_t)(result);
loc_008ADB4E:
    if (0 == 0) {
        Arg1 = v_stack_m128;
        result = ObDereferenceObjectDeferDelete(Arg1, result, (uint32_t)(*(uint32_t *)(v_stack_m128 + 0x50)), *(uint64_t *)(result + 0x18));
    }
loc_008ADB5F:
    if (((uint32_t)((uint32_t)(v_stack_m110))) != 259) goto loc_008ADE9D;
    if (0 == 0) goto loc_008ADF2B;
    local_r14 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m128 + 0x50))) & (4));
loc_008ADB87:
    if (((*(uint8_t *)(v_stack_m128 + 0x98)) & (127)) != 0) goto loc_008ADD9D;
    if ((*(uint32_t *)(v_stack_m128 + 0x9C)) == 0) goto loc_008ADD9D;
loc_008ADBA1:
loc_008ADBA9:
    result = IopReleaseFileObjectLock(v_stack_m128, result, (uint32_t)(*(uint32_t *)(v_stack_m128 + 0x50)), *(uint64_t *)(result + 0x18));
loc_008ADBAE:
    if (v_stack_m134 != 0) {
        Arg1 = 1;
        result = KeSetKernelStackSwapEnable(Arg1, result, (uint32_t)(*(uint32_t *)(v_stack_m128 + 0x50)), *(uint64_t *)(result + 0x18));
    }
loc_008ADBBE:
    Arg1 = (v_stack_m40) ^ (local_rsp);
    result = _security_check_cookie(Arg1, result, (uint32_t)(*(uint32_t *)(v_stack_m128 + 0x50)), *(uint64_t *)(result + 0x18));
    local_rsp = (local_rsp) + (304);
    return result;
loc_008ADBE2:
    if (((uint8_t)((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)))) == 1) {
        Arg1 = 0;
        result = KeSetKernelStackSwapEnable(Arg1, result, (uint32_t)(*(uint32_t *)(v_stack_m128 + 0x50)), *(uint64_t *)(result + 0x18));
        v_stack_p34 = (uint8_t)(result);
        Arg1 = result;
    }
    *(uint32_t *)(result + 0x10) = 4;
    v_stack_p80 = v_stack_pF0;
    goto loc_008AD8F8;
loc_008ADC1D:
    if (result + 16 == 0) goto loc_008AD85D;
loc_008ADC26:
    v_stack_pD0 = v_xmm0;
    v_stack_p30 = 0;
    v_stack_p39 = 0;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x656DDF)))) & (16)) != 0) goto loc_008ADCCE;
loc_008ADC49:
    result = 0;
loc_008ADC4B:
    v_stack_p68 = 0;
    v_stack_pE0 = 0;
    v_stack_p20 = 1;
    if (((uint32_t)(local_rbx)) == 4) goto loc_008ADC7E;
    goto loc_008ADC81;
loc_008ADC7E:
loc_008ADC81:
    result = guard_dispatch_icall((uint32_t)(*(uint32_t *)(v_stack_m128 + 0x38)), 1, v_stack_p70, v_stack_pD0);
    v_stack_p30 = (uint8_t)(result);
    if (v_stack_p68 != 0) {
        Arg2 = result;
        result = VfFastIoCheckState(v_stack_p68, Arg2, v_stack_p70, v_stack_pD0);
        result = v_stack_p30;
    }
    if ((uint8_t)(result) == 0) goto loc_008ADCF6;
    v_stack_p48 = (uint32_t)((uint32_t)(v_stack_pD0));
    v_stack_p39 = 1;
    *(uint64_t *)(v_stack_p50) = v_xmm0;
    goto loc_008ADCF6;
loc_008ADCCE:
    v_stack_p68 = *(uint64_t *)(1 + 0x8);
    result = MmIsDriverVerifying(*(uint64_t *)(1 + 0x8), Arg2, v_stack_p70, v_stack_pD0);
    if ((uint32_t)(result) == 0) goto loc_008ADC49;
    result = VfFastIoSnapState(v_stack_p68, Arg2, v_stack_p70, v_stack_pD0);
    goto loc_008ADC4B;
loc_008ADCF6:
    goto loc_008ADD61;
loc_008ADD61:
    if ((uint8_t)(result) == 0) goto loc_008AD85D;
loc_008ADD69:
    result = IopReleaseFileObjectLock((uint32_t)(*(uint32_t *)(v_stack_m128 + 0x38)), Arg2, v_stack_p70, v_stack_pD0);
loc_008ADD71:
    result = ObfDereferenceObject((uint32_t)(*(uint32_t *)(v_stack_m128 + 0x38)), Arg2, v_stack_p70, v_stack_pD0);
    goto loc_008ADBBE;
loc_008ADD8B:
    if ((((uint8_t)(v_stack_p70)) & (4)) != 0) goto loc_008AE1A9;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m128 + 0x38))) | (32));
    goto loc_008ADA3E;
loc_008ADD9D:
    Arg3 = 0;
    if ((uint32_t)(local_r14) != 0) { Arg3 = (uint32_t)(v_stack_p33); }
    v_stack_p20 = 0;
    Arg2 = 0;
    result = KeWaitForSingleObject((uint32_t)(*(uint32_t *)(v_stack_m128 + 0x38)) + 152, Arg2, Arg3, 1);
    if (((uint32_t)(result)) != 192) goto loc_008ADFBC;
loc_008ADDD2:
    if ((uint32_t)(local_r14) != 0) goto loc_008ADE37;
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5A0))))) != 0) goto loc_008ADE37;
    local_r12 = 0;
    if ((*(uint32_t *)(v_rip + 0x718F23)) != ((uint32_t)(local_r14))) goto loc_008AE03A;
loc_008ADE03:
    if ((*(uint32_t *)((uint32_t)(*(uint32_t *)(v_stack_m128 + 0x38)) + 0x9C)) == 0) goto loc_008AE0DC;
loc_008ADE10:
    result = *(uint64_t *)(gs_base + (0 + 0x188));
    if ((*(uint32_t *)(v_rip + 0x718F09)) != 0) {
        Arg1 = 1;
        Arg2 = (uint8_t)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, Arg3, 1);
    }
    if (0 == 0) goto loc_008ADB87;
loc_008ADE37:
    result = IopCancelAlertedRequest((uint32_t)(*(uint32_t *)(v_stack_m128 + 0x38)) + 152, result, Arg3, 1);
    goto loc_008ADBA1;
loc_008ADE4B:
    v_stack_p38 = 1;
    if (v_stack_p4C < 8) goto loc_008AE323;
    *(uint64_t *)(v_stack_p70) = *(uint64_t *)((uint32_t)(*(uint32_t *)(v_stack_m128 + 0x38)) + 0x68);
    v_stack_p38 = 0;
    *(uint32_t *)(v_stack_p50) = 0;
    *(uint64_t *)(v_stack_p50 + 0x8) = 8;
    goto loc_008ADD69;
loc_008ADE9D:
    v_stack_p78 = 0;
    if ((uint8_t)(v_cr8) == 0) {
        *(uint64_t *)(result + 0x50) = 0;
    }
    *(uint64_t *)(result + 0x48) = v_stack_p50;
    if ((*(uint32_t *)(v_rip + 0x718E4F)) != 0) goto loc_008AE072;
loc_008ADED7:
    v_stack_p20 = v_stack_p78;
    result = IopCompleteRequest(result + 120, v_stack_p118, v_stack_p78, v_stack_p40);
    if ((*(uint32_t *)(v_rip + 0x718E1D)) != 0) {
        Arg1 = 1;
        Arg2 = (uint8_t)((uint8_t)(v_cr8));
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, v_stack_p78, v_stack_p40);
    }
    if ((uint8_t)(v_cr8) == 0) goto loc_008ADBAE;
    goto loc_008ADBA9;
loc_008ADF2B:
    v_stack_p20 = 0;
    Arg4 = 0;
    Arg2 = 0;
    result = KeWaitForSingleObject(v_stack_p100, Arg2, 0, Arg4);
    if (((uint32_t)(result)) == 257) goto loc_008AE41D;
    if (((uint32_t)(result)) == 192) goto loc_008AE41D;
loc_008ADF60:
    *(uint64_t *)(v_stack_p50) = v_xmm0;
    goto loc_008ADBAE;
loc_008ADF83:
    if (((*(uint8_t *)(v_stack_p50)) & (2)) == 0) goto loc_008ADB1E;
    goto loc_008ADB2D;
loc_008ADF93:
    result = IopGetFileVolumeNameInformation(*(uint64_t *)((uint32_t)(v_stack_pF0) + 0x8), v_stack_p50, v_stack_p70, (uint32_t)(v_stack_p4C));
    result = ObfDereferenceObject((uint32_t)(v_stack_pF0), v_stack_p50, v_stack_p70, (uint32_t)(v_stack_p4C));
    goto loc_008ADBBE;
loc_008ADFBC:
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))))) == 257) goto loc_008ADDD2;
    goto loc_008ADBA1;
loc_008ADFCC:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r14))) >> (1));
    result = (uint8_t)((result) & (1));
    v_stack_p20 = (uint8_t)(result);
    Arg4 = 0;
    Arg3 = 0;
    result = IopExceptionCleanupEx((uint32_t)(v_stack_pF0), result, Arg3, Arg4);
    if (v_stack_p34 != 0) goto loc_008AE33B;
loc_008ADFF3:
    goto loc_008ADBBE;
loc_008ADFFD:
    if ((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)(result)) + 0x58))) == 0) goto loc_008ADA93;
    local_rbx = (uint32_t)(((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)(result)) + 0x58))) << (17));
    goto loc_008ADAD8;
loc_008AE010:
    if (((uint32_t)(local_rbx)) != 75) goto loc_008AD714;
    v_stack_p58 = 71;
    v_stack_p32 = 1;
    goto loc_008AD714;
loc_008AE02C:
    if (result != 0) goto loc_008ADC26;
    goto loc_008AD854;
loc_008AE03A:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(v_cr8), 1, Arg3, Arg4);
    goto loc_008ADE03;
loc_008AE04C:
    if (((uint8_t)(v_cr8)) != (*(uint64_t *)(gs_base + (0 + 0x188)))) goto loc_008ADACF;
    local_rbx = 71;
    if ((*(uint32_t *)((uint8_t)(v_cr8) + 0x5E0)) != 0) { local_rbx = 2; }
    goto loc_008ADACF;
loc_008AE072:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(local_rbx), 1, Arg3, Arg4);
    goto loc_008ADED7;
loc_008AE083:
    result = IoGetAttachedDevice(*(uint64_t *)((uint32_t)(v_stack_pF0) + 0x8), 1, Arg3, Arg4);
    goto loc_008AD77D;
loc_008AE091:
    result = IopGetModeInformation(v_stack_p40, 1, Arg3, *(uint64_t *)(result + 0x18));
    *(uint32_t *)(*(uint64_t *)(result + 0x18)) = (uint32_t)(result);
    *(uint64_t *)(result + 0x38) = 4;
loc_008AE0AA:
    *(uint32_t *)(result + 0x30) = (uint32_t)((uint32_t)(v_stack_pF0));
    goto loc_008ADB5F;
loc_008AE0B2:
    v_stack_p20 = v_stack_p37;
    result = IopWaitAndAcquireFileObjectLock(v_stack_p40, 0, (uint8_t)(result), result);
    goto loc_008AD810;
loc_008AE0DC:
    local_r12 = ((*(uint8_t *)(result + 0x44)) == 1) ? 1 : 0;
    goto loc_008ADE10;
loc_008AE0E9:
    if ((*(uint8_t *)(v_stack_p40)) != 0) goto loc_008ADB08;
    if (*(uint64_t *)(v_stack_p68) == 0) goto loc_008AE11A;
    if (((*(uint32_t *)(*(uint64_t *)(v_stack_p68) + 0x74)) & (0x400ULL)) != 0) goto loc_008ADB08;
    if (sign_flag) goto loc_008ADB08;
loc_008AE11A:
    local_rbx = (uint32_t)((local_rbx) & (0xFFF1FFFFULL));
    local_rbx = (uint32_t)((local_rbx) | (0x60000ULL));
    *(uint32_t *)(local_r14) = (uint32_t)(local_rbx);
    goto loc_008ADB08;
loc_008AE134:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_r14)))) & (2)) != 0) goto loc_008AE32E;
loc_008AE13F:
    result = ObfDereferenceObject(v_stack_p40, 0, (uint8_t)(result), result);
    goto loc_008ADBBE;
loc_008AE151:
    v_stack_p36 = 1;
    if (v_stack_p4C < 1) goto loc_008AE2F2;
    Arg1 = (uint8_t)((*(uint8_t *)(*(uint64_t *)(v_stack_p40 + 0x8) + 0x34)) >> (4));
    Arg1 = (uint8_t)((Arg1) & (1));
    *(uint8_t *)(v_stack_p70) = (uint8_t)(Arg1);
    v_stack_p36 = 0;
    *(uint32_t *)(v_stack_p50) = (uint32_t)(result);
    *(uint64_t *)(v_stack_p50 + 0x8) = 1;
    goto loc_008ADD71;
loc_008AE1A9:
    Arg1 = (uint32_t)((Arg1) | (16));
    goto loc_008ADA3E;
loc_008AE1B1:
    if (((uint32_t)(local_r14)) < 4) goto loc_008AE266;
    v_stack_p35 = 1;
    *(uint32_t *)(1) = (uint32_t)((uint32_t)(v_stack_p94));
    v_stack_p35 = 0;
    *(uint32_t *)(v_stack_p50) = (uint32_t)(result);
    *(uint64_t *)(v_stack_p50 + 0x8) = 4;
    goto loc_008AE20D;
loc_008AE20D:
    result = ObfDereferenceObject(v_stack_p40, 0, v_stack_p70, result);
    goto loc_008ADBBE;
loc_008AE21F:
    v_stack_p118 = v_xmm0;
    v_stack_p118 = v_xmm0;
    result = IoSetActivityIdThread(v_stack_p118, 0, v_stack_p70, result);
    result = IofCallDriver(1, result, v_stack_p70, result);
    v_stack_p58 = (uint32_t)(result);
    result = IoSetActivityIdThread(result, result, v_stack_p70, result);
    goto loc_008ADB4E;
loc_008AE266:
    result = ObfDereferenceObject(v_stack_p40, result, v_stack_p70, result);
    goto loc_008ADBBE;
loc_008AE27E:
    if (*(uint64_t *)(v_stack_p40 + 0xD0) != 0) goto loc_008AE308;
loc_008AE293:
    *(uint32_t *)(*(uint64_t *)(result + 0x18)) = 2;
    *(uint64_t *)(result + 0x38) = 4;
    *(uint32_t *)(result + 0x30) = (uint32_t)(v_stack_p40);
    goto loc_008ADB5F;
loc_008AE2AA:
    v_stack_p78 = (uint32_t)(v_stack_p40);
    result = IopQueryProcessIdsUsingFile(v_stack_p40, *(uint64_t *)(result + 0x18), (uint32_t)(v_stack_p4C), v_stack_p78);
    v_stack_p32 = 1;
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0xC0000004ULL)))) goto loc_008AE38B;
    *(uint64_t *)(result + 0x38) = (uint32_t)(v_stack_p78);
    goto loc_008ADA63;
loc_008AE2F2:
    result = ObfDereferenceObject((uint32_t)((uint32_t)(result)), *(uint64_t *)(result + 0x18), (uint32_t)(v_stack_p4C), v_stack_p78);
    goto loc_008ADBBE;
loc_008AE308:
    if ((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)((uint32_t)(0xC0000004ULL))) + 0x58))) == 0) goto loc_008AE293;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)((uint32_t)(0xC0000004ULL))) + 0x58))) - 1);
    *(uint32_t *)((uint32_t)((uint32_t)(result))) = (uint32_t)(result);
    *(uint64_t *)(result + 0x38) = 4;
    *(uint32_t *)(result + 0x30) = (uint32_t)((uint32_t)((uint32_t)(result)));
    goto loc_008ADB5F;
loc_008AE323:
    goto loc_008ADD69;
loc_008AE32E:
    result = IopReleaseFileObjectLock((uint32_t)((uint32_t)(result)), *(uint64_t *)(result + 0x18), (uint32_t)(v_stack_p4C), v_stack_p78);
    goto loc_008AE13F;
loc_008AE33B:
    result = KeSetKernelStackSwapEnable(1, *(uint64_t *)(result + 0x18), (uint32_t)(v_stack_p4C), v_stack_p78);
    goto loc_008ADFF3;
loc_008AE347:
    goto loc_008AD9A1;
loc_008AE350:
    *(uint32_t *)(*(uint64_t *)(result + 0x18)) = (uint32_t)((uint32_t)(*(uint32_t *)(1 + 0x98)));
    *(uint64_t *)(result + 0x38) = 4;
    goto loc_008AE0AA;
loc_008AE36A:
    *(uint32_t *)(*(uint64_t *)(result + 0x18)) = (uint32_t)((uint32_t)((uint32_t)(result)));
    Arg2 = 0;
    *(uint32_t *)(*(uint64_t *)(result + 0x18)) = 2;
loc_008AE38B:
    *(uint64_t *)(v_stack_p50 + 0x8) = (uint32_t)(v_stack_p78);
    goto loc_008ADA68;
loc_008AE3F0:
    result = IopGetNumaNodeInformation(v_stack_p40, *(uint64_t *)(result + 0x18), (uint32_t)(v_stack_p4C), v_stack_p78);
    if (sign_flag) goto loc_008ADA68;
    *(uint64_t *)(result + 0x38) = 2;
    goto loc_008ADA68;
loc_008AE41D:
    result = IopCancelAlertedRequest(v_stack_p100, result, (uint32_t)(v_stack_p4C), v_stack_p78);
    goto loc_008ADF60;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008AD630&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
