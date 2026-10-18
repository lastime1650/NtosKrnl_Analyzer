# MiAddViewsForSection

- RVA: `0x00324990`–`0x00325055` (길이 `1,733` bytes)
- VA: `0x0000000140324990`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00075B88`
- 디코드: `412`개 명령, `1,733/1,733` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **32**; 고유 호출 대상: **21**
- 직접 호출자로 확인된 함수: **7**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x00324A22` → [ExpWaitForSpinLockExclusiveAndAcquire](ExpWaitForSpinLockExclusiveAndAcquire_function_003239A0.md) (function, `0x003239A0`)
- `0x00324ABA` → [MiReferenceActiveSubsection](MiReferenceActiveSubsection_function_00325060.md) (function, `0x00325060`)
- `0x00324B2B` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x00324BCA` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00324BFD` → [KeAbPreAcquire](../21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00324C16` → [ExfAcquirePushLockExclusiveEx](../20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x00324C8D` → [KiCheckForKernelApcDelivery](../2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (function, `0x002E2C80`)
- `0x00324CBC` → [ExpAcquireSpinLockExclusiveAtDpcLevelInstrumented](ExpAcquireSpinLockExclusiveAtDpcLevelInstrumented_function_00323A70.md) (function, `0x00323A70`)
- `0x00324CD7` → [ExReleaseSpinLockExclusiveFromDpcLevel](../24/ExReleaseSpinLockExclusiveFromDpcLevel_function_002497E0.md) (function, `0x002497E0`)
- `0x00324CF3` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x00324D26` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x00324D5C` → [KiAbEntryFreeAndEnableInterrupts](../26/KiAbEntryFreeAndEnableInterrupts_function_002622D0.md) (function, `0x002622D0`)
- `0x00324DA1` → [MiCreatePrototypePtes](../29/MiCreatePrototypePtes_function_002950FC.md) (function, `0x002950FC`)
- `0x00324DBF` → [ExAcquireSpinLockExclusive](../24/ExAcquireSpinLockExclusive_function_00248690.md) (function, `0x00248690`)
- `0x00324E06` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00324E15` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00324E22` → [ExfTryToWakePushLock](../26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x00324E4F` → [ExAcquireSpinLockExclusive](../24/ExAcquireSpinLockExclusive_function_00248690.md) (function, `0x00248690`)
- `0x00324E62` → [MiCheckControlArea](../28/MiCheckControlArea_function_002861B0.md) (function, `0x002861B0`)
- `0x00324E8F` → [ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented](../2C/ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented_function_002C0F44.md) (function, `0x002C0F44`)
- `0x00324EB3` → [ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented](../2C/ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented_function_002C0F44.md) (function, `0x002C0F44`)
- `0x00324EDD` → [KeAbPostRelease](../2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00324F03` → [KiCheckForKernelApcDelivery](../2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (function, `0x002E2C80`)
- `0x00324F29` → [KeAbPreAcquire](../21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00324F4C` → [ExfAcquirePushLockExclusiveEx](../20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x00324F86` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x00324F98` → [ExAcquireSpinLockExclusive](../24/ExAcquireSpinLockExclusive_function_00248690.md) (function, `0x00248690`)
- `0x00324FA2` → [ExfTryToWakePushLock](../26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x00324FCD` → [KeAbPreAcquire](../21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00324FF4` → [ExfAcquirePushLockExclusiveEx](../20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x0032500B` → [MiReleaseSpinLockExclusive](../24/MiReleaseSpinLockExclusive_function_002482C0.md) (function, `0x002482C0`)
- `0x00325037` → [MiReleaseSpinLockExclusive](../24/MiReleaseSpinLockExclusive_function_002482C0.md) (function, `0x002482C0`)

### Direct callers
- [MmMapViewInSystemCache](../27/MmMapViewInSystemCache_function_00273094.md) at `0x00273118`
- [MiReferenceDataSubsections](../3B/MiReferenceDataSubsections_function_003B3768.md) at `0x003B37CF`
- [sub_006E720A](../6E/Unknown_function_006E720A.md) at `0x006E7217`
- [sub_00884EE1](../../page/88/Unknown_function_00884EE1.md) at `0x00884F97`
- [MiPfPrepareReadList](../../page/93/MiPfPrepareReadList_function_0093CD5C.md) at `0x0093D099`
- [MiPfPrepareSequentialReadList](../../page/93/MiPfPrepareSequentialReadList_function_0093D8E8.md) at `0x0093DE62`
- [sub_00B1B86E](../../page/B1/Unknown_function_00B1B86E.md) at `0x00B1B87A`

### Static image references
- `0x003249F7` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x00324A04` → RVA `0x00FC6B06` (`ALMOSTRO`; read)
- `0x00324A4D` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x00324CA6` → RVA `0x00F0DE58` (`.data`; read)
- `0x00324DF8` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **7**
  - `0x00324C55` → [sub_006E19B0 + 0x12](../6E/Unknown_function_006E19B0.md) (`tail-transfer`)
  - `0x00324E3F` → [sub_006E19B0 + 0x164](../6E/Unknown_function_006E19B0.md) (`tail-transfer`)
  - `0x00324FE5` → [sub_006E19B0](../6E/Unknown_function_006E19B0.md) (`tail-transfer`)
  - `0x00324FFE` → [sub_006E19B0](../6E/Unknown_function_006E19B0.md) (`tail-transfer`)
  - `0x00325019` → [sub_006E19B0 + 0x112](../6E/Unknown_function_006E19B0.md) (`tail-transfer`)
  - `0x0032501F` → [sub_006E19B0 + 0x158](../6E/Unknown_function_006E19B0.md) (`tail-transfer`)
  - `0x00325045` → [sub_006E19B0 + 0x112](../6E/Unknown_function_006E19B0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00324990  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
00324995  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
0032499A  53                              push rbx
0032499B  55                              push rbp
0032499C  56                              push rsi
0032499D  57                              push rdi
0032499E  41 54                           push r12
003249A0  41 55                           push r13
003249A2  41 56                           push r14
003249A4  41 57                           push r15
003249A6  48 83 EC 78                     sub rsp, 0x78
003249AA  4C 8B 31                        mov r14, qword ptr [rcx]
003249AD  33 DB                           xor ebx, ebx
003249AF  41 8B E8                        mov ebp, r8d
003249B2  44 89 44 24 30                  mov dword ptr [rsp + 0x30], r8d
003249B7  41 8B F8                        mov edi, r8d
003249BA  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
003249BF  4C 8B E9                        mov r13, rcx
003249C2  49 39 5E 40                     cmp qword ptr [r14 + 0x40], rbx
003249C6  0F 84 04 02 00 00               je 0x140324bd0
003249CC  C7 84 24 D8 00 00 00 01 00 00 00  mov dword ptr [rsp + 0xd8], 1
003249D7  44 8B FB                        mov r15d, ebx
003249DA  48 89 5C 24 48                  mov qword ptr [rsp + 0x48], rbx
003249DF  8B C5                           mov eax, ebp
003249E1  25 80 00 00 00                  and eax, 0x80
003249E6  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
003249EA  45 0F 20 C4                     mov r12, cr8
003249EE  B8 02 00 00 00                  mov eax, 2
003249F3  44 0F 22 C0                     mov cr8, rax
003249F7  83 3D 22 23 CA 00 00            cmp dword ptr [rip + 0xca2322], 0
003249FE  0F 85 1B 03 00 00               jne 0x140324d1f
00324A04  F6 05 FB 20 CA 00 21            test byte ptr [rip + 0xca20fb], 0x21
00324A0B  0F 85 95 02 00 00               jne 0x140324ca6
00324A11  F0 41 0F BA 6E 48 1F            lock bts dword ptr [r14 + 0x48], 0x1f
00324A18  73 0F                           jae 0x140324a29
00324A1A  41 0F B6 D4                     movzx edx, r12b
00324A1E  49 8D 4E 48                     lea rcx, [r14 + 0x48]
00324A22  E8 79 EF FF FF                  call 0x1403239a0
00324A27  8B D8                           mov ebx, eax
00324A29  41 8B 56 48                     mov edx, dword ptr [r14 + 0x48]
00324A2D  B8 00 00 00 80                  mov eax, 0x80000000
00324A32  8B CA                           mov ecx, edx
00324A34  0F BA F1 1E                     btr ecx, 0x1e
00324A38  3B C8                           cmp ecx, eax
00324A3A  74 32                           je 0x140324a6e
00324A3C  0F BA E2 1E                     bt edx, 0x1e
00324A40  72 09                           jb 0x140324a4b
00324A42  F0 41 81 4E 48 00 00 00 40      lock or dword ptr [r14 + 0x48], 0x40000000
00324A4B  FF C3                           inc ebx
00324A4D  85 1D 59 08 CA 00               test dword ptr [rip + 0xca0859], ebx
00324A53  0F 84 9F 03 00 00               je 0x140324df8
00324A59  F3 90                           pause
00324A5B  41 8B 56 48                     mov edx, dword ptr [r14 + 0x48]
00324A5F  B9 00 00 00 80                  mov ecx, 0x80000000
00324A64  8B C2                           mov eax, edx
00324A66  0F BA F0 1E                     btr eax, 0x1e
00324A6A  3B C1                           cmp eax, ecx
00324A6C  75 CE                           jne 0x140324a3c
00324A6E  40 F6 C5 01                     test bpl, 1
00324A72  74 11                           je 0x140324a85
00324A74  49 FF 46 28                     inc qword ptr [r14 + 0x28]
00324A78  41 FF 46 58                     inc dword ptr [r14 + 0x58]
00324A7C  83 CD 04                        or ebp, 4
00324A7F  8B FD                           mov edi, ebp
00324A81  89 6C 24 30                     mov dword ptr [rsp + 0x30], ebp
00324A85  48 C7 C3 FF FF FF FF            mov rbx, 0xffffffffffffffff
00324A8C  49 83 7D 08 00                  cmp qword ptr [r13 + 8], 0
00324A91  41 8B 45 2C                     mov eax, dword ptr [r13 + 0x2c]
00324A95  89 84 24 D0 00 00 00            mov dword ptr [rsp + 0xd0], eax
00324A9C  4C 89 6C 24 68                  mov qword ptr [rsp + 0x68], r13
00324AA1  0F 84 1F 02 00 00               je 0x140324cc6
00324AA7  0F BA E5 09                     bt ebp, 9
00324AAB  0F 82 73 05 00 00               jb 0x140325024
00324AB1  45 0F B6 C4                     movzx r8d, r12b
00324AB5  8B D7                           mov edx, edi
00324AB7  49 8B CD                        mov rcx, r13
00324ABA  E8 A1 05 00 00                  call 0x140325060
00324ABF  89 84 24 D0 00 00 00            mov dword ptr [rsp + 0xd0], eax
00324AC6  85 C0                           test eax, eax
00324AC8  0F 88 98 02 00 00               js 0x140324d66
00324ACE  8B BC 24 D8 00 00 00            mov edi, dword ptr [rsp + 0xd8]
00324AD5  85 FF                           test edi, edi
00324AD7  0F 85 6A 01 00 00               jne 0x140324c47
00324ADD  48 8B 8C 24 C8 00 00 00         mov rcx, qword ptr [rsp + 0xc8]
00324AE5  48 85 C9                        test rcx, rcx
00324AE8  0F 84 E6 02 00 00               je 0x140324dd4
00324AEE  41 8B 45 2C                     mov eax, dword ptr [r13 + 0x2c]
00324AF2  48 3B C8                        cmp rcx, rax
00324AF5  0F 87 CE 02 00 00               ja 0x140324dc9
00324AFB  41 80 FC 11                     cmp r12b, 0x11
00324AFF  0F 84 28 01 00 00               je 0x140324c2d
00324B05  F6 05 FA 1F CA 00 01            test byte ptr [rip + 0xca1ffa], 1
00324B0C  0F 85 63 03 00 00               jne 0x140324e75
00324B12  41 C7 46 48 00 00 00 00         mov dword ptr [r14 + 0x48], 0
00324B1A  83 3D FF 21 CA 00 00            cmp dword ptr [rip + 0xca21ff], 0
00324B21  74 0D                           je 0x140324b30
00324B23  44 0F 20 C1                     mov rcx, cr8
00324B27  41 0F B6 D4                     movzx edx, r12b
00324B2B  E8 68 0B 1D 00                  call 0x1404f5698
00324B30  41 0F B6 C4                     movzx eax, r12b
00324B34  44 0F 22 C0                     mov cr8, rax
00324B38  85 FF                           test edi, edi
00324B3A  0F 85 52 01 00 00               jne 0x140324c92
00324B40  48 8B 7C 24 48                  mov rdi, qword ptr [rsp + 0x48]
00324B45  48 83 C7 28                     add rdi, 0x28
00324B49  F0 48 0F C1 1F                  lock xadd qword ptr [rdi], rbx
00324B4E  80 E3 06                        and bl, 6
00324B51  80 FB 02                        cmp bl, 2
00324B54  0F 84 C5 02 00 00               je 0x140324e1f
00324B5A  65 4C 8B 1C 25 88 01 00 00      mov r11, qword ptr gs:[0x188]
00324B63  FA                              cli
00324B64  4D 8B 83 70 04 00 00            mov r8, qword ptr [r11 + 0x470]
00324B6B  4C 8B CF                        mov r9, rdi
00324B6E  48 BE FC FF FF FF FF FF FF 7F   movabs rsi, 0x7ffffffffffffffc
00324B78  4C 23 CE                        and r9, rsi
00324B7B  33 DB                           xor ebx, ebx
00324B7D  8B C3                           mov eax, ebx
00324B7F  90                              nop
00324B80  41 0F B6 48 0C                  movzx ecx, byte ptr [r8 + 0xc]
00324B85  3B C1                           cmp eax, ecx
00324B87  73 20                           jae 0x140324ba9
00324B89  8B C8                           mov ecx, eax
00324B8B  4C 6B D1 58                     imul r10, rcx, 0x58
00324B8F  4D 03 D0                        add r10, r8
00324B92  49 8B 52 10                     mov rdx, qword ptr [r10 + 0x10]
00324B96  48 8B CA                        mov rcx, rdx
00324B99  48 23 CE                        and rcx, rsi
00324B9C  49 3B C9                        cmp rcx, r9
00324B9F  0F 84 8B 01 00 00               je 0x140324d30
00324BA5  FF C0                           inc eax
00324BA7  EB D7                           jmp 0x140324b80
00324BA9  41 8B 43 78                     mov eax, dword ptr [r11 + 0x78]
00324BAD  0F BA E0 10                     bt eax, 0x10
00324BB1  0F 82 A3 00 00 00               jb 0x140324c5a
00324BB7  45 33 C9                        xor r9d, r9d
00324BBA  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00324BBF  4C 8B C7                        mov r8, rdi
00324BC2  49 8B D3                        mov rdx, r11
00324BC5  B9 62 01 00 00                  mov ecx, 0x162
00324BCA  E8 91 8A 1D 00                  call 0x1404fd660
00324BCF  CC                              int3
00324BD0  65 4C 8B 3C 25 88 01 00 00      mov r15, qword ptr gs:[0x188]
00324BD9  45 33 C0                        xor r8d, r8d
00324BDC  49 8B 06                        mov rax, qword ptr [r14]
00324BDF  33 D2                           xor edx, edx
00324BE1  89 9C 24 D8 00 00 00            mov dword ptr [rsp + 0xd8], ebx
00324BE8  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00324BED  66 41 FF 8F E6 01 00 00         dec word ptr [r15 + 0x1e6]
00324BF5  90                              nop
00324BF6  48 8D 58 28                     lea rbx, [rax + 0x28]
00324BFA  48 8B CB                        mov rcx, rbx
00324BFD  E8 2E B6 EE FF                  call 0x140210230
00324C02  F0 48 0F BA 2B 00               lock bts qword ptr [rbx], 0
00324C08  48 8B F8                        mov rdi, rax
00324C0B  73 0E                           jae 0x140324c1b
00324C0D  4C 8B C3                        mov r8, rbx
00324C10  48 8B D0                        mov rdx, rax
00324C13  48 8B CB                        mov rcx, rbx
00324C16  E8 75 B0 EE FF                  call 0x14020fc90
00324C1B  33 DB                           xor ebx, ebx
00324C1D  48 85 FF                        test rdi, rdi
00324C20  74 04                           je 0x140324c26
00324C22  C6 47 0A 01                     mov byte ptr [rdi + 0xa], 1
00324C26  8B FD                           mov edi, ebp
00324C28  E9 B2 FD FF FF                  jmp 0x1403249df
00324C2D  F6 05 D2 1E CA 00 01            test byte ptr [rip + 0xca1ed2], 1
00324C34  0F 85 5F 02 00 00               jne 0x140324e99
00324C3A  41 C7 46 48 00 00 00 00         mov dword ptr [r14 + 0x48], 0
00324C42  E9 F1 FE FF FF                  jmp 0x140324b38
00324C47  41 8B 45 34                     mov eax, dword ptr [r13 + 0x34]
00324C4B  0F BA E0 1E                     bt eax, 0x1e
00324C4F  0F 83 88 FE FF FF               jae 0x140324add
00324C55  E9 68 CD 3B 00                  jmp 0x1406e19c2
00324C5A  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
00324C63  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
00324C6A  4D 85 C0                        test r8, r8
00324C6D  0F 85 F5 02 00 00               jne 0x140324f68
00324C73  FB                              sti
00324C74  90                              nop
00324C75  66 41 83 87 E6 01 00 00 01      add word ptr [r15 + 0x1e6], 1
00324C7E  75 12                           jne 0x140324c92
00324C80  49 8D 87 98 00 00 00            lea rax, [r15 + 0x98]
00324C87  90                              nop
00324C88  48 39 00                        cmp qword ptr [rax], rax
00324C8B  74 05                           je 0x140324c92
00324C8D  E8 EE DF FB FF                  call 0x1402e2c80
00324C92  33 C0                           xor eax, eax
00324C94  48 83 C4 78                     add rsp, 0x78
00324C98  41 5F                           pop r15
00324C9A  41 5E                           pop r14
00324C9C  41 5D                           pop r13
00324C9E  41 5C                           pop r12
00324CA0  5F                              pop rdi
00324CA1  5E                              pop rsi
00324CA2  5D                              pop rbp
00324CA3  5B                              pop rbx
00324CA4  C3                              ret
00324CA5  CC                              int3
00324CA6  8B 05 AC 91 BE 00               mov eax, dword ptr [rip + 0xbe91ac]
00324CAC  85 C0                           test eax, eax
00324CAE  0F 85 5D FD FF FF               jne 0x140324a11
00324CB4  41 0F B6 D4                     movzx edx, r12b
00324CB8  49 8D 4E 48                     lea rcx, [r14 + 0x48]
00324CBC  E8 AF ED FF FF                  call 0x140323a70
00324CC1  E9 A8 FD FF FF                  jmp 0x140324a6e
00324CC6  41 8B 45 34                     mov eax, dword ptr [r13 + 0x34]
00324CCA  49 8D 4E 48                     lea rcx, [r14 + 0x48]
00324CCE  25 FF FF FF 3F                  and eax, 0x3fffffff
00324CD3  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
00324CD7  E8 04 4B F2 FF                  call 0x1402497e0
00324CDC  41 80 FC 11                     cmp r12b, 0x11
00324CE0  74 1E                           je 0x140324d00
00324CE2  83 3D 37 20 CA 00 00            cmp dword ptr [rip + 0xca2037], 0
00324CE9  74 0D                           je 0x140324cf8
00324CEB  44 0F 20 C1                     mov rcx, cr8
00324CEF  41 0F B6 D4                     movzx edx, r12b
00324CF3  E8 A0 09 1D 00                  call 0x1404f5698
00324CF8  41 0F B6 C4                     movzx eax, r12b
00324CFC  44 0F 22 C0                     mov cr8, rax
00324D00  8B BC 24 D8 00 00 00            mov edi, dword ptr [rsp + 0xd8]
00324D07  85 FF                           test edi, edi
00324D09  0F 84 AE 01 00 00               je 0x140324ebd
00324D0F  40 F6 C5 02                     test bpl, 2
00324D13  74 75                           je 0x140324d8a
00324D15  B8 89 01 00 C0                  mov eax, 0xc0000189
00324D1A  E9 75 FF FF FF                  jmp 0x140324c94
00324D1F  0F B6 D0                        movzx edx, al
00324D22  41 0F B6 CC                     movzx ecx, r12b
00324D26  E8 D1 09 1D 00                  call 0x1404f56fc
00324D2B  E9 D4 FC FF FF                  jmp 0x140324a04
00324D30  41 38 5A 1A                     cmp byte ptr [r10 + 0x1a], bl
00324D34  0F 84 6B FE FF FF               je 0x140324ba5
00324D3A  F6 C2 01                        test dl, 1
00324D3D  0F 85 62 FE FF FF               jne 0x140324ba5
00324D43  41 B9 01 00 00 00               mov r9d, 1
00324D49  41 88 5A 1A                     mov byte ptr [r10 + 0x1a], bl
00324D4D  4C 8B C7                        mov r8, rdi
00324D50  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00324D55  49 8B D3                        mov rdx, r11
00324D58  49 8D 4A 10                     lea rcx, [r10 + 0x10]
00324D5C  E8 6F D5 F3 FF                  call 0x1402622d0
00324D61  E9 0E FF FF FF                  jmp 0x140324c74
00324D66  3D 0A 02 00 C0                  cmp eax, 0xc000020a
00324D6B  0F 85 92 02 00 00               jne 0x140325003
00324D71  8B BC 24 D8 00 00 00            mov edi, dword ptr [rsp + 0xd8]
00324D78  4D 85 ED                        test r13, r13
00324D7B  0F 84 7A FD FF FF               je 0x140324afb
00324D81  8B 7C 24 30                     mov edi, dword ptr [rsp + 0x30]
00324D85  E9 02 FD FF FF                  jmp 0x140324a8c
00324D8A  44 8B 8C 24 D0 00 00 00         mov r9d, dword ptr [rsp + 0xd0]
00324D92  49 8B CD                        mov rcx, r13
00324D95  8B 54 24 30                     mov edx, dword ptr [rsp + 0x30]
00324D99  45 8B C1                        mov r8d, r9d
00324D9C  44 2B 44 24 58                  sub r8d, dword ptr [rsp + 0x58]
00324DA1  E8 56 03 F7 FF                  call 0x1402950fc
00324DA6  89 84 24 D0 00 00 00            mov dword ptr [rsp + 0xd0], eax
00324DAD  8B C8                           mov ecx, eax
00324DAF  85 C0                           test eax, eax
00324DB1  78 79                           js 0x140324e2c
00324DB3  85 FF                           test edi, edi
00324DB5  0F 84 52 01 00 00               je 0x140324f0d
00324DBB  49 8D 4E 48                     lea rcx, [r14 + 0x48]
00324DBF  E8 CC 38 F2 FF                  call 0x140248690
00324DC4  E9 14 FD FF FF                  jmp 0x140324add
00324DC9  48 2B C8                        sub rcx, rax
00324DCC  48 89 8C 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], rcx
00324DD4  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
00324DD9  4D 8B 6D 10                     mov r13, qword ptr [r13 + 0x10]
00324DDD  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
00324DE2  85 FF                           test edi, edi
00324DE4  75 92                           jne 0x140324d78
00324DE6  8B 44 24 40                     mov eax, dword ptr [rsp + 0x40]
00324DEA  83 C8 04                        or eax, 4
00324DED  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
00324DF2  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00324DF6  EB 80                           jmp 0x140324d78
00324DF8  8B 05 BA 1C CA 00               mov eax, dword ptr [rip + 0xca1cba]
00324DFE  A8 40                           test al, 0x40
00324E00  0F 84 53 FC FF FF               je 0x140324a59
00324E06  E8 85 A6 FE FF                  call 0x14030f490
00324E0B  84 C0                           test al, al
00324E0D  0F 84 46 FC FF FF               je 0x140324a59
00324E13  8B CB                           mov ecx, ebx
00324E15  E8 46 A6 FE FF                  call 0x14030f460
00324E1A  E9 3C FC FF FF                  jmp 0x140324a5b
00324E1F  48 8B CF                        mov rcx, rdi
00324E22  E8 A9 0F F4 FF                  call 0x140265dd0
00324E27  E9 2E FD FF FF                  jmp 0x140324b5a
00324E2C  3D 0A 02 00 C0                  cmp eax, 0xc000020a
00324E31  0F 84 59 01 00 00               je 0x140324f90
00324E37  4C 8B 6C 24 38                  mov r13, qword ptr [rsp + 0x38]
00324E3C  4D 85 ED                        test r13, r13
00324E3F  0F 85 CF CC 3B 00               jne 0x1406e1b14
00324E45  40 F6 C5 01                     test bpl, 1
00324E49  74 23                           je 0x140324e6e
00324E4B  49 8D 4E 48                     lea rcx, [r14 + 0x48]
00324E4F  E8 3C 38 F2 FF                  call 0x140248690
00324E54  49 FF 4E 28                     dec qword ptr [r14 + 0x28]
00324E58  0F B6 D0                        movzx edx, al
00324E5B  41 FF 4E 58                     dec dword ptr [r14 + 0x58]
00324E5F  49 8B CE                        mov rcx, r14
00324E62  E8 49 13 F6 FF                  call 0x1402861b0
00324E67  8B 8C 24 D0 00 00 00            mov ecx, dword ptr [rsp + 0xd0]
00324E6E  8B C1                           mov eax, ecx
00324E70  E9 1F FE FF FF                  jmp 0x140324c94
00324E75  8B 05 DD 8F BE 00               mov eax, dword ptr [rip + 0xbe8fdd]
00324E7B  85 C0                           test eax, eax
00324E7D  0F 85 8F FC FF FF               jne 0x140324b12
00324E83  48 8B 94 24 B8 00 00 00         mov rdx, qword ptr [rsp + 0xb8]
00324E8B  49 8D 4E 48                     lea rcx, [r14 + 0x48]
00324E8F  E8 B0 C0 F9 FF                  call 0x1402c0f44
00324E94  E9 81 FC FF FF                  jmp 0x140324b1a
00324E99  8B 05 B9 8F BE 00               mov eax, dword ptr [rip + 0xbe8fb9]
00324E9F  85 C0                           test eax, eax
00324EA1  0F 85 93 FD FF FF               jne 0x140324c3a
00324EA7  48 8B 94 24 B8 00 00 00         mov rdx, qword ptr [rsp + 0xb8]
00324EAF  49 8D 4E 48                     lea rcx, [r14 + 0x48]
00324EB3  E8 8C C0 F9 FF                  call 0x1402c0f44
00324EB8  E9 7B FC FF FF                  jmp 0x140324b38
00324EBD  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00324EC2  48 8B C3                        mov rax, rbx
00324EC5  48 83 C1 28                     add rcx, 0x28
00324EC9  48 89 4C 24 50                  mov qword ptr [rsp + 0x50], rcx
00324ECE  F0 48 0F C1 01                  lock xadd qword ptr [rcx], rax
00324ED3  24 06                           and al, 6
00324ED5  3C 02                           cmp al, 2
00324ED7  0F 84 C5 00 00 00               je 0x140324fa2
00324EDD  E8 1E C7 FB FF                  call 0x1402e1600
00324EE2  90                              nop
00324EE3  66 41 83 87 E6 01 00 00 01      add word ptr [r15 + 0x1e6], 1
00324EEC  0F 85 1D FE FF FF               jne 0x140324d0f
00324EF2  49 8D 87 98 00 00 00            lea rax, [r15 + 0x98]
00324EF9  90                              nop
00324EFA  48 39 00                        cmp qword ptr [rax], rax
00324EFD  0F 84 0C FE FF FF               je 0x140324d0f
00324F03  E8 78 DD FB FF                  call 0x1402e2c80
00324F08  E9 02 FE FF FF                  jmp 0x140324d0f
00324F0D  66 41 FF 8F E6 01 00 00         dec word ptr [r15 + 0x1e6]
00324F15  45 33 C0                        xor r8d, r8d
00324F18  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00324F1D  33 D2                           xor edx, edx
00324F1F  48 83 C1 28                     add rcx, 0x28
00324F23  90                              nop
00324F24  48 89 4C 24 50                  mov qword ptr [rsp + 0x50], rcx
00324F29  E8 02 B3 EE FF                  call 0x140210230
00324F2E  48 8B C8                        mov rcx, rax
00324F31  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00324F36  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
00324F3B  F0 48 0F BA 28 00               lock bts qword ptr [rax], 0
00324F41  73 13                           jae 0x140324f56
00324F43  48 8B D1                        mov rdx, rcx
00324F46  4C 8B C0                        mov r8, rax
00324F49  48 8B C8                        mov rcx, rax
00324F4C  E8 3F AD EE FF                  call 0x14020fc90
00324F51  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
00324F56  48 85 C9                        test rcx, rcx
00324F59  0F 84 5C FE FF FF               je 0x140324dbb
00324F5F  C6 41 0A 01                     mov byte ptr [rcx + 0xa], 1
00324F63  E9 53 FE FF FF                  jmp 0x140324dbb
00324F68  41 0F 0D 08                     prefetchw byte ptr [r8]
00324F6C  41 8B 00                        mov eax, dword ptr [r8]
00324F6F  8B D0                           mov edx, eax
00324F71  0F BA F2 15                     btr edx, 0x15
00324F75  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
00324F7A  75 F3                           jne 0x140324f6f
00324F7C  0F BA E0 15                     bt eax, 0x15
00324F80  0F 83 ED FC FF FF               jae 0x140324c73
00324F86  E8 45 E2 F3 FF                  call 0x1402631d0
00324F8B  E9 E3 FC FF FF                  jmp 0x140324c73
00324F90  85 FF                           test edi, edi
00324F92  74 1D                           je 0x140324fb1
00324F94  49 8D 4E 48                     lea rcx, [r14 + 0x48]
00324F98  E8 F3 36 F2 FF                  call 0x140248690
00324F9D  E9 D6 FD FF FF                  jmp 0x140324d78
00324FA2  E8 29 0E F4 FF                  call 0x140265dd0
00324FA7  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00324FAC  E9 2C FF FF FF                  jmp 0x140324edd
00324FB1  66 41 FF 8F E6 01 00 00         dec word ptr [r15 + 0x1e6]
00324FB9  45 33 C0                        xor r8d, r8d
00324FBC  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00324FC1  33 D2                           xor edx, edx
00324FC3  48 83 C1 28                     add rcx, 0x28
00324FC7  90                              nop
00324FC8  48 89 4C 24 50                  mov qword ptr [rsp + 0x50], rcx
00324FCD  E8 5E B2 EE FF                  call 0x140210230
00324FD2  48 8B C8                        mov rcx, rax
00324FD5  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
00324FDA  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
00324FDF  F0 48 0F BA 28 00               lock bts qword ptr [rax], 0
00324FE5  0F 83 C5 C9 3B 00               jae 0x1406e19b0
00324FEB  48 8B D1                        mov rdx, rcx
00324FEE  4C 8B C0                        mov r8, rax
00324FF1  48 8B C8                        mov rcx, rax
00324FF4  E8 97 AC EE FF                  call 0x14020fc90
00324FF9  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00324FFE  E9 AD C9 3B 00                  jmp 0x1406e19b0
00325003  41 0F B6 D4                     movzx edx, r12b
00325007  49 8D 4E 48                     lea rcx, [r14 + 0x48]
0032500B  E8 B0 32 F2 FF                  call 0x1402482c0
00325010  8B BC 24 D8 00 00 00            mov edi, dword ptr [rsp + 0xd8]
00325017  85 FF                           test edi, edi
00325019  0F 84 A3 CA 3B 00               je 0x1406e1ac2
0032501F  E9 E4 CA 3B 00                  jmp 0x1406e1b08
00325024  41 0F B6 D4                     movzx edx, r12b
00325028  C7 84 24 D0 00 00 00 18 00 00 C0  mov dword ptr [rsp + 0xd0], 0xc0000018
00325033  49 8D 4E 48                     lea rcx, [r14 + 0x48]
00325037  E8 84 32 F2 FF                  call 0x1402482c0
0032503C  8B BC 24 D8 00 00 00            mov edi, dword ptr [rsp + 0xd8]
00325043  85 FF                           test edi, edi
00325045  0F 84 77 CA 3B 00               je 0x1406e1ac2
0032504B  B9 18 00 00 C0                  mov ecx, 0xc0000018
00325050  E9 E2 FD FF FF                  jmp 0x140324e37
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiAddViewsForSection(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m70;
    unsigned int v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned int v_stack_m88;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned int v_stack_p20;
    unsigned int v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned int v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned int v_stack_p58;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p8;
    unsigned __int64 v_stack_pB8;
    unsigned __int64 v_stack_pC8;
    unsigned int v_stack_pD0;
    unsigned int v_stack_pD8;

    v_stack_p10 = a2;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (120);
    v_rbx = 0;
    v_stack_m88 = a3;
    v_stack_m80 = 0;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 64)) == 0) goto loc_00324BD0;
    v_stack_p20 = 1;
    v_stack_m70 = 0;
loc_003249DF:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a3)))) & (128));
    v_stack_m78 = (unsigned int)(result);
    if ((*(unsigned int *)(v_rip + 13247266)) != 0) goto loc_00324D1F;
loc_00324A04:
    if (((*(unsigned __int8 *)(v_rip + 13246715)) & (33)) != 0) goto loc_00324CA6;
loc_00324A11:
    result = 2;
    if (!(condition_is_above_or_equal)) {
        a2 = (unsigned __int8)(v_cr8);
        a1 = *(unsigned __int64 *)(a1) + 72;
        result = ExpWaitForSpinLockExclusiveAndAcquire(a1, a2, a3, a4);
        v_rbx = (unsigned int)(result);
    }
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 72)))))) == ((unsigned int)((unsigned int)(0x80000000ULL)))) goto loc_00324A6E;
loc_00324A3C:
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 72)))))) >= ((unsigned int)((unsigned int)(0x80000000ULL)))) {
    }
    v_rbx = (unsigned int)((v_rbx) + 1);
    if (((*(unsigned int *)(v_rip + 13240409)) & ((unsigned int)(v_rbx))) == 0) goto loc_00324DF8;
loc_00324A59:
loc_00324A5B:
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 72)))))) != ((unsigned int)((unsigned int)(0x80000000ULL)))) goto loc_00324A3C;
loc_00324A6E:
    v_rdi = (unsigned int)(a3);
    v_rbp = (unsigned int)(a3);
    if ((((unsigned __int8)((unsigned int)(a3))) & (1)) != 0) {
        v_rbp = (unsigned int)(((unsigned int)(a3)) | (4));
        v_rdi = (unsigned int)(v_rbp);
        v_stack_m88 = (unsigned int)(v_rbp);
    }
loc_00324A8C:
    v_stack_p18 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 44)));
    v_stack_m50 = a1;
    if ((*(unsigned __int64 *)(a1 + 8)) == 0) goto loc_00324CC6;
    if ((*(unsigned __int64 *)(a1 + 8)) < 0) goto loc_00325024;
    result = MiReferenceActiveSubsection(a1, (unsigned int)((unsigned int)(v_rdi)), (unsigned __int8)(v_cr8), a4);
    v_stack_p18 = (unsigned int)(result);
    if (sign_flag) goto loc_00324D66;
    if ((unsigned int)((unsigned int)(v_stack_p20)) != 0) goto loc_00324C47;
loc_00324ADD:
    if (v_stack_p10 == 0) goto loc_00324DD4;
    if (v_stack_p10 > ((unsigned int)(*(unsigned int *)(a1 + 44)))) goto loc_00324DC9;
loc_00324AFB:
    if (((unsigned __int8)(v_cr8)) == 17) goto loc_00324C2D;
    if (((*(unsigned __int8 *)(v_rip + 13246458)) & (1)) != 0) goto loc_00324E75;
loc_00324B12:
    *(unsigned int *)(*(unsigned __int64 *)(a1) + 72) = 0;
loc_00324B1A:
    result = (unsigned int)(*(unsigned int *)(a1 + 44));
    if ((*(unsigned int *)(v_rip + 13246975)) != 0) {
        a1 = 2;
        a2 = (unsigned __int8)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, (unsigned __int8)(v_cr8), a4);
    }
loc_00324B38:
    if ((unsigned int)((unsigned int)(v_stack_p20)) != 0) goto loc_00324C92;
    v_rdi = (v_stack_m70) + (40);
    v_rbx = (unsigned __int8)((-1) & (6));
    if (((unsigned __int8)(v_rbx)) == 2) goto loc_00324E1F;
loc_00324B5A:
    a4 = (v_rdi) & (v_rsi);
    v_rbx = 0;
loc_00324B80:
    if (0 >= ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1136) + 12)))) goto loc_00324BA9;
    v_r10 = (v_r10) * (0);
    v_r10 = (v_r10) + (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1136));
    a1 = (*(unsigned __int64 *)(v_r10 + 16)) & (v_rsi);
    if (a1 == a4) goto loc_00324D30;
loc_00324BA5:
    result = (unsigned int)((0) + 1);
    goto loc_00324B80;
loc_00324BA9:
    if (a1 < a4) goto loc_00324C5A;
    a4 = 0;
    v_stack_m98 = 0;
    result = KeBugCheckEx(354, *(unsigned __int64 *)(gs_base + (0 + 392)), v_rdi, a4);
loc_00324BD0:
    a3 = 0;
    a2 = 0;
    v_stack_p20 = 0;
    v_stack_m70 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1));
    result = KeAbPreAcquire(*(unsigned __int64 *)(*(unsigned __int64 *)(a1)) + 40, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1)) + 40;
        a2 = result;
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1)) + 40;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    v_rbx = 0;
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    goto loc_003249DF;
loc_00324C2D:
    if (((*(unsigned __int8 *)(v_rip + 13246162)) & (1)) != 0) goto loc_00324E99;
loc_00324C3A:
    *(unsigned int *)(*(unsigned __int64 *)(a1) + 72) = 0;
    goto loc_00324B38;
loc_00324C47:
    if (condition_is_above_or_equal) goto loc_00324ADD;
loc_00324C5A:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) != 0) goto loc_00324F68;
loc_00324C73:
loc_00324C74:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) != 0) goto loc_00324C92;
    result = *(unsigned __int64 *)(gs_base + (0 + 392)) + 152;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 152)) != (*(unsigned __int64 *)(gs_base + (0 + 392)) + 152)) {
        result = KiCheckForKernelApcDelivery(*(unsigned __int64 *)(gs_base + (0 + 32)), a2, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), a4);
    }
    result = 0;
loc_00324C94:
    v_rsp = (v_rsp) + (120);
    return result;
loc_00324CA6:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12489132))) != 0) goto loc_00324A11;
    result = ExpAcquireSpinLockExclusiveAtDpcLevelInstrumented(*(unsigned __int64 *)(a1) + 72, (unsigned __int8)(v_cr8), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), a4);
    goto loc_00324A6E;
loc_00324CC6:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 52))) & (0x3FFFFFFFULL));
    v_stack_p58 = (unsigned int)(result);
    result = ExReleaseSpinLockExclusiveFromDpcLevel(*(unsigned __int64 *)(a1) + 72, (unsigned __int8)(v_cr8), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), a4);
    if (((unsigned __int8)(v_cr8)) == 17) goto loc_00324D00;
    if ((*(unsigned int *)(v_rip + 13246519)) != 0) {
        a1 = (unsigned __int8)(v_cr8);
        a2 = (unsigned __int8)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), a4);
    }
loc_00324D00:
    if ((unsigned int)((unsigned int)(v_stack_pD8)) == 0) goto loc_00324EBD;
loc_00324D0F:
    if ((((unsigned __int8)(v_rbp)) & (2)) == 0) goto loc_00324D8A;
    goto loc_00324C94;
loc_00324D1F:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(v_cr8), (unsigned __int8)((unsigned int)(0xC0000189ULL)), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), a4);
    goto loc_00324A04;
loc_00324D30:
    if ((*(unsigned __int8 *)(v_r10 + 26)) == 0) goto loc_00324BA5;
    if ((((unsigned __int8)((unsigned __int8)((unsigned int)(0xC0000189ULL)))) & (1)) != 0) goto loc_00324BA5;
    *(unsigned __int8 *)(v_r10 + 26) = 0;
    v_stack_p20 = 0;
    result = KiAbEntryFreeAndEnableInterrupts(v_r10 + 16, *(unsigned __int64 *)(gs_base + (0 + 392)), (unsigned int)(v_stack_pD8), 1);
    goto loc_00324C74;
loc_00324D66:
    if (((unsigned int)(result)) != 0xC000020AULL) goto loc_00325003;
loc_00324D78:
    if (a1 == 0) goto loc_00324AFB;
    goto loc_00324A8C;
loc_00324D8A:
    a3 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_pD0)))) - (v_stack_p58));
    result = MiCreatePrototypePtes(a1, (unsigned int)(v_stack_p30), a3, (unsigned int)(v_stack_pD0));
    v_stack_pD0 = (unsigned int)(result);
    if (sign_flag) goto loc_00324E2C;
    if ((unsigned int)((unsigned int)(v_stack_p30)) == 0) goto loc_00324F0D;
loc_00324DBB:
    result = ExAcquireSpinLockExclusive(*(unsigned __int64 *)(a1) + 72, (unsigned int)(v_stack_p30), a3, (unsigned int)(v_stack_pD0));
    goto loc_00324ADD;
loc_00324DC9:
    a1 = (*(unsigned __int64 *)(a1) + 72) - (result);
    v_stack_pC8 = a1;
loc_00324DD4:
    v_stack_p38 = v_stack_p68;
    if ((unsigned int)((unsigned int)(v_stack_p30)) != 0) goto loc_00324D78;
    result = (unsigned int)(((unsigned int)(v_stack_p40)) | (4));
    v_stack_p38 = v_stack_p68;
    v_stack_p30 = (unsigned int)(result);
    goto loc_00324D78;
loc_00324DF8:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13245626)))) & (64)) == 0) goto loc_00324A59;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_stack_p68, (unsigned int)(v_stack_p30), a3, (unsigned int)(v_stack_pD0));
    if ((unsigned __int8)(result) == 0) goto loc_00324A59;
    result = HvlNotifyLongSpinWait(0, (unsigned int)(v_stack_p30), a3, (unsigned int)(v_stack_pD0));
    goto loc_00324A5B;
loc_00324E1F:
    result = ExfTryToWakePushLock((unsigned int)(v_stack_p30), (unsigned int)(v_stack_p30), a3, (unsigned int)(v_stack_pD0));
    goto loc_00324B5A;
loc_00324E2C:
    if (((unsigned int)(result)) == 0xC000020AULL) goto loc_00324F90;
loc_00324E37:
    if ((((unsigned __int8)(v_rbp)) & (1)) != 0) {
        a1 = *(unsigned __int64 *)(a1) + 72;
        result = ExAcquireSpinLockExclusive(a1, (unsigned int)(v_stack_p30), a3, (unsigned int)(v_stack_pD0));
        a2 = (unsigned __int8)(result);
        a1 = *(unsigned __int64 *)(a1);
        result = MiCheckControlArea(a1, a2, a3, (unsigned int)(v_stack_pD0));
        a1 = v_stack_pD0;
    }
    goto loc_00324C94;
loc_00324E75:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12488669))) != 0) goto loc_00324B12;
    result = ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented(*(unsigned __int64 *)(a1) + 72, v_stack_pB8, a3, (unsigned int)(v_stack_pD0));
    goto loc_00324B1A;
loc_00324E99:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12488633))) != 0) goto loc_00324C3A;
    result = ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented(*(unsigned __int64 *)(a1) + 72, v_stack_pB8, a3, (unsigned int)(v_stack_pD0));
    goto loc_00324B38;
loc_00324EBD:
    a1 = (v_stack_p48) + (40);
    v_stack_p50 = a1;
    result = (unsigned __int8)((0) & (6));
    if (((unsigned __int8)(result)) == 2) goto loc_00324FA2;
loc_00324EDD:
    result = KeAbPostRelease(a1, v_stack_pB8, a3, (unsigned int)(v_stack_pD0));
    if (((unsigned __int8)(result)) != 2) goto loc_00324D0F;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 152)) == (*(unsigned __int64 *)(gs_base + (0 + 392)) + 152)) goto loc_00324D0F;
    result = KiCheckForKernelApcDelivery(a1, v_stack_pB8, a3, (unsigned int)(v_stack_pD0));
    goto loc_00324D0F;
loc_00324F0D:
    a3 = 0;
    a2 = 0;
    a1 = (v_stack_p48) + (40);
    v_stack_p50 = a1;
    result = KeAbPreAcquire(a1, a2, a3, (unsigned int)(v_stack_pD0));
    v_stack_p38 = result;
    result = v_stack_p50;
    if (!(condition_is_above_or_equal)) {
        a2 = result;
        a3 = v_stack_p50;
        a1 = v_stack_p50;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, (unsigned int)(v_stack_pD0));
        a1 = v_stack_p38;
    }
    if (a1 == 0) goto loc_00324DBB;
    *(unsigned __int8 *)(a1 + 10) = 1;
    goto loc_00324DBB;
loc_00324F68:
loc_00324F6F:
    if (a1 != 0) goto loc_00324F6F;
    if (condition_is_above_or_equal) goto loc_00324C73;
    result = KiRemoveSystemWorkPriorityKick(a1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a3)))), a3, (unsigned int)(v_stack_pD0));
    goto loc_00324C73;
loc_00324F90:
    if ((unsigned int)((unsigned int)(v_stack_p30)) == 0) goto loc_00324FB1;
    result = ExAcquireSpinLockExclusive(*(unsigned __int64 *)(a1) + 72, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a3)))), a3, (unsigned int)(v_stack_pD0));
    goto loc_00324D78;
loc_00324FA2:
    result = ExfTryToWakePushLock(*(unsigned __int64 *)(a1) + 72, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a3)))), a3, (unsigned int)(v_stack_pD0));
    goto loc_00324EDD;
loc_00324FB1:
    a3 = 0;
    a2 = 0;
    a1 = (v_stack_p48) + (40);
    v_stack_p50 = a1;
    result = KeAbPreAcquire(a1, a2, a3, (unsigned int)(v_stack_pD0));
    v_stack_p58 = result;
    result = ExfAcquirePushLockExclusiveEx(v_stack_p50, result, v_stack_p50, (unsigned int)(v_stack_pD0));
loc_00325003:
    result = MiReleaseSpinLockExclusive(*(unsigned __int64 *)(a1) + 72, (unsigned __int8)(v_cr8), v_stack_p50, (unsigned int)(v_stack_pD0));
loc_00325024:
    v_stack_pD0 = 0xC0000018ULL;
    result = MiReleaseSpinLockExclusive(*(unsigned __int64 *)(a1) + 72, (unsigned __int8)(v_cr8), v_stack_p50, (unsigned int)(v_stack_pD0));
    goto loc_00324E37;
}
```

## 5. (Beta) C Style

```c
int64_t MiAddViewsForSection(void *Arg1, int64_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m50;
    uint64_t v_stack_m70;
    uint32_t v_stack_m78;
    uint64_t v_stack_m80;
    uint32_t v_stack_m88;
    uint64_t v_stack_m98;
    uint64_t v_stack_p10;
    uint32_t v_stack_p18;
    uint32_t v_stack_p20;
    uint32_t v_stack_p30;
    uint64_t v_stack_p38;
    uint32_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint32_t v_stack_p58;
    uint64_t v_stack_p68;
    uint64_t v_stack_p8;
    uint64_t v_stack_pB8;
    uint64_t v_stack_pC8;
    uint32_t v_stack_pD0;
    uint32_t v_stack_pD8;

    v_stack_p10 = Arg2;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (120);
    local_rbx = 0;
    v_stack_m88 = Arg3;
    v_stack_m80 = 0;
    if ((*(uint64_t *)(*(uint64_t *)(arg1) + 0x40)) == 0) goto loc_00324BD0;
    v_stack_p20 = 1;
    v_stack_m70 = 0;
loc_003249DF:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg3)))) & (128));
    v_stack_m78 = (uint32_t)(result);
    if ((*(uint32_t *)(v_rip + 0xCA2322)) != 0) goto loc_00324D1F;
loc_00324A04:
    if (((*(uint8_t *)(v_rip + 0xCA20FB)) & (33)) != 0) goto loc_00324CA6;
loc_00324A11:
    result = 2;
    if (!(condition_is_above_or_equal)) {
        Arg2 = (uint8_t)(v_cr8);
        Arg1 = *(uint64_t *)(arg1) + 72;
        result = ExpWaitForSpinLockExclusiveAndAcquire(Arg1, Arg2, Arg3, a4);
        local_rbx = (uint32_t)(result);
    }
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x48)))))) == ((uint32_t)((uint32_t)(0x80000000ULL)))) goto loc_00324A6E;
loc_00324A3C:
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x48)))))) >= ((uint32_t)((uint32_t)(0x80000000ULL)))) {
    }
    local_rbx = (uint32_t)((local_rbx) + 1);
    if (((*(uint32_t *)(v_rip + 0xCA0859)) & ((uint32_t)(local_rbx))) == 0) goto loc_00324DF8;
loc_00324A59:
loc_00324A5B:
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x48)))))) != ((uint32_t)((uint32_t)(0x80000000ULL)))) goto loc_00324A3C;
loc_00324A6E:
    local_rdi = (uint32_t)(Arg3);
    local_rbp = (uint32_t)(Arg3);
    if ((((uint8_t)((uint32_t)(Arg3))) & (1)) != 0) {
        local_rbp = (uint32_t)(((uint32_t)(Arg3)) | (4));
        local_rdi = (uint32_t)(local_rbp);
        v_stack_m88 = (uint32_t)(local_rbp);
    }
loc_00324A8C:
    v_stack_p18 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x2C)));
    v_stack_m50 = Arg1;
    if ((*(uint64_t *)(arg1 + 0x8)) == 0) goto loc_00324CC6;
    if ((*(uint64_t *)(arg1 + 0x8)) < 0) goto loc_00325024;
    result = MiReferenceActiveSubsection(Arg1, (uint32_t)((uint32_t)(local_rdi)), (uint8_t)(v_cr8), a4);
    v_stack_p18 = (uint32_t)(result);
    if (sign_flag) goto loc_00324D66;
    if ((uint32_t)((uint32_t)(v_stack_p20)) != 0) goto loc_00324C47;
loc_00324ADD:
    if (v_stack_p10 == 0) goto loc_00324DD4;
    if (v_stack_p10 > ((uint32_t)(*(uint32_t *)(arg1 + 0x2C)))) goto loc_00324DC9;
loc_00324AFB:
    if (((uint8_t)(v_cr8)) == 17) goto loc_00324C2D;
    if (((*(uint8_t *)(v_rip + 0xCA1FFA)) & (1)) != 0) goto loc_00324E75;
loc_00324B12:
    *(uint32_t *)(*(uint64_t *)(arg1) + 0x48) = 0;
loc_00324B1A:
    result = (uint32_t)(*(uint32_t *)(arg1 + 0x2C));
    if ((*(uint32_t *)(v_rip + 0xCA21FF)) != 0) {
        Arg1 = 2;
        Arg2 = (uint8_t)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, (uint8_t)(v_cr8), a4);
    }
loc_00324B38:
    if ((uint32_t)((uint32_t)(v_stack_p20)) != 0) goto loc_00324C92;
    local_rdi = (v_stack_m70) + (40);
    local_rbx = (uint8_t)((-1) & (6));
    if (((uint8_t)(local_rbx)) == 2) goto loc_00324E1F;
loc_00324B5A:
    a4 = (local_rdi) & (local_rsi);
    local_rbx = 0;
loc_00324B80:
    if (0 >= ((uint32_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x470) + 0xC)))) goto loc_00324BA9;
    local_r10 = (local_r10) * (0);
    local_r10 = (local_r10) + (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x470));
    Arg1 = (*(uint64_t *)(local_r10 + 0x10)) & (local_rsi);
    if (Arg1 == a4) goto loc_00324D30;
loc_00324BA5:
    result = (uint32_t)((0) + 1);
    goto loc_00324B80;
loc_00324BA9:
    if (Arg1 < a4) goto loc_00324C5A;
    a4 = 0;
    v_stack_m98 = 0;
    result = KeBugCheckEx(354, *(uint64_t *)(gs_base + (0 + 0x188)), local_rdi, a4);
loc_00324BD0:
    Arg3 = 0;
    Arg2 = 0;
    v_stack_p20 = 0;
    v_stack_m70 = *(uint64_t *)(*(uint64_t *)(arg1));
    result = KeAbPreAcquire(*(uint64_t *)(*(uint64_t *)(arg1)) + 40, Arg2, Arg3, a4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = *(uint64_t *)(*(uint64_t *)(arg1)) + 40;
        Arg2 = result;
        Arg1 = *(uint64_t *)(*(uint64_t *)(arg1)) + 40;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, a4);
    }
    local_rbx = 0;
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    goto loc_003249DF;
loc_00324C2D:
    if (((*(uint8_t *)(v_rip + 0xCA1ED2)) & (1)) != 0) goto loc_00324E99;
loc_00324C3A:
    *(uint32_t *)(*(uint64_t *)(arg1) + 0x48) = 0;
    goto loc_00324B38;
loc_00324C47:
    if (condition_is_above_or_equal) goto loc_00324ADD;
loc_00324C5A:
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) != 0) goto loc_00324F68;
loc_00324C73:
loc_00324C74:
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) != 0) goto loc_00324C92;
    result = *(uint64_t *)(gs_base + (0 + 0x188)) + 152;
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x98)) != (*(uint64_t *)(gs_base + (0 + 0x188)) + 152)) {
        result = KiCheckForKernelApcDelivery(*(uint64_t *)(gs_base + (0 + 0x20)), Arg2, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), a4);
    }
    result = 0;
loc_00324C94:
    local_rsp = (local_rsp) + (120);
    return result;
loc_00324CA6:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBE91AC))) != 0) goto loc_00324A11;
    result = ExpAcquireSpinLockExclusiveAtDpcLevelInstrumented(*(uint64_t *)(arg1) + 72, (uint8_t)(v_cr8), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), a4);
    goto loc_00324A6E;
loc_00324CC6:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x34))) & (0x3FFFFFFFULL));
    v_stack_p58 = (uint32_t)(result);
    result = ExReleaseSpinLockExclusiveFromDpcLevel(*(uint64_t *)(arg1) + 72, (uint8_t)(v_cr8), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), a4);
    if (((uint8_t)(v_cr8)) == 17) goto loc_00324D00;
    if ((*(uint32_t *)(v_rip + 0xCA2037)) != 0) {
        Arg1 = (uint8_t)(v_cr8);
        Arg2 = (uint8_t)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), a4);
    }
loc_00324D00:
    if ((uint32_t)((uint32_t)(v_stack_pD8)) == 0) goto loc_00324EBD;
loc_00324D0F:
    if ((((uint8_t)(local_rbp)) & (2)) == 0) goto loc_00324D8A;
    goto loc_00324C94;
loc_00324D1F:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(v_cr8), (uint8_t)((uint32_t)(0xC0000189ULL)), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), a4);
    goto loc_00324A04;
loc_00324D30:
    if ((*(uint8_t *)(local_r10 + 0x1A)) == 0) goto loc_00324BA5;
    if ((((uint8_t)((uint8_t)((uint32_t)(0xC0000189ULL)))) & (1)) != 0) goto loc_00324BA5;
    *(uint8_t *)(local_r10 + 0x1A) = 0;
    v_stack_p20 = 0;
    result = KiAbEntryFreeAndEnableInterrupts(local_r10 + 16, *(uint64_t *)(gs_base + (0 + 0x188)), (uint32_t)(v_stack_pD8), 1);
    goto loc_00324C74;
loc_00324D66:
    if (((uint32_t)(result)) != 0xC000020AULL) goto loc_00325003;
loc_00324D78:
    if (Arg1 == NULL) goto loc_00324AFB;
    goto loc_00324A8C;
loc_00324D8A:
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_pD0)))) - (v_stack_p58));
    result = MiCreatePrototypePtes(Arg1, (uint32_t)(v_stack_p30), Arg3, (uint32_t)(v_stack_pD0));
    v_stack_pD0 = (uint32_t)(result);
    if (sign_flag) goto loc_00324E2C;
    if ((uint32_t)((uint32_t)(v_stack_p30)) == 0) goto loc_00324F0D;
loc_00324DBB:
    result = ExAcquireSpinLockExclusive(*(uint64_t *)(arg1) + 72, (uint32_t)(v_stack_p30), Arg3, (uint32_t)(v_stack_pD0));
    goto loc_00324ADD;
loc_00324DC9:
    Arg1 = (*(uint64_t *)(arg1) + 72) - (result);
    v_stack_pC8 = Arg1;
loc_00324DD4:
    v_stack_p38 = v_stack_p68;
    if ((uint32_t)((uint32_t)(v_stack_p30)) != 0) goto loc_00324D78;
    result = (uint32_t)(((uint32_t)(v_stack_p40)) | (4));
    v_stack_p38 = v_stack_p68;
    v_stack_p30 = (uint32_t)(result);
    goto loc_00324D78;
loc_00324DF8:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCA1CBA)))) & (64)) == 0) goto loc_00324A59;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_stack_p68, (uint32_t)(v_stack_p30), Arg3, (uint32_t)(v_stack_pD0));
    if ((uint8_t)(result) == 0) goto loc_00324A59;
    result = HvlNotifyLongSpinWait(0, (uint32_t)(v_stack_p30), Arg3, (uint32_t)(v_stack_pD0));
    goto loc_00324A5B;
loc_00324E1F:
    result = ExfTryToWakePushLock((uint32_t)(v_stack_p30), (uint32_t)(v_stack_p30), Arg3, (uint32_t)(v_stack_pD0));
    goto loc_00324B5A;
loc_00324E2C:
    if (((uint32_t)(result)) == 0xC000020AULL) goto loc_00324F90;
loc_00324E37:
    if ((((uint8_t)(local_rbp)) & (1)) != 0) {
        Arg1 = *(uint64_t *)(arg1) + 72;
        result = ExAcquireSpinLockExclusive(Arg1, (uint32_t)(v_stack_p30), Arg3, (uint32_t)(v_stack_pD0));
        Arg2 = (uint8_t)(result);
        Arg1 = *(uint64_t *)(arg1);
        result = MiCheckControlArea(Arg1, Arg2, Arg3, (uint32_t)(v_stack_pD0));
        Arg1 = v_stack_pD0;
    }
    goto loc_00324C94;
loc_00324E75:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBE8FDD))) != 0) goto loc_00324B12;
    result = ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented(*(uint64_t *)(arg1) + 72, v_stack_pB8, Arg3, (uint32_t)(v_stack_pD0));
    goto loc_00324B1A;
loc_00324E99:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBE8FB9))) != 0) goto loc_00324C3A;
    result = ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented(*(uint64_t *)(arg1) + 72, v_stack_pB8, Arg3, (uint32_t)(v_stack_pD0));
    goto loc_00324B38;
loc_00324EBD:
    Arg1 = (v_stack_p48) + (40);
    v_stack_p50 = Arg1;
    result = (uint8_t)((0) & (6));
    if (((uint8_t)(result)) == 2) goto loc_00324FA2;
loc_00324EDD:
    result = KeAbPostRelease(Arg1, v_stack_pB8, Arg3, (uint32_t)(v_stack_pD0));
    if (((uint8_t)(result)) != 2) goto loc_00324D0F;
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x98)) == (*(uint64_t *)(gs_base + (0 + 0x188)) + 152)) goto loc_00324D0F;
    result = KiCheckForKernelApcDelivery(Arg1, v_stack_pB8, Arg3, (uint32_t)(v_stack_pD0));
    goto loc_00324D0F;
loc_00324F0D:
    Arg3 = 0;
    Arg2 = 0;
    Arg1 = (v_stack_p48) + (40);
    v_stack_p50 = Arg1;
    result = KeAbPreAcquire(Arg1, Arg2, Arg3, (uint32_t)(v_stack_pD0));
    v_stack_p38 = result;
    result = v_stack_p50;
    if (!(condition_is_above_or_equal)) {
        Arg2 = result;
        Arg3 = v_stack_p50;
        Arg1 = v_stack_p50;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, (uint32_t)(v_stack_pD0));
        Arg1 = v_stack_p38;
    }
    if (Arg1 == NULL) goto loc_00324DBB;
    *(uint8_t *)(arg1 + 0xA) = 1;
    goto loc_00324DBB;
loc_00324F68:
loc_00324F6F:
    if (Arg1 != NULL) goto loc_00324F6F;
    if (condition_is_above_or_equal) goto loc_00324C73;
    result = KiRemoveSystemWorkPriorityKick(Arg1, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg3)))), Arg3, (uint32_t)(v_stack_pD0));
    goto loc_00324C73;
loc_00324F90:
    if ((uint32_t)((uint32_t)(v_stack_p30)) == 0) goto loc_00324FB1;
    result = ExAcquireSpinLockExclusive(*(uint64_t *)(arg1) + 72, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg3)))), Arg3, (uint32_t)(v_stack_pD0));
    goto loc_00324D78;
loc_00324FA2:
    result = ExfTryToWakePushLock(*(uint64_t *)(arg1) + 72, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg3)))), Arg3, (uint32_t)(v_stack_pD0));
    goto loc_00324EDD;
loc_00324FB1:
    Arg3 = 0;
    Arg2 = 0;
    Arg1 = (v_stack_p48) + (40);
    v_stack_p50 = Arg1;
    result = KeAbPreAcquire(Arg1, Arg2, Arg3, (uint32_t)(v_stack_pD0));
    v_stack_p58 = result;
    result = ExfAcquirePushLockExclusiveEx(v_stack_p50, result, v_stack_p50, (uint32_t)(v_stack_pD0));
loc_00325003:
    result = MiReleaseSpinLockExclusive(*(uint64_t *)(arg1) + 72, (uint8_t)(v_cr8), v_stack_p50, (uint32_t)(v_stack_pD0));
loc_00325024:
    v_stack_pD0 = 0xC0000018ULL;
    result = MiReleaseSpinLockExclusive(*(uint64_t *)(arg1) + 72, (uint8_t)(v_cr8), v_stack_p50, (uint32_t)(v_stack_pD0));
    goto loc_00324E37;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00324990&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
