# MiInPagePageTable

- RVA: `0x003EF8DC`–`0x003EFFCB` (길이 `1,775` bytes)
- VA: `0x00000001403EF8DC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00096B84`
- 디코드: `412`개 명령, `1,775/1,775` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **32**; 고유 호출 대상: **25**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x003EF933` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x003EF942` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x003EF991` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x003EF9C5` → [MiCheckVirtualAddress](../32/MiCheckVirtualAddress_function_0032E4F0.md) (function, `0x0032E4F0`)
- `0x003EFA5B` → [MiMakeDemandZeroPte](../33/MiMakeDemandZeroPte_function_00337A00.md) (function, `0x00337A00`)
- `0x003EFA9E` → [ExReleaseSpinLockSharedFromDpcLevel](../24/ExReleaseSpinLockSharedFromDpcLevel_function_0024A590.md) (function, `0x0024A590`)
- `0x003EFAD5` → [MiIncreaseUsedPtes](../24/MiIncreaseUsedPtes_function_00243630.md) (function, `0x00243630`)
- `0x003EFB04` → [ExReleaseSpinLockSharedFromDpcLevel](../24/ExReleaseSpinLockSharedFromDpcLevel_function_0024A590.md) (function, `0x0024A590`)
- `0x003EFB82` → [MiNodeFromFaultPacket](../3F/MiNodeFromFaultPacket_function_003F0070.md) (function, `0x003F0070`)
- `0x003EFB89` → [MiGetClosestImplicitNode](../3F/MiGetClosestImplicitNode_function_003F00AC.md) (function, `0x003F00AC`)
- `0x003EFBD8` → [MiDispatchFault](../32/MiDispatchFault_function_00320520.md) (function, `0x00320520`)
- `0x003EFBF2` → [MiPropagateFaultPacketFields](MiPropagateFaultPacketFields_function_003EFFE0.md) (function, `0x003EFFE0`)
- `0x003EFC09` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x003EFC39` → [MiCheckFatalAccessViolation](../3F/MiCheckFatalAccessViolation_function_003F00F0.md) (function, `0x003F00F0`)
- `0x003EFC73` → [MiGetLeafVa](../27/MiGetLeafVa_function_0027C0A0.md) (function, `0x0027C0A0`)
- `0x003EFC96` → [MiUnlockVadTree](../29/MiUnlockVadTree_function_00297020.md) (function, `0x00297020`)
- `0x003EFD89` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x003EFD92` → [MiIsVadLarge](../3F/MiIsVadLarge_function_003F0190.md) (function, `0x003F0190`)
- `0x003EFDB6` → [MiUnlockVadTree](../29/MiUnlockVadTree_function_00297020.md) (function, `0x00297020`)
- `0x003EFDD0` → [MiLeapPrefetch](../4C/MiLeapPrefetch_function_004CAED0.md) (function, `0x004CAED0`)
- `0x003EFE14` → [MiIssueHardFault](../38/MiIssueHardFault_function_00380074.md) (function, `0x00380074`)
- `0x003EFE5A` → [MiVadPureReserve](../2C/MiVadPureReserve_function_002C34C0.md) (function, `0x002C34C0`)
- `0x003EFE6D` → [MiGetLargeVadMappingIndex](../4F/MiGetLargeVadMappingIndex_function_004F94D0.md) (function, `0x004F94D0`)
- `0x003EFE83` → [MiMakeDemandZeroPte](../33/MiMakeDemandZeroPte_function_00337A00.md) (function, `0x00337A00`)
- `0x003EFE92` → [MiUnlockVadTree](../29/MiUnlockVadTree_function_00297020.md) (function, `0x00297020`)
- `0x003EFEAD` → [MiInsertLargeVadMapping](../3F/MiInsertLargeVadMapping_function_003F0498.md) (function, `0x003F0498`)
- `0x003EFEFE` → [MiIncreaseUsedPtes](../24/MiIncreaseUsedPtes_function_00243630.md) (function, `0x00243630`)
- `0x003EFF09` → [MiLargePageFault](../3F/MiLargePageFault_function_003F01C4.md) (function, `0x003F01C4`)
- `0x003EFF26` → [MiUnlockVadTree](../29/MiUnlockVadTree_function_00297020.md) (function, `0x00297020`)
- `0x003EFF69` → [MiReleaseFaultState](../27/MiReleaseFaultState_function_0027D290.md) (function, `0x0027D290`)
- `0x003EFF79` → [MmAccessFault](../27/MmAccessFault_function_0027EE80.md) (function, `0x0027EE80`)
- `0x003EFF87` → [MiLockWorkingSetShared](../27/MiLockWorkingSetShared_function_0027CBF0.md) (function, `0x0027CBF0`)

### Direct callers
- [sub_002759BE](../27/Unknown_function_002759BE.md) at `0x00275BBB`

### Static image references
- `0x003EF8FB` → RVA `0x00E0A740` (`.data`; read)
- `0x003EFF52` → RVA `0x00010880` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **7**
  - `0x003EFC7B` → [sub_006EAE58](../6E/Unknown_function_006EAE58.md) (`tail-transfer`)
  - `0x003EFC8A` → [sub_006EAE58 + 0xB](../6E/Unknown_function_006EAE58.md) (`tail-transfer`)
  - `0x003EFCC4` → [sub_006EAE58 + 0x14](../6E/Unknown_function_006EAE58.md) (`tail-transfer`)
  - `0x003EFCCE` → [sub_006EAE58 + 0x14](../6E/Unknown_function_006EAE58.md) (`tail-transfer`)
  - `0x003EFCD4` → [sub_006EAE58 + 0x19](../6E/Unknown_function_006EAE58.md) (`tail-transfer`)
  - `0x003EFF38` → [sub_006EAE58 + 0x3D](../6E/Unknown_function_006EAE58.md) (`tail-transfer`)
  - `0x003EFF45` → [sub_006EAE58 + 0x3D](../6E/Unknown_function_006EAE58.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003EF8DC  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
003EF8E1  55                              push rbp
003EF8E2  56                              push rsi
003EF8E3  57                              push rdi
003EF8E4  41 54                           push r12
003EF8E6  41 55                           push r13
003EF8E8  41 56                           push r14
003EF8EA  41 57                           push r15
003EF8EC  48 8D AC 24 40 FF FF FF         lea rbp, [rsp - 0xc0]
003EF8F4  48 81 EC C0 01 00 00            sub rsp, 0x1c0
003EF8FB  48 8B 05 3E AE A1 00            mov rax, qword ptr [rip + 0xa1ae3e]
003EF902  48 33 C4                        xor rax, rsp
003EF905  48 89 85 B0 00 00 00            mov qword ptr [rbp + 0xb0], rax
003EF90C  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
003EF912  4C 8B F9                        mov r15, rcx
003EF915  83 64 24 38 00                  and dword ptr [rsp + 0x38], 0
003EF91A  48 8D 4D 10                     lea rcx, [rbp + 0x10]
003EF91E  48 83 64 24 40 00               and qword ptr [rsp + 0x40], 0
003EF924  41 B8 98 00 00 00               mov r8d, 0x98
003EF92A  48 63 DA                        movsxd rbx, edx
003EF92D  33 D2                           xor edx, edx
003EF92F  89 5C 24 48                     mov dword ptr [rsp + 0x48], ebx
003EF933  E8 08 73 2D 00                  call 0x1406c6c40
003EF938  33 D2                           xor edx, edx
003EF93A  48 8D 4D 90                     lea rcx, [rbp - 0x70]
003EF93E  44 8D 42 78                     lea r8d, [rdx + 0x78]
003EF942  E8 F9 72 2D 00                  call 0x1406c6c40
003EF947  0F 57 C0                        xorps xmm0, xmm0
003EF94A  0F 11 44 24 78                  movups xmmword ptr [rsp + 0x78], xmm0
003EF94F  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
003EF958  49 8B 7F 10                     mov rdi, qword ptr [r15 + 0x10]
003EF95C  4C 8B B0 B8 00 00 00            mov r14, qword ptr [rax + 0xb8]
003EF963  4C 89 74 24 50                  mov qword ptr [rsp + 0x50], r14
003EF968  49 8D 86 00 04 00 00            lea rax, [r14 + 0x400]
003EF96F  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
003EF974  40 F6 C7 01                     test dil, 1
003EF978  0F 85 75 03 00 00               jne 0x1403efcf3
003EF97E  33 FF                           xor edi, edi
003EF980  49 8B 74 DF 18                  mov rsi, qword ptr [r15 + rbx*8 + 0x18]
003EF985  49 8D 47 38                     lea rax, [r15 + 0x38]
003EF989  48 8B CE                        mov rcx, rsi
003EF98C  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
003EF991  E8 0A 2F E9 FF                  call 0x1402828a0
003EF996  4C 8B E6                        mov r12, rsi
003EF999  49 BD 00 00 00 00 80 F6 FF FF   movabs r13, 0xfffff68000000000
003EF9A3  49 C1 E4 19                     shl r12, 0x19
003EF9A7  48 8B D8                        mov rbx, rax
003EF9AA  49 8B C5                        mov rax, r13
003EF9AD  49 8B 0F                        mov rcx, qword ptr [r15]
003EF9B0  4C 8D 44 24 30                  lea r8, [rsp + 0x30]
003EF9B5  48 C1 E0 19                     shl rax, 0x19
003EF9B9  48 8D 54 24 38                  lea rdx, [rsp + 0x38]
003EF9BE  4C 2B E0                        sub r12, rax
003EF9C1  49 C1 FC 10                     sar r12, 0x10
003EF9C5  E8 26 EB F3 FF                  call 0x14032e4f0
003EF9CA  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
003EF9CF  49 BA F8 FF FF FF 7F 00 00 00   movabs r10, 0x7ffffffff8
003EF9D9  48 85 DB                        test rbx, rbx
003EF9DC  0F 85 FA 00 00 00               jne 0x1403efadc
003EF9E2  49 8B 0F                        mov rcx, qword ptr [r15]
003EF9E5  48 B8 00 00 00 00 00 80 FF FF   movabs rax, 0xffff800000000000
003EF9EF  48 3B C8                        cmp rcx, rax
003EF9F2  0F 83 26 03 00 00               jae 0x1403efd1e
003EF9F8  44 8B 6C 24 38                  mov r13d, dword ptr [rsp + 0x38]
003EF9FD  41 83 FD 18                     cmp r13d, 0x18
003EFA01  0F 84 23 02 00 00               je 0x1403efc2a
003EFA07  4C 8B 74 24 30                  mov r14, qword ptr [rsp + 0x30]
003EFA0C  4D 85 F6                        test r14, r14
003EFA0F  74 0E                           je 0x1403efa1f
003EFA11  41 F7 46 30 00 00 20 00         test dword ptr [r14 + 0x30], 0x200000
003EFA19  0F 85 7E 02 00 00               jne 0x1403efc9d
003EFA1F  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
003EFA24  48 8B 89 70 02 00 00            mov rcx, qword ptr [rcx + 0x270]
003EFA2B  48 85 C9                        test rcx, rcx
003EFA2E  0F 85 01 05 00 00               jne 0x1403eff35
003EFA34  4D 85 F6                        test r14, r14
003EFA37  74 1D                           je 0x1403efa56
003EFA39  48 85 FF                        test rdi, rdi
003EFA3C  0F 85 4D 03 00 00               jne 0x1403efd8f
003EFA42  4D 85 F6                        test r14, r14
003EFA45  74 0F                           je 0x1403efa56
003EFA47  41 8B 46 30                     mov eax, dword ptr [r14 + 0x30]
003EFA4B  83 E0 70                        and eax, 0x70
003EFA4E  3C 50                           cmp al, 0x50
003EFA50  0F 84 01 04 00 00               je 0x1403efe57
003EFA56  B9 04 00 00 00                  mov ecx, 4
003EFA5B  E8 A0 7F F4 FF                  call 0x140337a00
003EFA60  48 B9 00 D0 BE 7D FB F6 FF FF   movabs rcx, 0xfffff6fb7dbed000
003EFA6A  48 8B C9                        mov rcx, rcx
003EFA6D  48 3B F1                        cmp rsi, rcx
003EFA70  0F 83 68 03 00 00               jae 0x1403efdde
003EFA76  33 DB                           xor ebx, ebx
003EFA78  48 89 06                        mov qword ptr [rsi], rax
003EFA7B  4D 85 F6                        test r14, r14
003EFA7E  74 28                           je 0x1403efaa8
003EFA80  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
003EFA89  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
003EFA90  48 8B 89 10 04 00 00            mov rcx, qword ptr [rcx + 0x410]
003EFA97  48 81 C1 EC 03 00 00            add rcx, 0x3ec
003EFA9E  E8 ED AA E5 FF                  call 0x14024a590
003EFAA3  4C 8B 74 24 30                  mov r14, qword ptr [rsp + 0x30]
003EFAA8  49 BD 00 00 00 00 80 F6 FF FF   movabs r13, 0xfffff68000000000
003EFAB2  85 DB                           test ebx, ebx
003EFAB4  75 58                           jne 0x1403efb0e
003EFAB6  48 C1 EE 09                     shr rsi, 9
003EFABA  48 BA F8 FF FF FF 7F 00 00 00   movabs rdx, 0x7ffffffff8
003EFAC4  48 23 D6                        and rdx, rsi
003EFAC7  49 8B C5                        mov rax, r13
003EFACA  48 03 D0                        add rdx, rax
003EFACD  44 8D 4B 02                     lea r9d, [rbx + 2]
003EFAD1  44 8D 43 01                     lea r8d, [rbx + 1]
003EFAD5  E8 56 3B E5 FF                  call 0x140243630
003EFADA  EB 32                           jmp 0x1403efb0e
003EFADC  4C 8B 74 24 30                  mov r14, qword ptr [rsp + 0x30]
003EFAE1  4D 85 F6                        test r14, r14
003EFAE4  74 32                           je 0x1403efb18
003EFAE6  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
003EFAEF  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
003EFAF6  48 8B 89 10 04 00 00            mov rcx, qword ptr [rcx + 0x410]
003EFAFD  48 81 C1 EC 03 00 00            add rcx, 0x3ec
003EFB04  E8 87 AA E5 FF                  call 0x14024a590
003EFB09  4C 8B 74 24 30                  mov r14, qword ptr [rsp + 0x30]
003EFB0E  49 BA F8 FF FF FF 7F 00 00 00   movabs r10, 0x7ffffffff8
003EFB18  41 0F 10 07                     movups xmm0, xmmword ptr [r15]
003EFB1C  48 8D 4D 10                     lea rcx, [rbp + 0x10]
003EFB20  BA 80 00 00 00                  mov edx, 0x80
003EFB25  41 0F 10 4F 10                  movups xmm1, xmmword ptr [r15 + 0x10]
003EFB2A  0F 11 01                        movups xmmword ptr [rcx], xmm0
003EFB2D  49 8B 44 17 10                  mov rax, qword ptr [r15 + rdx + 0x10]
003EFB32  41 0F 10 47 20                  movups xmm0, xmmword ptr [r15 + 0x20]
003EFB37  0F 11 49 10                     movups xmmword ptr [rcx + 0x10], xmm1
003EFB3B  41 0F 10 4F 30                  movups xmm1, xmmword ptr [r15 + 0x30]
003EFB40  0F 11 41 20                     movups xmmword ptr [rcx + 0x20], xmm0
003EFB44  41 0F 10 47 40                  movups xmm0, xmmword ptr [r15 + 0x40]
003EFB49  0F 11 49 30                     movups xmmword ptr [rcx + 0x30], xmm1
003EFB4D  41 0F 10 4F 50                  movups xmm1, xmmword ptr [r15 + 0x50]
003EFB52  0F 11 41 40                     movups xmmword ptr [rcx + 0x40], xmm0
003EFB56  41 0F 10 47 60                  movups xmm0, xmmword ptr [r15 + 0x60]
003EFB5B  0F 11 49 50                     movups xmmword ptr [rcx + 0x50], xmm1
003EFB5F  41 0F 10 0C 17                  movups xmm1, xmmword ptr [r15 + rdx]
003EFB64  0F 11 41 60                     movups xmmword ptr [rcx + 0x60], xmm0
003EFB68  41 0F 10 47 70                  movups xmm0, xmmword ptr [r15 + 0x70]
003EFB6D  0F 11 44 11 F0                  movups xmmword ptr [rcx + rdx - 0x10], xmm0
003EFB72  0F 11 0C 11                     movups xmmword ptr [rcx + rdx], xmm1
003EFB76  48 89 44 11 10                  mov qword ptr [rcx + rdx + 0x10], rax
003EFB7B  49 8B CF                        mov rcx, r15
003EFB7E  83 65 60 00                     and dword ptr [rbp + 0x60], 0
003EFB82  E8 E9 04 00 00                  call 0x1403f0070
003EFB87  8B C8                           mov ecx, eax
003EFB89  E8 1E 05 00 00                  call 0x1403f00ac
003EFB8E  49 8B 4F 10                     mov rcx, qword ptr [r15 + 0x10]
003EFB92  48 8B D1                        mov rdx, rcx
003EFB95  48 83 E2 FE                     and rdx, 0xfffffffffffffffe
003EFB99  F6 C1 01                        test cl, 1
003EFB9C  0F 85 37 01 00 00               jne 0x1403efcd9
003EFBA2  48 C7 45 18 02 00 00 00         mov qword ptr [rbp + 0x18], 2
003EFBAA  33 C9                           xor ecx, ecx
003EFBAC  4C 89 65 10                     mov qword ptr [rbp + 0x10], r12
003EFBB0  4C 89 75 68                     mov qword ptr [rbp + 0x68], r14
003EFBB4  49 C1 EC 09                     shr r12, 9
003EFBB8  4D 23 E2                        and r12, r10
003EFBBB  49 8B C5                        mov rax, r13
003EFBBE  4C 03 E0                        add r12, rax
003EFBC1  4C 89 64 CD 28                  mov qword ptr [rbp + rcx*8 + 0x28], r12
003EFBC6  48 FF C1                        inc rcx
003EFBC9  48 83 F9 04                     cmp rcx, 4
003EFBCD  7C E5                           jl 0x1403efbb4
003EFBCF  48 8D 54 24 40                  lea rdx, [rsp + 0x40]
003EFBD4  48 8D 4D 10                     lea rcx, [rbp + 0x10]
003EFBD8  E8 43 09 F3 FF                  call 0x140320520
003EFBDD  44 8B C8                        mov r9d, eax
003EFBE0  3D 33 33 03 C0                  cmp eax, 0xc0033333
003EFBE5  0F 84 13 02 00 00               je 0x1403efdfe
003EFBEB  48 8D 55 10                     lea rdx, [rbp + 0x10]
003EFBEF  49 8B CF                        mov rcx, r15
003EFBF2  E8 E9 03 00 00                  call 0x1403effe0
003EFBF7  45 85 C9                        test r9d, r9d
003EFBFA  79 60                           jns 0x1403efc5c
003EFBFC  41 8B C1                        mov eax, r9d
003EFBFF  48 8B 8D B0 00 00 00            mov rcx, qword ptr [rbp + 0xb0]
003EFC06  48 33 CC                        xor rcx, rsp
003EFC09  E8 32 CA 2B 00                  call 0x1406ac640
003EFC0E  48 8B 9C 24 10 02 00 00         mov rbx, qword ptr [rsp + 0x210]
003EFC16  48 81 C4 C0 01 00 00            add rsp, 0x1c0
003EFC1D  41 5F                           pop r15
003EFC1F  41 5E                           pop r14
003EFC21  41 5D                           pop r13
003EFC23  41 5C                           pop r12
003EFC25  5F                              pop rdi
003EFC26  5E                              pop rsi
003EFC27  5D                              pop rbp
003EFC28  C3                              ret
003EFC29  CC                              int3
003EFC2A  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
003EFC2F  4D 8B CE                        mov r9, r14
003EFC32  4D 8B 47 08                     mov r8, qword ptr [r15 + 8]
003EFC36  48 8B D3                        mov rdx, rbx
003EFC39  E8 B2 04 00 00                  call 0x1403f00f0
003EFC3E  48 85 DB                        test rbx, rbx
003EFC41  75 4C                           jne 0x1403efc8f
003EFC43  4D 8B 0F                        mov r9, qword ptr [r15]
003EFC46  48 B8 FF FF FE FF FF 7F 00 00   movabs rax, 0x7ffffffeffff
003EFC50  4C 3B C8                        cmp r9, rax
003EFC53  76 10                           jbe 0x1403efc65
003EFC55  B8 05 00 00 C0                  mov eax, 0xc0000005
003EFC5A  EB A3                           jmp 0x1403efbff
003EFC5C  41 83 67 50 EF                  and dword ptr [r15 + 0x50], 0xffffffef
003EFC61  33 C0                           xor eax, eax
003EFC63  EB 9A                           jmp 0x1403efbff
003EFC65  48 85 DB                        test rbx, rbx
003EFC68  74 EB                           je 0x1403efc55
003EFC6A  48 85 FF                        test rdi, rdi
003EFC6D  74 E6                           je 0x1403efc55
003EFC6F  48 8D 4E 08                     lea rcx, [rsi + 8]
003EFC73  E8 28 C4 E8 FF                  call 0x14027c0a0
003EFC78  49 3B C1                        cmp rax, r9
003EFC7B  0F 83 D7 B1 2F 00               jae 0x1406eae58
003EFC81  48 FF 47 18                     inc qword ptr [rdi + 0x18]
003EFC85  48 83 67 20 00                  and qword ptr [rdi + 0x20], 0
003EFC8A  E9 D4 B1 2F 00                  jmp 0x1406eae63
003EFC8F  B2 11                           mov dl, 0x11
003EFC91  B9 01 00 00 00                  mov ecx, 1
003EFC96  E8 85 73 EA FF                  call 0x140297020
003EFC9B  EB A6                           jmp 0x1403efc43
003EFC9D  48 85 FF                        test rdi, rdi
003EFCA0  0F 84 79 FD FF FF               je 0x1403efa1f
003EFCA6  49 8B 5F 10                     mov rbx, qword ptr [r15 + 0x10]
003EFCAA  48 83 E3 FE                     and rbx, 0xfffffffffffffffe
003EFCAE  8B 4B 50                        mov ecx, dword ptr [rbx + 0x50]
003EFCB1  0F BA E1 12                     bt ecx, 0x12
003EFCB5  0F 82 64 FD FF FF               jb 0x1403efa1f
003EFCBB  41 8B C5                        mov eax, r13d
003EFCBE  C1 E8 03                        shr eax, 3
003EFCC1  83 F8 03                        cmp eax, 3
003EFCC4  0F 85 A2 B1 2F 00               jne 0x1406eae6c
003EFCCA  41 F6 C5 07                     test r13b, 7
003EFCCE  0F 84 98 B1 2F 00               je 0x1406eae6c
003EFCD4  E9 98 B1 2F 00                  jmp 0x1406eae71
003EFCD9  8A 0A                           mov cl, byte ptr [rdx]
003EFCDB  80 F9 01                        cmp cl, 1
003EFCDE  75 25                           jne 0x1403efd05
003EFCE0  80 F9 02                        cmp cl, 2
003EFCE3  0F 84 38 01 00 00               je 0x1403efe21
003EFCE9  48 83 65 20 00                  and qword ptr [rbp + 0x20], 0
003EFCEE  E9 AF FE FF FF                  jmp 0x1403efba2
003EFCF3  48 83 E7 FE                     and rdi, 0xfffffffffffffffe
003EFCF7  80 3F 01                        cmp byte ptr [rdi], 1
003EFCFA  0F 84 80 FC FF FF               je 0x1403ef980
003EFD00  E9 79 FC FF FF                  jmp 0x1403ef97e
003EFD05  80 F9 03                        cmp cl, 3
003EFD08  74 DF                           je 0x1403efce9
003EFD0A  80 F9 02                        cmp cl, 2
003EFD0D  0F 84 0E 01 00 00               je 0x1403efe21
003EFD13  80 F9 05                        cmp cl, 5
003EFD16  0F 85 86 FE FF FF               jne 0x1403efba2
003EFD1C  EB CB                           jmp 0x1403efce9
003EFD1E  48 85 FF                        test rdi, rdi
003EFD21  0F 85 04 02 00 00               jne 0x1403eff2b
003EFD27  49 8B C5                        mov rax, r13
003EFD2A  48 3B C8                        cmp rcx, rax
003EFD2D  0F 82 C5 FC FF FF               jb 0x1403ef9f8
003EFD33  48 B8 FF FF FF FF FF F6 FF FF   movabs rax, 0xfffff6ffffffffff
003EFD3D  48 3B C8                        cmp rcx, rax
003EFD40  0F 87 B2 FC FF FF               ja 0x1403ef9f8
003EFD46  49 8B 57 10                     mov rdx, qword ptr [r15 + 0x10]
003EFD4A  48 85 D2                        test rdx, rdx
003EFD4D  0F 84 A5 FC FF FF               je 0x1403ef9f8
003EFD53  48 8B C2                        mov rax, rdx
003EFD56  48 83 E0 FE                     and rax, 0xfffffffffffffffe
003EFD5A  F6 C2 01                        test dl, 1
003EFD5D  74 12                           je 0x1403efd71
003EFD5F  80 38 07                        cmp byte ptr [rax], 7
003EFD62  0F 84 90 FC FF FF               je 0x1403ef9f8
003EFD68  80 38 08                        cmp byte ptr [rax], 8
003EFD6B  0F 84 87 FC FF FF               je 0x1403ef9f8
003EFD71  4D 8B 47 08                     mov r8, qword ptr [r15 + 8]
003EFD75  48 8B D1                        mov rdx, rcx
003EFD78  B9 50 00 00 00                  mov ecx, 0x50
003EFD7D  48 C7 44 24 20 06 00 00 00      mov qword ptr [rsp + 0x20], 6
003EFD86  4C 8B CE                        mov r9, rsi
003EFD89  E8 D2 D8 10 00                  call 0x1404fd660
003EFD8E  CC                              int3
003EFD8F  49 8B CE                        mov rcx, r14
003EFD92  E8 F9 03 00 00                  call 0x1403f0190
003EFD97  85 C0                           test eax, eax
003EFD99  0F 84 A3 FC FF FF               je 0x1403efa42
003EFD9F  41 0F B6 5E 21                  movzx ebx, byte ptr [r14 + 0x21]
003EFDA4  B2 11                           mov dl, 0x11
003EFDA6  41 8B 46 1C                     mov eax, dword ptr [r14 + 0x1c]
003EFDAA  B9 01 00 00 00                  mov ecx, 1
003EFDAF  48 C1 E3 20                     shl rbx, 0x20
003EFDB3  48 0B D8                        or rbx, rax
003EFDB6  E8 65 72 EA FF                  call 0x140297020
003EFDBB  48 C1 E3 0C                     shl rbx, 0xc
003EFDBF  48 8B CF                        mov rcx, rdi
003EFDC2  48 81 CB FF 0F 00 00            or rbx, 0xfff
003EFDC9  48 8D 93 00 10 00 00            lea rdx, [rbx + 0x1000]
003EFDD0  E8 FB B0 0D 00                  call 0x1404caed0
003EFDD5  C6 47 01 01                     mov byte ptr [rdi + 1], 1
003EFDD9  E9 4D 01 00 00                  jmp 0x1403eff2b
003EFDDE  48 B9 FF DF BE 7D FB F6 FF FF   movabs rcx, 0xfffff6fb7dbedfff
003EFDE8  48 8B C9                        mov rcx, rcx
003EFDEB  48 3B F1                        cmp rsi, rcx
003EFDEE  0F 87 82 FC FF FF               ja 0x1403efa76
003EFDF4  BB 01 00 00 00                  mov ebx, 1
003EFDF9  E9 7A FC FF FF                  jmp 0x1403efa78
003EFDFE  F7 45 60 00 01 00 00            test dword ptr [rbp + 0x60], 0x100
003EFE05  0F 85 A1 01 00 00               jne 0x1403effac
003EFE0B  48 8B 54 24 40                  mov rdx, qword ptr [rsp + 0x40]
003EFE10  48 8D 4D 10                     lea rcx, [rbp + 0x10]
003EFE14  E8 5B 02 F9 FF                  call 0x140380074
003EFE19  44 8B C8                        mov r9d, eax
003EFE1C  E9 CA FD FF FF                  jmp 0x1403efbeb
003EFE21  89 45 B8                        mov dword ptr [rbp - 0x48], eax
003EFE24  48 8D 4C 24 78                  lea rcx, [rsp + 0x78]
003EFE29  48 8D 45 90                     lea rax, [rbp - 0x70]
003EFE2D  4C 89 64 24 78                  mov qword ptr [rsp + 0x78], r12
003EFE32  48 83 C8 01                     or rax, 1
003EFE36  48 C7 45 80 00 10 00 00         mov qword ptr [rbp - 0x80], 0x1000
003EFE3E  48 89 45 20                     mov qword ptr [rbp + 0x20], rax
003EFE42  C6 45 90 02                     mov byte ptr [rbp - 0x70], 2
003EFE46  48 89 4D 98                     mov qword ptr [rbp - 0x68], rcx
003EFE4A  48 C7 45 A0 01 00 00 00         mov qword ptr [rbp - 0x60], 1
003EFE52  E9 4B FD FF FF                  jmp 0x1403efba2
003EFE57  49 8B CE                        mov rcx, r14
003EFE5A  E8 61 36 ED FF                  call 0x1402c34c0
003EFE5F  85 C0                           test eax, eax
003EFE61  0F 85 EF FB FF FF               jne 0x1403efa56
003EFE67  49 8B 17                        mov rdx, qword ptr [r15]
003EFE6A  49 8B CE                        mov rcx, r14
003EFE6D  E8 5E 96 10 00                  call 0x1404f94d0
003EFE72  8B D8                           mov ebx, eax
003EFE74  39 44 24 48                     cmp dword ptr [rsp + 0x48], eax
003EFE78  0F 85 D8 FB FF FF               jne 0x1403efa56
003EFE7E  B9 04 00 00 00                  mov ecx, 4
003EFE83  E8 78 7B F4 FF                  call 0x140337a00
003EFE88  B9 01 00 00 00                  mov ecx, 1
003EFE8D  48 89 06                        mov qword ptr [rsi], rax
003EFE90  B2 11                           mov dl, 0x11
003EFE92  E8 89 71 EA FF                  call 0x140297020
003EFE97  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
003EFE9C  4C 8B CE                        mov r9, rsi
003EFE9F  49 8B 0F                        mov rcx, qword ptr [r15]
003EFEA2  48 8B D7                        mov rdx, rdi
003EFEA5  44 8B C3                        mov r8d, ebx
003EFEA8  44 89 6C 24 20                  mov dword ptr [rsp + 0x20], r13d
003EFEAD  E8 E6 05 00 00                  call 0x1403f0498
003EFEB2  85 C0                           test eax, eax
003EFEB4  0F 84 98 00 00 00               je 0x1403eff52
003EFEBA  48 B9 00 D0 BE 7D FB F6 FF FF   movabs rcx, 0xfffff6fb7dbed000
003EFEC4  48 8B C1                        mov rax, rcx
003EFEC7  48 3B F0                        cmp rsi, rax
003EFECA  0F 83 C1 00 00 00               jae 0x1403eff91
003EFED0  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
003EFEDA  48 8B D6                        mov rdx, rsi
003EFEDD  48 C1 EA 09                     shr rdx, 9
003EFEE1  48 23 D0                        and rdx, rax
003EFEE4  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
003EFEEE  48 8B C0                        mov rax, rax
003EFEF1  41 B9 02 00 00 00               mov r9d, 2
003EFEF7  48 03 D0                        add rdx, rax
003EFEFA  45 8D 41 FF                     lea r8d, [r9 - 1]
003EFEFE  E8 2D 37 E5 FF                  call 0x140243630
003EFF03  48 8B D6                        mov rdx, rsi
003EFF06  49 8B CF                        mov rcx, r15
003EFF09  E8 B6 02 00 00                  call 0x1403f01c4
003EFF0E  85 C0                           test eax, eax
003EFF10  B9 34 04 00 C0                  mov ecx, 0xc0000434
003EFF15  0F 48 C8                        cmovs ecx, eax
003EFF18  8B C1                           mov eax, ecx
003EFF1A  E9 E0 FC FF FF                  jmp 0x1403efbff
003EFF1F  B2 11                           mov dl, 0x11
003EFF21  B9 01 00 00 00                  mov ecx, 1
003EFF26  E8 F5 70 EA FF                  call 0x140297020
003EFF2B  B8 34 04 00 C0                  mov eax, 0xc0000434
003EFF30  E9 CA FC FF FF                  jmp 0x1403efbff
003EFF35  48 85 FF                        test rdi, rdi
003EFF38  0F 84 57 AF 2F 00               je 0x1406eae95
003EFF3E  48 8D 47 38                     lea rax, [rdi + 0x38]
003EFF42  48 39 00                        cmp qword ptr [rax], rax
003EFF45  0F 84 4A AF 2F 00               je 0x1406eae95
003EFF4B  4D 85 F6                        test r14, r14
003EFF4E  74 DB                           je 0x1403eff2b
003EFF50  EB CD                           jmp 0x1403eff1f
003EFF52  48 8B 05 27 09 C2 FF            mov rax, qword ptr [rip - 0x3df6d9]
003EFF59  45 33 C0                        xor r8d, r8d
003EFF5C  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
003EFF61  B2 11                           mov dl, 0x11
003EFF63  48 8B CB                        mov rcx, rbx
003EFF66  48 89 06                        mov qword ptr [rsi], rax
003EFF69  E8 22 D3 E8 FF                  call 0x14027d290
003EFF6E  45 33 C9                        xor r9d, r9d
003EFF71  45 33 C0                        xor r8d, r8d
003EFF74  48 8B D7                        mov rdx, rdi
003EFF77  33 C9                           xor ecx, ecx
003EFF79  E8 02 EF E8 FF                  call 0x14027ee80
003EFF7E  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
003EFF83  80 63 0D FE                     and byte ptr [rbx + 0xd], 0xfe
003EFF87  E8 64 CC E8 FF                  call 0x14027cbf0
003EFF8C  88 43 0C                        mov byte ptr [rbx + 0xc], al
003EFF8F  EB 9A                           jmp 0x1403eff2b
003EFF91  48 B9 FF DF BE 7D FB F6 FF FF   movabs rcx, 0xfffff6fb7dbedfff
003EFF9B  48 8B C1                        mov rax, rcx
003EFF9E  48 3B F0                        cmp rsi, rax
003EFFA1  0F 86 5C FF FF FF               jbe 0x1403eff03
003EFFA7  E9 24 FF FF FF                  jmp 0x1403efed0
003EFFAC  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
003EFFB1  8B 80 C0 00 00 00               mov eax, dword ptr [rax + 0xc0]
003EFFB7  48 8B 54 24 40                  mov rdx, qword ptr [rsp + 0x40]
003EFFBC  0F BA E8 13                     bts eax, 0x13
003EFFC0  89 82 C0 00 00 00               mov dword ptr [rdx + 0xc0], eax
003EFFC6  E9 45 FE FF FF                  jmp 0x1403efe10
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiInPagePageTable(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m140;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m180;
    unsigned __int64 v_stack_m190;
    unsigned __int64 v_stack_m198;
    unsigned __int64 v_stack_m1A0;
    unsigned __int64 v_stack_m1A8;
    unsigned int v_stack_m1B0;
    unsigned __int64 v_stack_m1B8;
    unsigned int v_stack_m1C0;
    unsigned __int64 v_stack_m1C8;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m90;
    unsigned int v_stack_m98;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p40;
    unsigned int v_stack_p48;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p78;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (448);
    result = (*(unsigned __int64 *)(v_rip + 10595902)) ^ (v_rsp);
    v_stack_m48 = result;
    a2 = 0;
    v_stack_m1B0 = (unsigned int)((int)(a2));
    result = memset(v_stack_mE8, a2, 152, a4);
    a2 = 0;
    result = memset(v_stack_m168, a2, a2 + 120, a4);
    v_stack_m180 = v_xmm0;
    v_stack_m1A8 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184);
    v_stack_m190 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1024;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a1 + 16))) & (1)) != 0) goto loc_003EFCF3;
loc_003EF97E:
    v_rdi = 0;
loc_003EF980:
    v_stack_m198 = a1 + 56;
    result = MI_READ_PTE_LOCK_FREE(*(unsigned __int64 *)(a1 + (int)(a2) * 8 + 24), a2, a2 + 120, a4);
    v_r12 = (*(unsigned __int64 *)(a1 + (int)(a2) * 8 + 24)) << (25);
    result = (v_r13) << (25);
    v_r12 = (v_r12) - (result);
    v_r12 = (v_r12) >> (16);
    result = MiCheckVirtualAddress(*(unsigned __int64 *)(a1), v_stack_m1C0, v_stack_m1C8, a4);
    v_stack_m1A0 = result;
    if (result != 0) goto loc_003EFADC;
    if ((*(unsigned __int64 *)(a1)) >= result) goto loc_003EFD1E;
loc_003EF9F8:
    if (((unsigned int)((unsigned int)(v_stack_m1C0))) == 24) goto loc_003EFC2A;
    if (v_stack_m1C8 == 0) goto loc_003EFA1F;
    if (((*(unsigned int *)(v_stack_m1C8 + 48)) & (0x200000ULL)) != 0) goto loc_003EFC9D;
loc_003EFA1F:
    if (*(unsigned __int64 *)(v_stack_m1A8 + 624) != 0) goto loc_003EFF35;
    if (v_stack_m1C8 == 0) goto loc_003EFA56;
    if (0 != 0) goto loc_003EFD8F;
loc_003EFA42:
    if (v_stack_m1C8 == 0) goto loc_003EFA56;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m1C8 + 48))) & (112));
    if (((unsigned __int8)(result)) == 80) goto loc_003EFE57;
loc_003EFA56:
    result = MiMakeDemandZeroPte(4, v_stack_m1C0, v_stack_m1C8, a4);
    if ((*(unsigned __int64 *)(a1 + (int)(a2) * 8 + 24)) >= 4) goto loc_003EFDDE;
loc_003EFA76:
    v_rbx = 0;
loc_003EFA78:
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + (int)(a2) * 8 + 24)) = result;
    v_r14 = v_stack_m1C8;
    if (v_stack_m1C8 != 0) {
        result = *(unsigned __int64 *)(gs_base + (0 + 392));
        a1 = *(unsigned __int64 *)(result + 184);
        a1 = *(unsigned __int64 *)(a1 + 1040);
        a1 = (a1) + (0x3ECULL);
        result = ExReleaseSpinLockSharedFromDpcLevel(a1, v_stack_m1C0, v_stack_m1C8, a4);
        v_r14 = v_stack_m1C8;
    }
    if (0 != 0) goto loc_003EFB0E;
    v_rsi = (*(unsigned __int64 *)(a1 + (int)(a2) * 8 + 24)) >> (9);
    a2 = (v_stack_m1C0) & (v_rsi);
    a2 = (a2) + ((unsigned int)(v_stack_m1C0));
    result = MiIncreaseUsedPtes(a1, a2, v_rbx + 1, v_rbx + 2);
    goto loc_003EFB0E;
loc_003EFADC:
    if (v_stack_m1C8 == 0) goto loc_003EFB18;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1040)) + (0x3ECULL);
    result = ExReleaseSpinLockSharedFromDpcLevel(a1, a2, v_rbx + 1, v_rbx + 2);
loc_003EFB0E:
loc_003EFB18:
    *(unsigned __int64 *)(v_stack_mE8) = v_xmm0;
    *(unsigned __int64 *)(v_stack_mE8 + 16) = v_xmm1;
    *(unsigned __int64 *)(v_stack_mE8 + 32) = v_xmm0;
    *(unsigned __int64 *)(v_stack_mE8 + 48) = v_xmm1;
    *(unsigned __int64 *)(v_stack_mE8 + 64) = v_xmm0;
    *(unsigned __int64 *)(v_stack_mE8 + 80) = v_xmm1;
    *(unsigned __int64 *)(v_stack_mE8 + 96) = v_xmm0;
    *(unsigned __int64 *)(v_stack_mE8 + 128 * 1 - 16) = v_xmm0;
    *(unsigned __int64 *)(v_stack_mE8 + 128 * 1) = v_xmm1;
    *(unsigned __int64 *)(v_stack_mE8 + 128 * 1 + 16) = *(unsigned __int64 *)(a1 + 128 * 1 + 16);
    result = MiNodeFromFaultPacket(a1, 128, v_rbx + 1, v_rbx + 2);
    result = MiGetClosestImplicitNode((unsigned int)((unsigned int)(result)), 128, v_rbx + 1, v_rbx + 2);
    a2 = (*(unsigned __int64 *)(a1 + 16)) & (-2);
    if ((((unsigned __int8)(*(unsigned __int64 *)(a1 + 16))) & (1)) != 0) goto loc_003EFCD9;
loc_003EFBA2:
    v_stack_mE0 = 2;
    a1 = 0;
    v_stack_mE8 = v_r12;
    v_stack_m90 = v_stack_m1C8;
loc_003EFBB4:
    v_r12 = (v_r12) >> (9);
    v_r12 = (v_r12) & (v_r10);
    v_r12 = (v_r12) + ((unsigned int)(v_stack_m1C0));
    *(unsigned __int64 *)(v_stack_mF8 + a1 * 8 + 40) = v_r12;
    a1 = (a1) + 1;
    if (a1 < 4) goto loc_003EFBB4;
    result = MiDispatchFault(v_stack_mE8, v_stack_m1B8, v_rbx + 1, v_rbx + 2);
    if (((unsigned int)(result)) == 0xC0033333ULL) goto loc_003EFDFE;
loc_003EFBEB:
    result = MiPropagateFaultPacketFields(a1, v_stack_mE8, v_rbx + 1, (unsigned int)((unsigned int)(result)));
    if (!sign_flag) goto loc_003EFC5C;
loc_003EFBFF:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, v_stack_mE8, v_rbx + 1, (unsigned int)((unsigned int)(result)));
    v_rsp = (v_rsp) + (448);
    return result;
loc_003EFC2A:
    result = MiCheckFatalAccessViolation(a1, v_stack_p30, *(unsigned __int64 *)(a1 + 8), v_stack_m1C8);
    if (v_stack_p30 != 0) goto loc_003EFC8F;
loc_003EFC43:
    if ((*(unsigned __int64 *)(a1)) <= result) goto loc_003EFC65;
loc_003EFC55:
    goto loc_003EFBFF;
loc_003EFC5C:
    result = 0;
    goto loc_003EFBFF;
loc_003EFC65:
    if (v_stack_p30 == 0) goto loc_003EFC55;
    if (0 == 0) goto loc_003EFC55;
    result = MiGetLeafVa(v_rsi + 8, v_stack_p30, *(unsigned __int64 *)(a1 + 8), *(unsigned __int64 *)(a1));
loc_003EFC8F:
    result = MiUnlockVadTree(1, 17, *(unsigned __int64 *)(a1 + 8), *(unsigned __int64 *)(a1));
    goto loc_003EFC43;
loc_003EFC9D:
    if (0 == 0) goto loc_003EFA1F;
    v_rbx = (*(unsigned __int64 *)(a1 + 16)) & (-2);
    if (condition_is_below) goto loc_003EFA1F;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m1C0)))) >> (3));
loc_003EFCD9:
    if (((unsigned __int8)(*(unsigned __int8 *)(17))) != 1) goto loc_003EFD05;
    if (((unsigned __int8)(*(unsigned __int8 *)(17))) == 2) goto loc_003EFE21;
loc_003EFCE9:
    goto loc_003EFBA2;
loc_003EFCF3:
    v_rdi = (v_rdi) & (-2);
    if ((*(unsigned __int8 *)(v_rdi)) == 1) goto loc_003EF980;
    goto loc_003EF97E;
loc_003EFD05:
    if (((unsigned __int8)(*(unsigned __int8 *)(17))) == 3) goto loc_003EFCE9;
    if (((unsigned __int8)(*(unsigned __int8 *)(17))) == 2) goto loc_003EFE21;
    if (((unsigned __int8)(*(unsigned __int8 *)(17))) != 5) goto loc_003EFBA2;
    goto loc_003EFCE9;
loc_003EFD1E:
    if (v_rdi != 0) goto loc_003EFF2B;
    if ((*(unsigned __int8 *)(17)) < ((unsigned int)(v_stack_m1C0))) goto loc_003EF9F8;
    if ((*(unsigned __int8 *)(17)) > ((unsigned int)(v_stack_m1C0))) goto loc_003EF9F8;
    if (*(unsigned __int64 *)(a1 + 16) == 0) goto loc_003EF9F8;
    result = (*(unsigned __int64 *)(a1 + 16)) & (-2);
    if ((((unsigned __int8)(*(unsigned __int64 *)(a1 + 16))) & (1)) == 0) goto loc_003EFD71;
    if ((*(unsigned __int8 *)(result)) == 7) goto loc_003EF9F8;
    if ((*(unsigned __int8 *)(result)) == 8) goto loc_003EF9F8;
loc_003EFD71:
    v_stack_p20 = 6;
    result = KeBugCheckEx(80, *(unsigned __int8 *)(17), *(unsigned __int64 *)(a1 + 8), v_rsi);
loc_003EFD8F:
    result = MiIsVadLarge(v_stack_m1C8, *(unsigned __int8 *)(17), *(unsigned __int64 *)(a1 + 8), v_rsi);
    if ((unsigned int)(result) == 0) goto loc_003EFA42;
    v_rbx = (*(unsigned __int8 *)(v_stack_m1C8 + 33)) << (32);
    v_rbx = (v_rbx) | ((unsigned int)(*(unsigned int *)(v_stack_m1C8 + 28)));
    result = MiUnlockVadTree(1, 17, *(unsigned __int64 *)(a1 + 8), v_rsi);
    v_rbx = (v_rbx) << (12);
    v_rbx = (v_rbx) | (0xFFFULL);
    result = MiLeapPrefetch(v_rdi, v_rbx + 4096, *(unsigned __int64 *)(a1 + 8), v_rsi);
    *(unsigned __int8 *)(v_rdi + 1) = 1;
    goto loc_003EFF2B;
loc_003EFDDE:
    if (v_rsi > v_rdi) goto loc_003EFA76;
    goto loc_003EFA78;
loc_003EFDFE:
    if (((v_stack_m98) & (256)) != 0) goto loc_003EFFAC;
loc_003EFE10:
    result = MiIssueHardFault(v_stack_mE8, v_stack_p40, *(unsigned __int64 *)(a1 + 8), v_rsi);
    goto loc_003EFBEB;
loc_003EFE21:
    v_stack_m140 = (unsigned int)(result);
    v_stack_p78 = v_r12;
    result = (v_stack_m168) | (1);
    v_stack_m178 = 0x1000ULL;
    v_stack_mD8 = result;
    v_stack_m168 = 2;
    v_stack_m160 = v_stack_p78;
    v_stack_m158 = 1;
    goto loc_003EFBA2;
loc_003EFE57:
    result = MiVadPureReserve(v_stack_m1C8, v_stack_p40, *(unsigned __int64 *)(a1 + 8), (unsigned int)((unsigned int)(result)));
    if ((unsigned int)(result) != 0) goto loc_003EFA56;
    result = MiGetLargeVadMappingIndex(v_stack_m1C8, *(unsigned __int64 *)(a1), *(unsigned __int64 *)(a1 + 8), (unsigned int)((unsigned int)(result)));
    if (v_stack_p48 != ((unsigned int)(result))) goto loc_003EFA56;
    result = MiMakeDemandZeroPte(4, *(unsigned __int64 *)(a1), *(unsigned __int64 *)(a1 + 8), (unsigned int)((unsigned int)(result)));
    *(unsigned __int64 *)(v_rsi) = result;
    result = MiUnlockVadTree(1, 17, *(unsigned __int64 *)(a1 + 8), (unsigned int)((unsigned int)(result)));
    v_stack_p20 = (unsigned int)((unsigned int)(v_stack_m1C0));
    result = MiInsertLargeVadMapping(*(unsigned __int64 *)(a1), v_stack_p58, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), v_rsi);
    if ((unsigned int)(result) == 0) goto loc_003EFF52;
    if (v_rsi >= (*(unsigned __int64 *)(a1))) goto loc_003EFF91;
loc_003EFED0:
    a2 = (v_rsi) >> (9);
    a2 = (a2) & (*(unsigned __int64 *)(a1));
    a2 = (a2) + (*(unsigned __int64 *)(a1));
    result = MiIncreaseUsedPtes(*(unsigned __int64 *)(a1), a2, 2 - 1, 2);
loc_003EFF03:
    result = MiLargePageFault(a1, v_rsi, 2 - 1, 2);
    a1 = (unsigned int)(0xC0000434ULL);
    if (sign_flag) { a1 = (unsigned int)(result); }
    goto loc_003EFBFF;
loc_003EFF1F:
    result = MiUnlockVadTree(1, 17, 2 - 1, 2);
loc_003EFF2B:
    goto loc_003EFBFF;
loc_003EFF35:
    if (v_stack_m1C8 == 0) goto loc_003EFF2B;
    goto loc_003EFF1F;
loc_003EFF52:
    a3 = 0;
    *(unsigned __int64 *)(v_rsi) = *(unsigned __int64 *)(v_rip - 4060889);
    result = MiReleaseFaultState(v_stack_p60, 17, a3, 2);
    a4 = 0;
    a3 = 0;
    a1 = 0;
    result = MmAccessFault(a1, v_stack_p58, a3, a4);
    result = MiLockWorkingSetShared(v_stack_p68, v_stack_p58, a3, a4);
    *(unsigned __int8 *)(v_stack_p60 + 12) = (unsigned __int8)(result);
    goto loc_003EFF2B;
loc_003EFF91:
    if (v_rsi <= v_stack_p68) goto loc_003EFF03;
    goto loc_003EFED0;
loc_003EFFAC:
    *(unsigned int *)(v_stack_p40 + 192) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p40 + 192)));
    goto loc_003EFE10;
}
```

## 5. (Beta) C Style

```c
int64_t MiInPagePageTable(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m140;
    uint64_t v_stack_m158;
    uint64_t v_stack_m160;
    uint64_t v_stack_m168;
    uint64_t v_stack_m178;
    uint64_t v_stack_m180;
    uint64_t v_stack_m190;
    uint64_t v_stack_m198;
    uint64_t v_stack_m1A0;
    uint64_t v_stack_m1A8;
    uint32_t v_stack_m1B0;
    uint64_t v_stack_m1B8;
    uint32_t v_stack_m1C0;
    uint64_t v_stack_m1C8;
    uint64_t v_stack_m48;
    uint64_t v_stack_m90;
    uint32_t v_stack_m98;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p30;
    uint64_t v_stack_p40;
    uint32_t v_stack_p48;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint64_t v_stack_p78;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (448);
    result = (*(uint64_t *)(v_rip + 0xA1AE3E)) ^ (local_rsp);
    v_stack_m48 = result;
    Arg2 = 0;
    v_stack_m1B0 = (uint32_t)((int32_t)(Arg2));
    result = memset(v_stack_mE8, Arg2, 152, a4);
    Arg2 = 0;
    result = memset(v_stack_m168, Arg2, Arg2 + 120, a4);
    v_stack_m180 = v_xmm0;
    v_stack_m1A8 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8);
    v_stack_m190 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 1024;
    if ((((uint8_t)(*(uint64_t *)(arg1 + 0x10))) & (1)) != 0) goto loc_003EFCF3;
loc_003EF97E:
    local_rdi = 0;
loc_003EF980:
    v_stack_m198 = Arg1 + 56;
    result = MI_READ_PTE_LOCK_FREE(*(uint64_t *)(arg1 + (int32_t)(Arg2) * 8 + 0x18), Arg2, Arg2 + 120, a4);
    local_r12 = (*(uint64_t *)(arg1 + (int32_t)(Arg2) * 8 + 0x18)) << (25);
    result = (local_r13) << (25);
    local_r12 = (local_r12) - (result);
    local_r12 = (local_r12) >> (16);
    result = MiCheckVirtualAddress(*(uint64_t *)(arg1), v_stack_m1C0, v_stack_m1C8, a4);
    v_stack_m1A0 = result;
    if (result != 0) goto loc_003EFADC;
    if ((*(uint64_t *)(arg1)) >= result) goto loc_003EFD1E;
loc_003EF9F8:
    if (((uint32_t)((uint32_t)(v_stack_m1C0))) == 24) goto loc_003EFC2A;
    if (v_stack_m1C8 == 0) goto loc_003EFA1F;
    if (((*(uint32_t *)(v_stack_m1C8 + 0x30)) & (0x200000ULL)) != 0) goto loc_003EFC9D;
loc_003EFA1F:
    if (*(uint64_t *)(v_stack_m1A8 + 0x270) != 0) goto loc_003EFF35;
    if (v_stack_m1C8 == 0) goto loc_003EFA56;
    if (0 != 0) goto loc_003EFD8F;
loc_003EFA42:
    if (v_stack_m1C8 == 0) goto loc_003EFA56;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m1C8 + 0x30))) & (112));
    if (((uint8_t)(result)) == 80) goto loc_003EFE57;
loc_003EFA56:
    result = MiMakeDemandZeroPte(4, v_stack_m1C0, v_stack_m1C8, a4);
    if ((*(uint64_t *)(arg1 + (int32_t)(Arg2) * 8 + 0x18)) >= 4) goto loc_003EFDDE;
loc_003EFA76:
    local_rbx = 0;
loc_003EFA78:
    *(uint64_t *)(*(uint64_t *)(arg1 + (int32_t)(Arg2) * 8 + 0x18)) = result;
    local_r14 = v_stack_m1C8;
    if (v_stack_m1C8 != 0) {
        result = *(uint64_t *)(gs_base + (0 + 0x188));
        Arg1 = *(uint64_t *)(result + 0xB8);
        Arg1 = *(uint64_t *)(arg1 + 0x410);
        Arg1 = (Arg1) + (0x3ECULL);
        result = ExReleaseSpinLockSharedFromDpcLevel(Arg1, v_stack_m1C0, v_stack_m1C8, a4);
        local_r14 = v_stack_m1C8;
    }
    if (0 != 0) goto loc_003EFB0E;
    local_rsi = (*(uint64_t *)(arg1 + (int32_t)(Arg2) * 8 + 0x18)) >> (9);
    Arg2 = (v_stack_m1C0) & (local_rsi);
    Arg2 = (Arg2) + ((uint32_t)(v_stack_m1C0));
    result = MiIncreaseUsedPtes(Arg1, Arg2, local_rbx + 1, local_rbx + 2);
    goto loc_003EFB0E;
loc_003EFADC:
    if (v_stack_m1C8 == 0) goto loc_003EFB18;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x410)) + (0x3ECULL);
    result = ExReleaseSpinLockSharedFromDpcLevel(Arg1, Arg2, local_rbx + 1, local_rbx + 2);
loc_003EFB0E:
loc_003EFB18:
    *(uint64_t *)(v_stack_mE8) = v_xmm0;
    *(uint64_t *)(v_stack_mE8 + 0x10) = v_xmm1;
    *(uint64_t *)(v_stack_mE8 + 0x20) = v_xmm0;
    *(uint64_t *)(v_stack_mE8 + 0x30) = v_xmm1;
    *(uint64_t *)(v_stack_mE8 + 0x40) = v_xmm0;
    *(uint64_t *)(v_stack_mE8 + 0x50) = v_xmm1;
    *(uint64_t *)(v_stack_mE8 + 0x60) = v_xmm0;
    *(uint64_t *)(v_stack_mE8 + 0x80 * 1 - 0x10) = v_xmm0;
    *(uint64_t *)(v_stack_mE8 + 0x80 * 1) = v_xmm1;
    *(uint64_t *)(v_stack_mE8 + 0x80 * 1 + 0x10) = *(uint64_t *)(arg1 + 0x80 * 1 + 0x10);
    result = MiNodeFromFaultPacket(Arg1, 128, local_rbx + 1, local_rbx + 2);
    result = MiGetClosestImplicitNode((uint32_t)((uint32_t)(result)), 128, local_rbx + 1, local_rbx + 2);
    Arg2 = (*(uint64_t *)(arg1 + 0x10)) & (-2);
    if ((((uint8_t)(*(uint64_t *)(arg1 + 0x10))) & (1)) != 0) goto loc_003EFCD9;
loc_003EFBA2:
    v_stack_mE0 = 2;
    Arg1 = 0;
    v_stack_mE8 = local_r12;
    v_stack_m90 = v_stack_m1C8;
loc_003EFBB4:
    local_r12 = (local_r12) >> (9);
    local_r12 = (local_r12) & (local_r10);
    local_r12 = (local_r12) + ((uint32_t)(v_stack_m1C0));
    *(uint64_t *)(v_stack_mF8 + arg1 * 8 + 0x28) = local_r12;
    Arg1 = (Arg1) + 1;
    if (Arg1 < 4) goto loc_003EFBB4;
    result = MiDispatchFault(v_stack_mE8, v_stack_m1B8, local_rbx + 1, local_rbx + 2);
    if (((uint32_t)(result)) == 0xC0033333ULL) goto loc_003EFDFE;
loc_003EFBEB:
    result = MiPropagateFaultPacketFields(Arg1, v_stack_mE8, local_rbx + 1, (uint32_t)((uint32_t)(result)));
    if (!sign_flag) goto loc_003EFC5C;
loc_003EFBFF:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_stack_mE8, local_rbx + 1, (uint32_t)((uint32_t)(result)));
    local_rsp = (local_rsp) + (448);
    return result;
loc_003EFC2A:
    result = MiCheckFatalAccessViolation(Arg1, v_stack_p30, *(uint64_t *)(arg1 + 0x8), v_stack_m1C8);
    if (v_stack_p30 != 0) goto loc_003EFC8F;
loc_003EFC43:
    if ((*(uint64_t *)(arg1)) <= result) goto loc_003EFC65;
loc_003EFC55:
    goto loc_003EFBFF;
loc_003EFC5C:
    result = 0;
    goto loc_003EFBFF;
loc_003EFC65:
    if (v_stack_p30 == 0) goto loc_003EFC55;
    if (0 == 0) goto loc_003EFC55;
    result = MiGetLeafVa(local_rsi + 8, v_stack_p30, *(uint64_t *)(arg1 + 0x8), *(uint64_t *)(arg1));
loc_003EFC8F:
    result = MiUnlockVadTree(1, 17, *(uint64_t *)(arg1 + 0x8), *(uint64_t *)(arg1));
    goto loc_003EFC43;
loc_003EFC9D:
    if (0 == 0) goto loc_003EFA1F;
    local_rbx = (*(uint64_t *)(arg1 + 0x10)) & (-2);
    if (condition_is_below) goto loc_003EFA1F;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m1C0)))) >> (3));
loc_003EFCD9:
    if (((uint8_t)(*(uint8_t *)(17))) != 1) goto loc_003EFD05;
    if (((uint8_t)(*(uint8_t *)(17))) == 2) goto loc_003EFE21;
loc_003EFCE9:
    goto loc_003EFBA2;
loc_003EFCF3:
    local_rdi = (local_rdi) & (-2);
    if ((*(uint8_t *)(local_rdi)) == 1) goto loc_003EF980;
    goto loc_003EF97E;
loc_003EFD05:
    if (((uint8_t)(*(uint8_t *)(17))) == 3) goto loc_003EFCE9;
    if (((uint8_t)(*(uint8_t *)(17))) == 2) goto loc_003EFE21;
    if (((uint8_t)(*(uint8_t *)(17))) != 5) goto loc_003EFBA2;
    goto loc_003EFCE9;
loc_003EFD1E:
    if (local_rdi != 0) goto loc_003EFF2B;
    if ((*(uint8_t *)(17)) < ((uint32_t)(v_stack_m1C0))) goto loc_003EF9F8;
    if ((*(uint8_t *)(17)) > ((uint32_t)(v_stack_m1C0))) goto loc_003EF9F8;
    if (*(uint64_t *)(arg1 + 0x10) == 0) goto loc_003EF9F8;
    result = (*(uint64_t *)(arg1 + 0x10)) & (-2);
    if ((((uint8_t)(*(uint64_t *)(arg1 + 0x10))) & (1)) == 0) goto loc_003EFD71;
    if ((*(uint8_t *)(result)) == 7) goto loc_003EF9F8;
    if ((*(uint8_t *)(result)) == 8) goto loc_003EF9F8;
loc_003EFD71:
    v_stack_p20 = 6;
    result = KeBugCheckEx(80, *(uint8_t *)(17), *(uint64_t *)(arg1 + 0x8), local_rsi);
loc_003EFD8F:
    result = MiIsVadLarge(v_stack_m1C8, *(uint8_t *)(17), *(uint64_t *)(arg1 + 0x8), local_rsi);
    if ((uint32_t)(result) == 0) goto loc_003EFA42;
    local_rbx = (*(uint8_t *)(v_stack_m1C8 + 0x21)) << (32);
    local_rbx = (local_rbx) | ((uint32_t)(*(uint32_t *)(v_stack_m1C8 + 0x1C)));
    result = MiUnlockVadTree(1, 17, *(uint64_t *)(arg1 + 0x8), local_rsi);
    local_rbx = (local_rbx) << (12);
    local_rbx = (local_rbx) | (0xFFFULL);
    result = MiLeapPrefetch(local_rdi, local_rbx + 4096, *(uint64_t *)(arg1 + 0x8), local_rsi);
    *(uint8_t *)(local_rdi + 0x1) = 1;
    goto loc_003EFF2B;
loc_003EFDDE:
    if (local_rsi > local_rdi) goto loc_003EFA76;
    goto loc_003EFA78;
loc_003EFDFE:
    if (((v_stack_m98) & (256)) != 0) goto loc_003EFFAC;
loc_003EFE10:
    result = MiIssueHardFault(v_stack_mE8, v_stack_p40, *(uint64_t *)(arg1 + 0x8), local_rsi);
    goto loc_003EFBEB;
loc_003EFE21:
    v_stack_m140 = (uint32_t)(result);
    v_stack_p78 = local_r12;
    result = (v_stack_m168) | (1);
    v_stack_m178 = 0x1000ULL;
    v_stack_mD8 = result;
    v_stack_m168 = 2;
    v_stack_m160 = v_stack_p78;
    v_stack_m158 = 1;
    goto loc_003EFBA2;
loc_003EFE57:
    result = MiVadPureReserve(v_stack_m1C8, v_stack_p40, *(uint64_t *)(arg1 + 0x8), (uint32_t)((uint32_t)(result)));
    if ((uint32_t)(result) != 0) goto loc_003EFA56;
    result = MiGetLargeVadMappingIndex(v_stack_m1C8, *(uint64_t *)(arg1), *(uint64_t *)(arg1 + 0x8), (uint32_t)((uint32_t)(result)));
    if (v_stack_p48 != ((uint32_t)(result))) goto loc_003EFA56;
    result = MiMakeDemandZeroPte(4, *(uint64_t *)(arg1), *(uint64_t *)(arg1 + 0x8), (uint32_t)((uint32_t)(result)));
    *(uint64_t *)(local_rsi) = result;
    result = MiUnlockVadTree(1, 17, *(uint64_t *)(arg1 + 0x8), (uint32_t)((uint32_t)(result)));
    v_stack_p20 = (uint32_t)((uint32_t)(v_stack_m1C0));
    result = MiInsertLargeVadMapping(*(uint64_t *)(arg1), v_stack_p58, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), local_rsi);
    if ((uint32_t)(result) == 0) goto loc_003EFF52;
    if (local_rsi >= (*(uint64_t *)(arg1))) goto loc_003EFF91;
loc_003EFED0:
    Arg2 = (local_rsi) >> (9);
    Arg2 = (Arg2) & (*(uint64_t *)(arg1));
    Arg2 = (Arg2) + (*(uint64_t *)(arg1));
    result = MiIncreaseUsedPtes(*(uint64_t *)(arg1), Arg2, 2 - 1, 2);
loc_003EFF03:
    result = MiLargePageFault(Arg1, local_rsi, 2 - 1, 2);
    Arg1 = (uint32_t)(0xC0000434ULL);
    if (sign_flag) { Arg1 = (uint32_t)(result); }
    goto loc_003EFBFF;
loc_003EFF1F:
    result = MiUnlockVadTree(1, 17, 2 - 1, 2);
loc_003EFF2B:
    goto loc_003EFBFF;
loc_003EFF35:
    if (v_stack_m1C8 == 0) goto loc_003EFF2B;
    goto loc_003EFF1F;
loc_003EFF52:
    a3 = 0;
    *(uint64_t *)(local_rsi) = *(uint64_t *)(v_rip - 0x3DF6D9);
    result = MiReleaseFaultState(v_stack_p60, 17, a3, 2);
    a4 = 0;
    a3 = 0;
    Arg1 = 0;
    result = MmAccessFault(Arg1, v_stack_p58, a3, a4);
    result = MiLockWorkingSetShared(v_stack_p68, v_stack_p58, a3, a4);
    *(uint8_t *)(v_stack_p60 + 0xC) = (uint8_t)(result);
    goto loc_003EFF2B;
loc_003EFF91:
    if (local_rsi <= v_stack_p68) goto loc_003EFF03;
    goto loc_003EFED0;
loc_003EFFAC:
    *(uint32_t *)(v_stack_p40 + 0xC0) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p40 + 0xC0)));
    goto loc_003EFE10;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x0` | `128` | `R` |
| `Arg1` | `+ 0x0 + rdx*1` | `128` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x10` | `128` | `R` |
| `Arg1` | `+ 0x10 + rdx*1` | `64` | `R` |
| `Arg1` | `+ 0x18 + rbx*8` | `64` | `R` |
| `Arg1` | `+ 0x20` | `128` | `R` |
| `Arg1` | `+ 0x30` | `128` | `R` |
| `Arg1` | `+ 0x38` | `64` | `R` |
| `Arg1` | `+ 0x40` | `128` | `R` |
| `Arg1` | `+ 0x50` | `32` | `R/W` |
| `Arg1` | `+ 0x50` | `128` | `R` |
| `Arg1` | `+ 0x60` | `128` | `R` |
| `Arg1` | `+ 0x70` | `128` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003EF8DC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
