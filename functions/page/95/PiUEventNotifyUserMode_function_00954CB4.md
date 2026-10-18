# PiUEventNotifyUserMode

- RVA: `0x00954CB4`–`0x0095527C` (길이 `1,480` bytes)
- VA: `0x0000000140954CB4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000922A0`
- 디코드: `382`개 명령, `1,480/1,480` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **34**; 고유 호출 대상: **24**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **15**

### Outgoing calls
- `0x00954D3C` → [PiUEventDeviceNeedsInstall](../A8/PiUEventDeviceNeedsInstall_function_00A8B1BC.md) (function, `0x00A8B1BC`)
- `0x00954D4C` → [PpDevCfgRequestDeviceInstall](../70/PpDevCfgRequestDeviceInstall_function_00704520.md) (function, `0x00704520`)
- `0x00954D68` → [McTemplateK0z_EtwWriteTransfer](../../text/4D/McTemplateK0z_EtwWriteTransfer_function_004DEF6C.md) (function, `0x004DEF6C`)
- `0x00954D72` → [PiUEventShouldQueueEvent](../../text/49/PiUEventShouldQueueEvent_function_00491910.md) (function, `0x00491910`)
- `0x00954D7E` → [PiUEventIsDeviceEventVetoable](../A5/PiUEventIsDeviceEventVetoable_function_00A51650.md) (function, `0x00A51650`)
- `0x00954D86` → [Feature_KernelPnP_CheckDeviceInstancePath__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_KernelPnP_CheckDeviceInstancePath__private_IsEnabledDeviceUsageNoInline_function_004F58C4.md) (function, `0x004F58C4`)
- `0x00954E0C` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00954E31` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00954E4C` → [KeInitializeGuardedMutex](../../text/46/KeInitializeGuardedMutex_function_00466E90.md) (function, `0x00466E90`)
- `0x00954EC5` → [PnpWatchdogTimerPause](PnpWatchdogTimerPause_function_00955B6C.md) (function, `0x00955B6C`)
- `0x00954EDC` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00954F02` → [KeInitializeEvent](../../text/40/KeInitializeEvent_function_0040DD10.md) (function, `0x0040DD10`)
- `0x00954F0A` → [PiUEventReferenceEventEntry](../A2/PiUEventReferenceEventEntry_function_00A2143C.md) (function, `0x00A2143C`)
- `0x00954F2F` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00954F54` → [RtlStringCchCopyNW](../../text/47/RtlStringCchCopyNW_function_0047169C.md) (function, `0x0047169C`)
- `0x00954F5C` → [PiUEventCacheObjectProperties](../A2/PiUEventCacheObjectProperties_function_00A2C458.md) (function, `0x00A2C458`)
- `0x00954F68` → [ExAcquireFastMutex](../../text/20/ExAcquireFastMutex_function_0020E5A0.md) (function, `0x0020E5A0`)
- `0x00954FA6` → [ExReleaseFastMutex](../../text/25/ExReleaseFastMutex_function_002519C0.md) (function, `0x002519C0`)
- `0x00954FC5` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00954FEF` → [ExQueueWorkItem](../../text/2F/ExQueueWorkItem_function_002F9520.md) (function, `0x002F9520`)
- `0x00955064` → [KeWaitForMultipleObjects](../../text/20/KeWaitForMultipleObjects_function_0020D110.md) (function, `0x0020D110`)
- `0x0095508F` → [ZwUpdateWnfStateData](../../text/6B/ZwUpdateWnfStateData_function_006B0D10.md) (function, `0x006B0D10`)
- `0x0095511B` → [PiUEventGatherEventData](../A6/PiUEventGatherEventData_function_00A6EBAC.md) (function, `0x00A6EBAC`)
- `0x0095515F` → [McTemplateK0jqzjzx_EtwWriteTransfer](../../text/5A/McTemplateK0jqzjzx_EtwWriteTransfer_function_005A7270.md) (function, `0x005A7270`)
- `0x00955186` → [PiUEventGatherEventData](../A6/PiUEventGatherEventData_function_00A6EBAC.md) (function, `0x00A6EBAC`)
- `0x009551C4` → [McTemplateK0jqzjzx_EtwWriteTransfer](../../text/5A/McTemplateK0jqzjzx_EtwWriteTransfer_function_005A7270.md) (function, `0x005A7270`)
- `0x009551DB` → [ExAcquireFastMutex](../../text/20/ExAcquireFastMutex_function_0020E5A0.md) (function, `0x0020E5A0`)
- `0x009551F1` → [ExReleaseFastMutex](../../text/25/ExReleaseFastMutex_function_002519C0.md) (function, `0x002519C0`)
- `0x009551F9` → [PiUEventDereferenceEventEntry](../9C/PiUEventDereferenceEventEntry_function_009C3244.md) (function, `0x009C3244`)
- `0x0095520D` → [PnpWatchdogTimerStart](../8F/PnpWatchdogTimerStart_function_008FB624.md) (function, `0x008FB624`)
- `0x00955229` → [ExAcquireFastMutex](../../text/20/ExAcquireFastMutex_function_0020E5A0.md) (function, `0x0020E5A0`)
- `0x0095524E` → [ExReleaseFastMutex](../../text/25/ExReleaseFastMutex_function_002519C0.md) (function, `0x002519C0`)
- `0x00955263` → [PiUEventDereferenceEventEntry](../9C/PiUEventDereferenceEventEntry_function_009C3244.md) (function, `0x009C3244`)
- `0x0095526B` → [PiUEventFreeEventEntry](../9C/PiUEventFreeEventEntry_function_009C32A4.md) (function, `0x009C32A4`)

### Direct callers
- [PnpNotifyUserModeDeviceRemoval](PnpNotifyUserModeDeviceRemoval_function_00954258.md) at `0x00954363`
- [PnpProcessCustomDeviceEvent](PnpProcessCustomDeviceEvent_function_00954734.md) at `0x0095475F`
- [PnpDeviceEventWorker](PnpDeviceEventWorker_function_009556B0.md) at `0x0095598C`
- [PnpDeviceEventWorker](PnpDeviceEventWorker_function_009556B0.md) at `0x009559BE`
- [PnpProcessTargetDeviceEvent](../A0/PnpProcessTargetDeviceEvent_function_00A046BC.md) at `0x00A047D3`
- [sub_00B269D0](../B2/Unknown_function_00B269D0.md) at `0x00B269D3`

### Static image references
- `0x00954CD5` → RVA `0x00F8C5E4` (`.data`; read)
- `0x00954D55` → RVA `0x00EF012A` (`.data`; read)
- `0x00954D61` → RVA `0x0001E1D8` (`.rdata`; read)
- `0x00954F61` → RVA `0x00F8CAA0` (`.data`; read)
- `0x00954F6D` → RVA `0x00F8CA88` (`.data`; read)
- `0x00954F74` → RVA `0x00F8CA80` (`.data`; read)
- `0x00954F9F` → RVA `0x00F8CA88` (`.data`; write)
- `0x00954FD5` → RVA `0x009C2870` (`PiUEventProcessEventWorker`; read)
- `0x00955002` → RVA `0x00EF012C` (`.data`; read)
- `0x0095501D` → RVA `0x00F8C5E0` (`.data`; read)
- `0x00955033` → RVA `0x00E0AA10` (`.data`; read)
- `0x00955071` → RVA `0x0001E318` (`.rdata`; read)
- `0x009550FC` → RVA `0x00E0AA08` (`.data`; read)
- `0x0095513A` → RVA `0x00027090` (`.rdata`; read)
- `0x0095519B` → RVA `0x00026DC0` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **22**
  - `0x00954D68` → [McTemplateK0z_EtwWriteTransfer](../../text/4D/McTemplateK0z_EtwWriteTransfer_function_004DEF6C.md) (`PAGE` → `.text`)
  - `0x00954D72` → [PiUEventShouldQueueEvent](../../text/49/PiUEventShouldQueueEvent_function_00491910.md) (`PAGE` → `.text`)
  - `0x00954D86` → [Feature_KernelPnP_CheckDeviceInstancePath__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_KernelPnP_CheckDeviceInstancePath__private_IsEnabledDeviceUsageNoInline_function_004F58C4.md) (`PAGE` → `.text`)
  - `0x00954E0C` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00954E31` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00954E4C` → [KeInitializeGuardedMutex](../../text/46/KeInitializeGuardedMutex_function_00466E90.md) (`PAGE` → `.text`)
  - `0x00954EDC` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00954F02` → [KeInitializeEvent](../../text/40/KeInitializeEvent_function_0040DD10.md) (`PAGE` → `.text`)
  - `0x00954F2F` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00954F54` → [RtlStringCchCopyNW](../../text/47/RtlStringCchCopyNW_function_0047169C.md) (`PAGE` → `.text`)
  - `0x00954F68` → [ExAcquireFastMutex](../../text/20/ExAcquireFastMutex_function_0020E5A0.md) (`PAGE` → `.text`)
  - `0x00954FA6` → [ExReleaseFastMutex](../../text/25/ExReleaseFastMutex_function_002519C0.md) (`PAGE` → `.text`)
  - `0x00954FC5` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00954FEF` → [ExQueueWorkItem](../../text/2F/ExQueueWorkItem_function_002F9520.md) (`PAGE` → `.text`)
  - `0x00955064` → [KeWaitForMultipleObjects](../../text/20/KeWaitForMultipleObjects_function_0020D110.md) (`PAGE` → `.text`)
  - `0x0095508F` → [ZwUpdateWnfStateData](../../text/6B/ZwUpdateWnfStateData_function_006B0D10.md) (`PAGE` → `.text`)
  - `0x0095515F` → [McTemplateK0jqzjzx_EtwWriteTransfer](../../text/5A/McTemplateK0jqzjzx_EtwWriteTransfer_function_005A7270.md) (`PAGE` → `.text`)
  - `0x009551C4` → [McTemplateK0jqzjzx_EtwWriteTransfer](../../text/5A/McTemplateK0jqzjzx_EtwWriteTransfer_function_005A7270.md) (`PAGE` → `.text`)
  - `0x009551DB` → [ExAcquireFastMutex](../../text/20/ExAcquireFastMutex_function_0020E5A0.md) (`PAGE` → `.text`)
  - `0x009551F1` → [ExReleaseFastMutex](../../text/25/ExReleaseFastMutex_function_002519C0.md) (`PAGE` → `.text`)
  - `0x00955229` → [ExAcquireFastMutex](../../text/20/ExAcquireFastMutex_function_0020E5A0.md) (`PAGE` → `.text`)
  - `0x0095524E` → [ExReleaseFastMutex](../../text/25/ExReleaseFastMutex_function_002519C0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00954CB4  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00954CB9  55                              push rbp
00954CBA  56                              push rsi
00954CBB  57                              push rdi
00954CBC  41 54                           push r12
00954CBE  41 55                           push r13
00954CC0  41 56                           push r14
00954CC2  41 57                           push r15
00954CC4  48 8D 6C 24 D9                  lea rbp, [rsp - 0x27]
00954CC9  48 81 EC 90 00 00 00            sub rsp, 0x90
00954CD0  33 FF                           xor edi, edi
00954CD2  4C 8B F9                        mov r15, rcx
00954CD5  39 3D 09 79 63 00               cmp dword ptr [rip + 0x637909], edi
00954CDB  8B F7                           mov esi, edi
00954CDD  44 8A EF                        mov r13b, dil
00954CE0  48 89 7D 07                     mov qword ptr [rbp + 7], rdi
00954CE4  44 8B E7                        mov r12d, edi
00954CE7  40 88 7D 6F                     mov byte ptr [rbp + 0x6f], dil
00954CEB  44 8B F7                        mov r14d, edi
00954CEE  48 89 7D FF                     mov qword ptr [rbp - 1], rdi
00954CF2  48 89 7D F7                     mov qword ptr [rbp - 9], rdi
00954CF6  8B DF                           mov ebx, edi
00954CF8  48 89 7D EF                     mov qword ptr [rbp - 0x11], rdi
00954CFC  40 88 7D 7F                     mov byte ptr [rbp + 0x7f], dil
00954D00  74 23                           je 0x140954d25
00954D02  BE 89 01 00 C0                  mov esi, 0xc0000189
00954D07  48 8B 9C 24 D0 00 00 00         mov rbx, qword ptr [rsp + 0xd0]
00954D0F  8B C6                           mov eax, esi
00954D11  48 81 C4 90 00 00 00            add rsp, 0x90
00954D18  41 5F                           pop r15
00954D1A  41 5E                           pop r14
00954D1C  41 5D                           pop r13
00954D1E  41 5C                           pop r12
00954D20  5F                              pop rdi
00954D21  5E                              pop rsi
00954D22  5D                              pop rbp
00954D23  C3                              ret
00954D24  CC                              int3
00954D25  83 B9 88 00 00 00 04            cmp dword ptr [rcx + 0x88], 4
00954D2C  75 41                           jne 0x140954d6f
00954D2E  48 8D B9 A8 00 00 00            lea rdi, [rcx + 0xa8]
00954D35  48 8B CF                        mov rcx, rdi
00954D38  48 8D 55 6F                     lea rdx, [rbp + 0x6f]
00954D3C  E8 7B 64 13 00                  call 0x140a8b1bc
00954D41  33 C9                           xor ecx, ecx
00954D43  85 C0                           test eax, eax
00954D45  78 26                           js 0x140954d6d
00954D47  38 4D 6F                        cmp byte ptr [rbp + 0x6f], cl
00954D4A  74 21                           je 0x140954d6d
00954D4C  E8 CF F7 DA FF                  call 0x140704520
00954D51  85 C0                           test eax, eax
00954D53  78 18                           js 0x140954d6d
00954D55  F6 05 CE B3 59 00 10            test byte ptr [rip + 0x59b3ce], 0x10
00954D5C  74 0F                           je 0x140954d6d
00954D5E  4C 8B CF                        mov r9, rdi
00954D61  48 8D 15 70 94 6C FF            lea rdx, [rip - 0x936b90]
00954D68  E8 FF A1 B8 FF                  call 0x1404def6c
00954D6D  33 FF                           xor edi, edi
00954D6F  49 8B CF                        mov rcx, r15
00954D72  E8 99 CB B3 FF                  call 0x140491910
00954D77  84 C0                           test al, al
00954D79  74 8C                           je 0x140954d07
00954D7B  49 8B CF                        mov rcx, r15
00954D7E  E8 CD C8 0F 00                  call 0x140a51650
00954D83  88 45 6F                        mov byte ptr [rbp + 0x6f], al
00954D86  E8 39 0B BA FF                  call 0x1404f58c4
00954D8B  8B C8                           mov ecx, eax
00954D8D  49 8B 87 A0 00 00 00            mov rax, qword ptr [r15 + 0xa0]
00954D94  48 85 C0                        test rax, rax
00954D97  74 55                           je 0x140954dee
00954D99  85 C9                           test ecx, ecx
00954D9B  74 2C                           je 0x140954dc9
00954D9D  48 8B 88 38 01 00 00            mov rcx, qword ptr [rax + 0x138]
00954DA4  48 8B 51 28                     mov rdx, qword ptr [rcx + 0x28]
00954DA8  48 85 D2                        test rdx, rdx
00954DAB  74 41                           je 0x140954dee
00954DAD  48 8B 42 30                     mov rax, qword ptr [rdx + 0x30]
00954DB1  48 85 C0                        test rax, rax
00954DB4  74 38                           je 0x140954dee
00954DB6  4C 8B E0                        mov r12, rax
00954DB9  49 83 CE FF                     or r14, 0xffffffffffffffff
00954DBD  49 FF C6                        inc r14
00954DC0  66 42 39 3C 70                  cmp word ptr [rax + r14*2], di
00954DC5  75 F6                           jne 0x140954dbd
00954DC7  EB 22                           jmp 0x140954deb
00954DC9  48 8B 80 38 01 00 00            mov rax, qword ptr [rax + 0x138]
00954DD0  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
00954DD4  48 85 C9                        test rcx, rcx
00954DD7  74 15                           je 0x140954dee
00954DD9  4C 8B 61 30                     mov r12, qword ptr [rcx + 0x30]
00954DDD  49 83 CE FF                     or r14, 0xffffffffffffffff
00954DE1  49 FF C6                        inc r14
00954DE4  66 43 39 3C 74                  cmp word ptr [r12 + r14*2], di
00954DE9  75 F6                           jne 0x140954de1
00954DEB  49 FF C6                        inc r14
00954DEE  41 8B 8F 9C 00 00 00            mov ecx, dword ptr [r15 + 0x9c]
00954DF5  41 B8 50 6E 70 59               mov r8d, 0x59706e50
00954DFB  83 C1 50                        add ecx, 0x50
00954DFE  42 8D 0C 71                     lea ecx, [rcx + r14*2]
00954E02  89 4D EB                        mov dword ptr [rbp - 0x15], ecx
00954E05  8B D1                           mov edx, ecx
00954E07  B9 00 01 00 00                  mov ecx, 0x100
00954E0C  E8 DF D2 22 00                  call 0x140b820f0
00954E11  48 8B F8                        mov rdi, rax
00954E14  48 85 C0                        test rax, rax
00954E17  75 0A                           jne 0x140954e23
00954E19  BE 9A 00 00 C0                  mov esi, 0xc000009a
00954E1E  E9 E4 FE FF FF                  jmp 0x140954d07
00954E23  BA 38 00 00 00                  mov edx, 0x38
00954E28  41 B8 50 6E 70 59               mov r8d, 0x59706e50
00954E2E  8D 4A 08                        lea ecx, [rdx + 8]
00954E31  E8 BA D2 22 00                  call 0x140b820f0
00954E36  48 89 47 10                     mov qword ptr [rdi + 0x10], rax
00954E3A  48 85 C0                        test rax, rax
00954E3D  75 0A                           jne 0x140954e49
00954E3F  BE 9A 00 00 C0                  mov esi, 0xc000009a
00954E44  E9 1F 04 00 00                  jmp 0x140955268
00954E49  48 8B C8                        mov rcx, rax
00954E4C  E8 3F 20 B1 FF                  call 0x140466e90
00954E51  8A 4D 6F                        mov cl, byte ptr [rbp + 0x6f]
00954E54  33 D2                           xor edx, edx
00954E56  88 4F 4D                        mov byte ptr [rdi + 0x4d], cl
00954E59  C7 47 38 01 00 00 00            mov dword ptr [rdi + 0x38], 1
00954E60  49 8B 47 30                     mov rax, qword ptr [r15 + 0x30]
00954E64  84 C9                           test cl, cl
00954E66  74 25                           je 0x140954e8d
00954E68  48 89 47 20                     mov qword ptr [rdi + 0x20], rax
00954E6C  49 8B 47 38                     mov rax, qword ptr [r15 + 0x38]
00954E70  48 89 47 28                     mov qword ptr [rdi + 0x28], rax
00954E74  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
00954E78  66 89 11                        mov word ptr [rcx], dx
00954E7B  48 8B 47 28                     mov rax, qword ptr [rdi + 0x28]
00954E7F  8A 4D 6F                        mov cl, byte ptr [rbp + 0x6f]
00954E82  66 89 10                        mov word ptr [rax], dx
00954E85  48 8B 47 20                     mov rax, qword ptr [rdi + 0x20]
00954E89  89 10                           mov dword ptr [rax], edx
00954E8B  EB 1E                           jmp 0x140954eab
00954E8D  48 85 C0                        test rax, rax
00954E90  74 02                           je 0x140954e94
00954E92  89 10                           mov dword ptr [rax], edx
00954E94  49 8B 47 38                     mov rax, qword ptr [r15 + 0x38]
00954E98  48 85 C0                        test rax, rax
00954E9B  74 0E                           je 0x140954eab
00954E9D  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00954EA1  66 89 10                        mov word ptr [rax], dx
00954EA4  49 8B 47 38                     mov rax, qword ptr [r15 + 0x38]
00954EA8  66 89 10                        mov word ptr [rax], dx
00954EAB  49 39 57 18                     cmp qword ptr [r15 + 0x18], rdx
00954EAF  75 04                           jne 0x140954eb5
00954EB1  84 C9                           test cl, cl
00954EB3  74 5A                           je 0x140954f0f
00954EB5  49 8B 4F 68                     mov rcx, qword ptr [r15 + 0x68]
00954EB9  41 B5 01                        mov r13b, 1
00954EBC  48 85 C9                        test rcx, rcx
00954EBF  74 0D                           je 0x140954ece
00954EC1  48 8B 49 08                     mov rcx, qword ptr [rcx + 8]
00954EC5  E8 A2 0C 00 00                  call 0x140955b6c
00954ECA  44 88 6D 7F                     mov byte ptr [rbp + 0x7f], r13b
00954ECE  BA 18 00 00 00                  mov edx, 0x18
00954ED3  41 B8 50 6E 70 59               mov r8d, 0x59706e50
00954ED9  8D 4A 28                        lea ecx, [rdx + 0x28]
00954EDC  E8 0F D2 22 00                  call 0x140b820f0
00954EE1  33 D2                           xor edx, edx
00954EE3  48 89 47 18                     mov qword ptr [rdi + 0x18], rax
00954EE7  48 85 C0                        test rax, rax
00954EEA  75 10                           jne 0x140954efc
00954EEC  44 8A E2                        mov r12b, dl
00954EEF  BE 9A 00 00 C0                  mov esi, 0xc000009a
00954EF4  44 8A F2                        mov r14b, dl
00954EF7  E9 04 03 00 00                  jmp 0x140955200
00954EFC  45 33 C0                        xor r8d, r8d
00954EFF  48 8B C8                        mov rcx, rax
00954F02  E8 09 8E AB FF                  call 0x14040dd10
00954F07  48 8B CF                        mov rcx, rdi
00954F0A  E8 2D C5 0C 00                  call 0x140a2143c
00954F0F  44 88 6F 4C                     mov byte ptr [rdi + 0x4c], r13b
00954F13  48 8D 4F 50                     lea rcx, [rdi + 0x50]
00954F17  41 8B 87 9C 00 00 00            mov eax, dword ptr [r15 + 0x9c]
00954F1E  49 8D 57 78                     lea rdx, [r15 + 0x78]
00954F22  83 C0 08                        add eax, 8
00954F25  89 47 48                        mov dword ptr [rdi + 0x48], eax
00954F28  45 8B 87 9C 00 00 00            mov r8d, dword ptr [r15 + 0x9c]
00954F2F  E8 0C 19 D7 FF                  call 0x1406c6840
00954F34  4D 85 F6                        test r14, r14
00954F37  74 20                           je 0x140954f59
00954F39  41 8B 8F 9C 00 00 00            mov ecx, dword ptr [r15 + 0x9c]
00954F40  4D 8B CE                        mov r9, r14
00954F43  48 83 C1 50                     add rcx, 0x50
00954F47  4D 8B C4                        mov r8, r12
00954F4A  48 03 CF                        add rcx, rdi
00954F4D  49 8B D6                        mov rdx, r14
00954F50  48 89 4F 40                     mov qword ptr [rdi + 0x40], rcx
00954F54  E8 43 C7 B1 FF                  call 0x14047169c
00954F59  48 8B CF                        mov rcx, rdi
00954F5C  E8 F7 74 0D 00                  call 0x140a2c458
00954F61  48 8D 0D 38 7B 63 00            lea rcx, [rip + 0x637b38]
00954F68  E8 33 96 8B FF                  call 0x14020e5a0
00954F6D  48 8B 05 14 7B 63 00            mov rax, qword ptr [rip + 0x637b14]
00954F74  48 8D 0D 05 7B 63 00            lea rcx, [rip + 0x637b05]
00954F7B  4C 8B 35 FE 7A 63 00            mov r14, qword ptr [rip + 0x637afe]
00954F82  48 39 08                        cmp qword ptr [rax], rcx
00954F85  0F 85 EA 02 00 00               jne 0x140955275
00954F8B  48 89 0F                        mov qword ptr [rdi], rcx
00954F8E  41 B4 01                        mov r12b, 1
00954F91  48 89 47 08                     mov qword ptr [rdi + 8], rax
00954F95  48 8D 0D 04 7B 63 00            lea rcx, [rip + 0x637b04]
00954F9C  48 89 38                        mov qword ptr [rax], rdi
00954F9F  48 89 3D E2 7A 63 00            mov qword ptr [rip + 0x637ae2], rdi
00954FA6  E8 15 CA 8F FF                  call 0x1402519c0
00954FAB  48 8D 05 CE 7A 63 00            lea rax, [rip + 0x637ace]
00954FB2  4C 3B F0                        cmp r14, rax
00954FB5  75 3D                           jne 0x140954ff4
00954FB7  BA 20 00 00 00                  mov edx, 0x20
00954FBC  41 B8 50 6E 70 59               mov r8d, 0x59706e50
00954FC2  8D 4A 20                        lea ecx, [rdx + 0x20]
00954FC5  E8 26 D1 22 00                  call 0x140b820f0
00954FCA  33 D2                           xor edx, edx
00954FCC  48 85 C0                        test rax, rax
00954FCF  0F 84 1A FF FF FF               je 0x140954eef
00954FD5  48 8D 0D 94 D8 06 00            lea rcx, [rip + 0x6d894]
00954FDC  48 89 10                        mov qword ptr [rax], rdx
00954FDF  48 89 48 10                     mov qword ptr [rax + 0x10], rcx
00954FE3  BA 03 00 00 00                  mov edx, 3
00954FE8  48 8B C8                        mov rcx, rax
00954FEB  48 89 40 18                     mov qword ptr [rax + 0x18], rax
00954FEF  E8 2C 45 9A FF                  call 0x1402f9520
00954FF4  33 D2                           xor edx, edx
00954FF6  45 8A F4                        mov r14b, r12b
00954FF9  45 84 ED                        test r13b, r13b
00954FFC  0F 84 FE 01 00 00               je 0x140955200
00955002  F6 05 23 B1 59 00 02            test byte ptr [rip + 0x59b123], 2
00955009  48 B9 14 00 00 00 80 F7 FF FF   movabs rcx, 0xfffff78000000014
00955013  74 03                           je 0x140955018
00955015  48 8B 19                        mov rbx, qword ptr [rcx]
00955018  48 89 54 24 38                  mov qword ptr [rsp + 0x38], rdx
0095501D  48 8D 05 BC 75 63 00            lea rax, [rip + 0x6375bc]
00955024  48 89 45 0F                     mov qword ptr [rbp + 0xf], rax
00955028  45 33 C9                        xor r9d, r9d
0095502B  48 8B 47 18                     mov rax, qword ptr [rdi + 0x18]
0095502F  48 89 45 17                     mov qword ptr [rbp + 0x17], rax
00955033  0F B7 05 D6 59 4B 00            movzx eax, word ptr [rip + 0x4b59d6]
0095503A  69 C0 F0 D8 FF FF               imul eax, eax, 0xffffd8f0
00955040  45 8D 41 01                     lea r8d, [r9 + 1]
00955044  41 8D 49 02                     lea ecx, [r9 + 2]
00955048  48 98                           cdqe
0095504A  48 89 45 07                     mov qword ptr [rbp + 7], rax
0095504E  48 8D 45 07                     lea rax, [rbp + 7]
00955052  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00955057  44 88 64 24 28                  mov byte ptr [rsp + 0x28], r12b
0095505C  88 54 24 20                     mov byte ptr [rsp + 0x20], dl
00955060  48 8D 55 0F                     lea rdx, [rbp + 0xf]
00955064  E8 A7 80 8B FF                  call 0x14020d110
00955069  8B F0                           mov esi, eax
0095506B  48 8D 55 EB                     lea rdx, [rbp - 0x15]
0095506F  33 C0                           xor eax, eax
00955071  48 8D 0D A0 92 6C FF            lea rcx, [rip - 0x936d60]
00955078  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
0095507C  45 33 C9                        xor r9d, r9d
0095507F  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
00955083  89 45 EB                        mov dword ptr [rbp - 0x15], eax
00955086  44 8D 40 04                     lea r8d, [rax + 4]
0095508A  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0095508F  E8 7C BC D5 FF                  call 0x1406b0d10
00955094  33 C9                           xor ecx, ecx
00955096  85 F6                           test esi, esi
00955098  75 0A                           jne 0x1409550a4
0095509A  BE 89 01 00 C0                  mov esi, 0xc0000189
0095509F  E9 30 01 00 00                  jmp 0x1409551d4
009550A4  83 FE 01                        cmp esi, 1
009550A7  0F 85 B9 00 00 00               jne 0x140955166
009550AD  38 4D 6F                        cmp byte ptr [rbp + 0x6f], cl
009550B0  74 0D                           je 0x1409550bf
009550B2  49 8B 47 30                     mov rax, qword ptr [r15 + 0x30]
009550B6  BE 20 01 00 C0                  mov esi, 0xc0000120
009550BB  39 08                           cmp dword ptr [rax], ecx
009550BD  75 02                           jne 0x1409550c1
009550BF  8B F1                           mov esi, ecx
009550C1  F6 05 64 B0 59 00 02            test byte ptr [rip + 0x59b064], 2
009550C8  0F 84 06 01 00 00               je 0x1409551d4
009550CE  48 B9 14 00 00 00 80 F7 FF FF   movabs rcx, 0xfffff78000000014
009550D8  48 B8 4B 59 86 38 D6 C5 6D 34   movabs rax, 0x346dc5d63886594b
009550E2  48 8B 09                        mov rcx, qword ptr [rcx]
009550E5  48 2B CB                        sub rcx, rbx
009550E8  48 F7 E9                        imul rcx
009550EB  48 8B DA                        mov rbx, rdx
009550EE  48 C1 FB 0B                     sar rbx, 0xb
009550F2  48 8B C3                        mov rax, rbx
009550F5  48 C1 E8 3F                     shr rax, 0x3f
009550F9  48 03 D8                        add rbx, rax
009550FC  0F B7 05 05 59 4B 00            movzx eax, word ptr [rip + 0x4b5905]
00955103  48 3B D8                        cmp rbx, rax
00955106  0F 8E C8 00 00 00               jle 0x1409551d4
0095510C  4C 8D 4D EF                     lea r9, [rbp - 0x11]
00955110  48 8B CF                        mov rcx, rdi
00955113  4C 8D 45 F7                     lea r8, [rbp - 9]
00955117  48 8D 55 FF                     lea rdx, [rbp - 1]
0095511B  E8 8C 9A 11 00                  call 0x140a6ebac
00955120  F6 05 05 B0 59 00 02            test byte ptr [rip + 0x59b005], 2
00955127  0F 84 A7 00 00 00               je 0x1409551d4
0095512D  48 8B 45 EF                     mov rax, qword ptr [rbp - 0x11]
00955131  4C 8D 4F 50                     lea r9, [rdi + 0x50]
00955135  48 89 5C 24 40                  mov qword ptr [rsp + 0x40], rbx
0095513A  48 8D 15 4F 1F 6D FF            lea rdx, [rip - 0x92e0b1]
00955141  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00955146  48 8B 45 F7                     mov rax, qword ptr [rbp - 9]
0095514A  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0095514F  48 8B 45 FF                     mov rax, qword ptr [rbp - 1]
00955153  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00955158  8B 47 60                        mov eax, dword ptr [rdi + 0x60]
0095515B  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
0095515F  E8 0C 21 C5 FF                  call 0x1405a7270
00955164  EB 6E                           jmp 0x1409551d4
00955166  81 FE 02 01 00 00               cmp esi, 0x102
0095516C  75 61                           jne 0x1409551cf
0095516E  F6 05 B7 AF 59 00 02            test byte ptr [rip + 0x59afb7], 2
00955175  74 54                           je 0x1409551cb
00955177  4C 8D 4D EF                     lea r9, [rbp - 0x11]
0095517B  48 8B CF                        mov rcx, rdi
0095517E  4C 8D 45 F7                     lea r8, [rbp - 9]
00955182  48 8D 55 FF                     lea rdx, [rbp - 1]
00955186  E8 21 9A 11 00                  call 0x140a6ebac
0095518B  0F B7 05 7E 58 4B 00            movzx eax, word ptr [rip + 0x4b587e]
00955192  4C 8D 4F 50                     lea r9, [rdi + 0x50]
00955196  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
0095519B  48 8D 15 1E 1C 6D FF            lea rdx, [rip - 0x92e3e2]
009551A2  48 8B 45 EF                     mov rax, qword ptr [rbp - 0x11]
009551A6  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
009551AB  48 8B 45 F7                     mov rax, qword ptr [rbp - 9]
009551AF  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
009551B4  48 8B 45 FF                     mov rax, qword ptr [rbp - 1]
009551B8  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009551BD  8B 47 60                        mov eax, dword ptr [rdi + 0x60]
009551C0  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
009551C4  E8 A7 20 C5 FF                  call 0x1405a7270
009551C9  33 C9                           xor ecx, ecx
009551CB  8B F1                           mov esi, ecx
009551CD  EB 05                           jmp 0x1409551d4
009551CF  BE 01 00 00 C0                  mov esi, 0xc0000001
009551D4  48 8D 0D C5 78 63 00            lea rcx, [rip + 0x6378c5]
009551DB  E8 C0 93 8B FF                  call 0x14020e5a0
009551E0  33 C0                           xor eax, eax
009551E2  48 8D 0D B7 78 63 00            lea rcx, [rip + 0x6378b7]
009551E9  48 89 47 20                     mov qword ptr [rdi + 0x20], rax
009551ED  48 89 47 28                     mov qword ptr [rdi + 0x28], rax
009551F1  E8 CA C7 8F FF                  call 0x1402519c0
009551F6  48 8B CF                        mov rcx, rdi
009551F9  E8 46 E0 06 00                  call 0x1409c3244
009551FE  33 D2                           xor edx, edx
00955200  38 55 7F                        cmp byte ptr [rbp + 0x7f], dl
00955203  74 0F                           je 0x140955214
00955205  49 8B 4F 68                     mov rcx, qword ptr [r15 + 0x68]
00955209  48 8B 49 08                     mov rcx, qword ptr [rcx + 8]
0095520D  E8 12 64 FA FF                  call 0x1408fb624
00955212  33 D2                           xor edx, edx
00955214  45 84 F6                        test r14b, r14b
00955217  0F 85 EA FA FF FF               jne 0x140954d07
0095521D  45 84 E4                        test r12b, r12b
00955220  74 33                           je 0x140955255
00955222  48 8D 0D 77 78 63 00            lea rcx, [rip + 0x637877]
00955229  E8 72 93 8B FF                  call 0x14020e5a0
0095522E  48 8B 17                        mov rdx, qword ptr [rdi]
00955231  48 39 7A 08                     cmp qword ptr [rdx + 8], rdi
00955235  75 3E                           jne 0x140955275
00955237  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
0095523B  48 39 38                        cmp qword ptr [rax], rdi
0095523E  75 35                           jne 0x140955275
00955240  48 89 10                        mov qword ptr [rax], rdx
00955243  48 8D 0D 56 78 63 00            lea rcx, [rip + 0x637856]
0095524A  48 89 42 08                     mov qword ptr [rdx + 8], rax
0095524E  E8 6D C7 8F FF                  call 0x1402519c0
00955253  33 D2                           xor edx, edx
00955255  45 84 ED                        test r13b, r13b
00955258  74 0E                           je 0x140955268
0095525A  48 39 57 18                     cmp qword ptr [rdi + 0x18], rdx
0095525E  74 08                           je 0x140955268
00955260  48 8B CF                        mov rcx, rdi
00955263  E8 DC DF 06 00                  call 0x1409c3244
00955268  48 8B CF                        mov rcx, rdi
0095526B  E8 34 E0 06 00                  call 0x1409c32a4
00955270  E9 92 FA FF FF                  jmp 0x140954d07
00955275  B9 03 00 00 00                  mov ecx, 3
0095527A  CD 29                           int 0x29
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiUEventNotifyUserMode(__int64 a1)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m5F;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned int v_stack_m74;
    unsigned __int8 v_stack_p10;
    unsigned __int8 v_stack_p20;
    unsigned __int8 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (144);
    v_rdi = 0;
    v_stack_m58 = 0;
    v_stack_p10 = 0;
    v_stack_m60 = 0;
    v_stack_m68 = 0;
    v_stack_m70 = 0;
    v_stack_p20 = 0;
    if ((*(unsigned int *)(v_rip + 6519049)) == 0) goto loc_00954D25;
loc_00954D07:
    v_rsp = (v_rsp) + (144);
    return (unsigned int)((unsigned int)((unsigned int)(0xC0000189ULL)));
loc_00954D25:
    if ((*(unsigned int *)(a1 + 136)) != 4) goto loc_00954D6F;
    result = PiUEventDeviceNeedsInstall(a1 + 168, v_stack_p10, a3, a4);
    a1 = 0;
    if (sign_flag) goto loc_00954D6D;
    if (v_stack_p10 == 0) goto loc_00954D6D;
    result = PpDevCfgRequestDeviceInstall(a1, v_stack_p10, a3, a4);
    if (sign_flag) goto loc_00954D6D;
    if (((*(unsigned __int8 *)(v_rip + 5878734)) & (16)) != 0) {
        a4 = a1 + 168;
        a2 = v_rip - 9661328;
        result = McTemplateK0z_EtwWriteTransfer(a1, a2, a3, a4);
    }
    v_rdi = 0;
loc_00954D6F:
    result = PiUEventShouldQueueEvent(0, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00954D07;
    result = PiUEventIsDeviceEventVetoable(0, a2, a3, a4);
    v_stack_p10 = (unsigned __int8)(result);
    result = Feature_KernelPnP_CheckDeviceInstancePath__private_IsEnabledDeviceUsageNoInline(0, a2, a3, a4);
    if (*(unsigned __int64 *)(a1 + 160) == 0) goto loc_00954DEE;
    if ((unsigned int)((unsigned int)((unsigned int)(result))) == 0) goto loc_00954DC9;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 160) + 312) + 40) == 0) goto loc_00954DEE;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 160) + 312) + 40) + 48) == 0) goto loc_00954DEE;
    v_r14 = (0) | (-1);
loc_00954DBD:
    v_r14 = (v_r14) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 160) + 312) + 40) + 48) + v_r14 * 2)) != 0) goto loc_00954DBD;
    goto loc_00954DEB;
loc_00954DC9:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 160) + 312) + 40) + 48) + 312) + 40) == 0) goto loc_00954DEE;
    v_r14 = (v_r14) | (-1);
loc_00954DE1:
    v_r14 = (v_r14) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 160) + 312) + 40) + 48) + 312) + 40) + 48) + v_r14 * 2)) != 0) goto loc_00954DE1;
loc_00954DEB:
    v_r14 = (v_r14) + 1;
loc_00954DEE:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 156))) + (80));
    v_stack_m74 = (unsigned int)(a1 + v_r14 * 2);
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(a1 + v_r14 * 2)), (unsigned int)(0x59706E50ULL), a4);
    if (result != 0) goto loc_00954E23;
    goto loc_00954D07;
loc_00954E23:
    result = ExAllocatePool2(56 + 8, 56, (unsigned int)(0x59706E50ULL), a4);
    *(unsigned __int64 *)(result + 16) = result;
    if (result != 0) goto loc_00954E49;
    goto loc_00955268;
loc_00954E49:
    result = KeInitializeGuardedMutex(result, 56, (unsigned int)(0x59706E50ULL), a4);
    a2 = 0;
    *(unsigned __int8 *)(result + 77) = (unsigned __int8)(v_stack_p10);
    *(unsigned int *)(result + 56) = 1;
    if ((unsigned __int8)(v_stack_p10) == 0) goto loc_00954E8D;
    *(unsigned __int64 *)(result + 32) = *(unsigned __int64 *)(a1 + 48);
    *(unsigned __int64 *)(result + 40) = *(unsigned __int64 *)(a1 + 56);
    *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 56) + 8)) = 0;
    *(unsigned __int16 *)(*(unsigned __int64 *)(result + 40)) = 0;
    *(unsigned int *)(*(unsigned __int64 *)(result + 32)) = 0;
    goto loc_00954EAB;
loc_00954E8D:
    if (*(unsigned __int64 *)(result + 32) != 0) {
        *(unsigned int *)(*(unsigned __int64 *)(result + 32)) = 0;
    }
    result = *(unsigned __int64 *)(a1 + 56);
    if (*(unsigned __int64 *)(a1 + 56) != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 56) + 8);
        *(unsigned __int16 *)(result) = 0;
        result = *(unsigned __int64 *)(a1 + 56);
        *(unsigned __int16 *)(result) = 0;
    }
    if ((*(unsigned __int64 *)(a1 + 24)) != 0) goto loc_00954EB5;
    if ((unsigned __int8)(v_stack_p10) == 0) goto loc_00954F0F;
loc_00954EB5:
    if (*(unsigned __int64 *)(a1 + 104) != 0) {
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 104) + 8);
        result = PnpWatchdogTimerPause(a1, a2, (unsigned int)(0x59706E50ULL), a4);
        v_stack_p20 = 1;
    }
    result = ExAllocatePool2(24 + 40, 24, (unsigned int)(0x59706E50ULL), a4);
    a2 = 0;
    *(unsigned __int64 *)(result + 24) = result;
    if (result != 0) goto loc_00954EFC;
loc_00954EEF:
    goto loc_00955200;
loc_00954EFC:
    a3 = 0;
    result = KeInitializeEvent(result, a2, a3, a4);
    result = PiUEventReferenceEventEntry(result, a2, a3, a4);
loc_00954F0F:
    *(unsigned __int8 *)(result + 76) = 1;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 156))) + (8));
    *(unsigned int *)(result + 72) = (unsigned int)(result);
    result = memcpy(result + 80, a1 + 120, (unsigned int)(*(unsigned int *)(a1 + 156)), a4);
    if (0 != 0) {
        a1 = *(unsigned int *)(a1 + 156);
        a4 = 0;
        a1 = (a1) + (80);
        a3 = 0;
        a1 = (a1) + (result);
        a2 = 0;
        *(unsigned __int64 *)(result + 64) = a1;
        result = RtlStringCchCopyNW(a1, a2, a3, a4);
    }
    result = PiUEventCacheObjectProperties(result, a2, a3, a4);
    result = ExAcquireFastMutex(v_rip + 6519608, a2, a3, a4);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6519572))) != (v_rip + 6519557)) goto loc_00955275;
    *(unsigned __int64 *)(result) = v_rip + 6519557;
    *(unsigned __int64 *)(result + 8) = *(unsigned __int64 *)(v_rip + 6519572);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6519572)) = result;
    *(unsigned __int64 *)(v_rip + 6519522) = result;
    result = ExReleaseFastMutex(v_rip + 6519556, a2, a3, a4);
    if ((*(unsigned __int64 *)(v_rip + 6519550)) != (v_rip + 6519502)) goto loc_00954FF4;
    result = ExAllocatePool2(32 + 32, 32, (unsigned int)(0x59706E50ULL), a4);
    a2 = 0;
    if (result == 0) goto loc_00954EEF;
    *(unsigned __int64 *)(result) = 0;
    *(unsigned __int64 *)(result + 16) = v_rip + 448660;
    *(unsigned __int64 *)(result + 24) = result;
    result = ExQueueWorkItem(result, 3, (unsigned int)(0x59706E50ULL), a4);
loc_00954FF4:
    a2 = 0;
    if (1 == 0) goto loc_00955200;
    v_rbx = v_stack_p8;
    if (((*(unsigned __int8 *)(v_rip + 5878051)) & (2)) != 0) {
        v_rbx = *(unsigned __int64 *)(result);
    }
    v_stack_p38 = 0;
    v_stack_m50 = v_rip + 6518204;
    a4 = 0;
    v_stack_m48 = *(unsigned __int64 *)(result + 24);
    result = (unsigned int)((*(unsigned __int16 *)(v_rip + 4938198)) * ((unsigned int)(*(unsigned __int16 *)(v_rip + 4938198))));
    v_stack_m58 = result;
    v_stack_p30 = v_stack_m58;
    v_stack_p28 = 1;
    v_stack_p20 = 0;
    result = KeWaitForMultipleObjects(a4 + 2, v_stack_m50, a4 + 1, a4);
    result = 0;
    v_stack_p30 = 0;
    a4 = 0;
    v_stack_p28 = 0;
    v_stack_m74 = 0;
    v_stack_p20 = 0;
    result = ZwUpdateWnfStateData(v_rip - 9661792, v_stack_m74, result + 4, a4);
    a1 = 0;
    if ((unsigned int)((unsigned int)((unsigned int)(result))) != 0) goto loc_009550A4;
    goto loc_009551D4;
loc_009550A4:
    if (((unsigned int)((unsigned int)(0xC0000189ULL))) != 1) goto loc_00955166;
    if (v_stack_p10 == 0) goto loc_009550BF;
    v_rsi = (unsigned int)(0xC0000120ULL);
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 48))) == 0) {
        v_rsi = 0;
    }
    if (((*(unsigned __int8 *)(v_rip + 5877860)) & (2)) == 0) goto loc_009551D4;
    a1 = (*(unsigned __int64 *)(a1)) - (v_rbx);
    v_rbx = (v_stack_m74) >> (11);
    result = (v_rbx) >> (63);
    v_rbx = (v_rbx) + (result);
    if (v_rbx <= (*(unsigned __int16 *)(v_rip + 4937989))) goto loc_009551D4;
    result = PiUEventGatherEventData(result, v_stack_m60, v_stack_m68, v_stack_m70);
    if (((*(unsigned __int8 *)(v_rip + 5877765)) & (2)) == 0) goto loc_009551D4;
    v_stack_p40 = v_rbx;
    v_stack_p38 = v_stack_m70;
    v_stack_p30 = v_stack_m68;
    v_stack_p28 = v_stack_m60;
    v_stack_p20 = (unsigned int)((unsigned int)(*(unsigned int *)(result + 96)));
    result = McTemplateK0jqzjzx_EtwWriteTransfer(result, v_rip - 9625777, v_stack_m68, result + 80);
    goto loc_009551D4;
loc_00955166:
    if (((unsigned int)(v_rsi)) != 258) goto loc_009551CF;
    if (((*(unsigned __int8 *)(v_rip + 5877687)) & (2)) != 0) {
        a4 = v_stack_m70;
        a1 = result;
        a3 = v_stack_m68;
        a2 = v_stack_m60;
        result = PiUEventGatherEventData(a1, a2, a3, a4);
        result = *(unsigned __int16 *)(v_rip + 4937854);
        a4 = result + 80;
        v_stack_p40 = result;
        a2 = v_rip - 9626594;
        result = v_stack_m70;
        v_stack_p38 = result;
        result = v_stack_m68;
        v_stack_p30 = result;
        result = v_stack_m60;
        v_stack_p28 = result;
        result = *(unsigned int *)(result + 96);
        v_stack_p20 = (unsigned int)(result);
        result = McTemplateK0jqzjzx_EtwWriteTransfer(a1, a2, a3, a4);
        a1 = 0;
    }
    goto loc_009551D4;
loc_009551CF:
loc_009551D4:
    result = ExAcquireFastMutex(v_rip + 6518981, a2, a3, a4);
    result = 0;
    *(unsigned __int64 *)(result + 32) = 0;
    *(unsigned __int64 *)(result + 40) = 0;
    result = ExReleaseFastMutex(v_rip + 6518967, a2, a3, a4);
    result = PiUEventDereferenceEventEntry(result, a2, a3, a4);
    a2 = 0;
loc_00955200:
    if (v_stack_p20 != 0) {
        a1 = *(unsigned __int64 *)(a1 + 104);
        a1 = *(unsigned __int64 *)(a1 + 8);
        result = PnpWatchdogTimerStart(a1, a2, a3, a4);
        a2 = 0;
    }
    if (1 != 0) goto loc_00954D07;
    if (1 == 0) goto loc_00955255;
    result = ExAcquireFastMutex(v_rip + 6518903, a2, a3, a4);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result) + 8)) != result) goto loc_00955275;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8))) != result) goto loc_00955275;
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 8)) = *(unsigned __int64 *)(result);
    *(unsigned __int64 *)(*(unsigned __int64 *)(result) + 8) = *(unsigned __int64 *)(result + 8);
    result = ExReleaseFastMutex(v_rip + 6518870, *(unsigned __int64 *)(result), a3, a4);
    a2 = 0;
loc_00955255:
    if (1 == 0) goto loc_00955268;
    if ((*(unsigned __int64 *)(result + 24)) != 0) {
        a1 = result;
        result = PiUEventDereferenceEventEntry(a1, a2, a3, a4);
    }
    result = PiUEventFreeEventEntry(result, a2, a3, a4);
    goto loc_00954D07;
loc_00955275:
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PiUEventNotifyUserMode(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m5F;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint32_t v_stack_m74;
    uint8_t v_stack_p10;
    uint8_t v_stack_p20;
    uint8_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (144);
    local_rdi = 0;
    v_stack_m58 = 0;
    v_stack_p10 = 0;
    v_stack_m60 = 0;
    v_stack_m68 = 0;
    v_stack_m70 = 0;
    v_stack_p20 = 0;
    if ((*(uint32_t *)(v_rip + 0x637909)) == 0) goto loc_00954D25;
loc_00954D07:
    local_rsp = (local_rsp) + (144);
    return (uint32_t)((uint32_t)((uint32_t)(0xC0000189ULL)));
loc_00954D25:
    if ((*(uint32_t *)(arg1 + 0x88)) != 4) goto loc_00954D6F;
    result = PiUEventDeviceNeedsInstall(Arg1 + 168, v_stack_p10, a3, a4);
    Arg1 = 0;
    if (sign_flag) goto loc_00954D6D;
    if (v_stack_p10 == 0) goto loc_00954D6D;
    result = PpDevCfgRequestDeviceInstall(Arg1, v_stack_p10, a3, a4);
    if (sign_flag) goto loc_00954D6D;
    if (((*(uint8_t *)(v_rip + 0x59B3CE)) & (16)) != 0) {
        a4 = Arg1 + 168;
        a2 = v_rip - 9661328;
        result = McTemplateK0z_EtwWriteTransfer(Arg1, a2, a3, a4);
    }
    local_rdi = 0;
loc_00954D6F:
    result = PiUEventShouldQueueEvent(0, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00954D07;
    result = PiUEventIsDeviceEventVetoable(0, a2, a3, a4);
    v_stack_p10 = (uint8_t)(result);
    result = Feature_KernelPnP_CheckDeviceInstancePath__private_IsEnabledDeviceUsageNoInline(0, a2, a3, a4);
    if (*(uint64_t *)(arg1 + 0xA0) == 0) goto loc_00954DEE;
    if ((uint32_t)((uint32_t)((uint32_t)(result))) == 0) goto loc_00954DC9;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xA0) + 0x138) + 0x28) == 0) goto loc_00954DEE;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xA0) + 0x138) + 0x28) + 0x30) == 0) goto loc_00954DEE;
    local_r14 = (0) | (-1);
loc_00954DBD:
    local_r14 = (local_r14) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xA0) + 0x138) + 0x28) + 0x30) + local_r14 * 2)) != 0) goto loc_00954DBD;
    goto loc_00954DEB;
loc_00954DC9:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xA0) + 0x138) + 0x28) + 0x30) + 0x138) + 0x28) == 0) goto loc_00954DEE;
    local_r14 = (local_r14) | (-1);
loc_00954DE1:
    local_r14 = (local_r14) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xA0) + 0x138) + 0x28) + 0x30) + 0x138) + 0x28) + 0x30) + local_r14 * 2)) != 0) goto loc_00954DE1;
loc_00954DEB:
    local_r14 = (local_r14) + 1;
loc_00954DEE:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x9C))) + (80));
    v_stack_m74 = (uint32_t)(Arg1 + local_r14 * 2);
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(Arg1 + local_r14 * 2)), (uint32_t)(0x59706E50ULL), a4);
    if (result != 0) goto loc_00954E23;
    goto loc_00954D07;
loc_00954E23:
    result = ExAllocatePool2(56 + 8, 56, (uint32_t)(0x59706E50ULL), a4);
    *(uint64_t *)(result + 0x10) = result;
    if (result != 0) goto loc_00954E49;
    goto loc_00955268;
loc_00954E49:
    result = KeInitializeGuardedMutex(result, 56, (uint32_t)(0x59706E50ULL), a4);
    a2 = 0;
    *(uint8_t *)(result + 0x4D) = (uint8_t)(v_stack_p10);
    *(uint32_t *)(result + 0x38) = 1;
    if ((uint8_t)(v_stack_p10) == 0) goto loc_00954E8D;
    *(uint64_t *)(result + 0x20) = *(uint64_t *)(arg1 + 0x30);
    *(uint64_t *)(result + 0x28) = *(uint64_t *)(arg1 + 0x38);
    *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x38) + 0x8)) = 0;
    *(uint16_t *)(*(uint64_t *)(result + 0x28)) = 0;
    *(uint32_t *)(*(uint64_t *)(result + 0x20)) = 0;
    goto loc_00954EAB;
loc_00954E8D:
    if (*(uint64_t *)(result + 0x20) != 0) {
        *(uint32_t *)(*(uint64_t *)(result + 0x20)) = 0;
    }
    result = *(uint64_t *)(arg1 + 0x38);
    if (*(uint64_t *)(arg1 + 0x38) != 0) {
        result = *(uint64_t *)(*(uint64_t *)(arg1 + 0x38) + 0x8);
        *(uint16_t *)(result) = 0;
        result = *(uint64_t *)(arg1 + 0x38);
        *(uint16_t *)(result) = 0;
    }
    if ((*(uint64_t *)(arg1 + 0x18)) != 0) goto loc_00954EB5;
    if ((uint8_t)(v_stack_p10) == 0) goto loc_00954F0F;
loc_00954EB5:
    if (*(uint64_t *)(arg1 + 0x68) != 0) {
        Arg1 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x68) + 0x8);
        result = PnpWatchdogTimerPause(Arg1, a2, (uint32_t)(0x59706E50ULL), a4);
        v_stack_p20 = 1;
    }
    result = ExAllocatePool2(24 + 40, 24, (uint32_t)(0x59706E50ULL), a4);
    a2 = 0;
    *(uint64_t *)(result + 0x18) = result;
    if (result != 0) goto loc_00954EFC;
loc_00954EEF:
    goto loc_00955200;
loc_00954EFC:
    a3 = 0;
    result = KeInitializeEvent(result, a2, a3, a4);
    result = PiUEventReferenceEventEntry(result, a2, a3, a4);
loc_00954F0F:
    *(uint8_t *)(result + 0x4C) = 1;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x9C))) + (8));
    *(uint32_t *)(result + 0x48) = (uint32_t)(result);
    result = memcpy(result + 80, Arg1 + 120, (uint32_t)(*(uint32_t *)(arg1 + 0x9C)), a4);
    if (0 != 0) {
        Arg1 = *(uint32_t *)(arg1 + 0x9C);
        a4 = 0;
        Arg1 = (Arg1) + (80);
        a3 = 0;
        Arg1 = (Arg1) + (result);
        a2 = 0;
        *(void **)(result + 0x40) = Arg1;
        result = RtlStringCchCopyNW(Arg1, a2, a3, a4);
    }
    result = PiUEventCacheObjectProperties(result, a2, a3, a4);
    result = ExAcquireFastMutex(v_rip + 6519608, a2, a3, a4);
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x637B14))) != (v_rip + 6519557)) goto loc_00955275;
    *(uint64_t *)(result) = v_rip + 6519557;
    *(uint64_t *)(result + 0x8) = *(uint64_t *)(v_rip + 0x637B14);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x637B14)) = result;
    *(uint64_t *)(v_rip + 0x637AE2) = result;
    result = ExReleaseFastMutex(v_rip + 6519556, a2, a3, a4);
    if ((*(uint64_t *)(v_rip + 0x637AFE)) != (v_rip + 6519502)) goto loc_00954FF4;
    result = ExAllocatePool2(32 + 32, 32, (uint32_t)(0x59706E50ULL), a4);
    a2 = 0;
    if (result == 0) goto loc_00954EEF;
    *(uint64_t *)(result) = 0;
    *(uint64_t *)(result + 0x10) = v_rip + 448660;
    *(uint64_t *)(result + 0x18) = result;
    result = ExQueueWorkItem(result, 3, (uint32_t)(0x59706E50ULL), a4);
loc_00954FF4:
    a2 = 0;
    if (1 == 0) goto loc_00955200;
    local_rbx = v_stack_p8;
    if (((*(uint8_t *)(v_rip + 0x59B123)) & (2)) != 0) {
        local_rbx = *(uint64_t *)(result);
    }
    v_stack_p38 = 0;
    v_stack_m50 = v_rip + 6518204;
    a4 = 0;
    v_stack_m48 = *(uint64_t *)(result + 0x18);
    result = (uint32_t)((*(uint16_t *)(v_rip + 0x4B59D6)) * ((uint32_t)(*(uint16_t *)(v_rip + 0x4B59D6))));
    v_stack_m58 = result;
    v_stack_p30 = v_stack_m58;
    v_stack_p28 = 1;
    v_stack_p20 = 0;
    result = KeWaitForMultipleObjects(a4 + 2, v_stack_m50, a4 + 1, a4);
    result = 0;
    v_stack_p30 = 0;
    a4 = 0;
    v_stack_p28 = 0;
    v_stack_m74 = 0;
    v_stack_p20 = 0;
    result = ZwUpdateWnfStateData(v_rip - 9661792, v_stack_m74, result + 4, a4);
    Arg1 = 0;
    if ((uint32_t)((uint32_t)((uint32_t)(result))) != 0) goto loc_009550A4;
    goto loc_009551D4;
loc_009550A4:
    if (((uint32_t)((uint32_t)(0xC0000189ULL))) != 1) goto loc_00955166;
    if (v_stack_p10 == 0) goto loc_009550BF;
    local_rsi = (uint32_t)(0xC0000120ULL);
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0x30))) == 0) {
        local_rsi = 0;
    }
    if (((*(uint8_t *)(v_rip + 0x59B064)) & (2)) == 0) goto loc_009551D4;
    Arg1 = (*(uint64_t *)(arg1)) - (local_rbx);
    local_rbx = (v_stack_m74) >> (11);
    result = (local_rbx) >> (63);
    local_rbx = (local_rbx) + (result);
    if (local_rbx <= (*(uint16_t *)(v_rip + 0x4B5905))) goto loc_009551D4;
    result = PiUEventGatherEventData(result, v_stack_m60, v_stack_m68, v_stack_m70);
    if (((*(uint8_t *)(v_rip + 0x59B005)) & (2)) == 0) goto loc_009551D4;
    v_stack_p40 = local_rbx;
    v_stack_p38 = v_stack_m70;
    v_stack_p30 = v_stack_m68;
    v_stack_p28 = v_stack_m60;
    v_stack_p20 = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x60)));
    result = McTemplateK0jqzjzx_EtwWriteTransfer(result, v_rip - 9625777, v_stack_m68, result + 80);
    goto loc_009551D4;
loc_00955166:
    if (((uint32_t)(local_rsi)) != 258) goto loc_009551CF;
    if (((*(uint8_t *)(v_rip + 0x59AFB7)) & (2)) != 0) {
        a4 = v_stack_m70;
        Arg1 = result;
        a3 = v_stack_m68;
        a2 = v_stack_m60;
        result = PiUEventGatherEventData(Arg1, a2, a3, a4);
        result = *(uint16_t *)(v_rip + 0x4B587E);
        a4 = result + 80;
        v_stack_p40 = result;
        a2 = v_rip - 9626594;
        result = v_stack_m70;
        v_stack_p38 = result;
        result = v_stack_m68;
        v_stack_p30 = result;
        result = v_stack_m60;
        v_stack_p28 = result;
        result = *(uint32_t *)(result + 0x60);
        v_stack_p20 = (uint32_t)(result);
        result = McTemplateK0jqzjzx_EtwWriteTransfer(Arg1, a2, a3, a4);
        Arg1 = 0;
    }
    goto loc_009551D4;
loc_009551CF:
loc_009551D4:
    result = ExAcquireFastMutex(v_rip + 6518981, a2, a3, a4);
    result = 0;
    *(uint64_t *)(result + 0x20) = 0;
    *(uint64_t *)(result + 0x28) = 0;
    result = ExReleaseFastMutex(v_rip + 6518967, a2, a3, a4);
    result = PiUEventDereferenceEventEntry(result, a2, a3, a4);
    a2 = 0;
loc_00955200:
    if (v_stack_p20 != 0) {
        Arg1 = *(uint64_t *)(arg1 + 0x68);
        Arg1 = *(uint64_t *)(arg1 + 0x8);
        result = PnpWatchdogTimerStart(Arg1, a2, a3, a4);
        a2 = 0;
    }
    if (1 != 0) goto loc_00954D07;
    if (1 == 0) goto loc_00955255;
    result = ExAcquireFastMutex(v_rip + 6518903, a2, a3, a4);
    if ((*(uint64_t *)(*(uint64_t *)(result) + 0x8)) != result) goto loc_00955275;
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x8))) != result) goto loc_00955275;
    *(uint64_t *)(*(uint64_t *)(result + 0x8)) = *(uint64_t *)(result);
    *(uint64_t *)(*(uint64_t *)(result) + 0x8) = *(uint64_t *)(result + 0x8);
    result = ExReleaseFastMutex(v_rip + 6518870, *(uint64_t *)(result), a3, a4);
    a2 = 0;
loc_00955255:
    if (1 == 0) goto loc_00955268;
    if ((*(uint64_t *)(result + 0x18)) != 0) {
        Arg1 = result;
        result = PiUEventDereferenceEventEntry(Arg1, a2, a3, a4);
    }
    result = PiUEventFreeEventEntry(result, a2, a3, a4);
    goto loc_00954D07;
loc_00955275:
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0x38` | `64` | `R` |
| `Arg1` | `+ 0x68` | `64` | `R` |
| `Arg1` | `+ 0x78` | `64` | `R` |
| `Arg1` | `+ 0x88` | `32` | `R` |
| `Arg1` | `+ 0x9C` | `32` | `R` |
| `Arg1` | `+ 0xA0` | `64` | `R` |
| `Arg1` | `+ 0xA8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00954CB4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
