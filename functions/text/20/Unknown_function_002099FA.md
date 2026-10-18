# sub_002099FA

- RVA: `0x002099FA`–`0x00209F76` (길이 `1,404` bytes)
- VA: `0x00000001402099FA`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D6A4`
- 디코드: `327`개 명령, `1,404/1,404` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **26**; 고유 호출 대상: **15**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x00209A65` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00209A96` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x00209AA6` → [KiDeliverApc](../25/KiDeliverApc_function_00250F20.md) (function, `0x00250F20`)
- `0x00209AD6` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00209AE5` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00209B29` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x00209B37` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x00209B79` → [Feature_StackingDecayBoosts__private_IsEnabledNoReportingNoInline](../4E/Feature_StackingDecayBoosts__private_IsEnabledNoReportingNoInline_function_004EF7C0.md) (function, `0x004EF7C0`)
- `0x00209BFD` → [KiSetPriorityThread](../22/KiSetPriorityThread_function_00220E78.md) (function, `0x00220E78`)
- `0x00209C17` → [KiComputeThreadPriorityNonStacking](../5C/KiComputeThreadPriorityNonStacking_function_005CA81C.md) (function, `0x005CA81C`)
- `0x00209C3F` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00209C4E` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00209C64` → [KiProcessDeferredReadyList](../25/KiProcessDeferredReadyList_function_00250800.md) (function, `0x00250800`)
- `0x00209C85` → [KiProcessDeferredReadyList](../25/KiProcessDeferredReadyList_function_00250800.md) (function, `0x00250800`)
- `0x00209CA0` → [KiExitThreadWaitReschedule](../35/KiExitThreadWaitReschedule_function_00352EC8.md) (function, `0x00352EC8`)
- `0x00209CC0` → [KiProcessDeferredReadyList](../25/KiProcessDeferredReadyList_function_00250800.md) (function, `0x00250800`)
- `0x00209CCC` → [KiDeliverApc](../25/KiDeliverApc_function_00250F20.md) (function, `0x00250F20`)
- `0x00209CE0` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x00209CEE` → [KeDisableInterrupts](../21/KeDisableInterrupts_function_00217BE0.md) (function, `0x00217BE0`)
- `0x00209D68` → [KeDisableInterrupts](../21/KeDisableInterrupts_function_00217BE0.md) (function, `0x00217BE0`)
- `0x00209DED` → [KeDisableInterrupts](../21/KeDisableInterrupts_function_00217BE0.md) (function, `0x00217BE0`)
- `0x00209E3C` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x00209E94` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x00209EB9` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x00209F1C` → [KiSrcuReportQuiescent](../5C/KiSrcuReportQuiescent_function_005C2C08.md) (function, `0x005C2C08`)
- `0x00209F35` → [KiSrcuFlushCompleted](../5C/KiSrcuFlushCompleted_function_005C22B4.md) (function, `0x005C22B4`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00209A1B` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x00209A87` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x00209AC8` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x00209F58` → RVA `0x00F210E8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **25**
  - `0x00209A07` → [sub_002098FF + 0x5D](Unknown_function_002098FF.md) (`tail-transfer`)
  - `0x00209A73` → [sub_0020959D + 0x118](Unknown_function_0020959D.md) (`tail-transfer`)
  - `0x00209A7D` → [sub_0020959D + 0x118](Unknown_function_0020959D.md) (`tail-transfer`)
  - `0x00209AC3` → [sub_0020959D + 0xCC](Unknown_function_0020959D.md) (`tail-transfer`)
  - `0x00209AD0` → [sub_00209822 + 0xE](Unknown_function_00209822.md) (`tail-transfer`)
  - `0x00209ADD` → [sub_00209822 + 0xE](Unknown_function_00209822.md) (`tail-transfer`)
  - `0x00209AEA` → [sub_00209822 + 0x10](Unknown_function_00209822.md) (`tail-transfer`)
  - `0x00209B11` → [sub_0020959D + 0xAF](Unknown_function_0020959D.md) (`tail-transfer`)
  - `0x00209B20` → [sub_0020959D + 0x19B](Unknown_function_0020959D.md) (`tail-transfer`)
  - `0x00209C0D` → [sub_0020959D + 0x21E](Unknown_function_0020959D.md) (`tail-transfer`)
  - `0x00209C69` → [sub_0020959D + 0x256](Unknown_function_0020959D.md) (`tail-transfer`)
  - `0x00209C8C` → [sub_0020959D + 0x269](Unknown_function_0020959D.md) (`tail-transfer`)
  - `0x00209CA5` → [sub_0020959D + 0x256](Unknown_function_0020959D.md) (`tail-transfer`)
  - `0x00209CB3` → [sub_0020959D + 0x19B](Unknown_function_0020959D.md) (`tail-transfer`)
  - `0x00209CE9` → [sub_0020959D + 0x256](Unknown_function_0020959D.md) (`tail-transfer`)
  - `0x00209D4D` → [sub_0020959D + 0x71](Unknown_function_0020959D.md) (`tail-transfer`)
  - `0x00209DE7` → [sub_0020959D + 0x7E](Unknown_function_0020959D.md) (`tail-transfer`)
  - `0x00209E01` → [sub_0020959D + 0x7E](Unknown_function_0020959D.md) (`tail-transfer`)
  - `0x00209E1D` → [sub_0020959D + 0x7E](Unknown_function_0020959D.md) (`tail-transfer`)
  - `0x00209E59` → [sub_0020959D + 0x71](Unknown_function_0020959D.md) (`tail-transfer`)
  - `0x00209E75` → [sub_0020959D + 0x71](Unknown_function_0020959D.md) (`tail-transfer`)
  - `0x00209EC6` → [sub_0020959D + 0x71](Unknown_function_0020959D.md) (`tail-transfer`)
  - `0x00209EE8` → [sub_006D662C](../6D/Unknown_function_006D662C.md) (`tail-transfer`)
  - `0x00209F23` → [sub_0020959D + 0x71](Unknown_function_0020959D.md) (`tail-transfer`)
  - `0x00209F3A` → [sub_0020959D + 0x71](Unknown_function_0020959D.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002099FA  48 B9 14 00 00 00 80 F7 FF FF   movabs rcx, 0xfffff78000000014
00209A04  48 8B 09                        mov rcx, qword ptr [rcx]
00209A07  E9 50 FF FF FF                  jmp 0x14020995c
00209A0C  41 8B F7                        mov esi, r15d
00209A0F  90                              nop
00209A10  F0 48 0F BA 6F 40 00            lock bts qword ptr [rdi + 0x40], 0
00209A17  73 1B                           jae 0x140209a34
00209A19  FF C6                           inc esi
00209A1B  85 35 8B B8 DB 00               test dword ptr [rip + 0xdbb88b], esi
00209A21  0F 84 0A 02 00 00               je 0x140209c31
00209A27  F3 90                           pause
00209A29  48 8B 47 40                     mov rax, qword ptr [rdi + 0x40]
00209A2D  48 85 C0                        test rax, rax
00209A30  74 DE                           je 0x140209a10
00209A32  EB E5                           jmp 0x140209a19
00209A34  48 0F BE 97 1B 03 00 00         movsx rdx, byte ptr [rdi + 0x31b]
00209A3C  4C 8B C2                        mov r8, rdx
00209A3F  48 8D 0C 3A                     lea rcx, [rdx + rdi]
00209A43  0F B6 81 38 03 00 00            movzx eax, byte ptr [rcx + 0x338]
00209A4A  84 C0                           test al, al
00209A4C  0F 85 EC 00 00 00               jne 0x140209b3e
00209A52  41 B9 02 00 00 00               mov r9d, 2
00209A58  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00209A5D  48 8B D7                        mov rdx, rdi
00209A60  B9 57 01 00 00                  mov ecx, 0x157
00209A65  E8 F6 3B 2F 00                  call 0x1404fd660
00209A6A  CC                              int3
00209A6B  66 44 39 BF E6 01 00 00         cmp word ptr [rdi + 0x1e6], r15w
00209A73  0F 85 3C FC FF FF               jne 0x1402096b5
00209A79  41 80 FD 01                     cmp r13b, 1
00209A7D  0F 83 32 FC FF FF               jae 0x1402096b5
00209A83  4C 89 7F 40                     mov qword ptr [rdi + 0x40], r15
00209A87  44 39 3D 92 D2 DB 00            cmp dword ptr [rip + 0xdbd292], r15d
00209A8E  74 0B                           je 0x140209a9b
00209A90  44 0F 20 C1                     mov rcx, cr8
00209A94  B2 01                           mov dl, 1
00209A96  E8 FD BB 2E 00                  call 0x1404f5698
00209A9B  44 0F 22 C3                     mov cr8, rbx
00209A9F  45 33 C0                        xor r8d, r8d
00209AA2  33 D2                           xor edx, edx
00209AA4  33 C9                           xor ecx, ecx
00209AA6  E8 75 74 04 00                  call 0x140250f20
00209AAB  44 0F 20 C1                     mov rcx, cr8
00209AAF  45 0F 22 C4                     mov cr8, r12
00209AB3  44 39 3D 66 D2 DB 00            cmp dword ptr [rip + 0xdbd266], r15d
00209ABA  75 69                           jne 0x140209b25
00209ABC  44 88 AF 86 01 00 00            mov byte ptr [rdi + 0x186], r13b
00209AC3  E9 A1 FB FF FF                  jmp 0x140209669
00209AC8  8B 05 EA CF DB 00               mov eax, dword ptr [rip + 0xdbcfea]
00209ACE  A8 40                           test al, 0x40
00209AD0  0F 84 5A FD FF FF               je 0x140209830
00209AD6  E8 B5 59 10 00                  call 0x14030f490
00209ADB  84 C0                           test al, al
00209ADD  0F 84 4D FD FF FF               je 0x140209830
00209AE3  8B CE                           mov ecx, esi
00209AE5  E8 76 59 10 00                  call 0x14030f460
00209AEA  E9 43 FD FF FF                  jmp 0x140209832
00209AEF  44 0F 20 C6                     mov rsi, cr8
00209AF3  B8 02 00 00 00                  mov eax, 2
00209AF8  44 0F 22 C0                     mov cr8, rax
00209AFC  44 39 3D 1D D2 DB 00            cmp dword ptr [rip + 0xdbd21d], r15d
00209B03  75 2B                           jne 0x140209b30
00209B05  40 88 B7 86 01 00 00            mov byte ptr [rdi + 0x186], sil
00209B0C  BB 01 00 00 00                  mov ebx, 1
00209B11  E9 36 FB FF FF                  jmp 0x14020964c
00209B16  44 88 7C 3D 72                  mov byte ptr [rbp + rdi + 0x72], r15b
00209B1B  BE 01 01 00 00                  mov esi, 0x101
00209B20  E9 13 FC FF FF                  jmp 0x140209738
00209B25  41 0F B6 D4                     movzx edx, r12b
00209B29  E8 CE BB 2E 00                  call 0x1404f56fc
00209B2E  EB 8C                           jmp 0x140209abc
00209B30  0F B6 D0                        movzx edx, al
00209B33  40 0F B6 CE                     movzx ecx, sil
00209B37  E8 C0 BB 2E 00                  call 0x1404f56fc
00209B3C  EB C7                           jmp 0x140209b05
00209B3E  2C 01                           sub al, 1
00209B40  88 81 38 03 00 00               mov byte ptr [rcx + 0x338], al
00209B46  0F 85 B6 00 00 00               jne 0x140209c02
00209B4C  8B 87 58 03 00 00               mov eax, dword ptr [rdi + 0x358]
00209B52  8B CA                           mov ecx, edx
00209B54  0F BB D0                        btc eax, edx
00209B57  BA 01 00 00 00                  mov edx, 1
00209B5C  D3 E2                           shl edx, cl
00209B5E  89 87 58 03 00 00               mov dword ptr [rdi + 0x358], eax
00209B64  3B C2                           cmp eax, edx
00209B66  0F 83 96 00 00 00               jae 0x140209c02
00209B6C  80 BF C3 00 00 00 1F            cmp byte ptr [rdi + 0xc3], 0x1f
00209B73  0F 8F 89 00 00 00               jg 0x140209c02
00209B79  E8 42 5C 2E 00                  call 0x1404ef7c0
00209B7E  85 C0                           test eax, eax
00209B80  0F 84 8C 00 00 00               je 0x140209c12
00209B86  44 0F BE 87 33 02 00 00         movsx r8d, byte ptr [rdi + 0x233]
00209B8E  45 8B D0                        mov r10d, r8d
00209B91  45 8B C8                        mov r9d, r8d
00209B94  41 83 F8 10                     cmp r8d, 0x10
00209B98  7D 45                           jge 0x140209bdf
00209B9A  0F B6 8F 66 03 00 00            movzx ecx, byte ptr [rdi + 0x366]
00209BA1  0F B7 97 06 02 00 00            movzx edx, word ptr [rdi + 0x206]
00209BA8  8B C2                           mov eax, edx
00209BAA  83 E0 0F                        and eax, 0xf
00209BAD  41 03 C0                        add eax, r8d
00209BB0  41 3B C1                        cmp eax, r9d
00209BB3  44 8B C0                        mov r8d, eax
00209BB6  41 8B C7                        mov eax, r15d
00209BB9  45 0F 4E C1                     cmovle r8d, r9d
00209BBD  84 C9                           test cl, cl
00209BBF  0F 4F C1                        cmovg eax, ecx
00209BC2  0F BE C0                        movsx eax, al
00209BC5  44 03 C0                        add r8d, eax
00209BC8  41 83 F8 10                     cmp r8d, 0x10
00209BCC  0F 8D 99 03 00 00               jge 0x140209f6b
00209BD2  C1 EA 04                        shr edx, 4
00209BD5  0F B6 C2                        movzx eax, dl
00209BD8  41 3B C0                        cmp eax, r8d
00209BDB  44 0F 4F C0                     cmovg r8d, eax
00209BDF  8B 87 58 03 00 00               mov eax, dword ptr [rdi + 0x358]
00209BE5  85 C0                           test eax, eax
00209BE7  75 38                           jne 0x140209c21
00209BE9  0F BE 87 C3 00 00 00            movsx eax, byte ptr [rdi + 0xc3]
00209BF0  44 3B C0                        cmp r8d, eax
00209BF3  7D 0D                           jge 0x140209c02
00209BF5  48 8D 54 24 40                  lea rdx, [rsp + 0x40]
00209BFA  48 8B CF                        mov rcx, rdi
00209BFD  E8 76 72 01 00                  call 0x140220e78
00209C02  C6 87 1B 03 00 00 20            mov byte ptr [rdi + 0x31b], 0x20
00209C09  4C 89 7F 40                     mov qword ptr [rdi + 0x40], r15
00209C0D  E9 A9 FB FF FF                  jmp 0x1402097bb
00209C12  33 D2                           xor edx, edx
00209C14  48 8B CF                        mov rcx, rdi
00209C17  E8 00 0C 3C 00                  call 0x1405ca81c
00209C1C  44 8B C0                        mov r8d, eax
00209C1F  EB C8                           jmp 0x140209be9
00209C21  0F BD C0                        bsr eax, eax
00209C24  44 3B C0                        cmp r8d, eax
00209C27  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
00209C2B  44 0F 4C C0                     cmovl r8d, eax
00209C2F  EB B8                           jmp 0x140209be9
00209C31  8B 05 81 CE DB 00               mov eax, dword ptr [rip + 0xdbce81]
00209C37  A8 40                           test al, 0x40
00209C39  0F 84 E8 FD FF FF               je 0x140209a27
00209C3F  E8 4C 58 10 00                  call 0x14030f490
00209C44  84 C0                           test al, al
00209C46  0F 84 DB FD FF FF               je 0x140209a27
00209C4C  8B CE                           mov ecx, esi
00209C4E  E8 0D 58 10 00                  call 0x14030f460
00209C53  E9 D1 FD FF FF                  jmp 0x140209a29
00209C58  44 0F B6 C7                     movzx r8d, dil
00209C5C  48 8D 54 24 40                  lea rdx, [rsp + 0x40]
00209C61  48 8B CD                        mov rcx, rbp
00209C64  E8 97 6B 04 00                  call 0x140250800
00209C69  E9 85 FB FF FF                  jmp 0x1402097f3
00209C6E  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
00209C77  48 8D 54 24 50                  lea rdx, [rsp + 0x50]
00209C7C  44 0F B6 84 24 B8 00 00 00      movzx r8d, byte ptr [rsp + 0xb8]
00209C85  E8 76 6B 04 00                  call 0x140250800
00209C8A  8B C6                           mov eax, esi
00209C8C  E9 75 FB FF FF                  jmp 0x140209806
00209C91  48 8B CD                        mov rcx, rbp
00209C94  A8 18                           test al, 0x18
00209C96  74 20                           je 0x140209cb8
00209C98  4C 8D 44 24 40                  lea r8, [rsp + 0x40]
00209C9D  48 8B D7                        mov rdx, rdi
00209CA0  E8 23 92 14 00                  call 0x140352ec8
00209CA5  E9 49 FB FF FF                  jmp 0x1402097f3
00209CAA  44 88 7F 72                     mov byte ptr [rdi + 0x72], r15b
00209CAE  BE 01 01 00 00                  mov esi, 0x101
00209CB3  E9 80 FA FF FF                  jmp 0x140209738
00209CB8  41 B0 01                        mov r8b, 1
00209CBB  48 8D 54 24 40                  lea rdx, [rsp + 0x40]
00209CC0  E8 3B 6B 04 00                  call 0x140250800
00209CC5  45 33 C0                        xor r8d, r8d
00209CC8  33 D2                           xor edx, edx
00209CCA  33 C9                           xor ecx, ecx
00209CCC  E8 4F 72 04 00                  call 0x140250f20
00209CD1  44 39 3D 48 D0 DB 00            cmp dword ptr [rip + 0xdbd048], r15d
00209CD8  74 0B                           je 0x140209ce5
00209CDA  44 0F 20 C1                     mov rcx, cr8
00209CDE  33 D2                           xor edx, edx
00209CE0  E8 B3 B9 2E 00                  call 0x1404f5698
00209CE5  45 0F 22 C7                     mov cr8, r15
00209CE9  E9 05 FB FF FF                  jmp 0x1402097f3
00209CEE  E8 ED DE 00 00                  call 0x140217be0
00209CF3  4C 8B AE F8 38 00 00            mov r13, qword ptr [rsi + 0x38f8]
00209CFA  44 0F B6 C8                     movzx r9d, al
00209CFE  4D 85 ED                        test r13, r13
00209D01  0F 84 BC 01 00 00               je 0x140209ec3
00209D07  4D 8D 45 F8                     lea r8, [r13 - 8]
00209D0B  49 8B 45 00                     mov rax, qword ptr [r13]
00209D0F  4C 89 84 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], r8
00209D17  4D 39 38                        cmp qword ptr [r8], r15
00209D1A  0F 85 CD 01 00 00               jne 0x140209eed
00209D20  49 3B C5                        cmp rax, r13
00209D23  75 7A                           jne 0x140209d9f
00209D25  4C 89 BE F8 38 00 00            mov qword ptr [rsi + 0x38f8], r15
00209D2C  49 8B 40 38                     mov rax, qword ptr [r8 + 0x38]
00209D30  4D 89 7D 00                     mov qword ptr [r13], r15
00209D34  48 8B 40 38                     mov rax, qword ptr [rax + 0x38]
00209D38  49 89 40 18                     mov qword ptr [r8 + 0x18], rax
00209D3C  45 84 C9                        test r9b, r9b
00209D3F  0F 85 80 00 00 00               jne 0x140209dc5
00209D45  4D 8B 48 18                     mov r9, qword ptr [r8 + 0x18]
00209D49  4D 3B 48 20                     cmp r9, qword ptr [r8 + 0x20]
00209D4D  0F 84 BB F8 FF FF               je 0x14020960e
00209D53  49 8B 40 30                     mov rax, qword ptr [r8 + 0x30]
00209D57  49 8B 50 28                     mov rdx, qword ptr [r8 + 0x28]
00209D5B  48 8B 08                        mov rcx, qword ptr [rax]
00209D5E  48 85 4A 28                     test qword ptr [rdx + 0x28], rcx
00209D62  0F 84 AE 01 00 00               je 0x140209f16
00209D68  E8 73 DE 00 00                  call 0x140217be0
00209D6D  44 0F B6 C0                     movzx r8d, al
00209D71  4D 39 7D 00                     cmp qword ptr [r13], r15
00209D75  0F 85 DB 00 00 00               jne 0x140209e56
00209D7B  48 8B 8E F8 38 00 00            mov rcx, qword ptr [rsi + 0x38f8]
00209D82  48 85 C9                        test rcx, rcx
00209D85  0F 84 77 01 00 00               je 0x140209f02
00209D8B  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
00209D8F  48 39 08                        cmp qword ptr [rax], rcx
00209D92  0F 84 AF 00 00 00               je 0x140209e47
00209D98  B9 03 00 00 00                  mov ecx, 3
00209D9D  CD 29                           int 0x29
00209D9F  48 89 86 F8 38 00 00            mov qword ptr [rsi + 0x38f8], rax
00209DA6  49 8B 4D 00                     mov rcx, qword ptr [r13]
00209DAA  49 8B 45 08                     mov rax, qword ptr [r13 + 8]
00209DAE  4C 39 69 08                     cmp qword ptr [rcx + 8], r13
00209DB2  75 E4                           jne 0x140209d98
00209DB4  4C 39 28                        cmp qword ptr [rax], r13
00209DB7  75 DF                           jne 0x140209d98
00209DB9  48 89 08                        mov qword ptr [rax], rcx
00209DBC  48 89 41 08                     mov qword ptr [rcx + 8], rax
00209DC0  E9 67 FF FF FF                  jmp 0x140209d2c
00209DC5  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
00209DCE  4C 8B 89 B8 8E 00 00            mov r9, qword ptr [rcx + 0x8eb8]
00209DD5  4D 85 C9                        test r9, r9
00209DD8  75 48                           jne 0x140209e22
00209DDA  FB                              sti
00209DDB  E9 65 FF FF FF                  jmp 0x140209d45
00209DE0  44 39 BE E0 38 00 00            cmp dword ptr [rsi + 0x38e0], r15d
00209DE7  0F 85 2E F8 FF FF               jne 0x14020961b
00209DED  E8 EE DD 00 00                  call 0x140217be0
00209DF2  44 38 BE E5 38 00 00            cmp byte ptr [rsi + 0x38e5], r15b
00209DF9  0F 85 40 01 00 00               jne 0x140209f3f
00209DFF  84 C0                           test al, al
00209E01  0F 84 14 F8 FF FF               je 0x14020961b
00209E07  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
00209E10  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
00209E17  4D 85 C0                        test r8, r8
00209E1A  75 7F                           jne 0x140209e9b
00209E1C  FB                              sti
00209E1D  E9 F9 F7 FF FF                  jmp 0x14020961b
00209E22  41 0F 0D 09                     prefetchw byte ptr [r9]
00209E26  41 8B 01                        mov eax, dword ptr [r9]
00209E29  8B D0                           mov edx, eax
00209E2B  0F BA F2 15                     btr edx, 0x15
00209E2F  F0 41 0F B1 11                  lock cmpxchg dword ptr [r9], edx
00209E34  75 F3                           jne 0x140209e29
00209E36  0F BA E0 15                     bt eax, 0x15
00209E3A  73 9E                           jae 0x140209dda
00209E3C  E8 8F 93 05 00                  call 0x1402631d0
00209E41  4D 8D 45 F8                     lea r8, [r13 - 8]
00209E45  EB 93                           jmp 0x140209dda
00209E47  49 89 4D 00                     mov qword ptr [r13], rcx
00209E4B  49 89 45 08                     mov qword ptr [r13 + 8], rax
00209E4F  4C 89 28                        mov qword ptr [rax], r13
00209E52  4C 89 69 08                     mov qword ptr [rcx + 8], r13
00209E56  45 84 C0                        test r8b, r8b
00209E59  0F 84 AF F7 FF FF               je 0x14020960e
00209E5F  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
00209E68  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
00209E6F  4D 85 C0                        test r8, r8
00209E72  75 06                           jne 0x140209e7a
00209E74  FB                              sti
00209E75  E9 94 F7 FF FF                  jmp 0x14020960e
00209E7A  41 0F 0D 08                     prefetchw byte ptr [r8]
00209E7E  41 8B 00                        mov eax, dword ptr [r8]
00209E81  8B D0                           mov edx, eax
00209E83  0F BA F2 15                     btr edx, 0x15
00209E87  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
00209E8C  75 F3                           jne 0x140209e81
00209E8E  0F BA E0 15                     bt eax, 0x15
00209E92  73 E0                           jae 0x140209e74
00209E94  E8 37 93 05 00                  call 0x1402631d0
00209E99  EB D9                           jmp 0x140209e74
00209E9B  41 0F 0D 08                     prefetchw byte ptr [r8]
00209E9F  41 8B 00                        mov eax, dword ptr [r8]
00209EA2  8B D0                           mov edx, eax
00209EA4  0F BA F2 15                     btr edx, 0x15
00209EA8  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
00209EAD  75 F3                           jne 0x140209ea2
00209EAF  0F BA E0 15                     bt eax, 0x15
00209EB3  0F 83 63 FF FF FF               jae 0x140209e1c
00209EB9  E8 12 93 05 00                  call 0x1402631d0
00209EBE  E9 59 FF FF FF                  jmp 0x140209e1c
00209EC3  45 84 C9                        test r9b, r9b
00209EC6  0F 84 42 F7 FF FF               je 0x14020960e
00209ECC  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
00209ED5  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
00209EDC  4D 85 C0                        test r8, r8
00209EDF  74 93                           je 0x140209e74
00209EE1  41 0F 0D 08                     prefetchw byte ptr [r8]
00209EE5  41 8B 00                        mov eax, dword ptr [r8]
00209EE8  E9 3F C7 4C 00                  jmp 0x1406d662c
00209EED  4C 3B E8                        cmp r13, rax
00209EF0  0F 84 46 FE FF FF               je 0x140209d3c
00209EF6  48 89 86 F8 38 00 00            mov qword ptr [rsi + 0x38f8], rax
00209EFD  E9 3A FE FF FF                  jmp 0x140209d3c
00209F02  4D 89 6D 08                     mov qword ptr [r13 + 8], r13
00209F06  4D 89 6D 00                     mov qword ptr [r13], r13
00209F0A  4C 89 AE F8 38 00 00            mov qword ptr [rsi + 0x38f8], r13
00209F11  E9 40 FF FF FF                  jmp 0x140209e56
00209F16  49 8B D1                        mov rdx, r9
00209F19  49 8B C8                        mov rcx, r8
00209F1C  E8 E7 8C 3B 00                  call 0x1405c2c08
00209F21  85 C0                           test eax, eax
00209F23  0F 84 E5 F6 FF FF               je 0x14020960e
00209F29  48 8B 8C 24 B8 00 00 00         mov rcx, qword ptr [rsp + 0xb8]
00209F31  48 8B 49 38                     mov rcx, qword ptr [rcx + 0x38]
00209F35  E8 7A 83 3B 00                  call 0x1405c22b4
00209F3A  E9 CF F6 FF FF                  jmp 0x14020960e
00209F3F  44 39 BE E0 38 00 00            cmp dword ptr [rsi + 0x38e0], r15d
00209F46  0F 85 B3 FE FF FF               jne 0x140209dff
00209F4C  44 88 BE E5 38 00 00            mov byte ptr [rsi + 0x38e5], r15b
00209F53  F0 44 09 3C 24                  lock or dword ptr [rsp], r15d
00209F58  48 8B 0D 89 71 D1 00            mov rcx, qword ptr [rip + 0xd17189]
00209F5F  48 89 8E E8 38 00 00            mov qword ptr [rsi + 0x38e8], rcx
00209F66  E9 94 FE FF FF                  jmp 0x140209dff
00209F6B  41 B8 0F 00 00 00               mov r8d, 0xf
00209F71  E9 5C FC FF FF                  jmp 0x140209bd2
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_002099FA(void)
{
    unsigned int v_stack_p0;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p50;
    unsigned __int8 v_stack_pB8;
}
```

## 5. (Beta) C Style

```c
void sub_002099FA(void)
{
    uint32_t v_stack_p0;
    uint64_t v_stack_p20;
    uint32_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p50;
    uint8_t v_stack_pB8;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002099FA&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
