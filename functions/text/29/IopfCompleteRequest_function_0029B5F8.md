# IopfCompleteRequest

- RVA: `0x0029B5F8`–`0x0029BDA3` (길이 `1,963` bytes)
- VA: `0x000000014029B5F8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00067E2C`
- 디코드: `512`개 명령, `1,963/1,963` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **43**; 고유 호출 대상: **30**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x0029B664` → [PoDeviceReleaseIrp](../39/PoDeviceReleaseIrp_function_00391B7C.md) (function, `0x00391B7C`)
- `0x0029B781` → [PoDeviceAcquireIrp](../38/PoDeviceAcquireIrp_function_0038FF88.md) (function, `0x0038FF88`)
- `0x0029B798` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0029B7BA` → [PoDeviceReleaseIrp](../39/PoDeviceReleaseIrp_function_00391B7C.md) (function, `0x00391B7C`)
- `0x0029B80E` → [IoFreeMdl](IoFreeMdl_function_0029EA80.md) (function, `0x0029EA80`)
- `0x0029B81E` → [IoFreeIrp](../24/IoFreeIrp_function_0024DF70.md) (function, `0x0024DF70`)
- `0x0029B83A` → [IofCompleteRequest](IofCompleteRequest_function_0029B5C0.md) (function, `0x0029B5C0`)
- `0x0029B8AF` → [IoGetRelatedDeviceObject](IoGetRelatedDeviceObject_function_0029B120.md) (function, `0x0029B120`)
- `0x0029B8D9` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0029B90D` → [IopFreeIrpExtension](../24/IopFreeIrpExtension_function_0024EDB0.md) (function, `0x0024EDB0`)
- `0x0029B92A` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0029B967` → [IopDequeueIrpFromThread](../20/IopDequeueIrpFromThread_function_00207B20.md) (function, `0x00207B20`)
- `0x0029B97B` → [KeSetEvent](../33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x0029B98C` → [IoFreeIrp](../24/IoFreeIrp_function_0024DF70.md) (function, `0x0024DF70`)
- `0x0029B999` → [IopDequeueIrpFromThread](../20/IopDequeueIrpFromThread_function_00207B20.md) (function, `0x00207B20`)
- `0x0029B9CD` → [KeInitializeApc](../42/KeInitializeApc_function_00428510.md) (function, `0x00428510`)
- `0x0029B9E3` → [KeInsertQueueApc](../20/KeInsertQueueApc_function_00203F10.md) (function, `0x00203F10`)
- `0x0029B9FF` → [MmUnlockPages](MmUnlockPages_function_0029EEE0.md) (function, `0x0029EEE0`)
- `0x0029BA19` → [Feature_3458701627__private_IsEnabledDeviceUsageNoInline](../59/Feature_3458701627__private_IsEnabledDeviceUsageNoInline_function_00597838.md) (function, `0x00597838`)
- `0x0029BA32` → [ObfDereferenceObjectWithTag](../2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x0029BAB3` → [Feature_1565498680__private_IsEnabledDeviceUsageNoInline](../59/Feature_1565498680__private_IsEnabledDeviceUsageNoInline_function_005977E4.md) (function, `0x005977E4`)
- `0x0029BAC3` → [IopDoesCompletionNeedsApc](../3F/IopDoesCompletionNeedsApc_function_003FD094.md) (function, `0x003FD094`)
- `0x0029BAF1` → [IopDoesCompletionNeedsApc](../3F/IopDoesCompletionNeedsApc_function_003FD094.md) (function, `0x003FD094`)
- `0x0029BB02` → [KeAreAllApcsDisabled](../2F/KeAreAllApcsDisabled_function_002F7AC0.md) (function, `0x002F7AC0`)
- `0x0029BB3D` → [IopIoRingCompleteIrp](../3E/IopIoRingCompleteIrp_function_003ED13C.md) (function, `0x003ED13C`)
- `0x0029BB60` → [IopCompleteIrpInFileObjectList](../24/IopCompleteIrpInFileObjectList_function_0024F330.md) (function, `0x0024F330`)
- `0x0029BB80` → [KeAcquireSpinLockRaiseToDpc](../20/KeAcquireSpinLockRaiseToDpc_function_00208470.md) (function, `0x00208470`)
- `0x0029BB8A` → [KeReleaseSpinLock](../39/KeReleaseSpinLock_function_00392BA0.md) (function, `0x00392BA0`)
- `0x0029BBAB` → [KeAreAllApcsDisabled](../2F/KeAreAllApcsDisabled_function_002F7AC0.md) (function, `0x002F7AC0`)
- `0x0029BBE0` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x0029BC02` → [IopCompleteRequest](../20/IopCompleteRequest_function_0020AF50.md) (function, `0x0020AF50`)
- `0x0029BC16` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0029BC59` → [KeInitializeApc](../42/KeInitializeApc_function_00428510.md) (function, `0x00428510`)
- `0x0029BC7A` → [KeAcquireQueuedSpinLock](../27/KeAcquireQueuedSpinLock_function_00273D80.md) (function, `0x00273D80`)
- `0x0029BCEA` → [KeInitializeApc](../42/KeInitializeApc_function_00428510.md) (function, `0x00428510`)
- `0x0029BD01` → [KeInsertQueueApc](../20/KeInsertQueueApc_function_00203F10.md) (function, `0x00203F10`)
- `0x0029BD0B` → [KeReleaseQueuedSpinLock](../27/KeReleaseQueuedSpinLock_function_00272540.md) (function, `0x00272540`)
- `0x0029BD37` → [ObfDereferenceObjectWithTag](../2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x0029BD41` → [KeReleaseQueuedSpinLock](../27/KeReleaseQueuedSpinLock_function_00272540.md) (function, `0x00272540`)
- `0x0029BD4D` → [IopDropIrp](../21/IopDropIrp_function_002107B0.md) (function, `0x002107B0`)
- `0x0029BD52` → [Feature_3458701627__private_IsEnabledDeviceUsageNoInline](../59/Feature_3458701627__private_IsEnabledDeviceUsageNoInline_function_00597838.md) (function, `0x00597838`)
- `0x0029BD6C` → [ObfDereferenceObjectWithTag](../2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x0029BD9D` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)

### Direct callers
- [IofCompleteRequest](IofCompleteRequest_function_0029B5C0.md) at `0x0029B5CE`
- [IopPerfCompleteRequest](../4A/IopPerfCompleteRequest_function_004A69B8.md) at `0x004A6A58`
- [IopPerfCompleteRequest](../4A/IopPerfCompleteRequest_function_004A69B8.md) at `0x004A6B50`
- [IovCompleteRequest](../../pagevrfy/BB/IovCompleteRequest_function_00BB6758.md) at `0x00BB6877`

### Static image references
- `0x0029B9A2` → RVA `0x00298010` (`IopCompletePageWrite`; read)
- `0x0029BBD2` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x0029BC2B` → RVA `0x0071AC40` (`IopAbortRequest`; read)
- `0x0029BC37` → RVA `0x0020AF50` (`IopCompleteRequest`; read)
- `0x0029BC85` → RVA `0x00F8D470` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0029B8D9` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0029B5F8  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
0029B5FD  55                              push rbp
0029B5FE  53                              push rbx
0029B5FF  56                              push rsi
0029B600  57                              push rdi
0029B601  41 54                           push r12
0029B603  41 55                           push r13
0029B605  41 56                           push r14
0029B607  41 57                           push r15
0029B609  48 8B EC                        mov rbp, rsp
0029B60C  48 83 EC 68                     sub rsp, 0x68
0029B610  45 33 C9                        xor r9d, r9d
0029B613  48 8B F1                        mov rsi, rcx
0029B616  8A 49 42                        mov cl, byte ptr [rcx + 0x42]
0029B619  44 8A F2                        mov r14b, dl
0029B61C  45 8B E1                        mov r12d, r9d
0029B61F  4C 89 4D 58                     mov qword ptr [rbp + 0x58], r9
0029B623  4C 89 4D D8                     mov qword ptr [rbp - 0x28], r9
0029B627  44 8A 46 43                     mov r8b, byte ptr [rsi + 0x43]
0029B62B  45 8D 51 01                     lea r10d, [r9 + 1]
0029B62F  41 8D 04 0A                     lea eax, [r10 + rcx]
0029B633  44 3A C0                        cmp r8b, al
0029B636  0F 8F 4E 07 00 00               jg 0x14029bd8a
0029B63C  66 83 3E 06                     cmp word ptr [rsi], 6
0029B640  0F 85 44 07 00 00               jne 0x14029bd8a
0029B646  48 8B 9E B8 00 00 00            mov rbx, qword ptr [rsi + 0xb8]
0029B64D  44 3A C1                        cmp r8b, cl
0029B650  7F 25                           jg 0x14029b677
0029B652  80 3B 16                        cmp byte ptr [rbx], 0x16
0029B655  75 20                           jne 0x14029b677
0029B657  4C 8B 43 28                     mov r8, qword ptr [rbx + 0x28]
0029B65B  48 8B CE                        mov rcx, rsi
0029B65E  8A 53 01                        mov dl, byte ptr [rbx + 1]
0029B661  45 8A EA                        mov r13b, r10b
0029B664  E8 13 65 0F 00                  call 0x140391b7c
0029B669  48 8B 75 48                     mov rsi, qword ptr [rbp + 0x48]
0029B66D  45 8D 54 24 01                  lea r10d, [r12 + 1]
0029B672  45 33 C9                        xor r9d, r9d
0029B675  EB 03                           jmp 0x14029b67a
0029B677  45 8A E9                        mov r13b, r9b
0029B67A  F6 86 D3 00 00 00 02            test byte ptr [rsi + 0xd3], 2
0029B681  74 09                           je 0x14029b68c
0029B683  44 8B BE F0 00 00 00            mov r15d, dword ptr [rsi + 0xf0]
0029B68A  EB 03                           jmp 0x14029b68f
0029B68C  45 8B F9                        mov r15d, r9d
0029B68F  44 00 56 43                     add byte ptr [rsi + 0x43], r10b
0029B693  48 8B 45 48                     mov rax, qword ptr [rbp + 0x48]
0029B697  48 83 80 B8 00 00 00 48         add qword ptr [rax + 0xb8], 0x48
0029B69F  48 8B 7D 48                     mov rdi, qword ptr [rbp + 0x48]
0029B6A3  8A 47 42                        mov al, byte ptr [rdi + 0x42]
0029B6A6  41 02 C2                        add al, r10b
0029B6A9  38 47 43                        cmp byte ptr [rdi + 0x43], al
0029B6AC  0F 8F 45 01 00 00               jg 0x14029b7f7
0029B6B2  48 83 C3 03                     add rbx, 3
0029B6B6  8A 03                           mov al, byte ptr [rbx]
0029B6B8  41 22 C2                        and al, r10b
0029B6BB  88 47 41                        mov byte ptr [rdi + 0x41], al
0029B6BE  48 8B 4D 48                     mov rcx, qword ptr [rbp + 0x48]
0029B6C2  48 63 41 30                     movsxd rax, dword ptr [rcx + 0x30]
0029B6C6  85 C0                           test eax, eax
0029B6C8  79 1D                           jns 0x14029b6e7
0029B6CA  41 3B C7                        cmp eax, r15d
0029B6CD  74 18                           je 0x14029b6e7
0029B6CF  80 0B 02                        or byte ptr [rbx], 2
0029B6D2  4C 8B F8                        mov r15, rax
0029B6D5  80 8E D3 00 00 00 02            or byte ptr [rsi + 0xd3], 2
0029B6DC  48 89 86 F0 00 00 00            mov qword ptr [rsi + 0xf0], rax
0029B6E3  48 8B 4D 48                     mov rcx, qword ptr [rbp + 0x48]
0029B6E7  8A 13                           mov dl, byte ptr [rbx]
0029B6E9  8A C2                           mov al, dl
0029B6EB  44 39 49 30                     cmp dword ptr [rcx + 0x30], r9d
0029B6EF  7C 36                           jl 0x14029b727
0029B6F1  F6 C2 40                        test dl, 0x40
0029B6F4  74 35                           je 0x14029b72b
0029B6F6  44 8A 63 FE                     mov r12b, byte ptr [rbx - 2]
0029B6FA  24 02                           and al, 2
0029B6FC  66 83 63 FE 00                  and word ptr [rbx - 2], 0
0029B701  88 03                           mov byte ptr [rbx], al
0029B703  4C 89 4B 05                     mov qword ptr [rbx + 5], r9
0029B707  4C 89 4B 0D                     mov qword ptr [rbx + 0xd], r9
0029B70B  4C 89 4B 15                     mov qword ptr [rbx + 0x15], r9
0029B70F  4C 89 4B 2D                     mov qword ptr [rbx + 0x2d], r9
0029B713  48 8B 4D 48                     mov rcx, qword ptr [rbp + 0x48]
0029B717  8A 41 42                        mov al, byte ptr [rcx + 0x42]
0029B71A  41 02 C2                        add al, r10b
0029B71D  38 41 43                        cmp byte ptr [rcx + 0x43], al
0029B720  75 49                           jne 0x14029b76b
0029B722  49 8B F9                        mov rdi, r9
0029B725  EB 4F                           jmp 0x14029b776
0029B727  84 D2                           test dl, dl
0029B729  78 CB                           js 0x14029b6f6
0029B72B  44 38 49 44                     cmp byte ptr [rcx + 0x44], r9b
0029B72F  74 07                           je 0x14029b738
0029B731  8A C2                           mov al, dl
0029B733  F6 C2 20                        test dl, 0x20
0029B736  75 BE                           jne 0x14029b6f6
0029B738  44 38 49 41                     cmp byte ptr [rcx + 0x41], r9b
0029B73C  74 13                           je 0x14029b751
0029B73E  8A 41 42                        mov al, byte ptr [rcx + 0x42]
0029B741  38 41 43                        cmp byte ptr [rcx + 0x43], al
0029B744  7F 0B                           jg 0x14029b751
0029B746  48 8B 81 B8 00 00 00            mov rax, qword ptr [rcx + 0xb8]
0029B74D  44 08 50 03                     or byte ptr [rax + 3], r10b
0029B751  66 83 63 FE 00                  and word ptr [rbx - 2], 0
0029B756  80 23 02                        and byte ptr [rbx], 2
0029B759  4C 89 4B 05                     mov qword ptr [rbx + 5], r9
0029B75D  4C 89 4B 0D                     mov qword ptr [rbx + 0xd], r9
0029B761  4C 89 4B 15                     mov qword ptr [rbx + 0x15], r9
0029B765  4C 89 4B 2D                     mov qword ptr [rbx + 0x2d], r9
0029B769  EB 5D                           jmp 0x14029b7c8
0029B76B  48 8B 81 B8 00 00 00            mov rax, qword ptr [rcx + 0xb8]
0029B772  48 8B 78 28                     mov rdi, qword ptr [rax + 0x28]
0029B776  45 84 ED                        test r13b, r13b
0029B779  74 0F                           je 0x14029b78a
0029B77B  4C 8B C7                        mov r8, rdi
0029B77E  41 8A D4                        mov dl, r12b
0029B781  E8 02 48 0F 00                  call 0x14038ff88
0029B786  48 8B 4D 48                     mov rcx, qword ptr [rbp + 0x48]
0029B78A  48 8B 43 35                     mov rax, qword ptr [rbx + 0x35]
0029B78E  48 8B D1                        mov rdx, rcx
0029B791  4C 8B 43 3D                     mov r8, qword ptr [rbx + 0x3d]
0029B795  48 8B CF                        mov rcx, rdi
0029B798  E8 33 F3 41 00                  call 0x1406baad0
0029B79D  3D 16 00 00 C0                  cmp eax, 0xc0000016
0029B7A2  0F 84 AA 05 00 00               je 0x14029bd52
0029B7A8  45 33 C9                        xor r9d, r9d
0029B7AB  45 84 ED                        test r13b, r13b
0029B7AE  74 12                           je 0x14029b7c2
0029B7B0  48 8B 4D 48                     mov rcx, qword ptr [rbp + 0x48]
0029B7B4  4C 8B C7                        mov r8, rdi
0029B7B7  41 8A D4                        mov dl, r12b
0029B7BA  E8 BD 63 0F 00                  call 0x140391b7c
0029B7BF  45 33 C9                        xor r9d, r9d
0029B7C2  41 BA 01 00 00 00               mov r10d, 1
0029B7C8  48 8B 45 48                     mov rax, qword ptr [rbp + 0x48]
0029B7CC  48 83 C3 48                     add rbx, 0x48
0029B7D0  44 00 50 43                     add byte ptr [rax + 0x43], r10b
0029B7D4  48 8B 45 48                     mov rax, qword ptr [rbp + 0x48]
0029B7D8  48 83 80 B8 00 00 00 48         add qword ptr [rax + 0xb8], 0x48
0029B7E0  48 8B 7D 48                     mov rdi, qword ptr [rbp + 0x48]
0029B7E4  8A 47 42                        mov al, byte ptr [rdi + 0x42]
0029B7E7  41 02 C2                        add al, r10b
0029B7EA  38 47 43                        cmp byte ptr [rdi + 0x43], al
0029B7ED  0F 8E C3 FE FF FF               jle 0x14029b6b6
0029B7F3  4C 8B 65 58                     mov r12, qword ptr [rbp + 0x58]
0029B7F7  8B 47 10                        mov eax, dword ptr [rdi + 0x10]
0029B7FA  A8 08                           test al, 8
0029B7FC  74 46                           je 0x14029b844
0029B7FE  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
0029B802  48 8B 77 18                     mov rsi, qword ptr [rdi + 0x18]
0029B806  48 85 C9                        test rcx, rcx
0029B809  74 10                           je 0x14029b81b
0029B80B  48 8B 19                        mov rbx, qword ptr [rcx]
0029B80E  E8 6D 32 00 00                  call 0x14029ea80
0029B813  48 8B CB                        mov rcx, rbx
0029B816  48 85 DB                        test rbx, rbx
0029B819  75 F0                           jne 0x14029b80b
0029B81B  48 8B CF                        mov rcx, rdi
0029B81E  E8 4D 27 FB FF                  call 0x14024df70
0029B823  83 C8 FF                        or eax, 0xffffffff
0029B826  F0 0F C1 46 18                  lock xadd dword ptr [rsi + 0x18], eax
0029B82B  83 F8 01                        cmp eax, 1
0029B82E  0F 85 1E 05 00 00               jne 0x14029bd52
0029B834  41 8A D6                        mov dl, r14b
0029B837  48 8B CE                        mov rcx, rsi
0029B83A  E8 81 FD FF FF                  call 0x14029b5c0
0029B83F  E9 0E 05 00 00                  jmp 0x14029bd52
0029B844  BE 04 01 00 00                  mov esi, 0x104
0029B849  48 B9 FD FF FF 5F FF FF FF FF   movabs rcx, 0xffffffff5ffffffd
0029B853  BA 01 02 40 00                  mov edx, 0x400201
0029B858  39 77 30                        cmp dword ptr [rdi + 0x30], esi
0029B85B  75 38                           jne 0x14029b895
0029B85D  48 8B 47 38                     mov rax, qword ptr [rdi + 0x38]
0029B861  48 83 F8 02                     cmp rax, 2
0029B865  76 2E                           jbe 0x14029b895
0029B867  48 03 C8                        add rcx, rax
0029B86A  48 83 F9 16                     cmp rcx, 0x16
0029B86E  77 1A                           ja 0x14029b88a
0029B870  48 0F A3 CA                     bt rdx, rcx
0029B874  73 14                           jae 0x14029b88a
0029B876  4C 8B A7 A0 00 00 00            mov r12, qword ptr [rdi + 0xa0]
0029B87D  4C 89 65 58                     mov qword ptr [rbp + 0x58], r12
0029B881  4C 89 8F A0 00 00 00            mov qword ptr [rdi + 0xa0], r9
0029B888  EB 07                           jmp 0x14029b891
0029B88A  C7 47 30 79 02 00 C0            mov dword ptr [rdi + 0x30], 0xc0000279
0029B891  48 8B 7D 48                     mov rdi, qword ptr [rbp + 0x48]
0029B895  45 84 F6                        test r14b, r14b
0029B898  75 2B                           jne 0x14029b8c5
0029B89A  48 8B 8F C0 00 00 00            mov rcx, qword ptr [rdi + 0xc0]
0029B8A1  48 85 C9                        test rcx, rcx
0029B8A4  74 1F                           je 0x14029b8c5
0029B8A6  F7 47 10 00 04 00 00            test dword ptr [rdi + 0x10], 0x400
0029B8AD  75 16                           jne 0x14029b8c5
0029B8AF  E8 6C F8 FF FF                  call 0x14029b120
0029B8B4  8B 48 48                        mov ecx, dword ptr [rax + 0x48]
0029B8B7  83 F9 08                        cmp ecx, 8
0029B8BA  74 36                           je 0x14029b8f2
0029B8BC  83 F9 14                        cmp ecx, 0x14
0029B8BF  74 31                           je 0x14029b8f2
0029B8C1  48 8B 7D 48                     mov rdi, qword ptr [rbp + 0x48]
0029B8C5  41 BD 01 00 00 00               mov r13d, 1
0029B8CB  48 8B 8F A0 00 00 00            mov rcx, qword ptr [rdi + 0xa0]
0029B8D2  48 85 C9                        test rcx, rcx
0029B8D5  74 2A                           je 0x14029b901
0029B8D7  33 D2                           xor edx, edx
0029B8D9  E8 92 6F 8E 00                  call 0x140b82870
0029B8DE  48 8B 45 48                     mov rax, qword ptr [rbp + 0x48]
0029B8E2  45 33 FF                        xor r15d, r15d
0029B8E5  4C 89 B8 A0 00 00 00            mov qword ptr [rax + 0xa0], r15
0029B8EC  48 8B 7D 48                     mov rdi, qword ptr [rbp + 0x48]
0029B8F0  EB 12                           jmp 0x14029b904
0029B8F2  48 8B 7D 48                     mov rdi, qword ptr [rbp + 0x48]
0029B8F6  41 BD 01 00 00 00               mov r13d, 1
0029B8FC  45 8A F5                        mov r14b, r13b
0029B8FF  EB CA                           jmp 0x14029b8cb
0029B901  45 33 FF                        xor r15d, r15d
0029B904  45 8A C5                        mov r8b, r13b
0029B907  83 CA FF                        or edx, 0xffffffff
0029B90A  48 8B CF                        mov rcx, rdi
0029B90D  E8 9E 34 FB FF                  call 0x14024edb0
0029B912  48 85 C0                        test rax, rax
0029B915  74 20                           je 0x14029b937
0029B917  48 8B 55 48                     mov rdx, qword ptr [rbp + 0x48]
0029B91B  48 8D 4D 48                     lea rcx, [rbp + 0x48]
0029B91F  45 0F B6 C6                     movzx r8d, r14b
0029B923  48 8B 92 C0 00 00 00            mov rdx, qword ptr [rdx + 0xc0]
0029B92A  E8 A1 F1 41 00                  call 0x1406baad0
0029B92F  84 C0                           test al, al
0029B931  0F 85 1B 04 00 00               jne 0x14029bd52
0029B937  48 8B 5D 48                     mov rbx, qword ptr [rbp + 0x48]
0029B93B  8B 7B 10                        mov edi, dword ptr [rbx + 0x10]
0029B93E  F7 C7 02 04 00 00               test edi, 0x402
0029B944  0F 84 A3 00 00 00               je 0x14029b9ed
0029B94A  F7 C7 40 04 00 00               test edi, 0x440
0029B950  74 44                           je 0x14029b996
0029B952  48 8B 43 48                     mov rax, qword ptr [rbx + 0x48]
0029B956  0F 10 43 30                     movups xmm0, xmmword ptr [rbx + 0x30]
0029B95A  F3 0F 7F 00                     movdqu xmmword ptr [rax], xmm0
0029B95E  83 E7 42                        and edi, 0x42
0029B961  74 09                           je 0x14029b96c
0029B963  48 8B 4D 48                     mov rcx, qword ptr [rbp + 0x48]
0029B967  E8 B4 C1 F6 FF                  call 0x140207b20
0029B96C  48 8B 4D 48                     mov rcx, qword ptr [rbp + 0x48]
0029B970  45 33 C0                        xor r8d, r8d
0029B973  41 0F B6 D6                     movzx edx, r14b
0029B977  48 8B 49 50                     mov rcx, qword ptr [rcx + 0x50]
0029B97B  E8 90 39 0A 00                  call 0x14033f310
0029B980  85 FF                           test edi, edi
0029B982  0F 84 CA 03 00 00               je 0x14029bd52
0029B988  48 8B 4D 48                     mov rcx, qword ptr [rbp + 0x48]
0029B98C  E8 DF 25 FB FF                  call 0x14024df70
0029B991  E9 BC 03 00 00                  jmp 0x14029bd52
0029B996  48 8B CB                        mov rcx, rbx
0029B999  E8 82 C1 F6 FF                  call 0x140207b20
0029B99E  48 8B 55 48                     mov rdx, qword ptr [rbp + 0x48]
0029B9A2  4C 8D 0D 67 C6 FF FF            lea r9, [rip - 0x3999]
0029B9A9  4C 89 7C 24 38                  mov qword ptr [rsp + 0x38], r15
0029B9AE  44 88 7C 24 30                  mov byte ptr [rsp + 0x30], r15b
0029B9B3  4C 89 7C 24 28                  mov qword ptr [rsp + 0x28], r15
0029B9B8  44 0F BE 42 46                  movsx r8d, byte ptr [rdx + 0x46]
0029B9BD  48 8D 4A 78                     lea rcx, [rdx + 0x78]
0029B9C1  48 8B 92 98 00 00 00            mov rdx, qword ptr [rdx + 0x98]
0029B9C8  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
0029B9CD  E8 3E CB 18 00                  call 0x140428510
0029B9D2  48 8B 4D 48                     mov rcx, qword ptr [rbp + 0x48]
0029B9D6  45 33 C0                        xor r8d, r8d
0029B9D9  48 83 C1 78                     add rcx, 0x78
0029B9DD  33 D2                           xor edx, edx
0029B9DF  45 0F B6 CE                     movzx r9d, r14b
0029B9E3  E8 28 85 F6 FF                  call 0x140203f10
0029B9E8  E9 65 03 00 00                  jmp 0x14029bd52
0029B9ED  48 8B 7B 08                     mov rdi, qword ptr [rbx + 8]
0029B9F1  48 85 FF                        test rdi, rdi
0029B9F4  74 1A                           je 0x14029ba10
0029B9F6  F6 47 0A 02                     test byte ptr [rdi + 0xa], 2
0029B9FA  74 08                           je 0x14029ba04
0029B9FC  48 8B CF                        mov rcx, rdi
0029B9FF  E8 DC 34 00 00                  call 0x14029eee0
0029BA04  48 8B 3F                        mov rdi, qword ptr [rdi]
0029BA07  48 85 FF                        test rdi, rdi
0029BA0A  75 EA                           jne 0x14029b9f6
0029BA0C  48 8B 5D 48                     mov rbx, qword ptr [rbp + 0x48]
0029BA10  F7 43 10 00 20 00 00            test dword ptr [rbx + 0x10], 0x2000
0029BA17  74 33                           je 0x14029ba4c
0029BA19  E8 1A BE 2F 00                  call 0x140597838
0029BA1E  85 C0                           test eax, eax
0029BA20  75 1B                           jne 0x14029ba3d
0029BA22  48 8B 4D 48                     mov rcx, qword ptr [rbp + 0x48]
0029BA26  BA 44 66 6C 74                  mov edx, 0x746c6644
0029BA2B  48 8B 89 98 00 00 00            mov rcx, qword ptr [rcx + 0x98]
0029BA32  E8 A9 BE 05 00                  call 0x1402f78e0
0029BA37  48 8B 5D 48                     mov rbx, qword ptr [rbp + 0x48]
0029BA3B  EB 0F                           jmp 0x14029ba4c
0029BA3D  48 8B 5D 48                     mov rbx, qword ptr [rbp + 0x48]
0029BA41  48 8B 83 98 00 00 00            mov rax, qword ptr [rbx + 0x98]
0029BA48  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
0029BA4C  8B 43 10                        mov eax, dword ptr [rbx + 0x10]
0029BA4F  0F BA E0 0B                     bt eax, 0xb
0029BA53  73 42                           jae 0x14029ba97
0029BA55  44 38 7B 41                     cmp byte ptr [rbx + 0x41], r15b
0029BA59  75 3C                           jne 0x14029ba97
0029BA5B  39 73 30                        cmp dword ptr [rbx + 0x30], esi
0029BA5E  0F 85 EE 02 00 00               jne 0x14029bd52
0029BA64  48 B9 FD FF FF 5F FF FF FF FF   movabs rcx, 0xffffffff5ffffffd
0029BA6E  48 03 4B 38                     add rcx, qword ptr [rbx + 0x38]
0029BA72  48 83 F9 16                     cmp rcx, 0x16
0029BA76  0F 87 D6 02 00 00               ja 0x14029bd52
0029BA7C  B8 01 02 40 00                  mov eax, 0x400201
0029BA81  48 0F A3 C8                     bt rax, rcx
0029BA85  0F 83 C7 02 00 00               jae 0x14029bd52
0029BA8B  4C 89 A3 A0 00 00 00            mov qword ptr [rbx + 0xa0], r12
0029BA92  E9 BB 02 00 00                  jmp 0x14029bd52
0029BA97  48 8B BB C0 00 00 00            mov rdi, qword ptr [rbx + 0xc0]
0029BA9E  48 8B B3 98 00 00 00            mov rsi, qword ptr [rbx + 0x98]
0029BAA5  48 89 7D 60                     mov qword ptr [rbp + 0x60], rdi
0029BAA9  0F BA E0 15                     bt eax, 0x15
0029BAAD  0F 83 9E 00 00 00               jae 0x14029bb51
0029BAB3  E8 2C BD 2F 00                  call 0x1405977e4
0029BAB8  48 8B 5D 48                     mov rbx, qword ptr [rbp + 0x48]
0029BABC  85 C0                           test eax, eax
0029BABE  75 25                           jne 0x14029bae5
0029BAC0  48 8B CB                        mov rcx, rbx
0029BAC3  E8 CC 15 16 00                  call 0x1403fd094
0029BAC8  84 C0                           test al, al
0029BACA  0F 85 A1 00 00 00               jne 0x14029bb71
0029BAD0  44 38 7B 44                     cmp byte ptr [rbx + 0x44], r15b
0029BAD4  74 5D                           je 0x14029bb33
0029BAD6  F7 43 10 00 20 00 00            test dword ptr [rbx + 0x10], 0x2000
0029BADD  0F 84 8E 00 00 00               je 0x14029bb71
0029BAE3  EB 4E                           jmp 0x14029bb33
0029BAE5  F7 43 10 00 20 00 00            test dword ptr [rbx + 0x10], 0x2000
0029BAEC  74 0E                           je 0x14029bafc
0029BAEE  48 8B CB                        mov rcx, rbx
0029BAF1  E8 9E 15 16 00                  call 0x1403fd094
0029BAF6  84 C0                           test al, al
0029BAF8  75 77                           jne 0x14029bb71
0029BAFA  EB 37                           jmp 0x14029bb33
0029BAFC  44 38 7B 44                     cmp byte ptr [rbx + 0x44], r15b
0029BB00  75 6F                           jne 0x14029bb71
0029BB02  E8 B9 BF 05 00                  call 0x1402f7ac0
0029BB07  84 C0                           test al, al
0029BB09  75 62                           jne 0x14029bb6d
0029BB0B  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0029BB14  44 38 A8 4A 02 00 00            cmp byte ptr [rax + 0x24a], r13b
0029BB1B  74 2A                           je 0x14029bb47
0029BB1D  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0029BB26  48 3B F0                        cmp rsi, rax
0029BB29  75 1C                           jne 0x14029bb47
0029BB2B  48 8B 5D 48                     mov rbx, qword ptr [rbp + 0x48]
0029BB2F  48 8B 7D 60                     mov rdi, qword ptr [rbp + 0x60]
0029BB33  45 0F B6 C6                     movzx r8d, r14b
0029BB37  48 8B D7                        mov rdx, rdi
0029BB3A  48 8B CB                        mov rcx, rbx
0029BB3D  E8 FA 15 15 00                  call 0x1403ed13c
0029BB42  E9 0B 02 00 00                  jmp 0x14029bd52
0029BB47  48 8B 7D 60                     mov rdi, qword ptr [rbp + 0x60]
0029BB4B  4C 8B 65 58                     mov r12, qword ptr [rbp + 0x58]
0029BB4F  EB 1C                           jmp 0x14029bb6d
0029BB51  0F BA E0 0D                     bt eax, 0xd
0029BB55  73 1A                           jae 0x14029bb71
0029BB57  45 8A C6                        mov r8b, r14b
0029BB5A  48 8B D7                        mov rdx, rdi
0029BB5D  48 8B CB                        mov rcx, rbx
0029BB60  E8 CB 37 FB FF                  call 0x14024f330
0029BB65  84 C0                           test al, al
0029BB67  0F 85 E5 01 00 00               jne 0x14029bd52
0029BB6D  48 8B 5D 48                     mov rbx, qword ptr [rbp + 0x48]
0029BB71  48 85 F6                        test rsi, rsi
0029BB74  74 1D                           je 0x14029bb93
0029BB76  48 8D 9E 18 06 00 00            lea rbx, [rsi + 0x618]
0029BB7D  48 8B CB                        mov rcx, rbx
0029BB80  E8 EB C8 F6 FF                  call 0x140208470
0029BB85  8A D0                           mov dl, al
0029BB87  48 8B CB                        mov rcx, rbx
0029BB8A  E8 11 70 0F 00                  call 0x140392ba0
0029BB8F  48 8B 5D 48                     mov rbx, qword ptr [rbp + 0x48]
0029BB93  44 38 7B 44                     cmp byte ptr [rbx + 0x44], r15b
0029BB97  0F 85 D6 00 00 00               jne 0x14029bc73
0029BB9D  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0029BBA6  48 3B F0                        cmp rsi, rax
0029BBA9  75 7C                           jne 0x14029bc27
0029BBAB  E8 10 BF 05 00                  call 0x1402f7ac0
0029BBB0  84 C0                           test al, al
0029BBB2  75 73                           jne 0x14029bc27
0029BBB4  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0029BBBD  44 38 A8 4A 02 00 00            cmp byte ptr [rax + 0x24a], r13b
0029BBC4  74 61                           je 0x14029bc27
0029BBC6  4C 89 6D E0                     mov qword ptr [rbp - 0x20], r13
0029BBCA  44 0F 20 C3                     mov rbx, cr8
0029BBCE  45 0F 22 C5                     mov cr8, r13
0029BBD2  44 39 3D 47 B1 D2 00            cmp dword ptr [rip + 0xd2b147], r15d
0029BBD9  74 0A                           je 0x14029bbe5
0029BBDB  41 8A D5                        mov dl, r13b
0029BBDE  8A CB                           mov cl, bl
0029BBE0  E8 17 9B 25 00                  call 0x1404f56fc
0029BBE5  48 8B 4D 48                     mov rcx, qword ptr [rbp + 0x48]
0029BBE9  48 8D 45 58                     lea rax, [rbp + 0x58]
0029BBED  48 83 C1 78                     add rcx, 0x78
0029BBF1  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0029BBF6  4C 8D 4D 60                     lea r9, [rbp + 0x60]
0029BBFA  4C 8D 45 E0                     lea r8, [rbp - 0x20]
0029BBFE  48 8D 55 E8                     lea rdx, [rbp - 0x18]
0029BC02  E8 49 F3 F6 FF                  call 0x14020af50
0029BC07  44 39 3D 12 B1 D2 00            cmp dword ptr [rip + 0xd2b112], r15d
0029BC0E  74 0B                           je 0x14029bc1b
0029BC10  44 0F 20 C1                     mov rcx, cr8
0029BC14  8A D3                           mov dl, bl
0029BC16  E8 7D 9A 25 00                  call 0x1404f5698
0029BC1B  0F B6 C3                        movzx eax, bl
0029BC1E  44 0F 22 C0                     mov cr8, rax
0029BC22  E9 2B 01 00 00                  jmp 0x14029bd52
0029BC27  48 8B 4D 48                     mov rcx, qword ptr [rbp + 0x48]
0029BC2B  48 8D 05 0E F0 47 00            lea rax, [rip + 0x47f00e]
0029BC32  4C 89 7C 24 38                  mov qword ptr [rsp + 0x38], r15
0029BC37  4C 8D 0D 12 F3 F6 FF            lea r9, [rip - 0x90cee]
0029BC3E  44 88 7C 24 30                  mov byte ptr [rsp + 0x30], r15b
0029BC43  48 8B D6                        mov rdx, rsi
0029BC46  4C 89 7C 24 28                  mov qword ptr [rsp + 0x28], r15
0029BC4B  44 0F BE 41 46                  movsx r8d, byte ptr [rcx + 0x46]
0029BC50  48 83 C1 78                     add rcx, 0x78
0029BC54  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0029BC59  E8 B2 C8 18 00                  call 0x140428510
0029BC5E  48 8B 4D 48                     mov rcx, qword ptr [rbp + 0x48]
0029BC62  4C 8B 45 58                     mov r8, qword ptr [rbp + 0x58]
0029BC66  48 83 C1 78                     add rcx, 0x78
0029BC6A  48 8B 55 60                     mov rdx, qword ptr [rbp + 0x60]
0029BC6E  E9 6C FD FF FF                  jmp 0x14029b9df
0029BC73  BE 0B 00 00 00                  mov esi, 0xb
0029BC78  8B CE                           mov ecx, esi
0029BC7A  E8 01 81 FD FF                  call 0x140273d80
0029BC7F  4C 8B 4D 48                     mov r9, qword ptr [rbp + 0x48]
0029BC83  8A D8                           mov bl, al
0029BC85  48 8B 15 E4 17 CF 00            mov rdx, qword ptr [rip + 0xcf17e4]
0029BC8C  48 8D 05 DD 17 CF 00            lea rax, [rip + 0xcf17dd]
0029BC93  4D 8B 91 98 00 00 00            mov r10, qword ptr [r9 + 0x98]
0029BC9A  48 3B D0                        cmp rdx, rax
0029BC9D  74 14                           je 0x14029bcb3
0029BC9F  4C 8B 02                        mov r8, qword ptr [rdx]
0029BCA2  48 8D 4A E0                     lea rcx, [rdx - 0x20]
0029BCA6  49 3B C9                        cmp rcx, r9
0029BCA9  74 67                           je 0x14029bd12
0029BCAB  49 8B D0                        mov rdx, r8
0029BCAE  4C 3B C0                        cmp r8, rax
0029BCB1  75 EC                           jne 0x14029bc9f
0029BCB3  4D 85 D2                        test r10, r10
0029BCB6  0F 84 80 00 00 00               je 0x14029bd3c
0029BCBC  45 0F BE 41 46                  movsx r8d, byte ptr [r9 + 0x46]
0029BCC1  49 8D 49 78                     lea rcx, [r9 + 0x78]
0029BCC5  4C 89 7C 24 38                  mov qword ptr [rsp + 0x38], r15
0029BCCA  48 8D 05 6F EF 47 00            lea rax, [rip + 0x47ef6f]
0029BCD1  44 88 7C 24 30                  mov byte ptr [rsp + 0x30], r15b
0029BCD6  4C 8D 0D 73 F2 F6 FF            lea r9, [rip - 0x90d8d]
0029BCDD  4C 89 7C 24 28                  mov qword ptr [rsp + 0x28], r15
0029BCE2  49 8B D2                        mov rdx, r10
0029BCE5  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0029BCEA  E8 21 C8 18 00                  call 0x140428510
0029BCEF  48 8B 4D 48                     mov rcx, qword ptr [rbp + 0x48]
0029BCF3  4D 8B C4                        mov r8, r12
0029BCF6  48 83 C1 78                     add rcx, 0x78
0029BCFA  45 0F B6 CE                     movzx r9d, r14b
0029BCFE  48 8B D7                        mov rdx, rdi
0029BD01  E8 0A 82 F6 FF                  call 0x140203f10
0029BD06  8A D3                           mov dl, bl
0029BD08  48 8B CE                        mov rcx, rsi
0029BD0B  E8 30 68 FD FF                  call 0x140272540
0029BD10  EB 40                           jmp 0x14029bd52
0029BD12  49 39 50 08                     cmp qword ptr [r8 + 8], rdx
0029BD16  75 6B                           jne 0x14029bd83
0029BD18  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
0029BD1C  48 39 10                        cmp qword ptr [rax], rdx
0029BD1F  75 62                           jne 0x14029bd83
0029BD21  4C 89 00                        mov qword ptr [rax], r8
0029BD24  49 8B CA                        mov rcx, r10
0029BD27  49 89 40 08                     mov qword ptr [r8 + 8], rax
0029BD2B  48 89 52 08                     mov qword ptr [rdx + 8], rdx
0029BD2F  48 89 12                        mov qword ptr [rdx], rdx
0029BD32  BA 44 66 6C 74                  mov edx, 0x746c6644
0029BD37  E8 A4 BB 05 00                  call 0x1402f78e0
0029BD3C  8A D3                           mov dl, bl
0029BD3E  48 8B CE                        mov rcx, rsi
0029BD41  E8 FA 67 FD FF                  call 0x140272540
0029BD46  48 8B 4D 48                     mov rcx, qword ptr [rbp + 0x48]
0029BD4A  48 8B D7                        mov rdx, rdi
0029BD4D  E8 5E 4A F7 FF                  call 0x1402107b0
0029BD52  E8 E1 BA 2F 00                  call 0x140597838
0029BD57  85 C0                           test eax, eax
0029BD59  74 16                           je 0x14029bd71
0029BD5B  48 8B 45 D8                     mov rax, qword ptr [rbp - 0x28]
0029BD5F  48 85 C0                        test rax, rax
0029BD62  74 0D                           je 0x14029bd71
0029BD64  BA 44 66 6C 74                  mov edx, 0x746c6644
0029BD69  48 8B C8                        mov rcx, rax
0029BD6C  E8 6F BB 05 00                  call 0x1402f78e0
0029BD71  48 83 C4 68                     add rsp, 0x68
0029BD75  41 5F                           pop r15
0029BD77  41 5E                           pop r14
0029BD79  41 5D                           pop r13
0029BD7B  41 5C                           pop r12
0029BD7D  5F                              pop rdi
0029BD7E  5E                              pop rsi
0029BD7F  5B                              pop rbx
0029BD80  5D                              pop rbp
0029BD81  C3                              ret
0029BD82  CC                              int3
0029BD83  B9 03 00 00 00                  mov ecx, 3
0029BD88  CD 29                           int 0x29
0029BD8A  41 B8 15 13 00 00               mov r8d, 0x1315
0029BD90  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
0029BD95  48 8B D6                        mov rdx, rsi
0029BD98  B9 44 00 00 00                  mov ecx, 0x44
0029BD9D  E8 BE 18 26 00                  call 0x1404fd660
0029BDA2  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopfCompleteRequest(__int64 a1, unsigned __int8 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int8 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (104);
    a4 = 0;
    v_stack_p18 = 0;
    v_stack_m68 = 0;
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 67))) > ((unsigned __int8)(a4 + 1 + *(unsigned __int8 *)(a1 + 66) * 1))) goto loc_0029BD8A;
    if ((*(unsigned __int16 *)(a1)) != 6) goto loc_0029BD8A;
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 67))) > ((unsigned __int8)(*(unsigned __int8 *)(a1 + 66)))) goto loc_0029B677;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 184))) != 22) goto loc_0029B677;
    result = PoDeviceReleaseIrp(a1, *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 184) + 1), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184) + 40), a4);
    a4 = 0;
    goto loc_0029B67A;
loc_0029B677:
loc_0029B67A:
    if (((*(unsigned __int8 *)(v_stack_p8 + 211)) & (2)) == 0) goto loc_0029B68C;
    goto loc_0029B68F;
loc_0029B68C:
loc_0029B68F:
    result = (unsigned __int8)((*(unsigned __int8 *)(v_stack_p8 + 66)) + ((unsigned __int8)(0 + 1)));
    if ((*(unsigned __int8 *)(v_stack_p8 + 67)) > ((unsigned __int8)(result))) goto loc_0029B7F7;
    v_rbx = (*(unsigned __int64 *)(a1 + 184)) + (3);
loc_0029B6B6:
    result = (unsigned __int8)((*(unsigned __int8 *)(v_rbx)) & ((unsigned __int8)(0 + 1)));
    *(unsigned __int8 *)(v_stack_p8 + 65) = (unsigned __int8)(result);
    if (!sign_flag) goto loc_0029B6E7;
    v_r15 = 0;
    if (((unsigned int)((int)(*(unsigned int *)(v_stack_p8 + 48)))) != 0) {
        v_r15 = (int)(*(unsigned int *)(v_stack_p8 + 48));
        *(unsigned __int64 *)(v_stack_p8 + 240) = (int)(*(unsigned int *)(v_stack_p8 + 48));
        a1 = v_stack_p8;
    }
    if ((*(unsigned int *)(a1 + 48)) < 0) goto loc_0029B727;
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_rbx))) & (64)) == 0) goto loc_0029B72B;
loc_0029B6F6:
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(v_rbx))) & (2));
    *(unsigned __int8 *)(v_rbx) = (unsigned __int8)(result);
    *(unsigned __int64 *)(v_rbx + 5) = 0;
    *(unsigned __int64 *)(v_rbx + 13) = 0;
    *(unsigned __int64 *)(v_rbx + 21) = 0;
    *(unsigned __int64 *)(v_rbx + 45) = 0;
    result = (unsigned __int8)((*(unsigned __int8 *)(v_stack_p8 + 66)) + ((unsigned __int8)(0 + 1)));
    if ((*(unsigned __int8 *)(v_stack_p8 + 67)) != ((unsigned __int8)(result))) goto loc_0029B76B;
    goto loc_0029B776;
loc_0029B727:
    if (sign_flag) goto loc_0029B6F6;
loc_0029B72B:
    if ((*(unsigned __int8 *)(v_stack_p8 + 68)) == 0) goto loc_0029B738;
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_rbx))) & (32)) != 0) goto loc_0029B6F6;
loc_0029B738:
    if ((*(unsigned __int8 *)(v_stack_p8 + 65)) == 0) goto loc_0029B751;
    result = *(unsigned __int8 *)(v_stack_p8 + 66);
    if ((*(unsigned __int8 *)(v_stack_p8 + 67)) <= ((unsigned __int8)(*(unsigned __int8 *)(v_stack_p8 + 66)))) {
        result = *(unsigned __int64 *)(v_stack_p8 + 184);
    }
    *(unsigned __int64 *)(v_rbx + 5) = 0;
    *(unsigned __int64 *)(v_rbx + 13) = 0;
    *(unsigned __int64 *)(v_rbx + 21) = 0;
    *(unsigned __int64 *)(v_rbx + 45) = 0;
    goto loc_0029B7C8;
loc_0029B76B:
loc_0029B776:
    result = *(unsigned __int64 *)(v_stack_p8 + 184);
    if (0 != 0) {
        a3 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 184) + 40);
        a2 = (unsigned __int8)(*(unsigned __int8 *)(v_rbx - 2));
        result = PoDeviceAcquireIrp(v_stack_p8, a2, a3, a4);
        a1 = v_stack_p8;
    }
    result = guard_dispatch_icall(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 184) + 40), a1, *(unsigned __int64 *)(v_rbx + 61), a4);
    if (((unsigned int)(result)) == 0xC0000016ULL) goto loc_0029BD52;
    a4 = 0;
    if (0 != 0) {
        a1 = v_stack_p8;
        a3 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 184) + 40);
        a2 = (unsigned __int8)(*(unsigned __int8 *)(v_rbx - 2));
        result = PoDeviceReleaseIrp(a1, a2, a3, a4);
        a4 = 0;
    }
loc_0029B7C8:
    v_rbx = (v_rbx) + (72);
    result = (unsigned __int8)((*(unsigned __int8 *)(v_stack_p8 + 66)) + (1));
    if ((*(unsigned __int8 *)(v_stack_p8 + 67)) <= ((unsigned __int8)(result))) goto loc_0029B6B6;
loc_0029B7F7:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p8 + 16)))) & (8)) == 0) goto loc_0029B844;
    if (*(unsigned __int64 *)(v_stack_p8 + 8) == 0) goto loc_0029B81B;
loc_0029B80B:
    result = IoFreeMdl(*(unsigned __int64 *)(v_stack_p8 + 8), a2, a3, a4);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 8)) != 0) goto loc_0029B80B;
loc_0029B81B:
    result = IoFreeIrp(v_stack_p8, a2, a3, a4);
    result = (unsigned int)((result) | (0xFFFFFFFFULL));
    if (((unsigned int)(result)) != 1) goto loc_0029BD52;
    result = IofCompleteRequest(*(unsigned __int64 *)(v_stack_p8 + 24), a2, a3, a4);
    goto loc_0029BD52;
loc_0029B844:
    if ((*(unsigned int *)(v_stack_p8 + 48)) != 260) goto loc_0029B895;
    if ((*(unsigned __int64 *)(v_stack_p8 + 56)) <= 2) goto loc_0029B895;
    a1 = (*(unsigned __int64 *)(v_stack_p8 + 24)) + (*(unsigned __int64 *)(v_stack_p8 + 56));
    if (a1 > 22) goto loc_0029B88A;
    if (a1 >= 22) goto loc_0029B88A;
    v_stack_p18 = *(unsigned __int64 *)(v_stack_p8 + 160);
    *(unsigned __int64 *)(v_stack_p8 + 160) = 0;
    goto loc_0029B891;
loc_0029B88A:
    *(unsigned int *)(v_stack_p8 + 48) = 0xC0000279ULL;
loc_0029B891:
loc_0029B895:
    if (a2 != 0) goto loc_0029B8C5;
    if (*(unsigned __int64 *)(v_stack_p8 + 192) == 0) goto loc_0029B8C5;
    if (((*(unsigned int *)(v_stack_p8 + 16)) & (0x400ULL)) != 0) goto loc_0029B8C5;
    result = IoGetRelatedDeviceObject(*(unsigned __int64 *)(v_stack_p8 + 192), (unsigned int)(0x400201ULL), a3, a4);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result + 72)))) == 8) goto loc_0029B8F2;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result + 72)))) == 20) goto loc_0029B8F2;
loc_0029B8C5:
loc_0029B8CB:
    if (*(unsigned __int64 *)(v_stack_p8 + 160) == 0) goto loc_0029B901;
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(v_stack_p8 + 160), a2, a3, a4);
    v_r15 = 0;
    *(unsigned __int64 *)(v_stack_p8 + 160) = 0;
    goto loc_0029B904;
loc_0029B8F2:
    goto loc_0029B8CB;
loc_0029B901:
    v_r15 = 0;
loc_0029B904:
    a2 = (unsigned int)((a2) | (0xFFFFFFFFULL));
    result = IopFreeIrpExtension(v_stack_p8, a2, 1, a4);
    if (result == 0) goto loc_0029B937;
    result = guard_dispatch_icall(v_stack_p8, *(unsigned __int64 *)(v_stack_p8 + 192), 1, a4);
    if ((unsigned __int8)(result) != 0) goto loc_0029BD52;
loc_0029B937:
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 16)))) & (0x402ULL)) == 0) goto loc_0029B9ED;
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 16)))) & (0x440ULL)) == 0) goto loc_0029B996;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 72)) = v_xmm0;
    v_rdi = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p8 + 16))) & (66));
    result = *(unsigned __int64 *)(v_stack_p8 + 72);
    if (!(condition_is_equal)) {
        a1 = v_stack_p8;
        result = IopDequeueIrpFromThread(a1, *(unsigned __int64 *)(v_stack_p8 + 192), 1, a4);
    }
    a3 = 0;
    result = KeSetEvent(*(unsigned __int64 *)(v_stack_p8 + 80), 1, a3, a4);
    if ((unsigned int)(v_rdi) == 0) goto loc_0029BD52;
    result = IoFreeIrp(v_stack_p8, 1, a3, a4);
    goto loc_0029BD52;
loc_0029B996:
    result = IopDequeueIrpFromThread(v_stack_p8, 1, a3, a4);
    v_stack_m70 = 0;
    v_stack_m78 = 0;
    v_stack_m80 = 0;
    v_stack_m88 = 0;
    result = KeInitializeApc(v_stack_p8 + 120, *(unsigned __int64 *)(v_stack_p8 + 152), (__int8)(*(unsigned __int8 *)(v_stack_p8 + 70)), v_rip - 14745);
    a3 = 0;
    a1 = (v_stack_p8) + (120);
    a2 = 0;
loc_0029B9DF:
    result = KeInsertQueueApc(a1, a2, a3, 1);
    goto loc_0029BD52;
loc_0029B9ED:
    if (*(unsigned __int64 *)(v_stack_p8 + 8) == 0) goto loc_0029BA10;
loc_0029B9F6:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_p8 + 8) + 10)) & (2)) != 0) {
        a1 = *(unsigned __int64 *)(v_stack_p8 + 8);
        result = MmUnlockPages(a1, a2, a3, 1);
    }
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 8)) != 0) goto loc_0029B9F6;
loc_0029BA10:
    if (((*(unsigned int *)(v_stack_p8 + 16)) & (0x2000ULL)) == 0) goto loc_0029BA4C;
    result = Feature_3458701627__private_IsEnabledDeviceUsageNoInline(a1, a2, a3, 1);
    if ((unsigned int)(result) != 0) goto loc_0029BA3D;
    result = ObfDereferenceObjectWithTag(*(unsigned __int64 *)(v_stack_p8 + 152), (unsigned int)(0x746C6644ULL), a3, 1);
    goto loc_0029BA4C;
loc_0029BA3D:
    v_stack_m68 = *(unsigned __int64 *)(v_stack_p8 + 152);
loc_0029BA4C:
    if (condition_is_above_or_equal) goto loc_0029BA97;
    if ((*(unsigned __int8 *)(v_stack_p8 + 65)) != 0) goto loc_0029BA97;
    if ((*(unsigned int *)(v_stack_p8 + 48)) != 260) goto loc_0029BD52;
    a1 = (*(unsigned __int64 *)(v_stack_p8 + 152)) + (*(unsigned __int64 *)(v_stack_p8 + 56));
    if (a1 > 22) goto loc_0029BD52;
    if (a1 >= 22) goto loc_0029BD52;
    *(unsigned __int64 *)(v_stack_p8 + 160) = *(unsigned __int64 *)(v_stack_p8 + 160);
    goto loc_0029BD52;
loc_0029BA97:
    v_stack_p20 = *(unsigned __int64 *)(v_stack_p8 + 192);
    if (a1 >= 22) goto loc_0029BB51;
    result = Feature_1565498680__private_IsEnabledDeviceUsageNoInline(a1, (unsigned int)(0x746C6644ULL), a3, 1);
    if ((unsigned int)(result) != 0) goto loc_0029BAE5;
    result = IopDoesCompletionNeedsApc(v_stack_p8, (unsigned int)(0x746C6644ULL), a3, 1);
    if ((unsigned __int8)(result) != 0) goto loc_0029BB71;
    if ((*(unsigned __int8 *)(v_stack_p8 + 68)) == 0) goto loc_0029BB33;
    if (((*(unsigned int *)(v_stack_p8 + 16)) & (0x2000ULL)) == 0) goto loc_0029BB71;
    goto loc_0029BB33;
loc_0029BAE5:
    if (((*(unsigned int *)(v_stack_p8 + 16)) & (0x2000ULL)) == 0) goto loc_0029BAFC;
    result = IopDoesCompletionNeedsApc(v_stack_p8, (unsigned int)(0x746C6644ULL), a3, 1);
    if ((unsigned __int8)(result) != 0) goto loc_0029BB71;
    goto loc_0029BB33;
loc_0029BAFC:
    if ((*(unsigned __int8 *)(v_stack_p8 + 68)) != 0) goto loc_0029BB71;
    result = KeAreAllApcsDisabled(v_stack_p8, (unsigned int)(0x746C6644ULL), a3, 1);
    if ((unsigned __int8)(result) != 0) goto loc_0029BB6D;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 586)) == 1) goto loc_0029BB47;
    if ((*(unsigned __int64 *)(v_stack_p8 + 152)) != (*(unsigned __int64 *)(gs_base + (0 + 392)))) goto loc_0029BB47;
loc_0029BB33:
    result = IopIoRingCompleteIrp(v_stack_p8, v_stack_p20, 1, 1);
    goto loc_0029BD52;
loc_0029BB47:
    goto loc_0029BB6D;
loc_0029BB51:
    if ((*(unsigned __int64 *)(v_stack_p8 + 152)) >= (*(unsigned __int64 *)(gs_base + (0 + 392)))) goto loc_0029BB71;
    result = IopCompleteIrpInFileObjectList(v_stack_p8, v_stack_p20, 1, 1);
    if ((unsigned __int8)(result) != 0) goto loc_0029BD52;
loc_0029BB6D:
loc_0029BB71:
    v_rbx = v_stack_p8;
    if (*(unsigned __int64 *)(v_stack_p8 + 152) != 0) {
        v_rbx = *(unsigned __int64 *)(v_stack_p8 + 152) + 1560;
        a1 = v_rbx;
        result = KeAcquireSpinLockRaiseToDpc(a1, v_stack_p20, 1, 1);
        a2 = (unsigned __int8)(result);
        a1 = v_rbx;
        result = KeReleaseSpinLock(a1, a2, 1, 1);
        v_rbx = v_stack_p8;
    }
    if ((*(unsigned __int8 *)(v_rbx + 68)) != 0) goto loc_0029BC73;
    if ((*(unsigned __int64 *)(v_stack_p8 + 152)) != (*(unsigned __int64 *)(gs_base + (0 + 392)))) goto loc_0029BC27;
    result = KeAreAllApcsDisabled(a1, a2, 1, 1);
    if ((unsigned __int8)(result) != 0) goto loc_0029BC27;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 586)) == 1) goto loc_0029BC27;
    v_stack_m60 = 1;
    result = *(unsigned __int64 *)(gs_base + (0 + 392));
    if ((*(unsigned int *)(v_rip + 13807943)) != 0) {
        a2 = 1;
        a1 = (unsigned __int8)(v_cr8);
        result = KiRaiseIrqlProcessIrqlFlags(a1, a2, 1, 1);
    }
    a1 = (v_stack_p8) + (120);
    v_stack_m88 = v_stack_p18;
    result = IopCompleteRequest(a1, v_stack_m58, v_stack_m60, v_stack_p20);
    if ((*(unsigned int *)(v_rip + 13807890)) != 0) {
        a1 = 1;
        a2 = (unsigned __int8)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, v_stack_m60, v_stack_p20);
    }
    goto loc_0029BD52;
loc_0029BC27:
    v_stack_m70 = 0;
    v_stack_m78 = 0;
    v_stack_m80 = 0;
    a1 = (v_stack_p8) + (120);
    v_stack_m88 = v_rip + 4714510;
    result = KeInitializeApc(a1, *(unsigned __int64 *)(v_stack_p8 + 152), (__int8)(*(unsigned __int8 *)(v_stack_p8 + 70)), v_rip - 593134);
    a1 = (v_stack_p8) + (120);
    goto loc_0029B9DF;
loc_0029BC73:
    result = KeAcquireQueuedSpinLock(11, v_stack_p20, v_stack_p18, v_rip - 593134);
    if ((*(unsigned __int64 *)(v_rip + 13572068)) == (v_rip + 13572061)) goto loc_0029BCB3;
loc_0029BC9F:
    if ((*(unsigned __int64 *)(v_rip + 13572068) - 32) == v_stack_p8) goto loc_0029BD12;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 13572068))) != (v_rip + 13572061)) goto loc_0029BC9F;
loc_0029BCB3:
    if (*(unsigned __int64 *)(v_stack_p8 + 152) == 0) goto loc_0029BD3C;
    v_stack_m70 = 0;
    v_stack_m78 = 0;
    v_stack_m80 = 0;
    v_stack_m88 = v_rip + 4714351;
    result = KeInitializeApc(v_stack_p8 + 120, *(unsigned __int64 *)(v_stack_p8 + 152), (__int8)(*(unsigned __int8 *)(v_stack_p8 + 70)), v_rip - 593293);
    a1 = (v_stack_p8) + (120);
    result = KeInsertQueueApc(a1, v_stack_p20, v_stack_p18, 1);
    result = KeReleaseQueuedSpinLock(11, (unsigned __int8)((unsigned __int8)(result)), v_stack_p18, 1);
    goto loc_0029BD52;
loc_0029BD12:
    if ((*(unsigned __int64 *)(v_stack_p18 + 8)) != ((unsigned __int8)((unsigned __int8)(result)))) goto loc_0029BD83;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned __int8)((unsigned __int8)(result)) + 8))) != ((unsigned __int8)((unsigned __int8)(result)))) goto loc_0029BD83;
    *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned __int8)((unsigned __int8)(result)) + 8)) = v_stack_p18;
    *(unsigned __int64 *)(v_stack_p18 + 8) = *(unsigned __int64 *)((unsigned __int8)((unsigned __int8)(result)) + 8);
    *(unsigned __int64 *)((unsigned __int8)((unsigned __int8)(result)) + 8) = (unsigned __int8)((unsigned __int8)(result));
    *(unsigned __int64 *)((unsigned __int8)((unsigned __int8)(result))) = (unsigned __int8)((unsigned __int8)(result));
    result = ObfDereferenceObjectWithTag(*(unsigned __int64 *)(v_stack_p8 + 152), (unsigned int)(0x746C6644ULL), v_stack_p18, 1);
loc_0029BD3C:
    result = KeReleaseQueuedSpinLock(11, (unsigned __int8)((unsigned __int8)(result)), v_stack_p18, 1);
    result = IopDropIrp(v_stack_p8, v_stack_p20, v_stack_p18, 1);
loc_0029BD52:
    result = Feature_3458701627__private_IsEnabledDeviceUsageNoInline(v_stack_p8, v_stack_p20, v_stack_p18, 1);
    if ((unsigned int)(result) == 0) goto loc_0029BD71;
    result = v_stack_m68;
    if (v_stack_m68 != 0) {
        a2 = 0x746C6644ULL;
        a1 = v_stack_m68;
        result = ObfDereferenceObjectWithTag(a1, a2, v_stack_p18, 1);
    }
    v_rsp = (v_rsp) + (104);
    return result;
loc_0029BD83:
loc_0029BD8A:
    v_stack_p20 = 1;
    result = KeBugCheckEx(68, 11, (unsigned int)(0x1315ULL), 1);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t IopfCompleteRequest(void *Arg1, uint8_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint8_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (104);
    Arg4 = 0;
    v_stack_p18 = 0;
    v_stack_m68 = 0;
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x43))) > ((uint8_t)(Arg4 + 1 + *(uint8_t *)(arg1 + 0x42) * 1))) goto loc_0029BD8A;
    if ((*(uint16_t *)(arg1)) != 6) goto loc_0029BD8A;
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x43))) > ((uint8_t)(*(uint8_t *)(arg1 + 0x42)))) goto loc_0029B677;
    if ((*(uint8_t *)(*(uint64_t *)(arg1 + 0xB8))) != 22) goto loc_0029B677;
    result = PoDeviceReleaseIrp(Arg1, *(uint8_t *)(*(uint64_t *)(arg1 + 0xB8) + 0x1), *(uint64_t *)(*(uint64_t *)(arg1 + 0xB8) + 0x28), Arg4);
    Arg4 = 0;
    goto loc_0029B67A;
loc_0029B677:
loc_0029B67A:
    if (((*(uint8_t *)(v_stack_p8 + 0xD3)) & (2)) == 0) goto loc_0029B68C;
    goto loc_0029B68F;
loc_0029B68C:
loc_0029B68F:
    result = (uint8_t)((*(uint8_t *)(v_stack_p8 + 0x42)) + ((uint8_t)(0 + 1)));
    if ((*(uint8_t *)(v_stack_p8 + 0x43)) > ((uint8_t)(result))) goto loc_0029B7F7;
    local_rbx = (*(uint64_t *)(arg1 + 0xB8)) + (3);
loc_0029B6B6:
    result = (uint8_t)((*(uint8_t *)(local_rbx)) & ((uint8_t)(0 + 1)));
    *(uint8_t *)(v_stack_p8 + 0x41) = (uint8_t)(result);
    if (!sign_flag) goto loc_0029B6E7;
    local_r15 = 0;
    if (((uint32_t)((int32_t)(*(uint32_t *)(v_stack_p8 + 0x30)))) != 0) {
        local_r15 = (int32_t)(*(uint32_t *)(v_stack_p8 + 0x30));
        *(uint64_t *)(v_stack_p8 + 0xF0) = (int32_t)(*(uint32_t *)(v_stack_p8 + 0x30));
        Arg1 = v_stack_p8;
    }
    if ((*(uint32_t *)(arg1 + 0x30)) < 0) goto loc_0029B727;
    if ((((uint8_t)(*(uint8_t *)(local_rbx))) & (64)) == 0) goto loc_0029B72B;
loc_0029B6F6:
    result = (uint8_t)(((uint8_t)(*(uint8_t *)(local_rbx))) & (2));
    *(uint8_t *)(local_rbx) = (uint8_t)(result);
    *(uint64_t *)(local_rbx + 0x5) = 0;
    *(uint64_t *)(local_rbx + 0xD) = 0;
    *(uint64_t *)(local_rbx + 0x15) = 0;
    *(uint64_t *)(local_rbx + 0x2D) = 0;
    result = (uint8_t)((*(uint8_t *)(v_stack_p8 + 0x42)) + ((uint8_t)(0 + 1)));
    if ((*(uint8_t *)(v_stack_p8 + 0x43)) != ((uint8_t)(result))) goto loc_0029B76B;
    goto loc_0029B776;
loc_0029B727:
    if (sign_flag) goto loc_0029B6F6;
loc_0029B72B:
    if ((*(uint8_t *)(v_stack_p8 + 0x44)) == 0) goto loc_0029B738;
    if ((((uint8_t)(*(uint8_t *)(local_rbx))) & (32)) != 0) goto loc_0029B6F6;
loc_0029B738:
    if ((*(uint8_t *)(v_stack_p8 + 0x41)) == 0) goto loc_0029B751;
    result = *(uint8_t *)(v_stack_p8 + 0x42);
    if ((*(uint8_t *)(v_stack_p8 + 0x43)) <= ((uint8_t)(*(uint8_t *)(v_stack_p8 + 0x42)))) {
        result = *(uint64_t *)(v_stack_p8 + 0xB8);
    }
    *(uint64_t *)(local_rbx + 0x5) = 0;
    *(uint64_t *)(local_rbx + 0xD) = 0;
    *(uint64_t *)(local_rbx + 0x15) = 0;
    *(uint64_t *)(local_rbx + 0x2D) = 0;
    goto loc_0029B7C8;
loc_0029B76B:
loc_0029B776:
    result = *(uint64_t *)(v_stack_p8 + 0xB8);
    if (0 != 0) {
        Arg3 = *(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0xB8) + 0x28);
        Arg2 = (uint8_t)(*(uint8_t *)(local_rbx - 0x2));
        result = PoDeviceAcquireIrp(v_stack_p8, Arg2, Arg3, Arg4);
        Arg1 = v_stack_p8;
    }
    result = guard_dispatch_icall(*(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0xB8) + 0x28), Arg1, *(uint64_t *)(local_rbx + 0x3D), Arg4);
    if (((uint32_t)(result)) == 0xC0000016ULL) goto loc_0029BD52;
    Arg4 = 0;
    if (0 != 0) {
        Arg1 = v_stack_p8;
        Arg3 = *(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0xB8) + 0x28);
        Arg2 = (uint8_t)(*(uint8_t *)(local_rbx - 0x2));
        result = PoDeviceReleaseIrp(Arg1, Arg2, Arg3, Arg4);
        Arg4 = 0;
    }
loc_0029B7C8:
    local_rbx = (local_rbx) + (72);
    result = (uint8_t)((*(uint8_t *)(v_stack_p8 + 0x42)) + (1));
    if ((*(uint8_t *)(v_stack_p8 + 0x43)) <= ((uint8_t)(result))) goto loc_0029B6B6;
loc_0029B7F7:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x10)))) & (8)) == 0) goto loc_0029B844;
    if (*(uint64_t *)(v_stack_p8 + 0x8) == 0) goto loc_0029B81B;
loc_0029B80B:
    result = IoFreeMdl(*(uint64_t *)(v_stack_p8 + 0x8), Arg2, Arg3, Arg4);
    if (*(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0x8)) != 0) goto loc_0029B80B;
loc_0029B81B:
    result = IoFreeIrp(v_stack_p8, Arg2, Arg3, Arg4);
    result = (uint32_t)((result) | (0xFFFFFFFFULL));
    if (((uint32_t)(result)) != 1) goto loc_0029BD52;
    result = IofCompleteRequest(*(uint64_t *)(v_stack_p8 + 0x18), Arg2, Arg3, Arg4);
    goto loc_0029BD52;
loc_0029B844:
    if ((*(uint32_t *)(v_stack_p8 + 0x30)) != 260) goto loc_0029B895;
    if ((*(uint64_t *)(v_stack_p8 + 0x38)) <= 2) goto loc_0029B895;
    Arg1 = (*(uint64_t *)(v_stack_p8 + 0x18)) + (*(uint64_t *)(v_stack_p8 + 0x38));
    if (Arg1 > 22) goto loc_0029B88A;
    if (Arg1 >= 22) goto loc_0029B88A;
    v_stack_p18 = *(uint64_t *)(v_stack_p8 + 0xA0);
    *(uint64_t *)(v_stack_p8 + 0xA0) = 0;
    goto loc_0029B891;
loc_0029B88A:
    *(uint32_t *)(v_stack_p8 + 0x30) = 0xC0000279ULL;
loc_0029B891:
loc_0029B895:
    if (Arg2 != 0) goto loc_0029B8C5;
    if (*(uint64_t *)(v_stack_p8 + 0xC0) == 0) goto loc_0029B8C5;
    if (((*(uint32_t *)(v_stack_p8 + 0x10)) & (0x400ULL)) != 0) goto loc_0029B8C5;
    result = IoGetRelatedDeviceObject(*(uint64_t *)(v_stack_p8 + 0xC0), (uint32_t)(0x400201ULL), Arg3, Arg4);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x48)))) == 8) goto loc_0029B8F2;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x48)))) == 20) goto loc_0029B8F2;
loc_0029B8C5:
loc_0029B8CB:
    if (*(uint64_t *)(v_stack_p8 + 0xA0) == 0) goto loc_0029B901;
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(v_stack_p8 + 0xA0), Arg2, Arg3, Arg4);
    local_r15 = 0;
    *(uint64_t *)(v_stack_p8 + 0xA0) = 0;
    goto loc_0029B904;
loc_0029B8F2:
    goto loc_0029B8CB;
loc_0029B901:
    local_r15 = 0;
loc_0029B904:
    Arg2 = (uint32_t)((Arg2) | (0xFFFFFFFFULL));
    result = IopFreeIrpExtension(v_stack_p8, Arg2, 1, Arg4);
    if (result == 0) goto loc_0029B937;
    result = guard_dispatch_icall(v_stack_p8, *(uint64_t *)(v_stack_p8 + 0xC0), 1, Arg4);
    if ((uint8_t)(result) != 0) goto loc_0029BD52;
loc_0029B937:
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x10)))) & (0x402ULL)) == 0) goto loc_0029B9ED;
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x10)))) & (0x440ULL)) == 0) goto loc_0029B996;
    *(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0x48)) = v_xmm0;
    local_rdi = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x10))) & (66));
    result = *(uint64_t *)(v_stack_p8 + 0x48);
    if (!(condition_is_equal)) {
        Arg1 = v_stack_p8;
        result = IopDequeueIrpFromThread(Arg1, *(uint64_t *)(v_stack_p8 + 0xC0), 1, Arg4);
    }
    Arg3 = 0;
    result = KeSetEvent(*(uint64_t *)(v_stack_p8 + 0x50), 1, Arg3, Arg4);
    if ((uint32_t)(local_rdi) == 0) goto loc_0029BD52;
    result = IoFreeIrp(v_stack_p8, 1, Arg3, Arg4);
    goto loc_0029BD52;
loc_0029B996:
    result = IopDequeueIrpFromThread(v_stack_p8, 1, Arg3, Arg4);
    v_stack_m70 = 0;
    v_stack_m78 = 0;
    v_stack_m80 = 0;
    v_stack_m88 = 0;
    result = KeInitializeApc(v_stack_p8 + 120, *(uint64_t *)(v_stack_p8 + 0x98), (int8_t)(*(uint8_t *)(v_stack_p8 + 0x46)), v_rip - 14745);
    Arg3 = 0;
    Arg1 = (v_stack_p8) + (120);
    Arg2 = 0;
loc_0029B9DF:
    result = KeInsertQueueApc(Arg1, Arg2, Arg3, 1);
    goto loc_0029BD52;
loc_0029B9ED:
    if (*(uint64_t *)(v_stack_p8 + 0x8) == 0) goto loc_0029BA10;
loc_0029B9F6:
    if (((*(uint8_t *)(*(uint64_t *)(v_stack_p8 + 0x8) + 0xA)) & (2)) != 0) {
        Arg1 = *(uint64_t *)(v_stack_p8 + 0x8);
        result = MmUnlockPages(Arg1, Arg2, Arg3, 1);
    }
    if (*(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0x8)) != 0) goto loc_0029B9F6;
loc_0029BA10:
    if (((*(uint32_t *)(v_stack_p8 + 0x10)) & (0x2000ULL)) == 0) goto loc_0029BA4C;
    result = Feature_3458701627__private_IsEnabledDeviceUsageNoInline(Arg1, Arg2, Arg3, 1);
    if ((uint32_t)(result) != 0) goto loc_0029BA3D;
    result = ObfDereferenceObjectWithTag(*(uint64_t *)(v_stack_p8 + 0x98), (uint32_t)(0x746C6644ULL), Arg3, 1);
    goto loc_0029BA4C;
loc_0029BA3D:
    v_stack_m68 = *(uint64_t *)(v_stack_p8 + 0x98);
loc_0029BA4C:
    if (condition_is_above_or_equal) goto loc_0029BA97;
    if ((*(uint8_t *)(v_stack_p8 + 0x41)) != 0) goto loc_0029BA97;
    if ((*(uint32_t *)(v_stack_p8 + 0x30)) != 260) goto loc_0029BD52;
    Arg1 = (*(uint64_t *)(v_stack_p8 + 0x98)) + (*(uint64_t *)(v_stack_p8 + 0x38));
    if (Arg1 > 22) goto loc_0029BD52;
    if (Arg1 >= 22) goto loc_0029BD52;
    *(uint64_t *)(v_stack_p8 + 0xA0) = *(uint64_t *)(v_stack_p8 + 0xA0);
    goto loc_0029BD52;
loc_0029BA97:
    v_stack_p20 = *(uint64_t *)(v_stack_p8 + 0xC0);
    if (Arg1 >= 22) goto loc_0029BB51;
    result = Feature_1565498680__private_IsEnabledDeviceUsageNoInline(Arg1, (uint32_t)(0x746C6644ULL), Arg3, 1);
    if ((uint32_t)(result) != 0) goto loc_0029BAE5;
    result = IopDoesCompletionNeedsApc(v_stack_p8, (uint32_t)(0x746C6644ULL), Arg3, 1);
    if ((uint8_t)(result) != 0) goto loc_0029BB71;
    if ((*(uint8_t *)(v_stack_p8 + 0x44)) == 0) goto loc_0029BB33;
    if (((*(uint32_t *)(v_stack_p8 + 0x10)) & (0x2000ULL)) == 0) goto loc_0029BB71;
    goto loc_0029BB33;
loc_0029BAE5:
    if (((*(uint32_t *)(v_stack_p8 + 0x10)) & (0x2000ULL)) == 0) goto loc_0029BAFC;
    result = IopDoesCompletionNeedsApc(v_stack_p8, (uint32_t)(0x746C6644ULL), Arg3, 1);
    if ((uint8_t)(result) != 0) goto loc_0029BB71;
    goto loc_0029BB33;
loc_0029BAFC:
    if ((*(uint8_t *)(v_stack_p8 + 0x44)) != 0) goto loc_0029BB71;
    result = KeAreAllApcsDisabled(v_stack_p8, (uint32_t)(0x746C6644ULL), Arg3, 1);
    if ((uint8_t)(result) != 0) goto loc_0029BB6D;
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x24A)) == 1) goto loc_0029BB47;
    if ((*(uint64_t *)(v_stack_p8 + 0x98)) != (*(uint64_t *)(gs_base + (0 + 0x188)))) goto loc_0029BB47;
loc_0029BB33:
    result = IopIoRingCompleteIrp(v_stack_p8, v_stack_p20, 1, 1);
    goto loc_0029BD52;
loc_0029BB47:
    goto loc_0029BB6D;
loc_0029BB51:
    if ((*(uint64_t *)(v_stack_p8 + 0x98)) >= (*(uint64_t *)(gs_base + (0 + 0x188)))) goto loc_0029BB71;
    result = IopCompleteIrpInFileObjectList(v_stack_p8, v_stack_p20, 1, 1);
    if ((uint8_t)(result) != 0) goto loc_0029BD52;
loc_0029BB6D:
loc_0029BB71:
    local_rbx = v_stack_p8;
    if (*(uint64_t *)(v_stack_p8 + 0x98) != 0) {
        local_rbx = *(uint64_t *)(v_stack_p8 + 0x98) + 1560;
        Arg1 = local_rbx;
        result = KeAcquireSpinLockRaiseToDpc(Arg1, v_stack_p20, 1, 1);
        Arg2 = (uint8_t)(result);
        Arg1 = local_rbx;
        result = KeReleaseSpinLock(Arg1, Arg2, 1, 1);
        local_rbx = v_stack_p8;
    }
    if ((*(uint8_t *)(local_rbx + 0x44)) != 0) goto loc_0029BC73;
    if ((*(uint64_t *)(v_stack_p8 + 0x98)) != (*(uint64_t *)(gs_base + (0 + 0x188)))) goto loc_0029BC27;
    result = KeAreAllApcsDisabled(Arg1, Arg2, 1, 1);
    if ((uint8_t)(result) != 0) goto loc_0029BC27;
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x24A)) == 1) goto loc_0029BC27;
    v_stack_m60 = 1;
    result = *(uint64_t *)(gs_base + (0 + 0x188));
    if ((*(uint32_t *)(v_rip + 0xD2B147)) != 0) {
        Arg2 = 1;
        Arg1 = (uint8_t)(v_cr8);
        result = KiRaiseIrqlProcessIrqlFlags(Arg1, Arg2, 1, 1);
    }
    Arg1 = (v_stack_p8) + (120);
    v_stack_m88 = v_stack_p18;
    result = IopCompleteRequest(Arg1, v_stack_m58, v_stack_m60, v_stack_p20);
    if ((*(uint32_t *)(v_rip + 0xD2B112)) != 0) {
        Arg1 = 1;
        Arg2 = (uint8_t)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, v_stack_m60, v_stack_p20);
    }
    goto loc_0029BD52;
loc_0029BC27:
    v_stack_m70 = 0;
    v_stack_m78 = 0;
    v_stack_m80 = 0;
    Arg1 = (v_stack_p8) + (120);
    v_stack_m88 = v_rip + 4714510;
    result = KeInitializeApc(Arg1, *(uint64_t *)(v_stack_p8 + 0x98), (int8_t)(*(uint8_t *)(v_stack_p8 + 0x46)), v_rip - 593134);
    Arg1 = (v_stack_p8) + (120);
    goto loc_0029B9DF;
loc_0029BC73:
    result = KeAcquireQueuedSpinLock(11, v_stack_p20, v_stack_p18, v_rip - 593134);
    if ((*(uint64_t *)(v_rip + 0xCF17E4)) == (v_rip + 13572061)) goto loc_0029BCB3;
loc_0029BC9F:
    if ((*(uint64_t *)(v_rip + 0xCF17E4) - 32) == v_stack_p8) goto loc_0029BD12;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xCF17E4))) != (v_rip + 13572061)) goto loc_0029BC9F;
loc_0029BCB3:
    if (*(uint64_t *)(v_stack_p8 + 0x98) == 0) goto loc_0029BD3C;
    v_stack_m70 = 0;
    v_stack_m78 = 0;
    v_stack_m80 = 0;
    v_stack_m88 = v_rip + 4714351;
    result = KeInitializeApc(v_stack_p8 + 120, *(uint64_t *)(v_stack_p8 + 0x98), (int8_t)(*(uint8_t *)(v_stack_p8 + 0x46)), v_rip - 593293);
    Arg1 = (v_stack_p8) + (120);
    result = KeInsertQueueApc(Arg1, v_stack_p20, v_stack_p18, 1);
    result = KeReleaseQueuedSpinLock(11, (uint8_t)((uint8_t)(result)), v_stack_p18, 1);
    goto loc_0029BD52;
loc_0029BD12:
    if ((*(uint64_t *)(v_stack_p18 + 0x8)) != ((uint8_t)((uint8_t)(result)))) goto loc_0029BD83;
    if ((*(uint64_t *)(*(uint64_t *)((uint8_t)((uint8_t)(result)) + 0x8))) != ((uint8_t)((uint8_t)(result)))) goto loc_0029BD83;
    *(uint64_t *)(*(uint64_t *)((uint8_t)((uint8_t)(result)) + 0x8)) = v_stack_p18;
    *(uint64_t *)(v_stack_p18 + 0x8) = *(uint64_t *)((uint8_t)((uint8_t)(result)) + 0x8);
    *(uint64_t *)((uint8_t)((uint8_t)(result)) + 0x8) = (uint8_t)((uint8_t)(result));
    *(uint64_t *)((uint8_t)((uint8_t)(result))) = (uint8_t)((uint8_t)(result));
    result = ObfDereferenceObjectWithTag(*(uint64_t *)(v_stack_p8 + 0x98), (uint32_t)(0x746C6644ULL), v_stack_p18, 1);
loc_0029BD3C:
    result = KeReleaseQueuedSpinLock(11, (uint8_t)((uint8_t)(result)), v_stack_p18, 1);
    result = IopDropIrp(v_stack_p8, v_stack_p20, v_stack_p18, 1);
loc_0029BD52:
    result = Feature_3458701627__private_IsEnabledDeviceUsageNoInline(v_stack_p8, v_stack_p20, v_stack_p18, 1);
    if ((uint32_t)(result) == 0) goto loc_0029BD71;
    result = v_stack_m68;
    if (v_stack_m68 != 0) {
        Arg2 = 0x746C6644ULL;
        Arg1 = v_stack_m68;
        result = ObfDereferenceObjectWithTag(Arg1, Arg2, v_stack_p18, 1);
    }
    local_rsp = (local_rsp) + (104);
    return result;
loc_0029BD83:
loc_0029BD8A:
    v_stack_p20 = 1;
    result = KeBugCheckEx(68, 11, (uint32_t)(0x1315ULL), 1);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `16` | `R` |
| `Arg1` | `+ 0x42` | `8` | `R` |
| `Arg1` | `+ 0x43` | `8` | `R` |
| `Arg1` | `+ 0xB8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0029B5F8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
