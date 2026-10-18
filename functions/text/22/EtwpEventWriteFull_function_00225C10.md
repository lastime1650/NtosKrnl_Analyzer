# EtwpEventWriteFull

- RVA: `0x00225C10`–`0x0022785C` (길이 `7,244` bytes)
- VA: `0x0000000140225C10`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005FB00`
- 디코드: `1,465`개 명령, `7,244/7,244` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **67**; 고유 호출 대상: **38**
- 직접 호출자로 확인된 함수: **8**
- RIP 상대 이미지 참조: **11**

### Outgoing calls
- `0x00225D2C` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00225D9B` → [PsGetCurrentServerSiloGlobals](../2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (function, `0x002FE1F0`)
- `0x00225E15` → [DecodeProviderTraits](../3F/DecodeProviderTraits_function_003FD9D0.md) (function, `0x003FD9D0`)
- `0x00225E8E` → [KeGetEffectiveIrql](../2F/KeGetEffectiveIrql_function_002F8030.md) (function, `0x002F8030`)
- `0x00225FDB` → [EtwpLevelKeywordEnabled](../2F/EtwpLevelKeywordEnabled_function_002FD110.md) (function, `0x002FD110`)
- `0x0022609B` → [EtwpApplyEventIdPayloadFilter](../3F/EtwpApplyEventIdPayloadFilter_function_003F41A0.md) (function, `0x003F41A0`)
- `0x002260E4` → [EtwpIsEventNameFilterEnabled](../3F/EtwpIsEventNameFilterEnabled_function_003F1414.md) (function, `0x003F1414`)
- `0x00226131` → [EtwpApplyEventNameFilter](../3F/EtwpApplyEventNameFilter_function_003F10B8.md) (function, `0x003F10B8`)
- `0x00226177` → [ExAcquireRundownProtectionCacheAwareEx](../41/ExAcquireRundownProtectionCacheAwareEx_function_00411F50.md) (function, `0x00411F50`)
- `0x0022621F` → [ExReleaseRundownProtectionCacheAwareEx](../25/ExReleaseRundownProtectionCacheAwareEx_function_0025F050.md) (function, `0x0025F050`)
- `0x00226224` → [Feature_1345841464__private_IsEnabledDeviceUsageNoInline](../4E/Feature_1345841464__private_IsEnabledDeviceUsageNoInline_function_004EF340.md) (function, `0x004EF340`)
- `0x002262B3` → [MmCanThreadFault](../2F/MmCanThreadFault_function_002F86B0.md) (function, `0x002F86B0`)
- `0x0022635D` → [ExpInterlockedPopEntrySList](../6B/ExpInterlockedPopEntrySList_function_006BA570.md) (function, `0x006BA570`)
- `0x00226384` → [ExpInterlockedPopEntrySList](../6B/ExpInterlockedPopEntrySList_function_006BA570.md) (function, `0x006BA570`)
- `0x002263AB` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x002263D3` → [EtwpGetSidExtendedHeaderItem](../../page/9A/EtwpGetSidExtendedHeaderItem_function_009A8D80.md) (function, `0x009A8D80`)
- `0x00226417` → [KeGetEffectiveIrql](../2F/KeGetEffectiveIrql_function_002F8030.md) (function, `0x002F8030`)
- `0x002264F4` → [EtwpApplyLevelKwFilter](../46/EtwpApplyLevelKwFilter_function_00464740.md) (function, `0x00464740`)
- `0x00226520` → [EtwpApplyStackWalkIdFilter](../41/EtwpApplyStackWalkIdFilter_function_0041C0A8.md) (function, `0x0041C0A8`)
- `0x00226571` → [EtwpApplyEventNameFilter](../3F/EtwpApplyEventNameFilter_function_003F10B8.md) (function, `0x003F10B8`)
- `0x00226587` → [EtwpGetStackLookasideListEntry](../44/EtwpGetStackLookasideListEntry_function_004468F0.md) (function, `0x004468F0`)
- `0x0022662A` → [EtwpGetStackExtendedHeaderItem](../44/EtwpGetStackExtendedHeaderItem_function_00443D70.md) (function, `0x00443D70`)
- `0x0022663B` → [EtwpReleaseStackLookasideListEntry](../41/EtwpReleaseStackLookasideListEntry_function_0041D770.md) (function, `0x0041D770`)
- `0x0022667F` → [EtwpGetCrimsonStackKey](../4D/EtwpGetCrimsonStackKey_function_004D68CC.md) (function, `0x004D68CC`)
- `0x002266D8` → [Feature_1345841464__private_IsEnabledDeviceUsageNoInline](../4E/Feature_1345841464__private_IsEnabledDeviceUsageNoInline_function_004EF340.md) (function, `0x004EF340`)
- `0x00226722` → [Feature_1345841464__private_IsEnabledDeviceUsageNoInline](../4E/Feature_1345841464__private_IsEnabledDeviceUsageNoInline_function_004EF340.md) (function, `0x004EF340`)
- `0x00226776` → [Feature_1345841464__private_IsEnabledDeviceUsageNoInline](../4E/Feature_1345841464__private_IsEnabledDeviceUsageNoInline_function_004EF340.md) (function, `0x004EF340`)
- `0x002267A6` → [Feature_1345841464__private_IsEnabledDeviceUsageNoInline](../4E/Feature_1345841464__private_IsEnabledDeviceUsageNoInline_function_004EF340.md) (function, `0x004EF340`)
- `0x002267EB` → [Feature_1345841464__private_IsEnabledDeviceUsageNoInline](../4E/Feature_1345841464__private_IsEnabledDeviceUsageNoInline_function_004EF340.md) (function, `0x004EF340`)
- `0x0022680F` → [EtwpDereferenceStackEntry](../3F/EtwpDereferenceStackEntry_function_003FC9D0.md) (function, `0x003FC9D0`)
- `0x0022683C` → [ExReleaseRundownProtectionCacheAwareEx](../25/ExReleaseRundownProtectionCacheAwareEx_function_0025F050.md) (function, `0x0025F050`)
- `0x00226894` → [Feature_Servicing_EtwLostEventsFlags__private_IsEnabledDeviceUsageNoInline](../45/Feature_Servicing_EtwLostEventsFlags__private_IsEnabledDeviceUsageNoInline_function_004501F8.md) (function, `0x004501F8`)
- `0x002268E4` → [EtwpReserveTraceBuffer](../2F/EtwpReserveTraceBuffer_function_002FC8C0.md) (function, `0x002FC8C0`)
- `0x00226913` → [EtwpDereferenceStackEntry](../3F/EtwpDereferenceStackEntry_function_003FC9D0.md) (function, `0x003FC9D0`)
- `0x00226918` → [Feature_1345841464__private_IsEnabledDeviceUsageNoInline](../4E/Feature_1345841464__private_IsEnabledDeviceUsageNoInline_function_004EF340.md) (function, `0x004EF340`)
- `0x00226942` → [EtwpGetReserveTraceBufferStatus](../44/EtwpGetReserveTraceBufferStatus_function_00446430.md) (function, `0x00446430`)
- `0x00226975` → [EtwEventEnabled](../39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x002269C0` → [EtwpTraceLostEvent](../3F/EtwpTraceLostEvent_function_003F0D58.md) (function, `0x003F0D58`)
- `0x00226A0F` → [ExReleaseRundownProtectionCacheAwareEx](../25/ExReleaseRundownProtectionCacheAwareEx_function_0025F050.md) (function, `0x0025F050`)
- `0x00226A14` → [Feature_1345841464__private_IsEnabledDeviceUsageNoInline](../4E/Feature_1345841464__private_IsEnabledDeviceUsageNoInline_function_004EF340.md) (function, `0x004EF340`)
- `0x00226AA1` → [Feature_1345841464__private_IsEnabledDeviceUsageNoInline](../4E/Feature_1345841464__private_IsEnabledDeviceUsageNoInline_function_004EF340.md) (function, `0x004EF340`)
- `0x00226C2F` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00226C4C` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00226D13` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00226D79` → [PsGetCurrentProcessSessionId](../23/PsGetCurrentProcessSessionId_function_002303D0.md) (function, `0x002303D0`)
- `0x00226F0D` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00226F3C` → [EtwpQueueStackWalkApc](../20/EtwpQueueStackWalkApc_function_00203AA0.md) (function, `0x00203AA0`)
- `0x00227061` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00227073` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x002270AD` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00227205` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x002273C3` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x002273E4` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x002274F8` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0022751E` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00227638` → [EtwpSendTraceEvent](../4B/EtwpSendTraceEvent_function_004B6E10.md) (function, `0x004B6E10`)
- `0x00227660` → [EtwpInvokeEventCallback](../4B/EtwpInvokeEventCallback_function_004B6F0C.md) (function, `0x004B6F0C`)
- `0x002276C2` → [EtwpReleaseStackLookasideListEntry](../41/EtwpReleaseStackLookasideListEntry_function_0041D770.md) (function, `0x0041D770`)
- `0x002276F2` → [EtwpReleaseTraceBuffer](../3F/EtwpReleaseTraceBuffer_function_003F0D20.md) (function, `0x003F0D20`)
- `0x00227710` → [ExReleaseRundownProtectionCacheAwareEx](../25/ExReleaseRundownProtectionCacheAwareEx_function_0025F050.md) (function, `0x0025F050`)
- `0x00227787` → [EtwpFailLogging](../3F/EtwpFailLogging_function_003F0A50.md) (function, `0x003F0A50`)
- `0x0022779E` → [KiLeaveCriticalRegionUnsafe](../25/KiLeaveCriticalRegionUnsafe_function_0025F010.md) (function, `0x0025F010`)
- `0x002277F0` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x002277FA` → [ExpInterlockedPushEntrySList](../6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (function, `0x006BA5B0`)
- `0x0022780D` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x0022783B` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00227856` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)

### Direct callers
- [EtwpDiskProvTraceDisk](EtwpDiskProvTraceDisk_function_00225A1C.md) at `0x00225B30`
- [EtwWriteKMSecurityEvent](EtwWriteKMSecurityEvent_function_00225B8C.md) at `0x00225BF9`
- [EtwpStackWalkApc](EtwpStackWalkApc_function_00227870.md) at `0x002279F9`
- [sub_0025F1D2](../25/Unknown_function_0025F1D2.md) at `0x0025F283`
- [sub_0025F1D2](../25/Unknown_function_0025F1D2.md) at `0x0025F311`
- [sub_0025F1D2](../25/Unknown_function_0025F1D2.md) at `0x0025F406`
- [sub_0025F1D2](../25/Unknown_function_0025F1D2.md) at `0x0025F4BB`
- [EtwpApcPoolThunk](../2F/EtwpApcPoolThunk_function_002FA090.md) at `0x002FA373`
- [sub_006D6BDE](../6D/Unknown_function_006D6BDE.md) at `0x006D6C61`
- [sub_006D6BDE](../6D/Unknown_function_006D6BDE.md) at `0x006D6D0B`
- [sub_006D6BDE](../6D/Unknown_function_006D6BDE.md) at `0x006D6DB3`
- [sub_006FB552](../6F/Unknown_function_006FB552.md) at `0x006FB5CF`
- [sub_006FB552](../6F/Unknown_function_006FB552.md) at `0x006FB66C`
- [sub_006FB552](../6F/Unknown_function_006FB552.md) at `0x006FB71C`
- [sub_006FB552](../6F/Unknown_function_006FB552.md) at `0x006FB7CF`
- [EtwWriteErrorLogEntry](../../page/A5/EtwWriteErrorLogEntry_function_00A5E030.md) at `0x00A5E34F`

### Static image references
- `0x00225C23` → RVA `0x00E0A740` (`.data`; read)
- `0x002262A0` → RVA `0x00EFF285` (`.data`; read)
- `0x002262FD` → RVA `0x00FC6AA8` (`ALMOSTRO`; read)
- `0x002265DA` → RVA `0x00013050` (`.rdata`; read)
- `0x002265E7` → RVA `0x00013058` (`.rdata`; read)
- `0x00226967` → RVA `0x00013040` (`.rdata`; read)
- `0x0022696E` → RVA `0x00EFF840` (`.data`; read)
- `0x00226B51` → RVA `0x000112D0` (`.rdata`; read)
- `0x00227612` → RVA `0x00F475DC` (`.data`; read)
- `0x0022761B` → RVA `0x00E0AA1C` (`.data`; read)
- `0x00227624` → RVA `0x00F55CB3` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x002263D3` → [EtwpGetSidExtendedHeaderItem](../../page/9A/EtwpGetSidExtendedHeaderItem_function_009A8D80.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00225C10  40 53                           push rbx
00225C12  56                              push rsi
00225C13  57                              push rdi
00225C14  41 54                           push r12
00225C16  41 55                           push r13
00225C18  41 56                           push r14
00225C1A  41 57                           push r15
00225C1C  48 81 EC 40 05 00 00            sub rsp, 0x540
00225C23  48 8B 05 16 4B BE 00            mov rax, qword ptr [rip + 0xbe4b16]
00225C2A  48 33 C4                        xor rax, rsp
00225C2D  48 89 84 24 30 05 00 00         mov qword ptr [rsp + 0x530], rax
00225C35  44 89 8C 24 8C 00 00 00         mov dword ptr [rsp + 0x8c], r9d
00225C3D  49 8B D8                        mov rbx, r8
00225C40  0F B7 F2                        movzx esi, dx
00225C43  48 89 8C 24 08 01 00 00         mov qword ptr [rsp + 0x108], rcx
00225C4B  48 8B 94 24 D0 05 00 00         mov rdx, qword ptr [rsp + 0x5d0]
00225C53  48 89 94 24 00 01 00 00         mov qword ptr [rsp + 0x100], rdx
00225C5B  48 89 94 24 10 02 00 00         mov qword ptr [rsp + 0x210], rdx
00225C63  8B 84 24 C8 05 00 00            mov eax, dword ptr [rsp + 0x5c8]
00225C6A  89 84 24 B0 01 00 00            mov dword ptr [rsp + 0x1b0], eax
00225C71  48 8B 84 24 C0 05 00 00         mov rax, qword ptr [rsp + 0x5c0]
00225C79  48 89 84 24 08 02 00 00         mov qword ptr [rsp + 0x208], rax
00225C81  48 8B BC 24 E8 05 00 00         mov rdi, qword ptr [rsp + 0x5e8]
00225C89  0F B7 84 24 A8 05 00 00         movzx eax, word ptr [rsp + 0x5a8]
00225C91  66 89 84 24 40 01 00 00         mov word ptr [rsp + 0x140], ax
00225C99  48 89 8C 24 98 01 00 00         mov qword ptr [rsp + 0x198], rcx
00225CA1  44 89 8C 24 18 01 00 00         mov dword ptr [rsp + 0x118], r9d
00225CA9  44 89 8C 24 D8 01 00 00         mov dword ptr [rsp + 0x1d8], r9d
00225CB1  48 8B 84 24 A0 05 00 00         mov rax, qword ptr [rsp + 0x5a0]
00225CB9  48 89 84 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rax
00225CC1  48 89 94 24 A0 01 00 00         mov qword ptr [rsp + 0x1a0], rdx
00225CC9  48 8B 84 24 D8 05 00 00         mov rax, qword ptr [rsp + 0x5d8]
00225CD1  48 89 84 24 28 01 00 00         mov qword ptr [rsp + 0x128], rax
00225CD9  48 8B 84 24 E0 05 00 00         mov rax, qword ptr [rsp + 0x5e0]
00225CE1  48 89 84 24 F8 00 00 00         mov qword ptr [rsp + 0xf8], rax
00225CE9  48 8B 84 24 F8 05 00 00         mov rax, qword ptr [rsp + 0x5f8]
00225CF1  48 89 84 24 E0 01 00 00         mov qword ptr [rsp + 0x1e0], rax
00225CF9  48 8B 84 24 00 06 00 00         mov rax, qword ptr [rsp + 0x600]
00225D01  48 89 84 24 58 01 00 00         mov qword ptr [rsp + 0x158], rax
00225D09  45 33 FF                        xor r15d, r15d
00225D0C  45 8B F7                        mov r14d, r15d
00225D0F  44 89 7C 24 70                  mov dword ptr [rsp + 0x70], r15d
00225D14  44 89 BC 24 E0 00 00 00         mov dword ptr [rsp + 0xe0], r15d
00225D1C  33 D2                           xor edx, edx
00225D1E  41 B8 08 03 00 00               mov r8d, 0x308
00225D24  48 8D 8C 24 20 02 00 00         lea rcx, [rsp + 0x220]
00225D2C  E8 0F 0F 4A 00                  call 0x1406c6c40
00225D31  44 89 BC 24 88 00 00 00         mov dword ptr [rsp + 0x88], r15d
00225D39  41 8B C7                        mov eax, r15d
00225D3C  48 89 84 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], rax
00225D44  48 89 84 24 68 01 00 00         mov qword ptr [rsp + 0x168], rax
00225D4C  4C 89 BC 24 50 01 00 00         mov qword ptr [rsp + 0x150], r15
00225D54  4C 89 BC 24 C8 01 00 00         mov qword ptr [rsp + 0x1c8], r15
00225D5C  4C 89 BC 24 C0 01 00 00         mov qword ptr [rsp + 0x1c0], r15
00225D64  66 44 89 BC 24 90 00 00 00      mov word ptr [rsp + 0x90], r15w
00225D6D  4C 89 BC 24 78 01 00 00         mov qword ptr [rsp + 0x178], r15
00225D75  0F B7 94 24 F0 05 00 00         movzx edx, word ptr [rsp + 0x5f0]
00225D7D  0F B7 C2                        movzx eax, dx
00225D80  B9 00 01 00 00                  mov ecx, 0x100
00225D85  66 23 C1                        and ax, cx
00225D88  66 89 84 24 C8 00 00 00         mov word ptr [rsp + 0xc8], ax
00225D90  66 C1 EA 09                     shr dx, 9
00225D94  45 8D 67 01                     lea r12d, [r15 + 1]
00225D98  41 22 D4                        and dl, r12b
00225D9B  E8 50 84 0D 00                  call 0x1402fe1f0
00225DA0  48 8B 80 40 03 00 00            mov rax, qword ptr [rax + 0x340]
00225DA7  48 89 84 24 48 01 00 00         mov qword ptr [rsp + 0x148], rax
00225DAF  48 89 84 24 90 01 00 00         mov qword ptr [rsp + 0x190], rax
00225DB7  44 88 7C 24 74                  mov byte ptr [rsp + 0x74], r15b
00225DBC  45 8B EC                        mov r13d, r12d
00225DBF  4C 89 BC 24 60 01 00 00         mov qword ptr [rsp + 0x160], r15
00225DC7  44 89 BC 24 A0 00 00 00         mov dword ptr [rsp + 0xa0], r15d
00225DCF  81 BC 24 C8 05 00 00 80 00 00 00  cmp dword ptr [rsp + 0x5c8], 0x80
00225DDA  76 0A                           jbe 0x140225de6
00225DDC  B8 0D 00 00 C0                  mov eax, 0xc000000d
00225DE1  E9 1C 1A 00 00                  jmp 0x140227802
00225DE6  48 85 FF                        test rdi, rdi
00225DE9  4C 8B 94 24 08 01 00 00         mov r10, qword ptr [rsp + 0x108]
00225DF1  49 0F 44 FA                     cmove rdi, r10
00225DF5  48 89 BC 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], rdi
00225DFD  4C 8D 8C 24 78 01 00 00         lea r9, [rsp + 0x178]
00225E05  4C 8D 84 24 90 00 00 00         lea r8, [rsp + 0x90]
00225E0D  48 8B 8C 24 E0 01 00 00         mov rcx, qword ptr [rsp + 0x1e0]
00225E15  E8 B6 7B 1D 00                  call 0x1403fd9d0
00225E1A  41 8A FF                        mov dil, r15b
00225E1D  44 88 7C 24 60                  mov byte ptr [rsp + 0x60], r15b
00225E22  49 8B 82 88 02 00 00            mov rax, qword ptr [r10 + 0x288]
00225E29  48 89 84 24 F0 00 00 00         mov qword ptr [rsp + 0xf0], rax
00225E31  48 89 84 24 88 01 00 00         mov qword ptr [rsp + 0x188], rax
00225E39  48 8B 84 24 58 01 00 00         mov rax, qword ptr [rsp + 0x158]
00225E41  48 85 C0                        test rax, rax
00225E44  74 18                           je 0x140225e5e
00225E46  48 8B 00                        mov rax, qword ptr [rax]
00225E49  48 85 C0                        test rax, rax
00225E4C  74 10                           je 0x140225e5e
00225E4E  48 89 84 24 C0 01 00 00         mov qword ptr [rsp + 0x1c0], rax
00225E56  40 B7 04                        mov dil, 4
00225E59  40 88 7C 24 60                  mov byte ptr [rsp + 0x60], dil
00225E5E  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00225E67  48 89 8C 24 D0 01 00 00         mov qword ptr [rsp + 0x1d0], rcx
00225E6F  48 8B 84 24 28 01 00 00         mov rax, qword ptr [rsp + 0x128]
00225E77  48 85 C0                        test rax, rax
00225E7A  48 0F 44 C1                     cmove rax, rcx
00225E7E  48 89 84 24 28 01 00 00         mov qword ptr [rsp + 0x128], rax
00225E86  48 89 84 24 A8 01 00 00         mov qword ptr [rsp + 0x1a8], rax
00225E8E  E8 9D 21 0D 00                  call 0x1402f8030
00225E93  88 44 24 61                     mov byte ptr [rsp + 0x61], al
00225E97  88 44 24 69                     mov byte ptr [rsp + 0x69], al
00225E9B  44 88 BC 24 80 00 00 00         mov byte ptr [rsp + 0x80], r15b
00225EA3  41 3A C4                        cmp al, r12b
00225EA6  73 18                           jae 0x140225ec0
00225EA8  48 8B 84 24 D0 01 00 00         mov rax, qword ptr [rsp + 0x1d0]
00225EB0  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00225EB7  90                              nop
00225EB8  44 88 A4 24 80 00 00 00         mov byte ptr [rsp + 0x80], r12b
00225EC0  66 F7 D3                        not bx
00225EC3  66 23 F3                        and si, bx
00225EC6  89 B4 24 84 00 00 00            mov dword ptr [rsp + 0x84], esi
00225ECD  4C 8B 84 24 F8 00 00 00         mov r8, qword ptr [rsp + 0xf8]
00225ED5  4C 8B 9C 24 D0 00 00 00         mov r11, qword ptr [rsp + 0xd0]
00225EDD  4C 8B 94 24 B0 00 00 00         mov r10, qword ptr [rsp + 0xb0]
00225EE5  8B 9C 24 84 00 00 00            mov ebx, dword ptr [rsp + 0x84]
00225EEC  0F B7 C3                        movzx eax, bx
00225EEF  0F BC C8                        bsf ecx, eax
00225EF2  89 8C 24 88 00 00 00            mov dword ptr [rsp + 0x88], ecx
00225EF9  0F 84 EC 08 00 00               je 0x1402267eb
00225EFF  0F 57 C0                        xorps xmm0, xmm0
00225F02  33 C0                           xor eax, eax
00225F04  0F 11 84 24 F0 01 00 00         movups xmmword ptr [rsp + 0x1f0], xmm0
00225F0C  48 89 84 24 00 02 00 00         mov qword ptr [rsp + 0x200], rax
00225F14  4C 89 BC 24 B8 01 00 00         mov qword ptr [rsp + 0x1b8], r15
00225F1C  C7 44 24 64 50 00 00 00         mov dword ptr [rsp + 0x64], 0x50
00225F24  49 8B C7                        mov rax, r15
00225F27  48 89 84 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rax
00225F2F  48 89 84 24 20 01 00 00         mov qword ptr [rsp + 0x120], rax
00225F37  44 89 7C 24 78                  mov dword ptr [rsp + 0x78], r15d
00225F3C  44 89 7C 24 7C                  mov dword ptr [rsp + 0x7c], r15d
00225F41  4C 89 BC 24 80 01 00 00         mov qword ptr [rsp + 0x180], r15
00225F49  4C 89 BC 24 E8 01 00 00         mov qword ptr [rsp + 0x1e8], r15
00225F51  41 8A F7                        mov sil, r15b
00225F54  89 74 24 74                     mov dword ptr [rsp + 0x74], esi
00225F58  4D 8B EC                        mov r13, r12
00225F5B  4C 89 A4 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], r12
00225F63  4C 89 A4 24 30 01 00 00         mov qword ptr [rsp + 0x130], r12
00225F6B  4C 89 BC 24 60 01 00 00         mov qword ptr [rsp + 0x160], r15
00225F73  0F B7 C3                        movzx eax, bx
00225F76  66 41 2B C4                     sub ax, r12w
00225F7A  66 23 D8                        and bx, ax
00225F7D  89 9C 24 84 00 00 00            mov dword ptr [rsp + 0x84], ebx
00225F84  66 89 9C 24 98 00 00 00         mov word ptr [rsp + 0x98], bx
00225F8C  44 8B C9                        mov r9d, ecx
00225F8F  48 8D 59 04                     lea rbx, [rcx + 4]
00225F93  48 C1 E3 05                     shl rbx, 5
00225F97  49 03 DB                        add rbx, r11
00225F9A  48 89 9C 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rbx
00225FA2  4D 85 C0                        test r8, r8
00225FA5  74 29                           je 0x140225fd0
00225FA7  0F B7 43 06                     movzx eax, word ptr [rbx + 6]
00225FAB  8B C8                           mov ecx, eax
00225FAD  C1 E9 05                        shr ecx, 5
00225FB0  25 1F 00 00 80                  and eax, 0x8000001f
00225FB5  7D 09                           jge 0x140225fc0
00225FB7  41 2B C4                        sub eax, r12d
00225FBA  83 C8 E0                        or eax, 0xffffffe0
00225FBD  41 03 C4                        add eax, r12d
00225FC0  0F B6 D0                        movzx edx, al
00225FC3  41 8B 0C 88                     mov ecx, dword ptr [r8 + rcx*4]
00225FC7  0F A3 D1                        bt ecx, edx
00225FCA  0F 82 15 FF FF FF               jb 0x140225ee5
00225FD0  4D 8B 42 08                     mov r8, qword ptr [r10 + 8]
00225FD4  41 8A 52 04                     mov dl, byte ptr [r10 + 4]
00225FD8  48 8B CB                        mov rcx, rbx
00225FDB  E8 30 71 0D 00                  call 0x1402fd110
00225FE0  84 C0                           test al, al
00225FE2  4C 8B 84 24 F8 00 00 00         mov r8, qword ptr [rsp + 0xf8]
00225FEA  0F 84 F5 FE FF FF               je 0x140225ee5
00225FF0  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00225FF9  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00226000  F6 84 24 8C 00 00 00 02         test byte ptr [rsp + 0x8c], 2
00226008  75 09                           jne 0x140226013
0022600A  44 39 B9 F0 01 00 00            cmp dword ptr [rcx + 0x1f0], r15d
00226011  7D 0D                           jge 0x140226020
00226013  F7 43 08 00 02 00 00            test dword ptr [rbx + 8], 0x200
0022601A  0F 85 C5 FE FF FF               jne 0x140225ee5
00226020  49 8B 8B 80 02 00 00            mov rcx, qword ptr [r11 + 0x280]
00226027  48 85 C9                        test rcx, rcx
0022602A  74 28                           je 0x140226054
0022602C  49 6B C1 68                     imul rax, r9, 0x68
00226030  8B 0C 08                        mov ecx, dword ptr [rax + rcx]
00226033  8B C1                           mov eax, ecx
00226035  25 00 02 00 80                  and eax, 0x80000200
0022603A  3D 00 02 00 80                  cmp eax, 0x80000200
0022603F  74 0E                           je 0x14022604f
00226041  81 E1 00 01 00 80               and ecx, 0x80000100
00226047  81 F9 00 01 00 80               cmp ecx, 0x80000100
0022604D  75 05                           jne 0x140226054
0022604F  41 8A C4                        mov al, r12b
00226052  EB 03                           jmp 0x140226057
00226054  41 8A C7                        mov al, r15b
00226057  40 8A 74 24 61                  mov sil, byte ptr [rsp + 0x61]
0022605C  84 C0                           test al, al
0022605E  74 58                           je 0x1402260b8
00226060  45 33 C0                        xor r8d, r8d
00226063  40 88 74 24 40                  mov byte ptr [rsp + 0x40], sil
00226068  44 88 7C 24 38                  mov byte ptr [rsp + 0x38], r15b
0022606D  48 8B 84 24 00 01 00 00         mov rax, qword ptr [rsp + 0x100]
00226075  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0022607A  8B 84 24 C8 05 00 00            mov eax, dword ptr [rsp + 0x5c8]
00226081  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
00226085  41 0F B7 02                     movzx eax, word ptr [r10]
00226089  66 89 44 24 20                  mov word ptr [rsp + 0x20], ax
0022608E  4D 8B CA                        mov r9, r10
00226091  8B 94 24 88 00 00 00            mov edx, dword ptr [rsp + 0x88]
00226098  49 8B CB                        mov rcx, r11
0022609B  E8 00 E1 1C 00                  call 0x1403f41a0
002260A0  84 C0                           test al, al
002260A2  0F 84 25 FE FF FF               je 0x140225ecd
002260A8  4C 8B 94 24 B0 00 00 00         mov r10, qword ptr [rsp + 0xb0]
002260B0  4C 8B 9C 24 D0 00 00 00         mov r11, qword ptr [rsp + 0xd0]
002260B8  66 44 39 BC 24 C8 00 00 00      cmp word ptr [rsp + 0xc8], r15w
002260C1  74 7B                           je 0x14022613e
002260C3  44 88 7C 24 28                  mov byte ptr [rsp + 0x28], r15b
002260C8  49 8B 42 08                     mov rax, qword ptr [r10 + 8]
002260CC  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
002260D1  45 8A 4A 04                     mov r9b, byte ptr [r10 + 4]
002260D5  44 8A C6                        mov r8b, sil
002260D8  8B B4 24 88 00 00 00            mov esi, dword ptr [rsp + 0x88]
002260DF  8B D6                           mov edx, esi
002260E1  49 8B CB                        mov rcx, r11
002260E4  E8 2B B3 1C 00                  call 0x1403f1414
002260E9  84 C0                           test al, al
002260EB  74 51                           je 0x14022613e
002260ED  44 88 7C 24 40                  mov byte ptr [rsp + 0x40], r15b
002260F2  48 8B 8C 24 B0 00 00 00         mov rcx, qword ptr [rsp + 0xb0]
002260FA  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
002260FE  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00226103  8A 41 04                        mov al, byte ptr [rcx + 4]
00226106  88 44 24 30                     mov byte ptr [rsp + 0x30], al
0022610A  8A 44 24 61                     mov al, byte ptr [rsp + 0x61]
0022610E  88 44 24 28                     mov byte ptr [rsp + 0x28], al
00226112  44 88 7C 24 20                  mov byte ptr [rsp + 0x20], r15b
00226117  4C 8B 8C 24 00 01 00 00         mov r9, qword ptr [rsp + 0x100]
0022611F  44 8B 84 24 C8 05 00 00         mov r8d, dword ptr [rsp + 0x5c8]
00226127  8B D6                           mov edx, esi
00226129  48 8B 8C 24 D0 00 00 00         mov rcx, qword ptr [rsp + 0xd0]
00226131  E8 82 AF 1C 00                  call 0x1403f10b8
00226136  84 C0                           test al, al
00226138  0F 84 8F FD FF FF               je 0x140225ecd
0022613E  0F B7 43 06                     movzx eax, word ptr [rbx + 6]
00226142  89 84 24 A0 00 00 00            mov dword ptr [rsp + 0xa0], eax
00226149  89 84 24 10 01 00 00            mov dword ptr [rsp + 0x110], eax
00226150  8B D8                           mov ebx, eax
00226152  48 89 84 24 70 01 00 00         mov qword ptr [rsp + 0x170], rax
0022615A  48 8B B4 24 F0 00 00 00         mov rsi, qword ptr [rsp + 0xf0]
00226162  80 7C 24 61 02                  cmp byte ptr [rsp + 0x61], 2
00226167  73 57                           jae 0x1402261c0
00226169  48 8B 8E C0 02 00 00            mov rcx, qword ptr [rsi + 0x2c0]
00226170  41 8B D4                        mov edx, r12d
00226173  48 8B 0C C1                     mov rcx, qword ptr [rcx + rax*8]
00226177  E8 D4 BD 1E 00                  call 0x140411f50
0022617C  84 C0                           test al, al
0022617E  0F 84 81 00 00 00               je 0x140226205
00226184  3B 5E 10                        cmp ebx, dword ptr [rsi + 0x10]
00226187  73 20                           jae 0x1402261a9
00226189  0F AE E8                        lfence
0022618C  48 8B 86 C8 02 00 00            mov rax, qword ptr [rsi + 0x2c8]
00226193  4C 8B 2C D8                     mov r13, qword ptr [rax + rbx*8]
00226197  4C 89 AC 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], r13
0022619F  4C 89 AC 24 30 01 00 00         mov qword ptr [rsp + 0x130], r13
002261A7  EB 10                           jmp 0x1402261b9
002261A9  4C 89 A4 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], r12
002261B1  4C 89 A4 24 30 01 00 00         mov qword ptr [rsp + 0x130], r12
002261B9  44 88 64 24 74                  mov byte ptr [rsp + 0x74], r12b
002261BE  EB 45                           jmp 0x140226205
002261C0  48 89 9C 24 70 01 00 00         mov qword ptr [rsp + 0x170], rbx
002261C8  3B 46 10                        cmp eax, dword ptr [rsi + 0x10]
002261CB  73 20                           jae 0x1402261ed
002261CD  0F AE E8                        lfence
002261D0  48 8B 86 C8 02 00 00            mov rax, qword ptr [rsi + 0x2c8]
002261D7  4C 8B 2C D8                     mov r13, qword ptr [rax + rbx*8]
002261DB  4C 89 AC 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], r13
002261E3  4C 89 AC 24 30 01 00 00         mov qword ptr [rsp + 0x130], r13
002261EB  EB 18                           jmp 0x140226205
002261ED  4C 89 A4 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], r12
002261F5  4C 89 A4 24 30 01 00 00         mov qword ptr [rsp + 0x130], r12
002261FD  48 89 9C 24 70 01 00 00         mov qword ptr [rsp + 0x170], rbx
00226205  45 84 EC                        test r12b, r13b
00226208  74 5C                           je 0x140226266
0022620A  44 38 7C 24 74                  cmp byte ptr [rsp + 0x74], r15b
0022620F  74 29                           je 0x14022623a
00226211  48 8B 8E C0 02 00 00            mov rcx, qword ptr [rsi + 0x2c0]
00226218  41 8B D4                        mov edx, r12d
0022621B  48 8B 0C D9                     mov rcx, qword ptr [rcx + rbx*8]
0022621F  E8 2C 8E 03 00                  call 0x14025f050
00226224  E8 17 91 2C 00                  call 0x1404ef340
00226229  8B 4C 24 74                     mov ecx, dword ptr [rsp + 0x74]
0022622D  0F B6 C9                        movzx ecx, cl
00226230  85 C0                           test eax, eax
00226232  41 0F 45 CF                     cmovne ecx, r15d
00226236  89 4C 24 74                     mov dword ptr [rsp + 0x74], ecx
0022623A  83 FB 03                        cmp ebx, 3
0022623D  0F 85 8A FC FF FF               jne 0x140225ecd
00226243  8B 86 F4 10 00 00               mov eax, dword ptr [rsi + 0x10f4]
00226249  F7 D8                           neg eax
0022624B  45 1B F6                        sbb r14d, r14d
0022624E  41 81 E6 F6 02 00 00            and r14d, 0x2f6
00226255  41 81 C6 08 00 00 C0            add r14d, 0xc0000008
0022625C  44 89 74 24 70                  mov dword ptr [rsp + 0x70], r14d
00226261  E9 E5 07 00 00                  jmp 0x140226a4b
00226266  48 8B 8C 24 08 02 00 00         mov rcx, qword ptr [rsp + 0x208]
0022626E  48 8B C1                        mov rax, rcx
00226271  48 F7 D8                        neg rax
00226274  1B DB                           sbb ebx, ebx
00226276  83 E3 10                        and ebx, 0x10
00226279  48 F7 D9                        neg rcx
0022627C  1B F6                           sbb esi, esi
0022627E  83 E6 18                        and esi, 0x18
00226281  83 C6 50                        add esi, 0x50
00226284  44 8B EE                        mov r13d, esi
00226287  89 74 24 6C                     mov dword ptr [rsp + 0x6c], esi
0022628B  48 8B 84 24 C0 00 00 00         mov rax, qword ptr [rsp + 0xc0]
00226293  F7 40 08 9F FF FF FF            test dword ptr [rax + 8], 0xffffff9f
0022629A  0F 84 FF 03 00 00               je 0x14022669f
002262A0  80 3D DE 8F CD 00 00            cmp byte ptr [rip + 0xcd8fde], 0
002262A7  75 29                           jne 0x1402262d2
002262A9  44 84 A4 24 8C 00 00 00         test byte ptr [rsp + 0x8c], r12b
002262B1  75 1F                           jne 0x1402262d2
002262B3  E8 F8 23 0D 00                  call 0x1402f86b0
002262B8  85 C0                           test eax, eax
002262BA  74 16                           je 0x1402262d2
002262BC  48 8B 84 24 D0 01 00 00         mov rax, qword ptr [rsp + 0x1d0]
002262C4  44 38 B8 AE 05 00 00            cmp byte ptr [rax + 0x5ae], r15b
002262CB  B8 00 01 00 00                  mov eax, 0x100
002262D0  74 03                           je 0x1402262d5
002262D2  41 8B C7                        mov eax, r15d
002262D5  0B D8                           or ebx, eax
002262D7  48 8B 84 24 C0 00 00 00         mov rax, qword ptr [rsp + 0xc0]
002262DF  8B 48 08                        mov ecx, dword ptr [rax + 8]
002262E2  89 74 24 6C                     mov dword ptr [rsp + 0x6c], esi
002262E6  0F BA E1 0B                     bt ecx, 0xb
002262EA  73 36                           jae 0x140226322
002262EC  48 8B 94 24 48 01 00 00         mov rdx, qword ptr [rsp + 0x148]
002262F4  48 85 D2                        test rdx, rdx
002262F7  74 29                           je 0x140226322
002262F9  89 74 24 6C                     mov dword ptr [rsp + 0x6c], esi
002262FD  48 3B 15 A4 07 DA 00            cmp rdx, qword ptr [rip + 0xda07a4]
00226304  74 1C                           je 0x140226322
00226306  0F BA EB 09                     bts ebx, 9
0022630A  44 0F B7 AA 90 11 00 00         movzx r13d, word ptr [rdx + 0x1190]
00226312  41 83 C5 0F                     add r13d, 0xf
00226316  41 83 E5 F8                     and r13d, 0xfffffff8
0022631A  44 03 EE                        add r13d, esi
0022631D  44 89 6C 24 6C                  mov dword ptr [rsp + 0x6c], r13d
00226322  41 84 CC                        test r12b, cl
00226325  0F 84 CD 00 00 00               je 0x1402263f8
0022632B  0F BA E3 08                     bt ebx, 8
0022632F  0F 83 C3 00 00 00               jae 0x1402263f8
00226335  48 8B 8C 24 D8 00 00 00         mov rcx, qword ptr [rsp + 0xd8]
0022633D  48 85 C9                        test rcx, rcx
00226340  0F 85 A4 00 00 00               jne 0x1402263ea
00226346  65 4C 8B 34 25 20 00 00 00      mov r14, qword ptr gs:[0x20]
0022634F  49 8B B6 80 08 00 00            mov rsi, qword ptr [r14 + 0x880]
00226356  44 01 66 14                     add dword ptr [rsi + 0x14], r12d
0022635A  48 8B CE                        mov rcx, rsi
0022635D  E8 0E 42 49 00                  call 0x1406ba570
00226362  48 8B C8                        mov rcx, rax
00226365  48 89 84 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], rax
0022636D  48 85 C0                        test rax, rax
00226370  75 49                           jne 0x1402263bb
00226372  44 01 66 18                     add dword ptr [rsi + 0x18], r12d
00226376  49 8B B6 88 08 00 00            mov rsi, qword ptr [r14 + 0x888]
0022637D  44 01 66 14                     add dword ptr [rsi + 0x14], r12d
00226381  48 8B CE                        mov rcx, rsi
00226384  E8 E7 41 49 00                  call 0x1406ba570
00226389  48 8B C8                        mov rcx, rax
0022638C  48 89 84 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], rax
00226394  48 85 C0                        test rax, rax
00226397  75 22                           jne 0x1402263bb
00226399  44 01 66 18                     add dword ptr [rsi + 0x18], r12d
0022639D  8B 56 2C                        mov edx, dword ptr [rsi + 0x2c]
002263A0  48 8B 46 30                     mov rax, qword ptr [rsi + 0x30]
002263A4  44 8B 46 28                     mov r8d, dword ptr [rsi + 0x28]
002263A8  8B 4E 24                        mov ecx, dword ptr [rsi + 0x24]
002263AB  E8 20 47 49 00                  call 0x1406baad0
002263B0  48 8B C8                        mov rcx, rax
002263B3  48 89 84 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], rax
002263BB  48 85 C9                        test rcx, rcx
002263BE  74 06                           je 0x1402263c6
002263C0  41 8B 46 24                     mov eax, dword ptr [r14 + 0x24]
002263C4  89 01                           mov dword ptr [rcx], eax
002263C6  48 89 8C 24 68 01 00 00         mov qword ptr [rsp + 0x168], rcx
002263CE  48 85 C9                        test rcx, rcx
002263D1  74 0D                           je 0x1402263e0
002263D3  E8 A8 29 78 00                  call 0x1409a8d80
002263D8  48 8B 8C 24 D8 00 00 00         mov rcx, qword ptr [rsp + 0xd8]
002263E0  44 8B 74 24 70                  mov r14d, dword ptr [rsp + 0x70]
002263E5  48 85 C9                        test rcx, rcx
002263E8  74 0E                           je 0x1402263f8
002263EA  83 CB 02                        or ebx, 2
002263ED  0F B7 01                        movzx eax, word ptr [rcx]
002263F0  44 03 E8                        add r13d, eax
002263F3  44 89 6C 24 6C                  mov dword ptr [rsp + 0x6c], r13d
002263F8  48 8B B4 24 C0 00 00 00         mov rsi, qword ptr [rsp + 0xc0]
00226400  8B 46 08                        mov eax, dword ptr [rsi + 8]
00226403  A8 02                           test al, 2
00226405  74 0C                           je 0x140226413
00226407  41 0B DC                        or ebx, r12d
0022640A  41 83 C5 10                     add r13d, 0x10
0022640E  44 89 6C 24 6C                  mov dword ptr [rsp + 0x6c], r13d
00226413  84 C0                           test al, al
00226415  79 2E                           jns 0x140226445
00226417  E8 14 1C 0D 00                  call 0x1402f8030
0022641C  3C 02                           cmp al, 2
0022641E  72 12                           jb 0x140226432
00226420  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
00226429  44 38 78 20                     cmp byte ptr [rax + 0x20], r15b
0022642D  41 8A C4                        mov al, r12b
00226430  75 03                           jne 0x140226435
00226432  41 8A C7                        mov al, r15b
00226435  84 C0                           test al, al
00226437  75 0C                           jne 0x140226445
00226439  83 CB 40                        or ebx, 0x40
0022643C  41 83 C5 10                     add r13d, 0x10
00226440  44 89 6C 24 6C                  mov dword ptr [rsp + 0x6c], r13d
00226445  8B 46 08                        mov eax, dword ptr [rsi + 8]
00226448  0F BA E0 08                     bt eax, 8
0022644C  73 0D                           jae 0x14022645b
0022644E  0F BA EB 07                     bts ebx, 7
00226452  41 83 C5 10                     add r13d, 0x10
00226456  44 89 6C 24 6C                  mov dword ptr [rsp + 0x6c], r13d
0022645B  A8 04                           test al, 4
0022645D  0F 84 3C 02 00 00               je 0x14022669f
00226463  80 3D 1B 8E CD 00 00            cmp byte ptr [rip + 0xcd8e1b], 0
0022646A  0F 85 2F 02 00 00               jne 0x14022669f
00226470  4C 8B 94 24 D0 00 00 00         mov r10, qword ptr [rsp + 0xd0]
00226478  49 8B 92 80 02 00 00            mov rdx, qword ptr [r10 + 0x280]
0022647F  48 85 D2                        test rdx, rdx
00226482  74 3D                           je 0x1402264c1
00226484  8B 84 24 88 00 00 00            mov eax, dword ptr [rsp + 0x88]
0022648B  48 6B C8 68                     imul rcx, rax, 0x68
0022648F  8B 14 11                        mov edx, dword ptr [rcx + rdx]
00226492  8B C2                           mov eax, edx
00226494  25 00 10 00 80                  and eax, 0x80001000
00226499  3D 00 10 00 80                  cmp eax, 0x80001000
0022649E  74 1C                           je 0x1402264bc
002264A0  8B C2                           mov eax, edx
002264A2  25 00 20 00 80                  and eax, 0x80002000
002264A7  3D 00 20 00 80                  cmp eax, 0x80002000
002264AC  74 0E                           je 0x1402264bc
002264AE  81 E2 00 40 00 80               and edx, 0x80004000
002264B4  81 FA 00 40 00 80               cmp edx, 0x80004000
002264BA  75 05                           jne 0x1402264c1
002264BC  41 8A C4                        mov al, r12b
002264BF  EB 03                           jmp 0x1402264c4
002264C1  41 8A C7                        mov al, r15b
002264C4  84 C0                           test al, al
002264C6  0F 84 B2 00 00 00               je 0x14022657e
002264CC  80 7C 24 69 02                  cmp byte ptr [rsp + 0x69], 2
002264D1  0F 92 C0                        setb al
002264D4  88 44 24 20                     mov byte ptr [rsp + 0x20], al
002264D8  48 8B 84 24 B0 00 00 00         mov rax, qword ptr [rsp + 0xb0]
002264E0  4C 8B 48 08                     mov r9, qword ptr [rax + 8]
002264E4  44 8A 40 04                     mov r8b, byte ptr [rax + 4]
002264E8  8B B4 24 88 00 00 00            mov esi, dword ptr [rsp + 0x88]
002264EF  8B D6                           mov edx, esi
002264F1  49 8B CA                        mov rcx, r10
002264F4  E8 47 E2 23 00                  call 0x140464740
002264F9  84 C0                           test al, al
002264FB  0F 84 9E 01 00 00               je 0x14022669f
00226501  80 7C 24 69 02                  cmp byte ptr [rsp + 0x69], 2
00226506  41 0F 92 C1                     setb r9b
0022650A  44 8B C6                        mov r8d, esi
0022650D  48 8B 94 24 D0 00 00 00         mov rdx, qword ptr [rsp + 0xd0]
00226515  48 8B 84 24 B0 00 00 00         mov rax, qword ptr [rsp + 0xb0]
0022651D  0F B7 08                        movzx ecx, word ptr [rax]
00226520  E8 83 5B 1F 00                  call 0x14041c0a8
00226525  84 C0                           test al, al
00226527  0F 84 72 01 00 00               je 0x14022669f
0022652D  44 88 64 24 40                  mov byte ptr [rsp + 0x40], r12b
00226532  48 8B 8C 24 B0 00 00 00         mov rcx, qword ptr [rsp + 0xb0]
0022653A  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
0022653E  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00226543  8A 41 04                        mov al, byte ptr [rcx + 4]
00226546  88 44 24 30                     mov byte ptr [rsp + 0x30], al
0022654A  8A 44 24 61                     mov al, byte ptr [rsp + 0x61]
0022654E  88 44 24 28                     mov byte ptr [rsp + 0x28], al
00226552  44 88 7C 24 20                  mov byte ptr [rsp + 0x20], r15b
00226557  4C 8B 8C 24 00 01 00 00         mov r9, qword ptr [rsp + 0x100]
0022655F  44 8B 84 24 C8 05 00 00         mov r8d, dword ptr [rsp + 0x5c8]
00226567  8B D6                           mov edx, esi
00226569  48 8B 8C 24 D0 00 00 00         mov rcx, qword ptr [rsp + 0xd0]
00226571  E8 42 AB 1C 00                  call 0x1403f10b8
00226576  84 C0                           test al, al
00226578  0F 84 21 01 00 00               je 0x14022669f
0022657E  41 84 FC                        test r12b, dil
00226581  0F 85 CD 00 00 00               jne 0x140226654
00226587  E8 64 03 22 00                  call 0x1404468f0
0022658C  4C 8B C8                        mov r9, rax
0022658F  48 89 84 24 C8 01 00 00         mov qword ptr [rsp + 0x1c8], rax
00226597  48 85 C0                        test rax, rax
0022659A  0F 84 AC 00 00 00               je 0x14022664c
002265A0  48 8D 70 20                     lea rsi, [rax + 0x20]
002265A4  48 89 B4 24 50 01 00 00         mov qword ptr [rsp + 0x150], rsi
002265AC  40 80 CF 02                     or dil, 2
002265B0  49 8B D7                        mov rdx, r15
002265B3  4C 8B 94 24 A8 00 00 00         mov r10, qword ptr [rsp + 0xa8]
002265BB  41 F7 82 30 03 00 00 00 00 00 40  test dword ptr [r10 + 0x330], 0x40000000
002265C6  41 0F B6 CC                     movzx ecx, r12b
002265CA  41 0F 45 CF                     cmovne ecx, r15d
002265CE  4C 8B 84 24 08 01 00 00         mov r8, qword ptr [rsp + 0x108]
002265D6  49 8B 40 28                     mov rax, qword ptr [r8 + 0x28]
002265DA  48 3B 05 6F CA DE FF            cmp rax, qword ptr [rip - 0x213591]
002265E1  75 2B                           jne 0x14022660e
002265E3  49 8B 40 30                     mov rax, qword ptr [r8 + 0x30]
002265E7  48 3B 05 6A CA DE FF            cmp rax, qword ptr [rip - 0x213596]
002265EE  75 1E                           jne 0x14022660e
002265F0  48 8B 84 24 B0 00 00 00         mov rax, qword ptr [rsp + 0xb0]
002265F8  41 BB 12 00 00 00               mov r11d, 0x12
002265FE  66 44 39 18                     cmp word ptr [rax], r11w
00226602  75 0A                           jne 0x14022660e
00226604  83 CB 20                        or ebx, 0x20
00226607  49 8D 50 50                     lea rdx, [r8 + 0x50]
0022660B  41 8A CF                        mov cl, r15b
0022660E  48 89 54 24 28                  mov qword ptr [rsp + 0x28], rdx
00226613  88 4C 24 20                     mov byte ptr [rsp + 0x20], cl
00226617  44 8B 84 24 8C 00 00 00         mov r8d, dword ptr [rsp + 0x8c]
0022661F  48 8B 94 24 28 01 00 00         mov rdx, qword ptr [rsp + 0x128]
00226627  49 8B CA                        mov rcx, r10
0022662A  E8 41 D7 21 00                  call 0x140443d70
0022662F  84 C0                           test al, al
00226631  75 19                           jne 0x14022664c
00226633  48 8B 8C 24 C8 01 00 00         mov rcx, qword ptr [rsp + 0x1c8]
0022663B  E8 30 71 1F 00                  call 0x14041d770
00226640  40 80 E7 FD                     and dil, 0xfd
00226644  4C 89 BC 24 50 01 00 00         mov qword ptr [rsp + 0x150], r15
0022664C  41 0A FC                        or dil, r12b
0022664F  40 88 7C 24 60                  mov byte ptr [rsp + 0x60], dil
00226654  48 8B B4 24 50 01 00 00         mov rsi, qword ptr [rsp + 0x150]
0022665C  48 85 F6                        test rsi, rsi
0022665F  74 3E                           je 0x14022669f
00226661  48 8B 8C 24 A8 00 00 00         mov rcx, qword ptr [rsp + 0xa8]
00226669  8B 81 34 03 00 00               mov eax, dword ptr [rcx + 0x334]
0022666F  41 84 C4                        test r12b, al
00226672  74 1D                           je 0x140226691
00226674  4C 8D 84 24 60 01 00 00         lea r8, [rsp + 0x160]
0022667C  48 8B D6                        mov rdx, rsi
0022667F  E8 48 02 2B 00                  call 0x1404d68cc
00226684  84 C0                           test al, al
00226686  74 09                           je 0x140226691
00226688  83 CB 08                        or ebx, 8
0022668B  41 83 C5 18                     add r13d, 0x18
0022668F  EB 09                           jmp 0x14022669a
00226691  83 CB 04                        or ebx, 4
00226694  0F B7 06                        movzx eax, word ptr [rsi]
00226697  44 03 E8                        add r13d, eax
0022669A  44 89 6C 24 6C                  mov dword ptr [rsp + 0x6c], r13d
0022669F  8B 84 24 20 05 00 00            mov eax, dword ptr [rsp + 0x520]
002266A6  48 8D 04 40                     lea rax, [rax + rax*2]
002266AA  48 C1 E0 04                     shl rax, 4
002266AE  48 89 84 24 38 01 00 00         mov qword ptr [rsp + 0x138], rax
002266B6  44 89 BC 24 E8 00 00 00         mov dword ptr [rsp + 0xe8], r15d
002266BE  44 39 BC 24 C8 05 00 00         cmp dword ptr [rsp + 0x5c8], r15d
002266C6  0F 86 A3 00 00 00               jbe 0x14022676f
002266CC  48 8B B4 24 00 01 00 00         mov rsi, qword ptr [rsp + 0x100]
002266D4  48 83 C6 08                     add rsi, 8
002266D8  E8 63 8C 2C 00                  call 0x1404ef340
002266DD  85 C0                           test eax, eax
002266DF  74 0C                           je 0x1402266ed
002266E1  81 3E FF FF 00 00               cmp dword ptr [rsi], 0xffff
002266E7  0F 87 D1 00 00 00               ja 0x1402267be
002266ED  66 44 39 BC 24 C8 00 00 00      cmp word ptr [rsp + 0xc8], r15w
002266F6  41 8A C7                        mov al, r15b
002266F9  74 03                           je 0x1402266fe
002266FB  8A 46 04                        mov al, byte ptr [rsi + 4]
002266FE  0F B6 C8                        movzx ecx, al
00226701  84 C0                           test al, al
00226703  74 40                           je 0x140226745
00226705  83 E9 01                        sub ecx, 1
00226708  74 18                           je 0x140226722
0022670A  83 F9 03                        cmp ecx, 3
0022670D  75 3E                           jne 0x14022674d
0022670F  83 3E 10                        cmp dword ptr [rsi], 0x10
00226712  75 39                           jne 0x14022674d
00226714  48 8B 46 F8                     mov rax, qword ptr [rsi - 8]
00226718  48 89 84 24 78 01 00 00         mov qword ptr [rsp + 0x178], rax
00226720  EB 2B                           jmp 0x14022674d
00226722  E8 19 8C 2C 00                  call 0x1404ef340
00226727  85 C0                           test eax, eax
00226729  75 09                           jne 0x140226734
0022672B  0F B7 06                        movzx eax, word ptr [rsi]
0022672E  01 44 24 78                     add dword ptr [rsp + 0x78], eax
00226732  EB 0A                           jmp 0x14022673e
00226734  8B 44 24 78                     mov eax, dword ptr [rsp + 0x78]
00226738  03 06                           add eax, dword ptr [rsi]
0022673A  89 44 24 78                     mov dword ptr [rsp + 0x78], eax
0022673E  44 01 64 24 7C                  add dword ptr [rsp + 0x7c], r12d
00226743  EB 08                           jmp 0x14022674d
00226745  44 03 2E                        add r13d, dword ptr [rsi]
00226748  44 89 6C 24 6C                  mov dword ptr [rsp + 0x6c], r13d
0022674D  8B 84 24 E8 00 00 00            mov eax, dword ptr [rsp + 0xe8]
00226754  41 03 C4                        add eax, r12d
00226757  89 84 24 E8 00 00 00            mov dword ptr [rsp + 0xe8], eax
0022675E  48 83 C6 10                     add rsi, 0x10
00226762  3B 84 24 C8 05 00 00            cmp eax, dword ptr [rsp + 0x5c8]
00226769  0F 82 69 FF FF FF               jb 0x1402266d8
0022676F  44 39 7C 24 7C                  cmp dword ptr [rsp + 0x7c], r15d
00226774  74 1F                           je 0x140226795
00226776  E8 C5 8B 2C 00                  call 0x1404ef340
0022677B  85 C0                           test eax, eax
0022677D  8B 44 24 78                     mov eax, dword ptr [rsp + 0x78]
00226781  0F 85 BF 00 00 00               jne 0x140226846
00226787  83 C0 0F                        add eax, 0xf
0022678A  83 E0 F8                        and eax, 0xfffffff8
0022678D  44 03 E8                        add r13d, eax
00226790  44 89 6C 24 6C                  mov dword ptr [rsp + 0x6c], r13d
00226795  0F B7 B4 24 90 00 00 00         movzx esi, word ptr [rsp + 0x90]
0022679D  66 85 F6                        test si, si
002267A0  0F 84 DE 00 00 00               je 0x140226884
002267A6  E8 95 8B 2C 00                  call 0x1404ef340
002267AB  85 C0                           test eax, eax
002267AD  8D 46 0F                        lea eax, [rsi + 0xf]
002267B0  0F 85 BC 00 00 00               jne 0x140226872
002267B6  83 E0 F8                        and eax, 0xfffffff8
002267B9  E9 BE 00 00 00                  jmp 0x14022687c
002267BE  B8 05 00 00 80                  mov eax, 0x80000005
002267C3  45 85 F6                        test r14d, r14d
002267C6  44 0F 49 F0                     cmovns r14d, eax
002267CA  8B 9C 24 84 00 00 00            mov ebx, dword ptr [rsp + 0x84]
002267D1  0F B7 DB                        movzx ebx, bx
002267D4  44 89 74 24 70                  mov dword ptr [rsp + 0x70], r14d
002267D9  8B 84 24 88 00 00 00            mov eax, dword ptr [rsp + 0x88]
002267E0  0F AB C3                        bts ebx, eax
002267E3  4C 8B AC 24 A8 00 00 00         mov r13, qword ptr [rsp + 0xa8]
002267EB  E8 50 8B 2C 00                  call 0x1404ef340
002267F0  85 C0                           test eax, eax
002267F2  0F 84 B4 0E 00 00               je 0x1402276ac
002267F8  48 8B B4 24 60 01 00 00         mov rsi, qword ptr [rsp + 0x160]
00226800  48 85 F6                        test rsi, rsi
00226803  74 0F                           je 0x140226814
00226805  49 8B 95 20 04 00 00            mov rdx, qword ptr [r13 + 0x420]
0022680C  48 8B CE                        mov rcx, rsi
0022680F  E8 BC 61 1D 00                  call 0x1403fc9d0
00226814  48 8B B4 24 F0 00 00 00         mov rsi, qword ptr [rsp + 0xf0]
0022681C  44 38 7C 24 74                  cmp byte ptr [rsp + 0x74], r15b
00226821  0F 84 8D 0E 00 00               je 0x1402276b4
00226827  8B 84 24 A0 00 00 00            mov eax, dword ptr [rsp + 0xa0]
0022682E  48 8B 8E C0 02 00 00            mov rcx, qword ptr [rsi + 0x2c0]
00226835  41 8B D4                        mov edx, r12d
00226838  48 8B 0C C1                     mov rcx, qword ptr [rcx + rax*8]
0022683C  E8 0F 88 03 00                  call 0x14025f050
00226841  E9 6E 0E 00 00                  jmp 0x1402276b4
00226846  83 C0 0F                        add eax, 0xf
00226849  83 E0 F8                        and eax, 0xfffffff8
0022684C  3D FF FF 00 00                  cmp eax, 0xffff
00226851  0F 86 36 FF FF FF               jbe 0x14022678d
00226857  45 85 F6                        test r14d, r14d
0022685A  B8 95 00 00 C0                  mov eax, 0xc0000095
0022685F  44 0F 49 F0                     cmovns r14d, eax
00226863  8B 84 24 84 00 00 00            mov eax, dword ptr [rsp + 0x84]
0022686A  0F B7 D8                        movzx ebx, ax
0022686D  E9 62 FF FF FF                  jmp 0x1402267d4
00226872  83 E0 F8                        and eax, 0xfffffff8
00226875  3D FF FF 00 00                  cmp eax, 0xffff
0022687A  77 DB                           ja 0x140226857
0022687C  44 03 E8                        add r13d, eax
0022687F  44 89 6C 24 6C                  mov dword ptr [rsp + 0x6c], r13d
00226884  48 8B 84 24 38 01 00 00         mov rax, qword ptr [rsp + 0x138]
0022688C  44 89 AC 04 48 02 00 00         mov dword ptr [rsp + rax + 0x248], r13d
00226894  E8 5F 99 22 00                  call 0x1404501f8
00226899  85 C0                           test eax, eax
0022689B  75 09                           jne 0x1402268a6
0022689D  8B 84 24 D8 01 00 00            mov eax, dword ptr [rsp + 0x1d8]
002268A4  EB 1F                           jmp 0x1402268c5
002268A6  41 8B C7                        mov eax, r15d
002268A9  8B 8C 24 8C 00 00 00            mov ecx, dword ptr [rsp + 0x8c]
002268B0  F6 C1 04                        test cl, 4
002268B3  BA 00 02 00 00                  mov edx, 0x200
002268B8  0F 45 C2                        cmovne eax, edx
002268BB  F6 C1 08                        test cl, 8
002268BE  74 05                           je 0x1402268c5
002268C0  0D 00 06 00 00                  or eax, 0x600
002268C5  4C 8D 8C 24 B8 01 00 00         lea r9, [rsp + 0x1b8]
002268CD  4C 8D 84 24 F0 01 00 00         lea r8, [rsp + 0x1f0]
002268D5  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
002268D9  41 8B D5                        mov edx, r13d
002268DC  48 8B 8C 24 A8 00 00 00         mov rcx, qword ptr [rsp + 0xa8]
002268E4  E8 D7 5F 0D 00                  call 0x1402fc8c0
002268E9  4C 8B F0                        mov r14, rax
002268EC  48 89 84 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rax
002268F4  48 8B B4 24 60 01 00 00         mov rsi, qword ptr [rsp + 0x160]
002268FC  48 85 F6                        test rsi, rsi
002268FF  74 2A                           je 0x14022692b
00226901  48 8B 84 24 A8 00 00 00         mov rax, qword ptr [rsp + 0xa8]
00226909  48 8B 90 20 04 00 00            mov rdx, qword ptr [rax + 0x420]
00226910  48 8B CE                        mov rcx, rsi
00226913  E8 B8 60 1D 00                  call 0x1403fc9d0
00226918  E8 23 8A 2C 00                  call 0x1404ef340
0022691D  85 C0                           test eax, eax
0022691F  49 0F 45 F7                     cmovne rsi, r15
00226923  48 89 B4 24 60 01 00 00         mov qword ptr [rsp + 0x160], rsi
0022692B  4D 85 F6                        test r14, r14
0022692E  0F 85 23 01 00 00               jne 0x140226a57
00226934  41 8B D5                        mov edx, r13d
00226937  4C 8B AC 24 A8 00 00 00         mov r13, qword ptr [rsp + 0xa8]
0022693F  49 8B CD                        mov rcx, r13
00226942  E8 E9 FA 21 00                  call 0x140446430
00226947  8B D8                           mov ebx, eax
00226949  48 8B B4 24 10 02 00 00         mov rsi, qword ptr [rsp + 0x210]
00226951  8B 44 24 7C                     mov eax, dword ptr [rsp + 0x7c]
00226955  85 C0                           test eax, eax
00226957  49 0F 44 F7                     cmove rsi, r15
0022695B  44 8B B4 24 B0 01 00 00         mov r14d, dword ptr [rsp + 0x1b0]
00226963  45 0F 44 F7                     cmove r14d, r15d
00226967  48 8D 15 D2 C6 DE FF            lea rdx, [rip - 0x21392e]
0022696E  48 8B 0D CB 8E CD 00            mov rcx, qword ptr [rip + 0xcd8ecb]
00226975  E8 D6 BA 16 00                  call 0x140392450
0022697A  84 C0                           test al, al
0022697C  74 47                           je 0x1402269c5
0022697E  80 7C 24 69 02                  cmp byte ptr [rsp + 0x69], 2
00226983  0F 92 C0                        setb al
00226986  4D 8D 85 88 00 00 00            lea r8, [r13 + 0x88]
0022698D  48 8B 8C 24 08 01 00 00         mov rcx, qword ptr [rsp + 0x108]
00226995  48 83 C1 28                     add rcx, 0x28
00226999  44 88 7C 24 40                  mov byte ptr [rsp + 0x40], r15b
0022699E  88 44 24 38                     mov byte ptr [rsp + 0x38], al
002269A2  48 89 74 24 30                  mov qword ptr [rsp + 0x30], rsi
002269A7  44 89 74 24 28                  mov dword ptr [rsp + 0x28], r14d
002269AC  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
002269B0  44 8B 8C 24 8C 00 00 00         mov r9d, dword ptr [rsp + 0x8c]
002269B8  48 8B 94 24 B0 00 00 00         mov rdx, qword ptr [rsp + 0xb0]
002269C0  E8 93 A3 1C 00                  call 0x1403f0d58
002269C5  44 8B 74 24 70                  mov r14d, dword ptr [rsp + 0x70]
002269CA  45 85 F6                        test r14d, r14d
002269CD  78 19                           js 0x1402269e8
002269CF  41 F7 45 0C 00 00 00 08         test dword ptr [r13 + 0xc], 0x8000000
002269D7  44 0F 44 F3                     cmove r14d, ebx
002269DB  44 89 74 24 70                  mov dword ptr [rsp + 0x70], r14d
002269E0  44 89 B4 24 E0 00 00 00         mov dword ptr [rsp + 0xe0], r14d
002269E8  8B 74 24 74                     mov esi, dword ptr [rsp + 0x74]
002269EC  40 84 F6                        test sil, sil
002269EF  74 36                           je 0x140226a27
002269F1  48 8B 8C 24 F0 00 00 00         mov rcx, qword ptr [rsp + 0xf0]
002269F9  48 8B 89 C0 02 00 00            mov rcx, qword ptr [rcx + 0x2c0]
00226A00  41 8B D4                        mov edx, r12d
00226A03  48 8B 84 24 70 01 00 00         mov rax, qword ptr [rsp + 0x170]
00226A0B  48 8B 0C C1                     mov rcx, qword ptr [rcx + rax*8]
00226A0F  E8 3C 86 03 00                  call 0x14025f050
00226A14  E8 27 89 2C 00                  call 0x1404ef340
00226A19  40 0F B6 CE                     movzx ecx, sil
00226A1D  85 C0                           test eax, eax
00226A1F  41 0F 45 CF                     cmovne ecx, r15d
00226A23  88 4C 24 74                     mov byte ptr [rsp + 0x74], cl
00226A27  BA 95 00 00 C0                  mov edx, 0xc0000095
00226A2C  3B DA                           cmp ebx, edx
00226A2E  4C 8B 9C 24 D0 00 00 00         mov r11, qword ptr [rsp + 0xd0]
00226A36  4C 8B 84 24 F8 00 00 00         mov r8, qword ptr [rsp + 0xf8]
00226A3E  0F 85 99 F4 FF FF               jne 0x140225edd
00226A44  44 8B F2                        mov r14d, edx
00226A47  89 54 24 70                     mov dword ptr [rsp + 0x70], edx
00226A4B  8B 9C 24 84 00 00 00            mov ebx, dword ptr [rsp + 0x84]
00226A52  E9 94 FD FF FF                  jmp 0x1402267eb
00226A57  48 8B 84 24 38 01 00 00         mov rax, qword ptr [rsp + 0x138]
00226A5F  48 8B 8C 24 A8 00 00 00         mov rcx, qword ptr [rsp + 0xa8]
00226A67  48 89 8C 04 20 02 00 00         mov qword ptr [rsp + rax + 0x220], rcx
00226A6F  4C 89 B4 04 28 02 00 00         mov qword ptr [rsp + rax + 0x228], r14
00226A77  0F 10 84 24 F0 01 00 00         movups xmm0, xmmword ptr [rsp + 0x1f0]
00226A7F  0F 11 84 04 30 02 00 00         movups xmmword ptr [rsp + rax + 0x230], xmm0
00226A87  F2 0F 10 84 24 00 02 00 00      movsd xmm0, qword ptr [rsp + 0x200]
00226A90  F2 0F 11 84 04 40 02 00 00      movsd qword ptr [rsp + rax + 0x240], xmm0
00226A99  44 01 A4 24 20 05 00 00         add dword ptr [rsp + 0x520], r12d
00226AA1  E8 9A 88 2C 00                  call 0x1404ef340
00226AA6  0F B6 4C 24 74                  movzx ecx, byte ptr [rsp + 0x74]
00226AAB  85 C0                           test eax, eax
00226AAD  41 0F 45 CF                     cmovne ecx, r15d
00226AB1  8A C1                           mov al, cl
00226AB3  89 44 24 74                     mov dword ptr [rsp + 0x74], eax
00226AB7  88 4C 24 68                     mov byte ptr [rsp + 0x68], cl
00226ABB  41 8B C5                        mov eax, r13d
00226ABE  0D 00 00 13 C0                  or eax, 0xc0130000
00226AC3  41 89 06                        mov dword ptr [r14], eax
00226AC6  49 8D 76 04                     lea rsi, [r14 + 4]
00226ACA  48 89 B4 24 E8 00 00 00         mov qword ptr [rsp + 0xe8], rsi
00226AD2  0F B7 84 24 A8 05 00 00         movzx eax, word ptr [rsp + 0x5a8]
00226ADA  66 89 06                        mov word ptr [rsi], ax
00226ADD  0F B7 84 24 B0 05 00 00         movzx eax, word ptr [rsp + 0x5b0]
00226AE5  66 41 89 46 06                  mov word ptr [r14 + 6], ax
00226AEA  48 8B 84 24 B0 00 00 00         mov rax, qword ptr [rsp + 0xb0]
00226AF2  0F 10 00                        movups xmm0, xmmword ptr [rax]
00226AF5  F3 41 0F 7F 46 28               movdqu xmmword ptr [r14 + 0x28], xmm0
00226AFB  4C 39 BC 24 78 01 00 00         cmp qword ptr [rsp + 0x178], r15
00226B03  75 16                           jne 0x140226b1b
00226B05  48 8B 84 24 08 01 00 00         mov rax, qword ptr [rsp + 0x108]
00226B0D  0F 10 40 28                     movups xmm0, xmmword ptr [rax + 0x28]
00226B11  0F B7 94 24 40 01 00 00         movzx edx, word ptr [rsp + 0x140]
00226B19  EB 1E                           jmp 0x140226b39
00226B1B  48 8B 84 24 78 01 00 00         mov rax, qword ptr [rsp + 0x178]
00226B23  0F 10 00                        movups xmm0, xmmword ptr [rax]
00226B26  0F B7 94 24 A8 05 00 00         movzx edx, word ptr [rsp + 0x5a8]
00226B2E  B8 80 00 00 00                  mov eax, 0x80
00226B33  66 0B D0                        or dx, ax
00226B36  66 89 16                        mov word ptr [rsi], dx
00226B39  F3 41 0F 7F 46 18               movdqu xmmword ptr [r14 + 0x18], xmm0
00226B3F  48 8B 84 24 B8 05 00 00         mov rax, qword ptr [rsp + 0x5b8]
00226B47  48 85 C0                        test rax, rax
00226B4A  74 05                           je 0x140226b51
00226B4C  0F 10 00                        movups xmm0, xmmword ptr [rax]
00226B4F  EB 07                           jmp 0x140226b58
00226B51  0F 10 05 78 A7 DE FF            movups xmm0, xmmword ptr [rip - 0x215888]
00226B58  F3 41 0F 7F 46 40               movdqu xmmword ptr [r14 + 0x40], xmm0
00226B5E  49 8D 4E 10                     lea rcx, [r14 + 0x10]
00226B62  48 89 8C 24 70 01 00 00         mov qword ptr [rsp + 0x170], rcx
00226B6A  48 8B 84 24 B8 01 00 00         mov rax, qword ptr [rsp + 0x1b8]
00226B72  48 89 01                        mov qword ptr [rcx], rax
00226B75  48 8B 8C 24 28 01 00 00         mov rcx, qword ptr [rsp + 0x128]
00226B7D  8B 81 10 05 00 00               mov eax, dword ptr [rcx + 0x510]
00226B83  41 89 46 08                     mov dword ptr [r14 + 8], eax
00226B87  8B 81 08 05 00 00               mov eax, dword ptr [rcx + 0x508]
00226B8D  41 89 46 0C                     mov dword ptr [r14 + 0xc], eax
00226B91  8B 81 8C 02 00 00               mov eax, dword ptr [rcx + 0x28c]
00226B97  41 89 46 38                     mov dword ptr [r14 + 0x38], eax
00226B9B  8B 81 DC 02 00 00               mov eax, dword ptr [rcx + 0x2dc]
00226BA1  41 89 46 3C                     mov dword ptr [r14 + 0x3c], eax
00226BA5  B8 00 04 00 00                  mov eax, 0x400
00226BAA  66 85 84 24 F0 05 00 00         test word ptr [rsp + 0x5f0], ax
00226BB2  74 06                           je 0x140226bba
00226BB4  66 0B D0                        or dx, ax
00226BB7  66 89 16                        mov word ptr [rsi], dx
00226BBA  85 DB                           test ebx, ebx
00226BBC  0F 84 34 04 00 00               je 0x140226ff6
00226BC2  0F BA E3 09                     bt ebx, 9
00226BC6  0F 83 B8 00 00 00               jae 0x140226c84
00226BCC  49 8D 4E 50                     lea rcx, [r14 + 0x50]
00226BD0  48 89 8C 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rcx
00226BD8  48 8B 94 24 48 01 00 00         mov rdx, qword ptr [rsp + 0x148]
00226BE0  44 0F B7 B2 90 11 00 00         movzx r14d, word ptr [rdx + 0x1190]
00226BE8  66 41 83 C6 0F                  add r14w, 0xf
00226BED  B8 F8 FF 00 00                  mov eax, 0xfff8
00226BF2  66 44 23 F0                     and r14w, ax
00226BF6  66 44 89 31                     mov word ptr [rcx], r14w
00226BFA  66 C7 41 02 10 00               mov word ptr [rcx + 2], 0x10
00226C00  0F B7 82 90 11 00 00            movzx eax, word ptr [rdx + 0x1190]
00226C07  66 89 41 06                     mov word ptr [rcx + 6], ax
00226C0B  66 44 89 79 04                  mov word ptr [rcx + 4], r15w
00226C10  44 0F B7 82 90 11 00 00         movzx r8d, word ptr [rdx + 0x1190]
00226C18  66 45 2B F0                     sub r14w, r8w
00226C1C  66 41 83 EE 08                  sub r14w, 8
00226C21  48 8D 71 08                     lea rsi, [rcx + 8]
00226C25  48 8B 92 88 11 00 00            mov rdx, qword ptr [rdx + 0x1188]
00226C2C  48 8B CE                        mov rcx, rsi
00226C2F  E8 0C FC 49 00                  call 0x1406c6840
00226C34  45 0F B7 C6                     movzx r8d, r14w
00226C38  48 8B 84 24 48 01 00 00         mov rax, qword ptr [rsp + 0x148]
00226C40  0F B7 88 90 11 00 00            movzx ecx, word ptr [rax + 0x1190]
00226C47  48 03 CE                        add rcx, rsi
00226C4A  33 D2                           xor edx, edx
00226C4C  E8 EF FF 49 00                  call 0x1406c6c40
00226C51  48 8B B4 24 E8 00 00 00         mov rsi, qword ptr [rsp + 0xe8]
00226C59  66 44 09 26                     or word ptr [rsi], r12w
00226C5D  48 8B 94 24 B8 00 00 00         mov rdx, qword ptr [rsp + 0xb8]
00226C65  44 0F B7 12                     movzx r10d, word ptr [rdx]
00226C69  41 83 C2 50                     add r10d, 0x50
00226C6D  44 89 54 24 64                  mov dword ptr [rsp + 0x64], r10d
00226C72  48 89 94 24 20 01 00 00         mov qword ptr [rsp + 0x120], rdx
00226C7A  4C 8B B4 24 C0 00 00 00         mov r14, qword ptr [rsp + 0xc0]
00226C82  EB 08                           jmp 0x140226c8c
00226C84  49 8B D7                        mov rdx, r15
00226C87  44 8B 54 24 64                  mov r10d, dword ptr [rsp + 0x64]
00226C8C  41 BB 10 00 00 00               mov r11d, 0x10
00226C92  41 84 DB                        test r11b, bl
00226C95  74 52                           je 0x140226ce9
00226C97  41 8B CA                        mov ecx, r10d
00226C9A  49 03 CE                        add rcx, r14
00226C9D  45 8D 43 08                     lea r8d, [r11 + 8]
00226CA1  C7 01 18 00 01 00               mov dword ptr [rcx], 0x10018
00226CA7  C7 41 04 00 00 10 00            mov dword ptr [rcx + 4], 0x100000
00226CAE  48 8B 84 24 C0 05 00 00         mov rax, qword ptr [rsp + 0x5c0]
00226CB6  0F 10 00                        movups xmm0, xmmword ptr [rax]
00226CB9  F3 0F 7F 41 08                  movdqu xmmword ptr [rcx + 8], xmm0
00226CBE  66 44 09 26                     or word ptr [rsi], r12w
00226CC2  45 03 D0                        add r10d, r8d
00226CC5  44 89 54 24 64                  mov dword ptr [rsp + 0x64], r10d
00226CCA  48 85 D2                        test rdx, rdx
00226CCD  74 05                           je 0x140226cd4
00226CCF  66 44 09 62 04                  or word ptr [rdx + 4], r12w
00226CD4  4C 8B F1                        mov r14, rcx
00226CD7  48 89 8C 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rcx
00226CDF  48 89 8C 24 20 01 00 00         mov qword ptr [rsp + 0x120], rcx
00226CE7  EB 08                           jmp 0x140226cf1
00226CE9  4C 8B B4 24 B8 00 00 00         mov r14, qword ptr [rsp + 0xb8]
00226CF1  F6 C3 02                        test bl, 2
00226CF4  74 66                           je 0x140226d5c
00226CF6  45 8B F2                        mov r14d, r10d
00226CF9  4C 03 B4 24 C0 00 00 00         add r14, qword ptr [rsp + 0xc0]
00226D01  48 8B 84 24 D8 00 00 00         mov rax, qword ptr [rsp + 0xd8]
00226D09  44 0F B7 00                     movzx r8d, word ptr [rax]
00226D0D  48 8B D0                        mov rdx, rax
00226D10  49 8B CE                        mov rcx, r14
00226D13  E8 28 FB 49 00                  call 0x1406c6840
00226D18  66 44 09 26                     or word ptr [rsi], r12w
00226D1C  48 8B 84 24 D8 00 00 00         mov rax, qword ptr [rsp + 0xd8]
00226D24  0F B7 00                        movzx eax, word ptr [rax]
00226D27  44 8B 54 24 64                  mov r10d, dword ptr [rsp + 0x64]
00226D2C  44 03 D0                        add r10d, eax
00226D2F  44 89 54 24 64                  mov dword ptr [rsp + 0x64], r10d
00226D34  48 8B 84 24 B8 00 00 00         mov rax, qword ptr [rsp + 0xb8]
00226D3C  48 85 C0                        test rax, rax
00226D3F  74 05                           je 0x140226d46
00226D41  66 44 09 60 04                  or word ptr [rax + 4], r12w
00226D46  4C 89 B4 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], r14
00226D4E  4C 89 B4 24 20 01 00 00         mov qword ptr [rsp + 0x120], r14
00226D56  41 BB 10 00 00 00               mov r11d, 0x10
00226D5C  41 84 DC                        test r12b, bl
00226D5F  74 5C                           je 0x140226dbd
00226D61  41 8B F2                        mov esi, r10d
00226D64  48 03 B4 24 C0 00 00 00         add rsi, qword ptr [rsp + 0xc0]
00226D6C  C7 06 10 00 03 00               mov dword ptr [rsi], 0x30010
00226D72  C7 46 04 00 00 04 00            mov dword ptr [rsi + 4], 0x40000
00226D79  E8 52 96 00 00                  call 0x1402303d0
00226D7E  89 46 08                        mov dword ptr [rsi + 8], eax
00226D81  48 8B 84 24 E8 00 00 00         mov rax, qword ptr [rsp + 0xe8]
00226D89  66 44 09 20                     or word ptr [rax], r12w
00226D8D  44 8B 54 24 64                  mov r10d, dword ptr [rsp + 0x64]
00226D92  41 BB 10 00 00 00               mov r11d, 0x10
00226D98  45 03 D3                        add r10d, r11d
00226D9B  44 89 54 24 64                  mov dword ptr [rsp + 0x64], r10d
00226DA0  4D 85 F6                        test r14, r14
00226DA3  74 05                           je 0x140226daa
00226DA5  66 45 09 66 04                  or word ptr [r14 + 4], r12w
00226DAA  4C 8B F6                        mov r14, rsi
00226DAD  48 89 B4 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rsi
00226DB5  48 89 B4 24 20 01 00 00         mov qword ptr [rsp + 0x120], rsi
00226DBD  4C 8B 8C 24 C0 00 00 00         mov r9, qword ptr [rsp + 0xc0]
00226DC5  48 8B B4 24 E8 00 00 00         mov rsi, qword ptr [rsp + 0xe8]
00226DCD  F6 C3 40                        test bl, 0x40
00226DD0  74 67                           je 0x140226e39
00226DD2  41 8B D2                        mov edx, r10d
00226DD5  49 03 D1                        add rdx, r9
00226DD8  C7 02 10 00 0D 00               mov dword ptr [rdx], 0xd0010
00226DDE  C7 42 04 00 00 08 00            mov dword ptr [rdx + 4], 0x80000
00226DE5  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00226DEE  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00226DF5  48 B8 C4 02 00 00 80 F7 FF FF   movabs rax, 0xfffff780000002c4
00226DFF  8B 00                           mov eax, dword ptr [rax]
00226E01  48 C1 E0 30                     shl rax, 0x30
00226E05  48 0B 81 78 06 00 00            or rax, qword ptr [rcx + 0x678]
00226E0C  48 89 42 08                     mov qword ptr [rdx + 8], rax
00226E10  66 44 09 26                     or word ptr [rsi], r12w
00226E14  45 03 D3                        add r10d, r11d
00226E17  44 89 54 24 64                  mov dword ptr [rsp + 0x64], r10d
00226E1C  4D 85 F6                        test r14, r14
00226E1F  74 05                           je 0x140226e26
00226E21  66 45 09 66 04                  or word ptr [r14 + 4], r12w
00226E26  4C 8B F2                        mov r14, rdx
00226E29  48 89 94 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rdx
00226E31  48 89 94 24 20 01 00 00         mov qword ptr [rsp + 0x120], rdx
00226E39  84 DB                           test bl, bl
00226E3B  0F 89 AB 00 00 00               jns 0x140226eec
00226E41  45 8B C2                        mov r8d, r10d
00226E44  4D 03 C1                        add r8, r9
00226E47  41 C7 00 10 00 0A 00            mov dword ptr [r8], 0xa0010
00226E4E  BA 08 00 00 00                  mov edx, 8
00226E53  41 C7 40 04 00 00 08 00         mov dword ptr [r8 + 4], 0x80000
00226E5B  40 F6 C7 04                     test dil, 4
00226E5F  75 56                           jne 0x140226eb7
00226E61  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
00226E6A  48 8B 81 A8 8B 00 00            mov rax, qword ptr [rcx + 0x8ba8]
00226E71  48 03 C2                        add rax, rdx
00226E74  49 8B D4                        mov rdx, r12
00226E77  F0 48 0F C1 10                  lock xadd qword ptr [rax], rdx
00226E7C  49 03 D4                        add rdx, r12
00226E7F  8B 41 24                        mov eax, dword ptr [rcx + 0x24]
00226E82  48 C1 E0 30                     shl rax, 0x30
00226E86  48 B9 FF FF FF FF FF FF 00 00   movabs rcx, 0xffffffffffff
00226E90  48 23 D1                        and rdx, rcx
00226E93  48 0B C2                        or rax, rdx
00226E96  48 89 84 24 C0 01 00 00         mov qword ptr [rsp + 0x1c0], rax
00226E9E  40 80 CF 04                     or dil, 4
00226EA2  40 88 7C 24 60                  mov byte ptr [rsp + 0x60], dil
00226EA7  48 8B 8C 24 58 01 00 00         mov rcx, qword ptr [rsp + 0x158]
00226EAF  48 85 C9                        test rcx, rcx
00226EB2  74 03                           je 0x140226eb7
00226EB4  48 89 01                        mov qword ptr [rcx], rax
00226EB7  48 8B 84 24 C0 01 00 00         mov rax, qword ptr [rsp + 0x1c0]
00226EBF  49 89 40 08                     mov qword ptr [r8 + 8], rax
00226EC3  66 44 09 26                     or word ptr [rsi], r12w
00226EC7  45 03 D3                        add r10d, r11d
00226ECA  44 89 54 24 64                  mov dword ptr [rsp + 0x64], r10d
00226ECF  4D 85 F6                        test r14, r14
00226ED2  74 05                           je 0x140226ed9
00226ED4  66 45 09 66 04                  or word ptr [r14 + 4], r12w
00226ED9  4D 8B F0                        mov r14, r8
00226EDC  4C 89 84 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], r8
00226EE4  4C 89 84 24 20 01 00 00         mov qword ptr [rsp + 0x120], r8
00226EEC  F6 C3 04                        test bl, 4
00226EEF  0F 84 95 00 00 00               je 0x140226f8a
00226EF5  45 8B F2                        mov r14d, r10d
00226EF8  4D 03 F1                        add r14, r9
00226EFB  48 8B 84 24 50 01 00 00         mov rax, qword ptr [rsp + 0x150]
00226F03  44 0F B7 00                     movzx r8d, word ptr [rax]
00226F07  48 8B D0                        mov rdx, rax
00226F0A  49 8B CE                        mov rcx, r14
00226F0D  E8 2E F9 49 00                  call 0x1406c6840
00226F12  49 8D 46 08                     lea rax, [r14 + 8]
00226F16  4C 39 38                        cmp qword ptr [rax], r15
00226F19  74 2E                           je 0x140226f49
00226F1B  F6 C3 20                        test bl, 0x20
00226F1E  75 29                           jne 0x140226f49
00226F20  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00226F25  45 8A CC                        mov r9b, r12b
00226F28  4C 8B 84 24 A8 00 00 00         mov r8, qword ptr [rsp + 0xa8]
00226F30  8A 54 24 61                     mov dl, byte ptr [rsp + 0x61]
00226F34  48 8B 8C 24 28 01 00 00         mov rcx, qword ptr [rsp + 0x128]
00226F3C  E8 5F CB FD FF                  call 0x140203aa0
00226F41  84 C0                           test al, al
00226F43  75 04                           jne 0x140226f49
00226F45  4D 89 7E 08                     mov qword ptr [r14 + 8], r15
00226F49  66 44 09 26                     or word ptr [rsi], r12w
00226F4D  4C 8B 84 24 50 01 00 00         mov r8, qword ptr [rsp + 0x150]
00226F55  41 0F B7 00                     movzx eax, word ptr [r8]
00226F59  44 8B 54 24 64                  mov r10d, dword ptr [rsp + 0x64]
00226F5E  44 03 D0                        add r10d, eax
00226F61  44 89 54 24 64                  mov dword ptr [rsp + 0x64], r10d
00226F66  48 8B 84 24 B8 00 00 00         mov rax, qword ptr [rsp + 0xb8]
00226F6E  48 85 C0                        test rax, rax
00226F71  74 05                           je 0x140226f78
00226F73  66 44 09 60 04                  or word ptr [rax + 4], r12w
00226F78  4C 89 B4 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], r14
00226F80  4C 89 B4 24 20 01 00 00         mov qword ptr [rsp + 0x120], r14
00226F88  EB 08                           jmp 0x140226f92
00226F8A  4C 8B 84 24 50 01 00 00         mov r8, qword ptr [rsp + 0x150]
00226F92  B8 08 00 00 00                  mov eax, 8
00226F97  48 8B 94 24 C0 00 00 00         mov rdx, qword ptr [rsp + 0xc0]
00226F9F  84 D8                           test al, bl
00226FA1  74 60                           je 0x140227003
00226FA3  41 8B CA                        mov ecx, r10d
00226FA6  48 03 CA                        add rcx, rdx
00226FA9  44 8D 48 10                     lea r9d, [rax + 0x10]
00226FAD  C7 01 18 00 12 00               mov dword ptr [rcx], 0x120018
00226FB3  C7 41 04 00 00 10 00            mov dword ptr [rcx + 4], 0x100000
00226FBA  48 8B 84 24 60 01 00 00         mov rax, qword ptr [rsp + 0x160]
00226FC2  48 89 41 10                     mov qword ptr [rcx + 0x10], rax
00226FC6  49 8B 40 08                     mov rax, qword ptr [r8 + 8]
00226FCA  48 89 41 08                     mov qword ptr [rcx + 8], rax
00226FCE  66 44 09 26                     or word ptr [rsi], r12w
00226FD2  45 03 D1                        add r10d, r9d
00226FD5  44 89 54 24 64                  mov dword ptr [rsp + 0x64], r10d
00226FDA  4D 85 F6                        test r14, r14
00226FDD  74 05                           je 0x140226fe4
00226FDF  66 45 09 66 04                  or word ptr [r14 + 4], r12w
00226FE4  48 89 8C 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rcx
00226FEC  48 89 8C 24 20 01 00 00         mov qword ptr [rsp + 0x120], rcx
00226FF4  EB 08                           jmp 0x140226ffe
00226FF6  49 8B D6                        mov rdx, r14
00226FF9  44 8B 54 24 64                  mov r10d, dword ptr [rsp + 0x64]
00226FFE  B8 08 00 00 00                  mov eax, 8
00227003  0F B7 8C 24 90 00 00 00         movzx ecx, word ptr [rsp + 0x90]
0022700B  66 85 C9                        test cx, cx
0022700E  0F 84 94 01 00 00               je 0x1402271a8
00227014  45 8B F2                        mov r14d, r10d
00227017  4C 03 F2                        add r14, rdx
0022701A  4C 89 B4 24 38 01 00 00         mov qword ptr [rsp + 0x138], r14
00227022  BE 0F 00 00 00                  mov esi, 0xf
00227027  03 F1                           add esi, ecx
00227029  BA F8 FF 00 00                  mov edx, 0xfff8
0022702E  66 23 F2                        and si, dx
00227031  66 41 89 36                     mov word ptr [r14], si
00227035  41 C7 46 02 0C 00 00 00         mov dword ptr [r14 + 2], 0xc
0022703D  66 41 89 4E 06                  mov word ptr [r14 + 6], cx
00227042  66 2B F1                        sub si, cx
00227045  66 2B F0                        sub si, ax
00227048  66 89 B4 24 88 00 00 00         mov word ptr [rsp + 0x88], si
00227050  8B D9                           mov ebx, ecx
00227052  44 8B C1                        mov r8d, ecx
00227055  48 8B 94 24 E0 01 00 00         mov rdx, qword ptr [rsp + 0x1e0]
0022705D  49 8D 4E 08                     lea rcx, [r14 + 8]
00227061  E8 DA F7 49 00                  call 0x1406c6840
00227066  44 0F B7 C6                     movzx r8d, si
0022706A  48 8D 4B 08                     lea rcx, [rbx + 8]
0022706E  49 03 CE                        add rcx, r14
00227071  33 D2                           xor edx, edx
00227073  E8 C8 FB 49 00                  call 0x1406c6c40
00227078  48 8B 8C 24 B8 00 00 00         mov rcx, qword ptr [rsp + 0xb8]
00227080  44 8B 54 24 64                  mov r10d, dword ptr [rsp + 0x64]
00227085  E9 F4 00 00 00                  jmp 0x14022717e
0022708A  0F B7 8C 24 88 00 00 00         movzx ecx, word ptr [rsp + 0x88]
00227092  0F B7 84 24 90 00 00 00         movzx eax, word ptr [rsp + 0x90]
0022709A  03 C8                           add ecx, eax
0022709C  4C 63 C1                        movsxd r8, ecx
0022709F  4C 8B B4 24 38 01 00 00         mov r14, qword ptr [rsp + 0x138]
002270A7  49 8D 4E 08                     lea rcx, [r14 + 8]
002270AB  33 D2                           xor edx, edx
002270AD  E8 8E FB 49 00                  call 0x1406c6c40
002270B2  45 33 FF                        xor r15d, r15d
002270B5  45 8D 67 01                     lea r12d, [r15 + 1]
002270B9  8B 84 24 E0 00 00 00            mov eax, dword ptr [rsp + 0xe0]
002270C0  89 44 24 70                     mov dword ptr [rsp + 0x70], eax
002270C4  48 8B 84 24 68 01 00 00         mov rax, qword ptr [rsp + 0x168]
002270CC  48 89 84 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], rax
002270D4  48 8B 84 24 88 01 00 00         mov rax, qword ptr [rsp + 0x188]
002270DC  48 89 84 24 F0 00 00 00         mov qword ptr [rsp + 0xf0], rax
002270E4  48 8B 84 24 90 01 00 00         mov rax, qword ptr [rsp + 0x190]
002270EC  48 89 84 24 48 01 00 00         mov qword ptr [rsp + 0x148], rax
002270F4  8A 44 24 68                     mov al, byte ptr [rsp + 0x68]
002270F8  89 44 24 74                     mov dword ptr [rsp + 0x74], eax
002270FC  48 8B 84 24 30 01 00 00         mov rax, qword ptr [rsp + 0x130]
00227104  48 89 84 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rax
0022710C  8B 84 24 10 01 00 00            mov eax, dword ptr [rsp + 0x110]
00227113  89 84 24 A0 00 00 00            mov dword ptr [rsp + 0xa0], eax
0022711A  40 8A 7C 24 60                  mov dil, byte ptr [rsp + 0x60]
0022711F  44 8B 6C 24 6C                  mov r13d, dword ptr [rsp + 0x6c]
00227124  44 8B 54 24 64                  mov r10d, dword ptr [rsp + 0x64]
00227129  48 8B 8C 24 20 01 00 00         mov rcx, qword ptr [rsp + 0x120]
00227131  48 8B 84 24 98 01 00 00         mov rax, qword ptr [rsp + 0x198]
00227139  48 89 84 24 08 01 00 00         mov qword ptr [rsp + 0x108], rax
00227141  0F B7 84 24 98 00 00 00         movzx eax, word ptr [rsp + 0x98]
00227149  89 84 24 84 00 00 00            mov dword ptr [rsp + 0x84], eax
00227150  8B 84 24 18 01 00 00            mov eax, dword ptr [rsp + 0x118]
00227157  89 84 24 8C 00 00 00            mov dword ptr [rsp + 0x8c], eax
0022715E  48 8B 84 24 A0 01 00 00         mov rax, qword ptr [rsp + 0x1a0]
00227166  48 89 84 24 00 01 00 00         mov qword ptr [rsp + 0x100], rax
0022716E  48 8B 84 24 A8 01 00 00         mov rax, qword ptr [rsp + 0x1a8]
00227176  48 89 84 24 28 01 00 00         mov qword ptr [rsp + 0x128], rax
0022717E  48 8B B4 24 E8 00 00 00         mov rsi, qword ptr [rsp + 0xe8]
00227186  66 44 09 26                     or word ptr [rsi], r12w
0022718A  41 0F B7 06                     movzx eax, word ptr [r14]
0022718E  44 03 D0                        add r10d, eax
00227191  44 89 54 24 64                  mov dword ptr [rsp + 0x64], r10d
00227196  48 85 C9                        test rcx, rcx
00227199  74 05                           je 0x1402271a0
0022719B  66 44 09 61 04                  or word ptr [rcx + 4], r12w
002271A0  4C 89 B4 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], r14
002271A8  44 8B 5C 24 7C                  mov r11d, dword ptr [rsp + 0x7c]
002271AD  4C 8B B4 24 C0 00 00 00         mov r14, qword ptr [rsp + 0xc0]
002271B5  45 85 DB                        test r11d, r11d
002271B8  74 7B                           je 0x140227235
002271BA  41 8B DA                        mov ebx, r10d
002271BD  49 03 DE                        add rbx, r14
002271C0  8B 44 24 78                     mov eax, dword ptr [rsp + 0x78]
002271C4  BA 0F 00 00 00                  mov edx, 0xf
002271C9  03 D0                           add edx, eax
002271CB  B9 F8 FF 00 00                  mov ecx, 0xfff8
002271D0  66 23 D1                        and dx, cx
002271D3  66 89 13                        mov word ptr [rbx], dx
002271D6  C7 43 02 0B 00 00 00            mov dword ptr [rbx + 2], 0xb
002271DD  66 89 43 06                     mov word ptr [rbx + 6], ax
002271E1  66 2B D0                        sub dx, ax
002271E4  66 83 EA 08                     sub dx, 8
002271E8  48 8D 4B 08                     lea rcx, [rbx + 8]
002271EC  48 89 8C 24 80 01 00 00         mov qword ptr [rsp + 0x180], rcx
002271F4  48 03 C8                        add rcx, rax
002271F7  48 89 8C 24 E8 01 00 00         mov qword ptr [rsp + 0x1e8], rcx
002271FF  44 0F B7 C2                     movzx r8d, dx
00227203  33 D2                           xor edx, edx
00227205  E8 36 FA 49 00                  call 0x1406c6c40
0022720A  66 44 09 26                     or word ptr [rsi], r12w
0022720E  0F B7 03                        movzx eax, word ptr [rbx]
00227211  44 8B 54 24 64                  mov r10d, dword ptr [rsp + 0x64]
00227216  44 03 D0                        add r10d, eax
00227219  44 89 54 24 64                  mov dword ptr [rsp + 0x64], r10d
0022721E  48 8B 84 24 B8 00 00 00         mov rax, qword ptr [rsp + 0xb8]
00227226  44 8B 5C 24 7C                  mov r11d, dword ptr [rsp + 0x7c]
0022722B  48 85 C0                        test rax, rax
0022722E  74 05                           je 0x140227235
00227230  66 44 09 60 04                  or word ptr [rax + 4], r12w
00227235  41 8B F7                        mov esi, r15d
00227238  89 74 24 78                     mov dword ptr [rsp + 0x78], esi
0022723C  3B B4 24 C8 05 00 00            cmp esi, dword ptr [rsp + 0x5c8]
00227243  0F 83 B7 03 00 00               jae 0x140227600
00227249  8B C6                           mov eax, esi
0022724B  48 03 C0                        add rax, rax
0022724E  4C 8B 84 24 00 01 00 00         mov r8, qword ptr [rsp + 0x100]
00227256  41 8B 54 C0 08                  mov edx, dword ptr [r8 + rax*8 + 8]
0022725B  89 94 24 E8 00 00 00            mov dword ptr [rsp + 0xe8], edx
00227262  4D 8B 0C C0                     mov r9, qword ptr [r8 + rax*8]
00227266  66 44 39 BC 24 C8 00 00 00      cmp word ptr [rsp + 0xc8], r15w
0022726F  75 05                           jne 0x140227276
00227271  41 8A C7                        mov al, r15b
00227274  EB 05                           jmp 0x14022727b
00227276  41 8A 44 C0 0C                  mov al, byte ptr [r8 + rax*8 + 0xc]
0022727B  0F B6 C8                        movzx ecx, al
0022727E  84 C0                           test al, al
00227280  0F 84 4D 02 00 00               je 0x1402274d3
00227286  83 E9 01                        sub ecx, 1
00227289  0F 84 F7 00 00 00               je 0x140227386
0022728F  83 F9 02                        cmp ecx, 2
00227292  0F 85 58 03 00 00               jne 0x1402275f0
00227298  83 FA 08                        cmp edx, 8
0022729B  0F 85 4F 03 00 00               jne 0x1402275f0
002272A1  49 8B 09                        mov rcx, qword ptr [r9]
002272A4  48 8B 84 24 70 01 00 00         mov rax, qword ptr [rsp + 0x170]
002272AC  48 89 08                        mov qword ptr [rax], rcx
002272AF  E9 3C 03 00 00                  jmp 0x1402275f0
002272B4  45 33 FF                        xor r15d, r15d
002272B7  45 8D 67 01                     lea r12d, [r15 + 1]
002272BB  8B 84 24 E0 00 00 00            mov eax, dword ptr [rsp + 0xe0]
002272C2  89 44 24 70                     mov dword ptr [rsp + 0x70], eax
002272C6  48 8B 8C 24 68 01 00 00         mov rcx, qword ptr [rsp + 0x168]
002272CE  48 89 8C 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], rcx
002272D6  48 8B 94 24 88 01 00 00         mov rdx, qword ptr [rsp + 0x188]
002272DE  48 89 94 24 F0 00 00 00         mov qword ptr [rsp + 0xf0], rdx
002272E6  4C 8B 84 24 90 01 00 00         mov r8, qword ptr [rsp + 0x190]
002272EE  4C 89 84 24 48 01 00 00         mov qword ptr [rsp + 0x148], r8
002272F6  8A 54 24 68                     mov dl, byte ptr [rsp + 0x68]
002272FA  89 54 24 74                     mov dword ptr [rsp + 0x74], edx
002272FE  48 8B 84 24 30 01 00 00         mov rax, qword ptr [rsp + 0x130]
00227306  48 89 84 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rax
0022730E  8B 94 24 10 01 00 00            mov edx, dword ptr [rsp + 0x110]
00227315  89 94 24 A0 00 00 00            mov dword ptr [rsp + 0xa0], edx
0022731C  40 8A 7C 24 60                  mov dil, byte ptr [rsp + 0x60]
00227321  44 8B 6C 24 6C                  mov r13d, dword ptr [rsp + 0x6c]
00227326  8B 74 24 78                     mov esi, dword ptr [rsp + 0x78]
0022732A  44 8B 54 24 64                  mov r10d, dword ptr [rsp + 0x64]
0022732F  48 8B 8C 24 98 01 00 00         mov rcx, qword ptr [rsp + 0x198]
00227337  48 89 8C 24 08 01 00 00         mov qword ptr [rsp + 0x108], rcx
0022733F  0F B7 84 24 98 00 00 00         movzx eax, word ptr [rsp + 0x98]
00227347  89 84 24 84 00 00 00            mov dword ptr [rsp + 0x84], eax
0022734E  8B 94 24 18 01 00 00            mov edx, dword ptr [rsp + 0x118]
00227355  89 94 24 8C 00 00 00            mov dword ptr [rsp + 0x8c], edx
0022735C  48 8B 8C 24 A0 01 00 00         mov rcx, qword ptr [rsp + 0x1a0]
00227364  48 89 8C 24 00 01 00 00         mov qword ptr [rsp + 0x100], rcx
0022736C  48 8B 84 24 A8 01 00 00         mov rax, qword ptr [rsp + 0x1a8]
00227374  48 89 84 24 28 01 00 00         mov qword ptr [rsp + 0x128], rax
0022737C  44 8B 5C 24 7C                  mov r11d, dword ptr [rsp + 0x7c]
00227381  E9 6A 02 00 00                  jmp 0x1402275f0
00227386  48 8B 84 24 80 01 00 00         mov rax, qword ptr [rsp + 0x180]
0022738E  48 85 C0                        test rax, rax
00227391  0F 84 8F 04 00 00               je 0x140227826
00227397  4C 8B C2                        mov r8, rdx
0022739A  48 8D 1C 02                     lea rbx, [rdx + rax]
0022739E  48 89 9C 24 38 01 00 00         mov qword ptr [rsp + 0x138], rbx
002273A6  48 3B 9C 24 E8 01 00 00         cmp rbx, qword ptr [rsp + 0x1e8]
002273AE  0F 87 72 04 00 00               ja 0x140227826
002273B4  45 85 DB                        test r11d, r11d
002273B7  0F 84 69 04 00 00               je 0x140227826
002273BD  49 8B D1                        mov rdx, r9
002273C0  48 8B C8                        mov rcx, rax
002273C3  E8 78 F4 49 00                  call 0x1406c6840
002273C8  44 8B 54 24 64                  mov r10d, dword ptr [rsp + 0x64]
002273CD  E9 E7 00 00 00                  jmp 0x1402274b9
002273D2  44 8B 84 24 E8 00 00 00         mov r8d, dword ptr [rsp + 0xe8]
002273DA  33 D2                           xor edx, edx
002273DC  48 8B 8C 24 80 01 00 00         mov rcx, qword ptr [rsp + 0x180]
002273E4  E8 57 F8 49 00                  call 0x1406c6c40
002273E9  45 33 FF                        xor r15d, r15d
002273EC  45 8D 67 01                     lea r12d, [r15 + 1]
002273F0  8B 84 24 E0 00 00 00            mov eax, dword ptr [rsp + 0xe0]
002273F7  89 44 24 70                     mov dword ptr [rsp + 0x70], eax
002273FB  48 8B 84 24 68 01 00 00         mov rax, qword ptr [rsp + 0x168]
00227403  48 89 84 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], rax
0022740B  48 8B 84 24 88 01 00 00         mov rax, qword ptr [rsp + 0x188]
00227413  48 89 84 24 F0 00 00 00         mov qword ptr [rsp + 0xf0], rax
0022741B  48 8B 84 24 90 01 00 00         mov rax, qword ptr [rsp + 0x190]
00227423  48 89 84 24 48 01 00 00         mov qword ptr [rsp + 0x148], rax
0022742B  8A 44 24 68                     mov al, byte ptr [rsp + 0x68]
0022742F  89 44 24 74                     mov dword ptr [rsp + 0x74], eax
00227433  48 8B 84 24 30 01 00 00         mov rax, qword ptr [rsp + 0x130]
0022743B  48 89 84 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rax
00227443  8B 84 24 10 01 00 00            mov eax, dword ptr [rsp + 0x110]
0022744A  89 84 24 A0 00 00 00            mov dword ptr [rsp + 0xa0], eax
00227451  40 8A 7C 24 60                  mov dil, byte ptr [rsp + 0x60]
00227456  44 8B 6C 24 6C                  mov r13d, dword ptr [rsp + 0x6c]
0022745B  8B 74 24 78                     mov esi, dword ptr [rsp + 0x78]
0022745F  44 8B 54 24 64                  mov r10d, dword ptr [rsp + 0x64]
00227464  48 8B 9C 24 38 01 00 00         mov rbx, qword ptr [rsp + 0x138]
0022746C  48 8B 84 24 98 01 00 00         mov rax, qword ptr [rsp + 0x198]
00227474  48 89 84 24 08 01 00 00         mov qword ptr [rsp + 0x108], rax
0022747C  0F B7 84 24 98 00 00 00         movzx eax, word ptr [rsp + 0x98]
00227484  89 84 24 84 00 00 00            mov dword ptr [rsp + 0x84], eax
0022748B  8B 84 24 18 01 00 00            mov eax, dword ptr [rsp + 0x118]
00227492  89 84 24 8C 00 00 00            mov dword ptr [rsp + 0x8c], eax
00227499  48 8B 84 24 A0 01 00 00         mov rax, qword ptr [rsp + 0x1a0]
002274A1  48 89 84 24 00 01 00 00         mov qword ptr [rsp + 0x100], rax
002274A9  48 8B 84 24 A8 01 00 00         mov rax, qword ptr [rsp + 0x1a8]
002274B1  48 89 84 24 28 01 00 00         mov qword ptr [rsp + 0x128], rax
002274B9  48 89 9C 24 80 01 00 00         mov qword ptr [rsp + 0x180], rbx
002274C1  44 8B 5C 24 7C                  mov r11d, dword ptr [rsp + 0x7c]
002274C6  41 FF CB                        dec r11d
002274C9  44 89 5C 24 7C                  mov dword ptr [rsp + 0x7c], r11d
002274CE  E9 1D 01 00 00                  jmp 0x1402275f0
002274D3  41 8B CA                        mov ecx, r10d
002274D6  49 03 CE                        add rcx, r14
002274D9  48 89 8C 24 38 01 00 00         mov qword ptr [rsp + 0x138], rcx
002274E1  44 03 D2                        add r10d, edx
002274E4  44 89 54 24 64                  mov dword ptr [rsp + 0x64], r10d
002274E9  45 3B D5                        cmp r10d, r13d
002274EC  0F 87 4F 03 00 00               ja 0x140227841
002274F2  4C 8B C2                        mov r8, rdx
002274F5  49 8B D1                        mov rdx, r9
002274F8  E8 43 F3 49 00                  call 0x1406c6840
002274FD  44 8B 54 24 64                  mov r10d, dword ptr [rsp + 0x64]
00227502  44 8B 5C 24 7C                  mov r11d, dword ptr [rsp + 0x7c]
00227507  E9 E4 00 00 00                  jmp 0x1402275f0
0022750C  44 8B 84 24 E8 00 00 00         mov r8d, dword ptr [rsp + 0xe8]
00227514  33 D2                           xor edx, edx
00227516  48 8B 8C 24 38 01 00 00         mov rcx, qword ptr [rsp + 0x138]
0022751E  E8 1D F7 49 00                  call 0x1406c6c40
00227523  45 33 FF                        xor r15d, r15d
00227526  45 8D 67 01                     lea r12d, [r15 + 1]
0022752A  8B 84 24 E0 00 00 00            mov eax, dword ptr [rsp + 0xe0]
00227531  89 44 24 70                     mov dword ptr [rsp + 0x70], eax
00227535  48 8B 84 24 68 01 00 00         mov rax, qword ptr [rsp + 0x168]
0022753D  48 89 84 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], rax
00227545  48 8B 84 24 88 01 00 00         mov rax, qword ptr [rsp + 0x188]
0022754D  48 89 84 24 F0 00 00 00         mov qword ptr [rsp + 0xf0], rax
00227555  48 8B 84 24 90 01 00 00         mov rax, qword ptr [rsp + 0x190]
0022755D  48 89 84 24 48 01 00 00         mov qword ptr [rsp + 0x148], rax
00227565  8A 44 24 68                     mov al, byte ptr [rsp + 0x68]
00227569  89 44 24 74                     mov dword ptr [rsp + 0x74], eax
0022756D  48 8B 84 24 30 01 00 00         mov rax, qword ptr [rsp + 0x130]
00227575  48 89 84 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rax
0022757D  8B 84 24 10 01 00 00            mov eax, dword ptr [rsp + 0x110]
00227584  89 84 24 A0 00 00 00            mov dword ptr [rsp + 0xa0], eax
0022758B  40 8A 7C 24 60                  mov dil, byte ptr [rsp + 0x60]
00227590  44 8B 6C 24 6C                  mov r13d, dword ptr [rsp + 0x6c]
00227595  8B 74 24 78                     mov esi, dword ptr [rsp + 0x78]
00227599  44 8B 54 24 64                  mov r10d, dword ptr [rsp + 0x64]
0022759E  48 8B 84 24 98 01 00 00         mov rax, qword ptr [rsp + 0x198]
002275A6  48 89 84 24 08 01 00 00         mov qword ptr [rsp + 0x108], rax
002275AE  0F B7 84 24 98 00 00 00         movzx eax, word ptr [rsp + 0x98]
002275B6  89 84 24 84 00 00 00            mov dword ptr [rsp + 0x84], eax
002275BD  8B 84 24 18 01 00 00            mov eax, dword ptr [rsp + 0x118]
002275C4  89 84 24 8C 00 00 00            mov dword ptr [rsp + 0x8c], eax
002275CB  48 8B 84 24 A0 01 00 00         mov rax, qword ptr [rsp + 0x1a0]
002275D3  48 89 84 24 00 01 00 00         mov qword ptr [rsp + 0x100], rax
002275DB  48 8B 84 24 A8 01 00 00         mov rax, qword ptr [rsp + 0x1a8]
002275E3  48 89 84 24 28 01 00 00         mov qword ptr [rsp + 0x128], rax
002275EB  44 8B 5C 24 7C                  mov r11d, dword ptr [rsp + 0x7c]
002275F0  41 03 F4                        add esi, r12d
002275F3  4C 8B B4 24 C0 00 00 00         mov r14, qword ptr [rsp + 0xc0]
002275FB  E9 38 FC FF FF                  jmp 0x140227238
00227600  4C 8B AC 24 A8 00 00 00         mov r13, qword ptr [rsp + 0xa8]
00227608  41 F7 45 0C 00 00 08 00         test dword ptr [r13 + 0xc], 0x80000
00227610  74 2B                           je 0x14022763d
00227612  80 3D C3 FF D1 00 00            cmp byte ptr [rip + 0xd1ffc3], 0
00227619  75 09                           jne 0x140227624
0022761B  80 3D FA 33 BE 00 00            cmp byte ptr [rip + 0xbe33fa], 0
00227622  74 09                           je 0x14022762d
00227624  80 3D 88 E6 D2 00 00            cmp byte ptr [rip + 0xd2e688], 0
0022762B  74 10                           je 0x14022763d
0022762D  48 8D 94 24 F0 01 00 00         lea rdx, [rsp + 0x1f0]
00227635  49 8B CD                        mov rcx, r13
00227638  E8 D3 F7 28 00                  call 0x1404b6e10
0022763D  4D 39 BD 20 06 00 00            cmp qword ptr [r13 + 0x620], r15
00227644  74 1F                           je 0x140227665
00227646  4C 8B 84 24 08 01 00 00         mov r8, qword ptr [rsp + 0x108]
0022764E  49 83 C0 28                     add r8, 0x28
00227652  45 33 C9                        xor r9d, r9d
00227655  48 8D 94 24 F0 01 00 00         lea rdx, [rsp + 0x1f0]
0022765D  49 8B CD                        mov rcx, r13
00227660  E8 A7 F8 28 00                  call 0x1404b6f0c
00227665  4C 8B 84 24 F8 00 00 00         mov r8, qword ptr [rsp + 0xf8]
0022766D  4D 85 C0                        test r8, r8
00227670  44 8B 74 24 70                  mov r14d, dword ptr [rsp + 0x70]
00227675  4C 8B 94 24 B0 00 00 00         mov r10, qword ptr [rsp + 0xb0]
0022767D  4C 8B 9C 24 D0 00 00 00         mov r11, qword ptr [rsp + 0xd0]
00227685  0F 84 5A E8 FF FF               je 0x140225ee5
0022768B  8B 8C 24 A0 00 00 00            mov ecx, dword ptr [rsp + 0xa0]
00227692  8B C1                           mov eax, ecx
00227694  C1 E8 05                        shr eax, 5
00227697  8B D0                           mov edx, eax
00227699  83 E1 1F                        and ecx, 0x1f
0022769C  41 8B 04 80                     mov eax, dword ptr [r8 + rax*4]
002276A0  0F AB C8                        bts eax, ecx
002276A3  41 89 04 90                     mov dword ptr [r8 + rdx*4], eax
002276A7  E9 39 E8 FF FF                  jmp 0x140225ee5
002276AC  48 8B B4 24 F0 00 00 00         mov rsi, qword ptr [rsp + 0xf0]
002276B4  40 F6 C7 02                     test dil, 2
002276B8  74 0D                           je 0x1402276c7
002276BA  48 8B 8C 24 C8 01 00 00         mov rcx, qword ptr [rsp + 0x1c8]
002276C2  E8 A9 60 1F 00                  call 0x14041d770
002276C7  45 85 F6                        test r14d, r14d
002276CA  78 59                           js 0x140227725
002276CC  44 39 BC 24 20 05 00 00         cmp dword ptr [rsp + 0x520], r15d
002276D4  0F 86 B2 00 00 00               jbe 0x14022778c
002276DA  48 8D 9C 24 20 02 00 00         lea rbx, [rsp + 0x220]
002276E2  8B BC 24 20 05 00 00            mov edi, dword ptr [rsp + 0x520]
002276E9  44 8A 74 24 61                  mov r14b, byte ptr [rsp + 0x61]
002276EE  48 8D 4B 10                     lea rcx, [rbx + 0x10]
002276F2  E8 29 96 1C 00                  call 0x1403f0d20
002276F7  41 80 FE 02                     cmp r14b, 2
002276FB  73 18                           jae 0x140227715
002276FD  48 8B 03                        mov rax, qword ptr [rbx]
00227700  8B 00                           mov eax, dword ptr [rax]
00227702  48 8B 8E C0 02 00 00            mov rcx, qword ptr [rsi + 0x2c0]
00227709  41 8B D4                        mov edx, r12d
0022770C  48 8B 0C C1                     mov rcx, qword ptr [rcx + rax*8]
00227710  E8 3B 79 03 00                  call 0x14025f050
00227715  48 83 C3 30                     add rbx, 0x30
00227719  49 2B FC                        sub rdi, r12
0022771C  75 D0                           jne 0x1402276ee
0022771E  44 8B 74 24 70                  mov r14d, dword ptr [rsp + 0x70]
00227723  EB 67                           jmp 0x14022778c
00227725  80 7C 24 69 02                  cmp byte ptr [rsp + 0x69], 2
0022772A  0F 92 C0                        setb al
0022772D  44 88 7C 24 58                  mov byte ptr [rsp + 0x58], r15b
00227732  48 8B 8C 24 00 01 00 00         mov rcx, qword ptr [rsp + 0x100]
0022773A  48 89 4C 24 50                  mov qword ptr [rsp + 0x50], rcx
0022773F  8B 8C 24 C8 05 00 00            mov ecx, dword ptr [rsp + 0x5c8]
00227746  89 4C 24 48                     mov dword ptr [rsp + 0x48], ecx
0022774A  88 44 24 40                     mov byte ptr [rsp + 0x40], al
0022774E  48 8B 84 24 B0 00 00 00         mov rax, qword ptr [rsp + 0xb0]
00227756  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0022775B  44 89 74 24 30                  mov dword ptr [rsp + 0x30], r14d
00227760  8B 8C 24 8C 00 00 00            mov ecx, dword ptr [rsp + 0x8c]
00227767  89 4C 24 28                     mov dword ptr [rsp + 0x28], ecx
0022776B  66 89 5C 24 20                  mov word ptr [rsp + 0x20], bx
00227770  4C 8D 8C 24 20 02 00 00         lea r9, [rsp + 0x220]
00227778  4C 8B 84 24 08 01 00 00         mov r8, qword ptr [rsp + 0x108]
00227780  48 8B 50 08                     mov rdx, qword ptr [rax + 8]
00227784  8A 48 04                        mov cl, byte ptr [rax + 4]
00227787  E8 C4 92 1C 00                  call 0x1403f0a50
0022778C  44 38 BC 24 80 00 00 00         cmp byte ptr [rsp + 0x80], r15b
00227794  74 0D                           je 0x1402277a3
00227796  48 8B 8C 24 D0 01 00 00         mov rcx, qword ptr [rsp + 0x1d0]
0022779E  E8 6D 78 03 00                  call 0x14025f010
002277A3  4C 8B 84 24 D8 00 00 00         mov r8, qword ptr [rsp + 0xd8]
002277AB  4D 85 C0                        test r8, r8
002277AE  74 4F                           je 0x1402277ff
002277B0  65 48 8B 14 25 20 00 00 00      mov rdx, qword ptr gs:[0x20]
002277B9  48 8B 8A 80 08 00 00            mov rcx, qword ptr [rdx + 0x880]
002277C0  44 01 61 1C                     add dword ptr [rcx + 0x1c], r12d
002277C4  0F B7 41 10                     movzx eax, word ptr [rcx + 0x10]
002277C8  66 39 01                        cmp word ptr [rcx], ax
002277CB  72 2A                           jb 0x1402277f7
002277CD  44 01 61 20                     add dword ptr [rcx + 0x20], r12d
002277D1  48 8B 8A 88 08 00 00            mov rcx, qword ptr [rdx + 0x888]
002277D8  44 01 61 1C                     add dword ptr [rcx + 0x1c], r12d
002277DC  0F B7 41 10                     movzx eax, word ptr [rcx + 0x10]
002277E0  66 39 01                        cmp word ptr [rcx], ax
002277E3  72 12                           jb 0x1402277f7
002277E5  44 01 61 20                     add dword ptr [rcx + 0x20], r12d
002277E9  48 8B 41 38                     mov rax, qword ptr [rcx + 0x38]
002277ED  49 8B C8                        mov rcx, r8
002277F0  E8 DB 32 49 00                  call 0x1406baad0
002277F5  EB 08                           jmp 0x1402277ff
002277F7  49 8B D0                        mov rdx, r8
002277FA  E8 B1 2D 49 00                  call 0x1406ba5b0
002277FF  41 8B C6                        mov eax, r14d
00227802  48 8B 8C 24 30 05 00 00         mov rcx, qword ptr [rsp + 0x530]
0022780A  48 33 CC                        xor rcx, rsp
0022780D  E8 2E 4E 48 00                  call 0x1406ac640
00227812  48 81 C4 40 05 00 00            add rsp, 0x540
00227819  41 5F                           pop r15
0022781B  41 5E                           pop r14
0022781D  41 5D                           pop r13
0022781F  41 5C                           pop r12
00227821  5F                              pop rdi
00227822  5E                              pop rsi
00227823  5B                              pop rbx
00227824  C3                              ret
00227825  CC                              int3
00227826  45 8B CD                        mov r9d, r13d
00227829  45 8B C2                        mov r8d, r10d
0022782C  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00227831  BA 05 00 00 00                  mov edx, 5
00227836  B9 1D 01 00 00                  mov ecx, 0x11d
0022783B  E8 20 5E 2D 00                  call 0x1404fd660
00227840  CC                              int3
00227841  45 8B CD                        mov r9d, r13d
00227844  45 8B C2                        mov r8d, r10d
00227847  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
0022784C  BA 05 00 00 00                  mov edx, 5
00227851  B9 1D 01 00 00                  mov ecx, 0x11d
00227856  E8 05 5E 2D 00                  call 0x1404fd660
0022785B  90                              nop
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpEventWriteFull(__int64 a1, unsigned __int16 a2, __int64 a3, int a4, __int64 a5, unsigned __int16 a6, unsigned __int16 a7, __int64 a8, __int64 a9, unsigned int a10, __int64 a11, __int64 a12, __int64 a13, __int64 a14, unsigned __int16 a15, __int64 a16, __int64 a17)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m358;
    unsigned __int64 v_stack_m368;
    unsigned __int64 v_stack_m370;
    unsigned __int64 v_stack_m378;
    unsigned __int64 v_stack_m388;
    unsigned __int64 v_stack_m390;
    unsigned __int64 v_stack_m398;
    unsigned int v_stack_m3A0;
    unsigned __int64 v_stack_m3A8;
    unsigned __int64 v_stack_m3B0;
    unsigned __int64 v_stack_m3B8;
    unsigned __int64 v_stack_m3C0;
    unsigned int v_stack_m3C8;
    unsigned __int64 v_stack_m3D0;
    unsigned __int64 v_stack_m3D8;
    unsigned __int64 v_stack_m3E0;
    unsigned __int64 v_stack_m3E8;
    unsigned __int64 v_stack_m3F0;
    unsigned __int64 v_stack_m3F8;
    unsigned __int64 v_stack_m400;
    unsigned __int64 v_stack_m408;
    unsigned __int64 v_stack_m410;
    unsigned __int64 v_stack_m418;
    unsigned __int64 v_stack_m420;
    unsigned __int64 v_stack_m428;
    unsigned __int64 v_stack_m430;
    unsigned __int16 v_stack_m438;
    unsigned __int64 v_stack_m440;
    unsigned __int64 v_stack_m448;
    unsigned __int64 v_stack_m450;
    unsigned __int64 v_stack_m458;
    unsigned int v_stack_m460;
    unsigned int v_stack_m468;
    unsigned __int64 v_stack_m470;
    unsigned __int64 v_stack_m478;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m480;
    unsigned __int64 v_stack_m488;
    unsigned int v_stack_m490;
    unsigned int v_stack_m498;
    unsigned __int64 v_stack_m4A0;
    unsigned __int64 v_stack_m4A8;
    unsigned __int16 v_stack_m4B0;
    unsigned __int64 v_stack_m4B8;
    unsigned __int64 v_stack_m4C0;
    unsigned __int64 v_stack_m4C8;
    unsigned __int64 v_stack_m4D0;
    unsigned int v_stack_m4D8;
    unsigned __int16 v_stack_m4E0;
    unsigned __int16 v_stack_m4E8;
    unsigned int v_stack_m4EC;
    unsigned int v_stack_m4F0;
    unsigned int v_stack_m4F4;
    unsigned __int8 v_stack_m4F8;
    unsigned int v_stack_m4FC;
    unsigned int v_stack_m500;
    unsigned __int8 v_stack_m504;
    unsigned int v_stack_m508;
    unsigned int v_stack_m50C;
    unsigned __int8 v_stack_m50F;
    unsigned __int8 v_stack_m510;
    unsigned int v_stack_m514;
    unsigned __int8 v_stack_m517;
    unsigned __int8 v_stack_m518;
    unsigned __int8 v_stack_m520;
    unsigned __int64 v_stack_m528;
    unsigned int v_stack_m530;
    unsigned __int8 v_stack_m538;
    unsigned __int8 v_stack_m540;
    unsigned __int64 v_stack_m548;
    unsigned int v_stack_m550;
    unsigned __int16 v_stack_m558;
    unsigned int v_stack_m58;
    unsigned __int64 v_stack_p20;
    unsigned __int16 v_stack_p78;

    v_rsp = (v_rsp) - (0x540ULL);
    result = (*(unsigned __int64 *)(v_rip + 12471062)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m4EC = a4;
    v_stack_m470 = a1;
    v_stack_m478 = a11;
    v_stack_m368 = a11;
    v_stack_m3C8 = (unsigned int)((unsigned int)(a10));
    v_stack_m370 = a9;
    v_stack_m438 = a6;
    v_stack_m3E0 = a1;
    v_stack_m460 = a4;
    v_stack_m3A0 = a4;
    v_stack_m4C8 = a5;
    v_stack_m3D8 = a11;
    v_stack_m450 = a12;
    v_stack_m480 = a13;
    v_stack_m398 = a16;
    v_stack_m420 = a17;
    v_r15 = 0;
    v_stack_m508 = 0;
    v_stack_m498 = 0;
    a2 = 0;
    result = memset(v_stack_m358, a2, 776, a4);
    v_stack_m4F0 = 0;
    v_stack_m4A0 = 0;
    v_stack_m410 = 0;
    v_stack_m428 = 0;
    v_stack_m3B0 = 0;
    v_stack_m3B8 = 0;
    v_stack_m4E8 = 0;
    v_stack_m400 = 0;
    result = (unsigned __int16)((a15) & (256));
    v_stack_m4B0 = (unsigned __int16)(result);
    a2 = (unsigned __int16)((a15) >> (9));
    a2 = (unsigned __int8)((a2) & ((unsigned __int8)(v_r15 + 1)));
    result = PsGetCurrentServerSiloGlobals(256, a2, 776, a4);
    v_stack_m430 = *(unsigned __int64 *)(result + 832);
    v_stack_m3E8 = *(unsigned __int64 *)(result + 832);
    v_stack_m504 = 0;
    v_stack_m418 = 0;
    v_stack_m4D8 = 0;
    if (a10 <= 128) goto loc_00225DE6;
    goto loc_00227802;
loc_00225DE6:
    if (a14 == 0) { a14 = v_stack_m470; }
    v_stack_m4A8 = a14;
    result = DecodeProviderTraits(v_stack_m398, a2, v_stack_m4E8, v_stack_m400);
    v_stack_m518 = 0;
    v_stack_m488 = *(unsigned __int64 *)(v_stack_m470 + 648);
    v_stack_m3F0 = *(unsigned __int64 *)(v_stack_m470 + 648);
    if (v_stack_m420 == 0) goto loc_00225E5E;
    v_rdi = 0;
    if (*(unsigned __int64 *)(v_stack_m420) != 0) {
        v_stack_m3B8 = *(unsigned __int64 *)(v_stack_m420);
        v_rdi = 4;
        v_stack_m518 = (unsigned __int8)(v_rdi);
    }
    v_stack_m3A8 = *(unsigned __int64 *)(gs_base + (0 + 392));
    result = v_stack_m450;
    if (v_stack_m450 == 0) { result = *(unsigned __int64 *)(gs_base + (0 + 392)); }
    v_stack_m450 = result;
    v_stack_m3D0 = result;
    result = KeGetEffectiveIrql(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, v_stack_m4E8, v_stack_m400);
    v_stack_m517 = (unsigned __int8)(result);
    v_stack_m50F = (unsigned __int8)(result);
    v_stack_m4F8 = 0;
    if (((unsigned __int8)(result)) < ((unsigned __int8)(v_r15 + 1))) {
        result = v_stack_m3A8;
        v_stack_m4F8 = (unsigned __int8)(v_r15 + 1);
    }
    v_rbx = (unsigned __int16)(~(a3));
    v_rsi = (unsigned __int16)((a2) & ((unsigned __int16)(v_rbx)));
    v_stack_m4F4 = (unsigned int)(v_rsi);
loc_00225ECD:
loc_00225EDD:
loc_00225EE5:
    v_stack_m4F0 = (unsigned int)(*(unsigned __int64 *)(gs_base + (0 + 392)));
    if (condition_is_equal) goto loc_002267EB;
    result = 0;
    v_stack_m388 = v_xmm0;
    v_stack_m378 = 0;
    v_stack_m3C0 = 0;
    v_stack_m514 = 80;
    v_stack_m4C0 = 0;
    v_stack_m458 = 0;
    v_stack_m500 = 0;
    v_stack_m4FC = 0;
    v_stack_m3F8 = 0;
    v_stack_m390 = 0;
    v_stack_m504 = 0;
    v_stack_m4D0 = v_r15 + 1;
    v_stack_m448 = v_r15 + 1;
    v_stack_m418 = 0;
    result = (unsigned __int16)(((unsigned __int16)((unsigned int)(v_stack_m4F4))) - ((unsigned __int16)(v_r15 + 1)));
    v_rbx = (unsigned __int16)(((unsigned int)(v_stack_m4F4)) & ((unsigned __int16)(result)));
    v_stack_m4F4 = (unsigned int)(v_rbx);
    v_stack_m4E0 = (unsigned __int16)(v_rbx);
    v_rbx = (*(unsigned __int64 *)(gs_base + (0 + 392)) + 4) << (5);
    v_rbx = (v_rbx) + (v_stack_m4A8);
    v_stack_m4B8 = v_rbx;
    if (v_stack_m480 == 0) goto loc_00225FD0;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rbx + 6)))) >> (5));
    result = (unsigned int)((*(unsigned __int16 *)(v_rbx + 6)) & (0x8000001FULL));
    if (!(condition_is_greater_or_equal)) {
        result = (unsigned int)((result) - ((unsigned int)(v_r15 + 1)));
        result = (unsigned int)((result) | (0xFFFFFFE0ULL));
        result = (unsigned int)((result) + ((unsigned int)(v_r15 + 1)));
    }
    if (condition_is_below) goto loc_00225EE5;
loc_00225FD0:
    result = EtwpLevelKeywordEnabled(v_rbx, *(unsigned __int8 *)(v_stack_m4C8 + 4), *(unsigned __int64 *)(v_stack_m4C8 + 8), (unsigned int)((unsigned int)(*(unsigned __int64 *)(gs_base + (0 + 392)))));
    if ((unsigned __int8)(result) == 0) goto loc_00225EE5;
    if (((v_stack_m4EC) & (2)) != 0) goto loc_00226013;
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 496)) >= 0) goto loc_00226020;
loc_00226013:
    if (((*(unsigned int *)(v_rbx + 8)) & (512)) != 0) goto loc_00225EE5;
loc_00226020:
    if (*(unsigned __int64 *)(v_stack_m4A8 + 640) == 0) goto loc_00226054;
    result = (*(unsigned __int64 *)(gs_base + (0 + 392))) * ((unsigned int)((unsigned int)(*(unsigned __int64 *)(gs_base + (0 + 392)))));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + *(unsigned __int64 *)(v_stack_m4A8 + 640) * 1))))) & (0x80000200ULL));
    if (((unsigned int)(result)) == 0x80000200ULL) goto loc_0022604F;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(result + *(unsigned __int64 *)(v_stack_m4A8 + 640) * 1))) & (0x80000100ULL));
    if (((unsigned int)(a1)) != 0x80000100ULL) goto loc_00226054;
loc_0022604F:
    goto loc_00226057;
loc_00226054:
loc_00226057:
    if (0 == 0) goto loc_002260B8;
    a3 = 0;
    v_stack_m538 = (unsigned __int8)(v_stack_m517);
    v_stack_m540 = 0;
    v_stack_m548 = v_stack_m478;
    v_stack_m550 = (unsigned int)((unsigned int)(a10));
    v_stack_m558 = (unsigned __int16)(*(unsigned __int16 *)(v_stack_m4C8));
    result = EtwpApplyEventIdPayloadFilter(v_stack_m4A8, (unsigned int)(v_stack_m4F0), a3, v_stack_m4C8);
    if ((unsigned __int8)(result) == 0) goto loc_00225ECD;
loc_002260B8:
    if (v_stack_m4B0 == 0) goto loc_0022613E;
    v_stack_m550 = 0;
    v_stack_m558 = *(unsigned __int64 *)(v_stack_m4C8 + 8);
    result = EtwpIsEventNameFilterEnabled(v_stack_m4A8, (unsigned int)((unsigned int)((unsigned int)(v_stack_m4F0))), (unsigned __int8)(v_stack_m517), *(unsigned __int8 *)(v_stack_m4C8 + 4));
    if ((unsigned __int8)(result) == 0) goto loc_0022613E;
    v_stack_m538 = 0;
    v_stack_m540 = *(unsigned __int64 *)(v_stack_m4C8 + 8);
    v_stack_m548 = (unsigned __int8)(*(unsigned __int8 *)(v_stack_m4C8 + 4));
    v_stack_m550 = (unsigned __int8)(v_stack_m517);
    v_stack_m558 = 0;
    result = EtwpApplyEventNameFilter(v_stack_m4A8, (unsigned int)((unsigned int)((unsigned int)(v_stack_m4F0))), (unsigned int)(a10), v_stack_m478);
    if ((unsigned __int8)(result) == 0) goto loc_00225ECD;
loc_0022613E:
    v_stack_m4D8 = (unsigned int)(*(unsigned __int16 *)(v_rbx + 6));
    v_stack_m468 = (unsigned int)(*(unsigned __int16 *)(v_rbx + 6));
    v_stack_m408 = *(unsigned __int16 *)(v_rbx + 6);
    if (v_stack_m517 >= 2) goto loc_002261C0;
    result = ExAcquireRundownProtectionCacheAwareEx(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m488 + 704) + *(unsigned __int16 *)(v_rbx + 6) * 8), (unsigned int)((unsigned int)(v_r15 + 1)), (unsigned int)(a10), v_stack_m478);
    if ((unsigned __int8)(result) == 0) goto loc_00226205;
    if (((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rbx + 6))))) >= (*(unsigned int *)(v_stack_m488 + 16))) goto loc_002261A9;
    v_stack_m4D0 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m488 + 712) + (unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rbx + 6))) * 8);
    v_stack_m448 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m488 + 712) + (unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rbx + 6))) * 8);
    goto loc_002261B9;
loc_002261A9:
    v_stack_m4D0 = v_r15 + 1;
    v_stack_m448 = v_r15 + 1;
loc_002261B9:
    v_stack_m504 = (unsigned __int8)(v_r15 + 1);
    goto loc_00226205;
loc_002261C0:
    v_stack_m408 = (unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rbx + 6)));
    if (((unsigned int)(*(unsigned __int64 *)(v_stack_m488 + 712))) >= (*(unsigned int *)(v_stack_m488 + 16))) goto loc_002261ED;
    v_stack_m4D0 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m488 + 712) + (unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rbx + 6))) * 8);
    v_stack_m448 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m488 + 712) + (unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rbx + 6))) * 8);
    goto loc_00226205;
loc_002261ED:
    v_stack_m4D0 = v_r15 + 1;
    v_stack_m448 = v_r15 + 1;
    v_stack_m408 = (unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rbx + 6)));
loc_00226205:
    if ((((unsigned __int8)(v_r15 + 1)) & ((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m488 + 712) + (unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rbx + 6))) * 8)))) == 0) goto loc_00226266;
    result = *(unsigned __int64 *)(v_stack_m488 + 712);
    if (v_stack_m504 != 0) {
        a1 = *(unsigned __int64 *)(v_stack_m488 + 704);
        a2 = (unsigned int)(v_r15 + 1);
        a1 = *(unsigned __int64 *)(a1 + (unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rbx + 6))) * 8);
        result = ExReleaseRundownProtectionCacheAwareEx(a1, a2, (unsigned int)(a10), v_stack_m478);
        result = Feature_1345841464__private_IsEnabledDeviceUsageNoInline(a1, a2, (unsigned int)(a10), v_stack_m478);
        a1 = v_stack_m504;
        a1 = (unsigned __int8)(a1);
        if ((unsigned int)(result) != 0) { a1 = 0; }
        v_stack_m504 = (unsigned int)(a1);
    }
    if (((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rbx + 6))))) != 3) goto loc_00225ECD;
    result = (unsigned int)(-((unsigned int)(*(unsigned int *)(v_stack_m488 + 4340))));
    v_r14 = (unsigned int)((0) & (758));
    v_r14 = (unsigned int)((v_r14) + (0xC0000008ULL));
    v_stack_m508 = (unsigned int)(v_r14);
    goto loc_00226A4B;
loc_00226266:
    result = -(v_stack_m370);
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rbx + 6)))) & (16));
    a1 = -(v_stack_m370);
    v_rsi = (unsigned int)((v_stack_m488) & (24));
    v_rsi = (unsigned int)((v_rsi) + (80));
    v_stack_m50C = (unsigned int)(v_rsi);
    if (((*(unsigned int *)(v_stack_m4B8 + 8)) & (0xFFFFFF9FULL)) == 0) goto loc_0022669F;
    if ((*(unsigned __int8 *)(v_rip + 13471710)) != 0) goto loc_002262D2;
    if (((v_stack_m4EC) & ((unsigned __int8)(v_r15 + 1))) != 0) goto loc_002262D2;
    result = MmCanThreadFault(a1, a2, (unsigned int)(a10), v_stack_m478);
    if ((unsigned int)(result) == 0) goto loc_002262D2;
    result = 256;
    if ((*(unsigned __int8 *)(v_stack_m3A8 + 1454)) != 0) {
        result = 0;
    }
    v_rbx = (unsigned int)((v_rbx) | ((unsigned int)(result)));
    v_stack_m50C = (unsigned int)(v_rsi);
    if (condition_is_above_or_equal) goto loc_00226322;
    if (v_stack_m430 == 0) goto loc_00226322;
    v_stack_m50C = (unsigned int)(v_rsi);
    v_r13 = (unsigned int)((unsigned int)(v_rsi));
    if (v_stack_m430 != (*(unsigned __int64 *)(v_rip + 14288804))) {
        v_r13 = *(unsigned __int16 *)(v_stack_m430 + 4496);
        v_r13 = (unsigned int)((v_r13) + (15));
        v_r13 = (unsigned int)((v_r13) & (0xFFFFFFF8ULL));
        v_r13 = (unsigned int)((v_r13) + ((unsigned int)(v_rsi)));
        v_stack_m50C = (unsigned int)(v_r13);
    }
    if ((((unsigned __int8)(v_r15 + 1)) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m4B8 + 8))))) == 0) goto loc_002263F8;
    if (condition_is_above_or_equal) goto loc_002263F8;
    if (v_stack_m4A0 != 0) goto loc_002263EA;
    result = ExpInterlockedPopEntrySList(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2176), v_stack_m430, (unsigned int)(a10), v_stack_m478);
    v_stack_m4A0 = result;
    if (result != 0) goto loc_002263BB;
    result = ExpInterlockedPopEntrySList(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2184), v_stack_m430, (unsigned int)(a10), v_stack_m478);
    v_stack_m4A0 = result;
    if (result == 0) {
        a2 = *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2184) + 44);
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2184) + 48);
        a3 = *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2184) + 40);
        a1 = *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2184) + 36);
        result = guard_dispatch_icall(a1, a2, a3, v_stack_m478);
        a1 = result;
        v_stack_m4A0 = result;
    }
    if (a1 != 0) {
        result = *(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36);
        *(unsigned int *)(a1) = (unsigned int)(result);
    }
    v_stack_m410 = a1;
    if (a1 != 0) {
        result = EtwpGetSidExtendedHeaderItem(a1, a2, a3, v_stack_m478);
        a1 = v_stack_m4A0;
    }
    if (a1 != 0) {
        v_rbx = (unsigned int)((v_rbx) | (2));
        result = *(unsigned __int16 *)(a1);
        v_r13 = (unsigned int)((v_r13) + ((unsigned int)(result)));
        v_stack_m50C = (unsigned int)(v_r13);
    }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m4B8 + 8)))) & (2)) != 0) {
        v_rbx = (unsigned int)((v_rbx) | ((unsigned int)(v_r15 + 1)));
        v_r13 = (unsigned int)((v_r13) + (16));
        v_stack_m50C = (unsigned int)(v_r13);
    }
    if (!sign_flag) goto loc_00226445;
    result = KeGetEffectiveIrql(a1, a2, a3, v_stack_m478);
    if (((unsigned __int8)(result)) < 2) goto loc_00226432;
    result = (unsigned __int8)(v_r15 + 1);
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 32)) == 0) {
        result = 0;
    }
    if ((unsigned __int8)(result) == 0) {
        v_rbx = (unsigned int)((v_rbx) | (64));
        v_r13 = (unsigned int)((v_r13) + (16));
        v_stack_m50C = (unsigned int)(v_r13);
    }
    if (!(condition_is_above_or_equal)) {
        v_r13 = (unsigned int)((v_r13) + (16));
        v_stack_m50C = (unsigned int)(v_r13);
    }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m4B8 + 8)))) & (4)) == 0) goto loc_0022669F;
    if ((*(unsigned __int8 *)(v_rip + 13471259)) != 0) goto loc_0022669F;
    if (*(unsigned __int64 *)(v_stack_m4A8 + 640) == 0) goto loc_002264C1;
    a1 = (a1) * ((unsigned int)(v_stack_m4F0));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + *(unsigned __int64 *)(v_stack_m4A8 + 640) * 1))))) & (0x80001000ULL));
    if (((unsigned int)(result)) == 0x80001000ULL) goto loc_002264BC;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + *(unsigned __int64 *)(v_stack_m4A8 + 640) * 1))))) & (0x80002000ULL));
    if (((unsigned int)(result)) == 0x80002000ULL) goto loc_002264BC;
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + *(unsigned __int64 *)(v_stack_m4A8 + 640) * 1))) & (0x80004000ULL));
    if (a2 != 0x80004000ULL) goto loc_002264C1;
loc_002264BC:
    goto loc_002264C4;
loc_002264C1:
loc_002264C4:
    if (0 == 0) goto loc_0022657E;
    result = (v_stack_m50F < 2) ? 1 : 0;
    v_stack_m558 = (unsigned __int8)(result);
    result = EtwpApplyLevelKwFilter(v_stack_m4A8, (unsigned int)((unsigned int)((unsigned int)(v_stack_m4F0))), *(unsigned __int8 *)(v_stack_m4C8 + 4), *(unsigned __int64 *)(v_stack_m4C8 + 8));
    if ((unsigned __int8)(result) == 0) goto loc_0022669F;
    a4 = (v_stack_m50F < 2) ? 1 : 0;
    result = EtwpApplyStackWalkIdFilter(*(unsigned __int16 *)(v_stack_m4C8), v_stack_m4A8, (unsigned int)((unsigned int)((unsigned int)(v_stack_m4F0))), a4);
    if ((unsigned __int8)(result) == 0) goto loc_0022669F;
    v_stack_m538 = (unsigned __int8)(v_r15 + 1);
    v_stack_m540 = *(unsigned __int64 *)(v_stack_m4C8 + 8);
    v_stack_m548 = (unsigned __int8)(*(unsigned __int8 *)(v_stack_m4C8 + 4));
    v_stack_m550 = (unsigned __int8)(v_stack_m517);
    v_stack_m558 = 0;
    result = EtwpApplyEventNameFilter(v_stack_m4A8, (unsigned int)((unsigned int)((unsigned int)(v_stack_m4F0))), (unsigned int)(a10), v_stack_m478);
    if ((unsigned __int8)(result) == 0) goto loc_0022669F;
loc_0022657E:
    if ((((unsigned __int8)(v_r15 + 1)) & ((unsigned __int8)(v_rdi))) != 0) goto loc_00226654;
    result = EtwpGetStackLookasideListEntry(v_stack_m4A8, (unsigned int)((unsigned int)((unsigned int)(v_stack_m4F0))), (unsigned int)(a10), v_stack_m478);
    v_stack_m3B0 = result;
    if (result == 0) goto loc_0022664C;
    v_stack_m428 = result + 32;
    v_rdi = (unsigned __int8)((v_rdi) | (2));
    a1 = (unsigned __int8)(v_r15 + 1);
    if (((*(unsigned int *)(v_stack_m4D0 + 816)) & (0x40000000ULL)) != 0) { a1 = 0; }
    if ((*(unsigned __int64 *)(v_stack_m470 + 40)) != (*(unsigned __int64 *)(v_rip - 2176401))) goto loc_0022660E;
    if ((*(unsigned __int64 *)(v_stack_m470 + 48)) != (*(unsigned __int64 *)(v_rip - 2176406))) goto loc_0022660E;
    if ((*(unsigned __int16 *)(v_stack_m4C8)) == 18) {
        v_rbx = (unsigned int)((v_rbx) | (32));
        a2 = v_stack_m470 + 80;
        a1 = 0;
    }
    v_stack_m550 = a2;
    v_stack_m558 = (unsigned __int8)(a1);
    result = EtwpGetStackExtendedHeaderItem(v_stack_m4D0, v_stack_m450, (unsigned int)(v_stack_m4EC), result);
    if ((unsigned __int8)(result) == 0) {
        a1 = v_stack_m3B0;
        result = EtwpReleaseStackLookasideListEntry(a1, v_stack_m450, (unsigned int)(v_stack_m4EC), result);
        v_rdi = (unsigned __int8)((v_rdi) & (253));
        v_stack_m428 = 0;
    }
    v_rdi = (unsigned __int8)((v_rdi) | ((unsigned __int8)(v_r15 + 1)));
    v_stack_m518 = (unsigned __int8)(v_rdi);
loc_00226654:
    if (v_stack_m428 == 0) goto loc_0022669F;
    if ((((unsigned __int8)(v_r15 + 1)) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m4D0 + 820))))) == 0) goto loc_00226691;
    result = EtwpGetCrimsonStackKey(v_stack_m4D0, v_stack_m428, v_stack_m418, result);
    if ((unsigned __int8)(result) == 0) goto loc_00226691;
    v_rbx = (unsigned int)((v_rbx) | (8));
    v_r13 = (unsigned int)((v_r13) + (24));
    goto loc_0022669A;
loc_00226691:
    v_rbx = (unsigned int)((v_rbx) | (4));
    v_r13 = (unsigned int)((v_r13) + ((unsigned int)(*(unsigned __int16 *)(v_stack_m428))));
loc_0022669A:
    v_stack_m50C = (unsigned int)(v_r13);
loc_0022669F:
    result = ((unsigned int)(v_stack_m58) + (unsigned int)(v_stack_m58) * 2) << (4);
    v_stack_m440 = result;
    v_stack_m490 = 0;
    if (a10 <= 0) goto loc_0022676F;
    v_rsi = (v_stack_m478) + (8);
loc_002266D8:
    result = Feature_1345841464__private_IsEnabledDeviceUsageNoInline(v_stack_m4D0, v_stack_m428, v_stack_m418, result);
    if ((unsigned int)(result) == 0) goto loc_002266ED;
    if ((*(unsigned int *)(v_rsi)) > 0xFFFFULL) goto loc_002267BE;
loc_002266ED:
    result = 0;
    if (v_stack_m4B0 != 0) {
        result = *(unsigned __int8 *)(v_rsi + 4);
    }
    if ((unsigned __int8)(result) == 0) goto loc_00226745;
    a1 = (unsigned int)(((unsigned __int8)(result)) - (1));
    if (condition_is_equal) goto loc_00226722;
    if (((unsigned int)(a1)) != 3) goto loc_0022674D;
    if ((*(unsigned int *)(v_rsi)) != 16) goto loc_0022674D;
    v_stack_m400 = *(unsigned __int64 *)(v_rsi - 8);
    goto loc_0022674D;
loc_00226722:
    result = Feature_1345841464__private_IsEnabledDeviceUsageNoInline(a1, v_stack_m428, v_stack_m418, result);
    if ((unsigned int)(result) != 0) goto loc_00226734;
    goto loc_0022673E;
loc_00226734:
    result = (unsigned int)(((unsigned int)(v_stack_m500)) + (*(unsigned int *)(v_rsi)));
    v_stack_m500 = (unsigned int)(result);
loc_0022673E:
    goto loc_0022674D;
loc_00226745:
    v_r13 = (unsigned int)((v_r13) + (*(unsigned int *)(v_rsi)));
    v_stack_m50C = (unsigned int)(v_r13);
loc_0022674D:
    result = (unsigned int)(((unsigned int)(v_stack_m490)) + ((unsigned int)(v_r15 + 1)));
    v_stack_m490 = (unsigned int)(result);
    v_rsi = (v_rsi) + (16);
    if (((unsigned int)(result)) < a10) goto loc_002266D8;
loc_0022676F:
    if (v_stack_m4FC == 0) goto loc_00226795;
    result = Feature_1345841464__private_IsEnabledDeviceUsageNoInline(a1, v_stack_m428, v_stack_m418, result);
    if ((unsigned int)(result) != 0) goto loc_00226846;
    result = (unsigned int)(((unsigned int)(v_stack_m500)) + (15));
    result = (unsigned int)((result) & (0xFFFFFFF8ULL));
loc_0022678D:
    v_r13 = (unsigned int)((v_r13) + ((unsigned int)(result)));
    v_stack_m50C = (unsigned int)(v_r13);
loc_00226795:
    if ((unsigned __int16)(v_stack_m4E8) == 0) goto loc_00226884;
    result = Feature_1345841464__private_IsEnabledDeviceUsageNoInline(a1, v_stack_m428, v_stack_m418, result);
    if ((unsigned int)(result) != 0) goto loc_00226872;
    result = (unsigned int)((v_stack_m4E8 + 15) & (0xFFFFFFF8ULL));
    goto loc_0022687C;
loc_002267BE:
    v_r14 = (unsigned int)(v_stack_m508);
    if (!sign_flag) { v_r14 = (unsigned int)((unsigned int)(0x80000005ULL)); }
loc_002267D4:
    v_stack_m508 = (unsigned int)(v_r14);
loc_002267EB:
    result = Feature_1345841464__private_IsEnabledDeviceUsageNoInline(a1, v_stack_m428, v_stack_m418, result);
    if ((unsigned int)(result) == 0) goto loc_002276AC;
    if (v_stack_m418 != 0) {
        a2 = *(unsigned __int64 *)(v_stack_m4D0 + 1056);
        a1 = v_stack_m418;
        result = EtwpDereferenceStackEntry(a1, a2, v_stack_m418, result);
    }
    if (v_stack_m504 == 0) goto loc_002276B4;
    result = ExReleaseRundownProtectionCacheAwareEx(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m488 + 704) + (unsigned int)(v_stack_m4D8) * 8), (unsigned int)((unsigned int)(v_r15 + 1)), v_stack_m418, result);
    goto loc_002276B4;
loc_00226846:
    result = (unsigned int)((result) + (15));
    result = (unsigned int)((result) & (0xFFFFFFF8ULL));
    if (((unsigned int)(result)) <= 0xFFFFULL) goto loc_0022678D;
loc_00226857:
    if (!sign_flag) { v_r14 = (unsigned int)((unsigned int)(0xC0000095ULL)); }
    goto loc_002267D4;
loc_00226872:
    result = (unsigned int)(((unsigned int)(v_stack_m4F4)) & (0xFFFFFFF8ULL));
    if (((unsigned int)(result)) > 0xFFFFULL) goto loc_00226857;
loc_0022687C:
    v_r13 = (unsigned int)((v_stack_m4D0) + ((unsigned int)(result)));
    v_stack_m50C = (unsigned int)(v_r13);
loc_00226884:
    *(unsigned int *)(v_rsp + v_stack_m440 * 1 + 584) = (unsigned int)(v_r13);
    result = Feature_Servicing_EtwLostEventsFlags__private_IsEnabledDeviceUsageNoInline(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m488 + 704) + (unsigned int)(v_stack_m4D8) * 8), (unsigned int)((unsigned int)(v_r15 + 1)), v_stack_m418, result);
    if ((unsigned int)(result) != 0) goto loc_002268A6;
    goto loc_002268C5;
loc_002268A6:
    result = 0;
    if ((((unsigned __int8)((unsigned int)(v_stack_m4EC))) & (4)) != 0) { result = 512; }
    if ((((unsigned __int8)((unsigned int)(v_stack_m4EC))) & (8)) != 0) {
        result = (unsigned int)((result) | (0x600ULL));
    }
    v_stack_m558 = (unsigned int)(result);
    result = EtwpReserveTraceBuffer(v_stack_m4D0, (unsigned int)((unsigned int)(v_r13)), v_stack_m388, v_stack_m3C0);
    v_stack_m4B8 = result;
    v_rsi = v_stack_m418;
    if (v_stack_m418 != 0) {
        result = v_stack_m4D0;
        a2 = *(unsigned __int64 *)(result + 1056);
        a1 = v_stack_m418;
        result = EtwpDereferenceStackEntry(a1, a2, v_stack_m388, v_stack_m3C0);
        result = Feature_1345841464__private_IsEnabledDeviceUsageNoInline(a1, a2, v_stack_m388, v_stack_m3C0);
        v_rsi = v_stack_m418;
        if ((unsigned int)(result) != 0) { v_rsi = 0; }
        v_stack_m418 = v_rsi;
    }
    if (result != 0) goto loc_00226A57;
    result = EtwpGetReserveTraceBufferStatus(v_stack_m4D0, (unsigned int)((unsigned int)(v_r13)), v_stack_m388, v_stack_m3C0);
    v_rsi = v_stack_m368;
    if ((unsigned int)((unsigned int)(v_stack_m4FC)) == 0) { v_rsi = 0; }
    v_r14 = (unsigned int)(v_stack_m3C8);
    if ((unsigned int)((unsigned int)(v_stack_m4FC)) == 0) { v_r14 = 0; }
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 13471435), v_rip - 2177326, v_stack_m388, v_stack_m3C0);
    if ((unsigned __int8)(result) != 0) {
        result = (v_stack_m50F < 2) ? 1 : 0;
        a3 = v_stack_m4D0 + 136;
        a1 = v_stack_m470;
        a1 = (a1) + (40);
        v_stack_m538 = 0;
        v_stack_m540 = (unsigned __int8)(result);
        v_stack_m548 = v_rsi;
        v_stack_m550 = (unsigned int)(v_r14);
        v_stack_m558 = (unsigned int)((unsigned int)((unsigned int)(result)));
        a4 = v_stack_m4EC;
        a2 = v_stack_m4C8;
        result = EtwpTraceLostEvent(a1, a2, a3, a4);
    }
    v_r14 = (unsigned int)(v_stack_m508);
    if (!(sign_flag)) {
        v_r14 = (unsigned int)(v_stack_m508);
        if (((*(unsigned int *)(v_stack_m4D0 + 12)) & (0x8000000ULL)) == 0) { v_r14 = (unsigned int)((unsigned int)((unsigned int)(result))); }
        v_stack_m508 = (unsigned int)(v_r14);
        v_stack_m498 = (unsigned int)(v_r14);
    }
    if ((unsigned __int8)((unsigned int)(v_stack_m504)) != 0) {
        a1 = v_stack_m488;
        a1 = *(unsigned __int64 *)(a1 + 704);
        a2 = (unsigned int)(v_r15 + 1);
        result = v_stack_m408;
        a1 = *(unsigned __int64 *)(a1 + result * 8);
        result = ExReleaseRundownProtectionCacheAwareEx(a1, a2, a3, a4);
        result = Feature_1345841464__private_IsEnabledDeviceUsageNoInline(a1, a2, a3, a4);
        a1 = (unsigned __int8)((unsigned int)(v_stack_m504));
        if ((unsigned int)(result) != 0) { a1 = 0; }
        v_stack_m504 = (unsigned __int8)(a1);
    }
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != ((unsigned int)((unsigned int)(0xC0000095ULL)))) goto loc_00225EDD;
    v_stack_m508 = (unsigned int)((unsigned int)(0xC0000095ULL));
loc_00226A4B:
    goto loc_002267EB;
loc_00226A57:
    *(unsigned __int64 *)(v_rsp + v_stack_m440 * 1 + 544) = v_stack_m4D0;
    *(unsigned __int64 *)(v_rsp + v_stack_m440 * 1 + 552) = (unsigned int)((unsigned int)((unsigned int)(0xC0000095ULL)));
    *(unsigned __int64 *)(v_rsp + v_stack_m440 * 1 + 560) = v_xmm0;
    *(unsigned __int64 *)(v_rsp + v_stack_m440 * 1 + 576) = v_xmm0;
    result = Feature_1345841464__private_IsEnabledDeviceUsageNoInline(v_stack_m4D0, (unsigned int)(0xC0000095ULL), v_stack_m480, a4);
    a1 = v_stack_m504;
    if ((unsigned int)(result) != 0) { a1 = 0; }
    v_stack_m504 = (unsigned int)((unsigned __int8)(a1));
    v_stack_m510 = (unsigned __int8)(a1);
    result = (unsigned int)(((unsigned int)((unsigned int)(v_stack_m4D0))) | (0xC0130000ULL));
    *(unsigned int *)((unsigned int)((unsigned int)((unsigned int)(0xC0000095ULL)))) = (unsigned int)(result);
    v_stack_m490 = (unsigned int)((unsigned int)((unsigned int)(0xC0000095ULL))) + 4;
    *(unsigned __int16 *)((unsigned int)((unsigned int)((unsigned int)(0xC0000095ULL))) + 4) = a6;
    *(unsigned __int16 *)((unsigned int)((unsigned int)((unsigned int)(0xC0000095ULL))) + 6) = a7;
    *(unsigned __int64 *)((unsigned int)((unsigned int)((unsigned int)(0xC0000095ULL))) + 40) = v_xmm0;
    if (v_stack_m400 != 0) goto loc_00226B1B;
    goto loc_00226B39;
loc_00226B1B:
    a2 = (unsigned __int16)((a6) | (128));
    *(unsigned __int16 *)((unsigned int)((unsigned int)((unsigned int)(0xC0000095ULL))) + 4) = a2;
loc_00226B39:
    *(unsigned __int64 *)((unsigned int)((unsigned int)((unsigned int)(0xC0000095ULL))) + 24) = v_xmm0;
    if (a8 == 0) goto loc_00226B51;
    goto loc_00226B58;
loc_00226B51:
loc_00226B58:
    *(unsigned __int64 *)((unsigned int)((unsigned int)((unsigned int)(0xC0000095ULL))) + 64) = v_xmm0;
    v_stack_m408 = (unsigned int)((unsigned int)((unsigned int)(0xC0000095ULL))) + 16;
    *(unsigned __int64 *)((unsigned int)((unsigned int)((unsigned int)(0xC0000095ULL))) + 16) = v_stack_m3C0;
    *(unsigned int *)((unsigned int)((unsigned int)((unsigned int)(0xC0000095ULL))) + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m450 + 1296)));
    *(unsigned int *)((unsigned int)((unsigned int)((unsigned int)(0xC0000095ULL))) + 12) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m450 + 1288)));
    *(unsigned int *)((unsigned int)((unsigned int)((unsigned int)(0xC0000095ULL))) + 56) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m450 + 652)));
    *(unsigned int *)((unsigned int)((unsigned int)((unsigned int)(0xC0000095ULL))) + 60) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m450 + 732)));
    if (((v_stack_p78) & ((unsigned __int16)((unsigned int)(0x400ULL)))) != 0) {
        a2 = (unsigned __int16)((a2) | ((unsigned __int16)((unsigned int)(0x400ULL))));
        *(unsigned __int16 *)((unsigned int)((unsigned int)((unsigned int)(0xC0000095ULL))) + 4) = a2;
    }
    if ((unsigned int)((unsigned int)(v_stack_m4F4)) == 0) goto loc_00226FF6;
    if (condition_is_above_or_equal) goto loc_00226C84;
    v_stack_m4C0 = (unsigned int)((unsigned int)((unsigned int)(0xC0000095ULL))) + 80;
    v_r14 = (unsigned __int16)((*(unsigned __int16 *)(v_stack_m430 + 4496)) + (15));
    v_r14 = (unsigned __int16)((v_r14) & ((unsigned __int16)((unsigned int)(0xFFF8ULL))));
    *(unsigned __int16 *)((unsigned int)((unsigned int)((unsigned int)(0xC0000095ULL))) + 80) = (unsigned __int16)(v_r14);
    *(unsigned __int16 *)((unsigned int)((unsigned int)((unsigned int)(0xC0000095ULL))) + 80 + 2) = 16;
    *(unsigned __int16 *)((unsigned int)((unsigned int)((unsigned int)(0xC0000095ULL))) + 80 + 6) = (unsigned __int16)(*(unsigned __int16 *)(v_stack_m430 + 4496));
    *(unsigned __int16 *)((unsigned int)((unsigned int)((unsigned int)(0xC0000095ULL))) + 80 + 4) = 0;
    v_r14 = (unsigned __int16)((v_r14) - ((unsigned __int16)(*(unsigned __int16 *)(v_stack_m430 + 4496))));
    v_r14 = (unsigned __int16)((v_r14) - (8));
    result = memcpy((unsigned int)((unsigned int)((unsigned int)(0xC0000095ULL))) + 80 + 8, *(unsigned __int64 *)(v_stack_m430 + 4488), *(unsigned __int16 *)(v_stack_m430 + 4496), a4);
    a1 = (*(unsigned __int16 *)(v_stack_m430 + 4496)) + ((unsigned int)((unsigned int)((unsigned int)(0xC0000095ULL))) + 80 + 8);
    a2 = 0;
    result = memset(a1, a2, (unsigned __int16)(v_r14), a4);
    v_r10 = (unsigned int)((*(unsigned __int16 *)(v_stack_m4C0)) + (80));
    v_stack_m514 = (unsigned int)(v_r10);
    v_stack_m458 = v_stack_m4C0;
    goto loc_00226C8C;
loc_00226C84:
loc_00226C8C:
    if (((16) & ((unsigned __int8)((unsigned int)(v_stack_m4F4)))) == 0) goto loc_00226CE9;
    a1 = ((unsigned int)((unsigned int)((unsigned int)(v_stack_m514)))) + (v_stack_m4B8);
    *(unsigned int *)(a1) = 0x10018ULL;
    *(unsigned int *)(a1 + 4) = 0x100000ULL;
    *(unsigned __int64 *)(a1 + 8) = v_xmm0;
    v_r10 = (unsigned int)(((unsigned int)(v_stack_m514)) + ((unsigned int)(16 + 8)));
    v_stack_m514 = (unsigned int)(v_r10);
    if (0 != 0) {
    }
    v_stack_m4C0 = a1;
    v_stack_m458 = a1;
    goto loc_00226CF1;
loc_00226CE9:
loc_00226CF1:
    if ((((unsigned __int8)((unsigned int)(v_stack_m4F4))) & (2)) == 0) goto loc_00226D5C;
    v_r14 = ((unsigned int)((unsigned int)(v_r10))) + (v_stack_m4B8);
    result = memcpy(v_r14, v_stack_m4A0, *(unsigned __int16 *)(v_stack_m4A0), a4);
    v_r10 = (unsigned int)(((unsigned int)(v_stack_m514)) + ((unsigned int)(*(unsigned __int16 *)(v_stack_m4A0))));
    v_stack_m514 = (unsigned int)(v_r10);
    if (v_stack_m4C0 != 0) {
    }
    v_stack_m4C0 = v_r14;
    v_stack_m458 = v_r14;
loc_00226D5C:
    if ((((unsigned __int8)(v_r15 + 1)) & ((unsigned __int8)((unsigned int)(v_stack_m4F4)))) == 0) goto loc_00226DBD;
    v_rsi = ((unsigned int)((unsigned int)(v_r10))) + (v_stack_m4B8);
    *(unsigned int *)(v_rsi) = 0x30010ULL;
    *(unsigned int *)(v_rsi + 4) = 0x40000ULL;
    result = PsGetCurrentProcessSessionId(v_r14, v_stack_m4A0, *(unsigned __int16 *)(v_stack_m4A0), a4);
    *(unsigned int *)(v_rsi + 8) = (unsigned int)(result);
    v_r10 = (unsigned int)(((unsigned int)(v_stack_m514)) + (16));
    v_stack_m514 = (unsigned int)(v_r10);
    if (v_r14 != 0) {
    }
    v_stack_m4C0 = v_rsi;
    v_stack_m458 = v_rsi;
loc_00226DBD:
    if ((((unsigned __int8)((unsigned int)(v_stack_m4F4))) & (64)) == 0) goto loc_00226E39;
    a2 = ((unsigned int)((unsigned int)(v_r10))) + (v_stack_m4B8);
    *(unsigned int *)(a2) = 0xD0010ULL;
    *(unsigned int *)(a2 + 4) = 0x80000ULL;
    result = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392))))) << (48);
    result = (result) | (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1656));
    *(unsigned __int64 *)(a2 + 8) = result;
    v_r10 = (unsigned int)((v_r10) + (16));
    v_stack_m514 = (unsigned int)(v_r10);
    if (v_rsi != 0) {
    }
    v_stack_m4C0 = a2;
    v_stack_m458 = a2;
loc_00226E39:
    if (!sign_flag) goto loc_00226EEC;
    a3 = ((unsigned int)((unsigned int)(v_r10))) + (v_stack_m4B8);
    *(unsigned int *)(a3) = 0xA0010ULL;
    *(unsigned int *)(a3 + 4) = 0x80000ULL;
    if ((((unsigned __int8)(v_rdi)) & (4)) != 0) goto loc_00226EB7;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35752)) + (8);
    a2 = (v_r15 + 1) + (v_r15 + 1);
    result = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36))) << (48);
    a2 = (a2) & (*(unsigned __int64 *)(gs_base + (0 + 32)));
    result = (result) | (a2);
    v_stack_m3B8 = result;
    v_rdi = (unsigned __int8)((v_rdi) | (4));
    v_stack_m518 = (unsigned __int8)(v_rdi);
    if (v_stack_m420 != 0) {
        *(unsigned __int64 *)(v_stack_m420) = result;
    }
    *(unsigned __int64 *)(a3 + 8) = v_stack_m3B8;
    v_r10 = (unsigned int)((v_r10) + (16));
    v_stack_m514 = (unsigned int)(v_r10);
    if (a2 != 0) {
    }
    v_stack_m4C0 = a3;
    v_stack_m458 = a3;
loc_00226EEC:
    if ((((unsigned __int8)((unsigned int)(v_stack_m4F4))) & (4)) == 0) goto loc_00226F8A;
    v_r14 = ((unsigned int)((unsigned int)(v_r10))) + (v_stack_m4B8);
    result = memcpy(v_r14, v_stack_m428, *(unsigned __int16 *)(v_stack_m428), v_stack_m4B8);
    if ((*(unsigned __int64 *)(v_r14 + 8)) == 0) goto loc_00226F49;
    if ((((unsigned __int8)((unsigned int)(v_stack_m4F4))) & (32)) != 0) goto loc_00226F49;
    v_stack_m558 = v_r14 + 8;
    result = EtwpQueueStackWalkApc(v_stack_m450, v_stack_m517, v_stack_m4D0, (unsigned __int8)(v_r15 + 1));
    if ((unsigned __int8)(result) == 0) {
        *(unsigned __int64 *)(v_r14 + 8) = 0;
    }
    v_r10 = (unsigned int)(((unsigned int)(v_stack_m514)) + ((unsigned int)(*(unsigned __int16 *)(v_stack_m428))));
    v_stack_m514 = (unsigned int)(v_r10);
    if (v_stack_m4C0 != 0) {
    }
    v_stack_m4C0 = v_r14;
    v_stack_m458 = v_r14;
    goto loc_00226F92;
loc_00226F8A:
loc_00226F92:
    if (((8) & ((unsigned __int8)((unsigned int)(v_stack_m4F4)))) == 0) goto loc_00227003;
    a1 = ((unsigned int)((unsigned int)(v_r10))) + (v_stack_m4B8);
    *(unsigned int *)(a1) = 0x120018ULL;
    *(unsigned int *)(a1 + 4) = 0x100000ULL;
    *(unsigned __int64 *)(a1 + 16) = v_stack_m418;
    *(unsigned __int64 *)(a1 + 8) = *(unsigned __int64 *)(v_stack_m428 + 8);
    v_r10 = (unsigned int)((v_r10) + ((unsigned int)(8 + 16)));
    v_stack_m514 = (unsigned int)(v_r10);
    if (v_r14 != 0) {
    }
    v_stack_m4C0 = a1;
    v_stack_m458 = a1;
    goto loc_00226FFE;
loc_00226FF6:
loc_00226FFE:
loc_00227003:
    if ((unsigned __int16)(v_stack_m4E8) == 0) goto loc_002271A8;
    v_r14 = ((unsigned int)((unsigned int)((unsigned int)(v_stack_m514)))) + (v_r14);
    v_stack_m440 = v_r14;
    v_rsi = (unsigned int)((15) + ((unsigned int)(v_stack_m4E8)));
    v_rsi = (unsigned __int16)((v_rsi) & ((unsigned __int16)((unsigned int)(0xFFF8ULL))));
    *(unsigned __int16 *)(v_r14) = (unsigned __int16)(v_rsi);
    *(unsigned int *)(v_r14 + 2) = 12;
    *(unsigned __int16 *)(v_r14 + 6) = (unsigned __int16)(v_stack_m4E8);
    v_rsi = (unsigned __int16)((v_rsi) - ((unsigned __int16)(v_stack_m4E8)));
    v_rsi = (unsigned __int16)((v_rsi) - (8));
    v_stack_m4F0 = (unsigned __int16)(v_rsi);
    result = memcpy(v_r14 + 8, v_stack_m398, (unsigned int)((unsigned int)(v_stack_m4E8)), 8 + 16);
    a1 = ((unsigned int)((unsigned int)(v_stack_m4E8)) + 8) + (v_r14);
    a2 = 0;
    result = memset(a1, a2, (unsigned __int16)(v_rsi), 8 + 16);
    goto loc_0022717E;
loc_0022717E:
    v_r10 = (unsigned int)(((unsigned int)(v_stack_m514)) + ((unsigned int)(*(unsigned __int16 *)(v_r14))));
    v_stack_m514 = (unsigned int)(v_r10);
    if (v_stack_m4C0 != 0) {
    }
    v_stack_m4C0 = v_r14;
loc_002271A8:
    if ((unsigned int)((unsigned int)(v_stack_m4FC)) == 0) goto loc_00227235;
    v_rbx = ((unsigned int)((unsigned int)(v_r10))) + (v_stack_m4B8);
    a2 = (unsigned int)((15) + ((unsigned int)((unsigned int)(v_stack_m500))));
    a2 = (unsigned __int16)((a2) & ((unsigned __int16)((unsigned int)(0xFFF8ULL))));
    *(unsigned __int16 *)(v_rbx) = a2;
    *(unsigned int *)(v_rbx + 2) = 11;
    *(unsigned __int16 *)(v_rbx + 6) = (unsigned __int16)((unsigned int)(v_stack_m500));
    a2 = (unsigned __int16)((a2) - ((unsigned __int16)((unsigned int)(v_stack_m500))));
    a2 = (unsigned __int16)((a2) - (8));
    v_stack_m3F8 = v_rbx + 8;
    a1 = (v_rbx + 8) + ((unsigned int)(v_stack_m500));
    v_stack_m390 = a1;
    a2 = 0;
    result = memset(a1, a2, a2, 8 + 16);
    v_r10 = (unsigned int)(((unsigned int)(v_stack_m514)) + ((unsigned int)(*(unsigned __int16 *)(v_rbx))));
    v_stack_m514 = (unsigned int)(v_r10);
    if (v_stack_m4C0 != 0) {
    }
loc_00227238:
    v_stack_m500 = 0;
    if (0 >= a10) goto loc_00227600;
    result = (0) + (0);
    v_stack_m490 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m478 + result * 8 + 8)));
    if (v_stack_m4B0 != 0) goto loc_00227276;
    goto loc_0022727B;
loc_00227276:
loc_0022727B:
    if ((unsigned __int8)(*(unsigned __int8 *)(v_stack_m478 + 0 * 8 + 12)) == 0) goto loc_002274D3;
    a1 = (unsigned int)(((unsigned __int8)(*(unsigned __int8 *)(v_stack_m478 + 0 * 8 + 12))) - (1));
    if (condition_is_equal) goto loc_00227386;
    if (((unsigned int)(a1)) != 2) goto loc_002275F0;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m478 + result * 8 + 8)))) != 8) goto loc_002275F0;
    *(unsigned __int64 *)(v_stack_m408) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m478 + result * 8));
    goto loc_002275F0;
loc_00227386:
    if (v_stack_m3F8 == 0) goto loc_00227826;
    v_stack_m440 = (unsigned int)(*(unsigned int *)(v_stack_m478 + result * 8 + 8)) + v_stack_m3F8 * 1;
    if (((unsigned int)(*(unsigned int *)(v_stack_m478 + result * 8 + 8)) + v_stack_m3F8 * 1) > v_stack_m390) goto loc_00227826;
    if ((unsigned int)((unsigned int)(v_stack_m4FC)) == 0) goto loc_00227826;
    result = memcpy(v_stack_m3F8, *(unsigned __int64 *)(v_stack_m478 + result * 8), (unsigned int)(*(unsigned int *)(v_stack_m478 + result * 8 + 8)), *(unsigned __int64 *)(v_stack_m478 + result * 8));
    goto loc_002274B9;
loc_002274B9:
    v_stack_m3F8 = (unsigned int)(*(unsigned int *)(v_stack_m478 + result * 8 + 8)) + v_stack_m3F8 * 1;
    v_r11 = (unsigned int)(((unsigned int)(v_stack_m4FC)) - 1);
    v_stack_m4FC = (unsigned int)(v_r11);
    goto loc_002275F0;
loc_002274D3:
    a1 = ((unsigned int)((unsigned int)((unsigned int)(v_stack_m514)))) + (v_stack_m4B8);
    v_stack_m440 = a1;
    v_r10 = (unsigned int)(((unsigned int)(v_stack_m514)) + ((unsigned int)(*(unsigned __int64 *)(v_stack_m478 + result * 8))));
    v_stack_m514 = (unsigned int)(v_r10);
    if (((unsigned int)(v_r10)) > ((unsigned int)(v_stack_m4D0))) goto loc_00227841;
    result = memcpy(a1, *(unsigned __int64 *)(v_stack_m478 + result * 8), *(unsigned __int64 *)(v_stack_m478 + result * 8), *(unsigned __int64 *)(v_stack_m478 + result * 8));
    goto loc_002275F0;
loc_002275F0:
    v_rsi = (unsigned int)((0) + ((unsigned int)(v_r15 + 1)));
    goto loc_00227238;
loc_00227600:
    if (((*(unsigned int *)(v_stack_m4D0 + 12)) & (0x80000ULL)) == 0) goto loc_0022763D;
    if ((*(unsigned __int8 *)(v_rip + 13762499)) != 0) goto loc_00227624;
    if ((*(unsigned __int8 *)(v_rip + 12465146)) == 0) goto loc_0022762D;
loc_00227624:
    if ((*(unsigned __int8 *)(v_rip + 13821576)) != 0) {
        a2 = v_stack_m388;
        a1 = v_stack_m4D0;
        result = EtwpSendTraceEvent(a1, a2, *(unsigned __int64 *)(v_stack_m478 + result * 8), *(unsigned __int64 *)(v_stack_m478 + result * 8));
    }
    if ((*(unsigned __int64 *)(v_stack_m4D0 + 1568)) != 0) {
        a3 = v_stack_m470;
        a3 = (a3) + (40);
        a4 = 0;
        a2 = v_stack_m388;
        a1 = v_stack_m4D0;
        result = EtwpInvokeEventCallback(a1, a2, a3, a4);
    }
    if (v_stack_m480 == 0) goto loc_00225EE5;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m4D8)))) >> (5));
    a1 = (unsigned int)(((unsigned int)(v_stack_m4D8)) & (31));
    *(unsigned int *)(v_stack_m480 + (unsigned int)((unsigned int)(result)) * 4) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m480 + result * 4)));
    goto loc_00225EE5;
loc_002276AC:
loc_002276B4:
    result = (unsigned int)(*(unsigned int *)(v_stack_m480 + result * 4));
    if ((((unsigned __int8)(v_rdi)) & (2)) != 0) {
        a1 = v_stack_m3B0;
        result = EtwpReleaseStackLookasideListEntry(a1, (unsigned int)((unsigned int)(result)), v_stack_m480, a4);
    }
    if (sign_flag) goto loc_00227725;
    if (v_stack_m58 <= 0) goto loc_0022778C;
loc_002276EE:
    result = EtwpReleaseTraceBuffer(v_stack_m358 + 16, (unsigned int)((unsigned int)(result)), v_stack_m480, a4);
    if (((unsigned __int8)(v_stack_m517)) < 2) {
        result = *(unsigned __int64 *)(v_stack_m358);
        result = *(unsigned int *)(result);
        a1 = *(unsigned __int64 *)(v_stack_m488 + 704);
        a2 = (unsigned int)(v_r15 + 1);
        a1 = *(unsigned __int64 *)(a1 + result * 8);
        result = ExReleaseRundownProtectionCacheAwareEx(a1, a2, v_stack_m480, a4);
    }
    v_rbx = (v_stack_m358) + (48);
    v_rdi = ((unsigned int)(v_stack_m58)) - (v_r15 + 1);
    if (condition_is_not_equal) goto loc_002276EE;
    goto loc_0022778C;
loc_00227725:
    result = (v_stack_m50F < 2) ? 1 : 0;
    v_stack_m520 = 0;
    v_stack_m528 = v_stack_m478;
    v_stack_m530 = (unsigned int)((unsigned int)(a10));
    v_stack_m538 = (unsigned __int8)(result);
    v_stack_m540 = v_stack_m4C8;
    v_stack_m548 = (unsigned int)((unsigned int)(v_stack_m508));
    v_stack_m550 = (unsigned int)((unsigned int)(v_stack_m4EC));
    v_stack_m558 = (unsigned __int16)(v_rbx);
    result = EtwpFailLogging(*(unsigned __int8 *)(v_stack_m4C8 + 4), *(unsigned __int64 *)(v_stack_m4C8 + 8), v_stack_m470, v_stack_m358);
loc_0022778C:
    if (v_stack_m4F8 != 0) {
        a1 = v_stack_m3A8;
        result = KiLeaveCriticalRegionUnsafe(a1, *(unsigned __int64 *)(v_stack_m4C8 + 8), v_stack_m470, v_stack_m358);
    }
    if (v_stack_m4A0 == 0) goto loc_002277FF;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2176))) < ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2176) + 16)))) goto loc_002277F7;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2184))) < ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2184) + 16)))) goto loc_002277F7;
    result = guard_dispatch_icall(v_stack_m4A0, *(unsigned __int64 *)(gs_base + (0 + 32)), v_stack_m4A0, v_stack_m358);
    goto loc_002277FF;
loc_002277F7:
    result = ExpInterlockedPushEntrySList(v_stack_m4A0, v_stack_m4A0, v_stack_m4A0, v_stack_m358);
loc_002277FF:
loc_00227802:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, v_stack_m4A0, v_stack_m4A0, v_stack_m358);
    v_rsp = (v_rsp) + (0x540ULL);
    return result;
loc_00227826:
    v_stack_p20 = 0;
    result = KeBugCheckEx(285, 5, (unsigned int)((unsigned int)(v_stack_m4C8)), (unsigned int)((unsigned int)(v_stack_m4D0)));
loc_00227841:
    v_stack_p20 = 0;
    result = KeBugCheckEx(285, 5, (unsigned int)((unsigned int)(v_stack_m4C8)), (unsigned int)((unsigned int)(v_stack_m4D0)));
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t EtwpEventWriteFull(int64_t Arg1, uint16_t Arg2, int64_t Arg3, int32_t Arg4, int64_t Arg5, uint16_t Arg6, uint16_t Arg7, int64_t Arg8, void *Arg9, uint32_t Arg10, int64_t Arg11, int64_t Arg12, int64_t Arg13, int64_t Arg14, uint16_t Arg15, int64_t Arg16, int64_t Arg17)
{
    uint8_t *arg9 = (uint8_t *)Arg9;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m358;
    uint64_t v_stack_m368;
    uint64_t v_stack_m370;
    uint64_t v_stack_m378;
    uint64_t v_stack_m388;
    uint64_t v_stack_m390;
    uint64_t v_stack_m398;
    uint32_t v_stack_m3A0;
    uint64_t v_stack_m3A8;
    uint64_t v_stack_m3B0;
    uint64_t v_stack_m3B8;
    uint64_t v_stack_m3C0;
    uint32_t v_stack_m3C8;
    uint64_t v_stack_m3D0;
    uint64_t v_stack_m3D8;
    uint64_t v_stack_m3E0;
    uint64_t v_stack_m3E8;
    uint64_t v_stack_m3F0;
    uint64_t v_stack_m3F8;
    uint64_t v_stack_m400;
    uint64_t v_stack_m408;
    uint64_t v_stack_m410;
    uint64_t v_stack_m418;
    uint64_t v_stack_m420;
    uint64_t v_stack_m428;
    uint64_t v_stack_m430;
    uint16_t v_stack_m438;
    uint64_t v_stack_m440;
    uint64_t v_stack_m448;
    uint64_t v_stack_m450;
    uint64_t v_stack_m458;
    uint32_t v_stack_m460;
    uint32_t v_stack_m468;
    uint64_t v_stack_m470;
    uint64_t v_stack_m478;
    uint64_t v_stack_m48;
    uint64_t v_stack_m480;
    uint64_t v_stack_m488;
    uint32_t v_stack_m490;
    uint32_t v_stack_m498;
    uint64_t v_stack_m4A0;
    uint64_t v_stack_m4A8;
    uint16_t v_stack_m4B0;
    uint64_t v_stack_m4B8;
    uint64_t v_stack_m4C0;
    uint64_t v_stack_m4C8;
    uint64_t v_stack_m4D0;
    uint32_t v_stack_m4D8;
    uint16_t v_stack_m4E0;
    uint16_t v_stack_m4E8;
    uint32_t v_stack_m4EC;
    uint32_t v_stack_m4F0;
    uint32_t v_stack_m4F4;
    uint8_t v_stack_m4F8;
    uint32_t v_stack_m4FC;
    uint32_t v_stack_m500;
    uint8_t v_stack_m504;
    uint32_t v_stack_m508;
    uint32_t v_stack_m50C;
    uint8_t v_stack_m50F;
    uint8_t v_stack_m510;
    uint32_t v_stack_m514;
    uint8_t v_stack_m517;
    uint8_t v_stack_m518;
    uint8_t v_stack_m520;
    uint64_t v_stack_m528;
    uint32_t v_stack_m530;
    uint8_t v_stack_m538;
    uint8_t v_stack_m540;
    uint64_t v_stack_m548;
    uint32_t v_stack_m550;
    uint16_t v_stack_m558;
    uint32_t v_stack_m58;
    uint64_t v_stack_p20;
    uint16_t v_stack_p78;

    local_rsp = (local_rsp) - (0x540ULL);
    result = (*(uint64_t *)(v_rip + 0xBE4B16)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m4EC = Arg4;
    v_stack_m470 = Arg1;
    v_stack_m478 = Arg11;
    v_stack_m368 = Arg11;
    v_stack_m3C8 = (uint32_t)((uint32_t)(Arg10));
    v_stack_m370 = Arg9;
    v_stack_m438 = Arg6;
    v_stack_m3E0 = Arg1;
    v_stack_m460 = Arg4;
    v_stack_m3A0 = Arg4;
    v_stack_m4C8 = Arg5;
    v_stack_m3D8 = Arg11;
    v_stack_m450 = Arg12;
    v_stack_m480 = Arg13;
    v_stack_m398 = Arg16;
    v_stack_m420 = Arg17;
    local_r15 = 0;
    v_stack_m508 = 0;
    v_stack_m498 = 0;
    Arg2 = 0;
    result = memset(v_stack_m358, Arg2, 776, Arg4);
    v_stack_m4F0 = 0;
    v_stack_m4A0 = 0;
    v_stack_m410 = 0;
    v_stack_m428 = 0;
    v_stack_m3B0 = 0;
    v_stack_m3B8 = 0;
    v_stack_m4E8 = 0;
    v_stack_m400 = 0;
    result = (uint16_t)((Arg15) & (256));
    v_stack_m4B0 = (uint16_t)(result);
    Arg2 = (uint16_t)((Arg15) >> (9));
    Arg2 = (uint8_t)((Arg2) & ((uint8_t)(local_r15 + 1)));
    result = PsGetCurrentServerSiloGlobals(256, Arg2, 776, Arg4);
    v_stack_m430 = *(uint64_t *)(result + 0x340);
    v_stack_m3E8 = *(uint64_t *)(result + 0x340);
    v_stack_m504 = 0;
    v_stack_m418 = 0;
    v_stack_m4D8 = 0;
    if (Arg10 <= 128) goto loc_00225DE6;
    goto loc_00227802;
loc_00225DE6:
    if (Arg14 == 0) { Arg14 = v_stack_m470; }
    v_stack_m4A8 = Arg14;
    result = DecodeProviderTraits(v_stack_m398, Arg2, v_stack_m4E8, v_stack_m400);
    v_stack_m518 = 0;
    v_stack_m488 = *(uint64_t *)(v_stack_m470 + 0x288);
    v_stack_m3F0 = *(uint64_t *)(v_stack_m470 + 0x288);
    if (v_stack_m420 == 0) goto loc_00225E5E;
    local_rdi = 0;
    if (*(uint64_t *)(v_stack_m420) != 0) {
        v_stack_m3B8 = *(uint64_t *)(v_stack_m420);
        local_rdi = 4;
        v_stack_m518 = (uint8_t)(local_rdi);
    }
    v_stack_m3A8 = *(uint64_t *)(gs_base + (0 + 0x188));
    result = v_stack_m450;
    if (v_stack_m450 == 0) { result = *(uint64_t *)(gs_base + (0 + 0x188)); }
    v_stack_m450 = result;
    v_stack_m3D0 = result;
    result = KeGetEffectiveIrql(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, v_stack_m4E8, v_stack_m400);
    v_stack_m517 = (uint8_t)(result);
    v_stack_m50F = (uint8_t)(result);
    v_stack_m4F8 = 0;
    if (((uint8_t)(result)) < ((uint8_t)(local_r15 + 1))) {
        result = v_stack_m3A8;
        v_stack_m4F8 = (uint8_t)(local_r15 + 1);
    }
    local_rbx = (uint16_t)(~(Arg3));
    local_rsi = (uint16_t)((Arg2) & ((uint16_t)(local_rbx)));
    v_stack_m4F4 = (uint32_t)(local_rsi);
loc_00225ECD:
loc_00225EDD:
loc_00225EE5:
    v_stack_m4F0 = (uint32_t)(*(uint64_t *)(gs_base + (0 + 0x188)));
    if (condition_is_equal) goto loc_002267EB;
    result = 0;
    v_stack_m388 = v_xmm0;
    v_stack_m378 = 0;
    v_stack_m3C0 = 0;
    v_stack_m514 = 80;
    v_stack_m4C0 = 0;
    v_stack_m458 = 0;
    v_stack_m500 = 0;
    v_stack_m4FC = 0;
    v_stack_m3F8 = 0;
    v_stack_m390 = 0;
    v_stack_m504 = 0;
    v_stack_m4D0 = local_r15 + 1;
    v_stack_m448 = local_r15 + 1;
    v_stack_m418 = 0;
    result = (uint16_t)(((uint16_t)((uint32_t)(v_stack_m4F4))) - ((uint16_t)(local_r15 + 1)));
    local_rbx = (uint16_t)(((uint32_t)(v_stack_m4F4)) & ((uint16_t)(result)));
    v_stack_m4F4 = (uint32_t)(local_rbx);
    v_stack_m4E0 = (uint16_t)(local_rbx);
    local_rbx = (*(uint64_t *)(gs_base + (0 + 0x188)) + 4) << (5);
    local_rbx = (local_rbx) + (v_stack_m4A8);
    v_stack_m4B8 = local_rbx;
    if (v_stack_m480 == 0) goto loc_00225FD0;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(local_rbx + 0x6)))) >> (5));
    result = (uint32_t)((*(uint16_t *)(local_rbx + 0x6)) & (0x8000001FULL));
    if (!(condition_is_greater_or_equal)) {
        result = (uint32_t)((result) - ((uint32_t)(local_r15 + 1)));
        result = (uint32_t)((result) | (0xFFFFFFE0ULL));
        result = (uint32_t)((result) + ((uint32_t)(local_r15 + 1)));
    }
    if (condition_is_below) goto loc_00225EE5;
loc_00225FD0:
    result = EtwpLevelKeywordEnabled(local_rbx, *(uint8_t *)(v_stack_m4C8 + 0x4), *(uint64_t *)(v_stack_m4C8 + 0x8), (uint32_t)((uint32_t)(*(uint64_t *)(gs_base + (0 + 0x188)))));
    if ((uint8_t)(result) == 0) goto loc_00225EE5;
    if (((v_stack_m4EC) & (2)) != 0) goto loc_00226013;
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x1F0)) >= 0) goto loc_00226020;
loc_00226013:
    if (((*(uint32_t *)(local_rbx + 0x8)) & (512)) != 0) goto loc_00225EE5;
loc_00226020:
    if (*(uint64_t *)(v_stack_m4A8 + 0x280) == 0) goto loc_00226054;
    result = (*(uint64_t *)(gs_base + (0 + 0x188))) * ((uint32_t)((uint32_t)(*(uint64_t *)(gs_base + (0 + 0x188)))));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + *(uint64_t *)(v_stack_m4A8 + 0x280) * 1))))) & (0x80000200ULL));
    if (((uint32_t)(result)) == 0x80000200ULL) goto loc_0022604F;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(result + *(uint64_t *)(v_stack_m4A8 + 0x280) * 1))) & (0x80000100ULL));
    if (((uint32_t)(Arg1)) != 0x80000100ULL) goto loc_00226054;
loc_0022604F:
    goto loc_00226057;
loc_00226054:
loc_00226057:
    if (0 == 0) goto loc_002260B8;
    Arg3 = 0;
    v_stack_m538 = (uint8_t)(v_stack_m517);
    v_stack_m540 = 0;
    v_stack_m548 = v_stack_m478;
    v_stack_m550 = (uint32_t)((uint32_t)(Arg10));
    v_stack_m558 = (uint16_t)(*(uint16_t *)(v_stack_m4C8));
    result = EtwpApplyEventIdPayloadFilter(v_stack_m4A8, (uint32_t)(v_stack_m4F0), Arg3, v_stack_m4C8);
    if ((uint8_t)(result) == 0) goto loc_00225ECD;
loc_002260B8:
    if (v_stack_m4B0 == 0) goto loc_0022613E;
    v_stack_m550 = 0;
    v_stack_m558 = *(uint64_t *)(v_stack_m4C8 + 0x8);
    result = EtwpIsEventNameFilterEnabled(v_stack_m4A8, (uint32_t)((uint32_t)((uint32_t)(v_stack_m4F0))), (uint8_t)(v_stack_m517), *(uint8_t *)(v_stack_m4C8 + 0x4));
    if ((uint8_t)(result) == 0) goto loc_0022613E;
    v_stack_m538 = 0;
    v_stack_m540 = *(uint64_t *)(v_stack_m4C8 + 0x8);
    v_stack_m548 = (uint8_t)(*(uint8_t *)(v_stack_m4C8 + 0x4));
    v_stack_m550 = (uint8_t)(v_stack_m517);
    v_stack_m558 = 0;
    result = EtwpApplyEventNameFilter(v_stack_m4A8, (uint32_t)((uint32_t)((uint32_t)(v_stack_m4F0))), (uint32_t)(Arg10), v_stack_m478);
    if ((uint8_t)(result) == 0) goto loc_00225ECD;
loc_0022613E:
    v_stack_m4D8 = (uint32_t)(*(uint16_t *)(local_rbx + 0x6));
    v_stack_m468 = (uint32_t)(*(uint16_t *)(local_rbx + 0x6));
    v_stack_m408 = *(uint16_t *)(local_rbx + 0x6);
    if (v_stack_m517 >= 2) goto loc_002261C0;
    result = ExAcquireRundownProtectionCacheAwareEx(*(uint64_t *)(*(uint64_t *)(v_stack_m488 + 0x2C0) + *(uint16_t *)(local_rbx + 0x6) * 8), (uint32_t)((uint32_t)(local_r15 + 1)), (uint32_t)(Arg10), v_stack_m478);
    if ((uint8_t)(result) == 0) goto loc_00226205;
    if (((uint32_t)((uint32_t)((uint32_t)(*(uint16_t *)(local_rbx + 0x6))))) >= (*(uint32_t *)(v_stack_m488 + 0x10))) goto loc_002261A9;
    v_stack_m4D0 = *(uint64_t *)(*(uint64_t *)(v_stack_m488 + 0x2C8) + (uint32_t)((uint32_t)(*(uint16_t *)(local_rbx + 0x6))) * 8);
    v_stack_m448 = *(uint64_t *)(*(uint64_t *)(v_stack_m488 + 0x2C8) + (uint32_t)((uint32_t)(*(uint16_t *)(local_rbx + 0x6))) * 8);
    goto loc_002261B9;
loc_002261A9:
    v_stack_m4D0 = local_r15 + 1;
    v_stack_m448 = local_r15 + 1;
loc_002261B9:
    v_stack_m504 = (uint8_t)(local_r15 + 1);
    goto loc_00226205;
loc_002261C0:
    v_stack_m408 = (uint32_t)((uint32_t)(*(uint16_t *)(local_rbx + 0x6)));
    if (((uint32_t)(*(uint64_t *)(v_stack_m488 + 0x2C8))) >= (*(uint32_t *)(v_stack_m488 + 0x10))) goto loc_002261ED;
    v_stack_m4D0 = *(uint64_t *)(*(uint64_t *)(v_stack_m488 + 0x2C8) + (uint32_t)((uint32_t)(*(uint16_t *)(local_rbx + 0x6))) * 8);
    v_stack_m448 = *(uint64_t *)(*(uint64_t *)(v_stack_m488 + 0x2C8) + (uint32_t)((uint32_t)(*(uint16_t *)(local_rbx + 0x6))) * 8);
    goto loc_00226205;
loc_002261ED:
    v_stack_m4D0 = local_r15 + 1;
    v_stack_m448 = local_r15 + 1;
    v_stack_m408 = (uint32_t)((uint32_t)(*(uint16_t *)(local_rbx + 0x6)));
loc_00226205:
    if ((((uint8_t)(local_r15 + 1)) & ((uint8_t)(*(uint64_t *)(*(uint64_t *)(v_stack_m488 + 0x2C8) + (uint32_t)((uint32_t)(*(uint16_t *)(local_rbx + 0x6))) * 8)))) == 0) goto loc_00226266;
    result = *(uint64_t *)(v_stack_m488 + 0x2C8);
    if (v_stack_m504 != 0) {
        Arg1 = *(uint64_t *)(v_stack_m488 + 0x2C0);
        Arg2 = (uint32_t)(local_r15 + 1);
        Arg1 = *(uint64_t *)(Arg1 + (uint32_t)((uint32_t)(*(uint16_t *)(local_rbx + 0x6))) * 8);
        result = ExReleaseRundownProtectionCacheAwareEx(Arg1, Arg2, (uint32_t)(Arg10), v_stack_m478);
        result = Feature_1345841464__private_IsEnabledDeviceUsageNoInline(Arg1, Arg2, (uint32_t)(Arg10), v_stack_m478);
        Arg1 = v_stack_m504;
        Arg1 = (uint8_t)(Arg1);
        if ((uint32_t)(result) != 0) { Arg1 = 0; }
        v_stack_m504 = (uint32_t)(Arg1);
    }
    if (((uint32_t)((uint32_t)((uint32_t)(*(uint16_t *)(local_rbx + 0x6))))) != 3) goto loc_00225ECD;
    result = (uint32_t)(-((uint32_t)(*(uint32_t *)(v_stack_m488 + 0x10F4))));
    local_r14 = (uint32_t)((0) & (758));
    local_r14 = (uint32_t)((local_r14) + (0xC0000008ULL));
    v_stack_m508 = (uint32_t)(local_r14);
    goto loc_00226A4B;
loc_00226266:
    result = -(v_stack_m370);
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(local_rbx + 0x6)))) & (16));
    Arg1 = -(v_stack_m370);
    local_rsi = (uint32_t)((v_stack_m488) & (24));
    local_rsi = (uint32_t)((local_rsi) + (80));
    v_stack_m50C = (uint32_t)(local_rsi);
    if (((*(uint32_t *)(v_stack_m4B8 + 0x8)) & (0xFFFFFF9FULL)) == 0) goto loc_0022669F;
    if ((*(uint8_t *)(v_rip + 0xCD8FDE)) != 0) goto loc_002262D2;
    if (((v_stack_m4EC) & ((uint8_t)(local_r15 + 1))) != 0) goto loc_002262D2;
    result = MmCanThreadFault(Arg1, Arg2, (uint32_t)(Arg10), v_stack_m478);
    if ((uint32_t)(result) == 0) goto loc_002262D2;
    result = 256;
    if ((*(uint8_t *)(v_stack_m3A8 + 0x5AE)) != 0) {
        result = 0;
    }
    local_rbx = (uint32_t)((local_rbx) | ((uint32_t)(result)));
    v_stack_m50C = (uint32_t)(local_rsi);
    if (condition_is_above_or_equal) goto loc_00226322;
    if (v_stack_m430 == 0) goto loc_00226322;
    v_stack_m50C = (uint32_t)(local_rsi);
    local_r13 = (uint32_t)((uint32_t)(local_rsi));
    if (v_stack_m430 != (*(uint64_t *)(v_rip + 0xDA07A4))) {
        local_r13 = *(uint16_t *)(v_stack_m430 + 0x1190);
        local_r13 = (uint32_t)((local_r13) + (15));
        local_r13 = (uint32_t)((local_r13) & (0xFFFFFFF8ULL));
        local_r13 = (uint32_t)((local_r13) + ((uint32_t)(local_rsi)));
        v_stack_m50C = (uint32_t)(local_r13);
    }
    if ((((uint8_t)(local_r15 + 1)) & ((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m4B8 + 0x8))))) == 0) goto loc_002263F8;
    if (condition_is_above_or_equal) goto loc_002263F8;
    if (v_stack_m4A0 != 0) goto loc_002263EA;
    result = ExpInterlockedPopEntrySList(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x880), v_stack_m430, (uint32_t)(Arg10), v_stack_m478);
    v_stack_m4A0 = result;
    if (result != 0) goto loc_002263BB;
    result = ExpInterlockedPopEntrySList(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x888), v_stack_m430, (uint32_t)(Arg10), v_stack_m478);
    v_stack_m4A0 = result;
    if (result == 0) {
        Arg2 = *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x888) + 0x2C);
        result = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x888) + 0x30);
        Arg3 = *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x888) + 0x28);
        Arg1 = *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x888) + 0x24);
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, v_stack_m478);
        Arg1 = result;
        v_stack_m4A0 = result;
    }
    if (Arg1 != 0) {
        result = *(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x24);
        *(uint32_t *)(Arg1) = (uint32_t)(result);
    }
    v_stack_m410 = Arg1;
    if (Arg1 != 0) {
        result = EtwpGetSidExtendedHeaderItem(Arg1, Arg2, Arg3, v_stack_m478);
        Arg1 = v_stack_m4A0;
    }
    if (Arg1 != 0) {
        local_rbx = (uint32_t)((local_rbx) | (2));
        result = *(uint16_t *)(Arg1);
        local_r13 = (uint32_t)((local_r13) + ((uint32_t)(result)));
        v_stack_m50C = (uint32_t)(local_r13);
    }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m4B8 + 0x8)))) & (2)) != 0) {
        local_rbx = (uint32_t)((local_rbx) | ((uint32_t)(local_r15 + 1)));
        local_r13 = (uint32_t)((local_r13) + (16));
        v_stack_m50C = (uint32_t)(local_r13);
    }
    if (!sign_flag) goto loc_00226445;
    result = KeGetEffectiveIrql(Arg1, Arg2, Arg3, v_stack_m478);
    if (((uint8_t)(result)) < 2) goto loc_00226432;
    result = (uint8_t)(local_r15 + 1);
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x20)) == 0) {
        result = 0;
    }
    if ((uint8_t)(result) == 0) {
        local_rbx = (uint32_t)((local_rbx) | (64));
        local_r13 = (uint32_t)((local_r13) + (16));
        v_stack_m50C = (uint32_t)(local_r13);
    }
    if (!(condition_is_above_or_equal)) {
        local_r13 = (uint32_t)((local_r13) + (16));
        v_stack_m50C = (uint32_t)(local_r13);
    }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m4B8 + 0x8)))) & (4)) == 0) goto loc_0022669F;
    if ((*(uint8_t *)(v_rip + 0xCD8E1B)) != 0) goto loc_0022669F;
    if (*(uint64_t *)(v_stack_m4A8 + 0x280) == 0) goto loc_002264C1;
    Arg1 = (Arg1) * ((uint32_t)(v_stack_m4F0));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + *(uint64_t *)(v_stack_m4A8 + 0x280) * 1))))) & (0x80001000ULL));
    if (((uint32_t)(result)) == 0x80001000ULL) goto loc_002264BC;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + *(uint64_t *)(v_stack_m4A8 + 0x280) * 1))))) & (0x80002000ULL));
    if (((uint32_t)(result)) == 0x80002000ULL) goto loc_002264BC;
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg1 + *(uint64_t *)(v_stack_m4A8 + 0x280) * 1))) & (0x80004000ULL));
    if (Arg2 != 0x80004000ULL) goto loc_002264C1;
loc_002264BC:
    goto loc_002264C4;
loc_002264C1:
loc_002264C4:
    if (0 == 0) goto loc_0022657E;
    result = (v_stack_m50F < 2) ? 1 : 0;
    v_stack_m558 = (uint8_t)(result);
    result = EtwpApplyLevelKwFilter(v_stack_m4A8, (uint32_t)((uint32_t)((uint32_t)(v_stack_m4F0))), *(uint8_t *)(v_stack_m4C8 + 0x4), *(uint64_t *)(v_stack_m4C8 + 0x8));
    if ((uint8_t)(result) == 0) goto loc_0022669F;
    Arg4 = (v_stack_m50F < 2) ? 1 : 0;
    result = EtwpApplyStackWalkIdFilter(*(uint16_t *)(v_stack_m4C8), v_stack_m4A8, (uint32_t)((uint32_t)((uint32_t)(v_stack_m4F0))), Arg4);
    if ((uint8_t)(result) == 0) goto loc_0022669F;
    v_stack_m538 = (uint8_t)(local_r15 + 1);
    v_stack_m540 = *(uint64_t *)(v_stack_m4C8 + 0x8);
    v_stack_m548 = (uint8_t)(*(uint8_t *)(v_stack_m4C8 + 0x4));
    v_stack_m550 = (uint8_t)(v_stack_m517);
    v_stack_m558 = 0;
    result = EtwpApplyEventNameFilter(v_stack_m4A8, (uint32_t)((uint32_t)((uint32_t)(v_stack_m4F0))), (uint32_t)(Arg10), v_stack_m478);
    if ((uint8_t)(result) == 0) goto loc_0022669F;
loc_0022657E:
    if ((((uint8_t)(local_r15 + 1)) & ((uint8_t)(local_rdi))) != 0) goto loc_00226654;
    result = EtwpGetStackLookasideListEntry(v_stack_m4A8, (uint32_t)((uint32_t)((uint32_t)(v_stack_m4F0))), (uint32_t)(Arg10), v_stack_m478);
    v_stack_m3B0 = result;
    if (result == 0) goto loc_0022664C;
    v_stack_m428 = result + 32;
    local_rdi = (uint8_t)((local_rdi) | (2));
    Arg1 = (uint8_t)(local_r15 + 1);
    if (((*(uint32_t *)(v_stack_m4D0 + 0x330)) & (0x40000000ULL)) != 0) { Arg1 = 0; }
    if ((*(uint64_t *)(v_stack_m470 + 0x28)) != (*(uint64_t *)(v_rip - 0x213591))) goto loc_0022660E;
    if ((*(uint64_t *)(v_stack_m470 + 0x30)) != (*(uint64_t *)(v_rip - 0x213596))) goto loc_0022660E;
    if ((*(uint16_t *)(v_stack_m4C8)) == 18) {
        local_rbx = (uint32_t)((local_rbx) | (32));
        Arg2 = v_stack_m470 + 80;
        Arg1 = 0;
    }
    v_stack_m550 = Arg2;
    v_stack_m558 = (uint8_t)(Arg1);
    result = EtwpGetStackExtendedHeaderItem(v_stack_m4D0, v_stack_m450, (uint32_t)(v_stack_m4EC), result);
    if ((uint8_t)(result) == 0) {
        Arg1 = v_stack_m3B0;
        result = EtwpReleaseStackLookasideListEntry(Arg1, v_stack_m450, (uint32_t)(v_stack_m4EC), result);
        local_rdi = (uint8_t)((local_rdi) & (253));
        v_stack_m428 = 0;
    }
    local_rdi = (uint8_t)((local_rdi) | ((uint8_t)(local_r15 + 1)));
    v_stack_m518 = (uint8_t)(local_rdi);
loc_00226654:
    if (v_stack_m428 == 0) goto loc_0022669F;
    if ((((uint8_t)(local_r15 + 1)) & ((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m4D0 + 0x334))))) == 0) goto loc_00226691;
    result = EtwpGetCrimsonStackKey(v_stack_m4D0, v_stack_m428, v_stack_m418, result);
    if ((uint8_t)(result) == 0) goto loc_00226691;
    local_rbx = (uint32_t)((local_rbx) | (8));
    local_r13 = (uint32_t)((local_r13) + (24));
    goto loc_0022669A;
loc_00226691:
    local_rbx = (uint32_t)((local_rbx) | (4));
    local_r13 = (uint32_t)((local_r13) + ((uint32_t)(*(uint16_t *)(v_stack_m428))));
loc_0022669A:
    v_stack_m50C = (uint32_t)(local_r13);
loc_0022669F:
    result = ((uint32_t)(v_stack_m58) + (uint32_t)(v_stack_m58) * 2) << (4);
    v_stack_m440 = result;
    v_stack_m490 = 0;
    if (Arg10 <= 0) goto loc_0022676F;
    local_rsi = (v_stack_m478) + (8);
loc_002266D8:
    result = Feature_1345841464__private_IsEnabledDeviceUsageNoInline(v_stack_m4D0, v_stack_m428, v_stack_m418, result);
    if ((uint32_t)(result) == 0) goto loc_002266ED;
    if ((*(uint32_t *)(local_rsi)) > 0xFFFFULL) goto loc_002267BE;
loc_002266ED:
    result = 0;
    if (v_stack_m4B0 != 0) {
        result = *(uint8_t *)(local_rsi + 0x4);
    }
    if ((uint8_t)(result) == 0) goto loc_00226745;
    Arg1 = (uint32_t)(((uint8_t)(result)) - (1));
    if (condition_is_equal) goto loc_00226722;
    if (((uint32_t)(Arg1)) != 3) goto loc_0022674D;
    if ((*(uint32_t *)(local_rsi)) != 16) goto loc_0022674D;
    v_stack_m400 = *(uint64_t *)(local_rsi - 0x8);
    goto loc_0022674D;
loc_00226722:
    result = Feature_1345841464__private_IsEnabledDeviceUsageNoInline(Arg1, v_stack_m428, v_stack_m418, result);
    if ((uint32_t)(result) != 0) goto loc_00226734;
    goto loc_0022673E;
loc_00226734:
    result = (uint32_t)(((uint32_t)(v_stack_m500)) + (*(uint32_t *)(local_rsi)));
    v_stack_m500 = (uint32_t)(result);
loc_0022673E:
    goto loc_0022674D;
loc_00226745:
    local_r13 = (uint32_t)((local_r13) + (*(uint32_t *)(local_rsi)));
    v_stack_m50C = (uint32_t)(local_r13);
loc_0022674D:
    result = (uint32_t)(((uint32_t)(v_stack_m490)) + ((uint32_t)(local_r15 + 1)));
    v_stack_m490 = (uint32_t)(result);
    local_rsi = (local_rsi) + (16);
    if (((uint32_t)(result)) < Arg10) goto loc_002266D8;
loc_0022676F:
    if (v_stack_m4FC == 0) goto loc_00226795;
    result = Feature_1345841464__private_IsEnabledDeviceUsageNoInline(Arg1, v_stack_m428, v_stack_m418, result);
    if ((uint32_t)(result) != 0) goto loc_00226846;
    result = (uint32_t)(((uint32_t)(v_stack_m500)) + (15));
    result = (uint32_t)((result) & (0xFFFFFFF8ULL));
loc_0022678D:
    local_r13 = (uint32_t)((local_r13) + ((uint32_t)(result)));
    v_stack_m50C = (uint32_t)(local_r13);
loc_00226795:
    if ((uint16_t)(v_stack_m4E8) == 0) goto loc_00226884;
    result = Feature_1345841464__private_IsEnabledDeviceUsageNoInline(Arg1, v_stack_m428, v_stack_m418, result);
    if ((uint32_t)(result) != 0) goto loc_00226872;
    result = (uint32_t)((v_stack_m4E8 + 15) & (0xFFFFFFF8ULL));
    goto loc_0022687C;
loc_002267BE:
    local_r14 = (uint32_t)(v_stack_m508);
    if (!sign_flag) { local_r14 = (uint32_t)((uint32_t)(0x80000005ULL)); }
loc_002267D4:
    v_stack_m508 = (uint32_t)(local_r14);
loc_002267EB:
    result = Feature_1345841464__private_IsEnabledDeviceUsageNoInline(Arg1, v_stack_m428, v_stack_m418, result);
    if ((uint32_t)(result) == 0) goto loc_002276AC;
    if (v_stack_m418 != 0) {
        Arg2 = *(uint64_t *)(v_stack_m4D0 + 0x420);
        Arg1 = v_stack_m418;
        result = EtwpDereferenceStackEntry(Arg1, Arg2, v_stack_m418, result);
    }
    if (v_stack_m504 == 0) goto loc_002276B4;
    result = ExReleaseRundownProtectionCacheAwareEx(*(uint64_t *)(*(uint64_t *)(v_stack_m488 + 0x2C0) + (uint32_t)(v_stack_m4D8) * 8), (uint32_t)((uint32_t)(local_r15 + 1)), v_stack_m418, result);
    goto loc_002276B4;
loc_00226846:
    result = (uint32_t)((result) + (15));
    result = (uint32_t)((result) & (0xFFFFFFF8ULL));
    if (((uint32_t)(result)) <= 0xFFFFULL) goto loc_0022678D;
loc_00226857:
    if (!sign_flag) { local_r14 = (uint32_t)((uint32_t)(0xC0000095ULL)); }
    goto loc_002267D4;
loc_00226872:
    result = (uint32_t)(((uint32_t)(v_stack_m4F4)) & (0xFFFFFFF8ULL));
    if (((uint32_t)(result)) > 0xFFFFULL) goto loc_00226857;
loc_0022687C:
    local_r13 = (uint32_t)((v_stack_m4D0) + ((uint32_t)(result)));
    v_stack_m50C = (uint32_t)(local_r13);
loc_00226884:
    *(uint32_t *)(local_rsp + v_stack_m440 * 1 + 0x248) = (uint32_t)(local_r13);
    result = Feature_Servicing_EtwLostEventsFlags__private_IsEnabledDeviceUsageNoInline(*(uint64_t *)(*(uint64_t *)(v_stack_m488 + 0x2C0) + (uint32_t)(v_stack_m4D8) * 8), (uint32_t)((uint32_t)(local_r15 + 1)), v_stack_m418, result);
    if ((uint32_t)(result) != 0) goto loc_002268A6;
    goto loc_002268C5;
loc_002268A6:
    result = 0;
    if ((((uint8_t)((uint32_t)(v_stack_m4EC))) & (4)) != 0) { result = 512; }
    if ((((uint8_t)((uint32_t)(v_stack_m4EC))) & (8)) != 0) {
        result = (uint32_t)((result) | (0x600ULL));
    }
    v_stack_m558 = (uint32_t)(result);
    result = EtwpReserveTraceBuffer(v_stack_m4D0, (uint32_t)((uint32_t)(local_r13)), v_stack_m388, v_stack_m3C0);
    v_stack_m4B8 = result;
    local_rsi = v_stack_m418;
    if (v_stack_m418 != 0) {
        result = v_stack_m4D0;
        Arg2 = *(uint64_t *)(result + 0x420);
        Arg1 = v_stack_m418;
        result = EtwpDereferenceStackEntry(Arg1, Arg2, v_stack_m388, v_stack_m3C0);
        result = Feature_1345841464__private_IsEnabledDeviceUsageNoInline(Arg1, Arg2, v_stack_m388, v_stack_m3C0);
        local_rsi = v_stack_m418;
        if ((uint32_t)(result) != 0) { local_rsi = 0; }
        v_stack_m418 = local_rsi;
    }
    if (result != 0) goto loc_00226A57;
    result = EtwpGetReserveTraceBufferStatus(v_stack_m4D0, (uint32_t)((uint32_t)(local_r13)), v_stack_m388, v_stack_m3C0);
    local_rsi = v_stack_m368;
    if ((uint32_t)((uint32_t)(v_stack_m4FC)) == 0) { local_rsi = 0; }
    local_r14 = (uint32_t)(v_stack_m3C8);
    if ((uint32_t)((uint32_t)(v_stack_m4FC)) == 0) { local_r14 = 0; }
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0xCD8ECB), v_rip - 2177326, v_stack_m388, v_stack_m3C0);
    if ((uint8_t)(result) != 0) {
        result = (v_stack_m50F < 2) ? 1 : 0;
        Arg3 = v_stack_m4D0 + 136;
        Arg1 = v_stack_m470;
        Arg1 = (Arg1) + (40);
        v_stack_m538 = 0;
        v_stack_m540 = (uint8_t)(result);
        v_stack_m548 = local_rsi;
        v_stack_m550 = (uint32_t)(local_r14);
        v_stack_m558 = (uint32_t)((uint32_t)((uint32_t)(result)));
        Arg4 = v_stack_m4EC;
        Arg2 = v_stack_m4C8;
        result = EtwpTraceLostEvent(Arg1, Arg2, Arg3, Arg4);
    }
    local_r14 = (uint32_t)(v_stack_m508);
    if (!(sign_flag)) {
        local_r14 = (uint32_t)(v_stack_m508);
        if (((*(uint32_t *)(v_stack_m4D0 + 0xC)) & (0x8000000ULL)) == 0) { local_r14 = (uint32_t)((uint32_t)((uint32_t)(result))); }
        v_stack_m508 = (uint32_t)(local_r14);
        v_stack_m498 = (uint32_t)(local_r14);
    }
    if ((uint8_t)((uint32_t)(v_stack_m504)) != 0) {
        Arg1 = v_stack_m488;
        Arg1 = *(uint64_t *)(Arg1 + 0x2C0);
        Arg2 = (uint32_t)(local_r15 + 1);
        result = v_stack_m408;
        Arg1 = *(uint64_t *)(Arg1 + result * 8);
        result = ExReleaseRundownProtectionCacheAwareEx(Arg1, Arg2, Arg3, Arg4);
        result = Feature_1345841464__private_IsEnabledDeviceUsageNoInline(Arg1, Arg2, Arg3, Arg4);
        Arg1 = (uint8_t)((uint32_t)(v_stack_m504));
        if ((uint32_t)(result) != 0) { Arg1 = 0; }
        v_stack_m504 = (uint8_t)(Arg1);
    }
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != ((uint32_t)((uint32_t)(0xC0000095ULL)))) goto loc_00225EDD;
    v_stack_m508 = (uint32_t)((uint32_t)(0xC0000095ULL));
loc_00226A4B:
    goto loc_002267EB;
loc_00226A57:
    *(uint64_t *)(local_rsp + v_stack_m440 * 1 + 0x220) = v_stack_m4D0;
    *(uint64_t *)(local_rsp + v_stack_m440 * 1 + 0x228) = (uint32_t)((uint32_t)((uint32_t)(0xC0000095ULL)));
    *(uint64_t *)(local_rsp + v_stack_m440 * 1 + 0x230) = v_xmm0;
    *(uint64_t *)(local_rsp + v_stack_m440 * 1 + 0x240) = v_xmm0;
    result = Feature_1345841464__private_IsEnabledDeviceUsageNoInline(v_stack_m4D0, (uint32_t)(0xC0000095ULL), v_stack_m480, Arg4);
    Arg1 = v_stack_m504;
    if ((uint32_t)(result) != 0) { Arg1 = 0; }
    v_stack_m504 = (uint32_t)((uint8_t)(Arg1));
    v_stack_m510 = (uint8_t)(Arg1);
    result = (uint32_t)(((uint32_t)((uint32_t)(v_stack_m4D0))) | (0xC0130000ULL));
    *(uint32_t *)((uint32_t)((uint32_t)((uint32_t)(0xC0000095ULL)))) = (uint32_t)(result);
    v_stack_m490 = (uint32_t)((uint32_t)((uint32_t)(0xC0000095ULL))) + 4;
    *(uint16_t *)((uint32_t)((uint32_t)((uint32_t)(0xC0000095ULL))) + 0x4) = Arg6;
    *(uint16_t *)((uint32_t)((uint32_t)((uint32_t)(0xC0000095ULL))) + 0x6) = Arg7;
    *(uint64_t *)((uint32_t)((uint32_t)((uint32_t)(0xC0000095ULL))) + 0x28) = v_xmm0;
    if (v_stack_m400 != 0) goto loc_00226B1B;
    goto loc_00226B39;
loc_00226B1B:
    Arg2 = (uint16_t)((Arg6) | (128));
    *(uint16_t *)((uint32_t)((uint32_t)((uint32_t)(0xC0000095ULL))) + 0x4) = Arg2;
loc_00226B39:
    *(uint64_t *)((uint32_t)((uint32_t)((uint32_t)(0xC0000095ULL))) + 0x18) = v_xmm0;
    if (Arg8 == 0) goto loc_00226B51;
    goto loc_00226B58;
loc_00226B51:
loc_00226B58:
    *(uint64_t *)((uint32_t)((uint32_t)((uint32_t)(0xC0000095ULL))) + 0x40) = v_xmm0;
    v_stack_m408 = (uint32_t)((uint32_t)((uint32_t)(0xC0000095ULL))) + 16;
    *(uint64_t *)((uint32_t)((uint32_t)((uint32_t)(0xC0000095ULL))) + 0x10) = v_stack_m3C0;
    *(uint32_t *)((uint32_t)((uint32_t)((uint32_t)(0xC0000095ULL))) + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m450 + 0x510)));
    *(uint32_t *)((uint32_t)((uint32_t)((uint32_t)(0xC0000095ULL))) + 0xC) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m450 + 0x508)));
    *(uint32_t *)((uint32_t)((uint32_t)((uint32_t)(0xC0000095ULL))) + 0x38) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m450 + 0x28C)));
    *(uint32_t *)((uint32_t)((uint32_t)((uint32_t)(0xC0000095ULL))) + 0x3C) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m450 + 0x2DC)));
    if (((v_stack_p78) & ((uint16_t)((uint32_t)(0x400ULL)))) != 0) {
        Arg2 = (uint16_t)((Arg2) | ((uint16_t)((uint32_t)(0x400ULL))));
        *(uint16_t *)((uint32_t)((uint32_t)((uint32_t)(0xC0000095ULL))) + 0x4) = Arg2;
    }
    if ((uint32_t)((uint32_t)(v_stack_m4F4)) == 0) goto loc_00226FF6;
    if (condition_is_above_or_equal) goto loc_00226C84;
    v_stack_m4C0 = (uint32_t)((uint32_t)((uint32_t)(0xC0000095ULL))) + 80;
    local_r14 = (uint16_t)((*(uint16_t *)(v_stack_m430 + 0x1190)) + (15));
    local_r14 = (uint16_t)((local_r14) & ((uint16_t)((uint32_t)(0xFFF8ULL))));
    *(uint16_t *)((uint32_t)((uint32_t)((uint32_t)(0xC0000095ULL))) + 0x50) = (uint16_t)(local_r14);
    *(uint16_t *)((uint32_t)((uint32_t)((uint32_t)(0xC0000095ULL))) + 0x50 + 0x2) = 16;
    *(uint16_t *)((uint32_t)((uint32_t)((uint32_t)(0xC0000095ULL))) + 0x50 + 0x6) = (uint16_t)(*(uint16_t *)(v_stack_m430 + 0x1190));
    *(uint16_t *)((uint32_t)((uint32_t)((uint32_t)(0xC0000095ULL))) + 0x50 + 0x4) = 0;
    local_r14 = (uint16_t)((local_r14) - ((uint16_t)(*(uint16_t *)(v_stack_m430 + 0x1190))));
    local_r14 = (uint16_t)((local_r14) - (8));
    result = memcpy((uint32_t)((uint32_t)((uint32_t)(0xC0000095ULL))) + 80 + 8, *(uint64_t *)(v_stack_m430 + 0x1188), *(uint16_t *)(v_stack_m430 + 0x1190), Arg4);
    Arg1 = (*(uint16_t *)(v_stack_m430 + 0x1190)) + ((uint32_t)((uint32_t)((uint32_t)(0xC0000095ULL))) + 80 + 8);
    Arg2 = 0;
    result = memset(Arg1, Arg2, (uint16_t)(local_r14), Arg4);
    local_r10 = (uint32_t)((*(uint16_t *)(v_stack_m4C0)) + (80));
    v_stack_m514 = (uint32_t)(local_r10);
    v_stack_m458 = v_stack_m4C0;
    goto loc_00226C8C;
loc_00226C84:
loc_00226C8C:
    if (((16) & ((uint8_t)((uint32_t)(v_stack_m4F4)))) == 0) goto loc_00226CE9;
    Arg1 = ((uint32_t)((uint32_t)((uint32_t)(v_stack_m514)))) + (v_stack_m4B8);
    *(uint32_t *)(Arg1) = 0x10018ULL;
    *(uint32_t *)(Arg1 + 0x4) = 0x100000ULL;
    *(uint64_t *)(Arg1 + 0x8) = v_xmm0;
    local_r10 = (uint32_t)(((uint32_t)(v_stack_m514)) + ((uint32_t)(16 + 8)));
    v_stack_m514 = (uint32_t)(local_r10);
    if (0 != 0) {
    }
    v_stack_m4C0 = Arg1;
    v_stack_m458 = Arg1;
    goto loc_00226CF1;
loc_00226CE9:
loc_00226CF1:
    if ((((uint8_t)((uint32_t)(v_stack_m4F4))) & (2)) == 0) goto loc_00226D5C;
    local_r14 = ((uint32_t)((uint32_t)(local_r10))) + (v_stack_m4B8);
    result = memcpy(local_r14, v_stack_m4A0, *(uint16_t *)(v_stack_m4A0), Arg4);
    local_r10 = (uint32_t)(((uint32_t)(v_stack_m514)) + ((uint32_t)(*(uint16_t *)(v_stack_m4A0))));
    v_stack_m514 = (uint32_t)(local_r10);
    if (v_stack_m4C0 != 0) {
    }
    v_stack_m4C0 = local_r14;
    v_stack_m458 = local_r14;
loc_00226D5C:
    if ((((uint8_t)(local_r15 + 1)) & ((uint8_t)((uint32_t)(v_stack_m4F4)))) == 0) goto loc_00226DBD;
    local_rsi = ((uint32_t)((uint32_t)(local_r10))) + (v_stack_m4B8);
    *(uint32_t *)(local_rsi) = 0x30010ULL;
    *(uint32_t *)(local_rsi + 0x4) = 0x40000ULL;
    result = PsGetCurrentProcessSessionId(local_r14, v_stack_m4A0, *(uint16_t *)(v_stack_m4A0), Arg4);
    *(uint32_t *)(local_rsi + 0x8) = (uint32_t)(result);
    local_r10 = (uint32_t)(((uint32_t)(v_stack_m514)) + (16));
    v_stack_m514 = (uint32_t)(local_r10);
    if (local_r14 != 0) {
    }
    v_stack_m4C0 = local_rsi;
    v_stack_m458 = local_rsi;
loc_00226DBD:
    if ((((uint8_t)((uint32_t)(v_stack_m4F4))) & (64)) == 0) goto loc_00226E39;
    Arg2 = ((uint32_t)((uint32_t)(local_r10))) + (v_stack_m4B8);
    *(uint32_t *)(Arg2) = 0xD0010ULL;
    *(uint32_t *)(Arg2 + 0x4) = 0x80000ULL;
    result = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188))))) << (48);
    result = (result) | (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x678));
    *(uint64_t *)(Arg2 + 0x8) = result;
    local_r10 = (uint32_t)((local_r10) + (16));
    v_stack_m514 = (uint32_t)(local_r10);
    if (local_rsi != 0) {
    }
    v_stack_m4C0 = Arg2;
    v_stack_m458 = Arg2;
loc_00226E39:
    if (!sign_flag) goto loc_00226EEC;
    Arg3 = ((uint32_t)((uint32_t)(local_r10))) + (v_stack_m4B8);
    *(uint32_t *)(Arg3) = 0xA0010ULL;
    *(uint32_t *)(Arg3 + 0x4) = 0x80000ULL;
    if ((((uint8_t)(local_rdi)) & (4)) != 0) goto loc_00226EB7;
    result = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8BA8)) + (8);
    Arg2 = (local_r15 + 1) + (local_r15 + 1);
    result = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x24))) << (48);
    Arg2 = (Arg2) & (*(uint64_t *)(gs_base + (0 + 0x20)));
    result = (result) | (Arg2);
    v_stack_m3B8 = result;
    local_rdi = (uint8_t)((local_rdi) | (4));
    v_stack_m518 = (uint8_t)(local_rdi);
    if (v_stack_m420 != 0) {
        *(uint64_t *)(v_stack_m420) = result;
    }
    *(uint64_t *)(Arg3 + 0x8) = v_stack_m3B8;
    local_r10 = (uint32_t)((local_r10) + (16));
    v_stack_m514 = (uint32_t)(local_r10);
    if (Arg2 != 0) {
    }
    v_stack_m4C0 = Arg3;
    v_stack_m458 = Arg3;
loc_00226EEC:
    if ((((uint8_t)((uint32_t)(v_stack_m4F4))) & (4)) == 0) goto loc_00226F8A;
    local_r14 = ((uint32_t)((uint32_t)(local_r10))) + (v_stack_m4B8);
    result = memcpy(local_r14, v_stack_m428, *(uint16_t *)(v_stack_m428), v_stack_m4B8);
    if ((*(uint64_t *)(local_r14 + 0x8)) == 0) goto loc_00226F49;
    if ((((uint8_t)((uint32_t)(v_stack_m4F4))) & (32)) != 0) goto loc_00226F49;
    v_stack_m558 = local_r14 + 8;
    result = EtwpQueueStackWalkApc(v_stack_m450, v_stack_m517, v_stack_m4D0, (uint8_t)(local_r15 + 1));
    if ((uint8_t)(result) == 0) {
        *(uint64_t *)(local_r14 + 0x8) = 0;
    }
    local_r10 = (uint32_t)(((uint32_t)(v_stack_m514)) + ((uint32_t)(*(uint16_t *)(v_stack_m428))));
    v_stack_m514 = (uint32_t)(local_r10);
    if (v_stack_m4C0 != 0) {
    }
    v_stack_m4C0 = local_r14;
    v_stack_m458 = local_r14;
    goto loc_00226F92;
loc_00226F8A:
loc_00226F92:
    if (((8) & ((uint8_t)((uint32_t)(v_stack_m4F4)))) == 0) goto loc_00227003;
    Arg1 = ((uint32_t)((uint32_t)(local_r10))) + (v_stack_m4B8);
    *(uint32_t *)(Arg1) = 0x120018ULL;
    *(uint32_t *)(Arg1 + 0x4) = 0x100000ULL;
    *(uint64_t *)(Arg1 + 0x10) = v_stack_m418;
    *(uint64_t *)(Arg1 + 0x8) = *(uint64_t *)(v_stack_m428 + 0x8);
    local_r10 = (uint32_t)((local_r10) + ((uint32_t)(8 + 16)));
    v_stack_m514 = (uint32_t)(local_r10);
    if (local_r14 != 0) {
    }
    v_stack_m4C0 = Arg1;
    v_stack_m458 = Arg1;
    goto loc_00226FFE;
loc_00226FF6:
loc_00226FFE:
loc_00227003:
    if ((uint16_t)(v_stack_m4E8) == 0) goto loc_002271A8;
    local_r14 = ((uint32_t)((uint32_t)((uint32_t)(v_stack_m514)))) + (local_r14);
    v_stack_m440 = local_r14;
    local_rsi = (uint32_t)((15) + ((uint32_t)(v_stack_m4E8)));
    local_rsi = (uint16_t)((local_rsi) & ((uint16_t)((uint32_t)(0xFFF8ULL))));
    *(uint16_t *)(local_r14) = (uint16_t)(local_rsi);
    *(uint32_t *)(local_r14 + 0x2) = 12;
    *(uint16_t *)(local_r14 + 0x6) = (uint16_t)(v_stack_m4E8);
    local_rsi = (uint16_t)((local_rsi) - ((uint16_t)(v_stack_m4E8)));
    local_rsi = (uint16_t)((local_rsi) - (8));
    v_stack_m4F0 = (uint16_t)(local_rsi);
    result = memcpy(local_r14 + 8, v_stack_m398, (uint32_t)((uint32_t)(v_stack_m4E8)), 8 + 16);
    Arg1 = ((uint32_t)((uint32_t)(v_stack_m4E8)) + 8) + (local_r14);
    Arg2 = 0;
    result = memset(Arg1, Arg2, (uint16_t)(local_rsi), 8 + 16);
    goto loc_0022717E;
loc_0022717E:
    local_r10 = (uint32_t)(((uint32_t)(v_stack_m514)) + ((uint32_t)(*(uint16_t *)(local_r14))));
    v_stack_m514 = (uint32_t)(local_r10);
    if (v_stack_m4C0 != 0) {
    }
    v_stack_m4C0 = local_r14;
loc_002271A8:
    if ((uint32_t)((uint32_t)(v_stack_m4FC)) == 0) goto loc_00227235;
    local_rbx = ((uint32_t)((uint32_t)(local_r10))) + (v_stack_m4B8);
    Arg2 = (uint32_t)((15) + ((uint32_t)((uint32_t)(v_stack_m500))));
    Arg2 = (uint16_t)((Arg2) & ((uint16_t)((uint32_t)(0xFFF8ULL))));
    *(uint16_t *)(local_rbx) = Arg2;
    *(uint32_t *)(local_rbx + 0x2) = 11;
    *(uint16_t *)(local_rbx + 0x6) = (uint16_t)((uint32_t)(v_stack_m500));
    Arg2 = (uint16_t)((Arg2) - ((uint16_t)((uint32_t)(v_stack_m500))));
    Arg2 = (uint16_t)((Arg2) - (8));
    v_stack_m3F8 = local_rbx + 8;
    Arg1 = (local_rbx + 8) + ((uint32_t)(v_stack_m500));
    v_stack_m390 = Arg1;
    Arg2 = 0;
    result = memset(Arg1, Arg2, Arg2, 8 + 16);
    local_r10 = (uint32_t)(((uint32_t)(v_stack_m514)) + ((uint32_t)(*(uint16_t *)(local_rbx))));
    v_stack_m514 = (uint32_t)(local_r10);
    if (v_stack_m4C0 != 0) {
    }
loc_00227238:
    v_stack_m500 = 0;
    if (0 >= Arg10) goto loc_00227600;
    result = (0) + (0);
    v_stack_m490 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m478 + result * 8 + 0x8)));
    if (v_stack_m4B0 != 0) goto loc_00227276;
    goto loc_0022727B;
loc_00227276:
loc_0022727B:
    if ((uint8_t)(*(uint8_t *)(v_stack_m478 + 0x0 * 8 + 0xC)) == 0) goto loc_002274D3;
    Arg1 = (uint32_t)(((uint8_t)(*(uint8_t *)(v_stack_m478 + 0x0 * 8 + 0xC))) - (1));
    if (condition_is_equal) goto loc_00227386;
    if (((uint32_t)(Arg1)) != 2) goto loc_002275F0;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m478 + result * 8 + 0x8)))) != 8) goto loc_002275F0;
    *(uint64_t *)(v_stack_m408) = *(uint64_t *)(*(uint64_t *)(v_stack_m478 + result * 8));
    goto loc_002275F0;
loc_00227386:
    if (v_stack_m3F8 == 0) goto loc_00227826;
    v_stack_m440 = (uint32_t)(*(uint32_t *)(v_stack_m478 + result * 8 + 0x8)) + v_stack_m3F8 * 1;
    if (((uint32_t)(*(uint32_t *)(v_stack_m478 + result * 8 + 0x8)) + v_stack_m3F8 * 1) > v_stack_m390) goto loc_00227826;
    if ((uint32_t)((uint32_t)(v_stack_m4FC)) == 0) goto loc_00227826;
    result = memcpy(v_stack_m3F8, *(uint64_t *)(v_stack_m478 + result * 8), (uint32_t)(*(uint32_t *)(v_stack_m478 + result * 8 + 0x8)), *(uint64_t *)(v_stack_m478 + result * 8));
    goto loc_002274B9;
loc_002274B9:
    v_stack_m3F8 = (uint32_t)(*(uint32_t *)(v_stack_m478 + result * 8 + 0x8)) + v_stack_m3F8 * 1;
    local_r11 = (uint32_t)(((uint32_t)(v_stack_m4FC)) - 1);
    v_stack_m4FC = (uint32_t)(local_r11);
    goto loc_002275F0;
loc_002274D3:
    Arg1 = ((uint32_t)((uint32_t)((uint32_t)(v_stack_m514)))) + (v_stack_m4B8);
    v_stack_m440 = Arg1;
    local_r10 = (uint32_t)(((uint32_t)(v_stack_m514)) + ((uint32_t)(*(uint64_t *)(v_stack_m478 + result * 8))));
    v_stack_m514 = (uint32_t)(local_r10);
    if (((uint32_t)(local_r10)) > ((uint32_t)(v_stack_m4D0))) goto loc_00227841;
    result = memcpy(Arg1, *(uint64_t *)(v_stack_m478 + result * 8), *(uint64_t *)(v_stack_m478 + result * 8), *(uint64_t *)(v_stack_m478 + result * 8));
    goto loc_002275F0;
loc_002275F0:
    local_rsi = (uint32_t)((0) + ((uint32_t)(local_r15 + 1)));
    goto loc_00227238;
loc_00227600:
    if (((*(uint32_t *)(v_stack_m4D0 + 0xC)) & (0x80000ULL)) == 0) goto loc_0022763D;
    if ((*(uint8_t *)(v_rip + 0xD1FFC3)) != 0) goto loc_00227624;
    if ((*(uint8_t *)(v_rip + 0xBE33FA)) == 0) goto loc_0022762D;
loc_00227624:
    if ((*(uint8_t *)(v_rip + 0xD2E688)) != 0) {
        Arg2 = v_stack_m388;
        Arg1 = v_stack_m4D0;
        result = EtwpSendTraceEvent(Arg1, Arg2, *(uint64_t *)(v_stack_m478 + result * 8), *(uint64_t *)(v_stack_m478 + result * 8));
    }
    if ((*(uint64_t *)(v_stack_m4D0 + 0x620)) != 0) {
        Arg3 = v_stack_m470;
        Arg3 = (Arg3) + (40);
        Arg4 = 0;
        Arg2 = v_stack_m388;
        Arg1 = v_stack_m4D0;
        result = EtwpInvokeEventCallback(Arg1, Arg2, Arg3, Arg4);
    }
    if (v_stack_m480 == 0) goto loc_00225EE5;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m4D8)))) >> (5));
    Arg1 = (uint32_t)(((uint32_t)(v_stack_m4D8)) & (31));
    *(uint32_t *)(v_stack_m480 + (uint32_t)((uint32_t)(result)) * 4) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m480 + result * 4)));
    goto loc_00225EE5;
loc_002276AC:
loc_002276B4:
    result = (uint32_t)(*(uint32_t *)(v_stack_m480 + result * 4));
    if ((((uint8_t)(local_rdi)) & (2)) != 0) {
        Arg1 = v_stack_m3B0;
        result = EtwpReleaseStackLookasideListEntry(Arg1, (uint32_t)((uint32_t)(result)), v_stack_m480, Arg4);
    }
    if (sign_flag) goto loc_00227725;
    if (v_stack_m58 <= 0) goto loc_0022778C;
loc_002276EE:
    result = EtwpReleaseTraceBuffer(v_stack_m358 + 16, (uint32_t)((uint32_t)(result)), v_stack_m480, Arg4);
    if (((uint8_t)(v_stack_m517)) < 2) {
        result = *(uint64_t *)(v_stack_m358);
        result = *(uint32_t *)(result);
        Arg1 = *(uint64_t *)(v_stack_m488 + 0x2C0);
        Arg2 = (uint32_t)(local_r15 + 1);
        Arg1 = *(uint64_t *)(Arg1 + result * 8);
        result = ExReleaseRundownProtectionCacheAwareEx(Arg1, Arg2, v_stack_m480, Arg4);
    }
    local_rbx = (v_stack_m358) + (48);
    local_rdi = ((uint32_t)(v_stack_m58)) - (local_r15 + 1);
    if (condition_is_not_equal) goto loc_002276EE;
    goto loc_0022778C;
loc_00227725:
    result = (v_stack_m50F < 2) ? 1 : 0;
    v_stack_m520 = 0;
    v_stack_m528 = v_stack_m478;
    v_stack_m530 = (uint32_t)((uint32_t)(Arg10));
    v_stack_m538 = (uint8_t)(result);
    v_stack_m540 = v_stack_m4C8;
    v_stack_m548 = (uint32_t)((uint32_t)(v_stack_m508));
    v_stack_m550 = (uint32_t)((uint32_t)(v_stack_m4EC));
    v_stack_m558 = (uint16_t)(local_rbx);
    result = EtwpFailLogging(*(uint8_t *)(v_stack_m4C8 + 0x4), *(uint64_t *)(v_stack_m4C8 + 0x8), v_stack_m470, v_stack_m358);
loc_0022778C:
    if (v_stack_m4F8 != 0) {
        Arg1 = v_stack_m3A8;
        result = KiLeaveCriticalRegionUnsafe(Arg1, *(uint64_t *)(v_stack_m4C8 + 0x8), v_stack_m470, v_stack_m358);
    }
    if (v_stack_m4A0 == 0) goto loc_002277FF;
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x880))) < ((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x880) + 0x10)))) goto loc_002277F7;
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x888))) < ((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x888) + 0x10)))) goto loc_002277F7;
    result = guard_dispatch_icall(v_stack_m4A0, *(uint64_t *)(gs_base + (0 + 0x20)), v_stack_m4A0, v_stack_m358);
    goto loc_002277FF;
loc_002277F7:
    result = ExpInterlockedPushEntrySList(v_stack_m4A0, v_stack_m4A0, v_stack_m4A0, v_stack_m358);
loc_002277FF:
loc_00227802:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_stack_m4A0, v_stack_m4A0, v_stack_m358);
    local_rsp = (local_rsp) + (0x540ULL);
    return result;
loc_00227826:
    v_stack_p20 = 0;
    result = KeBugCheckEx(285, 5, (uint32_t)((uint32_t)(v_stack_m4C8)), (uint32_t)((uint32_t)(v_stack_m4D0)));
loc_00227841:
    v_stack_p20 = 0;
    result = KeBugCheckEx(285, 5, (uint32_t)((uint32_t)(v_stack_m4C8)), (uint32_t)((uint32_t)(v_stack_m4D0)));
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg9` | `+ 0x0` | `128` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00225C10&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
