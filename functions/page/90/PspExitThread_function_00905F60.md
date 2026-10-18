# PspExitThread

- RVA: `0x00905F60`–`0x009067CB` (길이 `2,155` bytes)
- VA: `0x0000000140905F60`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00088C98`
- 디코드: `469`개 명령, `2,155/2,155` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **60**; 고유 호출 대상: **45**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x00905FC6` → [PspClearProcessThreadCidRefs](PspClearProcessThreadCidRefs_function_009071D8.md) (function, `0x009071D8`)
- `0x00905FEB` → [KiLowerIrqlProcessIrqlFlags](../../text/4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0090602B` → [PspEmptyPropertySet](PspEmptyPropertySet_function_00905D04.md) (function, `0x00905D04`)
- `0x00906033` → [PspRevertContainerImpersonation](../../text/39/PspRevertContainerImpersonation_function_00395070.md) (function, `0x00395070`)
- `0x0090603F` → [ExWaitForRundownProtectionRelease](../../text/2A/ExWaitForRundownProtectionRelease_function_002A4CB0.md) (function, `0x002A4CB0`)
- `0x00906079` → [EtwTraceThread](EtwTraceThread_function_00905700.md) (function, `0x00905700`)
- `0x009060A2` → [PspCallThreadNotifyRoutines](PspCallThreadNotifyRoutines_function_00905530.md) (function, `0x00905530`)
- `0x009060B6` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x009060D1` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x00906139` → [PspUnlockProcessExclusive](../../text/46/PspUnlockProcessExclusive_function_004601C0.md) (function, `0x004601C0`)
- `0x009061A2` → [PsCaptureExceptionPort](PsCaptureExceptionPort_function_00904CB0.md) (function, `0x00904CB0`)
- `0x009061D3` → [LpcRequestPort](../88/LpcRequestPort_function_0088A940.md) (function, `0x0088A940`)
- `0x009061F1` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00906235` → [PspUpdateCalloutParameters](../../text/49/PspUpdateCalloutParameters_function_0049BBA4.md) (function, `0x0049BBA4`)
- `0x0090623E` → [PsSessionGetWin32Callouts](../../text/47/PsSessionGetWin32Callouts_function_00474F98.md) (function, `0x00474F98`)
- `0x00906251` → [ExCallCallBack](ExCallCallBack_function_009054B4.md) (function, `0x009054B4`)
- `0x00906296` → [RtlpFlsDataCleanup](../A1/RtlpFlsDataCleanup_function_00A1D998.md) (function, `0x00A1D998`)
- `0x0090629B` → [KeLeaveGuardedRegion](../../text/2E/KeLeaveGuardedRegion_function_002E2C40.md) (function, `0x002E2C40`)
- `0x009062A0` → [IoCancelThreadIo](IoCancelThreadIo_function_00906830.md) (function, `0x00906830`)
- `0x009062A5` → [ExTimerRundown](../../text/39/ExTimerRundown_function_00391394.md) (function, `0x00391394`)
- `0x009062AD` → [CmNotifyRunDown](CmNotifyRunDown_function_00906984.md) (function, `0x00906984`)
- `0x009062BB` → [KiRundownMutants](../../text/48/KiRundownMutants_function_00488504.md) (function, `0x00488504`)
- `0x009062C3` → [PspSchedulerSharedDataRegionSlotFree](PspSchedulerSharedDataRegionSlotFree_function_00905AD4.md) (function, `0x00905AD4`)
- `0x009062EA` → [PspLockUnlockTebAccessExclusive](../../text/4E/PspLockUnlockTebAccessExclusive_function_004E9A2C.md) (function, `0x004E9A2C`)
- `0x00906352` → [ZwFreeVirtualMemory](../../text/6A/ZwFreeVirtualMemory_function_006AD490.md) (function, `0x006AD490`)
- `0x0090636F` → [ObCloseHandle](../8A/ObCloseHandle_function_008A1870.md) (function, `0x008A1870`)
- `0x009063B7` → [ZwFreeVirtualMemory](../../text/6A/ZwFreeVirtualMemory_function_006AD490.md) (function, `0x006AD490`)
- `0x00906418` → [MmDeleteTeb](../87/MmDeleteTeb_function_0087FAC0.md) (function, `0x0087FAC0`)
- `0x0090641D` → [KeQuerySystemTimeUnsafe](../../text/48/KeQuerySystemTimeUnsafe_function_00484438.md) (function, `0x00484438`)
- `0x00906432` → [KeQuerySystemTimePrecise](../../text/37/KeQuerySystemTimePrecise_function_0037DA40.md) (function, `0x0037DA40`)
- `0x00906443` → [KeRundownApcQueues](KeRundownApcQueues_function_00905C44.md) (function, `0x00905C44`)
- `0x00906485` → [PspThreadIndexCleanup](PspThreadIndexCleanup_function_009067D4.md) (function, `0x009067D4`)
- `0x009064AC` → [KeTerminateThread](../../text/35/KeTerminateThread_function_00355138.md) (function, `0x00355138`)
- `0x009064D7` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x009064ED` → [PspExitLastThread](PspExitLastThread_function_00904184.md) (function, `0x00904184`)
- `0x00906506` → [PspExitLastThread](PspExitLastThread_function_00904184.md) (function, `0x00904184`)
- `0x0090651F` → [PspExitLastThread](PspExitLastThread_function_00904184.md) (function, `0x00904184`)
- `0x00906542` → [RtlpFlsSlotDataValidateEmpty](../../text/49/RtlpFlsSlotDataValidateEmpty_function_00497108.md) (function, `0x00497108`)
- `0x0090656A` → [RtlpFlsDataCleanup](../A1/RtlpFlsDataCleanup_function_00A1D998.md) (function, `0x00A1D998`)
- `0x0090656F` → [KeLeaveGuardedRegion](../../text/2E/KeLeaveGuardedRegion_function_002E2C40.md) (function, `0x002E2C40`)
- `0x009065B4` → [PspFreeCurrentThreadUserShadowStack](../87/PspFreeCurrentThreadUserShadowStack_function_0087FD7C.md) (function, `0x0087FD7C`)
- `0x009065C9` → [KeDelayExecutionThread](../../text/20/KeDelayExecutionThread_function_00209550.md) (function, `0x00209550`)
- `0x00906601` → [PspExitLastThread](PspExitLastThread_function_00904184.md) (function, `0x00904184`)
- `0x00906630` → [LpcRequestPort](../88/LpcRequestPort_function_0088A940.md) (function, `0x0088A940`)
- `0x0090664F` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00906660` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00906673` → [PoDeletePowerRequest](../A4/PoDeletePowerRequest_function_00A48F00.md) (function, `0x00A48F00`)
- `0x009066A0` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x009066B9` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x009066CF` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x009066DA` → [KeSetThreadChargeOnlySchedulingGroup](../../text/39/KeSetThreadChargeOnlySchedulingGroup_function_00392F20.md) (function, `0x00392F20`)
- `0x009066EB` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00906719` → [DbgkExitProcess](../71/DbgkExitProcess_function_00710998.md) (function, `0x00710998`)
- `0x00906733` → [KeUnsecureThread](../../text/5B/KeUnsecureThread_function_005B90F0.md) (function, `0x005B90F0`)
- `0x00906748` → [MmUnlockPages](../../text/29/MmUnlockPages_function_0029EEE0.md) (function, `0x0029EEE0`)
- `0x0090675A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0090676F` → [KeDelayExecutionThread](../../text/20/KeDelayExecutionThread_function_00209550.md) (function, `0x00209550`)
- `0x0090678B` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x009067A4` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x009067BA` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [KiSchedulerApcTerminate](KiSchedulerApcTerminate_function_00905D40.md) at `0x00905D6F`
- [PspTerminateThreadByPointer](PspTerminateThreadByPointer_function_00905E80.md) at `0x00905ECA`
- [NtTerminateProcess](../AE/NtTerminateProcess_function_00AEC320.md) at `0x00AEC587`

### Static image references
- `0x00905FDD` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x00906067` → RVA `0x00FC6B00` (`ALMOSTRO`; read)
- `0x0090616F` → RVA `0x00F475F8` (`.data`; read)
- `0x009065BE` → RVA `0x000118C8` (`.rdata`; read)
- `0x00906791` → RVA `0x00FD9F80` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **36**
  - `0x00905FEB` → [KiLowerIrqlProcessIrqlFlags](../../text/4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (`PAGE` → `.text`)
  - `0x00906033` → [PspRevertContainerImpersonation](../../text/39/PspRevertContainerImpersonation_function_00395070.md) (`PAGE` → `.text`)
  - `0x0090603F` → [ExWaitForRundownProtectionRelease](../../text/2A/ExWaitForRundownProtectionRelease_function_002A4CB0.md) (`PAGE` → `.text`)
  - `0x009060B6` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x009060D1` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x00906139` → [PspUnlockProcessExclusive](../../text/46/PspUnlockProcessExclusive_function_004601C0.md) (`PAGE` → `.text`)
  - `0x009061F1` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00906235` → [PspUpdateCalloutParameters](../../text/49/PspUpdateCalloutParameters_function_0049BBA4.md) (`PAGE` → `.text`)
  - `0x0090623E` → [PsSessionGetWin32Callouts](../../text/47/PsSessionGetWin32Callouts_function_00474F98.md) (`PAGE` → `.text`)
  - `0x0090629B` → [KeLeaveGuardedRegion](../../text/2E/KeLeaveGuardedRegion_function_002E2C40.md) (`PAGE` → `.text`)
  - `0x009062A5` → [ExTimerRundown](../../text/39/ExTimerRundown_function_00391394.md) (`PAGE` → `.text`)
  - `0x009062BB` → [KiRundownMutants](../../text/48/KiRundownMutants_function_00488504.md) (`PAGE` → `.text`)
  - `0x009062EA` → [PspLockUnlockTebAccessExclusive](../../text/4E/PspLockUnlockTebAccessExclusive_function_004E9A2C.md) (`PAGE` → `.text`)
  - `0x00906352` → [ZwFreeVirtualMemory](../../text/6A/ZwFreeVirtualMemory_function_006AD490.md) (`PAGE` → `.text`)
  - `0x009063B7` → [ZwFreeVirtualMemory](../../text/6A/ZwFreeVirtualMemory_function_006AD490.md) (`PAGE` → `.text`)
  - `0x0090641D` → [KeQuerySystemTimeUnsafe](../../text/48/KeQuerySystemTimeUnsafe_function_00484438.md) (`PAGE` → `.text`)
  - `0x00906432` → [KeQuerySystemTimePrecise](../../text/37/KeQuerySystemTimePrecise_function_0037DA40.md) (`PAGE` → `.text`)
  - `0x009064AC` → [KeTerminateThread](../../text/35/KeTerminateThread_function_00355138.md) (`PAGE` → `.text`)
  - `0x009064D7` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x00906542` → [RtlpFlsSlotDataValidateEmpty](../../text/49/RtlpFlsSlotDataValidateEmpty_function_00497108.md) (`PAGE` → `.text`)
  - `0x0090656F` → [KeLeaveGuardedRegion](../../text/2E/KeLeaveGuardedRegion_function_002E2C40.md) (`PAGE` → `.text`)
  - `0x009065C9` → [KeDelayExecutionThread](../../text/20/KeDelayExecutionThread_function_00209550.md) (`PAGE` → `.text`)
  - `0x0090664F` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00906660` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x009066A0` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x009066B9` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x009066CF` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x009066DA` → [KeSetThreadChargeOnlySchedulingGroup](../../text/39/KeSetThreadChargeOnlySchedulingGroup_function_00392F20.md) (`PAGE` → `.text`)
  - `0x009066EB` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00906733` → [KeUnsecureThread](../../text/5B/KeUnsecureThread_function_005B90F0.md) (`PAGE` → `.text`)
  - `0x00906748` → [MmUnlockPages](../../text/29/MmUnlockPages_function_0029EEE0.md) (`PAGE` → `.text`)
  - `0x0090675A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0090676F` → [KeDelayExecutionThread](../../text/20/KeDelayExecutionThread_function_00209550.md) (`PAGE` → `.text`)
  - `0x0090678B` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x009067A4` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x009067BA` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x0090614F` → [sub_00B20D7E](../B2/Unknown_function_00B20D7E.md) (`tail-transfer`)
  - `0x00906176` → [sub_00B20D7E + 0x89](../B2/Unknown_function_00B20D7E.md) (`tail-transfer`)
  - `0x0090670C` → [sub_00B20D7E + 0x7B](../B2/Unknown_function_00B20D7E.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00905F60  4C 8B DC                        mov r11, rsp
00905F63  53                              push rbx
00905F64  56                              push rsi
00905F65  57                              push rdi
00905F66  41 54                           push r12
00905F68  41 55                           push r13
00905F6A  41 56                           push r14
00905F6C  41 57                           push r15
00905F6E  48 81 EC C0 00 00 00            sub rsp, 0xc0
00905F75  44 8B E9                        mov r13d, ecx
00905F78  0F 57 C0                        xorps xmm0, xmm0
00905F7B  0F 11 44 24 40                  movups xmmword ptr [rsp + 0x40], xmm0
00905F80  0F 11 44 24 50                  movups xmmword ptr [rsp + 0x50], xmm0
00905F85  0F 11 44 24 60                  movups xmmword ptr [rsp + 0x60], xmm0
00905F8A  33 C0                           xor eax, eax
00905F8C  41 0F 11 43 98                  movups xmmword ptr [r11 - 0x68], xmm0
00905F91  49 89 43 A8                     mov qword ptr [r11 - 0x58], rax
00905F95  41 89 43 B0                     mov dword ptr [r11 - 0x50], eax
00905F99  65 48 8B 3C 25 88 01 00 00      mov rdi, qword ptr gs:[0x188]
00905FA2  48 89 BC 24 88 00 00 00         mov qword ptr [rsp + 0x88], rdi
00905FAA  4C 8B B7 20 02 00 00            mov r14, qword ptr [rdi + 0x220]
00905FB1  4C 89 B4 24 80 00 00 00         mov qword ptr [rsp + 0x80], r14
00905FB9  4C 8B C7                        mov r8, rdi
00905FBC  48 8B 97 10 05 00 00            mov rdx, qword ptr [rdi + 0x510]
00905FC3  48 8B CF                        mov rcx, rdi
00905FC6  E8 0D 12 00 00                  call 0x1409071d8
00905FCB  4C 8B 87 B8 00 00 00            mov r8, qword ptr [rdi + 0xb8]
00905FD2  4D 3B F0                        cmp r14, r8
00905FD5  0F 85 B0 06 00 00               jne 0x14090668b
00905FDB  33 F6                           xor esi, esi
00905FDD  39 35 3D 0D 6C 00               cmp dword ptr [rip + 0x6c0d3d], esi
00905FE3  74 0B                           je 0x140905ff0
00905FE5  44 0F 20 C1                     mov rcx, cr8
00905FE9  33 D2                           xor edx, edx
00905FEB  E8 A8 F6 BE FF                  call 0x1404f5698
00905FF0  44 0F 22 C6                     mov cr8, rsi
00905FF4  8B 87 A4 05 00 00               mov eax, dword ptr [rdi + 0x5a4]
00905FFA  41 BF 01 00 00 00               mov r15d, 1
00906000  41 84 C7                        test r15b, al
00906003  0F 85 9D 06 00 00               jne 0x1409066a6
00906009  8B 87 E4 01 00 00               mov eax, dword ptr [rdi + 0x1e4]
0090600F  85 C0                           test eax, eax
00906011  0F 85 A8 06 00 00               jne 0x1409066bf
00906017  48 39 B7 68 05 00 00            cmp qword ptr [rdi + 0x568], rsi
0090601E  0F 85 B1 06 00 00               jne 0x1409066d5
00906024  48 8D 8F 58 06 00 00            lea rcx, [rdi + 0x658]
0090602B  E8 D4 FC FF FF                  call 0x140905d04
00906030  48 8B CF                        mov rcx, rdi
00906033  E8 38 F0 A8 FF                  call 0x140395070
00906038  48 8D 8F 88 05 00 00            lea rcx, [rdi + 0x588]
0090603F  E8 6C EC 99 FF                  call 0x1402a4cb0
00906044  48 8B 8F 70 05 00 00            mov rcx, qword ptr [rdi + 0x570]
0090604B  48 85 C9                        test rcx, rcx
0090604E  0F 85 1F 06 00 00               jne 0x140906673
00906054  44 0F B6 E6                     movzx r12d, sil
00906058  44 88 A4 24 08 01 00 00         mov byte ptr [rsp + 0x108], r12b
00906060  44 89 AF D8 05 00 00            mov dword ptr [rdi + 0x5d8], r13d
00906067  8B 05 93 0A 6C 00               mov eax, dword ptr [rip + 0x6c0a93]
0090606D  A8 02                           test al, 2
0090606F  74 0D                           je 0x14090607e
00906071  45 33 C0                        xor r8d, r8d
00906074  33 D2                           xor edx, edx
00906076  48 8B CF                        mov rcx, rdi
00906079  E8 82 F6 FF FF                  call 0x140905700
0090607E  48 83 C8 FF                     or rax, 0xffffffffffffffff
00906082  66 01 87 E4 01 00 00            add word ptr [rdi + 0x1e4], ax
00906089  90                              nop
0090608A  41 8B 86 FC 05 00 00            mov eax, dword ptr [r14 + 0x5fc]
00906091  41 84 C7                        test r15b, al
00906094  0F 85 39 05 00 00               jne 0x1409065d3
0090609A  45 33 C0                        xor r8d, r8d
0090609D  33 D2                           xor edx, edx
0090609F  48 8B CF                        mov rcx, rdi
009060A2  E8 89 F4 FF FF                  call 0x140905530
009060A7  49 8D 9E C8 01 00 00            lea rbx, [r14 + 0x1c8]
009060AE  45 33 C0                        xor r8d, r8d
009060B1  33 D2                           xor edx, edx
009060B3  48 8B CB                        mov rcx, rbx
009060B6  E8 75 A1 90 FF                  call 0x140210230
009060BB  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
009060C0  F0 48 0F BA 2B 00               lock bts qword ptr [rbx], 0
009060C6  73 13                           jae 0x1409060db
009060C8  4C 8B C3                        mov r8, rbx
009060CB  48 8B D0                        mov rdx, rax
009060CE  48 8B CB                        mov rcx, rbx
009060D1  E8 BA 9B 90 FF                  call 0x14020fc90
009060D6  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
009060DB  48 85 C0                        test rax, rax
009060DE  74 04                           je 0x1409060e4
009060E0  44 88 78 0A                     mov byte ptr [rax + 0xa], r15b
009060E4  41 8B 86 80 03 00 00            mov eax, dword ptr [r14 + 0x380]
009060EB  41 2B C7                        sub eax, r15d
009060EE  41 89 86 80 03 00 00            mov dword ptr [r14 + 0x380], eax
009060F5  41 8B 86 FC 05 00 00            mov eax, dword ptr [r14 + 0x5fc]
009060FC  41 84 C7                        test r15b, al
009060FF  0F 85 74 04 00 00               jne 0x140906579
00906105  41 8B 86 80 03 00 00            mov eax, dword ptr [r14 + 0x380]
0090610C  85 C0                           test eax, eax
0090610E  45 0F 44 E7                     cmove r12d, r15d
00906112  44 88 A4 24 08 01 00 00         mov byte ptr [rsp + 0x108], r12b
0090611A  45 84 E4                        test r12b, r12b
0090611D  0F 85 C2 04 00 00               jne 0x1409065e5
00906123  41 81 FD 4B 00 00 C0            cmp r13d, 0xc000004b
0090612A  74 07                           je 0x140906133
0090612C  45 89 AE 8C 03 00 00            mov dword ptr [r14 + 0x38c], r13d
00906133  48 8B D7                        mov rdx, rdi
00906136  49 8B CE                        mov rcx, r14
00906139  E8 82 A0 B5 FF                  call 0x1404601c0
0090613E  48 8B 87 98 06 00 00            mov rax, qword ptr [rdi + 0x698]
00906145  48 C7 C1 FD FF FF FF            mov rcx, 0xfffffffffffffffd
0090614C  48 3B C1                        cmp rax, rcx
0090614F  0F 85 29 AC 21 00               jne 0x140b20d7e
00906155  49 39 B6 08 03 00 00            cmp qword ptr [r14 + 0x308], rsi
0090615C  0F 85 9A 05 00 00               jne 0x1409066fc
00906162  45 84 BE 70 01 00 00            test byte ptr [r14 + 0x170], r15b
00906169  0F 85 B4 05 00 00               jne 0x140906723
0090616F  40 38 35 82 14 64 00            cmp byte ptr [rip + 0x641482], sil
00906176  0F 85 8B AC 21 00               jne 0x140b20e07
0090617C  45 84 E4                        test r12b, r12b
0090617F  0F 85 58 03 00 00               jne 0x1409064dd
00906185  4C 8B AF E8 04 00 00            mov r13, qword ptr [rdi + 0x4e8]
0090618C  4D 85 ED                        test r13, r13
0090618F  0F 85 76 04 00 00               jne 0x14090660b
00906195  8B 87 A0 05 00 00               mov eax, dword ptr [rdi + 0x5a0]
0090619B  A8 02                           test al, 2
0090619D  74 57                           je 0x1409061f6
0090619F  49 8B CE                        mov rcx, r14
009061A2  E8 09 EB FF FF                  call 0x140904cb0
009061A7  48 8B D8                        mov rbx, rax
009061AA  48 85 C0                        test rax, rax
009061AD  74 47                           je 0x1409061f6
009061AF  C7 44 24 40 08 00 30 00         mov dword ptr [rsp + 0x40], 0x300008
009061B7  C7 44 24 44 06 00 00 00         mov dword ptr [rsp + 0x44], 6
009061BF  48 8B 8F C0 04 00 00            mov rcx, qword ptr [rdi + 0x4c0]
009061C6  48 89 4C 24 68                  mov qword ptr [rsp + 0x68], rcx
009061CB  48 8D 54 24 40                  lea rdx, [rsp + 0x40]
009061D0  48 8B CB                        mov rcx, rbx
009061D3  E8 68 47 F8 FF                  call 0x14088a940
009061D8  3D 9A 00 00 C0                  cmp eax, 0xc000009a
009061DD  0F 84 DB 03 00 00               je 0x1409065be
009061E3  3D 17 00 00 C0                  cmp eax, 0xc0000017
009061E8  0F 84 D0 03 00 00               je 0x1409065be
009061EE  48 8B CB                        mov rcx, rbx
009061F1  E8 5A 31 9F FF                  call 0x1402f9350
009061F6  48 8B 87 C8 01 00 00            mov rax, qword ptr [rdi + 0x1c8]
009061FD  48 85 C0                        test rax, rax
00906200  74 54                           je 0x140906256
00906202  48 89 BC 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rdi
0090620A  44 89 BC 24 A8 00 00 00         mov dword ptr [rsp + 0xa8], r15d
00906212  33 C0                           xor eax, eax
00906214  48 89 84 24 B4 00 00 00         mov qword ptr [rsp + 0xb4], rax
0090621C  48 89 84 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rax
00906224  45 33 C9                        xor r9d, r9d
00906227  45 33 C0                        xor r8d, r8d
0090622A  48 8D 94 24 90 00 00 00         lea rdx, [rsp + 0x90]
00906232  41 8B CF                        mov ecx, r15d
00906235  E8 6A 59 B9 FF                  call 0x14049bba4
0090623A  85 C0                           test eax, eax
0090623C  74 18                           je 0x140906256
0090623E  E8 55 ED B6 FF                  call 0x140474f98
00906243  48 8B C8                        mov rcx, rax
00906246  4C 8D 84 24 90 00 00 00         lea r8, [rsp + 0x90]
0090624E  49 8B D7                        mov rdx, r15
00906251  E8 5E F2 FF FF                  call 0x1409054b4
00906256  45 84 E4                        test r12b, r12b
00906259  0F 85 98 02 00 00               jne 0x1409064f7
0090625F  8B 47 78                        mov eax, dword ptr [rdi + 0x78]
00906262  A8 40                           test al, 0x40
00906264  0F 84 0F 05 00 00               je 0x140906779
0090626A  48 8B 97 F0 06 00 00            mov rdx, qword ptr [rdi + 0x6f0]
00906271  44 09 BF F0 06 00 00            or dword ptr [rdi + 0x6f0], r15d
00906278  49 83 CD FF                     or r13, 0xffffffffffffffff
0090627C  48 85 D2                        test rdx, rdx
0090627F  74 1F                           je 0x1409062a0
00906281  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0090628A  66 44 01 A8 E6 01 00 00         add word ptr [rax + 0x1e6], r13w
00906292  90                              nop
00906293  45 8B C7                        mov r8d, r15d
00906296  E8 FD 76 11 00                  call 0x140a1d998
0090629B  E8 A0 C9 9D FF                  call 0x1402e2c40
009062A0  E8 8B 05 00 00                  call 0x140906830
009062A5  E8 EA B0 A8 FF                  call 0x140391394
009062AA  48 8B CF                        mov rcx, rdi
009062AD  E8 D2 06 00 00                  call 0x140906984
009062B2  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
009062BB  E8 44 22 B8 FF                  call 0x140488504
009062C0  48 8B CF                        mov rcx, rdi
009062C3  E8 0C F8 FF FF                  call 0x140905ad4
009062C8  48 8B 9F F0 00 00 00            mov rbx, qword ptr [rdi + 0xf0]
009062CF  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
009062D4  48 85 DB                        test rbx, rbx
009062D7  0F 84 40 01 00 00               je 0x14090641d
009062DD  48 89 B7 F0 00 00 00            mov qword ptr [rdi + 0xf0], rsi
009062E4  48 8B D7                        mov rdx, rdi
009062E7  48 8B CF                        mov rcx, rdi
009062EA  E8 3D 37 BE FF                  call 0x1404e9a2c
009062EF  F7 47 74 00 04 00 00            test dword ptr [rdi + 0x74], 0x400
009062F6  0F 85 21 01 00 00               jne 0x14090641d
009062FC  41 8B 86 F4 01 00 00            mov eax, dword ptr [r14 + 0x1f4]
00906303  A9 08 00 00 40                  test eax, 0x40000008
00906308  0F 85 0F 01 00 00               jne 0x14090641d
0090630E  8B 87 A0 05 00 00               mov eax, dword ptr [rdi + 0x5a0]
00906314  A8 02                           test al, 2
00906316  74 48                           je 0x140906360
00906318  48 8B 83 78 14 00 00            mov rax, qword ptr [rbx + 0x1478]
0090631F  48 89 84 24 10 01 00 00         mov qword ptr [rsp + 0x110], rax
00906327  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
0090632C  48 89 B4 24 18 01 00 00         mov qword ptr [rsp + 0x118], rsi
00906334  48 89 B4 24 18 01 00 00         mov qword ptr [rsp + 0x118], rsi
0090633C  41 B9 00 80 00 00               mov r9d, 0x8000
00906342  4C 8D 84 24 18 01 00 00         lea r8, [rsp + 0x118]
0090634A  48 8D 54 24 70                  lea rdx, [rsp + 0x70]
0090634F  49 8B CD                        mov rcx, r13
00906352  E8 39 71 DA FF                  call 0x1406ad490
00906357  49 39 B6 10 03 00 00            cmp qword ptr [r14 + 0x310], rsi
0090635E  75 16                           jne 0x140906376
00906360  48 8B 8B A8 16 00 00            mov rcx, qword ptr [rbx + 0x16a8]
00906367  48 85 C9                        test rcx, rcx
0090636A  74 61                           je 0x1409063cd
0090636C  41 8A D7                        mov dl, r15b
0090636F  E8 FC B4 F9 FF                  call 0x1408a1870
00906374  EB 57                           jmp 0x1409063cd
00906376  41 0F B7 86 EC 06 00 00         movzx eax, word ptr [r14 + 0x6ec]
0090637E  B9 4C 01 00 00                  mov ecx, 0x14c
00906383  66 3B C1                        cmp ax, cx
00906386  75 36                           jne 0x1409063be
00906388  41 8A C7                        mov al, r15b
0090638B  84 C0                           test al, al
0090638D  74 D1                           je 0x140906360
0090638F  8B 83 0C 2E 00 00               mov eax, dword ptr [rbx + 0x2e0c]
00906395  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
0090639A  48 89 74 24 38                  mov qword ptr [rsp + 0x38], rsi
0090639F  48 89 74 24 38                  mov qword ptr [rsp + 0x38], rsi
009063A4  41 B9 00 80 00 00               mov r9d, 0x8000
009063AA  4C 8D 44 24 38                  lea r8, [rsp + 0x38]
009063AF  48 8D 54 24 78                  lea rdx, [rsp + 0x78]
009063B4  49 8B CD                        mov rcx, r13
009063B7  E8 D4 70 DA FF                  call 0x1406ad490
009063BC  EB A2                           jmp 0x140906360
009063BE  B9 C4 01 00 00                  mov ecx, 0x1c4
009063C3  66 3B C1                        cmp ax, cx
009063C6  40 8A C6                        mov al, sil
009063C9  75 C0                           jne 0x14090638b
009063CB  EB BB                           jmp 0x140906388
009063CD  EB 27                           jmp 0x1409063f6
009063CF  33 F6                           xor esi, esi
009063D1  44 8D 7E 01                     lea r15d, [rsi + 1]
009063D5  49 83 CD FF                     or r13, 0xffffffffffffffff
009063D9  44 8A A4 24 08 01 00 00         mov r12b, byte ptr [rsp + 0x108]
009063E1  4C 8B B4 24 80 00 00 00         mov r14, qword ptr [rsp + 0x80]
009063E9  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
009063EE  48 8B BC 24 88 00 00 00         mov rdi, qword ptr [rsp + 0x88]
009063F6  F6 87 A0 05 00 00 02            test byte ptr [rdi + 0x5a0], 2
009063FD  0F 95 C1                        setne cl
00906400  F7 47 74 00 00 10 00            test dword ptr [rdi + 0x74], 0x100000
00906407  0F 95 C0                        setne al
0090640A  84 C8                           test al, cl
0090640C  0F 85 A2 01 00 00               jne 0x1409065b4
00906412  48 8B D3                        mov rdx, rbx
00906415  49 8B CE                        mov rcx, r14
00906418  E8 A3 96 F7 FF                  call 0x14087fac0
0090641D  E8 16 E0 B7 FF                  call 0x140484438
00906422  48 85 C0                        test rax, rax
00906425  0F 84 FE 00 00 00               je 0x140906529
0090642B  48 8D 8F C8 04 00 00            lea rcx, [rdi + 0x4c8]
00906432  E8 09 76 A7 FF                  call 0x14037da40
00906437  45 84 E4                        test r12b, r12b
0090643A  0F 85 D0 00 00 00               jne 0x140906510
00906440  48 8B CF                        mov rcx, rdi
00906443  E8 FC F7 FF FF                  call 0x140905c44
00906448  48 39 B7 D0 02 00 00            cmp qword ptr [rdi + 0x2d0], rsi
0090644F  0F 85 3C 03 00 00               jne 0x140906791
00906455  8B 87 F0 06 00 00               mov eax, dword ptr [rdi + 0x6f0]
0090645B  41 84 C7                        test r15b, al
0090645E  0F 84 20 02 00 00               je 0x140906684
00906464  48 8B 9F F0 06 00 00            mov rbx, qword ptr [rdi + 0x6f0]
0090646B  83 C8 02                        or eax, 2
0090646E  89 87 F0 06 00 00               mov dword ptr [rdi + 0x6f0], eax
00906474  48 83 E3 FC                     and rbx, 0xfffffffffffffffc
00906478  0F 85 C1 00 00 00               jne 0x14090653f
0090647E  41 0F B6 D4                     movzx edx, r12b
00906482  48 8B CF                        mov rcx, rdi
00906485  E8 4A 03 00 00                  call 0x1409067d4
0090648A  48 8B 8F A8 06 00 00            mov rcx, qword ptr [rdi + 0x6a8]
00906491  48 85 C9                        test rcx, rcx
00906494  0F 85 1B 03 00 00               jne 0x1409067b5
0090649A  48 8D 87 B8 06 00 00            lea rax, [rdi + 0x6b8]
009064A1  4C 8B 08                        mov r9, qword ptr [rax]
009064A4  4C 3B C8                        cmp r9, rax
009064A7  75 1C                           jne 0x1409064c5
009064A9  48 8B CF                        mov rcx, rdi
009064AC  E8 87 EC A4 FF                  call 0x140355138
009064B1  48 81 C4 C0 00 00 00            add rsp, 0xc0
009064B8  41 5F                           pop r15
009064BA  41 5E                           pop r14
009064BC  41 5D                           pop r13
009064BE  41 5C                           pop r12
009064C0  5F                              pop rdi
009064C1  5E                              pop rsi
009064C2  5B                              pop rbx
009064C3  C3                              ret
009064C4  CC                              int3
009064C5  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
009064CA  4C 8B C7                        mov r8, rdi
009064CD  BA 14 00 00 00                  mov edx, 0x14
009064D2  B9 C6 01 00 00                  mov ecx, 0x1c6
009064D7  E8 84 71 BF FF                  call 0x1404fd660
009064DC  CC                              int3
009064DD  44 89 6C 24 20                  mov dword ptr [rsp + 0x20], r13d
009064E2  4C 8B CF                        mov r9, rdi
009064E5  4D 8B C6                        mov r8, r14
009064E8  33 D2                           xor edx, edx
009064EA  41 8B CF                        mov ecx, r15d
009064ED  E8 92 DC FF FF                  call 0x140904184
009064F2  E9 8E FC FF FF                  jmp 0x140906185
009064F7  89 74 24 20                     mov dword ptr [rsp + 0x20], esi
009064FB  4C 8B CF                        mov r9, rdi
009064FE  4D 8B C6                        mov r8, r14
00906501  33 D2                           xor edx, edx
00906503  8D 4A 02                        lea ecx, [rdx + 2]
00906506  E8 79 DC FF FF                  call 0x140904184
0090650B  E9 4F FD FF FF                  jmp 0x14090625f
00906510  89 74 24 20                     mov dword ptr [rsp + 0x20], esi
00906514  4C 8B CF                        mov r9, rdi
00906517  4D 8B C6                        mov r8, r14
0090651A  33 D2                           xor edx, edx
0090651C  8D 4A 03                        lea ecx, [rdx + 3]
0090651F  E8 60 DC FF FF                  call 0x140904184
00906524  E9 17 FF FF FF                  jmp 0x140906440
00906529  48 A1 14 00 00 00 80 F7 FF FF   movabs rax, qword ptr [0xfffff78000000014]
00906533  48 89 87 C8 04 00 00            mov qword ptr [rdi + 0x4c8], rax
0090653A  E9 F8 FE FF FF                  jmp 0x140906437
0090653F  48 8B D3                        mov rdx, rbx
00906542  E8 C1 0B B9 FF                  call 0x140497108
00906547  84 C0                           test al, al
00906549  0F 84 5F 02 00 00               je 0x1409067ae
0090654F  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00906558  66 44 01 A8 E6 01 00 00         add word ptr [rax + 0x1e6], r13w
00906560  90                              nop
00906561  41 B8 02 00 00 00               mov r8d, 2
00906567  48 8B D3                        mov rdx, rbx
0090656A  E8 29 74 11 00                  call 0x140a1d998
0090656F  E8 CC C6 9D FF                  call 0x1402e2c40
00906574  E9 05 FF FF FF                  jmp 0x14090647e
00906579  49 39 B6 40 06 00 00            cmp qword ptr [r14 + 0x640], rsi
00906580  0F 85 7F FB FF FF               jne 0x140906105
00906586  41 8B 86 DC 07 00 00            mov eax, dword ptr [r14 + 0x7dc]
0090658D  A8 02                           test al, 2
0090658F  0F 84 85 FB FF FF               je 0x14090611a
00906595  41 8B 86 80 03 00 00            mov eax, dword ptr [r14 + 0x380]
0090659C  85 C0                           test eax, eax
0090659E  0F 85 76 FB FF FF               jne 0x14090611a
009065A4  45 8A E7                        mov r12b, r15b
009065A7  44 88 BC 24 08 01 00 00         mov byte ptr [rsp + 0x108], r15b
009065AF  E9 66 FB FF FF                  jmp 0x14090611a
009065B4  E8 C3 97 F7 FF                  call 0x14087fd7c
009065B9  E9 54 FE FF FF                  jmp 0x140906412
009065BE  4C 8D 05 03 B3 70 FF            lea r8, [rip - 0x8f4cfd]
009065C5  33 D2                           xor edx, edx
009065C7  33 C9                           xor ecx, ecx
009065C9  E8 82 2F 90 FF                  call 0x140209550
009065CE  E9 F8 FB FF FF                  jmp 0x1409061cb
009065D3  49 39 B6 40 06 00 00            cmp qword ptr [r14 + 0x640], rsi
009065DA  0F 84 C7 FA FF FF               je 0x1409060a7
009065E0  E9 B5 FA FF FF                  jmp 0x14090609a
009065E5  F0 41 81 8E F4 01 00 00 08 00 00 02  lock or dword ptr [r14 + 0x1f4], 0x2000008
009065F1  44 89 6C 24 20                  mov dword ptr [rsp + 0x20], r13d
009065F6  4C 8B CF                        mov r9, rdi
009065F9  4D 8B C6                        mov r8, r14
009065FC  41 8A D7                        mov dl, r15b
009065FF  33 C9                           xor ecx, ecx
00906601  E8 7E DB FF FF                  call 0x140904184
00906606  E9 33 FB FF FF                  jmp 0x14090613e
0090660B  C7 44 24 40 08 00 30 00         mov dword ptr [rsp + 0x40], 0x300008
00906613  C7 44 24 44 06 00 00 00         mov dword ptr [rsp + 0x44], 6
0090661B  48 8B 87 C0 04 00 00            mov rax, qword ptr [rdi + 0x4c0]
00906622  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00906627  48 8D 54 24 40                  lea rdx, [rsp + 0x40]
0090662C  49 8B 4D 08                     mov rcx, qword ptr [r13 + 8]
00906630  E8 0B 43 F8 FF                  call 0x14088a940
00906635  3D 17 00 00 C0                  cmp eax, 0xc0000017
0090663A  0F 84 24 01 00 00               je 0x140906764
00906640  3D 9A 00 00 C0                  cmp eax, 0xc000009a
00906645  0F 84 19 01 00 00               je 0x140906764
0090664B  49 8B 4D 08                     mov rcx, qword ptr [r13 + 8]
0090664F  E8 FC 2C 9F FF                  call 0x1402f9350
00906654  49 8B 5D 00                     mov rbx, qword ptr [r13]
00906658  BA 50 73 54 70                  mov edx, 0x70547350
0090665D  49 8B CD                        mov rcx, r13
00906660  E8 0B C2 27 00                  call 0x140b82870
00906665  4C 8B EB                        mov r13, rbx
00906668  48 85 DB                        test rbx, rbx
0090666B  0F 84 24 FB FF FF               je 0x140906195
00906671  EB B4                           jmp 0x140906627
00906673  E8 88 28 14 00                  call 0x140a48f00
00906678  48 89 B7 70 05 00 00            mov qword ptr [rdi + 0x570], rsi
0090667F  E9 D0 F9 FF FF                  jmp 0x140906054
00906684  CD 2C                           int 0x2c
00906686  E9 D9 FD FF FF                  jmp 0x140906464
0090668B  44 0F B6 8F 4A 02 00 00         movzx r9d, byte ptr [rdi + 0x24a]
00906693  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00906698  49 8B D6                        mov rdx, r14
0090669B  B9 05 00 00 00                  mov ecx, 5
009066A0  E8 BB 6F BF FF                  call 0x1404fd660
009066A5  CC                              int3
009066A6  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
009066AB  45 33 C9                        xor r9d, r9d
009066AE  45 33 C0                        xor r8d, r8d
009066B1  48 8B D7                        mov rdx, rdi
009066B4  B9 E9 00 00 00                  mov ecx, 0xe9
009066B9  E8 A2 6F BF FF                  call 0x1404fd660
009066BE  CC                              int3
009066BF  4C 8B C0                        mov r8, rax
009066C2  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
009066C7  45 33 C9                        xor r9d, r9d
009066CA  33 D2                           xor edx, edx
009066CC  8D 4A 20                        lea ecx, [rdx + 0x20]
009066CF  E8 8C 6F BF FF                  call 0x1404fd660
009066D4  CC                              int3
009066D5  33 D2                           xor edx, edx
009066D7  48 8B CF                        mov rcx, rdi
009066DA  E8 41 C8 A8 FF                  call 0x140392f20
009066DF  BA 50 73 51 79                  mov edx, 0x79517350
009066E4  48 8B 8F 68 05 00 00            mov rcx, qword ptr [rdi + 0x568]
009066EB  E8 F0 11 9F FF                  call 0x1402f78e0
009066F0  48 89 B7 68 05 00 00            mov qword ptr [rdi + 0x568], rsi
009066F7  E9 28 F9 FF FF                  jmp 0x140906024
009066FC  F7 47 74 00 04 00 00            test dword ptr [rdi + 0x74], 0x400
00906703  0F 85 59 FA FF FF               jne 0x140906162
00906709  45 84 E4                        test r12b, r12b
0090670C  0F 84 E7 A6 21 00               je 0x140b20df9
00906712  41 8B 8E 54 05 00 00            mov ecx, dword ptr [r14 + 0x554]
00906719  E8 7A A2 E0 FF                  call 0x140710998
0090671E  E9 3F FA FF FF                  jmp 0x140906162
00906723  48 89 B4 24 10 01 00 00         mov qword ptr [rsp + 0x110], rsi
0090672B  48 8D 8C 24 10 01 00 00         lea rcx, [rsp + 0x110]
00906733  E8 B8 29 CB FF                  call 0x1405b90f0
00906738  85 C0                           test eax, eax
0090673A  0F 88 2F FA FF FF               js 0x14090616f
00906740  48 8B 8C 24 10 01 00 00         mov rcx, qword ptr [rsp + 0x110]
00906748  E8 93 87 99 FF                  call 0x14029eee0
0090674D  BA 50 73 53 65                  mov edx, 0x65537350
00906752  48 8B 8C 24 10 01 00 00         mov rcx, qword ptr [rsp + 0x110]
0090675A  E8 11 C1 27 00                  call 0x140b82870
0090675F  E9 0B FA FF FF                  jmp 0x14090616f
00906764  4C 8D 05 5D B1 70 FF            lea r8, [rip - 0x8f4ea3]
0090676B  33 D2                           xor edx, edx
0090676D  33 C9                           xor ecx, ecx
0090676F  E8 DC 2D 90 FF                  call 0x140209550
00906774  E9 AE FE FF FF                  jmp 0x140906627
00906779  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
0090677E  45 33 C9                        xor r9d, r9d
00906781  4C 8B C7                        mov r8, rdi
00906784  33 D2                           xor edx, edx
00906786  B9 94 00 00 00                  mov ecx, 0x94
0090678B  E8 D0 6E BF FF                  call 0x1404fd660
00906790  CC                              int3
00906791  48 8B 05 E8 37 6D 00            mov rax, qword ptr [rip + 0x6d37e8]
00906798  48 85 C0                        test rax, rax
0090679B  0F 84 B4 FC FF FF               je 0x140906455
009067A1  48 8B CF                        mov rcx, rdi
009067A4  E8 27 43 DB FF                  call 0x1406baad0
009067A9  E9 A7 FC FF FF                  jmp 0x140906455
009067AE  B9 46 00 00 00                  mov ecx, 0x46
009067B3  CD 29                           int 0x29
009067B5  BA 50 73 53 63                  mov edx, 0x63537350
009067BA  E8 B1 C0 27 00                  call 0x140b82870
009067BF  48 89 B7 A8 06 00 00            mov qword ptr [rdi + 0x6a8], rsi
009067C6  E9 CF FC FF FF                  jmp 0x14090649a
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PspExitThread(int a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m44;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA8;
    unsigned int v_stack_mB4;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int8 v_stack_p10;
    unsigned __int8 v_stack_p108;
    unsigned __int64 v_stack_p110;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p40;
    unsigned int v_stack_p44;
    unsigned __int64 v_stack_p68;

    v_rsp = (v_rsp) - (192);
    v_stack_mB8 = v_xmm0;
    v_stack_mA8 = v_xmm0;
    v_stack_m98 = v_xmm0;
    result = 0;
    *(unsigned __int64 *)(v_rsp - 104) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 88) = 0;
    *(unsigned int *)(v_rsp - 80) = 0;
    v_stack_m70 = *(unsigned __int64 *)(gs_base + (0 + 392));
    v_stack_m78 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544);
    result = PspClearProcessThreadCidRefs(*(unsigned __int64 *)(gs_base + (0 + 392)), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1296), *(unsigned __int64 *)(gs_base + (0 + 392)), a4);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184))) goto loc_0090668B;
    v_rsi = 0;
    if ((*(unsigned int *)(v_rip + 7081277)) != 0) {
        a1 = v_cr8;
        a2 = 0;
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), a4);
    }
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1444))))) != 0) goto loc_009066A6;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 484))) != 0) goto loc_009066BF;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1384)) != 0) goto loc_009066D5;
loc_00906024:
    result = PspEmptyPropertySet(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1624, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), a4);
    result = PspRevertContainerImpersonation(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), a4);
    result = ExWaitForRundownProtectionRelease(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1416, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), a4);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1392) != 0) goto loc_00906673;
loc_00906054:
    v_stack_p10 = 0;
    *(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1496) = (unsigned int)((unsigned int)(a1));
    result = (unsigned int)(*(unsigned int *)(v_rip + 7080595));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 7080595)))) & (2)) != 0) {
        a3 = 0;
        a2 = 0;
        a1 = *(unsigned __int64 *)(gs_base + (0 + 392));
        result = EtwTraceThread(a1, a2, a3, a4);
    }
    result = (result) | (-1);
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544) + 1532))))) != 0) goto loc_009065D3;
loc_0090609A:
    a3 = 0;
    a2 = 0;
    result = PspCallThreadNotifyRoutines(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, a4);
loc_009060A7:
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544) + 456, a2, a3, a4);
    v_stack_mC8 = result;
    if (!(condition_is_above_or_equal)) {
        a3 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544) + 456;
        a2 = result;
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544) + 456;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
        result = v_stack_mC8;
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544) + 896))) - (1));
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544) + 896) = (unsigned int)(result);
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544) + 1532))))) != 0) goto loc_00906579;
loc_00906105:
    v_r12 = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544) + 896))) == 0) { v_r12 = 1; }
    v_stack_p10 = (unsigned __int8)(v_r12);
loc_0090611A:
    if ((unsigned __int8)(v_r12) != 0) goto loc_009065E5;
    if (((unsigned int)((unsigned int)(a1))) != 0xC000004BULL) {
        *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544) + 908) = (unsigned int)((unsigned int)(a1));
    }
    result = PspUnlockProcessExclusive(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544), *(unsigned __int64 *)(gs_base + (0 + 392)), a3, a4);
loc_0090613E:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544) + 776)) != 0) goto loc_009066FC;
loc_00906162:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544) + 368)) & (1)) != 0) goto loc_00906723;
loc_0090616F:
    if ((unsigned __int8)(v_r12) != 0) goto loc_009064DD;
loc_00906185:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1256) != 0) goto loc_0090660B;
loc_00906195:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1440)))) & (2)) == 0) goto loc_009061F6;
    result = PsCaptureExceptionPort(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544), *(unsigned __int64 *)(gs_base + (0 + 392)), a3, a4);
    if (result == 0) goto loc_009061F6;
    v_stack_mB8 = 0x300008ULL;
    v_stack_mB4 = 6;
    v_stack_m90 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1216);
loc_009061CB:
    result = LpcRequestPort(result, v_stack_mB8, a3, a4);
    if (((unsigned int)(result)) == 0xC000009AULL) goto loc_009065BE;
    if (((unsigned int)(result)) == 0xC0000017ULL) goto loc_009065BE;
    result = ObfDereferenceObject(result, v_stack_mB8, a3, a4);
loc_009061F6:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 456) == 0) goto loc_00906256;
    v_stack_m58 = *(unsigned __int64 *)(gs_base + (0 + 392));
    v_stack_m50 = 1;
    result = 0;
    v_stack_m44 = 0;
    v_stack_m48 = 0;
    a4 = 0;
    a3 = 0;
    result = PspUpdateCalloutParameters(1, v_stack_m68, a3, a4);
    if ((unsigned int)(result) != 0) {
        result = PsSessionGetWin32Callouts(1, v_stack_m68, a3, a4);
        a1 = result;
        a3 = v_stack_m68;
        a2 = 1;
        result = ExCallCallBack(a1, a2, a3, a4);
    }
    if ((unsigned __int8)(v_r12) != 0) goto loc_009064F7;
loc_0090625F:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 120)))) & (64)) == 0) goto loc_00906779;
    v_r13 = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1256)) | (-1);
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 120));
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1776) != 0) {
        result = *(unsigned __int64 *)(gs_base + (0 + 392));
        a3 = 1;
        result = RtlpFlsDataCleanup(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1776), a3, a4);
        result = KeLeaveGuardedRegion(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1776), a3, a4);
    }
    result = IoCancelThreadIo(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1776), a3, a4);
    result = ExTimerRundown(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1776), a3, a4);
    result = CmNotifyRunDown(*(unsigned __int64 *)(gs_base + (0 + 392)), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1776), a3, a4);
    result = KiRundownMutants(*(unsigned __int64 *)(gs_base + (0 + 392)), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1776), a3, a4);
    result = PspSchedulerSharedDataRegionSlotFree(*(unsigned __int64 *)(gs_base + (0 + 392)), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1776), a3, a4);
    v_stack_mC8 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 240);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 240) == 0) goto loc_0090641D;
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 240) = 0;
    result = PspLockUnlockTebAccessExclusive(*(unsigned __int64 *)(gs_base + (0 + 392)), *(unsigned __int64 *)(gs_base + (0 + 392)), a3, a4);
    if (((*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 116)) & (0x400ULL)) != 0) goto loc_0090641D;
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544) + 500)))) & (0x40000008ULL)) != 0) goto loc_0090641D;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1440)))) & (2)) == 0) goto loc_00906360;
    v_stack_p18 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 240) + 5240);
    v_stack_m88 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 240) + 5240);
    v_stack_p20 = 0;
    v_stack_p20 = 0;
    result = ZwFreeVirtualMemory(v_r13, v_stack_m88, v_stack_p20, (unsigned int)(0x8000ULL));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544) + 784)) != 0) goto loc_00906376;
loc_00906360:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 240) + 5800) == 0) goto loc_009063CD;
    result = ObCloseHandle(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 240) + 5800), 1, v_stack_p20, (unsigned int)(0x8000ULL));
    goto loc_009063CD;
loc_00906376:
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544) + 1772))) != 332) goto loc_009063BE;
loc_00906388:
loc_0090638B:
    if (1 == 0) goto loc_00906360;
    v_stack_m80 = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 240) + 11788));
    v_stack_mC0 = 0;
    v_stack_mC0 = 0;
    result = ZwFreeVirtualMemory(v_r13, v_stack_m80, v_stack_mC0, (unsigned int)(0x8000ULL));
    goto loc_00906360;
loc_009063BE:
    if (((unsigned __int16)(result)) != 452) goto loc_0090638B;
    goto loc_00906388;
loc_009063CD:
    goto loc_009063F6;
loc_009063F6:
    a1 = (((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1440)) & (2)) != 0) ? 1 : 0;
    result = (((*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 116)) & (0x100000ULL)) != 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) != 0) goto loc_009065B4;
loc_00906412:
    result = MmDeleteTeb(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 240), v_stack_mC0, (unsigned int)(0x8000ULL));
loc_0090641D:
    result = KeQuerySystemTimeUnsafe(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 240), v_stack_mC0, (unsigned int)(0x8000ULL));
    if (result == 0) goto loc_00906529;
    result = KeQuerySystemTimePrecise(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1224, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 240), v_stack_mC0, (unsigned int)(0x8000ULL));
loc_00906437:
    if ((unsigned __int8)(v_r12) != 0) goto loc_00906510;
loc_00906440:
    result = KeRundownApcQueues(*(unsigned __int64 *)(gs_base + (0 + 392)), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 240), v_stack_mC0, (unsigned int)(0x8000ULL));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 720)) != 0) goto loc_00906791;
loc_00906455:
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1776))))) == 0) goto loc_00906684;
loc_00906464:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1776))) | (2));
    *(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1776) = (unsigned int)(result);
    v_rbx = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1776)) & (-4);
    if (condition_is_not_equal) goto loc_0090653F;
loc_0090647E:
    result = PspThreadIndexCleanup(*(unsigned __int64 *)(gs_base + (0 + 392)), (unsigned __int8)(v_r12), v_stack_mC0, (unsigned int)(0x8000ULL));
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1704) != 0) goto loc_009067B5;
loc_0090649A:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1720)) != (*(unsigned __int64 *)(gs_base + (0 + 392)) + 1720)) goto loc_009064C5;
    result = KeTerminateThread(*(unsigned __int64 *)(gs_base + (0 + 392)), (unsigned __int8)(v_r12), v_stack_mC0, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1720));
    v_rsp = (v_rsp) + (192);
    return result;
loc_009064C5:
    v_stack_p20 = 0;
    result = KeBugCheckEx(454, 20, *(unsigned __int64 *)(gs_base + (0 + 392)), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1720));
loc_009064DD:
    v_stack_p20 = (unsigned int)(v_r13);
    a2 = 0;
    result = PspExitLastThread(1, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544), *(unsigned __int64 *)(gs_base + (0 + 392)));
    goto loc_00906185;
loc_009064F7:
    v_stack_p20 = 0;
    a2 = 0;
    result = PspExitLastThread(a2 + 2, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544), *(unsigned __int64 *)(gs_base + (0 + 392)));
    goto loc_0090625F;
loc_00906510:
    v_stack_p20 = 0;
    a2 = 0;
    result = PspExitLastThread(a2 + 3, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544), *(unsigned __int64 *)(gs_base + (0 + 392)));
    goto loc_00906440;
loc_00906529:
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1224) = result;
    goto loc_00906437;
loc_0090653F:
    result = RtlpFlsSlotDataValidateEmpty(a2 + 3, v_rbx, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544), *(unsigned __int64 *)(gs_base + (0 + 392)));
    if ((unsigned __int8)(result) == 0) goto loc_009067AE;
    result = RtlpFlsDataCleanup(a2 + 3, v_rbx, 2, *(unsigned __int64 *)(gs_base + (0 + 392)));
    result = KeLeaveGuardedRegion(a2 + 3, v_rbx, 2, *(unsigned __int64 *)(gs_base + (0 + 392)));
    goto loc_0090647E;
loc_00906579:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544) + 1600)) != 0) goto loc_00906105;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544) + 2012)))) & (2)) == 0) goto loc_0090611A;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544) + 896))) != 0) goto loc_0090611A;
    v_stack_p108 = 1;
    goto loc_0090611A;
loc_009065B4:
    result = PspFreeCurrentThreadUserShadowStack(a2 + 3, v_rbx, 2, *(unsigned __int64 *)(gs_base + (0 + 392)));
    goto loc_00906412;
loc_009065BE:
    a2 = 0;
    a1 = 0;
    result = KeDelayExecutionThread(a1, a2, v_rip - 9391357, *(unsigned __int64 *)(gs_base + (0 + 392)));
    goto loc_009061CB;
loc_009065D3:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544) + 1600)) == 0) goto loc_009060A7;
    goto loc_0090609A;
loc_009065E5:
    v_stack_p20 = (unsigned int)(v_r13);
    a1 = 0;
    result = PspExitLastThread(a1, 1, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544), *(unsigned __int64 *)(gs_base + (0 + 392)));
    goto loc_0090613E;
loc_0090660B:
    v_stack_p40 = 0x300008ULL;
    v_stack_p44 = 6;
    v_stack_p68 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1216);
loc_00906627:
    result = LpcRequestPort(*(unsigned __int64 *)(v_r13 + 8), v_stack_p40, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544), *(unsigned __int64 *)(gs_base + (0 + 392)));
    if (((unsigned int)(result)) == 0xC0000017ULL) goto loc_00906764;
    if (((unsigned int)(result)) == 0xC000009AULL) goto loc_00906764;
    result = ObfDereferenceObject(*(unsigned __int64 *)(v_r13 + 8), v_stack_p40, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544), *(unsigned __int64 *)(gs_base + (0 + 392)));
    result = ExFreePoolWithTag(v_r13, (unsigned int)(0x70547350ULL), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544), *(unsigned __int64 *)(gs_base + (0 + 392)));
    if (*(unsigned __int64 *)(v_r13) == 0) goto loc_00906195;
    goto loc_00906627;
loc_00906673:
    result = PoDeletePowerRequest(v_r13, (unsigned int)(0x70547350ULL), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544), *(unsigned __int64 *)(gs_base + (0 + 392)));
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1392) = 0;
    goto loc_00906054;
loc_00906684:
    goto loc_00906464;
loc_0090668B:
    v_stack_p20 = *(unsigned __int64 *)(gs_base + (0 + 392));
    result = KeBugCheckEx(5, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544), *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 586));
loc_009066A6:
    v_stack_p20 = 0;
    a4 = 0;
    a3 = 0;
    result = KeBugCheckEx(233, *(unsigned __int64 *)(gs_base + (0 + 392)), a3, a4);
loc_009066BF:
    v_stack_p20 = 1;
    a4 = 0;
    a2 = 0;
    result = KeBugCheckEx(a2 + 32, a2, result, a4);
loc_009066D5:
    a2 = 0;
    result = KeSetThreadChargeOnlySchedulingGroup(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, result, a4);
    result = ObfDereferenceObjectWithTag(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1384), (unsigned int)(0x79517350ULL), result, a4);
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1384) = 0;
    goto loc_00906024;
loc_009066FC:
    if (((*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 116)) & (0x400ULL)) != 0) goto loc_00906162;
    result = DbgkExitProcess((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544) + 1364)), (unsigned int)(0x79517350ULL), result, a4);
    goto loc_00906162;
loc_00906723:
    v_stack_p110 = 0;
    result = KeUnsecureThread(v_stack_p110, (unsigned int)(0x79517350ULL), result, a4);
    if (sign_flag) goto loc_0090616F;
    result = MmUnlockPages(v_stack_p110, (unsigned int)(0x79517350ULL), result, a4);
    result = ExFreePoolWithTag(v_stack_p110, (unsigned int)(0x65537350ULL), result, a4);
    goto loc_0090616F;
loc_00906764:
    a2 = 0;
    a1 = 0;
    result = KeDelayExecutionThread(a1, a2, v_rip - 9391779, a4);
    goto loc_00906627;
loc_00906779:
    v_stack_p20 = 0;
    a4 = 0;
    a2 = 0;
    result = KeBugCheckEx(148, a2, *(unsigned __int64 *)(gs_base + (0 + 392)), a4);
loc_00906791:
    if (*(unsigned __int64 *)(v_rip + 7157736) == 0) goto loc_00906455;
    result = guard_dispatch_icall(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, *(unsigned __int64 *)(gs_base + (0 + 392)), a4);
    goto loc_00906455;
loc_009067AE:
loc_009067B5:
    result = ExFreePoolWithTag(70, (unsigned int)(0x63537350ULL), *(unsigned __int64 *)(gs_base + (0 + 392)), a4);
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1704) = 0;
    goto loc_0090649A;
}
```

## 5. (Beta) C Style

```c
int64_t PspExitThread(int32_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m44;
    uint64_t v_stack_m48;
    uint32_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA8;
    uint32_t v_stack_mB4;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint8_t v_stack_p10;
    uint8_t v_stack_p108;
    uint64_t v_stack_p110;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint32_t v_stack_p40;
    uint32_t v_stack_p44;
    uint64_t v_stack_p68;

    local_rsp = (local_rsp) - (192);
    v_stack_mB8 = v_xmm0;
    v_stack_mA8 = v_xmm0;
    v_stack_m98 = v_xmm0;
    result = 0;
    *(uint64_t *)(local_rsp - 0x68) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x58) = 0;
    *(uint32_t *)(local_rsp - 0x50) = 0;
    v_stack_m70 = *(uint64_t *)(gs_base + (0 + 0x188));
    v_stack_m78 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220);
    result = PspClearProcessThreadCidRefs(*(uint64_t *)(gs_base + (0 + 0x188)), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x510), *(uint64_t *)(gs_base + (0 + 0x188)), Arg4);
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220)) != (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8))) goto loc_0090668B;
    local_rsi = 0;
    if ((*(uint32_t *)(v_rip + 0x6C0D3D)) != 0) {
        Arg1 = v_cr8;
        Arg2 = 0;
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), Arg4);
    }
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5A4))))) != 0) goto loc_009066A6;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x1E4))) != 0) goto loc_009066BF;
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x568)) != 0) goto loc_009066D5;
loc_00906024:
    result = PspEmptyPropertySet(*(uint64_t *)(gs_base + (0 + 0x188)) + 1624, Arg2, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), Arg4);
    result = PspRevertContainerImpersonation(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), Arg4);
    result = ExWaitForRundownProtectionRelease(*(uint64_t *)(gs_base + (0 + 0x188)) + 1416, Arg2, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), Arg4);
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x570) != 0) goto loc_00906673;
loc_00906054:
    v_stack_p10 = 0;
    *(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5D8) = (uint32_t)((uint32_t)(Arg1));
    result = (uint32_t)(*(uint32_t *)(v_rip + 0x6C0A93));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x6C0A93)))) & (2)) != 0) {
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x188));
        result = EtwTraceThread(Arg1, Arg2, Arg3, Arg4);
    }
    result = (result) | (-1);
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220) + 0x5FC))))) != 0) goto loc_009065D3;
loc_0090609A:
    Arg3 = 0;
    Arg2 = 0;
    result = PspCallThreadNotifyRoutines(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, Arg3, Arg4);
loc_009060A7:
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220) + 456, Arg2, Arg3, Arg4);
    v_stack_mC8 = result;
    if (!(condition_is_above_or_equal)) {
        Arg3 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220) + 456;
        Arg2 = result;
        Arg1 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220) + 456;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, Arg4);
        result = v_stack_mC8;
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220) + 0x380))) - (1));
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220) + 0x380) = (uint32_t)(result);
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220) + 0x5FC))))) != 0) goto loc_00906579;
loc_00906105:
    local_r12 = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220) + 0x380))) == 0) { local_r12 = 1; }
    v_stack_p10 = (uint8_t)(local_r12);
loc_0090611A:
    if ((uint8_t)(local_r12) != 0) goto loc_009065E5;
    if (((uint32_t)((uint32_t)(Arg1))) != 0xC000004BULL) {
        *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220) + 0x38C) = (uint32_t)((uint32_t)(Arg1));
    }
    result = PspUnlockProcessExclusive(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220), *(uint64_t *)(gs_base + (0 + 0x188)), Arg3, Arg4);
loc_0090613E:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220) + 0x308)) != 0) goto loc_009066FC;
loc_00906162:
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220) + 0x170)) & (1)) != 0) goto loc_00906723;
loc_0090616F:
    if ((uint8_t)(local_r12) != 0) goto loc_009064DD;
loc_00906185:
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x4E8) != 0) goto loc_0090660B;
loc_00906195:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5A0)))) & (2)) == 0) goto loc_009061F6;
    result = PsCaptureExceptionPort(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220), *(uint64_t *)(gs_base + (0 + 0x188)), Arg3, Arg4);
    if (result == 0) goto loc_009061F6;
    v_stack_mB8 = 0x300008ULL;
    v_stack_mB4 = 6;
    v_stack_m90 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x4C0);
loc_009061CB:
    result = LpcRequestPort(result, v_stack_mB8, Arg3, Arg4);
    if (((uint32_t)(result)) == 0xC000009AULL) goto loc_009065BE;
    if (((uint32_t)(result)) == 0xC0000017ULL) goto loc_009065BE;
    result = ObfDereferenceObject(result, v_stack_mB8, Arg3, Arg4);
loc_009061F6:
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x1C8) == 0) goto loc_00906256;
    v_stack_m58 = *(uint64_t *)(gs_base + (0 + 0x188));
    v_stack_m50 = 1;
    result = 0;
    v_stack_m44 = 0;
    v_stack_m48 = 0;
    Arg4 = 0;
    Arg3 = 0;
    result = PspUpdateCalloutParameters(1, v_stack_m68, Arg3, Arg4);
    if ((uint32_t)(result) != 0) {
        result = PsSessionGetWin32Callouts(1, v_stack_m68, Arg3, Arg4);
        Arg1 = result;
        Arg3 = v_stack_m68;
        Arg2 = 1;
        result = ExCallCallBack(Arg1, Arg2, Arg3, Arg4);
    }
    if ((uint8_t)(local_r12) != 0) goto loc_009064F7;
loc_0090625F:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x78)))) & (64)) == 0) goto loc_00906779;
    local_r13 = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x4E8)) | (-1);
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x78));
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x6F0) != 0) {
        result = *(uint64_t *)(gs_base + (0 + 0x188));
        Arg3 = 1;
        result = RtlpFlsDataCleanup(Arg1, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x6F0), Arg3, Arg4);
        result = KeLeaveGuardedRegion(Arg1, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x6F0), Arg3, Arg4);
    }
    result = IoCancelThreadIo(Arg1, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x6F0), Arg3, Arg4);
    result = ExTimerRundown(Arg1, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x6F0), Arg3, Arg4);
    result = CmNotifyRunDown(*(uint64_t *)(gs_base + (0 + 0x188)), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x6F0), Arg3, Arg4);
    result = KiRundownMutants(*(uint64_t *)(gs_base + (0 + 0x188)), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x6F0), Arg3, Arg4);
    result = PspSchedulerSharedDataRegionSlotFree(*(uint64_t *)(gs_base + (0 + 0x188)), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x6F0), Arg3, Arg4);
    v_stack_mC8 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xF0);
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xF0) == 0) goto loc_0090641D;
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xF0) = 0;
    result = PspLockUnlockTebAccessExclusive(*(uint64_t *)(gs_base + (0 + 0x188)), *(uint64_t *)(gs_base + (0 + 0x188)), Arg3, Arg4);
    if (((*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x74)) & (0x400ULL)) != 0) goto loc_0090641D;
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220) + 0x1F4)))) & (0x40000008ULL)) != 0) goto loc_0090641D;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5A0)))) & (2)) == 0) goto loc_00906360;
    v_stack_p18 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xF0) + 0x1478);
    v_stack_m88 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xF0) + 0x1478);
    v_stack_p20 = 0;
    v_stack_p20 = 0;
    result = ZwFreeVirtualMemory(local_r13, v_stack_m88, v_stack_p20, (uint32_t)(0x8000ULL));
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220) + 0x310)) != 0) goto loc_00906376;
loc_00906360:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xF0) + 0x16A8) == 0) goto loc_009063CD;
    result = ObCloseHandle(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xF0) + 0x16A8), 1, v_stack_p20, (uint32_t)(0x8000ULL));
    goto loc_009063CD;
loc_00906376:
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220) + 0x6EC))) != 332) goto loc_009063BE;
loc_00906388:
loc_0090638B:
    if (1 == 0) goto loc_00906360;
    v_stack_m80 = (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xF0) + 0x2E0C));
    v_stack_mC0 = 0;
    v_stack_mC0 = 0;
    result = ZwFreeVirtualMemory(local_r13, v_stack_m80, v_stack_mC0, (uint32_t)(0x8000ULL));
    goto loc_00906360;
loc_009063BE:
    if (((uint16_t)(result)) != 452) goto loc_0090638B;
    goto loc_00906388;
loc_009063CD:
    goto loc_009063F6;
loc_009063F6:
    Arg1 = (((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5A0)) & (2)) != 0) ? 1 : 0;
    result = (((*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x74)) & (0x100000ULL)) != 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) != 0) goto loc_009065B4;
loc_00906412:
    result = MmDeleteTeb(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xF0), v_stack_mC0, (uint32_t)(0x8000ULL));
loc_0090641D:
    result = KeQuerySystemTimeUnsafe(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xF0), v_stack_mC0, (uint32_t)(0x8000ULL));
    if (result == 0) goto loc_00906529;
    result = KeQuerySystemTimePrecise(*(uint64_t *)(gs_base + (0 + 0x188)) + 1224, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xF0), v_stack_mC0, (uint32_t)(0x8000ULL));
loc_00906437:
    if ((uint8_t)(local_r12) != 0) goto loc_00906510;
loc_00906440:
    result = KeRundownApcQueues(*(uint64_t *)(gs_base + (0 + 0x188)), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xF0), v_stack_mC0, (uint32_t)(0x8000ULL));
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x2D0)) != 0) goto loc_00906791;
loc_00906455:
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x6F0))))) == 0) goto loc_00906684;
loc_00906464:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x6F0))) | (2));
    *(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x6F0) = (uint32_t)(result);
    local_rbx = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x6F0)) & (-4);
    if (condition_is_not_equal) goto loc_0090653F;
loc_0090647E:
    result = PspThreadIndexCleanup(*(uint64_t *)(gs_base + (0 + 0x188)), (uint8_t)(local_r12), v_stack_mC0, (uint32_t)(0x8000ULL));
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x6A8) != 0) goto loc_009067B5;
loc_0090649A:
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x6B8)) != (*(uint64_t *)(gs_base + (0 + 0x188)) + 1720)) goto loc_009064C5;
    result = KeTerminateThread(*(uint64_t *)(gs_base + (0 + 0x188)), (uint8_t)(local_r12), v_stack_mC0, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x6B8));
    local_rsp = (local_rsp) + (192);
    return result;
loc_009064C5:
    v_stack_p20 = 0;
    result = KeBugCheckEx(454, 20, *(uint64_t *)(gs_base + (0 + 0x188)), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x6B8));
loc_009064DD:
    v_stack_p20 = (uint32_t)(local_r13);
    Arg2 = 0;
    result = PspExitLastThread(1, Arg2, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220), *(uint64_t *)(gs_base + (0 + 0x188)));
    goto loc_00906185;
loc_009064F7:
    v_stack_p20 = 0;
    Arg2 = 0;
    result = PspExitLastThread(Arg2 + 2, Arg2, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220), *(uint64_t *)(gs_base + (0 + 0x188)));
    goto loc_0090625F;
loc_00906510:
    v_stack_p20 = 0;
    Arg2 = 0;
    result = PspExitLastThread(Arg2 + 3, Arg2, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220), *(uint64_t *)(gs_base + (0 + 0x188)));
    goto loc_00906440;
loc_00906529:
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x4C8) = result;
    goto loc_00906437;
loc_0090653F:
    result = RtlpFlsSlotDataValidateEmpty(Arg2 + 3, local_rbx, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220), *(uint64_t *)(gs_base + (0 + 0x188)));
    if ((uint8_t)(result) == 0) goto loc_009067AE;
    result = RtlpFlsDataCleanup(Arg2 + 3, local_rbx, 2, *(uint64_t *)(gs_base + (0 + 0x188)));
    result = KeLeaveGuardedRegion(Arg2 + 3, local_rbx, 2, *(uint64_t *)(gs_base + (0 + 0x188)));
    goto loc_0090647E;
loc_00906579:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220) + 0x640)) != 0) goto loc_00906105;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220) + 0x7DC)))) & (2)) == 0) goto loc_0090611A;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220) + 0x380))) != 0) goto loc_0090611A;
    v_stack_p108 = 1;
    goto loc_0090611A;
loc_009065B4:
    result = PspFreeCurrentThreadUserShadowStack(Arg2 + 3, local_rbx, 2, *(uint64_t *)(gs_base + (0 + 0x188)));
    goto loc_00906412;
loc_009065BE:
    Arg2 = 0;
    Arg1 = 0;
    result = KeDelayExecutionThread(Arg1, Arg2, v_rip - 9391357, *(uint64_t *)(gs_base + (0 + 0x188)));
    goto loc_009061CB;
loc_009065D3:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220) + 0x640)) == 0) goto loc_009060A7;
    goto loc_0090609A;
loc_009065E5:
    v_stack_p20 = (uint32_t)(local_r13);
    Arg1 = 0;
    result = PspExitLastThread(Arg1, 1, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220), *(uint64_t *)(gs_base + (0 + 0x188)));
    goto loc_0090613E;
loc_0090660B:
    v_stack_p40 = 0x300008ULL;
    v_stack_p44 = 6;
    v_stack_p68 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x4C0);
loc_00906627:
    result = LpcRequestPort(*(uint64_t *)(local_r13 + 0x8), v_stack_p40, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220), *(uint64_t *)(gs_base + (0 + 0x188)));
    if (((uint32_t)(result)) == 0xC0000017ULL) goto loc_00906764;
    if (((uint32_t)(result)) == 0xC000009AULL) goto loc_00906764;
    result = ObfDereferenceObject(*(uint64_t *)(local_r13 + 0x8), v_stack_p40, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220), *(uint64_t *)(gs_base + (0 + 0x188)));
    result = ExFreePoolWithTag(local_r13, (uint32_t)(0x70547350ULL), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220), *(uint64_t *)(gs_base + (0 + 0x188)));
    if (*(uint64_t *)(local_r13) == 0) goto loc_00906195;
    goto loc_00906627;
loc_00906673:
    result = PoDeletePowerRequest(local_r13, (uint32_t)(0x70547350ULL), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220), *(uint64_t *)(gs_base + (0 + 0x188)));
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x570) = 0;
    goto loc_00906054;
loc_00906684:
    goto loc_00906464;
loc_0090668B:
    v_stack_p20 = *(uint64_t *)(gs_base + (0 + 0x188));
    result = KeBugCheckEx(5, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220), *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x24A));
loc_009066A6:
    v_stack_p20 = 0;
    Arg4 = 0;
    Arg3 = 0;
    result = KeBugCheckEx(233, *(uint64_t *)(gs_base + (0 + 0x188)), Arg3, Arg4);
loc_009066BF:
    v_stack_p20 = 1;
    Arg4 = 0;
    Arg2 = 0;
    result = KeBugCheckEx(Arg2 + 32, Arg2, result, Arg4);
loc_009066D5:
    Arg2 = 0;
    result = KeSetThreadChargeOnlySchedulingGroup(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, result, Arg4);
    result = ObfDereferenceObjectWithTag(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x568), (uint32_t)(0x79517350ULL), result, Arg4);
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x568) = 0;
    goto loc_00906024;
loc_009066FC:
    if (((*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x74)) & (0x400ULL)) != 0) goto loc_00906162;
    result = DbgkExitProcess((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220) + 0x554)), (uint32_t)(0x79517350ULL), result, Arg4);
    goto loc_00906162;
loc_00906723:
    v_stack_p110 = 0;
    result = KeUnsecureThread(v_stack_p110, (uint32_t)(0x79517350ULL), result, Arg4);
    if (sign_flag) goto loc_0090616F;
    result = MmUnlockPages(v_stack_p110, (uint32_t)(0x79517350ULL), result, Arg4);
    result = ExFreePoolWithTag(v_stack_p110, (uint32_t)(0x65537350ULL), result, Arg4);
    goto loc_0090616F;
loc_00906764:
    Arg2 = 0;
    Arg1 = 0;
    result = KeDelayExecutionThread(Arg1, Arg2, v_rip - 9391779, Arg4);
    goto loc_00906627;
loc_00906779:
    v_stack_p20 = 0;
    Arg4 = 0;
    Arg2 = 0;
    result = KeBugCheckEx(148, Arg2, *(uint64_t *)(gs_base + (0 + 0x188)), Arg4);
loc_00906791:
    if (*(uint64_t *)(v_rip + 0x6D37E8) == 0) goto loc_00906455;
    result = guard_dispatch_icall(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, *(uint64_t *)(gs_base + (0 + 0x188)), Arg4);
    goto loc_00906455;
loc_009067AE:
loc_009067B5:
    result = ExFreePoolWithTag(70, (uint32_t)(0x63537350ULL), *(uint64_t *)(gs_base + (0 + 0x188)), Arg4);
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x6A8) = 0;
    goto loc_0090649A;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00905F60&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
