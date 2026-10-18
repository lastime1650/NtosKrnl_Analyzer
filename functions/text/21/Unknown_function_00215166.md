# sub_00215166

- RVA: `0x00215166`–`0x00215B2E` (길이 `2,504` bytes)
- VA: `0x0000000140215166`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005E1BC`
- 디코드: `628`개 명령, `2,504/2,504` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **36**; 고유 호출 대상: **25**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x002151E0` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x0021522E` → [EtwpGetTrackingLockSlotForThread](EtwpGetTrackingLockSlotForThread_function_00215B34.md) (function, `0x00215B34`)
- `0x002152BC` → [KxWaitForLockChainValid](KxWaitForLockChainValid_function_00217AA0.md) (function, `0x00217AA0`)
- `0x002152D9` → [KeWakeAddressAll](KeWakeAddressAll_function_00217C20.md) (function, `0x00217C20`)
- `0x002152F2` → [KiReleaseQueuedSpinLockInstrumented](KiReleaseQueuedSpinLockInstrumented_function_002179F0.md) (function, `0x002179F0`)
- `0x0021530C` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x00215371` → [EtwpGetTrackingLockSlotForThread](EtwpGetTrackingLockSlotForThread_function_00215B34.md) (function, `0x00215B34`)
- `0x00215412` → [ExpApplyPriorityBoost](ExpApplyPriorityBoost_function_00213F10.md) (function, `0x00213F10`)
- `0x00215424` → [ExpWaitForResource](ExpWaitForResource_function_002166F0.md) (function, `0x002166F0`)
- `0x00215559` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x00215573` → [IoBoostThreadIoPriority](IoBoostThreadIoPriority_function_00216110.md) (function, `0x00216110`)
- `0x00215581` → [PsBoostThreadOutstandingIoQoS](PsBoostThreadOutstandingIoQoS_function_00215C54.md) (function, `0x00215C54`)
- `0x002155EA` → [EtwpGetTrackingLockSlotForThread](EtwpGetTrackingLockSlotForThread_function_00215B34.md) (function, `0x00215B34`)
- `0x00215640` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x0021566A` → [KiAcquireQueuedSpinLockInstrumented](../27/KiAcquireQueuedSpinLockInstrumented_function_00275850.md) (function, `0x00275850`)
- `0x002156CC` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x00215720` → [KxWaitForLockOwnerShip](../25/KxWaitForLockOwnerShip_function_00257EB0.md) (function, `0x00257EB0`)
- `0x00215748` → [PsBoostThreadIoEx](../39/PsBoostThreadIoEx_function_00392C00.md) (function, `0x00392C00`)
- `0x002157B2` → [KiAbThreadInsertList](KiAbThreadInsertList_function_0021F0E0.md) (function, `0x0021F0E0`)
- `0x002157BF` → [KiAbQueueAutoBoostDpc](../20/KiAbQueueAutoBoostDpc_function_002074D0.md) (function, `0x002074D0`)
- `0x002157D5` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x002157ED` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x00215841` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00215871` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x002158A3` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x002158CC` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x002158E1` → [KeAbPreAcquire](KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x002159CE` → [ExpAcquireFastResourceExclusiveSlow](../3B/ExpAcquireFastResourceExclusiveSlow_function_003BE2E0.md) (function, `0x003BE2E0`)
- `0x002159EF` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x00215A06` → [KeAbPostReleaseEx](../26/KeAbPostReleaseEx_function_00262210.md) (function, `0x00262210`)
- `0x00215A21` → [ObfReferenceObjectWithTag](ObfReferenceObjectWithTag_function_00210710.md) (function, `0x00210710`)
- `0x00215A37` → [KeAbPostReleaseEx](../26/KeAbPostReleaseEx_function_00262210.md) (function, `0x00262210`)
- `0x00215A48` → [KeAbMarkCrossThreadReleasable](../3B/KeAbMarkCrossThreadReleasable_function_003BE8AC.md) (function, `0x003BE8AC`)
- `0x00215A82` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00215AE0` → [KeAcquireSpinLockAtDpcLevel](../20/KeAcquireSpinLockAtDpcLevel_function_00208430.md) (function, `0x00208430`)
- `0x00215B0F` → [KxReleaseSpinLock](../20/KxReleaseSpinLock_function_00206670.md) (function, `0x00206670`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0021528C` → RVA `0x00FC6B06` (`ALMOSTRO`; read)
- `0x002152E0` → RVA `0x00F0DE58` (`.data`; read)
- `0x002152F7` → RVA `0x00FC6D20` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **7**
  - `0x0021526F` → [sub_00214E58 + 0x251](Unknown_function_00214E58.md) (`tail-transfer`)
  - `0x00215637` → [sub_00214E58 + 0x251](Unknown_function_00214E58.md) (`tail-transfer`)
  - `0x00215650` → [sub_00214E58 + 0x251](Unknown_function_00214E58.md) (`tail-transfer`)
  - `0x002159A5` → [sub_00214E58 + 0x255](Unknown_function_00214E58.md) (`tail-transfer`)
  - `0x00215A0F` → [sub_00214E58 + 0x255](Unknown_function_00214E58.md) (`tail-transfer`)
  - `0x00215A2A` → [sub_00214E58 + 0x255](Unknown_function_00214E58.md) (`tail-transfer`)
  - `0x00215A3E` → [sub_00214E58 + 0x255](Unknown_function_00214E58.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00215166  0F B6 43 1A                     movzx eax, byte ptr [rbx + 0x1a]
0021516A  84 C0                           test al, al
0021516C  79 06                           jns 0x140215174
0021516E  4C 39 6B 30                     cmp qword ptr [rbx + 0x30], r13
00215172  74 55                           je 0x1402151c9
00215174  45 84 E4                        test r12b, r12b
00215177  0F 84 BF 04 00 00               je 0x14021563c
0021517D  FF 43 4C                        inc dword ptr [rbx + 0x4c]
00215180  48 8D 45 D7                     lea rax, [rbp - 0x29]
00215184  48 89 45 DF                     mov qword ptr [rbp - 0x21], rax
00215188  48 8D 45 D7                     lea rax, [rbp - 0x29]
0021518C  48 89 45 D7                     mov qword ptr [rbp - 0x29], rax
00215190  48 8B 43 28                     mov rax, qword ptr [rbx + 0x28]
00215194  4C 89 7D B7                     mov qword ptr [rbp - 0x49], r15
00215198  4C 89 7D BF                     mov qword ptr [rbp - 0x41], r15
0021519C  48 C7 45 CF 01 00 06 00         mov qword ptr [rbp - 0x31], 0x60001
002151A4  4C 89 6D C7                     mov qword ptr [rbp - 0x39], r13
002151A8  4C 89 7D E7                     mov qword ptr [rbp - 0x19], r15
002151AC  48 85 C0                        test rax, rax
002151AF  0F 84 BF 00 00 00               je 0x140215274
002151B5  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
002151B9  48 39 01                        cmp qword ptr [rcx], rax
002151BC  0F 84 93 05 00 00               je 0x140215755
002151C2  B9 03 00 00 00                  mov ecx, 3
002151C7  CD 29                           int 0x29
002151C9  8B 7B 38                        mov edi, dword ptr [rbx + 0x38]
002151CC  48 8D 4D 9F                     lea rcx, [rbp - 0x61]
002151D0  8D 47 08                        lea eax, [rdi + 8]
002151D3  33 F8                           xor edi, eax
002151D5  83 E7 07                        and edi, 7
002151D8  33 F8                           xor edi, eax
002151DA  89 7B 38                        mov dword ptr [rbx + 0x38], edi
002151DD  C1 EF 03                        shr edi, 3
002151E0  E8 FB DA 12 00                  call 0x140342ce0
002151E5  65 FF 04 25 80 90 00 00         inc dword ptr gs:[0x9080]
002151ED  65 FF 04 25 64 90 00 00         inc dword ptr gs:[0x9064]
002151F5  45 85 F6                        test r14d, r14d
002151F8  74 72                           je 0x14021526c
002151FA  65 48 8B 34 25 20 00 00 00      mov rsi, qword ptr gs:[0x20]
00215203  BA 00 00 01 00                  mov edx, 0x10000
00215208  44 8B 73 44                     mov r14d, dword ptr [rbx + 0x44]
0021520C  48 8B CB                        mov rcx, rbx
0021520F  44 88 7D 8A                     mov byte ptr [rbp - 0x76], r15b
00215213  0F B6 86 D0 00 00 00            movzx eax, byte ptr [rsi + 0xd0]
0021521A  FF 86 70 8F 00 00               inc dword ptr [rsi + 0x8f70]
00215220  66 89 45 87                     mov word ptr [rbp - 0x79], ax
00215224  0F B6 86 D1 00 00 00            movzx eax, byte ptr [rsi + 0xd1]
0021522B  88 45 89                        mov byte ptr [rbp - 0x77], al
0021522E  E8 01 09 00 00                  call 0x140215b34
00215233  48 8B C8                        mov rcx, rax
00215236  48 85 C0                        test rax, rax
00215239  74 31                           je 0x14021526c
0021523B  FF 86 74 8F 00 00               inc dword ptr [rsi + 0x8f74]
00215241  BE 01 00 00 00                  mov esi, 1
00215246  44 39 78 20                     cmp dword ptr [rax + 0x20], r15d
0021524A  0F 85 CD 08 00 00               jne 0x140215b1d
00215250  B8 02 00 00 00                  mov eax, 2
00215255  48 89 31                        mov qword ptr [rcx], rsi
00215258  48 89 41 08                     mov qword ptr [rcx + 8], rax
0021525C  8B 45 87                        mov eax, dword ptr [rbp - 0x79]
0021525F  89 41 18                        mov dword ptr [rcx + 0x18], eax
00215262  89 79 24                        mov dword ptr [rcx + 0x24], edi
00215265  44 89 71 2C                     mov dword ptr [rcx + 0x2c], r14d
00215269  89 71 20                        mov dword ptr [rcx + 0x20], esi
0021526C  41 B4 01                        mov r12b, 1
0021526F  E9 35 FE FF FF                  jmp 0x1402150a9
00215274  48 8D 45 B7                     lea rax, [rbp - 0x49]
00215278  48 89 45 BF                     mov qword ptr [rbp - 0x41], rax
0021527C  48 8D 45 B7                     lea rax, [rbp - 0x49]
00215280  48 89 45 B7                     mov qword ptr [rbp - 0x49], rax
00215284  48 8D 45 B7                     lea rax, [rbp - 0x49]
00215288  48 89 43 28                     mov qword ptr [rbx + 0x28], rax
0021528C  F6 05 73 18 DB 00 01            test byte ptr [rip + 0xdb1873], 1
00215293  75 4B                           jne 0x1402152e0
00215295  0F 0D 4D 9F                     prefetchw byte ptr [rbp - 0x61]
00215299  48 8B 45 9F                     mov rax, qword ptr [rbp - 0x61]
0021529D  48 85 C0                        test rax, rax
002152A0  75 1F                           jne 0x1402152c1
002152A2  48 8B 4D A7                     mov rcx, qword ptr [rbp - 0x59]
002152A6  48 8D 45 9F                     lea rax, [rbp - 0x61]
002152AA  F0 4C 0F B1 39                  lock cmpxchg qword ptr [rcx], r15
002152AF  48 8D 4D 9F                     lea rcx, [rbp - 0x61]
002152B3  48 3B C1                        cmp rax, rcx
002152B6  74 3F                           je 0x1402152f7
002152B8  48 8D 4D 9F                     lea rcx, [rbp - 0x61]
002152BC  E8 DF 27 00 00                  call 0x140217aa0
002152C1  48 8D 48 08                     lea rcx, [rax + 8]
002152C5  4C 89 7D 9F                     mov qword ptr [rbp - 0x61], r15
002152C9  48 8B 55 A7                     mov rdx, qword ptr [rbp - 0x59]
002152CD  48 8B C2                        mov rax, rdx
002152D0  48 87 01                        xchg qword ptr [rcx], rax
002152D3  32 C2                           xor al, dl
002152D5  A8 04                           test al, 4
002152D7  74 1E                           je 0x1402152f7
002152D9  E8 42 29 00 00                  call 0x140217c20
002152DE  EB 17                           jmp 0x1402152f7
002152E0  8B 05 72 8B CF 00               mov eax, dword ptr [rip + 0xcf8b72]
002152E6  85 C0                           test eax, eax
002152E8  75 AB                           jne 0x140215295
002152EA  48 8B 55 5F                     mov rdx, qword ptr [rbp + 0x5f]
002152EE  48 8D 4D 9F                     lea rcx, [rbp - 0x61]
002152F2  E8 F9 26 00 00                  call 0x1402179f0
002152F7  44 39 3D 22 1A DB 00            cmp dword ptr [rip + 0xdb1a22], r15d
002152FE  0F B6 75 AF                     movzx esi, byte ptr [rbp - 0x51]
00215302  74 0D                           je 0x140215311
00215304  44 0F 20 C1                     mov rcx, cr8
00215308  40 0F B6 D6                     movzx edx, sil
0021530C  E8 87 03 2E 00                  call 0x1404f5698
00215311  44 0F 22 C6                     mov cr8, rsi
00215315  65 FF 04 25 84 90 00 00         inc dword ptr gs:[0x9084]
0021531D  45 85 F6                        test r14d, r14d
00215320  0F 84 04 04 00 00               je 0x14021572a
00215326  0F 57 C0                        xorps xmm0, xmm0
00215329  0F 11 45 07                     movups xmmword ptr [rbp + 7], xmm0
0021532D  0F 11 45 17                     movups xmmword ptr [rbp + 0x17], xmm0
00215331  0F 11 45 27                     movups xmmword ptr [rbp + 0x27], xmm0
00215335  0F 31                           rdtsc
00215337  65 48 8B 34 25 20 00 00 00      mov rsi, qword ptr gs:[0x20]
00215340  48 C1 E2 20                     shl rdx, 0x20
00215344  48 0B C2                        or rax, rdx
00215347  44 88 7D 8A                     mov byte ptr [rbp - 0x76], r15b
0021534B  BA 00 00 01 00                  mov edx, 0x10000
00215350  4C 8B E0                        mov r12, rax
00215353  0F B6 8E D0 00 00 00            movzx ecx, byte ptr [rsi + 0xd0]
0021535A  FF 86 70 8F 00 00               inc dword ptr [rsi + 0x8f70]
00215360  66 89 4D 87                     mov word ptr [rbp - 0x79], cx
00215364  0F B6 8E D1 00 00 00            movzx ecx, byte ptr [rsi + 0xd1]
0021536B  88 4D 89                        mov byte ptr [rbp - 0x77], cl
0021536E  48 8B CB                        mov rcx, rbx
00215371  E8 BE 07 00 00                  call 0x140215b34
00215376  41 B9 04 00 00 00               mov r9d, 4
0021537C  48 85 C0                        test rax, rax
0021537F  74 13                           je 0x140215394
00215381  FF 86 74 8F 00 00               inc dword ptr [rsi + 0x8f74]
00215387  8B 4D 87                        mov ecx, dword ptr [rbp - 0x79]
0021538A  44 89 48 20                     mov dword ptr [rax + 0x20], r9d
0021538E  4C 89 20                        mov qword ptr [rax], r12
00215391  89 48 18                        mov dword ptr [rax + 0x18], ecx
00215394  65 4C 8B 04 25 88 01 00 00      mov r8, qword ptr gs:[0x188]
0021539D  41 8B D7                        mov edx, r15d
002153A0  49 8B 80 20 02 00 00            mov rax, qword ptr [r8 + 0x220]
002153A7  41 8B 88 A0 05 00 00            mov ecx, dword ptr [r8 + 0x5a0]
002153AE  C1 E9 09                        shr ecx, 9
002153B1  83 E1 07                        and ecx, 7
002153B4  48 8B 80 A0 02 00 00            mov rax, qword ptr [rax + 0x2a0]
002153BB  48 85 C0                        test rax, rax
002153BE  74 0B                           je 0x1402153cb
002153C0  8B 80 3C 04 00 00               mov eax, dword ptr [rax + 0x43c]
002153C6  3B C8                           cmp ecx, eax
002153C8  0F 4D C8                        cmovge ecx, eax
002153CB  83 F9 02                        cmp ecx, 2
002153CE  0F 8C 24 03 00 00               jl 0x1402156f8
002153D4  83 F9 01                        cmp ecx, 1
002153D7  7E 08                           jle 0x1402153e1
002153D9  F6 43 1A 04                     test byte ptr [rbx + 0x1a], 4
002153DD  41 0F 44 D1                     cmove edx, r9d
002153E1  41 0F BE 88 C3 00 00 00         movsx ecx, byte ptr [r8 + 0xc3]
002153E9  44 8B CA                        mov r9d, edx
002153EC  0F B6 43 1B                     movzx eax, byte ptr [rbx + 0x1b]
002153F0  41 83 C9 02                     or r9d, 2
002153F4  F6 43 1A 02                     test byte ptr [rbx + 0x1a], 2
002153F8  44 0F 45 CA                     cmovne r9d, edx
002153FC  41 8B D1                        mov edx, r9d
002153FF  81 CA 00 FF 00 00               or edx, 0xff00
00215405  3B C8                           cmp ecx, eax
00215407  41 0F 4E D1                     cmovle edx, r9d
0021540B  85 D2                           test edx, edx
0021540D  74 08                           je 0x140215417
0021540F  48 8B CB                        mov rcx, rbx
00215412  E8 F9 EA FF FF                  call 0x140213f10
00215417  41 B8 24 02 01 00               mov r8d, 0x10224
0021541D  48 8D 55 B7                     lea rdx, [rbp - 0x49]
00215421  48 8B CB                        mov rcx, rbx
00215424  E8 C7 12 00 00                  call 0x1402166f0
00215429  33 C0                           xor eax, eax
0021542B  0F 57 C0                        xorps xmm0, xmm0
0021542E  48 89 45 FF                     mov qword ptr [rbp - 1], rax
00215432  BE 01 00 00 00                  mov esi, 1
00215437  0F B7 43 1A                     movzx eax, word ptr [rbx + 0x1a]
0021543B  0F 11 45 EF                     movups xmmword ptr [rbp - 0x11], xmm0
0021543F  A8 08                           test al, 8
00215441  0F 85 3F 01 00 00               jne 0x140215586
00215447  41 8B D7                        mov edx, r15d
0021544A  A8 04                           test al, 4
0021544C  74 36                           je 0x140215484
0021544E  49 8B 85 20 02 00 00            mov rax, qword ptr [r13 + 0x220]
00215455  41 8B 8D A0 05 00 00            mov ecx, dword ptr [r13 + 0x5a0]
0021545C  C1 E9 09                        shr ecx, 9
0021545F  83 E1 07                        and ecx, 7
00215462  48 8B 80 A0 02 00 00            mov rax, qword ptr [rax + 0x2a0]
00215469  48 85 C0                        test rax, rax
0021546C  74 0B                           je 0x140215479
0021546E  8B 80 3C 04 00 00               mov eax, dword ptr [rax + 0x43c]
00215474  3B C8                           cmp ecx, eax
00215476  0F 4D C8                        cmovge ecx, eax
00215479  83 F9 02                        cmp ecx, 2
0021547C  B8 04 00 00 00                  mov eax, 4
00215481  0F 4C D0                        cmovl edx, eax
00215484  44 8B E2                        mov r12d, edx
00215487  41 83 CC 02                     or r12d, 2
0021548B  F6 43 1A 02                     test byte ptr [rbx + 0x1a], 2
0021548F  44 0F 44 E2                     cmove r12d, edx
00215493  45 85 E4                        test r12d, r12d
00215496  0F 84 EA 00 00 00               je 0x140215586
0021549C  48 89 7D F7                     mov qword ptr [rbp - 9], rdi
002154A0  4C 89 7D EF                     mov qword ptr [rbp - 0x11], r15
002154A4  90                              nop
002154A5  44 0F 20 C0                     mov rax, cr8
002154A9  48 89 45 97                     mov qword ptr [rbp - 0x69], rax
002154AD  B9 02 00 00 00                  mov ecx, 2
002154B2  44 0F 22 C1                     mov cr8, rcx
002154B6  44 39 3D 63 18 DB 00            cmp dword ptr [rip + 0xdb1863], r15d
002154BD  0F 85 03 02 00 00               jne 0x1402156c6
002154C3  F6 05 3C 16 DB 00 21            test byte ptr [rip + 0xdb163c], 0x21
002154CA  88 45 FF                        mov byte ptr [rbp - 1], al
002154CD  0F 85 82 01 00 00               jne 0x140215655
002154D3  48 8D 55 EF                     lea rdx, [rbp - 0x11]
002154D7  48 87 17                        xchg qword ptr [rdi], rdx
002154DA  48 85 D2                        test rdx, rdx
002154DD  0F 85 39 02 00 00               jne 0x14021571c
002154E3  48 8B 43 30                     mov rax, qword ptr [rbx + 0x30]
002154E7  48 8D 7B 30                     lea rdi, [rbx + 0x30]
002154EB  49 3B C5                        cmp rax, r13
002154EE  74 25                           je 0x140215515
002154F0  48 8B 7B 10                     mov rdi, qword ptr [rbx + 0x10]
002154F4  48 85 C0                        test rax, rax
002154F7  8B 53 48                        mov edx, dword ptr [rbx + 0x48]
002154FA  49 8B CF                        mov rcx, r15
002154FD  8B 43 40                        mov eax, dword ptr [rbx + 0x40]
00215500  0F 95 C1                        setne cl
00215503  48 03 D0                        add rdx, rax
00215506  4C 8B CF                        mov r9, rdi
00215509  48 85 FF                        test rdi, rdi
0021550C  0F 85 75 01 00 00               jne 0x140215687
00215512  49 8B FF                        mov rdi, r15
00215515  41 F6 C4 04                     test r12b, 4
00215519  0F 85 16 02 00 00               jne 0x140215735
0021551F  41 F6 C4 02                     test r12b, 2
00215523  74 30                           je 0x140215555
00215525  8B 47 08                        mov eax, dword ptr [rdi + 8]
00215528  A8 04                           test al, 4
0021552A  0F 85 4E 01 00 00               jne 0x14021567e
00215530  8B C6                           mov eax, esi
00215532  F0 41 0F C1 85 E4 05 00 00      lock xadd dword ptr [r13 + 0x5e4], eax
0021553B  FF C0                           inc eax
0021553D  3B C6                           cmp eax, esi
0021553F  75 10                           jne 0x140215551
00215541  41 0F B6 85 18 03 00 00         movzx eax, byte ptr [r13 + 0x318]
00215549  84 C0                           test al, al
0021554B  0F 85 29 02 00 00               jne 0x14021577a
00215551  83 4F 08 04                     or dword ptr [rdi + 8], 4
00215555  48 8D 4D EF                     lea rcx, [rbp - 0x11]
00215559  E8 82 D7 12 00                  call 0x140342ce0
0021555E  45 85 E4                        test r12d, r12d
00215561  74 23                           je 0x140215586
00215563  41 F6 C4 04                     test r12b, 4
00215567  74 0F                           je 0x140215578
00215569  45 33 C0                        xor r8d, r8d
0021556C  49 8B CD                        mov rcx, r13
0021556F  41 8D 50 02                     lea edx, [r8 + 2]
00215573  E8 98 0B 00 00                  call 0x140216110
00215578  41 F6 C4 02                     test r12b, 2
0021557C  74 08                           je 0x140215586
0021557E  49 8B CD                        mov rcx, r13
00215581  E8 CE 06 00 00                  call 0x140215c54
00215586  65 FF 04 25 7C 90 00 00         inc dword ptr gs:[0x907c]
0021558E  65 FF 04 25 64 90 00 00         inc dword ptr gs:[0x9064]
00215596  45 85 F6                        test r14d, r14d
00215599  0F 84 94 00 00 00               je 0x140215633
0021559F  8B 43 44                        mov eax, dword ptr [rbx + 0x44]
002155A2  89 45 97                        mov dword ptr [rbp - 0x69], eax
002155A5  44 89 7D 87                     mov dword ptr [rbp - 0x79], r15d
002155A9  0F 31                           rdtsc
002155AB  65 4C 8B 34 25 20 00 00 00      mov r14, qword ptr gs:[0x20]
002155B4  48 8B CB                        mov rcx, rbx
002155B7  48 C1 E2 20                     shl rdx, 0x20
002155BB  48 0B C2                        or rax, rdx
002155BE  44 88 7D 8A                     mov byte ptr [rbp - 0x76], r15b
002155C2  BA 00 00 01 00                  mov edx, 0x10000
002155C7  48 8B F8                        mov rdi, rax
002155CA  45 0F B6 AE D0 00 00 00         movzx r13d, byte ptr [r14 + 0xd0]
002155D2  45 0F B6 A6 D1 00 00 00         movzx r12d, byte ptr [r14 + 0xd1]
002155DA  41 FF 86 70 8F 00 00            inc dword ptr [r14 + 0x8f70]
002155E1  66 44 89 6D 87                  mov word ptr [rbp - 0x79], r13w
002155E6  44 88 65 89                     mov byte ptr [rbp - 0x77], r12b
002155EA  E8 45 05 00 00                  call 0x140215b34
002155EF  48 8B C8                        mov rcx, rax
002155F2  48 85 C0                        test rax, rax
002155F5  74 3C                           je 0x140215633
002155F7  41 FF 86 74 8F 00 00            inc dword ptr [r14 + 0x8f74]
002155FE  48 89 78 08                     mov qword ptr [rax + 8], rdi
00215602  8B 40 20                        mov eax, dword ptr [rax + 0x20]
00215605  85 C0                           test eax, eax
00215607  74 70                           je 0x140215679
00215609  83 F8 04                        cmp eax, 4
0021560C  75 6B                           jne 0x140215679
0021560E  66 44 39 69 18                  cmp word ptr [rcx + 0x18], r13w
00215613  75 5F                           jne 0x140215674
00215615  44 38 61 1A                     cmp byte ptr [rcx + 0x1a], r12b
00215619  75 59                           jne 0x140215674
0021561B  48 2B 39                        sub rdi, qword ptr [rcx]
0021561E  48 89 39                        mov qword ptr [rcx], rdi
00215621  8B 45 87                        mov eax, dword ptr [rbp - 0x79]
00215624  89 41 18                        mov dword ptr [rcx + 0x18], eax
00215627  8B 45 97                        mov eax, dword ptr [rbp - 0x69]
0021562A  89 41 2C                        mov dword ptr [rcx + 0x2c], eax
0021562D  89 71 20                        mov dword ptr [rcx + 0x20], esi
00215630  89 71 24                        mov dword ptr [rcx + 0x24], esi
00215633  44 0F B6 E6                     movzx r12d, sil
00215637  E9 6D FA FF FF                  jmp 0x1402150a9
0021563C  48 8D 4D 9F                     lea rcx, [rbp - 0x61]
00215640  E8 9B D6 12 00                  call 0x140342ce0
00215645  65 FF 04 25 88 90 00 00         inc dword ptr gs:[0x9088]
0021564D  45 32 E4                        xor r12b, r12b
00215650  E9 54 FA FF FF                  jmp 0x1402150a9
00215655  8B 05 FD 87 CF 00               mov eax, dword ptr [rip + 0xcf87fd]
0021565B  85 C0                           test eax, eax
0021565D  0F 85 70 FE FF FF               jne 0x1402154d3
00215663  48 8B D7                        mov rdx, rdi
00215666  48 8D 4D EF                     lea rcx, [rbp - 0x11]
0021566A  E8 E1 01 06 00                  call 0x140275850
0021566F  E9 6F FE FF FF                  jmp 0x1402154e3
00215674  48 89 31                        mov qword ptr [rcx], rsi
00215677  EB A8                           jmp 0x140215621
00215679  4C 89 39                        mov qword ptr [rcx], r15
0021567C  EB A3                           jmp 0x140215621
0021567E  41 83 E4 FD                     and r12d, 0xfffffffd
00215682  E9 CE FE FF FF                  jmp 0x140215555
00215687  44 8B 47 08                     mov r8d, dword ptr [rdi + 8]
0021568B  49 C1 E0 04                     shl r8, 4
0021568F  4C 03 C7                        add r8, rdi
00215692  48 83 C7 10                     add rdi, 0x10
00215696  48 3B CA                        cmp rcx, rdx
00215699  0F 83 73 FE FF FF               jae 0x140215512
0021569F  48 8B 07                        mov rax, qword ptr [rdi]
002156A2  49 3B C5                        cmp rax, r13
002156A5  74 33                           je 0x1402156da
002156A7  48 85 C0                        test rax, rax
002156AA  74 0C                           je 0x1402156b8
002156AC  48 FF C1                        inc rcx
002156AF  48 3B CA                        cmp rcx, rdx
002156B2  0F 84 5A FE FF FF               je 0x140215512
002156B8  48 83 C7 10                     add rdi, 0x10
002156BC  49 3B F8                        cmp rdi, r8
002156BF  75 DE                           jne 0x14021569f
002156C1  E9 4C FE FF FF                  jmp 0x140215512
002156C6  0F B6 D1                        movzx edx, cl
002156C9  0F B6 C8                        movzx ecx, al
002156CC  E8 2B 00 2E 00                  call 0x1404f56fc
002156D1  48 8B 45 97                     mov rax, qword ptr [rbp - 0x69]
002156D5  E9 E9 FD FF FF                  jmp 0x1402154c3
002156DA  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
002156E3  48 8B C7                        mov rax, rdi
002156E6  49 2B C1                        sub rax, r9
002156E9  48 C1 F8 04                     sar rax, 4
002156ED  88 81 60 04 00 00               mov byte ptr [rcx + 0x460], al
002156F3  E9 1D FE FF FF                  jmp 0x140215515
002156F8  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00215701  4C 3B C0                        cmp r8, rax
00215704  0F 85 CA FC FF FF               jne 0x1402153d4
0021570A  41 39 90 E0 05 00 00            cmp dword ptr [r8 + 0x5e0], edx
00215711  0F 84 BD FC FF FF               je 0x1402153d4
00215717  E9 BD FC FF FF                  jmp 0x1402153d9
0021571C  48 8D 4D EF                     lea rcx, [rbp - 0x11]
00215720  E8 8B 27 04 00                  call 0x140257eb0
00215725  E9 B9 FD FF FF                  jmp 0x1402154e3
0021572A  41 B9 04 00 00 00               mov r9d, 4
00215730  E9 5F FC FF FF                  jmp 0x140215394
00215735  8B 47 08                        mov eax, dword ptr [rdi + 8]
00215738  40 84 C6                        test sil, al
0021573B  75 34                           jne 0x140215771
0021573D  45 33 C9                        xor r9d, r9d
00215740  45 33 C0                        xor r8d, r8d
00215743  33 D2                           xor edx, edx
00215745  49 8B CD                        mov rcx, r13
00215748  E8 B3 D4 17 00                  call 0x140392c00
0021574D  09 77 08                        or dword ptr [rdi + 8], esi
00215750  E9 CA FD FF FF                  jmp 0x14021551f
00215755  48 89 4D BF                     mov qword ptr [rbp - 0x41], rcx
00215759  48 8D 55 B7                     lea rdx, [rbp - 0x49]
0021575D  48 89 45 B7                     mov qword ptr [rbp - 0x49], rax
00215761  48 89 11                        mov qword ptr [rcx], rdx
00215764  48 8D 4D B7                     lea rcx, [rbp - 0x49]
00215768  48 89 48 08                     mov qword ptr [rax + 8], rcx
0021576C  E9 1B FB FF FF                  jmp 0x14021528c
00215771  41 83 E4 FB                     and r12d, 0xfffffffb
00215775  E9 A5 FD FF FF                  jmp 0x14021551f
0021577A  44 0F 20 C0                     mov rax, cr8
0021577E  48 89 45 97                     mov qword ptr [rbp - 0x69], rax
00215782  B9 02 00 00 00                  mov ecx, 2
00215787  44 0F 22 C1                     mov cr8, rcx
0021578B  44 39 3D 8E 15 DB 00            cmp dword ptr [rip + 0xdb158e], r15d
00215792  75 53                           jne 0x1402157e7
00215794  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
0021579D  4D 8D 85 28 03 00 00            lea r8, [r13 + 0x328]
002157A4  49 8B CD                        mov rcx, r13
002157A7  48 89 45 87                     mov qword ptr [rbp - 0x79], rax
002157AB  48 8D 90 78 91 00 00            lea rdx, [rax + 0x9178]
002157B2  E8 29 99 00 00                  call 0x14021f0e0
002157B7  85 C0                           test eax, eax
002157B9  74 09                           je 0x1402157c4
002157BB  48 8B 4D 87                     mov rcx, qword ptr [rbp - 0x79]
002157BF  E8 0C 1D FF FF                  call 0x1402074d0
002157C4  44 39 3D 55 15 DB 00            cmp dword ptr [rip + 0xdb1555], r15d
002157CB  74 0D                           je 0x1402157da
002157CD  44 0F 20 C1                     mov rcx, cr8
002157D1  0F B6 55 97                     movzx edx, byte ptr [rbp - 0x69]
002157D5  E8 BE FE 2D 00                  call 0x1404f5698
002157DA  0F B6 45 97                     movzx eax, byte ptr [rbp - 0x69]
002157DE  44 0F 22 C0                     mov cr8, rax
002157E2  E9 6A FD FF FF                  jmp 0x140215551
002157E7  0F B6 D1                        movzx edx, cl
002157EA  0F B6 C8                        movzx ecx, al
002157ED  E8 0A FF 2D 00                  call 0x1404f56fc
002157F2  EB A0                           jmp 0x140215794
002157F4  65 48 8B 3C 25 88 01 00 00      mov rdi, qword ptr gs:[0x188]
002157FD  BE 01 00 00 00                  mov esi, 1
00215802  45 84 E4                        test r12b, r12b
00215805  0F 84 44 02 00 00               je 0x140215a4f
0021580B  44 8D 66 08                     lea r12d, [rsi + 8]
0021580F  40 0F B6 C6                     movzx eax, sil
00215813  44 8D 76 07                     lea r14d, [rsi + 7]
00215817  40 32 C6                        xor al, sil
0021581A  FE C0                           inc al
0021581C  44 0F 20 C2                     mov rdx, cr8
00215820  65 4C 8B 04 25 88 01 00 00      mov r8, qword ptr gs:[0x188]
00215829  3A D0                           cmp dl, al
0021582B  76 1A                           jbe 0x140215847
0021582D  44 0F B6 C2                     movzx r8d, dl
00215831  B9 C6 01 00 00                  mov ecx, 0x1c6
00215836  33 D2                           xor edx, edx
00215838  44 0F B6 C8                     movzx r9d, al
0021583C  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00215841  E8 1A 7E 2E 00                  call 0x1404fd660
00215846  CC                              int3
00215847  80 FA 02                        cmp dl, 2
0021584A  73 5D                           jae 0x1402158a9
0021584C  F6 C1 08                        test cl, 8
0021584F  75 26                           jne 0x140215877
00215851  41 0F B6 80 C0 00 00 00         movzx eax, byte ptr [r8 + 0xc0]
00215859  A8 02                           test al, 2
0021585B  74 1A                           je 0x140215877
0021585D  45 33 C9                        xor r9d, r9d
00215860  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00215865  45 33 C0                        xor r8d, r8d
00215868  B9 C6 01 00 00                  mov ecx, 0x1c6
0021586D  41 8D 51 06                     lea edx, [r9 + 6]
00215871  E8 EA 7D 2E 00                  call 0x1404fd660
00215876  CC                              int3
00215877  40 3A D6                        cmp dl, sil
0021587A  73 56                           jae 0x1402158d2
0021587C  41 F7 40 74 00 04 00 00         test dword ptr [r8 + 0x74], 0x400
00215884  75 4C                           jne 0x1402158d2
00215886  45 39 B8 E4 01 00 00            cmp dword ptr [r8 + 0x1e4], r15d
0021588D  75 43                           jne 0x1402158d2
0021588F  45 33 C9                        xor r9d, r9d
00215892  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00215897  45 33 C0                        xor r8d, r8d
0021589A  B9 C6 01 00 00                  mov ecx, 0x1c6
0021589F  41 8D 51 07                     lea edx, [r9 + 7]
002158A3  E8 B8 7D 2E 00                  call 0x1404fd660
002158A8  CC                              int3
002158A9  65 8B 04 25 3C 3A 00 00         mov eax, dword ptr gs:[0x3a3c]
002158B1  A9 01 00 01 00                  test eax, 0x10001
002158B6  74 94                           je 0x14021584c
002158B8  45 33 C9                        xor r9d, r9d
002158BB  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
002158C0  45 33 C0                        xor r8d, r8d
002158C3  B9 C6 01 00 00                  mov ecx, 0x1c6
002158C8  41 8D 51 05                     lea edx, [r9 + 5]
002158CC  E8 8F 7D 2E 00                  call 0x1404fd660
002158D1  CC                              int3
002158D2  45 8B C7                        mov r8d, r15d
002158D5  45 85 F6                        test r14d, r14d
002158D8  48 8B CB                        mov rcx, rbx
002158DB  41 0F 94 C0                     sete r8b
002158DF  33 D2                           xor edx, edx
002158E1  E8 4A A9 FF FF                  call 0x140210230
002158E6  48 8B D0                        mov rdx, rax
002158E9  48 89 45 97                     mov qword ptr [rbp - 0x69], rax
002158ED  33 C0                           xor eax, eax
002158EF  F0 48 0F B1 33                  lock cmpxchg qword ptr [rbx], rsi
002158F4  4C 8D 6B 40                     lea r13, [rbx + 0x40]
002158F8  0F 85 B4 00 00 00               jne 0x1402159b2
002158FE  41 F6 C4 10                     test r12b, 0x10
00215902  B9 03 00 00 00                  mov ecx, 3
00215907  B8 0F 00 00 00                  mov eax, 0xf
0021590C  0F 45 C8                        cmovne ecx, eax
0021590F  44 8B F1                        mov r14d, ecx
00215912  8B D9                           mov ebx, ecx
00215914  41 83 E6 02                     and r14d, 2
00215918  83 E3 04                        and ebx, 4
0021591B  F6 C1 08                        test cl, 8
0021591E  0F 84 86 00 00 00               je 0x1402159aa
00215924  44 0F B6 E6                     movzx r12d, sil
00215928  85 DB                           test ebx, ebx
0021592A  41 89 75 20                     mov dword ptr [r13 + 0x20], esi
0021592E  41 0F 95 C7                     setne r15b
00215932  4C 0B FF                        or r15, rdi
00215935  4D 89 7D 10                     mov qword ptr [r13 + 0x10], r15
00215939  48 85 D2                        test rdx, rdx
0021593C  74 13                           je 0x140215951
0021593E  0F B6 42 08                     movzx eax, byte ptr [rdx + 8]
00215942  24 3F                           and al, 0x3f
00215944  40 88 72 0A                     mov byte ptr [rdx + 0xa], sil
00215948  02 C0                           add al, al
0021594A  40 0A C6                        or al, sil
0021594D  41 88 45 24                     mov byte ptr [r13 + 0x24], al
00215951  45 85 F6                        test r14d, r14d
00215954  74 01                           je 0x140215957
00215956  FA                              cli
00215957  85 DB                           test ebx, ebx
00215959  0F 85 7A 01 00 00               jne 0x140215ad9
0021595F  48 8D 87 B8 06 00 00            lea rax, [rdi + 0x6b8]
00215966  48 8B 08                        mov rcx, qword ptr [rax]
00215969  48 39 41 08                     cmp qword ptr [rcx + 8], rax
0021596D  0F 85 4F F8 FF FF               jne 0x1402151c2
00215973  49 89 4D 00                     mov qword ptr [r13], rcx
00215977  49 89 45 08                     mov qword ptr [r13 + 8], rax
0021597B  4C 89 69 08                     mov qword ptr [rcx + 8], r13
0021597F  4C 89 28                        mov qword ptr [rax], r13
00215982  45 85 F6                        test r14d, r14d
00215985  74 16                           je 0x14021599d
00215987  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
00215990  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
00215997  4D 85 C0                        test r8, r8
0021599A  75 39                           jne 0x1402159d5
0021599C  FB                              sti
0021599D  85 DB                           test ebx, ebx
0021599F  75 73                           jne 0x140215a14
002159A1  40 0F B6 C6                     movzx eax, sil
002159A5  E9 03 F7 FF FF                  jmp 0x1402150ad
002159AA  45 32 E4                        xor r12b, r12b
002159AD  E9 76 FF FF FF                  jmp 0x140215928
002159B2  49 39 7D 10                     cmp qword ptr [r13 + 0x10], rdi
002159B6  74 42                           je 0x1402159fa
002159B8  45 85 F6                        test r14d, r14d
002159BB  74 72                           je 0x140215a2f
002159BD  4C 8B CA                        mov r9, rdx
002159C0  44 89 64 24 20                  mov dword ptr [rsp + 0x20], r12d
002159C5  48 8B D0                        mov rdx, rax
002159C8  4C 8B C7                        mov r8, rdi
002159CB  48 8B CB                        mov rcx, rbx
002159CE  E8 0D 89 1A 00                  call 0x1403be2e0
002159D3  EB CC                           jmp 0x1402159a1
002159D5  41 0F 0D 08                     prefetchw byte ptr [r8]
002159D9  41 8B 00                        mov eax, dword ptr [r8]
002159DC  8B D0                           mov edx, eax
002159DE  0F BA F2 15                     btr edx, 0x15
002159E2  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
002159E7  75 F3                           jne 0x1402159dc
002159E9  0F BA E0 15                     bt eax, 0x15
002159ED  73 05                           jae 0x1402159f4
002159EF  E8 DC D7 04 00                  call 0x1402631d0
002159F4  48 8B 55 97                     mov rdx, qword ptr [rbp - 0x69]
002159F8  EB A2                           jmp 0x14021599c
002159FA  41 FF 45 20                     inc dword ptr [r13 + 0x20]
002159FE  48 85 D2                        test rdx, rdx
00215A01  74 9E                           je 0x1402159a1
00215A03  48 8B CB                        mov rcx, rbx
00215A06  E8 05 C8 04 00                  call 0x140262210
00215A0B  40 0F B6 C6                     movzx eax, sil
00215A0F  E9 99 F6 FF FF                  jmp 0x1402150ad
00215A14  45 84 E4                        test r12b, r12b
00215A17  75 2A                           jne 0x140215a43
00215A19  BA 44 66 6C 74                  mov edx, 0x746c6644
00215A1E  48 8B CF                        mov rcx, rdi
00215A21  E8 EA AC FF FF                  call 0x140210710
00215A26  40 0F B6 C6                     movzx eax, sil
00215A2A  E9 7E F6 FF FF                  jmp 0x1402150ad
00215A2F  48 85 D2                        test rdx, rdx
00215A32  74 08                           je 0x140215a3c
00215A34  48 8B CB                        mov rcx, rbx
00215A37  E8 D4 C7 04 00                  call 0x140262210
00215A3C  32 C0                           xor al, al
00215A3E  E9 6A F6 FF FF                  jmp 0x1402150ad
00215A43  48 85 D2                        test rdx, rdx
00215A46  74 D1                           je 0x140215a19
00215A48  E8 5F 8E 1A 00                  call 0x1403be8ac
00215A4D  EB CA                           jmp 0x140215a19
00215A4F  45 8B F7                        mov r14d, r15d
00215A52  32 C0                           xor al, al
00215A54  44 8B E6                        mov r12d, esi
00215A57  E9 BB FD FF FF                  jmp 0x140215817
00215A5C  44 0F 20 C2                     mov rdx, cr8
00215A60  65 4C 8B 0C 25 88 01 00 00      mov r9, qword ptr gs:[0x188]
00215A69  41 3A D0                        cmp dl, r8b
00215A6C  76 1A                           jbe 0x140215a88
00215A6E  45 0F B6 C8                     movzx r9d, r8b
00215A72  B9 C6 01 00 00                  mov ecx, 0x1c6
00215A77  44 0F B6 C2                     movzx r8d, dl
00215A7B  33 D2                           xor edx, edx
00215A7D  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00215A82  E8 D9 7B 2E 00                  call 0x1404fd660
00215A87  CC                              int3
00215A88  80 FA 02                        cmp dl, 2
00215A8B  72 13                           jb 0x140215aa0
00215A8D  65 8B 04 25 3C 3A 00 00         mov eax, dword ptr gs:[0x3a3c]
00215A95  A9 01 00 01 00                  test eax, 0x10001
00215A9A  0F 85 18 FE FF FF               jne 0x1402158b8
00215AA0  41 0F B6 81 C0 00 00 00         movzx eax, byte ptr [r9 + 0xc0]
00215AA8  A8 02                           test al, 2
00215AAA  0F 85 AD FD FF FF               jne 0x14021585d
00215AB0  80 FA 01                        cmp dl, 1
00215AB3  0F 83 3B FD FF FF               jae 0x1402157f4
00215AB9  41 F7 41 74 00 04 00 00         test dword ptr [r9 + 0x74], 0x400
00215AC1  0F 85 2D FD FF FF               jne 0x1402157f4
00215AC7  45 39 B9 E4 01 00 00            cmp dword ptr [r9 + 0x1e4], r15d
00215ACE  0F 84 BB FD FF FF               je 0x14021588f
00215AD4  E9 1B FD FF FF                  jmp 0x1402157f4
00215AD9  48 8D 8F C8 06 00 00            lea rcx, [rdi + 0x6c8]
00215AE0  E8 4B 29 FF FF                  call 0x140208430
00215AE5  48 8D 87 D0 06 00 00            lea rax, [rdi + 0x6d0]
00215AEC  48 8B 10                        mov rdx, qword ptr [rax]
00215AEF  48 39 42 08                     cmp qword ptr [rdx + 8], rax
00215AF3  0F 85 C9 F6 FF FF               jne 0x1402151c2
00215AF9  49 89 55 00                     mov qword ptr [r13], rdx
00215AFD  48 8D 8F C8 06 00 00            lea rcx, [rdi + 0x6c8]
00215B04  49 89 45 08                     mov qword ptr [r13 + 8], rax
00215B08  4C 89 6A 08                     mov qword ptr [rdx + 8], r13
00215B0C  4C 89 28                        mov qword ptr [rax], r13
00215B0F  E8 5C 0B FF FF                  call 0x140206670
00215B14  48 8B 55 97                     mov rdx, qword ptr [rbp - 0x69]
00215B18  E9 65 FE FF FF                  jmp 0x140215982
00215B1D  39 78 24                        cmp dword ptr [rax + 0x24], edi
00215B20  0F 83 43 F7 FF FF               jae 0x140215269
00215B26  89 78 24                        mov dword ptr [rax + 0x24], edi
00215B29  E9 3B F7 FF FF                  jmp 0x140215269
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00215166(void)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_rdi;
    unsigned __int64 v_stack_p20;

    if (!sign_flag) goto loc_00215174;
    if ((*(unsigned __int64 *)(v_rbx + 48)) == v_r13) goto loc_002151C9;
loc_00215174:
    if ((unsigned __int8)(v_r12) == 0) goto loc_0021563C;
    *(unsigned __int64 *)(v_rbp - 33) = v_rbp - 41;
    *(unsigned __int64 *)(v_rbp - 41) = v_rbp - 41;
    *(unsigned __int64 *)(v_rbp - 73) = v_r15;
    *(unsigned __int64 *)(v_rbp - 65) = v_r15;
    *(unsigned __int64 *)(v_rbp - 49) = 0x60001ULL;
    *(unsigned __int64 *)(v_rbp - 57) = v_r13;
    *(unsigned __int64 *)(v_rbp - 25) = v_r15;
    if (*(unsigned __int64 *)(v_rbx + 40) == 0) goto loc_00215274;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 40) + 8))) == (*(unsigned __int64 *)(v_rbx + 40))) goto loc_00215755;
loc_002151C2:
loc_002151C9:
    v_rdi = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbx + 56))) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 56)) + 8)));
    v_rdi = (unsigned int)((v_rdi) & (7));
    v_rdi = (unsigned int)((v_rdi) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 56)) + 8)));
    *(unsigned int *)(v_rbx + 56) = (unsigned int)(v_rdi);
    v_rdi = (unsigned int)((v_rdi) >> (3));
    result = KeReleaseInStackQueuedSpinLock(v_rbp - 97, a2, a3, a4);
    if ((unsigned int)(v_r14) == 0) goto loc_0021526C;
    *(unsigned __int8 *)(v_rbp - 118) = (unsigned __int8)(v_r15);
    *(unsigned __int16 *)(v_rbp - 121) = (unsigned __int16)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 208));
    *(unsigned __int8 *)(v_rbp - 119) = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 209));
    result = EtwpGetTrackingLockSlotForThread(v_rbx, (unsigned int)(0x10000ULL), a3, a4);
    if (result == 0) goto loc_0021526C;
    if ((*(unsigned int *)(result + 32)) != ((unsigned int)(v_r15))) goto loc_00215B1D;
    *(unsigned __int64 *)(result) = 1;
    *(unsigned __int64 *)(result + 8) = 2;
    *(unsigned int *)(result + 24) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbp - 121)));
    *(unsigned int *)(result + 36) = (unsigned int)(v_rdi);
    *(unsigned int *)(result + 44) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 68)));
loc_00215269:
    *(unsigned int *)(result + 32) = 1;
loc_0021526C:
loc_00215274:
    *(unsigned __int64 *)(v_rbp - 65) = v_rbp - 73;
    *(unsigned __int64 *)(v_rbp - 73) = v_rbp - 73;
    *(unsigned __int64 *)(v_rbx + 40) = v_rbp - 73;
loc_0021528C:
    if (((*(unsigned __int8 *)(v_rip + 14358643)) & (1)) != 0) goto loc_002152E0;
loc_00215295:
    if (*(unsigned __int64 *)(v_rbp - 97) != 0) goto loc_002152C1;
    if ((v_rbp - 97) == (v_rbp - 97)) goto loc_002152F7;
    result = KxWaitForLockChainValid(v_rbp - 97, (unsigned int)(0x10000ULL), a3, a4);
loc_002152C1:
    *(unsigned __int64 *)(v_rbp - 97) = v_r15;
    result = (unsigned __int8)((*(unsigned __int64 *)(v_rbp - 89)) ^ ((unsigned __int8)(*(unsigned __int64 *)(v_rbp - 89))));
    if ((((unsigned __int8)(result)) & (4)) == 0) goto loc_002152F7;
    result = KeWakeAddressAll(result + 8, *(unsigned __int64 *)(v_rbp - 89), a3, a4);
    goto loc_002152F7;
loc_002152E0:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13601650))) != 0) goto loc_00215295;
    result = KiReleaseQueuedSpinLockInstrumented(v_rbp - 97, *(unsigned __int64 *)(v_rbp + 95), a3, a4);
loc_002152F7:
    if ((*(unsigned int *)(v_rip + 14359074)) != ((unsigned int)(v_r15))) {
        a1 = v_cr8;
        a2 = (unsigned __int8)(*(unsigned __int8 *)(v_rbp - 81));
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, a3, a4);
    }
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 68))) == 0) goto loc_0021572A;
    *(unsigned __int64 *)(v_rbp + 7) = v_xmm0;
    *(unsigned __int64 *)(v_rbp + 23) = v_xmm0;
    *(unsigned __int64 *)(v_rbp + 39) = v_xmm0;
    a2 = (a2) << (32);
    result = (result) | (a2);
    *(unsigned __int8 *)(v_rbp - 118) = (unsigned __int8)(v_r15);
    *(unsigned __int16 *)(v_rbp - 121) = (unsigned __int16)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 208));
    *(unsigned __int8 *)(v_rbp - 119) = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 209));
    result = EtwpGetTrackingLockSlotForThread(v_rbx, (unsigned int)(0x10000ULL), a3, a4);
    if (result != 0) {
        a1 = *(unsigned int *)(v_rbp - 121);
        *(unsigned int *)(result + 32) = 4;
        *(unsigned __int64 *)(result) = result;
        *(unsigned int *)(result + 24) = (unsigned int)(a1);
    }
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1440))) >> (9));
    a1 = (unsigned int)((a1) & (7));
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544) + 672);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544) + 672) != 0) {
        result = *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544) + 672) + 1084);
        if (((unsigned int)(a1)) >= ((unsigned int)(result))) { a1 = (unsigned int)(result); }
    }
    if (((unsigned int)(a1)) < 2) goto loc_002156F8;
loc_002153D4:
    if (((unsigned int)(a1)) >= = 1) {
        a2 = (unsigned int)((unsigned int)(v_r15));
        if (((*(unsigned __int8 *)(v_rbx + 26)) & (4)) == 0) { a2 = 4; }
    }
    a4 = (unsigned int)(((unsigned int)((unsigned int)(a2))) | (2));
    if (((*(unsigned __int8 *)(v_rbx + 26)) & (2)) != 0) { a4 = (unsigned int)(a2); }
    a2 = (unsigned int)(((unsigned int)((unsigned int)(a4))) | (0xFF00ULL));
    if (((unsigned int)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 195)))) <= ((unsigned int)(*(unsigned __int8 *)(v_rbx + 27)))) { a2 = (unsigned int)(a4); }
    result = *(unsigned __int8 *)(v_rbx + 27);
    if ((unsigned int)(a2) != 0) {
        a1 = v_rbx;
        result = ExpApplyPriorityBoost(a1, a2, *(unsigned __int64 *)(gs_base + (0 + 392)), a4);
    }
    result = ExpWaitForResource(v_rbx, v_rbp - 73, (unsigned int)(0x10224ULL), a4);
    result = 0;
    *(unsigned __int64 *)(v_rbp - 1) = 0;
    *(unsigned __int64 *)(v_rbp - 17) = v_xmm0;
    if ((((unsigned __int8)(*(unsigned __int16 *)(v_rbx + 26))) & (8)) != 0) goto loc_00215586;
    if ((((unsigned __int8)(*(unsigned __int16 *)(v_rbx + 26))) & (4)) == 0) goto loc_00215484;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r13 + 1440))) >> (9));
    a1 = (unsigned int)((a1) & (7));
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_r13 + 544) + 672);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_r13 + 544) + 672) != 0) {
        result = *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r13 + 544) + 672) + 1084);
        if (((unsigned int)(a1)) >= ((unsigned int)(result))) { a1 = (unsigned int)(result); }
    }
    a2 = (unsigned int)((unsigned int)(v_r15));
    if (((unsigned int)(a1)) < 2) { a2 = 4; }
loc_00215484:
    v_r12 = (unsigned int)(((unsigned int)((unsigned int)(a2))) | (2));
    if (((*(unsigned __int8 *)(v_rbx + 26)) & (2)) == 0) { v_r12 = (unsigned int)(a2); }
    if ((unsigned int)(v_r12) == 0) goto loc_00215586;
    *(unsigned __int64 *)(v_rbp - 9) = v_rdi;
    *(unsigned __int64 *)(v_rbp - 17) = v_r15;
    *(unsigned __int64 *)(v_rbp - 105) = *(unsigned __int8 *)(v_rbp - 81);
    if ((*(unsigned int *)(v_rip + 14358627)) != ((unsigned int)(v_r15))) goto loc_002156C6;
loc_002154C3:
    *(unsigned __int8 *)(v_rbp - 1) = (unsigned __int8)(*(unsigned __int8 *)(v_rbp - 81));
    if (((*(unsigned __int8 *)(v_rip + 14358076)) & (33)) != 0) goto loc_00215655;
loc_002154D3:
    if (v_rbp - 17 != 0) goto loc_0021571C;
loc_002154E3:
    if ((*(unsigned __int64 *)(v_rbx + 48)) == v_r13) goto loc_00215515;
    a1 = (*(unsigned __int64 *)(v_rbx + 48) != 0) ? 1 : 0;
    a2 = ((unsigned int)(*(unsigned int *)(v_rbx + 72))) + ((unsigned int)(*(unsigned int *)(v_rbx + 64)));
    if (*(unsigned __int64 *)(v_rbx + 16) != 0) goto loc_00215687;
loc_00215512:
loc_00215515:
    if ((((unsigned __int8)(v_r12)) & (4)) != 0) goto loc_00215735;
loc_0021551F:
    if ((((unsigned __int8)(v_r12)) & (2)) == 0) goto loc_00215555;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_r15 + 8)))) & (4)) != 0) goto loc_0021567E;
    result = (unsigned int)((1) + 1);
    if (((unsigned int)(result)) != 1) goto loc_00215551;
    if ((unsigned __int8)(*(unsigned __int8 *)(v_r13 + 792)) != 0) goto loc_0021577A;
loc_00215551:
loc_00215555:
    result = KeReleaseInStackQueuedSpinLock(v_rbp - 17, a2, (unsigned int)(0x10224ULL), *(unsigned __int64 *)(v_rbx + 16));
    if ((unsigned int)(v_r12) == 0) goto loc_00215586;
    if ((((unsigned __int8)(v_r12)) & (4)) != 0) {
        a3 = 0;
        a1 = v_r13;
        a2 = a3 + 2;
        result = IoBoostThreadIoPriority(a1, a2, a3, *(unsigned __int64 *)(v_rbx + 16));
    }
    if ((((unsigned __int8)(v_r12)) & (2)) != 0) {
        a1 = v_r13;
        result = PsBoostThreadOutstandingIoQoS(a1, a2, a3, *(unsigned __int64 *)(v_rbx + 16));
    }
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 68))) == 0) goto loc_00215633;
    *(unsigned int *)(v_rbp - 105) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 68)));
    *(unsigned int *)(v_rbp - 121) = (unsigned int)(v_r15);
    a2 = (a2) << (32);
    result = ((unsigned int)(*(unsigned int *)(v_rbx + 68))) | (a2);
    *(unsigned __int8 *)(v_rbp - 118) = (unsigned __int8)(v_r15);
    *(unsigned __int16 *)(v_rbp - 121) = (unsigned __int16)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 208));
    *(unsigned __int8 *)(v_rbp - 119) = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 209));
    result = EtwpGetTrackingLockSlotForThread(v_rbx, (unsigned int)(0x10000ULL), a3, *(unsigned __int64 *)(v_rbx + 16));
    if (result == 0) goto loc_00215633;
    *(unsigned __int64 *)(result + 8) = result;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(result + 32))) == 0) goto loc_00215679;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result + 32)))) != 4) goto loc_00215679;
    if ((*(unsigned __int16 *)(result + 24)) != ((unsigned __int16)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 208)))) goto loc_00215674;
    if ((*(unsigned __int8 *)(result + 26)) != ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 209)))) goto loc_00215674;
    v_rdi = (result) - (*(unsigned __int64 *)(result));
    *(unsigned __int64 *)(result) = v_rdi;
loc_00215621:
    *(unsigned int *)(result + 24) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbp - 121)));
    *(unsigned int *)(result + 44) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbp - 105)));
    *(unsigned int *)(result + 32) = 1;
    *(unsigned int *)(result + 36) = 1;
loc_00215633:
loc_0021563C:
    result = KeReleaseInStackQueuedSpinLock(v_rbp - 97, (unsigned int)(0x10000ULL), a3, *(unsigned __int64 *)(v_rbx + 16));
    v_r12 = 0;
loc_00215655:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13600765))) != 0) goto loc_002154D3;
    result = KiAcquireQueuedSpinLockInstrumented(v_rbp - 17, v_rdi, a3, *(unsigned __int64 *)(v_rbx + 16));
    goto loc_002154E3;
loc_00215674:
    *(unsigned __int64 *)(v_rbp - 17) = 1;
    goto loc_00215621;
loc_00215679:
    *(unsigned __int64 *)(v_rbp - 17) = v_r15;
    goto loc_00215621;
loc_0021567E:
    v_r12 = (unsigned int)((v_r12) & (0xFFFFFFFDULL));
    goto loc_00215555;
loc_00215687:
    a3 = ((unsigned int)(*(unsigned int *)(v_rdi + 8))) << (4);
    a3 = (a3) + (v_rdi);
    v_rdi = (v_rdi) + (16);
    if ((v_rbp - 17) >= v_rdi) goto loc_00215512;
loc_0021569F:
    if ((*(unsigned __int64 *)(v_rdi)) == (*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 208))) goto loc_002156DA;
    if (*(unsigned __int64 *)(v_rdi) == 0) goto loc_002156B8;
    a1 = (v_rbp - 17) + 1;
    if (a1 == v_rdi) goto loc_00215512;
loc_002156B8:
    v_rdi = (v_rdi) + (16);
    if (v_rdi != a3) goto loc_0021569F;
    goto loc_00215512;
loc_002156C6:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(*(unsigned __int64 *)(v_rdi)), (unsigned __int8)(a1), a3, *(unsigned __int64 *)(v_rbx + 16));
    goto loc_002154C3;
loc_002156DA:
    result = (v_rdi) - (*(unsigned __int64 *)(v_rbx + 16));
    result = (result) >> (4);
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1120) = (unsigned __int8)(result);
    goto loc_00215515;
loc_002156F8:
    if (a3 != (*(unsigned __int64 *)(gs_base + (0 + 392)))) goto loc_002153D4;
    if ((*(unsigned int *)(a3 + 1504)) == ((unsigned int)((unsigned __int8)(a1)))) goto loc_002153D4;
    goto loc_002153D9;
loc_0021571C:
    result = KxWaitForLockOwnerShip(v_rbp - 17, (unsigned __int8)(a1), a3, *(unsigned __int64 *)(v_rbx + 16));
    goto loc_002154E3;
loc_0021572A:
    goto loc_00215394;
loc_00215735:
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rdi + 8))))) != 0) goto loc_00215771;
    a4 = 0;
    a3 = 0;
    a2 = 0;
    result = PsBoostThreadIoEx(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 208), a2, a3, a4);
    goto loc_0021551F;
loc_00215755:
    *(unsigned __int64 *)(v_rbp - 65) = *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 208);
    *(unsigned __int64 *)(v_rbp - 73) = result;
    *(unsigned __int64 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 208)) = v_rbp - 73;
    *(unsigned __int64 *)(result + 8) = v_rbp - 73;
    goto loc_0021528C;
loc_00215771:
    v_r12 = (unsigned int)((v_r12) & (0xFFFFFFFBULL));
    goto loc_0021551F;
loc_0021577A:
    *(unsigned __int64 *)(v_rbp - 105) = 2;
    if ((*(unsigned int *)(v_rip + 14357902)) != ((unsigned int)(v_r15))) goto loc_002157E7;
loc_00215794:
    *(unsigned __int64 *)(v_rbp - 121) = *(unsigned __int64 *)(gs_base + (0 + 32));
    result = KiAbThreadInsertList(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 208), *(unsigned __int64 *)(gs_base + (0 + 32)) + 37240, *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 208) + 808, a4);
    if ((unsigned int)(result) != 0) {
        a1 = *(unsigned __int64 *)(v_rbp - 121);
        result = KiAbQueueAutoBoostDpc(a1, *(unsigned __int64 *)(gs_base + (0 + 32)) + 37240, *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 208) + 808, a4);
    }
    if ((*(unsigned int *)(v_rip + 14357845)) != ((unsigned int)(v_r15))) {
        a1 = 2;
        a2 = *(unsigned __int8 *)(v_rbp - 105);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 208) + 808, a4);
    }
    goto loc_00215551;
loc_002157E7:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(*(unsigned __int8 *)(v_rbp - 105)), (unsigned __int8)(a1), *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 208) + 808, a4);
    goto loc_00215794;
loc_00215B1D:
    if ((*(unsigned int *)(result + 36)) >= ((unsigned int)(v_rdi))) goto loc_00215269;
    *(unsigned int *)(result + 36) = (unsigned int)(v_rdi);
    goto loc_00215269;
}
```

## 5. (Beta) C Style

```c
void sub_00215166(void)
{
    int64_t result;
    int64_t local_r12;
    int64_t local_rdi;
    uint64_t v_stack_p20;

    if (!sign_flag) goto loc_00215174;
    if ((*(uint64_t *)(local_rbx + 0x30)) == local_r13) goto loc_002151C9;
loc_00215174:
    if ((uint8_t)(local_r12) == 0) goto loc_0021563C;
    *(uint64_t *)(local_rbp - 0x21) = local_rbp - 41;
    *(uint64_t *)(local_rbp - 0x29) = local_rbp - 41;
    *(uint64_t *)(local_rbp - 0x49) = local_r15;
    *(uint64_t *)(local_rbp - 0x41) = local_r15;
    *(uint64_t *)(local_rbp - 0x31) = 0x60001ULL;
    *(uint64_t *)(local_rbp - 0x39) = local_r13;
    *(uint64_t *)(local_rbp - 0x19) = local_r15;
    if (*(uint64_t *)(local_rbx + 0x28) == 0) goto loc_00215274;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rbx + 0x28) + 0x8))) == (*(uint64_t *)(local_rbx + 0x28))) goto loc_00215755;
loc_002151C2:
loc_002151C9:
    local_rdi = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbx + 0x38))) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x38)) + 8)));
    local_rdi = (uint32_t)((local_rdi) & (7));
    local_rdi = (uint32_t)((local_rdi) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x38)) + 8)));
    *(uint32_t *)(local_rbx + 0x38) = (uint32_t)(local_rdi);
    local_rdi = (uint32_t)((local_rdi) >> (3));
    result = KeReleaseInStackQueuedSpinLock(local_rbp - 97, a2, a3, a4);
    if ((uint32_t)(local_r14) == 0) goto loc_0021526C;
    *(uint8_t *)(local_rbp - 0x76) = (uint8_t)(local_r15);
    *(uint16_t *)(local_rbp - 0x79) = (uint16_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xD0));
    *(uint8_t *)(local_rbp - 0x77) = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xD1));
    result = EtwpGetTrackingLockSlotForThread(local_rbx, (uint32_t)(0x10000ULL), a3, a4);
    if (result == 0) goto loc_0021526C;
    if ((*(uint32_t *)(result + 0x20)) != ((uint32_t)(local_r15))) goto loc_00215B1D;
    *(uint64_t *)(result) = 1;
    *(uint64_t *)(result + 0x8) = 2;
    *(uint32_t *)(result + 0x18) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbp - 0x79)));
    *(uint32_t *)(result + 0x24) = (uint32_t)(local_rdi);
    *(uint32_t *)(result + 0x2C) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x44)));
loc_00215269:
    *(uint32_t *)(result + 0x20) = 1;
loc_0021526C:
loc_00215274:
    *(uint64_t *)(local_rbp - 0x41) = local_rbp - 73;
    *(uint64_t *)(local_rbp - 0x49) = local_rbp - 73;
    *(uint64_t *)(local_rbx + 0x28) = local_rbp - 73;
loc_0021528C:
    if (((*(uint8_t *)(v_rip + 0xDB1873)) & (1)) != 0) goto loc_002152E0;
loc_00215295:
    if (*(uint64_t *)(local_rbp - 0x61) != 0) goto loc_002152C1;
    if ((local_rbp - 97) == (local_rbp - 97)) goto loc_002152F7;
    result = KxWaitForLockChainValid(local_rbp - 97, (uint32_t)(0x10000ULL), a3, a4);
loc_002152C1:
    *(uint64_t *)(local_rbp - 0x61) = local_r15;
    result = (uint8_t)((*(uint64_t *)(local_rbp - 0x59)) ^ ((uint8_t)(*(uint64_t *)(local_rbp - 0x59))));
    if ((((uint8_t)(result)) & (4)) == 0) goto loc_002152F7;
    result = KeWakeAddressAll(result + 8, *(uint64_t *)(local_rbp - 0x59), a3, a4);
    goto loc_002152F7;
loc_002152E0:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCF8B72))) != 0) goto loc_00215295;
    result = KiReleaseQueuedSpinLockInstrumented(local_rbp - 97, *(uint64_t *)(local_rbp + 0x5F), a3, a4);
loc_002152F7:
    if ((*(uint32_t *)(v_rip + 0xDB1A22)) != ((uint32_t)(local_r15))) {
        a1 = v_cr8;
        a2 = (uint8_t)(*(uint8_t *)(local_rbp - 0x51));
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, a3, a4);
    }
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x44))) == 0) goto loc_0021572A;
    *(uint64_t *)(local_rbp + 0x7) = v_xmm0;
    *(uint64_t *)(local_rbp + 0x17) = v_xmm0;
    *(uint64_t *)(local_rbp + 0x27) = v_xmm0;
    a2 = (a2) << (32);
    result = (result) | (a2);
    *(uint8_t *)(local_rbp - 0x76) = (uint8_t)(local_r15);
    *(uint16_t *)(local_rbp - 0x79) = (uint16_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xD0));
    *(uint8_t *)(local_rbp - 0x77) = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xD1));
    result = EtwpGetTrackingLockSlotForThread(local_rbx, (uint32_t)(0x10000ULL), a3, a4);
    if (result != 0) {
        a1 = *(uint32_t *)(local_rbp - 0x79);
        *(uint32_t *)(result + 0x20) = 4;
        *(uint64_t *)(result) = result;
        *(uint32_t *)(result + 0x18) = (uint32_t)(a1);
    }
    a1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5A0))) >> (9));
    a1 = (uint32_t)((a1) & (7));
    result = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220) + 0x2A0);
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220) + 0x2A0) != 0) {
        result = *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220) + 0x2A0) + 0x43C);
        if (((uint32_t)(a1)) >= ((uint32_t)(result))) { a1 = (uint32_t)(result); }
    }
    if (((uint32_t)(a1)) < 2) goto loc_002156F8;
loc_002153D4:
    if (((uint32_t)(a1)) >= = 1) {
        a2 = (uint32_t)((uint32_t)(local_r15));
        if (((*(uint8_t *)(local_rbx + 0x1A)) & (4)) == 0) { a2 = 4; }
    }
    a4 = (uint32_t)(((uint32_t)((uint32_t)(a2))) | (2));
    if (((*(uint8_t *)(local_rbx + 0x1A)) & (2)) != 0) { a4 = (uint32_t)(a2); }
    a2 = (uint32_t)(((uint32_t)((uint32_t)(a4))) | (0xFF00ULL));
    if (((uint32_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xC3)))) <= ((uint32_t)(*(uint8_t *)(local_rbx + 0x1B)))) { a2 = (uint32_t)(a4); }
    result = *(uint8_t *)(local_rbx + 0x1B);
    if ((uint32_t)(a2) != 0) {
        a1 = local_rbx;
        result = ExpApplyPriorityBoost(a1, a2, *(uint64_t *)(gs_base + (0 + 0x188)), a4);
    }
    result = ExpWaitForResource(local_rbx, local_rbp - 73, (uint32_t)(0x10224ULL), a4);
    result = 0;
    *(uint64_t *)(local_rbp - 0x1) = 0;
    *(uint64_t *)(local_rbp - 0x11) = v_xmm0;
    if ((((uint8_t)(*(uint16_t *)(local_rbx + 0x1A))) & (8)) != 0) goto loc_00215586;
    if ((((uint8_t)(*(uint16_t *)(local_rbx + 0x1A))) & (4)) == 0) goto loc_00215484;
    a1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r13 + 0x5A0))) >> (9));
    a1 = (uint32_t)((a1) & (7));
    result = *(uint64_t *)(*(uint64_t *)(local_r13 + 0x220) + 0x2A0);
    if (*(uint64_t *)(*(uint64_t *)(local_r13 + 0x220) + 0x2A0) != 0) {
        result = *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(local_r13 + 0x220) + 0x2A0) + 0x43C);
        if (((uint32_t)(a1)) >= ((uint32_t)(result))) { a1 = (uint32_t)(result); }
    }
    a2 = (uint32_t)((uint32_t)(local_r15));
    if (((uint32_t)(a1)) < 2) { a2 = 4; }
loc_00215484:
    local_r12 = (uint32_t)(((uint32_t)((uint32_t)(a2))) | (2));
    if (((*(uint8_t *)(local_rbx + 0x1A)) & (2)) == 0) { local_r12 = (uint32_t)(a2); }
    if ((uint32_t)(local_r12) == 0) goto loc_00215586;
    *(uint64_t *)(local_rbp - 0x9) = local_rdi;
    *(uint64_t *)(local_rbp - 0x11) = local_r15;
    *(uint64_t *)(local_rbp - 0x69) = *(uint8_t *)(local_rbp - 0x51);
    if ((*(uint32_t *)(v_rip + 0xDB1863)) != ((uint32_t)(local_r15))) goto loc_002156C6;
loc_002154C3:
    *(uint8_t *)(local_rbp - 0x1) = (uint8_t)(*(uint8_t *)(local_rbp - 0x51));
    if (((*(uint8_t *)(v_rip + 0xDB163C)) & (33)) != 0) goto loc_00215655;
loc_002154D3:
    if (local_rbp - 17 != 0) goto loc_0021571C;
loc_002154E3:
    if ((*(uint64_t *)(local_rbx + 0x30)) == local_r13) goto loc_00215515;
    a1 = (*(uint64_t *)(local_rbx + 0x30) != 0) ? 1 : 0;
    a2 = ((uint32_t)(*(uint32_t *)(local_rbx + 0x48))) + ((uint32_t)(*(uint32_t *)(local_rbx + 0x40)));
    if (*(uint64_t *)(local_rbx + 0x10) != 0) goto loc_00215687;
loc_00215512:
loc_00215515:
    if ((((uint8_t)(local_r12)) & (4)) != 0) goto loc_00215735;
loc_0021551F:
    if ((((uint8_t)(local_r12)) & (2)) == 0) goto loc_00215555;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_r15 + 0x8)))) & (4)) != 0) goto loc_0021567E;
    result = (uint32_t)((1) + 1);
    if (((uint32_t)(result)) != 1) goto loc_00215551;
    if ((uint8_t)(*(uint8_t *)(local_r13 + 0x318)) != 0) goto loc_0021577A;
loc_00215551:
loc_00215555:
    result = KeReleaseInStackQueuedSpinLock(local_rbp - 17, a2, (uint32_t)(0x10224ULL), *(uint64_t *)(local_rbx + 0x10));
    if ((uint32_t)(local_r12) == 0) goto loc_00215586;
    if ((((uint8_t)(local_r12)) & (4)) != 0) {
        a3 = 0;
        a1 = local_r13;
        a2 = a3 + 2;
        result = IoBoostThreadIoPriority(a1, a2, a3, *(uint64_t *)(local_rbx + 0x10));
    }
    if ((((uint8_t)(local_r12)) & (2)) != 0) {
        a1 = local_r13;
        result = PsBoostThreadOutstandingIoQoS(a1, a2, a3, *(uint64_t *)(local_rbx + 0x10));
    }
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x44))) == 0) goto loc_00215633;
    *(uint32_t *)(local_rbp - 0x69) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x44)));
    *(uint32_t *)(local_rbp - 0x79) = (uint32_t)(local_r15);
    a2 = (a2) << (32);
    result = ((uint32_t)(*(uint32_t *)(local_rbx + 0x44))) | (a2);
    *(uint8_t *)(local_rbp - 0x76) = (uint8_t)(local_r15);
    *(uint16_t *)(local_rbp - 0x79) = (uint16_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xD0));
    *(uint8_t *)(local_rbp - 0x77) = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xD1));
    result = EtwpGetTrackingLockSlotForThread(local_rbx, (uint32_t)(0x10000ULL), a3, *(uint64_t *)(local_rbx + 0x10));
    if (result == 0) goto loc_00215633;
    *(uint64_t *)(result + 0x8) = result;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x20))) == 0) goto loc_00215679;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x20)))) != 4) goto loc_00215679;
    if ((*(uint16_t *)(result + 0x18)) != ((uint16_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xD0)))) goto loc_00215674;
    if ((*(uint8_t *)(result + 0x1A)) != ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xD1)))) goto loc_00215674;
    local_rdi = (result) - (*(uint64_t *)(result));
    *(uint64_t *)(result) = local_rdi;
loc_00215621:
    *(uint32_t *)(result + 0x18) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbp - 0x79)));
    *(uint32_t *)(result + 0x2C) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbp - 0x69)));
    *(uint32_t *)(result + 0x20) = 1;
    *(uint32_t *)(result + 0x24) = 1;
loc_00215633:
loc_0021563C:
    result = KeReleaseInStackQueuedSpinLock(local_rbp - 97, (uint32_t)(0x10000ULL), a3, *(uint64_t *)(local_rbx + 0x10));
    local_r12 = 0;
loc_00215655:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCF87FD))) != 0) goto loc_002154D3;
    result = KiAcquireQueuedSpinLockInstrumented(local_rbp - 17, local_rdi, a3, *(uint64_t *)(local_rbx + 0x10));
    goto loc_002154E3;
loc_00215674:
    *(uint64_t *)(local_rbp - 0x11) = 1;
    goto loc_00215621;
loc_00215679:
    *(uint64_t *)(local_rbp - 0x11) = local_r15;
    goto loc_00215621;
loc_0021567E:
    local_r12 = (uint32_t)((local_r12) & (0xFFFFFFFDULL));
    goto loc_00215555;
loc_00215687:
    a3 = ((uint32_t)(*(uint32_t *)(local_rdi + 0x8))) << (4);
    a3 = (a3) + (local_rdi);
    local_rdi = (local_rdi) + (16);
    if ((local_rbp - 17) >= local_rdi) goto loc_00215512;
loc_0021569F:
    if ((*(uint64_t *)(local_rdi)) == (*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xD0))) goto loc_002156DA;
    if (*(uint64_t *)(local_rdi) == 0) goto loc_002156B8;
    a1 = (local_rbp - 17) + 1;
    if (a1 == local_rdi) goto loc_00215512;
loc_002156B8:
    local_rdi = (local_rdi) + (16);
    if (local_rdi != a3) goto loc_0021569F;
    goto loc_00215512;
loc_002156C6:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(*(uint64_t *)(local_rdi)), (uint8_t)(a1), a3, *(uint64_t *)(local_rbx + 0x10));
    goto loc_002154C3;
loc_002156DA:
    result = (local_rdi) - (*(uint64_t *)(local_rbx + 0x10));
    result = (result) >> (4);
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x460) = (uint8_t)(result);
    goto loc_00215515;
loc_002156F8:
    if (a3 != (*(uint64_t *)(gs_base + (0 + 0x188)))) goto loc_002153D4;
    if ((*(uint32_t *)(a3 + 0x5E0)) == ((uint32_t)((uint8_t)(a1)))) goto loc_002153D4;
    goto loc_002153D9;
loc_0021571C:
    result = KxWaitForLockOwnerShip(local_rbp - 17, (uint8_t)(a1), a3, *(uint64_t *)(local_rbx + 0x10));
    goto loc_002154E3;
loc_0021572A:
    goto loc_00215394;
loc_00215735:
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x8))))) != 0) goto loc_00215771;
    a4 = 0;
    a3 = 0;
    a2 = 0;
    result = PsBoostThreadIoEx(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xD0), a2, a3, a4);
    goto loc_0021551F;
loc_00215755:
    *(uint64_t *)(local_rbp - 0x41) = *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xD0);
    *(uint64_t *)(local_rbp - 0x49) = result;
    *(uint64_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xD0)) = local_rbp - 73;
    *(uint64_t *)(result + 0x8) = local_rbp - 73;
    goto loc_0021528C;
loc_00215771:
    local_r12 = (uint32_t)((local_r12) & (0xFFFFFFFBULL));
    goto loc_0021551F;
loc_0021577A:
    *(uint64_t *)(local_rbp - 0x69) = 2;
    if ((*(uint32_t *)(v_rip + 0xDB158E)) != ((uint32_t)(local_r15))) goto loc_002157E7;
loc_00215794:
    *(uint64_t *)(local_rbp - 0x79) = *(uint64_t *)(gs_base + (0 + 0x20));
    result = KiAbThreadInsertList(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xD0), *(uint64_t *)(gs_base + (0 + 0x20)) + 37240, *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xD0) + 808, a4);
    if ((uint32_t)(result) != 0) {
        a1 = *(uint64_t *)(local_rbp - 0x79);
        result = KiAbQueueAutoBoostDpc(a1, *(uint64_t *)(gs_base + (0 + 0x20)) + 37240, *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xD0) + 808, a4);
    }
    if ((*(uint32_t *)(v_rip + 0xDB1555)) != ((uint32_t)(local_r15))) {
        a1 = 2;
        a2 = *(uint8_t *)(local_rbp - 0x69);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xD0) + 808, a4);
    }
    goto loc_00215551;
loc_002157E7:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(*(uint8_t *)(local_rbp - 0x69)), (uint8_t)(a1), *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xD0) + 808, a4);
    goto loc_00215794;
loc_00215B1D:
    if ((*(uint32_t *)(result + 0x24)) >= ((uint32_t)(local_rdi))) goto loc_00215269;
    *(uint32_t *)(result + 0x24) = (uint32_t)(local_rdi);
    goto loc_00215269;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00215166&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
