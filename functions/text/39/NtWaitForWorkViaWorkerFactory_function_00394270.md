# NtWaitForWorkViaWorkerFactory

- RVA: `0x00394270`–`0x00394F36` (길이 `3,270` bytes)
- VA: `0x0000000140394270`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00080FB8`
- 디코드: `679`개 명령, `3,270/3,270` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **52**; 고유 호출 대상: **41**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **10**

### Outgoing calls
- `0x003943A3` → [ProbeForWrite](../../page/8E/ProbeForWrite_function_008E91C0.md) (function, `0x008E91C0`)
- `0x003943E3` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x0039447D` → [ObReferenceObjectByHandle](../../page/86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x0039451B` → [KiDeregisterObjectWaitBlock](KiDeregisterObjectWaitBlock_function_00394F3C.md) (function, `0x00394F3C`)
- `0x0039452C` → [ObfDereferenceObjectWithTag](../2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x003945C2` → [KxWaitForLockChainValid](../21/KxWaitForLockChainValid_function_00217AA0.md) (function, `0x00217AA0`)
- `0x003945E5` → [KeWakeAddressAll](../21/KeWakeAddressAll_function_00217C20.md) (function, `0x00217C20`)
- `0x00394643` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00394666` → [ObpPushStackInfo](../21/ObpPushStackInfo_function_002109E4.md) (function, `0x002109E4`)
- `0x00394693` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x003946D2` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x003946EE` → [KiAcquireQueuedSpinLockInstrumented](../27/KiAcquireQueuedSpinLockInstrumented_function_00275850.md) (function, `0x00275850`)
- `0x00394713` → [KiReleaseQueuedSpinLockInstrumented](../21/KiReleaseQueuedSpinLockInstrumented_function_002179F0.md) (function, `0x002179F0`)
- `0x0039472D` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x003947D4` → [ObReferenceObjectByHandle](../../page/86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x00394856` → [AlpcpSendMessage](../../page/88/AlpcpSendMessage_function_0088BD40.md) (function, `0x0088BD40`)
- `0x00394890` → [AlpcpSignal](AlpcpSignal_function_003955E0.md) (function, `0x003955E0`)
- `0x0039489E` → [KeLeaveCriticalRegionThread](../25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x003948EC` → [PspRevertContainerImpersonation](PspRevertContainerImpersonation_function_00395070.md) (function, `0x00395070`)
- `0x0039492A` → [IoRemoveIoCompletion](../20/IoRemoveIoCompletion_function_0020B580.md) (function, `0x0020B580`)
- `0x0039493A` → [ExpWorkerFactoryFinishDeferredWork](ExpWorkerFactoryFinishDeferredWork_function_00395000.md) (function, `0x00395000`)
- `0x003949F9` → [ObfDereferenceObjectWithTag](../2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00394A73` → [KxWaitForLockChainValid](../21/KxWaitForLockChainValid_function_00217AA0.md) (function, `0x00217AA0`)
- `0x00394AA6` → [KeDisableInterrupts](../21/KeDisableInterrupts_function_00217BE0.md) (function, `0x00217BE0`)
- `0x00394AB9` → [KiHaltOnAddressWakeEntireList](../21/KiHaltOnAddressWakeEntireList_function_00217AF4.md) (function, `0x00217AF4`)
- `0x00394AF9` → [KiReleaseQueuedSpinLockInstrumented](../21/KiReleaseQueuedSpinLockInstrumented_function_002179F0.md) (function, `0x002179F0`)
- `0x00394B1A` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x00394B98` → [KiAcquireQueuedSpinLockInstrumented](../27/KiAcquireQueuedSpinLockInstrumented_function_00275850.md) (function, `0x00275850`)
- `0x00394BE3` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00394C30` → [ObfReferenceObjectWithTag](../21/ObfReferenceObjectWithTag_function_00210710.md) (function, `0x00210710`)
- `0x00394C47` → [KeRegisterObjectNotification](KeRegisterObjectNotification_function_00393454.md) (function, `0x00393454`)
- `0x00394C59` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x00394C6A` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x00394C7B` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x00394C8D` → [ObfReferenceObjectWithTag](../21/ObfReferenceObjectWithTag_function_00210710.md) (function, `0x00210710`)
- `0x00394CB8` → [KxWaitForLockOwnerShip](../25/KxWaitForLockOwnerShip_function_00257EB0.md) (function, `0x00257EB0`)
- `0x00394CCD` → [ExpWorkerFactoryCheckCreate](../34/ExpWorkerFactoryCheckCreate_function_00344460.md) (function, `0x00344460`)
- `0x00394CE3` → [KxWaitForLockOwnerShip](../25/KxWaitForLockOwnerShip_function_00257EB0.md) (function, `0x00257EB0`)
- `0x00394D0B` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x00394D1D` → [ExpWorkerFactoryWantsToCreate](../45/ExpWorkerFactoryWantsToCreate_function_00452734.md) (function, `0x00452734`)
- `0x00394D8E` → [ExpRemoveCurrentThreadFromThreadHistory](../48/ExpRemoveCurrentThreadFromThreadHistory_function_00483154.md) (function, `0x00483154`)
- `0x00394DAF` → [KeAreInterruptsEnabled](../2F/KeAreInterruptsEnabled_function_002F8060.md) (function, `0x002F8060`)
- `0x00394DDD` → [ObpDeregisterObject](../../page/9D/ObpDeregisterObject_function_009D7F78.md) (function, `0x009D7F78`)
- `0x00394DE8` → [ObpRemoveObjectRoutine](../../page/86/ObpRemoveObjectRoutine_function_00864A60.md) (function, `0x00864A60`)
- `0x00394E0D` → [ObpHandleRevocationBlockRemoveObject](../../page/9D/ObpHandleRevocationBlockRemoveObject_function_009D7E30.md) (function, `0x009D7E30`)
- `0x00394E31` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x00394E58` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00394EB9` → [NtAlpcSendWaitReceivePort](../../page/86/NtAlpcSendWaitReceivePort_function_00868040.md) (function, `0x00868040`)
- `0x00394EC7` → [ObpDeferObjectDeletion](../3A/ObpDeferObjectDeletion_function_003A2394.md) (function, `0x003A2394`)
- `0x00394EE5` → [KeAbPreAcquire](../21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00394F0B` → [ExfAcquirePushLockExclusiveEx](../20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x00394F2C` → [ObfDereferenceObject](../2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00394285` → RVA `0x00E0A740` (`.data`; read)
- `0x00394452` → RVA `0x00FC51E0` (`ALMOSTRO`; read)
- `0x003944B8` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x003944CA` → RVA `0x00FC6B06` (`ALMOSTRO`; read)
- `0x00394615` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x0039464D` → RVA `0x00FC5010` (`ALMOSTRO`; read)
- `0x003946D8` → RVA `0x00F0DE58` (`.data`; read)
- `0x003947A8` → RVA `0x00FC6C18` (`ALMOSTRO`; read)
- `0x00394BBF` → RVA `0x00FC6E4C` (`ALMOSTRO`; read)
- `0x00394C3C` → RVA `0x00EFA1A0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **11**
  - `0x003943A3` → [ProbeForWrite](../../page/8E/ProbeForWrite_function_008E91C0.md) (`.text` → `PAGE`)
  - `0x003943E3` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (`.text` → `PAGE`)
  - `0x0039447D` → [ObReferenceObjectByHandle](../../page/86/ObReferenceObjectByHandle_function_00868DB0.md) (`.text` → `PAGE`)
  - `0x00394643` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x003947D4` → [ObReferenceObjectByHandle](../../page/86/ObReferenceObjectByHandle_function_00868DB0.md) (`.text` → `PAGE`)
  - `0x00394856` → [AlpcpSendMessage](../../page/88/AlpcpSendMessage_function_0088BD40.md) (`.text` → `PAGE`)
  - `0x00394DDD` → [ObpDeregisterObject](../../page/9D/ObpDeregisterObject_function_009D7F78.md) (`.text` → `PAGE`)
  - `0x00394DE8` → [ObpRemoveObjectRoutine](../../page/86/ObpRemoveObjectRoutine_function_00864A60.md) (`.text` → `PAGE`)
  - `0x00394E0D` → [ObpHandleRevocationBlockRemoveObject](../../page/9D/ObpHandleRevocationBlockRemoveObject_function_009D7E30.md) (`.text` → `PAGE`)
  - `0x00394E58` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x00394EB9` → [NtAlpcSendWaitReceivePort](../../page/86/NtAlpcSendWaitReceivePort_function_00868040.md) (`.text` → `PAGE`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x00394EFF` → [sub_006E5986](../6E/Unknown_function_006E5986.md) (`tail-transfer`)
  - `0x00394F1F` → [sub_006E5986](../6E/Unknown_function_006E5986.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00394270  4C 8B DC                        mov r11, rsp
00394273  53                              push rbx
00394274  56                              push rsi
00394275  57                              push rdi
00394276  41 54                           push r12
00394278  41 55                           push r13
0039427A  41 56                           push r14
0039427C  41 57                           push r15
0039427E  48 81 EC C0 01 00 00            sub rsp, 0x1c0
00394285  48 8B 05 B4 64 A7 00            mov rax, qword ptr [rip + 0xa764b4]
0039428C  48 33 C4                        xor rax, rsp
0039428F  48 89 84 24 B0 01 00 00         mov qword ptr [rsp + 0x1b0], rax
00394297  49 8B C1                        mov rax, r9
0039429A  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
003942A2  45 8B F8                        mov r15d, r8d
003942A5  44 89 7C 24 60                  mov dword ptr [rsp + 0x60], r15d
003942AA  4C 8B CA                        mov r9, rdx
003942AD  48 89 94 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], rdx
003942B5  48 8B F9                        mov rdi, rcx
003942B8  48 89 8C 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rcx
003942C0  48 89 94 24 88 00 00 00         mov qword ptr [rsp + 0x88], rdx
003942C8  44 89 7C 24 70                  mov dword ptr [rsp + 0x70], r15d
003942CD  48 89 84 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], rax
003942D5  48 8B 9C 24 20 02 00 00         mov rbx, qword ptr [rsp + 0x220]
003942DD  0F 57 C0                        xorps xmm0, xmm0
003942E0  33 C0                           xor eax, eax
003942E2  0F 11 84 24 A8 00 00 00         movups xmmword ptr [rsp + 0xa8], xmm0
003942EA  0F 11 84 24 B8 00 00 00         movups xmmword ptr [rsp + 0xb8], xmm0
003942F2  49 89 83 D0 FE FF FF            mov qword ptr [r11 - 0x130], rax
003942F9  0F 11 44 24 48                  movups xmmword ptr [rsp + 0x48], xmm0
003942FE  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
00394303  0F 57 C9                        xorps xmm1, xmm1
00394306  0F 11 8C 24 30 01 00 00         movups xmmword ptr [rsp + 0x130], xmm1
0039430E  0F 11 8C 24 40 01 00 00         movups xmmword ptr [rsp + 0x140], xmm1
00394316  0F 11 8C 24 50 01 00 00         movups xmmword ptr [rsp + 0x150], xmm1
0039431E  0F 11 8C 24 60 01 00 00         movups xmmword ptr [rsp + 0x160], xmm1
00394326  0F 11 8C 24 70 01 00 00         movups xmmword ptr [rsp + 0x170], xmm1
0039432E  41 0F 11 4B 88                  movups xmmword ptr [r11 - 0x78], xmm1
00394333  41 0F 11 4B 98                  movups xmmword ptr [r11 - 0x68], xmm1
00394338  41 0F 11 4B A8                  movups xmmword ptr [r11 - 0x58], xmm1
0039433D  45 33 ED                        xor r13d, r13d
00394340  44 89 6C 24 64                  mov dword ptr [rsp + 0x64], r13d
00394345  45 8B F5                        mov r14d, r13d
00394348  41 8B F5                        mov esi, r13d
0039434B  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00394354  48 89 84 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], rax
0039435C  44 0F B6 A0 32 02 00 00         movzx r12d, byte ptr [rax + 0x232]
00394364  44 88 64 24 40                  mov byte ptr [rsp + 0x40], r12b
00394369  44 88 64 24 41                  mov byte ptr [rsp + 0x41], r12b
0039436E  49 8D 83 38 FF FF FF            lea rax, [r11 - 0xc8]
00394375  48 89 84 24 98 00 00 00         mov qword ptr [rsp + 0x98], rax
0039437D  41 8D 47 FF                     lea eax, [r15 - 1]
00394381  3D FE FF FF 07                  cmp eax, 0x7fffffe
00394386  0F 87 88 0A 00 00               ja 0x140394e14
0039438C  45 84 E4                        test r12b, r12b
0039438F  0F 84 5A 02 00 00               je 0x1403945ef
00394395  41 8B D7                        mov edx, r15d
00394398  48 C1 E2 05                     shl rdx, 5
0039439C  45 8D 45 08                     lea r8d, [r13 + 8]
003943A0  49 8B C9                        mov rcx, r9
003943A3  E8 18 4E 55 00                  call 0x1408e91c0
003943A8  49 B8 00 00 FF FF FF 7F 00 00   movabs r8, 0x7fffffff0000
003943B2  49 8B C8                        mov rcx, r8
003943B5  4C 39 84 24 90 00 00 00         cmp qword ptr [rsp + 0x90], r8
003943BD  48 0F 42 8C 24 90 00 00 00      cmovb rcx, qword ptr [rsp + 0x90]
003943C6  8B 01                           mov eax, dword ptr [rcx]
003943C8  89 01                           mov dword ptr [rcx], eax
003943CA  F6 C3 07                        test bl, 7
003943CD  75 14                           jne 0x1403943e3
003943CF  48 8D 43 18                     lea rax, [rbx + 0x18]
003943D3  49 3B C0                        cmp rax, r8
003943D6  77 05                           ja 0x1403943dd
003943D8  48 3B C3                        cmp rax, rbx
003943DB  73 0B                           jae 0x1403943e8
003943DD  41 0F B6 00                     movzx eax, byte ptr [r8]
003943E1  EB 05                           jmp 0x1403943e8
003943E3  E8 E8 5B 50 00                  call 0x140899fd0
003943E8  0F 10 03                        movups xmm0, xmmword ptr [rbx]
003943EB  0F 11 84 24 B8 00 00 00         movups xmmword ptr [rsp + 0xb8], xmm0
003943F3  F2 0F 10 4B 10                  movsd xmm1, qword ptr [rbx + 0x10]
003943F8  F2 0F 11 8C 24 C8 00 00 00      movsd qword ptr [rsp + 0xc8], xmm1
00394401  EB 46                           jmp 0x140394449
00394403  44 8B F0                        mov r14d, eax
00394406  45 33 ED                        xor r13d, r13d
00394409  44 0F B6 64 24 41               movzx r12d, byte ptr [rsp + 0x41]
0039440F  44 88 64 24 40                  mov byte ptr [rsp + 0x40], r12b
00394414  48 8B BC 24 A0 00 00 00         mov rdi, qword ptr [rsp + 0xa0]
0039441C  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
00394424  48 89 84 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], rax
0039442C  44 8B 7C 24 70                  mov r15d, dword ptr [rsp + 0x70]
00394431  44 89 7C 24 60                  mov dword ptr [rsp + 0x60], r15d
00394436  48 8B 84 24 D0 00 00 00         mov rax, qword ptr [rsp + 0xd0]
0039443E  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
00394446  41 8B F5                        mov esi, r13d
00394449  45 85 F6                        test r14d, r14d
0039444C  0F 88 BB 01 00 00               js 0x14039460d
00394452  4C 8B 05 87 0D C3 00            mov r8, qword ptr [rip + 0xc30d87]
00394459  4C 89 6C 24 78                  mov qword ptr [rsp + 0x78], r13
0039445E  4C 89 6C 24 28                  mov qword ptr [rsp + 0x28], r13
00394463  48 8D 44 24 78                  lea rax, [rsp + 0x78]
00394468  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0039446D  45 0F B6 CC                     movzx r9d, r12b
00394471  41 BC 02 00 00 00               mov r12d, 2
00394477  41 8B D4                        mov edx, r12d
0039447A  48 8B CF                        mov rcx, rdi
0039447D  E8 2E 49 4D 00                  call 0x140868db0
00394482  44 8B F0                        mov r14d, eax
00394485  48 8B 74 24 78                  mov rsi, qword ptr [rsp + 0x78]
0039448A  48 89 74 24 68                  mov qword ptr [rsp + 0x68], rsi
0039448F  85 C0                           test eax, eax
00394491  0F 88 7E 01 00 00               js 0x140394615
00394497  41 83 FF 10                     cmp r15d, 0x10
0039449B  0F 87 A5 09 00 00               ja 0x140394e46
003944A1  48 8B 5E 10                     mov rbx, qword ptr [rsi + 0x10]
003944A5  48 89 5C 24 50                  mov qword ptr [rsp + 0x50], rbx
003944AA  4C 89 6C 24 48                  mov qword ptr [rsp + 0x48], r13
003944AF  90                              nop
003944B0  44 0F 20 C7                     mov rdi, cr8
003944B4  45 0F 22 C4                     mov cr8, r12
003944B8  83 3D 61 28 C3 00 00            cmp dword ptr [rip + 0xc32861], 0
003944BF  0F 85 8C 07 00 00               jne 0x140394c51
003944C5  40 88 7C 24 58                  mov byte ptr [rsp + 0x58], dil
003944CA  F6 05 35 26 C3 00 21            test byte ptr [rip + 0xc32635], 0x21
003944D1  0F 85 01 02 00 00               jne 0x1403946d8
003944D7  48 8D 54 24 48                  lea rdx, [rsp + 0x48]
003944DC  48 87 13                        xchg qword ptr [rbx], rdx
003944DF  48 85 D2                        test rdx, rdx
003944E2  0F 85 CB 07 00 00               jne 0x140394cb3
003944E8  48 8B 74 24 78                  mov rsi, qword ptr [rsp + 0x78]
003944ED  4C 8D 7E 10                     lea r15, [rsi + 0x10]
003944F1  49 8B 0F                        mov rcx, qword ptr [r15]
003944F4  80 79 21 00                     cmp byte ptr [rcx + 0x21], 0
003944F8  0F 85 2E 09 00 00               jne 0x140394e2c
003944FE  8B 86 98 01 00 00               mov eax, dword ptr [rsi + 0x198]
00394504  0F BA E0 09                     bt eax, 9
00394508  73 3B                           jae 0x140394545
0039450A  0F BA E0 0A                     bt eax, 0xa
0039450E  73 2B                           jae 0x14039453b
00394510  48 8B 49 08                     mov rcx, qword ptr [rcx + 8]
00394514  48 8D 96 68 02 00 00            lea rdx, [rsi + 0x268]
0039451B  E8 1C 0A 00 00                  call 0x140394f3c
00394520  84 C0                           test al, al
00394522  74 17                           je 0x14039453b
00394524  BA 44 66 6C 74                  mov edx, 0x746c6644
00394529  48 8B CE                        mov rcx, rsi
0039452C  E8 AF 33 F6 FF                  call 0x1402f78e0
00394531  81 A6 98 01 00 00 FF FB FF FF   and dword ptr [rsi + 0x198], 0xfffffbff
0039453B  81 A6 98 01 00 00 FF FD FF FF   and dword ptr [rsi + 0x198], 0xfffffdff
00394545  49 8B 07                        mov rax, qword ptr [r15]
00394548  FF 40 1C                        inc dword ptr [rax + 0x1c]
0039454B  48 8D 8E 7C 01 00 00            lea rcx, [rsi + 0x17c]
00394552  48 89 8C 24 88 00 00 00         mov qword ptr [rsp + 0x88], rcx
0039455A  48 8D 86 80 01 00 00            lea rax, [rsi + 0x180]
00394561  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00394566  49 C7 C4 FF FF FF FF            mov r12, 0xffffffffffffffff
0039456D  8B 00                           mov eax, dword ptr [rax]
0039456F  39 01                           cmp dword ptr [rcx], eax
00394571  0F 82 2B 06 00 00               jb 0x140394ba2
00394577  49 8B 07                        mov rax, qword ptr [r15]
0039457A  80 78 21 00                     cmp byte ptr [rax + 0x21], 0
0039457E  0F 85 1E 06 00 00               jne 0x140394ba2
00394584  F6 05 7B 25 C3 00 01            test byte ptr [rip + 0xc3257b], 1
0039458B  0F 85 67 01 00 00               jne 0x1403946f8
00394591  0F 0D 4C 24 48                  prefetchw byte ptr [rsp + 0x48]
00394596  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
0039459B  48 85 C0                        test rax, rax
0039459E  75 27                           jne 0x1403945c7
003945A0  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
003945A5  48 8D 44 24 48                  lea rax, [rsp + 0x48]
003945AA  F0 4C 0F B1 29                  lock cmpxchg qword ptr [rcx], r13
003945AF  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
003945B4  48 3B C1                        cmp rax, rcx
003945B7  0F 84 5B 01 00 00               je 0x140394718
003945BD  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
003945C2  E8 D9 34 E8 FF                  call 0x140217aa0
003945C7  4C 89 6C 24 48                  mov qword ptr [rsp + 0x48], r13
003945CC  48 8B 54 24 50                  mov rdx, qword ptr [rsp + 0x50]
003945D1  48 8D 48 08                     lea rcx, [rax + 8]
003945D5  48 8B C2                        mov rax, rdx
003945D8  48 87 01                        xchg qword ptr [rcx], rax
003945DB  32 C2                           xor al, dl
003945DD  A8 04                           test al, 4
003945DF  0F 84 33 01 00 00               je 0x140394718
003945E5  E8 36 36 E8 FF                  call 0x140217c20
003945EA  E9 29 01 00 00                  jmp 0x140394718
003945EF  0F 10 03                        movups xmm0, xmmword ptr [rbx]
003945F2  0F 11 84 24 B8 00 00 00         movups xmmword ptr [rsp + 0xb8], xmm0
003945FA  F2 0F 10 4B 10                  movsd xmm1, qword ptr [rbx + 0x10]
003945FF  F2 0F 11 8C 24 C8 00 00 00      movsd qword ptr [rsp + 0xc8], xmm1
00394608  E9 45 FE FF FF                  jmp 0x140394452
0039460D  44 89 AC 24 CC 00 00 00         mov dword ptr [rsp + 0xcc], r13d
00394615  48 8D 3D E4 B9 C6 FF            lea rdi, [rip - 0x39461c]
0039461C  49 C7 C4 FF FF FF FF            mov r12, 0xffffffffffffffff
00394623  41 BF 02 00 00 00               mov r15d, 2
00394629  48 8D 8C 24 30 01 00 00         lea rcx, [rsp + 0x130]
00394631  48 8B 84 24 98 00 00 00         mov rax, qword ptr [rsp + 0x98]
00394639  48 3B C1                        cmp rax, rcx
0039463C  74 0A                           je 0x140394648
0039463E  33 D2                           xor edx, edx
00394640  48 8B C8                        mov rcx, rax
00394643  E8 28 E2 7E 00                  call 0x140b82870
00394648  48 85 F6                        test rsi, rsi
0039464B  74 2A                           je 0x140394677
0039464D  83 3D BC 09 C3 00 00            cmp dword ptr [rip + 0xc309bc], 0
00394654  74 15                           je 0x14039466b
00394656  33 D2                           xor edx, edx
00394658  41 B9 44 66 6C 74               mov r9d, 0x746c6644
0039465E  44 8D 42 01                     lea r8d, [rdx + 1]
00394662  48 8D 4E D0                     lea rcx, [rsi - 0x30]
00394666  E8 79 C3 E7 FF                  call 0x1402109e4
0039466B  F0 4C 0F C1 66 D0               lock xadd qword ptr [rsi - 0x30], r12
00394671  49 83 EC 01                     sub r12, 1
00394675  7E 35                           jle 0x1403946ac
00394677  F6 84 24 CC 00 00 00 01         test byte ptr [rsp + 0xcc], 1
0039467F  0F 85 06 08 00 00               jne 0x140394e8b
00394685  41 8B C6                        mov eax, r14d
00394688  48 8B 8C 24 B0 01 00 00         mov rcx, qword ptr [rsp + 0x1b0]
00394690  48 33 CC                        xor rcx, rsp
00394693  E8 A8 7F 31 00                  call 0x1406ac640
00394698  48 81 C4 C0 01 00 00            add rsp, 0x1c0
0039469F  41 5F                           pop r15
003946A1  41 5E                           pop r14
003946A3  41 5D                           pop r13
003946A5  41 5C                           pop r12
003946A7  5F                              pop rdi
003946A8  5E                              pop rsi
003946A9  5B                              pop rbx
003946AA  C3                              ret
003946AB  CC                              int3
003946AC  48 8B 4E D8                     mov rcx, qword ptr [rsi - 0x28]
003946B0  48 85 C9                        test rcx, rcx
003946B3  0F 85 F4 04 00 00               jne 0x140394bad
003946B9  4D 85 E4                        test r12, r12
003946BC  0F 89 D6 06 00 00               jns 0x140394d98
003946C2  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
003946C7  4D 8B CF                        mov r9, r15
003946CA  4C 8B C6                        mov r8, rsi
003946CD  33 D2                           xor edx, edx
003946CF  8D 4A 18                        lea ecx, [rdx + 0x18]
003946D2  E8 89 8F 16 00                  call 0x1404fd660
003946D7  CC                              int3
003946D8  8B 05 7A 97 B7 00               mov eax, dword ptr [rip + 0xb7977a]
003946DE  85 C0                           test eax, eax
003946E0  0F 85 F1 FD FF FF               jne 0x1403944d7
003946E6  48 8B D3                        mov rdx, rbx
003946E9  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
003946EE  E8 5D 11 EE FF                  call 0x140275850
003946F3  E9 F0 FD FF FF                  jmp 0x1403944e8
003946F8  8B 05 5A 97 B7 00               mov eax, dword ptr [rip + 0xb7975a]
003946FE  85 C0                           test eax, eax
00394700  0F 85 8B FE FF FF               jne 0x140394591
00394706  48 8B 94 24 F8 01 00 00         mov rdx, qword ptr [rsp + 0x1f8]
0039470E  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
00394713  E8 D8 32 E8 FF                  call 0x1402179f0
00394718  0F B6 5C 24 58                  movzx ebx, byte ptr [rsp + 0x58]
0039471D  83 3D FC 25 C3 00 00            cmp dword ptr [rip + 0xc325fc], 0
00394724  74 0C                           je 0x140394732
00394726  44 0F 20 C1                     mov rcx, cr8
0039472A  0F B6 D3                        movzx edx, bl
0039472D  E8 66 0F 16 00                  call 0x1404f5698
00394732  44 0F 22 C3                     mov cr8, rbx
00394736  8B 84 24 CC 00 00 00            mov eax, dword ptr [rsp + 0xcc]
0039473D  A8 01                           test al, 1
0039473F  0F 84 65 01 00 00               je 0x1403948aa
00394745  48 8B B4 24 B8 00 00 00         mov rsi, qword ptr [rsp + 0xb8]
0039474D  8B 9C 24 C8 00 00 00            mov ebx, dword ptr [rsp + 0xc8]
00394754  48 8B 8C 24 C0 00 00 00         mov rcx, qword ptr [rsp + 0xc0]
0039475C  0F 57 C0                        xorps xmm0, xmm0
0039475F  0F 11 84 24 F0 00 00 00         movups xmmword ptr [rsp + 0xf0], xmm0
00394767  0F 11 84 24 00 01 00 00         movups xmmword ptr [rsp + 0x100], xmm0
0039476F  0F 11 84 24 10 01 00 00         movups xmmword ptr [rsp + 0x110], xmm0
00394777  0F 11 84 24 20 01 00 00         movups xmmword ptr [rsp + 0x120], xmm0
0039477F  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00394788  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
0039478F  90                              nop
00394790  0F 11 84 24 A8 00 00 00         movups xmmword ptr [rsp + 0xa8], xmm0
00394798  81 E3 00 00 FF FF               and ebx, 0xffff0000
0039479E  0F BA E3 11                     bt ebx, 0x11
003947A2  0F 82 ED 00 00 00               jb 0x140394895
003947A8  4C 8B 05 69 24 C3 00            mov r8, qword ptr [rip + 0xc32469]
003947AF  4C 89 AC 24 80 00 00 00         mov qword ptr [rsp + 0x80], r13
003947B7  4C 89 6C 24 28                  mov qword ptr [rsp + 0x28], r13
003947BC  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
003947C4  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
003947C9  44 0F B6 4C 24 40               movzx r9d, byte ptr [rsp + 0x40]
003947CF  BA 01 00 00 00                  mov edx, 1
003947D4  E8 D7 45 4D 00                  call 0x140868db0
003947D9  85 C0                           test eax, eax
003947DB  0F 88 B4 00 00 00               js 0x140394895
003947E1  0F BA E3 12                     bt ebx, 0x12
003947E5  0F 83 34 06 00 00               jae 0x140394e1f
003947EB  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
003947F3  BF 01 00 00 00                  mov edi, 1
003947F8  F0 0F C1 B8 94 01 00 00         lock xadd dword ptr [rax + 0x194], edi
00394800  FF C7                           inc edi
00394802  4C 8B B4 24 80 00 00 00         mov r14, qword ptr [rsp + 0x80]
0039480A  49 83 BE 98 01 00 00 00         cmp qword ptr [r14 + 0x198], 0
00394812  0F 85 B9 06 00 00               jne 0x140394ed1
00394818  4C 89 B4 24 F0 00 00 00         mov qword ptr [rsp + 0xf0], r14
00394820  83 CB 04                        or ebx, 4
00394823  89 9C 24 20 01 00 00            mov dword ptr [rsp + 0x120], ebx
0039482A  4C 89 AC 24 10 01 00 00         mov qword ptr [rsp + 0x110], r13
00394832  4C 89 AC 24 08 01 00 00         mov qword ptr [rsp + 0x108], r13
0039483A  4C 89 AC 24 18 01 00 00         mov qword ptr [rsp + 0x118], r13
00394842  44 0F B6 4C 24 40               movzx r9d, byte ptr [rsp + 0x40]
00394848  45 33 C0                        xor r8d, r8d
0039484B  48 8B D6                        mov rdx, rsi
0039484E  48 8D 8C 24 F0 00 00 00         lea rcx, [rsp + 0xf0]
00394856  E8 E5 74 4F 00                  call 0x14088bd40
0039485B  85 C0                           test eax, eax
0039485D  0F 88 C1 06 00 00               js 0x140394f24
00394863  48 8B 84 24 10 01 00 00         mov rax, qword ptr [rsp + 0x110]
0039486B  48 89 84 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rax
00394873  48 8B 84 24 F0 00 00 00         mov rax, qword ptr [rsp + 0xf0]
0039487B  48 89 84 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rax
00394883  45 33 C0                        xor r8d, r8d
00394886  B2 01                           mov dl, 1
00394888  48 8D 8C 24 F0 00 00 00         lea rcx, [rsp + 0xf0]
00394890  E8 4B 0D 00 00                  call 0x1403955e0
00394895  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0039489E  E8 4D A7 EC FF                  call 0x14025eff0
003948A3  8B 84 24 CC 00 00 00            mov eax, dword ptr [rsp + 0xcc]
003948AA  A8 02                           test al, 2
003948AC  74 43                           je 0x1403948f1
003948AE  65 48 8B 1C 25 88 01 00 00      mov rbx, qword ptr gs:[0x188]
003948B7  8B 43 74                        mov eax, dword ptr [rbx + 0x74]
003948BA  A8 04                           test al, 4
003948BC  75 25                           jne 0x1403948e3
003948BE  44 0F 20 C7                     mov rdi, cr8
003948C2  B8 02 00 00 00                  mov eax, 2
003948C7  44 0F 22 C0                     mov cr8, rax
003948CB  83 3D 4E 24 C3 00 00            cmp dword ptr [rip + 0xc3244e], 0
003948D2  0F 85 9C 03 00 00               jne 0x140394c74
003948D8  40 88 BB 86 01 00 00            mov byte ptr [rbx + 0x186], dil
003948DF  83 4B 74 04                     or dword ptr [rbx + 0x74], 4
003948E3  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
003948EC  E8 7F 07 00 00                  call 0x140395070
003948F1  49 8B 0F                        mov rcx, qword ptr [r15]
003948F4  C6 44 24 38 01                  mov byte ptr [rsp + 0x38], 1
003948F9  4C 89 6C 24 30                  mov qword ptr [rsp + 0x30], r13
003948FE  0F B6 44 24 40                  movzx eax, byte ptr [rsp + 0x40]
00394903  88 44 24 28                     mov byte ptr [rsp + 0x28], al
00394907  48 8D 44 24 64                  lea rax, [rsp + 0x64]
0039490C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00394911  44 8B 4C 24 60                  mov r9d, dword ptr [rsp + 0x60]
00394916  4C 8B 84 24 98 00 00 00         mov r8, qword ptr [rsp + 0x98]
0039491E  48 8B 94 24 D8 00 00 00         mov rdx, qword ptr [rsp + 0xd8]
00394926  48 8B 49 08                     mov rcx, qword ptr [rcx + 8]
0039492A  E8 51 6C E7 FF                  call 0x14020b580
0039492F  44 8B F0                        mov r14d, eax
00394932  48 8D 8C 24 A8 00 00 00         lea rcx, [rsp + 0xa8]
0039493A  E8 C1 06 00 00                  call 0x140395000
0039493F  49 8B 1F                        mov rbx, qword ptr [r15]
00394942  48 89 5C 24 50                  mov qword ptr [rsp + 0x50], rbx
00394947  4C 89 6C 24 48                  mov qword ptr [rsp + 0x48], r13
0039494C  90                              nop
0039494D  44 0F 20 C7                     mov rdi, cr8
00394951  B8 02 00 00 00                  mov eax, 2
00394956  44 0F 22 C0                     mov cr8, rax
0039495A  83 3D BF 23 C3 00 00            cmp dword ptr [rip + 0xc323bf], 0
00394961  0F 85 FC 02 00 00               jne 0x140394c63
00394967  40 88 7C 24 58                  mov byte ptr [rsp + 0x58], dil
0039496C  F6 05 93 21 C3 00 21            test byte ptr [rip + 0xc32193], 0x21
00394973  0F 85 09 02 00 00               jne 0x140394b82
00394979  48 8D 54 24 48                  lea rdx, [rsp + 0x48]
0039497E  48 87 13                        xchg qword ptr [rbx], rdx
00394981  48 85 D2                        test rdx, rdx
00394984  0F 85 54 03 00 00               jne 0x140394cde
0039498A  48 8B 74 24 78                  mov rsi, qword ptr [rsp + 0x78]
0039498F  41 81 FE 02 01 00 00            cmp r14d, 0x102
00394996  0F 84 79 03 00 00               je 0x140394d15
0039499C  48 8B 46 10                     mov rax, qword ptr [rsi + 0x10]
003949A0  FF 48 1C                        dec dword ptr [rax + 0x1c]
003949A3  41 81 FE 02 01 00 00            cmp r14d, 0x102
003949AA  0F 84 CF 03 00 00               je 0x140394d7f
003949B0  8B 86 98 01 00 00               mov eax, dword ptr [rsi + 0x198]
003949B6  24 07                           and al, 7
003949B8  3C 04                           cmp al, 4
003949BA  74 5D                           je 0x140394a19
003949BC  65 4C 8B 3C 25 88 01 00 00      mov r15, qword ptr gs:[0x188]
003949C5  41 8B C5                        mov eax, r13d
003949C8  48 8B 74 24 78                  mov rsi, qword ptr [rsp + 0x78]
003949CD  83 F8 04                        cmp eax, 4
003949D0  0F 83 AF 02 00 00               jae 0x140394c85
003949D6  8B C8                           mov ecx, eax
003949D8  4C 39 7C CE 48                  cmp qword ptr [rsi + rcx*8 + 0x48], r15
003949DD  74 3A                           je 0x140394a19
003949DF  FF C0                           inc eax
003949E1  EB EA                           jmp 0x1403949cd
003949E3  8B BE 98 01 00 00               mov edi, dword ptr [rsi + 0x198]
003949E9  83 E7 07                        and edi, 7
003949EC  48 8D 1C FE                     lea rbx, [rsi + rdi*8]
003949F0  48 8B 4B 48                     mov rcx, qword ptr [rbx + 0x48]
003949F4  BA 44 66 6C 74                  mov edx, 0x746c6644
003949F9  E8 E2 2E F6 FF                  call 0x1402f78e0
003949FE  4C 89 7B 48                     mov qword ptr [rbx + 0x48], r15
00394A02  8D 4F 01                        lea ecx, [rdi + 1]
00394A05  83 E1 03                        and ecx, 3
00394A08  8B 86 98 01 00 00               mov eax, dword ptr [rsi + 0x198]
00394A0E  83 E0 F8                        and eax, 0xfffffff8
00394A11  0B C8                           or ecx, eax
00394A13  89 8E 98 01 00 00               mov dword ptr [rsi + 0x198], ecx
00394A19  48 8B 5E 10                     mov rbx, qword ptr [rsi + 0x10]
00394A1D  8B 86 7C 01 00 00               mov eax, dword ptr [rsi + 0x17c]
00394A23  39 86 80 01 00 00               cmp dword ptr [rsi + 0x180], eax
00394A29  73 0A                           jae 0x140394a35
00394A2B  83 7B 1C 00                     cmp dword ptr [rbx + 0x1c], 0
00394A2F  0F 84 B4 01 00 00               je 0x140394be9
00394A35  F6 05 CA 20 C3 00 01            test byte ptr [rip + 0xc320ca], 1
00394A3C  0F 85 9C 00 00 00               jne 0x140394ade
00394A42  0F 0D 4C 24 48                  prefetchw byte ptr [rsp + 0x48]
00394A47  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00394A4C  48 85 C0                        test rax, rax
00394A4F  75 27                           jne 0x140394a78
00394A51  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00394A56  48 8D 44 24 48                  lea rax, [rsp + 0x48]
00394A5B  F0 4C 0F B1 29                  lock cmpxchg qword ptr [rcx], r13
00394A60  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
00394A65  48 3B C1                        cmp rax, rcx
00394A68  0F 84 90 00 00 00               je 0x140394afe
00394A6E  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
00394A73  E8 28 30 E8 FF                  call 0x140217aa0
00394A78  4C 89 6C 24 48                  mov qword ptr [rsp + 0x48], r13
00394A7D  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00394A82  4C 8D 40 08                     lea r8, [rax + 8]
00394A86  48 8B C1                        mov rax, rcx
00394A89  49 87 00                        xchg qword ptr [r8], rax
00394A8C  32 C1                           xor al, cl
00394A8E  A8 04                           test al, 4
00394A90  74 6C                           je 0x140394afe
00394A92  F0 83 0C 24 00                  lock or dword ptr [rsp], 0
00394A97  49 C1 E8 05                     shr r8, 5
00394A9B  41 83 E0 7F                     and r8d, 0x7f
00394A9F  48 8D 3D 5A B5 C6 FF            lea rdi, [rip - 0x394aa6]
00394AA6  E8 35 31 E8 FF                  call 0x140217be0
00394AAB  0F B6 D8                        movzx ebx, al
00394AAE  49 8B D5                        mov rdx, r13
00394AB1  4A 87 94 C7 20 1B F2 00         xchg qword ptr [rdi + r8*8 + 0xf21b20], rdx
00394AB9  E8 36 30 E8 FF                  call 0x140217af4
00394ABE  84 DB                           test bl, bl
00394AC0  74 43                           je 0x140394b05
00394AC2  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
00394ACB  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
00394AD2  4D 85 C0                        test r8, r8
00394AD5  0F 85 12 02 00 00               jne 0x140394ced
00394ADB  FB                              sti
00394ADC  EB 27                           jmp 0x140394b05
00394ADE  8B 05 74 93 B7 00               mov eax, dword ptr [rip + 0xb79374]
00394AE4  85 C0                           test eax, eax
00394AE6  0F 85 56 FF FF FF               jne 0x140394a42
00394AEC  48 8B 94 24 F8 01 00 00         mov rdx, qword ptr [rsp + 0x1f8]
00394AF4  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
00394AF9  E8 F2 2E E8 FF                  call 0x1402179f0
00394AFE  48 8D 3D FB B4 C6 FF            lea rdi, [rip - 0x394b05]
00394B05  0F B6 5C 24 58                  movzx ebx, byte ptr [rsp + 0x58]
00394B0A  83 3D 0F 22 C3 00 00            cmp dword ptr [rip + 0xc3220f], 0
00394B11  74 0C                           je 0x140394b1f
00394B13  44 0F 20 C1                     mov rcx, cr8
00394B17  0F B6 D3                        movzx edx, bl
00394B1A  E8 79 0B 16 00                  call 0x1404f5698
00394B1F  44 0F 22 C3                     mov cr8, rbx
00394B23  45 85 F6                        test r14d, r14d
00394B26  75 50                           jne 0x140394b78
00394B28  44 38 74 24 40                  cmp byte ptr [rsp + 0x40], r14b
00394B2D  74 3B                           je 0x140394b6a
00394B2F  8B 44 24 64                     mov eax, dword ptr [rsp + 0x64]
00394B33  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
00394B3B  89 01                           mov dword ptr [rcx], eax
00394B3D  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
00394B42  45 8D 7E 02                     lea r15d, [r14 + 2]
00394B46  E9 DE FA FF FF                  jmp 0x140394629
00394B4B  44 8B F0                        mov r14d, eax
00394B4E  45 33 ED                        xor r13d, r13d
00394B51  45 8D 7D 02                     lea r15d, [r13 + 2]
00394B55  4D 8D 65 FF                     lea r12, [r13 - 1]
00394B59  48 8D 3D A0 B4 C6 FF            lea rdi, [rip - 0x394b60]
00394B60  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
00394B65  E9 BF FA FF FF                  jmp 0x140394629
00394B6A  8B 44 24 64                     mov eax, dword ptr [rsp + 0x64]
00394B6E  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
00394B76  89 01                           mov dword ptr [rcx], eax
00394B78  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
00394B7D  E9 A1 FA FF FF                  jmp 0x140394623
00394B82  8B 05 D0 92 B7 00               mov eax, dword ptr [rip + 0xb792d0]
00394B88  85 C0                           test eax, eax
00394B8A  0F 85 E9 FD FF FF               jne 0x140394979
00394B90  48 8B D3                        mov rdx, rbx
00394B93  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
00394B98  E8 B3 0C EE FF                  call 0x140275850
00394B9D  E9 E8 FD FF FF                  jmp 0x14039498a
00394BA2  41 BE 02 01 00 00               mov r14d, 0x102
00394BA8  E9 EF FD FF FF                  jmp 0x14039499c
00394BAD  48 8D 46 D0                     lea rax, [rsi - 0x30]
00394BB1  48 C1 E8 08                     shr rax, 8
00394BB5  0F B6 D0                        movzx edx, al
00394BB8  0F B6 46 E8                     movzx eax, byte ptr [rsi - 0x18]
00394BBC  48 33 D0                        xor rdx, rax
00394BBF  0F B6 05 86 22 C3 00            movzx eax, byte ptr [rip + 0xc32286]
00394BC6  48 33 D0                        xor rdx, rax
00394BC9  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00394BCE  41 B9 01 00 00 00               mov r9d, 1
00394BD4  4C 8B C6                        mov r8, rsi
00394BD7  48 8B 94 D7 00 78 FC 00         mov rdx, qword ptr [rdi + rdx*8 + 0xfc7800]
00394BDF  41 8D 49 17                     lea ecx, [r9 + 0x17]
00394BE3  E8 78 8A 16 00                  call 0x1404fd660
00394BE8  CC                              int3
00394BE9  83 BE 94 01 00 00 00            cmp dword ptr [rsi + 0x194], 0
00394BF0  0F 84 CC 00 00 00               je 0x140394cc2
00394BF6  8B 8E 98 01 00 00               mov ecx, dword ptr [rsi + 0x198]
00394BFC  0F BA E9 09                     bts ecx, 9
00394C00  89 8E 98 01 00 00               mov dword ptr [rsi + 0x198], ecx
00394C06  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
00394C0A  83 78 04 00                     cmp dword ptr [rax + 4], 0
00394C0E  0F 85 AE 00 00 00               jne 0x140394cc2
00394C14  0F BA E1 0A                     bt ecx, 0xa
00394C18  0F 82 17 FE FF FF               jb 0x140394a35
00394C1E  0F BA E9 0A                     bts ecx, 0xa
00394C22  89 8E 98 01 00 00               mov dword ptr [rsi + 0x198], ecx
00394C28  BA 44 66 6C 74                  mov edx, 0x746c6644
00394C2D  48 8B CE                        mov rcx, rsi
00394C30  E8 DB BA E7 FF                  call 0x140210710
00394C35  4C 8D 86 68 02 00 00            lea r8, [rsi + 0x268]
00394C3C  48 8D 15 5D 55 B6 00            lea rdx, [rip + 0xb6555d]
00394C43  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
00394C47  E8 08 E8 FF FF                  call 0x140393454
00394C4C  E9 E4 FD FF FF                  jmp 0x140394a35
00394C51  41 0F B6 D4                     movzx edx, r12b
00394C55  40 0F B6 CF                     movzx ecx, dil
00394C59  E8 9E 0A 16 00                  call 0x1404f56fc
00394C5E  E9 62 F8 FF FF                  jmp 0x1403944c5
00394C63  0F B6 D0                        movzx edx, al
00394C66  40 0F B6 CF                     movzx ecx, dil
00394C6A  E8 8D 0A 16 00                  call 0x1404f56fc
00394C6F  E9 F3 FC FF FF                  jmp 0x140394967
00394C74  0F B6 D0                        movzx edx, al
00394C77  40 0F B6 CF                     movzx ecx, dil
00394C7B  E8 7C 0A 16 00                  call 0x1404f56fc
00394C80  E9 53 FC FF FF                  jmp 0x1403948d8
00394C85  BA 44 66 6C 74                  mov edx, 0x746c6644
00394C8A  49 8B CF                        mov rcx, r15
00394C8D  E8 7E BA E7 FF                  call 0x140210710
00394C92  41 8B CD                        mov ecx, r13d
00394C95  83 F9 04                        cmp ecx, 4
00394C98  0F 83 45 FD FF FF               jae 0x1403949e3
00394C9E  8B C1                           mov eax, ecx
00394CA0  48 8D 14 C6                     lea rdx, [rsi + rax*8]
00394CA4  48 83 7A 48 00                  cmp qword ptr [rdx + 0x48], 0
00394CA9  0F 84 C7 00 00 00               je 0x140394d76
00394CAF  FF C1                           inc ecx
00394CB1  EB E2                           jmp 0x140394c95
00394CB3  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
00394CB8  E8 F3 31 EC FF                  call 0x140257eb0
00394CBD  E9 26 F8 FF FF                  jmp 0x1403944e8
00394CC2  45 33 C0                        xor r8d, r8d
00394CC5  48 8D 54 24 48                  lea rdx, [rsp + 0x48]
00394CCA  48 8B CE                        mov rcx, rsi
00394CCD  E8 8E F7 FA FF                  call 0x140344460
00394CD2  48 8D 3D 27 B3 C6 FF            lea rdi, [rip - 0x394cd9]
00394CD9  E9 45 FE FF FF                  jmp 0x140394b23
00394CDE  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
00394CE3  E8 C8 31 EC FF                  call 0x140257eb0
00394CE8  E9 9D FC FF FF                  jmp 0x14039498a
00394CED  41 0F 0D 08                     prefetchw byte ptr [r8]
00394CF1  41 8B 00                        mov eax, dword ptr [r8]
00394CF4  8B D0                           mov edx, eax
00394CF6  0F BA F2 15                     btr edx, 0x15
00394CFA  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
00394CFF  75 F3                           jne 0x140394cf4
00394D01  0F BA E0 15                     bt eax, 0x15
00394D05  0F 83 D0 FD FF FF               jae 0x140394adb
00394D0B  E8 C0 E4 EC FF                  call 0x1402631d0
00394D10  E9 C6 FD FF FF                  jmp 0x140394adb
00394D15  BA 01 00 00 00                  mov edx, 1
00394D1A  48 8B CE                        mov rcx, rsi
00394D1D  E8 12 DA 0B 00                  call 0x140452734
00394D22  84 C0                           test al, al
00394D24  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
00394D29  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00394D31  0F 85 36 F8 FF FF               jne 0x14039456d
00394D37  8B 86 78 01 00 00               mov eax, dword ptr [rsi + 0x178]
00394D3D  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
00394D42  39 01                           cmp dword ptr [rcx], eax
00394D44  48 8B C1                        mov rax, rcx
00394D47  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00394D4F  0F 86 18 F8 FF FF               jbe 0x14039456d
00394D55  48 8B 84 24 E0 00 00 00         mov rax, qword ptr [rsp + 0xe0]
00394D5D  48 05 40 05 00 00               add rax, 0x540
00394D63  48 39 00                        cmp qword ptr [rax], rax
00394D66  0F 84 30 FC FF FF               je 0x14039499c
00394D6C  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
00394D71  E9 F7 F7 FF FF                  jmp 0x14039456d
00394D76  4C 89 7A 48                     mov qword ptr [rdx + 0x48], r15
00394D7A  E9 9A FC FF FF                  jmp 0x140394a19
00394D7F  FF 8E 80 01 00 00               dec dword ptr [rsi + 0x180]
00394D85  FF 8E 84 01 00 00               dec dword ptr [rsi + 0x184]
00394D8B  48 8B CE                        mov rcx, rsi
00394D8E  E8 C1 E3 0E 00                  call 0x140483154
00394D93  E9 81 FC FF FF                  jmp 0x140394a19
00394D98  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00394DA1  66 83 B8 E6 01 00 00 00         cmp word ptr [rax + 0x1e6], 0
00394DA9  0F 85 14 01 00 00               jne 0x140394ec3
00394DAF  E8 AC 32 F6 FF                  call 0x1402f8060
00394DB4  84 C0                           test al, al
00394DB6  0F 84 07 01 00 00               je 0x140394ec3
00394DBC  44 0F 20 C0                     mov rax, cr8
00394DC0  3C 01                           cmp al, 1
00394DC2  0F 83 FB 00 00 00               jae 0x140394ec3
00394DC8  0F B6 46 EA                     movzx eax, byte ptr [rsi - 0x16]
00394DCC  A8 40                           test al, 0x40
00394DCE  75 22                           jne 0x140394df2
00394DD0  83 3D 39 02 C3 00 00            cmp dword ptr [rip + 0xc30239], 0
00394DD7  74 09                           je 0x140394de2
00394DD9  48 8D 4E D0                     lea rcx, [rsi - 0x30]
00394DDD  E8 96 31 64 00                  call 0x1409d7f78
00394DE2  33 D2                           xor edx, edx
00394DE4  48 8D 4E D0                     lea rcx, [rsi - 0x30]
00394DE8  E8 73 FC 4C 00                  call 0x140864a60
00394DED  E9 85 F8 FF FF                  jmp 0x140394677
00394DF2  83 E0 7F                        and eax, 0x7f
00394DF5  0F B6 84 38 80 FF F0 00         movzx eax, byte ptr [rax + rdi + 0xf0ff80]
00394DFD  48 8D 4E D0                     lea rcx, [rsi - 0x30]
00394E01  48 2B C8                        sub rcx, rax
00394E04  48 8B 09                        mov rcx, qword ptr [rcx]
00394E07  80 79 18 00                     cmp byte ptr [rcx + 0x18], 0
00394E0B  74 C3                           je 0x140394dd0
00394E0D  E8 1E 30 64 00                  call 0x1409d7e30
00394E12  EB BC                           jmp 0x140394dd0
00394E14  41 BE 0D 00 00 C0               mov r14d, 0xc000000d
00394E1A  E9 F6 F7 FF FF                  jmp 0x140394615
00394E1F  4C 8B B4 24 80 00 00 00         mov r14, qword ptr [rsp + 0x80]
00394E27  E9 EC F9 FF FF                  jmp 0x140394818
00394E2C  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
00394E31  E8 AA DE FA FF                  call 0x140342ce0
00394E36  41 BE 80 00 00 00               mov r14d, 0x80
00394E3C  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
00394E41  E9 CF F7 FF FF                  jmp 0x140394615
00394E46  41 8B D7                        mov edx, r15d
00394E49  48 C1 E2 03                     shl rdx, 3
00394E4D  B9 40 00 00 00                  mov ecx, 0x40
00394E52  41 B8 4E 6F 6E 65               mov r8d, 0x656e6f4e
00394E58  E8 93 D2 7E 00                  call 0x140b820f0
00394E5D  48 89 84 24 98 00 00 00         mov qword ptr [rsp + 0x98], rax
00394E65  48 85 C0                        test rax, rax
00394E68  0F 85 33 F6 FF FF               jne 0x1403944a1
00394E6E  C7 44 24 60 10 00 00 00         mov dword ptr [rsp + 0x60], 0x10
00394E76  48 8D 84 24 30 01 00 00         lea rax, [rsp + 0x130]
00394E7E  48 89 84 24 98 00 00 00         mov qword ptr [rsp + 0x98], rax
00394E86  E9 16 F6 FF FF                  jmp 0x1403944a1
00394E8B  4C 89 6C 24 38                  mov qword ptr [rsp + 0x38], r13
00394E90  4C 89 6C 24 30                  mov qword ptr [rsp + 0x30], r13
00394E95  4C 89 6C 24 28                  mov qword ptr [rsp + 0x28], r13
00394E9A  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00394E9F  45 33 C9                        xor r9d, r9d
00394EA2  4C 8B 84 24 B8 00 00 00         mov r8, qword ptr [rsp + 0xb8]
00394EAA  8B 94 24 C8 00 00 00            mov edx, dword ptr [rsp + 0xc8]
00394EB1  48 8B 8C 24 C0 00 00 00         mov rcx, qword ptr [rsp + 0xc0]
00394EB9  E8 82 31 4D 00                  call 0x140868040
00394EBE  E9 C2 F7 FF FF                  jmp 0x140394685
00394EC3  48 8D 4E D0                     lea rcx, [rsi - 0x30]
00394EC7  E8 C8 D4 00 00                  call 0x1403a2394
00394ECC  E9 A6 F7 FF FF                  jmp 0x140394677
00394ED1  49 8D 8E 60 01 00 00            lea rcx, [r14 + 0x160]
00394ED8  48 89 8C 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rcx
00394EE0  45 33 C0                        xor r8d, r8d
00394EE3  33 D2                           xor edx, edx
00394EE5  E8 46 B3 E7 FF                  call 0x140210230
00394EEA  48 89 84 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], rax
00394EF2  49 8D 8E 60 01 00 00            lea rcx, [r14 + 0x160]
00394EF9  F0 48 0F BA 29 00               lock bts qword ptr [rcx], 0
00394EFF  0F 83 81 0A 35 00               jae 0x1406e5986
00394F05  4C 8B C1                        mov r8, rcx
00394F08  48 8B D0                        mov rdx, rax
00394F0B  E8 80 AD E7 FF                  call 0x14020fc90
00394F10  49 8D 8E 60 01 00 00            lea rcx, [r14 + 0x160]
00394F17  48 8B 84 24 D0 00 00 00         mov rax, qword ptr [rsp + 0xd0]
00394F1F  E9 62 0A 35 00                  jmp 0x1406e5986
00394F24  48 8B 8C 24 F0 00 00 00         mov rcx, qword ptr [rsp + 0xf0]
00394F2C  E8 1F 44 F6 FF                  call 0x1402f9350
00394F31  E9 5F F9 FF FF                  jmp 0x140394895
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtWaitForWorkViaWorkerFactory(__int64 a1, __int64 a2, int a3, __int64 a4, __int64 a5)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned int v_stack_m12C;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned __int64 v_stack_m180;
    unsigned int v_stack_m188;
    unsigned __int64 v_stack_m190;
    unsigned int v_stack_m194;
    unsigned int v_stack_m198;
    unsigned __int64 v_stack_m1A0;
    unsigned __int64 v_stack_m1A8;
    unsigned __int64 v_stack_m1B0;
    unsigned __int8 v_stack_m1B7;
    unsigned __int8 v_stack_m1B8;
    unsigned __int64 v_stack_m1D0;
    unsigned __int64 v_stack_m1D8;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC8;
    unsigned int v_stack_p0;
    unsigned __int64 v_stack_p100;
    unsigned __int64 v_stack_p108;
    unsigned __int64 v_stack_p110;
    unsigned __int64 v_stack_p118;
    unsigned __int64 v_stack_p120;
    unsigned __int64 v_stack_p130;
    unsigned __int64 v_stack_p1F8;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int8 v_stack_p38;
    unsigned __int8 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int8 v_stack_p58;
    unsigned int v_stack_p60;
    unsigned __int64 v_stack_p64;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;
    unsigned __int64 v_stack_p80;
    unsigned __int64 v_stack_p88;
    unsigned __int64 v_stack_p90;
    unsigned __int64 v_stack_p98;
    unsigned __int64 v_stack_pA0;
    unsigned __int64 v_stack_pA8;
    unsigned __int64 v_stack_pB0;
    unsigned __int64 v_stack_pB8;
    unsigned __int64 v_stack_pC0;
    unsigned int v_stack_pC8;
    unsigned int v_stack_pCC;
    unsigned __int64 v_stack_pD0;
    unsigned __int64 v_stack_pD8;
    unsigned __int64 v_stack_pE0;
    unsigned __int64 v_stack_pF0;

    v_rsp = (v_rsp) - (448);
    result = (*(unsigned __int64 *)(v_rip + 10970292)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m168 = a4;
    v_stack_m198 = (unsigned int)((unsigned int)(a3));
    v_stack_m120 = a2;
    v_stack_m158 = a1;
    v_stack_m170 = a2;
    v_stack_m188 = (unsigned int)((unsigned int)(a3));
    v_stack_m128 = a4;
    result = 0;
    v_stack_m150 = v_xmm0;
    v_stack_m140 = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 304) = 0;
    v_stack_m1B0 = v_xmm0;
    v_stack_m1A0 = 0;
    v_stack_mC8 = v_xmm1;
    v_stack_mB8 = v_xmm1;
    v_stack_mA8 = v_xmm1;
    v_stack_m98 = v_xmm1;
    v_stack_m88 = v_xmm1;
    *(unsigned __int64 *)(v_rsp - 120) = v_xmm1;
    *(unsigned __int64 *)(v_rsp - 104) = v_xmm1;
    *(unsigned __int64 *)(v_rsp - 88) = v_xmm1;
    v_r13 = 0;
    v_stack_m194 = 0;
    v_stack_m118 = *(unsigned __int64 *)(gs_base + (0 + 392));
    v_stack_m1B8 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    v_stack_m1B7 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    v_stack_m160 = v_rsp - 200;
    if (((unsigned int)((unsigned int)(a3) - 1)) > 0x7FFFFFEULL) goto loc_00394E14;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_003945EF;
    a2 = ((unsigned int)((unsigned int)((unsigned int)(a3)))) << (5);
    result = ProbeForWrite(a2, a2, v_r13 + 8, a2);
    a1 = v_r13 + 8;
    if (v_stack_m168 < (v_r13 + 8)) { a1 = v_stack_m168; }
    *(unsigned int *)(a1) = (unsigned int)((unsigned int)(*(unsigned int *)(a1)));
    if ((((unsigned __int8)(a5)) & (7)) != 0) goto loc_003943E3;
    if ((a5 + 24) > (v_r13 + 8)) goto loc_003943DD;
    if ((a5 + 24) >= a5) goto loc_003943E8;
loc_003943DD:
    goto loc_003943E8;
loc_003943E3:
    result = ExRaiseDatatypeMisalignment(a1, a2, v_r13 + 8, a2);
loc_003943E8:
    v_stack_m140 = v_xmm0;
    v_stack_m130 = v_xmm1;
    goto loc_00394449;
loc_00394449:
    if (sign_flag) goto loc_0039460D;
loc_00394452:
    v_stack_m180 = 0;
    v_stack_m1D0 = 0;
    v_stack_m1D8 = v_stack_m180;
    result = ObReferenceObjectByHandle(a1, 2, *(unsigned __int64 *)(v_rip + 12782983), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    v_stack_m190 = v_stack_m180;
    if (sign_flag) goto loc_00394615;
    if (((unsigned int)((unsigned int)(a3))) > 16) goto loc_00394E46;
loc_003944A1:
    v_stack_m1A8 = *(unsigned __int64 *)(v_stack_m180 + 16);
    v_stack_m1B0 = 0;
    if ((*(unsigned int *)(v_rip + 12789857)) != 0) goto loc_00394C51;
loc_003944C5:
    v_stack_m1A0 = (unsigned __int8)(v_cr8);
    if (((*(unsigned __int8 *)(v_rip + 12789301)) & (33)) != 0) goto loc_003946D8;
loc_003944D7:
    if (v_stack_m1B0 != 0) goto loc_00394CB3;
loc_003944E8:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m180 + 16) + 33)) != 0) goto loc_00394E2C;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m180 + 16) + 33)) >= 0) goto loc_00394545;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m180 + 16) + 33)) >= 0) goto loc_0039453B;
    result = KiDeregisterObjectWaitBlock(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m180 + 16) + 8), v_stack_m180 + 616, *(unsigned __int64 *)(v_rip + 12782983), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    if ((unsigned __int8)(result) != 0) {
        a2 = 0x746C6644ULL;
        a1 = v_stack_m180;
        result = ObfDereferenceObjectWithTag(a1, a2, *(unsigned __int64 *)(v_rip + 12782983), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    }
loc_00394545:
    v_stack_m170 = v_stack_m180 + 380;
    v_stack_m188 = v_stack_m180 + 384;
loc_0039456D:
    if ((*(unsigned int *)(v_stack_m180 + 380)) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m180 + 384))))) goto loc_00394BA2;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m180 + 16) + 33)) != 0) goto loc_00394BA2;
    if (((*(unsigned __int8 *)(v_rip + 12789115)) & (1)) != 0) goto loc_003946F8;
loc_00394591:
    if (v_stack_m1B0 != 0) goto loc_003945C7;
    if (v_stack_m1B0 == v_stack_m1B0) goto loc_00394718;
    result = KxWaitForLockChainValid(v_stack_m1B0, a2, *(unsigned __int64 *)(v_rip + 12782983), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
loc_003945C7:
    v_stack_m1B0 = 0;
    result = (unsigned __int8)((v_stack_m1A8) ^ ((unsigned __int8)(v_stack_m1A8)));
    if ((((unsigned __int8)(result)) & (4)) == 0) goto loc_00394718;
    result = KeWakeAddressAll(result + 8, v_stack_m1A8, *(unsigned __int64 *)(v_rip + 12782983), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    goto loc_00394718;
loc_003945EF:
    v_stack_m140 = v_xmm0;
    v_stack_m130 = v_xmm1;
    goto loc_00394452;
loc_0039460D:
    v_stack_m12C = 0;
loc_00394615:
loc_00394623:
loc_00394629:
    result = v_stack_m160;
    if (v_stack_m160 != v_stack_mC8) {
        a2 = 0;
        a1 = v_stack_m160;
        result = ExFreePoolWithTag(a1, a2, *(unsigned __int64 *)(v_rip + 12782983), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    }
    if (v_stack_m180 == 0) goto loc_00394677;
    if ((*(unsigned int *)(v_rip + 12782012)) != 0) {
        a2 = 0;
        a4 = 0x746C6644ULL;
        a3 = a2 + 1;
        a1 = v_stack_m180 - 48;
        result = ObpPushStackInfo(a1, a2, a3, a4);
    }
    v_r12 = (-1) - (1);
    if (condition_is_less_or_equal) goto loc_003946AC;
loc_00394677:
    if (((v_stack_m12C) & (1)) != 0) goto loc_00394E8B;
loc_00394685:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (448);
    return result;
loc_003946AC:
    if (*(unsigned __int64 *)(v_stack_m180 - 40) != 0) goto loc_00394BAD;
    if (!sign_flag) goto loc_00394D98;
    v_stack_p20 = v_r12;
    a2 = 0;
    result = KeBugCheckEx(a2 + 24, a2, v_stack_m180, 2);
loc_003946D8:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12031866))) != 0) goto loc_003944D7;
    result = KiAcquireQueuedSpinLockInstrumented(v_stack_p48, *(unsigned __int64 *)(v_stack_m180 + 16), v_stack_m180, 2);
    goto loc_003944E8;
loc_003946F8:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12031834))) != 0) goto loc_00394591;
    result = KiReleaseQueuedSpinLockInstrumented(v_stack_p48, v_stack_p1F8, v_stack_m180, 2);
loc_00394718:
    if ((*(unsigned int *)(v_rip + 12789244)) != 0) {
        a1 = 2;
        a2 = (unsigned __int8)(v_stack_p58);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, v_stack_m180, 2);
    }
    if ((((unsigned __int8)((unsigned int)(v_stack_pCC))) & (1)) == 0) goto loc_003948AA;
    v_stack_pF0 = v_xmm0;
    v_stack_p100 = v_xmm0;
    v_stack_p110 = v_xmm0;
    v_stack_p120 = v_xmm0;
    v_stack_pA8 = v_xmm0;
    v_rbx = (unsigned int)(((unsigned int)(v_stack_pC8)) & (0xFFFF0000ULL));
    if (condition_is_below) goto loc_00394895;
    v_stack_p80 = 0;
    v_stack_p28 = 0;
    v_stack_p20 = v_stack_p80;
    result = ObReferenceObjectByHandle(v_stack_pC0, 1, *(unsigned __int64 *)(v_rip + 12788841), v_stack_p40);
    if (sign_flag) goto loc_00394895;
    if (condition_is_above_or_equal) goto loc_00394E1F;
    v_rdi = (unsigned int)((1) + 1);
    if ((*(unsigned __int64 *)(v_stack_p80 + 408)) != 0) goto loc_00394ED1;
loc_00394818:
    v_stack_pF0 = v_stack_p80;
    v_rbx = (unsigned int)((v_rbx) | (4));
    v_stack_p120 = (unsigned int)(v_rbx);
    v_stack_p110 = 0;
    v_stack_p108 = 0;
    v_stack_p118 = 0;
    a3 = 0;
    result = AlpcpSendMessage(v_stack_pF0, v_stack_pB8, a3, v_stack_p40);
    if (sign_flag) goto loc_00394F24;
    v_stack_pA8 = v_stack_p110;
    v_stack_pB0 = v_stack_pF0;
    a3 = 0;
    result = AlpcpSignal(v_stack_pF0, 1, a3, v_stack_p40);
loc_00394895:
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), 1, a3, v_stack_p40);
loc_003948AA:
    if ((((unsigned __int8)((unsigned int)(v_stack_pCC))) & (2)) == 0) goto loc_003948F1;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 116)))) & (4)) != 0) goto loc_003948E3;
    if ((*(unsigned int *)(v_rip + 12788814)) != 0) goto loc_00394C74;
loc_003948D8:
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) = (unsigned __int8)(v_stack_p58);
loc_003948E3:
    result = PspRevertContainerImpersonation(*(unsigned __int64 *)(gs_base + (0 + 392)), 1, a3, v_stack_p40);
loc_003948F1:
    v_stack_p38 = 1;
    v_stack_p30 = 0;
    v_stack_p28 = (unsigned __int8)(v_stack_p40);
    v_stack_p20 = v_stack_p64;
    result = IoRemoveIoCompletion(*(unsigned __int64 *)(*(unsigned __int64 *)(2) + 8), v_stack_pD8, v_stack_p98, (unsigned int)(v_stack_p60));
    result = ExpWorkerFactoryFinishDeferredWork(v_stack_pA8, v_stack_pD8, v_stack_p98, (unsigned int)(v_stack_p60));
    v_stack_p50 = *(unsigned __int64 *)(2);
    v_stack_p48 = 0;
    if ((*(unsigned int *)(v_rip + 12788671)) != 0) goto loc_00394C63;
loc_00394967:
    v_stack_p58 = 2;
    if (((*(unsigned __int8 *)(v_rip + 12788115)) & (33)) != 0) goto loc_00394B82;
loc_00394979:
    if (v_stack_p48 != 0) goto loc_00394CDE;
loc_0039498A:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == 258) goto loc_00394D15;
loc_0039499C:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == 258) goto loc_00394D7F;
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(v_stack_p78 + 408))) & (7));
    if (((unsigned __int8)(result)) == 4) goto loc_00394A19;
loc_003949CD:
    if (0 >= 4) goto loc_00394C85;
    if ((*(unsigned __int64 *)(v_stack_p78 + 0 * 8 + 72)) == (*(unsigned __int64 *)(gs_base + (0 + 392)))) goto loc_00394A19;
    result = (unsigned int)((0) + 1);
    goto loc_003949CD;
loc_003949E3:
    v_rdi = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p78 + 408))) & (7));
    result = ObfDereferenceObjectWithTag(*(unsigned __int64 *)(v_stack_p78 + v_rdi * 8 + 72), (unsigned int)(0x746C6644ULL), v_stack_p98, (unsigned int)(v_stack_p60));
    *(unsigned __int64 *)(v_stack_p78 + v_rdi * 8 + 72) = *(unsigned __int64 *)(gs_base + (0 + 392));
    a1 = (unsigned int)((v_rdi + 1) & (3));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p78 + 408))) & (0xFFFFFFF8ULL));
    a1 = (unsigned int)((a1) | ((unsigned int)(result)));
    *(unsigned int *)(v_stack_p78 + 408) = (unsigned int)(a1);
loc_00394A19:
    if ((*(unsigned int *)(v_stack_p78 + 384)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p78 + 380))))) goto loc_00394A35;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_stack_p78 + 16) + 28)) == 0) goto loc_00394BE9;
loc_00394A35:
    if (((*(unsigned __int8 *)(v_rip + 12787914)) & (1)) != 0) goto loc_00394ADE;
loc_00394A42:
    if (v_stack_p48 != 0) goto loc_00394A78;
    if (v_stack_p48 == v_stack_p48) goto loc_00394AFE;
    result = KxWaitForLockChainValid(v_stack_p48, (unsigned int)(0x746C6644ULL), v_stack_p98, (unsigned int)(v_stack_p60));
loc_00394A78:
    v_stack_p48 = 0;
    result = (unsigned __int8)((v_stack_p50) ^ ((unsigned __int8)(v_stack_p50)));
    if ((((unsigned __int8)(result)) & (4)) == 0) goto loc_00394AFE;
    a3 = (result + 8) >> (5);
    a3 = (unsigned int)((a3) & (127));
    result = KeDisableInterrupts(v_stack_p50, (unsigned int)(0x746C6644ULL), a3, (unsigned int)(v_stack_p60));
    result = KiHaltOnAddressWakeEntireList(v_stack_p50, 0, a3, (unsigned int)(v_stack_p60));
    if ((unsigned __int8)((unsigned __int8)(result)) == 0) goto loc_00394B05;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) != 0) goto loc_00394CED;
loc_00394ADB:
    goto loc_00394B05;
loc_00394ADE:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12030836))) != 0) goto loc_00394A42;
    result = KiReleaseQueuedSpinLockInstrumented(v_stack_p48, v_stack_p1F8, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), (unsigned int)(v_stack_p60));
loc_00394AFE:
loc_00394B05:
    if ((*(unsigned int *)(v_rip + 12788239)) != 0) {
        a1 = 2;
        a2 = (unsigned __int8)(v_stack_p58);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), (unsigned int)(v_stack_p60));
    }
loc_00394B23:
    if ((unsigned int)((unsigned int)((unsigned int)(result))) != 0) goto loc_00394B78;
    if (v_stack_p40 == ((unsigned __int8)((unsigned int)((unsigned int)(result))))) goto loc_00394B6A;
    *(unsigned int *)(v_stack_p90) = (unsigned int)((unsigned int)(v_stack_p64));
    goto loc_00394629;
loc_00394B6A:
    *(unsigned int *)(v_stack_p90) = (unsigned int)((unsigned int)(v_stack_p64));
loc_00394B78:
    goto loc_00394623;
loc_00394B82:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12030672))) != 0) goto loc_00394979;
    result = KiAcquireQueuedSpinLockInstrumented(v_stack_p48, v_stack_p58, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), (unsigned int)(v_stack_p60));
    goto loc_0039498A;
loc_00394BA2:
    goto loc_0039499C;
loc_00394BAD:
    result = (v_stack_p68 - 48) >> (8);
    a2 = ((unsigned __int8)(result)) ^ (*(unsigned __int8 *)(v_stack_p68 - 24));
    a2 = (a2) ^ (*(unsigned __int8 *)(v_rip + 12788358));
    v_stack_p20 = v_stack_p48;
    result = KeBugCheckEx(1 + 23, *(unsigned __int64 *)(v_rip - 3754757 + a2 * 8 + 16545792), v_stack_p68, 1);
loc_00394BE9:
    if ((*(unsigned int *)(v_stack_p68 + 404)) == 0) goto loc_00394CC2;
    *(unsigned int *)(v_stack_p68 + 408) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p68 + 408)));
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_stack_p58 + 8) + 4)) != 0) goto loc_00394CC2;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_stack_p58 + 8) + 4)) < 0) goto loc_00394A35;
    *(unsigned int *)(v_stack_p68 + 408) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p68 + 408)));
    result = ObfReferenceObjectWithTag(v_stack_p68, (unsigned int)(0x746C6644ULL), v_stack_p68, 1);
    result = KeRegisterObjectNotification(*(unsigned __int64 *)(v_stack_p58 + 8), v_rip + 11949405, v_stack_p68 + 616, 1);
    goto loc_00394A35;
loc_00394C51:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(v_rip - 3754757), (unsigned __int8)(v_r12), v_stack_p68 + 616, 1);
    goto loc_003944C5;
loc_00394C63:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(v_rip - 3754757), (unsigned __int8)(result), v_stack_p68 + 616, 1);
    goto loc_00394967;
loc_00394C74:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(v_rip - 3754757), (unsigned __int8)(result), v_stack_p68 + 616, 1);
    goto loc_003948D8;
loc_00394C85:
    result = ObfReferenceObjectWithTag((unsigned int)((unsigned int)(result)) + 2, (unsigned int)(0x746C6644ULL), v_stack_p68 + 616, 1);
loc_00394C95:
    if (0 >= 4) goto loc_003949E3;
    if ((*(unsigned __int64 *)(v_stack_p68 + 0 * 8 + 72)) == 0) goto loc_00394D76;
    a1 = (unsigned int)((0) + 1);
    goto loc_00394C95;
loc_00394CB3:
    result = KxWaitForLockOwnerShip(v_stack_p48, v_stack_p68 + 0 * 8, v_stack_p68 + 616, 1);
    goto loc_003944E8;
loc_00394CC2:
    a3 = 0;
    result = ExpWorkerFactoryCheckCreate(v_stack_p68, v_stack_p48, a3, 1);
    goto loc_00394B23;
loc_00394CDE:
    result = KxWaitForLockOwnerShip(v_stack_p48, v_stack_p48, a3, 1);
    goto loc_0039498A;
loc_00394CED:
loc_00394CF4:
    if (condition_is_not_equal) goto loc_00394CF4;
    if (condition_is_above_or_equal) goto loc_00394ADB;
    result = KiRemoveSystemWorkPriorityKick(v_stack_p48, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a3)))), a3, 1);
    goto loc_00394ADB;
loc_00394D15:
    result = ExpWorkerFactoryWantsToCreate(v_stack_p68, 1, a3, 1);
    if ((unsigned __int8)(result) != 0) goto loc_0039456D;
    if ((*(unsigned int *)(v_stack_p70)) <= ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p68 + 376))))) goto loc_0039456D;
    result = (v_stack_pE0) + (0x540ULL);
    if ((*(unsigned __int64 *)(result)) == result) goto loc_0039499C;
    goto loc_0039456D;
loc_00394D76:
    *(unsigned __int64 *)(1 + 72) = (unsigned int)((unsigned int)(result)) + 2;
    goto loc_00394A19;
loc_00394D7F:
    result = ExpRemoveCurrentThreadFromThreadHistory(v_stack_p68, 1, a3, 1);
    goto loc_00394A19;
loc_00394D98:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 486)) != 0) goto loc_00394EC3;
    result = KeAreInterruptsEnabled(v_stack_p68, 1, a3, 1);
    if ((unsigned __int8)(result) == 0) goto loc_00394EC3;
    if (((unsigned __int8)(v_stack_p58)) >= 1) goto loc_00394EC3;
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_stack_p68 - 22))) & (64)) != 0) goto loc_00394DF2;
loc_00394DD0:
    result = *(unsigned __int8 *)(v_stack_p68 - 22);
    if ((*(unsigned int *)(v_rip + 12780089)) != 0) {
        a1 = v_stack_p68 - 48;
        result = ObpDeregisterObject(a1, 1, a3, 1);
    }
    a2 = 0;
    result = ObpRemoveObjectRoutine(v_stack_p68 - 48, a2, a3, 1);
    goto loc_00394677;
loc_00394DF2:
    result = (unsigned int)((result) & (127));
    a1 = (v_stack_p68 - 48) - (*(unsigned __int8 *)(result + v_rip - 3755225 * 1 + 15794048));
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 24)) == 0) goto loc_00394DD0;
    result = ObpHandleRevocationBlockRemoveObject(*(unsigned __int64 *)(a1), a2, a3, 1);
    goto loc_00394DD0;
loc_00394E14:
    goto loc_00394615;
loc_00394E1F:
    goto loc_00394818;
loc_00394E2C:
    result = KeReleaseInStackQueuedSpinLock(v_stack_p48, a2, a3, 1);
    goto loc_00394615;
loc_00394E46:
    a2 = ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)) + 2))) << (3);
    result = ExAllocatePool2(64, a2, (unsigned int)(0x656E6F4EULL), 1);
    v_stack_p98 = result;
    if (result != 0) goto loc_003944A1;
    v_stack_p60 = 16;
    v_stack_p98 = v_stack_p130;
    goto loc_003944A1;
loc_00394E8B:
    v_stack_p38 = 0;
    v_stack_p30 = 0;
    v_stack_p28 = 0;
    v_stack_p20 = 0;
    a4 = 0;
    result = NtAlpcSendWaitReceivePort(v_stack_pC0, (unsigned int)(v_stack_pC8), v_stack_pB8, a4);
    goto loc_00394685;
loc_00394EC3:
    result = ObpDeferObjectDeletion(v_stack_p68 - 48, (unsigned int)(v_stack_pC8), v_stack_pB8, a4);
    goto loc_00394677;
loc_00394ED1:
    v_stack_pA0 = 128 + 352;
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(128 + 352, a2, a3, a4);
    v_stack_pD0 = result;
    result = ExfAcquirePushLockExclusiveEx(128 + 352, result, 128 + 352, a4);
loc_00394F24:
    result = ObfDereferenceObject(v_stack_pF0, result, 128 + 352, a4);
    goto loc_00394895;
}
```

## 5. (Beta) C Style

```c
int64_t NtWaitForWorkViaWorkerFactory(int64_t Arg1, int64_t Arg2, void *Arg3, int64_t Arg4, void *Arg5)
{
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg5 = (uint8_t *)Arg5;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint32_t v_stack_m12C;
    uint64_t v_stack_m130;
    uint64_t v_stack_m140;
    uint64_t v_stack_m150;
    uint64_t v_stack_m158;
    uint64_t v_stack_m160;
    uint64_t v_stack_m168;
    uint64_t v_stack_m170;
    uint64_t v_stack_m180;
    uint32_t v_stack_m188;
    uint64_t v_stack_m190;
    uint32_t v_stack_m194;
    uint32_t v_stack_m198;
    uint64_t v_stack_m1A0;
    uint64_t v_stack_m1A8;
    uint64_t v_stack_m1B0;
    uint8_t v_stack_m1B7;
    uint8_t v_stack_m1B8;
    uint64_t v_stack_m1D0;
    uint64_t v_stack_m1D8;
    uint64_t v_stack_m48;
    uint64_t v_stack_m88;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC8;
    uint32_t v_stack_p0;
    uint64_t v_stack_p100;
    uint64_t v_stack_p108;
    uint64_t v_stack_p110;
    uint64_t v_stack_p118;
    uint64_t v_stack_p120;
    uint64_t v_stack_p130;
    uint64_t v_stack_p1F8;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint8_t v_stack_p38;
    uint8_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint8_t v_stack_p58;
    uint32_t v_stack_p60;
    uint64_t v_stack_p64;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;
    uint64_t v_stack_p80;
    uint64_t v_stack_p88;
    uint64_t v_stack_p90;
    uint64_t v_stack_p98;
    uint64_t v_stack_pA0;
    uint64_t v_stack_pA8;
    uint64_t v_stack_pB0;
    uint64_t v_stack_pB8;
    uint64_t v_stack_pC0;
    uint32_t v_stack_pC8;
    uint32_t v_stack_pCC;
    uint64_t v_stack_pD0;
    uint64_t v_stack_pD8;
    uint64_t v_stack_pE0;
    uint64_t v_stack_pF0;

    local_rsp = (local_rsp) - (448);
    result = (*(uint64_t *)(v_rip + 0xA764B4)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m168 = Arg4;
    v_stack_m198 = (uint32_t)((uint32_t)(Arg3));
    v_stack_m120 = Arg2;
    v_stack_m158 = Arg1;
    v_stack_m170 = Arg2;
    v_stack_m188 = (uint32_t)((uint32_t)(Arg3));
    v_stack_m128 = Arg4;
    result = 0;
    v_stack_m150 = v_xmm0;
    v_stack_m140 = v_xmm0;
    *(uint64_t *)(local_rsp - 0x130) = 0;
    v_stack_m1B0 = v_xmm0;
    v_stack_m1A0 = 0;
    v_stack_mC8 = v_xmm1;
    v_stack_mB8 = v_xmm1;
    v_stack_mA8 = v_xmm1;
    v_stack_m98 = v_xmm1;
    v_stack_m88 = v_xmm1;
    *(uint64_t *)(local_rsp - 0x78) = v_xmm1;
    *(uint64_t *)(local_rsp - 0x68) = v_xmm1;
    *(uint64_t *)(local_rsp - 0x58) = v_xmm1;
    local_r13 = 0;
    v_stack_m194 = 0;
    v_stack_m118 = *(uint64_t *)(gs_base + (0 + 0x188));
    v_stack_m1B8 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    v_stack_m1B7 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    v_stack_m160 = local_rsp - 200;
    if (((uint32_t)((uint32_t)(Arg3) - 1)) > 0x7FFFFFEULL) goto loc_00394E14;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_003945EF;
    Arg2 = ((uint32_t)((uint32_t)((uint32_t)(Arg3)))) << (5);
    result = ProbeForWrite(Arg2, Arg2, local_r13 + 8, Arg2);
    Arg1 = local_r13 + 8;
    if (v_stack_m168 < (local_r13 + 8)) { Arg1 = v_stack_m168; }
    *(uint32_t *)(Arg1) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg1)));
    if ((((uint8_t)(Arg5)) & (7)) != 0) goto loc_003943E3;
    if ((Arg5 + 24) > (local_r13 + 8)) goto loc_003943DD;
    if ((Arg5 + 24) >= Arg5) goto loc_003943E8;
loc_003943DD:
    goto loc_003943E8;
loc_003943E3:
    result = ExRaiseDatatypeMisalignment(Arg1, Arg2, local_r13 + 8, Arg2);
loc_003943E8:
    v_stack_m140 = v_xmm0;
    v_stack_m130 = v_xmm1;
    goto loc_00394449;
loc_00394449:
    if (sign_flag) goto loc_0039460D;
loc_00394452:
    v_stack_m180 = 0;
    v_stack_m1D0 = 0;
    v_stack_m1D8 = v_stack_m180;
    result = ObReferenceObjectByHandle(Arg1, 2, *(uint64_t *)(v_rip + 0xC30D87), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    v_stack_m190 = v_stack_m180;
    if (sign_flag) goto loc_00394615;
    if (((uint32_t)((uint32_t)(Arg3))) > 16) goto loc_00394E46;
loc_003944A1:
    v_stack_m1A8 = *(uint64_t *)(v_stack_m180 + 0x10);
    v_stack_m1B0 = 0;
    if ((*(uint32_t *)(v_rip + 0xC32861)) != 0) goto loc_00394C51;
loc_003944C5:
    v_stack_m1A0 = (uint8_t)(v_cr8);
    if (((*(uint8_t *)(v_rip + 0xC32635)) & (33)) != 0) goto loc_003946D8;
loc_003944D7:
    if (v_stack_m1B0 != 0) goto loc_00394CB3;
loc_003944E8:
    if ((*(uint8_t *)(*(uint64_t *)(v_stack_m180 + 0x10) + 0x21)) != 0) goto loc_00394E2C;
    if ((*(uint8_t *)(*(uint64_t *)(v_stack_m180 + 0x10) + 0x21)) >= 0) goto loc_00394545;
    if ((*(uint8_t *)(*(uint64_t *)(v_stack_m180 + 0x10) + 0x21)) >= 0) goto loc_0039453B;
    result = KiDeregisterObjectWaitBlock(*(uint64_t *)(*(uint64_t *)(v_stack_m180 + 0x10) + 0x8), v_stack_m180 + 616, *(uint64_t *)(v_rip + 0xC30D87), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    if ((uint8_t)(result) != 0) {
        Arg2 = 0x746C6644ULL;
        Arg1 = v_stack_m180;
        result = ObfDereferenceObjectWithTag(Arg1, Arg2, *(uint64_t *)(v_rip + 0xC30D87), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    }
loc_00394545:
    v_stack_m170 = v_stack_m180 + 380;
    v_stack_m188 = v_stack_m180 + 384;
loc_0039456D:
    if ((*(uint32_t *)(v_stack_m180 + 0x17C)) < ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m180 + 0x180))))) goto loc_00394BA2;
    if ((*(uint8_t *)(*(uint64_t *)(v_stack_m180 + 0x10) + 0x21)) != 0) goto loc_00394BA2;
    if (((*(uint8_t *)(v_rip + 0xC3257B)) & (1)) != 0) goto loc_003946F8;
loc_00394591:
    if (v_stack_m1B0 != 0) goto loc_003945C7;
    if (v_stack_m1B0 == v_stack_m1B0) goto loc_00394718;
    result = KxWaitForLockChainValid(v_stack_m1B0, Arg2, *(uint64_t *)(v_rip + 0xC30D87), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
loc_003945C7:
    v_stack_m1B0 = 0;
    result = (uint8_t)((v_stack_m1A8) ^ ((uint8_t)(v_stack_m1A8)));
    if ((((uint8_t)(result)) & (4)) == 0) goto loc_00394718;
    result = KeWakeAddressAll(result + 8, v_stack_m1A8, *(uint64_t *)(v_rip + 0xC30D87), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    goto loc_00394718;
loc_003945EF:
    v_stack_m140 = v_xmm0;
    v_stack_m130 = v_xmm1;
    goto loc_00394452;
loc_0039460D:
    v_stack_m12C = 0;
loc_00394615:
loc_00394623:
loc_00394629:
    result = v_stack_m160;
    if (v_stack_m160 != v_stack_mC8) {
        Arg2 = 0;
        Arg1 = v_stack_m160;
        result = ExFreePoolWithTag(Arg1, Arg2, *(uint64_t *)(v_rip + 0xC30D87), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    }
    if (v_stack_m180 == 0) goto loc_00394677;
    if ((*(uint32_t *)(v_rip + 0xC309BC)) != 0) {
        Arg2 = 0;
        Arg4 = 0x746C6644ULL;
        Arg3 = Arg2 + 1;
        Arg1 = v_stack_m180 - 48;
        result = ObpPushStackInfo(Arg1, Arg2, Arg3, Arg4);
    }
    local_r12 = (-1) - (1);
    if (condition_is_less_or_equal) goto loc_003946AC;
loc_00394677:
    if (((v_stack_m12C) & (1)) != 0) goto loc_00394E8B;
loc_00394685:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (448);
    return result;
loc_003946AC:
    if (*(uint64_t *)(v_stack_m180 - 0x28) != 0) goto loc_00394BAD;
    if (!sign_flag) goto loc_00394D98;
    v_stack_p20 = local_r12;
    Arg2 = 0;
    result = KeBugCheckEx(Arg2 + 24, Arg2, v_stack_m180, 2);
loc_003946D8:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB7977A))) != 0) goto loc_003944D7;
    result = KiAcquireQueuedSpinLockInstrumented(v_stack_p48, *(uint64_t *)(v_stack_m180 + 0x10), v_stack_m180, 2);
    goto loc_003944E8;
loc_003946F8:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB7975A))) != 0) goto loc_00394591;
    result = KiReleaseQueuedSpinLockInstrumented(v_stack_p48, v_stack_p1F8, v_stack_m180, 2);
loc_00394718:
    if ((*(uint32_t *)(v_rip + 0xC325FC)) != 0) {
        Arg1 = 2;
        Arg2 = (uint8_t)(v_stack_p58);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, v_stack_m180, 2);
    }
    if ((((uint8_t)((uint32_t)(v_stack_pCC))) & (1)) == 0) goto loc_003948AA;
    v_stack_pF0 = v_xmm0;
    v_stack_p100 = v_xmm0;
    v_stack_p110 = v_xmm0;
    v_stack_p120 = v_xmm0;
    v_stack_pA8 = v_xmm0;
    local_rbx = (uint32_t)(((uint32_t)(v_stack_pC8)) & (0xFFFF0000ULL));
    if (condition_is_below) goto loc_00394895;
    v_stack_p80 = 0;
    v_stack_p28 = 0;
    v_stack_p20 = v_stack_p80;
    result = ObReferenceObjectByHandle(v_stack_pC0, 1, *(uint64_t *)(v_rip + 0xC32469), v_stack_p40);
    if (sign_flag) goto loc_00394895;
    if (condition_is_above_or_equal) goto loc_00394E1F;
    local_rdi = (uint32_t)((1) + 1);
    if ((*(uint64_t *)(v_stack_p80 + 0x198)) != 0) goto loc_00394ED1;
loc_00394818:
    v_stack_pF0 = v_stack_p80;
    local_rbx = (uint32_t)((local_rbx) | (4));
    v_stack_p120 = (uint32_t)(local_rbx);
    v_stack_p110 = 0;
    v_stack_p108 = 0;
    v_stack_p118 = 0;
    Arg3 = 0;
    result = AlpcpSendMessage(v_stack_pF0, v_stack_pB8, Arg3, v_stack_p40);
    if (sign_flag) goto loc_00394F24;
    v_stack_pA8 = v_stack_p110;
    v_stack_pB0 = v_stack_pF0;
    Arg3 = 0;
    result = AlpcpSignal(v_stack_pF0, 1, Arg3, v_stack_p40);
loc_00394895:
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), 1, Arg3, v_stack_p40);
loc_003948AA:
    if ((((uint8_t)((uint32_t)(v_stack_pCC))) & (2)) == 0) goto loc_003948F1;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x74)))) & (4)) != 0) goto loc_003948E3;
    if ((*(uint32_t *)(v_rip + 0xC3244E)) != 0) goto loc_00394C74;
loc_003948D8:
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) = (uint8_t)(v_stack_p58);
loc_003948E3:
    result = PspRevertContainerImpersonation(*(uint64_t *)(gs_base + (0 + 0x188)), 1, Arg3, v_stack_p40);
loc_003948F1:
    v_stack_p38 = 1;
    v_stack_p30 = 0;
    v_stack_p28 = (uint8_t)(v_stack_p40);
    v_stack_p20 = v_stack_p64;
    result = IoRemoveIoCompletion(*(uint64_t *)(*(uint64_t *)(2) + 0x8), v_stack_pD8, v_stack_p98, (uint32_t)(v_stack_p60));
    result = ExpWorkerFactoryFinishDeferredWork(v_stack_pA8, v_stack_pD8, v_stack_p98, (uint32_t)(v_stack_p60));
    v_stack_p50 = *(uint64_t *)(2);
    v_stack_p48 = 0;
    if ((*(uint32_t *)(v_rip + 0xC323BF)) != 0) goto loc_00394C63;
loc_00394967:
    v_stack_p58 = 2;
    if (((*(uint8_t *)(v_rip + 0xC32193)) & (33)) != 0) goto loc_00394B82;
loc_00394979:
    if (v_stack_p48 != 0) goto loc_00394CDE;
loc_0039498A:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == 258) goto loc_00394D15;
loc_0039499C:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == 258) goto loc_00394D7F;
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(v_stack_p78 + 0x198))) & (7));
    if (((uint8_t)(result)) == 4) goto loc_00394A19;
loc_003949CD:
    if (0 >= 4) goto loc_00394C85;
    if ((*(uint64_t *)(v_stack_p78 + 0x0 * 8 + 0x48)) == (*(uint64_t *)(gs_base + (0 + 0x188)))) goto loc_00394A19;
    result = (uint32_t)((0) + 1);
    goto loc_003949CD;
loc_003949E3:
    local_rdi = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p78 + 0x198))) & (7));
    result = ObfDereferenceObjectWithTag(*(uint64_t *)(v_stack_p78 + local_rdi * 8 + 0x48), (uint32_t)(0x746C6644ULL), v_stack_p98, (uint32_t)(v_stack_p60));
    *(uint64_t *)(v_stack_p78 + local_rdi * 8 + 0x48) = *(uint64_t *)(gs_base + (0 + 0x188));
    Arg1 = (uint32_t)((local_rdi + 1) & (3));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p78 + 0x198))) & (0xFFFFFFF8ULL));
    Arg1 = (uint32_t)((Arg1) | ((uint32_t)(result)));
    *(uint32_t *)(v_stack_p78 + 0x198) = (uint32_t)(Arg1);
loc_00394A19:
    if ((*(uint32_t *)(v_stack_p78 + 0x180)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p78 + 0x17C))))) goto loc_00394A35;
    if ((*(uint32_t *)(*(uint64_t *)(v_stack_p78 + 0x10) + 0x1C)) == 0) goto loc_00394BE9;
loc_00394A35:
    if (((*(uint8_t *)(v_rip + 0xC320CA)) & (1)) != 0) goto loc_00394ADE;
loc_00394A42:
    if (v_stack_p48 != 0) goto loc_00394A78;
    if (v_stack_p48 == v_stack_p48) goto loc_00394AFE;
    result = KxWaitForLockChainValid(v_stack_p48, (uint32_t)(0x746C6644ULL), v_stack_p98, (uint32_t)(v_stack_p60));
loc_00394A78:
    v_stack_p48 = 0;
    result = (uint8_t)((v_stack_p50) ^ ((uint8_t)(v_stack_p50)));
    if ((((uint8_t)(result)) & (4)) == 0) goto loc_00394AFE;
    Arg3 = (result + 8) >> (5);
    Arg3 = (uint32_t)((Arg3) & (127));
    result = KeDisableInterrupts(v_stack_p50, (uint32_t)(0x746C6644ULL), Arg3, (uint32_t)(v_stack_p60));
    result = KiHaltOnAddressWakeEntireList(v_stack_p50, 0, Arg3, (uint32_t)(v_stack_p60));
    if ((uint8_t)((uint8_t)(result)) == 0) goto loc_00394B05;
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) != 0) goto loc_00394CED;
loc_00394ADB:
    goto loc_00394B05;
loc_00394ADE:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB79374))) != 0) goto loc_00394A42;
    result = KiReleaseQueuedSpinLockInstrumented(v_stack_p48, v_stack_p1F8, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), (uint32_t)(v_stack_p60));
loc_00394AFE:
loc_00394B05:
    if ((*(uint32_t *)(v_rip + 0xC3220F)) != 0) {
        Arg1 = 2;
        Arg2 = (uint8_t)(v_stack_p58);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), (uint32_t)(v_stack_p60));
    }
loc_00394B23:
    if ((uint32_t)((uint32_t)((uint32_t)(result))) != 0) goto loc_00394B78;
    if (v_stack_p40 == ((uint8_t)((uint32_t)((uint32_t)(result))))) goto loc_00394B6A;
    *(uint32_t *)(v_stack_p90) = (uint32_t)((uint32_t)(v_stack_p64));
    goto loc_00394629;
loc_00394B6A:
    *(uint32_t *)(v_stack_p90) = (uint32_t)((uint32_t)(v_stack_p64));
loc_00394B78:
    goto loc_00394623;
loc_00394B82:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB792D0))) != 0) goto loc_00394979;
    result = KiAcquireQueuedSpinLockInstrumented(v_stack_p48, v_stack_p58, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), (uint32_t)(v_stack_p60));
    goto loc_0039498A;
loc_00394BA2:
    goto loc_0039499C;
loc_00394BAD:
    result = (v_stack_p68 - 48) >> (8);
    Arg2 = ((uint8_t)(result)) ^ (*(uint8_t *)(v_stack_p68 - 0x18));
    Arg2 = (Arg2) ^ (*(uint8_t *)(v_rip + 0xC32286));
    v_stack_p20 = v_stack_p48;
    result = KeBugCheckEx(1 + 23, *(uint64_t *)(v_rip - 0x394B05 + Arg2 * 8 + 0xFC7800), v_stack_p68, 1);
loc_00394BE9:
    if ((*(uint32_t *)(v_stack_p68 + 0x194)) == 0) goto loc_00394CC2;
    *(uint32_t *)(v_stack_p68 + 0x198) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p68 + 0x198)));
    if ((*(uint32_t *)(*(uint64_t *)(v_stack_p58 + 0x8) + 0x4)) != 0) goto loc_00394CC2;
    if ((*(uint32_t *)(*(uint64_t *)(v_stack_p58 + 0x8) + 0x4)) < 0) goto loc_00394A35;
    *(uint32_t *)(v_stack_p68 + 0x198) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p68 + 0x198)));
    result = ObfReferenceObjectWithTag(v_stack_p68, (uint32_t)(0x746C6644ULL), v_stack_p68, 1);
    result = KeRegisterObjectNotification(*(uint64_t *)(v_stack_p58 + 0x8), v_rip + 11949405, v_stack_p68 + 616, 1);
    goto loc_00394A35;
loc_00394C51:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(v_rip - 3754757), (uint8_t)(local_r12), v_stack_p68 + 616, 1);
    goto loc_003944C5;
loc_00394C63:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(v_rip - 3754757), (uint8_t)(result), v_stack_p68 + 616, 1);
    goto loc_00394967;
loc_00394C74:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(v_rip - 3754757), (uint8_t)(result), v_stack_p68 + 616, 1);
    goto loc_003948D8;
loc_00394C85:
    result = ObfReferenceObjectWithTag((uint32_t)((uint32_t)(result)) + 2, (uint32_t)(0x746C6644ULL), v_stack_p68 + 616, 1);
loc_00394C95:
    if (0 >= 4) goto loc_003949E3;
    if ((*(uint64_t *)(v_stack_p68 + 0x0 * 8 + 0x48)) == 0) goto loc_00394D76;
    Arg1 = (uint32_t)((0) + 1);
    goto loc_00394C95;
loc_00394CB3:
    result = KxWaitForLockOwnerShip(v_stack_p48, v_stack_p68 + 0 * 8, v_stack_p68 + 616, 1);
    goto loc_003944E8;
loc_00394CC2:
    Arg3 = 0;
    result = ExpWorkerFactoryCheckCreate(v_stack_p68, v_stack_p48, Arg3, 1);
    goto loc_00394B23;
loc_00394CDE:
    result = KxWaitForLockOwnerShip(v_stack_p48, v_stack_p48, Arg3, 1);
    goto loc_0039498A;
loc_00394CED:
loc_00394CF4:
    if (condition_is_not_equal) goto loc_00394CF4;
    if (condition_is_above_or_equal) goto loc_00394ADB;
    result = KiRemoveSystemWorkPriorityKick(v_stack_p48, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg3)))), Arg3, 1);
    goto loc_00394ADB;
loc_00394D15:
    result = ExpWorkerFactoryWantsToCreate(v_stack_p68, 1, Arg3, 1);
    if ((uint8_t)(result) != 0) goto loc_0039456D;
    if ((*(uint32_t *)(v_stack_p70)) <= ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p68 + 0x178))))) goto loc_0039456D;
    result = (v_stack_pE0) + (0x540ULL);
    if ((*(uint64_t *)(result)) == result) goto loc_0039499C;
    goto loc_0039456D;
loc_00394D76:
    *(uint64_t *)(1 + 0x48) = (uint32_t)((uint32_t)(result)) + 2;
    goto loc_00394A19;
loc_00394D7F:
    result = ExpRemoveCurrentThreadFromThreadHistory(v_stack_p68, 1, Arg3, 1);
    goto loc_00394A19;
loc_00394D98:
    if ((*(uint16_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x1E6)) != 0) goto loc_00394EC3;
    result = KeAreInterruptsEnabled(v_stack_p68, 1, Arg3, 1);
    if ((uint8_t)(result) == 0) goto loc_00394EC3;
    if (((uint8_t)(v_stack_p58)) >= 1) goto loc_00394EC3;
    if ((((uint8_t)(*(uint8_t *)(v_stack_p68 - 0x16))) & (64)) != 0) goto loc_00394DF2;
loc_00394DD0:
    result = *(uint8_t *)(v_stack_p68 - 0x16);
    if ((*(uint32_t *)(v_rip + 0xC30239)) != 0) {
        Arg1 = v_stack_p68 - 48;
        result = ObpDeregisterObject(Arg1, 1, Arg3, 1);
    }
    Arg2 = 0;
    result = ObpRemoveObjectRoutine(v_stack_p68 - 48, Arg2, Arg3, 1);
    goto loc_00394677;
loc_00394DF2:
    result = (uint32_t)((result) & (127));
    Arg1 = (v_stack_p68 - 48) - (*(uint8_t *)(result + v_rip - 0x394CD9 * 1 + 0xF0FF80));
    if ((*(uint8_t *)(*(uint64_t *)(Arg1) + 0x18)) == 0) goto loc_00394DD0;
    result = ObpHandleRevocationBlockRemoveObject(*(uint64_t *)(Arg1), Arg2, Arg3, 1);
    goto loc_00394DD0;
loc_00394E14:
    goto loc_00394615;
loc_00394E1F:
    goto loc_00394818;
loc_00394E2C:
    result = KeReleaseInStackQueuedSpinLock(v_stack_p48, Arg2, Arg3, 1);
    goto loc_00394615;
loc_00394E46:
    Arg2 = ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)) + 2))) << (3);
    result = ExAllocatePool2(64, Arg2, (uint32_t)(0x656E6F4EULL), 1);
    v_stack_p98 = result;
    if (result != 0) goto loc_003944A1;
    v_stack_p60 = 16;
    v_stack_p98 = v_stack_p130;
    goto loc_003944A1;
loc_00394E8B:
    v_stack_p38 = 0;
    v_stack_p30 = 0;
    v_stack_p28 = 0;
    v_stack_p20 = 0;
    Arg4 = 0;
    result = NtAlpcSendWaitReceivePort(v_stack_pC0, (uint32_t)(v_stack_pC8), v_stack_pB8, Arg4);
    goto loc_00394685;
loc_00394EC3:
    result = ObpDeferObjectDeletion(v_stack_p68 - 48, (uint32_t)(v_stack_pC8), v_stack_pB8, Arg4);
    goto loc_00394677;
loc_00394ED1:
    v_stack_pA0 = 128 + 352;
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(128 + 352, Arg2, Arg3, Arg4);
    v_stack_pD0 = result;
    result = ExfAcquirePushLockExclusiveEx(128 + 352, result, 128 + 352, Arg4);
loc_00394F24:
    result = ObfDereferenceObject(v_stack_pF0, result, 128 + 352, Arg4);
    goto loc_00394895;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `- 0x1` | `32` | `R` |
| `Arg5` | `+ 0x0` | `128` | `R` |
| `Arg5` | `+ 0x10` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00394270&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
