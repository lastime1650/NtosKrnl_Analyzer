# sub_0025D903

- RVA: `0x0025D903`–`0x0025E5F5` (길이 `3,314` bytes)
- VA: `0x000000014025D903`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000640E4`
- 디코드: `790`개 명령, `3,314/3,314` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **33**; 고유 호출 대상: **18**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **11**

### Outgoing calls
- `0x0025D9F2` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0025DA0E` → [KiAcquireQueuedSpinLockInstrumented](../27/KiAcquireQueuedSpinLockInstrumented_function_00275850.md) (function, `0x00275850`)
- `0x0025DAD7` → [ObpPushStackInfo](../21/ObpPushStackInfo_function_002109E4.md) (function, `0x002109E4`)
- `0x0025DB9D` → [KxWaitForLockChainValid](../21/KxWaitForLockChainValid_function_00217AA0.md) (function, `0x00217AA0`)
- `0x0025DBCF` → [KeDisableInterrupts](../21/KeDisableInterrupts_function_00217BE0.md) (function, `0x00217BE0`)
- `0x0025DBE2` → [KiHaltOnAddressWakeEntireList](../21/KiHaltOnAddressWakeEntireList_function_00217AF4.md) (function, `0x00217AF4`)
- `0x0025DC1E` → [KiReleaseQueuedSpinLockInstrumented](../21/KiReleaseQueuedSpinLockInstrumented_function_002179F0.md) (function, `0x002179F0`)
- `0x0025DC37` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0025DCE7` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0025DD40` → [KiReleaseQueuedSpinLockInstrumented](../21/KiReleaseQueuedSpinLockInstrumented_function_002179F0.md) (function, `0x002179F0`)
- `0x0025DD59` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0025DE1F` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0025DE5E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0025DF56` → [KxWaitForLockChainValid](../21/KxWaitForLockChainValid_function_00217AA0.md) (function, `0x00217AA0`)
- `0x0025DF8C` → [KeDisableInterrupts](../21/KeDisableInterrupts_function_00217BE0.md) (function, `0x00217BE0`)
- `0x0025DF9F` → [KiHaltOnAddressWakeEntireList](../21/KiHaltOnAddressWakeEntireList_function_00217AF4.md) (function, `0x00217AF4`)
- `0x0025DFE1` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x0025E0D7` → [KiAcquireKobjectLockSafe](KiAcquireKobjectLockSafe_function_00251C90.md) (function, `0x00251C90`)
- `0x0025E148` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0025E153` → [KxWaitForLockOwnerShip](KxWaitForLockOwnerShip_function_00257EB0.md) (function, `0x00257EB0`)
- `0x0025E1A8` → [ExpFreeOwnerEntry](../20/ExpFreeOwnerEntry_function_0020F740.md) (function, `0x0020F740`)
- `0x0025E249` → [KxWaitForLockChainValid](../21/KxWaitForLockChainValid_function_00217AA0.md) (function, `0x00217AA0`)
- `0x0025E268` → [KeWakeAddressAll](../21/KeWakeAddressAll_function_00217C20.md) (function, `0x00217C20`)
- `0x0025E282` → [KiReleaseQueuedSpinLockInstrumented](../21/KiReleaseQueuedSpinLockInstrumented_function_002179F0.md) (function, `0x002179F0`)
- `0x0025E29B` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0025E30C` → [KiReleaseQueuedSpinLockInstrumented](../21/KiReleaseQueuedSpinLockInstrumented_function_002179F0.md) (function, `0x002179F0`)
- `0x0025E325` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0025E3E7` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0025E423` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0025E58B` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0025E59E` → [ExReleaseFastResource](../26/ExReleaseFastResource_function_002613D0.md) (function, `0x002613D0`)
- `0x0025E5B1` → [KeLeaveCriticalRegionThread](KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x0025E5E5` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0025D957` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x0025D963` → RVA `0x00FC6B06` (`ALMOSTRO`; read)
- `0x0025D9A0` → RVA `0x00EFAC10` (`.data`; read)
- `0x0025D9B4` → RVA `0x00FC6B04` (`ALMOSTRO`; read)
- `0x0025D9F8` → RVA `0x00F0DE58` (`.data`; read)
- `0x0025DA6D` → RVA `0x00FC6F88` (`ALMOSTRO`; read)
- `0x0025DAC0` → RVA `0x00FC5010` (`ALMOSTRO`; read)
- `0x0025DBC4` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x0025DD0A` → RVA `0x00FC6B06` (`ALMOSTRO`; reference)
- `0x0025DDFF` → RVA `0x00E68468` (`.data`; read)
- `0x0025E507` → RVA `0x00E0EB10` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x0025DE1F` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x0025DE5E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x0025E3E7` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x0025E423` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **35**
  - `0x0025D91A` → [sub_0025EB5D + 0x2BF](Unknown_function_0025EB5D.md) (`tail-transfer`)
  - `0x0025DA76` → [sub_0025EB5D + 0x124](Unknown_function_0025EB5D.md) (`tail-transfer`)
  - `0x0025DA82` → [sub_0025EB5D + 0x26B](Unknown_function_0025EB5D.md) (`tail-transfer`)
  - `0x0025DA92` → [sub_0025EB5D + 0x329](Unknown_function_0025EB5D.md) (`tail-transfer`)
  - `0x0025DAED` → [sub_0025EB5D + 0x41](Unknown_function_0025EB5D.md) (`tail-transfer`)
  - `0x0025DBFE` → [sub_0025E5F6 + 0x2A0](Unknown_function_0025E5F6.md) (`tail-transfer`)
  - `0x0025DC8D` → [sub_0025E5F6 + 0x299](Unknown_function_0025E5F6.md) (`tail-transfer`)
  - `0x0025DEE9` → [sub_0025EB5D + 0x3EA](Unknown_function_0025EB5D.md) (`tail-transfer`)
  - `0x0025DFBF` → [sub_0025E5F6 + 0x14E](Unknown_function_0025E5F6.md) (`tail-transfer`)
  - `0x0025E05F` → [sub_0025E5F6 + 0x143](Unknown_function_0025E5F6.md) (`tail-transfer`)
  - `0x0025E06B` → [sub_0025E5F6 + 0x123](Unknown_function_0025E5F6.md) (`tail-transfer`)
  - `0x0025E085` → [sub_0025E5F6 + 0x2DE](Unknown_function_0025E5F6.md) (`tail-transfer`)
  - `0x0025E0A8` → [sub_0025E5F6 + 0x2EA](Unknown_function_0025E5F6.md) (`tail-transfer`)
  - `0x0025E0F8` → [sub_0025E5F6 + 0xC9](Unknown_function_0025E5F6.md) (`tail-transfer`)
  - `0x0025E116` → [sub_0025E5F6 + 0x80](Unknown_function_0025E5F6.md) (`tail-transfer`)
  - `0x0025E1C0` → [sub_0025E5F6 + 0x367](Unknown_function_0025E5F6.md) (`tail-transfer`)
  - `0x0025E1CB` → [sub_0025EB5D + 0x110](Unknown_function_0025EB5D.md) (`tail-transfer`)
  - `0x0025E2BF` → [sub_0025E5F6 + 0x176](Unknown_function_0025E5F6.md) (`tail-transfer`)
  - `0x0025E2EF` → [sub_0025E5F6 + 0x22](Unknown_function_0025E5F6.md) (`tail-transfer`)
  - `0x0025E2FD` → [sub_0025E5F6 + 0x22](Unknown_function_0025E5F6.md) (`tail-transfer`)
  - `0x0025E44F` → [sub_0025E5F6 + 0x17](Unknown_function_0025E5F6.md) (`tail-transfer`)
  - `0x0025E457` → [sub_0025E5F6 + 0x14](Unknown_function_0025E5F6.md) (`tail-transfer`)
  - `0x0025E461` → [sub_0025E5F6 + 0x17](Unknown_function_0025E5F6.md) (`tail-transfer`)
  - `0x0025E4B4` → [sub_0025EB5D + 0x437](Unknown_function_0025EB5D.md) (`tail-transfer`)
  - `0x0025E4C6` → [sub_0025E5F6 + 0x2C8](Unknown_function_0025E5F6.md) (`tail-transfer`)
  - `0x0025E4D3` → [sub_0025EB5D + 0x43F](Unknown_function_0025EB5D.md) (`tail-transfer`)
  - `0x0025E4E0` → [sub_0025E5F6 + 0x4E5](Unknown_function_0025E5F6.md) (`tail-transfer`)
  - `0x0025E4F1` → [sub_0025EB5D + 0x469](Unknown_function_0025EB5D.md) (`tail-transfer`)
  - `0x0025E50F` → [sub_0025E5F6 + 0x508](Unknown_function_0025E5F6.md) (`tail-transfer`)
  - `0x0025E51E` → [sub_0025EB5D + 0x3F3](Unknown_function_0025EB5D.md) (`tail-transfer`)
  - `0x0025E52B` → [sub_0025E5F6 + 0x3AA](Unknown_function_0025E5F6.md) (`tail-transfer`)
  - `0x0025E53C` → [sub_0025EB5D + 0x41D](Unknown_function_0025EB5D.md) (`tail-transfer`)
  - `0x0025E55A` → [sub_0025E5F6 + 0x3CD](Unknown_function_0025E5F6.md) (`tail-transfer`)
  - `0x0025E56C` → [sub_0025E5F6](Unknown_function_0025E5F6.md) (`tail-transfer`)
  - `0x0025E5A6` → [sub_0025E5F6 + 0x8](Unknown_function_0025E5F6.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0025D903  49 89 5B 10                     mov qword ptr [r11 + 0x10], rbx
0025D907  4D 89 63 18                     mov qword ptr [r11 + 0x18], r12
0025D90B  4D 89 6B 20                     mov qword ptr [r11 + 0x20], r13
0025D90F  4D 89 73 E0                     mov qword ptr [r11 - 0x20], r14
0025D913  4D 89 7B D8                     mov qword ptr [r11 - 0x28], r15
0025D917  F6 C1 01                        test cl, 1
0025D91A  0F 85 FC 14 00 00               jne 0x14025ee1c
0025D920  65 4C 8B 34 25 88 01 00 00      mov r14, qword ptr gs:[0x188]
0025D929  48 8D 5F 60                     lea rbx, [rdi + 0x60]
0025D92D  33 C0                           xor eax, eax
0025D92F  0F 57 C0                        xorps xmm0, xmm0
0025D932  0F 11 44 24 48                  movups xmmword ptr [rsp + 0x48], xmm0
0025D937  33 F6                           xor esi, esi
0025D939  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
0025D93E  48 89 74 24 48                  mov qword ptr [rsp + 0x48], rsi
0025D943  48 89 5C 24 50                  mov qword ptr [rsp + 0x50], rbx
0025D948  90                              nop
0025D949  45 0F 20 C7                     mov r15, cr8
0025D94D  41 BC 02 00 00 00               mov r12d, 2
0025D953  45 0F 22 C4                     mov cr8, r12
0025D957  39 05 C3 93 D6 00               cmp dword ptr [rip + 0xd693c3], eax
0025D95D  0F 85 76 06 00 00               jne 0x14025dfd9
0025D963  F6 05 9C 91 D6 00 21            test byte ptr [rip + 0xd6919c], 0x21
0025D96A  44 88 7C 24 58                  mov byte ptr [rsp + 0x58], r15b
0025D96F  0F 85 83 00 00 00               jne 0x14025d9f8
0025D975  48 8D 54 24 48                  lea rdx, [rsp + 0x48]
0025D97A  48 87 13                        xchg qword ptr [rbx], rdx
0025D97D  48 85 D2                        test rdx, rdx
0025D980  0F 85 C8 07 00 00               jne 0x14025e14e
0025D986  65 4C 8B 04 25 88 01 00 00      mov r8, qword ptr gs:[0x188]
0025D98F  0F B7 57 1A                     movzx edx, word ptr [rdi + 0x1a]
0025D993  0F B7 CA                        movzx ecx, dx
0025D996  66 83 E1 01                     and cx, 1
0025D99A  0F 85 81 07 00 00               jne 0x14025e121
0025D9A0  39 35 6A D2 C9 00               cmp dword ptr [rip + 0xc9d26a], esi
0025D9A6  0F 85 75 07 00 00               jne 0x14025e121
0025D9AC  84 D2                           test dl, dl
0025D9AE  0F 89 C0 02 00 00               jns 0x14025dc74
0025D9B4  8B 05 4A 91 D6 00               mov eax, dword ptr [rip + 0xd6914a]
0025D9BA  25 00 00 02 00                  and eax, 0x20000
0025D9BF  48 89 75 98                     mov qword ptr [rbp - 0x68], rsi
0025D9C3  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
0025D9C7  66 85 C9                        test cx, cx
0025D9CA  75 08                           jne 0x14025d9d4
0025D9CC  39 35 3E D2 C9 00               cmp dword ptr [rip + 0xc9d23e], esi
0025D9D2  74 44                           je 0x14025da18
0025D9D4  4C 39 77 30                     cmp qword ptr [rdi + 0x30], r14
0025D9D8  74 3E                           je 0x14025da18
0025D9DA  4C 8B 4F 10                     mov r9, qword ptr [rdi + 0x10]
0025D9DE  4D 8B C6                        mov r8, r14
0025D9E1  48 8B D7                        mov rdx, rdi
0025D9E4  48 C7 44 24 20 01 00 00 00      mov qword ptr [rsp + 0x20], 1
0025D9ED  B9 E3 00 00 00                  mov ecx, 0xe3
0025D9F2  E8 69 FC 29 00                  call 0x1404fd660
0025D9F7  CC                              int3
0025D9F8  8B 05 5A 04 CB 00               mov eax, dword ptr [rip + 0xcb045a]
0025D9FE  85 C0                           test eax, eax
0025DA00  0F 85 6F FF FF FF               jne 0x14025d975
0025DA06  48 8B D3                        mov rdx, rbx
0025DA09  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
0025DA0E  E8 3D 7E 01 00                  call 0x140275850
0025DA13  E9 6E FF FF FF                  jmp 0x14025d986
0025DA18  8B 4F 38                        mov ecx, dword ptr [rdi + 0x38]
0025DA1B  41 BF 01 00 00 00               mov r15d, 1
0025DA21  8B C1                           mov eax, ecx
0025DA23  83 E1 07                        and ecx, 7
0025DA26  C1 E8 03                        shr eax, 3
0025DA29  44 8D 2C C5 F8 FF FF FF         lea r13d, [rax*8 - 8]
0025DA31  44 0B E9                        or r13d, ecx
0025DA34  44 89 6F 38                     mov dword ptr [rdi + 0x38], r13d
0025DA38  41 C1 ED 03                     shr r13d, 3
0025DA3C  45 85 ED                        test r13d, r13d
0025DA3F  0F 85 C5 02 00 00               jne 0x14025dd0a
0025DA45  8B 47 38                        mov eax, dword ptr [rdi + 0x38]
0025DA48  48 8B 5F 30                     mov rbx, qword ptr [rdi + 0x30]
0025DA4C  41 84 C4                        test r12b, al
0025DA4F  0F 84 76 05 00 00               je 0x14025dfcb
0025DA55  48 83 E3 FC                     and rbx, 0xfffffffffffffffc
0025DA59  48 85 DB                        test rbx, rbx
0025DA5C  0F 84 95 00 00 00               je 0x14025daf7
0025DA62  41 84 C7                        test r15b, al
0025DA65  74 40                           je 0x14025daa7
0025DA67  45 32 F6                        xor r14b, r14b
0025DA6A  45 32 FF                        xor r15b, r15b
0025DA6D  39 35 15 95 D6 00               cmp dword ptr [rip + 0xd69515], esi
0025DA73  4C 8B EE                        mov r13, rsi
0025DA76  0F 85 05 12 00 00               jne 0x14025ec81
0025DA7C  39 B3 E0 05 00 00               cmp dword ptr [rbx + 0x5e0], esi
0025DA82  0F 84 40 13 00 00               je 0x14025edc8
0025DA88  F0 FF 8B E0 05 00 00            lock dec dword ptr [rbx + 0x5e0]
0025DA8F  45 84 F6                        test r14b, r14b
0025DA92  0F 85 EE 13 00 00               jne 0x14025ee86
0025DA98  8B 47 38                        mov eax, dword ptr [rdi + 0x38]
0025DA9B  41 BF 01 00 00 00               mov r15d, 1
0025DAA1  83 E0 FE                        and eax, 0xfffffffe
0025DAA4  89 47 38                        mov dword ptr [rdi + 0x38], eax
0025DAA7  A8 04                           test al, 4
0025DAA9  74 10                           je 0x14025dabb
0025DAAB  F0 FF 8B E4 05 00 00            lock dec dword ptr [rbx + 0x5e4]
0025DAB2  8B 47 38                        mov eax, dword ptr [rdi + 0x38]
0025DAB5  83 E0 FB                        and eax, 0xfffffffb
0025DAB8  89 47 38                        mov dword ptr [rdi + 0x38], eax
0025DABB  41 84 C4                        test r12b, al
0025DABE  74 37                           je 0x14025daf7
0025DAC0  39 35 4A 75 D6 00               cmp dword ptr [rip + 0xd6754a], esi
0025DAC6  74 14                           je 0x14025dadc
0025DAC8  41 B9 44 66 6C 74               mov r9d, 0x746c6644
0025DACE  48 8D 4B D0                     lea rcx, [rbx - 0x30]
0025DAD2  45 8B C7                        mov r8d, r15d
0025DAD5  33 D2                           xor edx, edx
0025DAD7  E8 08 2F FB FF                  call 0x1402109e4
0025DADC  48 C7 C0 FF FF FF FF            mov rax, 0xffffffffffffffff
0025DAE3  F0 48 0F C1 43 D0               lock xadd qword ptr [rbx - 0x30], rax
0025DAE9  48 83 E8 01                     sub rax, 1
0025DAED  0F 8E AB 10 00 00               jle 0x14025eb9e
0025DAF3  83 67 38 FD                     and dword ptr [rdi + 0x38], 0xfffffffd
0025DAF7  48 89 77 30                     mov qword ptr [rdi + 0x30], rsi
0025DAFB  4C 8B F6                        mov r14, rsi
0025DAFE  8B 4F 48                        mov ecx, dword ptr [rdi + 0x48]
0025DB01  8B 47 44                        mov eax, dword ptr [rdi + 0x44]
0025DB04  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
0025DB08  85 C9                           test ecx, ecx
0025DB0A  0F 84 DD 01 00 00               je 0x14025dced
0025DB10  48 8B 47 20                     mov rax, qword ptr [rdi + 0x20]
0025DB14  BA 7F FF 00 00                  mov edx, 0xff7f
0025DB19  48 89 77 20                     mov qword ptr [rdi + 0x20], rsi
0025DB1D  66 21 57 1A                     and word ptr [rdi + 0x1a], dx
0025DB21  48 89 45 98                     mov qword ptr [rbp - 0x68], rax
0025DB25  89 77 48                        mov dword ptr [rdi + 0x48], esi
0025DB28  8B 57 40                        mov edx, dword ptr [rdi + 0x40]
0025DB2B  FF CA                           dec edx
0025DB2D  03 D1                           add edx, ecx
0025DB2F  89 57 40                        mov dword ptr [rdi + 0x40], edx
0025DB32  39 77 4C                        cmp dword ptr [rdi + 0x4c], esi
0025DB35  75 0E                           jne 0x14025db45
0025DB37  39 77 48                        cmp dword ptr [rdi + 0x48], esi
0025DB3A  75 09                           jne 0x14025db45
0025DB3C  B9 F9 00 00 00                  mov ecx, 0xf9
0025DB41  66 21 4F 1A                     and word ptr [rdi + 0x1a], cx
0025DB45  44 0F B6 6F 1B                  movzx r13d, byte ptr [rdi + 0x1b]
0025DB4A  4D 85 F6                        test r14, r14
0025DB4D  74 10                           je 0x14025db5f
0025DB4F  8B 47 38                        mov eax, dword ptr [rdi + 0x38]
0025DB52  83 E0 07                        and eax, 7
0025DB55  4C 89 77 30                     mov qword ptr [rdi + 0x30], r14
0025DB59  83 C8 08                        or eax, 8
0025DB5C  89 47 38                        mov dword ptr [rdi + 0x38], eax
0025DB5F  F6 05 A0 8F D6 00 01            test byte ptr [rip + 0xd68fa0], 1
0025DB66  0F 85 9B 00 00 00               jne 0x14025dc07
0025DB6C  0F 0D 4C 24 48                  prefetchw byte ptr [rsp + 0x48]
0025DB71  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
0025DB76  48 85 C0                        test rax, rax
0025DB79  75 27                           jne 0x14025dba2
0025DB7B  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
0025DB80  48 8D 44 24 48                  lea rax, [rsp + 0x48]
0025DB85  F0 48 0F B1 31                  lock cmpxchg qword ptr [rcx], rsi
0025DB8A  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
0025DB8F  48 3B C1                        cmp rax, rcx
0025DB92  0F 84 8B 00 00 00               je 0x14025dc23
0025DB98  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
0025DB9D  E8 FE 9E FB FF                  call 0x140217aa0
0025DBA2  4C 8D 40 08                     lea r8, [rax + 8]
0025DBA6  48 89 74 24 48                  mov qword ptr [rsp + 0x48], rsi
0025DBAB  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
0025DBB0  48 8B C1                        mov rax, rcx
0025DBB3  49 87 00                        xchg qword ptr [r8], rax
0025DBB6  32 C1                           xor al, cl
0025DBB8  A8 04                           test al, 4
0025DBBA  74 67                           je 0x14025dc23
0025DBBC  F0 09 34 24                     lock or dword ptr [rsp], esi
0025DBC0  49 C1 E8 05                     shr r8, 5
0025DBC4  4C 8D 15 35 24 DA FF            lea r10, [rip - 0x25dbcb]
0025DBCB  41 83 E0 7F                     and r8d, 0x7f
0025DBCF  E8 0C A0 FB FF                  call 0x140217be0
0025DBD4  48 8B D6                        mov rdx, rsi
0025DBD7  0F B6 D8                        movzx ebx, al
0025DBDA  4B 87 94 C2 20 1B F2 00         xchg qword ptr [r10 + r8*8 + 0xf21b20], rdx
0025DBE2  E8 0D 9F FB FF                  call 0x140217af4
0025DBE7  84 DB                           test bl, bl
0025DBE9  74 38                           je 0x14025dc23
0025DBEB  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
0025DBF4  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
0025DBFB  4D 85 C0                        test r8, r8
0025DBFE  0F 85 92 0C 00 00               jne 0x14025e896
0025DC04  FB                              sti
0025DC05  EB 1C                           jmp 0x14025dc23
0025DC07  8B 05 4B 02 CB 00               mov eax, dword ptr [rip + 0xcb024b]
0025DC0D  85 C0                           test eax, eax
0025DC0F  0F 85 57 FF FF FF               jne 0x14025db6c
0025DC15  48 8B 55 48                     mov rdx, qword ptr [rbp + 0x48]
0025DC19  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
0025DC1E  E8 CD 9D FB FF                  call 0x1402179f0
0025DC23  39 35 F7 90 D6 00               cmp dword ptr [rip + 0xd690f7], esi
0025DC29  0F B6 5C 24 58                  movzx ebx, byte ptr [rsp + 0x58]
0025DC2E  74 0C                           je 0x14025dc3c
0025DC30  44 0F 20 C1                     mov rcx, cr8
0025DC34  0F B6 D3                        movzx edx, bl
0025DC37  E8 5C 7A 29 00                  call 0x1404f5698
0025DC3C  44 0F 22 C3                     mov cr8, rbx
0025DC40  4D 85 F6                        test r14, r14
0025DC43  B8 01 00 00 00                  mov eax, 1
0025DC48  8B D8                           mov ebx, eax
0025DC4A  41 BF 03 00 00 00               mov r15d, 3
0025DC50  41 0F 45 DF                     cmovne ebx, r15d
0025DC54  44 8B F0                        mov r14d, eax
0025DC57  48 39 75 98                     cmp qword ptr [rbp - 0x68], rsi
0025DC5B  0F 85 35 04 00 00               jne 0x14025e096
0025DC61  41 BE 22 00 01 00               mov r14d, 0x10022
0025DC67  44 8B EE                        mov r13d, esi
0025DC6A  44 89 74 24 68                  mov dword ptr [rsp + 0x68], r14d
0025DC6F  E9 EE 00 00 00                  jmp 0x14025dd62
0025DC74  44 8B 2D 89 8E D6 00            mov r13d, dword ptr [rip + 0xd68e89]
0025DC7B  48 8B DE                        mov rbx, rsi
0025DC7E  41 81 E5 00 00 02 00            and r13d, 0x20000
0025DC85  48 89 5D A0                     mov qword ptr [rbp - 0x60], rbx
0025DC89  41 F6 C6 03                     test r14b, 3
0025DC8D  0F 85 FC 0B 00 00               jne 0x14025e88f
0025DC93  41 0F B6 86 60 04 00 00         movzx eax, byte ptr [r14 + 0x460]
0025DC9B  4C 8B 47 30                     mov r8, qword ptr [rdi + 0x30]
0025DC9F  48 8D 57 30                     lea rdx, [rdi + 0x30]
0025DCA3  4D 3B C6                        cmp r8, r14
0025DCA6  0F 84 CD 04 00 00               je 0x14025e179
0025DCAC  4D 85 C0                        test r8, r8
0025DCAF  48 8B CE                        mov rcx, rsi
0025DCB2  0F 95 C1                        setne cl
0025DCB5  85 C0                           test eax, eax
0025DCB7  0F 85 2E 03 00 00               jne 0x14025dfeb
0025DCBD  44 8B 47 48                     mov r8d, dword ptr [rdi + 0x48]
0025DCC1  8B 47 40                        mov eax, dword ptr [rdi + 0x40]
0025DCC4  48 8B 57 10                     mov rdx, qword ptr [rdi + 0x10]
0025DCC8  4C 03 C0                        add r8, rax
0025DCCB  48 85 D2                        test rdx, rdx
0025DCCE  0F 85 45 03 00 00               jne 0x14025e019
0025DCD4  4C 8B CA                        mov r9, rdx
0025DCD7  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
0025DCDC  48 8B D7                        mov rdx, rdi
0025DCDF  4D 8B C6                        mov r8, r14
0025DCE2  B9 E3 00 00 00                  mov ecx, 0xe3
0025DCE7  E8 74 F9 29 00                  call 0x1404fd660
0025DCEC  CC                              int3
0025DCED  39 77 4C                        cmp dword ptr [rdi + 0x4c], esi
0025DCF0  0F 85 62 03 00 00               jne 0x14025e058
0025DCF6  BA 7F FF 00 00                  mov edx, 0xff7f
0025DCFB  66 89 77 18                     mov word ptr [rdi + 0x18], si
0025DCFF  66 21 57 1A                     and word ptr [rdi + 0x1a], dx
0025DD03  8B D6                           mov edx, esi
0025DD05  E9 25 FE FF FF                  jmp 0x14025db2f
0025DD0A  44 84 3D F5 8D D6 00            test byte ptr [rip + 0xd68df5], r15b
0025DD11  41 BE 32 00 01 00               mov r14d, 0x10032
0025DD17  8B 47 44                        mov eax, dword ptr [rdi + 0x44]
0025DD1A  44 89 74 24 68                  mov dword ptr [rsp + 0x68], r14d
0025DD1F  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
0025DD23  0F 84 FC 01 00 00               je 0x14025df25
0025DD29  8B 05 29 01 CB 00               mov eax, dword ptr [rip + 0xcb0129]
0025DD2F  85 C0                           test eax, eax
0025DD31  0F 85 EE 01 00 00               jne 0x14025df25
0025DD37  48 8B 55 48                     mov rdx, qword ptr [rbp + 0x48]
0025DD3B  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
0025DD40  E8 AB 9C FB FF                  call 0x1402179f0
0025DD45  39 35 D5 8F D6 00               cmp dword ptr [rip + 0xd68fd5], esi
0025DD4B  0F B6 5C 24 58                  movzx ebx, byte ptr [rsp + 0x58]
0025DD50  74 0C                           je 0x14025dd5e
0025DD52  44 0F 20 C1                     mov rcx, cr8
0025DD56  0F B6 D3                        movzx edx, bl
0025DD59  E8 3A 79 29 00                  call 0x1404f5698
0025DD5E  44 0F 22 C3                     mov cr8, rbx
0025DD62  65 FF 04 25 6C 90 00 00         inc dword ptr gs:[0x906c]
0025DD6A  39 74 24 60                     cmp dword ptr [rsp + 0x60], esi
0025DD6E  0F 84 34 08 00 00               je 0x14025e5a8
0025DD74  0F 57 C0                        xorps xmm0, xmm0
0025DD77  0F 11 45 A8                     movups xmmword ptr [rbp - 0x58], xmm0
0025DD7B  0F 11 45 B8                     movups xmmword ptr [rbp - 0x48], xmm0
0025DD7F  0F 11 45 C8                     movups xmmword ptr [rbp - 0x38], xmm0
0025DD83  0F 31                           rdtsc
0025DD85  65 4C 8B 3C 25 20 00 00 00      mov r15, qword ptr gs:[0x20]
0025DD8E  48 C1 E2 20                     shl rdx, 0x20
0025DD92  48 0B C2                        or rax, rdx
0025DD95  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
0025DD9A  41 FF 87 70 8F 00 00            inc dword ptr [r15 + 0x8f70]
0025DDA1  41 0F B6 87 D0 00 00 00         movzx eax, byte ptr [r15 + 0xd0]
0025DDA9  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0025DDB2  66 89 44 24 40                  mov word ptr [rsp + 0x40], ax
0025DDB7  41 0F B6 87 D1 00 00 00         movzx eax, byte ptr [r15 + 0xd1]
0025DDBF  88 44 24 30                     mov byte ptr [rsp + 0x30], al
0025DDC3  48 39 B1 20 06 00 00            cmp qword ptr [rcx + 0x620], rsi
0025DDCA  0F 84 D8 07 00 00               je 0x14025e5a8
0025DDD0  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0025DDD9  41 8B D6                        mov edx, r14d
0025DDDC  81 E2 00 00 FF FF               and edx, 0xffff0000
0025DDE2  48 89 4D 90                     mov qword ptr [rbp - 0x70], rcx
0025DDE6  89 54 24 38                     mov dword ptr [rsp + 0x38], edx
0025DDEA  8B 81 A0 05 00 00               mov eax, dword ptr [rcx + 0x5a0]
0025DDF0  A8 01                           test al, 1
0025DDF2  0F 85 B0 07 00 00               jne 0x14025e5a8
0025DDF8  4C 8B B1 20 06 00 00            mov r14, qword ptr [rcx + 0x620]
0025DDFF  44 8B 05 62 A6 C0 00            mov r8d, dword ptr [rip + 0xc0a662]
0025DE06  44 89 44 24 60                  mov dword ptr [rsp + 0x60], r8d
0025DE0B  4D 85 F6                        test r14, r14
0025DE0E  75 5C                           jne 0x14025de6c
0025DE10  BA 00 02 00 00                  mov edx, 0x200
0025DE15  41 8D 4E 48                     lea ecx, [r14 + 0x48]
0025DE19  41 B8 52 65 54 72               mov r8d, 0x72546552
0025DE1F  E8 CC 42 92 00                  call 0x140b820f0
0025DE24  48 8B D8                        mov rbx, rax
0025DE27  48 85 C0                        test rax, rax
0025DE2A  0F 84 78 07 00 00               je 0x14025e5a8
0025DE30  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
0025DE34  48 89 78 10                     mov qword ptr [rax + 0x10], rdi
0025DE38  8B 44 24 38                     mov eax, dword ptr [rsp + 0x38]
0025DE3C  89 43 1C                        mov dword ptr [rbx + 0x1c], eax
0025DE3F  8B 44 24 60                     mov eax, dword ptr [rsp + 0x60]
0025DE43  89 43 28                        mov dword ptr [rbx + 0x28], eax
0025DE46  33 C0                           xor eax, eax
0025DE48  89 73 20                        mov dword ptr [rbx + 0x20], esi
0025DE4B  F0 48 0F B1 99 20 06 00 00      lock cmpxchg qword ptr [rcx + 0x620], rbx
0025DE54  4C 8B F0                        mov r14, rax
0025DE57  74 79                           je 0x14025ded2
0025DE59  33 D2                           xor edx, edx
0025DE5B  48 8B CB                        mov rcx, rbx
0025DE5E  E8 0D 4A 92 00                  call 0x140b82870
0025DE63  8B 54 24 38                     mov edx, dword ptr [rsp + 0x38]
0025DE67  44 8B 44 24 60                  mov r8d, dword ptr [rsp + 0x60]
0025DE6C  48 8B C6                        mov rax, rsi
0025DE6F  8B CE                           mov ecx, esi
0025DE71  83 F9 08                        cmp ecx, 8
0025DE74  73 2C                           jae 0x14025dea2
0025DE76  45 8B 4E 1C                     mov r9d, dword ptr [r14 + 0x1c]
0025DE7A  44 3B CA                        cmp r9d, edx
0025DE7D  75 0C                           jne 0x14025de8b
0025DE7F  49 39 7E 10                     cmp qword ptr [r14 + 0x10], rdi
0025DE83  75 06                           jne 0x14025de8b
0025DE85  45 39 46 28                     cmp dword ptr [r14 + 0x28], r8d
0025DE89  74 3B                           je 0x14025dec6
0025DE8B  48 85 C0                        test rax, rax
0025DE8E  0F 85 86 00 00 00               jne 0x14025df1a
0025DE94  45 85 C9                        test r9d, r9d
0025DE97  74 7E                           je 0x14025df17
0025DE99  45 39 46 28                     cmp dword ptr [r14 + 0x28], r8d
0025DE9D  7D 7B                           jge 0x14025df1a
0025DE9F  49 8B C6                        mov rax, r14
0025DEA2  4C 8B F0                        mov r14, rax
0025DEA5  48 85 C0                        test rax, rax
0025DEA8  74 1C                           je 0x14025dec6
0025DEAA  48 89 78 10                     mov qword ptr [rax + 0x10], rdi
0025DEAE  89 50 1C                        mov dword ptr [rax + 0x1c], edx
0025DEB1  48 89 70 20                     mov qword ptr [rax + 0x20], rsi
0025DEB5  48 89 30                        mov qword ptr [rax], rsi
0025DEB8  48 89 70 08                     mov qword ptr [rax + 8], rsi
0025DEBC  89 70 18                        mov dword ptr [rax + 0x18], esi
0025DEBF  44 89 40 28                     mov dword ptr [rax + 0x28], r8d
0025DEC3  89 70 2C                        mov dword ptr [rax + 0x2c], esi
0025DEC6  49 8B DE                        mov rbx, r14
0025DEC9  4D 85 F6                        test r14, r14
0025DECC  0F 84 D6 06 00 00               je 0x14025e5a8
0025DED2  39 73 20                        cmp dword ptr [rbx + 0x20], esi
0025DED5  0F 84 85 06 00 00               je 0x14025e560
0025DEDB  41 FF 87 74 8F 00 00            inc dword ptr [r15 + 0x8f74]
0025DEE2  41 FF C5                        inc r13d
0025DEE5  44 39 6B 24                     cmp dword ptr [rbx + 0x24], r13d
0025DEE9  0F 82 58 10 00 00               jb 0x14025ef47
0025DEEF  44 8B 44 24 68                  mov r8d, dword ptr [rsp + 0x68]
0025DEF4  41 81 F8 22 00 01 00            cmp r8d, 0x10022
0025DEFB  0F 84 16 06 00 00               je 0x14025e517
0025DF01  41 81 F8 32 00 01 00            cmp r8d, 0x10032
0025DF08  0F 85 9A 06 00 00               jne 0x14025e5a8
0025DF0E  44 89 63 20                     mov dword ptr [rbx + 0x20], r12d
0025DF12  E9 91 06 00 00                  jmp 0x14025e5a8
0025DF17  49 8B C6                        mov rax, r14
0025DF1A  49 83 C6 40                     add r14, 0x40
0025DF1E  FF C1                           inc ecx
0025DF20  E9 4C FF FF FF                  jmp 0x14025de71
0025DF25  0F 0D 4C 24 48                  prefetchw byte ptr [rsp + 0x48]
0025DF2A  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
0025DF2F  48 85 C0                        test rax, rax
0025DF32  75 27                           jne 0x14025df5b
0025DF34  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
0025DF39  48 8D 44 24 48                  lea rax, [rsp + 0x48]
0025DF3E  F0 48 0F B1 31                  lock cmpxchg qword ptr [rcx], rsi
0025DF43  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
0025DF48  48 3B C1                        cmp rax, rcx
0025DF4B  0F 84 F4 FD FF FF               je 0x14025dd45
0025DF51  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
0025DF56  E8 45 9B FB FF                  call 0x140217aa0
0025DF5B  4C 8D 40 08                     lea r8, [rax + 8]
0025DF5F  48 89 74 24 48                  mov qword ptr [rsp + 0x48], rsi
0025DF64  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
0025DF69  48 8B C1                        mov rax, rcx
0025DF6C  49 87 00                        xchg qword ptr [r8], rax
0025DF6F  32 C1                           xor al, cl
0025DF71  A8 04                           test al, 4
0025DF73  0F 84 CC FD FF FF               je 0x14025dd45
0025DF79  F0 09 34 24                     lock or dword ptr [rsp], esi
0025DF7D  49 C1 E8 05                     shr r8, 5
0025DF81  4C 8D 15 78 20 DA FF            lea r10, [rip - 0x25df88]
0025DF88  41 83 E0 7F                     and r8d, 0x7f
0025DF8C  E8 4F 9C FB FF                  call 0x140217be0
0025DF91  48 8B D6                        mov rdx, rsi
0025DF94  0F B6 D8                        movzx ebx, al
0025DF97  4B 87 94 C2 20 1B F2 00         xchg qword ptr [r10 + r8*8 + 0xf21b20], rdx
0025DF9F  E8 50 9B FB FF                  call 0x140217af4
0025DFA4  84 DB                           test bl, bl
0025DFA6  0F 84 99 FD FF FF               je 0x14025dd45
0025DFAC  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
0025DFB5  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
0025DFBC  4D 85 C0                        test r8, r8
0025DFBF  0F 85 7F 07 00 00               jne 0x14025e744
0025DFC5  FB                              sti
0025DFC6  E9 7A FD FF FF                  jmp 0x14025dd45
0025DFCB  F6 C3 03                        test bl, 3
0025DFCE  0F 85 23 FB FF FF               jne 0x14025daf7
0025DFD4  E9 80 FA FF FF                  jmp 0x14025da59
0025DFD9  41 0F B6 D4                     movzx edx, r12b
0025DFDD  41 0F B6 CF                     movzx ecx, r15b
0025DFE1  E8 16 77 29 00                  call 0x1404f56fc
0025DFE6  E9 78 F9 FF FF                  jmp 0x14025d963
0025DFEB  4C 8B 47 10                     mov r8, qword ptr [rdi + 0x10]
0025DFEF  4D 85 C0                        test r8, r8
0025DFF2  0F 84 C5 FC FF FF               je 0x14025dcbd
0025DFF8  41 3B 40 08                     cmp eax, dword ptr [r8 + 8]
0025DFFC  0F 83 BB FC FF FF               jae 0x14025dcbd
0025E002  8B D0                           mov edx, eax
0025E004  48 C1 E2 04                     shl rdx, 4
0025E008  49 03 D0                        add rdx, r8
0025E00B  4C 39 32                        cmp qword ptr [rdx], r14
0025E00E  0F 85 A9 FC FF FF               jne 0x14025dcbd
0025E014  E9 60 01 00 00                  jmp 0x14025e179
0025E019  44 8B 4A 08                     mov r9d, dword ptr [rdx + 8]
0025E01D  49 C1 E1 04                     shl r9, 4
0025E021  4C 03 CA                        add r9, rdx
0025E024  48 83 C2 10                     add rdx, 0x10
0025E028  49 3B C8                        cmp rcx, r8
0025E02B  73 22                           jae 0x14025e04f
0025E02D  48 8B 02                        mov rax, qword ptr [rdx]
0025E030  49 3B C6                        cmp rax, r14
0025E033  0F 84 24 01 00 00               je 0x14025e15d
0025E039  48 85 C0                        test rax, rax
0025E03C  74 08                           je 0x14025e046
0025E03E  48 FF C1                        inc rcx
0025E041  49 3B C8                        cmp rcx, r8
0025E044  74 09                           je 0x14025e04f
0025E046  48 83 C2 10                     add rdx, 0x10
0025E04A  49 3B D1                        cmp rdx, r9
0025E04D  75 DE                           jne 0x14025e02d
0025E04F  48 8B 57 10                     mov rdx, qword ptr [rdi + 0x10]
0025E053  E9 7C FC FF FF                  jmp 0x14025dcd4
0025E058  48 8B 4F 28                     mov rcx, qword ptr [rdi + 0x28]
0025E05C  48 85 C9                        test rcx, rcx
0025E05F  0F 84 D4 06 00 00               je 0x14025e739
0025E065  48 8B 01                        mov rax, qword ptr [rcx]
0025E068  48 3B C1                        cmp rax, rcx
0025E06B  0F 84 A8 06 00 00               je 0x14025e719
0025E071  48 89 47 28                     mov qword ptr [rdi + 0x28], rax
0025E075  48 8B 11                        mov rdx, qword ptr [rcx]
0025E078  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
0025E07C  48 39 4A 08                     cmp qword ptr [rdx + 8], rcx
0025E080  75 09                           jne 0x14025e08b
0025E082  48 39 08                        cmp qword ptr [rax], rcx
0025E085  0F 84 49 08 00 00               je 0x14025e8d4
0025E08B  41 BF 03 00 00 00               mov r15d, 3
0025E091  E9 86 00 00 00                  jmp 0x14025e11c
0025E096  44 0F 20 C0                     mov rax, cr8
0025E09A  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
0025E09E  45 0F 22 C4                     mov cr8, r12
0025E0A2  39 35 78 8C D6 00               cmp dword ptr [rip + 0xd68c78], esi
0025E0A8  0F 85 32 08 00 00               jne 0x14025e8e0
0025E0AE  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
0025E0B7  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
0025E0BB  48 8B 45 98                     mov rax, qword ptr [rbp - 0x68]
0025E0BF  48 8B 08                        mov rcx, qword ptr [rax]
0025E0C2  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
0025E0C6  48 83 C0 18                     add rax, 0x18
0025E0CA  48 89 4C 24 78                  mov qword ptr [rsp + 0x78], rcx
0025E0CF  48 8B C8                        mov rcx, rax
0025E0D2  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
0025E0D7  E8 B4 3B FF FF                  call 0x140251c90
0025E0DC  48 8B 45 80                     mov rax, qword ptr [rbp - 0x80]
0025E0E0  4C 8D 48 18                     lea r9, [rax + 0x18]
0025E0E4  44 89 70 1C                     mov dword ptr [rax + 0x1c], r14d
0025E0E8  49 8B 41 08                     mov rax, qword ptr [r9 + 8]
0025E0EC  49 8D 49 08                     lea rcx, [r9 + 8]
0025E0F0  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
0025E0F5  48 3B C1                        cmp rax, rcx
0025E0F8  0F 84 C1 05 00 00               je 0x14025e6bf
0025E0FE  48 8B 10                        mov rdx, qword ptr [rax]
0025E101  48 8B C8                        mov rcx, rax
0025E104  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0025E108  48 89 54 24 68                  mov qword ptr [rsp + 0x68], rdx
0025E10D  48 39 4A 08                     cmp qword ptr [rdx + 8], rcx
0025E111  75 09                           jne 0x14025e11c
0025E113  48 39 08                        cmp qword ptr [rax], rcx
0025E116  0F 84 5A 05 00 00               je 0x14025e676
0025E11C  49 8B CF                        mov rcx, r15
0025E11F  CD 29                           int 0x29
0025E121  41 0F B6 C6                     movzx eax, r14b
0025E125  24 03                           and al, 3
0025E127  3C 03                           cmp al, 3
0025E129  0F 84 7D F8 FF FF               je 0x14025d9ac
0025E12F  4D 3B F0                        cmp r14, r8
0025E132  0F 84 74 F8 FF FF               je 0x14025d9ac
0025E138  4D 8B CE                        mov r9, r14
0025E13B  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
0025E140  48 8B D7                        mov rdx, rdi
0025E143  B9 6E 01 00 00                  mov ecx, 0x16e
0025E148  E8 13 F5 29 00                  call 0x1404fd660
0025E14D  CC                              int3
0025E14E  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
0025E153  E8 58 9D FF FF                  call 0x140257eb0
0025E158  E9 29 F8 FF FF                  jmp 0x14025d986
0025E15D  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0025E166  8B C2                           mov eax, edx
0025E168  2B 47 10                        sub eax, dword ptr [rdi + 0x10]
0025E16B  48 8B 5D A0                     mov rbx, qword ptr [rbp - 0x60]
0025E16F  48 C1 F8 04                     sar rax, 4
0025E173  88 81 60 04 00 00               mov byte ptr [rcx + 0x460], al
0025E179  8B 4A 08                        mov ecx, dword ptr [rdx + 8]
0025E17C  8B C1                           mov eax, ecx
0025E17E  C1 E8 03                        shr eax, 3
0025E181  83 E1 07                        and ecx, 7
0025E184  44 8D 34 C5 F8 FF FF FF         lea r14d, [rax*8 - 8]
0025E18C  44 0B F1                        or r14d, ecx
0025E18F  44 89 72 08                     mov dword ptr [rdx + 8], r14d
0025E193  41 C1 EE 03                     shr r14d, 3
0025E197  44 89 74 24 60                  mov dword ptr [rsp + 0x60], r14d
0025E19C  45 85 F6                        test r14d, r14d
0025E19F  0F 85 31 01 00 00               jne 0x14025e2d6
0025E1A5  48 8B CA                        mov rcx, rdx
0025E1A8  E8 93 15 FB FF                  call 0x14020f740
0025E1AD  83 7F 40 01                     cmp dword ptr [rdi + 0x40], 1
0025E1B1  4C 8B F6                        mov r14, rsi
0025E1B4  8B 47 44                        mov eax, dword ptr [rdi + 0x44]
0025E1B7  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
0025E1BB  77 14                           ja 0x14025e1d1
0025E1BD  39 77 4C                        cmp dword ptr [rdi + 0x4c], esi
0025E1C0  0F 85 97 07 00 00               jne 0x14025e95d
0025E1C6  8B 4F 48                        mov ecx, dword ptr [rdi + 0x48]
0025E1C9  85 C9                           test ecx, ecx
0025E1CB  0F 85 9C 0A 00 00               jne 0x14025ec6d
0025E1D1  8B CE                           mov ecx, esi
0025E1D3  8B 47 40                        mov eax, dword ptr [rdi + 0x40]
0025E1D6  FF C8                           dec eax
0025E1D8  03 C8                           add ecx, eax
0025E1DA  89 4F 40                        mov dword ptr [rdi + 0x40], ecx
0025E1DD  75 04                           jne 0x14025e1e3
0025E1DF  66 89 77 18                     mov word ptr [rdi + 0x18], si
0025E1E3  39 77 4C                        cmp dword ptr [rdi + 0x4c], esi
0025E1E6  75 0E                           jne 0x14025e1f6
0025E1E8  39 77 48                        cmp dword ptr [rdi + 0x48], esi
0025E1EB  75 09                           jne 0x14025e1f6
0025E1ED  B9 F9 00 00 00                  mov ecx, 0xf9
0025E1F2  66 21 4F 1A                     and word ptr [rdi + 0x1a], cx
0025E1F6  0F B6 47 1B                     movzx eax, byte ptr [rdi + 0x1b]
0025E1FA  89 44 24 68                     mov dword ptr [rsp + 0x68], eax
0025E1FE  4D 85 F6                        test r14, r14
0025E201  74 10                           je 0x14025e213
0025E203  8B 47 38                        mov eax, dword ptr [rdi + 0x38]
0025E206  83 E0 07                        and eax, 7
0025E209  4C 89 77 30                     mov qword ptr [rdi + 0x30], r14
0025E20D  83 C8 08                        or eax, 8
0025E210  89 47 38                        mov dword ptr [rdi + 0x38], eax
0025E213  F6 05 EC 88 D6 00 01            test byte ptr [rip + 0xd688ec], 1
0025E21A  75 53                           jne 0x14025e26f
0025E21C  0F 0D 4C 24 48                  prefetchw byte ptr [rsp + 0x48]
0025E221  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
0025E226  48 85 C0                        test rax, rax
0025E229  75 23                           jne 0x14025e24e
0025E22B  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
0025E230  48 8D 44 24 48                  lea rax, [rsp + 0x48]
0025E235  F0 48 0F B1 31                  lock cmpxchg qword ptr [rcx], rsi
0025E23A  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
0025E23F  48 3B C1                        cmp rax, rcx
0025E242  74 43                           je 0x14025e287
0025E244  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
0025E249  E8 52 98 FB FF                  call 0x140217aa0
0025E24E  48 8D 48 08                     lea rcx, [rax + 8]
0025E252  48 89 74 24 48                  mov qword ptr [rsp + 0x48], rsi
0025E257  48 8B 54 24 50                  mov rdx, qword ptr [rsp + 0x50]
0025E25C  48 8B C2                        mov rax, rdx
0025E25F  48 87 01                        xchg qword ptr [rcx], rax
0025E262  32 C2                           xor al, dl
0025E264  A8 04                           test al, 4
0025E266  74 1F                           je 0x14025e287
0025E268  E8 B3 99 FB FF                  call 0x140217c20
0025E26D  EB 18                           jmp 0x14025e287
0025E26F  8B 05 E3 FB CA 00               mov eax, dword ptr [rip + 0xcafbe3]
0025E275  85 C0                           test eax, eax
0025E277  75 A3                           jne 0x14025e21c
0025E279  48 8B 55 48                     mov rdx, qword ptr [rbp + 0x48]
0025E27D  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
0025E282  E8 69 97 FB FF                  call 0x1402179f0
0025E287  39 35 93 8A D6 00               cmp dword ptr [rip + 0xd68a93], esi
0025E28D  0F B6 5C 24 58                  movzx ebx, byte ptr [rsp + 0x58]
0025E292  74 0C                           je 0x14025e2a0
0025E294  44 0F 20 C1                     mov rcx, cr8
0025E298  0F B6 D3                        movzx edx, bl
0025E29B  E8 F8 73 29 00                  call 0x1404f5698
0025E2A0  44 0F 22 C3                     mov cr8, rbx
0025E2A4  4D 85 F6                        test r14, r14
0025E2A7  B8 01 00 00 00                  mov eax, 1
0025E2AC  8B D8                           mov ebx, eax
0025E2AE  41 BF 03 00 00 00               mov r15d, 3
0025E2B4  41 0F 45 DF                     cmovne ebx, r15d
0025E2B8  44 8B F0                        mov r14d, eax
0025E2BB  48 39 75 A0                     cmp qword ptr [rbp - 0x60], rsi
0025E2BF  0F 85 A7 04 00 00               jne 0x14025e76c
0025E2C5  41 BE 42 00 01 00               mov r14d, 0x10042
0025E2CB  89 74 24 60                     mov dword ptr [rsp + 0x60], esi
0025E2CF  44 89 74 24 38                  mov dword ptr [rsp + 0x38], r14d
0025E2D4  EB 58                           jmp 0x14025e32e
0025E2D6  F6 05 29 88 D6 00 01            test byte ptr [rip + 0xd68829], 1
0025E2DD  41 BE 52 00 01 00               mov r14d, 0x10052
0025E2E3  8B 47 44                        mov eax, dword ptr [rdi + 0x44]
0025E2E6  44 89 74 24 38                  mov dword ptr [rsp + 0x38], r14d
0025E2EB  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
0025E2EF  0F 84 23 03 00 00               je 0x14025e618
0025E2F5  8B 05 5D FB CA 00               mov eax, dword ptr [rip + 0xcafb5d]
0025E2FB  85 C0                           test eax, eax
0025E2FD  0F 85 15 03 00 00               jne 0x14025e618
0025E303  48 8B 55 48                     mov rdx, qword ptr [rbp + 0x48]
0025E307  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
0025E30C  E8 DF 96 FB FF                  call 0x1402179f0
0025E311  39 35 09 8A D6 00               cmp dword ptr [rip + 0xd68a09], esi
0025E317  0F B6 5C 24 58                  movzx ebx, byte ptr [rsp + 0x58]
0025E31C  74 0C                           je 0x14025e32a
0025E31E  44 0F 20 C1                     mov rcx, cr8
0025E322  0F B6 D3                        movzx edx, bl
0025E325  E8 6E 73 29 00                  call 0x1404f5698
0025E32A  44 0F 22 C3                     mov cr8, rbx
0025E32E  65 FF 04 25 70 90 00 00         inc dword ptr gs:[0x9070]
0025E336  45 85 ED                        test r13d, r13d
0025E339  0F 84 69 02 00 00               je 0x14025e5a8
0025E33F  0F 57 C0                        xorps xmm0, xmm0
0025E342  0F 11 45 D8                     movups xmmword ptr [rbp - 0x28], xmm0
0025E346  0F 11 45 E8                     movups xmmword ptr [rbp - 0x18], xmm0
0025E34A  0F 11 45 F8                     movups xmmword ptr [rbp - 8], xmm0
0025E34E  0F 31                           rdtsc
0025E350  65 4C 8B 2C 25 20 00 00 00      mov r13, qword ptr gs:[0x20]
0025E359  48 C1 E2 20                     shl rdx, 0x20
0025E35D  48 0B C2                        or rax, rdx
0025E360  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
0025E365  41 FF 85 70 8F 00 00            inc dword ptr [r13 + 0x8f70]
0025E36C  41 0F B6 85 D0 00 00 00         movzx eax, byte ptr [r13 + 0xd0]
0025E374  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0025E37D  66 89 44 24 40                  mov word ptr [rsp + 0x40], ax
0025E382  41 0F B6 85 D1 00 00 00         movzx eax, byte ptr [r13 + 0xd1]
0025E38A  88 44 24 30                     mov byte ptr [rsp + 0x30], al
0025E38E  48 39 B1 20 06 00 00            cmp qword ptr [rcx + 0x620], rsi
0025E395  0F 84 0D 02 00 00               je 0x14025e5a8
0025E39B  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0025E3A4  45 8B FE                        mov r15d, r14d
0025E3A7  41 81 E7 00 00 FF FF            and r15d, 0xffff0000
0025E3AE  48 89 4D 90                     mov qword ptr [rbp - 0x70], rcx
0025E3B2  8B 81 A0 05 00 00               mov eax, dword ptr [rcx + 0x5a0]
0025E3B8  A8 01                           test al, 1
0025E3BA  0F 85 E8 01 00 00               jne 0x14025e5a8
0025E3C0  4C 8B B1 20 06 00 00            mov r14, qword ptr [rcx + 0x620]
0025E3C7  44 8B 05 9A A0 C0 00            mov r8d, dword ptr [rip + 0xc0a09a]
0025E3CE  44 89 44 24 68                  mov dword ptr [rsp + 0x68], r8d
0025E3D3  4D 85 F6                        test r14, r14
0025E3D6  75 55                           jne 0x14025e42d
0025E3D8  BA 00 02 00 00                  mov edx, 0x200
0025E3DD  41 8D 4E 48                     lea ecx, [r14 + 0x48]
0025E3E1  41 B8 52 65 54 72               mov r8d, 0x72546552
0025E3E7  E8 04 3D 92 00                  call 0x140b820f0
0025E3EC  48 8B D8                        mov rbx, rax
0025E3EF  48 85 C0                        test rax, rax
0025E3F2  0F 84 B0 01 00 00               je 0x14025e5a8
0025E3F8  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
0025E3FC  48 89 78 10                     mov qword ptr [rax + 0x10], rdi
0025E400  44 89 78 1C                     mov dword ptr [rax + 0x1c], r15d
0025E404  89 70 20                        mov dword ptr [rax + 0x20], esi
0025E407  8B 44 24 68                     mov eax, dword ptr [rsp + 0x68]
0025E40B  89 43 28                        mov dword ptr [rbx + 0x28], eax
0025E40E  33 C0                           xor eax, eax
0025E410  F0 48 0F B1 99 20 06 00 00      lock cmpxchg qword ptr [rcx + 0x620], rbx
0025E419  4C 8B F0                        mov r14, rax
0025E41C  74 7D                           je 0x14025e49b
0025E41E  33 D2                           xor edx, edx
0025E420  48 8B CB                        mov rcx, rbx
0025E423  E8 48 44 92 00                  call 0x140b82870
0025E428  44 8B 44 24 68                  mov r8d, dword ptr [rsp + 0x68]
0025E42D  48 8B C6                        mov rax, rsi
0025E430  8B D6                           mov edx, esi
0025E432  83 FA 08                        cmp edx, 8
0025E435  73 33                           jae 0x14025e46a
0025E437  41 8B 4E 1C                     mov ecx, dword ptr [r14 + 0x1c]
0025E43B  41 3B CF                        cmp ecx, r15d
0025E43E  75 0C                           jne 0x14025e44c
0025E440  49 39 7E 10                     cmp qword ptr [r14 + 0x10], rdi
0025E444  75 06                           jne 0x14025e44c
0025E446  45 39 46 28                     cmp dword ptr [r14 + 0x28], r8d
0025E44A  74 43                           je 0x14025e48f
0025E44C  48 85 C0                        test rax, rax
0025E44F  0F 85 B8 01 00 00               jne 0x14025e60d
0025E455  85 C9                           test ecx, ecx
0025E457  0F 84 AD 01 00 00               je 0x14025e60a
0025E45D  45 39 46 28                     cmp dword ptr [r14 + 0x28], r8d
0025E461  0F 8D A6 01 00 00               jge 0x14025e60d
0025E467  49 8B C6                        mov rax, r14
0025E46A  4C 8B F0                        mov r14, rax
0025E46D  48 85 C0                        test rax, rax
0025E470  74 1D                           je 0x14025e48f
0025E472  48 89 78 10                     mov qword ptr [rax + 0x10], rdi
0025E476  44 89 78 1C                     mov dword ptr [rax + 0x1c], r15d
0025E47A  48 89 70 20                     mov qword ptr [rax + 0x20], rsi
0025E47E  48 89 30                        mov qword ptr [rax], rsi
0025E481  48 89 70 08                     mov qword ptr [rax + 8], rsi
0025E485  89 70 18                        mov dword ptr [rax + 0x18], esi
0025E488  44 89 40 28                     mov dword ptr [rax + 0x28], r8d
0025E48C  89 70 2C                        mov dword ptr [rax + 0x2c], esi
0025E48F  49 8B DE                        mov rbx, r14
0025E492  4D 85 F6                        test r14, r14
0025E495  0F 84 0D 01 00 00               je 0x14025e5a8
0025E49B  39 73 20                        cmp dword ptr [rbx + 0x20], esi
0025E49E  0F 84 BC 00 00 00               je 0x14025e560
0025E4A4  41 FF 85 74 8F 00 00            inc dword ptr [r13 + 0x8f74]
0025E4AB  8B 44 24 60                     mov eax, dword ptr [rsp + 0x60]
0025E4AF  FF C0                           inc eax
0025E4B1  39 43 24                        cmp dword ptr [rbx + 0x24], eax
0025E4B4  0F 82 DA 0A 00 00               jb 0x14025ef94
0025E4BA  44 8B 44 24 38                  mov r8d, dword ptr [rsp + 0x38]
0025E4BF  41 81 F8 42 00 01 00            cmp r8d, 0x10042
0025E4C6  0F 85 F2 03 00 00               jne 0x14025e8be
0025E4CC  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
0025E4D0  49 3B C4                        cmp rax, r12
0025E4D3  0F 87 C3 0A 00 00               ja 0x14025ef9c
0025E4D9  4C 8B CE                        mov r9, rsi
0025E4DC  48 83 3B 01                     cmp qword ptr [rbx], 1
0025E4E0  0F 87 F5 05 00 00               ja 0x14025eadb
0025E4E6  8B 4B 2C                        mov ecx, dword ptr [rbx + 0x2c]
0025E4E9  44 8B 54 24 44                  mov r10d, dword ptr [rsp + 0x44]
0025E4EE  44 3B D1                        cmp r10d, ecx
0025E4F1  0F 87 CF 0A 00 00               ja 0x14025efc6
0025E4F7  41 8B 85 F0 8E 00 00            mov eax, dword ptr [r13 + 0x8ef0]
0025E4FE  33 D2                           xor edx, edx
0025E500  41 03 85 EC 8E 00 00            add eax, dword ptr [r13 + 0x8eec]
0025E507  F7 35 03 06 BB 00               div dword ptr [rip + 0xbb0603]
0025E50D  85 D2                           test edx, edx
0025E50F  0F 84 E9 05 00 00               je 0x14025eafe
0025E515  EB 49                           jmp 0x14025e560
0025E517  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
0025E51B  49 3B C4                        cmp rax, r12
0025E51E  0F 87 2C 0A 00 00               ja 0x14025ef50
0025E524  4C 8B CE                        mov r9, rsi
0025E527  48 83 3B 01                     cmp qword ptr [rbx], 1
0025E52B  0F 87 6F 04 00 00               ja 0x14025e9a0
0025E531  8B 4B 2C                        mov ecx, dword ptr [rbx + 0x2c]
0025E534  44 8B 54 24 44                  mov r10d, dword ptr [rsp + 0x44]
0025E539  44 3B D1                        cmp r10d, ecx
0025E53C  0F 87 38 0A 00 00               ja 0x14025ef7a
0025E542  41 8B 87 F0 8E 00 00            mov eax, dword ptr [r15 + 0x8ef0]
0025E549  33 D2                           xor edx, edx
0025E54B  41 03 87 EC 8E 00 00            add eax, dword ptr [r15 + 0x8eec]
0025E552  F7 35 B8 05 BB 00               div dword ptr [rip + 0xbb05b8]
0025E558  85 D2                           test edx, edx
0025E55A  0F 84 63 04 00 00               je 0x14025e9c3
0025E560  89 73 1C                        mov dword ptr [rbx + 0x1c], esi
0025E563  EB 43                           jmp 0x14025e5a8
0025E565  0F B6 43 25                     movzx eax, byte ptr [rbx + 0x25]
0025E569  41 84 C4                        test r12b, al
0025E56C  0F 85 84 00 00 00               jne 0x14025e5f6
0025E572  24 FE                           and al, 0xfe
0025E574  41 B6 01                        mov r14b, 1
0025E577  88 43 25                        mov byte ptr [rbx + 0x25], al
0025E57A  83 3D 9F 87 D6 00 00            cmp dword ptr [rip + 0xd6879f], 0
0025E581  74 0D                           je 0x14025e590
0025E583  44 0F 20 C1                     mov rcx, cr8
0025E587  40 0F B6 D6                     movzx edx, sil
0025E58B  E8 08 71 29 00                  call 0x1404f5698
0025E590  40 0F B6 C6                     movzx eax, sil
0025E594  44 0F 22 C0                     mov cr8, rax
0025E598  48 8B D3                        mov rdx, rbx
0025E59B  48 8B CF                        mov rcx, rdi
0025E59E  E8 2D 2E 00 00                  call 0x1402613d0
0025E5A3  45 84 F6                        test r14b, r14b
0025E5A6  75 56                           jne 0x14025e5fe
0025E5A8  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0025E5B1  E8 3A 0A 00 00                  call 0x14025eff0
0025E5B6  4C 8B B4 24 28 01 00 00         mov r14, qword ptr [rsp + 0x128]
0025E5BE  4C 8B AC 24 68 01 00 00         mov r13, qword ptr [rsp + 0x168]
0025E5C6  4C 8B A4 24 60 01 00 00         mov r12, qword ptr [rsp + 0x160]
0025E5CE  48 8B 9C 24 58 01 00 00         mov rbx, qword ptr [rsp + 0x158]
0025E5D6  4C 8B BC 24 20 01 00 00         mov r15, qword ptr [rsp + 0x120]
0025E5DE  48 8B 4D 18                     mov rcx, qword ptr [rbp + 0x18]
0025E5E2  48 33 CC                        xor rcx, rsp
0025E5E5  E8 56 E0 44 00                  call 0x1406ac640
0025E5EA  48 81 C4 30 01 00 00            add rsp, 0x130
0025E5F1  5F                              pop rdi
0025E5F2  5E                              pop rsi
0025E5F3  5D                              pop rbp
0025E5F4  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0025D903(unsigned __int8 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, unsigned int a7, __int64 a8, unsigned __int8 a9, __int64 a10, unsigned __int8 a11, unsigned int a12, unsigned int a13, __int64 a14, __int64 a15, __int64 a16, __int64 a17, __int64 a18, __int64 a19, __int64 a20, __int64 a21, __int64 a22, __int64 a23, __int64 a24, __int64 a25, __int64 a26, __int64 a27, __int64 a28, __int64 a29, __int64 a30, __int64 a31, __int64 a32, __int64 a33, __int64 a34, __int64 a35, __int64 a36, __int64 a37, __int64 a38, __int64 a39, __int64 a40, __int64 a41, __int64 a42, __int64 a43, __int64 a44, __int64 a45)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_p0;
    unsigned __int64 v_stack_p20;
    unsigned __int8 v_stack_p30;
    unsigned int v_stack_p38;
    unsigned __int16 v_stack_p40;
    unsigned int v_stack_p44;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned int v_stack_p60;
    unsigned int v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;

    *(unsigned __int64 *)(v_r11 + 16) = v_rbx;
    *(unsigned __int64 *)(v_r11 + 24) = v_r12;
    *(unsigned __int64 *)(v_r11 + 32) = v_r13;
    *(unsigned __int64 *)(v_r11 - 32) = v_r14;
    *(unsigned __int64 *)(v_r11 - 40) = v_r15;
    result = 0;
    a9 = v_xmm0;
    v_rsi = 0;
    v_stack_p58 = 0;
    v_stack_p48 = 0;
    v_stack_p50 = v_rdi + 96;
    if ((*(unsigned int *)(v_rip + 14062531)) != 0) goto loc_0025DFD9;
loc_0025D963:
    v_stack_p58 = (unsigned __int8)(v_cr8);
    if (((*(unsigned __int8 *)(v_rip + 14061980)) & (33)) != 0) goto loc_0025D9F8;
loc_0025D975:
    if (a9 != 0) goto loc_0025E14E;
loc_0025D986:
    a1 = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(v_rdi + 26))) & (1));
    if (condition_is_not_equal) goto loc_0025E121;
    if ((*(unsigned int *)(v_rip + 13226602)) != 0) goto loc_0025E121;
loc_0025D9AC:
    if (!sign_flag) goto loc_0025DC74;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 14061898))) & (0x20000ULL));
    *(unsigned __int64 *)(v_rbp - 104) = 0;
    v_stack_p60 = (unsigned int)(result);
    if (a1 != 0) goto loc_0025D9D4;
    if ((*(unsigned int *)(v_rip + 13226558)) == 0) goto loc_0025DA18;
loc_0025D9D4:
    if ((*(unsigned __int64 *)(v_rdi + 48)) == (*(unsigned __int64 *)(gs_base + (0 + 392)))) goto loc_0025DA18;
    v_stack_p20 = 1;
    result = KeBugCheckEx(227, v_rdi, *(unsigned __int64 *)(gs_base + (0 + 392)), *(unsigned __int64 *)(v_rdi + 16));
loc_0025D9F8:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13304922))) != 0) goto loc_0025D975;
    result = KiAcquireQueuedSpinLockInstrumented(a9, v_rdi + 96, *(unsigned __int64 *)(gs_base + (0 + 392)), *(unsigned __int64 *)(v_rdi + 16));
    goto loc_0025D986;
loc_0025DA18:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rdi + 56))) & (7));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 56))))) >> (3));
    v_r13 = (unsigned int)((result * 8 - 8) | (a1));
    *(unsigned int *)(v_rdi + 56) = (unsigned int)(v_r13);
    v_r13 = (unsigned int)((v_r13) >> (3));
    if ((unsigned int)(v_r13) != 0) goto loc_0025DD0A;
    if (((2) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rdi + 56))))) == 0) goto loc_0025DFCB;
    v_rbx = (*(unsigned __int64 *)(v_rdi + 48)) & (-4);
loc_0025DA59:
    if (v_rbx == 0) goto loc_0025DAF7;
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rdi + 56))))) == 0) goto loc_0025DAA7;
    v_r14 = 0;
    v_r15 = 0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rdi + 56))) & (0xFFFFFFFEULL));
    *(unsigned int *)(v_rdi + 56) = (unsigned int)(result);
loc_0025DAA7:
    if ((((unsigned __int8)(result)) & (4)) != 0) {
        result = *(unsigned int *)(v_rdi + 56);
        result = (unsigned int)((result) & (0xFFFFFFFBULL));
        *(unsigned int *)(v_rdi + 56) = (unsigned int)(result);
    }
    if (((2) & ((unsigned __int8)(result))) == 0) goto loc_0025DAF7;
    if ((*(unsigned int *)(v_rip + 14054730)) != 0) {
        a4 = 0x746C6644ULL;
        a1 = v_rbx - 48;
        a3 = 1;
        a2 = 0;
        result = ObpPushStackInfo(a1, a2, a3, a4);
    }
    result = (-1) - (1);
loc_0025DAF7:
    *(unsigned __int64 *)(v_rdi + 48) = 0;
    v_stack_p44 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 68)));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 72))) == 0) goto loc_0025DCED;
    *(unsigned __int64 *)(v_rdi + 32) = 0;
    *(unsigned __int64 *)(v_rbp - 104) = *(unsigned __int64 *)(v_rdi + 32);
    *(unsigned int *)(v_rdi + 72) = 0;
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rdi + 64))) - 1);
    a2 = (unsigned int)((a2) + ((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 72)))));
loc_0025DB2F:
    *(unsigned int *)(v_rdi + 64) = (unsigned int)(a2);
    if ((*(unsigned int *)(v_rdi + 76)) != 0) goto loc_0025DB45;
    if ((*(unsigned int *)(v_rdi + 72)) == 0) {
        a1 = 249;
    }
    result = *(unsigned __int64 *)(v_rdi + 32);
    if (0 != 0) {
        result = *(unsigned int *)(v_rdi + 56);
        result = (unsigned int)((result) & (7));
        *(unsigned __int64 *)(v_rdi + 48) = 0;
        result = (unsigned int)((result) | (8));
        *(unsigned int *)(v_rdi + 56) = (unsigned int)(result);
    }
    if (((*(unsigned __int8 *)(v_rip + 14061472)) & (1)) != 0) goto loc_0025DC07;
loc_0025DB6C:
    if (a9 != 0) goto loc_0025DBA2;
    if (a9 == a9) goto loc_0025DC23;
    result = KxWaitForLockChainValid(a9, a2, a3, a4);
loc_0025DBA2:
    v_stack_p48 = 0;
    result = (unsigned __int8)((a10) ^ ((unsigned __int8)(a10)));
    if ((((unsigned __int8)(result)) & (4)) == 0) goto loc_0025DC23;
    a3 = (result + 8) >> (5);
    a3 = (unsigned int)((a3) & (127));
    result = KeDisableInterrupts(a10, a2, a3, a4);
    result = KiHaltOnAddressWakeEntireList(a10, 0, a3, a4);
    if ((unsigned __int8)((unsigned __int8)(result)) == 0) goto loc_0025DC23;
    goto loc_0025DC23;
loc_0025DC07:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13304395))) != 0) goto loc_0025DB6C;
    result = KiReleaseQueuedSpinLockInstrumented(a9, *(unsigned __int64 *)(v_rbp + 72), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), a4);
loc_0025DC23:
    if ((*(unsigned int *)(v_rip + 14061815)) != 0) {
        a1 = 2;
        a2 = a11;
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), a4);
    }
    v_rbx = 1;
    if (0 != 0) { v_rbx = 3; }
    if ((*(unsigned __int64 *)(v_rbp - 104)) != 0) goto loc_0025E096;
    v_stack_p68 = (unsigned int)((unsigned int)(0x10022ULL));
    goto loc_0025DD62;
loc_0025DC74:
    v_r13 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 14061193))) & (0x20000ULL));
    *(unsigned __int64 *)(v_rbp - 96) = 0;
    if ((*(unsigned __int64 *)(v_rdi + 48)) == ((unsigned int)(0x10022ULL))) goto loc_0025E179;
    a1 = (*(unsigned __int64 *)(v_rdi + 48) != 0) ? 1 : 0;
    if ((unsigned int)(*(unsigned __int8 *)((unsigned int)(0x10022ULL) + 1120)) != 0) goto loc_0025DFEB;
loc_0025DCBD:
    a3 = ((unsigned int)(*(unsigned int *)(v_rdi + 72))) + ((unsigned int)(*(unsigned int *)(v_rdi + 64)));
    if (*(unsigned __int64 *)(v_rdi + 16) != 0) goto loc_0025E019;
loc_0025DCD4:
    v_stack_p20 = 2;
    result = KeBugCheckEx(227, v_rdi, (unsigned int)(0x10022ULL), *(unsigned __int64 *)(v_rdi + 16));
loc_0025DCED:
    if ((*(unsigned int *)(v_rdi + 76)) != 0) goto loc_0025E058;
    *(unsigned __int16 *)(v_rdi + 24) = 0;
    goto loc_0025DB2F;
loc_0025DD0A:
    v_stack_p68 = (unsigned int)((unsigned int)(0x10032ULL));
    v_stack_p44 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 68)));
    if (((*(unsigned __int8 *)(v_rip + 14061045)) & (3)) == 0) goto loc_0025DF25;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13304105))) != 0) goto loc_0025DF25;
    result = KiReleaseQueuedSpinLockInstrumented(a9, *(unsigned __int64 *)(v_rbp + 72), (unsigned int)(0x10022ULL), *(unsigned __int64 *)(v_rdi + 16));
loc_0025DD45:
    if ((*(unsigned int *)(v_rip + 14061525)) != 0) {
        a1 = a11;
        a2 = a11;
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, (unsigned int)(0x10022ULL), *(unsigned __int64 *)(v_rdi + 16));
    }
loc_0025DD62:
    if (a12 == 0) goto loc_0025E5A8;
    *(unsigned __int64 *)(v_rbp - 88) = v_xmm0;
    *(unsigned __int64 *)(v_rbp - 72) = v_xmm0;
    *(unsigned __int64 *)(v_rbp - 56) = v_xmm0;
    a2 = (a2) << (32);
    result = (result) | (a2);
    v_stack_p78 = result;
    v_stack_p40 = (unsigned __int16)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 208));
    v_stack_p30 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 209));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1568)) == 0) goto loc_0025E5A8;
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(0x10032ULL)))) & (0xFFFF0000ULL));
    *(unsigned __int64 *)(v_rbp - 112) = *(unsigned __int64 *)(gs_base + (0 + 392));
    v_stack_p38 = (unsigned int)(a2);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1440)))) & (1)) != 0) goto loc_0025E5A8;
    v_stack_p60 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12625506)));
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1568) != 0) goto loc_0025DE6C;
    result = ExAllocatePool2(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1568) + 72, 512, (unsigned int)(0x72546552ULL), *(unsigned __int64 *)(v_rdi + 16));
    if (result == 0) goto loc_0025E5A8;
    *(unsigned __int64 *)(result + 16) = v_rdi;
    *(unsigned int *)(result + 28) = (unsigned int)((unsigned int)(a7));
    *(unsigned int *)(result + 40) = (unsigned int)((unsigned int)(a12));
    result = 0;
    *(unsigned int *)(result + 32) = 0;
    if (condition_is_equal) goto loc_0025DED2;
    a2 = 0;
    result = ExFreePoolWithTag(0, a2, (unsigned int)(0x72546552ULL), *(unsigned __int64 *)(v_rdi + 16));
loc_0025DE6C:
loc_0025DE71:
    if (0 >= 8) goto loc_0025DEA2;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(0 + 28)))) != ((unsigned int)((unsigned int)(a7)))) goto loc_0025DE8B;
    if ((*(unsigned __int64 *)(0 + 16)) != v_rdi) goto loc_0025DE8B;
    if ((*(unsigned int *)(0 + 40)) == ((unsigned int)((unsigned int)(a12)))) goto loc_0025DEC6;
loc_0025DE8B:
    if (0 != 0) goto loc_0025DF1A;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(0 + 28))) == 0) goto loc_0025DF17;
    if ((*(unsigned int *)(0 + 40)) >= ((unsigned int)((unsigned int)(a12)))) goto loc_0025DF1A;
loc_0025DEA2:
    if (0 != 0) {
        *(unsigned __int64 *)(0 + 16) = v_rdi;
        *(unsigned int *)(0 + 28) = (unsigned int)((unsigned int)(a7));
        *(unsigned __int64 *)(0 + 32) = 0;
        *(unsigned __int64 *)(0) = 0;
        *(unsigned __int64 *)(0 + 8) = 0;
        *(unsigned int *)(0 + 24) = 0;
        *(unsigned int *)(0 + 40) = (unsigned int)((unsigned int)(a12));
        *(unsigned int *)(0 + 44) = 0;
    }
    if (0 == 0) goto loc_0025E5A8;
loc_0025DED2:
    if ((*(unsigned int *)(0 + 32)) == 0) goto loc_0025E560;
    v_r13 = (unsigned int)((v_r13) + 1);
    if (((unsigned int)((unsigned int)(a13))) == 0x10022ULL) goto loc_0025E517;
    if (((unsigned int)((unsigned int)(a13))) != 0x10032ULL) goto loc_0025E5A8;
    *(unsigned int *)(0 + 32) = 2;
    goto loc_0025E5A8;
loc_0025DF17:
loc_0025DF1A:
    v_r14 = (0) + (64);
    a1 = (unsigned int)((0) + 1);
    goto loc_0025DE71;
loc_0025DF25:
    if (a9 != 0) goto loc_0025DF5B;
    if (a9 == a9) goto loc_0025DD45;
    result = KxWaitForLockChainValid(a9, (unsigned int)(a7), (unsigned int)(a13), (unsigned int)(*(unsigned int *)(0 + 28)));
loc_0025DF5B:
    v_stack_p48 = 0;
    result = (unsigned __int8)((a10) ^ ((unsigned __int8)(a10)));
    if ((((unsigned __int8)(result)) & (4)) == 0) goto loc_0025DD45;
    a3 = (result + 8) >> (5);
    a3 = (unsigned int)((a3) & (127));
    result = KeDisableInterrupts(a10, (unsigned int)(a7), a3, (unsigned int)(*(unsigned int *)(0 + 28)));
    result = KiHaltOnAddressWakeEntireList(a10, 0, a3, (unsigned int)(*(unsigned int *)(0 + 28)));
    if ((unsigned __int8)((unsigned __int8)(result)) == 0) goto loc_0025DD45;
    goto loc_0025DD45;
loc_0025DFCB:
    if ((((unsigned __int8)((unsigned __int8)(result))) & (3)) != 0) goto loc_0025DAF7;
    goto loc_0025DA59;
loc_0025DFD9:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(*(unsigned __int64 *)(gs_base + (0 + 32))), 2, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), (unsigned int)(*(unsigned int *)(0 + 28)));
    goto loc_0025D963;
loc_0025DFEB:
    if (*(unsigned __int64 *)(v_rdi + 16) == 0) goto loc_0025DCBD;
    if (((unsigned int)(result)) >= (*(unsigned int *)(*(unsigned __int64 *)(v_rdi + 16) + 8))) goto loc_0025DCBD;
    a2 = ((unsigned int)((unsigned int)(result))) << (4);
    a2 = (a2) + (*(unsigned __int64 *)(v_rdi + 16));
    if ((*(unsigned __int64 *)(a2)) != v_r14) goto loc_0025DCBD;
    goto loc_0025E179;
loc_0025E019:
    a4 = ((unsigned int)(*(unsigned int *)(a2 + 8))) << (4);
    a4 = (a4) + (a2);
    a2 = (a2) + (16);
    if (((unsigned __int8)(*(unsigned __int64 *)(gs_base + (0 + 32)))) >= (*(unsigned __int64 *)(v_rdi + 16))) goto loc_0025E04F;
loc_0025E02D:
    if ((*(unsigned __int64 *)(a2)) == v_r14) goto loc_0025E15D;
    if (*(unsigned __int64 *)(a2) == 0) goto loc_0025E046;
    a1 = ((unsigned __int8)(*(unsigned __int64 *)(gs_base + (0 + 32)))) + 1;
    if (a1 == (*(unsigned __int64 *)(v_rdi + 16))) goto loc_0025E04F;
loc_0025E046:
    a2 = (a2) + (16);
    if (a2 != a4) goto loc_0025E02D;
loc_0025E04F:
    goto loc_0025DCD4;
loc_0025E058:
    *(unsigned __int64 *)(v_rdi + 40) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 40));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 40)) + 8)) != (*(unsigned __int64 *)(v_rdi + 40))) goto loc_0025E08B;
loc_0025E08B:
    goto loc_0025E11C;
loc_0025E096:
    *(unsigned __int64 *)(v_rbp - 112) = a11;
    *(unsigned __int64 *)(v_rbp - 120) = *(unsigned __int64 *)(gs_base + (0 + 32));
    *(unsigned __int64 *)(v_rbp - 128) = *(unsigned __int64 *)(v_rbp - 104);
    result = (*(unsigned __int64 *)(v_rbp - 104)) + (24);
    v_stack_p78 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 104));
    v_stack_p70 = result;
    result = KiAcquireKobjectLockSafe(result, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 40)), *(unsigned __int64 *)(v_rdi + 16), a4);
    *(unsigned int *)(*(unsigned __int64 *)(v_rbp - 128) + 28) = (unsigned int)(v_r14);
    v_stack_p38 = *(unsigned __int64 *)(v_rbp - 128) + 24 + 8;
    v_stack_p68 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 128) + 24 + 8));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 128) + 24 + 8)) + 8)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 128) + 24 + 8))) goto loc_0025E11C;
loc_0025E11C:
loc_0025E121:
    result = (unsigned __int8)(((unsigned __int8)(v_r14)) & (3));
    if (((unsigned __int8)(result)) == 3) goto loc_0025D9AC;
    if (v_r14 == (*(unsigned __int64 *)(v_rdi + 16))) goto loc_0025D9AC;
    v_stack_p20 = 0;
    result = KeBugCheckEx(366, v_rdi, *(unsigned __int64 *)(v_rdi + 16), v_r14);
loc_0025E14E:
    result = KxWaitForLockOwnerShip(a9, v_rdi, *(unsigned __int64 *)(v_rdi + 16), v_r14);
    goto loc_0025D986;
loc_0025E15D:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) - (*(unsigned int *)(v_rdi + 16)));
    result = (result) >> (4);
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1120) = (unsigned __int8)(result);
loc_0025E179:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 8))))) >> (3));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rdi + 8))) & (7));
    v_r14 = (unsigned int)((result * 8 - 8) | (a1));
    *(unsigned int *)(v_rdi + 8) = (unsigned int)(v_r14);
    v_r14 = (unsigned int)((v_r14) >> (3));
    v_stack_p60 = (unsigned int)(v_r14);
    if ((unsigned int)(v_r14) != 0) goto loc_0025E2D6;
    result = ExpFreeOwnerEntry(v_rdi, v_rdi, *(unsigned __int64 *)(v_rdi + 16), v_r14);
    v_stack_p44 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 68)));
    if ((*(unsigned int *)(v_rdi + 64)) > 1) goto loc_0025E1D1;
loc_0025E1D1:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rdi + 64))) - 1);
    a1 = (unsigned int)((0) + ((unsigned int)(result)));
    *(unsigned int *)(v_rdi + 64) = a1;
    if (!(condition_is_not_equal)) {
        *(unsigned __int16 *)(v_rdi + 24) = 0;
    }
    if ((*(unsigned int *)(v_rdi + 76)) != 0) goto loc_0025E1F6;
    if ((*(unsigned int *)(v_rdi + 72)) == 0) {
        a1 = 249;
    }
    v_stack_p68 = (unsigned int)(*(unsigned __int8 *)(v_rdi + 27));
    result = *(unsigned __int8 *)(v_rdi + 27);
    if (0 != 0) {
        result = *(unsigned int *)(v_rdi + 56);
        result = (unsigned int)((result) & (7));
        *(unsigned __int64 *)(v_rdi + 48) = 0;
        result = (unsigned int)((result) | (8));
        *(unsigned int *)(v_rdi + 56) = (unsigned int)(result);
    }
    if (((*(unsigned __int8 *)(v_rip + 14059756)) & (1)) != 0) goto loc_0025E26F;
loc_0025E21C:
    if (a9 != 0) goto loc_0025E24E;
    if (a9 == a9) goto loc_0025E287;
    result = KxWaitForLockChainValid(a9, v_rdi, *(unsigned __int64 *)(v_rdi + 16), v_r14);
loc_0025E24E:
    v_stack_p48 = 0;
    result = (unsigned __int8)((a10) ^ ((unsigned __int8)(a10)));
    if ((((unsigned __int8)(result)) & (4)) == 0) goto loc_0025E287;
    result = KeWakeAddressAll(result + 8, a10, *(unsigned __int64 *)(v_rdi + 16), v_r14);
    goto loc_0025E287;
loc_0025E26F:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13302755))) != 0) goto loc_0025E21C;
    result = KiReleaseQueuedSpinLockInstrumented(a9, *(unsigned __int64 *)(v_rbp + 72), *(unsigned __int64 *)(v_rdi + 16), v_r14);
loc_0025E287:
    if ((*(unsigned int *)(v_rip + 14060179)) != 0) {
        a1 = 2;
        a2 = a11;
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, *(unsigned __int64 *)(v_rdi + 16), v_r14);
    }
    v_rbx = 1;
    if (0 != 0) { v_rbx = 3; }
    v_stack_p60 = 0;
    v_stack_p38 = (unsigned int)((unsigned int)(0x10042ULL));
    goto loc_0025E32E;
loc_0025E2D6:
    v_stack_p38 = (unsigned int)((unsigned int)(0x10052ULL));
    v_stack_p44 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 68)));
    result = KiReleaseQueuedSpinLockInstrumented(a9, *(unsigned __int64 *)(v_rbp + 72), *(unsigned __int64 *)(v_rdi + 16), v_r14);
    if ((*(unsigned int *)(v_rip + 14060041)) != 0) {
        a1 = a11;
        a2 = a11;
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, *(unsigned __int64 *)(v_rdi + 16), v_r14);
    }
loc_0025E32E:
    if ((unsigned int)(v_r13) == 0) goto loc_0025E5A8;
    *(unsigned __int64 *)(v_rbp - 40) = v_xmm0;
    *(unsigned __int64 *)(v_rbp - 24) = v_xmm0;
    *(unsigned __int64 *)(v_rbp - 8) = v_xmm0;
    a2 = (a2) << (32);
    result = (result) | (a2);
    v_stack_p78 = result;
    v_stack_p40 = (unsigned __int16)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 208));
    v_stack_p30 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 209));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1568)) == 0) goto loc_0025E5A8;
    v_r15 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(0x10052ULL)))) & (0xFFFF0000ULL));
    *(unsigned __int64 *)(v_rbp - 112) = *(unsigned __int64 *)(gs_base + (0 + 392));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1440)))) & (1)) != 0) goto loc_0025E5A8;
    v_stack_p68 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12624026)));
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1568) != 0) goto loc_0025E42D;
    result = ExAllocatePool2(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1568) + 72, 512, (unsigned int)(0x72546552ULL), v_r14);
    if (result == 0) goto loc_0025E5A8;
    *(unsigned __int64 *)(result + 16) = v_rdi;
    *(unsigned int *)(result + 28) = (unsigned int)(v_r15);
    *(unsigned int *)(result + 32) = 0;
    *(unsigned int *)(result + 40) = (unsigned int)((unsigned int)(a13));
    result = 0;
    if (condition_is_equal) goto loc_0025E49B;
    a2 = 0;
    result = ExFreePoolWithTag(0, a2, (unsigned int)(0x72546552ULL), v_r14);
loc_0025E42D:
    if (0 >= 8) goto loc_0025E46A;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(0 + 28)))) != ((unsigned int)(v_r15))) goto loc_0025E44C;
    if ((*(unsigned __int64 *)(0 + 16)) != v_rdi) goto loc_0025E44C;
    if ((*(unsigned int *)(0 + 40)) == ((unsigned int)((unsigned int)(a13)))) goto loc_0025E48F;
loc_0025E44C:
loc_0025E46A:
    if (0 != 0) {
        *(unsigned __int64 *)(0 + 16) = v_rdi;
        *(unsigned int *)(0 + 28) = (unsigned int)(v_r15);
        *(unsigned __int64 *)(0 + 32) = 0;
        *(unsigned __int64 *)(0) = 0;
        *(unsigned __int64 *)(0 + 8) = 0;
        *(unsigned int *)(0 + 24) = 0;
        *(unsigned int *)(0 + 40) = (unsigned int)((unsigned int)(a13));
        *(unsigned int *)(0 + 44) = 0;
    }
    if (0 == 0) goto loc_0025E5A8;
loc_0025E49B:
    if ((*(unsigned int *)(0 + 32)) == 0) goto loc_0025E560;
    result = (unsigned int)(((unsigned int)(a12)) + 1);
    a2 = 0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36592))) + (*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36588)));
    goto loc_0025E560;
loc_0025E517:
    a2 = 0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r15 + 36592))) + (*(unsigned int *)(v_r15 + 36588)));
loc_0025E560:
    *(unsigned int *)(0 + 28) = 0;
    goto loc_0025E5A8;
loc_0025E5A8:
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, (unsigned int)(a7), 0);
    a1 = (*(unsigned __int64 *)(v_rbp + 24)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, (unsigned int)(a7), 0);
    v_rsp = (v_rsp) + (304);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t sub_0025D903(uint8_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint32_t Arg7, uint64_t Arg8, uint8_t Arg9, void *Arg10, uint8_t Arg11, uint32_t Arg12, uint32_t Arg13, uint64_t Arg14, uint64_t Arg15, uint64_t Arg16, uint64_t Arg17, uint64_t Arg18, uint64_t Arg19, uint64_t Arg20, uint64_t Arg21, uint64_t Arg22, uint64_t Arg23, uint64_t Arg24, uint64_t Arg25, uint64_t Arg26, uint64_t Arg27, uint64_t Arg28, uint64_t Arg29, uint64_t Arg30, uint64_t Arg31, uint64_t Arg32, uint64_t Arg33, uint64_t Arg34, uint64_t Arg35, int64_t Arg36, int64_t Arg37, uint64_t Arg38, uint64_t Arg39, uint64_t Arg40, uint64_t Arg41, uint64_t Arg42, int64_t Arg43, int64_t Arg44, int64_t Arg45)
{
    uint8_t *arg10 = (uint8_t *)Arg10;

    int64_t result;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_p0;
    uint64_t v_stack_p20;
    uint8_t v_stack_p30;
    uint32_t v_stack_p38;
    uint16_t v_stack_p40;
    uint32_t v_stack_p44;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint32_t v_stack_p60;
    uint32_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;

    *(uint64_t *)(local_r11 + 0x10) = local_rbx;
    *(uint64_t *)(local_r11 + 0x18) = local_r12;
    *(uint64_t *)(local_r11 + 0x20) = local_r13;
    *(uint64_t *)(local_r11 - 0x20) = local_r14;
    *(uint64_t *)(local_r11 - 0x28) = local_r15;
    result = 0;
    Arg9 = v_xmm0;
    local_rsi = 0;
    v_stack_p58 = 0;
    v_stack_p48 = 0;
    v_stack_p50 = local_rdi + 96;
    if ((*(uint32_t *)(v_rip + 0xD693C3)) != 0) goto loc_0025DFD9;
loc_0025D963:
    v_stack_p58 = (uint8_t)(v_cr8);
    if (((*(uint8_t *)(v_rip + 0xD6919C)) & (33)) != 0) goto loc_0025D9F8;
loc_0025D975:
    if (Arg9 != 0) goto loc_0025E14E;
loc_0025D986:
    Arg1 = (uint16_t)(((uint16_t)(*(uint16_t *)(local_rdi + 0x1A))) & (1));
    if (condition_is_not_equal) goto loc_0025E121;
    if ((*(uint32_t *)(v_rip + 0xC9D26A)) != 0) goto loc_0025E121;
loc_0025D9AC:
    if (!sign_flag) goto loc_0025DC74;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xD6914A))) & (0x20000ULL));
    *(uint64_t *)(local_rbp - 0x68) = 0;
    v_stack_p60 = (uint32_t)(result);
    if (Arg1 != 0) goto loc_0025D9D4;
    if ((*(uint32_t *)(v_rip + 0xC9D23E)) == 0) goto loc_0025DA18;
loc_0025D9D4:
    if ((*(uint64_t *)(local_rdi + 0x30)) == (*(uint64_t *)(gs_base + (0 + 0x188)))) goto loc_0025DA18;
    v_stack_p20 = 1;
    result = KeBugCheckEx(227, local_rdi, *(uint64_t *)(gs_base + (0 + 0x188)), *(uint64_t *)(local_rdi + 0x10));
loc_0025D9F8:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCB045A))) != 0) goto loc_0025D975;
    result = KiAcquireQueuedSpinLockInstrumented(Arg9, local_rdi + 96, *(uint64_t *)(gs_base + (0 + 0x188)), *(uint64_t *)(local_rdi + 0x10));
    goto loc_0025D986;
loc_0025DA18:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rdi + 0x38))) & (7));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x38))))) >> (3));
    local_r13 = (uint32_t)((result * 8 - 8) | (Arg1));
    *(uint32_t *)(local_rdi + 0x38) = (uint32_t)(local_r13);
    local_r13 = (uint32_t)((local_r13) >> (3));
    if ((uint32_t)(local_r13) != 0) goto loc_0025DD0A;
    if (((2) & ((uint8_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x38))))) == 0) goto loc_0025DFCB;
    local_rbx = (*(uint64_t *)(local_rdi + 0x30)) & (-4);
loc_0025DA59:
    if (local_rbx == 0) goto loc_0025DAF7;
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x38))))) == 0) goto loc_0025DAA7;
    local_r14 = 0;
    local_r15 = 0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rdi + 0x38))) & (0xFFFFFFFEULL));
    *(uint32_t *)(local_rdi + 0x38) = (uint32_t)(result);
loc_0025DAA7:
    if ((((uint8_t)(result)) & (4)) != 0) {
        result = *(uint32_t *)(local_rdi + 0x38);
        result = (uint32_t)((result) & (0xFFFFFFFBULL));
        *(uint32_t *)(local_rdi + 0x38) = (uint32_t)(result);
    }
    if (((2) & ((uint8_t)(result))) == 0) goto loc_0025DAF7;
    if ((*(uint32_t *)(v_rip + 0xD6754A)) != 0) {
        Arg4 = 0x746C6644ULL;
        Arg1 = local_rbx - 48;
        Arg3 = 1;
        Arg2 = 0;
        result = ObpPushStackInfo(Arg1, Arg2, Arg3, Arg4);
    }
    result = (-1) - (1);
loc_0025DAF7:
    *(uint64_t *)(local_rdi + 0x30) = 0;
    v_stack_p44 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x44)));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x48))) == 0) goto loc_0025DCED;
    *(uint64_t *)(local_rdi + 0x20) = 0;
    *(uint64_t *)(local_rbp - 0x68) = *(uint64_t *)(local_rdi + 0x20);
    *(uint32_t *)(local_rdi + 0x48) = 0;
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rdi + 0x40))) - 1);
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x48)))));
loc_0025DB2F:
    *(uint32_t *)(local_rdi + 0x40) = (uint32_t)(Arg2);
    if ((*(uint32_t *)(local_rdi + 0x4C)) != 0) goto loc_0025DB45;
    if ((*(uint32_t *)(local_rdi + 0x48)) == 0) {
        Arg1 = 249;
    }
    result = *(uint64_t *)(local_rdi + 0x20);
    if (0 != 0) {
        result = *(uint32_t *)(local_rdi + 0x38);
        result = (uint32_t)((result) & (7));
        *(uint64_t *)(local_rdi + 0x30) = 0;
        result = (uint32_t)((result) | (8));
        *(uint32_t *)(local_rdi + 0x38) = (uint32_t)(result);
    }
    if (((*(uint8_t *)(v_rip + 0xD68FA0)) & (1)) != 0) goto loc_0025DC07;
loc_0025DB6C:
    if (Arg9 != 0) goto loc_0025DBA2;
    if (Arg9 == Arg9) goto loc_0025DC23;
    result = KxWaitForLockChainValid(Arg9, Arg2, Arg3, Arg4);
loc_0025DBA2:
    v_stack_p48 = 0;
    result = (uint8_t)((Arg10) ^ ((uint8_t)(Arg10)));
    if ((((uint8_t)(result)) & (4)) == 0) goto loc_0025DC23;
    Arg3 = (result + 8) >> (5);
    Arg3 = (uint32_t)((Arg3) & (127));
    result = KeDisableInterrupts(Arg10, Arg2, Arg3, Arg4);
    result = KiHaltOnAddressWakeEntireList(Arg10, 0, Arg3, Arg4);
    if ((uint8_t)((uint8_t)(result)) == 0) goto loc_0025DC23;
    goto loc_0025DC23;
loc_0025DC07:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCB024B))) != 0) goto loc_0025DB6C;
    result = KiReleaseQueuedSpinLockInstrumented(Arg9, *(uint64_t *)(local_rbp + 0x48), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), Arg4);
loc_0025DC23:
    if ((*(uint32_t *)(v_rip + 0xD690F7)) != 0) {
        Arg1 = 2;
        Arg2 = Arg11;
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), Arg4);
    }
    local_rbx = 1;
    if (0 != 0) { local_rbx = 3; }
    if ((*(uint64_t *)(local_rbp - 0x68)) != 0) goto loc_0025E096;
    v_stack_p68 = (uint32_t)((uint32_t)(0x10022ULL));
    goto loc_0025DD62;
loc_0025DC74:
    local_r13 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xD68E89))) & (0x20000ULL));
    *(uint64_t *)(local_rbp - 0x60) = 0;
    if ((*(uint64_t *)(local_rdi + 0x30)) == ((uint32_t)(0x10022ULL))) goto loc_0025E179;
    Arg1 = (*(uint64_t *)(local_rdi + 0x30) != 0) ? 1 : 0;
    if ((uint32_t)(*(uint8_t *)((uint32_t)(0x10022ULL) + 0x460)) != 0) goto loc_0025DFEB;
loc_0025DCBD:
    Arg3 = ((uint32_t)(*(uint32_t *)(local_rdi + 0x48))) + ((uint32_t)(*(uint32_t *)(local_rdi + 0x40)));
    if (*(uint64_t *)(local_rdi + 0x10) != 0) goto loc_0025E019;
loc_0025DCD4:
    v_stack_p20 = 2;
    result = KeBugCheckEx(227, local_rdi, (uint32_t)(0x10022ULL), *(uint64_t *)(local_rdi + 0x10));
loc_0025DCED:
    if ((*(uint32_t *)(local_rdi + 0x4C)) != 0) goto loc_0025E058;
    *(uint16_t *)(local_rdi + 0x18) = 0;
    goto loc_0025DB2F;
loc_0025DD0A:
    v_stack_p68 = (uint32_t)((uint32_t)(0x10032ULL));
    v_stack_p44 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x44)));
    if (((*(uint8_t *)(v_rip + 0xD68DF5)) & (3)) == 0) goto loc_0025DF25;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCB0129))) != 0) goto loc_0025DF25;
    result = KiReleaseQueuedSpinLockInstrumented(Arg9, *(uint64_t *)(local_rbp + 0x48), (uint32_t)(0x10022ULL), *(uint64_t *)(local_rdi + 0x10));
loc_0025DD45:
    if ((*(uint32_t *)(v_rip + 0xD68FD5)) != 0) {
        Arg1 = Arg11;
        Arg2 = Arg11;
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, (uint32_t)(0x10022ULL), *(uint64_t *)(local_rdi + 0x10));
    }
loc_0025DD62:
    if (Arg12 == 0) goto loc_0025E5A8;
    *(uint64_t *)(local_rbp - 0x58) = v_xmm0;
    *(uint64_t *)(local_rbp - 0x48) = v_xmm0;
    *(uint64_t *)(local_rbp - 0x38) = v_xmm0;
    Arg2 = (Arg2) << (32);
    result = (result) | (Arg2);
    v_stack_p78 = result;
    v_stack_p40 = (uint16_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xD0));
    v_stack_p30 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xD1));
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x620)) == 0) goto loc_0025E5A8;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(0x10032ULL)))) & (0xFFFF0000ULL));
    *(uint64_t *)(local_rbp - 0x70) = *(uint64_t *)(gs_base + (0 + 0x188));
    v_stack_p38 = (uint32_t)(Arg2);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5A0)))) & (1)) != 0) goto loc_0025E5A8;
    v_stack_p60 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC0A662)));
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x620) != 0) goto loc_0025DE6C;
    result = ExAllocatePool2(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x620) + 72, 512, (uint32_t)(0x72546552ULL), *(uint64_t *)(local_rdi + 0x10));
    if (result == 0) goto loc_0025E5A8;
    *(uint64_t *)(result + 0x10) = local_rdi;
    *(uint32_t *)(result + 0x1C) = (uint32_t)((uint32_t)(Arg7));
    *(uint32_t *)(result + 0x28) = (uint32_t)((uint32_t)(Arg12));
    result = 0;
    *(uint32_t *)(result + 0x20) = 0;
    if (condition_is_equal) goto loc_0025DED2;
    Arg2 = 0;
    result = ExFreePoolWithTag(0, Arg2, (uint32_t)(0x72546552ULL), *(uint64_t *)(local_rdi + 0x10));
loc_0025DE6C:
loc_0025DE71:
    if (0 >= 8) goto loc_0025DEA2;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x1C)))) != ((uint32_t)((uint32_t)(Arg7)))) goto loc_0025DE8B;
    if ((*(uint64_t *)(0 + 0x10)) != local_rdi) goto loc_0025DE8B;
    if ((*(uint32_t *)(0 + 0x28)) == ((uint32_t)((uint32_t)(Arg12)))) goto loc_0025DEC6;
loc_0025DE8B:
    if (0 != 0) goto loc_0025DF1A;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x1C))) == 0) goto loc_0025DF17;
    if ((*(uint32_t *)(0 + 0x28)) >= ((uint32_t)((uint32_t)(Arg12)))) goto loc_0025DF1A;
loc_0025DEA2:
    if (0 != 0) {
        *(uint64_t *)(0 + 0x10) = local_rdi;
        *(uint32_t *)(0 + 0x1C) = (uint32_t)((uint32_t)(Arg7));
        *(uint64_t *)(0 + 0x20) = 0;
        *(uint64_t *)(0) = 0;
        *(uint64_t *)(0 + 0x8) = 0;
        *(uint32_t *)(0 + 0x18) = 0;
        *(uint32_t *)(0 + 0x28) = (uint32_t)((uint32_t)(Arg12));
        *(uint32_t *)(0 + 0x2C) = 0;
    }
    if (0 == 0) goto loc_0025E5A8;
loc_0025DED2:
    if ((*(uint32_t *)(0 + 0x20)) == 0) goto loc_0025E560;
    local_r13 = (uint32_t)((local_r13) + 1);
    if (((uint32_t)((uint32_t)(Arg13))) == 0x10022ULL) goto loc_0025E517;
    if (((uint32_t)((uint32_t)(Arg13))) != 0x10032ULL) goto loc_0025E5A8;
    *(uint32_t *)(0 + 0x20) = 2;
    goto loc_0025E5A8;
loc_0025DF17:
loc_0025DF1A:
    local_r14 = (0) + (64);
    Arg1 = (uint32_t)((0) + 1);
    goto loc_0025DE71;
loc_0025DF25:
    if (Arg9 != 0) goto loc_0025DF5B;
    if (Arg9 == Arg9) goto loc_0025DD45;
    result = KxWaitForLockChainValid(Arg9, (uint32_t)(Arg7), (uint32_t)(Arg13), (uint32_t)(*(uint32_t *)(0 + 0x1C)));
loc_0025DF5B:
    v_stack_p48 = 0;
    result = (uint8_t)((Arg10) ^ ((uint8_t)(Arg10)));
    if ((((uint8_t)(result)) & (4)) == 0) goto loc_0025DD45;
    Arg3 = (result + 8) >> (5);
    Arg3 = (uint32_t)((Arg3) & (127));
    result = KeDisableInterrupts(Arg10, (uint32_t)(Arg7), Arg3, (uint32_t)(*(uint32_t *)(0 + 0x1C)));
    result = KiHaltOnAddressWakeEntireList(Arg10, 0, Arg3, (uint32_t)(*(uint32_t *)(0 + 0x1C)));
    if ((uint8_t)((uint8_t)(result)) == 0) goto loc_0025DD45;
    goto loc_0025DD45;
loc_0025DFCB:
    if ((((uint8_t)((uint8_t)(result))) & (3)) != 0) goto loc_0025DAF7;
    goto loc_0025DA59;
loc_0025DFD9:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(*(uint64_t *)(gs_base + (0 + 0x20))), 2, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), (uint32_t)(*(uint32_t *)(0 + 0x1C)));
    goto loc_0025D963;
loc_0025DFEB:
    if (*(uint64_t *)(local_rdi + 0x10) == 0) goto loc_0025DCBD;
    if (((uint32_t)(result)) >= (*(uint32_t *)(*(uint64_t *)(local_rdi + 0x10) + 0x8))) goto loc_0025DCBD;
    Arg2 = ((uint32_t)((uint32_t)(result))) << (4);
    Arg2 = (Arg2) + (*(uint64_t *)(local_rdi + 0x10));
    if ((*(uint64_t *)(Arg2)) != local_r14) goto loc_0025DCBD;
    goto loc_0025E179;
loc_0025E019:
    Arg4 = ((uint32_t)(*(uint32_t *)(Arg2 + 0x8))) << (4);
    Arg4 = (Arg4) + (Arg2);
    Arg2 = (Arg2) + (16);
    if (((uint8_t)(*(uint64_t *)(gs_base + (0 + 0x20)))) >= (*(uint64_t *)(local_rdi + 0x10))) goto loc_0025E04F;
loc_0025E02D:
    if ((*(uint64_t *)(Arg2)) == local_r14) goto loc_0025E15D;
    if (*(uint64_t *)(Arg2) == 0) goto loc_0025E046;
    Arg1 = ((uint8_t)(*(uint64_t *)(gs_base + (0 + 0x20)))) + 1;
    if (Arg1 == (*(uint64_t *)(local_rdi + 0x10))) goto loc_0025E04F;
loc_0025E046:
    Arg2 = (Arg2) + (16);
    if (Arg2 != Arg4) goto loc_0025E02D;
loc_0025E04F:
    goto loc_0025DCD4;
loc_0025E058:
    *(uint64_t *)(local_rdi + 0x28) = *(uint64_t *)(*(uint64_t *)(local_rdi + 0x28));
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rdi + 0x28)) + 0x8)) != (*(uint64_t *)(local_rdi + 0x28))) goto loc_0025E08B;
loc_0025E08B:
    goto loc_0025E11C;
loc_0025E096:
    *(uint64_t *)(local_rbp - 0x70) = Arg11;
    *(uint64_t *)(local_rbp - 0x78) = *(uint64_t *)(gs_base + (0 + 0x20));
    *(uint64_t *)(local_rbp - 0x80) = *(uint64_t *)(local_rbp - 0x68);
    result = (*(uint64_t *)(local_rbp - 0x68)) + (24);
    v_stack_p78 = *(uint64_t *)(*(uint64_t *)(local_rbp - 0x68));
    v_stack_p70 = result;
    result = KiAcquireKobjectLockSafe(result, *(uint64_t *)(*(uint64_t *)(local_rdi + 0x28)), *(uint64_t *)(local_rdi + 0x10), Arg4);
    *(uint32_t *)(*(uint64_t *)(local_rbp - 0x80) + 0x1C) = (uint32_t)(local_r14);
    v_stack_p38 = *(uint64_t *)(local_rbp - 0x80) + 24 + 8;
    v_stack_p68 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp - 0x80) + 0x18 + 0x8));
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp - 0x80) + 0x18 + 0x8)) + 0x8)) != (*(uint64_t *)(*(uint64_t *)(local_rbp - 0x80) + 0x18 + 0x8))) goto loc_0025E11C;
loc_0025E11C:
loc_0025E121:
    result = (uint8_t)(((uint8_t)(local_r14)) & (3));
    if (((uint8_t)(result)) == 3) goto loc_0025D9AC;
    if (local_r14 == (*(uint64_t *)(local_rdi + 0x10))) goto loc_0025D9AC;
    v_stack_p20 = 0;
    result = KeBugCheckEx(366, local_rdi, *(uint64_t *)(local_rdi + 0x10), local_r14);
loc_0025E14E:
    result = KxWaitForLockOwnerShip(Arg9, local_rdi, *(uint64_t *)(local_rdi + 0x10), local_r14);
    goto loc_0025D986;
loc_0025E15D:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) - (*(uint32_t *)(local_rdi + 0x10)));
    result = (result) >> (4);
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x460) = (uint8_t)(result);
loc_0025E179:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x8))))) >> (3));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rdi + 0x8))) & (7));
    local_r14 = (uint32_t)((result * 8 - 8) | (Arg1));
    *(uint32_t *)(local_rdi + 0x8) = (uint32_t)(local_r14);
    local_r14 = (uint32_t)((local_r14) >> (3));
    v_stack_p60 = (uint32_t)(local_r14);
    if ((uint32_t)(local_r14) != 0) goto loc_0025E2D6;
    result = ExpFreeOwnerEntry(local_rdi, local_rdi, *(uint64_t *)(local_rdi + 0x10), local_r14);
    v_stack_p44 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x44)));
    if ((*(uint32_t *)(local_rdi + 0x40)) > 1) goto loc_0025E1D1;
loc_0025E1D1:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rdi + 0x40))) - 1);
    Arg1 = (uint32_t)((0) + ((uint32_t)(result)));
    *(uint32_t *)(local_rdi + 0x40) = Arg1;
    if (!(condition_is_not_equal)) {
        *(uint16_t *)(local_rdi + 0x18) = 0;
    }
    if ((*(uint32_t *)(local_rdi + 0x4C)) != 0) goto loc_0025E1F6;
    if ((*(uint32_t *)(local_rdi + 0x48)) == 0) {
        Arg1 = 249;
    }
    v_stack_p68 = (uint32_t)(*(uint8_t *)(local_rdi + 0x1B));
    result = *(uint8_t *)(local_rdi + 0x1B);
    if (0 != 0) {
        result = *(uint32_t *)(local_rdi + 0x38);
        result = (uint32_t)((result) & (7));
        *(uint64_t *)(local_rdi + 0x30) = 0;
        result = (uint32_t)((result) | (8));
        *(uint32_t *)(local_rdi + 0x38) = (uint32_t)(result);
    }
    if (((*(uint8_t *)(v_rip + 0xD688EC)) & (1)) != 0) goto loc_0025E26F;
loc_0025E21C:
    if (Arg9 != 0) goto loc_0025E24E;
    if (Arg9 == Arg9) goto loc_0025E287;
    result = KxWaitForLockChainValid(Arg9, local_rdi, *(uint64_t *)(local_rdi + 0x10), local_r14);
loc_0025E24E:
    v_stack_p48 = 0;
    result = (uint8_t)((Arg10) ^ ((uint8_t)(Arg10)));
    if ((((uint8_t)(result)) & (4)) == 0) goto loc_0025E287;
    result = KeWakeAddressAll(result + 8, Arg10, *(uint64_t *)(local_rdi + 0x10), local_r14);
    goto loc_0025E287;
loc_0025E26F:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCAFBE3))) != 0) goto loc_0025E21C;
    result = KiReleaseQueuedSpinLockInstrumented(Arg9, *(uint64_t *)(local_rbp + 0x48), *(uint64_t *)(local_rdi + 0x10), local_r14);
loc_0025E287:
    if ((*(uint32_t *)(v_rip + 0xD68A93)) != 0) {
        Arg1 = 2;
        Arg2 = Arg11;
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, *(uint64_t *)(local_rdi + 0x10), local_r14);
    }
    local_rbx = 1;
    if (0 != 0) { local_rbx = 3; }
    v_stack_p60 = 0;
    v_stack_p38 = (uint32_t)((uint32_t)(0x10042ULL));
    goto loc_0025E32E;
loc_0025E2D6:
    v_stack_p38 = (uint32_t)((uint32_t)(0x10052ULL));
    v_stack_p44 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x44)));
    result = KiReleaseQueuedSpinLockInstrumented(Arg9, *(uint64_t *)(local_rbp + 0x48), *(uint64_t *)(local_rdi + 0x10), local_r14);
    if ((*(uint32_t *)(v_rip + 0xD68A09)) != 0) {
        Arg1 = Arg11;
        Arg2 = Arg11;
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, *(uint64_t *)(local_rdi + 0x10), local_r14);
    }
loc_0025E32E:
    if ((uint32_t)(local_r13) == 0) goto loc_0025E5A8;
    *(uint64_t *)(local_rbp - 0x28) = v_xmm0;
    *(uint64_t *)(local_rbp - 0x18) = v_xmm0;
    *(uint64_t *)(local_rbp - 0x8) = v_xmm0;
    Arg2 = (Arg2) << (32);
    result = (result) | (Arg2);
    v_stack_p78 = result;
    v_stack_p40 = (uint16_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xD0));
    v_stack_p30 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xD1));
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x620)) == 0) goto loc_0025E5A8;
    local_r15 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(0x10052ULL)))) & (0xFFFF0000ULL));
    *(uint64_t *)(local_rbp - 0x70) = *(uint64_t *)(gs_base + (0 + 0x188));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5A0)))) & (1)) != 0) goto loc_0025E5A8;
    v_stack_p68 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC0A09A)));
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x620) != 0) goto loc_0025E42D;
    result = ExAllocatePool2(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x620) + 72, 512, (uint32_t)(0x72546552ULL), local_r14);
    if (result == 0) goto loc_0025E5A8;
    *(uint64_t *)(result + 0x10) = local_rdi;
    *(uint32_t *)(result + 0x1C) = (uint32_t)(local_r15);
    *(uint32_t *)(result + 0x20) = 0;
    *(uint32_t *)(result + 0x28) = (uint32_t)((uint32_t)(Arg13));
    result = 0;
    if (condition_is_equal) goto loc_0025E49B;
    Arg2 = 0;
    result = ExFreePoolWithTag(0, Arg2, (uint32_t)(0x72546552ULL), local_r14);
loc_0025E42D:
    if (0 >= 8) goto loc_0025E46A;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x1C)))) != ((uint32_t)(local_r15))) goto loc_0025E44C;
    if ((*(uint64_t *)(0 + 0x10)) != local_rdi) goto loc_0025E44C;
    if ((*(uint32_t *)(0 + 0x28)) == ((uint32_t)((uint32_t)(Arg13)))) goto loc_0025E48F;
loc_0025E44C:
loc_0025E46A:
    if (0 != 0) {
        *(uint64_t *)(0 + 0x10) = local_rdi;
        *(uint32_t *)(0 + 0x1C) = (uint32_t)(local_r15);
        *(uint64_t *)(0 + 0x20) = 0;
        *(uint64_t *)(0) = 0;
        *(uint64_t *)(0 + 0x8) = 0;
        *(uint32_t *)(0 + 0x18) = 0;
        *(uint32_t *)(0 + 0x28) = (uint32_t)((uint32_t)(Arg13));
        *(uint32_t *)(0 + 0x2C) = 0;
    }
    if (0 == 0) goto loc_0025E5A8;
loc_0025E49B:
    if ((*(uint32_t *)(0 + 0x20)) == 0) goto loc_0025E560;
    result = (uint32_t)(((uint32_t)(Arg12)) + 1);
    Arg2 = 0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EF0))) + (*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EEC)));
    goto loc_0025E560;
loc_0025E517:
    Arg2 = 0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r15 + 0x8EF0))) + (*(uint32_t *)(local_r15 + 0x8EEC)));
loc_0025E560:
    *(uint32_t *)(0 + 0x1C) = 0;
    goto loc_0025E5A8;
loc_0025E5A8:
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, (uint32_t)(Arg7), 0);
    Arg1 = (*(uint64_t *)(local_rbp + 0x18)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, (uint32_t)(Arg7), 0);
    local_rsp = (local_rsp) + (304);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg10` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0025D903&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
