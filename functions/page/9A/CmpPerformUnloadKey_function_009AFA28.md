# CmpPerformUnloadKey

- RVA: `0x009AFA28`–`0x009B0143` (길이 `1,819` bytes)
- VA: `0x00000001409AFA28`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0009E0D4`
- 디코드: `441`개 명령, `1,819/1,819` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **60**; 고유 호출 대상: **36**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x009AFAA1` → [CmpInitializeDelayDerefContext](../../text/42/CmpInitializeDelayDerefContext_function_0042A7F0.md) (function, `0x0042A7F0`)
- `0x009AFAA6` → [LOCK_HIVE_LOAD](../9B/LOCK_HIVE_LOAD_function_009B2300.md) (function, `0x009B2300`)
- `0x009AFAAD` → [CmpLockRegistryFreezeAware](../9B/CmpLockRegistryFreezeAware_function_009B4AE4.md) (function, `0x009B4AE4`)
- `0x009AFAD1` → [CmpPerformKeyBodyDeletionCheck](../../pagecmrc/BC/CmpPerformKeyBodyDeletionCheck_function_00BC97D0.md) (function, `0x00BC97D0`)
- `0x009AFB03` → [CmpStartKcbStackForTopLayerKcb](../84/CmpStartKcbStackForTopLayerKcb_function_00848390.md) (function, `0x00848390`)
- `0x009AFB46` → [CmpReportNotifyHelper](../8C/CmpReportNotifyHelper_function_008C7230.md) (function, `0x008C7230`)
- `0x009AFB6E` → [CmpReportNotifyHelper](../8C/CmpReportNotifyHelper_function_008C7230.md) (function, `0x008C7230`)
- `0x009AFB9E` → [CmpPostNotify](../86/CmpPostNotify_function_008645D8.md) (function, `0x008645D8`)
- `0x009AFBB0` → [SeReleaseSubjectContext](../86/SeReleaseSubjectContext_function_0086B710.md) (function, `0x0086B710`)
- `0x009AFBD8` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x009AFC1A` → [CmpDoesKeyHaveOpenSubkeys](../9B/CmpDoesKeyHaveOpenSubkeys_function_009B0274.md) (function, `0x009B0274`)
- `0x009AFC49` → [CmpUnfreezeHive](../7E/CmpUnfreezeHive_function_007EA778.md) (function, `0x007EA778`)
- `0x009AFC62` → [CmpDrainDelayDerefContext](../../text/41/CmpDrainDelayDerefContext_function_0041B9A0.md) (function, `0x0041B9A0`)
- `0x009AFC67` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x009AFC6C` → [UNLOCK_HIVE_LOAD](../9B/UNLOCK_HIVE_LOAD_function_009B2EBC.md) (function, `0x009B2EBC`)
- `0x009AFC82` → [ExWaitForRundownProtectionRelease](../../text/2A/ExWaitForRundownProtectionRelease_function_002A4CB0.md) (function, `0x002A4CB0`)
- `0x009AFC8F` → [LOCK_HIVE_LOAD](../9B/LOCK_HIVE_LOAD_function_009B2300.md) (function, `0x009B2300`)
- `0x009AFC96` → [CmpLockRegistryFreezeAware](../9B/CmpLockRegistryFreezeAware_function_009B4AE4.md) (function, `0x009B4AE4`)
- `0x009AFCB6` → [CmpAttachToRegistryProcess](../../pagecmrc/BC/CmpAttachToRegistryProcess_function_00BC98E0.md) (function, `0x00BC98E0`)
- `0x009AFCC2` → [CmpCompleteUnloadKey](../9B/CmpCompleteUnloadKey_function_009B32FC.md) (function, `0x009B32FC`)
- `0x009AFCCB` → [CmpDetachFromRegistryProcess](../../pagecmrc/BC/CmpDetachFromRegistryProcess_function_00BC9920.md) (function, `0x00BC9920`)
- `0x009AFCFA` → [ExfUnblockPushLock](../../text/2A/ExfUnblockPushLock_function_002A3FE0.md) (function, `0x002A3FE0`)
- `0x009AFD25` → [CmpSignalDeferredPosts](../84/CmpSignalDeferredPosts_function_008484B0.md) (function, `0x008484B0`)
- `0x009AFD33` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (function, `0x00475D80`)
- `0x009AFD3C` → [CmpCleanupRollbackPacket](../9B/CmpCleanupRollbackPacket_function_009B014C.md) (function, `0x009B014C`)
- `0x009AFD4A` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x009AFD7E` → [LOCK_HIVE_LOAD](../9B/LOCK_HIVE_LOAD_function_009B2300.md) (function, `0x009B2300`)
- `0x009AFDAE` → [CmpTryAcquireKcbIXLocks](../9B/CmpTryAcquireKcbIXLocks_function_009B056C.md) (function, `0x009B056C`)
- `0x009AFDCD` → [CmpPrepareForSubtreeInvalidation](../9B/CmpPrepareForSubtreeInvalidation_function_009B01B0.md) (function, `0x009B01B0`)
- `0x009AFDEF` → [CmpLogTransactionAbortedWithChildName](CmpLogTransactionAbortedWithChildName_function_009AED70.md) (function, `0x009AED70`)
- `0x009AFDF4` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x009AFDF9` → [UNLOCK_HIVE_LOAD](../9B/UNLOCK_HIVE_LOAD_function_009B2EBC.md) (function, `0x009B2EBC`)
- `0x009AFE26` → [CmSnapshotRMTxArray](CmSnapshotRMTxArray_function_009AEC9C.md) (function, `0x009AEC9C`)
- `0x009AFE45` → [CmpLogTransactionAbortedWithChildName](CmpLogTransactionAbortedWithChildName_function_009AED70.md) (function, `0x009AED70`)
- `0x009AFE4A` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x009AFE4F` → [UNLOCK_HIVE_LOAD](../9B/UNLOCK_HIVE_LOAD_function_009B2EBC.md) (function, `0x009B2EBC`)
- `0x009AFE76` → [CmpCleanupRollbackPacket](../9B/CmpCleanupRollbackPacket_function_009B014C.md) (function, `0x009B014C`)
- `0x009AFE8C` → [LOCK_HIVE_LOAD](../9B/LOCK_HIVE_LOAD_function_009B2300.md) (function, `0x009B2300`)
- `0x009AFEB5` → [UNLOCK_HIVE_LOAD](../9B/UNLOCK_HIVE_LOAD_function_009B2EBC.md) (function, `0x009B2EBC`)
- `0x009AFECB` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x009AFED0` → [LOCK_HIVE_LOAD](../9B/LOCK_HIVE_LOAD_function_009B2300.md) (function, `0x009B2300`)
- `0x009AFEDE` → [CmShutdownCmRM](../9B/CmShutdownCmRM_function_009B05E0.md) (function, `0x009B05E0`)
- `0x009AFEE5` → [CmpLockRegistryFreezeAware](../9B/CmpLockRegistryFreezeAware_function_009B4AE4.md) (function, `0x009B4AE4`)
- `0x009AFEFB` → [CmpLogUnsupportedOperation](CmpLogUnsupportedOperation_function_009AEA40.md) (function, `0x009AEA40`)
- `0x009AFF1A` → [CmpLogTransactionAbortedWithChildName](CmpLogTransactionAbortedWithChildName_function_009AED70.md) (function, `0x009AED70`)
- `0x009AFF1F` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x009AFF24` → [UNLOCK_HIVE_LOAD](../9B/UNLOCK_HIVE_LOAD_function_009B2EBC.md) (function, `0x009B2EBC`)
- `0x009AFF5C` → [CmpFreezeHive](CmpFreezeHive_function_009AE818.md) (function, `0x009AE818`)
- `0x009AFFF2` → [CmpRollbackLightWeightTransaction](../9B/CmpRollbackLightWeightTransaction_function_009B1158.md) (function, `0x009B1158`)
- `0x009B0005` → [CmpTransDereferenceTransaction](../87/CmpTransDereferenceTransaction_function_00873608.md) (function, `0x00873608`)
- `0x009B0039` → [CmpRollbackLightWeightTransaction](../9B/CmpRollbackLightWeightTransaction_function_009B1158.md) (function, `0x009B1158`)
- `0x009B004C` → [CmpTransDereferenceTransaction](../87/CmpTransDereferenceTransaction_function_00873608.md) (function, `0x00873608`)
- `0x009B007C` → [CmpInvalidateSubtree](../7E/CmpInvalidateSubtree_function_007EAEC0.md) (function, `0x007EAEC0`)
- `0x009B0090` → [CmpFlushNotifiesOnKeyBodyList](../9B/CmpFlushNotifiesOnKeyBodyList_function_009B3594.md) (function, `0x009B3594`)
- `0x009B00BB` → [CmpRollbackLightWeightTransaction](../9B/CmpRollbackLightWeightTransaction_function_009B1158.md) (function, `0x009B1158`)
- `0x009B00CE` → [CmpTransDereferenceTransaction](../87/CmpTransDereferenceTransaction_function_00873608.md) (function, `0x00873608`)
- `0x009B00E8` → [CmObliterateRMTxArray](../7E/CmObliterateRMTxArray_function_007EDF3C.md) (function, `0x007EDF3C`)
- `0x009B0125` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x009B012F` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x009B0139` → [UNLOCK_HIVE_LOAD](../9B/UNLOCK_HIVE_LOAD_function_009B2EBC.md) (function, `0x009B2EBC`)

### Direct callers
- [CmUnloadKey](CmUnloadKey_function_009AF2FC.md) at `0x009AF6BA`

### Static image references
- `0x009AFA44` → RVA `0x00E0A740` (`.data`; read)
- `0x009AFB4B` → RVA `0x00FD9A90` (`PAGEDATA`; read)
- `0x009AFC4E` → RVA `0x00EF59A8` (`.data`; read)
- `0x009AFC56` → RVA `0x00EF59A8` (`.data`; write)
- `0x009AFC71` → RVA `0x00EEFBD0` (`.data`; read/write)
- `0x009AFCE7` → RVA `0x00EF7B30` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **17**
  - `0x009AFAA1` → [CmpInitializeDelayDerefContext](../../text/42/CmpInitializeDelayDerefContext_function_0042A7F0.md) (`PAGE` → `.text`)
  - `0x009AFAD1` → [CmpPerformKeyBodyDeletionCheck](../../pagecmrc/BC/CmpPerformKeyBodyDeletionCheck_function_00BC97D0.md) (`PAGE` → `PAGECMRC`)
  - `0x009AFBD8` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x009AFC62` → [CmpDrainDelayDerefContext](../../text/41/CmpDrainDelayDerefContext_function_0041B9A0.md) (`PAGE` → `.text`)
  - `0x009AFC67` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x009AFC82` → [ExWaitForRundownProtectionRelease](../../text/2A/ExWaitForRundownProtectionRelease_function_002A4CB0.md) (`PAGE` → `.text`)
  - `0x009AFCB6` → [CmpAttachToRegistryProcess](../../pagecmrc/BC/CmpAttachToRegistryProcess_function_00BC98E0.md) (`PAGE` → `PAGECMRC`)
  - `0x009AFCCB` → [CmpDetachFromRegistryProcess](../../pagecmrc/BC/CmpDetachFromRegistryProcess_function_00BC9920.md) (`PAGE` → `PAGECMRC`)
  - `0x009AFCFA` → [ExfUnblockPushLock](../../text/2A/ExfUnblockPushLock_function_002A3FE0.md) (`PAGE` → `.text`)
  - `0x009AFD33` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (`PAGE` → `.text`)
  - `0x009AFD4A` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x009AFDF4` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x009AFE4A` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x009AFECB` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x009AFF1F` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x009B0125` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x009B012F` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
- call이 아닌 외부 분기/꼬리 이동: **14**
  - `0x009AFD78` → [sub_00B2D90C + 0x115](../B2/Unknown_function_00B2D90C.md) (`tail-transfer`)
  - `0x009AFD87` → [sub_00B2D90C + 0x115](../B2/Unknown_function_00B2D90C.md) (`tail-transfer`)
  - `0x009AFFDC` → [sub_00B2D90C + 0x49](../B2/Unknown_function_00B2D90C.md) (`tail-transfer`)
  - `0x009AFFE8` → [sub_00B2D90C](../B2/Unknown_function_00B2D90C.md) (`tail-transfer`)
  - `0x009AFFFC` → [sub_00B2D90C + 0x21](../B2/Unknown_function_00B2D90C.md) (`tail-transfer`)
  - `0x009B0013` → [sub_00B2D90C + 0x3E](../B2/Unknown_function_00B2D90C.md) (`tail-transfer`)
  - `0x009B0023` → [sub_00B2D90C + 0xA4](../B2/Unknown_function_00B2D90C.md) (`tail-transfer`)
  - `0x009B002F` → [sub_00B2D90C + 0x5B](../B2/Unknown_function_00B2D90C.md) (`tail-transfer`)
  - `0x009B0043` → [sub_00B2D90C + 0x7C](../B2/Unknown_function_00B2D90C.md) (`tail-transfer`)
  - `0x009B005A` → [sub_00B2D90C + 0x99](../B2/Unknown_function_00B2D90C.md) (`tail-transfer`)
  - `0x009B00A5` → [sub_00B2D90C + 0x103](../B2/Unknown_function_00B2D90C.md) (`tail-transfer`)
  - `0x009B00B1` → [sub_00B2D90C + 0xB6](../B2/Unknown_function_00B2D90C.md) (`tail-transfer`)
  - `0x009B00C5` → [sub_00B2D90C + 0xD7](../B2/Unknown_function_00B2D90C.md) (`tail-transfer`)
  - `0x009B00DC` → [sub_00B2D90C + 0xF8](../B2/Unknown_function_00B2D90C.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
009AFA28  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
009AFA2D  55                              push rbp
009AFA2E  56                              push rsi
009AFA2F  57                              push rdi
009AFA30  41 54                           push r12
009AFA32  41 55                           push r13
009AFA34  41 56                           push r14
009AFA36  41 57                           push r15
009AFA38  48 8D 6C 24 D9                  lea rbp, [rsp - 0x27]
009AFA3D  48 81 EC E0 00 00 00            sub rsp, 0xe0
009AFA44  48 8B 05 F5 AC 45 00            mov rax, qword ptr [rip + 0x45acf5]
009AFA4B  48 33 C4                        xor rax, rsp
009AFA4E  48 89 45 1F                     mov qword ptr [rbp + 0x1f], rax
009AFA52  0F 57 C0                        xorps xmm0, xmm0
009AFA55  4C 89 4D E7                     mov qword ptr [rbp - 0x19], r9
009AFA59  48 8D 45 A7                     lea rax, [rbp - 0x59]
009AFA5D  0F 57 C9                        xorps xmm1, xmm1
009AFA60  48 89 45 AF                     mov qword ptr [rbp - 0x51], rax
009AFA64  4C 8B F1                        mov r14, rcx
009AFA67  48 8D 45 A7                     lea rax, [rbp - 0x59]
009AFA6B  32 DB                           xor bl, bl
009AFA6D  48 89 45 A7                     mov qword ptr [rbp - 0x59], rax
009AFA71  48 8D 4D D7                     lea rcx, [rbp - 0x29]
009AFA75  83 C8 FF                        or eax, 0xffffffff
009AFA78  88 5D 87                        mov byte ptr [rbp - 0x79], bl
009AFA7B  0F 11 4D B7                     movups xmmword ptr [rbp - 0x49], xmm1
009AFA7F  66 89 45 B9                     mov word ptr [rbp - 0x47], ax
009AFA83  45 8A E0                        mov r12b, r8b
009AFA86  44 8B FA                        mov r15d, edx
009AFA89  0F 11 45 EF                     movups xmmword ptr [rbp - 0x11], xmm0
009AFA8D  0F 11 45 FF                     movups xmmword ptr [rbp - 1], xmm0
009AFA91  0F 11 45 0F                     movups xmmword ptr [rbp + 0xf], xmm0
009AFA95  0F 11 45 D7                     movups xmmword ptr [rbp - 0x29], xmm0
009AFA99  0F 11 45 97                     movups xmmword ptr [rbp - 0x69], xmm0
009AFA9D  0F 11 4D C7                     movups xmmword ptr [rbp - 0x39], xmm1
009AFAA1  E8 4A AD A7 FF                  call 0x14042a7f0
009AFAA6  E8 55 28 00 00                  call 0x1409b2300
009AFAAB  B1 01                           mov cl, 1
009AFAAD  E8 32 50 00 00                  call 0x1409b4ae4
009AFAB2  49 8B 76 08                     mov rsi, qword ptr [r14 + 8]
009AFAB6  C7 45 8B 06 00 00 00            mov dword ptr [rbp - 0x75], 6
009AFABD  8B 46 08                        mov eax, dword ptr [rsi + 8]
009AFAC0  4C 8B 6E 20                     mov r13, qword ptr [rsi + 0x20]
009AFAC4  84 C0                           test al, al
009AFAC6  0F 88 DD 04 00 00               js 0x1409affa9
009AFACC  33 D2                           xor edx, edx
009AFACE  49 8B CE                        mov rcx, r14
009AFAD1  E8 FA 9C 21 00                  call 0x140bc97d0
009AFAD6  8B F8                           mov edi, eax
009AFAD8  85 C0                           test eax, eax
009AFADA  0F 88 93 02 00 00               js 0x1409afd73
009AFAE0  F7 46 08 00 00 04 00            test dword ptr [rsi + 8], 0x40000
009AFAE7  0F 85 C6 04 00 00               jne 0x1409affb3
009AFAED  33 FF                           xor edi, edi
009AFAEF  41 38 BD 80 0B 00 00            cmp byte ptr [r13 + 0xb80], dil
009AFAF6  0F 85 79 04 00 00               jne 0x1409aff75
009AFAFC  48 8B D6                        mov rdx, rsi
009AFAFF  48 8D 4D B7                     lea rcx, [rbp - 0x49]
009AFB03  E8 88 88 E9 FF                  call 0x140848390
009AFB08  85 C0                           test eax, eax
009AFB0A  0F 88 AD 04 00 00               js 0x1409affbd
009AFB10  B8 02 00 00 00                  mov eax, 2
009AFB15  66 39 45 B9                     cmp word ptr [rbp - 0x47], ax
009AFB19  0F AE E8                        lfence
009AFB1C  0F 8D 63 04 00 00               jge 0x1409aff85
009AFB22  48 0F BF 45 B9                  movsx rax, word ptr [rbp - 0x47]
009AFB27  48 8B 5C C5 BF                  mov rbx, qword ptr [rbp + rax*8 - 0x41]
009AFB2C  48 8B 53 20                     mov rdx, qword ptr [rbx + 0x20]
009AFB30  48 8D 45 A7                     lea rax, [rbp - 0x59]
009AFB34  41 B9 04 00 00 00               mov r9d, 4
009AFB3A  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
009AFB3F  45 33 C0                        xor r8d, r8d
009AFB42  48 8D 4D B7                     lea rcx, [rbp - 0x49]
009AFB46  E8 E5 76 F1 FF                  call 0x1408c7230
009AFB4B  48 8B 15 3E 9F 62 00            mov rdx, qword ptr [rip + 0x629f3e]
009AFB52  48 39 53 20                     cmp qword ptr [rbx + 0x20], rdx
009AFB56  74 1B                           je 0x1409afb73
009AFB58  48 8D 45 A7                     lea rax, [rbp - 0x59]
009AFB5C  41 B9 04 00 00 00               mov r9d, 4
009AFB62  45 33 C0                        xor r8d, r8d
009AFB65  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
009AFB6A  48 8D 4D B7                     lea rcx, [rbp - 0x49]
009AFB6E  E8 BD 76 F1 FF                  call 0x1408c7230
009AFB73  49 8B 4E 10                     mov rcx, qword ptr [r14 + 0x10]
009AFB77  48 85 C9                        test rcx, rcx
009AFB7A  74 61                           je 0x1409afbdd
009AFB7C  48 8D 41 10                     lea rax, [rcx + 0x10]
009AFB80  48 39 00                        cmp qword ptr [rax], rax
009AFB83  74 1E                           je 0x1409afba3
009AFB85  48 8D 45 A7                     lea rax, [rbp - 0x59]
009AFB89  41 B9 0B 01 00 00               mov r9d, 0x10b
009AFB8F  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
009AFB94  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
009AFB99  40 88 7C 24 20                  mov byte ptr [rsp + 0x20], dil
009AFB9E  E8 35 4A EB FF                  call 0x1408645d8
009AFBA3  49 8B 5E 10                     mov rbx, qword ptr [r14 + 0x10]
009AFBA7  48 85 DB                        test rbx, rbx
009AFBAA  74 31                           je 0x1409afbdd
009AFBAC  48 8D 4B 38                     lea rcx, [rbx + 0x38]
009AFBB0  E8 5B BB EB FF                  call 0x14086b710
009AFBB5  48 8B 53 08                     mov rdx, qword ptr [rbx + 8]
009AFBB9  48 8B 03                        mov rax, qword ptr [rbx]
009AFBBC  48 89 02                        mov qword ptr [rdx], rax
009AFBBF  48 8B 0B                        mov rcx, qword ptr [rbx]
009AFBC2  48 85 C9                        test rcx, rcx
009AFBC5  74 08                           je 0x1409afbcf
009AFBC7  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
009AFBCB  48 89 41 08                     mov qword ptr [rcx + 8], rax
009AFBCF  33 D2                           xor edx, edx
009AFBD1  49 89 7E 10                     mov qword ptr [r14 + 0x10], rdi
009AFBD5  48 8B CB                        mov rcx, rbx
009AFBD8  E8 93 2C 1D 00                  call 0x140b82870
009AFBDD  48 8B 4E 20                     mov rcx, qword ptr [rsi + 0x20]
009AFBE1  48 3B 0D A8 9E 62 00            cmp rcx, qword ptr [rip + 0x629ea8]
009AFBE8  0F 84 D9 03 00 00               je 0x1409affc7
009AFBEE  BB 00 00 04 00                  mov ebx, 0x40000
009AFBF3  85 9E B8 00 00 00               test dword ptr [rsi + 0xb8], ebx
009AFBF9  0F 84 C8 03 00 00               je 0x1409affc7
009AFBFF  8B 81 10 10 00 00               mov eax, dword ptr [rcx + 0x1010]
009AFC05  A8 04                           test al, 4
009AFC07  0F 85 5E 01 00 00               jne 0x1409afd6b
009AFC0D  41 F6 C7 01                     test r15b, 1
009AFC11  0F 85 75 01 00 00               jne 0x1409afd8c
009AFC17  48 8B CE                        mov rcx, rsi
009AFC1A  E8 55 06 00 00                  call 0x1409b0274
009AFC1F  84 C0                           test al, al
009AFC21  0F 85 29 03 00 00               jne 0x1409aff50
009AFC27  B8 02 00 00 00                  mov eax, 2
009AFC2C  48 39 06                        cmp qword ptr [rsi], rax
009AFC2F  0F 85 1B 03 00 00               jne 0x1409aff50
009AFC35  09 5E 08                        or dword ptr [rsi + 8], ebx
009AFC38  41 80 BD 80 0B 00 00 01         cmp byte ptr [r13 + 0xb80], 1
009AFC40  C6 45 87 01                     mov byte ptr [rbp - 0x79], 1
009AFC44  75 16                           jne 0x1409afc5c
009AFC46  49 8B CD                        mov rcx, r13
009AFC49  E8 2A AB E3 FF                  call 0x1407ea778
009AFC4E  8B 05 54 5D 54 00               mov eax, dword ptr [rip + 0x545d54]
009AFC54  FF C0                           inc eax
009AFC56  89 05 4C 5D 54 00               mov dword ptr [rip + 0x545d4c], eax
009AFC5C  33 D2                           xor edx, edx
009AFC5E  48 8D 4D D7                     lea rcx, [rbp - 0x29]
009AFC62  E8 39 BD A6 FF                  call 0x14041b9a0
009AFC67  E8 18 9E 21 00                  call 0x140bc9a84
009AFC6C  E8 4B 32 00 00                  call 0x1409b2ebc
009AFC71  F0 FF 05 58 FF 53 00            lock inc dword ptr [rip + 0x53ff58]
009AFC78  49 8D 9D 68 06 00 00            lea rbx, [r13 + 0x668]
009AFC7F  48 8B CB                        mov rcx, rbx
009AFC82  E8 29 50 8F FF                  call 0x1402a4cb0
009AFC87  B8 01 00 00 00                  mov eax, 1
009AFC8C  48 87 03                        xchg qword ptr [rbx], rax
009AFC8F  E8 6C 26 00 00                  call 0x1409b2300
009AFC94  B1 01                           mov cl, 1
009AFC96  E8 49 4E 00 00                  call 0x1409b4ae4
009AFC9B  49 8B 8D 38 10 00 00            mov rcx, qword ptr [r13 + 0x1038]
009AFCA2  C7 45 8B 06 00 00 00            mov dword ptr [rbp - 0x75], 6
009AFCA9  48 85 C9                        test rcx, rcx
009AFCAC  0F 85 70 01 00 00               jne 0x1409afe22
009AFCB2  48 8D 4D EF                     lea rcx, [rbp - 0x11]
009AFCB6  E8 25 9C 21 00                  call 0x140bc98e0
009AFCBB  4C 8D 45 8B                     lea r8, [rbp - 0x75]
009AFCBF  48 8B CE                        mov rcx, rsi
009AFCC2  E8 35 36 00 00                  call 0x1409b32fc
009AFCC7  48 8D 4D EF                     lea rcx, [rbp - 0x11]
009AFCCB  E8 50 9C 21 00                  call 0x140bc9920
009AFCD0  33 FF                           xor edi, edi
009AFCD2  83 C8 FF                        or eax, 0xffffffff
009AFCD5  F0 0F C1 05 F3 FE 53 00         lock xadd dword ptr [rip + 0x53fef3], eax
009AFCDD  83 F8 01                        cmp eax, 1
009AFCE0  75 1D                           jne 0x1409afcff
009AFCE2  F0 83 0C 24 00                  lock or dword ptr [rsp], 0
009AFCE7  48 83 3D 41 7E 54 00 00         cmp qword ptr [rip + 0x547e41], 0
009AFCEF  74 0E                           je 0x1409afcff
009AFCF1  33 D2                           xor edx, edx
009AFCF3  48 8D 0D 36 7E 54 00            lea rcx, [rip + 0x547e36]
009AFCFA  E8 E1 42 8F FF                  call 0x1402a3fe0
009AFCFF  B8 02 00 00 00                  mov eax, 2
009AFD04  84 45 8B                        test byte ptr [rbp - 0x75], al
009AFD07  0F 85 22 04 00 00               jne 0x1409b012f
009AFD0D  F6 45 8B 04                     test byte ptr [rbp - 0x75], 4
009AFD11  0F 85 22 04 00 00               jne 0x1409b0139
009AFD17  48 8D 45 A7                     lea rax, [rbp - 0x59]
009AFD1B  48 39 45 A7                     cmp qword ptr [rbp - 0x59], rax
009AFD1F  74 09                           je 0x1409afd2a
009AFD21  48 8D 4D A7                     lea rcx, [rbp - 0x59]
009AFD25  E8 86 87 E9 FF                  call 0x1408484b0
009AFD2A  48 8B 4D CF                     mov rcx, qword ptr [rbp - 0x31]
009AFD2E  48 85 C9                        test rcx, rcx
009AFD31  74 05                           je 0x1409afd38
009AFD33  E8 48 60 AC FF                  call 0x140475d80
009AFD38  48 8D 4D 97                     lea rcx, [rbp - 0x69]
009AFD3C  E8 0B 04 00 00                  call 0x1409b014c
009AFD41  8B C7                           mov eax, edi
009AFD43  48 8B 4D 1F                     mov rcx, qword ptr [rbp + 0x1f]
009AFD47  48 33 CC                        xor rcx, rsp
009AFD4A  E8 F1 C8 CF FF                  call 0x1406ac640
009AFD4F  48 8B 9C 24 28 01 00 00         mov rbx, qword ptr [rsp + 0x128]
009AFD57  48 81 C4 E0 00 00 00            add rsp, 0xe0
009AFD5E  41 5F                           pop r15
009AFD60  41 5E                           pop r14
009AFD62  41 5D                           pop r13
009AFD64  41 5C                           pop r12
009AFD66  5F                              pop rdi
009AFD67  5E                              pop rsi
009AFD68  5D                              pop rbp
009AFD69  C3                              ret
009AFD6A  CC                              int3
009AFD6B  BF 22 00 00 C0                  mov edi, 0xc0000022
009AFD70  8A 5D 87                        mov bl, byte ptr [rbp - 0x79]
009AFD73  8B 45 8B                        mov eax, dword ptr [rbp - 0x75]
009AFD76  A8 04                           test al, 4
009AFD78  0F 85 A3 DC 17 00               jne 0x140b2da21
009AFD7E  E8 7D 25 00 00                  call 0x1409b2300
009AFD83  83 4D 8B 04                     or dword ptr [rbp - 0x75], 4
009AFD87  E9 95 DC 17 00                  jmp 0x140b2da21
009AFD8C  48 8B 86 C0 00 00 00            mov rax, qword ptr [rsi + 0xc0]
009AFD93  48 85 C0                        test rax, rax
009AFD96  74 0D                           je 0x1409afda5
009AFD98  48 83 C0 20                     add rax, 0x20
009AFD9C  48 39 00                        cmp qword ptr [rax], rax
009AFD9F  0F 85 51 01 00 00               jne 0x1409afef6
009AFDA5  4C 8D 4D 97                     lea r9, [rbp - 0x69]
009AFDA9  B2 01                           mov dl, 1
009AFDAB  48 8B CE                        mov rcx, rsi
009AFDAE  E8 B9 07 00 00                  call 0x1409b056c
009AFDB3  8B F8                           mov edi, eax
009AFDB5  3D 2D 02 00 C0                  cmp eax, 0xc000022d
009AFDBA  0F 84 4A 01 00 00               je 0x1409aff0a
009AFDC0  85 C0                           test eax, eax
009AFDC2  78 AC                           js 0x1409afd70
009AFDC4  4C 8D 45 97                     lea r8, [rbp - 0x69]
009AFDC8  33 D2                           xor edx, edx
009AFDCA  48 8B CE                        mov rcx, rsi
009AFDCD  E8 DE 03 00 00                  call 0x1409b01b0
009AFDD2  8B F8                           mov edi, eax
009AFDD4  3D 2D 02 00 C0                  cmp eax, 0xc000022d
009AFDD9  0F 85 80 02 00 00               jne 0x1409b005f
009AFDDF  8B 45 97                        mov eax, dword ptr [rbp - 0x69]
009AFDE2  33 D2                           xor edx, edx
009AFDE4  48 8B CE                        mov rcx, rsi
009AFDE7  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
009AFDEB  44 8D 42 0A                     lea r8d, [rdx + 0xa]
009AFDEF  E8 7C EF FF FF                  call 0x1409aed70
009AFDF4  E8 8B 9C 21 00                  call 0x140bc9a84
009AFDF9  E8 BE 30 00 00                  call 0x1409b2ebc
009AFDFE  83 65 8B 00                     and dword ptr [rbp - 0x75], 0
009AFE02  33 FF                           xor edi, edi
009AFE04  45 33 FF                        xor r15d, r15d
009AFE07  39 7D 97                        cmp dword ptr [rbp - 0x69], edi
009AFE0A  0F 87 08 02 00 00               ja 0x1409b0018
009AFE10  85 FF                           test edi, edi
009AFE12  0F 88 58 FF FF FF               js 0x1409afd70
009AFE18  BF 2D 02 00 C0                  mov edi, 0xc000022d
009AFE1D  E9 4E FF FF FF                  jmp 0x1409afd70
009AFE22  48 8D 55 97                     lea rdx, [rbp - 0x69]
009AFE26  E8 71 EE FF FF                  call 0x1409aec9c
009AFE2B  8B F8                           mov edi, eax
009AFE2D  85 C0                           test eax, eax
009AFE2F  0F 88 3B FF FF FF               js 0x1409afd70
009AFE35  8B 45 97                        mov eax, dword ptr [rbp - 0x69]
009AFE38  33 D2                           xor edx, edx
009AFE3A  48 8B CE                        mov rcx, rsi
009AFE3D  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
009AFE41  44 8D 42 09                     lea r8d, [rdx + 9]
009AFE45  E8 26 EF FF FF                  call 0x1409aed70
009AFE4A  E8 35 9C 21 00                  call 0x140bc9a84
009AFE4F  E8 68 30 00 00                  call 0x1409b2ebc
009AFE54  83 65 8B 00                     and dword ptr [rbp - 0x75], 0
009AFE58  33 FF                           xor edi, edi
009AFE5A  45 33 FF                        xor r15d, r15d
009AFE5D  40 88 7D 8F                     mov byte ptr [rbp - 0x71], dil
009AFE61  39 7D 97                        cmp dword ptr [rbp - 0x69], edi
009AFE64  0F 87 30 02 00 00               ja 0x1409b009a
009AFE6A  85 FF                           test edi, edi
009AFE6C  0F 88 FE FE FF FF               js 0x1409afd70
009AFE72  48 8D 4D 97                     lea rcx, [rbp - 0x69]
009AFE76  E8 D1 02 00 00                  call 0x1409b014c
009AFE7B  80 7D 8F 00                     cmp byte ptr [rbp - 0x71], 0
009AFE7F  0F 57 C0                        xorps xmm0, xmm0
009AFE82  0F 11 45 97                     movups xmmword ptr [rbp - 0x69], xmm0
009AFE86  0F 85 55 02 00 00               jne 0x1409b00e1
009AFE8C  E8 6F 24 00 00                  call 0x1409b2300
009AFE91  49 8B 85 38 10 00 00            mov rax, qword ptr [r13 + 0x1038]
009AFE98  33 FF                           xor edi, edi
009AFE9A  48 85 C0                        test rax, rax
009AFE9D  0F 85 4F 02 00 00               jne 0x1409b00f2
009AFEA3  49 8B 85 38 10 00 00            mov rax, qword ptr [r13 + 0x1038]
009AFEAA  33 DB                           xor ebx, ebx
009AFEAC  48 85 C0                        test rax, rax
009AFEAF  0F 85 55 02 00 00               jne 0x1409b010a
009AFEB5  E8 02 30 00 00                  call 0x1409b2ebc
009AFEBA  48 85 FF                        test rdi, rdi
009AFEBD  0F 85 5F 02 00 00               jne 0x1409b0122
009AFEC3  48 85 DB                        test rbx, rbx
009AFEC6  74 08                           je 0x1409afed0
009AFEC8  48 8B CB                        mov rcx, rbx
009AFECB  E8 E0 D3 CF FF                  call 0x1406ad2b0
009AFED0  E8 2B 24 00 00                  call 0x1409b2300
009AFED5  49 8B 8D 38 10 00 00            mov rcx, qword ptr [r13 + 0x1038]
009AFEDC  B2 01                           mov dl, 1
009AFEDE  E8 FD 06 00 00                  call 0x1409b05e0
009AFEE3  B1 01                           mov cl, 1
009AFEE5  E8 FA 4B 00 00                  call 0x1409b4ae4
009AFEEA  C7 45 8B 06 00 00 00            mov dword ptr [rbp - 0x75], 6
009AFEF1  E9 BC FD FF FF                  jmp 0x1409afcb2
009AFEF6  B9 03 00 00 00                  mov ecx, 3
009AFEFB  E8 40 EB FF FF                  call 0x1409aea40
009AFF00  BF 21 01 00 C0                  mov edi, 0xc0000121
009AFF05  E9 66 FE FF FF                  jmp 0x1409afd70
009AFF0A  8B 45 97                        mov eax, dword ptr [rbp - 0x69]
009AFF0D  33 D2                           xor edx, edx
009AFF0F  48 8B CE                        mov rcx, rsi
009AFF12  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
009AFF16  44 8D 42 0A                     lea r8d, [rdx + 0xa]
009AFF1A  E8 51 EE FF FF                  call 0x1409aed70
009AFF1F  E8 60 9B 21 00                  call 0x140bc9a84
009AFF24  E8 93 2F 00 00                  call 0x1409b2ebc
009AFF29  83 65 8B 00                     and dword ptr [rbp - 0x75], 0
009AFF2D  33 FF                           xor edi, edi
009AFF2F  45 33 FF                        xor r15d, r15d
009AFF32  39 7D 97                        cmp dword ptr [rbp - 0x69], edi
009AFF35  0F 87 96 00 00 00               ja 0x1409affd1
009AFF3B  8A 5D 87                        mov bl, byte ptr [rbp - 0x79]
009AFF3E  85 FF                           test edi, edi
009AFF40  0F 88 2D FE FF FF               js 0x1409afd73
009AFF46  BF 2D 02 00 C0                  mov edi, 0xc000022d
009AFF4B  E9 23 FE FF FF                  jmp 0x1409afd73
009AFF50  45 84 E4                        test r12b, r12b
009AFF53  74 AB                           je 0x1409aff00
009AFF55  48 8B 55 E7                     mov rdx, qword ptr [rbp - 0x19]
009AFF59  48 8B CE                        mov rcx, rsi
009AFF5C  E8 B7 E8 FF FF                  call 0x1409ae818
009AFF61  8B F8                           mov edi, eax
009AFF63  85 C0                           test eax, eax
009AFF65  0F 88 05 FE FF FF               js 0x1409afd70
009AFF6B  BF 03 01 00 00                  mov edi, 0x103
009AFF70  E9 8A FD FF FF                  jmp 0x1409afcff
009AFF75  41 F6 C7 01                     test r15b, 1
009AFF79  75 1D                           jne 0x1409aff98
009AFF7B  BF 89 01 00 C0                  mov edi, 0xc0000189
009AFF80  E9 EE FD FF FF                  jmp 0x1409afd73
009AFF85  48 0F BF 4D B9                  movsx rcx, word ptr [rbp - 0x47]
009AFF8A  48 8B 45 CF                     mov rax, qword ptr [rbp - 0x31]
009AFF8E  48 8B 5C C8 F0                  mov rbx, qword ptr [rax + rcx*8 - 0x10]
009AFF93  E9 94 FB FF FF                  jmp 0x1409afb2c
009AFF98  41 8B 85 10 10 00 00            mov eax, dword ptr [r13 + 0x1010]
009AFF9F  A8 20                           test al, 0x20
009AFFA1  0F 85 55 FB FF FF               jne 0x1409afafc
009AFFA7  EB D2                           jmp 0x1409aff7b
009AFFA9  BF 22 00 00 C0                  mov edi, 0xc0000022
009AFFAE  E9 C0 FD FF FF                  jmp 0x1409afd73
009AFFB3  BF 25 04 00 C0                  mov edi, 0xc0000425
009AFFB8  E9 B6 FD FF FF                  jmp 0x1409afd73
009AFFBD  BF 9A 00 00 C0                  mov edi, 0xc000009a
009AFFC2  E9 AC FD FF FF                  jmp 0x1409afd73
009AFFC7  BF 0D 00 00 C0                  mov edi, 0xc000000d
009AFFCC  E9 9F FD FF FF                  jmp 0x1409afd70
009AFFD1  48 8B 5D 9F                     mov rbx, qword ptr [rbp - 0x61]
009AFFD5  4A 8B 1C FB                     mov rbx, qword ptr [rbx + r15*8]
009AFFD9  48 85 DB                        test rbx, rbx
009AFFDC  0F 84 73 D9 17 00               je 0x140b2d955
009AFFE2  48 8B CB                        mov rcx, rbx
009AFFE5  F6 C3 01                        test bl, 1
009AFFE8  0F 84 1E D9 17 00               je 0x140b2d90c
009AFFEE  48 83 E1 FE                     and rcx, 0xfffffffffffffffe
009AFFF2  E8 61 11 00 00                  call 0x1409b1158
009AFFF7  44 8B F0                        mov r14d, eax
009AFFFA  85 C0                           test eax, eax
009AFFFC  0F 88 2B D9 17 00               js 0x140b2d92d
009B0002  48 8B CB                        mov rcx, rbx
009B0005  E8 FE 35 EC FF                  call 0x140873608
009B000A  48 8B 4D 9F                     mov rcx, qword ptr [rbp - 0x61]
009B000E  4A 83 24 F9 00                  and qword ptr [rcx + r15*8], 0
009B0013  E9 32 D9 17 00                  jmp 0x140b2d94a
009B0018  48 8B 5D 9F                     mov rbx, qword ptr [rbp - 0x61]
009B001C  4A 8B 1C FB                     mov rbx, qword ptr [rbx + r15*8]
009B0020  48 85 DB                        test rbx, rbx
009B0023  0F 84 87 D9 17 00               je 0x140b2d9b0
009B0029  48 8B CB                        mov rcx, rbx
009B002C  F6 C3 01                        test bl, 1
009B002F  0F 84 32 D9 17 00               je 0x140b2d967
009B0035  48 83 E1 FE                     and rcx, 0xfffffffffffffffe
009B0039  E8 1A 11 00 00                  call 0x1409b1158
009B003E  44 8B F0                        mov r14d, eax
009B0041  85 C0                           test eax, eax
009B0043  0F 88 3F D9 17 00               js 0x140b2d988
009B0049  48 8B CB                        mov rcx, rbx
009B004C  E8 B7 35 EC FF                  call 0x140873608
009B0051  48 8B 4D 9F                     mov rcx, qword ptr [rbp - 0x61]
009B0055  4A 83 24 F9 00                  and qword ptr [rcx + r15*8], 0
009B005A  E9 46 D9 17 00                  jmp 0x140b2d9a5
009B005F  85 C0                           test eax, eax
009B0061  0F 88 09 FD FF FF               js 0x1409afd70
009B0067  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
009B006D  4C 8D 4D D7                     lea r9, [rbp - 0x29]
009B0071  BA 01 00 00 00                  mov edx, 1
009B0076  48 8B CE                        mov rcx, rsi
009B0079  44 8B C2                        mov r8d, edx
009B007C  E8 3F AE E3 FF                  call 0x1407eaec0
009B0081  41 B1 01                        mov r9b, 1
009B0084  4C 8D 45 D7                     lea r8, [rbp - 0x29]
009B0088  BA 01 00 00 00                  mov edx, 1
009B008D  48 8B CE                        mov rcx, rsi
009B0090  E8 FF 34 00 00                  call 0x1409b3594
009B0095  E9 9B FB FF FF                  jmp 0x1409afc35
009B009A  48 8B 5D 9F                     mov rbx, qword ptr [rbp - 0x61]
009B009E  4A 8B 1C FB                     mov rbx, qword ptr [rbx + r15*8]
009B00A2  48 85 DB                        test rbx, rbx
009B00A5  0F 84 64 D9 17 00               je 0x140b2da0f
009B00AB  48 8B CB                        mov rcx, rbx
009B00AE  F6 C3 01                        test bl, 1
009B00B1  0F 84 0B D9 17 00               je 0x140b2d9c2
009B00B7  48 83 E1 FE                     and rcx, 0xfffffffffffffffe
009B00BB  E8 98 10 00 00                  call 0x1409b1158
009B00C0  44 8B F0                        mov r14d, eax
009B00C3  85 C0                           test eax, eax
009B00C5  0F 88 18 D9 17 00               js 0x140b2d9e3
009B00CB  48 8B CB                        mov rcx, rbx
009B00CE  E8 35 35 EC FF                  call 0x140873608
009B00D3  48 8B 4D 9F                     mov rcx, qword ptr [rbp - 0x61]
009B00D7  4A 83 24 F9 00                  and qword ptr [rcx + r15*8], 0
009B00DC  E9 23 D9 17 00                  jmp 0x140b2da04
009B00E1  49 8B 8D 38 10 00 00            mov rcx, qword ptr [r13 + 0x1038]
009B00E8  E8 4F DE E3 FF                  call 0x1407edf3c
009B00ED  E9 9A FD FF FF                  jmp 0x1409afe8c
009B00F2  83 78 40 01                     cmp dword ptr [rax + 0x40], 1
009B00F6  0F 85 A7 FD FF FF               jne 0x1409afea3
009B00FC  48 8B 78 30                     mov rdi, qword ptr [rax + 0x30]
009B0100  48 83 60 30 00                  and qword ptr [rax + 0x30], 0
009B0105  E9 99 FD FF FF                  jmp 0x1409afea3
009B010A  83 78 40 01                     cmp dword ptr [rax + 0x40], 1
009B010E  0F 85 A1 FD FF FF               jne 0x1409afeb5
009B0114  48 8B 58 20                     mov rbx, qword ptr [rax + 0x20]
009B0118  48 83 60 20 00                  and qword ptr [rax + 0x20], 0
009B011D  E9 93 FD FF FF                  jmp 0x1409afeb5
009B0122  48 8B CF                        mov rcx, rdi
009B0125  E8 86 D1 CF FF                  call 0x1406ad2b0
009B012A  E9 94 FD FF FF                  jmp 0x1409afec3
009B012F  E8 50 99 21 00                  call 0x140bc9a84
009B0134  E9 D4 FB FF FF                  jmp 0x1409afd0d
009B0139  E8 7E 2D 00 00                  call 0x1409b2ebc
009B013E  E9 D4 FB FF FF                  jmp 0x1409afd17
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpPerformUnloadKey(__int64 a1, int a2, int a3, __int64 a4)
{
    __int64 result;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned int v_stack_m118;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m5F;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int16 v_stack_mA6;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int8 v_stack_mD0;
    unsigned int v_stack_mD4;
    unsigned __int8 v_stack_mD8;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p20;

    v_stack_p10 = v_rbx;
    v_rsp = (v_rsp) - (224);
    result = (*(unsigned __int64 *)(v_rip + 4566261)) ^ (v_rsp);
    v_stack_m40 = result;
    v_stack_m78 = a4;
    v_stack_mB0 = v_stack_mB8;
    v_rbx = 0;
    v_stack_mB8 = v_stack_mB8;
    result = (unsigned int)((v_stack_mB8) | (0xFFFFFFFFULL));
    v_stack_mD8 = 0;
    v_stack_mA8 = v_xmm1;
    v_stack_mA6 = (unsigned __int16)(result);
    v_stack_m70 = v_xmm0;
    v_stack_m60 = v_xmm0;
    v_stack_m50 = v_xmm0;
    v_stack_m88 = v_xmm0;
    v_stack_mC8 = v_xmm0;
    v_stack_m98 = v_xmm1;
    result = CmpInitializeDelayDerefContext(v_stack_m88, a2, a3, a4);
    result = LOCK_HIVE_LOAD(v_stack_m88, a2, a3, a4);
    result = CmpLockRegistryFreezeAware(1, a2, a3, a4);
    v_stack_mD4 = 6;
    if (sign_flag) goto loc_009AFFA9;
    a2 = 0;
    result = CmpPerformKeyBodyDeletionCheck(a1, a2, a3, a4);
    if (sign_flag) goto loc_009AFD73;
    if (((*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 8)) & (0x40000ULL)) != 0) goto loc_009AFFB3;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 2944)) != 0) goto loc_009AFF75;
loc_009AFAFC:
    result = CmpStartKcbStackForTopLayerKcb(v_stack_mA8, *(unsigned __int64 *)(a1 + 8), a3, a4);
    if (sign_flag) goto loc_009AFFBD;
    if (v_stack_mA6 >= 2) goto loc_009AFF85;
loc_009AFB2C:
    v_stack_mF8 = v_stack_mB8;
    a3 = 0;
    result = CmpReportNotifyHelper(v_stack_mA8, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m5F + (__int16)(v_stack_mA6) * 8 - 65) + 32), a3, 4);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m5F + (__int16)(v_stack_mA6) * 8 - 65) + 32)) != (*(unsigned __int64 *)(v_rip + 6463294))) {
        result = v_stack_mB8;
        a4 = 4;
        a3 = 0;
        v_stack_mF8 = result;
        a1 = v_stack_mA8;
        result = CmpReportNotifyHelper(a1, *(unsigned __int64 *)(v_rip + 6463294), a3, a4);
    }
    if (*(unsigned __int64 *)(a1 + 16) == 0) goto loc_009AFBDD;
    result = *(unsigned __int64 *)(a1 + 16) + 16;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 16)) != (*(unsigned __int64 *)(a1 + 16) + 16)) {
        result = v_stack_mB8;
        a4 = 267;
        v_stack_mE8 = result;
        v_stack_mF0 = 0;
        v_stack_mF8 = 0;
        result = CmpPostNotify(*(unsigned __int64 *)(a1 + 16), *(unsigned __int64 *)(v_rip + 6463294), a3, a4);
    }
    if (*(unsigned __int64 *)(a1 + 16) == 0) goto loc_009AFBDD;
    result = SeReleaseSubjectContext(*(unsigned __int64 *)(a1 + 16) + 56, *(unsigned __int64 *)(v_rip + 6463294), a3, a4);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 8)) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16));
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16));
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16)) != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 8);
        *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16)) + 8) = result;
    }
    a2 = 0;
    *(unsigned __int64 *)(a1 + 16) = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(a1 + 16), a2, a3, a4);
loc_009AFBDD:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32)) == (*(unsigned __int64 *)(v_rip + 6463144))) goto loc_009AFFC7;
    if (((*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 184)) & ((unsigned int)((unsigned int)(0x40000ULL)))) == 0) goto loc_009AFFC7;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 4112)))) & (4)) != 0) goto loc_009AFD6B;
    if ((((unsigned __int8)((unsigned int)(a2))) & (1)) != 0) goto loc_009AFD8C;
    result = CmpDoesKeyHaveOpenSubkeys(*(unsigned __int64 *)(a1 + 8), a2, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_009AFF50;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8))) != 2) goto loc_009AFF50;
loc_009AFC35:
    v_stack_mD8 = 1;
    result = 2;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 2944)) == 1) {
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32);
        result = CmpUnfreezeHive(a1, a2, a3, a4);
        result = *(unsigned int *)(v_rip + 5528916);
        result = (unsigned int)((result) + 1);
        *(unsigned int *)(v_rip + 5528908) = (unsigned int)(result);
    }
    a2 = 0;
    result = CmpDrainDelayDerefContext(v_stack_m88, a2, a3, a4);
    result = CmpUnlockRegistry(v_stack_m88, a2, a3, a4);
    result = UNLOCK_HIVE_LOAD(v_stack_m88, a2, a3, a4);
    result = ExWaitForRundownProtectionRelease(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 1640, a2, a3, a4);
    result = LOCK_HIVE_LOAD(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 1640, a2, a3, a4);
    result = CmpLockRegistryFreezeAware(1, a2, a3, a4);
    v_stack_mD4 = 6;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 4152) != 0) goto loc_009AFE22;
loc_009AFCB2:
    result = CmpAttachToRegistryProcess(v_stack_m70, a2, a3, a4);
    result = CmpCompleteUnloadKey(*(unsigned __int64 *)(a1 + 8), a2, v_stack_mD4, a4);
    result = CmpDetachFromRegistryProcess(v_stack_m70, a2, v_stack_mD4, a4);
    v_rdi = 0;
    result = (unsigned int)((result) | (0xFFFFFFFFULL));
    if (((unsigned int)(result)) != 1) goto loc_009AFCFF;
    if ((*(unsigned __int64 *)(v_rip + 5537345)) != 0) {
        a2 = 0;
        a1 = v_rip + 5537334;
        result = ExfUnblockPushLock(a1, a2, v_stack_mD4, a4);
    }
    if (((v_stack_mD4) & (2)) != 0) goto loc_009B012F;
loc_009AFD0D:
    if (((v_stack_mD4) & (4)) != 0) goto loc_009B0139;
loc_009AFD17:
    result = v_stack_mB8;
    if (v_stack_mB8 != v_stack_mB8) {
        a1 = v_stack_mB8;
        result = CmpSignalDeferredPosts(a1, a2, v_stack_mD4, a4);
    }
    if (v_stack_m90 != 0) {
        result = CmSiFreeMemory(v_stack_m90, a2, v_stack_mD4, a4);
    }
    result = CmpCleanupRollbackPacket(v_stack_mC8, a2, v_stack_mD4, a4);
    a1 = (v_stack_m40) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, v_stack_mD4, a4);
    v_rsp = (v_rsp) + (224);
    return result;
loc_009AFD6B:
loc_009AFD70:
loc_009AFD73:
    result = LOCK_HIVE_LOAD(a1, a2, v_stack_mD4, a4);
loc_009AFD8C:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 192) == 0) goto loc_009AFDA5;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 192)) + (32);
    if ((*(unsigned __int64 *)(result)) != result) goto loc_009AFEF6;
loc_009AFDA5:
    result = CmpTryAcquireKcbIXLocks(*(unsigned __int64 *)(a1 + 8), 1, v_stack_mD4, v_stack_mC8);
    if (((unsigned int)(result)) == 0xC000022DULL) goto loc_009AFF0A;
    if (sign_flag) goto loc_009AFD70;
    a2 = 0;
    result = CmpPrepareForSubtreeInvalidation(*(unsigned __int64 *)(a1 + 8), a2, v_stack_mC8, v_stack_mC8);
    if (((unsigned int)(result)) != 0xC000022DULL) goto loc_009B005F;
    a2 = 0;
    v_stack_p20 = (unsigned int)((unsigned int)(v_stack_mC8));
    result = CmpLogTransactionAbortedWithChildName(*(unsigned __int64 *)(a1 + 8), a2, a2 + 10, v_stack_mC8);
    result = CmpUnlockRegistry(*(unsigned __int64 *)(a1 + 8), a2, a2 + 10, v_stack_mC8);
    result = UNLOCK_HIVE_LOAD(*(unsigned __int64 *)(a1 + 8), a2, a2 + 10, v_stack_mC8);
    v_rdi = 0;
    v_r15 = 0;
    if (v_stack_mC8 > 0) goto loc_009B0018;
    if (sign_flag) goto loc_009AFD70;
    goto loc_009AFD70;
loc_009AFE22:
    result = CmSnapshotRMTxArray(*(unsigned __int64 *)(a1 + 8), v_stack_mC8, a2 + 10, v_stack_mC8);
    if (sign_flag) goto loc_009AFD70;
    a2 = 0;
    v_stack_p20 = (unsigned int)((unsigned int)(v_stack_mC8));
    result = CmpLogTransactionAbortedWithChildName(*(unsigned __int64 *)(a1 + 8), a2, a2 + 9, v_stack_mC8);
    result = CmpUnlockRegistry(*(unsigned __int64 *)(a1 + 8), a2, a2 + 9, v_stack_mC8);
    result = UNLOCK_HIVE_LOAD(*(unsigned __int64 *)(a1 + 8), a2, a2 + 9, v_stack_mC8);
    v_rdi = 0;
    v_r15 = 0;
    v_stack_mD0 = 0;
    if (v_stack_mC8 > 0) goto loc_009B009A;
    if (sign_flag) goto loc_009AFD70;
    result = CmpCleanupRollbackPacket(v_stack_mC8, a2, a2 + 9, v_stack_mC8);
    v_stack_mC8 = v_xmm0;
    if (v_stack_mD0 != 0) goto loc_009B00E1;
loc_009AFE8C:
    result = LOCK_HIVE_LOAD(v_stack_mC8, a2, a2 + 9, v_stack_mC8);
    v_rdi = 0;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 4152) != 0) goto loc_009B00F2;
loc_009AFEA3:
    v_rbx = 0;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 4152) != 0) goto loc_009B010A;
loc_009AFEB5:
    result = UNLOCK_HIVE_LOAD(v_stack_mC8, a2, a2 + 9, v_stack_mC8);
    if (0 != 0) goto loc_009B0122;
loc_009AFEC3:
    if (0 != 0) {
        a1 = 0;
        result = ZwClose(a1, a2, a2 + 9, v_stack_mC8);
    }
    result = LOCK_HIVE_LOAD(a1, a2, a2 + 9, v_stack_mC8);
    result = CmShutdownCmRM(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 4152), 1, a2 + 9, v_stack_mC8);
    result = CmpLockRegistryFreezeAware(1, 1, a2 + 9, v_stack_mC8);
    v_stack_mD4 = 6;
    goto loc_009AFCB2;
loc_009AFEF6:
    result = CmpLogUnsupportedOperation(3, 1, a2 + 9, v_stack_mC8);
loc_009AFF00:
    goto loc_009AFD70;
loc_009AFF0A:
    a2 = 0;
    v_stack_p20 = (unsigned int)((unsigned int)(v_stack_mC8));
    result = CmpLogTransactionAbortedWithChildName(*(unsigned __int64 *)(a1 + 8), a2, a2 + 10, v_stack_mC8);
    result = CmpUnlockRegistry(*(unsigned __int64 *)(a1 + 8), a2, a2 + 10, v_stack_mC8);
    result = UNLOCK_HIVE_LOAD(*(unsigned __int64 *)(a1 + 8), a2, a2 + 10, v_stack_mC8);
    v_rdi = 0;
    v_r15 = 0;
    if (v_stack_mC8 > 0) goto loc_009AFFD1;
    if (sign_flag) goto loc_009AFD73;
    goto loc_009AFD73;
loc_009AFF50:
    if ((unsigned __int8)((unsigned __int8)(a3)) == 0) goto loc_009AFF00;
    result = CmpFreezeHive(*(unsigned __int64 *)(a1 + 8), v_stack_m78, a2 + 10, v_stack_mC8);
    if (sign_flag) goto loc_009AFD70;
    goto loc_009AFCFF;
loc_009AFF75:
    if (((0) & (1)) != 0) goto loc_009AFF98;
loc_009AFF7B:
    goto loc_009AFD73;
loc_009AFF85:
    goto loc_009AFB2C;
loc_009AFF98:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 4112)))) & (32)) != 0) goto loc_009AFAFC;
    goto loc_009AFF7B;
loc_009AFFA9:
    goto loc_009AFD73;
loc_009AFFB3:
    goto loc_009AFD73;
loc_009AFFBD:
    goto loc_009AFD73;
loc_009AFFC7:
    goto loc_009AFD70;
loc_009AFFD1:
    a1 = (*(unsigned __int64 *)(v_stack_mC0 + v_r15 * 8)) & (-2);
    result = CmpRollbackLightWeightTransaction(a1, v_stack_m78, a2 + 10, v_stack_mC8);
    result = CmpTransDereferenceTransaction(*(unsigned __int64 *)(v_stack_mC0 + v_r15 * 8), v_stack_m78, a2 + 10, v_stack_mC8);
loc_009B0018:
    a1 = (*(unsigned __int64 *)(v_stack_mC0 + v_r15 * 8)) & (-2);
    result = CmpRollbackLightWeightTransaction(a1, v_stack_m78, a2 + 10, v_stack_mC8);
    result = CmpTransDereferenceTransaction(*(unsigned __int64 *)(v_stack_mC0 + v_r15 * 8), v_stack_m78, a2 + 10, v_stack_mC8);
loc_009B005F:
    if (sign_flag) goto loc_009AFD70;
    result = CmpInvalidateSubtree(*(unsigned __int64 *)(a1 + 8), 1, 1, v_stack_m88);
    result = CmpFlushNotifiesOnKeyBodyList(*(unsigned __int64 *)(a1 + 8), 1, v_stack_m88, 1);
    goto loc_009AFC35;
loc_009B009A:
    a1 = (*(unsigned __int64 *)(v_stack_mC0 + v_r15 * 8)) & (-2);
    result = CmpRollbackLightWeightTransaction(a1, 1, v_stack_m88, 1);
    result = CmpTransDereferenceTransaction(*(unsigned __int64 *)(v_stack_mC0 + v_r15 * 8), 1, v_stack_m88, 1);
loc_009B00E1:
    result = CmObliterateRMTxArray(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 4152), 1, v_stack_m88, 1);
    goto loc_009AFE8C;
loc_009B00F2:
    if ((*(unsigned int *)(result + 64)) != 1) goto loc_009AFEA3;
    goto loc_009AFEA3;
loc_009B010A:
    if ((*(unsigned int *)(result + 64)) != 1) goto loc_009AFEB5;
    goto loc_009AFEB5;
loc_009B0122:
    result = ZwClose(*(unsigned __int64 *)(result + 48), 1, v_stack_m88, 1);
    goto loc_009AFEC3;
loc_009B012F:
    result = CmpUnlockRegistry(*(unsigned __int64 *)(result + 48), 1, v_stack_m88, 1);
    goto loc_009AFD0D;
loc_009B0139:
    result = UNLOCK_HIVE_LOAD(*(unsigned __int64 *)(result + 48), 1, v_stack_m88, 1);
    goto loc_009AFD17;
}
```

## 5. (Beta) C Style

```c
int64_t CmpPerformUnloadKey(void *Arg1, int32_t Arg2, int32_t Arg3, int64_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint32_t v_stack_m118;
    uint64_t v_stack_m40;
    uint64_t v_stack_m50;
    uint64_t v_stack_m5F;
    uint64_t v_stack_m60;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint16_t v_stack_mA6;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint8_t v_stack_mD0;
    uint32_t v_stack_mD4;
    uint8_t v_stack_mD8;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p10;
    uint32_t v_stack_p20;

    v_stack_p10 = local_rbx;
    local_rsp = (local_rsp) - (224);
    result = (*(uint64_t *)(v_rip + 0x45ACF5)) ^ (local_rsp);
    v_stack_m40 = result;
    v_stack_m78 = Arg4;
    v_stack_mB0 = v_stack_mB8;
    local_rbx = 0;
    v_stack_mB8 = v_stack_mB8;
    result = (uint32_t)((v_stack_mB8) | (0xFFFFFFFFULL));
    v_stack_mD8 = 0;
    v_stack_mA8 = v_xmm1;
    v_stack_mA6 = (uint16_t)(result);
    v_stack_m70 = v_xmm0;
    v_stack_m60 = v_xmm0;
    v_stack_m50 = v_xmm0;
    v_stack_m88 = v_xmm0;
    v_stack_mC8 = v_xmm0;
    v_stack_m98 = v_xmm1;
    result = CmpInitializeDelayDerefContext(v_stack_m88, Arg2, Arg3, Arg4);
    result = LOCK_HIVE_LOAD(v_stack_m88, Arg2, Arg3, Arg4);
    result = CmpLockRegistryFreezeAware(1, Arg2, Arg3, Arg4);
    v_stack_mD4 = 6;
    if (sign_flag) goto loc_009AFFA9;
    Arg2 = 0;
    result = CmpPerformKeyBodyDeletionCheck(Arg1, Arg2, Arg3, Arg4);
    if (sign_flag) goto loc_009AFD73;
    if (((*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x8)) & (0x40000ULL)) != 0) goto loc_009AFFB3;
    local_rdi = 0;
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0xB80)) != 0) goto loc_009AFF75;
loc_009AFAFC:
    result = CmpStartKcbStackForTopLayerKcb(v_stack_mA8, *(uint64_t *)(arg1 + 0x8), Arg3, Arg4);
    if (sign_flag) goto loc_009AFFBD;
    if (v_stack_mA6 >= 2) goto loc_009AFF85;
loc_009AFB2C:
    v_stack_mF8 = v_stack_mB8;
    Arg3 = 0;
    result = CmpReportNotifyHelper(v_stack_mA8, *(uint64_t *)(*(uint64_t *)(v_stack_m5F + (int16_t)(v_stack_mA6) * 8 - 0x41) + 0x20), Arg3, 4);
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m5F + (int16_t)(v_stack_mA6) * 8 - 0x41) + 0x20)) != (*(uint64_t *)(v_rip + 0x629F3E))) {
        result = v_stack_mB8;
        Arg4 = 4;
        Arg3 = 0;
        v_stack_mF8 = result;
        Arg1 = v_stack_mA8;
        result = CmpReportNotifyHelper(Arg1, *(uint64_t *)(v_rip + 0x629F3E), Arg3, Arg4);
    }
    if (*(uint64_t *)(arg1 + 0x10) == 0) goto loc_009AFBDD;
    result = *(uint64_t *)(arg1 + 0x10) + 16;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x10)) != (*(uint64_t *)(arg1 + 0x10) + 16)) {
        result = v_stack_mB8;
        Arg4 = 267;
        v_stack_mE8 = result;
        v_stack_mF0 = 0;
        v_stack_mF8 = 0;
        result = CmpPostNotify(*(uint64_t *)(arg1 + 0x10), *(uint64_t *)(v_rip + 0x629F3E), Arg3, Arg4);
    }
    if (*(uint64_t *)(arg1 + 0x10) == 0) goto loc_009AFBDD;
    result = SeReleaseSubjectContext(*(uint64_t *)(arg1 + 0x10) + 56, *(uint64_t *)(v_rip + 0x629F3E), Arg3, Arg4);
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8)) = *(uint64_t *)(*(uint64_t *)(arg1 + 0x10));
    result = *(uint64_t *)(*(uint64_t *)(arg1 + 0x10));
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x10)) != 0) {
        result = *(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8);
        *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10)) + 0x8) = result;
    }
    Arg2 = 0;
    *(uint64_t *)(arg1 + 0x10) = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(arg1 + 0x10), Arg2, Arg3, Arg4);
loc_009AFBDD:
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20)) == (*(uint64_t *)(v_rip + 0x629EA8))) goto loc_009AFFC7;
    if (((*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0xB8)) & ((uint32_t)((uint32_t)(0x40000ULL)))) == 0) goto loc_009AFFC7;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0x1010)))) & (4)) != 0) goto loc_009AFD6B;
    if ((((uint8_t)((uint32_t)(Arg2))) & (1)) != 0) goto loc_009AFD8C;
    result = CmpDoesKeyHaveOpenSubkeys(*(uint64_t *)(arg1 + 0x8), Arg2, Arg3, Arg4);
    if ((uint8_t)(result) != 0) goto loc_009AFF50;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x8))) != 2) goto loc_009AFF50;
loc_009AFC35:
    v_stack_mD8 = 1;
    result = 2;
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0xB80)) == 1) {
        Arg1 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20);
        result = CmpUnfreezeHive(Arg1, Arg2, Arg3, Arg4);
        result = *(uint32_t *)(v_rip + 0x545D54);
        result = (uint32_t)((result) + 1);
        *(uint32_t *)(v_rip + 0x545D4C) = (uint32_t)(result);
    }
    Arg2 = 0;
    result = CmpDrainDelayDerefContext(v_stack_m88, Arg2, Arg3, Arg4);
    result = CmpUnlockRegistry(v_stack_m88, Arg2, Arg3, Arg4);
    result = UNLOCK_HIVE_LOAD(v_stack_m88, Arg2, Arg3, Arg4);
    result = ExWaitForRundownProtectionRelease(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 1640, Arg2, Arg3, Arg4);
    result = LOCK_HIVE_LOAD(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 1640, Arg2, Arg3, Arg4);
    result = CmpLockRegistryFreezeAware(1, Arg2, Arg3, Arg4);
    v_stack_mD4 = 6;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0x1038) != 0) goto loc_009AFE22;
loc_009AFCB2:
    result = CmpAttachToRegistryProcess(v_stack_m70, Arg2, Arg3, Arg4);
    result = CmpCompleteUnloadKey(*(uint64_t *)(arg1 + 0x8), Arg2, v_stack_mD4, Arg4);
    result = CmpDetachFromRegistryProcess(v_stack_m70, Arg2, v_stack_mD4, Arg4);
    local_rdi = 0;
    result = (uint32_t)((result) | (0xFFFFFFFFULL));
    if (((uint32_t)(result)) != 1) goto loc_009AFCFF;
    if ((*(uint64_t *)(v_rip + 0x547E41)) != 0) {
        Arg2 = 0;
        Arg1 = v_rip + 5537334;
        result = ExfUnblockPushLock(Arg1, Arg2, v_stack_mD4, Arg4);
    }
    if (((v_stack_mD4) & (2)) != 0) goto loc_009B012F;
loc_009AFD0D:
    if (((v_stack_mD4) & (4)) != 0) goto loc_009B0139;
loc_009AFD17:
    result = v_stack_mB8;
    if (v_stack_mB8 != v_stack_mB8) {
        Arg1 = v_stack_mB8;
        result = CmpSignalDeferredPosts(Arg1, Arg2, v_stack_mD4, Arg4);
    }
    if (v_stack_m90 != 0) {
        result = CmSiFreeMemory(v_stack_m90, Arg2, v_stack_mD4, Arg4);
    }
    result = CmpCleanupRollbackPacket(v_stack_mC8, Arg2, v_stack_mD4, Arg4);
    Arg1 = (v_stack_m40) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, v_stack_mD4, Arg4);
    local_rsp = (local_rsp) + (224);
    return result;
loc_009AFD6B:
loc_009AFD70:
loc_009AFD73:
    result = LOCK_HIVE_LOAD(Arg1, Arg2, v_stack_mD4, Arg4);
loc_009AFD8C:
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0xC0) == 0) goto loc_009AFDA5;
    result = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0xC0)) + (32);
    if ((*(uint64_t *)(result)) != result) goto loc_009AFEF6;
loc_009AFDA5:
    result = CmpTryAcquireKcbIXLocks(*(uint64_t *)(arg1 + 0x8), 1, v_stack_mD4, v_stack_mC8);
    if (((uint32_t)(result)) == 0xC000022DULL) goto loc_009AFF0A;
    if (sign_flag) goto loc_009AFD70;
    Arg2 = 0;
    result = CmpPrepareForSubtreeInvalidation(*(uint64_t *)(arg1 + 0x8), Arg2, v_stack_mC8, v_stack_mC8);
    if (((uint32_t)(result)) != 0xC000022DULL) goto loc_009B005F;
    Arg2 = 0;
    v_stack_p20 = (uint32_t)((uint32_t)(v_stack_mC8));
    result = CmpLogTransactionAbortedWithChildName(*(uint64_t *)(arg1 + 0x8), Arg2, Arg2 + 10, v_stack_mC8);
    result = CmpUnlockRegistry(*(uint64_t *)(arg1 + 0x8), Arg2, Arg2 + 10, v_stack_mC8);
    result = UNLOCK_HIVE_LOAD(*(uint64_t *)(arg1 + 0x8), Arg2, Arg2 + 10, v_stack_mC8);
    local_rdi = 0;
    local_r15 = 0;
    if (v_stack_mC8 > 0) goto loc_009B0018;
    if (sign_flag) goto loc_009AFD70;
    goto loc_009AFD70;
loc_009AFE22:
    result = CmSnapshotRMTxArray(*(uint64_t *)(arg1 + 0x8), v_stack_mC8, Arg2 + 10, v_stack_mC8);
    if (sign_flag) goto loc_009AFD70;
    Arg2 = 0;
    v_stack_p20 = (uint32_t)((uint32_t)(v_stack_mC8));
    result = CmpLogTransactionAbortedWithChildName(*(uint64_t *)(arg1 + 0x8), Arg2, Arg2 + 9, v_stack_mC8);
    result = CmpUnlockRegistry(*(uint64_t *)(arg1 + 0x8), Arg2, Arg2 + 9, v_stack_mC8);
    result = UNLOCK_HIVE_LOAD(*(uint64_t *)(arg1 + 0x8), Arg2, Arg2 + 9, v_stack_mC8);
    local_rdi = 0;
    local_r15 = 0;
    v_stack_mD0 = 0;
    if (v_stack_mC8 > 0) goto loc_009B009A;
    if (sign_flag) goto loc_009AFD70;
    result = CmpCleanupRollbackPacket(v_stack_mC8, Arg2, Arg2 + 9, v_stack_mC8);
    v_stack_mC8 = v_xmm0;
    if (v_stack_mD0 != 0) goto loc_009B00E1;
loc_009AFE8C:
    result = LOCK_HIVE_LOAD(v_stack_mC8, Arg2, Arg2 + 9, v_stack_mC8);
    local_rdi = 0;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0x1038) != 0) goto loc_009B00F2;
loc_009AFEA3:
    local_rbx = 0;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0x1038) != 0) goto loc_009B010A;
loc_009AFEB5:
    result = UNLOCK_HIVE_LOAD(v_stack_mC8, Arg2, Arg2 + 9, v_stack_mC8);
    if (0 != 0) goto loc_009B0122;
loc_009AFEC3:
    if (0 != 0) {
        Arg1 = 0;
        result = ZwClose(Arg1, Arg2, Arg2 + 9, v_stack_mC8);
    }
    result = LOCK_HIVE_LOAD(Arg1, Arg2, Arg2 + 9, v_stack_mC8);
    result = CmShutdownCmRM(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0x1038), 1, Arg2 + 9, v_stack_mC8);
    result = CmpLockRegistryFreezeAware(1, 1, Arg2 + 9, v_stack_mC8);
    v_stack_mD4 = 6;
    goto loc_009AFCB2;
loc_009AFEF6:
    result = CmpLogUnsupportedOperation(3, 1, Arg2 + 9, v_stack_mC8);
loc_009AFF00:
    goto loc_009AFD70;
loc_009AFF0A:
    Arg2 = 0;
    v_stack_p20 = (uint32_t)((uint32_t)(v_stack_mC8));
    result = CmpLogTransactionAbortedWithChildName(*(uint64_t *)(arg1 + 0x8), Arg2, Arg2 + 10, v_stack_mC8);
    result = CmpUnlockRegistry(*(uint64_t *)(arg1 + 0x8), Arg2, Arg2 + 10, v_stack_mC8);
    result = UNLOCK_HIVE_LOAD(*(uint64_t *)(arg1 + 0x8), Arg2, Arg2 + 10, v_stack_mC8);
    local_rdi = 0;
    local_r15 = 0;
    if (v_stack_mC8 > 0) goto loc_009AFFD1;
    if (sign_flag) goto loc_009AFD73;
    goto loc_009AFD73;
loc_009AFF50:
    if ((uint8_t)((uint8_t)(Arg3)) == 0) goto loc_009AFF00;
    result = CmpFreezeHive(*(uint64_t *)(arg1 + 0x8), v_stack_m78, Arg2 + 10, v_stack_mC8);
    if (sign_flag) goto loc_009AFD70;
    goto loc_009AFCFF;
loc_009AFF75:
    if (((0) & (1)) != 0) goto loc_009AFF98;
loc_009AFF7B:
    goto loc_009AFD73;
loc_009AFF85:
    goto loc_009AFB2C;
loc_009AFF98:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0x1010)))) & (32)) != 0) goto loc_009AFAFC;
    goto loc_009AFF7B;
loc_009AFFA9:
    goto loc_009AFD73;
loc_009AFFB3:
    goto loc_009AFD73;
loc_009AFFBD:
    goto loc_009AFD73;
loc_009AFFC7:
    goto loc_009AFD70;
loc_009AFFD1:
    Arg1 = (*(uint64_t *)(v_stack_mC0 + local_r15 * 8)) & (-2);
    result = CmpRollbackLightWeightTransaction(Arg1, v_stack_m78, Arg2 + 10, v_stack_mC8);
    result = CmpTransDereferenceTransaction(*(uint64_t *)(v_stack_mC0 + local_r15 * 8), v_stack_m78, Arg2 + 10, v_stack_mC8);
loc_009B0018:
    Arg1 = (*(uint64_t *)(v_stack_mC0 + local_r15 * 8)) & (-2);
    result = CmpRollbackLightWeightTransaction(Arg1, v_stack_m78, Arg2 + 10, v_stack_mC8);
    result = CmpTransDereferenceTransaction(*(uint64_t *)(v_stack_mC0 + local_r15 * 8), v_stack_m78, Arg2 + 10, v_stack_mC8);
loc_009B005F:
    if (sign_flag) goto loc_009AFD70;
    result = CmpInvalidateSubtree(*(uint64_t *)(arg1 + 0x8), 1, 1, v_stack_m88);
    result = CmpFlushNotifiesOnKeyBodyList(*(uint64_t *)(arg1 + 0x8), 1, v_stack_m88, 1);
    goto loc_009AFC35;
loc_009B009A:
    Arg1 = (*(uint64_t *)(v_stack_mC0 + local_r15 * 8)) & (-2);
    result = CmpRollbackLightWeightTransaction(Arg1, 1, v_stack_m88, 1);
    result = CmpTransDereferenceTransaction(*(uint64_t *)(v_stack_mC0 + local_r15 * 8), 1, v_stack_m88, 1);
loc_009B00E1:
    result = CmObliterateRMTxArray(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0x1038), 1, v_stack_m88, 1);
    goto loc_009AFE8C;
loc_009B00F2:
    if ((*(uint32_t *)(result + 0x40)) != 1) goto loc_009AFEA3;
    goto loc_009AFEA3;
loc_009B010A:
    if ((*(uint32_t *)(result + 0x40)) != 1) goto loc_009AFEB5;
    goto loc_009AFEB5;
loc_009B0122:
    result = ZwClose(*(uint64_t *)(result + 0x30), 1, v_stack_m88, 1);
    goto loc_009AFEC3;
loc_009B012F:
    result = CmpUnlockRegistry(*(uint64_t *)(result + 0x30), 1, v_stack_m88, 1);
    goto loc_009AFD0D;
loc_009B0139:
    result = UNLOCK_HIVE_LOAD(*(uint64_t *)(result + 0x30), 1, v_stack_m88, 1);
    goto loc_009AFD17;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009AFA28&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
