# KeYieldExecution

- RVA: `0x00209FA0`–`0x0020A4AB` (길이 `1,291` bytes)
- VA: `0x0000000140209FA0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D6E4`
- 디코드: `328`개 명령, `1,291/1,291` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **33**; 고유 호출 대상: **28**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x0020A057` → [KiAbProcessPreContextSwitch](../21/KiAbProcessPreContextSwitch_function_0021D420.md) (function, `0x0021D420`)
- `0x0020A08F` → [KiAcquirePrcbLocksForIsolationUnit](../30/KiAcquirePrcbLocksForIsolationUnit_function_0030ED60.md) (function, `0x0030ED60`)
- `0x0020A0E7` → [KzReleaseAdditionalPrcbLocks](KzReleaseAdditionalPrcbLocks_function_00202B70.md) (function, `0x00202B70`)
- `0x0020A111` → [KiUpdateTotalCyclesCurrentThread](../37/KiUpdateTotalCyclesCurrentThread_function_0037DE40.md) (function, `0x0037DE40`)
- `0x0020A136` → [KiQueryQuantumReset](../21/KiQueryQuantumReset_function_0021F6B4.md) (function, `0x0021F6B4`)
- `0x0020A15E` → [KiComputeNewPriority](../3C/KiComputeNewPriority_function_003C2D8C.md) (function, `0x003C2D8C`)
- `0x0020A16E` → [KiUpdateVPBackingThreadPriority](../30/KiUpdateVPBackingThreadPriority_function_00306040.md) (function, `0x00306040`)
- `0x0020A189` → [KiCaptureTotalCyclesCurrentThread](../37/KiCaptureTotalCyclesCurrentThread_function_0037CB90.md) (function, `0x0037CB90`)
- `0x0020A194` → [KiUpdatePriorityMatrixForRunningTransition](../37/KiUpdatePriorityMatrixForRunningTransition_function_0037B3A0.md) (function, `0x0037B3A0`)
- `0x0020A1B1` → [KiQueueReadyThread](../21/KiQueueReadyThread_function_0021C7B0.md) (function, `0x0021C7B0`)
- `0x0020A1BF` → [KiSwapContext](../6B/KiSwapContext_function_006B9740.md) (function, `0x006B9740`)
- `0x0020A1C7` → [KiAbProcessPostContextSwitch](../24/KiAbProcessPostContextSwitch_function_00248790.md) (function, `0x00248790`)
- `0x0020A1DF` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0020A222` → [KiUpdateThreadPriority](../25/KiUpdateThreadPriority_function_00257810.md) (function, `0x00257810`)
- `0x0020A231` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x0020A252` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0020A261` → [KiStartRescheduleContext](../30/KiStartRescheduleContext_function_0030C6B0.md) (function, `0x0030C6B0`)
- `0x0020A278` → [KiFindRescheduleContextEntryForPrcb](../35/KiFindRescheduleContextEntryForPrcb_function_00353060.md) (function, `0x00353060`)
- `0x0020A2AB` → [KiSearchForNewThreadsForRescheduleContext](../25/KiSearchForNewThreadsForRescheduleContext_function_00258620.md) (function, `0x00258620`)
- `0x0020A2BD` → [KiCommitRescheduleContext](../30/KiCommitRescheduleContext_function_0030CF20.md) (function, `0x0030CF20`)
- `0x0020A2DA` → [KiReleasePrcbLocksForIsolationUnit](../39/KiReleasePrcbLocksForIsolationUnit_function_00399C50.md) (function, `0x00399C50`)
- `0x0020A324` → [KiReleasePrcbLocksForIsolationUnit](../39/KiReleasePrcbLocksForIsolationUnit_function_00399C50.md) (function, `0x00399C50`)
- `0x0020A330` → [KiAbProcessPostContextSwitch](../24/KiAbProcessPostContextSwitch_function_00248790.md) (function, `0x00248790`)
- `0x0020A358` → [KiVpBackingThreadYieldExecution](../4D/KiVpBackingThreadYieldExecution_function_004DF1A4.md) (function, `0x004DF1A4`)
- `0x0020A37D` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0020A38C` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0020A3B4` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x0020A3C7` → [KiAcquirePrcbLocksForIsolationUnit](../30/KiAcquirePrcbLocksForIsolationUnit_function_0030ED60.md) (function, `0x0030ED60`)
- `0x0020A3F4` → [KiCompleteRescheduleContextEntry](../35/KiCompleteRescheduleContextEntry_function_00356330.md) (function, `0x00356330`)
- `0x0020A40C` → [KiFlushSoftwareInterruptBatch](../25/KiFlushSoftwareInterruptBatch_function_00252200.md) (function, `0x00252200`)
- `0x0020A424` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0020A433` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0020A4A1` → [KiReadyDeferredReadyList](../30/KiReadyDeferredReadyList_function_0030DD80.md) (function, `0x0030DD80`)

### Direct callers
- [KeDelayExecutionThread](KeDelayExecutionThread_function_00209550.md) at `0x0020958C`
- [sub_0020959D](Unknown_function_0020959D.md) at `0x002097FB`
- [NtYieldExecution](NtYieldExecution_function_00209F80.md) at `0x00209F86`

### Static image references
- `0x0020A026` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x0020A06A` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x0020A13B` → RVA `0x00FC5098` (`ALMOSTRO`; read)
- `0x0020A36F` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00209FA0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00209FA5  55                              push rbp
00209FA6  56                              push rsi
00209FA7  57                              push rdi
00209FA8  41 54                           push r12
00209FAA  41 55                           push r13
00209FAC  41 56                           push r14
00209FAE  41 57                           push r15
00209FB0  48 8B EC                        mov rbp, rsp
00209FB3  48 83 EC 30                     sub rsp, 0x30
00209FB7  45 33 ED                        xor r13d, r13d
00209FBA  44 8B F9                        mov r15d, ecx
00209FBD  4C 89 6D 50                     mov qword ptr [rbp + 0x50], r13
00209FC1  4C 89 6D 48                     mov qword ptr [rbp + 0x48], r13
00209FC5  F7 C1 FC FF FF FF               test ecx, 0xfffffffc
00209FCB  74 1D                           je 0x140209fea
00209FCD  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00209FD2  8B C3                           mov eax, ebx
00209FD4  48 8B 5C 24 70                  mov rbx, qword ptr [rsp + 0x70]
00209FD9  48 83 C4 30                     add rsp, 0x30
00209FDD  41 5F                           pop r15
00209FDF  41 5E                           pop r14
00209FE1  41 5D                           pop r13
00209FE3  41 5C                           pop r12
00209FE5  5F                              pop rdi
00209FE6  5E                              pop rsi
00209FE7  5D                              pop rbp
00209FE8  C3                              ret
00209FE9  CC                              int3
00209FEA  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
00209FF3  44 39 A9 D8 83 00 00            cmp dword ptr [rcx + 0x83d8], r13d
00209FFA  75 14                           jne 0x14020a010
00209FFC  48 8B 81 48 8E 00 00            mov rax, qword ptr [rcx + 0x8e48]
0020A003  44 39 68 08                     cmp dword ptr [rax + 8], r13d
0020A007  75 07                           jne 0x14020a010
0020A009  BB 24 00 00 40                  mov ebx, 0x40000024
0020A00E  EB C2                           jmp 0x140209fd2
0020A010  65 48 8B 3C 25 88 01 00 00      mov rdi, qword ptr gs:[0x188]
0020A019  45 0F 20 C4                     mov r12, cr8
0020A01D  B9 02 00 00 00                  mov ecx, 2
0020A022  44 0F 22 C1                     mov cr8, rcx
0020A026  44 39 2D F3 CC DB 00            cmp dword ptr [rip + 0xdbccf3], r13d
0020A02D  0F 85 F9 01 00 00               jne 0x14020a22c
0020A033  65 48 8B 34 25 20 00 00 00      mov rsi, qword ptr gs:[0x20]
0020A03C  44 39 AE D8 83 00 00            cmp dword ptr [rsi + 0x83d8], r13d
0020A043  0F 84 B6 01 00 00               je 0x14020a1ff
0020A049  44 84 F9                        test cl, r15b
0020A04C  0F 85 F6 02 00 00               jne 0x14020a348
0020A052  33 D2                           xor edx, edx
0020A054  48 8B CF                        mov rcx, rdi
0020A057  E8 C4 33 01 00                  call 0x14021d420
0020A05C  41 8B DD                        mov ebx, r13d
0020A05F  F0 48 0F BA 6F 40 00            lock bts qword ptr [rdi + 0x40], 0
0020A066  73 1B                           jae 0x14020a083
0020A068  FF C3                           inc ebx
0020A06A  85 1D 3C B2 DB 00               test dword ptr [rip + 0xdbb23c], ebx
0020A070  0F 84 F9 02 00 00               je 0x14020a36f
0020A076  F3 90                           pause
0020A078  48 8B 47 40                     mov rax, qword ptr [rdi + 0x40]
0020A07C  48 85 C0                        test rax, rax
0020A07F  74 DE                           je 0x14020a05f
0020A081  EB E5                           jmp 0x14020a068
0020A083  4C 8D 45 48                     lea r8, [rbp + 0x48]
0020A087  BA 01 00 00 00                  mov edx, 1
0020A08C  48 8B CE                        mov rcx, rsi
0020A08F  E8 CC 4C 10 00                  call 0x14030ed60
0020A094  4C 39 6E 10                     cmp qword ptr [rsi + 0x10], r13
0020A098  0F 84 A2 01 00 00               je 0x14020a240
0020A09E  48 8B 45 48                     mov rax, qword ptr [rbp + 0x48]
0020A0A2  4D 8B D5                        mov r10, r13
0020A0A5  48 8B D8                        mov rbx, rax
0020A0A8  41 8B D5                        mov edx, r13d
0020A0AB  48 83 E3 FE                     and rbx, 0xfffffffffffffffe
0020A0AF  48 89 5D 58                     mov qword ptr [rbp + 0x58], rbx
0020A0B3  83 E0 01                        and eax, 1
0020A0B6  74 38                           je 0x14020a0f0
0020A0B8  85 C0                           test eax, eax
0020A0BA  0F 84 31 01 00 00               je 0x14020a1f1
0020A0C0  83 F8 01                        cmp eax, 1
0020A0C3  75 15                           jne 0x14020a0da
0020A0C5  48 8B 83 58 8E 00 00            mov rax, qword ptr [rbx + 0x8e58]
0020A0CC  4C 8B 93 58 8E 00 00            mov r10, qword ptr [rbx + 0x8e58]
0020A0D3  49 83 C2 08                     add r10, 8
0020A0D7  0F B6 10                        movzx edx, byte ptr [rax]
0020A0DA  41 B9 01 00 00 00               mov r9d, 1
0020A0E0  4C 8D 45 58                     lea r8, [rbp + 0x58]
0020A0E4  49 8B CA                        mov rcx, r10
0020A0E7  E8 84 8A FF FF                  call 0x140202b70
0020A0EC  48 89 5D 48                     mov qword ptr [rbp + 0x48], rbx
0020A0F0  48 8B 5E 10                     mov rbx, qword ptr [rsi + 0x10]
0020A0F4  48 85 DB                        test rbx, rbx
0020A0F7  0F 84 23 02 00 00               je 0x14020a320
0020A0FD  44 38 6E 20                     cmp byte ptr [rsi + 0x20], r13b
0020A101  0F 85 38 02 00 00               jne 0x14020a33f
0020A107  FA                              cli
0020A108  45 33 C0                        xor r8d, r8d
0020A10B  48 8B D7                        mov rdx, rdi
0020A10E  48 8B CE                        mov rcx, rsi
0020A111  E8 2A 3D 17 00                  call 0x14037de40
0020A116  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
0020A11F  4C 8B F0                        mov r14, rax
0020A122  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
0020A129  4D 85 C0                        test r8, r8
0020A12C  0F 85 64 02 00 00               jne 0x14020a396
0020A132  FB                              sti
0020A133  48 8B CF                        mov rcx, rdi
0020A136  E8 79 55 01 00                  call 0x14021f6b4
0020A13B  0F AF 05 56 AF DB 00            imul eax, dword ptr [rip + 0xdbaf56]
0020A142  8B C8                           mov ecx, eax
0020A144  8B 47 78                        mov eax, dword ptr [rdi + 0x78]
0020A147  49 03 CE                        add rcx, r14
0020A14A  A8 20                           test al, 0x20
0020A14C  74 06                           je 0x14020a154
0020A14E  F0 0F BA 77 78 05               lock btr dword ptr [rdi + 0x78], 5
0020A154  48 89 4F 20                     mov qword ptr [rdi + 0x20], rcx
0020A158  41 B0 01                        mov r8b, 1
0020A15B  48 8B CF                        mov rcx, rdi
0020A15E  E8 29 8C 1B 00                  call 0x1403c2d8c
0020A163  45 33 C9                        xor r9d, r9d
0020A166  33 D2                           xor edx, edx
0020A168  48 8B CF                        mov rcx, rdi
0020A16B  44 8B F0                        mov r14d, eax
0020A16E  E8 CD BE 0F 00                  call 0x140306040
0020A173  84 C0                           test al, al
0020A175  0F 84 9A 00 00 00               je 0x14020a215
0020A17B  4C 89 6F 40                     mov qword ptr [rdi + 0x40], r13
0020A17F  48 8B D7                        mov rdx, rdi
0020A182  48 8B CE                        mov rcx, rsi
0020A185  4C 89 6E 10                     mov qword ptr [rsi + 0x10], r13
0020A189  E8 02 2A 17 00                  call 0x14037cb90
0020A18E  48 8B D3                        mov rdx, rbx
0020A191  48 8B CE                        mov rcx, rsi
0020A194  E8 07 12 17 00                  call 0x14037b3a0
0020A199  4C 8B C7                        mov r8, rdi
0020A19C  C6 87 83 02 00 00 21            mov byte ptr [rdi + 0x283], 0x21
0020A1A3  48 8D 55 48                     lea rdx, [rbp + 0x48]
0020A1A7  44 88 A7 86 01 00 00            mov byte ptr [rdi + 0x186], r12b
0020A1AE  48 8B CE                        mov rcx, rsi
0020A1B1  E8 FA 25 01 00                  call 0x14021c7b0
0020A1B6  41 B0 01                        mov r8b, 1
0020A1B9  48 8B D3                        mov rdx, rbx
0020A1BC  48 8B CF                        mov rcx, rdi
0020A1BF  E8 7C F5 4A 00                  call 0x1406b9740
0020A1C4  48 8B CF                        mov rcx, rdi
0020A1C7  E8 C4 E5 03 00                  call 0x140248790
0020A1CC  41 8B DD                        mov ebx, r13d
0020A1CF  44 39 2D 4A CB DB 00            cmp dword ptr [rip + 0xdbcb4a], r13d
0020A1D6  74 0C                           je 0x14020a1e4
0020A1D8  44 0F 20 C1                     mov rcx, cr8
0020A1DC  41 8A D4                        mov dl, r12b
0020A1DF  E8 B4 B4 2E 00                  call 0x1404f5698
0020A1E4  41 0F B6 CC                     movzx ecx, r12b
0020A1E8  44 0F 22 C1                     mov cr8, rcx
0020A1EC  E9 E1 FD FF FF                  jmp 0x140209fd2
0020A1F1  4C 8D 55 58                     lea r10, [rbp + 0x58]
0020A1F5  BA 01 00 00 00                  mov edx, 1
0020A1FA  E9 DB FE FF FF                  jmp 0x14020a0da
0020A1FF  48 8B 86 48 8E 00 00            mov rax, qword ptr [rsi + 0x8e48]
0020A206  44 39 68 08                     cmp dword ptr [rax + 8], r13d
0020A20A  0F 85 39 FE FF FF               jne 0x14020a049
0020A210  E9 20 01 00 00                  jmp 0x14020a335
0020A215  45 8B CE                        mov r9d, r14d
0020A218  44 88 6C 24 20                  mov byte ptr [rsp + 0x20], r13b
0020A21D  4C 8B C7                        mov r8, rdi
0020A220  33 C9                           xor ecx, ecx
0020A222  E8 E9 D5 04 00                  call 0x140257810
0020A227  E9 4F FF FF FF                  jmp 0x14020a17b
0020A22C  8A D1                           mov dl, cl
0020A22E  41 8A CC                        mov cl, r12b
0020A231  E8 C6 B4 2E 00                  call 0x1404f56fc
0020A236  B9 02 00 00 00                  mov ecx, 2
0020A23B  E9 F3 FD FF FF                  jmp 0x14020a033
0020A240  4C 8B B6 E8 37 00 00            mov r14, qword ptr [rsi + 0x37e8]
0020A247  33 D2                           xor edx, edx
0020A249  49 8B CE                        mov rcx, r14
0020A24C  41 B8 F0 00 00 00               mov r8d, 0xf0
0020A252  E8 E9 C9 4B 00                  call 0x1406c6c40
0020A257  4C 8B C7                        mov r8, rdi
0020A25A  48 8D 55 48                     lea rdx, [rbp + 0x48]
0020A25E  49 8B CE                        mov rcx, r14
0020A261  E8 4A 24 10 00                  call 0x14030c6b0
0020A266  41 F6 C7 01                     test r15b, 1
0020A26A  0F 85 15 02 00 00               jne 0x14020a485
0020A270  B3 01                           mov bl, 1
0020A272  48 8B D6                        mov rdx, rsi
0020A275  49 8B CE                        mov rcx, r14
0020A278  E8 E3 8D 14 00                  call 0x140353060
0020A27D  4C 8B C8                        mov r9, rax
0020A280  44 0F B6 40 20                  movzx r8d, byte ptr [rax + 0x20]
0020A285  41 8A C8                        mov cl, r8b
0020A288  84 DB                           test bl, bl
0020A28A  0F 84 D7 00 00 00               je 0x14020a367
0020A290  80 C9 10                        or cl, 0x10
0020A293  88 48 20                        mov byte ptr [rax + 0x20], cl
0020A296  80 48 22 02                     or byte ptr [rax + 0x22], 2
0020A29A  41 F6 C0 02                     test r8b, 2
0020A29E  0F 85 99 01 00 00               jne 0x14020a43d
0020A2A4  48 8D 55 50                     lea rdx, [rbp + 0x50]
0020A2A8  49 8B CE                        mov rcx, r14
0020A2AB  E8 70 E3 04 00                  call 0x140258620
0020A2B0  4C 8D 4D 50                     lea r9, [rbp + 0x50]
0020A2B4  45 33 C0                        xor r8d, r8d
0020A2B7  48 8B D6                        mov rdx, rsi
0020A2BA  49 8B CE                        mov rcx, r14
0020A2BD  E8 5E 2C 10 00                  call 0x14030cf20
0020A2C2  48 8B 5D 50                     mov rbx, qword ptr [rbp + 0x50]
0020A2C6  44 8A F8                        mov r15b, al
0020A2C9  84 C0                           test al, al
0020A2CB  75 09                           jne 0x14020a2d6
0020A2CD  48 85 DB                        test rbx, rbx
0020A2D0  0F 84 C8 FD FF FF               je 0x14020a09e
0020A2D6  48 8D 4D 48                     lea rcx, [rbp + 0x48]
0020A2DA  E8 71 F9 18 00                  call 0x140399c50
0020A2DF  4C 89 6F 40                     mov qword ptr [rdi + 0x40], r13
0020A2E3  45 84 FF                        test r15b, r15b
0020A2E6  0F 85 E5 00 00 00               jne 0x14020a3d1
0020A2EC  48 85 DB                        test rbx, rbx
0020A2EF  0F 85 A5 01 00 00               jne 0x14020a49a
0020A2F5  41 8B DD                        mov ebx, r13d
0020A2F8  F0 48 0F BA 6F 40 00            lock bts qword ptr [rdi + 0x40], 0
0020A2FF  0F 83 B9 00 00 00               jae 0x14020a3be
0020A305  FF C3                           inc ebx
0020A307  85 1D 9F AF DB 00               test dword ptr [rip + 0xdbaf9f], ebx
0020A30D  0F 84 03 01 00 00               je 0x14020a416
0020A313  F3 90                           pause
0020A315  48 8B 47 40                     mov rax, qword ptr [rdi + 0x40]
0020A319  48 85 C0                        test rax, rax
0020A31C  74 DA                           je 0x14020a2f8
0020A31E  EB E5                           jmp 0x14020a305
0020A320  48 8D 4D 48                     lea rcx, [rbp + 0x48]
0020A324  E8 27 F9 18 00                  call 0x140399c50
0020A329  48 8B CF                        mov rcx, rdi
0020A32C  4C 89 6F 40                     mov qword ptr [rdi + 0x40], r13
0020A330  E8 5B E4 03 00                  call 0x140248790
0020A335  BB 24 00 00 40                  mov ebx, 0x40000024
0020A33A  E9 90 FE FF FF                  jmp 0x14020a1cf
0020A33F  4C 8B 77 48                     mov r14, qword ptr [rdi + 0x48]
0020A343  E9 EB FD FF FF                  jmp 0x14020a133
0020A348  F7 47 78 00 00 40 00            test dword ptr [rdi + 0x78], 0x400000
0020A34F  0F 84 FD FC FF FF               je 0x14020a052
0020A355  48 8B CF                        mov rcx, rdi
0020A358  E8 47 4E 2D 00                  call 0x1404df1a4
0020A35D  84 C0                           test al, al
0020A35F  0F 85 ED FC FF FF               jne 0x14020a052
0020A365  EB CE                           jmp 0x14020a335
0020A367  80 C9 08                        or cl, 8
0020A36A  E9 24 FF FF FF                  jmp 0x14020a293
0020A36F  8B 05 43 C7 DB 00               mov eax, dword ptr [rip + 0xdbc743]
0020A375  A8 40                           test al, 0x40
0020A377  0F 84 F9 FC FF FF               je 0x14020a076
0020A37D  E8 0E 51 10 00                  call 0x14030f490
0020A382  84 C0                           test al, al
0020A384  0F 84 EC FC FF FF               je 0x14020a076
0020A38A  8B CB                           mov ecx, ebx
0020A38C  E8 CF 50 10 00                  call 0x14030f460
0020A391  E9 E2 FC FF FF                  jmp 0x14020a078
0020A396  41 0F 0D 08                     prefetchw byte ptr [r8]
0020A39A  41 8B 00                        mov eax, dword ptr [r8]
0020A39D  8B D0                           mov edx, eax
0020A39F  0F BA F2 15                     btr edx, 0x15
0020A3A3  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
0020A3A8  75 F3                           jne 0x14020a39d
0020A3AA  0F BA E0 15                     bt eax, 0x15
0020A3AE  0F 83 7E FD FF FF               jae 0x14020a132
0020A3B4  E8 17 8E 05 00                  call 0x1402631d0
0020A3B9  E9 74 FD FF FF                  jmp 0x14020a132
0020A3BE  4C 8D 45 48                     lea r8, [rbp + 0x48]
0020A3C2  33 D2                           xor edx, edx
0020A3C4  48 8B CE                        mov rcx, rsi
0020A3C7  E8 94 49 10 00                  call 0x14030ed60
0020A3CC  E9 CD FC FF FF                  jmp 0x14020a09e
0020A3D1  45 8B FD                        mov r15d, r13d
0020A3D4  45 38 2E                        cmp byte ptr [r14], r13b
0020A3D7  76 2C                           jbe 0x14020a405
0020A3D9  41 8B C7                        mov eax, r15d
0020A3DC  45 33 C9                        xor r9d, r9d
0020A3DF  45 33 C0                        xor r8d, r8d
0020A3E2  48 8B D6                        mov rdx, rsi
0020A3E5  48 8D 0C 85 02 00 00 00         lea rcx, [rax*4 + 2]
0020A3ED  48 03 C8                        add rcx, rax
0020A3F0  49 8D 0C CE                     lea rcx, [r14 + rcx*8]
0020A3F4  E8 37 BF 14 00                  call 0x140356330
0020A3F9  41 0F B6 06                     movzx eax, byte ptr [r14]
0020A3FD  41 FF C7                        inc r15d
0020A400  44 3B F8                        cmp r15d, eax
0020A403  72 D4                           jb 0x14020a3d9
0020A405  48 8D 8E D8 35 00 00            lea rcx, [rsi + 0x35d8]
0020A40C  E8 EF 7D 04 00                  call 0x140252200
0020A411  E9 D6 FE FF FF                  jmp 0x14020a2ec
0020A416  8B 05 9C C6 DB 00               mov eax, dword ptr [rip + 0xdbc69c]
0020A41C  A8 40                           test al, 0x40
0020A41E  0F 84 EF FE FF FF               je 0x14020a313
0020A424  E8 67 50 10 00                  call 0x14030f490
0020A429  84 C0                           test al, al
0020A42B  0F 84 E2 FE FF FF               je 0x14020a313
0020A431  8B CB                           mov ecx, ebx
0020A433  E8 28 50 10 00                  call 0x14030f460
0020A438  E9 D8 FE FF FF                  jmp 0x14020a315
0020A43D  41 8B D5                        mov edx, r13d
0020A440  45 38 2E                        cmp byte ptr [r14], r13b
0020A443  0F 86 5B FE FF FF               jbe 0x14020a2a4
0020A449  8B C2                           mov eax, edx
0020A44B  4C 8D 04 85 02 00 00 00         lea r8, [rax*4 + 2]
0020A453  4C 03 C0                        add r8, rax
0020A456  4F 8D 04 C6                     lea r8, [r14 + r8*8]
0020A45A  4D 3B C1                        cmp r8, r9
0020A45D  74 13                           je 0x14020a472
0020A45F  41 8A 40 20                     mov al, byte ptr [r8 + 0x20]
0020A463  84 DB                           test bl, bl
0020A465  74 1A                           je 0x14020a481
0020A467  0C 10                           or al, 0x10
0020A469  41 88 40 20                     mov byte ptr [r8 + 0x20], al
0020A46D  41 80 48 22 02                  or byte ptr [r8 + 0x22], 2
0020A472  41 0F B6 06                     movzx eax, byte ptr [r14]
0020A476  FF C2                           inc edx
0020A478  3B D0                           cmp edx, eax
0020A47A  72 CD                           jb 0x14020a449
0020A47C  E9 23 FE FF FF                  jmp 0x14020a2a4
0020A481  0C 08                           or al, 8
0020A483  EB E4                           jmp 0x14020a469
0020A485  80 BF C3 00 00 00 10            cmp byte ptr [rdi + 0xc3], 0x10
0020A48C  41 8A DD                        mov bl, r13b
0020A48F  0F 8C DD FD FF FF               jl 0x14020a272
0020A495  E9 D6 FD FF FF                  jmp 0x14020a270
0020A49A  48 8D 55 50                     lea rdx, [rbp + 0x50]
0020A49E  48 8B CE                        mov rcx, rsi
0020A4A1  E8 DA 38 10 00                  call 0x14030dd80
0020A4A6  E9 4A FE FF FF                  jmp 0x14020a2f5
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KeYieldExecution(int a1, int a2)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (48);
    v_r13 = 0;
    v_stack_p18 = 0;
    v_stack_p10 = 0;
    if (((a1) & (0xFFFFFFFCULL)) == 0) goto loc_00209FEA;
loc_00209FD2:
    v_rsp = (v_rsp) + (48);
    return (unsigned int)((unsigned int)((unsigned int)(0xC000000DULL)));
loc_00209FEA:
    if ((*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 33752)) != 0) goto loc_0020A010;
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36424) + 8)) != 0) goto loc_0020A010;
    goto loc_00209FD2;
loc_0020A010:
    if ((*(unsigned int *)(v_rip + 14404851)) != 0) goto loc_0020A22C;
loc_0020A033:
    if ((*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 33752)) == 0) goto loc_0020A1FF;
loc_0020A049:
    if (((2) & ((unsigned __int8)((unsigned int)(a1)))) != 0) goto loc_0020A348;
loc_0020A052:
    a2 = 0;
    result = KiAbProcessPreContextSwitch(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, a4);
loc_0020A05F:
    if (condition_is_above_or_equal) goto loc_0020A083;
loc_0020A068:
    v_rbx = (unsigned int)((0) + 1);
    if (((*(unsigned int *)(v_rip + 14398012)) & ((unsigned int)(v_rbx))) == 0) goto loc_0020A36F;
loc_0020A076:
loc_0020A078:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 64) == 0) goto loc_0020A05F;
    goto loc_0020A068;
loc_0020A083:
    result = KiAcquirePrcbLocksForIsolationUnit(*(unsigned __int64 *)(gs_base + (0 + 32)), 1, v_stack_p10, a4);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 16)) == 0) goto loc_0020A240;
loc_0020A09E:
    v_rbx = (v_stack_p10) & (-2);
    v_stack_p20 = v_rbx;
    result = (unsigned int)((v_stack_p10) & (1));
    if (condition_is_equal) goto loc_0020A0F0;
    if ((unsigned int)(result) == 0) goto loc_0020A1F1;
    v_r10 = 0;
    if (((unsigned int)(result)) == 1) {
        result = *(unsigned __int64 *)(v_rbx + 36440);
        v_r10 = *(unsigned __int64 *)(v_rbx + 36440);
        v_r10 = (v_r10) + (8);
        a2 = *(unsigned __int8 *)(result);
    }
    result = KzReleaseAdditionalPrcbLocks(v_r10, a2, v_stack_p20, 1);
    v_stack_p10 = v_rbx;
loc_0020A0F0:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 16) == 0) goto loc_0020A320;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 32)) != 0) goto loc_0020A33F;
    a3 = 0;
    result = KiUpdateTotalCyclesCurrentThread(*(unsigned __int64 *)(gs_base + (0 + 32)), *(unsigned __int64 *)(gs_base + (0 + 392)), a3, 1);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) != 0) goto loc_0020A396;
loc_0020A132:
loc_0020A133:
    result = KiQueryQuantumReset(*(unsigned __int64 *)(gs_base + (0 + 392)), *(unsigned __int64 *)(gs_base + (0 + 392)), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), 1);
    result = (unsigned int)((result) * (*(unsigned int *)(v_rip + 14397270)));
    a1 = ((unsigned int)((unsigned int)(result))) + (result);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 120)))) & (32)) != 0) {
    }
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 32) = a1;
    result = KiComputeNewPriority(*(unsigned __int64 *)(gs_base + (0 + 392)), *(unsigned __int64 *)(gs_base + (0 + 392)), 1, 1);
    a4 = 0;
    a2 = 0;
    result = KiUpdateVPBackingThreadPriority(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, 1, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0020A215;
loc_0020A17B:
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 64) = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 16) = 0;
    result = KiCaptureTotalCyclesCurrentThread(*(unsigned __int64 *)(gs_base + (0 + 32)), *(unsigned __int64 *)(gs_base + (0 + 392)), 1, a4);
    result = KiUpdatePriorityMatrixForRunningTransition(*(unsigned __int64 *)(gs_base + (0 + 32)), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 16), 1, a4);
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 643) = 33;
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) = (unsigned __int8)(v_cr8);
    result = KiQueueReadyThread(*(unsigned __int64 *)(gs_base + (0 + 32)), v_stack_p10, *(unsigned __int64 *)(gs_base + (0 + 392)), a4);
    result = KiSwapContext(*(unsigned __int64 *)(gs_base + (0 + 392)), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 16), 1, a4);
    result = KiAbProcessPostContextSwitch(*(unsigned __int64 *)(gs_base + (0 + 392)), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 16), 1, a4);
loc_0020A1CF:
    if ((*(unsigned int *)(v_rip + 14404426)) != 0) {
        a1 = 2;
        a2 = (unsigned __int8)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, 1, a4);
    }
    goto loc_00209FD2;
loc_0020A1F1:
    goto loc_0020A0DA;
loc_0020A1FF:
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36424) + 8)) != 0) goto loc_0020A049;
    goto loc_0020A335;
loc_0020A215:
    v_stack_p20 = 0;
    a1 = 0;
    result = KiUpdateThreadPriority(a1, 1, *(unsigned __int64 *)(gs_base + (0 + 392)), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
    goto loc_0020A17B;
loc_0020A22C:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(v_cr8), 0, *(unsigned __int64 *)(gs_base + (0 + 392)), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
    goto loc_0020A033;
loc_0020A240:
    a2 = 0;
    result = memset(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14312), a2, 240, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
    result = KiStartRescheduleContext(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14312), v_stack_p10, *(unsigned __int64 *)(gs_base + (0 + 392)), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
    if ((((unsigned __int8)((unsigned int)(a1))) & (1)) != 0) goto loc_0020A485;
loc_0020A270:
loc_0020A272:
    result = KiFindRescheduleContextEntryForPrcb(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14312), *(unsigned __int64 *)(gs_base + (0 + 32)), *(unsigned __int64 *)(gs_base + (0 + 392)), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
    if (1 == 0) goto loc_0020A367;
    a1 = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(result + 32))) | (16));
loc_0020A293:
    *(unsigned __int8 *)(result + 32) = (unsigned __int8)(a1);
    if ((((unsigned __int8)(*(unsigned __int8 *)(result + 32))) & (2)) != 0) goto loc_0020A43D;
loc_0020A2A4:
    result = KiSearchForNewThreadsForRescheduleContext(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14312), v_stack_p18, *(unsigned __int8 *)(result + 32), result);
    a3 = 0;
    result = KiCommitRescheduleContext(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14312), *(unsigned __int64 *)(gs_base + (0 + 32)), a3, v_stack_p18);
    if ((unsigned __int8)(result) != 0) goto loc_0020A2D6;
    if (v_stack_p18 == 0) goto loc_0020A09E;
loc_0020A2D6:
    result = KiReleasePrcbLocksForIsolationUnit(v_stack_p10, *(unsigned __int64 *)(gs_base + (0 + 32)), a3, v_stack_p18);
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 64) = 0;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) goto loc_0020A3D1;
loc_0020A2EC:
    if (v_stack_p18 != 0) goto loc_0020A49A;
loc_0020A2F5:
loc_0020A2F8:
    if (condition_is_above_or_equal) goto loc_0020A3BE;
loc_0020A305:
    v_rbx = (unsigned int)((0) + 1);
    if (((*(unsigned int *)(v_rip + 14397343)) & ((unsigned int)(v_rbx))) == 0) goto loc_0020A416;
loc_0020A313:
loc_0020A315:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 64) == 0) goto loc_0020A2F8;
    goto loc_0020A305;
loc_0020A320:
    result = KiReleasePrcbLocksForIsolationUnit(v_stack_p10, *(unsigned __int64 *)(gs_base + (0 + 32)), a3, v_stack_p18);
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 64) = 0;
    result = KiAbProcessPostContextSwitch(*(unsigned __int64 *)(gs_base + (0 + 392)), *(unsigned __int64 *)(gs_base + (0 + 32)), a3, v_stack_p18);
loc_0020A335:
    goto loc_0020A1CF;
loc_0020A33F:
    goto loc_0020A133;
loc_0020A348:
    if (((*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 120)) & (0x400000ULL)) == 0) goto loc_0020A052;
    result = KiVpBackingThreadYieldExecution(*(unsigned __int64 *)(gs_base + (0 + 392)), *(unsigned __int64 *)(gs_base + (0 + 32)), a3, v_stack_p18);
    if ((unsigned __int8)(result) != 0) goto loc_0020A052;
    goto loc_0020A335;
loc_0020A367:
    a1 = (unsigned __int8)((*(unsigned __int64 *)(gs_base + (0 + 392))) | (8));
    goto loc_0020A293;
loc_0020A36F:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14403395)))) & (64)) == 0) goto loc_0020A076;
    result = KiCheckVpBackingLongSpinWaitHypercall(a1, *(unsigned __int64 *)(gs_base + (0 + 32)), a3, v_stack_p18);
    if ((unsigned __int8)(result) == 0) goto loc_0020A076;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)((unsigned int)(0x40000024ULL))), *(unsigned __int64 *)(gs_base + (0 + 32)), a3, v_stack_p18);
    goto loc_0020A078;
loc_0020A396:
loc_0020A39D:
    if ((unsigned __int8)(result) != 0) goto loc_0020A39D;
    if (condition_is_above_or_equal) goto loc_0020A132;
    result = KiRemoveSystemWorkPriorityKick((unsigned int)((unsigned int)((unsigned int)(0x40000024ULL))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a3)))), a3, v_stack_p18);
    goto loc_0020A132;
loc_0020A3BE:
    a2 = 0;
    result = KiAcquirePrcbLocksForIsolationUnit(*(unsigned __int64 *)(gs_base + (0 + 32)), a2, v_stack_p10, v_stack_p18);
    goto loc_0020A09E;
loc_0020A3D1:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 72))) <= 0) goto loc_0020A405;
loc_0020A3D9:
    a4 = 0;
    a3 = 0;
    a1 = (0 * 4 + 2) + (0);
    result = KiCompleteRescheduleContextEntry(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 72) + a1 * 8, *(unsigned __int64 *)(gs_base + (0 + 32)), a3, a4);
    v_r15 = (unsigned int)((0) + 1);
    if (((unsigned int)(v_r15)) < ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 72))))) goto loc_0020A3D9;
loc_0020A405:
    result = KiFlushSoftwareInterruptBatch(*(unsigned __int64 *)(gs_base + (0 + 32)) + 13784, *(unsigned __int64 *)(gs_base + (0 + 32)), a3, a4);
    goto loc_0020A2EC;
loc_0020A416:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14403228)))) & (64)) == 0) goto loc_0020A313;
    result = KiCheckVpBackingLongSpinWaitHypercall(*(unsigned __int64 *)(gs_base + (0 + 32)) + 13784, *(unsigned __int64 *)(gs_base + (0 + 32)), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0020A313;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)((unsigned int)(0x40000024ULL))), *(unsigned __int64 *)(gs_base + (0 + 32)), a3, a4);
    goto loc_0020A315;
loc_0020A43D:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 72))) <= 0) goto loc_0020A2A4;
loc_0020A449:
    a3 = (0 * 4 + 2) + (0);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 72) + a3 * 8) == 0) goto loc_0020A472;
    if ((unsigned __int8)((unsigned int)(0x40000024ULL)) == 0) goto loc_0020A481;
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 72) + a3 * 8 + 32)) | (16));
loc_0020A469:
    *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 72) + a3 * 8 + 32) = (unsigned __int8)(result);
loc_0020A472:
    a2 = (unsigned int)((0) + 1);
    if (a2 < ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 72))))) goto loc_0020A449;
    goto loc_0020A2A4;
loc_0020A481:
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 72))) | (8));
    goto loc_0020A469;
loc_0020A485:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 195)) < 16) goto loc_0020A272;
    goto loc_0020A270;
loc_0020A49A:
    result = KiReadyDeferredReadyList(*(unsigned __int64 *)(gs_base + (0 + 32)), v_stack_p18, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 72) + a3 * 8, a4);
    goto loc_0020A2F5;
}
```

## 5. (Beta) C Style

```c
int64_t KeYieldExecution(int32_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (48);
    local_r13 = 0;
    v_stack_p18 = 0;
    v_stack_p10 = 0;
    if (((Arg1) & (0xFFFFFFFCULL)) == 0) goto loc_00209FEA;
loc_00209FD2:
    local_rsp = (local_rsp) + (48);
    return (uint32_t)((uint32_t)((uint32_t)(0xC000000DULL)));
loc_00209FEA:
    if ((*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x83D8)) != 0) goto loc_0020A010;
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8E48) + 0x8)) != 0) goto loc_0020A010;
    goto loc_00209FD2;
loc_0020A010:
    if ((*(uint32_t *)(v_rip + 0xDBCCF3)) != 0) goto loc_0020A22C;
loc_0020A033:
    if ((*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x83D8)) == 0) goto loc_0020A1FF;
loc_0020A049:
    if (((2) & ((uint8_t)((uint32_t)(Arg1)))) != 0) goto loc_0020A348;
loc_0020A052:
    Arg2 = 0;
    result = KiAbProcessPreContextSwitch(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, a3, a4);
loc_0020A05F:
    if (condition_is_above_or_equal) goto loc_0020A083;
loc_0020A068:
    local_rbx = (uint32_t)((0) + 1);
    if (((*(uint32_t *)(v_rip + 0xDBB23C)) & ((uint32_t)(local_rbx))) == 0) goto loc_0020A36F;
loc_0020A076:
loc_0020A078:
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x40) == 0) goto loc_0020A05F;
    goto loc_0020A068;
loc_0020A083:
    result = KiAcquirePrcbLocksForIsolationUnit(*(uint64_t *)(gs_base + (0 + 0x20)), 1, v_stack_p10, a4);
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x10)) == 0) goto loc_0020A240;
loc_0020A09E:
    local_rbx = (v_stack_p10) & (-2);
    v_stack_p20 = local_rbx;
    result = (uint32_t)((v_stack_p10) & (1));
    if (condition_is_equal) goto loc_0020A0F0;
    if ((uint32_t)(result) == 0) goto loc_0020A1F1;
    local_r10 = 0;
    if (((uint32_t)(result)) == 1) {
        result = *(uint64_t *)(local_rbx + 0x8E58);
        local_r10 = *(uint64_t *)(local_rbx + 0x8E58);
        local_r10 = (local_r10) + (8);
        Arg2 = *(uint8_t *)(result);
    }
    result = KzReleaseAdditionalPrcbLocks(local_r10, Arg2, v_stack_p20, 1);
    v_stack_p10 = local_rbx;
loc_0020A0F0:
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x10) == 0) goto loc_0020A320;
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x20)) != 0) goto loc_0020A33F;
    a3 = 0;
    result = KiUpdateTotalCyclesCurrentThread(*(uint64_t *)(gs_base + (0 + 0x20)), *(uint64_t *)(gs_base + (0 + 0x188)), a3, 1);
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) != 0) goto loc_0020A396;
loc_0020A132:
loc_0020A133:
    result = KiQueryQuantumReset(*(uint64_t *)(gs_base + (0 + 0x188)), *(uint64_t *)(gs_base + (0 + 0x188)), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), 1);
    result = (uint32_t)((result) * (*(uint32_t *)(v_rip + 0xDBAF56)));
    Arg1 = ((uint32_t)((uint32_t)(result))) + (result);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x78)))) & (32)) != 0) {
    }
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x20) = Arg1;
    result = KiComputeNewPriority(*(uint64_t *)(gs_base + (0 + 0x188)), *(uint64_t *)(gs_base + (0 + 0x188)), 1, 1);
    a4 = 0;
    Arg2 = 0;
    result = KiUpdateVPBackingThreadPriority(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, 1, a4);
    if ((uint8_t)(result) == 0) goto loc_0020A215;
loc_0020A17B:
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x40) = 0;
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x10) = 0;
    result = KiCaptureTotalCyclesCurrentThread(*(uint64_t *)(gs_base + (0 + 0x20)), *(uint64_t *)(gs_base + (0 + 0x188)), 1, a4);
    result = KiUpdatePriorityMatrixForRunningTransition(*(uint64_t *)(gs_base + (0 + 0x20)), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x10), 1, a4);
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x283) = 33;
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) = (uint8_t)(v_cr8);
    result = KiQueueReadyThread(*(uint64_t *)(gs_base + (0 + 0x20)), v_stack_p10, *(uint64_t *)(gs_base + (0 + 0x188)), a4);
    result = KiSwapContext(*(uint64_t *)(gs_base + (0 + 0x188)), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x10), 1, a4);
    result = KiAbProcessPostContextSwitch(*(uint64_t *)(gs_base + (0 + 0x188)), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x10), 1, a4);
loc_0020A1CF:
    if ((*(uint32_t *)(v_rip + 0xDBCB4A)) != 0) {
        Arg1 = 2;
        Arg2 = (uint8_t)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, 1, a4);
    }
    goto loc_00209FD2;
loc_0020A1F1:
    goto loc_0020A0DA;
loc_0020A1FF:
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8E48) + 0x8)) != 0) goto loc_0020A049;
    goto loc_0020A335;
loc_0020A215:
    v_stack_p20 = 0;
    Arg1 = 0;
    result = KiUpdateThreadPriority(Arg1, 1, *(uint64_t *)(gs_base + (0 + 0x188)), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
    goto loc_0020A17B;
loc_0020A22C:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(v_cr8), 0, *(uint64_t *)(gs_base + (0 + 0x188)), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
    goto loc_0020A033;
loc_0020A240:
    Arg2 = 0;
    result = memset(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x37E8), Arg2, 240, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
    result = KiStartRescheduleContext(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x37E8), v_stack_p10, *(uint64_t *)(gs_base + (0 + 0x188)), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
    if ((((uint8_t)((uint32_t)(Arg1))) & (1)) != 0) goto loc_0020A485;
loc_0020A270:
loc_0020A272:
    result = KiFindRescheduleContextEntryForPrcb(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x37E8), *(uint64_t *)(gs_base + (0 + 0x20)), *(uint64_t *)(gs_base + (0 + 0x188)), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
    if (1 == 0) goto loc_0020A367;
    Arg1 = (uint8_t)(((uint8_t)(*(uint8_t *)(result + 0x20))) | (16));
loc_0020A293:
    *(uint8_t *)(result + 0x20) = (uint8_t)(Arg1);
    if ((((uint8_t)(*(uint8_t *)(result + 0x20))) & (2)) != 0) goto loc_0020A43D;
loc_0020A2A4:
    result = KiSearchForNewThreadsForRescheduleContext(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x37E8), v_stack_p18, *(uint8_t *)(result + 0x20), result);
    a3 = 0;
    result = KiCommitRescheduleContext(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x37E8), *(uint64_t *)(gs_base + (0 + 0x20)), a3, v_stack_p18);
    if ((uint8_t)(result) != 0) goto loc_0020A2D6;
    if (v_stack_p18 == 0) goto loc_0020A09E;
loc_0020A2D6:
    result = KiReleasePrcbLocksForIsolationUnit(v_stack_p10, *(uint64_t *)(gs_base + (0 + 0x20)), a3, v_stack_p18);
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x40) = 0;
    if ((uint8_t)((uint8_t)(result)) != 0) goto loc_0020A3D1;
loc_0020A2EC:
    if (v_stack_p18 != 0) goto loc_0020A49A;
loc_0020A2F5:
loc_0020A2F8:
    if (condition_is_above_or_equal) goto loc_0020A3BE;
loc_0020A305:
    local_rbx = (uint32_t)((0) + 1);
    if (((*(uint32_t *)(v_rip + 0xDBAF9F)) & ((uint32_t)(local_rbx))) == 0) goto loc_0020A416;
loc_0020A313:
loc_0020A315:
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x40) == 0) goto loc_0020A2F8;
    goto loc_0020A305;
loc_0020A320:
    result = KiReleasePrcbLocksForIsolationUnit(v_stack_p10, *(uint64_t *)(gs_base + (0 + 0x20)), a3, v_stack_p18);
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x40) = 0;
    result = KiAbProcessPostContextSwitch(*(uint64_t *)(gs_base + (0 + 0x188)), *(uint64_t *)(gs_base + (0 + 0x20)), a3, v_stack_p18);
loc_0020A335:
    goto loc_0020A1CF;
loc_0020A33F:
    goto loc_0020A133;
loc_0020A348:
    if (((*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x78)) & (0x400000ULL)) == 0) goto loc_0020A052;
    result = KiVpBackingThreadYieldExecution(*(uint64_t *)(gs_base + (0 + 0x188)), *(uint64_t *)(gs_base + (0 + 0x20)), a3, v_stack_p18);
    if ((uint8_t)(result) != 0) goto loc_0020A052;
    goto loc_0020A335;
loc_0020A367:
    Arg1 = (uint8_t)((*(uint64_t *)(gs_base + (0 + 0x188))) | (8));
    goto loc_0020A293;
loc_0020A36F:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xDBC743)))) & (64)) == 0) goto loc_0020A076;
    result = KiCheckVpBackingLongSpinWaitHypercall(Arg1, *(uint64_t *)(gs_base + (0 + 0x20)), a3, v_stack_p18);
    if ((uint8_t)(result) == 0) goto loc_0020A076;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)((uint32_t)(0x40000024ULL))), *(uint64_t *)(gs_base + (0 + 0x20)), a3, v_stack_p18);
    goto loc_0020A078;
loc_0020A396:
loc_0020A39D:
    if ((uint8_t)(result) != 0) goto loc_0020A39D;
    if (condition_is_above_or_equal) goto loc_0020A132;
    result = KiRemoveSystemWorkPriorityKick((uint32_t)((uint32_t)((uint32_t)(0x40000024ULL))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(a3)))), a3, v_stack_p18);
    goto loc_0020A132;
loc_0020A3BE:
    Arg2 = 0;
    result = KiAcquirePrcbLocksForIsolationUnit(*(uint64_t *)(gs_base + (0 + 0x20)), Arg2, v_stack_p10, v_stack_p18);
    goto loc_0020A09E;
loc_0020A3D1:
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x48))) <= 0) goto loc_0020A405;
loc_0020A3D9:
    a4 = 0;
    a3 = 0;
    Arg1 = (0 * 4 + 2) + (0);
    result = KiCompleteRescheduleContextEntry(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x48) + Arg1 * 8, *(uint64_t *)(gs_base + (0 + 0x20)), a3, a4);
    local_r15 = (uint32_t)((0) + 1);
    if (((uint32_t)(local_r15)) < ((uint32_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x48))))) goto loc_0020A3D9;
loc_0020A405:
    result = KiFlushSoftwareInterruptBatch(*(uint64_t *)(gs_base + (0 + 0x20)) + 13784, *(uint64_t *)(gs_base + (0 + 0x20)), a3, a4);
    goto loc_0020A2EC;
loc_0020A416:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xDBC69C)))) & (64)) == 0) goto loc_0020A313;
    result = KiCheckVpBackingLongSpinWaitHypercall(*(uint64_t *)(gs_base + (0 + 0x20)) + 13784, *(uint64_t *)(gs_base + (0 + 0x20)), a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0020A313;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)((uint32_t)(0x40000024ULL))), *(uint64_t *)(gs_base + (0 + 0x20)), a3, a4);
    goto loc_0020A315;
loc_0020A43D:
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x48))) <= 0) goto loc_0020A2A4;
loc_0020A449:
    a3 = (0 * 4 + 2) + (0);
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x48) + a3 * 8) == 0) goto loc_0020A472;
    if ((uint8_t)((uint32_t)(0x40000024ULL)) == 0) goto loc_0020A481;
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x48) + a3 * 8 + 0x20)) | (16));
loc_0020A469:
    *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x48) + a3 * 8 + 0x20) = (uint8_t)(result);
loc_0020A472:
    Arg2 = (uint32_t)((0) + 1);
    if (Arg2 < ((uint32_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x48))))) goto loc_0020A449;
    goto loc_0020A2A4;
loc_0020A481:
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x48))) | (8));
    goto loc_0020A469;
loc_0020A485:
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xC3)) < 16) goto loc_0020A272;
    goto loc_0020A270;
loc_0020A49A:
    result = KiReadyDeferredReadyList(*(uint64_t *)(gs_base + (0 + 0x20)), v_stack_p18, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x48) + a3 * 8, a4);
    goto loc_0020A2F5;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00209FA0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
