# MiReserveUserMemory

- RVA: `0x00884498`–`0x00884E0F` (길이 `2,423` bytes)
- VA: `0x0000000140884498`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0007C868`
- 디코드: `597`개 명령, `2,423/2,423` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **44**; 고유 호출 대상: **39**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00884552` → [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) (function, `0x0035B540`)
- `0x00884610` → [MiGetProcessPartition](../../text/44/MiGetProcessPartition_function_00443B10.md) (function, `0x00443B10`)
- `0x008846B6` → [LOCK_ADDRESS_SPACE](../../text/2A/LOCK_ADDRESS_SPACE_function_002A4944.md) (function, `0x002A4944`)
- `0x00884719` → [MiSelectUserAddress](MiSelectUserAddress_function_00885C40.md) (function, `0x00885C40`)
- `0x00884745` → [MiUpdateVadStartVpn](../../text/45/MiUpdateVadStartVpn_function_00450ED4.md) (function, `0x00450ED4`)
- `0x0088476B` → [MiInsertVadCharges](MiInsertVadCharges_function_00886AA8.md) (function, `0x00886AA8`)
- `0x00884790` → [MiLockVad](../../text/29/MiLockVad_function_00295810.md) (function, `0x00295810`)
- `0x0088479F` → [MiInsertVad](../../text/26/MiInsertVad_function_00265540.md) (function, `0x00265540`)
- `0x008847B4` → [MiAdvanceVadHint](MiAdvanceVadHint_function_00886C40.md) (function, `0x00886C40`)
- `0x00884805` → [MiUnlockVad](../../text/2A/MiUnlockVad_function_002A59C8.md) (function, `0x002A59C8`)
- `0x00884811` → [UNLOCK_ADDRESS_SPACE](../../text/2A/UNLOCK_ADDRESS_SPACE_function_002A4844.md) (function, `0x002A4844`)
- `0x00884890` → [MiIsVaRangeAvailable](../97/MiIsVaRangeAvailable_function_0097FD90.md) (function, `0x0097FD90`)
- `0x008848C2` → [UNLOCK_ADDRESS_SPACE](../../text/2A/UNLOCK_ADDRESS_SPACE_function_002A4844.md) (function, `0x002A4844`)
- `0x008848CC` → [MiReleaseVadEventBlocks](../9B/MiReleaseVadEventBlocks_function_009BB0A0.md) (function, `0x009BB0A0`)
- `0x008848D6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0088491C` → [MiArbitraryCodeBlocked](../97/MiArbitraryCodeBlocked_function_0097D7CC.md) (function, `0x0097D7CC`)
- `0x00884938` → [UNLOCK_ADDRESS_SPACE](../../text/2A/UNLOCK_ADDRESS_SPACE_function_002A4844.md) (function, `0x002A4844`)
- `0x00884940` → [MiReferenceVad](../../text/29/MiReferenceVad_function_00295890.md) (function, `0x00295890`)
- `0x008849B5` → [MiSecureVad](../9F/MiSecureVad_function_009F5788.md) (function, `0x009F5788`)
- `0x008849E6` → [MiUnlockAndDereferenceVad](../../text/31/MiUnlockAndDereferenceVad_function_00316E60.md) (function, `0x00316E60`)
- `0x00884A1B` → [MiLogReserveVaFailed](../AA/MiLogReserveVaFailed_function_00AA774C.md) (function, `0x00AA774C`)
- `0x00884A31` → [MiFindPlaceholderVadToReplace](../../text/2A/MiFindPlaceholderVadToReplace_function_002A7280.md) (function, `0x002A7280`)
- `0x00884A8C` → [MiAddSecureEntry](../98/MiAddSecureEntry_function_00980250.md) (function, `0x00980250`)
- `0x00884AAC` → [MiCreatePlaceholderStorage](../8C/MiCreatePlaceholderStorage_function_008CF330.md) (function, `0x008CF330`)
- `0x00884AD1` → [MiPreparePlaceholderVadReplacement](../A7/MiPreparePlaceholderVadReplacement_function_00A7E998.md) (function, `0x00A7E998`)
- `0x00884AE2` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00884AFB` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x00884B1F` → [MiCommitVadMetadataBits](../8D/MiCommitVadMetadataBits_function_008D1A00.md) (function, `0x008D1A00`)
- `0x00884B37` → [MiDeleteVad](MiDeleteVad_function_00888C80.md) (function, `0x00888C80`)
- `0x00884B64` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00884B70` → [UNLOCK_ADDRESS_SPACE](../../text/2A/UNLOCK_ADDRESS_SPACE_function_002A4844.md) (function, `0x002A4844`)
- `0x00884B7C` → [MiSetVadDeleted](../../text/29/MiSetVadDeleted_function_00296E00.md) (function, `0x00296E00`)
- `0x00884B89` → [MiDeleteVad](MiDeleteVad_function_00888C80.md) (function, `0x00888C80`)
- `0x00884B92` → [MiDecrementVadsBeingDeleted](../../text/34/MiDecrementVadsBeingDeleted_function_00341010.md) (function, `0x00341010`)
- `0x00884BB7` → [MiCreateUserPhysicalView](../AD/MiCreateUserPhysicalView_function_00ADA4B4.md) (function, `0x00ADA4B4`)
- `0x00884BEF` → [MiCreateWriteWatchView](../98/MiCreateWriteWatchView_function_0098039C.md) (function, `0x0098039C`)
- `0x00884C1A` → [MiUnlockAndDereferenceNestedVad](../../text/4E/MiUnlockAndDereferenceNestedVad_function_004EEFCC.md) (function, `0x004EEFCC`)
- `0x00884C27` → [MiCreateRotateView](../A7/MiCreateRotateView_function_00A7F498.md) (function, `0x00A7F498`)
- `0x00884C67` → [MiCreateLargePageVad](../A9/MiCreateLargePageVad_function_00A99B50.md) (function, `0x00A99B50`)
- `0x00884C9F` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x00884D7E` → [MiStoreGraphicsProtectionInVad](../AD/MiStoreGraphicsProtectionInVad_function_00AD9E64.md) (function, `0x00AD9E64`)
- `0x00884D97` → [MiUnlockVad](../../text/2A/MiUnlockVad_function_002A59C8.md) (function, `0x002A59C8`)
- `0x00884DB9` → [MiMapUserLargePages](../../text/3D/MiMapUserLargePages_function_003D26F4.md) (function, `0x003D26F4`)
- `0x00884DFB` → [MiFinishPlaceholderVadReplacement](../A8/MiFinishPlaceholderVadReplacement_function_00A87630.md) (function, `0x00A87630`)

### Direct callers
- [MiAllocateVirtualMemory](MiAllocateVirtualMemory_function_00883B40.md) at `0x00883E74`

### Static image references
- `0x00884856` → RVA `0x00FC6A88` (`ALMOSTRO`; read)
- `0x008849D0` → RVA `0x00E2DB80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **24**
  - `0x00884552` → [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) (`PAGE` → `.text`)
  - `0x00884610` → [MiGetProcessPartition](../../text/44/MiGetProcessPartition_function_00443B10.md) (`PAGE` → `.text`)
  - `0x008846B6` → [LOCK_ADDRESS_SPACE](../../text/2A/LOCK_ADDRESS_SPACE_function_002A4944.md) (`PAGE` → `.text`)
  - `0x00884745` → [MiUpdateVadStartVpn](../../text/45/MiUpdateVadStartVpn_function_00450ED4.md) (`PAGE` → `.text`)
  - `0x00884790` → [MiLockVad](../../text/29/MiLockVad_function_00295810.md) (`PAGE` → `.text`)
  - `0x0088479F` → [MiInsertVad](../../text/26/MiInsertVad_function_00265540.md) (`PAGE` → `.text`)
  - `0x00884805` → [MiUnlockVad](../../text/2A/MiUnlockVad_function_002A59C8.md) (`PAGE` → `.text`)
  - `0x00884811` → [UNLOCK_ADDRESS_SPACE](../../text/2A/UNLOCK_ADDRESS_SPACE_function_002A4844.md) (`PAGE` → `.text`)
  - `0x008848C2` → [UNLOCK_ADDRESS_SPACE](../../text/2A/UNLOCK_ADDRESS_SPACE_function_002A4844.md) (`PAGE` → `.text`)
  - `0x008848D6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00884938` → [UNLOCK_ADDRESS_SPACE](../../text/2A/UNLOCK_ADDRESS_SPACE_function_002A4844.md) (`PAGE` → `.text`)
  - `0x00884940` → [MiReferenceVad](../../text/29/MiReferenceVad_function_00295890.md) (`PAGE` → `.text`)
  - `0x008849E6` → [MiUnlockAndDereferenceVad](../../text/31/MiUnlockAndDereferenceVad_function_00316E60.md) (`PAGE` → `.text`)
  - `0x00884A31` → [MiFindPlaceholderVadToReplace](../../text/2A/MiFindPlaceholderVadToReplace_function_002A7280.md) (`PAGE` → `.text`)
  - `0x00884AE2` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x00884AFB` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x00884B64` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00884B70` → [UNLOCK_ADDRESS_SPACE](../../text/2A/UNLOCK_ADDRESS_SPACE_function_002A4844.md) (`PAGE` → `.text`)
  - `0x00884B7C` → [MiSetVadDeleted](../../text/29/MiSetVadDeleted_function_00296E00.md) (`PAGE` → `.text`)
  - `0x00884B92` → [MiDecrementVadsBeingDeleted](../../text/34/MiDecrementVadsBeingDeleted_function_00341010.md) (`PAGE` → `.text`)
  - `0x00884C1A` → [MiUnlockAndDereferenceNestedVad](../../text/4E/MiUnlockAndDereferenceNestedVad_function_004EEFCC.md) (`PAGE` → `.text`)
  - `0x00884C9F` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x00884D97` → [MiUnlockVad](../../text/2A/MiUnlockVad_function_002A59C8.md) (`PAGE` → `.text`)
  - `0x00884DB9` → [MiMapUserLargePages](../../text/3D/MiMapUserLargePages_function_003D26F4.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **5**
  - `0x00884D18` → [sub_00B18F20 + 0x2D](../B1/Unknown_function_00B18F20.md) (`tail-transfer`)
  - `0x00884D25` → [sub_00B18F20](../B1/Unknown_function_00B18F20.md) (`tail-transfer`)
  - `0x00884D2E` → [sub_00B18F20 + 0x9](../B1/Unknown_function_00B18F20.md) (`tail-transfer`)
  - `0x00884D52` → [sub_00B18F20 + 0x42](../B1/Unknown_function_00B18F20.md) (`tail-transfer`)
  - `0x00884D61` → [sub_00B18F20 + 0x42](../B1/Unknown_function_00B18F20.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00884498  48 8B C4                        mov rax, rsp
0088449B  48 89 58 08                     mov qword ptr [rax + 8], rbx
0088449F  4C 89 48 20                     mov qword ptr [rax + 0x20], r9
008844A3  44 89 40 18                     mov dword ptr [rax + 0x18], r8d
008844A7  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
008844AB  55                              push rbp
008844AC  56                              push rsi
008844AD  57                              push rdi
008844AE  41 54                           push r12
008844B0  41 55                           push r13
008844B2  41 56                           push r14
008844B4  41 57                           push r15
008844B6  48 8B EC                        mov rbp, rsp
008844B9  48 81 EC 80 00 00 00            sub rsp, 0x80
008844C0  45 33 E4                        xor r12d, r12d
008844C3  41 8B D8                        mov ebx, r8d
008844C6  44 89 65 D0                     mov dword ptr [rbp - 0x30], r12d
008844CA  48 8B F1                        mov rsi, rcx
008844CD  45 8B EC                        mov r13d, r12d
008844D0  48 83 FA 01                     cmp rdx, 1
008844D4  0F 84 CF 07 00 00               je 0x140884ca9
008844DA  48 8B 41 58                     mov rax, qword ptr [rcx + 0x58]
008844DE  45 8D 7C 24 08                  lea r15d, [r12 + 8]
008844E3  48 8B 49 08                     mov rcx, qword ptr [rcx + 8]
008844E7  48 2B 0E                        sub rcx, qword ptr [rsi]
008844EA  48 FF C1                        inc rcx
008844ED  48 8B 80 10 04 00 00            mov rax, qword ptr [rax + 0x410]
008844F4  48 05 00 03 00 00               add rax, 0x300
008844FA  48 3B 4E 18                     cmp rcx, qword ptr [rsi + 0x18]
008844FE  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
00884502  8B 46 2C                        mov eax, dword ptr [rsi + 0x2c]
00884505  45 0F 45 FC                     cmovne r15d, r12d
00884509  A8 88                           test al, 0x88
0088450B  0F 85 F4 08 00 00               jne 0x140884e05
00884511  F7 46 40 00 00 00 20            test dword ptr [rsi + 0x40], 0x20000000
00884518  0F 85 38 03 00 00               jne 0x140884856
0088451E  F6 C3 02                        test bl, 2
00884521  0F 85 F1 03 00 00               jne 0x140884918
00884527  48 8B 46 18                     mov rax, qword ptr [rsi + 0x18]
0088452B  49 8B FC                        mov rdi, r12
0088452E  48 A9 FF 0F 00 00               test rax, 0xfff
00884534  41 B8 56 61 64 53               mov r8d, 0x53646156
0088453A  40 0F 95 C7                     setne dil
0088453E  48 C1 E8 0C                     shr rax, 0xc
00884542  48 03 F8                        add rdi, rax
00884545  B8 40 00 00 00                  mov eax, 0x40
0088454A  8B D0                           mov edx, eax
0088454C  48 89 7D E0                     mov qword ptr [rbp - 0x20], rdi
00884550  8B C8                           mov ecx, eax
00884552  E8 E9 6F AD FF                  call 0x14035b540
00884557  4C 8B F0                        mov r14, rax
0088455A  48 85 C0                        test rax, rax
0088455D  0F 84 AB 03 00 00               je 0x14088490e
00884563  8B 4E 34                        mov ecx, dword ptr [rsi + 0x34]
00884566  48 C7 C0 FE FF FF FF            mov rax, 0xfffffffffffffffe
0088456D  8B D1                           mov edx, ecx
0088456F  49 89 46 10                     mov qword ptr [r14 + 0x10], rax
00884573  C1 E2 0C                        shl edx, 0xc
00884576  49 89 06                        mov qword ptr [r14], rax
00884579  49 89 46 08                     mov qword ptr [r14 + 8], rax
0088457D  41 8B 46 30                     mov eax, dword ptr [r14 + 0x30]
00884581  33 D0                           xor edx, eax
00884583  81 E2 00 F0 07 00               and edx, 0x7f000
00884589  4D 89 66 28                     mov qword ptr [r14 + 0x28], r12
0088458D  33 D0                           xor edx, eax
0088458F  41 89 56 30                     mov dword ptr [r14 + 0x30], edx
00884593  85 C9                           test ecx, ecx
00884595  0F 85 A0 02 00 00               jne 0x14088483b
0088459B  44 8B 46 28                     mov r8d, dword ptr [rsi + 0x28]
0088459F  41 0F BA E0 0C                  bt r8d, 0xc
008845A4  0F 83 C2 02 00 00               jae 0x14088486c
008845AA  48 8B CF                        mov rcx, rdi
008845AD  0F BA EA 19                     bts edx, 0x19
008845B1  8B C3                           mov eax, ebx
008845B3  C1 E0 07                        shl eax, 7
008845B6  33 C2                           xor eax, edx
008845B8  25 80 0F 00 00                  and eax, 0xf80
008845BD  33 C2                           xor eax, edx
008845BF  8B 56 40                        mov edx, dword ptr [rsi + 0x40]
008845C2  0F BA E8 15                     bts eax, 0x15
008845C6  41 89 46 30                     mov dword ptr [r14 + 0x30], eax
008845CA  0F BA E2 1E                     bt edx, 0x1e
008845CE  73 08                           jae 0x1408845d8
008845D0  0F BA E8 1C                     bts eax, 0x1c
008845D4  41 89 46 30                     mov dword ptr [r14 + 0x30], eax
008845D8  F6 C2 01                        test dl, 1
008845DB  0F 85 01 03 00 00               jne 0x1408848e2
008845E1  0F BA E2 1B                     bt edx, 0x1b
008845E5  48 B8 FD FF FF FF 07 00 00 00   movabs rax, 0x7fffffffd
008845EF  48 0F 42 C8                     cmovb rcx, rax
008845F3  41 89 4E 34                     mov dword ptr [r14 + 0x34], ecx
008845F7  48 C1 E9 20                     shr rcx, 0x20
008845FB  41 88 4E 22                     mov byte ptr [r14 + 0x22], cl
008845FF  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00884608  48 8B 4E 58                     mov rcx, qword ptr [rsi + 0x58]
0088460C  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
00884610  E8 FB F4 BB FF                  call 0x140443b10
00884615  4C 8B 4D 60                     mov r9, qword ptr [rbp + 0x60]
00884619  0F B7 08                        movzx ecx, word ptr [rax]
0088461C  41 8B C0                        mov eax, r8d
0088461F  66 41 89 09                     mov word ptr [r9], cx
00884623  B9 00 00 40 20                  mov ecx, 0x20400000
00884628  23 C1                           and eax, ecx
0088462A  3D 00 00 00 20                  cmp eax, 0x20000000
0088462F  0F 84 BB 03 00 00               je 0x1408849f0
00884635  3B C1                           cmp eax, ecx
00884637  0F 84 76 06 00 00               je 0x140884cb3
0088463D  3D 00 00 40 00                  cmp eax, 0x400000
00884642  0F 84 A9 02 00 00               je 0x1408848f1
00884648  41 8B DF                        mov ebx, r15d
0088464B  41 0F BA E0 17                  bt r8d, 0x17
00884650  0F 82 CE 05 00 00               jb 0x140884c24
00884656  83 FB 10                        cmp ebx, 0x10
00884659  0F 83 EB 05 00 00               jae 0x140884c4a
0088465F  41 8B 4E 30                     mov ecx, dword ptr [r14 + 0x30]
00884663  81 E1 FF FF E7 FF               and ecx, 0xffe7ffff
00884669  41 C1 E4 13                     shl r12d, 0x13
0088466D  41 0B CC                        or ecx, r12d
00884670  F7 46 28 00 00 20 00            test dword ptr [rsi + 0x28], 0x200000
00884677  41 89 4E 30                     mov dword ptr [r14 + 0x30], ecx
0088467B  0F 85 64 05 00 00               jne 0x140884be5
00884681  F6 46 70 01                     test byte ptr [rsi + 0x70], 1
00884685  0F 85 BA 06 00 00               jne 0x140884d45
0088468B  44 39 6E 30                     cmp dword ptr [rsi + 0x30], r13d
0088468F  0F 85 DC 06 00 00               jne 0x140884d71
00884695  45 33 FF                        xor r15d, r15d
00884698  0F BA 66 40 1A                  bt dword ptr [rsi + 0x40], 0x1a
0088469D  4C 89 7D E0                     mov qword ptr [rbp - 0x20], r15
008846A1  0F 82 02 04 00 00               jb 0x140884aa9
008846A7  48 8B 56 58                     mov rdx, qword ptr [rsi + 0x58]
008846AB  83 CB 02                        or ebx, 2
008846AE  48 8B 4D D8                     mov rcx, qword ptr [rbp - 0x28]
008846B2  4C 21 6D F0                     and qword ptr [rbp - 0x10], r13
008846B6  E8 89 02 A2 FF                  call 0x1402a4944
008846BB  4C 8B 56 58                     mov r10, qword ptr [rsi + 0x58]
008846BF  41 8B 82 F4 01 00 00            mov eax, dword ptr [r10 + 0x1f4]
008846C6  A8 20                           test al, 0x20
008846C8  0F 85 72 05 00 00               jne 0x140884c40
008846CE  8B 46 40                        mov eax, dword ptr [rsi + 0x40]
008846D1  48 8B 0E                        mov rcx, qword ptr [rsi]
008846D4  48 8B 56 08                     mov rdx, qword ptr [rsi + 8]
008846D8  F6 C3 08                        test bl, 8
008846DB  0F 85 93 01 00 00               jne 0x140884874
008846E1  4C 8B 4E 18                     mov r9, qword ptr [rsi + 0x18]
008846E5  4C 8D 45 E0                     lea r8, [rbp - 0x20]
008846E9  4C 89 44 24 48                  mov qword ptr [rsp + 0x48], r8
008846EE  4C 8D 45 F0                     lea r8, [rbp - 0x10]
008846F2  4C 89 44 24 40                  mov qword ptr [rsp + 0x40], r8
008846F7  4C 8B C2                        mov r8, rdx
008846FA  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
008846FE  48 8B D1                        mov rdx, rcx
00884701  8B 45 50                        mov eax, dword ptr [rbp + 0x50]
00884704  8B 4E 28                        mov ecx, dword ptr [rsi + 0x28]
00884707  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
0088470B  48 8B 46 10                     mov rax, qword ptr [rsi + 0x10]
0088470F  4C 21 6C 24 28                  and qword ptr [rsp + 0x28], r13
00884714  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00884719  E8 22 15 00 00                  call 0x140885c40
0088471E  8B F8                           mov edi, eax
00884720  85 C0                           test eax, eax
00884722  0F 88 E4 02 00 00               js 0x140884a0c
00884728  4C 8B 7D E0                     mov r15, qword ptr [rbp - 0x20]
0088472C  4D 8D 67 FF                     lea r12, [r15 - 1]
00884730  4C 03 66 18                     add r12, qword ptr [rsi + 0x18]
00884734  49 8B C7                        mov rax, r15
00884737  49 8B CE                        mov rcx, r14
0088473A  48 C1 E8 0C                     shr rax, 0xc
0088473E  48 8B D0                        mov rdx, rax
00884741  48 89 45 F8                     mov qword ptr [rbp - 8], rax
00884745  E8 8A C7 BC FF                  call 0x140450ed4
0088474A  49 C1 EC 0C                     shr r12, 0xc
0088474E  49 8B C4                        mov rax, r12
00884751  45 89 66 1C                     mov dword ptr [r14 + 0x1c], r12d
00884755  48 C1 E8 20                     shr rax, 0x20
00884759  F6 46 70 01                     test byte ptr [rsi + 0x70], 1
0088475D  41 88 46 21                     mov byte ptr [r14 + 0x21], al
00884761  0F 85 14 06 00 00               jne 0x140884d7b
00884767  48 8B 56 58                     mov rdx, qword ptr [rsi + 0x58]
0088476B  E8 38 23 00 00                  call 0x140886aa8
00884770  89 45 D0                        mov dword ptr [rbp - 0x30], eax
00884773  8B F8                           mov edi, eax
00884775  85 C0                           test eax, eax
00884777  0F 88 25 01 00 00               js 0x1408848a2
0088477D  4D 85 ED                        test r13, r13
00884780  0F 85 40 03 00 00               jne 0x140884ac6
00884786  48 8B 5D D8                     mov rbx, qword ptr [rbp - 0x28]
0088478A  49 8B D6                        mov rdx, r14
0088478D  48 8B CB                        mov rcx, rbx
00884790  E8 7B 10 A1 FF                  call 0x140295810
00884795  48 8B 56 58                     mov rdx, qword ptr [rsi + 0x58]
00884799  45 33 C0                        xor r8d, r8d
0088479C  49 8B CE                        mov rcx, r14
0088479F  E8 9C 0D 9E FF                  call 0x140265540
008847A4  4C 8B 45 F0                     mov r8, qword ptr [rbp - 0x10]
008847A8  4D 85 C0                        test r8, r8
008847AB  74 0C                           je 0x1408847b9
008847AD  48 8B 4D F8                     mov rcx, qword ptr [rbp - 8]
008847B1  49 8B D4                        mov rdx, r12
008847B4  E8 87 24 00 00                  call 0x140886c40
008847B9  45 33 E4                        xor r12d, r12d
008847BC  BF 00 00 18 00                  mov edi, 0x180000
008847C1  44 39 66 78                     cmp dword ptr [rsi + 0x78], r12d
008847C5  0F 85 66 01 00 00               jne 0x140884931
008847CB  41 8B 46 30                     mov eax, dword ptr [r14 + 0x30]
008847CF  0F BA E0 15                     bt eax, 0x15
008847D3  73 17                           jae 0x1408847ec
008847D5  0F BA E0 17                     bt eax, 0x17
008847D9  0F 82 52 01 00 00               jb 0x140884931
008847DF  23 C7                           and eax, edi
008847E1  3D 00 00 10 00                  cmp eax, 0x100000
008847E6  0F 83 45 01 00 00               jae 0x140884931
008847EC  4C 39 66 48                     cmp qword ptr [rsi + 0x48], r12
008847F0  0F 85 3B 01 00 00               jne 0x140884931
008847F6  4D 85 ED                        test r13, r13
008847F9  0F 85 4D 03 00 00               jne 0x140884b4c
008847FF  49 8B D6                        mov rdx, r14
00884802  48 8B CB                        mov rcx, rbx
00884805  E8 BE 11 A2 FF                  call 0x1402a59c8
0088480A  48 8B 56 58                     mov rdx, qword ptr [rsi + 0x58]
0088480E  48 8B CB                        mov rcx, rbx
00884811  E8 2E 00 A2 FF                  call 0x1402a4844
00884816  48 8B 45 58                     mov rax, qword ptr [rbp + 0x58]
0088481A  4C 89 38                        mov qword ptr [rax], r15
0088481D  33 C0                           xor eax, eax
0088481F  48 8B 9C 24 C0 00 00 00         mov rbx, qword ptr [rsp + 0xc0]
00884827  48 81 C4 80 00 00 00            add rsp, 0x80
0088482E  41 5F                           pop r15
00884830  41 5E                           pop r14
00884832  41 5D                           pop r13
00884834  41 5C                           pop r12
00884836  5F                              pop rdi
00884837  5E                              pop rsi
00884838  5D                              pop rbp
00884839  C3                              ret
0088483A  CC                              int3
0088483B  48 8B 46 58                     mov rax, qword ptr [rsi + 0x58]
0088483F  48 8B 88 10 04 00 00            mov rcx, qword ptr [rax + 0x410]
00884846  C6 81 24 04 00 00 01            mov byte ptr [rcx + 0x424], 1
0088484D  41 8B 56 30                     mov edx, dword ptr [r14 + 0x30]
00884851  E9 45 FD FF FF                  jmp 0x14088459b
00884856  48 F7 05 27 22 74 00 00 00 08 00  test qword ptr [rip + 0x742227], 0x80000
00884861  0F 84 C0 FC FF FF               je 0x140884527
00884867  E9 B2 FC FF FF                  jmp 0x14088451e
0088486C  49 8B CC                        mov rcx, r12
0088486F  E9 3D FD FF FF                  jmp 0x1408845b1
00884874  0F BA E0 1A                     bt eax, 0x1a
00884878  0F 82 AB 01 00 00               jb 0x140884a29
0088487E  4C 8B 46 18                     mov r8, qword ptr [rsi + 0x18]
00884882  4C 8B C9                        mov r9, rcx
00884885  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
0088488A  48 8B D1                        mov rdx, rcx
0088488D  49 8B CA                        mov rcx, r10
00884890  E8 FB B4 0F 00                  call 0x14097fd90
00884895  85 C0                           test eax, eax
00884897  0F 85 A5 01 00 00               jne 0x140884a42
0088489D  BF 18 00 00 C0                  mov edi, 0xc0000018
008848A2  48 8B 45 58                     mov rax, qword ptr [rbp + 0x58]
008848A6  4C 89 38                        mov qword ptr [rax], r15
008848A9  4D 85 ED                        test r13, r13
008848AC  0F 85 DB 04 00 00               jne 0x140884d8d
008848B2  4C 8B 7D D8                     mov r15, qword ptr [rbp - 0x28]
008848B6  F6 C3 02                        test bl, 2
008848B9  74 0C                           je 0x1408848c7
008848BB  48 8B 56 58                     mov rdx, qword ptr [rsi + 0x58]
008848BF  49 8B CF                        mov rcx, r15
008848C2  E8 7D FF A1 FF                  call 0x1402a4844
008848C7  33 D2                           xor edx, edx
008848C9  49 8B CE                        mov rcx, r14
008848CC  E8 CF 67 13 00                  call 0x1409bb0a0
008848D1  33 D2                           xor edx, edx
008848D3  49 8B CE                        mov rcx, r14
008848D6  E8 95 DF 2F 00                  call 0x140b82870
008848DB  8B C7                           mov eax, edi
008848DD  E9 3D FF FF FF                  jmp 0x14088481f
008848E2  48 B9 FE FF FF FF 07 00 00 00   movabs rcx, 0x7fffffffe
008848EC  E9 02 FD FF FF                  jmp 0x1408845f3
008848F1  8B CB                           mov ecx, ebx
008848F3  8B C3                           mov eax, ebx
008848F5  83 E1 07                        and ecx, 7
008848F8  83 E0 F8                        and eax, 0xfffffff8
008848FB  83 F8 10                        cmp eax, 0x10
008848FE  0F 85 98 02 00 00               jne 0x140884b9c
00884904  BF 45 00 00 C0                  mov edi, 0xc0000045
00884909  41 8B DF                        mov ebx, r15d
0088490C  EB A4                           jmp 0x1408848b2
0088490E  B8 9A 00 00 C0                  mov eax, 0xc000009a
00884913  E9 07 FF FF FF                  jmp 0x14088481f
00884918  48 8B 4E 60                     mov rcx, qword ptr [rsi + 0x60]
0088491C  E8 AB 8E 0F 00                  call 0x14097d7cc
00884921  89 45 D0                        mov dword ptr [rbp - 0x30], eax
00884924  85 C0                           test eax, eax
00884926  0F 89 FB FB FF FF               jns 0x140884527
0088492C  E9 EE FE FF FF                  jmp 0x14088481f
00884931  48 8B 56 58                     mov rdx, qword ptr [rsi + 0x58]
00884935  48 8B CB                        mov rcx, rbx
00884938  E8 07 FF A1 FF                  call 0x1402a4844
0088493D  49 8B CE                        mov rcx, r14
00884940  E8 4B 0F A1 FF                  call 0x140295890
00884945  41 8B 56 30                     mov edx, dword ptr [r14 + 0x30]
00884949  0F BA E2 15                     bt edx, 0x15
0088494D  73 19                           jae 0x140884968
0088494F  0F BA E2 17                     bt edx, 0x17
00884953  0F 82 48 04 00 00               jb 0x140884da1
00884959  8B C2                           mov eax, edx
0088495B  23 C7                           and eax, edi
0088495D  3D 00 00 10 00                  cmp eax, 0x100000
00884962  0F 83 39 04 00 00               jae 0x140884da1
00884968  44 8B 46 78                     mov r8d, dword ptr [rsi + 0x78]
0088496C  45 85 C0                        test r8d, r8d
0088496F  0F 85 A5 01 00 00               jne 0x140884b1a
00884975  4C 39 66 48                     cmp qword ptr [rsi + 0x48], r12
00884979  74 5F                           je 0x1408849da
0088497B  F7 46 40 00 00 00 40            test dword ptr [rsi + 0x40], 0x40000000
00884982  44 8B 4E 44                     mov r9d, dword ptr [rsi + 0x44]
00884986  4C 89 65 48                     mov qword ptr [rbp + 0x48], r12
0088498A  0F 85 C2 00 00 00               jne 0x140884a52
00884990  41 8D 41 FF                     lea eax, [r9 - 1]
00884994  83 F8 01                        cmp eax, 1
00884997  0F 87 30 04 00 00               ja 0x140884dcd
0088499D  4C 8B 46 18                     mov r8, qword ptr [rsi + 0x18]
008849A1  48 8D 45 48                     lea rax, [rbp + 0x48]
008849A5  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008849AA  49 8B D7                        mov rdx, r15
008849AD  49 8B CE                        mov rcx, r14
008849B0  44 89 64 24 20                  mov dword ptr [rsp + 0x20], r12d
008849B5  E8 CE 0D 17 00                  call 0x1409f5788
008849BA  48 8B 55 48                     mov rdx, qword ptr [rbp + 0x48]
008849BE  8B D8                           mov ebx, eax
008849C0  85 DB                           test ebx, ebx
008849C2  0F 88 66 01 00 00               js 0x140884b2e
008849C8  48 8B 46 48                     mov rax, qword ptr [rsi + 0x48]
008849CC  48 33 56 58                     xor rdx, qword ptr [rsi + 0x58]
008849D0  48 33 15 A9 91 5A 00            xor rdx, qword ptr [rip + 0x5a91a9]
008849D7  48 89 10                        mov qword ptr [rax], rdx
008849DA  49 8B CE                        mov rcx, r14
008849DD  4D 85 ED                        test r13, r13
008849E0  0F 85 34 02 00 00               jne 0x140884c1a
008849E6  E8 75 24 A9 FF                  call 0x140316e60
008849EB  E9 26 FE FF FF                  jmp 0x140884816
008849F0  44 8B 66 70                     mov r12d, dword ptr [rsi + 0x70]
008849F4  41 83 CF 10                     or r15d, 0x10
008849F8  49 C1 EC 04                     shr r12, 4
008849FC  41 8B DF                        mov ebx, r15d
008849FF  41 83 E4 01                     and r12d, 1
00884A03  41 83 CC 02                     or r12d, 2
00884A07  E9 4A FC FF FF                  jmp 0x140884656
00884A0C  4C 8B 4E 08                     mov r9, qword ptr [rsi + 8]
00884A10  4C 8B 06                        mov r8, qword ptr [rsi]
00884A13  48 8B 56 10                     mov rdx, qword ptr [rsi + 0x10]
00884A17  48 8B 4E 18                     mov rcx, qword ptr [rsi + 0x18]
00884A1B  E8 2C 2D 22 00                  call 0x140aa774c
00884A20  4C 8B 7D E0                     mov r15, qword ptr [rbp - 0x20]
00884A24  E9 79 FE FF FF                  jmp 0x1408848a2
00884A29  44 8A 46 39                     mov r8b, byte ptr [rsi + 0x39]
00884A2D  4C 8D 4D D0                     lea r9, [rbp - 0x30]
00884A31  E8 4A 28 A2 FF                  call 0x1402a7280
00884A36  4C 8B E8                        mov r13, rax
00884A39  48 85 C0                        test rax, rax
00884A3C  0F 84 D0 01 00 00               je 0x140884c12
00884A42  4C 8B 3E                        mov r15, qword ptr [rsi]
00884A45  4C 8B 66 08                     mov r12, qword ptr [rsi + 8]
00884A49  4C 89 7D E0                     mov qword ptr [rbp - 0x20], r15
00884A4D  E9 E2 FC FF FF                  jmp 0x140884734
00884A52  41 8B 46 1C                     mov eax, dword ptr [r14 + 0x1c]
00884A56  49 8B CE                        mov rcx, r14
00884A59  45 0F B6 46 21                  movzx r8d, byte ptr [r14 + 0x21]
00884A5E  41 0F B6 56 20                  movzx edx, byte ptr [r14 + 0x20]
00884A63  49 C1 E0 20                     shl r8, 0x20
00884A67  4C 0B C0                        or r8, rax
00884A6A  48 C1 E2 20                     shl rdx, 0x20
00884A6E  41 8B 46 18                     mov eax, dword ptr [r14 + 0x18]
00884A72  48 0B D0                        or rdx, rax
00884A75  49 C1 E0 0C                     shl r8, 0xc
00884A79  48 C1 E2 0C                     shl rdx, 0xc
00884A7D  49 81 C8 FF 0F 00 00            or r8, 0xfff
00884A84  C7 44 24 20 01 00 00 00         mov dword ptr [rsp + 0x20], 1
00884A8C  E8 BF B7 0F 00                  call 0x140980250
00884A91  48 8B C8                        mov rcx, rax
00884A94  48 8B D0                        mov rdx, rax
00884A97  48 F7 D9                        neg rcx
00884A9A  1B DB                           sbb ebx, ebx
00884A9C  F7 D3                           not ebx
00884A9E  81 E3 9A 00 00 C0               and ebx, 0xc000009a
00884AA4  E9 17 FF FF FF                  jmp 0x1408849c0
00884AA9  49 8B CE                        mov rcx, r14
00884AAC  E8 7F A8 04 00                  call 0x1408cf330
00884AB1  89 45 D0                        mov dword ptr [rbp - 0x30], eax
00884AB4  8B F8                           mov edi, eax
00884AB6  85 C0                           test eax, eax
00884AB8  0F 88 E4 FD FF FF               js 0x1408848a2
00884ABE  83 CB 04                        or ebx, 4
00884AC1  E9 E1 FB FF FF                  jmp 0x1408846a7
00884AC6  4C 8B 45 E8                     mov r8, qword ptr [rbp - 0x18]
00884ACA  49 8B CD                        mov rcx, r13
00884ACD  48 8B 56 58                     mov rdx, qword ptr [rsi + 0x58]
00884AD1  E8 C2 9E 1F 00                  call 0x140a7e998
00884AD6  49 8D 5E 28                     lea rbx, [r14 + 0x28]
00884ADA  45 33 C0                        xor r8d, r8d
00884ADD  48 8B CB                        mov rcx, rbx
00884AE0  33 D2                           xor edx, edx
00884AE2  E8 49 B7 98 FF                  call 0x140210230
00884AE7  F0 48 0F BA 2B 00               lock bts qword ptr [rbx], 0
00884AED  48 8B F8                        mov rdi, rax
00884AF0  73 0E                           jae 0x140884b00
00884AF2  4C 8B C3                        mov r8, rbx
00884AF5  48 8B D0                        mov rdx, rax
00884AF8  48 8B CB                        mov rcx, rbx
00884AFB  E8 90 B1 98 FF                  call 0x14020fc90
00884B00  4C 8B 7D E0                     mov r15, qword ptr [rbp - 0x20]
00884B04  48 8B 5D D8                     mov rbx, qword ptr [rbp - 0x28]
00884B08  48 85 FF                        test rdi, rdi
00884B0B  0F 84 84 FC FF FF               je 0x140884795
00884B11  C6 47 0A 01                     mov byte ptr [rdi + 0xa], 1
00884B15  E9 7B FC FF FF                  jmp 0x140884795
00884B1A  33 D2                           xor edx, edx
00884B1C  49 8B CE                        mov rcx, r14
00884B1F  E8 DC CE 04 00                  call 0x1408d1a00
00884B24  8B D8                           mov ebx, eax
00884B26  85 C0                           test eax, eax
00884B28  0F 89 47 FE FF FF               jns 0x140884975
00884B2E  45 33 C0                        xor r8d, r8d
00884B31  49 8B D5                        mov rdx, r13
00884B34  49 8B CE                        mov rcx, r14
00884B37  E8 44 41 00 00                  call 0x140888c80
00884B3C  4D 85 ED                        test r13, r13
00884B3F  0F 85 A9 02 00 00               jne 0x140884dee
00884B45  8B C3                           mov eax, ebx
00884B47  E9 D3 FC FF FF                  jmp 0x14088481f
00884B4C  48 83 C8 FF                     or rax, 0xffffffffffffffff
00884B50  F0 49 0F C1 46 28               lock xadd qword ptr [r14 + 0x28], rax
00884B56  24 06                           and al, 6
00884B58  3C 02                           cmp al, 2
00884B5A  0F 84 3B 01 00 00               je 0x140884c9b
00884B60  49 8D 4E 28                     lea rcx, [r14 + 0x28]
00884B64  E8 97 CA A5 FF                  call 0x1402e1600
00884B69  48 8B 56 58                     mov rdx, qword ptr [rsi + 0x58]
00884B6D  48 8B CB                        mov rcx, rbx
00884B70  E8 CF FC A1 FF                  call 0x1402a4844
00884B75  4C 8B 7D E0                     mov r15, qword ptr [rbp - 0x20]
00884B79  49 8B CD                        mov rcx, r13
00884B7C  E8 7F 22 A1 FF                  call 0x140296e00
00884B81  45 33 C0                        xor r8d, r8d
00884B84  33 D2                           xor edx, edx
00884B86  49 8B CD                        mov rcx, r13
00884B89  E8 F2 40 00 00                  call 0x140888c80
00884B8E  48 8B 4D E8                     mov rcx, qword ptr [rbp - 0x18]
00884B92  E8 79 C4 AB FF                  call 0x140341010
00884B97  E9 7A FC FF FF                  jmp 0x140884816
00884B9C  83 F9 04                        cmp ecx, 4
00884B9F  0F 85 29 01 00 00               jne 0x140884cce
00884BA5  F6 46 70 01                     test byte ptr [rsi + 0x70], 1
00884BA9  8B D3                           mov edx, ebx
00884BAB  0F 85 2B 01 00 00               jne 0x140884cdc
00884BB1  4C 8B C6                        mov r8, rsi
00884BB4  49 8B CE                        mov rcx, r14
00884BB7  E8 F8 58 25 00                  call 0x140ada4b4
00884BBC  89 45 D0                        mov dword ptr [rbp - 0x30], eax
00884BBF  41 8B DF                        mov ebx, r15d
00884BC2  85 C0                           test eax, eax
00884BC4  0F 88 42 01 00 00               js 0x140884d0c
00884BCA  41 8B 46 30                     mov eax, dword ptr [r14 + 0x30]
00884BCE  83 E0 BF                        and eax, 0xffffffbf
00884BD1  83 C8 30                        or eax, 0x30
00884BD4  0F BA F0 1B                     btr eax, 0x1b
00884BD8  83 4E 40 04                     or dword ptr [rsi + 0x40], 4
00884BDC  41 89 46 30                     mov dword ptr [r14 + 0x30], eax
00884BE0  E9 71 FA FF FF                  jmp 0x140884656
00884BE5  48 8B 4E 58                     mov rcx, qword ptr [rsi + 0x58]
00884BE9  4C 8B C7                        mov r8, rdi
00884BEC  49 8B D6                        mov rdx, r14
00884BEF  E8 A8 B7 0F 00                  call 0x14098039c
00884BF4  89 45 D0                        mov dword ptr [rbp - 0x30], eax
00884BF7  8B F8                           mov edi, eax
00884BF9  85 C0                           test eax, eax
00884BFB  0F 88 B1 FC FF FF               js 0x1408848b2
00884C01  41 8B 4E 30                     mov ecx, dword ptr [r14 + 0x30]
00884C05  0F BA E9 16                     bts ecx, 0x16
00884C09  41 89 4E 30                     mov dword ptr [r14 + 0x30], ecx
00884C0D  E9 6F FA FF FF                  jmp 0x140884681
00884C12  8B 7D D0                        mov edi, dword ptr [rbp - 0x30]
00884C15  E9 88 FC FF FF                  jmp 0x1408848a2
00884C1A  E8 AD A3 C6 FF                  call 0x1404eefcc
00884C1F  E9 55 FF FF FF                  jmp 0x140884b79
00884C24  49 8B CE                        mov rcx, r14
00884C27  E8 6C A8 1F 00                  call 0x140a7f498
00884C2C  85 C0                           test eax, eax
00884C2E  0F 84 D8 00 00 00               je 0x140884d0c
00884C34  41 8B 46 30                     mov eax, dword ptr [r14 + 0x30]
00884C38  83 E0 CF                        and eax, 0xffffffcf
00884C3B  83 C8 40                        or eax, 0x40
00884C3E  EB 9C                           jmp 0x140884bdc
00884C40  BF 0A 01 00 C0                  mov edi, 0xc000010a
00884C45  E9 58 FC FF FF                  jmp 0x1408848a2
00884C4A  48 8B 46 70                     mov rax, qword ptr [rsi + 0x70]
00884C4E  A8 04                           test al, 4
00884C50  0F 85 C0 00 00 00               jne 0x140884d16
00884C56  4C 8B 7D 48                     mov r15, qword ptr [rbp + 0x48]
00884C5A  48 8B 4E 58                     mov rcx, qword ptr [rsi + 0x58]
00884C5E  45 33 C9                        xor r9d, r9d
00884C61  4D 8B C7                        mov r8, r15
00884C64  49 8B D6                        mov rdx, r14
00884C67  E8 E4 4E 21 00                  call 0x140a99b50
00884C6C  89 45 D0                        mov dword ptr [rbp - 0x30], eax
00884C6F  8B F8                           mov edi, eax
00884C71  85 C0                           test eax, eax
00884C73  0F 88 39 FC FF FF               js 0x1408848b2
00884C79  4D 85 FF                        test r15, r15
00884C7C  0F 85 B1 00 00 00               jne 0x140884d33
00884C82  F6 46 70 1A                     test byte ptr [rsi + 0x70], 0x1a
00884C86  48 8B 7D E0                     mov rdi, qword ptr [rbp - 0x20]
00884C8A  0F 84 CF F9 FF FF               je 0x14088465f
00884C90  41 0F BA 6E 30 17               bts dword ptr [r14 + 0x30], 0x17
00884C96  E9 C4 F9 FF FF                  jmp 0x14088465f
00884C9B  49 8D 4E 28                     lea rcx, [r14 + 0x28]
00884C9F  E8 2C 11 9E FF                  call 0x140265dd0
00884CA4  E9 B7 FE FF FF                  jmp 0x140884b60
00884CA9  B8 0D 00 00 C0                  mov eax, 0xc000000d
00884CAE  E9 6C FB FF FF                  jmp 0x14088481f
00884CB3  F6 46 70 02                     test byte ptr [rsi + 0x70], 2
00884CB7  41 BC 01 00 00 00               mov r12d, 1
00884CBD  41 8B DF                        mov ebx, r15d
00884CC0  0F 84 90 F9 FF FF               je 0x140884656
00884CC6  83 CB 10                        or ebx, 0x10
00884CC9  E9 88 F9 FF FF                  jmp 0x140884656
00884CCE  83 F9 01                        cmp ecx, 1
00884CD1  0F 85 2D FC FF FF               jne 0x140884904
00884CD7  E9 C9 FE FF FF                  jmp 0x140884ba5
00884CDC  4C 39 66 68                     cmp qword ptr [rsi + 0x68], r12
00884CE0  0F 84 1E FC FF FF               je 0x140884904
00884CE6  8B 4E 30                        mov ecx, dword ptr [rsi + 0x30]
00884CE9  83 CA 02                        or edx, 2
00884CEC  F7 C1 00 C0 01 00               test ecx, 0x1c000
00884CF2  0F 44 D3                        cmove edx, ebx
00884CF5  F7 C1 00 20 01 00               test ecx, 0x12000
00884CFB  0F 84 B0 FE FF FF               je 0x140884bb1
00884D01  83 E2 FE                        and edx, 0xfffffffe
00884D04  83 CA 04                        or edx, 4
00884D07  E9 A5 FE FF FF                  jmp 0x140884bb1
00884D0C  BF 9A 00 00 C0                  mov edi, 0xc000009a
00884D11  E9 9C FB FF FF                  jmp 0x1408848b2
00884D16  A8 1A                           test al, 0x1a
00884D18  0F 84 2F 42 29 00               je 0x140b18f4d
00884D1E  4C 8B 7D 48                     mov r15, qword ptr [rbp + 0x48]
00884D22  4D 85 FF                        test r15, r15
00884D25  0F 84 F5 41 29 00               je 0x140b18f20
00884D2B  49 8B 07                        mov rax, qword ptr [r15]
00884D2E  E9 F6 41 29 00                  jmp 0x140b18f29
00884D33  49 8B 07                        mov rax, qword ptr [r15]
00884D36  0F B7 08                        movzx ecx, word ptr [rax]
00884D39  48 8B 45 60                     mov rax, qword ptr [rbp + 0x60]
00884D3D  66 89 08                        mov word ptr [rax], cx
00884D40  E9 3D FF FF FF                  jmp 0x140884c82
00884D45  8B 46 28                        mov eax, dword ptr [rsi + 0x28]
00884D48  25 00 00 40 20                  and eax, 0x20400000
00884D4D  3D 00 00 40 00                  cmp eax, 0x400000
00884D52  0F 84 0A 42 29 00               je 0x140b18f62
00884D58  B8 00 00 A0 00                  mov eax, 0xa00000
00884D5D  23 C8                           and ecx, eax
00884D5F  3B C8                           cmp ecx, eax
00884D61  0F 84 FB 41 29 00               je 0x140b18f62
00884D67  BF BB 00 00 C0                  mov edi, 0xc00000bb
00884D6C  E9 41 FB FF FF                  jmp 0x1408848b2
00884D71  BF 45 00 00 C0                  mov edi, 0xc0000045
00884D76  E9 37 FB FF FF                  jmp 0x1408848b2
00884D7B  8B 56 30                        mov edx, dword ptr [rsi + 0x30]
00884D7E  E8 E1 50 25 00                  call 0x140ad9e64
00884D83  BF BB 00 00 C0                  mov edi, 0xc00000bb
00884D88  E9 15 FB FF FF                  jmp 0x1408848a2
00884D8D  4C 8B 7D D8                     mov r15, qword ptr [rbp - 0x28]
00884D91  49 8B D5                        mov rdx, r13
00884D94  49 8B CF                        mov rcx, r15
00884D97  E8 2C 0C A2 FF                  call 0x1402a59c8
00884D9C  E9 15 FB FF FF                  jmp 0x1408848b6
00884DA1  0F BA E2 19                     bt edx, 0x19
00884DA5  0F 83 BD FB FF FF               jae 0x140884968
00884DAB  8B 56 34                        mov edx, dword ptr [rsi + 0x34]
00884DAE  49 8B CE                        mov rcx, r14
00884DB1  4C 8B 4D 48                     mov r9, qword ptr [rbp + 0x48]
00884DB5  44 8A 46 38                     mov r8b, byte ptr [rsi + 0x38]
00884DB9  E8 36 D9 B4 FF                  call 0x1403d26f4
00884DBE  8B D8                           mov ebx, eax
00884DC0  85 C0                           test eax, eax
00884DC2  0F 88 66 FD FF FF               js 0x140884b2e
00884DC8  E9 9B FB FF FF                  jmp 0x140884968
00884DCD  41 83 F9 04                     cmp r9d, 4
00884DD1  0F 84 C6 FB FF FF               je 0x14088499d
00884DD7  41 81 F9 01 00 00 80            cmp r9d, 0x80000001
00884DDE  0F 84 B9 FB FF FF               je 0x14088499d
00884DE4  BB 45 00 00 C0                  mov ebx, 0xc0000045
00884DE9  E9 40 FD FF FF                  jmp 0x140884b2e
00884DEE  48 8B 55 E8                     mov rdx, qword ptr [rbp - 0x18]
00884DF2  41 B8 01 00 00 00               mov r8d, 1
00884DF8  49 8B CD                        mov rcx, r13
00884DFB  E8 30 28 20 00                  call 0x140a87630
00884E00  E9 40 FD FF FF                  jmp 0x140884b45
00884E05  B8 45 00 00 C0                  mov eax, 0xc0000045
00884E0A  E9 10 FA FF FF                  jmp 0x14088481f
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiReserveUserMemory(__int64 a1, __int64 a2, int a3, __int64 a4, __int64 a5)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned int v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned int v_stack_m80;
    unsigned int v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 32) = a4;
    *(unsigned int *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    v_rsp = (v_rsp) - (128);
    v_r12 = 0;
    v_stack_m68 = 0;
    if (a2 == 1) goto loc_00884CA9;
    a1 = (*(unsigned __int64 *)(a1 + 8)) - (*(unsigned __int64 *)(a1));
    a1 = (a1) + 1;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 88) + 1040)) + (768);
    v_stack_m50 = result;
    v_r15 = v_r12 + 8;
    if (a1 != (*(unsigned __int64 *)(a1 + 24))) { v_r15 = 0; }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 44)))) & (136)) != 0) goto loc_00884E05;
    if (((*(unsigned int *)(a1 + 64)) & (0x20000000ULL)) != 0) goto loc_00884856;
loc_0088451E:
    if ((((unsigned __int8)((unsigned int)(a3))) & (2)) != 0) goto loc_00884918;
loc_00884527:
    v_rdi = (((*(unsigned __int64 *)(a1 + 24)) & (0xFFFULL)) != 0) ? 1 : 0;
    result = (*(unsigned __int64 *)(a1 + 24)) >> (12);
    v_rdi = (v_rdi) + (result);
    v_stack_m58 = v_rdi;
    result = MiAllocatePool(64, 64, (unsigned int)(0x53646156ULL), a4);
    if (result == 0) goto loc_0088490E;
    *(unsigned __int64 *)(result + 16) = -2;
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 52))))) << (12));
    *(unsigned __int64 *)(result) = -2;
    *(unsigned __int64 *)(result + 8) = -2;
    a2 = (unsigned int)((a2) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(result + 48)))));
    a2 = (unsigned int)((a2) & (0x7F000ULL));
    *(unsigned __int64 *)(result + 40) = 0;
    a2 = (unsigned int)((a2) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(result + 48)))));
    *(unsigned int *)(result + 48) = (unsigned int)(a2);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 52))) != 0) goto loc_0088483B;
loc_0088459B:
    if (condition_is_above_or_equal) goto loc_0088486C;
loc_008845B1:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a3)))) << (7));
    result = (unsigned int)((result) ^ ((unsigned int)(a2)));
    result = (unsigned int)((result) & (0xF80ULL));
    result = (unsigned int)((result) ^ ((unsigned int)(a2)));
    *(unsigned int *)(result + 48) = (unsigned int)(result);
    if (!(condition_is_above_or_equal)) {
        *(unsigned int *)(result + 48) = (unsigned int)(result);
    }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 64)))) & (1)) != 0) goto loc_008848E2;
    a1 = v_rdi;
    if (condition_is_below) { a1 = result; }
loc_008845F3:
    *(unsigned int *)(result + 52) = (unsigned int)(a1);
    a1 = (a1) >> (32);
    *(unsigned __int8 *)(result + 34) = (unsigned __int8)(a1);
    v_stack_m60 = *(unsigned __int64 *)(gs_base + (0 + 392));
    result = MiGetProcessPartition(*(unsigned __int64 *)(a1 + 88), (unsigned int)(*(unsigned int *)(a1 + 64)), (unsigned int)(*(unsigned int *)(a1 + 40)), a4);
    *(unsigned __int16 *)(a5) = (unsigned __int16)(*(unsigned __int16 *)(result));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 40))))) & ((unsigned int)((unsigned int)(0x20400000ULL))));
    if (((unsigned int)(result)) == 0x20000000ULL) goto loc_008849F0;
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0x20400000ULL)))) goto loc_00884CB3;
    if (((unsigned int)(result)) == 0x400000ULL) goto loc_008848F1;
    if (((unsigned int)(result)) < 0x400000ULL) goto loc_00884C24;
loc_00884656:
    if (((unsigned int)((unsigned int)((unsigned int)(v_r15)))) >= 16) goto loc_00884C4A;
loc_0088465F:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 48))) & (0xFFE7FFFFULL));
    v_r12 = (unsigned int)((v_r12) << (19));
    a1 = (unsigned int)((a1) | ((unsigned int)(v_r12)));
    *(unsigned int *)(result + 48) = (unsigned int)(a1);
    if (((*(unsigned int *)(a1 + 40)) & (0x200000ULL)) != 0) goto loc_00884BE5;
loc_00884681:
    if (((*(unsigned __int8 *)(a1 + 112)) & (1)) != 0) goto loc_00884D45;
    if ((*(unsigned int *)(a1 + 48)) != 0) goto loc_00884D71;
    v_r15 = 0;
    v_stack_m58 = 0;
    if (condition_is_below) goto loc_00884AA9;
loc_008846A7:
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)(v_r15))) | (2));
    result = LOCK_ADDRESS_SPACE(v_stack_m60, *(unsigned __int64 *)(a1 + 88), (unsigned int)(*(unsigned int *)(a1 + 40)), a5);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 88) + 500)))) & (32)) != 0) goto loc_00884C40;
    if ((((unsigned __int8)(v_rbx)) & (8)) != 0) goto loc_00884874;
    v_stack_m70 = v_stack_m58;
    v_stack_m78 = v_stack_m48;
    v_stack_m80 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 64)));
    v_stack_m88 = (unsigned int)((unsigned int)(v_stack_p18));
    v_stack_m98 = *(unsigned __int64 *)(a1 + 16);
    result = MiSelectUserAddress((unsigned int)(*(unsigned int *)(a1 + 40)), *(unsigned __int64 *)(a1), *(unsigned __int64 *)(a1 + 8), *(unsigned __int64 *)(a1 + 24));
    if (sign_flag) goto loc_00884A0C;
    v_r12 = (v_stack_m58 - 1) + (*(unsigned __int64 *)(a1 + 24));
loc_00884734:
    result = (v_stack_m58) >> (12);
    v_stack_m40 = result;
    result = MiUpdateVadStartVpn(result, result, *(unsigned __int64 *)(a1 + 8), *(unsigned __int64 *)(a1 + 24));
    v_r12 = (v_r12) >> (12);
    *(unsigned int *)(result + 28) = (unsigned int)(v_r12);
    result = (v_r12) >> (32);
    *(unsigned __int8 *)(result + 33) = (unsigned __int8)(result);
    if (((*(unsigned __int8 *)(a1 + 112)) & (1)) != 0) goto loc_00884D7B;
    result = MiInsertVadCharges(result, *(unsigned __int64 *)(a1 + 88), *(unsigned __int64 *)(a1 + 8), *(unsigned __int64 *)(a1 + 24));
    v_stack_m68 = (unsigned int)(result);
    if (sign_flag) goto loc_008848A2;
    if (0 != 0) goto loc_00884AC6;
    result = MiLockVad(v_stack_m60, result, *(unsigned __int64 *)(a1 + 8), *(unsigned __int64 *)(a1 + 24));
loc_00884795:
    a3 = 0;
    result = MiInsertVad(result, *(unsigned __int64 *)(a1 + 88), a3, *(unsigned __int64 *)(a1 + 24));
    if (v_stack_m48 != 0) {
        a1 = v_stack_m40;
        a2 = v_r12;
        result = MiAdvanceVadHint(a1, a2, v_stack_m48, *(unsigned __int64 *)(a1 + 24));
    }
    v_r12 = 0;
    if ((*(unsigned int *)(a1 + 120)) != 0) goto loc_00884931;
    if ((*(unsigned int *)(a1 + 120)) >= 0) goto loc_008847EC;
    if ((*(unsigned int *)(a1 + 120)) < 0) goto loc_00884931;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 48))) & ((unsigned int)((unsigned int)(0x180000ULL))));
    if (((unsigned int)(result)) >= 0x100000ULL) goto loc_00884931;
loc_008847EC:
    if ((*(unsigned __int64 *)(a1 + 72)) != 0) goto loc_00884931;
    if (0 != 0) goto loc_00884B4C;
    result = MiUnlockVad(v_stack_m60, result, v_stack_m48, *(unsigned __int64 *)(a1 + 24));
    result = UNLOCK_ADDRESS_SPACE(v_stack_m60, *(unsigned __int64 *)(a1 + 88), v_stack_m48, *(unsigned __int64 *)(a1 + 24));
loc_00884816:
    *(unsigned __int64 *)(v_stack_p20) = v_stack_m58;
    result = 0;
loc_0088481F:
    v_rsp = (v_rsp) + (128);
    return result;
loc_0088483B:
    *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 88) + 1040) + 1060) = 1;
    goto loc_0088459B;
loc_00884856:
    if (((*(unsigned __int64 *)(v_rip + 7610919)) & (0x80000ULL)) == 0) goto loc_00884527;
    goto loc_0088451E;
loc_0088486C:
    goto loc_008845B1;
loc_00884874:
    if (condition_is_below) goto loc_00884A29;
    v_stack_p20 = (unsigned int)(*(unsigned int *)(result + 48));
    result = MiIsVaRangeAvailable(*(unsigned __int64 *)(a1 + 88), 0, *(unsigned __int64 *)(a1 + 24), 0);
    if ((unsigned int)(result) != 0) goto loc_00884A42;
loc_008848A2:
    *(unsigned __int64 *)(v_stack_p20) = v_stack_m58;
    if (0 != 0) goto loc_00884D8D;
loc_008848B2:
loc_008848B6:
    result = v_stack_p20;
    if ((((unsigned __int8)(v_stack_p8)) & (2)) != 0) {
        a2 = *(unsigned __int64 *)(a1 + 88);
        a1 = v_stack_m60;
        result = UNLOCK_ADDRESS_SPACE(a1, a2, *(unsigned __int64 *)(a1 + 24), 0);
    }
    a2 = 0;
    result = MiReleaseVadEventBlocks(result, a2, *(unsigned __int64 *)(a1 + 24), 0);
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, *(unsigned __int64 *)(a1 + 24), 0);
    goto loc_0088481F;
loc_008848E2:
    goto loc_008845F3;
loc_008848F1:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_stack_p8))) & (7));
    result = (unsigned int)(((unsigned int)((unsigned int)(v_stack_p8))) & (0xFFFFFFF8ULL));
    if (((unsigned int)(result)) != 16) goto loc_00884B9C;
loc_00884904:
    goto loc_008848B2;
loc_0088490E:
    goto loc_0088481F;
loc_00884918:
    result = MiArbitraryCodeBlocked(*(unsigned __int64 *)(a1 + 96), a2, *(unsigned __int64 *)(a1 + 24), 0);
    v_stack_m68 = (unsigned int)(result);
    if (!sign_flag) goto loc_00884527;
    goto loc_0088481F;
loc_00884931:
    result = UNLOCK_ADDRESS_SPACE((unsigned int)((unsigned int)(v_stack_m60)), *(unsigned __int64 *)(a1 + 88), *(unsigned __int64 *)(a1 + 24), 0);
    result = MiReferenceVad(result, *(unsigned __int64 *)(a1 + 88), *(unsigned __int64 *)(a1 + 24), 0);
    if (condition_is_above_or_equal) goto loc_00884968;
    if (condition_is_below) goto loc_00884DA1;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + 48))))) & ((unsigned int)((unsigned int)(0xC0000045ULL))));
    if (((unsigned int)(result)) >= 0x100000ULL) goto loc_00884DA1;
loc_00884968:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 120))) != 0) goto loc_00884B1A;
loc_00884975:
    if ((*(unsigned __int64 *)(a1 + 72)) == 0) goto loc_008849DA;
    v_stack_p10 = 0;
    if (((*(unsigned int *)(a1 + 64)) & (0x40000000ULL)) != 0) goto loc_00884A52;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 68)) - 1)) > 1) goto loc_00884DCD;
loc_0088499D:
    v_stack_p28 = v_stack_p10;
    v_stack_p20 = 0;
    result = MiSecureVad(result, v_stack_m60, *(unsigned __int64 *)(a1 + 24), (unsigned int)(*(unsigned int *)(a1 + 68)));
loc_008849C0:
    if (sign_flag) goto loc_00884B2E;
    a2 = (v_stack_p10) ^ (*(unsigned __int64 *)(a1 + 88));
    a2 = (a2) ^ (*(unsigned __int64 *)(v_rip + 5935529));
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72)) = a2;
loc_008849DA:
    if (0 != 0) goto loc_00884C1A;
    result = MiUnlockAndDereferenceVad(result, a2, *(unsigned __int64 *)(a1 + 24), (unsigned int)(*(unsigned int *)(a1 + 68)));
    goto loc_00884816;
loc_008849F0:
    v_r15 = (unsigned int)((v_stack_m60) | (16));
    v_r12 = ((unsigned int)(*(unsigned int *)(a1 + 112))) >> (4);
    v_r12 = (unsigned int)((v_r12) & (1));
    v_r12 = (unsigned int)((v_r12) | (2));
    goto loc_00884656;
loc_00884A0C:
    result = MiLogReserveVaFailed(*(unsigned __int64 *)(a1 + 24), *(unsigned __int64 *)(a1 + 16), *(unsigned __int64 *)(a1), *(unsigned __int64 *)(a1 + 8));
    goto loc_008848A2;
loc_00884A29:
    result = MiFindPlaceholderVadToReplace(*(unsigned __int64 *)(a1 + 24), *(unsigned __int64 *)(a1 + 16), *(unsigned __int8 *)(a1 + 57), v_stack_m68);
    if (result == 0) goto loc_00884C12;
loc_00884A42:
    v_stack_m58 = *(unsigned __int64 *)(a1);
    goto loc_00884734;
loc_00884A52:
    a3 = (*(unsigned __int8 *)(result + 33)) << (32);
    a3 = (a3) | ((unsigned int)(*(unsigned int *)(result + 28)));
    a2 = (*(unsigned __int8 *)(result + 32)) << (32);
    a2 = (a2) | ((unsigned int)(*(unsigned int *)(result + 24)));
    a3 = (a3) << (12);
    a2 = (a2) << (12);
    a3 = (a3) | (0xFFFULL);
    v_stack_p20 = 1;
    result = MiAddSecureEntry(result, a2, a3, v_stack_m68);
    a1 = -(result);
    v_rbx = (unsigned int)(~((unsigned int)((unsigned int)(v_r15))));
    v_rbx = (unsigned int)((v_rbx) & (0xC000009AULL));
    goto loc_008849C0;
loc_00884AA9:
    result = MiCreatePlaceholderStorage(result, result, a3, v_stack_m68);
    v_stack_m68 = (unsigned int)(result);
    if (sign_flag) goto loc_008848A2;
    v_rbx = (unsigned int)((v_rbx) | (4));
    goto loc_008846A7;
loc_00884AC6:
    result = MiPreparePlaceholderVadReplacement(result, *(unsigned __int64 *)(a1 + 88), v_stack_m50, v_stack_m68);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(result + 40, a2, a3, v_stack_m68);
    if (!(condition_is_above_or_equal)) {
        a3 = result + 40;
        a2 = result;
        a1 = result + 40;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, v_stack_m68);
    }
    if (result == 0) goto loc_00884795;
    *(unsigned __int8 *)(result + 10) = 1;
    goto loc_00884795;
loc_00884B1A:
    a2 = 0;
    result = MiCommitVadMetadataBits(result, a2, a3, v_stack_m68);
    if (!sign_flag) goto loc_00884975;
loc_00884B2E:
    a3 = 0;
    result = MiDeleteVad(result, result, a3, v_stack_m68);
    if (result != 0) goto loc_00884DEE;
loc_00884B45:
    goto loc_0088481F;
loc_00884B4C:
    result = ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))))) | (-1);
    result = (unsigned __int8)((result) & (6));
    if (((unsigned __int8)(result)) == 2) goto loc_00884C9B;
loc_00884B60:
    result = KeAbPostRelease(result + 40, result, a3, v_stack_m68);
    result = UNLOCK_ADDRESS_SPACE((unsigned int)((unsigned int)(result)), *(unsigned __int64 *)(a1 + 88), a3, v_stack_m68);
loc_00884B79:
    result = MiSetVadDeleted(result, *(unsigned __int64 *)(a1 + 88), a3, v_stack_m68);
    a3 = 0;
    a2 = 0;
    result = MiDeleteVad(result, a2, a3, v_stack_m68);
    result = MiDecrementVadsBeingDeleted(v_stack_m50, a2, a3, v_stack_m68);
    goto loc_00884816;
loc_00884B9C:
    if (((unsigned int)(v_stack_m50)) != 4) goto loc_00884CCE;
loc_00884BA5:
    if (((*(unsigned __int8 *)(a1 + 112)) & (1)) != 0) goto loc_00884CDC;
loc_00884BB1:
    result = MiCreateUserPhysicalView(result, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), a1, v_stack_m68);
    v_stack_m68 = (unsigned int)(result);
    if (sign_flag) goto loc_00884D0C;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 48))) & (0xFFFFFFBFULL));
    result = (unsigned int)((result) | (48));
loc_00884BDC:
    *(unsigned int *)(result + 48) = (unsigned int)(result);
    goto loc_00884656;
loc_00884BE5:
    result = MiCreateWriteWatchView(*(unsigned __int64 *)(a1 + 88), result, result, v_stack_m68);
    v_stack_m68 = (unsigned int)(result);
    if (sign_flag) goto loc_008848B2;
    *(unsigned int *)(result + 48) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 48)));
    goto loc_00884681;
loc_00884C12:
    goto loc_008848A2;
loc_00884C1A:
    result = MiUnlockAndDereferenceNestedVad((unsigned int)(*(unsigned int *)(result + 48)), result, result, v_stack_m68);
    goto loc_00884B79;
loc_00884C24:
    result = MiCreateRotateView(result, result, result, v_stack_m68);
    if ((unsigned int)(result) == 0) goto loc_00884D0C;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 48))) & (0xFFFFFFCFULL));
    result = (unsigned int)((result) | (64));
    goto loc_00884BDC;
loc_00884C40:
    goto loc_008848A2;
loc_00884C4A:
    if ((((unsigned __int8)(*(unsigned __int64 *)(a1 + 112))) & (4)) != 0) goto loc_00884D16;
    a4 = 0;
    result = MiCreateLargePageVad(*(unsigned __int64 *)(a1 + 88), result, v_stack_p10, a4);
    v_stack_m68 = (unsigned int)(result);
    if (sign_flag) goto loc_008848B2;
    if (v_stack_p10 != 0) goto loc_00884D33;
loc_00884C82:
    if (((*(unsigned __int8 *)(a1 + 112)) & (26)) == 0) goto loc_0088465F;
    goto loc_0088465F;
loc_00884C9B:
    result = ExfTryToWakePushLock(result + 40, result, v_stack_p10, a4);
    goto loc_00884B60;
loc_00884CA9:
    goto loc_0088481F;
loc_00884CB3:
    if (((*(unsigned __int8 *)(a1 + 112)) & (2)) == 0) goto loc_00884656;
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)(v_stack_p10))) | (16));
    goto loc_00884656;
loc_00884CCE:
    if (((unsigned int)(result + 40)) != 1) goto loc_00884904;
    goto loc_00884BA5;
loc_00884CDC:
    if ((*(unsigned __int64 *)(a1 + 104)) == 1) goto loc_00884904;
    a2 = (unsigned int)((result) | (2));
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 48)))) & (0x1C000ULL)) == 0) { a2 = (unsigned int)(v_rbx); }
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 48)))) & (0x12000ULL)) == 0) goto loc_00884BB1;
    a2 = (unsigned int)((a2) & (0xFFFFFFFEULL));
    a2 = (unsigned int)((a2) | (4));
    goto loc_00884BB1;
loc_00884D0C:
    goto loc_008848B2;
loc_00884D16:
loc_00884D33:
    *(unsigned __int16 *)(a5) = (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p10)));
    goto loc_00884C82;
loc_00884D45:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 40))) & (0x20400000ULL));
    a1 = (unsigned int)((*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p10))) & ((unsigned int)((unsigned int)(0xA00000ULL))));
    goto loc_008848B2;
loc_00884D71:
    goto loc_008848B2;
loc_00884D7B:
    result = MiStoreGraphicsProtectionInVad(a1, (unsigned int)(*(unsigned int *)(a1 + 48)), v_stack_p10, a4);
    goto loc_008848A2;
loc_00884D8D:
    result = MiUnlockVad(v_stack_m60, result, v_stack_p10, a4);
    goto loc_008848B6;
loc_00884DA1:
    if (((unsigned int)(a1)) >= ((unsigned int)((unsigned int)(0xA00000ULL)))) goto loc_00884968;
    result = MiMapUserLargePages(result, (unsigned int)(*(unsigned int *)(a1 + 52)), *(unsigned __int8 *)(a1 + 56), v_stack_p10);
    if (sign_flag) goto loc_00884B2E;
    goto loc_00884968;
loc_00884DCD:
    if (((unsigned int)(v_stack_p10)) == 4) goto loc_0088499D;
    if (((unsigned int)(v_stack_p10)) == 0x80000001ULL) goto loc_0088499D;
    goto loc_00884B2E;
loc_00884DEE:
    result = MiFinishPlaceholderVadReplacement(result, v_stack_m50, 1, v_stack_p10);
    goto loc_00884B45;
loc_00884E05:
    goto loc_0088481F;
}
```

## 5. (Beta) C Style

```c
int64_t MiReserveUserMemory(void *Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4, void *Arg5)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg5 = (uint8_t *)Arg5;

    int64_t result;
    int64_t local_r12;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint32_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint32_t v_stack_m80;
    uint32_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_p10;
    uint32_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x20) = Arg4;
    *(uint32_t *)(local_rsp + 0x18) = Arg3;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    local_rsp = (local_rsp) - (128);
    local_r12 = 0;
    v_stack_m68 = 0;
    if (Arg2 == 1) goto loc_00884CA9;
    Arg1 = (*(uint64_t *)(arg1 + 0x8)) - (*(uint64_t *)(arg1));
    Arg1 = (Arg1) + 1;
    result = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x58) + 0x410)) + (768);
    v_stack_m50 = result;
    local_r15 = local_r12 + 8;
    if (Arg1 != (*(uint64_t *)(arg1 + 0x18))) { local_r15 = 0; }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x2C)))) & (136)) != 0) goto loc_00884E05;
    if (((*(uint32_t *)(arg1 + 0x40)) & (0x20000000ULL)) != 0) goto loc_00884856;
loc_0088451E:
    if ((((uint8_t)((uint32_t)(Arg3))) & (2)) != 0) goto loc_00884918;
loc_00884527:
    local_rdi = (((*(uint64_t *)(arg1 + 0x18)) & (0xFFFULL)) != 0) ? 1 : 0;
    result = (*(uint64_t *)(arg1 + 0x18)) >> (12);
    local_rdi = (local_rdi) + (result);
    v_stack_m58 = local_rdi;
    result = MiAllocatePool(64, 64, (uint32_t)(0x53646156ULL), Arg4);
    if (result == 0) goto loc_0088490E;
    *(uint64_t *)(result + 0x10) = -2;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x34))))) << (12));
    *(uint64_t *)(result) = -2;
    *(uint64_t *)(result + 0x8) = -2;
    Arg2 = (uint32_t)((Arg2) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x30)))));
    Arg2 = (uint32_t)((Arg2) & (0x7F000ULL));
    *(uint64_t *)(result + 0x28) = 0;
    Arg2 = (uint32_t)((Arg2) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x30)))));
    *(uint32_t *)(result + 0x30) = (uint32_t)(Arg2);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x34))) != 0) goto loc_0088483B;
loc_0088459B:
    if (condition_is_above_or_equal) goto loc_0088486C;
loc_008845B1:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg3)))) << (7));
    result = (uint32_t)((result) ^ ((uint32_t)(Arg2)));
    result = (uint32_t)((result) & (0xF80ULL));
    result = (uint32_t)((result) ^ ((uint32_t)(Arg2)));
    *(uint32_t *)(result + 0x30) = (uint32_t)(result);
    if (!(condition_is_above_or_equal)) {
        *(uint32_t *)(result + 0x30) = (uint32_t)(result);
    }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x40)))) & (1)) != 0) goto loc_008848E2;
    Arg1 = local_rdi;
    if (condition_is_below) { Arg1 = result; }
loc_008845F3:
    *(uint32_t *)(result + 0x34) = (uint32_t)(Arg1);
    Arg1 = (Arg1) >> (32);
    *(uint8_t *)(result + 0x22) = (uint8_t)(Arg1);
    v_stack_m60 = *(uint64_t *)(gs_base + (0 + 0x188));
    result = MiGetProcessPartition(*(uint64_t *)(arg1 + 0x58), (uint32_t)(*(uint32_t *)(arg1 + 0x40)), (uint32_t)(*(uint32_t *)(arg1 + 0x28)), Arg4);
    *(uint16_t *)(arg5) = (uint16_t)(*(uint16_t *)(result));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x28))))) & ((uint32_t)((uint32_t)(0x20400000ULL))));
    if (((uint32_t)(result)) == 0x20000000ULL) goto loc_008849F0;
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0x20400000ULL)))) goto loc_00884CB3;
    if (((uint32_t)(result)) == 0x400000ULL) goto loc_008848F1;
    if (((uint32_t)(result)) < 0x400000ULL) goto loc_00884C24;
loc_00884656:
    if (((uint32_t)((uint32_t)((uint32_t)(local_r15)))) >= 16) goto loc_00884C4A;
loc_0088465F:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x30))) & (0xFFE7FFFFULL));
    local_r12 = (uint32_t)((local_r12) << (19));
    Arg1 = (uint32_t)((Arg1) | ((uint32_t)(local_r12)));
    *(uint32_t *)(result + 0x30) = (uint32_t)(Arg1);
    if (((*(uint32_t *)(arg1 + 0x28)) & (0x200000ULL)) != 0) goto loc_00884BE5;
loc_00884681:
    if (((*(uint8_t *)(arg1 + 0x70)) & (1)) != 0) goto loc_00884D45;
    if ((*(uint32_t *)(arg1 + 0x30)) != 0) goto loc_00884D71;
    local_r15 = 0;
    v_stack_m58 = 0;
    if (condition_is_below) goto loc_00884AA9;
loc_008846A7:
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)(local_r15))) | (2));
    result = LOCK_ADDRESS_SPACE(v_stack_m60, *(uint64_t *)(arg1 + 0x58), (uint32_t)(*(uint32_t *)(arg1 + 0x28)), Arg5);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x58) + 0x1F4)))) & (32)) != 0) goto loc_00884C40;
    if ((((uint8_t)(local_rbx)) & (8)) != 0) goto loc_00884874;
    v_stack_m70 = v_stack_m58;
    v_stack_m78 = v_stack_m48;
    v_stack_m80 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x40)));
    v_stack_m88 = (uint32_t)((uint32_t)(v_stack_p18));
    v_stack_m98 = *(uint64_t *)(arg1 + 0x10);
    result = MiSelectUserAddress((uint32_t)(*(uint32_t *)(arg1 + 0x28)), *(uint64_t *)(arg1), *(uint64_t *)(arg1 + 0x8), *(uint64_t *)(arg1 + 0x18));
    if (sign_flag) goto loc_00884A0C;
    local_r12 = (v_stack_m58 - 1) + (*(uint64_t *)(arg1 + 0x18));
loc_00884734:
    result = (v_stack_m58) >> (12);
    v_stack_m40 = result;
    result = MiUpdateVadStartVpn(result, result, *(uint64_t *)(arg1 + 0x8), *(uint64_t *)(arg1 + 0x18));
    local_r12 = (local_r12) >> (12);
    *(uint32_t *)(result + 0x1C) = (uint32_t)(local_r12);
    result = (local_r12) >> (32);
    *(uint8_t *)(result + 0x21) = (uint8_t)(result);
    if (((*(uint8_t *)(arg1 + 0x70)) & (1)) != 0) goto loc_00884D7B;
    result = MiInsertVadCharges(result, *(uint64_t *)(arg1 + 0x58), *(uint64_t *)(arg1 + 0x8), *(uint64_t *)(arg1 + 0x18));
    v_stack_m68 = (uint32_t)(result);
    if (sign_flag) goto loc_008848A2;
    if (0 != 0) goto loc_00884AC6;
    result = MiLockVad(v_stack_m60, result, *(uint64_t *)(arg1 + 0x8), *(uint64_t *)(arg1 + 0x18));
loc_00884795:
    Arg3 = 0;
    result = MiInsertVad(result, *(uint64_t *)(arg1 + 0x58), Arg3, *(uint64_t *)(arg1 + 0x18));
    if (v_stack_m48 != 0) {
        Arg1 = v_stack_m40;
        Arg2 = local_r12;
        result = MiAdvanceVadHint(Arg1, Arg2, v_stack_m48, *(uint64_t *)(arg1 + 0x18));
    }
    local_r12 = 0;
    if ((*(uint32_t *)(arg1 + 0x78)) != 0) goto loc_00884931;
    if ((*(uint32_t *)(arg1 + 0x78)) >= 0) goto loc_008847EC;
    if ((*(uint32_t *)(arg1 + 0x78)) < 0) goto loc_00884931;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x30))) & ((uint32_t)((uint32_t)(0x180000ULL))));
    if (((uint32_t)(result)) >= 0x100000ULL) goto loc_00884931;
loc_008847EC:
    if ((*(uint64_t *)(arg1 + 0x48)) != 0) goto loc_00884931;
    if (0 != 0) goto loc_00884B4C;
    result = MiUnlockVad(v_stack_m60, result, v_stack_m48, *(uint64_t *)(arg1 + 0x18));
    result = UNLOCK_ADDRESS_SPACE(v_stack_m60, *(uint64_t *)(arg1 + 0x58), v_stack_m48, *(uint64_t *)(arg1 + 0x18));
loc_00884816:
    *(uint64_t *)(v_stack_p20) = v_stack_m58;
    result = 0;
loc_0088481F:
    local_rsp = (local_rsp) + (128);
    return result;
loc_0088483B:
    *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x58) + 0x410) + 0x424) = 1;
    goto loc_0088459B;
loc_00884856:
    if (((*(uint64_t *)(v_rip + 0x742227)) & (0x80000ULL)) == 0) goto loc_00884527;
    goto loc_0088451E;
loc_0088486C:
    goto loc_008845B1;
loc_00884874:
    if (condition_is_below) goto loc_00884A29;
    v_stack_p20 = (uint32_t)(*(uint32_t *)(result + 0x30));
    result = MiIsVaRangeAvailable(*(uint64_t *)(arg1 + 0x58), 0, *(uint64_t *)(arg1 + 0x18), 0);
    if ((uint32_t)(result) != 0) goto loc_00884A42;
loc_008848A2:
    *(uint64_t *)(v_stack_p20) = v_stack_m58;
    if (0 != 0) goto loc_00884D8D;
loc_008848B2:
loc_008848B6:
    result = v_stack_p20;
    if ((((uint8_t)(v_stack_p8)) & (2)) != 0) {
        Arg2 = *(uint64_t *)(arg1 + 0x58);
        Arg1 = v_stack_m60;
        result = UNLOCK_ADDRESS_SPACE(Arg1, Arg2, *(uint64_t *)(arg1 + 0x18), 0);
    }
    Arg2 = 0;
    result = MiReleaseVadEventBlocks(result, Arg2, *(uint64_t *)(arg1 + 0x18), 0);
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, *(uint64_t *)(arg1 + 0x18), 0);
    goto loc_0088481F;
loc_008848E2:
    goto loc_008845F3;
loc_008848F1:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(v_stack_p8))) & (7));
    result = (uint32_t)(((uint32_t)((uint32_t)(v_stack_p8))) & (0xFFFFFFF8ULL));
    if (((uint32_t)(result)) != 16) goto loc_00884B9C;
loc_00884904:
    goto loc_008848B2;
loc_0088490E:
    goto loc_0088481F;
loc_00884918:
    result = MiArbitraryCodeBlocked(*(uint64_t *)(arg1 + 0x60), Arg2, *(uint64_t *)(arg1 + 0x18), 0);
    v_stack_m68 = (uint32_t)(result);
    if (!sign_flag) goto loc_00884527;
    goto loc_0088481F;
loc_00884931:
    result = UNLOCK_ADDRESS_SPACE((uint32_t)((uint32_t)(v_stack_m60)), *(uint64_t *)(arg1 + 0x58), *(uint64_t *)(arg1 + 0x18), 0);
    result = MiReferenceVad(result, *(uint64_t *)(arg1 + 0x58), *(uint64_t *)(arg1 + 0x18), 0);
    if (condition_is_above_or_equal) goto loc_00884968;
    if (condition_is_below) goto loc_00884DA1;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x30))))) & ((uint32_t)((uint32_t)(0xC0000045ULL))));
    if (((uint32_t)(result)) >= 0x100000ULL) goto loc_00884DA1;
loc_00884968:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x78))) != 0) goto loc_00884B1A;
loc_00884975:
    if ((*(uint64_t *)(arg1 + 0x48)) == 0) goto loc_008849DA;
    v_stack_p10 = 0;
    if (((*(uint32_t *)(arg1 + 0x40)) & (0x40000000ULL)) != 0) goto loc_00884A52;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x44)) - 1)) > 1) goto loc_00884DCD;
loc_0088499D:
    v_stack_p28 = v_stack_p10;
    v_stack_p20 = 0;
    result = MiSecureVad(result, v_stack_m60, *(uint64_t *)(arg1 + 0x18), (uint32_t)(*(uint32_t *)(arg1 + 0x44)));
loc_008849C0:
    if (sign_flag) goto loc_00884B2E;
    Arg2 = (v_stack_p10) ^ (*(uint64_t *)(arg1 + 0x58));
    Arg2 = (Arg2) ^ (*(uint64_t *)(v_rip + 0x5A91A9));
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x48)) = Arg2;
loc_008849DA:
    if (0 != 0) goto loc_00884C1A;
    result = MiUnlockAndDereferenceVad(result, Arg2, *(uint64_t *)(arg1 + 0x18), (uint32_t)(*(uint32_t *)(arg1 + 0x44)));
    goto loc_00884816;
loc_008849F0:
    local_r15 = (uint32_t)((v_stack_m60) | (16));
    local_r12 = ((uint32_t)(*(uint32_t *)(arg1 + 0x70))) >> (4);
    local_r12 = (uint32_t)((local_r12) & (1));
    local_r12 = (uint32_t)((local_r12) | (2));
    goto loc_00884656;
loc_00884A0C:
    result = MiLogReserveVaFailed(*(uint64_t *)(arg1 + 0x18), *(uint64_t *)(arg1 + 0x10), *(uint64_t *)(arg1), *(uint64_t *)(arg1 + 0x8));
    goto loc_008848A2;
loc_00884A29:
    result = MiFindPlaceholderVadToReplace(*(uint64_t *)(arg1 + 0x18), *(uint64_t *)(arg1 + 0x10), *(uint8_t *)(arg1 + 0x39), v_stack_m68);
    if (result == 0) goto loc_00884C12;
loc_00884A42:
    v_stack_m58 = *(uint64_t *)(arg1);
    goto loc_00884734;
loc_00884A52:
    Arg3 = (*(uint8_t *)(result + 0x21)) << (32);
    Arg3 = (Arg3) | ((uint32_t)(*(uint32_t *)(result + 0x1C)));
    Arg2 = (*(uint8_t *)(result + 0x20)) << (32);
    Arg2 = (Arg2) | ((uint32_t)(*(uint32_t *)(result + 0x18)));
    Arg3 = (Arg3) << (12);
    Arg2 = (Arg2) << (12);
    Arg3 = (Arg3) | (0xFFFULL);
    v_stack_p20 = 1;
    result = MiAddSecureEntry(result, Arg2, Arg3, v_stack_m68);
    Arg1 = -(result);
    local_rbx = (uint32_t)(~((uint32_t)((uint32_t)(local_r15))));
    local_rbx = (uint32_t)((local_rbx) & (0xC000009AULL));
    goto loc_008849C0;
loc_00884AA9:
    result = MiCreatePlaceholderStorage(result, result, Arg3, v_stack_m68);
    v_stack_m68 = (uint32_t)(result);
    if (sign_flag) goto loc_008848A2;
    local_rbx = (uint32_t)((local_rbx) | (4));
    goto loc_008846A7;
loc_00884AC6:
    result = MiPreparePlaceholderVadReplacement(result, *(uint64_t *)(arg1 + 0x58), v_stack_m50, v_stack_m68);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(result + 40, Arg2, Arg3, v_stack_m68);
    if (!(condition_is_above_or_equal)) {
        Arg3 = result + 40;
        Arg2 = result;
        Arg1 = result + 40;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, v_stack_m68);
    }
    if (result == 0) goto loc_00884795;
    *(uint8_t *)(result + 0xA) = 1;
    goto loc_00884795;
loc_00884B1A:
    Arg2 = 0;
    result = MiCommitVadMetadataBits(result, Arg2, Arg3, v_stack_m68);
    if (!sign_flag) goto loc_00884975;
loc_00884B2E:
    Arg3 = 0;
    result = MiDeleteVad(result, result, Arg3, v_stack_m68);
    if (result != 0) goto loc_00884DEE;
loc_00884B45:
    goto loc_0088481F;
loc_00884B4C:
    result = ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))))) | (-1);
    result = (uint8_t)((result) & (6));
    if (((uint8_t)(result)) == 2) goto loc_00884C9B;
loc_00884B60:
    result = KeAbPostRelease(result + 40, result, Arg3, v_stack_m68);
    result = UNLOCK_ADDRESS_SPACE((uint32_t)((uint32_t)(result)), *(uint64_t *)(arg1 + 0x58), Arg3, v_stack_m68);
loc_00884B79:
    result = MiSetVadDeleted(result, *(uint64_t *)(arg1 + 0x58), Arg3, v_stack_m68);
    Arg3 = 0;
    Arg2 = 0;
    result = MiDeleteVad(result, Arg2, Arg3, v_stack_m68);
    result = MiDecrementVadsBeingDeleted(v_stack_m50, Arg2, Arg3, v_stack_m68);
    goto loc_00884816;
loc_00884B9C:
    if (((uint32_t)(v_stack_m50)) != 4) goto loc_00884CCE;
loc_00884BA5:
    if (((*(uint8_t *)(arg1 + 0x70)) & (1)) != 0) goto loc_00884CDC;
loc_00884BB1:
    result = MiCreateUserPhysicalView(result, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), Arg1, v_stack_m68);
    v_stack_m68 = (uint32_t)(result);
    if (sign_flag) goto loc_00884D0C;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x30))) & (0xFFFFFFBFULL));
    result = (uint32_t)((result) | (48));
loc_00884BDC:
    *(uint32_t *)(result + 0x30) = (uint32_t)(result);
    goto loc_00884656;
loc_00884BE5:
    result = MiCreateWriteWatchView(*(uint64_t *)(arg1 + 0x58), result, result, v_stack_m68);
    v_stack_m68 = (uint32_t)(result);
    if (sign_flag) goto loc_008848B2;
    *(uint32_t *)(result + 0x30) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x30)));
    goto loc_00884681;
loc_00884C12:
    goto loc_008848A2;
loc_00884C1A:
    result = MiUnlockAndDereferenceNestedVad((uint32_t)(*(uint32_t *)(result + 0x30)), result, result, v_stack_m68);
    goto loc_00884B79;
loc_00884C24:
    result = MiCreateRotateView(result, result, result, v_stack_m68);
    if ((uint32_t)(result) == 0) goto loc_00884D0C;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x30))) & (0xFFFFFFCFULL));
    result = (uint32_t)((result) | (64));
    goto loc_00884BDC;
loc_00884C40:
    goto loc_008848A2;
loc_00884C4A:
    if ((((uint8_t)(*(uint64_t *)(arg1 + 0x70))) & (4)) != 0) goto loc_00884D16;
    Arg4 = 0;
    result = MiCreateLargePageVad(*(uint64_t *)(arg1 + 0x58), result, v_stack_p10, Arg4);
    v_stack_m68 = (uint32_t)(result);
    if (sign_flag) goto loc_008848B2;
    if (v_stack_p10 != 0) goto loc_00884D33;
loc_00884C82:
    if (((*(uint8_t *)(arg1 + 0x70)) & (26)) == 0) goto loc_0088465F;
    goto loc_0088465F;
loc_00884C9B:
    result = ExfTryToWakePushLock(result + 40, result, v_stack_p10, Arg4);
    goto loc_00884B60;
loc_00884CA9:
    goto loc_0088481F;
loc_00884CB3:
    if (((*(uint8_t *)(arg1 + 0x70)) & (2)) == 0) goto loc_00884656;
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)(v_stack_p10))) | (16));
    goto loc_00884656;
loc_00884CCE:
    if (((uint32_t)(result + 40)) != 1) goto loc_00884904;
    goto loc_00884BA5;
loc_00884CDC:
    if ((*(uint64_t *)(arg1 + 0x68)) == 1) goto loc_00884904;
    Arg2 = (uint32_t)((result) | (2));
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x30)))) & (0x1C000ULL)) == 0) { Arg2 = (uint32_t)(local_rbx); }
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x30)))) & (0x12000ULL)) == 0) goto loc_00884BB1;
    Arg2 = (uint32_t)((Arg2) & (0xFFFFFFFEULL));
    Arg2 = (uint32_t)((Arg2) | (4));
    goto loc_00884BB1;
loc_00884D0C:
    goto loc_008848B2;
loc_00884D16:
loc_00884D33:
    *(uint16_t *)(arg5) = (uint16_t)(*(uint16_t *)(*(uint64_t *)(v_stack_p10)));
    goto loc_00884C82;
loc_00884D45:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x28))) & (0x20400000ULL));
    Arg1 = (uint32_t)((*(uint16_t *)(*(uint64_t *)(v_stack_p10))) & ((uint32_t)((uint32_t)(0xA00000ULL))));
    goto loc_008848B2;
loc_00884D71:
    goto loc_008848B2;
loc_00884D7B:
    result = MiStoreGraphicsProtectionInVad(Arg1, (uint32_t)(*(uint32_t *)(arg1 + 0x30)), v_stack_p10, Arg4);
    goto loc_008848A2;
loc_00884D8D:
    result = MiUnlockVad(v_stack_m60, result, v_stack_p10, Arg4);
    goto loc_008848B6;
loc_00884DA1:
    if (((uint32_t)(Arg1)) >= ((uint32_t)((uint32_t)(0xA00000ULL)))) goto loc_00884968;
    result = MiMapUserLargePages(result, (uint32_t)(*(uint32_t *)(arg1 + 0x34)), *(uint8_t *)(arg1 + 0x38), v_stack_p10);
    if (sign_flag) goto loc_00884B2E;
    goto loc_00884968;
loc_00884DCD:
    if (((uint32_t)(v_stack_p10)) == 4) goto loc_0088499D;
    if (((uint32_t)(v_stack_p10)) == 0x80000001ULL) goto loc_0088499D;
    goto loc_00884B2E;
loc_00884DEE:
    result = MiFinishPlaceholderVadReplacement(result, v_stack_m50, 1, v_stack_p10);
    goto loc_00884B45;
loc_00884E05:
    goto loc_0088481F;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x28` | `32` | `R` |
| `Arg1` | `+ 0x2C` | `32` | `R` |
| `Arg1` | `+ 0x30` | `32` | `R` |
| `Arg1` | `+ 0x34` | `32` | `R` |
| `Arg1` | `+ 0x38` | `8` | `R` |
| `Arg1` | `+ 0x39` | `8` | `R` |
| `Arg1` | `+ 0x40` | `32` | `R` |
| `Arg1` | `+ 0x40` | `32` | `R/W` |
| `Arg1` | `+ 0x44` | `32` | `R` |
| `Arg1` | `+ 0x48` | `64` | `R` |
| `Arg1` | `+ 0x58` | `64` | `R` |
| `Arg1` | `+ 0x60` | `64` | `R` |
| `Arg1` | `+ 0x68` | `64` | `R` |
| `Arg1` | `+ 0x70` | `8` | `R` |
| `Arg1` | `+ 0x70` | `32` | `R` |
| `Arg1` | `+ 0x70` | `64` | `R` |
| `Arg1` | `+ 0x78` | `32` | `R` |
| `Arg5` | `+ 0x0` | `16` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00884498&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
