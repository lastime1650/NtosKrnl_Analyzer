# MiProtectEnclavePages

- RVA: `0x004D5528`–`0x004D5B34` (길이 `1,548` bytes)
- VA: `0x00000001404D5528`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BE28C`
- 디코드: `380`개 명령, `1,548/1,548` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **27**; 고유 호출 대상: **20**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x004D55BB` → [VslDebugProtectSecureProcessMemory](../../page/AD/VslDebugProtectSecureProcessMemory_function_00AD9580.md) (function, `0x00AD9580`)
- `0x004D574C` → [MiMakeValidPte](../2C/MiMakeValidPte_function_002C5590.md) (function, `0x002C5590`)
- `0x004D5757` → [MiLockWorkingSetShared](../27/MiLockWorkingSetShared_function_0027CBF0.md) (function, `0x0027CBF0`)
- `0x004D57A3` → [MiWorkingSetIsContended](../2A/MiWorkingSetIsContended_function_002AE520.md) (function, `0x002AE520`)
- `0x004D57AC` → [KeShouldYieldProcessor](../27/KeShouldYieldProcessor_function_002773E0.md) (function, `0x002773E0`)
- `0x004D57C0` → [MiPageTableLockIsContended](../2A/MiPageTableLockIsContended_function_002AE650.md) (function, `0x002AE650`)
- `0x004D57D4` → [MiFlushEnclaveTb](../68/MiFlushEnclaveTb_function_00686E10.md) (function, `0x00686E10`)
- `0x004D57ED` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x004D57FC` → [MiUnlockWorkingSetShared](../27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)
- `0x004D5804` → [MiLockWorkingSetShared](../27/MiLockWorkingSetShared_function_0027CBF0.md) (function, `0x0027CBF0`)
- `0x004D582A` → [MiFlushEnclaveTb](../68/MiFlushEnclaveTb_function_00686E10.md) (function, `0x00686E10`)
- `0x004D5843` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x004D588A` → [MiMakeSystemAddressValid](../27/MiMakeSystemAddressValid_function_0027FF70.md) (function, `0x0027FF70`)
- `0x004D589F` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x004D5900` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x004D5937` → [MiUpdateEnclavePfnProtection](../68/MiUpdateEnclavePfnProtection_function_00687128.md) (function, `0x00687128`)
- `0x004D596E` → [MiWriteEnclavePte](../36/MiWriteEnclavePte_function_00368570.md) (function, `0x00368570`)
- `0x004D598E` → [MI_TIGHTER_PERMISSIONS](../38/MI_TIGHTER_PERMISSIONS_function_00384C30.md) (function, `0x00384C30`)
- `0x004D599C` → [MiGetProcessorFlushList](../24/MiGetProcessorFlushList_function_00242C90.md) (function, `0x00242C90`)
- `0x004D59BE` → [MiInitializeTbFlushList](../29/MiInitializeTbFlushList_function_00294F00.md) (function, `0x00294F00`)
- `0x004D59D2` → [MiInsertTbFlushEntry](../29/MiInsertTbFlushEntry_function_00293670.md) (function, `0x00293670`)
- `0x004D5A02` → [KeCanChangeEnclavePageProtection](../5B/KeCanChangeEnclavePageProtection_function_005BB9E0.md) (function, `0x005BB9E0`)
- `0x004D5A23` → [MiFlushEnclaveTb](../68/MiFlushEnclaveTb_function_00686E10.md) (function, `0x00686E10`)
- `0x004D5A38` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x004D5A44` → [MiUnlockWorkingSetShared](../27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)
- `0x004D5AA5` → [KeChangeEnclavePageProtection](../5B/KeChangeEnclavePageProtection_function_005BBAA0.md) (function, `0x005BBAA0`)
- `0x004D5AD2` → [KeTrackEnclaveTbFlush](../5B/KeTrackEnclaveTbFlush_function_005BBC94.md) (function, `0x005BBC94`)

### Direct callers
- [sub_00B18CEA](../../page/B1/Unknown_function_00B18CEA.md) at `0x00B18D44`

### Static image references
- `0x004D5973` → RVA `0x00FC6A88` (`ALMOSTRO`; read)
- `0x004D5A52` → RVA `0x00014630` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x004D55BB` → [VslDebugProtectSecureProcessMemory](../../page/AD/VslDebugProtectSecureProcessMemory_function_00AD9580.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004D5528  4C 8B DC                        mov r11, rsp
004D552B  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
004D552F  4D 89 4B 20                     mov qword ptr [r11 + 0x20], r9
004D5533  4D 89 43 18                     mov qword ptr [r11 + 0x18], r8
004D5537  55                              push rbp
004D5538  56                              push rsi
004D5539  57                              push rdi
004D553A  41 54                           push r12
004D553C  41 55                           push r13
004D553E  41 56                           push r14
004D5540  41 57                           push r15
004D5542  48 81 EC 80 00 00 00            sub rsp, 0x80
004D5549  41 8B 40 40                     mov eax, dword ptr [r8 + 0x40]
004D554D  4D 8B F9                        mov r15, r9
004D5550  A8 01                           test al, 1
004D5552  0F 85 9B 00 00 00               jne 0x1404d55f3
004D5558  4C 8B 94 24 E0 00 00 00         mov r10, qword ptr [rsp + 0xe0]
004D5560  49 8B 40 48                     mov rax, qword ptr [r8 + 0x48]
004D5564  4D 2B D1                        sub r10, r9
004D5567  49 FF C2                        inc r10
004D556A  4D 89 53 18                     mov qword ptr [r11 + 0x18], r10
004D556E  80 78 4C 00                     cmp byte ptr [rax + 0x4c], 0
004D5572  74 1F                           je 0x1404d5593
004D5574  F7 84 24 F8 00 00 00 00 00 00 20  test dword ptr [rsp + 0xf8], 0x20000000
004D557F  74 12                           je 0x1404d5593
004D5581  48 8B 84 24 00 01 00 00         mov rax, qword ptr [rsp + 0x100]
004D5589  C7 00 04 00 00 00               mov dword ptr [rax], 4
004D558F  33 C0                           xor eax, eax
004D5591  EB 45                           jmp 0x1404d55d8
004D5593  48 8B 84 24 00 01 00 00         mov rax, qword ptr [rsp + 0x100]
004D559B  4C 8D 8C 24 D0 00 00 00         lea r9, [rsp + 0xd0]
004D55A3  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
004D55A8  4C 8D 84 24 D8 00 00 00         lea r8, [rsp + 0xd8]
004D55B0  8B 84 24 E8 00 00 00            mov eax, dword ptr [rsp + 0xe8]
004D55B7  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
004D55BB  E8 C0 3F 60 00                  call 0x140ad9580
004D55C0  85 C0                           test eax, eax
004D55C2  0F 88 B0 00 00 00               js 0x1404d5678
004D55C8  4C 8B BC 24 D8 00 00 00         mov r15, qword ptr [rsp + 0xd8]
004D55D0  4C 8B 94 24 D0 00 00 00         mov r10, qword ptr [rsp + 0xd0]
004D55D8  48 8B 8C 24 08 01 00 00         mov rcx, qword ptr [rsp + 0x108]
004D55E0  4C 89 39                        mov qword ptr [rcx], r15
004D55E3  48 8B 8C 24 10 01 00 00         mov rcx, qword ptr [rsp + 0x110]
004D55EB  4C 89 11                        mov qword ptr [rcx], r10
004D55EE  E9 85 00 00 00                  jmp 0x1404d5678
004D55F3  8B B4 24 F8 00 00 00            mov esi, dword ptr [rsp + 0xf8]
004D55FA  33 ED                           xor ebp, ebp
004D55FC  44 8B A4 24 F0 00 00 00         mov r12d, dword ptr [rsp + 0xf0]
004D5604  8B CE                           mov ecx, esi
004D5606  41 B9 00 00 00 80               mov r9d, 0x80000000
004D560C  81 E1 00 00 00 20               and ecx, 0x20000000
004D5612  75 47                           jne 0x1404d565b
004D5614  A8 02                           test al, 2
004D5616  74 3C                           je 0x1404d5654
004D5618  41 8B 40 48                     mov eax, dword ptr [r8 + 0x48]
004D561C  A8 01                           test al, 1
004D561E  74 34                           je 0x1404d5654
004D5620  85 F6                           test esi, esi
004D5622  79 13                           jns 0x1404d5637
004D5624  41 3B F1                        cmp esi, r9d
004D5627  75 4A                           jne 0x1404d5673
004D5629  39 AC 24 E8 00 00 00            cmp dword ptr [rsp + 0xe8], ebp
004D5630  75 41                           jne 0x1404d5673
004D5632  8D 69 08                        lea ebp, [rcx + 8]
004D5635  EB 7B                           jmp 0x1404d56b2
004D5637  B8 00 00 00 10                  mov eax, 0x10000000
004D563C  85 F0                           test eax, esi
004D563E  74 23                           je 0x1404d5663
004D5640  3B F0                           cmp esi, eax
004D5642  75 2F                           jne 0x1404d5673
004D5644  39 AC 24 E8 00 00 00            cmp dword ptr [rsp + 0xe8], ebp
004D564B  75 26                           jne 0x1404d5673
004D564D  BD 80 00 00 00                  mov ebp, 0x80
004D5652  EB 5E                           jmp 0x1404d56b2
004D5654  B8 18 00 00 C0                  mov eax, 0xc0000018
004D5659  EB 1D                           jmp 0x1404d5678
004D565B  F7 C6 00 00 00 90               test esi, 0x90000000
004D5661  75 10                           jne 0x1404d5673
004D5663  41 83 FC 07                     cmp r12d, 7
004D5667  76 2B                           jbe 0x1404d5694
004D5669  41 83 FC 18                     cmp r12d, 0x18
004D566D  75 04                           jne 0x1404d5673
004D566F  85 C9                           test ecx, ecx
004D5671  74 3F                           je 0x1404d56b2
004D5673  B8 45 00 00 C0                  mov eax, 0xc0000045
004D5678  48 8B 9C 24 C0 00 00 00         mov rbx, qword ptr [rsp + 0xc0]
004D5680  48 81 C4 80 00 00 00            add rsp, 0x80
004D5687  41 5F                           pop r15
004D5689  41 5E                           pop r14
004D568B  41 5D                           pop r13
004D568D  41 5C                           pop r12
004D568F  5F                              pop rdi
004D5690  5E                              pop rsi
004D5691  5D                              pop rbp
004D5692  C3                              ret
004D5693  CC                              int3
004D5694  41 8B C4                        mov eax, r12d
004D5697  83 E0 05                        and eax, 5
004D569A  3C 05                           cmp al, 5
004D569C  74 D5                           je 0x1404d5673
004D569E  41 8B EC                        mov ebp, r12d
004D56A1  83 E5 04                        and ebp, 4
004D56A4  83 CD 02                        or ebp, 2
004D56A7  D1 ED                           shr ebp, 1
004D56A9  41 F6 C4 02                     test r12b, 2
004D56AD  74 03                           je 0x1404d56b2
004D56AF  83 CD 04                        or ebp, 4
004D56B2  49 C1 EF 09                     shr r15, 9
004D56B6  49 BA F8 FF FF FF 7F 00 00 00   movabs r10, 0x7ffffffff8
004D56C0  4D 23 FA                        and r15, r10
004D56C3  49 B8 00 00 00 00 80 F6 FF FF   movabs r8, 0xfffff68000000000
004D56CD  49 8B C0                        mov rax, r8
004D56D0  48 8B 94 24 E0 00 00 00         mov rdx, qword ptr [rsp + 0xe0]
004D56D8  4C 03 F8                        add r15, rax
004D56DB  48 C1 EA 09                     shr rdx, 9
004D56DF  49 23 D2                        and rdx, r10
004D56E2  49 8B C0                        mov rax, r8
004D56E5  48 03 D0                        add rdx, rax
004D56E8  49 83 CA FF                     or r10, 0xffffffffffffffff
004D56EC  83 C8 FF                        or eax, 0xffffffff
004D56EF  48 89 54 24 78                  mov qword ptr [rsp + 0x78], rdx
004D56F4  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
004D56F9  45 33 F6                        xor r14d, r14d
004D56FC  33 C0                           xor eax, eax
004D56FE  4C 89 54 24 38                  mov qword ptr [rsp + 0x38], r10
004D5703  89 44 24 4C                     mov dword ptr [rsp + 0x4c], eax
004D5707  45 33 ED                        xor r13d, r13d
004D570A  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
004D5713  48 8B 98 B8 00 00 00            mov rbx, qword ptr [rax + 0xb8]
004D571A  48 81 C3 00 04 00 00            add rbx, 0x400
004D5721  48 89 5C 24 60                  mov qword ptr [rsp + 0x60], rbx
004D5726  85 C9                           test ecx, ecx
004D5728  75 08                           jne 0x1404d5732
004D572A  41 83 E4 02                     and r12d, 2
004D572E  41 83 CC 04                     or r12d, 4
004D5732  F7 D9                           neg ecx
004D5734  45 8B C4                        mov r8d, r12d
004D5737  49 8B D2                        mov rdx, r10
004D573A  49 8B CF                        mov rcx, r15
004D573D  1B C0                           sbb eax, eax
004D573F  45 0B C1                        or r8d, r9d
004D5742  83 E0 FE                        and eax, 0xfffffffe
004D5745  83 C0 04                        add eax, 4
004D5748  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
004D574C  E8 3F FE DE FF                  call 0x1402c5590
004D5751  48 8B CB                        mov rcx, rbx
004D5754  48 8B F8                        mov rdi, rax
004D5757  E8 94 74 DA FF                  call 0x14027cbf0
004D575C  44 21 6C 24 48                  and dword ptr [rsp + 0x48], r13d
004D5761  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
004D5766  88 44 24 30                     mov byte ptr [rsp + 0x30], al
004D576A  48 8B 84 24 D8 00 00 00         mov rax, qword ptr [rsp + 0xd8]
004D5772  48 25 00 F0 FF FF               and rax, 0xfffffffffffff000
004D5778  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
004D577D  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
004D5782  49 8B C7                        mov rax, r15
004D5785  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
004D578A  48 3B 44 24 78                  cmp rax, qword ptr [rsp + 0x78]
004D578F  0F 87 5E 03 00 00               ja 0x1404d5af3
004D5795  A8 78                           test al, 0x78
004D5797  75 72                           jne 0x1404d580b
004D5799  49 3B C7                        cmp rax, r15
004D579C  74 6D                           je 0x1404d580b
004D579E  33 D2                           xor edx, edx
004D57A0  48 8B CB                        mov rcx, rbx
004D57A3  E8 78 8D DD FF                  call 0x1402ae520
004D57A8  85 C0                           test eax, eax
004D57AA  75 1D                           jne 0x1404d57c9
004D57AC  E8 2F 1C DA FF                  call 0x1402773e0
004D57B1  85 C0                           test eax, eax
004D57B3  75 14                           jne 0x1404d57c9
004D57B5  4D 85 F6                        test r14, r14
004D57B8  74 65                           je 0x1404d581f
004D57BA  49 8B D6                        mov rdx, r14
004D57BD  48 8B CB                        mov rcx, rbx
004D57C0  E8 8B 8E DD FF                  call 0x1402ae650
004D57C5  85 C0                           test eax, eax
004D57C7  74 49                           je 0x1404d5812
004D57C9  48 8B 54 24 38                  mov rdx, qword ptr [rsp + 0x38]
004D57CE  44 8B C6                        mov r8d, esi
004D57D1  49 8B CD                        mov rcx, r13
004D57D4  E8 37 16 1B 00                  call 0x140686e10
004D57D9  48 83 4C 24 38 FF               or qword ptr [rsp + 0x38], 0xffffffffffffffff
004D57DF  45 33 ED                        xor r13d, r13d
004D57E2  4D 85 F6                        test r14, r14
004D57E5  74 0E                           je 0x1404d57f5
004D57E7  49 8B D6                        mov rdx, r14
004D57EA  48 8B CB                        mov rcx, rbx
004D57ED  E8 CE 16 D4 FF                  call 0x140216ec0
004D57F2  45 33 F6                        xor r14d, r14d
004D57F5  8A 54 24 30                     mov dl, byte ptr [rsp + 0x30]
004D57F9  48 8B CB                        mov rcx, rbx
004D57FC  E8 8F 7E DA FF                  call 0x14027d690
004D5801  48 8B CB                        mov rcx, rbx
004D5804  E8 E7 73 DA FF                  call 0x14027cbf0
004D5809  EB 14                           jmp 0x1404d581f
004D580B  4D 85 F6                        test r14, r14
004D580E  75 07                           jne 0x1404d5817
004D5810  EB 0D                           jmp 0x1404d581f
004D5812  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
004D5817  48 A9 FF 0F 00 00               test rax, 0xfff
004D581D  75 75                           jne 0x1404d5894
004D581F  48 8B 54 24 38                  mov rdx, qword ptr [rsp + 0x38]
004D5824  44 8B C6                        mov r8d, esi
004D5827  49 8B CD                        mov rcx, r13
004D582A  E8 E1 15 1B 00                  call 0x140686e10
004D582F  48 83 4C 24 38 FF               or qword ptr [rsp + 0x38], 0xffffffffffffffff
004D5835  45 33 ED                        xor r13d, r13d
004D5838  4D 85 F6                        test r14, r14
004D583B  74 0B                           je 0x1404d5848
004D583D  49 8B D6                        mov rdx, r14
004D5840  48 8B CB                        mov rcx, rbx
004D5843  E8 78 16 D4 FF                  call 0x140216ec0
004D5848  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
004D584D  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
004D5857  4C 8B F1                        mov r14, rcx
004D585A  49 C1 EE 09                     shr r14, 9
004D585E  4C 23 F0                        and r14, rax
004D5861  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
004D586B  48 8B C0                        mov rax, rax
004D586E  44 8A 44 24 30                  mov r8b, byte ptr [rsp + 0x30]
004D5873  4C 03 F0                        add r14, rax
004D5876  48 8B 84 24 D0 00 00 00         mov rax, qword ptr [rsp + 0xd0]
004D587E  45 33 C9                        xor r9d, r9d
004D5881  8B 50 30                        mov edx, dword ptr [rax + 0x30]
004D5884  C1 EA 0C                        shr edx, 0xc
004D5887  83 E2 7F                        and edx, 0x7f
004D588A  E8 E1 A6 DA FF                  call 0x14027ff70
004D588F  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
004D5894  8B 4C 24 48                     mov ecx, dword ptr [rsp + 0x48]
004D5898  85 C9                           test ecx, ecx
004D589A  75 51                           jne 0x1404d58ed
004D589C  48 8B C8                        mov rcx, rax
004D589F  E8 FC CF DA FF                  call 0x1402828a0
004D58A4  A8 01                           test al, 1
004D58A6  0F 84 67 01 00 00               je 0x1404d5a13
004D58AC  4C 39 7C 24 40                  cmp qword ptr [rsp + 0x40], r15
004D58B1  0F 85 20 02 00 00               jne 0x1404d5ad7
004D58B7  48 B9 FF FF FF FF FF 00 00 00   movabs rcx, 0xffffffffff
004D58C1  48 C1 E8 0C                     shr rax, 0xc
004D58C5  48 23 C1                        and rax, rcx
004D58C8  48 8D 0C 40                     lea rcx, [rax + rax*2]
004D58CC  48 03 C9                        add rcx, rcx
004D58CF  48 B8 10 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000010
004D58D9  8B 04 C8                        mov eax, dword ptr [rax + rcx*8]
004D58DC  48 C1 E8 05                     shr rax, 5
004D58E0  83 E0 1F                        and eax, 0x1f
004D58E3  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
004D58E8  E9 EA 01 00 00                  jmp 0x1404d5ad7
004D58ED  8B 44 24 58                     mov eax, dword ptr [rsp + 0x58]
004D58F1  FF C8                           dec eax
004D58F3  3B C8                           cmp ecx, eax
004D58F5  0F 85 F7 00 00 00               jne 0x1404d59f2
004D58FB  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
004D5900  E8 9B CF DA FF                  call 0x1402828a0
004D5905  48 8B F0                        mov rsi, rax
004D5908  48 8B D8                        mov rbx, rax
004D590B  48 B9 FF FF FF FF FF 00 00 00   movabs rcx, 0xffffffffff
004D5915  48 C1 EE 0C                     shr rsi, 0xc
004D5919  48 8B C6                        mov rax, rsi
004D591C  48 23 C1                        and rax, rcx
004D591F  48 8D 0C 40                     lea rcx, [rax + rax*2]
004D5923  48 C1 E1 04                     shl rcx, 4
004D5927  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
004D5931  48 03 C8                        add rcx, rax
004D5934  41 8B D4                        mov edx, r12d
004D5937  E8 EC 17 1B 00                  call 0x140687128
004D593C  4C 8B 84 24 D0 00 00 00         mov r8, qword ptr [rsp + 0xd0]
004D5944  48 B9 FF 0F 00 00 00 00 F0 FF   movabs rcx, 0xfff0000000000fff
004D594E  83 64 24 20 00                  and dword ptr [rsp + 0x20], 0
004D5953  41 B9 01 00 00 00               mov r9d, 1
004D5959  48 C1 E6 0C                     shl rsi, 0xc
004D595D  48 33 FE                        xor rdi, rsi
004D5960  48 23 F9                        and rdi, rcx
004D5963  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
004D5968  48 33 FE                        xor rdi, rsi
004D596B  48 8B D7                        mov rdx, rdi
004D596E  E8 FD 2B E9 FF                  call 0x140368570
004D5973  48 8B 05 0E 11 AF 00            mov rax, qword ptr [rip + 0xaf110e]
004D597A  48 0F BA E0 08                  bt rax, 8
004D597F  72 07                           jb 0x1404d5988
004D5981  48 0F BA E0 09                  bt rax, 9
004D5986  73 0F                           jae 0x1404d5997
004D5988  48 8B D7                        mov rdx, rdi
004D598B  48 8B CB                        mov rcx, rbx
004D598E  E8 9D F2 EA FF                  call 0x140384c30
004D5993  85 C0                           test eax, eax
004D5995  74 40                           je 0x1404d59d7
004D5997  4D 85 ED                        test r13, r13
004D599A  75 27                           jne 0x1404d59c3
004D599C  E8 EF D2 D6 FF                  call 0x140242c90
004D59A1  48 8B 54 24 60                  mov rdx, qword ptr [rsp + 0x60]
004D59A6  41 B9 08 00 00 00               mov r9d, 8
004D59AC  48 8B C8                        mov rcx, rax
004D59AF  C7 44 24 20 20 00 00 00         mov dword ptr [rsp + 0x20], 0x20
004D59B7  4C 8B E8                        mov r13, rax
004D59BA  44 8B 40 0C                     mov r8d, dword ptr [rax + 0xc]
004D59BE  E8 3D F5 DB FF                  call 0x140294f00
004D59C3  48 8B 54 24 50                  mov rdx, qword ptr [rsp + 0x50]
004D59C8  45 33 C9                        xor r9d, r9d
004D59CB  49 8B CD                        mov rcx, r13
004D59CE  45 8D 41 01                     lea r8d, [r9 + 1]
004D59D2  E8 99 DC DB FF                  call 0x140293670
004D59D7  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
004D59DC  8B B4 24 F8 00 00 00            mov esi, dword ptr [rsp + 0xf8]
004D59E3  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
004D59E8  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
004D59ED  E9 EA 00 00 00                  jmp 0x1404d5adc
004D59F2  83 F9 01                        cmp ecx, 1
004D59F5  8B D5                           mov edx, ebp
004D59F7  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
004D59FC  0F 85 A3 00 00 00               jne 0x1404d5aa5
004D5A02  E8 D9 5F 0E 00                  call 0x1405bb9e0
004D5A07  89 44 24 4C                     mov dword ptr [rsp + 0x4c], eax
004D5A0B  85 C0                           test eax, eax
004D5A0D  0F 89 C4 00 00 00               jns 0x1404d5ad7
004D5A13  48 8B 54 24 38                  mov rdx, qword ptr [rsp + 0x38]
004D5A18  BB 18 00 00 C0                  mov ebx, 0xc0000018
004D5A1D  44 8B C6                        mov r8d, esi
004D5A20  49 8B CD                        mov rcx, r13
004D5A23  E8 E8 13 1B 00                  call 0x140686e10
004D5A28  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
004D5A2D  4D 85 F6                        test r14, r14
004D5A30  74 0B                           je 0x1404d5a3d
004D5A32  49 8B D6                        mov rdx, r14
004D5A35  48 8B CE                        mov rcx, rsi
004D5A38  E8 83 14 D4 FF                  call 0x140216ec0
004D5A3D  8A 54 24 30                     mov dl, byte ptr [rsp + 0x30]
004D5A41  48 8B CE                        mov rcx, rsi
004D5A44  E8 47 7C DA FF                  call 0x14027d690
004D5A49  85 DB                           test ebx, ebx
004D5A4B  78 51                           js 0x1404d5a9e
004D5A4D  48 8B 54 24 70                  mov rdx, qword ptr [rsp + 0x70]
004D5A52  48 8D 0D D7 EB B3 FF            lea rcx, [rip - 0x4c1429]
004D5A59  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
004D5A5E  8B C0                           mov eax, eax
004D5A60  8B 0C 81                        mov ecx, dword ptr [rcx + rax*4]
004D5A63  48 8B 84 24 00 01 00 00         mov rax, qword ptr [rsp + 0x100]
004D5A6B  89 08                           mov dword ptr [rax], ecx
004D5A6D  48 8B 84 24 08 01 00 00         mov rax, qword ptr [rsp + 0x108]
004D5A75  48 8B 8C 24 E0 00 00 00         mov rcx, qword ptr [rsp + 0xe0]
004D5A7D  48 81 E1 00 F0 FF FF            and rcx, 0xfffffffffffff000
004D5A84  48 2B CA                        sub rcx, rdx
004D5A87  48 89 10                        mov qword ptr [rax], rdx
004D5A8A  48 81 C1 00 10 00 00            add rcx, 0x1000
004D5A91  48 8B 84 24 10 01 00 00         mov rax, qword ptr [rsp + 0x110]
004D5A99  33 DB                           xor ebx, ebx
004D5A9B  48 89 08                        mov qword ptr [rax], rcx
004D5A9E  8B C3                           mov eax, ebx
004D5AA0  E9 D3 FB FF FF                  jmp 0x1404d5678
004D5AA5  E8 F6 5F 0E 00                  call 0x1405bbaa0
004D5AAA  48 8B 84 24 D0 00 00 00         mov rax, qword ptr [rsp + 0xd0]
004D5AB2  48 8B 48 50                     mov rcx, qword ptr [rax + 0x50]
004D5AB6  48 C1 E1 19                     shl rcx, 0x19
004D5ABA  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
004D5AC4  48 8B C0                        mov rax, rax
004D5AC7  48 C1 E0 19                     shl rax, 0x19
004D5ACB  48 2B C8                        sub rcx, rax
004D5ACE  48 C1 F9 10                     sar rcx, 0x10
004D5AD2  E8 BD 61 0E 00                  call 0x1405bbc94
004D5AD7  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
004D5ADC  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
004D5AE1  48 83 C0 08                     add rax, 8
004D5AE5  48 81 44 24 50 00 10 00 00      add qword ptr [rsp + 0x50], 0x1000
004D5AEE  E9 92 FC FF FF                  jmp 0x1404d5785
004D5AF3  8B 44 24 4C                     mov eax, dword ptr [rsp + 0x4c]
004D5AF7  48 8B D1                        mov rdx, rcx
004D5AFA  8B D8                           mov ebx, eax
004D5AFC  85 C0                           test eax, eax
004D5AFE  0F 88 19 FF FF FF               js 0x1404d5a1d
004D5B04  44 8B 54 24 48                  mov r10d, dword ptr [rsp + 0x48]
004D5B09  41 FF C2                        inc r10d
004D5B0C  44 89 54 24 48                  mov dword ptr [rsp + 0x48], r10d
004D5B11  44 3B 54 24 58                  cmp r10d, dword ptr [rsp + 0x58]
004D5B16  0F 83 01 FF FF FF               jae 0x1404d5a1d
004D5B1C  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
004D5B21  89 44 24 4C                     mov dword ptr [rsp + 0x4c], eax
004D5B25  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
004D5B2A  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
004D5B2F  E9 49 FC FF FF                  jmp 0x1404d577d
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiProtectEnclavePages(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, unsigned int a6, unsigned int a7, unsigned int a8, __int64 a9, __int64 a10, __int64 a11)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m90;
    unsigned int v_stack_m98;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int8 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned int v_stack_p48;
    unsigned int v_stack_p4C;
    unsigned __int64 v_stack_p50;
    unsigned int v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;
    unsigned __int64 v_stack_p8;
    unsigned __int64 v_stack_pD0;
    unsigned __int64 v_stack_pD8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    v_rsp = (v_rsp) - (128);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a3 + 64)))) & (1)) != 0) goto loc_004D55F3;
    v_r10 = (a5) - (a4);
    v_r10 = (v_r10) + 1;
    *(unsigned __int64 *)(v_rsp + 24) = v_r10;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a3 + 72) + 76)) == 0) goto loc_004D5593;
    if (((a8) & (0x20000000ULL)) == 0) goto loc_004D5593;
    *(unsigned int *)(a9) = 4;
    result = 0;
    goto loc_004D55D8;
loc_004D5593:
    v_stack_m90 = a9;
    v_stack_m98 = (unsigned int)((unsigned int)(a6));
    result = VslDebugProtectSecureProcessMemory(a1, a2, v_stack_p20, v_stack_p18);
    if (sign_flag) goto loc_004D5678;
loc_004D55D8:
    *(unsigned __int64 *)(a10) = v_stack_p20;
    *(unsigned __int64 *)(a11) = v_stack_p18;
    goto loc_004D5678;
loc_004D55F3:
    v_rbp = 0;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a8)))) & (0x20000000ULL));
    if (condition_is_not_equal) goto loc_004D565B;
    if ((((unsigned __int8)(result)) & (2)) == 0) goto loc_004D5654;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p20 + 72)))) & (1)) == 0) goto loc_004D5654;
    if (!sign_flag) goto loc_004D5637;
    if (((unsigned int)((unsigned int)(a8))) != ((unsigned int)((unsigned int)(0x80000000ULL)))) goto loc_004D5673;
    if (a6 != 0) goto loc_004D5673;
    goto loc_004D56B2;
loc_004D5637:
    if ((((unsigned int)((unsigned int)(0x10000000ULL))) & ((unsigned int)((unsigned int)(a8)))) == 0) goto loc_004D5663;
    if (((unsigned int)((unsigned int)(a8))) != ((unsigned int)((unsigned int)(0x10000000ULL)))) goto loc_004D5673;
    if (a6 != ((unsigned int)(a1 + 8))) goto loc_004D5673;
    goto loc_004D56B2;
loc_004D5654:
    goto loc_004D5678;
loc_004D565B:
    if ((((unsigned int)((unsigned int)(a8))) & (0x90000000ULL)) != 0) goto loc_004D5673;
loc_004D5663:
    if (((unsigned int)((unsigned int)(a7))) <= 7) goto loc_004D5694;
    if (((unsigned int)((unsigned int)(a7))) != 24) goto loc_004D5673;
    if ((unsigned int)(a1) == 0) goto loc_004D56B2;
loc_004D5673:
loc_004D5678:
    v_rsp = (v_rsp) + (128);
    return (unsigned int)(0xC0000045ULL);
loc_004D5694:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a7)))) & (5));
    if (((unsigned __int8)(result)) == 5) goto loc_004D5673;
    v_rbp = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a7)))) & (4));
    v_rbp = (unsigned int)((v_rbp) | (2));
    v_rbp = (unsigned int)((v_rbp) >> (1));
    if ((((unsigned __int8)((unsigned int)(a7))) & (2)) != 0) {
        v_rbp = (unsigned int)((v_rbp) | (4));
    }
    v_r15 = (v_stack_p20) >> (9);
    v_r15 = (v_r15) & (v_stack_p18);
    v_r15 = (v_r15) + (v_stack_p20);
    a2 = (a5) >> (9);
    a2 = (a2) & (v_stack_p18);
    a2 = (a2) + (v_stack_p20);
    v_r10 = (v_stack_p18) | (-1);
    result = (unsigned int)((v_stack_p20) | (0xFFFFFFFFULL));
    v_stack_p78 = a2;
    v_stack_p68 = result;
    v_r14 = 0;
    result = 0;
    v_stack_p38 = v_r10;
    v_stack_p4C = 0;
    v_r13 = 0;
    v_rbx = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184)) + (0x400ULL);
    v_stack_p60 = v_rbx;
    v_r12 = (unsigned int)(a7);
    if ((unsigned int)(a1) == 0) {
        v_r12 = (unsigned int)(((unsigned int)(a7)) & (2));
        v_r12 = (unsigned int)((v_r12) | (4));
    }
    a1 = (unsigned int)(-(a1));
    a3 = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) | ((unsigned int)((unsigned int)(0x80000000ULL))));
    result = (unsigned int)((*(unsigned __int64 *)(gs_base + (0 + 392))) & (0xFFFFFFFEULL));
    result = (unsigned int)((result) + (4));
    v_stack_p58 = (unsigned int)(result);
    result = MiMakeValidPte(v_r15, v_r10, a3, (unsigned int)(0x80000000ULL));
    result = MiLockWorkingSetShared(v_rbx, v_r10, a3, (unsigned int)(0x80000000ULL));
    v_stack_p30 = (unsigned __int8)(result);
    result = (v_stack_pD8) & (0xFFFFFFFFFFFFF000ULL);
    v_stack_p70 = result;
loc_004D577D:
    v_stack_p50 = result;
loc_004D5785:
    v_stack_p40 = v_r15;
    if (v_r15 > v_stack_p78) goto loc_004D5AF3;
    if ((((unsigned __int8)(v_r15)) & (120)) != 0) goto loc_004D580B;
    if (v_r15 == v_r15) goto loc_004D580B;
    a2 = 0;
    result = MiWorkingSetIsContended(v_rbx, a2, a3, (unsigned int)(0x80000000ULL));
    if ((unsigned int)(result) != 0) goto loc_004D57C9;
    result = KeShouldYieldProcessor(v_rbx, a2, a3, (unsigned int)(0x80000000ULL));
    if ((unsigned int)(result) != 0) goto loc_004D57C9;
    if (0 == 0) goto loc_004D581F;
    result = MiPageTableLockIsContended(v_rbx, 0, a3, (unsigned int)(0x80000000ULL));
    if ((unsigned int)(result) == 0) goto loc_004D5812;
loc_004D57C9:
    result = MiFlushEnclaveTb(0, v_stack_p38, (unsigned int)((unsigned int)((unsigned int)(a8))), (unsigned int)(0x80000000ULL));
    v_r13 = 0;
    if (0 != 0) {
        a2 = 0;
        a1 = v_rbx;
        result = MiUnlockPageTable(a1, a2, (unsigned int)((unsigned int)((unsigned int)(a8))), (unsigned int)(0x80000000ULL));
        v_r14 = 0;
    }
    result = MiUnlockWorkingSetShared(v_rbx, v_stack_p30, (unsigned int)((unsigned int)((unsigned int)(a8))), (unsigned int)(0x80000000ULL));
    result = MiLockWorkingSetShared(v_rbx, v_stack_p30, (unsigned int)((unsigned int)((unsigned int)(a8))), (unsigned int)(0x80000000ULL));
    goto loc_004D581F;
loc_004D580B:
    if (0 != 0) goto loc_004D5817;
    goto loc_004D581F;
loc_004D5812:
loc_004D5817:
    if (((v_stack_p40) & (0xFFFULL)) != 0) goto loc_004D5894;
loc_004D581F:
    result = MiFlushEnclaveTb(0, v_stack_p38, (unsigned int)((unsigned int)((unsigned int)(a8))), (unsigned int)(0x80000000ULL));
    v_r13 = 0;
    if (0 != 0) {
        a2 = 0;
        a1 = v_rbx;
        result = MiUnlockPageTable(a1, a2, (unsigned int)((unsigned int)((unsigned int)(a8))), (unsigned int)(0x80000000ULL));
    }
    v_r14 = (v_stack_p40) >> (9);
    v_r14 = (v_r14) & (result);
    v_r14 = (v_r14) + (result);
    a4 = 0;
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_pD0 + 48))) >> (12));
    a2 = (unsigned int)((a2) & (127));
    result = MiMakeSystemAddressValid(v_stack_p40, a2, v_stack_p30, a4);
loc_004D5894:
    if ((unsigned int)((unsigned int)(v_stack_p48)) != 0) goto loc_004D58ED;
    result = MI_READ_PTE_LOCK_FREE(v_stack_p40, a2, v_stack_p30, a4);
    if ((((unsigned __int8)(result)) & (1)) == 0) goto loc_004D5A13;
    if (v_stack_p40 != v_r15) goto loc_004D5AD7;
    result = (result) >> (12);
    result = (result) & (v_stack_p40);
    a1 = (result + result * 2) + (result + result * 2);
    result = ((unsigned int)(*(unsigned int *)(result + a1 * 8))) >> (5);
    result = (unsigned int)((result) & (31));
    v_stack_p68 = result;
    goto loc_004D5AD7;
loc_004D58ED:
    result = (unsigned int)(((unsigned int)(v_stack_p58)) - 1);
    if (((unsigned int)(a1)) != ((unsigned int)(result))) goto loc_004D59F2;
    result = MI_READ_PTE_LOCK_FREE(v_stack_p40, a2, v_stack_p30, a4);
    v_rsi = (result) >> (12);
    result = (v_rsi) & (v_stack_p40);
    a1 = (result + result * 2) << (4);
    a1 = (a1) + (result);
    result = MiUpdateEnclavePfnProtection(a1, (unsigned int)((unsigned int)(v_r12)), v_stack_p30, a4);
    v_rsi = (v_rsi) << (12);
    v_rdi = (result) ^ (v_rsi);
    v_rdi = (v_rdi) & (a1);
    v_rdi = (v_rdi) ^ (v_rsi);
    result = MiWriteEnclavePte(v_stack_p40, v_rdi, v_stack_pD0, 1);
    if (condition_is_below) goto loc_004D5988;
    if (condition_is_above_or_equal) goto loc_004D5997;
loc_004D5988:
    result = MI_TIGHTER_PERMISSIONS(result, v_rdi, v_stack_pD0, 1);
    if ((unsigned int)(result) == 0) goto loc_004D59D7;
loc_004D5997:
    if (0 == 0) {
        result = MiGetProcessorFlushList(result, v_rdi, v_stack_pD0, 1);
        a2 = v_stack_p60;
        a4 = 8;
        a1 = result;
        v_stack_p20 = 32;
        v_r13 = result;
        a3 = *(unsigned int *)(result + 12);
        result = MiInitializeTbFlushList(a1, a2, a3, a4);
    }
    a4 = 0;
    result = MiInsertTbFlushEntry(v_r13, v_stack_p50, a4 + 1, a4);
loc_004D59D7:
    v_stack_p38 = v_stack_p50;
    goto loc_004D5ADC;
loc_004D59F2:
    if (((unsigned int)(v_stack_p50)) != 1) goto loc_004D5AA5;
    result = KeCanChangeEnclavePageProtection(v_stack_p50, (unsigned int)((unsigned int)(v_rbp)), a4 + 1, a4);
    v_stack_p4C = (unsigned int)(result);
    if (!sign_flag) goto loc_004D5AD7;
loc_004D5A13:
loc_004D5A1D:
    result = MiFlushEnclaveTb(v_r13, v_stack_p38, (unsigned int)((unsigned int)((unsigned int)(a8))), a4);
    if (v_r14 != 0) {
        a2 = v_r14;
        a1 = v_stack_p60;
        result = MiUnlockPageTable(a1, a2, (unsigned int)((unsigned int)((unsigned int)(a8))), a4);
    }
    result = MiUnlockWorkingSetShared(v_stack_p60, v_stack_p30, (unsigned int)((unsigned int)((unsigned int)(a8))), a4);
    v_rbx = (unsigned int)(0xC0000018ULL);
    if (!(sign_flag)) {
        a2 = v_stack_p70;
        a1 = v_rip - 4985897;
        result = v_stack_p68;
        result = (unsigned int)(result);
        a1 = *(unsigned int *)(a1 + result * 4);
        result = a9;
        *(unsigned int *)(result) = (unsigned int)(a1);
        result = a10;
        a1 = a5;
        a1 = (a1) & (0xFFFFFFFFFFFFF000ULL);
        a1 = (a1) - (a2);
        *(unsigned __int64 *)(result) = a2;
        a1 = (a1) + (0x1000ULL);
        result = a11;
        v_rbx = 0;
        *(unsigned __int64 *)(result) = a1;
    }
    goto loc_004D5678;
loc_004D5AA5:
    result = KeChangeEnclavePageProtection(a1, a2, (unsigned int)((unsigned int)((unsigned int)(a8))), a4);
    a1 = (*(unsigned __int64 *)(v_stack_pD0 + 80)) << (25);
    result = (v_stack_pD0) << (25);
    a1 = (a1) - (result);
    a1 = (a1) >> (16);
    result = KeTrackEnclaveTbFlush(a1, a2, (unsigned int)((unsigned int)((unsigned int)(a8))), a4);
loc_004D5AD7:
loc_004D5ADC:
    result = (v_stack_p40) + (8);
    goto loc_004D5785;
loc_004D5AF3:
    if (sign_flag) goto loc_004D5A1D;
    v_r10 = (unsigned int)(((unsigned int)(v_stack_p48)) + 1);
    v_stack_p48 = (unsigned int)(v_r10);
    if (((unsigned int)(v_r10)) >= v_stack_p58) goto loc_004D5A1D;
    v_stack_p4C = (unsigned int)((unsigned int)(v_stack_p4C));
    v_stack_p38 = v_stack_p38;
    goto loc_004D577D;
}
```

## 5. (Beta) C Style

```c
int64_t MiProtectEnclavePages(int64_t Arg1, int64_t Arg2, void *Arg3, int64_t Arg4, int64_t Arg5, uint32_t Arg6, uint32_t Arg7, void *Arg8, void *Arg9, void *Arg10, void *Arg11)
{
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg8 = (uint8_t *)Arg8;
    uint8_t *arg9 = (uint8_t *)Arg9;
    uint8_t *arg10 = (uint8_t *)Arg10;
    uint8_t *arg11 = (uint8_t *)Arg11;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m90;
    uint32_t v_stack_m98;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint8_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint32_t v_stack_p48;
    uint32_t v_stack_p4C;
    uint64_t v_stack_p50;
    uint32_t v_stack_p58;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;
    uint64_t v_stack_p8;
    uint64_t v_stack_pD0;
    uint64_t v_stack_pD8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x20) = Arg4;
    *(void **)(local_rsp + 0x18) = Arg3;
    local_rsp = (local_rsp) - (128);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg3 + 0x40)))) & (1)) != 0) goto loc_004D55F3;
    local_r10 = (Arg5) - (Arg4);
    local_r10 = (local_r10) + 1;
    *(uint64_t *)(local_rsp + 0x18) = local_r10;
    if ((*(uint8_t *)(*(uint64_t *)(arg3 + 0x48) + 0x4C)) == 0) goto loc_004D5593;
    if (((Arg8) & (0x20000000ULL)) == 0) goto loc_004D5593;
    *(uint32_t *)(arg9) = 4;
    result = 0;
    goto loc_004D55D8;
loc_004D5593:
    v_stack_m90 = Arg9;
    v_stack_m98 = (uint32_t)((uint32_t)(Arg6));
    result = VslDebugProtectSecureProcessMemory(Arg1, Arg2, v_stack_p20, v_stack_p18);
    if (sign_flag) goto loc_004D5678;
loc_004D55D8:
    *(uint64_t *)(arg10) = v_stack_p20;
    *(uint64_t *)(arg11) = v_stack_p18;
    goto loc_004D5678;
loc_004D55F3:
    local_rbp = 0;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg8)))) & (0x20000000ULL));
    if (condition_is_not_equal) goto loc_004D565B;
    if ((((uint8_t)(result)) & (2)) == 0) goto loc_004D5654;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x48)))) & (1)) == 0) goto loc_004D5654;
    if (!sign_flag) goto loc_004D5637;
    if (((uint32_t)((uint32_t)(Arg8))) != ((uint32_t)((uint32_t)(0x80000000ULL)))) goto loc_004D5673;
    if (Arg6 != 0) goto loc_004D5673;
    goto loc_004D56B2;
loc_004D5637:
    if ((((uint32_t)((uint32_t)(0x10000000ULL))) & ((uint32_t)((uint32_t)(Arg8)))) == 0) goto loc_004D5663;
    if (((uint32_t)((uint32_t)(Arg8))) != ((uint32_t)((uint32_t)(0x10000000ULL)))) goto loc_004D5673;
    if (Arg6 != ((uint32_t)(Arg1 + 8))) goto loc_004D5673;
    goto loc_004D56B2;
loc_004D5654:
    goto loc_004D5678;
loc_004D565B:
    if ((((uint32_t)((uint32_t)(Arg8))) & (0x90000000ULL)) != 0) goto loc_004D5673;
loc_004D5663:
    if (((uint32_t)((uint32_t)(Arg7))) <= 7) goto loc_004D5694;
    if (((uint32_t)((uint32_t)(Arg7))) != 24) goto loc_004D5673;
    if ((uint32_t)(Arg1) == 0) goto loc_004D56B2;
loc_004D5673:
loc_004D5678:
    local_rsp = (local_rsp) + (128);
    return (uint32_t)(0xC0000045ULL);
loc_004D5694:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg7)))) & (5));
    if (((uint8_t)(result)) == 5) goto loc_004D5673;
    local_rbp = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg7)))) & (4));
    local_rbp = (uint32_t)((local_rbp) | (2));
    local_rbp = (uint32_t)((local_rbp) >> (1));
    if ((((uint8_t)((uint32_t)(Arg7))) & (2)) != 0) {
        local_rbp = (uint32_t)((local_rbp) | (4));
    }
    local_r15 = (v_stack_p20) >> (9);
    local_r15 = (local_r15) & (v_stack_p18);
    local_r15 = (local_r15) + (v_stack_p20);
    Arg2 = (Arg5) >> (9);
    Arg2 = (Arg2) & (v_stack_p18);
    Arg2 = (Arg2) + (v_stack_p20);
    local_r10 = (v_stack_p18) | (-1);
    result = (uint32_t)((v_stack_p20) | (0xFFFFFFFFULL));
    v_stack_p78 = Arg2;
    v_stack_p68 = result;
    local_r14 = 0;
    result = 0;
    v_stack_p38 = local_r10;
    v_stack_p4C = 0;
    local_r13 = 0;
    local_rbx = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8)) + (0x400ULL);
    v_stack_p60 = local_rbx;
    local_r12 = (uint32_t)(Arg7);
    if ((uint32_t)(Arg1) == 0) {
        local_r12 = (uint32_t)(((uint32_t)(Arg7)) & (2));
        local_r12 = (uint32_t)((local_r12) | (4));
    }
    Arg1 = (uint32_t)(-(Arg1));
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) | ((uint32_t)((uint32_t)(0x80000000ULL))));
    result = (uint32_t)((*(uint64_t *)(gs_base + (0 + 0x188))) & (0xFFFFFFFEULL));
    result = (uint32_t)((result) + (4));
    v_stack_p58 = (uint32_t)(result);
    result = MiMakeValidPte(local_r15, local_r10, Arg3, (uint32_t)(0x80000000ULL));
    result = MiLockWorkingSetShared(local_rbx, local_r10, Arg3, (uint32_t)(0x80000000ULL));
    v_stack_p30 = (uint8_t)(result);
    result = (v_stack_pD8) & (0xFFFFFFFFFFFFF000ULL);
    v_stack_p70 = result;
loc_004D577D:
    v_stack_p50 = result;
loc_004D5785:
    v_stack_p40 = local_r15;
    if (local_r15 > v_stack_p78) goto loc_004D5AF3;
    if ((((uint8_t)(local_r15)) & (120)) != 0) goto loc_004D580B;
    if (local_r15 == local_r15) goto loc_004D580B;
    Arg2 = 0;
    result = MiWorkingSetIsContended(local_rbx, Arg2, Arg3, (uint32_t)(0x80000000ULL));
    if ((uint32_t)(result) != 0) goto loc_004D57C9;
    result = KeShouldYieldProcessor(local_rbx, Arg2, Arg3, (uint32_t)(0x80000000ULL));
    if ((uint32_t)(result) != 0) goto loc_004D57C9;
    if (0 == 0) goto loc_004D581F;
    result = MiPageTableLockIsContended(local_rbx, 0, Arg3, (uint32_t)(0x80000000ULL));
    if ((uint32_t)(result) == 0) goto loc_004D5812;
loc_004D57C9:
    result = MiFlushEnclaveTb(0, v_stack_p38, (uint32_t)((uint32_t)((uint32_t)(Arg8))), (uint32_t)(0x80000000ULL));
    local_r13 = 0;
    if (0 != 0) {
        Arg2 = 0;
        Arg1 = local_rbx;
        result = MiUnlockPageTable(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg8))), (uint32_t)(0x80000000ULL));
        local_r14 = 0;
    }
    result = MiUnlockWorkingSetShared(local_rbx, v_stack_p30, (uint32_t)((uint32_t)((uint32_t)(Arg8))), (uint32_t)(0x80000000ULL));
    result = MiLockWorkingSetShared(local_rbx, v_stack_p30, (uint32_t)((uint32_t)((uint32_t)(Arg8))), (uint32_t)(0x80000000ULL));
    goto loc_004D581F;
loc_004D580B:
    if (0 != 0) goto loc_004D5817;
    goto loc_004D581F;
loc_004D5812:
loc_004D5817:
    if (((v_stack_p40) & (0xFFFULL)) != 0) goto loc_004D5894;
loc_004D581F:
    result = MiFlushEnclaveTb(0, v_stack_p38, (uint32_t)((uint32_t)((uint32_t)(Arg8))), (uint32_t)(0x80000000ULL));
    local_r13 = 0;
    if (0 != 0) {
        Arg2 = 0;
        Arg1 = local_rbx;
        result = MiUnlockPageTable(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg8))), (uint32_t)(0x80000000ULL));
    }
    local_r14 = (v_stack_p40) >> (9);
    local_r14 = (local_r14) & (result);
    local_r14 = (local_r14) + (result);
    Arg4 = 0;
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_pD0 + 0x30))) >> (12));
    Arg2 = (uint32_t)((Arg2) & (127));
    result = MiMakeSystemAddressValid(v_stack_p40, Arg2, v_stack_p30, Arg4);
loc_004D5894:
    if ((uint32_t)((uint32_t)(v_stack_p48)) != 0) goto loc_004D58ED;
    result = MI_READ_PTE_LOCK_FREE(v_stack_p40, Arg2, v_stack_p30, Arg4);
    if ((((uint8_t)(result)) & (1)) == 0) goto loc_004D5A13;
    if (v_stack_p40 != local_r15) goto loc_004D5AD7;
    result = (result) >> (12);
    result = (result) & (v_stack_p40);
    Arg1 = (result + result * 2) + (result + result * 2);
    result = ((uint32_t)(*(uint32_t *)(result + Arg1 * 8))) >> (5);
    result = (uint32_t)((result) & (31));
    v_stack_p68 = result;
    goto loc_004D5AD7;
loc_004D58ED:
    result = (uint32_t)(((uint32_t)(v_stack_p58)) - 1);
    if (((uint32_t)(Arg1)) != ((uint32_t)(result))) goto loc_004D59F2;
    result = MI_READ_PTE_LOCK_FREE(v_stack_p40, Arg2, v_stack_p30, Arg4);
    local_rsi = (result) >> (12);
    result = (local_rsi) & (v_stack_p40);
    Arg1 = (result + result * 2) << (4);
    Arg1 = (Arg1) + (result);
    result = MiUpdateEnclavePfnProtection(Arg1, (uint32_t)((uint32_t)(local_r12)), v_stack_p30, Arg4);
    local_rsi = (local_rsi) << (12);
    local_rdi = (result) ^ (local_rsi);
    local_rdi = (local_rdi) & (Arg1);
    local_rdi = (local_rdi) ^ (local_rsi);
    result = MiWriteEnclavePte(v_stack_p40, local_rdi, v_stack_pD0, 1);
    if (condition_is_below) goto loc_004D5988;
    if (condition_is_above_or_equal) goto loc_004D5997;
loc_004D5988:
    result = MI_TIGHTER_PERMISSIONS(result, local_rdi, v_stack_pD0, 1);
    if ((uint32_t)(result) == 0) goto loc_004D59D7;
loc_004D5997:
    if (0 == 0) {
        result = MiGetProcessorFlushList(result, local_rdi, v_stack_pD0, 1);
        Arg2 = v_stack_p60;
        Arg4 = 8;
        Arg1 = result;
        v_stack_p20 = 32;
        local_r13 = result;
        Arg3 = *(uint32_t *)(result + 0xC);
        result = MiInitializeTbFlushList(Arg1, Arg2, Arg3, Arg4);
    }
    Arg4 = 0;
    result = MiInsertTbFlushEntry(local_r13, v_stack_p50, Arg4 + 1, Arg4);
loc_004D59D7:
    v_stack_p38 = v_stack_p50;
    goto loc_004D5ADC;
loc_004D59F2:
    if (((uint32_t)(v_stack_p50)) != 1) goto loc_004D5AA5;
    result = KeCanChangeEnclavePageProtection(v_stack_p50, (uint32_t)((uint32_t)(local_rbp)), Arg4 + 1, Arg4);
    v_stack_p4C = (uint32_t)(result);
    if (!sign_flag) goto loc_004D5AD7;
loc_004D5A13:
loc_004D5A1D:
    result = MiFlushEnclaveTb(local_r13, v_stack_p38, (uint32_t)((uint32_t)((uint32_t)(Arg8))), Arg4);
    if (local_r14 != 0) {
        Arg2 = local_r14;
        Arg1 = v_stack_p60;
        result = MiUnlockPageTable(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg8))), Arg4);
    }
    result = MiUnlockWorkingSetShared(v_stack_p60, v_stack_p30, (uint32_t)((uint32_t)((uint32_t)(Arg8))), Arg4);
    local_rbx = (uint32_t)(0xC0000018ULL);
    if (!(sign_flag)) {
        Arg2 = v_stack_p70;
        Arg1 = v_rip - 4985897;
        result = v_stack_p68;
        result = (uint32_t)(result);
        Arg1 = *(uint32_t *)(Arg1 + result * 4);
        result = Arg9;
        *(uint32_t *)(result) = (uint32_t)(Arg1);
        result = Arg10;
        Arg1 = Arg5;
        Arg1 = (Arg1) & (0xFFFFFFFFFFFFF000ULL);
        Arg1 = (Arg1) - (Arg2);
        *(uint64_t *)(result) = Arg2;
        Arg1 = (Arg1) + (0x1000ULL);
        result = Arg11;
        local_rbx = 0;
        *(uint64_t *)(result) = Arg1;
    }
    goto loc_004D5678;
loc_004D5AA5:
    result = KeChangeEnclavePageProtection(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg8))), Arg4);
    Arg1 = (*(uint64_t *)(v_stack_pD0 + 0x50)) << (25);
    result = (v_stack_pD0) << (25);
    Arg1 = (Arg1) - (result);
    Arg1 = (Arg1) >> (16);
    result = KeTrackEnclaveTbFlush(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg8))), Arg4);
loc_004D5AD7:
loc_004D5ADC:
    result = (v_stack_p40) + (8);
    goto loc_004D5785;
loc_004D5AF3:
    if (sign_flag) goto loc_004D5A1D;
    local_r10 = (uint32_t)(((uint32_t)(v_stack_p48)) + 1);
    v_stack_p48 = (uint32_t)(local_r10);
    if (((uint32_t)(local_r10)) >= v_stack_p58) goto loc_004D5A1D;
    v_stack_p4C = (uint32_t)((uint32_t)(v_stack_p4C));
    v_stack_p38 = v_stack_p38;
    goto loc_004D577D;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x40` | `32` | `R` |
| `Arg3` | `+ 0x48` | `32` | `R` |
| `Arg3` | `+ 0x48` | `64` | `R` |
| `Arg8` | `+ 0x8` | `32` | `R` |
| `Arg9` | `+ 0x0` | `32` | `W` |
| `Arg10` | `+ 0x0` | `64` | `W` |
| `Arg11` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004D5528&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
