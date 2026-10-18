# MiCreatePagingFileMap

- RVA: `0x009852F8`–`0x00985B67` (길이 `2,159` bytes)
- VA: `0x00000001409852F8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00097C0C`
- 디코드: `520`개 명령, `2,159/2,159` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **29**; 고유 호출 대상: **23**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0098533C` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0098537B` → [MiInitializeLargePfnList](../../text/43/MiInitializeLargePfnList_function_00432E70.md) (function, `0x00432E70`)
- `0x00985452` → [MiChargeCommit](../../text/28/MiChargeCommit_function_00286EB0.md) (function, `0x00286EB0`)
- `0x009854A0` → [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) (function, `0x0035B540`)
- `0x009854C1` → [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) (function, `0x0035B540`)
- `0x00985575` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00985664` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0098567F` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x00985698` → [MiUpdateControlAreaCommitCount](../../text/45/MiUpdateControlAreaCommitCount_function_004588E8.md) (function, `0x004588E8`)
- `0x009856B7` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x009856DD` → [KiCheckForKernelApcDelivery](../../text/2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (function, `0x002E2C80`)
- `0x00985703` → [MiInitializePrototypePtes](MiInitializePrototypePtes_function_009829AC.md) (function, `0x009829AC`)
- `0x0098570E` → [MiUpdateSystemProtoPtesTree](../../text/29/MiUpdateSystemProtoPtesTree_function_00295F0C.md) (function, `0x00295F0C`)
- `0x00985763` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x009857D9` → [Mi4KStartForSubsection](../../text/46/Mi4KStartForSubsection_function_0046C358.md) (function, `0x0046C358`)
- `0x00985806` → [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) (function, `0x0035B540`)
- `0x009858A6` → [MiChargeResident](../../text/28/MiChargeResident_function_0028A0F0.md) (function, `0x0028A0F0`)
- `0x009858BD` → [MiFreeLargeZeroPages](../../text/3B/MiFreeLargeZeroPages_function_003B5F0C.md) (function, `0x003B5F0C`)
- `0x009858D3` → [MiReturnResident](../../text/28/MiReturnResident_function_00286890.md) (function, `0x00286890`)
- `0x00985912` → [MmLockPreChargedPagedPool](../AD/MmLockPreChargedPagedPool_function_00AD6E20.md) (function, `0x00AD6E20`)
- `0x00985941` → [MiUpdateSystemProtoPtesTree](../../text/29/MiUpdateSystemProtoPtesTree_function_00295F0C.md) (function, `0x00295F0C`)
- `0x009859B4` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x009859D9` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x00985A25` → [MiValidateUserPhysicalExternalFlags](../80/MiValidateUserPhysicalExternalFlags_function_0080AE88.md) (function, `0x0080AE88`)
- `0x00985AA7` → [MiThreadIdealNode](../../text/3D/MiThreadIdealNode_function_003D3480.md) (function, `0x003D3480`)
- `0x00985AF3` → [MmObtainChargesToLockPagedPool](../7F/MmObtainChargesToLockPagedPool_function_007FE390.md) (function, `0x007FE390`)
- `0x00985B05` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00985B4E` → [MiLogSectionCreate](../7F/MiLogSectionCreate_function_007FCDEC.md) (function, `0x007FCDEC`)
- `0x00985B5D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [MmCreateSectionEx](MmCreateSectionEx_function_009839CC.md) at `0x00983BE5`
- [MmCreateCacheManagerSection](MmCreateCacheManagerSection_function_00983CB8.md) at `0x00983E16`
- [MiCreateSection](MiCreateSection_function_00983EC0.md) at `0x00984080`

### Static image references
- `0x0098531E` → RVA `0x00E0A740` (`.data`; read)
- `0x0098542C` → RVA `0x00E38D00` (`.data`; read)
- `0x00985747` → RVA `0x00FC6B04` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **24**
  - `0x0098533C` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x0098537B` → [MiInitializeLargePfnList](../../text/43/MiInitializeLargePfnList_function_00432E70.md) (`PAGE` → `.text`)
  - `0x00985452` → [MiChargeCommit](../../text/28/MiChargeCommit_function_00286EB0.md) (`PAGE` → `.text`)
  - `0x009854A0` → [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) (`PAGE` → `.text`)
  - `0x009854C1` → [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) (`PAGE` → `.text`)
  - `0x00985575` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00985664` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0098567F` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x00985698` → [MiUpdateControlAreaCommitCount](../../text/45/MiUpdateControlAreaCommitCount_function_004588E8.md) (`PAGE` → `.text`)
  - `0x009856B7` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x009856DD` → [KiCheckForKernelApcDelivery](../../text/2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (`PAGE` → `.text`)
  - `0x0098570E` → [MiUpdateSystemProtoPtesTree](../../text/29/MiUpdateSystemProtoPtesTree_function_00295F0C.md) (`PAGE` → `.text`)
  - `0x00985763` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x009857D9` → [Mi4KStartForSubsection](../../text/46/Mi4KStartForSubsection_function_0046C358.md) (`PAGE` → `.text`)
  - `0x00985806` → [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) (`PAGE` → `.text`)
  - `0x009858A6` → [MiChargeResident](../../text/28/MiChargeResident_function_0028A0F0.md) (`PAGE` → `.text`)
  - `0x009858BD` → [MiFreeLargeZeroPages](../../text/3B/MiFreeLargeZeroPages_function_003B5F0C.md) (`PAGE` → `.text`)
  - `0x009858D3` → [MiReturnResident](../../text/28/MiReturnResident_function_00286890.md) (`PAGE` → `.text`)
  - `0x00985941` → [MiUpdateSystemProtoPtesTree](../../text/29/MiUpdateSystemProtoPtesTree_function_00295F0C.md) (`PAGE` → `.text`)
  - `0x009859B4` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x009859D9` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x00985AA7` → [MiThreadIdealNode](../../text/3D/MiThreadIdealNode_function_003D3480.md) (`PAGE` → `.text`)
  - `0x00985B05` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00985B5D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **12**
  - `0x009858C7` → [sub_00B2AD32 + 0x247](../B2/Unknown_function_00B2AD32.md) (`tail-transfer`)
  - `0x009858D9` → [sub_00B2AD32 + 0x247](../B2/Unknown_function_00B2AD32.md) (`tail-transfer`)
  - `0x00985A2C` → [sub_00B2AD32 + 0xA](../B2/Unknown_function_00B2AD32.md) (`tail-transfer`)
  - `0x00985A3A` → [sub_00B2AD32](../B2/Unknown_function_00B2AD32.md) (`tail-transfer`)
  - `0x00985A54` → [sub_00B2AD32 + 0x14](../B2/Unknown_function_00B2AD32.md) (`tail-transfer`)
  - `0x00985A9D` → [sub_00B2AD32 + 0x3C](../B2/Unknown_function_00B2AD32.md) (`tail-transfer`)
  - `0x00985AAD` → [sub_00B2AD32 + 0x3E](../B2/Unknown_function_00B2AD32.md) (`tail-transfer`)
  - `0x00985ADD` → [sub_00B2AD32 + 0xF2](../B2/Unknown_function_00B2AD32.md) (`tail-transfer`)
  - `0x00985AE7` → [sub_00B2AD32 + 0x10A](../B2/Unknown_function_00B2AD32.md) (`tail-transfer`)
  - `0x00985B12` → [sub_00B2AD32 + 0x22E](../B2/Unknown_function_00B2AD32.md) (`tail-transfer`)
  - `0x00985B25` → [sub_00B2AD32 + 0x1F6](../B2/Unknown_function_00B2AD32.md) (`tail-transfer`)
  - `0x00985B44` → [sub_00B2AD32 + 0x16A](../B2/Unknown_function_00B2AD32.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
009852F8  48 8B C4                        mov rax, rsp
009852FB  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
009852FF  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
00985303  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
00985307  55                              push rbp
00985308  41 54                           push r12
0098530A  41 55                           push r13
0098530C  41 56                           push r14
0098530E  41 57                           push r15
00985310  48 8D A8 28 FF FF FF            lea rbp, [rax - 0xd8]
00985317  48 81 EC B0 01 00 00            sub rsp, 0x1b0
0098531E  48 8B 05 1B 54 48 00            mov rax, qword ptr [rip + 0x48541b]
00985325  48 33 C4                        xor rax, rsp
00985328  48 89 85 A0 00 00 00            mov qword ptr [rbp + 0xa0], rax
0098532F  33 D2                           xor edx, edx
00985331  4C 8B F1                        mov r14, rcx
00985334  48 8D 4D 40                     lea rcx, [rbp + 0x40]
00985338  44 8D 42 60                     lea r8d, [rdx + 0x60]
0098533C  E8 FF 18 D4 FF                  call 0x1406c6c40
00985341  41 8B 5E 10                     mov ebx, dword ptr [r14 + 0x10]
00985345  33 C0                           xor eax, eax
00985347  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
0098534B  0F 57 C0                        xorps xmm0, xmm0
0098534E  0F 29 45 D0                     movaps xmmword ptr [rbp - 0x30], xmm0
00985352  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
00985356  48 89 45 30                     mov qword ptr [rbp + 0x30], rax
0098535A  89 45 38                        mov dword ptr [rbp + 0x38], eax
0098535D  89 5C 24 58                     mov dword ptr [rsp + 0x58], ebx
00985361  0F 11 45 00                     movups xmmword ptr [rbp], xmm0
00985365  0F 11 45 10                     movups xmmword ptr [rbp + 0x10], xmm0
00985369  0F 11 45 20                     movups xmmword ptr [rbp + 0x20], xmm0
0098536D  0F BA E3 18                     bt ebx, 0x18
00985371  0F 82 6C 06 00 00               jb 0x1409859e3
00985377  48 8D 4D 40                     lea rcx, [rbp + 0x40]
0098537B  E8 F0 DA AA FF                  call 0x140432e70
00985380  41 8A BE C0 00 00 00            mov dil, byte ptr [r14 + 0xc0]
00985387  B9 00 00 00 08                  mov ecx, 0x8000000
0098538C  40 88 7C 24 31                  mov byte ptr [rsp + 0x31], dil
00985391  40 84 FF                        test dil, dil
00985394  0F 85 89 06 00 00               jne 0x140985a23
0098539A  85 DB                           test ebx, ebx
0098539C  0F 88 A8 06 00 00               js 0x140985a4a
009853A2  0F BA E3 11                     bt ebx, 0x11
009853A6  0F 82 E0 04 00 00               jb 0x14098588c
009853AC  4D 8B A6 98 00 00 00            mov r12, qword ptr [r14 + 0x98]
009853B3  BE 01 00 00 00                  mov esi, 1
009853B8  40 84 FF                        test dil, dil
009853BB  0F 85 AE 04 00 00               jne 0x14098586f
009853C1  4D 85 E4                        test r12, r12
009853C4  0F 84 A3 06 00 00               je 0x140985a6d
009853CA  8B D3                           mov edx, ebx
009853CC  23 D1                           and edx, ecx
009853CE  8B C2                           mov eax, edx
009853D0  F7 D8                           neg eax
009853D2  48 B8 00 10 00 FF FF 0F 00 00   movabs rax, 0xfffff001000
009853DC  48 1B C9                        sbb rcx, rcx
009853DF  48 23 C8                        and rcx, rax
009853E2  48 81 C1 00 F0 FF FF            add rcx, -0x1000
009853E9  4C 3B E1                        cmp r12, rcx
009853EC  0F 87 67 06 00 00               ja 0x140985a59
009853F2  49 81 C4 FF 0F 00 00            add r12, 0xfff
009853F9  49 C1 EC 0C                     shr r12, 0xc
009853FD  48 83 65 90 00                  and qword ptr [rbp - 0x70], 0
00985402  33 C0                           xor eax, eax
00985404  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00985409  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00985412  4D 8B AE B0 00 00 00            mov r13, qword ptr [r14 + 0xb0]
00985419  C6 44 24 30 00                  mov byte ptr [rsp + 0x30], 0
0098541E  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00985423  4D 85 ED                        test r13, r13
00985426  0F 85 CD 05 00 00               jne 0x1409859f9
0098542C  4C 8D 2D CD 38 4B 00            lea r13, [rip + 0x4b38cd]
00985433  85 D2                           test edx, edx
00985435  74 30                           je 0x140985467
00985437  0F BA E3 13                     bt ebx, 0x13
0098543B  0F 82 22 06 00 00               jb 0x140985a63
00985441  85 DB                           test ebx, ebx
00985443  0F 88 2E 06 00 00               js 0x140985a77
00985449  45 33 C0                        xor r8d, r8d
0098544C  49 8B D4                        mov rdx, r12
0098544F  49 8B CD                        mov rcx, r13
00985452  E8 59 1A 90 FF                  call 0x140286eb0
00985457  85 C0                           test eax, eax
00985459  0F 84 26 06 00 00               je 0x140985a85
0098545F  85 DB                           test ebx, ebx
00985461  0F 88 36 04 00 00               js 0x14098589d
00985467  33 C0                           xor eax, eax
00985469  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0098546E  8B C3                           mov eax, ebx
00985470  25 00 00 00 88                  and eax, 0x88000000
00985475  3D 00 00 00 08                  cmp eax, 0x8000000
0098547A  0F 85 FA 04 00 00               jne 0x14098597a
00985480  4C 89 64 24 78                  mov qword ptr [rsp + 0x78], r12
00985485  48 8B C6                        mov rax, rsi
00985488  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0098548D  48 6B D0 58                     imul rdx, rax, 0x58
00985491  B9 40 00 00 00                  mov ecx, 0x40
00985496  41 B8 4D 6D 43 61               mov r8d, 0x61436d4d
0098549C  48 83 EA 80                     sub rdx, -0x80
009854A0  E8 9B 60 9D FF                  call 0x14035b540
009854A5  48 8B F0                        mov rsi, rax
009854A8  48 85 C0                        test rax, rax
009854AB  0F 84 11 05 00 00               je 0x1409859c2
009854B1  BA 50 00 00 00                  mov edx, 0x50
009854B6  B9 00 01 00 00                  mov ecx, 0x100
009854BB  41 B8 4D 53 65 67               mov r8d, 0x6765534d
009854C1  E8 7A 60 9D FF                  call 0x14035b540
009854C6  4C 8B F8                        mov r15, rax
009854C9  48 85 C0                        test rax, rax
009854CC  0F 84 38 06 00 00               je 0x140985b0a
009854D2  48 83 60 48 00                  and qword ptr [rax + 0x48], 0
009854D7  B8 FF 03 00 00                  mov eax, 0x3ff
009854DC  0F B7 4E 3C                     movzx ecx, word ptr [rsi + 0x3c]
009854E0  48 8B 7C 24 38                  mov rdi, qword ptr [rsp + 0x38]
009854E5  0F B7 D1                        movzx edx, cx
009854E8  66 41 33 55 00                  xor dx, word ptr [r13]
009854ED  66 23 D0                        and dx, ax
009854F0  89 7E 60                        mov dword ptr [rsi + 0x60], edi
009854F3  48 8D 46 08                     lea rax, [rsi + 8]
009854F7  4C 89 3E                        mov qword ptr [rsi], r15
009854FA  66 33 D1                        xor dx, cx
009854FD  66 89 56 3C                     mov word ptr [rsi + 0x3c], dx
00985501  48 89 40 08                     mov qword ptr [rax + 8], rax
00985505  48 89 00                        mov qword ptr [rax], rax
00985508  B8 01 00 00 00                  mov eax, 1
0098550D  48 89 46 70                     mov qword ptr [rsi + 0x70], rax
00985511  48 89 46 18                     mov qword ptr [rsi + 0x18], rax
00985515  48 89 46 30                     mov qword ptr [rsi + 0x30], rax
00985519  0F BA E3 15                     bt ebx, 0x15
0098551D  0F 82 8F 05 00 00               jb 0x140985ab2
00985523  B8 00 10 00 00                  mov eax, 0x1000
00985528  0F BA E3 1A                     bt ebx, 0x1a
0098552C  0F 82 52 03 00 00               jb 0x140985884
00985532  8B C3                           mov eax, ebx
00985534  B9 00 20 00 00                  mov ecx, 0x2000
00985539  25 00 00 00 08                  and eax, 0x8000000
0098553E  74 03                           je 0x140985543
00985540  09 4E 38                        or dword ptr [rsi + 0x38], ecx
00985543  0F BA E3 13                     bt ebx, 0x13
00985547  0F 82 6E 05 00 00               jb 0x140985abb
0098554D  41 8B 8E AC 00 00 00            mov ecx, dword ptr [r14 + 0xac]
00985554  33 D2                           xor edx, edx
00985556  8B 46 38                        mov eax, dword ptr [rsi + 0x38]
00985559  48 83 66 68 00                  and qword ptr [rsi + 0x68], 0
0098555E  C1 E1 14                        shl ecx, 0x14
00985561  33 C8                           xor ecx, eax
00985563  44 8D 42 48                     lea r8d, [rdx + 0x48]
00985567  81 E1 00 00 F0 07               and ecx, 0x7f00000
0098556D  33 C8                           xor ecx, eax
0098556F  89 4E 38                        mov dword ptr [rsi + 0x38], ecx
00985572  49 8B CF                        mov rcx, r15
00985575  E8 C6 16 D4 FF                  call 0x1406c6c40
0098557A  0F BA E3 1C                     bt ebx, 0x1c
0098557E  0F 82 41 05 00 00               jb 0x140985ac5
00985584  0F BA E3 1E                     bt ebx, 0x1e
00985588  0F 82 D2 02 00 00               jb 0x140985860
0098558E  41 8A 47 0E                     mov al, byte ptr [r15 + 0xe]
00985592  BA FF 03 00 00                  mov edx, 0x3ff
00985597  8A C8                           mov cl, al
00985599  41 32 4E 20                     xor cl, byte ptr [r14 + 0x20]
0098559D  80 E1 1F                        and cl, 0x1f
009855A0  32 C8                           xor cl, al
009855A2  41 88 4F 0E                     mov byte ptr [r15 + 0xe], cl
009855A6  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
009855AF  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
009855B6  8B 81 D0 01 00 00               mov eax, dword ptr [rcx + 0x1d0]
009855BC  49 8B CC                        mov rcx, r12
009855BF  48 C1 E9 20                     shr rcx, 0x20
009855C3  41 89 47 30                     mov dword ptr [r15 + 0x30], eax
009855C7  49 8B C4                        mov rax, r12
009855CA  48 C1 E0 0C                     shl rax, 0xc
009855CE  49 89 47 18                     mov qword ptr [r15 + 0x18], rax
009855D2  41 0F B7 47 0C                  movzx eax, word ptr [r15 + 0xc]
009855D7  66 33 C8                        xor cx, ax
009855DA  49 89 37                        mov qword ptr [r15], rsi
009855DD  66 23 CA                        and cx, dx
009855E0  45 89 67 08                     mov dword ptr [r15 + 8], r12d
009855E4  66 33 C8                        xor cx, ax
009855E7  80 7C 24 31 00                  cmp byte ptr [rsp + 0x31], 0
009855EC  66 41 89 4F 0C                  mov word ptr [r15 + 0xc], cx
009855F1  0F 85 D8 04 00 00               jne 0x140985acf
009855F7  33 C0                           xor eax, eax
009855F9  4C 89 64 24 60                  mov qword ptr [rsp + 0x60], r12
009855FE  45 33 D2                        xor r10d, r10d
00985601  4C 8D 86 80 00 00 00            lea r8, [rsi + 0x80]
00985608  44 8B DB                        mov r11d, ebx
0098560B  4D 8B C8                        mov r9, r8
0098560E  41 81 E3 00 00 00 08            and r11d, 0x8000000
00985615  8D 50 01                        lea edx, [rax + 1]
00985618  44 89 5C 24 34                  mov dword ptr [rsp + 0x34], r11d
0098561D  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
00985621  4C 89 44 24 40                  mov qword ptr [rsp + 0x40], r8
00985626  4C 89 55 80                     mov qword ptr [rbp - 0x80], r10
0098562A  48 3B C7                        cmp rax, rdi
0098562D  0F 82 57 01 00 00               jb 0x14098578a
00985633  49 83 61 10 00                  and qword ptr [r9 + 0x10], 0
00985638  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
0098563D  49 89 47 40                     mov qword ptr [r15 + 0x40], rax
00985641  0F BA E3 1B                     bt ebx, 0x1b
00985645  0F 83 25 03 00 00               jae 0x140985970
0098564B  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00985650  49 8D 7F 28                     lea rdi, [r15 + 0x28]
00985654  45 33 C0                        xor r8d, r8d
00985657  66 29 91 E6 01 00 00            sub word ptr [rcx + 0x1e6], dx
0098565E  33 D2                           xor edx, edx
00985660  48 8B CF                        mov rcx, rdi
00985663  90                              nop
00985664  E8 C7 AB 88 FF                  call 0x140210230
00985669  F0 48 0F BA 2F 00               lock bts qword ptr [rdi], 0
0098566F  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00985674  73 13                           jae 0x140985689
00985676  4C 8B C7                        mov r8, rdi
00985679  48 8B D0                        mov rdx, rax
0098567C  48 8B CF                        mov rcx, rdi
0098567F  E8 0C A6 88 FF                  call 0x14020fc90
00985684  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
00985689  48 85 C0                        test rax, rax
0098568C  74 04                           je 0x140985692
0098568E  C6 40 0A 01                     mov byte ptr [rax + 0xa], 1
00985692  49 8B D4                        mov rdx, r12
00985695  48 8B CE                        mov rcx, rsi
00985698  E8 4B 32 AD FF                  call 0x1404588e8
0098569D  48 83 C8 FF                     or rax, 0xffffffffffffffff
009856A1  49 8D 7F 28                     lea rdi, [r15 + 0x28]
009856A5  F0 48 0F C1 07                  lock xadd qword ptr [rdi], rax
009856AA  24 06                           and al, 6
009856AC  3C 02                           cmp al, 2
009856AE  0F 84 22 03 00 00               je 0x1409859d6
009856B4  48 8B CF                        mov rcx, rdi
009856B7  E8 44 BF 95 FF                  call 0x1402e1600
009856BC  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
009856C1  BA 01 00 00 00                  mov edx, 1
009856C6  90                              nop
009856C7  66 01 91 E6 01 00 00            add word ptr [rcx + 0x1e6], dx
009856CE  75 12                           jne 0x1409856e2
009856D0  48 8D 81 98 00 00 00            lea rax, [rcx + 0x98]
009856D7  90                              nop
009856D8  48 39 00                        cmp qword ptr [rax], rax
009856DB  74 05                           je 0x1409856e2
009856DD  E8 9E D5 95 FF                  call 0x1402e2c80
009856E2  48 8D BE 80 00 00 00            lea rdi, [rsi + 0x80]
009856E9  85 DB                           test ebx, ebx
009856EB  0F 88 ED 01 00 00               js 0x1409858de
009856F1  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
009856F5  BB 01 00 00 00                  mov ebx, 1
009856FA  44 8B CB                        mov r9d, ebx
009856FD  4C 8B C7                        mov r8, rdi
00985700  49 8B D4                        mov rdx, r12
00985703  E8 A4 D2 FF FF                  call 0x1409829ac
00985708  48 8D 4F 38                     lea rcx, [rdi + 0x38]
0098570C  8B D3                           mov edx, ebx
0098570E  E8 F9 07 91 FF                  call 0x140295f0c
00985713  49 89 76 40                     mov qword ptr [r14 + 0x40], rsi
00985717  48 8B C3                        mov rax, rbx
0098571A  F0 49 0F C1 85 D0 06 00 00      lock xadd qword ptr [r13 + 0x6d0], rax
00985723  48 03 C3                        add rax, rbx
00985726  48 3B C3                        cmp rax, rbx
00985729  0F 8E BE 02 00 00               jle 0x1409859ed
0098572F  41 83 0E 04                     or dword ptr [r14], 4
00985733  48 83 C9 FF                     or rcx, 0xffffffffffffffff
00985737  48 8B C1                        mov rax, rcx
0098573A  F0 49 0F B1 4F 18               lock cmpxchg qword ptr [r15 + 0x18], rcx
00985740  49 89 86 80 00 00 00            mov qword ptr [r14 + 0x80], rax
00985747  F7 05 B3 13 64 00 01 00 40 00   test dword ptr [rip + 0x6413b3], 0x400001
00985751  0F 85 F2 03 00 00               jne 0x140985b49
00985757  33 C0                           xor eax, eax
00985759  48 8B 8D A0 00 00 00            mov rcx, qword ptr [rbp + 0xa0]
00985760  48 33 CC                        xor rcx, rsp
00985763  E8 D8 6E D2 FF                  call 0x1406ac640
00985768  4C 8D 9C 24 B0 01 00 00         lea r11, [rsp + 0x1b0]
00985770  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
00985774  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
00985778  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
0098577C  49 8B E3                        mov rsp, r11
0098577F  41 5F                           pop r15
00985781  41 5E                           pop r14
00985783  41 5D                           pop r13
00985785  41 5C                           pop r12
00985787  5D                              pop rbp
00985788  C3                              ret
00985789  CC                              int3
0098578A  49 8B 40 50                     mov rax, qword ptr [r8 + 0x50]
0098578E  4D 8B C8                        mov r9, r8
00985791  48 83 E0 F9                     and rax, 0xfffffffffffffff9
00985795  49 89 30                        mov qword ptr [r8], rsi
00985798  48 0B C2                        or rax, rdx
0098579B  4C 89 44 24 70                  mov qword ptr [rsp + 0x70], r8
009857A0  49 89 40 50                     mov qword ptr [r8 + 0x50], rax
009857A4  41 8B 40 20                     mov eax, dword ptr [r8 + 0x20]
009857A8  41 0F B7 4E 20                  movzx ecx, word ptr [r14 + 0x20]
009857AD  03 C9                           add ecx, ecx
009857AF  8B D1                           mov edx, ecx
009857B1  33 D0                           xor edx, eax
009857B3  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
009857B8  83 E2 C1                        and edx, 0xffffffc1
009857BB  48 8B F8                        mov rdi, rax
009857BE  33 D1                           xor edx, ecx
009857C0  49 8B C8                        mov rcx, r8
009857C3  48 3B 44 24 78                  cmp rax, qword ptr [rsp + 0x78]
009857C8  41 89 50 20                     mov dword ptr [r8 + 0x20], edx
009857CC  49 8B D2                        mov rdx, r10
009857CF  48 0F 47 7C 24 78               cmova rdi, qword ptr [rsp + 0x78]
009857D5  41 89 78 2C                     mov dword ptr [r8 + 0x2c], edi
009857D9  E8 7A 6B AE FF                  call 0x14046c358
009857DE  48 29 7C 24 60                  sub qword ptr [rsp + 0x60], rdi
009857E3  48 8D 04 FD 00 00 00 00         lea rax, [rdi*8]
009857EB  48 89 45 98                     mov qword ptr [rbp - 0x68], rax
009857EF  45 85 DB                        test r11d, r11d
009857F2  0F 84 9E 00 00 00               je 0x140985896
009857F8  41 B8 4D 6D 53 74               mov r8d, 0x74536d4d
009857FE  48 8B D0                        mov rdx, rax
00985801  B9 12 01 00 00                  mov ecx, 0x112
00985806  E8 35 5D 9D FF                  call 0x14035b540
0098580B  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00985810  48 8B F8                        mov rdi, rax
00985813  48 85 C0                        test rax, rax
00985816  0F 84 EE 02 00 00               je 0x140985b0a
0098581C  85 DB                           test ebx, ebx
0098581E  0F 88 C8 02 00 00               js 0x140985aec
00985824  4C 8B 44 24 40                  mov r8, qword ptr [rsp + 0x40]
00985829  4C 8B 4C 24 70                  mov r9, qword ptr [rsp + 0x70]
0098582E  4C 8B 55 80                     mov r10, qword ptr [rbp - 0x80]
00985832  44 8B 5C 24 34                  mov r11d, dword ptr [rsp + 0x34]
00985837  49 89 78 08                     mov qword ptr [r8 + 8], rdi
0098583B  41 8B 40 2C                     mov eax, dword ptr [r8 + 0x2c]
0098583F  BA 01 00 00 00                  mov edx, 1
00985844  48 8B 7C 24 38                  mov rdi, qword ptr [rsp + 0x38]
00985849  4C 03 D0                        add r10, rax
0098584C  48 8B 45 88                     mov rax, qword ptr [rbp - 0x78]
00985850  49 83 C0 58                     add r8, 0x58
00985854  48 03 C2                        add rax, rdx
00985857  4D 89 41 10                     mov qword ptr [r9 + 0x10], r8
0098585B  E9 BD FD FF FF                  jmp 0x14098561d
00985860  B8 00 10 00 00                  mov eax, 0x1000
00985865  66 41 09 47 0C                  or word ptr [r15 + 0xc], ax
0098586A  E9 1F FD FF FF                  jmp 0x14098558e
0098586F  4D 85 E4                        test r12, r12
00985872  0F 85 F5 01 00 00               jne 0x140985a6d
00985878  8B D3                           mov edx, ebx
0098587A  4C 8B E6                        mov r12, rsi
0098587D  23 D1                           and edx, ecx
0098587F  E9 79 FB FF FF                  jmp 0x1409853fd
00985884  09 46 38                        or dword ptr [rsi + 0x38], eax
00985887  E9 A6 FC FF FF                  jmp 0x140985532
0098588C  B8 F4 00 00 C0                  mov eax, 0xc00000f4
00985891  E9 C3 FE FF FF                  jmp 0x140985759
00985896  4C 8B 44 24 40                  mov r8, qword ptr [rsp + 0x40]
0098589B  EB 9E                           jmp 0x14098583b
0098589D  45 33 C0                        xor r8d, r8d
009858A0  49 8B D4                        mov rdx, r12
009858A3  49 8B CD                        mov rcx, r13
009858A6  E8 45 48 90 FF                  call 0x14028a0f0
009858AB  85 C0                           test eax, eax
009858AD  0F 85 DC 01 00 00               jne 0x140985a8f
009858B3  45 33 C0                        xor r8d, r8d
009858B6  48 8D 55 40                     lea rdx, [rbp + 0x40]
009858BA  49 8B CD                        mov rcx, r13
009858BD  E8 4A 06 A3 FF                  call 0x1403b5f0c
009858C2  80 7C 24 30 00                  cmp byte ptr [rsp + 0x30], 0
009858C7  0F 84 AC 56 1A 00               je 0x140b2af79
009858CD  49 8B D4                        mov rdx, r12
009858D0  49 8B CD                        mov rcx, r13
009858D3  E8 B8 0F 90 FF                  call 0x140286890
009858D8  90                              nop
009858D9  E9 9B 56 1A 00                  jmp 0x140b2af79
009858DE  48 83 64 24 48 00               and qword ptr [rsp + 0x48], 0
009858E4  B8 00 04 00 00                  mov eax, 0x400
009858E9  66 41 09 47 0C                  or word ptr [r15 + 0xc], ax
009858EE  0F BA 6E 5C 10                  bts dword ptr [rsi + 0x5c], 0x10
009858F3  48 83 7C 24 38 00               cmp qword ptr [rsp + 0x38], 0
009858F9  76 75                           jbe 0x140985970
009858FB  48 8D 5F 30                     lea rbx, [rdi + 0x30]
009858FF  48 8B 7B D8                     mov rdi, qword ptr [rbx - 0x28]
00985903  8B 53 FC                        mov edx, dword ptr [rbx - 4]
00985906  48 8B CF                        mov rcx, rdi
00985909  48 C1 E2 03                     shl rdx, 3
0098590D  48 89 7C 24 40                  mov qword ptr [rsp + 0x40], rdi
00985912  E8 09 15 15 00                  call 0x140ad6e20
00985917  8B 03                           mov eax, dword ptr [rbx]
00985919  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
0098591E  25 FF FF FF 3F                  and eax, 0x3fffffff
00985923  0F BA E8 1E                     bts eax, 0x1e
00985927  89 03                           mov dword ptr [rbx], eax
00985929  48 85 C9                        test rcx, rcx
0098592C  0F 85 F8 01 00 00               jne 0x140985b2a
00985932  8B 4B FC                        mov ecx, dword ptr [rbx - 4]
00985935  33 C0                           xor eax, eax
00985937  F3 48 AB                        rep stosq qword ptr [rdi], rax
0098593A  8D 50 01                        lea edx, [rax + 1]
0098593D  48 8D 4B 08                     lea rcx, [rbx + 8]
00985941  E8 C6 05 91 FF                  call 0x140295f0c
00985946  45 33 E4                        xor r12d, r12d
00985949  4C 21 64 24 50                  and qword ptr [rsp + 0x50], r12
0098594E  44 39 63 FC                     cmp dword ptr [rbx - 4], r12d
00985952  0F 85 EA 01 00 00               jne 0x140985b42
00985958  4C 8B 64 24 48                  mov r12, qword ptr [rsp + 0x48]
0098595D  48 83 C3 58                     add rbx, 0x58
00985961  49 FF C4                        inc r12
00985964  4C 89 64 24 48                  mov qword ptr [rsp + 0x48], r12
00985969  4C 3B 64 24 38                  cmp r12, qword ptr [rsp + 0x38]
0098596E  72 8F                           jb 0x1409858ff
00985970  BB 01 00 00 00                  mov ebx, 1
00985975  E9 99 FD FF FF                  jmp 0x140985713
0098597A  8B FB                           mov edi, ebx
0098597C  B9 00 00 10 00                  mov ecx, 0x100000
00985981  C1 FF 1F                        sar edi, 0x1f
00985984  33 D2                           xor edx, edx
00985986  23 F9                           and edi, ecx
00985988  49 8B C4                        mov rax, r12
0098598B  03 F9                           add edi, ecx
0098598D  48 C1 EF 03                     shr rdi, 3
00985991  48 F7 F7                        div rdi
00985994  48 89 7C 24 78                  mov qword ptr [rsp + 0x78], rdi
00985999  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0098599E  48 85 D2                        test rdx, rdx
009859A1  0F 84 E6 FA FF FF               je 0x14098548d
009859A7  48 03 C6                        add rax, rsi
009859AA  E9 D9 FA FF FF                  jmp 0x140985488
009859AF  33 D2                           xor edx, edx
009859B1  48 8B CE                        mov rcx, rsi
009859B4  E8 B7 CE 1F 00                  call 0x140b82870
009859B9  4D 85 FF                        test r15, r15
009859BC  0F 85 96 01 00 00               jne 0x140985b58
009859C2  0F BA E3 1B                     bt ebx, 0x1b
009859C6  0F 82 E7 FE FF FF               jb 0x1409858b3
009859CC  B8 9A 00 00 C0                  mov eax, 0xc000009a
009859D1  E9 83 FD FF FF                  jmp 0x140985759
009859D6  48 8B CF                        mov rcx, rdi
009859D9  E8 F2 03 8E FF                  call 0x140265dd0
009859DE  E9 D1 FC FF FF                  jmp 0x1409856b4
009859E3  B8 20 00 00 C0                  mov eax, 0xc0000020
009859E8  E9 6C FD FF FF                  jmp 0x140985759
009859ED  B9 0E 00 00 00                  mov ecx, 0xe
009859F2  CD 29                           int 0x29
009859F4  E9 36 FD FF FF                  jmp 0x14098572f
009859F9  4D 8B 6D 00                     mov r13, qword ptr [r13]
009859FD  48 8D 05 FC 32 4B 00            lea rax, [rip + 0x4b32fc]
00985A04  4C 3B E8                        cmp r13, rax
00985A07  0F 84 26 FA FF FF               je 0x140985433
00985A0D  41 8B 45 04                     mov eax, dword ptr [r13 + 4]
00985A11  84 C0                           test al, al
00985A13  0F 89 1A FA FF FF               jns 0x140985433
00985A19  B8 BB 00 00 C0                  mov eax, 0xc00000bb
00985A1E  E9 36 FD FF FF                  jmp 0x140985759
00985A23  8B CB                           mov ecx, ebx
00985A25  E8 5E 54 E8 FF                  call 0x14080ae88
00985A2A  85 C0                           test eax, eax
00985A2C  0F 88 0A 53 1A 00               js 0x140b2ad3c
00985A32  41 8B 46 1C                     mov eax, dword ptr [r14 + 0x1c]
00985A36  24 07                           and al, 7
00985A38  3C 04                           cmp al, 4
00985A3A  0F 84 F2 52 1A 00               je 0x140b2ad32
00985A40  B8 45 00 00 C0                  mov eax, 0xc0000045
00985A45  E9 0F FD FF FF                  jmp 0x140985759
00985A4A  8B C3                           mov eax, ebx
00985A4C  23 C1                           and eax, ecx
00985A4E  0F 84 38 FE FF FF               je 0x14098588c
00985A54  E9 ED 52 1A 00                  jmp 0x140b2ad46
00985A59  B8 40 00 00 C0                  mov eax, 0xc0000040
00985A5E  E9 F6 FC FF FF                  jmp 0x140985759
00985A63  41 F6 C4 0F                     test r12b, 0xf
00985A67  0F 84 D4 F9 FF FF               je 0x140985441
00985A6D  B8 F2 00 00 C0                  mov eax, 0xc00000f2
00985A72  E9 E2 FC FF FF                  jmp 0x140985759
00985A77  49 F7 C4 FF 01 00 00            test r12, 0x1ff
00985A7E  75 ED                           jne 0x140985a6d
00985A80  E9 C4 F9 FF FF                  jmp 0x140985449
00985A85  B8 2D 01 00 C0                  mov eax, 0xc000012d
00985A8A  E9 CA FC FF FF                  jmp 0x140985759
00985A8F  41 8B 86 AC 00 00 00            mov eax, dword ptr [r14 + 0xac]
00985A96  40 88 74 24 30                  mov byte ptr [rsp + 0x30], sil
00985A9B  85 C0                           test eax, eax
00985A9D  0F 85 CB 52 1A 00               jne 0x140b2ad6e
00985AA3  33 D2                           xor edx, edx
00985AA5  33 C9                           xor ecx, ecx
00985AA7  E8 D4 D9 A4 FF                  call 0x1403d3480
00985AAC  90                              nop
00985AAD  E9 BE 52 1A 00                  jmp 0x140b2ad70
00985AB2  83 4E 38 40                     or dword ptr [rsi + 0x38], 0x40
00985AB6  E9 68 FA FF FF                  jmp 0x140985523
00985ABB  0F BA 6E 38 1F                  bts dword ptr [rsi + 0x38], 0x1f
00985AC0  E9 88 FA FF FF                  jmp 0x14098554d
00985AC5  B8 00 20 00 00                  mov eax, 0x2000
00985ACA  E9 96 FD FF FF                  jmp 0x140985865
00985ACF  41 8B 7E 10                     mov edi, dword ptr [r14 + 0x10]
00985AD3  41 B8 01 00 00 00               mov r8d, 1
00985AD9  0F BA E7 11                     bt edi, 0x11
00985ADD  0F 83 41 53 1A 00               jae 0x140b2ae24
00985AE3  41 8D 50 03                     lea edx, [r8 + 3]
00985AE7  E9 50 53 1A 00                  jmp 0x140b2ae3c
00985AEC  48 8B 55 98                     mov rdx, qword ptr [rbp - 0x68]
00985AF0  48 8B CF                        mov rcx, rdi
00985AF3  E8 98 88 E7 FF                  call 0x1407fe390
00985AF8  85 C0                           test eax, eax
00985AFA  0F 85 24 FD FF FF               jne 0x140985824
00985B00  33 D2                           xor edx, edx
00985B02  48 8B CF                        mov rcx, rdi
00985B05  E8 66 CD 1F 00                  call 0x140b82870
00985B0A  45 33 F6                        xor r14d, r14d
00985B0D  4C 39 74 24 38                  cmp qword ptr [rsp + 0x38], r14
00985B12  0F 86 48 54 1A 00               jbe 0x140b2af60
00985B18  81 E3 00 00 00 88               and ebx, 0x88000000
00985B1E  48 8D BE 88 00 00 00            lea rdi, [rsi + 0x88]
00985B25  E9 FE 53 1A 00                  jmp 0x140b2af28
00985B2A  48 FF C9                        dec rcx
00985B2D  25 FF FF FF 3F                  and eax, 0x3fffffff
00985B32  0F BA E8 1F                     bts eax, 0x1f
00985B36  48 89 4C 24 68                  mov qword ptr [rsp + 0x68], rcx
00985B3B  89 03                           mov dword ptr [rbx], eax
00985B3D  E9 F0 FD FF FF                  jmp 0x140985932
00985B42  33 C0                           xor eax, eax
00985B44  E9 53 53 1A 00                  jmp 0x140b2ae9c
00985B49  8B D3                           mov edx, ebx
00985B4B  48 8B CE                        mov rcx, rsi
00985B4E  E8 99 72 E7 FF                  call 0x1407fcdec
00985B53  E9 FF FB FF FF                  jmp 0x140985757
00985B58  33 D2                           xor edx, edx
00985B5A  49 8B CF                        mov rcx, r15
00985B5D  E8 0E CD 1F 00                  call 0x140b82870
00985B62  E9 5B FE FF FF                  jmp 0x1409859c2
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiCreatePagingFileMap(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m150;
    unsigned __int64 v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned int v_stack_m17C;
    unsigned int v_stack_m180;
    unsigned __int64 v_stack_m188;
    unsigned __int64 v_stack_m190;
    unsigned __int64 v_stack_m198;
    unsigned __int64 v_stack_m1A0;
    unsigned int v_stack_m1A4;
    unsigned __int8 v_stack_m1A7;
    unsigned __int8 v_stack_m1A8;
    unsigned __int64 v_stack_m28;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (432);
    result = (*(unsigned __int64 *)(v_rip + 4740123)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 216 + 160) = result;
    a2 = 0;
    result = memset(v_rsp - 216 + 64, a2, a2 + 96, a4);
    result = 0;
    *(unsigned __int64 *)(v_rsp - 216 - 96) = 0;
    *(unsigned __int64 *)(v_rsp - 216 - 48) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 216 - 24) = 0;
    *(unsigned __int64 *)(v_rsp - 216 + 48) = 0;
    *(unsigned int *)(v_rsp - 216 + 56) = 0;
    v_stack_m180 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 16)));
    *(unsigned __int64 *)(v_rsp - 216) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 216 + 16) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 216 + 32) = v_xmm0;
    if (condition_is_below) goto loc_009859E3;
    result = MiInitializeLargePfnList(v_rsp - 216 + 64, a2, a2 + 96, a4);
    v_stack_m1A7 = (unsigned __int8)(*(unsigned __int8 *)(a1 + 192));
    if ((unsigned __int8)(*(unsigned __int8 *)(a1 + 192)) != 0) goto loc_00985A23;
    if (sign_flag) goto loc_00985A4A;
    if (condition_is_below) goto loc_0098588C;
    if ((unsigned __int8)(*(unsigned __int8 *)(a1 + 192)) != 0) goto loc_0098586F;
    if (*(unsigned __int64 *)(a1 + 152) == 0) goto loc_00985A6D;
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 16))))) & ((unsigned int)((unsigned int)(0x8000000ULL))));
    result = (unsigned int)(-((unsigned int)(a2)));
    a1 = ((unsigned int)(0x8000000ULL)) & (result);
    a1 = (a1) + (0xFFFFFFFFFFFFF000ULL);
    if ((*(unsigned __int64 *)(a1 + 152)) > a1) goto loc_00985A59;
    v_r12 = (*(unsigned __int64 *)(a1 + 152)) + (0xFFFULL);
    v_r12 = (v_r12) >> (12);
loc_009853FD:
    result = 0;
    v_stack_m170 = 0;
    v_stack_m1A8 = 0;
    v_stack_m188 = *(unsigned __int64 *)(gs_base + (0 + 392));
    if (*(unsigned __int64 *)(a1 + 176) != 0) goto loc_009859F9;
loc_00985433:
    if (a2 == 0) goto loc_00985467;
    if (condition_is_below) goto loc_00985A63;
loc_00985441:
    if (sign_flag) goto loc_00985A77;
loc_00985449:
    a3 = 0;
    result = MiChargeCommit(v_rip + 4929741, v_r12, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_00985A85;
    if (sign_flag) goto loc_0098589D;
loc_00985467:
    result = 0;
    v_stack_m190 = 0;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 16))))) & (0x88000000ULL));
    if (((unsigned int)(result)) != 0x8000000ULL) goto loc_0098597A;
    v_stack_m160 = v_r12;
loc_00985488:
    v_stack_m1A0 = 1;
loc_0098548D:
    a2 = (v_r12) * (1);
    a2 = (a2) - (-128);
    result = MiAllocatePool(64, a2, (unsigned int)(0x61436D4DULL), a4);
    if (result == 0) goto loc_009859C2;
    result = MiAllocatePool(256, 80, (unsigned int)(0x6765534DULL), a4);
    if (result == 0) goto loc_00985B0A;
    a2 = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(result + 60))) ^ (*(unsigned __int16 *)(v_rip + 4929741)));
    a2 = (unsigned __int16)((a2) & ((unsigned __int16)((unsigned int)(0x3FFULL))));
    *(unsigned int *)(result + 96) = (unsigned int)(v_stack_m1A0);
    *(unsigned __int64 *)(result) = result;
    a2 = (unsigned __int16)((a2) ^ ((unsigned __int16)(*(unsigned __int16 *)(result + 60))));
    *(unsigned __int16 *)(result + 60) = (unsigned __int16)(a2);
    *(unsigned __int64 *)(result + 8 + 8) = result + 8;
    *(unsigned __int64 *)(result + 8) = result + 8;
    *(unsigned __int64 *)(result + 112) = 1;
    *(unsigned __int64 *)(result + 24) = 1;
    *(unsigned __int64 *)(result + 48) = 1;
    if (condition_is_below) goto loc_00985AB2;
loc_00985523:
    if (condition_is_below) goto loc_00985884;
loc_00985532:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 16))))) & (0x8000000ULL));
    if (!(condition_is_equal)) {
    }
    if (condition_is_below) goto loc_00985ABB;
loc_0098554D:
    a2 = 0;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 172))) << (20));
    a1 = (unsigned int)((a1) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(result + 56)))));
    a1 = (unsigned int)((a1) & (0x7F00000ULL));
    a1 = (unsigned int)((a1) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(result + 56)))));
    *(unsigned int *)(result + 56) = (unsigned int)(a1);
    result = memset(result, a2, a2 + 72, a4);
    if (condition_is_below) goto loc_00985AC5;
    if (condition_is_below) goto loc_00985860;
loc_0098558E:
    a1 = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(result + 14))) ^ (*(unsigned __int8 *)(a1 + 32)));
    a1 = (unsigned __int8)((a1) & (31));
    a1 = (unsigned __int8)((a1) ^ ((unsigned __int8)(*(unsigned __int8 *)(result + 14))));
    *(unsigned __int8 *)(result + 14) = (unsigned __int8)(a1);
    a1 = (v_r12) >> (32);
    *(unsigned int *)(result + 48) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 464)));
    result = (v_r12) << (12);
    *(unsigned __int64 *)(result + 24) = result;
    a1 = (unsigned __int16)((a1) ^ ((unsigned __int16)(*(unsigned __int16 *)(result + 12))));
    *(unsigned __int64 *)(result) = result;
    a1 = (unsigned __int16)((a1) & ((unsigned __int16)((unsigned int)(0x3FFULL))));
    *(unsigned int *)(result + 8) = (unsigned int)(v_r12);
    a1 = (unsigned __int16)((a1) ^ ((unsigned __int16)(*(unsigned __int16 *)(result + 12))));
    *(unsigned __int16 *)(result + 12) = (unsigned __int16)(a1);
    if (v_stack_m1A7 != 0) goto loc_00985ACF;
    result = 0;
    v_stack_m178 = v_r12;
    v_r10 = 0;
    v_r11 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 16))))) & (0x8000000ULL));
    v_stack_m1A4 = (unsigned int)(v_r11);
loc_0098561D:
    *(unsigned __int64 *)(v_rsp - 216 - 120) = 0;
    v_stack_m198 = result + 128;
    *(unsigned __int64 *)(v_rsp - 216 - 128) = 0;
    if (0 < v_stack_m1A0) goto loc_0098578A;
    *(unsigned __int64 *)(result + 64) = v_stack_m190;
    if (0 >= v_stack_m1A0) goto loc_00985970;
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(result + 40, a2, a3, result + 128);
    v_stack_m168 = result;
    if (!(condition_is_above_or_equal)) {
        a3 = result + 40;
        a2 = result;
        a1 = result + 40;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, result + 128);
        result = v_stack_m168;
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    result = MiUpdateControlAreaCommitCount(result, v_r12, a3, result + 128);
    result = (result) | (-1);
    result = (unsigned __int8)((result) & (6));
    if (((unsigned __int8)(result)) == 2) goto loc_009859D6;
loc_009856B4:
    result = KeAbPostRelease(result + 40, v_r12, a3, result + 128);
    if (((unsigned __int8)(result)) != 2) goto loc_009856E2;
    result = v_stack_m188 + 152;
    if ((*(unsigned __int64 *)(v_stack_m188 + 152)) != (v_stack_m188 + 152)) {
        result = KiCheckForKernelApcDelivery(v_stack_m188, 1, a3, result + 128);
    }
    if (sign_flag) goto loc_009858DE;
    result = MiInitializePrototypePtes(*(unsigned __int64 *)(result + 128 + 8), v_r12, result + 128, 1);
    result = MiUpdateSystemProtoPtesTree(result + 128 + 56, 1, result + 128, 1);
loc_00985713:
    *(unsigned __int64 *)(a1 + 64) = result;
    result = (1) + (1);
    if (result <= 1) goto loc_009859ED;
loc_0098572F:
    a1 = (result + 128 + 56) | (-1);
    *(unsigned __int64 *)(a1 + 128) = a1;
    if (((*(unsigned int *)(v_rip + 6558643)) & (0x400001ULL)) != 0) goto loc_00985B49;
loc_00985757:
    result = 0;
loc_00985759:
    a1 = (*(unsigned __int64 *)(v_rsp - 216 + 160)) ^ (v_rsp);
    result = _security_check_cookie(a1, 1, result + 128, 1);
    return result;
loc_0098578A:
    result = (*(unsigned __int64 *)(result + 128 + 80)) & (-7);
    *(unsigned __int64 *)(result + 128) = *(unsigned __int64 *)(v_stack_m28 + 64);
    result = (result) | (1);
    v_stack_m140 = result + 128;
    *(unsigned __int64 *)(result + 128 + 80) = result;
    a1 = (unsigned int)((*(unsigned __int16 *)(a1 + 32)) + ((unsigned int)(*(unsigned __int16 *)(a1 + 32))));
    a2 = (unsigned int)(((unsigned int)((unsigned int)(a1))) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(result + 128 + 32)))));
    a2 = (unsigned int)((a2) & (0xFFFFFFC1ULL));
    a2 = (unsigned int)((a2) ^ ((unsigned int)(a1)));
    *(unsigned int *)(result + 128 + 32) = a2;
    v_rdi = v_stack_m150;
    if (v_stack_m150 > v_stack_m138) { v_rdi = v_stack_m138; }
    *(unsigned int *)(result + 128 + 44) = (unsigned int)(v_rdi);
    result = Mi4KStartForSubsection(result + 128, 0, result + 128, result + 128);
    *(unsigned __int64 *)(v_rsp - 216 - 104) = v_rdi * 8;
    if ((unsigned int)(v_stack_m28) == 0) goto loc_00985896;
    result = MiAllocatePool(274, v_rdi * 8, (unsigned int)(0x74536D4DULL), result + 128);
    v_stack_m168 = result;
    if (result == 0) goto loc_00985B0A;
    if (sign_flag) goto loc_00985AEC;
loc_00985824:
    *(unsigned __int64 *)(v_stack_m170 + 8) = result;
loc_0098583B:
    v_r10 = (*(unsigned __int64 *)(v_rsp - 216 - 128)) + ((unsigned int)(*(unsigned int *)(v_stack_m170 + 44)));
    a3 = (v_stack_m170) + (88);
    result = (*(unsigned __int64 *)(v_rsp - 216 - 120)) + (1);
    *(unsigned __int64 *)(v_stack_m140 + 16) = a3;
    goto loc_0098561D;
loc_00985860:
loc_00985865:
    goto loc_0098558E;
loc_0098586F:
    if (v_r12 != 0) goto loc_00985A6D;
    a2 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 56)))) & (274));
    goto loc_009853FD;
loc_00985884:
    goto loc_00985532;
loc_0098588C:
    goto loc_00985759;
loc_00985896:
    goto loc_0098583B;
loc_0098589D:
    a3 = 0;
    result = MiChargeResident(v_rip + 4929741, *(unsigned __int64 *)(v_stack_m28 + 64), a3, v_stack_m140);
    if ((unsigned int)(result) != 0) goto loc_00985A8F;
loc_009858B3:
    a3 = 0;
    result = MiFreeLargeZeroPages(v_rip + 4929741, v_rsp - 216 + 64, a3, v_stack_m140);
    result = MiReturnResident(v_rip + 4929741, *(unsigned __int64 *)(v_stack_m28 + 64), a3, v_stack_m140);
loc_009858DE:
    if (v_stack_m178 <= 0) goto loc_00985970;
loc_009858FF:
    a2 = ((unsigned int)(*(unsigned int *)(v_stack_m178 + 48 - 4))) << (3);
    v_stack_m170 = *(unsigned __int64 *)(v_stack_m178 + 48 - 40);
    result = MmLockPreChargedPagedPool(*(unsigned __int64 *)(v_stack_m178 + 48 - 40), a2, a3, v_stack_m140);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m178 + 48))) & (0x3FFFFFFFULL));
    *(unsigned int *)(v_stack_m178 + 48) = (unsigned int)(result);
    if (v_stack_m148 != 0) goto loc_00985B2A;
loc_00985932:
    result = 0;
    result = MiUpdateSystemProtoPtesTree(v_stack_m178 + 48 + 8, result + 1, a3, v_stack_m140);
    v_r12 = 0;
    if ((*(unsigned int *)(v_stack_m178 + 48 - 4)) != 0) goto loc_00985B42;
    v_rbx = (v_stack_m178 + 48) + (88);
    v_r12 = (v_stack_m168) + 1;
    v_stack_m168 = v_r12;
    if (v_r12 < v_stack_m178) goto loc_009858FF;
loc_00985970:
    goto loc_00985713;
loc_0098597A:
    v_rdi = (unsigned int)((1) >> (31));
    a2 = 0;
    v_rdi = (unsigned int)((v_rdi) & ((unsigned int)((unsigned int)(0x100000ULL))));
    v_rdi = (unsigned int)((v_rdi) + ((unsigned int)((unsigned int)(0x100000ULL))));
    v_rdi = (v_rdi) >> (3);
    v_stack_m138 = v_rdi;
    v_stack_m178 = v_r12;
    if (0 == 0) goto loc_0098548D;
    result = (v_r12) + (*(unsigned __int64 *)(v_stack_m28 + 64));
    goto loc_00985488;
loc_009859C2:
    if (condition_is_below) goto loc_009858B3;
    goto loc_00985759;
loc_009859D6:
    result = ExfTryToWakePushLock(v_rdi, a2, a3, v_stack_m140);
    goto loc_009856B4;
loc_009859E3:
    goto loc_00985759;
loc_009859ED:
    goto loc_0098572F;
loc_009859F9:
    if ((*(unsigned __int64 *)(v_rip + 4929741)) == (v_rip + 4928252)) goto loc_00985433;
    if (!sign_flag) goto loc_00985433;
    goto loc_00985759;
loc_00985A23:
    result = MiValidateUserPhysicalExternalFlags(1, a2, a3, v_stack_m140);
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(a1 + 28))) & (7));
    goto loc_00985759;
loc_00985A4A:
    result = (unsigned int)((1) & (1));
    if (condition_is_equal) goto loc_0098588C;
loc_00985A59:
    goto loc_00985759;
loc_00985A63:
    if ((((unsigned __int8)(v_r12)) & (15)) == 0) goto loc_00985441;
loc_00985A6D:
    goto loc_00985759;
loc_00985A77:
    if (((v_r12) & (511)) != 0) goto loc_00985A6D;
    goto loc_00985449;
loc_00985A85:
    goto loc_00985759;
loc_00985A8F:
    v_stack_m180 = (unsigned __int8)(*(unsigned __int64 *)(v_stack_m28 + 64));
    a2 = 0;
    a1 = 0;
    result = MiThreadIdealNode(a1, a2, a3, v_stack_m140);
loc_00985AB2:
    goto loc_00985523;
loc_00985ABB:
    goto loc_0098554D;
loc_00985AC5:
    goto loc_00985865;
loc_00985ACF:
loc_00985AEC:
    result = MmObtainChargesToLockPagedPool((unsigned int)(*(unsigned int *)(a1 + 16)), *(unsigned __int64 *)(v_rsp - 216 - 104), 1, v_stack_m140);
    if ((unsigned int)(result) != 0) goto loc_00985824;
    a2 = 0;
    result = ExFreePoolWithTag((unsigned int)(*(unsigned int *)(a1 + 16)), a2, 1, v_stack_m140);
loc_00985B0A:
    v_r14 = 0;
    v_rbx = (unsigned int)((1) & (0x88000000ULL));
loc_00985B2A:
    a1 = ((unsigned int)(*(unsigned int *)(a1 + 16))) - 1;
    result = (unsigned int)((result) & (0x3FFFFFFFULL));
    v_stack_m148 = a1;
    *(unsigned int *)(v_rbx) = (unsigned int)(result);
    goto loc_00985932;
loc_00985B42:
    result = 0;
loc_00985B49:
    result = MiLogSectionCreate(*(unsigned __int64 *)(v_stack_m28 + 64), (unsigned int)((unsigned int)(v_rbx)), 1, v_stack_m140);
    goto loc_00985757;
}
```

## 5. (Beta) C Style

```c
int64_t MiCreatePagingFileMap(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint64_t v_stack_m148;
    uint64_t v_stack_m150;
    uint64_t v_stack_m160;
    uint64_t v_stack_m168;
    uint64_t v_stack_m170;
    uint64_t v_stack_m178;
    uint32_t v_stack_m17C;
    uint32_t v_stack_m180;
    uint64_t v_stack_m188;
    uint64_t v_stack_m190;
    uint64_t v_stack_m198;
    uint64_t v_stack_m1A0;
    uint32_t v_stack_m1A4;
    uint8_t v_stack_m1A7;
    uint8_t v_stack_m1A8;
    uint64_t v_stack_m28;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (432);
    result = (*(uint64_t *)(v_rip + 0x48541B)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0xD8 + 0xA0) = result;
    Arg2 = 0;
    result = memset(local_rsp - 216 + 64, Arg2, Arg2 + 96, a4);
    result = 0;
    *(uint64_t *)(local_rsp - 0xD8 - 0x60) = 0;
    *(uint64_t *)(local_rsp - 0xD8 - 0x30) = v_xmm0;
    *(uint64_t *)(local_rsp - 0xD8 - 0x18) = 0;
    *(uint64_t *)(local_rsp - 0xD8 + 0x30) = 0;
    *(uint32_t *)(local_rsp - 0xD8 + 0x38) = 0;
    v_stack_m180 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x10)));
    *(uint64_t *)(local_rsp - 0xD8) = v_xmm0;
    *(uint64_t *)(local_rsp - 0xD8 + 0x10) = v_xmm0;
    *(uint64_t *)(local_rsp - 0xD8 + 0x20) = v_xmm0;
    if (condition_is_below) goto loc_009859E3;
    result = MiInitializeLargePfnList(local_rsp - 216 + 64, Arg2, Arg2 + 96, a4);
    v_stack_m1A7 = (uint8_t)(*(uint8_t *)(arg1 + 0xC0));
    if ((uint8_t)(*(uint8_t *)(arg1 + 0xC0)) != 0) goto loc_00985A23;
    if (sign_flag) goto loc_00985A4A;
    if (condition_is_below) goto loc_0098588C;
    if ((uint8_t)(*(uint8_t *)(arg1 + 0xC0)) != 0) goto loc_0098586F;
    if (*(uint64_t *)(arg1 + 0x98) == 0) goto loc_00985A6D;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x10))))) & ((uint32_t)((uint32_t)(0x8000000ULL))));
    result = (uint32_t)(-((uint32_t)(Arg2)));
    Arg1 = ((uint32_t)(0x8000000ULL)) & (result);
    Arg1 = (Arg1) + (0xFFFFFFFFFFFFF000ULL);
    if ((*(uint64_t *)(arg1 + 0x98)) > Arg1) goto loc_00985A59;
    local_r12 = (*(uint64_t *)(arg1 + 0x98)) + (0xFFFULL);
    local_r12 = (local_r12) >> (12);
loc_009853FD:
    result = 0;
    v_stack_m170 = 0;
    v_stack_m1A8 = 0;
    v_stack_m188 = *(uint64_t *)(gs_base + (0 + 0x188));
    if (*(uint64_t *)(arg1 + 0xB0) != 0) goto loc_009859F9;
loc_00985433:
    if (Arg2 == 0) goto loc_00985467;
    if (condition_is_below) goto loc_00985A63;
loc_00985441:
    if (sign_flag) goto loc_00985A77;
loc_00985449:
    a3 = 0;
    result = MiChargeCommit(v_rip + 4929741, local_r12, a3, a4);
    if ((uint32_t)(result) == 0) goto loc_00985A85;
    if (sign_flag) goto loc_0098589D;
loc_00985467:
    result = 0;
    v_stack_m190 = 0;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x10))))) & (0x88000000ULL));
    if (((uint32_t)(result)) != 0x8000000ULL) goto loc_0098597A;
    v_stack_m160 = local_r12;
loc_00985488:
    v_stack_m1A0 = 1;
loc_0098548D:
    Arg2 = (local_r12) * (1);
    Arg2 = (Arg2) - (-128);
    result = MiAllocatePool(64, Arg2, (uint32_t)(0x61436D4DULL), a4);
    if (result == 0) goto loc_009859C2;
    result = MiAllocatePool(256, 80, (uint32_t)(0x6765534DULL), a4);
    if (result == 0) goto loc_00985B0A;
    Arg2 = (uint16_t)(((uint16_t)(*(uint16_t *)(result + 0x3C))) ^ (*(uint16_t *)(v_rip + 0x4B38CD)));
    Arg2 = (uint16_t)((Arg2) & ((uint16_t)((uint32_t)(0x3FFULL))));
    *(uint32_t *)(result + 0x60) = (uint32_t)(v_stack_m1A0);
    *(uint64_t *)(result) = result;
    Arg2 = (uint16_t)((Arg2) ^ ((uint16_t)(*(uint16_t *)(result + 0x3C))));
    *(uint16_t *)(result + 0x3C) = (uint16_t)(Arg2);
    *(uint64_t *)(result + 0x8 + 0x8) = result + 8;
    *(uint64_t *)(result + 0x8) = result + 8;
    *(uint64_t *)(result + 0x70) = 1;
    *(uint64_t *)(result + 0x18) = 1;
    *(uint64_t *)(result + 0x30) = 1;
    if (condition_is_below) goto loc_00985AB2;
loc_00985523:
    if (condition_is_below) goto loc_00985884;
loc_00985532:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x10))))) & (0x8000000ULL));
    if (!(condition_is_equal)) {
    }
    if (condition_is_below) goto loc_00985ABB;
loc_0098554D:
    Arg2 = 0;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0xAC))) << (20));
    Arg1 = (uint32_t)((Arg1) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x38)))));
    Arg1 = (uint32_t)((Arg1) & (0x7F00000ULL));
    Arg1 = (uint32_t)((Arg1) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x38)))));
    *(uint32_t *)(result + 0x38) = (uint32_t)(Arg1);
    result = memset(result, Arg2, Arg2 + 72, a4);
    if (condition_is_below) goto loc_00985AC5;
    if (condition_is_below) goto loc_00985860;
loc_0098558E:
    Arg1 = (uint8_t)(((uint8_t)(*(uint8_t *)(result + 0xE))) ^ (*(uint8_t *)(arg1 + 0x20)));
    Arg1 = (uint8_t)((Arg1) & (31));
    Arg1 = (uint8_t)((Arg1) ^ ((uint8_t)(*(uint8_t *)(result + 0xE))));
    *(uint8_t *)(result + 0xE) = (uint8_t)(Arg1);
    Arg1 = (local_r12) >> (32);
    *(uint32_t *)(result + 0x30) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x1D0)));
    result = (local_r12) << (12);
    *(uint64_t *)(result + 0x18) = result;
    Arg1 = (uint16_t)((Arg1) ^ ((uint16_t)(*(uint16_t *)(result + 0xC))));
    *(uint64_t *)(result) = result;
    Arg1 = (uint16_t)((Arg1) & ((uint16_t)((uint32_t)(0x3FFULL))));
    *(uint32_t *)(result + 0x8) = (uint32_t)(local_r12);
    Arg1 = (uint16_t)((Arg1) ^ ((uint16_t)(*(uint16_t *)(result + 0xC))));
    *(uint16_t *)(result + 0xC) = (uint16_t)(Arg1);
    if (v_stack_m1A7 != 0) goto loc_00985ACF;
    result = 0;
    v_stack_m178 = local_r12;
    local_r10 = 0;
    local_r11 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x10))))) & (0x8000000ULL));
    v_stack_m1A4 = (uint32_t)(local_r11);
loc_0098561D:
    *(uint64_t *)(local_rsp - 0xD8 - 0x78) = 0;
    v_stack_m198 = result + 128;
    *(uint64_t *)(local_rsp - 0xD8 - 0x80) = 0;
    if (0 < v_stack_m1A0) goto loc_0098578A;
    *(uint64_t *)(result + 0x40) = v_stack_m190;
    if (0 >= v_stack_m1A0) goto loc_00985970;
    a3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(result + 40, Arg2, a3, result + 128);
    v_stack_m168 = result;
    if (!(condition_is_above_or_equal)) {
        a3 = result + 40;
        Arg2 = result;
        Arg1 = result + 40;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, a3, result + 128);
        result = v_stack_m168;
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    result = MiUpdateControlAreaCommitCount(result, local_r12, a3, result + 128);
    result = (result) | (-1);
    result = (uint8_t)((result) & (6));
    if (((uint8_t)(result)) == 2) goto loc_009859D6;
loc_009856B4:
    result = KeAbPostRelease(result + 40, local_r12, a3, result + 128);
    if (((uint8_t)(result)) != 2) goto loc_009856E2;
    result = v_stack_m188 + 152;
    if ((*(uint64_t *)(v_stack_m188 + 0x98)) != (v_stack_m188 + 152)) {
        result = KiCheckForKernelApcDelivery(v_stack_m188, 1, a3, result + 128);
    }
    if (sign_flag) goto loc_009858DE;
    result = MiInitializePrototypePtes(*(uint64_t *)(result + 0x80 + 0x8), local_r12, result + 128, 1);
    result = MiUpdateSystemProtoPtesTree(result + 128 + 56, 1, result + 128, 1);
loc_00985713:
    *(uint64_t *)(arg1 + 0x40) = result;
    result = (1) + (1);
    if (result <= 1) goto loc_009859ED;
loc_0098572F:
    Arg1 = (result + 128 + 56) | (-1);
    *(void **)(arg1 + 0x80) = Arg1;
    if (((*(uint32_t *)(v_rip + 0x6413B3)) & (0x400001ULL)) != 0) goto loc_00985B49;
loc_00985757:
    result = 0;
loc_00985759:
    Arg1 = (*(uint64_t *)(local_rsp - 0xD8 + 0xA0)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, 1, result + 128, 1);
    return result;
loc_0098578A:
    result = (*(uint64_t *)(result + 0x80 + 0x50)) & (-7);
    *(uint64_t *)(result + 0x80) = *(uint64_t *)(v_stack_m28 + 0x40);
    result = (result) | (1);
    v_stack_m140 = result + 128;
    *(uint64_t *)(result + 0x80 + 0x50) = result;
    Arg1 = (uint32_t)((*(uint16_t *)(arg1 + 0x20)) + ((uint32_t)(*(uint16_t *)(arg1 + 0x20))));
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x80 + 0x20)))));
    Arg2 = (uint32_t)((Arg2) & (0xFFFFFFC1ULL));
    Arg2 = (uint32_t)((Arg2) ^ ((uint32_t)(Arg1)));
    *(uint32_t *)(result + 0x80 + 0x20) = Arg2;
    local_rdi = v_stack_m150;
    if (v_stack_m150 > v_stack_m138) { local_rdi = v_stack_m138; }
    *(uint32_t *)(result + 0x80 + 0x2C) = (uint32_t)(local_rdi);
    result = Mi4KStartForSubsection(result + 128, 0, result + 128, result + 128);
    *(uint64_t *)(local_rsp - 0xD8 - 0x68) = local_rdi * 8;
    if ((uint32_t)(v_stack_m28) == 0) goto loc_00985896;
    result = MiAllocatePool(274, local_rdi * 8, (uint32_t)(0x74536D4DULL), result + 128);
    v_stack_m168 = result;
    if (result == 0) goto loc_00985B0A;
    if (sign_flag) goto loc_00985AEC;
loc_00985824:
    *(uint64_t *)(v_stack_m170 + 0x8) = result;
loc_0098583B:
    local_r10 = (*(uint64_t *)(local_rsp - 0xD8 - 0x80)) + ((uint32_t)(*(uint32_t *)(v_stack_m170 + 0x2C)));
    a3 = (v_stack_m170) + (88);
    result = (*(uint64_t *)(local_rsp - 0xD8 - 0x78)) + (1);
    *(uint64_t *)(v_stack_m140 + 0x10) = a3;
    goto loc_0098561D;
loc_00985860:
loc_00985865:
    goto loc_0098558E;
loc_0098586F:
    if (local_r12 != 0) goto loc_00985A6D;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x38)))) & (274));
    goto loc_009853FD;
loc_00985884:
    goto loc_00985532;
loc_0098588C:
    goto loc_00985759;
loc_00985896:
    goto loc_0098583B;
loc_0098589D:
    a3 = 0;
    result = MiChargeResident(v_rip + 4929741, *(uint64_t *)(v_stack_m28 + 0x40), a3, v_stack_m140);
    if ((uint32_t)(result) != 0) goto loc_00985A8F;
loc_009858B3:
    a3 = 0;
    result = MiFreeLargeZeroPages(v_rip + 4929741, local_rsp - 216 + 64, a3, v_stack_m140);
    result = MiReturnResident(v_rip + 4929741, *(uint64_t *)(v_stack_m28 + 0x40), a3, v_stack_m140);
loc_009858DE:
    if (v_stack_m178 <= 0) goto loc_00985970;
loc_009858FF:
    Arg2 = ((uint32_t)(*(uint32_t *)(v_stack_m178 + 0x30 - 0x4))) << (3);
    v_stack_m170 = *(uint64_t *)(v_stack_m178 + 0x30 - 0x28);
    result = MmLockPreChargedPagedPool(*(uint64_t *)(v_stack_m178 + 0x30 - 0x28), Arg2, a3, v_stack_m140);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m178 + 0x30))) & (0x3FFFFFFFULL));
    *(uint32_t *)(v_stack_m178 + 0x30) = (uint32_t)(result);
    if (v_stack_m148 != 0) goto loc_00985B2A;
loc_00985932:
    result = 0;
    result = MiUpdateSystemProtoPtesTree(v_stack_m178 + 48 + 8, result + 1, a3, v_stack_m140);
    local_r12 = 0;
    if ((*(uint32_t *)(v_stack_m178 + 0x30 - 0x4)) != 0) goto loc_00985B42;
    local_rbx = (v_stack_m178 + 48) + (88);
    local_r12 = (v_stack_m168) + 1;
    v_stack_m168 = local_r12;
    if (local_r12 < v_stack_m178) goto loc_009858FF;
loc_00985970:
    goto loc_00985713;
loc_0098597A:
    local_rdi = (uint32_t)((1) >> (31));
    Arg2 = 0;
    local_rdi = (uint32_t)((local_rdi) & ((uint32_t)((uint32_t)(0x100000ULL))));
    local_rdi = (uint32_t)((local_rdi) + ((uint32_t)((uint32_t)(0x100000ULL))));
    local_rdi = (local_rdi) >> (3);
    v_stack_m138 = local_rdi;
    v_stack_m178 = local_r12;
    if (0 == 0) goto loc_0098548D;
    result = (local_r12) + (*(uint64_t *)(v_stack_m28 + 0x40));
    goto loc_00985488;
loc_009859C2:
    if (condition_is_below) goto loc_009858B3;
    goto loc_00985759;
loc_009859D6:
    result = ExfTryToWakePushLock(local_rdi, Arg2, a3, v_stack_m140);
    goto loc_009856B4;
loc_009859E3:
    goto loc_00985759;
loc_009859ED:
    goto loc_0098572F;
loc_009859F9:
    if ((*(uint64_t *)(v_rip + 0x4B38CD)) == (v_rip + 4928252)) goto loc_00985433;
    if (!sign_flag) goto loc_00985433;
    goto loc_00985759;
loc_00985A23:
    result = MiValidateUserPhysicalExternalFlags(1, Arg2, a3, v_stack_m140);
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x1C))) & (7));
    goto loc_00985759;
loc_00985A4A:
    result = (uint32_t)((1) & (1));
    if (condition_is_equal) goto loc_0098588C;
loc_00985A59:
    goto loc_00985759;
loc_00985A63:
    if ((((uint8_t)(local_r12)) & (15)) == 0) goto loc_00985441;
loc_00985A6D:
    goto loc_00985759;
loc_00985A77:
    if (((local_r12) & (511)) != 0) goto loc_00985A6D;
    goto loc_00985449;
loc_00985A85:
    goto loc_00985759;
loc_00985A8F:
    v_stack_m180 = (uint8_t)(*(uint64_t *)(v_stack_m28 + 0x40));
    Arg2 = 0;
    Arg1 = 0;
    result = MiThreadIdealNode(Arg1, Arg2, a3, v_stack_m140);
loc_00985AB2:
    goto loc_00985523;
loc_00985ABB:
    goto loc_0098554D;
loc_00985AC5:
    goto loc_00985865;
loc_00985ACF:
loc_00985AEC:
    result = MmObtainChargesToLockPagedPool((uint32_t)(*(uint32_t *)(arg1 + 0x10)), *(uint64_t *)(local_rsp - 0xD8 - 0x68), 1, v_stack_m140);
    if ((uint32_t)(result) != 0) goto loc_00985824;
    Arg2 = 0;
    result = ExFreePoolWithTag((uint32_t)(*(uint32_t *)(arg1 + 0x10)), Arg2, 1, v_stack_m140);
loc_00985B0A:
    local_r14 = 0;
    local_rbx = (uint32_t)((1) & (0x88000000ULL));
loc_00985B2A:
    Arg1 = ((uint32_t)(*(uint32_t *)(arg1 + 0x10))) - 1;
    result = (uint32_t)((result) & (0x3FFFFFFFULL));
    v_stack_m148 = Arg1;
    *(uint32_t *)(local_rbx) = (uint32_t)(result);
    goto loc_00985932;
loc_00985B42:
    result = 0;
loc_00985B49:
    result = MiLogSectionCreate(*(uint64_t *)(v_stack_m28 + 0x40), (uint32_t)((uint32_t)(local_rbx)), 1, v_stack_m140);
    goto loc_00985757;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R/W` |
| `Arg1` | `+ 0x10` | `32` | `R` |
| `Arg1` | `+ 0x1C` | `32` | `R` |
| `Arg1` | `+ 0x20` | `8` | `R` |
| `Arg1` | `+ 0x20` | `16` | `R` |
| `Arg1` | `+ 0x40` | `64` | `W` |
| `Arg1` | `+ 0x80` | `64` | `W` |
| `Arg1` | `+ 0x98` | `64` | `R` |
| `Arg1` | `+ 0xAC` | `32` | `R` |
| `Arg1` | `+ 0xB0` | `64` | `R` |
| `Arg1` | `+ 0xC0` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009852F8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
