# IopMountVolume

- RVA: `0x00A329D0`–`0x00A330AB` (길이 `1,755` bytes)
- VA: `0x0000000140A329D0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000AD438`
- 디코드: `414`개 명령, `1,755/1,755` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **42**; 고유 호출 대상: **29**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **15**

### Outgoing calls
- `0x00A32A49` → [MmIsThisAnNtAsSystem](../../text/4B/MmIsThisAnNtAsSystem_function_004B2860.md) (function, `0x004B2860`)
- `0x00A32A7D` → [ExAcquireRundownProtection](../../text/21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00A32ABF` → [IopWaitForLockAlertable](../../text/47/IopWaitForLockAlertable_function_0047A684.md) (function, `0x0047A684`)
- `0x00A32AEE` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x00A32AF6` → [IopQueryVpbFlagsSafe](../../text/4A/IopQueryVpbFlagsSafe_function_004A1184.md) (function, `0x004A1184`)
- `0x00A32B17` → [KeInitializeEvent](../../text/40/KeInitializeEvent_function_0040DD10.md) (function, `0x0040DD10`)
- `0x00A32B3D` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (function, `0x0020FA20`)
- `0x00A32BCD` → [KeResetEvent](../../text/24/KeResetEvent_function_00248350.md) (function, `0x00248350`)
- `0x00A32BDC` → [IopAllocateIrpWithExtension](../../text/29/IopAllocateIrpWithExtension_function_0029DF38.md) (function, `0x0029DF38`)
- `0x00A32C51` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (function, `0x0020FA20`)
- `0x00A32C5D` → [IopIncrementDeviceObjectRefCount](../../text/41/IopIncrementDeviceObjectRefCount_function_0041B1D0.md) (function, `0x0041B1D0`)
- `0x00A32C70` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00A32C7B` → [IofCallDriver](../../text/29/IofCallDriver_function_0029B4B0.md) (function, `0x0029B4B0`)
- `0x00A32C9C` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x00A32CBB` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00A32CCD` → [IopDecrementDeviceObjectRef](../../text/27/IopDecrementDeviceObjectRef_function_00270970.md) (function, `0x00270970`)
- `0x00A32CE9` → [IopMountInitializeVpb](../../text/49/IopMountInitializeVpb_function_004972C4.md) (function, `0x004972C4`)
- `0x00A32D39` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00A32D45` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00A32D5B` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x00A32D60` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00A32D68` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x00A32D87` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00A32D95` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00A32E23` → [FsRtlIsTotalDeviceFailure](../../text/40/FsRtlIsTotalDeviceFailure_function_00408710.md) (function, `0x00408710`)
- `0x00A32E83` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00A32E95` → [MmIsThisAnNtAsSystem](../../text/4B/MmIsThisAnNtAsSystem_function_004B2860.md) (function, `0x004B2860`)
- `0x00A32ED1` → [McTemplateK0jhzr1_EtwWriteTransfer](../../text/42/McTemplateK0jhzr1_EtwWriteTransfer_function_00424504.md) (function, `0x00424504`)
- `0x00A32EE4` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A32F1D` → [IoGetActivityIdThread](../../text/44/IoGetActivityIdThread_function_00445030.md) (function, `0x00445030`)
- `0x00A32F31` → [IoVolumeDeviceToGuid](../95/IoVolumeDeviceToGuid_function_00952A90.md) (function, `0x00952A90`)
- `0x00A32F3E` → [IoVolumeDeviceToDosName](../8A/IoVolumeDeviceToDosName_function_008A63F0.md) (function, `0x008A63F0`)
- `0x00A32F5A` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (function, `0x0020E6B0`)
- `0x00A32F64` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00A32F79` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A32F83` → [MmIsThisAnNtAsSystem](../../text/4B/MmIsThisAnNtAsSystem_function_004B2860.md) (function, `0x004B2860`)
- `0x00A32FC2` → [McTemplateK0jhzr1_EtwWriteTransfer](../../text/42/McTemplateK0jhzr1_EtwWriteTransfer_function_00424504.md) (function, `0x00424504`)
- `0x00A32FEC` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x00A33035` → [IopIncrementDeviceObjectRefCount](../../text/41/IopIncrementDeviceObjectRefCount_function_0041B1D0.md) (function, `0x0041B1D0`)
- `0x00A33041` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00A3305E` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x00A330A1` → [McTemplateK0jhzr1d_EtwWriteTransfer](../../text/59/McTemplateK0jhzr1d_EtwWriteTransfer_function_00597748.md) (function, `0x00597748`)

### Direct callers
- [IopCheckVpbMounted](../../text/27/IopCheckVpbMounted_function_00270540.md) at `0x0027084A`
- [IoVerifyVolume](../AC/IoVerifyVolume_function_00ACF200.md) at `0x00ACF398`

### Static image references
- `0x00A329EC` → RVA `0x00E0A740` (`.data`; read)
- `0x00A32A57` → RVA `0x00F8D290` (`.data`; read)
- `0x00A32AE3` → RVA `0x00F8D320` (`.data`; read)
- `0x00A32B4E` → RVA `0x00F8D280` (`.data`; read)
- `0x00A32C39` → RVA `0x00F8D200` (`.data`; read)
- `0x00A32C62` → RVA `0x00E66118` (`.data`; read/write)
- `0x00A32CAB` → RVA `0x00E6611C` (`.data`; read)
- `0x00A32E62` → RVA `0x00FC41A0` (`.data`; read)
- `0x00A32EA6` → RVA `0x00F8D8D4` (`.data`; read)
- `0x00A32EBD` → RVA `0x0001A300` (`.rdata`; read)
- `0x00A32F00` → RVA `0x00F8D270` (`.data`; read)
- `0x00A32F90` → RVA `0x00F8D8D4` (`.data`; reference)
- `0x00A32FAB` → RVA `0x00021188` (`.rdata`; read)
- `0x00A32FCD` → RVA `0x00F8D260` (`.data`; read)
- `0x00A32FE3` → RVA `0x00F8D6E0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **40**
  - `0x00A32A49` → [MmIsThisAnNtAsSystem](../../text/4B/MmIsThisAnNtAsSystem_function_004B2860.md) (`PAGE` → `.text`)
  - `0x00A32A7D` → [ExAcquireRundownProtection](../../text/21/ExAcquireRundownProtection_function_00216620.md) (`PAGE` → `.text`)
  - `0x00A32ABF` → [IopWaitForLockAlertable](../../text/47/IopWaitForLockAlertable_function_0047A684.md) (`PAGE` → `.text`)
  - `0x00A32AEE` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x00A32AF6` → [IopQueryVpbFlagsSafe](../../text/4A/IopQueryVpbFlagsSafe_function_004A1184.md) (`PAGE` → `.text`)
  - `0x00A32B17` → [KeInitializeEvent](../../text/40/KeInitializeEvent_function_0040DD10.md) (`PAGE` → `.text`)
  - `0x00A32B3D` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (`PAGE` → `.text`)
  - `0x00A32BCD` → [KeResetEvent](../../text/24/KeResetEvent_function_00248350.md) (`PAGE` → `.text`)
  - `0x00A32BDC` → [IopAllocateIrpWithExtension](../../text/29/IopAllocateIrpWithExtension_function_0029DF38.md) (`PAGE` → `.text`)
  - `0x00A32C51` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (`PAGE` → `.text`)
  - `0x00A32C5D` → [IopIncrementDeviceObjectRefCount](../../text/41/IopIncrementDeviceObjectRefCount_function_0041B1D0.md) (`PAGE` → `.text`)
  - `0x00A32C70` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00A32C7B` → [IofCallDriver](../../text/29/IofCallDriver_function_0029B4B0.md) (`PAGE` → `.text`)
  - `0x00A32C9C` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x00A32CBB` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00A32CCD` → [IopDecrementDeviceObjectRef](../../text/27/IopDecrementDeviceObjectRef_function_00270970.md) (`PAGE` → `.text`)
  - `0x00A32CE9` → [IopMountInitializeVpb](../../text/49/IopMountInitializeVpb_function_004972C4.md) (`PAGE` → `.text`)
  - `0x00A32D39` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00A32D45` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00A32D5B` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (`PAGE` → `.text`)
  - `0x00A32D60` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00A32D68` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x00A32D87` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (`PAGE` → `.text`)
  - `0x00A32D95` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x00A32E23` → [FsRtlIsTotalDeviceFailure](../../text/40/FsRtlIsTotalDeviceFailure_function_00408710.md) (`PAGE` → `.text`)
  - `0x00A32E83` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x00A32E95` → [MmIsThisAnNtAsSystem](../../text/4B/MmIsThisAnNtAsSystem_function_004B2860.md) (`PAGE` → `.text`)
  - `0x00A32ED1` → [McTemplateK0jhzr1_EtwWriteTransfer](../../text/42/McTemplateK0jhzr1_EtwWriteTransfer_function_00424504.md) (`PAGE` → `.text`)
  - `0x00A32EE4` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A32F1D` → [IoGetActivityIdThread](../../text/44/IoGetActivityIdThread_function_00445030.md) (`PAGE` → `.text`)
  - `0x00A32F5A` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (`PAGE` → `.text`)
  - `0x00A32F64` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00A32F79` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A32F83` → [MmIsThisAnNtAsSystem](../../text/4B/MmIsThisAnNtAsSystem_function_004B2860.md) (`PAGE` → `.text`)
  - `0x00A32FC2` → [McTemplateK0jhzr1_EtwWriteTransfer](../../text/42/McTemplateK0jhzr1_EtwWriteTransfer_function_00424504.md) (`PAGE` → `.text`)
  - `0x00A32FEC` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (`PAGE` → `.text`)
  - `0x00A33035` → [IopIncrementDeviceObjectRefCount](../../text/41/IopIncrementDeviceObjectRefCount_function_0041B1D0.md) (`PAGE` → `.text`)
  - `0x00A33041` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00A3305E` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (`PAGE` → `.text`)
  - `0x00A330A1` → [McTemplateK0jhzr1d_EtwWriteTransfer](../../text/59/McTemplateK0jhzr1d_EtwWriteTransfer_function_00597748.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **5**
  - `0x00A32F8A` → [sub_00B39BB0](../B3/Unknown_function_00B39BB0.md) (`tail-transfer`)
  - `0x00A32F97` → [sub_00B39BB0](../B3/Unknown_function_00B39BB0.md) (`tail-transfer`)
  - `0x00A32FC8` → [sub_00B39BB0](../B3/Unknown_function_00B39BB0.md) (`tail-transfer`)
  - `0x00A3304C` → [sub_00B39BB0 + 0xA](../B3/Unknown_function_00B39BB0.md) (`tail-transfer`)
  - `0x00A33066` → [sub_00B39BB0 + 0xA](../B3/Unknown_function_00B39BB0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00A329D0  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00A329D5  55                              push rbp
00A329D6  56                              push rsi
00A329D7  57                              push rdi
00A329D8  41 54                           push r12
00A329DA  41 55                           push r13
00A329DC  41 56                           push r14
00A329DE  41 57                           push r15
00A329E0  48 8D 6C 24 F0                  lea rbp, [rsp - 0x10]
00A329E5  48 81 EC 10 01 00 00            sub rsp, 0x110
00A329EC  48 8B 05 4D 7D 3D 00            mov rax, qword ptr [rip + 0x3d7d4d]
00A329F3  48 33 C4                        xor rax, rsp
00A329F6  48 89 45 08                     mov qword ptr [rbp + 8], rax
00A329FA  48 8B 45 70                     mov rax, qword ptr [rbp + 0x70]
00A329FE  0F 57 C0                        xorps xmm0, xmm0
00A32A01  0F 57 C9                        xorps xmm1, xmm1
00A32A04  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
00A32A08  33 C0                           xor eax, eax
00A32A0A  44 88 4C 24 46                  mov byte ptr [rsp + 0x46], r9b
00A32A0F  45 33 F6                        xor r14d, r14d
00A32A12  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
00A32A16  88 44 24 43                     mov byte ptr [rsp + 0x43], al
00A32A1A  45 8A E9                        mov r13b, r9b
00A32A1D  45 8A F8                        mov r15b, r8b
00A32A20  44 88 44 24 45                  mov byte ptr [rsp + 0x45], r8b
00A32A25  88 54 24 40                     mov byte ptr [rsp + 0x40], dl
00A32A29  48 8B F9                        mov rdi, rcx
00A32A2C  0F 11 45 B0                     movups xmmword ptr [rbp - 0x50], xmm0
00A32A30  4C 89 74 24 60                  mov qword ptr [rsp + 0x60], r14
00A32A35  45 32 E4                        xor r12b, r12b
00A32A38  0F 11 45 80                     movups xmmword ptr [rbp - 0x80], xmm0
00A32A3C  0F 11 4D 90                     movups xmmword ptr [rbp - 0x70], xmm1
00A32A40  0F 11 45 C8                     movups xmmword ptr [rbp - 0x38], xmm0
00A32A44  0F 11 4C 24 68                  movups xmmword ptr [rsp + 0x68], xmm1
00A32A49  E8 12 FE A7 FF                  call 0x1404b2860
00A32A4E  0F 57 C0                        xorps xmm0, xmm0
00A32A51  88 44 24 42                     mov byte ptr [rsp + 0x42], al
00A32A55  8A D8                           mov bl, al
00A32A57  48 8D 0D 32 A8 55 00            lea rcx, [rip + 0x55a832]
00A32A5E  33 C0                           xor eax, eax
00A32A60  48 89 45 F8                     mov qword ptr [rbp - 8], rax
00A32A64  89 45 00                        mov dword ptr [rbp], eax
00A32A67  0F 11 45 D8                     movups xmmword ptr [rbp - 0x28], xmm0
00A32A6B  0F 11 45 E8                     movups xmmword ptr [rbp - 0x18], xmm0
00A32A6F  65 48 8B 34 25 88 01 00 00      mov rsi, qword ptr gs:[0x188]
00A32A78  48 89 74 24 50                  mov qword ptr [rsp + 0x50], rsi
00A32A7D  E8 9E 3B 7E FF                  call 0x140216620
00A32A82  84 C0                           test al, al
00A32A84  0F 84 89 04 00 00               je 0x140a32f13
00A32A8A  84 DB                           test bl, bl
00A32A8C  0F 85 8B 04 00 00               jne 0x140a32f1d
00A32A92  83 CA FF                        or edx, 0xffffffff
00A32A95  45 84 FF                        test r15b, r15b
00A32A98  0F 85 34 03 00 00               jne 0x140a32dd2
00A32A9E  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00A32AA7  45 8A C5                        mov r8b, r13b
00A32AAA  66 01 91 E4 01 00 00            add word ptr [rcx + 0x1e4], dx
00A32AB1  90                              nop
00A32AB2  8A 96 32 02 00 00               mov dl, byte ptr [rsi + 0x232]
00A32AB8  48 8D 8F 18 01 00 00            lea rcx, [rdi + 0x118]
00A32ABF  E8 C0 7B A4 FF                  call 0x14047a684
00A32AC4  8B D8                           mov ebx, eax
00A32AC6  85 C0                           test eax, eax
00A32AC8  0F 88 96 04 00 00               js 0x140a32f64
00A32ACE  8A 5C 24 42                     mov bl, byte ptr [rsp + 0x42]
00A32AD2  41 BF 01 00 00 00               mov r15d, 1
00A32AD8  45 8A E7                        mov r12b, r15b
00A32ADB  66 44 29 BE E4 01 00 00         sub word ptr [rsi + 0x1e4], r15w
00A32AE3  48 8D 0D 36 A8 55 00            lea rcx, [rip + 0x55a836]
00A32AEA  41 8A D7                        mov dl, r15b
00A32AED  90                              nop
00A32AEE  E8 CD F0 7D FF                  call 0x140211bc0
00A32AF3  48 8B CF                        mov rcx, rdi
00A32AF6  E8 89 E6 A6 FF                  call 0x1404a1184
00A32AFB  0F B7 C0                        movzx eax, ax
00A32AFE  A8 09                           test al, 9
00A32B00  0F 85 DE 02 00 00               jne 0x140a32de4
00A32B06  84 DB                           test bl, bl
00A32B08  0F 85 75 04 00 00               jne 0x140a32f83
00A32B0E  45 33 C0                        xor r8d, r8d
00A32B11  48 8D 4D B0                     lea rcx, [rbp - 0x50]
00A32B15  33 D2                           xor edx, edx
00A32B17  E8 F4 B1 9D FF                  call 0x14040dd10
00A32B1C  83 67 30 FD                     and dword ptr [rdi + 0x30], 0xfffffffd
00A32B20  BB 01 00 00 C0                  mov ebx, 0xc0000001
00A32B25  48 8B 47 18                     mov rax, qword ptr [rdi + 0x18]
00A32B29  4C 8B EF                        mov r13, rdi
00A32B2C  EB 07                           jmp 0x140a32b35
00A32B2E  4C 8B E8                        mov r13, rax
00A32B31  48 8B 40 18                     mov rax, qword ptr [rax + 0x18]
00A32B35  48 85 C0                        test rax, rax
00A32B38  75 F4                           jne 0x140a32b2e
00A32B3A  49 8B CD                        mov rcx, r13
00A32B3D  E8 DE CE 7D FF                  call 0x14020fa20
00A32B42  8B 47 48                        mov eax, dword ptr [rdi + 0x48]
00A32B45  83 F8 07                        cmp eax, 7
00A32B48  0F 85 A0 03 00 00               jne 0x140a32eee
00A32B4E  48 8B 35 2B A7 55 00            mov rsi, qword ptr [rip + 0x55a72b]
00A32B55  4C 8D 3D 24 A7 55 00            lea r15, [rip + 0x55a724]
00A32B5C  48 8B 47 38                     mov rax, qword ptr [rdi + 0x38]
00A32B60  8A 54 24 40                     mov dl, byte ptr [rsp + 0x40]
00A32B64  0F B7 48 04                     movzx ecx, word ptr [rax + 4]
00A32B68  83 E1 10                        and ecx, 0x10
00A32B6B  89 4C 24 48                     mov dword ptr [rsp + 0x48], ecx
00A32B6F  49 3B F7                        cmp rsi, r15
00A32B72  0F 84 B5 01 00 00               je 0x140a32d2d
00A32B78  85 DB                           test ebx, ebx
00A32B7A  0F 89 EB 04 00 00               jns 0x140a3306b
00A32B80  48 8B 06                        mov rax, qword ptr [rsi]
00A32B83  49 3B C7                        cmp rax, r15
00A32B86  48 89 45 A8                     mov qword ptr [rbp - 0x58], rax
00A32B8A  0F 94 44 24 44                  sete byte ptr [rsp + 0x44]
00A32B8F  84 D2                           test dl, dl
00A32B91  0F 84 1F 02 00 00               je 0x140a32db6
00A32B97  85 C9                           test ecx, ecx
00A32B99  74 0A                           je 0x140a32ba5
00A32B9B  49 3B C7                        cmp rax, r15
00A32B9E  74 05                           je 0x140a32ba5
00A32BA0  48 8B 36                        mov rsi, qword ptr [rsi]
00A32BA3  EB CA                           jmp 0x140a32b6f
00A32BA5  48 8D 5E B0                     lea rbx, [rsi - 0x50]
00A32BA9  41 BE 01 00 00 00               mov r14d, 1
00A32BAF  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
00A32BB3  48 89 5C 24 78                  mov qword ptr [rsp + 0x78], rbx
00A32BB8  EB 0A                           jmp 0x140a32bc4
00A32BBA  48 8B D8                        mov rbx, rax
00A32BBD  41 FF C6                        inc r14d
00A32BC0  48 8B 40 18                     mov rax, qword ptr [rax + 0x18]
00A32BC4  48 85 C0                        test rax, rax
00A32BC7  75 F1                           jne 0x140a32bba
00A32BC9  48 8D 4D B0                     lea rcx, [rbp - 0x50]
00A32BCD  E8 7E 57 81 FF                  call 0x140248350
00A32BD2  45 02 75 4C                     add r14b, byte ptr [r13 + 0x4c]
00A32BD6  45 33 C0                        xor r8d, r8d
00A32BD9  41 8A D6                        mov dl, r14b
00A32BDC  E8 57 B3 86 FF                  call 0x14029df38
00A32BE1  4C 8B F0                        mov r14, rax
00A32BE4  48 85 C0                        test rax, rax
00A32BE7  0F 84 F0 01 00 00               je 0x140a32ddd
00A32BED  49 8B 8E B8 00 00 00            mov rcx, qword ptr [r14 + 0xb8]
00A32BF4  C7 40 10 42 00 00 00            mov dword ptr [rax + 0x10], 0x42
00A32BFB  48 8D 45 D8                     lea rax, [rbp - 0x28]
00A32BFF  49 89 46 18                     mov qword ptr [r14 + 0x18], rax
00A32C03  48 8D 45 B0                     lea rax, [rbp - 0x50]
00A32C07  49 89 46 50                     mov qword ptr [r14 + 0x50], rax
00A32C0B  48 8D 45 80                     lea rax, [rbp - 0x80]
00A32C0F  49 89 46 48                     mov qword ptr [r14 + 0x48], rax
00A32C13  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
00A32C18  49 89 86 98 00 00 00            mov qword ptr [r14 + 0x98], rax
00A32C1F  8A 44 24 40                     mov al, byte ptr [rsp + 0x40]
00A32C23  41 C6 46 40 00                  mov byte ptr [r14 + 0x40], 0
00A32C28  88 41 BA                        mov byte ptr [rcx - 0x46], al
00A32C2B  66 C7 41 B8 0D 01               mov word ptr [rcx - 0x48], 0x10d
00A32C31  48 8B 47 38                     mov rax, qword ptr [rdi + 0x38]
00A32C35  48 89 41 C0                     mov qword ptr [rcx - 0x40], rax
00A32C39  8B 05 C1 A5 55 00               mov eax, dword ptr [rip + 0x55a5c1]
00A32C3F  4C 89 69 C8                     mov qword ptr [rcx - 0x38], r13
00A32C43  C7 41 D0 2C 00 00 00            mov dword ptr [rcx - 0x30], 0x2c
00A32C4A  48 8B CB                        mov rcx, rbx
00A32C4D  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
00A32C51  E8 CA CD 7D FF                  call 0x14020fa20
00A32C56  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
00A32C5B  B2 01                           mov dl, 1
00A32C5D  E8 6E 85 9E FF                  call 0x14041b1d0
00A32C62  F0 FF 05 AF 34 43 00            lock inc dword ptr [rip + 0x4334af]
00A32C69  48 8D 0D B0 A6 55 00            lea rcx, [rip + 0x55a6b0]
00A32C70  E8 9B CD 82 FF                  call 0x14025fa10
00A32C75  49 8B D6                        mov rdx, r14
00A32C78  48 8B CB                        mov rcx, rbx
00A32C7B  E8 30 88 86 FF                  call 0x14029b4b0
00A32C80  3D 03 01 00 00                  cmp eax, 0x103
00A32C85  0F 84 BD 02 00 00               je 0x140a32f48
00A32C8B  48 83 65 88 00                  and qword ptr [rbp - 0x78], 0
00A32C90  89 45 80                        mov dword ptr [rbp - 0x80], eax
00A32C93  B2 01                           mov dl, 1
00A32C95  48 8D 0D 84 A6 55 00            lea rcx, [rip + 0x55a684]
00A32C9C  E8 1F EF 7D FF                  call 0x140211bc0
00A32CA1  83 C8 FF                        or eax, 0xffffffff
00A32CA4  F0 01 05 6D 34 43 00            lock add dword ptr [rip + 0x43346d], eax
00A32CAB  83 3D 6A 34 43 00 00            cmp dword ptr [rip + 0x43346a], 0
00A32CB2  0F 85 28 03 00 00               jne 0x140a32fe0
00A32CB8  48 8B CB                        mov rcx, rbx
00A32CBB  E8 90 66 8C FF                  call 0x1402f9350
00A32CC0  4C 8B 74 24 78                  mov r14, qword ptr [rsp + 0x78]
00A32CC5  45 33 C0                        xor r8d, r8d
00A32CC8  49 8B CE                        mov rcx, r14
00A32CCB  33 D2                           xor edx, edx
00A32CCD  E8 9E DC 83 FF                  call 0x140270970
00A32CD2  8B 5D 80                        mov ebx, dword ptr [rbp - 0x80]
00A32CD5  85 DB                           test ebx, ebx
00A32CD7  78 29                           js 0x140a32d02
00A32CD9  44 8A 4C 24 44                  mov r9b, byte ptr [rsp + 0x44]
00A32CDE  49 8B D5                        mov rdx, r13
00A32CE1  44 8B 44 24 48                  mov r8d, dword ptr [rsp + 0x48]
00A32CE6  48 8B CF                        mov rcx, rdi
00A32CE9  E8 D6 45 A6 FF                  call 0x1404972c4
00A32CEE  48 8B 4D A0                     mov rcx, qword ptr [rbp - 0x60]
00A32CF2  48 89 01                        mov qword ptr [rcx], rax
00A32CF5  8B 4C 24 48                     mov ecx, dword ptr [rsp + 0x48]
00A32CF9  8A 54 24 40                     mov dl, byte ptr [rsp + 0x40]
00A32CFD  E9 9E FE FF FF                  jmp 0x140a32ba0
00A32D02  8D 83 5E FF FF 3F               lea eax, [rbx + 0x3fffff5e]
00A32D08  B9 01 00 00 00                  mov ecx, 1
00A32D0D  3B C1                           cmp eax, ecx
00A32D0F  76 12                           jbe 0x140a32d23
00A32D11  8D 83 ED FF FF 3F               lea eax, [rbx + 0x3fffffed]
00A32D17  81 FB 12 00 00 C0               cmp ebx, 0xc0000012
00A32D1D  0F 85 D3 02 00 00               jne 0x140a32ff6
00A32D23  48 39 4D 88                     cmp qword ptr [rbp - 0x78], rcx
00A32D27  0F 85 C9 00 00 00               jne 0x140a32df6
00A32D2D  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
00A32D32  85 DB                           test ebx, ebx
00A32D34  79 08                           jns 0x140a32d3e
00A32D36  49 8B CD                        mov rcx, r13
00A32D39  E8 12 66 8C FF                  call 0x1402f9350
00A32D3E  48 8D 0D DB A5 55 00            lea rcx, [rip + 0x55a5db]
00A32D45  E8 C6 CC 82 FF                  call 0x14025fa10
00A32D4A  45 84 E4                        test r12b, r12b
00A32D4D  74 16                           je 0x140a32d65
00A32D4F  48 8D 8F 18 01 00 00            lea rcx, [rdi + 0x118]
00A32D56  45 33 C0                        xor r8d, r8d
00A32D59  33 D2                           xor edx, edx
00A32D5B  E8 B0 C5 90 FF                  call 0x14033f310
00A32D60  E8 4B AB 82 FF                  call 0x14025d8b0
00A32D65  48 8B CE                        mov rcx, rsi
00A32D68  E8 83 C2 82 FF                  call 0x14025eff0
00A32D6D  80 7C 24 42 00                  cmp byte ptr [rsp + 0x42], 0
00A32D72  0F 85 11 01 00 00               jne 0x140a32e89
00A32D78  85 DB                           test ebx, ebx
00A32D7A  0F 88 D5 00 00 00               js 0x140a32e55
00A32D80  48 8D 0D 09 A5 55 00            lea rcx, [rip + 0x55a509]
00A32D87  E8 F4 70 91 FF                  call 0x140349e80
00A32D8C  8B C3                           mov eax, ebx
00A32D8E  48 8B 4D 08                     mov rcx, qword ptr [rbp + 8]
00A32D92  48 33 CC                        xor rcx, rsp
00A32D95  E8 A6 98 C7 FF                  call 0x1406ac640
00A32D9A  48 8B 9C 24 58 01 00 00         mov rbx, qword ptr [rsp + 0x158]
00A32DA2  48 81 C4 10 01 00 00            add rsp, 0x110
00A32DA9  41 5F                           pop r15
00A32DAB  41 5E                           pop r14
00A32DAD  41 5D                           pop r13
00A32DAF  41 5C                           pop r12
00A32DB1  5F                              pop rdi
00A32DB2  5E                              pop rsi
00A32DB3  5D                              pop rbp
00A32DB4  C3                              ret
00A32DB5  CC                              int3
00A32DB6  49 3B C7                        cmp rax, r15
00A32DB9  0F 85 D8 FD FF FF               jne 0x140a32b97
00A32DBF  49 3B 37                        cmp rsi, qword ptr [r15]
00A32DC2  0F 84 CF FD FF FF               je 0x140a32b97
00A32DC8  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
00A32DCD  E9 64 FF FF FF                  jmp 0x140a32d36
00A32DD2  41 BF 01 00 00 00               mov r15d, 1
00A32DD8  E9 FE FC FF FF                  jmp 0x140a32adb
00A32DDD  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00A32DE2  EB E4                           jmp 0x140a32dc8
00A32DE4  24 08                           and al, 8
00A32DE6  BB C0 00 00 C0                  mov ebx, 0xc00000c0
00A32DEB  F6 D8                           neg al
00A32DED  1B C0                           sbb eax, eax
00A32DEF  23 D8                           and ebx, eax
00A32DF1  E9 48 FF FF FF                  jmp 0x140a32d3e
00A32DF6  8B 44 24 58                     mov eax, dword ptr [rsp + 0x58]
00A32DFA  3B 05 00 A4 55 00               cmp eax, dword ptr [rip + 0x55a400]
00A32E00  0F 85 15 02 00 00               jne 0x140a3301b
00A32E06  81 FB 9C 01 00 C0               cmp ebx, 0xc000019c
00A32E0C  0F 84 1E 02 00 00               je 0x140a33030
00A32E12  41 8A C4                        mov al, r12b
00A32E15  81 FB 4F 01 00 C0               cmp ebx, 0xc000014f
00A32E1B  0F 84 D4 FE FF FF               je 0x140a32cf5
00A32E21  8B CB                           mov ecx, ebx
00A32E23  E8 E8 58 9D FF                  call 0x140408710
00A32E28  84 C0                           test al, al
00A32E2A  0F 84 C5 FE FF FF               je 0x140a32cf5
00A32E30  80 7C 24 40 00                  cmp byte ptr [rsp + 0x40], 0
00A32E35  41 8A CC                        mov cl, r12b
00A32E38  0F 84 EF FE FF FF               je 0x140a32d2d
00A32E3E  4C 39 7D A8                     cmp qword ptr [rbp - 0x58], r15
00A32E42  0F 84 E5 FE FF FF               je 0x140a32d2d
00A32E48  49 8B 47 08                     mov rax, qword ptr [r15 + 8]
00A32E4C  48 8B 70 08                     mov rsi, qword ptr [rax + 8]
00A32E50  E9 A0 FE FF FF                  jmp 0x140a32cf5
00A32E55  F7 47 30 00 01 00 00            test dword ptr [rdi + 0x30], 0x100
00A32E5C  0F 84 1E FF FF FF               je 0x140a32d80
00A32E62  83 3D 37 13 59 00 02            cmp dword ptr [rip + 0x591337], 2
00A32E69  0F 83 11 FF FF FF               jae 0x140a32d80
00A32E6F  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
00A32E75  45 33 C9                        xor r9d, r9d
00A32E78  4C 63 C3                        movsxd r8, ebx
00A32E7B  48 8B D7                        mov rdx, rdi
00A32E7E  B9 ED 00 00 00                  mov ecx, 0xed
00A32E83  E8 D8 A7 AC FF                  call 0x1404fd660
00A32E88  CC                              int3
00A32E89  80 7C 24 43 00                  cmp byte ptr [rsp + 0x43], 0
00A32E8E  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
00A32E93  74 41                           je 0x140a32ed6
00A32E95  E8 C6 F9 A7 FF                  call 0x1404b2860
00A32E9A  84 C0                           test al, al
00A32E9C  74 38                           je 0x140a32ed6
00A32E9E  85 DB                           test ebx, ebx
00A32EA0  0F 88 CF 01 00 00               js 0x140a33075
00A32EA6  F6 05 27 AA 55 00 01            test byte ptr [rip + 0x55aa27], 1
00A32EAD  74 27                           je 0x140a32ed6
00A32EAF  0F B7 44 24 68                  movzx eax, word ptr [rsp + 0x68]
00A32EB4  4C 8D 4D C8                     lea r9, [rbp - 0x38]
00A32EB8  4C 8B 44 24 60                  mov r8, qword ptr [rsp + 0x60]
00A32EBD  48 8D 15 3C 74 5E FF            lea rdx, [rip - 0xa18bc4]
00A32EC4  66 D1 E8                        shr ax, 1
00A32EC7  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
00A32ECC  66 89 44 24 20                  mov word ptr [rsp + 0x20], ax
00A32ED1  E8 2E 16 9F FF                  call 0x140424504
00A32ED6  48 85 F6                        test rsi, rsi
00A32ED9  0F 84 99 FE FF FF               je 0x140a32d78
00A32EDF  33 D2                           xor edx, edx
00A32EE1  48 8B CE                        mov rcx, rsi
00A32EE4  E8 87 F9 14 00                  call 0x140b82870
00A32EE9  E9 8A FE FF FF                  jmp 0x140a32d78
00A32EEE  83 F8 24                        cmp eax, 0x24
00A32EF1  0F 84 57 FC FF FF               je 0x140a32b4e
00A32EF7  83 F8 02                        cmp eax, 2
00A32EFA  0F 85 CD 00 00 00               jne 0x140a32fcd
00A32F00  48 8B 35 69 A3 55 00            mov rsi, qword ptr [rip + 0x55a369]
00A32F07  4C 8D 3D 62 A3 55 00            lea r15, [rip + 0x55a362]
00A32F0E  E9 49 FC FF FF                  jmp 0x140a32b5c
00A32F13  B8 89 01 00 C0                  mov eax, 0xc0000189
00A32F18  E9 71 FE FF FF                  jmp 0x140a32d8e
00A32F1D  E8 0E 21 A1 FF                  call 0x140445030
00A32F22  48 8D 55 C8                     lea rdx, [rbp - 0x38]
00A32F26  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00A32F2B  48 8B CF                        mov rcx, rdi
00A32F2E  4C 8B F0                        mov r14, rax
00A32F31  E8 5A FB F1 FF                  call 0x140952a90
00A32F36  48 8D 54 24 68                  lea rdx, [rsp + 0x68]
00A32F3B  48 8B CF                        mov rcx, rdi
00A32F3E  E8 AD 34 E7 FF                  call 0x1408a63f0
00A32F43  E9 4A FB FF FF                  jmp 0x140a32a92
00A32F48  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
00A32F4E  48 8D 4D B0                     lea rcx, [rbp - 0x50]
00A32F52  45 33 C9                        xor r9d, r9d
00A32F55  45 33 C0                        xor r8d, r8d
00A32F58  33 D2                           xor edx, edx
00A32F5A  E8 51 B7 7D FF                  call 0x14020e6b0
00A32F5F  E9 2F FD FF FF                  jmp 0x140a32c93
00A32F64  E8 47 A9 82 FF                  call 0x14025d8b0
00A32F69  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
00A32F6E  48 85 C9                        test rcx, rcx
00A32F71  0F 84 09 FE FF FF               je 0x140a32d80
00A32F77  33 D2                           xor edx, edx
00A32F79  E8 F2 F8 14 00                  call 0x140b82870
00A32F7E  E9 FD FD FF FF                  jmp 0x140a32d80
00A32F83  E8 D8 F8 A7 FF                  call 0x1404b2860
00A32F88  84 C0                           test al, al
00A32F8A  0F 84 20 6C 10 00               je 0x140b39bb0
00A32F90  44 84 3D 3D A9 55 00            test byte ptr [rip + 0x55a93d], r15b
00A32F97  0F 84 13 6C 10 00               je 0x140b39bb0
00A32F9D  0F B7 4C 24 68                  movzx ecx, word ptr [rsp + 0x68]
00A32FA2  4C 8D 4D C8                     lea r9, [rbp - 0x38]
00A32FA6  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
00A32FAB  48 8D 15 D6 E1 5E FF            lea rdx, [rip - 0xa11e2a]
00A32FB2  66 D1 E9                        shr cx, 1
00A32FB5  4D 8B C6                        mov r8, r14
00A32FB8  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A32FBD  66 89 4C 24 20                  mov word ptr [rsp + 0x20], cx
00A32FC2  E8 3D 15 9F FF                  call 0x140424504
00A32FC7  90                              nop
00A32FC8  E9 E3 6B 10 00                  jmp 0x140b39bb0
00A32FCD  48 8B 35 8C A2 55 00            mov rsi, qword ptr [rip + 0x55a28c]
00A32FD4  4C 8D 3D 85 A2 55 00            lea r15, [rip + 0x55a285]
00A32FDB  E9 7C FB FF FF                  jmp 0x140a32b5c
00A32FE0  45 33 C0                        xor r8d, r8d
00A32FE3  48 8D 0D F6 A6 55 00            lea rcx, [rip + 0x55a6f6]
00A32FEA  33 D2                           xor edx, edx
00A32FEC  E8 1F C3 90 FF                  call 0x14033f310
00A32FF1  E9 C2 FC FF FF                  jmp 0x140a32cb8
00A32FF6  3B C1                           cmp eax, ecx
00A32FF8  0F 86 25 FD FF FF               jbe 0x140a32d23
00A32FFE  81 FB 16 00 00 80               cmp ebx, 0x80000016
00A33004  0F 84 19 FD FF FF               je 0x140a32d23
00A3300A  81 FB B5 00 00 C0               cmp ebx, 0xc00000b5
00A33010  0F 84 0D FD FF FF               je 0x140a32d23
00A33016  E9 DB FD FF FF                  jmp 0x140a32df6
00A3301B  49 8B 07                        mov rax, qword ptr [r15]
00A3301E  48 8D 75 90                     lea rsi, [rbp - 0x70]
00A33022  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
00A33026  BB 4F 01 00 C0                  mov ebx, 0xc000014f
00A3302B  E9 E2 FD FF FF                  jmp 0x140a32e12
00A33030  8A D1                           mov dl, cl
00A33032  49 8B CE                        mov rcx, r14
00A33035  E8 96 81 9E FF                  call 0x14041b1d0
00A3303A  48 8D 0D DF A2 55 00            lea rcx, [rip + 0x55a2df]
00A33041  E8 CA C9 82 FF                  call 0x14025fa10
00A33046  8A 5C 24 45                     mov bl, byte ptr [rsp + 0x45]
00A3304A  84 DB                           test bl, bl
00A3304C  0F 85 68 6B 10 00               jne 0x140b39bba
00A33052  48 8D 8F 18 01 00 00            lea rcx, [rdi + 0x118]
00A33059  45 33 C0                        xor r8d, r8d
00A3305C  33 D2                           xor edx, edx
00A3305E  E8 AD C2 90 FF                  call 0x14033f310
00A33063  45 32 E4                        xor r12b, r12b
00A33066  E9 4F 6B 10 00                  jmp 0x140b39bba
00A3306B  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
00A33070  E9 C9 FC FF FF                  jmp 0x140a32d3e
00A33075  F6 05 58 A8 55 00 02            test byte ptr [rip + 0x55a858], 2
00A3307C  0F 84 54 FE FF FF               je 0x140a32ed6
00A33082  0F B7 44 24 68                  movzx eax, word ptr [rsp + 0x68]
00A33087  4C 8D 4D C8                     lea r9, [rbp - 0x38]
00A3308B  4C 8B 44 24 60                  mov r8, qword ptr [rsp + 0x60]
00A33090  66 D1 E8                        shr ax, 1
00A33093  89 5C 24 30                     mov dword ptr [rsp + 0x30], ebx
00A33097  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
00A3309C  66 89 44 24 20                  mov word ptr [rsp + 0x20], ax
00A330A1  E8 A2 46 B6 FF                  call 0x140597748
00A330A6  E9 2B FE FF FF                  jmp 0x140a32ed6
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopMountVolume(__int64 a1, int a2, unsigned __int8 a3, unsigned __int8 a4, __int64 a5)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned int v_stack_m100;
    unsigned __int8 v_stack_m102;
    unsigned __int8 v_stack_m103;
    unsigned __int8 v_stack_m104;
    unsigned __int8 v_stack_m105;
    unsigned __int8 v_stack_m106;
    unsigned __int8 v_stack_m108;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned int v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned int v_stack_p30;
    unsigned __int8 v_stack_p40;
    unsigned __int8 v_stack_p43;
    unsigned __int8 v_stack_p45;
    unsigned __int64 v_stack_p50;
    unsigned int v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int16 v_stack_p68;
    unsigned __int64 v_stack_p70;

    v_stack_p10 = v_rbx;
    v_rsp = (v_rsp) - (272);
    result = (*(unsigned __int64 *)(v_rip + 4029773)) ^ (v_rsp);
    v_stack_m40 = result;
    v_stack_mA8 = a5;
    result = 0;
    v_stack_m102 = a4;
    v_r14 = 0;
    v_stack_m88 = 0;
    v_stack_m105 = 0;
    v_stack_m103 = a3;
    v_stack_m108 = (unsigned __int8)(a2);
    v_stack_m98 = v_xmm0;
    v_stack_mE8 = 0;
    v_r12 = 0;
    v_stack_mC8 = v_xmm0;
    v_stack_mB8 = v_xmm1;
    v_stack_m80 = v_xmm0;
    v_stack_mE0 = v_xmm1;
    result = MmIsThisAnNtAsSystem(a1, a2, a3, a4);
    v_stack_m106 = (unsigned __int8)(result);
    result = 0;
    v_stack_m50 = 0;
    v_stack_m48 = 0;
    v_stack_m70 = v_xmm0;
    v_stack_m60 = v_xmm0;
    v_stack_mF8 = *(unsigned __int64 *)(gs_base + (0 + 392));
    result = ExAcquireRundownProtection(v_rip + 5613618, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00A32F13;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) goto loc_00A32F1D;
loc_00A32A92:
    a2 = (unsigned int)((a2) | (0xFFFFFFFFULL));
    if (a3 != 0) goto loc_00A32DD2;
    result = IopWaitForLockAlertable(a1 + 280, *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562), a4, a4);
    if (sign_flag) goto loc_00A32F64;
loc_00A32ADB:
    result = ExAcquireResourceSharedLite(v_rip + 5613622, 1, a4, a4);
    result = IopQueryVpbFlagsSafe(a1, 1, a4, a4);
    if ((((unsigned __int8)((unsigned __int16)(result))) & (9)) != 0) goto loc_00A32DE4;
    if ((unsigned __int8)(v_stack_m106) != 0) goto loc_00A32F83;
    a3 = 0;
    a2 = 0;
    result = KeInitializeEvent(v_stack_m98, a2, a3, a4);
    goto loc_00A32B35;
loc_00A32B2E:
loc_00A32B35:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 24) != 0) goto loc_00A32B2E;
    result = ObfReferenceObject(*(unsigned __int64 *)(a1 + 24), a2, a3, a4);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 72)))) != 7) goto loc_00A32EEE;
loc_00A32B4E:
loc_00A32B5C:
    a1 = (unsigned int)((*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 56) + 4)) & (16));
    v_stack_m100 = (unsigned int)(a1);
loc_00A32B6F:
    if ((*(unsigned __int64 *)(v_rip + 5613355)) == (v_rip + 5613348)) goto loc_00A32D2D;
    if (!sign_flag) goto loc_00A3306B;
    v_stack_mA0 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 5613355));
    if ((unsigned __int8)(v_stack_m108) == 0) goto loc_00A32DB6;
loc_00A32B97:
    if ((unsigned int)(a1) == 0) goto loc_00A32BA5;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 5613355))) == (v_rip + 5613348)) goto loc_00A32BA5;
loc_00A32BA0:
    goto loc_00A32B6F;
loc_00A32BA5:
    v_stack_mD0 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 5613355)) - 80;
    goto loc_00A32BC4;
loc_00A32BBA:
    v_r14 = (unsigned int)((1) + 1);
loc_00A32BC4:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 5613355)) - 80 + 24) + 24) != 0) goto loc_00A32BBA;
    result = KeResetEvent(v_stack_m98, v_stack_m108, a3, a4);
    v_r14 = (unsigned __int8)((v_r14) + (*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 24) + 76)));
    a3 = 0;
    result = IopAllocateIrpWithExtension(v_stack_m98, (unsigned __int8)(v_r14), a3, a4);
    if (result == 0) goto loc_00A32DDD;
    *(unsigned int *)(result + 16) = 66;
    *(unsigned __int64 *)(result + 24) = v_stack_m70;
    *(unsigned __int64 *)(result + 80) = v_stack_m98;
    *(unsigned __int64 *)(result + 72) = v_stack_mC8;
    *(unsigned __int64 *)(result + 152) = v_stack_mF8;
    *(unsigned __int8 *)(result + 64) = 0;
    *(unsigned __int8 *)(*(unsigned __int64 *)(result + 184) - 70) = (unsigned __int8)(v_stack_m108);
    *(unsigned __int16 *)(*(unsigned __int64 *)(result + 184) - 72) = 269;
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 184) - 64) = *(unsigned __int64 *)(a1 + 56);
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 184) - 56) = *(unsigned __int64 *)(a1 + 24);
    *(unsigned int *)(*(unsigned __int64 *)(result + 184) - 48) = 44;
    v_stack_mF0 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5612993)));
    result = ObfReferenceObject(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 5613355)) - 80 + 24), (unsigned __int8)(v_r14), a3, a4);
    result = IopIncrementDeviceObjectRefCount(v_stack_mD0, 1, a3, a4);
    result = ExReleaseResourceLite(v_rip + 5613232, 1, a3, a4);
    result = IofCallDriver(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 5613355)) - 80 + 24), result, a3, a4);
    if (((unsigned int)(result)) == 259) goto loc_00A32F48;
    v_stack_mC8 = (unsigned int)(result);
loc_00A32C93:
    result = ExAcquireResourceSharedLite(v_rip + 5613188, 1, a3, a4);
    result = (unsigned int)((result) | (0xFFFFFFFFULL));
    if ((*(unsigned int *)(v_rip + 4404330)) != 0) goto loc_00A32FE0;
loc_00A32CB8:
    result = ObfDereferenceObject(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 5613355)) - 80 + 24), 1, a3, a4);
    a3 = 0;
    a2 = 0;
    result = IopDecrementDeviceObjectRef(v_stack_mD0, a2, a3, a4);
    if (sign_flag) goto loc_00A32D02;
    result = IopMountInitializeVpb(a1, *(unsigned __int64 *)(a1 + 24), (unsigned int)(v_stack_m100), v_stack_m104);
    *(unsigned __int64 *)(v_stack_mA8) = result;
loc_00A32CF5:
    goto loc_00A32BA0;
loc_00A32D02:
    if (((unsigned int)((unsigned int)(v_stack_mC8) + 1073741662)) <= 1) goto loc_00A32D23;
    if (((unsigned int)((unsigned int)(v_stack_mC8))) != 0xC0000012ULL) goto loc_00A32FF6;
loc_00A32D23:
    if (v_stack_mC0 != 1) goto loc_00A32DF6;
loc_00A32D2D:
    result = (unsigned int)(v_stack_mC8) + 1073741805;
    if (sign_flag) {
        a1 = *(unsigned __int64 *)(a1 + 24);
        result = ObfDereferenceObject(a1, v_stack_m108, (unsigned int)(v_stack_m100), v_stack_m104);
    }
    result = ExReleaseResourceLite(v_rip + 5613019, v_stack_m108, (unsigned int)(v_stack_m100), v_stack_m104);
    if (1 != 0) {
        a1 = a1 + 280;
        a3 = 0;
        a2 = 0;
        result = KeSetEvent(a1, a2, a3, v_stack_m104);
        result = KeLeaveCriticalRegion(a1, a2, a3, v_stack_m104);
    }
    result = KeLeaveCriticalRegionThread(v_stack_mF8, a2, a3, v_stack_m104);
    if (v_stack_m106 != 0) goto loc_00A32E89;
loc_00A32D78:
    if (sign_flag) goto loc_00A32E55;
loc_00A32D80:
    result = ExReleaseRundownProtection(v_rip + 5612809, a2, a3, v_stack_m104);
loc_00A32D8E:
    a1 = (v_stack_m40) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, v_stack_m104);
    v_rsp = (v_rsp) + (272);
    return result;
loc_00A32DB6:
    if (result != (v_rip + 5613348)) goto loc_00A32B97;
    if (v_stack_mF8 == (*(unsigned __int64 *)(v_rip + 5613348))) goto loc_00A32B97;
loc_00A32DC8:
    goto loc_00A32D36;
loc_00A32DD2:
    goto loc_00A32ADB;
loc_00A32DDD:
    goto loc_00A32DC8;
loc_00A32DE4:
    result = (unsigned __int8)((result) & (8));
    result = (unsigned __int8)(-(result));
    v_rbx = (unsigned int)(((unsigned int)(0xC00000C0ULL)) & ((unsigned int)(result)));
    goto loc_00A32D3E;
loc_00A32DF6:
    if (((unsigned int)((unsigned int)(v_stack_p58))) != (*(unsigned int *)(v_rip + 5612544))) goto loc_00A3301B;
    if (((unsigned int)(v_rbx)) == 0xC000019CULL) goto loc_00A33030;
loc_00A32E12:
    if (((unsigned int)(v_rbx)) == 0xC000014FULL) goto loc_00A32CF5;
    result = FsRtlIsTotalDeviceFailure((unsigned int)((unsigned int)(v_rbx)), a2, a3, v_stack_m104);
    if ((unsigned __int8)(result) == 0) goto loc_00A32CF5;
    if (v_stack_p40 == 0) goto loc_00A32D2D;
    if (v_stack_mA0 == 1) goto loc_00A32D2D;
    goto loc_00A32CF5;
loc_00A32E55:
    if (((*(unsigned int *)(a1 + 48)) & (256)) == 0) goto loc_00A32D80;
    if ((*(unsigned int *)(v_rip + 5837623)) >= 2) goto loc_00A32D80;
    a4 = 0;
    result = KeBugCheckEx(237, a1, (int)((unsigned int)(v_rbx)), a4);
loc_00A32E89:
    if (v_stack_p43 == 0) goto loc_00A32ED6;
    result = MmIsThisAnNtAsSystem(237, a1, (int)((unsigned int)(v_rbx)), a4);
    if ((unsigned __int8)(result) == 0) goto loc_00A32ED6;
    if (sign_flag) goto loc_00A33075;
    if (((*(unsigned __int8 *)(v_rip + 5614119)) & (1)) != 0) {
        result = v_stack_p68;
        a4 = v_stack_m80;
        a3 = v_stack_p60;
        a2 = v_rip - 10587076;
        result = (unsigned __int16)((result) >> (1));
        v_stack_p28 = v_stack_p70;
        v_stack_p20 = (unsigned __int16)(result);
        result = McTemplateK0jhzr1_EtwWriteTransfer(237, a2, a3, a4);
    }
    if (v_stack_p70 == 0) goto loc_00A32D78;
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_p70, a2, a3, a4);
    goto loc_00A32D78;
loc_00A32EEE:
    if (((unsigned int)(result)) == 36) goto loc_00A32B4E;
    if (((unsigned int)(result)) != 2) goto loc_00A32FCD;
    goto loc_00A32B5C;
loc_00A32F13:
    goto loc_00A32D8E;
loc_00A32F1D:
    result = IoGetActivityIdThread(v_stack_p70, a2, a3, a4);
    v_stack_p60 = result;
    result = IoVolumeDeviceToGuid(a1, v_stack_m80, a3, a4);
    result = IoVolumeDeviceToDosName(a1, v_stack_p68, a3, a4);
    goto loc_00A32A92;
loc_00A32F48:
    a4 = 0;
    a3 = 0;
    a2 = 0;
    result = KeWaitForSingleObject(v_stack_m98, a2, a3, a4);
    goto loc_00A32C93;
loc_00A32F64:
    result = KeLeaveCriticalRegion(v_stack_m98, a2, a3, a4);
    if (v_stack_p70 == 0) goto loc_00A32D80;
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_p70, a2, a3, a4);
    goto loc_00A32D80;
loc_00A32F83:
    result = MmIsThisAnNtAsSystem(v_stack_p70, a2, a3, a4);
    a1 = (unsigned __int16)((v_stack_p68) >> (1));
    v_stack_p28 = v_stack_p70;
    v_stack_p20 = (unsigned __int16)(a1);
    result = McTemplateK0jhzr1_EtwWriteTransfer(a1, v_rip - 10559018, result, v_stack_m80);
loc_00A32FCD:
    goto loc_00A32B5C;
loc_00A32FE0:
    a3 = 0;
    a2 = 0;
    result = KeSetEvent(v_rip + 5613302, a2, a3, v_stack_m80);
    goto loc_00A32CB8;
loc_00A32FF6:
    if (((unsigned int)(result)) <= ((unsigned int)(v_rip + 5613302))) goto loc_00A32D23;
    if (((unsigned int)(v_rbx)) == 0x80000016ULL) goto loc_00A32D23;
    if (((unsigned int)(v_rbx)) == 0xC00000B5ULL) goto loc_00A32D23;
    goto loc_00A32DF6;
loc_00A3301B:
    v_stack_mB8 = *(unsigned __int64 *)(v_rip + 5612165);
    goto loc_00A32E12;
loc_00A33030:
    result = IopIncrementDeviceObjectRefCount(result, (unsigned __int8)(v_rip + 5613302), a3, v_stack_m80);
    result = ExReleaseResourceLite(v_rip + 5612255, (unsigned __int8)(v_rip + 5613302), a3, v_stack_m80);
    a3 = 0;
    a2 = 0;
    result = KeSetEvent(a1 + 280, a2, a3, v_stack_m80);
    v_r12 = 0;
loc_00A3306B:
    goto loc_00A32D3E;
loc_00A33075:
    if (((*(unsigned __int8 *)(v_rip + 5613656)) & (2)) == 0) goto loc_00A32ED6;
    result = (unsigned __int16)((v_stack_p68) >> (1));
    v_stack_p30 = (unsigned int)(v_stack_p45);
    v_stack_p28 = v_stack_p50;
    v_stack_p20 = (unsigned __int16)(result);
    result = McTemplateK0jhzr1d_EtwWriteTransfer(a1 + 280, a2, v_stack_p60, v_stack_m80);
    goto loc_00A32ED6;
}
```

## 5. (Beta) C Style

```c
int64_t IopMountVolume(void *Arg1, int32_t Arg2, uint8_t Arg3, uint8_t Arg4, int64_t Arg5)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rsp;
    uint32_t v_stack_m100;
    uint8_t v_stack_m102;
    uint8_t v_stack_m103;
    uint8_t v_stack_m104;
    uint8_t v_stack_m105;
    uint8_t v_stack_m106;
    uint8_t v_stack_m108;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m60;
    uint64_t v_stack_m70;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint32_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint32_t v_stack_p30;
    uint8_t v_stack_p40;
    uint8_t v_stack_p43;
    uint8_t v_stack_p45;
    uint64_t v_stack_p50;
    uint32_t v_stack_p58;
    uint64_t v_stack_p60;
    uint16_t v_stack_p68;
    uint64_t v_stack_p70;

    v_stack_p10 = local_rbx;
    local_rsp = (local_rsp) - (272);
    result = (*(uint64_t *)(v_rip + 0x3D7D4D)) ^ (local_rsp);
    v_stack_m40 = result;
    v_stack_mA8 = Arg5;
    result = 0;
    v_stack_m102 = Arg4;
    local_r14 = 0;
    v_stack_m88 = 0;
    v_stack_m105 = 0;
    v_stack_m103 = Arg3;
    v_stack_m108 = (uint8_t)(Arg2);
    v_stack_m98 = v_xmm0;
    v_stack_mE8 = 0;
    local_r12 = 0;
    v_stack_mC8 = v_xmm0;
    v_stack_mB8 = v_xmm1;
    v_stack_m80 = v_xmm0;
    v_stack_mE0 = v_xmm1;
    result = MmIsThisAnNtAsSystem(Arg1, Arg2, Arg3, Arg4);
    v_stack_m106 = (uint8_t)(result);
    result = 0;
    v_stack_m50 = 0;
    v_stack_m48 = 0;
    v_stack_m70 = v_xmm0;
    v_stack_m60 = v_xmm0;
    v_stack_mF8 = *(uint64_t *)(gs_base + (0 + 0x188));
    result = ExAcquireRundownProtection(v_rip + 5613618, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00A32F13;
    if ((uint8_t)((uint8_t)(result)) != 0) goto loc_00A32F1D;
loc_00A32A92:
    Arg2 = (uint32_t)((Arg2) | (0xFFFFFFFFULL));
    if (Arg3 != 0) goto loc_00A32DD2;
    result = IopWaitForLockAlertable(Arg1 + 280, *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232), Arg4, Arg4);
    if (sign_flag) goto loc_00A32F64;
loc_00A32ADB:
    result = ExAcquireResourceSharedLite(v_rip + 5613622, 1, Arg4, Arg4);
    result = IopQueryVpbFlagsSafe(Arg1, 1, Arg4, Arg4);
    if ((((uint8_t)((uint16_t)(result))) & (9)) != 0) goto loc_00A32DE4;
    if ((uint8_t)(v_stack_m106) != 0) goto loc_00A32F83;
    Arg3 = 0;
    Arg2 = 0;
    result = KeInitializeEvent(v_stack_m98, Arg2, Arg3, Arg4);
    goto loc_00A32B35;
loc_00A32B2E:
loc_00A32B35:
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x18) != 0) goto loc_00A32B2E;
    result = ObfReferenceObject(*(uint64_t *)(arg1 + 0x18), Arg2, Arg3, Arg4);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x48)))) != 7) goto loc_00A32EEE;
loc_00A32B4E:
loc_00A32B5C:
    Arg1 = (uint32_t)((*(uint16_t *)(*(uint64_t *)(arg1 + 0x38) + 0x4)) & (16));
    v_stack_m100 = (uint32_t)(Arg1);
loc_00A32B6F:
    if ((*(uint64_t *)(v_rip + 0x55A72B)) == (v_rip + 5613348)) goto loc_00A32D2D;
    if (!sign_flag) goto loc_00A3306B;
    v_stack_mA0 = *(uint64_t *)(*(uint64_t *)(v_rip + 0x55A72B));
    if ((uint8_t)(v_stack_m108) == 0) goto loc_00A32DB6;
loc_00A32B97:
    if ((uint32_t)(Arg1) == 0) goto loc_00A32BA5;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x55A72B))) == (v_rip + 5613348)) goto loc_00A32BA5;
loc_00A32BA0:
    goto loc_00A32B6F;
loc_00A32BA5:
    v_stack_mD0 = *(uint64_t *)(*(uint64_t *)(v_rip + 0x55A72B)) - 80;
    goto loc_00A32BC4;
loc_00A32BBA:
    local_r14 = (uint32_t)((1) + 1);
loc_00A32BC4:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x55A72B)) - 0x50 + 0x18) + 0x18) != 0) goto loc_00A32BBA;
    result = KeResetEvent(v_stack_m98, v_stack_m108, Arg3, Arg4);
    local_r14 = (uint8_t)((local_r14) + (*(uint8_t *)(*(uint64_t *)(arg1 + 0x18) + 0x4C)));
    Arg3 = 0;
    result = IopAllocateIrpWithExtension(v_stack_m98, (uint8_t)(local_r14), Arg3, Arg4);
    if (result == 0) goto loc_00A32DDD;
    *(uint32_t *)(result + 0x10) = 66;
    *(uint64_t *)(result + 0x18) = v_stack_m70;
    *(uint64_t *)(result + 0x50) = v_stack_m98;
    *(uint64_t *)(result + 0x48) = v_stack_mC8;
    *(uint64_t *)(result + 0x98) = v_stack_mF8;
    *(uint8_t *)(result + 0x40) = 0;
    *(uint8_t *)(*(uint64_t *)(result + 0xB8) - 0x46) = (uint8_t)(v_stack_m108);
    *(uint16_t *)(*(uint64_t *)(result + 0xB8) - 0x48) = 269;
    *(uint64_t *)(*(uint64_t *)(result + 0xB8) - 0x40) = *(uint64_t *)(arg1 + 0x38);
    *(uint64_t *)(*(uint64_t *)(result + 0xB8) - 0x38) = *(uint64_t *)(arg1 + 0x18);
    *(uint32_t *)(*(uint64_t *)(result + 0xB8) - 0x30) = 44;
    v_stack_mF0 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x55A5C1)));
    result = ObfReferenceObject(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x55A72B)) - 0x50 + 0x18), (uint8_t)(local_r14), Arg3, Arg4);
    result = IopIncrementDeviceObjectRefCount(v_stack_mD0, 1, Arg3, Arg4);
    result = ExReleaseResourceLite(v_rip + 5613232, 1, Arg3, Arg4);
    result = IofCallDriver(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x55A72B)) - 0x50 + 0x18), result, Arg3, Arg4);
    if (((uint32_t)(result)) == 259) goto loc_00A32F48;
    v_stack_mC8 = (uint32_t)(result);
loc_00A32C93:
    result = ExAcquireResourceSharedLite(v_rip + 5613188, 1, Arg3, Arg4);
    result = (uint32_t)((result) | (0xFFFFFFFFULL));
    if ((*(uint32_t *)(v_rip + 0x43346A)) != 0) goto loc_00A32FE0;
loc_00A32CB8:
    result = ObfDereferenceObject(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x55A72B)) - 0x50 + 0x18), 1, Arg3, Arg4);
    Arg3 = 0;
    Arg2 = 0;
    result = IopDecrementDeviceObjectRef(v_stack_mD0, Arg2, Arg3, Arg4);
    if (sign_flag) goto loc_00A32D02;
    result = IopMountInitializeVpb(Arg1, *(uint64_t *)(arg1 + 0x18), (uint32_t)(v_stack_m100), v_stack_m104);
    *(uint64_t *)(v_stack_mA8) = result;
loc_00A32CF5:
    goto loc_00A32BA0;
loc_00A32D02:
    if (((uint32_t)((uint32_t)(v_stack_mC8) + 1073741662)) <= 1) goto loc_00A32D23;
    if (((uint32_t)((uint32_t)(v_stack_mC8))) != 0xC0000012ULL) goto loc_00A32FF6;
loc_00A32D23:
    if (v_stack_mC0 != 1) goto loc_00A32DF6;
loc_00A32D2D:
    result = (uint32_t)(v_stack_mC8) + 1073741805;
    if (sign_flag) {
        Arg1 = *(uint64_t *)(arg1 + 0x18);
        result = ObfDereferenceObject(Arg1, v_stack_m108, (uint32_t)(v_stack_m100), v_stack_m104);
    }
    result = ExReleaseResourceLite(v_rip + 5613019, v_stack_m108, (uint32_t)(v_stack_m100), v_stack_m104);
    if (1 != 0) {
        Arg1 = Arg1 + 280;
        Arg3 = 0;
        Arg2 = 0;
        result = KeSetEvent(Arg1, Arg2, Arg3, v_stack_m104);
        result = KeLeaveCriticalRegion(Arg1, Arg2, Arg3, v_stack_m104);
    }
    result = KeLeaveCriticalRegionThread(v_stack_mF8, Arg2, Arg3, v_stack_m104);
    if (v_stack_m106 != 0) goto loc_00A32E89;
loc_00A32D78:
    if (sign_flag) goto loc_00A32E55;
loc_00A32D80:
    result = ExReleaseRundownProtection(v_rip + 5612809, Arg2, Arg3, v_stack_m104);
loc_00A32D8E:
    Arg1 = (v_stack_m40) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, v_stack_m104);
    local_rsp = (local_rsp) + (272);
    return result;
loc_00A32DB6:
    if (result != (v_rip + 5613348)) goto loc_00A32B97;
    if (v_stack_mF8 == (*(uint64_t *)(v_rip + 0x55A724))) goto loc_00A32B97;
loc_00A32DC8:
    goto loc_00A32D36;
loc_00A32DD2:
    goto loc_00A32ADB;
loc_00A32DDD:
    goto loc_00A32DC8;
loc_00A32DE4:
    result = (uint8_t)((result) & (8));
    result = (uint8_t)(-(result));
    local_rbx = (uint32_t)(((uint32_t)(0xC00000C0ULL)) & ((uint32_t)(result)));
    goto loc_00A32D3E;
loc_00A32DF6:
    if (((uint32_t)((uint32_t)(v_stack_p58))) != (*(uint32_t *)(v_rip + 0x55A400))) goto loc_00A3301B;
    if (((uint32_t)(local_rbx)) == 0xC000019CULL) goto loc_00A33030;
loc_00A32E12:
    if (((uint32_t)(local_rbx)) == 0xC000014FULL) goto loc_00A32CF5;
    result = FsRtlIsTotalDeviceFailure((uint32_t)((uint32_t)(local_rbx)), Arg2, Arg3, v_stack_m104);
    if ((uint8_t)(result) == 0) goto loc_00A32CF5;
    if (v_stack_p40 == 0) goto loc_00A32D2D;
    if (v_stack_mA0 == 1) goto loc_00A32D2D;
    goto loc_00A32CF5;
loc_00A32E55:
    if (((*(uint32_t *)(arg1 + 0x30)) & (256)) == 0) goto loc_00A32D80;
    if ((*(uint32_t *)(v_rip + 0x591337)) >= 2) goto loc_00A32D80;
    Arg4 = 0;
    result = KeBugCheckEx(237, Arg1, (int32_t)((uint32_t)(local_rbx)), Arg4);
loc_00A32E89:
    if (v_stack_p43 == 0) goto loc_00A32ED6;
    result = MmIsThisAnNtAsSystem(237, Arg1, (int32_t)((uint32_t)(local_rbx)), Arg4);
    if ((uint8_t)(result) == 0) goto loc_00A32ED6;
    if (sign_flag) goto loc_00A33075;
    if (((*(uint8_t *)(v_rip + 0x55AA27)) & (1)) != 0) {
        result = v_stack_p68;
        Arg4 = v_stack_m80;
        Arg3 = v_stack_p60;
        Arg2 = v_rip - 10587076;
        result = (uint16_t)((result) >> (1));
        v_stack_p28 = v_stack_p70;
        v_stack_p20 = (uint16_t)(result);
        result = McTemplateK0jhzr1_EtwWriteTransfer(237, Arg2, Arg3, Arg4);
    }
    if (v_stack_p70 == 0) goto loc_00A32D78;
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_p70, Arg2, Arg3, Arg4);
    goto loc_00A32D78;
loc_00A32EEE:
    if (((uint32_t)(result)) == 36) goto loc_00A32B4E;
    if (((uint32_t)(result)) != 2) goto loc_00A32FCD;
    goto loc_00A32B5C;
loc_00A32F13:
    goto loc_00A32D8E;
loc_00A32F1D:
    result = IoGetActivityIdThread(v_stack_p70, Arg2, Arg3, Arg4);
    v_stack_p60 = result;
    result = IoVolumeDeviceToGuid(Arg1, v_stack_m80, Arg3, Arg4);
    result = IoVolumeDeviceToDosName(Arg1, v_stack_p68, Arg3, Arg4);
    goto loc_00A32A92;
loc_00A32F48:
    Arg4 = 0;
    Arg3 = 0;
    Arg2 = 0;
    result = KeWaitForSingleObject(v_stack_m98, Arg2, Arg3, Arg4);
    goto loc_00A32C93;
loc_00A32F64:
    result = KeLeaveCriticalRegion(v_stack_m98, Arg2, Arg3, Arg4);
    if (v_stack_p70 == 0) goto loc_00A32D80;
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_p70, Arg2, Arg3, Arg4);
    goto loc_00A32D80;
loc_00A32F83:
    result = MmIsThisAnNtAsSystem(v_stack_p70, Arg2, Arg3, Arg4);
    Arg1 = (uint16_t)((v_stack_p68) >> (1));
    v_stack_p28 = v_stack_p70;
    v_stack_p20 = (uint16_t)(Arg1);
    result = McTemplateK0jhzr1_EtwWriteTransfer(Arg1, v_rip - 10559018, result, v_stack_m80);
loc_00A32FCD:
    goto loc_00A32B5C;
loc_00A32FE0:
    Arg3 = 0;
    Arg2 = 0;
    result = KeSetEvent(v_rip + 5613302, Arg2, Arg3, v_stack_m80);
    goto loc_00A32CB8;
loc_00A32FF6:
    if (((uint32_t)(result)) <= ((uint32_t)(v_rip + 5613302))) goto loc_00A32D23;
    if (((uint32_t)(local_rbx)) == 0x80000016ULL) goto loc_00A32D23;
    if (((uint32_t)(local_rbx)) == 0xC00000B5ULL) goto loc_00A32D23;
    goto loc_00A32DF6;
loc_00A3301B:
    v_stack_mB8 = *(uint64_t *)(v_rip + 0x55A285);
    goto loc_00A32E12;
loc_00A33030:
    result = IopIncrementDeviceObjectRefCount(result, (uint8_t)(v_rip + 5613302), Arg3, v_stack_m80);
    result = ExReleaseResourceLite(v_rip + 5612255, (uint8_t)(v_rip + 5613302), Arg3, v_stack_m80);
    Arg3 = 0;
    Arg2 = 0;
    result = KeSetEvent(Arg1 + 280, Arg2, Arg3, v_stack_m80);
    local_r12 = 0;
loc_00A3306B:
    goto loc_00A32D3E;
loc_00A33075:
    if (((*(uint8_t *)(v_rip + 0x55A858)) & (2)) == 0) goto loc_00A32ED6;
    result = (uint16_t)((v_stack_p68) >> (1));
    v_stack_p30 = (uint32_t)(v_stack_p45);
    v_stack_p28 = v_stack_p50;
    v_stack_p20 = (uint16_t)(result);
    result = McTemplateK0jhzr1d_EtwWriteTransfer(Arg1 + 280, Arg2, v_stack_p60, v_stack_m80);
    goto loc_00A32ED6;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x30` | `32` | `R` |
| `Arg1` | `+ 0x30` | `32` | `R/W` |
| `Arg1` | `+ 0x38` | `64` | `R` |
| `Arg1` | `+ 0x48` | `32` | `R` |
| `Arg1` | `+ 0x118` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A329D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
