# KiSetPriorityThread

- RVA: `0x00220E78`–`0x002213AB` (길이 `1,331` bytes)
- VA: `0x0000000140220E78`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0005F4A8`
- 디코드: `353`개 명령, `1,331/1,331` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **23**; 고유 호출 대상: **20**
- 직접 호출자로 확인된 함수: **26**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x00220F92` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00220FA0` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00220FF3` → [KiRemoveThreadFromAnyReadyQueue](../20/KiRemoveThreadFromAnyReadyQueue_function_002015E4.md) (function, `0x002015E4`)
- `0x00221006` → [KiUpdateThreadPriority](../25/KiUpdateThreadPriority_function_00257810.md) (function, `0x00257810`)
- `0x00221018` → [KiPrepareReadyThreadForRescheduling](../39/KiPrepareReadyThreadForRescheduling_function_00397F2C.md) (function, `0x00397F2C`)
- `0x00221022` → [KiUpdateSharedReadyQueueAffinityThread](../2C/KiUpdateSharedReadyQueueAffinityThread_function_002CE470.md) (function, `0x002CE470`)
- `0x0022103E` → [KiStartRescheduleContext](../30/KiStartRescheduleContext_function_0030C6B0.md) (function, `0x0030C6B0`)
- `0x00221049` → [KiFindRescheduleContextEntryForPrcb](../35/KiFindRescheduleContextEntryForPrcb_function_00353060.md) (function, `0x00353060`)
- `0x00221055` → [KiSearchForNewThreadsForRescheduleContext](../25/KiSearchForNewThreadsForRescheduleContext_function_00258620.md) (function, `0x00258620`)
- `0x00221066` → [KiCommitRescheduleContext](../30/KiCommitRescheduleContext_function_0030CF20.md) (function, `0x0030CF20`)
- `0x00221081` → [KiReleaseThreadStateLock](../21/KiReleaseThreadStateLock_function_00217910.md) (function, `0x00217910`)
- `0x002210CB` → [KiUpdateThreadPriority](../25/KiUpdateThreadPriority_function_00257810.md) (function, `0x00257810`)
- `0x00221115` → [KiAcquireMultiplePrcbLocks](../39/KiAcquireMultiplePrcbLocks_function_00393160.md) (function, `0x00393160`)
- `0x0022115F` → [KiUpdateThreadPriority](../25/KiUpdateThreadPriority_function_00257810.md) (function, `0x00257810`)
- `0x002211FC` → [KiAcquirePrcbLocksForIsolationUnit](../30/KiAcquirePrcbLocksForIsolationUnit_function_0030ED60.md) (function, `0x0030ED60`)
- `0x0022121D` → [KiReleasePrcbLocksForIsolationUnit](../39/KiReleasePrcbLocksForIsolationUnit_function_00399C50.md) (function, `0x00399C50`)
- `0x0022129D` → [KxWaitForLockChainValid](../21/KxWaitForLockChainValid_function_00217AA0.md) (function, `0x00217AA0`)
- `0x002212C8` → [KeWakeAddressAll](../21/KeWakeAddressAll_function_00217C20.md) (function, `0x00217C20`)
- `0x002212DF` → [KxWaitForLockOwnerShip](../25/KxWaitForLockOwnerShip_function_00257EB0.md) (function, `0x00257EB0`)
- `0x0022130E` → [KiCompleteRescheduleContextEntry](../35/KiCompleteRescheduleContextEntry_function_00356330.md) (function, `0x00356330`)
- `0x00221324` → [KiFlushSoftwareInterruptBatch](../25/KiFlushSoftwareInterruptBatch_function_00252200.md) (function, `0x00252200`)
- `0x0022134B` → [KiUpdateThreadPriority](../25/KiUpdateThreadPriority_function_00257810.md) (function, `0x00257810`)
- `0x002213A1` → [KiHvEnlightenedGuestPriorityKick](../44/KiHvEnlightenedGuestPriorityKick_function_00443880.md) (function, `0x00443880`)

### Direct callers
- [sub_002099FA](../20/Unknown_function_002099FA.md) at `0x00209BFD`
- [sub_0020C2D4](../20/Unknown_function_0020C2D4.md) at `0x0020C94C`
- [sub_0020C2D4](../20/Unknown_function_0020C2D4.md) at `0x0020CAD2`
- [KeWaitForSingleObject](../20/KeWaitForSingleObject_function_0020E6B0.md) at `0x0020F065`
- [KeWaitForSingleObject](../20/KeWaitForSingleObject_function_0020E6B0.md) at `0x0020F457`
- [sub_00210BCA](../21/Unknown_function_00210BCA.md) at `0x00210D42`
- [sub_0021F36F](../21/Unknown_function_0021F36F.md) at `0x0021F3A6`
- [KiWakePriQueueWaiter](../21/KiWakePriQueueWaiter_function_0021F720.md) at `0x0021F90F`
- [sub_0021FF3E](../21/Unknown_function_0021FF3E.md) at `0x0021FF83`
- [sub_002202B6](Unknown_function_002202B6.md) at `0x00220390`
- [sub_0022053D](Unknown_function_0022053D.md) at `0x002205FC`
- [sub_002208AD](Unknown_function_002208AD.md) at `0x00220938`
- [KiFastExitThreadWait](KiFastExitThreadWait_function_00220BB0.md) at `0x00220DA7`
- [KeSetPriorityThread](../2C/KeSetPriorityThread_function_002C76E0.md) at `0x002C781A`
- [KiSetSystemPriorityThread](../2D/KiSetSystemPriorityThread_function_002D9FF8.md) at `0x002DA080`
- [KiUpdateVpBackingThreadPriorityFromTopLevel](../30/KiUpdateVpBackingThreadPriorityFromTopLevel_function_00303BA0.md) at `0x00303CDE`
- [sub_00352D10](../35/Unknown_function_00352D10.md) at `0x00352DCD`
- [KeAdjustWobPriority](../39/KeAdjustWobPriority_function_00393570.md) at `0x00393700`
- [KiClearPriorityFloor](../39/KiClearPriorityFloor_function_00396314.md) at `0x0039644D`
- [KiSetPriorityBoost](../39/KiSetPriorityBoost_function_00398A40.md) at `0x00398A6C`
- [KiSetDisableBoostThread](../3C/KiSetDisableBoostThread_function_003C1A5C.md) at `0x003C1B0F`
- [KeSetPriorityAndQuantumProcess](../3C/KeSetPriorityAndQuantumProcess_function_003C2EC0.md) at `0x003C315A`
- [KeAdjustPriorityFloor](../3C/KeAdjustPriorityFloor_function_003C3574.md) at `0x003C36A0`
- [KeSetActualBasePriorityThread](../3C/KeSetActualBasePriorityThread_function_003C4370.md) at `0x003C4503`
- [KeRemovePriQueue](../3C/KeRemovePriQueue_function_003C5090.md) at `0x003C55DF`
- [KeSetBasePriorityThread](../3C/KeSetBasePriorityThread_function_003C6EB0.md) at `0x003C7098`
- [KeBoostPriorityThread](../4D/KeBoostPriorityThread_function_004D37F8.md) at `0x004D39AA`
- [sub_006E7EC2](../6E/Unknown_function_006E7EC2.md) at `0x006E7F8B`

### Static image references
- `0x00220EBB` → RVA `0x00FC8C40` (`ALMOSTRO`; read)
- `0x00220F73` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x00220F88` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x002211B8` → RVA `0x00FC6B38` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x002211E0` → [sub_006D69EA](../6D/Unknown_function_006D69EA.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00220E78  44 89 44 24 18                  mov dword ptr [rsp + 0x18], r8d
00220E7D  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
00220E82  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
00220E87  55                              push rbp
00220E88  53                              push rbx
00220E89  56                              push rsi
00220E8A  57                              push rdi
00220E8B  41 54                           push r12
00220E8D  41 55                           push r13
00220E8F  41 56                           push r14
00220E91  41 57                           push r15
00220E93  48 8B EC                        mov rbp, rsp
00220E96  48 83 EC 68                     sub rsp, 0x68
00220E9A  0F BE 81 C3 00 00 00            movsx eax, byte ptr [rcx + 0xc3]
00220EA1  48 8B F9                        mov rdi, rcx
00220EA4  41 3B C0                        cmp eax, r8d
00220EA7  0F 84 2C 02 00 00               je 0x1402210d9
00220EAD  0F 57 C0                        xorps xmm0, xmm0
00220EB0  45 33 C0                        xor r8d, r8d
00220EB3  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
00220EB7  4C 89 45 D8                     mov qword ptr [rbp - 0x28], r8
00220EBB  48 8D 15 7E 7D DA 00            lea rdx, [rip + 0xda7d7e]
00220EC2  44 0F B6 B7 84 01 00 00         movzx r14d, byte ptr [rdi + 0x184]
00220ECA  49 8B F0                        mov rsi, r8
00220ECD  41 8B CE                        mov ecx, r14d
00220ED0  4C 89 45 D0                     mov qword ptr [rbp - 0x30], r8
00220ED4  44 88 75 60                     mov byte ptr [rbp + 0x60], r14b
00220ED8  4D 8B D0                        mov r10, r8
00220EDB  83 E9 01                        sub ecx, 1
00220EDE  0F 84 C4 02 00 00               je 0x1402211a8
00220EE4  83 E9 01                        sub ecx, 1
00220EE7  0F 84 FD 01 00 00               je 0x1402210ea
00220EED  83 E9 01                        sub ecx, 1
00220EF0  0F 85 B4 00 00 00               jne 0x140220faa
00220EF6  44 8B A7 18 02 00 00            mov r12d, dword ptr [rdi + 0x218]
00220EFD  45 85 E4                        test r12d, r12d
00220F00  78 C0                           js 0x140220ec2
00220F02  4A 8B 34 E2                     mov rsi, qword ptr [rdx + r12*8]
00220F06  48 8B C6                        mov rax, rsi
00220F09  48 83 C8 01                     or rax, 1
00220F0D  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
00220F11  48 8B 86 58 8E 00 00            mov rax, qword ptr [rsi + 0x8e58]
00220F18  0F B6 08                        movzx ecx, byte ptr [rax]
00220F1B  4C 8D 78 08                     lea r15, [rax + 8]
00220F1F  84 C9                           test cl, cl
00220F21  74 24                           je 0x140220f47
00220F23  44 8B E9                        mov r13d, ecx
00220F26  4D 8B 37                        mov r14, qword ptr [r15]
00220F29  41 8B D8                        mov ebx, r8d
00220F2C  F0 49 0F BA 6E 30 00            lock bts qword ptr [r14 + 0x30], 0
00220F33  72 3C                           jb 0x140220f71
00220F35  49 83 C7 08                     add r15, 8
00220F39  49 83 ED 01                     sub r13, 1
00220F3D  75 E7                           jne 0x140220f26
00220F3F  4C 8B 55 D0                     mov r10, qword ptr [rbp - 0x30]
00220F43  44 8A 75 60                     mov r14b, byte ptr [rbp + 0x60]
00220F47  48 3B 7E 10                     cmp rdi, qword ptr [rsi + 0x10]
00220F4B  74 6F                           je 0x140220fbc
00220F4D  8A 87 84 01 00 00               mov al, byte ptr [rdi + 0x184]
00220F53  3C 03                           cmp al, 3
00220F55  0F 85 BE 02 00 00               jne 0x140221219
00220F5B  8B 87 18 02 00 00               mov eax, dword ptr [rdi + 0x218]
00220F61  41 3B C4                        cmp eax, r12d
00220F64  0F 85 AF 02 00 00               jne 0x140221219
00220F6A  B9 1E 00 00 00                  mov ecx, 0x1e
00220F6F  CD 29                           int 0x29
00220F71  FF C3                           inc ebx
00220F73  85 1D 33 43 DA 00               test dword ptr [rip + 0xda4333], ebx
00220F79  74 0D                           je 0x140220f88
00220F7B  F3 90                           pause
00220F7D  49 8B 46 30                     mov rax, qword ptr [r14 + 0x30]
00220F81  48 85 C0                        test rax, rax
00220F84  74 A6                           je 0x140220f2c
00220F86  EB E9                           jmp 0x140220f71
00220F88  8B 05 2A 5B DA 00               mov eax, dword ptr [rip + 0xda5b2a]
00220F8E  A8 40                           test al, 0x40
00220F90  74 E9                           je 0x140220f7b
00220F92  E8 F9 E4 0E 00                  call 0x14030f490
00220F97  45 33 C0                        xor r8d, r8d
00220F9A  84 C0                           test al, al
00220F9C  74 DD                           je 0x140220f7b
00220F9E  8B CB                           mov ecx, ebx
00220FA0  E8 BB E4 0E 00                  call 0x14030f460
00220FA5  45 33 C0                        xor r8d, r8d
00220FA8  EB D3                           jmp 0x140220f7d
00220FAA  83 F9 02                        cmp ecx, 2
00220FAD  75 0D                           jne 0x140220fbc
00220FAF  8A 47 70                        mov al, byte ptr [rdi + 0x70]
00220FB2  24 07                           and al, 7
00220FB4  3C 01                           cmp al, 1
00220FB6  0F 85 21 01 00 00               jne 0x1402210dd
00220FBC  65 4C 8B 2C 25 20 00 00 00      mov r13, qword ptr gs:[0x20]
00220FC5  41 8A D8                        mov bl, r8b
00220FC8  44 0F BE A7 C3 00 00 00         movsx r12d, byte ptr [rdi + 0xc3]
00220FD0  4D 8B F8                        mov r15, r8
00220FD3  41 0F B6 CE                     movzx ecx, r14b
00220FD7  45 8B F0                        mov r14d, r8d
00220FDA  44 88 45 60                     mov byte ptr [rbp + 0x60], r8b
00220FDE  83 E9 01                        sub ecx, 1
00220FE1  0F 85 C4 00 00 00               jne 0x1402210ab
00220FE7  45 8B CC                        mov r9d, r12d
00220FEA  4C 8B C7                        mov r8, rdi
00220FED  49 8B D2                        mov rdx, r10
00220FF0  48 8B CE                        mov rcx, rsi
00220FF3  E8 EC 05 FE FF                  call 0x1402015e4
00220FF8  44 8B 4D 58                     mov r9d, dword ptr [rbp + 0x58]
00220FFC  4C 8B C7                        mov r8, rdi
00220FFF  33 C9                           xor ecx, ecx
00221001  C6 44 24 20 00                  mov byte ptr [rsp + 0x20], 0
00221006  E8 05 68 03 00                  call 0x140257810
0022100B  4C 8B 65 50                     mov r12, qword ptr [rbp + 0x50]
0022100F  48 8B CF                        mov rcx, rdi
00221012  8B 55 58                        mov edx, dword ptr [rbp + 0x58]
00221015  4D 8B C4                        mov r8, r12
00221018  E8 0F 6F 17 00                  call 0x140397f2c
0022101D  48 8B D7                        mov rdx, rdi
00221020  33 C9                           xor ecx, ecx
00221022  E8 49 D4 0A 00                  call 0x1402ce470
00221027  80 7D 60 00                     cmp byte ptr [rbp + 0x60], 0
0022102B  74 40                           je 0x14022106d
0022102D  4D 8B BD E8 37 00 00            mov r15, qword ptr [r13 + 0x37e8]
00221034  48 8D 55 D8                     lea rdx, [rbp - 0x28]
00221038  49 8B CF                        mov rcx, r15
0022103B  45 33 C0                        xor r8d, r8d
0022103E  E8 6D B6 0E 00                  call 0x14030c6b0
00221043  48 8B D6                        mov rdx, rsi
00221046  49 8B CF                        mov rcx, r15
00221049  E8 12 20 13 00                  call 0x140353060
0022104E  49 8B D4                        mov rdx, r12
00221051  80 48 22 02                     or byte ptr [rax + 0x22], 2
00221055  E8 C6 75 03 00                  call 0x140258620
0022105A  4D 8B CC                        mov r9, r12
0022105D  45 33 C0                        xor r8d, r8d
00221060  49 8B D5                        mov rdx, r13
00221063  49 8B CF                        mov rcx, r15
00221066  E8 B5 BE 0E 00                  call 0x14030cf20
0022106B  8A D8                           mov bl, al
0022106D  4C 8B 4D D0                     mov r9, qword ptr [rbp - 0x30]
00221071  48 8D 45 E0                     lea rax, [rbp - 0x20]
00221075  4C 8D 45 D8                     lea r8, [rbp - 0x28]
00221079  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0022107E  48 8B D6                        mov rdx, rsi
00221081  E8 8A 68 FF FF                  call 0x140217910
00221086  84 DB                           test bl, bl
00221088  0F 85 62 02 00 00               jne 0x1402212f0
0022108E  45 85 F6                        test r14d, r14d
00221091  0F 8F 01 03 00 00               jg 0x140221398
00221097  B0 01                           mov al, 1
00221099  48 83 C4 68                     add rsp, 0x68
0022109D  41 5F                           pop r15
0022109F  41 5E                           pop r14
002210A1  41 5D                           pop r13
002210A3  41 5C                           pop r12
002210A5  5F                              pop rdi
002210A6  5E                              pop rsi
002210A7  5B                              pop rbx
002210A8  5D                              pop rbp
002210A9  C3                              ret
002210AA  CC                              int3
002210AB  83 E9 01                        sub ecx, 1
002210AE  0F 84 93 00 00 00               je 0x140221147
002210B4  83 F9 01                        cmp ecx, 1
002210B7  0F 84 7D 02 00 00               je 0x14022133a
002210BD  44 8B 4D 58                     mov r9d, dword ptr [rbp + 0x58]
002210C1  33 C9                           xor ecx, ecx
002210C3  44 88 44 24 20                  mov byte ptr [rsp + 0x20], r8b
002210C8  4C 8B C7                        mov r8, rdi
002210CB  E8 40 67 03 00                  call 0x140257810
002210D0  4C 8B 65 50                     mov r12, qword ptr [rbp + 0x50]
002210D4  E9 44 FF FF FF                  jmp 0x14022101d
002210D9  32 C0                           xor al, al
002210DB  EB BC                           jmp 0x140221099
002210DD  2C 03                           sub al, 3
002210DF  3C 03                           cmp al, 3
002210E1  0F 86 D5 FE FF FF               jbe 0x140220fbc
002210E7  41 B6 02                        mov r14b, 2
002210EA  8B 9F 18 02 00 00               mov ebx, dword ptr [rdi + 0x218]
002210F0  85 DB                           test ebx, ebx
002210F2  0F 88 CA FD FF FF               js 0x140220ec2
002210F8  48 8B 34 DA                     mov rsi, qword ptr [rdx + rbx*8]
002210FC  48 8B C6                        mov rax, rsi
002210FF  48 83 C8 01                     or rax, 1
00221103  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
00221107  48 8B 86 58 8E 00 00            mov rax, qword ptr [rsi + 0x8e58]
0022110E  0F B6 10                        movzx edx, byte ptr [rax]
00221111  48 8D 48 08                     lea rcx, [rax + 8]
00221115  E8 46 20 17 00                  call 0x140393160
0022111A  48 3B 7E 08                     cmp rdi, qword ptr [rsi + 8]
0022111E  0F 84 0A 02 00 00               je 0x14022132e
00221124  8A 87 84 01 00 00               mov al, byte ptr [rdi + 0x184]
0022112A  3C 02                           cmp al, 2
0022112C  0F 85 E7 00 00 00               jne 0x140221219
00221132  8B 87 18 02 00 00               mov eax, dword ptr [rdi + 0x218]
00221138  3B C3                           cmp eax, ebx
0022113A  0F 85 D9 00 00 00               jne 0x140221219
00221140  B9 4A 00 00 00                  mov ecx, 0x4a
00221145  CD 29                           int 0x29
00221147  48 8B 5E 10                     mov rbx, qword ptr [rsi + 0x10]
0022114B  4C 8B C7                        mov r8, rdi
0022114E  44 8B 4D 58                     mov r9d, dword ptr [rbp + 0x58]
00221152  48 85 DB                        test rbx, rbx
00221155  48 8B CE                        mov rcx, rsi
00221158  0F 94 C0                        sete al
0022115B  88 44 24 20                     mov byte ptr [rsp + 0x20], al
0022115F  E8 AC 66 03 00                  call 0x140257810
00221164  48 85 DB                        test rbx, rbx
00221167  75 1B                           jne 0x140221184
00221169  44 8B 45 58                     mov r8d, dword ptr [rbp + 0x58]
0022116D  45 3B C4                        cmp r8d, r12d
00221170  7D 1A                           jge 0x14022118c
00221172  8A 87 84 01 00 00               mov al, byte ptr [rdi + 0x184]
00221178  3C 02                           cmp al, 2
0022117A  0F 85 E6 01 00 00               jne 0x140221366
00221180  C6 45 60 01                     mov byte ptr [rbp + 0x60], 1
00221184  41 8A DE                        mov bl, r14b
00221187  E9 44 FF FF FF                  jmp 0x1402210d0
0022118C  7E F6                           jle 0x140221184
0022118E  8A 87 84 01 00 00               mov al, byte ptr [rdi + 0x184]
00221194  4C 8B 65 50                     mov r12, qword ptr [rbp + 0x50]
00221198  3C 02                           cmp al, 2
0022119A  0F 84 ED 01 00 00               je 0x14022138d
002211A0  41 8A DE                        mov bl, r14b
002211A3  E9 75 FE FF FF                  jmp 0x14022101d
002211A8  8B 9F 18 02 00 00               mov ebx, dword ptr [rdi + 0x218]
002211AE  85 DB                           test ebx, ebx
002211B0  79 3D                           jns 0x1402211ef
002211B2  8B C3                           mov eax, ebx
002211B4  0F BA F0 1F                     btr eax, 0x1f
002211B8  F7 05 76 59 DA 00 00 00 20 00   test dword ptr [rip + 0xda5976], 0x200000
002211C2  48 8B 04 C2                     mov rax, qword ptr [rdx + rax*8]
002211C6  4C 8B 90 48 8E 00 00            mov r10, qword ptr [rax + 0x8e48]
002211CD  4C 89 55 D0                     mov qword ptr [rbp - 0x30], r10
002211D1  75 57                           jne 0x14022122a
002211D3  44 89 45 C8                     mov dword ptr [rbp - 0x38], r8d
002211D7  49 8B FA                        mov rdi, r10
002211DA  F0 48 0F BA 2F 00               lock bts qword ptr [rdi], 0
002211E0  0F 82 04 58 4B 00               jb 0x1406d69ea
002211E6  48 8B 7D 48                     mov rdi, qword ptr [rbp + 0x48]
002211EA  E9 F8 00 00 00                  jmp 0x1402212e7
002211EF  48 8B 34 DA                     mov rsi, qword ptr [rdx + rbx*8]
002211F3  4C 8D 45 D8                     lea r8, [rbp - 0x28]
002211F7  48 8B CE                        mov rcx, rsi
002211FA  33 D2                           xor edx, edx
002211FC  E8 5F DB 0E 00                  call 0x14030ed60
00221201  8A 87 84 01 00 00               mov al, byte ptr [rdi + 0x184]
00221207  3C 01                           cmp al, 1
00221209  75 0E                           jne 0x140221219
0022120B  8B 87 18 02 00 00               mov eax, dword ptr [rdi + 0x218]
00221211  3B C3                           cmp eax, ebx
00221213  0F 84 15 01 00 00               je 0x14022132e
00221219  48 8D 4D D8                     lea rcx, [rbp - 0x28]
0022121D  E8 2E 8A 17 00                  call 0x140399c50
00221222  45 33 C0                        xor r8d, r8d
00221225  E9 91 FC FF FF                  jmp 0x140220ebb
0022122A  4C 89 55 E8                     mov qword ptr [rbp - 0x18], r10
0022122E  48 8D 55 E0                     lea rdx, [rbp - 0x20]
00221232  4C 89 45 E0                     mov qword ptr [rbp - 0x20], r8
00221236  90                              nop
00221237  49 87 12                        xchg qword ptr [r10], rdx
0022123A  48 85 D2                        test rdx, rdx
0022123D  0F 85 98 00 00 00               jne 0x1402212db
00221243  8A 87 84 01 00 00               mov al, byte ptr [rdi + 0x184]
00221249  3C 01                           cmp al, 1
0022124B  75 12                           jne 0x14022125f
0022124D  8B 87 18 02 00 00               mov eax, dword ptr [rdi + 0x218]
00221253  3B C3                           cmp eax, ebx
00221255  75 08                           jne 0x14022125f
00221257  49 8B F0                        mov rsi, r8
0022125A  E9 5D FD FF FF                  jmp 0x140220fbc
0022125F  F7 05 CF 58 DA 00 00 00 20 00   test dword ptr [rip + 0xda58cf], 0x200000
00221269  74 67                           je 0x1402212d2
0022126B  0F 0D 4D E0                     prefetchw byte ptr [rbp - 0x20]
0022126F  48 8B 45 E0                     mov rax, qword ptr [rbp - 0x20]
00221273  48 85 C0                        test rax, rax
00221276  75 2D                           jne 0x1402212a5
00221278  48 8B 4D E8                     mov rcx, qword ptr [rbp - 0x18]
0022127C  48 8D 45 E0                     lea rax, [rbp - 0x20]
00221280  F0 4C 0F B1 01                  lock cmpxchg qword ptr [rcx], r8
00221285  48 8D 4D E0                     lea rcx, [rbp - 0x20]
00221289  48 8D 15 B0 79 DA 00            lea rdx, [rip + 0xda79b0]
00221290  48 3B C1                        cmp rax, rcx
00221293  0F 84 29 FC FF FF               je 0x140220ec2
00221299  48 8D 4D E0                     lea rcx, [rbp - 0x20]
0022129D  E8 FE 67 FF FF                  call 0x140217aa0
002212A2  45 33 C0                        xor r8d, r8d
002212A5  48 8D 48 08                     lea rcx, [rax + 8]
002212A9  4C 89 45 E0                     mov qword ptr [rbp - 0x20], r8
002212AD  48 8B 55 E8                     mov rdx, qword ptr [rbp - 0x18]
002212B1  48 8B C2                        mov rax, rdx
002212B4  48 87 01                        xchg qword ptr [rcx], rax
002212B7  32 C2                           xor al, dl
002212B9  48 8D 15 80 79 DA 00            lea rdx, [rip + 0xda7980]
002212C0  A8 04                           test al, 4
002212C2  0F 84 FA FB FF FF               je 0x140220ec2
002212C8  E8 53 69 FF FF                  call 0x140217c20
002212CD  E9 50 FF FF FF                  jmp 0x140221222
002212D2  F0 4D 21 02                     lock and qword ptr [r10], r8
002212D6  E9 E0 FB FF FF                  jmp 0x140220ebb
002212DB  48 8D 4D E0                     lea rcx, [rbp - 0x20]
002212DF  E8 CC 6B 03 00                  call 0x140257eb0
002212E4  45 33 C0                        xor r8d, r8d
002212E7  4C 8B 55 D0                     mov r10, qword ptr [rbp - 0x30]
002212EB  E9 53 FF FF FF                  jmp 0x140221243
002212F0  33 DB                           xor ebx, ebx
002212F2  41 38 1F                        cmp byte ptr [r15], bl
002212F5  76 26                           jbe 0x14022131d
002212F7  8B CB                           mov ecx, ebx
002212F9  45 33 C9                        xor r9d, r9d
002212FC  48 83 C1 02                     add rcx, 2
00221300  45 33 C0                        xor r8d, r8d
00221303  49 8B D5                        mov rdx, r13
00221306  48 8D 0C 99                     lea rcx, [rcx + rbx*4]
0022130A  49 8D 0C CF                     lea rcx, [r15 + rcx*8]
0022130E  E8 1D 50 13 00                  call 0x140356330
00221313  41 0F B6 07                     movzx eax, byte ptr [r15]
00221317  FF C3                           inc ebx
00221319  3B D8                           cmp ebx, eax
0022131B  72 DA                           jb 0x1402212f7
0022131D  49 8D 8D D8 35 00 00            lea rcx, [r13 + 0x35d8]
00221324  E8 D7 0E 03 00                  call 0x140252200
00221329  E9 60 FD FF FF                  jmp 0x14022108e
0022132E  4C 8B 55 D0                     mov r10, qword ptr [rbp - 0x30]
00221332  45 33 C0                        xor r8d, r8d
00221335  E9 82 FC FF FF                  jmp 0x140220fbc
0022133A  8B 5D 58                        mov ebx, dword ptr [rbp + 0x58]
0022133D  4C 8B C7                        mov r8, rdi
00221340  44 8B CB                        mov r9d, ebx
00221343  C6 44 24 20 01                  mov byte ptr [rsp + 0x20], 1
00221348  48 8B CE                        mov rcx, rsi
0022134B  E8 C0 64 03 00                  call 0x140257810
00221350  45 33 F6                        xor r14d, r14d
00221353  41 3B DC                        cmp ebx, r12d
00221356  44 0F 4D F3                     cmovge r14d, ebx
0022135A  0F 9C 45 60                     setl byte ptr [rbp + 0x60]
0022135E  41 8A DF                        mov bl, r15b
00221361  E9 6A FD FF FF                  jmp 0x1402210d0
00221366  48 8B 86 48 8E 00 00            mov rax, qword ptr [rsi + 0x8e48]
0022136D  41 8D 48 01                     lea ecx, [r8 + 1]
00221371  8B 50 08                        mov edx, dword ptr [rax + 8]
00221374  0B 96 D8 83 00 00               or edx, dword ptr [rsi + 0x83d8]
0022137A  D3 EA                           shr edx, cl
0022137C  85 D2                           test edx, edx
0022137E  0F 84 00 FE FF FF               je 0x140221184
00221384  80 4F 70 10                     or byte ptr [rdi + 0x70], 0x10
00221388  E9 F7 FD FF FF                  jmp 0x140221184
0022138D  45 8B F0                        mov r14d, r8d
00221390  41 8A DF                        mov bl, r15b
00221393  E9 85 FC FF FF                  jmp 0x14022101d
00221398  45 8B C6                        mov r8d, r14d
0022139B  48 8B D6                        mov rdx, rsi
0022139E  49 8B CD                        mov rcx, r13
002213A1  E8 DA 24 22 00                  call 0x140443880
002213A6  E9 EC FC FF FF                  jmp 0x140221097
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiSetPriorityThread(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned int v_stack_m78;
    unsigned __int8 v_stack_m88;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned __int8 v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p18 = a3;
    v_stack_p10 = a2;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (104);
    if (((unsigned int)((__int8)(*(unsigned __int8 *)(a1 + 195)))) == a3) goto loc_002210D9;
    a3 = 0;
    v_stack_m60 = v_xmm0;
    v_stack_m68 = 0;
loc_00220EBB:
loc_00220EC2:
    v_stack_m70 = 0;
    v_stack_p20 = (unsigned __int8)(*(unsigned __int8 *)(a1 + 388));
    a1 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int8 *)(a1 + 388)))) - (1));
    if (condition_is_equal) goto loc_002211A8;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_002210EA;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_not_equal) goto loc_00220FAA;
    if (sign_flag) goto loc_00220EC2;
    result = (*(unsigned __int64 *)(v_rip + 14318974 + (unsigned int)(*(unsigned int *)(a1 + 536)) * 8)) | (1);
    v_stack_m68 = result;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 14318974 + (unsigned int)(*(unsigned int *)(a1 + 536)) * 8) + 36440))) == 0) goto loc_00220F47;
loc_00220F26:
loc_00220F2C:
    if (condition_is_below) goto loc_00220F71;
    v_r15 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 14318974 + (unsigned int)(*(unsigned int *)(a1 + 536)) * 8) + 36440) + 8) + (8);
    v_r13 = ((unsigned int)((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 14318974 + (unsigned int)(*(unsigned int *)(a1 + 536)) * 8) + 36440))))) - (1);
    if (condition_is_not_equal) goto loc_00220F26;
loc_00220F47:
    if (a1 == (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 14318974 + (unsigned int)(*(unsigned int *)(a1 + 536)) * 8) + 16))) goto loc_00220FBC;
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 388))) != 3) goto loc_00221219;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 536)))) != ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 536))))) goto loc_00221219;
loc_00220F71:
    v_rbx = (unsigned int)((0) + 1);
    if (((*(unsigned int *)(v_rip + 14304051)) & ((unsigned int)(v_rbx))) == 0) goto loc_00220F88;
loc_00220F7B:
loc_00220F7D:
    if (*(unsigned __int64 *)(v_stack_p20 + 48) == 0) goto loc_00220F2C;
    goto loc_00220F71;
loc_00220F88:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14310186)))) & (64)) == 0) goto loc_00220F7B;
    result = KiCheckVpBackingLongSpinWaitHypercall(30, v_rip + 14318974, a3, a4);
    a3 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_00220F7B;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rbx)), v_rip + 14318974, a3, a4);
    a3 = 0;
    goto loc_00220F7D;
loc_00220FAA:
    if (((unsigned int)((unsigned int)((unsigned int)(v_rbx)))) != 2) goto loc_00220FBC;
    result = (unsigned __int8)((*(unsigned __int8 *)(a1 + 112)) & (7));
    if (((unsigned __int8)(result)) != 1) goto loc_002210DD;
loc_00220FBC:
    v_stack_p20 = 0;
    a1 = (unsigned int)(((unsigned __int8)(v_stack_p20)) - (1));
    if (condition_is_not_equal) goto loc_002210AB;
    result = KiRemoveThreadFromAnyReadyQueue(*(unsigned __int64 *)(v_rip + 14318974 + (unsigned int)(*(unsigned int *)(a1 + 536)) * 8), v_stack_m70, a1, (unsigned int)((unsigned int)((__int8)(*(unsigned __int8 *)(a1 + 195)))));
    a1 = 0;
    v_stack_m88 = 0;
    result = KiUpdateThreadPriority(a1, v_stack_m70, a1, (unsigned int)(v_stack_p18));
    result = KiPrepareReadyThreadForRescheduling(0, (unsigned int)(v_stack_p18), v_stack_p10, (unsigned int)(v_stack_p18));
loc_0022101D:
    a1 = 0;
    result = KiUpdateSharedReadyQueueAffinityThread(a1, 0, v_stack_p10, (unsigned int)(v_stack_p18));
    v_rbx = 0;
    v_r15 = 0;
    if (v_stack_p20 != 0) {
        v_r15 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14312);
        a2 = v_stack_m68;
        a1 = v_r15;
        a3 = 0;
        result = KiStartRescheduleContext(a1, a2, a3, (unsigned int)(v_stack_p18));
        a2 = *(unsigned __int64 *)(v_rip + 14318974 + (unsigned int)(*(unsigned int *)(a1 + 536)) * 8);
        a1 = v_r15;
        result = KiFindRescheduleContextEntryForPrcb(a1, a2, a3, (unsigned int)(v_stack_p18));
        a2 = v_stack_p10;
        result = KiSearchForNewThreadsForRescheduleContext(a1, a2, a3, (unsigned int)(v_stack_p18));
        a4 = v_stack_p10;
        a3 = 0;
        a2 = *(unsigned __int64 *)(gs_base + (0 + 32));
        a1 = v_r15;
        result = KiCommitRescheduleContext(a1, a2, a3, a4);
        v_rbx = (unsigned __int8)(result);
    }
    v_stack_m88 = v_stack_m60;
    result = KiReleaseThreadStateLock(a1, *(unsigned __int64 *)(v_rip + 14318974 + (unsigned int)(*(unsigned int *)(a1 + 536)) * 8), v_stack_m68, v_stack_m70);
    if ((unsigned __int8)(v_rbx) != 0) goto loc_002212F0;
loc_0022108E:
    if (condition_is_greater) goto loc_00221398;
loc_00221097:
loc_00221099:
    v_rsp = (v_rsp) + (104);
    return 1;
loc_002210AB:
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00221147;
    if (((unsigned int)(a1)) == 1) goto loc_0022133A;
    a1 = 0;
    v_stack_p20 = (unsigned __int8)(v_stack_m68);
    result = KiUpdateThreadPriority(a1, *(unsigned __int64 *)(v_rip + 14318974 + (unsigned int)(*(unsigned int *)(a1 + 536)) * 8), 0, (unsigned int)(v_stack_p18));
loc_002210D0:
    goto loc_0022101D;
loc_002210D9:
    result = 0;
    goto loc_00221099;
loc_002210DD:
    result = (unsigned __int8)((result) - (3));
    if (((unsigned __int8)(result)) <= 3) goto loc_00220FBC;
loc_002210EA:
    if (sign_flag) goto loc_00220EC2;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 14318974 + (unsigned int)(*(unsigned int *)(a1 + 536)) * 8) + (unsigned int)(*(unsigned int *)(a1 + 536)) * 8)) | (1);
    v_stack_m68 = result;
    result = KiAcquireMultiplePrcbLocks(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 14318974 + (unsigned int)(*(unsigned int *)(a1 + 536)) * 8) + (unsigned int)(*(unsigned int *)(a1 + 536)) * 8) + 36440) + 8, *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 14318974 + (unsigned int)(*(unsigned int *)(a1 + 536)) * 8) + (unsigned int)(*(unsigned int *)(a1 + 536)) * 8) + 36440)), 0, (unsigned int)(v_stack_p18));
    if (0 == (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 14318974 + (unsigned int)(*(unsigned int *)(a1 + 536)) * 8) + (unsigned int)(*(unsigned int *)(a1 + 536)) * 8) + 8))) goto loc_0022132E;
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 388))) != 2) goto loc_00221219;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 536)))) != ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 536))))) goto loc_00221219;
loc_00221147:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 14318974 + (unsigned int)(*(unsigned int *)(a1 + 536)) * 8) + (unsigned int)(*(unsigned int *)(a1 + 536)) * 8) + 16) == 0) ? 1 : 0;
    v_stack_p20 = (unsigned __int8)(result);
    result = KiUpdateThreadPriority(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 14318974 + (unsigned int)(*(unsigned int *)(a1 + 536)) * 8) + (unsigned int)(*(unsigned int *)(a1 + 536)) * 8), *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 14318974 + (unsigned int)(*(unsigned int *)(a1 + 536)) * 8) + (unsigned int)(*(unsigned int *)(a1 + 536)) * 8) + 36440)), 0, (unsigned int)(v_stack_p18));
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 14318974 + (unsigned int)(*(unsigned int *)(a1 + 536)) * 8) + (unsigned int)(*(unsigned int *)(a1 + 536)) * 8) + 16) != 0) goto loc_00221184;
    if (((unsigned int)((unsigned int)(v_stack_p18))) >= ((unsigned int)(v_stack_p10))) goto loc_0022118C;
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 388))) != 2) goto loc_00221366;
    v_stack_p20 = 1;
loc_00221184:
    goto loc_002210D0;
loc_0022118C:
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 388))) <= 2) goto loc_00221184;
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 388))) == 2) goto loc_0022138D;
    goto loc_0022101D;
loc_002211A8:
    if (!sign_flag) goto loc_002211EF;
    v_stack_m70 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 14318974 + (unsigned int)(*(unsigned int *)(a1 + 536)) * 8) + (unsigned int)(*(unsigned int *)(a1 + 536)) * 8) + 36440)) + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 536)))) * 8) + 36424);
    if (((*(unsigned int *)(v_rip + 14309750)) & (0x200000ULL)) != 0) goto loc_0022122A;
    v_stack_m78 = (unsigned int)((unsigned int)(v_stack_p18));
    goto loc_002212E7;
loc_002211EF:
    a2 = 0;
    result = KiAcquirePrcbLocksForIsolationUnit(*(unsigned __int64 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 14318974 + (unsigned int)(*(unsigned int *)(a1 + 536)) * 8) + (unsigned int)(*(unsigned int *)(a1 + 536)) * 8) + 36440)) + (unsigned int)(*(unsigned int *)(a1 + 536)) * 8), a2, v_stack_m68, (unsigned int)(v_stack_p18));
    if (((unsigned __int8)(*(unsigned __int8 *)(v_stack_p8 + 388))) != 1) goto loc_00221219;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 536)))) == ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 536))))) goto loc_0022132E;
loc_00221219:
    result = KiReleasePrcbLocksForIsolationUnit(v_stack_m68, a2, v_stack_m68, (unsigned int)(v_stack_p18));
loc_00221222:
    a3 = 0;
    goto loc_00220EBB;
loc_0022122A:
    v_stack_m58 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 14318974 + (unsigned int)(*(unsigned int *)(a1 + 536)) * 8) + (unsigned int)(*(unsigned int *)(a1 + 536)) * 8) + 36440)) + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 536)))) * 8) + 36424);
    v_stack_m60 = 0;
    if (v_stack_m60 != 0) goto loc_002212DB;
loc_00221243:
    if (((unsigned __int8)(*(unsigned __int8 *)(v_stack_p8 + 388))) != 1) goto loc_0022125F;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 536)))) != ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 536))))) goto loc_0022125F;
    goto loc_00220FBC;
loc_0022125F:
    if (((*(unsigned int *)(v_rip + 14309583)) & (0x200000ULL)) == 0) goto loc_002212D2;
    if (v_stack_m60 != 0) goto loc_002212A5;
    if (v_stack_m60 == v_stack_m60) goto loc_00220EC2;
    result = KxWaitForLockChainValid(v_stack_m60, v_rip + 14318000, a3, (unsigned int)(v_stack_p18));
    a3 = 0;
loc_002212A5:
    v_stack_m60 = 0;
    result = (unsigned __int8)((v_stack_m58) ^ ((unsigned __int8)(v_stack_m58)));
    if ((((unsigned __int8)(result)) & (4)) == 0) goto loc_00220EC2;
    result = KeWakeAddressAll(result + 8, v_rip + 14317952, a3, (unsigned int)(v_stack_p18));
    goto loc_00221222;
loc_002212D2:
    goto loc_00220EBB;
loc_002212DB:
    result = KxWaitForLockOwnerShip(v_stack_m60, v_rip + 14317952, a3, (unsigned int)(v_stack_p18));
    a3 = 0;
loc_002212E7:
    goto loc_00221243;
loc_002212F0:
    v_rbx = 0;
    if ((*(unsigned __int8 *)(v_r15)) <= 0) goto loc_0022131D;
loc_002212F7:
    a4 = 0;
    a1 = (0) + (2);
    a3 = 0;
    result = KiCompleteRescheduleContextEntry(v_r15 + a1 + v_rbx * 4 * 8, *(unsigned __int64 *)(gs_base + (0 + 32)), a3, a4);
    v_rbx = (unsigned int)((v_rbx) + 1);
    if (((unsigned int)(v_rbx)) < ((unsigned int)(*(unsigned __int8 *)(v_r15)))) goto loc_002212F7;
loc_0022131D:
    result = KiFlushSoftwareInterruptBatch(*(unsigned __int64 *)(gs_base + (0 + 32)) + 13784, *(unsigned __int64 *)(gs_base + (0 + 32)), a3, a4);
    goto loc_0022108E;
loc_0022132E:
    a3 = 0;
    goto loc_00220FBC;
loc_0022133A:
    v_stack_p20 = 1;
    result = KiUpdateThreadPriority(0, *(unsigned __int64 *)(gs_base + (0 + 32)), v_stack_p8, (unsigned int)((unsigned int)((unsigned int)(v_stack_p18))));
    v_r14 = 0;
    if (((unsigned int)((unsigned int)(v_stack_p18))) >= ((unsigned int)(v_stack_p10))) { v_r14 = (unsigned int)((unsigned int)(v_stack_p18)); }
    goto loc_002210D0;
loc_00221366:
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(0 + 36424) + 8))) | (*(unsigned int *)(0 + 33752)));
    a2 = (unsigned int)((a2) >> ((unsigned __int8)(v_stack_p8 + 1)));
    if ((unsigned int)(a2) == 0) goto loc_00221184;
    goto loc_00221184;
loc_0022138D:
    goto loc_0022101D;
loc_00221398:
    result = KiHvEnlightenedGuestPriorityKick(*(unsigned __int64 *)(gs_base + (0 + 32)), 0, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_p8)))), (unsigned int)((unsigned int)((unsigned int)(v_stack_p18))));
    goto loc_00221097;
}
```

## 5. (Beta) C Style

```c
int64_t KiSetPriorityThread(void *Arg1, int64_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint32_t v_stack_m78;
    uint8_t v_stack_m88;
    uint64_t v_stack_p10;
    uint32_t v_stack_p18;
    uint8_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p18 = Arg3;
    v_stack_p10 = Arg2;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (104);
    if (((uint32_t)((int8_t)(*(uint8_t *)(arg1 + 0xC3)))) == Arg3) goto loc_002210D9;
    Arg3 = 0;
    v_stack_m60 = v_xmm0;
    v_stack_m68 = 0;
loc_00220EBB:
loc_00220EC2:
    v_stack_m70 = 0;
    v_stack_p20 = (uint8_t)(*(uint8_t *)(arg1 + 0x184));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(*(uint8_t *)(arg1 + 0x184)))) - (1));
    if (condition_is_equal) goto loc_002211A8;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_002210EA;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_not_equal) goto loc_00220FAA;
    if (sign_flag) goto loc_00220EC2;
    result = (*(uint64_t *)(v_rip + 0xDA7D7E + (uint32_t)(*(uint32_t *)(arg1 + 0x218)) * 8)) | (1);
    v_stack_m68 = result;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xDA7D7E + (uint32_t)(*(uint32_t *)(arg1 + 0x218)) * 8) + 0x8E58))) == 0) goto loc_00220F47;
loc_00220F26:
loc_00220F2C:
    if (condition_is_below) goto loc_00220F71;
    local_r15 = (*(uint64_t *)(*(uint64_t *)(v_rip + 0xDA7D7E + (uint32_t)(*(uint32_t *)(arg1 + 0x218)) * 8) + 0x8E58) + 8) + (8);
    local_r13 = ((uint32_t)((uint32_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xDA7D7E + (uint32_t)(*(uint32_t *)(arg1 + 0x218)) * 8) + 0x8E58))))) - (1);
    if (condition_is_not_equal) goto loc_00220F26;
loc_00220F47:
    if (Arg1 == (*(uint64_t *)(*(uint64_t *)(v_rip + 0xDA7D7E + (uint32_t)(*(uint32_t *)(arg1 + 0x218)) * 8) + 0x10))) goto loc_00220FBC;
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x184))) != 3) goto loc_00221219;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x218)))) != ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x218))))) goto loc_00221219;
loc_00220F71:
    local_rbx = (uint32_t)((0) + 1);
    if (((*(uint32_t *)(v_rip + 0xDA4333)) & ((uint32_t)(local_rbx))) == 0) goto loc_00220F88;
loc_00220F7B:
loc_00220F7D:
    if (*(uint64_t *)(v_stack_p20 + 0x30) == 0) goto loc_00220F2C;
    goto loc_00220F71;
loc_00220F88:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xDA5B2A)))) & (64)) == 0) goto loc_00220F7B;
    result = KiCheckVpBackingLongSpinWaitHypercall(30, v_rip + 14318974, Arg3, a4);
    Arg3 = 0;
    if ((uint8_t)(result) == 0) goto loc_00220F7B;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rbx)), v_rip + 14318974, Arg3, a4);
    Arg3 = 0;
    goto loc_00220F7D;
loc_00220FAA:
    if (((uint32_t)((uint32_t)((uint32_t)(local_rbx)))) != 2) goto loc_00220FBC;
    result = (uint8_t)((*(uint8_t *)(arg1 + 0x70)) & (7));
    if (((uint8_t)(result)) != 1) goto loc_002210DD;
loc_00220FBC:
    v_stack_p20 = 0;
    Arg1 = (uint32_t)(((uint8_t)(v_stack_p20)) - (1));
    if (condition_is_not_equal) goto loc_002210AB;
    result = KiRemoveThreadFromAnyReadyQueue(*(uint64_t *)(v_rip + 0xDA7D7E + (uint32_t)(*(uint32_t *)(arg1 + 0x218)) * 8), v_stack_m70, Arg1, (uint32_t)((uint32_t)((int8_t)(*(uint8_t *)(arg1 + 0xC3)))));
    Arg1 = 0;
    v_stack_m88 = 0;
    result = KiUpdateThreadPriority(Arg1, v_stack_m70, Arg1, (uint32_t)(v_stack_p18));
    result = KiPrepareReadyThreadForRescheduling(0, (uint32_t)(v_stack_p18), v_stack_p10, (uint32_t)(v_stack_p18));
loc_0022101D:
    Arg1 = 0;
    result = KiUpdateSharedReadyQueueAffinityThread(Arg1, 0, v_stack_p10, (uint32_t)(v_stack_p18));
    local_rbx = 0;
    local_r15 = 0;
    if (v_stack_p20 != 0) {
        local_r15 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x37E8);
        Arg2 = v_stack_m68;
        Arg1 = local_r15;
        Arg3 = 0;
        result = KiStartRescheduleContext(Arg1, Arg2, Arg3, (uint32_t)(v_stack_p18));
        Arg2 = *(uint64_t *)(v_rip + 0xDA7D7E + (uint32_t)(*(uint32_t *)(arg1 + 0x218)) * 8);
        Arg1 = local_r15;
        result = KiFindRescheduleContextEntryForPrcb(Arg1, Arg2, Arg3, (uint32_t)(v_stack_p18));
        Arg2 = v_stack_p10;
        result = KiSearchForNewThreadsForRescheduleContext(Arg1, Arg2, Arg3, (uint32_t)(v_stack_p18));
        a4 = v_stack_p10;
        Arg3 = 0;
        Arg2 = *(uint64_t *)(gs_base + (0 + 0x20));
        Arg1 = local_r15;
        result = KiCommitRescheduleContext(Arg1, Arg2, Arg3, a4);
        local_rbx = (uint8_t)(result);
    }
    v_stack_m88 = v_stack_m60;
    result = KiReleaseThreadStateLock(Arg1, *(uint64_t *)(v_rip + 0xDA7D7E + (uint32_t)(*(uint32_t *)(arg1 + 0x218)) * 8), v_stack_m68, v_stack_m70);
    if ((uint8_t)(local_rbx) != 0) goto loc_002212F0;
loc_0022108E:
    if (condition_is_greater) goto loc_00221398;
loc_00221097:
loc_00221099:
    local_rsp = (local_rsp) + (104);
    return 1;
loc_002210AB:
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00221147;
    if (((uint32_t)(Arg1)) == 1) goto loc_0022133A;
    Arg1 = 0;
    v_stack_p20 = (uint8_t)(v_stack_m68);
    result = KiUpdateThreadPriority(Arg1, *(uint64_t *)(v_rip + 0xDA7D7E + (uint32_t)(*(uint32_t *)(arg1 + 0x218)) * 8), 0, (uint32_t)(v_stack_p18));
loc_002210D0:
    goto loc_0022101D;
loc_002210D9:
    result = 0;
    goto loc_00221099;
loc_002210DD:
    result = (uint8_t)((result) - (3));
    if (((uint8_t)(result)) <= 3) goto loc_00220FBC;
loc_002210EA:
    if (sign_flag) goto loc_00220EC2;
    result = (*(uint64_t *)(*(uint64_t *)(v_rip + 0xDA7D7E + (uint32_t)(*(uint32_t *)(arg1 + 0x218)) * 8) + (uint32_t)(*(uint32_t *)(arg1 + 0x218)) * 8)) | (1);
    v_stack_m68 = result;
    result = KiAcquireMultiplePrcbLocks(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xDA7D7E + (uint32_t)(*(uint32_t *)(arg1 + 0x218)) * 8) + (uint32_t)(*(uint32_t *)(arg1 + 0x218)) * 8) + 0x8E58) + 8, *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xDA7D7E + (uint32_t)(*(uint32_t *)(arg1 + 0x218)) * 8) + (uint32_t)(*(uint32_t *)(arg1 + 0x218)) * 8) + 0x8E58)), 0, (uint32_t)(v_stack_p18));
    if (0 == (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xDA7D7E + (uint32_t)(*(uint32_t *)(arg1 + 0x218)) * 8) + (uint32_t)(*(uint32_t *)(arg1 + 0x218)) * 8) + 0x8))) goto loc_0022132E;
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x184))) != 2) goto loc_00221219;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x218)))) != ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x218))))) goto loc_00221219;
loc_00221147:
    result = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xDA7D7E + (uint32_t)(*(uint32_t *)(arg1 + 0x218)) * 8) + (uint32_t)(*(uint32_t *)(arg1 + 0x218)) * 8) + 0x10) == 0) ? 1 : 0;
    v_stack_p20 = (uint8_t)(result);
    result = KiUpdateThreadPriority(*(uint64_t *)(*(uint64_t *)(v_rip + 0xDA7D7E + (uint32_t)(*(uint32_t *)(arg1 + 0x218)) * 8) + (uint32_t)(*(uint32_t *)(arg1 + 0x218)) * 8), *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xDA7D7E + (uint32_t)(*(uint32_t *)(arg1 + 0x218)) * 8) + (uint32_t)(*(uint32_t *)(arg1 + 0x218)) * 8) + 0x8E58)), 0, (uint32_t)(v_stack_p18));
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xDA7D7E + (uint32_t)(*(uint32_t *)(arg1 + 0x218)) * 8) + (uint32_t)(*(uint32_t *)(arg1 + 0x218)) * 8) + 0x10) != 0) goto loc_00221184;
    if (((uint32_t)((uint32_t)(v_stack_p18))) >= ((uint32_t)(v_stack_p10))) goto loc_0022118C;
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x184))) != 2) goto loc_00221366;
    v_stack_p20 = 1;
loc_00221184:
    goto loc_002210D0;
loc_0022118C:
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x184))) <= 2) goto loc_00221184;
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x184))) == 2) goto loc_0022138D;
    goto loc_0022101D;
loc_002211A8:
    if (!sign_flag) goto loc_002211EF;
    v_stack_m70 = *(uint64_t *)(*(uint64_t *)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xDA7D7E + (uint32_t)(*(uint32_t *)(arg1 + 0x218)) * 8) + (uint32_t)(*(uint32_t *)(arg1 + 0x218)) * 8) + 0x8E58)) + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x218)))) * 8) + 0x8E48);
    if (((*(uint32_t *)(v_rip + 0xDA5976)) & (0x200000ULL)) != 0) goto loc_0022122A;
    v_stack_m78 = (uint32_t)((uint32_t)(v_stack_p18));
    goto loc_002212E7;
loc_002211EF:
    Arg2 = 0;
    result = KiAcquirePrcbLocksForIsolationUnit(*(uint64_t *)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xDA7D7E + (uint32_t)(*(uint32_t *)(arg1 + 0x218)) * 8) + (uint32_t)(*(uint32_t *)(arg1 + 0x218)) * 8) + 0x8E58)) + (uint32_t)(*(uint32_t *)(arg1 + 0x218)) * 8), Arg2, v_stack_m68, (uint32_t)(v_stack_p18));
    if (((uint8_t)(*(uint8_t *)(v_stack_p8 + 0x184))) != 1) goto loc_00221219;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x218)))) == ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x218))))) goto loc_0022132E;
loc_00221219:
    result = KiReleasePrcbLocksForIsolationUnit(v_stack_m68, Arg2, v_stack_m68, (uint32_t)(v_stack_p18));
loc_00221222:
    Arg3 = 0;
    goto loc_00220EBB;
loc_0022122A:
    v_stack_m58 = *(uint64_t *)(*(uint64_t *)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xDA7D7E + (uint32_t)(*(uint32_t *)(arg1 + 0x218)) * 8) + (uint32_t)(*(uint32_t *)(arg1 + 0x218)) * 8) + 0x8E58)) + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x218)))) * 8) + 0x8E48);
    v_stack_m60 = 0;
    if (v_stack_m60 != 0) goto loc_002212DB;
loc_00221243:
    if (((uint8_t)(*(uint8_t *)(v_stack_p8 + 0x184))) != 1) goto loc_0022125F;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x218)))) != ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x218))))) goto loc_0022125F;
    goto loc_00220FBC;
loc_0022125F:
    if (((*(uint32_t *)(v_rip + 0xDA58CF)) & (0x200000ULL)) == 0) goto loc_002212D2;
    if (v_stack_m60 != 0) goto loc_002212A5;
    if (v_stack_m60 == v_stack_m60) goto loc_00220EC2;
    result = KxWaitForLockChainValid(v_stack_m60, v_rip + 14318000, Arg3, (uint32_t)(v_stack_p18));
    Arg3 = 0;
loc_002212A5:
    v_stack_m60 = 0;
    result = (uint8_t)((v_stack_m58) ^ ((uint8_t)(v_stack_m58)));
    if ((((uint8_t)(result)) & (4)) == 0) goto loc_00220EC2;
    result = KeWakeAddressAll(result + 8, v_rip + 14317952, Arg3, (uint32_t)(v_stack_p18));
    goto loc_00221222;
loc_002212D2:
    goto loc_00220EBB;
loc_002212DB:
    result = KxWaitForLockOwnerShip(v_stack_m60, v_rip + 14317952, Arg3, (uint32_t)(v_stack_p18));
    Arg3 = 0;
loc_002212E7:
    goto loc_00221243;
loc_002212F0:
    local_rbx = 0;
    if ((*(uint8_t *)(local_r15)) <= 0) goto loc_0022131D;
loc_002212F7:
    a4 = 0;
    Arg1 = (0) + (2);
    Arg3 = 0;
    result = KiCompleteRescheduleContextEntry(local_r15 + Arg1 + local_rbx * 4 * 8, *(uint64_t *)(gs_base + (0 + 0x20)), Arg3, a4);
    local_rbx = (uint32_t)((local_rbx) + 1);
    if (((uint32_t)(local_rbx)) < ((uint32_t)(*(uint8_t *)(local_r15)))) goto loc_002212F7;
loc_0022131D:
    result = KiFlushSoftwareInterruptBatch(*(uint64_t *)(gs_base + (0 + 0x20)) + 13784, *(uint64_t *)(gs_base + (0 + 0x20)), Arg3, a4);
    goto loc_0022108E;
loc_0022132E:
    Arg3 = 0;
    goto loc_00220FBC;
loc_0022133A:
    v_stack_p20 = 1;
    result = KiUpdateThreadPriority(0, *(uint64_t *)(gs_base + (0 + 0x20)), v_stack_p8, (uint32_t)((uint32_t)((uint32_t)(v_stack_p18))));
    local_r14 = 0;
    if (((uint32_t)((uint32_t)(v_stack_p18))) >= ((uint32_t)(v_stack_p10))) { local_r14 = (uint32_t)((uint32_t)(v_stack_p18)); }
    goto loc_002210D0;
loc_00221366:
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(0 + 0x8E48) + 0x8))) | (*(uint32_t *)(0 + 0x83D8)));
    Arg2 = (uint32_t)((Arg2) >> ((uint8_t)(v_stack_p8 + 1)));
    if ((uint32_t)(Arg2) == 0) goto loc_00221184;
    goto loc_00221184;
loc_0022138D:
    goto loc_0022101D;
loc_00221398:
    result = KiHvEnlightenedGuestPriorityKick(*(uint64_t *)(gs_base + (0 + 0x20)), 0, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_p8)))), (uint32_t)((uint32_t)((uint32_t)(v_stack_p18))));
    goto loc_00221097;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xC3` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00220E78&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
