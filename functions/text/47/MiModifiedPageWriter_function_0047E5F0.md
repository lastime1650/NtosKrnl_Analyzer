# MiModifiedPageWriter

- RVA: `0x0047E5F0`–`0x0047EC78` (길이 `1,672` bytes)
- VA: `0x000000014047E5F0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000ADFF0`
- 디코드: `387`개 명령, `1,672/1,672` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **37**; 고유 호출 대상: **20**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0047E654` → [KeAbPreAcquire](../21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0047E66D` → [ExfAcquirePushLockExclusiveEx](../20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x0047E687` → [KeSetEvent](../33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x0047E6BA` → [ExfTryToWakePushLock](../26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x0047E6C2` → [KeAbPostRelease](../2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0047E6E9` → [KeSetActualBasePriorityThread](../3C/KeSetActualBasePriorityThread_function_003C4370.md) (function, `0x003C4370`)
- `0x0047E765` → [MiStoreCheckCompleteWriteBatch](MiStoreCheckCompleteWriteBatch_function_0047EC80.md) (function, `0x0047EC80`)
- `0x0047E795` → [KeWaitForMultipleObjects](../20/KeWaitForMultipleObjects_function_0020D110.md) (function, `0x0020D110`)
- `0x0047E7C7` → [MiStoreCheckCompleteWriteBatch](MiStoreCheckCompleteWriteBatch_function_0047EC80.md) (function, `0x0047EC80`)
- `0x0047E834` → [MiUseLowIoPriorityForModifiedPages](../34/MiUseLowIoPriorityForModifiedPages_function_0034D284.md) (function, `0x0034D284`)
- `0x0047E865` → [KeSetActualBasePriorityThread](../3C/KeSetActualBasePriorityThread_function_003C4370.md) (function, `0x003C4370`)
- `0x0047E8C2` → [KiCheckForKernelApcDelivery](../2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (function, `0x002E2C80`)
- `0x0047E8D2` → [MiGatherPagefilePages](../37/MiGatherPagefilePages_function_00372B08.md) (function, `0x00372B08`)
- `0x0047E8E3` → [MiCheckFreeModifiedReservations](MiCheckFreeModifiedReservations_function_0047ED60.md) (function, `0x0047ED60`)
- `0x0047E920` → [KiCheckForKernelApcDelivery](../2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (function, `0x002E2C80`)
- `0x0047E94C` → [KeWaitForMultipleObjects](../20/KeWaitForMultipleObjects_function_0020D110.md) (function, `0x0020D110`)
- `0x0047E973` → [KeQueryPriorityThread](../38/KeQueryPriorityThread_function_0038F4F0.md) (function, `0x0038F4F0`)
- `0x0047E983` → [KeSetActualBasePriorityThread](../3C/KeSetActualBasePriorityThread_function_003C4370.md) (function, `0x003C4370`)
- `0x0047E9D9` → [KiCheckForKernelApcDelivery](../2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (function, `0x002E2C80`)
- `0x0047E9E6` → [KeResetEvent](../24/KeResetEvent_function_00248350.md) (function, `0x00248350`)
- `0x0047EA59` → [MiMakePagefileWriterEntryAvailable](MiMakePagefileWriterEntryAvailable_function_0047EE78.md) (function, `0x0047EE78`)
- `0x0047EA7D` → [KeResetEvent](../24/KeResetEvent_function_00248350.md) (function, `0x00248350`)
- `0x0047EA98` → [IoBoostThreadIoPriority](../21/IoBoostThreadIoPriority_function_00216110.md) (function, `0x00216110`)
- `0x0047EAB9` → [ExWaitForRundownProtectionRelease](../2A/ExWaitForRundownProtectionRelease_function_002A4CB0.md) (function, `0x002A4CB0`)
- `0x0047EAD3` → [KeSetActualBasePriorityThread](../3C/KeSetActualBasePriorityThread_function_003C4370.md) (function, `0x003C4370`)
- `0x0047EAE4` → [KeSetEvent](../33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x0047EAF3` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x0047EB2B` → [KiCheckForKernelApcDelivery](../2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (function, `0x002E2C80`)
- `0x0047EB49` → [ExfTryToWakePushLock](../26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x0047EB63` → [KeSetEvent](../33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x0047EB6B` → [KeCancelTimer](../23/KeCancelTimer_function_002327E0.md) (function, `0x002327E0`)
- `0x0047EB9E` → [KeResetEvent](../24/KeResetEvent_function_00248350.md) (function, `0x00248350`)
- `0x0047EBA6` → [MiStoreUpdateMemoryConditions](../34/MiStoreUpdateMemoryConditions_function_0034CF3C.md) (function, `0x0034CF3C`)
- `0x0047EBEE` → [KiCheckForKernelApcDelivery](../2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (function, `0x002E2C80`)
- `0x0047EC02` → [IoBoostThreadIoPriority](../21/IoBoostThreadIoPriority_function_00216110.md) (function, `0x00216110`)
- `0x0047EC34` → [KiCheckForKernelApcDelivery](../2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (function, `0x002E2C80`)
- `0x0047EC4F` → [IoBoostThreadIoPriority](../21/IoBoostThreadIoPriority_function_00216110.md) (function, `0x00216110`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0047E616` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **6**
  - `0x0047EB40` → [sub_006F4C8C](../6F/Unknown_function_006F4C8C.md) (`tail-transfer`)
  - `0x0047EB4F` → [sub_006F4C8C](../6F/Unknown_function_006F4C8C.md) (`tail-transfer`)
  - `0x0047EBD7` → [sub_006F4C8C + 0x37](../6F/Unknown_function_006F4C8C.md) (`tail-transfer`)
  - `0x0047EBE8` → [sub_006F4C8C + 0x37](../6F/Unknown_function_006F4C8C.md) (`tail-transfer`)
  - `0x0047EBF4` → [sub_006F4C8C + 0x37](../6F/Unknown_function_006F4C8C.md) (`tail-transfer`)
  - `0x0047EC73` → [sub_006F4C8C + 0x4B](../6F/Unknown_function_006F4C8C.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0047E5F0  48 8B C4                        mov rax, rsp
0047E5F3  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
0047E5F7  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0047E5FB  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
0047E5FF  55                              push rbp
0047E600  41 54                           push r12
0047E602  41 55                           push r13
0047E604  41 56                           push r14
0047E606  41 57                           push r15
0047E608  48 8D A8 B8 FE FF FF            lea rbp, [rax - 0x148]
0047E60F  48 81 EC 20 02 00 00            sub rsp, 0x220
0047E616  48 8B 05 23 C1 98 00            mov rax, qword ptr [rip + 0x98c123]
0047E61D  48 33 C4                        xor rax, rsp
0047E620  48 89 85 10 01 00 00            mov qword ptr [rbp + 0x110], rax
0047E627  48 8B 31                        mov rsi, qword ptr [rcx]
0047E62A  4C 8B F9                        mov r15, rcx
0047E62D  65 48 8B 3C 25 88 01 00 00      mov rdi, qword ptr gs:[0x188]
0047E636  41 BD 01 00 00 00               mov r13d, 1
0047E63C  45 33 C0                        xor r8d, r8d
0047E63F  33 D2                           xor edx, edx
0047E641  4C 8D B6 40 04 00 00            lea r14, [rsi + 0x440]
0047E648  66 44 29 AF E6 01 00 00         sub word ptr [rdi + 0x1e6], r13w
0047E650  49 8B CE                        mov rcx, r14
0047E653  90                              nop
0047E654  E8 D7 1B D9 FF                  call 0x140210230
0047E659  F0 49 0F BA 2E 00               lock bts qword ptr [r14], 0
0047E65F  48 8B D8                        mov rbx, rax
0047E662  73 0E                           jae 0x14047e672
0047E664  4D 8B C6                        mov r8, r14
0047E667  48 8B D0                        mov rdx, rax
0047E66A  49 8B CE                        mov rcx, r14
0047E66D  E8 1E 16 D9 FF                  call 0x14020fc90
0047E672  45 33 E4                        xor r12d, r12d
0047E675  48 85 DB                        test rbx, rbx
0047E678  74 04                           je 0x14047e67e
0047E67A  44 88 6B 0A                     mov byte ptr [rbx + 0xa], r13b
0047E67E  49 8D 4F 08                     lea rcx, [r15 + 8]
0047E682  45 33 C0                        xor r8d, r8d
0047E685  33 D2                           xor edx, edx
0047E687  E8 84 0C EC FF                  call 0x14033f310
0047E68C  48 83 CB FF                     or rbx, 0xffffffffffffffff
0047E690  44 8D 6B 03                     lea r13d, [rbx + 3]
0047E694  4C 39 A6 E0 03 00 00            cmp qword ptr [rsi + 0x3e0], r12
0047E69B  0F 85 94 04 00 00               jne 0x14047eb35
0047E6A1  48 89 BE E0 03 00 00            mov qword ptr [rsi + 0x3e0], rdi
0047E6A8  48 8B C3                        mov rax, rbx
0047E6AB  F0 49 0F C1 06                  lock xadd qword ptr [r14], rax
0047E6B0  24 06                           and al, 6
0047E6B2  41 3A C5                        cmp al, r13b
0047E6B5  75 08                           jne 0x14047e6bf
0047E6B7  49 8B CE                        mov rcx, r14
0047E6BA  E8 11 77 DE FF                  call 0x140265dd0
0047E6BF  49 8B CE                        mov rcx, r14
0047E6C2  E8 39 2F E6 FF                  call 0x1402e1600
0047E6C7  B9 01 00 00 00                  mov ecx, 1
0047E6CC  90                              nop
0047E6CD  66 01 8F E6 01 00 00            add word ptr [rdi + 0x1e6], cx
0047E6D4  0F 84 40 04 00 00               je 0x14047eb1a
0047E6DA  44 09 AF A4 05 00 00            or dword ptr [rdi + 0x5a4], r13d
0047E6E1  BA 12 00 00 00                  mov edx, 0x12
0047E6E6  48 8B CF                        mov rcx, rdi
0047E6E9  E8 82 5C F4 FF                  call 0x1403c4370
0047E6EE  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
0047E6F2  48 8D 56 58                     lea rdx, [rsi + 0x58]
0047E6F6  48 8D 86 10 03 00 00            lea rax, [rsi + 0x310]
0047E6FD  49 8B CC                        mov rcx, r12
0047E700  48 87 8E E8 03 00 00            xchg qword ptr [rsi + 0x3e8], rcx
0047E707  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
0047E70C  4C 8D BE A0 03 00 00            lea r15, [rsi + 0x3a0]
0047E713  48 8D 86 C8 03 00 00            lea rax, [rsi + 0x3c8]
0047E71A  48 89 54 24 50                  mov qword ptr [rsp + 0x50], rdx
0047E71F  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0047E723  4C 8D B6 D8 04 00 00            lea r14, [rsi + 0x4d8]
0047E72A  48 8D 86 E8 02 00 00            lea rax, [rsi + 0x2e8]
0047E731  48 89 55 C0                     mov qword ptr [rbp - 0x40], rdx
0047E735  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
0047E739  48 8D 86 20 04 00 00            lea rax, [rsi + 0x420]
0047E740  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
0047E744  4C 89 7D C8                     mov qword ptr [rbp - 0x38], r15
0047E748  4C 89 75 E8                     mov qword ptr [rbp - 0x18], r14
0047E74C  4C 89 A6 78 03 00 00            mov qword ptr [rsi + 0x378], r12
0047E753  48 8B CE                        mov rcx, rsi
0047E756  44 89 A6 80 03 00 00            mov dword ptr [rsi + 0x380], r12d
0047E75D  44 88 A6 D2 02 00 00            mov byte ptr [rsi + 0x2d2], r12b
0047E764  90                              nop
0047E765  E8 16 05 00 00                  call 0x14047ec80
0047E76A  41 B9 13 00 00 00               mov r9d, 0x13
0047E770  48 8D 44 24 60                  lea rax, [rsp + 0x60]
0047E775  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0047E77A  48 8D 54 24 50                  lea rdx, [rsp + 0x50]
0047E77F  4C 89 64 24 30                  mov qword ptr [rsp + 0x30], r12
0047E784  41 8B CD                        mov ecx, r13d
0047E787  44 88 64 24 28                  mov byte ptr [rsp + 0x28], r12b
0047E78C  45 8D 41 EE                     lea r8d, [r9 - 0x12]
0047E790  44 88 64 24 20                  mov byte ptr [rsp + 0x20], r12b
0047E795  E8 76 E9 D8 FF                  call 0x14020d110
0047E79A  C6 86 D2 02 00 00 01            mov byte ptr [rsi + 0x2d2], 1
0047E7A1  85 C0                           test eax, eax
0047E7A3  0F 84 FC 02 00 00               je 0x14047eaa5
0047E7A9  44 39 66 5C                     cmp dword ptr [rsi + 0x5c], r12d
0047E7AD  0F 85 F2 02 00 00               jne 0x14047eaa5
0047E7B3  4C 39 A6 A0 4C 00 00            cmp qword ptr [rsi + 0x4ca0], r12
0047E7BA  74 90                           je 0x14047e74c
0047E7BC  66 01 9F E6 01 00 00            add word ptr [rdi + 0x1e6], bx
0047E7C3  48 8B CE                        mov rcx, rsi
0047E7C6  90                              nop
0047E7C7  E8 B4 04 00 00                  call 0x14047ec80
0047E7CC  4C 8D A6 B8 03 00 00            lea r12, [rsi + 0x3b8]
0047E7D3  4D 39 24 24                     cmp qword ptr [r12], r12
0047E7D7  0F 84 21 01 00 00               je 0x14047e8fe
0047E7DD  45 33 C0                        xor r8d, r8d
0047E7E0  44 39 86 EC 02 00 00            cmp dword ptr [rsi + 0x2ec], r8d
0047E7E7  0F 85 89 02 00 00               jne 0x14047ea76
0047E7ED  44 38 86 DC 04 00 00            cmp byte ptr [rsi + 0x4dc], r8b
0047E7F4  0F 85 5A 03 00 00               jne 0x14047eb54
0047E7FA  44 39 86 A4 03 00 00            cmp dword ptr [rsi + 0x3a4], r8d
0047E801  0F 85 DC 01 00 00               jne 0x14047e9e3
0047E807  44 39 86 24 04 00 00            cmp dword ptr [rsi + 0x424], r8d
0047E80E  0F 85 83 03 00 00               jne 0x14047eb97
0047E814  4D 39 24 24                     cmp qword ptr [r12], r12
0047E818  0F 84 93 01 00 00               je 0x14047e9b1
0047E81E  8B 86 B0 04 00 00               mov eax, dword ptr [rsi + 0x4b0]
0047E824  B9 01 00 00 00                  mov ecx, 1
0047E829  84 C1                           test cl, al
0047E82B  0F 85 82 03 00 00               jne 0x14047ebb3
0047E831  48 8B CE                        mov rcx, rsi
0047E834  E8 4B EA EC FF                  call 0x14034d284
0047E839  85 C0                           test eax, eax
0047E83B  0F 84 56 01 00 00               je 0x14047e997
0047E841  48 8B 86 08 03 00 00            mov rax, qword ptr [rsi + 0x308]
0047E848  48 39 86 A0 4C 00 00            cmp qword ptr [rsi + 0x4ca0], rax
0047E84F  0F 82 B7 03 00 00               jb 0x14047ec0c
0047E855  B8 04 00 00 00                  mov eax, 4
0047E85A  48 8B CF                        mov rcx, rdi
0047E85D  8B D0                           mov edx, eax
0047E85F  89 86 00 03 00 00               mov dword ptr [rsi + 0x300], eax
0047E865  E8 06 5B F4 FF                  call 0x1403c4370
0047E86A  44 8B F8                        mov r15d, eax
0047E86D  33 C9                           xor ecx, ecx
0047E86F  4D 8B 34 24                     mov r14, qword ptr [r12]
0047E873  4D 39 66 08                     cmp qword ptr [r14 + 8], r12
0047E877  0F 85 F2 01 00 00               jne 0x14047ea6f
0047E87D  49 8B 06                        mov rax, qword ptr [r14]
0047E880  4C 39 70 08                     cmp qword ptr [rax + 8], r14
0047E884  0F 85 E5 01 00 00               jne 0x14047ea6f
0047E88A  49 89 04 24                     mov qword ptr [r12], rax
0047E88E  4C 89 60 08                     mov qword ptr [rax + 8], r12
0047E892  41 8B 46 28                     mov eax, dword ptr [r14 + 0x28]
0047E896  83 E0 E3                        and eax, 0xffffffe3
0047E899  49 C7 06 61 00 00 00            mov qword ptr [r14], 0x61
0047E8A0  0B C1                           or eax, ecx
0047E8A2  41 89 46 28                     mov dword ptr [r14 + 0x28], eax
0047E8A6  B8 01 00 00 00                  mov eax, 1
0047E8AB  90                              nop
0047E8AC  66 01 87 E6 01 00 00            add word ptr [rdi + 0x1e6], ax
0047E8B3  75 12                           jne 0x14047e8c7
0047E8B5  48 8D 87 98 00 00 00            lea rax, [rdi + 0x98]
0047E8BC  90                              nop
0047E8BD  48 39 00                        cmp qword ptr [rax], rax
0047E8C0  74 05                           je 0x14047e8c7
0047E8C2  E8 B9 43 E6 FF                  call 0x1402e2c80
0047E8C7  49 8D 46 68                     lea rax, [r14 + 0x68]
0047E8CB  49 8B CE                        mov rcx, r14
0047E8CE  49 89 46 60                     mov qword ptr [r14 + 0x60], rax
0047E8D2  E8 31 42 EF FF                  call 0x140372b08
0047E8D7  44 3B FB                        cmp r15d, ebx
0047E8DA  0F 85 90 00 00 00               jne 0x14047e970
0047E8E0  48 8B CE                        mov rcx, rsi
0047E8E3  E8 78 04 00 00                  call 0x14047ed60
0047E8E8  45 33 E4                        xor r12d, r12d
0047E8EB  4C 8D B6 D8 04 00 00            lea r14, [rsi + 0x4d8]
0047E8F2  4C 8D BE A0 03 00 00            lea r15, [rsi + 0x3a0]
0047E8F9  E9 AB FE FF FF                  jmp 0x14047e7a9
0047E8FE  B8 01 00 00 00                  mov eax, 1
0047E903  88 86 D1 02 00 00               mov byte ptr [rsi + 0x2d1], al
0047E909  90                              nop
0047E90A  66 01 87 E6 01 00 00            add word ptr [rdi + 0x1e6], ax
0047E911  75 12                           jne 0x14047e925
0047E913  48 8D 87 98 00 00 00            lea rax, [rdi + 0x98]
0047E91A  90                              nop
0047E91B  48 39 00                        cmp qword ptr [rax], rax
0047E91E  74 05                           je 0x14047e925
0047E920  E8 5B 43 E6 FF                  call 0x1402e2c80
0047E925  48 8D 45 F0                     lea rax, [rbp - 0x10]
0047E929  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0047E92E  48 8D 55 C0                     lea rdx, [rbp - 0x40]
0047E932  33 C0                           xor eax, eax
0047E934  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0047E939  88 44 24 28                     mov byte ptr [rsp + 0x28], al
0047E93D  88 44 24 20                     mov byte ptr [rsp + 0x20], al
0047E941  44 8D 48 13                     lea r9d, [rax + 0x13]
0047E945  44 8D 40 01                     lea r8d, [rax + 1]
0047E949  8D 48 06                        lea ecx, [rax + 6]
0047E94C  E8 BF E7 D8 FF                  call 0x14020d110
0047E951  45 33 C0                        xor r8d, r8d
0047E954  85 C0                           test eax, eax
0047E956  0F 84 E2 02 00 00               je 0x14047ec3e
0047E95C  66 01 9F E6 01 00 00            add word ptr [rdi + 0x1e6], bx
0047E963  90                              nop
0047E964  44 88 86 D1 02 00 00            mov byte ptr [rsi + 0x2d1], r8b
0047E96B  E9 70 FE FF FF                  jmp 0x14047e7e0
0047E970  48 8B CF                        mov rcx, rdi
0047E973  E8 78 0B F1 FF                  call 0x14038f4f0
0047E978  83 F8 12                        cmp eax, 0x12
0047E97B  74 0B                           je 0x14047e988
0047E97D  41 8B D7                        mov edx, r15d
0047E980  48 8B CF                        mov rcx, rdi
0047E983  E8 E8 59 F4 FF                  call 0x1403c4370
0047E988  C7 86 00 03 00 00 12 00 00 00   mov dword ptr [rsi + 0x300], 0x12
0047E992  E9 49 FF FF FF                  jmp 0x14047e8e0
0047E997  83 BE E4 02 00 00 00            cmp dword ptr [rsi + 0x2e4], 0
0047E99E  0F 85 55 02 00 00               jne 0x14047ebf9
0047E9A4  44 8B FB                        mov r15d, ebx
0047E9A7  B9 08 00 00 00                  mov ecx, 8
0047E9AC  E9 BE FE FF FF                  jmp 0x14047e86f
0047E9B1  B8 01 00 00 00                  mov eax, 1
0047E9B6  90                              nop
0047E9B7  66 01 87 E6 01 00 00            add word ptr [rdi + 0x1e6], ax
0047E9BE  44 8D 60 FF                     lea r12d, [rax - 1]
0047E9C2  0F 85 E1 FD FF FF               jne 0x14047e7a9
0047E9C8  48 8D 87 98 00 00 00            lea rax, [rdi + 0x98]
0047E9CF  90                              nop
0047E9D0  48 39 00                        cmp qword ptr [rax], rax
0047E9D3  0F 84 D0 FD FF FF               je 0x14047e7a9
0047E9D9  E8 A2 42 E6 FF                  call 0x1402e2c80
0047E9DE  E9 C6 FD FF FF                  jmp 0x14047e7a9
0047E9E3  49 8B CF                        mov rcx, r15
0047E9E6  E8 65 99 DC FF                  call 0x140248350
0047E9EB  45 33 C0                        xor r8d, r8d
0047E9EE  F0 44 09 04 24                  lock or dword ptr [rsp], r8d
0047E9F3  8B 86 58 48 00 00               mov eax, dword ptr [rsi + 0x4858]
0047E9F9  85 C0                           test eax, eax
0047E9FB  0F 84 06 FE FF FF               je 0x14047e807
0047EA01  48 8D 96 60 48 00 00            lea rdx, [rsi + 0x4860]
0047EA08  44 8B D0                        mov r10d, eax
0047EA0B  45 8D 58 01                     lea r11d, [r8 + 1]
0047EA0F  48 8B 0A                        mov rcx, qword ptr [rdx]
0047EA12  8A 81 AE 00 00 00               mov al, byte ptr [rcx + 0xae]
0047EA18  41 84 C3                        test r11b, al
0047EA1B  75 0E                           jne 0x14047ea2b
0047EA1D  48 83 C2 08                     add rdx, 8
0047EA21  4D 2B D3                        sub r10, r11
0047EA24  75 E9                           jne 0x14047ea0f
0047EA26  E9 DC FD FF FF                  jmp 0x14047e807
0047EA2B  24 FE                           and al, 0xfe
0047EA2D  45 8B C8                        mov r9d, r8d
0047EA30  88 81 AE 00 00 00               mov byte ptr [rcx + 0xae], al
0047EA36  48 8B 02                        mov rax, qword ptr [rdx]
0047EA39  44 39 40 28                     cmp dword ptr [rax + 0x28], r8d
0047EA3D  76 DE                           jbe 0x14047ea1d
0047EA3F  48 8B 40 20                     mov rax, qword ptr [rax + 0x20]
0047EA43  41 8B C9                        mov ecx, r9d
0047EA46  48 8B 0C C8                     mov rcx, qword ptr [rax + rcx*8]
0047EA4A  48 85 C9                        test rcx, rcx
0047EA4D  74 12                           je 0x14047ea61
0047EA4F  B8 11 77 88 99                  mov eax, 0x99887711
0047EA54  48 39 01                        cmp qword ptr [rcx], rax
0047EA57  75 08                           jne 0x14047ea61
0047EA59  E8 1A 04 00 00                  call 0x14047ee78
0047EA5E  45 33 C0                        xor r8d, r8d
0047EA61  48 8B 02                        mov rax, qword ptr [rdx]
0047EA64  45 03 CB                        add r9d, r11d
0047EA67  44 3B 48 28                     cmp r9d, dword ptr [rax + 0x28]
0047EA6B  72 D2                           jb 0x14047ea3f
0047EA6D  EB AE                           jmp 0x14047ea1d
0047EA6F  B9 03 00 00 00                  mov ecx, 3
0047EA74  CD 29                           int 0x29
0047EA76  48 8D 8E E8 02 00 00            lea rcx, [rsi + 0x2e8]
0047EA7D  E8 CE 98 DC FF                  call 0x140248350
0047EA82  45 33 C0                        xor r8d, r8d
0047EA85  44 39 86 E4 02 00 00            cmp dword ptr [rsi + 0x2e4], r8d
0047EA8C  0F 84 5B FD FF FF               je 0x14047e7ed
0047EA92  41 8B D5                        mov edx, r13d
0047EA95  48 8B CF                        mov rcx, rdi
0047EA98  E8 73 76 D9 FF                  call 0x140216110
0047EA9D  45 33 C0                        xor r8d, r8d
0047EAA0  E9 48 FD FF FF                  jmp 0x14047e7ed
0047EAA5  44 39 A6 E4 02 00 00            cmp dword ptr [rsi + 0x2e4], r12d
0047EAAC  0F 85 94 01 00 00               jne 0x14047ec46
0047EAB2  48 8D 8E E8 03 00 00            lea rcx, [rsi + 0x3e8]
0047EAB9  E8 F2 61 E2 FF                  call 0x1402a4cb0
0047EABE  8B 86 58 48 00 00               mov eax, dword ptr [rsi + 0x4858]
0047EAC4  85 C0                           test eax, eax
0047EAC6  0F 85 8D 01 00 00               jne 0x14047ec59
0047EACC  8B 54 24 40                     mov edx, dword ptr [rsp + 0x40]
0047EAD0  48 8B CF                        mov rcx, rdi
0047EAD3  E8 98 58 F4 FF                  call 0x1403c4370
0047EAD8  48 8D 8E 28 03 00 00            lea rcx, [rsi + 0x328]
0047EADF  45 33 C0                        xor r8d, r8d
0047EAE2  33 D2                           xor edx, edx
0047EAE4  E8 27 08 EC FF                  call 0x14033f310
0047EAE9  48 8B 8D 10 01 00 00            mov rcx, qword ptr [rbp + 0x110]
0047EAF0  48 33 CC                        xor rcx, rsp
0047EAF3  E8 48 DB 22 00                  call 0x1406ac640
0047EAF8  4C 8D 9C 24 20 02 00 00         lea r11, [rsp + 0x220]
0047EB00  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
0047EB04  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
0047EB08  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
0047EB0C  49 8B E3                        mov rsp, r11
0047EB0F  41 5F                           pop r15
0047EB11  41 5E                           pop r14
0047EB13  41 5D                           pop r13
0047EB15  41 5C                           pop r12
0047EB17  5D                              pop rbp
0047EB18  C3                              ret
0047EB19  CC                              int3
0047EB1A  48 8D 87 98 00 00 00            lea rax, [rdi + 0x98]
0047EB21  90                              nop
0047EB22  48 39 00                        cmp qword ptr [rax], rax
0047EB25  0F 84 AF FB FF FF               je 0x14047e6da
0047EB2B  E8 50 41 E6 FF                  call 0x1402e2c80
0047EB30  E9 A5 FB FF FF                  jmp 0x14047e6da
0047EB35  F0 49 0F C1 1E                  lock xadd qword ptr [r14], rbx
0047EB3A  80 E3 06                        and bl, 6
0047EB3D  41 3A DD                        cmp bl, r13b
0047EB40  0F 85 46 61 27 00               jne 0x1406f4c8c
0047EB46  49 8B CE                        mov rcx, r14
0047EB49  E8 82 72 DE FF                  call 0x140265dd0
0047EB4E  90                              nop
0047EB4F  E9 38 61 27 00                  jmp 0x1406f4c8c
0047EB54  44 89 86 D0 04 00 00            mov dword ptr [rsi + 0x4d0], r8d
0047EB5B  33 D2                           xor edx, edx
0047EB5D  45 33 C0                        xor r8d, r8d
0047EB60  49 8B CF                        mov rcx, r15
0047EB63  E8 A8 07 EC FF                  call 0x14033f310
0047EB68  49 8B CE                        mov rcx, r14
0047EB6B  E8 70 3C DB FF                  call 0x1402327e0
0047EB70  45 33 C0                        xor r8d, r8d
0047EB73  49 8D 46 08                     lea rax, [r14 + 8]
0047EB77  4D 89 06                        mov qword ptr [r14], r8
0047EB7A  41 C6 06 08                     mov byte ptr [r14], 8
0047EB7E  48 89 40 08                     mov qword ptr [rax + 8], rax
0047EB82  48 89 00                        mov qword ptr [rax], rax
0047EB85  4D 89 46 18                     mov qword ptr [r14 + 0x18], r8
0047EB89  45 89 46 3C                     mov dword ptr [r14 + 0x3c], r8d
0047EB8D  66 45 89 46 38                  mov word ptr [r14 + 0x38], r8w
0047EB92  E9 63 FC FF FF                  jmp 0x14047e7fa
0047EB97  48 8D 8E 20 04 00 00            lea rcx, [rsi + 0x420]
0047EB9E  E8 AD 97 DC FF                  call 0x140248350
0047EBA3  48 8B CE                        mov rcx, rsi
0047EBA6  E8 91 E3 EC FF                  call 0x14034cf3c
0047EBAB  45 33 C0                        xor r8d, r8d
0047EBAE  E9 61 FC FF FF                  jmp 0x14047e814
0047EBB3  A9 FE FF FF FF                  test eax, 0xfffffffe
0047EBB8  0F 85 73 FC FF FF               jne 0x14047e831
0047EBBE  8B C1                           mov eax, ecx
0047EBC0  F0 44 0F B1 86 B0 04 00 00      lock cmpxchg dword ptr [rsi + 0x4b0], r8d
0047EBC9  0F 85 62 FC FF FF               jne 0x14047e831
0047EBCF  90                              nop
0047EBD0  66 01 8F E6 01 00 00            add word ptr [rdi + 0x1e6], cx
0047EBD7  0F 85 E6 60 27 00               jne 0x1406f4cc3
0047EBDD  48 8D 87 98 00 00 00            lea rax, [rdi + 0x98]
0047EBE4  90                              nop
0047EBE5  48 39 00                        cmp qword ptr [rax], rax
0047EBE8  0F 84 D5 60 27 00               je 0x1406f4cc3
0047EBEE  E8 8D 40 E6 FF                  call 0x1402e2c80
0047EBF3  90                              nop
0047EBF4  E9 CA 60 27 00                  jmp 0x1406f4cc3
0047EBF9  45 33 C0                        xor r8d, r8d
0047EBFC  41 8B D5                        mov edx, r13d
0047EBFF  48 8B CF                        mov rcx, rdi
0047EC02  E8 09 75 D9 FF                  call 0x140216110
0047EC07  E9 98 FD FF FF                  jmp 0x14047e9a4
0047EC0C  B8 01 00 00 00                  mov eax, 1
0047EC11  90                              nop
0047EC12  66 01 87 E6 01 00 00            add word ptr [rdi + 0x1e6], ax
0047EC19  44 8D 60 FF                     lea r12d, [rax - 1]
0047EC1D  0F 85 29 FB FF FF               jne 0x14047e74c
0047EC23  48 8D 87 98 00 00 00            lea rax, [rdi + 0x98]
0047EC2A  90                              nop
0047EC2B  48 39 00                        cmp qword ptr [rax], rax
0047EC2E  0F 84 18 FB FF FF               je 0x14047e74c
0047EC34  E8 47 40 E6 FF                  call 0x1402e2c80
0047EC39  E9 0E FB FF FF                  jmp 0x14047e74c
0047EC3E  45 33 E4                        xor r12d, r12d
0047EC41  E9 5F FE FF FF                  jmp 0x14047eaa5
0047EC46  45 33 C0                        xor r8d, r8d
0047EC49  41 8B D5                        mov edx, r13d
0047EC4C  48 8B CF                        mov rcx, rdi
0047EC4F  E8 BC 74 D9 FF                  call 0x140216110
0047EC54  E9 59 FE FF FF                  jmp 0x14047eab2
0047EC59  4C 8D B6 60 48 00 00            lea r14, [rsi + 0x4860]
0047EC60  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
0047EC65  4C 89 74 24 48                  mov qword ptr [rsp + 0x48], r14
0047EC6A  4C 8B E8                        mov r13, rax
0047EC6D  41 BF 01 00 00 00               mov r15d, 1
0047EC73  E9 5F 60 27 00                  jmp 0x1406f4cd7
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiModifiedPageWriter(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m1D0;
    unsigned __int64 v_stack_m1D8;
    unsigned __int64 v_stack_m1E8;
    unsigned __int64 v_stack_m1F0;
    unsigned __int64 v_stack_m1F8;
    unsigned int v_stack_m208;
    unsigned __int64 v_stack_m210;
    unsigned __int64 v_stack_m218;
    unsigned __int8 v_stack_m220;
    unsigned __int8 v_stack_m228;
    unsigned int v_stack_m248;
    unsigned __int64 v_stack_m28;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (544);
    result = (*(unsigned __int64 *)(v_rip + 10010915)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 328 + 272) = result;
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(*(unsigned __int64 *)(a1) + 1088, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = *(unsigned __int64 *)(a1) + 1088;
        a2 = result;
        a1 = *(unsigned __int64 *)(a1) + 1088;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    v_r12 = 0;
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    a3 = 0;
    a2 = 0;
    result = KeSetEvent(a1 + 8, a2, a3, a4);
    v_rbx = (result) | (-1);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 992)) != 0) goto loc_0047EB35;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 992) = *(unsigned __int64 *)(gs_base + (0 + 392));
    result = (unsigned __int8)((v_rbx) & (6));
    if (((unsigned __int8)(result)) == ((unsigned __int8)(v_rbx + 3))) {
        a1 = *(unsigned __int64 *)(a1) + 1088;
        result = ExfTryToWakePushLock(a1, a2, a3, a4);
    }
    result = KeAbPostRelease(*(unsigned __int64 *)(a1) + 1088, a2, a3, a4);
    if (((unsigned __int8)(result)) == ((unsigned __int8)(v_rbx + 3))) goto loc_0047EB1A;
loc_0047E6DA:
    result = KeSetActualBasePriorityThread(*(unsigned __int64 *)(gs_base + (0 + 392)), 18, a3, a4);
    v_stack_m208 = (unsigned int)(result);
    v_stack_m1F0 = *(unsigned __int64 *)(a1) + 784;
    v_stack_m1F8 = *(unsigned __int64 *)(a1) + 88;
    *(unsigned __int64 *)(v_rsp - 328 - 48) = *(unsigned __int64 *)(a1) + 968;
    *(unsigned __int64 *)(v_rsp - 328 - 64) = *(unsigned __int64 *)(a1) + 88;
    *(unsigned __int64 *)(v_rsp - 328 - 40) = *(unsigned __int64 *)(a1) + 744;
    *(unsigned __int64 *)(v_rsp - 328 - 32) = *(unsigned __int64 *)(a1) + 1056;
    *(unsigned __int64 *)(v_rsp - 328 - 56) = *(unsigned __int64 *)(a1) + 928;
    *(unsigned __int64 *)(v_rsp - 328 - 24) = *(unsigned __int64 *)(a1) + 1240;
loc_0047E74C:
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 888) = 0;
    *(unsigned int *)(*(unsigned __int64 *)(a1) + 896) = 0;
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 722) = 0;
    result = MiStoreCheckCompleteWriteBatch(*(unsigned __int64 *)(a1), *(unsigned __int64 *)(a1) + 88, a3, a4);
    v_stack_m210 = v_stack_m1E8;
    v_stack_m218 = 0;
    v_stack_m220 = 0;
    v_stack_m228 = 0;
    result = KeWaitForMultipleObjects((unsigned int)((unsigned int)(v_rbx + 3)), v_stack_m1F8, 19 - 18, 19);
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 722) = 1;
    if ((unsigned int)(result) == 0) goto loc_0047EAA5;
loc_0047E7A9:
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1) + 92)) != 0) goto loc_0047EAA5;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 19616)) == 0) goto loc_0047E74C;
    result = MiStoreCheckCompleteWriteBatch(*(unsigned __int64 *)(a1), v_stack_m1F8, 19 - 18, 19);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 952)) == (*(unsigned __int64 *)(a1) + 952)) goto loc_0047E8FE;
    a3 = 0;
loc_0047E7E0:
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1) + 748)) != 0) goto loc_0047EA76;
loc_0047E7ED:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 1244)) != 0) goto loc_0047EB54;
loc_0047E7FA:
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1) + 932)) != 0) goto loc_0047E9E3;
loc_0047E807:
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1) + 1060)) != 0) goto loc_0047EB97;
loc_0047E814:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 952)) == (*(unsigned __int64 *)(a1) + 952)) goto loc_0047E9B1;
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 1200))))) != 0) goto loc_0047EBB3;
loc_0047E831:
    result = MiUseLowIoPriorityForModifiedPages(*(unsigned __int64 *)(a1), v_stack_m1F8, a3, 19);
    if ((unsigned int)(result) == 0) goto loc_0047E997;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 19616)) < (*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 776))) goto loc_0047EC0C;
    *(unsigned int *)(*(unsigned __int64 *)(a1) + 768) = 4;
    result = KeSetActualBasePriorityThread(*(unsigned __int64 *)(gs_base + (0 + 392)), 4, a3, 19);
    a1 = 0;
loc_0047E86F:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 952) + 8)) != (*(unsigned __int64 *)(a1) + 952)) goto loc_0047EA6F;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 952)) + 8)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 952))) goto loc_0047EA6F;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 952) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 952));
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 952)) + 8) = *(unsigned __int64 *)(a1) + 952;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 952) + 40))) & (0xFFFFFFE3ULL));
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 952)) = 97;
    result = (unsigned int)((result) | (0));
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 952) + 40) = (unsigned int)(result);
    if (condition_is_not_equal) goto loc_0047E8C7;
    result = *(unsigned __int64 *)(gs_base + (0 + 392)) + 152;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 152)) != (*(unsigned __int64 *)(gs_base + (0 + 392)) + 152)) {
        result = KiCheckForKernelApcDelivery(a1, 4, a3, 19);
    }
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 952) + 96) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 952) + 104;
    result = MiGatherPagefilePages(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 952), 4, a3, 19);
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != ((unsigned int)(v_rbx))) goto loc_0047E970;
loc_0047E8E0:
    result = MiCheckFreeModifiedReservations(*(unsigned __int64 *)(a1), 4, a3, 19);
    v_r12 = 0;
    goto loc_0047E7A9;
loc_0047E8FE:
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 721) = 1;
    if (condition_is_not_equal) goto loc_0047E925;
    result = *(unsigned __int64 *)(gs_base + (0 + 392)) + 152;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 152)) != (*(unsigned __int64 *)(gs_base + (0 + 392)) + 152)) {
        result = KiCheckForKernelApcDelivery(*(unsigned __int64 *)(a1), 4, a3, 19);
    }
    v_stack_m210 = v_rsp - 328 - 16;
    result = 0;
    v_stack_m218 = 0;
    v_stack_m220 = 0;
    v_stack_m228 = 0;
    result = KeWaitForMultipleObjects(result + 6, v_rsp - 328 - 64, result + 1, result + 19);
    a3 = 0;
    if ((unsigned int)(result) == 0) goto loc_0047EC3E;
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 721) = 0;
    goto loc_0047E7E0;
loc_0047E970:
    result = KeQueryPriorityThread(*(unsigned __int64 *)(gs_base + (0 + 392)), v_rsp - 328 - 64, a3, result + 19);
    if (((unsigned int)(result)) != 18) {
        a2 = (unsigned int)(*(unsigned __int64 *)(a1) + 928);
        a1 = *(unsigned __int64 *)(gs_base + (0 + 392));
        result = KeSetActualBasePriorityThread(a1, a2, a3, result + 19);
    }
    *(unsigned int *)(*(unsigned __int64 *)(a1) + 768) = 18;
    goto loc_0047E8E0;
loc_0047E997:
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1) + 740)) != 0) goto loc_0047EBF9;
loc_0047E9A4:
    goto loc_0047E86F;
loc_0047E9B1:
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1) + 740)) != 0) goto loc_0047E7A9;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 152)) == (*(unsigned __int64 *)(gs_base + (0 + 392)) + 152)) goto loc_0047E7A9;
    result = KiCheckForKernelApcDelivery(8, a2, a3, result + 19);
    goto loc_0047E7A9;
loc_0047E9E3:
    result = KeResetEvent((unsigned int)((unsigned int)(v_rbx)), a2, a3, result + 19);
    a3 = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 18520))) == 0) goto loc_0047E807;
loc_0047EA0F:
    if ((((unsigned __int8)(a3 + 1)) & ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 18528) + 174)))) != 0) goto loc_0047EA2B;
loc_0047EA1D:
    a2 = (*(unsigned __int64 *)(a1) + 18528) + (8);
    v_r10 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 18520))))) - (a3 + 1);
    if (condition_is_not_equal) goto loc_0047EA0F;
    goto loc_0047E807;
loc_0047EA2B:
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 18528) + 174)) & (254));
    *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 18528) + 174) = (unsigned __int8)(result);
    if ((*(unsigned int *)(*(unsigned __int64 *)(a2) + 40)) <= 0) goto loc_0047EA1D;
loc_0047EA3F:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2) + 32) + 0 * 8) == 0) goto loc_0047EA61;
    result = (unsigned int)(0x99887711ULL);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2) + 32) + 0 * 8))) == ((unsigned int)(0x99887711ULL))) {
        result = MiMakePagefileWriterEntryAvailable(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2) + 32) + 0 * 8), a2, a3, 0);
        a3 = 0;
    }
    a4 = (unsigned int)((0) + ((unsigned int)(a3 + 1)));
    if (((unsigned int)(a4)) < (*(unsigned int *)(*(unsigned __int64 *)(a2) + 40))) goto loc_0047EA3F;
    goto loc_0047EA1D;
loc_0047EA6F:
loc_0047EA76:
    result = KeResetEvent(*(unsigned __int64 *)(a1) + 744, a2, a3, a4);
    a3 = 0;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1) + 740)) == 0) goto loc_0047E7ED;
    result = IoBoostThreadIoPriority(*(unsigned __int64 *)(gs_base + (0 + 392)), (unsigned int)((unsigned int)(v_rbx + 3)), a3, a4);
    a3 = 0;
    goto loc_0047E7ED;
loc_0047EAA5:
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1) + 740)) != ((unsigned int)(1 - 1))) goto loc_0047EC46;
loc_0047EAB2:
    result = ExWaitForRundownProtectionRelease(*(unsigned __int64 *)(a1) + 1000, (unsigned int)((unsigned int)(v_rbx + 3)), a3, a4);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 18520))) != 0) goto loc_0047EC59;
    result = KeSetActualBasePriorityThread(*(unsigned __int64 *)(gs_base + (0 + 392)), (unsigned int)(v_stack_m208), a3, a4);
    a3 = 0;
    a2 = 0;
    result = KeSetEvent(*(unsigned __int64 *)(a1) + 808, a2, a3, a4);
    a1 = (*(unsigned __int64 *)(v_rsp - 328 + 272)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    return result;
loc_0047EB1A:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 152)) == (*(unsigned __int64 *)(v_stack_m28 + 72) + 152)) goto loc_0047E6DA;
    result = KiCheckForKernelApcDelivery(a1, a2, a3, a4);
    goto loc_0047E6DA;
loc_0047EB35:
    v_rbx = (unsigned __int8)((*(unsigned __int64 *)(v_stack_m28 + 56)) & (6));
    result = ExfTryToWakePushLock(*(unsigned __int64 *)(a1) + 1240, a2, a3, a4);
loc_0047EB54:
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 1232) = 0;
    a2 = 0;
    a3 = 0;
    result = KeSetEvent((unsigned int)((unsigned int)(v_rbx)), a2, a3, a4);
    result = KeCancelTimer(*(unsigned __int64 *)(a1) + 1240, a2, a3, a4);
    a3 = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 1240) = 0;
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 1240) = 8;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 1240 + 8 + 8) = *(unsigned __int64 *)(a1) + 1240 + 8;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 1240 + 8) = *(unsigned __int64 *)(a1) + 1240 + 8;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 1240 + 24) = 0;
    *(unsigned int *)(*(unsigned __int64 *)(a1) + 1240 + 60) = 0;
    *(unsigned __int16 *)(*(unsigned __int64 *)(a1) + 1240 + 56) = 0;
    goto loc_0047E7FA;
loc_0047EB97:
    result = KeResetEvent(*(unsigned __int64 *)(v_stack_m28 + 64) + 1056, a2, a3, a4);
    result = MiStoreUpdateMemoryConditions(*(unsigned __int64 *)(v_stack_m28 + 64), a2, a3, a4);
    a3 = 0;
    goto loc_0047E814;
loc_0047EBB3:
    if ((((unsigned int)(result)) & (0xFFFFFFFEULL)) != 0) goto loc_0047E831;
    if ((((unsigned int)(result)) & (0xFFFFFFFEULL)) != 0) goto loc_0047E831;
    result = KiCheckForKernelApcDelivery(*(unsigned __int64 *)(v_stack_m28 + 64), a2, a3, a4);
loc_0047EBF9:
    a3 = 0;
    result = IoBoostThreadIoPriority(*(unsigned __int64 *)(v_stack_m28 + 72), (unsigned int)((unsigned int)(v_rbx + 3)), a3, a4);
    goto loc_0047E9A4;
loc_0047EC0C:
    if (condition_is_not_equal) goto loc_0047E74C;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 152)) == (*(unsigned __int64 *)(v_stack_m28 + 72) + 152)) goto loc_0047E74C;
    result = KiCheckForKernelApcDelivery(*(unsigned __int64 *)(v_stack_m28 + 72), (unsigned int)((unsigned int)(v_rbx + 3)), a3, a4);
    goto loc_0047E74C;
loc_0047EC3E:
    v_r12 = 0;
    goto loc_0047EAA5;
loc_0047EC46:
    a3 = 0;
    result = IoBoostThreadIoPriority(*(unsigned __int64 *)(v_stack_m28 + 72), (unsigned int)((unsigned int)(v_rbx + 3)), a3, a4);
    goto loc_0047EAB2;
loc_0047EC59:
    v_stack_m1D0 = result;
    v_stack_m1D8 = *(unsigned __int64 *)(v_stack_m28 + 64) + 18528;
}
```

## 5. (Beta) C Style

```c
int64_t MiModifiedPageWriter(void *Arg1, int32_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m1D0;
    uint64_t v_stack_m1D8;
    uint64_t v_stack_m1E8;
    uint64_t v_stack_m1F0;
    uint64_t v_stack_m1F8;
    uint32_t v_stack_m208;
    uint64_t v_stack_m210;
    uint64_t v_stack_m218;
    uint8_t v_stack_m220;
    uint8_t v_stack_m228;
    uint32_t v_stack_m248;
    uint64_t v_stack_m28;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (544);
    result = (*(uint64_t *)(v_rip + 0x98C123)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x148 + 0x110) = result;
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(*(uint64_t *)(arg1) + 1088, Arg2, Arg3, a4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = *(uint64_t *)(arg1) + 1088;
        Arg2 = result;
        Arg1 = *(uint64_t *)(arg1) + 1088;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, a4);
    }
    local_r12 = 0;
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    Arg3 = 0;
    Arg2 = 0;
    result = KeSetEvent(Arg1 + 8, Arg2, Arg3, a4);
    local_rbx = (result) | (-1);
    if ((*(uint64_t *)(*(uint64_t *)(arg1) + 0x3E0)) != 0) goto loc_0047EB35;
    *(uint64_t *)(*(uint64_t *)(arg1) + 0x3E0) = *(uint64_t *)(gs_base + (0 + 0x188));
    result = (uint8_t)((local_rbx) & (6));
    if (((uint8_t)(result)) == ((uint8_t)(local_rbx + 3))) {
        Arg1 = *(uint64_t *)(arg1) + 1088;
        result = ExfTryToWakePushLock(Arg1, Arg2, Arg3, a4);
    }
    result = KeAbPostRelease(*(uint64_t *)(arg1) + 1088, Arg2, Arg3, a4);
    if (((uint8_t)(result)) == ((uint8_t)(local_rbx + 3))) goto loc_0047EB1A;
loc_0047E6DA:
    result = KeSetActualBasePriorityThread(*(uint64_t *)(gs_base + (0 + 0x188)), 18, Arg3, a4);
    v_stack_m208 = (uint32_t)(result);
    v_stack_m1F0 = *(uint64_t *)(arg1) + 784;
    v_stack_m1F8 = *(uint64_t *)(arg1) + 88;
    *(uint64_t *)(local_rsp - 0x148 - 0x30) = *(uint64_t *)(arg1) + 968;
    *(uint64_t *)(local_rsp - 0x148 - 0x40) = *(uint64_t *)(arg1) + 88;
    *(uint64_t *)(local_rsp - 0x148 - 0x28) = *(uint64_t *)(arg1) + 744;
    *(uint64_t *)(local_rsp - 0x148 - 0x20) = *(uint64_t *)(arg1) + 1056;
    *(uint64_t *)(local_rsp - 0x148 - 0x38) = *(uint64_t *)(arg1) + 928;
    *(uint64_t *)(local_rsp - 0x148 - 0x18) = *(uint64_t *)(arg1) + 1240;
loc_0047E74C:
    *(uint64_t *)(*(uint64_t *)(arg1) + 0x378) = 0;
    *(uint32_t *)(*(uint64_t *)(arg1) + 0x380) = 0;
    *(uint8_t *)(*(uint64_t *)(arg1) + 0x2D2) = 0;
    result = MiStoreCheckCompleteWriteBatch(*(uint64_t *)(arg1), *(uint64_t *)(arg1) + 88, Arg3, a4);
    v_stack_m210 = v_stack_m1E8;
    v_stack_m218 = 0;
    v_stack_m220 = 0;
    v_stack_m228 = 0;
    result = KeWaitForMultipleObjects((uint32_t)((uint32_t)(local_rbx + 3)), v_stack_m1F8, 19 - 18, 19);
    *(uint8_t *)(*(uint64_t *)(arg1) + 0x2D2) = 1;
    if ((uint32_t)(result) == 0) goto loc_0047EAA5;
loc_0047E7A9:
    if ((*(uint32_t *)(*(uint64_t *)(arg1) + 0x5C)) != 0) goto loc_0047EAA5;
    if ((*(uint64_t *)(*(uint64_t *)(arg1) + 0x4CA0)) == 0) goto loc_0047E74C;
    result = MiStoreCheckCompleteWriteBatch(*(uint64_t *)(arg1), v_stack_m1F8, 19 - 18, 19);
    if ((*(uint64_t *)(*(uint64_t *)(arg1) + 0x3B8)) == (*(uint64_t *)(arg1) + 952)) goto loc_0047E8FE;
    Arg3 = 0;
loc_0047E7E0:
    if ((*(uint32_t *)(*(uint64_t *)(arg1) + 0x2EC)) != 0) goto loc_0047EA76;
loc_0047E7ED:
    if ((*(uint8_t *)(*(uint64_t *)(arg1) + 0x4DC)) != 0) goto loc_0047EB54;
loc_0047E7FA:
    if ((*(uint32_t *)(*(uint64_t *)(arg1) + 0x3A4)) != 0) goto loc_0047E9E3;
loc_0047E807:
    if ((*(uint32_t *)(*(uint64_t *)(arg1) + 0x424)) != 0) goto loc_0047EB97;
loc_0047E814:
    if ((*(uint64_t *)(*(uint64_t *)(arg1) + 0x3B8)) == (*(uint64_t *)(arg1) + 952)) goto loc_0047E9B1;
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x4B0))))) != 0) goto loc_0047EBB3;
loc_0047E831:
    result = MiUseLowIoPriorityForModifiedPages(*(uint64_t *)(arg1), v_stack_m1F8, Arg3, 19);
    if ((uint32_t)(result) == 0) goto loc_0047E997;
    if ((*(uint64_t *)(*(uint64_t *)(arg1) + 0x4CA0)) < (*(uint64_t *)(*(uint64_t *)(arg1) + 0x308))) goto loc_0047EC0C;
    *(uint32_t *)(*(uint64_t *)(arg1) + 0x300) = 4;
    result = KeSetActualBasePriorityThread(*(uint64_t *)(gs_base + (0 + 0x188)), 4, Arg3, 19);
    Arg1 = 0;
loc_0047E86F:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x3B8) + 0x8)) != (*(uint64_t *)(arg1) + 952)) goto loc_0047EA6F;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x3B8)) + 0x8)) != (*(uint64_t *)(*(uint64_t *)(arg1) + 0x3B8))) goto loc_0047EA6F;
    *(uint64_t *)(*(uint64_t *)(arg1) + 0x3B8) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x3B8));
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x3B8)) + 0x8) = *(uint64_t *)(arg1) + 952;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x3B8) + 0x28))) & (0xFFFFFFE3ULL));
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x3B8)) = 97;
    result = (uint32_t)((result) | (0));
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x3B8) + 0x28) = (uint32_t)(result);
    if (condition_is_not_equal) goto loc_0047E8C7;
    result = *(uint64_t *)(gs_base + (0 + 0x188)) + 152;
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x98)) != (*(uint64_t *)(gs_base + (0 + 0x188)) + 152)) {
        result = KiCheckForKernelApcDelivery(Arg1, 4, Arg3, 19);
    }
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x3B8) + 0x60) = *(uint64_t *)(*(uint64_t *)(arg1) + 0x3B8) + 104;
    result = MiGatherPagefilePages(*(uint64_t *)(*(uint64_t *)(arg1) + 0x3B8), 4, Arg3, 19);
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != ((uint32_t)(local_rbx))) goto loc_0047E970;
loc_0047E8E0:
    result = MiCheckFreeModifiedReservations(*(uint64_t *)(arg1), 4, Arg3, 19);
    local_r12 = 0;
    goto loc_0047E7A9;
loc_0047E8FE:
    *(uint8_t *)(*(uint64_t *)(arg1) + 0x2D1) = 1;
    if (condition_is_not_equal) goto loc_0047E925;
    result = *(uint64_t *)(gs_base + (0 + 0x188)) + 152;
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x98)) != (*(uint64_t *)(gs_base + (0 + 0x188)) + 152)) {
        result = KiCheckForKernelApcDelivery(*(uint64_t *)(arg1), 4, Arg3, 19);
    }
    v_stack_m210 = local_rsp - 328 - 16;
    result = 0;
    v_stack_m218 = 0;
    v_stack_m220 = 0;
    v_stack_m228 = 0;
    result = KeWaitForMultipleObjects(result + 6, local_rsp - 328 - 64, result + 1, result + 19);
    Arg3 = 0;
    if ((uint32_t)(result) == 0) goto loc_0047EC3E;
    *(uint8_t *)(*(uint64_t *)(arg1) + 0x2D1) = 0;
    goto loc_0047E7E0;
loc_0047E970:
    result = KeQueryPriorityThread(*(uint64_t *)(gs_base + (0 + 0x188)), local_rsp - 328 - 64, Arg3, result + 19);
    if (((uint32_t)(result)) != 18) {
        Arg2 = (uint32_t)(*(uint64_t *)(arg1) + 928);
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x188));
        result = KeSetActualBasePriorityThread(Arg1, Arg2, Arg3, result + 19);
    }
    *(uint32_t *)(*(uint64_t *)(arg1) + 0x300) = 18;
    goto loc_0047E8E0;
loc_0047E997:
    if ((*(uint32_t *)(*(uint64_t *)(arg1) + 0x2E4)) != 0) goto loc_0047EBF9;
loc_0047E9A4:
    goto loc_0047E86F;
loc_0047E9B1:
    if ((*(uint32_t *)(*(uint64_t *)(arg1) + 0x2E4)) != 0) goto loc_0047E7A9;
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x98)) == (*(uint64_t *)(gs_base + (0 + 0x188)) + 152)) goto loc_0047E7A9;
    result = KiCheckForKernelApcDelivery(8, Arg2, Arg3, result + 19);
    goto loc_0047E7A9;
loc_0047E9E3:
    result = KeResetEvent((uint32_t)((uint32_t)(local_rbx)), Arg2, Arg3, result + 19);
    Arg3 = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x4858))) == 0) goto loc_0047E807;
loc_0047EA0F:
    if ((((uint8_t)(Arg3 + 1)) & ((uint8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x4860) + 0xAE)))) != 0) goto loc_0047EA2B;
loc_0047EA1D:
    Arg2 = (*(uint64_t *)(arg1) + 18528) + (8);
    local_r10 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x4858))))) - (Arg3 + 1);
    if (condition_is_not_equal) goto loc_0047EA0F;
    goto loc_0047E807;
loc_0047EA2B:
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x4860) + 0xAE)) & (254));
    *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x4860) + 0xAE) = (uint8_t)(result);
    if ((*(uint32_t *)(*(uint64_t *)(Arg2) + 0x28)) <= 0) goto loc_0047EA1D;
loc_0047EA3F:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg2) + 0x20) + 0x0 * 8) == 0) goto loc_0047EA61;
    result = (uint32_t)(0x99887711ULL);
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg2) + 0x20) + 0x0 * 8))) == ((uint32_t)(0x99887711ULL))) {
        result = MiMakePagefileWriterEntryAvailable(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg2) + 0x20) + 0x0 * 8), Arg2, Arg3, 0);
        Arg3 = 0;
    }
    a4 = (uint32_t)((0) + ((uint32_t)(Arg3 + 1)));
    if (((uint32_t)(a4)) < (*(uint32_t *)(*(uint64_t *)(Arg2) + 0x28))) goto loc_0047EA3F;
    goto loc_0047EA1D;
loc_0047EA6F:
loc_0047EA76:
    result = KeResetEvent(*(uint64_t *)(arg1) + 744, Arg2, Arg3, a4);
    Arg3 = 0;
    if ((*(uint32_t *)(*(uint64_t *)(arg1) + 0x2E4)) == 0) goto loc_0047E7ED;
    result = IoBoostThreadIoPriority(*(uint64_t *)(gs_base + (0 + 0x188)), (uint32_t)((uint32_t)(local_rbx + 3)), Arg3, a4);
    Arg3 = 0;
    goto loc_0047E7ED;
loc_0047EAA5:
    if ((*(uint32_t *)(*(uint64_t *)(arg1) + 0x2E4)) != ((uint32_t)(1 - 1))) goto loc_0047EC46;
loc_0047EAB2:
    result = ExWaitForRundownProtectionRelease(*(uint64_t *)(arg1) + 1000, (uint32_t)((uint32_t)(local_rbx + 3)), Arg3, a4);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x4858))) != 0) goto loc_0047EC59;
    result = KeSetActualBasePriorityThread(*(uint64_t *)(gs_base + (0 + 0x188)), (uint32_t)(v_stack_m208), Arg3, a4);
    Arg3 = 0;
    Arg2 = 0;
    result = KeSetEvent(*(uint64_t *)(arg1) + 808, Arg2, Arg3, a4);
    Arg1 = (*(uint64_t *)(local_rsp - 0x148 + 0x110)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, a4);
    return result;
loc_0047EB1A:
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x98)) == (*(uint64_t *)(v_stack_m28 + 0x48) + 152)) goto loc_0047E6DA;
    result = KiCheckForKernelApcDelivery(Arg1, Arg2, Arg3, a4);
    goto loc_0047E6DA;
loc_0047EB35:
    local_rbx = (uint8_t)((*(uint64_t *)(v_stack_m28 + 0x38)) & (6));
    result = ExfTryToWakePushLock(*(uint64_t *)(arg1) + 1240, Arg2, Arg3, a4);
loc_0047EB54:
    *(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x4D0) = 0;
    Arg2 = 0;
    Arg3 = 0;
    result = KeSetEvent((uint32_t)((uint32_t)(local_rbx)), Arg2, Arg3, a4);
    result = KeCancelTimer(*(uint64_t *)(arg1) + 1240, Arg2, Arg3, a4);
    Arg3 = 0;
    *(uint64_t *)(*(uint64_t *)(arg1) + 0x4D8) = 0;
    *(uint8_t *)(*(uint64_t *)(arg1) + 0x4D8) = 8;
    *(uint64_t *)(*(uint64_t *)(arg1) + 0x4D8 + 0x8 + 0x8) = *(uint64_t *)(arg1) + 1240 + 8;
    *(uint64_t *)(*(uint64_t *)(arg1) + 0x4D8 + 0x8) = *(uint64_t *)(arg1) + 1240 + 8;
    *(uint64_t *)(*(uint64_t *)(arg1) + 0x4D8 + 0x18) = 0;
    *(uint32_t *)(*(uint64_t *)(arg1) + 0x4D8 + 0x3C) = 0;
    *(uint16_t *)(*(uint64_t *)(arg1) + 0x4D8 + 0x38) = 0;
    goto loc_0047E7FA;
loc_0047EB97:
    result = KeResetEvent(*(uint64_t *)(v_stack_m28 + 0x40) + 1056, Arg2, Arg3, a4);
    result = MiStoreUpdateMemoryConditions(*(uint64_t *)(v_stack_m28 + 0x40), Arg2, Arg3, a4);
    Arg3 = 0;
    goto loc_0047E814;
loc_0047EBB3:
    if ((((uint32_t)(result)) & (0xFFFFFFFEULL)) != 0) goto loc_0047E831;
    if ((((uint32_t)(result)) & (0xFFFFFFFEULL)) != 0) goto loc_0047E831;
    result = KiCheckForKernelApcDelivery(*(uint64_t *)(v_stack_m28 + 0x40), Arg2, Arg3, a4);
loc_0047EBF9:
    Arg3 = 0;
    result = IoBoostThreadIoPriority(*(uint64_t *)(v_stack_m28 + 0x48), (uint32_t)((uint32_t)(local_rbx + 3)), Arg3, a4);
    goto loc_0047E9A4;
loc_0047EC0C:
    if (condition_is_not_equal) goto loc_0047E74C;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x98)) == (*(uint64_t *)(v_stack_m28 + 0x48) + 152)) goto loc_0047E74C;
    result = KiCheckForKernelApcDelivery(*(uint64_t *)(v_stack_m28 + 0x48), (uint32_t)((uint32_t)(local_rbx + 3)), Arg3, a4);
    goto loc_0047E74C;
loc_0047EC3E:
    local_r12 = 0;
    goto loc_0047EAA5;
loc_0047EC46:
    Arg3 = 0;
    result = IoBoostThreadIoPriority(*(uint64_t *)(v_stack_m28 + 0x48), (uint32_t)((uint32_t)(local_rbx + 3)), Arg3, a4);
    goto loc_0047EAB2;
loc_0047EC59:
    v_stack_m1D0 = result;
    v_stack_m1D8 = *(uint64_t *)(v_stack_m28 + 0x40) + 18528;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0047E5F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
