# HalpIommuCreateDevice

- RVA: `0x0054ED60`–`0x0054F35F` (길이 `1,535` bytes)
- VA: `0x000000014054ED60`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C4224`
- 디코드: `410`개 명령, `1,535/1,535` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **40**; 고유 호출 대상: **24**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **10**

### Outgoing calls
- `0x0054EDDA` → [KeAbPreAcquire](../21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0054EDF3` → [ExfAcquirePushLockExclusiveEx](../20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x0054EE1B` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x0054EE27` → [ExAcquireSpinLockExclusiveAtDpcLevel](../24/ExAcquireSpinLockExclusiveAtDpcLevel_function_00248E80.md) (function, `0x00248E80`)
- `0x0054EE4E` → [IidAreIdsStrictlyEqual](../6A/IidAreIdsStrictlyEqual_function_006A2BE4.md) (function, `0x006A2BE4`)
- `0x0054EED3` → [IommupDeviceGetPasidSettings](IommupDeviceGetPasidSettings_function_0054F910.md) (function, `0x0054F910`)
- `0x0054EF4F` → [ExReleaseSpinLockExclusiveFromDpcLevel](../24/ExReleaseSpinLockExclusiveFromDpcLevel_function_002497E0.md) (function, `0x002497E0`)
- `0x0054EF63` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0054EF81` → [ObfReferenceObjectWithTag](../21/ObfReferenceObjectWithTag_function_00210710.md) (function, `0x00210710`)
- `0x0054EF92` → [ObfDereferenceObjectWithTag](../2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x0054EFC5` → [IommupDeviceDisablePasidTaggedDma](../../page/70/IommupDeviceDisablePasidTaggedDma_function_007089A8.md) (function, `0x007089A8`)
- `0x0054EFD8` → [ObfDereferenceObjectWithTag](../2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x0054EFF7` → [IommupHvUnregisterDeviceId](../56/IommupHvUnregisterDeviceId_function_00567878.md) (function, `0x00567878`)
- `0x0054F008` → [ExReleaseSpinLockExclusiveFromDpcLevel](../24/ExReleaseSpinLockExclusiveFromDpcLevel_function_002497E0.md) (function, `0x002497E0`)
- `0x0054F01D` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0054F02F` → [HalpMmAllocCtxAlloc](../3E/HalpMmAllocCtxAlloc_function_003E10B8.md) (function, `0x003E10B8`)
- `0x0054F067` → [HalpIommuCloneDeviceId](../4E/HalpIommuCloneDeviceId_function_004E4228.md) (function, `0x004E4228`)
- `0x0054F07D` → [HalpMmAllocCtxAlloc](../3E/HalpMmAllocCtxAlloc_function_003E10B8.md) (function, `0x003E10B8`)
- `0x0054F09C` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0054F0D4` → [HalpIommuQueryAcpiDeviceMapping](../4B/HalpIommuQueryAcpiDeviceMapping_function_004BC784.md) (function, `0x004BC784`)
- `0x0054F0EB` → [HalpIommuCloneDeviceId](../4E/HalpIommuCloneDeviceId_function_004E4228.md) (function, `0x004E4228`)
- `0x0054F143` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0054F162` → [HalpIommuCreateDeviceInternal](../4D/HalpIommuCreateDeviceInternal_function_004D9A4C.md) (function, `0x004D9A4C`)
- `0x0054F19B` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0054F1B2` → [ExWaitForRundownProtectionRelease](../2A/ExWaitForRundownProtectionRelease_function_002A4CB0.md) (function, `0x002A4CB0`)
- `0x0054F1D6` → [HalpIommuCloneDeviceId](../4E/HalpIommuCloneDeviceId_function_004E4228.md) (function, `0x004E4228`)
- `0x0054F1FD` → [ObfReferenceObjectWithTag](../21/ObfReferenceObjectWithTag_function_00210710.md) (function, `0x00210710`)
- `0x0054F222` → [IommupDeviceEnablePasidTaggedDma](../../page/70/IommupDeviceEnablePasidTaggedDma_function_00708B74.md) (function, `0x00708B74`)
- `0x0054F234` → [HalpIommuCheckDpptException](../4C/HalpIommuCheckDpptException_function_004C6478.md) (function, `0x004C6478`)
- `0x0054F260` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x0054F26C` → [ExAcquireSpinLockExclusiveAtDpcLevel](../24/ExAcquireSpinLockExclusiveAtDpcLevel_function_00248E80.md) (function, `0x00248E80`)
- `0x0054F2A3` → [ExReleaseSpinLockExclusiveFromDpcLevel](../24/ExReleaseSpinLockExclusiveFromDpcLevel_function_002497E0.md) (function, `0x002497E0`)
- `0x0054F2B8` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0054F2D6` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0054F2DE` → [HalpMmAllocCtxFree](../3E/HalpMmAllocCtxFree_function_003E1904.md) (function, `0x003E1904`)
- `0x0054F2FB` → [HalpMmAllocCtxFree](../3E/HalpMmAllocCtxFree_function_003E1904.md) (function, `0x003E1904`)
- `0x0054F303` → [HalpMmAllocCtxFree](../3E/HalpMmAllocCtxFree_function_003E1904.md) (function, `0x003E1904`)
- `0x0054F311` → [HalpMmAllocCtxFree](../3E/HalpMmAllocCtxFree_function_003E1904.md) (function, `0x003E1904`)
- `0x0054F330` → [ExfTryToWakePushLock](../26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x0054F33C` → [KeAbPostRelease](../2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)

### Direct callers
- [HalpIommuUnblockDevice](../4C/HalpIommuUnblockDevice_function_004C6250.md) at `0x004C6300`
- [IommuCreateAtsDevice](../56/IommuCreateAtsDevice_function_00564BB0.md) at `0x00564C78`
- [IommuMapDevice](../56/IommuMapDevice_function_00565AB0.md) at `0x00565B0B`
- [IommuDomainAttachDevice](../56/IommuDomainAttachDevice_function_00567960.md) at `0x005679DD`
- [IommuDeviceCreate](../../page/70/IommuDeviceCreate_function_0070D030.md) at `0x0070D07D`

### Static image references
- `0x0054ED8A` → RVA `0x00FC18C0` (`.data`; read)
- `0x0054EE0E` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x0054EE20` → RVA `0x00FC18E0` (`.data`; read)
- `0x0054EE2C` → RVA `0x00FC18D0` (`.data`; read)
- `0x0054EFE6` → RVA `0x00FC1710` (`.data`; read)
- `0x0054F105` → RVA `0x00E117E0` (`.data`; read/write)
- `0x0054F139` → RVA `0x00FC1DF8` (`.data`; read)
- `0x0054F271` → RVA `0x00FC18D8` (`.data`; read)
- `0x0054F29C` → RVA `0x00FC18D8` (`.data`; write)
- `0x0054F31A` → RVA `0x00FC18C0` (`.data`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x0054EFC5` → [IommupDeviceDisablePasidTaggedDma](../../page/70/IommupDeviceDisablePasidTaggedDma_function_007089A8.md) (`.text` → `PAGE`)
  - `0x0054F222` → [IommupDeviceEnablePasidTaggedDma](../../page/70/IommupDeviceEnablePasidTaggedDma_function_00708B74.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0054ED60  48 8B C4                        mov rax, rsp
0054ED63  48 89 58 20                     mov qword ptr [rax + 0x20], rbx
0054ED67  4C 89 40 18                     mov qword ptr [rax + 0x18], r8
0054ED6B  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
0054ED6F  48 89 48 08                     mov qword ptr [rax + 8], rcx
0054ED73  55                              push rbp
0054ED74  56                              push rsi
0054ED75  57                              push rdi
0054ED76  41 54                           push r12
0054ED78  41 55                           push r13
0054ED7A  41 56                           push r14
0054ED7C  41 57                           push r15
0054ED7E  48 8B EC                        mov rbp, rsp
0054ED81  48 81 EC 80 00 00 00            sub rsp, 0x80
0054ED88  33 F6                           xor esi, esi
0054ED8A  4C 8D 35 2F 2B A7 00            lea r14, [rip + 0xa72b2f]
0054ED91  0F 57 C0                        xorps xmm0, xmm0
0054ED94  48 89 75 D8                     mov qword ptr [rbp - 0x28], rsi
0054ED98  33 C0                           xor eax, eax
0054ED9A  48 89 75 C0                     mov qword ptr [rbp - 0x40], rsi
0054ED9E  49 8B CE                        mov rcx, r14
0054EDA1  48 89 45 F8                     mov qword ptr [rbp - 8], rax
0054EDA5  45 33 C0                        xor r8d, r8d
0054EDA8  48 89 75 D0                     mov qword ptr [rbp - 0x30], rsi
0054EDAC  33 D2                           xor edx, edx
0054EDAE  48 89 75 C8                     mov qword ptr [rbp - 0x38], rsi
0054EDB2  45 8B F9                        mov r15d, r9d
0054EDB5  40 88 75 B5                     mov byte ptr [rbp - 0x4b], sil
0054EDB9  0F 11 45 E8                     movups xmmword ptr [rbp - 0x18], xmm0
0054EDBD  8B FE                           mov edi, esi
0054EDBF  40 88 75 B6                     mov byte ptr [rbp - 0x4a], sil
0054EDC3  40 88 75 B3                     mov byte ptr [rbp - 0x4d], sil
0054EDC7  44 8B EE                        mov r13d, esi
0054EDCA  40 88 75 B1                     mov byte ptr [rbp - 0x4f], sil
0054EDCE  40 88 75 B7                     mov byte ptr [rbp - 0x49], sil
0054EDD2  40 88 75 B2                     mov byte ptr [rbp - 0x4e], sil
0054EDD6  40 88 75 B8                     mov byte ptr [rbp - 0x48], sil
0054EDDA  E8 51 14 CC FF                  call 0x140210230
0054EDDF  F0 49 0F BA 2E 00               lock bts qword ptr [r14], 0
0054EDE5  48 8B D8                        mov rbx, rax
0054EDE8  73 0E                           jae 0x14054edf8
0054EDEA  4D 8B C6                        mov r8, r14
0054EDED  48 8B D0                        mov rdx, rax
0054EDF0  49 8B CE                        mov rcx, r14
0054EDF3  E8 98 0E CC FF                  call 0x14020fc90
0054EDF8  48 85 DB                        test rbx, rbx
0054EDFB  74 04                           je 0x14054ee01
0054EDFD  C6 43 0A 01                     mov byte ptr [rbx + 0xa], 1
0054EE01  45 0F 20 C4                     mov r12, cr8
0054EE05  B8 0F 00 00 00                  mov eax, 0xf
0054EE0A  44 0F 22 C0                     mov cr8, rax
0054EE0E  39 35 0C 7F A7 00               cmp dword ptr [rip + 0xa77f0c], esi
0054EE14  74 0A                           je 0x14054ee20
0054EE16  8A D0                           mov dl, al
0054EE18  41 8A CC                        mov cl, r12b
0054EE1B  E8 DC 68 FA FF                  call 0x1404f56fc
0054EE20  48 8D 0D B9 2A A7 00            lea rcx, [rip + 0xa72ab9]
0054EE27  E8 54 A0 CF FF                  call 0x140248e80
0054EE2C  48 8B 35 9D 2A A7 00            mov rsi, qword ptr [rip + 0xa72a9d]
0054EE33  4C 8B 75 40                     mov r14, qword ptr [rbp + 0x40]
0054EE37  48 8D 05 92 2A A7 00            lea rax, [rip + 0xa72a92]
0054EE3E  48 3B F0                        cmp rsi, rax
0054EE41  0F 84 BA 01 00 00               je 0x14054f001
0054EE47  48 8B 4E 10                     mov rcx, qword ptr [rsi + 0x10]
0054EE4B  49 8B D6                        mov rdx, r14
0054EE4E  E8 91 3D 15 00                  call 0x1406a2be4
0054EE53  84 C0                           test al, al
0054EE55  75 05                           jne 0x14054ee5c
0054EE57  48 8B 36                        mov rsi, qword ptr [rsi]
0054EE5A  EB DB                           jmp 0x14054ee37
0054EE5C  4C 8B 46 18                     mov r8, qword ptr [rsi + 0x18]
0054EE60  41 8B 88 88 01 00 00            mov ecx, dword ptr [r8 + 0x188]
0054EE67  41 8B 90 84 01 00 00            mov edx, dword ptr [r8 + 0x184]
0054EE6E  41 3B CF                        cmp ecx, r15d
0054EE71  74 49                           je 0x14054eebc
0054EE73  85 C9                           test ecx, ecx
0054EE75  74 0F                           je 0x14054ee86
0054EE77  83 E9 01                        sub ecx, 1
0054EE7A  74 31                           je 0x14054eead
0054EE7C  83 E9 01                        sub ecx, 1
0054EE7F  74 3B                           je 0x14054eebc
0054EE81  83 F9 01                        cmp ecx, 1
0054EE84  75 16                           jne 0x14054ee9c
0054EE86  41 83 FF 01                     cmp r15d, 1
0054EE8A  0F 95 C0                        setne al
0054EE8D  41 83 FF 02                     cmp r15d, 2
0054EE91  75 05                           jne 0x14054ee98
0054EE93  41 3B D7                        cmp edx, r15d
0054EE96  75 04                           jne 0x14054ee9c
0054EE98  84 C0                           test al, al
0054EE9A  75 20                           jne 0x14054eebc
0054EE9C  BB BB 00 00 C0                  mov ebx, 0xc00000bb
0054EEA1  4C 8B 75 48                     mov r14, qword ptr [rbp + 0x48]
0054EEA5  44 8A FF                        mov r15b, dil
0054EEA8  E9 9B 00 00 00                  jmp 0x14054ef48
0054EEAD  41 83 FF 02                     cmp r15d, 2
0054EEB1  75 E9                           jne 0x14054ee9c
0054EEB3  41 3B D7                        cmp edx, r15d
0054EEB6  74 04                           je 0x14054eebc
0054EEB8  32 C0                           xor al, al
0054EEBA  EB DC                           jmp 0x14054ee98
0054EEBC  45 87 B8 88 01 00 00            xchg dword ptr [r8 + 0x188], r15d
0054EEC3  48 8B 4D 50                     mov rcx, qword ptr [rbp + 0x50]
0054EEC7  4C 8D 45 B6                     lea r8, [rbp - 0x4a]
0054EECB  4C 8D 4D B7                     lea r9, [rbp - 0x49]
0054EECF  48 8D 55 B5                     lea rdx, [rbp - 0x4b]
0054EED3  E8 38 0A 00 00                  call 0x14054f910
0054EED8  8B D8                           mov ebx, eax
0054EEDA  85 C0                           test eax, eax
0054EEDC  78 C3                           js 0x14054eea1
0054EEDE  8A 45 B5                        mov al, byte ptr [rbp - 0x4b]
0054EEE1  40 38 7D B6                     cmp byte ptr [rbp - 0x4a], dil
0054EEE5  75 04                           jne 0x14054eeeb
0054EEE7  84 C0                           test al, al
0054EEE9  74 04                           je 0x14054eeef
0054EEEB  B2 01                           mov dl, 1
0054EEED  EB 03                           jmp 0x14054eef2
0054EEEF  40 8A D7                        mov dl, dil
0054EEF2  48 8B 4E 18                     mov rcx, qword ptr [rsi + 0x18]
0054EEF6  38 91 12 01 00 00               cmp byte ptr [rcx + 0x112], dl
0054EEFC  75 9E                           jne 0x14054ee9c
0054EEFE  38 81 11 01 00 00               cmp byte ptr [rcx + 0x111], al
0054EF04  75 96                           jne 0x14054ee9c
0054EF06  8A 45 B7                        mov al, byte ptr [rbp - 0x49]
0054EF09  38 81 10 01 00 00               cmp byte ptr [rcx + 0x110], al
0054EF0F  75 8B                           jne 0x14054ee9c
0054EF11  FF 46 20                        inc dword ptr [rsi + 0x20]
0054EF14  33 DB                           xor ebx, ebx
0054EF16  48 8B 45 60                     mov rax, qword ptr [rbp + 0x60]
0054EF1A  4C 8B 75 48                     mov r14, qword ptr [rbp + 0x48]
0054EF1E  4C 8B 69 08                     mov r13, qword ptr [rcx + 8]
0054EF22  C6 45 B1 01                     mov byte ptr [rbp - 0x4f], 1
0054EF26  48 89 08                        mov qword ptr [rax], rcx
0054EF29  4D 85 F6                        test r14, r14
0054EF2C  74 17                           je 0x14054ef45
0054EF2E  4D 3B F5                        cmp r14, r13
0054EF31  74 12                           je 0x14054ef45
0054EF33  4C 89 71 08                     mov qword ptr [rcx + 8], r14
0054EF37  41 B7 01                        mov r15b, 1
0054EF3A  4D 85 ED                        test r13, r13
0054EF3D  74 09                           je 0x14054ef48
0054EF3F  44 88 7D B8                     mov byte ptr [rbp - 0x48], r15b
0054EF43  EB 03                           jmp 0x14054ef48
0054EF45  44 8A FB                        mov r15b, bl
0054EF48  48 8D 0D 91 29 A7 00            lea rcx, [rip + 0xa72991]
0054EF4F  E8 8C A8 CF FF                  call 0x1402497e0
0054EF54  39 3D C6 7D A7 00               cmp dword ptr [rip + 0xa77dc6], edi
0054EF5A  74 0C                           je 0x14054ef68
0054EF5C  44 0F 20 C1                     mov rcx, cr8
0054EF60  41 8A D4                        mov dl, r12b
0054EF63  E8 30 67 FA FF                  call 0x1404f5698
0054EF68  41 0F B6 C4                     movzx eax, r12b
0054EF6C  44 0F 22 C0                     mov cr8, rax
0054EF70  45 84 FF                        test r15b, r15b
0054EF73  74 22                           je 0x14054ef97
0054EF75  41 BF 48 61 6C 44               mov r15d, 0x446c6148
0054EF7B  49 8B CE                        mov rcx, r14
0054EF7E  41 8B D7                        mov edx, r15d
0054EF81  E8 8A 17 CC FF                  call 0x140210710
0054EF86  40 38 7D B8                     cmp byte ptr [rbp - 0x48], dil
0054EF8A  74 0B                           je 0x14054ef97
0054EF8C  41 8B D7                        mov edx, r15d
0054EF8F  49 8B CD                        mov rcx, r13
0054EF92  E8 49 89 DA FF                  call 0x1402f78e0
0054EF97  45 33 ED                        xor r13d, r13d
0054EF9A  8A 45 B3                        mov al, byte ptr [rbp - 0x4d]
0054EF9D  44 8A 75 B1                     mov r14b, byte ptr [rbp - 0x4f]
0054EFA1  44 8A 7D B2                     mov r15b, byte ptr [rbp - 0x4e]
0054EFA5  88 45 B3                        mov byte ptr [rbp - 0x4d], al
0054EFA8  85 DB                           test ebx, ebx
0054EFAA  0F 89 66 03 00 00               jns 0x14054f316
0054EFB0  48 85 FF                        test rdi, rdi
0054EFB3  0F 84 2D 03 00 00               je 0x14054f2e6
0054EFB9  44 38 AF 12 01 00 00            cmp byte ptr [rdi + 0x112], r13b
0054EFC0  74 08                           je 0x14054efca
0054EFC2  48 8B CF                        mov rcx, rdi
0054EFC5  E8 DE 99 1B 00                  call 0x1407089a8
0054EFCA  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
0054EFCE  48 85 C9                        test rcx, rcx
0054EFD1  74 0A                           je 0x14054efdd
0054EFD3  BA 48 61 6C 44                  mov edx, 0x446c6148
0054EFD8  E8 03 89 DA FF                  call 0x1402f78e0
0054EFDD  45 84 FF                        test r15b, r15b
0054EFE0  0F 84 F5 02 00 00               je 0x14054f2db
0054EFE6  44 38 2D 23 27 A7 00            cmp byte ptr [rip + 0xa72723], r13b
0054EFED  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
0054EFF1  0F 84 D0 02 00 00               je 0x14054f2c7
0054EFF7  E8 7C 88 01 00                  call 0x140567878
0054EFFC  E9 DA 02 00 00                  jmp 0x14054f2db
0054F001  48 8D 0D D8 28 A7 00            lea rcx, [rip + 0xa728d8]
0054F008  E8 D3 A7 CF FF                  call 0x1402497e0
0054F00D  44 39 2D 0C 7D A7 00            cmp dword ptr [rip + 0xa77d0c], r13d
0054F014  74 0C                           je 0x14054f022
0054F016  44 0F 20 C1                     mov rcx, cr8
0054F01A  41 8A D4                        mov dl, r12b
0054F01D  E8 76 66 FA FF                  call 0x1404f5698
0054F022  41 0F B6 C4                     movzx eax, r12b
0054F026  44 0F 22 C0                     mov cr8, rax
0054F02A  BA 28 00 00 00                  mov edx, 0x28
0054F02F  E8 84 20 E9 FF                  call 0x1403e10b8
0054F034  48 8B F0                        mov rsi, rax
0054F037  48 85 C0                        test rax, rax
0054F03A  75 0A                           jne 0x14054f046
0054F03C  BB 9A 00 00 C0                  mov ebx, 0xc000009a
0054F041  E9 D0 02 00 00                  jmp 0x14054f316
0054F046  0F 57 C0                        xorps xmm0, xmm0
0054F049  48 8D 56 10                     lea rdx, [rsi + 0x10]
0054F04D  0F 11 06                        movups xmmword ptr [rsi], xmm0
0054F050  33 C0                           xor eax, eax
0054F052  41 BC 01 00 00 00               mov r12d, 1
0054F058  0F 11 46 10                     movups xmmword ptr [rsi + 0x10], xmm0
0054F05C  49 8B CE                        mov rcx, r14
0054F05F  48 89 46 20                     mov qword ptr [rsi + 0x20], rax
0054F063  44 88 65 B3                     mov byte ptr [rbp - 0x4d], r12b
0054F067  E8 BC 51 F9 FF                  call 0x1404e4228
0054F06C  8B D8                           mov ebx, eax
0054F06E  85 C0                           test eax, eax
0054F070  0F 88 24 FF FF FF               js 0x14054ef9a
0054F076  BB A8 01 00 00                  mov ebx, 0x1a8
0054F07B  8B D3                           mov edx, ebx
0054F07D  E8 36 20 E9 FF                  call 0x1403e10b8
0054F082  48 8B F8                        mov rdi, rax
0054F085  48 85 C0                        test rax, rax
0054F088  75 0A                           jne 0x14054f094
0054F08A  BB 9A 00 00 C0                  mov ebx, 0xc000009a
0054F08F  E9 5E 02 00 00                  jmp 0x14054f2f2
0054F094  4C 8B C3                        mov r8, rbx
0054F097  33 D2                           xor edx, edx
0054F099  48 8B CF                        mov rcx, rdi
0054F09C  E8 9F 7B 17 00                  call 0x1406c6c40
0054F0A1  44 38 2D 68 26 A7 00            cmp byte ptr [rip + 0xa72668], r13b
0054F0A8  48 89 7E 18                     mov qword ptr [rsi + 0x18], rdi
0054F0AC  44 89 BF 84 01 00 00            mov dword ptr [rdi + 0x184], r15d
0054F0B3  44 89 BF 88 01 00 00            mov dword ptr [rdi + 0x188], r15d
0054F0BA  4C 89 AF A0 01 00 00            mov qword ptr [rdi + 0x1a0], r13
0054F0C1  0F 84 8D 00 00 00               je 0x14054f154
0054F0C7  41 83 3E 02                     cmp dword ptr [r14], 2
0054F0CB  75 35                           jne 0x14054f102
0054F0CD  48 8D 55 E8                     lea rdx, [rbp - 0x18]
0054F0D1  49 8B CE                        mov rcx, r14
0054F0D4  E8 AB D6 F6 FF                  call 0x1404bc784
0054F0D9  8B D8                           mov ebx, eax
0054F0DB  85 C0                           test eax, eax
0054F0DD  0F 88 B7 FE FF FF               js 0x14054ef9a
0054F0E3  48 8D 55 40                     lea rdx, [rbp + 0x40]
0054F0E7  48 8D 4D E8                     lea rcx, [rbp - 0x18]
0054F0EB  E8 38 51 F9 FF                  call 0x1404e4228
0054F0F0  8B D8                           mov ebx, eax
0054F0F2  85 C0                           test eax, eax
0054F0F4  0F 88 A0 FE FF FF               js 0x14054ef9a
0054F0FA  48 8B 45 40                     mov rax, qword ptr [rbp + 0x40]
0054F0FE  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
0054F102  41 8B C4                        mov eax, r12d
0054F105  F0 0F C1 05 D3 26 8C 00         lock xadd dword ptr [rip + 0x8c26d3], eax
0054F10D  41 03 C4                        add eax, r12d
0054F110  4C 63 F0                        movsxd r14, eax
0054F113  48 B8 FF FF FF FF FF FF FF 1F   movabs rax, 0x1fffffffffffffff
0054F11D  4C 3B F0                        cmp r14, rax
0054F120  76 10                           jbe 0x14054f132
0054F122  BB 9A 00 00 C0                  mov ebx, 0xc000009a
0054F127  45 8A FD                        mov r15b, r13b
0054F12A  45 8A F5                        mov r14b, r13b
0054F12D  E9 87 FE FF FF                  jmp 0x14054efb9
0054F132  4C 8B 7D 40                     mov r15, qword ptr [rbp + 0x40]
0054F136  49 8B D6                        mov rdx, r14
0054F139  48 8B 05 B8 2C A7 00            mov rax, qword ptr [rip + 0xa72cb8]
0054F140  49 8B CF                        mov rcx, r15
0054F143  E8 88 B9 16 00                  call 0x1406baad0
0054F148  8B D8                           mov ebx, eax
0054F14A  85 C0                           test eax, eax
0054F14C  78 D9                           js 0x14054f127
0054F14E  4C 89 77 20                     mov qword ptr [rdi + 0x20], r14
0054F152  EB 71                           jmp 0x14054f1c5
0054F154  4C 8D 4D D0                     lea r9, [rbp - 0x30]
0054F158  48 8B D7                        mov rdx, rdi
0054F15B  4C 8D 45 C8                     lea r8, [rbp - 0x38]
0054F15F  49 8B CE                        mov rcx, r14
0054F162  E8 E5 A8 F8 FF                  call 0x1404d9a4c
0054F167  8B D8                           mov ebx, eax
0054F169  85 C0                           test eax, eax
0054F16B  0F 88 29 FE FF FF               js 0x14054ef9a
0054F171  48 8B 45 C8                     mov rax, qword ptr [rbp - 0x38]
0054F175  48 8B 4D D0                     mov rcx, qword ptr [rbp - 0x30]
0054F179  48 89 47 28                     mov qword ptr [rdi + 0x28], rax
0054F17D  48 89 4F 20                     mov qword ptr [rdi + 0x20], rcx
0054F181  48 8B 81 D0 00 00 00            mov rax, qword ptr [rcx + 0xd0]
0054F188  48 85 C0                        test rax, rax
0054F18B  74 1B                           je 0x14054f1a8
0054F18D  48 8B 49 10                     mov rcx, qword ptr [rcx + 0x10]
0054F191  4C 8D 4D D8                     lea r9, [rbp - 0x28]
0054F195  45 8A C4                        mov r8b, r12b
0054F198  49 8B D6                        mov rdx, r14
0054F19B  E8 30 B9 16 00                  call 0x1406baad0
0054F1A0  48 8B 45 D8                     mov rax, qword ptr [rbp - 0x28]
0054F1A4  48 89 47 30                     mov qword ptr [rdi + 0x30], rax
0054F1A8  48 8D 5F 40                     lea rbx, [rdi + 0x40]
0054F1AC  48 8B CB                        mov rcx, rbx
0054F1AF  4C 89 2B                        mov qword ptr [rbx], r13
0054F1B2  E8 F9 5A D5 FF                  call 0x1402a4cb0
0054F1B7  49 8B C4                        mov rax, r12
0054F1BA  48 87 03                        xchg qword ptr [rbx], rax
0054F1BD  83 4F 48 FF                     or dword ptr [rdi + 0x48], 0xffffffff
0054F1C1  4C 8B 7D 40                     mov r15, qword ptr [rbp + 0x40]
0054F1C5  44 88 65 B2                     mov byte ptr [rbp - 0x4e], r12b
0054F1C9  4C 39 6D C0                     cmp qword ptr [rbp - 0x40], r13
0054F1CD  75 16                           jne 0x14054f1e5
0054F1CF  48 8D 55 C0                     lea rdx, [rbp - 0x40]
0054F1D3  49 8B CF                        mov rcx, r15
0054F1D6  E8 4D 50 F9 FF                  call 0x1404e4228
0054F1DB  8B D8                           mov ebx, eax
0054F1DD  85 C0                           test eax, eax
0054F1DF  0F 88 B5 FD FF FF               js 0x14054ef9a
0054F1E5  48 8B 5D 48                     mov rbx, qword ptr [rbp + 0x48]
0054F1E9  48 8B 45 C0                     mov rax, qword ptr [rbp - 0x40]
0054F1ED  48 89 07                        mov qword ptr [rdi], rax
0054F1F0  48 85 DB                        test rbx, rbx
0054F1F3  74 0D                           je 0x14054f202
0054F1F5  BA 48 61 6C 44                  mov edx, 0x446c6148
0054F1FA  48 8B CB                        mov rcx, rbx
0054F1FD  E8 0E 15 CC FF                  call 0x140210710
0054F202  48 8B 55 50                     mov rdx, qword ptr [rbp + 0x50]
0054F206  48 8D 87 68 01 00 00            lea rax, [rdi + 0x168]
0054F20D  48 89 5F 08                     mov qword ptr [rdi + 8], rbx
0054F211  48 8B CF                        mov rcx, rdi
0054F214  48 89 40 08                     mov qword ptr [rax + 8], rax
0054F218  48 89 00                        mov qword ptr [rax], rax
0054F21B  4C 89 AF 78 01 00 00            mov qword ptr [rdi + 0x178], r13
0054F222  E8 4D 99 1B 00                  call 0x140708b74
0054F227  8B D8                           mov ebx, eax
0054F229  85 C0                           test eax, eax
0054F22B  0F 88 69 FD FF FF               js 0x14054ef9a
0054F231  49 8B CF                        mov rcx, r15
0054F234  E8 3F 72 F7 FF                  call 0x1404c6478
0054F239  88 47 58                        mov byte ptr [rdi + 0x58], al
0054F23C  48 8B 45 60                     mov rax, qword ptr [rbp + 0x60]
0054F240  44 89 66 20                     mov dword ptr [rsi + 0x20], r12d
0054F244  48 89 38                        mov qword ptr [rax], rdi
0054F247  44 0F 20 C7                     mov rdi, cr8
0054F24B  BA 0F 00 00 00                  mov edx, 0xf
0054F250  44 0F 22 C2                     mov cr8, rdx
0054F254  44 39 2D C5 7A A7 00            cmp dword ptr [rip + 0xa77ac5], r13d
0054F25B  74 08                           je 0x14054f265
0054F25D  40 8A CF                        mov cl, dil
0054F260  E8 97 64 FA FF                  call 0x1404f56fc
0054F265  48 8D 0D 74 26 A7 00            lea rcx, [rip + 0xa72674]
0054F26C  E8 0F 9C CF FF                  call 0x140248e80
0054F271  48 8B 05 60 26 A7 00            mov rax, qword ptr [rip + 0xa72660]
0054F278  48 8D 0D 51 26 A7 00            lea rcx, [rip + 0xa72651]
0054F27F  48 39 08                        cmp qword ptr [rax], rcx
0054F282  74 07                           je 0x14054f28b
0054F284  B9 03 00 00 00                  mov ecx, 3
0054F289  CD 29                           int 0x29
0054F28B  48 89 0E                        mov qword ptr [rsi], rcx
0054F28E  48 8D 0D 4B 26 A7 00            lea rcx, [rip + 0xa7264b]
0054F295  48 89 46 08                     mov qword ptr [rsi + 8], rax
0054F299  48 89 30                        mov qword ptr [rax], rsi
0054F29C  48 89 35 35 26 A7 00            mov qword ptr [rip + 0xa72635], rsi
0054F2A3  E8 38 A5 CF FF                  call 0x1402497e0
0054F2A8  44 39 2D 71 7A A7 00            cmp dword ptr [rip + 0xa77a71], r13d
0054F2AF  74 0C                           je 0x14054f2bd
0054F2B1  44 0F 20 C1                     mov rcx, cr8
0054F2B5  40 8A D7                        mov dl, dil
0054F2B8  E8 DB 63 FA FF                  call 0x1404f5698
0054F2BD  40 0F B6 C7                     movzx eax, dil
0054F2C1  44 0F 22 C0                     mov cr8, rax
0054F2C5  EB 4F                           jmp 0x14054f316
0054F2C7  48 8B 41 60                     mov rax, qword ptr [rcx + 0x60]
0054F2CB  45 33 C0                        xor r8d, r8d
0054F2CE  48 8B 49 10                     mov rcx, qword ptr [rcx + 0x10]
0054F2D2  48 8B 57 28                     mov rdx, qword ptr [rdi + 0x28]
0054F2D6  E8 F5 B7 16 00                  call 0x1406baad0
0054F2DB  48 8B D7                        mov rdx, rdi
0054F2DE  E8 21 26 E9 FF                  call 0x1403e1904
0054F2E3  8A 45 B3                        mov al, byte ptr [rbp - 0x4d]
0054F2E6  45 84 F6                        test r14b, r14b
0054F2E9  74 03                           je 0x14054f2ee
0054F2EB  FF 4E 20                        dec dword ptr [rsi + 0x20]
0054F2EE  84 C0                           test al, al
0054F2F0  74 16                           je 0x14054f308
0054F2F2  48 8B 56 10                     mov rdx, qword ptr [rsi + 0x10]
0054F2F6  48 85 D2                        test rdx, rdx
0054F2F9  74 05                           je 0x14054f300
0054F2FB  E8 04 26 E9 FF                  call 0x1403e1904
0054F300  48 8B D6                        mov rdx, rsi
0054F303  E8 FC 25 E9 FF                  call 0x1403e1904
0054F308  48 8B 55 C0                     mov rdx, qword ptr [rbp - 0x40]
0054F30C  48 85 D2                        test rdx, rdx
0054F30F  74 05                           je 0x14054f316
0054F311  E8 EE 25 E9 FF                  call 0x1403e1904
0054F316  48 83 C8 FF                     or rax, 0xffffffffffffffff
0054F31A  F0 48 0F C1 05 9D 25 A7 00      lock xadd qword ptr [rip + 0xa7259d], rax
0054F323  24 06                           and al, 6
0054F325  3C 02                           cmp al, 2
0054F327  75 0C                           jne 0x14054f335
0054F329  48 8D 0D 90 25 A7 00            lea rcx, [rip + 0xa72590]
0054F330  E8 9B 6A D1 FF                  call 0x140265dd0
0054F335  48 8D 0D 84 25 A7 00            lea rcx, [rip + 0xa72584]
0054F33C  E8 BF 22 D9 FF                  call 0x1402e1600
0054F341  8B C3                           mov eax, ebx
0054F343  48 8B 9C 24 D8 00 00 00         mov rbx, qword ptr [rsp + 0xd8]
0054F34B  48 81 C4 80 00 00 00            add rsp, 0x80
0054F352  41 5F                           pop r15
0054F354  41 5E                           pop r14
0054F356  41 5D                           pop r13
0054F358  41 5C                           pop r12
0054F35A  5F                              pop rdi
0054F35B  5E                              pop rsi
0054F35C  5D                              pop rbp
0054F35D  C3                              ret
0054F35E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpIommuCreateDevice(__int64 a1, __int64 a2, __int64 a3, int a4, __int64 a5)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int8 v_stack_m80;
    unsigned __int8 v_stack_m81;
    unsigned __int8 v_stack_m82;
    unsigned __int8 v_stack_m83;
    unsigned __int8 v_stack_m85;
    unsigned __int8 v_stack_m86;
    unsigned __int8 v_stack_m87;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 32) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (128);
    v_rsi = 0;
    v_stack_m60 = 0;
    result = 0;
    v_stack_m78 = 0;
    v_stack_m40 = 0;
    a3 = 0;
    v_stack_m68 = 0;
    a2 = 0;
    v_stack_m70 = 0;
    v_stack_m83 = 0;
    v_stack_m50 = v_xmm0;
    v_stack_m82 = 0;
    v_stack_m85 = 0;
    v_stack_m87 = 0;
    v_stack_m81 = 0;
    v_stack_m86 = 0;
    v_stack_m80 = 0;
    result = KeAbPreAcquire(v_rip + 10955567, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = v_rip + 10955567;
        a2 = result;
        a1 = v_rip + 10955567;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    result = 15;
    if ((*(unsigned int *)(v_rip + 10977036)) != 0) {
        a2 = 15;
        a1 = (unsigned __int8)(v_cr8);
        result = KiRaiseIrqlProcessIrqlFlags(a1, a2, a3, a4);
    }
    result = ExAcquireSpinLockExclusiveAtDpcLevel(v_rip + 10955449, a2, a3, a4);
loc_0054EE37:
    if ((*(unsigned __int64 *)(v_rip + 10955421)) == (v_rip + 10955410)) goto loc_0054F001;
    result = IidAreIdsStrictlyEqual(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10955421) + 16), v_stack_p8, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_0054EE5C;
    goto loc_0054EE37;
loc_0054EE5C:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10955421)) + 24) + 392)))) == ((unsigned int)((unsigned int)(a4)))) goto loc_0054EEBC;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10955421)) + 24) + 392))) == 0) goto loc_0054EE86;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10955421)) + 24) + 392))) - (1));
    if (condition_is_equal) goto loc_0054EEAD;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0054EEBC;
    if (((unsigned int)(a1)) != 1) goto loc_0054EE9C;
loc_0054EE86:
    result = (((unsigned int)((unsigned int)(a4))) != 1) ? 1 : 0;
    if (((unsigned int)((unsigned int)(a4))) != 2) goto loc_0054EE98;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10955421)) + 24) + 388)))) != ((unsigned int)((unsigned int)(a4)))) goto loc_0054EE9C;
loc_0054EE98:
    if ((unsigned __int8)(result) != 0) goto loc_0054EEBC;
loc_0054EE9C:
loc_0054EEA1:
    goto loc_0054EF48;
loc_0054EEAD:
    if (0 != 2) goto loc_0054EE9C;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10955421)) + 24) + 388)))) == 0) goto loc_0054EEBC;
    result = 0;
    goto loc_0054EE98;
loc_0054EEBC:
    result = IommupDeviceGetPasidSettings(v_stack_p18, v_stack_m83, v_stack_m82, v_stack_m81);
    if (sign_flag) goto loc_0054EEA1;
    if (v_stack_m82 != 0) goto loc_0054EEEB;
    if ((unsigned __int8)(v_stack_m83) == 0) goto loc_0054EEEF;
loc_0054EEEB:
    goto loc_0054EEF2;
loc_0054EEEF:
loc_0054EEF2:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10955421)) + 24) + 274)) != 0) goto loc_0054EE9C;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10955421)) + 24) + 273)) != ((unsigned __int8)(v_stack_m83))) goto loc_0054EE9C;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10955421)) + 24) + 272)) != ((unsigned __int8)(v_stack_m81))) goto loc_0054EE9C;
    v_rbx = 0;
    v_stack_m87 = 1;
    *(unsigned __int64 *)(a5) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10955421)) + 24);
    if (v_stack_p10 == 0) goto loc_0054EF45;
    if (v_stack_p10 == (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10955421)) + 24) + 8))) goto loc_0054EF45;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10955421)) + 24) + 8) = v_stack_p10;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10955421)) + 24) + 8) == 0) goto loc_0054EF48;
    v_stack_m80 = 1;
    goto loc_0054EF48;
loc_0054EF45:
loc_0054EF48:
    result = ExReleaseSpinLockExclusiveFromDpcLevel(v_rip + 10955153, 0, v_stack_m82, v_stack_m81);
    if ((*(unsigned int *)(v_rip + 10976710)) != 0) {
        a1 = 15;
        a2 = (unsigned __int8)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, v_stack_m82, v_stack_m81);
    }
    if (0 == 0) goto loc_0054EF97;
    result = ObfReferenceObjectWithTag(v_stack_p10, (unsigned int)((unsigned int)((unsigned int)(0x446C6148ULL))), v_stack_m82, v_stack_m81);
    if (v_stack_m80 != 0) {
        a2 = (unsigned int)((unsigned int)(0x446C6148ULL));
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10955421)) + 24) + 8);
        result = ObfDereferenceObjectWithTag(a1, a2, v_stack_m82, v_stack_m81);
    }
    v_r13 = 0;
loc_0054EF9A:
    v_stack_m85 = (unsigned __int8)(v_stack_m85);
    if (!sign_flag) goto loc_0054F316;
    if (0 == 0) goto loc_0054F2E6;
loc_0054EFB9:
    result = v_stack_m85;
    if ((*(unsigned __int8 *)(0 + 274)) != 0) {
        a1 = 0;
        result = IommupDeviceDisablePasidTaggedDma(a1, a2, v_stack_m82, v_stack_m81);
    }
    if (*(unsigned __int64 *)(0 + 8) != 0) {
        a2 = 0x446C6148ULL;
        result = ObfDereferenceObjectWithTag(*(unsigned __int64 *)(0 + 8), a2, v_stack_m82, v_stack_m81);
    }
    if ((unsigned __int8)(v_stack_m86) == 0) goto loc_0054F2DB;
    if ((*(unsigned __int8 *)(v_rip + 10954531)) == 0) goto loc_0054F2C7;
    result = IommupHvUnregisterDeviceId(*(unsigned __int64 *)(0 + 32), a2, v_stack_m82, v_stack_m81);
    goto loc_0054F2DB;
loc_0054F001:
    result = ExReleaseSpinLockExclusiveFromDpcLevel(v_rip + 10954968, a2, v_stack_m82, v_stack_m81);
    if ((*(unsigned int *)(v_rip + 10976524)) != 0) {
        a1 = (unsigned __int8)(v_cr8);
        a2 = (unsigned __int8)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, v_stack_m82, v_stack_m81);
    }
    result = HalpMmAllocCtxAlloc(a1, 40, v_stack_m82, v_stack_m81);
    if (result != 0) goto loc_0054F046;
    goto loc_0054F316;
loc_0054F046:
    *(unsigned __int64 *)(result) = v_xmm0;
    result = 0;
    *(unsigned __int64 *)(result + 16) = v_xmm0;
    *(unsigned __int64 *)(result + 32) = 0;
    v_stack_m85 = 1;
    result = HalpIommuCloneDeviceId(v_stack_m87, result + 16, v_stack_m82, v_stack_m81);
    if (sign_flag) goto loc_0054EF9A;
    result = HalpMmAllocCtxAlloc(v_stack_m87, 424, v_stack_m82, v_stack_m81);
    if (result != 0) goto loc_0054F094;
    goto loc_0054F2F2;
loc_0054F094:
    a2 = 0;
    result = memset(result, a2, (unsigned int)(0xC000009AULL), v_stack_m81);
    *(unsigned __int64 *)(result + 24) = result;
    *(unsigned int *)(result + 388) = (unsigned int)(v_stack_m86);
    *(unsigned int *)(result + 392) = (unsigned int)(v_stack_m86);
    *(unsigned __int64 *)(result + 416) = 0;
    if ((*(unsigned __int8 *)(v_rip + 10954344)) == 0) goto loc_0054F154;
    if ((*(unsigned int *)(v_stack_m87)) != 2) goto loc_0054F102;
    result = HalpIommuQueryAcpiDeviceMapping(v_stack_m87, v_stack_m50, (unsigned int)(0xC000009AULL), v_stack_m81);
    if (sign_flag) goto loc_0054EF9A;
    result = HalpIommuCloneDeviceId(v_stack_m50, v_stack_p8, (unsigned int)(0xC000009AULL), v_stack_m81);
    if (sign_flag) goto loc_0054EF9A;
    v_stack_m78 = v_stack_p8;
loc_0054F102:
    result = (unsigned int)((1) + (1));
    if (((int)((unsigned int)(result))) <= result) goto loc_0054F132;
loc_0054F127:
    goto loc_0054EFB9;
loc_0054F132:
    result = guard_dispatch_icall(v_stack_p8, 0, (unsigned int)(0xC000009AULL), v_stack_m81);
    if (sign_flag) goto loc_0054F127;
    *(unsigned __int64 *)(result + 32) = 0;
    goto loc_0054F1C5;
loc_0054F154:
    result = HalpIommuCreateDeviceInternal(0, result, v_stack_m70, v_stack_m68);
    if (sign_flag) goto loc_0054EF9A;
    *(unsigned __int64 *)(result + 40) = v_stack_m70;
    *(unsigned __int64 *)(result + 32) = v_stack_m68;
    result = *(unsigned __int64 *)(v_stack_m68 + 208);
    if (*(unsigned __int64 *)(v_stack_m68 + 208) != 0) {
        a1 = *(unsigned __int64 *)(v_stack_m68 + 16);
        a4 = v_stack_m60;
        a3 = 1;
        a2 = 0;
        result = guard_dispatch_icall(a1, a2, a3, a4);
        result = v_stack_m60;
        *(unsigned __int64 *)(result + 48) = result;
    }
    *(unsigned __int64 *)(result + 64) = 0;
    result = ExWaitForRundownProtectionRelease(result + 64, a2, a3, a4);
loc_0054F1C5:
    v_stack_m86 = 1;
    if (v_stack_m78 != 0) goto loc_0054F1E5;
    result = HalpIommuCloneDeviceId(v_stack_p8, v_stack_m78, a3, a4);
    if (sign_flag) goto loc_0054EF9A;
loc_0054F1E5:
    *(unsigned __int64 *)(result) = v_stack_m78;
    result = v_stack_m78;
    if (v_stack_p10 != 0) {
        a2 = 0x446C6148ULL;
        a1 = v_stack_p10;
        result = ObfReferenceObjectWithTag(a1, a2, a3, a4);
    }
    *(unsigned __int64 *)(result + 8) = v_stack_p10;
    *(unsigned __int64 *)(result + 360 + 8) = result + 360;
    *(unsigned __int64 *)(result + 360) = result + 360;
    *(unsigned __int64 *)(result + 376) = 0;
    result = IommupDeviceEnablePasidTaggedDma(result, v_stack_p18, a3, a4);
    if (sign_flag) goto loc_0054EF9A;
    result = HalpIommuCheckDpptException(v_stack_p8, v_stack_p18, a3, a4);
    *(unsigned __int8 *)(result + 88) = (unsigned __int8)(result);
    *(unsigned int *)(result + 32) = 1;
    *(unsigned __int64 *)(a5) = result;
    result = a5;
    if ((*(unsigned int *)(v_rip + 10975941)) != 0) {
        a1 = (unsigned __int8)((unsigned __int8)(v_cr8));
        result = KiRaiseIrqlProcessIrqlFlags(a1, 15, a3, a4);
    }
    result = ExAcquireSpinLockExclusiveAtDpcLevel(v_rip + 10954356, 15, a3, a4);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10954336))) != (v_rip + 10954321)) {
        a1 = 3;
    }
    *(unsigned __int64 *)(result) = a1;
    *(unsigned __int64 *)(result + 8) = *(unsigned __int64 *)(v_rip + 10954336);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10954336)) = result;
    *(unsigned __int64 *)(v_rip + 10954293) = result;
    result = ExReleaseSpinLockExclusiveFromDpcLevel(v_rip + 10954315, 15, a3, a4);
    if ((*(unsigned int *)(v_rip + 10975857)) != 0) {
        a1 = 15;
        a2 = (unsigned __int8)((unsigned __int8)(v_cr8));
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, a3, a4);
    }
    goto loc_0054F316;
loc_0054F2C7:
    a3 = 0;
    result = guard_dispatch_icall(*(unsigned __int64 *)(a1 + 16), *(unsigned __int64 *)((unsigned __int8)(v_cr8) + 40), a3, a4);
loc_0054F2DB:
    result = HalpMmAllocCtxFree(*(unsigned __int64 *)(a1 + 16), (unsigned __int8)(v_cr8), a3, a4);
loc_0054F2E6:
    if (0 != 0) {
    }
    if ((unsigned __int8)(v_stack_m85) == 0) goto loc_0054F308;
loc_0054F2F2:
    result = v_stack_m85;
    if (*(unsigned __int64 *)(result + 16) != 0) {
        result = HalpMmAllocCtxFree(*(unsigned __int64 *)(a1 + 16), *(unsigned __int64 *)(result + 16), a3, a4);
    }
    result = HalpMmAllocCtxFree(*(unsigned __int64 *)(a1 + 16), result, a3, a4);
loc_0054F308:
    if (v_stack_m78 != 0) {
        result = HalpMmAllocCtxFree(*(unsigned __int64 *)(a1 + 16), v_stack_m78, a3, a4);
    }
    result = (result) | (-1);
    result = (unsigned __int8)((result) & (6));
    if (((unsigned __int8)(result)) == 2) {
        a1 = v_rip + 10954128;
        result = ExfTryToWakePushLock(a1, v_stack_m78, a3, a4);
    }
    result = KeAbPostRelease(v_rip + 10954116, v_stack_m78, a3, a4);
    v_rsp = (v_rsp) + (128);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
}
```

## 5. (Beta) C Style

```c
int64_t HalpIommuCreateDevice(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4, void *Arg5)
{
    uint8_t *arg5 = (uint8_t *)Arg5;

    int64_t result;
    int64_t local_r13;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint64_t v_stack_m50;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint8_t v_stack_m80;
    uint8_t v_stack_m81;
    uint8_t v_stack_m82;
    uint8_t v_stack_m83;
    uint8_t v_stack_m85;
    uint8_t v_stack_m86;
    uint8_t v_stack_m87;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x20) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (128);
    local_rsi = 0;
    v_stack_m60 = 0;
    result = 0;
    v_stack_m78 = 0;
    v_stack_m40 = 0;
    Arg3 = 0;
    v_stack_m68 = 0;
    Arg2 = 0;
    v_stack_m70 = 0;
    v_stack_m83 = 0;
    v_stack_m50 = v_xmm0;
    v_stack_m82 = 0;
    v_stack_m85 = 0;
    v_stack_m87 = 0;
    v_stack_m81 = 0;
    v_stack_m86 = 0;
    v_stack_m80 = 0;
    result = KeAbPreAcquire(v_rip + 10955567, Arg2, Arg3, Arg4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = v_rip + 10955567;
        Arg2 = result;
        Arg1 = v_rip + 10955567;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    result = 15;
    if ((*(uint32_t *)(v_rip + 0xA77F0C)) != 0) {
        Arg2 = 15;
        Arg1 = (uint8_t)(v_cr8);
        result = KiRaiseIrqlProcessIrqlFlags(Arg1, Arg2, Arg3, Arg4);
    }
    result = ExAcquireSpinLockExclusiveAtDpcLevel(v_rip + 10955449, Arg2, Arg3, Arg4);
loc_0054EE37:
    if ((*(uint64_t *)(v_rip + 0xA72A9D)) == (v_rip + 10955410)) goto loc_0054F001;
    result = IidAreIdsStrictlyEqual(*(uint64_t *)(*(uint64_t *)(v_rip + 0xA72A9D) + 0x10), v_stack_p8, Arg3, Arg4);
    if ((uint8_t)(result) != 0) goto loc_0054EE5C;
    goto loc_0054EE37;
loc_0054EE5C:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xA72A9D)) + 0x18) + 0x188)))) == ((uint32_t)((uint32_t)(Arg4)))) goto loc_0054EEBC;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xA72A9D)) + 0x18) + 0x188))) == 0) goto loc_0054EE86;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xA72A9D)) + 0x18) + 0x188))) - (1));
    if (condition_is_equal) goto loc_0054EEAD;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0054EEBC;
    if (((uint32_t)(Arg1)) != 1) goto loc_0054EE9C;
loc_0054EE86:
    result = (((uint32_t)((uint32_t)(Arg4))) != 1) ? 1 : 0;
    if (((uint32_t)((uint32_t)(Arg4))) != 2) goto loc_0054EE98;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xA72A9D)) + 0x18) + 0x184)))) != ((uint32_t)((uint32_t)(Arg4)))) goto loc_0054EE9C;
loc_0054EE98:
    if ((uint8_t)(result) != 0) goto loc_0054EEBC;
loc_0054EE9C:
loc_0054EEA1:
    goto loc_0054EF48;
loc_0054EEAD:
    if (0 != 2) goto loc_0054EE9C;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xA72A9D)) + 0x18) + 0x184)))) == 0) goto loc_0054EEBC;
    result = 0;
    goto loc_0054EE98;
loc_0054EEBC:
    result = IommupDeviceGetPasidSettings(v_stack_p18, v_stack_m83, v_stack_m82, v_stack_m81);
    if (sign_flag) goto loc_0054EEA1;
    if (v_stack_m82 != 0) goto loc_0054EEEB;
    if ((uint8_t)(v_stack_m83) == 0) goto loc_0054EEEF;
loc_0054EEEB:
    goto loc_0054EEF2;
loc_0054EEEF:
loc_0054EEF2:
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xA72A9D)) + 0x18) + 0x112)) != 0) goto loc_0054EE9C;
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xA72A9D)) + 0x18) + 0x111)) != ((uint8_t)(v_stack_m83))) goto loc_0054EE9C;
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xA72A9D)) + 0x18) + 0x110)) != ((uint8_t)(v_stack_m81))) goto loc_0054EE9C;
    local_rbx = 0;
    v_stack_m87 = 1;
    *(uint64_t *)(arg5) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xA72A9D)) + 0x18);
    if (v_stack_p10 == 0) goto loc_0054EF45;
    if (v_stack_p10 == (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xA72A9D)) + 0x18) + 0x8))) goto loc_0054EF45;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xA72A9D)) + 0x18) + 0x8) = v_stack_p10;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xA72A9D)) + 0x18) + 0x8) == 0) goto loc_0054EF48;
    v_stack_m80 = 1;
    goto loc_0054EF48;
loc_0054EF45:
loc_0054EF48:
    result = ExReleaseSpinLockExclusiveFromDpcLevel(v_rip + 10955153, 0, v_stack_m82, v_stack_m81);
    if ((*(uint32_t *)(v_rip + 0xA77DC6)) != 0) {
        Arg1 = 15;
        Arg2 = (uint8_t)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, v_stack_m82, v_stack_m81);
    }
    if (0 == 0) goto loc_0054EF97;
    result = ObfReferenceObjectWithTag(v_stack_p10, (uint32_t)((uint32_t)((uint32_t)(0x446C6148ULL))), v_stack_m82, v_stack_m81);
    if (v_stack_m80 != 0) {
        Arg2 = (uint32_t)((uint32_t)(0x446C6148ULL));
        Arg1 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xA72A9D)) + 0x18) + 0x8);
        result = ObfDereferenceObjectWithTag(Arg1, Arg2, v_stack_m82, v_stack_m81);
    }
    local_r13 = 0;
loc_0054EF9A:
    v_stack_m85 = (uint8_t)(v_stack_m85);
    if (!sign_flag) goto loc_0054F316;
    if (0 == 0) goto loc_0054F2E6;
loc_0054EFB9:
    result = v_stack_m85;
    if ((*(uint8_t *)(0 + 0x112)) != 0) {
        Arg1 = 0;
        result = IommupDeviceDisablePasidTaggedDma(Arg1, Arg2, v_stack_m82, v_stack_m81);
    }
    if (*(uint64_t *)(0 + 0x8) != 0) {
        Arg2 = 0x446C6148ULL;
        result = ObfDereferenceObjectWithTag(*(uint64_t *)(0 + 0x8), Arg2, v_stack_m82, v_stack_m81);
    }
    if ((uint8_t)(v_stack_m86) == 0) goto loc_0054F2DB;
    if ((*(uint8_t *)(v_rip + 0xA72723)) == 0) goto loc_0054F2C7;
    result = IommupHvUnregisterDeviceId(*(uint64_t *)(0 + 0x20), Arg2, v_stack_m82, v_stack_m81);
    goto loc_0054F2DB;
loc_0054F001:
    result = ExReleaseSpinLockExclusiveFromDpcLevel(v_rip + 10954968, Arg2, v_stack_m82, v_stack_m81);
    if ((*(uint32_t *)(v_rip + 0xA77D0C)) != 0) {
        Arg1 = (uint8_t)(v_cr8);
        Arg2 = (uint8_t)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, v_stack_m82, v_stack_m81);
    }
    result = HalpMmAllocCtxAlloc(Arg1, 40, v_stack_m82, v_stack_m81);
    if (result != 0) goto loc_0054F046;
    goto loc_0054F316;
loc_0054F046:
    *(uint64_t *)(result) = v_xmm0;
    result = 0;
    *(uint64_t *)(result + 0x10) = v_xmm0;
    *(uint64_t *)(result + 0x20) = 0;
    v_stack_m85 = 1;
    result = HalpIommuCloneDeviceId(v_stack_m87, result + 16, v_stack_m82, v_stack_m81);
    if (sign_flag) goto loc_0054EF9A;
    result = HalpMmAllocCtxAlloc(v_stack_m87, 424, v_stack_m82, v_stack_m81);
    if (result != 0) goto loc_0054F094;
    goto loc_0054F2F2;
loc_0054F094:
    Arg2 = 0;
    result = memset(result, Arg2, (uint32_t)(0xC000009AULL), v_stack_m81);
    *(uint64_t *)(result + 0x18) = result;
    *(uint32_t *)(result + 0x184) = (uint32_t)(v_stack_m86);
    *(uint32_t *)(result + 0x188) = (uint32_t)(v_stack_m86);
    *(uint64_t *)(result + 0x1A0) = 0;
    if ((*(uint8_t *)(v_rip + 0xA72668)) == 0) goto loc_0054F154;
    if ((*(uint32_t *)(v_stack_m87)) != 2) goto loc_0054F102;
    result = HalpIommuQueryAcpiDeviceMapping(v_stack_m87, v_stack_m50, (uint32_t)(0xC000009AULL), v_stack_m81);
    if (sign_flag) goto loc_0054EF9A;
    result = HalpIommuCloneDeviceId(v_stack_m50, v_stack_p8, (uint32_t)(0xC000009AULL), v_stack_m81);
    if (sign_flag) goto loc_0054EF9A;
    v_stack_m78 = v_stack_p8;
loc_0054F102:
    result = (uint32_t)((1) + (1));
    if (((int32_t)((uint32_t)(result))) <= result) goto loc_0054F132;
loc_0054F127:
    goto loc_0054EFB9;
loc_0054F132:
    result = guard_dispatch_icall(v_stack_p8, 0, (uint32_t)(0xC000009AULL), v_stack_m81);
    if (sign_flag) goto loc_0054F127;
    *(uint64_t *)(result + 0x20) = 0;
    goto loc_0054F1C5;
loc_0054F154:
    result = HalpIommuCreateDeviceInternal(0, result, v_stack_m70, v_stack_m68);
    if (sign_flag) goto loc_0054EF9A;
    *(uint64_t *)(result + 0x28) = v_stack_m70;
    *(uint64_t *)(result + 0x20) = v_stack_m68;
    result = *(uint64_t *)(v_stack_m68 + 0xD0);
    if (*(uint64_t *)(v_stack_m68 + 0xD0) != 0) {
        Arg1 = *(uint64_t *)(v_stack_m68 + 0x10);
        Arg4 = v_stack_m60;
        Arg3 = 1;
        Arg2 = 0;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
        result = v_stack_m60;
        *(uint64_t *)(result + 0x30) = result;
    }
    *(uint64_t *)(result + 0x40) = 0;
    result = ExWaitForRundownProtectionRelease(result + 64, Arg2, Arg3, Arg4);
loc_0054F1C5:
    v_stack_m86 = 1;
    if (v_stack_m78 != 0) goto loc_0054F1E5;
    result = HalpIommuCloneDeviceId(v_stack_p8, v_stack_m78, Arg3, Arg4);
    if (sign_flag) goto loc_0054EF9A;
loc_0054F1E5:
    *(uint64_t *)(result) = v_stack_m78;
    result = v_stack_m78;
    if (v_stack_p10 != 0) {
        Arg2 = 0x446C6148ULL;
        Arg1 = v_stack_p10;
        result = ObfReferenceObjectWithTag(Arg1, Arg2, Arg3, Arg4);
    }
    *(uint64_t *)(result + 0x8) = v_stack_p10;
    *(uint64_t *)(result + 0x168 + 0x8) = result + 360;
    *(uint64_t *)(result + 0x168) = result + 360;
    *(uint64_t *)(result + 0x178) = 0;
    result = IommupDeviceEnablePasidTaggedDma(result, v_stack_p18, Arg3, Arg4);
    if (sign_flag) goto loc_0054EF9A;
    result = HalpIommuCheckDpptException(v_stack_p8, v_stack_p18, Arg3, Arg4);
    *(uint8_t *)(result + 0x58) = (uint8_t)(result);
    *(uint32_t *)(result + 0x20) = 1;
    *(uint64_t *)(arg5) = result;
    result = Arg5;
    if ((*(uint32_t *)(v_rip + 0xA77AC5)) != 0) {
        Arg1 = (uint8_t)((uint8_t)(v_cr8));
        result = KiRaiseIrqlProcessIrqlFlags(Arg1, 15, Arg3, Arg4);
    }
    result = ExAcquireSpinLockExclusiveAtDpcLevel(v_rip + 10954356, 15, Arg3, Arg4);
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xA72660))) != (v_rip + 10954321)) {
        Arg1 = 3;
    }
    *(uint64_t *)(result) = Arg1;
    *(uint64_t *)(result + 0x8) = *(uint64_t *)(v_rip + 0xA72660);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0xA72660)) = result;
    *(uint64_t *)(v_rip + 0xA72635) = result;
    result = ExReleaseSpinLockExclusiveFromDpcLevel(v_rip + 10954315, 15, Arg3, Arg4);
    if ((*(uint32_t *)(v_rip + 0xA77A71)) != 0) {
        Arg1 = 15;
        Arg2 = (uint8_t)((uint8_t)(v_cr8));
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, Arg3, Arg4);
    }
    goto loc_0054F316;
loc_0054F2C7:
    Arg3 = 0;
    result = guard_dispatch_icall(*(uint64_t *)(Arg1 + 0x10), *(uint64_t *)((uint8_t)(v_cr8) + 0x28), Arg3, Arg4);
loc_0054F2DB:
    result = HalpMmAllocCtxFree(*(uint64_t *)(Arg1 + 0x10), (uint8_t)(v_cr8), Arg3, Arg4);
loc_0054F2E6:
    if (0 != 0) {
    }
    if ((uint8_t)(v_stack_m85) == 0) goto loc_0054F308;
loc_0054F2F2:
    result = v_stack_m85;
    if (*(uint64_t *)(result + 0x10) != 0) {
        result = HalpMmAllocCtxFree(*(uint64_t *)(Arg1 + 0x10), *(uint64_t *)(result + 0x10), Arg3, Arg4);
    }
    result = HalpMmAllocCtxFree(*(uint64_t *)(Arg1 + 0x10), result, Arg3, Arg4);
loc_0054F308:
    if (v_stack_m78 != 0) {
        result = HalpMmAllocCtxFree(*(uint64_t *)(Arg1 + 0x10), v_stack_m78, Arg3, Arg4);
    }
    result = (result) | (-1);
    result = (uint8_t)((result) & (6));
    if (((uint8_t)(result)) == 2) {
        Arg1 = v_rip + 10954128;
        result = ExfTryToWakePushLock(Arg1, v_stack_m78, Arg3, Arg4);
    }
    result = KeAbPostRelease(v_rip + 10954116, v_stack_m78, Arg3, Arg4);
    local_rsp = (local_rsp) + (128);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg5` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0054ED60&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
