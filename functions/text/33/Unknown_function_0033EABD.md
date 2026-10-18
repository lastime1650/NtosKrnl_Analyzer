# sub_0033EABD

- RVA: `0x0033EABD`–`0x0033EF73` (길이 `1,206` bytes)
- VA: `0x000000014033EABD`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000772FC`
- 디코드: `272`개 명령, `1,206/1,206` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **28**; 고유 호출 대상: **15**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0033EB55` → [MiUpdateAvailableEventsAtDpc](../3B/MiUpdateAvailableEventsAtDpc_function_003BC804.md) (function, `0x003BC804`)
- `0x0033EBC0` → [MiRebuildStandbyLookasideList](../3D/MiRebuildStandbyLookasideList_function_003D50E0.md) (function, `0x003D50E0`)
- `0x0033EBCB` → [MiExclusiveInsertPfnChainInList](../44/MiExclusiveInsertPfnChainInList_function_00445C48.md) (function, `0x00445C48`)
- `0x0033EBD9` → [ExReleaseSpinLockExclusiveFromDpcLevel](../24/ExReleaseSpinLockExclusiveFromDpcLevel_function_002497E0.md) (function, `0x002497E0`)
- `0x0033EBF4` → [MiSufficientAvailablePages](../36/MiSufficientAvailablePages_function_0036D0B0.md) (function, `0x0036D0B0`)
- `0x0033EC18` → [MiWakeModifiedPageWriter](../3B/MiWakeModifiedPageWriter_function_003BCB18.md) (function, `0x003BCB18`)
- `0x0033EC46` → [KeSetEvent](KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x0033ECA1` → [ExpReleaseSpinLockSharedFromDpcLevelInstrumented](../2F/ExpReleaseSpinLockSharedFromDpcLevelInstrumented_function_002F0F48.md) (function, `0x002F0F48`)
- `0x0033ECE4` → [MiSlabDemotionLowMemoryConditionUpdate](../3B/MiSlabDemotionLowMemoryConditionUpdate_function_003BB7E0.md) (function, `0x003BB7E0`)
- `0x0033ED01` → [ExReleaseSpinLockExclusiveFromDpcLevel](../24/ExReleaseSpinLockExclusiveFromDpcLevel_function_002497E0.md) (function, `0x002497E0`)
- `0x0033ED29` → [MiGetPfnPriority](../32/MiGetPfnPriority_function_003226F0.md) (function, `0x003226F0`)
- `0x0033ED60` → [ExAcquireSpinLockExclusiveAtDpcLevel](../24/ExAcquireSpinLockExclusiveAtDpcLevel_function_00248E80.md) (function, `0x00248E80`)
- `0x0033ED6B` → [MiExclusiveInsertPfnChainInList](../44/MiExclusiveInsertPfnChainInList_function_00445C48.md) (function, `0x00445C48`)
- `0x0033ED87` → [ExAcquireSpinLockExclusive](../24/ExAcquireSpinLockExclusive_function_00248690.md) (function, `0x00248690`)
- `0x0033ED98` → [MiRestockOverCommit](../40/MiRestockOverCommit_function_00407D94.md) (function, `0x00407D94`)
- `0x0033EDA8` → [MiReleaseSpinLockExclusive](../24/MiReleaseSpinLockExclusive_function_002482C0.md) (function, `0x002482C0`)
- `0x0033EDCC` → [ExAcquireSpinLockExclusiveAtDpcLevel](../24/ExAcquireSpinLockExclusiveAtDpcLevel_function_00248E80.md) (function, `0x00248E80`)
- `0x0033EE06` → [ExAcquireSpinLockExclusiveAtDpcLevel](../24/ExAcquireSpinLockExclusiveAtDpcLevel_function_00248E80.md) (function, `0x00248E80`)
- `0x0033EE22` → [KeSetEvent](KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x0033EE44` → [KeSetEvent](KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x0033EE66` → [KeSetEvent](KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x0033EE7D` → [ExReleaseSpinLockExclusiveFromDpcLevel](../24/ExReleaseSpinLockExclusiveFromDpcLevel_function_002497E0.md) (function, `0x002497E0`)
- `0x0033EECF` → [MiSlabDemotionLowMemoryConditionUpdate](../3B/MiSlabDemotionLowMemoryConditionUpdate_function_003BB7E0.md) (function, `0x003BB7E0`)
- `0x0033EEF6` → [ExAcquireSpinLockExclusiveAtDpcLevel](../24/ExAcquireSpinLockExclusiveAtDpcLevel_function_00248E80.md) (function, `0x00248E80`)
- `0x0033EF03` → [KeSetEvent](KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x0033EF0E` → [ExReleaseSpinLockExclusiveFromDpcLevel](../24/ExReleaseSpinLockExclusiveFromDpcLevel_function_002497E0.md) (function, `0x002497E0`)
- `0x0033EF2A` → [MiUpdateAvailableEventsAtDpc](../3B/MiUpdateAvailableEventsAtDpc_function_003BC804.md) (function, `0x003BC804`)
- `0x0033EF63` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0033EC8F` → RVA `0x00F0DE58` (`.data`; read)
- `0x0033ED32` → RVA `0x00E30088` (`.data`; read)
- `0x0033EDBB` → RVA `0x00E38D00` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **25**
  - `0x0033EACB` → [sub_0033E2D1 + 0x15E](Unknown_function_0033E2D1.md) (`tail-transfer`)
  - `0x0033EAEE` → [sub_0033E2D1 + 0x133](Unknown_function_0033E2D1.md) (`tail-transfer`)
  - `0x0033EAF6` → [sub_0033E2D1 + 0x14D](Unknown_function_0033E2D1.md) (`tail-transfer`)
  - `0x0033EAFC` → [sub_0033E2D1 + 0x133](Unknown_function_0033E2D1.md) (`tail-transfer`)
  - `0x0033EB61` → [sub_0033E2D1 + 0x133](Unknown_function_0033E2D1.md) (`tail-transfer`)
  - `0x0033EB90` → [sub_0033E839 + 0x1A6](Unknown_function_0033E839.md) (`tail-transfer`)
  - `0x0033EBA1` → [sub_0033E2D1 + 0x2C5](Unknown_function_0033E2D1.md) (`tail-transfer`)
  - `0x0033EBD0` → [sub_0033E2D1 + 0x417](Unknown_function_0033E2D1.md) (`tail-transfer`)
  - `0x0033EBE1` → [sub_0033E2D1 + 0x4FC](Unknown_function_0033E2D1.md) (`tail-transfer`)
  - `0x0033EBFB` → [sub_0033E2D1 + 0x4FC](Unknown_function_0033E2D1.md) (`tail-transfer`)
  - `0x0033EC27` → [sub_0033E2D1 + 0x4FC](Unknown_function_0033E2D1.md) (`tail-transfer`)
  - `0x0033EC34` → [sub_0033E2D1 + 0x4FC](Unknown_function_0033E2D1.md) (`tail-transfer`)
  - `0x0033EC4B` → [sub_0033E2D1 + 0x4FC](Unknown_function_0033E2D1.md) (`tail-transfer`)
  - `0x0033EC53` → [sub_0033E839 + 0x16F](Unknown_function_0033E839.md) (`tail-transfer`)
  - `0x0033EC6C` → [sub_0033E2D1 + 0x2C5](Unknown_function_0033E2D1.md) (`tail-transfer`)
  - `0x0033EC74` → [sub_0033E839 + 0xED](Unknown_function_0033E839.md) (`tail-transfer`)
  - `0x0033EC8A` → [sub_0033E2D1 + 0x2CF](Unknown_function_0033E2D1.md) (`tail-transfer`)
  - `0x0033EC97` → [sub_0033E2D1 + 0x4F2](Unknown_function_0033E2D1.md) (`tail-transfer`)
  - `0x0033ECA6` → [sub_0033E2D1 + 0x4FC](Unknown_function_0033E2D1.md) (`tail-transfer`)
  - `0x0033ECD6` → [sub_0033E2D1 + 0x10F](Unknown_function_0033E2D1.md) (`tail-transfer`)
  - `0x0033ED70` → [sub_0033E2D1 + 0x417](Unknown_function_0033E2D1.md) (`tail-transfer`)
  - `0x0033EDB0` → [sub_0033E839 + 0x13E](Unknown_function_0033E839.md) (`tail-transfer`)
  - `0x0033EDC2` → [sub_0033E839 + 0xD1](Unknown_function_0033E839.md) (`tail-transfer`)
  - `0x0033EF22` → [sub_0033E2D1 + 0x10F](Unknown_function_0033E2D1.md) (`tail-transfer`)
  - `0x0033EF2F` → [sub_0033E2D1 + 0x12C](Unknown_function_0033E2D1.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0033EABD  49 8B 82 C0 44 00 00            mov rax, qword ptr [r10 + 0x44c0]
0033EAC4  8B 40 18                        mov eax, dword ptr [rax + 0x18]
0033EAC7  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
0033EACB  E9 5F F9 FF FF                  jmp 0x14033e42f
0033EAD0  33 C0                           xor eax, eax
0033EAD2  C7 44 24 34 00 00 00 00         mov dword ptr [rsp + 0x34], 0
0033EADA  45 84 FF                        test r15b, r15b
0033EADD  41 0F 44 C6                     cmove eax, r14d
0033EAE1  8B 4F 60                        mov ecx, dword ptr [rdi + 0x60]
0033EAE4  44 8B E8                        mov r13d, eax
0033EAE7  89 4C 24 40                     mov dword ptr [rsp + 0x40], ecx
0033EAEB  45 84 FF                        test r15b, r15b
0033EAEE  0F 85 10 F9 FF FF               jne 0x14033e404
0033EAF4  85 F6                           test esi, esi
0033EAF6  0F 85 22 F9 FF FF               jne 0x14033e41e
0033EAFC  E9 03 F9 FF FF                  jmp 0x14033e404
0033EB01  49 8B CC                        mov rcx, r12
0033EB04  F0 49 0F C1 8A 00 49 00 00      lock xadd qword ptr [r10 + 0x4900], rcx
0033EB0D  48 8B C1                        mov rax, rcx
0033EB10  48 89 4C 24 50                  mov qword ptr [rsp + 0x50], rcx
0033EB15  49 03 CC                        add rcx, r12
0033EB18  48 89 4C 24 48                  mov qword ptr [rsp + 0x48], rcx
0033EB1D  48 3D 20 04 00 00               cmp rax, 0x420
0033EB23  0F 82 AA 02 00 00               jb 0x14033edd3
0033EB29  49 8B 82 08 41 00 00            mov rax, qword ptr [r10 + 0x4108]
0033EB30  48 8B 54 24 50                  mov rdx, qword ptr [rsp + 0x50]
0033EB35  48 3B D0                        cmp rdx, rax
0033EB38  0F 86 3B 01 00 00               jbe 0x14033ec79
0033EB3E  4D 8B 82 00 41 00 00            mov r8, qword ptr [r10 + 0x4100]
0033EB45  41 8B C5                        mov eax, r13d
0033EB48  49 3B D0                        cmp rdx, r8
0033EB4B  77 94                           ja 0x14033eae1
0033EB4D  49 3B C8                        cmp rcx, r8
0033EB50  76 8F                           jbe 0x14033eae1
0033EB52  49 8B CA                        mov rcx, r10
0033EB55  E8 AA DC 07 00                  call 0x1403bc804
0033EB5A  8B 4F 60                        mov ecx, dword ptr [rdi + 0x60]
0033EB5D  89 4C 24 40                     mov dword ptr [rsp + 0x40], ecx
0033EB61  E9 9E F8 FF FF                  jmp 0x14033e404
0033EB66  B9 C0 00 00 00                  mov ecx, 0xc0
0033EB6B  3B D1                           cmp edx, ecx
0033EB6D  7E 1E                           jle 0x14033eb8d
0033EB6F  83 FA FF                        cmp edx, -1
0033EB72  74 19                           je 0x14033eb8d
0033EB74  8B C2                           mov eax, edx
0033EB76  F0 41 0F B1 88 9C 8B 00 00      lock cmpxchg dword ptr [r8 + 0x8b9c], ecx
0033EB7F  75 0C                           jne 0x14033eb8d
0033EB81  8D 82 40 FF FF FF               lea eax, [rdx - 0xc0]
0033EB87  4C 63 C8                        movsxd r9, eax
0033EB8A  4D 03 CC                        add r9, r12
0033EB8D  4D 85 C9                        test r9, r9
0033EB90  0F 84 49 FE FF FF               je 0x14033e9df
0033EB96  F0 4D 01 8A 40 49 00 00         lock add qword ptr [r10 + 0x4940], r9
0033EB9E  45 33 ED                        xor r13d, r13d
0033EBA1  E9 F0 F9 FF FF                  jmp 0x14033e596
0033EBA6  4D 85 F6                        test r14, r14
0033EBA9  0F 85 3F 01 00 00               jne 0x14033ecee
0033EBAF  0F B6 55 A2                     movzx edx, byte ptr [rbp - 0x5e]
0033EBB3  83 FA 03                        cmp edx, 3
0033EBB6  74 0D                           je 0x14033ebc5
0033EBB8  44 0F B6 45 A1                  movzx r8d, byte ptr [rbp - 0x5f]
0033EBBD  48 8B CB                        mov rcx, rbx
0033EBC0  E8 1B 65 09 00                  call 0x1403d50e0
0033EBC5  49 8B D7                        mov rdx, r15
0033EBC8  48 8B CF                        mov rcx, rdi
0033EBCB  E8 78 70 10 00                  call 0x140445c48
0033EBD0  E9 13 FB FF FF                  jmp 0x14033e6e8
0033EBD5  49 8D 4F 20                     lea rcx, [r15 + 0x20]
0033EBD9  E8 02 AC F0 FF                  call 0x1402497e0
0033EBDE  83 FB 03                        cmp ebx, 3
0033EBE1  0F 84 E6 FB FF FF               je 0x14033e7cd
0033EBE7  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
0033EBEC  BA 20 04 00 00                  mov edx, 0x420
0033EBF1  48 8B CE                        mov rcx, rsi
0033EBF4  E8 B7 E4 02 00                  call 0x14036d0b0
0033EBF9  85 C0                           test eax, eax
0033EBFB  0F 85 CC FB FF FF               jne 0x14033e7cd
0033EC01  48 8B 9E A0 4C 00 00            mov rbx, qword ptr [rsi + 0x4ca0]
0033EC08  48 83 FB 10                     cmp rbx, 0x10
0033EC0C  72 0F                           jb 0x14033ec1d
0033EC0E  48 C7 C2 FF FF FF FF            mov rdx, 0xffffffffffffffff
0033EC15  48 8B CE                        mov rcx, rsi
0033EC18  E8 FB DE 07 00                  call 0x1403bcb18
0033EC1D  48 8B 86 C0 4B 00 00            mov rax, qword ptr [rsi + 0x4bc0]
0033EC24  48 3B C3                        cmp rax, rbx
0033EC27  0F 86 A0 FB FF FF               jbe 0x14033e7cd
0033EC2D  48 2B C3                        sub rax, rbx
0033EC30  48 83 F8 10                     cmp rax, 0x10
0033EC34  0F 82 93 FB FF FF               jb 0x14033e7cd
0033EC3A  48 8D 8E 48 03 00 00            lea rcx, [rsi + 0x348]
0033EC41  45 33 C0                        xor r8d, r8d
0033EC44  33 D2                           xor edx, edx
0033EC46  E8 C5 06 00 00                  call 0x14033f310
0033EC4B  E9 7D FB FF FF                  jmp 0x14033e7cd
0033EC50  83 F8 FF                        cmp eax, -1
0033EC53  0F 85 4F FD FF FF               jne 0x14033e9a8
0033EC59  E9 08 FF FF FF                  jmp 0x14033eb66
0033EC5E  4D 8B CC                        mov r9, r12
0033EC61  F0 4D 01 8A 40 49 00 00         lock add qword ptr [r10 + 0x4940], r9
0033EC69  45 33 ED                        xor r13d, r13d
0033EC6C  E9 25 F9 FF FF                  jmp 0x14033e596
0033EC71  4C 8B C1                        mov r8, rcx
0033EC74  E9 AD FC FF FF                  jmp 0x14033e926
0033EC79  48 3B C8                        cmp rcx, rax
0033EC7C  0F 86 BC FE FF FF               jbe 0x14033eb3e
0033EC82  E9 CB FE FF FF                  jmp 0x14033eb52
0033EC87  45 33 ED                        xor r13d, r13d
0033EC8A  E9 11 F9 FF FF                  jmp 0x14033e5a0
0033EC8F  8B 05 C3 F1 BC 00               mov eax, dword ptr [rip + 0xbcf1c3]
0033EC95  85 C0                           test eax, eax
0033EC97  0F 85 26 FB FF FF               jne 0x14033e7c3
0033EC9D  48 8B 55 48                     mov rdx, qword ptr [rbp + 0x48]
0033ECA1  E8 A2 22 FB FF                  call 0x1402f0f48
0033ECA6  E9 22 FB FF FF                  jmp 0x14033e7cd
0033ECAB  49 81 FE A0 00 00 00            cmp r14, 0xa0
0033ECB2  0F 84 B1 02 00 00               je 0x14033ef69
0033ECB8  49 81 FE 20 04 00 00            cmp r14, 0x420
0033ECBF  0F 84 6F 02 00 00               je 0x14033ef34
0033ECC5  49 83 FE 22                     cmp r14, 0x22
0033ECC9  0F 84 14 02 00 00               je 0x14033eee3
0033ECCF  49 81 FE 20 01 00 00            cmp r14, 0x120
0033ECD6  0F 85 04 F7 FF FF               jne 0x14033e3e0
0033ECDC  BA 01 00 00 00                  mov edx, 1
0033ECE1  49 8B CA                        mov rcx, r10
0033ECE4  E8 F7 CA 07 00                  call 0x1403bb7e0
0033ECE9  E9 2F 02 00 00                  jmp 0x14033ef1d
0033ECEE  41 8B 46 20                     mov eax, dword ptr [r14 + 0x20]
0033ECF2  C1 E8 18                        shr eax, 0x18
0033ECF5  A8 08                           test al, 8
0033ECF7  0F 85 C8 FE FF FF               jne 0x14033ebc5
0033ECFD  49 8D 4F 20                     lea rcx, [r15 + 0x20]
0033ED01  E8 DA AA F0 FF                  call 0x1402497e0
0033ED06  4C 89 6F 58                     mov qword ptr [rdi + 0x58], r13
0033ED0A  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
0033ED0E  4C 8D 14 40                     lea r10, [rax + rax*2]
0033ED12  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
0033ED1C  49 C1 E2 04                     shl r10, 4
0033ED20  48 8B C0                        mov rax, rax
0033ED23  4C 03 D0                        add r10, rax
0033ED26  49 8B CA                        mov rcx, r10
0033ED29  E8 C2 39 FE FF                  call 0x1403226f0
0033ED2E  49 8B 4A 28                     mov rcx, qword ptr [r10 + 0x28]
0033ED32  48 8B 15 4F 13 AF 00            mov rdx, qword ptr [rip + 0xaf134f]
0033ED39  48 C1 E9 2B                     shr rcx, 0x2b
0033ED3D  81 E1 FF 03 00 00               and ecx, 0x3ff
0033ED43  8B C0                           mov eax, eax
0033ED45  48 8B 14 CA                     mov rdx, qword ptr [rdx + rcx*8]
0033ED49  48 6B C8 58                     imul rcx, rax, 0x58
0033ED4D  4C 8D BA C0 0C 00 00            lea r15, [rdx + 0xcc0]
0033ED54  48 89 54 24 38                  mov qword ptr [rsp + 0x38], rdx
0033ED59  4C 03 F9                        add r15, rcx
0033ED5C  49 8D 4F 20                     lea rcx, [r15 + 0x20]
0033ED60  E8 1B A1 F0 FF                  call 0x140248e80
0033ED65  49 8B D7                        mov rdx, r15
0033ED68  48 8B CF                        mov rcx, rdi
0033ED6B  E8 D8 6E 10 00                  call 0x140445c48
0033ED70  E9 73 F9 FF FF                  jmp 0x14033e6e8
0033ED75  44 0F 20 C0                     mov rax, cr8
0033ED79  4D 8D AA F8 41 00 00            lea r13, [r10 + 0x41f8]
0033ED80  49 8B CD                        mov rcx, r13
0033ED83  3C 02                           cmp al, 2
0033ED85  74 40                           je 0x14033edc7
0033ED87  E8 04 99 F0 FF                  call 0x140248690
0033ED8C  88 44 24 30                     mov byte ptr [rsp + 0x30], al
0033ED90  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
0033ED95  49 8B D4                        mov rdx, r12
0033ED98  E8 F7 8F 0C 00                  call 0x140407d94
0033ED9D  0F B6 54 24 30                  movzx edx, byte ptr [rsp + 0x30]
0033EDA2  49 8B CD                        mov rcx, r13
0033EDA5  4C 8B F0                        mov r14, rax
0033EDA8  E8 13 95 F0 FF                  call 0x1402482c0
0033EDAD  4D 85 F6                        test r14, r14
0033EDB0  0F 84 C1 FB FF FF               je 0x14033e977
0033EDB6  4C 8B 54 24 38                  mov r10, qword ptr [rsp + 0x38]
0033EDBB  48 8D 0D 3E 9F AF 00            lea rcx, [rip + 0xaf9f3e]
0033EDC2  E9 43 FB FF FF                  jmp 0x14033e90a
0033EDC7  C6 44 24 30 11                  mov byte ptr [rsp + 0x30], 0x11
0033EDCC  E8 AF A0 F0 FF                  call 0x140248e80
0033EDD1  EB BD                           jmp 0x14033ed90
0033EDD3  48 81 F9 20 04 00 00            cmp rcx, 0x420
0033EDDA  44 0F 42 F2                     cmovb r14d, edx
0033EDDE  48 3D A0 00 00 00               cmp rax, 0xa0
0033EDE4  0F 82 AC 00 00 00               jb 0x14033ee96
0033EDEA  48 3D 20 01 00 00               cmp rax, 0x120
0033EDF0  0F 82 C4 00 00 00               jb 0x14033eeba
0033EDF6  45 85 F6                        test r14d, r14d
0033EDF9  0F 84 2A FD FF FF               je 0x14033eb29
0033EDFF  49 8D 8A 40 3F 00 00            lea rcx, [r10 + 0x3f40]
0033EE06  E8 75 A0 F0 FF                  call 0x140248e80
0033EE0B  41 F6 C6 01                     test r14b, 1
0033EE0F  74 1C                           je 0x14033ee2d
0033EE11  48 8B 7C 24 38                  mov rdi, qword ptr [rsp + 0x38]
0033EE16  45 33 C0                        xor r8d, r8d
0033EE19  33 D2                           xor edx, edx
0033EE1B  48 8D 8F 48 3F 00 00            lea rcx, [rdi + 0x3f48]
0033EE22  E8 E9 04 00 00                  call 0x14033f310
0033EE27  FF 87 60 3F 00 00               inc dword ptr [rdi + 0x3f60]
0033EE2D  41 F6 C6 02                     test r14b, 2
0033EE31  74 1C                           je 0x14033ee4f
0033EE33  48 8B 7C 24 38                  mov rdi, qword ptr [rsp + 0x38]
0033EE38  45 33 C0                        xor r8d, r8d
0033EE3B  33 D2                           xor edx, edx
0033EE3D  48 8D 8F 68 3F 00 00            lea rcx, [rdi + 0x3f68]
0033EE44  E8 C7 04 00 00                  call 0x14033f310
0033EE49  FF 87 80 3F 00 00               inc dword ptr [rdi + 0x3f80]
0033EE4F  41 F6 C6 04                     test r14b, 4
0033EE53  74 1C                           je 0x14033ee71
0033EE55  48 8B 7C 24 38                  mov rdi, qword ptr [rsp + 0x38]
0033EE5A  45 33 C0                        xor r8d, r8d
0033EE5D  33 D2                           xor edx, edx
0033EE5F  48 8D 8F 88 3F 00 00            lea rcx, [rdi + 0x3f88]
0033EE66  E8 A5 04 00 00                  call 0x14033f310
0033EE6B  FF 87 A0 3F 00 00               inc dword ptr [rdi + 0x3fa0]
0033EE71  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
0033EE76  48 81 C1 40 3F 00 00            add rcx, 0x3f40
0033EE7D  E8 5E A9 F0 FF                  call 0x1402497e0
0033EE82  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
0033EE87  4C 8B 54 24 38                  mov r10, qword ptr [rsp + 0x38]
0033EE8C  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
0033EE91  E9 93 FC FF FF                  jmp 0x14033eb29
0033EE96  41 8B D6                        mov edx, r14d
0033EE99  83 CA 02                        or edx, 2
0033EE9C  48 81 F9 A0 00 00 00            cmp rcx, 0xa0
0033EEA3  41 0F 42 D6                     cmovb edx, r14d
0033EEA7  44 8B F2                        mov r14d, edx
0033EEAA  48 83 F8 22                     cmp rax, 0x22
0033EEAE  73 0A                           jae 0x14033eeba
0033EEB0  48 83 F9 22                     cmp rcx, 0x22
0033EEB4  72 04                           jb 0x14033eeba
0033EEB6  41 83 CE 01                     or r14d, 1
0033EEBA  48 81 F9 20 01 00 00            cmp rcx, 0x120
0033EEC1  0F 82 2F FF FF FF               jb 0x14033edf6
0033EEC7  BA 01 00 00 00                  mov edx, 1
0033EECC  49 8B CA                        mov rcx, r10
0033EECF  E8 0C C9 07 00                  call 0x1403bb7e0
0033EED4  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
0033EED9  4C 8B 54 24 38                  mov r10, qword ptr [rsp + 0x38]
0033EEDE  E9 13 FF FF FF                  jmp 0x14033edf6
0033EEE3  B8 48 3F 00 00                  mov eax, 0x3f48
0033EEE8  49 8D B2 40 3F 00 00            lea rsi, [r10 + 0x3f40]
0033EEEF  48 8B CE                        mov rcx, rsi
0033EEF2  49 8D 3C 02                     lea rdi, [r10 + rax]
0033EEF6  E8 85 9F F0 FF                  call 0x140248e80
0033EEFB  45 33 C0                        xor r8d, r8d
0033EEFE  33 D2                           xor edx, edx
0033EF00  48 8B CF                        mov rcx, rdi
0033EF03  E8 08 04 00 00                  call 0x14033f310
0033EF08  FF 47 18                        inc dword ptr [rdi + 0x18]
0033EF0B  48 8B CE                        mov rcx, rsi
0033EF0E  E8 CD A8 F0 FF                  call 0x1402497e0
0033EF13  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
0033EF18  48 8B 74 24 58                  mov rsi, qword ptr [rsp + 0x58]
0033EF1D  4C 8B 54 24 38                  mov r10, qword ptr [rsp + 0x38]
0033EF22  E9 B9 F4 FF FF                  jmp 0x14033e3e0
0033EF27  49 8B CA                        mov rcx, r10
0033EF2A  E8 D5 D8 07 00                  call 0x1403bc804
0033EF2F  E9 C9 F4 FF FF                  jmp 0x14033e3fd
0033EF34  B8 88 3F 00 00                  mov eax, 0x3f88
0033EF39  EB AD                           jmp 0x14033eee8
0033EF3B  49 8B C6                        mov rax, r14
0033EF3E  4C 2B D8                        sub r11, rax
0033EF41  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0033EF46  49 C1 FB 04                     sar r11, 4
0033EF4A  BA 06 00 00 00                  mov edx, 6
0033EF4F  49 B8 AB AA AA AA AA AA AA AA   movabs r8, 0xaaaaaaaaaaaaaaab
0033EF59  4D 8B CA                        mov r9, r10
0033EF5C  4D 0F AF C3                     imul r8, r11
0033EF60  8D 4A 48                        lea ecx, [rdx + 0x48]
0033EF63  E8 F8 E6 1B 00                  call 0x1404fd660
0033EF68  CC                              int3
0033EF69  B8 68 3F 00 00                  mov eax, 0x3f68
0033EF6E  E9 75 FF FF FF                  jmp 0x14033eee8
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0033EABD(void)
{
    unsigned __int64 v_stack_p20;
    unsigned __int8 v_stack_p30;
    unsigned int v_stack_p34;
    unsigned __int64 v_stack_p38;
    unsigned int v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned int v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p68;

    v_stack_p50 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_r10 + 17600) + 24)));
}
```

## 5. (Beta) C Style

```c
void sub_0033EABD(void)
{
    uint64_t v_stack_p20;
    uint8_t v_stack_p30;
    uint32_t v_stack_p34;
    uint64_t v_stack_p38;
    uint32_t v_stack_p40;
    uint64_t v_stack_p48;
    uint32_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p68;

    v_stack_p50 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_r10 + 0x44C0) + 0x18)));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0033EABD&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
