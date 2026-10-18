# sub_0025E5F6

- RVA: `0x0025E5F6`–`0x0025EB42` (길이 `1,356` bytes)
- VA: `0x000000014025E5F6`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006411C`
- 디코드: `318`개 명령, `1,356/1,356` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **17**; 고유 호출 대상: **11**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x0025E603` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0025E649` → [KxWaitForLockChainValid](../21/KxWaitForLockChainValid_function_00217AA0.md) (function, `0x00217AA0`)
- `0x0025E66C` → [KeWakeAddressAll](../21/KeWakeAddressAll_function_00217C20.md) (function, `0x00217C20`)
- `0x0025E699` → [KiTryUnwaitThread](../35/KiTryUnwaitThread_function_003506D0.md) (function, `0x003506D0`)
- `0x0025E6E5` → [KiRemoveBoostThread](../21/KiRemoveBoostThread_function_00219128.md) (function, `0x00219128`)
- `0x0025E70F` → [KiExitDispatcher](KiExitDispatcher_function_00251CF0.md) (function, `0x00251CF0`)
- `0x0025E762` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x0025E7AD` → [KiAcquireKobjectLockSafe](KiAcquireKobjectLockSafe_function_00251C90.md) (function, `0x00251C90`)
- `0x0025E815` → [KiTryUnwaitThread](../35/KiTryUnwaitThread_function_003506D0.md) (function, `0x003506D0`)
- `0x0025E859` → [KiRemoveBoostThread](../21/KiRemoveBoostThread_function_00219128.md) (function, `0x00219128`)
- `0x0025E885` → [KiExitDispatcher](KiExitDispatcher_function_00251CF0.md) (function, `0x00251CF0`)
- `0x0025E8B4` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x0025E8E7` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x0025E905` → [KiInsertQueueInternal](../21/KiInsertQueueInternal_function_00219B30.md) (function, `0x00219B30`)
- `0x0025EA2B` → [EtwTraceKernelEvent](../23/EtwTraceKernelEvent_function_00235350.md) (function, `0x00235350`)
- `0x0025EA3C` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x0025EA5A` → [KiInsertQueueInternal](../21/KiInsertQueueInternal_function_00219B30.md) (function, `0x00219B30`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0025E778` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x0025E9B0` → RVA `0x00E0EB18` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0025E603` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **36**
  - `0x0025E5F9` → [sub_0025D903 + 0xC77](Unknown_function_0025D903.md) (`tail-transfer`)
  - `0x0025E608` → [sub_0025D903 + 0xCA5](Unknown_function_0025D903.md) (`tail-transfer`)
  - `0x0025E613` → [sub_0025D903 + 0xB2F](Unknown_function_0025D903.md) (`tail-transfer`)
  - `0x0025E63E` → [sub_0025D903 + 0xA0E](Unknown_function_0025D903.md) (`tail-transfer`)
  - `0x0025E666` → [sub_0025D903 + 0xA0E](Unknown_function_0025D903.md) (`tail-transfer`)
  - `0x0025E671` → [sub_0025D903 + 0xA0E](Unknown_function_0025D903.md) (`tail-transfer`)
  - `0x0025E6AF` → [sub_0025D903 + 0x7F2](Unknown_function_0025D903.md) (`tail-transfer`)
  - `0x0025E6B9` → [sub_0025D903 + 0x7F2](Unknown_function_0025D903.md) (`tail-transfer`)
  - `0x0025E714` → [sub_0025D903 + 0x35E](Unknown_function_0025D903.md) (`tail-transfer`)
  - `0x0025E73F` → [sub_0025D903 + 0x225](Unknown_function_0025D903.md) (`tail-transfer`)
  - `0x0025E75C` → [sub_0025D903 + 0x6C2](Unknown_function_0025D903.md) (`tail-transfer`)
  - `0x0025E767` → [sub_0025D903 + 0x6C2](Unknown_function_0025D903.md) (`tail-transfer`)
  - `0x0025E7E3` → [sub_0025D903 + 0x819](Unknown_function_0025D903.md) (`tail-transfer`)
  - `0x0025E7EC` → [sub_0025D903 + 0x819](Unknown_function_0025D903.md) (`tail-transfer`)
  - `0x0025E866` → [sub_0025EB5D + 0x32](Unknown_function_0025EB5D.md) (`tail-transfer`)
  - `0x0025E86F` → [sub_0025EB5D](Unknown_function_0025EB5D.md) (`tail-transfer`)
  - `0x0025E88A` → [sub_0025D903 + 0x9C2](Unknown_function_0025D903.md) (`tail-transfer`)
  - `0x0025E891` → [sub_0025D903 + 0x398](Unknown_function_0025D903.md) (`tail-transfer`)
  - `0x0025E8AE` → [sub_0025D903 + 0x301](Unknown_function_0025D903.md) (`tail-transfer`)
  - `0x0025E8B9` → [sub_0025D903 + 0x301](Unknown_function_0025D903.md) (`tail-transfer`)
  - `0x0025E8C5` → [sub_0025D903 + 0xCA5](Unknown_function_0025D903.md) (`tail-transfer`)
  - `0x0025E8CF` → [sub_0025D903 + 0xCA5](Unknown_function_0025D903.md) (`tail-transfer`)
  - `0x0025E8EC` → [sub_0025D903 + 0x7AB](Unknown_function_0025D903.md) (`tail-transfer`)
  - `0x0025E8F4` → [sub_0025EB5D + 0x6A](Unknown_function_0025EB5D.md) (`tail-transfer`)
  - `0x0025E923` → [sub_0025D903 + 0x7F2](Unknown_function_0025D903.md) (`tail-transfer`)
  - `0x0025E92E` → [sub_0025D903 + 0x7BF](Unknown_function_0025D903.md) (`tail-transfer`)
  - `0x0025E93A` → [sub_0025D903 + 0x788](Unknown_function_0025D903.md) (`tail-transfer`)
  - `0x0025E958` → [sub_0025D903 + 0x225](Unknown_function_0025D903.md) (`tail-transfer`)
  - `0x0025E985` → [sub_0025D903 + 0x788](Unknown_function_0025D903.md) (`tail-transfer`)
  - `0x0025E98E` → [sub_0025D903 + 0x788](Unknown_function_0025D903.md) (`tail-transfer`)
  - `0x0025E9B8` → [sub_0025D903 + 0xC2E](Unknown_function_0025D903.md) (`tail-transfer`)
  - `0x0025EA30` → [sub_0025D903 + 0xC5D](Unknown_function_0025D903.md) (`tail-transfer`)
  - `0x0025EA49` → [sub_0025EB5D + 0xDE](Unknown_function_0025EB5D.md) (`tail-transfer`)
  - `0x0025EAA5` → [sub_0025EB5D + 0x12](Unknown_function_0025EB5D.md) (`tail-transfer`)
  - `0x0025EAC7` → [sub_0025D903 + 0x8D0](Unknown_function_0025D903.md) (`tail-transfer`)
  - `0x0025EAF3` → [sub_0025D903 + 0xBE3](Unknown_function_0025D903.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0025E5F6  45 32 F6                        xor r14b, r14b
0025E5F9  E9 7C FF FF FF                  jmp 0x14025e57a
0025E5FE  33 D2                           xor edx, edx
0025E600  48 8B CB                        mov rcx, rbx
0025E603  E8 68 42 92 00                  call 0x140b82870
0025E608  EB 9E                           jmp 0x14025e5a8
0025E60A  49 8B C6                        mov rax, r14
0025E60D  49 83 C6 40                     add r14, 0x40
0025E611  FF C2                           inc edx
0025E613  E9 1A FE FF FF                  jmp 0x14025e432
0025E618  0F 0D 4C 24 48                  prefetchw byte ptr [rsp + 0x48]
0025E61D  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
0025E622  48 85 C0                        test rax, rax
0025E625  75 27                           jne 0x14025e64e
0025E627  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
0025E62C  48 8D 44 24 48                  lea rax, [rsp + 0x48]
0025E631  F0 48 0F B1 31                  lock cmpxchg qword ptr [rcx], rsi
0025E636  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
0025E63B  48 3B C1                        cmp rax, rcx
0025E63E  0F 84 CD FC FF FF               je 0x14025e311
0025E644  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
0025E649  E8 52 94 FB FF                  call 0x140217aa0
0025E64E  48 8D 48 08                     lea rcx, [rax + 8]
0025E652  48 89 74 24 48                  mov qword ptr [rsp + 0x48], rsi
0025E657  48 8B 54 24 50                  mov rdx, qword ptr [rsp + 0x50]
0025E65C  48 8B C2                        mov rax, rdx
0025E65F  48 87 01                        xchg qword ptr [rcx], rax
0025E662  32 C2                           xor al, dl
0025E664  A8 04                           test al, 4
0025E666  0F 84 A5 FC FF FF               je 0x14025e311
0025E66C  E8 AF 95 FB FF                  call 0x140217c20
0025E671  E9 9B FC FF FF                  jmp 0x14025e311
0025E676  48 89 10                        mov qword ptr [rax], rdx
0025E679  48 89 42 08                     mov qword ptr [rdx + 8], rax
0025E67D  0F B6 41 10                     movzx eax, byte ptr [rcx + 0x10]
0025E681  41 3A C6                        cmp al, r14b
0025E684  0F 85 67 02 00 00               jne 0x14025e8f1
0025E68A  44 0F B7 41 12                  movzx r8d, word ptr [rcx + 0x12]
0025E68F  48 8B D1                        mov rdx, rcx
0025E692  48 8B 4D 88                     mov rcx, qword ptr [rbp - 0x78]
0025E696  45 33 C9                        xor r9d, r9d
0025E699  E8 32 20 0F 00                  call 0x1403506d0
0025E69E  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
0025E6A3  84 C0                           test al, al
0025E6A5  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
0025E6AA  4C 8B 4C 24 70                  mov r9, qword ptr [rsp + 0x70]
0025E6AF  0F 84 40 FA FF FF               je 0x14025e0f5
0025E6B5  45 29 71 04                     sub dword ptr [r9 + 4], r14d
0025E6B9  0F 85 36 FA FF FF               jne 0x14025e0f5
0025E6BF  48 8B 45 80                     mov rax, qword ptr [rbp - 0x80]
0025E6C3  F0 81 60 18 7F FF FF FF         lock and dword ptr [rax + 0x18], 0xffffff7f
0025E6CB  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
0025E6D0  48 3B 4D 98                     cmp rcx, qword ptr [rbp - 0x68]
0025E6D4  0F 85 4E 02 00 00               jne 0x14025e928
0025E6DA  4C 8B 7D 88                     mov r15, qword ptr [rbp - 0x78]
0025E6DE  49 8B CF                        mov rcx, r15
0025E6E1  49 8B 57 08                     mov rdx, qword ptr [r15 + 8]
0025E6E5  E8 3E AA FB FF                  call 0x140219128
0025E6EA  45 85 ED                        test r13d, r13d
0025E6ED  0F 85 D9 03 00 00               jne 0x14025eacc
0025E6F3  41 84 DC                        test r12b, bl
0025E6F6  0F 85 81 03 00 00               jne 0x14025ea7d
0025E6FC  48 8B 45 90                     mov rax, qword ptr [rbp - 0x70]
0025E700  45 8B CD                        mov r9d, r13d
0025E703  45 8B C6                        mov r8d, r14d
0025E706  88 44 24 20                     mov byte ptr [rsp + 0x20], al
0025E70A  33 D2                           xor edx, edx
0025E70C  49 8B CF                        mov rcx, r15
0025E70F  E8 DC 35 FF FF                  call 0x140251cf0
0025E714  E9 48 F5 FF FF                  jmp 0x14025dc61
0025E719  48 89 77 28                     mov qword ptr [rdi + 0x28], rsi
0025E71D  48 8B 45 98                     mov rax, qword ptr [rbp - 0x68]
0025E721  4C 8B 71 10                     mov r14, qword ptr [rcx + 0x10]
0025E725  48 85 C0                        test rax, rax
0025E728  0F 85 05 02 00 00               jne 0x14025e933
0025E72E  48 89 49 08                     mov qword ptr [rcx + 8], rcx
0025E732  48 89 09                        mov qword ptr [rcx], rcx
0025E735  48 89 4D 98                     mov qword ptr [rbp - 0x68], rcx
0025E739  FF 4F 4C                        dec dword ptr [rdi + 0x4c]
0025E73C  41 8B CF                        mov ecx, r15d
0025E73F  E9 E4 F3 FF FF                  jmp 0x14025db28
0025E744  41 0F 0D 08                     prefetchw byte ptr [r8]
0025E748  41 8B 00                        mov eax, dword ptr [r8]
0025E74B  8B D0                           mov edx, eax
0025E74D  0F BA F2 15                     btr edx, 0x15
0025E751  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
0025E756  75 F3                           jne 0x14025e74b
0025E758  0F BA E0 15                     bt eax, 0x15
0025E75C  0F 83 63 F8 FF FF               jae 0x14025dfc5
0025E762  E8 69 4A 00 00                  call 0x1402631d0
0025E767  E9 59 F8 FF FF                  jmp 0x14025dfc5
0025E76C  44 0F 20 C0                     mov rax, cr8
0025E770  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
0025E774  45 0F 22 C4                     mov cr8, r12
0025E778  39 35 A2 85 D6 00               cmp dword ptr [rip + 0xd685a2], esi
0025E77E  0F 85 B1 02 00 00               jne 0x14025ea35
0025E784  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
0025E78D  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
0025E791  48 8B 45 A0                     mov rax, qword ptr [rbp - 0x60]
0025E795  48 8B 08                        mov rcx, qword ptr [rax]
0025E798  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
0025E79C  48 83 C0 18                     add rax, 0x18
0025E7A0  48 89 4C 24 78                  mov qword ptr [rsp + 0x78], rcx
0025E7A5  48 8B C8                        mov rcx, rax
0025E7A8  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0025E7AD  E8 DE 34 FF FF                  call 0x140251c90
0025E7B2  48 8B 45 88                     mov rax, qword ptr [rbp - 0x78]
0025E7B6  44 89 70 1C                     mov dword ptr [rax + 0x1c], r14d
0025E7BA  4C 8D 48 18                     lea r9, [rax + 0x18]
0025E7BE  49 8B 49 08                     mov rcx, qword ptr [r9 + 8]
0025E7C2  49 8D 41 08                     lea rax, [r9 + 8]
0025E7C6  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
0025E7CB  48 3B C8                        cmp rcx, rax
0025E7CE  74 63                           je 0x14025e833
0025E7D0  48 8B 11                        mov rdx, qword ptr [rcx]
0025E7D3  48 8B C1                        mov rax, rcx
0025E7D6  48 8B 49 08                     mov rcx, qword ptr [rcx + 8]
0025E7DA  48 89 54 24 70                  mov qword ptr [rsp + 0x70], rdx
0025E7DF  48 39 42 08                     cmp qword ptr [rdx + 8], rax
0025E7E3  0F 85 33 F9 FF FF               jne 0x14025e11c
0025E7E9  48 39 01                        cmp qword ptr [rcx], rax
0025E7EC  0F 85 2A F9 FF FF               jne 0x14025e11c
0025E7F2  48 89 11                        mov qword ptr [rcx], rdx
0025E7F5  48 89 4A 08                     mov qword ptr [rdx + 8], rcx
0025E7F9  0F B6 48 10                     movzx ecx, byte ptr [rax + 0x10]
0025E7FD  41 3A CE                        cmp cl, r14b
0025E800  0F 85 40 02 00 00               jne 0x14025ea46
0025E806  44 0F B7 40 12                  movzx r8d, word ptr [rax + 0x12]
0025E80B  45 33 C9                        xor r9d, r9d
0025E80E  48 8B 4D 80                     mov rcx, qword ptr [rbp - 0x80]
0025E812  48 8B D0                        mov rdx, rax
0025E815  E8 B6 1E 0F 00                  call 0x1403506d0
0025E81A  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
0025E81F  84 C0                           test al, al
0025E821  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
0025E826  4C 8B 4C 24 38                  mov r9, qword ptr [rsp + 0x38]
0025E82B  74 9E                           je 0x14025e7cb
0025E82D  45 29 71 04                     sub dword ptr [r9 + 4], r14d
0025E831  75 98                           jne 0x14025e7cb
0025E833  48 8B 45 88                     mov rax, qword ptr [rbp - 0x78]
0025E837  F0 81 60 18 7F FF FF FF         lock and dword ptr [rax + 0x18], 0xffffff7f
0025E83F  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
0025E844  48 3B 4D A0                     cmp rcx, qword ptr [rbp - 0x60]
0025E848  0F 85 41 02 00 00               jne 0x14025ea8f
0025E84E  4C 8B 7D 80                     mov r15, qword ptr [rbp - 0x80]
0025E852  49 8B CF                        mov rcx, r15
0025E855  49 8B 57 08                     mov rdx, qword ptr [r15 + 8]
0025E859  E8 CA A8 FB FF                  call 0x140219128
0025E85E  44 8B 4C 24 68                  mov r9d, dword ptr [rsp + 0x68]
0025E863  45 85 C9                        test r9d, r9d
0025E866  0F 85 23 03 00 00               jne 0x14025eb8f
0025E86C  41 84 DC                        test r12b, bl
0025E86F  0F 85 E8 02 00 00               jne 0x14025eb5d
0025E875  48 8B 45 90                     mov rax, qword ptr [rbp - 0x70]
0025E879  45 8B C6                        mov r8d, r14d
0025E87C  33 D2                           xor edx, edx
0025E87E  88 44 24 20                     mov byte ptr [rsp + 0x20], al
0025E882  49 8B CF                        mov rcx, r15
0025E885  E8 66 34 FF FF                  call 0x140251cf0
0025E88A  E9 36 FA FF FF                  jmp 0x14025e2c5
0025E88F  8B C6                           mov eax, esi
0025E891  E9 05 F4 FF FF                  jmp 0x14025dc9b
0025E896  41 0F 0D 08                     prefetchw byte ptr [r8]
0025E89A  41 8B 00                        mov eax, dword ptr [r8]
0025E89D  8B D0                           mov edx, eax
0025E89F  0F BA F2 15                     btr edx, 0x15
0025E8A3  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
0025E8A8  75 F3                           jne 0x14025e89d
0025E8AA  0F BA E0 15                     bt eax, 0x15
0025E8AE  0F 83 50 F3 FF FF               jae 0x14025dc04
0025E8B4  E8 17 49 00 00                  call 0x1402631d0
0025E8B9  E9 46 F3 FF FF                  jmp 0x14025dc04
0025E8BE  41 81 F8 52 00 01 00            cmp r8d, 0x10052
0025E8C5  0F 85 DD FC FF FF               jne 0x14025e5a8
0025E8CB  44 89 63 20                     mov dword ptr [rbx + 0x20], r12d
0025E8CF  E9 D4 FC FF FF                  jmp 0x14025e5a8
0025E8D4  48 89 10                        mov qword ptr [rax], rdx
0025E8D7  48 89 42 08                     mov qword ptr [rdx + 8], rax
0025E8DB  E9 3D FE FF FF                  jmp 0x14025e71d
0025E8E0  41 0F B6 D4                     movzx edx, r12b
0025E8E4  0F B6 C8                        movzx ecx, al
0025E8E7  E8 10 6E 29 00                  call 0x1404f56fc
0025E8EC  E9 BD F7 FF FF                  jmp 0x14025e0ae
0025E8F1  41 3A C4                        cmp al, r12b
0025E8F4  0F 85 CD 02 00 00               jne 0x14025ebc7
0025E8FA  C6 41 11 05                     mov byte ptr [rcx + 0x11], 5
0025E8FE  48 8B D1                        mov rdx, rcx
0025E901  48 8B 49 18                     mov rcx, qword ptr [rcx + 0x18]
0025E905  E8 26 B2 FB FF                  call 0x140219b30
0025E90A  4C 8B 4C 24 70                  mov r9, qword ptr [rsp + 0x70]
0025E90F  45 29 71 04                     sub dword ptr [r9 + 4], r14d
0025E913  0F 84 A6 FD FF FF               je 0x14025e6bf
0025E919  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
0025E91E  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
0025E923  E9 CD F7 FF FF                  jmp 0x14025e0f5
0025E928  48 8B C1                        mov rax, rcx
0025E92B  48 8B 09                        mov rcx, qword ptr [rcx]
0025E92E  E9 8F F7 FF FF                  jmp 0x14025e0c2
0025E933  48 8B 50 08                     mov rdx, qword ptr [rax + 8]
0025E937  48 39 02                        cmp qword ptr [rdx], rax
0025E93A  0F 85 4B F7 FF FF               jne 0x14025e08b
0025E940  48 89 01                        mov qword ptr [rcx], rax
0025E943  48 89 51 08                     mov qword ptr [rcx + 8], rdx
0025E947  48 89 0A                        mov qword ptr [rdx], rcx
0025E94A  48 89 48 08                     mov qword ptr [rax + 8], rcx
0025E94E  FF 4F 4C                        dec dword ptr [rdi + 0x4c]
0025E951  48 89 4D 98                     mov qword ptr [rbp - 0x68], rcx
0025E955  41 8B CF                        mov ecx, r15d
0025E958  E9 CB F1 FF FF                  jmp 0x14025db28
0025E95D  48 8B 47 28                     mov rax, qword ptr [rdi + 0x28]
0025E961  48 85 C0                        test rax, rax
0025E964  0F 84 4C 01 00 00               je 0x14025eab6
0025E96A  48 8B 08                        mov rcx, qword ptr [rax]
0025E96D  48 3B C8                        cmp rcx, rax
0025E970  0F 84 24 01 00 00               je 0x14025ea9a
0025E976  48 89 4F 28                     mov qword ptr [rdi + 0x28], rcx
0025E97A  48 8B 10                        mov rdx, qword ptr [rax]
0025E97D  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
0025E981  48 39 42 08                     cmp qword ptr [rdx + 8], rax
0025E985  0F 85 00 F7 FF FF               jne 0x14025e08b
0025E98B  48 39 01                        cmp qword ptr [rcx], rax
0025E98E  0F 85 F7 F6 FF FF               jne 0x14025e08b
0025E994  48 89 11                        mov qword ptr [rcx], rdx
0025E997  48 89 4A 08                     mov qword ptr [rdx + 8], rcx
0025E99B  E9 FE 00 00 00                  jmp 0x14025ea9e
0025E9A0  41 8B 87 F0 8E 00 00            mov eax, dword ptr [r15 + 0x8ef0]
0025E9A7  33 D2                           xor edx, edx
0025E9A9  41 03 87 EC 8E 00 00            add eax, dword ptr [r15 + 0x8eec]
0025E9B0  F7 35 62 01 BB 00               div dword ptr [rip + 0xbb0162]
0025E9B6  85 D2                           test edx, edx
0025E9B8  0F 85 73 FB FF FF               jne 0x14025e531
0025E9BE  44 8B 54 24 44                  mov r10d, dword ptr [rsp + 0x44]
0025E9C3  44 89 45 D0                     mov dword ptr [rbp - 0x30], r8d
0025E9C7  48 89 7D C8                     mov qword ptr [rbp - 0x38], rdi
0025E9CB  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
0025E9CF  48 89 45 A8                     mov qword ptr [rbp - 0x58], rax
0025E9D3  8B 43 24                        mov eax, dword ptr [rbx + 0x24]
0025E9D6  89 45 C0                        mov dword ptr [rbp - 0x40], eax
0025E9D9  4C 89 4D B0                     mov qword ptr [rbp - 0x50], r9
0025E9DD  48 8B 03                        mov rax, qword ptr [rbx]
0025E9E0  48 89 45 B8                     mov qword ptr [rbp - 0x48], rax
0025E9E4  44 2B 53 2C                     sub r10d, dword ptr [rbx + 0x2c]
0025E9E8  44 89 55 D4                     mov dword ptr [rbp - 0x2c], r10d
0025E9EC  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0025E9F5  8B 88 10 05 00 00               mov ecx, dword ptr [rax + 0x510]
0025E9FB  48 8D 45 A8                     lea rax, [rbp - 0x58]
0025E9FF  89 4D C4                        mov dword ptr [rbp - 0x3c], ecx
0025EA02  41 B9 2B 05 00 00               mov r9d, 0x52b
0025EA08  C7 44 24 20 02 18 60 01         mov dword ptr [rsp + 0x20], 0x1601802
0025EA10  41 B8 00 00 02 20               mov r8d, 0x20020000
0025EA16  48 89 45 08                     mov qword ptr [rbp + 8], rax
0025EA1A  BA 01 00 00 00                  mov edx, 1
0025EA1F  48 C7 45 10 30 00 00 00         mov qword ptr [rbp + 0x10], 0x30
0025EA27  48 8D 4D 08                     lea rcx, [rbp + 8]
0025EA2B  E8 20 69 FD FF                  call 0x140235350
0025EA30  E9 2B FB FF FF                  jmp 0x14025e560
0025EA35  41 0F B6 D4                     movzx edx, r12b
0025EA39  0F B6 C8                        movzx ecx, al
0025EA3C  E8 BB 6C 29 00                  call 0x1404f56fc
0025EA41  E9 3E FD FF FF                  jmp 0x14025e784
0025EA46  41 3A CC                        cmp cl, r12b
0025EA49  0F 85 EC 01 00 00               jne 0x14025ec3b
0025EA4F  C6 40 11 05                     mov byte ptr [rax + 0x11], 5
0025EA53  48 8B D0                        mov rdx, rax
0025EA56  48 8B 48 18                     mov rcx, qword ptr [rax + 0x18]
0025EA5A  E8 D1 B0 FB FF                  call 0x140219b30
0025EA5F  4C 8B 4C 24 38                  mov r9, qword ptr [rsp + 0x38]
0025EA64  45 29 71 04                     sub dword ptr [r9 + 4], r14d
0025EA68  0F 84 C5 FD FF FF               je 0x14025e833
0025EA6E  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
0025EA73  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
0025EA78  E9 4E FD FF FF                  jmp 0x14025e7cb
0025EA7D  41 83 FE 01                     cmp r14d, 1
0025EA81  B8 01 00 00 00                  mov eax, 1
0025EA86  44 0F 44 E8                     cmove r13d, eax
0025EA8A  E9 6D FC FF FF                  jmp 0x14025e6fc
0025EA8F  48 8B C1                        mov rax, rcx
0025EA92  48 8B 09                        mov rcx, qword ptr [rcx]
0025EA95  E9 FE FC FF FF                  jmp 0x14025e798
0025EA9A  48 89 77 28                     mov qword ptr [rdi + 0x28], rsi
0025EA9E  4C 8B 70 10                     mov r14, qword ptr [rax + 0x10]
0025EAA2  48 85 DB                        test rbx, rbx
0025EAA5  0F 85 C4 00 00 00               jne 0x14025eb6f
0025EAAB  48 89 40 08                     mov qword ptr [rax + 8], rax
0025EAAF  48 89 00                        mov qword ptr [rax], rax
0025EAB2  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
0025EAB6  FF 4F 4C                        dec dword ptr [rdi + 0x4c]
0025EAB9  B8 80 00 00 00                  mov eax, 0x80
0025EABE  66 09 47 1A                     or word ptr [rdi + 0x1a], ax
0025EAC2  B9 01 00 00 00                  mov ecx, 1
0025EAC7  E9 07 F7 FF FF                  jmp 0x14025e1d3
0025EACC  41 3B C5                        cmp eax, r13d
0025EACF  45 8B F4                        mov r14d, r12d
0025EAD2  44 0F 4F E8                     cmovg r13d, eax
0025EAD6  E9 18 FC FF FF                  jmp 0x14025e6f3
0025EADB  41 8B 85 F0 8E 00 00            mov eax, dword ptr [r13 + 0x8ef0]
0025EAE2  33 D2                           xor edx, edx
0025EAE4  41 03 85 EC 8E 00 00            add eax, dword ptr [r13 + 0x8eec]
0025EAEB  F7 35 27 00 BB 00               div dword ptr [rip + 0xbb0027]
0025EAF1  85 D2                           test edx, edx
0025EAF3  0F 85 ED F9 FF FF               jne 0x14025e4e6
0025EAF9  44 8B 54 24 44                  mov r10d, dword ptr [rsp + 0x44]
0025EAFE  44 89 45 00                     mov dword ptr [rbp], r8d
0025EB02  48 89 7D F8                     mov qword ptr [rbp - 8], rdi
0025EB06  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
0025EB0A  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
0025EB0E  8B 43 24                        mov eax, dword ptr [rbx + 0x24]
0025EB11  89 45 F0                        mov dword ptr [rbp - 0x10], eax
0025EB14  4C 89 4D E0                     mov qword ptr [rbp - 0x20], r9
0025EB18  48 8B 03                        mov rax, qword ptr [rbx]
0025EB1B  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
0025EB1F  44 2B 53 2C                     sub r10d, dword ptr [rbx + 0x2c]
0025EB23  44 89 55 04                     mov dword ptr [rbp + 4], r10d
0025EB27  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0025EB30  8B 88 10 05 00 00               mov ecx, dword ptr [rax + 0x510]
0025EB36  48 8D 45 D8                     lea rax, [rbp - 0x28]
0025EB3A  89 4D F4                        mov dword ptr [rbp - 0xc], ecx
0025EB3D  E9 C0 FE FF FF                  jmp 0x14025ea02
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0025E5F6(__int64 a1, int a2, __int64 a3, int a4)
{
    __int64 v_r14;
    unsigned __int8 v_stack_p20;
    unsigned __int64 v_stack_p38;
    unsigned int v_stack_p44;
    unsigned __int8 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;

    v_r14 = 0;
}
```

## 5. (Beta) C Style

```c
int64_t sub_0025E5F6(int64_t Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t local_r14;
    uint8_t v_stack_p20;
    uint64_t v_stack_p38;
    uint32_t v_stack_p44;
    uint8_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;

    local_r14 = 0;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0025E5F6&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
