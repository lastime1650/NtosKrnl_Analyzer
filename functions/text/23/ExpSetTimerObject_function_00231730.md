# ExpSetTimerObject

- RVA: `0x00231730`–`0x002326F8` (길이 `4,040` bytes)
- VA: `0x0000000140231730`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00060414`
- 디코드: `862`개 명령, `4,040/4,040` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **53**; 고유 호출 대상: **32**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **22**

### Outgoing calls
- `0x00231815` → [KiAcquireSpinLockInstrumented](../20/KiAcquireSpinLockInstrumented_function_002084F0.md) (function, `0x002084F0`)
- `0x00231841` → [KiAcquireSpinLockInstrumented](../20/KiAcquireSpinLockInstrumented_function_002084F0.md) (function, `0x002084F0`)
- `0x0023186A` → [KeCancelTimer](KeCancelTimer_function_002327E0.md) (function, `0x002327E0`)
- `0x00231925` → [KiAcquireSpinLockInstrumented](../20/KiAcquireSpinLockInstrumented_function_002084F0.md) (function, `0x002084F0`)
- `0x00231960` → [KxWaitForSpinLockAndAcquire](../20/KxWaitForSpinLockAndAcquire_function_002085C0.md) (function, `0x002085C0`)
- `0x00231972` → [KxWaitForSpinLockAndAcquire](../20/KxWaitForSpinLockAndAcquire_function_002085C0.md) (function, `0x002085C0`)
- `0x00231986` → [KxReleaseSpinLock](../20/KxReleaseSpinLock_function_00206670.md) (function, `0x00206670`)
- `0x0023199B` → [KxReleaseSpinLock](../20/KxReleaseSpinLock_function_00206670.md) (function, `0x00206670`)
- `0x002319B2` → [KxWaitForSpinLockAndAcquire](../20/KxWaitForSpinLockAndAcquire_function_002085C0.md) (function, `0x002085C0`)
- `0x002319C2` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x00231C69` → [KiComputeDueTime](KiComputeDueTime_function_002332E8.md) (function, `0x002332E8`)
- `0x00231C93` → [KiInsertTimerTable](KiInsertTimerTable_function_00233400.md) (function, `0x00233400`)
- `0x00231CCE` → [KiExitDispatcher](../25/KiExitDispatcher_function_00251CF0.md) (function, `0x00251CF0`)
- `0x00231D67` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x00231D9C` → [ObpPushStackInfo](../21/ObpPushStackInfo_function_002109E4.md) (function, `0x002109E4`)
- `0x00231DDE` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00231E57` → [KiEncodeTolerableDelayValue](KiEncodeTolerableDelayValue_function_0023141C.md) (function, `0x0023141C`)
- `0x00231E77` → [KiTimerWaitTest](KiTimerWaitTest_function_002337D0.md) (function, `0x002337D0`)
- `0x00231ED6` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x00232099` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x002320A9` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0023216E` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00232179` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0023218E` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0023219F` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x002321BF` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x002321CE` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x002321EE` → [KiReleaseSpinLockInstrumented](../39/KiReleaseSpinLockInstrumented_function_00392EF0.md) (function, `0x00392EF0`)
- `0x0023220E` → [KiReleaseSpinLockInstrumented](../39/KiReleaseSpinLockInstrumented_function_00392EF0.md) (function, `0x00392EF0`)
- `0x00232235` → [KiReleaseSpinLockInstrumented](../39/KiReleaseSpinLockInstrumented_function_00392EF0.md) (function, `0x00392EF0`)
- `0x00232250` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0023225F` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00232277` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00232288` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x002322D2` → [KeAbPreAcquire](../21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x002322F7` → [ExfAcquirePushLockExclusiveEx](../20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x00232359` → [EtwTraceKernelEvent](EtwTraceKernelEvent_function_00235350.md) (function, `0x00235350`)
- `0x002323AE` → [ExpCheckTestsigningEnabled](../../page/70/ExpCheckTestsigningEnabled_function_00704864.md) (function, `0x00704864`)
- `0x002323CB` → [ExpCheckWakeTimerAccess](../../page/AB/ExpCheckWakeTimerAccess_function_00AB15FC.md) (function, `0x00AB15FC`)
- `0x002323E6` → [ObfDereferenceObjectWithTag](../2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x002323FB` → [KiTraceSetTimer](../22/KiTraceSetTimer_function_0022FB08.md) (function, `0x0022FB08`)
- `0x00232450` → [KeAcquireSpinLockAtDpcLevel](../20/KeAcquireSpinLockAtDpcLevel_function_00208430.md) (function, `0x00208430`)
- `0x00232484` → [KxReleaseSpinLock](../20/KxReleaseSpinLock_function_00206670.md) (function, `0x00206670`)
- `0x002324A3` → [KeCancelTimer](KeCancelTimer_function_002327E0.md) (function, `0x002327E0`)
- `0x002324B9` → [KeRemoveQueueApc](../3C/KeRemoveQueueApc_function_003C4820.md) (function, `0x003C4820`)
- `0x002324F6` → [ObpDeferObjectDeletion](../3A/ObpDeferObjectDeletion_function_003A2394.md) (function, `0x003A2394`)
- `0x0023252C` → [KeAbPostRelease](../2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00232539` → [KiLeaveCriticalRegionUnsafe](../25/KiLeaveCriticalRegionUnsafe_function_0025F010.md) (function, `0x0025F010`)
- `0x0023254A` → [PoDestroyReasonContext](PoDestroyReasonContext_function_00230944.md) (function, `0x00230944`)
- `0x0023255B` → [ExfTryToWakePushLock](../26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x0023259E` → [KeRemoveQueueDpcEx](../46/KeRemoveQueueDpcEx_function_0046CDC0.md) (function, `0x0046CDC0`)
- `0x002326A7` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x002326C0` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)

### Direct callers
- [NtSetTimer](NtSetTimer_function_00231190.md) at `0x002312E3`
- [NtSetTimerEx](NtSetTimerEx_function_00231480.md) at `0x0023162A`

### Static image references
- `0x0023174A` → RVA `0x00E0A740` (`.data`; read)
- `0x002317D4` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x002317FA` → RVA `0x00FC6B06` (`ALMOSTRO`; read)
- `0x00231807` → RVA `0x00F0DE58` (`.data`; read)
- `0x002318D3` → RVA `0x0049A5E0` (`ExpTimerApcRoutine`; read)
- `0x00231A65` → RVA `0x00FC7250` (`ALMOSTRO`; read)
- `0x00231A72` → RVA `0x00FC6F78` (`ALMOSTRO`; read)
- `0x00231ABE` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x00231B35` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x00231BE9` → RVA `0x00FC6B08` (`ALMOSTRO`; read)
- `0x00231BFE` → RVA `0x00FC6C48` (`ALMOSTRO`; read)
- `0x00231D84` → RVA `0x00FC5010` (`ALMOSTRO`; read)
- `0x00231F77` → RVA `0x00FC5030` (`ALMOSTRO`; read)
- `0x0023208B` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x0023229B` → RVA `0x00F0CF00` (`.data`; read)
- `0x002322CB` → RVA `0x00EFABA8` (`.data`; read)
- `0x002322DA` → RVA `0x00EFABA8` (`.data`; read/write)
- `0x00232381` → RVA `0x00EFAB98` (`.data`; read)
- `0x00232388` → RVA `0x00EFAB90` (`.data`; read)
- `0x002323A2` → RVA `0x00EFAB98` (`.data`; write)
- `0x00232562` → RVA `0x00F0CED3` (`.data`; read)
- `0x00232683` → RVA `0x00FC6E4C` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x002323AE` → [ExpCheckTestsigningEnabled](../../page/70/ExpCheckTestsigningEnabled_function_00704864.md) (`.text` → `PAGE`)
  - `0x002323CB` → [ExpCheckWakeTimerAccess](../../page/AB/ExpCheckWakeTimerAccess_function_00AB15FC.md) (`.text` → `PAGE`)
- call이 아닌 외부 분기/꼬리 이동: **9**
  - `0x0023198E` → [sub_006D73CA](../6D/Unknown_function_006D73CA.md) (`tail-transfer`)
  - `0x002319A1` → [sub_006D73CA](../6D/Unknown_function_006D73CA.md) (`tail-transfer`)
  - `0x002325B3` → [sub_006D73CA + 0xC9](../6D/Unknown_function_006D73CA.md) (`tail-transfer`)
  - `0x002325C3` → [sub_006D73CA + 0xC9](../6D/Unknown_function_006D73CA.md) (`tail-transfer`)
  - `0x002325D0` → [sub_006D73CA + 0xC9](../6D/Unknown_function_006D73CA.md) (`tail-transfer`)
  - `0x002325D9` → [sub_006D73CA + 0xC9](../6D/Unknown_function_006D73CA.md) (`tail-transfer`)
  - `0x002325E7` → [sub_006D73CA + 0xF2](../6D/Unknown_function_006D73CA.md) (`tail-transfer`)
  - `0x002325F7` → [sub_006D73CA + 0x113](../6D/Unknown_function_006D73CA.md) (`tail-transfer`)
  - `0x002326CB` → [sub_006D73CA + 0x178](../6D/Unknown_function_006D73CA.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00231730  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00231735  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
0023173A  57                              push rdi
0023173B  41 54                           push r12
0023173D  41 55                           push r13
0023173F  41 56                           push r14
00231741  41 57                           push r15
00231743  48 81 EC E0 00 00 00            sub rsp, 0xe0
0023174A  48 8B 05 EF 8F BD 00            mov rax, qword ptr [rip + 0xbd8fef]
00231751  48 33 C4                        xor rax, rsp
00231754  48 89 84 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], rax
0023175C  4D 8B F1                        mov r14, r9
0023175F  4D 8B F8                        mov r15, r8
00231762  88 54 24 32                     mov byte ptr [rsp + 0x32], dl
00231766  48 8B F9                        mov rdi, rcx
00231769  48 8B 84 24 58 01 00 00         mov rax, qword ptr [rsp + 0x158]
00231771  48 89 84 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rax
00231779  44 0F B6 A4 24 40 01 00 00      movzx r12d, byte ptr [rsp + 0x140]
00231782  33 F6                           xor esi, esi
00231784  89 74 24 44                     mov dword ptr [rsp + 0x44], esi
00231788  40 88 74 24 31                  mov byte ptr [rsp + 0x31], sil
0023178D  48 89 B4 24 80 00 00 00         mov qword ptr [rsp + 0x80], rsi
00231795  48 39 B4 24 38 01 00 00         cmp qword ptr [rsp + 0x138], rsi
0023179D  0F 85 EF 0A 00 00               jne 0x140232292
002317A3  48 89 74 24 70                  mov qword ptr [rsp + 0x70], rsi
002317A8  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
002317B1  4C 8B A8 B8 00 00 00            mov r13, qword ptr [rax + 0xb8]
002317B8  4C 89 6C 24 78                  mov qword ptr [rsp + 0x78], r13
002317BD  40 88 74 24 30                  mov byte ptr [rsp + 0x30], sil
002317C2  44 0F 20 C0                     mov rax, cr8
002317C6  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
002317CB  B9 02 00 00 00                  mov ecx, 2
002317D0  44 0F 22 C1                     mov cr8, rcx
002317D4  83 3D 45 55 D9 00 00            cmp dword ptr [rip + 0xd95545], 0
002317DB  0F 85 DB 01 00 00               jne 0x1402319bc
002317E1  40 38 74 24 32                  cmp byte ptr [rsp + 0x32], sil
002317E6  74 3A                           je 0x140231822
002317E8  41 8B 85 88 00 00 00            mov eax, dword ptr [r13 + 0x88]
002317EF  A8 10                           test al, 0x10
002317F1  74 2F                           je 0x140231822
002317F3  49 8D 8D 08 07 00 00            lea rcx, [r13 + 0x708]
002317FA  F6 05 05 53 D9 00 21            test byte ptr [rip + 0xd95305], 0x21
00231801  0F 84 9F 01 00 00               je 0x1402319a6
00231807  8B 05 4B C6 CD 00               mov eax, dword ptr [rip + 0xcdc64b]
0023180D  85 C0                           test eax, eax
0023180F  0F 85 91 01 00 00               jne 0x1402319a6
00231815  E8 D6 6C FD FF                  call 0x1402084f0
0023181A  40 B6 01                        mov sil, 1
0023181D  40 88 74 24 30                  mov byte ptr [rsp + 0x30], sil
00231822  F6 05 DD 52 D9 00 21            test byte ptr [rip + 0xd952dd], 0x21
00231829  0F 84 20 01 00 00               je 0x14023194f
0023182F  8B 05 23 C6 CD 00               mov eax, dword ptr [rip + 0xcdc623]
00231835  85 C0                           test eax, eax
00231837  0F 85 12 01 00 00               jne 0x14023194f
0023183D  48 8D 4F 40                     lea rcx, [rdi + 0x40]
00231841  E8 AA 6C FD FF                  call 0x1402084f0
00231846  48 8B 87 00 01 00 00            mov rax, qword ptr [rdi + 0x100]
0023184D  80 7C 24 31 00                  cmp byte ptr [rsp + 0x31], 0
00231852  0F 84 21 01 00 00               je 0x140231979
00231858  33 DB                           xor ebx, ebx
0023185A  F6 87 30 01 00 00 01            test byte ptr [rdi + 0x130], 1
00231861  0F 85 DE 0B 00 00               jne 0x140232445
00231867  48 8B CF                        mov rcx, rdi
0023186A  E8 71 0F 00 00                  call 0x1402327e0
0023186F  C6 87 F8 00 00 00 00            mov byte ptr [rdi + 0xf8], 0
00231876  44 8D 6B 01                     lea r13d, [rbx + 1]
0023187A  0F B6 47 04                     movzx eax, byte ptr [rdi + 4]
0023187E  88 44 24 33                     mov byte ptr [rsp + 0x33], al
00231882  44 8B 94 24 48 01 00 00         mov r10d, dword ptr [rsp + 0x148]
0023188A  44 89 97 F0 00 00 00            mov dword ptr [rdi + 0xf0], r10d
00231891  45 33 C0                        xor r8d, r8d
00231894  44 89 87 F4 00 00 00            mov dword ptr [rdi + 0xf4], r8d
0023189B  8B B4 24 50 01 00 00            mov esi, dword ptr [rsp + 0x150]
002318A2  89 B7 40 01 00 00               mov dword ptr [rdi + 0x140], esi
002318A8  4D 85 F6                        test r14, r14
002318AB  0F 84 F8 08 00 00               je 0x1402321a9
002318B1  65 48 8B 1C 25 88 01 00 00      mov rbx, qword ptr gs:[0x188]
002318BA  C6 47 48 12                     mov byte ptr [rdi + 0x48], 0x12
002318BE  C6 47 4A 58                     mov byte ptr [rdi + 0x4a], 0x58
002318C2  0F B6 83 4A 02 00 00            movzx eax, byte ptr [rbx + 0x24a]
002318C9  88 87 98 00 00 00               mov byte ptr [rdi + 0x98], al
002318CF  48 89 5F 50                     mov qword ptr [rdi + 0x50], rbx
002318D3  48 8D 05 06 8D 26 00            lea rax, [rip + 0x268d06]
002318DA  48 89 47 68                     mov qword ptr [rdi + 0x68], rax
002318DE  4C 89 47 70                     mov qword ptr [rdi + 0x70], r8
002318E2  4C 89 77 78                     mov qword ptr [rdi + 0x78], r14
002318E6  0F B6 44 24 32                  movzx eax, byte ptr [rsp + 0x32]
002318EB  88 87 99 00 00 00               mov byte ptr [rdi + 0x99], al
002318F1  48 8B 84 24 30 01 00 00         mov rax, qword ptr [rsp + 0x130]
002318F9  48 89 87 80 00 00 00            mov qword ptr [rdi + 0x80], rax
00231900  44 88 87 9A 00 00 00            mov byte ptr [rdi + 0x9a], r8b
00231907  44 88 47 49                     mov byte ptr [rdi + 0x49], r8b
0023190B  48 8D 8B F0 04 00 00            lea rcx, [rbx + 0x4f0]
00231912  F6 05 ED 51 D9 00 21            test byte ptr [rip + 0xd951ed], 0x21
00231919  74 4F                           je 0x14023196a
0023191B  8B 05 37 C5 CD 00               mov eax, dword ptr [rip + 0xcdc537]
00231921  85 C0                           test eax, eax
00231923  75 45                           jne 0x14023196a
00231925  E8 C6 6B FD FF                  call 0x1402084f0
0023192A  45 33 C0                        xor r8d, r8d
0023192D  48 8D 8F E0 00 00 00            lea rcx, [rdi + 0xe0]
00231934  48 8D 83 F8 04 00 00            lea rax, [rbx + 0x4f8]
0023193B  48 8B 50 08                     mov rdx, qword ptr [rax + 8]
0023193F  48 39 02                        cmp qword ptr [rdx], rax
00231942  0F 84 84 00 00 00               je 0x1402319cc
00231948  B9 03 00 00 00                  mov ecx, 3
0023194D  CD 29                           int 0x29
0023194F  F0 48 0F BA 6F 40 00            lock bts qword ptr [rdi + 0x40], 0
00231956  0F 83 EA FE FF FF               jae 0x140231846
0023195C  48 8D 4F 40                     lea rcx, [rdi + 0x40]
00231960  E8 5B 6C FD FF                  call 0x1402085c0
00231965  E9 DC FE FF FF                  jmp 0x140231846
0023196A  F0 48 0F BA 29 00               lock bts qword ptr [rcx], 0
00231970  73 BB                           jae 0x14023192d
00231972  E8 49 6C FD FF                  call 0x1402085c0
00231977  EB B1                           jmp 0x14023192a
00231979  48 85 C0                        test rax, rax
0023197C  0F 84 D6 FE FF FF               je 0x140231858
00231982  48 8D 4F 40                     lea rcx, [rdi + 0x40]
00231986  E8 E5 4C FD FF                  call 0x140206670
0023198B  40 84 F6                        test sil, sil
0023198E  0F 84 36 5A 4A 00               je 0x1406d73ca
00231994  49 8D 8D 08 07 00 00            lea rcx, [r13 + 0x708]
0023199B  E8 D0 4C FD FF                  call 0x140206670
002319A0  90                              nop
002319A1  E9 24 5A 4A 00                  jmp 0x1406d73ca
002319A6  F0 48 0F BA 29 00               lock bts qword ptr [rcx], 0
002319AC  0F 83 68 FE FF FF               jae 0x14023181a
002319B2  E8 09 6C FD FF                  call 0x1402085c0
002319B7  E9 5E FE FF FF                  jmp 0x14023181a
002319BC  0F B6 D1                        movzx edx, cl
002319BF  0F B6 C8                        movzx ecx, al
002319C2  E8 35 3D 2C 00                  call 0x1404f56fc
002319C7  E9 15 FE FF FF                  jmp 0x1402317e1
002319CC  48 89 01                        mov qword ptr [rcx], rax
002319CF  48 89 51 08                     mov qword ptr [rcx + 8], rdx
002319D3  48 89 0A                        mov qword ptr [rdx], rcx
002319D6  48 89 48 08                     mov qword ptr [rax + 8], rcx
002319DA  80 8F 30 01 00 00 01            or byte ptr [rdi + 0x130], 1
002319E1  F6 05 1E 51 D9 00 01            test byte ptr [rip + 0xd9511e], 1
002319E8  0F 85 2A 08 00 00               jne 0x140232218
002319EE  F0 48 83 A3 F0 04 00 00 00      lock and qword ptr [rbx + 0x4f0], 0
002319F7  4C 8D 9F A0 00 00 00            lea r11, [rdi + 0xa0]
002319FE  4C 89 5C 24 70                  mov qword ptr [rsp + 0x70], r11
00231A03  41 FF CD                        dec r13d
00231A06  45 8B D0                        mov r10d, r8d
00231A09  44 89 84 24 48 01 00 00         mov dword ptr [rsp + 0x148], r8d
00231A11  45 32 C9                        xor r9b, r9b
00231A14  49 8B 1F                        mov rbx, qword ptr [r15]
00231A17  48 89 5C 24 68                  mov qword ptr [rsp + 0x68], rbx
00231A1C  4C 8B 74 24 78                  mov r14, qword ptr [rsp + 0x78]
00231A21  49 8B 8E A0 02 00 00            mov rcx, qword ptr [r14 + 0x2a0]
00231A28  44 38 4C 24 30                  cmp byte ptr [rsp + 0x30], r9b
00231A2D  0F 85 65 04 00 00               jne 0x140231e98
00231A33  F6 87 30 01 00 00 02            test byte ptr [rdi + 0x130], 2
00231A3A  0F 85 C5 09 00 00               jne 0x140232405
00231A40  0F 57 C0                        xorps xmm0, xmm0
00231A43  33 C0                           xor eax, eax
00231A45  0F 11 84 24 B0 00 00 00         movups xmmword ptr [rsp + 0xb0], xmm0
00231A4D  48 89 84 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rax
00231A55  85 F6                           test esi, esi
00231A57  0F 85 B4 03 00 00               jne 0x140231e11
00231A5D  44 89 44 24 54                  mov dword ptr [rsp + 0x54], r8d
00231A62  4D 8B F3                        mov r14, r11
00231A65  4C 33 35 E4 57 D9 00            xor r14, qword ptr [rip + 0xd957e4]
00231A6C  49 0F CE                        bswap r14
00231A6F  4C 33 F7                        xor r14, rdi
00231A72  48 8B 05 FF 54 D9 00            mov rax, qword ptr [rip + 0xd954ff]
00231A79  8B C8                           mov ecx, eax
00231A7B  49 D3 CE                        ror r14, cl
00231A7E  4C 33 F0                        xor r14, rax
00231A81  44 0F 20 C0                     mov rax, cr8
00231A85  48 89 84 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rax
00231A8D  B9 02 00 00 00                  mov ecx, 2
00231A92  44 0F 22 C1                     mov cr8, rcx
00231A96  83 3D 83 52 D9 00 00            cmp dword ptr [rip + 0xd95283], 0
00231A9D  0F 85 2D 04 00 00               jne 0x140231ed0
00231AA3  65 4C 8B 3C 25 20 00 00 00      mov r15, qword ptr gs:[0x20]
00231AAC  4C 89 7C 24 68                  mov qword ptr [rsp + 0x68], r15
00231AB1  4C 89 84 24 98 00 00 00         mov qword ptr [rsp + 0x98], r8
00231AB9  44 89 44 24 38                  mov dword ptr [rsp + 0x38], r8d
00231ABE  48 8D 0D 3B E5 DC FF            lea rcx, [rip - 0x231ac5]
00231AC5  44 89 44 24 48                  mov dword ptr [rsp + 0x48], r8d
00231ACA  F0 0F BA 2F 07                  lock bts dword ptr [rdi], 7
00231ACF  0F 82 DB 04 00 00               jb 0x140231fb0
00231AD5  F6 47 03 C0                     test byte ptr [rdi + 3], 0xc0
00231AD9  0F 84 22 03 00 00               je 0x140231e01
00231ADF  44 0F B6 7F 02                  movzx r15d, byte ptr [rdi + 2]
00231AE4  44 89 7C 24 34                  mov dword ptr [rsp + 0x34], r15d
00231AE9  0F B7 47 38                     movzx eax, word ptr [rdi + 0x38]
00231AED  4C 8B 9C C1 40 8C FC 00         mov r11, qword ptr [rcx + rax*8 + 0xfc8c40]
00231AF5  49 81 C3 00 41 00 00            add r11, 0x4100
00231AFC  4C 89 5C 24 58                  mov qword ptr [rsp + 0x58], r11
00231B01  0F B7 4F 3A                     movzx ecx, word ptr [rdi + 0x3a]
00231B05  48 C1 E1 08                     shl rcx, 8
00231B09  49 8D 77 10                     lea rsi, [r15 + 0x10]
00231B0D  48 03 F1                        add rsi, rcx
00231B10  48 C1 E6 05                     shl rsi, 5
00231B14  49 03 F3                        add rsi, r11
00231B17  44 89 44 24 4C                  mov dword ptr [rsp + 0x4c], r8d
00231B1C  0F 1F 40 00                     nop dword ptr [rax]
00231B20  F0 48 0F BA 2E 00               lock bts qword ptr [rsi], 0
00231B26  73 26                           jae 0x140231b4e
00231B28  44 8B 7C 24 4C                  mov r15d, dword ptr [rsp + 0x4c]
00231B2D  41 FF C7                        inc r15d
00231B30  44 89 7C 24 4C                  mov dword ptr [rsp + 0x4c], r15d
00231B35  44 85 3D 70 37 D9 00            test dword ptr [rip + 0xd93770], r15d
00231B3C  0F 84 49 05 00 00               je 0x14023208b
00231B42  F3 90                           pause
00231B44  48 8B 06                        mov rax, qword ptr [rsi]
00231B47  48 85 C0                        test rax, rax
00231B4A  74 D4                           je 0x140231b20
00231B4C  EB DA                           jmp 0x140231b28
00231B4E  0F B6 47 03                     movzx eax, byte ptr [rdi + 3]
00231B52  84 C0                           test al, al
00231B54  0F 88 9B 05 00 00               js 0x1402320f5
00231B5A  44 0F B7 47 3A                  movzx r8d, word ptr [rdi + 0x3a]
00231B5F  41 8B C8                        mov ecx, r8d
00231B62  48 C1 E1 08                     shl rcx, 8
00231B66  44 8B 7C 24 34                  mov r15d, dword ptr [rsp + 0x34]
00231B6B  4D 8D 4F 10                     lea r9, [r15 + 0x10]
00231B6F  4C 03 C9                        add r9, rcx
00231B72  49 C1 E1 05                     shl r9, 5
00231B76  4C 8B 5C 24 58                  mov r11, qword ptr [rsp + 0x58]
00231B7B  4D 03 CB                        add r9, r11
00231B7E  4C 89 8C 24 88 00 00 00         mov qword ptr [rsp + 0x88], r9
00231B86  41 8B C8                        mov ecx, r8d
00231B89  48 83 F1 01                     xor rcx, 1
00231B8D  48 C1 E1 08                     shl rcx, 8
00231B91  4D 8D 57 10                     lea r10, [r15 + 0x10]
00231B95  4C 03 D1                        add r10, rcx
00231B98  49 C1 E2 05                     shl r10, 5
00231B9C  4D 03 D3                        add r10, r11
00231B9F  4C 89 94 24 90 00 00 00         mov qword ptr [rsp + 0x90], r10
00231BA7  48 8D 57 20                     lea rdx, [rdi + 0x20]
00231BAB  48 8B 0A                        mov rcx, qword ptr [rdx]
00231BAE  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
00231BB2  48 39 51 08                     cmp qword ptr [rcx + 8], rdx
00231BB6  0F 85 8C FD FF FF               jne 0x140231948
00231BBC  48 39 10                        cmp qword ptr [rax], rdx
00231BBF  0F 85 83 FD FF FF               jne 0x140231948
00231BC5  48 89 08                        mov qword ptr [rax], rcx
00231BC8  48 89 41 08                     mov qword ptr [rcx + 8], rax
00231BCC  48 3B C1                        cmp rax, rcx
00231BCF  0F 84 0E 03 00 00               je 0x140231ee3
00231BD5  F0 48 83 26 00                  lock and qword ptr [rsi], 0
00231BDA  F0 81 27 FF FF FF BF            lock and dword ptr [rdi], 0xbfffffff
00231BE1  41 B7 01                        mov r15b, 1
00231BE4  BE 01 00 00 00                  mov esi, 1
00231BE9  F7 05 15 4F D9 00 00 00 02 00   test dword ptr [rip + 0xd94f15], 0x20000
00231BF3  0F 85 15 07 00 00               jne 0x14023230e
00231BF9  4C 8B 7C 24 68                  mov r15, qword ptr [rsp + 0x68]
00231BFE  83 3D 43 50 D9 00 00            cmp dword ptr [rip + 0xd95043], 0
00231C05  75 35                           jne 0x140231c3c
00231C07  41 80 7F 20 00                  cmp byte ptr [r15 + 0x20], 0
00231C0C  0F 85 F7 01 00 00               jne 0x140231e09
00231C12  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00231C1B  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00231C22  F7 81 F4 01 00 00 00 10 00 00   test dword ptr [rcx + 0x1f4], 0x1000
00231C2C  0F 85 4F 02 00 00               jne 0x140231e81
00231C32  32 C0                           xor al, al
00231C34  84 C0                           test al, al
00231C36  0F 84 CD 01 00 00               je 0x140231e09
00231C3C  33 D2                           xor edx, edx
00231C3E  B8 3A 00 00 00                  mov eax, 0x3a
00231C43  48 8B CF                        mov rcx, rdi
00231C46  66 89 14 01                     mov word ptr [rcx + rax], dx
00231C4A  4C 89 77 30                     mov qword ptr [rdi + 0x30], r14
00231C4E  8B 84 24 48 01 00 00            mov eax, dword ptr [rsp + 0x148]
00231C55  89 47 3C                        mov dword ptr [rdi + 0x3c], eax
00231C58  4C 8D 4C 24 54                  lea r9, [rsp + 0x54]
00231C5D  44 0F B6 84 24 B1 00 00 00      movzx r8d, byte ptr [rsp + 0xb1]
00231C66  48 8B D3                        mov rdx, rbx
00231C69  E8 7A 16 00 00                  call 0x1402332e8
00231C6E  85 C0                           test eax, eax
00231C70  0F 84 F8 01 00 00               je 0x140231e6e
00231C76  33 C0                           xor eax, eax
00231C78  89 47 04                        mov dword ptr [rdi + 4], eax
00231C7B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00231C80  44 8B 4C 24 54                  mov r9d, dword ptr [rsp + 0x54]
00231C85  48 8B 5C 24 70                  mov rbx, qword ptr [rsp + 0x70]
00231C8A  4C 8B C3                        mov r8, rbx
00231C8D  48 8B D7                        mov rdx, rdi
00231C90  49 8B CF                        mov rcx, r15
00231C93  E8 68 17 00 00                  call 0x140233400
00231C98  84 C0                           test al, al
00231C9A  0F 84 CE 01 00 00               je 0x140231e6e
00231CA0  F7 05 5E 4E D9 00 00 00 02 00   test dword ptr [rip + 0xd94e5e], 0x20000
00231CAA  0F 85 42 07 00 00               jne 0x1402323f2
00231CB0  F0 81 27 7F FF FF FF            lock and dword ptr [rdi], 0xffffff7f
00231CB7  48 8B 84 24 A0 00 00 00         mov rax, qword ptr [rsp + 0xa0]
00231CBF  88 44 24 20                     mov byte ptr [rsp + 0x20], al
00231CC3  45 33 C9                        xor r9d, r9d
00231CC6  44 8B C6                        mov r8d, esi
00231CC9  33 D2                           xor edx, edx
00231CCB  49 8B CF                        mov rcx, r15
00231CCE  E8 1D 00 02 00                  call 0x140251cf0
00231CD3  48 8B 84 24 38 01 00 00         mov rax, qword ptr [rsp + 0x138]
00231CDB  4C 8B 74 24 78                  mov r14, qword ptr [rsp + 0x78]
00231CE0  4C 8D 3D 19 E3 DC FF            lea r15, [rip - 0x231ce7]
00231CE7  48 85 C0                        test rax, rax
00231CEA  74 05                           je 0x140231cf1
00231CEC  F0 0F BA 2F 09                  lock bts dword ptr [rdi], 9
00231CF1  48 8B 9F 00 01 00 00            mov rbx, qword ptr [rdi + 0x100]
00231CF8  48 89 87 00 01 00 00            mov qword ptr [rdi + 0x100], rax
00231CFF  0F B6 87 30 01 00 00            movzx eax, byte ptr [rdi + 0x130]
00231D06  41 C0 E4 02                     shl r12b, 2
00231D0A  44 32 E0                        xor r12b, al
00231D0D  41 80 E4 04                     and r12b, 4
00231D11  44 32 E0                        xor r12b, al
00231D14  44 88 A7 30 01 00 00            mov byte ptr [rdi + 0x130], r12b
00231D1B  48 8D 4F 40                     lea rcx, [rdi + 0x40]
00231D1F  F6 05 E0 4D D9 00 01            test byte ptr [rip + 0xd94de0], 1
00231D26  0F 85 AC 04 00 00               jne 0x1402321d8
00231D2C  F0 48 83 21 00                  lock and qword ptr [rcx], 0
00231D31  80 7C 24 30 00                  cmp byte ptr [rsp + 0x30], 0
00231D36  74 19                           je 0x140231d51
00231D38  49 8D 8E 08 07 00 00            lea rcx, [r14 + 0x708]
00231D3F  F6 05 C0 4D D9 00 01            test byte ptr [rip + 0xd94dc0], 1
00231D46  0F 85 AC 04 00 00               jne 0x1402321f8
00231D4C  F0 48 83 21 00                  lock and qword ptr [rcx], 0
00231D51  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
00231D56  83 3D C3 4F D9 00 00            cmp dword ptr [rip + 0xd94fc3], 0
00231D5D  74 0D                           je 0x140231d6c
00231D5F  44 0F 20 C1                     mov rcx, cr8
00231D63  40 0F B6 D6                     movzx edx, sil
00231D67  E8 2C 39 2C 00                  call 0x1404f5698
00231D6C  40 0F B6 C6                     movzx eax, sil
00231D70  44 0F 22 C0                     mov cr8, rax
00231D74  80 7C 24 31 00                  cmp byte ptr [rsp + 0x31], 0
00231D79  0F 85 E4 05 00 00               jne 0x140232363
00231D7F  45 85 ED                        test r13d, r13d
00231D82  74 3A                           je 0x140231dbe
00231D84  83 3D 85 32 D9 00 00            cmp dword ptr [rip + 0xd93285], 0
00231D8B  74 14                           je 0x140231da1
00231D8D  41 B9 44 66 6C 74               mov r9d, 0x746c6644
00231D93  45 8B C5                        mov r8d, r13d
00231D96  33 D2                           xor edx, edx
00231D98  48 8D 4F D0                     lea rcx, [rdi - 0x30]
00231D9C  E8 43 EC FD FF                  call 0x1402109e4
00231DA1  41 8B C5                        mov eax, r13d
00231DA4  F7 D8                           neg eax
00231DA6  48 63 C8                        movsxd rcx, eax
00231DA9  F0 48 0F C1 4F D0               lock xadd qword ptr [rdi - 0x30], rcx
00231DAF  49 63 C5                        movsxd rax, r13d
00231DB2  48 2B C8                        sub rcx, rax
00231DB5  48 85 C9                        test rcx, rcx
00231DB8  0F 8E 1E 07 00 00               jle 0x1402324dc
00231DBE  48 8B 94 24 A8 00 00 00         mov rdx, qword ptr [rsp + 0xa8]
00231DC6  48 85 D2                        test rdx, rdx
00231DC9  0F 85 F7 08 00 00               jne 0x1402326c6
00231DCF  8B 44 24 44                     mov eax, dword ptr [rsp + 0x44]
00231DD3  48 8B 8C 24 D8 00 00 00         mov rcx, qword ptr [rsp + 0xd8]
00231DDB  48 33 CC                        xor rcx, rsp
00231DDE  E8 5D A8 47 00                  call 0x1406ac640
00231DE3  4C 8D 9C 24 E0 00 00 00         lea r11, [rsp + 0xe0]
00231DEB  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
00231DEF  49 8B 73 48                     mov rsi, qword ptr [r11 + 0x48]
00231DF3  49 8B E3                        mov rsp, r11
00231DF6  41 5F                           pop r15
00231DF8  41 5E                           pop r14
00231DFA  41 5D                           pop r13
00231DFC  41 5C                           pop r12
00231DFE  5F                              pop rdi
00231DFF  C3                              ret
00231E00  CC                              int3
00231E01  45 32 FF                        xor r15b, r15b
00231E04  E9 DB FD FF FF                  jmp 0x140231be4
00231E09  0F B7 D6                        movzx edx, si
00231E0C  E9 2D FE FF FF                  jmp 0x140231c3e
00231E11  48 69 CE 10 27 00 00            imul rcx, rsi, 0x2710
00231E18  48 81 F9 00 7C 92 00            cmp rcx, 0x927c00
00231E1F  76 36                           jbe 0x140231e57
00231E21  48 81 C1 00 84 6D FF            add rcx, -0x927c00
00231E28  48 85 DB                        test rbx, rbx
00231E2B  0F 88 82 02 00 00               js 0x1402320b3
00231E31  4C 8D 04 19                     lea r8, [rcx + rbx]
00231E35  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
00231E3F  4C 3B C3                        cmp r8, rbx
00231E42  4C 0F 4C C0                     cmovl r8, rax
00231E46  45 85 D2                        test r10d, r10d
00231E49  0F 85 AD 07 00 00               jne 0x1402325fc
00231E4F  B9 00 7C 92 00                  mov ecx, 0x927c00
00231E54  49 8B D8                        mov rbx, r8
00231E57  E8 C0 F5 FF FF                  call 0x14023141c
00231E5C  C0 E0 02                        shl al, 2
00231E5F  88 84 24 B1 00 00 00            mov byte ptr [rsp + 0xb1], al
00231E66  45 33 C0                        xor r8d, r8d
00231E69  E9 EF FB FF FF                  jmp 0x140231a5d
00231E6E  45 33 C0                        xor r8d, r8d
00231E71  48 8B D7                        mov rdx, rdi
00231E74  49 8B CF                        mov rcx, r15
00231E77  E8 54 19 00 00                  call 0x1402337d0
00231E7C  E9 36 FE FF FF                  jmp 0x140231cb7
00231E81  F7 81 FC 05 00 00 00 00 00 04   test dword ptr [rcx + 0x5fc], 0x4000000
00231E8B  0F 85 A1 FD FF FF               jne 0x140231c32
00231E91  B0 01                           mov al, 1
00231E93  E9 9C FD FF FF                  jmp 0x140231c34
00231E98  4C 8D 87 18 01 00 00            lea r8, [rdi + 0x118]
00231E9F  49 83 38 00                     cmp qword ptr [r8], 0
00231EA3  0F 84 07 07 00 00               je 0x1402325b0
00231EA9  F0 41 FF 86 F8 06 00 00         lock inc dword ptr [r14 + 0x6f8]
00231EB1  41 8B 86 88 00 00 00            mov eax, dword ptr [r14 + 0x88]
00231EB8  A8 10                           test al, 0x10
00231EBA  74 0C                           je 0x140231ec8
00231EBC  41 8B 4E 44                     mov ecx, dword ptr [r14 + 0x44]
00231EC0  85 C9                           test ecx, ecx
00231EC2  0F 85 16 07 00 00               jne 0x1402325de
00231EC8  45 33 C0                        xor r8d, r8d
00231ECB  E9 63 FB FF FF                  jmp 0x140231a33
00231ED0  0F B6 D1                        movzx edx, cl
00231ED3  0F B6 C8                        movzx ecx, al
00231ED6  E8 21 38 2C 00                  call 0x1404f56fc
00231EDB  45 33 C0                        xor r8d, r8d
00231EDE  E9 C0 FB FF FF                  jmp 0x140231aa3
00231EE3  41 C7 41 1C FF FF FF FF         mov dword ptr [r9 + 0x1c], 0xffffffff
00231EEB  66 45 85 C0                     test r8w, r8w
00231EEF  0F 85 EF 00 00 00               jne 0x140231fe4
00231EF5  49 81 C7 10 01 00 00            add r15, 0x110
00231EFC  49 C1 E7 05                     shl r15, 5
00231F00  4D 03 FB                        add r15, r11
00231F03  C7 44 24 3C 00 00 00 00         mov dword ptr [rsp + 0x3c], 0
00231F0B  0F 1F 44 00 00                  nop dword ptr [rax + rax]
00231F10  F0 49 0F BA 2F 00               lock bts qword ptr [r15], 0
00231F16  73 22                           jae 0x140231f3a
00231F18  8B 44 24 3C                     mov eax, dword ptr [rsp + 0x3c]
00231F1C  FF C0                           inc eax
00231F1E  89 44 24 3C                     mov dword ptr [rsp + 0x3c], eax
00231F22  85 05 84 33 D9 00               test dword ptr [rip + 0xd93384], eax
00231F28  0F 84 52 02 00 00               je 0x140232180
00231F2E  F3 90                           pause
00231F30  49 8B 07                        mov rax, qword ptr [r15]
00231F33  48 85 C0                        test rax, rax
00231F36  74 D8                           je 0x140231f10
00231F38  EB DE                           jmp 0x140231f18
00231F3A  4C 8B 5C 24 58                  mov r11, qword ptr [rsp + 0x58]
00231F3F  4C 8B 94 24 90 00 00 00         mov r10, qword ptr [rsp + 0x90]
00231F47  4C 8B 8C 24 88 00 00 00         mov r9, qword ptr [rsp + 0x88]
00231F4F  41 83 79 1C FF                  cmp dword ptr [r9 + 0x1c], -1
00231F54  75 48                           jne 0x140231f9e
00231F56  41 83 7A 1C FF                  cmp dword ptr [r10 + 0x1c], -1
00231F5B  75 41                           jne 0x140231f9e
00231F5D  41 0F B6 83 D0 BF FF FF         movzx eax, byte ptr [r11 - 0x4030]
00231F65  48 03 C0                        add rax, rax
00231F68  48 8D 0D 91 E0 DC FF            lea rcx, [rip - 0x231f6f]
00231F6F  48 8B 8C C1 28 85 FC 00         mov rcx, qword ptr [rcx + rax*8 + 0xfc8528]
00231F77  83 3D B2 30 D9 00 00            cmp dword ptr [rip + 0xd930b2], 0
00231F7E  0F 84 4D 01 00 00               je 0x1402320d1
00231F84  44 8B 44 24 34                  mov r8d, dword ptr [rsp + 0x34]
00231F89  41 8B D0                        mov edx, r8d
00231F8C  83 E2 3F                        and edx, 0x3f
00231F8F  41 C1 E8 06                     shr r8d, 6
00231F93  4A 8D 0C C1                     lea rcx, [rcx + r8*8]
00231F97  8B C2                           mov eax, edx
00231F99  F0 48 0F B3 01                  lock btr qword ptr [rcx], rax
00231F9E  F0 49 83 27 00                  lock and qword ptr [r15], 0
00231FA3  E9 2D FC FF FF                  jmp 0x140231bd5
00231FA8  0F 1F 84 00 00 00 00 00         nop dword ptr [rax + rax]
00231FB0  8B 74 24 48                     mov esi, dword ptr [rsp + 0x48]
00231FB4  FF C6                           inc esi
00231FB6  89 74 24 48                     mov dword ptr [rsp + 0x48], esi
00231FBA  85 35 EC 32 D9 00               test dword ptr [rip + 0xd932ec], esi
00231FC0  0F 84 EB 01 00 00               je 0x1402321b1
00231FC6  F3 90                           pause
00231FC8  8B 07                           mov eax, dword ptr [rdi]
00231FCA  84 C0                           test al, al
00231FCC  78 E2                           js 0x140231fb0
00231FCE  F0 0F BA 2F 07                  lock bts dword ptr [rdi], 7
00231FD3  72 DB                           jb 0x140231fb0
00231FD5  48 8D 0D 24 E0 DC FF            lea rcx, [rip - 0x231fdc]
00231FDC  45 33 C0                        xor r8d, r8d
00231FDF  E9 F1 FA FF FF                  jmp 0x140231ad5
00231FE4  49 83 C7 10                     add r15, 0x10
00231FE8  49 C1 E7 05                     shl r15, 5
00231FEC  4D 03 FB                        add r15, r11
00231FEF  49 8B C7                        mov rax, r15
00231FF2  F0 49 0F BA 2F 00               lock bts qword ptr [r15], 0
00231FF8  73 05                           jae 0x140231fff
00231FFA  F3 90                           pause
00231FFC  45 33 FF                        xor r15d, r15d
00231FFF  4D 85 FF                        test r15, r15
00232002  0F 85 47 FF FF FF               jne 0x140231f4f
00232008  F0 4C 21 3E                     lock and qword ptr [rsi], r15
0023200C  4C 8B F8                        mov r15, rax
0023200F  C7 44 24 50 00 00 00 00         mov dword ptr [rsp + 0x50], 0
00232017  F0 49 0F BA 2F 00               lock bts qword ptr [r15], 0
0023201D  73 22                           jae 0x140232041
0023201F  8B 74 24 50                     mov esi, dword ptr [rsp + 0x50]
00232023  FF C6                           inc esi
00232025  89 74 24 50                     mov dword ptr [rsp + 0x50], esi
00232029  85 35 7D 32 D9 00               test dword ptr [rip + 0xd9327d], esi
0023202F  0F 84 0D 02 00 00               je 0x140232242
00232035  F3 90                           pause
00232037  49 8B 07                        mov rax, qword ptr [r15]
0023203A  48 85 C0                        test rax, rax
0023203D  74 D8                           je 0x140232017
0023203F  EB DE                           jmp 0x14023201f
00232041  8B 74 24 34                     mov esi, dword ptr [rsp + 0x34]
00232045  48 81 C6 10 01 00 00            add rsi, 0x110
0023204C  48 C1 E6 05                     shl rsi, 5
00232050  48 03 74 24 58                  add rsi, qword ptr [rsp + 0x58]
00232055  C7 44 24 40 00 00 00 00         mov dword ptr [rsp + 0x40], 0
0023205D  F0 48 0F BA 2E 00               lock bts qword ptr [rsi], 0
00232063  0F 83 D1 FE FF FF               jae 0x140231f3a
00232069  8B 44 24 40                     mov eax, dword ptr [rsp + 0x40]
0023206D  FF C0                           inc eax
0023206F  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00232073  85 05 33 32 D9 00               test dword ptr [rip + 0xd93233], eax
00232079  0F 84 EA 01 00 00               je 0x140232269
0023207F  F3 90                           pause
00232081  48 8B 06                        mov rax, qword ptr [rsi]
00232084  48 85 C0                        test rax, rax
00232087  74 D4                           je 0x14023205d
00232089  EB DE                           jmp 0x140232069
0023208B  8B 05 27 4A D9 00               mov eax, dword ptr [rip + 0xd94a27]
00232091  A8 40                           test al, 0x40
00232093  0F 84 A9 FA FF FF               je 0x140231b42
00232099  E8 F2 D3 0D 00                  call 0x14030f490
0023209E  84 C0                           test al, al
002320A0  0F 84 9C FA FF FF               je 0x140231b42
002320A6  41 8B CF                        mov ecx, r15d
002320A9  E8 B2 D3 0D 00                  call 0x14030f460
002320AE  E9 91 FA FF FF                  jmp 0x140231b44
002320B3  4C 8B C3                        mov r8, rbx
002320B6  4C 2B C1                        sub r8, rcx
002320B9  4C 3B C3                        cmp r8, rbx
002320BC  0F 8E 84 FD FF FF               jle 0x140231e46
002320C2  49 B8 00 00 00 00 00 00 00 80   movabs r8, 0x8000000000000000
002320CC  E9 75 FD FF FF                  jmp 0x140231e46
002320D1  41 0F B6 93 D1 BF FF FF         movzx edx, byte ptr [r11 - 0x402f]
002320D9  8B 44 24 34                     mov eax, dword ptr [rsp + 0x34]
002320DD  48 C1 E0 06                     shl rax, 6
002320E1  48 03 C8                        add rcx, rax
002320E4  8B C2                           mov eax, edx
002320E6  F0 48 0F B3 01                  lock btr qword ptr [rcx], rax
002320EB  F0 49 83 27 00                  lock and qword ptr [r15], 0
002320F0  E9 E0 FA FF FF                  jmp 0x140231bd5
002320F5  F0 48 83 26 00                  lock and qword ptr [rsi], 0
002320FA  0F B6 47 03                     movzx eax, byte ptr [rdi + 3]
002320FE  83 E0 3F                        and eax, 0x3f
00232101  45 33 C0                        xor r8d, r8d
00232104  41 8B C8                        mov ecx, r8d
00232107  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
0023210C  48 87 0C C2                     xchg qword ptr [rdx + rax*8], rcx
00232110  48 85 C9                        test rcx, rcx
00232113  0F 85 B4 03 00 00               jne 0x1402324cd
00232119  F0 81 27 7F FF FF FF            lock and dword ptr [rdi], 0xffffff7f
00232120  44 89 44 24 38                  mov dword ptr [rsp + 0x38], r8d
00232125  0F B6 47 03                     movzx eax, byte ptr [rdi + 3]
00232129  84 C0                           test al, al
0023212B  48 8D 0D CE DE DC FF            lea rcx, [rip - 0x232132]
00232132  0F 89 8D F9 FF FF               jns 0x140231ac5
00232138  0F 1F 84 00 00 00 00 00         nop dword ptr [rax + rax]
00232140  8B 74 24 38                     mov esi, dword ptr [rsp + 0x38]
00232144  FF C6                           inc esi
00232146  89 74 24 38                     mov dword ptr [rsp + 0x38], esi
0023214A  85 35 5C 31 D9 00               test dword ptr [rip + 0xd9315c], esi
00232150  74 12                           je 0x140232164
00232152  F3 90                           pause
00232154  0F B6 47 03                     movzx eax, byte ptr [rdi + 3]
00232158  84 C0                           test al, al
0023215A  78 E4                           js 0x140232140
0023215C  45 33 C0                        xor r8d, r8d
0023215F  E9 5A F9 FF FF                  jmp 0x140231abe
00232164  8B 05 4E 49 D9 00               mov eax, dword ptr [rip + 0xd9494e]
0023216A  A8 40                           test al, 0x40
0023216C  74 E4                           je 0x140232152
0023216E  E8 1D D3 0D 00                  call 0x14030f490
00232173  84 C0                           test al, al
00232175  74 DB                           je 0x140232152
00232177  8B CE                           mov ecx, esi
00232179  E8 E2 D2 0D 00                  call 0x14030f460
0023217E  EB D4                           jmp 0x140232154
00232180  8B 05 32 49 D9 00               mov eax, dword ptr [rip + 0xd94932]
00232186  A8 40                           test al, 0x40
00232188  0F 84 A0 FD FF FF               je 0x140231f2e
0023218E  E8 FD D2 0D 00                  call 0x14030f490
00232193  84 C0                           test al, al
00232195  0F 84 93 FD FF FF               je 0x140231f2e
0023219B  8B 4C 24 3C                     mov ecx, dword ptr [rsp + 0x3c]
0023219F  E8 BC D2 0D 00                  call 0x14030f460
002321A4  E9 87 FD FF FF                  jmp 0x140231f30
002321A9  4D 8B D8                        mov r11, r8
002321AC  E9 60 F8 FF FF                  jmp 0x140231a11
002321B1  8B 05 01 49 D9 00               mov eax, dword ptr [rip + 0xd94901]
002321B7  A8 40                           test al, 0x40
002321B9  0F 84 07 FE FF FF               je 0x140231fc6
002321BF  E8 CC D2 0D 00                  call 0x14030f490
002321C4  84 C0                           test al, al
002321C6  0F 84 FA FD FF FF               je 0x140231fc6
002321CC  8B CE                           mov ecx, esi
002321CE  E8 8D D2 0D 00                  call 0x14030f460
002321D3  E9 F0 FD FF FF                  jmp 0x140231fc8
002321D8  8B 05 7A BC CD 00               mov eax, dword ptr [rip + 0xcdbc7a]
002321DE  85 C0                           test eax, eax
002321E0  0F 85 46 FB FF FF               jne 0x140231d2c
002321E6  48 8B 94 24 08 01 00 00         mov rdx, qword ptr [rsp + 0x108]
002321EE  E8 FD 0C 16 00                  call 0x140392ef0
002321F3  E9 39 FB FF FF                  jmp 0x140231d31
002321F8  8B 05 5A BC CD 00               mov eax, dword ptr [rip + 0xcdbc5a]
002321FE  85 C0                           test eax, eax
00232200  0F 85 46 FB FF FF               jne 0x140231d4c
00232206  48 8B 94 24 08 01 00 00         mov rdx, qword ptr [rsp + 0x108]
0023220E  E8 DD 0C 16 00                  call 0x140392ef0
00232213  E9 39 FB FF FF                  jmp 0x140231d51
00232218  8B 05 3A BC CD 00               mov eax, dword ptr [rip + 0xcdbc3a]
0023221E  85 C0                           test eax, eax
00232220  0F 85 C8 F7 FF FF               jne 0x1402319ee
00232226  48 8B 94 24 08 01 00 00         mov rdx, qword ptr [rsp + 0x108]
0023222E  48 8D 8B F0 04 00 00            lea rcx, [rbx + 0x4f0]
00232235  E8 B6 0C 16 00                  call 0x140392ef0
0023223A  45 33 C0                        xor r8d, r8d
0023223D  E9 B5 F7 FF FF                  jmp 0x1402319f7
00232242  8B 05 70 48 D9 00               mov eax, dword ptr [rip + 0xd94870]
00232248  A8 40                           test al, 0x40
0023224A  0F 84 E5 FD FF FF               je 0x140232035
00232250  E8 3B D2 0D 00                  call 0x14030f490
00232255  84 C0                           test al, al
00232257  0F 84 D8 FD FF FF               je 0x140232035
0023225D  8B CE                           mov ecx, esi
0023225F  E8 FC D1 0D 00                  call 0x14030f460
00232264  E9 CE FD FF FF                  jmp 0x140232037
00232269  8B 05 49 48 D9 00               mov eax, dword ptr [rip + 0xd94849]
0023226F  A8 40                           test al, 0x40
00232271  0F 84 08 FE FF FF               je 0x14023207f
00232277  E8 14 D2 0D 00                  call 0x14030f490
0023227C  84 C0                           test al, al
0023227E  0F 84 FB FD FF FF               je 0x14023207f
00232284  8B 4C 24 40                     mov ecx, dword ptr [rsp + 0x40]
00232288  E8 D3 D1 0D 00                  call 0x14030f460
0023228D  E9 EF FD FF FF                  jmp 0x140232081
00232292  45 84 E4                        test r12b, r12b
00232295  0F 85 13 01 00 00               jne 0x1402323ae
0023229B  83 3D 5E AC CD 00 02            cmp dword ptr [rip + 0xcdac5e], 2
002322A2  0F 8C BA 02 00 00               jl 0x140232562
002322A8  C6 44 24 31 01                  mov byte ptr [rsp + 0x31], 1
002322AD  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
002322B6  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
002322BE  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
002322C5  90                              nop
002322C6  45 33 C0                        xor r8d, r8d
002322C9  33 D2                           xor edx, edx
002322CB  48 8D 0D D6 88 CC 00            lea rcx, [rip + 0xcc88d6]
002322D2  E8 59 DF FD FF                  call 0x140210230
002322D7  48 8B D8                        mov rbx, rax
002322DA  F0 48 0F BA 2D C4 88 CC 00 00   lock bts qword ptr [rip + 0xcc88c4], 0
002322E4  73 16                           jae 0x1402322fc
002322E6  4C 8D 05 BB 88 CC 00            lea r8, [rip + 0xcc88bb]
002322ED  48 8B D0                        mov rdx, rax
002322F0  48 8D 0D B1 88 CC 00            lea rcx, [rip + 0xcc88b1]
002322F7  E8 94 D9 FD FF                  call 0x14020fc90
002322FC  48 85 DB                        test rbx, rbx
002322FF  0F 84 9E F4 FF FF               je 0x1402317a3
00232305  C6 43 0A 01                     mov byte ptr [rbx + 0xa], 1
00232309  E9 95 F4 FF FF                  jmp 0x1402317a3
0023230E  45 84 FF                        test r15b, r15b
00232311  0F 84 E2 F8 FF FF               je 0x140231bf9
00232317  48 89 BC 24 98 00 00 00         mov qword ptr [rsp + 0x98], rdi
0023231F  48 8D 84 24 98 00 00 00         lea rax, [rsp + 0x98]
00232327  48 89 84 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], rax
0023232F  48 C7 84 24 D0 00 00 00 08 00 00 00  mov qword ptr [rsp + 0xd0], 8
0023233B  41 B9 55 0F 00 00               mov r9d, 0xf55
00232341  C7 44 24 20 02 06 00 00         mov dword ptr [rsp + 0x20], 0x602
00232349  41 B8 00 00 02 40               mov r8d, 0x40020000
0023234F  8B D6                           mov edx, esi
00232351  48 8D 8C 24 C8 00 00 00         lea rcx, [rsp + 0xc8]
00232359  E8 F2 2F 00 00                  call 0x140235350
0023235E  E9 96 F8 FF FF                  jmp 0x140231bf9
00232363  48 85 DB                        test rbx, rbx
00232366  0F 85 94 01 00 00               jne 0x140232500
0023236C  48 39 9C 24 38 01 00 00         cmp qword ptr [rsp + 0x138], rbx
00232374  0F 84 95 01 00 00               je 0x14023250f
0023237A  48 8D 8F 08 01 00 00            lea rcx, [rdi + 0x108]
00232381  48 8B 05 10 88 CC 00            mov rax, qword ptr [rip + 0xcc8810]
00232388  48 8D 15 01 88 CC 00            lea rdx, [rip + 0xcc8801]
0023238F  48 39 10                        cmp qword ptr [rax], rdx
00232392  0F 85 B0 F5 FF FF               jne 0x140231948
00232398  48 89 11                        mov qword ptr [rcx], rdx
0023239B  48 89 41 08                     mov qword ptr [rcx + 8], rax
0023239F  48 89 08                        mov qword ptr [rax], rcx
002323A2  48 89 0D EF 87 CC 00            mov qword ptr [rip + 0xcc87ef], rcx
002323A9  E9 61 01 00 00                  jmp 0x14023250f
002323AE  E8 B1 24 4D 00                  call 0x140704864
002323B3  84 C0                           test al, al
002323B5  0F 85 E0 FE FF FF               jne 0x14023229b
002323BB  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
002323C4  0F B6 88 32 02 00 00            movzx ecx, byte ptr [rax + 0x232]
002323CB  E8 2C F2 87 00                  call 0x140ab15fc
002323D0  8B D8                           mov ebx, eax
002323D2  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
002323D6  85 C0                           test eax, eax
002323D8  0F 84 BD FE FF FF               je 0x14023229b
002323DE  BA 44 66 6C 74                  mov edx, 0x746c6644
002323E3  48 8B CF                        mov rcx, rdi
002323E6  E8 F5 54 0C 00                  call 0x1402f78e0
002323EB  8B C3                           mov eax, ebx
002323ED  E9 E1 F9 FF FF                  jmp 0x140231dd3
002323F2  45 33 C0                        xor r8d, r8d
002323F5  48 8B D3                        mov rdx, rbx
002323F8  48 8B CF                        mov rcx, rdi
002323FB  E8 08 D7 FF FF                  call 0x14022fb08
00232400  E9 B2 F8 FF FF                  jmp 0x140231cb7
00232405  48 89 9F 38 01 00 00            mov qword ptr [rdi + 0x138], rbx
0023240C  83 7C 24 6C 00                  cmp dword ptr [rsp + 0x6c], 0
00232411  0F 8D 1A 02 00 00               jge 0x140232631
00232417  48 8B D7                        mov rdx, rdi
0023241A  B8 F8 00 00 00                  mov eax, 0xf8
0023241F  48 83 BC 24 38 01 00 00 00      cmp qword ptr [rsp + 0x138], 0
00232428  B1 03                           mov cl, 3
0023242A  75 02                           jne 0x14023242e
0023242C  B1 02                           mov cl, 2
0023242E  88 0C 02                        mov byte ptr [rdx + rax], cl
00232431  48 8B 84 24 38 01 00 00         mov rax, qword ptr [rsp + 0x138]
00232439  4C 8D 3D C0 DB DC FF            lea r15, [rip - 0x232440]
00232440  E9 AC F8 FF FF                  jmp 0x140231cf1
00232445  48 8B 77 50                     mov rsi, qword ptr [rdi + 0x50]
00232449  48 8D 8E F0 04 00 00            lea rcx, [rsi + 0x4f0]
00232450  E8 DB 5F FD FF                  call 0x140208430
00232455  48 8D 87 E0 00 00 00            lea rax, [rdi + 0xe0]
0023245C  4C 8B 00                        mov r8, qword ptr [rax]
0023245F  48 8B 50 08                     mov rdx, qword ptr [rax + 8]
00232463  49 39 40 08                     cmp qword ptr [r8 + 8], rax
00232467  0F 85 DB F4 FF FF               jne 0x140231948
0023246D  48 39 02                        cmp qword ptr [rdx], rax
00232470  0F 85 D2 F4 FF FF               jne 0x140231948
00232476  4C 89 02                        mov qword ptr [rdx], r8
00232479  49 89 50 08                     mov qword ptr [r8 + 8], rdx
0023247D  48 8D 8E F0 04 00 00            lea rcx, [rsi + 0x4f0]
00232484  E8 E7 41 FD FF                  call 0x140206670
00232489  0F B6 87 30 01 00 00            movzx eax, byte ptr [rdi + 0x130]
00232490  24 FE                           and al, 0xfe
00232492  88 87 30 01 00 00               mov byte ptr [rdi + 0x130], al
00232498  A8 02                           test al, 2
0023249A  0F 85 E4 00 00 00               jne 0x140232584
002324A0  48 8B CF                        mov rcx, rdi
002324A3  E8 38 03 00 00                  call 0x1402327e0
002324A8  84 C0                           test al, al
002324AA  0F 84 E5 00 00 00               je 0x140232595
002324B0  BB 01 00 00 00                  mov ebx, 1
002324B5  48 8D 4F 48                     lea rcx, [rdi + 0x48]
002324B9  E8 62 23 19 00                  call 0x1403c4820
002324BE  84 C0                           test al, al
002324C0  0F 84 A9 F3 FF FF               je 0x14023186f
002324C6  FF C3                           inc ebx
002324C8  E9 A2 F3 FF FF                  jmp 0x14023186f
002324CD  F0 81 27 FF FF FF 00            lock and dword ptr [rdi], 0xffffff
002324D4  41 B7 01                        mov r15b, 1
002324D7  E9 08 F7 FF FF                  jmp 0x140231be4
002324DC  4C 8B 47 D8                     mov r8, qword ptr [rdi - 0x28]
002324E0  4D 85 C0                        test r8, r8
002324E3  0F 85 88 01 00 00               jne 0x140232671
002324E9  48 85 C9                        test rcx, rcx
002324EC  0F 88 BB 01 00 00               js 0x1402326ad
002324F2  48 8D 4F D0                     lea rcx, [rdi - 0x30]
002324F6  E8 99 FE 16 00                  call 0x1403a2394
002324FB  E9 BE F8 FF FF                  jmp 0x140231dbe
00232500  48 83 BC 24 38 01 00 00 00      cmp qword ptr [rsp + 0x138], 0
00232509  0F 84 2E 01 00 00               je 0x14023263d
0023250F  48 C7 C0 FF FF FF FF            mov rax, 0xffffffffffffffff
00232516  F0 48 0F C1 05 89 86 CC 00      lock xadd qword ptr [rip + 0xcc8689], rax
0023251F  24 06                           and al, 6
00232521  3C 02                           cmp al, 2
00232523  74 2F                           je 0x140232554
00232525  48 8D 0D 7C 86 CC 00            lea rcx, [rip + 0xcc867c]
0023252C  E8 CF F0 0A 00                  call 0x1402e1600
00232531  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
00232539  E8 D2 CA 02 00                  call 0x14025f010
0023253E  48 85 DB                        test rbx, rbx
00232541  0F 84 38 F8 FF FF               je 0x140231d7f
00232547  48 8B CB                        mov rcx, rbx
0023254A  E8 F5 E3 FF FF                  call 0x140230944
0023254F  E9 2B F8 FF FF                  jmp 0x140231d7f
00232554  48 8D 0D 4D 86 CC 00            lea rcx, [rip + 0xcc864d]
0023255B  E8 70 38 03 00                  call 0x140265dd0
00232560  EB C3                           jmp 0x140232525
00232562  40 38 35 6A A9 CD 00            cmp byte ptr [rip + 0xcda96a], sil
00232569  0F 85 39 FD FF FF               jne 0x1402322a8
0023256F  C7 44 24 44 25 00 00 40         mov dword ptr [rsp + 0x44], 0x40000025
00232577  48 89 B4 24 38 01 00 00         mov qword ptr [rsp + 0x138], rsi
0023257F  E9 1F F2 FF FF                  jmp 0x1402317a3
00232584  38 9F F8 00 00 00               cmp byte ptr [rdi + 0xf8], bl
0023258A  0F 85 20 FF FF FF               jne 0x1402324b0
00232590  E9 0B FF FF FF                  jmp 0x1402324a0
00232595  48 8D 8F A0 00 00 00            lea rcx, [rdi + 0xa0]
0023259C  33 D2                           xor edx, edx
0023259E  E8 1D A8 23 00                  call 0x14046cdc0
002325A3  84 C0                           test al, al
002325A5  0F 84 0A FF FF FF               je 0x1402324b5
002325AB  E9 00 FF FF FF                  jmp 0x1402324b0
002325B0  48 85 C9                        test rcx, rcx
002325B3  0F 84 DA 4E 4A 00               je 0x1406d7493
002325B9  F7 81 10 06 00 00 00 00 04 00   test dword ptr [rcx + 0x610], 0x40000
002325C3  0F 84 CA 4E 4A 00               je 0x1406d7493
002325C9  83 B9 28 04 00 00 00            cmp dword ptr [rcx + 0x428], 0
002325D0  0F 84 BD 4E 4A 00               je 0x1406d7493
002325D6  41 B1 01                        mov r9b, 1
002325D9  E9 B5 4E 4A 00                  jmp 0x1406d7493
002325DE  49 8B 1F                        mov rbx, qword ptr [r15]
002325E1  48 8B C3                        mov rax, rbx
002325E4  48 85 DB                        test rbx, rbx
002325E7  0F 89 CF 4E 4A 00               jns 0x1406d74bc
002325ED  48 2B C1                        sub rax, rcx
002325F0  48 3B C3                        cmp rax, rbx
002325F3  48 0F 4E D8                     cmovle rbx, rax
002325F7  E9 E1 4E 4A 00                  jmp 0x1406d74dd
002325FC  48 B8 4B 59 86 38 D6 C5 6D 34   movabs rax, 0x346dc5d63886594b
00232606  48 F7 E9                        imul rcx
00232609  48 C1 FA 0B                     sar rdx, 0xb
0023260D  48 8B CA                        mov rcx, rdx
00232610  48 C1 E9 3F                     shr rcx, 0x3f
00232614  48 03 CA                        add rcx, rdx
00232617  41 03 CA                        add ecx, r10d
0023261A  B8 FF FF FF FF                  mov eax, 0xffffffff
0023261F  41 3B CA                        cmp ecx, r10d
00232622  0F 43 C1                        cmovae eax, ecx
00232625  89 84 24 48 01 00 00            mov dword ptr [rsp + 0x148], eax
0023262C  E9 1E F8 FF FF                  jmp 0x140231e4f
00232631  C6 87 F8 00 00 00 01            mov byte ptr [rdi + 0xf8], 1
00232638  E9 F4 FD FF FF                  jmp 0x140232431
0023263D  48 8D 87 08 01 00 00            lea rax, [rdi + 0x108]
00232644  48 8B 10                        mov rdx, qword ptr [rax]
00232647  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
0023264B  48 39 42 08                     cmp qword ptr [rdx + 8], rax
0023264F  0F 85 F3 F2 FF FF               jne 0x140231948
00232655  48 39 01                        cmp qword ptr [rcx], rax
00232658  0F 85 EA F2 FF FF               jne 0x140231948
0023265E  48 89 11                        mov qword ptr [rcx], rdx
00232661  48 89 4A 08                     mov qword ptr [rdx + 8], rcx
00232665  48 C7 00 00 00 00 00            mov qword ptr [rax], 0
0023266C  E9 9E FE FF FF                  jmp 0x14023250f
00232671  48 8D 47 D0                     lea rax, [rdi - 0x30]
00232675  48 C1 E8 08                     shr rax, 8
00232679  0F B6 D0                        movzx edx, al
0023267C  0F B6 47 E8                     movzx eax, byte ptr [rdi - 0x18]
00232680  48 33 D0                        xor rdx, rax
00232683  0F B6 05 C2 47 D9 00            movzx eax, byte ptr [rip + 0xd947c2]
0023268A  48 33 D0                        xor rdx, rax
0023268D  4C 89 44 24 20                  mov qword ptr [rsp + 0x20], r8
00232692  41 B9 06 00 00 00               mov r9d, 6
00232698  4C 8B C7                        mov r8, rdi
0023269B  49 8B 94 D7 00 78 FC 00         mov rdx, qword ptr [r15 + rdx*8 + 0xfc7800]
002326A3  41 8D 49 12                     lea ecx, [r9 + 0x12]
002326A7  E8 B4 AF 2C 00                  call 0x1404fd660
002326AC  CC                              int3
002326AD  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
002326B2  41 B9 05 00 00 00               mov r9d, 5
002326B8  4C 8B C7                        mov r8, rdi
002326BB  33 D2                           xor edx, edx
002326BD  8D 4A 18                        lea ecx, [rdx + 0x18]
002326C0  E8 9B AF 2C 00                  call 0x1404fd660
002326C5  CC                              int3
002326C6  80 7C 24 32 00                  cmp byte ptr [rsp + 0x32], 0
002326CB  0F 84 71 4E 4A 00               je 0x1406d7542
002326D1  48 B9 00 00 FF FF FF 7F 00 00   movabs rcx, 0x7fffffff0000
002326DB  48 3B D1                        cmp rdx, rcx
002326DE  48 0F 42 CA                     cmovb rcx, rdx
002326E2  0F B6 01                        movzx eax, byte ptr [rcx]
002326E5  88 01                           mov byte ptr [rcx], al
002326E7  0F B6 44 24 33                  movzx eax, byte ptr [rsp + 0x33]
002326EC  88 02                           mov byte ptr [rdx], al
002326EE  E9 DC F6 FF FF                  jmp 0x140231dcf
002326F3  E9 D7 F6 FF FF                  jmp 0x140231dcf
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpSetTimerObject(__int64 a1, unsigned __int8 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, unsigned __int8 a7, unsigned int a8, unsigned int a9, __int64 a10)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m28;
    unsigned __int8 v_stack_m2F;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int8 v_stack_m57;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned int v_stack_m74;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned int v_stack_m9C;
    unsigned __int64 v_stack_mA0;
    unsigned int v_stack_mA4;
    unsigned __int64 v_stack_mA8;
    unsigned int v_stack_mAC;
    unsigned __int8 v_stack_mAD;
    unsigned __int8 v_stack_mAE;
    unsigned __int8 v_stack_mAF;
    unsigned __int64 v_stack_mB0;
    unsigned int v_stack_mB4;
    unsigned int v_stack_mBC;
    unsigned int v_stack_mC0;
    unsigned int v_stack_mC4;
    unsigned int v_stack_mD0;
    unsigned int v_stack_mD4;
    unsigned __int8 v_stack_mD5;
    unsigned __int8 v_stack_mD6;
    unsigned __int8 v_stack_mD7;
    unsigned __int8 v_stack_mD8;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned int v_stack_p40;
    unsigned __int64 v_stack_p58;
    unsigned int v_stack_p68;

    v_stack_p10 = v_rbx;
    v_stack_p20 = v_rsi;
    v_rsp = (v_rsp) - (224);
    result = (*(unsigned __int64 *)(v_rip + 12423151)) ^ (v_rsp);
    v_stack_m30 = result;
    v_stack_mD6 = a2;
    v_stack_m60 = a10;
    v_rsi = 0;
    v_stack_mC4 = 0;
    v_stack_mD7 = 0;
    v_stack_m88 = 0;
    if (a6 != 0) goto loc_00232292;
loc_002317A3:
    v_stack_m98 = 0;
    v_stack_m90 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184);
    v_stack_mD8 = 0;
    v_stack_mA8 = v_cr8;
    if ((*(unsigned int *)(v_rip + 14243141)) != 0) goto loc_002319BC;
loc_002317E1:
    if (v_stack_mD6 == 0) goto loc_00231822;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 136)))) & (16)) == 0) goto loc_00231822;
    if (((*(unsigned __int8 *)(v_rip + 14242565)) & (33)) == 0) goto loc_002319A6;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13485643))) != 0) goto loc_002319A6;
    result = KiAcquireSpinLockInstrumented(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1800, a2, a3, a4);
loc_0023181A:
    v_stack_mD8 = 1;
loc_00231822:
    if (((*(unsigned __int8 *)(v_rip + 14242525)) & (33)) == 0) goto loc_0023194F;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13485603))) != 0) goto loc_0023194F;
    result = KiAcquireSpinLockInstrumented(a1 + 64, a2, a3, a4);
loc_00231846:
    if (v_stack_mD7 == 0) goto loc_00231979;
loc_00231858:
    v_rbx = 0;
    if (((*(unsigned __int8 *)(a1 + 304)) & (1)) != 0) goto loc_00232445;
    result = KeCancelTimer(a1, a2, a3, a4);
loc_0023186F:
    *(unsigned __int8 *)(a1 + 248) = 0;
    v_stack_mD5 = (unsigned __int8)(*(unsigned __int8 *)(a1 + 4));
    *(unsigned int *)(a1 + 240) = (unsigned int)((unsigned int)(a8));
    a3 = 0;
    *(unsigned int *)(a1 + 244) = 0;
    *(unsigned int *)(a1 + 320) = (unsigned int)((unsigned int)(a9));
    if (a4 == 0) goto loc_002321A9;
    *(unsigned __int8 *)(a1 + 72) = 18;
    *(unsigned __int8 *)(a1 + 74) = 88;
    *(unsigned __int8 *)(a1 + 152) = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 586));
    *(unsigned __int64 *)(a1 + 80) = *(unsigned __int64 *)(gs_base + (0 + 392));
    *(unsigned __int64 *)(a1 + 104) = v_rip + 2526470;
    *(unsigned __int64 *)(a1 + 112) = 0;
    *(unsigned __int64 *)(a1 + 120) = a4;
    *(unsigned __int8 *)(a1 + 153) = (unsigned __int8)(v_stack_mD6);
    *(unsigned __int64 *)(a1 + 128) = a5;
    *(unsigned __int8 *)(a1 + 154) = 0;
    *(unsigned __int8 *)(a1 + 73) = 0;
    if (((*(unsigned __int8 *)(v_rip + 14242285)) & (33)) == 0) goto loc_0023196A;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13485367))) != 0) goto loc_0023196A;
    result = KiAcquireSpinLockInstrumented(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1264, a2, a3, a4);
loc_0023192A:
    a3 = 0;
loc_0023192D:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1272 + 8))) == (*(unsigned __int64 *)(gs_base + (0 + 392)) + 1272)) goto loc_002319CC;
loc_00231948:
loc_0023194F:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1272 + 8))) >= (*(unsigned __int64 *)(gs_base + (0 + 392)) + 1272)) goto loc_00231846;
    result = KxWaitForSpinLockAndAcquire(a1 + 64, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1272 + 8), a3, a4);
    goto loc_00231846;
loc_0023196A:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1272 + 8))) >= (*(unsigned __int64 *)(gs_base + (0 + 392)) + 1272)) goto loc_0023192D;
    result = KxWaitForSpinLockAndAcquire(a1 + 64, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1272 + 8), a3, a4);
    goto loc_0023192A;
loc_00231979:
    if (result == 0) goto loc_00231858;
    result = KxReleaseSpinLock(a1 + 64, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1272 + 8), a3, a4);
    result = KxReleaseSpinLock(v_rbx + 1 + 1800, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1272 + 8), a3, a4);
loc_002319A6:
    if (condition_is_above_or_equal) goto loc_0023181A;
    result = KxWaitForSpinLockAndAcquire(v_rbx + 1 + 1800, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1272 + 8), a3, a4);
    goto loc_0023181A;
loc_002319BC:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(result), (unsigned __int8)(v_rbx + 1 + 1800), a3, a4);
    goto loc_002317E1;
loc_002319CC:
    *(unsigned __int64 *)((unsigned __int8)(result)) = result;
    *(unsigned __int64 *)((unsigned __int8)(result) + 8) = (unsigned __int8)(v_rbx + 1 + 1800);
    *(unsigned __int64 *)((unsigned __int8)(v_rbx + 1 + 1800)) = (unsigned __int8)(result);
    *(unsigned __int64 *)(result + 8) = (unsigned __int8)(result);
    if (((*(unsigned __int8 *)(v_rip + 14242078)) & (1)) != 0) goto loc_00232218;
loc_002319EE:
loc_002319F7:
    v_stack_m98 = a1 + 160;
    v_r13 = (unsigned int)((v_rbx + 1) - 1);
    v_stack_p40 = 0;
loc_00231A11:
    a4 = 0;
    v_stack_mA0 = *(unsigned __int64 *)(a3);
    if (v_stack_mD8 != 0) goto loc_00231E98;
loc_00231A33:
    if (((*(unsigned __int8 *)(a1 + 304)) & (2)) != 0) goto loc_00232405;
    result = 0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = 0;
    if ((unsigned int)((unsigned int)(a9)) != 0) goto loc_00231E11;
loc_00231A5D:
    v_stack_mB4 = 0;
    v_r14 = (a1 + 160) ^ (*(unsigned __int64 *)(v_rip + 14243812));
    v_r14 = (v_r14) ^ (a1);
    v_r14 = (v_r14) ^ (*(unsigned __int64 *)(v_rip + 14243071));
    v_stack_m68 = 2;
    if ((*(unsigned int *)(v_rip + 14242435)) != 0) goto loc_00231ED0;
loc_00231AA3:
    v_stack_mA0 = *(unsigned __int64 *)(gs_base + (0 + 32));
    v_stack_m70 = 0;
    v_stack_mD0 = 0;
loc_00231ABE:
loc_00231AC5:
    v_stack_mC0 = 0;
    if ((*(unsigned int *)(v_rip + 14242435)) < 0) goto loc_00231FB0;
loc_00231AD5:
    if (((*(unsigned __int8 *)(a1 + 3)) & (192)) == 0) goto loc_00231E01;
    v_stack_mD4 = (unsigned int)(*(unsigned __int8 *)(a1 + 2));
    v_r11 = (*(unsigned __int64 *)(v_rip - 2300613 + *(unsigned __int16 *)(a1 + 56) * 8 + 16550976)) + (0x4100ULL);
    v_stack_mB0 = v_r11;
    a1 = (*(unsigned __int16 *)(a1 + 58)) << (8);
    v_rsi = (*(unsigned __int8 *)(a1 + 2) + 16) + (a1);
    v_rsi = (v_rsi) << (5);
    v_rsi = (v_rsi) + (v_r11);
    v_stack_mBC = 0;
loc_00231B20:
    if (condition_is_above_or_equal) goto loc_00231B4E;
loc_00231B28:
    v_r15 = (unsigned int)(((unsigned int)(v_stack_mBC)) + 1);
    v_stack_mBC = (unsigned int)(v_r15);
    if (((*(unsigned int *)(v_rip + 14235504)) & ((unsigned int)(v_r15))) == 0) goto loc_0023208B;
loc_00231B42:
loc_00231B44:
    if (*(unsigned __int64 *)(v_rsi) == 0) goto loc_00231B20;
    goto loc_00231B28;
loc_00231B4E:
    if (sign_flag) goto loc_002320F5;
    a1 = ((unsigned int)((unsigned int)(*(unsigned __int16 *)(a1 + 58)))) << (8);
    a4 = ((unsigned int)(v_stack_mD4) + 16) + (a1);
    a4 = (a4) << (5);
    a4 = (a4) + (v_stack_mB0);
    v_stack_m80 = a4;
    a1 = ((unsigned int)((unsigned int)(*(unsigned __int16 *)(a1 + 58)))) ^ (1);
    a1 = (a1) << (8);
    v_r10 = ((unsigned int)(v_stack_mD4) + 16) + (a1);
    v_r10 = (v_r10) << (5);
    v_r10 = (v_r10) + (v_stack_mB0);
    v_stack_m78 = v_r10;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 8)) != (a1 + 32)) goto loc_00231948;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32 + 8))) != (a1 + 32)) goto loc_00231948;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32 + 8)) = *(unsigned __int64 *)(a1 + 32);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 8) = *(unsigned __int64 *)(a1 + 32 + 8);
    if ((*(unsigned __int64 *)(a1 + 32 + 8)) == (*(unsigned __int64 *)(a1 + 32))) goto loc_00231EE3;
loc_00231BD5:
loc_00231BE4:
    if (((*(unsigned int *)(v_rip + 14241557)) & (0x20000ULL)) != 0) goto loc_0023230E;
loc_00231BF9:
    if ((*(unsigned int *)(v_rip + 14241859)) != 0) goto loc_00231C3C;
    if ((*(unsigned __int8 *)(v_stack_mA0 + 32)) != 0) goto loc_00231E09;
    if (((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 500)) & (0x1000ULL)) != 0) goto loc_00231E81;
loc_00231C32:
    result = 0;
loc_00231C34:
    if (0 == 0) goto loc_00231E09;
loc_00231C3C:
    a2 = 0;
loc_00231C3E:
    *(unsigned __int16 *)(a1 + 58 * 1) = 0;
    *(unsigned __int64 *)(a1 + 48) = v_r14;
    *(unsigned int *)(a1 + 60) = (unsigned int)((unsigned int)(a8));
    result = KiComputeDueTime(a1, *(unsigned __int64 *)(a3), v_stack_m57, v_stack_mB4);
    if ((unsigned int)(result) == 0) goto loc_00231E6E;
    result = 0;
    *(unsigned int *)(a1 + 4) = 0;
    v_stack_mE8 = 0;
    result = KiInsertTimerTable(v_stack_mA0, a1, v_stack_m98, (unsigned int)(v_stack_mB4));
    if ((unsigned __int8)(result) == 0) goto loc_00231E6E;
    if (((*(unsigned int *)(v_rip + 14241374)) & (0x20000ULL)) != 0) goto loc_002323F2;
loc_00231CB7:
    v_stack_mE8 = (unsigned __int8)(v_stack_m68);
    a4 = 0;
    a2 = 0;
    result = KiExitDispatcher(v_stack_mA0, a2, 1, a4);
    if (a6 != 0) {
    }
    *(unsigned __int64 *)(a1 + 256) = a6;
    v_r12 = (unsigned __int8)((a7) << (2));
    v_r12 = (unsigned __int8)((v_r12) ^ ((unsigned __int8)(*(unsigned __int8 *)(a1 + 304))));
    v_r12 = (unsigned __int8)((v_r12) & (4));
    v_r12 = (unsigned __int8)((v_r12) ^ ((unsigned __int8)(*(unsigned __int8 *)(a1 + 304))));
    *(unsigned __int8 *)(a1 + 304) = (unsigned __int8)(v_r12);
    if (((*(unsigned __int8 *)(v_rip + 14241248)) & (1)) != 0) goto loc_002321D8;
loc_00231D2C:
loc_00231D31:
    if (v_stack_mD8 == 0) goto loc_00231D51;
    if (((*(unsigned __int8 *)(v_rip + 14241216)) & (1)) != 0) goto loc_002321F8;
loc_00231D4C:
loc_00231D51:
    result = *(unsigned __int8 *)(a1 + 304);
    if ((*(unsigned int *)(v_rip + 14241731)) != 0) {
        a1 = 2;
        a2 = (unsigned __int8)(v_stack_mA8);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, 1, a4);
    }
    if (v_stack_mD7 != 0) goto loc_00232363;
loc_00231D7F:
    if ((unsigned int)(v_r13) == 0) goto loc_00231DBE;
    result = (unsigned __int8)(v_stack_mA8);
    if ((*(unsigned int *)(v_rip + 14234245)) != 0) {
        a4 = 0x746C6644ULL;
        a3 = (unsigned int)(v_r13);
        a2 = 0;
        a1 = a1 - 48;
        result = ObpPushStackInfo(a1, a2, a3, a4);
    }
    result = (unsigned int)(-((unsigned int)((unsigned int)(v_r13))));
    a1 = ((int)((unsigned int)(result))) - ((int)((unsigned int)(v_r13)));
    if (condition_is_less_or_equal) goto loc_002324DC;
loc_00231DBE:
    if (v_stack_m60 != 0) goto loc_002326C6;
loc_00231DCF:
loc_00231DD3:
    a1 = (v_stack_m30) ^ (v_rsp);
    result = _security_check_cookie(a1, v_stack_m60, a3, a4);
    return result;
loc_00231E01:
    v_r15 = 0;
    goto loc_00231BE4;
loc_00231E09:
    goto loc_00231C3E;
loc_00231E11:
    a1 = (a1) * (*(unsigned __int64 *)(v_stack_m28 + 72));
    if (a1 <= 0x927C00ULL) goto loc_00231E57;
    a1 = (a1) + (0xFFFFFFFFFF6D8400ULL);
    if (sign_flag) goto loc_002320B3;
    a3 = a1 + *(unsigned __int64 *)(v_stack_m28 + 56) * 1;
    if ((a1 + *(unsigned __int64 *)(v_stack_m28 + 56) * 1) < (*(unsigned __int64 *)(v_stack_m28 + 56))) { a3 = result; }
loc_00231E46:
    if ((unsigned int)(v_r10) != 0) goto loc_002325FC;
loc_00231E4F:
loc_00231E57:
    result = KiEncodeTolerableDelayValue((unsigned int)(0x927C00ULL), (unsigned __int16)(*(unsigned __int64 *)(v_stack_m28 + 72)), a3, a4);
    result = (unsigned __int8)((result) << (2));
    v_stack_m2F = (unsigned __int8)(result);
    a3 = 0;
    goto loc_00231A5D;
loc_00231E6E:
    a3 = 0;
    result = KiTimerWaitTest(0, a1, a3, a4);
    goto loc_00231CB7;
loc_00231E81:
    if (((*(unsigned int *)(0 + 1532)) & (0x4000000ULL)) != 0) goto loc_00231C32;
    goto loc_00231C34;
loc_00231E98:
    if ((*(unsigned __int64 *)(a1 + 280)) == 0) goto loc_002325B0;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m90 + 136)))) & (16)) == 0) goto loc_00231EC8;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m90 + 68))) != 0) goto loc_002325DE;
loc_00231EC8:
    a3 = 0;
    goto loc_00231A33;
loc_00231ED0:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m90 + 136))), (unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m90 + 68))), a3, a4);
    a3 = 0;
    goto loc_00231AA3;
loc_00231EE3:
    *(unsigned int *)(a4 + 28) = 0xFFFFFFFFULL;
    if (0 != 0) goto loc_00231FE4;
    v_r15 = (v_r15) + (272);
    v_r15 = (v_r15) << (5);
    v_r15 = (v_r15) + (v_stack_m28);
    v_stack_mA4 = 0;
loc_00231F10:
    if (condition_is_above_or_equal) goto loc_00231F3A;
loc_00231F18:
    result = (unsigned int)(((unsigned int)(v_stack_mA4)) + 1);
    v_stack_mA4 = (unsigned int)(result);
    if (((*(unsigned int *)(v_rip + 14234500)) & ((unsigned int)(result))) == 0) goto loc_00232180;
loc_00231F2E:
loc_00231F30:
    if (*(unsigned __int64 *)(v_r15) == 0) goto loc_00231F10;
    goto loc_00231F18;
loc_00231F3A:
loc_00231F4F:
    if ((*(unsigned int *)(v_stack_m58 + 28)) != -1) goto loc_00231F9E;
    if ((*(unsigned int *)(v_stack_m50 + 28)) != -1) goto loc_00231F9E;
    result = (*(unsigned __int8 *)(v_stack_m88 - 16432)) + (*(unsigned __int8 *)(v_stack_m88 - 16432));
    if ((*(unsigned int *)(v_rip + 14233778)) == 0) goto loc_002320D1;
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_mAC)))) & (63));
    a3 = (unsigned int)(((unsigned int)(v_stack_mAC)) >> (6));
loc_00231F9E:
    goto loc_00231BD5;
loc_00231FB0:
    v_rsi = (unsigned int)(((unsigned int)(v_stack_m98)) + 1);
    v_stack_m98 = (unsigned int)(v_rsi);
    if (((*(unsigned int *)(v_rip + 14234348)) & ((unsigned int)(v_rsi))) == 0) goto loc_002321B1;
loc_00231FC6:
loc_00231FC8:
    if (sign_flag) goto loc_00231FB0;
    if (condition_is_below) goto loc_00231FB0;
    a3 = 0;
    goto loc_00231AD5;
loc_00231FE4:
    v_r15 = (v_r15) + (16);
    v_r15 = (v_r15) << (5);
    v_r15 = (v_r15) + (v_stack_m88);
    if (!(condition_is_above_or_equal)) {
        v_r15 = 0;
    }
    if (0 != 0) goto loc_00231F4F;
    v_stack_m90 = 0;
loc_00232017:
    if (condition_is_above_or_equal) goto loc_00232041;
loc_0023201F:
    v_rsi = (unsigned int)(((unsigned int)(v_stack_m90)) + 1);
    v_stack_m90 = (unsigned int)(v_rsi);
    if (((*(unsigned int *)(v_rip + 14234237)) & ((unsigned int)(v_rsi))) == 0) goto loc_00232242;
loc_00232035:
loc_00232037:
    if (*(unsigned __int64 *)(0) == 0) goto loc_00232017;
    goto loc_0023201F;
loc_00232041:
    v_rsi = ((unsigned int)(v_stack_mAC)) + (272);
    v_rsi = (v_rsi) << (5);
    v_rsi = (v_rsi) + (v_stack_m88);
    v_stack_mA0 = 0;
loc_0023205D:
    if (condition_is_above_or_equal) goto loc_00231F3A;
loc_00232069:
    result = (unsigned int)(((unsigned int)(v_stack_mA0)) + 1);
    v_stack_mA0 = (unsigned int)(result);
    if (((*(unsigned int *)(v_rip + 14234163)) & ((unsigned int)(result))) == 0) goto loc_00232269;
loc_0023207F:
loc_00232081:
    if (*(unsigned __int64 *)(v_rsi) == 0) goto loc_0023205D;
    goto loc_00232069;
loc_0023208B:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14240295)))) & (64)) == 0) goto loc_00231B42;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_rip - 2301916, a2, a3, v_stack_m58);
    if ((unsigned __int8)(result) == 0) goto loc_00231B42;
    result = HvlNotifyLongSpinWait(0, a2, a3, v_stack_m58);
    goto loc_00231B44;
loc_002320B3:
    a3 = (0) - (0);
    if (a3 <= a3) goto loc_00231E46;
    goto loc_00231E46;
loc_002320D1:
    result = ((unsigned int)(v_stack_mAC)) << (6);
    a1 = (0) + (result);
    goto loc_00231BD5;
loc_002320F5:
    result = (unsigned int)((*(unsigned __int8 *)(a1 + 3)) & (63));
    a3 = 0;
    if (0 != 0) goto loc_002324CD;
    v_stack_mA8 = 0;
    if (!sign_flag) goto loc_00231AC5;
loc_00232140:
    v_rsi = (unsigned int)(((unsigned int)(v_stack_mA8)) + 1);
    v_stack_mA8 = (unsigned int)(v_rsi);
    if (((*(unsigned int *)(v_rip + 14233948)) & ((unsigned int)(v_rsi))) == 0) goto loc_00232164;
loc_00232152:
loc_00232154:
    if (sign_flag) goto loc_00232140;
    a3 = 0;
    goto loc_00231ABE;
loc_00232164:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14240078)))) & (64)) == 0) goto loc_00232152;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_rip - 2302258, v_stack_m88, a3, v_stack_m58);
    if ((unsigned __int8)(result) == 0) goto loc_00232152;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rsi)), v_stack_m88, a3, v_stack_m58);
    goto loc_00232154;
loc_00232180:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14240050)))) & (64)) == 0) goto loc_00231F2E;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)((unsigned int)(v_rsi)), v_stack_m88, a3, v_stack_m58);
    if ((unsigned __int8)(result) == 0) goto loc_00231F2E;
    result = HvlNotifyLongSpinWait((unsigned int)(v_stack_mA4), v_stack_m88, a3, v_stack_m58);
    goto loc_00231F30;
loc_002321A9:
    goto loc_00231A11;
loc_002321B1:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14240001)))) & (64)) == 0) goto loc_00231FC6;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)(v_stack_mA4), v_stack_m88, a3, v_stack_m58);
    if ((unsigned __int8)(result) == 0) goto loc_00231FC6;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rsi)), v_stack_m88, a3, v_stack_m58);
    goto loc_00231FC8;
loc_002321D8:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13483130))) != 0) goto loc_00231D2C;
    result = KiReleaseSpinLockInstrumented((unsigned int)((unsigned int)(v_rsi)), v_stack_p28, a3, v_stack_m58);
    goto loc_00231D31;
loc_002321F8:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13483098))) != 0) goto loc_00231D4C;
    result = KiReleaseSpinLockInstrumented((unsigned int)((unsigned int)(v_rsi)), v_stack_p28, a3, v_stack_m58);
    goto loc_00231D51;
loc_00232218:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13483066))) != 0) goto loc_002319EE;
    result = KiReleaseSpinLockInstrumented(a3 + 1264, v_stack_p28, a3, v_stack_m58);
    a3 = 0;
    goto loc_002319F7;
loc_00232242:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14239856)))) & (64)) == 0) goto loc_00232035;
    result = KiCheckVpBackingLongSpinWaitHypercall(a3 + 1264, v_stack_p28, a3, v_stack_m58);
    if ((unsigned __int8)(result) == 0) goto loc_00232035;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rsi)), v_stack_p28, a3, v_stack_m58);
    goto loc_00232037;
loc_00232269:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14239817)))) & (64)) == 0) goto loc_0023207F;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)((unsigned int)(v_rsi)), v_stack_p28, a3, v_stack_m58);
    if ((unsigned __int8)(result) == 0) goto loc_0023207F;
    result = HvlNotifyLongSpinWait((unsigned int)(v_stack_mA0), v_stack_p28, a3, v_stack_m58);
    goto loc_00232081;
loc_00232292:
    if ((unsigned __int8)(v_r12) != 0) goto loc_002323AE;
loc_0023229B:
    if ((*(unsigned int *)(v_rip + 13479006)) < 2) goto loc_00232562;
loc_002322A8:
    v_stack_mAF = 1;
    v_stack_m60 = *(unsigned __int64 *)(gs_base + (0 + 392));
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_rip + 13404374, a2, a3, v_stack_m58);
    if (!(condition_is_above_or_equal)) {
        a3 = v_rip + 13404347;
        a2 = result;
        a1 = v_rip + 13404337;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, v_stack_m58);
    }
    if (result == 0) goto loc_002317A3;
    *(unsigned __int8 *)(result + 10) = 1;
    goto loc_002317A3;
loc_0023230E:
    if (0 == 0) goto loc_00231BF9;
    v_stack_m48 = a1;
    v_stack_m18 = v_stack_m48;
    v_stack_m10 = 8;
    v_stack_mC0 = 0x602ULL;
    result = EtwTraceKernelEvent(v_stack_m18, (unsigned int)((unsigned int)(v_rsi)), (unsigned int)(0x40020000ULL), (unsigned int)(0xF55ULL));
    goto loc_00231BF9;
loc_00232363:
    if (result != 0) goto loc_00232500;
    if (a6 == result) goto loc_0023250F;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 13404176))) != (v_rip + 13404161)) goto loc_00231948;
    *(unsigned __int64 *)(a1 + 264) = v_rip + 13404161;
    *(unsigned __int64 *)(a1 + 264 + 8) = *(unsigned __int64 *)(v_rip + 13404176);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 13404176)) = a1 + 264;
    *(unsigned __int64 *)(v_rip + 13404143) = a1 + 264;
    goto loc_0023250F;
loc_002323AE:
    result = ExpCheckTestsigningEnabled(a1 + 264, v_rip + 13404161, (unsigned int)(0x40020000ULL), (unsigned int)(0xF55ULL));
    if ((unsigned __int8)(result) != 0) goto loc_0023229B;
    result = ExpCheckWakeTimerAccess(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562), v_rip + 13404161, (unsigned int)(0x40020000ULL), (unsigned int)(0xF55ULL));
    v_stack_m9C = (unsigned int)(result);
    if ((unsigned int)(result) == 0) goto loc_0023229B;
    result = ObfDereferenceObjectWithTag(a1, (unsigned int)(0x746C6644ULL), (unsigned int)(0x40020000ULL), (unsigned int)(0xF55ULL));
    goto loc_00231DD3;
loc_002323F2:
    a3 = 0;
    result = KiTraceSetTimer(a1, (unsigned int)((unsigned int)(result)), a3, (unsigned int)(0xF55ULL));
    goto loc_00231CB7;
loc_00232405:
    *(unsigned __int64 *)(a1 + 312) = (unsigned int)((unsigned int)(result));
    if (v_stack_m74 >= 0) goto loc_00232631;
    if (a6 == 0) {
        a1 = 2;
    }
    *(unsigned __int8 *)(a1 + 248 * 1) = (unsigned __int8)(a1);
loc_00232431:
    goto loc_00231CF1;
loc_00232445:
    result = KeAcquireSpinLockAtDpcLevel(*(unsigned __int64 *)(a1 + 80) + 1264, a1, a3, (unsigned int)(0xF55ULL));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 224) + 8)) != (a1 + 224)) goto loc_00231948;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 224 + 8))) != (a1 + 224)) goto loc_00231948;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 224 + 8)) = *(unsigned __int64 *)(a1 + 224);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 224) + 8) = *(unsigned __int64 *)(a1 + 224 + 8);
    result = KxReleaseSpinLock(*(unsigned __int64 *)(a1 + 80) + 1264, *(unsigned __int64 *)(a1 + 224 + 8), *(unsigned __int64 *)(a1 + 224), (unsigned int)(0xF55ULL));
    result = (unsigned __int8)((*(unsigned __int8 *)(a1 + 304)) & (254));
    *(unsigned __int8 *)(a1 + 304) = (unsigned __int8)(result);
    if ((((unsigned __int8)(result)) & (2)) != 0) goto loc_00232584;
loc_002324A0:
    result = KeCancelTimer(a1, *(unsigned __int64 *)(a1 + 224 + 8), *(unsigned __int64 *)(a1 + 224), (unsigned int)(0xF55ULL));
    if ((unsigned __int8)(result) == 0) goto loc_00232595;
loc_002324B0:
loc_002324B5:
    result = KeRemoveQueueApc(a1 + 72, *(unsigned __int64 *)(a1 + 224 + 8), *(unsigned __int64 *)(a1 + 224), (unsigned int)(0xF55ULL));
    if ((unsigned __int8)(result) == 0) goto loc_0023186F;
    v_rbx = (unsigned int)((1) + 1);
    goto loc_0023186F;
loc_002324CD:
    goto loc_00231BE4;
loc_002324DC:
    if (*(unsigned __int64 *)(a1 - 40) != 0) goto loc_00232671;
    if (sign_flag) goto loc_002326AD;
    result = ObpDeferObjectDeletion(a1 - 48, *(unsigned __int64 *)(a1 + 224 + 8), *(unsigned __int64 *)(a1 - 40), (unsigned int)(0xF55ULL));
    goto loc_00231DBE;
loc_00232500:
    if (a6 == 0) goto loc_0023263D;
loc_0023250F:
    result = (unsigned __int8)((-1) & (6));
    if (((unsigned __int8)(result)) == 2) goto loc_00232554;
loc_00232525:
    result = KeAbPostRelease(v_rip + 13403772, *(unsigned __int64 *)(a1 + 224 + 8), *(unsigned __int64 *)(a1 - 40), (unsigned int)(0xF55ULL));
    result = KiLeaveCriticalRegionUnsafe(v_stack_m60, *(unsigned __int64 *)(a1 + 224 + 8), *(unsigned __int64 *)(a1 - 40), (unsigned int)(0xF55ULL));
    if (v_rbx == 0) goto loc_00231D7F;
    result = PoDestroyReasonContext(v_rbx, *(unsigned __int64 *)(a1 + 224 + 8), *(unsigned __int64 *)(a1 - 40), (unsigned int)(0xF55ULL));
    goto loc_00231D7F;
loc_00232554:
    result = ExfTryToWakePushLock(v_rip + 13403725, *(unsigned __int64 *)(a1 + 224 + 8), *(unsigned __int64 *)(a1 - 40), (unsigned int)(0xF55ULL));
    goto loc_00232525;
loc_00232562:
    if ((*(unsigned __int8 *)(v_rip + 13478250)) != ((unsigned __int8)(*(unsigned __int64 *)(a1 + 80)))) goto loc_002322A8;
    v_stack_m9C = 0x40000025ULL;
    v_stack_p58 = *(unsigned __int64 *)(a1 + 80);
    goto loc_002317A3;
loc_00232584:
    if ((*(unsigned __int8 *)(a1 + 248)) != ((unsigned __int8)(v_rbx))) goto loc_002324B0;
    goto loc_002324A0;
loc_00232595:
    a2 = 0;
    result = KeRemoveQueueDpcEx(a1 + 160, a2, *(unsigned __int64 *)(a1 - 40), (unsigned int)(0xF55ULL));
    if ((unsigned __int8)(result) == 0) goto loc_002324B5;
    goto loc_002324B0;
loc_002325B0:
loc_002325DE:
    result = (*(unsigned __int64 *)(1)) - (a1 + 160);
    v_rbx = *(unsigned __int64 *)(1);
    if (result <= (*(unsigned __int64 *)(1))) { v_rbx = result; }
loc_002325FC:
    a2 = (a2) >> (11);
    a1 = (a2) >> (63);
    a1 = (a1) + (a2);
    a1 = (unsigned int)((a1) + ((unsigned int)(v_stack_m50)));
    result = (unsigned int)(0xFFFFFFFFULL);
    if (((unsigned int)(a1)) >= ((unsigned int)(v_stack_m50))) { result = (unsigned int)(a1); }
    v_stack_p68 = (unsigned int)(result);
    goto loc_00231E4F;
loc_00232631:
    *(unsigned __int8 *)(a1 + 248) = 1;
    goto loc_00232431;
loc_0023263D:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 264) + 8)) != (a1 + 264)) goto loc_00231948;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 264 + 8))) != (a1 + 264)) goto loc_00231948;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 264 + 8)) = *(unsigned __int64 *)(a1 + 264);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 264) + 8) = *(unsigned __int64 *)(a1 + 264 + 8);
    *(unsigned __int64 *)(a1 + 264) = 0;
    goto loc_0023250F;
loc_00232671:
    result = (a1 - 48) >> (8);
    a2 = ((unsigned __int8)(result)) ^ (*(unsigned __int8 *)(a1 - 24));
    a2 = (a2) ^ (*(unsigned __int8 *)(v_rip + 14239682));
    v_stack_mC0 = *(unsigned __int64 *)(a1 - 40);
    result = KeBugCheckEx(6 + 18, *(unsigned __int64 *)(1 + a2 * 8 + 16545792), a1, 6);
loc_002326AD:
    v_stack_mC0 = 6 + 18;
    a2 = 0;
    result = KeBugCheckEx(a2 + 24, a2, a1, 5);
loc_002326C6:
    a1 = a2 + 24;
    if (0 < (a2 + 24)) { a1 = 0; }
    *(unsigned __int8 *)(a1) = (unsigned __int8)(*(unsigned __int8 *)(a1));
    *(unsigned __int8 *)(a2) = (unsigned __int8)(v_stack_mAD);
    goto loc_00231DCF;
}
```

## 5. (Beta) C Style

```c
int64_t ExpSetTimerObject(void *Arg1, uint8_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, int64_t Arg6, uint8_t Arg7, uint32_t Arg8, uint32_t Arg9, int64_t Arg10)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint64_t v_stack_m18;
    uint64_t v_stack_m28;
    uint8_t v_stack_m2F;
    uint64_t v_stack_m30;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint8_t v_stack_m57;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint32_t v_stack_m74;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint32_t v_stack_m9C;
    uint64_t v_stack_mA0;
    uint32_t v_stack_mA4;
    uint64_t v_stack_mA8;
    uint32_t v_stack_mAC;
    uint8_t v_stack_mAD;
    uint8_t v_stack_mAE;
    uint8_t v_stack_mAF;
    uint64_t v_stack_mB0;
    uint32_t v_stack_mB4;
    uint32_t v_stack_mBC;
    uint32_t v_stack_mC0;
    uint32_t v_stack_mC4;
    uint32_t v_stack_mD0;
    uint32_t v_stack_mD4;
    uint8_t v_stack_mD5;
    uint8_t v_stack_mD6;
    uint8_t v_stack_mD7;
    uint8_t v_stack_mD8;
    uint64_t v_stack_mE8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint32_t v_stack_p40;
    uint64_t v_stack_p58;
    uint32_t v_stack_p68;

    v_stack_p10 = local_rbx;
    v_stack_p20 = local_rsi;
    local_rsp = (local_rsp) - (224);
    result = (*(uint64_t *)(v_rip + 0xBD8FEF)) ^ (local_rsp);
    v_stack_m30 = result;
    v_stack_mD6 = Arg2;
    v_stack_m60 = Arg10;
    local_rsi = 0;
    v_stack_mC4 = 0;
    v_stack_mD7 = 0;
    v_stack_m88 = 0;
    if (Arg6 != 0) goto loc_00232292;
loc_002317A3:
    v_stack_m98 = 0;
    v_stack_m90 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8);
    v_stack_mD8 = 0;
    v_stack_mA8 = v_cr8;
    if ((*(uint32_t *)(v_rip + 0xD95545)) != 0) goto loc_002319BC;
loc_002317E1:
    if (v_stack_mD6 == 0) goto loc_00231822;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x88)))) & (16)) == 0) goto loc_00231822;
    if (((*(uint8_t *)(v_rip + 0xD95305)) & (33)) == 0) goto loc_002319A6;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCDC64B))) != 0) goto loc_002319A6;
    result = KiAcquireSpinLockInstrumented(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 1800, Arg2, Arg3, Arg4);
loc_0023181A:
    v_stack_mD8 = 1;
loc_00231822:
    if (((*(uint8_t *)(v_rip + 0xD952DD)) & (33)) == 0) goto loc_0023194F;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCDC623))) != 0) goto loc_0023194F;
    result = KiAcquireSpinLockInstrumented(Arg1 + 64, Arg2, Arg3, Arg4);
loc_00231846:
    if (v_stack_mD7 == 0) goto loc_00231979;
loc_00231858:
    local_rbx = 0;
    if (((*(uint8_t *)(arg1 + 0x130)) & (1)) != 0) goto loc_00232445;
    result = KeCancelTimer(Arg1, Arg2, Arg3, Arg4);
loc_0023186F:
    *(uint8_t *)(arg1 + 0xF8) = 0;
    v_stack_mD5 = (uint8_t)(*(uint8_t *)(arg1 + 0x4));
    *(uint32_t *)(arg1 + 0xF0) = (uint32_t)((uint32_t)(Arg8));
    Arg3 = 0;
    *(uint32_t *)(arg1 + 0xF4) = 0;
    *(uint32_t *)(arg1 + 0x140) = (uint32_t)((uint32_t)(Arg9));
    if (Arg4 == 0) goto loc_002321A9;
    *(uint8_t *)(arg1 + 0x48) = 18;
    *(uint8_t *)(arg1 + 0x4A) = 88;
    *(uint8_t *)(arg1 + 0x98) = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x24A));
    *(uint64_t *)(arg1 + 0x50) = *(uint64_t *)(gs_base + (0 + 0x188));
    *(uint64_t *)(arg1 + 0x68) = v_rip + 2526470;
    *(uint64_t *)(arg1 + 0x70) = 0;
    *(uint64_t *)(arg1 + 0x78) = Arg4;
    *(uint8_t *)(arg1 + 0x99) = (uint8_t)(v_stack_mD6);
    *(uint64_t *)(arg1 + 0x80) = Arg5;
    *(uint8_t *)(arg1 + 0x9A) = 0;
    *(uint8_t *)(arg1 + 0x49) = 0;
    if (((*(uint8_t *)(v_rip + 0xD951ED)) & (33)) == 0) goto loc_0023196A;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCDC537))) != 0) goto loc_0023196A;
    result = KiAcquireSpinLockInstrumented(*(uint64_t *)(gs_base + (0 + 0x188)) + 1264, Arg2, Arg3, Arg4);
loc_0023192A:
    Arg3 = 0;
loc_0023192D:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x4F8 + 0x8))) == (*(uint64_t *)(gs_base + (0 + 0x188)) + 1272)) goto loc_002319CC;
loc_00231948:
loc_0023194F:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x4F8 + 0x8))) >= (*(uint64_t *)(gs_base + (0 + 0x188)) + 1272)) goto loc_00231846;
    result = KxWaitForSpinLockAndAcquire(Arg1 + 64, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x4F8 + 0x8), Arg3, Arg4);
    goto loc_00231846;
loc_0023196A:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x4F8 + 0x8))) >= (*(uint64_t *)(gs_base + (0 + 0x188)) + 1272)) goto loc_0023192D;
    result = KxWaitForSpinLockAndAcquire(Arg1 + 64, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x4F8 + 0x8), Arg3, Arg4);
    goto loc_0023192A;
loc_00231979:
    if (result == 0) goto loc_00231858;
    result = KxReleaseSpinLock(Arg1 + 64, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x4F8 + 0x8), Arg3, Arg4);
    result = KxReleaseSpinLock(local_rbx + 1 + 1800, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x4F8 + 0x8), Arg3, Arg4);
loc_002319A6:
    if (condition_is_above_or_equal) goto loc_0023181A;
    result = KxWaitForSpinLockAndAcquire(local_rbx + 1 + 1800, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x4F8 + 0x8), Arg3, Arg4);
    goto loc_0023181A;
loc_002319BC:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(result), (uint8_t)(local_rbx + 1 + 1800), Arg3, Arg4);
    goto loc_002317E1;
loc_002319CC:
    *(uint64_t *)((uint8_t)(result)) = result;
    *(uint64_t *)((uint8_t)(result) + 0x8) = (uint8_t)(local_rbx + 1 + 1800);
    *(uint64_t *)((uint8_t)(local_rbx + 0x1 + 0x708)) = (uint8_t)(result);
    *(uint64_t *)(result + 0x8) = (uint8_t)(result);
    if (((*(uint8_t *)(v_rip + 0xD9511E)) & (1)) != 0) goto loc_00232218;
loc_002319EE:
loc_002319F7:
    v_stack_m98 = Arg1 + 160;
    local_r13 = (uint32_t)((local_rbx + 1) - 1);
    v_stack_p40 = 0;
loc_00231A11:
    Arg4 = 0;
    v_stack_mA0 = *(uint64_t *)(Arg3);
    if (v_stack_mD8 != 0) goto loc_00231E98;
loc_00231A33:
    if (((*(uint8_t *)(arg1 + 0x130)) & (2)) != 0) goto loc_00232405;
    result = 0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = 0;
    if ((uint32_t)((uint32_t)(Arg9)) != 0) goto loc_00231E11;
loc_00231A5D:
    v_stack_mB4 = 0;
    local_r14 = (Arg1 + 160) ^ (*(uint64_t *)(v_rip + 0xD957E4));
    local_r14 = (local_r14) ^ (Arg1);
    local_r14 = (local_r14) ^ (*(uint64_t *)(v_rip + 0xD954FF));
    v_stack_m68 = 2;
    if ((*(uint32_t *)(v_rip + 0xD95283)) != 0) goto loc_00231ED0;
loc_00231AA3:
    v_stack_mA0 = *(uint64_t *)(gs_base + (0 + 0x20));
    v_stack_m70 = 0;
    v_stack_mD0 = 0;
loc_00231ABE:
loc_00231AC5:
    v_stack_mC0 = 0;
    if ((*(uint32_t *)(v_rip + 0xD95283)) < 0) goto loc_00231FB0;
loc_00231AD5:
    if (((*(uint8_t *)(arg1 + 0x3)) & (192)) == 0) goto loc_00231E01;
    v_stack_mD4 = (uint32_t)(*(uint8_t *)(arg1 + 0x2));
    local_r11 = (*(uint64_t *)(v_rip - 0x231AC5 + *(uint16_t *)(arg1 + 0x38) * 8 + 0xFC8C40)) + (0x4100ULL);
    v_stack_mB0 = local_r11;
    Arg1 = (*(uint16_t *)(arg1 + 0x3A)) << (8);
    local_rsi = (*(uint8_t *)(arg1 + 0x2) + 16) + (Arg1);
    local_rsi = (local_rsi) << (5);
    local_rsi = (local_rsi) + (local_r11);
    v_stack_mBC = 0;
loc_00231B20:
    if (condition_is_above_or_equal) goto loc_00231B4E;
loc_00231B28:
    local_r15 = (uint32_t)(((uint32_t)(v_stack_mBC)) + 1);
    v_stack_mBC = (uint32_t)(local_r15);
    if (((*(uint32_t *)(v_rip + 0xD93770)) & ((uint32_t)(local_r15))) == 0) goto loc_0023208B;
loc_00231B42:
loc_00231B44:
    if (*(uint64_t *)(local_rsi) == 0) goto loc_00231B20;
    goto loc_00231B28;
loc_00231B4E:
    if (sign_flag) goto loc_002320F5;
    Arg1 = ((uint32_t)((uint32_t)(*(uint16_t *)(arg1 + 0x3A)))) << (8);
    Arg4 = ((uint32_t)(v_stack_mD4) + 16) + (Arg1);
    Arg4 = (Arg4) << (5);
    Arg4 = (Arg4) + (v_stack_mB0);
    v_stack_m80 = Arg4;
    Arg1 = ((uint32_t)((uint32_t)(*(uint16_t *)(arg1 + 0x3A)))) ^ (1);
    Arg1 = (Arg1) << (8);
    local_r10 = ((uint32_t)(v_stack_mD4) + 16) + (Arg1);
    local_r10 = (local_r10) << (5);
    local_r10 = (local_r10) + (v_stack_mB0);
    v_stack_m78 = local_r10;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x8)) != (Arg1 + 32)) goto loc_00231948;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x20 + 0x8))) != (Arg1 + 32)) goto loc_00231948;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x20 + 0x8)) = *(uint64_t *)(arg1 + 0x20);
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x8) = *(uint64_t *)(arg1 + 0x20 + 0x8);
    if ((*(uint64_t *)(arg1 + 0x20 + 0x8)) == (*(uint64_t *)(arg1 + 0x20))) goto loc_00231EE3;
loc_00231BD5:
loc_00231BE4:
    if (((*(uint32_t *)(v_rip + 0xD94F15)) & (0x20000ULL)) != 0) goto loc_0023230E;
loc_00231BF9:
    if ((*(uint32_t *)(v_rip + 0xD95043)) != 0) goto loc_00231C3C;
    if ((*(uint8_t *)(v_stack_mA0 + 0x20)) != 0) goto loc_00231E09;
    if (((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x1F4)) & (0x1000ULL)) != 0) goto loc_00231E81;
loc_00231C32:
    result = 0;
loc_00231C34:
    if (0 == 0) goto loc_00231E09;
loc_00231C3C:
    Arg2 = 0;
loc_00231C3E:
    *(uint16_t *)(arg1 + 0x3A * 1) = 0;
    *(uint64_t *)(arg1 + 0x30) = local_r14;
    *(uint32_t *)(arg1 + 0x3C) = (uint32_t)((uint32_t)(Arg8));
    result = KiComputeDueTime(Arg1, *(uint64_t *)(Arg3), v_stack_m57, v_stack_mB4);
    if ((uint32_t)(result) == 0) goto loc_00231E6E;
    result = 0;
    *(uint32_t *)(arg1 + 0x4) = 0;
    v_stack_mE8 = 0;
    result = KiInsertTimerTable(v_stack_mA0, Arg1, v_stack_m98, (uint32_t)(v_stack_mB4));
    if ((uint8_t)(result) == 0) goto loc_00231E6E;
    if (((*(uint32_t *)(v_rip + 0xD94E5E)) & (0x20000ULL)) != 0) goto loc_002323F2;
loc_00231CB7:
    v_stack_mE8 = (uint8_t)(v_stack_m68);
    Arg4 = 0;
    Arg2 = 0;
    result = KiExitDispatcher(v_stack_mA0, Arg2, 1, Arg4);
    if (Arg6 != 0) {
    }
    *(uint64_t *)(arg1 + 0x100) = Arg6;
    local_r12 = (uint8_t)((Arg7) << (2));
    local_r12 = (uint8_t)((local_r12) ^ ((uint8_t)(*(uint8_t *)(arg1 + 0x130))));
    local_r12 = (uint8_t)((local_r12) & (4));
    local_r12 = (uint8_t)((local_r12) ^ ((uint8_t)(*(uint8_t *)(arg1 + 0x130))));
    *(uint8_t *)(arg1 + 0x130) = (uint8_t)(local_r12);
    if (((*(uint8_t *)(v_rip + 0xD94DE0)) & (1)) != 0) goto loc_002321D8;
loc_00231D2C:
loc_00231D31:
    if (v_stack_mD8 == 0) goto loc_00231D51;
    if (((*(uint8_t *)(v_rip + 0xD94DC0)) & (1)) != 0) goto loc_002321F8;
loc_00231D4C:
loc_00231D51:
    result = *(uint8_t *)(arg1 + 0x130);
    if ((*(uint32_t *)(v_rip + 0xD94FC3)) != 0) {
        Arg1 = 2;
        Arg2 = (uint8_t)(v_stack_mA8);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, 1, Arg4);
    }
    if (v_stack_mD7 != 0) goto loc_00232363;
loc_00231D7F:
    if ((uint32_t)(local_r13) == 0) goto loc_00231DBE;
    result = (uint8_t)(v_stack_mA8);
    if ((*(uint32_t *)(v_rip + 0xD93285)) != 0) {
        Arg4 = 0x746C6644ULL;
        Arg3 = (uint32_t)(local_r13);
        Arg2 = 0;
        Arg1 = Arg1 - 48;
        result = ObpPushStackInfo(Arg1, Arg2, Arg3, Arg4);
    }
    result = (uint32_t)(-((uint32_t)((uint32_t)(local_r13))));
    Arg1 = ((int32_t)((uint32_t)(result))) - ((int32_t)((uint32_t)(local_r13)));
    if (condition_is_less_or_equal) goto loc_002324DC;
loc_00231DBE:
    if (v_stack_m60 != 0) goto loc_002326C6;
loc_00231DCF:
loc_00231DD3:
    Arg1 = (v_stack_m30) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_stack_m60, Arg3, Arg4);
    return result;
loc_00231E01:
    local_r15 = 0;
    goto loc_00231BE4;
loc_00231E09:
    goto loc_00231C3E;
loc_00231E11:
    Arg1 = (Arg1) * (*(uint64_t *)(v_stack_m28 + 0x48));
    if (Arg1 <= 0x927C00ULL) goto loc_00231E57;
    Arg1 = (Arg1) + (0xFFFFFFFFFF6D8400ULL);
    if (sign_flag) goto loc_002320B3;
    Arg3 = Arg1 + *(uint64_t *)(v_stack_m28 + 0x38) * 1;
    if ((Arg1 + *(uint64_t *)(v_stack_m28 + 0x38) * 1) < (*(uint64_t *)(v_stack_m28 + 0x38))) { Arg3 = result; }
loc_00231E46:
    if ((uint32_t)(local_r10) != 0) goto loc_002325FC;
loc_00231E4F:
loc_00231E57:
    result = KiEncodeTolerableDelayValue((uint32_t)(0x927C00ULL), (uint16_t)(*(uint64_t *)(v_stack_m28 + 0x48)), Arg3, Arg4);
    result = (uint8_t)((result) << (2));
    v_stack_m2F = (uint8_t)(result);
    Arg3 = 0;
    goto loc_00231A5D;
loc_00231E6E:
    Arg3 = 0;
    result = KiTimerWaitTest(0, Arg1, Arg3, Arg4);
    goto loc_00231CB7;
loc_00231E81:
    if (((*(uint32_t *)(0 + 0x5FC)) & (0x4000000ULL)) != 0) goto loc_00231C32;
    goto loc_00231C34;
loc_00231E98:
    if ((*(uint64_t *)(arg1 + 0x118)) == 0) goto loc_002325B0;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m90 + 0x88)))) & (16)) == 0) goto loc_00231EC8;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m90 + 0x44))) != 0) goto loc_002325DE;
loc_00231EC8:
    Arg3 = 0;
    goto loc_00231A33;
loc_00231ED0:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m90 + 0x88))), (uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m90 + 0x44))), Arg3, Arg4);
    Arg3 = 0;
    goto loc_00231AA3;
loc_00231EE3:
    *(uint32_t *)(Arg4 + 0x1C) = 0xFFFFFFFFULL;
    if (0 != 0) goto loc_00231FE4;
    local_r15 = (local_r15) + (272);
    local_r15 = (local_r15) << (5);
    local_r15 = (local_r15) + (v_stack_m28);
    v_stack_mA4 = 0;
loc_00231F10:
    if (condition_is_above_or_equal) goto loc_00231F3A;
loc_00231F18:
    result = (uint32_t)(((uint32_t)(v_stack_mA4)) + 1);
    v_stack_mA4 = (uint32_t)(result);
    if (((*(uint32_t *)(v_rip + 0xD93384)) & ((uint32_t)(result))) == 0) goto loc_00232180;
loc_00231F2E:
loc_00231F30:
    if (*(uint64_t *)(local_r15) == 0) goto loc_00231F10;
    goto loc_00231F18;
loc_00231F3A:
loc_00231F4F:
    if ((*(uint32_t *)(v_stack_m58 + 0x1C)) != -1) goto loc_00231F9E;
    if ((*(uint32_t *)(v_stack_m50 + 0x1C)) != -1) goto loc_00231F9E;
    result = (*(uint8_t *)(v_stack_m88 - 0x4030)) + (*(uint8_t *)(v_stack_m88 - 0x4030));
    if ((*(uint32_t *)(v_rip + 0xD930B2)) == 0) goto loc_002320D1;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_mAC)))) & (63));
    Arg3 = (uint32_t)(((uint32_t)(v_stack_mAC)) >> (6));
loc_00231F9E:
    goto loc_00231BD5;
loc_00231FB0:
    local_rsi = (uint32_t)(((uint32_t)(v_stack_m98)) + 1);
    v_stack_m98 = (uint32_t)(local_rsi);
    if (((*(uint32_t *)(v_rip + 0xD932EC)) & ((uint32_t)(local_rsi))) == 0) goto loc_002321B1;
loc_00231FC6:
loc_00231FC8:
    if (sign_flag) goto loc_00231FB0;
    if (condition_is_below) goto loc_00231FB0;
    Arg3 = 0;
    goto loc_00231AD5;
loc_00231FE4:
    local_r15 = (local_r15) + (16);
    local_r15 = (local_r15) << (5);
    local_r15 = (local_r15) + (v_stack_m88);
    if (!(condition_is_above_or_equal)) {
        local_r15 = 0;
    }
    if (0 != 0) goto loc_00231F4F;
    v_stack_m90 = 0;
loc_00232017:
    if (condition_is_above_or_equal) goto loc_00232041;
loc_0023201F:
    local_rsi = (uint32_t)(((uint32_t)(v_stack_m90)) + 1);
    v_stack_m90 = (uint32_t)(local_rsi);
    if (((*(uint32_t *)(v_rip + 0xD9327D)) & ((uint32_t)(local_rsi))) == 0) goto loc_00232242;
loc_00232035:
loc_00232037:
    if (*(uint64_t *)(0) == 0) goto loc_00232017;
    goto loc_0023201F;
loc_00232041:
    local_rsi = ((uint32_t)(v_stack_mAC)) + (272);
    local_rsi = (local_rsi) << (5);
    local_rsi = (local_rsi) + (v_stack_m88);
    v_stack_mA0 = 0;
loc_0023205D:
    if (condition_is_above_or_equal) goto loc_00231F3A;
loc_00232069:
    result = (uint32_t)(((uint32_t)(v_stack_mA0)) + 1);
    v_stack_mA0 = (uint32_t)(result);
    if (((*(uint32_t *)(v_rip + 0xD93233)) & ((uint32_t)(result))) == 0) goto loc_00232269;
loc_0023207F:
loc_00232081:
    if (*(uint64_t *)(local_rsi) == 0) goto loc_0023205D;
    goto loc_00232069;
loc_0023208B:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD94A27)))) & (64)) == 0) goto loc_00231B42;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_rip - 2301916, Arg2, Arg3, v_stack_m58);
    if ((uint8_t)(result) == 0) goto loc_00231B42;
    result = HvlNotifyLongSpinWait(0, Arg2, Arg3, v_stack_m58);
    goto loc_00231B44;
loc_002320B3:
    Arg3 = (0) - (0);
    if (Arg3 <= Arg3) goto loc_00231E46;
    goto loc_00231E46;
loc_002320D1:
    result = ((uint32_t)(v_stack_mAC)) << (6);
    Arg1 = (0) + (result);
    goto loc_00231BD5;
loc_002320F5:
    result = (uint32_t)((*(uint8_t *)(arg1 + 0x3)) & (63));
    Arg3 = 0;
    if (0 != 0) goto loc_002324CD;
    v_stack_mA8 = 0;
    if (!sign_flag) goto loc_00231AC5;
loc_00232140:
    local_rsi = (uint32_t)(((uint32_t)(v_stack_mA8)) + 1);
    v_stack_mA8 = (uint32_t)(local_rsi);
    if (((*(uint32_t *)(v_rip + 0xD9315C)) & ((uint32_t)(local_rsi))) == 0) goto loc_00232164;
loc_00232152:
loc_00232154:
    if (sign_flag) goto loc_00232140;
    Arg3 = 0;
    goto loc_00231ABE;
loc_00232164:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD9494E)))) & (64)) == 0) goto loc_00232152;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_rip - 2302258, v_stack_m88, Arg3, v_stack_m58);
    if ((uint8_t)(result) == 0) goto loc_00232152;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rsi)), v_stack_m88, Arg3, v_stack_m58);
    goto loc_00232154;
loc_00232180:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD94932)))) & (64)) == 0) goto loc_00231F2E;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)((uint32_t)(local_rsi)), v_stack_m88, Arg3, v_stack_m58);
    if ((uint8_t)(result) == 0) goto loc_00231F2E;
    result = HvlNotifyLongSpinWait((uint32_t)(v_stack_mA4), v_stack_m88, Arg3, v_stack_m58);
    goto loc_00231F30;
loc_002321A9:
    goto loc_00231A11;
loc_002321B1:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD94901)))) & (64)) == 0) goto loc_00231FC6;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)(v_stack_mA4), v_stack_m88, Arg3, v_stack_m58);
    if ((uint8_t)(result) == 0) goto loc_00231FC6;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rsi)), v_stack_m88, Arg3, v_stack_m58);
    goto loc_00231FC8;
loc_002321D8:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCDBC7A))) != 0) goto loc_00231D2C;
    result = KiReleaseSpinLockInstrumented((uint32_t)((uint32_t)(local_rsi)), v_stack_p28, Arg3, v_stack_m58);
    goto loc_00231D31;
loc_002321F8:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCDBC5A))) != 0) goto loc_00231D4C;
    result = KiReleaseSpinLockInstrumented((uint32_t)((uint32_t)(local_rsi)), v_stack_p28, Arg3, v_stack_m58);
    goto loc_00231D51;
loc_00232218:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCDBC3A))) != 0) goto loc_002319EE;
    result = KiReleaseSpinLockInstrumented(Arg3 + 1264, v_stack_p28, Arg3, v_stack_m58);
    Arg3 = 0;
    goto loc_002319F7;
loc_00232242:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD94870)))) & (64)) == 0) goto loc_00232035;
    result = KiCheckVpBackingLongSpinWaitHypercall(Arg3 + 1264, v_stack_p28, Arg3, v_stack_m58);
    if ((uint8_t)(result) == 0) goto loc_00232035;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rsi)), v_stack_p28, Arg3, v_stack_m58);
    goto loc_00232037;
loc_00232269:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD94849)))) & (64)) == 0) goto loc_0023207F;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)((uint32_t)(local_rsi)), v_stack_p28, Arg3, v_stack_m58);
    if ((uint8_t)(result) == 0) goto loc_0023207F;
    result = HvlNotifyLongSpinWait((uint32_t)(v_stack_mA0), v_stack_p28, Arg3, v_stack_m58);
    goto loc_00232081;
loc_00232292:
    if ((uint8_t)(local_r12) != 0) goto loc_002323AE;
loc_0023229B:
    if ((*(uint32_t *)(v_rip + 0xCDAC5E)) < 2) goto loc_00232562;
loc_002322A8:
    v_stack_mAF = 1;
    v_stack_m60 = *(uint64_t *)(gs_base + (0 + 0x188));
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(v_rip + 13404374, Arg2, Arg3, v_stack_m58);
    if (!(condition_is_above_or_equal)) {
        Arg3 = v_rip + 13404347;
        Arg2 = result;
        Arg1 = v_rip + 13404337;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, v_stack_m58);
    }
    if (result == 0) goto loc_002317A3;
    *(uint8_t *)(result + 0xA) = 1;
    goto loc_002317A3;
loc_0023230E:
    if (0 == 0) goto loc_00231BF9;
    v_stack_m48 = Arg1;
    v_stack_m18 = v_stack_m48;
    v_stack_m10 = 8;
    v_stack_mC0 = 0x602ULL;
    result = EtwTraceKernelEvent(v_stack_m18, (uint32_t)((uint32_t)(local_rsi)), (uint32_t)(0x40020000ULL), (uint32_t)(0xF55ULL));
    goto loc_00231BF9;
loc_00232363:
    if (result != 0) goto loc_00232500;
    if (Arg6 == result) goto loc_0023250F;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xCC8810))) != (v_rip + 13404161)) goto loc_00231948;
    *(uint64_t *)(arg1 + 0x108) = v_rip + 13404161;
    *(uint64_t *)(arg1 + 0x108 + 0x8) = *(uint64_t *)(v_rip + 0xCC8810);
    *(void **)(*(uint64_t *)(v_rip + 0xCC8810)) = Arg1 + 264;
    *(void **)(v_rip + 0xCC87EF) = Arg1 + 264;
    goto loc_0023250F;
loc_002323AE:
    result = ExpCheckTestsigningEnabled(Arg1 + 264, v_rip + 13404161, (uint32_t)(0x40020000ULL), (uint32_t)(0xF55ULL));
    if ((uint8_t)(result) != 0) goto loc_0023229B;
    result = ExpCheckWakeTimerAccess(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232), v_rip + 13404161, (uint32_t)(0x40020000ULL), (uint32_t)(0xF55ULL));
    v_stack_m9C = (uint32_t)(result);
    if ((uint32_t)(result) == 0) goto loc_0023229B;
    result = ObfDereferenceObjectWithTag(Arg1, (uint32_t)(0x746C6644ULL), (uint32_t)(0x40020000ULL), (uint32_t)(0xF55ULL));
    goto loc_00231DD3;
loc_002323F2:
    Arg3 = 0;
    result = KiTraceSetTimer(Arg1, (uint32_t)((uint32_t)(result)), Arg3, (uint32_t)(0xF55ULL));
    goto loc_00231CB7;
loc_00232405:
    *(uint64_t *)(arg1 + 0x138) = (uint32_t)((uint32_t)(result));
    if (v_stack_m74 >= 0) goto loc_00232631;
    if (Arg6 == 0) {
        Arg1 = 2;
    }
    *(uint8_t *)(arg1 + 0xF8 * 1) = (uint8_t)(Arg1);
loc_00232431:
    goto loc_00231CF1;
loc_00232445:
    result = KeAcquireSpinLockAtDpcLevel(*(uint64_t *)(arg1 + 0x50) + 1264, Arg1, Arg3, (uint32_t)(0xF55ULL));
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0xE0) + 0x8)) != (Arg1 + 224)) goto loc_00231948;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0xE0 + 0x8))) != (Arg1 + 224)) goto loc_00231948;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0xE0 + 0x8)) = *(uint64_t *)(arg1 + 0xE0);
    *(uint64_t *)(*(uint64_t *)(arg1 + 0xE0) + 0x8) = *(uint64_t *)(arg1 + 0xE0 + 0x8);
    result = KxReleaseSpinLock(*(uint64_t *)(arg1 + 0x50) + 1264, *(uint64_t *)(arg1 + 0xE0 + 0x8), *(uint64_t *)(arg1 + 0xE0), (uint32_t)(0xF55ULL));
    result = (uint8_t)((*(uint8_t *)(arg1 + 0x130)) & (254));
    *(uint8_t *)(arg1 + 0x130) = (uint8_t)(result);
    if ((((uint8_t)(result)) & (2)) != 0) goto loc_00232584;
loc_002324A0:
    result = KeCancelTimer(Arg1, *(uint64_t *)(arg1 + 0xE0 + 0x8), *(uint64_t *)(arg1 + 0xE0), (uint32_t)(0xF55ULL));
    if ((uint8_t)(result) == 0) goto loc_00232595;
loc_002324B0:
loc_002324B5:
    result = KeRemoveQueueApc(Arg1 + 72, *(uint64_t *)(arg1 + 0xE0 + 0x8), *(uint64_t *)(arg1 + 0xE0), (uint32_t)(0xF55ULL));
    if ((uint8_t)(result) == 0) goto loc_0023186F;
    local_rbx = (uint32_t)((1) + 1);
    goto loc_0023186F;
loc_002324CD:
    goto loc_00231BE4;
loc_002324DC:
    if (*(uint64_t *)(arg1 - 0x28) != 0) goto loc_00232671;
    if (sign_flag) goto loc_002326AD;
    result = ObpDeferObjectDeletion(Arg1 - 48, *(uint64_t *)(arg1 + 0xE0 + 0x8), *(uint64_t *)(arg1 - 0x28), (uint32_t)(0xF55ULL));
    goto loc_00231DBE;
loc_00232500:
    if (Arg6 == 0) goto loc_0023263D;
loc_0023250F:
    result = (uint8_t)((-1) & (6));
    if (((uint8_t)(result)) == 2) goto loc_00232554;
loc_00232525:
    result = KeAbPostRelease(v_rip + 13403772, *(uint64_t *)(arg1 + 0xE0 + 0x8), *(uint64_t *)(arg1 - 0x28), (uint32_t)(0xF55ULL));
    result = KiLeaveCriticalRegionUnsafe(v_stack_m60, *(uint64_t *)(arg1 + 0xE0 + 0x8), *(uint64_t *)(arg1 - 0x28), (uint32_t)(0xF55ULL));
    if (local_rbx == 0) goto loc_00231D7F;
    result = PoDestroyReasonContext(local_rbx, *(uint64_t *)(arg1 + 0xE0 + 0x8), *(uint64_t *)(arg1 - 0x28), (uint32_t)(0xF55ULL));
    goto loc_00231D7F;
loc_00232554:
    result = ExfTryToWakePushLock(v_rip + 13403725, *(uint64_t *)(arg1 + 0xE0 + 0x8), *(uint64_t *)(arg1 - 0x28), (uint32_t)(0xF55ULL));
    goto loc_00232525;
loc_00232562:
    if ((*(uint8_t *)(v_rip + 0xCDA96A)) != ((uint8_t)(*(uint64_t *)(arg1 + 0x50)))) goto loc_002322A8;
    v_stack_m9C = 0x40000025ULL;
    v_stack_p58 = *(uint64_t *)(arg1 + 0x50);
    goto loc_002317A3;
loc_00232584:
    if ((*(uint8_t *)(arg1 + 0xF8)) != ((uint8_t)(local_rbx))) goto loc_002324B0;
    goto loc_002324A0;
loc_00232595:
    Arg2 = 0;
    result = KeRemoveQueueDpcEx(Arg1 + 160, Arg2, *(uint64_t *)(arg1 - 0x28), (uint32_t)(0xF55ULL));
    if ((uint8_t)(result) == 0) goto loc_002324B5;
    goto loc_002324B0;
loc_002325B0:
loc_002325DE:
    result = (*(uint64_t *)(1)) - (Arg1 + 160);
    local_rbx = *(uint64_t *)(1);
    if (result <= (*(uint64_t *)(1))) { local_rbx = result; }
loc_002325FC:
    Arg2 = (Arg2) >> (11);
    Arg1 = (Arg2) >> (63);
    Arg1 = (Arg1) + (Arg2);
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(v_stack_m50)));
    result = (uint32_t)(0xFFFFFFFFULL);
    if (((uint32_t)(Arg1)) >= ((uint32_t)(v_stack_m50))) { result = (uint32_t)(Arg1); }
    v_stack_p68 = (uint32_t)(result);
    goto loc_00231E4F;
loc_00232631:
    *(uint8_t *)(arg1 + 0xF8) = 1;
    goto loc_00232431;
loc_0023263D:
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x108) + 0x8)) != (Arg1 + 264)) goto loc_00231948;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x108 + 0x8))) != (Arg1 + 264)) goto loc_00231948;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x108 + 0x8)) = *(uint64_t *)(arg1 + 0x108);
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x108) + 0x8) = *(uint64_t *)(arg1 + 0x108 + 0x8);
    *(uint64_t *)(arg1 + 0x108) = 0;
    goto loc_0023250F;
loc_00232671:
    result = (Arg1 - 48) >> (8);
    Arg2 = ((uint8_t)(result)) ^ (*(uint8_t *)(arg1 - 0x18));
    Arg2 = (Arg2) ^ (*(uint8_t *)(v_rip + 0xD947C2));
    v_stack_mC0 = *(uint64_t *)(arg1 - 0x28);
    result = KeBugCheckEx(6 + 18, *(uint64_t *)(1 + Arg2 * 8 + 0xFC7800), Arg1, 6);
loc_002326AD:
    v_stack_mC0 = 6 + 18;
    Arg2 = 0;
    result = KeBugCheckEx(Arg2 + 24, Arg2, Arg1, 5);
loc_002326C6:
    Arg1 = Arg2 + 24;
    if (0 < (Arg2 + 24)) { Arg1 = 0; }
    *(uint8_t *)(arg1) = (uint8_t)(*(uint8_t *)(arg1));
    *(uint8_t *)(Arg2) = (uint8_t)(v_stack_mAD);
    goto loc_00231DCF;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `- 0x30` | `64` | `R` |
| `Arg1` | `- 0x30` | `64` | `R/W` |
| `Arg1` | `- 0x28` | `64` | `R` |
| `Arg1` | `- 0x18` | `8` | `R` |
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x0` | `32` | `R/W` |
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x0` | `64` | `R/W` |
| `Arg1` | `+ 0x0` | `64` | `W` |
| `Arg1` | `+ 0x0 + rax*1` | `8` | `W` |
| `Arg1` | `+ 0x0 + rax*1` | `16` | `W` |
| `Arg1` | `+ 0x2` | `8` | `R` |
| `Arg1` | `+ 0x3` | `8` | `R` |
| `Arg1` | `+ 0x4` | `8` | `R` |
| `Arg1` | `+ 0x4` | `32` | `W` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `W` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x30` | `64` | `W` |
| `Arg1` | `+ 0x38` | `16` | `R` |
| `Arg1` | `+ 0x3A` | `16` | `R` |
| `Arg1` | `+ 0x3C` | `32` | `W` |
| `Arg1` | `+ 0x40` | `64` | `R` |
| `Arg1` | `+ 0x40` | `64` | `R/W` |
| `Arg1` | `+ 0x48` | `8` | `W` |
| `Arg1` | `+ 0x48` | `64` | `R` |
| `Arg1` | `+ 0x49` | `8` | `W` |
| `Arg1` | `+ 0x4A` | `8` | `W` |
| `Arg1` | `+ 0x50` | `64` | `R` |
| `Arg1` | `+ 0x50` | `64` | `W` |
| `Arg1` | `+ 0x68` | `64` | `W` |
| `Arg1` | `+ 0x70` | `64` | `W` |

추가 오프셋 20개는 표에서 생략했습니다.

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00231730&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
