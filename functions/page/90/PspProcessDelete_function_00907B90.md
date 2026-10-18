# PspProcessDelete

- RVA: `0x00907B90`–`0x00908162` (길이 `1,490` bytes)
- VA: `0x0000000140907B90`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00088E18`
- 디코드: `331`개 명령, `1,490/1,490` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **47**; 고유 호출 대상: **42**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **13**

### Outgoing calls
- `0x00907C09` → [PspLockProcessListExclusive](../../text/22/PspLockProcessListExclusive_function_0022578C.md) (function, `0x0022578C`)
- `0x00907C31` → [PspUnlockProcessListExclusive](../../text/2D/PspUnlockProcessListExclusive_function_002DFD18.md) (function, `0x002DFD18`)
- `0x00907C44` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00907C53` → [ObClearProcessDeviceMap](ObClearProcessDeviceMap_function_00907688.md) (function, `0x00907688`)
- `0x00907C88` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00907CA4` → [PsGetProcessId](../../text/43/PsGetProcessId_function_0043D910.md) (function, `0x0043D910`)
- `0x00907CAC` → [sub_00907768](Unknown_function_00907768.md) (function, `0x00907768`)
- `0x00907CCB` → [KiStackAttachProcess](../../text/21/KiStackAttachProcess_function_00216820.md) (function, `0x00216820`)
- `0x00907D06` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (function, `0x00217D30`)
- `0x00907D0E` → [MmDeleteProcessAddressSpace](../AC/MmDeleteProcessAddressSpace_function_00AC804C.md) (function, `0x00AC804C`)
- `0x00907D1F` → [PspReleaseReferenceToSession](../A9/PspReleaseReferenceToSession_function_00A9E444.md) (function, `0x00A9E444`)
- `0x00907D3B` → [PspRemoveProcessFromJobChain](PspRemoveProcessFromJobChain_function_00907288.md) (function, `0x00907288`)
- `0x00907D4C` → [ObDereferenceObjectDeferDeleteWithTag](../../text/26/ObDereferenceObjectDeferDeleteWithTag_function_00263EA0.md) (function, `0x00263EA0`)
- `0x00907D9A` → [ExMapHandleToPointer](../86/ExMapHandleToPointer_function_00868B60.md) (function, `0x00868B60`)
- `0x00907DB9` → [ExDestroyHandle](../88/ExDestroyHandle_function_00889430.md) (function, `0x00889430`)
- `0x00907DD6` → [KiCheckForKernelApcDelivery](../../text/2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (function, `0x002E2C80`)
- `0x00907DE7` → [SeDeassignPrimaryToken](SeDeassignPrimaryToken_function_009075C0.md) (function, `0x009075C0`)
- `0x00907E28` → [SmProcessDeleteNotification](../A6/SmProcessDeleteNotification_function_00A686F4.md) (function, `0x00A686F4`)
- `0x00907E38` → [PsDereferencePartition](../../text/34/PsDereferencePartition_function_00342E70.md) (function, `0x00342E70`)
- `0x00907E40` → [EtwExitProcess](EtwExitProcess_function_00907600.md) (function, `0x00907600`)
- `0x00907E48` → [LpcExitProcess](LpcExitProcess_function_00907920.md) (function, `0x00907920`)
- `0x00907E72` → [ExpWnfDeleteProcessContext](ExpWnfDeleteProcessContext_function_00908270.md) (function, `0x00908270`)
- `0x00907E87` → [ExpWnfDeleteScopeById](ExpWnfDeleteScopeById_function_00908168.md) (function, `0x00908168`)
- `0x00907E8C` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00907E96` → [IoSetDiskIoAttributionOnProcess](../../text/49/IoSetDiskIoAttributionOnProcess_function_0049521C.md) (function, `0x0049521C`)
- `0x00907E9E` → [PoEnergyContextCleanup](PoEnergyContextCleanup_function_00907A38.md) (function, `0x00907A38`)
- `0x00907F45` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00907F4F` → [ZwDeleteWnfStateName](../../text/6A/ZwDeleteWnfStateName_function_006AECF0.md) (function, `0x006AECF0`)
- `0x00907F5C` → [SmCompressionProcessHoldsPartitionReference](../../text/4F/SmCompressionProcessHoldsPartitionReference_function_004F7DA0.md) (function, `0x004F7DA0`)
- `0x00907F73` → [KeBugCheck](../../text/4F/KeBugCheck_function_004FD640.md) (function, `0x004FD640`)
- `0x00907F85` → [PspDereferenceQuota](PspDereferenceQuota_function_009075A4.md) (function, `0x009075A4`)
- `0x00907FA1` → [ExSaFree](../../text/43/ExSaFree_function_0043FACC.md) (function, `0x0043FACC`)
- `0x00907FA9` → [KiRemoveAndFreeCpuPartitionAssignmentProcess](../../text/43/KiRemoveAndFreeCpuPartitionAssignmentProcess_function_0043F8C0.md) (function, `0x0043F8C0`)
- `0x00907FBE` → [KiRundownAvailableCpusWorkItem](../../text/43/KiRundownAvailableCpusWorkItem_function_0043FA78.md) (function, `0x0043FA78`)
- `0x00907FD1` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00907FE5` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x0090802E` → [KeInitializeDpc](../../text/45/KeInitializeDpc_function_0045BBD0.md) (function, `0x0045BBD0`)
- `0x00908046` → [KeInsertQueueDpc](../../text/20/KeInsertQueueDpc_function_00207C50.md) (function, `0x00207C50`)
- `0x009080EC` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x009080F2` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00908106` → [PspDetachProcessFromSyscallProvider](../77/PspDetachProcessFromSyscallProvider_function_0077E4BC.md) (function, `0x0077E4BC`)
- `0x0090811A` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00908127` → [KeUnsecureProcess](../../text/5B/KeUnsecureProcess_function_005B9960.md) (function, `0x005B9960`)
- `0x00908133` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00908140` → [PsReturnProcessNonPagedPoolQuota](../../text/41/PsReturnProcessNonPagedPoolQuota_function_0041C200.md) (function, `0x0041C200`)
- `0x0090814A` → [VmpProcessContextCleanup](../7A/VmpProcessContextCleanup_function_007ADDAC.md) (function, `0x007ADDAC`)
- `0x00908158` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00907BAF` → RVA `0x00E0A740` (`.data`; read)
- `0x00907D5F` → RVA `0x00FC6C08` (`ALMOSTRO`; read)
- `0x00907D93` → RVA `0x00FC6CA8` (`ALMOSTRO`; read)
- `0x00907EE0` → RVA `0x00E62650` (`.data`; read)
- `0x00907EF1` → RVA `0x012018C0` (`CFGRO`; read)
- `0x00907F02` → RVA `0x00E62640` (`.data`; read)
- `0x00907F0D` → RVA `0x00E62648` (`.data`; read)
- `0x00908011` → RVA `0x0069BEC0` (`KiSchedulerDpc`; read)
- `0x00908018` → RVA `0x00E625E8` (`.data`; read)
- `0x0090801F` → RVA `0x00E625D0` (`.data`; read)
- `0x00908036` → RVA `0x00E62638` (`.data`; write)
- `0x009080A3` → RVA `0x00E62650` (`.data`; write)
- `0x00908110` → RVA `0x00F06538` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **30**
  - `0x00907C09` → [PspLockProcessListExclusive](../../text/22/PspLockProcessListExclusive_function_0022578C.md) (`PAGE` → `.text`)
  - `0x00907C31` → [PspUnlockProcessListExclusive](../../text/2D/PspUnlockProcessListExclusive_function_002DFD18.md) (`PAGE` → `.text`)
  - `0x00907C44` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00907C88` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00907CA4` → [PsGetProcessId](../../text/43/PsGetProcessId_function_0043D910.md) (`PAGE` → `.text`)
  - `0x00907CCB` → [KiStackAttachProcess](../../text/21/KiStackAttachProcess_function_00216820.md) (`PAGE` → `.text`)
  - `0x00907D06` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (`PAGE` → `.text`)
  - `0x00907D4C` → [ObDereferenceObjectDeferDeleteWithTag](../../text/26/ObDereferenceObjectDeferDeleteWithTag_function_00263EA0.md) (`PAGE` → `.text`)
  - `0x00907DD6` → [KiCheckForKernelApcDelivery](../../text/2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (`PAGE` → `.text`)
  - `0x00907E38` → [PsDereferencePartition](../../text/34/PsDereferencePartition_function_00342E70.md) (`PAGE` → `.text`)
  - `0x00907E8C` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00907E96` → [IoSetDiskIoAttributionOnProcess](../../text/49/IoSetDiskIoAttributionOnProcess_function_0049521C.md) (`PAGE` → `.text`)
  - `0x00907F45` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00907F4F` → [ZwDeleteWnfStateName](../../text/6A/ZwDeleteWnfStateName_function_006AECF0.md) (`PAGE` → `.text`)
  - `0x00907F5C` → [SmCompressionProcessHoldsPartitionReference](../../text/4F/SmCompressionProcessHoldsPartitionReference_function_004F7DA0.md) (`PAGE` → `.text`)
  - `0x00907F73` → [KeBugCheck](../../text/4F/KeBugCheck_function_004FD640.md) (`PAGE` → `.text`)
  - `0x00907FA1` → [ExSaFree](../../text/43/ExSaFree_function_0043FACC.md) (`PAGE` → `.text`)
  - `0x00907FA9` → [KiRemoveAndFreeCpuPartitionAssignmentProcess](../../text/43/KiRemoveAndFreeCpuPartitionAssignmentProcess_function_0043F8C0.md) (`PAGE` → `.text`)
  - `0x00907FBE` → [KiRundownAvailableCpusWorkItem](../../text/43/KiRundownAvailableCpusWorkItem_function_0043FA78.md) (`PAGE` → `.text`)
  - `0x00907FD1` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00907FE5` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x0090802E` → [KeInitializeDpc](../../text/45/KeInitializeDpc_function_0045BBD0.md) (`PAGE` → `.text`)
  - `0x00908046` → [KeInsertQueueDpc](../../text/20/KeInsertQueueDpc_function_00207C50.md) (`PAGE` → `.text`)
  - `0x009080EC` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x009080F2` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x0090811A` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00908127` → [KeUnsecureProcess](../../text/5B/KeUnsecureProcess_function_005B9960.md) (`PAGE` → `.text`)
  - `0x00908133` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00908140` → [PsReturnProcessNonPagedPoolQuota](../../text/41/PsReturnProcessNonPagedPoolQuota_function_0041C200.md) (`PAGE` → `.text`)
  - `0x00908158` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x00907F31` → [sub_00B21032](../B2/Unknown_function_00B21032.md) (`tail-transfer`)
  - `0x00907F37` → [sub_00B21032 + 0x15](../B2/Unknown_function_00B21032.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00907B90  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00907B95  48 89 6C 24 18                  mov qword ptr [rsp + 0x18], rbp
00907B9A  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00907B9F  57                              push rdi
00907BA0  41 54                           push r12
00907BA2  41 55                           push r13
00907BA4  41 56                           push r14
00907BA6  41 57                           push r15
00907BA8  48 81 EC 80 00 00 00            sub rsp, 0x80
00907BAF  48 8B 05 8A 2B 50 00            mov rax, qword ptr [rip + 0x502b8a]
00907BB6  48 33 C4                        xor rax, rsp
00907BB9  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
00907BBE  8B 81 FC 05 00 00               mov eax, dword ptr [rcx + 0x5fc]
00907BC4  0F 57 C0                        xorps xmm0, xmm0
00907BC7  45 33 FF                        xor r15d, r15d
00907BCA  48 8B D9                        mov rbx, rcx
00907BCD  0F 11 44 24 48                  movups xmmword ptr [rsp + 0x48], xmm0
00907BD2  0F 11 44 24 58                  movups xmmword ptr [rsp + 0x58], xmm0
00907BD7  45 8D 67 01                     lea r12d, [r15 + 1]
00907BDB  0F 11 44 24 68                  movups xmmword ptr [rsp + 0x68], xmm0
00907BE0  41 84 C4                        test r12b, al
00907BE3  0F 85 C6 04 00 00               jne 0x1409080af
00907BE9  0F BA B1 F4 01 00 00 1A         btr dword ptr [rcx + 0x1f4], 0x1a
00907BF1  48 8D B9 D8 01 00 00            lea rdi, [rcx + 0x1d8]
00907BF8  65 48 8B 34 25 88 01 00 00      mov rsi, qword ptr gs:[0x188]
00907C01  4C 39 3F                        cmp qword ptr [rdi], r15
00907C04  74 30                           je 0x140907c36
00907C06  48 8B CE                        mov rcx, rsi
00907C09  E8 7E DB 91 FF                  call 0x14022578c
00907C0E  48 8B 0F                        mov rcx, qword ptr [rdi]
00907C11  48 39 79 08                     cmp qword ptr [rcx + 8], rdi
00907C15  75 09                           jne 0x140907c20
00907C17  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
00907C1B  48 39 38                        cmp qword ptr [rax], rdi
00907C1E  74 07                           je 0x140907c27
00907C20  B9 03 00 00 00                  mov ecx, 3
00907C25  CD 29                           int 0x29
00907C27  48 89 08                        mov qword ptr [rax], rcx
00907C2A  48 89 41 08                     mov qword ptr [rcx + 8], rax
00907C2E  48 8B CE                        mov rcx, rsi
00907C31  E8 E2 80 9D FF                  call 0x1402dfd18
00907C36  48 8B 8B 50 03 00 00            mov rcx, qword ptr [rbx + 0x350]
00907C3D  48 85 C9                        test rcx, rcx
00907C40  74 0E                           je 0x140907c50
00907C42  33 D2                           xor edx, edx
00907C44  E8 27 AC 27 00                  call 0x140b82870
00907C49  4C 89 BB 50 03 00 00            mov qword ptr [rbx + 0x350], r15
00907C50  48 8B CB                        mov rcx, rbx
00907C53  E8 30 FA FF FF                  call 0x140907688
00907C58  48 8D 8B 20 07 00 00            lea rcx, [rbx + 0x720]
00907C5F  4C 39 39                        cmp qword ptr [rcx], r15
00907C62  0F 85 E7 02 00 00               jne 0x140907f4f
00907C68  48 8B 8B 08 03 00 00            mov rcx, qword ptr [rbx + 0x308]
00907C6F  48 85 C9                        test rcx, rcx
00907C72  0F 85 7A 04 00 00               jne 0x1409080f2
00907C78  48 8B 8B 40 02 00 00            mov rcx, qword ptr [rbx + 0x240]
00907C7F  48 85 C9                        test rcx, rcx
00907C82  74 10                           je 0x140907c94
00907C84  48 83 E1 F8                     and rcx, 0xfffffffffffffff8
00907C88  E8 C3 16 9F FF                  call 0x1402f9350
00907C8D  4C 89 BB 40 02 00 00            mov qword ptr [rbx + 0x240], r15
00907C94  4C 39 BB B8 07 00 00            cmp qword ptr [rbx + 0x7b8], r15
00907C9B  0F 85 62 04 00 00               jne 0x140908103
00907CA1  48 8B CB                        mov rcx, rbx
00907CA4  E8 67 5C B3 FF                  call 0x14043d910
00907CA9  48 8B C8                        mov rcx, rax
00907CAC  E8 B7 FA FF FF                  call 0x140907768
00907CB1  0F BA A3 F4 01 00 00 12         bt dword ptr [rbx + 0x1f4], 0x12
00907CB9  41 BE 04 00 00 00               mov r14d, 4
00907CBF  73 63                           jae 0x140907d24
00907CC1  4C 8D 44 24 48                  lea r8, [rsp + 0x48]
00907CC6  33 D2                           xor edx, edx
00907CC8  48 8B CB                        mov rcx, rbx
00907CCB  E8 50 EB 90 FF                  call 0x140216820
00907CD0  F7 83 F0 01 00 00 00 04 00 00   test dword ptr [rbx + 0x1f0], 0x400
00907CDA  0F 85 30 04 00 00               jne 0x140908110
00907CE0  F0 44 09 B3 F4 01 00 00         lock or dword ptr [rbx + 0x1f4], r14d
00907CE8  48 8B 8B 48 03 00 00            mov rcx, qword ptr [rbx + 0x348]
00907CEF  48 85 C9                        test rcx, rcx
00907CF2  0F 85 44 02 00 00               jne 0x140907f3c
00907CF8  4C 89 A3 48 03 00 00            mov qword ptr [rbx + 0x348], r12
00907CFF  33 D2                           xor edx, edx
00907D01  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
00907D06  E8 25 00 91 FF                  call 0x140217d30
00907D0B  48 8B CB                        mov rcx, rbx
00907D0E  E8 39 03 1C 00                  call 0x140ac804c
00907D13  48 8B 8B E8 02 00 00            mov rcx, qword ptr [rbx + 0x2e8]
00907D1A  48 85 C9                        test rcx, rcx
00907D1D  74 05                           je 0x140907d24
00907D1F  E8 20 67 19 00                  call 0x140a9e444
00907D24  48 8B 83 A0 02 00 00            mov rax, qword ptr [rbx + 0x2a0]
00907D2B  48 85 C0                        test rax, rax
00907D2E  74 3D                           je 0x140907d6d
00907D30  45 33 C9                        xor r9d, r9d
00907D33  45 8B C4                        mov r8d, r12d
00907D36  33 D2                           xor edx, edx
00907D38  48 8B CB                        mov rcx, rbx
00907D3B  E8 48 F5 FF FF                  call 0x140907288
00907D40  48 8B 8B A0 02 00 00            mov rcx, qword ptr [rbx + 0x2a0]
00907D47  BA 50 73 50 73                  mov edx, 0x73507350
00907D4C  E8 4F C1 95 FF                  call 0x140263ea0
00907D51  4C 89 BB A0 02 00 00            mov qword ptr [rbx + 0x2a0], r15
00907D58  4C 89 BB 78 02 00 00            mov qword ptr [rbx + 0x278], r15
00907D5F  48 8B 05 A2 EE 6B 00            mov rax, qword ptr [rip + 0x6beea2]
00907D66  48 89 83 F0 05 00 00            mov qword ptr [rbx + 0x5f0], rax
00907D6D  4C 39 BB 70 01 00 00            cmp qword ptr [rbx + 0x170], r15
00907D74  0F 85 AA 03 00 00               jne 0x140908124
00907D7A  4C 39 BB D0 01 00 00            cmp qword ptr [rbx + 0x1d0], r15
00907D81  74 58                           je 0x140907ddb
00907D83  66 44 29 A6 E6 01 00 00         sub word ptr [rsi + 0x1e6], r12w
00907D8B  90                              nop
00907D8C  48 8B 93 D0 01 00 00            mov rdx, qword ptr [rbx + 0x1d0]
00907D93  48 8B 0D 0E EF 6B 00            mov rcx, qword ptr [rip + 0x6bef0e]
00907D9A  E8 C1 0D F6 FF                  call 0x140868b60
00907D9F  48 85 C0                        test rax, rax
00907DA2  0F 84 C6 01 00 00               je 0x140907f6e
00907DA8  48 8B 93 D0 01 00 00            mov rdx, qword ptr [rbx + 0x1d0]
00907DAF  4C 8B C0                        mov r8, rax
00907DB2  48 8B 0D EF EE 6B 00            mov rcx, qword ptr [rip + 0x6beeef]
00907DB9  E8 72 16 F8 FF                  call 0x140889430
00907DBE  90                              nop
00907DBF  66 44 01 A6 E6 01 00 00         add word ptr [rsi + 0x1e6], r12w
00907DC7  75 12                           jne 0x140907ddb
00907DC9  48 8D 86 98 00 00 00            lea rax, [rsi + 0x98]
00907DD0  90                              nop
00907DD1  48 39 00                        cmp qword ptr [rax], rax
00907DD4  74 05                           je 0x140907ddb
00907DD6  E8 A5 AE 9D FF                  call 0x1402e2c80
00907DDB  4C 39 BB 48 02 00 00            cmp qword ptr [rbx + 0x248], r15
00907DE2  74 08                           je 0x140907dec
00907DE4  48 8B CB                        mov rcx, rbx
00907DE7  E8 D4 F7 FF FF                  call 0x1409075c0
00907DEC  48 8B 8B C0 02 00 00            mov rcx, qword ptr [rbx + 0x2c0]
00907DF3  48 85 C9                        test rcx, rcx
00907DF6  0F 85 35 03 00 00               jne 0x140908131
00907DFC  4C 39 BB 58 07 00 00            cmp qword ptr [rbx + 0x758], r15
00907E03  74 38                           je 0x140907e3d
00907E05  F7 83 FC 05 00 00 00 00 00 40   test dword ptr [rbx + 0x5fc], 0x40000000
00907E0F  41 8B FF                        mov edi, r15d
00907E12  0F 85 41 01 00 00               jne 0x140907f59
00907E18  41 8B FC                        mov edi, r12d
00907E1B  0F BA A3 F4 01 00 00 12         bt dword ptr [rbx + 0x1f4], 0x12
00907E23  73 08                           jae 0x140907e2d
00907E25  48 8B CB                        mov rcx, rbx
00907E28  E8 C7 08 16 00                  call 0x140a686f4
00907E2D  85 FF                           test edi, edi
00907E2F  74 0C                           je 0x140907e3d
00907E31  48 8B 8B 58 07 00 00            mov rcx, qword ptr [rbx + 0x758]
00907E38  E8 33 B0 A3 FF                  call 0x140342e70
00907E3D  48 8B CB                        mov rcx, rbx
00907E40  E8 BB F7 FF FF                  call 0x140907600
00907E45  48 8B CB                        mov rcx, rbx
00907E48  E8 D3 FA FF FF                  call 0x140907920
00907E4D  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00907E56  48 89 5C 24 40                  mov qword ptr [rsp + 0x40], rbx
00907E5B  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00907E62  90                              nop
00907E63  48 8B 8B E8 05 00 00            mov rcx, qword ptr [rbx + 0x5e8]
00907E6A  48 85 C9                        test rcx, rcx
00907E6D  74 08                           je 0x140907e77
00907E6F  41 8B D4                        mov edx, r12d
00907E72  E8 F9 03 00 00                  call 0x140908270
00907E77  BE 08 00 00 00                  mov esi, 8
00907E7C  48 8D 54 24 40                  lea rdx, [rsp + 0x40]
00907E81  44 8B C6                        mov r8d, esi
00907E84  8D 4E FB                        lea ecx, [rsi - 5]
00907E87  E8 DC 02 00 00                  call 0x140908168
00907E8C  E8 1F 5A 95 FF                  call 0x14025d8b0
00907E91  48 8B D3                        mov rdx, rbx
00907E94  33 C9                           xor ecx, ecx
00907E96  E8 81 D3 B8 FF                  call 0x14049521c
00907E9B  48 8B CB                        mov rcx, rbx
00907E9E  E8 95 FB FF FF                  call 0x140907a38
00907EA3  48 8B 8B 70 06 00 00            mov rcx, qword ptr [rbx + 0x670]
00907EAA  48 85 C9                        test rcx, rcx
00907EAD  0F 85 97 02 00 00               jne 0x14090814a
00907EB3  49 BC B0 03 00 00 80 F7 FF FF   movabs r12, 0xfffff780000003b0
00907EBD  49 BF 08 00 00 00 80 F7 FF FF   movabs r15, 0xfffff78000000008
00907EC7  49 8B 14 24                     mov rdx, qword ptr [r12]
00907ECB  49 8B 0F                        mov rcx, qword ptr [r15]
00907ECE  49 8B 04 24                     mov rax, qword ptr [r12]
00907ED2  48 3B D0                        cmp rdx, rax
00907ED5  75 F0                           jne 0x140907ec7
00907ED7  41 BF 00 00 00 00               mov r15d, 0
00907EDD  48 2B CA                        sub rcx, rdx
00907EE0  48 3B 0D 69 A7 55 00            cmp rcx, qword ptr [rip + 0x55a769]
00907EE7  45 8D 67 01                     lea r12d, [r15 + 1]
00907EEB  0F 82 88 00 00 00               jb 0x140907f79
00907EF1  4C 8D 1D C8 99 8F 00            lea r11, [rip + 0x8f99c8]
00907EF8  4D 8B CB                        mov r9, r11
00907EFB  0F 18 05 BE 99 8F 00            prefetchnta byte ptr [rip + 0x8f99be]
00907F02  4C 8B 05 37 A7 55 00            mov r8, qword ptr [rip + 0x55a737]
00907F09  45 8D 57 40                     lea r10d, [r15 + 0x40]
00907F0D  48 8B 3D 34 A7 55 00            mov rdi, qword ptr [rip + 0x55a734]
00907F14  49 8B D0                        mov rdx, r8
00907F17  48 8B C6                        mov rax, rsi
00907F1A  49 2B 11                        sub rdx, qword ptr [r9]
00907F1D  8B CF                           mov ecx, edi
00907F1F  48 D3 CA                        ror rdx, cl
00907F22  4C 03 CE                        add r9, rsi
00907F25  41 83 C2 F8                     add r10d, -8
00907F29  49 2B C4                        sub rax, r12
00907F2C  75 EC                           jne 0x140907f1a
00907F2E  45 85 D2                        test r10d, r10d
00907F31  0F 85 FB 90 21 00               jne 0x140b21032
00907F37  E9 0B 91 21 00                  jmp 0x140b21047
00907F3C  49 3B CC                        cmp rcx, r12
00907F3F  0F 84 BA FD FF FF               je 0x140907cff
00907F45  E8 06 14 9F FF                  call 0x1402f9350
00907F4A  E9 A9 FD FF FF                  jmp 0x140907cf8
00907F4F  E8 9C 6D DA FF                  call 0x1406aecf0
00907F54  E9 0F FD FF FF                  jmp 0x140907c68
00907F59  48 8B CB                        mov rcx, rbx
00907F5C  E8 3F FE BE FF                  call 0x1404f7da0
00907F61  85 C0                           test eax, eax
00907F63  0F 84 B2 FE FF FF               je 0x140907e1b
00907F69  E9 AA FE FF FF                  jmp 0x140907e18
00907F6E  B9 17 00 00 00                  mov ecx, 0x17
00907F73  E8 C8 56 BF FF                  call 0x1404fd640
00907F78  CC                              int3
00907F79  48 8B 8B F8 02 00 00            mov rcx, qword ptr [rbx + 0x2f8]
00907F80  48 85 C9                        test rcx, rcx
00907F83  74 05                           je 0x140907f8a
00907F85  E8 1A F6 FF FF                  call 0x1409075a4
00907F8A  8B 83 08 01 00 00               mov eax, dword ptr [rbx + 0x108]
00907F90  48 8B 8B 90 01 00 00            mov rcx, qword ptr [rbx + 0x190]
00907F97  48 85 C9                        test rcx, rcx
00907F9A  74 0A                           je 0x140907fa6
00907F9C  BA 10 00 00 00                  mov edx, 0x10
00907FA1  E8 26 7B B3 FF                  call 0x14043facc
00907FA6  48 8B CB                        mov rcx, rbx
00907FA9  E8 12 79 B3 FF                  call 0x14043f8c0
00907FAE  48 8B 8B C0 01 00 00            mov rcx, qword ptr [rbx + 0x1c0]
00907FB5  48 85 C9                        test rcx, rcx
00907FB8  74 09                           je 0x140907fc3
00907FBA  48 83 C1 38                     add rcx, 0x38
00907FBE  E8 B5 7A B3 FF                  call 0x14043fa78
00907FC3  48 8B 8B 10 03 00 00            mov rcx, qword ptr [rbx + 0x310]
00907FCA  48 85 C9                        test rcx, rcx
00907FCD  74 0E                           je 0x140907fdd
00907FCF  33 D2                           xor edx, edx
00907FD1  E8 9A A8 27 00                  call 0x140b82870
00907FD6  4C 89 BB 10 03 00 00            mov qword ptr [rbx + 0x310], r15
00907FDD  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
00907FE2  48 33 CC                        xor rcx, rsp
00907FE5  E8 56 46 DA FF                  call 0x1406ac640
00907FEA  4C 8D 9C 24 80 00 00 00         lea r11, [rsp + 0x80]
00907FF2  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
00907FF6  49 8B 6B 40                     mov rbp, qword ptr [r11 + 0x40]
00907FFA  49 8B 73 48                     mov rsi, qword ptr [r11 + 0x48]
00907FFE  49 8B E3                        mov rsp, r11
00908001  41 5F                           pop r15
00908003  41 5E                           pop r14
00908005  41 5D                           pop r13
00908007  41 5C                           pop r12
00908009  5F                              pop rdi
0090800A  C3                              ret
0090800B  CC                              int3
0090800C  48 85 D2                        test rdx, rdx
0090800F  74 3A                           je 0x14090804b
00908011  48 8D 15 A8 3E D9 FF            lea rdx, [rip - 0x26c158]
00908018  48 39 15 C9 A5 55 00            cmp qword ptr [rip + 0x55a5c9], rdx
0090801F  48 8D 3D AA A5 55 00            lea rdi, [rip + 0x55a5aa]
00908026  74 0B                           je 0x140908033
00908028  4C 8B C7                        mov r8, rdi
0090802B  48 8B CF                        mov rcx, rdi
0090802E  E8 9D 3B B5 FF                  call 0x14045bbd0
00908033  45 33 C0                        xor r8d, r8d
00908036  48 C7 05 F7 A5 55 00 40 D9 1A 00  mov qword ptr [rip + 0x55a5f7], 0x1ad940
00908041  33 D2                           xor edx, edx
00908043  48 8B CF                        mov rcx, rdi
00908046  E8 05 FC 8F FF                  call 0x140207c50
0090804B  48 BA B0 03 00 00 80 F7 FF FF   movabs rdx, 0xfffff780000003b0
00908055  49 B9 08 00 00 00 80 F7 FF FF   movabs r9, 0xfffff78000000008
0090805F  48 8B 0A                        mov rcx, qword ptr [rdx]
00908062  4D 8B 01                        mov r8, qword ptr [r9]
00908065  48 8B 02                        mov rax, qword ptr [rdx]
00908068  48 3B C8                        cmp rcx, rax
0090806B  75 F2                           jne 0x14090805f
0090806D  0F 31                           rdtsc
0090806F  48 C1 E2 20                     shl rdx, 0x20
00908073  49 B9 00 20 5F A0 12 00 00 00   movabs r9, 0x12a05f2000
0090807D  48 0B C2                        or rax, rdx
00908080  33 D2                           xor edx, edx
00908082  48 C1 E8 04                     shr rax, 4
00908086  48 69 C0 BF CB 7F 02            imul rax, rax, 0x27fcbbf
0090808D  49 F7 F1                        div r9
00908090  48 2B D1                        sub rdx, rcx
00908093  48 B9 00 40 23 0E 43 00 00 00   movabs rcx, 0x430e234000
0090809D  48 03 CA                        add rcx, rdx
009080A0  49 03 C8                        add rcx, r8
009080A3  48 89 0D A6 A5 55 00            mov qword ptr [rip + 0x55a5a6], rcx
009080AA  E9 CA FE FF FF                  jmp 0x140907f79
009080AF  4C 39 B9 40 06 00 00            cmp qword ptr [rcx + 0x640], r15
009080B6  0F 85 2D FB FF FF               jne 0x140907be9
009080BC  F7 81 F4 01 00 00 00 00 00 04   test dword ptr [rcx + 0x1f4], 0x4000000
009080C6  0F 84 1D FB FF FF               je 0x140907be9
009080CC  8B 81 DC 07 00 00               mov eax, dword ptr [rcx + 0x7dc]
009080D2  A8 02                           test al, 2
009080D4  0F 85 0F FB FF FF               jne 0x140907be9
009080DA  45 33 C9                        xor r9d, r9d
009080DD  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
009080E2  4C 8B C3                        mov r8, rbx
009080E5  33 D2                           xor edx, edx
009080E7  B9 F8 01 00 00                  mov ecx, 0x1f8
009080EC  E8 6F 55 BF FF                  call 0x1404fd660
009080F1  CC                              int3
009080F2  E8 59 12 9F FF                  call 0x1402f9350
009080F7  4C 89 BB 08 03 00 00            mov qword ptr [rbx + 0x308], r15
009080FE  E9 75 FB FF FF                  jmp 0x140907c78
00908103  48 8B CB                        mov rcx, rbx
00908106  E8 B1 63 E7 FF                  call 0x14077e4bc
0090810B  E9 91 FB FF FF                  jmp 0x140907ca1
00908110  48 8B 05 21 E4 5F 00            mov rax, qword ptr [rip + 0x5fe421]
00908117  48 8B CB                        mov rcx, rbx
0090811A  E8 B1 29 DB FF                  call 0x1406baad0
0090811F  E9 BC FB FF FF                  jmp 0x140907ce0
00908124  48 8B CB                        mov rcx, rbx
00908127  E8 34 18 CB FF                  call 0x1405b9960
0090812C  E9 49 FC FF FF                  jmp 0x140907d7a
00908131  33 D2                           xor edx, edx
00908133  E8 38 A7 27 00                  call 0x140b82870
00908138  BA 28 60 00 00                  mov edx, 0x6028
0090813D  48 8B CB                        mov rcx, rbx
00908140  E8 BB 40 B1 FF                  call 0x14041c200
00908145  E9 B2 FC FF FF                  jmp 0x140907dfc
0090814A  E8 5D 5C EA FF                  call 0x1407addac
0090814F  48 8B 8B 70 06 00 00            mov rcx, qword ptr [rbx + 0x670]
00908156  33 D2                           xor edx, edx
00908158  E8 13 A7 27 00                  call 0x140b82870
0090815D  E9 51 FD FF FF                  jmp 0x140907eb3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PspProcessDelete(__int64 a1, int a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r15;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;

    v_stack_p10 = v_rbx;
    v_stack_p18 = v_rbp;
    v_stack_p20 = v_rsi;
    v_rsp = (v_rsp) - (128);
    result = (*(unsigned __int64 *)(v_rip + 5254026)) ^ (v_rsp);
    v_stack_m30 = result;
    v_r15 = 0;
    v_stack_m60 = v_xmm0;
    v_stack_m50 = v_xmm0;
    v_stack_m40 = v_xmm0;
    if ((((unsigned __int8)(v_r15 + 1)) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 1532))))) != 0) goto loc_009080AF;
loc_00907BE9:
    if ((*(unsigned __int64 *)(a1 + 472)) == 0) goto loc_00907C36;
    result = PspLockProcessListExclusive(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, a4);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 472) + 8)) != (a1 + 472)) goto loc_00907C20;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 472 + 8))) != (a1 + 472)) {
        a1 = 3;
    }
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 472 + 8)) = a1;
    *(unsigned __int64 *)(a1 + 8) = *(unsigned __int64 *)(a1 + 472 + 8);
    result = PspUnlockProcessListExclusive(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, a4);
loc_00907C36:
    if (*(unsigned __int64 *)(a1 + 848) != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(a1 + 848), a2, a3, a4);
        *(unsigned __int64 *)(a1 + 848) = 0;
    }
    result = ObClearProcessDeviceMap(a1, a2, a3, a4);
    if ((*(unsigned __int64 *)(a1 + 1824)) != 0) goto loc_00907F4F;
loc_00907C68:
    if (*(unsigned __int64 *)(a1 + 776) != 0) goto loc_009080F2;
loc_00907C78:
    if (*(unsigned __int64 *)(a1 + 576) != 0) {
        a1 = (*(unsigned __int64 *)(a1 + 576)) & (-8);
        result = ObfDereferenceObject(a1, a2, a3, a4);
        *(unsigned __int64 *)(a1 + 576) = 0;
    }
    if ((*(unsigned __int64 *)(a1 + 1976)) != 0) goto loc_00908103;
loc_00907CA1:
    result = PsGetProcessId(a1, a2, a3, a4);
    result = sub_00907768(result, a2, a3, a4);
    if ((*(unsigned __int64 *)(a1 + 1976)) >= 0) goto loc_00907D24;
    a2 = 0;
    result = KiStackAttachProcess(a1, a2, v_stack_m60, a4);
    if (((*(unsigned int *)(a1 + 496)) & (0x400ULL)) != 0) goto loc_00908110;
loc_00907CE0:
    if (*(unsigned __int64 *)(a1 + 840) != 0) goto loc_00907F3C;
loc_00907CF8:
    *(unsigned __int64 *)(a1 + 840) = v_r15 + 1;
loc_00907CFF:
    a2 = 0;
    result = KiUnstackDetachProcess(v_stack_m60, a2, v_stack_m60, a4);
    result = MmDeleteProcessAddressSpace(a1, a2, v_stack_m60, a4);
    if (*(unsigned __int64 *)(a1 + 744) != 0) {
        result = PspReleaseReferenceToSession(*(unsigned __int64 *)(a1 + 744), a2, v_stack_m60, a4);
    }
    result = *(unsigned __int64 *)(a1 + 672);
    if (*(unsigned __int64 *)(a1 + 672) != 0) {
        a4 = 0;
        a3 = (unsigned int)(v_r15 + 1);
        a2 = 0;
        a1 = a1;
        result = PspRemoveProcessFromJobChain(a1, a2, a3, a4);
        a1 = *(unsigned __int64 *)(a1 + 672);
        a2 = 0x73507350ULL;
        result = ObDereferenceObjectDeferDeleteWithTag(a1, a2, a3, a4);
        *(unsigned __int64 *)(a1 + 672) = 0;
        *(unsigned __int64 *)(a1 + 632) = 0;
        result = *(unsigned __int64 *)(v_rip + 7073442);
        *(unsigned __int64 *)(a1 + 1520) = result;
    }
    if ((*(unsigned __int64 *)(a1 + 368)) != 0) goto loc_00908124;
loc_00907D7A:
    if ((*(unsigned __int64 *)(a1 + 464)) == 0) goto loc_00907DDB;
    result = ExMapHandleToPointer(*(unsigned __int64 *)(v_rip + 7073550), *(unsigned __int64 *)(a1 + 464), a3, a4);
    if (result == 0) goto loc_00907F6E;
    result = ExDestroyHandle(*(unsigned __int64 *)(v_rip + 7073519), *(unsigned __int64 *)(a1 + 464), result, a4);
    if (result != 0) goto loc_00907DDB;
    result = *(unsigned __int64 *)(gs_base + (0 + 392)) + 152;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 152)) != (*(unsigned __int64 *)(gs_base + (0 + 392)) + 152)) {
        result = KiCheckForKernelApcDelivery(*(unsigned __int64 *)(v_rip + 7073519), *(unsigned __int64 *)(a1 + 464), result, a4);
    }
    if ((*(unsigned __int64 *)(a1 + 584)) != 0) {
        a1 = a1;
        result = SeDeassignPrimaryToken(a1, *(unsigned __int64 *)(a1 + 464), result, a4);
    }
    if (*(unsigned __int64 *)(a1 + 704) != 0) goto loc_00908131;
loc_00907DFC:
    if ((*(unsigned __int64 *)(a1 + 1880)) == 0) goto loc_00907E3D;
    if (((*(unsigned int *)(a1 + 1532)) & (0x40000000ULL)) != 0) goto loc_00907F59;
loc_00907E18:
loc_00907E1B:
    if (!(condition_is_above_or_equal)) {
        a1 = a1;
        result = SmProcessDeleteNotification(a1, *(unsigned __int64 *)(a1 + 464), result, a4);
    }
    if ((unsigned int)((unsigned int)((unsigned int)(v_r15 + 1))) != 0) {
        a1 = *(unsigned __int64 *)(a1 + 1880);
        result = PsDereferencePartition(a1, *(unsigned __int64 *)(a1 + 464), result, a4);
    }
    result = EtwExitProcess(a1, *(unsigned __int64 *)(a1 + 464), result, a4);
    result = LpcExitProcess(a1, *(unsigned __int64 *)(a1 + 464), result, a4);
    v_stack_m68 = a1;
    result = *(unsigned __int64 *)(gs_base + (0 + 392));
    if (*(unsigned __int64 *)(a1 + 1512) != 0) {
        a2 = (unsigned int)(v_r15 + 1);
        result = ExpWnfDeleteProcessContext(*(unsigned __int64 *)(a1 + 1512), a2, result, a4);
    }
    result = ExpWnfDeleteScopeById(8 - 5, v_stack_m68, 8, a4);
    result = KeLeaveCriticalRegion(8 - 5, v_stack_m68, 8, a4);
    a1 = 0;
    result = IoSetDiskIoAttributionOnProcess(a1, a1, 8, a4);
    result = PoEnergyContextCleanup(0, a1, 8, a4);
    if (*(unsigned __int64 *)(a1 + 1648) != 0) goto loc_0090814A;
loc_00907EB3:
loc_00907EC7:
    if ((*(unsigned __int64 *)(v_r15 + 1)) != (*(unsigned __int64 *)(v_r15 + 1))) goto loc_00907EC7;
    a1 = (*(unsigned __int64 *)(v_r15)) - (*(unsigned __int64 *)(v_r15 + 1));
    if (a1 < (*(unsigned __int64 *)(v_rip + 5613417))) goto loc_00907F79;
loc_00907F1A:
    a2 = (*(unsigned __int64 *)(v_rip + 5613367)) - (*(unsigned __int64 *)(v_rip + 9411016));
    a4 = (v_rip + 9411016) + (8);
    v_r10 = (unsigned int)((0 + 64) + (-8));
    result = (8) - (0 + 1);
    if (condition_is_not_equal) goto loc_00907F1A;
loc_00907F3C:
    if (((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rip + 5613364)))) == (0 + 1)) goto loc_00907CFF;
    result = ObfDereferenceObject((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rip + 5613364))), a2, *(unsigned __int64 *)(v_rip + 5613367), a4);
    goto loc_00907CF8;
loc_00907F4F:
    result = ZwDeleteWnfStateName((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rip + 5613364))), a2, *(unsigned __int64 *)(v_rip + 5613367), a4);
    goto loc_00907C68;
loc_00907F59:
    result = SmCompressionProcessHoldsPartitionReference(a1, a2, *(unsigned __int64 *)(v_rip + 5613367), a4);
    if ((unsigned int)(result) == 0) goto loc_00907E1B;
    goto loc_00907E18;
loc_00907F6E:
    result = KeBugCheck(23, a2, *(unsigned __int64 *)(v_rip + 5613367), a4);
loc_00907F79:
    if (*(unsigned __int64 *)(a1 + 760) != 0) {
        result = PspDereferenceQuota(*(unsigned __int64 *)(a1 + 760), a2, *(unsigned __int64 *)(v_rip + 5613367), a4);
    }
    result = (unsigned int)(*(unsigned int *)(a1 + 264));
    if (*(unsigned __int64 *)(a1 + 400) != 0) {
        a2 = 16;
        result = ExSaFree(*(unsigned __int64 *)(a1 + 400), a2, *(unsigned __int64 *)(v_rip + 5613367), a4);
    }
    result = KiRemoveAndFreeCpuPartitionAssignmentProcess(a1, a2, *(unsigned __int64 *)(v_rip + 5613367), a4);
    if (*(unsigned __int64 *)(a1 + 448) != 0) {
        a1 = (*(unsigned __int64 *)(a1 + 448)) + (56);
        result = KiRundownAvailableCpusWorkItem(a1, a2, *(unsigned __int64 *)(v_rip + 5613367), a4);
    }
    if (*(unsigned __int64 *)(a1 + 784) != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(a1 + 784), a2, *(unsigned __int64 *)(v_rip + 5613367), a4);
        *(unsigned __int64 *)(a1 + 784) = 0;
    }
    a1 = (v_stack_m30) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, *(unsigned __int64 *)(v_rip + 5613367), a4);
    return result;
loc_009080AF:
    if ((*(unsigned __int64 *)(a1 + 1600)) != 0) goto loc_00907BE9;
    if (((*(unsigned int *)(a1 + 500)) & (0x4000000ULL)) == 0) goto loc_00907BE9;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 2012)))) & (2)) != 0) goto loc_00907BE9;
    a4 = 0;
    v_stack_m60 = 0;
    a2 = 0;
    result = KeBugCheckEx(504, a2, *(unsigned __int64 *)(v_stack_m28 + 56), a4);
loc_009080F2:
    result = ObfDereferenceObject(504, a2, *(unsigned __int64 *)(v_stack_m28 + 56), a4);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 776) = 0;
    goto loc_00907C78;
loc_00908103:
    result = PspDetachProcessFromSyscallProvider(*(unsigned __int64 *)(v_stack_m28 + 56), a2, *(unsigned __int64 *)(v_stack_m28 + 56), a4);
    goto loc_00907CA1;
loc_00908110:
    result = guard_dispatch_icall(*(unsigned __int64 *)(v_stack_m28 + 56), a2, *(unsigned __int64 *)(v_stack_m28 + 56), a4);
    goto loc_00907CE0;
loc_00908124:
    result = KeUnsecureProcess(*(unsigned __int64 *)(v_stack_m28 + 56), a2, *(unsigned __int64 *)(v_stack_m28 + 56), a4);
    goto loc_00907D7A;
loc_00908131:
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(v_stack_m28 + 56), a2, *(unsigned __int64 *)(v_stack_m28 + 56), a4);
    result = PsReturnProcessNonPagedPoolQuota(*(unsigned __int64 *)(v_stack_m28 + 56), (unsigned int)(0x6028ULL), *(unsigned __int64 *)(v_stack_m28 + 56), a4);
    goto loc_00907DFC;
loc_0090814A:
    result = VmpProcessContextCleanup(*(unsigned __int64 *)(v_stack_m28 + 56), (unsigned int)(0x6028ULL), *(unsigned __int64 *)(v_stack_m28 + 56), a4);
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 1648), a2, *(unsigned __int64 *)(v_stack_m28 + 56), a4);
    goto loc_00907EB3;
}
```

## 5. (Beta) C Style

```c
int64_t PspProcessDelete(void *Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r15;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m40;
    uint64_t v_stack_m50;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;

    v_stack_p10 = local_rbx;
    v_stack_p18 = local_rbp;
    v_stack_p20 = local_rsi;
    local_rsp = (local_rsp) - (128);
    result = (*(uint64_t *)(v_rip + 0x502B8A)) ^ (local_rsp);
    v_stack_m30 = result;
    local_r15 = 0;
    v_stack_m60 = v_xmm0;
    v_stack_m50 = v_xmm0;
    v_stack_m40 = v_xmm0;
    if ((((uint8_t)(local_r15 + 1)) & ((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x5FC))))) != 0) goto loc_009080AF;
loc_00907BE9:
    if ((*(uint64_t *)(arg1 + 0x1D8)) == 0) goto loc_00907C36;
    result = PspLockProcessListExclusive(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, Arg3, Arg4);
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x1D8) + 0x8)) != (Arg1 + 472)) goto loc_00907C20;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x1D8 + 0x8))) != (Arg1 + 472)) {
        Arg1 = 3;
    }
    *(void **)(*(uint64_t *)(arg1 + 0x1D8 + 0x8)) = Arg1;
    *(uint64_t *)(arg1 + 0x8) = *(uint64_t *)(arg1 + 0x1D8 + 0x8);
    result = PspUnlockProcessListExclusive(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, Arg3, Arg4);
loc_00907C36:
    if (*(uint64_t *)(arg1 + 0x350) != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(arg1 + 0x350), Arg2, Arg3, Arg4);
        *(uint64_t *)(arg1 + 0x350) = 0;
    }
    result = ObClearProcessDeviceMap(Arg1, Arg2, Arg3, Arg4);
    if ((*(uint64_t *)(arg1 + 0x720)) != 0) goto loc_00907F4F;
loc_00907C68:
    if (*(uint64_t *)(arg1 + 0x308) != 0) goto loc_009080F2;
loc_00907C78:
    if (*(uint64_t *)(arg1 + 0x240) != 0) {
        Arg1 = (*(uint64_t *)(arg1 + 0x240)) & (-8);
        result = ObfDereferenceObject(Arg1, Arg2, Arg3, Arg4);
        *(uint64_t *)(arg1 + 0x240) = 0;
    }
    if ((*(uint64_t *)(arg1 + 0x7B8)) != 0) goto loc_00908103;
loc_00907CA1:
    result = PsGetProcessId(Arg1, Arg2, Arg3, Arg4);
    result = sub_00907768(result, Arg2, Arg3, Arg4);
    if ((*(uint64_t *)(arg1 + 0x7B8)) >= 0) goto loc_00907D24;
    Arg2 = 0;
    result = KiStackAttachProcess(Arg1, Arg2, v_stack_m60, Arg4);
    if (((*(uint32_t *)(arg1 + 0x1F0)) & (0x400ULL)) != 0) goto loc_00908110;
loc_00907CE0:
    if (*(uint64_t *)(arg1 + 0x348) != 0) goto loc_00907F3C;
loc_00907CF8:
    *(uint64_t *)(arg1 + 0x348) = local_r15 + 1;
loc_00907CFF:
    Arg2 = 0;
    result = KiUnstackDetachProcess(v_stack_m60, Arg2, v_stack_m60, Arg4);
    result = MmDeleteProcessAddressSpace(Arg1, Arg2, v_stack_m60, Arg4);
    if (*(uint64_t *)(arg1 + 0x2E8) != 0) {
        result = PspReleaseReferenceToSession(*(uint64_t *)(arg1 + 0x2E8), Arg2, v_stack_m60, Arg4);
    }
    result = *(uint64_t *)(arg1 + 0x2A0);
    if (*(uint64_t *)(arg1 + 0x2A0) != 0) {
        Arg4 = 0;
        Arg3 = (uint32_t)(local_r15 + 1);
        Arg2 = 0;
        Arg1 = Arg1;
        result = PspRemoveProcessFromJobChain(Arg1, Arg2, Arg3, Arg4);
        Arg1 = *(uint64_t *)(arg1 + 0x2A0);
        Arg2 = 0x73507350ULL;
        result = ObDereferenceObjectDeferDeleteWithTag(Arg1, Arg2, Arg3, Arg4);
        *(uint64_t *)(arg1 + 0x2A0) = 0;
        *(uint64_t *)(arg1 + 0x278) = 0;
        result = *(uint64_t *)(v_rip + 0x6BEEA2);
        *(uint64_t *)(arg1 + 0x5F0) = result;
    }
    if ((*(uint64_t *)(arg1 + 0x170)) != 0) goto loc_00908124;
loc_00907D7A:
    if ((*(uint64_t *)(arg1 + 0x1D0)) == 0) goto loc_00907DDB;
    result = ExMapHandleToPointer(*(uint64_t *)(v_rip + 0x6BEF0E), *(uint64_t *)(arg1 + 0x1D0), Arg3, Arg4);
    if (result == 0) goto loc_00907F6E;
    result = ExDestroyHandle(*(uint64_t *)(v_rip + 0x6BEEEF), *(uint64_t *)(arg1 + 0x1D0), result, Arg4);
    if (result != 0) goto loc_00907DDB;
    result = *(uint64_t *)(gs_base + (0 + 0x188)) + 152;
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x98)) != (*(uint64_t *)(gs_base + (0 + 0x188)) + 152)) {
        result = KiCheckForKernelApcDelivery(*(uint64_t *)(v_rip + 0x6BEEEF), *(uint64_t *)(arg1 + 0x1D0), result, Arg4);
    }
    if ((*(uint64_t *)(arg1 + 0x248)) != 0) {
        Arg1 = Arg1;
        result = SeDeassignPrimaryToken(Arg1, *(uint64_t *)(arg1 + 0x1D0), result, Arg4);
    }
    if (*(uint64_t *)(arg1 + 0x2C0) != 0) goto loc_00908131;
loc_00907DFC:
    if ((*(uint64_t *)(arg1 + 0x758)) == 0) goto loc_00907E3D;
    if (((*(uint32_t *)(arg1 + 0x5FC)) & (0x40000000ULL)) != 0) goto loc_00907F59;
loc_00907E18:
loc_00907E1B:
    if (!(condition_is_above_or_equal)) {
        Arg1 = Arg1;
        result = SmProcessDeleteNotification(Arg1, *(uint64_t *)(arg1 + 0x1D0), result, Arg4);
    }
    if ((uint32_t)((uint32_t)((uint32_t)(local_r15 + 1))) != 0) {
        Arg1 = *(uint64_t *)(arg1 + 0x758);
        result = PsDereferencePartition(Arg1, *(uint64_t *)(arg1 + 0x1D0), result, Arg4);
    }
    result = EtwExitProcess(Arg1, *(uint64_t *)(arg1 + 0x1D0), result, Arg4);
    result = LpcExitProcess(Arg1, *(uint64_t *)(arg1 + 0x1D0), result, Arg4);
    v_stack_m68 = Arg1;
    result = *(uint64_t *)(gs_base + (0 + 0x188));
    if (*(uint64_t *)(arg1 + 0x5E8) != 0) {
        Arg2 = (uint32_t)(local_r15 + 1);
        result = ExpWnfDeleteProcessContext(*(uint64_t *)(arg1 + 0x5E8), Arg2, result, Arg4);
    }
    result = ExpWnfDeleteScopeById(8 - 5, v_stack_m68, 8, Arg4);
    result = KeLeaveCriticalRegion(8 - 5, v_stack_m68, 8, Arg4);
    Arg1 = 0;
    result = IoSetDiskIoAttributionOnProcess(Arg1, Arg1, 8, Arg4);
    result = PoEnergyContextCleanup(0, Arg1, 8, Arg4);
    if (*(uint64_t *)(arg1 + 0x670) != 0) goto loc_0090814A;
loc_00907EB3:
loc_00907EC7:
    if ((*(uint64_t *)(local_r15 + 0x1)) != (*(uint64_t *)(local_r15 + 0x1))) goto loc_00907EC7;
    Arg1 = (*(uint64_t *)(local_r15)) - (*(uint64_t *)(local_r15 + 0x1));
    if (Arg1 < (*(uint64_t *)(v_rip + 0x55A769))) goto loc_00907F79;
loc_00907F1A:
    Arg2 = (*(uint64_t *)(v_rip + 0x55A737)) - (*(uint64_t *)(v_rip + 0x8F99C8));
    Arg4 = (v_rip + 9411016) + (8);
    local_r10 = (uint32_t)((0 + 64) + (-8));
    result = (8) - (0 + 1);
    if (condition_is_not_equal) goto loc_00907F1A;
loc_00907F3C:
    if (((uint32_t)((uint32_t)(*(uint64_t *)(v_rip + 0x55A734)))) == (0 + 1)) goto loc_00907CFF;
    result = ObfDereferenceObject((uint32_t)((uint32_t)(*(uint64_t *)(v_rip + 0x55A734))), Arg2, *(uint64_t *)(v_rip + 0x55A737), Arg4);
    goto loc_00907CF8;
loc_00907F4F:
    result = ZwDeleteWnfStateName((uint32_t)((uint32_t)(*(uint64_t *)(v_rip + 0x55A734))), Arg2, *(uint64_t *)(v_rip + 0x55A737), Arg4);
    goto loc_00907C68;
loc_00907F59:
    result = SmCompressionProcessHoldsPartitionReference(Arg1, Arg2, *(uint64_t *)(v_rip + 0x55A737), Arg4);
    if ((uint32_t)(result) == 0) goto loc_00907E1B;
    goto loc_00907E18;
loc_00907F6E:
    result = KeBugCheck(23, Arg2, *(uint64_t *)(v_rip + 0x55A737), Arg4);
loc_00907F79:
    if (*(uint64_t *)(arg1 + 0x2F8) != 0) {
        result = PspDereferenceQuota(*(uint64_t *)(arg1 + 0x2F8), Arg2, *(uint64_t *)(v_rip + 0x55A737), Arg4);
    }
    result = (uint32_t)(*(uint32_t *)(arg1 + 0x108));
    if (*(uint64_t *)(arg1 + 0x190) != 0) {
        Arg2 = 16;
        result = ExSaFree(*(uint64_t *)(arg1 + 0x190), Arg2, *(uint64_t *)(v_rip + 0x55A737), Arg4);
    }
    result = KiRemoveAndFreeCpuPartitionAssignmentProcess(Arg1, Arg2, *(uint64_t *)(v_rip + 0x55A737), Arg4);
    if (*(uint64_t *)(arg1 + 0x1C0) != 0) {
        Arg1 = (*(uint64_t *)(arg1 + 0x1C0)) + (56);
        result = KiRundownAvailableCpusWorkItem(Arg1, Arg2, *(uint64_t *)(v_rip + 0x55A737), Arg4);
    }
    if (*(uint64_t *)(arg1 + 0x310) != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(arg1 + 0x310), Arg2, *(uint64_t *)(v_rip + 0x55A737), Arg4);
        *(uint64_t *)(arg1 + 0x310) = 0;
    }
    Arg1 = (v_stack_m30) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, *(uint64_t *)(v_rip + 0x55A737), Arg4);
    return result;
loc_009080AF:
    if ((*(uint64_t *)(arg1 + 0x640)) != 0) goto loc_00907BE9;
    if (((*(uint32_t *)(arg1 + 0x1F4)) & (0x4000000ULL)) == 0) goto loc_00907BE9;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x7DC)))) & (2)) != 0) goto loc_00907BE9;
    Arg4 = 0;
    v_stack_m60 = 0;
    Arg2 = 0;
    result = KeBugCheckEx(504, Arg2, *(uint64_t *)(v_stack_m28 + 0x38), Arg4);
loc_009080F2:
    result = ObfDereferenceObject(504, Arg2, *(uint64_t *)(v_stack_m28 + 0x38), Arg4);
    *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x308) = 0;
    goto loc_00907C78;
loc_00908103:
    result = PspDetachProcessFromSyscallProvider(*(uint64_t *)(v_stack_m28 + 0x38), Arg2, *(uint64_t *)(v_stack_m28 + 0x38), Arg4);
    goto loc_00907CA1;
loc_00908110:
    result = guard_dispatch_icall(*(uint64_t *)(v_stack_m28 + 0x38), Arg2, *(uint64_t *)(v_stack_m28 + 0x38), Arg4);
    goto loc_00907CE0;
loc_00908124:
    result = KeUnsecureProcess(*(uint64_t *)(v_stack_m28 + 0x38), Arg2, *(uint64_t *)(v_stack_m28 + 0x38), Arg4);
    goto loc_00907D7A;
loc_00908131:
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(v_stack_m28 + 0x38), Arg2, *(uint64_t *)(v_stack_m28 + 0x38), Arg4);
    result = PsReturnProcessNonPagedPoolQuota(*(uint64_t *)(v_stack_m28 + 0x38), (uint32_t)(0x6028ULL), *(uint64_t *)(v_stack_m28 + 0x38), Arg4);
    goto loc_00907DFC;
loc_0090814A:
    result = VmpProcessContextCleanup(*(uint64_t *)(v_stack_m28 + 0x38), (uint32_t)(0x6028ULL), *(uint64_t *)(v_stack_m28 + 0x38), Arg4);
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x670), Arg2, *(uint64_t *)(v_stack_m28 + 0x38), Arg4);
    goto loc_00907EB3;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x108` | `32` | `R` |
| `Arg1` | `+ 0x170` | `64` | `R` |
| `Arg1` | `+ 0x190` | `64` | `R` |
| `Arg1` | `+ 0x1C0` | `64` | `R` |
| `Arg1` | `+ 0x1D0` | `64` | `R` |
| `Arg1` | `+ 0x1D8` | `64` | `R` |
| `Arg1` | `+ 0x1F0` | `32` | `R` |
| `Arg1` | `+ 0x1F4` | `32` | `R` |
| `Arg1` | `+ 0x1F4` | `32` | `R/W` |
| `Arg1` | `+ 0x240` | `64` | `R` |
| `Arg1` | `+ 0x240` | `64` | `W` |
| `Arg1` | `+ 0x248` | `64` | `R` |
| `Arg1` | `+ 0x278` | `64` | `W` |
| `Arg1` | `+ 0x2A0` | `64` | `R` |
| `Arg1` | `+ 0x2A0` | `64` | `W` |
| `Arg1` | `+ 0x2C0` | `64` | `R` |
| `Arg1` | `+ 0x2E8` | `64` | `R` |
| `Arg1` | `+ 0x2F8` | `64` | `R` |
| `Arg1` | `+ 0x308` | `64` | `R` |
| `Arg1` | `+ 0x308` | `64` | `W` |
| `Arg1` | `+ 0x310` | `64` | `R` |
| `Arg1` | `+ 0x310` | `64` | `W` |
| `Arg1` | `+ 0x348` | `64` | `R` |
| `Arg1` | `+ 0x348` | `64` | `W` |
| `Arg1` | `+ 0x350` | `64` | `R` |
| `Arg1` | `+ 0x350` | `64` | `W` |
| `Arg1` | `+ 0x5E8` | `64` | `R` |
| `Arg1` | `+ 0x5F0` | `64` | `W` |
| `Arg1` | `+ 0x5FC` | `32` | `R` |
| `Arg1` | `+ 0x640` | `64` | `R` |

추가 오프셋 5개는 표에서 생략했습니다.

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00907B90&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
