# CmpCreateKeyControlBlock

- RVA: `0x00851DB0`–`0x00852766` (길이 `2,486` bytes)
- VA: `0x0000000140851DB0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00069E7C`
- 디코드: `595`개 명령, `2,486/2,486` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **54**; 고유 호출 대상: **36**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **8**

### Outgoing calls
- `0x00851E15` → [HvpGetCellContextInitialize](HvpGetCellContextInitialize_function_00855F10.md) (function, `0x00855F10`)
- `0x00851F85` → [ExAllocateFromLookasideListEx](../../text/3C/ExAllocateFromLookasideListEx_function_003CD390.md) (function, `0x003CD390`)
- `0x00851FA9` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00852051` → [CmpGetNameControlBlock](../84/CmpGetNameControlBlock_function_0084A750.md) (function, `0x0084A750`)
- `0x00852085` → [HvpGetCellFlat](HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x008520C3` → [HvpReleaseCellPaged](HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x008520D8` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x008520FA` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x00852121` → [HvpGetCellFlat](HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x0085215F` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x00852168` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00852201` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00852242` → [CmLockHiveSecurityShared](../../pagecmrc/BC/CmLockHiveSecurityShared_function_00BC996C.md) (function, `0x00BC996C`)
- `0x00852252` → [CmpFindSecurityCellCacheIndex](../../text/42/CmpFindSecurityCellCacheIndex_function_00428060.md) (function, `0x00428060`)
- `0x00852279` → [CmUnlockHiveSecurity](../../pagecmrc/BC/CmUnlockHiveSecurity_function_00BC99C8.md) (function, `0x00BC99C8`)
- `0x00852284` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (function, `0x00BC92C0`)
- `0x0085229F` → [HvpReleaseCellPaged](HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x008522D8` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00852369` → [CmpAttachToRegistryProcess](../../pagecmrc/BC/CmpAttachToRegistryProcess_function_00BC98E0.md) (function, `0x00BC98E0`)
- `0x00852371` → [CmpConstructName](CmpConstructName_function_00856BE0.md) (function, `0x00856BE0`)
- `0x008523A4` → [EtwpTraceRegistry](../86/EtwpTraceRegistry_function_00862980.md) (function, `0x00862980`)
- `0x008523B1` → [CmpFreePoolWithTag](../../text/44/CmpFreePoolWithTag_function_004489E0.md) (function, `0x004489E0`)
- `0x008523BA` → [CmpDetachFromRegistryProcess](../../pagecmrc/BC/CmpDetachFromRegistryProcess_function_00BC9920.md) (function, `0x00BC9920`)
- `0x008523CF` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x008523F0` → [HvpGetCellPaged](HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x008523FA` → [HvpGetCellPaged](HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x0085240A` → [HvpMarkCellDirty](HvpMarkCellDirty_function_00858080.md) (function, `0x00858080`)
- `0x008524BD` → [CmpLockKcbExclusive](../86/CmpLockKcbExclusive_function_00861EB0.md) (function, `0x00861EB0`)
- `0x008524C5` → [CmpTryToLockKcbExclusive](../9E/CmpTryToLockKcbExclusive_function_009E7B30.md) (function, `0x009E7B30`)
- `0x008524D9` → [CmpAllocateLayerInfoForKcb](CmpAllocateLayerInfoForKcb_function_0085CB90.md) (function, `0x0085CB90`)
- `0x008524EB` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (function, `0x00BC92C0`)
- `0x008524F3` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (function, `0x00BC92C0`)
- `0x00852501` → [CmUnlockHiveSecurity](../../pagecmrc/BC/CmUnlockHiveSecurity_function_00BC99C8.md) (function, `0x00BC99C8`)
- `0x00852509` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (function, `0x00BC92C0`)
- `0x00852528` → [HvpReleaseCellPaged](HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00852539` → [CmpDereferenceNameControlBlockWithLock](../86/CmpDereferenceNameControlBlockWithLock_function_00862840.md) (function, `0x00862840`)
- `0x00852548` → [CmpDereferenceKeyControlBlockUnsafe](../99/CmpDereferenceKeyControlBlockUnsafe_function_0099F960.md) (function, `0x0099F960`)
- `0x0085255B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0085256A` → [CmpFreeKeyControlBlock](../9D/CmpFreeKeyControlBlock_function_009DB7B0.md) (function, `0x009DB7B0`)
- `0x00852577` → [CmpAllocateLayerInfoForKcb](CmpAllocateLayerInfoForKcb_function_0085CB90.md) (function, `0x0085CB90`)
- `0x00852587` → [CmpReferenceKeyControlBlock](CmpReferenceKeyControlBlock_function_0085D370.md) (function, `0x0085D370`)
- `0x008525C2` → [HvpReleaseCellFlat](HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x008525E1` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x008525E7` → [HvpReleaseCellFlat](HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x008525F1` → [HvpReleaseCellFlat](HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x0085260C` → [RtlUpcaseUnicodeChar](RtlUpcaseUnicodeChar_function_0085F0F0.md) (function, `0x0085F0F0`)
- `0x00852638` → [KeAbPostReleaseEx](../../text/26/KeAbPostReleaseEx_function_00262210.md) (function, `0x00262210`)
- `0x00852663` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (function, `0x00BC92C0`)
- `0x0085266B` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (function, `0x00BC92C0`)
- `0x008526FC` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (function, `0x00BC92C0`)
- `0x00852704` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (function, `0x00BC92C0`)
- `0x00852713` → [RtlUpcaseUnicodeChar](RtlUpcaseUnicodeChar_function_0085F0F0.md) (function, `0x0085F0F0`)
- `0x0085272F` → [CmpReferenceKeyControlBlockLockNotHeld](../99/CmpReferenceKeyControlBlockLockNotHeld_function_0099F9A0.md) (function, `0x0099F9A0`)
- `0x0085275C` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [CmRenameKey](../7E/CmRenameKey_function_007E8F48.md) at `0x007E98AA`
- [CmpWalkOneLevel](CmpWalkOneLevel_function_00852BA0.md) at `0x008537A3`
- [CmpDoParseKey](CmpDoParseKey_function_0085F750.md) at `0x008615B8`
- [CmpCreateRegistryRoot](../../init/C5/CmpCreateRegistryRoot_function_00C57880.md) at `0x00C5797D`

### Static image references
- `0x00851DCC` → RVA `0x00E0A740` (`.data`; read)
- `0x00851F76` → RVA `0x00FDA430` (`PAGEDATA`; read/write)
- `0x00851F7E` → RVA `0x00E2CAC0` (`.data`; read)
- `0x00851F96` → RVA `0x00FDA450` (`PAGEDATA`; read/write)
- `0x008520A5` → RVA `0x00E0EC94` (`.data`; reference)
- `0x0085233F` → RVA `0x00FD8008` (`PAGEDATA`; read)
- `0x0085237E` → RVA `0x00862980` (`EtwpTraceRegistry`; read)
- `0x00852417` → RVA `0x00E0EC94` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **28**
  - `0x00851F85` → [ExAllocateFromLookasideListEx](../../text/3C/ExAllocateFromLookasideListEx_function_003CD390.md) (`PAGE` → `.text`)
  - `0x00851FA9` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x008520D8` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x008520FA` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x0085215F` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x00852168` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00852201` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x00852242` → [CmLockHiveSecurityShared](../../pagecmrc/BC/CmLockHiveSecurityShared_function_00BC996C.md) (`PAGE` → `PAGECMRC`)
  - `0x00852252` → [CmpFindSecurityCellCacheIndex](../../text/42/CmpFindSecurityCellCacheIndex_function_00428060.md) (`PAGE` → `.text`)
  - `0x00852279` → [CmUnlockHiveSecurity](../../pagecmrc/BC/CmUnlockHiveSecurity_function_00BC99C8.md) (`PAGE` → `PAGECMRC`)
  - `0x00852284` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (`PAGE` → `PAGECMRC`)
  - `0x008522D8` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x00852369` → [CmpAttachToRegistryProcess](../../pagecmrc/BC/CmpAttachToRegistryProcess_function_00BC98E0.md) (`PAGE` → `PAGECMRC`)
  - `0x008523B1` → [CmpFreePoolWithTag](../../text/44/CmpFreePoolWithTag_function_004489E0.md) (`PAGE` → `.text`)
  - `0x008523BA` → [CmpDetachFromRegistryProcess](../../pagecmrc/BC/CmpDetachFromRegistryProcess_function_00BC9920.md) (`PAGE` → `PAGECMRC`)
  - `0x008523CF` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x008524EB` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (`PAGE` → `PAGECMRC`)
  - `0x008524F3` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (`PAGE` → `PAGECMRC`)
  - `0x00852501` → [CmUnlockHiveSecurity](../../pagecmrc/BC/CmUnlockHiveSecurity_function_00BC99C8.md) (`PAGE` → `PAGECMRC`)
  - `0x00852509` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (`PAGE` → `PAGECMRC`)
  - `0x0085255B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008525E1` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x00852638` → [KeAbPostReleaseEx](../../text/26/KeAbPostReleaseEx_function_00262210.md) (`PAGE` → `.text`)
  - `0x00852663` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (`PAGE` → `PAGECMRC`)
  - `0x0085266B` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (`PAGE` → `PAGECMRC`)
  - `0x008526FC` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (`PAGE` → `PAGECMRC`)
  - `0x00852704` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (`PAGE` → `PAGECMRC`)
  - `0x0085275C` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00851DB0  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00851DB5  55                              push rbp
00851DB6  56                              push rsi
00851DB7  57                              push rdi
00851DB8  41 54                           push r12
00851DBA  41 55                           push r13
00851DBC  41 56                           push r14
00851DBE  41 57                           push r15
00851DC0  48 8D 6C 24 F9                  lea rbp, [rsp - 7]
00851DC5  48 81 EC E0 00 00 00            sub rsp, 0xe0
00851DCC  48 8B 05 6D 89 5B 00            mov rax, qword ptr [rip + 0x5b896d]
00851DD3  48 33 C4                        xor rax, rsp
00851DD6  48 89 45 FF                     mov qword ptr [rbp - 1], rax
00851DDA  48 8B 85 87 00 00 00            mov rax, qword ptr [rbp + 0x87]
00851DE1  4C 8B E9                        mov r13, rcx
00851DE4  8B 5D 7F                        mov ebx, dword ptr [rbp + 0x7f]
00851DE7  4D 8B F8                        mov r15, r8
00851DEA  48 89 4D 8F                     mov qword ptr [rbp - 0x71], rcx
00851DEE  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
00851DF3  4C 89 4D A7                     mov qword ptr [rbp - 0x59], r9
00851DF7  4C 8B 4D 6F                     mov r9, qword ptr [rbp + 0x6f]
00851DFB  4C 89 4C 24 58                  mov qword ptr [rsp + 0x58], r9
00851E00  4C 89 45 87                     mov qword ptr [rbp - 0x79], r8
00851E04  89 54 24 50                     mov dword ptr [rsp + 0x50], edx
00851E08  48 89 45 97                     mov qword ptr [rbp - 0x69], rax
00851E0C  48 C7 44 24 48 00 00 00 00      mov qword ptr [rsp + 0x48], 0
00851E15  E8 F6 40 00 00                  call 0x140855f10
00851E1A  41 8B 95 A0 00 00 00            mov edx, dword ptr [r13 + 0xa0]
00851E21  F6 C2 20                        test dl, 0x20
00851E24  74 16                           je 0x140851e3c
00851E26  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00851E2F  49 39 85 48 10 00 00            cmp qword ptr [r13 + 0x1048], rax
00851E36  0F 85 F4 04 00 00               jne 0x140852330
00851E3C  8B C3                           mov eax, ebx
00851E3E  41 B8 E0 FF 00 00               mov r8d, 0xffe0
00851E44  C1 E8 09                        shr eax, 9
00851E47  33 C3                           xor eax, ebx
00851E49  69 C0 A3 8A 01 00               imul eax, eax, 0x18aa3
00851E4F  45 8D 50 1F                     lea r10d, [r8 + 0x1f]
00851E53  8B C8                           mov ecx, eax
00851E55  8B D0                           mov edx, eax
00851E57  49 8B 85 70 06 00 00            mov rax, qword ptr [r13 + 0x670]
00851E5E  48 C1 EA 09                     shr rdx, 9
00851E62  48 33 D1                        xor rdx, rcx
00851E65  41 8B 8D 78 06 00 00            mov ecx, dword ptr [r13 + 0x678]
00851E6C  FF C9                           dec ecx
00851E6E  48 23 D1                        and rdx, rcx
00851E71  48 8D 0C 52                     lea rcx, [rdx + rdx*2]
00851E75  4C 8B 74 C8 10                  mov r14, qword ptr [rax + rcx*8 + 0x10]
00851E7A  4D 85 F6                        test r14, r14
00851E7D  0F 84 9E 00 00 00               je 0x140851f21
00851E83  41 39 1E                        cmp dword ptr [r14], ebx
00851E86  0F 85 6F 04 00 00               jne 0x1408522fb
00851E8C  4D 39 7E 38                     cmp qword ptr [r14 + 0x38], r15
00851E90  4D 8D 6E F0                     lea r13, [r14 - 0x10]
00851E94  0F 85 61 04 00 00               jne 0x1408522fb
00851E9A  49 8B 4D 50                     mov rcx, qword ptr [r13 + 0x50]
00851E9E  41 0F B7 39                     movzx edi, word ptr [r9]
00851EA2  66 D1 EF                        shr di, 1
00851EA5  8B 01                           mov eax, dword ptr [rcx]
00851EA7  4C 8D 61 1A                     lea r12, [rcx + 0x1a]
00851EAB  0F B7 71 18                     movzx esi, word ptr [rcx + 0x18]
00851EAF  A8 01                           test al, 1
00851EB1  0F 84 DA 07 00 00               je 0x140852691
00851EB7  4D 8B 79 08                     mov r15, qword ptr [r9 + 8]
00851EBB  66 85 FF                        test di, di
00851EBE  74 46                           je 0x140851f06
00851EC0  66 85 F6                        test si, si
00851EC3  74 41                           je 0x140851f06
00851EC5  41 0F B6 04 24                  movzx eax, byte ptr [r12]
00851ECA  49 FF C4                        inc r12
00851ECD  41 0F B7 0F                     movzx ecx, word ptr [r15]
00851ED1  49 83 C7 02                     add r15, 2
00851ED5  66 89 44 24 40                  mov word ptr [rsp + 0x40], ax
00851EDA  66 3B C8                        cmp cx, ax
00851EDD  74 1D                           je 0x140851efc
00851EDF  66 83 F9 61                     cmp cx, 0x61
00851EE3  72 0E                           jb 0x140851ef3
00851EE5  66 83 F9 7A                     cmp cx, 0x7a
00851EE9  0F 87 1D 07 00 00               ja 0x14085260c
00851EEF  66 41 03 C8                     add cx, r8w
00851EF3  66 3B C8                        cmp cx, ax
00851EF6  0F 85 F6 03 00 00               jne 0x1408522f2
00851EFC  66 41 03 FA                     add di, r10w
00851F00  66 41 03 F2                     add si, r10w
00851F04  EB B5                           jmp 0x140851ebb
00851F06  4C 8B 7D 87                     mov r15, qword ptr [rbp - 0x79]
00851F0A  66 3B FE                        cmp di, si
00851F0D  0F 85 E3 03 00 00               jne 0x1408522f6
00851F13  4D 85 ED                        test r13, r13
00851F16  0F 85 10 08 00 00               jne 0x14085272c
00851F1C  4C 8B 4C 24 58                  mov r9, qword ptr [rsp + 0x58]
00851F21  33 F6                           xor esi, esi
00851F23  49 8B C7                        mov rax, r15
00851F26  8B D6                           mov edx, esi
00851F28  4D 85 FF                        test r15, r15
00851F2B  74 37                           je 0x140851f64
00851F2D  0F 1F 00                        nop dword ptr [rax]
00851F30  F7 80 B8 00 00 00 00 00 04 00   test dword ptr [rax + 0xb8], 0x40000
00851F3A  4C 8D 40 48                     lea r8, [rax + 0x48]
00851F3E  0F 85 9A 03 00 00               jne 0x1408522de
00851F44  48 8B 40 50                     mov rax, qword ptr [rax + 0x50]
00851F48  0F B7 48 18                     movzx ecx, word ptr [rax + 0x18]
00851F4C  8B 00                           mov eax, dword ptr [rax]
00851F4E  A8 01                           test al, 1
00851F50  0F 84 AE 03 00 00               je 0x140852304
00851F56  8D 14 4A                        lea edx, [rdx + rcx*2]
00851F59  49 8B 00                        mov rax, qword ptr [r8]
00851F5C  83 C2 02                        add edx, 2
00851F5F  48 85 C0                        test rax, rax
00851F62  75 CC                           jne 0x140851f30
00851F64  41 0F B7 01                     movzx eax, word ptr [r9]
00851F68  8D 4A 02                        lea ecx, [rdx + 2]
00851F6B  03 C8                           add ecx, eax
00851F6D  41 3B CA                        cmp ecx, r10d
00851F70  0F 87 CC 07 00 00               ja 0x140852742
00851F76  F0 48 FF 05 B2 84 78 00         lock inc qword ptr [rip + 0x7884b2]
00851F7E  48 8D 0D 3B AB 5D 00            lea rcx, [rip + 0x5dab3b]
00851F85  E8 06 B4 B7 FF                  call 0x1403cd390
00851F8A  48 8B F8                        mov rdi, rax
00851F8D  48 85 C0                        test rax, rax
00851F90  0F 84 F1 06 00 00               je 0x140852687
00851F96  F0 48 FF 05 B2 84 78 00         lock inc qword ptr [rip + 0x7884b2]
00851F9E  33 D2                           xor edx, edx
00851FA0  41 B8 38 01 00 00               mov r8d, 0x138
00851FA6  48 8B C8                        mov rcx, rax
00851FA9  E8 92 4C E7 FF                  call 0x1406c6c40
00851FAE  8B 44 24 50                     mov eax, dword ptr [rsp + 0x50]
00851FB2  48 8D 4F 78                     lea rcx, [rdi + 0x78]
00851FB6  4C 8B 6D 8F                     mov r13, qword ptr [rbp - 0x71]
00851FBA  48 8D 55 77                     lea rdx, [rbp + 0x77]
00851FBE  48 89 49 08                     mov qword ptr [rcx + 8], rcx
00851FC2  41 BE 01 00 00 00               mov r14d, 1
00851FC8  48 89 09                        mov qword ptr [rcx], rcx
00851FCB  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00851FD0  48 89 B7 88 00 00 00            mov qword ptr [rdi + 0x88], rsi
00851FD7  48 89 B7 90 00 00 00            mov qword ptr [rdi + 0x90], rsi
00851FDE  48 89 B7 98 00 00 00            mov qword ptr [rdi + 0x98], rsi
00851FE5  48 89 B7 A0 00 00 00            mov qword ptr [rdi + 0xa0], rsi
00851FEC  89 47 28                        mov dword ptr [rdi + 0x28], eax
00851FEF  48 8D 87 D0 00 00 00            lea rax, [rdi + 0xd0]
00851FF6  4C 89 37                        mov qword ptr [rdi], r14
00851FF9  4C 89 6F 20                     mov qword ptr [rdi + 0x20], r13
00851FFD  89 5F 10                        mov dword ptr [rdi + 0x10], ebx
00852000  48 89 77 30                     mov qword ptr [rdi + 0x30], rsi
00852004  48 89 40 08                     mov qword ptr [rax + 8], rax
00852008  48 89 00                        mov qword ptr [rax], rax
0085200B  48 8D 87 E0 00 00 00            lea rax, [rdi + 0xe0]
00852012  48 89 40 08                     mov qword ptr [rax + 8], rax
00852016  48 89 00                        mov qword ptr [rax], rax
00852019  48 89 B7 F0 00 00 00            mov qword ptr [rdi + 0xf0], rsi
00852020  89 B7 F8 00 00 00               mov dword ptr [rdi + 0xf8], esi
00852026  48 89 B7 00 01 00 00            mov qword ptr [rdi + 0x100], rsi
0085202D  89 B7 08 01 00 00               mov dword ptr [rdi + 0x108], esi
00852033  48 89 B7 10 01 00 00            mov qword ptr [rdi + 0x110], rsi
0085203A  89 B7 18 01 00 00               mov dword ptr [rdi + 0x118], esi
00852040  C7 87 1C 01 00 00 FF FF FF FF   mov dword ptr [rdi + 0x11c], 0xffffffff
0085204A  48 89 B7 20 01 00 00            mov qword ptr [rdi + 0x120], rsi
00852051  E8 FA 86 FF FF                  call 0x14084a750
00852056  48 89 47 50                     mov qword ptr [rdi + 0x50], rax
0085205A  48 85 C0                        test rax, rax
0085205D  0F 84 E9 06 00 00               je 0x14085274c
00852063  8B 57 28                        mov edx, dword ptr [rdi + 0x28]
00852066  83 FA FF                        cmp edx, -1
00852069  0F 84 9C 02 00 00               je 0x14085230b
0085206F  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
00852073  4C 8D 44 24 48                  lea r8, [rsp + 0x48]
00852078  44 84 B1 8C 00 00 00            test byte ptr [rcx + 0x8c], r14b
0085207F  0F 84 6B 03 00 00               je 0x1408523f0
00852085  E8 D6 2B 00 00                  call 0x140854c60
0085208A  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
0085208E  48 8B D8                        mov rbx, rax
00852091  F7 81 A0 00 00 00 01 80 00 00   test dword ptr [rcx + 0xa0], 0x8001
0085209B  0F 85 D0 00 00 00               jne 0x140852171
008520A1  0F B6 40 0C                     movzx eax, byte ptr [rax + 0xc]
008520A5  84 05 E9 CB 5B 00               test byte ptr [rip + 0x5bcbe9], al
008520AB  0F 85 C0 00 00 00               jne 0x140852171
008520B1  48 8D 54 24 48                  lea rdx, [rsp + 0x48]
008520B6  44 84 B1 8C 00 00 00            test byte ptr [rcx + 0x8c], r14b
008520BD  0F 85 2E 05 00 00               jne 0x1408525f1
008520C3  E8 78 3E 00 00                  call 0x140855f40
008520C8  48 8B 5F 20                     mov rbx, qword ptr [rdi + 0x20]
008520CC  45 33 C0                        xor r8d, r8d
008520CF  48 83 C3 48                     add rbx, 0x48
008520D3  33 D2                           xor edx, edx
008520D5  48 8B CB                        mov rcx, rbx
008520D8  E8 53 E1 9B FF                  call 0x140210230
008520DD  4C 8B F8                        mov r15, rax
008520E0  41 BC 11 00 00 00               mov r12d, 0x11
008520E6  33 C0                           xor eax, eax
008520E8  F0 4C 0F B1 23                  lock cmpxchg qword ptr [rbx], r12
008520ED  74 10                           je 0x1408520ff
008520EF  4C 8B CB                        mov r9, rbx
008520F2  4D 8B C7                        mov r8, r15
008520F5  33 D2                           xor edx, edx
008520F7  48 8B CB                        mov rcx, rbx
008520FA  E8 4D E3 9B FF                  call 0x14021044c
008520FF  4D 85 FF                        test r15, r15
00852102  74 04                           je 0x140852108
00852104  45 88 77 0A                     mov byte ptr [r15 + 0xa], r14b
00852108  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
0085210C  4C 8D 44 24 48                  lea r8, [rsp + 0x48]
00852111  8B 57 28                        mov edx, dword ptr [rdi + 0x28]
00852114  44 84 B1 8C 00 00 00            test byte ptr [rcx + 0x8c], r14b
0085211B  0F 84 D9 02 00 00               je 0x1408523fa
00852121  E8 3A 2B 00 00                  call 0x140854c60
00852126  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
0085212A  48 8B D8                        mov rbx, rax
0085212D  8B 57 28                        mov edx, dword ptr [rdi + 0x28]
00852130  F7 81 A0 00 00 00 01 80 00 00   test dword ptr [rcx + 0xa0], 0x8001
0085213A  75 10                           jne 0x14085214c
0085213C  0F B6 40 0C                     movzx eax, byte ptr [rax + 0xc]
00852140  84 05 4E CB 5B 00               test byte ptr [rip + 0x5bcb4e], al
00852146  0F 84 B8 02 00 00               je 0x140852404
0085214C  4C 8B 7F 20                     mov r15, qword ptr [rdi + 0x20]
00852150  49 8B C4                        mov rax, r12
00852153  F0 49 0F B1 77 48               lock cmpxchg qword ptr [r15 + 0x48], rsi
00852159  74 09                           je 0x140852164
0085215B  49 8D 4F 48                     lea rcx, [r15 + 0x48]
0085215F  E8 DC 12 A1 FF                  call 0x140263440
00852164  49 8D 4F 48                     lea rcx, [r15 + 0x48]
00852168  E8 93 F4 A8 FF                  call 0x1402e1600
0085216D  4C 8B 7D 87                     mov r15, qword ptr [rbp - 0x79]
00852171  0F B6 43 0D                     movzx eax, byte ptr [rbx + 0xd]
00852175  45 8B C6                        mov r8d, r14d
00852178  24 03                           and al, 3
0085217A  33 D2                           xor edx, edx
0085217C  88 47 41                        mov byte ptr [rdi + 0x41], al
0085217F  8B 43 24                        mov eax, dword ptr [rbx + 0x24]
00852182  8B 4B 28                        mov ecx, dword ptr [rbx + 0x28]
00852185  89 47 60                        mov dword ptr [rdi + 0x60], eax
00852188  89 4F 64                        mov dword ptr [rdi + 0x64], ecx
0085218B  0F B7 43 02                     movzx eax, word ptr [rbx + 2]
0085218F  66 89 87 BA 00 00 00            mov word ptr [rdi + 0xba], ax
00852196  8B 43 18                        mov eax, dword ptr [rbx + 0x18]
00852199  03 43 14                        add eax, dword ptr [rbx + 0x14]
0085219C  89 47 70                        mov dword ptr [rdi + 0x70], eax
0085219F  48 8B 43 04                     mov rax, qword ptr [rbx + 4]
008521A3  48 89 87 A8 00 00 00            mov qword ptr [rdi + 0xa8], rax
008521AA  0F B7 43 34                     movzx eax, word ptr [rbx + 0x34]
008521AE  66 89 87 B0 00 00 00            mov word ptr [rdi + 0xb0], ax
008521B5  0F B7 43 3C                     movzx eax, word ptr [rbx + 0x3c]
008521B9  66 89 87 B2 00 00 00            mov word ptr [rdi + 0xb2], ax
008521C0  8B 43 40                        mov eax, dword ptr [rbx + 0x40]
008521C3  89 87 B4 00 00 00               mov dword ptr [rdi + 0xb4], eax
008521C9  8B 87 B8 00 00 00               mov eax, dword ptr [rdi + 0xb8]
008521CF  0F B7 4B 36                     movzx ecx, word ptr [rbx + 0x36]
008521D3  33 C8                           xor ecx, eax
008521D5  83 E1 0F                        and ecx, 0xf
008521D8  33 C8                           xor ecx, eax
008521DA  89 8F B8 00 00 00               mov dword ptr [rdi + 0xb8], ecx
008521E0  0F B7 43 36                     movzx eax, word ptr [rbx + 0x36]
008521E4  33 C1                           xor eax, ecx
008521E6  25 F0 00 00 00                  and eax, 0xf0
008521EB  33 C1                           xor eax, ecx
008521ED  48 8D 4F 30                     lea rcx, [rdi + 0x30]
008521F1  89 87 B8 00 00 00               mov dword ptr [rdi + 0xb8], eax
008521F7  0F B6 43 37                     movzx eax, byte ptr [rbx + 0x37]
008521FB  88 87 B9 00 00 00               mov byte ptr [rdi + 0xb9], al
00852201  E8 2A E0 9B FF                  call 0x140210230
00852206  F0 48 0F BA 6F 30 00            lock bts qword ptr [rdi + 0x30], 0
0085220D  0F 82 15 04 00 00               jb 0x140852628
00852213  48 85 C0                        test rax, rax
00852216  74 04                           je 0x14085221c
00852218  44 88 70 0A                     mov byte ptr [rax + 0xa], r14b
0085221C  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00852225  48 89 47 38                     mov qword ptr [rdi + 0x38], rax
00852229  44 8B 63 2C                     mov r12d, dword ptr [rbx + 0x2c]
0085222D  89 74 24 50                     mov dword ptr [rsp + 0x50], esi
00852231  41 83 FC FF                     cmp r12d, -1
00852235  0F 84 43 04 00 00               je 0x14085267e
0085223B  48 8B 5F 20                     mov rbx, qword ptr [rdi + 0x20]
0085223F  48 8B CB                        mov rcx, rbx
00852242  E8 25 77 37 00                  call 0x140bc996c
00852247  4C 8D 44 24 50                  lea r8, [rsp + 0x50]
0085224C  41 8B D4                        mov edx, r12d
0085224F  48 8B CB                        mov rcx, rbx
00852252  E8 09 5E BD FF                  call 0x140428060
00852257  84 C0                           test al, al
00852259  0F 84 9B 02 00 00               je 0x1408524fa
0085225F  48 8B 83 60 07 00 00            mov rax, qword ptr [rbx + 0x760]
00852266  8B 4C 24 50                     mov ecx, dword ptr [rsp + 0x50]
0085226A  48 03 C9                        add rcx, rcx
0085226D  48 8B 4C C8 08                  mov rcx, qword ptr [rax + rcx*8 + 8]
00852272  48 89 4F 58                     mov qword ptr [rdi + 0x58], rcx
00852276  48 8B CB                        mov rcx, rbx
00852279  E8 4A 77 37 00                  call 0x140bc99c8
0085227E  48 8B CF                        mov rcx, rdi
00852281  48 8B DF                        mov rbx, rdi
00852284  E8 37 70 37 00                  call 0x140bc92c0
00852289  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
0085228D  48 8D 54 24 48                  lea rdx, [rsp + 0x48]
00852292  44 84 B1 8C 00 00 00            test byte ptr [rcx + 0x8c], r14b
00852299  0F 85 48 03 00 00               jne 0x1408525e7
0085229F  E8 9C 3C 00 00                  call 0x140855f40
008522A4  4D 85 FF                        test r15, r15
008522A7  0F 84 4E 03 00 00               je 0x1408525fb
008522AD  F0 4D 0F C1 37                  lock xadd qword ptr [r15], r14
008522B2  49 83 C6 01                     add r14, 1
008522B6  0F 84 13 03 00 00               je 0x1408525cf
008522BC  49 83 FE 01                     cmp r14, 1
008522C0  0F 85 60 01 00 00               jne 0x140852426
008522C6  41 8D 56 14                     lea edx, [r14 + 0x14]
008522CA  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
008522CF  8D 4A 3C                        lea ecx, [rdx + 0x3c]
008522D2  45 33 C9                        xor r9d, r9d
008522D5  45 33 C0                        xor r8d, r8d
008522D8  E8 83 B3 CA FF                  call 0x1404fd660
008522DD  CC                              int3
008522DE  49 8B 08                        mov rcx, qword ptr [r8]
008522E1  48 85 C9                        test rcx, rcx
008522E4  0F 84 5A FC FF FF               je 0x140851f44
008522EA  48 8B C1                        mov rax, rcx
008522ED  E9 3E FC FF FF                  jmp 0x140851f30
008522F2  4C 8B 7D 87                     mov r15, qword ptr [rbp - 0x79]
008522F6  4C 8B 4C 24 58                  mov r9, qword ptr [rsp + 0x58]
008522FB  4D 8B 76 08                     mov r14, qword ptr [r14 + 8]
008522FF  E9 76 FB FF FF                  jmp 0x140851e7a
00852304  03 D1                           add edx, ecx
00852306  E9 4E FC FF FF                  jmp 0x140851f59
0085230B  41 0F B6 47 41                  movzx eax, byte ptr [r15 + 0x41]
00852310  FE C8                           dec al
00852312  A8 FD                           test al, 0xfd
00852314  0F 84 5B 03 00 00               je 0x140852675
0085231A  48 8B DF                        mov rbx, rdi
0085231D  44 84 75 67                     test byte ptr [rbp + 0x67], r14b
00852321  74 81                           je 0x1408522a4
00852323  66 83 8F BA 00 00 00 04         or word ptr [rdi + 0xba], 4
0085232B  E9 74 FF FF FF                  jmp 0x1408522a4
00852330  BE 34 00 00 C0                  mov esi, 0xc0000034
00852335  E9 8C 00 00 00                  jmp 0x1408523c6
0085233A  66 83 4F 08 20                  or word ptr [rdi + 8], 0x20
0085233F  48 8B 1D C2 5C 78 00            mov rbx, qword ptr [rip + 0x785cc2]
00852346  48 85 DB                        test rbx, rbx
00852349  74 74                           je 0x1408523bf
0085234B  0F 57 C9                        xorps xmm1, xmm1
0085234E  48 8D 4D CF                     lea rcx, [rbp - 0x31]
00852352  0F 57 C0                        xorps xmm0, xmm0
00852355  0F 11 45 AF                     movups xmmword ptr [rbp - 0x51], xmm0
00852359  0F 11 45 BF                     movups xmmword ptr [rbp - 0x41], xmm0
0085235D  0F 11 4D CF                     movups xmmword ptr [rbp - 0x31], xmm1
00852361  0F 11 4D DF                     movups xmmword ptr [rbp - 0x21], xmm1
00852365  0F 11 4D EF                     movups xmmword ptr [rbp - 0x11], xmm1
00852369  E8 72 75 37 00                  call 0x140bc98e0
0085236E  48 8B CF                        mov rcx, rdi
00852371  E8 6A 48 00 00                  call 0x140856be0
00852376  4C 8B F0                        mov r14, rax
00852379  48 85 C0                        test rax, rax
0085237C  74 38                           je 0x1408523b6
0085237E  48 8D 05 FB 05 01 00            lea rax, [rip + 0x105fb]
00852385  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
0085238A  45 33 C9                        xor r9d, r9d
0085238D  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00852392  45 33 C0                        xor r8d, r8d
00852395  48 8D 55 AF                     lea rdx, [rbp - 0x51]
00852399  B1 16                           mov cl, 0x16
0085239B  48 3B D8                        cmp rbx, rax
0085239E  0F 85 B5 03 00 00               jne 0x140852759
008523A4  E8 D7 05 01 00                  call 0x140862980
008523A9  BA 43 4D 4E 62                  mov edx, 0x624e4d43
008523AE  49 8B CE                        mov rcx, r14
008523B1  E8 2A 66 BF FF                  call 0x1404489e0
008523B6  48 8D 4D CF                     lea rcx, [rbp - 0x31]
008523BA  E8 61 75 37 00                  call 0x140bc9920
008523BF  48 8B 45 97                     mov rax, qword ptr [rbp - 0x69]
008523C3  48 89 38                        mov qword ptr [rax], rdi
008523C6  8B C6                           mov eax, esi
008523C8  48 8B 4D FF                     mov rcx, qword ptr [rbp - 1]
008523CC  48 33 CC                        xor rcx, rsp
008523CF  E8 6C A2 E5 FF                  call 0x1406ac640
008523D4  48 8B 9C 24 28 01 00 00         mov rbx, qword ptr [rsp + 0x128]
008523DC  48 81 C4 E0 00 00 00            add rsp, 0xe0
008523E3  41 5F                           pop r15
008523E5  41 5E                           pop r14
008523E7  41 5D                           pop r13
008523E9  41 5C                           pop r12
008523EB  5F                              pop rdi
008523EC  5E                              pop rsi
008523ED  5D                              pop rbp
008523EE  C3                              ret
008523EF  CC                              int3
008523F0  E8 BB 28 00 00                  call 0x140854cb0
008523F5  E9 90 FC FF FF                  jmp 0x14085208a
008523FA  E8 B1 28 00 00                  call 0x140854cb0
008523FF  E9 22 FD FF FF                  jmp 0x140852126
00852404  45 8B CE                        mov r9d, r14d
00852407  45 33 C0                        xor r8d, r8d
0085240A  E8 71 5C 00 00                  call 0x140858080
0085240F  85 C0                           test eax, eax
00852411  0F 88 35 FD FF FF               js 0x14085214c
00852417  0F B6 0D 76 C8 5B 00            movzx ecx, byte ptr [rip + 0x5bc876]
0085241E  08 4B 0C                        or byte ptr [rbx + 0xc], cl
00852421  E9 26 FD FF FF                  jmp 0x14085214c
00852426  F7 87 B8 00 00 00 00 00 04 00   test dword ptr [rdi + 0xb8], 0x40000
00852430  8B 4F 08                        mov ecx, dword ptr [rdi + 8]
00852433  4C 89 7F 48                     mov qword ptr [rdi + 0x48], r15
00852437  41 8B 57 08                     mov edx, dword ptr [r15 + 8]
0085243B  0F 85 01 02 00 00               jne 0x140852642
00852441  8D 82 00 00 20 00               lea eax, [rdx + 0x200000]
00852447  33 C1                           xor eax, ecx
00852449  25 00 00 E0 7F                  and eax, 0x7fe00000
0085244E  33 C1                           xor eax, ecx
00852450  4C 8B 75 A7                     mov r14, qword ptr [rbp - 0x59]
00852454  89 47 08                        mov dword ptr [rdi + 8], eax
00852457  4D 85 F6                        test r14, r14
0085245A  75 5E                           jne 0x1408524ba
0085245C  8B 47 10                        mov eax, dword ptr [rdi + 0x10]
0085245F  8B C8                           mov ecx, eax
00852461  4C 8B 47 20                     mov r8, qword ptr [rdi + 0x20]
00852465  C1 E9 09                        shr ecx, 9
00852468  33 C8                           xor ecx, eax
0085246A  69 C1 A3 8A 01 00               imul eax, ecx, 0x18aa3
00852470  8B C8                           mov ecx, eax
00852472  8B D0                           mov edx, eax
00852474  49 8B 80 70 06 00 00            mov rax, qword ptr [r8 + 0x670]
0085247B  48 C1 EA 09                     shr rdx, 9
0085247F  48 33 D1                        xor rdx, rcx
00852482  41 8B 88 78 06 00 00            mov ecx, dword ptr [r8 + 0x678]
00852489  FF C9                           dec ecx
0085248B  48 23 D1                        and rdx, rcx
0085248E  48 8D 0C 52                     lea rcx, [rdx + rdx*2]
00852492  48 8D 14 C8                     lea rdx, [rax + rcx*8]
00852496  48 8B 44 C8 10                  mov rax, qword ptr [rax + rcx*8 + 0x10]
0085249B  48 89 47 18                     mov qword ptr [rdi + 0x18], rax
0085249F  48 8D 47 10                     lea rax, [rdi + 0x10]
008524A3  48 89 42 10                     mov qword ptr [rdx + 0x10], rax
008524A7  41 80 BD 80 0B 00 00 01         cmp byte ptr [r13 + 0xb80], 1
008524AF  0F 84 85 FE FF FF               je 0x14085233a
008524B5  E9 85 FE FF FF                  jmp 0x14085233f
008524BA  49 8B CE                        mov rcx, r14
008524BD  E8 EE F9 00 00                  call 0x140861eb0
008524C2  48 8B CF                        mov rcx, rdi
008524C5  E8 66 56 19 00                  call 0x1409e7b30
008524CA  66 41 83 7E 42 7F               cmp word ptr [r14 + 0x42], 0x7f
008524D0  0F 8D 23 02 00 00               jge 0x1408526f9
008524D6  49 8B CE                        mov rcx, r14
008524D9  E8 B2 A6 00 00                  call 0x14085cb90
008524DE  85 C0                           test eax, eax
008524E0  0F 89 8E 00 00 00               jns 0x140852574
008524E6  48 8B CF                        mov rcx, rdi
008524E9  8B F0                           mov esi, eax
008524EB  E8 D0 6D 37 00                  call 0x140bc92c0
008524F0  49 8B CE                        mov rcx, r14
008524F3  E8 C8 6D 37 00                  call 0x140bc92c0
008524F8  EB 36                           jmp 0x140852530
008524FA  48 8B CB                        mov rcx, rbx
008524FD  48 89 77 58                     mov qword ptr [rdi + 0x58], rsi
00852501  E8 C2 74 37 00                  call 0x140bc99c8
00852506  48 8B CF                        mov rcx, rdi
00852509  E8 B2 6D 37 00                  call 0x140bc92c0
0085250E  BE 9A 00 00 C0                  mov esi, 0xc000009a
00852513  48 8D 54 24 48                  lea rdx, [rsp + 0x48]
00852518  49 8B CD                        mov rcx, r13
0085251B  45 84 B5 8C 00 00 00            test byte ptr [r13 + 0x8c], r14b
00852522  0F 85 9A 00 00 00               jne 0x1408525c2
00852528  E8 13 3A 00 00                  call 0x140855f40
0085252D  48 8B DF                        mov rbx, rdi
00852530  48 8B 4B 50                     mov rcx, qword ptr [rbx + 0x50]
00852534  48 85 C9                        test rcx, rcx
00852537  74 05                           je 0x14085253e
00852539  E8 02 03 01 00                  call 0x140862840
0085253E  48 83 7B 48 00                  cmp qword ptr [rbx + 0x48], 0
00852543  74 08                           je 0x14085254d
00852545  49 8B CF                        mov rcx, r15
00852548  E8 13 D4 14 00                  call 0x14099f960
0085254D  48 8B 8B C0 00 00 00            mov rcx, qword ptr [rbx + 0xc0]
00852554  48 85 C9                        test rcx, rcx
00852557  74 07                           je 0x140852560
00852559  33 D2                           xor edx, edx
0085255B  E8 10 03 33 00                  call 0x140b82870
00852560  81 4B 08 00 00 08 00            or dword ptr [rbx + 8], 0x80000
00852567  48 8B CB                        mov rcx, rbx
0085256A  E8 41 92 18 00                  call 0x1409db7b0
0085256F  E9 52 FE FF FF                  jmp 0x1408523c6
00852574  48 8B CF                        mov rcx, rdi
00852577  E8 14 A6 00 00                  call 0x14085cb90
0085257C  85 C0                           test eax, eax
0085257E  0F 88 62 FF FF FF               js 0x1408524e6
00852584  49 8B CE                        mov rcx, r14
00852587  E8 E4 AD 00 00                  call 0x14085d370
0085258C  41 0F B7 46 42                  movzx eax, word ptr [r14 + 0x42]
00852591  48 8B 8F C0 00 00 00            mov rcx, qword ptr [rdi + 0xc0]
00852598  66 FF C0                        inc ax
0085259B  66 89 47 42                     mov word ptr [rdi + 0x42], ax
0085259F  49 8B 86 C0 00 00 00            mov rax, qword ptr [r14 + 0xc0]
008525A6  48 89 41 18                     mov qword ptr [rcx + 0x18], rax
008525AA  48 83 C0 20                     add rax, 0x20
008525AE  48 8B 50 08                     mov rdx, qword ptr [rax + 8]
008525B2  48 39 02                        cmp qword ptr [rdx], rax
008525B5  0F 84 97 00 00 00               je 0x140852652
008525BB  B9 03 00 00 00                  mov ecx, 3
008525C0  CD 29                           int 0x29
008525C2  E8 59 A6 00 00                  call 0x14085cc20
008525C7  48 8B DF                        mov rbx, rdi
008525CA  E9 61 FF FF FF                  jmp 0x140852530
008525CF  45 33 C9                        xor r9d, r9d
008525D2  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
008525D7  4D 8B C7                        mov r8, r15
008525DA  41 8D 51 24                     lea edx, [r9 + 0x24]
008525DE  8D 4A 2D                        lea ecx, [rdx + 0x2d]
008525E1  E8 7A B0 CA FF                  call 0x1404fd660
008525E6  CC                              int3
008525E7  E8 34 A6 00 00                  call 0x14085cc20
008525EC  E9 B3 FC FF FF                  jmp 0x1408522a4
008525F1  E8 2A A6 00 00                  call 0x14085cc20
008525F6  E9 CD FA FF FF                  jmp 0x1408520c8
008525FB  8B 47 08                        mov eax, dword ptr [rdi + 8]
008525FE  25 FF FF 3F 80                  and eax, 0x803fffff
00852603  0F BA E8 15                     bts eax, 0x15
00852607  E9 44 FE FF FF                  jmp 0x140852450
0085260C  E8 DF CA 00 00                  call 0x14085f0f0
00852611  41 BA FF FF 00 00               mov r10d, 0xffff
00852617  0F B7 C8                        movzx ecx, ax
0085261A  0F B7 44 24 40                  movzx eax, word ptr [rsp + 0x40]
0085261F  45 8D 42 E1                     lea r8d, [r10 - 0x1f]
00852623  E9 CB F8 FF FF                  jmp 0x140851ef3
00852628  48 85 C0                        test rax, rax
0085262B  0F 84 F8 FB FF FF               je 0x140852229
00852631  48 8B D0                        mov rdx, rax
00852634  48 8D 4F 30                     lea rcx, [rdi + 0x30]
00852638  E8 D3 FB A0 FF                  call 0x140262210
0085263D  E9 E7 FB FF FF                  jmp 0x140852229
00852642  8B C1                           mov eax, ecx
00852644  33 C2                           xor eax, edx
00852646  25 00 00 E0 7F                  and eax, 0x7fe00000
0085264B  33 C1                           xor eax, ecx
0085264D  E9 FE FD FF FF                  jmp 0x140852450
00852652  48 89 01                        mov qword ptr [rcx], rax
00852655  48 89 51 08                     mov qword ptr [rcx + 8], rdx
00852659  48 89 0A                        mov qword ptr [rdx], rcx
0085265C  48 89 48 08                     mov qword ptr [rax + 8], rcx
00852660  48 8B CF                        mov rcx, rdi
00852663  E8 58 6C 37 00                  call 0x140bc92c0
00852668  49 8B CE                        mov rcx, r14
0085266B  E8 50 6C 37 00                  call 0x140bc92c0
00852670  E9 E7 FD FF FF                  jmp 0x14085245c
00852675  44 88 77 41                     mov byte ptr [rdi + 0x41], r14b
00852679  E9 9C FC FF FF                  jmp 0x14085231a
0085267E  48 89 77 58                     mov qword ptr [rdi + 0x58], rsi
00852682  E9 F7 FB FF FF                  jmp 0x14085227e
00852687  BE 9A 00 00 C0                  mov esi, 0xc000009a
0085268C  E9 35 FD FF FF                  jmp 0x1408523c6
00852691  49 8B 41 08                     mov rax, qword ptr [r9 + 8]
00852695  66 D1 EE                        shr si, 1
00852698  0F 1F 84 00 00 00 00 00         nop dword ptr [rax + rax]
008526A0  66 85 FF                        test di, di
008526A3  0F 84 61 F8 FF FF               je 0x140851f0a
008526A9  66 85 F6                        test si, si
008526AC  0F 84 58 F8 FF FF               je 0x140851f0a
008526B2  41 0F B7 14 24                  movzx edx, word ptr [r12]
008526B7  49 83 C4 02                     add r12, 2
008526BB  0F B7 08                        movzx ecx, word ptr [rax]
008526BE  48 83 C0 02                     add rax, 2
008526C2  48 89 45 9F                     mov qword ptr [rbp - 0x61], rax
008526C6  66 89 54 24 40                  mov word ptr [rsp + 0x40], dx
008526CB  66 3B CA                        cmp cx, dx
008526CE  75 0A                           jne 0x1408526da
008526D0  66 41 03 FA                     add di, r10w
008526D4  66 41 03 F2                     add si, r10w
008526D8  EB C6                           jmp 0x1408526a0
008526DA  66 83 F9 61                     cmp cx, 0x61
008526DE  72 0A                           jb 0x1408526ea
008526E0  66 83 F9 7A                     cmp cx, 0x7a
008526E4  77 2D                           ja 0x140852713
008526E6  66 41 03 C8                     add cx, r8w
008526EA  66 3B CA                        cmp cx, dx
008526ED  0F 85 03 FC FF FF               jne 0x1408522f6
008526F3  48 8B 45 9F                     mov rax, qword ptr [rbp - 0x61]
008526F7  EB D7                           jmp 0x1408526d0
008526F9  48 8B CF                        mov rcx, rdi
008526FC  E8 BF 6B 37 00                  call 0x140bc92c0
00852701  49 8B CE                        mov rcx, r14
00852704  E8 B7 6B 37 00                  call 0x140bc92c0
00852709  BE 0D 00 00 C0                  mov esi, 0xc000000d
0085270E  E9 1D FE FF FF                  jmp 0x140852530
00852713  E8 D8 C9 00 00                  call 0x14085f0f0
00852718  0F B7 54 24 40                  movzx edx, word ptr [rsp + 0x40]
0085271D  41 BA FF FF 00 00               mov r10d, 0xffff
00852723  0F B7 C8                        movzx ecx, ax
00852726  45 8D 42 E1                     lea r8d, [r10 - 0x1f]
0085272A  EB BE                           jmp 0x1408526ea
0085272C  49 8B CD                        mov rcx, r13
0085272F  E8 6C D2 14 00                  call 0x14099f9a0
00852734  48 8B 45 97                     mov rax, qword ptr [rbp - 0x69]
00852738  33 F6                           xor esi, esi
0085273A  4C 89 28                        mov qword ptr [rax], r13
0085273D  E9 84 FC FF FF                  jmp 0x1408523c6
00852742  BE 0D 00 00 C0                  mov esi, 0xc000000d
00852747  E9 7A FC FF FF                  jmp 0x1408523c6
0085274C  BE 9A 00 00 C0                  mov esi, 0xc000009a
00852751  48 8B DF                        mov rbx, rdi
00852754  E9 D7 FD FF FF                  jmp 0x140852530
00852759  48 8B C3                        mov rax, rbx
0085275C  E8 6F 83 E6 FF                  call 0x1406baad0
00852761  E9 43 FC FF FF                  jmp 0x1408523a9
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpCreateKeyControlBlock(__int64 a1, int a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, unsigned int a8, __int64 a9)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m3F;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned int v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int16 v_stack_mD8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p20;
    unsigned __int8 v_stack_p28;
    unsigned __int16 v_stack_p40;
    unsigned __int64 v_stack_p48;

    v_stack_p10 = v_rbx;
    v_rsp = (v_rsp) - (224);
    result = (*(unsigned __int64 *)(v_rip + 5998957)) ^ (v_rsp);
    v_stack_m40 = result;
    v_stack_mB0 = a1;
    v_stack_m98 = a4;
    v_stack_mC0 = a6;
    v_stack_mB8 = a3;
    v_stack_mC8 = a2;
    v_stack_mA8 = a9;
    v_stack_mD0 = 0;
    result = HvpGetCellContextInitialize(v_stack_mD0, a2, a3, a6);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 160)))) & (32)) == 0) goto loc_00851E3C;
    if ((*(unsigned __int64 *)(a1 + 4168)) != (*(unsigned __int64 *)(gs_base + (0 + 392)))) goto loc_00852330;
loc_00851E3C:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a8)))) >> (9));
    result = (unsigned int)((result) ^ ((unsigned int)((unsigned int)(a8))));
    result = (unsigned int)((result) * ((unsigned int)(result)));
    a2 = ((unsigned int)((unsigned int)(result))) >> (9);
    a2 = (a2) ^ ((unsigned int)((unsigned int)(result)));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 1656))) - 1);
    a2 = (a2) & (a1);
loc_00851E7A:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1648) + a2 + a2 * 2 * 8 + 16) == 0) goto loc_00851F21;
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1648) + a2 + a2 * 2 * 8 + 16))) != ((unsigned int)((unsigned int)(a8)))) goto loc_008522FB;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1648) + a2 + a2 * 2 * 8 + 16) + 56)) != a3) goto loc_008522FB;
    v_rdi = (unsigned __int16)((*(unsigned __int16 *)(a6)) >> (1));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1648) + a2 + a2 * 2 * 8 + 16) - 16 + 80))))) & (1)) == 0) goto loc_00852691;
loc_00851EBB:
    if ((unsigned __int16)(v_rdi) == 0) goto loc_00851F06;
    if ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1648) + a2 + a2 * 2 * 8 + 16) - 16 + 80) + 24)) == 0) goto loc_00851F06;
    v_r12 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1648) + a2 + a2 * 2 * 8 + 16) - 16 + 80) + 26) + 1;
    v_r15 = (*(unsigned __int64 *)(a6 + 8)) + (2);
    v_stack_mD8 = (unsigned __int16)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1648) + a2 + a2 * 2 * 8 + 16) - 16 + 80) + 26));
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a6 + 8)))) == ((unsigned __int16)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1648) + a2 + a2 * 2 * 8 + 16) - 16 + 80) + 26)))) goto loc_00851EFC;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a6 + 8)))) < 97) goto loc_00851EF3;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a6 + 8)))) > 122) goto loc_0085260C;
    a1 = (unsigned __int16)((*(unsigned __int16 *)(*(unsigned __int64 *)(a6 + 8))) + ((unsigned __int16)((unsigned int)(0xFFE0ULL))));
loc_00851EF3:
    if (((unsigned __int16)(a1)) != ((unsigned __int16)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1648) + a2 + a2 * 2 * 8 + 16) - 16 + 80) + 26)))) goto loc_008522F2;
loc_00851EFC:
    v_rdi = (unsigned __int16)((v_rdi) + ((unsigned __int16)((unsigned int)(0xFFE0ULL) + 31)));
    v_rsi = (unsigned __int16)((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1648) + a2 + a2 * 2 * 8 + 16) - 16 + 80) + 24)) + ((unsigned __int16)((unsigned int)(0xFFE0ULL) + 31)));
    goto loc_00851EBB;
loc_00851F06:
loc_00851F0A:
    if (((unsigned __int16)(v_rdi)) != ((unsigned __int16)(v_rsi))) goto loc_008522F6;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1648) + a2 + a2 * 2 * 8 + 16) - 16 != 0) goto loc_0085272C;
loc_00851F21:
    v_rsi = 0;
    if (v_stack_mB8 == 0) goto loc_00851F64;
loc_00851F30:
    if (((*(unsigned int *)(v_stack_mB8 + 184)) & (0x40000ULL)) != 0) goto loc_008522DE;
loc_00851F44:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_mB8 + 80))))) & (1)) == 0) goto loc_00852304;
loc_00851F59:
    a2 = (unsigned int)((0 + *(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_mB8 + 80) + 24) * 2) + (2));
    if (*(unsigned __int64 *)(v_stack_mB8 + 72) != 0) goto loc_00851F30;
loc_00851F64:
    a1 = (unsigned int)((a2 + 2) + ((unsigned int)(*(unsigned __int16 *)(v_stack_mC0))));
    if (((unsigned int)(a1)) > ((unsigned int)((unsigned int)(0xFFE0ULL) + 31))) goto loc_00852742;
    result = ExAllocateFromLookasideListEx(v_rip + 6138683, a2, v_stack_mB8 + 72, v_stack_mC0);
    if (result == 0) goto loc_00852687;
    a2 = 0;
    result = memset(result, a2, 312, v_stack_mC0);
    *(unsigned __int64 *)(result + 120 + 8) = result + 120;
    *(unsigned __int64 *)(result + 120) = result + 120;
    *(unsigned __int64 *)(result + 136) = 0;
    *(unsigned __int64 *)(result + 144) = 0;
    *(unsigned __int64 *)(result + 152) = 0;
    *(unsigned __int64 *)(result + 160) = 0;
    *(unsigned int *)(result + 40) = (unsigned int)((unsigned int)(v_stack_mC8));
    *(unsigned __int64 *)(result) = 1;
    *(unsigned __int64 *)(result + 32) = v_stack_mB0;
    *(unsigned int *)(result + 16) = (unsigned int)((unsigned int)(a8));
    *(unsigned __int64 *)(result + 48) = 0;
    *(unsigned __int64 *)(result + 208 + 8) = result + 208;
    *(unsigned __int64 *)(result + 208) = result + 208;
    *(unsigned __int64 *)(result + 224 + 8) = result + 224;
    *(unsigned __int64 *)(result + 224) = result + 224;
    *(unsigned __int64 *)(result + 240) = 0;
    *(unsigned int *)(result + 248) = 0;
    *(unsigned __int64 *)(result + 256) = 0;
    *(unsigned int *)(result + 264) = 0;
    *(unsigned __int64 *)(result + 272) = 0;
    *(unsigned int *)(result + 280) = 0;
    *(unsigned int *)(result + 284) = 0xFFFFFFFFULL;
    *(unsigned __int64 *)(result + 288) = 0;
    result = CmpGetNameControlBlock(v_stack_mC0, a7, 312, v_stack_mC0);
    *(unsigned __int64 *)(result + 80) = result;
    if (result == 0) goto loc_0085274C;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result + 40)))) == -1) goto loc_0085230B;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(result + 32) + 140)) & (1)) == 0) goto loc_008523F0;
    result = HvpGetCellFlat(*(unsigned __int64 *)(result + 32), (unsigned int)(*(unsigned int *)(result + 40)), v_stack_mD0, v_stack_mC0);
loc_0085208A:
    if (((*(unsigned int *)(*(unsigned __int64 *)(result + 32) + 160)) & (0x8001ULL)) != 0) goto loc_00852171;
    if (((*(unsigned __int8 *)(v_rip + 6015977)) & ((unsigned __int8)(*(unsigned __int8 *)(result + 12)))) != 0) goto loc_00852171;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(result + 32) + 140)) & (1)) != 0) goto loc_008525F1;
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(result + 32), v_stack_mD0, v_stack_mD0, v_stack_mC0);
loc_008520C8:
    a3 = 0;
    v_rbx = (*(unsigned __int64 *)(result + 32)) + (72);
    a2 = 0;
    result = KeAbPreAcquire(v_rbx, a2, a3, v_stack_mC0);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = v_rbx;
        a3 = 0;
        a2 = 0;
        a1 = v_rbx;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(result + 32) + 140)) & (1)) == 0) goto loc_008523FA;
    result = HvpGetCellFlat(*(unsigned __int64 *)(result + 32), (unsigned int)(*(unsigned int *)(result + 40)), v_stack_mD0, a4);
loc_00852126:
    if (((*(unsigned int *)(*(unsigned __int64 *)(result + 32) + 160)) & (0x8001ULL)) != 0) goto loc_0085214C;
    if (((*(unsigned __int8 *)(v_rip + 6015822)) & ((unsigned __int8)(*(unsigned __int8 *)(result + 12)))) == 0) goto loc_00852404;
loc_0085214C:
    result = 17;
    if (((*(unsigned __int8 *)(v_rip + 6015822)) & ((unsigned __int8)(*(unsigned __int8 *)(result + 12)))) != 0) {
        a1 = *(unsigned __int64 *)(result + 32) + 72;
        result = ExfReleasePushLockShared(a1, (unsigned int)(*(unsigned int *)(result + 40)), v_stack_mD0, a4);
    }
    result = KeAbPostRelease(*(unsigned __int64 *)(result + 32) + 72, (unsigned int)(*(unsigned int *)(result + 40)), v_stack_mD0, a4);
loc_00852171:
    result = (unsigned __int8)((*(unsigned __int8 *)(result + 13)) & (3));
    a2 = 0;
    *(unsigned __int8 *)(result + 65) = (unsigned __int8)(result);
    *(unsigned int *)(result + 96) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 36)));
    *(unsigned int *)(result + 100) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 40)));
    *(unsigned __int16 *)(result + 186) = (unsigned __int16)(*(unsigned __int16 *)(result + 2));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 24))) + (*(unsigned int *)(result + 20)));
    *(unsigned int *)(result + 112) = (unsigned int)(result);
    *(unsigned __int64 *)(result + 168) = *(unsigned __int64 *)(result + 4);
    *(unsigned __int16 *)(result + 176) = (unsigned __int16)(*(unsigned __int16 *)(result + 52));
    *(unsigned __int16 *)(result + 178) = (unsigned __int16)(*(unsigned __int16 *)(result + 60));
    *(unsigned int *)(result + 180) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 64)));
    a1 = (unsigned int)((*(unsigned __int16 *)(result + 54)) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(result + 184)))));
    a1 = (unsigned int)((a1) & (15));
    a1 = (unsigned int)((a1) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(result + 184)))));
    *(unsigned int *)(result + 184) = (unsigned int)(a1);
    result = (unsigned int)((*(unsigned __int16 *)(result + 54)) ^ ((unsigned int)(a1)));
    result = (unsigned int)((result) & (240));
    result = (unsigned int)((result) ^ ((unsigned int)(a1)));
    *(unsigned int *)(result + 184) = (unsigned int)(result);
    *(unsigned __int8 *)(result + 185) = (unsigned __int8)(*(unsigned __int8 *)(result + 55));
    result = KeAbPreAcquire(result + 48, a2, 1, a4);
    if (condition_is_below) goto loc_00852628;
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    *(unsigned __int64 *)(result + 56) = *(unsigned __int64 *)(gs_base + (0 + 392));
loc_00852229:
    v_stack_mC8 = 0;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result + 44)))) == -1) goto loc_0085267E;
    result = CmLockHiveSecurityShared(*(unsigned __int64 *)(result + 32), a2, 1, a4);
    result = CmpFindSecurityCellCacheIndex(*(unsigned __int64 *)(result + 32), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + 44)))), v_stack_mC8, a4);
    if ((unsigned __int8)(result) == 0) goto loc_008524FA;
    a1 = ((unsigned int)(v_stack_mC8)) + ((unsigned int)(v_stack_mC8));
    *(unsigned __int64 *)(result + 88) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) + 1888) + a1 * 8 + 8);
    result = CmUnlockHiveSecurity(*(unsigned __int64 *)(result + 32), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + 44)))), v_stack_mC8, a4);
loc_0085227E:
    result = CmpUnlockKcb(result, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + 44)))), v_stack_mC8, a4);
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(result + 32) + 140)) & (1)) != 0) goto loc_008525E7;
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(result + 32), v_stack_mD0, v_stack_mC8, a4);
loc_008522A4:
    if (v_stack_mB8 == 0) goto loc_008525FB;
    v_r14 = (1) + (1);
    if (condition_is_equal) goto loc_008525CF;
    if (v_r14 != 1) goto loc_00852426;
    v_stack_mF8 = 0;
    a4 = 0;
    a3 = 0;
    result = KeBugCheckEx(v_r14 + 20 + 60, v_r14 + 20, a3, a4);
loc_008522DE:
    if (*(unsigned __int64 *)(a3) == 0) goto loc_00851F44;
    goto loc_00851F30;
loc_008522F2:
loc_008522F6:
loc_008522FB:
    goto loc_00851E7A;
loc_00852304:
    a2 = (unsigned int)((v_r14 + 20) + ((unsigned int)(*(unsigned __int64 *)(a3))));
    goto loc_00851F59;
loc_0085230B:
    result = (unsigned __int8)((*(unsigned __int8 *)(v_stack_mB8 + 65)) - 1);
    if ((((unsigned __int8)(result)) & (253)) == 0) goto loc_00852675;
loc_0085231A:
    if (((v_stack_p28) & ((unsigned __int8)(*(unsigned __int64 *)(v_r14 + 8)))) == 0) goto loc_008522A4;
    goto loc_008522A4;
loc_00852330:
    goto loc_008523C6;
loc_0085233A:
loc_0085233F:
    if (*(unsigned __int64 *)(v_rip + 7888066) == 0) goto loc_008523BF;
    v_stack_m90 = v_xmm0;
    v_stack_m80 = v_xmm0;
    v_stack_m70 = v_xmm1;
    v_stack_m60 = v_xmm1;
    v_stack_m50 = v_xmm1;
    result = CmpAttachToRegistryProcess(v_stack_m70, a2, a3, v_stack_mC0);
    result = CmpConstructName(result, a2, a3, v_stack_mC0);
    if (result == 0) goto loc_008523B6;
    v_stack_mF0 = result;
    a4 = 0;
    v_stack_mF8 = result;
    a3 = 0;
    if ((*(unsigned __int64 *)(v_rip + 7888066)) != (v_rip + 67067)) goto loc_00852759;
    result = EtwpTraceRegistry(22, v_stack_m90, a3, a4);
loc_008523A9:
    result = CmpFreePoolWithTag(result, (unsigned int)(0x624E4D43ULL), a3, a4);
loc_008523B6:
    result = CmpDetachFromRegistryProcess(v_stack_m70, (unsigned int)(0x624E4D43ULL), a3, a4);
loc_008523BF:
    *(unsigned __int64 *)(v_stack_mA8) = result;
loc_008523C6:
    a1 = (v_stack_m40) ^ (v_rsp);
    result = _security_check_cookie(a1, (unsigned int)(0x624E4D43ULL), a3, a4);
    v_rsp = (v_rsp) + (224);
    return result;
loc_008523F0:
    result = HvpGetCellPaged(a1, (unsigned int)(0x624E4D43ULL), a3, a4);
    goto loc_0085208A;
loc_008523FA:
    result = HvpGetCellPaged(a1, (unsigned int)(0x624E4D43ULL), a3, a4);
    goto loc_00852126;
loc_00852404:
    a3 = 0;
    result = HvpMarkCellDirty(a1, (unsigned int)(0x624E4D43ULL), a3, (unsigned int)((unsigned int)(result)));
    if (sign_flag) goto loc_0085214C;
    goto loc_0085214C;
loc_00852426:
    *(unsigned __int64 *)(result + 72) = v_stack_mB8;
    if (((*(unsigned int *)(result + 184)) & (0x40000ULL)) != 0) goto loc_00852642;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_mB8 + 8)) + 2097152) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(result + 8)))));
    result = (unsigned int)((result) & (0x7FE00000ULL));
    result = (unsigned int)((result) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(result + 8)))));
loc_00852450:
    *(unsigned int *)(result + 8) = (unsigned int)(result);
    if (v_stack_m98 != 0) goto loc_008524BA;
loc_0085245C:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + 16))))) >> (9));
    a1 = (unsigned int)((a1) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(result + 16)))));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 16))) * ((unsigned int)(a1)));
    a2 = ((unsigned int)((unsigned int)(result))) >> (9);
    a2 = (a2) ^ ((unsigned int)((unsigned int)(result)));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 32) + 1656))) - 1);
    a2 = (a2) & (a1);
    *(unsigned __int64 *)(result + 24) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) + 1648) + a2 + a2 * 2 * 8 + 16);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) + 1648) + a2 + a2 * 2 * 8 + 16) = result + 16;
    if ((*(unsigned __int8 *)(v_stack_mB0 + 2944)) == 1) goto loc_0085233A;
    goto loc_0085233F;
loc_008524BA:
    result = CmpLockKcbExclusive(v_stack_m98, *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) + 1648) + a2 + a2 * 2 * 8, *(unsigned __int64 *)(result + 32), (unsigned int)((unsigned int)(result)));
    result = CmpTryToLockKcbExclusive(result, *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) + 1648) + a2 + a2 * 2 * 8, *(unsigned __int64 *)(result + 32), (unsigned int)((unsigned int)(result)));
    if ((*(unsigned __int16 *)(v_stack_m98 + 66)) >= 127) goto loc_008526F9;
    result = CmpAllocateLayerInfoForKcb(v_stack_m98, *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) + 1648) + a2 + a2 * 2 * 8, *(unsigned __int64 *)(result + 32), (unsigned int)((unsigned int)(result)));
    if (!sign_flag) goto loc_00852574;
loc_008524E6:
    result = CmpUnlockKcb(result, *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) + 1648) + a2 + a2 * 2 * 8, *(unsigned __int64 *)(result + 32), (unsigned int)((unsigned int)(result)));
    result = CmpUnlockKcb(v_stack_m98, *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) + 1648) + a2 + a2 * 2 * 8, *(unsigned __int64 *)(result + 32), (unsigned int)((unsigned int)(result)));
    goto loc_00852530;
loc_008524FA:
    *(unsigned __int64 *)(result + 88) = (unsigned int)((unsigned int)(result));
    result = CmUnlockHiveSecurity(v_stack_p10, *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) + 1648) + a2 + a2 * 2 * 8, *(unsigned __int64 *)(result + 32), (unsigned int)((unsigned int)(result)));
    result = CmpUnlockKcb(result, *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) + 1648) + a2 + a2 * 2 * 8, *(unsigned __int64 *)(result + 32), (unsigned int)((unsigned int)(result)));
    if (((*(unsigned __int8 *)(v_stack_mB0 + 140)) & ((unsigned __int8)(v_stack_m98))) != 0) goto loc_008525C2;
    result = HvpReleaseCellPaged(v_stack_mB0, v_stack_p48, *(unsigned __int64 *)(result + 32), (unsigned int)((unsigned int)(result)));
loc_00852530:
    if (*(unsigned __int64 *)(result + 80) != 0) {
        result = CmpDereferenceNameControlBlockWithLock(*(unsigned __int64 *)(result + 80), v_stack_p48, *(unsigned __int64 *)(result + 32), (unsigned int)((unsigned int)(result)));
    }
    if ((*(unsigned __int64 *)(result + 72)) != 0) {
        a1 = v_stack_mB8;
        result = CmpDereferenceKeyControlBlockUnsafe(a1, v_stack_p48, *(unsigned __int64 *)(result + 32), (unsigned int)((unsigned int)(result)));
    }
    if (*(unsigned __int64 *)(result + 192) != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(result + 192), a2, *(unsigned __int64 *)(result + 32), (unsigned int)((unsigned int)(result)));
    }
    result = CmpFreeKeyControlBlock(result, a2, *(unsigned __int64 *)(result + 32), (unsigned int)((unsigned int)(result)));
    goto loc_008523C6;
loc_00852574:
    result = CmpAllocateLayerInfoForKcb(result, a2, *(unsigned __int64 *)(result + 32), (unsigned int)((unsigned int)(result)));
    if (sign_flag) goto loc_008524E6;
    result = CmpReferenceKeyControlBlock(v_stack_m98, a2, *(unsigned __int64 *)(result + 32), (unsigned int)((unsigned int)(result)));
    result = (unsigned __int16)((*(unsigned __int16 *)(v_stack_m98 + 66)) + 1);
    *(unsigned __int16 *)(result + 66) = (unsigned __int16)(result);
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 192) + 24) = *(unsigned __int64 *)(v_stack_m98 + 192);
    result = (*(unsigned __int64 *)(v_stack_m98 + 192)) + (32);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8))) == result) goto loc_00852652;
loc_008525C2:
    result = HvpReleaseCellFlat(3, *(unsigned __int64 *)(result + 8), *(unsigned __int64 *)(result + 32), (unsigned int)((unsigned int)(result)));
    goto loc_00852530;
loc_008525CF:
    a4 = 0;
    v_stack_p20 = (unsigned int)(0xC000009AULL);
    result = KeBugCheckEx(a4 + 36 + 45, a4 + 36, v_stack_mB8, a4);
loc_008525E7:
    result = HvpReleaseCellFlat(a4 + 36 + 45, a4 + 36, v_stack_mB8, a4);
    goto loc_008522A4;
loc_008525F1:
    result = HvpReleaseCellFlat(a4 + 36 + 45, a4 + 36, v_stack_mB8, a4);
    goto loc_008520C8;
loc_008525FB:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 8))) & (0x803FFFFFULL));
    goto loc_00852450;
loc_0085260C:
    result = RtlUpcaseUnicodeChar(a4 + 36 + 45, a4 + 36, v_stack_mB8, a4);
    goto loc_00851EF3;
loc_00852628:
    if (v_stack_p40 == 0) goto loc_00852229;
    result = KeAbPostReleaseEx(result + 48, v_stack_p40, (unsigned int)(0xFFFFULL) - 31, a4);
    goto loc_00852229;
loc_00852642:
    result = (unsigned int)(((unsigned int)((unsigned int)(result + 48))) ^ ((unsigned int)(v_stack_p40)));
    result = (unsigned int)((result) & (0x7FE00000ULL));
    result = (unsigned int)((result) ^ ((unsigned int)(result + 48)));
    goto loc_00852450;
loc_00852652:
    *(unsigned __int64 *)(result + 48) = result;
    *(unsigned __int64 *)(result + 48 + 8) = v_stack_p40;
    *(unsigned __int64 *)(v_stack_p40) = result + 48;
    *(unsigned __int64 *)(result + 8) = result + 48;
    result = CmpUnlockKcb(result, v_stack_p40, (unsigned int)(0xFFFFULL) - 31, a4);
    result = CmpUnlockKcb(v_stack_m98, v_stack_p40, (unsigned int)(0xFFFFULL) - 31, a4);
    goto loc_0085245C;
loc_00852675:
    *(unsigned __int8 *)(result + 65) = (unsigned __int8)(v_stack_m98);
    goto loc_0085231A;
loc_0085267E:
    *(unsigned __int64 *)(result + 88) = (unsigned int)(0xC000009AULL);
    goto loc_0085227E;
loc_00852687:
    goto loc_008523C6;
loc_00852691:
    v_rsi = (unsigned __int16)(((unsigned int)(0xC000009AULL)) >> (1));
loc_008526A0:
    if ((unsigned __int16)(result) == 0) goto loc_00851F0A;
    if ((unsigned __int16)(v_rsi) == 0) goto loc_00851F0A;
    v_r12 = ((unsigned int)(*(unsigned int *)(result + 44))) + (2);
    result = (*(unsigned __int64 *)(a4 + 8)) + (2);
    v_stack_mA0 = result;
    v_stack_p40 = (unsigned __int16)(*(unsigned __int16 *)((unsigned int)(*(unsigned int *)(result + 44))));
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a4 + 8)))) != ((unsigned __int16)(*(unsigned __int16 *)((unsigned int)(*(unsigned int *)(result + 44)))))) goto loc_008526DA;
loc_008526D0:
    v_rdi = (unsigned __int16)((result) + ((unsigned __int16)((unsigned int)(0xFFFFULL))));
    v_rsi = (unsigned __int16)((v_rsi) + ((unsigned __int16)((unsigned int)(0xFFFFULL))));
    goto loc_008526A0;
loc_008526DA:
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a4 + 8)))) < 97) goto loc_008526EA;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a4 + 8)))) > 122) goto loc_00852713;
    a1 = (unsigned __int16)((*(unsigned __int16 *)(*(unsigned __int64 *)(a4 + 8))) + ((unsigned __int16)((unsigned int)(0xFFFFULL) - 31)));
loc_008526EA:
    if (((unsigned __int16)(a1)) != ((unsigned __int16)(*(unsigned __int16 *)((unsigned int)(*(unsigned int *)(result + 44)))))) goto loc_008522F6;
    goto loc_008526D0;
loc_008526F9:
    result = CmpUnlockKcb(v_rdi, *(unsigned __int16 *)((unsigned int)(*(unsigned int *)(result + 44))), (unsigned int)(0xFFFFULL) - 31, a4);
    result = CmpUnlockKcb(v_stack_m98, *(unsigned __int16 *)((unsigned int)(*(unsigned int *)(result + 44))), (unsigned int)(0xFFFFULL) - 31, a4);
    goto loc_00852530;
loc_00852713:
    result = RtlUpcaseUnicodeChar(v_stack_m98, *(unsigned __int16 *)((unsigned int)(*(unsigned int *)(result + 44))), (unsigned int)(0xFFFFULL) - 31, a4);
    goto loc_008526EA;
loc_0085272C:
    result = CmpReferenceKeyControlBlockLockNotHeld(v_stack_mB0, v_stack_p40, (unsigned int)(0xFFFFULL) - 31, a4);
    v_rsi = 0;
    *(unsigned __int64 *)(v_stack_mA8) = v_stack_mB0;
    goto loc_008523C6;
loc_00852742:
    goto loc_008523C6;
loc_0085274C:
    goto loc_00852530;
loc_00852759:
    result = guard_dispatch_icall(v_stack_mB0, v_stack_p40, (unsigned int)(0xFFFFULL) - 31, a4);
    goto loc_008523A9;
}
```

## 5. (Beta) C Style

```c
int64_t CmpCreateKeyControlBlock(void *Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, int64_t Arg6, int64_t Arg7, uint32_t Arg8, int64_t Arg9)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m3F;
    uint64_t v_stack_m40;
    uint64_t v_stack_m50;
    uint64_t v_stack_m60;
    uint64_t v_stack_m70;
    uint64_t v_stack_m80;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint32_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint16_t v_stack_mD8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p20;
    uint8_t v_stack_p28;
    uint16_t v_stack_p40;
    uint64_t v_stack_p48;

    v_stack_p10 = local_rbx;
    local_rsp = (local_rsp) - (224);
    result = (*(uint64_t *)(v_rip + 0x5B896D)) ^ (local_rsp);
    v_stack_m40 = result;
    v_stack_mB0 = Arg1;
    v_stack_m98 = Arg4;
    v_stack_mC0 = Arg6;
    v_stack_mB8 = Arg3;
    v_stack_mC8 = Arg2;
    v_stack_mA8 = Arg9;
    v_stack_mD0 = 0;
    result = HvpGetCellContextInitialize(v_stack_mD0, Arg2, Arg3, Arg6);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0xA0)))) & (32)) == 0) goto loc_00851E3C;
    if ((*(uint64_t *)(arg1 + 0x1048)) != (*(uint64_t *)(gs_base + (0 + 0x188)))) goto loc_00852330;
loc_00851E3C:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg8)))) >> (9));
    result = (uint32_t)((result) ^ ((uint32_t)((uint32_t)(Arg8))));
    result = (uint32_t)((result) * ((uint32_t)(result)));
    Arg2 = ((uint32_t)((uint32_t)(result))) >> (9);
    Arg2 = (Arg2) ^ ((uint32_t)((uint32_t)(result)));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x678))) - 1);
    Arg2 = (Arg2) & (Arg1);
loc_00851E7A:
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x670) + Arg2 + Arg2 * 2 * 8 + 0x10) == 0) goto loc_00851F21;
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x670) + Arg2 + Arg2 * 2 * 8 + 0x10))) != ((uint32_t)((uint32_t)(Arg8)))) goto loc_008522FB;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x670) + Arg2 + Arg2 * 2 * 8 + 0x10) + 0x38)) != Arg3) goto loc_008522FB;
    local_rdi = (uint16_t)((*(uint16_t *)(Arg6)) >> (1));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x670) + Arg2 + Arg2 * 2 * 8 + 0x10) - 0x10 + 0x50))))) & (1)) == 0) goto loc_00852691;
loc_00851EBB:
    if ((uint16_t)(local_rdi) == 0) goto loc_00851F06;
    if ((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x670) + Arg2 + Arg2 * 2 * 8 + 0x10) - 0x10 + 0x50) + 0x18)) == 0) goto loc_00851F06;
    local_r12 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x670) + Arg2 + Arg2 * 2 * 8 + 0x10) - 0x10 + 0x50) + 26) + 1;
    local_r15 = (*(uint64_t *)(Arg6 + 0x8)) + (2);
    v_stack_mD8 = (uint16_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x670) + Arg2 + Arg2 * 2 * 8 + 0x10) - 0x10 + 0x50) + 0x1A));
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(Arg6 + 0x8)))) == ((uint16_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x670) + Arg2 + Arg2 * 2 * 8 + 0x10) - 0x10 + 0x50) + 0x1A)))) goto loc_00851EFC;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(Arg6 + 0x8)))) < 97) goto loc_00851EF3;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(Arg6 + 0x8)))) > 122) goto loc_0085260C;
    Arg1 = (uint16_t)((*(uint16_t *)(*(uint64_t *)(Arg6 + 0x8))) + ((uint16_t)((uint32_t)(0xFFE0ULL))));
loc_00851EF3:
    if (((uint16_t)(Arg1)) != ((uint16_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x670) + Arg2 + Arg2 * 2 * 8 + 0x10) - 0x10 + 0x50) + 0x1A)))) goto loc_008522F2;
loc_00851EFC:
    local_rdi = (uint16_t)((local_rdi) + ((uint16_t)((uint32_t)(0xFFE0ULL) + 31)));
    local_rsi = (uint16_t)((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x670) + Arg2 + Arg2 * 2 * 8 + 0x10) - 0x10 + 0x50) + 0x18)) + ((uint16_t)((uint32_t)(0xFFE0ULL) + 31)));
    goto loc_00851EBB;
loc_00851F06:
loc_00851F0A:
    if (((uint16_t)(local_rdi)) != ((uint16_t)(local_rsi))) goto loc_008522F6;
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x670) + Arg2 + Arg2 * 2 * 8 + 0x10) - 16 != 0) goto loc_0085272C;
loc_00851F21:
    local_rsi = 0;
    if (v_stack_mB8 == 0) goto loc_00851F64;
loc_00851F30:
    if (((*(uint32_t *)(v_stack_mB8 + 0xB8)) & (0x40000ULL)) != 0) goto loc_008522DE;
loc_00851F44:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_mB8 + 0x50))))) & (1)) == 0) goto loc_00852304;
loc_00851F59:
    Arg2 = (uint32_t)((0 + *(uint16_t *)(*(uint64_t *)(v_stack_mB8 + 0x50) + 0x18) * 2) + (2));
    if (*(uint64_t *)(v_stack_mB8 + 0x48) != 0) goto loc_00851F30;
loc_00851F64:
    Arg1 = (uint32_t)((Arg2 + 2) + ((uint32_t)(*(uint16_t *)(v_stack_mC0))));
    if (((uint32_t)(Arg1)) > ((uint32_t)((uint32_t)(0xFFE0ULL) + 31))) goto loc_00852742;
    result = ExAllocateFromLookasideListEx(v_rip + 6138683, Arg2, v_stack_mB8 + 72, v_stack_mC0);
    if (result == 0) goto loc_00852687;
    Arg2 = 0;
    result = memset(result, Arg2, 312, v_stack_mC0);
    *(uint64_t *)(result + 0x78 + 0x8) = result + 120;
    *(uint64_t *)(result + 0x78) = result + 120;
    *(uint64_t *)(result + 0x88) = 0;
    *(uint64_t *)(result + 0x90) = 0;
    *(uint64_t *)(result + 0x98) = 0;
    *(uint64_t *)(result + 0xA0) = 0;
    *(uint32_t *)(result + 0x28) = (uint32_t)((uint32_t)(v_stack_mC8));
    *(uint64_t *)(result) = 1;
    *(uint64_t *)(result + 0x20) = v_stack_mB0;
    *(uint32_t *)(result + 0x10) = (uint32_t)((uint32_t)(Arg8));
    *(uint64_t *)(result + 0x30) = 0;
    *(uint64_t *)(result + 0xD0 + 0x8) = result + 208;
    *(uint64_t *)(result + 0xD0) = result + 208;
    *(uint64_t *)(result + 0xE0 + 0x8) = result + 224;
    *(uint64_t *)(result + 0xE0) = result + 224;
    *(uint64_t *)(result + 0xF0) = 0;
    *(uint32_t *)(result + 0xF8) = 0;
    *(uint64_t *)(result + 0x100) = 0;
    *(uint32_t *)(result + 0x108) = 0;
    *(uint64_t *)(result + 0x110) = 0;
    *(uint32_t *)(result + 0x118) = 0;
    *(uint32_t *)(result + 0x11C) = 0xFFFFFFFFULL;
    *(uint64_t *)(result + 0x120) = 0;
    result = CmpGetNameControlBlock(v_stack_mC0, Arg7, 312, v_stack_mC0);
    *(uint64_t *)(result + 0x50) = result;
    if (result == 0) goto loc_0085274C;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x28)))) == -1) goto loc_0085230B;
    if (((*(uint8_t *)(*(uint64_t *)(result + 0x20) + 0x8C)) & (1)) == 0) goto loc_008523F0;
    result = HvpGetCellFlat(*(uint64_t *)(result + 0x20), (uint32_t)(*(uint32_t *)(result + 0x28)), v_stack_mD0, v_stack_mC0);
loc_0085208A:
    if (((*(uint32_t *)(*(uint64_t *)(result + 0x20) + 0xA0)) & (0x8001ULL)) != 0) goto loc_00852171;
    if (((*(uint8_t *)(v_rip + 0x5BCBE9)) & ((uint8_t)(*(uint8_t *)(result + 0xC)))) != 0) goto loc_00852171;
    if (((*(uint8_t *)(*(uint64_t *)(result + 0x20) + 0x8C)) & (1)) != 0) goto loc_008525F1;
    result = HvpReleaseCellPaged(*(uint64_t *)(result + 0x20), v_stack_mD0, v_stack_mD0, v_stack_mC0);
loc_008520C8:
    Arg3 = 0;
    local_rbx = (*(uint64_t *)(result + 0x20)) + (72);
    Arg2 = 0;
    result = KeAbPreAcquire(local_rbx, Arg2, Arg3, v_stack_mC0);
    result = 0;
    if (!(condition_is_equal)) {
        Arg4 = local_rbx;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = local_rbx;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    if (((*(uint8_t *)(*(uint64_t *)(result + 0x20) + 0x8C)) & (1)) == 0) goto loc_008523FA;
    result = HvpGetCellFlat(*(uint64_t *)(result + 0x20), (uint32_t)(*(uint32_t *)(result + 0x28)), v_stack_mD0, Arg4);
loc_00852126:
    if (((*(uint32_t *)(*(uint64_t *)(result + 0x20) + 0xA0)) & (0x8001ULL)) != 0) goto loc_0085214C;
    if (((*(uint8_t *)(v_rip + 0x5BCB4E)) & ((uint8_t)(*(uint8_t *)(result + 0xC)))) == 0) goto loc_00852404;
loc_0085214C:
    result = 17;
    if (((*(uint8_t *)(v_rip + 0x5BCB4E)) & ((uint8_t)(*(uint8_t *)(result + 0xC)))) != 0) {
        Arg1 = *(uint64_t *)(result + 0x20) + 72;
        result = ExfReleasePushLockShared(Arg1, (uint32_t)(*(uint32_t *)(result + 0x28)), v_stack_mD0, Arg4);
    }
    result = KeAbPostRelease(*(uint64_t *)(result + 0x20) + 72, (uint32_t)(*(uint32_t *)(result + 0x28)), v_stack_mD0, Arg4);
loc_00852171:
    result = (uint8_t)((*(uint8_t *)(result + 0xD)) & (3));
    Arg2 = 0;
    *(uint8_t *)(result + 0x41) = (uint8_t)(result);
    *(uint32_t *)(result + 0x60) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x24)));
    *(uint32_t *)(result + 0x64) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x28)));
    *(uint16_t *)(result + 0xBA) = (uint16_t)(*(uint16_t *)(result + 0x2));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x18))) + (*(uint32_t *)(result + 0x14)));
    *(uint32_t *)(result + 0x70) = (uint32_t)(result);
    *(uint64_t *)(result + 0xA8) = *(uint64_t *)(result + 0x4);
    *(uint16_t *)(result + 0xB0) = (uint16_t)(*(uint16_t *)(result + 0x34));
    *(uint16_t *)(result + 0xB2) = (uint16_t)(*(uint16_t *)(result + 0x3C));
    *(uint32_t *)(result + 0xB4) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x40)));
    Arg1 = (uint32_t)((*(uint16_t *)(result + 0x36)) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0xB8)))));
    Arg1 = (uint32_t)((Arg1) & (15));
    Arg1 = (uint32_t)((Arg1) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0xB8)))));
    *(uint32_t *)(result + 0xB8) = (uint32_t)(Arg1);
    result = (uint32_t)((*(uint16_t *)(result + 0x36)) ^ ((uint32_t)(Arg1)));
    result = (uint32_t)((result) & (240));
    result = (uint32_t)((result) ^ ((uint32_t)(Arg1)));
    *(uint32_t *)(result + 0xB8) = (uint32_t)(result);
    *(uint8_t *)(result + 0xB9) = (uint8_t)(*(uint8_t *)(result + 0x37));
    result = KeAbPreAcquire(result + 48, Arg2, 1, Arg4);
    if (condition_is_below) goto loc_00852628;
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    *(uint64_t *)(result + 0x38) = *(uint64_t *)(gs_base + (0 + 0x188));
loc_00852229:
    v_stack_mC8 = 0;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x2C)))) == -1) goto loc_0085267E;
    result = CmLockHiveSecurityShared(*(uint64_t *)(result + 0x20), Arg2, 1, Arg4);
    result = CmpFindSecurityCellCacheIndex(*(uint64_t *)(result + 0x20), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x2C)))), v_stack_mC8, Arg4);
    if ((uint8_t)(result) == 0) goto loc_008524FA;
    Arg1 = ((uint32_t)(v_stack_mC8)) + ((uint32_t)(v_stack_mC8));
    *(uint64_t *)(result + 0x58) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x20) + 0x760) + arg1 * 8 + 0x8);
    result = CmUnlockHiveSecurity(*(uint64_t *)(result + 0x20), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x2C)))), v_stack_mC8, Arg4);
loc_0085227E:
    result = CmpUnlockKcb(result, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x2C)))), v_stack_mC8, Arg4);
    if (((*(uint8_t *)(*(uint64_t *)(result + 0x20) + 0x8C)) & (1)) != 0) goto loc_008525E7;
    result = HvpReleaseCellPaged(*(uint64_t *)(result + 0x20), v_stack_mD0, v_stack_mC8, Arg4);
loc_008522A4:
    if (v_stack_mB8 == 0) goto loc_008525FB;
    local_r14 = (1) + (1);
    if (condition_is_equal) goto loc_008525CF;
    if (local_r14 != 1) goto loc_00852426;
    v_stack_mF8 = 0;
    Arg4 = 0;
    Arg3 = 0;
    result = KeBugCheckEx(local_r14 + 20 + 60, local_r14 + 20, Arg3, Arg4);
loc_008522DE:
    if (*(uint64_t *)(Arg3) == 0) goto loc_00851F44;
    goto loc_00851F30;
loc_008522F2:
loc_008522F6:
loc_008522FB:
    goto loc_00851E7A;
loc_00852304:
    Arg2 = (uint32_t)((local_r14 + 20) + ((uint32_t)(*(uint64_t *)(Arg3))));
    goto loc_00851F59;
loc_0085230B:
    result = (uint8_t)((*(uint8_t *)(v_stack_mB8 + 0x41)) - 1);
    if ((((uint8_t)(result)) & (253)) == 0) goto loc_00852675;
loc_0085231A:
    if (((v_stack_p28) & ((uint8_t)(*(uint64_t *)(local_r14 + 0x8)))) == 0) goto loc_008522A4;
    goto loc_008522A4;
loc_00852330:
    goto loc_008523C6;
loc_0085233A:
loc_0085233F:
    if (*(uint64_t *)(v_rip + 0x785CC2) == 0) goto loc_008523BF;
    v_stack_m90 = v_xmm0;
    v_stack_m80 = v_xmm0;
    v_stack_m70 = v_xmm1;
    v_stack_m60 = v_xmm1;
    v_stack_m50 = v_xmm1;
    result = CmpAttachToRegistryProcess(v_stack_m70, Arg2, Arg3, v_stack_mC0);
    result = CmpConstructName(result, Arg2, Arg3, v_stack_mC0);
    if (result == 0) goto loc_008523B6;
    v_stack_mF0 = result;
    Arg4 = 0;
    v_stack_mF8 = result;
    Arg3 = 0;
    if ((*(uint64_t *)(v_rip + 0x785CC2)) != (v_rip + 67067)) goto loc_00852759;
    result = EtwpTraceRegistry(22, v_stack_m90, Arg3, Arg4);
loc_008523A9:
    result = CmpFreePoolWithTag(result, (uint32_t)(0x624E4D43ULL), Arg3, Arg4);
loc_008523B6:
    result = CmpDetachFromRegistryProcess(v_stack_m70, (uint32_t)(0x624E4D43ULL), Arg3, Arg4);
loc_008523BF:
    *(uint64_t *)(v_stack_mA8) = result;
loc_008523C6:
    Arg1 = (v_stack_m40) ^ (local_rsp);
    result = _security_check_cookie(Arg1, (uint32_t)(0x624E4D43ULL), Arg3, Arg4);
    local_rsp = (local_rsp) + (224);
    return result;
loc_008523F0:
    result = HvpGetCellPaged(Arg1, (uint32_t)(0x624E4D43ULL), Arg3, Arg4);
    goto loc_0085208A;
loc_008523FA:
    result = HvpGetCellPaged(Arg1, (uint32_t)(0x624E4D43ULL), Arg3, Arg4);
    goto loc_00852126;
loc_00852404:
    Arg3 = 0;
    result = HvpMarkCellDirty(Arg1, (uint32_t)(0x624E4D43ULL), Arg3, (uint32_t)((uint32_t)(result)));
    if (sign_flag) goto loc_0085214C;
    goto loc_0085214C;
loc_00852426:
    *(uint64_t *)(result + 0x48) = v_stack_mB8;
    if (((*(uint32_t *)(result + 0xB8)) & (0x40000ULL)) != 0) goto loc_00852642;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_mB8 + 0x8)) + 2097152) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x8)))));
    result = (uint32_t)((result) & (0x7FE00000ULL));
    result = (uint32_t)((result) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x8)))));
loc_00852450:
    *(uint32_t *)(result + 0x8) = (uint32_t)(result);
    if (v_stack_m98 != 0) goto loc_008524BA;
loc_0085245C:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x10))))) >> (9));
    Arg1 = (uint32_t)((Arg1) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x10)))));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x10))) * ((uint32_t)(Arg1)));
    Arg2 = ((uint32_t)((uint32_t)(result))) >> (9);
    Arg2 = (Arg2) ^ ((uint32_t)((uint32_t)(result)));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x20) + 0x678))) - 1);
    Arg2 = (Arg2) & (Arg1);
    *(uint64_t *)(result + 0x18) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x20) + 0x670) + Arg2 + Arg2 * 2 * 8 + 0x10);
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x20) + 0x670) + Arg2 + Arg2 * 2 * 8 + 0x10) = result + 16;
    if ((*(uint8_t *)(v_stack_mB0 + 0xB80)) == 1) goto loc_0085233A;
    goto loc_0085233F;
loc_008524BA:
    result = CmpLockKcbExclusive(v_stack_m98, *(uint64_t *)(*(uint64_t *)(result + 0x20) + 0x670) + Arg2 + Arg2 * 2 * 8, *(uint64_t *)(result + 0x20), (uint32_t)((uint32_t)(result)));
    result = CmpTryToLockKcbExclusive(result, *(uint64_t *)(*(uint64_t *)(result + 0x20) + 0x670) + Arg2 + Arg2 * 2 * 8, *(uint64_t *)(result + 0x20), (uint32_t)((uint32_t)(result)));
    if ((*(uint16_t *)(v_stack_m98 + 0x42)) >= 127) goto loc_008526F9;
    result = CmpAllocateLayerInfoForKcb(v_stack_m98, *(uint64_t *)(*(uint64_t *)(result + 0x20) + 0x670) + Arg2 + Arg2 * 2 * 8, *(uint64_t *)(result + 0x20), (uint32_t)((uint32_t)(result)));
    if (!sign_flag) goto loc_00852574;
loc_008524E6:
    result = CmpUnlockKcb(result, *(uint64_t *)(*(uint64_t *)(result + 0x20) + 0x670) + Arg2 + Arg2 * 2 * 8, *(uint64_t *)(result + 0x20), (uint32_t)((uint32_t)(result)));
    result = CmpUnlockKcb(v_stack_m98, *(uint64_t *)(*(uint64_t *)(result + 0x20) + 0x670) + Arg2 + Arg2 * 2 * 8, *(uint64_t *)(result + 0x20), (uint32_t)((uint32_t)(result)));
    goto loc_00852530;
loc_008524FA:
    *(uint64_t *)(result + 0x58) = (uint32_t)((uint32_t)(result));
    result = CmUnlockHiveSecurity(v_stack_p10, *(uint64_t *)(*(uint64_t *)(result + 0x20) + 0x670) + Arg2 + Arg2 * 2 * 8, *(uint64_t *)(result + 0x20), (uint32_t)((uint32_t)(result)));
    result = CmpUnlockKcb(result, *(uint64_t *)(*(uint64_t *)(result + 0x20) + 0x670) + Arg2 + Arg2 * 2 * 8, *(uint64_t *)(result + 0x20), (uint32_t)((uint32_t)(result)));
    if (((*(uint8_t *)(v_stack_mB0 + 0x8C)) & ((uint8_t)(v_stack_m98))) != 0) goto loc_008525C2;
    result = HvpReleaseCellPaged(v_stack_mB0, v_stack_p48, *(uint64_t *)(result + 0x20), (uint32_t)((uint32_t)(result)));
loc_00852530:
    if (*(uint64_t *)(result + 0x50) != 0) {
        result = CmpDereferenceNameControlBlockWithLock(*(uint64_t *)(result + 0x50), v_stack_p48, *(uint64_t *)(result + 0x20), (uint32_t)((uint32_t)(result)));
    }
    if ((*(uint64_t *)(result + 0x48)) != 0) {
        Arg1 = v_stack_mB8;
        result = CmpDereferenceKeyControlBlockUnsafe(Arg1, v_stack_p48, *(uint64_t *)(result + 0x20), (uint32_t)((uint32_t)(result)));
    }
    if (*(uint64_t *)(result + 0xC0) != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(result + 0xC0), Arg2, *(uint64_t *)(result + 0x20), (uint32_t)((uint32_t)(result)));
    }
    result = CmpFreeKeyControlBlock(result, Arg2, *(uint64_t *)(result + 0x20), (uint32_t)((uint32_t)(result)));
    goto loc_008523C6;
loc_00852574:
    result = CmpAllocateLayerInfoForKcb(result, Arg2, *(uint64_t *)(result + 0x20), (uint32_t)((uint32_t)(result)));
    if (sign_flag) goto loc_008524E6;
    result = CmpReferenceKeyControlBlock(v_stack_m98, Arg2, *(uint64_t *)(result + 0x20), (uint32_t)((uint32_t)(result)));
    result = (uint16_t)((*(uint16_t *)(v_stack_m98 + 0x42)) + 1);
    *(uint16_t *)(result + 0x42) = (uint16_t)(result);
    *(uint64_t *)(*(uint64_t *)(result + 0xC0) + 0x18) = *(uint64_t *)(v_stack_m98 + 0xC0);
    result = (*(uint64_t *)(v_stack_m98 + 0xC0)) + (32);
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x8))) == result) goto loc_00852652;
loc_008525C2:
    result = HvpReleaseCellFlat(3, *(uint64_t *)(result + 0x8), *(uint64_t *)(result + 0x20), (uint32_t)((uint32_t)(result)));
    goto loc_00852530;
loc_008525CF:
    Arg4 = 0;
    v_stack_p20 = (uint32_t)(0xC000009AULL);
    result = KeBugCheckEx(Arg4 + 36 + 45, Arg4 + 36, v_stack_mB8, Arg4);
loc_008525E7:
    result = HvpReleaseCellFlat(Arg4 + 36 + 45, Arg4 + 36, v_stack_mB8, Arg4);
    goto loc_008522A4;
loc_008525F1:
    result = HvpReleaseCellFlat(Arg4 + 36 + 45, Arg4 + 36, v_stack_mB8, Arg4);
    goto loc_008520C8;
loc_008525FB:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x8))) & (0x803FFFFFULL));
    goto loc_00852450;
loc_0085260C:
    result = RtlUpcaseUnicodeChar(Arg4 + 36 + 45, Arg4 + 36, v_stack_mB8, Arg4);
    goto loc_00851EF3;
loc_00852628:
    if (v_stack_p40 == 0) goto loc_00852229;
    result = KeAbPostReleaseEx(result + 48, v_stack_p40, (uint32_t)(0xFFFFULL) - 31, Arg4);
    goto loc_00852229;
loc_00852642:
    result = (uint32_t)(((uint32_t)((uint32_t)(result + 48))) ^ ((uint32_t)(v_stack_p40)));
    result = (uint32_t)((result) & (0x7FE00000ULL));
    result = (uint32_t)((result) ^ ((uint32_t)(result + 48)));
    goto loc_00852450;
loc_00852652:
    *(uint64_t *)(result + 0x30) = result;
    *(uint64_t *)(result + 0x30 + 0x8) = v_stack_p40;
    *(uint64_t *)(v_stack_p40) = result + 48;
    *(uint64_t *)(result + 0x8) = result + 48;
    result = CmpUnlockKcb(result, v_stack_p40, (uint32_t)(0xFFFFULL) - 31, Arg4);
    result = CmpUnlockKcb(v_stack_m98, v_stack_p40, (uint32_t)(0xFFFFULL) - 31, Arg4);
    goto loc_0085245C;
loc_00852675:
    *(uint8_t *)(result + 0x41) = (uint8_t)(v_stack_m98);
    goto loc_0085231A;
loc_0085267E:
    *(uint64_t *)(result + 0x58) = (uint32_t)(0xC000009AULL);
    goto loc_0085227E;
loc_00852687:
    goto loc_008523C6;
loc_00852691:
    local_rsi = (uint16_t)(((uint32_t)(0xC000009AULL)) >> (1));
loc_008526A0:
    if ((uint16_t)(result) == 0) goto loc_00851F0A;
    if ((uint16_t)(local_rsi) == 0) goto loc_00851F0A;
    local_r12 = ((uint32_t)(*(uint32_t *)(result + 0x2C))) + (2);
    result = (*(uint64_t *)(Arg4 + 0x8)) + (2);
    v_stack_mA0 = result;
    v_stack_p40 = (uint16_t)(*(uint16_t *)((uint32_t)(*(uint32_t *)(result + 0x2C))));
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(Arg4 + 0x8)))) != ((uint16_t)(*(uint16_t *)((uint32_t)(*(uint32_t *)(result + 0x2C)))))) goto loc_008526DA;
loc_008526D0:
    local_rdi = (uint16_t)((result) + ((uint16_t)((uint32_t)(0xFFFFULL))));
    local_rsi = (uint16_t)((local_rsi) + ((uint16_t)((uint32_t)(0xFFFFULL))));
    goto loc_008526A0;
loc_008526DA:
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(Arg4 + 0x8)))) < 97) goto loc_008526EA;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(Arg4 + 0x8)))) > 122) goto loc_00852713;
    Arg1 = (uint16_t)((*(uint16_t *)(*(uint64_t *)(Arg4 + 0x8))) + ((uint16_t)((uint32_t)(0xFFFFULL) - 31)));
loc_008526EA:
    if (((uint16_t)(Arg1)) != ((uint16_t)(*(uint16_t *)((uint32_t)(*(uint32_t *)(result + 0x2C)))))) goto loc_008522F6;
    goto loc_008526D0;
loc_008526F9:
    result = CmpUnlockKcb(local_rdi, *(uint16_t *)((uint32_t)(*(uint32_t *)(result + 0x2C))), (uint32_t)(0xFFFFULL) - 31, Arg4);
    result = CmpUnlockKcb(v_stack_m98, *(uint16_t *)((uint32_t)(*(uint32_t *)(result + 0x2C))), (uint32_t)(0xFFFFULL) - 31, Arg4);
    goto loc_00852530;
loc_00852713:
    result = RtlUpcaseUnicodeChar(v_stack_m98, *(uint16_t *)((uint32_t)(*(uint32_t *)(result + 0x2C))), (uint32_t)(0xFFFFULL) - 31, Arg4);
    goto loc_008526EA;
loc_0085272C:
    result = CmpReferenceKeyControlBlockLockNotHeld(v_stack_mB0, v_stack_p40, (uint32_t)(0xFFFFULL) - 31, Arg4);
    local_rsi = 0;
    *(uint64_t *)(v_stack_mA8) = v_stack_mB0;
    goto loc_008523C6;
loc_00852742:
    goto loc_008523C6;
loc_0085274C:
    goto loc_00852530;
loc_00852759:
    result = guard_dispatch_icall(v_stack_mB0, v_stack_p40, (uint32_t)(0xFFFFULL) - 31, Arg4);
    goto loc_008523A9;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xA0` | `32` | `R` |
| `Arg1` | `+ 0x670` | `64` | `R` |
| `Arg1` | `+ 0x678` | `32` | `R` |
| `Arg1` | `+ 0x1048` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00851DB0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
