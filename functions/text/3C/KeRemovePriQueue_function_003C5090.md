# KeRemovePriQueue

- RVA: `0x003C5090`–`0x003C57F8` (길이 `1,896` bytes)
- VA: `0x00000001403C5090`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008E460`
- 디코드: `444`개 명령, `1,896/1,896` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **31**; 고유 호출 대상: **23**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x003C50E1` → [KiCheckWaitNext](KiCheckWaitNext_function_003C5FC0.md) (function, `0x003C5FC0`)
- `0x003C5190` → [KiPerformWaitDeferredWork](../22/KiPerformWaitDeferredWork_function_00220480.md) (function, `0x00220480`)
- `0x003C51B4` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x003C5230` → [KiAcquireKobjectLockSafe](../25/KiAcquireKobjectLockSafe_function_00251C90.md) (function, `0x00251C90`)
- `0x003C539F` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x003C53AE` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x003C53C6` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x003C53D5` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x003C5410` → [KiCommitThreadWait](../20/KiCommitThreadWait_function_0020DFE0.md) (function, `0x0020DFE0`)
- `0x003C543D` → [EtwTracePriQDequeueWork](EtwTracePriQDequeueWork_function_003C6608.md) (function, `0x003C6608`)
- `0x003C5488` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x003C54AC` → [KiReleaseThreadLockLowerIrql](KiReleaseThreadLockLowerIrql_function_003C65D0.md) (function, `0x003C65D0`)
- `0x003C54B8` → [KiDeliverApc](../25/KiDeliverApc_function_00250F20.md) (function, `0x00250F20`)
- `0x003C5516` → [KiAttemptFastRemovePriQueue](KiAttemptFastRemovePriQueue_function_003C6AA0.md) (function, `0x003C6AA0`)
- `0x003C554B` → [KiSetBasePriorityAndClearDecrement](KiSetBasePriorityAndClearDecrement_function_003C6B9C.md) (function, `0x003C6B9C`)
- `0x003C5555` → [KiAdjustRealtimePriorityFloor](../21/KiAdjustRealtimePriorityFloor_function_0021FBE0.md) (function, `0x0021FBE0`)
- `0x003C5562` → [KiComputeThreadPriority](KiComputeThreadPriority_function_003C45F4.md) (function, `0x003C45F4`)
- `0x003C558F` → [KiUpdateTotalCyclesCurrentThread](../37/KiUpdateTotalCyclesCurrentThread_function_0037DE40.md) (function, `0x0037DE40`)
- `0x003C55B4` → [KiQueryQuantumReset](../21/KiQueryQuantumReset_function_0021F6B4.md) (function, `0x0021F6B4`)
- `0x003C55DF` → [KiSetPriorityThread](../22/KiSetPriorityThread_function_00220E78.md) (function, `0x00220E78`)
- `0x003C561D` → [KiFastExitThreadWait](../22/KiFastExitThreadWait_function_00220BB0.md) (function, `0x00220BB0`)
- `0x003C5634` → [EtwTracePriQDequeueWork](EtwTracePriQDequeueWork_function_003C6608.md) (function, `0x003C6608`)
- `0x003C56A4` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x003C56D4` → [KiSwitchPriQueue](KiSwitchPriQueue_function_003C6DC0.md) (function, `0x003C6DC0`)
- `0x003C56F5` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x003C5704` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x003C572C` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x003C5744` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x003C5753` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x003C576D` → [KiProcessDeferredReadyList](../25/KiProcessDeferredReadyList_function_00250800.md) (function, `0x00250800`)
- `0x003C57EE` → [KiProcessThreadWaitList](../25/KiProcessThreadWaitList_function_00252CC0.md) (function, `0x00252CC0`)

### Direct callers
- [ExpWorkerThread](../4E/ExpWorkerThread_function_004ECAF0.md) at `0x004ECBC6`

### Static image references
- `0x003C5128` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x003C51A5` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x003C5391` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x003C542B` → RVA `0x00FC6B04` (`ALMOSTRO`; read)
- `0x003C55B9` → RVA `0x00FC5098` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003C5090  48 8B C4                        mov rax, rsp
003C5093  48 89 58 20                     mov qword ptr [rax + 0x20], rbx
003C5097  44 88 40 18                     mov byte ptr [rax + 0x18], r8b
003C509B  88 50 10                        mov byte ptr [rax + 0x10], dl
003C509E  48 89 48 08                     mov qword ptr [rax + 8], rcx
003C50A2  55                              push rbp
003C50A3  56                              push rsi
003C50A4  57                              push rdi
003C50A5  41 54                           push r12
003C50A7  41 55                           push r13
003C50A9  41 56                           push r14
003C50AB  41 57                           push r15
003C50AD  48 8B EC                        mov rbp, rsp
003C50B0  48 83 EC 50                     sub rsp, 0x50
003C50B4  65 48 8B 3C 25 88 01 00 00      mov rdi, qword ptr gs:[0x188]
003C50BD  48 8D 4D E4                     lea rcx, [rbp - 0x1c]
003C50C1  45 33 FF                        xor r15d, r15d
003C50C4  48 89 48 98                     mov qword ptr [rax - 0x68], rcx
003C50C8  49 8B D1                        mov rdx, r9
003C50CB  4C 89 7D F0                     mov qword ptr [rbp - 0x10], r15
003C50CF  48 8B CF                        mov rcx, rdi
003C50D2  44 89 7D E0                     mov dword ptr [rbp - 0x20], r15d
003C50D6  4C 8D 4D F0                     lea r9, [rbp - 0x10]
003C50DA  44 89 7D E4                     mov dword ptr [rbp - 0x1c], r15d
003C50DE  45 33 C0                        xor r8d, r8d
003C50E1  E8 DA 0E 00 00                  call 0x1403c5fc0
003C50E6  89 45 E8                        mov dword ptr [rbp - 0x18], eax
003C50E9  44 0F B6 B7 86 01 00 00         movzx r14d, byte ptr [rdi + 0x186]
003C50F1  BB 02 00 00 00                  mov ebx, 2
003C50F6  44 8A 6D 48                     mov r13b, byte ptr [rbp + 0x48]
003C50FA  44 8A 65 50                     mov r12b, byte ptr [rbp + 0x50]
003C50FE  4C 89 7D F8                     mov qword ptr [rbp - 8], r15
003C5102  83 67 74 EF                     and dword ptr [rdi + 0x74], 0xffffffef
003C5106  44 88 7F 70                     mov byte ptr [rdi + 0x70], r15b
003C510A  44 88 AF 87 01 00 00            mov byte ptr [rdi + 0x187], r13b
003C5111  45 84 E4                        test r12b, r12b
003C5114  74 04                           je 0x1403c511a
003C5116  83 4F 74 10                     or dword ptr [rdi + 0x74], 0x10
003C511A  41 8B F7                        mov esi, r15d
003C511D  F0 48 0F BA 6F 40 00            lock bts qword ptr [rdi + 0x40], 0
003C5124  73 1B                           jae 0x1403c5141
003C5126  FF C6                           inc esi
003C5128  85 35 7E 01 C0 00               test dword ptr [rip + 0xc0017e], esi
003C512E  0F 84 5D 02 00 00               je 0x1403c5391
003C5134  F3 90                           pause
003C5136  48 8B 47 40                     mov rax, qword ptr [rdi + 0x40]
003C513A  48 85 C0                        test rax, rax
003C513D  74 DE                           je 0x1403c511d
003C513F  EB E5                           jmp 0x1403c5126
003C5141  44 38 BF C1 00 00 00            cmp byte ptr [rdi + 0xc1], r15b
003C5148  0F 85 41 03 00 00               jne 0x1403c548f
003C514E  8B 5D E8                        mov ebx, dword ptr [rbp - 0x18]
003C5151  4C 8D AF 40 01 00 00            lea r13, [rdi + 0x140]
003C5158  4C 8B 7D 40                     mov r15, qword ptr [rbp + 0x40]
003C515C  45 84 E4                        test r12b, r12b
003C515F  41 BC 7F FF FF FF               mov r12d, 0xffffff7f
003C5165  0F 85 79 01 00 00               jne 0x1403c52e4
003C516B  F6 87 C2 00 00 00 02            test byte ptr [rdi + 0xc2], 2
003C5172  74 6D                           je 0x1403c51e1
003C5174  33 C9                           xor ecx, ecx
003C5176  38 4D 48                        cmp byte ptr [rbp + 0x48], cl
003C5179  74 66                           je 0x1403c51e1
003C517B  BE C0 00 00 00                  mov esi, 0xc0
003C5180  48 89 4D F8                     mov qword ptr [rbp - 8], rcx
003C5184  4C 8D 4D F8                     lea r9, [rbp - 8]
003C5188  48 8B CF                        mov rcx, rdi
003C518B  41 B0 01                        mov r8b, 1
003C518E  8B D3                           mov edx, ebx
003C5190  E8 EB B2 E5 FF                  call 0x140220480
003C5195  48 C7 47 40 00 00 00 00         mov qword ptr [rdi + 0x40], 0
003C519D  85 C0                           test eax, eax
003C519F  0F 85 B8 05 00 00               jne 0x1403c575d
003C51A5  39 05 75 1B C0 00               cmp dword ptr [rip + 0xc01b75], eax
003C51AB  74 0C                           je 0x1403c51b9
003C51AD  44 0F 20 C1                     mov rcx, cr8
003C51B1  41 8A D6                        mov dl, r14b
003C51B4  E8 DF 04 13 00                  call 0x1404f5698
003C51B9  45 0F 22 C6                     mov cr8, r14
003C51BD  45 33 F6                        xor r14d, r14d
003C51C0  48 85 F6                        test rsi, rsi
003C51C3  74 43                           je 0x1403c5208
003C51C5  E9 61 02 00 00                  jmp 0x1403c542b
003C51CA  80 8F C2 00 00 00 02            or byte ptr [rdi + 0xc2], 2
003C51D1  41 B8 C0 00 00 00               mov r8d, 0xc0
003C51D7  41 8B C0                        mov eax, r8d
003C51DA  49 8B F0                        mov rsi, r8
003C51DD  85 C0                           test eax, eax
003C51DF  75 9F                           jne 0x1403c5180
003C51E1  C6 87 84 01 00 00 05            mov byte ptr [rdi + 0x184], 5
003C51E8  48 B8 20 03 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000320
003C51F2  C6 87 83 02 00 00 0F            mov byte ptr [rdi + 0x283], 0xf
003C51F9  45 33 F6                        xor r14d, r14d
003C51FC  8B 00                           mov eax, dword ptr [rax]
003C51FE  89 87 B4 01 00 00               mov dword ptr [rdi + 0x1b4], eax
003C5204  4C 89 77 40                     mov qword ptr [rdi + 0x40], r14
003C5208  4C 8B 87 E8 00 00 00            mov r8, qword ptr [rdi + 0xe8]
003C520F  4D 3B F8                        cmp r15, r8
003C5212  0F 85 B6 04 00 00               jne 0x1403c56ce
003C5218  41 C6 45 10 03                  mov byte ptr [r13 + 0x10], 3
003C521D  49 8B CF                        mov rcx, r15
003C5220  41 C6 45 11 04                  mov byte ptr [r13 + 0x11], 4
003C5225  66 41 C7 45 12 80 00            mov word ptr [r13 + 0x12], 0x80
003C522C  4D 89 7D 20                     mov qword ptr [r13 + 0x20], r15
003C5230  E8 5B CA E8 FF                  call 0x140251c90
003C5235  45 39 77 04                     cmp dword ptr [r15 + 4], r14d
003C5239  0F 85 9F 02 00 00               jne 0x1403c54de
003C523F  41 F6 47 01 01                  test byte ptr [r15 + 1], 1
003C5244  0F 85 06 04 00 00               jne 0x1403c5650
003C524A  8B 4D E4                        mov ecx, dword ptr [rbp - 0x1c]
003C524D  41 B8 02 00 00 00               mov r8d, 2
003C5253  48 8B 45 F0                     mov rax, qword ptr [rbp - 0x10]
003C5257  41 3B C8                        cmp ecx, r8d
003C525A  0F 84 BC 00 00 00               je 0x1403c531c
003C5260  85 C9                           test ecx, ecx
003C5262  74 1F                           je 0x1403c5283
003C5264  48 85 C0                        test rax, rax
003C5267  0F 84 69 05 00 00               je 0x1403c57d6
003C526D  48 B9 14 00 00 00 80 F7 FF FF   movabs rcx, 0xfffff78000000014
003C5277  48 8B 09                        mov rcx, qword ptr [rcx]
003C527A  48 3B C8                        cmp rcx, rax
003C527D  0F 87 53 05 00 00               ja 0x1403c57d6
003C5283  41 8B F6                        mov esi, r14d
003C5286  F0 48 0F BA 6F 40 00            lock bts qword ptr [rdi + 0x40], 0
003C528D  73 1B                           jae 0x1403c52aa
003C528F  FF C6                           inc esi
003C5291  85 35 15 00 C0 00               test dword ptr [rip + 0xc00015], esi
003C5297  0F 84 1B 01 00 00               je 0x1403c53b8
003C529D  F3 90                           pause
003C529F  48 8B 47 40                     mov rax, qword ptr [rdi + 0x40]
003C52A3  48 85 C0                        test rax, rax
003C52A6  74 DE                           je 0x1403c5286
003C52A8  EB E5                           jmp 0x1403c528f
003C52AA  8B 87 1C 02 00 00               mov eax, dword ptr [rdi + 0x21c]
003C52B0  0F B6 C0                        movzx eax, al
003C52B3  8B C8                           mov ecx, eax
003C52B5  0F BA E8 08                     bts eax, 8
003C52B9  89 87 1C 02 00 00               mov dword ptr [rdi + 0x21c], eax
003C52BF  49 8D 47 08                     lea rax, [r15 + 8]
003C52C3  F0 41 FF 8C 8F 18 02 00 00      lock dec dword ptr [r15 + rcx*4 + 0x218]
003C52CC  4C 89 77 40                     mov qword ptr [rdi + 0x40], r14
003C52D0  48 8B 08                        mov rcx, qword ptr [rax]
003C52D3  48 39 41 08                     cmp qword ptr [rcx + 8], rax
003C52D7  0F 84 02 01 00 00               je 0x1403c53df
003C52DD  B9 03 00 00 00                  mov ecx, 3
003C52E2  CD 29                           int 0x29
003C52E4  48 0F BE 55 48                  movsx rdx, byte ptr [rbp + 0x48]
003C52E9  33 C9                           xor ecx, ecx
003C52EB  38 4C 3A 72                     cmp byte ptr [rdx + rdi + 0x72], cl
003C52EF  0F 85 4C 03 00 00               jne 0x1403c5641
003C52F5  84 D2                           test dl, dl
003C52F7  74 10                           je 0x1403c5309
003C52F9  48 8D 87 A8 00 00 00            lea rax, [rdi + 0xa8]
003C5300  48 39 00                        cmp qword ptr [rax], rax
003C5303  0F 85 C1 FE FF FF               jne 0x1403c51ca
003C5309  38 4F 72                        cmp byte ptr [rdi + 0x72], cl
003C530C  0F 85 BC 04 00 00               jne 0x1403c57ce
003C5312  8B C1                           mov eax, ecx
003C5314  48 8B F1                        mov rsi, rcx
003C5317  E9 C1 FE FF FF                  jmp 0x1403c51dd
003C531C  48 B8 B0 03 00 00 80 F7 FF FF   movabs rax, 0xfffff780000003b0
003C5326  48 B9 08 00 00 00 80 F7 FF FF   movabs rcx, 0xfffff78000000008
003C5330  48 8B 00                        mov rax, qword ptr [rax]
003C5333  48 8B 09                        mov rcx, qword ptr [rcx]
003C5336  48 2B 8F F8 00 00 00            sub rcx, qword ptr [rdi + 0xf8]
003C533D  8B 97 B8 03 00 00               mov edx, dword ptr [rdi + 0x3b8]
003C5343  48 2B C8                        sub rcx, rax
003C5346  48 8B 45 F0                     mov rax, qword ptr [rbp - 0x10]
003C534A  44 38 B7 87 01 00 00            cmp byte ptr [rdi + 0x187], r14b
003C5351  0F 84 23 FF FF FF               je 0x1403c527a
003C5357  44 39 B7 E4 01 00 00            cmp dword ptr [rdi + 0x1e4], r14d
003C535E  0F 85 16 FF FF FF               jne 0x1403c527a
003C5364  44 38 B7 86 01 00 00            cmp byte ptr [rdi + 0x186], r14b
003C536B  0F 85 09 FF FF FF               jne 0x1403c527a
003C5371  44 38 B7 C0 00 00 00            cmp byte ptr [rdi + 0xc0], r14b
003C5378  0F 85 FC FE FF FF               jne 0x1403c527a
003C537E  85 D2                           test edx, edx
003C5380  0F 84 F4 FE FF FF               je 0x1403c527a
003C5386  8B C2                           mov eax, edx
003C5388  48 03 45 F0                     add rax, qword ptr [rbp - 0x10]
003C538C  E9 E9 FE FF FF                  jmp 0x1403c527a
003C5391  8B 05 21 17 C0 00               mov eax, dword ptr [rip + 0xc01721]
003C5397  A8 40                           test al, 0x40
003C5399  0F 84 95 FD FF FF               je 0x1403c5134
003C539F  E8 EC A0 F4 FF                  call 0x14030f490
003C53A4  84 C0                           test al, al
003C53A6  0F 84 88 FD FF FF               je 0x1403c5134
003C53AC  8B CE                           mov ecx, esi
003C53AE  E8 AD A0 F4 FF                  call 0x14030f460
003C53B3  E9 7E FD FF FF                  jmp 0x1403c5136
003C53B8  8B 05 FA 16 C0 00               mov eax, dword ptr [rip + 0xc016fa]
003C53BE  A8 40                           test al, 0x40
003C53C0  0F 84 D7 FE FF FF               je 0x1403c529d
003C53C6  E8 C5 A0 F4 FF                  call 0x14030f490
003C53CB  84 C0                           test al, al
003C53CD  0F 84 CA FE FF FF               je 0x1403c529d
003C53D3  8B CE                           mov ecx, esi
003C53D5  E8 86 A0 F4 FF                  call 0x14030f460
003C53DA  E9 C0 FE FF FF                  jmp 0x1403c529f
003C53DF  49 89 4D 00                     mov qword ptr [r13], rcx
003C53E3  49 89 45 08                     mov qword ptr [r13 + 8], rax
003C53E7  4C 89 69 08                     mov qword ptr [rcx + 8], r13
003C53EB  4C 89 28                        mov qword ptr [rax], r13
003C53EE  F0 45 21 27                     lock and dword ptr [r15], r12d
003C53F2  4C 8B 4D F0                     mov r9, qword ptr [rbp - 0x10]
003C53F6  49 8B D5                        mov rdx, r13
003C53F9  44 8B 45 E4                     mov r8d, dword ptr [rbp - 0x1c]
003C53FD  48 8B CF                        mov rcx, rdi
003C5400  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
003C5405  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
003C5409  C6 87 4B 02 00 00 01            mov byte ptr [rdi + 0x24b], 1
003C5410  E8 CB 8B E4 FF                  call 0x14020dfe0
003C5415  44 89 75 E8                     mov dword ptr [rbp - 0x18], r14d
003C5419  48 8B F0                        mov rsi, rax
003C541C  44 88 B7 83 02 00 00            mov byte ptr [rdi + 0x283], r14b
003C5423  48 3D 00 01 00 00               cmp rax, 0x100
003C5429  74 33                           je 0x1403c545e
003C542B  F7 05 CF 16 C0 00 00 00 00 01   test dword ptr [rip + 0xc016cf], 0x1000000
003C5435  74 0B                           je 0x1403c5442
003C5437  48 8B D6                        mov rdx, rsi
003C543A  48 8B CF                        mov rcx, rdi
003C543D  E8 C6 11 00 00                  call 0x1403c6608
003C5442  48 8B C6                        mov rax, rsi
003C5445  48 8B 9C 24 A8 00 00 00         mov rbx, qword ptr [rsp + 0xa8]
003C544D  48 83 C4 50                     add rsp, 0x50
003C5451  41 5F                           pop r15
003C5453  41 5E                           pop r14
003C5455  41 5D                           pop r13
003C5457  41 5C                           pop r12
003C5459  5F                              pop rdi
003C545A  5E                              pop rsi
003C545B  5D                              pop rbp
003C545C  C3                              ret
003C545D  CC                              int3
003C545E  44 0F 20 C6                     mov rsi, cr8
003C5462  B8 02 00 00 00                  mov eax, 2
003C5467  44 0F 22 C0                     mov cr8, rax
003C546B  44 39 35 AE 18 C0 00            cmp dword ptr [rip + 0xc018ae], r14d
003C5472  75 0F                           jne 0x1403c5483
003C5474  40 88 B7 86 01 00 00            mov byte ptr [rdi + 0x186], sil
003C547B  45 33 FF                        xor r15d, r15d
003C547E  E9 66 FC FF FF                  jmp 0x1403c50e9
003C5483  8A D0                           mov dl, al
003C5485  40 8A CE                        mov cl, sil
003C5488  E8 6F 02 13 00                  call 0x1404f56fc
003C548D  EB E5                           jmp 0x1403c5474
003C548F  66 44 39 BF E6 01 00 00         cmp word ptr [rdi + 0x1e6], r15w
003C5497  0F 85 B1 FC FF FF               jne 0x1403c514e
003C549D  41 80 FE 01                     cmp r14b, 1
003C54A1  0F 83 A7 FC FF FF               jae 0x1403c514e
003C54A7  B2 01                           mov dl, 1
003C54A9  48 8B CF                        mov rcx, rdi
003C54AC  E8 1F 11 00 00                  call 0x1403c65d0
003C54B1  45 33 C0                        xor r8d, r8d
003C54B4  33 D2                           xor edx, edx
003C54B6  33 C9                           xor ecx, ecx
003C54B8  E8 63 BA E8 FF                  call 0x140250f20
003C54BD  44 0F 20 C1                     mov rcx, cr8
003C54C1  44 0F 22 C3                     mov cr8, rbx
003C54C5  44 39 3D 54 18 C0 00            cmp dword ptr [rip + 0xc01854], r15d
003C54CC  0F 85 D0 01 00 00               jne 0x1403c56a2
003C54D2  44 88 B7 86 01 00 00            mov byte ptr [rdi + 0x186], r14b
003C54D9  E9 24 FC FF FF                  jmp 0x1403c5102
003C54DE  41 8B F6                        mov esi, r14d
003C54E1  F0 48 0F BA 6F 40 00            lock bts qword ptr [rdi + 0x40], 0
003C54E8  73 1B                           jae 0x1403c5505
003C54EA  FF C6                           inc esi
003C54EC  85 35 BA FD BF 00               test dword ptr [rip + 0xbffdba], esi
003C54F2  0F 84 EF 01 00 00               je 0x1403c56e7
003C54F8  F3 90                           pause
003C54FA  48 8B 47 40                     mov rax, qword ptr [rdi + 0x40]
003C54FE  48 85 C0                        test rax, rax
003C5501  74 DE                           je 0x1403c54e1
003C5503  EB E5                           jmp 0x1403c54ea
003C5505  8B 87 1C 02 00 00               mov eax, dword ptr [rdi + 0x21c]
003C550B  48 8D 55 E0                     lea rdx, [rbp - 0x20]
003C550F  44 0F B6 C0                     movzx r8d, al
003C5513  49 8B CF                        mov rcx, r15
003C5516  E8 85 15 00 00                  call 0x1403c6aa0
003C551B  4C 8B F0                        mov r14, rax
003C551E  48 85 C0                        test rax, rax
003C5521  0F 84 6F 01 00 00               je 0x1403c5696
003C5527  44 8B 87 1C 02 00 00            mov r8d, dword ptr [rdi + 0x21c]
003C552E  8B 75 E0                        mov esi, dword ptr [rbp - 0x20]
003C5531  41 0F B6 C0                     movzx eax, r8b
003C5535  3B C6                           cmp eax, esi
003C5537  0F 85 71 01 00 00               jne 0x1403c56ae
003C553D  48 8D 55 E0                     lea rdx, [rbp - 0x20]
003C5541  C6 87 85 02 00 00 00            mov byte ptr [rdi + 0x285], 0
003C5548  48 8B CF                        mov rcx, rdi
003C554B  E8 4C 16 00 00                  call 0x1403c6b9c
003C5550  8B D6                           mov edx, esi
003C5552  48 8B CF                        mov rcx, rdi
003C5555  E8 86 A6 E5 FF                  call 0x14021fbe0
003C555A  45 33 C0                        xor r8d, r8d
003C555D  33 D2                           xor edx, edx
003C555F  48 8B CF                        mov rcx, rdi
003C5562  E8 8D F0 FF FF                  call 0x1403c45f4
003C5567  0F BE 8F C3 00 00 00            movsx ecx, byte ptr [rdi + 0xc3]
003C556E  89 45 E0                        mov dword ptr [rbp - 0x20], eax
003C5571  3B C1                           cmp eax, ecx
003C5573  74 6F                           je 0x1403c55e4
003C5575  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
003C557E  80 79 20 00                     cmp byte ptr [rcx + 0x20], 0
003C5582  0F 85 56 01 00 00               jne 0x1403c56de
003C5588  FA                              cli
003C5589  45 33 C0                        xor r8d, r8d
003C558C  48 8B D7                        mov rdx, rdi
003C558F  E8 AC 88 FB FF                  call 0x14037de40
003C5594  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
003C559D  48 8B F0                        mov rsi, rax
003C55A0  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
003C55A7  4D 85 C0                        test r8, r8
003C55AA  0F 85 5E 01 00 00               jne 0x1403c570e
003C55B0  FB                              sti
003C55B1  48 8B CF                        mov rcx, rdi
003C55B4  E8 FB A0 E5 FF                  call 0x14021f6b4
003C55B9  0F AF 05 D8 FA BF 00            imul eax, dword ptr [rip + 0xbffad8]
003C55C0  8B C8                           mov ecx, eax
003C55C2  8B 47 78                        mov eax, dword ptr [rdi + 0x78]
003C55C5  48 03 CE                        add rcx, rsi
003C55C8  A8 20                           test al, 0x20
003C55CA  74 06                           je 0x1403c55d2
003C55CC  F0 0F BA 77 78 05               lock btr dword ptr [rdi + 0x78], 5
003C55D2  44 8B 45 E0                     mov r8d, dword ptr [rbp - 0x20]
003C55D6  33 D2                           xor edx, edx
003C55D8  48 89 4F 20                     mov qword ptr [rdi + 0x20], rcx
003C55DC  48 8B CF                        mov rcx, rdi
003C55DF  E8 94 B8 E5 FF                  call 0x140220e78
003C55E4  48 C7 47 40 00 00 00 00         mov qword ptr [rdi + 0x40], 0
003C55EC  41 B8 02 00 00 00               mov r8d, 2
003C55F2  F0 45 21 27                     lock and dword ptr [r15], r12d
003C55F6  C6 87 83 02 00 00 00            mov byte ptr [rdi + 0x283], 0
003C55FD  65 48 8B 34 25 20 00 00 00      mov rsi, qword ptr gs:[0x20]
003C5606  48 83 BE 08 2D 00 00 00         cmp qword ptr [rsi + 0x2d08], 0
003C560E  0F 85 CD 01 00 00               jne 0x1403c57e1
003C5614  44 8B C3                        mov r8d, ebx
003C5617  48 8B D7                        mov rdx, rdi
003C561A  48 8B CE                        mov rcx, rsi
003C561D  E8 8E B5 E5 FF                  call 0x140220bb0
003C5622  F7 05 D8 14 C0 00 00 00 00 01   test dword ptr [rip + 0xc014d8], 0x1000000
003C562C  74 0B                           je 0x1403c5639
003C562E  49 8B D6                        mov rdx, r14
003C5631  48 8B CF                        mov rcx, rdi
003C5634  E8 CF 0F 00 00                  call 0x1403c6608
003C5639  49 8B C6                        mov rax, r14
003C563C  E9 04 FE FF FF                  jmp 0x1403c5445
003C5641  88 4C 3A 72                     mov byte ptr [rdx + rdi + 0x72], cl
003C5645  41 B8 01 01 00 00               mov r8d, 0x101
003C564B  E9 87 FB FF FF                  jmp 0x1403c51d7
003C5650  41 8B F6                        mov esi, r14d
003C5653  F0 48 0F BA 6F 40 00            lock bts qword ptr [rdi + 0x40], 0
003C565A  73 1B                           jae 0x1403c5677
003C565C  FF C6                           inc esi
003C565E  85 35 48 FC BF 00               test dword ptr [rip + 0xbffc48], esi
003C5664  0F 84 CC 00 00 00               je 0x1403c5736
003C566A  F3 90                           pause
003C566C  48 8B 47 40                     mov rax, qword ptr [rdi + 0x40]
003C5670  48 85 C0                        test rax, rax
003C5673  74 DE                           je 0x1403c5653
003C5675  EB E5                           jmp 0x1403c565c
003C5677  48 8B 87 E8 00 00 00            mov rax, qword ptr [rdi + 0xe8]
003C567E  49 3B C7                        cmp rax, r15
003C5681  0F 84 F0 00 00 00               je 0x1403c5777
003C5687  4C 89 77 40                     mov qword ptr [rdi + 0x40], r14
003C568B  41 BE 80 00 00 00               mov r14d, 0x80
003C5691  E9 56 FF FF FF                  jmp 0x1403c55ec
003C5696  45 33 F6                        xor r14d, r14d
003C5699  4C 89 77 40                     mov qword ptr [rdi + 0x40], r14
003C569D  E9 9D FB FF FF                  jmp 0x1403c523f
003C56A2  8A D3                           mov dl, bl
003C56A4  E8 53 00 13 00                  call 0x1404f56fc
003C56A9  E9 24 FE FF FF                  jmp 0x1403c54d2
003C56AE  41 81 E0 00 01 00 00            and r8d, 0x100
003C56B5  0F 84 F0 00 00 00               je 0x1403c57ab
003C56BB  40 0F B6 C6                     movzx eax, sil
003C56BF  44 0B C0                        or r8d, eax
003C56C2  44 89 87 1C 02 00 00            mov dword ptr [rdi + 0x21c], r8d
003C56C9  E9 6F FE FF FF                  jmp 0x1403c553d
003C56CE  49 8B D7                        mov rdx, r15
003C56D1  48 8B CF                        mov rcx, rdi
003C56D4  E8 E7 16 00 00                  call 0x1403c6dc0
003C56D9  E9 3A FB FF FF                  jmp 0x1403c5218
003C56DE  48 8B 77 48                     mov rsi, qword ptr [rdi + 0x48]
003C56E2  E9 CA FE FF FF                  jmp 0x1403c55b1
003C56E7  8B 05 CB 13 C0 00               mov eax, dword ptr [rip + 0xc013cb]
003C56ED  A8 40                           test al, 0x40
003C56EF  0F 84 03 FE FF FF               je 0x1403c54f8
003C56F5  E8 96 9D F4 FF                  call 0x14030f490
003C56FA  84 C0                           test al, al
003C56FC  0F 84 F6 FD FF FF               je 0x1403c54f8
003C5702  8B CE                           mov ecx, esi
003C5704  E8 57 9D F4 FF                  call 0x14030f460
003C5709  E9 EC FD FF FF                  jmp 0x1403c54fa
003C570E  41 0F 0D 08                     prefetchw byte ptr [r8]
003C5712  41 8B 00                        mov eax, dword ptr [r8]
003C5715  8B D0                           mov edx, eax
003C5717  0F BA F2 15                     btr edx, 0x15
003C571B  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
003C5720  75 F3                           jne 0x1403c5715
003C5722  0F BA E0 15                     bt eax, 0x15
003C5726  0F 83 84 FE FF FF               jae 0x1403c55b0
003C572C  E8 9F DA E9 FF                  call 0x1402631d0
003C5731  E9 7A FE FF FF                  jmp 0x1403c55b0
003C5736  8B 05 7C 13 C0 00               mov eax, dword ptr [rip + 0xc0137c]
003C573C  A8 40                           test al, 0x40
003C573E  0F 84 26 FF FF FF               je 0x1403c566a
003C5744  E8 47 9D F4 FF                  call 0x14030f490
003C5749  84 C0                           test al, al
003C574B  0F 84 19 FF FF FF               je 0x1403c566a
003C5751  8B CE                           mov ecx, esi
003C5753  E8 08 9D F4 FF                  call 0x14030f460
003C5758  E9 0F FF FF FF                  jmp 0x1403c566c
003C575D  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
003C5766  48 8D 55 F8                     lea rdx, [rbp - 8]
003C576A  45 8A C6                        mov r8b, r14b
003C576D  E8 8E B0 E8 FF                  call 0x140250800
003C5772  E9 46 FA FF FF                  jmp 0x1403c51bd
003C5777  48 8D 87 08 02 00 00            lea rax, [rdi + 0x208]
003C577E  4C 89 B7 E8 00 00 00            mov qword ptr [rdi + 0xe8], r14
003C5785  48 8B 10                        mov rdx, qword ptr [rax]
003C5788  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
003C578C  48 39 42 08                     cmp qword ptr [rdx + 8], rax
003C5790  0F 85 47 FB FF FF               jne 0x1403c52dd
003C5796  48 39 01                        cmp qword ptr [rcx], rax
003C5799  0F 85 3E FB FF FF               jne 0x1403c52dd
003C579F  48 89 11                        mov qword ptr [rcx], rdx
003C57A2  48 89 4A 08                     mov qword ptr [rdx + 8], rcx
003C57A6  E9 DC FE FF FF                  jmp 0x1403c5687
003C57AB  48 8B 8F E8 00 00 00            mov rcx, qword ptr [rdi + 0xe8]
003C57B2  F0 FF 8C 81 18 02 00 00         lock dec dword ptr [rcx + rax*4 + 0x218]
003C57BA  48 63 45 E0                     movsxd rax, dword ptr [rbp - 0x20]
003C57BE  F0 FF 84 81 18 02 00 00         lock inc dword ptr [rcx + rax*4 + 0x218]
003C57C6  8B 75 E0                        mov esi, dword ptr [rbp - 0x20]
003C57C9  E9 ED FE FF FF                  jmp 0x1403c56bb
003C57CE  88 4F 72                        mov byte ptr [rdi + 0x72], cl
003C57D1  E9 6F FE FF FF                  jmp 0x1403c5645
003C57D6  41 BE 02 01 00 00               mov r14d, 0x102
003C57DC  E9 11 FE FF FF                  jmp 0x1403c55f2
003C57E1  45 8B C8                        mov r9d, r8d
003C57E4  48 8B CE                        mov rcx, rsi
003C57E7  45 33 C0                        xor r8d, r8d
003C57EA  41 8D 50 01                     lea edx, [r8 + 1]
003C57EE  E8 CD D4 E8 FF                  call 0x140252cc0
003C57F3  E9 1C FE FF FF                  jmp 0x1403c5614
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KeRemovePriQueue(__int64 a1, unsigned __int8 a2, int a3, __int64 a4)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m50;
    unsigned __int64 v_stack_m54;
    unsigned int v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned int v_stack_m68;
    unsigned __int8 v_stack_p10;
    unsigned __int8 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 32) = v_rbx;
    *(unsigned __int8 *)(v_rsp + 24) = (unsigned __int8)(a3);
    *(unsigned __int8 *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (80);
    v_r15 = 0;
    *(unsigned __int64 *)(v_rsp - 104) = v_stack_m54;
    v_stack_m48 = 0;
    v_stack_m58 = 0;
    v_stack_m54 = 0;
    a3 = 0;
    result = KiCheckWaitNext(*(unsigned __int64 *)(gs_base + (0 + 392)), a4, a3, v_stack_m48);
    v_stack_m50 = (unsigned int)(result);
loc_003C50E9:
    v_stack_m40 = 0;
loc_003C5102:
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 112) = 0;
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 391) = (unsigned __int8)(v_stack_p10);
    if ((unsigned __int8)(v_stack_p18) != 0) {
    }
loc_003C511D:
    if (condition_is_above_or_equal) goto loc_003C5141;
loc_003C5126:
    v_rsi = (unsigned int)((0) + 1);
    if (((*(unsigned int *)(v_rip + 12583294)) & ((unsigned int)(v_rsi))) == 0) goto loc_003C5391;
loc_003C5134:
loc_003C5136:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 64) == 0) goto loc_003C511D;
    goto loc_003C5126;
loc_003C5141:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 193)) != 0) goto loc_003C548F;
loc_003C514E:
    if ((unsigned __int8)(v_stack_p18) != 0) goto loc_003C52E4;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 194)) & (2)) == 0) goto loc_003C51E1;
    a1 = 0;
    if (v_stack_p10 == 0) goto loc_003C51E1;
loc_003C5180:
    v_stack_m40 = 0;
    result = KiPerformWaitDeferredWork(*(unsigned __int64 *)(gs_base + (0 + 392)), (unsigned int)((unsigned int)((unsigned int)(v_stack_m50))), 1, v_stack_m40);
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 64) = 0;
    if ((unsigned int)(result) != 0) goto loc_003C575D;
    if ((*(unsigned int *)(v_rip + 12589941)) != ((unsigned int)(result))) {
        a1 = v_cr8;
        a2 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390));
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, 1, v_stack_m40);
    }
loc_003C51BD:
    v_r14 = 0;
    if (192 == 0) goto loc_003C5208;
    goto loc_003C542B;
loc_003C51CA:
loc_003C51D7:
loc_003C51DD:
    if (192 != 0) goto loc_003C5180;
loc_003C51E1:
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 388) = 5;
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 643) = 15;
    v_r14 = 0;
    *(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 436) = (unsigned int)((unsigned int)(*(unsigned int *)(192)));
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 64) = 0;
loc_003C5208:
    if (v_stack_p8 != (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 232))) goto loc_003C56CE;
loc_003C5218:
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 320 + 16) = 3;
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 320 + 17) = 4;
    *(unsigned __int16 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 320 + 18) = 128;
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 320 + 32) = v_stack_p8;
    result = KiAcquireKobjectLockSafe(v_stack_p8, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 232), v_stack_m40);
    if ((*(unsigned int *)(v_stack_p8 + 4)) != 0) goto loc_003C54DE;
loc_003C523F:
    if (((*(unsigned __int8 *)(v_stack_p8 + 1)) & (1)) != 0) goto loc_003C5650;
    if (((unsigned int)((unsigned int)(v_stack_m54))) == 2) goto loc_003C531C;
    if ((unsigned int)((unsigned int)(v_stack_m54)) == 0) goto loc_003C5283;
    if (v_stack_m48 == 0) goto loc_003C57D6;
loc_003C527A:
    if ((*(unsigned __int64 *)((unsigned int)(v_stack_m54))) > v_stack_m48) goto loc_003C57D6;
loc_003C5283:
loc_003C5286:
    if ((*(unsigned __int64 *)((unsigned int)(v_stack_m54))) >= v_stack_m48) goto loc_003C52AA;
loc_003C528F:
    v_rsi = (unsigned int)((0) + 1);
    if (((*(unsigned int *)(v_rip + 12582933)) & ((unsigned int)(v_rsi))) == 0) goto loc_003C53B8;
loc_003C529D:
loc_003C529F:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 64) == 0) goto loc_003C5286;
    goto loc_003C528F;
loc_003C52AA:
    *(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 540) = (unsigned int)((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 540))));
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 64) = 0;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 8) + 8)) == (v_stack_p8 + 8)) goto loc_003C53DF;
loc_003C52DD:
loc_003C52E4:
    a1 = 0;
    if ((*(unsigned __int8 *)((__int8)(v_stack_p10) + *(unsigned __int64 *)(gs_base + (0 + 392)) * 1 + 114)) != 0) goto loc_003C5641;
    if ((unsigned __int8)((__int8)(v_stack_p10)) == 0) goto loc_003C5309;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 168)) != (*(unsigned __int64 *)(gs_base + (0 + 392)) + 168)) goto loc_003C51CA;
loc_003C5309:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 114)) != 0) goto loc_003C57CE;
    goto loc_003C51DD;
loc_003C531C:
    a1 = (*(unsigned __int64 *)(a1)) - (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 248));
    a1 = (a1) - (*(unsigned __int64 *)(0));
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 391)) == 0) goto loc_003C527A;
    if ((*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 484)) != 0) goto loc_003C527A;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390)) != 0) goto loc_003C527A;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 192)) != 0) goto loc_003C527A;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 952))) == 0) goto loc_003C527A;
    result = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 952))))) + (v_stack_m48);
    goto loc_003C527A;
loc_003C5391:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12588833)))) & (64)) == 0) goto loc_003C5134;
    result = KiCheckVpBackingLongSpinWaitHypercall(a1, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 952)), 2, v_stack_m40);
    if ((unsigned __int8)(result) == 0) goto loc_003C5134;
    result = HvlNotifyLongSpinWait(0, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 952)), 2, v_stack_m40);
    goto loc_003C5136;
loc_003C53B8:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12588794)))) & (64)) == 0) goto loc_003C529D;
    result = KiCheckVpBackingLongSpinWaitHypercall(0, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 952)), 2, v_stack_m40);
    if ((unsigned __int8)(result) == 0) goto loc_003C529D;
    result = HvlNotifyLongSpinWait(0, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 952)), 2, v_stack_m40);
    goto loc_003C529F;
loc_003C53DF:
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 320) = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 320 + 8) = result;
    *(unsigned __int64 *)(0 + 8) = *(unsigned __int64 *)(gs_base + (0 + 392)) + 320;
    *(unsigned __int64 *)(result) = *(unsigned __int64 *)(gs_base + (0 + 392)) + 320;
    v_stack_m60 = 0;
    v_stack_m68 = (unsigned int)((unsigned int)(v_stack_m50));
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 587) = 1;
    result = KiCommitThreadWait(*(unsigned __int64 *)(gs_base + (0 + 392)), *(unsigned __int64 *)(gs_base + (0 + 392)) + 320, (unsigned int)(v_stack_m54), v_stack_m48);
    v_stack_m50 = 0;
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 643) = 0;
    if (result == 256) goto loc_003C545E;
loc_003C542B:
    if (((*(unsigned int *)(v_rip + 12588751)) & (0x1000000ULL)) != 0) {
        a2 = result;
        a1 = *(unsigned __int64 *)(gs_base + (0 + 392));
        result = EtwTracePriQDequeueWork(a1, a2, (unsigned int)(v_stack_m54), v_stack_m48);
    }
loc_003C5445:
    v_rsp = (v_rsp) + (80);
    return result;
loc_003C545E:
    if ((*(unsigned int *)(v_rip + 12589230)) != 0) goto loc_003C5483;
loc_003C5474:
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390));
    v_r15 = 0;
    goto loc_003C50E9;
loc_003C5483:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390)), 2, (unsigned int)(v_stack_m54), v_stack_m48);
    goto loc_003C5474;
loc_003C548F:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 486)) != 0) goto loc_003C514E;
    if (0 >= 1) goto loc_003C514E;
    result = KiReleaseThreadLockLowerIrql(*(unsigned __int64 *)(gs_base + (0 + 392)), 1, (unsigned int)(v_stack_m54), v_stack_m48);
    a3 = 0;
    a2 = 0;
    a1 = 0;
    result = KiDeliverApc(a1, a2, a3, v_stack_m48);
    if ((*(unsigned int *)(v_rip + 12589140)) != 0) goto loc_003C56A2;
loc_003C54D2:
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) = 0;
    goto loc_003C5102;
loc_003C54DE:
loc_003C54E1:
    if ((*(unsigned int *)(v_rip + 12589140)) >= 0) goto loc_003C5505;
loc_003C54EA:
    v_rsi = (unsigned int)((0) + 1);
    if (((*(unsigned int *)(v_rip + 12582330)) & ((unsigned int)(v_rsi))) == 0) goto loc_003C56E7;
loc_003C54F8:
loc_003C54FA:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 64) == 0) goto loc_003C54E1;
    goto loc_003C54EA;
loc_003C5505:
    result = KiAttemptFastRemovePriQueue(0, v_stack_m58, (unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 540))), v_stack_m48);
    if (result == 0) goto loc_003C5696;
    if (((unsigned int)((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 540))))) != ((unsigned int)((unsigned int)(v_stack_m58)))) goto loc_003C56AE;
loc_003C553D:
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 645) = 0;
    result = KiSetBasePriorityAndClearDecrement(*(unsigned __int64 *)(gs_base + (0 + 392)), v_stack_m58, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 540)), v_stack_m48);
    result = KiAdjustRealtimePriorityFloor(*(unsigned __int64 *)(gs_base + (0 + 392)), (unsigned int)((unsigned int)((unsigned int)(v_stack_m58))), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 540)), v_stack_m48);
    a3 = 0;
    a2 = 0;
    result = KiComputeThreadPriority(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, v_stack_m48);
    v_stack_m58 = (unsigned int)(result);
    if (((unsigned int)(result)) == ((unsigned int)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 195))))) goto loc_003C55E4;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 32)) != 0) goto loc_003C56DE;
    a3 = 0;
    result = KiUpdateTotalCyclesCurrentThread(*(unsigned __int64 *)(gs_base + (0 + 32)), *(unsigned __int64 *)(gs_base + (0 + 392)), a3, v_stack_m48);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) != 0) goto loc_003C570E;
loc_003C55B0:
loc_003C55B1:
    result = KiQueryQuantumReset(*(unsigned __int64 *)(gs_base + (0 + 392)), *(unsigned __int64 *)(gs_base + (0 + 392)), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), v_stack_m48);
    result = (unsigned int)((result) * (*(unsigned int *)(v_rip + 12581592)));
    a1 = ((unsigned int)((unsigned int)(result))) + (result);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 120)))) & (32)) != 0) {
    }
    a2 = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 32) = a1;
    result = KiSetPriorityThread(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, (unsigned int)(v_stack_m58), v_stack_m48);
loc_003C55E4:
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 64) = 0;
loc_003C55EC:
loc_003C55F2:
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 643) = 0;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 11528)) != 0) goto loc_003C57E1;
loc_003C5614:
    result = KiFastExitThreadWait(*(unsigned __int64 *)(gs_base + (0 + 32)), *(unsigned __int64 *)(gs_base + (0 + 392)), (unsigned int)((unsigned int)(v_stack_p20)), v_stack_m48);
    if (((*(unsigned int *)(v_rip + 12588248)) & (0x1000000ULL)) != 0) {
        a2 = result;
        a1 = *(unsigned __int64 *)(gs_base + (0 + 392));
        result = EtwTracePriQDequeueWork(a1, a2, (unsigned int)((unsigned int)(v_stack_p20)), v_stack_m48);
    }
    goto loc_003C5445;
loc_003C5641:
    *(unsigned __int8 *)(a2 + *(unsigned __int64 *)(gs_base + (0 + 392)) * 1 + 114) = (unsigned __int8)(a1);
loc_003C5645:
    goto loc_003C51D7;
loc_003C5650:
loc_003C5653:
    if (condition_is_above_or_equal) goto loc_003C5677;
loc_003C565C:
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(result))) + 1);
    if (((*(unsigned int *)(v_rip + 12581960)) & ((unsigned int)(v_rsi))) == 0) goto loc_003C5736;
loc_003C566A:
loc_003C566C:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 64) == 0) goto loc_003C5653;
    goto loc_003C565C;
loc_003C5677:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 232)) == 0) goto loc_003C5777;
loc_003C5687:
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 64) = result;
    goto loc_003C55EC;
loc_003C5696:
    v_r14 = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 64) = 0;
    goto loc_003C523F;
loc_003C56A2:
    result = KiRaiseIrqlProcessIrqlFlags(a1, (unsigned __int8)(v_stack_p20), 257, v_stack_m48);
    goto loc_003C54D2;
loc_003C56AE:
    a3 = (unsigned int)((257) & (256));
    if (condition_is_equal) goto loc_003C57AB;
loc_003C56BB:
    a3 = (unsigned int)((a3) | ((unsigned int)((unsigned __int8)(v_rsi))));
    *(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 540) = a3;
    goto loc_003C553D;
loc_003C56CE:
    result = KiSwitchPriQueue(*(unsigned __int64 *)(gs_base + (0 + 392)), 0, a3, v_stack_m48);
    goto loc_003C5218;
loc_003C56DE:
    goto loc_003C55B1;
loc_003C56E7:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12587979)))) & (64)) == 0) goto loc_003C54F8;
    result = KiCheckVpBackingLongSpinWaitHypercall(*(unsigned __int64 *)(gs_base + (0 + 392)), 0, a3, v_stack_m48);
    if ((unsigned __int8)(result) == 0) goto loc_003C54F8;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 72))), 0, a3, v_stack_m48);
    goto loc_003C54FA;
loc_003C570E:
loc_003C5715:
    if ((unsigned __int8)(result) != 0) goto loc_003C5715;
    if (condition_is_above_or_equal) goto loc_003C55B0;
    result = KiRemoveSystemWorkPriorityKick((unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 72))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a3)))), a3, v_stack_m48);
    goto loc_003C55B0;
loc_003C5736:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12587900)))) & (64)) == 0) goto loc_003C566A;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 72))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a3)))), a3, v_stack_m48);
    if ((unsigned __int8)(result) == 0) goto loc_003C566A;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 72))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a3)))), a3, v_stack_m48);
    goto loc_003C566C;
loc_003C575D:
    result = KiProcessDeferredReadyList(*(unsigned __int64 *)(gs_base + (0 + 32)), v_stack_m40, 0, v_stack_m48);
    goto loc_003C51BD;
loc_003C5777:
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 232) = 0;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 520) + 8)) != (*(unsigned __int64 *)(gs_base + (0 + 392)) + 520)) goto loc_003C52DD;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 520 + 8))) != (*(unsigned __int64 *)(gs_base + (0 + 392)) + 520)) goto loc_003C52DD;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 520 + 8)) = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 520);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 520) + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 520 + 8);
    goto loc_003C5687;
loc_003C57AB:
    goto loc_003C56BB;
loc_003C57CE:
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 114) = (unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 232));
    goto loc_003C5645;
loc_003C57D6:
    goto loc_003C55F2;
loc_003C57E1:
    a3 = 0;
    result = KiProcessThreadWaitList((unsigned int)(v_stack_m58), a3 + 1, a3, 0);
    goto loc_003C5614;
}
```

## 5. (Beta) C Style

```c
int64_t KeRemovePriQueue(int64_t Arg1, uint8_t Arg2, int32_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint32_t v_stack_m50;
    uint64_t v_stack_m54;
    uint32_t v_stack_m58;
    uint64_t v_stack_m60;
    uint32_t v_stack_m68;
    uint8_t v_stack_p10;
    uint8_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x20) = local_rbx;
    *(uint8_t *)(local_rsp + 0x18) = (uint8_t)(Arg3);
    *(uint8_t *)(local_rsp + 0x10) = Arg2;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (80);
    local_r15 = 0;
    *(uint64_t *)(local_rsp - 0x68) = v_stack_m54;
    v_stack_m48 = 0;
    v_stack_m58 = 0;
    v_stack_m54 = 0;
    Arg3 = 0;
    result = KiCheckWaitNext(*(uint64_t *)(gs_base + (0 + 0x188)), Arg4, Arg3, v_stack_m48);
    v_stack_m50 = (uint32_t)(result);
loc_003C50E9:
    v_stack_m40 = 0;
loc_003C5102:
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x70) = 0;
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x187) = (uint8_t)(v_stack_p10);
    if ((uint8_t)(v_stack_p18) != 0) {
    }
loc_003C511D:
    if (condition_is_above_or_equal) goto loc_003C5141;
loc_003C5126:
    local_rsi = (uint32_t)((0) + 1);
    if (((*(uint32_t *)(v_rip + 0xC0017E)) & ((uint32_t)(local_rsi))) == 0) goto loc_003C5391;
loc_003C5134:
loc_003C5136:
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x40) == 0) goto loc_003C511D;
    goto loc_003C5126;
loc_003C5141:
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xC1)) != 0) goto loc_003C548F;
loc_003C514E:
    if ((uint8_t)(v_stack_p18) != 0) goto loc_003C52E4;
    if (((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xC2)) & (2)) == 0) goto loc_003C51E1;
    Arg1 = 0;
    if (v_stack_p10 == 0) goto loc_003C51E1;
loc_003C5180:
    v_stack_m40 = 0;
    result = KiPerformWaitDeferredWork(*(uint64_t *)(gs_base + (0 + 0x188)), (uint32_t)((uint32_t)((uint32_t)(v_stack_m50))), 1, v_stack_m40);
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x40) = 0;
    if ((uint32_t)(result) != 0) goto loc_003C575D;
    if ((*(uint32_t *)(v_rip + 0xC01B75)) != ((uint32_t)(result))) {
        Arg1 = v_cr8;
        Arg2 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186));
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, 1, v_stack_m40);
    }
loc_003C51BD:
    local_r14 = 0;
    if (192 == 0) goto loc_003C5208;
    goto loc_003C542B;
loc_003C51CA:
loc_003C51D7:
loc_003C51DD:
    if (192 != 0) goto loc_003C5180;
loc_003C51E1:
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x184) = 5;
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x283) = 15;
    local_r14 = 0;
    *(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x1B4) = (uint32_t)((uint32_t)(*(uint32_t *)(192)));
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x40) = 0;
loc_003C5208:
    if (v_stack_p8 != (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xE8))) goto loc_003C56CE;
loc_003C5218:
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x140 + 0x10) = 3;
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x140 + 0x11) = 4;
    *(uint16_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x140 + 0x12) = 128;
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x140 + 0x20) = v_stack_p8;
    result = KiAcquireKobjectLockSafe(v_stack_p8, Arg2, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xE8), v_stack_m40);
    if ((*(uint32_t *)(v_stack_p8 + 0x4)) != 0) goto loc_003C54DE;
loc_003C523F:
    if (((*(uint8_t *)(v_stack_p8 + 0x1)) & (1)) != 0) goto loc_003C5650;
    if (((uint32_t)((uint32_t)(v_stack_m54))) == 2) goto loc_003C531C;
    if ((uint32_t)((uint32_t)(v_stack_m54)) == 0) goto loc_003C5283;
    if (v_stack_m48 == 0) goto loc_003C57D6;
loc_003C527A:
    if ((*(uint64_t *)((uint32_t)(v_stack_m54))) > v_stack_m48) goto loc_003C57D6;
loc_003C5283:
loc_003C5286:
    if ((*(uint64_t *)((uint32_t)(v_stack_m54))) >= v_stack_m48) goto loc_003C52AA;
loc_003C528F:
    local_rsi = (uint32_t)((0) + 1);
    if (((*(uint32_t *)(v_rip + 0xC00015)) & ((uint32_t)(local_rsi))) == 0) goto loc_003C53B8;
loc_003C529D:
loc_003C529F:
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x40) == 0) goto loc_003C5286;
    goto loc_003C528F;
loc_003C52AA:
    *(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x21C) = (uint32_t)((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x21C))));
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x40) = 0;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0x8) + 0x8)) == (v_stack_p8 + 8)) goto loc_003C53DF;
loc_003C52DD:
loc_003C52E4:
    Arg1 = 0;
    if ((*(uint8_t *)((int8_t)(v_stack_p10) + *(uint64_t *)(gs_base + (0 + 0x188)) * 1 + 0x72)) != 0) goto loc_003C5641;
    if ((uint8_t)((int8_t)(v_stack_p10)) == 0) goto loc_003C5309;
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xA8)) != (*(uint64_t *)(gs_base + (0 + 0x188)) + 168)) goto loc_003C51CA;
loc_003C5309:
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x72)) != 0) goto loc_003C57CE;
    goto loc_003C51DD;
loc_003C531C:
    Arg1 = (*(uint64_t *)(Arg1)) - (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xF8));
    Arg1 = (Arg1) - (*(uint64_t *)(0));
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x187)) == 0) goto loc_003C527A;
    if ((*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x1E4)) != 0) goto loc_003C527A;
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186)) != 0) goto loc_003C527A;
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xC0)) != 0) goto loc_003C527A;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x3B8))) == 0) goto loc_003C527A;
    result = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x3B8))))) + (v_stack_m48);
    goto loc_003C527A;
loc_003C5391:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC01721)))) & (64)) == 0) goto loc_003C5134;
    result = KiCheckVpBackingLongSpinWaitHypercall(Arg1, (uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x3B8)), 2, v_stack_m40);
    if ((uint8_t)(result) == 0) goto loc_003C5134;
    result = HvlNotifyLongSpinWait(0, (uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x3B8)), 2, v_stack_m40);
    goto loc_003C5136;
loc_003C53B8:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC016FA)))) & (64)) == 0) goto loc_003C529D;
    result = KiCheckVpBackingLongSpinWaitHypercall(0, (uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x3B8)), 2, v_stack_m40);
    if ((uint8_t)(result) == 0) goto loc_003C529D;
    result = HvlNotifyLongSpinWait(0, (uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x3B8)), 2, v_stack_m40);
    goto loc_003C529F;
loc_003C53DF:
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x140) = 0;
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x140 + 0x8) = result;
    *(uint64_t *)(0 + 0x8) = *(uint64_t *)(gs_base + (0 + 0x188)) + 320;
    *(uint64_t *)(result) = *(uint64_t *)(gs_base + (0 + 0x188)) + 320;
    v_stack_m60 = 0;
    v_stack_m68 = (uint32_t)((uint32_t)(v_stack_m50));
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x24B) = 1;
    result = KiCommitThreadWait(*(uint64_t *)(gs_base + (0 + 0x188)), *(uint64_t *)(gs_base + (0 + 0x188)) + 320, (uint32_t)(v_stack_m54), v_stack_m48);
    v_stack_m50 = 0;
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x283) = 0;
    if (result == 256) goto loc_003C545E;
loc_003C542B:
    if (((*(uint32_t *)(v_rip + 0xC016CF)) & (0x1000000ULL)) != 0) {
        Arg2 = result;
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x188));
        result = EtwTracePriQDequeueWork(Arg1, Arg2, (uint32_t)(v_stack_m54), v_stack_m48);
    }
loc_003C5445:
    local_rsp = (local_rsp) + (80);
    return result;
loc_003C545E:
    if ((*(uint32_t *)(v_rip + 0xC018AE)) != 0) goto loc_003C5483;
loc_003C5474:
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186));
    local_r15 = 0;
    goto loc_003C50E9;
loc_003C5483:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186)), 2, (uint32_t)(v_stack_m54), v_stack_m48);
    goto loc_003C5474;
loc_003C548F:
    if ((*(uint16_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x1E6)) != 0) goto loc_003C514E;
    if (0 >= 1) goto loc_003C514E;
    result = KiReleaseThreadLockLowerIrql(*(uint64_t *)(gs_base + (0 + 0x188)), 1, (uint32_t)(v_stack_m54), v_stack_m48);
    Arg3 = 0;
    Arg2 = 0;
    Arg1 = 0;
    result = KiDeliverApc(Arg1, Arg2, Arg3, v_stack_m48);
    if ((*(uint32_t *)(v_rip + 0xC01854)) != 0) goto loc_003C56A2;
loc_003C54D2:
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) = 0;
    goto loc_003C5102;
loc_003C54DE:
loc_003C54E1:
    if ((*(uint32_t *)(v_rip + 0xC01854)) >= 0) goto loc_003C5505;
loc_003C54EA:
    local_rsi = (uint32_t)((0) + 1);
    if (((*(uint32_t *)(v_rip + 0xBFFDBA)) & ((uint32_t)(local_rsi))) == 0) goto loc_003C56E7;
loc_003C54F8:
loc_003C54FA:
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x40) == 0) goto loc_003C54E1;
    goto loc_003C54EA;
loc_003C5505:
    result = KiAttemptFastRemovePriQueue(0, v_stack_m58, (uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x21C))), v_stack_m48);
    if (result == 0) goto loc_003C5696;
    if (((uint32_t)((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x21C))))) != ((uint32_t)((uint32_t)(v_stack_m58)))) goto loc_003C56AE;
loc_003C553D:
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x285) = 0;
    result = KiSetBasePriorityAndClearDecrement(*(uint64_t *)(gs_base + (0 + 0x188)), v_stack_m58, (uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x21C)), v_stack_m48);
    result = KiAdjustRealtimePriorityFloor(*(uint64_t *)(gs_base + (0 + 0x188)), (uint32_t)((uint32_t)((uint32_t)(v_stack_m58))), (uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x21C)), v_stack_m48);
    Arg3 = 0;
    Arg2 = 0;
    result = KiComputeThreadPriority(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, Arg3, v_stack_m48);
    v_stack_m58 = (uint32_t)(result);
    if (((uint32_t)(result)) == ((uint32_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xC3))))) goto loc_003C55E4;
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x20)) != 0) goto loc_003C56DE;
    Arg3 = 0;
    result = KiUpdateTotalCyclesCurrentThread(*(uint64_t *)(gs_base + (0 + 0x20)), *(uint64_t *)(gs_base + (0 + 0x188)), Arg3, v_stack_m48);
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) != 0) goto loc_003C570E;
loc_003C55B0:
loc_003C55B1:
    result = KiQueryQuantumReset(*(uint64_t *)(gs_base + (0 + 0x188)), *(uint64_t *)(gs_base + (0 + 0x188)), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), v_stack_m48);
    result = (uint32_t)((result) * (*(uint32_t *)(v_rip + 0xBFFAD8)));
    Arg1 = ((uint32_t)((uint32_t)(result))) + (result);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x78)))) & (32)) != 0) {
    }
    Arg2 = 0;
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x20) = Arg1;
    result = KiSetPriorityThread(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, (uint32_t)(v_stack_m58), v_stack_m48);
loc_003C55E4:
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x40) = 0;
loc_003C55EC:
loc_003C55F2:
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x283) = 0;
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x2D08)) != 0) goto loc_003C57E1;
loc_003C5614:
    result = KiFastExitThreadWait(*(uint64_t *)(gs_base + (0 + 0x20)), *(uint64_t *)(gs_base + (0 + 0x188)), (uint32_t)((uint32_t)(v_stack_p20)), v_stack_m48);
    if (((*(uint32_t *)(v_rip + 0xC014D8)) & (0x1000000ULL)) != 0) {
        Arg2 = result;
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x188));
        result = EtwTracePriQDequeueWork(Arg1, Arg2, (uint32_t)((uint32_t)(v_stack_p20)), v_stack_m48);
    }
    goto loc_003C5445;
loc_003C5641:
    *(uint8_t *)(Arg2 + *(uint64_t *)(gs_base + (0 + 0x188)) * 1 + 0x72) = (uint8_t)(Arg1);
loc_003C5645:
    goto loc_003C51D7;
loc_003C5650:
loc_003C5653:
    if (condition_is_above_or_equal) goto loc_003C5677;
loc_003C565C:
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(result))) + 1);
    if (((*(uint32_t *)(v_rip + 0xBFFC48)) & ((uint32_t)(local_rsi))) == 0) goto loc_003C5736;
loc_003C566A:
loc_003C566C:
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x40) == 0) goto loc_003C5653;
    goto loc_003C565C;
loc_003C5677:
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xE8)) == 0) goto loc_003C5777;
loc_003C5687:
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x40) = result;
    goto loc_003C55EC;
loc_003C5696:
    local_r14 = 0;
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x40) = 0;
    goto loc_003C523F;
loc_003C56A2:
    result = KiRaiseIrqlProcessIrqlFlags(Arg1, (uint8_t)(v_stack_p20), 257, v_stack_m48);
    goto loc_003C54D2;
loc_003C56AE:
    Arg3 = (uint32_t)((257) & (256));
    if (condition_is_equal) goto loc_003C57AB;
loc_003C56BB:
    Arg3 = (uint32_t)((Arg3) | ((uint32_t)((uint8_t)(local_rsi))));
    *(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x21C) = Arg3;
    goto loc_003C553D;
loc_003C56CE:
    result = KiSwitchPriQueue(*(uint64_t *)(gs_base + (0 + 0x188)), 0, Arg3, v_stack_m48);
    goto loc_003C5218;
loc_003C56DE:
    goto loc_003C55B1;
loc_003C56E7:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC013CB)))) & (64)) == 0) goto loc_003C54F8;
    result = KiCheckVpBackingLongSpinWaitHypercall(*(uint64_t *)(gs_base + (0 + 0x188)), 0, Arg3, v_stack_m48);
    if ((uint8_t)(result) == 0) goto loc_003C54F8;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x48))), 0, Arg3, v_stack_m48);
    goto loc_003C54FA;
loc_003C570E:
loc_003C5715:
    if ((uint8_t)(result) != 0) goto loc_003C5715;
    if (condition_is_above_or_equal) goto loc_003C55B0;
    result = KiRemoveSystemWorkPriorityKick((uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x48))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg3)))), Arg3, v_stack_m48);
    goto loc_003C55B0;
loc_003C5736:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC0137C)))) & (64)) == 0) goto loc_003C566A;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x48))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg3)))), Arg3, v_stack_m48);
    if ((uint8_t)(result) == 0) goto loc_003C566A;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x48))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg3)))), Arg3, v_stack_m48);
    goto loc_003C566C;
loc_003C575D:
    result = KiProcessDeferredReadyList(*(uint64_t *)(gs_base + (0 + 0x20)), v_stack_m40, 0, v_stack_m48);
    goto loc_003C51BD;
loc_003C5777:
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xE8) = 0;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x208) + 0x8)) != (*(uint64_t *)(gs_base + (0 + 0x188)) + 520)) goto loc_003C52DD;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x208 + 0x8))) != (*(uint64_t *)(gs_base + (0 + 0x188)) + 520)) goto loc_003C52DD;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x208 + 0x8)) = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x208);
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x208) + 0x8) = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x208 + 0x8);
    goto loc_003C5687;
loc_003C57AB:
    goto loc_003C56BB;
loc_003C57CE:
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x72) = (uint8_t)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xE8));
    goto loc_003C5645;
loc_003C57D6:
    goto loc_003C55F2;
loc_003C57E1:
    Arg3 = 0;
    result = KiProcessThreadWaitList((uint32_t)(v_stack_m58), Arg3 + 1, Arg3, 0);
    goto loc_003C5614;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003C5090&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
