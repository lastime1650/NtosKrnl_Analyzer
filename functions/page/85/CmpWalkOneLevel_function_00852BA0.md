# CmpWalkOneLevel

- RVA: `0x00852BA0`–`0x00853A67` (길이 `3,783` bytes)
- VA: `0x0000000140852BA0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00069EC0`
- 디코드: `870`개 명령, `3,783/3,783` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **59**; 고유 호출 대상: **31**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00852BE3` → [HvpGetCellContextInitialize](HvpGetCellContextInitialize_function_00855F10.md) (function, `0x00855F10`)
- `0x00852C96` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00852CAF` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x00852D33` → [CmpLockKcbShared](../../pagecmrc/BC/CmpLockKcbShared_function_00BC9A1C.md) (function, `0x00BC9A1C`)
- `0x00852DCC` → [CmpAttachToRegistryProcess](../../pagecmrc/BC/CmpAttachToRegistryProcess_function_00BC98E0.md) (function, `0x00BC98E0`)
- `0x00852E35` → [HvpGetCellFlat](HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x00852E76` → [HvpReleaseCellPaged](HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00852E8B` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00852EAD` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x00852ED5` → [HvpGetCellFlat](HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x00852F1E` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00852F93` → [HvpGetCellFlat](HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x00853052` → [HvpGetCellPaged](HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x0085305C` → [HvpGetCellPaged](HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x00853077` → [HvpMarkCellDirty](HvpMarkCellDirty_function_00858080.md) (function, `0x00858080`)
- `0x00853133` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (function, `0x00BC92C0`)
- `0x008531DB` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x008531F3` → [CmpDeleteHive](../86/CmpDeleteHive_function_0086450C.md) (function, `0x0086450C`)
- `0x00853226` → [CmpDereferenceKeyControlBlock](CmpDereferenceKeyControlBlock_function_00851310.md) (function, `0x00851310`)
- `0x00853259` → [CmListGetNextElement](../../pagecmrc/BC/CmListGetNextElement_function_00BC9940.md) (function, `0x00BC9940`)
- `0x00853274` → [CmEqualTrans](../84/CmEqualTrans_function_0084BF60.md) (function, `0x0084BF60`)
- `0x008532A9` → [CmpTransUowIsEqual](../70/CmpTransUowIsEqual_function_007049CC.md) (function, `0x007049CC`)
- `0x008532D0` → [CmpRecordParseFailure](CmpRecordParseFailure_function_00851280.md) (function, `0x00851280`)
- `0x008532F1` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (function, `0x002638D0`)
- `0x00853314` → [CmpLockHashEntryShared](../97/CmpLockHashEntryShared_function_0097B060.md) (function, `0x0097B060`)
- `0x00853325` → [CmpFindKcbInHashEntryByName](../94/CmpFindKcbInHashEntryByName_function_0094D7A0.md) (function, `0x0094D7A0`)
- `0x0085333B` → [CmpReferenceKeyControlBlockLockNotHeld](../99/CmpReferenceKeyControlBlockLockNotHeld_function_0099F9A0.md) (function, `0x0099F9A0`)
- `0x00853346` → [CmpUnlockHashEntry](../86/CmpUnlockHashEntry_function_00864460.md) (function, `0x00864460`)
- `0x0085337A` → [HvpReleaseCellFlat](HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00853451` → [CmpFindSubKeyInLeafWithStatus](CmpFindSubKeyInLeafWithStatus_function_00853A70.md) (function, `0x00853A70`)
- `0x0085348F` → [HvpReleaseCellPaged](HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x0085349C` → [HvpGetCellPaged](HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x008534CE` → [HvpGetCellFlat](HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x008535B8` → [HvpReleaseCellPaged](HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x008535F3` → [RtlUpcaseUnicodeChar](RtlUpcaseUnicodeChar_function_0085F0F0.md) (function, `0x0085F0F0`)
- `0x0085360D` → [HvpGetCellPaged](HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x0085363A` → [HvpReleaseCellPaged](HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00853658` → [HvpReleaseCellPaged](HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x008536B7` → [HvpReleaseCellFlat](HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x008536DB` → [CmpFindSubKeyInRoot](CmpFindSubKeyInRoot_function_0085D890.md) (function, `0x0085D890`)
- `0x008536FE` → [HvpReleaseCellPaged](HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00853722` → [HvpGetCellFlat](HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x00853746` → [RtlUpcaseUnicodeChar](RtlUpcaseUnicodeChar_function_0085F0F0.md) (function, `0x0085F0F0`)
- `0x00853750` → [HvpReleaseCellFlat](HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x0085375A` → [HvpGetCellPaged](HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x008537A3` → [CmpCreateKeyControlBlock](CmpCreateKeyControlBlock_function_00851DB0.md) (function, `0x00851DB0`)
- `0x008537DF` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00853880` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x008538B8` → [CmpDeleteHive](../86/CmpDeleteHive_function_0086450C.md) (function, `0x0086450C`)
- `0x008538C2` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (function, `0x002638D0`)
- `0x008538D4` → [HvpReleaseCellFlat](HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x008538DE` → [HvpReleaseCellFlat](HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x008538FB` → [RtlUpcaseUnicodeChar](RtlUpcaseUnicodeChar_function_0085F0F0.md) (function, `0x0085F0F0`)
- `0x00853926` → [RtlCompareUnicodeStrings](../97/RtlCompareUnicodeStrings_function_009727E0.md) (function, `0x009727E0`)
- `0x00853948` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0085394E` → [HvpReleaseCellFlat](HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00853987` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x00853997` → [CmpUnlockHashEntry](../86/CmpUnlockHashEntry_function_00864460.md) (function, `0x00864460`)
- `0x00853A17` → [CmpRecordParseFailure](CmpRecordParseFailure_function_00851280.md) (function, `0x00851280`)

### Direct callers
- [CmpDoBuildVirtualStack](../7E/CmpDoBuildVirtualStack_function_007EB4C4.md) at `0x007EB691`
- [CmpDoParseKey](CmpDoParseKey_function_0085F750.md) at `0x00860028`

### Static image references
- `0x00852E59` → RVA `0x00E0EC94` (`.data`; reference)
- `0x00853084` → RVA `0x00E0EC94` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **16**
  - `0x00852C96` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x00852CAF` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x00852D33` → [CmpLockKcbShared](../../pagecmrc/BC/CmpLockKcbShared_function_00BC9A1C.md) (`PAGE` → `PAGECMRC`)
  - `0x00852DCC` → [CmpAttachToRegistryProcess](../../pagecmrc/BC/CmpAttachToRegistryProcess_function_00BC98E0.md) (`PAGE` → `PAGECMRC`)
  - `0x00852E8B` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x00852EAD` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x00852F1E` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00853133` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (`PAGE` → `PAGECMRC`)
  - `0x008531DB` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00853259` → [CmListGetNextElement](../../pagecmrc/BC/CmListGetNextElement_function_00BC9940.md) (`PAGE` → `PAGECMRC`)
  - `0x008532F1` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (`PAGE` → `.text`)
  - `0x008537DF` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x00853880` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x008538C2` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (`PAGE` → `.text`)
  - `0x00853948` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x00853987` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00852BA0  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
00852BA5  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
00852BAA  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
00852BAF  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
00852BB4  55                              push rbp
00852BB5  53                              push rbx
00852BB6  56                              push rsi
00852BB7  57                              push rdi
00852BB8  41 54                           push r12
00852BBA  41 55                           push r13
00852BBC  41 56                           push r14
00852BBE  41 57                           push r15
00852BC0  48 8D 6C 24 F9                  lea rbp, [rsp - 7]
00852BC5  48 81 EC F8 00 00 00            sub rsp, 0xf8
00852BCC  4C 8B E9                        mov r13, rcx
00852BCF  4C 8B E2                        mov r12, rdx
00852BD2  33 D2                           xor edx, edx
00852BD4  48 8D 4D 87                     lea rcx, [rbp - 0x79]
00852BD8  48 89 55 87                     mov qword ptr [rbp - 0x79], rdx
00852BDC  4D 8B F9                        mov r15, r9
00852BDF  48 89 55 BF                     mov qword ptr [rbp - 0x41], rdx
00852BE3  E8 28 33 00 00                  call 0x140855f10
00852BE8  41 0F B7 7D 42                  movzx edi, word ptr [r13 + 0x42]
00852BED  48 C7 C0 FF FF FF FF            mov rax, 0xffffffffffffffff
00852BF4  8B 9D 87 00 00 00               mov ebx, dword ptr [rbp + 0x87]
00852BFA  8B F2                           mov esi, edx
00852BFC  4C 8B 75 77                     mov r14, qword ptr [rbp + 0x77]
00852C00  66 89 44 24 56                  mov word ptr [rsp + 0x56], ax
00852C05  66 FF CF                        dec di
00852C08  48 89 74 24 58                  mov qword ptr [rsp + 0x58], rsi
00852C0D  66 85 FF                        test di, di
00852C10  0F 89 E5 06 00 00               jns 0x1408532fb
00852C16  48 85 F6                        test rsi, rsi
00852C19  0F 85 31 07 00 00               jne 0x140853350
00852C1F  33 D2                           xor edx, edx
00852C21  66 41 C7 47 02 FF FF            mov word ptr [r15 + 2], 0xffff
00852C28  8B FA                           mov edi, edx
00852C2A  48 89 74 24 58                  mov qword ptr [rsp + 0x58], rsi
00852C2F  4C 8B 6D 4F                     mov r13, qword ptr [rbp + 0x4f]
00852C33  66 89 7C 24 54                  mov word ptr [rsp + 0x54], di
00852C38  66 41 3B 7D 42                  cmp di, word ptr [r13 + 0x42]
00852C3D  0F 8F CB 00 00 00               jg 0x140852d0e
00852C43  8B C3                           mov eax, ebx
00852C45  C1 E8 09                        shr eax, 9
00852C48  33 C3                           xor eax, ebx
00852C4A  69 C0 A3 8A 01 00               imul eax, eax, 0x18aa3
00852C50  44 8B F8                        mov r15d, eax
00852C53  49 C1 EF 09                     shr r15, 9
00852C57  8B C8                           mov ecx, eax
00852C59  4C 33 F9                        xor r15, rcx
00852C5C  48 0F BF CF                     movsx rcx, di
00852C60  66 83 FF 02                     cmp di, 2
00852C64  0F 8D 0A 0D 00 00               jge 0x140853974
00852C6A  4D 8B 74 CC 08                  mov r14, qword ptr [r12 + rcx*8 + 8]
00852C6F  4D 8B 76 20                     mov r14, qword ptr [r14 + 0x20]
00852C73  45 33 C0                        xor r8d, r8d
00852C76  33 D2                           xor edx, edx
00852C78  41 8B 8E 78 06 00 00            mov ecx, dword ptr [r14 + 0x678]
00852C7F  49 8B 86 70 06 00 00            mov rax, qword ptr [r14 + 0x670]
00852C86  FF C9                           dec ecx
00852C88  49 23 CF                        and rcx, r15
00852C8B  48 8D 0C 49                     lea rcx, [rcx + rcx*2]
00852C8F  48 8D 34 C8                     lea rsi, [rax + rcx*8]
00852C93  48 8B CE                        mov rcx, rsi
00852C96  E8 95 D5 9B FF                  call 0x140210230
00852C9B  F0 48 0F BA 2E 00               lock bts qword ptr [rsi], 0
00852CA1  4C 8B E8                        mov r13, rax
00852CA4  73 0E                           jae 0x140852cb4
00852CA6  4C 8B C6                        mov r8, rsi
00852CA9  48 8B D0                        mov rdx, rax
00852CAC  48 8B CE                        mov rcx, rsi
00852CAF  E8 DC CF 9B FF                  call 0x14020fc90
00852CB4  4D 85 ED                        test r13, r13
00852CB7  74 05                           je 0x140852cbe
00852CB9  41 C6 45 0A 01                  mov byte ptr [r13 + 0xa], 1
00852CBE  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00852CC7  48 89 46 08                     mov qword ptr [rsi + 8], rax
00852CCB  41 0F 0D 8E 88 10 00 00         prefetchw byte ptr [r14 + 0x1088]
00852CD3  41 8B 86 88 10 00 00            mov eax, dword ptr [r14 + 0x1088]
00852CDA  85 C0                           test eax, eax
00852CDC  0F 84 51 0C 00 00               je 0x140853933
00852CE2  8D 48 01                        lea ecx, [rax + 1]
00852CE5  F0 41 0F B1 8E 88 10 00 00      lock cmpxchg dword ptr [r14 + 0x1088], ecx
00852CEE  75 EA                           jne 0x140852cda
00852CF0  4C 8B 6D 4F                     mov r13, qword ptr [rbp + 0x4f]
00852CF4  66 89 7C 24 56                  mov word ptr [rsp + 0x56], di
00852CF9  66 FF C7                        inc di
00852CFC  66 41 3B 7D 42                  cmp di, word ptr [r13 + 0x42]
00852D01  0F 8E 55 FF FF FF               jle 0x140852c5c
00852D07  48 8B 74 24 58                  mov rsi, qword ptr [rsp + 0x58]
00852D0C  33 D2                           xor edx, edx
00852D0E  41 0F B7 4C 24 02               movzx ecx, word ptr [r12 + 2]
00852D14  0F B7 FA                        movzx edi, dx
00852D17  66 3B D1                        cmp dx, cx
00852D1A  7F 2C                           jg 0x140852d48
00852D1C  0F 1F 40 00                     nop dword ptr [rax]
00852D20  48 0F BF CF                     movsx rcx, di
00852D24  66 83 FF 02                     cmp di, 2
00852D28  0F 8D B1 05 00 00               jge 0x1408532df
00852D2E  49 8B 4C CC 08                  mov rcx, qword ptr [r12 + rcx*8 + 8]
00852D33  E8 E4 6C 37 00                  call 0x140bc9a1c
00852D38  41 0F B7 4C 24 02               movzx ecx, word ptr [r12 + 2]
00852D3E  66 FF C7                        inc di
00852D41  66 3B F9                        cmp di, cx
00852D44  7E DA                           jle 0x140852d20
00852D46  33 D2                           xor edx, edx
00852D48  48 89 55 C7                     mov qword ptr [rbp - 0x39], rdx
00852D4C  66 85 C9                        test cx, cx
00852D4F  0F 88 3E 03 00 00               js 0x140853093
00852D55  48 0F BF D1                     movsx rdx, cx
00852D59  66 83 F9 02                     cmp cx, 2
00852D5D  0F 8D 85 0B 00 00               jge 0x1408538e8
00852D63  49 8B 54 D4 08                  mov rdx, qword ptr [r12 + rdx*8 + 8]
00852D68  66 83 7A 42 00                  cmp word ptr [rdx + 0x42], 0
00852D6D  74 0A                           je 0x140852d79
00852D6F  80 7A 41 01                     cmp byte ptr [rdx + 0x41], 1
00852D73  0F 84 1A 03 00 00               je 0x140853093
00852D79  83 7A 28 FF                     cmp dword ptr [rdx + 0x28], -1
00852D7D  0F 84 E3 02 00 00               je 0x140853066
00852D83  48 8B BD 8F 00 00 00            mov rdi, qword ptr [rbp + 0x8f]
00852D8A  48 85 FF                        test rdi, rdi
00852D8D  0F 85 B0 04 00 00               jne 0x140853243
00852D93  49 8B 95 F0 00 00 00            mov rdx, qword ptr [r13 + 0xf0]
00852D9A  48 85 D2                        test rdx, rdx
00852D9D  0F 85 E3 04 00 00               jne 0x140853286
00852DA3  41 F7 85 B8 00 00 00 00 00 02 00  test dword ptr [r13 + 0xb8], 0x20000
00852DAE  0F 85 3F 0C 00 00               jne 0x1408539f3
00852DB4  48 8B BD 9F 00 00 00            mov rdi, qword ptr [rbp + 0x9f]
00852DBB  8B 87 A0 00 00 00               mov eax, dword ptr [rdi + 0xa0]
00852DC1  A8 01                           test al, 1
00852DC3  75 13                           jne 0x140852dd8
00852DC5  48 8D 8F A8 00 00 00            lea rcx, [rdi + 0xa8]
00852DCC  E8 0F 6B 37 00                  call 0x140bc98e0
00852DD1  83 8F A0 00 00 00 01            or dword ptr [rdi + 0xa0], 1
00852DD8  48 85 F6                        test rsi, rsi
00852DDB  0F 85 85 0B 00 00               jne 0x140853966
00852DE1  33 C0                           xor eax, eax
00852DE3  44 0F B7 F8                     movzx r15d, ax
00852DE7  8B 7D 7F                        mov edi, dword ptr [rbp + 0x7f]
00852DEA  66 44 89 7C 24 60               mov word ptr [rsp + 0x60], r15w
00852DF0  66 45 3B 7D 42                  cmp r15w, word ptr [r13 + 0x42]
00852DF5  0F 8F E5 02 00 00               jg 0x1408530e0
00852DFB  49 0F BF CF                     movsx rcx, r15w
00852DFF  66 41 83 FF 02                  cmp r15w, 2
00852E04  0F 8D F8 05 00 00               jge 0x140853402
00852E0A  4D 8B 6C CC 08                  mov r13, qword ptr [r12 + rcx*8 + 8]
00852E0F  41 8B 55 28                     mov edx, dword ptr [r13 + 0x28]
00852E13  4C 89 6D D7                     mov qword ptr [rbp - 0x29], r13
00852E17  83 FA FF                        cmp edx, -1
00852E1A  0F 84 64 05 00 00               je 0x140853384
00852E20  49 8B 4D 20                     mov rcx, qword ptr [r13 + 0x20]
00852E24  4C 8D 45 87                     lea r8, [rbp - 0x79]
00852E28  F6 81 8C 00 00 00 01            test byte ptr [rcx + 0x8c], 1
00852E2F  0F 84 1D 02 00 00               je 0x140853052
00852E35  E8 26 1E 00 00                  call 0x140854c60
00852E3A  49 8B 4D 20                     mov rcx, qword ptr [r13 + 0x20]
00852E3E  48 8B F0                        mov rsi, rax
00852E41  48 89 45 A7                     mov qword ptr [rbp - 0x59], rax
00852E45  F7 81 A0 00 00 00 01 80 00 00   test dword ptr [rcx + 0xa0], 0x8001
00852E4F  0F 85 CE 00 00 00               jne 0x140852f23
00852E55  0F B6 40 0C                     movzx eax, byte ptr [rax + 0xc]
00852E59  84 05 35 BE 5B 00               test byte ptr [rip + 0x5bbe35], al
00852E5F  0F 85 BE 00 00 00               jne 0x140852f23
00852E65  F6 81 8C 00 00 00 01            test byte ptr [rcx + 0x8c], 1
00852E6C  48 8D 55 87                     lea rdx, [rbp - 0x79]
00852E70  0F 85 04 05 00 00               jne 0x14085337a
00852E76  E8 C5 30 00 00                  call 0x140855f40
00852E7B  49 8B 75 20                     mov rsi, qword ptr [r13 + 0x20]
00852E7F  45 33 C0                        xor r8d, r8d
00852E82  48 83 C6 48                     add rsi, 0x48
00852E86  33 D2                           xor edx, edx
00852E88  48 8B CE                        mov rcx, rsi
00852E8B  E8 A0 D3 9B FF                  call 0x140210230
00852E90  4C 8B F0                        mov r14, rax
00852E93  41 BF 11 00 00 00               mov r15d, 0x11
00852E99  33 C0                           xor eax, eax
00852E9B  F0 4C 0F B1 3E                  lock cmpxchg qword ptr [rsi], r15
00852EA0  74 10                           je 0x140852eb2
00852EA2  4C 8B CE                        mov r9, rsi
00852EA5  4D 8B C6                        mov r8, r14
00852EA8  33 D2                           xor edx, edx
00852EAA  48 8B CE                        mov rcx, rsi
00852EAD  E8 9A D5 9B FF                  call 0x14021044c
00852EB2  4D 85 F6                        test r14, r14
00852EB5  74 05                           je 0x140852ebc
00852EB7  41 C6 46 0A 01                  mov byte ptr [r14 + 0xa], 1
00852EBC  49 8B 4D 20                     mov rcx, qword ptr [r13 + 0x20]
00852EC0  4C 8D 45 87                     lea r8, [rbp - 0x79]
00852EC4  41 8B 55 28                     mov edx, dword ptr [r13 + 0x28]
00852EC8  F6 81 8C 00 00 00 01            test byte ptr [rcx + 0x8c], 1
00852ECF  0F 84 87 01 00 00               je 0x14085305c
00852ED5  E8 86 1D 00 00                  call 0x140854c60
00852EDA  49 8B 4D 20                     mov rcx, qword ptr [r13 + 0x20]
00852EDE  48 8B F0                        mov rsi, rax
00852EE1  41 8B 55 28                     mov edx, dword ptr [r13 + 0x28]
00852EE5  48 89 45 A7                     mov qword ptr [rbp - 0x59], rax
00852EE9  F7 81 A0 00 00 00 01 80 00 00   test dword ptr [rcx + 0xa0], 0x8001
00852EF3  75 10                           jne 0x140852f05
00852EF5  0F B6 40 0C                     movzx eax, byte ptr [rax + 0xc]
00852EF9  84 05 95 BD 5B 00               test byte ptr [rip + 0x5bbd95], al
00852EFF  0F 84 69 01 00 00               je 0x14085306e
00852F05  49 8B 75 20                     mov rsi, qword ptr [r13 + 0x20]
00852F09  49 8B C7                        mov rax, r15
00852F0C  33 C9                           xor ecx, ecx
00852F0E  F0 48 0F B1 4E 48               lock cmpxchg qword ptr [rsi + 0x48], rcx
00852F14  0F 85 69 0A 00 00               jne 0x140853983
00852F1A  48 8D 4E 48                     lea rcx, [rsi + 0x48]
00852F1E  E8 DD E6 A8 FF                  call 0x1402e1600
00852F23  4D 8B 6D 20                     mov r13, qword ptr [r13 + 0x20]
00852F27  33 D2                           xor edx, edx
00852F29  41 BF 34 00 00 C0               mov r15d, 0xc0000034
00852F2F  4C 89 6D CF                     mov qword ptr [rbp - 0x31], r13
00852F33  B9 FF FF FF FF                  mov ecx, 0xffffffff
00852F38  44 89 7C 24 50                  mov dword ptr [rsp + 0x50], r15d
00852F3D  89 54 24 6C                     mov dword ptr [rsp + 0x6c], edx
00852F41  44 8B E2                        mov r12d, edx
00852F44  89 54 24 64                     mov dword ptr [rsp + 0x64], edx
00852F48  89 55 B7                        mov dword ptr [rbp - 0x49], edx
00852F4B  89 4D 9F                        mov dword ptr [rbp - 0x61], ecx
00852F4E  C7 44 24 68 FF FF FF FF         mov dword ptr [rsp + 0x68], 0xffffffff
00852F56  44 89 65 8F                     mov dword ptr [rbp - 0x71], r12d
00852F5A  45 3B A5 D8 00 00 00            cmp r12d, dword ptr [r13 + 0xd8]
00852F61  0F 83 D8 06 00 00               jae 0x14085363f
00852F67  48 8B 4D A7                     mov rcx, qword ptr [rbp - 0x59]
00852F6B  41 8B C4                        mov eax, r12d
00852F6E  83 7C 81 14 00                  cmp dword ptr [rcx + rax*4 + 0x14], 0
00852F73  0F 84 1B 05 00 00               je 0x140853494
00852F79  41 F6 85 8C 00 00 00 01         test byte ptr [r13 + 0x8c], 1
00852F81  4C 8D 44 24 68                  lea r8, [rsp + 0x68]
00852F86  8B 54 81 1C                     mov edx, dword ptr [rcx + rax*4 + 0x1c]
00852F8A  49 8B CD                        mov rcx, r13
00852F8D  0F 84 09 05 00 00               je 0x14085349c
00852F93  E8 C8 1C 00 00                  call 0x140854c60
00852F98  4C 8B F0                        mov r14, rax
00852F9B  48 85 C0                        test rax, rax
00852F9E  0F 84 8F 07 00 00               je 0x140853733
00852FA4  B8 72 69 00 00                  mov eax, 0x6972
00852FA9  66 41 39 06                     cmp word ptr [r14], ax
00852FAD  0F 84 11 07 00 00               je 0x1408536c4
00852FB3  B8 6C 68 00 00                  mov eax, 0x686c
00852FB8  66 41 39 06                     cmp word ptr [r14], ax
00852FBC  0F 85 6F 04 00 00               jne 0x140853431
00852FC2  4C 8B 65 77                     mov r12, qword ptr [rbp + 0x77]
00852FC6  33 C9                           xor ecx, ecx
00852FC8  44 8B F9                        mov r15d, ecx
00852FCB  41 0F 10 04 24                  movups xmm0, xmmword ptr [r12]
00852FD0  66 0F 7E C0                     movd eax, xmm0
00852FD4  0F 11 45 E7                     movups xmmword ptr [rbp - 0x19], xmm0
00852FD8  66 83 F8 02                     cmp ax, 2
00852FDC  72 40                           jb 0x14085301e
00852FDE  48 8B 75 EF                     mov rsi, qword ptr [rbp - 0x11]
00852FE2  44 0F B7 E0                     movzx r12d, ax
00852FE6  49 D1 EC                        shr r12, 1
00852FE9  0F B7 06                        movzx eax, word ptr [rsi]
00852FEC  66 83 F8 61                     cmp ax, 0x61
00852FF0  72 0E                           jb 0x140853000
00852FF2  66 83 F8 7A                     cmp ax, 0x7a
00852FF6  0F 87 47 07 00 00               ja 0x140853743
00852FFC  66 83 E8 20                     sub ax, 0x20
00853000  45 6B FF 25                     imul r15d, r15d, 0x25
00853004  48 83 C6 02                     add rsi, 2
00853008  0F B7 C0                        movzx eax, ax
0085300B  44 03 F8                        add r15d, eax
0085300E  49 83 EC 01                     sub r12, 1
00853012  75 D5                           jne 0x140852fe9
00853014  4C 8B 65 77                     mov r12, qword ptr [rbp + 0x77]
00853018  33 C9                           xor ecx, ecx
0085301A  48 89 75 EF                     mov qword ptr [rbp - 0x11], rsi
0085301E  C7 44 24 64 FF FF FF FF         mov dword ptr [rsp + 0x64], 0xffffffff
00853026  0F B7 F1                        movzx esi, cx
00853029  0F 1F 80 00 00 00 00            nop dword ptr [rax]
00853030  66 41 3B 76 02                  cmp si, word ptr [r14 + 2]
00853035  0F 83 E5 03 00 00               jae 0x140853420
0085303B  0F B7 C6                        movzx eax, si
0085303E  45 3B 7C C6 08                  cmp r15d, dword ptr [r14 + rax*8 + 8]
00853043  0F 84 5D 04 00 00               je 0x1408534a6
00853049  4C 8B 65 77                     mov r12, qword ptr [rbp + 0x77]
0085304D  66 FF C6                        inc si
00853050  EB DE                           jmp 0x140853030
00853052  E8 59 1C 00 00                  call 0x140854cb0
00853057  E9 DE FD FF FF                  jmp 0x140852e3a
0085305C  E8 4F 1C 00 00                  call 0x140854cb0
00853061  E9 74 FE FF FF                  jmp 0x140852eda
00853066  66 FF C9                        dec cx
00853069  E9 DE FC FF FF                  jmp 0x140852d4c
0085306E  41 B9 01 00 00 00               mov r9d, 1
00853074  45 33 C0                        xor r8d, r8d
00853077  E8 04 50 00 00                  call 0x140858080
0085307C  85 C0                           test eax, eax
0085307E  0F 88 81 FE FF FF               js 0x140852f05
00853084  0F B6 05 09 BC 5B 00            movzx eax, byte ptr [rip + 0x5bbc09]
0085308B  08 46 0C                        or byte ptr [rsi + 0xc], al
0085308E  E9 72 FE FF FF                  jmp 0x140852f05
00853093  48 8B 8D 9F 00 00 00            mov rcx, qword ptr [rbp + 0x9f]
0085309A  41 BF 34 00 00 C0               mov r15d, 0xc0000034
008530A0  44 89 7C 24 50                  mov dword ptr [rsp + 0x50], r15d
008530A5  48 85 C9                        test rcx, rcx
008530A8  0F 84 27 02 00 00               je 0x1408532d5
008530AE  0F B6 81 AA 01 00 00            movzx eax, byte ptr [rcx + 0x1aa]
008530B5  4C 8B 6C 24 58                  mov r13, qword ptr [rsp + 0x58]
008530BA  3C 04                           cmp al, 4
008530BC  73 51                           jae 0x14085310f
008530BE  44 89 BC C1 AC 01 00 00         mov dword ptr [rcx + rax*8 + 0x1ac], r15d
008530C6  0F B6 81 AA 01 00 00            movzx eax, byte ptr [rcx + 0x1aa]
008530CD  C7 84 C1 B0 01 00 00 00 02 05 00  mov dword ptr [rcx + rax*8 + 0x1b0], 0x50200
008530D8  FE 81 AA 01 00 00               inc byte ptr [rcx + 0x1aa]
008530DE  EB 2F                           jmp 0x14085310f
008530E0  0F B6 85 97 00 00 00            movzx eax, byte ptr [rbp + 0x97]
008530E7  84 C0                           test al, al
008530E9  0F 85 6C 09 00 00               jne 0x140853a5b
008530EF  48 8B 4D 6F                     mov rcx, qword ptr [rbp + 0x6f]
008530F3  0F 95 C0                        setne al
008530F6  45 33 FF                        xor r15d, r15d
008530F9  45 8B EF                        mov r13d, r15d
008530FC  4C 89 7C 24 58                  mov qword ptr [rsp + 0x58], r15
00853101  44 89 7C 24 50                  mov dword ptr [rsp + 0x50], r15d
00853106  88 01                           mov byte ptr [rcx], al
00853108  48 8B 45 5F                     mov rax, qword ptr [rbp + 0x5f]
0085310C  48 89 30                        mov qword ptr [rax], rsi
0085310F  33 C0                           xor eax, eax
00853111  0F B7 F8                        movzx edi, ax
00853114  66 41 3B 44 24 02               cmp ax, word ptr [r12 + 2]
0085311A  7F 27                           jg 0x140853143
0085311C  0F 1F 40 00                     nop dword ptr [rax]
00853120  48 0F BF CF                     movsx rcx, di
00853124  66 83 FF 02                     cmp di, 2
00853128  0F 8D E3 02 00 00               jge 0x140853411
0085312E  49 8B 4C CC 08                  mov rcx, qword ptr [r12 + rcx*8 + 8]
00853133  E8 88 61 37 00                  call 0x140bc92c0
00853138  66 FF C7                        inc di
0085313B  66 41 3B 7C 24 02               cmp di, word ptr [r12 + 2]
00853141  7E DD                           jle 0x140853120
00853143  48 0F BF 54 24 54               movsx rdx, word ptr [rsp + 0x54]
00853149  66 3B 54 24 56                  cmp dx, word ptr [rsp + 0x56]
0085314E  0F 8F CA 00 00 00               jg 0x14085321e
00853154  8B C3                           mov eax, ebx
00853156  4C 8D 34 D5 F0 FF FF FF         lea r14, [rdx*8 - 0x10]
0085315E  C1 E8 09                        shr eax, 9
00853161  33 C3                           xor eax, ebx
00853163  69 C0 A3 8A 01 00               imul eax, eax, 0x18aa3
00853169  8B F0                           mov esi, eax
0085316B  48 C1 EE 09                     shr rsi, 9
0085316F  8B C8                           mov ecx, eax
00853171  48 33 F1                        xor rsi, rcx
00853174  45 33 ED                        xor r13d, r13d
00853177  4D 8D 7D FF                     lea r15, [r13 - 1]
0085317B  66 83 FA 02                     cmp dx, 2
0085317F  0F 8D D3 07 00 00               jge 0x140853958
00853185  4B 8B 7C 34 18                  mov rdi, qword ptr [r12 + r14 + 0x18]
0085318A  48 8B 7F 20                     mov rdi, qword ptr [rdi + 0x20]
0085318E  8B 8F 78 06 00 00               mov ecx, dword ptr [rdi + 0x678]
00853194  48 8B 87 70 06 00 00            mov rax, qword ptr [rdi + 0x670]
0085319B  FF C9                           dec ecx
0085319D  48 23 CE                        and rcx, rsi
008531A0  48 8D 0C 49                     lea rcx, [rcx + rcx*2]
008531A4  48 8D 1C C8                     lea rbx, [rax + rcx*8]
008531A8  4C 89 6B 08                     mov qword ptr [rbx + 8], r13
008531AC  0F 0D 0B                        prefetchw byte ptr [rbx]
008531AF  48 8B 03                        mov rax, qword ptr [rbx]
008531B2  48 8B C8                        mov rcx, rax
008531B5  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
008531B9  48 83 F9 10                     cmp rcx, 0x10
008531BD  48 8D 50 F0                     lea rdx, [rax - 0x10]
008531C1  49 0F 46 D5                     cmovbe rdx, r13
008531C5  A8 02                           test al, 2
008531C7  0F 85 21 01 00 00               jne 0x1408532ee
008531CD  F0 48 0F B1 13                  lock cmpxchg qword ptr [rbx], rdx
008531D2  0F 85 16 01 00 00               jne 0x1408532ee
008531D8  48 8B CB                        mov rcx, rbx
008531DB  E8 20 E4 A8 FF                  call 0x1402e1600
008531E0  41 8B C7                        mov eax, r15d
008531E3  F0 0F C1 87 88 10 00 00         lock xadd dword ptr [rdi + 0x1088], eax
008531EB  83 F8 01                        cmp eax, 1
008531EE  75 08                           jne 0x1408531f8
008531F0  48 8B CF                        mov rcx, rdi
008531F3  E8 14 13 01 00                  call 0x14086450c
008531F8  0F B7 54 24 54                  movzx edx, word ptr [rsp + 0x54]
008531FD  49 83 C6 08                     add r14, 8
00853201  66 FF C2                        inc dx
00853204  66 89 54 24 54                  mov word ptr [rsp + 0x54], dx
00853209  66 3B 54 24 56                  cmp dx, word ptr [rsp + 0x56]
0085320E  0F 8E 67 FF FF FF               jle 0x14085317b
00853214  44 8B 7C 24 50                  mov r15d, dword ptr [rsp + 0x50]
00853219  4C 8B 6C 24 58                  mov r13, qword ptr [rsp + 0x58]
0085321E  4D 85 ED                        test r13, r13
00853221  74 08                           je 0x14085322b
00853223  49 8B CD                        mov rcx, r13
00853226  E8 E5 E0 FF FF                  call 0x140851310
0085322B  41 8B C7                        mov eax, r15d
0085322E  48 81 C4 F8 00 00 00            add rsp, 0xf8
00853235  41 5F                           pop r15
00853237  41 5E                           pop r14
00853239  41 5D                           pop r13
0085323B  41 5C                           pop r12
0085323D  5F                              pop rdi
0085323E  5E                              pop rsi
0085323F  5B                              pop rbx
00853240  5D                              pop rbp
00853241  C3                              ret
00853242  CC                              int3
00853243  4D 8B 4C 24 08                  mov r9, qword ptr [r12 + 8]
00853248  41 B8 20 00 00 00               mov r8d, 0x20
0085324E  48 8D 55 C7                     lea rdx, [rbp - 0x39]
00853252  49 8D 89 D0 00 00 00            lea rcx, [r9 + 0xd0]
00853259  E8 E2 66 37 00                  call 0x140bc9940
0085325E  48 85 C0                        test rax, rax
00853261  0F 84 2C FB FF FF               je 0x140852d93
00853267  83 78 44 02                     cmp dword ptr [rax + 0x44], 2
0085326B  75 DB                           jne 0x140853248
0085326D  48 8B 48 38                     mov rcx, qword ptr [rax + 0x38]
00853271  48 8B D7                        mov rdx, rdi
00853274  E8 E7 8C FF FF                  call 0x14084bf60
00853279  84 C0                           test al, al
0085327B  0F 84 12 FB FF FF               je 0x140852d93
00853281  E9 0D FE FF FF                  jmp 0x140853093
00853286  48 85 FF                        test rdi, rdi
00853289  74 2B                           je 0x1408532b6
0085328B  48 3B FA                        cmp rdi, rdx
0085328E  0F 84 0F FB FF FF               je 0x140852da3
00853294  48 8B 4F 38                     mov rcx, qword ptr [rdi + 0x38]
00853298  48 85 C9                        test rcx, rcx
0085329B  0F 85 A2 07 00 00               jne 0x140853a43
008532A1  48 83 C2 58                     add rdx, 0x58
008532A5  48 8D 4F 58                     lea rcx, [rdi + 0x58]
008532A9  E8 1E 17 EB FF                  call 0x1407049cc
008532AE  84 C0                           test al, al
008532B0  0F 85 ED FA FF FF               jne 0x140852da3
008532B6  41 BF 34 00 00 C0               mov r15d, 0xc0000034
008532BC  BA 00 03 05 00                  mov edx, 0x50300
008532C1  44 89 7C 24 50                  mov dword ptr [rsp + 0x50], r15d
008532C6  48 8B 8D 9F 00 00 00            mov rcx, qword ptr [rbp + 0x9f]
008532CD  45 8B C7                        mov r8d, r15d
008532D0  E8 AB DF FF FF                  call 0x140851280
008532D5  4C 8B 6C 24 58                  mov r13, qword ptr [rsp + 0x58]
008532DA  E9 30 FE FF FF                  jmp 0x14085310f
008532DF  49 8B 44 24 18                  mov rax, qword ptr [r12 + 0x18]
008532E4  48 8B 4C C8 F0                  mov rcx, qword ptr [rax + rcx*8 - 0x10]
008532E9  E9 45 FA FF FF                  jmp 0x140852d33
008532EE  48 8B CB                        mov rcx, rbx
008532F1  E8 DA 05 A1 FF                  call 0x1402638d0
008532F6  E9 DD FE FF FF                  jmp 0x1408531d8
008532FB  48 0F BF F7                     movsx rsi, di
008532FF  66 83 FF 02                     cmp di, 2
00853303  0F 8D DB 06 00 00               jge 0x1408539e4
00853309  49 8B 74 F4 08                  mov rsi, qword ptr [r12 + rsi*8 + 8]
0085330E  48 8B 4E 20                     mov rcx, qword ptr [rsi + 0x20]
00853312  8B D3                           mov edx, ebx
00853314  E8 47 7D 12 00                  call 0x14097b060
00853319  48 8B 4E 20                     mov rcx, qword ptr [rsi + 0x20]
0085331D  4D 8B CE                        mov r9, r14
00853320  4C 8B C6                        mov r8, rsi
00853323  8B D3                           mov edx, ebx
00853325  E8 76 A4 0F 00                  call 0x14094d7a0
0085332A  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
0085332F  48 85 C0                        test rax, rax
00853332  0F 84 59 06 00 00               je 0x140853991
00853338  48 8B C8                        mov rcx, rax
0085333B  E8 60 C6 14 00                  call 0x14099f9a0
00853340  48 8B 4E 20                     mov rcx, qword ptr [rsi + 0x20]
00853344  8B D3                           mov edx, ebx
00853346  E8 15 11 01 00                  call 0x140864460
0085334B  48 8B 74 24 58                  mov rsi, qword ptr [rsp + 0x58]
00853350  0F B7 46 42                     movzx eax, word ptr [rsi + 0x42]
00853354  66 41 89 47 02                  mov word ptr [r15 + 2], ax
00853359  48 0F BF 4E 42                  movsx rcx, word ptr [rsi + 0x42]
0085335E  66 85 C9                        test cx, cx
00853361  0F 85 3F 06 00 00               jne 0x1408539a6
00853367  49 89 74 CF 08                  mov qword ptr [r15 + rcx*8 + 8], rsi
0085336C  0F B7 7E 42                     movzx edi, word ptr [rsi + 0x42]
00853370  66 FF C7                        inc di
00853373  33 D2                           xor edx, edx
00853375  E9 B5 F8 FF FF                  jmp 0x140852c2f
0085337A  E8 A1 98 00 00                  call 0x14085cc20
0085337F  E9 F7 FA FF FF                  jmp 0x140852e7b
00853384  41 BE FF FF FF FF               mov r14d, 0xffffffff
0085338A  EB 0F                           jmp 0x14085339b
0085338C  41 BE FF FF FF FF               mov r14d, 0xffffffff
00853392  48 8B 74 24 58                  mov rsi, qword ptr [rsp + 0x58]
00853397  4C 8B 65 57                     mov r12, qword ptr [rbp + 0x57]
0085339B  48 8B 45 4F                     mov rax, qword ptr [rbp + 0x4f]
0085339F  66 83 78 42 00                  cmp word ptr [rax + 0x42], 0
008533A4  0F 85 CA 03 00 00               jne 0x140853774
008533AA  80 BD 97 00 00 00 00            cmp byte ptr [rbp + 0x97], 0
008533B1  0F 85 BD 03 00 00               jne 0x140853774
008533B7  48 8B 8D 9F 00 00 00            mov rcx, qword ptr [rbp + 0x9f]
008533BE  41 BF 34 00 00 C0               mov r15d, 0xc0000034
008533C4  4C 8B 6C 24 58                  mov r13, qword ptr [rsp + 0x58]
008533C9  44 89 7C 24 50                  mov dword ptr [rsp + 0x50], r15d
008533CE  0F B6 81 AA 01 00 00            movzx eax, byte ptr [rcx + 0x1aa]
008533D5  3C 04                           cmp al, 4
008533D7  0F 83 32 FD FF FF               jae 0x14085310f
008533DD  44 89 BC C1 AC 01 00 00         mov dword ptr [rcx + rax*8 + 0x1ac], r15d
008533E5  0F B6 81 AA 01 00 00            movzx eax, byte ptr [rcx + 0x1aa]
008533EC  C7 84 C1 B0 01 00 00 00 06 05 00  mov dword ptr [rcx + rax*8 + 0x1b0], 0x50600
008533F7  FE 81 AA 01 00 00               inc byte ptr [rcx + 0x1aa]
008533FD  E9 0D FD FF FF                  jmp 0x14085310f
00853402  49 8B 44 24 18                  mov rax, qword ptr [r12 + 0x18]
00853407  4C 8B 6C C8 F0                  mov r13, qword ptr [rax + rcx*8 - 0x10]
0085340C  E9 FE F9 FF FF                  jmp 0x140852e0f
00853411  49 8B 44 24 18                  mov rax, qword ptr [r12 + 0x18]
00853416  48 8B 4C C8 F0                  mov rcx, qword ptr [rax + rcx*8 - 0x10]
0085341B  E9 13 FD FF FF                  jmp 0x140853133
00853420  44 8B 65 8F                     mov r12d, dword ptr [rbp - 0x71]
00853424  41 BF 34 00 00 C0               mov r15d, 0xc0000034
0085342A  44 89 7C 24 50                  mov dword ptr [rsp + 0x50], r15d
0085342F  EB 48                           jmp 0x140853479
00853431  4C 8B 45 77                     mov r8, qword ptr [rbp + 0x77]
00853435  48 8D 45 B7                     lea rax, [rbp - 0x49]
00853439  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0085343E  45 33 C9                        xor r9d, r9d
00853441  48 8D 44 24 64                  lea rax, [rsp + 0x64]
00853446  49 8B D6                        mov rdx, r14
00853449  49 8B CD                        mov rcx, r13
0085344C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00853451  E8 1A 06 00 00                  call 0x140853a70
00853456  B9 00 00 00 80                  mov ecx, 0x80000000
0085345B  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
0085345F  44 8B F8                        mov r15d, eax
00853462  03 C1                           add eax, ecx
00853464  85 C1                           test ecx, eax
00853466  0F 84 74 01 00 00               je 0x1408535e0
0085346C  8B 4C 24 64                     mov ecx, dword ptr [rsp + 0x64]
00853470  83 F9 FF                        cmp ecx, -1
00853473  0F 85 9E 01 00 00               jne 0x140853617
00853479  41 F6 85 8C 00 00 00 01         test byte ptr [r13 + 0x8c], 1
00853481  48 8D 54 24 68                  lea rdx, [rsp + 0x68]
00853486  49 8B CD                        mov rcx, r13
00853489  0F 85 28 02 00 00               jne 0x1408536b7
0085348F  E8 AC 2A 00 00                  call 0x140855f40
00853494  41 FF C4                        inc r12d
00853497  E9 BA FA FF FF                  jmp 0x140852f56
0085349C  E8 0F 18 00 00                  call 0x140854cb0
008534A1  E9 F2 FA FF FF                  jmp 0x140852f98
008534A6  41 F6 85 8C 00 00 00 01         test byte ptr [r13 + 0x8c], 1
008534AE  4C 8D 45 97                     lea r8, [rbp - 0x69]
008534B2  41 8B 54 C6 04                  mov edx, dword ptr [r14 + rax*8 + 4]
008534B7  49 8B CD                        mov rcx, r13
008534BA  C7 45 97 FF FF FF FF            mov dword ptr [rbp - 0x69], 0xffffffff
008534C1  C7 45 9B 00 00 00 00            mov dword ptr [rbp - 0x65], 0
008534C8  0F 84 3F 01 00 00               je 0x14085360d
008534CE  E8 8D 17 00 00                  call 0x140854c60
008534D3  48 8B C8                        mov rcx, rax
008534D6  48 85 C0                        test rax, rax
008534D9  0F 84 EA 03 00 00               je 0x1408538c9
008534DF  F6 40 02 20                     test byte ptr [rax + 2], 0x20
008534E3  4C 8D 50 4C                     lea r10, [rax + 0x4c]
008534E7  0F 84 1C 04 00 00               je 0x140853909
008534ED  41 0F B7 14 24                  movzx edx, word ptr [r12]
008534F2  4D 8B 44 24 08                  mov r8, qword ptr [r12 + 8]
008534F7  0F B7 40 48                     movzx eax, word ptr [rax + 0x48]
008534FB  66 D1 EA                        shr dx, 1
008534FE  66 89 44 24 50                  mov word ptr [rsp + 0x50], ax
00853503  66 89 54 24 70                  mov word ptr [rsp + 0x70], dx
00853508  66 85 D2                        test dx, dx
0085350B  0F 84 84 00 00 00               je 0x140853595
00853511  66 85 C0                        test ax, ax
00853514  74 7F                           je 0x140853595
00853516  45 0F B7 20                     movzx r12d, word ptr [r8]
0085351A  49 83 C0 02                     add r8, 2
0085351E  45 0F B6 2A                     movzx r13d, byte ptr [r10]
00853522  49 FF C2                        inc r10
00853525  4C 89 45 DF                     mov qword ptr [rbp - 0x21], r8
00853529  4C 89 55 AF                     mov qword ptr [rbp - 0x51], r10
0085352D  66 45 3B E5                     cmp r12w, r13w
00853531  74 52                           je 0x140853585
00853533  66 41 83 FC 61                  cmp r12w, 0x61
00853538  0F 82 BE 00 00 00               jb 0x1408535fc
0085353E  66 41 83 FC 7A                  cmp r12w, 0x7a
00853543  0F 87 A6 00 00 00               ja 0x1408535ef
00853549  B8 E0 FF 00 00                  mov eax, 0xffe0
0085354E  66 44 03 E0                     add r12w, ax
00853552  41 83 FD 61                     cmp r13d, 0x61
00853556  72 0E                           jb 0x140853566
00853558  41 83 FD 7A                     cmp r13d, 0x7a
0085355C  0F 87 95 03 00 00               ja 0x1408538f7
00853562  66 44 03 E8                     add r13w, ax
00853566  41 0F B7 C5                     movzx eax, r13w
0085356A  45 0F B7 E4                     movzx r12d, r12w
0085356E  44 2B E0                        sub r12d, eax
00853571  75 2C                           jne 0x14085359f
00853573  0F B7 54 24 70                  movzx edx, word ptr [rsp + 0x70]
00853578  0F B7 44 24 50                  movzx eax, word ptr [rsp + 0x50]
0085357D  4C 8B 45 DF                     mov r8, qword ptr [rbp - 0x21]
00853581  4C 8B 55 AF                     mov r10, qword ptr [rbp - 0x51]
00853585  B9 FF FF 00 00                  mov ecx, 0xffff
0085358A  66 03 D1                        add dx, cx
0085358D  66 03 C1                        add ax, cx
00853590  E9 69 FF FF FF                  jmp 0x1408534fe
00853595  0F B7 C0                        movzx eax, ax
00853598  44 0F B7 E2                     movzx r12d, dx
0085359C  44 2B E0                        sub r12d, eax
0085359F  4C 8B 6D CF                     mov r13, qword ptr [rbp - 0x31]
008535A3  41 F6 85 8C 00 00 00 01         test byte ptr [r13 + 0x8c], 1
008535AB  48 8D 55 97                     lea rdx, [rbp - 0x69]
008535AF  49 8B CD                        mov rcx, r13
008535B2  0F 85 98 01 00 00               jne 0x140853750
008535B8  E8 83 29 00 00                  call 0x140855f40
008535BD  45 85 E4                        test r12d, r12d
008535C0  75 44                           jne 0x140853606
008535C2  44 8B 65 8F                     mov r12d, dword ptr [rbp - 0x71]
008535C6  0F B7 C6                        movzx eax, si
008535C9  41 8B 4C C6 04                  mov ecx, dword ptr [r14 + rax*8 + 4]
008535CE  33 C0                           xor eax, eax
008535D0  44 8B F8                        mov r15d, eax
008535D3  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
008535D7  89 4C 24 64                     mov dword ptr [rsp + 0x64], ecx
008535DB  E9 90 FE FF FF                  jmp 0x140853470
008535E0  41 81 FF 34 00 00 C0            cmp r15d, 0xc0000034
008535E7  0F 84 7F FE FF FF               je 0x14085346c
008535ED  EB 35                           jmp 0x140853624
008535EF  41 0F B7 CC                     movzx ecx, r12w
008535F3  E8 F8 BA 00 00                  call 0x14085f0f0
008535F8  44 0F B7 E0                     movzx r12d, ax
008535FC  B8 E0 FF 00 00                  mov eax, 0xffe0
00853601  E9 4C FF FF FF                  jmp 0x140853552
00853606  33 C9                           xor ecx, ecx
00853608  E9 3C FA FF FF                  jmp 0x140853049
0085360D  E8 9E 16 00 00                  call 0x140854cb0
00853612  E9 BC FE FF FF                  jmp 0x1408534d3
00853617  33 C0                           xor eax, eax
00853619  89 4D 9F                        mov dword ptr [rbp - 0x61], ecx
0085361C  44 8B F8                        mov r15d, eax
0085361F  44 89 7C 24 50                  mov dword ptr [rsp + 0x50], r15d
00853624  41 F6 85 8C 00 00 00 01         test byte ptr [r13 + 0x8c], 1
0085362C  48 8D 54 24 68                  lea rdx, [rsp + 0x68]
00853631  49 8B CD                        mov rcx, r13
00853634  0F 85 9A 02 00 00               jne 0x1408538d4
0085363A  E8 01 29 00 00                  call 0x140855f40
0085363F  4C 8B 6D D7                     mov r13, qword ptr [rbp - 0x29]
00853643  48 8D 55 87                     lea rdx, [rbp - 0x79]
00853647  49 8B 4D 20                     mov rcx, qword ptr [r13 + 0x20]
0085364B  F6 81 8C 00 00 00 01            test byte ptr [rcx + 0x8c], 1
00853652  0F 85 86 02 00 00               jne 0x1408538de
00853658  E8 E3 28 00 00                  call 0x140855f40
0085365D  41 81 FF 34 00 00 C0            cmp r15d, 0xc0000034
00853664  0F 84 22 FD FF FF               je 0x14085338c
0085366A  45 85 FF                        test r15d, r15d
0085366D  0F 89 EE 00 00 00               jns 0x140853761
00853673  48 8B 8D 9F 00 00 00            mov rcx, qword ptr [rbp + 0x9f]
0085367A  4C 8B 65 57                     mov r12, qword ptr [rbp + 0x57]
0085367E  4C 8B 6C 24 58                  mov r13, qword ptr [rsp + 0x58]
00853683  0F B6 81 AA 01 00 00            movzx eax, byte ptr [rcx + 0x1aa]
0085368A  3C 04                           cmp al, 4
0085368C  0F 83 7D FA FF FF               jae 0x14085310f
00853692  44 89 BC C1 AC 01 00 00         mov dword ptr [rcx + rax*8 + 0x1ac], r15d
0085369A  0F B6 81 AA 01 00 00            movzx eax, byte ptr [rcx + 0x1aa]
008536A1  C7 84 C1 B0 01 00 00 00 05 05 00  mov dword ptr [rcx + rax*8 + 0x1b0], 0x50500
008536AC  FE 81 AA 01 00 00               inc byte ptr [rcx + 0x1aa]
008536B2  E9 58 FA FF FF                  jmp 0x14085310f
008536B7  E8 64 95 00 00                  call 0x14085cc20
008536BC  41 FF C4                        inc r12d
008536BF  E9 92 F8 FF FF                  jmp 0x140852f56
008536C4  4C 8B 45 77                     mov r8, qword ptr [rbp + 0x77]
008536C8  48 8D 44 24 64                  lea rax, [rsp + 0x64]
008536CD  45 33 C9                        xor r9d, r9d
008536D0  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008536D5  49 8B D6                        mov rdx, r14
008536D8  49 8B CD                        mov rcx, r13
008536DB  E8 B0 A1 00 00                  call 0x14085d890
008536E0  85 C0                           test eax, eax
008536E2  0F 88 E1 01 00 00               js 0x1408538c9
008536E8  41 F6 85 8C 00 00 00 01         test byte ptr [r13 + 0x8c], 1
008536F0  48 8D 54 24 68                  lea rdx, [rsp + 0x68]
008536F5  49 8B CD                        mov rcx, r13
008536F8  0F 85 50 02 00 00               jne 0x14085394e
008536FE  E8 3D 28 00 00                  call 0x140855f40
00853703  8B 54 24 64                     mov edx, dword ptr [rsp + 0x64]
00853707  83 FA FF                        cmp edx, -1
0085370A  0F 84 84 FD FF FF               je 0x140853494
00853710  41 F6 85 8C 00 00 00 01         test byte ptr [r13 + 0x8c], 1
00853718  4C 8D 44 24 68                  lea r8, [rsp + 0x68]
0085371D  49 8B CD                        mov rcx, r13
00853720  74 38                           je 0x14085375a
00853722  E8 39 15 00 00                  call 0x140854c60
00853727  4C 8B F0                        mov r14, rax
0085372A  48 85 C0                        test rax, rax
0085372D  0F 85 80 F8 FF FF               jne 0x140852fb3
00853733  41 BF 9A 00 00 C0               mov r15d, 0xc000009a
00853739  44 89 7C 24 50                  mov dword ptr [rsp + 0x50], r15d
0085373E  E9 FC FE FF FF                  jmp 0x14085363f
00853743  0F B7 C8                        movzx ecx, ax
00853746  E8 A5 B9 00 00                  call 0x14085f0f0
0085374B  E9 B0 F8 FF FF                  jmp 0x140853000
00853750  E8 CB 94 00 00                  call 0x14085cc20
00853755  E9 63 FE FF FF                  jmp 0x1408535bd
0085375A  E8 51 15 00 00                  call 0x140854cb0
0085375F  EB C6                           jmp 0x140853727
00853761  44 8B 75 9F                     mov r14d, dword ptr [rbp - 0x61]
00853765  41 83 FE FF                     cmp r14d, -1
00853769  0F 84 23 FC FF FF               je 0x140853392
0085376F  48 8B 74 24 58                  mov rsi, qword ptr [rsp + 0x58]
00853774  49 8B 4D 20                     mov rcx, qword ptr [r13 + 0x20]
00853778  48 8D 45 BF                     lea rax, [rbp - 0x41]
0085377C  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00853781  45 33 E4                        xor r12d, r12d
00853784  48 8B 45 77                     mov rax, qword ptr [rbp + 0x77]
00853788  4C 8B CE                        mov r9, rsi
0085378B  89 5C 24 38                     mov dword ptr [rsp + 0x38], ebx
0085378F  4D 8B C5                        mov r8, r13
00853792  89 7C 24 30                     mov dword ptr [rsp + 0x30], edi
00853796  41 8B D6                        mov edx, r14d
00853799  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0085379E  44 89 64 24 20                  mov dword ptr [rsp + 0x20], r12d
008537A3  E8 08 E6 FF FF                  call 0x140851db0
008537A8  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
008537AC  44 8B F8                        mov r15d, eax
008537AF  85 C0                           test eax, eax
008537B1  0F 88 51 02 00 00               js 0x140853a08
008537B7  48 85 F6                        test rsi, rsi
008537BA  74 29                           je 0x1408537e5
008537BC  48 C7 C0 FF FF FF FF            mov rax, 0xffffffffffffffff
008537C3  F0 48 0F C1 06                  lock xadd qword ptr [rsi], rax
008537C8  48 83 F8 01                     cmp rax, 1
008537CC  75 17                           jne 0x1408537e5
008537CE  45 33 C9                        xor r9d, r9d
008537D1  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
008537D6  45 33 C0                        xor r8d, r8d
008537D9  8D 50 1E                        lea edx, [rax + 0x1e]
008537DC  8D 48 50                        lea ecx, [rax + 0x50]
008537DF  E8 7C 9E CA FF                  call 0x1404fd660
008537E4  CC                              int3
008537E5  48 8B 75 BF                     mov rsi, qword ptr [rbp - 0x41]
008537E9  48 8B 45 67                     mov rax, qword ptr [rbp + 0x67]
008537ED  4C 0F BF 7C 24 60               movsx r15, word ptr [rsp + 0x60]
008537F3  48 89 74 24 58                  mov qword ptr [rsp + 0x58], rsi
008537F8  4C 89 65 BF                     mov qword ptr [rbp - 0x41], r12
008537FC  66 FF 40 02                     inc word ptr [rax + 2]
00853800  41 83 FF 02                     cmp r15d, 2
00853804  0F 8D 20 02 00 00               jge 0x140853a2a
0085380A  4A 89 74 F8 08                  mov qword ptr [rax + r15*8 + 8], rsi
0085380F  48 8B 45 4F                     mov rax, qword ptr [rbp + 0x4f]
00853813  66 44 3B 78 42                  cmp r15w, word ptr [rax + 0x42]
00853818  0F 84 86 00 00 00               je 0x1408538a4
0085381E  4D 8B 75 20                     mov r14, qword ptr [r13 + 0x20]
00853822  8B C3                           mov eax, ebx
00853824  C1 E8 09                        shr eax, 9
00853827  33 C3                           xor eax, ebx
00853829  69 C0 A3 8A 01 00               imul eax, eax, 0x18aa3
0085382F  8B C8                           mov ecx, eax
00853831  8B D0                           mov edx, eax
00853833  49 8B 86 70 06 00 00            mov rax, qword ptr [r14 + 0x670]
0085383A  48 C1 EA 09                     shr rdx, 9
0085383E  48 33 D1                        xor rdx, rcx
00853841  41 8B 8E 78 06 00 00            mov ecx, dword ptr [r14 + 0x678]
00853848  FF C9                           dec ecx
0085384A  48 23 D1                        and rdx, rcx
0085384D  48 8D 0C 52                     lea rcx, [rdx + rdx*2]
00853851  48 8D 34 C8                     lea rsi, [rax + rcx*8]
00853855  4C 89 66 08                     mov qword ptr [rsi + 8], r12
00853859  0F 0D 0E                        prefetchw byte ptr [rsi]
0085385C  48 8B 06                        mov rax, qword ptr [rsi]
0085385F  48 8B C8                        mov rcx, rax
00853862  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
00853866  48 83 F9 10                     cmp rcx, 0x10
0085386A  48 8D 50 F0                     lea rdx, [rax - 0x10]
0085386E  49 0F 46 D4                     cmovbe rdx, r12
00853872  A8 02                           test al, 2
00853874  75 49                           jne 0x1408538bf
00853876  F0 48 0F B1 16                  lock cmpxchg qword ptr [rsi], rdx
0085387B  75 42                           jne 0x1408538bf
0085387D  48 8B CE                        mov rcx, rsi
00853880  E8 7B DD A8 FF                  call 0x1402e1600
00853885  48 C7 C0 FF FF FF FF            mov rax, 0xffffffffffffffff
0085388C  F0 41 0F C1 86 88 10 00 00      lock xadd dword ptr [r14 + 0x1088], eax
00853895  83 F8 01                        cmp eax, 1
00853898  74 1B                           je 0x1408538b5
0085389A  66 FF 44 24 54                  inc word ptr [rsp + 0x54]
0085389F  48 8B 74 24 58                  mov rsi, qword ptr [rsp + 0x58]
008538A4  4C 8B 65 57                     mov r12, qword ptr [rbp + 0x57]
008538A8  66 41 FF C7                     inc r15w
008538AC  4C 8B 6D 4F                     mov r13, qword ptr [rbp + 0x4f]
008538B0  E9 35 F5 FF FF                  jmp 0x140852dea
008538B5  49 8B CE                        mov rcx, r14
008538B8  E8 4F 0C 01 00                  call 0x14086450c
008538BD  EB DB                           jmp 0x14085389a
008538BF  48 8B CE                        mov rcx, rsi
008538C2  E8 09 00 A1 FF                  call 0x1402638d0
008538C7  EB B4                           jmp 0x14085387d
008538C9  41 BF 9A 00 00 C0               mov r15d, 0xc000009a
008538CF  E9 4B FD FF FF                  jmp 0x14085361f
008538D4  E8 47 93 00 00                  call 0x14085cc20
008538D9  E9 61 FD FF FF                  jmp 0x14085363f
008538DE  E8 3D 93 00 00                  call 0x14085cc20
008538E3  E9 75 FD FF FF                  jmp 0x14085365d
008538E8  49 8B 44 24 18                  mov rax, qword ptr [r12 + 0x18]
008538ED  48 8B 54 D0 F0                  mov rdx, qword ptr [rax + rdx*8 - 0x10]
008538F2  E9 71 F4 FF FF                  jmp 0x140852d68
008538F7  41 0F B7 CD                     movzx ecx, r13w
008538FB  E8 F0 B7 00 00                  call 0x14085f0f0
00853900  44 0F B7 E8                     movzx r13d, ax
00853904  E9 5D FC FF FF                  jmp 0x140853566
00853909  44 0F B7 49 48                  movzx r9d, word ptr [rcx + 0x48]
0085390E  4D 8B C2                        mov r8, r10
00853911  41 0F B7 14 24                  movzx edx, word ptr [r12]
00853916  49 8B 4C 24 08                  mov rcx, qword ptr [r12 + 8]
0085391B  49 D1 E9                        shr r9, 1
0085391E  48 D1 EA                        shr rdx, 1
00853921  C6 44 24 20 01                  mov byte ptr [rsp + 0x20], 1
00853926  E8 B5 EE 11 00                  call 0x1409727e0
0085392B  44 8B E0                        mov r12d, eax
0085392E  E9 70 FC FF FF                  jmp 0x1408535a3
00853933  41 B9 0C 00 00 00               mov r9d, 0xc
00853939  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
0085393E  4D 8B C6                        mov r8, r14
00853941  41 8D 51 0B                     lea edx, [r9 + 0xb]
00853945  8D 4A 3A                        lea ecx, [rdx + 0x3a]
00853948  E8 13 9D CA FF                  call 0x1404fd660
0085394D  CC                              int3
0085394E  E8 CD 92 00 00                  call 0x14085cc20
00853953  E9 AB FD FF FF                  jmp 0x140853703
00853958  49 8B 44 24 18                  mov rax, qword ptr [r12 + 0x18]
0085395D  49 8B 3C 06                     mov rdi, qword ptr [r14 + rax]
00853961  E9 24 F8 FF FF                  jmp 0x14085318a
00853966  44 0F B7 7E 42                  movzx r15d, word ptr [rsi + 0x42]
0085396B  66 41 FF C7                     inc r15w
0085396F  E9 73 F4 FF FF                  jmp 0x140852de7
00853974  49 8B 44 24 18                  mov rax, qword ptr [r12 + 0x18]
00853979  4C 8B 74 C8 F0                  mov r14, qword ptr [rax + rcx*8 - 0x10]
0085397E  E9 EC F2 FF FF                  jmp 0x140852c6f
00853983  48 8D 4E 48                     lea rcx, [rsi + 0x48]
00853987  E8 B4 FA A0 FF                  call 0x140263440
0085398C  E9 89 F5 FF FF                  jmp 0x140852f1a
00853991  48 8B 4E 20                     mov rcx, qword ptr [rsi + 0x20]
00853995  8B D3                           mov edx, ebx
00853997  E8 C4 0A 01 00                  call 0x140864460
0085399C  48 8B 74 24 58                  mov rsi, qword ptr [rsp + 0x58]
008539A1  E9 5F F2 FF FF                  jmp 0x140852c05
008539A6  48 8B 96 C0 00 00 00            mov rdx, qword ptr [rsi + 0xc0]
008539AD  48 85 D2                        test rdx, rdx
008539B0  0F 84 B6 F9 FF FF               je 0x14085336c
008539B6  66 66 0F 1F 84 00 00 00 00 00   nop word ptr [rax + rax]
008539C0  4C 8B 42 10                     mov r8, qword ptr [rdx + 0x10]
008539C4  4C 0F BF C9                     movsx r9, cx
008539C8  66 83 F9 02                     cmp cx, 2
008539CC  7D 6A                           jge 0x140853a38
008539CE  4F 89 44 CF 08                  mov qword ptr [r15 + r9*8 + 8], r8
008539D3  48 8B 52 18                     mov rdx, qword ptr [rdx + 0x18]
008539D7  66 FF C9                        dec cx
008539DA  48 85 D2                        test rdx, rdx
008539DD  75 E1                           jne 0x1408539c0
008539DF  E9 88 F9 FF FF                  jmp 0x14085336c
008539E4  49 8B 44 24 18                  mov rax, qword ptr [r12 + 0x18]
008539E9  48 8B 74 F0 F0                  mov rsi, qword ptr [rax + rsi*8 - 0x10]
008539EE  E9 1B F9 FF FF                  jmp 0x14085330e
008539F3  41 BF 34 00 00 C0               mov r15d, 0xc0000034
008539F9  BA 00 04 05 00                  mov edx, 0x50400
008539FE  44 89 7C 24 50                  mov dword ptr [rsp + 0x50], r15d
00853A03  E9 BE F8 FF FF                  jmp 0x1408532c6
00853A08  48 8B 8D 9F 00 00 00            mov rcx, qword ptr [rbp + 0x9f]
00853A0F  44 8B C0                        mov r8d, eax
00853A12  BA 00 07 05 00                  mov edx, 0x50700
00853A17  E8 64 D8 FF FF                  call 0x140851280
00853A1C  4C 8B 65 57                     mov r12, qword ptr [rbp + 0x57]
00853A20  4C 8B 6C 24 58                  mov r13, qword ptr [rsp + 0x58]
00853A25  E9 E5 F6 FF FF                  jmp 0x14085310f
00853A2A  48 8B 40 18                     mov rax, qword ptr [rax + 0x18]
00853A2E  4A 89 74 F8 F0                  mov qword ptr [rax + r15*8 - 0x10], rsi
00853A33  E9 D7 FD FF FF                  jmp 0x14085380f
00853A38  49 8B 47 18                     mov rax, qword ptr [r15 + 0x18]
00853A3C  4E 89 44 C8 F0                  mov qword ptr [rax + r9*8 - 0x10], r8
00853A41  EB 90                           jmp 0x1408539d3
00853A43  48 8B 42 38                     mov rax, qword ptr [rdx + 0x38]
00853A47  48 85 C0                        test rax, rax
00853A4A  0F 84 51 F8 FF FF               je 0x1408532a1
00853A50  48 3B C8                        cmp rcx, rax
00853A53  0F 94 C0                        sete al
00853A56  E9 53 F8 FF FF                  jmp 0x1408532ae
00853A5B  66 FF 4C 24 56                  dec word ptr [rsp + 0x56]
00853A60  84 C0                           test al, al
00853A62  E9 88 F6 FF FF                  jmp 0x1408530ef
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpWalkOneLevel(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, unsigned int a7, unsigned int a8, __int64 a9, unsigned __int8 a10, __int64 a11)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m47;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned int v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned int v_stack_mA8;
    unsigned int v_stack_mAC;
    unsigned __int64 v_stack_mB0;
    unsigned int v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned int v_stack_mCC;
    unsigned int v_stack_mD0;
    unsigned int v_stack_mD4;
    unsigned __int16 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int16 v_stack_mE2;
    unsigned __int16 v_stack_mE4;
    unsigned int v_stack_mE8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned int v_stack_p30;
    unsigned int v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned int v_stack_p50;
    unsigned __int16 v_stack_p54;
    unsigned __int16 v_stack_p56;
    unsigned __int64 v_stack_p58;
    unsigned __int16 v_stack_p60;
    unsigned __int64 v_stack_p64;
    unsigned __int64 v_stack_p68;
    unsigned __int16 v_stack_p70;
    unsigned __int64 v_stack_p8;

    v_stack_p20 = a4;
    v_stack_p18 = a3;
    v_stack_p10 = a2;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (248);
    a2 = 0;
    v_stack_mC0 = 0;
    v_stack_m88 = 0;
    result = HvpGetCellContextInitialize(v_stack_mC0, a2, a3, a4);
    v_stack_mE2 = -1;
loc_00852C05:
    v_rdi = (unsigned __int16)((*(unsigned __int16 *)(a1 + 66)) - 1);
    v_stack_mE0 = 0;
    if (!sign_flag) goto loc_008532FB;
    if (0 != 0) goto loc_00853350;
    a2 = 0;
    *(unsigned __int16 *)(a4 + 2) = 0xFFFFULL;
    v_stack_mE0 = 0;
loc_00852C2F:
    v_stack_mE4 = 0;
    if (0 > (*(unsigned __int16 *)(v_stack_p8 + 66))) goto loc_00852D0E;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a8)))) >> (9));
    result = (unsigned int)((result) ^ ((unsigned int)((unsigned int)(a8))));
    result = (unsigned int)((result) * ((unsigned int)(result)));
    v_r15 = ((unsigned int)((unsigned int)(result))) >> (9);
    v_r15 = (v_r15) ^ ((unsigned int)((unsigned int)(result)));
loc_00852C5C:
    if (0 >= 2) goto loc_00853974;
loc_00852C6F:
    a3 = 0;
    a2 = 0;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + (__int16)(0) * 8 + 8) + 32) + 1656))) - 1);
    a1 = (a1) & (v_r15);
    result = KeAbPreAcquire(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + (__int16)(0) * 8 + 8) + 32) + 1648) + a1 + a1 * 2 * 8, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + (__int16)(0) * 8 + 8) + 32) + 1648) + a1 + a1 * 2 * 8;
        a2 = result;
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + (__int16)(0) * 8 + 8) + 32) + 1648) + a1 + a1 * 2 * 8;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + (__int16)(0) * 8 + 8) + 32) + 1648) + a1 + a1 * 2 * 8 + 8) = *(unsigned __int64 *)(gs_base + (0 + 392));
loc_00852CDA:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + (__int16)(0) * 8 + 8) + 32) + 4232))) == 0) goto loc_00853933;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + (__int16)(0) * 8 + 8) + 32) + 4232))) != 0) goto loc_00852CDA;
    v_stack_mE2 = 0;
    v_rdi = (unsigned __int16)((0) + 1);
    if (((unsigned __int16)(v_rdi)) <= (*(unsigned __int16 *)(v_stack_p8 + 66))) goto loc_00852C5C;
    a2 = 0;
loc_00852D0E:
    if (0 > ((unsigned __int16)(*(unsigned __int16 *)(a2 + 2)))) goto loc_00852D48;
loc_00852D20:
    if (0 >= 2) goto loc_008532DF;
loc_00852D33:
    result = CmpLockKcbShared(*(unsigned __int64 *)(a2 + (__int16)(0) * 8 + 8), a2, a3, a4);
    v_rdi = (unsigned __int16)((0) + 1);
    if (((unsigned __int16)(v_rdi)) <= ((unsigned __int16)(*(unsigned __int16 *)(a2 + 2)))) goto loc_00852D20;
    a2 = 0;
loc_00852D48:
    v_stack_m80 = 0;
loc_00852D4C:
    if (sign_flag) goto loc_00853093;
    if (((unsigned __int16)(*(unsigned __int16 *)(a2 + 2))) >= 2) goto loc_008538E8;
loc_00852D68:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a2 + (__int16)((unsigned __int16)(*(unsigned __int16 *)(a2 + 2))) * 8 + 8) + 66)) == 0) goto loc_00852D79;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + (__int16)((unsigned __int16)(*(unsigned __int16 *)(a2 + 2))) * 8 + 8) + 65)) == 1) goto loc_00853093;
loc_00852D79:
    if ((*(unsigned int *)(*(unsigned __int64 *)(a2 + (__int16)((unsigned __int16)(*(unsigned __int16 *)(a2 + 2))) * 8 + 8) + 40)) == -1) goto loc_00853066;
    if (a9 != 0) goto loc_00853243;
loc_00852D93:
    if (*(unsigned __int64 *)(v_stack_p8 + 240) != 0) goto loc_00853286;
loc_00852DA3:
    if (((*(unsigned int *)(v_stack_p8 + 184)) & (0x20000ULL)) != 0) goto loc_008539F3;
    result = (unsigned int)(*(unsigned int *)(a11 + 160));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a11 + 160)))) & (1)) == 0) {
        a1 = a11 + 168;
        result = CmpAttachToRegistryProcess(a1, *(unsigned __int64 *)(v_stack_p8 + 240), a3, a4);
    }
    if (v_stack_mE0 != 0) goto loc_00853966;
    result = 0;
loc_00852DE7:
loc_00852DEA:
    v_stack_mD8 = 0;
    if (0 > (*(unsigned __int16 *)(v_stack_p8 + 66))) goto loc_008530E0;
    if (0 >= 2) goto loc_00853402;
loc_00852E0F:
    v_stack_m70 = *(unsigned __int64 *)(a2 + (__int16)(0) * 8 + 8);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + (__int16)(0) * 8 + 8) + 40)))) == -1) goto loc_00853384;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + (__int16)(0) * 8 + 8) + 32) + 140)) & (1)) == 0) goto loc_00853052;
    result = HvpGetCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + (__int16)(0) * 8 + 8) + 32), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + (__int16)(0) * 8 + 8) + 40)), v_stack_mC0, a4);
loc_00852E3A:
    v_stack_mA0 = result;
    if (((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + (__int16)(0) * 8 + 8) + 32) + 160)) & (0x8001ULL)) != 0) goto loc_00852F23;
    if (((*(unsigned __int8 *)(v_rip + 6012469)) & ((unsigned __int8)(*(unsigned __int8 *)(result + 12)))) != 0) goto loc_00852F23;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + (__int16)(0) * 8 + 8) + 32) + 140)) & (1)) != 0) goto loc_0085337A;
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + (__int16)(0) * 8 + 8) + 32), v_stack_mC0, v_stack_mC0, a4);
loc_00852E7B:
    a3 = 0;
    v_rsi = (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + (__int16)(0) * 8 + 8) + 32)) + (72);
    a2 = 0;
    result = KeAbPreAcquire(v_rsi, a2, a3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = v_rsi;
        a3 = 0;
        a2 = 0;
        a1 = v_rsi;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + (__int16)(0) * 8 + 8) + 32) + 140)) & (1)) == 0) goto loc_0085305C;
    result = HvpGetCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + (__int16)(0) * 8 + 8) + 32), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + (__int16)(0) * 8 + 8) + 40)), v_stack_mC0, a4);
loc_00852EDA:
    v_stack_mA0 = result;
    if (((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + (__int16)(0) * 8 + 8) + 32) + 160)) & (0x8001ULL)) != 0) goto loc_00852F05;
    if (((*(unsigned __int8 *)(v_rip + 6012309)) & ((unsigned __int8)(*(unsigned __int8 *)(result + 12)))) == 0) goto loc_0085306E;
loc_00852F05:
    a1 = 0;
    if (condition_is_not_equal) goto loc_00853983;
loc_00852F1A:
    result = KeAbPostRelease(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + (__int16)(0) * 8 + 8) + 32) + 72, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + (__int16)(0) * 8 + 8) + 40)), v_stack_mC0, a4);
loc_00852F23:
    a2 = 0;
    v_stack_m78 = *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + (__int16)(0) * 8 + 8) + 32);
    v_stack_mE8 = (unsigned int)((unsigned int)(0xC0000034ULL));
    v_stack_mCC = 0;
    v_stack_mD4 = 0;
    v_stack_m90 = 0;
    v_stack_mA8 = (unsigned int)((unsigned int)(0xFFFFFFFFULL));
    v_stack_mD0 = 0xFFFFFFFFULL;
loc_00852F56:
    v_stack_mB8 = 0;
    if (0 >= (*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + (__int16)(0) * 8 + 8) + 32) + 216))) goto loc_0085363F;
    if ((*(unsigned int *)(v_stack_mA0 + 0 * 4 + 20)) == 0) goto loc_00853494;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + (__int16)(0) * 8 + 8) + 32) + 140)) & (1)) == 0) goto loc_0085349C;
    result = HvpGetCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + (__int16)(0) * 8 + 8) + 32), (unsigned int)(*(unsigned int *)(v_stack_mA0 + 0 * 4 + 28)), v_stack_mD0, a4);
loc_00852F98:
    if (result == 0) goto loc_00853733;
    if ((*(unsigned __int16 *)(result)) == ((unsigned __int16)((unsigned int)(0x6972ULL)))) goto loc_008536C4;
loc_00852FB3:
    if ((*(unsigned __int16 *)(result)) != ((unsigned __int16)((unsigned int)(0x686CULL)))) goto loc_00853431;
    a1 = 0;
    v_stack_m60 = v_xmm0;
    if (((unsigned __int16)((unsigned int)(0x686CULL))) < 2) goto loc_0085301E;
    v_r12 = ((unsigned __int16)((unsigned int)(0x686CULL))) >> (1);
loc_00852FE9:
    if (((unsigned __int16)(*(unsigned __int16 *)(v_stack_m58))) < 97) goto loc_00853000;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_stack_m58))) > 122) goto loc_00853743;
    result = (unsigned __int16)((*(unsigned __int16 *)(v_stack_m58)) - (32));
loc_00853000:
    v_r15 = (unsigned int)((0) * (0));
    v_rsi = (v_stack_m58) + (2);
    v_r15 = (unsigned int)((v_r15) + ((unsigned int)((unsigned __int16)(result))));
    v_r12 = (v_r12) - (1);
    if (condition_is_not_equal) goto loc_00852FE9;
    a1 = 0;
    v_stack_m58 = v_rsi;
loc_0085301E:
    v_stack_mD4 = 0xFFFFFFFFULL;
loc_00853030:
    if (0 >= (*(unsigned __int16 *)(result + 2))) goto loc_00853420;
    if (((unsigned int)(v_r15)) == (*(unsigned int *)(result + 0 * 8 + 8))) goto loc_008534A6;
loc_00853049:
    v_rsi = (unsigned __int16)((0) + 1);
    goto loc_00853030;
loc_00853052:
    result = HvpGetCellPaged(a1, (unsigned int)(*(unsigned int *)(v_stack_mA0 + 0 * 4 + 28)), v_stack_mD0, a4);
    goto loc_00852E3A;
loc_0085305C:
    result = HvpGetCellPaged(a1, (unsigned int)(*(unsigned int *)(v_stack_mA0 + 0 * 4 + 28)), v_stack_mD0, a4);
    goto loc_00852EDA;
loc_00853066:
    a1 = (unsigned __int16)((a1) - 1);
    goto loc_00852D4C;
loc_0085306E:
    a3 = 0;
    result = HvpMarkCellDirty(a1, (unsigned int)(*(unsigned int *)(v_stack_mA0 + 0 * 4 + 28)), a3, 1);
    if (sign_flag) goto loc_00852F05;
    goto loc_00852F05;
loc_00853093:
    v_stack_mE8 = (unsigned int)((unsigned int)(0xC0000034ULL));
    if (a11 == 0) goto loc_008532D5;
    if (((unsigned __int8)(*(unsigned __int8 *)(a11 + 426))) >= 4) goto loc_0085310F;
    *(unsigned int *)(a11 + *(unsigned __int8 *)(a11 + 426) * 8 + 428) = (unsigned int)((unsigned int)(0xC0000034ULL));
    *(unsigned int *)(a11 + *(unsigned __int8 *)(a11 + 426) * 8 + 432) = 0x50200ULL;
    goto loc_0085310F;
loc_008530E0:
    if (a10 != 0) goto loc_00853A5B;
loc_008530EF:
    result = (a10 != 0) ? 1 : 0;
    v_r15 = 0;
    v_stack_mE0 = 0;
    v_stack_mE8 = 0;
    *(unsigned __int8 *)(a5) = (unsigned __int8)(result);
    *(unsigned __int64 *)(v_stack_p18) = v_rsi;
loc_0085310F:
    result = 0;
    if (0 > (*(unsigned __int16 *)(a6 + 2))) goto loc_00853143;
loc_00853120:
    if (0 >= 2) goto loc_00853411;
loc_00853133:
    result = CmpUnlockKcb(*(unsigned __int64 *)(a6 + (__int16)(0) * 8 + 8), (unsigned int)(*(unsigned int *)(v_stack_mA0 + 0 * 4 + 28)), a3, 1);
    v_rdi = (unsigned __int16)((0) + 1);
    if (((unsigned __int16)(v_rdi)) <= (*(unsigned __int16 *)(a6 + 2))) goto loc_00853120;
loc_00853143:
    if (((unsigned __int16)((__int16)(v_stack_mE4))) > v_stack_mE2) goto loc_0085321E;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a8)))) >> (9));
    result = (unsigned int)((result) ^ ((unsigned int)((unsigned int)(a8))));
    result = (unsigned int)((result) * ((unsigned int)(result)));
    v_rsi = ((unsigned int)((unsigned int)(result))) >> (9);
    v_rsi = (v_rsi) ^ ((unsigned int)((unsigned int)(result)));
    v_r13 = 0;
loc_0085317B:
    if (((unsigned __int16)((__int16)(v_stack_mE4))) >= 2) goto loc_00853958;
loc_0085318A:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a6 + (__int16)(v_stack_mE4) * 8 - 16 * 1 + 24) + 32) + 1656))) - 1);
    a1 = (a1) & (v_rsi);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a6 + (__int16)(v_stack_mE4) * 8 - 16 * 1 + 24) + 32) + 1648) + a1 + a1 * 2 * 8 + 8) = 0;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a6 + (__int16)(v_stack_mE4) * 8 - 16 * 1 + 24) + 32) + 1648) + a1 + a1 * 2 * 8)) & (-16);
    a2 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a6 + (__int16)(v_stack_mE4) * 8 - 16 * 1 + 24) + 32) + 1648) + a1 + a1 * 2 * 8) - 16;
    if (a1 <= 16) { a2 = 0; }
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a6 + (__int16)(v_stack_mE4) * 8 - 16 * 1 + 24) + 32) + 1648) + a1 + a1 * 2 * 8))) & (2)) != 0) goto loc_008532EE;
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a6 + (__int16)(v_stack_mE4) * 8 - 16 * 1 + 24) + 32) + 1648) + a1 + a1 * 2 * 8))) & (2)) != 0) goto loc_008532EE;
loc_008531D8:
    result = KeAbPostRelease(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a6 + (__int16)(v_stack_mE4) * 8 - 16 * 1 + 24) + 32) + 1648) + a1 + a1 * 2 * 8, a2, a3, 1);
    result = (unsigned int)((unsigned int)(v_r13 - 1));
    if (((unsigned int)((unsigned int)((unsigned int)(v_r13 - 1)))) == 1) {
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(a6 + (__int16)(v_stack_mE4) * 8 - 16 * 1 + 24) + 32);
        result = CmpDeleteHive(a1, a2, a3, 1);
    }
    v_r14 = ((__int16)(v_stack_mE4) * 8 - 16) + (8);
    a2 = (unsigned __int16)((v_stack_mE4) + 1);
    v_stack_mE4 = (unsigned __int16)(a2);
    if (((unsigned __int16)(a2)) <= v_stack_mE2) goto loc_0085317B;
loc_0085321E:
    if (v_stack_mE0 != 0) {
        a1 = v_stack_mE0;
        result = CmpDereferenceKeyControlBlock(a1, a2, a3, 1);
    }
    v_rsp = (v_rsp) + (248);
    return (unsigned int)((unsigned int)((unsigned int)(v_stack_mE8)));
loc_00853243:
loc_00853248:
    result = CmListGetNextElement(*(unsigned __int64 *)(a6 + 8) + 208, v_stack_m80, 32, *(unsigned __int64 *)(a6 + 8));
    if (result == 0) goto loc_00852D93;
    if ((*(unsigned int *)(result + 68)) != 2) goto loc_00853248;
    result = CmEqualTrans(*(unsigned __int64 *)(result + 56), *(unsigned __int64 *)(*(unsigned __int64 *)(a6 + (__int16)(v_stack_mE4) * 8 - 16 * 1 + 24) + 32), 32, *(unsigned __int64 *)(a6 + 8));
    if ((unsigned __int8)(result) == 0) goto loc_00852D93;
    goto loc_00853093;
loc_00853286:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a6 + (__int16)(v_stack_mE4) * 8 - 16 * 1 + 24) + 32) == 0) goto loc_008532B6;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a6 + (__int16)(v_stack_mE4) * 8 - 16 * 1 + 24) + 32)) == (*(unsigned __int64 *)(*(unsigned __int64 *)(a6 + (__int16)(v_stack_mE4) * 8 - 16 * 1 + 24) + 32))) goto loc_00852DA3;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a6 + (__int16)(v_stack_mE4) * 8 - 16 * 1 + 24) + 32) + 56) != 0) goto loc_00853A43;
loc_008532A1:
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a6 + (__int16)(v_stack_mE4) * 8 - 16 * 1 + 24) + 32)) + (88);
    result = CmpTransUowIsEqual(*(unsigned __int64 *)(*(unsigned __int64 *)(a6 + (__int16)(v_stack_mE4) * 8 - 16 * 1 + 24) + 32) + 88, a2, 32, *(unsigned __int64 *)(a6 + 8));
loc_008532AE:
    if ((unsigned __int8)(result) != 0) goto loc_00852DA3;
loc_008532B6:
    v_stack_p50 = (unsigned int)((unsigned int)(0xC0000034ULL));
loc_008532C6:
    result = CmpRecordParseFailure(a11, (unsigned int)(0x50300ULL), (unsigned int)((unsigned int)((unsigned int)(0xC0000034ULL))), *(unsigned __int64 *)(a6 + 8));
loc_008532D5:
    goto loc_0085310F;
loc_008532DF:
    goto loc_00852D33;
loc_008532EE:
    result = ExfReleasePushLock(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a6 + (__int16)(v_stack_mE4) * 8 - 16 * 1 + 24) + 32) + 1648) + a1 + a1 * 2 * 8, (unsigned int)(0x50300ULL), (unsigned int)((unsigned int)((unsigned int)(0xC0000034ULL))), *(unsigned __int64 *)(a6 + 8));
    goto loc_008531D8;
loc_008532FB:
    if (((unsigned __int16)(*(unsigned __int64 *)(*(unsigned __int64 *)(a6 + (__int16)(v_stack_mE4) * 8 - 16 * 1 + 24) + 32))) >= 2) goto loc_008539E4;
loc_0085330E:
    result = CmpLockHashEntryShared(*(unsigned __int64 *)(*(unsigned __int64 *)(a6 + (__int16)((unsigned __int16)(*(unsigned __int64 *)(*(unsigned __int64 *)(a6 + (__int16)(v_stack_mE4) * 8 - 16 * 1 + 24) + 32))) * 8 + 8) + 32), (unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a6 + (__int16)(v_stack_mE4) * 8 - 16 * 1 + 24) + 32) + 1648) + a1 + a1 * 2 * 8)), (unsigned int)((unsigned int)((unsigned int)(0xC0000034ULL))), *(unsigned __int64 *)(a6 + 8));
    result = CmpFindKcbInHashEntryByName(*(unsigned __int64 *)(*(unsigned __int64 *)(a6 + (__int16)((unsigned __int16)(*(unsigned __int64 *)(*(unsigned __int64 *)(a6 + (__int16)(v_stack_mE4) * 8 - 16 * 1 + 24) + 32))) * 8 + 8) + 32), (unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a6 + (__int16)(v_stack_mE4) * 8 - 16 * 1 + 24) + 32) + 1648) + a1 + a1 * 2 * 8)), *(unsigned __int64 *)(a6 + (__int16)((unsigned __int16)(*(unsigned __int64 *)(*(unsigned __int64 *)(a6 + (__int16)(v_stack_mE4) * 8 - 16 * 1 + 24) + 32))) * 8 + 8), v_r14);
    v_stack_p58 = result;
    if (result == 0) goto loc_00853991;
    result = CmpReferenceKeyControlBlockLockNotHeld(result, (unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a6 + (__int16)(v_stack_mE4) * 8 - 16 * 1 + 24) + 32) + 1648) + a1 + a1 * 2 * 8)), *(unsigned __int64 *)(a6 + (__int16)((unsigned __int16)(*(unsigned __int64 *)(*(unsigned __int64 *)(a6 + (__int16)(v_stack_mE4) * 8 - 16 * 1 + 24) + 32))) * 8 + 8), v_r14);
    result = CmpUnlockHashEntry(*(unsigned __int64 *)(*(unsigned __int64 *)(a6 + (__int16)((unsigned __int16)(*(unsigned __int64 *)(*(unsigned __int64 *)(a6 + (__int16)(v_stack_mE4) * 8 - 16 * 1 + 24) + 32))) * 8 + 8) + 32), (unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a6 + (__int16)(v_stack_mE4) * 8 - 16 * 1 + 24) + 32) + 1648) + a1 + a1 * 2 * 8)), *(unsigned __int64 *)(a6 + (__int16)((unsigned __int16)(*(unsigned __int64 *)(*(unsigned __int64 *)(a6 + (__int16)(v_stack_mE4) * 8 - 16 * 1 + 24) + 32))) * 8 + 8), v_r14);
loc_00853350:
    *(unsigned __int16 *)((unsigned int)(0xC0000034ULL) + 2) = (unsigned __int16)(*(unsigned __int16 *)(v_stack_p58 + 66));
    if ((unsigned __int16)((__int16)(*(unsigned __int16 *)(v_stack_p58 + 66))) != 0) goto loc_008539A6;
    *(unsigned __int64 *)((unsigned int)(0xC0000034ULL) + (__int16)(*(unsigned __int16 *)(v_stack_p58 + 66)) * 8 + 8) = v_stack_p58;
loc_0085336C:
    v_rdi = (unsigned __int16)((*(unsigned __int16 *)(v_stack_p58 + 66)) + 1);
    a2 = 0;
    goto loc_00852C2F;
loc_0085337A:
    result = HvpReleaseCellFlat((__int16)(*(unsigned __int16 *)(v_stack_p58 + 66)), a2, *(unsigned __int64 *)(a6 + (__int16)((unsigned __int16)(*(unsigned __int64 *)(*(unsigned __int64 *)(a6 + (__int16)(v_stack_mE4) * 8 - 16 * 1 + 24) + 32))) * 8 + 8), v_r14);
    goto loc_00852E7B;
loc_00853384:
    goto loc_0085339B;
loc_0085338C:
loc_00853392:
loc_0085339B:
    if ((*(unsigned __int16 *)(v_stack_p8 + 66)) != 0) goto loc_00853774;
    if (a10 != 0) goto loc_00853774;
    v_stack_p50 = (unsigned int)((unsigned int)(0xC0000034ULL));
    if (((unsigned __int8)(*(unsigned __int8 *)(a11 + 426))) >= 4) goto loc_0085310F;
    *(unsigned int *)(a11 + *(unsigned __int8 *)(a11 + 426) * 8 + 428) = (unsigned int)((unsigned int)(0xC0000034ULL));
    *(unsigned int *)(a11 + *(unsigned __int8 *)(a11 + 426) * 8 + 432) = 0x50600ULL;
    goto loc_0085310F;
loc_00853402:
    goto loc_00852E0F;
loc_00853411:
    goto loc_00853133;
loc_00853420:
    v_stack_p50 = (unsigned int)((unsigned int)(0xC0000034ULL));
    goto loc_00853479;
loc_00853431:
    v_stack_p28 = v_stack_m90;
    a4 = 0;
    v_stack_p20 = v_stack_p64;
    result = CmpFindSubKeyInLeafWithStatus(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 24) + a11 * 8 - 16), (unsigned int)(0xFFFFFFFFULL), a6, a4);
    v_stack_p50 = (unsigned int)(result);
    result = (unsigned int)((result) + ((unsigned int)((unsigned int)(0x80000000ULL))));
    if ((((unsigned int)((unsigned int)(0x80000000ULL))) & ((unsigned int)(result))) == 0) goto loc_008535E0;
loc_0085346C:
loc_00853470:
    if (((unsigned int)((unsigned int)(v_stack_p64))) != -1) goto loc_00853617;
loc_00853479:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 24) + a11 * 8 - 16) + 140)) & (1)) != 0) goto loc_008536B7;
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 24) + a11 * 8 - 16), v_stack_p68, a6, a4);
loc_00853494:
    v_r12 = (unsigned int)(((unsigned int)(v_stack_mB8)) + 1);
    goto loc_00852F56;
loc_0085349C:
    result = HvpGetCellPaged(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 24) + a11 * 8 - 16), v_stack_p68, a6, a4);
    goto loc_00852F98;
loc_008534A6:
    v_stack_mB0 = 0xFFFFFFFFULL;
    v_stack_mAC = 0;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 24) + a11 * 8 - 16) + 140)) & (1)) == 0) goto loc_0085360D;
    result = HvpGetCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 24) + a11 * 8 - 16), (unsigned int)(*(unsigned int *)((unsigned int)(0xFFFFFFFFULL) + result * 8 + 4)), v_stack_mB0, a4);
loc_008534D3:
    if (result == 0) goto loc_008538C9;
    if (((*(unsigned __int8 *)(result + 2)) & (32)) == 0) goto loc_00853909;
    a2 = (unsigned __int16)((*(unsigned __int16 *)(v_r12)) >> (1));
loc_008534FE:
    v_stack_p50 = (unsigned __int16)(*(unsigned __int16 *)(result + 72));
    v_stack_p70 = (unsigned __int16)(a2);
    if ((unsigned __int16)(a2) == 0) goto loc_00853595;
    if ((unsigned __int16)(*(unsigned __int16 *)(result + 72)) == 0) goto loc_00853595;
    a3 = (*(unsigned __int64 *)(v_r12 + 8)) + (2);
    v_r10 = (result + 76) + 1;
    v_stack_m68 = a3;
    v_stack_m98 = v_r10;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_r12 + 8)))) == ((unsigned __int16)(*(unsigned __int8 *)(result + 76)))) goto loc_00853585;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_r12 + 8)))) < 97) goto loc_008535FC;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_r12 + 8)))) > 122) goto loc_008535EF;
    v_r12 = (unsigned __int16)((*(unsigned __int16 *)(*(unsigned __int64 *)(v_r12 + 8))) + ((unsigned __int16)((unsigned int)(0xFFE0ULL))));
loc_00853552:
    if (((unsigned int)(*(unsigned __int8 *)(result + 76))) < 97) goto loc_00853566;
    if (((unsigned int)(*(unsigned __int8 *)(result + 76))) > 122) goto loc_008538F7;
    v_r13 = (unsigned __int16)((*(unsigned __int8 *)(result + 76)) + ((unsigned __int16)((unsigned int)(0xFFE0ULL))));
loc_00853566:
    v_r12 = (unsigned int)(((unsigned __int16)(v_r12)) - ((unsigned int)((unsigned __int16)(v_r13))));
    if (condition_is_not_equal) goto loc_0085359F;
loc_00853585:
    a2 = (unsigned __int16)((v_stack_p70) + ((unsigned __int16)((unsigned int)(0xFFFFULL))));
    result = (unsigned __int16)((v_stack_p50) + ((unsigned __int16)((unsigned int)(0xFFFFULL))));
    goto loc_008534FE;
loc_00853595:
    v_r12 = (unsigned int)(((unsigned __int16)(a2)) - ((unsigned int)((unsigned __int16)(result))));
loc_0085359F:
loc_008535A3:
    if (((*(unsigned __int8 *)(v_stack_m78 + 140)) & (1)) != 0) goto loc_00853750;
    result = HvpReleaseCellPaged(v_stack_m78, v_stack_mB0, v_stack_m68, a4);
loc_008535BD:
    if ((unsigned int)(v_r12) != 0) goto loc_00853606;
    result = 0;
    v_stack_p50 = 0;
    v_stack_p64 = (unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(0xFFFFFFFFULL) + (unsigned __int16)(v_stack_p58) * 8 + 4)));
    goto loc_00853470;
loc_008535E0:
    if (0 == 0xC0000034ULL) goto loc_0085346C;
    goto loc_00853624;
loc_008535EF:
    result = RtlUpcaseUnicodeChar((unsigned __int16)((unsigned int)(v_stack_mB8)), v_stack_mB0, v_stack_m68, a4);
loc_008535FC:
    goto loc_00853552;
loc_00853606:
    a1 = 0;
    goto loc_00853049;
loc_0085360D:
    result = HvpGetCellPaged(a1, v_stack_mB0, v_stack_m68, a4);
    goto loc_008534D3;
loc_00853617:
    result = 0;
    v_stack_mA8 = 0;
loc_0085361F:
    v_stack_p50 = 0;
loc_00853624:
    if (((*(unsigned __int8 *)(v_stack_m78 + 140)) & (1)) != 0) goto loc_008538D4;
    result = HvpReleaseCellPaged(v_stack_m78, v_stack_p68, v_stack_m68, a4);
loc_0085363F:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m70 + 32) + 140)) & (1)) != 0) goto loc_008538DE;
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(v_stack_m70 + 32), v_stack_mC0, v_stack_m68, a4);
loc_0085365D:
    if (0 == 0xC0000034ULL) goto loc_0085338C;
    if (!sign_flag) goto loc_00853761;
    if (((unsigned __int8)(*(unsigned __int8 *)(a11 + 426))) >= 4) goto loc_0085310F;
    *(unsigned int *)(a11 + *(unsigned __int8 *)(a11 + 426) * 8 + 428) = 0;
    *(unsigned int *)(a11 + *(unsigned __int8 *)(a11 + 426) * 8 + 432) = 0x50500ULL;
    goto loc_0085310F;
loc_008536B7:
    result = HvpReleaseCellFlat(a11, v_stack_mC0, v_stack_m68, a4);
    v_r12 = (unsigned int)((v_stack_p10) + 1);
    goto loc_00852F56;
loc_008536C4:
    a4 = 0;
    v_stack_p20 = v_stack_p64;
    result = CmpFindSubKeyInRoot(v_stack_p58, (unsigned int)(0xFFFFFFFFULL), a6, a4);
    if (sign_flag) goto loc_008538C9;
    if (((*(unsigned __int8 *)(v_stack_p58 + 140)) & (1)) != 0) goto loc_0085394E;
    result = HvpReleaseCellPaged(v_stack_p58, v_stack_p68, a6, a4);
loc_00853703:
    if (((unsigned int)((unsigned int)(v_stack_p64))) == -1) goto loc_00853494;
    if (((*(unsigned __int8 *)(v_stack_p58 + 140)) & (1)) == 0) goto loc_0085375A;
    result = HvpGetCellFlat(v_stack_p58, (unsigned int)(v_stack_p64), v_stack_p68, a4);
loc_00853727:
    if (result != 0) goto loc_00852FB3;
loc_00853733:
    v_stack_p50 = (unsigned int)((unsigned int)(0xC000009AULL));
    goto loc_0085363F;
loc_00853743:
    result = RtlUpcaseUnicodeChar((unsigned __int16)(result), (unsigned int)(v_stack_p64), v_stack_p68, a4);
    goto loc_00853000;
loc_00853750:
    result = HvpReleaseCellFlat((unsigned __int16)(result), (unsigned int)(v_stack_p64), v_stack_p68, a4);
    goto loc_008535BD;
loc_0085375A:
    result = HvpGetCellPaged((unsigned __int16)(result), (unsigned int)(v_stack_p64), v_stack_p68, a4);
    goto loc_00853727;
loc_00853761:
    if (((unsigned int)((unsigned int)(v_stack_mA8))) == -1) goto loc_00853392;
loc_00853774:
    v_stack_p40 = v_stack_m88;
    v_r12 = 0;
    v_stack_p38 = (unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a6 + (__int16)(v_stack_mE4) * 8 - 16 * 1 + 24) + 32) + 1648) + a1 + a1 * 2 * 8);
    v_stack_p30 = (unsigned int)(v_rdi);
    v_stack_p28 = a6;
    v_stack_p20 = 0;
    result = CmpCreateKeyControlBlock(*(unsigned __int64 *)(v_stack_p58 + 32), (unsigned int)((unsigned int)((unsigned int)(v_stack_mA8))), v_stack_p58, v_stack_p58);
    v_stack_p50 = (unsigned int)(result);
    if (sign_flag) goto loc_00853A08;
    if (v_stack_p58 == 0) goto loc_008537E5;
    result = -1;
    if (-1 == 1) {
        a4 = 0;
        v_stack_p20 = 0;
        a3 = 0;
        a2 = -1 + 30;
        a1 = -1 + 80;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    v_stack_p58 = v_stack_m88;
    v_stack_m88 = 0;
    if (((unsigned int)((__int16)(v_stack_p60))) >= 2) goto loc_00853A2A;
    *(unsigned __int64 *)(v_stack_p20 + (__int16)(v_stack_p60) * 8 + 8) = v_stack_m88;
loc_0085380F:
    if (((unsigned __int16)((__int16)(v_stack_p60))) == (*(unsigned __int16 *)(v_stack_p8 + 66))) goto loc_008538A4;
    result = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a6 + (__int16)(v_stack_mE4) * 8 - 16 * 1 + 24) + 32) + 1648) + a1 + a1 * 2 * 8))) >> (9));
    result = (unsigned int)((result) ^ ((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a6 + (__int16)(v_stack_mE4) * 8 - 16 * 1 + 24) + 32) + 1648) + a1 + a1 * 2 * 8)));
    result = (unsigned int)((result) * ((unsigned int)(result)));
    a2 = ((unsigned int)((unsigned int)(result))) >> (9);
    a2 = (a2) ^ ((unsigned int)((unsigned int)(result)));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p58 + 32) + 1656))) - 1);
    a2 = (a2) & (a1);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p58 + 32) + 1648) + a2 + a2 * 2 * 8 + 8) = 0;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p58 + 32) + 1648) + a2 + a2 * 2 * 8)) & (-16);
    a2 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p58 + 32) + 1648) + a2 + a2 * 2 * 8) - 16;
    if (a1 <= 16) { a2 = 0; }
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p58 + 32) + 1648) + a2 + a2 * 2 * 8))) & (2)) != 0) goto loc_008538BF;
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p58 + 32) + 1648) + a2 + a2 * 2 * 8))) & (2)) != 0) goto loc_008538BF;
loc_0085387D:
    result = KeAbPostRelease(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p58 + 32) + 1648) + a2 + a2 * 2 * 8, a2, a3, a4);
    if (-1 == 1) goto loc_008538B5;
loc_0085389A:
loc_008538A4:
    v_r15 = (unsigned __int16)(((__int16)(v_stack_p60)) + 1);
    goto loc_00852DEA;
loc_008538B5:
    result = CmpDeleteHive(*(unsigned __int64 *)(v_stack_p58 + 32), a2, a3, a4);
    goto loc_0085389A;
loc_008538BF:
    result = ExfReleasePushLock(v_stack_p58, a2, a3, a4);
    goto loc_0085387D;
loc_008538C9:
    goto loc_0085361F;
loc_008538D4:
    result = HvpReleaseCellFlat(v_stack_p58, a2, a3, a4);
    goto loc_0085363F;
loc_008538DE:
    result = HvpReleaseCellFlat(v_stack_p58, a2, a3, a4);
    goto loc_0085365D;
loc_008538E8:
    goto loc_00852D68;
loc_008538F7:
    result = RtlUpcaseUnicodeChar((unsigned __int16)(v_stack_p8), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 24) + a2 * 8 - 16), a3, a4);
    goto loc_00853566;
loc_00853909:
    a4 = (*(unsigned __int16 *)((unsigned __int16)(v_stack_p8) + 72)) >> (1);
    a2 = (*(unsigned __int16 *)(v_stack_p10)) >> (1);
    v_stack_p20 = 1;
    result = RtlCompareUnicodeStrings(*(unsigned __int64 *)(v_stack_p10 + 8), a2, v_stack_m98, a4);
    goto loc_008535A3;
loc_00853933:
    v_stack_p20 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a6 + (__int16)(v_stack_mE4) * 8 - 16 * 1 + 24) + 32) + 1648) + a1 + a1 * 2 * 8;
    result = KeBugCheckEx(12 + 11 + 58, 12 + 11, *(unsigned __int64 *)(v_stack_p58 + 32), 12);
loc_0085394E:
    result = HvpReleaseCellFlat(12 + 11 + 58, 12 + 11, *(unsigned __int64 *)(v_stack_p58 + 32), 12);
    goto loc_00853703;
loc_00853958:
    goto loc_0085318A;
loc_00853966:
    v_r15 = (unsigned __int16)((*(unsigned __int16 *)(v_stack_p58 + 66)) + 1);
    goto loc_00852DE7;
loc_00853974:
    goto loc_00852C6F;
loc_00853983:
    result = ExfReleasePushLockShared(v_stack_p58 + 72, 12 + 11, *(unsigned __int64 *)(v_stack_p58 + 32), 12);
    goto loc_00852F1A;
loc_00853991:
    result = CmpUnlockHashEntry(*(unsigned __int64 *)(v_stack_p58 + 32), (unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a6 + (__int16)(v_stack_mE4) * 8 - 16 * 1 + 24) + 32) + 1648) + a1 + a1 * 2 * 8)), *(unsigned __int64 *)(v_stack_p58 + 32), 12);
    goto loc_00852C05;
loc_008539A6:
    if (*(unsigned __int64 *)(v_stack_p58 + 192) == 0) goto loc_0085336C;
loc_008539C0:
    if (((unsigned __int16)(*(unsigned __int64 *)(v_stack_p58 + 32))) >= 2) goto loc_00853A38;
    *(unsigned __int64 *)(v_r15 + (__int16)((unsigned __int16)(*(unsigned __int64 *)(v_stack_p58 + 32))) * 8 + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p58 + 192) + 16);
loc_008539D3:
    a1 = (unsigned __int16)((*(unsigned __int64 *)(v_stack_p58 + 32)) - 1);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p58 + 192) + 24) != 0) goto loc_008539C0;
    goto loc_0085336C;
loc_008539E4:
    goto loc_0085330E;
loc_008539F3:
    v_stack_p50 = (unsigned int)((unsigned int)(0xC0000034ULL));
    goto loc_008532C6;
loc_00853A08:
    result = CmpRecordParseFailure(a11, (unsigned int)(0x50700ULL), (unsigned int)((unsigned int)(*(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 24))), (__int16)((unsigned __int16)(*(unsigned __int64 *)(v_stack_p58 + 32))));
    goto loc_0085310F;
loc_00853A2A:
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 24) + (unsigned int)(0xC0000034ULL) * 8 - 16) = *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 24) + v_stack_p58 * 8 - 16);
    goto loc_0085380F;
loc_00853A38:
    *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC0000034ULL) + 24) + (__int16)((unsigned __int16)(*(unsigned __int64 *)(v_stack_p58 + 32))) * 8 - 16) = (unsigned int)((unsigned int)(*(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 24)));
    goto loc_008539D3;
loc_00853A43:
    if (*(unsigned __int64 *)((unsigned int)(0x50700ULL) + 56) == 0) goto loc_008532A1;
    result = (a11 == (*(unsigned __int64 *)((unsigned int)(0x50700ULL) + 56))) ? 1 : 0;
    goto loc_008532AE;
loc_00853A5B:
    goto loc_008530EF;
}
```

## 5. (Beta) C Style

```c
int64_t CmpWalkOneLevel(void *Arg1, void *Arg2, int64_t Arg3, void *Arg4, void *Arg5, void *Arg6, uint32_t Arg7, uint32_t Arg8, int64_t Arg9, uint8_t Arg10, void *Arg11)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg4 = (uint8_t *)Arg4;
    uint8_t *arg5 = (uint8_t *)Arg5;
    uint8_t *arg6 = (uint8_t *)Arg6;
    uint8_t *arg11 = (uint8_t *)Arg11;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m47;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint32_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint32_t v_stack_mA8;
    uint32_t v_stack_mAC;
    uint64_t v_stack_mB0;
    uint32_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint32_t v_stack_mCC;
    uint32_t v_stack_mD0;
    uint32_t v_stack_mD4;
    uint16_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint16_t v_stack_mE2;
    uint16_t v_stack_mE4;
    uint32_t v_stack_mE8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint32_t v_stack_p30;
    uint32_t v_stack_p38;
    uint64_t v_stack_p40;
    uint32_t v_stack_p50;
    uint16_t v_stack_p54;
    uint16_t v_stack_p56;
    uint64_t v_stack_p58;
    uint16_t v_stack_p60;
    uint64_t v_stack_p64;
    uint64_t v_stack_p68;
    uint16_t v_stack_p70;
    uint64_t v_stack_p8;

    v_stack_p20 = Arg4;
    v_stack_p18 = Arg3;
    v_stack_p10 = Arg2;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (248);
    Arg2 = 0;
    v_stack_mC0 = 0;
    v_stack_m88 = 0;
    result = HvpGetCellContextInitialize(v_stack_mC0, Arg2, Arg3, Arg4);
    v_stack_mE2 = -1;
loc_00852C05:
    local_rdi = (uint16_t)((*(uint16_t *)(arg1 + 0x42)) - 1);
    v_stack_mE0 = 0;
    if (!sign_flag) goto loc_008532FB;
    if (0 != 0) goto loc_00853350;
    Arg2 = 0;
    *(uint16_t *)(arg4 + 0x2) = 0xFFFFULL;
    v_stack_mE0 = 0;
loc_00852C2F:
    v_stack_mE4 = 0;
    if (0 > (*(uint16_t *)(v_stack_p8 + 0x42))) goto loc_00852D0E;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg8)))) >> (9));
    result = (uint32_t)((result) ^ ((uint32_t)((uint32_t)(Arg8))));
    result = (uint32_t)((result) * ((uint32_t)(result)));
    local_r15 = ((uint32_t)((uint32_t)(result))) >> (9);
    local_r15 = (local_r15) ^ ((uint32_t)((uint32_t)(result)));
loc_00852C5C:
    if (0 >= 2) goto loc_00853974;
loc_00852C6F:
    Arg3 = 0;
    Arg2 = 0;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + (int16_t)(0) * 8 + 0x8) + 0x20) + 0x678))) - 1);
    Arg1 = (Arg1) & (local_r15);
    result = KeAbPreAcquire(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + (int16_t)(0) * 8 + 0x8) + 0x20) + 0x670) + Arg1 + Arg1 * 2 * 8, Arg2, Arg3, Arg4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + (int16_t)(0) * 8 + 0x8) + 0x20) + 0x670) + Arg1 + Arg1 * 2 * 8;
        Arg2 = result;
        Arg1 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + (int16_t)(0) * 8 + 0x8) + 0x20) + 0x670) + Arg1 + Arg1 * 2 * 8;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + (int16_t)(0) * 8 + 0x8) + 0x20) + 0x670) + arg1 + arg1 * 2 * 8 + 0x8) = *(uint64_t *)(gs_base + (0 + 0x188));
loc_00852CDA:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + (int16_t)(0) * 8 + 0x8) + 0x20) + 0x1088))) == 0) goto loc_00853933;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + (int16_t)(0) * 8 + 0x8) + 0x20) + 0x1088))) != 0) goto loc_00852CDA;
    v_stack_mE2 = 0;
    local_rdi = (uint16_t)((0) + 1);
    if (((uint16_t)(local_rdi)) <= (*(uint16_t *)(v_stack_p8 + 0x42))) goto loc_00852C5C;
    Arg2 = 0;
loc_00852D0E:
    if (0 > ((uint16_t)(*(uint16_t *)(arg2 + 0x2)))) goto loc_00852D48;
loc_00852D20:
    if (0 >= 2) goto loc_008532DF;
loc_00852D33:
    result = CmpLockKcbShared(*(uint64_t *)(arg2 + (int16_t)(0) * 8 + 0x8), Arg2, Arg3, Arg4);
    local_rdi = (uint16_t)((0) + 1);
    if (((uint16_t)(local_rdi)) <= ((uint16_t)(*(uint16_t *)(arg2 + 0x2)))) goto loc_00852D20;
    Arg2 = 0;
loc_00852D48:
    v_stack_m80 = 0;
loc_00852D4C:
    if (sign_flag) goto loc_00853093;
    if (((uint16_t)(*(uint16_t *)(arg2 + 0x2))) >= 2) goto loc_008538E8;
loc_00852D68:
    if ((*(uint16_t *)(*(uint64_t *)(arg2 + (int16_t)((uint16_t)(*(uint16_t *)(arg2 + 0x2))) * 8 + 0x8) + 0x42)) == 0) goto loc_00852D79;
    if ((*(uint8_t *)(*(uint64_t *)(arg2 + (int16_t)((uint16_t)(*(uint16_t *)(arg2 + 0x2))) * 8 + 0x8) + 0x41)) == 1) goto loc_00853093;
loc_00852D79:
    if ((*(uint32_t *)(*(uint64_t *)(arg2 + (int16_t)((uint16_t)(*(uint16_t *)(arg2 + 0x2))) * 8 + 0x8) + 0x28)) == -1) goto loc_00853066;
    if (Arg9 != 0) goto loc_00853243;
loc_00852D93:
    if (*(uint64_t *)(v_stack_p8 + 0xF0) != 0) goto loc_00853286;
loc_00852DA3:
    if (((*(uint32_t *)(v_stack_p8 + 0xB8)) & (0x20000ULL)) != 0) goto loc_008539F3;
    result = (uint32_t)(*(uint32_t *)(arg11 + 0xA0));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg11 + 0xA0)))) & (1)) == 0) {
        Arg1 = Arg11 + 168;
        result = CmpAttachToRegistryProcess(Arg1, *(uint64_t *)(v_stack_p8 + 0xF0), Arg3, Arg4);
    }
    if (v_stack_mE0 != 0) goto loc_00853966;
    result = 0;
loc_00852DE7:
loc_00852DEA:
    v_stack_mD8 = 0;
    if (0 > (*(uint16_t *)(v_stack_p8 + 0x42))) goto loc_008530E0;
    if (0 >= 2) goto loc_00853402;
loc_00852E0F:
    v_stack_m70 = *(uint64_t *)(arg2 + (int16_t)(0) * 8 + 0x8);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + (int16_t)(0) * 8 + 0x8) + 0x28)))) == -1) goto loc_00853384;
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + (int16_t)(0) * 8 + 0x8) + 0x20) + 0x8C)) & (1)) == 0) goto loc_00853052;
    result = HvpGetCellFlat(*(uint64_t *)(*(uint64_t *)(arg2 + (int16_t)(0) * 8 + 0x8) + 0x20), (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + (int16_t)(0) * 8 + 0x8) + 0x28)), v_stack_mC0, Arg4);
loc_00852E3A:
    v_stack_mA0 = result;
    if (((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + (int16_t)(0) * 8 + 0x8) + 0x20) + 0xA0)) & (0x8001ULL)) != 0) goto loc_00852F23;
    if (((*(uint8_t *)(v_rip + 0x5BBE35)) & ((uint8_t)(*(uint8_t *)(result + 0xC)))) != 0) goto loc_00852F23;
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + (int16_t)(0) * 8 + 0x8) + 0x20) + 0x8C)) & (1)) != 0) goto loc_0085337A;
    result = HvpReleaseCellPaged(*(uint64_t *)(*(uint64_t *)(arg2 + (int16_t)(0) * 8 + 0x8) + 0x20), v_stack_mC0, v_stack_mC0, Arg4);
loc_00852E7B:
    Arg3 = 0;
    local_rsi = (*(uint64_t *)(*(uint64_t *)(arg2 + (int16_t)(0) * 8 + 0x8) + 0x20)) + (72);
    Arg2 = 0;
    result = KeAbPreAcquire(local_rsi, Arg2, Arg3, Arg4);
    result = 0;
    if (!(condition_is_equal)) {
        Arg4 = local_rsi;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = local_rsi;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + (int16_t)(0) * 8 + 0x8) + 0x20) + 0x8C)) & (1)) == 0) goto loc_0085305C;
    result = HvpGetCellFlat(*(uint64_t *)(*(uint64_t *)(arg2 + (int16_t)(0) * 8 + 0x8) + 0x20), (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + (int16_t)(0) * 8 + 0x8) + 0x28)), v_stack_mC0, Arg4);
loc_00852EDA:
    v_stack_mA0 = result;
    if (((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + (int16_t)(0) * 8 + 0x8) + 0x20) + 0xA0)) & (0x8001ULL)) != 0) goto loc_00852F05;
    if (((*(uint8_t *)(v_rip + 0x5BBD95)) & ((uint8_t)(*(uint8_t *)(result + 0xC)))) == 0) goto loc_0085306E;
loc_00852F05:
    Arg1 = 0;
    if (condition_is_not_equal) goto loc_00853983;
loc_00852F1A:
    result = KeAbPostRelease(*(uint64_t *)(*(uint64_t *)(arg2 + (int16_t)(0) * 8 + 0x8) + 0x20) + 72, (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + (int16_t)(0) * 8 + 0x8) + 0x28)), v_stack_mC0, Arg4);
loc_00852F23:
    Arg2 = 0;
    v_stack_m78 = *(uint64_t *)(*(uint64_t *)(arg2 + (int16_t)(0) * 8 + 0x8) + 0x20);
    v_stack_mE8 = (uint32_t)((uint32_t)(0xC0000034ULL));
    v_stack_mCC = 0;
    v_stack_mD4 = 0;
    v_stack_m90 = 0;
    v_stack_mA8 = (uint32_t)((uint32_t)(0xFFFFFFFFULL));
    v_stack_mD0 = 0xFFFFFFFFULL;
loc_00852F56:
    v_stack_mB8 = 0;
    if (0 >= (*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + (int16_t)(0) * 8 + 0x8) + 0x20) + 0xD8))) goto loc_0085363F;
    if ((*(uint32_t *)(v_stack_mA0 + 0x0 * 4 + 0x14)) == 0) goto loc_00853494;
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + (int16_t)(0) * 8 + 0x8) + 0x20) + 0x8C)) & (1)) == 0) goto loc_0085349C;
    result = HvpGetCellFlat(*(uint64_t *)(*(uint64_t *)(arg2 + (int16_t)(0) * 8 + 0x8) + 0x20), (uint32_t)(*(uint32_t *)(v_stack_mA0 + 0x0 * 4 + 0x1C)), v_stack_mD0, Arg4);
loc_00852F98:
    if (result == 0) goto loc_00853733;
    if ((*(uint16_t *)(result)) == ((uint16_t)((uint32_t)(0x6972ULL)))) goto loc_008536C4;
loc_00852FB3:
    if ((*(uint16_t *)(result)) != ((uint16_t)((uint32_t)(0x686CULL)))) goto loc_00853431;
    Arg1 = 0;
    v_stack_m60 = v_xmm0;
    if (((uint16_t)((uint32_t)(0x686CULL))) < 2) goto loc_0085301E;
    local_r12 = ((uint16_t)((uint32_t)(0x686CULL))) >> (1);
loc_00852FE9:
    if (((uint16_t)(*(uint16_t *)(v_stack_m58))) < 97) goto loc_00853000;
    if (((uint16_t)(*(uint16_t *)(v_stack_m58))) > 122) goto loc_00853743;
    result = (uint16_t)((*(uint16_t *)(v_stack_m58)) - (32));
loc_00853000:
    local_r15 = (uint32_t)((0) * (0));
    local_rsi = (v_stack_m58) + (2);
    local_r15 = (uint32_t)((local_r15) + ((uint32_t)((uint16_t)(result))));
    local_r12 = (local_r12) - (1);
    if (condition_is_not_equal) goto loc_00852FE9;
    Arg1 = 0;
    v_stack_m58 = local_rsi;
loc_0085301E:
    v_stack_mD4 = 0xFFFFFFFFULL;
loc_00853030:
    if (0 >= (*(uint16_t *)(result + 0x2))) goto loc_00853420;
    if (((uint32_t)(local_r15)) == (*(uint32_t *)(result + 0x0 * 8 + 0x8))) goto loc_008534A6;
loc_00853049:
    local_rsi = (uint16_t)((0) + 1);
    goto loc_00853030;
loc_00853052:
    result = HvpGetCellPaged(Arg1, (uint32_t)(*(uint32_t *)(v_stack_mA0 + 0x0 * 4 + 0x1C)), v_stack_mD0, Arg4);
    goto loc_00852E3A;
loc_0085305C:
    result = HvpGetCellPaged(Arg1, (uint32_t)(*(uint32_t *)(v_stack_mA0 + 0x0 * 4 + 0x1C)), v_stack_mD0, Arg4);
    goto loc_00852EDA;
loc_00853066:
    Arg1 = (uint16_t)((Arg1) - 1);
    goto loc_00852D4C;
loc_0085306E:
    Arg3 = 0;
    result = HvpMarkCellDirty(Arg1, (uint32_t)(*(uint32_t *)(v_stack_mA0 + 0x0 * 4 + 0x1C)), Arg3, 1);
    if (sign_flag) goto loc_00852F05;
    goto loc_00852F05;
loc_00853093:
    v_stack_mE8 = (uint32_t)((uint32_t)(0xC0000034ULL));
    if (Arg11 == NULL) goto loc_008532D5;
    if (((uint8_t)(*(uint8_t *)(arg11 + 0x1AA))) >= 4) goto loc_0085310F;
    *(uint32_t *)(arg11 + *(uint8_t *)(arg11 + 0x1AA) * 8 + 0x1AC) = (uint32_t)((uint32_t)(0xC0000034ULL));
    *(uint32_t *)(arg11 + *(uint8_t *)(arg11 + 0x1AA) * 8 + 0x1B0) = 0x50200ULL;
    goto loc_0085310F;
loc_008530E0:
    if (Arg10 != 0) goto loc_00853A5B;
loc_008530EF:
    result = (Arg10 != 0) ? 1 : 0;
    local_r15 = 0;
    v_stack_mE0 = 0;
    v_stack_mE8 = 0;
    *(uint8_t *)(arg5) = (uint8_t)(result);
    *(uint64_t *)(v_stack_p18) = local_rsi;
loc_0085310F:
    result = 0;
    if (0 > (*(uint16_t *)(arg6 + 0x2))) goto loc_00853143;
loc_00853120:
    if (0 >= 2) goto loc_00853411;
loc_00853133:
    result = CmpUnlockKcb(*(uint64_t *)(arg6 + (int16_t)(0) * 8 + 0x8), (uint32_t)(*(uint32_t *)(v_stack_mA0 + 0x0 * 4 + 0x1C)), Arg3, 1);
    local_rdi = (uint16_t)((0) + 1);
    if (((uint16_t)(local_rdi)) <= (*(uint16_t *)(arg6 + 0x2))) goto loc_00853120;
loc_00853143:
    if (((uint16_t)((int16_t)(v_stack_mE4))) > v_stack_mE2) goto loc_0085321E;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg8)))) >> (9));
    result = (uint32_t)((result) ^ ((uint32_t)((uint32_t)(Arg8))));
    result = (uint32_t)((result) * ((uint32_t)(result)));
    local_rsi = ((uint32_t)((uint32_t)(result))) >> (9);
    local_rsi = (local_rsi) ^ ((uint32_t)((uint32_t)(result)));
    local_r13 = 0;
loc_0085317B:
    if (((uint16_t)((int16_t)(v_stack_mE4))) >= 2) goto loc_00853958;
loc_0085318A:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg6 + (int16_t)(v_stack_mE4) * 8 - 0x10 * 1 + 0x18) + 0x20) + 0x678))) - 1);
    Arg1 = (Arg1) & (local_rsi);
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg6 + (int16_t)(v_stack_mE4) * 8 - 0x10 * 1 + 0x18) + 0x20) + 0x670) + arg1 + arg1 * 2 * 8 + 0x8) = 0;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg6 + (int16_t)(v_stack_mE4) * 8 - 0x10 * 1 + 0x18) + 0x20) + 0x670) + arg1 + arg1 * 2 * 8)) & (-16);
    Arg2 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg6 + (int16_t)(v_stack_mE4) * 8 - 0x10 * 1 + 0x18) + 0x20) + 0x670) + arg1 + arg1 * 2 * 8) - 16;
    if (Arg1 <= 16) { Arg2 = 0; }
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg6 + (int16_t)(v_stack_mE4) * 8 - 0x10 * 1 + 0x18) + 0x20) + 0x670) + arg1 + arg1 * 2 * 8))) & (2)) != 0) goto loc_008532EE;
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg6 + (int16_t)(v_stack_mE4) * 8 - 0x10 * 1 + 0x18) + 0x20) + 0x670) + arg1 + arg1 * 2 * 8))) & (2)) != 0) goto loc_008532EE;
loc_008531D8:
    result = KeAbPostRelease(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg6 + (int16_t)(v_stack_mE4) * 8 - 0x10 * 1 + 0x18) + 0x20) + 0x670) + Arg1 + Arg1 * 2 * 8, Arg2, Arg3, 1);
    result = (uint32_t)((uint32_t)(local_r13 - 1));
    if (((uint32_t)((uint32_t)((uint32_t)(local_r13 - 1)))) == 1) {
        Arg1 = *(uint64_t *)(*(uint64_t *)(arg6 + (int16_t)(v_stack_mE4) * 8 - 0x10 * 1 + 0x18) + 0x20);
        result = CmpDeleteHive(Arg1, Arg2, Arg3, 1);
    }
    local_r14 = ((int16_t)(v_stack_mE4) * 8 - 16) + (8);
    Arg2 = (uint16_t)((v_stack_mE4) + 1);
    v_stack_mE4 = (uint16_t)(Arg2);
    if (((uint16_t)(Arg2)) <= v_stack_mE2) goto loc_0085317B;
loc_0085321E:
    if (v_stack_mE0 != 0) {
        Arg1 = v_stack_mE0;
        result = CmpDereferenceKeyControlBlock(Arg1, Arg2, Arg3, 1);
    }
    local_rsp = (local_rsp) + (248);
    return (uint32_t)((uint32_t)((uint32_t)(v_stack_mE8)));
loc_00853243:
loc_00853248:
    result = CmListGetNextElement(*(uint64_t *)(arg6 + 0x8) + 208, v_stack_m80, 32, *(uint64_t *)(arg6 + 0x8));
    if (result == 0) goto loc_00852D93;
    if ((*(uint32_t *)(result + 0x44)) != 2) goto loc_00853248;
    result = CmEqualTrans(*(uint64_t *)(result + 0x38), *(uint64_t *)(*(uint64_t *)(arg6 + (int16_t)(v_stack_mE4) * 8 - 0x10 * 1 + 0x18) + 0x20), 32, *(uint64_t *)(arg6 + 0x8));
    if ((uint8_t)(result) == 0) goto loc_00852D93;
    goto loc_00853093;
loc_00853286:
    if (*(uint64_t *)(*(uint64_t *)(arg6 + (int16_t)(v_stack_mE4) * 8 - 0x10 * 1 + 0x18) + 0x20) == 0) goto loc_008532B6;
    if ((*(uint64_t *)(*(uint64_t *)(arg6 + (int16_t)(v_stack_mE4) * 8 - 0x10 * 1 + 0x18) + 0x20)) == (*(uint64_t *)(*(uint64_t *)(arg6 + (int16_t)(v_stack_mE4) * 8 - 0x10 * 1 + 0x18) + 0x20))) goto loc_00852DA3;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg6 + (int16_t)(v_stack_mE4) * 8 - 0x10 * 1 + 0x18) + 0x20) + 0x38) != 0) goto loc_00853A43;
loc_008532A1:
    Arg2 = (*(uint64_t *)(*(uint64_t *)(arg6 + (int16_t)(v_stack_mE4) * 8 - 0x10 * 1 + 0x18) + 0x20)) + (88);
    result = CmpTransUowIsEqual(*(uint64_t *)(*(uint64_t *)(arg6 + (int16_t)(v_stack_mE4) * 8 - 0x10 * 1 + 0x18) + 0x20) + 88, Arg2, 32, *(uint64_t *)(arg6 + 0x8));
loc_008532AE:
    if ((uint8_t)(result) != 0) goto loc_00852DA3;
loc_008532B6:
    v_stack_p50 = (uint32_t)((uint32_t)(0xC0000034ULL));
loc_008532C6:
    result = CmpRecordParseFailure(Arg11, (uint32_t)(0x50300ULL), (uint32_t)((uint32_t)((uint32_t)(0xC0000034ULL))), *(uint64_t *)(arg6 + 0x8));
loc_008532D5:
    goto loc_0085310F;
loc_008532DF:
    goto loc_00852D33;
loc_008532EE:
    result = ExfReleasePushLock(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg6 + (int16_t)(v_stack_mE4) * 8 - 0x10 * 1 + 0x18) + 0x20) + 0x670) + Arg1 + Arg1 * 2 * 8, (uint32_t)(0x50300ULL), (uint32_t)((uint32_t)((uint32_t)(0xC0000034ULL))), *(uint64_t *)(arg6 + 0x8));
    goto loc_008531D8;
loc_008532FB:
    if (((uint16_t)(*(uint64_t *)(*(uint64_t *)(arg6 + (int16_t)(v_stack_mE4) * 8 - 0x10 * 1 + 0x18) + 0x20))) >= 2) goto loc_008539E4;
loc_0085330E:
    result = CmpLockHashEntryShared(*(uint64_t *)(*(uint64_t *)(arg6 + (int16_t)((uint16_t)(*(uint64_t *)(*(uint64_t *)(arg6 + (int16_t)(v_stack_mE4) * 8 - 0x10 * 1 + 0x18) + 0x20))) * 8 + 0x8) + 0x20), (uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg6 + (int16_t)(v_stack_mE4) * 8 - 0x10 * 1 + 0x18) + 0x20) + 0x670) + Arg1 + Arg1 * 2 * 8)), (uint32_t)((uint32_t)((uint32_t)(0xC0000034ULL))), *(uint64_t *)(arg6 + 0x8));
    result = CmpFindKcbInHashEntryByName(*(uint64_t *)(*(uint64_t *)(arg6 + (int16_t)((uint16_t)(*(uint64_t *)(*(uint64_t *)(arg6 + (int16_t)(v_stack_mE4) * 8 - 0x10 * 1 + 0x18) + 0x20))) * 8 + 0x8) + 0x20), (uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg6 + (int16_t)(v_stack_mE4) * 8 - 0x10 * 1 + 0x18) + 0x20) + 0x670) + Arg1 + Arg1 * 2 * 8)), *(uint64_t *)(arg6 + (int16_t)((uint16_t)(*(uint64_t *)(*(uint64_t *)(arg6 + (int16_t)(v_stack_mE4) * 8 - 0x10 * 1 + 0x18) + 0x20))) * 8 + 0x8), local_r14);
    v_stack_p58 = result;
    if (result == 0) goto loc_00853991;
    result = CmpReferenceKeyControlBlockLockNotHeld(result, (uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg6 + (int16_t)(v_stack_mE4) * 8 - 0x10 * 1 + 0x18) + 0x20) + 0x670) + Arg1 + Arg1 * 2 * 8)), *(uint64_t *)(arg6 + (int16_t)((uint16_t)(*(uint64_t *)(*(uint64_t *)(arg6 + (int16_t)(v_stack_mE4) * 8 - 0x10 * 1 + 0x18) + 0x20))) * 8 + 0x8), local_r14);
    result = CmpUnlockHashEntry(*(uint64_t *)(*(uint64_t *)(arg6 + (int16_t)((uint16_t)(*(uint64_t *)(*(uint64_t *)(arg6 + (int16_t)(v_stack_mE4) * 8 - 0x10 * 1 + 0x18) + 0x20))) * 8 + 0x8) + 0x20), (uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg6 + (int16_t)(v_stack_mE4) * 8 - 0x10 * 1 + 0x18) + 0x20) + 0x670) + Arg1 + Arg1 * 2 * 8)), *(uint64_t *)(arg6 + (int16_t)((uint16_t)(*(uint64_t *)(*(uint64_t *)(arg6 + (int16_t)(v_stack_mE4) * 8 - 0x10 * 1 + 0x18) + 0x20))) * 8 + 0x8), local_r14);
loc_00853350:
    *(uint16_t *)((uint32_t)(0xC0000034ULL) + 0x2) = (uint16_t)(*(uint16_t *)(v_stack_p58 + 0x42));
    if ((uint16_t)((int16_t)(*(uint16_t *)(v_stack_p58 + 0x42))) != 0) goto loc_008539A6;
    *(uint64_t *)((uint32_t)(0xC0000034ULL) + (int16_t)(*(uint16_t *)(v_stack_p58 + 0x42)) * 8 + 0x8) = v_stack_p58;
loc_0085336C:
    local_rdi = (uint16_t)((*(uint16_t *)(v_stack_p58 + 0x42)) + 1);
    Arg2 = 0;
    goto loc_00852C2F;
loc_0085337A:
    result = HvpReleaseCellFlat((int16_t)(*(uint16_t *)(v_stack_p58 + 0x42)), Arg2, *(uint64_t *)(arg6 + (int16_t)((uint16_t)(*(uint64_t *)(*(uint64_t *)(arg6 + (int16_t)(v_stack_mE4) * 8 - 0x10 * 1 + 0x18) + 0x20))) * 8 + 0x8), local_r14);
    goto loc_00852E7B;
loc_00853384:
    goto loc_0085339B;
loc_0085338C:
loc_00853392:
loc_0085339B:
    if ((*(uint16_t *)(v_stack_p8 + 0x42)) != 0) goto loc_00853774;
    if (Arg10 != 0) goto loc_00853774;
    v_stack_p50 = (uint32_t)((uint32_t)(0xC0000034ULL));
    if (((uint8_t)(*(uint8_t *)(arg11 + 0x1AA))) >= 4) goto loc_0085310F;
    *(uint32_t *)(arg11 + *(uint8_t *)(arg11 + 0x1AA) * 8 + 0x1AC) = (uint32_t)((uint32_t)(0xC0000034ULL));
    *(uint32_t *)(arg11 + *(uint8_t *)(arg11 + 0x1AA) * 8 + 0x1B0) = 0x50600ULL;
    goto loc_0085310F;
loc_00853402:
    goto loc_00852E0F;
loc_00853411:
    goto loc_00853133;
loc_00853420:
    v_stack_p50 = (uint32_t)((uint32_t)(0xC0000034ULL));
    goto loc_00853479;
loc_00853431:
    v_stack_p28 = v_stack_m90;
    Arg4 = 0;
    v_stack_p20 = v_stack_p64;
    result = CmpFindSubKeyInLeafWithStatus(*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x18) + arg11 * 8 - 0x10), (uint32_t)(0xFFFFFFFFULL), Arg6, Arg4);
    v_stack_p50 = (uint32_t)(result);
    result = (uint32_t)((result) + ((uint32_t)((uint32_t)(0x80000000ULL))));
    if ((((uint32_t)((uint32_t)(0x80000000ULL))) & ((uint32_t)(result))) == 0) goto loc_008535E0;
loc_0085346C:
loc_00853470:
    if (((uint32_t)((uint32_t)(v_stack_p64))) != -1) goto loc_00853617;
loc_00853479:
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x18) + arg11 * 8 - 0x10) + 0x8C)) & (1)) != 0) goto loc_008536B7;
    result = HvpReleaseCellPaged(*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x18) + arg11 * 8 - 0x10), v_stack_p68, Arg6, Arg4);
loc_00853494:
    local_r12 = (uint32_t)(((uint32_t)(v_stack_mB8)) + 1);
    goto loc_00852F56;
loc_0085349C:
    result = HvpGetCellPaged(*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x18) + arg11 * 8 - 0x10), v_stack_p68, Arg6, Arg4);
    goto loc_00852F98;
loc_008534A6:
    v_stack_mB0 = 0xFFFFFFFFULL;
    v_stack_mAC = 0;
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x18) + arg11 * 8 - 0x10) + 0x8C)) & (1)) == 0) goto loc_0085360D;
    result = HvpGetCellFlat(*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x18) + arg11 * 8 - 0x10), (uint32_t)(*(uint32_t *)((uint32_t)(0xFFFFFFFFULL) + result * 8 + 0x4)), v_stack_mB0, Arg4);
loc_008534D3:
    if (result == 0) goto loc_008538C9;
    if (((*(uint8_t *)(result + 0x2)) & (32)) == 0) goto loc_00853909;
    Arg2 = (uint16_t)((*(uint16_t *)(local_r12)) >> (1));
loc_008534FE:
    v_stack_p50 = (uint16_t)(*(uint16_t *)(result + 0x48));
    v_stack_p70 = (uint16_t)(Arg2);
    if ((uint16_t)(Arg2) == 0) goto loc_00853595;
    if ((uint16_t)(*(uint16_t *)(result + 0x48)) == 0) goto loc_00853595;
    Arg3 = (*(uint64_t *)(local_r12 + 0x8)) + (2);
    local_r10 = (result + 76) + 1;
    v_stack_m68 = Arg3;
    v_stack_m98 = local_r10;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(local_r12 + 0x8)))) == ((uint16_t)(*(uint8_t *)(result + 0x4C)))) goto loc_00853585;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(local_r12 + 0x8)))) < 97) goto loc_008535FC;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(local_r12 + 0x8)))) > 122) goto loc_008535EF;
    local_r12 = (uint16_t)((*(uint16_t *)(*(uint64_t *)(local_r12 + 0x8))) + ((uint16_t)((uint32_t)(0xFFE0ULL))));
loc_00853552:
    if (((uint32_t)(*(uint8_t *)(result + 0x4C))) < 97) goto loc_00853566;
    if (((uint32_t)(*(uint8_t *)(result + 0x4C))) > 122) goto loc_008538F7;
    local_r13 = (uint16_t)((*(uint8_t *)(result + 0x4C)) + ((uint16_t)((uint32_t)(0xFFE0ULL))));
loc_00853566:
    local_r12 = (uint32_t)(((uint16_t)(local_r12)) - ((uint32_t)((uint16_t)(local_r13))));
    if (condition_is_not_equal) goto loc_0085359F;
loc_00853585:
    Arg2 = (uint16_t)((v_stack_p70) + ((uint16_t)((uint32_t)(0xFFFFULL))));
    result = (uint16_t)((v_stack_p50) + ((uint16_t)((uint32_t)(0xFFFFULL))));
    goto loc_008534FE;
loc_00853595:
    local_r12 = (uint32_t)(((uint16_t)(Arg2)) - ((uint32_t)((uint16_t)(result))));
loc_0085359F:
loc_008535A3:
    if (((*(uint8_t *)(v_stack_m78 + 0x8C)) & (1)) != 0) goto loc_00853750;
    result = HvpReleaseCellPaged(v_stack_m78, v_stack_mB0, v_stack_m68, Arg4);
loc_008535BD:
    if ((uint32_t)(local_r12) != 0) goto loc_00853606;
    result = 0;
    v_stack_p50 = 0;
    v_stack_p64 = (uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(0xFFFFFFFFULL) + (uint16_t)(v_stack_p58) * 8 + 0x4)));
    goto loc_00853470;
loc_008535E0:
    if (0 == 0xC0000034ULL) goto loc_0085346C;
    goto loc_00853624;
loc_008535EF:
    result = RtlUpcaseUnicodeChar((uint16_t)((uint32_t)(v_stack_mB8)), v_stack_mB0, v_stack_m68, Arg4);
loc_008535FC:
    goto loc_00853552;
loc_00853606:
    Arg1 = 0;
    goto loc_00853049;
loc_0085360D:
    result = HvpGetCellPaged(Arg1, v_stack_mB0, v_stack_m68, Arg4);
    goto loc_008534D3;
loc_00853617:
    result = 0;
    v_stack_mA8 = 0;
loc_0085361F:
    v_stack_p50 = 0;
loc_00853624:
    if (((*(uint8_t *)(v_stack_m78 + 0x8C)) & (1)) != 0) goto loc_008538D4;
    result = HvpReleaseCellPaged(v_stack_m78, v_stack_p68, v_stack_m68, Arg4);
loc_0085363F:
    if (((*(uint8_t *)(*(uint64_t *)(v_stack_m70 + 0x20) + 0x8C)) & (1)) != 0) goto loc_008538DE;
    result = HvpReleaseCellPaged(*(uint64_t *)(v_stack_m70 + 0x20), v_stack_mC0, v_stack_m68, Arg4);
loc_0085365D:
    if (0 == 0xC0000034ULL) goto loc_0085338C;
    if (!sign_flag) goto loc_00853761;
    if (((uint8_t)(*(uint8_t *)(arg11 + 0x1AA))) >= 4) goto loc_0085310F;
    *(uint32_t *)(arg11 + *(uint8_t *)(arg11 + 0x1AA) * 8 + 0x1AC) = 0;
    *(uint32_t *)(arg11 + *(uint8_t *)(arg11 + 0x1AA) * 8 + 0x1B0) = 0x50500ULL;
    goto loc_0085310F;
loc_008536B7:
    result = HvpReleaseCellFlat(Arg11, v_stack_mC0, v_stack_m68, Arg4);
    local_r12 = (uint32_t)((v_stack_p10) + 1);
    goto loc_00852F56;
loc_008536C4:
    Arg4 = 0;
    v_stack_p20 = v_stack_p64;
    result = CmpFindSubKeyInRoot(v_stack_p58, (uint32_t)(0xFFFFFFFFULL), Arg6, Arg4);
    if (sign_flag) goto loc_008538C9;
    if (((*(uint8_t *)(v_stack_p58 + 0x8C)) & (1)) != 0) goto loc_0085394E;
    result = HvpReleaseCellPaged(v_stack_p58, v_stack_p68, Arg6, Arg4);
loc_00853703:
    if (((uint32_t)((uint32_t)(v_stack_p64))) == -1) goto loc_00853494;
    if (((*(uint8_t *)(v_stack_p58 + 0x8C)) & (1)) == 0) goto loc_0085375A;
    result = HvpGetCellFlat(v_stack_p58, (uint32_t)(v_stack_p64), v_stack_p68, Arg4);
loc_00853727:
    if (result != 0) goto loc_00852FB3;
loc_00853733:
    v_stack_p50 = (uint32_t)((uint32_t)(0xC000009AULL));
    goto loc_0085363F;
loc_00853743:
    result = RtlUpcaseUnicodeChar((uint16_t)(result), (uint32_t)(v_stack_p64), v_stack_p68, Arg4);
    goto loc_00853000;
loc_00853750:
    result = HvpReleaseCellFlat((uint16_t)(result), (uint32_t)(v_stack_p64), v_stack_p68, Arg4);
    goto loc_008535BD;
loc_0085375A:
    result = HvpGetCellPaged((uint16_t)(result), (uint32_t)(v_stack_p64), v_stack_p68, Arg4);
    goto loc_00853727;
loc_00853761:
    if (((uint32_t)((uint32_t)(v_stack_mA8))) == -1) goto loc_00853392;
loc_00853774:
    v_stack_p40 = v_stack_m88;
    local_r12 = 0;
    v_stack_p38 = (uint32_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg6 + (int16_t)(v_stack_mE4) * 8 - 0x10 * 1 + 0x18) + 0x20) + 0x670) + Arg1 + Arg1 * 2 * 8);
    v_stack_p30 = (uint32_t)(local_rdi);
    v_stack_p28 = Arg6;
    v_stack_p20 = 0;
    result = CmpCreateKeyControlBlock(*(uint64_t *)(v_stack_p58 + 0x20), (uint32_t)((uint32_t)((uint32_t)(v_stack_mA8))), v_stack_p58, v_stack_p58);
    v_stack_p50 = (uint32_t)(result);
    if (sign_flag) goto loc_00853A08;
    if (v_stack_p58 == 0) goto loc_008537E5;
    result = -1;
    if (-1 == 1) {
        Arg4 = 0;
        v_stack_p20 = 0;
        Arg3 = 0;
        Arg2 = -1 + 30;
        Arg1 = -1 + 80;
        result = KeBugCheckEx(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_p58 = v_stack_m88;
    v_stack_m88 = 0;
    if (((uint32_t)((int16_t)(v_stack_p60))) >= 2) goto loc_00853A2A;
    *(uint64_t *)(v_stack_p20 + (int16_t)(v_stack_p60) * 8 + 0x8) = v_stack_m88;
loc_0085380F:
    if (((uint16_t)((int16_t)(v_stack_p60))) == (*(uint16_t *)(v_stack_p8 + 0x42))) goto loc_008538A4;
    result = (uint32_t)(((uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg6 + (int16_t)(v_stack_mE4) * 8 - 0x10 * 1 + 0x18) + 0x20) + 0x670) + Arg1 + Arg1 * 2 * 8))) >> (9));
    result = (uint32_t)((result) ^ ((uint32_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg6 + (int16_t)(v_stack_mE4) * 8 - 0x10 * 1 + 0x18) + 0x20) + 0x670) + Arg1 + Arg1 * 2 * 8)));
    result = (uint32_t)((result) * ((uint32_t)(result)));
    Arg2 = ((uint32_t)((uint32_t)(result))) >> (9);
    Arg2 = (Arg2) ^ ((uint32_t)((uint32_t)(result)));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p58 + 0x20) + 0x678))) - 1);
    Arg2 = (Arg2) & (Arg1);
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p58 + 0x20) + 0x670) + arg2 + arg2 * 2 * 8 + 0x8) = 0;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p58 + 0x20) + 0x670) + arg2 + arg2 * 2 * 8)) & (-16);
    Arg2 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p58 + 0x20) + 0x670) + arg2 + arg2 * 2 * 8) - 16;
    if (Arg1 <= 16) { Arg2 = 0; }
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p58 + 0x20) + 0x670) + arg2 + arg2 * 2 * 8))) & (2)) != 0) goto loc_008538BF;
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p58 + 0x20) + 0x670) + arg2 + arg2 * 2 * 8))) & (2)) != 0) goto loc_008538BF;
loc_0085387D:
    result = KeAbPostRelease(*(uint64_t *)(*(uint64_t *)(v_stack_p58 + 0x20) + 0x670) + Arg2 + Arg2 * 2 * 8, Arg2, Arg3, Arg4);
    if (-1 == 1) goto loc_008538B5;
loc_0085389A:
loc_008538A4:
    local_r15 = (uint16_t)(((int16_t)(v_stack_p60)) + 1);
    goto loc_00852DEA;
loc_008538B5:
    result = CmpDeleteHive(*(uint64_t *)(v_stack_p58 + 0x20), Arg2, Arg3, Arg4);
    goto loc_0085389A;
loc_008538BF:
    result = ExfReleasePushLock(v_stack_p58, Arg2, Arg3, Arg4);
    goto loc_0085387D;
loc_008538C9:
    goto loc_0085361F;
loc_008538D4:
    result = HvpReleaseCellFlat(v_stack_p58, Arg2, Arg3, Arg4);
    goto loc_0085363F;
loc_008538DE:
    result = HvpReleaseCellFlat(v_stack_p58, Arg2, Arg3, Arg4);
    goto loc_0085365D;
loc_008538E8:
    goto loc_00852D68;
loc_008538F7:
    result = RtlUpcaseUnicodeChar((uint16_t)(v_stack_p8), *(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x18) + arg2 * 8 - 0x10), Arg3, Arg4);
    goto loc_00853566;
loc_00853909:
    Arg4 = (*(uint16_t *)((uint16_t)(v_stack_p8) + 0x48)) >> (1);
    Arg2 = (*(uint16_t *)(v_stack_p10)) >> (1);
    v_stack_p20 = 1;
    result = RtlCompareUnicodeStrings(*(uint64_t *)(v_stack_p10 + 0x8), Arg2, v_stack_m98, Arg4);
    goto loc_008535A3;
loc_00853933:
    v_stack_p20 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg6 + (int16_t)(v_stack_mE4) * 8 - 0x10 * 1 + 0x18) + 0x20) + 0x670) + Arg1 + Arg1 * 2 * 8;
    result = KeBugCheckEx(12 + 11 + 58, 12 + 11, *(uint64_t *)(v_stack_p58 + 0x20), 12);
loc_0085394E:
    result = HvpReleaseCellFlat(12 + 11 + 58, 12 + 11, *(uint64_t *)(v_stack_p58 + 0x20), 12);
    goto loc_00853703;
loc_00853958:
    goto loc_0085318A;
loc_00853966:
    local_r15 = (uint16_t)((*(uint16_t *)(v_stack_p58 + 0x42)) + 1);
    goto loc_00852DE7;
loc_00853974:
    goto loc_00852C6F;
loc_00853983:
    result = ExfReleasePushLockShared(v_stack_p58 + 72, 12 + 11, *(uint64_t *)(v_stack_p58 + 0x20), 12);
    goto loc_00852F1A;
loc_00853991:
    result = CmpUnlockHashEntry(*(uint64_t *)(v_stack_p58 + 0x20), (uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg6 + (int16_t)(v_stack_mE4) * 8 - 0x10 * 1 + 0x18) + 0x20) + 0x670) + Arg1 + Arg1 * 2 * 8)), *(uint64_t *)(v_stack_p58 + 0x20), 12);
    goto loc_00852C05;
loc_008539A6:
    if (*(uint64_t *)(v_stack_p58 + 0xC0) == 0) goto loc_0085336C;
loc_008539C0:
    if (((uint16_t)(*(uint64_t *)(v_stack_p58 + 0x20))) >= 2) goto loc_00853A38;
    *(uint64_t *)(local_r15 + (int16_t)((uint16_t)(*(uint64_t *)(v_stack_p58 + 0x20))) * 8 + 0x8) = *(uint64_t *)(*(uint64_t *)(v_stack_p58 + 0xC0) + 0x10);
loc_008539D3:
    Arg1 = (uint16_t)((*(uint64_t *)(v_stack_p58 + 0x20)) - 1);
    if (*(uint64_t *)(*(uint64_t *)(v_stack_p58 + 0xC0) + 0x18) != 0) goto loc_008539C0;
    goto loc_0085336C;
loc_008539E4:
    goto loc_0085330E;
loc_008539F3:
    v_stack_p50 = (uint32_t)((uint32_t)(0xC0000034ULL));
    goto loc_008532C6;
loc_00853A08:
    result = CmpRecordParseFailure(Arg11, (uint32_t)(0x50700ULL), (uint32_t)((uint32_t)(*(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x18))), (int16_t)((uint16_t)(*(uint64_t *)(v_stack_p58 + 0x20))));
    goto loc_0085310F;
loc_00853A2A:
    *(uint64_t *)(*(uint64_t *)(result + 0x18) + (uint32_t)(0xC0000034ULL) * 8 - 0x10) = *(uint64_t *)(*(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x18) + v_stack_p58 * 8 - 0x10);
    goto loc_0085380F;
loc_00853A38:
    *(uint64_t *)(*(uint64_t *)((uint32_t)(0xC0000034ULL) + 0x18) + (int16_t)((uint16_t)(*(uint64_t *)(v_stack_p58 + 0x20))) * 8 - 0x10) = (uint32_t)((uint32_t)(*(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x18)));
    goto loc_008539D3;
loc_00853A43:
    if (*(uint64_t *)((uint32_t)(0x50700ULL) + 0x38) == 0) goto loc_008532A1;
    result = (Arg11 == (*(uint64_t *)((uint32_t)(0x50700ULL) + 0x38))) ? 1 : 0;
    goto loc_008532AE;
loc_00853A5B:
    goto loc_008530EF;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x42` | `16` | `R` |
| `Arg2` | `+ 0x2` | `16` | `R` |
| `Arg2` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0x8 + rcx*8` | `64` | `R` |
| `Arg2` | `+ 0x8 + rdx*8` | `64` | `R` |
| `Arg2` | `+ 0x8 + rsi*8` | `64` | `R` |
| `Arg2` | `+ 0x18` | `64` | `R` |
| `Arg4` | `+ 0x2` | `16` | `W` |
| `Arg4` | `+ 0x8 + r9*8` | `64` | `W` |
| `Arg4` | `+ 0x8 + rcx*8` | `64` | `W` |
| `Arg4` | `+ 0x18` | `64` | `R` |
| `Arg5` | `+ 0x0` | `8` | `W` |
| `Arg6` | `+ 0x0` | `16` | `R` |
| `Arg6` | `+ 0x0` | `128` | `R` |
| `Arg6` | `+ 0x8` | `64` | `R` |
| `Arg11` | `+ 0xA0` | `32` | `R` |
| `Arg11` | `+ 0xA0` | `32` | `R/W` |
| `Arg11` | `+ 0xA8` | `64` | `R` |
| `Arg11` | `+ 0x1AA` | `8` | `R` |
| `Arg11` | `+ 0x1AA` | `8` | `R/W` |
| `Arg11` | `+ 0x1AC + rax*8` | `32` | `W` |
| `Arg11` | `+ 0x1B0 + rax*8` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00852BA0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
