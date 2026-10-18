# AlpcpQueueIoCompletionPort

- RVA: `0x003FF760`–`0x003FFE13` (길이 `1,715` bytes)
- VA: `0x00000001403FF760`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0009A0D8`
- 디코드: `408`개 명령, `1,715/1,715` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **25**; 고유 호출 대상: **22**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x003FF854` → [KxWaitForLockChainValid](../21/KxWaitForLockChainValid_function_00217AA0.md) (function, `0x00217AA0`)
- `0x003FF873` → [KeWakeAddressAll](../21/KeWakeAddressAll_function_00217C20.md) (function, `0x00217C20`)
- `0x003FF891` → [KiReleaseQueuedSpinLockInstrumented](../21/KiReleaseQueuedSpinLockInstrumented_function_002179F0.md) (function, `0x002179F0`)
- `0x003FF8AD` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x003FF8D6` → [KeAbPostRelease](../2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x003FF9A2` → [KiAcquireKobjectLockSafe](../25/KiAcquireKobjectLockSafe_function_00251C90.md) (function, `0x00251C90`)
- `0x003FFA20` → [KiAcquireQueuedSpinLockInstrumented](../27/KiAcquireQueuedSpinLockInstrumented_function_00275850.md) (function, `0x00275850`)
- `0x003FFA31` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x003FFA40` → [KxWaitForLockOwnerShip](../25/KxWaitForLockOwnerShip_function_00257EB0.md) (function, `0x00257EB0`)
- `0x003FFA4F` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x003FFA7B` → [AlpcpQueueIoCompletion](../39/AlpcpQueueIoCompletion_function_00397480.md) (function, `0x00397480`)
- `0x003FFAAA` → [ExfReleasePushLockShared](../26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x003FFAB6` → [KeAbPostRelease](../2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x003FFB01` → [KiRemovePrcbWaitEntry](../25/KiRemovePrcbWaitEntry_function_002502D0.md) (function, `0x002502D0`)
- `0x003FFBCC` → [IopAllocateMiniCompletionPacket](../../page/9D/IopAllocateMiniCompletionPacket_function_009DA2E0.md) (function, `0x009DA2E0`)
- `0x003FFC5D` → [KiWakeOtherQueueWaiters](../39/KiWakeOtherQueueWaiters_function_003964D0.md) (function, `0x003964D0`)
- `0x003FFCA1` → [KiExitDispatcher](../25/KiExitDispatcher_function_00251CF0.md) (function, `0x00251CF0`)
- `0x003FFCE7` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x003FFD0E` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x003FFD1D` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x003FFD2A` → [KeIsThreadRunning](../39/KeIsThreadRunning_function_00396720.md) (function, `0x00396720`)
- `0x003FFD39` → [EtwTraceEnqueueWork](../39/EtwTraceEnqueueWork_function_0039674C.md) (function, `0x0039674C`)
- `0x003FFD7C` → [KiCompleteDirectSwitchThread](KiCompleteDirectSwitchThread_function_003FFE1C.md) (function, `0x003FFE1C`)
- `0x003FFD92` → [ExfReleasePushLockShared](../26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x003FFDFD` → [KeAcquireInStackQueuedSpinLock](../27/KeAcquireInStackQueuedSpinLock_function_002757A0.md) (function, `0x002757A0`)

### Direct callers
- [sub_0088EC77](../../page/88/Unknown_function_0088EC77.md) at `0x0088EFF4`
- [AlpcpAssociateIoCompletionPort](../../page/A1/AlpcpAssociateIoCompletionPort_function_00A1A28C.md) at `0x00A1A444`
- [AlpcpAdjustCompletionListConcurrencyCount](../../page/A1/AlpcpAdjustCompletionListConcurrencyCount_function_00A1A62C.md) at `0x00A1A6B7`
- [AlpcpSignalPortAndUnlock](../../page/A7/AlpcpSignalPortAndUnlock_function_00A76910.md) at `0x00A7693B`

### Static image references
- `0x003FF7C1` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x003FF7CE` → RVA `0x00FC6B06` (`ALMOSTRO`; read)
- `0x003FF87A` → RVA `0x00F0DE58` (`.data`; read)
- `0x003FF94A` → RVA `0x00FC6B04` (`ALMOSTRO`; read)
- `0x003FFC01` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x003FFD00` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x003FFBCC` → [IopAllocateMiniCompletionPacket](../../page/9D/IopAllocateMiniCompletionPacket_function_009DA2E0.md) (`.text` → `PAGE`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x003FFE05` → [sub_006EC0B0](../6E/Unknown_function_006EC0B0.md) (`tail-transfer`)
  - `0x003FFE0E` → [sub_006EC0B0 + 0x3](../6E/Unknown_function_006EC0B0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003FF760  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
003FF765  48 89 6C 24 18                  mov qword ptr [rsp + 0x18], rbp
003FF76A  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
003FF76F  57                              push rdi
003FF770  41 54                           push r12
003FF772  41 55                           push r13
003FF774  41 56                           push r14
003FF776  41 57                           push r15
003FF778  48 83 EC 60                     sub rsp, 0x60
003FF77C  48 8B 59 30                     mov rbx, qword ptr [rcx + 0x30]
003FF780  33 C0                           xor eax, eax
003FF782  4C 8B 69 20                     mov r13, qword ptr [rcx + 0x20]
003FF786  0F 57 C0                        xorps xmm0, xmm0
003FF789  44 8B A4 24 B0 00 00 00         mov r12d, dword ptr [rsp + 0xb0]
003FF791  45 0F B6 F9                     movzx r15d, r9b
003FF795  0F 11 44 24 48                  movups xmmword ptr [rsp + 0x48], xmm0
003FF79A  48 89 5C 24 50                  mov qword ptr [rsp + 0x50], rbx
003FF79F  45 0F B6 F0                     movzx r14d, r8b
003FF7A3  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
003FF7A8  0F B6 EA                        movzx ebp, dl
003FF7AB  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
003FF7B0  48 8B F1                        mov rsi, rcx
003FF7B3  90                              nop
003FF7B4  44 0F 20 C7                     mov rdi, cr8
003FF7B8  B8 02 00 00 00                  mov eax, 2
003FF7BD  44 0F 22 C0                     mov cr8, rax
003FF7C1  83 3D 58 75 BC 00 00            cmp dword ptr [rip + 0xbc7558], 0
003FF7C8  0F 85 5C 02 00 00               jne 0x1403ffa2a
003FF7CE  F6 05 31 73 BC 00 21            test byte ptr [rip + 0xbc7331], 0x21
003FF7D5  40 88 7C 24 58                  mov byte ptr [rsp + 0x58], dil
003FF7DA  0F 85 2A 02 00 00               jne 0x1403ffa0a
003FF7E0  48 8D 54 24 48                  lea rdx, [rsp + 0x48]
003FF7E5  48 87 13                        xchg qword ptr [rbx], rdx
003FF7E8  48 85 D2                        test rdx, rdx
003FF7EB  0F 85 4A 02 00 00               jne 0x1403ffa3b
003FF7F1  8B 53 0C                        mov edx, dword ptr [rbx + 0xc]
003FF7F4  3B 53 08                        cmp edx, dword ptr [rbx + 8]
003FF7F7  0F 83 4D 02 00 00               jae 0x1403ffa4a
003FF7FD  48 8B 4B 20                     mov rcx, qword ptr [rbx + 0x20]
003FF801  48 85 C9                        test rcx, rcx
003FF804  74 07                           je 0x1403ff80d
003FF806  48 8B 01                        mov rax, qword ptr [rcx]
003FF809  48 89 43 20                     mov qword ptr [rbx + 0x20], rax
003FF80D  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
003FF811  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
003FF816  8D 42 01                        lea eax, [rdx + 1]
003FF819  89 43 0C                        mov dword ptr [rbx + 0xc], eax
003FF81C  F6 05 E3 72 BC 00 01            test byte ptr [rip + 0xbc72e3], 1
003FF823  75 55                           jne 0x1403ff87a
003FF825  0F 0D 4C 24 48                  prefetchw byte ptr [rsp + 0x48]
003FF82A  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
003FF82F  33 FF                           xor edi, edi
003FF831  48 85 C0                        test rax, rax
003FF834  75 23                           jne 0x1403ff859
003FF836  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
003FF83B  48 8D 44 24 48                  lea rax, [rsp + 0x48]
003FF840  F0 48 0F B1 39                  lock cmpxchg qword ptr [rcx], rdi
003FF845  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
003FF84A  48 3B C1                        cmp rax, rcx
003FF84D  74 49                           je 0x1403ff898
003FF84F  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
003FF854  E8 47 82 E1 FF                  call 0x140217aa0
003FF859  48 8D 48 08                     lea rcx, [rax + 8]
003FF85D  48 89 7C 24 48                  mov qword ptr [rsp + 0x48], rdi
003FF862  48 8B 54 24 50                  mov rdx, qword ptr [rsp + 0x50]
003FF867  48 8B C2                        mov rax, rdx
003FF86A  48 87 01                        xchg qword ptr [rcx], rax
003FF86D  32 C2                           xor al, dl
003FF86F  A8 04                           test al, 4
003FF871  74 25                           je 0x1403ff898
003FF873  E8 A8 83 E1 FF                  call 0x140217c20
003FF878  EB 1E                           jmp 0x1403ff898
003FF87A  8B 05 D8 E5 B0 00               mov eax, dword ptr [rip + 0xb0e5d8]
003FF880  85 C0                           test eax, eax
003FF882  75 A1                           jne 0x1403ff825
003FF884  48 8B 94 24 88 00 00 00         mov rdx, qword ptr [rsp + 0x88]
003FF88C  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
003FF891  E8 5A 81 E1 FF                  call 0x1402179f0
003FF896  33 FF                           xor edi, edi
003FF898  83 3D 81 74 BC 00 00            cmp dword ptr [rip + 0xbc7481], 0
003FF89F  0F B6 5C 24 58                  movzx ebx, byte ptr [rsp + 0x58]
003FF8A4  74 0C                           je 0x1403ff8b2
003FF8A6  44 0F 20 C1                     mov rcx, cr8
003FF8AA  0F B6 D3                        movzx edx, bl
003FF8AD  E8 E6 5D 0F 00                  call 0x1404f5698
003FF8B2  44 0F 22 C3                     mov cr8, rbx
003FF8B6  45 84 F6                        test r14b, r14b
003FF8B9  74 20                           je 0x1403ff8db
003FF8BB  B8 11 00 00 00                  mov eax, 0x11
003FF8C0  F0 48 0F B1 BE 60 01 00 00      lock cmpxchg qword ptr [rsi + 0x160], rdi
003FF8C9  0F 85 BC 04 00 00               jne 0x1403ffd8b
003FF8CF  48 8D 8E 60 01 00 00            lea rcx, [rsi + 0x160]
003FF8D6  E8 25 1D EE FF                  call 0x1402e1600
003FF8DB  48 8B 7E 28                     mov rdi, qword ptr [rsi + 0x28]
003FF8DF  40 F6 DD                        neg bpl
003FF8E2  48 1B DB                        sbb rbx, rbx
003FF8E5  33 ED                           xor ebp, ebp
003FF8E7  45 84 FF                        test r15b, r15b
003FF8EA  8B C5                           mov eax, ebp
003FF8EC  4C 8B 7C 24 38                  mov r15, qword ptr [rsp + 0x38]
003FF8F1  0F 95 C0                        setne al
003FF8F4  8B F0                           mov esi, eax
003FF8F6  83 CE 04                        or esi, 4
003FF8F9  45 85 E4                        test r12d, r12d
003FF8FC  0F 44 F0                        cmove esi, eax
003FF8FF  89 B4 24 90 00 00 00            mov dword ptr [rsp + 0x90], esi
003FF906  4D 85 FF                        test r15, r15
003FF909  0F 84 B9 02 00 00               je 0x1403ffbc8
003FF90F  49 89 7F 18                     mov qword ptr [r15 + 0x18], rdi
003FF913  4D 8D 65 08                     lea r12, [r13 + 8]
003FF917  49 89 5F 20                     mov qword ptr [r15 + 0x20], rbx
003FF91B  41 89 6F 28                     mov dword ptr [r15 + 0x28], ebp
003FF91F  49 89 6F 30                     mov qword ptr [r15 + 0x30], rbp
003FF923  44 0F 20 C0                     mov rax, cr8
003FF927  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
003FF92C  B9 02 00 00 00                  mov ecx, 2
003FF931  44 0F 22 C1                     mov cr8, rcx
003FF935  39 2D E5 73 BC 00               cmp dword ptr [rip + 0xbc73e5], ebp
003FF93B  0F 85 A0 03 00 00               jne 0x1403ffce1
003FF941  65 48 8B 2C 25 20 00 00 00      mov rbp, qword ptr gs:[0x20]
003FF94A  8B 05 B4 71 BC 00               mov eax, dword ptr [rip + 0xbc71b4]
003FF950  48 89 6C 24 38                  mov qword ptr [rsp + 0x38], rbp
003FF955  48 8B 5D 08                     mov rbx, qword ptr [rbp + 8]
003FF959  0F BA E0 18                     bt eax, 0x18
003FF95D  0F 82 C4 03 00 00               jb 0x1403ffd27
003FF963  41 0F B6 45 01                  movzx eax, byte ptr [r13 + 1]
003FF968  F6 D0                           not al
003FF96A  D1 E8                           shr eax, 1
003FF96C  83 E0 01                        and eax, 1
003FF96F  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
003FF973  48 8B 83 50 06 00 00            mov rax, qword ptr [rbx + 0x650]
003FF97A  48 85 C0                        test rax, rax
003FF97D  48 0F 44 C3                     cmove rax, rbx
003FF981  85 F6                           test esi, esi
003FF983  74 17                           je 0x1403ff99c
003FF985  48 8B 80 20 02 00 00            mov rax, qword ptr [rax + 0x220]
003FF98C  8B 80 88 00 00 00               mov eax, dword ptr [rax + 0x88]
003FF992  0F BA E0 0D                     bt eax, 0xd
003FF996  0F 82 CC 03 00 00               jb 0x1403ffd68
003FF99C  40 32 FF                        xor dil, dil
003FF99F  49 8B CD                        mov rcx, r13
003FF9A2  E8 E9 22 E5 FF                  call 0x140251c90
003FF9A7  4D 39 24 24                     cmp qword ptr [r12], r12
003FF9AB  0F 84 72 02 00 00               je 0x1403ffc23
003FF9B1  41 8B 45 28                     mov eax, dword ptr [r13 + 0x28]
003FF9B5  41 3B 45 2C                     cmp eax, dword ptr [r13 + 0x2c]
003FF9B9  0F 83 5B 02 00 00               jae 0x1403ffc1a
003FF9BF  48 8B 83 E8 00 00 00            mov rax, qword ptr [rbx + 0xe8]
003FF9C6  49 3B C5                        cmp rax, r13
003FF9C9  0F 84 87 03 00 00               je 0x1403ffd56
003FF9CF  49 8B 34 24                     mov rsi, qword ptr [r12]
003FF9D3  33 D2                           xor edx, edx
003FF9D5  66 66 66 0F 1F 84 00 00 00 00 00  nop word ptr [rax + rax]
003FF9E0  48 8B FE                        mov rdi, rsi
003FF9E3  48 8B 36                        mov rsi, qword ptr [rsi]
003FF9E6  80 7F 10 03                     cmp byte ptr [rdi + 0x10], 3
003FF9EA  0F 85 A5 01 00 00               jne 0x1403ffb95
003FF9F0  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
003FF9F4  48 39 7E 08                     cmp qword ptr [rsi + 8], rdi
003FF9F8  75 09                           jne 0x1403ffa03
003FF9FA  48 39 38                        cmp qword ptr [rax], rdi
003FF9FD  0F 84 DF 01 00 00               je 0x1403ffbe2
003FFA03  B9 03 00 00 00                  mov ecx, 3
003FFA08  CD 29                           int 0x29
003FFA0A  8B 05 48 E4 B0 00               mov eax, dword ptr [rip + 0xb0e448]
003FFA10  85 C0                           test eax, eax
003FFA12  0F 85 C8 FD FF FF               jne 0x1403ff7e0
003FFA18  48 8B D3                        mov rdx, rbx
003FFA1B  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
003FFA20  E8 2B 5E E7 FF                  call 0x140275850
003FFA25  E9 C7 FD FF FF                  jmp 0x1403ff7f1
003FFA2A  0F B6 D0                        movzx edx, al
003FFA2D  40 0F B6 CF                     movzx ecx, dil
003FFA31  E8 C6 5C 0F 00                  call 0x1404f56fc
003FFA36  E9 93 FD FF FF                  jmp 0x1403ff7ce
003FFA3B  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
003FFA40  E8 6B 84 E5 FF                  call 0x140257eb0
003FFA45  E9 A7 FD FF FF                  jmp 0x1403ff7f1
003FFA4A  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
003FFA4F  E8 8C 32 F4 FF                  call 0x140342ce0
003FFA54  45 84 FF                        test r15b, r15b
003FFA57  0F 85 88 03 00 00               jne 0x1403ffde5
003FFA5D  32 C9                           xor cl, cl
003FFA5F  48 8B 56 28                     mov rdx, qword ptr [rsi + 0x28]
003FFA63  40 0F B6 C5                     movzx eax, bpl
003FFA67  F6 D8                           neg al
003FFA69  44 89 64 24 28                  mov dword ptr [rsp + 0x28], r12d
003FFA6E  88 4C 24 20                     mov byte ptr [rsp + 0x20], cl
003FFA72  49 8B CD                        mov rcx, r13
003FFA75  4D 1B C0                        sbb r8, r8
003FFA78  45 33 C9                        xor r9d, r9d
003FFA7B  E8 00 7A F9 FF                  call 0x140397480
003FFA80  85 C0                           test eax, eax
003FFA82  0F 84 6D 03 00 00               je 0x1403ffdf5
003FFA88  45 84 F6                        test r14b, r14b
003FFA8B  0F 84 15 02 00 00               je 0x1403ffca6
003FFA91  B8 11 00 00 00                  mov eax, 0x11
003FFA96  33 FF                           xor edi, edi
003FFA98  F0 48 0F B1 BE 60 01 00 00      lock cmpxchg qword ptr [rsi + 0x160], rdi
003FFAA1  74 0C                           je 0x1403ffaaf
003FFAA3  48 8D 8E 60 01 00 00            lea rcx, [rsi + 0x160]
003FFAAA  E8 91 39 E6 FF                  call 0x140263440
003FFAAF  48 8D 8E 60 01 00 00            lea rcx, [rsi + 0x160]
003FFAB6  E8 45 1B EE FF                  call 0x1402e1600
003FFABB  E9 E6 01 00 00                  jmp 0x1403ffca6
003FFAC0  0F B6 83 84 01 00 00            movzx eax, byte ptr [rbx + 0x184]
003FFAC7  3C 05                           cmp al, 5
003FFAC9  0F 85 E9 00 00 00               jne 0x1403ffbb8
003FFACF  0F B6 4B 70                     movzx ecx, byte ptr [rbx + 0x70]
003FFAD3  8B C1                           mov eax, ecx
003FFAD5  83 E0 07                        and eax, 7
003FFAD8  83 F8 01                        cmp eax, 1
003FFADB  0F 85 BB 02 00 00               jne 0x1403ffd9c
003FFAE1  48 8B 93 E8 00 00 00            mov rdx, qword ptr [rbx + 0xe8]
003FFAE8  48 85 D2                        test rdx, rdx
003FFAEB  74 11                           je 0x1403ffafe
003FFAED  0F B6 02                        movzx eax, byte ptr [rdx]
003FFAF0  24 7F                           and al, 0x7f
003FFAF2  3C 15                           cmp al, 0x15
003FFAF4  0F 84 CB 01 00 00               je 0x1403ffcc5
003FFAFA  F0 FF 42 28                     lock inc dword ptr [rdx + 0x28]
003FFAFE  48 8B CB                        mov rcx, rbx
003FFB01  E8 CA 07 E5 FF                  call 0x1402502d0
003FFB06  0F B6 83 84 01 00 00            movzx eax, byte ptr [rbx + 0x184]
003FFB0D  3C 01                           cmp al, 1
003FFB0F  0F 84 38 02 00 00               je 0x1403ffd4d
003FFB15  3C 05                           cmp al, 5
003FFB17  75 26                           jne 0x1403ffb3f
003FFB19  48 B8 20 03 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000320
003FFB23  8B 08                           mov ecx, dword ptr [rax]
003FFB25  2B 8B B4 01 00 00               sub ecx, dword ptr [rbx + 0x1b4]
003FFB2B  44 38 B3 87 01 00 00            cmp byte ptr [rbx + 0x187], r14b
003FFB32  0F 84 84 00 00 00               je 0x1403ffbbc
003FFB38  48 01 8B E8 03 00 00            add qword ptr [rbx + 0x3e8], rcx
003FFB3F  48 8B 54 24 38                  mov rdx, qword ptr [rsp + 0x38]
003FFB44  48 8D 8B D8 00 00 00            lea rcx, [rbx + 0xd8]
003FFB4B  C6 83 84 01 00 00 07            mov byte ptr [rbx + 0x184], 7
003FFB52  41 B6 01                        mov r14b, 1
003FFB55  48 8B 82 08 2D 00 00            mov rax, qword ptr [rdx + 0x2d08]
003FFB5C  48 89 01                        mov qword ptr [rcx], rax
003FFB5F  48 89 8A 08 2D 00 00            mov qword ptr [rdx + 0x2d08], rcx
003FFB66  33 D2                           xor edx, edx
003FFB68  4C 89 BB C8 00 00 00            mov qword ptr [rbx + 0xc8], r15
003FFB6F  48 89 93 D0 03 00 00            mov qword ptr [rbx + 0x3d0], rdx
003FFB76  48 89 53 40                     mov qword ptr [rbx + 0x40], rdx
003FFB7A  0F B6 47 11                     movzx eax, byte ptr [rdi + 0x11]
003FFB7E  FE C0                           inc al
003FFB80  88 47 11                        mov byte ptr [rdi + 0x11], al
003FFB83  45 84 F6                        test r14b, r14b
003FFB86  0F 85 65 01 00 00               jne 0x1403ffcf1
003FFB8C  49 3B F4                        cmp rsi, r12
003FFB8F  0F 85 4B FE FF FF               jne 0x1403ff9e0
003FFB95  8B B4 24 90 00 00 00            mov esi, dword ptr [rsp + 0x90]
003FFB9C  48 8B 6C 24 38                  mov rbp, qword ptr [rsp + 0x38]
003FFBA1  E9 7D 00 00 00                  jmp 0x1403ffc23
003FFBA6  83 F8 05                        cmp eax, 5
003FFBA9  0F 85 22 02 00 00               jne 0x1403ffdd1
003FFBAF  80 E1 FE                        and cl, 0xfe
003FFBB2  80 C9 06                        or cl, 6
003FFBB5  88 4B 70                        mov byte ptr [rbx + 0x70], cl
003FFBB8  33 D2                           xor edx, edx
003FFBBA  EB BA                           jmp 0x1403ffb76
003FFBBC  48 01 8B E0 03 00 00            add qword ptr [rbx + 0x3e0], rcx
003FFBC3  E9 77 FF FF FF                  jmp 0x1403ffb3f
003FFBC8  33 D2                           xor edx, edx
003FFBCA  B1 01                           mov cl, 1
003FFBCC  E8 0F A7 5D 00                  call 0x1409da2e0
003FFBD1  4C 8B F8                        mov r15, rax
003FFBD4  48 85 C0                        test rax, rax
003FFBD7  0F 85 32 FD FF FF               jne 0x1403ff90f
003FFBDD  E9 C4 00 00 00                  jmp 0x1403ffca6
003FFBE2  48 89 30                        mov qword ptr [rax], rsi
003FFBE5  45 32 F6                        xor r14b, r14b
003FFBE8  48 89 46 08                     mov qword ptr [rsi + 8], rax
003FFBEC  8B EA                           mov ebp, edx
003FFBEE  48 8B 5F 18                     mov rbx, qword ptr [rdi + 0x18]
003FFBF2  F0 48 0F BA 6B 40 00            lock bts qword ptr [rbx + 0x40], 0
003FFBF9  0F 83 C1 FE FF FF               jae 0x1403ffac0
003FFBFF  FF C5                           inc ebp
003FFC01  85 2D A5 56 BC 00               test dword ptr [rip + 0xbc56a5], ebp
003FFC07  0F 84 F3 00 00 00               je 0x1403ffd00
003FFC0D  F3 90                           pause
003FFC0F  48 8B 43 40                     mov rax, qword ptr [rbx + 0x40]
003FFC13  48 85 C0                        test rax, rax
003FFC16  74 DA                           je 0x1403ffbf2
003FFC18  EB E5                           jmp 0x1403ffbff
003FFC1A  40 84 FF                        test dil, dil
003FFC1D  0F 85 9C FD FF FF               jne 0x1403ff9bf
003FFC23  41 8B 4D 04                     mov ecx, dword ptr [r13 + 4]
003FFC27  8D 41 01                        lea eax, [rcx + 1]
003FFC2A  41 89 45 04                     mov dword ptr [r13 + 4], eax
003FFC2E  49 8D 45 18                     lea rax, [r13 + 0x18]
003FFC32  48 8B 50 08                     mov rdx, qword ptr [rax + 8]
003FFC36  48 39 02                        cmp qword ptr [rdx], rax
003FFC39  0F 85 C4 FD FF FF               jne 0x1403ffa03
003FFC3F  49 89 07                        mov qword ptr [r15], rax
003FFC42  49 89 57 08                     mov qword ptr [r15 + 8], rdx
003FFC46  4C 89 3A                        mov qword ptr [rdx], r15
003FFC49  4C 89 78 08                     mov qword ptr [rax + 8], r15
003FFC4D  85 C9                           test ecx, ecx
003FFC4F  75 11                           jne 0x1403ffc62
003FFC51  4D 39 24 24                     cmp qword ptr [r12], r12
003FFC55  74 0B                           je 0x1403ffc62
003FFC57  49 8B D5                        mov rdx, r13
003FFC5A  48 8B CD                        mov rcx, rbp
003FFC5D  E8 6E 68 F9 FF                  call 0x1403964d0
003FFC62  33 D2                           xor edx, edx
003FFC64  F0 41 81 65 00 7F FF FF FF      lock and dword ptr [r13], 0xffffff7f
003FFC6D  40 F6 C6 01                     test sil, 1
003FFC71  0F 85 CC 00 00 00               jne 0x1403ffd43
003FFC77  8B CA                           mov ecx, edx
003FFC79  40 F6 C6 04                     test sil, 4
003FFC7D  0F 85 ED 00 00 00               jne 0x1403ffd70
003FFC83  48 8B 5C 24 38                  mov rbx, qword ptr [rsp + 0x38]
003FFC88  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
003FFC8D  8B D1                           mov edx, ecx
003FFC8F  44 8B 4C 24 30                  mov r9d, dword ptr [rsp + 0x30]
003FFC94  48 8B CB                        mov rcx, rbx
003FFC97  41 B8 01 00 00 00               mov r8d, 1
003FFC9D  88 44 24 20                     mov byte ptr [rsp + 0x20], al
003FFCA1  E8 4A 20 E5 FF                  call 0x140251cf0
003FFCA6  4C 8D 5C 24 60                  lea r11, [rsp + 0x60]
003FFCAB  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
003FFCAF  49 8B 6B 40                     mov rbp, qword ptr [r11 + 0x40]
003FFCB3  49 8B 73 48                     mov rsi, qword ptr [r11 + 0x48]
003FFCB7  49 8B E3                        mov rsp, r11
003FFCBA  41 5F                           pop r15
003FFCBC  41 5E                           pop r14
003FFCBE  41 5D                           pop r13
003FFCC0  41 5C                           pop r12
003FFCC2  5F                              pop rdi
003FFCC3  C3                              ret
003FFCC4  CC                              int3
003FFCC5  8B 83 1C 02 00 00               mov eax, dword ptr [rbx + 0x21c]
003FFCCB  0F B6 C0                        movzx eax, al
003FFCCE  89 83 1C 02 00 00               mov dword ptr [rbx + 0x21c], eax
003FFCD4  F0 FF 84 82 18 02 00 00         lock inc dword ptr [rdx + rax*4 + 0x218]
003FFCDC  E9 1D FE FF FF                  jmp 0x1403ffafe
003FFCE1  0F B6 D1                        movzx edx, cl
003FFCE4  0F B6 C8                        movzx ecx, al
003FFCE7  E8 10 5A 0F 00                  call 0x1404f56fc
003FFCEC  E9 50 FC FF FF                  jmp 0x1403ff941
003FFCF1  8B B4 24 90 00 00 00            mov esi, dword ptr [rsp + 0x90]
003FFCF8  49 89 17                        mov qword ptr [r15], rdx
003FFCFB  E9 64 FF FF FF                  jmp 0x1403ffc64
003FFD00  8B 05 B2 6D BC 00               mov eax, dword ptr [rip + 0xbc6db2]
003FFD06  A8 40                           test al, 0x40
003FFD08  0F 84 FF FE FF FF               je 0x1403ffc0d
003FFD0E  E8 7D F7 F0 FF                  call 0x14030f490
003FFD13  84 C0                           test al, al
003FFD15  0F 84 F2 FE FF FF               je 0x1403ffc0d
003FFD1B  8B CD                           mov ecx, ebp
003FFD1D  E8 3E F7 F0 FF                  call 0x14030f460
003FFD22  E9 E8 FE FF FF                  jmp 0x1403ffc0f
003FFD27  48 8B CB                        mov rcx, rbx
003FFD2A  E8 F1 69 F9 FF                  call 0x140396720
003FFD2F  44 0F B6 C0                     movzx r8d, al
003FFD33  48 8B CB                        mov rcx, rbx
003FFD36  49 8B D7                        mov rdx, r15
003FFD39  E8 0E 6A F9 FF                  call 0x14039674c
003FFD3E  E9 20 FC FF FF                  jmp 0x1403ff963
003FFD43  B9 03 00 00 00                  mov ecx, 3
003FFD48  E9 36 FF FF FF                  jmp 0x1403ffc83
003FFD4D  83 4B 74 02                     or dword ptr [rbx + 0x74], 2
003FFD51  E9 E9 FD FF FF                  jmp 0x1403ffb3f
003FFD56  80 BB 83 02 00 00 0F            cmp byte ptr [rbx + 0x283], 0xf
003FFD5D  0F 85 6C FC FF FF               jne 0x1403ff9cf
003FFD63  E9 BB FE FF FF                  jmp 0x1403ffc23
003FFD68  40 B7 01                        mov dil, 1
003FFD6B  E9 2F FC FF FF                  jmp 0x1403ff99f
003FFD70  48 8B 5C 24 38                  mov rbx, qword ptr [rsp + 0x38]
003FFD75  48 8B CB                        mov rcx, rbx
003FFD78  48 8B 53 08                     mov rdx, qword ptr [rbx + 8]
003FFD7C  E8 9B 00 00 00                  call 0x1403ffe1c
003FFD81  B9 06 00 00 00                  mov ecx, 6
003FFD86  E9 FD FE FF FF                  jmp 0x1403ffc88
003FFD8B  48 8D 8E 60 01 00 00            lea rcx, [rsi + 0x160]
003FFD92  E8 A9 36 E6 FF                  call 0x140263440
003FFD97  E9 33 FB FF FF                  jmp 0x1403ff8cf
003FFD9C  83 F8 04                        cmp eax, 4
003FFD9F  0F 84 3C FD FF FF               je 0x1403ffae1
003FFDA5  85 C0                           test eax, eax
003FFDA7  0F 85 F9 FD FF FF               jne 0x1403ffba6
003FFDAD  80 E1 FA                        and cl, 0xfa
003FFDB0  41 B6 01                        mov r14b, 1
003FFDB3  80 C9 02                        or cl, 2
003FFDB6  88 4B 70                        mov byte ptr [rbx + 0x70], cl
003FFDB9  33 D2                           xor edx, edx
003FFDBB  4C 89 BB C8 00 00 00            mov qword ptr [rbx + 0xc8], r15
003FFDC2  48 89 93 D0 03 00 00            mov qword ptr [rbx + 0x3d0], rdx
003FFDC9  88 57 11                        mov byte ptr [rdi + 0x11], dl
003FFDCC  E9 A5 FD FF FF                  jmp 0x1403ffb76
003FFDD1  33 D2                           xor edx, edx
003FFDD3  83 F8 03                        cmp eax, 3
003FFDD6  0F 85 9A FD FF FF               jne 0x1403ffb76
003FFDDC  C6 47 11 02                     mov byte ptr [rdi + 0x11], 2
003FFDE0  E9 91 FD FF FF                  jmp 0x1403ffb76
003FFDE5  45 84 F6                        test r14b, r14b
003FFDE8  0F 85 6F FC FF FF               jne 0x1403ffa5d
003FFDEE  B1 01                           mov cl, 1
003FFDF0  E9 6A FC FF FF                  jmp 0x1403ffa5f
003FFDF5  48 8D 54 24 48                  lea rdx, [rsp + 0x48]
003FFDFA  48 8B CB                        mov rcx, rbx
003FFDFD  E8 9E 59 E7 FF                  call 0x1402757a0
003FFE02  40 84 ED                        test bpl, bpl
003FFE05  0F 84 A5 C2 2E 00               je 0x1406ec0b0
003FFE0B  FF 43 14                        inc dword ptr [rbx + 0x14]
003FFE0E  E9 A0 C2 2E 00                  jmp 0x1406ec0b3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall AlpcpQueueIoCompletionPort(__int64 a1, unsigned __int8 a2, __int64 a3, int a4, unsigned int a5)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned int v_stack_m58;
    unsigned int v_stack_m60;
    unsigned __int8 v_stack_m68;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p30;
    unsigned int v_stack_p8;

    v_stack_p10 = v_rbx;
    v_stack_p18 = v_rbp;
    v_stack_p20 = v_rsi;
    v_rsp = (v_rsp) - (96);
    result = 0;
    v_stack_m40 = v_xmm0;
    v_stack_m38 = *(unsigned __int64 *)(a1 + 48);
    v_stack_m40 = 0;
    v_stack_m30 = 0;
    if ((*(unsigned int *)(v_rip + 12350808)) != 0) goto loc_003FFA2A;
loc_003FF7CE:
    v_stack_m30 = (unsigned __int8)(v_cr8);
    if (((*(unsigned __int8 *)(v_rip + 12350257)) & (33)) != 0) goto loc_003FFA0A;
loc_003FF7E0:
    if (v_stack_m40 != 0) goto loc_003FFA3B;
loc_003FF7F1:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 48) + 12)))) >= (*(unsigned int *)(*(unsigned __int64 *)(a1 + 48) + 8))) goto loc_003FFA4A;
    result = 2;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48) + 32) != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48) + 32));
        *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48) + 32) = result;
    }
    v_stack_m50 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48) + 32) + 8);
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 48) + 12) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 48) + 12)) + 1);
    if (((*(unsigned __int8 *)(v_rip + 12350179)) & (1)) != 0) goto loc_003FF87A;
loc_003FF825:
    v_rdi = 0;
    if (v_stack_m40 != 0) goto loc_003FF859;
    if (v_stack_m40 == v_stack_m40) goto loc_003FF898;
    result = KxWaitForLockChainValid(v_stack_m40, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 48) + 12)), a3, a4);
loc_003FF859:
    v_stack_m40 = 0;
    result = (unsigned __int8)((v_stack_m38) ^ ((unsigned __int8)(v_stack_m38)));
    if ((((unsigned __int8)(result)) & (4)) == 0) goto loc_003FF898;
    result = KeWakeAddressAll(result + 8, v_stack_m38, a3, a4);
    goto loc_003FF898;
loc_003FF87A:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11593176))) != 0) goto loc_003FF825;
    result = KiReleaseQueuedSpinLockInstrumented(v_stack_m40, v_stack_p0, a3, a4);
    v_rdi = 0;
loc_003FF898:
    if ((*(unsigned int *)(v_rip + 12350593)) != 0) {
        a1 = 2;
        a2 = (unsigned __int8)(v_stack_m30);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, a3, a4);
    }
    if ((unsigned __int8)((unsigned __int8)(a3)) == 0) goto loc_003FF8DB;
    if ((unsigned __int8)((unsigned __int8)(a3)) != 0) goto loc_003FFD8B;
loc_003FF8CF:
    result = KeAbPostRelease(a1 + 352, a2, a3, a4);
loc_003FF8DB:
    v_rbp = (unsigned __int8)(-(a2));
    v_rbp = 0;
    result = ((unsigned __int8)((unsigned __int8)(a4)) != 0) ? 1 : 0;
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(result))) | (4));
    if ((unsigned int)((unsigned int)(a5)) == 0) { v_rsi = (unsigned int)(result); }
    v_stack_p8 = (unsigned int)(v_rsi);
    if (v_stack_m50 == 0) goto loc_003FFBC8;
loc_003FF90F:
    *(unsigned __int64 *)(v_stack_m50 + 24) = *(unsigned __int64 *)(a1 + 40);
    *(unsigned __int64 *)(v_stack_m50 + 32) = v_stack_m30;
    *(unsigned int *)(v_stack_m50 + 40) = 0;
    *(unsigned __int64 *)(v_stack_m50 + 48) = 0;
    v_stack_m48 = v_stack_m30;
    if ((*(unsigned int *)(v_rip + 12350437)) != 0) goto loc_003FFCE1;
loc_003FF941:
    v_stack_m50 = *(unsigned __int64 *)(gs_base + (0 + 32));
    if ((*(unsigned int *)(v_rip + 12350437)) < 0) goto loc_003FFD27;
loc_003FF963:
    result = (unsigned __int8)(~(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 32) + 1)));
    result = (unsigned int)((result) >> (1));
    result = (unsigned int)((result) & (1));
    v_stack_m58 = (unsigned int)(result);
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 1616);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 1616) == 0) { result = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8); }
    if ((unsigned int)(v_rsi) == 0) goto loc_003FF99C;
    if (condition_is_below) goto loc_003FFD68;
loc_003FF99C:
    v_rdi = 0;
loc_003FF99F:
    result = KiAcquireKobjectLockSafe(*(unsigned __int64 *)(a1 + 32), a2, a3, a4);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 8)) == (*(unsigned __int64 *)(a1 + 32) + 8)) goto loc_003FFC23;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 32) + 40)))) >= (*(unsigned int *)(*(unsigned __int64 *)(a1 + 32) + 44))) goto loc_003FFC1A;
loc_003FF9BF:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 232)) == (*(unsigned __int64 *)(a1 + 32))) goto loc_003FFD56;
loc_003FF9CF:
    a2 = 0;
loc_003FF9E0:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 8) + 16)) != 3) goto loc_003FFB95;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 8)) + 8)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 8))) goto loc_003FFA03;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 8) + 8))) == (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 8))) goto loc_003FFBE2;
loc_003FFA03:
loc_003FFA0A:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11592776))) != 0) goto loc_003FF7E0;
    result = KiAcquireQueuedSpinLockInstrumented(v_stack_m40, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8), a3, a4);
    goto loc_003FF7F1;
loc_003FFA2A:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 8)), (unsigned __int8)(result), a3, a4);
    goto loc_003FF7CE;
loc_003FFA3B:
    result = KxWaitForLockOwnerShip(v_stack_m40, (unsigned __int8)(result), a3, a4);
    goto loc_003FF7F1;
loc_003FFA4A:
    result = KeReleaseInStackQueuedSpinLock(v_stack_m40, (unsigned __int8)(result), a3, a4);
    if ((unsigned __int8)(v_stack_m50) != 0) goto loc_003FFDE5;
loc_003FFA5D:
    a1 = 0;
loc_003FFA5F:
    result = (unsigned __int8)(-((unsigned __int8)(*(unsigned __int64 *)(gs_base + (0 + 32)))));
    v_stack_m60 = (unsigned int)(*(unsigned __int64 *)(a1 + 32) + 8);
    v_stack_m68 = 0;
    a4 = 0;
    result = AlpcpQueueIoCompletion(*(unsigned __int64 *)(a1 + 32), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 8)) + 40), a3, a4);
    if ((unsigned int)(result) == 0) goto loc_003FFDF5;
    if ((unsigned __int8)((unsigned __int8)(a3)) == 0) goto loc_003FFCA6;
    v_rdi = 0;
    result = 17;
    if (!(condition_is_equal)) {
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 8)) + 352;
        result = ExfReleasePushLockShared(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 8)) + 40), a3, a4);
    }
    result = KeAbPostRelease(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 8)) + 352, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 8)) + 40), a3, a4);
    goto loc_003FFCA6;
loc_003FFAC0:
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 388))) != 5) goto loc_003FFBB8;
    result = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 112)))) & (7));
    if (((unsigned int)(result)) != 1) goto loc_003FFD9C;
loc_003FFAE1:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 232) == 0) goto loc_003FFAFE;
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 232))) & (127));
    if (((unsigned __int8)(result)) == 21) goto loc_003FFCC5;
loc_003FFAFE:
    result = KiRemovePrcbWaitEntry(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 232), a3, a4);
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 388))) == 1) goto loc_003FFD4D;
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 388))) != 5) goto loc_003FFB3F;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 388)))) - (*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 436)));
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 391)) == ((unsigned __int8)((unsigned __int8)(a3)))) goto loc_003FFBBC;
loc_003FFB3F:
    *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 388) = 7;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 216) = *(unsigned __int64 *)(v_stack_m50 + 11528);
    *(unsigned __int64 *)(v_stack_m50 + 11528) = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 216;
    a2 = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 200) = v_stack_m50;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 976) = 0;
loc_003FFB76:
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 64) = 0;
    result = (unsigned __int8)((*(unsigned __int8 *)(v_rdi + 17)) + 1);
    *(unsigned __int8 *)(v_rdi + 17) = (unsigned __int8)(result);
    if (1 != 0) goto loc_003FFCF1;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 8))) != (*(unsigned __int64 *)(a1 + 32) + 8)) goto loc_003FF9E0;
loc_003FFB95:
    goto loc_003FFC23;
loc_003FFBA6:
    if (((unsigned int)(result)) != 5) goto loc_003FFDD1;
    a1 = (unsigned __int8)((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 216) & (254));
    a1 = (unsigned __int8)((a1) | (6));
    *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 112) = (unsigned __int8)(a1);
loc_003FFBB8:
    a2 = 0;
    goto loc_003FFB76;
loc_003FFBBC:
    goto loc_003FFB3F;
loc_003FFBC8:
    a2 = 0;
    result = IopAllocateMiniCompletionPacket(1, a2, a3, a4);
    if (result != 0) goto loc_003FF90F;
    goto loc_003FFCA6;
loc_003FFBE2:
    *(unsigned __int64 *)(result) = (unsigned int)(v_stack_p8);
    v_r14 = 0;
    *(unsigned __int64 *)((unsigned int)(v_stack_p8) + 8) = result;
loc_003FFBF2:
    if (condition_is_above_or_equal) goto loc_003FFAC0;
loc_003FFBFF:
    v_rbp = (unsigned int)((0) + 1);
    if (((*(unsigned int *)(v_rip + 12342949)) & ((unsigned int)(v_rbp))) == 0) goto loc_003FFD00;
loc_003FFC0D:
loc_003FFC0F:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 24) + 64) == 0) goto loc_003FFBF2;
    goto loc_003FFBFF;
loc_003FFC1A:
    if (0 != 0) goto loc_003FF9BF;
loc_003FFC23:
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 32) + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 32) + 4)) + 1);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 24 + 8))) != (*(unsigned __int64 *)(a1 + 32) + 24)) goto loc_003FFA03;
    *(unsigned __int64 *)(result) = *(unsigned __int64 *)(a1 + 32) + 24;
    *(unsigned __int64 *)(result + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 24 + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 24 + 8)) = result;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 24 + 8) = result;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 32) + 4))) != 0) goto loc_003FFC62;
    result = *(unsigned __int64 *)(a1 + 32) + 24;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 8)) != (*(unsigned __int64 *)(a1 + 32) + 8)) {
        a2 = *(unsigned __int64 *)(a1 + 32);
        a1 = v_rbp;
        result = KiWakeOtherQueueWaiters(a1, a2, a3, a4);
    }
    a2 = 0;
loc_003FFC64:
    if ((((unsigned __int8)((unsigned int)(v_stack_p8))) & (1)) != 0) goto loc_003FFD43;
    if ((((unsigned __int8)((unsigned int)(v_stack_p8))) & (4)) != 0) goto loc_003FFD70;
loc_003FFC83:
loc_003FFC88:
    v_stack_m68 = (unsigned __int8)(v_stack_m48);
    result = KiExitDispatcher(v_stack_m50, 0, 1, (unsigned int)(v_stack_m58));
loc_003FFCA6:
    return result;
loc_003FFCC5:
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 540) = (unsigned int)((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 540))));
    goto loc_003FFAFE;
loc_003FFCE1:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 540)))), (unsigned __int8)(v_stack_m50), 1, (unsigned int)(v_stack_m58));
    goto loc_003FF941;
loc_003FFCF1:
    *(unsigned __int64 *)(result) = (unsigned __int8)(v_stack_m50);
    goto loc_003FFC64;
loc_003FFD00:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12348850)))) & (64)) == 0) goto loc_003FFC0D;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned __int8)((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 540)))), (unsigned __int8)(v_stack_m50), 1, (unsigned int)(v_stack_m58));
    if ((unsigned __int8)(result) == 0) goto loc_003FFC0D;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 64))), (unsigned __int8)(v_stack_m50), 1, (unsigned int)(v_stack_m58));
    goto loc_003FFC0F;
loc_003FFD27:
    result = KeIsThreadRunning(*(unsigned __int64 *)(v_stack_m28 + 56), (unsigned __int8)(v_stack_m50), 1, (unsigned int)(v_stack_m58));
    result = EtwTraceEnqueueWork(*(unsigned __int64 *)(v_stack_m28 + 56), result, (unsigned __int8)(result), (unsigned int)(v_stack_m58));
    goto loc_003FF963;
loc_003FFD43:
    goto loc_003FFC83;
loc_003FFD4D:
    goto loc_003FFB3F;
loc_003FFD56:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 643)) != 15) goto loc_003FF9CF;
    goto loc_003FFC23;
loc_003FFD68:
    goto loc_003FF99F;
loc_003FFD70:
    result = KiCompleteDirectSwitchThread(v_stack_m28, *(unsigned __int64 *)(v_stack_m28 + 8), (unsigned __int8)(result), (unsigned int)(v_stack_m58));
    goto loc_003FFC88;
loc_003FFD8B:
    result = ExfReleasePushLockShared((unsigned int)(v_stack_p30) + 352, *(unsigned __int64 *)(v_stack_m28 + 8), (unsigned __int8)(result), (unsigned int)(v_stack_m58));
    goto loc_003FF8CF;
loc_003FFD9C:
    if (((unsigned int)(result)) == 4) goto loc_003FFAE1;
    if ((unsigned int)(result) != 0) goto loc_003FFBA6;
    a1 = (unsigned __int8)(((unsigned int)(v_stack_p30) + 352) & (250));
    a1 = (unsigned __int8)((a1) | (2));
    *(unsigned __int8 *)(v_stack_m28 + 112) = (unsigned __int8)(a1);
    a2 = 0;
    *(unsigned __int64 *)(v_stack_m28 + 200) = result;
    *(unsigned __int64 *)(v_stack_m28 + 976) = 0;
    *(unsigned __int8 *)(1 + 17) = 0;
    goto loc_003FFB76;
loc_003FFDD1:
    a2 = 0;
    if (((unsigned int)(result)) != 3) goto loc_003FFB76;
    *(unsigned __int8 *)(1 + 17) = 2;
    goto loc_003FFB76;
loc_003FFDE5:
    if (1 != 0) goto loc_003FFA5D;
    goto loc_003FFA5F;
loc_003FFDF5:
    result = KeAcquireInStackQueuedSpinLock(v_stack_m28, v_stack_m18, (unsigned __int8)(result), (unsigned int)(v_stack_m58));
}
```

## 5. (Beta) C Style

```c
int64_t AlpcpQueueIoCompletionPort(void *Arg1, uint8_t Arg2, int64_t Arg3, int32_t Arg4, uint32_t Arg5)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r14;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint32_t v_stack_m58;
    uint32_t v_stack_m60;
    uint8_t v_stack_m68;
    uint64_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint32_t v_stack_p30;
    uint32_t v_stack_p8;

    v_stack_p10 = local_rbx;
    v_stack_p18 = local_rbp;
    v_stack_p20 = local_rsi;
    local_rsp = (local_rsp) - (96);
    result = 0;
    v_stack_m40 = v_xmm0;
    v_stack_m38 = *(uint64_t *)(arg1 + 0x30);
    v_stack_m40 = 0;
    v_stack_m30 = 0;
    if ((*(uint32_t *)(v_rip + 0xBC7558)) != 0) goto loc_003FFA2A;
loc_003FF7CE:
    v_stack_m30 = (uint8_t)(v_cr8);
    if (((*(uint8_t *)(v_rip + 0xBC7331)) & (33)) != 0) goto loc_003FFA0A;
loc_003FF7E0:
    if (v_stack_m40 != 0) goto loc_003FFA3B;
loc_003FF7F1:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x30) + 0xC)))) >= (*(uint32_t *)(*(uint64_t *)(arg1 + 0x30) + 0x8))) goto loc_003FFA4A;
    result = 2;
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x30) + 0x20) != 0) {
        result = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x30) + 0x20));
        *(uint64_t *)(*(uint64_t *)(arg1 + 0x30) + 0x20) = result;
    }
    v_stack_m50 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x30) + 0x20) + 0x8);
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x30) + 0xC) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x30) + 0xC)) + 1);
    if (((*(uint8_t *)(v_rip + 0xBC72E3)) & (1)) != 0) goto loc_003FF87A;
loc_003FF825:
    local_rdi = 0;
    if (v_stack_m40 != 0) goto loc_003FF859;
    if (v_stack_m40 == v_stack_m40) goto loc_003FF898;
    result = KxWaitForLockChainValid(v_stack_m40, (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x30) + 0xC)), Arg3, Arg4);
loc_003FF859:
    v_stack_m40 = 0;
    result = (uint8_t)((v_stack_m38) ^ ((uint8_t)(v_stack_m38)));
    if ((((uint8_t)(result)) & (4)) == 0) goto loc_003FF898;
    result = KeWakeAddressAll(result + 8, v_stack_m38, Arg3, Arg4);
    goto loc_003FF898;
loc_003FF87A:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB0E5D8))) != 0) goto loc_003FF825;
    result = KiReleaseQueuedSpinLockInstrumented(v_stack_m40, v_stack_p0, Arg3, Arg4);
    local_rdi = 0;
loc_003FF898:
    if ((*(uint32_t *)(v_rip + 0xBC7481)) != 0) {
        Arg1 = 2;
        Arg2 = (uint8_t)(v_stack_m30);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, Arg3, Arg4);
    }
    if ((uint8_t)((uint8_t)(Arg3)) == 0) goto loc_003FF8DB;
    if ((uint8_t)((uint8_t)(Arg3)) != 0) goto loc_003FFD8B;
loc_003FF8CF:
    result = KeAbPostRelease(Arg1 + 352, Arg2, Arg3, Arg4);
loc_003FF8DB:
    local_rbp = (uint8_t)(-(Arg2));
    local_rbp = 0;
    result = ((uint8_t)((uint8_t)(Arg4)) != 0) ? 1 : 0;
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(result))) | (4));
    if ((uint32_t)((uint32_t)(Arg5)) == 0) { local_rsi = (uint32_t)(result); }
    v_stack_p8 = (uint32_t)(local_rsi);
    if (v_stack_m50 == 0) goto loc_003FFBC8;
loc_003FF90F:
    *(uint64_t *)(v_stack_m50 + 0x18) = *(uint64_t *)(arg1 + 0x28);
    *(uint64_t *)(v_stack_m50 + 0x20) = v_stack_m30;
    *(uint32_t *)(v_stack_m50 + 0x28) = 0;
    *(uint64_t *)(v_stack_m50 + 0x30) = 0;
    v_stack_m48 = v_stack_m30;
    if ((*(uint32_t *)(v_rip + 0xBC73E5)) != 0) goto loc_003FFCE1;
loc_003FF941:
    v_stack_m50 = *(uint64_t *)(gs_base + (0 + 0x20));
    if ((*(uint32_t *)(v_rip + 0xBC73E5)) < 0) goto loc_003FFD27;
loc_003FF963:
    result = (uint8_t)(~(*(uint8_t *)(*(uint64_t *)(arg1 + 0x20) + 0x1)));
    result = (uint32_t)((result) >> (1));
    result = (uint32_t)((result) & (1));
    v_stack_m58 = (uint32_t)(result);
    result = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0x650);
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0x650) == 0) { result = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8); }
    if ((uint32_t)(local_rsi) == 0) goto loc_003FF99C;
    if (condition_is_below) goto loc_003FFD68;
loc_003FF99C:
    local_rdi = 0;
loc_003FF99F:
    result = KiAcquireKobjectLockSafe(*(uint64_t *)(arg1 + 0x20), Arg2, Arg3, Arg4);
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x8)) == (*(uint64_t *)(arg1 + 0x20) + 8)) goto loc_003FFC23;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x20) + 0x28)))) >= (*(uint32_t *)(*(uint64_t *)(arg1 + 0x20) + 0x2C))) goto loc_003FFC1A;
loc_003FF9BF:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0xE8)) == (*(uint64_t *)(arg1 + 0x20))) goto loc_003FFD56;
loc_003FF9CF:
    Arg2 = 0;
loc_003FF9E0:
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x8) + 0x10)) != 3) goto loc_003FFB95;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x8)) + 0x8)) != (*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x8))) goto loc_003FFA03;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x8) + 0x8))) == (*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x8))) goto loc_003FFBE2;
loc_003FFA03:
loc_003FFA0A:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB0E448))) != 0) goto loc_003FF7E0;
    result = KiAcquireQueuedSpinLockInstrumented(v_stack_m40, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8), Arg3, Arg4);
    goto loc_003FF7F1;
loc_003FFA2A:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x8)), (uint8_t)(result), Arg3, Arg4);
    goto loc_003FF7CE;
loc_003FFA3B:
    result = KxWaitForLockOwnerShip(v_stack_m40, (uint8_t)(result), Arg3, Arg4);
    goto loc_003FF7F1;
loc_003FFA4A:
    result = KeReleaseInStackQueuedSpinLock(v_stack_m40, (uint8_t)(result), Arg3, Arg4);
    if ((uint8_t)(v_stack_m50) != 0) goto loc_003FFDE5;
loc_003FFA5D:
    Arg1 = 0;
loc_003FFA5F:
    result = (uint8_t)(-((uint8_t)(*(uint64_t *)(gs_base + (0 + 0x20)))));
    v_stack_m60 = (uint32_t)(*(uint64_t *)(arg1 + 0x20) + 8);
    v_stack_m68 = 0;
    Arg4 = 0;
    result = AlpcpQueueIoCompletion(*(uint64_t *)(arg1 + 0x20), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x8)) + 0x28), Arg3, Arg4);
    if ((uint32_t)(result) == 0) goto loc_003FFDF5;
    if ((uint8_t)((uint8_t)(Arg3)) == 0) goto loc_003FFCA6;
    local_rdi = 0;
    result = 17;
    if (!(condition_is_equal)) {
        Arg1 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x8)) + 352;
        result = ExfReleasePushLockShared(Arg1, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x8)) + 0x28), Arg3, Arg4);
    }
    result = KeAbPostRelease(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x8)) + 352, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x8)) + 0x28), Arg3, Arg4);
    goto loc_003FFCA6;
loc_003FFAC0:
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0x184))) != 5) goto loc_003FFBB8;
    result = (uint32_t)(((uint32_t)((uint32_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0x70)))) & (7));
    if (((uint32_t)(result)) != 1) goto loc_003FFD9C;
loc_003FFAE1:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0xE8) == 0) goto loc_003FFAFE;
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0xE8))) & (127));
    if (((uint8_t)(result)) == 21) goto loc_003FFCC5;
loc_003FFAFE:
    result = KiRemovePrcbWaitEntry(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0xE8), Arg3, Arg4);
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0x184))) == 1) goto loc_003FFD4D;
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0x184))) != 5) goto loc_003FFB3F;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0x184)))) - (*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0x1B4)));
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0x187)) == ((uint8_t)((uint8_t)(Arg3)))) goto loc_003FFBBC;
loc_003FFB3F:
    *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0x184) = 7;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0xD8) = *(uint64_t *)(v_stack_m50 + 0x2D08);
    *(uint64_t *)(v_stack_m50 + 0x2D08) = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 216;
    Arg2 = 0;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0xC8) = v_stack_m50;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0x3D0) = 0;
loc_003FFB76:
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0x40) = 0;
    result = (uint8_t)((*(uint8_t *)(local_rdi + 0x11)) + 1);
    *(uint8_t *)(local_rdi + 0x11) = (uint8_t)(result);
    if (1 != 0) goto loc_003FFCF1;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x8))) != (*(uint64_t *)(arg1 + 0x20) + 8)) goto loc_003FF9E0;
loc_003FFB95:
    goto loc_003FFC23;
loc_003FFBA6:
    if (((uint32_t)(result)) != 5) goto loc_003FFDD1;
    Arg1 = (uint8_t)((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 216) & (254));
    Arg1 = (uint8_t)((Arg1) | (6));
    *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0x70) = (uint8_t)(Arg1);
loc_003FFBB8:
    Arg2 = 0;
    goto loc_003FFB76;
loc_003FFBBC:
    goto loc_003FFB3F;
loc_003FFBC8:
    Arg2 = 0;
    result = IopAllocateMiniCompletionPacket(1, Arg2, Arg3, Arg4);
    if (result != 0) goto loc_003FF90F;
    goto loc_003FFCA6;
loc_003FFBE2:
    *(uint64_t *)(result) = (uint32_t)(v_stack_p8);
    local_r14 = 0;
    *(uint64_t *)((uint32_t)(v_stack_p8) + 0x8) = result;
loc_003FFBF2:
    if (condition_is_above_or_equal) goto loc_003FFAC0;
loc_003FFBFF:
    local_rbp = (uint32_t)((0) + 1);
    if (((*(uint32_t *)(v_rip + 0xBC56A5)) & ((uint32_t)(local_rbp))) == 0) goto loc_003FFD00;
loc_003FFC0D:
loc_003FFC0F:
    if (*(uint64_t *)(*(uint64_t *)(local_rdi + 0x18) + 0x40) == 0) goto loc_003FFBF2;
    goto loc_003FFBFF;
loc_003FFC1A:
    if (0 != 0) goto loc_003FF9BF;
loc_003FFC23:
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x20) + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x20) + 0x4)) + 1);
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x18 + 0x8))) != (*(uint64_t *)(arg1 + 0x20) + 24)) goto loc_003FFA03;
    *(uint64_t *)(result) = *(uint64_t *)(arg1 + 0x20) + 24;
    *(uint64_t *)(result + 0x8) = *(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x18 + 0x8);
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x18 + 0x8)) = result;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x18 + 0x8) = result;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x20) + 0x4))) != 0) goto loc_003FFC62;
    result = *(uint64_t *)(arg1 + 0x20) + 24;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x8)) != (*(uint64_t *)(arg1 + 0x20) + 8)) {
        Arg2 = *(uint64_t *)(arg1 + 0x20);
        Arg1 = local_rbp;
        result = KiWakeOtherQueueWaiters(Arg1, Arg2, Arg3, Arg4);
    }
    Arg2 = 0;
loc_003FFC64:
    if ((((uint8_t)((uint32_t)(v_stack_p8))) & (1)) != 0) goto loc_003FFD43;
    if ((((uint8_t)((uint32_t)(v_stack_p8))) & (4)) != 0) goto loc_003FFD70;
loc_003FFC83:
loc_003FFC88:
    v_stack_m68 = (uint8_t)(v_stack_m48);
    result = KiExitDispatcher(v_stack_m50, 0, 1, (uint32_t)(v_stack_m58));
loc_003FFCA6:
    return result;
loc_003FFCC5:
    *(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x21C) = (uint32_t)((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x21C))));
    goto loc_003FFAFE;
loc_003FFCE1:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x21C)))), (uint8_t)(v_stack_m50), 1, (uint32_t)(v_stack_m58));
    goto loc_003FF941;
loc_003FFCF1:
    *(uint64_t *)(result) = (uint8_t)(v_stack_m50);
    goto loc_003FFC64;
loc_003FFD00:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBC6DB2)))) & (64)) == 0) goto loc_003FFC0D;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint8_t)((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x21C)))), (uint8_t)(v_stack_m50), 1, (uint32_t)(v_stack_m58));
    if ((uint8_t)(result) == 0) goto loc_003FFC0D;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x40))), (uint8_t)(v_stack_m50), 1, (uint32_t)(v_stack_m58));
    goto loc_003FFC0F;
loc_003FFD27:
    result = KeIsThreadRunning(*(uint64_t *)(v_stack_m28 + 0x38), (uint8_t)(v_stack_m50), 1, (uint32_t)(v_stack_m58));
    result = EtwTraceEnqueueWork(*(uint64_t *)(v_stack_m28 + 0x38), result, (uint8_t)(result), (uint32_t)(v_stack_m58));
    goto loc_003FF963;
loc_003FFD43:
    goto loc_003FFC83;
loc_003FFD4D:
    goto loc_003FFB3F;
loc_003FFD56:
    if ((*(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x283)) != 15) goto loc_003FF9CF;
    goto loc_003FFC23;
loc_003FFD68:
    goto loc_003FF99F;
loc_003FFD70:
    result = KiCompleteDirectSwitchThread(v_stack_m28, *(uint64_t *)(v_stack_m28 + 0x8), (uint8_t)(result), (uint32_t)(v_stack_m58));
    goto loc_003FFC88;
loc_003FFD8B:
    result = ExfReleasePushLockShared((uint32_t)(v_stack_p30) + 352, *(uint64_t *)(v_stack_m28 + 0x8), (uint8_t)(result), (uint32_t)(v_stack_m58));
    goto loc_003FF8CF;
loc_003FFD9C:
    if (((uint32_t)(result)) == 4) goto loc_003FFAE1;
    if ((uint32_t)(result) != 0) goto loc_003FFBA6;
    Arg1 = (uint8_t)(((uint32_t)(v_stack_p30) + 352) & (250));
    Arg1 = (uint8_t)((Arg1) | (2));
    *(uint8_t *)(v_stack_m28 + 0x70) = (uint8_t)(Arg1);
    Arg2 = 0;
    *(uint64_t *)(v_stack_m28 + 0xC8) = result;
    *(uint64_t *)(v_stack_m28 + 0x3D0) = 0;
    *(uint8_t *)(1 + 0x11) = 0;
    goto loc_003FFB76;
loc_003FFDD1:
    Arg2 = 0;
    if (((uint32_t)(result)) != 3) goto loc_003FFB76;
    *(uint8_t *)(1 + 0x11) = 2;
    goto loc_003FFB76;
loc_003FFDE5:
    if (1 != 0) goto loc_003FFA5D;
    goto loc_003FFA5F;
loc_003FFDF5:
    result = KeAcquireInStackQueuedSpinLock(v_stack_m28, v_stack_m18, (uint8_t)(result), (uint32_t)(v_stack_m58));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x30` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003FF760&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
