# ExpAcquireResourceSharedLite

- RVA: `0x00212040`–`0x0021343F` (길이 `5,119` bytes)
- VA: `0x0000000140212040`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005DF5C`
- 디코드: `1,241`개 명령, `5,119/5,119` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **49**; 고유 호출 대상: **22**
- 직접 호출자로 확인된 함수: **7**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x00212119` → [ExpGetThreadResourceHint](ExpGetThreadResourceHint_function_002134C0.md) (function, `0x002134C0`)
- `0x002121E0` → [KxWaitForLockChainValid](KxWaitForLockChainValid_function_00217AA0.md) (function, `0x00217AA0`)
- `0x00212211` → [KeDisableInterrupts](KeDisableInterrupts_function_00217BE0.md) (function, `0x00217BE0`)
- `0x00212220` → [KiHaltOnAddressWakeEntireList](KiHaltOnAddressWakeEntireList_function_00217AF4.md) (function, `0x00217AF4`)
- `0x0021225C` → [KiReleaseQueuedSpinLockInstrumented](KiReleaseQueuedSpinLockInstrumented_function_002179F0.md) (function, `0x002179F0`)
- `0x00212276` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x00212316` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00212353` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00212467` → [KiAcquireQueuedSpinLockInstrumented](../27/KiAcquireQueuedSpinLockInstrumented_function_00275850.md) (function, `0x00275850`)
- `0x002124B5` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x002125B9` → [KxWaitForLockChainValid](KxWaitForLockChainValid_function_00217AA0.md) (function, `0x00217AA0`)
- `0x002125EA` → [KeDisableInterrupts](KeDisableInterrupts_function_00217BE0.md) (function, `0x00217BE0`)
- `0x002125F9` → [KiHaltOnAddressWakeEntireList](KiHaltOnAddressWakeEntireList_function_00217AF4.md) (function, `0x00217AF4`)
- `0x00212635` → [KiReleaseQueuedSpinLockInstrumented](KiReleaseQueuedSpinLockInstrumented_function_002179F0.md) (function, `0x002179F0`)
- `0x0021264F` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x002126F1` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0021272B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0021282A` → [ExpExpandResourceOwnerTable](../3D/ExpExpandResourceOwnerTable_function_003D489C.md) (function, `0x003D489C`)
- `0x00212895` → [KxWaitForLockChainValid](KxWaitForLockChainValid_function_00217AA0.md) (function, `0x00217AA0`)
- `0x002128B2` → [KeWakeAddressAll](KeWakeAddressAll_function_00217C20.md) (function, `0x00217C20`)
- `0x002128CB` → [KiReleaseQueuedSpinLockInstrumented](KiReleaseQueuedSpinLockInstrumented_function_002179F0.md) (function, `0x002179F0`)
- `0x002128E5` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0021296F` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x002129A6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00212AC8` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x00212B4E` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00212B85` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00212C11` → [KxWaitForLockOwnerShip](../25/KxWaitForLockOwnerShip_function_00257EB0.md) (function, `0x00257EB0`)
- `0x00212C57` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x00212C7F` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x00212D66` → [ExpApplyPriorityBoost](ExpApplyPriorityBoost_function_00213F10.md) (function, `0x00213F10`)
- `0x00212D78` → [ExpWaitForResource](ExpWaitForResource_function_002166F0.md) (function, `0x002166F0`)
- `0x00212EBF` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x00212ED8` → [IoBoostThreadIoPriority](IoBoostThreadIoPriority_function_00216110.md) (function, `0x00216110`)
- `0x00212EE6` → [PsBoostThreadOutstandingIoQoS](PsBoostThreadOutstandingIoQoS_function_00215C54.md) (function, `0x00215C54`)
- `0x00212F82` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00212FB8` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x002130B8` → [KiAcquireQueuedSpinLockInstrumented](../27/KiAcquireQueuedSpinLockInstrumented_function_00275850.md) (function, `0x00275850`)
- `0x00213155` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x002131AD` → [KxWaitForLockOwnerShip](../25/KxWaitForLockOwnerShip_function_00257EB0.md) (function, `0x00257EB0`)
- `0x002131C9` → [PsBoostThreadIoEx](../39/PsBoostThreadIoEx_function_00392C00.md) (function, `0x00392C00`)
- `0x0021320F` → [KiAbThreadInsertList](KiAbThreadInsertList_function_0021F0E0.md) (function, `0x0021F0E0`)
- `0x0021321B` → [KiAbQueueAutoBoostDpc](../20/KiAbQueueAutoBoostDpc_function_002074D0.md) (function, `0x002074D0`)
- `0x00213231` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0021324A` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x002132B9` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x00213352` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00213385` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x002133D3` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)

### Direct callers
- [ExAcquireResourceSharedLite](ExAcquireResourceSharedLite_function_00211BC0.md) at `0x00211BF1`
- [sub_00213507](Unknown_function_00213507.md) at `0x00213516`
- [SeSecurityAttributePresent](SeSecurityAttributePresent_function_00213660.md) at `0x002136BA`
- [ExEnterPriorityRegionAndAcquireResourceShared](ExEnterPriorityRegionAndAcquireResourceShared_function_00213870.md) at `0x002138E2`
- [sub_00213BE2](Unknown_function_00213BE2.md) at `0x00213BF5`
- [sub_00213BE2](Unknown_function_00213BE2.md) at `0x00213C2E`
- [sub_0025F532](../25/Unknown_function_0025F532.md) at `0x0025F5A5`
- [SepCanTokenMatchAllPackageSid](../2F/SepCanTokenMatchAllPackageSid_function_002FFE90.md) at `0x002FFF37`

### Static image references
- `0x00212098` → RVA `0x00FC6B04` (`ALMOSTRO`; read)
- `0x002120C7` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x002120D4` → RVA `0x00FC6B06` (`ALMOSTRO`; read)
- `0x002121A8` → RVA `0x00FC6B06` (`ALMOSTRO`; reference)
- `0x00212206` → RVA `0x00F21B20` (`.data`; read)
- `0x00212246` → RVA `0x00F0DE58` (`.data`; read)
- `0x002122FC` → RVA `0x00E68468` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **12**
  - `0x00212316` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x00212353` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x002126F1` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x0021272B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x0021296F` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x002129A6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x00212B4E` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x00212B85` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x00212F82` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x00212FB8` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x00213352` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x00213385` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00212040  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00212045  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
0021204A  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
0021204F  55                              push rbp
00212050  41 54                           push r12
00212052  41 55                           push r13
00212054  41 56                           push r14
00212056  41 57                           push r15
00212058  48 8D 6C 24 C9                  lea rbp, [rsp - 0x37]
0021205D  48 81 EC D0 00 00 00            sub rsp, 0xd0
00212064  33 C0                           xor eax, eax
00212066  48 8D 79 60                     lea rdi, [rcx + 0x60]
0021206A  0F 57 C9                        xorps xmm1, xmm1
0021206D  48 89 45 9F                     mov qword ptr [rbp - 0x61], rax
00212071  0F 11 4D B7                     movups xmmword ptr [rbp - 0x49], xmm1
00212075  48 89 45 E7                     mov qword ptr [rbp - 0x19], rax
00212079  44 0F B6 E2                     movzx r12d, dl
0021207D  0F 11 4D C7                     movups xmmword ptr [rbp - 0x39], xmm1
00212081  48 8B D9                        mov rbx, rcx
00212084  0F 11 4D D7                     movups xmmword ptr [rbp - 0x29], xmm1
00212088  0F 57 C0                        xorps xmm0, xmm0
0021208B  0F 11 45 8F                     movups xmmword ptr [rbp - 0x71], xmm0
0021208F  65 4C 8B 34 25 88 01 00 00      mov r14, qword ptr gs:[0x188]
00212098  44 8B 3D 65 4A DB 00            mov r15d, dword ptr [rip + 0xdb4a65]
0021209F  41 81 E7 00 00 02 00            and r15d, 0x20000
002120A6  65 FF 04 25 8C 90 00 00         inc dword ptr gs:[0x908c]
002120AE  45 33 ED                        xor r13d, r13d
002120B1  48 89 7D 97                     mov qword ptr [rbp - 0x69], rdi
002120B5  4C 89 6D 8F                     mov qword ptr [rbp - 0x71], r13
002120B9  90                              nop
002120BA  44 0F 20 C6                     mov rsi, cr8
002120BE  B8 02 00 00 00                  mov eax, 2
002120C3  44 0F 22 C0                     mov cr8, rax
002120C7  44 39 2D 52 4C DB 00            cmp dword ptr [rip + 0xdb4c52], r13d
002120CE  0F 85 DA 03 00 00               jne 0x1402124ae
002120D4  F6 05 2B 4A DB 00 21            test byte ptr [rip + 0xdb4a2b], 0x21
002120DB  40 88 75 9F                     mov byte ptr [rbp - 0x61], sil
002120DF  0F 85 6D 03 00 00               jne 0x140212452
002120E5  48 8D 55 8F                     lea rdx, [rbp - 0x71]
002120E9  48 87 17                        xchg qword ptr [rdi], rdx
002120EC  48 85 D2                        test rdx, rdx
002120EF  0F 85 18 0B 00 00               jne 0x140212c0d
002120F5  41 BB 01 00 00 00               mov r11d, 1
002120FB  8B 43 40                        mov eax, dword ptr [rbx + 0x40]
002120FE  85 C0                           test eax, eax
00212100  0F 84 85 00 00 00               je 0x14021218b
00212106  0F B6 43 1A                     movzx eax, byte ptr [rbx + 0x1a]
0021210A  84 C0                           test al, al
0021210C  0F 88 95 09 00 00               js 0x140212aa7
00212112  44 8B 4B 4C                     mov r9d, dword ptr [rbx + 0x4c]
00212116  49 8B CE                        mov rcx, r14
00212119  E8 A2 13 00 00                  call 0x1402134c0
0021211E  48 8D 53 30                     lea rdx, [rbx + 0x30]
00212122  44 8B C0                        mov r8d, eax
00212125  48 8B 02                        mov rax, qword ptr [rdx]
00212128  49 3B C6                        cmp rax, r14
0021212B  0F 84 68 09 00 00               je 0x140212a99
00212131  49 8B CD                        mov rcx, r13
00212134  4D 8B D5                        mov r10, r13
00212137  48 85 C0                        test rax, rax
0021213A  0F 84 A5 0A 00 00               je 0x140212be5
00212140  49 8B CB                        mov rcx, r11
00212143  45 85 C0                        test r8d, r8d
00212146  0F 85 33 03 00 00               jne 0x14021247f
0021214C  44 8B 43 48                     mov r8d, dword ptr [rbx + 0x48]
00212150  8B 43 40                        mov eax, dword ptr [rbx + 0x40]
00212153  48 8B 53 10                     mov rdx, qword ptr [rbx + 0x10]
00212157  4C 03 C0                        add r8, rax
0021215A  48 85 D2                        test rdx, rdx
0021215D  0F 85 5C 03 00 00               jne 0x1402124bf
00212163  49 8B C5                        mov rax, r13
00212166  4D 85 D2                        test r10, r10
00212169  75 15                           jne 0x140212180
0021216B  48 3B D0                        cmp rdx, rax
0021216E  0F 83 AF 06 00 00               jae 0x140212823
00212174  4C 8B D2                        mov r10, rdx
00212177  48 85 D2                        test rdx, rdx
0021217A  0F 84 A3 06 00 00               je 0x140212823
00212180  41 8B C2                        mov eax, r10d
00212183  49 8B D2                        mov rdx, r10
00212186  E9 A0 03 00 00                  jmp 0x14021252b
0021218B  FF C0                           inc eax
0021218D  66 44 89 5B 18                  mov word ptr [rbx + 0x18], r11w
00212192  89 43 40                        mov dword ptr [rbx + 0x40], eax
00212195  40 B6 01                        mov sil, 1
00212198  8B 43 38                        mov eax, dword ptr [rbx + 0x38]
0021219B  83 E0 07                        and eax, 7
0021219E  4C 89 73 30                     mov qword ptr [rbx + 0x30], r14
002121A2  83 C8 08                        or eax, 8
002121A5  89 43 38                        mov dword ptr [rbx + 0x38], eax
002121A8  40 84 35 57 49 DB 00            test byte ptr [rip + 0xdb4957], sil
002121AF  0F 85 91 00 00 00               jne 0x140212246
002121B5  0F 0D 4D 8F                     prefetchw byte ptr [rbp - 0x71]
002121B9  48 8B 45 8F                     mov rax, qword ptr [rbp - 0x71]
002121BD  48 85 C0                        test rax, rax
002121C0  75 23                           jne 0x1402121e5
002121C2  48 8B 4D 97                     mov rcx, qword ptr [rbp - 0x69]
002121C6  48 8D 45 8F                     lea rax, [rbp - 0x71]
002121CA  F0 4C 0F B1 29                  lock cmpxchg qword ptr [rcx], r13
002121CF  48 8D 4D 8F                     lea rcx, [rbp - 0x71]
002121D3  48 3B C1                        cmp rax, rcx
002121D6  0F 84 85 00 00 00               je 0x140212261
002121DC  48 8D 4D 8F                     lea rcx, [rbp - 0x71]
002121E0  E8 BB 58 00 00                  call 0x140217aa0
002121E5  4C 8D 40 08                     lea r8, [rax + 8]
002121E9  4C 89 6D 8F                     mov qword ptr [rbp - 0x71], r13
002121ED  48 8B 4D 97                     mov rcx, qword ptr [rbp - 0x69]
002121F1  48 8B C1                        mov rax, rcx
002121F4  49 87 00                        xchg qword ptr [r8], rax
002121F7  32 C1                           xor al, cl
002121F9  A8 04                           test al, 4
002121FB  74 64                           je 0x140212261
002121FD  F0 44 09 2C 24                  lock or dword ptr [rsp], r13d
00212202  49 C1 E8 05                     shr r8, 5
00212206  4C 8D 0D 13 F9 D0 00            lea r9, [rip + 0xd0f913]
0021220D  41 83 E0 7F                     and r8d, 0x7f
00212211  E8 CA 59 00 00                  call 0x140217be0
00212216  49 8B D5                        mov rdx, r13
00212219  0F B6 F8                        movzx edi, al
0021221C  4B 87 14 C1                     xchg qword ptr [r9 + r8*8], rdx
00212220  E8 CF 58 00 00                  call 0x140217af4
00212225  40 84 FF                        test dil, dil
00212228  74 37                           je 0x140212261
0021222A  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
00212233  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
0021223A  4D 85 C0                        test r8, r8
0021223D  0F 85 F6 09 00 00               jne 0x140212c39
00212243  FB                              sti
00212244  EB 1B                           jmp 0x140212261
00212246  8B 05 0C BC CF 00               mov eax, dword ptr [rip + 0xcfbc0c]
0021224C  85 C0                           test eax, eax
0021224E  0F 85 61 FF FF FF               jne 0x1402121b5
00212254  48 8B 55 5F                     mov rdx, qword ptr [rbp + 0x5f]
00212258  48 8D 4D 8F                     lea rcx, [rbp - 0x71]
0021225C  E8 8F 57 00 00                  call 0x1402179f0
00212261  44 39 2D B8 4A DB 00            cmp dword ptr [rip + 0xdb4ab8], r13d
00212268  0F B6 7D 9F                     movzx edi, byte ptr [rbp - 0x61]
0021226C  74 0D                           je 0x14021227b
0021226E  44 0F 20 C1                     mov rcx, cr8
00212272  40 0F B6 D7                     movzx edx, dil
00212276  E8 1D 34 2E 00                  call 0x1404f5698
0021227B  44 0F 22 C7                     mov cr8, rdi
0021227F  65 FF 04 25 94 90 00 00         inc dword ptr gs:[0x9094]
00212287  65 FF 04 25 64 90 00 00         inc dword ptr gs:[0x9064]
0021228F  45 85 FF                        test r15d, r15d
00212292  0F 84 94 01 00 00               je 0x14021242c
00212298  8B 43 44                        mov eax, dword ptr [rbx + 0x44]
0021229B  89 45 A7                        mov dword ptr [rbp - 0x59], eax
0021229E  44 89 6D 87                     mov dword ptr [rbp - 0x79], r13d
002122A2  0F 31                           rdtsc
002122A4  65 4C 8B 3C 25 20 00 00 00      mov r15, qword ptr gs:[0x20]
002122AD  48 C1 E2 20                     shl rdx, 0x20
002122B1  48 0B C2                        or rax, rdx
002122B4  44 88 6D 8A                     mov byte ptr [rbp - 0x76], r13b
002122B8  4C 8B E0                        mov r12, rax
002122BB  41 FF 87 70 8F 00 00            inc dword ptr [r15 + 0x8f70]
002122C2  41 0F B6 87 D0 00 00 00         movzx eax, byte ptr [r15 + 0xd0]
002122CA  65 4C 8B 34 25 88 01 00 00      mov r14, qword ptr gs:[0x188]
002122D3  66 89 45 87                     mov word ptr [rbp - 0x79], ax
002122D7  41 0F B6 87 D1 00 00 00         movzx eax, byte ptr [r15 + 0xd1]
002122DF  88 45 8B                        mov byte ptr [rbp - 0x75], al
002122E2  41 8B 8E A0 05 00 00            mov ecx, dword ptr [r14 + 0x5a0]
002122E9  88 45 89                        mov byte ptr [rbp - 0x77], al
002122EC  40 84 CE                        test sil, cl
002122EF  0F 85 37 01 00 00               jne 0x14021242c
002122F5  49 8B BE 20 06 00 00            mov rdi, qword ptr [r14 + 0x620]
002122FC  44 8B 2D 65 61 C5 00            mov r13d, dword ptr [rip + 0xc56165]
00212303  48 85 FF                        test rdi, rdi
00212306  75 50                           jne 0x140212358
00212308  BA 00 02 00 00                  mov edx, 0x200
0021230D  8D 4F 48                        lea ecx, [rdi + 0x48]
00212310  41 B8 52 65 54 72               mov r8d, 0x72546552
00212316  E8 D5 FD 96 00                  call 0x140b820f0
0021231B  4C 8B C0                        mov r8, rax
0021231E  48 85 C0                        test rax, rax
00212321  0F 84 05 01 00 00               je 0x14021242c
00212327  45 33 C9                        xor r9d, r9d
0021232A  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
0021232E  48 C7 40 1C 00 00 01 00         mov qword ptr [rax + 0x1c], 0x10000
00212336  44 89 68 28                     mov dword ptr [rax + 0x28], r13d
0021233A  33 C0                           xor eax, eax
0021233C  F0 4D 0F B1 86 20 06 00 00      lock cmpxchg qword ptr [r14 + 0x620], r8
00212345  48 8B F8                        mov rdi, rax
00212348  0F 84 80 00 00 00               je 0x1402123ce
0021234E  33 D2                           xor edx, edx
00212350  49 8B C8                        mov rcx, r8
00212353  E8 18 05 97 00                  call 0x140b82870
00212358  45 33 C9                        xor r9d, r9d
0021235B  41 8B C1                        mov eax, r9d
0021235E  41 8B D1                        mov edx, r9d
00212361  83 FA 08                        cmp edx, 8
00212364  73 35                           jae 0x14021239b
00212366  8B 4F 1C                        mov ecx, dword ptr [rdi + 0x1c]
00212369  81 F9 00 00 01 00               cmp ecx, 0x10000
0021236F  75 0C                           jne 0x14021237d
00212371  48 39 5F 10                     cmp qword ptr [rdi + 0x10], rbx
00212375  75 06                           jne 0x14021237d
00212377  44 39 6F 28                     cmp dword ptr [rdi + 0x28], r13d
0021237B  74 49                           je 0x1402123c6
0021237D  48 85 C0                        test rax, rax
00212380  0F 85 EE 00 00 00               jne 0x140212474
00212386  85 C9                           test ecx, ecx
00212388  0F 84 E3 00 00 00               je 0x140212471
0021238E  44 39 6F 28                     cmp dword ptr [rdi + 0x28], r13d
00212392  0F 8D DC 00 00 00               jge 0x140212474
00212398  48 8B C7                        mov rax, rdi
0021239B  48 8B F8                        mov rdi, rax
0021239E  48 85 C0                        test rax, rax
002123A1  74 23                           je 0x1402123c6
002123A3  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
002123A7  48 C7 40 1C 00 00 01 00         mov qword ptr [rax + 0x1c], 0x10000
002123AF  44 89 48 24                     mov dword ptr [rax + 0x24], r9d
002123B3  4C 89 08                        mov qword ptr [rax], r9
002123B6  4C 89 48 08                     mov qword ptr [rax + 8], r9
002123BA  44 89 48 18                     mov dword ptr [rax + 0x18], r9d
002123BE  44 89 68 28                     mov dword ptr [rax + 0x28], r13d
002123C2  44 89 48 2C                     mov dword ptr [rax + 0x2c], r9d
002123C6  4C 8B C7                        mov r8, rdi
002123C9  48 85 FF                        test rdi, rdi
002123CC  74 5E                           je 0x14021242c
002123CE  41 FF 87 74 8F 00 00            inc dword ptr [r15 + 0x8f74]
002123D5  41 8B 40 20                     mov eax, dword ptr [r8 + 0x20]
002123D9  4D 89 60 08                     mov qword ptr [r8 + 8], r12
002123DD  85 C0                           test eax, eax
002123DF  0F 84 5C 04 00 00               je 0x140212841
002123E5  83 F8 04                        cmp eax, 4
002123E8  0F 85 53 04 00 00               jne 0x140212841
002123EE  0F B7 45 87                     movzx eax, word ptr [rbp - 0x79]
002123F2  66 41 39 40 18                  cmp word ptr [r8 + 0x18], ax
002123F7  0F 85 37 04 00 00               jne 0x140212834
002123FD  0F B6 45 8B                     movzx eax, byte ptr [rbp - 0x75]
00212401  41 38 40 1A                     cmp byte ptr [r8 + 0x1a], al
00212405  0F 85 29 04 00 00               jne 0x140212834
0021240B  4D 2B 20                        sub r12, qword ptr [r8]
0021240E  4D 89 20                        mov qword ptr [r8], r12
00212411  B8 01 00 00 00                  mov eax, 1
00212416  8B 4D 87                        mov ecx, dword ptr [rbp - 0x79]
00212419  41 89 40 20                     mov dword ptr [r8 + 0x20], eax
0021241D  41 89 40 24                     mov dword ptr [r8 + 0x24], eax
00212421  8B 45 A7                        mov eax, dword ptr [rbp - 0x59]
00212424  41 89 40 2C                     mov dword ptr [r8 + 0x2c], eax
00212428  41 89 48 18                     mov dword ptr [r8 + 0x18], ecx
0021242C  4C 8D 9C 24 D0 00 00 00         lea r11, [rsp + 0xd0]
00212434  40 0F B6 C6                     movzx eax, sil
00212438  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
0021243C  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
00212440  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
00212444  49 8B E3                        mov rsp, r11
00212447  41 5F                           pop r15
00212449  41 5E                           pop r14
0021244B  41 5D                           pop r13
0021244D  41 5C                           pop r12
0021244F  5D                              pop rbp
00212450  C3                              ret
00212451  CC                              int3
00212452  8B 05 00 BA CF 00               mov eax, dword ptr [rip + 0xcfba00]
00212458  85 C0                           test eax, eax
0021245A  0F 85 85 FC FF FF               jne 0x1402120e5
00212460  48 8B D7                        mov rdx, rdi
00212463  48 8D 4D 8F                     lea rcx, [rbp - 0x71]
00212467  E8 E4 33 06 00                  call 0x140275850
0021246C  E9 84 FC FF FF                  jmp 0x1402120f5
00212471  48 8B C7                        mov rax, rdi
00212474  48 83 C7 40                     add rdi, 0x40
00212478  FF C2                           inc edx
0021247A  E9 E2 FE FF FF                  jmp 0x140212361
0021247F  48 8B 43 10                     mov rax, qword ptr [rbx + 0x10]
00212483  48 85 C0                        test rax, rax
00212486  0F 84 C0 FC FF FF               je 0x14021214c
0021248C  44 3B 40 08                     cmp r8d, dword ptr [rax + 8]
00212490  0F 83 B6 FC FF FF               jae 0x14021214c
00212496  49 8B D0                        mov rdx, r8
00212499  48 C1 E2 04                     shl rdx, 4
0021249D  48 03 D0                        add rdx, rax
002124A0  4C 39 32                        cmp qword ptr [rdx], r14
002124A3  0F 85 A3 FC FF FF               jne 0x14021214c
002124A9  E9 EB 05 00 00                  jmp 0x140212a99
002124AE  0F B6 D0                        movzx edx, al
002124B1  40 0F B6 CE                     movzx ecx, sil
002124B5  E8 42 32 2E 00                  call 0x1404f56fc
002124BA  E9 15 FC FF FF                  jmp 0x1402120d4
002124BF  8B 42 08                        mov eax, dword ptr [rdx + 8]
002124C2  48 C1 E0 04                     shl rax, 4
002124C6  48 03 C2                        add rax, rdx
002124C9  48 83 C2 10                     add rdx, 0x10
002124CD  49 3B C8                        cmp rcx, r8
002124D0  0F 83 90 FC FF FF               jae 0x140212166
002124D6  4C 8B 0A                        mov r9, qword ptr [rdx]
002124D9  4D 3B CE                        cmp r9, r14
002124DC  0F 84 9F 05 00 00               je 0x140212a81
002124E2  4D 85 C9                        test r9, r9
002124E5  0F 84 6F 05 00 00               je 0x140212a5a
002124EB  48 FF C1                        inc rcx
002124EE  49 3B C8                        cmp rcx, r8
002124F1  0F 84 FF 06 00 00               je 0x140212bf6
002124F7  48 83 C2 10                     add rdx, 0x10
002124FB  48 3B D0                        cmp rdx, rax
002124FE  75 D6                           jne 0x1402124d6
00212500  E9 61 FC FF FF                  jmp 0x140212166
00212505  48 8B 53 10                     mov rdx, qword ptr [rbx + 0x10]
00212509  48 85 D2                        test rdx, rdx
0021250C  0F 84 11 03 00 00               je 0x140212823
00212512  8B 42 08                        mov eax, dword ptr [rdx + 8]
00212515  48 C1 E0 04                     shl rax, 4
00212519  48 03 C2                        add rax, rdx
0021251C  48 83 C2 10                     add rdx, 0x10
00212520  4C 39 2A                        cmp qword ptr [rdx], r13
00212523  0F 85 ED 02 00 00               jne 0x140212816
00212529  8B C2                           mov eax, edx
0021252B  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00212534  2B 43 10                        sub eax, dword ptr [rbx + 0x10]
00212537  48 C1 F8 04                     sar rax, 4
0021253B  88 81 60 04 00 00               mov byte ptr [rcx + 0x460], al
00212541  4C 39 32                        cmp qword ptr [rdx], r14
00212544  0F 84 08 03 00 00               je 0x140212852
0021254A  8B 4B 40                        mov ecx, dword ptr [rbx + 0x40]
0021254D  85 C9                           test ecx, ecx
0021254F  74 16                           je 0x140212567
00212551  0F B6 43 1A                     movzx eax, byte ptr [rbx + 0x1a]
00212555  84 C0                           test al, al
00212557  0F 88 F4 0C 00 00               js 0x140213251
0021255D  44 39 6B 4C                     cmp dword ptr [rbx + 0x4c], r13d
00212561  0F 85 EA 0C 00 00               jne 0x140213251
00212567  66 44 89 5B 18                  mov word ptr [rbx + 0x18], r11w
0021256C  8D 41 01                        lea eax, [rcx + 1]
0021256F  89 43 40                        mov dword ptr [rbx + 0x40], eax
00212572  8B 42 08                        mov eax, dword ptr [rdx + 8]
00212575  83 E0 07                        and eax, 7
00212578  4C 89 32                        mov qword ptr [rdx], r14
0021257B  83 C8 08                        or eax, 8
0021257E  89 42 08                        mov dword ptr [rdx + 8], eax
00212581  F6 05 7E 45 DB 00 01            test byte ptr [rip + 0xdb457e], 1
00212588  0F 85 91 00 00 00               jne 0x14021261f
0021258E  0F 0D 4D 8F                     prefetchw byte ptr [rbp - 0x71]
00212592  48 8B 45 8F                     mov rax, qword ptr [rbp - 0x71]
00212596  48 85 C0                        test rax, rax
00212599  75 23                           jne 0x1402125be
0021259B  48 8B 4D 97                     mov rcx, qword ptr [rbp - 0x69]
0021259F  48 8D 45 8F                     lea rax, [rbp - 0x71]
002125A3  F0 4C 0F B1 29                  lock cmpxchg qword ptr [rcx], r13
002125A8  48 8D 4D 8F                     lea rcx, [rbp - 0x71]
002125AC  48 3B C1                        cmp rax, rcx
002125AF  0F 84 85 00 00 00               je 0x14021263a
002125B5  48 8D 4D 8F                     lea rcx, [rbp - 0x71]
002125B9  E8 E2 54 00 00                  call 0x140217aa0
002125BE  4C 8D 40 08                     lea r8, [rax + 8]
002125C2  4C 89 6D 8F                     mov qword ptr [rbp - 0x71], r13
002125C6  48 8B 4D 97                     mov rcx, qword ptr [rbp - 0x69]
002125CA  48 8B C1                        mov rax, rcx
002125CD  49 87 00                        xchg qword ptr [r8], rax
002125D0  32 C1                           xor al, cl
002125D2  A8 04                           test al, 4
002125D4  74 64                           je 0x14021263a
002125D6  F0 44 09 2C 24                  lock or dword ptr [rsp], r13d
002125DB  49 C1 E8 05                     shr r8, 5
002125DF  4C 8D 0D 3A F5 D0 00            lea r9, [rip + 0xd0f53a]
002125E6  41 83 E0 7F                     and r8d, 0x7f
002125EA  E8 F1 55 00 00                  call 0x140217be0
002125EF  49 8B D5                        mov rdx, r13
002125F2  0F B6 F8                        movzx edi, al
002125F5  4B 87 14 C1                     xchg qword ptr [r9 + r8*8], rdx
002125F9  E8 F6 54 00 00                  call 0x140217af4
002125FE  40 84 FF                        test dil, dil
00212601  74 37                           je 0x14021263a
00212603  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
0021260C  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
00212613  4D 85 C0                        test r8, r8
00212616  0F 85 45 06 00 00               jne 0x140212c61
0021261C  FB                              sti
0021261D  EB 1B                           jmp 0x14021263a
0021261F  8B 05 33 B8 CF 00               mov eax, dword ptr [rip + 0xcfb833]
00212625  85 C0                           test eax, eax
00212627  0F 85 61 FF FF FF               jne 0x14021258e
0021262D  48 8B 55 5F                     mov rdx, qword ptr [rbp + 0x5f]
00212631  48 8D 4D 8F                     lea rcx, [rbp - 0x71]
00212635  E8 B6 53 00 00                  call 0x1402179f0
0021263A  44 39 2D DF 46 DB 00            cmp dword ptr [rip + 0xdb46df], r13d
00212641  0F B6 7D 9F                     movzx edi, byte ptr [rbp - 0x61]
00212645  74 0D                           je 0x140212654
00212647  44 0F 20 C1                     mov rcx, cr8
0021264B  40 0F B6 D7                     movzx edx, dil
0021264F  E8 44 30 2E 00                  call 0x1404f5698
00212654  44 0F 22 C7                     mov cr8, rdi
00212658  65 FF 04 25 94 90 00 00         inc dword ptr gs:[0x9094]
00212660  65 FF 04 25 64 90 00 00         inc dword ptr gs:[0x9064]
00212668  45 85 FF                        test r15d, r15d
0021266B  0F 84 8F 01 00 00               je 0x140212800
00212671  8B 43 44                        mov eax, dword ptr [rbx + 0x44]
00212674  89 45 A7                        mov dword ptr [rbp - 0x59], eax
00212677  44 89 6D 87                     mov dword ptr [rbp - 0x79], r13d
0021267B  0F 31                           rdtsc
0021267D  65 48 8B 34 25 20 00 00 00      mov rsi, qword ptr gs:[0x20]
00212686  48 C1 E2 20                     shl rdx, 0x20
0021268A  48 0B C2                        or rax, rdx
0021268D  C6 45 8A 00                     mov byte ptr [rbp - 0x76], 0
00212691  4C 8B C0                        mov r8, rax
00212694  48 89 45 AF                     mov qword ptr [rbp - 0x51], rax
00212698  FF 86 70 8F 00 00               inc dword ptr [rsi + 0x8f70]
0021269E  65 4C 8B 34 25 88 01 00 00      mov r14, qword ptr gs:[0x188]
002126A7  44 0F B6 AE D0 00 00 00         movzx r13d, byte ptr [rsi + 0xd0]
002126AF  44 0F B6 A6 D1 00 00 00         movzx r12d, byte ptr [rsi + 0xd1]
002126B7  66 44 89 6D 87                  mov word ptr [rbp - 0x79], r13w
002126BC  41 8B 8E A0 05 00 00            mov ecx, dword ptr [r14 + 0x5a0]
002126C3  44 88 65 89                     mov byte ptr [rbp - 0x77], r12b
002126C7  F6 C1 01                        test cl, 1
002126CA  0F 85 30 01 00 00               jne 0x140212800
002126D0  49 8B BE 20 06 00 00            mov rdi, qword ptr [r14 + 0x620]
002126D7  44 8B 3D 8A 5D C5 00            mov r15d, dword ptr [rip + 0xc55d8a]
002126DE  48 85 FF                        test rdi, rdi
002126E1  75 51                           jne 0x140212734
002126E3  BA 00 02 00 00                  mov edx, 0x200
002126E8  8D 4F 48                        lea ecx, [rdi + 0x48]
002126EB  41 B8 52 65 54 72               mov r8d, 0x72546552
002126F1  E8 FA F9 96 00                  call 0x140b820f0
002126F6  48 8B C8                        mov rcx, rax
002126F9  48 85 C0                        test rax, rax
002126FC  0F 84 FE 00 00 00               je 0x140212800
00212702  45 33 C9                        xor r9d, r9d
00212705  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00212709  48 C7 40 1C 00 00 01 00         mov qword ptr [rax + 0x1c], 0x10000
00212711  44 89 78 28                     mov dword ptr [rax + 0x28], r15d
00212715  33 C0                           xor eax, eax
00212717  F0 49 0F B1 8E 20 06 00 00      lock cmpxchg qword ptr [r14 + 0x620], rcx
00212720  48 8B F8                        mov rdi, rax
00212723  0F 84 20 01 00 00               je 0x140212849
00212729  33 D2                           xor edx, edx
0021272B  E8 40 01 97 00                  call 0x140b82870
00212730  4C 8B 45 AF                     mov r8, qword ptr [rbp - 0x51]
00212734  45 33 C9                        xor r9d, r9d
00212737  41 8B C1                        mov eax, r9d
0021273A  41 8B C9                        mov ecx, r9d
0021273D  83 F9 08                        cmp ecx, 8
00212740  73 35                           jae 0x140212777
00212742  8B 57 1C                        mov edx, dword ptr [rdi + 0x1c]
00212745  81 FA 00 00 01 00               cmp edx, 0x10000
0021274B  75 0C                           jne 0x140212759
0021274D  48 39 5F 10                     cmp qword ptr [rdi + 0x10], rbx
00212751  75 06                           jne 0x140212759
00212753  44 39 7F 28                     cmp dword ptr [rdi + 0x28], r15d
00212757  74 49                           je 0x1402127a2
00212759  48 85 C0                        test rax, rax
0021275C  0F 85 A9 00 00 00               jne 0x14021280b
00212762  85 D2                           test edx, edx
00212764  0F 84 9E 00 00 00               je 0x140212808
0021276A  44 39 7F 28                     cmp dword ptr [rdi + 0x28], r15d
0021276E  0F 8D 97 00 00 00               jge 0x14021280b
00212774  48 8B C7                        mov rax, rdi
00212777  48 8B F8                        mov rdi, rax
0021277A  48 85 C0                        test rax, rax
0021277D  74 23                           je 0x1402127a2
0021277F  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00212783  48 C7 40 1C 00 00 01 00         mov qword ptr [rax + 0x1c], 0x10000
0021278B  44 89 48 24                     mov dword ptr [rax + 0x24], r9d
0021278F  4C 89 08                        mov qword ptr [rax], r9
00212792  4C 89 48 08                     mov qword ptr [rax + 8], r9
00212796  44 89 48 18                     mov dword ptr [rax + 0x18], r9d
0021279A  44 89 78 28                     mov dword ptr [rax + 0x28], r15d
0021279E  44 89 48 2C                     mov dword ptr [rax + 0x2c], r9d
002127A2  48 8B CF                        mov rcx, rdi
002127A5  48 85 FF                        test rdi, rdi
002127A8  74 56                           je 0x140212800
002127AA  FF 86 74 8F 00 00               inc dword ptr [rsi + 0x8f74]
002127B0  8B 41 20                        mov eax, dword ptr [rcx + 0x20]
002127B3  4C 89 41 08                     mov qword ptr [rcx + 8], r8
002127B7  85 C0                           test eax, eax
002127B9  0F 84 BA 02 00 00               je 0x140212a79
002127BF  83 F8 04                        cmp eax, 4
002127C2  0F 85 B1 02 00 00               jne 0x140212a79
002127C8  66 44 39 69 18                  cmp word ptr [rcx + 0x18], r13w
002127CD  0F 85 98 02 00 00               jne 0x140212a6b
002127D3  44 38 61 1A                     cmp byte ptr [rcx + 0x1a], r12b
002127D7  0F 85 8E 02 00 00               jne 0x140212a6b
002127DD  4C 2B 01                        sub r8, qword ptr [rcx]
002127E0  4C 89 01                        mov qword ptr [rcx], r8
002127E3  41 B8 01 00 00 00               mov r8d, 1
002127E9  8B 45 87                        mov eax, dword ptr [rbp - 0x79]
002127EC  89 41 18                        mov dword ptr [rcx + 0x18], eax
002127EF  8B 45 A7                        mov eax, dword ptr [rbp - 0x59]
002127F2  89 41 2C                        mov dword ptr [rcx + 0x2c], eax
002127F5  44 89 41 20                     mov dword ptr [rcx + 0x20], r8d
002127F9  C7 41 24 01 00 00 00            mov dword ptr [rcx + 0x24], 1
00212800  40 B6 01                        mov sil, 1
00212803  E9 24 FC FF FF                  jmp 0x14021242c
00212808  48 8B C7                        mov rax, rdi
0021280B  48 83 C7 40                     add rdi, 0x40
0021280F  FF C1                           inc ecx
00212811  E9 27 FF FF FF                  jmp 0x14021273d
00212816  48 83 C2 10                     add rdx, 0x10
0021281A  48 3B D0                        cmp rdx, rax
0021281D  0F 85 FD FC FF FF               jne 0x140212520
00212823  48 8D 55 8F                     lea rdx, [rbp - 0x71]
00212827  48 8B CB                        mov rcx, rbx
0021282A  E8 6D 20 1C 00                  call 0x1403d489c
0021282F  E9 C1 F8 FF FF                  jmp 0x1402120f5
00212834  B8 01 00 00 00                  mov eax, 1
00212839  49 89 00                        mov qword ptr [r8], rax
0021283C  E9 D5 FB FF FF                  jmp 0x140212416
00212841  4D 89 08                        mov qword ptr [r8], r9
00212844  E9 C8 FB FF FF                  jmp 0x140212411
00212849  4C 8B 45 AF                     mov r8, qword ptr [rbp - 0x51]
0021284D  E9 58 FF FF FF                  jmp 0x1402127aa
00212852  8B 72 08                        mov esi, dword ptr [rdx + 8]
00212855  8D 46 08                        lea eax, [rsi + 8]
00212858  33 F0                           xor esi, eax
0021285A  83 E6 07                        and esi, 7
0021285D  33 F0                           xor esi, eax
0021285F  89 72 08                        mov dword ptr [rdx + 8], esi
00212862  C1 EE 03                        shr esi, 3
00212865  F6 05 9A 42 DB 00 01            test byte ptr [rip + 0xdb429a], 1
0021286C  75 4B                           jne 0x1402128b9
0021286E  0F 0D 4D 8F                     prefetchw byte ptr [rbp - 0x71]
00212872  48 8B 45 8F                     mov rax, qword ptr [rbp - 0x71]
00212876  48 85 C0                        test rax, rax
00212879  75 1F                           jne 0x14021289a
0021287B  48 8B 4D 97                     mov rcx, qword ptr [rbp - 0x69]
0021287F  48 8D 45 8F                     lea rax, [rbp - 0x71]
00212883  F0 4C 0F B1 29                  lock cmpxchg qword ptr [rcx], r13
00212888  48 8D 4D 8F                     lea rcx, [rbp - 0x71]
0021288C  48 3B C1                        cmp rax, rcx
0021288F  74 3F                           je 0x1402128d0
00212891  48 8D 4D 8F                     lea rcx, [rbp - 0x71]
00212895  E8 06 52 00 00                  call 0x140217aa0
0021289A  48 8D 48 08                     lea rcx, [rax + 8]
0021289E  4C 89 6D 8F                     mov qword ptr [rbp - 0x71], r13
002128A2  48 8B 55 97                     mov rdx, qword ptr [rbp - 0x69]
002128A6  48 8B C2                        mov rax, rdx
002128A9  48 87 01                        xchg qword ptr [rcx], rax
002128AC  32 C2                           xor al, dl
002128AE  A8 04                           test al, 4
002128B0  74 1E                           je 0x1402128d0
002128B2  E8 69 53 00 00                  call 0x140217c20
002128B7  EB 17                           jmp 0x1402128d0
002128B9  8B 05 99 B5 CF 00               mov eax, dword ptr [rip + 0xcfb599]
002128BF  85 C0                           test eax, eax
002128C1  75 AB                           jne 0x14021286e
002128C3  48 8B 55 5F                     mov rdx, qword ptr [rbp + 0x5f]
002128C7  48 8D 4D 8F                     lea rcx, [rbp - 0x71]
002128CB  E8 20 51 00 00                  call 0x1402179f0
002128D0  44 39 2D 49 44 DB 00            cmp dword ptr [rip + 0xdb4449], r13d
002128D7  0F B6 7D 9F                     movzx edi, byte ptr [rbp - 0x61]
002128DB  74 0D                           je 0x1402128ea
002128DD  44 0F 20 C1                     mov rcx, cr8
002128E1  40 0F B6 D7                     movzx edx, dil
002128E5  E8 AE 2D 2E 00                  call 0x1404f5698
002128EA  44 0F 22 C7                     mov cr8, rdi
002128EE  65 FF 04 25 98 90 00 00         inc dword ptr gs:[0x9098]
002128F6  65 FF 04 25 64 90 00 00         inc dword ptr gs:[0x9064]
002128FE  45 85 FF                        test r15d, r15d
00212901  0F 84 4B 01 00 00               je 0x140212a52
00212907  65 4C 8B 2C 25 20 00 00 00      mov r13, qword ptr gs:[0x20]
00212910  44 8B 63 44                     mov r12d, dword ptr [rbx + 0x44]
00212914  C6 45 8A 00                     mov byte ptr [rbp - 0x76], 0
00212918  41 0F B6 85 D0 00 00 00         movzx eax, byte ptr [r13 + 0xd0]
00212920  41 FF 85 70 8F 00 00            inc dword ptr [r13 + 0x8f70]
00212927  65 4C 8B 34 25 88 01 00 00      mov r14, qword ptr gs:[0x188]
00212930  66 89 45 87                     mov word ptr [rbp - 0x79], ax
00212934  41 0F B6 85 D1 00 00 00         movzx eax, byte ptr [r13 + 0xd1]
0021293C  88 45 89                        mov byte ptr [rbp - 0x77], al
0021293F  41 8B 86 A0 05 00 00            mov eax, dword ptr [r14 + 0x5a0]
00212946  A8 01                           test al, 1
00212948  0F 85 04 01 00 00               jne 0x140212a52
0021294E  49 8B BE 20 06 00 00            mov rdi, qword ptr [r14 + 0x620]
00212955  44 8B 3D 0C 5B C5 00            mov r15d, dword ptr [rip + 0xc55b0c]
0021295C  48 85 FF                        test rdi, rdi
0021295F  75 4A                           jne 0x1402129ab
00212961  BA 00 02 00 00                  mov edx, 0x200
00212966  8D 4F 48                        lea ecx, [rdi + 0x48]
00212969  41 B8 52 65 54 72               mov r8d, 0x72546552
0021296F  E8 7C F7 96 00                  call 0x140b820f0
00212974  48 8B C8                        mov rcx, rax
00212977  48 85 C0                        test rax, rax
0021297A  0F 84 D2 00 00 00               je 0x140212a52
00212980  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00212984  48 C7 40 1C 00 00 01 00         mov qword ptr [rax + 0x1c], 0x10000
0021298C  44 89 78 28                     mov dword ptr [rax + 0x28], r15d
00212990  33 C0                           xor eax, eax
00212992  F0 49 0F B1 8E 20 06 00 00      lock cmpxchg qword ptr [r14 + 0x620], rcx
0021299B  48 8B F8                        mov rdi, rax
0021299E  0F 84 85 02 00 00               je 0x140212c29
002129A4  33 D2                           xor edx, edx
002129A6  E8 C5 FE 96 00                  call 0x140b82870
002129AB  33 C9                           xor ecx, ecx
002129AD  8B C1                           mov eax, ecx
002129AF  83 F9 08                        cmp ecx, 8
002129B2  73 35                           jae 0x1402129e9
002129B4  8B 57 1C                        mov edx, dword ptr [rdi + 0x1c]
002129B7  81 FA 00 00 01 00               cmp edx, 0x10000
002129BD  75 0C                           jne 0x1402129cb
002129BF  48 39 5F 10                     cmp qword ptr [rdi + 0x10], rbx
002129C3  75 06                           jne 0x1402129cb
002129C5  44 39 7F 28                     cmp dword ptr [rdi + 0x28], r15d
002129C9  74 48                           je 0x140212a13
002129CB  48 85 C0                        test rax, rax
002129CE  0F 85 2E 02 00 00               jne 0x140212c02
002129D4  85 D2                           test edx, edx
002129D6  0F 84 23 02 00 00               je 0x140212bff
002129DC  44 39 7F 28                     cmp dword ptr [rdi + 0x28], r15d
002129E0  0F 8D 1C 02 00 00               jge 0x140212c02
002129E6  48 8B C7                        mov rax, rdi
002129E9  48 8B F8                        mov rdi, rax
002129EC  48 85 C0                        test rax, rax
002129EF  74 22                           je 0x140212a13
002129F1  33 D2                           xor edx, edx
002129F3  89 50 24                        mov dword ptr [rax + 0x24], edx
002129F6  48 89 10                        mov qword ptr [rax], rdx
002129F9  48 89 50 08                     mov qword ptr [rax + 8], rdx
002129FD  89 50 18                        mov dword ptr [rax + 0x18], edx
00212A00  89 50 2C                        mov dword ptr [rax + 0x2c], edx
00212A03  44 89 78 28                     mov dword ptr [rax + 0x28], r15d
00212A07  48 C7 40 1C 00 00 01 00         mov qword ptr [rax + 0x1c], 0x10000
00212A0F  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00212A13  48 8B CF                        mov rcx, rdi
00212A16  48 8B D7                        mov rdx, rdi
00212A19  48 85 FF                        test rdi, rdi
00212A1C  74 34                           je 0x140212a52
00212A1E  41 FF 85 74 8F 00 00            inc dword ptr [r13 + 0x8f74]
00212A25  41 B8 01 00 00 00               mov r8d, 1
00212A2B  83 79 20 00                     cmp dword ptr [rcx + 0x20], 0
00212A2F  0F 85 E7 09 00 00               jne 0x14021341c
00212A35  B8 02 00 00 00                  mov eax, 2
00212A3A  48 89 41 08                     mov qword ptr [rcx + 8], rax
00212A3E  8B 45 87                        mov eax, dword ptr [rbp - 0x79]
00212A41  4C 89 01                        mov qword ptr [rcx], r8
00212A44  89 41 18                        mov dword ptr [rcx + 0x18], eax
00212A47  44 89 61 2C                     mov dword ptr [rcx + 0x2c], r12d
00212A4B  89 72 24                        mov dword ptr [rdx + 0x24], esi
00212A4E  44 89 41 20                     mov dword ptr [rcx + 0x20], r8d
00212A52  40 B6 01                        mov sil, 1
00212A55  E9 D2 F9 FF FF                  jmp 0x14021242c
00212A5A  4D 85 D2                        test r10, r10
00212A5D  0F 85 94 FA FF FF               jne 0x1402124f7
00212A63  4C 8B D2                        mov r10, rdx
00212A66  E9 8C FA FF FF                  jmp 0x1402124f7
00212A6B  41 B8 01 00 00 00               mov r8d, 1
00212A71  4C 89 01                        mov qword ptr [rcx], r8
00212A74  E9 70 FD FF FF                  jmp 0x1402127e9
00212A79  4C 89 09                        mov qword ptr [rcx], r9
00212A7C  E9 62 FD FF FF                  jmp 0x1402127e3
00212A81  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00212A8A  8B C2                           mov eax, edx
00212A8C  2B 43 10                        sub eax, dword ptr [rbx + 0x10]
00212A8F  48 C1 F8 04                     sar rax, 4
00212A93  88 81 60 04 00 00               mov byte ptr [rcx + 0x460], al
00212A99  48 85 D2                        test rdx, rdx
00212A9C  0F 84 59 F6 FF FF               je 0x1402120fb
00212AA2  E9 9A FA FF FF                  jmp 0x140212541
00212AA7  4C 39 73 30                     cmp qword ptr [rbx + 0x30], r14
00212AAB  0F 85 54 FA FF FF               jne 0x140212505
00212AB1  8B 73 38                        mov esi, dword ptr [rbx + 0x38]
00212AB4  48 8D 4D 8F                     lea rcx, [rbp - 0x71]
00212AB8  8D 46 08                        lea eax, [rsi + 8]
00212ABB  33 F0                           xor esi, eax
00212ABD  83 E6 07                        and esi, 7
00212AC0  33 F0                           xor esi, eax
00212AC2  89 73 38                        mov dword ptr [rbx + 0x38], esi
00212AC5  C1 EE 03                        shr esi, 3
00212AC8  E8 13 02 13 00                  call 0x140342ce0
00212ACD  65 FF 04 25 90 90 00 00         inc dword ptr gs:[0x9090]
00212AD5  65 FF 04 25 64 90 00 00         inc dword ptr gs:[0x9064]
00212ADD  45 85 FF                        test r15d, r15d
00212AE0  0F 84 6C FF FF FF               je 0x140212a52
00212AE6  65 4C 8B 2C 25 20 00 00 00      mov r13, qword ptr gs:[0x20]
00212AEF  44 8B 63 44                     mov r12d, dword ptr [rbx + 0x44]
00212AF3  C6 45 8A 00                     mov byte ptr [rbp - 0x76], 0
00212AF7  41 0F B6 85 D0 00 00 00         movzx eax, byte ptr [r13 + 0xd0]
00212AFF  41 FF 85 70 8F 00 00            inc dword ptr [r13 + 0x8f70]
00212B06  65 4C 8B 34 25 88 01 00 00      mov r14, qword ptr gs:[0x188]
00212B0F  66 89 45 87                     mov word ptr [rbp - 0x79], ax
00212B13  41 0F B6 85 D1 00 00 00         movzx eax, byte ptr [r13 + 0xd1]
00212B1B  88 45 89                        mov byte ptr [rbp - 0x77], al
00212B1E  41 8B 86 A0 05 00 00            mov eax, dword ptr [r14 + 0x5a0]
00212B25  A8 01                           test al, 1
00212B27  0F 85 25 FF FF FF               jne 0x140212a52
00212B2D  49 8B BE 20 06 00 00            mov rdi, qword ptr [r14 + 0x620]
00212B34  44 8B 3D 2D 59 C5 00            mov r15d, dword ptr [rip + 0xc5592d]
00212B3B  48 85 FF                        test rdi, rdi
00212B3E  75 4A                           jne 0x140212b8a
00212B40  BA 00 02 00 00                  mov edx, 0x200
00212B45  8D 4F 48                        lea ecx, [rdi + 0x48]
00212B48  41 B8 52 65 54 72               mov r8d, 0x72546552
00212B4E  E8 9D F5 96 00                  call 0x140b820f0
00212B53  48 8B C8                        mov rcx, rax
00212B56  48 85 C0                        test rax, rax
00212B59  0F 84 F3 FE FF FF               je 0x140212a52
00212B5F  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00212B63  48 C7 40 1C 00 00 01 00         mov qword ptr [rax + 0x1c], 0x10000
00212B6B  44 89 78 28                     mov dword ptr [rax + 0x28], r15d
00212B6F  33 C0                           xor eax, eax
00212B71  F0 49 0F B1 8E 20 06 00 00      lock cmpxchg qword ptr [r14 + 0x620], rcx
00212B7A  48 8B F8                        mov rdi, rax
00212B7D  0F 84 AE 00 00 00               je 0x140212c31
00212B83  33 D2                           xor edx, edx
00212B85  E8 E6 FC 96 00                  call 0x140b82870
00212B8A  33 C9                           xor ecx, ecx
00212B8C  8B C1                           mov eax, ecx
00212B8E  8B D1                           mov edx, ecx
00212B90  83 FA 08                        cmp edx, 8
00212B93  73 2D                           jae 0x140212bc2
00212B95  8B 4F 1C                        mov ecx, dword ptr [rdi + 0x1c]
00212B98  81 F9 00 00 01 00               cmp ecx, 0x10000
00212B9E  75 10                           jne 0x140212bb0
00212BA0  48 39 5F 10                     cmp qword ptr [rdi + 0x10], rbx
00212BA4  75 0A                           jne 0x140212bb0
00212BA6  44 39 7F 28                     cmp dword ptr [rdi + 0x28], r15d
00212BAA  0F 84 63 FE FF FF               je 0x140212a13
00212BB0  48 85 C0                        test rax, rax
00212BB3  75 69                           jne 0x140212c1e
00212BB5  85 C9                           test ecx, ecx
00212BB7  74 62                           je 0x140212c1b
00212BB9  44 39 7F 28                     cmp dword ptr [rdi + 0x28], r15d
00212BBD  7D 5F                           jge 0x140212c1e
00212BBF  48 8B C7                        mov rax, rdi
00212BC2  48 8B F8                        mov rdi, rax
00212BC5  48 85 C0                        test rax, rax
00212BC8  0F 84 45 FE FF FF               je 0x140212a13
00212BCE  33 C9                           xor ecx, ecx
00212BD0  89 48 24                        mov dword ptr [rax + 0x24], ecx
00212BD3  48 89 08                        mov qword ptr [rax], rcx
00212BD6  48 89 48 08                     mov qword ptr [rax + 8], rcx
00212BDA  89 48 18                        mov dword ptr [rax + 0x18], ecx
00212BDD  89 48 2C                        mov dword ptr [rax + 0x2c], ecx
00212BE0  E9 1E FE FF FF                  jmp 0x140212a03
00212BE5  45 85 C9                        test r9d, r9d
00212BE8  0F 85 55 F5 FF FF               jne 0x140212143
00212BEE  4C 8B D2                        mov r10, rdx
00212BF1  E9 4D F5 FF FF                  jmp 0x140212143
00212BF6  48 83 C2 10                     add rdx, 0x10
00212BFA  E9 67 F5 FF FF                  jmp 0x140212166
00212BFF  48 8B C7                        mov rax, rdi
00212C02  48 83 C7 40                     add rdi, 0x40
00212C06  FF C1                           inc ecx
00212C08  E9 A2 FD FF FF                  jmp 0x1402129af
00212C0D  48 8D 4D 8F                     lea rcx, [rbp - 0x71]
00212C11  E8 9A 52 04 00                  call 0x140257eb0
00212C16  E9 DA F4 FF FF                  jmp 0x1402120f5
00212C1B  48 8B C7                        mov rax, rdi
00212C1E  48 83 C7 40                     add rdi, 0x40
00212C22  FF C2                           inc edx
00212C24  E9 67 FF FF FF                  jmp 0x140212b90
00212C29  48 8B D1                        mov rdx, rcx
00212C2C  E9 ED FD FF FF                  jmp 0x140212a1e
00212C31  48 8B D1                        mov rdx, rcx
00212C34  E9 E5 FD FF FF                  jmp 0x140212a1e
00212C39  41 0F 0D 08                     prefetchw byte ptr [r8]
00212C3D  41 8B 00                        mov eax, dword ptr [r8]
00212C40  8B D0                           mov edx, eax
00212C42  0F BA F2 15                     btr edx, 0x15
00212C46  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
00212C4B  75 F3                           jne 0x140212c40
00212C4D  0F BA E0 15                     bt eax, 0x15
00212C51  0F 83 EC F5 FF FF               jae 0x140212243
00212C57  E8 74 05 05 00                  call 0x1402631d0
00212C5C  E9 E2 F5 FF FF                  jmp 0x140212243
00212C61  41 0F 0D 08                     prefetchw byte ptr [r8]
00212C65  41 8B 00                        mov eax, dword ptr [r8]
00212C68  8B D0                           mov edx, eax
00212C6A  0F BA F2 15                     btr edx, 0x15
00212C6E  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
00212C73  75 F3                           jne 0x140212c68
00212C75  0F BA E0 15                     bt eax, 0x15
00212C79  0F 83 9D F9 FF FF               jae 0x14021261c
00212C7F  E8 4C 05 05 00                  call 0x1402631d0
00212C84  E9 93 F9 FF FF                  jmp 0x14021261c
00212C89  44 39 67 28                     cmp dword ptr [rdi + 0x28], r12d
00212C8D  0F 8D 34 07 00 00               jge 0x1402133c7
00212C93  48 8B C7                        mov rax, rdi
00212C96  48 8B F8                        mov rdi, rax
00212C99  48 85 C0                        test rax, rax
00212C9C  74 23                           je 0x140212cc1
00212C9E  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00212CA2  48 C7 40 1C 00 00 01 00         mov qword ptr [rax + 0x1c], 0x10000
00212CAA  44 89 68 24                     mov dword ptr [rax + 0x24], r13d
00212CAE  4C 89 28                        mov qword ptr [rax], r13
00212CB1  4C 89 68 08                     mov qword ptr [rax + 8], r13
00212CB5  44 89 68 18                     mov dword ptr [rax + 0x18], r13d
00212CB9  44 89 60 28                     mov dword ptr [rax + 0x28], r12d
00212CBD  44 89 68 2C                     mov dword ptr [rax + 0x2c], r13d
00212CC1  48 8B CF                        mov rcx, rdi
00212CC4  48 85 FF                        test rdi, rdi
00212CC7  0F 84 60 07 00 00               je 0x14021342d
00212CCD  FF 86 74 8F 00 00               inc dword ptr [rsi + 0x8f74]
00212CD3  BF 04 00 00 00                  mov edi, 4
00212CD8  48 8B 45 AF                     mov rax, qword ptr [rbp - 0x51]
00212CDC  48 89 01                        mov qword ptr [rcx], rax
00212CDF  8B 45 87                        mov eax, dword ptr [rbp - 0x79]
00212CE2  89 41 18                        mov dword ptr [rcx + 0x18], eax
00212CE5  89 79 20                        mov dword ptr [rcx + 0x20], edi
00212CE8  65 4C 8B 04 25 88 01 00 00      mov r8, qword ptr gs:[0x188]
00212CF1  41 8B D5                        mov edx, r13d
00212CF4  49 8B 80 20 02 00 00            mov rax, qword ptr [r8 + 0x220]
00212CFB  41 8B 88 A0 05 00 00            mov ecx, dword ptr [r8 + 0x5a0]
00212D02  C1 E9 09                        shr ecx, 9
00212D05  83 E1 07                        and ecx, 7
00212D08  48 8B 80 A0 02 00 00            mov rax, qword ptr [rax + 0x2a0]
00212D0F  48 85 C0                        test rax, rax
00212D12  74 0B                           je 0x140212d1f
00212D14  8B 80 3C 04 00 00               mov eax, dword ptr [rax + 0x43c]
00212D1A  3B C8                           cmp ecx, eax
00212D1C  0F 4D C8                        cmovge ecx, eax
00212D1F  83 F9 02                        cmp ecx, 2
00212D22  0F 8C 5C 04 00 00               jl 0x140213184
00212D28  83 F9 01                        cmp ecx, 1
00212D2B  7E 07                           jle 0x140212d34
00212D2D  F6 43 1A 04                     test byte ptr [rbx + 0x1a], 4
00212D31  0F 44 D7                        cmove edx, edi
00212D34  44 0F B7 4B 1A                  movzx r9d, word ptr [rbx + 0x1a]
00212D39  8B CA                           mov ecx, edx
00212D3B  41 0F BE 80 C3 00 00 00         movsx eax, byte ptr [r8 + 0xc3]
00212D43  83 C9 02                        or ecx, 2
00212D46  41 F6 C1 02                     test r9b, 2
00212D4A  0F 45 CA                        cmovne ecx, edx
00212D4D  41 C1 E9 08                     shr r9d, 8
00212D51  8B D1                           mov edx, ecx
00212D53  81 CA 00 FF 00 00               or edx, 0xff00
00212D59  41 3B C1                        cmp eax, r9d
00212D5C  0F 4E D1                        cmovle edx, ecx
00212D5F  85 D2                           test edx, edx
00212D61  74 08                           je 0x140212d6b
00212D63  48 8B CB                        mov rcx, rbx
00212D66  E8 A5 11 00 00                  call 0x140213f10
00212D6B  41 B8 44 02 01 00               mov r8d, 0x10244
00212D71  48 8D 55 B7                     lea rdx, [rbp - 0x49]
00212D75  48 8B CB                        mov rcx, rbx
00212D78  E8 73 39 00 00                  call 0x1402166f0
00212D7D  41 F6 C6 03                     test r14b, 3
00212D81  0F 85 F5 03 00 00               jne 0x14021317c
00212D87  45 0F B6 A6 60 04 00 00         movzx r12d, byte ptr [r14 + 0x460]
00212D8F  33 C0                           xor eax, eax
00212D91  0F 57 C0                        xorps xmm0, xmm0
00212D94  48 89 45 FF                     mov qword ptr [rbp - 1], rax
00212D98  0F B7 43 1A                     movzx eax, word ptr [rbx + 0x1a]
00212D9C  0F 11 45 EF                     movups xmmword ptr [rbp - 0x11], xmm0
00212DA0  A8 08                           test al, 8
00212DA2  0F 85 46 01 00 00               jne 0x140212eee
00212DA8  41 8B D5                        mov edx, r13d
00212DAB  A8 04                           test al, 4
00212DAD  74 31                           je 0x140212de0
00212DAF  49 8B 86 20 02 00 00            mov rax, qword ptr [r14 + 0x220]
00212DB6  41 8B 8E A0 05 00 00            mov ecx, dword ptr [r14 + 0x5a0]
00212DBD  C1 E9 09                        shr ecx, 9
00212DC0  83 E1 07                        and ecx, 7
00212DC3  48 8B 80 A0 02 00 00            mov rax, qword ptr [rax + 0x2a0]
00212DCA  48 85 C0                        test rax, rax
00212DCD  74 0B                           je 0x140212dda
00212DCF  8B 80 3C 04 00 00               mov eax, dword ptr [rax + 0x43c]
00212DD5  3B C8                           cmp ecx, eax
00212DD7  0F 4D C8                        cmovge ecx, eax
00212DDA  83 F9 02                        cmp ecx, 2
00212DDD  0F 4C D7                        cmovl edx, edi
00212DE0  8B F2                           mov esi, edx
00212DE2  83 CE 02                        or esi, 2
00212DE5  F6 43 1A 02                     test byte ptr [rbx + 0x1a], 2
00212DE9  0F 44 F2                        cmove esi, edx
00212DEC  85 F6                           test esi, esi
00212DEE  0F 84 FA 00 00 00               je 0x140212eee
00212DF4  48 8D 7B 60                     lea rdi, [rbx + 0x60]
00212DF8  4C 89 6D EF                     mov qword ptr [rbp - 0x11], r13
00212DFC  48 89 7D F7                     mov qword ptr [rbp - 9], rdi
00212E00  90                              nop
00212E01  45 0F 20 C5                     mov r13, cr8
00212E05  B8 02 00 00 00                  mov eax, 2
00212E0A  44 0F 22 C0                     mov cr8, rax
00212E0E  83 3D 0B 3F DB 00 00            cmp dword ptr [rip + 0xdb3f0b], 0
00212E15  0F 85 33 03 00 00               jne 0x14021314e
00212E1B  F6 05 E4 3C DB 00 21            test byte ptr [rip + 0xdb3ce4], 0x21
00212E22  44 88 6D FF                     mov byte ptr [rbp - 1], r13b
00212E26  0F 85 77 02 00 00               jne 0x1402130a3
00212E2C  48 8D 55 EF                     lea rdx, [rbp - 0x11]
00212E30  48 87 17                        xchg qword ptr [rdi], rdx
00212E33  48 85 D2                        test rdx, rdx
00212E36  0F 85 6D 03 00 00               jne 0x1402131a9
00212E3C  48 8B 43 30                     mov rax, qword ptr [rbx + 0x30]
00212E40  48 8D 7B 30                     lea rdi, [rbx + 0x30]
00212E44  49 3B C6                        cmp rax, r14
00212E47  74 2E                           je 0x140212e77
00212E49  45 33 C9                        xor r9d, r9d
00212E4C  48 85 C0                        test rax, rax
00212E4F  41 8B C9                        mov ecx, r9d
00212E52  0F 95 C1                        setne cl
00212E55  45 85 E4                        test r12d, r12d
00212E58  0F 85 64 02 00 00               jne 0x1402130c2
00212E5E  8B 53 48                        mov edx, dword ptr [rbx + 0x48]
00212E61  8B 43 40                        mov eax, dword ptr [rbx + 0x40]
00212E64  48 8B 7B 10                     mov rdi, qword ptr [rbx + 0x10]
00212E68  48 03 D0                        add rdx, rax
00212E6B  48 85 FF                        test rdi, rdi
00212E6E  0F 85 9B 02 00 00               jne 0x14021310f
00212E74  49 8B F9                        mov rdi, r9
00212E77  40 F6 C6 04                     test sil, 4
00212E7B  0F 85 36 03 00 00               jne 0x1402131b7
00212E81  40 F6 C6 02                     test sil, 2
00212E85  74 34                           je 0x140212ebb
00212E87  8B 47 08                        mov eax, dword ptr [rdi + 8]
00212E8A  A8 04                           test al, 4
00212E8C  0F 85 75 02 00 00               jne 0x140213107
00212E92  B8 01 00 00 00                  mov eax, 1
00212E97  F0 41 0F C1 86 E4 05 00 00      lock xadd dword ptr [r14 + 0x5e4], eax
00212EA0  FF C0                           inc eax
00212EA2  83 F8 01                        cmp eax, 1
00212EA5  75 10                           jne 0x140212eb7
00212EA7  41 0F B6 86 18 03 00 00         movzx eax, byte ptr [r14 + 0x318]
00212EAF  84 C0                           test al, al
00212EB1  0F 85 28 03 00 00               jne 0x1402131df
00212EB7  83 4F 08 04                     or dword ptr [rdi + 8], 4
00212EBB  48 8D 4D EF                     lea rcx, [rbp - 0x11]
00212EBF  E8 1C FE 12 00                  call 0x140342ce0
00212EC4  85 F6                           test esi, esi
00212EC6  74 23                           je 0x140212eeb
00212EC8  40 F6 C6 04                     test sil, 4
00212ECC  74 0F                           je 0x140212edd
00212ECE  45 33 C0                        xor r8d, r8d
00212ED1  49 8B CE                        mov rcx, r14
00212ED4  41 8D 50 02                     lea edx, [r8 + 2]
00212ED8  E8 33 32 00 00                  call 0x140216110
00212EDD  40 F6 C6 02                     test sil, 2
00212EE1  74 08                           je 0x140212eeb
00212EE3  49 8B CE                        mov rcx, r14
00212EE6  E8 69 2D 00 00                  call 0x140215c54
00212EEB  45 33 ED                        xor r13d, r13d
00212EEE  65 FF 04 25 94 90 00 00         inc dword ptr gs:[0x9094]
00212EF6  65 FF 04 25 64 90 00 00         inc dword ptr gs:[0x9064]
00212EFE  45 85 FF                        test r15d, r15d
00212F01  0F 84 86 01 00 00               je 0x14021308d
00212F07  8B 43 44                        mov eax, dword ptr [rbx + 0x44]
00212F0A  89 45 A7                        mov dword ptr [rbp - 0x59], eax
00212F0D  44 89 6D 87                     mov dword ptr [rbp - 0x79], r13d
00212F11  0F 31                           rdtsc
00212F13  65 4C 8B 3C 25 20 00 00 00      mov r15, qword ptr gs:[0x20]
00212F1C  48 C1 E2 20                     shl rdx, 0x20
00212F20  48 0B C2                        or rax, rdx
00212F23  C6 45 8A 00                     mov byte ptr [rbp - 0x76], 0
00212F27  4C 8B F0                        mov r14, rax
00212F2A  41 FF 87 70 8F 00 00            inc dword ptr [r15 + 0x8f70]
00212F31  65 48 8B 34 25 88 01 00 00      mov rsi, qword ptr gs:[0x188]
00212F3A  41 0F B6 87 D0 00 00 00         movzx eax, byte ptr [r15 + 0xd0]
00212F42  45 0F B6 AF D1 00 00 00         movzx r13d, byte ptr [r15 + 0xd1]
00212F4A  66 89 45 87                     mov word ptr [rbp - 0x79], ax
00212F4E  8B 8E A0 05 00 00               mov ecx, dword ptr [rsi + 0x5a0]
00212F54  44 88 6D 89                     mov byte ptr [rbp - 0x77], r13b
00212F58  F6 C1 01                        test cl, 1
00212F5B  0F 85 2C 01 00 00               jne 0x14021308d
00212F61  48 8B BE 20 06 00 00            mov rdi, qword ptr [rsi + 0x620]
00212F68  44 8B 25 F9 54 C5 00            mov r12d, dword ptr [rip + 0xc554f9]
00212F6F  48 85 FF                        test rdi, rdi
00212F72  75 49                           jne 0x140212fbd
00212F74  BA 00 02 00 00                  mov edx, 0x200
00212F79  8D 4F 48                        lea ecx, [rdi + 0x48]
00212F7C  41 B8 52 65 54 72               mov r8d, 0x72546552
00212F82  E8 69 F1 96 00                  call 0x140b820f0
00212F87  48 8B C8                        mov rcx, rax
00212F8A  48 85 C0                        test rax, rax
00212F8D  0F 84 FA 00 00 00               je 0x14021308d
00212F93  45 33 C0                        xor r8d, r8d
00212F96  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00212F9A  48 C7 40 1C 00 00 01 00         mov qword ptr [rax + 0x1c], 0x10000
00212FA2  44 89 60 28                     mov dword ptr [rax + 0x28], r12d
00212FA6  33 C0                           xor eax, eax
00212FA8  F0 48 0F B1 8E 20 06 00 00      lock cmpxchg qword ptr [rsi + 0x620], rcx
00212FB1  48 8B F8                        mov rdi, rax
00212FB4  74 7D                           je 0x140213033
00212FB6  33 D2                           xor edx, edx
00212FB8  E8 B3 F8 96 00                  call 0x140b82870
00212FBD  45 33 C0                        xor r8d, r8d
00212FC0  41 8B C0                        mov eax, r8d
00212FC3  41 8B D0                        mov edx, r8d
00212FC6  83 FA 08                        cmp edx, 8
00212FC9  73 35                           jae 0x140213000
00212FCB  8B 4F 1C                        mov ecx, dword ptr [rdi + 0x1c]
00212FCE  81 F9 00 00 01 00               cmp ecx, 0x10000
00212FD4  75 0C                           jne 0x140212fe2
00212FD6  48 39 5F 10                     cmp qword ptr [rdi + 0x10], rbx
00212FDA  75 06                           jne 0x140212fe2
00212FDC  44 39 67 28                     cmp dword ptr [rdi + 0x28], r12d
00212FE0  74 49                           je 0x14021302b
00212FE2  48 85 C0                        test rax, rax
00212FE5  0F 85 AD 00 00 00               jne 0x140213098
00212FEB  85 C9                           test ecx, ecx
00212FED  0F 84 A2 00 00 00               je 0x140213095
00212FF3  44 39 67 28                     cmp dword ptr [rdi + 0x28], r12d
00212FF7  0F 8D 9B 00 00 00               jge 0x140213098
00212FFD  48 8B C7                        mov rax, rdi
00213000  48 8B F8                        mov rdi, rax
00213003  48 85 C0                        test rax, rax
00213006  74 23                           je 0x14021302b
00213008  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
0021300C  48 C7 40 1C 00 00 01 00         mov qword ptr [rax + 0x1c], 0x10000
00213014  44 89 40 24                     mov dword ptr [rax + 0x24], r8d
00213018  4C 89 00                        mov qword ptr [rax], r8
0021301B  4C 89 40 08                     mov qword ptr [rax + 8], r8
0021301F  44 89 40 18                     mov dword ptr [rax + 0x18], r8d
00213023  44 89 60 28                     mov dword ptr [rax + 0x28], r12d
00213027  44 89 40 2C                     mov dword ptr [rax + 0x2c], r8d
0021302B  48 8B CF                        mov rcx, rdi
0021302E  48 85 FF                        test rdi, rdi
00213031  74 5A                           je 0x14021308d
00213033  41 FF 87 74 8F 00 00            inc dword ptr [r15 + 0x8f74]
0021303A  8B 41 20                        mov eax, dword ptr [rcx + 0x20]
0021303D  4C 89 71 08                     mov qword ptr [rcx + 8], r14
00213041  85 C0                           test eax, eax
00213043  0F 84 B6 00 00 00               je 0x1402130ff
00213049  83 F8 04                        cmp eax, 4
0021304C  0F 85 AD 00 00 00               jne 0x1402130ff
00213052  0F B7 45 87                     movzx eax, word ptr [rbp - 0x79]
00213056  66 39 41 18                     cmp word ptr [rcx + 0x18], ax
0021305A  0F 85 91 00 00 00               jne 0x1402130f1
00213060  44 38 69 1A                     cmp byte ptr [rcx + 0x1a], r13b
00213064  0F 85 87 00 00 00               jne 0x1402130f1
0021306A  4C 2B 31                        sub r14, qword ptr [rcx]
0021306D  4C 89 31                        mov qword ptr [rcx], r14
00213070  41 B8 01 00 00 00               mov r8d, 1
00213076  8B 45 87                        mov eax, dword ptr [rbp - 0x79]
00213079  89 41 18                        mov dword ptr [rcx + 0x18], eax
0021307C  8B 45 A7                        mov eax, dword ptr [rbp - 0x59]
0021307F  89 41 2C                        mov dword ptr [rcx + 0x2c], eax
00213082  44 89 41 20                     mov dword ptr [rcx + 0x20], r8d
00213086  C7 41 24 01 00 00 00            mov dword ptr [rcx + 0x24], 1
0021308D  40 B6 01                        mov sil, 1
00213090  E9 97 F3 FF FF                  jmp 0x14021242c
00213095  48 8B C7                        mov rax, rdi
00213098  48 83 C7 40                     add rdi, 0x40
0021309C  FF C2                           inc edx
0021309E  E9 23 FF FF FF                  jmp 0x140212fc6
002130A3  8B 05 AF AD CF 00               mov eax, dword ptr [rip + 0xcfadaf]
002130A9  85 C0                           test eax, eax
002130AB  0F 85 7B FD FF FF               jne 0x140212e2c
002130B1  48 8B D7                        mov rdx, rdi
002130B4  48 8D 4D EF                     lea rcx, [rbp - 0x11]
002130B8  E8 93 27 06 00                  call 0x140275850
002130BD  E9 7A FD FF FF                  jmp 0x140212e3c
002130C2  48 8B 43 10                     mov rax, qword ptr [rbx + 0x10]
002130C6  48 85 C0                        test rax, rax
002130C9  0F 84 8F FD FF FF               je 0x140212e5e
002130CF  44 3B 60 08                     cmp r12d, dword ptr [rax + 8]
002130D3  0F 83 85 FD FF FF               jae 0x140212e5e
002130D9  41 8B FC                        mov edi, r12d
002130DC  48 C1 E7 04                     shl rdi, 4
002130E0  48 03 F8                        add rdi, rax
002130E3  4C 39 37                        cmp qword ptr [rdi], r14
002130E6  0F 85 72 FD FF FF               jne 0x140212e5e
002130EC  E9 86 FD FF FF                  jmp 0x140212e77
002130F1  41 B8 01 00 00 00               mov r8d, 1
002130F7  4C 89 01                        mov qword ptr [rcx], r8
002130FA  E9 77 FF FF FF                  jmp 0x140213076
002130FF  4C 89 01                        mov qword ptr [rcx], r8
00213102  E9 69 FF FF FF                  jmp 0x140213070
00213107  83 E6 FD                        and esi, 0xfffffffd
0021310A  E9 AC FD FF FF                  jmp 0x140212ebb
0021310F  44 8B 47 08                     mov r8d, dword ptr [rdi + 8]
00213113  49 C1 E0 04                     shl r8, 4
00213117  4C 03 C7                        add r8, rdi
0021311A  48 83 C7 10                     add rdi, 0x10
0021311E  48 3B CA                        cmp rcx, rdx
00213121  0F 83 4D FD FF FF               jae 0x140212e74
00213127  48 8B 07                        mov rax, qword ptr [rdi]
0021312A  49 3B C6                        cmp rax, r14
0021312D  74 30                           je 0x14021315f
0021312F  48 85 C0                        test rax, rax
00213132  74 0C                           je 0x140213140
00213134  48 FF C1                        inc rcx
00213137  48 3B CA                        cmp rcx, rdx
0021313A  0F 84 34 FD FF FF               je 0x140212e74
00213140  48 83 C7 10                     add rdi, 0x10
00213144  49 3B F8                        cmp rdi, r8
00213147  75 DE                           jne 0x140213127
00213149  E9 26 FD FF FF                  jmp 0x140212e74
0021314E  0F B6 D0                        movzx edx, al
00213151  41 0F B6 CD                     movzx ecx, r13b
00213155  E8 A2 25 2E 00                  call 0x1404f56fc
0021315A  E9 BC FC FF FF                  jmp 0x140212e1b
0021315F  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00213168  8B C7                           mov eax, edi
0021316A  2B 43 10                        sub eax, dword ptr [rbx + 0x10]
0021316D  48 C1 F8 04                     sar rax, 4
00213171  88 81 60 04 00 00               mov byte ptr [rcx + 0x460], al
00213177  E9 FB FC FF FF                  jmp 0x140212e77
0021317C  45 8B E5                        mov r12d, r13d
0021317F  E9 0B FC FF FF                  jmp 0x140212d8f
00213184  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0021318D  4C 3B C0                        cmp r8, rax
00213190  0F 85 92 FB FF FF               jne 0x140212d28
00213196  41 83 B8 E0 05 00 00 00         cmp dword ptr [r8 + 0x5e0], 0
0021319E  0F 84 84 FB FF FF               je 0x140212d28
002131A4  E9 84 FB FF FF                  jmp 0x140212d2d
002131A9  48 8D 4D EF                     lea rcx, [rbp - 0x11]
002131AD  E8 FE 4C 04 00                  call 0x140257eb0
002131B2  E9 85 FC FF FF                  jmp 0x140212e3c
002131B7  8B 47 08                        mov eax, dword ptr [rdi + 8]
002131BA  A8 01                           test al, 1
002131BC  75 19                           jne 0x1402131d7
002131BE  45 33 C9                        xor r9d, r9d
002131C1  45 33 C0                        xor r8d, r8d
002131C4  33 D2                           xor edx, edx
002131C6  49 8B CE                        mov rcx, r14
002131C9  E8 32 FA 17 00                  call 0x140392c00
002131CE  83 4F 08 01                     or dword ptr [rdi + 8], 1
002131D2  E9 AA FC FF FF                  jmp 0x140212e81
002131D7  83 E6 FB                        and esi, 0xfffffffb
002131DA  E9 A2 FC FF FF                  jmp 0x140212e81
002131DF  45 0F 20 C4                     mov r12, cr8
002131E3  B8 02 00 00 00                  mov eax, 2
002131E8  44 0F 22 C0                     mov cr8, rax
002131EC  83 3D 2D 3B DB 00 00            cmp dword ptr [rip + 0xdb3b2d], 0
002131F3  75 4E                           jne 0x140213243
002131F5  65 4C 8B 2C 25 20 00 00 00      mov r13, qword ptr gs:[0x20]
002131FE  4D 8D 86 28 03 00 00            lea r8, [r14 + 0x328]
00213205  49 8B CE                        mov rcx, r14
00213208  49 8D 95 78 91 00 00            lea rdx, [r13 + 0x9178]
0021320F  E8 CC BE 00 00                  call 0x14021f0e0
00213214  85 C0                           test eax, eax
00213216  74 08                           je 0x140213220
00213218  49 8B CD                        mov rcx, r13
0021321B  E8 B0 42 FF FF                  call 0x1402074d0
00213220  83 3D F9 3A DB 00 00            cmp dword ptr [rip + 0xdb3af9], 0
00213227  74 0D                           je 0x140213236
00213229  44 0F 20 C1                     mov rcx, cr8
0021322D  41 0F B6 D4                     movzx edx, r12b
00213231  E8 62 24 2E 00                  call 0x1404f5698
00213236  41 0F B6 C4                     movzx eax, r12b
0021323A  44 0F 22 C0                     mov cr8, rax
0021323E  E9 74 FC FF FF                  jmp 0x140212eb7
00213243  0F B6 D0                        movzx edx, al
00213246  41 0F B6 CC                     movzx ecx, r12b
0021324A  E8 AD 24 2E 00                  call 0x1404f56fc
0021324F  EB A4                           jmp 0x1402131f5
00213251  45 84 E4                        test r12b, r12b
00213254  0F 84 75 01 00 00               je 0x1402133cf
0021325A  8B 42 08                        mov eax, dword ptr [rdx + 8]
0021325D  4C 89 32                        mov qword ptr [rdx], r14
00213260  83 E0 07                        and eax, 7
00213263  83 C8 08                        or eax, 8
00213266  89 42 08                        mov dword ptr [rdx + 8], eax
00213269  48 8D 45 D7                     lea rax, [rbp - 0x29]
0021326D  FF 43 48                        inc dword ptr [rbx + 0x48]
00213270  48 89 45 DF                     mov qword ptr [rbp - 0x21], rax
00213274  48 8D 45 D7                     lea rax, [rbp - 0x29]
00213278  48 89 45 D7                     mov qword ptr [rbp - 0x29], rax
0021327C  48 8B 43 20                     mov rax, qword ptr [rbx + 0x20]
00213280  4C 89 6D BF                     mov qword ptr [rbp - 0x41], r13
00213284  48 C7 45 CF 01 00 06 00         mov qword ptr [rbp - 0x31], 0x60001
0021328C  4C 89 75 C7                     mov qword ptr [rbp - 0x39], r14
00213290  4C 89 6D E7                     mov qword ptr [rbp - 0x19], r13
00213294  48 85 C0                        test rax, rax
00213297  0F 85 53 01 00 00               jne 0x1402133f0
0021329D  48 8D 45 B7                     lea rax, [rbp - 0x49]
002132A1  48 89 45 BF                     mov qword ptr [rbp - 0x41], rax
002132A5  48 8D 45 B7                     lea rax, [rbp - 0x49]
002132A9  48 89 45 B7                     mov qword ptr [rbp - 0x49], rax
002132AD  48 8D 45 B7                     lea rax, [rbp - 0x49]
002132B1  48 8D 4D 8F                     lea rcx, [rbp - 0x71]
002132B5  48 89 43 20                     mov qword ptr [rbx + 0x20], rax
002132B9  E8 22 FA 12 00                  call 0x140342ce0
002132BE  65 FF 04 25 9C 90 00 00         inc dword ptr gs:[0x909c]
002132C6  BF 04 00 00 00                  mov edi, 4
002132CB  45 85 FF                        test r15d, r15d
002132CE  0F 84 14 FA FF FF               je 0x140212ce8
002132D4  0F 57 C0                        xorps xmm0, xmm0
002132D7  0F 11 45 07                     movups xmmword ptr [rbp + 7], xmm0
002132DB  0F 11 45 17                     movups xmmword ptr [rbp + 0x17], xmm0
002132DF  0F 11 45 27                     movups xmmword ptr [rbp + 0x27], xmm0
002132E3  0F 31                           rdtsc
002132E5  65 48 8B 34 25 20 00 00 00      mov rsi, qword ptr gs:[0x20]
002132EE  48 C1 E2 20                     shl rdx, 0x20
002132F2  48 0B C2                        or rax, rdx
002132F5  44 88 6D 8A                     mov byte ptr [rbp - 0x76], r13b
002132F9  48 89 45 AF                     mov qword ptr [rbp - 0x51], rax
002132FD  0F B6 8E D0 00 00 00            movzx ecx, byte ptr [rsi + 0xd0]
00213304  FF 86 70 8F 00 00               inc dword ptr [rsi + 0x8f70]
0021330A  65 4C 8B 2C 25 88 01 00 00      mov r13, qword ptr gs:[0x188]
00213313  66 89 4D 87                     mov word ptr [rbp - 0x79], cx
00213317  0F B6 8E D1 00 00 00            movzx ecx, byte ptr [rsi + 0xd1]
0021331E  88 4D 89                        mov byte ptr [rbp - 0x77], cl
00213321  41 8B 8D A0 05 00 00            mov ecx, dword ptr [r13 + 0x5a0]
00213328  F6 C1 01                        test cl, 1
0021332B  0F 85 06 01 00 00               jne 0x140213437
00213331  49 8B BD 20 06 00 00            mov rdi, qword ptr [r13 + 0x620]
00213338  44 8B 25 29 51 C5 00            mov r12d, dword ptr [rip + 0xc55129]
0021333F  48 85 FF                        test rdi, rdi
00213342  75 46                           jne 0x14021338a
00213344  BA 00 02 00 00                  mov edx, 0x200
00213349  8D 4F 48                        lea ecx, [rdi + 0x48]
0021334C  41 B8 52 65 54 72               mov r8d, 0x72546552
00213352  E8 99 ED 96 00                  call 0x140b820f0
00213357  48 8B C8                        mov rcx, rax
0021335A  48 85 C0                        test rax, rax
0021335D  0F 84 C7 00 00 00               je 0x14021342a
00213363  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00213367  48 C7 40 1C 00 00 01 00         mov qword ptr [rax + 0x1c], 0x10000
0021336F  44 89 60 28                     mov dword ptr [rax + 0x28], r12d
00213373  33 C0                           xor eax, eax
00213375  F0 49 0F B1 8D 20 06 00 00      lock cmpxchg qword ptr [r13 + 0x620], rcx
0021337E  48 8B F8                        mov rdi, rax
00213381  74 65                           je 0x1402133e8
00213383  33 D2                           xor edx, edx
00213385  E8 E6 F4 96 00                  call 0x140b82870
0021338A  45 33 ED                        xor r13d, r13d
0021338D  41 8B C5                        mov eax, r13d
00213390  41 8B D5                        mov edx, r13d
00213393  83 FA 08                        cmp edx, 8
00213396  0F 83 FA F8 FF FF               jae 0x140212c96
0021339C  8B 4F 1C                        mov ecx, dword ptr [rdi + 0x1c]
0021339F  81 F9 00 00 01 00               cmp ecx, 0x10000
002133A5  75 10                           jne 0x1402133b7
002133A7  48 39 5F 10                     cmp qword ptr [rdi + 0x10], rbx
002133AB  75 0A                           jne 0x1402133b7
002133AD  44 39 67 28                     cmp dword ptr [rdi + 0x28], r12d
002133B1  0F 84 0A F9 FF FF               je 0x140212cc1
002133B7  48 85 C0                        test rax, rax
002133BA  75 0B                           jne 0x1402133c7
002133BC  85 C9                           test ecx, ecx
002133BE  0F 85 C5 F8 FF FF               jne 0x140212c89
002133C4  48 8B C7                        mov rax, rdi
002133C7  48 83 C7 40                     add rdi, 0x40
002133CB  FF C2                           inc edx
002133CD  EB C4                           jmp 0x140213393
002133CF  48 8D 4D 8F                     lea rcx, [rbp - 0x71]
002133D3  E8 08 F9 12 00                  call 0x140342ce0
002133D8  65 FF 04 25 A0 90 00 00         inc dword ptr gs:[0x90a0]
002133E0  40 32 F6                        xor sil, sil
002133E3  E9 44 F0 FF FF                  jmp 0x14021242c
002133E8  45 33 ED                        xor r13d, r13d
002133EB  E9 DD F8 FF FF                  jmp 0x140212ccd
002133F0  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
002133F4  48 39 01                        cmp qword ptr [rcx], rax
002133F7  74 07                           je 0x140213400
002133F9  B9 03 00 00 00                  mov ecx, 3
002133FE  CD 29                           int 0x29
00213400  48 89 4D BF                     mov qword ptr [rbp - 0x41], rcx
00213404  48 8D 55 B7                     lea rdx, [rbp - 0x49]
00213408  48 89 45 B7                     mov qword ptr [rbp - 0x49], rax
0021340C  48 89 11                        mov qword ptr [rcx], rdx
0021340F  48 8D 4D B7                     lea rcx, [rbp - 0x49]
00213413  48 89 48 08                     mov qword ptr [rax + 8], rcx
00213417  E9 91 FE FF FF                  jmp 0x1402132ad
0021341C  39 72 24                        cmp dword ptr [rdx + 0x24], esi
0021341F  0F 83 29 F6 FF FF               jae 0x140212a4e
00213425  E9 21 F6 FF FF                  jmp 0x140212a4b
0021342A  45 33 ED                        xor r13d, r13d
0021342D  BF 04 00 00 00                  mov edi, 4
00213432  E9 B1 F8 FF FF                  jmp 0x140212ce8
00213437  45 33 ED                        xor r13d, r13d
0021343A  E9 A9 F8 FF FF                  jmp 0x140212ce8
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpAcquireResourceSharedLite(__int64 a1, unsigned __int8 a2)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m5F;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned int v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int8 v_stack_mD4;
    unsigned __int8 v_stack_mD5;
    unsigned __int8 v_stack_mD6;
    unsigned int v_stack_mD8;
    unsigned int v_stack_mF8;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;

    v_stack_p10 = v_rbx;
    v_stack_p18 = v_rsi;
    v_stack_p20 = v_rdi;
    v_rsp = (v_rsp) - (208);
    result = 0;
    v_stack_mC0 = 0;
    v_stack_mA8 = v_xmm1;
    v_stack_m78 = 0;
    v_stack_m98 = v_xmm1;
    v_stack_m88 = v_xmm1;
    v_stack_mD0 = v_xmm0;
    v_r15 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 14371429))) & (0x20000ULL));
    v_r13 = 0;
    v_stack_mC8 = a1 + 96;
    v_stack_mD0 = 0;
    if ((*(unsigned int *)(v_rip + 14371922)) != 0) goto loc_002124AE;
loc_002120D4:
    v_stack_mC0 = (unsigned __int8)(v_cr8);
    if (((*(unsigned __int8 *)(v_rip + 14371371)) & (33)) != 0) goto loc_00212452;
loc_002120E5:
    if (v_stack_mD0 != 0) goto loc_00212C0D;
loc_002120F5:
loc_002120FB:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 64))) == 0) goto loc_0021218B;
    if (sign_flag) goto loc_00212AA7;
    result = ExpGetThreadResourceHint(*(unsigned __int64 *)(gs_base + (0 + 392)), v_stack_mD0, a3, (unsigned int)(*(unsigned int *)(a1 + 76)));
    if ((*(unsigned __int64 *)(a1 + 48)) == (*(unsigned __int64 *)(gs_base + (0 + 392)))) goto loc_00212A99;
    if (*(unsigned __int64 *)(a1 + 48) == 0) goto loc_00212BE5;
loc_00212143:
    if ((unsigned int)((unsigned int)((unsigned int)(result))) != 0) goto loc_0021247F;
loc_0021214C:
    a3 = ((unsigned int)(*(unsigned int *)(a1 + 72))) + ((unsigned int)(*(unsigned int *)(a1 + 64)));
    if (*(unsigned __int64 *)(a1 + 16) != 0) goto loc_002124BF;
loc_00212166:
    if (0 != 0) goto loc_00212180;
    if ((*(unsigned __int64 *)(a1 + 16)) >= 0) goto loc_00212823;
    if (*(unsigned __int64 *)(a1 + 16) == 0) goto loc_00212823;
loc_00212180:
    goto loc_0021252B;
loc_0021218B:
    result = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int64 *)(a1 + 16)))) + 1);
    *(unsigned __int16 *)(a1 + 24) = 1;
    *(unsigned int *)(a1 + 64) = (unsigned int)(result);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 56))) & (7));
    *(unsigned __int64 *)(a1 + 48) = *(unsigned __int64 *)(gs_base + (0 + 392));
    result = (unsigned int)((result) | (8));
    *(unsigned int *)(a1 + 56) = (unsigned int)(result);
    if (((*(unsigned __int8 *)(v_rip + 14371159)) & (1)) != 0) goto loc_00212246;
loc_002121B5:
    if (v_stack_mD0 != 0) goto loc_002121E5;
    if (v_stack_mD0 == v_stack_mD0) goto loc_00212261;
    result = KxWaitForLockChainValid(v_stack_mD0, *(unsigned __int64 *)(a1 + 16), a3, (unsigned int)(*(unsigned int *)(a1 + 76)));
loc_002121E5:
    v_stack_mD0 = 0;
    result = (unsigned __int8)((v_stack_mC8) ^ ((unsigned __int8)(v_stack_mC8)));
    if ((((unsigned __int8)(result)) & (4)) == 0) goto loc_00212261;
    a3 = (result + 8) >> (5);
    a3 = (unsigned int)((a3) & (127));
    result = KeDisableInterrupts(v_stack_mC8, *(unsigned __int64 *)(a1 + 16), a3, v_rip + 13695251);
    result = KiHaltOnAddressWakeEntireList(v_stack_mC8, 0, a3, v_rip + 13695251);
    if ((unsigned __int8)((unsigned __int8)(result)) == 0) goto loc_00212261;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) != 0) goto loc_00212C39;
loc_00212243:
    goto loc_00212261;
loc_00212246:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13614092))) != 0) goto loc_002121B5;
    result = KiReleaseQueuedSpinLockInstrumented(v_stack_mD0, v_stack_p0, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), v_rip + 13695251);
loc_00212261:
    if ((*(unsigned int *)(v_rip + 14371512)) != 0) {
        a1 = 2;
        a2 = (unsigned __int8)(v_stack_mC0);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), v_rip + 13695251);
    }
    if ((unsigned int)(v_r15) == 0) goto loc_0021242C;
    v_stack_mB8 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 68)));
    v_stack_mD8 = 0;
    a2 = (a2) << (32);
    result = ((unsigned int)(*(unsigned int *)(a1 + 68))) | (a2);
    v_stack_mD5 = 0;
    v_stack_mD8 = (unsigned __int16)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 208));
    v_stack_mD4 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 209));
    v_stack_mD6 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 209));
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1440))))) != 0) goto loc_0021242C;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1568) != 0) goto loc_00212358;
    result = ExAllocatePool2(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1568) + 72, 512, (unsigned int)(0x72546552ULL), v_rip + 13695251);
    if (result == 0) goto loc_0021242C;
    a4 = 0;
    *(unsigned __int64 *)(result + 16) = a1;
    *(unsigned __int64 *)(result + 28) = 0x10000ULL;
    *(unsigned int *)(result + 40) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12935525)));
    result = 0;
    if (condition_is_equal) goto loc_002123CE;
    a2 = 0;
    result = ExFreePoolWithTag(0, a2, result, a4);
loc_00212358:
    a4 = 0;
loc_00212361:
    if (0 >= 8) goto loc_0021239B;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(0 + 28)))) != 0x10000ULL) goto loc_0021237D;
    if ((*(unsigned __int64 *)(0 + 16)) != a1) goto loc_0021237D;
    if ((*(unsigned int *)(0 + 40)) == ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12935525))))) goto loc_002123C6;
loc_0021237D:
    if (0 != 0) goto loc_00212474;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(0 + 28))) == 0) goto loc_00212471;
    if ((*(unsigned int *)(0 + 40)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12935525))))) goto loc_00212474;
loc_0021239B:
    if (0 != 0) {
        *(unsigned __int64 *)(0 + 16) = a1;
        *(unsigned __int64 *)(0 + 28) = 0x10000ULL;
        *(unsigned int *)(0 + 36) = 0;
        *(unsigned __int64 *)(0) = 0;
        *(unsigned __int64 *)(0 + 8) = 0;
        *(unsigned int *)(0 + 24) = 0;
        *(unsigned int *)(0 + 40) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12935525)));
        *(unsigned int *)(0 + 44) = 0;
    }
    if (0 == 0) goto loc_0021242C;
loc_002123CE:
    *(unsigned __int64 *)(0 + 8) = result;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(0 + 32))) == 0) goto loc_00212841;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(0 + 32)))) != 4) goto loc_00212841;
    if ((*(unsigned __int16 *)(0 + 24)) != ((unsigned __int16)(v_stack_mD8))) goto loc_00212834;
    if ((*(unsigned __int8 *)(0 + 26)) != ((unsigned __int8)(v_stack_mD4))) goto loc_00212834;
    v_r12 = (result) - (*(unsigned __int64 *)(0));
    *(unsigned __int64 *)(0) = v_r12;
loc_00212411:
loc_00212416:
    *(unsigned int *)(0 + 32) = 1;
    *(unsigned int *)(0 + 36) = 1;
    *(unsigned int *)(0 + 44) = (unsigned int)((unsigned int)(v_stack_mB8));
    *(unsigned int *)(0 + 24) = (unsigned int)((unsigned int)(v_stack_mD8));
loc_0021242C:
    return 1;
loc_00212452:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13613568))) != 0) goto loc_002120E5;
    result = KiAcquireQueuedSpinLockInstrumented(v_stack_mD0, *(unsigned __int64 *)(v_stack_m28 + 72), 0, a4);
    goto loc_002120F5;
loc_00212471:
loc_00212474:
    v_rdi = (*(unsigned __int64 *)(v_stack_m28 + 72)) + (64);
    a2 = (unsigned int)((*(unsigned __int64 *)(v_stack_m28 + 72)) + 1);
    goto loc_00212361;
loc_0021247F:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 16) == 0) goto loc_0021214C;
    if (0 >= (*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 16) + 8))) goto loc_0021214C;
    a2 = (0) << (4);
    a2 = (a2) + (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 16));
    if ((*(unsigned __int64 *)(a2)) != (*(unsigned __int64 *)(gs_base + (0 + 392)))) goto loc_0021214C;
    goto loc_00212A99;
loc_002124AE:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(*(unsigned __int64 *)(v_stack_m28 + 64)), (unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 16)), 0, a4);
    goto loc_002120D4;
loc_002124BF:
    result = ((unsigned int)(*(unsigned int *)((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 16)) + 8))) << (4);
    result = (result) + ((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 16)));
    a2 = ((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 16))) + (16);
    if (((unsigned __int8)(*(unsigned __int64 *)(v_stack_m28 + 64))) >= 0) goto loc_00212166;
loc_002124D6:
    if ((*(unsigned __int64 *)(a2)) == (*(unsigned __int64 *)(gs_base + (0 + 392)))) goto loc_00212A81;
    if (*(unsigned __int64 *)(a2) == 0) goto loc_00212A5A;
    a1 = ((unsigned __int8)(*(unsigned __int64 *)(v_stack_m28 + 64))) + 1;
    if (a1 == 0) goto loc_00212BF6;
loc_002124F7:
    a2 = (a2) + (16);
    if (a2 != result) goto loc_002124D6;
    goto loc_00212166;
loc_00212505:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 16) == 0) goto loc_00212823;
    result = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 16) + 8))) << (4);
    result = (result) + (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 16));
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 16)) + (16);
loc_00212520:
    if ((*(unsigned __int64 *)(a2)) != ((unsigned int)(*(unsigned int *)(v_rip + 12935525)))) goto loc_00212816;
loc_0021252B:
    result = (unsigned int)(((unsigned int)(a2)) - (*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 16)));
    result = (result) >> (4);
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1120) = (unsigned __int8)(result);
loc_00212541:
    if ((*(unsigned __int64 *)(a2)) == (*(unsigned __int64 *)(gs_base + (0 + 392)))) goto loc_00212852;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 64))) == 0) goto loc_00212567;
    if (sign_flag) goto loc_00213251;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 76)) != ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12935525))))) goto loc_00213251;
loc_00212567:
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 24) = (unsigned __int16)(v_stack_m28);
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 64) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 64)) + 1);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 8))) & (7));
    *(unsigned __int64 *)(a2) = *(unsigned __int64 *)(gs_base + (0 + 392));
    result = (unsigned int)((result) | (8));
    *(unsigned int *)(a2 + 8) = (unsigned int)(result);
    if (((*(unsigned __int8 *)(v_rip + 14370174)) & (1)) != 0) goto loc_0021261F;
loc_0021258E:
    if (v_stack_mD0 != 0) goto loc_002125BE;
    if (v_stack_mD0 == v_stack_mD0) goto loc_0021263A;
    result = KxWaitForLockChainValid(v_stack_mD0, a2, 0, *(unsigned __int64 *)(a2));
loc_002125BE:
    v_stack_mD0 = (unsigned int)(*(unsigned int *)(v_rip + 12935525));
    result = (unsigned __int8)((v_stack_mC8) ^ ((unsigned __int8)(v_stack_mC8)));
    if ((((unsigned __int8)(result)) & (4)) == 0) goto loc_0021263A;
    a3 = (result + 8) >> (5);
    a3 = (unsigned int)((a3) & (127));
    result = KeDisableInterrupts(v_stack_mC8, a2, a3, v_rip + 13694266);
    result = KiHaltOnAddressWakeEntireList(v_stack_mC8, (unsigned int)(*(unsigned int *)(v_rip + 12935525)), a3, v_rip + 13694266);
    if ((unsigned __int8)((unsigned __int8)(result)) == 0) goto loc_0021263A;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) != 0) goto loc_00212C61;
loc_0021261C:
    goto loc_0021263A;
loc_0021261F:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13613107))) != 0) goto loc_0021258E;
    result = KiReleaseQueuedSpinLockInstrumented(v_stack_mD0, v_stack_p0, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), v_rip + 13694266);
loc_0021263A:
    if ((*(unsigned int *)(v_rip + 14370527)) != ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12935525))))) {
        a1 = v_stack_mC0;
        a2 = (unsigned __int8)(v_stack_mC0);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), v_rip + 13694266);
    }
    if ((unsigned int)(*(unsigned __int64 *)(gs_base + (0 + 32))) == 0) goto loc_00212800;
    v_stack_mB8 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 68)));
    v_stack_mD8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12935525)));
    a2 = (a2) << (32);
    result = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 68))) | (a2);
    v_stack_mD5 = 0;
    v_stack_mB0 = result;
    v_stack_mD8 = (unsigned __int16)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 208));
    v_stack_mD6 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 209));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1440)))) & (1)) != 0) goto loc_00212800;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1568) != 0) goto loc_00212734;
    result = ExAllocatePool2(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1568) + 72, 512, (unsigned int)(0x72546552ULL), v_rip + 13694266);
    if (result == 0) goto loc_00212800;
    a4 = 0;
    *(unsigned __int64 *)(result + 16) = *(unsigned __int64 *)(v_stack_m28 + 56);
    *(unsigned __int64 *)(result + 28) = 0x10000ULL;
    *(unsigned int *)(result + 40) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12934538)));
    result = 0;
    if (condition_is_equal) goto loc_00212849;
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, (unsigned int)(0x72546552ULL), a4);
loc_00212734:
    a4 = 0;
loc_0021273D:
    if (0 >= 8) goto loc_00212777;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(0 + 28)))) != 0x10000ULL) goto loc_00212759;
    if ((*(unsigned __int64 *)(0 + 16)) != (*(unsigned __int64 *)(v_stack_m28 + 56))) goto loc_00212759;
    if ((*(unsigned int *)(0 + 40)) == ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12934538))))) goto loc_002127A2;
loc_00212759:
    if (0 != 0) goto loc_0021280B;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(0 + 28))) == 0) goto loc_00212808;
    if ((*(unsigned int *)(0 + 40)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12934538))))) goto loc_0021280B;
loc_00212777:
    if (0 != 0) {
        *(unsigned __int64 *)(0 + 16) = *(unsigned __int64 *)(v_stack_m28 + 56);
        *(unsigned __int64 *)(0 + 28) = 0x10000ULL;
        *(unsigned int *)(0 + 36) = 0;
        *(unsigned __int64 *)(0) = 0;
        *(unsigned __int64 *)(0 + 8) = 0;
        *(unsigned int *)(0 + 24) = 0;
        *(unsigned int *)(0 + 40) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12934538)));
        *(unsigned int *)(0 + 44) = 0;
    }
    if (0 == 0) goto loc_00212800;
loc_002127AA:
    *(unsigned __int64 *)(0 + 8) = v_stack_mB0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(0 + 32))) == 0) goto loc_00212A79;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(0 + 32)))) != 4) goto loc_00212A79;
    if ((*(unsigned __int16 *)(0 + 24)) != ((unsigned __int16)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 208)))) goto loc_00212A6B;
    if ((*(unsigned __int8 *)(0 + 26)) != ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 209)))) goto loc_00212A6B;
    a3 = (v_stack_mB0) - (*(unsigned __int64 *)(0));
    *(unsigned __int64 *)(0) = a3;
loc_002127E3:
loc_002127E9:
    *(unsigned int *)(0 + 24) = (unsigned int)((unsigned int)(v_stack_mD8));
    *(unsigned int *)(0 + 44) = (unsigned int)((unsigned int)(v_stack_mB8));
    *(unsigned int *)(0 + 32) = 1;
    *(unsigned int *)(0 + 36) = 1;
loc_00212800:
    goto loc_0021242C;
loc_00212808:
loc_0021280B:
    v_rdi = (0) + (64);
    a1 = (unsigned int)((0) + 1);
    goto loc_0021273D;
loc_00212816:
    a2 = ((unsigned int)(*(unsigned int *)(0 + 28))) + (16);
    if (a2 != 0) goto loc_00212520;
loc_00212823:
    result = ExpExpandResourceOwnerTable(*(unsigned __int64 *)(v_stack_m28 + 56), v_stack_mD0, 1, a4);
    goto loc_002120F5;
loc_00212834:
    *(unsigned __int64 *)(1) = 1;
    goto loc_00212416;
loc_00212841:
    *(unsigned __int64 *)(1) = 0;
    goto loc_00212411;
loc_00212849:
    goto loc_002127AA;
loc_00212852:
    v_rsi = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_mD0 + 8))) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mD0 + 8)) + 8)));
    v_rsi = (unsigned int)((v_rsi) & (7));
    v_rsi = (unsigned int)((v_rsi) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mD0 + 8)) + 8)));
    *(unsigned int *)(v_stack_mD0 + 8) = (unsigned int)(v_rsi);
    v_rsi = (unsigned int)((v_rsi) >> (3));
    if (((*(unsigned __int8 *)(v_rip + 14369434)) & (1)) != 0) goto loc_002128B9;
loc_0021286E:
    if (v_stack_mD0 != 0) goto loc_0021289A;
    if (v_stack_mD0 == v_stack_mD0) goto loc_002128D0;
    result = KxWaitForLockChainValid(v_stack_mD0, v_stack_mD0, v_stack_mB0, a4);
loc_0021289A:
    v_stack_mD0 = *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 208);
    result = (unsigned __int8)((v_stack_mC8) ^ ((unsigned __int8)(v_stack_mC8)));
    if ((((unsigned __int8)(result)) & (4)) == 0) goto loc_002128D0;
    result = KeWakeAddressAll(result + 8, v_stack_mC8, v_stack_mB0, a4);
    goto loc_002128D0;
loc_002128B9:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13612441))) != 0) goto loc_0021286E;
    result = KiReleaseQueuedSpinLockInstrumented(v_stack_mD0, v_stack_p0, v_stack_mB0, a4);
loc_002128D0:
    if ((*(unsigned int *)(v_rip + 14369865)) != ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 208)))) {
        a1 = v_stack_mC0;
        a2 = (unsigned __int8)(v_stack_mC0);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, v_stack_mB0, a4);
    }
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12934538))) == 0) goto loc_00212A52;
    v_stack_mD5 = 0;
    v_stack_mD8 = (unsigned __int16)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 208));
    v_stack_mD6 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 209));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1440)))) & (1)) != 0) goto loc_00212A52;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1568) != 0) goto loc_002129AB;
    result = ExAllocatePool2(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1568) + 72, 512, (unsigned int)(0x72546552ULL), a4);
    if (result == 0) goto loc_00212A52;
    *(unsigned __int64 *)(result + 16) = *(unsigned __int64 *)(v_stack_m28 + 56);
    *(unsigned __int64 *)(result + 28) = 0x10000ULL;
    *(unsigned int *)(result + 40) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12933900)));
    result = 0;
    if (condition_is_equal) goto loc_00212C29;
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, (unsigned int)(0x72546552ULL), a4);
loc_002129AB:
    a1 = 0;
loc_002129AF:
    if (0 >= 8) goto loc_002129E9;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(0 + 28)))) != 0x10000ULL) goto loc_002129CB;
    if ((*(unsigned __int64 *)(0 + 16)) != (*(unsigned __int64 *)(v_stack_m28 + 56))) goto loc_002129CB;
    if ((*(unsigned int *)(0 + 40)) == ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12933900))))) goto loc_00212A13;
loc_002129CB:
    if (0 != 0) goto loc_00212C02;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(0 + 28))) == 0) goto loc_00212BFF;
    if ((*(unsigned int *)(0 + 40)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12933900))))) goto loc_00212C02;
loc_002129E9:
    if (0 == 0) goto loc_00212A13;
    a2 = 0;
    *(unsigned int *)(0 + 36) = 0;
    *(unsigned __int64 *)(0) = 0;
    *(unsigned __int64 *)(0 + 8) = 0;
    *(unsigned int *)(0 + 24) = 0;
    *(unsigned int *)(0 + 44) = 0;
loc_00212A03:
    *(unsigned int *)(0 + 40) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12933900)));
    *(unsigned __int64 *)(0 + 28) = 0x10000ULL;
    *(unsigned __int64 *)(0 + 16) = *(unsigned __int64 *)(v_stack_m28 + 56);
loc_00212A13:
    if (0 == 0) goto loc_00212A52;
loc_00212A1E:
    if ((*(unsigned int *)(0 + 32)) != 0) goto loc_0021341C;
    *(unsigned __int64 *)(0 + 8) = 2;
    *(unsigned __int64 *)(0) = 1;
    *(unsigned int *)(0 + 24) = (unsigned int)((unsigned int)(v_stack_mD8));
    *(unsigned int *)(0 + 44) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 68)));
loc_00212A4B:
    *(unsigned int *)(0 + 36) = (unsigned int)(v_rsi);
loc_00212A4E:
    *(unsigned int *)(0 + 32) = 1;
loc_00212A52:
    goto loc_0021242C;
loc_00212A5A:
    if (*(unsigned __int64 *)(a1 + 16) != 0) goto loc_002124F7;
    goto loc_002124F7;
loc_00212A6B:
    *(unsigned __int64 *)(0) = 1;
    goto loc_002127E9;
loc_00212A79:
    *(unsigned __int64 *)(0) = 0;
    goto loc_002127E3;
loc_00212A81:
    result = (unsigned int)((0) - (*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 16)));
    result = (result) >> (4);
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1120) = (unsigned __int8)(result);
loc_00212A99:
    if (0 == 0) goto loc_002120FB;
    goto loc_00212541;
loc_00212AA7:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 48)) != (*(unsigned __int64 *)(gs_base + (0 + 392)))) goto loc_00212505;
    v_rsi = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 56))) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 56)) + 8)));
    v_rsi = (unsigned int)((v_rsi) & (7));
    v_rsi = (unsigned int)((v_rsi) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 56)) + 8)));
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 56) = (unsigned int)(v_rsi);
    v_rsi = (unsigned int)((v_rsi) >> (3));
    result = KeReleaseInStackQueuedSpinLock(v_stack_mD0, 0, 1, a4);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12933900))) == 0) goto loc_00212A52;
    v_stack_mD5 = 0;
    v_stack_mD8 = (unsigned __int16)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 208));
    v_stack_mD6 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 209));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1440)))) & (1)) != 0) goto loc_00212A52;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1568) != 0) goto loc_00212B8A;
    result = ExAllocatePool2(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1568) + 72, 512, (unsigned int)(0x72546552ULL), a4);
    if (result == 0) goto loc_00212A52;
    *(unsigned __int64 *)(result + 16) = *(unsigned __int64 *)(v_stack_m28 + 56);
    *(unsigned __int64 *)(result + 28) = 0x10000ULL;
    *(unsigned int *)(result + 40) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12933421)));
    result = 0;
    if (condition_is_equal) goto loc_00212C31;
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, (unsigned int)(0x72546552ULL), a4);
loc_00212B8A:
    a1 = 0;
loc_00212B90:
    if (0 >= 8) goto loc_00212BC2;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(0 + 28)))) != 0x10000ULL) goto loc_00212BB0;
    if ((*(unsigned __int64 *)(0 + 16)) != (*(unsigned __int64 *)(v_stack_m28 + 56))) goto loc_00212BB0;
    if ((*(unsigned int *)(0 + 40)) == ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12933421))))) goto loc_00212A13;
loc_00212BB0:
    if (0 != 0) goto loc_00212C1E;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(0 + 28))) == 0) goto loc_00212C1B;
    if ((*(unsigned int *)(0 + 40)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12933421))))) goto loc_00212C1E;
loc_00212BC2:
    if (0 == 0) goto loc_00212A13;
    a1 = 0;
    *(unsigned int *)(0 + 36) = 0;
    *(unsigned __int64 *)(0) = 0;
    *(unsigned __int64 *)(0 + 8) = 0;
    *(unsigned int *)(0 + 24) = 0;
    *(unsigned int *)(0 + 44) = 0;
    goto loc_00212A03;
loc_00212BE5:
    if (0 != 0) goto loc_00212143;
    goto loc_00212143;
loc_00212BF6:
    a2 = (0) + (16);
    goto loc_00212166;
loc_00212BFF:
loc_00212C02:
    v_rdi = (0) + (64);
    a1 = (unsigned int)((a1) + 1);
    goto loc_002129AF;
loc_00212C0D:
    result = KxWaitForLockOwnerShip(v_stack_mD0, a2, (unsigned int)(0x72546552ULL), a4);
    goto loc_002120F5;
loc_00212C1B:
loc_00212C1E:
    v_rdi = (v_rdi) + (64);
    a2 = (unsigned int)((a2) + 1);
    goto loc_00212B90;
loc_00212C29:
    goto loc_00212A1E;
loc_00212C31:
    goto loc_00212A1E;
loc_00212C39:
loc_00212C40:
    if (condition_is_not_equal) goto loc_00212C40;
    if (condition_is_above_or_equal) goto loc_00212243;
    result = KiRemoveSystemWorkPriorityKick(v_stack_mD0, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(0x72546552ULL))))), (unsigned int)(0x72546552ULL), a4);
    goto loc_00212243;
loc_00212C61:
loc_00212C68:
    if (condition_is_not_equal) goto loc_00212C68;
    if (condition_is_above_or_equal) goto loc_0021261C;
    result = KiRemoveSystemWorkPriorityKick(v_stack_mD0, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(0x72546552ULL))))), (unsigned int)(0x72546552ULL), a4);
    goto loc_0021261C;
loc_00212C89:
    if ((*(unsigned int *)(v_rdi + 40)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 68))))) goto loc_002133C7;
loc_00212C96:
    if (v_rdi != 0) {
        *(unsigned __int64 *)(v_rdi + 16) = *(unsigned __int64 *)(v_stack_m28 + 56);
        *(unsigned __int64 *)(v_rdi + 28) = 0x10000ULL;
        *(unsigned int *)(v_rdi + 36) = (unsigned int)(*(unsigned __int64 *)(gs_base + (0 + 32)));
        *(unsigned __int64 *)(v_rdi) = *(unsigned __int64 *)(gs_base + (0 + 32));
        *(unsigned __int64 *)(v_rdi + 8) = *(unsigned __int64 *)(gs_base + (0 + 32));
        *(unsigned int *)(v_rdi + 24) = (unsigned int)(*(unsigned __int64 *)(gs_base + (0 + 32)));
        *(unsigned int *)(v_rdi + 40) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 68)));
        *(unsigned int *)(v_rdi + 44) = (unsigned int)(*(unsigned __int64 *)(gs_base + (0 + 32)));
    }
    if (v_rdi == 0) goto loc_0021342D;
loc_00212CCD:
    *(unsigned __int64 *)(v_rdi) = v_stack_mB0;
    *(unsigned int *)(v_rdi + 24) = (unsigned int)((unsigned int)(v_stack_mD8));
    *(unsigned int *)(v_rdi + 32) = 4;
loc_00212CE8:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1440))) >> (9));
    a1 = (unsigned int)((a1) & (7));
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544) + 672);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544) + 672) != 0) {
        result = *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544) + 672) + 1084);
        if (((unsigned int)(a1)) >= ((unsigned int)(result))) { a1 = (unsigned int)(result); }
    }
    if (((unsigned int)(a1)) < 2) goto loc_00213184;
loc_00212D28:
    if (((unsigned int)(a1)) >= = 1) {
        a2 = (unsigned int)((unsigned int)(*(unsigned __int64 *)(gs_base + (0 + 32))));
        if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 26)) & (4)) == 0) { a2 = 4; }
    }
    a1 = (unsigned int)(((unsigned int)(a2)) | (2));
    if ((((unsigned __int8)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 26))) & (2)) != 0) { a1 = a2; }
    a4 = (unsigned int)((*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 26)) >> (8));
    a2 = (unsigned int)(((unsigned int)((unsigned int)(a1))) | (0xFF00ULL));
    if (((unsigned int)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 195)))) <= ((unsigned int)(a4))) { a2 = (unsigned int)(a1); }
    result = (__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 195));
    if (a2 != 0) {
        a1 = *(unsigned __int64 *)(v_stack_m28 + 56);
        result = ExpApplyPriorityBoost(a1, a2, *(unsigned __int64 *)(gs_base + (0 + 392)), a4);
    }
    result = ExpWaitForResource(*(unsigned __int64 *)(v_stack_m28 + 56), v_stack_mA8, (unsigned int)(0x10244ULL), a4);
    if ((((unsigned __int8)(*(unsigned __int64 *)(gs_base + (0 + 392)))) & (3)) != 0) goto loc_0021317C;
loc_00212D8F:
    result = 0;
    v_stack_m60 = 0;
    v_stack_m70 = v_xmm0;
    if ((((unsigned __int8)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 26))) & (8)) != 0) goto loc_00212EEE;
    if ((((unsigned __int8)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 26))) & (4)) == 0) goto loc_00212DE0;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1440))) >> (9));
    a1 = (unsigned int)((a1) & (7));
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544) + 672);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544) + 672) != 0) {
        result = *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544) + 672) + 1084);
        if (((unsigned int)(a1)) >= ((unsigned int)(result))) { a1 = (unsigned int)(result); }
    }
    a2 = (unsigned int)((unsigned int)(*(unsigned __int64 *)(gs_base + (0 + 32))));
    if (((unsigned int)(a1)) < 2) { a2 = 4; }
loc_00212DE0:
    v_rsi = (unsigned int)(((unsigned int)(a2)) | (2));
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 26)) & (2)) == 0) { v_rsi = a2; }
    if ((unsigned int)(v_rsi) == 0) goto loc_00212EEE;
    v_stack_m70 = *(unsigned __int64 *)(gs_base + (0 + 32));
    v_stack_m68 = *(unsigned __int64 *)(v_stack_m28 + 56) + 96;
    if ((*(unsigned int *)(v_rip + 14368523)) != 0) goto loc_0021314E;
loc_00212E1B:
    v_stack_m60 = (unsigned __int8)(v_stack_mC0);
    if (((*(unsigned __int8 *)(v_rip + 14367972)) & (33)) != 0) goto loc_002130A3;
loc_00212E2C:
    if (v_stack_m70 != 0) goto loc_002131A9;
loc_00212E3C:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 48)) == (*(unsigned __int64 *)(gs_base + (0 + 392)))) goto loc_00212E77;
    a4 = 0;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 48) != 0) ? 1 : 0;
    if ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1120)) != 0) goto loc_002130C2;
loc_00212E5E:
    a2 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 72))) + ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 64)));
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 16) != 0) goto loc_0021310F;
loc_00212E74:
loc_00212E77:
    if ((((unsigned __int8)(v_rsi)) & (4)) != 0) goto loc_002131B7;
loc_00212E81:
    if ((((unsigned __int8)(v_rsi)) & (2)) == 0) goto loc_00212EBB;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(0 + 8)))) & (4)) != 0) goto loc_00213107;
    result = (unsigned int)((1) + 1);
    if (((unsigned int)(result)) != 1) goto loc_00212EB7;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 792)) != 0) goto loc_002131DF;
loc_00212EB7:
loc_00212EBB:
    result = KeReleaseInStackQueuedSpinLock(v_stack_m70, a2, (unsigned int)(0x10244ULL), a4);
    if ((unsigned int)(v_rsi) == 0) goto loc_00212EEB;
    if ((((unsigned __int8)(v_rsi)) & (4)) != 0) {
        a3 = 0;
        a1 = *(unsigned __int64 *)(gs_base + (0 + 392));
        a2 = a3 + 2;
        result = IoBoostThreadIoPriority(a1, a2, a3, a4);
    }
    if ((((unsigned __int8)(v_rsi)) & (2)) != 0) {
        a1 = *(unsigned __int64 *)(gs_base + (0 + 392));
        result = PsBoostThreadOutstandingIoQoS(a1, a2, a3, a4);
    }
    v_r13 = 0;
loc_00212EEE:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12933421))) == 0) goto loc_0021308D;
    v_stack_mB8 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 68)));
    v_stack_mD8 = 0;
    a2 = (a2) << (32);
    result = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 68))) | (a2);
    v_stack_mD5 = 0;
    v_stack_mD8 = (unsigned __int16)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 208));
    v_stack_mD6 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 209));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1440)))) & (1)) != 0) goto loc_0021308D;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1568) != 0) goto loc_00212FBD;
    result = ExAllocatePool2(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1568) + 72, 512, (unsigned int)(0x72546552ULL), a4);
    if (result == 0) goto loc_0021308D;
    a3 = 0;
    *(unsigned __int64 *)(result + 16) = *(unsigned __int64 *)(v_stack_m28 + 56);
    *(unsigned __int64 *)(result + 28) = 0x10000ULL;
    *(unsigned int *)(result + 40) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12932345)));
    result = 0;
    if (condition_is_equal) goto loc_00213033;
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, a3, a4);
loc_00212FBD:
    a3 = 0;
loc_00212FC6:
    if (0 >= 8) goto loc_00213000;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(0 + 28)))) != 0x10000ULL) goto loc_00212FE2;
    if ((*(unsigned __int64 *)(0 + 16)) != (*(unsigned __int64 *)(v_stack_m28 + 56))) goto loc_00212FE2;
    if ((*(unsigned int *)(0 + 40)) == ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12932345))))) goto loc_0021302B;
loc_00212FE2:
    if (0 != 0) goto loc_00213098;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(0 + 28))) == 0) goto loc_00213095;
    if ((*(unsigned int *)(0 + 40)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12932345))))) goto loc_00213098;
loc_00213000:
    if (0 != 0) {
        *(unsigned __int64 *)(0 + 16) = *(unsigned __int64 *)(v_stack_m28 + 56);
        *(unsigned __int64 *)(0 + 28) = 0x10000ULL;
        *(unsigned int *)(0 + 36) = 0;
        *(unsigned __int64 *)(0) = 0;
        *(unsigned __int64 *)(0 + 8) = 0;
        *(unsigned int *)(0 + 24) = 0;
        *(unsigned int *)(0 + 40) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12932345)));
        *(unsigned int *)(0 + 44) = 0;
    }
    if (0 == 0) goto loc_0021308D;
loc_00213033:
    *(unsigned __int64 *)(0 + 8) = result;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(0 + 32))) == 0) goto loc_002130FF;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(0 + 32)))) != 4) goto loc_002130FF;
    if ((*(unsigned __int16 *)(0 + 24)) != ((unsigned __int16)(v_stack_mD8))) goto loc_002130F1;
    if ((*(unsigned __int8 *)(0 + 26)) != ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 209)))) goto loc_002130F1;
    v_r14 = (result) - (*(unsigned __int64 *)(0));
    *(unsigned __int64 *)(0) = v_r14;
loc_00213070:
loc_00213076:
    *(unsigned int *)(0 + 24) = (unsigned int)((unsigned int)(v_stack_mD8));
    *(unsigned int *)(0 + 44) = (unsigned int)((unsigned int)(v_stack_mB8));
    *(unsigned int *)(0 + 32) = 1;
    *(unsigned int *)(0 + 36) = 1;
loc_0021308D:
    goto loc_0021242C;
loc_00213095:
loc_00213098:
    v_rdi = (0) + (64);
    a2 = (unsigned int)((0) + 1);
    goto loc_00212FC6;
loc_002130A3:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13610415))) != 0) goto loc_00212E2C;
    result = KiAcquireQueuedSpinLockInstrumented(v_stack_m70, v_rdi, 1, a4);
    goto loc_00212E3C;
loc_002130C2:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 16) == 0) goto loc_00212E5E;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12932345)))) >= (*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 16) + 8))) goto loc_00212E5E;
    v_rdi = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12932345))))) << (4);
    v_rdi = (v_rdi) + (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 16));
    if ((*(unsigned __int64 *)(v_rdi)) != v_r14) goto loc_00212E5E;
    goto loc_00212E77;
loc_002130F1:
    *(unsigned __int64 *)(v_stack_m70) = 1;
    goto loc_00213076;
loc_002130FF:
    *(unsigned __int64 *)(v_stack_m70) = 1;
    goto loc_00213070;
loc_00213107:
    v_rsi = (unsigned int)((1) & (0xFFFFFFFDULL));
    goto loc_00212EBB;
loc_0021310F:
    a3 = ((unsigned int)(*(unsigned int *)(v_rdi + 8))) << (4);
    a3 = (a3) + (v_rdi);
    v_rdi = (v_rdi) + (16);
    if (v_stack_m70 >= v_rdi) goto loc_00212E74;
loc_00213127:
    if ((*(unsigned __int64 *)(v_rdi)) == v_r14) goto loc_0021315F;
    if (*(unsigned __int64 *)(v_rdi) == 0) goto loc_00213140;
    a1 = (v_stack_m70) + 1;
    if (a1 == v_rdi) goto loc_00212E74;
loc_00213140:
    v_rdi = (v_rdi) + (16);
    if (v_rdi != a3) goto loc_00213127;
    goto loc_00212E74;
loc_0021314E:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 209)), (unsigned __int8)(*(unsigned __int64 *)(v_rdi)), a3, a4);
    goto loc_00212E1B;
loc_0021315F:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) - (*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 16)));
    result = (result) >> (4);
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1120) = (unsigned __int8)(result);
    goto loc_00212E77;
loc_0021317C:
    goto loc_00212D8F;
loc_00213184:
    if (a3 != (*(unsigned __int64 *)(gs_base + (0 + 392)))) goto loc_00212D28;
    if ((*(unsigned int *)(a3 + 1504)) == 0) goto loc_00212D28;
    goto loc_00212D2D;
loc_002131A9:
    result = KxWaitForLockOwnerShip(v_stack_m70, (unsigned __int8)(*(unsigned __int64 *)(v_rdi)), a3, a4);
    goto loc_00212E3C;
loc_002131B7:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rdi + 8)))) & (1)) != 0) goto loc_002131D7;
    a4 = 0;
    a3 = 0;
    a2 = 0;
    result = PsBoostThreadIoEx(v_r14, a2, a3, a4);
    goto loc_00212E81;
loc_002131D7:
    v_rsi = (unsigned int)((v_rsi) & (0xFFFFFFFBULL));
    goto loc_00212E81;
loc_002131DF:
    if ((*(unsigned int *)(v_rip + 14367533)) != 0) goto loc_00213243;
loc_002131F5:
    result = KiAbThreadInsertList(v_r14, *(unsigned __int64 *)(gs_base + (0 + 32)) + 37240, v_r14 + 808, a4);
    if ((unsigned int)(result) != 0) {
        a1 = *(unsigned __int64 *)(gs_base + (0 + 32));
        result = KiAbQueueAutoBoostDpc(a1, *(unsigned __int64 *)(gs_base + (0 + 32)) + 37240, v_r14 + 808, a4);
    }
    if ((*(unsigned int *)(v_rip + 14367481)) != 0) {
        a1 = 2;
        a2 = 2;
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, v_r14 + 808, a4);
    }
    goto loc_00212EB7;
loc_00213243:
    result = KiRaiseIrqlProcessIrqlFlags(2, 2, v_r14 + 808, a4);
    goto loc_002131F5;
loc_00213251:
    if (2 == 0) goto loc_002133CF;
    *(unsigned __int64 *)(2) = v_r14;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(2 + 8))) & (7));
    result = (unsigned int)((result) | (8));
    *(unsigned int *)(2 + 8) = (unsigned int)(result);
    v_stack_m80 = v_stack_m88;
    v_stack_m88 = v_stack_m88;
    v_stack_mA0 = *(unsigned __int64 *)(gs_base + (0 + 32));
    v_stack_m90 = 0x60001ULL;
    v_stack_m98 = v_r14;
    v_stack_m78 = *(unsigned __int64 *)(gs_base + (0 + 32));
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 32) != 0) goto loc_002133F0;
    v_stack_mA0 = v_stack_mA8;
    v_stack_mA8 = v_stack_mA8;
loc_002132AD:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 32) = v_stack_mA8;
    result = KeReleaseInStackQueuedSpinLock(v_stack_mD0, 2, v_r14 + 808, a4);
    if ((unsigned int)(*(unsigned __int64 *)(gs_base + (0 + 32))) == 0) goto loc_00212CE8;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    v_stack_m38 = v_xmm0;
    a2 = (2) << (32);
    result = (result) | (a2);
    v_stack_mD5 = (unsigned __int8)(*(unsigned __int64 *)(gs_base + (0 + 32)));
    v_stack_mB0 = result;
    v_stack_mD8 = (unsigned __int16)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 208));
    v_stack_mD6 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 209));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1440)))) & (1)) != 0) goto loc_00213437;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1568) != 0) goto loc_0021338A;
    result = ExAllocatePool2(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1568) + 72, 512, (unsigned int)(0x72546552ULL), a4);
    if (result == 0) goto loc_0021342A;
    *(unsigned __int64 *)(result + 16) = *(unsigned __int64 *)(v_stack_m28 + 56);
    *(unsigned __int64 *)(result + 28) = 0x10000ULL;
    *(unsigned int *)(result + 40) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12931369)));
    result = 0;
    if (condition_is_equal) goto loc_002133E8;
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, (unsigned int)(0x72546552ULL), a4);
loc_0021338A:
    v_r13 = 0;
loc_00213393:
    if (0 >= 8) goto loc_00212C96;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(0 + 28)))) != 0x10000ULL) goto loc_002133B7;
    if ((*(unsigned __int64 *)(0 + 16)) != (*(unsigned __int64 *)(v_stack_m28 + 56))) goto loc_002133B7;
    if ((*(unsigned int *)(0 + 40)) == ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12931369))))) goto loc_00212CC1;
loc_002133B7:
    if (0 != 0) goto loc_002133C7;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(0 + 28))) != 0) goto loc_00212C89;
loc_002133C7:
    v_rdi = (0) + (64);
    a2 = (unsigned int)((0) + 1);
    goto loc_00213393;
loc_002133CF:
    result = KeReleaseInStackQueuedSpinLock(v_stack_mD0, a2, (unsigned int)(0x72546552ULL), a4);
    v_rsi = 0;
    goto loc_0021242C;
loc_002133E8:
    v_r13 = 0;
    goto loc_00212CCD;
loc_002133F0:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8))) != result) {
        a1 = 3;
    }
    v_stack_mA0 = a1;
    v_stack_mA8 = result;
    *(unsigned __int64 *)(a1) = v_stack_mA8;
    *(unsigned __int64 *)(result + 8) = v_stack_mA8;
    goto loc_002132AD;
loc_0021341C:
    if ((*(unsigned int *)(v_stack_mA8 + 36)) >= 0) goto loc_00212A4E;
    goto loc_00212A4B;
loc_0021342A:
    v_r13 = 0;
loc_0021342D:
    goto loc_00212CE8;
loc_00213437:
    v_r13 = 0;
    goto loc_00212CE8;
}
```

## 5. (Beta) C Style

```c
int64_t ExpAcquireResourceSharedLite(void *Arg1, uint8_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_m48;
    uint64_t v_stack_m58;
    uint64_t v_stack_m5F;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint32_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint8_t v_stack_mD4;
    uint8_t v_stack_mD5;
    uint8_t v_stack_mD6;
    uint32_t v_stack_mD8;
    uint32_t v_stack_mF8;
    uint64_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;

    v_stack_p10 = local_rbx;
    v_stack_p18 = local_rsi;
    v_stack_p20 = local_rdi;
    local_rsp = (local_rsp) - (208);
    result = 0;
    v_stack_mC0 = 0;
    v_stack_mA8 = v_xmm1;
    v_stack_m78 = 0;
    v_stack_m98 = v_xmm1;
    v_stack_m88 = v_xmm1;
    v_stack_mD0 = v_xmm0;
    local_r15 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xDB4A65))) & (0x20000ULL));
    local_r13 = 0;
    v_stack_mC8 = Arg1 + 96;
    v_stack_mD0 = 0;
    if ((*(uint32_t *)(v_rip + 0xDB4C52)) != 0) goto loc_002124AE;
loc_002120D4:
    v_stack_mC0 = (uint8_t)(v_cr8);
    if (((*(uint8_t *)(v_rip + 0xDB4A2B)) & (33)) != 0) goto loc_00212452;
loc_002120E5:
    if (v_stack_mD0 != 0) goto loc_00212C0D;
loc_002120F5:
loc_002120FB:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x40))) == 0) goto loc_0021218B;
    if (sign_flag) goto loc_00212AA7;
    result = ExpGetThreadResourceHint(*(uint64_t *)(gs_base + (0 + 0x188)), v_stack_mD0, a3, (uint32_t)(*(uint32_t *)(arg1 + 0x4C)));
    if ((*(uint64_t *)(arg1 + 0x30)) == (*(uint64_t *)(gs_base + (0 + 0x188)))) goto loc_00212A99;
    if (*(uint64_t *)(arg1 + 0x30) == 0) goto loc_00212BE5;
loc_00212143:
    if ((uint32_t)((uint32_t)((uint32_t)(result))) != 0) goto loc_0021247F;
loc_0021214C:
    a3 = ((uint32_t)(*(uint32_t *)(arg1 + 0x48))) + ((uint32_t)(*(uint32_t *)(arg1 + 0x40)));
    if (*(uint64_t *)(arg1 + 0x10) != 0) goto loc_002124BF;
loc_00212166:
    if (0 != 0) goto loc_00212180;
    if ((*(uint64_t *)(arg1 + 0x10)) >= 0) goto loc_00212823;
    if (*(uint64_t *)(arg1 + 0x10) == 0) goto loc_00212823;
loc_00212180:
    goto loc_0021252B;
loc_0021218B:
    result = (uint32_t)(((uint32_t)((uint32_t)(*(uint64_t *)(arg1 + 0x10)))) + 1);
    *(uint16_t *)(arg1 + 0x18) = 1;
    *(uint32_t *)(arg1 + 0x40) = (uint32_t)(result);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x38))) & (7));
    *(uint64_t *)(arg1 + 0x30) = *(uint64_t *)(gs_base + (0 + 0x188));
    result = (uint32_t)((result) | (8));
    *(uint32_t *)(arg1 + 0x38) = (uint32_t)(result);
    if (((*(uint8_t *)(v_rip + 0xDB4957)) & (1)) != 0) goto loc_00212246;
loc_002121B5:
    if (v_stack_mD0 != 0) goto loc_002121E5;
    if (v_stack_mD0 == v_stack_mD0) goto loc_00212261;
    result = KxWaitForLockChainValid(v_stack_mD0, *(uint64_t *)(arg1 + 0x10), a3, (uint32_t)(*(uint32_t *)(arg1 + 0x4C)));
loc_002121E5:
    v_stack_mD0 = 0;
    result = (uint8_t)((v_stack_mC8) ^ ((uint8_t)(v_stack_mC8)));
    if ((((uint8_t)(result)) & (4)) == 0) goto loc_00212261;
    a3 = (result + 8) >> (5);
    a3 = (uint32_t)((a3) & (127));
    result = KeDisableInterrupts(v_stack_mC8, *(uint64_t *)(arg1 + 0x10), a3, v_rip + 13695251);
    result = KiHaltOnAddressWakeEntireList(v_stack_mC8, 0, a3, v_rip + 13695251);
    if ((uint8_t)((uint8_t)(result)) == 0) goto loc_00212261;
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) != 0) goto loc_00212C39;
loc_00212243:
    goto loc_00212261;
loc_00212246:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCFBC0C))) != 0) goto loc_002121B5;
    result = KiReleaseQueuedSpinLockInstrumented(v_stack_mD0, v_stack_p0, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), v_rip + 13695251);
loc_00212261:
    if ((*(uint32_t *)(v_rip + 0xDB4AB8)) != 0) {
        Arg1 = 2;
        Arg2 = (uint8_t)(v_stack_mC0);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), v_rip + 13695251);
    }
    if ((uint32_t)(local_r15) == 0) goto loc_0021242C;
    v_stack_mB8 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x44)));
    v_stack_mD8 = 0;
    Arg2 = (Arg2) << (32);
    result = ((uint32_t)(*(uint32_t *)(arg1 + 0x44))) | (Arg2);
    v_stack_mD5 = 0;
    v_stack_mD8 = (uint16_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xD0));
    v_stack_mD4 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xD1));
    v_stack_mD6 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xD1));
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5A0))))) != 0) goto loc_0021242C;
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x620) != 0) goto loc_00212358;
    result = ExAllocatePool2(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x620) + 72, 512, (uint32_t)(0x72546552ULL), v_rip + 13695251);
    if (result == 0) goto loc_0021242C;
    a4 = 0;
    *(void **)(result + 0x10) = Arg1;
    *(uint64_t *)(result + 0x1C) = 0x10000ULL;
    *(uint32_t *)(result + 0x28) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC56165)));
    result = 0;
    if (condition_is_equal) goto loc_002123CE;
    Arg2 = 0;
    result = ExFreePoolWithTag(0, Arg2, result, a4);
loc_00212358:
    a4 = 0;
loc_00212361:
    if (0 >= 8) goto loc_0021239B;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x1C)))) != 0x10000ULL) goto loc_0021237D;
    if ((*(uint64_t *)(0 + 0x10)) != Arg1) goto loc_0021237D;
    if ((*(uint32_t *)(0 + 0x28)) == ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC56165))))) goto loc_002123C6;
loc_0021237D:
    if (0 != 0) goto loc_00212474;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x1C))) == 0) goto loc_00212471;
    if ((*(uint32_t *)(0 + 0x28)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC56165))))) goto loc_00212474;
loc_0021239B:
    if (0 != 0) {
        *(void **)(0 + 0x10) = Arg1;
        *(uint64_t *)(0 + 0x1C) = 0x10000ULL;
        *(uint32_t *)(0 + 0x24) = 0;
        *(uint64_t *)(0) = 0;
        *(uint64_t *)(0 + 0x8) = 0;
        *(uint32_t *)(0 + 0x18) = 0;
        *(uint32_t *)(0 + 0x28) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC56165)));
        *(uint32_t *)(0 + 0x2C) = 0;
    }
    if (0 == 0) goto loc_0021242C;
loc_002123CE:
    *(uint64_t *)(0 + 0x8) = result;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x20))) == 0) goto loc_00212841;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x20)))) != 4) goto loc_00212841;
    if ((*(uint16_t *)(0 + 0x18)) != ((uint16_t)(v_stack_mD8))) goto loc_00212834;
    if ((*(uint8_t *)(0 + 0x1A)) != ((uint8_t)(v_stack_mD4))) goto loc_00212834;
    local_r12 = (result) - (*(uint64_t *)(0));
    *(uint64_t *)(0) = local_r12;
loc_00212411:
loc_00212416:
    *(uint32_t *)(0 + 0x20) = 1;
    *(uint32_t *)(0 + 0x24) = 1;
    *(uint32_t *)(0 + 0x2C) = (uint32_t)((uint32_t)(v_stack_mB8));
    *(uint32_t *)(0 + 0x18) = (uint32_t)((uint32_t)(v_stack_mD8));
loc_0021242C:
    return 1;
loc_00212452:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCFBA00))) != 0) goto loc_002120E5;
    result = KiAcquireQueuedSpinLockInstrumented(v_stack_mD0, *(uint64_t *)(v_stack_m28 + 0x48), 0, a4);
    goto loc_002120F5;
loc_00212471:
loc_00212474:
    local_rdi = (*(uint64_t *)(v_stack_m28 + 0x48)) + (64);
    Arg2 = (uint32_t)((*(uint64_t *)(v_stack_m28 + 0x48)) + 1);
    goto loc_00212361;
loc_0021247F:
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x10) == 0) goto loc_0021214C;
    if (0 >= (*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x10) + 0x8))) goto loc_0021214C;
    Arg2 = (0) << (4);
    Arg2 = (Arg2) + (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x10));
    if ((*(uint64_t *)(Arg2)) != (*(uint64_t *)(gs_base + (0 + 0x188)))) goto loc_0021214C;
    goto loc_00212A99;
loc_002124AE:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(*(uint64_t *)(v_stack_m28 + 0x40)), (uint8_t)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x10)), 0, a4);
    goto loc_002120D4;
loc_002124BF:
    result = ((uint32_t)(*(uint32_t *)((uint8_t)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x10)) + 0x8))) << (4);
    result = (result) + ((uint8_t)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x10)));
    Arg2 = ((uint8_t)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x10))) + (16);
    if (((uint8_t)(*(uint64_t *)(v_stack_m28 + 0x40))) >= 0) goto loc_00212166;
loc_002124D6:
    if ((*(uint64_t *)(Arg2)) == (*(uint64_t *)(gs_base + (0 + 0x188)))) goto loc_00212A81;
    if (*(uint64_t *)(Arg2) == 0) goto loc_00212A5A;
    Arg1 = ((uint8_t)(*(uint64_t *)(v_stack_m28 + 0x40))) + 1;
    if (Arg1 == NULL) goto loc_00212BF6;
loc_002124F7:
    Arg2 = (Arg2) + (16);
    if (Arg2 != result) goto loc_002124D6;
    goto loc_00212166;
loc_00212505:
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x10) == 0) goto loc_00212823;
    result = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x10) + 0x8))) << (4);
    result = (result) + (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x10));
    Arg2 = (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x10)) + (16);
loc_00212520:
    if ((*(uint64_t *)(Arg2)) != ((uint32_t)(*(uint32_t *)(v_rip + 0xC56165)))) goto loc_00212816;
loc_0021252B:
    result = (uint32_t)(((uint32_t)(Arg2)) - (*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x10)));
    result = (result) >> (4);
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x460) = (uint8_t)(result);
loc_00212541:
    if ((*(uint64_t *)(Arg2)) == (*(uint64_t *)(gs_base + (0 + 0x188)))) goto loc_00212852;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x40))) == 0) goto loc_00212567;
    if (sign_flag) goto loc_00213251;
    if ((*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x4C)) != ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC56165))))) goto loc_00213251;
loc_00212567:
    *(uint16_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x18) = (uint16_t)(v_stack_m28);
    *(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x40) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x40)) + 1);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg2 + 0x8))) & (7));
    *(uint64_t *)(Arg2) = *(uint64_t *)(gs_base + (0 + 0x188));
    result = (uint32_t)((result) | (8));
    *(uint32_t *)(Arg2 + 0x8) = (uint32_t)(result);
    if (((*(uint8_t *)(v_rip + 0xDB457E)) & (1)) != 0) goto loc_0021261F;
loc_0021258E:
    if (v_stack_mD0 != 0) goto loc_002125BE;
    if (v_stack_mD0 == v_stack_mD0) goto loc_0021263A;
    result = KxWaitForLockChainValid(v_stack_mD0, Arg2, 0, *(uint64_t *)(Arg2));
loc_002125BE:
    v_stack_mD0 = (uint32_t)(*(uint32_t *)(v_rip + 0xC56165));
    result = (uint8_t)((v_stack_mC8) ^ ((uint8_t)(v_stack_mC8)));
    if ((((uint8_t)(result)) & (4)) == 0) goto loc_0021263A;
    a3 = (result + 8) >> (5);
    a3 = (uint32_t)((a3) & (127));
    result = KeDisableInterrupts(v_stack_mC8, Arg2, a3, v_rip + 13694266);
    result = KiHaltOnAddressWakeEntireList(v_stack_mC8, (uint32_t)(*(uint32_t *)(v_rip + 0xC56165)), a3, v_rip + 13694266);
    if ((uint8_t)((uint8_t)(result)) == 0) goto loc_0021263A;
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) != 0) goto loc_00212C61;
loc_0021261C:
    goto loc_0021263A;
loc_0021261F:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCFB833))) != 0) goto loc_0021258E;
    result = KiReleaseQueuedSpinLockInstrumented(v_stack_mD0, v_stack_p0, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), v_rip + 13694266);
loc_0021263A:
    if ((*(uint32_t *)(v_rip + 0xDB46DF)) != ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC56165))))) {
        Arg1 = v_stack_mC0;
        Arg2 = (uint8_t)(v_stack_mC0);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), v_rip + 13694266);
    }
    if ((uint32_t)(*(uint64_t *)(gs_base + (0 + 0x20))) == 0) goto loc_00212800;
    v_stack_mB8 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x44)));
    v_stack_mD8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC56165)));
    Arg2 = (Arg2) << (32);
    result = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x44))) | (Arg2);
    v_stack_mD5 = 0;
    v_stack_mB0 = result;
    v_stack_mD8 = (uint16_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xD0));
    v_stack_mD6 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xD1));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5A0)))) & (1)) != 0) goto loc_00212800;
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x620) != 0) goto loc_00212734;
    result = ExAllocatePool2(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x620) + 72, 512, (uint32_t)(0x72546552ULL), v_rip + 13694266);
    if (result == 0) goto loc_00212800;
    a4 = 0;
    *(uint64_t *)(result + 0x10) = *(uint64_t *)(v_stack_m28 + 0x38);
    *(uint64_t *)(result + 0x1C) = 0x10000ULL;
    *(uint32_t *)(result + 0x28) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC55D8A)));
    result = 0;
    if (condition_is_equal) goto loc_00212849;
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, (uint32_t)(0x72546552ULL), a4);
loc_00212734:
    a4 = 0;
loc_0021273D:
    if (0 >= 8) goto loc_00212777;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x1C)))) != 0x10000ULL) goto loc_00212759;
    if ((*(uint64_t *)(0 + 0x10)) != (*(uint64_t *)(v_stack_m28 + 0x38))) goto loc_00212759;
    if ((*(uint32_t *)(0 + 0x28)) == ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC55D8A))))) goto loc_002127A2;
loc_00212759:
    if (0 != 0) goto loc_0021280B;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x1C))) == 0) goto loc_00212808;
    if ((*(uint32_t *)(0 + 0x28)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC55D8A))))) goto loc_0021280B;
loc_00212777:
    if (0 != 0) {
        *(uint64_t *)(0 + 0x10) = *(uint64_t *)(v_stack_m28 + 0x38);
        *(uint64_t *)(0 + 0x1C) = 0x10000ULL;
        *(uint32_t *)(0 + 0x24) = 0;
        *(uint64_t *)(0) = 0;
        *(uint64_t *)(0 + 0x8) = 0;
        *(uint32_t *)(0 + 0x18) = 0;
        *(uint32_t *)(0 + 0x28) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC55D8A)));
        *(uint32_t *)(0 + 0x2C) = 0;
    }
    if (0 == 0) goto loc_00212800;
loc_002127AA:
    *(uint64_t *)(0 + 0x8) = v_stack_mB0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x20))) == 0) goto loc_00212A79;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x20)))) != 4) goto loc_00212A79;
    if ((*(uint16_t *)(0 + 0x18)) != ((uint16_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xD0)))) goto loc_00212A6B;
    if ((*(uint8_t *)(0 + 0x1A)) != ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xD1)))) goto loc_00212A6B;
    a3 = (v_stack_mB0) - (*(uint64_t *)(0));
    *(uint64_t *)(0) = a3;
loc_002127E3:
loc_002127E9:
    *(uint32_t *)(0 + 0x18) = (uint32_t)((uint32_t)(v_stack_mD8));
    *(uint32_t *)(0 + 0x2C) = (uint32_t)((uint32_t)(v_stack_mB8));
    *(uint32_t *)(0 + 0x20) = 1;
    *(uint32_t *)(0 + 0x24) = 1;
loc_00212800:
    goto loc_0021242C;
loc_00212808:
loc_0021280B:
    local_rdi = (0) + (64);
    Arg1 = (uint32_t)((0) + 1);
    goto loc_0021273D;
loc_00212816:
    Arg2 = ((uint32_t)(*(uint32_t *)(0 + 0x1C))) + (16);
    if (Arg2 != 0) goto loc_00212520;
loc_00212823:
    result = ExpExpandResourceOwnerTable(*(uint64_t *)(v_stack_m28 + 0x38), v_stack_mD0, 1, a4);
    goto loc_002120F5;
loc_00212834:
    *(uint64_t *)(1) = 1;
    goto loc_00212416;
loc_00212841:
    *(uint64_t *)(1) = 0;
    goto loc_00212411;
loc_00212849:
    goto loc_002127AA;
loc_00212852:
    local_rsi = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_mD0 + 0x8))) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mD0 + 0x8)) + 8)));
    local_rsi = (uint32_t)((local_rsi) & (7));
    local_rsi = (uint32_t)((local_rsi) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mD0 + 0x8)) + 8)));
    *(uint32_t *)(v_stack_mD0 + 0x8) = (uint32_t)(local_rsi);
    local_rsi = (uint32_t)((local_rsi) >> (3));
    if (((*(uint8_t *)(v_rip + 0xDB429A)) & (1)) != 0) goto loc_002128B9;
loc_0021286E:
    if (v_stack_mD0 != 0) goto loc_0021289A;
    if (v_stack_mD0 == v_stack_mD0) goto loc_002128D0;
    result = KxWaitForLockChainValid(v_stack_mD0, v_stack_mD0, v_stack_mB0, a4);
loc_0021289A:
    v_stack_mD0 = *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xD0);
    result = (uint8_t)((v_stack_mC8) ^ ((uint8_t)(v_stack_mC8)));
    if ((((uint8_t)(result)) & (4)) == 0) goto loc_002128D0;
    result = KeWakeAddressAll(result + 8, v_stack_mC8, v_stack_mB0, a4);
    goto loc_002128D0;
loc_002128B9:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCFB599))) != 0) goto loc_0021286E;
    result = KiReleaseQueuedSpinLockInstrumented(v_stack_mD0, v_stack_p0, v_stack_mB0, a4);
loc_002128D0:
    if ((*(uint32_t *)(v_rip + 0xDB4449)) != ((uint32_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xD0)))) {
        Arg1 = v_stack_mC0;
        Arg2 = (uint8_t)(v_stack_mC0);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, v_stack_mB0, a4);
    }
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC55D8A))) == 0) goto loc_00212A52;
    v_stack_mD5 = 0;
    v_stack_mD8 = (uint16_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xD0));
    v_stack_mD6 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xD1));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5A0)))) & (1)) != 0) goto loc_00212A52;
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x620) != 0) goto loc_002129AB;
    result = ExAllocatePool2(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x620) + 72, 512, (uint32_t)(0x72546552ULL), a4);
    if (result == 0) goto loc_00212A52;
    *(uint64_t *)(result + 0x10) = *(uint64_t *)(v_stack_m28 + 0x38);
    *(uint64_t *)(result + 0x1C) = 0x10000ULL;
    *(uint32_t *)(result + 0x28) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC55B0C)));
    result = 0;
    if (condition_is_equal) goto loc_00212C29;
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, (uint32_t)(0x72546552ULL), a4);
loc_002129AB:
    Arg1 = 0;
loc_002129AF:
    if (0 >= 8) goto loc_002129E9;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x1C)))) != 0x10000ULL) goto loc_002129CB;
    if ((*(uint64_t *)(0 + 0x10)) != (*(uint64_t *)(v_stack_m28 + 0x38))) goto loc_002129CB;
    if ((*(uint32_t *)(0 + 0x28)) == ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC55B0C))))) goto loc_00212A13;
loc_002129CB:
    if (0 != 0) goto loc_00212C02;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x1C))) == 0) goto loc_00212BFF;
    if ((*(uint32_t *)(0 + 0x28)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC55B0C))))) goto loc_00212C02;
loc_002129E9:
    if (0 == 0) goto loc_00212A13;
    Arg2 = 0;
    *(uint32_t *)(0 + 0x24) = 0;
    *(uint64_t *)(0) = 0;
    *(uint64_t *)(0 + 0x8) = 0;
    *(uint32_t *)(0 + 0x18) = 0;
    *(uint32_t *)(0 + 0x2C) = 0;
loc_00212A03:
    *(uint32_t *)(0 + 0x28) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC55B0C)));
    *(uint64_t *)(0 + 0x1C) = 0x10000ULL;
    *(uint64_t *)(0 + 0x10) = *(uint64_t *)(v_stack_m28 + 0x38);
loc_00212A13:
    if (0 == 0) goto loc_00212A52;
loc_00212A1E:
    if ((*(uint32_t *)(0 + 0x20)) != 0) goto loc_0021341C;
    *(uint64_t *)(0 + 0x8) = 2;
    *(uint64_t *)(0) = 1;
    *(uint32_t *)(0 + 0x18) = (uint32_t)((uint32_t)(v_stack_mD8));
    *(uint32_t *)(0 + 0x2C) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x44)));
loc_00212A4B:
    *(uint32_t *)(0 + 0x24) = (uint32_t)(local_rsi);
loc_00212A4E:
    *(uint32_t *)(0 + 0x20) = 1;
loc_00212A52:
    goto loc_0021242C;
loc_00212A5A:
    if (*(uint64_t *)(arg1 + 0x10) != 0) goto loc_002124F7;
    goto loc_002124F7;
loc_00212A6B:
    *(uint64_t *)(0) = 1;
    goto loc_002127E9;
loc_00212A79:
    *(uint64_t *)(0) = 0;
    goto loc_002127E3;
loc_00212A81:
    result = (uint32_t)((0) - (*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x10)));
    result = (result) >> (4);
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x460) = (uint8_t)(result);
loc_00212A99:
    if (0 == 0) goto loc_002120FB;
    goto loc_00212541;
loc_00212AA7:
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x30)) != (*(uint64_t *)(gs_base + (0 + 0x188)))) goto loc_00212505;
    local_rsi = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x38))) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x38)) + 8)));
    local_rsi = (uint32_t)((local_rsi) & (7));
    local_rsi = (uint32_t)((local_rsi) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x38)) + 8)));
    *(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x38) = (uint32_t)(local_rsi);
    local_rsi = (uint32_t)((local_rsi) >> (3));
    result = KeReleaseInStackQueuedSpinLock(v_stack_mD0, 0, 1, a4);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC55B0C))) == 0) goto loc_00212A52;
    v_stack_mD5 = 0;
    v_stack_mD8 = (uint16_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xD0));
    v_stack_mD6 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xD1));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5A0)))) & (1)) != 0) goto loc_00212A52;
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x620) != 0) goto loc_00212B8A;
    result = ExAllocatePool2(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x620) + 72, 512, (uint32_t)(0x72546552ULL), a4);
    if (result == 0) goto loc_00212A52;
    *(uint64_t *)(result + 0x10) = *(uint64_t *)(v_stack_m28 + 0x38);
    *(uint64_t *)(result + 0x1C) = 0x10000ULL;
    *(uint32_t *)(result + 0x28) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC5592D)));
    result = 0;
    if (condition_is_equal) goto loc_00212C31;
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, (uint32_t)(0x72546552ULL), a4);
loc_00212B8A:
    Arg1 = 0;
loc_00212B90:
    if (0 >= 8) goto loc_00212BC2;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x1C)))) != 0x10000ULL) goto loc_00212BB0;
    if ((*(uint64_t *)(0 + 0x10)) != (*(uint64_t *)(v_stack_m28 + 0x38))) goto loc_00212BB0;
    if ((*(uint32_t *)(0 + 0x28)) == ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC5592D))))) goto loc_00212A13;
loc_00212BB0:
    if (0 != 0) goto loc_00212C1E;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x1C))) == 0) goto loc_00212C1B;
    if ((*(uint32_t *)(0 + 0x28)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC5592D))))) goto loc_00212C1E;
loc_00212BC2:
    if (0 == 0) goto loc_00212A13;
    Arg1 = 0;
    *(uint32_t *)(0 + 0x24) = 0;
    *(uint64_t *)(0) = 0;
    *(uint64_t *)(0 + 0x8) = 0;
    *(uint32_t *)(0 + 0x18) = 0;
    *(uint32_t *)(0 + 0x2C) = 0;
    goto loc_00212A03;
loc_00212BE5:
    if (0 != 0) goto loc_00212143;
    goto loc_00212143;
loc_00212BF6:
    Arg2 = (0) + (16);
    goto loc_00212166;
loc_00212BFF:
loc_00212C02:
    local_rdi = (0) + (64);
    Arg1 = (uint32_t)((Arg1) + 1);
    goto loc_002129AF;
loc_00212C0D:
    result = KxWaitForLockOwnerShip(v_stack_mD0, Arg2, (uint32_t)(0x72546552ULL), a4);
    goto loc_002120F5;
loc_00212C1B:
loc_00212C1E:
    local_rdi = (local_rdi) + (64);
    Arg2 = (uint32_t)((Arg2) + 1);
    goto loc_00212B90;
loc_00212C29:
    goto loc_00212A1E;
loc_00212C31:
    goto loc_00212A1E;
loc_00212C39:
loc_00212C40:
    if (condition_is_not_equal) goto loc_00212C40;
    if (condition_is_above_or_equal) goto loc_00212243;
    result = KiRemoveSystemWorkPriorityKick(v_stack_mD0, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(0x72546552ULL))))), (uint32_t)(0x72546552ULL), a4);
    goto loc_00212243;
loc_00212C61:
loc_00212C68:
    if (condition_is_not_equal) goto loc_00212C68;
    if (condition_is_above_or_equal) goto loc_0021261C;
    result = KiRemoveSystemWorkPriorityKick(v_stack_mD0, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(0x72546552ULL))))), (uint32_t)(0x72546552ULL), a4);
    goto loc_0021261C;
loc_00212C89:
    if ((*(uint32_t *)(local_rdi + 0x28)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x44))))) goto loc_002133C7;
loc_00212C96:
    if (local_rdi != 0) {
        *(uint64_t *)(local_rdi + 0x10) = *(uint64_t *)(v_stack_m28 + 0x38);
        *(uint64_t *)(local_rdi + 0x1C) = 0x10000ULL;
        *(uint32_t *)(local_rdi + 0x24) = (uint32_t)(*(uint64_t *)(gs_base + (0 + 0x20)));
        *(uint64_t *)(local_rdi) = *(uint64_t *)(gs_base + (0 + 0x20));
        *(uint64_t *)(local_rdi + 0x8) = *(uint64_t *)(gs_base + (0 + 0x20));
        *(uint32_t *)(local_rdi + 0x18) = (uint32_t)(*(uint64_t *)(gs_base + (0 + 0x20)));
        *(uint32_t *)(local_rdi + 0x28) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x44)));
        *(uint32_t *)(local_rdi + 0x2C) = (uint32_t)(*(uint64_t *)(gs_base + (0 + 0x20)));
    }
    if (local_rdi == 0) goto loc_0021342D;
loc_00212CCD:
    *(uint64_t *)(local_rdi) = v_stack_mB0;
    *(uint32_t *)(local_rdi + 0x18) = (uint32_t)((uint32_t)(v_stack_mD8));
    *(uint32_t *)(local_rdi + 0x20) = 4;
loc_00212CE8:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5A0))) >> (9));
    Arg1 = (uint32_t)((Arg1) & (7));
    result = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220) + 0x2A0);
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220) + 0x2A0) != 0) {
        result = *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220) + 0x2A0) + 0x43C);
        if (((uint32_t)(Arg1)) >= ((uint32_t)(result))) { Arg1 = (uint32_t)(result); }
    }
    if (((uint32_t)(Arg1)) < 2) goto loc_00213184;
loc_00212D28:
    if (((uint32_t)(Arg1)) >= = 1) {
        Arg2 = (uint32_t)((uint32_t)(*(uint64_t *)(gs_base + (0 + 0x20))));
        if (((*(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x1A)) & (4)) == 0) { Arg2 = 4; }
    }
    Arg1 = (uint32_t)(((uint32_t)(Arg2)) | (2));
    if ((((uint8_t)(*(uint16_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x1A))) & (2)) != 0) { Arg1 = Arg2; }
    a4 = (uint32_t)((*(uint16_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x1A)) >> (8));
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) | (0xFF00ULL));
    if (((uint32_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xC3)))) <= ((uint32_t)(a4))) { Arg2 = (uint32_t)(Arg1); }
    result = (int8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xC3));
    if (Arg2 != 0) {
        Arg1 = *(uint64_t *)(v_stack_m28 + 0x38);
        result = ExpApplyPriorityBoost(Arg1, Arg2, *(uint64_t *)(gs_base + (0 + 0x188)), a4);
    }
    result = ExpWaitForResource(*(uint64_t *)(v_stack_m28 + 0x38), v_stack_mA8, (uint32_t)(0x10244ULL), a4);
    if ((((uint8_t)(*(uint64_t *)(gs_base + (0 + 0x188)))) & (3)) != 0) goto loc_0021317C;
loc_00212D8F:
    result = 0;
    v_stack_m60 = 0;
    v_stack_m70 = v_xmm0;
    if ((((uint8_t)(*(uint16_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x1A))) & (8)) != 0) goto loc_00212EEE;
    if ((((uint8_t)(*(uint16_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x1A))) & (4)) == 0) goto loc_00212DE0;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5A0))) >> (9));
    Arg1 = (uint32_t)((Arg1) & (7));
    result = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220) + 0x2A0);
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220) + 0x2A0) != 0) {
        result = *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220) + 0x2A0) + 0x43C);
        if (((uint32_t)(Arg1)) >= ((uint32_t)(result))) { Arg1 = (uint32_t)(result); }
    }
    Arg2 = (uint32_t)((uint32_t)(*(uint64_t *)(gs_base + (0 + 0x20))));
    if (((uint32_t)(Arg1)) < 2) { Arg2 = 4; }
loc_00212DE0:
    local_rsi = (uint32_t)(((uint32_t)(Arg2)) | (2));
    if (((*(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x1A)) & (2)) == 0) { local_rsi = Arg2; }
    if ((uint32_t)(local_rsi) == 0) goto loc_00212EEE;
    v_stack_m70 = *(uint64_t *)(gs_base + (0 + 0x20));
    v_stack_m68 = *(uint64_t *)(v_stack_m28 + 0x38) + 96;
    if ((*(uint32_t *)(v_rip + 0xDB3F0B)) != 0) goto loc_0021314E;
loc_00212E1B:
    v_stack_m60 = (uint8_t)(v_stack_mC0);
    if (((*(uint8_t *)(v_rip + 0xDB3CE4)) & (33)) != 0) goto loc_002130A3;
loc_00212E2C:
    if (v_stack_m70 != 0) goto loc_002131A9;
loc_00212E3C:
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x30)) == (*(uint64_t *)(gs_base + (0 + 0x188)))) goto loc_00212E77;
    a4 = 0;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x30) != 0) ? 1 : 0;
    if ((uint32_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x460)) != 0) goto loc_002130C2;
loc_00212E5E:
    Arg2 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x48))) + ((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x40)));
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x10) != 0) goto loc_0021310F;
loc_00212E74:
loc_00212E77:
    if ((((uint8_t)(local_rsi)) & (4)) != 0) goto loc_002131B7;
loc_00212E81:
    if ((((uint8_t)(local_rsi)) & (2)) == 0) goto loc_00212EBB;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(0 + 0x8)))) & (4)) != 0) goto loc_00213107;
    result = (uint32_t)((1) + 1);
    if (((uint32_t)(result)) != 1) goto loc_00212EB7;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x318)) != 0) goto loc_002131DF;
loc_00212EB7:
loc_00212EBB:
    result = KeReleaseInStackQueuedSpinLock(v_stack_m70, Arg2, (uint32_t)(0x10244ULL), a4);
    if ((uint32_t)(local_rsi) == 0) goto loc_00212EEB;
    if ((((uint8_t)(local_rsi)) & (4)) != 0) {
        a3 = 0;
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x188));
        Arg2 = a3 + 2;
        result = IoBoostThreadIoPriority(Arg1, Arg2, a3, a4);
    }
    if ((((uint8_t)(local_rsi)) & (2)) != 0) {
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x188));
        result = PsBoostThreadOutstandingIoQoS(Arg1, Arg2, a3, a4);
    }
    local_r13 = 0;
loc_00212EEE:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC5592D))) == 0) goto loc_0021308D;
    v_stack_mB8 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x44)));
    v_stack_mD8 = 0;
    Arg2 = (Arg2) << (32);
    result = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x44))) | (Arg2);
    v_stack_mD5 = 0;
    v_stack_mD8 = (uint16_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xD0));
    v_stack_mD6 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xD1));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5A0)))) & (1)) != 0) goto loc_0021308D;
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x620) != 0) goto loc_00212FBD;
    result = ExAllocatePool2(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x620) + 72, 512, (uint32_t)(0x72546552ULL), a4);
    if (result == 0) goto loc_0021308D;
    a3 = 0;
    *(uint64_t *)(result + 0x10) = *(uint64_t *)(v_stack_m28 + 0x38);
    *(uint64_t *)(result + 0x1C) = 0x10000ULL;
    *(uint32_t *)(result + 0x28) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC554F9)));
    result = 0;
    if (condition_is_equal) goto loc_00213033;
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, a3, a4);
loc_00212FBD:
    a3 = 0;
loc_00212FC6:
    if (0 >= 8) goto loc_00213000;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x1C)))) != 0x10000ULL) goto loc_00212FE2;
    if ((*(uint64_t *)(0 + 0x10)) != (*(uint64_t *)(v_stack_m28 + 0x38))) goto loc_00212FE2;
    if ((*(uint32_t *)(0 + 0x28)) == ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC554F9))))) goto loc_0021302B;
loc_00212FE2:
    if (0 != 0) goto loc_00213098;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x1C))) == 0) goto loc_00213095;
    if ((*(uint32_t *)(0 + 0x28)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC554F9))))) goto loc_00213098;
loc_00213000:
    if (0 != 0) {
        *(uint64_t *)(0 + 0x10) = *(uint64_t *)(v_stack_m28 + 0x38);
        *(uint64_t *)(0 + 0x1C) = 0x10000ULL;
        *(uint32_t *)(0 + 0x24) = 0;
        *(uint64_t *)(0) = 0;
        *(uint64_t *)(0 + 0x8) = 0;
        *(uint32_t *)(0 + 0x18) = 0;
        *(uint32_t *)(0 + 0x28) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC554F9)));
        *(uint32_t *)(0 + 0x2C) = 0;
    }
    if (0 == 0) goto loc_0021308D;
loc_00213033:
    *(uint64_t *)(0 + 0x8) = result;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x20))) == 0) goto loc_002130FF;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x20)))) != 4) goto loc_002130FF;
    if ((*(uint16_t *)(0 + 0x18)) != ((uint16_t)(v_stack_mD8))) goto loc_002130F1;
    if ((*(uint8_t *)(0 + 0x1A)) != ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xD1)))) goto loc_002130F1;
    local_r14 = (result) - (*(uint64_t *)(0));
    *(uint64_t *)(0) = local_r14;
loc_00213070:
loc_00213076:
    *(uint32_t *)(0 + 0x18) = (uint32_t)((uint32_t)(v_stack_mD8));
    *(uint32_t *)(0 + 0x2C) = (uint32_t)((uint32_t)(v_stack_mB8));
    *(uint32_t *)(0 + 0x20) = 1;
    *(uint32_t *)(0 + 0x24) = 1;
loc_0021308D:
    goto loc_0021242C;
loc_00213095:
loc_00213098:
    local_rdi = (0) + (64);
    Arg2 = (uint32_t)((0) + 1);
    goto loc_00212FC6;
loc_002130A3:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCFADAF))) != 0) goto loc_00212E2C;
    result = KiAcquireQueuedSpinLockInstrumented(v_stack_m70, local_rdi, 1, a4);
    goto loc_00212E3C;
loc_002130C2:
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x10) == 0) goto loc_00212E5E;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC554F9)))) >= (*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x10) + 0x8))) goto loc_00212E5E;
    local_rdi = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC554F9))))) << (4);
    local_rdi = (local_rdi) + (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x10));
    if ((*(uint64_t *)(local_rdi)) != local_r14) goto loc_00212E5E;
    goto loc_00212E77;
loc_002130F1:
    *(uint64_t *)(v_stack_m70) = 1;
    goto loc_00213076;
loc_002130FF:
    *(uint64_t *)(v_stack_m70) = 1;
    goto loc_00213070;
loc_00213107:
    local_rsi = (uint32_t)((1) & (0xFFFFFFFDULL));
    goto loc_00212EBB;
loc_0021310F:
    a3 = ((uint32_t)(*(uint32_t *)(local_rdi + 0x8))) << (4);
    a3 = (a3) + (local_rdi);
    local_rdi = (local_rdi) + (16);
    if (v_stack_m70 >= local_rdi) goto loc_00212E74;
loc_00213127:
    if ((*(uint64_t *)(local_rdi)) == local_r14) goto loc_0021315F;
    if (*(uint64_t *)(local_rdi) == 0) goto loc_00213140;
    Arg1 = (v_stack_m70) + 1;
    if (Arg1 == local_rdi) goto loc_00212E74;
loc_00213140:
    local_rdi = (local_rdi) + (16);
    if (local_rdi != a3) goto loc_00213127;
    goto loc_00212E74;
loc_0021314E:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xD1)), (uint8_t)(*(uint64_t *)(local_rdi)), a3, a4);
    goto loc_00212E1B;
loc_0021315F:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) - (*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x10)));
    result = (result) >> (4);
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x460) = (uint8_t)(result);
    goto loc_00212E77;
loc_0021317C:
    goto loc_00212D8F;
loc_00213184:
    if (a3 != (*(uint64_t *)(gs_base + (0 + 0x188)))) goto loc_00212D28;
    if ((*(uint32_t *)(a3 + 0x5E0)) == 0) goto loc_00212D28;
    goto loc_00212D2D;
loc_002131A9:
    result = KxWaitForLockOwnerShip(v_stack_m70, (uint8_t)(*(uint64_t *)(local_rdi)), a3, a4);
    goto loc_00212E3C;
loc_002131B7:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x8)))) & (1)) != 0) goto loc_002131D7;
    a4 = 0;
    a3 = 0;
    Arg2 = 0;
    result = PsBoostThreadIoEx(local_r14, Arg2, a3, a4);
    goto loc_00212E81;
loc_002131D7:
    local_rsi = (uint32_t)((local_rsi) & (0xFFFFFFFBULL));
    goto loc_00212E81;
loc_002131DF:
    if ((*(uint32_t *)(v_rip + 0xDB3B2D)) != 0) goto loc_00213243;
loc_002131F5:
    result = KiAbThreadInsertList(local_r14, *(uint64_t *)(gs_base + (0 + 0x20)) + 37240, local_r14 + 808, a4);
    if ((uint32_t)(result) != 0) {
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x20));
        result = KiAbQueueAutoBoostDpc(Arg1, *(uint64_t *)(gs_base + (0 + 0x20)) + 37240, local_r14 + 808, a4);
    }
    if ((*(uint32_t *)(v_rip + 0xDB3AF9)) != 0) {
        Arg1 = 2;
        Arg2 = 2;
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, local_r14 + 808, a4);
    }
    goto loc_00212EB7;
loc_00213243:
    result = KiRaiseIrqlProcessIrqlFlags(2, 2, local_r14 + 808, a4);
    goto loc_002131F5;
loc_00213251:
    if (2 == 0) goto loc_002133CF;
    *(uint64_t *)(2) = local_r14;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(2 + 0x8))) & (7));
    result = (uint32_t)((result) | (8));
    *(uint32_t *)(2 + 0x8) = (uint32_t)(result);
    v_stack_m80 = v_stack_m88;
    v_stack_m88 = v_stack_m88;
    v_stack_mA0 = *(uint64_t *)(gs_base + (0 + 0x20));
    v_stack_m90 = 0x60001ULL;
    v_stack_m98 = local_r14;
    v_stack_m78 = *(uint64_t *)(gs_base + (0 + 0x20));
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x20) != 0) goto loc_002133F0;
    v_stack_mA0 = v_stack_mA8;
    v_stack_mA8 = v_stack_mA8;
loc_002132AD:
    *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x20) = v_stack_mA8;
    result = KeReleaseInStackQueuedSpinLock(v_stack_mD0, 2, local_r14 + 808, a4);
    if ((uint32_t)(*(uint64_t *)(gs_base + (0 + 0x20))) == 0) goto loc_00212CE8;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    v_stack_m38 = v_xmm0;
    Arg2 = (2) << (32);
    result = (result) | (Arg2);
    v_stack_mD5 = (uint8_t)(*(uint64_t *)(gs_base + (0 + 0x20)));
    v_stack_mB0 = result;
    v_stack_mD8 = (uint16_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xD0));
    v_stack_mD6 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xD1));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5A0)))) & (1)) != 0) goto loc_00213437;
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x620) != 0) goto loc_0021338A;
    result = ExAllocatePool2(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x620) + 72, 512, (uint32_t)(0x72546552ULL), a4);
    if (result == 0) goto loc_0021342A;
    *(uint64_t *)(result + 0x10) = *(uint64_t *)(v_stack_m28 + 0x38);
    *(uint64_t *)(result + 0x1C) = 0x10000ULL;
    *(uint32_t *)(result + 0x28) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC55129)));
    result = 0;
    if (condition_is_equal) goto loc_002133E8;
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, (uint32_t)(0x72546552ULL), a4);
loc_0021338A:
    local_r13 = 0;
loc_00213393:
    if (0 >= 8) goto loc_00212C96;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x1C)))) != 0x10000ULL) goto loc_002133B7;
    if ((*(uint64_t *)(0 + 0x10)) != (*(uint64_t *)(v_stack_m28 + 0x38))) goto loc_002133B7;
    if ((*(uint32_t *)(0 + 0x28)) == ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC55129))))) goto loc_00212CC1;
loc_002133B7:
    if (0 != 0) goto loc_002133C7;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x1C))) != 0) goto loc_00212C89;
loc_002133C7:
    local_rdi = (0) + (64);
    Arg2 = (uint32_t)((0) + 1);
    goto loc_00213393;
loc_002133CF:
    result = KeReleaseInStackQueuedSpinLock(v_stack_mD0, Arg2, (uint32_t)(0x72546552ULL), a4);
    local_rsi = 0;
    goto loc_0021242C;
loc_002133E8:
    local_r13 = 0;
    goto loc_00212CCD;
loc_002133F0:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x8))) != result) {
        Arg1 = 3;
    }
    v_stack_mA0 = Arg1;
    v_stack_mA8 = result;
    *(uint64_t *)(arg1) = v_stack_mA8;
    *(uint64_t *)(result + 0x8) = v_stack_mA8;
    goto loc_002132AD;
loc_0021341C:
    if ((*(uint32_t *)(v_stack_mA8 + 0x24)) >= 0) goto loc_00212A4E;
    goto loc_00212A4B;
loc_0021342A:
    local_r13 = 0;
loc_0021342D:
    goto loc_00212CE8;
loc_00213437:
    local_r13 = 0;
    goto loc_00212CE8;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x0` | `64` | `R/W` |
| `Arg1` | `+ 0x10` | `32` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x18` | `16` | `W` |
| `Arg1` | `+ 0x1A` | `8` | `R` |
| `Arg1` | `+ 0x1A` | `16` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x20` | `64` | `W` |
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0x30` | `64` | `W` |
| `Arg1` | `+ 0x38` | `32` | `R` |
| `Arg1` | `+ 0x38` | `32` | `W` |
| `Arg1` | `+ 0x40` | `32` | `R` |
| `Arg1` | `+ 0x40` | `32` | `W` |
| `Arg1` | `+ 0x44` | `32` | `R` |
| `Arg1` | `+ 0x48` | `32` | `R` |
| `Arg1` | `+ 0x48` | `32` | `R/W` |
| `Arg1` | `+ 0x4C` | `32` | `R` |
| `Arg1` | `+ 0x60` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00212040&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
