# IopReleaseFileObjectLock

- RVA: `0x00250A90`–`0x00250F19` (길이 `1,161` bytes)
- VA: `0x0000000140250A90`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00063464`
- 디코드: `284`개 명령, `1,161/1,161` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **23**; 고유 호출 대상: **19**
- 직접 호출자로 확인된 함수: **22**
- RIP 상대 이미지 참조: **9**

### Outgoing calls
- `0x00250B68` → [KiExitDispatcher](KiExitDispatcher_function_00251CF0.md) (function, `0x00251CF0`)
- `0x00250BE3` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00250C0C` → [KiTryUnwaitThread](../35/KiTryUnwaitThread_function_003506D0.md) (function, `0x003506D0`)
- `0x00250C26` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x00250C4A` → [KeAbPreWakeupThread](../35/KeAbPreWakeupThread_function_0035034C.md) (function, `0x0035034C`)
- `0x00250C68` → [KiInsertQueueInternal](../21/KiInsertQueueInternal_function_00219B30.md) (function, `0x00219B30`)
- `0x00250CBE` → [KiAbEntryFreeAndEnableInterrupts](../26/KiAbEntryFreeAndEnableInterrupts_function_002622D0.md) (function, `0x002622D0`)
- `0x00250CFB` → [ObpPushStackInfo](../21/ObpPushStackInfo_function_002109E4.md) (function, `0x002109E4`)
- `0x00250D1B` → [KeLeaveCriticalRegionThread](KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x00250D57` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00250D99` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00250DB6` → [KeAreInterruptsEnabled](../2F/KeAreInterruptsEnabled_function_002F8060.md) (function, `0x002F8060`)
- `0x00250DE3` → [ObpDeregisterObject](../../page/9D/ObpDeregisterObject_function_009D7F78.md) (function, `0x009D7F78`)
- `0x00250DED` → [ObpRemoveObjectRoutine](../../page/86/ObpRemoveObjectRoutine_function_00864A60.md) (function, `0x00864A60`)
- `0x00250E19` → [ObpHandleRevocationBlockRemoveObject](../../page/9D/ObpHandleRevocationBlockRemoveObject_function_009D7E30.md) (function, `0x009D7E30`)
- `0x00250E2E` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00250E3D` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00250E5B` → [KiTryUnwaitThread](../35/KiTryUnwaitThread_function_003506D0.md) (function, `0x003506D0`)
- `0x00250E83` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x00250E9F` → [KeInsertQueueDpc](../20/KeInsertQueueDpc_function_00207C50.md) (function, `0x00207C50`)
- `0x00250EE7` → [KeGetEffectiveIrql](../2F/KeGetEffectiveIrql_function_002F8030.md) (function, `0x002F8030`)
- `0x00250EF9` → [ExQueueWorkItem](../2F/ExQueueWorkItem_function_002F9520.md) (function, `0x002F9520`)
- `0x00250F0F` → [KeInsertQueueDpc](../20/KeInsertQueueDpc_function_00207C50.md) (function, `0x00207C50`)

### Direct callers
- [NtSetInformationFile](../29/NtSetInformationFile_function_0029C5E0.md) at `0x0029C8A3`
- [NtSetInformationFile](../29/NtSetInformationFile_function_0029C5E0.md) at `0x0029C93A`
- [NtSetInformationFile](../29/NtSetInformationFile_function_0029C5E0.md) at `0x0029CE03`
- [NtSetInformationFile](../29/NtSetInformationFile_function_0029C5E0.md) at `0x0029CE53`
- [NtSetInformationFile](../29/NtSetInformationFile_function_0029C5E0.md) at `0x0029D261`
- [IopValidateAndGetWriteParameters](../40/IopValidateAndGetWriteParameters_function_00400C30.md) at `0x00401056`
- [IopAllocateAndPopulateWriteIrp](../40/IopAllocateAndPopulateWriteIrp_function_004011F4.md) at `0x00401564`
- [IoSetInformation](../../page/71/IoSetInformation_function_0071DBF0.md) at `0x0071DF35`
- [IopCloseFile](../../page/86/IopCloseFile_function_008640C0.md) at `0x00864288`
- [IopGetSetSecurityObject](../../page/87/IopGetSetSecurityObject_function_00873A80.md) at `0x00873D5B`
- [IopGetSetSecurityObject](../../page/87/IopGetSetSecurityObject_function_00873A80.md) at `0x00874047`
- [sub_008A8BD4](../../page/8A/Unknown_function_008A8BD4.md) at `0x008A8BFB`
- [sub_008A8C40](../../page/8A/Unknown_function_008A8C40.md) at `0x008A8C5C`
- [NtQueryEaFile](../../page/8A/NtQueryEaFile_function_008AC1B0.md) at `0x008AC87C`
- [NtQueryVolumeInformationFile](../../page/8A/NtQueryVolumeInformationFile_function_008AC8C0.md) at `0x008ACE07`
- [IopFlushBuffersFile](../../page/8A/IopFlushBuffersFile_function_008ACFA4.md) at `0x008AD37C`
- [NtQueryInformationFile](../../page/8A/NtQueryInformationFile_function_008AD630.md) at `0x008ADBA9`
- [NtQueryInformationFile](../../page/8A/NtQueryInformationFile_function_008AD630.md) at `0x008ADD6C`
- [NtQueryInformationFile](../../page/8A/NtQueryInformationFile_function_008AD630.md) at `0x008AE331`
- [IopExceptionCleanupEx](../../page/8A/IopExceptionCleanupEx_function_008AE5C8.md) at `0x008AE63D`
- [IopReadFile](../../page/8A/IopReadFile_function_008AEFF0.md) at `0x008AF447`
- [IopReadFile](../../page/8A/IopReadFile_function_008AEFF0.md) at `0x008AF5AD`
- [IopReadFile](../../page/8A/IopReadFile_function_008AEFF0.md) at `0x008AF5E9`
- [IopReadFile](../../page/8A/IopReadFile_function_008AEFF0.md) at `0x008AF66C`
- [IopWriteFile](../../page/8E/IopWriteFile_function_008E9790.md) at `0x008E99DA`
- [IopXxxControlFile](../../page/8E/IopXxxControlFile_function_008E9AD0.md) at `0x008EA0C4`
- [IopXxxControlFile](../../page/8E/IopXxxControlFile_function_008E9AD0.md) at `0x008EA69A`
- [IopXxxControlFile](../../page/8E/IopXxxControlFile_function_008E9AD0.md) at `0x008EB3BC`
- [IopSynchronousServiceTail](../../page/8E/IopSynchronousServiceTail_function_008EB440.md) at `0x008EB830`
- [NtLockFile](../../page/9D/NtLockFile_function_009D86D0.md) at `0x009D8D37`
- [NtUnlockFile](../../page/9E/NtUnlockFile_function_009E5DA0.md) at `0x009E61E0`
- [IopAllocateIrpCleanup](../../page/A1/IopAllocateIrpCleanup_function_00A1E2D4.md) at `0x00A1E305`
- [sub_00B174A6](../../page/B1/Unknown_function_00B174A6.md) at `0x00B17659`
- [sub_00B1A4B8](../../page/B1/Unknown_function_00B1A4B8.md) at `0x00B1A55B`

### Static image references
- `0x00250AE6` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x00250C74` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x00250CDF` → RVA `0x00FC5010` (`ALMOSTRO`; read)
- `0x00250D68` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x00250D87` → RVA `0x00FC6E4C` (`ALMOSTRO`; read)
- `0x00250E20` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x00250EA9` → RVA `0x00F0F640` (`.data`; read)
- `0x00250EF2` → RVA `0x00F0F620` (`.data`; read)
- `0x00250F06` → RVA `0x00F0F5E0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00250DE3` → [ObpDeregisterObject](../../page/9D/ObpDeregisterObject_function_009D7F78.md) (`.text` → `PAGE`)
  - `0x00250DED` → [ObpRemoveObjectRoutine](../../page/86/ObpRemoveObjectRoutine_function_00864A60.md) (`.text` → `PAGE`)
  - `0x00250E19` → [ObpHandleRevocationBlockRemoveObject](../../page/9D/ObpHandleRevocationBlockRemoveObject_function_009D7E30.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00250A90  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00250A95  55                              push rbp
00250A96  56                              push rsi
00250A97  57                              push rdi
00250A98  41 54                           push r12
00250A9A  41 55                           push r13
00250A9C  41 56                           push r14
00250A9E  41 57                           push r15
00250AA0  48 83 EC 30                     sub rsp, 0x30
00250AA4  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00250AAD  48 8D 99 80 00 00 00            lea rbx, [rcx + 0x80]
00250AB4  45 33 ED                        xor r13d, r13d
00250AB7  48 8B F9                        mov rdi, rcx
00250ABA  4C 89 AC 24 80 00 00 00         mov qword ptr [rsp + 0x80], r13
00250AC2  44 0F B6 B8 C3 00 00 00         movzx r15d, byte ptr [rax + 0xc3]
00250ACA  41 8B C5                        mov eax, r13d
00250ACD  87 41 74                        xchg dword ptr [rcx + 0x74], eax
00250AD0  41 8D 6D 02                     lea ebp, [r13 + 2]
00250AD4  44 39 69 70                     cmp dword ptr [rcx + 0x70], r13d
00250AD8  0F 84 94 00 00 00               je 0x140250b72
00250ADE  45 0F 20 C4                     mov r12, cr8
00250AE2  44 0F 22 C5                     mov cr8, rbp
00250AE6  44 39 2D 33 62 D7 00            cmp dword ptr [rip + 0xd76233], r13d
00250AED  0F 85 2B 01 00 00               jne 0x140250c1e
00250AF3  65 48 8B 2C 25 20 00 00 00      mov rbp, qword ptr gs:[0x20]
00250AFC  41 8B F5                        mov esi, r13d
00250AFF  F0 0F BA 2B 07                  lock bts dword ptr [rbx], 7
00250B04  0F 82 68 01 00 00               jb 0x140250c72
00250B0A  48 8B 73 08                     mov rsi, qword ptr [rbx + 8]
00250B0E  4C 8D 73 08                     lea r14, [rbx + 8]
00250B12  C7 43 04 01 00 00 00            mov dword ptr [rbx + 4], 1
00250B19  49 3B F6                        cmp rsi, r14
00250B1C  74 29                           je 0x140250b47
00250B1E  48 8B 16                        mov rdx, qword ptr [rsi]
00250B21  48 8B C6                        mov rax, rsi
00250B24  48 8B F2                        mov rsi, rdx
00250B27  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
00250B2B  48 39 42 08                     cmp qword ptr [rdx + 8], rax
00250B2F  75 09                           jne 0x140250b3a
00250B31  48 39 01                        cmp qword ptr [rcx], rax
00250B34  0F 84 AF 00 00 00               je 0x140250be9
00250B3A  B9 03 00 00 00                  mov ecx, 3
00250B3F  CD 29                           int 0x29
00250B41  83 6B 04 01                     sub dword ptr [rbx + 4], 1
00250B45  75 D2                           jne 0x140250b19
00250B47  F0 81 23 7F FF FF FF            lock and dword ptr [rbx], 0xffffff7f
00250B4E  45 84 FF                        test r15b, r15b
00250B51  0F 85 D9 00 00 00               jne 0x140250c30
00250B57  45 33 C9                        xor r9d, r9d
00250B5A  44 88 64 24 20                  mov byte ptr [rsp + 0x20], r12b
00250B5F  33 D2                           xor edx, edx
00250B61  48 8B CD                        mov rcx, rbp
00250B64  45 8D 41 01                     lea r8d, [r9 + 1]
00250B68  E8 83 11 00 00                  call 0x140251cf0
00250B6D  BD 02 00 00 00                  mov ebp, 2
00250B72  65 4C 8B 14 25 88 01 00 00      mov r10, qword ptr gs:[0x188]
00250B7B  FA                              cli
00250B7C  4D 8B 82 70 04 00 00            mov r8, qword ptr [r10 + 0x470]
00250B83  4C 8B CB                        mov r9, rbx
00250B86  48 BE FC FF FF FF FF FF FF 7F   movabs rsi, 0x7ffffffffffffffc
00250B90  41 8B D5                        mov edx, r13d
00250B93  4C 23 CE                        and r9, rsi
00250B96  41 0F B6 40 0C                  movzx eax, byte ptr [r8 + 0xc]
00250B9B  3B D0                           cmp edx, eax
00250B9D  73 23                           jae 0x140250bc2
00250B9F  8B C2                           mov eax, edx
00250BA1  48 6B C8 58                     imul rcx, rax, 0x58
00250BA5  48 83 C1 10                     add rcx, 0x10
00250BA9  49 03 C8                        add rcx, r8
00250BAC  4C 8B 19                        mov r11, qword ptr [rcx]
00250BAF  49 8B C3                        mov rax, r11
00250BB2  48 23 C6                        and rax, rsi
00250BB5  49 3B C1                        cmp rax, r9
00250BB8  0F 84 D7 00 00 00               je 0x140250c95
00250BBE  FF C2                           inc edx
00250BC0  EB D4                           jmp 0x140250b96
00250BC2  41 8B 42 78                     mov eax, dword ptr [r10 + 0x78]
00250BC6  0F BA E0 10                     bt eax, 0x10
00250BCA  0F 82 F5 00 00 00               jb 0x140250cc5
00250BD0  45 33 C9                        xor r9d, r9d
00250BD3  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00250BD8  4C 8B C3                        mov r8, rbx
00250BDB  49 8B D2                        mov rdx, r10
00250BDE  B9 62 01 00 00                  mov ecx, 0x162
00250BE3  E8 78 CA 2A 00                  call 0x1404fd660
00250BE8  CC                              int3
00250BE9  48 89 11                        mov qword ptr [rcx], rdx
00250BEC  48 89 4A 08                     mov qword ptr [rdx + 8], rcx
00250BF0  0F B6 48 10                     movzx ecx, byte ptr [rax + 0x10]
00250BF4  80 F9 01                        cmp cl, 1
00250BF7  75 5B                           jne 0x140250c54
00250BF9  44 0F B7 40 12                  movzx r8d, word ptr [rax + 0x12]
00250BFE  4C 8D 8C 24 80 00 00 00         lea r9, [rsp + 0x80]
00250C06  48 8B D0                        mov rdx, rax
00250C09  48 8B CD                        mov rcx, rbp
00250C0C  E8 BF FA 0F 00                  call 0x1403506d0
00250C11  84 C0                           test al, al
00250C13  0F 84 00 FF FF FF               je 0x140250b19
00250C19  E9 23 FF FF FF                  jmp 0x140250b41
00250C1E  40 0F B6 D5                     movzx edx, bpl
00250C22  41 0F B6 CC                     movzx ecx, r12b
00250C26  E8 D1 4A 2A 00                  call 0x1404f56fc
00250C2B  E9 C3 FE FF FF                  jmp 0x140250af3
00250C30  48 8B 8D 08 2D 00 00            mov rcx, qword ptr [rbp + 0x2d08]
00250C37  48 85 C9                        test rcx, rcx
00250C3A  0F 84 17 FF FF FF               je 0x140250b57
00250C40  48 81 C1 28 FF FF FF            add rcx, -0xd8
00250C47  48 8B D3                        mov rdx, rbx
00250C4A  E8 FD F6 0F 00                  call 0x14035034c
00250C4F  E9 03 FF FF FF                  jmp 0x140250b57
00250C54  80 F9 02                        cmp cl, 2
00250C57  0F 85 EA 01 00 00               jne 0x140250e47
00250C5D  C6 40 11 05                     mov byte ptr [rax + 0x11], 5
00250C61  48 8B D0                        mov rdx, rax
00250C64  48 8B 48 18                     mov rcx, qword ptr [rax + 0x18]
00250C68  E8 C3 8E FC FF                  call 0x140219b30
00250C6D  E9 CF FE FF FF                  jmp 0x140250b41
00250C72  FF C6                           inc esi
00250C74  85 35 32 46 D7 00               test dword ptr [rip + 0xd74632], esi
00250C7A  0F 84 A0 01 00 00               je 0x140250e20
00250C80  F3 90                           pause
00250C82  8B 03                           mov eax, dword ptr [rbx]
00250C84  84 C0                           test al, al
00250C86  78 EA                           js 0x140250c72
00250C88  F0 0F BA 2B 07                  lock bts dword ptr [rbx], 7
00250C8D  0F 83 77 FE FF FF               jae 0x140250b0a
00250C93  EB DD                           jmp 0x140250c72
00250C95  44 38 69 0A                     cmp byte ptr [rcx + 0xa], r13b
00250C99  0F 84 1F FF FF FF               je 0x140250bbe
00250C9F  41 F6 C3 01                     test r11b, 1
00250CA3  0F 85 15 FF FF FF               jne 0x140250bbe
00250CA9  41 B9 01 00 00 00               mov r9d, 1
00250CAF  44 88 69 0A                     mov byte ptr [rcx + 0xa], r13b
00250CB3  4C 8B C3                        mov r8, rbx
00250CB6  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00250CBB  49 8B D2                        mov rdx, r10
00250CBE  E8 0D 16 01 00                  call 0x1402622d0
00250CC3  EB 1A                           jmp 0x140250cdf
00250CC5  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
00250CCE  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
00250CD5  4D 85 C0                        test r8, r8
00250CD8  0F 85 87 01 00 00               jne 0x140250e65
00250CDE  FB                              sti
00250CDF  44 39 2D 2A 43 D7 00            cmp dword ptr [rip + 0xd7432a], r13d
00250CE6  48 8D 5F D0                     lea rbx, [rdi - 0x30]
00250CEA  74 14                           je 0x140250d00
00250CEC  33 D2                           xor edx, edx
00250CEE  41 B9 44 66 6C 74               mov r9d, 0x746c6644
00250CF4  48 8B CB                        mov rcx, rbx
00250CF7  44 8D 42 01                     lea r8d, [rdx + 1]
00250CFB  E8 E4 FC FB FF                  call 0x1402109e4
00250D00  48 C7 C0 FF FF FF FF            mov rax, 0xffffffffffffffff
00250D07  F0 48 0F C1 03                  lock xadd qword ptr [rbx], rax
00250D0C  48 83 E8 01                     sub rax, 1
00250D10  7E 27                           jle 0x140250d39
00250D12  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00250D1B  E8 D0 E2 00 00                  call 0x14025eff0
00250D20  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
00250D28  48 83 C4 30                     add rsp, 0x30
00250D2C  41 5F                           pop r15
00250D2E  41 5E                           pop r14
00250D30  41 5D                           pop r13
00250D32  41 5C                           pop r12
00250D34  5F                              pop rdi
00250D35  5E                              pop rsi
00250D36  5D                              pop rbp
00250D37  C3                              ret
00250D38  CC                              int3
00250D39  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
00250D3D  48 85 C9                        test rcx, rcx
00250D40  75 1B                           jne 0x140250d5d
00250D42  48 85 C0                        test rax, rax
00250D45  79 58                           jns 0x140250d9f
00250D47  33 D2                           xor edx, edx
00250D49  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00250D4E  4C 8B CD                        mov r9, rbp
00250D51  4C 8B C7                        mov r8, rdi
00250D54  8D 4A 18                        lea ecx, [rdx + 0x18]
00250D57  E8 04 C9 2A 00                  call 0x1404fd660
00250D5C  CC                              int3
00250D5D  41 B9 01 00 00 00               mov r9d, 1
00250D63  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00250D68  4C 8D 15 91 F2 DA FF            lea r10, [rip - 0x250d6f]
00250D6F  48 8B C3                        mov rax, rbx
00250D72  48 C1 E8 08                     shr rax, 8
00250D76  4C 8B C7                        mov r8, rdi
00250D79  0F B6 D0                        movzx edx, al
00250D7C  0F B6 43 18                     movzx eax, byte ptr [rbx + 0x18]
00250D80  41 8D 49 17                     lea ecx, [r9 + 0x17]
00250D84  48 33 D0                        xor rdx, rax
00250D87  0F B6 05 BE 60 D7 00            movzx eax, byte ptr [rip + 0xd760be]
00250D8E  48 33 D0                        xor rdx, rax
00250D91  49 8B 94 D2 00 78 FC 00         mov rdx, qword ptr [r10 + rdx*8 + 0xfc7800]
00250D99  E8 C2 C8 2A 00                  call 0x1404fd660
00250D9E  CC                              int3
00250D9F  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00250DA8  66 44 39 A8 E6 01 00 00         cmp word ptr [rax + 0x1e6], r13w
00250DB0  0F 85 F3 00 00 00               jne 0x140250ea9
00250DB6  E8 A5 72 0A 00                  call 0x1402f8060
00250DBB  84 C0                           test al, al
00250DBD  0F 84 E6 00 00 00               je 0x140250ea9
00250DC3  44 0F 20 C0                     mov rax, cr8
00250DC7  3C 01                           cmp al, 1
00250DC9  0F 83 DA 00 00 00               jae 0x140250ea9
00250DCF  0F B6 43 1A                     movzx eax, byte ptr [rbx + 0x1a]
00250DD3  A8 40                           test al, 0x40
00250DD5  75 20                           jne 0x140250df7
00250DD7  44 39 2D 32 42 D7 00            cmp dword ptr [rip + 0xd74232], r13d
00250DDE  74 08                           je 0x140250de8
00250DE0  48 8B CB                        mov rcx, rbx
00250DE3  E8 90 71 78 00                  call 0x1409d7f78
00250DE8  33 D2                           xor edx, edx
00250DEA  48 8B CB                        mov rcx, rbx
00250DED  E8 6E 3C 61 00                  call 0x140864a60
00250DF2  E9 1B FF FF FF                  jmp 0x140250d12
00250DF7  83 E0 7F                        and eax, 0x7f
00250DFA  4C 8D 15 FF F1 DA FF            lea r10, [rip - 0x250e01]
00250E01  48 8B CB                        mov rcx, rbx
00250E04  42 0F B6 84 10 80 FF F0 00      movzx eax, byte ptr [rax + r10 + 0xf0ff80]
00250E0D  48 2B C8                        sub rcx, rax
00250E10  48 8B 09                        mov rcx, qword ptr [rcx]
00250E13  44 38 69 18                     cmp byte ptr [rcx + 0x18], r13b
00250E17  74 BE                           je 0x140250dd7
00250E19  E8 12 70 78 00                  call 0x1409d7e30
00250E1E  EB B7                           jmp 0x140250dd7
00250E20  8B 05 92 5C D7 00               mov eax, dword ptr [rip + 0xd75c92]
00250E26  A8 40                           test al, 0x40
00250E28  0F 84 52 FE FF FF               je 0x140250c80
00250E2E  E8 5D E6 0B 00                  call 0x14030f490
00250E33  84 C0                           test al, al
00250E35  0F 84 45 FE FF FF               je 0x140250c80
00250E3B  8B CE                           mov ecx, esi
00250E3D  E8 1E E6 0B 00                  call 0x14030f460
00250E42  E9 3B FE FF FF                  jmp 0x140250c82
00250E47  80 F9 04                        cmp cl, 4
00250E4A  74 41                           je 0x140250e8d
00250E4C  45 33 C9                        xor r9d, r9d
00250E4F  41 B8 00 01 00 00               mov r8d, 0x100
00250E55  48 8B D0                        mov rdx, rax
00250E58  48 8B CD                        mov rcx, rbp
00250E5B  E8 70 F8 0F 00                  call 0x1403506d0
00250E60  E9 B4 FC FF FF                  jmp 0x140250b19
00250E65  41 0F 0D 08                     prefetchw byte ptr [r8]
00250E69  41 8B 00                        mov eax, dword ptr [r8]
00250E6C  8B D0                           mov edx, eax
00250E6E  0F BA F2 15                     btr edx, 0x15
00250E72  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
00250E77  75 F3                           jne 0x140250e6c
00250E79  0F BA E0 15                     bt eax, 0x15
00250E7D  0F 83 5B FE FF FF               jae 0x140250cde
00250E83  E8 48 23 01 00                  call 0x1402631d0
00250E88  E9 51 FE FF FF                  jmp 0x140250cde
00250E8D  C6 40 11 05                     mov byte ptr [rax + 0x11], 5
00250E91  4C 8B C0                        mov r8, rax
00250E94  44 89 6B 04                     mov dword ptr [rbx + 4], r13d
00250E98  48 8B D3                        mov rdx, rbx
00250E9B  48 8B 48 18                     mov rcx, qword ptr [rax + 0x18]
00250E9F  E8 AC 6D FB FF                  call 0x140207c50
00250EA4  E9 70 FC FF FF                  jmp 0x140250b19
00250EA9  0F 0D 0D 90 E7 CB 00            prefetchw byte ptr [rip + 0xcbe790]
00250EB0  48 8B 0D 89 E7 CB 00            mov rcx, qword ptr [rip + 0xcbe789]
00250EB7  48 89 4B 08                     mov qword ptr [rbx + 8], rcx
00250EBB  48 8B C1                        mov rax, rcx
00250EBE  F0 48 0F B1 1D 79 E7 CB 00      lock cmpxchg qword ptr [rip + 0xcbe779], rbx
00250EC7  74 15                           je 0x140250ede
00250EC9  48 8B C8                        mov rcx, rax
00250ECC  48 89 43 08                     mov qword ptr [rbx + 8], rax
00250ED0  F0 48 0F B1 1D 67 E7 CB 00      lock cmpxchg qword ptr [rip + 0xcbe767], rbx
00250ED9  48 3B C1                        cmp rax, rcx
00250EDC  75 EB                           jne 0x140250ec9
00250EDE  48 85 C9                        test rcx, rcx
00250EE1  0F 85 2B FE FF FF               jne 0x140250d12
00250EE7  E8 44 71 0A 00                  call 0x1402f8030
00250EEC  3C 02                           cmp al, 2
00250EEE  77 13                           ja 0x140250f03
00250EF0  33 D2                           xor edx, edx
00250EF2  48 8D 0D 27 E7 CB 00            lea rcx, [rip + 0xcbe727]
00250EF9  E8 22 86 0A 00                  call 0x1402f9520
00250EFE  E9 0F FE FF FF                  jmp 0x140250d12
00250F03  45 33 C0                        xor r8d, r8d
00250F06  48 8D 0D D3 E6 CB 00            lea rcx, [rip + 0xcbe6d3]
00250F0D  33 D2                           xor edx, edx
00250F0F  E8 3C 6D FB FF                  call 0x140207c50
00250F14  E9 F9 FD FF FF                  jmp 0x140250d12
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopReleaseFileObjectLock(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int8 v_stack_m48;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;

    v_stack_p20 = v_rbx;
    v_rsp = (v_rsp) - (48);
    v_r13 = 0;
    v_stack_p18 = 0;
    if ((*(unsigned int *)(a1 + 112)) == 0) goto loc_00250B72;
    if ((*(unsigned int *)(v_rip + 14115379)) != 0) goto loc_00250C1E;
loc_00250AF3:
    if ((*(unsigned int *)(v_rip + 14115379)) < 0) goto loc_00250C72;
loc_00250B0A:
    *(unsigned int *)(a1 + 128 + 4) = 1;
loc_00250B19:
    if ((*(unsigned __int64 *)(a1 + 128 + 8)) == (a1 + 128 + 8)) goto loc_00250B47;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 128 + 8)) + 8)) != (*(unsigned __int64 *)(a1 + 128 + 8))) goto loc_00250B3A;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 128 + 8) + 8))) == (*(unsigned __int64 *)(a1 + 128 + 8))) goto loc_00250BE9;
loc_00250B3A:
loc_00250B41:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 128 + 8) + 8))) != (*(unsigned __int64 *)(a1 + 128 + 8))) goto loc_00250B19;
loc_00250B47:
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 195)) != 0) goto loc_00250C30;
loc_00250B57:
    a4 = 0;
    v_stack_m48 = (unsigned __int8)(v_cr8);
    a2 = 0;
    result = KiExitDispatcher(*(unsigned __int64 *)(gs_base + (0 + 32)), a2, a4 + 1, a4);
loc_00250B72:
    a4 = (a1 + 128) & (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 128 + 8)));
loc_00250B96:
    if (0 >= ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1136) + 12)))) goto loc_00250BC2;
    a1 = (*(unsigned __int64 *)(gs_base + (0 + 32))) * (0);
    a1 = (a1) + (16);
    a1 = (a1) + (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1136));
    result = (*(unsigned __int64 *)(a1)) & (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 128 + 8)));
    if (result == a4) goto loc_00250C95;
loc_00250BBE:
    a2 = (unsigned int)((0) + 1);
    goto loc_00250B96;
loc_00250BC2:
    if (result < a4) goto loc_00250CC5;
    a4 = 0;
    v_stack_m48 = 0;
    result = KeBugCheckEx(354, *(unsigned __int64 *)(gs_base + (0 + 392)), a1 + 128, a4);
loc_00250BE9:
    *(unsigned __int64 *)(354) = *(unsigned __int64 *)(gs_base + (0 + 392));
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 8) = 354;
    if (((unsigned __int8)(*(unsigned __int8 *)(result + 16))) != 1) goto loc_00250C54;
    result = KiTryUnwaitThread(2, result, *(unsigned __int16 *)(result + 18), v_stack_p18);
    if ((unsigned __int8)(result) == 0) goto loc_00250B19;
    goto loc_00250B41;
loc_00250C1E:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(v_cr8), 2, *(unsigned __int16 *)(result + 18), v_stack_p18);
    goto loc_00250AF3;
loc_00250C30:
    if (*(unsigned __int64 *)(2 + 11528) == 0) goto loc_00250B57;
    a1 = (*(unsigned __int64 *)(2 + 11528)) + (-216);
    result = KeAbPreWakeupThread(a1, a1 + 128, *(unsigned __int16 *)(result + 18), v_stack_p18);
    goto loc_00250B57;
loc_00250C54:
    if (((unsigned __int8)(a1)) != 2) goto loc_00250E47;
    *(unsigned __int8 *)(result + 17) = 5;
    result = KiInsertQueueInternal(*(unsigned __int64 *)(result + 24), result, *(unsigned __int16 *)(result + 18), v_stack_p18);
    goto loc_00250B41;
loc_00250C72:
    v_rsi = (unsigned int)((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 128 + 8))) + 1);
    if (((*(unsigned int *)(v_rip + 14108210)) & ((unsigned int)(v_rsi))) == 0) goto loc_00250E20;
loc_00250C80:
loc_00250C82:
    if (sign_flag) goto loc_00250C72;
    if (condition_is_above_or_equal) goto loc_00250B0A;
    goto loc_00250C72;
loc_00250C95:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(result + 24) + 10)) == 0) goto loc_00250BBE;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a1))) & (1)) != 0) goto loc_00250BBE;
    *(unsigned __int8 *)(*(unsigned __int64 *)(result + 24) + 10) = 0;
    v_stack_m48 = 0;
    result = KiAbEntryFreeAndEnableInterrupts(*(unsigned __int64 *)(result + 24), *(unsigned __int64 *)(gs_base + (0 + 392)), a1 + 128, 1);
    goto loc_00250CDF;
loc_00250CC5:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) != 0) goto loc_00250E65;
loc_00250CDE:
loc_00250CDF:
    if ((*(unsigned int *)(v_rip + 14107434)) != 0) {
        a2 = 0;
        a4 = 0x746C6644ULL;
        a1 = a1 - 48;
        a3 = a2 + 1;
        result = ObpPushStackInfo(a1, a2, a3, a4);
    }
    result = (-1) - (1);
    if (condition_is_less_or_equal) goto loc_00250D39;
loc_00250D12:
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, a4);
    v_rsp = (v_rsp) + (48);
    return result;
loc_00250D39:
    if (*(unsigned __int64 *)(v_stack_p20 + 8) != 0) goto loc_00250D5D;
    if (!sign_flag) goto loc_00250D9F;
    a2 = 0;
    v_stack_p20 = result;
    result = KeBugCheckEx(a2 + 24, a2, a1, 2);
loc_00250D5D:
    v_stack_p20 = a2 + 24;
    result = (v_stack_p20) >> (8);
    a2 = ((unsigned __int8)(result)) ^ (*(unsigned __int8 *)(v_stack_p20 + 24));
    a2 = (a2) ^ (*(unsigned __int8 *)(v_rip + 14115006));
    result = KeBugCheckEx(1 + 23, *(unsigned __int64 *)(v_rip - 2428271 + a2 * 8 + 16545792), a1, 1);
loc_00250D9F:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 486)) != 0) goto loc_00250EA9;
    result = KeAreInterruptsEnabled(1 + 23, *(unsigned __int64 *)(v_rip - 2428271 + a2 * 8 + 16545792), a1, 1);
    if ((unsigned __int8)(result) == 0) goto loc_00250EA9;
    if (((unsigned __int8)(v_r13 + 2)) >= 1) goto loc_00250EA9;
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_stack_p20 + 26))) & (64)) != 0) goto loc_00250DF7;
loc_00250DD7:
    result = *(unsigned __int8 *)(v_stack_p20 + 26);
    if ((*(unsigned int *)(v_rip + 14107186)) != 0) {
        a1 = v_stack_p20;
        result = ObpDeregisterObject(a1, *(unsigned __int64 *)(v_rip - 2428271 + a2 * 8 + 16545792), a1, 1);
    }
    a2 = 0;
    result = ObpRemoveObjectRoutine(v_stack_p20, a2, a1, 1);
    goto loc_00250D12;
loc_00250DF7:
    result = (unsigned int)((result) & (127));
    a1 = (v_stack_p20) - (*(unsigned __int8 *)(result + v_rip - 2428417 * 1 + 15794048));
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 24)) == 0) goto loc_00250DD7;
    result = ObpHandleRevocationBlockRemoveObject(*(unsigned __int64 *)(a1), a2, a1, 1);
    goto loc_00250DD7;
loc_00250E20:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14113938)))) & (64)) == 0) goto loc_00250C80;
    result = KiCheckVpBackingLongSpinWaitHypercall(*(unsigned __int64 *)(a1), a2, a1, 1);
    if ((unsigned __int8)(result) == 0) goto loc_00250C80;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rsi)), a2, a1, 1);
    goto loc_00250C82;
loc_00250E47:
    if (((unsigned __int8)((unsigned int)((unsigned int)(v_rsi)))) == 4) goto loc_00250E8D;
    a4 = 0;
    result = KiTryUnwaitThread(2, result, 256, a4);
    goto loc_00250B19;
loc_00250E65:
loc_00250E6C:
    if (condition_is_not_equal) goto loc_00250E6C;
    if (condition_is_above_or_equal) goto loc_00250CDE;
    result = KiRemoveSystemWorkPriorityKick(2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(256)))), 256, a4);
    goto loc_00250CDE;
loc_00250E8D:
    *(unsigned __int8 *)(result + 17) = 5;
    *(unsigned int *)(v_stack_p20 + 4) = 0;
    result = KeInsertQueueDpc(*(unsigned __int64 *)(result + 24), v_stack_p20, result, a4);
    goto loc_00250B19;
loc_00250EA9:
    *(unsigned __int64 *)(v_stack_p20 + 8) = *(unsigned __int64 *)(v_rip + 13363081);
    if (condition_is_equal) goto loc_00250EDE;
loc_00250EC9:
    *(unsigned __int64 *)(v_stack_p20 + 8) = *(unsigned __int64 *)(v_rip + 13363081);
    if ((*(unsigned __int64 *)(v_rip + 13363081)) != (*(unsigned __int64 *)(v_rip + 13363081))) goto loc_00250EC9;
loc_00250EDE:
    if (*(unsigned __int64 *)(v_rip + 13363081) != 0) goto loc_00250D12;
    result = KeGetEffectiveIrql(*(unsigned __int64 *)(v_rip + 13363081), v_stack_p20, result, a4);
    if (((unsigned __int8)(result)) > 2) goto loc_00250F03;
    a2 = 0;
    result = ExQueueWorkItem(v_rip + 13362983, a2, result, a4);
    goto loc_00250D12;
loc_00250F03:
    a3 = 0;
    a2 = 0;
    result = KeInsertQueueDpc(v_rip + 13362899, a2, a3, a4);
    goto loc_00250D12;
}
```

## 5. (Beta) C Style

```c
int64_t IopReleaseFileObjectLock(void *Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r13;
    int64_t local_rsi;
    int64_t local_rsp;
    uint8_t v_stack_m48;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;

    v_stack_p20 = local_rbx;
    local_rsp = (local_rsp) - (48);
    local_r13 = 0;
    v_stack_p18 = 0;
    if ((*(uint32_t *)(arg1 + 0x70)) == 0) goto loc_00250B72;
    if ((*(uint32_t *)(v_rip + 0xD76233)) != 0) goto loc_00250C1E;
loc_00250AF3:
    if ((*(uint32_t *)(v_rip + 0xD76233)) < 0) goto loc_00250C72;
loc_00250B0A:
    *(uint32_t *)(arg1 + 0x80 + 0x4) = 1;
loc_00250B19:
    if ((*(uint64_t *)(arg1 + 0x80 + 0x8)) == (Arg1 + 128 + 8)) goto loc_00250B47;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x80 + 0x8)) + 0x8)) != (*(uint64_t *)(arg1 + 0x80 + 0x8))) goto loc_00250B3A;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x80 + 0x8) + 0x8))) == (*(uint64_t *)(arg1 + 0x80 + 0x8))) goto loc_00250BE9;
loc_00250B3A:
loc_00250B41:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x80 + 0x8) + 0x8))) != (*(uint64_t *)(arg1 + 0x80 + 0x8))) goto loc_00250B19;
loc_00250B47:
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xC3)) != 0) goto loc_00250C30;
loc_00250B57:
    Arg4 = 0;
    v_stack_m48 = (uint8_t)(v_cr8);
    Arg2 = 0;
    result = KiExitDispatcher(*(uint64_t *)(gs_base + (0 + 0x20)), Arg2, Arg4 + 1, Arg4);
loc_00250B72:
    Arg4 = (Arg1 + 128) & (*(uint64_t *)(*(uint64_t *)(arg1 + 0x80 + 0x8)));
loc_00250B96:
    if (0 >= ((uint32_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x470) + 0xC)))) goto loc_00250BC2;
    Arg1 = (*(uint64_t *)(gs_base + (0 + 0x20))) * (0);
    Arg1 = (Arg1) + (16);
    Arg1 = (Arg1) + (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x470));
    result = (*(uint64_t *)(arg1)) & (*(uint64_t *)(*(uint64_t *)(arg1 + 0x80 + 0x8)));
    if (result == Arg4) goto loc_00250C95;
loc_00250BBE:
    Arg2 = (uint32_t)((0) + 1);
    goto loc_00250B96;
loc_00250BC2:
    if (result < Arg4) goto loc_00250CC5;
    Arg4 = 0;
    v_stack_m48 = 0;
    result = KeBugCheckEx(354, *(uint64_t *)(gs_base + (0 + 0x188)), Arg1 + 128, Arg4);
loc_00250BE9:
    *(uint64_t *)(354) = *(uint64_t *)(gs_base + (0 + 0x188));
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x8) = 354;
    if (((uint8_t)(*(uint8_t *)(result + 0x10))) != 1) goto loc_00250C54;
    result = KiTryUnwaitThread(2, result, *(uint16_t *)(result + 0x12), v_stack_p18);
    if ((uint8_t)(result) == 0) goto loc_00250B19;
    goto loc_00250B41;
loc_00250C1E:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(v_cr8), 2, *(uint16_t *)(result + 0x12), v_stack_p18);
    goto loc_00250AF3;
loc_00250C30:
    if (*(uint64_t *)(2 + 0x2D08) == 0) goto loc_00250B57;
    Arg1 = (*(uint64_t *)(2 + 0x2D08)) + (-216);
    result = KeAbPreWakeupThread(Arg1, Arg1 + 128, *(uint16_t *)(result + 0x12), v_stack_p18);
    goto loc_00250B57;
loc_00250C54:
    if (((uint8_t)(Arg1)) != 2) goto loc_00250E47;
    *(uint8_t *)(result + 0x11) = 5;
    result = KiInsertQueueInternal(*(uint64_t *)(result + 0x18), result, *(uint16_t *)(result + 0x12), v_stack_p18);
    goto loc_00250B41;
loc_00250C72:
    local_rsi = (uint32_t)((*(uint64_t *)(*(uint64_t *)(arg1 + 0x80 + 0x8))) + 1);
    if (((*(uint32_t *)(v_rip + 0xD74632)) & ((uint32_t)(local_rsi))) == 0) goto loc_00250E20;
loc_00250C80:
loc_00250C82:
    if (sign_flag) goto loc_00250C72;
    if (condition_is_above_or_equal) goto loc_00250B0A;
    goto loc_00250C72;
loc_00250C95:
    if ((*(uint8_t *)(*(uint64_t *)(result + 0x18) + 0xA)) == 0) goto loc_00250BBE;
    if ((((uint8_t)(*(uint64_t *)(arg1))) & (1)) != 0) goto loc_00250BBE;
    *(uint8_t *)(*(uint64_t *)(result + 0x18) + 0xA) = 0;
    v_stack_m48 = 0;
    result = KiAbEntryFreeAndEnableInterrupts(*(uint64_t *)(result + 0x18), *(uint64_t *)(gs_base + (0 + 0x188)), Arg1 + 128, 1);
    goto loc_00250CDF;
loc_00250CC5:
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) != 0) goto loc_00250E65;
loc_00250CDE:
loc_00250CDF:
    if ((*(uint32_t *)(v_rip + 0xD7432A)) != 0) {
        Arg2 = 0;
        Arg4 = 0x746C6644ULL;
        Arg1 = Arg1 - 48;
        Arg3 = Arg2 + 1;
        result = ObpPushStackInfo(Arg1, Arg2, Arg3, Arg4);
    }
    result = (-1) - (1);
    if (condition_is_less_or_equal) goto loc_00250D39;
loc_00250D12:
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (48);
    return result;
loc_00250D39:
    if (*(uint64_t *)(v_stack_p20 + 0x8) != 0) goto loc_00250D5D;
    if (!sign_flag) goto loc_00250D9F;
    Arg2 = 0;
    v_stack_p20 = result;
    result = KeBugCheckEx(Arg2 + 24, Arg2, Arg1, 2);
loc_00250D5D:
    v_stack_p20 = Arg2 + 24;
    result = (v_stack_p20) >> (8);
    Arg2 = ((uint8_t)(result)) ^ (*(uint8_t *)(v_stack_p20 + 0x18));
    Arg2 = (Arg2) ^ (*(uint8_t *)(v_rip + 0xD760BE));
    result = KeBugCheckEx(1 + 23, *(uint64_t *)(v_rip - 0x250D6F + Arg2 * 8 + 0xFC7800), Arg1, 1);
loc_00250D9F:
    if ((*(uint16_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x1E6)) != 0) goto loc_00250EA9;
    result = KeAreInterruptsEnabled(1 + 23, *(uint64_t *)(v_rip - 0x250D6F + Arg2 * 8 + 0xFC7800), Arg1, 1);
    if ((uint8_t)(result) == 0) goto loc_00250EA9;
    if (((uint8_t)(local_r13 + 2)) >= 1) goto loc_00250EA9;
    if ((((uint8_t)(*(uint8_t *)(v_stack_p20 + 0x1A))) & (64)) != 0) goto loc_00250DF7;
loc_00250DD7:
    result = *(uint8_t *)(v_stack_p20 + 0x1A);
    if ((*(uint32_t *)(v_rip + 0xD74232)) != 0) {
        Arg1 = v_stack_p20;
        result = ObpDeregisterObject(Arg1, *(uint64_t *)(v_rip - 0x250D6F + Arg2 * 8 + 0xFC7800), Arg1, 1);
    }
    Arg2 = 0;
    result = ObpRemoveObjectRoutine(v_stack_p20, Arg2, Arg1, 1);
    goto loc_00250D12;
loc_00250DF7:
    result = (uint32_t)((result) & (127));
    Arg1 = (v_stack_p20) - (*(uint8_t *)(result + v_rip - 0x250E01 * 1 + 0xF0FF80));
    if ((*(uint8_t *)(*(uint64_t *)(arg1) + 0x18)) == 0) goto loc_00250DD7;
    result = ObpHandleRevocationBlockRemoveObject(*(uint64_t *)(arg1), Arg2, Arg1, 1);
    goto loc_00250DD7;
loc_00250E20:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD75C92)))) & (64)) == 0) goto loc_00250C80;
    result = KiCheckVpBackingLongSpinWaitHypercall(*(uint64_t *)(arg1), Arg2, Arg1, 1);
    if ((uint8_t)(result) == 0) goto loc_00250C80;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rsi)), Arg2, Arg1, 1);
    goto loc_00250C82;
loc_00250E47:
    if (((uint8_t)((uint32_t)((uint32_t)(local_rsi)))) == 4) goto loc_00250E8D;
    Arg4 = 0;
    result = KiTryUnwaitThread(2, result, 256, Arg4);
    goto loc_00250B19;
loc_00250E65:
loc_00250E6C:
    if (condition_is_not_equal) goto loc_00250E6C;
    if (condition_is_above_or_equal) goto loc_00250CDE;
    result = KiRemoveSystemWorkPriorityKick(2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(256)))), 256, Arg4);
    goto loc_00250CDE;
loc_00250E8D:
    *(uint8_t *)(result + 0x11) = 5;
    *(uint32_t *)(v_stack_p20 + 0x4) = 0;
    result = KeInsertQueueDpc(*(uint64_t *)(result + 0x18), v_stack_p20, result, Arg4);
    goto loc_00250B19;
loc_00250EA9:
    *(uint64_t *)(v_stack_p20 + 0x8) = *(uint64_t *)(v_rip + 0xCBE789);
    if (condition_is_equal) goto loc_00250EDE;
loc_00250EC9:
    *(uint64_t *)(v_stack_p20 + 0x8) = *(uint64_t *)(v_rip + 0xCBE789);
    if ((*(uint64_t *)(v_rip + 0xCBE789)) != (*(uint64_t *)(v_rip + 0xCBE789))) goto loc_00250EC9;
loc_00250EDE:
    if (*(uint64_t *)(v_rip + 0xCBE789) != 0) goto loc_00250D12;
    result = KeGetEffectiveIrql(*(uint64_t *)(v_rip + 0xCBE789), v_stack_p20, result, Arg4);
    if (((uint8_t)(result)) > 2) goto loc_00250F03;
    Arg2 = 0;
    result = ExQueueWorkItem(v_rip + 13362983, Arg2, result, Arg4);
    goto loc_00250D12;
loc_00250F03:
    Arg3 = 0;
    Arg2 = 0;
    result = KeInsertQueueDpc(v_rip + 13362899, Arg2, Arg3, Arg4);
    goto loc_00250D12;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `- 0x30` | `64` | `R` |
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x0` | `32` | `R/W` |
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x0` | `64` | `R/W` |
| `Arg1` | `+ 0x4` | `32` | `R/W` |
| `Arg1` | `+ 0x4` | `32` | `W` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `W` |
| `Arg1` | `+ 0x18` | `8` | `R` |
| `Arg1` | `+ 0x1A` | `8` | `R` |
| `Arg1` | `+ 0x70` | `32` | `R` |
| `Arg1` | `+ 0x74` | `32` | `R/W` |
| `Arg1` | `+ 0x80` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00250A90&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
