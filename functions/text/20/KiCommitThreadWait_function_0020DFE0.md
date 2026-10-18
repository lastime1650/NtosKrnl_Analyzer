# KiCommitThreadWait

- RVA: `0x0020DFE0`–`0x0020E554` (길이 `1,396` bytes)
- VA: `0x000000014020DFE0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0005DA9C`
- 디코드: `330`개 명령, `1,396/1,396` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **19**; 고유 호출 대상: **17**
- 직접 호출자로 확인된 함수: **8**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x0020E042` → [KiIsKernelStackSwappable](../41/KiIsKernelStackSwappable_function_00415A80.md) (function, `0x00415A80`)
- `0x0020E0A2` → [KiPerformWaitDeferredWork](../22/KiPerformWaitDeferredWork_function_00220480.md) (function, `0x00220480`)
- `0x0020E1D2` → [KiInsertTimerTable](../23/KiInsertTimerTable_function_00233400.md) (function, `0x00233400`)
- `0x0020E200` → [KiSwapThread](../35/KiSwapThread_function_00355640.md) (function, `0x00355640`)
- `0x0020E2BE` → [KiExitThreadWait](../22/KiExitThreadWait_function_00220200.md) (function, `0x00220200`)
- `0x0020E2CF` → [KiAcquireKobjectLockSafe](../25/KiAcquireKobjectLockSafe_function_00251C90.md) (function, `0x00251C90`)
- `0x0020E2F9` → [KiInsertPrcbWaitEntry](../40/KiInsertPrcbWaitEntry_function_004015D0.md) (function, `0x004015D0`)
- `0x0020E322` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0020E332` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0020E343` → [PsTimerResolutionActive](../3A/PsTimerResolutionActive_function_003A3010.md) (function, `0x003A3010`)
- `0x0020E36B` → [KiActivateWaiterQueueWithThreadLock](../3C/KiActivateWaiterQueueWithThreadLock_function_003C6690.md) (function, `0x003C6690`)
- `0x0020E37E` → [KiTimerWaitTest](../23/KiTimerWaitTest_function_002337D0.md) (function, `0x002337D0`)
- `0x0020E44C` → [KiTraceSetTimer](../22/KiTraceSetTimer_function_0022FB08.md) (function, `0x0022FB08`)
- `0x0020E45D` → [KiDecrementProcessStackCount](../2A/KiDecrementProcessStackCount_function_002A1620.md) (function, `0x002A1620`)
- `0x0020E47A` → [KiIncrementConcurrencyCount](../41/KiIncrementConcurrencyCount_function_0041D820.md) (function, `0x0041D820`)
- `0x0020E492` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0020E4A1` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0020E4C3` → [KiComputeDueTime](../23/KiComputeDueTime_function_002332E8.md) (function, `0x002332E8`)
- `0x0020E54A` → [KiProcessThreadWaitList](../25/KiProcessThreadWaitList_function_00252CC0.md) (function, `0x00252CC0`)

### Direct callers
- [sub_002098FF](Unknown_function_002098FF.md) at `0x00209997`
- [sub_0020C2D4](Unknown_function_0020C2D4.md) at `0x0020C5C1`
- [sub_0020D5AD](Unknown_function_0020D5AD.md) at `0x0020D733`
- [KeWaitForSingleObject](KeWaitForSingleObject_function_0020E6B0.md) at `0x0020EEF1`
- [KeWaitForGate](../2C/KeWaitForGate_function_002CA794.md) at `0x002CA87D`
- [KeWaitForAlertByThreadId](../3C/KeWaitForAlertByThreadId_function_003C4B14.md) at `0x003C4CCB`
- [KeRemovePriQueue](../3C/KeRemovePriQueue_function_003C5090.md) at `0x003C5410`
- [KiWaitForAllObjects](../3C/KiWaitForAllObjects_function_003C5800.md) at `0x003C5DF2`

### Static image references
- `0x0020E05D` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x0020E1A4` → RVA `0x00FC6C48` (`ALMOSTRO`; read)
- `0x0020E1DF` → RVA `0x00FC6B08` (`ALMOSTRO`; read)
- `0x0020E314` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x0020E510` → [sub_006D671C](../6D/Unknown_function_006D671C.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0020DFE0  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
0020DFE5  55                              push rbp
0020DFE6  53                              push rbx
0020DFE7  56                              push rsi
0020DFE8  57                              push rdi
0020DFE9  41 54                           push r12
0020DFEB  41 55                           push r13
0020DFED  41 56                           push r14
0020DFEF  41 57                           push r15
0020DFF1  48 8B EC                        mov rbp, rsp
0020DFF4  48 83 EC 58                     sub rsp, 0x58
0020DFF8  33 C0                           xor eax, eax
0020DFFA  0F 57 C0                        xorps xmm0, xmm0
0020DFFD  21 45 48                        and dword ptr [rbp + 0x48], eax
0020E000  45 8B E0                        mov r12d, r8d
0020E003  45 33 FF                        xor r15d, r15d
0020E006  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
0020E00A  48 8B F2                        mov rsi, rdx
0020E00D  48 8B D9                        mov rbx, rcx
0020E010  0F 11 45 D8                     movups xmmword ptr [rbp - 0x28], xmm0
0020E014  0F 0D 49 70                     prefetchw byte ptr [rcx + 0x70]
0020E018  45 85 C0                        test r8d, r8d
0020E01B  0F 85 FC 01 00 00               jne 0x14020e21d
0020E021  F7 41 78 00 00 40 00            test dword ptr [rcx + 0x78], 0x400000
0020E028  0F 85 6D 03 00 00               jne 0x14020e39b
0020E02E  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
0020E037  48 89 45 50                     mov qword ptr [rbp + 0x50], rax
0020E03B  48 89 B1 D0 00 00 00            mov qword ptr [rcx + 0xd0], rsi
0020E042  E8 39 7A 20 00                  call 0x140415a80
0020E047  45 33 F6                        xor r14d, r14d
0020E04A  44 8B E8                        mov r13d, eax
0020E04D  41 8D 7E 01                     lea edi, [r14 + 1]
0020E051  F0 48 0F BA 6B 40 00            lock bts qword ptr [rbx + 0x40], 0
0020E058  73 1D                           jae 0x14020e077
0020E05A  44 03 F7                        add r14d, edi
0020E05D  44 85 35 48 72 DB 00            test dword ptr [rip + 0xdb7248], r14d
0020E064  0F 84 AA 02 00 00               je 0x14020e314
0020E06A  F3 90                           pause
0020E06C  48 8B 43 40                     mov rax, qword ptr [rbx + 0x40]
0020E070  48 85 C0                        test rax, rax
0020E073  74 DC                           je 0x14020e051
0020E075  EB E3                           jmp 0x14020e05a
0020E077  8A 43 70                        mov al, byte ptr [rbx + 0x70]
0020E07A  48 8D BB 00 01 00 00            lea rdi, [rbx + 0x100]
0020E081  A8 E7                           test al, 0xe7
0020E083  0F 85 A8 01 00 00               jne 0x14020e231
0020E089  8B 55 68                        mov edx, dword ptr [rbp + 0x68]
0020E08C  24 F9                           and al, 0xf9
0020E08E  BE 01 00 00 00                  mov esi, 1
0020E093  45 33 C9                        xor r9d, r9d
0020E096  40 0A C6                        or al, sil
0020E099  44 8A C6                        mov r8b, sil
0020E09C  48 8B CB                        mov rcx, rbx
0020E09F  88 43 70                        mov byte ptr [rbx + 0x70], al
0020E0A2  E8 D9 23 01 00                  call 0x140220480
0020E0A7  4C 8B 75 50                     mov r14, qword ptr [rbp + 0x50]
0020E0AB  45 85 ED                        test r13d, r13d
0020E0AE  0F 85 3F 02 00 00               jne 0x14020e2f3
0020E0B4  F7 43 78 00 10 00 00            test dword ptr [rbx + 0x78], 0x1000
0020E0BB  0F 85 EA 03 00 00               jne 0x14020e4ab
0020E0C1  0F BA 63 74 13                  bt dword ptr [rbx + 0x74], 0x13
0020E0C6  0F 92 C1                        setb cl
0020E0C9  0F BA 63 78 0E                  bt dword ptr [rbx + 0x78], 0xe
0020E0CE  0F 92 C0                        setb al
0020E0D1  84 C8                           test al, cl
0020E0D3  0F 85 2D 03 00 00               jne 0x14020e406
0020E0D9  40 32 F6                        xor sil, sil
0020E0DC  41 83 FC 02                     cmp r12d, 2
0020E0E0  75 3C                           jne 0x14020e11e
0020E0E2  8B 83 B8 03 00 00               mov eax, dword ptr [rbx + 0x3b8]
0020E0E8  40 38 B3 87 01 00 00            cmp byte ptr [rbx + 0x187], sil
0020E0EF  74 2D                           je 0x14020e11e
0020E0F1  83 BB E4 01 00 00 00            cmp dword ptr [rbx + 0x1e4], 0
0020E0F8  75 24                           jne 0x14020e11e
0020E0FA  40 38 B3 86 01 00 00            cmp byte ptr [rbx + 0x186], sil
0020E101  75 1B                           jne 0x14020e11e
0020E103  4C 8B 6D 60                     mov r13, qword ptr [rbp + 0x60]
0020E107  40 38 B3 C0 00 00 00            cmp byte ptr [rbx + 0xc0], sil
0020E10E  75 12                           jne 0x14020e122
0020E110  41 8D 74 24 FF                  lea esi, [r12 - 1]
0020E115  85 C0                           test eax, eax
0020E117  74 09                           je 0x14020e122
0020E119  4C 03 E8                        add r13, rax
0020E11C  EB 04                           jmp 0x14020e122
0020E11E  4C 8B 6D 60                     mov r13, qword ptr [rbp + 0x60]
0020E122  80 BB 83 02 00 00 0F            cmp byte ptr [rbx + 0x283], 0xf
0020E129  0F 85 29 02 00 00               jne 0x14020e358
0020E12F  48 C7 43 40 00 00 00 00         mov qword ptr [rbx + 0x40], 0
0020E137  45 85 FF                        test r15d, r15d
0020E13A  0F 85 16 03 00 00               jne 0x14020e456
0020E140  C6 83 35 02 00 00 00            mov byte ptr [rbx + 0x235], 0
0020E147  45 85 E4                        test r12d, r12d
0020E14A  0F 84 A6 00 00 00               je 0x14020e1f6
0020E150  41 83 FC 02                     cmp r12d, 2
0020E154  0F 85 5C 03 00 00               jne 0x14020e4b6
0020E15A  48 B8 B0 03 00 00 80 F7 FF FF   movabs rax, 0xfffff780000003b0
0020E164  48 8B 00                        mov rax, qword ptr [rax]
0020E167  48 8B 8B F8 00 00 00            mov rcx, qword ptr [rbx + 0xf8]
0020E16E  48 03 C8                        add rcx, rax
0020E171  49 03 CD                        add rcx, r13
0020E174  48 89 4F 18                     mov qword ptr [rdi + 0x18], rcx
0020E178  48 C1 E9 12                     shr rcx, 0x12
0020E17C  0F B6 C1                        movzx eax, cl
0020E17F  89 45 48                        mov dword ptr [rbp + 0x48], eax
0020E182  8B 07                           mov eax, dword ptr [rdi]
0020E184  89 45 D8                        mov dword ptr [rbp - 0x28], eax
0020E187  8A 45 48                        mov al, byte ptr [rbp + 0x48]
0020E18A  80 65 D9 FE                     and byte ptr [rbp - 0x27], 0xfe
0020E18E  88 45 DA                        mov byte ptr [rbp - 0x26], al
0020E191  40 84 F6                        test sil, sil
0020E194  8B 45 D8                        mov eax, dword ptr [rbp - 0x28]
0020E197  41 8D 74 24 FF                  lea esi, [r12 - 1]
0020E19C  89 07                           mov dword ptr [rdi], eax
0020E19E  0F 85 E4 01 00 00               jne 0x14020e388
0020E1A4  83 3D 9D 8A DB 00 00            cmp dword ptr [rip + 0xdb8a9d], 0
0020E1AB  0F 84 8B 01 00 00               je 0x14020e33c
0020E1B1  33 D2                           xor edx, edx
0020E1B3  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
0020E1B9  B8 3A 00 00 00                  mov eax, 0x3a
0020E1BE  48 8B CF                        mov rcx, rdi
0020E1C1  45 33 C0                        xor r8d, r8d
0020E1C4  66 89 14 08                     mov word ptr [rax + rcx], dx
0020E1C8  48 8B D7                        mov rdx, rdi
0020E1CB  44 8B 4D 48                     mov r9d, dword ptr [rbp + 0x48]
0020E1CF  49 8B CE                        mov rcx, r14
0020E1D2  E8 29 52 02 00                  call 0x140233400
0020E1D7  84 C0                           test al, al
0020E1D9  0F 84 96 01 00 00               je 0x14020e375
0020E1DF  F7 05 1F 89 DB 00 00 00 02 00   test dword ptr [rip + 0xdb891f], 0x20000
0020E1E9  0F 85 55 02 00 00               jne 0x14020e444
0020E1EF  F0 81 27 7F FF FF FF            lock and dword ptr [rdi], 0xffffff7f
0020E1F6  4C 8B 45 70                     mov r8, qword ptr [rbp + 0x70]
0020E1FA  49 8B D6                        mov rdx, r14
0020E1FD  48 8B CB                        mov rcx, rbx
0020E200  E8 3B 74 14 00                  call 0x140355640
0020E205  4C 8B F8                        mov r15, rax
0020E208  49 8B C7                        mov rax, r15
0020E20B  48 83 C4 58                     add rsp, 0x58
0020E20F  41 5F                           pop r15
0020E211  41 5E                           pop r14
0020E213  41 5D                           pop r13
0020E215  41 5C                           pop r12
0020E217  5F                              pop rdi
0020E218  5E                              pop rsi
0020E219  5B                              pop rbx
0020E21A  5D                              pop rbp
0020E21B  C3                              ret
0020E21C  CC                              int3
0020E21D  0F BA 69 74 09                  bts dword ptr [rcx + 0x74], 9
0020E222  81 89 00 01 00 00 80 00 00 40   or dword ptr [rcx + 0x100], 0x40000080
0020E22C  E9 F0 FD FF FF                  jmp 0x14020e021
0020E231  41 BD 01 01 00 00               mov r13d, 0x101
0020E237  A8 07                           test al, 7
0020E239  0F 84 D6 01 00 00               je 0x14020e415
0020E23F  45 8A C7                        mov r8b, r15b
0020E242  C6 83 84 01 00 00 02            mov byte ptr [rbx + 0x184], 2
0020E249  80 BB 83 02 00 00 0F            cmp byte ptr [rbx + 0x283], 0xf
0020E250  0F 84 11 02 00 00               je 0x14020e467
0020E256  4C 89 7B 40                     mov qword ptr [rbx + 0x40], r15
0020E25A  45 85 E4                        test r12d, r12d
0020E25D  0F 85 8E 02 00 00               jne 0x14020e4f1
0020E263  48 8B 4D 70                     mov rcx, qword ptr [rbp + 0x70]
0020E267  4C 8B BB C8 00 00 00            mov r15, qword ptr [rbx + 0xc8]
0020E26E  48 85 C9                        test rcx, rcx
0020E271  0F 85 84 02 00 00               jne 0x14020e4fb
0020E277  45 84 C0                        test r8b, r8b
0020E27A  0F 85 26 01 00 00               jne 0x14020e3a6
0020E280  0F B6 83 4B 02 00 00            movzx eax, byte ptr [rbx + 0x24b]
0020E287  48 8D 3C 40                     lea rdi, [rax + rax*2]
0020E28B  48 C1 E7 04                     shl rdi, 4
0020E28F  48 03 FE                        add rdi, rsi
0020E292  8A 46 11                        mov al, byte ptr [rsi + 0x11]
0020E295  3C 05                           cmp al, 5
0020E297  72 2F                           jb 0x14020e2c8
0020E299  48 83 C6 30                     add rsi, 0x30
0020E29D  48 3B F7                        cmp rsi, rdi
0020E2A0  75 F0                           jne 0x14020e292
0020E2A2  48 8B 7D 50                     mov rdi, qword ptr [rbp + 0x50]
0020E2A6  48 83 BF 08 2D 00 00 00         cmp qword ptr [rdi + 0x2d08], 0
0020E2AE  0F 85 89 02 00 00               jne 0x14020e53d
0020E2B4  44 8B 45 68                     mov r8d, dword ptr [rbp + 0x68]
0020E2B8  48 8B D3                        mov rdx, rbx
0020E2BB  48 8B CF                        mov rcx, rdi
0020E2BE  E8 3D 1F 01 00                  call 0x140220200
0020E2C3  E9 40 FF FF FF                  jmp 0x14020e208
0020E2C8  4C 8B 76 20                     mov r14, qword ptr [rsi + 0x20]
0020E2CC  49 8B CE                        mov rcx, r14
0020E2CF  E8 BC 39 04 00                  call 0x140251c90
0020E2D4  80 7E 11 04                     cmp byte ptr [rsi + 0x11], 4
0020E2D8  75 30                           jne 0x14020e30a
0020E2DA  48 8B 0E                        mov rcx, qword ptr [rsi]
0020E2DD  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
0020E2E1  48 39 71 08                     cmp qword ptr [rcx + 8], rsi
0020E2E5  75 05                           jne 0x14020e2ec
0020E2E7  48 39 30                        cmp qword ptr [rax], rsi
0020E2EA  74 17                           je 0x14020e303
0020E2EC  B9 03 00 00 00                  mov ecx, 3
0020E2F1  CD 29                           int 0x29
0020E2F3  49 8B D6                        mov rdx, r14
0020E2F6  48 8B CB                        mov rcx, rbx
0020E2F9  E8 D2 32 1F 00                  call 0x1404015d0
0020E2FE  E9 B1 FD FF FF                  jmp 0x14020e0b4
0020E303  48 89 08                        mov qword ptr [rax], rcx
0020E306  48 89 41 08                     mov qword ptr [rcx + 8], rax
0020E30A  F0 41 81 26 7F FF FF FF         lock and dword ptr [r14], 0xffffff7f
0020E312  EB 85                           jmp 0x14020e299
0020E314  8B 05 9E 87 DB 00               mov eax, dword ptr [rip + 0xdb879e]
0020E31A  A8 40                           test al, 0x40
0020E31C  0F 84 48 FD FF FF               je 0x14020e06a
0020E322  E8 69 11 10 00                  call 0x14030f490
0020E327  84 C0                           test al, al
0020E329  0F 84 3B FD FF FF               je 0x14020e06a
0020E32F  41 8B CE                        mov ecx, r14d
0020E332  E8 29 11 10 00                  call 0x14030f460
0020E337  E9 30 FD FF FF                  jmp 0x14020e06c
0020E33C  48 8B 8B 20 02 00 00            mov rcx, qword ptr [rbx + 0x220]
0020E343  E8 C8 4C 19 00                  call 0x1403a3010
0020E348  84 C0                           test al, al
0020E34A  0F 85 61 FE FF FF               jne 0x14020e1b1
0020E350  0F B7 D6                        movzx edx, si
0020E353  E9 5B FE FF FF                  jmp 0x14020e1b3
0020E358  48 8B 93 E8 00 00 00            mov rdx, qword ptr [rbx + 0xe8]
0020E35F  48 85 D2                        test rdx, rdx
0020E362  0F 84 C7 FD FF FF               je 0x14020e12f
0020E368  48 8B CB                        mov rcx, rbx
0020E36B  E8 20 83 1B 00                  call 0x1403c6690
0020E370  E9 C2 FD FF FF                  jmp 0x14020e137
0020E375  45 33 C0                        xor r8d, r8d
0020E378  48 8B D7                        mov rdx, rdi
0020E37B  49 8B CE                        mov rcx, r14
0020E37E  E8 4D 54 02 00                  call 0x1402337d0
0020E383  E9 6E FE FF FF                  jmp 0x14020e1f6
0020E388  48 8B 83 20 02 00 00            mov rax, qword ptr [rbx + 0x220]
0020E38F  F0 01 B0 00 07 00 00            lock add dword ptr [rax + 0x700], esi
0020E396  E9 09 FE FF FF                  jmp 0x14020e1a4
0020E39B  21 81 88 04 00 00               and dword ptr [rcx + 0x488], eax
0020E3A1  E9 88 FC FF FF                  jmp 0x14020e02e
0020E3A6  4C 0F BE B3 87 01 00 00         movsx r14, byte ptr [rbx + 0x187]
0020E3AE  33 FF                           xor edi, edi
0020E3B0  44 8D 6F 01                     lea r13d, [rdi + 1]
0020E3B4  F0 48 0F BA 6B 40 00            lock bts qword ptr [rbx + 0x40], 0
0020E3BB  73 1C                           jae 0x14020e3d9
0020E3BD  41 03 FD                        add edi, r13d
0020E3C0  85 3D E6 6E DB 00               test dword ptr [rip + 0xdb6ee6], edi
0020E3C6  0F 84 B8 00 00 00               je 0x14020e484
0020E3CC  F3 90                           pause
0020E3CE  48 8B 43 40                     mov rax, qword ptr [rbx + 0x40]
0020E3D2  48 85 C0                        test rax, rax
0020E3D5  74 DD                           je 0x14020e3b4
0020E3D7  EB E4                           jmp 0x14020e3bd
0020E3D9  41 BD 01 01 00 00               mov r13d, 0x101
0020E3DF  4D 3B FD                        cmp r15, r13
0020E3E2  0F 85 39 01 00 00               jne 0x14020e521
0020E3E8  8B 43 74                        mov eax, dword ptr [rbx + 0x74]
0020E3EB  A8 10                           test al, 0x10
0020E3ED  0F 85 17 01 00 00               jne 0x14020e50a
0020E3F3  F0 0F BA 73 78 04               lock btr dword ptr [rbx + 0x78], 4
0020E3F9  48 C7 43 40 00 00 00 00         mov qword ptr [rbx + 0x40], 0
0020E401  E9 7A FE FF FF                  jmp 0x14020e280
0020E406  F0 0F BA 6B 78 14               lock bts dword ptr [rbx + 0x78], 0x14
0020E40C  44 0F 43 FE                     cmovae r15d, esi
0020E410  E9 C4 FC FF FF                  jmp 0x14020e0d9
0020E415  A8 20                           test al, 0x20
0020E417  0F 85 BD 00 00 00               jne 0x14020e4da
0020E41D  24 40                           and al, 0x40
0020E41F  41 B8 01 00 00 00               mov r8d, 1
0020E425  F6 D8                           neg al
0020E427  48 1B C0                        sbb rax, rax
0020E42A  48 83 E0 BF                     and rax, 0xffffffffffffffbf
0020E42E  49 03 C5                        add rax, r13
0020E431  48 89 83 C8 00 00 00            mov qword ptr [rbx + 0xc8], rax
0020E438  4C 89 BB D0 03 00 00            mov qword ptr [rbx + 0x3d0], r15
0020E43F  E9 FE FD FF FF                  jmp 0x14020e242
0020E444  44 8A C6                        mov r8b, sil
0020E447  33 D2                           xor edx, edx
0020E449  48 8B CF                        mov rcx, rdi
0020E44C  E8 B7 16 02 00                  call 0x14022fb08
0020E451  E9 A0 FD FF FF                  jmp 0x14020e1f6
0020E456  48 8B 8B B8 00 00 00            mov rcx, qword ptr [rbx + 0xb8]
0020E45D  E8 BE 31 09 00                  call 0x1402a1620
0020E462  E9 D9 FC FF FF                  jmp 0x14020e140
0020E467  48 8B 8B E8 00 00 00            mov rcx, qword ptr [rbx + 0xe8]
0020E46E  48 85 C9                        test rcx, rcx
0020E471  0F 84 DF FD FF FF               je 0x14020e256
0020E477  48 8B D3                        mov rdx, rbx
0020E47A  E8 A1 F3 20 00                  call 0x14041d820
0020E47F  E9 D2 FD FF FF                  jmp 0x14020e256
0020E484  8B 05 2E 86 DB 00               mov eax, dword ptr [rip + 0xdb862e]
0020E48A  A8 40                           test al, 0x40
0020E48C  0F 84 3A FF FF FF               je 0x14020e3cc
0020E492  E8 F9 0F 10 00                  call 0x14030f490
0020E497  84 C0                           test al, al
0020E499  0F 84 2D FF FF FF               je 0x14020e3cc
0020E49F  8B CF                           mov ecx, edi
0020E4A1  E8 BA 0F 10 00                  call 0x14030f460
0020E4A6  E9 23 FF FF FF                  jmp 0x14020e3ce
0020E4AB  F0 0F BA 73 78 0C               lock btr dword ptr [rbx + 0x78], 0xc
0020E4B1  E9 0B FC FF FF                  jmp 0x14020e0c1
0020E4B6  4C 8D 4D 48                     lea r9, [rbp + 0x48]
0020E4BA  45 33 C0                        xor r8d, r8d
0020E4BD  49 8B D5                        mov rdx, r13
0020E4C0  48 8B CF                        mov rcx, rdi
0020E4C3  E8 20 4E 02 00                  call 0x1402332e8
0020E4C8  85 C0                           test eax, eax
0020E4CA  0F 84 A5 FE FF FF               je 0x14020e375
0020E4D0  BE 01 00 00 00                  mov esi, 1
0020E4D5  E9 CA FC FF FF                  jmp 0x14020e1a4
0020E4DA  48 C7 83 C8 00 00 00 00 01 00 00  mov qword ptr [rbx + 0xc8], 0x100
0020E4E5  4C 89 BB D0 03 00 00            mov qword ptr [rbx + 0x3d0], r15
0020E4EC  E9 4E FD FF FF                  jmp 0x14020e23f
0020E4F1  0F BA 73 74 09                  btr dword ptr [rbx + 0x74], 9
0020E4F6  E9 68 FD FF FF                  jmp 0x14020e263
0020E4FB  48 8B 83 D0 03 00 00            mov rax, qword ptr [rbx + 0x3d0]
0020E502  48 89 01                        mov qword ptr [rcx], rax
0020E505  E9 6D FD FF FF                  jmp 0x14020e277
0020E50A  41 80 7C 1E 72 00               cmp byte ptr [r14 + rbx + 0x72], 0
0020E510  0F 84 06 82 4C 00               je 0x1406d671c
0020E516  41 C6 44 1E 72 00               mov byte ptr [r14 + rbx + 0x72], 0
0020E51C  E9 D8 FE FF FF                  jmp 0x14020e3f9
0020E521  48 8D 83 A8 00 00 00            lea rax, [rbx + 0xa8]
0020E528  48 39 00                        cmp qword ptr [rax], rax
0020E52B  0F 84 C8 FE FF FF               je 0x14020e3f9
0020E531  80 8B C2 00 00 00 02            or byte ptr [rbx + 0xc2], 2
0020E538  E9 BC FE FF FF                  jmp 0x14020e3f9
0020E53D  45 33 C9                        xor r9d, r9d
0020E540  45 33 C0                        xor r8d, r8d
0020E543  48 8B CF                        mov rcx, rdi
0020E546  41 8D 51 01                     lea edx, [r9 + 1]
0020E54A  E8 71 47 04 00                  call 0x140252cc0
0020E54F  E9 60 FD FF FF                  jmp 0x14020e2b4
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiCommitThreadWait(__int64 a1, __int64 a2, int a3, __int64 a4, unsigned int a5, __int64 a6)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m58;
    unsigned __int8 v_stack_m66;
    unsigned __int8 v_stack_m67;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p8;

    v_stack_p20 = a4;
    v_rsp = (v_rsp) - (88);
    result = 0;
    v_r15 = 0;
    v_stack_m58 = 0;
    v_stack_m68 = v_xmm0;
    if (a3 != 0) goto loc_0020E21D;
loc_0020E021:
    if (((*(unsigned int *)(a1 + 120)) & (0x400000ULL)) != 0) goto loc_0020E39B;
loc_0020E02E:
    v_stack_p10 = *(unsigned __int64 *)(gs_base + (0 + 32));
    *(unsigned __int64 *)(a1 + 208) = a2;
    result = KiIsKernelStackSwappable(a1, a2, a3, a4);
    v_r14 = 0;
loc_0020E051:
    if (condition_is_above_or_equal) goto loc_0020E077;
loc_0020E05A:
    v_r14 = (unsigned int)((v_r14) + ((unsigned int)(v_r14 + 1)));
    if (((*(unsigned int *)(v_rip + 14381640)) & ((unsigned int)(v_r14))) == 0) goto loc_0020E314;
loc_0020E06A:
loc_0020E06C:
    if (*(unsigned __int64 *)(a1 + 64) == 0) goto loc_0020E051;
    goto loc_0020E05A;
loc_0020E077:
    if ((((unsigned __int8)(*(unsigned __int8 *)(a1 + 112))) & (231)) != 0) goto loc_0020E231;
    result = (unsigned __int8)((*(unsigned __int8 *)(a1 + 112)) & (249));
    a4 = 0;
    result = (unsigned __int8)((result) | (1));
    *(unsigned __int8 *)(a1 + 112) = (unsigned __int8)(result);
    result = KiPerformWaitDeferredWork(a1, (unsigned int)(a5), 1, a4);
    if ((unsigned int)((unsigned int)((unsigned int)(result))) != 0) goto loc_0020E2F3;
loc_0020E0B4:
    if (((*(unsigned int *)(a1 + 120)) & (0x1000ULL)) != 0) goto loc_0020E4AB;
loc_0020E0C1:
    a1 = (condition_is_below) ? 1 : 0;
    result = (condition_is_below) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) != 0) goto loc_0020E406;
loc_0020E0D9:
    v_rsi = 0;
    if (((unsigned int)((unsigned int)(a3))) != 2) goto loc_0020E11E;
    if ((*(unsigned __int8 *)(a1 + 391)) == 0) goto loc_0020E11E;
    if ((*(unsigned int *)(a1 + 484)) != 0) goto loc_0020E11E;
    if ((*(unsigned __int8 *)(a1 + 390)) != 0) goto loc_0020E11E;
    if ((*(unsigned __int8 *)(a1 + 192)) != 0) goto loc_0020E122;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 952))) == 0) goto loc_0020E122;
    v_r13 = (v_stack_p20) + ((unsigned int)(*(unsigned int *)(a1 + 952)));
    goto loc_0020E122;
loc_0020E11E:
loc_0020E122:
    if ((*(unsigned __int8 *)(a1 + 643)) != 15) goto loc_0020E358;
loc_0020E12F:
    *(unsigned __int64 *)(a1 + 64) = 0;
loc_0020E137:
    if (0 != 0) goto loc_0020E456;
loc_0020E140:
    *(unsigned __int8 *)(a1 + 565) = 0;
    if ((unsigned int)((unsigned int)(a3)) == 0) goto loc_0020E1F6;
    if (((unsigned int)((unsigned int)(a3))) != 2) goto loc_0020E4B6;
    a1 = (*(unsigned __int64 *)(a1 + 248)) + (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(a1 + 952))));
    a1 = (a1) + (v_stack_p20);
    *(unsigned __int64 *)(a1 + 256 + 24) = a1;
    a1 = (a1) >> (18);
    v_stack_p8 = (unsigned int)((unsigned __int8)(a1));
    v_stack_m68 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 256)));
    v_stack_m66 = (unsigned __int8)(v_stack_p8);
    *(unsigned int *)(a1 + 256) = (unsigned int)((unsigned int)(v_stack_m68));
    if ((unsigned __int8)((unsigned int)(a3) - 1) != 0) goto loc_0020E388;
loc_0020E1A4:
    if ((*(unsigned int *)(v_rip + 14387869)) == 0) goto loc_0020E33C;
loc_0020E1B1:
    a2 = 0;
loc_0020E1B3:
    a3 = 0;
    *(unsigned __int16 *)(58 + a1 + 256 * 1) = 0;
    result = KiInsertTimerTable(v_stack_p10, a1 + 256, a3, (unsigned int)(v_stack_p8));
    if ((unsigned __int8)(result) == 0) goto loc_0020E375;
    if (((*(unsigned int *)(v_rip + 14387487)) & (0x20000ULL)) != 0) goto loc_0020E444;
loc_0020E1F6:
    result = KiSwapThread(a1, v_stack_p10, a6, (unsigned int)(v_stack_p8));
loc_0020E208:
    v_rsp = (v_rsp) + (88);
    return result;
loc_0020E21D:
    goto loc_0020E021;
loc_0020E231:
    if ((((unsigned __int8)(result)) & (7)) == 0) goto loc_0020E415;
loc_0020E23F:
loc_0020E242:
    *(unsigned __int8 *)(a1 + 388) = 2;
    if ((*(unsigned __int8 *)(a1 + 643)) == 15) goto loc_0020E467;
loc_0020E256:
    *(unsigned __int64 *)(a1 + 64) = result;
    if ((unsigned int)((unsigned int)(a3)) != 0) goto loc_0020E4F1;
loc_0020E263:
    if (a6 != 0) goto loc_0020E4FB;
loc_0020E277:
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) goto loc_0020E3A6;
loc_0020E280:
    v_rdi = (*(unsigned __int8 *)(a1 + 587) + *(unsigned __int8 *)(a1 + 587) * 2) << (4);
    v_rdi = (v_rdi) + ((unsigned int)(a3) - 1);
loc_0020E292:
    if (((unsigned __int8)(*(unsigned __int8 *)((unsigned int)(a3) - 1 + 17))) < 5) goto loc_0020E2C8;
loc_0020E299:
    v_rsi = ((unsigned int)(a3) - 1) + (48);
    if (v_rsi != v_rdi) goto loc_0020E292;
    if ((*(unsigned __int64 *)(v_stack_p10 + 11528)) != 0) goto loc_0020E53D;
loc_0020E2B4:
    result = KiExitThreadWait(v_stack_p10, a1, (unsigned int)(a5), (unsigned int)(v_stack_p8));
    goto loc_0020E208;
loc_0020E2C8:
    result = KiAcquireKobjectLockSafe(*(unsigned __int64 *)(v_rsi + 32), a1, (unsigned int)(a5), (unsigned int)(v_stack_p8));
    if ((*(unsigned __int8 *)(v_rsi + 17)) != 4) goto loc_0020E30A;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) + 8)) != v_rsi) goto loc_0020E2EC;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 8))) == v_rsi) goto loc_0020E303;
loc_0020E2EC:
loc_0020E2F3:
    result = KiInsertPrcbWaitEntry(a1, *(unsigned __int64 *)(v_rsi + 32), (unsigned int)(a5), (unsigned int)(v_stack_p8));
    goto loc_0020E0B4;
loc_0020E303:
    *(unsigned __int64 *)(result) = a1;
    *(unsigned __int64 *)(a1 + 8) = result;
loc_0020E30A:
    goto loc_0020E299;
loc_0020E314:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14387102)))) & (64)) == 0) goto loc_0020E06A;
    result = KiCheckVpBackingLongSpinWaitHypercall(a1, *(unsigned __int64 *)(v_rsi + 32), (unsigned int)(a5), (unsigned int)(v_stack_p8));
    if ((unsigned __int8)(result) == 0) goto loc_0020E06A;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rsi + 32))), *(unsigned __int64 *)(v_rsi + 32), (unsigned int)(a5), (unsigned int)(v_stack_p8));
    goto loc_0020E06C;
loc_0020E33C:
    result = PsTimerResolutionActive(*(unsigned __int64 *)(a1 + 544), *(unsigned __int64 *)(v_rsi + 32), (unsigned int)(a5), (unsigned int)(v_stack_p8));
    if ((unsigned __int8)(result) != 0) goto loc_0020E1B1;
    goto loc_0020E1B3;
loc_0020E358:
    if (*(unsigned __int64 *)(a1 + 232) == 0) goto loc_0020E12F;
    result = KiActivateWaiterQueueWithThreadLock(a1, *(unsigned __int64 *)(a1 + 232), (unsigned int)(a5), (unsigned int)(v_stack_p8));
    goto loc_0020E137;
loc_0020E375:
    a3 = 0;
    result = KiTimerWaitTest(*(unsigned __int64 *)(v_rsi + 32), v_stack_p10, a3, (unsigned int)(v_stack_p8));
    goto loc_0020E1F6;
loc_0020E388:
    goto loc_0020E1A4;
loc_0020E39B:
    goto loc_0020E02E;
loc_0020E3A6:
    v_rdi = 0;
loc_0020E3B4:
    if (condition_is_above_or_equal) goto loc_0020E3D9;
loc_0020E3BD:
    v_rdi = (unsigned int)((v_rdi) + ((unsigned int)(v_rdi + 1)));
    if (((*(unsigned int *)(v_rip + 14380774)) & ((unsigned int)(v_rdi))) == 0) goto loc_0020E484;
loc_0020E3CC:
loc_0020E3CE:
    if (*(unsigned __int64 *)(a1 + 64) == 0) goto loc_0020E3B4;
    goto loc_0020E3BD;
loc_0020E3D9:
    if ((*(unsigned __int64 *)(a1 + 200)) != 257) goto loc_0020E521;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 116)))) & (16)) != 0) goto loc_0020E50A;
loc_0020E3F9:
    *(unsigned __int64 *)(a1 + 64) = 0;
    goto loc_0020E280;
loc_0020E406:
    v_r15 = *(unsigned __int64 *)(a1 + 200);
    if (condition_is_above_or_equal) { v_r15 = (unsigned int)(v_rsi); }
    goto loc_0020E0D9;
loc_0020E415:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 116)))) & (32)) != 0) goto loc_0020E4DA;
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(a1 + 116))) & (64));
    result = (unsigned __int8)(-(result));
    result = (result) & (-65);
    result = (result) + (257);
    *(unsigned __int64 *)(a1 + 200) = result;
    *(unsigned __int64 *)(a1 + 976) = v_r15;
    goto loc_0020E242;
loc_0020E444:
    a2 = 0;
    result = KiTraceSetTimer(v_rdi, a2, (unsigned __int8)(v_rsi), (unsigned int)(v_stack_p8));
    goto loc_0020E1F6;
loc_0020E456:
    result = KiDecrementProcessStackCount(*(unsigned __int64 *)(a1 + 184), a2, (unsigned __int8)(v_rsi), (unsigned int)(v_stack_p8));
    goto loc_0020E140;
loc_0020E467:
    if (*(unsigned __int64 *)(a1 + 232) == 0) goto loc_0020E256;
    result = KiIncrementConcurrencyCount(*(unsigned __int64 *)(a1 + 232), a1, (unsigned __int8)(v_rsi), (unsigned int)(v_stack_p8));
    goto loc_0020E256;
loc_0020E484:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14386734)))) & (64)) == 0) goto loc_0020E3CC;
    result = KiCheckVpBackingLongSpinWaitHypercall(*(unsigned __int64 *)(a1 + 232), a1, (unsigned __int8)(v_rsi), (unsigned int)(v_stack_p8));
    if ((unsigned __int8)(result) == 0) goto loc_0020E3CC;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rdi)), a1, (unsigned __int8)(v_rsi), (unsigned int)(v_stack_p8));
    goto loc_0020E3CE;
loc_0020E4AB:
    goto loc_0020E0C1;
loc_0020E4B6:
    a3 = 0;
    result = KiComputeDueTime(v_rdi, 257, a3, v_stack_p8);
    if ((unsigned int)(result) == 0) goto loc_0020E375;
    goto loc_0020E1A4;
loc_0020E4DA:
    *(unsigned __int64 *)(a1 + 200) = 256;
    *(unsigned __int64 *)(a1 + 976) = v_r15;
    goto loc_0020E23F;
loc_0020E4F1:
    goto loc_0020E263;
loc_0020E4FB:
    *(unsigned __int64 *)(v_rdi) = *(unsigned __int64 *)(a1 + 976);
    goto loc_0020E277;
loc_0020E50A:
    *(unsigned __int8 *)((__int8)(*(unsigned __int8 *)(a1 + 391)) + a1 * 1 + 114) = 0;
    goto loc_0020E3F9;
loc_0020E521:
    if ((*(unsigned __int64 *)(a1 + 168)) == (a1 + 168)) goto loc_0020E3F9;
    goto loc_0020E3F9;
loc_0020E53D:
    a4 = 0;
    a3 = 0;
    result = KiProcessThreadWaitList(v_rdi, a4 + 1, a3, a4);
    goto loc_0020E2B4;
}
```

## 5. (Beta) C Style

```c
int64_t KiCommitThreadWait(void *Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4, uint32_t Arg5, int64_t Arg6)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m58;
    uint8_t v_stack_m66;
    uint8_t v_stack_m67;
    uint64_t v_stack_m68;
    uint64_t v_stack_m78;
    uint64_t v_stack_p10;
    uint64_t v_stack_p20;
    uint32_t v_stack_p8;

    v_stack_p20 = Arg4;
    local_rsp = (local_rsp) - (88);
    result = 0;
    local_r15 = 0;
    v_stack_m58 = 0;
    v_stack_m68 = v_xmm0;
    if (Arg3 != 0) goto loc_0020E21D;
loc_0020E021:
    if (((*(uint32_t *)(arg1 + 0x78)) & (0x400000ULL)) != 0) goto loc_0020E39B;
loc_0020E02E:
    v_stack_p10 = *(uint64_t *)(gs_base + (0 + 0x20));
    *(uint64_t *)(arg1 + 0xD0) = Arg2;
    result = KiIsKernelStackSwappable(Arg1, Arg2, Arg3, Arg4);
    local_r14 = 0;
loc_0020E051:
    if (condition_is_above_or_equal) goto loc_0020E077;
loc_0020E05A:
    local_r14 = (uint32_t)((local_r14) + ((uint32_t)(local_r14 + 1)));
    if (((*(uint32_t *)(v_rip + 0xDB7248)) & ((uint32_t)(local_r14))) == 0) goto loc_0020E314;
loc_0020E06A:
loc_0020E06C:
    if (*(uint64_t *)(arg1 + 0x40) == 0) goto loc_0020E051;
    goto loc_0020E05A;
loc_0020E077:
    if ((((uint8_t)(*(uint8_t *)(arg1 + 0x70))) & (231)) != 0) goto loc_0020E231;
    result = (uint8_t)((*(uint8_t *)(arg1 + 0x70)) & (249));
    Arg4 = 0;
    result = (uint8_t)((result) | (1));
    *(uint8_t *)(arg1 + 0x70) = (uint8_t)(result);
    result = KiPerformWaitDeferredWork(Arg1, (uint32_t)(Arg5), 1, Arg4);
    if ((uint32_t)((uint32_t)((uint32_t)(result))) != 0) goto loc_0020E2F3;
loc_0020E0B4:
    if (((*(uint32_t *)(arg1 + 0x78)) & (0x1000ULL)) != 0) goto loc_0020E4AB;
loc_0020E0C1:
    Arg1 = (condition_is_below) ? 1 : 0;
    result = (condition_is_below) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) != 0) goto loc_0020E406;
loc_0020E0D9:
    local_rsi = 0;
    if (((uint32_t)((uint32_t)(Arg3))) != 2) goto loc_0020E11E;
    if ((*(uint8_t *)(arg1 + 0x187)) == 0) goto loc_0020E11E;
    if ((*(uint32_t *)(arg1 + 0x1E4)) != 0) goto loc_0020E11E;
    if ((*(uint8_t *)(arg1 + 0x186)) != 0) goto loc_0020E11E;
    if ((*(uint8_t *)(arg1 + 0xC0)) != 0) goto loc_0020E122;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x3B8))) == 0) goto loc_0020E122;
    local_r13 = (v_stack_p20) + ((uint32_t)(*(uint32_t *)(arg1 + 0x3B8)));
    goto loc_0020E122;
loc_0020E11E:
loc_0020E122:
    if ((*(uint8_t *)(arg1 + 0x283)) != 15) goto loc_0020E358;
loc_0020E12F:
    *(uint64_t *)(arg1 + 0x40) = 0;
loc_0020E137:
    if (0 != 0) goto loc_0020E456;
loc_0020E140:
    *(uint8_t *)(arg1 + 0x235) = 0;
    if ((uint32_t)((uint32_t)(Arg3)) == 0) goto loc_0020E1F6;
    if (((uint32_t)((uint32_t)(Arg3))) != 2) goto loc_0020E4B6;
    Arg1 = (*(uint64_t *)(arg1 + 0xF8)) + (*(uint64_t *)((uint32_t)(*(uint32_t *)(arg1 + 0x3B8))));
    Arg1 = (Arg1) + (v_stack_p20);
    *(void **)(arg1 + 0x100 + 0x18) = Arg1;
    Arg1 = (Arg1) >> (18);
    v_stack_p8 = (uint32_t)((uint8_t)(Arg1));
    v_stack_m68 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x100)));
    v_stack_m66 = (uint8_t)(v_stack_p8);
    *(uint32_t *)(arg1 + 0x100) = (uint32_t)((uint32_t)(v_stack_m68));
    if ((uint8_t)((uint32_t)(Arg3) - 1) != 0) goto loc_0020E388;
loc_0020E1A4:
    if ((*(uint32_t *)(v_rip + 0xDB8A9D)) == 0) goto loc_0020E33C;
loc_0020E1B1:
    Arg2 = 0;
loc_0020E1B3:
    Arg3 = 0;
    *(uint16_t *)(58 + arg1 + 0x100 * 1) = 0;
    result = KiInsertTimerTable(v_stack_p10, Arg1 + 256, Arg3, (uint32_t)(v_stack_p8));
    if ((uint8_t)(result) == 0) goto loc_0020E375;
    if (((*(uint32_t *)(v_rip + 0xDB891F)) & (0x20000ULL)) != 0) goto loc_0020E444;
loc_0020E1F6:
    result = KiSwapThread(Arg1, v_stack_p10, Arg6, (uint32_t)(v_stack_p8));
loc_0020E208:
    local_rsp = (local_rsp) + (88);
    return result;
loc_0020E21D:
    goto loc_0020E021;
loc_0020E231:
    if ((((uint8_t)(result)) & (7)) == 0) goto loc_0020E415;
loc_0020E23F:
loc_0020E242:
    *(uint8_t *)(arg1 + 0x184) = 2;
    if ((*(uint8_t *)(arg1 + 0x283)) == 15) goto loc_0020E467;
loc_0020E256:
    *(uint64_t *)(arg1 + 0x40) = result;
    if ((uint32_t)((uint32_t)(Arg3)) != 0) goto loc_0020E4F1;
loc_0020E263:
    if (Arg6 != 0) goto loc_0020E4FB;
loc_0020E277:
    if ((uint8_t)((uint8_t)(result)) != 0) goto loc_0020E3A6;
loc_0020E280:
    local_rdi = (*(uint8_t *)(arg1 + 0x24B) + *(uint8_t *)(arg1 + 0x24B) * 2) << (4);
    local_rdi = (local_rdi) + ((uint32_t)(Arg3) - 1);
loc_0020E292:
    if (((uint8_t)(*(uint8_t *)((uint32_t)(Arg3) - 0x1 + 0x11))) < 5) goto loc_0020E2C8;
loc_0020E299:
    local_rsi = ((uint32_t)(Arg3) - 1) + (48);
    if (local_rsi != local_rdi) goto loc_0020E292;
    if ((*(uint64_t *)(v_stack_p10 + 0x2D08)) != 0) goto loc_0020E53D;
loc_0020E2B4:
    result = KiExitThreadWait(v_stack_p10, Arg1, (uint32_t)(Arg5), (uint32_t)(v_stack_p8));
    goto loc_0020E208;
loc_0020E2C8:
    result = KiAcquireKobjectLockSafe(*(uint64_t *)(local_rsi + 0x20), Arg1, (uint32_t)(Arg5), (uint32_t)(v_stack_p8));
    if ((*(uint8_t *)(local_rsi + 0x11)) != 4) goto loc_0020E30A;
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi) + 0x8)) != local_rsi) goto loc_0020E2EC;
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi + 0x8))) == local_rsi) goto loc_0020E303;
loc_0020E2EC:
loc_0020E2F3:
    result = KiInsertPrcbWaitEntry(Arg1, *(uint64_t *)(local_rsi + 0x20), (uint32_t)(Arg5), (uint32_t)(v_stack_p8));
    goto loc_0020E0B4;
loc_0020E303:
    *(void **)(result) = Arg1;
    *(uint64_t *)(arg1 + 0x8) = result;
loc_0020E30A:
    goto loc_0020E299;
loc_0020E314:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xDB879E)))) & (64)) == 0) goto loc_0020E06A;
    result = KiCheckVpBackingLongSpinWaitHypercall(Arg1, *(uint64_t *)(local_rsi + 0x20), (uint32_t)(Arg5), (uint32_t)(v_stack_p8));
    if ((uint8_t)(result) == 0) goto loc_0020E06A;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(*(uint64_t *)(local_rsi + 0x20))), *(uint64_t *)(local_rsi + 0x20), (uint32_t)(Arg5), (uint32_t)(v_stack_p8));
    goto loc_0020E06C;
loc_0020E33C:
    result = PsTimerResolutionActive(*(uint64_t *)(arg1 + 0x220), *(uint64_t *)(local_rsi + 0x20), (uint32_t)(Arg5), (uint32_t)(v_stack_p8));
    if ((uint8_t)(result) != 0) goto loc_0020E1B1;
    goto loc_0020E1B3;
loc_0020E358:
    if (*(uint64_t *)(arg1 + 0xE8) == 0) goto loc_0020E12F;
    result = KiActivateWaiterQueueWithThreadLock(Arg1, *(uint64_t *)(arg1 + 0xE8), (uint32_t)(Arg5), (uint32_t)(v_stack_p8));
    goto loc_0020E137;
loc_0020E375:
    Arg3 = 0;
    result = KiTimerWaitTest(*(uint64_t *)(local_rsi + 0x20), v_stack_p10, Arg3, (uint32_t)(v_stack_p8));
    goto loc_0020E1F6;
loc_0020E388:
    goto loc_0020E1A4;
loc_0020E39B:
    goto loc_0020E02E;
loc_0020E3A6:
    local_rdi = 0;
loc_0020E3B4:
    if (condition_is_above_or_equal) goto loc_0020E3D9;
loc_0020E3BD:
    local_rdi = (uint32_t)((local_rdi) + ((uint32_t)(local_rdi + 1)));
    if (((*(uint32_t *)(v_rip + 0xDB6EE6)) & ((uint32_t)(local_rdi))) == 0) goto loc_0020E484;
loc_0020E3CC:
loc_0020E3CE:
    if (*(uint64_t *)(arg1 + 0x40) == 0) goto loc_0020E3B4;
    goto loc_0020E3BD;
loc_0020E3D9:
    if ((*(uint64_t *)(arg1 + 0xC8)) != 257) goto loc_0020E521;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x74)))) & (16)) != 0) goto loc_0020E50A;
loc_0020E3F9:
    *(uint64_t *)(arg1 + 0x40) = 0;
    goto loc_0020E280;
loc_0020E406:
    local_r15 = *(uint64_t *)(arg1 + 0xC8);
    if (condition_is_above_or_equal) { local_r15 = (uint32_t)(local_rsi); }
    goto loc_0020E0D9;
loc_0020E415:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x74)))) & (32)) != 0) goto loc_0020E4DA;
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x74))) & (64));
    result = (uint8_t)(-(result));
    result = (result) & (-65);
    result = (result) + (257);
    *(uint64_t *)(arg1 + 0xC8) = result;
    *(uint64_t *)(arg1 + 0x3D0) = local_r15;
    goto loc_0020E242;
loc_0020E444:
    Arg2 = 0;
    result = KiTraceSetTimer(local_rdi, Arg2, (uint8_t)(local_rsi), (uint32_t)(v_stack_p8));
    goto loc_0020E1F6;
loc_0020E456:
    result = KiDecrementProcessStackCount(*(uint64_t *)(arg1 + 0xB8), Arg2, (uint8_t)(local_rsi), (uint32_t)(v_stack_p8));
    goto loc_0020E140;
loc_0020E467:
    if (*(uint64_t *)(arg1 + 0xE8) == 0) goto loc_0020E256;
    result = KiIncrementConcurrencyCount(*(uint64_t *)(arg1 + 0xE8), Arg1, (uint8_t)(local_rsi), (uint32_t)(v_stack_p8));
    goto loc_0020E256;
loc_0020E484:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xDB862E)))) & (64)) == 0) goto loc_0020E3CC;
    result = KiCheckVpBackingLongSpinWaitHypercall(*(uint64_t *)(arg1 + 0xE8), Arg1, (uint8_t)(local_rsi), (uint32_t)(v_stack_p8));
    if ((uint8_t)(result) == 0) goto loc_0020E3CC;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rdi)), Arg1, (uint8_t)(local_rsi), (uint32_t)(v_stack_p8));
    goto loc_0020E3CE;
loc_0020E4AB:
    goto loc_0020E0C1;
loc_0020E4B6:
    Arg3 = 0;
    result = KiComputeDueTime(local_rdi, 257, Arg3, v_stack_p8);
    if ((uint32_t)(result) == 0) goto loc_0020E375;
    goto loc_0020E1A4;
loc_0020E4DA:
    *(uint64_t *)(arg1 + 0xC8) = 256;
    *(uint64_t *)(arg1 + 0x3D0) = local_r15;
    goto loc_0020E23F;
loc_0020E4F1:
    goto loc_0020E263;
loc_0020E4FB:
    *(uint64_t *)(local_rdi) = *(uint64_t *)(arg1 + 0x3D0);
    goto loc_0020E277;
loc_0020E50A:
    *(uint8_t *)((int8_t)(*(uint8_t *)(arg1 + 0x187)) + arg1 * 1 + 0x72) = 0;
    goto loc_0020E3F9;
loc_0020E521:
    if ((*(uint64_t *)(arg1 + 0xA8)) == (Arg1 + 168)) goto loc_0020E3F9;
    goto loc_0020E3F9;
loc_0020E53D:
    Arg4 = 0;
    Arg3 = 0;
    result = KiProcessThreadWaitList(local_rdi, Arg4 + 1, Arg3, Arg4);
    goto loc_0020E2B4;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x40` | `64` | `R` |
| `Arg1` | `+ 0x40` | `64` | `R/W` |
| `Arg1` | `+ 0x40` | `64` | `W` |
| `Arg1` | `+ 0x70` | `8` | `R` |
| `Arg1` | `+ 0x70` | `8` | `W` |
| `Arg1` | `+ 0x74` | `32` | `R` |
| `Arg1` | `+ 0x74` | `32` | `R/W` |
| `Arg1` | `+ 0x78` | `32` | `R` |
| `Arg1` | `+ 0x78` | `32` | `R/W` |
| `Arg1` | `+ 0xA8` | `64` | `R` |
| `Arg1` | `+ 0xB8` | `64` | `R` |
| `Arg1` | `+ 0xC0` | `8` | `R` |
| `Arg1` | `+ 0xC2` | `8` | `R/W` |
| `Arg1` | `+ 0xC8` | `64` | `R` |
| `Arg1` | `+ 0xC8` | `64` | `W` |
| `Arg1` | `+ 0xD0` | `64` | `W` |
| `Arg1` | `+ 0xE8` | `64` | `R` |
| `Arg1` | `+ 0xF8` | `64` | `R` |
| `Arg1` | `+ 0x100` | `32` | `R/W` |
| `Arg1` | `+ 0x100` | `64` | `R` |
| `Arg1` | `+ 0x184` | `8` | `W` |
| `Arg1` | `+ 0x186` | `8` | `R` |
| `Arg1` | `+ 0x187` | `8` | `R` |
| `Arg1` | `+ 0x1E4` | `32` | `R` |
| `Arg1` | `+ 0x220` | `64` | `R` |
| `Arg1` | `+ 0x235` | `8` | `W` |
| `Arg1` | `+ 0x24B` | `8` | `R` |
| `Arg1` | `+ 0x283` | `8` | `R` |
| `Arg1` | `+ 0x3B8` | `32` | `R` |
| `Arg1` | `+ 0x3D0` | `64` | `R` |
| `Arg1` | `+ 0x3D0` | `64` | `W` |

추가 오프셋 1개는 표에서 생략했습니다.

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0020DFE0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
