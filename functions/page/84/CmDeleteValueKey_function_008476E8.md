# CmDeleteValueKey

- RVA: `0x008476E8`–`0x0084837E` (길이 `3,222` bytes)
- VA: `0x00000001408476E8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000692F8`
- 디코드: `760`개 명령, `3,222/3,222` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **99**; 고유 호출 대상: **55**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00847794` → [HvpGetCellContextInitialize](../85/HvpGetCellContextInitialize_function_00855F10.md) (function, `0x00855F10`)
- `0x0084779D` → [HvpGetCellContextInitialize](../85/HvpGetCellContextInitialize_function_00855F10.md) (function, `0x00855F10`)
- `0x008477AC` → [HvpGetCellContextInitialize](../85/HvpGetCellContextInitialize_function_00855F10.md) (function, `0x00855F10`)
- `0x008477BF` → [CmpInitializeDelayDerefContext](../../text/42/CmpInitializeDelayDerefContext_function_0042A7F0.md) (function, `0x0042A7F0`)
- `0x008477D4` → [CmpAttachToRegistryProcess](../../pagecmrc/BC/CmpAttachToRegistryProcess_function_00BC98E0.md) (function, `0x00BC98E0`)
- `0x008477D9` → [CmpIsShutdownRundownActive](../../pagecmrc/BC/CmpIsShutdownRundownActive_function_00BC9C20.md) (function, `0x00BC9C20`)
- `0x008477F3` → [CmpLockRegistry](../../pagecmrc/BC/CmpLockRegistry_function_00BC9B34.md) (function, `0x00BC9B34`)
- `0x0084781D` → [CmpStartKcbStackForTopLayerKcb](CmpStartKcbStackForTopLayerKcb_function_00848390.md) (function, `0x00848390`)
- `0x00847830` → [CmpLockKcbStackTopExclusiveRestShared](CmpLockKcbStackTopExclusiveRestShared_function_00846B04.md) (function, `0x00846B04`)
- `0x00847859` → [CmpIsKeyDeletedForKeyBody](../../pagecmrc/BC/CmpIsKeyDeletedForKeyBody_function_00BC9480.md) (function, `0x00BC9480`)
- `0x008478C4` → [CmpGetEffectiveKcbSemantics](CmpGetEffectiveKcbSemantics_function_00848E20.md) (function, `0x00848E20`)
- `0x00847902` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x00847929` → [CmpFindNameInListWithStatus](CmpFindNameInListWithStatus_function_00846B80.md) (function, `0x00846B80`)
- `0x00847945` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00847965` → [CmpGetEffectiveKcbSemantics](CmpGetEffectiveKcbSemantics_function_00848E20.md) (function, `0x00848E20`)
- `0x008479AA` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x008479B9` → [CmpIsValueTombstone](CmpIsValueTombstone_function_00849900.md) (function, `0x00849900`)
- `0x008479DA` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x008479F7` → [HvLockHiveFlusherShared](HvLockHiveFlusherShared_function_0084F95C.md) (function, `0x0084F95C`)
- `0x00847A16` → [HvpMarkCellDirty](../85/HvpMarkCellDirty_function_00858080.md) (function, `0x00858080`)
- `0x00847A47` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x00847A5C` → [CmpUpdateKeyNodeAccessBits](CmpUpdateKeyNodeAccessBits_function_0084864C.md) (function, `0x0084864C`)
- `0x00847A8E` → [HvpMarkCellDirty](../85/HvpMarkCellDirty_function_00858080.md) (function, `0x00858080`)
- `0x00847AAD` → [HvpMarkCellDirty](../85/HvpMarkCellDirty_function_00858080.md) (function, `0x00858080`)
- `0x00847AC9` → [HvpMarkCellDirty](../85/HvpMarkCellDirty_function_00858080.md) (function, `0x00858080`)
- `0x00847AF6` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x00847B05` → [CmpMarkValueDataDirty](CmpMarkValueDataDirty_function_0084B910.md) (function, `0x0084B910`)
- `0x00847B2F` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00847B4B` → [CmpRemoveValueFromList](../A0/CmpRemoveValueFromList_function_00A0F6D4.md) (function, `0x00A0F6D4`)
- `0x00847B57` → [CmpFreeValue](CmpFreeValue_function_0084AF98.md) (function, `0x0084AF98`)
- `0x00847BA6` → [HvUnlockHiveFlusherShared](HvUnlockHiveFlusherShared_function_00848738.md) (function, `0x00848738`)
- `0x00847BF3` → [CmpReportNotifyHelper](../8C/CmpReportNotifyHelper_function_008C7230.md) (function, `0x008C7230`)
- `0x00847C1A` → [CmpReportNotifyHelper](../8C/CmpReportNotifyHelper_function_008C7230.md) (function, `0x008C7230`)
- `0x00847C4A` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00847C82` → [CmpUnlockKcbStack](CmpUnlockKcbStack_function_00848460.md) (function, `0x00848460`)
- `0x00847C8D` → [CmpDrainDelayDerefContext](../../text/41/CmpDrainDelayDerefContext_function_0041B9A0.md) (function, `0x0041B9A0`)
- `0x00847C99` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x00847CAC` → [CmpSignalDeferredPosts](CmpSignalDeferredPosts_function_008484B0.md) (function, `0x008484B0`)
- `0x00847CB5` → [CmpDetachFromRegistryProcess](../../pagecmrc/BC/CmpDetachFromRegistryProcess_function_00BC9920.md) (function, `0x00BC9920`)
- `0x00847CE5` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (function, `0x00475D80`)
- `0x00847CF3` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00847D19` → [CmpIsKeyDeletedForKeyBody](../../pagecmrc/BC/CmpIsKeyDeletedForKeyBody_function_00BC9480.md) (function, `0x00BC9480`)
- `0x00847D2E` → [CmpTransSearchAddTransFromKeyBody](../87/CmpTransSearchAddTransFromKeyBody_function_008736B8.md) (function, `0x008736B8`)
- `0x00847D99` → [SeAdtRegistryValueChangedAuditAlarm](../79/SeAdtRegistryValueChangedAuditAlarm_function_0079DDD4.md) (function, `0x0079DDD4`)
- `0x00847DA3` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x00847DAD` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x00847DB7` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x00847DC1` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x00847DCF` → [CmpUnlockKcbStack](CmpUnlockKcbStack_function_00848460.md) (function, `0x00848460`)
- `0x00847DE0` → [CmpPromoteKey](CmpPromoteKey_function_00844388.md) (function, `0x00844388`)
- `0x00847E01` → [CmpAllocateUnitOfWork](CmpAllocateUnitOfWork_function_00844BB0.md) (function, `0x00844BB0`)
- `0x00847E1D` → [CmpTransEnlistUowInKcb](../../text/48/CmpTransEnlistUowInKcb_function_0048F094.md) (function, `0x0048F094`)
- `0x00847E28` → [CmpTransEnlistUowInCmTrans](../../text/48/CmpTransEnlistUowInCmTrans_function_0048B330.md) (function, `0x0048B330`)
- `0x00847E41` → [CmpLockIXLockIntent](CmpLockIXLockIntent_function_00844C08.md) (function, `0x00844C08`)
- `0x00847E5E` → [CmpLockIXLockExclusive](CmpLockIXLockExclusive_function_00844CB4.md) (function, `0x00844CB4`)
- `0x00847E6F` → [HvLockHiveFlusherShared](HvLockHiveFlusherShared_function_0084F95C.md) (function, `0x0084F95C`)
- `0x00847E82` → [CmpCloneKCBValueListForTrans](CmpCloneKCBValueListForTrans_function_00844D30.md) (function, `0x00844D30`)
- `0x00847E95` → [HvUnlockHiveFlusherShared](HvUnlockHiveFlusherShared_function_00848738.md) (function, `0x00848738`)
- `0x00847EE0` → [CmpFindNameInListWithStatus](CmpFindNameInListWithStatus_function_00846B80.md) (function, `0x00846B80`)
- `0x00847F07` → [CmpRundownUnitOfWork](../87/CmpRundownUnitOfWork_function_0087497C.md) (function, `0x0087497C`)
- `0x00847F14` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00847F2F` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00847F3D` → [HvUnlockHiveFlusherShared](HvUnlockHiveFlusherShared_function_00848738.md) (function, `0x00848738`)
- `0x00847F5A` → [CmAddLogForAction](CmAddLogForAction_function_008445AC.md) (function, `0x008445AC`)
- `0x00847F70` → [HvLockHiveFlusherShared](HvLockHiveFlusherShared_function_0084F95C.md) (function, `0x0084F95C`)
- `0x00847F84` → [CmpRemoveValueFromList](../A0/CmpRemoveValueFromList_function_00A0F6D4.md) (function, `0x00A0F6D4`)
- `0x00847F97` → [CmpSnapshotTxOwnerArray](CmpSnapshotTxOwnerArray_function_00846808.md) (function, `0x00846808`)
- `0x00847FB7` → [CmpLogTransactionAbortedWithChildName](../9A/CmpLogTransactionAbortedWithChildName_function_009AED70.md) (function, `0x009AED70`)
- `0x00847FC0` → [CmpUnlockKcbStack](CmpUnlockKcbStack_function_00848460.md) (function, `0x00848460`)
- `0x00847FD1` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (function, `0x00475D80`)
- `0x00847FE8` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x00847FFC` → [CmpRollbackTransactionArray](../94/CmpRollbackTransactionArray_function_0094B3AC.md) (function, `0x0094B3AC`)
- `0x00848023` → [CmpDelayDerefKeyControlBlock](CmpDelayDerefKeyControlBlock_function_0084FA50.md) (function, `0x0084FA50`)
- `0x0084803A` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00848044` → [HvpMarkCellDirty](../85/HvpMarkCellDirty_function_00858080.md) (function, `0x00858080`)
- `0x00848082` → [CmpSetValueKeyTombstone](../AC/CmpSetValueKeyTombstone_function_00AC5D64.md) (function, `0x00AC5D64`)
- `0x008480DA` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x008480F2` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x008480FC` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x0084816C` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x0084817A` → [HvFreeCell](../85/HvFreeCell_function_0085A72C.md) (function, `0x0085A72C`)
- `0x008481A0` → [HvpMarkCellDirty](../85/HvpMarkCellDirty_function_00858080.md) (function, `0x00858080`)
- `0x008481C8` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x008481D7` → [CmpMarkValueDataDirty](CmpMarkValueDataDirty_function_0084B910.md) (function, `0x0084B910`)
- `0x008481F2` → [CmpFreeValueData](CmpFreeValueData_function_0084B040.md) (function, `0x0084B040`)
- `0x0084822F` → [CmpGetSecurityCacheEntryForKcbStack](../8C/CmpGetSecurityCacheEntryForKcbStack_function_008C7580.md) (function, `0x008C7580`)
- `0x00848245` → [CmpAllocatePool](../../text/3C/CmpAllocatePool_function_003CD504.md) (function, `0x003CD504`)
- `0x0084827A` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00848284` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x0084828E` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x008482AA` → [CmpSnapshotTxOwnerArray](CmpSnapshotTxOwnerArray_function_00846808.md) (function, `0x00846808`)
- `0x008482C6` → [CmpLogTransactionAbortedWithChildName](../9A/CmpLogTransactionAbortedWithChildName_function_009AED70.md) (function, `0x009AED70`)
- `0x008482CF` → [CmpUnlockKcbStack](CmpUnlockKcbStack_function_00848460.md) (function, `0x00848460`)
- `0x008482DB` → [CmpCleanupKcbStack](../94/CmpCleanupKcbStack_function_009470A0.md) (function, `0x009470A0`)
- `0x008482F8` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00848317` → [CmpGetValueForAudit](../7F/CmpGetValueForAudit_function_007F37C0.md) (function, `0x007F37C0`)
- `0x00848353` → [HvUnlockHiveFlusherShared](HvUnlockHiveFlusherShared_function_00848738.md) (function, `0x00848738`)
- `0x00848362` → [CmpFreePoolWithTag](../../text/44/CmpFreePoolWithTag_function_004489E0.md) (function, `0x004489E0`)
- `0x00848374` → [CmpFreePoolWithTag](../../text/44/CmpFreePoolWithTag_function_004489E0.md) (function, `0x004489E0`)

### Direct callers
- [NtDeleteValueKey](NtDeleteValueKey_function_00848770.md) at `0x00848AF0`

### Static image references
- `0x00847704` → RVA `0x00E0A740` (`.data`; read)
- `0x00847BF8` → RVA `0x00FD9A90` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **20**
  - `0x008477BF` → [CmpInitializeDelayDerefContext](../../text/42/CmpInitializeDelayDerefContext_function_0042A7F0.md) (`PAGE` → `.text`)
  - `0x008477D4` → [CmpAttachToRegistryProcess](../../pagecmrc/BC/CmpAttachToRegistryProcess_function_00BC98E0.md) (`PAGE` → `PAGECMRC`)
  - `0x008477D9` → [CmpIsShutdownRundownActive](../../pagecmrc/BC/CmpIsShutdownRundownActive_function_00BC9C20.md) (`PAGE` → `PAGECMRC`)
  - `0x008477F3` → [CmpLockRegistry](../../pagecmrc/BC/CmpLockRegistry_function_00BC9B34.md) (`PAGE` → `PAGECMRC`)
  - `0x00847859` → [CmpIsKeyDeletedForKeyBody](../../pagecmrc/BC/CmpIsKeyDeletedForKeyBody_function_00BC9480.md) (`PAGE` → `PAGECMRC`)
  - `0x00847C8D` → [CmpDrainDelayDerefContext](../../text/41/CmpDrainDelayDerefContext_function_0041B9A0.md) (`PAGE` → `.text`)
  - `0x00847C99` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x00847CB5` → [CmpDetachFromRegistryProcess](../../pagecmrc/BC/CmpDetachFromRegistryProcess_function_00BC9920.md) (`PAGE` → `PAGECMRC`)
  - `0x00847CE5` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (`PAGE` → `.text`)
  - `0x00847CF3` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x00847D19` → [CmpIsKeyDeletedForKeyBody](../../pagecmrc/BC/CmpIsKeyDeletedForKeyBody_function_00BC9480.md) (`PAGE` → `PAGECMRC`)
  - `0x00847E1D` → [CmpTransEnlistUowInKcb](../../text/48/CmpTransEnlistUowInKcb_function_0048F094.md) (`PAGE` → `.text`)
  - `0x00847E28` → [CmpTransEnlistUowInCmTrans](../../text/48/CmpTransEnlistUowInCmTrans_function_0048B330.md) (`PAGE` → `.text`)
  - `0x00847F14` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00847FD1` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (`PAGE` → `.text`)
  - `0x00847FE8` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x00848245` → [CmpAllocatePool](../../text/3C/CmpAllocatePool_function_003CD504.md) (`PAGE` → `.text`)
  - `0x008482F8` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00848362` → [CmpFreePoolWithTag](../../text/44/CmpFreePoolWithTag_function_004489E0.md) (`PAGE` → `.text`)
  - `0x00848374` → [CmpFreePoolWithTag](../../text/44/CmpFreePoolWithTag_function_004489E0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008476E8  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
008476ED  55                              push rbp
008476EE  56                              push rsi
008476EF  57                              push rdi
008476F0  41 54                           push r12
008476F2  41 55                           push r13
008476F4  41 56                           push r14
008476F6  41 57                           push r15
008476F8  48 8D 6C 24 A0                  lea rbp, [rsp - 0x60]
008476FD  48 81 EC 60 01 00 00            sub rsp, 0x160
00847704  48 8B 05 35 30 5C 00            mov rax, qword ptr [rip + 0x5c3035]
0084770B  48 33 C4                        xor rax, rsp
0084770E  48 89 45 50                     mov qword ptr [rbp + 0x50], rax
00847712  45 33 FF                        xor r15d, r15d
00847715  48 89 4C 24 50                  mov qword ptr [rsp + 0x50], rcx
0084771A  0F 57 C0                        xorps xmm0, xmm0
0084771D  44 88 4C 24 42                  mov byte ptr [rsp + 0x42], r9b
00847722  48 8D 45 D8                     lea rax, [rbp - 0x28]
00847726  4C 89 45 E8                     mov qword ptr [rbp - 0x18], r8
0084772A  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
0084772E  4C 8B E1                        mov r12, rcx
00847731  48 8D 45 D8                     lea rax, [rbp - 0x28]
00847735  48 89 55 D0                     mov qword ptr [rbp - 0x30], rdx
00847739  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
0084773D  48 8D 4D 88                     lea rcx, [rbp - 0x78]
00847741  83 C8 FF                        or eax, 0xffffffff
00847744  44 89 7C 24 68                  mov dword ptr [rsp + 0x68], r15d
00847749  0F 11 45 90                     movups xmmword ptr [rbp - 0x70], xmm0
0084774D  66 89 45 92                     mov word ptr [rbp - 0x6e], ax
00847751  45 8B EF                        mov r13d, r15d
00847754  4C 89 7D C8                     mov qword ptr [rbp - 0x38], r15
00847758  41 8B F7                        mov esi, r15d
0084775B  4C 89 7D 88                     mov qword ptr [rbp - 0x78], r15
0084775F  4C 89 7D B8                     mov qword ptr [rbp - 0x48], r15
00847763  4C 89 7C 24 48                  mov qword ptr [rsp + 0x48], r15
00847768  0F 11 45 20                     movups xmmword ptr [rbp + 0x20], xmm0
0084776C  4C 89 7C 24 60                  mov qword ptr [rsp + 0x60], r15
00847771  0F 11 45 30                     movups xmmword ptr [rbp + 0x30], xmm0
00847775  44 88 7C 24 41                  mov byte ptr [rsp + 0x41], r15b
0084777A  0F 11 45 40                     movups xmmword ptr [rbp + 0x40], xmm0
0084777E  44 89 7D B0                     mov dword ptr [rbp - 0x50], r15d
00847782  0F 11 45 F0                     movups xmmword ptr [rbp - 0x10], xmm0
00847786  4C 89 7C 24 70                  mov qword ptr [rsp + 0x70], r15
0084778B  0F 11 45 A0                     movups xmmword ptr [rbp - 0x60], xmm0
0084778F  4C 89 7C 24 78                  mov qword ptr [rsp + 0x78], r15
00847794  E8 77 E7 00 00                  call 0x140855f10
00847799  48 8D 4D B8                     lea rcx, [rbp - 0x48]
0084779D  E8 6E E7 00 00                  call 0x140855f10
008477A2  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
008477A7  4C 89 7C 24 58                  mov qword ptr [rsp + 0x58], r15
008477AC  E8 5F E7 00 00                  call 0x140855f10
008477B1  83 C8 FF                        or eax, 0xffffffff
008477B4  48 8D 4D F0                     lea rcx, [rbp - 0x10]
008477B8  89 45 80                        mov dword ptr [rbp - 0x80], eax
008477BB  89 44 24 6C                     mov dword ptr [rsp + 0x6c], eax
008477BF  E8 2C 30 BE FF                  call 0x14042a7f0
008477C4  48 8D 4D 20                     lea rcx, [rbp + 0x20]
008477C8  4C 89 7D C0                     mov qword ptr [rbp - 0x40], r15
008477CC  0F 11 45 00                     movups xmmword ptr [rbp], xmm0
008477D0  0F 11 45 10                     movups xmmword ptr [rbp + 0x10], xmm0
008477D4  E8 07 21 38 00                  call 0x140bc98e0
008477D9  E8 42 24 38 00                  call 0x140bc9c20
008477DE  84 C0                           test al, al
008477E0  0F 85 E2 08 00 00               jne 0x1408480c8
008477E6  48 BB 14 00 00 00 80 F7 FF FF   movabs rbx, 0xfffff78000000014
008477F0  48 8B 1B                        mov rbx, qword ptr [rbx]
008477F3  E8 3C 23 38 00                  call 0x140bc9b34
008477F8  49 8B 74 24 08                  mov rsi, qword ptr [r12 + 8]
008477FD  C6 44 24 40 01                  mov byte ptr [rsp + 0x40], 1
00847802  48 8B 46 20                     mov rax, qword ptr [rsi + 0x20]
00847806  F7 80 A0 00 00 00 00 00 10 00   test dword ptr [rax + 0xa0], 0x100000
00847810  0F 85 2F 0B 00 00               jne 0x140848345
00847816  48 8B D6                        mov rdx, rsi
00847819  48 8D 4D 90                     lea rcx, [rbp - 0x70]
0084781D  E8 6E 0B 00 00                  call 0x140848390
00847822  8B F8                           mov edi, eax
00847824  85 C0                           test eax, eax
00847826  0F 88 A6 08 00 00               js 0x1408480d2
0084782C  48 8D 4D 90                     lea rcx, [rbp - 0x70]
00847830  E8 CF F2 FF FF                  call 0x140846b04
00847835  41 B6 01                        mov r14b, 1
00847838  4D 39 7C 24 38                  cmp qword ptr [r12 + 0x38], r15
0084783D  0F 85 D1 04 00 00               jne 0x140847d14
00847843  4D 39 7C 24 40                  cmp qword ptr [r12 + 0x40], r15
00847848  0F 85 C6 04 00 00               jne 0x140847d14
0084784E  4C 8B 74 24 70                  mov r14, qword ptr [rsp + 0x70]
00847853  49 8B CC                        mov rcx, r12
00847856  49 8B D6                        mov rdx, r14
00847859  E8 22 1C 38 00                  call 0x140bc9480
0084785E  84 C0                           test al, al
00847860  0F 85 E6 08 00 00               jne 0x14084814c
00847866  4D 85 F6                        test r14, r14
00847869  0F 85 92 05 00 00               jne 0x140847e01
0084786F  48 8D 8E F8 00 00 00            lea rcx, [rsi + 0xf8]
00847876  44 39 39                        cmp dword ptr [rcx], r15d
00847879  0F 8C 0F 07 00 00               jl 0x140847f8e
0084787F  48 8D 8E 08 01 00 00            lea rcx, [rsi + 0x108]
00847886  44 39 39                        cmp dword ptr [rcx], r15d
00847889  0F 85 12 0A 00 00               jne 0x1408482a1
0084788F  45 33 D2                        xor r10d, r10d
00847892  44 0F B7 66 42                  movzx r12d, word ptr [rsi + 0x42]
00847897  4C 8B 4C 24 50                  mov r9, qword ptr [rsp + 0x50]
0084789C  66 45 85 E4                     test r12w, r12w
008478A0  0F 88 CC 00 00 00               js 0x140847972
008478A6  B8 02 00 00 00                  mov eax, 2
008478AB  4D 0F BF F4                     movsx r14, r12w
008478AF  66 44 3B E0                     cmp r12w, ax
008478B3  0F 8D 2B 08 00 00               jge 0x1408480e4
008478B9  4E 8B 74 F5 98                  mov r14, qword ptr [rbp + r14*8 - 0x68]
008478BE  49 8B D1                        mov rdx, r9
008478C1  49 8B CE                        mov rcx, r14
008478C4  E8 57 15 00 00                  call 0x140848e20
008478C9  83 F8 01                        cmp eax, 1
008478CC  0F 84 A0 00 00 00               je 0x140847972
008478D2  41 8B 56 28                     mov edx, dword ptr [r14 + 0x28]
008478D6  83 FA FF                        cmp edx, -1
008478D9  0F 84 C6 05 00 00               je 0x140847ea5
008478DF  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
008478E4  48 85 C0                        test rax, rax
008478E7  0F 85 C1 05 00 00               jne 0x140847eae
008478ED  49 8B 4E 20                     mov rcx, qword ptr [r14 + 0x20]
008478F1  4C 8D 45 B8                     lea r8, [rbp - 0x48]
008478F5  F6 81 8C 00 00 00 01            test byte ptr [rcx + 0x8c], 1
008478FC  0F 84 A1 04 00 00               je 0x140847da3
00847902  E8 59 D3 00 00                  call 0x140854c60
00847907  4C 8B 45 D0                     mov r8, qword ptr [rbp - 0x30]
0084790B  48 8D 50 24                     lea rdx, [rax + 0x24]
0084790F  49 8B 4E 20                     mov rcx, qword ptr [r14 + 0x20]
00847913  48 8D 45 80                     lea rax, [rbp - 0x80]
00847917  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0084791C  45 33 C9                        xor r9d, r9d
0084791F  48 8D 44 24 6C                  lea rax, [rsp + 0x6c]
00847924  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00847929  E8 52 F2 FF FF                  call 0x140846b80
0084792E  49 8B 4E 20                     mov rcx, qword ptr [r14 + 0x20]
00847932  48 8D 55 B8                     lea rdx, [rbp - 0x48]
00847936  8B F8                           mov edi, eax
00847938  F6 81 8C 00 00 00 01            test byte ptr [rcx + 0x8c], 1
0084793F  0F 85 95 07 00 00               jne 0x1408480da
00847945  E8 F6 E5 00 00                  call 0x140855f40
0084794A  45 33 D2                        xor r10d, r10d
0084794D  85 FF                           test edi, edi
0084794F  0F 89 C4 07 00 00               jns 0x140848119
00847955  81 FF 34 00 00 C0               cmp edi, 0xc0000034
0084795B  75 2C                           jne 0x140847989
0084795D  48 8B 54 24 50                  mov rdx, qword ptr [rsp + 0x50]
00847962  49 8B CE                        mov rcx, r14
00847965  E8 B6 14 00 00                  call 0x140848e20
0084796A  85 C0                           test eax, eax
0084796C  0F 84 26 09 00 00               je 0x140848298
00847972  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
00847977  44 8B 65 80                     mov r12d, dword ptr [rbp - 0x80]
0084797B  41 83 CE FF                     or r14d, 0xffffffff
0084797F  45 3B E6                        cmp r12d, r14d
00847982  75 0D                           jne 0x140847991
00847984  BF 34 00 00 C0                  mov edi, 0xc0000034
00847989  41 B6 01                        mov r14b, 1
0084798C  E9 C3 02 00 00                  jmp 0x140847c54
00847991  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
00847995  4C 8D 44 24 48                  lea r8, [rsp + 0x48]
0084799A  41 8B D4                        mov edx, r12d
0084799D  F6 81 8C 00 00 00 01            test byte ptr [rcx + 0x8c], 1
008479A4  0F 84 03 04 00 00               je 0x140847dad
008479AA  E8 B1 D2 00 00                  call 0x140854c60
008479AF  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
008479B3  48 8B D0                        mov rdx, rax
008479B6  4C 8B E8                        mov r13, rax
008479B9  E8 42 1F 00 00                  call 0x140849900
008479BE  33 FF                           xor edi, edi
008479C0  84 C0                           test al, al
008479C2  0F 85 B9 07 00 00               jne 0x140848181
008479C8  F6 81 8C 00 00 00 01            test byte ptr [rcx + 0x8c], 1
008479CF  48 8D 54 24 48                  lea rdx, [rsp + 0x48]
008479D4  0F 85 18 07 00 00               jne 0x1408480f2
008479DA  E8 61 E5 00 00                  call 0x140855f40
008479DF  4C 8B EF                        mov r13, rdi
008479E2  44 39 76 28                     cmp dword ptr [rsi + 0x28], r14d
008479E6  0F 84 DF 03 00 00               je 0x140847dcb
008479EC  48 8B 4E 20                     mov rcx, qword ptr [rsi + 0x20]
008479F0  48 FF 86 30 01 00 00            inc qword ptr [rsi + 0x130]
008479F7  E8 60 7F 00 00                  call 0x14084f95c
008479FC  4C 8B 74 24 70                  mov r14, qword ptr [rsp + 0x70]
00847A01  41 B7 01                        mov r15b, 1
00847A04  4D 85 F6                        test r14, r14
00847A07  75 26                           jne 0x140847a2f
00847A09  8B 56 28                        mov edx, dword ptr [rsi + 0x28]
00847A0C  45 33 C9                        xor r9d, r9d
00847A0F  48 8B 4E 20                     mov rcx, qword ptr [rsi + 0x20]
00847A13  45 33 C0                        xor r8d, r8d
00847A16  E8 65 06 01 00                  call 0x140858080
00847A1B  8B F8                           mov edi, eax
00847A1D  45 8A F7                        mov r14b, r15b
00847A20  85 C0                           test eax, eax
00847A22  0F 88 27 02 00 00               js 0x140847c4f
00847A28  4C 8B 74 24 70                  mov r14, qword ptr [rsp + 0x70]
00847A2D  33 FF                           xor edi, edi
00847A2F  48 8B 4E 20                     mov rcx, qword ptr [rsi + 0x20]
00847A33  4C 8D 45 88                     lea r8, [rbp - 0x78]
00847A37  8B 56 28                        mov edx, dword ptr [rsi + 0x28]
00847A3A  44 84 B9 8C 00 00 00            test byte ptr [rcx + 0x8c], r15b
00847A41  0F 84 70 03 00 00               je 0x140847db7
00847A47  E8 14 D2 00 00                  call 0x140854c60
00847A4C  44 8B 46 28                     mov r8d, dword ptr [rsi + 0x28]
00847A50  48 8B D0                        mov rdx, rax
00847A53  48 8B 4E 20                     mov rcx, qword ptr [rsi + 0x20]
00847A57  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
00847A5C  E8 EB 0B 00 00                  call 0x14084864c
00847A61  40 38 7C 24 42                  cmp byte ptr [rsp + 0x42], dil
00847A66  0F 85 B9 07 00 00               jne 0x140848225
00847A6C  48 8B 4E 20                     mov rcx, qword ptr [rsi + 0x20]
00847A70  48 39 7C 24 70                  cmp qword ptr [rsp + 0x70], rdi
00847A75  0F 85 A3 04 00 00               jne 0x140847f1e
00847A7B  8B 56 28                        mov edx, dword ptr [rsi + 0x28]
00847A7E  45 33 C9                        xor r9d, r9d
00847A81  45 33 C0                        xor r8d, r8d
00847A84  66 39 7E 42                     cmp word ptr [rsi + 0x42], di
00847A88  0F 85 B6 05 00 00               jne 0x140848044
00847A8E  E8 ED 05 01 00                  call 0x140858080
00847A93  8B F8                           mov edi, eax
00847A95  45 8A F7                        mov r14b, r15b
00847A98  85 C0                           test eax, eax
00847A9A  0F 88 8E 01 00 00               js 0x140847c2e
00847AA0  8B 56 64                        mov edx, dword ptr [rsi + 0x64]
00847AA3  45 33 C9                        xor r9d, r9d
00847AA6  48 8B 4E 20                     mov rcx, qword ptr [rsi + 0x20]
00847AAA  45 33 C0                        xor r8d, r8d
00847AAD  E8 CE 05 01 00                  call 0x140858080
00847AB2  8B F8                           mov edi, eax
00847AB4  85 C0                           test eax, eax
00847AB6  0F 88 72 01 00 00               js 0x140847c2e
00847ABC  48 8B 4E 20                     mov rcx, qword ptr [rsi + 0x20]
00847AC0  45 33 C9                        xor r9d, r9d
00847AC3  45 33 C0                        xor r8d, r8d
00847AC6  41 8B D4                        mov edx, r12d
00847AC9  E8 B2 05 01 00                  call 0x140858080
00847ACE  8B F8                           mov edi, eax
00847AD0  85 C0                           test eax, eax
00847AD2  0F 88 56 01 00 00               js 0x140847c2e
00847AD8  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
00847ADD  4C 8D 44 24 48                  lea r8, [rsp + 0x48]
00847AE2  41 8B D4                        mov edx, r12d
00847AE5  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
00847AE9  44 84 B9 8C 00 00 00            test byte ptr [rcx + 0x8c], r15b
00847AF0  0F 84 CB 02 00 00               je 0x140847dc1
00847AF6  E8 65 D1 00 00                  call 0x140854c60
00847AFB  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
00847AFF  48 8B D0                        mov rdx, rax
00847B02  4C 8B E8                        mov r13, rax
00847B05  E8 06 3E 00 00                  call 0x14084b910
00847B0A  8B F8                           mov edi, eax
00847B0C  85 C0                           test eax, eax
00847B0E  0F 88 0E 01 00 00               js 0x140847c22
00847B14  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00847B19  48 8D 54 24 48                  lea rdx, [rsp + 0x48]
00847B1E  48 8B 49 20                     mov rcx, qword ptr [rcx + 0x20]
00847B22  44 84 B1 8C 00 00 00            test byte ptr [rcx + 0x8c], r14b
00847B29  0F 85 CD 05 00 00               jne 0x1408480fc
00847B2F  E8 0C E4 00 00                  call 0x140855f40
00847B34  4C 8B 74 24 78                  mov r14, qword ptr [rsp + 0x78]
00847B39  45 33 FF                        xor r15d, r15d
00847B3C  8B 54 24 6C                     mov edx, dword ptr [rsp + 0x6c]
00847B40  45 8B EF                        mov r13d, r15d
00847B43  48 8B 4E 20                     mov rcx, qword ptr [rsi + 0x20]
00847B47  4D 8D 46 24                     lea r8, [r14 + 0x24]
00847B4B  E8 84 7B 1C 00                  call 0x140a0f6d4
00847B50  48 8B 4E 20                     mov rcx, qword ptr [rsi + 0x20]
00847B54  41 8B D4                        mov edx, r12d
00847B57  E8 3C 34 00 00                  call 0x14084af98
00847B5C  49 89 5E 04                     mov qword ptr [r14 + 4], rbx
00847B60  48 89 9E A8 00 00 00            mov qword ptr [rsi + 0xa8], rbx
00847B67  45 39 7E 24                     cmp dword ptr [r14 + 0x24], r15d
00847B6B  75 17                           jne 0x140847b84
00847B6D  45 89 7E 3C                     mov dword ptr [r14 + 0x3c], r15d
00847B71  66 44 89 BE B2 00 00 00         mov word ptr [rsi + 0xb2], r15w
00847B79  45 89 7E 40                     mov dword ptr [r14 + 0x40], r15d
00847B7D  44 89 BE B4 00 00 00            mov dword ptr [rsi + 0xb4], r15d
00847B84  F7 86 B8 00 00 00 00 00 40 00   test dword ptr [rsi + 0xb8], 0x400000
00847B8E  0F 84 7C 04 00 00               je 0x140848010
00847B94  41 8B 4E 28                     mov ecx, dword ptr [r14 + 0x28]
00847B98  41 8B 46 24                     mov eax, dword ptr [r14 + 0x24]
00847B9C  89 46 60                        mov dword ptr [rsi + 0x60], eax
00847B9F  89 4E 64                        mov dword ptr [rsi + 0x64], ecx
00847BA2  48 8B 4E 20                     mov rcx, qword ptr [rsi + 0x20]
00847BA6  E8 8D 0B 00 00                  call 0x140848738
00847BAB  33 FF                           xor edi, edi
00847BAD  44 8A FF                        mov r15b, dil
00847BB0  48 89 7C 24 60                  mov qword ptr [rsp + 0x60], rdi
00847BB5  40 88 7C 24 41                  mov byte ptr [rsp + 0x41], dil
00847BBA  8D 47 02                        lea eax, [rdi + 2]
00847BBD  66 39 45 92                     cmp word ptr [rbp - 0x6e], ax
00847BC1  0F AE E8                        lfence
00847BC4  0F 8D 3C 05 00 00               jge 0x140848106
00847BCA  48 0F BF 45 92                  movsx rax, word ptr [rbp - 0x6e]
00847BCF  48 8B 5C C5 98                  mov rbx, qword ptr [rbp + rax*8 - 0x68]
00847BD4  4C 8B 44 24 70                  mov r8, qword ptr [rsp + 0x70]
00847BD9  48 8D 45 D8                     lea rax, [rbp - 0x28]
00847BDD  48 8B 53 20                     mov rdx, qword ptr [rbx + 0x20]
00847BE1  48 8D 4D 90                     lea rcx, [rbp - 0x70]
00847BE5  41 BE 04 00 00 00               mov r14d, 4
00847BEB  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00847BF0  45 8B CE                        mov r9d, r14d
00847BF3  E8 38 F6 07 00                  call 0x1408c7230
00847BF8  48 8B 15 91 1E 79 00            mov rdx, qword ptr [rip + 0x791e91]
00847BFF  48 39 53 20                     cmp qword ptr [rbx + 0x20], rdx
00847C03  74 1A                           je 0x140847c1f
00847C05  4C 8B 44 24 70                  mov r8, qword ptr [rsp + 0x70]
00847C0A  48 8D 45 D8                     lea rax, [rbp - 0x28]
00847C0E  45 8B CE                        mov r9d, r14d
00847C11  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00847C16  48 8D 4D 90                     lea rcx, [rbp - 0x70]
00847C1A  E8 11 F6 07 00                  call 0x1408c7230
00847C1F  41 B6 01                        mov r14b, 1
00847C22  4D 85 ED                        test r13, r13
00847C25  0F 85 38 06 00 00               jne 0x140848263
00847C2B  45 33 ED                        xor r13d, r13d
00847C2E  4C 39 6C 24 78                  cmp qword ptr [rsp + 0x78], r13
00847C33  74 1A                           je 0x140847c4f
00847C35  48 8B 4E 20                     mov rcx, qword ptr [rsi + 0x20]
00847C39  48 8D 55 88                     lea rdx, [rbp - 0x78]
00847C3D  F6 81 8C 00 00 00 01            test byte ptr [rcx + 0x8c], 1
00847C44  0F 85 F0 03 00 00               jne 0x14084803a
00847C4A  E8 F1 E2 00 00                  call 0x140855f40
00847C4F  4C 8B 6C 24 60                  mov r13, qword ptr [rsp + 0x60]
00847C54  4C 8B 64 24 50                  mov r12, qword ptr [rsp + 0x50]
00847C59  4D 85 ED                        test r13, r13
00847C5C  0F 85 A2 02 00 00               jne 0x140847f04
00847C62  45 33 ED                        xor r13d, r13d
00847C65  44 38 6C 24 41                  cmp byte ptr [rsp + 0x41], r13b
00847C6A  0F 85 B6 04 00 00               jne 0x140848126
00847C70  45 84 FF                        test r15b, r15b
00847C73  0F 85 D6 06 00 00               jne 0x14084834f
00847C79  45 84 F6                        test r14b, r14b
00847C7C  74 09                           je 0x140847c87
00847C7E  48 8D 4D 90                     lea rcx, [rbp - 0x70]
00847C82  E8 D9 07 00 00                  call 0x140848460
00847C87  33 D2                           xor edx, edx
00847C89  48 8D 4D F0                     lea rcx, [rbp - 0x10]
00847C8D  E8 0E 3D BD FF                  call 0x14041b9a0
00847C92  44 38 6C 24 40                  cmp byte ptr [rsp + 0x40], r13b
00847C97  74 05                           je 0x140847c9e
00847C99  E8 E6 1D 38 00                  call 0x140bc9a84
00847C9E  48 8D 45 D8                     lea rax, [rbp - 0x28]
00847CA2  48 39 45 D8                     cmp qword ptr [rbp - 0x28], rax
00847CA6  74 09                           je 0x140847cb1
00847CA8  48 8D 4D D8                     lea rcx, [rbp - 0x28]
00847CAC  E8 FF 07 00 00                  call 0x1408484b0
00847CB1  48 8D 4D 20                     lea rcx, [rbp + 0x20]
00847CB5  E8 66 1C 38 00                  call 0x140bc9920
00847CBA  48 8B 5D C0                     mov rbx, qword ptr [rbp - 0x40]
00847CBE  85 FF                           test edi, edi
00847CC0  0F 89 94 00 00 00               jns 0x140847d5a
00847CC6  48 8B 4D 08                     mov rcx, qword ptr [rbp + 8]
00847CCA  48 85 C9                        test rcx, rcx
00847CCD  0F 85 8A 06 00 00               jne 0x14084835d
00847CD3  48 85 DB                        test rbx, rbx
00847CD6  0F 85 90 06 00 00               jne 0x14084836c
00847CDC  48 8B 4D A8                     mov rcx, qword ptr [rbp - 0x58]
00847CE0  48 85 C9                        test rcx, rcx
00847CE3  74 05                           je 0x140847cea
00847CE5  E8 96 E0 C2 FF                  call 0x140475d80
00847CEA  8B C7                           mov eax, edi
00847CEC  48 8B 4D 50                     mov rcx, qword ptr [rbp + 0x50]
00847CF0  48 33 CC                        xor rcx, rsp
00847CF3  E8 48 49 E6 FF                  call 0x1406ac640
00847CF8  48 8B 9C 24 B8 01 00 00         mov rbx, qword ptr [rsp + 0x1b8]
00847D00  48 81 C4 60 01 00 00            add rsp, 0x160
00847D07  41 5F                           pop r15
00847D09  41 5E                           pop r14
00847D0B  41 5D                           pop r13
00847D0D  41 5C                           pop r12
00847D0F  5F                              pop rdi
00847D10  5E                              pop rsi
00847D11  5D                              pop rbp
00847D12  C3                              ret
00847D13  CC                              int3
00847D14  33 D2                           xor edx, edx
00847D16  49 8B CC                        mov rcx, r12
00847D19  E8 62 17 38 00                  call 0x140bc9480
00847D1E  84 C0                           test al, al
00847D20  0F 85 29 04 00 00               jne 0x14084814f
00847D26  48 8D 54 24 70                  lea rdx, [rsp + 0x70]
00847D2B  49 8B CC                        mov rcx, r12
00847D2E  E8 85 B9 02 00                  call 0x1408736b8
00847D33  8B F8                           mov edi, eax
00847D35  85 C0                           test eax, eax
00847D37  0F 88 1C FF FF FF               js 0x140847c59
00847D3D  48 8B 46 20                     mov rax, qword ptr [rsi + 0x20]
00847D41  8B 88 A0 00 00 00               mov ecx, dword ptr [rax + 0xa0]
00847D47  F6 C1 02                        test cl, 2
00847D4A  0F 84 FE FA FF FF               je 0x14084784e
00847D50  BF 01 00 19 C0                  mov edi, 0xc0190001
00847D55  E9 FF FE FF FF                  jmp 0x140847c59
00847D5A  44 38 6C 24 42                  cmp byte ptr [rsp + 0x42], r13b
00847D5F  0F 84 61 FF FF FF               je 0x140847cc6
00847D65  48 85 DB                        test rbx, rbx
00847D68  0F 84 58 FF FF FF               je 0x140847cc6
00847D6E  4C 8B 4D D0                     mov r9, qword ptr [rbp - 0x30]
00847D72  48 8D 45 00                     lea rax, [rbp]
00847D76  C7 44 24 38 02 00 00 00         mov dword ptr [rsp + 0x38], 2
00847D7E  45 33 C0                        xor r8d, r8d
00847D81  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00847D86  48 8B D3                        mov rdx, rbx
00847D89  48 8B 45 E8                     mov rax, qword ptr [rbp - 0x18]
00847D8D  33 C9                           xor ecx, ecx
00847D8F  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00847D94  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00847D99  E8 36 60 F5 FF                  call 0x14079ddd4
00847D9E  E9 23 FF FF FF                  jmp 0x140847cc6
00847DA3  E8 08 CF 00 00                  call 0x140854cb0
00847DA8  E9 5A FB FF FF                  jmp 0x140847907
00847DAD  E8 FE CE 00 00                  call 0x140854cb0
00847DB2  E9 F8 FB FF FF                  jmp 0x1408479af
00847DB7  E8 F4 CE 00 00                  call 0x140854cb0
00847DBC  E9 8B FC FF FF                  jmp 0x140847a4c
00847DC1  E8 EA CE 00 00                  call 0x140854cb0
00847DC6  E9 30 FD FF FF                  jmp 0x140847afb
00847DCB  48 8D 4D 90                     lea rcx, [rbp - 0x70]
00847DCF  E8 8C 06 00 00                  call 0x140848460
00847DD4  41 B0 01                        mov r8b, 1
00847DD7  48 8D 4D 90                     lea rcx, [rbp - 0x70]
00847DDB  33 D2                           xor edx, edx
00847DDD  44 8A F7                        mov r14b, dil
00847DE0  E8 A3 C5 FF FF                  call 0x140844388
00847DE5  4C 8B 6C 24 60                  mov r13, qword ptr [rsp + 0x60]
00847DEA  8B F8                           mov edi, eax
00847DEC  4C 8B 64 24 50                  mov r12, qword ptr [rsp + 0x50]
00847DF1  85 C0                           test eax, eax
00847DF3  0F 88 60 FE FF FF               js 0x140847c59
00847DF9  45 33 FF                        xor r15d, r15d
00847DFC  E9 4D FA FF FF                  jmp 0x14084784e
00847E01  E8 AA CD FF FF                  call 0x140844bb0
00847E06  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00847E0B  4C 8B E8                        mov r13, rax
00847E0E  48 85 C0                        test rax, rax
00847E11  0F 84 21 05 00 00               je 0x140848338
00847E17  48 8B D6                        mov rdx, rsi
00847E1A  48 8B C8                        mov rcx, rax
00847E1D  E8 72 72 C4 FF                  call 0x14048f094
00847E22  49 8B D6                        mov rdx, r14
00847E25  49 8B CD                        mov rcx, r13
00847E28  E8 03 35 C4 FF                  call 0x14048b330
00847E2D  8B F8                           mov edi, eax
00847E2F  85 C0                           test eax, eax
00847E31  0F 88 CA 00 00 00               js 0x140847f01
00847E37  48 8D 8E F8 00 00 00            lea rcx, [rsi + 0xf8]
00847E3E  49 8B D5                        mov rdx, r13
00847E41  E8 C2 CD FF FF                  call 0x140844c08
00847E46  84 C0                           test al, al
00847E48  0F 84 AE 00 00 00               je 0x140847efc
00847E4E  48 8D 8E 08 01 00 00            lea rcx, [rsi + 0x108]
00847E55  41 B8 01 00 00 00               mov r8d, 1
00847E5B  49 8B D5                        mov rdx, r13
00847E5E  E8 51 CE FF FF                  call 0x140844cb4
00847E63  84 C0                           test al, al
00847E65  0F 84 91 00 00 00               je 0x140847efc
00847E6B  48 8B 4E 20                     mov rcx, qword ptr [rsi + 0x20]
00847E6F  E8 E8 7A 00 00                  call 0x14084f95c
00847E74  4C 8D 44 24 41                  lea r8, [rsp + 0x41]
00847E79  49 8B D6                        mov rdx, r14
00847E7C  48 8B CE                        mov rcx, rsi
00847E7F  41 B7 01                        mov r15b, 1
00847E82  E8 A9 CE FF FF                  call 0x140844d30
00847E87  8B F8                           mov edi, eax
00847E89  85 C0                           test eax, eax
00847E8B  0F 88 9F 04 00 00               js 0x140848330
00847E91  48 8B 4E 20                     mov rcx, qword ptr [rsi + 0x20]
00847E95  E8 9E 08 00 00                  call 0x140848738
00847E9A  45 33 D2                        xor r10d, r10d
00847E9D  45 8A FA                        mov r15b, r10b
00847EA0  E9 ED F9 FF FF                  jmp 0x140847892
00847EA5  66 41 FF CC                     dec r12w
00847EA9  E9 EE F9 FF FF                  jmp 0x14084789c
00847EAE  49 39 86 20 01 00 00            cmp qword ptr [r14 + 0x120], rax
00847EB5  0F 85 32 FA FF FF               jne 0x1408478ed
00847EBB  4C 8B 45 D0                     mov r8, qword ptr [rbp - 0x30]
00847EBF  48 8D 45 80                     lea rax, [rbp - 0x80]
00847EC3  49 8B 4E 20                     mov rcx, qword ptr [r14 + 0x20]
00847EC7  49 8D 96 18 01 00 00            lea rdx, [r14 + 0x118]
00847ECE  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00847ED3  45 33 C9                        xor r9d, r9d
00847ED6  48 8D 44 24 6C                  lea rax, [rsp + 0x6c]
00847EDB  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00847EE0  E8 9B EC FF FF                  call 0x140846b80
00847EE5  45 33 D2                        xor r10d, r10d
00847EE8  8B F8                           mov edi, eax
00847EEA  85 C0                           test eax, eax
00847EEC  0F 89 27 02 00 00               jns 0x140848119
00847EF2  3D 34 00 00 C0                  cmp eax, 0xc0000034
00847EF7  E9 5F FA FF FF                  jmp 0x14084795b
00847EFC  BF 01 00 19 C0                  mov edi, 0xc0190001
00847F01  41 B6 01                        mov r14b, 1
00847F04  49 8B CD                        mov rcx, r13
00847F07  E8 70 CA 02 00                  call 0x14087497c
00847F0C  BA 43 4D 55 77                  mov edx, 0x77554d43
00847F11  49 8B CD                        mov rcx, r13
00847F14  E8 57 A9 33 00                  call 0x140b82870
00847F19  E9 44 FD FF FF                  jmp 0x140847c62
00847F1E  48 8D 55 88                     lea rdx, [rbp - 0x78]
00847F22  44 84 B9 8C 00 00 00            test byte ptr [rcx + 0x8c], r15b
00847F29  0F 85 3D 02 00 00               jne 0x14084816c
00847F2F  E8 0C E0 00 00                  call 0x140855f40
00847F34  48 8B 4E 20                     mov rcx, qword ptr [rsi + 0x20]
00847F38  48 89 7C 24 78                  mov qword ptr [rsp + 0x78], rdi
00847F3D  E8 F6 07 00 00                  call 0x140848738
00847F42  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
00847F47  BA 01 00 00 00                  mov edx, 1
00847F4C  44 8A FF                        mov r15b, dil
00847F4F  C7 41 44 06 00 00 00            mov dword ptr [rcx + 0x44], 6
00847F56  44 89 61 58                     mov dword ptr [rcx + 0x58], r12d
00847F5A  E8 4D C6 FF FF                  call 0x1408445ac
00847F5F  8B F8                           mov edi, eax
00847F61  41 B6 01                        mov r14b, 1
00847F64  85 C0                           test eax, eax
00847F66  0F 88 E3 FC FF FF               js 0x140847c4f
00847F6C  48 8B 4E 20                     mov rcx, qword ptr [rsi + 0x20]
00847F70  E8 E7 79 00 00                  call 0x14084f95c
00847F75  8B 54 24 6C                     mov edx, dword ptr [rsp + 0x6c]
00847F79  4C 8D 86 18 01 00 00            lea r8, [rsi + 0x118]
00847F80  48 8B 4E 20                     mov rcx, qword ptr [rsi + 0x20]
00847F84  E8 4B 77 1C 00                  call 0x140a0f6d4
00847F89  E9 14 FC FF FF                  jmp 0x140847ba2
00847F8E  4C 8D 45 C8                     lea r8, [rbp - 0x38]
00847F92  48 8D 54 24 68                  lea rdx, [rsp + 0x68]
00847F97  E8 6C E8 FF FF                  call 0x140846808
00847F9C  8B F8                           mov edi, eax
00847F9E  85 C0                           test eax, eax
00847FA0  0F 88 3F 03 00 00               js 0x1408482e5
00847FA6  8B 5C 24 68                     mov ebx, dword ptr [rsp + 0x68]
00847FAA  33 D2                           xor edx, edx
00847FAC  48 8B CE                        mov rcx, rsi
00847FAF  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
00847FB3  44 8D 42 01                     lea r8d, [rdx + 1]
00847FB7  E8 B4 6D 16 00                  call 0x1409aed70
00847FBC  48 8D 4D 90                     lea rcx, [rbp - 0x70]
00847FC0  E8 9B 04 00 00                  call 0x140848460
00847FC5  48 8B 4D A8                     mov rcx, qword ptr [rbp - 0x58]
00847FC9  45 8A F7                        mov r14b, r15b
00847FCC  48 85 C9                        test rcx, rcx
00847FCF  74 05                           je 0x140847fd6
00847FD1  E8 AA DD C2 FF                  call 0x140475d80
00847FD6  0F 57 C0                        xorps xmm0, xmm0
00847FD9  83 C8 FF                        or eax, 0xffffffff
00847FDC  0F 11 45 90                     movups xmmword ptr [rbp - 0x70], xmm0
00847FE0  66 89 45 92                     mov word ptr [rbp - 0x6e], ax
00847FE4  0F 11 45 A0                     movups xmmword ptr [rbp - 0x60], xmm0
00847FE8  E8 97 1A 38 00                  call 0x140bc9a84
00847FED  48 8B 55 C8                     mov rdx, qword ptr [rbp - 0x38]
00847FF1  4C 8D 4D B0                     lea r9, [rbp - 0x50]
00847FF5  8B CB                           mov ecx, ebx
00847FF7  44 88 7C 24 40                  mov byte ptr [rsp + 0x40], r15b
00847FFC  E8 AB 33 10 00                  call 0x14094b3ac
00848001  8B F8                           mov edi, eax
00848003  85 C0                           test eax, eax
00848005  0F 89 CE F7 FF FF               jns 0x1408477d9
0084800B  E9 49 FC FF FF                  jmp 0x140847c59
00848010  8B 46 08                        mov eax, dword ptr [rsi + 8]
00848013  A8 08                           test al, 8
00848015  0F 84 79 FB FF FF               je 0x140847b94
0084801B  48 8B 4E 68                     mov rcx, qword ptr [rsi + 0x68]
0084801F  48 8D 55 F0                     lea rdx, [rbp - 0x10]
00848023  E8 28 7A 00 00                  call 0x14084fa50
00848028  B8 F7 FF 00 00                  mov eax, 0xfff7
0084802D  4C 89 7E 68                     mov qword ptr [rsi + 0x68], r15
00848031  66 21 46 08                     and word ptr [rsi + 8], ax
00848035  E9 5A FB FF FF                  jmp 0x140847b94
0084803A  E8 E1 4B 01 00                  call 0x14085cc20
0084803F  E9 0B FC FF FF                  jmp 0x140847c4f
00848044  E8 37 00 01 00                  call 0x140858080
00848049  8B F8                           mov edi, eax
0084804B  45 8A F7                        mov r14b, r15b
0084804E  48 3B 74 24 58                  cmp rsi, qword ptr [rsp + 0x58]
00848053  0F 84 32 01 00 00               je 0x14084818b
00848059  85 C0                           test eax, eax
0084805B  0F 88 CD FB FF FF               js 0x140847c2e
00848061  8B 46 28                        mov eax, dword ptr [rsi + 0x28]
00848064  4C 8B 65 D0                     mov r12, qword ptr [rbp - 0x30]
00848068  48 8B 4E 20                     mov rcx, qword ptr [rsi + 0x20]
0084806C  4D 8B C4                        mov r8, r12
0084806F  C1 E8 1F                        shr eax, 0x1f
00848072  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00848076  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
0084807B  48 8B D0                        mov rdx, rax
0084807E  44 8B 48 24                     mov r9d, dword ptr [rax + 0x24]
00848082  E8 DD DC 27 00                  call 0x140ac5d64
00848087  8B F8                           mov edi, eax
00848089  85 C0                           test eax, eax
0084808B  0F 88 9D FB FF FF               js 0x140847c2e
00848091  4C 8B 74 24 78                  mov r14, qword ptr [rsp + 0x78]
00848096  45 33 FF                        xor r15d, r15d
00848099  49 89 5E 04                     mov qword ptr [r14 + 4], rbx
0084809D  48 89 9E A8 00 00 00            mov qword ptr [rsi + 0xa8], rbx
008480A4  41 0F B7 04 24                  movzx eax, word ptr [r12]
008480A9  41 39 46 3C                     cmp dword ptr [r14 + 0x3c], eax
008480AD  0F 83 D1 FA FF FF               jae 0x140847b84
008480B3  41 89 46 3C                     mov dword ptr [r14 + 0x3c], eax
008480B7  41 0F B7 04 24                  movzx eax, word ptr [r12]
008480BC  66 89 86 B2 00 00 00            mov word ptr [rsi + 0xb2], ax
008480C3  E9 BC FA FF FF                  jmp 0x140847b84
008480C8  BF 89 01 00 C0                  mov edi, 0xc0000189
008480CD  44 88 7C 24 40                  mov byte ptr [rsp + 0x40], r15b
008480D2  45 8A F7                        mov r14b, r15b
008480D5  E9 7F FB FF FF                  jmp 0x140847c59
008480DA  E8 41 4B 01 00                  call 0x14085cc20
008480DF  E9 66 F8 FF FF                  jmp 0x14084794a
008480E4  48 8B 45 A8                     mov rax, qword ptr [rbp - 0x58]
008480E8  4E 8B 74 F0 F0                  mov r14, qword ptr [rax + r14*8 - 0x10]
008480ED  E9 CC F7 FF FF                  jmp 0x1408478be
008480F2  E8 29 4B 01 00                  call 0x14085cc20
008480F7  E9 E3 F8 FF FF                  jmp 0x1408479df
008480FC  E8 1F 4B 01 00                  call 0x14085cc20
00848101  E9 2E FA FF FF                  jmp 0x140847b34
00848106  48 0F BF 4D 92                  movsx rcx, word ptr [rbp - 0x6e]
0084810B  48 8B 45 A8                     mov rax, qword ptr [rbp - 0x58]
0084810F  48 8B 5C C8 F0                  mov rbx, qword ptr [rax + rcx*8 - 0x10]
00848114  E9 BB FA FF FF                  jmp 0x140847bd4
00848119  49 8B FE                        mov rdi, r14
0084811C  4C 89 74 24 58                  mov qword ptr [rsp + 0x58], r14
00848121  E9 51 F8 FF FF                  jmp 0x140847977
00848126  8B 96 1C 01 00 00               mov edx, dword ptr [rsi + 0x11c]
0084812C  83 CB FF                        or ebx, 0xffffffff
0084812F  3B D3                           cmp edx, ebx
00848131  75 43                           jne 0x140848176
00848133  89 9E 1C 01 00 00               mov dword ptr [rsi + 0x11c], ebx
00848139  44 89 AE 18 01 00 00            mov dword ptr [rsi + 0x118], r13d
00848140  4C 89 AE 20 01 00 00            mov qword ptr [rsi + 0x120], r13
00848147  E9 24 FB FF FF                  jmp 0x140847c70
0084814C  41 B6 01                        mov r14b, 1
0084814F  41 8A 44 24 30                  mov al, byte ptr [r12 + 0x30]
00848154  41 22 C6                        and al, r14b
00848157  F6 D8                           neg al
00848159  1B FF                           sbb edi, edi
0084815B  81 E7 A9 02 00 00               and edi, 0x2a9
00848161  81 C7 7C 01 00 C0               add edi, 0xc000017c
00848167  E9 ED FA FF FF                  jmp 0x140847c59
0084816C  E8 AF 4A 01 00                  call 0x14085cc20
00848171  E9 BE FD FF FF                  jmp 0x140847f34
00848176  48 8B 4E 20                     mov rcx, qword ptr [rsi + 0x20]
0084817A  E8 AD 25 01 00                  call 0x14085a72c
0084817F  EB B2                           jmp 0x140848133
00848181  BF 34 00 00 C0                  mov edi, 0xc0000034
00848186  E9 94 FA FF FF                  jmp 0x140847c1f
0084818B  85 C0                           test eax, eax
0084818D  0F 88 9B FA FF FF               js 0x140847c2e
00848193  48 8B 4E 20                     mov rcx, qword ptr [rsi + 0x20]
00848197  45 33 C9                        xor r9d, r9d
0084819A  45 33 C0                        xor r8d, r8d
0084819D  41 8B D4                        mov edx, r12d
008481A0  E8 DB FE 00 00                  call 0x140858080
008481A5  8B F8                           mov edi, eax
008481A7  85 C0                           test eax, eax
008481A9  0F 88 7F FA FF FF               js 0x140847c2e
008481AF  48 8B 4E 20                     mov rcx, qword ptr [rsi + 0x20]
008481B3  4C 8D 44 24 48                  lea r8, [rsp + 0x48]
008481B8  41 8B D4                        mov edx, r12d
008481BB  44 84 B1 8C 00 00 00            test byte ptr [rcx + 0x8c], r14b
008481C2  0F 84 BC 00 00 00               je 0x140848284
008481C8  E8 93 CA 00 00                  call 0x140854c60
008481CD  48 8B 4E 20                     mov rcx, qword ptr [rsi + 0x20]
008481D1  48 8B D0                        mov rdx, rax
008481D4  4C 8B E8                        mov r13, rax
008481D7  E8 34 37 00 00                  call 0x14084b910
008481DC  8B F8                           mov edi, eax
008481DE  85 C0                           test eax, eax
008481E0  0F 88 3C FA FF FF               js 0x140847c22
008481E6  45 8B 45 04                     mov r8d, dword ptr [r13 + 4]
008481EA  41 8B 55 08                     mov edx, dword ptr [r13 + 8]
008481EE  48 8B 4E 20                     mov rcx, qword ptr [rsi + 0x20]
008481F2  E8 49 2E 00 00                  call 0x14084b040
008481F7  41 83 4D 08 FF                  or dword ptr [r13 + 8], 0xffffffff
008481FC  45 33 FF                        xor r15d, r15d
008481FF  4C 8B 74 24 78                  mov r14, qword ptr [rsp + 0x78]
00848204  45 89 7D 0C                     mov dword ptr [r13 + 0xc], r15d
00848208  45 89 7D 04                     mov dword ptr [r13 + 4], r15d
0084820C  41 8D 47 02                     lea eax, [r15 + 2]
00848210  66 41 09 45 10                  or word ptr [r13 + 0x10], ax
00848215  49 89 5E 04                     mov qword ptr [r14 + 4], rbx
00848219  48 89 9E A8 00 00 00            mov qword ptr [rsi + 0xa8], rbx
00848220  E9 5F F9 FF FF                  jmp 0x140847b84
00848225  45 33 C0                        xor r8d, r8d
00848228  48 8D 4D 90                     lea rcx, [rbp - 0x70]
0084822C  49 8B D6                        mov rdx, r14
0084822F  E8 4C F3 07 00                  call 0x1408c7580
00848234  B9 00 01 00 00                  mov ecx, 0x100
00848239  41 B8 43 4D 41 32               mov r8d, 0x32414d43
0084823F  48 8B F8                        mov rdi, rax
00848242  8B 50 18                        mov edx, dword ptr [rax + 0x18]
00848245  E8 BA 52 B8 FF                  call 0x1403cd504
0084824A  4C 8B F0                        mov r14, rax
0084824D  48 85 C0                        test rax, rax
00848250  0F 85 97 00 00 00               jne 0x1408482ed
00848256  BF 9A 00 00 C0                  mov edi, 0xc000009a
0084825B  45 8A F7                        mov r14b, r15b
0084825E  E9 CB F9 FF FF                  jmp 0x140847c2e
00848263  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
00848268  48 8D 54 24 48                  lea rdx, [rsp + 0x48]
0084826D  48 8B 48 20                     mov rcx, qword ptr [rax + 0x20]
00848271  F6 81 8C 00 00 00 01            test byte ptr [rcx + 0x8c], 1
00848278  75 14                           jne 0x14084828e
0084827A  E8 C1 DC 00 00                  call 0x140855f40
0084827F  E9 A7 F9 FF FF                  jmp 0x140847c2b
00848284  E8 27 CA 00 00                  call 0x140854cb0
00848289  E9 3F FF FF FF                  jmp 0x1408481cd
0084828E  E8 8D 49 01 00                  call 0x14085cc20
00848293  E9 93 F9 FF FF                  jmp 0x140847c2b
00848298  66 41 FF CC                     dec r12w
0084829C  E9 F6 F5 FF FF                  jmp 0x140847897
008482A1  4C 8D 45 C8                     lea r8, [rbp - 0x38]
008482A5  48 8D 54 24 68                  lea rdx, [rsp + 0x68]
008482AA  E8 59 E5 FF FF                  call 0x140846808
008482AF  8B F8                           mov edi, eax
008482B1  85 C0                           test eax, eax
008482B3  78 30                           js 0x1408482e5
008482B5  8B 5C 24 68                     mov ebx, dword ptr [rsp + 0x68]
008482B9  33 D2                           xor edx, edx
008482BB  48 8B CE                        mov rcx, rsi
008482BE  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
008482C2  44 8D 42 01                     lea r8d, [rdx + 1]
008482C6  E8 A5 6A 16 00                  call 0x1409aed70
008482CB  48 8D 4D 90                     lea rcx, [rbp - 0x70]
008482CF  E8 8C 01 00 00                  call 0x140848460
008482D4  48 8D 4D 90                     lea rcx, [rbp - 0x70]
008482D8  45 8A F7                        mov r14b, r15b
008482DB  E8 C0 ED 0F 00                  call 0x1409470a0
008482E0  E9 F1 FC FF FF                  jmp 0x140847fd6
008482E5  41 B6 01                        mov r14b, 1
008482E8  E9 6C F9 FF FF                  jmp 0x140847c59
008482ED  44 8B 47 18                     mov r8d, dword ptr [rdi + 0x18]
008482F1  48 8D 57 20                     lea rdx, [rdi + 0x20]
008482F5  49 8B CE                        mov rcx, r14
008482F8  E8 43 E5 E7 FF                  call 0x1406c6840
008482FD  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00848302  4C 8D 45 00                     lea r8, [rbp]
00848306  41 B9 43 4D 41 31               mov r9d, 0x31414d43
0084830C  4C 89 75 C0                     mov qword ptr [rbp - 0x40], r14
00848310  41 8B D4                        mov edx, r12d
00848313  48 8B 49 20                     mov rcx, qword ptr [rcx + 0x20]
00848317  E8 A4 B4 FA FF                  call 0x1407f37c0
0084831C  8B F8                           mov edi, eax
0084831E  45 8A F7                        mov r14b, r15b
00848321  85 C0                           test eax, eax
00848323  0F 88 05 F9 FF FF               js 0x140847c2e
00848329  33 FF                           xor edi, edi
0084832B  E9 3C F7 FF FF                  jmp 0x140847a6c
00848330  45 8A F7                        mov r14b, r15b
00848333  E9 CC FB FF FF                  jmp 0x140847f04
00848338  BF 9A 00 00 C0                  mov edi, 0xc000009a
0084833D  41 B6 01                        mov r14b, 1
00848340  E9 1D F9 FF FF                  jmp 0x140847c62
00848345  BF 22 00 00 C0                  mov edi, 0xc0000022
0084834A  E9 83 FD FF FF                  jmp 0x1408480d2
0084834F  48 8B 4E 20                     mov rcx, qword ptr [rsi + 0x20]
00848353  E8 E0 03 00 00                  call 0x140848738
00848358  E9 1C F9 FF FF                  jmp 0x140847c79
0084835D  BA 43 4D 41 34                  mov edx, 0x34414d43
00848362  E8 79 06 C0 FF                  call 0x1404489e0
00848367  E9 67 F9 FF FF                  jmp 0x140847cd3
0084836C  BA 43 4D 41 33                  mov edx, 0x33414d43
00848371  48 8B CB                        mov rcx, rbx
00848374  E8 67 06 C0 FF                  call 0x1404489e0
00848379  E9 5E F9 FF FF                  jmp 0x140847cdc
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmDeleteValueKey(__int64 a1, __int64 a2, __int64 a3, unsigned __int8 a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int16 v_stack_m106;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned int v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned int v_stack_m12C;
    unsigned int v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m150;
    unsigned __int8 v_stack_m156;
    unsigned __int8 v_stack_m157;
    unsigned __int8 v_stack_m158;
    unsigned __int64 v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned int v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned int v_stack_p38;
    unsigned __int8 v_stack_p40;
    unsigned __int64 v_stack_p41;
    unsigned __int8 v_stack_p42;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p6C;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;

    v_stack_p20 = v_rbx;
    v_rsp = (v_rsp) - (352);
    result = (*(unsigned __int64 *)(v_rip + 6041653)) ^ (v_rsp);
    v_stack_m48 = result;
    v_r15 = 0;
    v_stack_m148 = a1;
    v_stack_m156 = a4;
    v_stack_mB0 = a3;
    v_stack_mB8 = v_stack_mC0;
    v_stack_mC8 = a2;
    v_stack_mC0 = v_stack_mC0;
    result = (unsigned int)((v_stack_mC0) | (0xFFFFFFFFULL));
    v_stack_m130 = 0;
    v_stack_m108 = v_xmm0;
    v_stack_m106 = (unsigned __int16)(result);
    v_stack_mD0 = 0;
    v_stack_m110 = 0;
    v_stack_mE0 = 0;
    v_stack_m150 = 0;
    v_stack_m78 = v_xmm0;
    v_stack_m138 = 0;
    v_stack_m68 = v_xmm0;
    v_stack_m157 = 0;
    v_stack_m58 = v_xmm0;
    v_stack_mE8 = 0;
    v_stack_mA8 = v_xmm0;
    v_stack_m128 = 0;
    v_stack_mF8 = v_xmm0;
    v_stack_m120 = 0;
    result = HvpGetCellContextInitialize(v_stack_m110, a2, a3, a4);
    result = HvpGetCellContextInitialize(v_stack_mE0, a2, a3, a4);
    v_stack_m140 = 0;
    result = HvpGetCellContextInitialize(v_stack_m150, a2, a3, a4);
    result = (unsigned int)((result) | (0xFFFFFFFFULL));
    v_stack_m118 = (unsigned int)(result);
    v_stack_m12C = (unsigned int)(result);
    result = CmpInitializeDelayDerefContext(v_stack_mA8, a2, a3, a4);
    v_stack_mD8 = 0;
    v_stack_m98 = v_xmm0;
    v_stack_m88 = v_xmm0;
    result = CmpAttachToRegistryProcess(v_stack_m78, a2, a3, a4);
loc_008477D9:
    result = CmpIsShutdownRundownActive(v_stack_m78, a2, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_008480C8;
    result = CmpLockRegistry(v_stack_m78, a2, a3, a4);
    v_stack_m158 = 1;
    if (((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 160)) & (0x100000ULL)) != 0) goto loc_00848345;
    result = CmpStartKcbStackForTopLayerKcb(v_stack_m108, *(unsigned __int64 *)(a1 + 8), a3, a4);
    if (sign_flag) goto loc_008480D2;
    result = CmpLockKcbStackTopExclusiveRestShared(v_stack_m108, *(unsigned __int64 *)(a1 + 8), a3, a4);
    if ((*(unsigned __int64 *)(a1 + 56)) != 0) goto loc_00847D14;
    if ((*(unsigned __int64 *)(a1 + 64)) != 0) goto loc_00847D14;
loc_0084784E:
    result = CmpIsKeyDeletedForKeyBody(a1, v_stack_m128, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_0084814C;
    if (v_stack_m128 != 0) goto loc_00847E01;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 248)) < 0) goto loc_00847F8E;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 264)) != 0) goto loc_008482A1;
    v_r10 = 0;
loc_00847892:
loc_00847897:
loc_0084789C:
    if (sign_flag) goto loc_00847972;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 66))) >= 2) goto loc_008480E4;
loc_008478BE:
    result = CmpGetEffectiveKcbSemantics(*(unsigned __int64 *)(v_stack_m98 + (__int16)((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 66))) * 8 - 104), v_stack_m148, a3, v_stack_m148);
    if (((unsigned int)(result)) == 1) goto loc_00847972;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m98 + (__int16)((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 66))) * 8 - 104) + 40)))) == -1) goto loc_00847EA5;
    if (v_stack_m128 != 0) goto loc_00847EAE;
loc_008478ED:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m98 + (__int16)((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 66))) * 8 - 104) + 32) + 140)) & (1)) == 0) goto loc_00847DA3;
    result = HvpGetCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m98 + (__int16)((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 66))) * 8 - 104) + 32), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m98 + (__int16)((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 66))) * 8 - 104) + 40)), v_stack_mE0, v_stack_m148);
loc_00847907:
    v_stack_m170 = v_stack_m118;
    a4 = 0;
    v_stack_m178 = v_stack_m12C;
    result = CmpFindNameInListWithStatus(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m98 + (__int16)((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 66))) * 8 - 104) + 32), result + 36, v_stack_mC8, a4);
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m98 + (__int16)((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 66))) * 8 - 104) + 32) + 140)) & (1)) != 0) goto loc_008480DA;
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m98 + (__int16)((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 66))) * 8 - 104) + 32), v_stack_mE0, v_stack_mC8, a4);
loc_0084794A:
    v_r10 = 0;
    if (!sign_flag) goto loc_00848119;
loc_0084795B:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != 0xC0000034ULL) goto loc_00847989;
    result = CmpGetEffectiveKcbSemantics(*(unsigned __int64 *)(v_stack_m98 + (__int16)((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 66))) * 8 - 104), v_stack_m148, v_stack_mC8, a4);
    if ((unsigned int)(result) == 0) goto loc_00848298;
loc_00847972:
loc_00847977:
    v_r14 = (unsigned int)((*(unsigned __int64 *)(v_stack_m98 + (__int16)((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 66))) * 8 - 104)) | (0xFFFFFFFFULL));
    if (((unsigned int)((unsigned int)(v_stack_m118))) != ((unsigned int)(v_r14))) goto loc_00847991;
loc_00847989:
    goto loc_00847C54;
loc_00847991:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)((unsigned int)(0xC0000034ULL) + 32) + 140)) & (1)) == 0) goto loc_00847DAD;
    result = HvpGetCellFlat(*(unsigned __int64 *)((unsigned int)(0xC0000034ULL) + 32), (unsigned int)((unsigned int)((unsigned int)(v_stack_m118))), v_stack_m150, a4);
loc_008479AF:
    result = CmpIsValueTombstone(*(unsigned __int64 *)((unsigned int)(0xC0000034ULL) + 32), result, v_stack_m150, a4);
    v_rdi = 0;
    if ((unsigned __int8)(result) != 0) goto loc_00848181;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)((unsigned int)(0xC0000034ULL) + 32) + 140)) & (1)) != 0) goto loc_008480F2;
    result = HvpReleaseCellPaged(*(unsigned __int64 *)((unsigned int)(0xC0000034ULL) + 32), v_stack_m150, v_stack_m150, a4);
loc_008479DF:
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 40)) == 1) goto loc_00847DCB;
    result = HvLockHiveFlusherShared(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), v_stack_m150, v_stack_m150, a4);
    if (v_stack_m128 != 0) goto loc_00847A2F;
    a4 = 0;
    a3 = 0;
    result = HvpMarkCellDirty(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 40)), a3, a4);
    if (sign_flag) goto loc_00847C4F;
    v_rdi = 0;
loc_00847A2F:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 140)) & (1)) == 0) goto loc_00847DB7;
    result = HvpGetCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 40)), v_stack_m110, a4);
loc_00847A4C:
    v_stack_m120 = result;
    result = CmpUpdateKeyNodeAccessBits(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), result, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 40)), a4);
    if (v_stack_m156 != 0) goto loc_00848225;
loc_00847A6C:
    if (v_stack_m128 != 0) goto loc_00847F1E;
    a4 = 0;
    a3 = 0;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 66)) != 0) goto loc_00848044;
    result = HvpMarkCellDirty(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 40)), a3, a4);
    if (sign_flag) goto loc_00847C2E;
    a4 = 0;
    a3 = 0;
    result = HvpMarkCellDirty(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 100)), a3, a4);
    if (sign_flag) goto loc_00847C2E;
    a4 = 0;
    a3 = 0;
    result = HvpMarkCellDirty(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), (unsigned int)((unsigned int)((unsigned int)(v_stack_m118))), a3, a4);
    if (sign_flag) goto loc_00847C2E;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m140 + 32) + 140)) & (1)) == 0) goto loc_00847DC1;
    result = HvpGetCellFlat(*(unsigned __int64 *)(v_stack_m140 + 32), (unsigned int)((unsigned int)((unsigned int)(v_stack_m118))), v_stack_m150, a4);
loc_00847AFB:
    result = CmpMarkValueDataDirty(*(unsigned __int64 *)(v_stack_m140 + 32), result, v_stack_m150, a4);
    if (sign_flag) goto loc_00847C22;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m140 + 32) + 140)) & (1)) != 0) goto loc_008480FC;
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(v_stack_m140 + 32), v_stack_m150, v_stack_m150, a4);
loc_00847B34:
    v_r15 = 0;
    result = CmpRemoveValueFromList(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), (unsigned int)(v_stack_m12C), v_stack_m120 + 36, a4);
    result = CmpFreeValue(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), (unsigned int)((unsigned int)((unsigned int)(v_stack_m118))), v_stack_m120 + 36, a4);
    *(unsigned __int64 *)(v_stack_m120 + 4) = *(unsigned __int64 *)(v_rbx);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 168) = *(unsigned __int64 *)(v_rbx);
    if ((*(unsigned int *)(v_stack_m120 + 36)) == 0) {
        *(unsigned int *)(v_stack_m120 + 60) = 0;
        *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 178) = 0;
        *(unsigned int *)(v_stack_m120 + 64) = 0;
        *(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 180) = 0;
    }
    if (((*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 184)) & (0x400000ULL)) == 0) goto loc_00848010;
loc_00847B94:
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 96) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m120 + 36)));
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 100) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m120 + 40)));
loc_00847BA2:
    result = HvUnlockHiveFlusherShared(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), (unsigned int)((unsigned int)((unsigned int)(v_stack_m118))), v_stack_m120 + 36, a4);
    v_rdi = 0;
    v_stack_m138 = 0;
    v_stack_m157 = 0;
    if (v_stack_m106 >= ((unsigned __int16)(v_rdi + 2))) goto loc_00848106;
loc_00847BD4:
    v_stack_m178 = v_stack_mC0;
    result = CmpReportNotifyHelper(v_stack_m108, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m98 + (__int16)(v_stack_m106) * 8 - 104) + 32), v_stack_m128, 4);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m98 + (__int16)(v_stack_m106) * 8 - 104) + 32)) != (*(unsigned __int64 *)(v_rip + 7937681))) {
        a3 = v_stack_m128;
        result = v_stack_mC0;
        a4 = 4;
        v_stack_m178 = result;
        a1 = v_stack_m108;
        result = CmpReportNotifyHelper(a1, *(unsigned __int64 *)(v_rip + 7937681), a3, a4);
    }
loc_00847C22:
    if (0 != 0) goto loc_00848263;
loc_00847C2B:
    v_r13 = 0;
loc_00847C2E:
    if (v_stack_m120 == 0) goto loc_00847C4F;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 140)) & (1)) != 0) goto loc_0084803A;
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), v_stack_m110, a3, a4);
loc_00847C4F:
loc_00847C54:
loc_00847C59:
    if (v_stack_m138 != 0) goto loc_00847F04;
loc_00847C62:
    v_r13 = 0;
    if (v_stack_m157 != 0) goto loc_00848126;
loc_00847C70:
    if (0 != 0) goto loc_0084834F;
loc_00847C79:
    if (1 != 0) {
        a1 = v_stack_m108;
        result = CmpUnlockKcbStack(a1, v_stack_m110, a3, a4);
    }
    a2 = 0;
    result = CmpDrainDelayDerefContext(v_stack_mA8, a2, a3, a4);
    if (v_stack_m158 != 0) {
        result = CmpUnlockRegistry(v_stack_mA8, a2, a3, a4);
    }
    result = v_stack_mC0;
    if (v_stack_mC0 != v_stack_mC0) {
        a1 = v_stack_mC0;
        result = CmpSignalDeferredPosts(a1, a2, a3, a4);
    }
    result = CmpDetachFromRegistryProcess(v_stack_m78, a2, a3, a4);
    if (!sign_flag) goto loc_00847D5A;
loc_00847CC6:
    if (v_stack_m90 != 0) goto loc_0084835D;
loc_00847CD3:
    if (v_stack_mD8 != 0) goto loc_0084836C;
loc_00847CDC:
    if (v_stack_mF0 != 0) {
        result = CmSiFreeMemory(v_stack_mF0, a2, a3, a4);
    }
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (352);
    return result;
loc_00847D14:
    a2 = 0;
    result = CmpIsKeyDeletedForKeyBody(v_stack_m148, a2, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_0084814F;
    result = CmpTransSearchAddTransFromKeyBody(v_stack_m148, v_stack_p70, a3, a4);
    if (sign_flag) goto loc_00847C59;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 160)))) & (2)) == 0) goto loc_0084784E;
    goto loc_00847C59;
loc_00847D5A:
    if (v_stack_p42 == 0) goto loc_00847CC6;
    if (v_stack_p20 == 0) goto loc_00847CC6;
    v_stack_p38 = 2;
    a3 = 0;
    v_stack_p30 = v_stack_m98;
    a1 = 0;
    v_stack_p28 = v_stack_mB0;
    v_stack_p20 = v_stack_m148;
    result = SeAdtRegistryValueChangedAuditAlarm(a1, v_stack_p20, a3, v_stack_mC8);
    goto loc_00847CC6;
loc_00847DA3:
    result = HvpGetCellPaged(a1, v_stack_p20, a3, v_stack_mC8);
    goto loc_00847907;
loc_00847DAD:
    result = HvpGetCellPaged(a1, v_stack_p20, a3, v_stack_mC8);
    goto loc_008479AF;
loc_00847DB7:
    result = HvpGetCellPaged(a1, v_stack_p20, a3, v_stack_mC8);
    goto loc_00847A4C;
loc_00847DC1:
    result = HvpGetCellPaged(a1, v_stack_p20, a3, v_stack_mC8);
    goto loc_00847AFB;
loc_00847DCB:
    result = CmpUnlockKcbStack(v_stack_m108, v_stack_p20, a3, v_stack_mC8);
    a2 = 0;
    result = CmpPromoteKey(v_stack_m108, a2, 1, v_stack_mC8);
    if (sign_flag) goto loc_00847C59;
    v_r15 = 0;
    goto loc_0084784E;
loc_00847E01:
    result = CmpAllocateUnitOfWork(v_stack_m108, a2, 1, v_stack_mC8);
    v_stack_p60 = result;
    if (result == 0) goto loc_00848338;
    result = CmpTransEnlistUowInKcb(result, *(unsigned __int64 *)(a1 + 8), 1, v_stack_mC8);
    result = CmpTransEnlistUowInCmTrans(result, (unsigned __int8)((unsigned int)(0xC0190001ULL)), 1, v_stack_mC8);
    if (sign_flag) goto loc_00847F01;
    result = CmpLockIXLockIntent(*(unsigned __int64 *)(a1 + 8) + 248, result, 1, v_stack_mC8);
    if ((unsigned __int8)(result) == 0) goto loc_00847EFC;
    result = CmpLockIXLockExclusive(*(unsigned __int64 *)(a1 + 8) + 264, result, 1, v_stack_mC8);
    if ((unsigned __int8)(result) == 0) goto loc_00847EFC;
    result = HvLockHiveFlusherShared(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), result, 1, v_stack_mC8);
    result = CmpCloneKCBValueListForTrans(*(unsigned __int64 *)(a1 + 8), (unsigned __int8)((unsigned int)(0xC0190001ULL)), v_stack_p41, v_stack_mC8);
    if (sign_flag) goto loc_00848330;
    result = HvUnlockHiveFlusherShared(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), (unsigned __int8)((unsigned int)(0xC0190001ULL)), v_stack_p41, v_stack_mC8);
    v_r10 = 0;
    goto loc_00847892;
loc_00847EA5:
    v_r12 = (unsigned __int16)((v_stack_p50) - 1);
    goto loc_0084789C;
loc_00847EAE:
    if ((*(unsigned __int64 *)((unsigned __int8)((unsigned int)(0xC0190001ULL)) + 288)) != result) goto loc_008478ED;
    v_stack_p28 = v_stack_m118;
    a4 = 0;
    v_stack_p20 = v_stack_p6C;
    result = CmpFindNameInListWithStatus(*(unsigned __int64 *)((unsigned __int8)((unsigned int)(0xC0190001ULL)) + 32), (unsigned __int8)((unsigned int)(0xC0190001ULL)) + 280, v_stack_mC8, a4);
    v_r10 = 0;
    if (!sign_flag) goto loc_00848119;
    goto loc_0084795B;
loc_00847EFC:
loc_00847F01:
loc_00847F04:
    result = CmpRundownUnitOfWork(result, (unsigned __int8)((unsigned int)(0xC0190001ULL)) + 280, v_stack_mC8, a4);
    result = ExFreePoolWithTag(result, (unsigned int)(0x77554D43ULL), v_stack_mC8, a4);
    goto loc_00847C62;
loc_00847F1E:
    if (((*(unsigned __int8 *)(result + 140)) & (0)) != 0) goto loc_0084816C;
    result = HvpReleaseCellPaged(result, v_stack_m110, v_stack_mC8, a4);
loc_00847F34:
    v_stack_p78 = (unsigned int)(0xC0190001ULL);
    result = HvUnlockHiveFlusherShared(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), v_stack_m110, v_stack_mC8, a4);
    *(unsigned int *)(v_stack_p60 + 68) = 6;
    *(unsigned int *)(v_stack_p60 + 88) = (unsigned int)(v_r12);
    result = CmAddLogForAction(v_stack_p60, 1, v_stack_mC8, a4);
    if (sign_flag) goto loc_00847C4F;
    result = HvLockHiveFlusherShared(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), 1, v_stack_mC8, a4);
    result = CmpRemoveValueFromList(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), (unsigned int)(v_stack_p6C), *(unsigned __int64 *)(a1 + 8) + 280, a4);
    goto loc_00847BA2;
loc_00847F8E:
    result = CmpSnapshotTxOwnerArray(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), v_stack_p68, v_stack_mD0, a4);
    if (sign_flag) goto loc_008482E5;
    a2 = 0;
    v_stack_p20 = (unsigned int)((unsigned int)(v_stack_p68));
    result = CmpLogTransactionAbortedWithChildName(*(unsigned __int64 *)(a1 + 8), a2, a2 + 1, a4);
    result = CmpUnlockKcbStack(v_stack_m108, a2, a2 + 1, a4);
    if (v_stack_mF0 != 0) {
        result = CmSiFreeMemory(v_stack_mF0, a2, a2 + 1, a4);
    }
    result = (unsigned int)((result) | (0xFFFFFFFFULL));
    v_stack_m108 = v_xmm0;
    v_stack_m106 = (unsigned __int16)(result);
    v_stack_mF8 = v_xmm0;
    result = CmpUnlockRegistry(v_stack_mF0, a2, a2 + 1, a4);
    v_stack_p40 = (unsigned __int8)((unsigned __int8)((unsigned int)(0xC0190001ULL)));
    result = CmpRollbackTransactionArray((unsigned int)((unsigned int)((unsigned int)(v_stack_p68))), v_stack_mD0, a2 + 1, v_stack_mE8);
    if (!sign_flag) goto loc_008477D9;
    goto loc_00847C59;
loc_00848010:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 8)))) & (8)) == 0) goto loc_00847B94;
    result = CmpDelayDerefKeyControlBlock(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 104), v_stack_mA8, a2 + 1, v_stack_mE8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 104) = (unsigned __int8)((unsigned int)(0xC0190001ULL));
    goto loc_00847B94;
loc_0084803A:
    result = HvpReleaseCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 104), v_stack_mA8, a2 + 1, v_stack_mE8);
    goto loc_00847C4F;
loc_00848044:
    result = HvpMarkCellDirty(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 104), v_stack_mA8, a2 + 1, v_stack_mE8);
    if ((*(unsigned __int64 *)(a1 + 8)) == v_stack_p58) goto loc_0084818B;
    if (sign_flag) goto loc_00847C2E;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 40))) >> (31));
    v_stack_p20 = (unsigned int)(result);
    result = CmpSetValueKeyTombstone(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), v_stack_p78, v_stack_mC8, (unsigned int)(*(unsigned int *)(v_stack_p78 + 36)));
    if (sign_flag) goto loc_00847C2E;
    v_r15 = 0;
    *(unsigned __int64 *)(v_stack_p78 + 4) = (unsigned int)(v_stack_p68);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 168) = (unsigned int)(v_stack_p68);
    if ((*(unsigned int *)(v_stack_p78 + 60)) >= ((unsigned int)(*(unsigned __int16 *)(v_stack_mC8)))) goto loc_00847B84;
    *(unsigned int *)(v_stack_p78 + 60) = (unsigned int)(*(unsigned __int16 *)(v_stack_mC8));
    *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 178) = (unsigned __int16)(*(unsigned __int16 *)(v_stack_mC8));
    goto loc_00847B84;
loc_008480C8:
    v_stack_p40 = 0;
loc_008480D2:
    goto loc_00847C59;
loc_008480DA:
    result = HvpReleaseCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), v_stack_p78, v_stack_mC8, (unsigned int)(*(unsigned int *)(v_stack_p78 + 36)));
    goto loc_0084794A;
loc_008480E4:
    goto loc_008478BE;
loc_008480F2:
    result = HvpReleaseCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), v_stack_p78, v_stack_mC8, (unsigned int)(*(unsigned int *)(v_stack_p78 + 36)));
    goto loc_008479DF;
loc_008480FC:
    result = HvpReleaseCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), v_stack_p78, v_stack_mC8, (unsigned int)(*(unsigned int *)(v_stack_p78 + 36)));
    goto loc_00847B34;
loc_00848106:
    goto loc_00847BD4;
loc_00848119:
    v_stack_p58 = *(unsigned __int64 *)(v_stack_mF0 + 0 * 8 - 16);
    goto loc_00847977;
loc_00848126:
    v_rbx = (unsigned int)((*(unsigned __int64 *)(v_stack_mF0 + (__int16)(v_stack_m106) * 8 - 16)) | (0xFFFFFFFFULL));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 284)))) != ((unsigned int)(v_rbx))) goto loc_00848176;
loc_00848133:
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 284) = (unsigned int)(v_rbx);
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 280) = (unsigned int)(result);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 288) = result;
    goto loc_00847C70;
loc_0084814C:
loc_0084814F:
    result = (unsigned __int8)((*(unsigned __int8 *)(v_stack_mC8 + 48)) & (1));
    result = (unsigned __int8)(-(result));
    v_rdi = (unsigned int)((*(unsigned __int64 *)(v_stack_mF0 + 0 * 8 - 16)) & (681));
    v_rdi = (unsigned int)((v_rdi) + (0xC000017CULL));
    goto loc_00847C59;
loc_0084816C:
    result = HvpReleaseCellFlat((__int16)(v_stack_m106), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 284)), v_stack_mC8, (unsigned int)(*(unsigned int *)(v_stack_p78 + 36)));
    goto loc_00847F34;
loc_00848176:
    result = HvFreeCell(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 284)), v_stack_mC8, (unsigned int)(*(unsigned int *)(v_stack_p78 + 36)));
    goto loc_00848133;
loc_00848181:
    goto loc_00847C1F;
loc_0084818B:
    if (sign_flag) goto loc_00847C2E;
    a4 = 0;
    a3 = 0;
    result = HvpMarkCellDirty(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), (unsigned int)((unsigned int)(v_stack_mC8)), a3, a4);
    if (sign_flag) goto loc_00847C2E;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 140)) & (1)) == 0) goto loc_00848284;
    result = HvpGetCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), (unsigned int)((unsigned int)(v_stack_mC8)), v_stack_p48, a4);
loc_008481CD:
    result = CmpMarkValueDataDirty(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), result, v_stack_p48, a4);
    if (sign_flag) goto loc_00847C22;
    result = CmpFreeValueData(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), (unsigned int)(*(unsigned int *)(result + 8)), (unsigned int)(*(unsigned int *)(result + 4)), a4);
    v_r15 = 0;
    *(unsigned int *)(result + 12) = 0;
    *(unsigned int *)(result + 4) = 0;
    *(unsigned __int64 *)(v_stack_p78 + 4) = v_rbx;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 168) = v_rbx;
    goto loc_00847B84;
loc_00848225:
    a3 = 0;
    result = CmpGetSecurityCacheEntryForKcbStack(v_stack_m108, v_stack_p78, a3, a4);
    result = CmpAllocatePool(256, (unsigned int)(*(unsigned int *)(result + 24)), (unsigned int)(0x32414D43ULL), a4);
    if (result != 0) goto loc_008482ED;
    goto loc_00847C2E;
loc_00848263:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_p58 + 32) + 140)) & (1)) != 0) goto loc_0084828E;
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(v_stack_p58 + 32), v_stack_p48, (unsigned int)(0x32414D43ULL), a4);
    goto loc_00847C2B;
loc_00848284:
    result = HvpGetCellPaged(*(unsigned __int64 *)(v_stack_p58 + 32), v_stack_p48, (unsigned int)(0x32414D43ULL), a4);
    goto loc_008481CD;
loc_0084828E:
    result = HvpReleaseCellFlat(*(unsigned __int64 *)(v_stack_p58 + 32), v_stack_p48, (unsigned int)(0x32414D43ULL), a4);
    goto loc_00847C2B;
loc_00848298:
    v_r12 = (unsigned __int16)((v_stack_mC8) - 1);
    goto loc_00847897;
loc_008482A1:
    result = CmpSnapshotTxOwnerArray(*(unsigned __int64 *)(v_stack_p58 + 32), v_stack_p68, v_stack_mD0, a4);
    if (sign_flag) goto loc_008482E5;
    a2 = 0;
    v_stack_p20 = (unsigned int)((unsigned int)(v_stack_p68));
    result = CmpLogTransactionAbortedWithChildName(*(unsigned __int64 *)(a1 + 8), a2, a2 + 1, a4);
    result = CmpUnlockKcbStack(v_stack_m108, a2, a2 + 1, a4);
    result = CmpCleanupKcbStack(v_stack_m108, a2, a2 + 1, a4);
    goto loc_00847FD6;
loc_008482E5:
    goto loc_00847C59;
loc_008482ED:
    result = memcpy(1, (unsigned int)((unsigned int)(result)) + 32, (unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)(result)) + 24)), a4);
    v_stack_mD8 = 1;
    result = CmpGetValueForAudit(*(unsigned __int64 *)(v_stack_p58 + 32), (unsigned int)((unsigned int)(v_r12)), v_stack_m98, (unsigned int)(0x31414D43ULL));
    if (sign_flag) goto loc_00847C2E;
    v_rdi = 0;
    goto loc_00847A6C;
loc_00848330:
    goto loc_00847F04;
loc_00848338:
    goto loc_00847C62;
loc_00848345:
    goto loc_008480D2;
loc_0084834F:
    result = HvUnlockHiveFlusherShared(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), (unsigned int)((unsigned int)(v_r12)), v_stack_m98, (unsigned int)(0x31414D43ULL));
    goto loc_00847C79;
loc_0084835D:
    result = CmpFreePoolWithTag(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), (unsigned int)(0x34414D43ULL), v_stack_m98, (unsigned int)(0x31414D43ULL));
    goto loc_00847CD3;
loc_0084836C:
    result = CmpFreePoolWithTag((unsigned int)(v_stack_p68), (unsigned int)(0x33414D43ULL), v_stack_m98, (unsigned int)(0x31414D43ULL));
    goto loc_00847CDC;
}
```

## 5. (Beta) C Style

```c
int64_t CmDeleteValueKey(int64_t Arg1, int64_t Arg2, int64_t Arg3, uint8_t Arg4)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint16_t v_stack_m106;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint32_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint32_t v_stack_m12C;
    uint32_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint64_t v_stack_m148;
    uint64_t v_stack_m150;
    uint8_t v_stack_m156;
    uint8_t v_stack_m157;
    uint8_t v_stack_m158;
    uint64_t v_stack_m170;
    uint64_t v_stack_m178;
    uint64_t v_stack_m48;
    uint64_t v_stack_m58;
    uint64_t v_stack_m68;
    uint64_t v_stack_m78;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint32_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint32_t v_stack_p38;
    uint8_t v_stack_p40;
    uint64_t v_stack_p41;
    uint8_t v_stack_p42;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint64_t v_stack_p6C;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;

    v_stack_p20 = local_rbx;
    local_rsp = (local_rsp) - (352);
    result = (*(uint64_t *)(v_rip + 0x5C3035)) ^ (local_rsp);
    v_stack_m48 = result;
    local_r15 = 0;
    v_stack_m148 = Arg1;
    v_stack_m156 = Arg4;
    v_stack_mB0 = Arg3;
    v_stack_mB8 = v_stack_mC0;
    v_stack_mC8 = Arg2;
    v_stack_mC0 = v_stack_mC0;
    result = (uint32_t)((v_stack_mC0) | (0xFFFFFFFFULL));
    v_stack_m130 = 0;
    v_stack_m108 = v_xmm0;
    v_stack_m106 = (uint16_t)(result);
    v_stack_mD0 = 0;
    v_stack_m110 = 0;
    v_stack_mE0 = 0;
    v_stack_m150 = 0;
    v_stack_m78 = v_xmm0;
    v_stack_m138 = 0;
    v_stack_m68 = v_xmm0;
    v_stack_m157 = 0;
    v_stack_m58 = v_xmm0;
    v_stack_mE8 = 0;
    v_stack_mA8 = v_xmm0;
    v_stack_m128 = 0;
    v_stack_mF8 = v_xmm0;
    v_stack_m120 = 0;
    result = HvpGetCellContextInitialize(v_stack_m110, Arg2, Arg3, Arg4);
    result = HvpGetCellContextInitialize(v_stack_mE0, Arg2, Arg3, Arg4);
    v_stack_m140 = 0;
    result = HvpGetCellContextInitialize(v_stack_m150, Arg2, Arg3, Arg4);
    result = (uint32_t)((result) | (0xFFFFFFFFULL));
    v_stack_m118 = (uint32_t)(result);
    v_stack_m12C = (uint32_t)(result);
    result = CmpInitializeDelayDerefContext(v_stack_mA8, Arg2, Arg3, Arg4);
    v_stack_mD8 = 0;
    v_stack_m98 = v_xmm0;
    v_stack_m88 = v_xmm0;
    result = CmpAttachToRegistryProcess(v_stack_m78, Arg2, Arg3, Arg4);
loc_008477D9:
    result = CmpIsShutdownRundownActive(v_stack_m78, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) != 0) goto loc_008480C8;
    result = CmpLockRegistry(v_stack_m78, Arg2, Arg3, Arg4);
    v_stack_m158 = 1;
    if (((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x20) + 0xA0)) & (0x100000ULL)) != 0) goto loc_00848345;
    result = CmpStartKcbStackForTopLayerKcb(v_stack_m108, *(uint64_t *)(Arg1 + 0x8), Arg3, Arg4);
    if (sign_flag) goto loc_008480D2;
    result = CmpLockKcbStackTopExclusiveRestShared(v_stack_m108, *(uint64_t *)(Arg1 + 0x8), Arg3, Arg4);
    if ((*(uint64_t *)(Arg1 + 0x38)) != 0) goto loc_00847D14;
    if ((*(uint64_t *)(Arg1 + 0x40)) != 0) goto loc_00847D14;
loc_0084784E:
    result = CmpIsKeyDeletedForKeyBody(Arg1, v_stack_m128, Arg3, Arg4);
    if ((uint8_t)(result) != 0) goto loc_0084814C;
    if (v_stack_m128 != 0) goto loc_00847E01;
    if ((*(uint32_t *)(*(uint64_t *)(Arg1 + 0x8) + 0xF8)) < 0) goto loc_00847F8E;
    if ((*(uint32_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x108)) != 0) goto loc_008482A1;
    local_r10 = 0;
loc_00847892:
loc_00847897:
loc_0084789C:
    if (sign_flag) goto loc_00847972;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x42))) >= 2) goto loc_008480E4;
loc_008478BE:
    result = CmpGetEffectiveKcbSemantics(*(uint64_t *)(v_stack_m98 + (int16_t)((uint16_t)(*(uint16_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x42))) * 8 - 0x68), v_stack_m148, Arg3, v_stack_m148);
    if (((uint32_t)(result)) == 1) goto loc_00847972;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m98 + (int16_t)((uint16_t)(*(uint16_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x42))) * 8 - 0x68) + 0x28)))) == -1) goto loc_00847EA5;
    if (v_stack_m128 != 0) goto loc_00847EAE;
loc_008478ED:
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m98 + (int16_t)((uint16_t)(*(uint16_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x42))) * 8 - 0x68) + 0x20) + 0x8C)) & (1)) == 0) goto loc_00847DA3;
    result = HvpGetCellFlat(*(uint64_t *)(*(uint64_t *)(v_stack_m98 + (int16_t)((uint16_t)(*(uint16_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x42))) * 8 - 0x68) + 0x20), (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m98 + (int16_t)((uint16_t)(*(uint16_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x42))) * 8 - 0x68) + 0x28)), v_stack_mE0, v_stack_m148);
loc_00847907:
    v_stack_m170 = v_stack_m118;
    Arg4 = 0;
    v_stack_m178 = v_stack_m12C;
    result = CmpFindNameInListWithStatus(*(uint64_t *)(*(uint64_t *)(v_stack_m98 + (int16_t)((uint16_t)(*(uint16_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x42))) * 8 - 0x68) + 0x20), result + 36, v_stack_mC8, Arg4);
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m98 + (int16_t)((uint16_t)(*(uint16_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x42))) * 8 - 0x68) + 0x20) + 0x8C)) & (1)) != 0) goto loc_008480DA;
    result = HvpReleaseCellPaged(*(uint64_t *)(*(uint64_t *)(v_stack_m98 + (int16_t)((uint16_t)(*(uint16_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x42))) * 8 - 0x68) + 0x20), v_stack_mE0, v_stack_mC8, Arg4);
loc_0084794A:
    local_r10 = 0;
    if (!sign_flag) goto loc_00848119;
loc_0084795B:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != 0xC0000034ULL) goto loc_00847989;
    result = CmpGetEffectiveKcbSemantics(*(uint64_t *)(v_stack_m98 + (int16_t)((uint16_t)(*(uint16_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x42))) * 8 - 0x68), v_stack_m148, v_stack_mC8, Arg4);
    if ((uint32_t)(result) == 0) goto loc_00848298;
loc_00847972:
loc_00847977:
    local_r14 = (uint32_t)((*(uint64_t *)(v_stack_m98 + (int16_t)((uint16_t)(*(uint16_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x42))) * 8 - 0x68)) | (0xFFFFFFFFULL));
    if (((uint32_t)((uint32_t)(v_stack_m118))) != ((uint32_t)(local_r14))) goto loc_00847991;
loc_00847989:
    goto loc_00847C54;
loc_00847991:
    if (((*(uint8_t *)(*(uint64_t *)((uint32_t)(0xC0000034ULL) + 0x20) + 0x8C)) & (1)) == 0) goto loc_00847DAD;
    result = HvpGetCellFlat(*(uint64_t *)((uint32_t)(0xC0000034ULL) + 0x20), (uint32_t)((uint32_t)((uint32_t)(v_stack_m118))), v_stack_m150, Arg4);
loc_008479AF:
    result = CmpIsValueTombstone(*(uint64_t *)((uint32_t)(0xC0000034ULL) + 0x20), result, v_stack_m150, Arg4);
    local_rdi = 0;
    if ((uint8_t)(result) != 0) goto loc_00848181;
    if (((*(uint8_t *)(*(uint64_t *)((uint32_t)(0xC0000034ULL) + 0x20) + 0x8C)) & (1)) != 0) goto loc_008480F2;
    result = HvpReleaseCellPaged(*(uint64_t *)((uint32_t)(0xC0000034ULL) + 0x20), v_stack_m150, v_stack_m150, Arg4);
loc_008479DF:
    if ((*(uint32_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x28)) == 1) goto loc_00847DCB;
    result = HvLockHiveFlusherShared(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x20), v_stack_m150, v_stack_m150, Arg4);
    if (v_stack_m128 != 0) goto loc_00847A2F;
    Arg4 = 0;
    Arg3 = 0;
    result = HvpMarkCellDirty(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x20), (uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x28)), Arg3, Arg4);
    if (sign_flag) goto loc_00847C4F;
    local_rdi = 0;
loc_00847A2F:
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x20) + 0x8C)) & (1)) == 0) goto loc_00847DB7;
    result = HvpGetCellFlat(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x20), (uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x28)), v_stack_m110, Arg4);
loc_00847A4C:
    v_stack_m120 = result;
    result = CmpUpdateKeyNodeAccessBits(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x20), result, (uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x28)), Arg4);
    if (v_stack_m156 != 0) goto loc_00848225;
loc_00847A6C:
    if (v_stack_m128 != 0) goto loc_00847F1E;
    Arg4 = 0;
    Arg3 = 0;
    if ((*(uint16_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x42)) != 0) goto loc_00848044;
    result = HvpMarkCellDirty(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x20), (uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x28)), Arg3, Arg4);
    if (sign_flag) goto loc_00847C2E;
    Arg4 = 0;
    Arg3 = 0;
    result = HvpMarkCellDirty(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x20), (uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x64)), Arg3, Arg4);
    if (sign_flag) goto loc_00847C2E;
    Arg4 = 0;
    Arg3 = 0;
    result = HvpMarkCellDirty(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x20), (uint32_t)((uint32_t)((uint32_t)(v_stack_m118))), Arg3, Arg4);
    if (sign_flag) goto loc_00847C2E;
    if (((*(uint8_t *)(*(uint64_t *)(v_stack_m140 + 0x20) + 0x8C)) & (1)) == 0) goto loc_00847DC1;
    result = HvpGetCellFlat(*(uint64_t *)(v_stack_m140 + 0x20), (uint32_t)((uint32_t)((uint32_t)(v_stack_m118))), v_stack_m150, Arg4);
loc_00847AFB:
    result = CmpMarkValueDataDirty(*(uint64_t *)(v_stack_m140 + 0x20), result, v_stack_m150, Arg4);
    if (sign_flag) goto loc_00847C22;
    if (((*(uint8_t *)(*(uint64_t *)(v_stack_m140 + 0x20) + 0x8C)) & (1)) != 0) goto loc_008480FC;
    result = HvpReleaseCellPaged(*(uint64_t *)(v_stack_m140 + 0x20), v_stack_m150, v_stack_m150, Arg4);
loc_00847B34:
    local_r15 = 0;
    result = CmpRemoveValueFromList(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x20), (uint32_t)(v_stack_m12C), v_stack_m120 + 36, Arg4);
    result = CmpFreeValue(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x20), (uint32_t)((uint32_t)((uint32_t)(v_stack_m118))), v_stack_m120 + 36, Arg4);
    *(uint64_t *)(v_stack_m120 + 0x4) = *(uint64_t *)(local_rbx);
    *(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0xA8) = *(uint64_t *)(local_rbx);
    if ((*(uint32_t *)(v_stack_m120 + 0x24)) == 0) {
        *(uint32_t *)(v_stack_m120 + 0x3C) = 0;
        *(uint16_t *)(*(uint64_t *)(Arg1 + 0x8) + 0xB2) = 0;
        *(uint32_t *)(v_stack_m120 + 0x40) = 0;
        *(uint32_t *)(*(uint64_t *)(Arg1 + 0x8) + 0xB4) = 0;
    }
    if (((*(uint32_t *)(*(uint64_t *)(Arg1 + 0x8) + 0xB8)) & (0x400000ULL)) == 0) goto loc_00848010;
loc_00847B94:
    *(uint32_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x60) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m120 + 0x24)));
    *(uint32_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x64) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m120 + 0x28)));
loc_00847BA2:
    result = HvUnlockHiveFlusherShared(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x20), (uint32_t)((uint32_t)((uint32_t)(v_stack_m118))), v_stack_m120 + 36, Arg4);
    local_rdi = 0;
    v_stack_m138 = 0;
    v_stack_m157 = 0;
    if (v_stack_m106 >= ((uint16_t)(local_rdi + 2))) goto loc_00848106;
loc_00847BD4:
    v_stack_m178 = v_stack_mC0;
    result = CmpReportNotifyHelper(v_stack_m108, *(uint64_t *)(*(uint64_t *)(v_stack_m98 + (int16_t)(v_stack_m106) * 8 - 0x68) + 0x20), v_stack_m128, 4);
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m98 + (int16_t)(v_stack_m106) * 8 - 0x68) + 0x20)) != (*(uint64_t *)(v_rip + 0x791E91))) {
        Arg3 = v_stack_m128;
        result = v_stack_mC0;
        Arg4 = 4;
        v_stack_m178 = result;
        Arg1 = v_stack_m108;
        result = CmpReportNotifyHelper(Arg1, *(uint64_t *)(v_rip + 0x791E91), Arg3, Arg4);
    }
loc_00847C22:
    if (0 != 0) goto loc_00848263;
loc_00847C2B:
    local_r13 = 0;
loc_00847C2E:
    if (v_stack_m120 == 0) goto loc_00847C4F;
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x20) + 0x8C)) & (1)) != 0) goto loc_0084803A;
    result = HvpReleaseCellPaged(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x20), v_stack_m110, Arg3, Arg4);
loc_00847C4F:
loc_00847C54:
loc_00847C59:
    if (v_stack_m138 != 0) goto loc_00847F04;
loc_00847C62:
    local_r13 = 0;
    if (v_stack_m157 != 0) goto loc_00848126;
loc_00847C70:
    if (0 != 0) goto loc_0084834F;
loc_00847C79:
    if (1 != 0) {
        Arg1 = v_stack_m108;
        result = CmpUnlockKcbStack(Arg1, v_stack_m110, Arg3, Arg4);
    }
    Arg2 = 0;
    result = CmpDrainDelayDerefContext(v_stack_mA8, Arg2, Arg3, Arg4);
    if (v_stack_m158 != 0) {
        result = CmpUnlockRegistry(v_stack_mA8, Arg2, Arg3, Arg4);
    }
    result = v_stack_mC0;
    if (v_stack_mC0 != v_stack_mC0) {
        Arg1 = v_stack_mC0;
        result = CmpSignalDeferredPosts(Arg1, Arg2, Arg3, Arg4);
    }
    result = CmpDetachFromRegistryProcess(v_stack_m78, Arg2, Arg3, Arg4);
    if (!sign_flag) goto loc_00847D5A;
loc_00847CC6:
    if (v_stack_m90 != 0) goto loc_0084835D;
loc_00847CD3:
    if (v_stack_mD8 != 0) goto loc_0084836C;
loc_00847CDC:
    if (v_stack_mF0 != 0) {
        result = CmSiFreeMemory(v_stack_mF0, Arg2, Arg3, Arg4);
    }
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (352);
    return result;
loc_00847D14:
    Arg2 = 0;
    result = CmpIsKeyDeletedForKeyBody(v_stack_m148, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) != 0) goto loc_0084814F;
    result = CmpTransSearchAddTransFromKeyBody(v_stack_m148, v_stack_p70, Arg3, Arg4);
    if (sign_flag) goto loc_00847C59;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x20) + 0xA0)))) & (2)) == 0) goto loc_0084784E;
    goto loc_00847C59;
loc_00847D5A:
    if (v_stack_p42 == 0) goto loc_00847CC6;
    if (v_stack_p20 == 0) goto loc_00847CC6;
    v_stack_p38 = 2;
    Arg3 = 0;
    v_stack_p30 = v_stack_m98;
    Arg1 = 0;
    v_stack_p28 = v_stack_mB0;
    v_stack_p20 = v_stack_m148;
    result = SeAdtRegistryValueChangedAuditAlarm(Arg1, v_stack_p20, Arg3, v_stack_mC8);
    goto loc_00847CC6;
loc_00847DA3:
    result = HvpGetCellPaged(Arg1, v_stack_p20, Arg3, v_stack_mC8);
    goto loc_00847907;
loc_00847DAD:
    result = HvpGetCellPaged(Arg1, v_stack_p20, Arg3, v_stack_mC8);
    goto loc_008479AF;
loc_00847DB7:
    result = HvpGetCellPaged(Arg1, v_stack_p20, Arg3, v_stack_mC8);
    goto loc_00847A4C;
loc_00847DC1:
    result = HvpGetCellPaged(Arg1, v_stack_p20, Arg3, v_stack_mC8);
    goto loc_00847AFB;
loc_00847DCB:
    result = CmpUnlockKcbStack(v_stack_m108, v_stack_p20, Arg3, v_stack_mC8);
    Arg2 = 0;
    result = CmpPromoteKey(v_stack_m108, Arg2, 1, v_stack_mC8);
    if (sign_flag) goto loc_00847C59;
    local_r15 = 0;
    goto loc_0084784E;
loc_00847E01:
    result = CmpAllocateUnitOfWork(v_stack_m108, Arg2, 1, v_stack_mC8);
    v_stack_p60 = result;
    if (result == 0) goto loc_00848338;
    result = CmpTransEnlistUowInKcb(result, *(uint64_t *)(Arg1 + 0x8), 1, v_stack_mC8);
    result = CmpTransEnlistUowInCmTrans(result, (uint8_t)((uint32_t)(0xC0190001ULL)), 1, v_stack_mC8);
    if (sign_flag) goto loc_00847F01;
    result = CmpLockIXLockIntent(*(uint64_t *)(Arg1 + 0x8) + 248, result, 1, v_stack_mC8);
    if ((uint8_t)(result) == 0) goto loc_00847EFC;
    result = CmpLockIXLockExclusive(*(uint64_t *)(Arg1 + 0x8) + 264, result, 1, v_stack_mC8);
    if ((uint8_t)(result) == 0) goto loc_00847EFC;
    result = HvLockHiveFlusherShared(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x20), result, 1, v_stack_mC8);
    result = CmpCloneKCBValueListForTrans(*(uint64_t *)(Arg1 + 0x8), (uint8_t)((uint32_t)(0xC0190001ULL)), v_stack_p41, v_stack_mC8);
    if (sign_flag) goto loc_00848330;
    result = HvUnlockHiveFlusherShared(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x20), (uint8_t)((uint32_t)(0xC0190001ULL)), v_stack_p41, v_stack_mC8);
    local_r10 = 0;
    goto loc_00847892;
loc_00847EA5:
    local_r12 = (uint16_t)((v_stack_p50) - 1);
    goto loc_0084789C;
loc_00847EAE:
    if ((*(uint64_t *)((uint8_t)((uint32_t)(0xC0190001ULL)) + 0x120)) != result) goto loc_008478ED;
    v_stack_p28 = v_stack_m118;
    Arg4 = 0;
    v_stack_p20 = v_stack_p6C;
    result = CmpFindNameInListWithStatus(*(uint64_t *)((uint8_t)((uint32_t)(0xC0190001ULL)) + 0x20), (uint8_t)((uint32_t)(0xC0190001ULL)) + 280, v_stack_mC8, Arg4);
    local_r10 = 0;
    if (!sign_flag) goto loc_00848119;
    goto loc_0084795B;
loc_00847EFC:
loc_00847F01:
loc_00847F04:
    result = CmpRundownUnitOfWork(result, (uint8_t)((uint32_t)(0xC0190001ULL)) + 280, v_stack_mC8, Arg4);
    result = ExFreePoolWithTag(result, (uint32_t)(0x77554D43ULL), v_stack_mC8, Arg4);
    goto loc_00847C62;
loc_00847F1E:
    if (((*(uint8_t *)(result + 0x8C)) & (0)) != 0) goto loc_0084816C;
    result = HvpReleaseCellPaged(result, v_stack_m110, v_stack_mC8, Arg4);
loc_00847F34:
    v_stack_p78 = (uint32_t)(0xC0190001ULL);
    result = HvUnlockHiveFlusherShared(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x20), v_stack_m110, v_stack_mC8, Arg4);
    *(uint32_t *)(v_stack_p60 + 0x44) = 6;
    *(uint32_t *)(v_stack_p60 + 0x58) = (uint32_t)(local_r12);
    result = CmAddLogForAction(v_stack_p60, 1, v_stack_mC8, Arg4);
    if (sign_flag) goto loc_00847C4F;
    result = HvLockHiveFlusherShared(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x20), 1, v_stack_mC8, Arg4);
    result = CmpRemoveValueFromList(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x20), (uint32_t)(v_stack_p6C), *(uint64_t *)(Arg1 + 0x8) + 280, Arg4);
    goto loc_00847BA2;
loc_00847F8E:
    result = CmpSnapshotTxOwnerArray(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x20), v_stack_p68, v_stack_mD0, Arg4);
    if (sign_flag) goto loc_008482E5;
    Arg2 = 0;
    v_stack_p20 = (uint32_t)((uint32_t)(v_stack_p68));
    result = CmpLogTransactionAbortedWithChildName(*(uint64_t *)(Arg1 + 0x8), Arg2, Arg2 + 1, Arg4);
    result = CmpUnlockKcbStack(v_stack_m108, Arg2, Arg2 + 1, Arg4);
    if (v_stack_mF0 != 0) {
        result = CmSiFreeMemory(v_stack_mF0, Arg2, Arg2 + 1, Arg4);
    }
    result = (uint32_t)((result) | (0xFFFFFFFFULL));
    v_stack_m108 = v_xmm0;
    v_stack_m106 = (uint16_t)(result);
    v_stack_mF8 = v_xmm0;
    result = CmpUnlockRegistry(v_stack_mF0, Arg2, Arg2 + 1, Arg4);
    v_stack_p40 = (uint8_t)((uint8_t)((uint32_t)(0xC0190001ULL)));
    result = CmpRollbackTransactionArray((uint32_t)((uint32_t)((uint32_t)(v_stack_p68))), v_stack_mD0, Arg2 + 1, v_stack_mE8);
    if (!sign_flag) goto loc_008477D9;
    goto loc_00847C59;
loc_00848010:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x8)))) & (8)) == 0) goto loc_00847B94;
    result = CmpDelayDerefKeyControlBlock(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x68), v_stack_mA8, Arg2 + 1, v_stack_mE8);
    *(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x68) = (uint8_t)((uint32_t)(0xC0190001ULL));
    goto loc_00847B94;
loc_0084803A:
    result = HvpReleaseCellFlat(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x68), v_stack_mA8, Arg2 + 1, v_stack_mE8);
    goto loc_00847C4F;
loc_00848044:
    result = HvpMarkCellDirty(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x68), v_stack_mA8, Arg2 + 1, v_stack_mE8);
    if ((*(uint64_t *)(Arg1 + 0x8)) == v_stack_p58) goto loc_0084818B;
    if (sign_flag) goto loc_00847C2E;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x28))) >> (31));
    v_stack_p20 = (uint32_t)(result);
    result = CmpSetValueKeyTombstone(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x20), v_stack_p78, v_stack_mC8, (uint32_t)(*(uint32_t *)(v_stack_p78 + 0x24)));
    if (sign_flag) goto loc_00847C2E;
    local_r15 = 0;
    *(uint64_t *)(v_stack_p78 + 0x4) = (uint32_t)(v_stack_p68);
    *(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0xA8) = (uint32_t)(v_stack_p68);
    if ((*(uint32_t *)(v_stack_p78 + 0x3C)) >= ((uint32_t)(*(uint16_t *)(v_stack_mC8)))) goto loc_00847B84;
    *(uint32_t *)(v_stack_p78 + 0x3C) = (uint32_t)(*(uint16_t *)(v_stack_mC8));
    *(uint16_t *)(*(uint64_t *)(Arg1 + 0x8) + 0xB2) = (uint16_t)(*(uint16_t *)(v_stack_mC8));
    goto loc_00847B84;
loc_008480C8:
    v_stack_p40 = 0;
loc_008480D2:
    goto loc_00847C59;
loc_008480DA:
    result = HvpReleaseCellFlat(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x20), v_stack_p78, v_stack_mC8, (uint32_t)(*(uint32_t *)(v_stack_p78 + 0x24)));
    goto loc_0084794A;
loc_008480E4:
    goto loc_008478BE;
loc_008480F2:
    result = HvpReleaseCellFlat(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x20), v_stack_p78, v_stack_mC8, (uint32_t)(*(uint32_t *)(v_stack_p78 + 0x24)));
    goto loc_008479DF;
loc_008480FC:
    result = HvpReleaseCellFlat(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x20), v_stack_p78, v_stack_mC8, (uint32_t)(*(uint32_t *)(v_stack_p78 + 0x24)));
    goto loc_00847B34;
loc_00848106:
    goto loc_00847BD4;
loc_00848119:
    v_stack_p58 = *(uint64_t *)(v_stack_mF0 + 0x0 * 8 - 0x10);
    goto loc_00847977;
loc_00848126:
    local_rbx = (uint32_t)((*(uint64_t *)(v_stack_mF0 + (int16_t)(v_stack_m106) * 8 - 0x10)) | (0xFFFFFFFFULL));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x11C)))) != ((uint32_t)(local_rbx))) goto loc_00848176;
loc_00848133:
    *(uint32_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x11C) = (uint32_t)(local_rbx);
    *(uint32_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x118) = (uint32_t)(result);
    *(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x120) = result;
    goto loc_00847C70;
loc_0084814C:
loc_0084814F:
    result = (uint8_t)((*(uint8_t *)(v_stack_mC8 + 0x30)) & (1));
    result = (uint8_t)(-(result));
    local_rdi = (uint32_t)((*(uint64_t *)(v_stack_mF0 + 0x0 * 8 - 0x10)) & (681));
    local_rdi = (uint32_t)((local_rdi) + (0xC000017CULL));
    goto loc_00847C59;
loc_0084816C:
    result = HvpReleaseCellFlat((int16_t)(v_stack_m106), (uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x11C)), v_stack_mC8, (uint32_t)(*(uint32_t *)(v_stack_p78 + 0x24)));
    goto loc_00847F34;
loc_00848176:
    result = HvFreeCell(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x20), (uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x11C)), v_stack_mC8, (uint32_t)(*(uint32_t *)(v_stack_p78 + 0x24)));
    goto loc_00848133;
loc_00848181:
    goto loc_00847C1F;
loc_0084818B:
    if (sign_flag) goto loc_00847C2E;
    Arg4 = 0;
    Arg3 = 0;
    result = HvpMarkCellDirty(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x20), (uint32_t)((uint32_t)(v_stack_mC8)), Arg3, Arg4);
    if (sign_flag) goto loc_00847C2E;
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x20) + 0x8C)) & (1)) == 0) goto loc_00848284;
    result = HvpGetCellFlat(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x20), (uint32_t)((uint32_t)(v_stack_mC8)), v_stack_p48, Arg4);
loc_008481CD:
    result = CmpMarkValueDataDirty(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x20), result, v_stack_p48, Arg4);
    if (sign_flag) goto loc_00847C22;
    result = CmpFreeValueData(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x20), (uint32_t)(*(uint32_t *)(result + 0x8)), (uint32_t)(*(uint32_t *)(result + 0x4)), Arg4);
    local_r15 = 0;
    *(uint32_t *)(result + 0xC) = 0;
    *(uint32_t *)(result + 0x4) = 0;
    *(uint64_t *)(v_stack_p78 + 0x4) = local_rbx;
    *(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0xA8) = local_rbx;
    goto loc_00847B84;
loc_00848225:
    Arg3 = 0;
    result = CmpGetSecurityCacheEntryForKcbStack(v_stack_m108, v_stack_p78, Arg3, Arg4);
    result = CmpAllocatePool(256, (uint32_t)(*(uint32_t *)(result + 0x18)), (uint32_t)(0x32414D43ULL), Arg4);
    if (result != 0) goto loc_008482ED;
    goto loc_00847C2E;
loc_00848263:
    if (((*(uint8_t *)(*(uint64_t *)(v_stack_p58 + 0x20) + 0x8C)) & (1)) != 0) goto loc_0084828E;
    result = HvpReleaseCellPaged(*(uint64_t *)(v_stack_p58 + 0x20), v_stack_p48, (uint32_t)(0x32414D43ULL), Arg4);
    goto loc_00847C2B;
loc_00848284:
    result = HvpGetCellPaged(*(uint64_t *)(v_stack_p58 + 0x20), v_stack_p48, (uint32_t)(0x32414D43ULL), Arg4);
    goto loc_008481CD;
loc_0084828E:
    result = HvpReleaseCellFlat(*(uint64_t *)(v_stack_p58 + 0x20), v_stack_p48, (uint32_t)(0x32414D43ULL), Arg4);
    goto loc_00847C2B;
loc_00848298:
    local_r12 = (uint16_t)((v_stack_mC8) - 1);
    goto loc_00847897;
loc_008482A1:
    result = CmpSnapshotTxOwnerArray(*(uint64_t *)(v_stack_p58 + 0x20), v_stack_p68, v_stack_mD0, Arg4);
    if (sign_flag) goto loc_008482E5;
    Arg2 = 0;
    v_stack_p20 = (uint32_t)((uint32_t)(v_stack_p68));
    result = CmpLogTransactionAbortedWithChildName(*(uint64_t *)(Arg1 + 0x8), Arg2, Arg2 + 1, Arg4);
    result = CmpUnlockKcbStack(v_stack_m108, Arg2, Arg2 + 1, Arg4);
    result = CmpCleanupKcbStack(v_stack_m108, Arg2, Arg2 + 1, Arg4);
    goto loc_00847FD6;
loc_008482E5:
    goto loc_00847C59;
loc_008482ED:
    result = memcpy(1, (uint32_t)((uint32_t)(result)) + 32, (uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)(result)) + 0x18)), Arg4);
    v_stack_mD8 = 1;
    result = CmpGetValueForAudit(*(uint64_t *)(v_stack_p58 + 0x20), (uint32_t)((uint32_t)(local_r12)), v_stack_m98, (uint32_t)(0x31414D43ULL));
    if (sign_flag) goto loc_00847C2E;
    local_rdi = 0;
    goto loc_00847A6C;
loc_00848330:
    goto loc_00847F04;
loc_00848338:
    goto loc_00847C62;
loc_00848345:
    goto loc_008480D2;
loc_0084834F:
    result = HvUnlockHiveFlusherShared(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x20), (uint32_t)((uint32_t)(local_r12)), v_stack_m98, (uint32_t)(0x31414D43ULL));
    goto loc_00847C79;
loc_0084835D:
    result = CmpFreePoolWithTag(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x20), (uint32_t)(0x34414D43ULL), v_stack_m98, (uint32_t)(0x31414D43ULL));
    goto loc_00847CD3;
loc_0084836C:
    result = CmpFreePoolWithTag((uint32_t)(v_stack_p68), (uint32_t)(0x33414D43ULL), v_stack_m98, (uint32_t)(0x31414D43ULL));
    goto loc_00847CDC;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008476E8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
