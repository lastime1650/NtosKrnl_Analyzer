# AlpcpSignal

- RVA: `0x003955E0`–`0x00396277` (길이 `3,223` bytes)
- VA: `0x00000001403955E0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000811EC`
- 디코드: `746`개 명령, `3,223/3,223` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **46**; 고유 호출 대상: **27**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x003956AF` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x003956CD` → [ExfReleasePushLockShared](../26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x003956D9` → [KeAbPostRelease](../2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x003957AD` → [KiAcquireKobjectLockSafe](../25/KiAcquireKobjectLockSafe_function_00251C90.md) (function, `0x00251C90`)
- `0x00395834` → [KeSetEvent](../33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x0039583D` → [AlpcpReleaseDirectAttribute](../47/AlpcpReleaseDirectAttribute_function_00474804.md) (function, `0x00474804`)
- `0x00395869` → [KiWakeOtherQueueWaiters](KiWakeOtherQueueWaiters_function_003964D0.md) (function, `0x003964D0`)
- `0x003958AF` → [KiExitDispatcher](../25/KiExitDispatcher_function_00251CF0.md) (function, `0x00251CF0`)
- `0x003958E3` → [KiAcquireQueuedSpinLockInstrumented](../27/KiAcquireQueuedSpinLockInstrumented_function_00275850.md) (function, `0x00275850`)
- `0x00395933` → [KiAcquireKobjectLockSafe](../25/KiAcquireKobjectLockSafe_function_00251C90.md) (function, `0x00251C90`)
- `0x00395A20` → [KiAcquireKobjectLockSafe](../25/KiAcquireKobjectLockSafe_function_00251C90.md) (function, `0x00251C90`)
- `0x00395B0A` → [KiRemovePrcbWaitEntry](../25/KiRemovePrcbWaitEntry_function_002502D0.md) (function, `0x002502D0`)
- `0x00395BB7` → [IopAllocateMiniCompletionPacket](../../page/9D/IopAllocateMiniCompletionPacket_function_009DA2E0.md) (function, `0x009DA2E0`)
- `0x00395C56` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x00395C67` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x00395C8F` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00395C9E` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00395CAB` → [KeIsThreadRunning](KeIsThreadRunning_function_00396720.md) (function, `0x00396720`)
- `0x00395CBA` → [EtwTraceEnqueueWork](EtwTraceEnqueueWork_function_0039674C.md) (function, `0x0039674C`)
- `0x00395CE2` → [KeReleaseSemaphoreEx](../34/KeReleaseSemaphoreEx_function_003468C0.md) (function, `0x003468C0`)
- `0x00395D87` → [KiRemovePrcbWaitEntry](../25/KiRemovePrcbWaitEntry_function_002502D0.md) (function, `0x002502D0`)
- `0x00395D8F` → [KiEnterDeferredReadyState](KiEnterDeferredReadyState_function_00397420.md) (function, `0x00397420`)
- `0x00395E81` → [KiRemovePrcbWaitEntry](../25/KiRemovePrcbWaitEntry_function_002502D0.md) (function, `0x002502D0`)
- `0x00395E89` → [KiEnterDeferredReadyState](KiEnterDeferredReadyState_function_00397420.md) (function, `0x00397420`)
- `0x00395F06` → [KxWaitForLockOwnerShip](../25/KxWaitForLockOwnerShip_function_00257EB0.md) (function, `0x00257EB0`)
- `0x00395F18` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x00395F35` → [KiInsertQueueInternal](../21/KiInsertQueueInternal_function_00219B30.md) (function, `0x00219B30`)
- `0x00395F51` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x00395F8A` → [KiInsertQueueInternal](../21/KiInsertQueueInternal_function_00219B30.md) (function, `0x00219B30`)
- `0x00395FB5` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00395FC4` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00395FEF` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x00396011` → [AlpcpQueueIoCompletion](AlpcpQueueIoCompletion_function_00397480.md) (function, `0x00397480`)
- `0x00396037` → [ExfReleasePushLockShared](../26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x00396043` → [KeAbPostRelease](../2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0039605B` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0039606A` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0039608D` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0039609F` → [RtlRaiseStatus](../2F/RtlRaiseStatus_function_002F6A50.md) (function, `0x002F6A50`)
- `0x003960B1` → [KiCompleteDirectSwitchThread](../3F/KiCompleteDirectSwitchThread_function_003FFE1C.md) (function, `0x003FFE1C`)
- `0x003960D9` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x00396142` → [KiTryUnwaitThread](../35/KiTryUnwaitThread_function_003506D0.md) (function, `0x003506D0`)
- `0x00396163` → [KiTryUnwaitThread](../35/KiTryUnwaitThread_function_003506D0.md) (function, `0x003506D0`)
- `0x00396209` → [KeInsertQueueDpc](../20/KeInsertQueueDpc_function_00207C50.md) (function, `0x00207C50`)
- `0x0039623A` → [KeInsertQueueDpc](../20/KeInsertQueueDpc_function_00207C50.md) (function, `0x00207C50`)
- `0x00396261` → [KeAcquireInStackQueuedSpinLock](../27/KeAcquireInStackQueuedSpinLock_function_002757A0.md) (function, `0x002757A0`)

### Direct callers
- [NtWaitForWorkViaWorkerFactory](NtWaitForWorkViaWorkerFactory_function_00394270.md) at `0x00394890`
- [sub_00868100](../../page/86/Unknown_function_00868100.md) at `0x008681B6`
- [NtReplyWaitReceivePortEx](../../page/89/NtReplyWaitReceivePortEx_function_00895850.md) at `0x0089599A`

### Static image references
- `0x0039564D` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x00395659` → RVA `0x00FC6B06` (`ALMOSTRO`; read)
- `0x00395752` → RVA `0x00FC6B04` (`ALMOSTRO`; read)
- `0x003958CD` → RVA `0x00F0DE58` (`.data`; read)
- `0x003959CF` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x00395C81` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00395BB7` → [IopAllocateMiniCompletionPacket](../../page/9D/IopAllocateMiniCompletionPacket_function_009DA2E0.md) (`.text` → `PAGE`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x00396269` → [sub_006E59DC](../6E/Unknown_function_006E59DC.md) (`tail-transfer`)
  - `0x00396272` → [sub_006E59DC + 0x3](../6E/Unknown_function_006E59DC.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003955E0  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
003955E5  55                              push rbp
003955E6  56                              push rsi
003955E7  57                              push rdi
003955E8  41 54                           push r12
003955EA  41 55                           push r13
003955EC  41 56                           push r14
003955EE  41 57                           push r15
003955F0  48 83 EC 60                     sub rsp, 0x60
003955F4  48 8B 79 20                     mov rdi, qword ptr [rcx + 0x20]
003955F8  44 0F B6 FA                     movzx r15d, dl
003955FC  41 0F B6 E8                     movzx ebp, r8b
00395600  48 8B D9                        mov rbx, rcx
00395603  48 85 FF                        test rdi, rdi
00395606  0F 84 FE 01 00 00               je 0x14039580a
0039560C  80 79 3A 00                     cmp byte ptr [rcx + 0x3a], 0
00395610  BE 02 00 00 00                  mov esi, 2
00395615  0F 84 CD 03 00 00               je 0x1403959e8
0039561B  48 8B 5F 30                     mov rbx, qword ptr [rdi + 0x30]
0039561F  33 C0                           xor eax, eax
00395621  44 0F B6 71 3B                  movzx r14d, byte ptr [rcx + 0x3b]
00395626  0F 57 C0                        xorps xmm0, xmm0
00395629  4C 8B 6F 20                     mov r13, qword ptr [rdi + 0x20]
0039562D  44 8B E5                        mov r12d, ebp
00395630  0F 11 44 24 40                  movups xmmword ptr [rsp + 0x40], xmm0
00395635  48 89 5C 24 48                  mov qword ptr [rsp + 0x48], rbx
0039563A  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
0039563F  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00395644  90                              nop
00395645  44 0F 20 C5                     mov rbp, cr8
00395649  44 0F 22 C6                     mov cr8, rsi
0039564D  39 05 CD 16 C3 00               cmp dword ptr [rip + 0xc316cd], eax
00395653  0F 85 F5 05 00 00               jne 0x140395c4e
00395659  F6 05 A6 14 C3 00 21            test byte ptr [rip + 0xc314a6], 0x21
00395660  40 88 6C 24 50                  mov byte ptr [rsp + 0x50], bpl
00395665  0F 85 62 02 00 00               jne 0x1403958cd
0039566B  48 8D 54 24 40                  lea rdx, [rsp + 0x40]
00395670  48 87 13                        xchg qword ptr [rbx], rdx
00395673  48 85 D2                        test rdx, rdx
00395676  0F 85 85 08 00 00               jne 0x140395f01
0039567C  8B 53 0C                        mov edx, dword ptr [rbx + 0xc]
0039567F  3B 53 08                        cmp edx, dword ptr [rbx + 8]
00395682  0F 83 62 09 00 00               jae 0x140395fea
00395688  48 8B 4B 20                     mov rcx, qword ptr [rbx + 0x20]
0039568C  48 85 C9                        test rcx, rcx
0039568F  74 07                           je 0x140395698
00395691  48 8B 01                        mov rax, qword ptr [rcx]
00395694  48 89 43 20                     mov qword ptr [rbx + 0x20], rax
00395698  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
0039569C  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
003956A1  48 89 84 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rax
003956A9  8D 42 01                        lea eax, [rdx + 1]
003956AC  89 43 0C                        mov dword ptr [rbx + 0xc], eax
003956AF  E8 2C D6 FA FF                  call 0x140342ce0
003956B4  B8 11 00 00 00                  mov eax, 0x11
003956B9  33 D2                           xor edx, edx
003956BB  F0 48 0F B1 97 60 01 00 00      lock cmpxchg qword ptr [rdi + 0x160], rdx
003956C4  74 0C                           je 0x1403956d2
003956C6  48 8D 8F 60 01 00 00            lea rcx, [rdi + 0x160]
003956CD  E8 6E DD EC FF                  call 0x140263440
003956D2  48 8D 8F 60 01 00 00            lea rcx, [rdi + 0x160]
003956D9  E8 22 BF F4 FF                  call 0x1402e1600
003956DE  48 8B 7F 28                     mov rdi, qword ptr [rdi + 0x28]
003956E2  41 F6 DE                        neg r14b
003956E5  48 1B DB                        sbb rbx, rbx
003956E8  45 33 F6                        xor r14d, r14d
003956EB  45 84 FF                        test r15b, r15b
003956EE  41 8B C6                        mov eax, r14d
003956F1  0F 95 C0                        setne al
003956F4  8B E8                           mov ebp, eax
003956F6  83 CD 04                        or ebp, 4
003956F9  45 85 E4                        test r12d, r12d
003956FC  4C 8B A4 24 B8 00 00 00         mov r12, qword ptr [rsp + 0xb8]
00395704  0F 44 E8                        cmove ebp, eax
00395707  89 AC 24 A0 00 00 00            mov dword ptr [rsp + 0xa0], ebp
0039570E  4D 85 E4                        test r12, r12
00395711  0F 84 9C 04 00 00               je 0x140395bb3
00395717  49 89 7C 24 18                  mov qword ptr [r12 + 0x18], rdi
0039571C  4D 8D 7D 08                     lea r15, [r13 + 8]
00395720  49 89 5C 24 20                  mov qword ptr [r12 + 0x20], rbx
00395725  45 89 74 24 28                  mov dword ptr [r12 + 0x28], r14d
0039572A  4D 89 74 24 30                  mov qword ptr [r12 + 0x30], r14
0039572F  44 0F 20 C0                     mov rax, cr8
00395733  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00395738  44 0F 22 C6                     mov cr8, rsi
0039573C  44 39 35 DD 15 C3 00            cmp dword ptr [rip + 0xc315dd], r14d
00395743  0F 85 17 05 00 00               jne 0x140395c60
00395749  65 48 8B 34 25 20 00 00 00      mov rsi, qword ptr gs:[0x20]
00395752  8B 05 AC 13 C3 00               mov eax, dword ptr [rip + 0xc313ac]
00395758  48 89 74 24 30                  mov qword ptr [rsp + 0x30], rsi
0039575D  48 8B 5E 08                     mov rbx, qword ptr [rsi + 8]
00395761  0F BA E0 18                     bt eax, 0x18
00395765  0F 82 3D 05 00 00               jb 0x140395ca8
0039576B  41 0F B6 45 01                  movzx eax, byte ptr [r13 + 1]
00395770  F6 D0                           not al
00395772  D1 E8                           shr eax, 1
00395774  83 E0 01                        and eax, 1
00395777  89 84 24 B8 00 00 00            mov dword ptr [rsp + 0xb8], eax
0039577E  48 8B 83 50 06 00 00            mov rax, qword ptr [rbx + 0x650]
00395785  48 85 C0                        test rax, rax
00395788  48 0F 44 C3                     cmove rax, rbx
0039578C  85 ED                           test ebp, ebp
0039578E  74 17                           je 0x1403957a7
00395790  48 8B 80 20 02 00 00            mov rax, qword ptr [rax + 0x220]
00395797  8B 80 88 00 00 00               mov eax, dword ptr [rax + 0x88]
0039579D  0F BA E0 0D                     bt eax, 0xd
003957A1  0F 82 F8 07 00 00               jb 0x140395f9f
003957A7  40 32 FF                        xor dil, dil
003957AA  49 8B CD                        mov rcx, r13
003957AD  E8 DE C4 EB FF                  call 0x140251c90
003957B2  4D 39 3F                        cmp qword ptr [r15], r15
003957B5  0F 84 56 04 00 00               je 0x140395c11
003957BB  41 8B 45 28                     mov eax, dword ptr [r13 + 0x28]
003957BF  41 3B 45 2C                     cmp eax, dword ptr [r13 + 0x2c]
003957C3  0F 83 3F 04 00 00               jae 0x140395c08
003957C9  48 8B 83 E8 00 00 00            mov rax, qword ptr [rbx + 0xe8]
003957D0  49 3B C5                        cmp rax, r13
003957D3  0F 84 5B 05 00 00               je 0x140395d34
003957D9  49 8B 37                        mov rsi, qword ptr [r15]
003957DC  0F 1F 40 00                     nop dword ptr [rax]
003957E0  48 8B FE                        mov rdi, rsi
003957E3  48 8B 36                        mov rsi, qword ptr [rsi]
003957E6  80 7F 10 03                     cmp byte ptr [rdi + 0x10], 3
003957EA  0F 85 AC 03 00 00               jne 0x140395b9c
003957F0  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
003957F4  48 39 7E 08                     cmp qword ptr [rsi + 8], rdi
003957F8  75 09                           jne 0x140395803
003957FA  48 39 38                        cmp qword ptr [rax], rdi
003957FD  0F 84 CA 03 00 00               je 0x140395bcd
00395803  B9 03 00 00 00                  mov ecx, 3
00395808  CD 29                           int 0x29
0039580A  48 8B 49 18                     mov rcx, qword ptr [rcx + 0x18]
0039580E  48 85 C9                        test rcx, rcx
00395811  0F 85 D6 00 00 00               jne 0x1403958ed
00395817  48 8B 4B 28                     mov rcx, qword ptr [rbx + 0x28]
0039581B  F6 C1 01                        test cl, 1
0039581E  0F 84 90 00 00 00               je 0x1403958b4
00395824  48 83 F9 04                     cmp rcx, 4
00395828  72 18                           jb 0x140395842
0039582A  48 83 E1 FC                     and rcx, 0xfffffffffffffffc
0039582E  45 0F B6 C7                     movzx r8d, r15b
00395832  33 D2                           xor edx, edx
00395834  E8 D7 9A FA FF                  call 0x14033f310
00395839  48 8B 4B 28                     mov rcx, qword ptr [rbx + 0x28]
0039583D  E8 C2 EF 0D 00                  call 0x140474804
00395842  33 D2                           xor edx, edx
00395844  48 89 53 28                     mov qword ptr [rbx + 0x28], rdx
00395848  EB 6A                           jmp 0x1403958b4
0039584A  49 89 04 24                     mov qword ptr [r12], rax
0039584E  49 89 54 24 08                  mov qword ptr [r12 + 8], rdx
00395853  4C 89 22                        mov qword ptr [rdx], r12
00395856  4C 89 60 08                     mov qword ptr [rax + 8], r12
0039585A  85 C9                           test ecx, ecx
0039585C  75 10                           jne 0x14039586e
0039585E  4D 39 3F                        cmp qword ptr [r15], r15
00395861  74 0B                           je 0x14039586e
00395863  49 8B D5                        mov rdx, r13
00395866  48 8B CE                        mov rcx, rsi
00395869  E8 62 0C 00 00                  call 0x1403964d0
0039586E  F0 41 81 65 00 7F FF FF FF      lock and dword ptr [r13], 0xffffff7f
00395877  40 F6 C5 01                     test bpl, 1
0039587B  0F 85 A0 04 00 00               jne 0x140395d21
00395881  41 8B CE                        mov ecx, r14d
00395884  40 F6 C5 04                     test bpl, 4
00395888  0F 85 17 08 00 00               jne 0x1403960a5
0039588E  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00395893  48 8B 44 24 38                  mov rax, qword ptr [rsp + 0x38]
00395898  41 B8 01 00 00 00               mov r8d, 1
0039589E  44 8B 8C 24 B8 00 00 00         mov r9d, dword ptr [rsp + 0xb8]
003958A6  8B D1                           mov edx, ecx
003958A8  88 44 24 20                     mov byte ptr [rsp + 0x20], al
003958AC  48 8B CB                        mov rcx, rbx
003958AF  E8 3C C4 EB FF                  call 0x140251cf0
003958B4  48 8B 9C 24 A8 00 00 00         mov rbx, qword ptr [rsp + 0xa8]
003958BC  48 83 C4 60                     add rsp, 0x60
003958C0  41 5F                           pop r15
003958C2  41 5E                           pop r14
003958C4  41 5D                           pop r13
003958C6  41 5C                           pop r12
003958C8  5F                              pop rdi
003958C9  5E                              pop rsi
003958CA  5D                              pop rbp
003958CB  C3                              ret
003958CC  CC                              int3
003958CD  8B 05 85 85 B7 00               mov eax, dword ptr [rip + 0xb78585]
003958D3  85 C0                           test eax, eax
003958D5  0F 85 90 FD FF FF               jne 0x14039566b
003958DB  48 8B D3                        mov rdx, rbx
003958DE  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
003958E3  E8 68 FF ED FF                  call 0x140275850
003958E8  E9 8F FD FF FF                  jmp 0x14039567c
003958ED  45 84 FF                        test r15b, r15b
003958F0  0F 84 CE 03 00 00               je 0x140395cc4
003958F6  4C 8D B9 18 05 00 00            lea r15, [rcx + 0x518]
003958FD  44 0F 20 C7                     mov rdi, cr8
00395901  48 89 BC 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rdi
00395909  BE 02 00 00 00                  mov esi, 2
0039590E  44 0F 22 C6                     mov cr8, rsi
00395912  83 3D 07 14 C3 00 00            cmp dword ptr [rip + 0xc31407], 0
00395919  0F 85 2A 06 00 00               jne 0x140395f49
0039591F  65 48 8B 1C 25 20 00 00 00      mov rbx, qword ptr gs:[0x20]
00395928  49 8B CF                        mov rcx, r15
0039592B  48 89 9C 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rbx
00395933  E8 58 C3 EB FF                  call 0x140251c90
00395938  41 8B 47 04                     mov eax, dword ptr [r15 + 4]
0039593C  8D 48 01                        lea ecx, [rax + 1]
0039593F  3B C8                           cmp ecx, eax
00395941  0F 8C 79 07 00 00               jl 0x1403960c0
00395947  41 3B 4F 18                     cmp ecx, dword ptr [r15 + 0x18]
0039594B  0F 8F 6F 07 00 00               jg 0x1403960c0
00395951  41 89 4F 04                     mov dword ptr [r15 + 4], ecx
00395955  85 C0                           test eax, eax
00395957  0F 85 A1 04 00 00               jne 0x140395dfe
0039595D  4D 8B 77 08                     mov r14, qword ptr [r15 + 8]
00395961  4D 8D 6F 08                     lea r13, [r15 + 8]
00395965  45 33 C0                        xor r8d, r8d
00395968  4D 3B F5                        cmp r14, r13
0039596B  0F 84 85 04 00 00               je 0x140395df6
00395971  49 8B 06                        mov rax, qword ptr [r14]
00395974  49 8B F6                        mov rsi, r14
00395977  4C 8B F0                        mov r14, rax
0039597A  48 8B 4E 08                     mov rcx, qword ptr [rsi + 8]
0039597E  48 39 70 08                     cmp qword ptr [rax + 8], rsi
00395982  0F 85 7B FE FF FF               jne 0x140395803
00395988  48 39 31                        cmp qword ptr [rcx], rsi
0039598B  0F 85 72 FE FF FF               jne 0x140395803
00395991  48 89 01                        mov qword ptr [rcx], rax
00395994  48 89 48 08                     mov qword ptr [rax + 8], rcx
00395998  0F B6 46 10                     movzx eax, byte ptr [rsi + 0x10]
0039599C  3C 01                           cmp al, 1
0039599E  0F 85 D3 05 00 00               jne 0x140395f77
003959A4  0F B7 56 12                     movzx edx, word ptr [rsi + 0x12]
003959A8  45 32 E4                        xor r12b, r12b
003959AB  48 8B 5E 18                     mov rbx, qword ptr [rsi + 0x18]
003959AF  41 8B F8                        mov edi, r8d
003959B2  48 89 54 24 30                  mov qword ptr [rsp + 0x30], rdx
003959B7  66 0F 1F 84 00 00 00 00 00      nop word ptr [rax + rax]
003959C0  F0 48 0F BA 6B 40 00            lock bts qword ptr [rbx + 0x40], 0
003959C7  0F 83 79 03 00 00               jae 0x140395d46
003959CD  FF C7                           inc edi
003959CF  85 3D D7 F8 C2 00               test dword ptr [rip + 0xc2f8d7], edi
003959D5  0F 84 72 06 00 00               je 0x14039604d
003959DB  F3 90                           pause
003959DD  48 8B 43 40                     mov rax, qword ptr [rbx + 0x40]
003959E1  48 85 C0                        test rax, rax
003959E4  74 DA                           je 0x1403959c0
003959E6  EB E5                           jmp 0x1403959cd
003959E8  48 8B AF F8 00 00 00            mov rbp, qword ptr [rdi + 0xf8]
003959EF  44 0F 20 C7                     mov rdi, cr8
003959F3  48 89 BC 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rdi
003959FB  44 0F 22 C6                     mov cr8, rsi
003959FF  83 3D 1A 13 C3 00 00            cmp dword ptr [rip + 0xc3131a], 0
00395A06  0F 85 04 05 00 00               jne 0x140395f10
00395A0C  65 48 8B 1C 25 20 00 00 00      mov rbx, qword ptr gs:[0x20]
00395A15  48 8B CD                        mov rcx, rbp
00395A18  48 89 9C 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rbx
00395A20  E8 6B C2 EB FF                  call 0x140251c90
00395A25  8B 45 04                        mov eax, dword ptr [rbp + 4]
00395A28  8D 48 01                        lea ecx, [rax + 1]
00395A2B  3B C8                           cmp ecx, eax
00395A2D  0F 8C 41 06 00 00               jl 0x140396074
00395A33  3B 4D 18                        cmp ecx, dword ptr [rbp + 0x18]
00395A36  0F 8F 38 06 00 00               jg 0x140396074
00395A3C  89 4D 04                        mov dword ptr [rbp + 4], ecx
00395A3F  85 C0                           test eax, eax
00395A41  0F 85 B7 02 00 00               jne 0x140395cfe
00395A47  4C 8B 75 08                     mov r14, qword ptr [rbp + 8]
00395A4B  4C 8D 65 08                     lea r12, [rbp + 8]
00395A4F  45 33 C0                        xor r8d, r8d
00395A52  4D 3B F4                        cmp r14, r12
00395A55  0F 84 9B 02 00 00               je 0x140395cf6
00395A5B  49 8B 06                        mov rax, qword ptr [r14]
00395A5E  49 8B F6                        mov rsi, r14
00395A61  4C 8B F0                        mov r14, rax
00395A64  48 8B 4E 08                     mov rcx, qword ptr [rsi + 8]
00395A68  48 39 70 08                     cmp qword ptr [rax + 8], rsi
00395A6C  0F 85 91 FD FF FF               jne 0x140395803
00395A72  48 39 31                        cmp qword ptr [rcx], rsi
00395A75  0F 85 88 FD FF FF               jne 0x140395803
00395A7B  48 89 01                        mov qword ptr [rcx], rax
00395A7E  48 89 48 08                     mov qword ptr [rax + 8], rcx
00395A82  0F B6 46 10                     movzx eax, byte ptr [rsi + 0x10]
00395A86  3C 01                           cmp al, 1
00395A88  0F 85 94 04 00 00               jne 0x140395f22
00395A8E  0F B7 56 12                     movzx edx, word ptr [rsi + 0x12]
00395A92  45 32 ED                        xor r13b, r13b
00395A95  48 8B 5E 18                     mov rbx, qword ptr [rsi + 0x18]
00395A99  41 8B F8                        mov edi, r8d
00395A9C  48 89 54 24 30                  mov qword ptr [rsp + 0x30], rdx
00395AA1  F0 48 0F BA 6B 40 00            lock bts qword ptr [rbx + 0x40], 0
00395AA8  0F 83 92 03 00 00               jae 0x140395e40
00395AAE  FF C7                           inc edi
00395AB0  85 3D F6 F7 C2 00               test dword ptr [rip + 0xc2f7f6], edi
00395AB6  0F 84 EB 04 00 00               je 0x140395fa7
00395ABC  F3 90                           pause
00395ABE  48 8B 43 40                     mov rax, qword ptr [rbx + 0x40]
00395AC2  48 85 C0                        test rax, rax
00395AC5  74 DA                           je 0x140395aa1
00395AC7  EB E5                           jmp 0x140395aae
00395AC9  0F B6 83 84 01 00 00            movzx eax, byte ptr [rbx + 0x184]
00395AD0  3C 05                           cmp al, 5
00395AD2  0F 85 A1 00 00 00               jne 0x140395b79
00395AD8  0F B6 4B 70                     movzx ecx, byte ptr [rbx + 0x70]
00395ADC  8B C1                           mov eax, ecx
00395ADE  83 E0 07                        and eax, 7
00395AE1  83 F8 01                        cmp eax, 1
00395AE4  0F 85 01 06 00 00               jne 0x1403960eb
00395AEA  48 8B 93 E8 00 00 00            mov rdx, qword ptr [rbx + 0xe8]
00395AF1  48 85 D2                        test rdx, rdx
00395AF4  74 11                           je 0x140395b07
00395AF6  0F B6 02                        movzx eax, byte ptr [rdx]
00395AF9  24 7F                           and al, 0x7f
00395AFB  3C 15                           cmp al, 0x15
00395AFD  0F 84 2F 01 00 00               je 0x140395c32
00395B03  F0 FF 42 28                     lock inc dword ptr [rdx + 0x28]
00395B07  48 8B CB                        mov rcx, rbx
00395B0A  E8 C1 A7 EB FF                  call 0x1402502d0
00395B0F  0F B6 83 84 01 00 00            movzx eax, byte ptr [rbx + 0x184]
00395B16  3C 01                           cmp al, 1
00395B18  0F 84 0D 02 00 00               je 0x140395d2b
00395B1E  3C 05                           cmp al, 5
00395B20  75 22                           jne 0x140395b44
00395B22  48 B8 20 03 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000320
00395B2C  8B 08                           mov ecx, dword ptr [rax]
00395B2E  2B 8B B4 01 00 00               sub ecx, dword ptr [rbx + 0x1b4]
00395B34  44 38 B3 87 01 00 00            cmp byte ptr [rbx + 0x187], r14b
00395B3B  74 6D                           je 0x140395baa
00395B3D  48 01 8B E8 03 00 00            add qword ptr [rbx + 0x3e8], rcx
00395B44  48 8B 54 24 30                  mov rdx, qword ptr [rsp + 0x30]
00395B49  48 8D 8B D8 00 00 00            lea rcx, [rbx + 0xd8]
00395B50  C6 83 84 01 00 00 07            mov byte ptr [rbx + 0x184], 7
00395B57  48 8B 82 08 2D 00 00            mov rax, qword ptr [rdx + 0x2d08]
00395B5E  48 89 01                        mov qword ptr [rcx], rax
00395B61  48 89 8A 08 2D 00 00            mov qword ptr [rdx + 0x2d08], rcx
00395B68  4C 89 A3 C8 00 00 00            mov qword ptr [rbx + 0xc8], r12
00395B6F  4C 89 B3 D0 03 00 00            mov qword ptr [rbx + 0x3d0], r14
00395B76  41 B7 01                        mov r15b, 1
00395B79  4C 89 73 40                     mov qword ptr [rbx + 0x40], r14
00395B7D  0F B6 47 11                     movzx eax, byte ptr [rdi + 0x11]
00395B81  FE C0                           inc al
00395B83  88 47 11                        mov byte ptr [rdi + 0x11], al
00395B86  45 84 FF                        test r15b, r15b
00395B89  0F 85 E2 00 00 00               jne 0x140395c71
00395B8F  4D 8D 7D 08                     lea r15, [r13 + 8]
00395B93  49 3B F7                        cmp rsi, r15
00395B96  0F 85 44 FC FF FF               jne 0x1403957e0
00395B9C  48 8B 74 24 30                  mov rsi, qword ptr [rsp + 0x30]
00395BA1  8B AC 24 A0 00 00 00            mov ebp, dword ptr [rsp + 0xa0]
00395BA8  EB 67                           jmp 0x140395c11
00395BAA  48 01 8B E0 03 00 00            add qword ptr [rbx + 0x3e0], rcx
00395BB1  EB 91                           jmp 0x140395b44
00395BB3  33 D2                           xor edx, edx
00395BB5  B1 01                           mov cl, 1
00395BB7  E8 24 47 64 00                  call 0x1409da2e0
00395BBC  4C 8B E0                        mov r12, rax
00395BBF  48 85 C0                        test rax, rax
00395BC2  0F 85 4F FB FF FF               jne 0x140395717
00395BC8  E9 E7 FC FF FF                  jmp 0x1403958b4
00395BCD  48 89 30                        mov qword ptr [rax], rsi
00395BD0  45 32 FF                        xor r15b, r15b
00395BD3  48 89 46 08                     mov qword ptr [rsi + 8], rax
00395BD7  41 8B EE                        mov ebp, r14d
00395BDA  48 8B 5F 18                     mov rbx, qword ptr [rdi + 0x18]
00395BDE  66 90                           nop
00395BE0  F0 48 0F BA 6B 40 00            lock bts qword ptr [rbx + 0x40], 0
00395BE7  0F 83 DC FE FF FF               jae 0x140395ac9
00395BED  FF C5                           inc ebp
00395BEF  85 2D B7 F6 C2 00               test dword ptr [rip + 0xc2f6b7], ebp
00395BF5  0F 84 86 00 00 00               je 0x140395c81
00395BFB  F3 90                           pause
00395BFD  48 8B 43 40                     mov rax, qword ptr [rbx + 0x40]
00395C01  48 85 C0                        test rax, rax
00395C04  74 DA                           je 0x140395be0
00395C06  EB E5                           jmp 0x140395bed
00395C08  40 84 FF                        test dil, dil
00395C0B  0F 85 B8 FB FF FF               jne 0x1403957c9
00395C11  41 8B 4D 04                     mov ecx, dword ptr [r13 + 4]
00395C15  8D 41 01                        lea eax, [rcx + 1]
00395C18  41 89 45 04                     mov dword ptr [r13 + 4], eax
00395C1C  49 8D 45 18                     lea rax, [r13 + 0x18]
00395C20  48 8B 50 08                     mov rdx, qword ptr [rax + 8]
00395C24  48 39 02                        cmp qword ptr [rdx], rax
00395C27  0F 85 D6 FB FF FF               jne 0x140395803
00395C2D  E9 18 FC FF FF                  jmp 0x14039584a
00395C32  8B 83 1C 02 00 00               mov eax, dword ptr [rbx + 0x21c]
00395C38  0F B6 C0                        movzx eax, al
00395C3B  89 83 1C 02 00 00               mov dword ptr [rbx + 0x21c], eax
00395C41  F0 FF 84 82 18 02 00 00         lock inc dword ptr [rdx + rax*4 + 0x218]
00395C49  E9 B9 FE FF FF                  jmp 0x140395b07
00395C4E  40 0F B6 D6                     movzx edx, sil
00395C52  40 0F B6 CD                     movzx ecx, bpl
00395C56  E8 A1 FA 15 00                  call 0x1404f56fc
00395C5B  E9 F9 F9 FF FF                  jmp 0x140395659
00395C60  40 0F B6 D6                     movzx edx, sil
00395C64  0F B6 C8                        movzx ecx, al
00395C67  E8 90 FA 15 00                  call 0x1404f56fc
00395C6C  E9 D8 FA FF FF                  jmp 0x140395749
00395C71  8B AC 24 A0 00 00 00            mov ebp, dword ptr [rsp + 0xa0]
00395C78  4D 89 34 24                     mov qword ptr [r12], r14
00395C7C  E9 ED FB FF FF                  jmp 0x14039586e
00395C81  8B 05 31 0E C3 00               mov eax, dword ptr [rip + 0xc30e31]
00395C87  A8 40                           test al, 0x40
00395C89  0F 84 6C FF FF FF               je 0x140395bfb
00395C8F  E8 FC 97 F7 FF                  call 0x14030f490
00395C94  84 C0                           test al, al
00395C96  0F 84 5F FF FF FF               je 0x140395bfb
00395C9C  8B CD                           mov ecx, ebp
00395C9E  E8 BD 97 F7 FF                  call 0x14030f460
00395CA3  E9 55 FF FF FF                  jmp 0x140395bfd
00395CA8  48 8B CB                        mov rcx, rbx
00395CAB  E8 70 0A 00 00                  call 0x140396720
00395CB0  44 0F B6 C0                     movzx r8d, al
00395CB4  48 8B CB                        mov rcx, rbx
00395CB7  49 8B D4                        mov rdx, r12
00395CBA  E8 8D 0A 00 00                  call 0x14039674c
00395CBF  E9 A7 FA FF FF                  jmp 0x14039576b
00395CC4  33 D2                           xor edx, edx
00395CC6  48 81 C1 18 05 00 00            add rcx, 0x518
00395CCD  48 89 54 24 28                  mov qword ptr [rsp + 0x28], rdx
00395CD2  BA 01 00 00 00                  mov edx, 1
00395CD7  44 8B C2                        mov r8d, edx
00395CDA  C7 44 24 20 02 00 00 00         mov dword ptr [rsp + 0x20], 2
00395CE2  E8 D9 0B FB FF                  call 0x1403468c0
00395CE7  E9 C8 FB FF FF                  jmp 0x1403958b4
00395CEC  83 6D 04 01                     sub dword ptr [rbp + 4], 1
00395CF0  0F 85 5C FD FF FF               jne 0x140395a52
00395CF6  48 8B BC 24 B8 00 00 00         mov rdi, qword ptr [rsp + 0xb8]
00395CFE  F0 81 65 00 7F FF FF FF         lock and dword ptr [rbp], 0xffffff7f
00395D06  41 F6 DF                        neg r15b
00395D09  40 88 7C 24 20                  mov byte ptr [rsp + 0x20], dil
00395D0E  41 B9 01 00 00 00               mov r9d, 1
00395D14  1B D2                           sbb edx, edx
00395D16  45 8B C1                        mov r8d, r9d
00395D19  83 E2 03                        and edx, 3
00395D1C  E9 8B FB FF FF                  jmp 0x1403958ac
00395D21  B9 03 00 00 00                  mov ecx, 3
00395D26  E9 63 FB FF FF                  jmp 0x14039588e
00395D2B  83 4B 74 02                     or dword ptr [rbx + 0x74], 2
00395D2F  E9 10 FE FF FF                  jmp 0x140395b44
00395D34  80 BB 83 02 00 00 0F            cmp byte ptr [rbx + 0x283], 0xf
00395D3B  0F 85 98 FA FF FF               jne 0x1403957d9
00395D41  E9 CB FE FF FF                  jmp 0x140395c11
00395D46  0F B6 83 84 01 00 00            movzx eax, byte ptr [rbx + 0x184]
00395D4D  3C 05                           cmp al, 5
00395D4F  0F 85 E6 00 00 00               jne 0x140395e3b
00395D55  0F B6 4B 70                     movzx ecx, byte ptr [rbx + 0x70]
00395D59  8B C1                           mov eax, ecx
00395D5B  83 E0 07                        and eax, 7
00395D5E  83 F8 01                        cmp eax, 1
00395D61  0F 85 54 04 00 00               jne 0x1403961bb
00395D67  48 8B 93 E8 00 00 00            mov rdx, qword ptr [rbx + 0xe8]
00395D6E  48 85 D2                        test rdx, rdx
00395D71  74 11                           je 0x140395d84
00395D73  0F B6 02                        movzx eax, byte ptr [rdx]
00395D76  24 7F                           and al, 0x7f
00395D78  3C 15                           cmp al, 0x15
00395D7A  0F 84 4E 02 00 00               je 0x140395fce
00395D80  F0 FF 42 28                     lock inc dword ptr [rdx + 0x28]
00395D84  48 8B CB                        mov rcx, rbx
00395D87  E8 44 A5 EB FF                  call 0x1402502d0
00395D8C  48 8B CB                        mov rcx, rbx
00395D8F  E8 8C 16 00 00                  call 0x140397420
00395D94  48 8B 94 24 A0 00 00 00         mov rdx, qword ptr [rsp + 0xa0]
00395D9C  48 8D 8B D8 00 00 00            lea rcx, [rbx + 0xd8]
00395DA3  45 33 C0                        xor r8d, r8d
00395DA6  41 B4 01                        mov r12b, 1
00395DA9  48 8B 82 08 2D 00 00            mov rax, qword ptr [rdx + 0x2d08]
00395DB0  48 89 01                        mov qword ptr [rcx], rax
00395DB3  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
00395DB8  48 89 8A 08 2D 00 00            mov qword ptr [rdx + 0x2d08], rcx
00395DBF  48 89 83 C8 00 00 00            mov qword ptr [rbx + 0xc8], rax
00395DC6  4C 89 83 D0 03 00 00            mov qword ptr [rbx + 0x3d0], r8
00395DCD  4C 89 43 40                     mov qword ptr [rbx + 0x40], r8
00395DD1  0F B6 46 11                     movzx eax, byte ptr [rsi + 0x11]
00395DD5  48 8B 9C 24 A0 00 00 00         mov rbx, qword ptr [rsp + 0xa0]
00395DDD  FE C0                           inc al
00395DDF  88 46 11                        mov byte ptr [rsi + 0x11], al
00395DE2  45 84 E4                        test r12b, r12b
00395DE5  0F 84 7D FB FF FF               je 0x140395968
00395DEB  41 83 6F 04 01                  sub dword ptr [r15 + 4], 1
00395DF0  0F 85 72 FB FF FF               jne 0x140395968
00395DF6  48 8B BC 24 B8 00 00 00         mov rdi, qword ptr [rsp + 0xb8]
00395DFE  F0 41 81 27 7F FF FF FF         lock and dword ptr [r15], 0xffffff7f
00395E06  40 84 ED                        test bpl, bpl
00395E09  40 88 7C 24 20                  mov byte ptr [rsp + 0x20], dil
00395E0E  BA 01 00 00 00                  mov edx, 1
00395E13  B9 03 00 00 00                  mov ecx, 3
00395E18  41 B9 01 00 00 00               mov r9d, 1
00395E1E  0F 45 D1                        cmovne edx, ecx
00395E21  45 8B C1                        mov r8d, r9d
00395E24  E9 83 FA FF FF                  jmp 0x1403958ac
00395E29  83 F8 05                        cmp eax, 5
00395E2C  0F 85 12 04 00 00               jne 0x140396244
00395E32  80 E1 FE                        and cl, 0xfe
00395E35  80 C9 06                        or cl, 6
00395E38  88 4B 70                        mov byte ptr [rbx + 0x70], cl
00395E3B  45 33 C0                        xor r8d, r8d
00395E3E  EB 8D                           jmp 0x140395dcd
00395E40  0F B6 83 84 01 00 00            movzx eax, byte ptr [rbx + 0x184]
00395E47  3C 05                           cmp al, 5
00395E49  0F 85 AD 00 00 00               jne 0x140395efc
00395E4F  0F B6 4B 70                     movzx ecx, byte ptr [rbx + 0x70]
00395E53  8B C1                           mov eax, ecx
00395E55  83 E0 07                        and eax, 7
00395E58  83 F8 01                        cmp eax, 1
00395E5B  0F 85 1E 03 00 00               jne 0x14039617f
00395E61  48 8B 93 E8 00 00 00            mov rdx, qword ptr [rbx + 0xe8]
00395E68  48 85 D2                        test rdx, rdx
00395E6B  74 11                           je 0x140395e7e
00395E6D  0F B6 02                        movzx eax, byte ptr [rdx]
00395E70  24 7F                           and al, 0x7f
00395E72  3C 15                           cmp al, 0x15
00395E74  0F 84 E1 00 00 00               je 0x140395f5b
00395E7A  F0 FF 42 28                     lock inc dword ptr [rdx + 0x28]
00395E7E  48 8B CB                        mov rcx, rbx
00395E81  E8 4A A4 EB FF                  call 0x1402502d0
00395E86  48 8B CB                        mov rcx, rbx
00395E89  E8 92 15 00 00                  call 0x140397420
00395E8E  48 8B 94 24 A0 00 00 00         mov rdx, qword ptr [rsp + 0xa0]
00395E96  48 8D 8B D8 00 00 00            lea rcx, [rbx + 0xd8]
00395E9D  45 33 C0                        xor r8d, r8d
00395EA0  41 B5 01                        mov r13b, 1
00395EA3  48 8B 82 08 2D 00 00            mov rax, qword ptr [rdx + 0x2d08]
00395EAA  48 89 01                        mov qword ptr [rcx], rax
00395EAD  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
00395EB2  48 89 8A 08 2D 00 00            mov qword ptr [rdx + 0x2d08], rcx
00395EB9  48 89 83 C8 00 00 00            mov qword ptr [rbx + 0xc8], rax
00395EC0  4C 89 83 D0 03 00 00            mov qword ptr [rbx + 0x3d0], r8
00395EC7  4C 89 43 40                     mov qword ptr [rbx + 0x40], r8
00395ECB  0F B6 46 11                     movzx eax, byte ptr [rsi + 0x11]
00395ECF  48 8B 9C 24 A0 00 00 00         mov rbx, qword ptr [rsp + 0xa0]
00395ED7  FE C0                           inc al
00395ED9  88 46 11                        mov byte ptr [rsi + 0x11], al
00395EDC  45 84 ED                        test r13b, r13b
00395EDF  0F 84 6D FB FF FF               je 0x140395a52
00395EE5  E9 02 FE FF FF                  jmp 0x140395cec
00395EEA  83 F8 05                        cmp eax, 5
00395EED  0F 85 20 03 00 00               jne 0x140396213
00395EF3  80 E1 FE                        and cl, 0xfe
00395EF6  80 C9 06                        or cl, 6
00395EF9  88 4B 70                        mov byte ptr [rbx + 0x70], cl
00395EFC  45 33 C0                        xor r8d, r8d
00395EFF  EB C6                           jmp 0x140395ec7
00395F01  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
00395F06  E8 A5 1F EC FF                  call 0x140257eb0
00395F0B  E9 6C F7 FF FF                  jmp 0x14039567c
00395F10  40 0F B6 D6                     movzx edx, sil
00395F14  40 0F B6 CF                     movzx ecx, dil
00395F18  E8 DF F7 15 00                  call 0x1404f56fc
00395F1D  E9 EA FA FF FF                  jmp 0x140395a0c
00395F22  3C 02                           cmp al, 2
00395F24  0F 85 01 02 00 00               jne 0x14039612b
00395F2A  C6 46 11 05                     mov byte ptr [rsi + 0x11], 5
00395F2E  48 8B D6                        mov rdx, rsi
00395F31  48 8B 4E 18                     mov rcx, qword ptr [rsi + 0x18]
00395F35  E8 F6 3B E8 FF                  call 0x140219b30
00395F3A  83 6D 04 01                     sub dword ptr [rbp + 4], 1
00395F3E  0F 84 B2 FD FF FF               je 0x140395cf6
00395F44  E9 06 FB FF FF                  jmp 0x140395a4f
00395F49  40 0F B6 D6                     movzx edx, sil
00395F4D  40 0F B6 CF                     movzx ecx, dil
00395F51  E8 A6 F7 15 00                  call 0x1404f56fc
00395F56  E9 C4 F9 FF FF                  jmp 0x14039591f
00395F5B  8B 83 1C 02 00 00               mov eax, dword ptr [rbx + 0x21c]
00395F61  0F B6 C0                        movzx eax, al
00395F64  89 83 1C 02 00 00               mov dword ptr [rbx + 0x21c], eax
00395F6A  F0 FF 84 82 18 02 00 00         lock inc dword ptr [rdx + rax*4 + 0x218]
00395F72  E9 07 FF FF FF                  jmp 0x140395e7e
00395F77  3C 02                           cmp al, 2
00395F79  0F 85 CD 01 00 00               jne 0x14039614c
00395F7F  C6 46 11 05                     mov byte ptr [rsi + 0x11], 5
00395F83  48 8B D6                        mov rdx, rsi
00395F86  48 8B 4E 18                     mov rcx, qword ptr [rsi + 0x18]
00395F8A  E8 A1 3B E8 FF                  call 0x140219b30
00395F8F  41 83 6F 04 01                  sub dword ptr [r15 + 4], 1
00395F94  0F 84 5C FE FF FF               je 0x140395df6
00395F9A  E9 C6 F9 FF FF                  jmp 0x140395965
00395F9F  40 B7 01                        mov dil, 1
00395FA2  E9 03 F8 FF FF                  jmp 0x1403957aa
00395FA7  8B 05 0B 0B C3 00               mov eax, dword ptr [rip + 0xc30b0b]
00395FAD  A8 40                           test al, 0x40
00395FAF  0F 84 07 FB FF FF               je 0x140395abc
00395FB5  E8 D6 94 F7 FF                  call 0x14030f490
00395FBA  84 C0                           test al, al
00395FBC  0F 84 FA FA FF FF               je 0x140395abc
00395FC2  8B CF                           mov ecx, edi
00395FC4  E8 97 94 F7 FF                  call 0x14030f460
00395FC9  E9 F0 FA FF FF                  jmp 0x140395abe
00395FCE  8B 83 1C 02 00 00               mov eax, dword ptr [rbx + 0x21c]
00395FD4  0F B6 C0                        movzx eax, al
00395FD7  89 83 1C 02 00 00               mov dword ptr [rbx + 0x21c], eax
00395FDD  F0 FF 84 82 18 02 00 00         lock inc dword ptr [rdx + rax*4 + 0x218]
00395FE5  E9 9A FD FF FF                  jmp 0x140395d84
00395FEA  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
00395FEF  E8 EC CC FA FF                  call 0x140342ce0
00395FF4  48 8B 57 28                     mov rdx, qword ptr [rdi + 0x28]
00395FF8  41 0F B6 C6                     movzx eax, r14b
00395FFC  F6 D8                           neg al
00395FFE  44 89 64 24 28                  mov dword ptr [rsp + 0x28], r12d
00396003  49 8B CD                        mov rcx, r13
00396006  C6 44 24 20 00                  mov byte ptr [rsp + 0x20], 0
0039600B  4D 1B C0                        sbb r8, r8
0039600E  45 33 C9                        xor r9d, r9d
00396011  E8 6A 14 00 00                  call 0x140397480
00396016  85 C0                           test eax, eax
00396018  0F 84 3B 02 00 00               je 0x140396259
0039601E  B8 11 00 00 00                  mov eax, 0x11
00396023  33 D2                           xor edx, edx
00396025  F0 48 0F B1 97 60 01 00 00      lock cmpxchg qword ptr [rdi + 0x160], rdx
0039602E  74 0C                           je 0x14039603c
00396030  48 8D 8F 60 01 00 00            lea rcx, [rdi + 0x160]
00396037  E8 04 D4 EC FF                  call 0x140263440
0039603C  48 8D 8F 60 01 00 00            lea rcx, [rdi + 0x160]
00396043  E8 B8 B5 F4 FF                  call 0x1402e1600
00396048  E9 67 F8 FF FF                  jmp 0x1403958b4
0039604D  8B 05 65 0A C3 00               mov eax, dword ptr [rip + 0xc30a65]
00396053  A8 40                           test al, 0x40
00396055  0F 84 80 F9 FF FF               je 0x1403959db
0039605B  E8 30 94 F7 FF                  call 0x14030f490
00396060  84 C0                           test al, al
00396062  0F 84 73 F9 FF FF               je 0x1403959db
00396068  8B CF                           mov ecx, edi
0039606A  E8 F1 93 F7 FF                  call 0x14030f460
0039606F  E9 69 F9 FF FF                  jmp 0x1403959dd
00396074  F0 81 65 00 7F FF FF FF         lock and dword ptr [rbp], 0xffffff7f
0039607C  83 3D 9D 0C C3 00 00            cmp dword ptr [rip + 0xc30c9d], 0
00396083  74 0D                           je 0x140396092
00396085  44 0F 20 C1                     mov rcx, cr8
00396089  40 0F B6 D7                     movzx edx, dil
0039608D  E8 06 F6 15 00                  call 0x1404f5698
00396092  40 0F B6 C7                     movzx eax, dil
00396096  44 0F 22 C0                     mov cr8, rax
0039609A  B9 47 00 00 C0                  mov ecx, 0xc0000047
0039609F  E8 AC 09 F6 FF                  call 0x1402f6a50
003960A4  CC                              int3
003960A5  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
003960AA  48 8B CB                        mov rcx, rbx
003960AD  48 8B 53 08                     mov rdx, qword ptr [rbx + 8]
003960B1  E8 66 9D 06 00                  call 0x1403ffe1c
003960B6  B9 06 00 00 00                  mov ecx, 6
003960BB  E9 D3 F7 FF FF                  jmp 0x140395893
003960C0  F0 41 81 27 7F FF FF FF         lock and dword ptr [r15], 0xffffff7f
003960C8  83 3D 51 0C C3 00 00            cmp dword ptr [rip + 0xc30c51], 0
003960CF  74 0D                           je 0x1403960de
003960D1  44 0F 20 C1                     mov rcx, cr8
003960D5  40 0F B6 D7                     movzx edx, dil
003960D9  E8 BA F5 15 00                  call 0x1404f5698
003960DE  40 0F B6 C7                     movzx eax, dil
003960E2  44 0F 22 C0                     mov cr8, rax
003960E6  E9 C9 F7 FF FF                  jmp 0x1403958b4
003960EB  83 F8 04                        cmp eax, 4
003960EE  0F 84 F6 F9 FF FF               je 0x140395aea
003960F4  85 C0                           test eax, eax
003960F6  75 20                           jne 0x140396118
003960F8  80 E1 FA                        and cl, 0xfa
003960FB  80 C9 02                        or cl, 2
003960FE  88 4B 70                        mov byte ptr [rbx + 0x70], cl
00396101  4C 89 A3 C8 00 00 00            mov qword ptr [rbx + 0xc8], r12
00396108  4C 89 B3 D0 03 00 00            mov qword ptr [rbx + 0x3d0], r14
0039610F  44 88 77 11                     mov byte ptr [rdi + 0x11], r14b
00396113  E9 5E FA FF FF                  jmp 0x140395b76
00396118  83 F8 05                        cmp eax, 5
0039611B  75 50                           jne 0x14039616d
0039611D  80 E1 FE                        and cl, 0xfe
00396120  80 C9 06                        or cl, 6
00396123  88 4B 70                        mov byte ptr [rbx + 0x70], cl
00396126  E9 4E FA FF FF                  jmp 0x140395b79
0039612B  3C 04                           cmp al, 4
0039612D  0F 84 C4 00 00 00               je 0x1403961f7
00396133  45 33 C9                        xor r9d, r9d
00396136  41 B8 00 01 00 00               mov r8d, 0x100
0039613C  48 8B D6                        mov rdx, rsi
0039613F  48 8B CB                        mov rcx, rbx
00396142  E8 89 A5 FB FF                  call 0x1403506d0
00396147  E9 03 F9 FF FF                  jmp 0x140395a4f
0039614C  3C 04                           cmp al, 4
0039614E  0F 84 D4 00 00 00               je 0x140396228
00396154  45 33 C9                        xor r9d, r9d
00396157  41 B8 00 01 00 00               mov r8d, 0x100
0039615D  48 8B D6                        mov rdx, rsi
00396160  48 8B CB                        mov rcx, rbx
00396163  E8 68 A5 FB FF                  call 0x1403506d0
00396168  E9 F8 F7 FF FF                  jmp 0x140395965
0039616D  83 F8 03                        cmp eax, 3
00396170  0F 85 03 FA FF FF               jne 0x140395b79
00396176  C6 47 11 02                     mov byte ptr [rdi + 0x11], 2
0039617A  E9 FA F9 FF FF                  jmp 0x140395b79
0039617F  83 F8 04                        cmp eax, 4
00396182  0F 84 D9 FC FF FF               je 0x140395e61
00396188  85 C0                           test eax, eax
0039618A  0F 85 5A FD FF FF               jne 0x140395eea
00396190  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
00396195  80 E1 FA                        and cl, 0xfa
00396198  80 C9 02                        or cl, 2
0039619B  41 B5 01                        mov r13b, 1
0039619E  88 4B 70                        mov byte ptr [rbx + 0x70], cl
003961A1  45 33 C0                        xor r8d, r8d
003961A4  48 89 83 C8 00 00 00            mov qword ptr [rbx + 0xc8], rax
003961AB  4C 89 83 D0 03 00 00            mov qword ptr [rbx + 0x3d0], r8
003961B2  44 88 46 11                     mov byte ptr [rsi + 0x11], r8b
003961B6  E9 0C FD FF FF                  jmp 0x140395ec7
003961BB  83 F8 04                        cmp eax, 4
003961BE  0F 84 A3 FB FF FF               je 0x140395d67
003961C4  85 C0                           test eax, eax
003961C6  0F 85 5D FC FF FF               jne 0x140395e29
003961CC  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
003961D1  80 E1 FA                        and cl, 0xfa
003961D4  80 C9 02                        or cl, 2
003961D7  41 B4 01                        mov r12b, 1
003961DA  88 4B 70                        mov byte ptr [rbx + 0x70], cl
003961DD  45 33 C0                        xor r8d, r8d
003961E0  48 89 83 C8 00 00 00            mov qword ptr [rbx + 0xc8], rax
003961E7  4C 89 83 D0 03 00 00            mov qword ptr [rbx + 0x3d0], r8
003961EE  44 88 46 11                     mov byte ptr [rsi + 0x11], r8b
003961F2  E9 D6 FB FF FF                  jmp 0x140395dcd
003961F7  C6 46 11 05                     mov byte ptr [rsi + 0x11], 5
003961FB  48 8B D5                        mov rdx, rbp
003961FE  44 89 45 04                     mov dword ptr [rbp + 4], r8d
00396202  4C 8B C6                        mov r8, rsi
00396205  48 8B 4E 18                     mov rcx, qword ptr [rsi + 0x18]
00396209  E8 42 1A E7 FF                  call 0x140207c50
0039620E  E9 3C F8 FF FF                  jmp 0x140395a4f
00396213  45 33 C0                        xor r8d, r8d
00396216  83 F8 03                        cmp eax, 3
00396219  0F 85 A8 FC FF FF               jne 0x140395ec7
0039621F  C6 46 11 02                     mov byte ptr [rsi + 0x11], 2
00396223  E9 9F FC FF FF                  jmp 0x140395ec7
00396228  C6 46 11 05                     mov byte ptr [rsi + 0x11], 5
0039622C  49 8B D7                        mov rdx, r15
0039622F  45 89 47 04                     mov dword ptr [r15 + 4], r8d
00396233  4C 8B C6                        mov r8, rsi
00396236  48 8B 4E 18                     mov rcx, qword ptr [rsi + 0x18]
0039623A  E8 11 1A E7 FF                  call 0x140207c50
0039623F  E9 21 F7 FF FF                  jmp 0x140395965
00396244  45 33 C0                        xor r8d, r8d
00396247  83 F8 03                        cmp eax, 3
0039624A  0F 85 7D FB FF FF               jne 0x140395dcd
00396250  C6 46 11 02                     mov byte ptr [rsi + 0x11], 2
00396254  E9 74 FB FF FF                  jmp 0x140395dcd
00396259  48 8D 54 24 40                  lea rdx, [rsp + 0x40]
0039625E  48 8B CB                        mov rcx, rbx
00396261  E8 3A F5 ED FF                  call 0x1402757a0
00396266  45 84 F6                        test r14b, r14b
00396269  0F 84 6D F7 34 00               je 0x1406e59dc
0039626F  FF 43 14                        inc dword ptr [rbx + 0x14]
00396272  E9 68 F7 34 00                  jmp 0x1406e59df
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall AlpcpSignal(__int64 a1, unsigned __int8 a2, unsigned __int8 a3)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int8 v_stack_m78;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p40;
    unsigned int v_stack_p8;
    unsigned __int64 v_stack_pA0;
    unsigned __int64 v_stack_pB8;

    v_stack_p10 = v_rbx;
    v_rsp = (v_rsp) - (96);
    if (*(unsigned __int64 *)(a1 + 32) == 0) goto loc_0039580A;
    if ((*(unsigned __int8 *)(a1 + 58)) == 0) goto loc_003959E8;
    result = 0;
    v_stack_m58 = v_xmm0;
    v_stack_m50 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 48);
    v_stack_m58 = 0;
    v_stack_m48 = 0;
    if ((*(unsigned int *)(v_rip + 12785357)) != 0) goto loc_00395C4E;
loc_00395659:
    v_stack_m48 = (unsigned __int8)(v_cr8);
    if (((*(unsigned __int8 *)(v_rip + 12784806)) & (33)) != 0) goto loc_003958CD;
loc_0039566B:
    if (v_stack_m58 != 0) goto loc_00395F01;
loc_0039567C:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 48) + 12)))) >= (*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 48) + 8))) goto loc_00395FEA;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 48) + 32) != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 48) + 32));
        *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 48) + 32) = result;
    }
    v_stack_p20 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 48) + 32) + 8);
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 48) + 12) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 48) + 12)) + 1);
    result = KeReleaseInStackQueuedSpinLock(v_stack_m58, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 48) + 12)), a3, a4);
    a2 = 0;
    result = 17;
    if (!(condition_is_equal)) {
        a1 = *(unsigned __int64 *)(a1 + 32) + 352;
        result = ExfReleasePushLockShared(a1, a2, a3, a4);
    }
    result = KeAbPostRelease(*(unsigned __int64 *)(a1 + 32) + 352, a2, a3, a4);
    v_r14 = (unsigned __int8)(-(*(unsigned __int8 *)(a1 + 59)));
    v_r14 = 0;
    result = (0 != 0) ? 1 : 0;
    v_rbp = (unsigned int)(((unsigned int)((unsigned int)(result))) | (4));
    if ((unsigned int)((unsigned int)(a3)) == 0) { v_rbp = (unsigned int)(result); }
    v_stack_p8 = (unsigned int)(v_rbp);
    if (v_stack_p20 == 0) goto loc_00395BB3;
loc_00395717:
    *(unsigned __int64 *)(v_stack_p20 + 24) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 40);
    *(unsigned __int64 *)(v_stack_p20 + 32) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 48);
    *(unsigned int *)(v_stack_p20 + 40) = 0;
    *(unsigned __int64 *)(v_stack_p20 + 48) = 0;
    v_stack_m60 = 2;
    if ((*(unsigned int *)(v_rip + 12785117)) != 0) goto loc_00395C60;
loc_00395749:
    v_stack_m68 = *(unsigned __int64 *)(gs_base + (0 + 32));
    if ((*(unsigned int *)(v_rip + 12785117)) < 0) goto loc_00395CA8;
loc_0039576B:
    result = (unsigned __int8)(~(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 32) + 1)));
    result = (unsigned int)((result) >> (1));
    result = (unsigned int)((result) & (1));
    v_stack_p20 = (unsigned int)(result);
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 1616);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 1616) == 0) { result = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8); }
    if ((unsigned int)(v_rbp) == 0) goto loc_003957A7;
    if (condition_is_below) goto loc_00395F9F;
loc_003957A7:
    v_rdi = 0;
loc_003957AA:
    result = KiAcquireKobjectLockSafe(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 32), a2, a3, a4);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 32) + 8)) == (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 32) + 8)) goto loc_00395C11;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 32) + 40)))) >= (*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 32) + 44))) goto loc_00395C08;
loc_003957C9:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 232)) == (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 32))) goto loc_00395D34;
loc_003957D9:
loc_003957E0:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 32) + 8) + 16)) != 3) goto loc_00395B9C;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 32) + 8)) + 8)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 32) + 8))) goto loc_00395803;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 32) + 8) + 8))) == (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 32) + 8))) goto loc_00395BCD;
loc_00395803:
loc_0039580A:
    if (*(unsigned __int64 *)(3 + 24) != 0) goto loc_003958ED;
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 40))) & (1)) == 0) goto loc_003958B4;
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 32) + 8) + 8);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 40)) >= 4) {
        a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 40)) & (-4);
        a3 = (unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 32) + 8);
        a2 = 0;
        result = KeSetEvent(a1, a2, a3, a4);
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 40);
        result = AlpcpReleaseDirectAttribute(a1, a2, a3, a4);
    }
    a2 = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 40) = 0;
    goto loc_003958B4;
loc_0039584A:
    *(unsigned __int64 *)(v_stack_p20) = result;
    *(unsigned __int64 *)(v_stack_p20 + 8) = 0;
    *(unsigned __int64 *)(a2) = v_stack_p20;
    *(unsigned __int64 *)(result + 8) = v_stack_p20;
    if ((unsigned int)(a1) != 0) goto loc_0039586E;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 32) + 8)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 32) + 8)) {
        a2 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 32);
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 32) + 8));
        result = KiWakeOtherQueueWaiters(a1, a2, a3, a4);
    }
    if ((((unsigned __int8)(v_rbp)) & (1)) != 0) goto loc_00395D21;
    if ((((unsigned __int8)(v_rbp)) & (4)) != 0) goto loc_003960A5;
loc_0039588E:
loc_00395893:
    v_stack_m78 = (unsigned __int8)(v_stack_m60);
loc_003958AC:
    result = KiExitDispatcher(v_stack_m68, 0, 1, (unsigned int)(v_stack_p20));
loc_003958B4:
    v_rsp = (v_rsp) + (96);
    return result;
loc_003958CD:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12027269))) != 0) goto loc_0039566B;
    result = KiAcquireQueuedSpinLockInstrumented(v_stack_p40, v_stack_p10, 1, (unsigned int)(v_stack_p20));
    goto loc_0039567C;
loc_003958ED:
    if ((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 32) + 8) == 0) goto loc_00395CC4;
    v_stack_pB8 = 2;
    if ((*(unsigned int *)(v_rip + 12784647)) != 0) goto loc_00395F49;
loc_0039591F:
    v_stack_pA0 = *(unsigned __int64 *)(gs_base + (0 + 32));
    result = KiAcquireKobjectLockSafe(v_stack_p40 + 1304, v_stack_p10, 1, (unsigned int)(v_stack_p20));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p40 + 1304 + 4)) + 1)) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p40 + 1304 + 4))))) goto loc_003960C0;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p40 + 1304 + 4)) + 1)) > (*(unsigned int *)(v_stack_p40 + 1304 + 24))) goto loc_003960C0;
    *(unsigned int *)(v_stack_p40 + 1304 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p40 + 1304 + 4)) + 1);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p40 + 1304 + 4))) != 0) goto loc_00395DFE;
loc_00395965:
    a3 = 0;
loc_00395968:
    if ((*(unsigned __int64 *)(v_stack_p40 + 1304 + 8)) == (v_stack_p40 + 1304 + 8)) goto loc_00395DF6;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p40 + 1304 + 8)) + 8)) != (*(unsigned __int64 *)(v_stack_p40 + 1304 + 8))) goto loc_00395803;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p40 + 1304 + 8) + 8))) != (*(unsigned __int64 *)(v_stack_p40 + 1304 + 8))) goto loc_00395803;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p40 + 1304 + 8) + 8)) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p40 + 1304 + 8));
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p40 + 1304 + 8)) + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p40 + 1304 + 8) + 8);
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_p40 + 1304 + 8) + 16))) != 1) goto loc_00395F77;
    v_r12 = 0;
    v_stack_p30 = *(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p40 + 1304 + 8) + 18);
loc_003959C0:
    if (condition_is_above_or_equal) goto loc_00395D46;
loc_003959CD:
    v_rdi = (unsigned int)((0) + 1);
    if (((*(unsigned int *)(v_rip + 12777687)) & ((unsigned int)(v_rdi))) == 0) goto loc_0039604D;
loc_003959DB:
loc_003959DD:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p40 + 1304 + 8) + 24) + 64) == 0) goto loc_003959C0;
    goto loc_003959CD;
loc_003959E8:
    v_stack_pB8 = 2;
    if ((*(unsigned int *)(v_rip + 12784410)) != 0) goto loc_00395F10;
loc_00395A0C:
    v_stack_pA0 = *(unsigned __int64 *)(gs_base + (0 + 32));
    result = KiAcquireKobjectLockSafe(*(unsigned __int64 *)(v_rdi + 248), *(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p40 + 1304 + 8) + 18), a3, (unsigned int)(v_stack_p20));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rdi + 248) + 4)) + 1)) < ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rdi + 248) + 4))))) goto loc_00396074;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rdi + 248) + 4)) + 1)) > (*(unsigned int *)(*(unsigned __int64 *)(v_rdi + 248) + 24))) goto loc_00396074;
    *(unsigned int *)(*(unsigned __int64 *)(v_rdi + 248) + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rdi + 248) + 4)) + 1);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rdi + 248) + 4))) != 0) goto loc_00395CFE;
loc_00395A4F:
    a3 = 0;
loc_00395A52:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 248) + 8)) == (*(unsigned __int64 *)(v_rdi + 248) + 8)) goto loc_00395CF6;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 248) + 8)) + 8)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 248) + 8))) goto loc_00395803;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 248) + 8) + 8))) != (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 248) + 8))) goto loc_00395803;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 248) + 8) + 8)) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 248) + 8));
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 248) + 8)) + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 248) + 8) + 8);
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 248) + 8) + 16))) != 1) goto loc_00395F22;
    v_r13 = 0;
    v_stack_p30 = *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 248) + 8) + 18);
loc_00395AA1:
    if (condition_is_above_or_equal) goto loc_00395E40;
loc_00395AAE:
    v_rdi = (unsigned int)((0) + 1);
    if (((*(unsigned int *)(v_rip + 12777462)) & ((unsigned int)(v_rdi))) == 0) goto loc_00395FA7;
loc_00395ABC:
loc_00395ABE:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 248) + 8) + 24) + 64) == 0) goto loc_00395AA1;
    goto loc_00395AAE;
loc_00395AC9:
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 248) + 8) + 24) + 388))) != 5) goto loc_00395B79;
    result = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 248) + 8) + 24) + 112)))) & (7));
    if (((unsigned int)(result)) != 1) goto loc_003960EB;
loc_00395AEA:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 248) + 8) + 24) + 232) == 0) goto loc_00395B07;
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 248) + 8) + 24) + 232))) & (127));
    if (((unsigned __int8)(result)) == 21) goto loc_00395C32;
loc_00395B07:
    result = KiRemovePrcbWaitEntry(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 248) + 8) + 24), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 248) + 8) + 24) + 232), a3, (unsigned int)(v_stack_p20));
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 248) + 8) + 24) + 388))) == 1) goto loc_00395D2B;
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 248) + 8) + 24) + 388))) != 5) goto loc_00395B44;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 248) + 8) + 24) + 388)))) - (*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 248) + 8) + 24) + 436)));
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 248) + 8) + 24) + 391)) == ((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 248) + 8))))) goto loc_00395BAA;
loc_00395B44:
    *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 248) + 8) + 24) + 388) = 7;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 248) + 8) + 24) + 216) = *(unsigned __int64 *)(v_stack_p30 + 11528);
    *(unsigned __int64 *)(v_stack_p30 + 11528) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 248) + 8) + 24) + 216;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 248) + 8) + 24) + 200) = *(unsigned __int64 *)(v_rdi + 248) + 8;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 248) + 8) + 24) + 976) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 248) + 8));
loc_00395B76:
loc_00395B79:
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 248) + 8) + 24) + 64) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 248) + 8));
    result = (unsigned __int8)((*(unsigned __int8 *)(v_rdi + 17)) + 1);
    *(unsigned __int8 *)(v_rdi + 17) = (unsigned __int8)(result);
    if (1 != 0) goto loc_00395C71;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 248) + 8)) != (v_r13 + 8)) goto loc_003957E0;
loc_00395B9C:
    goto loc_00395C11;
loc_00395BAA:
    goto loc_00395B44;
loc_00395BB3:
    a2 = 0;
    result = IopAllocateMiniCompletionPacket(1, a2, a3, (unsigned int)(v_stack_p20));
    if (result != 0) goto loc_00395717;
    goto loc_003958B4;
loc_00395BCD:
    *(unsigned __int64 *)(result) = v_stack_p30;
    v_r15 = 0;
    *(unsigned __int64 *)(v_stack_p30 + 8) = result;
loc_00395BE0:
    if (condition_is_above_or_equal) goto loc_00395AC9;
loc_00395BED:
    v_rbp = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 248) + 8))))) + 1);
    if (((*(unsigned int *)(v_rip + 12777143)) & ((unsigned int)(v_rbp))) == 0) goto loc_00395C81;
loc_00395BFB:
loc_00395BFD:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 24) + 64) == 0) goto loc_00395BE0;
    goto loc_00395BED;
loc_00395C08:
    if ((unsigned __int8)(v_rdi) != 0) goto loc_003957C9;
loc_00395C11:
    *(unsigned int *)(v_r13 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(v_r13 + 4)) + 1);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_r13 + 24 + 8))) != (v_r13 + 24)) goto loc_00395803;
    goto loc_0039584A;
loc_00395C32:
    *(unsigned int *)(*(unsigned __int64 *)(v_rdi + 24) + 540) = (unsigned int)((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rdi + 24) + 540))));
    goto loc_00395B07;
loc_00395C4E:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(v_rbp), (unsigned __int8)(v_stack_p30), a3, (unsigned int)(v_stack_p20));
    goto loc_00395659;
loc_00395C60:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(result), (unsigned __int8)(v_stack_p30), a3, (unsigned int)(v_stack_p20));
    goto loc_00395749;
loc_00395C71:
    *(unsigned __int64 *)(result) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 248) + 8));
    goto loc_0039586E;
loc_00395C81:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12783153)))) & (64)) == 0) goto loc_00395BFB;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned __int8)(result), (unsigned __int8)(v_stack_p30), a3, (unsigned int)(v_stack_p20));
    if ((unsigned __int8)(result) == 0) goto loc_00395BFB;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)((unsigned int)(v_stack_pA0))), (unsigned __int8)(v_stack_p30), a3, (unsigned int)(v_stack_p20));
    goto loc_00395BFD;
loc_00395CA8:
    result = KeIsThreadRunning(*(unsigned __int64 *)(v_rdi + 24), (unsigned __int8)(v_stack_p30), a3, (unsigned int)(v_stack_p20));
    result = EtwTraceEnqueueWork(*(unsigned __int64 *)(v_rdi + 24), result, (unsigned __int8)(result), (unsigned int)(v_stack_p20));
    goto loc_0039576B;
loc_00395CC4:
    a2 = 0;
    a1 = (*(unsigned __int64 *)(v_rdi + 24)) + (0x518ULL);
    v_stack_p28 = 0;
    v_stack_p20 = 2;
    result = KeReleaseSemaphoreEx(a1, 1, 1, (unsigned int)(v_stack_p20));
    goto loc_003958B4;
loc_00395CEC:
    if (condition_is_not_equal) goto loc_00395A52;
loc_00395CF6:
loc_00395CFE:
    v_r15 = (unsigned __int8)(-(v_r15));
    v_stack_p20 = (unsigned __int8)(v_stack_pB8);
    a2 = (unsigned int)((1) & (3));
    goto loc_003958AC;
loc_00395D21:
    goto loc_0039588E;
loc_00395D2B:
    goto loc_00395B44;
loc_00395D34:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rdi + 24) + 643)) != 15) goto loc_003957D9;
    goto loc_00395C11;
loc_00395D46:
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rdi + 24) + 388))) != 5) goto loc_00395E3B;
    result = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rdi + 24) + 112)))) & (7));
    if (((unsigned int)(result)) != 1) goto loc_003961BB;
loc_00395D67:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 24) + 232) == 0) goto loc_00395D84;
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 24) + 232))) & (127));
    if (((unsigned __int8)(result)) == 21) goto loc_00395FCE;
loc_00395D84:
    result = KiRemovePrcbWaitEntry(*(unsigned __int64 *)(v_rdi + 24), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 24) + 232), 1, 1);
    result = KiEnterDeferredReadyState(*(unsigned __int64 *)(v_rdi + 24), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 24) + 232), 1, 1);
    a3 = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 24) + 216) = *(unsigned __int64 *)(v_stack_pA0 + 11528);
    *(unsigned __int64 *)(v_stack_pA0 + 11528) = *(unsigned __int64 *)(v_rdi + 24) + 216;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 24) + 200) = v_stack_p30;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 24) + 976) = 0;
loc_00395DCD:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 24) + 64) = 0;
    result = (unsigned __int8)((*(unsigned __int8 *)(v_stack_p30 + 17)) + 1);
    *(unsigned __int8 *)(v_stack_p30 + 17) = (unsigned __int8)(result);
    if (1 == 0) goto loc_00395968;
    if (1 != 0) goto loc_00395968;
loc_00395DF6:
loc_00395DFE:
    v_stack_p20 = (unsigned __int8)(v_stack_pB8);
    a2 = 1;
    if ((unsigned __int8)((unsigned int)(v_stack_pA0)) != 0) { a2 = 3; }
    goto loc_003958AC;
loc_00395E29:
    if (((unsigned int)(result)) != 5) goto loc_00396244;
    a1 = (unsigned __int8)((3) & (254));
    a1 = (unsigned __int8)((a1) | (6));
    *(unsigned __int8 *)(v_stack_pA0 + 112) = (unsigned __int8)(a1);
loc_00395E3B:
    a3 = 0;
    goto loc_00395DCD;
loc_00395E40:
    if (((unsigned __int8)(*(unsigned __int8 *)(v_stack_pA0 + 388))) != 5) goto loc_00395EFC;
    result = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int8 *)(v_stack_pA0 + 112)))) & (7));
    if (((unsigned int)(result)) != 1) goto loc_0039617F;
loc_00395E61:
    if (*(unsigned __int64 *)(v_stack_pA0 + 232) == 0) goto loc_00395E7E;
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_pA0 + 232))) & (127));
    if (((unsigned __int8)(result)) == 21) goto loc_00395F5B;
loc_00395E7E:
    result = KiRemovePrcbWaitEntry(v_stack_pA0, *(unsigned __int64 *)(v_stack_pA0 + 232), a3, 1);
    result = KiEnterDeferredReadyState(v_stack_pA0, *(unsigned __int64 *)(v_stack_pA0 + 232), a3, 1);
    a3 = 0;
    *(unsigned __int64 *)(v_stack_pA0 + 216) = *(unsigned __int64 *)(v_stack_pA0 + 11528);
    *(unsigned __int64 *)(v_stack_pA0 + 11528) = v_stack_pA0 + 216;
    *(unsigned __int64 *)(v_stack_pA0 + 200) = v_stack_p30;
    *(unsigned __int64 *)(v_stack_pA0 + 976) = 0;
loc_00395EC7:
    *(unsigned __int64 *)(v_stack_pA0 + 64) = 0;
    result = (unsigned __int8)((*(unsigned __int8 *)(v_stack_p30 + 17)) + 1);
    *(unsigned __int8 *)(v_stack_p30 + 17) = (unsigned __int8)(result);
    if (1 == 0) goto loc_00395A52;
    goto loc_00395CEC;
loc_00395EEA:
    if (((unsigned int)(result)) != 5) goto loc_00396213;
    a1 = (unsigned __int8)((v_stack_pA0 + 216) & (254));
    a1 = (unsigned __int8)((a1) | (6));
    *(unsigned __int8 *)(v_stack_pA0 + 112) = (unsigned __int8)(a1);
loc_00395EFC:
    a3 = 0;
    goto loc_00395EC7;
loc_00395F01:
    result = KxWaitForLockOwnerShip(v_stack_p40, v_stack_pA0, a3, 1);
    goto loc_0039567C;
loc_00395F10:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(v_stack_pB8), (unsigned __int8)(v_stack_p30), a3, 1);
    goto loc_00395A0C;
loc_00395F22:
    if (((unsigned __int8)(result)) != 2) goto loc_0039612B;
    *(unsigned __int8 *)(v_stack_p30 + 17) = 5;
    result = KiInsertQueueInternal(*(unsigned __int64 *)(v_stack_p30 + 24), v_stack_p30, a3, 1);
    if (((unsigned __int8)(result)) == 2) goto loc_00395CF6;
    goto loc_00395A4F;
loc_00395F49:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(v_stack_pB8), (unsigned __int8)(v_stack_p30), a3, 1);
    goto loc_0039591F;
loc_00395F5B:
    *(unsigned int *)(v_stack_pA0 + 540) = (unsigned int)((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_pA0 + 540))));
    goto loc_00395E7E;
loc_00395F77:
    if (((unsigned __int8)((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_pA0 + 540))))) != 2) goto loc_0039614C;
    *(unsigned __int8 *)(v_stack_p30 + 17) = 5;
    result = KiInsertQueueInternal(*(unsigned __int64 *)(v_stack_p30 + 24), v_stack_p30, a3, 1);
    if (((unsigned __int8)((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_pA0 + 540))))) == 2) goto loc_00395DF6;
    goto loc_00395965;
loc_00395F9F:
    goto loc_003957AA;
loc_00395FA7:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12782347)))) & (64)) == 0) goto loc_00395ABC;
    result = KiCheckVpBackingLongSpinWaitHypercall(*(unsigned __int64 *)(v_stack_p30 + 24), v_stack_p30, a3, 1);
    if ((unsigned __int8)(result) == 0) goto loc_00395ABC;
    result = HvlNotifyLongSpinWait(1, v_stack_p30, a3, 1);
    goto loc_00395ABE;
loc_00395FCE:
    *(unsigned int *)(v_stack_pA0 + 540) = (unsigned int)((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_pA0 + 540))));
    goto loc_00395D84;
loc_00395FEA:
    result = KeReleaseInStackQueuedSpinLock(v_stack_p40, v_stack_p30, a3, 1);
    result = (unsigned __int8)(-((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 248) + 8)))));
    v_stack_p28 = 1;
    v_stack_p20 = 0;
    a4 = 0;
    result = AlpcpQueueIoCompletion(1, *(unsigned __int64 *)(1 + 40), a3, a4);
    if ((unsigned int)(result) == 0) goto loc_00396259;
    a2 = 0;
    result = 17;
    if (!(condition_is_equal)) {
        a1 = 1 + 352;
        result = ExfReleasePushLockShared(a1, a2, a3, a4);
    }
    result = KeAbPostRelease(1 + 352, a2, a3, a4);
    goto loc_003958B4;
loc_0039604D:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12782181)))) & (64)) == 0) goto loc_003959DB;
    result = KiCheckVpBackingLongSpinWaitHypercall(1 + 352, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_003959DB;
    result = HvlNotifyLongSpinWait(1, a2, a3, a4);
    goto loc_003959DD;
loc_00396074:
    if ((*(unsigned int *)(v_rip + 12782749)) != 0) {
        a1 = *(unsigned __int64 *)(v_stack_p40 + 1304 + 8);
        a2 = 1;
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, a3, a4);
    }
    result = RtlRaiseStatus((unsigned int)(0xC0000047ULL), a2, a3, a4);
loc_003960A5:
    result = KiCompleteDirectSwitchThread(v_stack_p30, *(unsigned __int64 *)(v_stack_p30 + 8), a3, a4);
    goto loc_00395893;
loc_003960C0:
    if ((*(unsigned int *)(v_rip + 12782673)) != 0) {
        a1 = 1;
        a2 = 1;
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, a3, a4);
    }
    goto loc_003958B4;
loc_003960EB:
    if (1 == 4) goto loc_00395AEA;
    if (1 != 0) goto loc_00396118;
    a1 = (unsigned __int8)((a1) & (250));
    a1 = (unsigned __int8)((a1) | (2));
    *(unsigned __int8 *)(v_stack_p30 + 112) = (unsigned __int8)(a1);
    *(unsigned __int64 *)(v_stack_p30 + 200) = 1;
    *(unsigned __int64 *)(v_stack_p30 + 976) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 248) + 8));
    *(unsigned __int8 *)(1 + 17) = (unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 248) + 8)));
    goto loc_00395B76;
loc_00396118:
    if (1 != 5) goto loc_0039616D;
    a1 = (unsigned __int8)((a1) & (254));
    a1 = (unsigned __int8)((a1) | (6));
    *(unsigned __int8 *)(v_stack_p30 + 112) = (unsigned __int8)(a1);
    goto loc_00395B79;
loc_0039612B:
    if (1 == 4) goto loc_003961F7;
    a4 = 0;
    result = KiTryUnwaitThread(v_stack_p30, v_stack_p30, 256, a4);
    goto loc_00395A4F;
loc_0039614C:
    if (((unsigned __int8)(result)) == 4) goto loc_00396228;
    a4 = 0;
    result = KiTryUnwaitThread(v_stack_p30, v_stack_p30, 256, a4);
    goto loc_00395965;
loc_0039616D:
    if (((unsigned int)(result)) != 3) goto loc_00395B79;
    *(unsigned __int8 *)(1 + 17) = 2;
    goto loc_00395B79;
loc_0039617F:
    if (((unsigned int)(result)) == 4) goto loc_00395E61;
    if ((unsigned int)(result) != 0) goto loc_00395EEA;
    a1 = (unsigned __int8)((v_stack_p30) & (250));
    a1 = (unsigned __int8)((a1) | (2));
    *(unsigned __int8 *)(v_stack_p30 + 112) = (unsigned __int8)(a1);
    a3 = 0;
    *(unsigned __int64 *)(v_stack_p30 + 200) = v_stack_p30;
    *(unsigned __int64 *)(v_stack_p30 + 976) = 0;
    *(unsigned __int8 *)(v_stack_p30 + 17) = 0;
    goto loc_00395EC7;
loc_003961BB:
    if (((unsigned int)(v_stack_p30)) == 4) goto loc_00395D67;
    if ((unsigned int)(v_stack_p30) != 0) goto loc_00395E29;
    a1 = (unsigned __int8)((a1) & (250));
    a1 = (unsigned __int8)((a1) | (2));
    *(unsigned __int8 *)(v_stack_p30 + 112) = (unsigned __int8)(a1);
    a3 = 0;
    *(unsigned __int64 *)(v_stack_p30 + 200) = v_stack_p30;
    *(unsigned __int64 *)(v_stack_p30 + 976) = 0;
    *(unsigned __int8 *)(v_stack_p30 + 17) = 0;
    goto loc_00395DCD;
loc_003961F7:
    *(unsigned __int8 *)(v_stack_p30 + 17) = 5;
    *(unsigned int *)((unsigned int)(v_stack_pA0) + 4) = 0;
    result = KeInsertQueueDpc(*(unsigned __int64 *)(v_stack_p30 + 24), (unsigned int)(v_stack_pA0), v_stack_p30, a4);
    goto loc_00395A4F;
loc_00396213:
    a3 = 0;
    if (((unsigned int)(result)) != 3) goto loc_00395EC7;
    *(unsigned __int8 *)(v_stack_p30 + 17) = 2;
    goto loc_00395EC7;
loc_00396228:
    *(unsigned __int8 *)(v_stack_p30 + 17) = 5;
    *(unsigned int *)(v_r15 + 4) = 0;
    result = KeInsertQueueDpc(*(unsigned __int64 *)(v_stack_p30 + 24), v_r15, v_stack_p30, a4);
    goto loc_00395965;
loc_00396244:
    a3 = 0;
    if (((unsigned int)(result)) != 3) goto loc_00395DCD;
    *(unsigned __int8 *)(v_stack_p30 + 17) = 2;
    goto loc_00395DCD;
loc_00396259:
    result = KeAcquireInStackQueuedSpinLock(v_stack_p30, v_stack_p40, a3, a4);
}
```

## 5. (Beta) C Style

```c
int64_t AlpcpSignal(void *Arg1, uint8_t Arg2, uint8_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint8_t v_stack_m78;
    uint64_t v_stack_p10;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p40;
    uint32_t v_stack_p8;
    uint64_t v_stack_pA0;
    uint64_t v_stack_pB8;

    v_stack_p10 = local_rbx;
    local_rsp = (local_rsp) - (96);
    if (*(uint64_t *)(arg1 + 0x20) == 0) goto loc_0039580A;
    if ((*(uint8_t *)(arg1 + 0x3A)) == 0) goto loc_003959E8;
    result = 0;
    v_stack_m58 = v_xmm0;
    v_stack_m50 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x30);
    v_stack_m58 = 0;
    v_stack_m48 = 0;
    if ((*(uint32_t *)(v_rip + 0xC316CD)) != 0) goto loc_00395C4E;
loc_00395659:
    v_stack_m48 = (uint8_t)(v_cr8);
    if (((*(uint8_t *)(v_rip + 0xC314A6)) & (33)) != 0) goto loc_003958CD;
loc_0039566B:
    if (v_stack_m58 != 0) goto loc_00395F01;
loc_0039567C:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x30) + 0xC)))) >= (*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x30) + 0x8))) goto loc_00395FEA;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x30) + 0x20) != 0) {
        result = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x30) + 0x20));
        *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x30) + 0x20) = result;
    }
    v_stack_p20 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x30) + 0x20) + 0x8);
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x30) + 0xC) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x30) + 0xC)) + 1);
    result = KeReleaseInStackQueuedSpinLock(v_stack_m58, (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x30) + 0xC)), Arg3, a4);
    Arg2 = 0;
    result = 17;
    if (!(condition_is_equal)) {
        Arg1 = *(uint64_t *)(arg1 + 0x20) + 352;
        result = ExfReleasePushLockShared(Arg1, Arg2, Arg3, a4);
    }
    result = KeAbPostRelease(*(uint64_t *)(arg1 + 0x20) + 352, Arg2, Arg3, a4);
    local_r14 = (uint8_t)(-(*(uint8_t *)(arg1 + 0x3B)));
    local_r14 = 0;
    result = (0 != 0) ? 1 : 0;
    local_rbp = (uint32_t)(((uint32_t)((uint32_t)(result))) | (4));
    if ((uint32_t)((uint32_t)(Arg3)) == 0) { local_rbp = (uint32_t)(result); }
    v_stack_p8 = (uint32_t)(local_rbp);
    if (v_stack_p20 == 0) goto loc_00395BB3;
loc_00395717:
    *(uint64_t *)(v_stack_p20 + 0x18) = *(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x28);
    *(uint64_t *)(v_stack_p20 + 0x20) = *(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x30);
    *(uint32_t *)(v_stack_p20 + 0x28) = 0;
    *(uint64_t *)(v_stack_p20 + 0x30) = 0;
    v_stack_m60 = 2;
    if ((*(uint32_t *)(v_rip + 0xC315DD)) != 0) goto loc_00395C60;
loc_00395749:
    v_stack_m68 = *(uint64_t *)(gs_base + (0 + 0x20));
    if ((*(uint32_t *)(v_rip + 0xC315DD)) < 0) goto loc_00395CA8;
loc_0039576B:
    result = (uint8_t)(~(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x20) + 0x1)));
    result = (uint32_t)((result) >> (1));
    result = (uint32_t)((result) & (1));
    v_stack_p20 = (uint32_t)(result);
    result = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0x650);
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0x650) == 0) { result = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8); }
    if ((uint32_t)(local_rbp) == 0) goto loc_003957A7;
    if (condition_is_below) goto loc_00395F9F;
loc_003957A7:
    local_rdi = 0;
loc_003957AA:
    result = KiAcquireKobjectLockSafe(*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x20), Arg2, Arg3, a4);
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x20) + 0x8)) == (*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x20) + 8)) goto loc_00395C11;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x20) + 0x28)))) >= (*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x20) + 0x2C))) goto loc_00395C08;
loc_003957C9:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0xE8)) == (*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x20))) goto loc_00395D34;
loc_003957D9:
loc_003957E0:
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x20) + 0x8) + 0x10)) != 3) goto loc_00395B9C;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x20) + 0x8)) + 0x8)) != (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x20) + 0x8))) goto loc_00395803;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x20) + 0x8) + 0x8))) == (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x20) + 0x8))) goto loc_00395BCD;
loc_00395803:
loc_0039580A:
    if (*(uint64_t *)(3 + 0x18) != 0) goto loc_003958ED;
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0x28))) & (1)) == 0) goto loc_003958B4;
    result = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x20) + 0x8) + 0x8);
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0x28)) >= 4) {
        Arg1 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0x28)) & (-4);
        Arg3 = (uint8_t)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x20) + 8);
        Arg2 = 0;
        result = KeSetEvent(Arg1, Arg2, Arg3, a4);
        Arg1 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0x28);
        result = AlpcpReleaseDirectAttribute(Arg1, Arg2, Arg3, a4);
    }
    Arg2 = 0;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0x28) = 0;
    goto loc_003958B4;
loc_0039584A:
    *(uint64_t *)(v_stack_p20) = result;
    *(uint64_t *)(v_stack_p20 + 0x8) = 0;
    *(uint64_t *)(Arg2) = v_stack_p20;
    *(uint64_t *)(result + 0x8) = v_stack_p20;
    if ((uint32_t)(Arg1) != 0) goto loc_0039586E;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x20) + 0x8)) != (*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x20) + 8)) {
        Arg2 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x20);
        Arg1 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x20) + 0x8));
        result = KiWakeOtherQueueWaiters(Arg1, Arg2, Arg3, a4);
    }
    if ((((uint8_t)(local_rbp)) & (1)) != 0) goto loc_00395D21;
    if ((((uint8_t)(local_rbp)) & (4)) != 0) goto loc_003960A5;
loc_0039588E:
loc_00395893:
    v_stack_m78 = (uint8_t)(v_stack_m60);
loc_003958AC:
    result = KiExitDispatcher(v_stack_m68, 0, 1, (uint32_t)(v_stack_p20));
loc_003958B4:
    local_rsp = (local_rsp) + (96);
    return result;
loc_003958CD:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB78585))) != 0) goto loc_0039566B;
    result = KiAcquireQueuedSpinLockInstrumented(v_stack_p40, v_stack_p10, 1, (uint32_t)(v_stack_p20));
    goto loc_0039567C;
loc_003958ED:
    if ((uint8_t)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x20) + 8) == 0) goto loc_00395CC4;
    v_stack_pB8 = 2;
    if ((*(uint32_t *)(v_rip + 0xC31407)) != 0) goto loc_00395F49;
loc_0039591F:
    v_stack_pA0 = *(uint64_t *)(gs_base + (0 + 0x20));
    result = KiAcquireKobjectLockSafe(v_stack_p40 + 1304, v_stack_p10, 1, (uint32_t)(v_stack_p20));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p40 + 0x518 + 0x4)) + 1)) < ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p40 + 0x518 + 0x4))))) goto loc_003960C0;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p40 + 0x518 + 0x4)) + 1)) > (*(uint32_t *)(v_stack_p40 + 0x518 + 0x18))) goto loc_003960C0;
    *(uint32_t *)(v_stack_p40 + 0x518 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p40 + 0x518 + 0x4)) + 1);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p40 + 0x518 + 0x4))) != 0) goto loc_00395DFE;
loc_00395965:
    Arg3 = 0;
loc_00395968:
    if ((*(uint64_t *)(v_stack_p40 + 0x518 + 0x8)) == (v_stack_p40 + 1304 + 8)) goto loc_00395DF6;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p40 + 0x518 + 0x8)) + 0x8)) != (*(uint64_t *)(v_stack_p40 + 0x518 + 0x8))) goto loc_00395803;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p40 + 0x518 + 0x8) + 0x8))) != (*(uint64_t *)(v_stack_p40 + 0x518 + 0x8))) goto loc_00395803;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p40 + 0x518 + 0x8) + 0x8)) = *(uint64_t *)(*(uint64_t *)(v_stack_p40 + 0x518 + 0x8));
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p40 + 0x518 + 0x8)) + 0x8) = *(uint64_t *)(*(uint64_t *)(v_stack_p40 + 0x518 + 0x8) + 0x8);
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(v_stack_p40 + 0x518 + 0x8) + 0x10))) != 1) goto loc_00395F77;
    local_r12 = 0;
    v_stack_p30 = *(uint16_t *)(*(uint64_t *)(v_stack_p40 + 0x518 + 0x8) + 0x12);
loc_003959C0:
    if (condition_is_above_or_equal) goto loc_00395D46;
loc_003959CD:
    local_rdi = (uint32_t)((0) + 1);
    if (((*(uint32_t *)(v_rip + 0xC2F8D7)) & ((uint32_t)(local_rdi))) == 0) goto loc_0039604D;
loc_003959DB:
loc_003959DD:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p40 + 0x518 + 0x8) + 0x18) + 0x40) == 0) goto loc_003959C0;
    goto loc_003959CD;
loc_003959E8:
    v_stack_pB8 = 2;
    if ((*(uint32_t *)(v_rip + 0xC3131A)) != 0) goto loc_00395F10;
loc_00395A0C:
    v_stack_pA0 = *(uint64_t *)(gs_base + (0 + 0x20));
    result = KiAcquireKobjectLockSafe(*(uint64_t *)(local_rdi + 0xF8), *(uint16_t *)(*(uint64_t *)(v_stack_p40 + 0x518 + 0x8) + 0x12), Arg3, (uint32_t)(v_stack_p20));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rdi + 0xF8) + 0x4)) + 1)) < ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rdi + 0xF8) + 0x4))))) goto loc_00396074;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rdi + 0xF8) + 0x4)) + 1)) > (*(uint32_t *)(*(uint64_t *)(local_rdi + 0xF8) + 0x18))) goto loc_00396074;
    *(uint32_t *)(*(uint64_t *)(local_rdi + 0xF8) + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rdi + 0xF8) + 0x4)) + 1);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rdi + 0xF8) + 0x4))) != 0) goto loc_00395CFE;
loc_00395A4F:
    Arg3 = 0;
loc_00395A52:
    if ((*(uint64_t *)(*(uint64_t *)(local_rdi + 0xF8) + 0x8)) == (*(uint64_t *)(local_rdi + 0xF8) + 8)) goto loc_00395CF6;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rdi + 0xF8) + 0x8)) + 0x8)) != (*(uint64_t *)(*(uint64_t *)(local_rdi + 0xF8) + 0x8))) goto loc_00395803;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rdi + 0xF8) + 0x8) + 0x8))) != (*(uint64_t *)(*(uint64_t *)(local_rdi + 0xF8) + 0x8))) goto loc_00395803;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rdi + 0xF8) + 0x8) + 0x8)) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rdi + 0xF8) + 0x8));
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rdi + 0xF8) + 0x8)) + 0x8) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rdi + 0xF8) + 0x8) + 0x8);
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(local_rdi + 0xF8) + 0x8) + 0x10))) != 1) goto loc_00395F22;
    local_r13 = 0;
    v_stack_p30 = *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(local_rdi + 0xF8) + 0x8) + 0x12);
loc_00395AA1:
    if (condition_is_above_or_equal) goto loc_00395E40;
loc_00395AAE:
    local_rdi = (uint32_t)((0) + 1);
    if (((*(uint32_t *)(v_rip + 0xC2F7F6)) & ((uint32_t)(local_rdi))) == 0) goto loc_00395FA7;
loc_00395ABC:
loc_00395ABE:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rdi + 0xF8) + 0x8) + 0x18) + 0x40) == 0) goto loc_00395AA1;
    goto loc_00395AAE;
loc_00395AC9:
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rdi + 0xF8) + 0x8) + 0x18) + 0x184))) != 5) goto loc_00395B79;
    result = (uint32_t)(((uint32_t)((uint32_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rdi + 0xF8) + 0x8) + 0x18) + 0x70)))) & (7));
    if (((uint32_t)(result)) != 1) goto loc_003960EB;
loc_00395AEA:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rdi + 0xF8) + 0x8) + 0x18) + 0xE8) == 0) goto loc_00395B07;
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rdi + 0xF8) + 0x8) + 0x18) + 0xE8))) & (127));
    if (((uint8_t)(result)) == 21) goto loc_00395C32;
loc_00395B07:
    result = KiRemovePrcbWaitEntry(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rdi + 0xF8) + 0x8) + 0x18), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rdi + 0xF8) + 0x8) + 0x18) + 0xE8), Arg3, (uint32_t)(v_stack_p20));
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rdi + 0xF8) + 0x8) + 0x18) + 0x184))) == 1) goto loc_00395D2B;
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rdi + 0xF8) + 0x8) + 0x18) + 0x184))) != 5) goto loc_00395B44;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rdi + 0xF8) + 0x8) + 0x18) + 0x184)))) - (*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rdi + 0xF8) + 0x8) + 0x18) + 0x1B4)));
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rdi + 0xF8) + 0x8) + 0x18) + 0x187)) == ((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rdi + 0xF8) + 0x8))))) goto loc_00395BAA;
loc_00395B44:
    *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rdi + 0xF8) + 0x8) + 0x18) + 0x184) = 7;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rdi + 0xF8) + 0x8) + 0x18) + 0xD8) = *(uint64_t *)(v_stack_p30 + 0x2D08);
    *(uint64_t *)(v_stack_p30 + 0x2D08) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rdi + 0xF8) + 0x8) + 0x18) + 216;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rdi + 0xF8) + 0x8) + 0x18) + 0xC8) = *(uint64_t *)(local_rdi + 0xF8) + 8;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rdi + 0xF8) + 0x8) + 0x18) + 0x3D0) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rdi + 0xF8) + 0x8));
loc_00395B76:
loc_00395B79:
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rdi + 0xF8) + 0x8) + 0x18) + 0x40) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rdi + 0xF8) + 0x8));
    result = (uint8_t)((*(uint8_t *)(local_rdi + 0x11)) + 1);
    *(uint8_t *)(local_rdi + 0x11) = (uint8_t)(result);
    if (1 != 0) goto loc_00395C71;
    if ((*(uint64_t *)(*(uint64_t *)(local_rdi + 0xF8) + 0x8)) != (local_r13 + 8)) goto loc_003957E0;
loc_00395B9C:
    goto loc_00395C11;
loc_00395BAA:
    goto loc_00395B44;
loc_00395BB3:
    Arg2 = 0;
    result = IopAllocateMiniCompletionPacket(1, Arg2, Arg3, (uint32_t)(v_stack_p20));
    if (result != 0) goto loc_00395717;
    goto loc_003958B4;
loc_00395BCD:
    *(uint64_t *)(result) = v_stack_p30;
    local_r15 = 0;
    *(uint64_t *)(v_stack_p30 + 0x8) = result;
loc_00395BE0:
    if (condition_is_above_or_equal) goto loc_00395AC9;
loc_00395BED:
    local_rbp = (uint32_t)(((uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rdi + 0xF8) + 0x8))))) + 1);
    if (((*(uint32_t *)(v_rip + 0xC2F6B7)) & ((uint32_t)(local_rbp))) == 0) goto loc_00395C81;
loc_00395BFB:
loc_00395BFD:
    if (*(uint64_t *)(*(uint64_t *)(local_rdi + 0x18) + 0x40) == 0) goto loc_00395BE0;
    goto loc_00395BED;
loc_00395C08:
    if ((uint8_t)(local_rdi) != 0) goto loc_003957C9;
loc_00395C11:
    *(uint32_t *)(local_r13 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(local_r13 + 0x4)) + 1);
    if ((*(uint64_t *)(*(uint64_t *)(local_r13 + 0x18 + 0x8))) != (local_r13 + 24)) goto loc_00395803;
    goto loc_0039584A;
loc_00395C32:
    *(uint32_t *)(*(uint64_t *)(local_rdi + 0x18) + 0x21C) = (uint32_t)((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rdi + 0x18) + 0x21C))));
    goto loc_00395B07;
loc_00395C4E:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(local_rbp), (uint8_t)(v_stack_p30), Arg3, (uint32_t)(v_stack_p20));
    goto loc_00395659;
loc_00395C60:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(result), (uint8_t)(v_stack_p30), Arg3, (uint32_t)(v_stack_p20));
    goto loc_00395749;
loc_00395C71:
    *(uint64_t *)(result) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rdi + 0xF8) + 0x8));
    goto loc_0039586E;
loc_00395C81:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC30E31)))) & (64)) == 0) goto loc_00395BFB;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint8_t)(result), (uint8_t)(v_stack_p30), Arg3, (uint32_t)(v_stack_p20));
    if ((uint8_t)(result) == 0) goto loc_00395BFB;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)((uint32_t)(v_stack_pA0))), (uint8_t)(v_stack_p30), Arg3, (uint32_t)(v_stack_p20));
    goto loc_00395BFD;
loc_00395CA8:
    result = KeIsThreadRunning(*(uint64_t *)(local_rdi + 0x18), (uint8_t)(v_stack_p30), Arg3, (uint32_t)(v_stack_p20));
    result = EtwTraceEnqueueWork(*(uint64_t *)(local_rdi + 0x18), result, (uint8_t)(result), (uint32_t)(v_stack_p20));
    goto loc_0039576B;
loc_00395CC4:
    Arg2 = 0;
    Arg1 = (*(uint64_t *)(local_rdi + 0x18)) + (0x518ULL);
    v_stack_p28 = 0;
    v_stack_p20 = 2;
    result = KeReleaseSemaphoreEx(Arg1, 1, 1, (uint32_t)(v_stack_p20));
    goto loc_003958B4;
loc_00395CEC:
    if (condition_is_not_equal) goto loc_00395A52;
loc_00395CF6:
loc_00395CFE:
    local_r15 = (uint8_t)(-(local_r15));
    v_stack_p20 = (uint8_t)(v_stack_pB8);
    Arg2 = (uint32_t)((1) & (3));
    goto loc_003958AC;
loc_00395D21:
    goto loc_0039588E;
loc_00395D2B:
    goto loc_00395B44;
loc_00395D34:
    if ((*(uint8_t *)(*(uint64_t *)(local_rdi + 0x18) + 0x283)) != 15) goto loc_003957D9;
    goto loc_00395C11;
loc_00395D46:
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(local_rdi + 0x18) + 0x184))) != 5) goto loc_00395E3B;
    result = (uint32_t)(((uint32_t)((uint32_t)(*(uint8_t *)(*(uint64_t *)(local_rdi + 0x18) + 0x70)))) & (7));
    if (((uint32_t)(result)) != 1) goto loc_003961BB;
loc_00395D67:
    if (*(uint64_t *)(*(uint64_t *)(local_rdi + 0x18) + 0xE8) == 0) goto loc_00395D84;
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(local_rdi + 0x18) + 0xE8))) & (127));
    if (((uint8_t)(result)) == 21) goto loc_00395FCE;
loc_00395D84:
    result = KiRemovePrcbWaitEntry(*(uint64_t *)(local_rdi + 0x18), *(uint64_t *)(*(uint64_t *)(local_rdi + 0x18) + 0xE8), 1, 1);
    result = KiEnterDeferredReadyState(*(uint64_t *)(local_rdi + 0x18), *(uint64_t *)(*(uint64_t *)(local_rdi + 0x18) + 0xE8), 1, 1);
    Arg3 = 0;
    *(uint64_t *)(*(uint64_t *)(local_rdi + 0x18) + 0xD8) = *(uint64_t *)(v_stack_pA0 + 0x2D08);
    *(uint64_t *)(v_stack_pA0 + 0x2D08) = *(uint64_t *)(local_rdi + 0x18) + 216;
    *(uint64_t *)(*(uint64_t *)(local_rdi + 0x18) + 0xC8) = v_stack_p30;
    *(uint64_t *)(*(uint64_t *)(local_rdi + 0x18) + 0x3D0) = 0;
loc_00395DCD:
    *(uint64_t *)(*(uint64_t *)(local_rdi + 0x18) + 0x40) = 0;
    result = (uint8_t)((*(uint8_t *)(v_stack_p30 + 0x11)) + 1);
    *(uint8_t *)(v_stack_p30 + 0x11) = (uint8_t)(result);
    if (1 == 0) goto loc_00395968;
    if (1 != 0) goto loc_00395968;
loc_00395DF6:
loc_00395DFE:
    v_stack_p20 = (uint8_t)(v_stack_pB8);
    Arg2 = 1;
    if ((uint8_t)((uint32_t)(v_stack_pA0)) != 0) { Arg2 = 3; }
    goto loc_003958AC;
loc_00395E29:
    if (((uint32_t)(result)) != 5) goto loc_00396244;
    Arg1 = (uint8_t)((3) & (254));
    Arg1 = (uint8_t)((Arg1) | (6));
    *(uint8_t *)(v_stack_pA0 + 0x70) = (uint8_t)(Arg1);
loc_00395E3B:
    Arg3 = 0;
    goto loc_00395DCD;
loc_00395E40:
    if (((uint8_t)(*(uint8_t *)(v_stack_pA0 + 0x184))) != 5) goto loc_00395EFC;
    result = (uint32_t)(((uint32_t)((uint32_t)(*(uint8_t *)(v_stack_pA0 + 0x70)))) & (7));
    if (((uint32_t)(result)) != 1) goto loc_0039617F;
loc_00395E61:
    if (*(uint64_t *)(v_stack_pA0 + 0xE8) == 0) goto loc_00395E7E;
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(v_stack_pA0 + 0xE8))) & (127));
    if (((uint8_t)(result)) == 21) goto loc_00395F5B;
loc_00395E7E:
    result = KiRemovePrcbWaitEntry(v_stack_pA0, *(uint64_t *)(v_stack_pA0 + 0xE8), Arg3, 1);
    result = KiEnterDeferredReadyState(v_stack_pA0, *(uint64_t *)(v_stack_pA0 + 0xE8), Arg3, 1);
    Arg3 = 0;
    *(uint64_t *)(v_stack_pA0 + 0xD8) = *(uint64_t *)(v_stack_pA0 + 0x2D08);
    *(uint64_t *)(v_stack_pA0 + 0x2D08) = v_stack_pA0 + 216;
    *(uint64_t *)(v_stack_pA0 + 0xC8) = v_stack_p30;
    *(uint64_t *)(v_stack_pA0 + 0x3D0) = 0;
loc_00395EC7:
    *(uint64_t *)(v_stack_pA0 + 0x40) = 0;
    result = (uint8_t)((*(uint8_t *)(v_stack_p30 + 0x11)) + 1);
    *(uint8_t *)(v_stack_p30 + 0x11) = (uint8_t)(result);
    if (1 == 0) goto loc_00395A52;
    goto loc_00395CEC;
loc_00395EEA:
    if (((uint32_t)(result)) != 5) goto loc_00396213;
    Arg1 = (uint8_t)((v_stack_pA0 + 216) & (254));
    Arg1 = (uint8_t)((Arg1) | (6));
    *(uint8_t *)(v_stack_pA0 + 0x70) = (uint8_t)(Arg1);
loc_00395EFC:
    Arg3 = 0;
    goto loc_00395EC7;
loc_00395F01:
    result = KxWaitForLockOwnerShip(v_stack_p40, v_stack_pA0, Arg3, 1);
    goto loc_0039567C;
loc_00395F10:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(v_stack_pB8), (uint8_t)(v_stack_p30), Arg3, 1);
    goto loc_00395A0C;
loc_00395F22:
    if (((uint8_t)(result)) != 2) goto loc_0039612B;
    *(uint8_t *)(v_stack_p30 + 0x11) = 5;
    result = KiInsertQueueInternal(*(uint64_t *)(v_stack_p30 + 0x18), v_stack_p30, Arg3, 1);
    if (((uint8_t)(result)) == 2) goto loc_00395CF6;
    goto loc_00395A4F;
loc_00395F49:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(v_stack_pB8), (uint8_t)(v_stack_p30), Arg3, 1);
    goto loc_0039591F;
loc_00395F5B:
    *(uint32_t *)(v_stack_pA0 + 0x21C) = (uint32_t)((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_pA0 + 0x21C))));
    goto loc_00395E7E;
loc_00395F77:
    if (((uint8_t)((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_pA0 + 0x21C))))) != 2) goto loc_0039614C;
    *(uint8_t *)(v_stack_p30 + 0x11) = 5;
    result = KiInsertQueueInternal(*(uint64_t *)(v_stack_p30 + 0x18), v_stack_p30, Arg3, 1);
    if (((uint8_t)((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_pA0 + 0x21C))))) == 2) goto loc_00395DF6;
    goto loc_00395965;
loc_00395F9F:
    goto loc_003957AA;
loc_00395FA7:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC30B0B)))) & (64)) == 0) goto loc_00395ABC;
    result = KiCheckVpBackingLongSpinWaitHypercall(*(uint64_t *)(v_stack_p30 + 0x18), v_stack_p30, Arg3, 1);
    if ((uint8_t)(result) == 0) goto loc_00395ABC;
    result = HvlNotifyLongSpinWait(1, v_stack_p30, Arg3, 1);
    goto loc_00395ABE;
loc_00395FCE:
    *(uint32_t *)(v_stack_pA0 + 0x21C) = (uint32_t)((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_pA0 + 0x21C))));
    goto loc_00395D84;
loc_00395FEA:
    result = KeReleaseInStackQueuedSpinLock(v_stack_p40, v_stack_p30, Arg3, 1);
    result = (uint8_t)(-((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rdi + 0xF8) + 0x8)))));
    v_stack_p28 = 1;
    v_stack_p20 = 0;
    a4 = 0;
    result = AlpcpQueueIoCompletion(1, *(uint64_t *)(1 + 0x28), Arg3, a4);
    if ((uint32_t)(result) == 0) goto loc_00396259;
    Arg2 = 0;
    result = 17;
    if (!(condition_is_equal)) {
        Arg1 = 1 + 352;
        result = ExfReleasePushLockShared(Arg1, Arg2, Arg3, a4);
    }
    result = KeAbPostRelease(1 + 352, Arg2, Arg3, a4);
    goto loc_003958B4;
loc_0039604D:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC30A65)))) & (64)) == 0) goto loc_003959DB;
    result = KiCheckVpBackingLongSpinWaitHypercall(1 + 352, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_003959DB;
    result = HvlNotifyLongSpinWait(1, Arg2, Arg3, a4);
    goto loc_003959DD;
loc_00396074:
    if ((*(uint32_t *)(v_rip + 0xC30C9D)) != 0) {
        Arg1 = *(uint64_t *)(v_stack_p40 + 0x518 + 0x8);
        Arg2 = 1;
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, Arg3, a4);
    }
    result = RtlRaiseStatus((uint32_t)(0xC0000047ULL), Arg2, Arg3, a4);
loc_003960A5:
    result = KiCompleteDirectSwitchThread(v_stack_p30, *(uint64_t *)(v_stack_p30 + 0x8), Arg3, a4);
    goto loc_00395893;
loc_003960C0:
    if ((*(uint32_t *)(v_rip + 0xC30C51)) != 0) {
        Arg1 = 1;
        Arg2 = 1;
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, Arg3, a4);
    }
    goto loc_003958B4;
loc_003960EB:
    if (1 == 4) goto loc_00395AEA;
    if (1 != 0) goto loc_00396118;
    Arg1 = (uint8_t)((Arg1) & (250));
    Arg1 = (uint8_t)((Arg1) | (2));
    *(uint8_t *)(v_stack_p30 + 0x70) = (uint8_t)(Arg1);
    *(uint64_t *)(v_stack_p30 + 0xC8) = 1;
    *(uint64_t *)(v_stack_p30 + 0x3D0) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rdi + 0xF8) + 0x8));
    *(uint8_t *)(1 + 0x11) = (uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rdi + 0xF8) + 0x8)));
    goto loc_00395B76;
loc_00396118:
    if (1 != 5) goto loc_0039616D;
    Arg1 = (uint8_t)((Arg1) & (254));
    Arg1 = (uint8_t)((Arg1) | (6));
    *(uint8_t *)(v_stack_p30 + 0x70) = (uint8_t)(Arg1);
    goto loc_00395B79;
loc_0039612B:
    if (1 == 4) goto loc_003961F7;
    a4 = 0;
    result = KiTryUnwaitThread(v_stack_p30, v_stack_p30, 256, a4);
    goto loc_00395A4F;
loc_0039614C:
    if (((uint8_t)(result)) == 4) goto loc_00396228;
    a4 = 0;
    result = KiTryUnwaitThread(v_stack_p30, v_stack_p30, 256, a4);
    goto loc_00395965;
loc_0039616D:
    if (((uint32_t)(result)) != 3) goto loc_00395B79;
    *(uint8_t *)(1 + 0x11) = 2;
    goto loc_00395B79;
loc_0039617F:
    if (((uint32_t)(result)) == 4) goto loc_00395E61;
    if ((uint32_t)(result) != 0) goto loc_00395EEA;
    Arg1 = (uint8_t)((v_stack_p30) & (250));
    Arg1 = (uint8_t)((Arg1) | (2));
    *(uint8_t *)(v_stack_p30 + 0x70) = (uint8_t)(Arg1);
    Arg3 = 0;
    *(uint64_t *)(v_stack_p30 + 0xC8) = v_stack_p30;
    *(uint64_t *)(v_stack_p30 + 0x3D0) = 0;
    *(uint8_t *)(v_stack_p30 + 0x11) = 0;
    goto loc_00395EC7;
loc_003961BB:
    if (((uint32_t)(v_stack_p30)) == 4) goto loc_00395D67;
    if ((uint32_t)(v_stack_p30) != 0) goto loc_00395E29;
    Arg1 = (uint8_t)((Arg1) & (250));
    Arg1 = (uint8_t)((Arg1) | (2));
    *(uint8_t *)(v_stack_p30 + 0x70) = (uint8_t)(Arg1);
    Arg3 = 0;
    *(uint64_t *)(v_stack_p30 + 0xC8) = v_stack_p30;
    *(uint64_t *)(v_stack_p30 + 0x3D0) = 0;
    *(uint8_t *)(v_stack_p30 + 0x11) = 0;
    goto loc_00395DCD;
loc_003961F7:
    *(uint8_t *)(v_stack_p30 + 0x11) = 5;
    *(uint32_t *)((uint32_t)(v_stack_pA0) + 0x4) = 0;
    result = KeInsertQueueDpc(*(uint64_t *)(v_stack_p30 + 0x18), (uint32_t)(v_stack_pA0), v_stack_p30, a4);
    goto loc_00395A4F;
loc_00396213:
    Arg3 = 0;
    if (((uint32_t)(result)) != 3) goto loc_00395EC7;
    *(uint8_t *)(v_stack_p30 + 0x11) = 2;
    goto loc_00395EC7;
loc_00396228:
    *(uint8_t *)(v_stack_p30 + 0x11) = 5;
    *(uint32_t *)(local_r15 + 0x4) = 0;
    result = KeInsertQueueDpc(*(uint64_t *)(v_stack_p30 + 0x18), local_r15, v_stack_p30, a4);
    goto loc_00395965;
loc_00396244:
    Arg3 = 0;
    if (((uint32_t)(result)) != 3) goto loc_00395DCD;
    *(uint8_t *)(v_stack_p30 + 0x11) = 2;
    goto loc_00395DCD;
loc_00396259:
    result = KeAcquireInStackQueuedSpinLock(v_stack_p30, v_stack_p40, Arg3, a4);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x3A` | `8` | `R` |
| `Arg1` | `+ 0x3B` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003955E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
