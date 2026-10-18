# IopCompleteIrpInFileObjectList

- RVA: `0x0024F330`–`0x0024FA6C` (길이 `1,852` bytes)
- VA: `0x000000014024F330`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000632FC`
- 디코드: `428`개 명령, `1,852/1,852` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **26**; 고유 호출 대상: **25**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x0024F44C` → [KiAcquireKobjectLockSafe](../25/KiAcquireKobjectLockSafe_function_00251C90.md) (function, `0x00251C90`)
- `0x0024F4EB` → [KiRemovePrcbWaitEntry](../25/KiRemovePrcbWaitEntry_function_002502D0.md) (function, `0x002502D0`)
- `0x0024F5D9` → [KiWakeOtherQueueWaiters](../39/KiWakeOtherQueueWaiters_function_003964D0.md) (function, `0x003964D0`)
- `0x0024F5FE` → [KiExitDispatcher](../25/KiExitDispatcher_function_00251CF0.md) (function, `0x00251CF0`)
- `0x0024F644` → [KxWaitForLockChainValid](../21/KxWaitForLockChainValid_function_00217AA0.md) (function, `0x00217AA0`)
- `0x0024F667` → [KeWakeAddressAll](../21/KeWakeAddressAll_function_00217C20.md) (function, `0x00217C20`)
- `0x0024F6FE` → [KiAcquireQueuedSpinLockInstrumented](../27/KiAcquireQueuedSpinLockInstrumented_function_00275850.md) (function, `0x00275850`)
- `0x0024F72C` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x0024F73D` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x0024F780` → [KiReleaseQueuedSpinLockInstrumented](../21/KiReleaseQueuedSpinLockInstrumented_function_002179F0.md) (function, `0x002179F0`)
- `0x0024F79A` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0024F7C0` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0024F7F6` → [KeAcquireSpinLockRaiseToDpc](../20/KeAcquireSpinLockRaiseToDpc_function_00208470.md) (function, `0x00208470`)
- `0x0024F849` → [ObFastDereferenceObject](../3E/ObFastDereferenceObject_function_003ED5F0.md) (function, `0x003ED5F0`)
- `0x0024F867` → [KeReleaseSpinLock](../39/KeReleaseSpinLock_function_00392BA0.md) (function, `0x00392BA0`)
- `0x0024F888` → [IoFreeIrp](IoFreeIrp_function_0024DF70.md) (function, `0x0024DF70`)
- `0x0024F8B6` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0024F8C5` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0024F8D2` → [KeIsThreadRunning](../39/KeIsThreadRunning_function_00396720.md) (function, `0x00396720`)
- `0x0024F8E1` → [EtwTraceEnqueueWork](../39/EtwTraceEnqueueWork_function_0039674C.md) (function, `0x0039674C`)
- `0x0024F90B` → [KxWaitForLockOwnerShip](../25/KxWaitForLockOwnerShip_function_00257EB0.md) (function, `0x00257EB0`)
- `0x0024F918` → [IopDoesCompletionNeedsApc](../3F/IopDoesCompletionNeedsApc_function_003FD094.md) (function, `0x003FD094`)
- `0x0024F942` → [ObDereferenceObjectExWithTag](../43/ObDereferenceObjectExWithTag_function_0043CBC0.md) (function, `0x0043CBC0`)
- `0x0024F9CE` → [IopCompleteRequest](../20/IopCompleteRequest_function_0020AF50.md) (function, `0x0020AF50`)
- `0x0024FA32` → [ObfDereferenceObjectWithTag](../2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x0024FA43` → [IoFreeMdl](../29/IoFreeMdl_function_0029EA80.md) (function, `0x0029EA80`)

### Direct callers
- [IopfCompleteRequest](../29/IopfCompleteRequest_function_0029B5F8.md) at `0x0029BB60`

### Static image references
- `0x0024F3B0` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x0024F3BC` → RVA `0x00FC6B06` (`ALMOSTRO`; read)
- `0x0024F425` → RVA `0x00FC6B04` (`ALMOSTRO`; read)
- `0x0024F6CF` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x0024F6E8` → RVA `0x00F0DE58` (`.data`; read)
- `0x0024F8A8` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0024F7C0` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0024F330  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
0024F335  55                              push rbp
0024F336  56                              push rsi
0024F337  57                              push rdi
0024F338  41 54                           push r12
0024F33A  41 55                           push r13
0024F33C  41 56                           push r14
0024F33E  41 57                           push r15
0024F340  48 83 EC 60                     sub rsp, 0x60
0024F344  45 33 F6                        xor r14d, r14d
0024F347  41 0F BE E8                     movsx ebp, r8b
0024F34B  48 8B F9                        mov rdi, rcx
0024F34E  4C 89 74 24 40                  mov qword ptr [rsp + 0x40], r14
0024F353  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
0024F358  44 38 71 41                     cmp byte ptr [rcx + 0x41], r14b
0024F35C  0F 84 EA 05 00 00               je 0x14024f94c
0024F362  48 8B 82 B0 00 00 00            mov rax, qword ptr [rdx + 0xb0]
0024F369  48 85 C0                        test rax, rax
0024F36C  0F 84 A3 05 00 00               je 0x14024f915
0024F372  0F 57 C0                        xorps xmm0, xmm0
0024F375  33 C9                           xor ecx, ecx
0024F377  0F 11 44 24 48                  movups xmmword ptr [rsp + 0x48], xmm0
0024F37C  48 89 4C 24 58                  mov qword ptr [rsp + 0x58], rcx
0024F381  4C 8B 38                        mov r15, qword ptr [rax]
0024F384  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0024F388  48 89 47 78                     mov qword ptr [rdi + 0x78], rax
0024F38C  44 89 B7 B8 00 00 00            mov dword ptr [rdi + 0xb8], r14d
0024F393  49 8D 5F 40                     lea rbx, [r15 + 0x40]
0024F397  4C 89 74 24 48                  mov qword ptr [rsp + 0x48], r14
0024F39C  48 89 5C 24 50                  mov qword ptr [rsp + 0x50], rbx
0024F3A1  90                              nop
0024F3A2  44 0F 20 C6                     mov rsi, cr8
0024F3A6  41 BC 02 00 00 00               mov r12d, 2
0024F3AC  45 0F 22 C4                     mov cr8, r12
0024F3B0  39 0D 6A 79 D7 00               cmp dword ptr [rip + 0xd7796a], ecx
0024F3B6  0F 85 68 03 00 00               jne 0x14024f724
0024F3BC  F6 05 43 77 D7 00 21            test byte ptr [rip + 0xd77743], 0x21
0024F3C3  40 88 74 24 58                  mov byte ptr [rsp + 0x58], sil
0024F3C8  0F 85 1A 03 00 00               jne 0x14024f6e8
0024F3CE  48 8D 54 24 48                  lea rdx, [rsp + 0x48]
0024F3D3  48 87 13                        xchg qword ptr [rbx], rdx
0024F3D6  48 85 D2                        test rdx, rdx
0024F3D9  0F 85 27 05 00 00               jne 0x14024f906
0024F3DF  81 4F 10 00 00 01 00            or dword ptr [rdi + 0x10], 0x10000
0024F3E6  45 38 77 48                     cmp byte ptr [r15 + 0x48], r14b
0024F3EA  0F 85 24 06 00 00               jne 0x14024fa14
0024F3F0  4C 8D B7 A8 00 00 00            lea r14, [rdi + 0xa8]
0024F3F7  89 AC 24 A0 00 00 00            mov dword ptr [rsp + 0xa0], ebp
0024F3FE  4D 8D 6F 08                     lea r13, [r15 + 8]
0024F402  44 0F 20 C0                     mov rax, cr8
0024F406  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0024F40B  45 0F 22 C4                     mov cr8, r12
0024F40F  83 3D 0A 79 D7 00 00            cmp dword ptr [rip + 0xd7790a], 0
0024F416  0F 85 1A 03 00 00               jne 0x14024f736
0024F41C  65 48 8B 34 25 20 00 00 00      mov rsi, qword ptr gs:[0x20]
0024F425  F7 05 D5 76 D7 00 00 00 00 01   test dword ptr [rip + 0xd776d5], 0x1000000
0024F42F  48 89 B4 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rsi
0024F437  48 8B 5E 08                     mov rbx, qword ptr [rsi + 8]
0024F43B  0F 85 8E 04 00 00               jne 0x14024f8cf
0024F441  85 ED                           test ebp, ebp
0024F443  0F 85 4D 02 00 00               jne 0x14024f696
0024F449  49 8B CF                        mov rcx, r15
0024F44C  E8 3F 28 00 00                  call 0x140251c90
0024F451  4D 39 6D 00                     cmp qword ptr [r13], r13
0024F455  0F 84 44 01 00 00               je 0x14024f59f
0024F45B  41 8B 47 28                     mov eax, dword ptr [r15 + 0x28]
0024F45F  41 3B 47 2C                     cmp eax, dword ptr [r15 + 0x2c]
0024F463  0F 83 36 01 00 00               jae 0x14024f59f
0024F469  48 8B 83 E8 00 00 00            mov rax, qword ptr [rbx + 0xe8]
0024F470  49 3B C7                        cmp rax, r15
0024F473  0F 84 7B 04 00 00               je 0x14024f8f4
0024F479  4D 8B 75 00                     mov r14, qword ptr [r13]
0024F47D  33 D2                           xor edx, edx
0024F47F  90                              nop
0024F480  49 8B F6                        mov rsi, r14
0024F483  4D 8B 36                        mov r14, qword ptr [r14]
0024F486  80 7E 10 03                     cmp byte ptr [rsi + 0x10], 3
0024F48A  0F 85 F9 00 00 00               jne 0x14024f589
0024F490  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
0024F494  49 39 76 08                     cmp qword ptr [r14 + 8], rsi
0024F498  75 09                           jne 0x14024f4a3
0024F49A  48 39 30                        cmp qword ptr [rax], rsi
0024F49D  0F 84 0B 02 00 00               je 0x14024f6ae
0024F4A3  B9 03 00 00 00                  mov ecx, 3
0024F4A8  CD 29                           int 0x29
0024F4AA  0F B6 83 84 01 00 00            movzx eax, byte ptr [rbx + 0x184]
0024F4B1  3C 05                           cmp al, 5
0024F4B3  0F 85 CA 01 00 00               jne 0x14024f683
0024F4B9  0F B6 4B 70                     movzx ecx, byte ptr [rbx + 0x70]
0024F4BD  8B C1                           mov eax, ecx
0024F4BF  83 E0 07                        and eax, 7
0024F4C2  83 F8 01                        cmp eax, 1
0024F4C5  0F 85 0D 05 00 00               jne 0x14024f9d8
0024F4CB  48 8B 93 E8 00 00 00            mov rdx, qword ptr [rbx + 0xe8]
0024F4D2  48 85 D2                        test rdx, rdx
0024F4D5  74 11                           je 0x14024f4e8
0024F4D7  0F B6 02                        movzx eax, byte ptr [rdx]
0024F4DA  24 7F                           and al, 0x7f
0024F4DC  3C 15                           cmp al, 0x15
0024F4DE  0F 84 24 02 00 00               je 0x14024f708
0024F4E4  F0 FF 42 28                     lock inc dword ptr [rdx + 0x28]
0024F4E8  48 8B CB                        mov rcx, rbx
0024F4EB  E8 E0 0D 00 00                  call 0x1402502d0
0024F4F0  0F B6 83 84 01 00 00            movzx eax, byte ptr [rbx + 0x184]
0024F4F7  3C 01                           cmp al, 1
0024F4F9  0F 84 EC 03 00 00               je 0x14024f8eb
0024F4FF  3C 05                           cmp al, 5
0024F501  75 26                           jne 0x14024f529
0024F503  48 B8 20 03 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000320
0024F50D  8B 08                           mov ecx, dword ptr [rax]
0024F50F  2B 8B B4 01 00 00               sub ecx, dword ptr [rbx + 0x1b4]
0024F515  44 38 A3 87 01 00 00            cmp byte ptr [rbx + 0x187], r12b
0024F51C  0F 84 68 01 00 00               je 0x14024f68a
0024F522  48 01 8B E8 03 00 00            add qword ptr [rbx + 0x3e8], rcx
0024F529  48 8B 94 24 B8 00 00 00         mov rdx, qword ptr [rsp + 0xb8]
0024F531  48 8D 8B D8 00 00 00            lea rcx, [rbx + 0xd8]
0024F538  C6 83 84 01 00 00 07            mov byte ptr [rbx + 0x184], 7
0024F53F  41 B4 01                        mov r12b, 1
0024F542  48 8B 82 08 2D 00 00            mov rax, qword ptr [rdx + 0x2d08]
0024F549  48 89 01                        mov qword ptr [rcx], rax
0024F54C  48 8D 87 A8 00 00 00            lea rax, [rdi + 0xa8]
0024F553  48 89 8A 08 2D 00 00            mov qword ptr [rdx + 0x2d08], rcx
0024F55A  33 D2                           xor edx, edx
0024F55C  48 89 83 C8 00 00 00            mov qword ptr [rbx + 0xc8], rax
0024F563  48 89 93 D0 03 00 00            mov qword ptr [rbx + 0x3d0], rdx
0024F56A  48 89 53 40                     mov qword ptr [rbx + 0x40], rdx
0024F56E  0F B6 46 11                     movzx eax, byte ptr [rsi + 0x11]
0024F572  FE C0                           inc al
0024F574  88 46 11                        mov byte ptr [rsi + 0x11], al
0024F577  45 84 E4                        test r12b, r12b
0024F57A  0F 85 C7 01 00 00               jne 0x14024f747
0024F580  4D 3B F5                        cmp r14, r13
0024F583  0F 85 F7 FE FF FF               jne 0x14024f480
0024F589  8B AC 24 A0 00 00 00            mov ebp, dword ptr [rsp + 0xa0]
0024F590  4C 8D B7 A8 00 00 00            lea r14, [rdi + 0xa8]
0024F597  48 8B B4 24 B8 00 00 00         mov rsi, qword ptr [rsp + 0xb8]
0024F59F  41 8B 57 04                     mov edx, dword ptr [r15 + 4]
0024F5A3  8D 42 01                        lea eax, [rdx + 1]
0024F5A6  41 89 47 04                     mov dword ptr [r15 + 4], eax
0024F5AA  49 8D 47 18                     lea rax, [r15 + 0x18]
0024F5AE  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
0024F5B2  48 39 01                        cmp qword ptr [rcx], rax
0024F5B5  0F 85 E8 FE FF FF               jne 0x14024f4a3
0024F5BB  49 89 06                        mov qword ptr [r14], rax
0024F5BE  49 89 4E 08                     mov qword ptr [r14 + 8], rcx
0024F5C2  4C 89 31                        mov qword ptr [rcx], r14
0024F5C5  4C 89 70 08                     mov qword ptr [rax + 8], r14
0024F5C9  85 D2                           test edx, edx
0024F5CB  75 11                           jne 0x14024f5de
0024F5CD  4D 39 6D 00                     cmp qword ptr [r13], r13
0024F5D1  74 0B                           je 0x14024f5de
0024F5D3  49 8B D7                        mov rdx, r15
0024F5D6  48 8B CE                        mov rcx, rsi
0024F5D9  E8 F2 6E 14 00                  call 0x1403964d0
0024F5DE  45 33 F6                        xor r14d, r14d
0024F5E1  F0 41 81 27 7F FF FF FF         lock and dword ptr [r15], 0xffffff7f
0024F5E9  48 8B 44 24 38                  mov rax, qword ptr [rsp + 0x38]
0024F5EE  33 D2                           xor edx, edx
0024F5F0  44 8B CD                        mov r9d, ebp
0024F5F3  88 44 24 20                     mov byte ptr [rsp + 0x20], al
0024F5F7  48 8B CE                        mov rcx, rsi
0024F5FA  44 8D 42 01                     lea r8d, [rdx + 1]
0024F5FE  E8 ED 26 00 00                  call 0x140251cf0
0024F603  40 32 F6                        xor sil, sil
0024F606  F6 05 F9 74 D7 00 01            test byte ptr [rip + 0xd774f9], 1
0024F60D  0F 85 52 01 00 00               jne 0x14024f765
0024F613  0F 0D 4C 24 48                  prefetchw byte ptr [rsp + 0x48]
0024F618  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
0024F61D  48 85 C0                        test rax, rax
0024F620  75 27                           jne 0x14024f649
0024F622  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
0024F627  48 8D 44 24 48                  lea rax, [rsp + 0x48]
0024F62C  F0 4C 0F B1 31                  lock cmpxchg qword ptr [rcx], r14
0024F631  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
0024F636  48 3B C1                        cmp rax, rcx
0024F639  0F 84 46 01 00 00               je 0x14024f785
0024F63F  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
0024F644  E8 57 84 FC FF                  call 0x140217aa0
0024F649  48 8D 48 08                     lea rcx, [rax + 8]
0024F64D  4C 89 74 24 48                  mov qword ptr [rsp + 0x48], r14
0024F652  48 8B 54 24 50                  mov rdx, qword ptr [rsp + 0x50]
0024F657  48 8B C2                        mov rax, rdx
0024F65A  48 87 01                        xchg qword ptr [rcx], rax
0024F65D  32 C2                           xor al, dl
0024F65F  A8 04                           test al, 4
0024F661  0F 84 1E 01 00 00               je 0x14024f785
0024F667  E8 B4 85 FC FF                  call 0x140217c20
0024F66C  E9 14 01 00 00                  jmp 0x14024f785
0024F671  83 F8 05                        cmp eax, 5
0024F674  0F 85 DE 03 00 00               jne 0x14024fa58
0024F67A  80 E1 FE                        and cl, 0xfe
0024F67D  80 C9 06                        or cl, 6
0024F680  88 4B 70                        mov byte ptr [rbx + 0x70], cl
0024F683  33 D2                           xor edx, edx
0024F685  E9 E0 FE FF FF                  jmp 0x14024f56a
0024F68A  48 01 8B E0 03 00 00            add qword ptr [rbx + 0x3e0], rcx
0024F691  E9 93 FE FF FF                  jmp 0x14024f529
0024F696  45 84 67 01                     test byte ptr [r15 + 1], r12b
0024F69A  B8 00 00 00 00                  mov eax, 0
0024F69F  0F 45 E8                        cmovne ebp, eax
0024F6A2  89 AC 24 A0 00 00 00            mov dword ptr [rsp + 0xa0], ebp
0024F6A9  E9 9B FD FF FF                  jmp 0x14024f449
0024F6AE  4C 89 30                        mov qword ptr [rax], r14
0024F6B1  45 32 E4                        xor r12b, r12b
0024F6B4  49 89 46 08                     mov qword ptr [r14 + 8], rax
0024F6B8  8B EA                           mov ebp, edx
0024F6BA  48 8B 5E 18                     mov rbx, qword ptr [rsi + 0x18]
0024F6BE  66 90                           nop
0024F6C0  F0 48 0F BA 6B 40 00            lock bts qword ptr [rbx + 0x40], 0
0024F6C7  0F 83 DD FD FF FF               jae 0x14024f4aa
0024F6CD  FF C5                           inc ebp
0024F6CF  85 2D D7 5B D7 00               test dword ptr [rip + 0xd75bd7], ebp
0024F6D5  0F 84 CD 01 00 00               je 0x14024f8a8
0024F6DB  F3 90                           pause
0024F6DD  48 8B 43 40                     mov rax, qword ptr [rbx + 0x40]
0024F6E1  48 85 C0                        test rax, rax
0024F6E4  74 DA                           je 0x14024f6c0
0024F6E6  EB E5                           jmp 0x14024f6cd
0024F6E8  8B 05 6A E7 CB 00               mov eax, dword ptr [rip + 0xcbe76a]
0024F6EE  85 C0                           test eax, eax
0024F6F0  0F 85 D8 FC FF FF               jne 0x14024f3ce
0024F6F6  48 8B D3                        mov rdx, rbx
0024F6F9  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
0024F6FE  E8 4D 61 02 00                  call 0x140275850
0024F703  E9 D7 FC FF FF                  jmp 0x14024f3df
0024F708  8B 83 1C 02 00 00               mov eax, dword ptr [rbx + 0x21c]
0024F70E  0F B6 C0                        movzx eax, al
0024F711  89 83 1C 02 00 00               mov dword ptr [rbx + 0x21c], eax
0024F717  F0 FF 84 82 18 02 00 00         lock inc dword ptr [rdx + rax*4 + 0x218]
0024F71F  E9 C4 FD FF FF                  jmp 0x14024f4e8
0024F724  41 0F B6 D4                     movzx edx, r12b
0024F728  40 0F B6 CE                     movzx ecx, sil
0024F72C  E8 CB 5F 2A 00                  call 0x1404f56fc
0024F731  E9 86 FC FF FF                  jmp 0x14024f3bc
0024F736  41 0F B6 D4                     movzx edx, r12b
0024F73A  0F B6 C8                        movzx ecx, al
0024F73D  E8 BA 5F 2A 00                  call 0x1404f56fc
0024F742  E9 D5 FC FF FF                  jmp 0x14024f41c
0024F747  48 8B B4 24 B8 00 00 00         mov rsi, qword ptr [rsp + 0xb8]
0024F74F  45 33 F6                        xor r14d, r14d
0024F752  8B AC 24 A0 00 00 00            mov ebp, dword ptr [rsp + 0xa0]
0024F759  4C 89 B7 A8 00 00 00            mov qword ptr [rdi + 0xa8], r14
0024F760  E9 7C FE FF FF                  jmp 0x14024f5e1
0024F765  8B 05 ED E6 CB 00               mov eax, dword ptr [rip + 0xcbe6ed]
0024F76B  85 C0                           test eax, eax
0024F76D  0F 85 A0 FE FF FF               jne 0x14024f613
0024F773  48 8B 94 24 98 00 00 00         mov rdx, qword ptr [rsp + 0x98]
0024F77B  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
0024F780  E8 6B 82 FC FF                  call 0x1402179f0
0024F785  83 3D 94 75 D7 00 00            cmp dword ptr [rip + 0xd77594], 0
0024F78C  0F B6 5C 24 58                  movzx ebx, byte ptr [rsp + 0x58]
0024F791  74 0C                           je 0x14024f79f
0024F793  44 0F 20 C1                     mov rcx, cr8
0024F797  0F B6 D3                        movzx edx, bl
0024F79A  E8 F9 5E 2A 00                  call 0x1404f5698
0024F79F  44 0F 22 C3                     mov cr8, rbx
0024F7A3  40 84 F6                        test sil, sil
0024F7A6  0F 84 E1 00 00 00               je 0x14024f88d
0024F7AC  8B 47 10                        mov eax, dword ptr [rdi + 0x10]
0024F7AF  48 8B B7 C0 00 00 00            mov rsi, qword ptr [rdi + 0xc0]
0024F7B6  A8 20                           test al, 0x20
0024F7B8  74 0E                           je 0x14024f7c8
0024F7BA  48 8B 4F 18                     mov rcx, qword ptr [rdi + 0x18]
0024F7BE  33 D2                           xor edx, edx
0024F7C0  E8 AB 30 93 00                  call 0x140b82870
0024F7C5  8B 47 10                        mov eax, dword ptr [rdi + 0x10]
0024F7C8  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
0024F7CC  48 85 C9                        test rcx, rcx
0024F7CF  0F 85 6B 02 00 00               jne 0x14024fa40
0024F7D5  48 8B 4F 50                     mov rcx, qword ptr [rdi + 0x50]
0024F7D9  48 85 C9                        test rcx, rcx
0024F7DC  0F 85 3A 02 00 00               jne 0x14024fa1c
0024F7E2  8B 47 10                        mov eax, dword ptr [rdi + 0x10]
0024F7E5  0F BA E0 0D                     bt eax, 0xd
0024F7E9  0F 83 80 00 00 00               jae 0x14024f86f
0024F7EF  48 8D 8E B8 00 00 00            lea rcx, [rsi + 0xb8]
0024F7F6  E8 75 8C FB FF                  call 0x140208470
0024F7FB  4C 8B 47 20                     mov r8, qword ptr [rdi + 0x20]
0024F7FF  48 8D 4F 20                     lea rcx, [rdi + 0x20]
0024F803  48 8B 51 08                     mov rdx, qword ptr [rcx + 8]
0024F807  0F B6 E8                        movzx ebp, al
0024F80A  49 39 48 08                     cmp qword ptr [r8 + 8], rcx
0024F80E  0F 85 8F FC FF FF               jne 0x14024f4a3
0024F814  48 39 0A                        cmp qword ptr [rdx], rcx
0024F817  0F 85 86 FC FF FF               jne 0x14024f4a3
0024F81D  4C 89 02                        mov qword ptr [rdx], r8
0024F820  49 89 50 08                     mov qword ptr [r8 + 8], rdx
0024F824  41 B8 49 6F 43 70               mov r8d, 0x70436f49
0024F82A  48 89 49 08                     mov qword ptr [rcx + 8], rcx
0024F82E  48 89 09                        mov qword ptr [rcx], rcx
0024F831  48 8B 57 58                     mov rdx, qword ptr [rdi + 0x58]
0024F835  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0024F83E  48 83 E2 F9                     and rdx, 0xfffffffffffffff9
0024F842  48 81 C1 90 07 00 00            add rcx, 0x790
0024F849  E8 A2 DD 19 00                  call 0x1403ed5f0
0024F84E  8B 47 10                        mov eax, dword ptr [rdi + 0x10]
0024F851  48 8D 8E B8 00 00 00            lea rcx, [rsi + 0xb8]
0024F858  0F BA F0 0D                     btr eax, 0xd
0024F85C  40 0F B6 D5                     movzx edx, bpl
0024F860  0F BA E8 0F                     bts eax, 0xf
0024F864  89 47 10                        mov dword ptr [rdi + 0x10], eax
0024F867  E8 34 33 14 00                  call 0x140392ba0
0024F86C  8B 47 10                        mov eax, dword ptr [rdi + 0x10]
0024F86F  48 85 F6                        test rsi, rsi
0024F872  0F 85 B4 00 00 00               jne 0x14024f92c
0024F878  F7 47 10 00 80 00 00            test dword ptr [rdi + 0x10], 0x8000
0024F87F  0F 85 EF 00 00 00               jne 0x14024f974
0024F885  48 8B CF                        mov rcx, rdi
0024F888  E8 E3 E6 FF FF                  call 0x14024df70
0024F88D  B0 01                           mov al, 1
0024F88F  48 8B 9C 24 A8 00 00 00         mov rbx, qword ptr [rsp + 0xa8]
0024F897  48 83 C4 60                     add rsp, 0x60
0024F89B  41 5F                           pop r15
0024F89D  41 5E                           pop r14
0024F89F  41 5D                           pop r13
0024F8A1  41 5C                           pop r12
0024F8A3  5F                              pop rdi
0024F8A4  5E                              pop rsi
0024F8A5  5D                              pop rbp
0024F8A6  C3                              ret
0024F8A7  CC                              int3
0024F8A8  8B 05 0A 72 D7 00               mov eax, dword ptr [rip + 0xd7720a]
0024F8AE  A8 40                           test al, 0x40
0024F8B0  0F 84 25 FE FF FF               je 0x14024f6db
0024F8B6  E8 D5 FB 0B 00                  call 0x14030f490
0024F8BB  84 C0                           test al, al
0024F8BD  0F 84 18 FE FF FF               je 0x14024f6db
0024F8C3  8B CD                           mov ecx, ebp
0024F8C5  E8 96 FB 0B 00                  call 0x14030f460
0024F8CA  E9 0E FE FF FF                  jmp 0x14024f6dd
0024F8CF  48 8B CB                        mov rcx, rbx
0024F8D2  E8 49 6E 14 00                  call 0x140396720
0024F8D7  44 0F B6 C0                     movzx r8d, al
0024F8DB  48 8B CB                        mov rcx, rbx
0024F8DE  49 8B D6                        mov rdx, r14
0024F8E1  E8 66 6E 14 00                  call 0x14039674c
0024F8E6  E9 56 FB FF FF                  jmp 0x14024f441
0024F8EB  83 4B 74 02                     or dword ptr [rbx + 0x74], 2
0024F8EF  E9 35 FC FF FF                  jmp 0x14024f529
0024F8F4  80 BB 83 02 00 00 0F            cmp byte ptr [rbx + 0x283], 0xf
0024F8FB  0F 85 78 FB FF FF               jne 0x14024f479
0024F901  E9 99 FC FF FF                  jmp 0x14024f59f
0024F906  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
0024F90B  E8 A0 85 00 00                  call 0x140257eb0
0024F910  E9 CA FA FF FF                  jmp 0x14024f3df
0024F915  48 8B CF                        mov rcx, rdi
0024F918  E8 77 D7 1A 00                  call 0x1403fd094
0024F91D  84 C0                           test al, al
0024F91F  0F 84 8A 00 00 00               je 0x14024f9af
0024F925  32 C0                           xor al, al
0024F927  E9 63 FF FF FF                  jmp 0x14024f88f
0024F92C  84 C0                           test al, al
0024F92E  0F 88 44 FF FF FF               js 0x14024f878
0024F934  BA 01 00 00 00                  mov edx, 1
0024F939  41 B8 44 66 6C 74               mov r8d, 0x746c6644
0024F93F  48 8B CE                        mov rcx, rsi
0024F942  E8 79 D2 1E 00                  call 0x14043cbc0
0024F947  E9 2C FF FF FF                  jmp 0x14024f878
0024F94C  8B 49 30                        mov ecx, dword ptr [rcx + 0x30]
0024F94F  8B C1                           mov eax, ecx
0024F951  25 00 00 00 C0                  and eax, 0xc0000000
0024F956  3D 00 00 00 C0                  cmp eax, 0xc0000000
0024F95B  74 C8                           je 0x14024f925
0024F95D  F7 42 50 00 00 00 02            test dword ptr [rdx + 0x50], 0x2000000
0024F964  0F 84 F8 F9 FF FF               je 0x14024f362
0024F96A  85 C9                           test ecx, ecx
0024F96C  0F 88 F0 F9 FF FF               js 0x14024f362
0024F972  EB B1                           jmp 0x14024f925
0024F974  48 8B 47 58                     mov rax, qword ptr [rdi + 0x58]
0024F978  4C 8B C8                        mov r9, rax
0024F97B  48 8B C8                        mov rcx, rax
0024F97E  49 D1 E9                        shr r9, 1
0024F981  48 83 E1 F9                     and rcx, 0xfffffffffffffff9
0024F985  41 83 E1 03                     and r9d, 3
0024F989  4C 8B C0                        mov r8, rax
0024F98C  49 FF C9                        dec r9
0024F98F  4B 8D 14 09                     lea rdx, [r9 + r9]
0024F993  48 0B D1                        or rdx, rcx
0024F996  F0 48 0F B1 57 58               lock cmpxchg qword ptr [rdi + 0x58], rdx
0024F99C  4C 3B C0                        cmp r8, rax
0024F99F  75 D7                           jne 0x14024f978
0024F9A1  45 85 C9                        test r9d, r9d
0024F9A4  0F 85 E3 FE FF FF               jne 0x14024f88d
0024F9AA  E9 D6 FE FF FF                  jmp 0x14024f885
0024F9AF  48 8D 44 24 30                  lea rax, [rsp + 0x30]
0024F9B4  4C 8D 8F C0 00 00 00            lea r9, [rdi + 0xc0]
0024F9BB  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0024F9C0  48 8D 4F 78                     lea rcx, [rdi + 0x78]
0024F9C4  4C 8D 44 24 30                  lea r8, [rsp + 0x30]
0024F9C9  48 8D 54 24 40                  lea rdx, [rsp + 0x40]
0024F9CE  E8 7D B5 FB FF                  call 0x14020af50
0024F9D3  E9 B5 FE FF FF                  jmp 0x14024f88d
0024F9D8  83 F8 04                        cmp eax, 4
0024F9DB  0F 84 EA FA FF FF               je 0x14024f4cb
0024F9E1  85 C0                           test eax, eax
0024F9E3  0F 85 88 FC FF FF               jne 0x14024f671
0024F9E9  80 E1 FA                        and cl, 0xfa
0024F9EC  48 8D 87 A8 00 00 00            lea rax, [rdi + 0xa8]
0024F9F3  80 C9 02                        or cl, 2
0024F9F6  41 B4 01                        mov r12b, 1
0024F9F9  88 4B 70                        mov byte ptr [rbx + 0x70], cl
0024F9FC  33 D2                           xor edx, edx
0024F9FE  48 89 83 C8 00 00 00            mov qword ptr [rbx + 0xc8], rax
0024FA05  48 89 93 D0 03 00 00            mov qword ptr [rbx + 0x3d0], rdx
0024FA0C  88 56 11                        mov byte ptr [rsi + 0x11], dl
0024FA0F  E9 56 FB FF FF                  jmp 0x14024f56a
0024FA14  40 B6 01                        mov sil, 1
0024FA17  E9 EA FB FF FF                  jmp 0x14024f606
0024FA1C  48 85 F6                        test rsi, rsi
0024FA1F  0F 84 BD FD FF FF               je 0x14024f7e2
0024FA25  A8 04                           test al, 4
0024FA27  0F 85 B5 FD FF FF               jne 0x14024f7e2
0024FA2D  BA 44 66 6C 74                  mov edx, 0x746c6644
0024FA32  E8 A9 7E 0A 00                  call 0x1402f78e0
0024FA37  E9 A6 FD FF FF                  jmp 0x14024f7e2
0024FA3C  0F 1F 40 00                     nop dword ptr [rax]
0024FA40  48 8B 19                        mov rbx, qword ptr [rcx]
0024FA43  E8 38 F0 04 00                  call 0x14029ea80
0024FA48  48 8B CB                        mov rcx, rbx
0024FA4B  48 85 DB                        test rbx, rbx
0024FA4E  75 F0                           jne 0x14024fa40
0024FA50  8B 47 10                        mov eax, dword ptr [rdi + 0x10]
0024FA53  E9 7D FD FF FF                  jmp 0x14024f7d5
0024FA58  33 D2                           xor edx, edx
0024FA5A  83 F8 03                        cmp eax, 3
0024FA5D  0F 85 07 FB FF FF               jne 0x14024f56a
0024FA63  C6 46 11 02                     mov byte ptr [rsi + 0x11], 2
0024FA67  E9 FE FA FF FF                  jmp 0x14024f56a
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopCompleteIrpInFileObjectList(__int64 a1, __int64 a2, unsigned __int8 a3)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_rbp;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int8 v_stack_m78;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned int v_stack_p8;

    v_stack_p10 = v_rbx;
    v_rsp = (v_rsp) - (96);
    v_r14 = 0;
    v_stack_m58 = 0;
    v_stack_m68 = 0;
    if ((*(unsigned __int8 *)(a1 + 65)) == 0) goto loc_0024F94C;
loc_0024F362:
    if (*(unsigned __int64 *)(a2 + 176) == 0) goto loc_0024F915;
    a1 = 0;
    v_stack_m50 = v_xmm0;
    v_stack_m40 = 0;
    *(unsigned __int64 *)(a1 + 120) = *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 176) + 8);
    *(unsigned int *)(a1 + 184) = 0;
    v_stack_m50 = 0;
    v_stack_m48 = *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 176)) + 64;
    if ((*(unsigned int *)(v_rip + 14121322)) != 0) goto loc_0024F724;
loc_0024F3BC:
    v_stack_m40 = (unsigned __int8)(v_cr8);
    if (((*(unsigned __int8 *)(v_rip + 14120771)) & (33)) != 0) goto loc_0024F6E8;
loc_0024F3CE:
    if (v_stack_m50 != 0) goto loc_0024F906;
loc_0024F3DF:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 176)) + 72)) != 0) goto loc_0024FA14;
    v_stack_p8 = (unsigned int)((__int8)(a3));
    v_stack_m60 = 2;
    if ((*(unsigned int *)(v_rip + 14121226)) != 0) goto loc_0024F736;
loc_0024F41C:
    v_stack_p20 = *(unsigned __int64 *)(gs_base + (0 + 32));
    if (((*(unsigned int *)(v_rip + 14120661)) & (0x1000000ULL)) != 0) goto loc_0024F8CF;
loc_0024F441:
    if ((unsigned int)((__int8)(a3)) != 0) goto loc_0024F696;
loc_0024F449:
    result = KiAcquireKobjectLockSafe(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 176)), v_stack_m50, a3, a4);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 176)) + 8)) == (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 176)) + 8)) goto loc_0024F59F;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 176)) + 40)))) >= (*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 176)) + 44))) goto loc_0024F59F;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 232)) == (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 176)))) goto loc_0024F8F4;
loc_0024F479:
    a2 = 0;
loc_0024F480:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 176)) + 8) + 16)) != 3) goto loc_0024F589;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 176)) + 8)) + 8)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 176)) + 8))) goto loc_0024F4A3;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 176)) + 8) + 8))) == (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 176)) + 8))) goto loc_0024F6AE;
loc_0024F4A3:
loc_0024F4AA:
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 388))) != 5) goto loc_0024F683;
    result = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 112)))) & (7));
    if (((unsigned int)(result)) != 1) goto loc_0024F9D8;
loc_0024F4CB:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 232) == 0) goto loc_0024F4E8;
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 232))) & (127));
    if (((unsigned __int8)(result)) == 21) goto loc_0024F708;
loc_0024F4E8:
    result = KiRemovePrcbWaitEntry(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 232), a3, a4);
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 388))) == 1) goto loc_0024F8EB;
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 388))) != 5) goto loc_0024F529;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 388)))) - (*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 436)));
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 391)) == 2) goto loc_0024F68A;
loc_0024F529:
    *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 388) = 7;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 216) = *(unsigned __int64 *)(v_stack_p20 + 11528);
    *(unsigned __int64 *)(v_stack_p20 + 11528) = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 216;
    a2 = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 200) = a1 + 168;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 976) = 0;
loc_0024F56A:
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 64) = 0;
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 176)) + 8) + 17)) + 1);
    *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 176)) + 8) + 17) = (unsigned __int8)(result);
    if (1 != 0) goto loc_0024F747;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 176)) + 8))) != (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 176)) + 8)) goto loc_0024F480;
loc_0024F589:
loc_0024F59F:
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 176)) + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 176)) + 4)) + 1);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 176)) + 24 + 8))) != (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 176)) + 24)) goto loc_0024F4A3;
    *(unsigned __int64 *)(a1 + 168) = *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 176)) + 24;
    *(unsigned __int64 *)(a1 + 168 + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 176)) + 24 + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 176)) + 24 + 8)) = a1 + 168;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 176)) + 24 + 8) = a1 + 168;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 176)) + 4))) != 0) goto loc_0024F5DE;
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 176)) + 24;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 176)) + 8)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 176)) + 8)) {
        a2 = *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 176));
        a1 = v_stack_p20;
        result = KiWakeOtherQueueWaiters(a1, a2, a3, a4);
    }
    v_r14 = 0;
loc_0024F5E1:
    a2 = 0;
    v_stack_m78 = (unsigned __int8)(v_stack_m60);
    result = KiExitDispatcher(v_stack_p20, a2, a2 + 1, (unsigned int)((unsigned int)((unsigned int)(v_stack_p8))));
    v_rsi = 0;
loc_0024F606:
    if (((*(unsigned __int8 *)(v_rip + 14120185)) & (1)) != 0) goto loc_0024F765;
loc_0024F613:
    if (v_stack_m50 != 0) goto loc_0024F649;
    if (v_stack_m50 == v_stack_m50) goto loc_0024F785;
    result = KxWaitForLockChainValid(v_stack_m50, a2, a2 + 1, (unsigned int)((unsigned int)((unsigned int)(v_stack_p8))));
loc_0024F649:
    v_stack_m50 = 0;
    result = (unsigned __int8)((v_stack_m48) ^ ((unsigned __int8)(v_stack_m48)));
    if ((((unsigned __int8)(result)) & (4)) == 0) goto loc_0024F785;
    result = KeWakeAddressAll(result + 8, v_stack_m48, a2 + 1, (unsigned int)((unsigned int)((unsigned int)(v_stack_p8))));
    goto loc_0024F785;
loc_0024F671:
    if (((unsigned int)(result)) != 5) goto loc_0024FA58;
    a1 = (unsigned __int8)((result + 8) & (254));
    a1 = (unsigned __int8)((a1) | (6));
    *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 112) = (unsigned __int8)(a1);
loc_0024F683:
    a2 = 0;
    goto loc_0024F56A;
loc_0024F68A:
    goto loc_0024F529;
loc_0024F696:
    v_rbp = (unsigned int)(v_stack_p8);
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 176)) + 1)) & (1)) != 0) { v_rbp = 0; }
    v_stack_p8 = (unsigned int)(v_rbp);
    goto loc_0024F449;
loc_0024F6AE:
    *(unsigned __int64 *)(0) = 0;
    v_r12 = 0;
    *(unsigned __int64 *)(v_r14 + 8) = 0;
loc_0024F6C0:
    if (condition_is_above_or_equal) goto loc_0024F4AA;
loc_0024F6CD:
    v_rbp = (unsigned int)((0) + 1);
    if (((*(unsigned int *)(v_rip + 14113751)) & ((unsigned int)(v_rbp))) == 0) goto loc_0024F8A8;
loc_0024F6DB:
loc_0024F6DD:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 24) + 64) == 0) goto loc_0024F6C0;
    goto loc_0024F6CD;
loc_0024F6E8:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13363050))) != 0) goto loc_0024F3CE;
    result = KiAcquireQueuedSpinLockInstrumented(v_stack_m50, *(unsigned __int64 *)(v_rsi + 24), a2 + 1, (unsigned int)((unsigned int)((unsigned int)(v_stack_p8))));
    goto loc_0024F3DF;
loc_0024F708:
    *(unsigned int *)(*(unsigned __int64 *)(v_rsi + 24) + 540) = (unsigned int)((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsi + 24) + 540))));
    goto loc_0024F4E8;
loc_0024F724:
    result = KiRaiseIrqlProcessIrqlFlags(0, 0, a2 + 1, (unsigned int)((unsigned int)((unsigned int)(v_stack_p8))));
    goto loc_0024F3BC;
loc_0024F736:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(result), 0, a2 + 1, (unsigned int)((unsigned int)((unsigned int)(v_stack_p8))));
    goto loc_0024F41C;
loc_0024F747:
    v_r14 = 0;
    *(unsigned __int64 *)(a1 + 168) = 0;
    goto loc_0024F5E1;
loc_0024F765:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13362925))) != 0) goto loc_0024F613;
    result = KiReleaseQueuedSpinLockInstrumented(v_stack_m50, v_stack_p0, a2 + 1, (unsigned int)((unsigned int)((unsigned int)(v_stack_p8))));
loc_0024F785:
    if ((*(unsigned int *)(v_rip + 14120340)) != 0) {
        a1 = 2;
        a2 = (unsigned __int8)(v_stack_m40);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, a2 + 1, (unsigned int)((unsigned int)((unsigned int)(v_stack_p8))));
    }
    if ((unsigned __int8)(v_stack_p20) == 0) goto loc_0024F88D;
    result = (unsigned int)(*(unsigned int *)(a1 + 16));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 16)))) & (32)) != 0) {
        a1 = *(unsigned __int64 *)(a1 + 24);
        a2 = 0;
        result = ExFreePoolWithTag(a1, a2, a2 + 1, (unsigned int)((unsigned int)((unsigned int)(v_stack_p8))));
        result = *(unsigned int *)(a1 + 16);
    }
    if (*(unsigned __int64 *)(a1 + 8) != 0) goto loc_0024FA40;
loc_0024F7D5:
    if (*(unsigned __int64 *)(a1 + 80) != 0) goto loc_0024FA1C;
loc_0024F7E2:
    if (condition_is_above_or_equal) goto loc_0024F86F;
    result = KeAcquireSpinLockRaiseToDpc(*(unsigned __int64 *)(a1 + 192) + 184, a2, a2 + 1, (unsigned int)((unsigned int)((unsigned int)(v_stack_p8))));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 8)) != (a1 + 32)) goto loc_0024F4A3;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32 + 8))) != (a1 + 32)) goto loc_0024F4A3;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32 + 8)) = *(unsigned __int64 *)(a1 + 32);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 8) = *(unsigned __int64 *)(a1 + 32 + 8);
    *(unsigned __int64 *)(a1 + 32 + 8) = a1 + 32;
    *(unsigned __int64 *)(a1 + 32) = a1 + 32;
    a2 = (*(unsigned __int64 *)(a1 + 88)) & (-7);
    a1 = (*(unsigned __int64 *)(gs_base + (0 + 392))) + (0x790ULL);
    result = ObFastDereferenceObject(a1, a2, (unsigned int)(0x70436F49ULL), (unsigned int)((unsigned int)((unsigned int)(v_stack_p8))));
    *(unsigned int *)(a1 + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 16)));
    result = KeReleaseSpinLock(*(unsigned __int64 *)(a1 + 192) + 184, (unsigned __int8)((unsigned __int8)(result)), (unsigned int)(0x70436F49ULL), (unsigned int)((unsigned int)((unsigned int)(v_stack_p8))));
loc_0024F86F:
    if (*(unsigned __int64 *)(a1 + 192) != 0) goto loc_0024F92C;
loc_0024F878:
    if (((*(unsigned int *)(a1 + 16)) & (0x8000ULL)) != 0) goto loc_0024F974;
loc_0024F885:
    result = IoFreeIrp(a1, (unsigned __int8)((unsigned __int8)(result)), (unsigned int)(0x70436F49ULL), (unsigned int)((unsigned int)((unsigned int)(v_stack_p8))));
loc_0024F88D:
loc_0024F88F:
    v_rsp = (v_rsp) + (96);
    return 1;
loc_0024F8A8:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14119434)))) & (64)) == 0) goto loc_0024F6DB;
    result = KiCheckVpBackingLongSpinWaitHypercall(a1, (unsigned __int8)((unsigned __int8)(result)), (unsigned int)(0x70436F49ULL), (unsigned int)((unsigned int)((unsigned int)(v_stack_p8))));
    if ((unsigned __int8)(result) == 0) goto loc_0024F6DB;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)((unsigned __int8)(result))), (unsigned __int8)((unsigned __int8)(result)), (unsigned int)(0x70436F49ULL), (unsigned int)((unsigned int)((unsigned int)(v_stack_p8))));
    goto loc_0024F6DD;
loc_0024F8CF:
    result = KeIsThreadRunning(v_stack_p10, (unsigned __int8)((unsigned __int8)(result)), (unsigned int)(0x70436F49ULL), (unsigned int)((unsigned int)((unsigned int)(v_stack_p8))));
    result = EtwTraceEnqueueWork(v_stack_p10, 0, (unsigned __int8)(result), (unsigned int)((unsigned int)((unsigned int)(v_stack_p8))));
    goto loc_0024F441;
loc_0024F8EB:
    goto loc_0024F529;
loc_0024F8F4:
    if ((*(unsigned __int8 *)(v_stack_p10 + 643)) != 15) goto loc_0024F479;
    goto loc_0024F59F;
loc_0024F906:
    result = KxWaitForLockOwnerShip(v_stack_p48, 0, (unsigned __int8)(result), (unsigned int)((unsigned int)((unsigned int)(v_stack_p8))));
    goto loc_0024F3DF;
loc_0024F915:
    result = IopDoesCompletionNeedsApc(a1, 0, (unsigned __int8)(result), (unsigned int)((unsigned int)((unsigned int)(v_stack_p8))));
    if ((unsigned __int8)(result) == 0) goto loc_0024F9AF;
loc_0024F925:
    result = 0;
    goto loc_0024F88F;
loc_0024F92C:
    if (sign_flag) goto loc_0024F878;
    result = ObDereferenceObjectExWithTag(*(unsigned __int64 *)(a1 + 192), 1, (unsigned int)(0x746C6644ULL), (unsigned int)((unsigned int)((unsigned int)(v_stack_p8))));
    goto loc_0024F878;
loc_0024F94C:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 192) + 48))))) & (0xC0000000ULL));
    if (((unsigned int)(result)) == 0xC0000000ULL) goto loc_0024F925;
    if (((*(unsigned int *)(1 + 80)) & (0x2000000ULL)) == 0) goto loc_0024F362;
    if (sign_flag) goto loc_0024F362;
    goto loc_0024F925;
loc_0024F974:
loc_0024F978:
    a4 = (*(unsigned __int64 *)(a1 + 88)) >> (1);
    a1 = (*(unsigned __int64 *)(a1 + 88)) & (-7);
    a4 = (unsigned int)((a4) & (3));
    a4 = (a4) - 1;
    a2 = (a4 + a4 * 1) | (a1);
    if ((*(unsigned __int64 *)(a1 + 88)) != (*(unsigned __int64 *)(a1 + 88))) goto loc_0024F978;
    if ((unsigned int)(a4) != 0) goto loc_0024F88D;
    goto loc_0024F885;
loc_0024F9AF:
    v_stack_p20 = v_stack_p30;
    result = IopCompleteRequest(a1 + 120, v_stack_p40, v_stack_p30, a1 + 192);
    goto loc_0024F88D;
loc_0024F9D8:
    if (((unsigned int)(result)) == 4) goto loc_0024F4CB;
    if ((unsigned int)(result) != 0) goto loc_0024F671;
    a1 = (unsigned __int8)((a1 + 120) & (250));
    a1 = (unsigned __int8)((a1) | (2));
    *(unsigned __int8 *)(v_stack_p10 + 112) = (unsigned __int8)(a1);
    a2 = 0;
    *(unsigned __int64 *)(v_stack_p10 + 200) = a1 + 168;
    *(unsigned __int64 *)(v_stack_p10 + 976) = 0;
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 192) + 17) = 0;
    goto loc_0024F56A;
loc_0024FA14:
    goto loc_0024F606;
loc_0024FA1C:
    if (1 == 0) goto loc_0024F7E2;
    if ((((unsigned __int8)(a1 + 168)) & (4)) != 0) goto loc_0024F7E2;
    result = ObfDereferenceObjectWithTag(a1, (unsigned int)(0x746C6644ULL), v_stack_p30, a1 + 192);
    goto loc_0024F7E2;
loc_0024FA40:
    result = IoFreeMdl(a1, (unsigned int)(0x746C6644ULL), v_stack_p30, a1 + 192);
    if (*(unsigned __int64 *)(a1) != 0) goto loc_0024FA40;
    goto loc_0024F7D5;
loc_0024FA58:
    a2 = 0;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 16)))) != 3) goto loc_0024F56A;
    *(unsigned __int8 *)(1 + 17) = 2;
    goto loc_0024F56A;
}
```

## 5. (Beta) C Style

```c
int64_t IopCompleteIrpInFileObjectList(void *Arg1, void *Arg2, uint8_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_rbp;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint8_t v_stack_m78;
    uint64_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p20;
    uint64_t v_stack_p30;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint32_t v_stack_p8;

    v_stack_p10 = local_rbx;
    local_rsp = (local_rsp) - (96);
    local_r14 = 0;
    v_stack_m58 = 0;
    v_stack_m68 = 0;
    if ((*(uint8_t *)(arg1 + 0x41)) == 0) goto loc_0024F94C;
loc_0024F362:
    if (*(uint64_t *)(arg2 + 0xB0) == 0) goto loc_0024F915;
    Arg1 = 0;
    v_stack_m50 = v_xmm0;
    v_stack_m40 = 0;
    *(uint64_t *)(arg1 + 0x78) = *(uint64_t *)(*(uint64_t *)(arg2 + 0xB0) + 0x8);
    *(uint32_t *)(arg1 + 0xB8) = 0;
    v_stack_m50 = 0;
    v_stack_m48 = *(uint64_t *)(*(uint64_t *)(arg2 + 0xB0)) + 64;
    if ((*(uint32_t *)(v_rip + 0xD7796A)) != 0) goto loc_0024F724;
loc_0024F3BC:
    v_stack_m40 = (uint8_t)(v_cr8);
    if (((*(uint8_t *)(v_rip + 0xD77743)) & (33)) != 0) goto loc_0024F6E8;
loc_0024F3CE:
    if (v_stack_m50 != 0) goto loc_0024F906;
loc_0024F3DF:
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0xB0)) + 0x48)) != 0) goto loc_0024FA14;
    v_stack_p8 = (uint32_t)((int8_t)(Arg3));
    v_stack_m60 = 2;
    if ((*(uint32_t *)(v_rip + 0xD7790A)) != 0) goto loc_0024F736;
loc_0024F41C:
    v_stack_p20 = *(uint64_t *)(gs_base + (0 + 0x20));
    if (((*(uint32_t *)(v_rip + 0xD776D5)) & (0x1000000ULL)) != 0) goto loc_0024F8CF;
loc_0024F441:
    if ((uint32_t)((int8_t)(Arg3)) != 0) goto loc_0024F696;
loc_0024F449:
    result = KiAcquireKobjectLockSafe(*(uint64_t *)(*(uint64_t *)(arg2 + 0xB0)), v_stack_m50, Arg3, a4);
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0xB0)) + 0x8)) == (*(uint64_t *)(*(uint64_t *)(arg2 + 0xB0)) + 8)) goto loc_0024F59F;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0xB0)) + 0x28)))) >= (*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0xB0)) + 0x2C))) goto loc_0024F59F;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0xE8)) == (*(uint64_t *)(*(uint64_t *)(arg2 + 0xB0)))) goto loc_0024F8F4;
loc_0024F479:
    Arg2 = 0;
loc_0024F480:
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0xB0)) + 0x8) + 0x10)) != 3) goto loc_0024F589;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0xB0)) + 0x8)) + 0x8)) != (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0xB0)) + 0x8))) goto loc_0024F4A3;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0xB0)) + 0x8) + 0x8))) == (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0xB0)) + 0x8))) goto loc_0024F6AE;
loc_0024F4A3:
loc_0024F4AA:
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0x184))) != 5) goto loc_0024F683;
    result = (uint32_t)(((uint32_t)((uint32_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0x70)))) & (7));
    if (((uint32_t)(result)) != 1) goto loc_0024F9D8;
loc_0024F4CB:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0xE8) == 0) goto loc_0024F4E8;
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0xE8))) & (127));
    if (((uint8_t)(result)) == 21) goto loc_0024F708;
loc_0024F4E8:
    result = KiRemovePrcbWaitEntry(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0xE8), Arg3, a4);
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0x184))) == 1) goto loc_0024F8EB;
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0x184))) != 5) goto loc_0024F529;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0x184)))) - (*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0x1B4)));
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0x187)) == 2) goto loc_0024F68A;
loc_0024F529:
    *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0x184) = 7;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0xD8) = *(uint64_t *)(v_stack_p20 + 0x2D08);
    *(uint64_t *)(v_stack_p20 + 0x2D08) = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 216;
    Arg2 = 0;
    *(void **)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0xC8) = Arg1 + 168;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0x3D0) = 0;
loc_0024F56A:
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0x40) = 0;
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0xB0)) + 0x8) + 0x11)) + 1);
    *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0xB0)) + 0x8) + 0x11) = (uint8_t)(result);
    if (1 != 0) goto loc_0024F747;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0xB0)) + 0x8))) != (*(uint64_t *)(*(uint64_t *)(arg2 + 0xB0)) + 8)) goto loc_0024F480;
loc_0024F589:
loc_0024F59F:
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0xB0)) + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0xB0)) + 0x4)) + 1);
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0xB0)) + 0x18 + 0x8))) != (*(uint64_t *)(*(uint64_t *)(arg2 + 0xB0)) + 24)) goto loc_0024F4A3;
    *(uint64_t *)(arg1 + 0xA8) = *(uint64_t *)(*(uint64_t *)(arg2 + 0xB0)) + 24;
    *(uint64_t *)(arg1 + 0xA8 + 0x8) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0xB0)) + 0x18 + 0x8);
    *(void **)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0xB0)) + 0x18 + 0x8)) = Arg1 + 168;
    *(void **)(*(uint64_t *)(*(uint64_t *)(arg2 + 0xB0)) + 0x18 + 0x8) = Arg1 + 168;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0xB0)) + 0x4))) != 0) goto loc_0024F5DE;
    result = *(uint64_t *)(*(uint64_t *)(arg2 + 0xB0)) + 24;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0xB0)) + 0x8)) != (*(uint64_t *)(*(uint64_t *)(arg2 + 0xB0)) + 8)) {
        Arg2 = *(uint64_t *)(*(uint64_t *)(arg2 + 0xB0));
        Arg1 = v_stack_p20;
        result = KiWakeOtherQueueWaiters(Arg1, Arg2, Arg3, a4);
    }
    local_r14 = 0;
loc_0024F5E1:
    Arg2 = 0;
    v_stack_m78 = (uint8_t)(v_stack_m60);
    result = KiExitDispatcher(v_stack_p20, Arg2, Arg2 + 1, (uint32_t)((uint32_t)((uint32_t)(v_stack_p8))));
    local_rsi = 0;
loc_0024F606:
    if (((*(uint8_t *)(v_rip + 0xD774F9)) & (1)) != 0) goto loc_0024F765;
loc_0024F613:
    if (v_stack_m50 != 0) goto loc_0024F649;
    if (v_stack_m50 == v_stack_m50) goto loc_0024F785;
    result = KxWaitForLockChainValid(v_stack_m50, Arg2, Arg2 + 1, (uint32_t)((uint32_t)((uint32_t)(v_stack_p8))));
loc_0024F649:
    v_stack_m50 = 0;
    result = (uint8_t)((v_stack_m48) ^ ((uint8_t)(v_stack_m48)));
    if ((((uint8_t)(result)) & (4)) == 0) goto loc_0024F785;
    result = KeWakeAddressAll(result + 8, v_stack_m48, Arg2 + 1, (uint32_t)((uint32_t)((uint32_t)(v_stack_p8))));
    goto loc_0024F785;
loc_0024F671:
    if (((uint32_t)(result)) != 5) goto loc_0024FA58;
    Arg1 = (uint8_t)((result + 8) & (254));
    Arg1 = (uint8_t)((Arg1) | (6));
    *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0x70) = (uint8_t)(Arg1);
loc_0024F683:
    Arg2 = 0;
    goto loc_0024F56A;
loc_0024F68A:
    goto loc_0024F529;
loc_0024F696:
    local_rbp = (uint32_t)(v_stack_p8);
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0xB0)) + 0x1)) & (1)) != 0) { local_rbp = 0; }
    v_stack_p8 = (uint32_t)(local_rbp);
    goto loc_0024F449;
loc_0024F6AE:
    *(uint64_t *)(0) = 0;
    local_r12 = 0;
    *(uint64_t *)(local_r14 + 0x8) = 0;
loc_0024F6C0:
    if (condition_is_above_or_equal) goto loc_0024F4AA;
loc_0024F6CD:
    local_rbp = (uint32_t)((0) + 1);
    if (((*(uint32_t *)(v_rip + 0xD75BD7)) & ((uint32_t)(local_rbp))) == 0) goto loc_0024F8A8;
loc_0024F6DB:
loc_0024F6DD:
    if (*(uint64_t *)(*(uint64_t *)(local_rsi + 0x18) + 0x40) == 0) goto loc_0024F6C0;
    goto loc_0024F6CD;
loc_0024F6E8:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCBE76A))) != 0) goto loc_0024F3CE;
    result = KiAcquireQueuedSpinLockInstrumented(v_stack_m50, *(uint64_t *)(local_rsi + 0x18), Arg2 + 1, (uint32_t)((uint32_t)((uint32_t)(v_stack_p8))));
    goto loc_0024F3DF;
loc_0024F708:
    *(uint32_t *)(*(uint64_t *)(local_rsi + 0x18) + 0x21C) = (uint32_t)((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsi + 0x18) + 0x21C))));
    goto loc_0024F4E8;
loc_0024F724:
    result = KiRaiseIrqlProcessIrqlFlags(0, 0, Arg2 + 1, (uint32_t)((uint32_t)((uint32_t)(v_stack_p8))));
    goto loc_0024F3BC;
loc_0024F736:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(result), 0, Arg2 + 1, (uint32_t)((uint32_t)((uint32_t)(v_stack_p8))));
    goto loc_0024F41C;
loc_0024F747:
    local_r14 = 0;
    *(uint64_t *)(arg1 + 0xA8) = 0;
    goto loc_0024F5E1;
loc_0024F765:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCBE6ED))) != 0) goto loc_0024F613;
    result = KiReleaseQueuedSpinLockInstrumented(v_stack_m50, v_stack_p0, Arg2 + 1, (uint32_t)((uint32_t)((uint32_t)(v_stack_p8))));
loc_0024F785:
    if ((*(uint32_t *)(v_rip + 0xD77594)) != 0) {
        Arg1 = 2;
        Arg2 = (uint8_t)(v_stack_m40);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, Arg2 + 1, (uint32_t)((uint32_t)((uint32_t)(v_stack_p8))));
    }
    if ((uint8_t)(v_stack_p20) == 0) goto loc_0024F88D;
    result = (uint32_t)(*(uint32_t *)(arg1 + 0x10));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x10)))) & (32)) != 0) {
        Arg1 = *(uint64_t *)(arg1 + 0x18);
        Arg2 = 0;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg2 + 1, (uint32_t)((uint32_t)((uint32_t)(v_stack_p8))));
        result = *(uint32_t *)(arg1 + 0x10);
    }
    if (*(uint64_t *)(arg1 + 0x8) != 0) goto loc_0024FA40;
loc_0024F7D5:
    if (*(uint64_t *)(arg1 + 0x50) != 0) goto loc_0024FA1C;
loc_0024F7E2:
    if (condition_is_above_or_equal) goto loc_0024F86F;
    result = KeAcquireSpinLockRaiseToDpc(*(uint64_t *)(arg1 + 0xC0) + 184, Arg2, Arg2 + 1, (uint32_t)((uint32_t)((uint32_t)(v_stack_p8))));
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x8)) != (Arg1 + 32)) goto loc_0024F4A3;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x20 + 0x8))) != (Arg1 + 32)) goto loc_0024F4A3;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x20 + 0x8)) = *(uint64_t *)(arg1 + 0x20);
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x8) = *(uint64_t *)(arg1 + 0x20 + 0x8);
    *(void **)(arg1 + 0x20 + 0x8) = Arg1 + 32;
    *(void **)(arg1 + 0x20) = Arg1 + 32;
    Arg2 = (*(uint64_t *)(arg1 + 0x58)) & (-7);
    Arg1 = (*(uint64_t *)(gs_base + (0 + 0x188))) + (0x790ULL);
    result = ObFastDereferenceObject(Arg1, Arg2, (uint32_t)(0x70436F49ULL), (uint32_t)((uint32_t)((uint32_t)(v_stack_p8))));
    *(uint32_t *)(arg1 + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x10)));
    result = KeReleaseSpinLock(*(uint64_t *)(arg1 + 0xC0) + 184, (uint8_t)((uint8_t)(result)), (uint32_t)(0x70436F49ULL), (uint32_t)((uint32_t)((uint32_t)(v_stack_p8))));
loc_0024F86F:
    if (*(uint64_t *)(arg1 + 0xC0) != 0) goto loc_0024F92C;
loc_0024F878:
    if (((*(uint32_t *)(arg1 + 0x10)) & (0x8000ULL)) != 0) goto loc_0024F974;
loc_0024F885:
    result = IoFreeIrp(Arg1, (uint8_t)((uint8_t)(result)), (uint32_t)(0x70436F49ULL), (uint32_t)((uint32_t)((uint32_t)(v_stack_p8))));
loc_0024F88D:
loc_0024F88F:
    local_rsp = (local_rsp) + (96);
    return 1;
loc_0024F8A8:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD7720A)))) & (64)) == 0) goto loc_0024F6DB;
    result = KiCheckVpBackingLongSpinWaitHypercall(Arg1, (uint8_t)((uint8_t)(result)), (uint32_t)(0x70436F49ULL), (uint32_t)((uint32_t)((uint32_t)(v_stack_p8))));
    if ((uint8_t)(result) == 0) goto loc_0024F6DB;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)((uint8_t)(result))), (uint8_t)((uint8_t)(result)), (uint32_t)(0x70436F49ULL), (uint32_t)((uint32_t)((uint32_t)(v_stack_p8))));
    goto loc_0024F6DD;
loc_0024F8CF:
    result = KeIsThreadRunning(v_stack_p10, (uint8_t)((uint8_t)(result)), (uint32_t)(0x70436F49ULL), (uint32_t)((uint32_t)((uint32_t)(v_stack_p8))));
    result = EtwTraceEnqueueWork(v_stack_p10, 0, (uint8_t)(result), (uint32_t)((uint32_t)((uint32_t)(v_stack_p8))));
    goto loc_0024F441;
loc_0024F8EB:
    goto loc_0024F529;
loc_0024F8F4:
    if ((*(uint8_t *)(v_stack_p10 + 0x283)) != 15) goto loc_0024F479;
    goto loc_0024F59F;
loc_0024F906:
    result = KxWaitForLockOwnerShip(v_stack_p48, 0, (uint8_t)(result), (uint32_t)((uint32_t)((uint32_t)(v_stack_p8))));
    goto loc_0024F3DF;
loc_0024F915:
    result = IopDoesCompletionNeedsApc(Arg1, 0, (uint8_t)(result), (uint32_t)((uint32_t)((uint32_t)(v_stack_p8))));
    if ((uint8_t)(result) == 0) goto loc_0024F9AF;
loc_0024F925:
    result = 0;
    goto loc_0024F88F;
loc_0024F92C:
    if (sign_flag) goto loc_0024F878;
    result = ObDereferenceObjectExWithTag(*(uint64_t *)(arg1 + 0xC0), 1, (uint32_t)(0x746C6644ULL), (uint32_t)((uint32_t)((uint32_t)(v_stack_p8))));
    goto loc_0024F878;
loc_0024F94C:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0xC0) + 0x30))))) & (0xC0000000ULL));
    if (((uint32_t)(result)) == 0xC0000000ULL) goto loc_0024F925;
    if (((*(uint32_t *)(1 + 0x50)) & (0x2000000ULL)) == 0) goto loc_0024F362;
    if (sign_flag) goto loc_0024F362;
    goto loc_0024F925;
loc_0024F974:
loc_0024F978:
    a4 = (*(uint64_t *)(arg1 + 0x58)) >> (1);
    Arg1 = (*(uint64_t *)(arg1 + 0x58)) & (-7);
    a4 = (uint32_t)((a4) & (3));
    a4 = (a4) - 1;
    Arg2 = (a4 + a4 * 1) | (Arg1);
    if ((*(uint64_t *)(arg1 + 0x58)) != (*(uint64_t *)(arg1 + 0x58))) goto loc_0024F978;
    if ((uint32_t)(a4) != 0) goto loc_0024F88D;
    goto loc_0024F885;
loc_0024F9AF:
    v_stack_p20 = v_stack_p30;
    result = IopCompleteRequest(Arg1 + 120, v_stack_p40, v_stack_p30, Arg1 + 192);
    goto loc_0024F88D;
loc_0024F9D8:
    if (((uint32_t)(result)) == 4) goto loc_0024F4CB;
    if ((uint32_t)(result) != 0) goto loc_0024F671;
    Arg1 = (uint8_t)((Arg1 + 120) & (250));
    Arg1 = (uint8_t)((Arg1) | (2));
    *(uint8_t *)(v_stack_p10 + 0x70) = (uint8_t)(Arg1);
    Arg2 = 0;
    *(void **)(v_stack_p10 + 0xC8) = Arg1 + 168;
    *(uint64_t *)(v_stack_p10 + 0x3D0) = 0;
    *(uint8_t *)(*(uint64_t *)(arg1 + 0xC0) + 0x11) = 0;
    goto loc_0024F56A;
loc_0024FA14:
    goto loc_0024F606;
loc_0024FA1C:
    if (1 == 0) goto loc_0024F7E2;
    if ((((uint8_t)(Arg1 + 168)) & (4)) != 0) goto loc_0024F7E2;
    result = ObfDereferenceObjectWithTag(Arg1, (uint32_t)(0x746C6644ULL), v_stack_p30, Arg1 + 192);
    goto loc_0024F7E2;
loc_0024FA40:
    result = IoFreeMdl(Arg1, (uint32_t)(0x746C6644ULL), v_stack_p30, Arg1 + 192);
    if (*(uint64_t *)(arg1) != 0) goto loc_0024FA40;
    goto loc_0024F7D5;
loc_0024FA58:
    Arg2 = 0;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x10)))) != 3) goto loc_0024F56A;
    *(uint8_t *)(1 + 0x11) = 2;
    goto loc_0024F56A;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `W` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `W` |
| `Arg1` | `+ 0x10` | `32` | `R` |
| `Arg1` | `+ 0x10` | `32` | `R/W` |
| `Arg1` | `+ 0x10` | `32` | `W` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x30` | `32` | `R` |
| `Arg1` | `+ 0x41` | `8` | `R` |
| `Arg1` | `+ 0x50` | `64` | `R` |
| `Arg1` | `+ 0x58` | `64` | `R` |
| `Arg1` | `+ 0x78` | `64` | `R` |
| `Arg1` | `+ 0x78` | `64` | `W` |
| `Arg1` | `+ 0xA8` | `64` | `R` |
| `Arg1` | `+ 0xA8` | `64` | `W` |
| `Arg1` | `+ 0xB8` | `32` | `W` |
| `Arg1` | `+ 0xC0` | `64` | `R` |
| `Arg2` | `+ 0x50` | `32` | `R` |
| `Arg2` | `+ 0xB0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0024F330&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
