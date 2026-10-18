# PopInvokeSystemStateHandler

- RVA: `0x00B76A6C`–`0x00B7726A` (길이 `2,046` bytes)
- VA: `0x0000000140B76A6C`
- 실행 섹션: `PAGELK`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A1130`
- 디코드: `472`개 명령, `2,046/2,046` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **57**; 고유 호출 대상: **25**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **51**

### Outgoing calls
- `0x00B76ADA` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00B76BA2` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00B76BE6` → [KeSetSystemGroupAffinityThread](../../text/39/KeSetSystemGroupAffinityThread_function_00399140.md) (function, `0x00399140`)
- `0x00B76C02` → [KiRaiseIrqlProcessIrqlFlags](../../text/4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x00B76C17` → [KeInitializeDpc](../../text/45/KeInitializeDpc_function_0045BBD0.md) (function, `0x0045BBD0`)
- `0x00B76C5D` → [KeInsertQueueDpc](../../text/20/KeInsertQueueDpc_function_00207C50.md) (function, `0x00207C50`)
- `0x00B76CFD` → [ExpInterlockedPushEntrySList](../../text/6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (function, `0x006BA5B0`)
- `0x00B76D0C` → [PopIssueNextState](PopIssueNextState_function_00B772EC.md) (function, `0x00B772EC`)
- `0x00B76D1E` → [PopIssueNextState](PopIssueNextState_function_00B772EC.md) (function, `0x00B772EC`)
- `0x00B76D4C` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x00B76D98` → [EtwTraceKernelEvent](../../text/23/EtwTraceKernelEvent_function_00235350.md) (function, `0x00235350`)
- `0x00B76DAA` → [PopIssueNextState](PopIssueNextState_function_00B772EC.md) (function, `0x00B772EC`)
- `0x00B76DBB` → [VfIsVerifierEnabled](../../text/4C/VfIsVerifierEnabled_function_004C72F0.md) (function, `0x004C72F0`)
- `0x00B76DC6` → [VfNotifyOfHibernate](../../pagevrfy/B9/VfNotifyOfHibernate_function_00B97618.md) (function, `0x00B97618`)
- `0x00B76DD7` → [PopCheckpointSystemSleep](PopCheckpointSystemSleep_function_00B77C90.md) (function, `0x00B77C90`)
- `0x00B76DFA` → [PopIssueNextState](PopIssueNextState_function_00B772EC.md) (function, `0x00B772EC`)
- `0x00B76E12` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00B76E2A` → [PopIssueNextState](PopIssueNextState_function_00B772EC.md) (function, `0x00B772EC`)
- `0x00B76E2F` → [KeSuspendDynamicTracing](../../text/4D/KeSuspendDynamicTracing_function_004D7B70.md) (function, `0x004D7B70`)
- `0x00B76E3E` → [MiUpdateUserMappings](MiUpdateUserMappings_function_00B7966C.md) (function, `0x00B7966C`)
- `0x00B76E57` → [PopIssueNextState](PopIssueNextState_function_00B772EC.md) (function, `0x00B772EC`)
- `0x00B76E61` → [PopCheckpointSystemSleep](PopCheckpointSystemSleep_function_00B77C90.md) (function, `0x00B77C90`)
- `0x00B76E73` → [PopIssueNextState](PopIssueNextState_function_00B772EC.md) (function, `0x00B772EC`)
- `0x00B76E7D` → [PopCheckpointSystemSleep](PopCheckpointSystemSleep_function_00B77C90.md) (function, `0x00B77C90`)
- `0x00B76E89` → [KeRebaselineInterruptTime](../../text/4E/KeRebaselineInterruptTime_function_004E34CC.md) (function, `0x004E34CC`)
- `0x00B76E95` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00B76EB5` → [PopIssueNextState](PopIssueNextState_function_00B772EC.md) (function, `0x00B772EC`)
- `0x00B76EC7` → [PopIssueNextState](PopIssueNextState_function_00B772EC.md) (function, `0x00B772EC`)
- `0x00B76EE3` → [PopCheckpointSystemSleep](PopCheckpointSystemSleep_function_00B77C90.md) (function, `0x00B77C90`)
- `0x00B76EF5` → [PopIssueNextState](PopIssueNextState_function_00B772EC.md) (function, `0x00B772EC`)
- `0x00B76EFF` → [PopCheckpointSystemSleep](PopCheckpointSystemSleep_function_00B77C90.md) (function, `0x00B77C90`)
- `0x00B76F10` → [MmInvalidateDumpAddresses](MmInvalidateDumpAddresses_function_00B74970.md) (function, `0x00B74970`)
- `0x00B76F2B` → [MmInvalidateDumpAddresses](MmInvalidateDumpAddresses_function_00B74970.md) (function, `0x00B74970`)
- `0x00B76F3D` → [PopIssueNextState](PopIssueNextState_function_00B772EC.md) (function, `0x00B772EC`)
- `0x00B76F53` → [MiUpdateUserMappings](MiUpdateUserMappings_function_00B7966C.md) (function, `0x00B7966C`)
- `0x00B76F5A` → [MiConvertHiberPhasePages](MiConvertHiberPhasePages_function_00B73E24.md) (function, `0x00B73E24`)
- `0x00B76F63` → [KeResumeDynamicTracing](../../text/5C/KeResumeDynamicTracing_function_005CAB08.md) (function, `0x005CAB08`)
- `0x00B76F75` → [PopIssueNextState](PopIssueNextState_function_00B772EC.md) (function, `0x00B772EC`)
- `0x00B76F91` → [DbgBreakPointWithStatus](../../text/4F/DbgBreakPointWithStatus_function_004FE4E0.md) (function, `0x004FE4E0`)
- `0x00B76FAF` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00B77010` → [PopIssueNextState](PopIssueNextState_function_00B772EC.md) (function, `0x00B772EC`)
- `0x00B77038` → [VfIsVerifierEnabled](../../text/4C/VfIsVerifierEnabled_function_004C72F0.md) (function, `0x004C72F0`)
- `0x00B77043` → [VfNotifyOfHibernate](../../pagevrfy/B9/VfNotifyOfHibernate_function_00B97618.md) (function, `0x00B97618`)
- `0x00B7706A` → [KeRebaselineInterruptTime](../../text/4E/KeRebaselineInterruptTime_function_004E34CC.md) (function, `0x004E34CC`)
- `0x00B7706F` → [KeRebaselineSystemTime](../../text/4E/KeRebaselineSystemTime_function_004E3554.md) (function, `0x004E3554`)
- `0x00B77079` → [PopCheckpointSystemSleep](PopCheckpointSystemSleep_function_00B77C90.md) (function, `0x00B77C90`)
- `0x00B77092` → [PopIssueNextState](PopIssueNextState_function_00B772EC.md) (function, `0x00B772EC`)
- `0x00B770C2` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00B770D7` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x00B770E3` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x00B7713A` → [EtwTraceKernelEvent](../../text/23/EtwTraceKernelEvent_function_00235350.md) (function, `0x00235350`)
- `0x00B771A4` → [PopIssueNextState](PopIssueNextState_function_00B772EC.md) (function, `0x00B772EC`)
- `0x00B771B6` → [PopIssueNextState](PopIssueNextState_function_00B772EC.md) (function, `0x00B772EC`)
- `0x00B771C8` → [PopIssueNextState](PopIssueNextState_function_00B772EC.md) (function, `0x00B772EC`)
- `0x00B77215` → [BgLibraryInitialize](../../pagebgfx/BC/BgLibraryInitialize_function_00BC0760.md) (function, `0x00BC0760`)
- `0x00B7722C` → [KiLowerIrqlProcessIrqlFlags](../../text/4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x00B77249` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PopShutdownSystem](PopShutdownSystem_function_00B71784.md) at `0x00B717EB`
- [PopShutdownSystem](PopShutdownSystem_function_00B71784.md) at `0x00B7180B`
- [PopEndMirroring](PopEndMirroring_function_00B75E50.md) at `0x00B75F59`
- [PopTransitionToSleep](PopTransitionToSleep_function_00B76970.md) at `0x00B769E8`

### Static image references
- `0x00B76A8B` → RVA `0x00E0A740` (`.data`; read)
- `0x00B76AF7` → RVA `0x00F0C700` (`.data`; read)
- `0x00B76B16` → RVA `0x00F0CC40` (`.data`; read)
- `0x00B76B37` → RVA `0x00FC6A80` (`ALMOSTRO`; read)
- `0x00B76B59` → RVA `0x00F0C9D4` (`.data`; read)
- `0x00B76B83` → RVA `0x006BA360` (`PopSaveHiberContextWrapper`; read)
- `0x00B76BB5` → RVA `0x00F231B0` (`.data`; read)
- `0x00B76BF3` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x00B76C0B` → RVA `0x00B77270` (`PopInvokeStateHandlerTargetProcessor`; read)
- `0x00B76C8F` → RVA `0x00E276C0` (`.data`; write)
- `0x00B76C96` → RVA `0x00E27700` (`.data`; read)
- `0x00B76CA1` → RVA `0x00E276C0` (`.data`; read)
- `0x00B76CA8` → RVA `0x00E276C8` (`.data`; write)
- `0x00B76CB3` → RVA `0x00E276D0` (`.data`; write)
- `0x00B76CBE` → RVA `0x00E276D8` (`.data`; write)
- `0x00B76CC9` → RVA `0x00E276E0` (`.data`; write)
- `0x00B76CD3` → RVA `0x00E276E8` (`.data`; write)
- `0x00B76CDC` → RVA `0x00E276EC` (`.data`; write)
- `0x00B76CE5` → RVA `0x00E276F0` (`.data`; write)
- `0x00B76CEE` → RVA `0x00E276FC` (`.data`; write)
- `0x00B76CF7` → RVA `0x00E276F8` (`.data`; write)
- `0x00B76D23` → RVA `0x00F0BD6C` (`.data`; read)
- `0x00B76D43` → RVA `0x00FC6BE0` (`ALMOSTRO`; read)
- `0x00B76D54` → RVA `0x00FC6B10` (`ALMOSTRO`; read)
- `0x00B76DB4` → RVA `0x00E67B4C` (`.data`; write)
- `0x00B76DD0` → RVA `0x00F0BD23` (`.data`; write)
- `0x00B76E0B` → RVA `0x00E00B28` (`.data`; read)
- `0x00B76E34` → RVA `0x00F0C2E0` (`.data`; read)
- `0x00B76E43` → RVA `0x00E30143` (`.data`; write)
- `0x00B76E8E` → RVA `0x00E00B18` (`.data`; read)
- `0x00B76F04` → RVA `0x00F0BF48` (`.data`; read)
- `0x00B76F7A` → RVA `0x00E67880` (`.data`; read)
- `0x00B76F85` → RVA `0x00F475F8` (`.data`; read)
- `0x00B76FB5` → RVA `0x00F0C6F4` (`.data`; write)
- `0x00B76FC1` → RVA `0x00F0CFC0` (`.data`; read/write)
- `0x00B76FC7` → RVA `0x00F0C680` (`.data`; read)
- `0x00B76FCE` → RVA `0x00F0CCE8` (`.data`; write)
- `0x00B76FD5` → RVA `0x00F0C684` (`.data`; write)
- `0x00B76FDC` → RVA `0x00F0C688` (`.data`; write)
- `0x00B76FE3` → RVA `0x00F0BC68` (`.data`; write)
- `0x00B76FEF` → RVA `0x00F0C684` (`.data`; read/write)
- `0x00B76FF7` → RVA `0x00F0C688` (`.data`; read/write)
- `0x00B7702A` → RVA `0x00F0DE58` (`.data`; write)
- `0x00B77048` → RVA `0x00E08810` (`.data`; read)
- `0x00B770B2` → RVA `0x00E00900` (`.data`; read)
- `0x00B770E8` → RVA `0x00F07770` (`.data`; read)
- `0x00B770EF` → RVA `0x00F0C488` (`.data`; write)
- `0x00B77190` → RVA `0x00F0C348` (`.data`; write)
- `0x00B771FA` → RVA `0x00F0BF61` (`.data`; read)
- `0x00B77203` → RVA `0x00E65EB9` (`.data`; read)
- `0x00B7720C` → RVA `0x00E65E90` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **29**
  - `0x00B76ADA` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGELK` → `.text`)
  - `0x00B76BA2` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGELK` → `.text`)
  - `0x00B76BE6` → [KeSetSystemGroupAffinityThread](../../text/39/KeSetSystemGroupAffinityThread_function_00399140.md) (`PAGELK` → `.text`)
  - `0x00B76C02` → [KiRaiseIrqlProcessIrqlFlags](../../text/4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (`PAGELK` → `.text`)
  - `0x00B76C17` → [KeInitializeDpc](../../text/45/KeInitializeDpc_function_0045BBD0.md) (`PAGELK` → `.text`)
  - `0x00B76C5D` → [KeInsertQueueDpc](../../text/20/KeInsertQueueDpc_function_00207C50.md) (`PAGELK` → `.text`)
  - `0x00B76CFD` → [ExpInterlockedPushEntrySList](../../text/6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (`PAGELK` → `.text`)
  - `0x00B76D4C` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (`PAGELK` → `.text`)
  - `0x00B76D98` → [EtwTraceKernelEvent](../../text/23/EtwTraceKernelEvent_function_00235350.md) (`PAGELK` → `.text`)
  - `0x00B76DBB` → [VfIsVerifierEnabled](../../text/4C/VfIsVerifierEnabled_function_004C72F0.md) (`PAGELK` → `.text`)
  - `0x00B76DC6` → [VfNotifyOfHibernate](../../pagevrfy/B9/VfNotifyOfHibernate_function_00B97618.md) (`PAGELK` → `PAGEVRFY`)
  - `0x00B76E12` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGELK` → `.text`)
  - `0x00B76E2F` → [KeSuspendDynamicTracing](../../text/4D/KeSuspendDynamicTracing_function_004D7B70.md) (`PAGELK` → `.text`)
  - `0x00B76E89` → [KeRebaselineInterruptTime](../../text/4E/KeRebaselineInterruptTime_function_004E34CC.md) (`PAGELK` → `.text`)
  - `0x00B76E95` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGELK` → `.text`)
  - `0x00B76F63` → [KeResumeDynamicTracing](../../text/5C/KeResumeDynamicTracing_function_005CAB08.md) (`PAGELK` → `.text`)
  - `0x00B76F91` → [DbgBreakPointWithStatus](../../text/4F/DbgBreakPointWithStatus_function_004FE4E0.md) (`PAGELK` → `.text`)
  - `0x00B76FAF` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGELK` → `.text`)
  - `0x00B77038` → [VfIsVerifierEnabled](../../text/4C/VfIsVerifierEnabled_function_004C72F0.md) (`PAGELK` → `.text`)
  - `0x00B77043` → [VfNotifyOfHibernate](../../pagevrfy/B9/VfNotifyOfHibernate_function_00B97618.md) (`PAGELK` → `PAGEVRFY`)
  - `0x00B7706A` → [KeRebaselineInterruptTime](../../text/4E/KeRebaselineInterruptTime_function_004E34CC.md) (`PAGELK` → `.text`)
  - `0x00B7706F` → [KeRebaselineSystemTime](../../text/4E/KeRebaselineSystemTime_function_004E3554.md) (`PAGELK` → `.text`)
  - `0x00B770C2` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGELK` → `.text`)
  - `0x00B770D7` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (`PAGELK` → `.text`)
  - `0x00B770E3` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (`PAGELK` → `.text`)
  - `0x00B7713A` → [EtwTraceKernelEvent](../../text/23/EtwTraceKernelEvent_function_00235350.md) (`PAGELK` → `.text`)
  - `0x00B77215` → [BgLibraryInitialize](../../pagebgfx/BC/BgLibraryInitialize_function_00BC0760.md) (`PAGELK` → `PAGEBGFX`)
  - `0x00B7722C` → [KiLowerIrqlProcessIrqlFlags](../../text/4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (`PAGELK` → `.text`)
  - `0x00B77249` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGELK` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B76A6C  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
00B76A71  55                              push rbp
00B76A72  56                              push rsi
00B76A73  57                              push rdi
00B76A74  41 54                           push r12
00B76A76  41 55                           push r13
00B76A78  41 56                           push r14
00B76A7A  41 57                           push r15
00B76A7C  48 8D AC 24 30 FF FF FF         lea rbp, [rsp - 0xd0]
00B76A84  48 81 EC D0 01 00 00            sub rsp, 0x1d0
00B76A8B  48 8B 05 AE 3C 29 00            mov rax, qword ptr [rip + 0x293cae]
00B76A92  48 33 C4                        xor rax, rsp
00B76A95  48 89 85 C8 00 00 00            mov qword ptr [rbp + 0xc8], rax
00B76A9C  33 C0                           xor eax, eax
00B76A9E  4C 63 F9                        movsxd r15, ecx
00B76AA1  48 21 44 24 30                  and qword ptr [rsp + 0x30], rax
00B76AA6  48 8D 4D 90                     lea rcx, [rbp - 0x70]
00B76AAA  0F 57 C0                        xorps xmm0, xmm0
00B76AAD  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
00B76AB1  4C 8B F2                        mov r14, rdx
00B76AB4  89 45 88                        mov dword ptr [rbp - 0x78], eax
00B76AB7  44 8D 40 50                     lea r8d, [rax + 0x50]
00B76ABB  33 D2                           xor edx, edx
00B76ABD  0F 11 44 24 38                  movups xmmword ptr [rsp + 0x38], xmm0
00B76AC2  45 32 ED                        xor r13b, r13b
00B76AC5  41 BC 01 00 00 C0               mov r12d, 0xc0000001
00B76ACB  0F 11 44 24 50                  movups xmmword ptr [rsp + 0x50], xmm0
00B76AD0  0F 11 44 24 60                  movups xmmword ptr [rsp + 0x60], xmm0
00B76AD5  0F 11 44 24 70                  movups xmmword ptr [rsp + 0x70], xmm0
00B76ADA  E8 61 01 B5 FF                  call 0x1406c6c40
00B76ADF  33 C0                           xor eax, eax
00B76AE1  44 89 7D B8                     mov dword ptr [rbp - 0x48], r15d
00B76AE5  48 89 85 C0 00 00 00            mov qword ptr [rbp + 0xc0], rax
00B76AEC  48 8D 85 B0 00 00 00            lea rax, [rbp + 0xb0]
00B76AF3  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
00B76AF7  48 8D 05 02 5C 39 00            lea rax, [rip + 0x395c02]
00B76AFE  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
00B76B02  0F 57 C0                        xorps xmm0, xmm0
00B76B05  0F 11 85 B0 00 00 00            movups xmmword ptr [rbp + 0xb0], xmm0
00B76B0C  41 83 FF 07                     cmp r15d, 7
00B76B10  74 25                           je 0x140b76b37
00B76B12  4B 8D 0C 7F                     lea rcx, [r15 + r15*2]
00B76B16  48 8D 15 23 61 39 00            lea rdx, [rip + 0x396123]
00B76B1D  48 8D 04 CA                     lea rax, [rdx + rcx*8]
00B76B21  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
00B76B25  48 83 7C CA 08 00               cmp qword ptr [rdx + rcx*8 + 8], 0
00B76B2B  75 0A                           jne 0x140b76b37
00B76B2D  B8 C0 00 00 C0                  mov eax, 0xc00000c0
00B76B32  E9 08 07 00 00                  jmp 0x140b7723f
00B76B37  8B 05 43 FF 44 00               mov eax, dword ptr [rip + 0x44ff43]
00B76B3D  BE 01 00 00 00                  mov esi, 1
00B76B42  89 45 C0                        mov dword ptr [rbp - 0x40], eax
00B76B45  8B 05 35 FF 44 00               mov eax, dword ptr [rip + 0x44ff35]
00B76B4B  89 45 CC                        mov dword ptr [rbp - 0x34], eax
00B76B4E  41 8D 47 FC                     lea eax, [r15 - 4]
00B76B52  89 75 C8                        mov dword ptr [rbp - 0x38], esi
00B76B55  3B C6                           cmp eax, esi
00B76B57  76 3D                           jbe 0x140b76b96
00B76B59  8B 05 75 5E 39 00               mov eax, dword ptr [rip + 0x395e75]
00B76B5F  85 C0                           test eax, eax
00B76B61  74 0F                           je 0x140b76b72
00B76B63  48 8B 55 90                     mov rdx, qword ptr [rbp - 0x70]
00B76B67  8B 4A 10                        mov ecx, dword ptr [rdx + 0x10]
00B76B6A  0F BA E9 12                     bts ecx, 0x12
00B76B6E  48 89 4A 10                     mov qword ptr [rdx + 0x10], rcx
00B76B72  41 83 FF 03                     cmp r15d, 3
00B76B76  74 06                           je 0x140b76b7e
00B76B78  41 83 FF 06                     cmp r15d, 6
00B76B7C  75 18                           jne 0x140b76b96
00B76B7E  4D 85 F6                        test r14, r14
00B76B81  74 13                           je 0x140b76b96
00B76B83  48 8D 05 D6 37 B4 FF            lea rax, [rip - 0x4bc82a]
00B76B8A  4C 89 75 A8                     mov qword ptr [rbp - 0x58], r14
00B76B8E  48 89 45 98                     mov qword ptr [rbp - 0x68], rax
00B76B92  4C 89 75 A0                     mov qword ptr [rbp - 0x60], r14
00B76B96  33 D2                           xor edx, edx
00B76B98  48 8D 4D 10                     lea rcx, [rbp + 0x10]
00B76B9C  41 B8 A0 00 00 00               mov r8d, 0xa0
00B76BA2  E8 99 00 B5 FF                  call 0x1406c6c40
00B76BA7  BF 02 00 00 00                  mov edi, 2
00B76BAC  4D 85 F6                        test r14, r14
00B76BAF  0F 85 CF 00 00 00               jne 0x140b76c84
00B76BB5  48 8B 05 F4 C5 3A 00            mov rax, qword ptr [rip + 0x3ac5f4]
00B76BBC  33 D2                           xor edx, edx
00B76BBE  89 54 24 42                     mov dword ptr [rsp + 0x42], edx
00B76BC2  66 89 54 24 46                  mov word ptr [rsp + 0x46], dx
00B76BC7  8B 08                           mov ecx, dword ptr [rax]
00B76BC9  8B C1                           mov eax, ecx
00B76BCB  C1 E8 06                        shr eax, 6
00B76BCE  83 E1 3F                        and ecx, 0x3f
00B76BD1  66 89 44 24 40                  mov word ptr [rsp + 0x40], ax
00B76BD6  48 8B C6                        mov rax, rsi
00B76BD9  48 D3 E0                        shl rax, cl
00B76BDC  48 8D 4C 24 38                  lea rcx, [rsp + 0x38]
00B76BE1  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00B76BE6  E8 55 25 82 FF                  call 0x140399140
00B76BEB  45 0F 20 C5                     mov r13, cr8
00B76BEF  44 0F 22 C7                     mov cr8, rdi
00B76BF3  44 39 35 26 01 45 00            cmp dword ptr [rip + 0x450126], r14d
00B76BFA  74 0B                           je 0x140b76c07
00B76BFC  40 8A D7                        mov dl, dil
00B76BFF  41 8A CD                        mov cl, r13b
00B76C02  E8 F5 EA 97 FF                  call 0x1404f56fc
00B76C07  4C 8D 45 90                     lea r8, [rbp - 0x70]
00B76C0B  48 8D 15 5E 06 00 00            lea rdx, [rip + 0x65e]
00B76C12  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
00B76C17  E8 B4 4F 8E FF                  call 0x14045bbd0
00B76C1C  8B 05 5E FE 44 00               mov eax, dword ptr [rip + 0x44fe5e]
00B76C22  33 DB                           xor ebx, ebx
00B76C24  40 88 7C 24 51                  mov byte ptr [rsp + 0x51], dil
00B76C29  85 C0                           test eax, eax
00B76C2B  74 51                           je 0x140b76c7e
00B76C2D  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
00B76C36  3B 58 24                        cmp ebx, dword ptr [rax + 0x24]
00B76C39  74 32                           je 0x140b76c6d
00B76C3B  8B 7D C4                        mov edi, dword ptr [rbp - 0x3c]
00B76C3E  48 8B 45 88                     mov rax, qword ptr [rbp - 0x78]
00B76C42  48 85 C0                        test rax, rax
00B76C45  75 0C                           jne 0x140b76c53
00B76C47  B8 00 08 00 00                  mov eax, 0x800
00B76C4C  03 C3                           add eax, ebx
00B76C4E  66 89 44 24 52                  mov word ptr [rsp + 0x52], ax
00B76C53  45 33 C0                        xor r8d, r8d
00B76C56  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
00B76C5B  33 D2                           xor edx, edx
00B76C5D  E8 EE 0F 69 FF                  call 0x140207c50
00B76C62  EB 02                           jmp 0x140b76c66
00B76C64  F3 90                           pause
00B76C66  8B 45 C4                        mov eax, dword ptr [rbp - 0x3c]
00B76C69  3B F8                           cmp edi, eax
00B76C6B  74 F7                           je 0x140b76c64
00B76C6D  8B 05 0D FE 44 00               mov eax, dword ptr [rip + 0x44fe0d]
00B76C73  03 DE                           add ebx, esi
00B76C75  3B D8                           cmp ebx, eax
00B76C77  72 B4                           jb 0x140b76c2d
00B76C79  BF 02 00 00 00                  mov edi, 2
00B76C7E  48 8D 75 90                     lea rsi, [rbp - 0x70]
00B76C82  EB 7E                           jmp 0x140b76d02
00B76C84  48 8B 45 90                     mov rax, qword ptr [rbp - 0x70]
00B76C88  48 8D 95 A0 00 00 00            lea rdx, [rbp + 0xa0]
00B76C8F  48 89 05 2A 0A 2B 00            mov qword ptr [rip + 0x2b0a2a], rax
00B76C96  48 8D 0D 63 0A 2B 00            lea rcx, [rip + 0x2b0a63]
00B76C9D  48 8B 45 98                     mov rax, qword ptr [rbp - 0x68]
00B76CA1  48 8D 35 18 0A 2B 00            lea rsi, [rip + 0x2b0a18]
00B76CA8  48 89 05 19 0A 2B 00            mov qword ptr [rip + 0x2b0a19], rax
00B76CAF  48 8B 45 A0                     mov rax, qword ptr [rbp - 0x60]
00B76CB3  48 89 05 16 0A 2B 00            mov qword ptr [rip + 0x2b0a16], rax
00B76CBA  48 8B 45 A8                     mov rax, qword ptr [rbp - 0x58]
00B76CBE  48 89 05 13 0A 2B 00            mov qword ptr [rip + 0x2b0a13], rax
00B76CC5  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
00B76CC9  48 89 05 10 0A 2B 00            mov qword ptr [rip + 0x2b0a10], rax
00B76CD0  8B 45 B8                        mov eax, dword ptr [rbp - 0x48]
00B76CD3  89 05 0F 0A 2B 00               mov dword ptr [rip + 0x2b0a0f], eax
00B76CD9  8A 45 BC                        mov al, byte ptr [rbp - 0x44]
00B76CDC  88 05 0A 0A 2B 00               mov byte ptr [rip + 0x2b0a0a], al
00B76CE2  8B 45 C0                        mov eax, dword ptr [rbp - 0x40]
00B76CE5  89 05 05 0A 2B 00               mov dword ptr [rip + 0x2b0a05], eax
00B76CEB  8B 45 CC                        mov eax, dword ptr [rbp - 0x34]
00B76CEE  89 05 08 0A 2B 00               mov dword ptr [rip + 0x2b0a08], eax
00B76CF4  8B 45 C8                        mov eax, dword ptr [rbp - 0x38]
00B76CF7  89 05 FB 09 2B 00               mov dword ptr [rip + 0x2b09fb], eax
00B76CFD  E8 AE 38 B4 FF                  call 0x1406ba5b0
00B76D02  44 8B C7                        mov r8d, edi
00B76D05  48 8D 55 10                     lea rdx, [rbp + 0x10]
00B76D09  48 8B CE                        mov rcx, rsi
00B76D0C  E8 DB 05 00 00                  call 0x140b772ec
00B76D11  41 B8 03 00 00 00               mov r8d, 3
00B76D17  48 8D 55 10                     lea rdx, [rbp + 0x10]
00B76D1B  48 8B CE                        mov rcx, rsi
00B76D1E  E8 C9 05 00 00                  call 0x140b772ec
00B76D23  83 3D 42 50 39 00 04            cmp dword ptr [rip + 0x395042], 4
00B76D2A  75 17                           jne 0x140b76d43
00B76D2C  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
00B76D35  33 FF                           xor edi, edi
00B76D37  8B 48 44                        mov ecx, dword ptr [rax + 0x44]
00B76D3A  48 69 D9 40 42 0F 00            imul rbx, rcx, 0xf4240
00B76D41  EB 11                           jmp 0x140b76d54
00B76D43  48 8B 1D 96 FE 44 00            mov rbx, qword ptr [rip + 0x44fe96]
00B76D4A  33 C9                           xor ecx, ecx
00B76D4C  E8 8F 7A 80 FF                  call 0x14037e7e0
00B76D51  48 8B F8                        mov rdi, rax
00B76D54  F7 05 B2 FD 44 00 00 80 00 00   test dword ptr [rip + 0x44fdb2], 0x8000
00B76D5E  74 3D                           je 0x140b76d9d
00B76D60  83 65 EC 00                     and dword ptr [rbp - 0x14], 0
00B76D64  48 8D 45 00                     lea rax, [rbp]
00B76D68  41 B9 30 12 00 00               mov r9d, 0x1230
00B76D6E  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
00B76D72  BA 01 00 00 00                  mov edx, 1
00B76D77  48 89 7D 00                     mov qword ptr [rbp], rdi
00B76D7B  41 B8 00 80 00 80               mov r8d, 0x80008000
00B76D81  48 89 5D 08                     mov qword ptr [rbp + 8], rbx
00B76D85  48 8D 4D E0                     lea rcx, [rbp - 0x20]
00B76D89  C7 45 E8 10 00 00 00            mov dword ptr [rbp - 0x18], 0x10
00B76D90  C7 44 24 20 02 18 50 00         mov dword ptr [rsp + 0x20], 0x501802
00B76D98  E8 B3 E5 6B FF                  call 0x140235350
00B76D9D  41 B8 04 00 00 00               mov r8d, 4
00B76DA3  48 8D 55 10                     lea rdx, [rbp + 0x10]
00B76DA7  48 8B CE                        mov rcx, rsi
00B76DAA  E8 3D 05 00 00                  call 0x140b772ec
00B76DAF  4D 85 F6                        test r14, r14
00B76DB2  74 17                           je 0x140b76dcb
00B76DB4  C6 05 91 0D 2F 00 00            mov byte ptr [rip + 0x2f0d91], 0
00B76DBB  E8 30 05 95 FF                  call 0x1404c72f0
00B76DC0  85 C0                           test eax, eax
00B76DC2  74 07                           je 0x140b76dcb
00B76DC4  B1 01                           mov cl, 1
00B76DC6  E8 4D 08 02 00                  call 0x140b97618
00B76DCB  B9 11 00 00 00                  mov ecx, 0x11
00B76DD0  C6 05 4C 4F 39 00 01            mov byte ptr [rip + 0x394f4c], 1
00B76DD7  E8 B4 0E 00 00                  call 0x140b77c90
00B76DDC  83 BD 88 00 00 00 00            cmp dword ptr [rbp + 0x88], 0
00B76DE3  0F 8C 2E 02 00 00               jl 0x140b77017
00B76DE9  41 B8 0C 00 00 00               mov r8d, 0xc
00B76DEF  C6 46 2C 01                     mov byte ptr [rsi + 0x2c], 1
00B76DF3  48 8D 55 10                     lea rdx, [rbp + 0x10]
00B76DF7  48 8B CE                        mov rcx, rsi
00B76DFA  E8 ED 04 00 00                  call 0x140b772ec
00B76DFF  41 83 FF 03                     cmp r15d, 3
00B76E03  74 12                           je 0x140b76e17
00B76E05  41 83 FF 06                     cmp r15d, 6
00B76E09  74 0C                           je 0x140b76e17
00B76E0B  48 8B 05 16 9D 28 00            mov rax, qword ptr [rip + 0x289d16]
00B76E12  E8 B9 3C B4 FF                  call 0x1406baad0
00B76E17  45 33 FF                        xor r15d, r15d
00B76E1A  4D 85 F6                        test r14, r14
00B76E1D  74 3D                           je 0x140b76e5c
00B76E1F  45 8D 47 05                     lea r8d, [r15 + 5]
00B76E23  48 8B CE                        mov rcx, rsi
00B76E26  48 8D 55 10                     lea rdx, [rbp + 0x10]
00B76E2A  E8 BD 04 00 00                  call 0x140b772ec
00B76E2F  E8 3C 0D 96 FF                  call 0x1404d7b70
00B76E34  0F BA 25 A4 54 39 00 08         bt dword ptr [rip + 0x3954a4], 8
00B76E3C  72 0C                           jb 0x140b76e4a
00B76E3E  E8 29 28 00 00                  call 0x140b7966c
00B76E43  C6 05 F9 92 2B 00 01            mov byte ptr [rip + 0x2b92f9], 1
00B76E4A  41 B8 0A 00 00 00               mov r8d, 0xa
00B76E50  48 8D 55 10                     lea rdx, [rbp + 0x10]
00B76E54  48 8B CE                        mov rcx, rsi
00B76E57  E8 90 04 00 00                  call 0x140b772ec
00B76E5C  B9 12 00 00 00                  mov ecx, 0x12
00B76E61  E8 2A 0E 00 00                  call 0x140b77c90
00B76E66  41 B8 06 00 00 00               mov r8d, 6
00B76E6C  48 8D 55 10                     lea rdx, [rbp + 0x10]
00B76E70  48 8B CE                        mov rcx, rsi
00B76E73  E8 74 04 00 00                  call 0x140b772ec
00B76E78  B9 1A 00 00 00                  mov ecx, 0x1a
00B76E7D  E8 0E 0E 00 00                  call 0x140b77c90
00B76E82  44 8B A5 88 00 00 00            mov r12d, dword ptr [rbp + 0x88]
00B76E89  E8 3E C6 96 FF                  call 0x1404e34cc
00B76E8E  48 8B 05 83 9C 28 00            mov rax, qword ptr [rip + 0x289c83]
00B76E95  E8 36 3C B4 FF                  call 0x1406baad0
00B76E9A  4D 85 F6                        test r14, r14
00B76E9D  74 1B                           je 0x140b76eba
00B76E9F  41 81 FC 94 02 00 40            cmp r12d, 0x40000294
00B76EA6  75 12                           jne 0x140b76eba
00B76EA8  41 B8 07 00 00 00               mov r8d, 7
00B76EAE  48 8D 55 10                     lea rdx, [rbp + 0x10]
00B76EB2  48 8B CE                        mov rcx, rsi
00B76EB5  E8 32 04 00 00                  call 0x140b772ec
00B76EBA  41 B8 08 00 00 00               mov r8d, 8
00B76EC0  48 8D 55 10                     lea rdx, [rbp + 0x10]
00B76EC4  48 8B CE                        mov rcx, rsi
00B76EC7  E8 20 04 00 00                  call 0x140b772ec
00B76ECC  4D 85 F6                        test r14, r14
00B76ECF  0F 84 A5 00 00 00               je 0x140b76f7a
00B76ED5  41 81 FC 94 02 00 40            cmp r12d, 0x40000294
00B76EDC  75 26                           jne 0x140b76f04
00B76EDE  B9 1B 00 00 00                  mov ecx, 0x1b
00B76EE3  E8 A8 0D 00 00                  call 0x140b77c90
00B76EE8  41 B8 09 00 00 00               mov r8d, 9
00B76EEE  48 8D 55 10                     lea rdx, [rbp + 0x10]
00B76EF2  48 8B CE                        mov rcx, rsi
00B76EF5  E8 F2 03 00 00                  call 0x140b772ec
00B76EFA  B9 20 00 00 00                  mov ecx, 0x20
00B76EFF  E8 8C 0D 00 00                  call 0x140b77c90
00B76F04  48 8B 0D 3D 50 39 00            mov rcx, qword ptr [rip + 0x39503d]
00B76F0B  BA 13 00 00 00                  mov edx, 0x13
00B76F10  E8 5B DA FF FF                  call 0x140b74970
00B76F15  49 8B 8E 50 01 00 00            mov rcx, qword ptr [r14 + 0x150]
00B76F1C  48 85 C9                        test rcx, rcx
00B76F1F  74 0F                           je 0x140b76f30
00B76F21  41 8B 96 20 01 00 00            mov edx, dword ptr [r14 + 0x120]
00B76F28  C1 E2 04                        shl edx, 4
00B76F2B  E8 40 DA FF FF                  call 0x140b74970
00B76F30  41 B8 0A 00 00 00               mov r8d, 0xa
00B76F36  48 8D 55 10                     lea rdx, [rbp + 0x10]
00B76F3A  48 8B CE                        mov rcx, rsi
00B76F3D  E8 AA 03 00 00                  call 0x140b772ec
00B76F42  0F BA 25 96 53 39 00 08         bt dword ptr [rip + 0x395396], 8
00B76F4A  72 13                           jb 0x140b76f5f
00B76F4C  44 88 3D F0 91 2B 00            mov byte ptr [rip + 0x2b91f0], r15b
00B76F53  E8 14 27 00 00                  call 0x140b7966c
00B76F58  33 C9                           xor ecx, ecx
00B76F5A  E8 C5 CE FF FF                  call 0x140b73e24
00B76F5F  45 88 7E 02                     mov byte ptr [r14 + 2], r15b
00B76F63  E8 A0 3B A5 FF                  call 0x1405cab08
00B76F68  41 B8 0B 00 00 00               mov r8d, 0xb
00B76F6E  48 8D 55 10                     lea rdx, [rbp + 0x10]
00B76F72  48 8B CE                        mov rcx, rsi
00B76F75  E8 72 03 00 00                  call 0x140b772ec
00B76F7A  8B 1D 00 09 2F 00               mov ebx, dword ptr [rip + 0x2f0900]
00B76F80  F6 C3 01                        test bl, 1
00B76F83  74 11                           je 0x140b76f96
00B76F85  44 38 3D 6C 06 3D 00            cmp byte ptr [rip + 0x3d066c], r15b
00B76F8C  74 08                           je 0x140b76f96
00B76F8E  41 8B CC                        mov ecx, r12d
00B76F91  E8 4A 75 98 FF                  call 0x1404fe4e0
00B76F96  F6 C3 02                        test bl, 2
00B76F99  74 1A                           je 0x140b76fb5
00B76F9B  45 33 C9                        xor r9d, r9d
00B76F9E  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00B76FA3  45 33 C0                        xor r8d, r8d
00B76FA6  B9 A0 00 00 00                  mov ecx, 0xa0
00B76FAB  41 8D 51 0A                     lea edx, [r9 + 0xa]
00B76FAF  E8 AC 66 98 FF                  call 0x1404fd660
00B76FB4  CC                              int3
00B76FB5  44 88 3D 38 57 39 00            mov byte ptr [rip + 0x395738], r15b
00B76FBC  45 85 E4                        test r12d, r12d
00B76FBF  78 3E                           js 0x140b76fff
00B76FC1  FF 05 F9 5F 39 00               inc dword ptr [rip + 0x395ff9]
00B76FC7  44 38 3D B2 56 39 00            cmp byte ptr [rip + 0x3956b2], r15b
00B76FCE  44 89 3D 13 5D 39 00            mov dword ptr [rip + 0x395d13], r15d
00B76FD5  44 89 3D A8 56 39 00            mov dword ptr [rip + 0x3956a8], r15d
00B76FDC  44 89 3D A5 56 39 00            mov dword ptr [rip + 0x3956a5], r15d
00B76FE3  C7 05 7B 4C 39 00 01 00 00 00   mov dword ptr [rip + 0x394c7b], 1
00B76FED  74 10                           je 0x140b76fff
00B76FEF  F0 83 0D 8D 56 39 00 01         lock or dword ptr [rip + 0x39568d], 1
00B76FF7  F0 83 0D 89 56 39 00 19         lock or dword ptr [rip + 0x395689], 0x19
00B76FFF  41 B8 0C 00 00 00               mov r8d, 0xc
00B77005  44 88 7E 2C                     mov byte ptr [rsi + 0x2c], r15b
00B77009  48 8D 55 10                     lea rdx, [rbp + 0x10]
00B7700D  48 8B CE                        mov rcx, rsi
00B77010  E8 D7 02 00 00                  call 0x140b772ec
00B77015  EB 03                           jmp 0x140b7701a
00B77017  45 33 FF                        xor r15d, r15d
00B7701A  4D 85 F6                        test r14, r14
00B7701D  74 4B                           je 0x140b7706a
00B7701F  41 81 FC C0 00 00 C0            cmp r12d, 0xc00000c0
00B77026  75 02                           jne 0x140b7702a
00B77028  EB FE                           jmp 0x140b77028
00B7702A  44 89 3D 27 6E 39 00            mov dword ptr [rip + 0x396e27], r15d
00B77031  45 89 A6 CC 00 00 00            mov dword ptr [r14 + 0xcc], r12d
00B77038  E8 B3 02 95 FF                  call 0x1404c72f0
00B7703D  85 C0                           test eax, eax
00B7703F  74 07                           je 0x140b77048
00B77041  33 C9                           xor ecx, ecx
00B77043  E8 D0 05 02 00                  call 0x140b97618
00B77048  48 8D 05 C1 17 29 00            lea rax, [rip + 0x2917c1]
00B7704F  48 39 05 BA 17 29 00            cmp qword ptr [rip + 0x2917ba], rax
00B77056  75 07                           jne 0x140b7705f
00B77058  C6 05 ED 0A 2F 00 01            mov byte ptr [rip + 0x2f0aed], 1
00B7705F  41 C7 86 CC 00 00 00 94 02 00 40  mov dword ptr [r14 + 0xcc], 0x40000294
00B7706A  E8 5D C4 96 FF                  call 0x1404e34cc
00B7706F  E8 E0 C4 96 FF                  call 0x1404e3554
00B77074  B9 21 00 00 00                  mov ecx, 0x21
00B77079  E8 12 0C 00 00                  call 0x140b77c90
00B7707E  41 B8 0D 00 00 00               mov r8d, 0xd
00B77084  44 88 3D 98 4C 39 00            mov byte ptr [rip + 0x394c98], r15b
00B7708B  48 8D 55 10                     lea rdx, [rbp + 0x10]
00B7708F  48 8B CE                        mov rcx, rsi
00B77092  E8 55 02 00 00                  call 0x140b772ec
00B77097  45 85 E4                        test r12d, r12d
00B7709A  0F 88 F7 00 00 00               js 0x140b77197
00B770A0  83 3D C5 4C 39 00 04            cmp dword ptr [rip + 0x394cc5], 4
00B770A7  75 29                           jne 0x140b770d2
00B770A9  44 38 3D D0 55 39 00            cmp byte ptr [rip + 0x3955d0], r15b
00B770B0  75 20                           jne 0x140b770d2
00B770B2  48 8B 05 47 98 28 00            mov rax, qword ptr [rip + 0x289847]
00B770B9  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
00B770BE  33 D2                           xor edx, edx
00B770C0  B3 01                           mov bl, 1
00B770C2  E8 09 3A B4 FF                  call 0x1406baad0
00B770C7  84 C0                           test al, al
00B770C9  75 2B                           jne 0x140b770f6
00B770CB  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
00B770D0  EB 24                           jmp 0x140b770f6
00B770D2  33 C9                           xor ecx, ecx
00B770D4  41 8A DF                        mov bl, r15b
00B770D7  E8 04 77 80 FF                  call 0x14037e7e0
00B770DC  33 C9                           xor ecx, ecx
00B770DE  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00B770E3  E8 F8 76 80 FF                  call 0x14037e7e0
00B770E8  48 2B 05 81 06 39 00            sub rax, qword ptr [rip + 0x390681]
00B770EF  48 89 05 92 53 39 00            mov qword ptr [rip + 0x395392], rax
00B770F6  F7 05 10 FA 44 00 00 80 00 00   test dword ptr [rip + 0x44fa10], 0x8000
00B77100  74 3D                           je 0x140b7713f
00B77102  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
00B77107  48 8D 4D F0                     lea rcx, [rbp - 0x10]
00B7710B  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00B77110  41 B9 31 12 00 00               mov r9d, 0x1231
00B77116  48 8D 44 24 48                  lea rax, [rsp + 0x48]
00B7711B  48 C7 45 F8 08 00 00 00         mov qword ptr [rbp - 8], 8
00B77123  BA 01 00 00 00                  mov edx, 1
00B77128  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00B7712C  41 B8 00 80 00 80               mov r8d, 0x80008000
00B77132  C7 44 24 20 02 18 50 00         mov dword ptr [rsp + 0x20], 0x501802
00B7713A  E8 11 E2 6B FF                  call 0x140235350
00B7713F  84 DB                           test bl, bl
00B77141  74 54                           je 0x140b77197
00B77143  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
00B7714C  33 D2                           xor edx, edx
00B7714E  8B 48 44                        mov ecx, dword ptr [rax + 0x44]
00B77151  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
00B77156  4C 69 C1 E8 03 00 00            imul r8, rcx, 0x3e8
00B7715D  48 8B 0D 7C FA 44 00            mov rcx, qword ptr [rip + 0x44fa7c]
00B77164  49 F7 F0                        div r8
00B77167  4C 8B C8                        mov r9, rax
00B7716A  48 B8 77 BE 9F 1A 2F DD 24 06   movabs rax, 0x624dd2f1a9fbe77
00B77174  48 F7 E1                        mul rcx
00B77177  48 2B CA                        sub rcx, rdx
00B7717A  48 D1 E9                        shr rcx, 1
00B7717D  48 03 CA                        add rcx, rdx
00B77180  48 C1 E9 09                     shr rcx, 9
00B77184  4C 0F AF C9                     imul r9, rcx
00B77188  4C 89 4C 24 30                  mov qword ptr [rsp + 0x30], r9
00B7718D  4C 2B CF                        sub r9, rdi
00B77190  4C 89 0D B1 51 39 00            mov qword ptr [rip + 0x3951b1], r9
00B77197  41 B8 0E 00 00 00               mov r8d, 0xe
00B7719D  48 8D 55 10                     lea rdx, [rbp + 0x10]
00B771A1  48 8B CE                        mov rcx, rsi
00B771A4  E8 43 01 00 00                  call 0x140b772ec
00B771A9  41 B8 0F 00 00 00               mov r8d, 0xf
00B771AF  48 8D 55 10                     lea rdx, [rbp + 0x10]
00B771B3  48 8B CE                        mov rcx, rsi
00B771B6  E8 31 01 00 00                  call 0x140b772ec
00B771BB  41 B8 10 00 00 00               mov r8d, 0x10
00B771C1  48 8D 55 10                     lea rdx, [rbp + 0x10]
00B771C5  48 8B CE                        mov rcx, rsi
00B771C8  E8 1F 01 00 00                  call 0x140b772ec
00B771CD  44 39 BD 88 00 00 00            cmp dword ptr [rbp + 0x88], r15d
00B771D4  7C 16                           jl 0x140b771ec
00B771D6  48 8B 0E                        mov rcx, qword ptr [rsi]
00B771D9  44 89 BD 88 00 00 00            mov dword ptr [rbp + 0x88], r15d
00B771E0  8A 41 05                        mov al, byte ptr [rcx + 5]
00B771E3  3C FF                           cmp al, 0xff
00B771E5  74 05                           je 0x140b771ec
00B771E7  FE C0                           inc al
00B771E9  88 41 05                        mov byte ptr [rcx + 5], al
00B771EC  4D 85 F6                        test r14, r14
00B771EF  74 2B                           je 0x140b7721c
00B771F1  41 81 FC 94 02 00 40            cmp r12d, 0x40000294
00B771F8  75 3F                           jne 0x140b77239
00B771FA  44 38 3D 60 4D 39 00            cmp byte ptr [rip + 0x394d60], r15b
00B77201  75 36                           jne 0x140b77239
00B77203  44 38 3D AF EC 2E 00            cmp byte ptr [rip + 0x2eecaf], r15b
00B7720A  74 2D                           je 0x140b77239
00B7720C  48 8B 0D 7D EC 2E 00            mov rcx, qword ptr [rip + 0x2eec7d]
00B77213  33 D2                           xor edx, edx
00B77215  E8 46 95 04 00                  call 0x140bc0760
00B7721A  EB 1D                           jmp 0x140b77239
00B7721C  44 39 3D FD FA 44 00            cmp dword ptr [rip + 0x44fafd], r15d
00B77223  74 0C                           je 0x140b77231
00B77225  44 0F 20 C1                     mov rcx, cr8
00B77229  41 8A D5                        mov dl, r13b
00B7722C  E8 67 E4 97 FF                  call 0x1404f5698
00B77231  41 0F B6 C5                     movzx eax, r13b
00B77235  44 0F 22 C0                     mov cr8, rax
00B77239  8B 85 88 00 00 00               mov eax, dword ptr [rbp + 0x88]
00B7723F  48 8B 8D C8 00 00 00            mov rcx, qword ptr [rbp + 0xc8]
00B77246  48 33 CC                        xor rcx, rsp
00B77249  E8 F2 53 B3 FF                  call 0x1406ac640
00B7724E  48 8B 9C 24 20 02 00 00         mov rbx, qword ptr [rsp + 0x220]
00B77256  48 81 C4 D0 01 00 00            add rsp, 0x1d0
00B7725D  41 5F                           pop r15
00B7725F  41 5E                           pop r14
00B77261  41 5D                           pop r13
00B77263  41 5C                           pop r12
00B77265  5F                              pop rdi
00B77266  5E                              pop rsi
00B77267  5D                              pop rbp
00B77268  C3                              ret
00B77269  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopInvokeSystemStateHandler(int a1, __int64 a2)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned int v_stack_m11C;
    unsigned int v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned int v_stack_m13C;
    unsigned int v_stack_m140;
    unsigned int v_stack_m144;
    unsigned int v_stack_m148;
    unsigned __int8 v_stack_m14C;
    unsigned int v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned int v_stack_m180;
    unsigned __int64 v_stack_m188;
    unsigned __int64 v_stack_m198;
    unsigned __int64 v_stack_m1A8;
    unsigned __int16 v_stack_m1B6;
    unsigned __int8 v_stack_m1B7;
    unsigned __int64 v_stack_m1B8;
    unsigned __int64 v_stack_m1C0;
    unsigned __int16 v_stack_m1C2;
    unsigned int v_stack_m1C6;
    unsigned __int16 v_stack_m1C8;
    unsigned __int64 v_stack_m1D0;
    unsigned __int64 v_stack_m1D8;
    unsigned int v_stack_m1E8;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_m80;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p18;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (464);
    result = (*(unsigned __int64 *)(v_rip + 2702510)) ^ (v_rsp);
    v_stack_m40 = result;
    result = 0;
    v_stack_m188 = 0;
    v_stack_m180 = 0;
    a2 = 0;
    v_stack_m1D0 = v_xmm0;
    v_r13 = 0;
    v_stack_m1B8 = v_xmm0;
    v_stack_m1A8 = v_xmm0;
    v_stack_m198 = v_xmm0;
    result = memset(v_stack_m178, a2, result + 80, a4);
    result = 0;
    v_stack_m150 = (unsigned int)((int)(a1));
    v_stack_m48 = 0;
    v_stack_m178 = v_stack_m58;
    v_stack_m158 = v_rip + 3759106;
    v_stack_m58 = v_xmm0;
    if (((unsigned int)((int)(a1))) == 7) goto loc_00B76B37;
    v_stack_m178 = v_rip + 3760419 + (int)(a1) + (int)(a1) * 2 * 8;
    if ((*(unsigned __int64 *)(v_rip + 3760419 + (int)(a1) + (int)(a1) * 2 * 8 + 8)) != 0) goto loc_00B76B37;
    goto loc_00B7723F;
loc_00B76B37:
    v_stack_m148 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4521795)));
    v_stack_m13C = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4521781)));
    v_stack_m140 = 1;
    if (((unsigned int)((int)(a1) - 4)) <= 1) goto loc_00B76B96;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3759733))) != 0) {
        a2 = v_stack_m178;
        a1 = *(unsigned int *)(a2 + 16);
        *(unsigned __int64 *)(a2 + 16) = a1;
    }
    if (((unsigned int)((int)(a1))) == 3) goto loc_00B76B7E;
    if (((unsigned int)((int)(a1))) != 6) goto loc_00B76B96;
loc_00B76B7E:
    result = (unsigned int)(*(unsigned int *)(v_rip + 3759733));
    if (a2 != 0) {
        result = v_rip - 4966442;
        v_stack_m160 = a2;
        v_stack_m170 = result;
        v_stack_m168 = a2;
    }
    a2 = 0;
    result = memset(v_stack_mF8, a2, 160, a4);
    if (0 != 0) goto loc_00B76C84;
    a2 = 0;
    v_stack_m1C6 = 0;
    v_stack_m1C2 = 0;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3851764)))))) >> (6));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3851764)))) & (63));
    v_stack_m1C8 = (unsigned __int16)(result);
    result = (1) << ((unsigned __int8)(a1));
    v_stack_m1D0 = result;
    result = KeSetSystemGroupAffinityThread(v_stack_m1D0, a2, 160, a4);
    if ((*(unsigned int *)(v_rip + 4522278)) != 0) {
        a2 = 2;
        a1 = (unsigned __int8)(v_cr8);
        result = KiRaiseIrqlProcessIrqlFlags(a1, a2, 160, a4);
    }
    result = KeInitializeDpc(v_stack_m1B8, v_rip + 1630, v_stack_m178, a4);
    v_rbx = 0;
    v_stack_m1B7 = 2;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4521566))) == 0) goto loc_00B76C7E;
loc_00B76C2D:
    if (0 == (*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36))) goto loc_00B76C6D;
    result = v_stack_m180;
    if (v_stack_m180 == 0) {
        result = 0x800ULL;
        result = (unsigned int)((result) + (0));
        v_stack_m1B6 = (unsigned __int16)(result);
    }
    a3 = 0;
    a2 = 0;
    result = KeInsertQueueDpc(v_stack_m1B8, a2, a3, a4);
    goto loc_00B76C66;
loc_00B76C64:
loc_00B76C66:
    if (((unsigned int)((unsigned int)(v_stack_m144))) == ((unsigned int)((unsigned int)(v_stack_m144)))) goto loc_00B76C64;
loc_00B76C6D:
    v_rbx = (unsigned int)((v_rbx) + (1));
    if (((unsigned int)(v_rbx)) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4521485))))) goto loc_00B76C2D;
loc_00B76C7E:
    goto loc_00B76D02;
loc_00B76C84:
    *(unsigned __int64 *)(v_rip + 2820650) = v_stack_m178;
    *(unsigned __int64 *)(v_rip + 2820633) = v_stack_m170;
    *(unsigned __int64 *)(v_rip + 2820630) = v_stack_m168;
    *(unsigned __int64 *)(v_rip + 2820627) = v_stack_m160;
    *(unsigned __int64 *)(v_rip + 2820624) = v_stack_m158;
    *(unsigned int *)(v_rip + 2820623) = (unsigned int)((unsigned int)(v_stack_m150));
    *(unsigned __int8 *)(v_rip + 2820618) = (unsigned __int8)(v_stack_m14C);
    *(unsigned int *)(v_rip + 2820613) = (unsigned int)((unsigned int)(v_stack_m148));
    *(unsigned int *)(v_rip + 2820616) = (unsigned int)((unsigned int)(v_stack_m13C));
    *(unsigned int *)(v_rip + 2820603) = (unsigned int)((unsigned int)(v_stack_m140));
    result = ExpInterlockedPushEntrySList(v_rip + 2820707, v_stack_m68, a3, a4);
loc_00B76D02:
    result = PopIssueNextState(v_rip + 2820632, v_stack_mF8, 2, a4);
    result = PopIssueNextState(v_rip + 2820632, v_stack_mF8, 3, a4);
    if ((*(unsigned int *)(v_rip + 3756098)) != 4) goto loc_00B76D43;
    v_rdi = 0;
    v_rbx = (v_rbx) * ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 68)));
    goto loc_00B76D54;
loc_00B76D43:
    a1 = 0;
    result = KeQueryPerformanceCounter(a1, v_stack_mF8, 3, a4);
loc_00B76D54:
    if (((*(unsigned int *)(v_rip + 4521394)) & (0x8000ULL)) != 0) {
        result = v_stack_m108;
        a4 = 0x1230ULL;
        v_stack_m128 = result;
        a2 = 1;
        v_stack_m108 = result;
        a3 = 0x80008000ULL;
        v_stack_m100 = *(unsigned __int64 *)(v_rip + 4521622);
        a1 = v_stack_m128;
        v_stack_m120 = 16;
        v_stack_m1E8 = 0x501802ULL;
        result = EtwTraceKernelEvent(a1, a2, a3, a4);
    }
    result = PopIssueNextState(v_rip + 2820632, v_stack_mF8, 4, a4);
    if (a2 == 0) goto loc_00B76DCB;
    *(unsigned __int8 *)(v_rip + 3083665) = 0;
    result = VfIsVerifierEnabled(v_rip + 2820632, v_stack_mF8, 4, a4);
    if ((unsigned int)(result) != 0) {
        a1 = 1;
        result = VfNotifyOfHibernate(a1, v_stack_mF8, 4, a4);
    }
    *(unsigned __int8 *)(v_rip + 3755852) = 1;
    result = PopCheckpointSystemSleep(17, v_stack_mF8, 4, a4);
    if (v_stack_m80 < 0) goto loc_00B77017;
    *(unsigned __int8 *)(v_rip + 2820632 + 44) = 1;
    result = PopIssueNextState(v_rip + 2820632, v_stack_mF8, 12, a4);
    if (((unsigned int)((int)(a1))) == 3) goto loc_00B76E17;
    if (((unsigned int)((int)(a1))) != 6) {
        result = *(unsigned __int64 *)(v_rip + 2661654);
        result = guard_dispatch_icall(v_rip + 2820632, v_stack_mF8, 12, a4);
    }
    v_r15 = 0;
    if (a2 == 0) goto loc_00B76E5C;
    result = PopIssueNextState(v_rip + 2820632, v_stack_mF8, v_r15 + 5, a4);
    result = KeSuspendDynamicTracing(v_rip + 2820632, v_stack_mF8, v_r15 + 5, a4);
    if (!(condition_is_below)) {
        result = MiUpdateUserMappings(v_rip + 2820632, v_stack_mF8, v_r15 + 5, a4);
        *(unsigned __int8 *)(v_rip + 2855673) = 1;
    }
    result = PopIssueNextState(v_rip + 2820632, v_stack_mF8, 10, a4);
loc_00B76E5C:
    result = PopCheckpointSystemSleep(18, v_stack_mF8, 10, a4);
    result = PopIssueNextState(v_rip + 2820632, v_stack_mF8, 6, a4);
    result = PopCheckpointSystemSleep(26, v_stack_mF8, 6, a4);
    result = KeRebaselineInterruptTime(26, v_stack_mF8, 6, a4);
    result = guard_dispatch_icall(26, v_stack_mF8, 6, a4);
    if (a2 == 0) goto loc_00B76EBA;
    if (((unsigned int)((unsigned int)(v_stack_m80))) == 0x40000294ULL) {
        a3 = 7;
        a2 = v_stack_mF8;
        a1 = v_rip + 2820632;
        result = PopIssueNextState(a1, a2, a3, a4);
    }
    result = PopIssueNextState(v_rip + 2820632, v_stack_mF8, 8, a4);
    if (a2 == 0) goto loc_00B76F7A;
    if (((unsigned int)((unsigned int)(v_stack_m80))) == 0x40000294ULL) {
        a1 = 27;
        result = PopCheckpointSystemSleep(a1, v_stack_mF8, 8, a4);
        a3 = 9;
        a2 = v_stack_mF8;
        a1 = v_rip + 2820632;
        result = PopIssueNextState(a1, a2, a3, a4);
        a1 = 32;
        result = PopCheckpointSystemSleep(a1, a2, a3, a4);
    }
    result = MmInvalidateDumpAddresses(*(unsigned __int64 *)(v_rip + 3756093), 19, a3, a4);
    if (*(unsigned __int64 *)(a2 + 336) != 0) {
        a2 = *(unsigned int *)(a2 + 288);
        a2 = (unsigned int)((a2) << (4));
        result = MmInvalidateDumpAddresses(*(unsigned __int64 *)(a2 + 336), a2, a3, a4);
    }
    result = PopIssueNextState(v_rip + 2820632, v_stack_mF8, 10, a4);
    if (!(condition_is_below)) {
        *(unsigned __int8 *)(v_rip + 2855408) = 0;
        result = MiUpdateUserMappings(v_rip + 2820632, v_stack_mF8, 10, a4);
        a1 = 0;
        result = MiConvertHiberPhasePages(a1, v_stack_mF8, 10, a4);
    }
    *(unsigned __int8 *)(a2 + 2) = 0;
    result = KeResumeDynamicTracing(a1, v_stack_mF8, 10, a4);
    result = PopIssueNextState(v_rip + 2820632, v_stack_mF8, 11, a4);
loc_00B76F7A:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 3082496)))) & (1)) == 0) goto loc_00B76F96;
    if ((*(unsigned __int8 *)(v_rip + 3999340)) != 0) {
        a1 = (unsigned int)((unsigned int)(v_stack_m80));
        result = DbgBreakPointWithStatus(a1, v_stack_mF8, 11, a4);
    }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 3082496)))) & (2)) != 0) {
        a4 = 0;
        v_stack_m1E8 = 0;
        a3 = 0;
        a1 = 160;
        a2 = a4 + 10;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    *(unsigned __int8 *)(v_rip + 3757880) = 0;
    if (sign_flag) goto loc_00B76FFF;
    *(unsigned int *)(v_rip + 3759379) = 0;
    *(unsigned int *)(v_rip + 3757736) = 0;
    *(unsigned int *)(v_rip + 3757733) = 0;
    *(unsigned int *)(v_rip + 3755131) = 1;
    if ((*(unsigned __int8 *)(v_rip + 3757746)) != 0) {
    }
    *(unsigned __int8 *)(v_rip + 2820632 + 44) = 0;
    result = PopIssueNextState(v_rip + 2820632, v_stack_mF8, 12, a4);
    goto loc_00B7701A;
loc_00B77017:
    v_r15 = 0;
loc_00B7701A:
    if (a2 == 0) goto loc_00B7706A;
    if (((unsigned int)((unsigned int)(v_stack_m80))) != 0xC00000C0ULL) goto loc_00B7702A;
loc_00B77028:
    goto loc_00B77028;
loc_00B7702A:
    *(unsigned int *)(v_rip + 3763751) = 0;
    *(unsigned int *)(a2 + 204) = (unsigned int)((unsigned int)(v_stack_m80));
    result = VfIsVerifierEnabled(v_rip + 2820632, v_stack_mF8, 12, a4);
    if ((unsigned int)(result) != 0) {
        a1 = 0;
        result = VfNotifyOfHibernate(a1, v_stack_mF8, 12, a4);
    }
    if ((*(unsigned __int64 *)(v_rip + 2693050)) == (v_rip + 2693057)) {
        *(unsigned __int8 *)(v_rip + 3082989) = 1;
    }
    *(unsigned int *)(a2 + 204) = 0x40000294ULL;
loc_00B7706A:
    result = KeRebaselineInterruptTime(a1, v_stack_mF8, 12, a4);
    result = KeRebaselineSystemTime(a1, v_stack_mF8, 12, a4);
    result = PopCheckpointSystemSleep(33, v_stack_mF8, 12, a4);
    *(unsigned __int8 *)(v_rip + 3755160) = 0;
    result = PopIssueNextState(v_rip + 2820632, v_stack_mF8, 13, a4);
    if (sign_flag) goto loc_00B77197;
    if ((*(unsigned int *)(v_rip + 3755205)) != 4) goto loc_00B770D2;
    if ((*(unsigned __int8 *)(v_rip + 3757520)) != 0) goto loc_00B770D2;
    a2 = 0;
    result = guard_dispatch_icall(v_stack_m1D8, a2, 13, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00B770F6;
    v_stack_m1D8 = 0;
    goto loc_00B770F6;
loc_00B770D2:
    a1 = 0;
    result = KeQueryPerformanceCounter(a1, a2, 13, a4);
    a1 = 0;
    v_stack_m1D8 = result;
    result = KeQueryPerformanceCounter(a1, a2, 13, a4);
    result = (result) - (*(unsigned __int64 *)(v_rip + 3737217));
    *(unsigned __int64 *)(v_rip + 3756946) = result;
loc_00B770F6:
    if (((*(unsigned int *)(v_rip + 4520464)) & (0x8000ULL)) != 0) {
        result = v_stack_m1D8;
        a1 = v_stack_m118;
        v_stack_m1C0 = result;
        a4 = 0x1231ULL;
        result = v_stack_m1C0;
        v_stack_m110 = 8;
        a2 = 1;
        v_stack_m118 = result;
        a3 = 0x80008000ULL;
        v_stack_m1E8 = 0x501802ULL;
        result = EtwTraceKernelEvent(a1, a2, a3, a4);
    }
    if (0 != 0) {
        result = *(unsigned __int64 *)(gs_base + (0 + 32));
        a2 = 0;
        a1 = *(unsigned int *)(result + 68);
        result = v_stack_m1D8;
        a3 = (a3) * (a1);
        a1 = *(unsigned __int64 *)(v_rip + 4520572);
        a4 = result;
        a1 = (a1) - (0);
        a1 = (a1) >> (1);
        a1 = (a1) + (0);
        a1 = (a1) >> (9);
        a4 = (a4) * (a1);
        v_stack_m1D8 = a4;
        a4 = (a4) - (result);
        *(unsigned __int64 *)(v_rip + 3756465) = a4;
    }
    result = PopIssueNextState(v_rip + 2820632, v_stack_mF8, 14, a4);
    result = PopIssueNextState(v_rip + 2820632, v_stack_mF8, 15, a4);
    result = PopIssueNextState(v_rip + 2820632, v_stack_mF8, 16, a4);
    if (v_stack_m80 < 0) goto loc_00B771EC;
    v_stack_m80 = 0;
    result = *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 2820632) + 5);
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 2820632) + 5))) != 255) {
        result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 2820632) + 5)) + 1);
        *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 2820632) + 5) = (unsigned __int8)(result);
    }
    if (0 == 0) goto loc_00B7721C;
    if (((unsigned int)((unsigned int)(v_stack_m80))) != 0x40000294ULL) goto loc_00B77239;
    if ((*(unsigned __int8 *)(v_rip + 3755360)) != 0) goto loc_00B77239;
    if ((*(unsigned __int8 *)(v_rip + 3075247)) == 0) goto loc_00B77239;
    a2 = 0;
    result = BgLibraryInitialize(*(unsigned __int64 *)(v_rip + 3075197), a2, 16, a4);
    goto loc_00B77239;
loc_00B7721C:
    if ((*(unsigned int *)(v_rip + 4520701)) != 0) {
        a1 = 2;
        a2 = (unsigned __int8)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, 16, a4);
    }
loc_00B77239:
loc_00B7723F:
    a1 = (v_stack_m40) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, 16, a4);
    v_rsp = (v_rsp) + (464);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopInvokeSystemStateHandler(int32_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint32_t v_stack_m11C;
    uint32_t v_stack_m120;
    uint64_t v_stack_m128;
    uint32_t v_stack_m13C;
    uint32_t v_stack_m140;
    uint32_t v_stack_m144;
    uint32_t v_stack_m148;
    uint8_t v_stack_m14C;
    uint32_t v_stack_m150;
    uint64_t v_stack_m158;
    uint64_t v_stack_m160;
    uint64_t v_stack_m168;
    uint64_t v_stack_m170;
    uint64_t v_stack_m178;
    uint32_t v_stack_m180;
    uint64_t v_stack_m188;
    uint64_t v_stack_m198;
    uint64_t v_stack_m1A8;
    uint16_t v_stack_m1B6;
    uint8_t v_stack_m1B7;
    uint64_t v_stack_m1B8;
    uint64_t v_stack_m1C0;
    uint16_t v_stack_m1C2;
    uint32_t v_stack_m1C6;
    uint16_t v_stack_m1C8;
    uint64_t v_stack_m1D0;
    uint64_t v_stack_m1D8;
    uint32_t v_stack_m1E8;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m58;
    uint64_t v_stack_m68;
    uint32_t v_stack_m80;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p18;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (464);
    result = (*(uint64_t *)(v_rip + 0x293CAE)) ^ (local_rsp);
    v_stack_m40 = result;
    result = 0;
    v_stack_m188 = 0;
    v_stack_m180 = 0;
    Arg2 = 0;
    v_stack_m1D0 = v_xmm0;
    local_r13 = 0;
    v_stack_m1B8 = v_xmm0;
    v_stack_m1A8 = v_xmm0;
    v_stack_m198 = v_xmm0;
    result = memset(v_stack_m178, Arg2, result + 80, a4);
    result = 0;
    v_stack_m150 = (uint32_t)((int32_t)(Arg1));
    v_stack_m48 = 0;
    v_stack_m178 = v_stack_m58;
    v_stack_m158 = v_rip + 3759106;
    v_stack_m58 = v_xmm0;
    if (((uint32_t)((int32_t)(Arg1))) == 7) goto loc_00B76B37;
    v_stack_m178 = v_rip + 3760419 + (int32_t)(Arg1) + (int32_t)(Arg1) * 2 * 8;
    if ((*(uint64_t *)(v_rip + 0x396123 + (int32_t)(Arg1) + (int32_t)(Arg1) * 2 * 8 + 0x8)) != 0) goto loc_00B76B37;
    goto loc_00B7723F;
loc_00B76B37:
    v_stack_m148 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x44FF43)));
    v_stack_m13C = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x44FF35)));
    v_stack_m140 = 1;
    if (((uint32_t)((int32_t)(Arg1) - 4)) <= 1) goto loc_00B76B96;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x395E75))) != 0) {
        Arg2 = v_stack_m178;
        Arg1 = *(uint32_t *)(Arg2 + 0x10);
        *(uint64_t *)(Arg2 + 0x10) = Arg1;
    }
    if (((uint32_t)((int32_t)(Arg1))) == 3) goto loc_00B76B7E;
    if (((uint32_t)((int32_t)(Arg1))) != 6) goto loc_00B76B96;
loc_00B76B7E:
    result = (uint32_t)(*(uint32_t *)(v_rip + 0x395E75));
    if (Arg2 != 0) {
        result = v_rip - 4966442;
        v_stack_m160 = Arg2;
        v_stack_m170 = result;
        v_stack_m168 = Arg2;
    }
    Arg2 = 0;
    result = memset(v_stack_mF8, Arg2, 160, a4);
    if (0 != 0) goto loc_00B76C84;
    Arg2 = 0;
    v_stack_m1C6 = 0;
    v_stack_m1C2 = 0;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x3AC5F4)))))) >> (6));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x3AC5F4)))) & (63));
    v_stack_m1C8 = (uint16_t)(result);
    result = (1) << ((uint8_t)(Arg1));
    v_stack_m1D0 = result;
    result = KeSetSystemGroupAffinityThread(v_stack_m1D0, Arg2, 160, a4);
    if ((*(uint32_t *)(v_rip + 0x450126)) != 0) {
        Arg2 = 2;
        Arg1 = (uint8_t)(v_cr8);
        result = KiRaiseIrqlProcessIrqlFlags(Arg1, Arg2, 160, a4);
    }
    result = KeInitializeDpc(v_stack_m1B8, v_rip + 1630, v_stack_m178, a4);
    local_rbx = 0;
    v_stack_m1B7 = 2;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x44FE5E))) == 0) goto loc_00B76C7E;
loc_00B76C2D:
    if (0 == (*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x24))) goto loc_00B76C6D;
    result = v_stack_m180;
    if (v_stack_m180 == 0) {
        result = 0x800ULL;
        result = (uint32_t)((result) + (0));
        v_stack_m1B6 = (uint16_t)(result);
    }
    a3 = 0;
    Arg2 = 0;
    result = KeInsertQueueDpc(v_stack_m1B8, Arg2, a3, a4);
    goto loc_00B76C66;
loc_00B76C64:
loc_00B76C66:
    if (((uint32_t)((uint32_t)(v_stack_m144))) == ((uint32_t)((uint32_t)(v_stack_m144)))) goto loc_00B76C64;
loc_00B76C6D:
    local_rbx = (uint32_t)((local_rbx) + (1));
    if (((uint32_t)(local_rbx)) < ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x44FE0D))))) goto loc_00B76C2D;
loc_00B76C7E:
    goto loc_00B76D02;
loc_00B76C84:
    *(uint64_t *)(v_rip + 0x2B0A2A) = v_stack_m178;
    *(uint64_t *)(v_rip + 0x2B0A19) = v_stack_m170;
    *(uint64_t *)(v_rip + 0x2B0A16) = v_stack_m168;
    *(uint64_t *)(v_rip + 0x2B0A13) = v_stack_m160;
    *(uint64_t *)(v_rip + 0x2B0A10) = v_stack_m158;
    *(uint32_t *)(v_rip + 0x2B0A0F) = (uint32_t)((uint32_t)(v_stack_m150));
    *(uint8_t *)(v_rip + 0x2B0A0A) = (uint8_t)(v_stack_m14C);
    *(uint32_t *)(v_rip + 0x2B0A05) = (uint32_t)((uint32_t)(v_stack_m148));
    *(uint32_t *)(v_rip + 0x2B0A08) = (uint32_t)((uint32_t)(v_stack_m13C));
    *(uint32_t *)(v_rip + 0x2B09FB) = (uint32_t)((uint32_t)(v_stack_m140));
    result = ExpInterlockedPushEntrySList(v_rip + 2820707, v_stack_m68, a3, a4);
loc_00B76D02:
    result = PopIssueNextState(v_rip + 2820632, v_stack_mF8, 2, a4);
    result = PopIssueNextState(v_rip + 2820632, v_stack_mF8, 3, a4);
    if ((*(uint32_t *)(v_rip + 0x395042)) != 4) goto loc_00B76D43;
    local_rdi = 0;
    local_rbx = (local_rbx) * ((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x44)));
    goto loc_00B76D54;
loc_00B76D43:
    Arg1 = 0;
    result = KeQueryPerformanceCounter(Arg1, v_stack_mF8, 3, a4);
loc_00B76D54:
    if (((*(uint32_t *)(v_rip + 0x44FDB2)) & (0x8000ULL)) != 0) {
        result = v_stack_m108;
        a4 = 0x1230ULL;
        v_stack_m128 = result;
        Arg2 = 1;
        v_stack_m108 = result;
        a3 = 0x80008000ULL;
        v_stack_m100 = *(uint64_t *)(v_rip + 0x44FE96);
        Arg1 = v_stack_m128;
        v_stack_m120 = 16;
        v_stack_m1E8 = 0x501802ULL;
        result = EtwTraceKernelEvent(Arg1, Arg2, a3, a4);
    }
    result = PopIssueNextState(v_rip + 2820632, v_stack_mF8, 4, a4);
    if (Arg2 == 0) goto loc_00B76DCB;
    *(uint8_t *)(v_rip + 0x2F0D91) = 0;
    result = VfIsVerifierEnabled(v_rip + 2820632, v_stack_mF8, 4, a4);
    if ((uint32_t)(result) != 0) {
        Arg1 = 1;
        result = VfNotifyOfHibernate(Arg1, v_stack_mF8, 4, a4);
    }
    *(uint8_t *)(v_rip + 0x394F4C) = 1;
    result = PopCheckpointSystemSleep(17, v_stack_mF8, 4, a4);
    if (v_stack_m80 < 0) goto loc_00B77017;
    *(uint8_t *)(v_rip + 0x2B0A18 + 0x2C) = 1;
    result = PopIssueNextState(v_rip + 2820632, v_stack_mF8, 12, a4);
    if (((uint32_t)((int32_t)(Arg1))) == 3) goto loc_00B76E17;
    if (((uint32_t)((int32_t)(Arg1))) != 6) {
        result = *(uint64_t *)(v_rip + 0x289D16);
        result = guard_dispatch_icall(v_rip + 2820632, v_stack_mF8, 12, a4);
    }
    local_r15 = 0;
    if (Arg2 == 0) goto loc_00B76E5C;
    result = PopIssueNextState(v_rip + 2820632, v_stack_mF8, local_r15 + 5, a4);
    result = KeSuspendDynamicTracing(v_rip + 2820632, v_stack_mF8, local_r15 + 5, a4);
    if (!(condition_is_below)) {
        result = MiUpdateUserMappings(v_rip + 2820632, v_stack_mF8, local_r15 + 5, a4);
        *(uint8_t *)(v_rip + 0x2B92F9) = 1;
    }
    result = PopIssueNextState(v_rip + 2820632, v_stack_mF8, 10, a4);
loc_00B76E5C:
    result = PopCheckpointSystemSleep(18, v_stack_mF8, 10, a4);
    result = PopIssueNextState(v_rip + 2820632, v_stack_mF8, 6, a4);
    result = PopCheckpointSystemSleep(26, v_stack_mF8, 6, a4);
    result = KeRebaselineInterruptTime(26, v_stack_mF8, 6, a4);
    result = guard_dispatch_icall(26, v_stack_mF8, 6, a4);
    if (Arg2 == 0) goto loc_00B76EBA;
    if (((uint32_t)((uint32_t)(v_stack_m80))) == 0x40000294ULL) {
        a3 = 7;
        Arg2 = v_stack_mF8;
        Arg1 = v_rip + 2820632;
        result = PopIssueNextState(Arg1, Arg2, a3, a4);
    }
    result = PopIssueNextState(v_rip + 2820632, v_stack_mF8, 8, a4);
    if (Arg2 == 0) goto loc_00B76F7A;
    if (((uint32_t)((uint32_t)(v_stack_m80))) == 0x40000294ULL) {
        Arg1 = 27;
        result = PopCheckpointSystemSleep(Arg1, v_stack_mF8, 8, a4);
        a3 = 9;
        Arg2 = v_stack_mF8;
        Arg1 = v_rip + 2820632;
        result = PopIssueNextState(Arg1, Arg2, a3, a4);
        Arg1 = 32;
        result = PopCheckpointSystemSleep(Arg1, Arg2, a3, a4);
    }
    result = MmInvalidateDumpAddresses(*(uint64_t *)(v_rip + 0x39503D), 19, a3, a4);
    if (*(uint64_t *)(Arg2 + 0x150) != 0) {
        Arg2 = *(uint32_t *)(Arg2 + 0x120);
        Arg2 = (uint32_t)((Arg2) << (4));
        result = MmInvalidateDumpAddresses(*(uint64_t *)(Arg2 + 0x150), Arg2, a3, a4);
    }
    result = PopIssueNextState(v_rip + 2820632, v_stack_mF8, 10, a4);
    if (!(condition_is_below)) {
        *(uint8_t *)(v_rip + 0x2B91F0) = 0;
        result = MiUpdateUserMappings(v_rip + 2820632, v_stack_mF8, 10, a4);
        Arg1 = 0;
        result = MiConvertHiberPhasePages(Arg1, v_stack_mF8, 10, a4);
    }
    *(uint8_t *)(Arg2 + 0x2) = 0;
    result = KeResumeDynamicTracing(Arg1, v_stack_mF8, 10, a4);
    result = PopIssueNextState(v_rip + 2820632, v_stack_mF8, 11, a4);
loc_00B76F7A:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x2F0900)))) & (1)) == 0) goto loc_00B76F96;
    if ((*(uint8_t *)(v_rip + 0x3D066C)) != 0) {
        Arg1 = (uint32_t)((uint32_t)(v_stack_m80));
        result = DbgBreakPointWithStatus(Arg1, v_stack_mF8, 11, a4);
    }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x2F0900)))) & (2)) != 0) {
        a4 = 0;
        v_stack_m1E8 = 0;
        a3 = 0;
        Arg1 = 160;
        Arg2 = a4 + 10;
        result = KeBugCheckEx(Arg1, Arg2, a3, a4);
    }
    *(uint8_t *)(v_rip + 0x395738) = 0;
    if (sign_flag) goto loc_00B76FFF;
    *(uint32_t *)(v_rip + 0x395D13) = 0;
    *(uint32_t *)(v_rip + 0x3956A8) = 0;
    *(uint32_t *)(v_rip + 0x3956A5) = 0;
    *(uint32_t *)(v_rip + 0x394C7B) = 1;
    if ((*(uint8_t *)(v_rip + 0x3956B2)) != 0) {
    }
    *(uint8_t *)(v_rip + 0x2B0A18 + 0x2C) = 0;
    result = PopIssueNextState(v_rip + 2820632, v_stack_mF8, 12, a4);
    goto loc_00B7701A;
loc_00B77017:
    local_r15 = 0;
loc_00B7701A:
    if (Arg2 == 0) goto loc_00B7706A;
    if (((uint32_t)((uint32_t)(v_stack_m80))) != 0xC00000C0ULL) goto loc_00B7702A;
loc_00B77028:
    goto loc_00B77028;
loc_00B7702A:
    *(uint32_t *)(v_rip + 0x396E27) = 0;
    *(uint32_t *)(Arg2 + 0xCC) = (uint32_t)((uint32_t)(v_stack_m80));
    result = VfIsVerifierEnabled(v_rip + 2820632, v_stack_mF8, 12, a4);
    if ((uint32_t)(result) != 0) {
        Arg1 = 0;
        result = VfNotifyOfHibernate(Arg1, v_stack_mF8, 12, a4);
    }
    if ((*(uint64_t *)(v_rip + 0x2917BA)) == (v_rip + 2693057)) {
        *(uint8_t *)(v_rip + 0x2F0AED) = 1;
    }
    *(uint32_t *)(Arg2 + 0xCC) = 0x40000294ULL;
loc_00B7706A:
    result = KeRebaselineInterruptTime(Arg1, v_stack_mF8, 12, a4);
    result = KeRebaselineSystemTime(Arg1, v_stack_mF8, 12, a4);
    result = PopCheckpointSystemSleep(33, v_stack_mF8, 12, a4);
    *(uint8_t *)(v_rip + 0x394C98) = 0;
    result = PopIssueNextState(v_rip + 2820632, v_stack_mF8, 13, a4);
    if (sign_flag) goto loc_00B77197;
    if ((*(uint32_t *)(v_rip + 0x394CC5)) != 4) goto loc_00B770D2;
    if ((*(uint8_t *)(v_rip + 0x3955D0)) != 0) goto loc_00B770D2;
    Arg2 = 0;
    result = guard_dispatch_icall(v_stack_m1D8, Arg2, 13, a4);
    if ((uint8_t)(result) != 0) goto loc_00B770F6;
    v_stack_m1D8 = 0;
    goto loc_00B770F6;
loc_00B770D2:
    Arg1 = 0;
    result = KeQueryPerformanceCounter(Arg1, Arg2, 13, a4);
    Arg1 = 0;
    v_stack_m1D8 = result;
    result = KeQueryPerformanceCounter(Arg1, Arg2, 13, a4);
    result = (result) - (*(uint64_t *)(v_rip + 0x390681));
    *(uint64_t *)(v_rip + 0x395392) = result;
loc_00B770F6:
    if (((*(uint32_t *)(v_rip + 0x44FA10)) & (0x8000ULL)) != 0) {
        result = v_stack_m1D8;
        Arg1 = v_stack_m118;
        v_stack_m1C0 = result;
        a4 = 0x1231ULL;
        result = v_stack_m1C0;
        v_stack_m110 = 8;
        Arg2 = 1;
        v_stack_m118 = result;
        a3 = 0x80008000ULL;
        v_stack_m1E8 = 0x501802ULL;
        result = EtwTraceKernelEvent(Arg1, Arg2, a3, a4);
    }
    if (0 != 0) {
        result = *(uint64_t *)(gs_base + (0 + 0x20));
        Arg2 = 0;
        Arg1 = *(uint32_t *)(result + 0x44);
        result = v_stack_m1D8;
        a3 = (a3) * (Arg1);
        Arg1 = *(uint64_t *)(v_rip + 0x44FA7C);
        a4 = result;
        Arg1 = (Arg1) - (0);
        Arg1 = (Arg1) >> (1);
        Arg1 = (Arg1) + (0);
        Arg1 = (Arg1) >> (9);
        a4 = (a4) * (Arg1);
        v_stack_m1D8 = a4;
        a4 = (a4) - (result);
        *(uint64_t *)(v_rip + 0x3951B1) = a4;
    }
    result = PopIssueNextState(v_rip + 2820632, v_stack_mF8, 14, a4);
    result = PopIssueNextState(v_rip + 2820632, v_stack_mF8, 15, a4);
    result = PopIssueNextState(v_rip + 2820632, v_stack_mF8, 16, a4);
    if (v_stack_m80 < 0) goto loc_00B771EC;
    v_stack_m80 = 0;
    result = *(uint8_t *)(*(uint64_t *)(v_rip + 0x2B0A18) + 0x5);
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(v_rip + 0x2B0A18) + 0x5))) != 255) {
        result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(v_rip + 0x2B0A18) + 0x5)) + 1);
        *(uint8_t *)(*(uint64_t *)(v_rip + 0x2B0A18) + 0x5) = (uint8_t)(result);
    }
    if (0 == 0) goto loc_00B7721C;
    if (((uint32_t)((uint32_t)(v_stack_m80))) != 0x40000294ULL) goto loc_00B77239;
    if ((*(uint8_t *)(v_rip + 0x394D60)) != 0) goto loc_00B77239;
    if ((*(uint8_t *)(v_rip + 0x2EECAF)) == 0) goto loc_00B77239;
    Arg2 = 0;
    result = BgLibraryInitialize(*(uint64_t *)(v_rip + 0x2EEC7D), Arg2, 16, a4);
    goto loc_00B77239;
loc_00B7721C:
    if ((*(uint32_t *)(v_rip + 0x44FAFD)) != 0) {
        Arg1 = 2;
        Arg2 = (uint8_t)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, 16, a4);
    }
loc_00B77239:
loc_00B7723F:
    Arg1 = (v_stack_m40) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, 16, a4);
    local_rsp = (local_rsp) + (464);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagelk&rva=0x00B76A6C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
