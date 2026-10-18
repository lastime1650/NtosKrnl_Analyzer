# CmSetValueKey

- RVA: `0x008457C0`–`0x00846800` (길이 `4,160` bytes)
- VA: `0x00000001408457C0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00069210`
- 디코드: `972`개 명령, `4,160/4,160` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **89**; 고유 호출 대상: **59**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0084587C` → [HvpGetCellContextInitialize](../85/HvpGetCellContextInitialize_function_00855F10.md) (function, `0x00855F10`)
- `0x00845885` → [HvpGetCellContextInitialize](../85/HvpGetCellContextInitialize_function_00855F10.md) (function, `0x00855F10`)
- `0x0084588E` → [CmpInitializeDelayDerefContext](../../text/42/CmpInitializeDelayDerefContext_function_0042A7F0.md) (function, `0x0042A7F0`)
- `0x008458D1` → [SeCaptureSubjectContext](../86/SeCaptureSubjectContext_function_0086B820.md) (function, `0x0086B820`)
- `0x008458DD` → [CmpAttachToRegistryProcess](../../pagecmrc/BC/CmpAttachToRegistryProcess_function_00BC98E0.md) (function, `0x00BC98E0`)
- `0x008458F0` → [CmpIsShutdownRundownActive](../../pagecmrc/BC/CmpIsShutdownRundownActive_function_00BC9C20.md) (function, `0x00BC9C20`)
- `0x00845900` → [CmpLockRegistry](../../pagecmrc/BC/CmpLockRegistry_function_00BC9B34.md) (function, `0x00BC9B34`)
- `0x00845982` → [CmpLockKcbStackTopExclusiveRestShared](CmpLockKcbStackTopExclusiveRestShared_function_00846B04.md) (function, `0x00846B04`)
- `0x008459A4` → [CmpIsKeyDeletedForKeyBody](../../pagecmrc/BC/CmpIsKeyDeletedForKeyBody_function_00BC9480.md) (function, `0x00BC9480`)
- `0x008459B8` → [CmpTransSearchAddTransFromKeyBody](../87/CmpTransSearchAddTransFromKeyBody_function_008736B8.md) (function, `0x008736B8`)
- `0x00845A15` → [CmpLockKcbShared](../../pagecmrc/BC/CmpLockKcbShared_function_00BC9A1C.md) (function, `0x00BC9A1C`)
- `0x00845A4B` → [CmpIsKeyDeletedForKeyBody](../../pagecmrc/BC/CmpIsKeyDeletedForKeyBody_function_00BC9480.md) (function, `0x00BC9480`)
- `0x00845A86` → [CmpSnapshotTxOwnerArray](CmpSnapshotTxOwnerArray_function_00846808.md) (function, `0x00846808`)
- `0x00845AA8` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00845AF3` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (function, `0x00BC92C0`)
- `0x00845B16` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (function, `0x00475D80`)
- `0x00845B32` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x00845BE5` → [CmpCompareNewValueDataAgainstKCBCache](CmpCompareNewValueDataAgainstKCBCache_function_00846920.md) (function, `0x00846920`)
- `0x00845C70` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (function, `0x00BC92C0`)
- `0x00845CA6` → [CmpLockKcbExclusive](../86/CmpLockKcbExclusive_function_00861EB0.md) (function, `0x00861EB0`)
- `0x00845CCF` → [HvLockHiveFlusherShared](HvLockHiveFlusherShared_function_0084F95C.md) (function, `0x0084F95C`)
- `0x00845CF3` → [HvpMarkCellDirty](../85/HvpMarkCellDirty_function_00858080.md) (function, `0x00858080`)
- `0x00845D1F` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x00845D32` → [CmpUpdateKeyNodeAccessBits](CmpUpdateKeyNodeAccessBits_function_0084864C.md) (function, `0x0084864C`)
- `0x00845D64` → [CmpFindNameInListWithStatus](CmpFindNameInListWithStatus_function_00846B80.md) (function, `0x00846B80`)
- `0x00845DD2` → [CmpAddValueKeyNew](../85/CmpAddValueKeyNew_function_0085AA58.md) (function, `0x0085AA58`)
- `0x00845E0F` → [CmpAddValueToListEx](../85/CmpAddValueToListEx_function_0085B460.md) (function, `0x0085B460`)
- `0x00845E22` → [HvUnlockHiveFlusherShared](HvUnlockHiveFlusherShared_function_00848738.md) (function, `0x00848738`)
- `0x00845E4E` → [CmAddLogForAction](CmAddLogForAction_function_008445AC.md) (function, `0x008445AC`)
- `0x00845EB6` → [CmpReportNotifyHelper](../8C/CmpReportNotifyHelper_function_008C7230.md) (function, `0x008C7230`)
- `0x00845EDF` → [CmpReportNotifyHelper](../8C/CmpReportNotifyHelper_function_008C7230.md) (function, `0x008C7230`)
- `0x00845F06` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00845F53` → [CmpUnlockKcbStack](CmpUnlockKcbStack_function_00848460.md) (function, `0x00848460`)
- `0x00845F5E` → [CmpDrainDelayDerefContext](../../text/41/CmpDrainDelayDerefContext_function_0041B9A0.md) (function, `0x0041B9A0`)
- `0x00845F68` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x00845F7B` → [CmpSignalDeferredPosts](CmpSignalDeferredPosts_function_008484B0.md) (function, `0x008484B0`)
- `0x00845F87` → [CmpDetachFromRegistryProcess](../../pagecmrc/BC/CmpDetachFromRegistryProcess_function_00BC9920.md) (function, `0x00BC9920`)
- `0x00845F90` → [SeReleaseSubjectContext](../86/SeReleaseSubjectContext_function_0086B710.md) (function, `0x0086B710`)
- `0x00845FC8` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (function, `0x00475D80`)
- `0x00845FD9` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00846046` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (function, `0x00BC92C0`)
- `0x0084607C` → [CmpLockKcbExclusive](../86/CmpLockKcbExclusive_function_00861EB0.md) (function, `0x00861EB0`)
- `0x008460DD` → [CmpAllocateUnitOfWork](CmpAllocateUnitOfWork_function_00844BB0.md) (function, `0x00844BB0`)
- `0x008460F8` → [CmpTransEnlistUowInKcb](../../text/48/CmpTransEnlistUowInKcb_function_0048F094.md) (function, `0x0048F094`)
- `0x00846103` → [CmpTransEnlistUowInCmTrans](../../text/48/CmpTransEnlistUowInCmTrans_function_0048B330.md) (function, `0x0048B330`)
- `0x00846121` → [CmpLockIXLockIntent](CmpLockIXLockIntent_function_00844C08.md) (function, `0x00844C08`)
- `0x0084613F` → [CmpLockIXLockExclusive](CmpLockIXLockExclusive_function_00844CB4.md) (function, `0x00844CB4`)
- `0x00846151` → [HvLockHiveFlusherShared](HvLockHiveFlusherShared_function_0084F95C.md) (function, `0x0084F95C`)
- `0x00846166` → [CmpCloneKCBValueListForTrans](CmpCloneKCBValueListForTrans_function_00844D30.md) (function, `0x00844D30`)
- `0x0084617A` → [HvUnlockHiveFlusherShared](HvUnlockHiveFlusherShared_function_00848738.md) (function, `0x00848738`)
- `0x00846199` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x008461D9` → [CmpSetValueKeyNew](../85/CmpSetValueKeyNew_function_0085BB44.md) (function, `0x0085BB44`)
- `0x0084624A` → [HvUnlockHiveFlusherShared](HvUnlockHiveFlusherShared_function_00848738.md) (function, `0x00848738`)
- `0x0084625B` → [CmpFindNameInListWithStatus](CmpFindNameInListWithStatus_function_00846B80.md) (function, `0x00846B80`)
- `0x008462B5` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (function, `0x00BC92C0`)
- `0x008462DC` → [CmpPromoteKey](CmpPromoteKey_function_00844388.md) (function, `0x00844388`)
- `0x0084633F` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x0084636F` → [CmpSetValueKeyExisting](CmpSetValueKeyExisting_function_0084B53C.md) (function, `0x0084B53C`)
- `0x0084638B` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x008463B1` → [CmpLockKcbExclusive](../86/CmpLockKcbExclusive_function_00861EB0.md) (function, `0x00861EB0`)
- `0x00846405` → [CmpSwapValueInList](../../text/4A/CmpSwapValueInList_function_004A266C.md) (function, `0x004A266C`)
- `0x0084640F` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x0084641E` → [CmpLockKcbExclusive](../86/CmpLockKcbExclusive_function_00861EB0.md) (function, `0x00861EB0`)
- `0x00846444` → [CmpAllocatePool](../../text/3C/CmpAllocatePool_function_003CD504.md) (function, `0x003CD504`)
- `0x00846482` → [CmpDelayDerefKeyControlBlock](CmpDelayDerefKeyControlBlock_function_0084FA50.md) (function, `0x0084FA50`)
- `0x008464AC` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x008464D4` → [CmpLockKcbShared](../../pagecmrc/BC/CmpLockKcbShared_function_00BC9A1C.md) (function, `0x00BC9A1C`)
- `0x00846534` → [CmpLockKcbShared](../../pagecmrc/BC/CmpLockKcbShared_function_00BC9A1C.md) (function, `0x00BC9A1C`)
- `0x00846582` → [RtlEqualUnicodeString](../93/RtlEqualUnicodeString_function_00932A20.md) (function, `0x00932A20`)
- `0x00846594` → [RtlIsSandboxedToken](../8B/RtlIsSandboxedToken_function_008B3AB0.md) (function, `0x008B3AB0`)
- `0x008465AB` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x008465D7` → [CmpGetSecurityCacheEntryForKcbStack](../8C/CmpGetSecurityCacheEntryForKcbStack_function_008C7580.md) (function, `0x008C7580`)
- `0x008465ED` → [CmpAllocatePool](../../text/3C/CmpAllocatePool_function_003CD504.md) (function, `0x003CD504`)
- `0x00846639` → [CmpSnapshotTxOwnerArray](CmpSnapshotTxOwnerArray_function_00846808.md) (function, `0x00846808`)
- `0x00846658` → [CmpLogTransactionAbortedWithChildName](../9A/CmpLogTransactionAbortedWithChildName_function_009AED70.md) (function, `0x009AED70`)
- `0x00846662` → [CmpUnlockKcbStack](CmpUnlockKcbStack_function_00848460.md) (function, `0x00848460`)
- `0x00846676` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (function, `0x00475D80`)
- `0x0084668C` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x008466B3` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (function, `0x00475D80`)
- `0x008466D9` → [KeDelayExecutionThread](../../text/20/KeDelayExecutionThread_function_00209550.md) (function, `0x00209550`)
- `0x00846702` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x0084672B` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x0084679E` → [CmpFreeValue](CmpFreeValue_function_0084AF98.md) (function, `0x0084AF98`)
- `0x008467AB` → [CmpRundownUnitOfWork](../87/CmpRundownUnitOfWork_function_0087497C.md) (function, `0x0087497C`)
- `0x008467B9` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008467C7` → [HvFreeCell](../85/HvFreeCell_function_0085A72C.md) (function, `0x0085A72C`)
- `0x008467D5` → [HvUnlockHiveFlusherShared](HvUnlockHiveFlusherShared_function_00848738.md) (function, `0x00848738`)
- `0x008467E4` → [CmpFreePoolWithTag](../../text/44/CmpFreePoolWithTag_function_004489E0.md) (function, `0x004489E0`)
- `0x008467F6` → [CmpFreePoolWithTag](../../text/44/CmpFreePoolWithTag_function_004489E0.md) (function, `0x004489E0`)

### Direct callers
- [NtSetValueKey](NtSetValueKey_function_00844EA0.md) at `0x008454C7`

### Static image references
- `0x008457DC` → RVA `0x00E0A740` (`.data`; read)
- `0x00845EBB` → RVA `0x00FD9A90` (`PAGEDATA`; read)
- `0x00846578` → RVA `0x00FD9C00` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **33**
  - `0x0084588E` → [CmpInitializeDelayDerefContext](../../text/42/CmpInitializeDelayDerefContext_function_0042A7F0.md) (`PAGE` → `.text`)
  - `0x008458DD` → [CmpAttachToRegistryProcess](../../pagecmrc/BC/CmpAttachToRegistryProcess_function_00BC98E0.md) (`PAGE` → `PAGECMRC`)
  - `0x008458F0` → [CmpIsShutdownRundownActive](../../pagecmrc/BC/CmpIsShutdownRundownActive_function_00BC9C20.md) (`PAGE` → `PAGECMRC`)
  - `0x00845900` → [CmpLockRegistry](../../pagecmrc/BC/CmpLockRegistry_function_00BC9B34.md) (`PAGE` → `PAGECMRC`)
  - `0x008459A4` → [CmpIsKeyDeletedForKeyBody](../../pagecmrc/BC/CmpIsKeyDeletedForKeyBody_function_00BC9480.md) (`PAGE` → `PAGECMRC`)
  - `0x00845A15` → [CmpLockKcbShared](../../pagecmrc/BC/CmpLockKcbShared_function_00BC9A1C.md) (`PAGE` → `PAGECMRC`)
  - `0x00845A4B` → [CmpIsKeyDeletedForKeyBody](../../pagecmrc/BC/CmpIsKeyDeletedForKeyBody_function_00BC9480.md) (`PAGE` → `PAGECMRC`)
  - `0x00845AA8` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00845AF3` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (`PAGE` → `PAGECMRC`)
  - `0x00845B16` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (`PAGE` → `.text`)
  - `0x00845B32` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x00845C70` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (`PAGE` → `PAGECMRC`)
  - `0x00845F5E` → [CmpDrainDelayDerefContext](../../text/41/CmpDrainDelayDerefContext_function_0041B9A0.md) (`PAGE` → `.text`)
  - `0x00845F68` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x00845F87` → [CmpDetachFromRegistryProcess](../../pagecmrc/BC/CmpDetachFromRegistryProcess_function_00BC9920.md) (`PAGE` → `PAGECMRC`)
  - `0x00845FC8` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (`PAGE` → `.text`)
  - `0x00845FD9` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x00846046` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (`PAGE` → `PAGECMRC`)
  - `0x008460F8` → [CmpTransEnlistUowInKcb](../../text/48/CmpTransEnlistUowInKcb_function_0048F094.md) (`PAGE` → `.text`)
  - `0x00846103` → [CmpTransEnlistUowInCmTrans](../../text/48/CmpTransEnlistUowInCmTrans_function_0048B330.md) (`PAGE` → `.text`)
  - `0x008462B5` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (`PAGE` → `PAGECMRC`)
  - `0x00846405` → [CmpSwapValueInList](../../text/4A/CmpSwapValueInList_function_004A266C.md) (`PAGE` → `.text`)
  - `0x00846444` → [CmpAllocatePool](../../text/3C/CmpAllocatePool_function_003CD504.md) (`PAGE` → `.text`)
  - `0x008464D4` → [CmpLockKcbShared](../../pagecmrc/BC/CmpLockKcbShared_function_00BC9A1C.md) (`PAGE` → `PAGECMRC`)
  - `0x00846534` → [CmpLockKcbShared](../../pagecmrc/BC/CmpLockKcbShared_function_00BC9A1C.md) (`PAGE` → `PAGECMRC`)
  - `0x008465ED` → [CmpAllocatePool](../../text/3C/CmpAllocatePool_function_003CD504.md) (`PAGE` → `.text`)
  - `0x00846676` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (`PAGE` → `.text`)
  - `0x0084668C` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x008466B3` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (`PAGE` → `.text`)
  - `0x008466D9` → [KeDelayExecutionThread](../../text/20/KeDelayExecutionThread_function_00209550.md) (`PAGE` → `.text`)
  - `0x008467B9` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008467E4` → [CmpFreePoolWithTag](../../text/44/CmpFreePoolWithTag_function_004489E0.md) (`PAGE` → `.text`)
  - `0x008467F6` → [CmpFreePoolWithTag](../../text/44/CmpFreePoolWithTag_function_004489E0.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **10**
  - `0x00845AB4` → [sub_00B160F4 + 0x3D](../B1/Unknown_function_00B160F4.md) (`tail-transfer`)
  - `0x00845FA4` → [sub_00B160F4 + 0x1EB](../B1/Unknown_function_00B160F4.md) (`tail-transfer`)
  - `0x0084666D` → [sub_00B160F4](../B1/Unknown_function_00B160F4.md) (`tail-transfer`)
  - `0x0084667C` → [sub_00B160F4](../B1/Unknown_function_00B160F4.md) (`tail-transfer`)
  - `0x008466C4` → [sub_00B160F4 + 0xA5](../B1/Unknown_function_00B160F4.md) (`tail-transfer`)
  - `0x008466FC` → [sub_00B160F4 + 0x11E](../B1/Unknown_function_00B160F4.md) (`tail-transfer`)
  - `0x00846708` → [sub_00B160F4 + 0x123](../B1/Unknown_function_00B160F4.md) (`tail-transfer`)
  - `0x00846710` → [sub_00B160F4 + 0x1A2](../B1/Unknown_function_00B160F4.md) (`tail-transfer`)
  - `0x00846725` → [sub_00B160F4 + 0x19A](../B1/Unknown_function_00B160F4.md) (`tail-transfer`)
  - `0x00846731` → [sub_00B160F4 + 0x19F](../B1/Unknown_function_00B160F4.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
008457C0  40 55                           push rbp
008457C2  53                              push rbx
008457C3  56                              push rsi
008457C4  57                              push rdi
008457C5  41 54                           push r12
008457C7  41 55                           push r13
008457C9  41 56                           push r14
008457CB  41 57                           push r15
008457CD  48 8D AC 24 38 FF FF FF         lea rbp, [rsp - 0xc8]
008457D5  48 81 EC C8 01 00 00            sub rsp, 0x1c8
008457DC  48 8B 05 5D 4F 5C 00            mov rax, qword ptr [rip + 0x5c4f5d]
008457E3  48 33 C4                        xor rax, rsp
008457E6  48 89 85 B8 00 00 00            mov qword ptr [rbp + 0xb8], rax
008457ED  48 8B 85 38 01 00 00            mov rax, qword ptr [rbp + 0x138]
008457F4  45 33 FF                        xor r15d, r15d
008457F7  0F 57 C0                        xorps xmm0, xmm0
008457FA  48 89 45 20                     mov qword ptr [rbp + 0x20], rax
008457FE  48 8D 45 00                     lea rax, [rbp]
00845802  48 89 4D F8                     mov qword ptr [rbp - 8], rcx
00845806  48 89 45 08                     mov qword ptr [rbp + 8], rax
0084580A  4C 8B F1                        mov r14, rcx
0084580D  48 8D 45 00                     lea rax, [rbp]
00845811  4C 89 4D F0                     mov qword ptr [rbp - 0x10], r9
00845815  48 89 45 00                     mov qword ptr [rbp], rax
00845819  48 8D 4D C0                     lea rcx, [rbp - 0x40]
0084581D  B8 FF FF FF FF                  mov eax, 0xffffffff
00845822  44 89 45 8C                     mov dword ptr [rbp - 0x74], r8d
00845826  0F 11 44 24 68                  movups xmmword ptr [rsp + 0x68], xmm0
0084582B  66 89 44 24 6A                  mov word ptr [rsp + 0x6a], ax
00845830  48 89 55 B0                     mov qword ptr [rbp - 0x50], rdx
00845834  44 89 7D A0                     mov dword ptr [rbp - 0x60], r15d
00845838  4C 89 7D E8                     mov qword ptr [rbp - 0x18], r15
0084583C  4C 89 7D C0                     mov qword ptr [rbp - 0x40], r15
00845840  44 89 7D A8                     mov dword ptr [rbp - 0x58], r15d
00845844  4C 89 7D 98                     mov qword ptr [rbp - 0x68], r15
00845848  0F 11 85 88 00 00 00            movups xmmword ptr [rbp + 0x88], xmm0
0084584F  4C 89 7D C8                     mov qword ptr [rbp - 0x38], r15
00845853  0F 11 85 98 00 00 00            movups xmmword ptr [rbp + 0x98], xmm0
0084585A  44 88 7C 24 50                  mov byte ptr [rsp + 0x50], r15b
0084585F  0F 11 85 A8 00 00 00            movups xmmword ptr [rbp + 0xa8], xmm0
00845866  44 89 7D A4                     mov dword ptr [rbp - 0x5c], r15d
0084586A  0F 11 45 28                     movups xmmword ptr [rbp + 0x28], xmm0
0084586E  4C 89 7D E0                     mov qword ptr [rbp - 0x20], r15
00845872  0F 11 44 24 78                  movups xmmword ptr [rsp + 0x78], xmm0
00845877  4C 89 7C 24 58                  mov qword ptr [rsp + 0x58], r15
0084587C  E8 8F 06 01 00                  call 0x140855f10
00845881  48 8D 4D 98                     lea rcx, [rbp - 0x68]
00845885  E8 86 06 01 00                  call 0x140855f10
0084588A  48 8D 4D 28                     lea rcx, [rbp + 0x28]
0084588E  E8 5D 4F BE FF                  call 0x14042a7f0
00845893  0F 11 45 38                     movups xmmword ptr [rbp + 0x38], xmm0
00845897  48 8D 4D 68                     lea rcx, [rbp + 0x68]
0084589B  C7 45 D8 FF FF FF FF            mov dword ptr [rbp - 0x28], 0xffffffff
008458A2  0F 11 45 48                     movups xmmword ptr [rbp + 0x48], xmm0
008458A6  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008458AF  C7 45 88 FF FF FF FF            mov dword ptr [rbp - 0x78], 0xffffffff
008458B6  4C 89 7D D0                     mov qword ptr [rbp - 0x30], r15
008458BA  44 89 7D 90                     mov dword ptr [rbp - 0x70], r15d
008458BE  0F B6 80 32 02 00 00            movzx eax, byte ptr [rax + 0x232]
008458C5  88 44 24 60                     mov byte ptr [rsp + 0x60], al
008458C9  0F 11 45 68                     movups xmmword ptr [rbp + 0x68], xmm0
008458CD  0F 11 45 78                     movups xmmword ptr [rbp + 0x78], xmm0
008458D1  E8 4A 5F 02 00                  call 0x14086b820
008458D6  48 8D 8D 88 00 00 00            lea rcx, [rbp + 0x88]
008458DD  E8 FE 3F 38 00                  call 0x140bc98e0
008458E2  48 B9 14 00 00 00 80 F7 FF FF   movabs rcx, 0xfffff78000000014
008458EC  0F 1F 40 00                     nop dword ptr [rax]
008458F0  E8 2B 43 38 00                  call 0x140bc9c20
008458F5  84 C0                           test al, al
008458F7  0F 85 B8 0C 00 00               jne 0x1408465b5
008458FD  48 8B 19                        mov rbx, qword ptr [rcx]
00845900  E8 2F 42 38 00                  call 0x140bc9b34
00845905  4D 8B 66 08                     mov r12, qword ptr [r14 + 8]
00845909  C6 44 24 41 01                  mov byte ptr [rsp + 0x41], 1
0084590E  4C 89 64 24 58                  mov qword ptr [rsp + 0x58], r12
00845913  49 8B 44 24 20                  mov rax, qword ptr [r12 + 0x20]
00845918  F7 80 A0 00 00 00 00 00 10 00   test dword ptr [rax + 0xa0], 0x100000
00845922  0F 85 C3 0B 00 00               jne 0x1408464eb
00845928  41 0F BF 7C 24 42               movsx edi, word ptr [r12 + 0x42]
0084592E  4D 8B EF                        mov r13, r15
00845931  4C 89 7C 24 48                  mov qword ptr [rsp + 0x48], r15
00845936  83 FF 02                        cmp edi, 2
00845939  7C 0B                           jl 0x140845946
0084593B  8B C7                           mov eax, edi
0084593D  83 E8 01                        sub eax, 1
00845940  0F 85 ED 0A 00 00               jne 0x140846433
00845946  49 0F BF 74 24 42               movsx rsi, word ptr [r12 + 0x42]
0084594C  66 89 7C 24 68                  mov word ptr [rsp + 0x68], di
00845951  4C 89 6D 80                     mov qword ptr [rbp - 0x80], r13
00845955  66 89 74 24 6A                  mov word ptr [rsp + 0x6a], si
0084595A  66 85 F6                        test si, si
0084595D  0F 85 58 0A 00 00               jne 0x1408463bb
00845963  4C 89 64 F4 70                  mov qword ptr [rsp + rsi*8 + 0x70], r12
00845968  4C 8B 6D 80                     mov r13, qword ptr [rbp - 0x80]
0084596C  0F B7 74 24 6A                  movzx esi, word ptr [rsp + 0x6a]
00845971  4C 89 6C 24 48                  mov qword ptr [rsp + 0x48], r13
00845976  49 83 7E 38 00                  cmp qword ptr [r14 + 0x38], 0
0084597B  74 63                           je 0x1408459e0
0084597D  48 8D 4C 24 68                  lea rcx, [rsp + 0x68]
00845982  E8 7D 11 00 00                  call 0x140846b04
00845987  41 B7 01                        mov r15b, 1
0084598A  49 83 7E 38 00                  cmp qword ptr [r14 + 0x38], 0
0084598F  44 88 7C 24 43                  mov byte ptr [rsp + 0x43], r15b
00845994  C6 44 24 40 01                  mov byte ptr [rsp + 0x40], 1
00845999  0F 84 93 00 00 00               je 0x140845a32
0084599F  33 D2                           xor edx, edx
008459A1  49 8B CE                        mov rcx, r14
008459A4  E8 D7 3A 38 00                  call 0x140bc9480
008459A9  84 C0                           test al, al
008459AB  0F 85 CF 0D 00 00               jne 0x140846780
008459B1  48 8D 55 E0                     lea rdx, [rbp - 0x20]
008459B5  49 8B CE                        mov rcx, r14
008459B8  E8 FB DC 02 00                  call 0x1408736b8
008459BD  8B F8                           mov edi, eax
008459BF  85 C0                           test eax, eax
008459C1  78 15                           js 0x1408459d8
008459C3  49 8B 44 24 20                  mov rax, qword ptr [r12 + 0x20]
008459C8  8B 88 A0 00 00 00               mov ecx, dword ptr [rax + 0xa0]
008459CE  F6 C1 02                        test cl, 2
008459D1  74 6A                           je 0x140845a3d
008459D3  BF 01 00 19 C0                  mov edi, 0xc0190001
008459D8  45 32 E4                        xor r12b, r12b
008459DB  E9 A6 07 00 00                  jmp 0x140846186
008459E0  49 83 7E 40 00                  cmp qword ptr [r14 + 0x40], 0
008459E5  75 96                           jne 0x14084597d
008459E7  41 0F B7 FF                     movzx edi, r15w
008459EB  66 44 3B FE                     cmp r15w, si
008459EF  7F 39                           jg 0x140845a2a
008459F1  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
008459F6  4D 8B FD                        mov r15, r13
008459F9  4C 2B F9                        sub r15, rcx
008459FC  4C 8D 74 24 70                  lea r14, [rsp + 0x70]
00845A01  49 83 C7 F0                     add r15, -0x10
00845A05  66 83 FF 02                     cmp di, 2
00845A09  0F 8D 8B 06 00 00               jge 0x14084609a
00845A0F  49 8B CE                        mov rcx, r14
00845A12  48 8B 09                        mov rcx, qword ptr [rcx]
00845A15  E8 02 40 38 00                  call 0x140bc9a1c
00845A1A  66 FF C7                        inc di
00845A1D  49 83 C6 08                     add r14, 8
00845A21  66 3B FE                        cmp di, si
00845A24  7E DF                           jle 0x140845a05
00845A26  4C 8B 75 F8                     mov r14, qword ptr [rbp - 8]
00845A2A  45 32 FF                        xor r15b, r15b
00845A2D  E9 58 FF FF FF                  jmp 0x14084598a
00845A32  49 83 7E 40 00                  cmp qword ptr [r14 + 0x40], 0
00845A37  0F 85 62 FF FF FF               jne 0x14084599f
00845A3D  4C 8B 75 E0                     mov r14, qword ptr [rbp - 0x20]
00845A41  48 8B 7D F8                     mov rdi, qword ptr [rbp - 8]
00845A45  49 8B D6                        mov rdx, r14
00845A48  48 8B CF                        mov rcx, rdi
00845A4B  E8 30 3A 38 00                  call 0x140bc9480
00845A50  84 C0                           test al, al
00845A52  0F 85 1F 0D 00 00               jne 0x140846777
00845A58  41 80 7C 24 41 01               cmp byte ptr [r12 + 0x41], 1
00845A5E  0F 84 09 0D 00 00               je 0x14084676d
00845A64  4D 85 F6                        test r14, r14
00845A67  0F 85 70 06 00 00               jne 0x1408460dd
00845A6D  49 8D 8C 24 F8 00 00 00         lea rcx, [r12 + 0xf8]
00845A75  44 39 31                        cmp dword ptr [rcx], r14d
00845A78  0F 8D E7 00 00 00               jge 0x140845b65
00845A7E  4C 8D 45 E8                     lea r8, [rbp - 0x18]
00845A82  48 8D 55 A0                     lea rdx, [rbp - 0x60]
00845A86  E8 7D 0D 00 00                  call 0x140846808
00845A8B  8B F8                           mov edi, eax
00845A8D  85 C0                           test eax, eax
00845A8F  0F 88 43 FF FF FF               js 0x1408459d8
00845A95  0F 57 C0                        xorps xmm0, xmm0
00845A98  48 8D 4D 58                     lea rcx, [rbp + 0x58]
00845A9C  33 FF                           xor edi, edi
00845A9E  33 D2                           xor edx, edx
00845AA0  0F 11 45 58                     movups xmmword ptr [rbp + 0x58], xmm0
00845AA4  48 89 7D 10                     mov qword ptr [rbp + 0x10], rdi
00845AA8  E8 D3 4C BE FF                  call 0x14042a780
00845AAD  44 8B 75 A0                     mov r14d, dword ptr [rbp - 0x60]
00845AB1  45 85 F6                        test r14d, r14d
00845AB4  0F 85 77 06 2D 00               jne 0x140b16131
00845ABA  48 8B 4D 60                     mov rcx, qword ptr [rbp + 0x60]
00845ABE  48 85 C9                        test rcx, rcx
00845AC1  0F 85 EC 0B 00 00               jne 0x1408466b3
00845AC7  0F B7 DF                        movzx ebx, di
00845ACA  66 3B FE                        cmp di, si
00845ACD  7F 37                           jg 0x140845b06
00845ACF  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
00845AD4  4D 8B FD                        mov r15, r13
00845AD7  4C 2B F9                        sub r15, rcx
00845ADA  48 8D 7C 24 70                  lea rdi, [rsp + 0x70]
00845ADF  49 83 C7 F0                     add r15, -0x10
00845AE3  66 83 FB 02                     cmp bx, 2
00845AE7  0F 8D A4 05 00 00               jge 0x140846091
00845AED  48 8B CF                        mov rcx, rdi
00845AF0  48 8B 09                        mov rcx, qword ptr [rcx]
00845AF3  E8 C8 37 38 00                  call 0x140bc92c0
00845AF8  66 FF C3                        inc bx
00845AFB  48 83 C7 08                     add rdi, 8
00845AFF  66 3B DE                        cmp bx, si
00845B02  7E DF                           jle 0x140845ae3
00845B04  33 FF                           xor edi, edi
00845B06  45 32 FF                        xor r15b, r15b
00845B09  44 88 7C 24 40                  mov byte ptr [rsp + 0x40], r15b
00845B0E  4D 85 ED                        test r13, r13
00845B11  74 08                           je 0x140845b1b
00845B13  49 8B CD                        mov rcx, r13
00845B16  E8 65 02 C3 FF                  call 0x140475d80
00845B1B  0F 57 C0                        xorps xmm0, xmm0
00845B1E  B8 FF FF FF FF                  mov eax, 0xffffffff
00845B23  0F 11 44 24 68                  movups xmmword ptr [rsp + 0x68], xmm0
00845B28  66 89 44 24 6A                  mov word ptr [rsp + 0x6a], ax
00845B2D  0F 11 44 24 78                  movups xmmword ptr [rsp + 0x78], xmm0
00845B32  E8 4D 3F 38 00                  call 0x140bc9a84
00845B37  45 85 F6                        test r14d, r14d
00845B3A  0F 85 7D 0B 00 00               jne 0x1408466bd
00845B40  8B 45 A4                        mov eax, dword ptr [rbp - 0x5c]
00845B43  FF C0                           inc eax
00845B45  89 45 A4                        mov dword ptr [rbp - 0x5c], eax
00845B48  83 F8 0A                        cmp eax, 0xa
00845B4B  0F 87 78 0B 00 00               ja 0x1408466c9
00845B51  85 FF                           test edi, edi
00845B53  0F 88 A6 09 00 00               js 0x1408464ff
00845B59  4C 8B 75 F8                     mov r14, qword ptr [rbp - 8]
00845B5D  45 33 FF                        xor r15d, r15d
00845B60  E9 7D FD FF FF                  jmp 0x1408458e2
00845B65  49 8D 8C 24 08 01 00 00         lea rcx, [r12 + 0x108]
00845B6D  83 39 00                        cmp dword ptr [rcx], 0
00845B70  0F 85 BB 0A 00 00               jne 0x140846631
00845B76  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
00845B7B  45 32 E4                        xor r12b, r12b
00845B7E  0F B7 C6                        movzx eax, si
00845B81  44 88 64 24 42                  mov byte ptr [rsp + 0x42], r12b
00845B86  66 85 C0                        test ax, ax
00845B89  78 2E                           js 0x140845bb9
00845B8B  48 0F BF C8                     movsx rcx, ax
00845B8F  66 83 F8 02                     cmp ax, 2
00845B93  0F 8D 88 07 00 00               jge 0x140846321
00845B99  48 8B 4C CC 70                  mov rcx, qword ptr [rsp + rcx*8 + 0x70]
00845B9E  83 79 28 FF                     cmp dword ptr [rcx + 0x28], -1
00845BA2  0F 84 FC 07 00 00               je 0x1408463a4
00845BA8  8B 81 B8 00 00 00               mov eax, dword ptr [rcx + 0xb8]
00845BAE  C1 E8 14                        shr eax, 0x14
00845BB1  A8 01                           test al, 1
00845BB3  0F 85 9C 09 00 00               jne 0x140846555
00845BB9  83 7F 28 FF                     cmp dword ptr [rdi + 0x28], -1
00845BBD  0F 84 C4 06 00 00               je 0x140846287
00845BC3  45 84 FF                        test r15b, r15b
00845BC6  0F 85 D7 04 00 00               jne 0x1408460a3
00845BCC  8B 85 30 01 00 00               mov eax, dword ptr [rbp + 0x130]
00845BD2  48 8B CF                        mov rcx, rdi
00845BD5  4C 8B 4D F0                     mov r9, qword ptr [rbp - 0x10]
00845BD9  44 8B 45 8C                     mov r8d, dword ptr [rbp - 0x74]
00845BDD  48 8B 55 B0                     mov rdx, qword ptr [rbp - 0x50]
00845BE1  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00845BE5  E8 36 0D 00 00                  call 0x140846920
00845BEA  83 F8 01                        cmp eax, 1
00845BED  0F 84 25 04 00 00               je 0x140846018
00845BF3  85 C0                           test eax, eax
00845BF5  0F 84 89 05 00 00               je 0x140846184
00845BFB  4C 8B 64 24 58                  mov r12, qword ptr [rsp + 0x58]
00845C00  41 B7 01                        mov r15b, 1
00845C03  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00845C0C  44 88 7C 24 43                  mov byte ptr [rsp + 0x43], r15b
00845C11  49 39 44 24 38                  cmp qword ptr [r12 + 0x38], rax
00845C16  0F 84 94 00 00 00               je 0x140845cb0
00845C1C  B8 11 00 00 00                  mov eax, 0x11
00845C21  B9 01 00 00 00                  mov ecx, 1
00845C26  F0 49 0F B1 4C 24 30            lock cmpxchg qword ptr [r12 + 0x30], rcx
00845C2D  0F 84 C0 03 00 00               je 0x140845ff3
00845C33  48 0F BF 74 24 6A               movsx rsi, word ptr [rsp + 0x6a]
00845C39  33 C0                           xor eax, eax
00845C3B  4C 8B 6D 80                     mov r13, qword ptr [rbp - 0x80]
00845C3F  0F B7 F8                        movzx edi, ax
00845C42  4C 89 6C 24 48                  mov qword ptr [rsp + 0x48], r13
00845C47  66 3B C6                        cmp ax, si
00845C4A  7F 3D                           jg 0x140845c89
00845C4C  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
00845C51  4D 8B FD                        mov r15, r13
00845C54  4C 2B F9                        sub r15, rcx
00845C57  4C 8D 74 24 70                  lea r14, [rsp + 0x70]
00845C5C  49 83 C7 F0                     add r15, -0x10
00845C60  66 83 FF 02                     cmp di, 2
00845C64  0F 8D 26 05 00 00               jge 0x140846190
00845C6A  49 8B CE                        mov rcx, r14
00845C6D  48 8B 09                        mov rcx, qword ptr [rcx]
00845C70  E8 4B 36 38 00                  call 0x140bc92c0
00845C75  66 FF C7                        inc di
00845C78  49 83 C6 08                     add r14, 8
00845C7C  66 3B FE                        cmp di, si
00845C7F  7E DF                           jle 0x140845c60
00845C81  44 0F B6 7C 24 43               movzx r15d, byte ptr [rsp + 0x43]
00845C87  33 C0                           xor eax, eax
00845C89  8B FE                           mov edi, esi
00845C8B  44 0F B7 F0                     movzx r14d, ax
00845C8F  83 EF 01                        sub edi, 1
00845C92  0F 89 28 08 00 00               jns 0x1408464c0
00845C98  83 FE 02                        cmp esi, 2
00845C9B  0F 8D 0B 07 00 00               jge 0x1408463ac
00845CA1  48 8B 4C F4 70                  mov rcx, qword ptr [rsp + rsi*8 + 0x70]
00845CA6  E8 05 C2 01 00                  call 0x140861eb0
00845CAB  E9 8D FD FF FF                  jmp 0x140845a3d
00845CB0  48 8B 45 80                     mov rax, qword ptr [rbp - 0x80]
00845CB4  0F B7 74 24 6A                  movzx esi, word ptr [rsp + 0x6a]
00845CB9  4C 8B 75 E0                     mov r14, qword ptr [rbp - 0x20]
00845CBD  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00845CC2  49 8B 4C 24 20                  mov rcx, qword ptr [r12 + 0x20]
00845CC7  49 FF 84 24 30 01 00 00         inc qword ptr [r12 + 0x130]
00845CCF  E8 88 9C 00 00                  call 0x14084f95c
00845CD4  41 B4 01                        mov r12b, 1
00845CD7  44 88 64 24 42                  mov byte ptr [rsp + 0x42], r12b
00845CDC  4D 85 F6                        test r14, r14
00845CDF  75 21                           jne 0x140845d02
00845CE1  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00845CE6  45 33 C9                        xor r9d, r9d
00845CE9  45 33 C0                        xor r8d, r8d
00845CEC  8B 51 28                        mov edx, dword ptr [rcx + 0x28]
00845CEF  48 8B 49 20                     mov rcx, qword ptr [rcx + 0x20]
00845CF3  E8 88 23 01 00                  call 0x140858080
00845CF8  8B F8                           mov edi, eax
00845CFA  85 C0                           test eax, eax
00845CFC  0F 88 84 04 00 00               js 0x140846186
00845D02  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
00845D07  4C 8D 45 C0                     lea r8, [rbp - 0x40]
00845D0B  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
00845D0F  8B 57 28                        mov edx, dword ptr [rdi + 0x28]
00845D12  44 84 A1 8C 00 00 00            test byte ptr [rcx + 0x8c], r12b
00845D19  0F 84 7A 04 00 00               je 0x140846199
00845D1F  E8 3C EF 00 00                  call 0x140854c60
00845D24  44 8B 47 28                     mov r8d, dword ptr [rdi + 0x28]
00845D28  48 8B D0                        mov rdx, rax
00845D2B  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
00845D2F  4C 8B F8                        mov r15, rax
00845D32  E8 15 29 00 00                  call 0x14084864c
00845D37  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
00845D3B  48 8D 45 D8                     lea rax, [rbp - 0x28]
00845D3F  4C 8B 45 B0                     mov r8, qword ptr [rbp - 0x50]
00845D43  45 33 C9                        xor r9d, r9d
00845D46  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00845D4B  48 8D 45 A8                     lea rax, [rbp - 0x58]
00845D4F  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00845D54  4D 85 F6                        test r14, r14
00845D57  0F 84 FA 04 00 00               je 0x140846257
00845D5D  48 8D 97 18 01 00 00            lea rdx, [rdi + 0x118]
00845D64  E8 17 0E 00 00                  call 0x140846b80
00845D69  B9 00 00 00 80                  mov ecx, 0x80000000
00845D6E  8B F8                           mov edi, eax
00845D70  03 C1                           add eax, ecx
00845D72  85 C1                           test ecx, eax
00845D74  0F 84 88 05 00 00               je 0x140846302
00845D7A  80 BD 40 01 00 00 00            cmp byte ptr [rbp + 0x140], 0
00845D81  44 8B 65 D8                     mov r12d, dword ptr [rbp - 0x28]
00845D85  0F 85 41 08 00 00               jne 0x1408465cc
00845D8B  4C 8B 6C 24 58                  mov r13, qword ptr [rsp + 0x58]
00845D90  45 8B 6D 28                     mov r13d, dword ptr [r13 + 0x28]
00845D94  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00845D99  41 C1 ED 1F                     shr r13d, 0x1f
00845D9D  48 8B 49 20                     mov rcx, qword ptr [rcx + 0x20]
00845DA1  4D 85 F6                        test r14, r14
00845DA4  0F 84 F9 03 00 00               je 0x1408461a3
00845DAA  4C 8B 4D F0                     mov r9, qword ptr [rbp - 0x10]
00845DAE  48 8D 45 88                     lea rax, [rbp - 0x78]
00845DB2  44 8B 45 8C                     mov r8d, dword ptr [rbp - 0x74]
00845DB6  BE 01 00 00 00                  mov esi, 1
00845DBB  48 8B 55 B0                     mov rdx, qword ptr [rbp - 0x50]
00845DBF  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00845DC4  8B 85 30 01 00 00               mov eax, dword ptr [rbp + 0x130]
00845DCA  89 74 24 28                     mov dword ptr [rsp + 0x28], esi
00845DCE  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00845DD2  E8 81 4C 01 00                  call 0x14085aa58
00845DD7  8B F8                           mov edi, eax
00845DD9  85 C0                           test eax, eax
00845DDB  0F 88 79 09 00 00               js 0x14084675a
00845DE1  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
00845DE6  8B 55 88                        mov edx, dword ptr [rbp - 0x78]
00845DE9  49 8B 4E 20                     mov rcx, qword ptr [r14 + 0x20]
00845DED  49 8D 86 18 01 00 00            lea rax, [r14 + 0x118]
00845DF4  41 83 FC FF                     cmp r12d, -1
00845DF8  0F 85 FE 05 00 00               jne 0x1408463fc
00845DFE  8B 18                           mov ebx, dword ptr [rax]
00845E00  44 8B CE                        mov r9d, esi
00845E03  44 8B C3                        mov r8d, ebx
00845E06  89 74 24 28                     mov dword ptr [rsp + 0x28], esi
00845E0A  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00845E0F  E8 4C 56 01 00                  call 0x14085b460
00845E14  8B F8                           mov edi, eax
00845E16  85 C0                           test eax, eax
00845E18  0F 88 18 09 00 00               js 0x140846736
00845E1E  49 8B 4E 20                     mov rcx, qword ptr [r14 + 0x20]
00845E22  E8 11 29 00 00                  call 0x140848738
00845E27  48 8B 4D C8                     mov rcx, qword ptr [rbp - 0x38]
00845E2B  C6 44 24 42 00                  mov byte ptr [rsp + 0x42], 0
00845E30  41 83 FC FF                     cmp r12d, -1
00845E34  0F 85 64 06 00 00               jne 0x14084649e
00845E3A  B8 04 00 00 00                  mov eax, 4
00845E3F  89 41 44                        mov dword ptr [rcx + 0x44], eax
00845E42  8B D6                           mov edx, esi
00845E44  8B 45 88                        mov eax, dword ptr [rbp - 0x78]
00845E47  89 41 5C                        mov dword ptr [rcx + 0x5c], eax
00845E4A  44 89 69 48                     mov dword ptr [rcx + 0x48], r13d
00845E4E  E8 59 E7 FF FF                  call 0x1408445ac
00845E53  8B F8                           mov edi, eax
00845E55  85 C0                           test eax, eax
00845E57  0F 88 B0 08 00 00               js 0x14084670d
00845E5D  0F B7 74 24 6A                  movzx esi, word ptr [rsp + 0x6a]
00845E62  44 0F B6 64 24 42               movzx r12d, byte ptr [rsp + 0x42]
00845E68  45 33 F6                        xor r14d, r14d
00845E6B  C7 45 88 FF FF FF FF            mov dword ptr [rbp - 0x78], 0xffffffff
00845E72  4C 89 75 C8                     mov qword ptr [rbp - 0x38], r14
00845E76  44 88 74 24 50                  mov byte ptr [rsp + 0x50], r14b
00845E7B  0F AE E8                        lfence
00845E7E  48 0F BF 44 24 6A               movsx rax, word ptr [rsp + 0x6a]
00845E84  66 83 FE 02                     cmp si, 2
00845E88  48 8B 75 80                     mov rsi, qword ptr [rbp - 0x80]
00845E8C  0F 8D B9 06 00 00               jge 0x14084654b
00845E92  48 8B 5C C4 70                  mov rbx, qword ptr [rsp + rax*8 + 0x70]
00845E97  48 8B 7D E0                     mov rdi, qword ptr [rbp - 0x20]
00845E9B  48 8D 45 00                     lea rax, [rbp]
00845E9F  48 8B 53 20                     mov rdx, qword ptr [rbx + 0x20]
00845EA3  48 8D 4C 24 68                  lea rcx, [rsp + 0x68]
00845EA8  4C 8B C7                        mov r8, rdi
00845EAB  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00845EB0  41 B9 04 00 00 00               mov r9d, 4
00845EB6  E8 75 13 08 00                  call 0x1408c7230
00845EBB  48 8B 15 CE 3B 79 00            mov rdx, qword ptr [rip + 0x793bce]
00845EC2  48 39 53 20                     cmp qword ptr [rbx + 0x20], rdx
00845EC6  74 1C                           je 0x140845ee4
00845EC8  48 8D 45 00                     lea rax, [rbp]
00845ECC  41 B9 04 00 00 00               mov r9d, 4
00845ED2  4C 8B C7                        mov r8, rdi
00845ED5  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00845EDA  48 8D 4C 24 68                  lea rcx, [rsp + 0x68]
00845EDF  E8 4C 13 08 00                  call 0x1408c7230
00845EE4  41 8B FE                        mov edi, r14d
00845EE7  4C 8B 6C 24 58                  mov r13, qword ptr [rsp + 0x58]
00845EEC  4D 85 FF                        test r15, r15
00845EEF  74 1A                           je 0x140845f0b
00845EF1  49 8B 4D 20                     mov rcx, qword ptr [r13 + 0x20]
00845EF5  48 8D 55 C0                     lea rdx, [rbp - 0x40]
00845EF9  F6 81 8C 00 00 00 01            test byte ptr [rcx + 0x8c], 1
00845F00  0F 85 A6 05 00 00               jne 0x1408464ac
00845F06  E8 35 00 01 00                  call 0x140855f40
00845F0B  44 0F B6 7C 24 40               movzx r15d, byte ptr [rsp + 0x40]
00845F11  44 0F B6 74 24 41               movzx r14d, byte ptr [rsp + 0x41]
00845F17  8B 55 88                        mov edx, dword ptr [rbp - 0x78]
00845F1A  4C 8B 6C 24 58                  mov r13, qword ptr [rsp + 0x58]
00845F1F  83 FA FF                        cmp edx, -1
00845F22  0F 85 72 08 00 00               jne 0x14084679a
00845F28  48 8B 45 C8                     mov rax, qword ptr [rbp - 0x38]
00845F2C  48 85 C0                        test rax, rax
00845F2F  0F 85 73 08 00 00               jne 0x1408467a8
00845F35  80 7C 24 50 00                  cmp byte ptr [rsp + 0x50], 0
00845F3A  0F 85 6D 01 00 00               jne 0x1408460ad
00845F40  45 84 E4                        test r12b, r12b
00845F43  0F 85 88 08 00 00               jne 0x1408467d1
00845F49  45 84 FF                        test r15b, r15b
00845F4C  74 0A                           je 0x140845f58
00845F4E  48 8D 4C 24 68                  lea rcx, [rsp + 0x68]
00845F53  E8 08 25 00 00                  call 0x140848460
00845F58  33 D2                           xor edx, edx
00845F5A  48 8D 4D 28                     lea rcx, [rbp + 0x28]
00845F5E  E8 3D 5A BD FF                  call 0x14041b9a0
00845F63  45 84 F6                        test r14b, r14b
00845F66  74 05                           je 0x140845f6d
00845F68  E8 17 3B 38 00                  call 0x140bc9a84
00845F6D  48 8D 45 00                     lea rax, [rbp]
00845F71  48 39 45 00                     cmp qword ptr [rbp], rax
00845F75  74 09                           je 0x140845f80
00845F77  48 8D 4D 00                     lea rcx, [rbp]
00845F7B  E8 30 25 00 00                  call 0x1408484b0
00845F80  48 8D 8D 88 00 00 00            lea rcx, [rbp + 0x88]
00845F87  E8 94 39 38 00                  call 0x140bc9920
00845F8C  48 8D 4D 68                     lea rcx, [rbp + 0x68]
00845F90  E8 7B 57 02 00                  call 0x14086b710
00845F95  48 8B 5D D0                     mov rbx, qword ptr [rbp - 0x30]
00845F99  85 FF                           test edi, edi
00845F9B  78 0D                           js 0x140845faa
00845F9D  80 BD 40 01 00 00 00            cmp byte ptr [rbp + 0x140], 0
00845FA4  0F 85 35 03 2D 00               jne 0x140b162df
00845FAA  48 8B 4D 40                     mov rcx, qword ptr [rbp + 0x40]
00845FAE  48 85 C9                        test rcx, rcx
00845FB1  0F 85 28 08 00 00               jne 0x1408467df
00845FB7  48 85 DB                        test rbx, rbx
00845FBA  0F 85 2E 08 00 00               jne 0x1408467ee
00845FC0  48 85 F6                        test rsi, rsi
00845FC3  74 08                           je 0x140845fcd
00845FC5  48 8B CE                        mov rcx, rsi
00845FC8  E8 B3 FD C2 FF                  call 0x140475d80
00845FCD  8B C7                           mov eax, edi
00845FCF  48 8B 8D B8 00 00 00            mov rcx, qword ptr [rbp + 0xb8]
00845FD6  48 33 CC                        xor rcx, rsp
00845FD9  E8 62 66 E6 FF                  call 0x1406ac640
00845FDE  48 81 C4 C8 01 00 00            add rsp, 0x1c8
00845FE5  41 5F                           pop r15
00845FE7  41 5E                           pop r14
00845FE9  41 5D                           pop r13
00845FEB  41 5C                           pop r12
00845FED  5F                              pop rdi
00845FEE  5E                              pop rsi
00845FEF  5B                              pop rbx
00845FF0  5D                              pop rbp
00845FF1  C3                              ret
00845FF2  CC                              int3
00845FF3  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00845FFC  48 8B 7D 80                     mov rdi, qword ptr [rbp - 0x80]
00846000  0F B7 74 24 6A                  movzx esi, word ptr [rsp + 0x6a]
00846005  4C 8B 75 E0                     mov r14, qword ptr [rbp - 0x20]
00846009  48 89 7C 24 48                  mov qword ptr [rsp + 0x48], rdi
0084600E  49 89 44 24 38                  mov qword ptr [r12 + 0x38], rax
00846013  E9 AA FC FF FF                  jmp 0x140845cc2
00846018  33 C0                           xor eax, eax
0084601A  0F B7 F8                        movzx edi, ax
0084601D  66 3B C6                        cmp ax, si
00846020  7F 37                           jg 0x140846059
00846022  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
00846027  4D 8B E5                        mov r12, r13
0084602A  4C 2B E1                        sub r12, rcx
0084602D  4C 8D 7C 24 70                  lea r15, [rsp + 0x70]
00846032  49 83 C4 F0                     add r12, -0x10
00846036  66 83 FF 02                     cmp di, 2
0084603A  0F 8D D8 02 00 00               jge 0x140846318
00846040  49 8B CF                        mov rcx, r15
00846043  48 8B 09                        mov rcx, qword ptr [rcx]
00846046  E8 75 32 38 00                  call 0x140bc92c0
0084604B  66 FF C7                        inc di
0084604E  49 83 C7 08                     add r15, 8
00846052  66 3B FE                        cmp di, si
00846055  7E DF                           jle 0x140846036
00846057  33 C0                           xor eax, eax
00846059  0F BF FE                        movsx edi, si
0084605C  44 0F B7 F8                     movzx r15d, ax
00846060  83 EF 01                        sub edi, 1
00846063  0F 89 B7 04 00 00               jns 0x140846520
00846069  48 0F BF C6                     movsx rax, si
0084606D  66 83 FE 02                     cmp si, 2
00846071  0F 8D A2 03 00 00               jge 0x140846419
00846077  48 8B 4C C4 70                  mov rcx, qword ptr [rsp + rax*8 + 0x70]
0084607C  E8 2F BE 01 00                  call 0x140861eb0
00846081  4C 8B 64 24 58                  mov r12, qword ptr [rsp + 0x58]
00846086  44 0F B6 7C 24 43               movzx r15d, byte ptr [rsp + 0x43]
0084608C  E9 B0 F9 FF FF                  jmp 0x140845a41
00846091  49 8D 0C 3F                     lea rcx, [r15 + rdi]
00846095  E9 56 FA FF FF                  jmp 0x140845af0
0084609A  4B 8D 0C 37                     lea rcx, [r15 + r14]
0084609E  E9 6F F9 FF FF                  jmp 0x140845a12
008460A3  4C 8B 64 24 58                  mov r12, qword ptr [rsp + 0x58]
008460A8  E9 15 FC FF FF                  jmp 0x140845cc2
008460AD  41 8B 95 1C 01 00 00            mov edx, dword ptr [r13 + 0x11c]
008460B4  83 FA FF                        cmp edx, -1
008460B7  0F 85 06 07 00 00               jne 0x1408467c3
008460BD  33 C0                           xor eax, eax
008460BF  41 C7 85 1C 01 00 00 FF FF FF FF  mov dword ptr [r13 + 0x11c], 0xffffffff
008460CA  41 89 85 18 01 00 00            mov dword ptr [r13 + 0x118], eax
008460D1  49 89 85 20 01 00 00            mov qword ptr [r13 + 0x120], rax
008460D8  E9 63 FE FF FF                  jmp 0x140845f40
008460DD  E8 CE EA FF FF                  call 0x140844bb0
008460E2  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
008460E6  48 8B F8                        mov rdi, rax
008460E9  48 85 C0                        test rax, rax
008460EC  0F 84 71 06 00 00               je 0x140846763
008460F2  49 8B D4                        mov rdx, r12
008460F5  48 8B C8                        mov rcx, rax
008460F8  E8 97 8F C4 FF                  call 0x14048f094
008460FD  49 8B D6                        mov rdx, r14
00846100  48 8B CF                        mov rcx, rdi
00846103  E8 28 52 C4 FF                  call 0x14048b330
00846108  8B F8                           mov edi, eax
0084610A  85 C0                           test eax, eax
0084610C  0F 88 C6 F8 FF FF               js 0x1408459d8
00846112  48 8B 7D C8                     mov rdi, qword ptr [rbp - 0x38]
00846116  49 8D 8C 24 F8 00 00 00         lea rcx, [r12 + 0xf8]
0084611E  48 8B D7                        mov rdx, rdi
00846121  E8 E2 EA FF FF                  call 0x140844c08
00846126  84 C0                           test al, al
00846128  0F 84 A5 F8 FF FF               je 0x1408459d3
0084612E  49 8D 8C 24 08 01 00 00         lea rcx, [r12 + 0x108]
00846136  41 B8 01 00 00 00               mov r8d, 1
0084613C  48 8B D7                        mov rdx, rdi
0084613F  E8 70 EB FF FF                  call 0x140844cb4
00846144  84 C0                           test al, al
00846146  0F 84 87 F8 FF FF               je 0x1408459d3
0084614C  49 8B 4C 24 20                  mov rcx, qword ptr [r12 + 0x20]
00846151  E8 06 98 00 00                  call 0x14084f95c
00846156  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
0084615B  4C 8D 44 24 50                  lea r8, [rsp + 0x50]
00846160  49 8B D6                        mov rdx, r14
00846163  41 B4 01                        mov r12b, 1
00846166  E8 C5 EB FF FF                  call 0x140844d30
0084616B  8B F8                           mov edi, eax
0084616D  85 C0                           test eax, eax
0084616F  78 15                           js 0x140846186
00846171  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
00846176  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
0084617A  E8 B9 25 00 00                  call 0x140848738
0084617F  E9 F7 F9 FF FF                  jmp 0x140845b7b
00846184  33 FF                           xor edi, edi
00846186  48 8B 74 24 48                  mov rsi, qword ptr [rsp + 0x48]
0084618B  E9 7B FD FF FF                  jmp 0x140845f0b
00846190  4B 8D 0C 37                     lea rcx, [r15 + r14]
00846194  E9 D4 FA FF FF                  jmp 0x140845c6d
00846199  E8 12 EB 00 00                  call 0x140854cb0
0084619E  E9 81 FB FF FF                  jmp 0x140845d24
008461A3  41 83 FC FF                     cmp r12d, -1
008461A7  0F 85 7E 01 00 00               jne 0x14084632b
008461AD  48 8B 45 F0                     mov rax, qword ptr [rbp - 0x10]
008461B1  49 8B D7                        mov rdx, r15
008461B4  44 8B A5 30 01 00 00            mov r12d, dword ptr [rbp + 0x130]
008461BB  44 8B 4D A8                     mov r9d, dword ptr [rbp - 0x58]
008461BF  4C 8B 45 B0                     mov r8, qword ptr [rbp - 0x50]
008461C3  44 89 6C 24 38                  mov dword ptr [rsp + 0x38], r13d
008461C8  44 89 64 24 30                  mov dword ptr [rsp + 0x30], r12d
008461CD  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008461D2  8B 45 8C                        mov eax, dword ptr [rbp - 0x74]
008461D5  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
008461D9  E8 66 59 01 00                  call 0x14085bb44
008461DE  8B F8                           mov edi, eax
008461E0  85 C0                           test eax, eax
008461E2  0F 88 1B 04 00 00               js 0x140846603
008461E8  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
008461ED  48 8B 4D B0                     mov rcx, qword ptr [rbp - 0x50]
008461F1  0F B7 01                        movzx eax, word ptr [rcx]
008461F4  41 39 47 3C                     cmp dword ptr [r15 + 0x3c], eax
008461F8  73 0F                           jae 0x140846209
008461FA  41 89 47 3C                     mov dword ptr [r15 + 0x3c], eax
008461FE  0F B7 01                        movzx eax, word ptr [rcx]
00846201  66 41 89 86 B2 00 00 00         mov word ptr [r14 + 0xb2], ax
00846209  45 39 67 40                     cmp dword ptr [r15 + 0x40], r12d
0084620D  73 0B                           jae 0x14084621a
0084620F  45 89 67 40                     mov dword ptr [r15 + 0x40], r12d
00846213  45 89 A6 B4 00 00 00            mov dword ptr [r14 + 0xb4], r12d
0084621A  49 89 5F 04                     mov qword ptr [r15 + 4], rbx
0084621E  41 F7 86 B8 00 00 00 00 00 40 00  test dword ptr [r14 + 0xb8], 0x400000
00846229  49 89 9E A8 00 00 00            mov qword ptr [r14 + 0xa8], rbx
00846230  0F 84 38 02 00 00               je 0x14084646e
00846236  41 8B 4F 28                     mov ecx, dword ptr [r15 + 0x28]
0084623A  41 8B 47 24                     mov eax, dword ptr [r15 + 0x24]
0084623E  41 89 4E 64                     mov dword ptr [r14 + 0x64], ecx
00846242  49 8B 4E 20                     mov rcx, qword ptr [r14 + 0x20]
00846246  41 89 46 60                     mov dword ptr [r14 + 0x60], eax
0084624A  E8 E9 24 00 00                  call 0x140848738
0084624F  45 32 E4                        xor r12b, r12b
00846252  E9 11 FC FF FF                  jmp 0x140845e68
00846257  49 8D 57 24                     lea rdx, [r15 + 0x24]
0084625B  E8 20 09 00 00                  call 0x140846b80
00846260  B9 00 00 00 80                  mov ecx, 0x80000000
00846265  8B F8                           mov edi, eax
00846267  03 C1                           add eax, ecx
00846269  85 C1                           test ecx, eax
0084626B  0F 85 09 FB FF FF               jne 0x140845d7a
00846271  81 FF 34 00 00 C0               cmp edi, 0xc0000034
00846277  0F 84 FD FA FF FF               je 0x140845d7a
0084627D  48 8B 74 24 48                  mov rsi, qword ptr [rsp + 0x48]
00846282  E9 60 FC FF FF                  jmp 0x140845ee7
00846287  33 C0                           xor eax, eax
00846289  0F B7 F8                        movzx edi, ax
0084628C  66 3B C6                        cmp ax, si
0084628F  7F 3B                           jg 0x1408462cc
00846291  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
00846296  4D 8B E5                        mov r12, r13
00846299  4C 2B E1                        sub r12, rcx
0084629C  4C 8D 7C 24 70                  lea r15, [rsp + 0x70]
008462A1  49 83 C4 F0                     add r12, -0x10
008462A5  66 83 FF 02                     cmp di, 2
008462A9  0F 8D 60 02 00 00               jge 0x14084650f
008462AF  49 8B CF                        mov rcx, r15
008462B2  48 8B 09                        mov rcx, qword ptr [rcx]
008462B5  E8 06 30 38 00                  call 0x140bc92c0
008462BA  66 FF C7                        inc di
008462BD  49 83 C7 08                     add r15, 8
008462C1  66 3B FE                        cmp di, si
008462C4  7E DF                           jle 0x1408462a5
008462C6  44 0F B6 64 24 42               movzx r12d, byte ptr [rsp + 0x42]
008462CC  32 C0                           xor al, al
008462CE  48 8D 4C 24 68                  lea rcx, [rsp + 0x68]
008462D3  41 B0 01                        mov r8b, 1
008462D6  88 44 24 40                     mov byte ptr [rsp + 0x40], al
008462DA  33 D2                           xor edx, edx
008462DC  E8 A7 E0 FF FF                  call 0x140844388
008462E1  8B F8                           mov edi, eax
008462E3  85 C0                           test eax, eax
008462E5  0F 88 9B FE FF FF               js 0x140846186
008462EB  4C 8B 64 24 58                  mov r12, qword ptr [rsp + 0x58]
008462F0  41 B7 01                        mov r15b, 1
008462F3  44 88 7C 24 43                  mov byte ptr [rsp + 0x43], r15b
008462F8  C6 44 24 40 01                  mov byte ptr [rsp + 0x40], 1
008462FD  E9 3F F7 FF FF                  jmp 0x140845a41
00846302  81 FF 34 00 00 C0               cmp edi, 0xc0000034
00846308  0F 84 6C FA FF FF               je 0x140845d7a
0084630E  48 8B 74 24 48                  mov rsi, qword ptr [rsp + 0x48]
00846313  E9 CF FB FF FF                  jmp 0x140845ee7
00846318  4B 8D 0C 3C                     lea rcx, [r12 + r15]
0084631C  E9 22 FD FF FF                  jmp 0x140846043
00846321  49 8B 4C CD F0                  mov rcx, qword ptr [r13 + rcx*8 - 0x10]
00846326  E9 73 F8 FF FF                  jmp 0x140845b9e
0084632B  F6 81 8C 00 00 00 01            test byte ptr [rcx + 0x8c], 1
00846332  4C 8D 45 98                     lea r8, [rbp - 0x68]
00846336  41 8B D4                        mov edx, r12d
00846339  0F 84 D0 00 00 00               je 0x14084640f
0084633F  E8 1C E9 00 00                  call 0x140854c60
00846344  8B 8D 30 01 00 00               mov ecx, dword ptr [rbp + 0x130]
0084634A  4C 8B C0                        mov r8, rax
0084634D  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
00846352  41 8B D4                        mov edx, r12d
00846355  44 8B 4D 8C                     mov r9d, dword ptr [rbp - 0x74]
00846359  44 89 6C 24 30                  mov dword ptr [rsp + 0x30], r13d
0084635E  89 4C 24 28                     mov dword ptr [rsp + 0x28], ecx
00846362  48 8B 4D F0                     mov rcx, qword ptr [rbp - 0x10]
00846366  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0084636B  49 8B 4E 20                     mov rcx, qword ptr [r14 + 0x20]
0084636F  E8 C8 51 00 00                  call 0x14084b53c
00846374  49 8B 4E 20                     mov rcx, qword ptr [r14 + 0x20]
00846378  48 8D 55 98                     lea rdx, [rbp - 0x68]
0084637C  8B F8                           mov edi, eax
0084637E  F6 81 8C 00 00 00 01            test byte ptr [rcx + 0x8c], 1
00846385  0F 85 20 02 00 00               jne 0x1408465ab
0084638B  E8 B0 FB 00 00                  call 0x140855f40
00846390  85 FF                           test edi, edi
00846392  0F 88 AF 03 00 00               js 0x140846747
00846398  44 8B A5 30 01 00 00            mov r12d, dword ptr [rbp + 0x130]
0084639F  E9 49 FE FF FF                  jmp 0x1408461ed
008463A4  66 FF C8                        dec ax
008463A7  E9 DA F7 FF FF                  jmp 0x140845b86
008463AC  49 8B 4C F5 F0                  mov rcx, qword ptr [r13 + rsi*8 - 0x10]
008463B1  E8 FA BA 01 00                  call 0x140861eb0
008463B6  E9 82 F6 FF FF                  jmp 0x140845a3d
008463BB  49 8B 84 24 C0 00 00 00         mov rax, qword ptr [r12 + 0xc0]
008463C3  48 85 C0                        test rax, rax
008463C6  0F 84 AA F5 FF FF               je 0x140845976
008463CC  0F 1F 40 00                     nop dword ptr [rax]
008463D0  48 8B 48 10                     mov rcx, qword ptr [rax + 0x10]
008463D4  48 0F BF D6                     movsx rdx, si
008463D8  66 83 FE 02                     cmp si, 2
008463DC  0F 8D 45 02 00 00               jge 0x140846627
008463E2  48 89 4C D4 70                  mov qword ptr [rsp + rdx*8 + 0x70], rcx
008463E7  4C 8B 6D 80                     mov r13, qword ptr [rbp - 0x80]
008463EB  48 8B 40 18                     mov rax, qword ptr [rax + 0x18]
008463EF  66 FF CE                        dec si
008463F2  48 85 C0                        test rax, rax
008463F5  75 D9                           jne 0x1408463d0
008463F7  E9 70 F5 FF FF                  jmp 0x14084596c
008463FC  8B 5D A8                        mov ebx, dword ptr [rbp - 0x58]
008463FF  4C 8B C8                        mov r9, rax
00846402  44 8B C3                        mov r8d, ebx
00846405  E8 62 C2 C5 FF                  call 0x1404a266c
0084640A  E9 0F FA FF FF                  jmp 0x140845e1e
0084640F  E8 9C E8 00 00                  call 0x140854cb0
00846414  E9 2B FF FF FF                  jmp 0x140846344
00846419  49 8B 4C C5 F0                  mov rcx, qword ptr [r13 + rax*8 - 0x10]
0084641E  E8 8D BA 01 00                  call 0x140861eb0
00846423  4C 8B 64 24 58                  mov r12, qword ptr [rsp + 0x58]
00846428  44 0F B6 7C 24 43               movzx r15d, byte ptr [rsp + 0x43]
0084642E  E9 0E F6 FF FF                  jmp 0x140845a41
00846433  8B D0                           mov edx, eax
00846435  B9 00 01 00 00                  mov ecx, 0x100
0084643A  48 C1 E2 03                     shl rdx, 3
0084643E  41 B8 43 4D 36 35               mov r8d, 0x35364d43
00846444  E8 BB 70 B8 FF                  call 0x1403cd504
00846449  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0084644E  4C 8B E8                        mov r13, rax
00846451  48 85 C0                        test rax, rax
00846454  0F 85 EC F4 FF FF               jne 0x140845946
0084645A  48 8B 75 80                     mov rsi, qword ptr [rbp - 0x80]
0084645E  45 32 FF                        xor r15b, r15b
00846461  45 32 E4                        xor r12b, r12b
00846464  BF 9A 00 00 C0                  mov edi, 0xc000009a
00846469  E9 A3 FA FF FF                  jmp 0x140845f11
0084646E  41 8B 46 08                     mov eax, dword ptr [r14 + 8]
00846472  A8 08                           test al, 8
00846474  0F 84 BC FD FF FF               je 0x140846236
0084647A  49 8B 4E 68                     mov rcx, qword ptr [r14 + 0x68]
0084647E  48 8D 55 28                     lea rdx, [rbp + 0x28]
00846482  E8 C9 95 00 00                  call 0x14084fa50
00846487  B8 F7 FF 00 00                  mov eax, 0xfff7
0084648C  49 C7 46 68 00 00 00 00         mov qword ptr [r14 + 0x68], 0
00846494  66 41 21 46 08                  and word ptr [r14 + 8], ax
00846499  E9 98 FD FF FF                  jmp 0x140846236
0084649E  44 89 61 58                     mov dword ptr [rcx + 0x58], r12d
008464A2  B8 05 00 00 00                  mov eax, 5
008464A7  E9 93 F9 FF FF                  jmp 0x140845e3f
008464AC  E8 6F 67 01 00                  call 0x14085cc20
008464B1  E9 55 FA FF FF                  jmp 0x140845f0b
008464B6  66 66 0F 1F 84 00 00 00 00 00   nop word ptr [rax + rax]
008464C0  49 0F BF C6                     movsx rax, r14w
008464C4  66 41 83 FE 02                  cmp r14w, 2
008464C9  0F 8D 44 01 00 00               jge 0x140846613
008464CF  48 8B 4C C4 70                  mov rcx, qword ptr [rsp + rax*8 + 0x70]
008464D4  E8 43 35 38 00                  call 0x140bc9a1c
008464D9  66 41 FF C6                     inc r14w
008464DD  41 0F BF C6                     movsx eax, r14w
008464E1  3B C7                           cmp eax, edi
008464E3  0F 8F AF F7 FF FF               jg 0x140845c98
008464E9  EB D5                           jmp 0x1408464c0
008464EB  48 8B 75 80                     mov rsi, qword ptr [rbp - 0x80]
008464EF  45 32 FF                        xor r15b, r15b
008464F2  45 32 E4                        xor r12b, r12b
008464F5  BF 22 00 00 C0                  mov edi, 0xc0000022
008464FA  E9 12 FA FF FF                  jmp 0x140845f11
008464FF  48 8B 75 80                     mov rsi, qword ptr [rbp - 0x80]
00846503  45 32 E4                        xor r12b, r12b
00846506  45 0F B6 F4                     movzx r14d, r12b
0084650A  E9 08 FA FF FF                  jmp 0x140845f17
0084650F  4B 8D 0C 27                     lea rcx, [r15 + r12]
00846513  E9 9A FD FF FF                  jmp 0x1408462b2
00846518  0F 1F 84 00 00 00 00 00         nop dword ptr [rax + rax]
00846520  49 0F BF C7                     movsx rax, r15w
00846524  66 41 83 FF 02                  cmp r15w, 2
00846529  0F 8D EE 00 00 00               jge 0x14084661d
0084652F  48 8B 4C C4 70                  mov rcx, qword ptr [rsp + rax*8 + 0x70]
00846534  E8 E3 34 38 00                  call 0x140bc9a1c
00846539  66 41 FF C7                     inc r15w
0084653D  41 0F BF C7                     movsx eax, r15w
00846541  3B C7                           cmp eax, edi
00846543  0F 8F 20 FB FF FF               jg 0x140846069
00846549  EB D5                           jmp 0x140846520
0084654B  48 8B 5C C6 F0                  mov rbx, qword ptr [rsi + rax*8 - 0x10]
00846550  E9 42 F9 FF FF                  jmp 0x140845e97
00846555  83 7D 8C 06                     cmp dword ptr [rbp - 0x74], 6
00846559  75 46                           jne 0x1408465a1
0084655B  8B 85 30 01 00 00               mov eax, dword ptr [rbp + 0x130]
00846561  A8 01                           test al, 1
00846563  75 3C                           jne 0x1408465a1
00846565  3D FF FF 00 00                  cmp eax, 0xffff
0084656A  77 35                           ja 0x1408465a1
0084656C  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
00846570  48 85 C0                        test rax, rax
00846573  74 2C                           je 0x1408465a1
00846575  41 B0 01                        mov r8b, 1
00846578  48 8D 0D 81 36 79 00            lea rcx, [rip + 0x793681]
0084657F  48 8B D0                        mov rdx, rax
00846582  E8 99 C4 0E 00                  call 0x140932a20
00846587  84 C0                           test al, al
00846589  74 16                           je 0x1408465a1
0084658B  0F B6 54 24 60                  movzx edx, byte ptr [rsp + 0x60]
00846590  48 8D 4D 68                     lea rcx, [rbp + 0x68]
00846594  E8 17 D5 06 00                  call 0x1408b3ab0
00846599  84 C0                           test al, al
0084659B  0F 84 18 F6 FF FF               je 0x140845bb9
008465A1  BF 22 00 00 C0                  mov edi, 0xc0000022
008465A6  E9 DB FB FF FF                  jmp 0x140846186
008465AB  E8 70 66 01 00                  call 0x14085cc20
008465B0  E9 DB FD FF FF                  jmp 0x140846390
008465B5  45 32 F6                        xor r14b, r14b
008465B8  BF 89 01 00 C0                  mov edi, 0xc0000189
008465BD  45 32 FF                        xor r15b, r15b
008465C0  48 8B 75 80                     mov rsi, qword ptr [rbp - 0x80]
008465C4  45 32 E4                        xor r12b, r12b
008465C7  E9 4B F9 FF FF                  jmp 0x140845f17
008465CC  45 33 C0                        xor r8d, r8d
008465CF  48 8D 4C 24 68                  lea rcx, [rsp + 0x68]
008465D4  49 8B D6                        mov rdx, r14
008465D7  E8 A4 0F 08 00                  call 0x1408c7580
008465DC  B9 00 01 00 00                  mov ecx, 0x100
008465E1  41 B8 43 4D 41 33               mov r8d, 0x33414d43
008465E7  48 8B F8                        mov rdi, rax
008465EA  8B 50 18                        mov edx, dword ptr [rax + 0x18]
008465ED  E8 12 6F B8 FF                  call 0x1403cd504
008465F2  4C 8B E8                        mov r13, rax
008465F5  48 85 C0                        test rax, rax
008465F8  0F 85 83 00 00 00               jne 0x140846681
008465FE  BF 9A 00 00 C0                  mov edi, 0xc000009a
00846603  44 0F B6 64 24 42               movzx r12d, byte ptr [rsp + 0x42]
00846609  48 8B 74 24 48                  mov rsi, qword ptr [rsp + 0x48]
0084660E  E9 D4 F8 FF FF                  jmp 0x140845ee7
00846613  49 8B 4C C5 F0                  mov rcx, qword ptr [r13 + rax*8 - 0x10]
00846618  E9 B7 FE FF FF                  jmp 0x1408464d4
0084661D  49 8B 4C C5 F0                  mov rcx, qword ptr [r13 + rax*8 - 0x10]
00846622  E9 0D FF FF FF                  jmp 0x140846534
00846627  49 89 4C D5 F0                  mov qword ptr [r13 + rdx*8 - 0x10], rcx
0084662C  E9 BA FD FF FF                  jmp 0x1408463eb
00846631  4C 8D 45 E8                     lea r8, [rbp - 0x18]
00846635  48 8D 55 A0                     lea rdx, [rbp - 0x60]
00846639  E8 CA 01 00 00                  call 0x140846808
0084663E  8B F8                           mov edi, eax
00846640  85 C0                           test eax, eax
00846642  0F 88 90 F3 FF FF               js 0x1408459d8
00846648  8B 5D A0                        mov ebx, dword ptr [rbp - 0x60]
0084664B  33 D2                           xor edx, edx
0084664D  49 8B CC                        mov rcx, r12
00846650  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
00846654  44 8D 42 01                     lea r8d, [rdx + 1]
00846658  E8 13 87 16 00                  call 0x1409aed70
0084665D  48 8D 4C 24 68                  lea rcx, [rsp + 0x68]
00846662  E8 F9 1D 00 00                  call 0x140848460
00846667  45 32 FF                        xor r15b, r15b
0084666A  4D 85 ED                        test r13, r13
0084666D  0F 84 81 FA 2C 00               je 0x140b160f4
00846673  49 8B CD                        mov rcx, r13
00846676  E8 05 F7 C2 FF                  call 0x140475d80
0084667B  90                              nop
0084667C  E9 73 FA 2C 00                  jmp 0x140b160f4
00846681  44 8B 47 18                     mov r8d, dword ptr [rdi + 0x18]
00846685  48 8D 57 20                     lea rdx, [rdi + 0x20]
00846689  49 8B CD                        mov rcx, r13
0084668C  E8 AF 01 E8 FF                  call 0x1406c6840
00846691  49 8B C5                        mov rax, r13
00846694  4C 8B 6C 24 58                  mov r13, qword ptr [rsp + 0x58]
00846699  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0084669D  41 83 FC FF                     cmp r12d, -1
008466A1  75 47                           jne 0x1408466ea
008466A3  C7 45 90 00 00 00 00            mov dword ptr [rbp - 0x70], 0
008466AA  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
008466AE  E9 DD F6 FF FF                  jmp 0x140845d90
008466B3  E8 C8 F6 C2 FF                  call 0x140475d80
008466B8  E9 0A F4 FF FF                  jmp 0x140845ac7
008466BD  4C 8B 7D E8                     mov r15, qword ptr [rbp - 0x18]
008466C1  4D 8B E6                        mov r12, r14
008466C4  E9 D0 FA 2C 00                  jmp 0x140b16199
008466C9  4C 8D 45 18                     lea r8, [rbp + 0x18]
008466CD  48 C7 45 18 80 69 67 FF         mov qword ptr [rbp + 0x18], 0xffffffffff676980
008466D5  33 D2                           xor edx, edx
008466D7  33 C9                           xor ecx, ecx
008466D9  E8 72 2E 9C FF                  call 0x140209550
008466DE  C7 45 A4 00 00 00 00            mov dword ptr [rbp - 0x5c], 0
008466E5  E9 67 F4 FF FF                  jmp 0x140845b51
008466EA  49 8B 4D 20                     mov rcx, qword ptr [r13 + 0x20]
008466EE  4C 8D 45 98                     lea r8, [rbp - 0x68]
008466F2  41 8B D4                        mov edx, r12d
008466F5  F6 81 8C 00 00 00 01            test byte ptr [rcx + 0x8c], 1
008466FC  0F 84 10 FB 2C 00               je 0x140b16212
00846702  E8 59 E5 00 00                  call 0x140854c60
00846707  90                              nop
00846708  E9 0A FB 2C 00                  jmp 0x140b16217
0084670D  4D 85 FF                        test r15, r15
00846710  0F 84 80 FB 2C 00               je 0x140b16296
00846716  49 8B 4E 20                     mov rcx, qword ptr [r14 + 0x20]
0084671A  48 8D 55 C0                     lea rdx, [rbp - 0x40]
0084671E  40 84 B1 8C 00 00 00            test byte ptr [rcx + 0x8c], sil
00846725  0F 84 63 FB 2C 00               je 0x140b1628e
0084672B  E8 F0 64 01 00                  call 0x14085cc20
00846730  90                              nop
00846731  E9 5D FB 2C 00                  jmp 0x140b16293
00846736  44 0F B6 E6                     movzx r12d, sil
0084673A  4D 8B EE                        mov r13, r14
0084673D  48 8B 74 24 48                  mov rsi, qword ptr [rsp + 0x48]
00846742  E9 A5 F7 FF FF                  jmp 0x140845eec
00846747  44 0F B6 64 24 42               movzx r12d, byte ptr [rsp + 0x42]
0084674D  4D 8B EE                        mov r13, r14
00846750  48 8B 74 24 48                  mov rsi, qword ptr [rsp + 0x48]
00846755  E9 92 F7 FF FF                  jmp 0x140845eec
0084675A  44 0F B6 E6                     movzx r12d, sil
0084675E  E9 1A FB FF FF                  jmp 0x14084627d
00846763  BF 9A 00 00 C0                  mov edi, 0xc000009a
00846768  E9 6B F2 FF FF                  jmp 0x1408459d8
0084676D  BF 22 00 00 C0                  mov edi, 0xc0000022
00846772  E9 61 F2 FF FF                  jmp 0x1408459d8
00846777  45 32 E4                        xor r12b, r12b
0084677A  F6 47 30 01                     test byte ptr [rdi + 0x30], 1
0084677E  EB 08                           jmp 0x140846788
00846780  45 32 E4                        xor r12b, r12b
00846783  41 F6 46 30 01                  test byte ptr [r14 + 0x30], 1
00846788  BF 25 04 00 C0                  mov edi, 0xc0000425
0084678D  B8 7C 01 00 C0                  mov eax, 0xc000017c
00846792  0F 44 F8                        cmove edi, eax
00846795  E9 EC F9 FF FF                  jmp 0x140846186
0084679A  49 8B 4D 20                     mov rcx, qword ptr [r13 + 0x20]
0084679E  E8 F5 47 00 00                  call 0x14084af98
008467A3  E9 80 F7 FF FF                  jmp 0x140845f28
008467A8  48 8B C8                        mov rcx, rax
008467AB  E8 CC E1 02 00                  call 0x14087497c
008467B0  48 8B 4D C8                     mov rcx, qword ptr [rbp - 0x38]
008467B4  BA 43 4D 55 77                  mov edx, 0x77554d43
008467B9  E8 B2 C0 33 00                  call 0x140b82870
008467BE  E9 72 F7 FF FF                  jmp 0x140845f35
008467C3  49 8B 4D 20                     mov rcx, qword ptr [r13 + 0x20]
008467C7  E8 60 3F 01 00                  call 0x14085a72c
008467CC  E9 EC F8 FF FF                  jmp 0x1408460bd
008467D1  49 8B 4D 20                     mov rcx, qword ptr [r13 + 0x20]
008467D5  E8 5E 1F 00 00                  call 0x140848738
008467DA  E9 6A F7 FF FF                  jmp 0x140845f49
008467DF  BA 43 4D 41 34                  mov edx, 0x34414d43
008467E4  E8 F7 21 C0 FF                  call 0x1404489e0
008467E9  E9 C9 F7 FF FF                  jmp 0x140845fb7
008467EE  BA 43 4D 41 33                  mov edx, 0x33414d43
008467F3  48 8B CB                        mov rcx, rbx
008467F6  E8 E5 21 C0 FF                  call 0x1404489e0
008467FB  E9 C0 F7 FF FF                  jmp 0x140845fc0
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmSetValueKey(__int64 a1, __int64 a2, int a3, __int64 a4, unsigned int a5, __int64 a6, unsigned __int8 a7)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned int v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m158;
    unsigned int v_stack_m160;
    unsigned int v_stack_m164;
    unsigned int v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned int v_stack_m178;
    unsigned int v_stack_m17C;
    unsigned int v_stack_m180;
    unsigned __int64 v_stack_m188;
    unsigned __int64 v_stack_m190;
    unsigned __int64 v_stack_m198;
    unsigned __int16 v_stack_m19E;
    unsigned __int64 v_stack_m1A0;
    unsigned __int8 v_stack_m1A8;
    unsigned __int64 v_stack_m1B0;
    unsigned __int8 v_stack_m1B8;
    unsigned __int64 v_stack_m1C0;
    unsigned __int8 v_stack_m1C5;
    unsigned __int8 v_stack_m1C6;
    unsigned __int8 v_stack_m1C7;
    unsigned __int8 v_stack_m1C8;
    unsigned __int64 v_stack_m1D8;
    unsigned __int64 v_stack_m1E0;
    unsigned int v_stack_m1E8;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned int v_stack_p30;
    unsigned int v_stack_p38;
    unsigned __int8 v_stack_p40;
    unsigned __int8 v_stack_p42;
    unsigned __int8 v_stack_p43;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int8 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int16 v_stack_p6A;
    unsigned __int64 v_stack_p70;

    v_rsp = (v_rsp) - (456);
    result = (*(unsigned __int64 *)(v_rip + 6049629)) ^ (v_rsp);
    v_stack_m50 = result;
    v_r15 = 0;
    v_stack_mE8 = a6;
    v_stack_m110 = a1;
    v_stack_m100 = v_stack_m108;
    v_stack_m118 = a4;
    v_stack_m108 = v_stack_m108;
    v_stack_m17C = a3;
    v_stack_m1A0 = v_xmm0;
    v_stack_m19E = (unsigned __int16)((unsigned int)(0xFFFFFFFFULL));
    v_stack_m158 = a2;
    v_stack_m168 = 0;
    v_stack_m120 = 0;
    v_stack_m148 = 0;
    v_stack_m160 = 0;
    v_stack_m170 = 0;
    v_stack_m80 = v_xmm0;
    v_stack_m140 = 0;
    v_stack_m70 = v_xmm0;
    v_stack_m1B8 = 0;
    v_stack_m60 = v_xmm0;
    v_stack_m164 = 0;
    v_stack_mE0 = v_xmm0;
    v_stack_m128 = 0;
    v_stack_m190 = v_xmm0;
    v_stack_m1B0 = 0;
    result = HvpGetCellContextInitialize(v_stack_m148, a2, a3, a4);
    result = HvpGetCellContextInitialize(v_stack_m170, a2, a3, a4);
    result = CmpInitializeDelayDerefContext(v_stack_mE0, a2, a3, a4);
    v_stack_mD0 = v_xmm0;
    v_stack_m130 = 0xFFFFFFFFULL;
    v_stack_mC0 = v_xmm0;
    v_stack_m180 = 0xFFFFFFFFULL;
    v_stack_m138 = 0;
    v_stack_m178 = 0;
    v_stack_m1A8 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    v_stack_mA0 = v_xmm0;
    v_stack_m90 = v_xmm0;
    result = SeCaptureSubjectContext(v_stack_mA0, a2, a3, a4);
    result = CmpAttachToRegistryProcess(v_stack_m80, a2, a3, a4);
loc_008458E2:
    result = CmpIsShutdownRundownActive(v_stack_m80, a2, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_008465B5;
    result = CmpLockRegistry(v_stack_m80, a2, a3, a4);
    v_stack_m1C7 = 1;
    v_stack_m1B0 = *(unsigned __int64 *)(a1 + 8);
    if (((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 160)) & (0x100000ULL)) != 0) goto loc_008464EB;
    v_stack_m1C0 = 0;
    if (((unsigned int)((__int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 66)))) < 2) goto loc_00845946;
    result = (unsigned int)(((unsigned int)((unsigned int)((__int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 66))))) - (1));
    if (condition_is_not_equal) goto loc_00846433;
loc_00845946:
    v_stack_m1A0 = (unsigned __int16)((__int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 66)));
    v_stack_m188 = 0;
    v_stack_m19E = (unsigned __int16)((__int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 66)));
    if ((unsigned __int16)((__int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 66))) != 0) goto loc_008463BB;
    *(unsigned __int64 *)(v_rsp + (__int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 66)) * 8 + 112) = *(unsigned __int64 *)(a1 + 8);
loc_0084596C:
    v_stack_m1C0 = v_stack_m188;
loc_00845976:
    if ((*(unsigned __int64 *)(a1 + 56)) == 0) goto loc_008459E0;
loc_0084597D:
    result = CmpLockKcbStackTopExclusiveRestShared(v_stack_m1A0, a2, a3, a4);
loc_0084598A:
    v_stack_m1C5 = 1;
    v_stack_m1C8 = 1;
    if ((*(unsigned __int64 *)(a1 + 56)) == 0) goto loc_00845A32;
loc_0084599F:
    a2 = 0;
    result = CmpIsKeyDeletedForKeyBody(a1, a2, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00846780;
    result = CmpTransSearchAddTransFromKeyBody(a1, v_stack_m128, a3, a4);
    if (sign_flag) goto loc_008459D8;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 160)))) & (2)) == 0) goto loc_00845A3D;
loc_008459D3:
loc_008459D8:
    v_r12 = 0;
    goto loc_00846186;
loc_008459E0:
    if ((*(unsigned __int64 *)(a1 + 64)) != 0) goto loc_0084597D;
    if (1 > ((unsigned __int16)(v_stack_m19E))) goto loc_00845A2A;
    v_r15 = (v_stack_m188) - (v_stack_m198);
    v_r15 = (v_r15) + (-16);
loc_00845A05:
    if (1 >= 2) goto loc_0084609A;
loc_00845A12:
    result = CmpLockKcbShared(*(unsigned __int64 *)(v_stack_m198), v_stack_m128, a3, a4);
    v_rdi = (unsigned __int16)((1) + 1);
    v_r14 = (v_stack_m198) + (8);
    if (((unsigned __int16)(v_rdi)) <= ((unsigned __int16)(v_stack_m19E))) goto loc_00845A05;
loc_00845A2A:
    v_r15 = 0;
    goto loc_0084598A;
loc_00845A32:
    if ((*(unsigned __int64 *)(v_stack_m110 + 64)) != 0) goto loc_0084599F;
loc_00845A3D:
loc_00845A41:
    result = CmpIsKeyDeletedForKeyBody(v_stack_m110, v_stack_m128, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00846777;
    if ((*(unsigned __int8 *)(v_r12 + 65)) == 1) goto loc_0084676D;
    if (v_stack_m128 != 0) goto loc_008460DD;
    if ((*(unsigned int *)(v_r12 + 248)) >= ((unsigned int)(v_stack_m128))) goto loc_00845B65;
    result = CmpSnapshotTxOwnerArray(v_r12 + 248, v_stack_m168, v_stack_m120, a4);
    if (sign_flag) goto loc_008459D8;
    v_rdi = 0;
    a2 = 0;
    v_stack_mB0 = v_xmm0;
    v_stack_mF8 = 0;
    result = RtlInitUnicodeString(v_stack_mB0, a2, v_stack_m120, a4);
    if (v_stack_mA8 != 0) goto loc_008466B3;
loc_00845AC7:
    if (0 > ((unsigned __int16)(v_stack_m19E))) goto loc_00845B06;
    v_r15 = (v_stack_m188) - (v_stack_m198);
    v_r15 = (v_r15) + (-16);
loc_00845AE3:
    if (0 >= 2) goto loc_00846091;
loc_00845AF0:
    result = CmpUnlockKcb(*(unsigned __int64 *)(v_stack_m198), a2, v_stack_m120, a4);
    v_rbx = (unsigned __int16)((0) + 1);
    v_rdi = (v_stack_m198) + (8);
    if (((unsigned __int16)(v_rbx)) <= ((unsigned __int16)(v_stack_m19E))) goto loc_00845AE3;
    v_rdi = 0;
loc_00845B06:
    v_r15 = 0;
    v_stack_m1C8 = 0;
    if (v_stack_m188 != 0) {
        a1 = v_stack_m188;
        result = CmSiFreeMemory(a1, a2, v_stack_m120, a4);
    }
    v_stack_m1A0 = v_xmm0;
    v_stack_m19E = (unsigned __int16)((unsigned int)(0xFFFFFFFFULL));
    v_stack_m190 = v_xmm0;
    result = CmpUnlockRegistry(a1, a2, v_stack_m120, a4);
    if ((unsigned int)((unsigned int)(v_stack_m168)) != 0) goto loc_008466BD;
    result = (unsigned int)(((unsigned int)(v_stack_m164)) + 1);
    v_stack_m164 = (unsigned int)(result);
    if (((unsigned int)(result)) > 10) goto loc_008466C9;
loc_00845B51:
    if (sign_flag) goto loc_008464FF;
    v_r15 = 0;
    goto loc_008458E2;
loc_00845B65:
    if ((*(unsigned int *)(v_r12 + 264)) != 0) goto loc_00846631;
loc_00845B7B:
    v_r12 = 0;
    v_stack_m1C6 = 0;
loc_00845B86:
    if (sign_flag) goto loc_00845BB9;
    if (((unsigned __int16)((unsigned __int16)(v_stack_m19E))) >= 2) goto loc_00846321;
loc_00845B9E:
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rsp + (__int16)((unsigned __int16)((unsigned __int16)(v_stack_m19E))) * 8 + 112) + 40)) == -1) goto loc_008463A4;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp + (__int16)((unsigned __int16)((unsigned __int16)(v_stack_m19E))) * 8 + 112) + 184))) >> (20));
    if ((((unsigned __int8)(result)) & (1)) != 0) goto loc_00846555;
loc_00845BB9:
    if ((*(unsigned int *)(v_stack_m1B0 + 40)) == -1) goto loc_00846287;
    if (0 != 0) goto loc_008460A3;
    v_stack_m1E8 = (unsigned int)((unsigned int)(a5));
    result = CmpCompareNewValueDataAgainstKCBCache(v_stack_m1B0, v_stack_m158, (unsigned int)(v_stack_m17C), v_stack_m118);
    if (((unsigned int)(result)) == 1) goto loc_00846018;
    if ((unsigned int)(result) == 0) goto loc_00846184;
    v_stack_m1C5 = 1;
    if ((*(unsigned __int64 *)(v_stack_m1B0 + 56)) == (*(unsigned __int64 *)(gs_base + (0 + 392)))) goto loc_00845CB0;
    if ((*(unsigned __int64 *)(v_stack_m1B0 + 56)) == (*(unsigned __int64 *)(gs_base + (0 + 392)))) goto loc_00845FF3;
    result = 0;
    v_stack_m1C0 = v_stack_m188;
    if (0 > ((unsigned __int16)((__int16)(v_stack_m19E)))) goto loc_00845C89;
    v_r15 = (v_stack_m188) - (v_stack_m198);
    v_r15 = (v_r15) + (-16);
loc_00845C60:
    if (0 >= 2) goto loc_00846190;
loc_00845C6D:
    result = CmpUnlockKcb(*(unsigned __int64 *)(v_stack_m198), v_stack_m158, (unsigned int)(v_stack_m17C), v_stack_m118);
    v_rdi = (unsigned __int16)((0) + 1);
    v_r14 = (v_stack_m198) + (8);
    if (((unsigned __int16)(v_rdi)) <= ((unsigned __int16)((__int16)(v_stack_m19E)))) goto loc_00845C60;
    result = 0;
loc_00845C89:
    v_rdi = (unsigned int)(((unsigned int)((unsigned int)((__int16)(v_stack_m19E)))) - (1));
    if (!sign_flag) goto loc_008464C0;
loc_00845C98:
    if (((unsigned int)((__int16)(v_stack_m19E))) >= 2) goto loc_008463AC;
    result = CmpLockKcbExclusive(*(unsigned __int64 *)(v_rsp + (__int16)(v_stack_m19E) * 8 + 112), v_stack_m158, (unsigned int)(v_stack_m17C), v_stack_m118);
    goto loc_00845A3D;
loc_00845CB0:
    v_stack_m1C0 = v_stack_m188;
loc_00845CC2:
    result = HvLockHiveFlusherShared(*(unsigned __int64 *)(v_stack_m1B0 + 32), v_stack_m158, (unsigned int)(v_stack_m17C), v_stack_m118);
    v_stack_m1C6 = 1;
    if (v_stack_m128 != 0) goto loc_00845D02;
    a4 = 0;
    a3 = 0;
    result = HvpMarkCellDirty(*(unsigned __int64 *)(v_stack_m1B0 + 32), (unsigned int)(*(unsigned int *)(v_stack_m1B0 + 40)), a3, a4);
    if (sign_flag) goto loc_00846186;
loc_00845D02:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m1B0 + 32) + 140)) & (1)) == 0) goto loc_00846199;
    result = HvpGetCellFlat(*(unsigned __int64 *)(v_stack_m1B0 + 32), (unsigned int)(*(unsigned int *)(v_stack_m1B0 + 40)), v_stack_m148, a4);
loc_00845D24:
    result = CmpUpdateKeyNodeAccessBits(*(unsigned __int64 *)(v_stack_m1B0 + 32), result, (unsigned int)(*(unsigned int *)(v_stack_m1B0 + 40)), a4);
    a4 = 0;
    v_stack_m1E0 = v_stack_m130;
    v_stack_m1E8 = v_stack_m160;
    if (v_stack_m128 == 0) goto loc_00846257;
    result = CmpFindNameInListWithStatus(*(unsigned __int64 *)(v_stack_m1B0 + 32), v_stack_m1B0 + 280, v_stack_m158, a4);
    result = (unsigned int)((result) + ((unsigned int)((unsigned int)(0x80000000ULL))));
    if ((((unsigned int)((unsigned int)(0x80000000ULL))) & ((unsigned int)(result))) == 0) goto loc_00846302;
loc_00845D7A:
    if (a7 != 0) goto loc_008465CC;
loc_00845D90:
    v_r13 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m1B0 + 40))) >> (31));
    if (v_stack_m128 == 0) goto loc_008461A3;
    v_stack_m1D8 = v_stack_m180;
    v_stack_m1E0 = 1;
    v_stack_m1E8 = (unsigned int)((unsigned int)(a5));
    result = CmpAddValueKeyNew(*(unsigned __int64 *)(v_stack_m1B0 + 32), v_stack_m158, (unsigned int)(v_stack_m17C), v_stack_m118);
    if (sign_flag) goto loc_0084675A;
    if (((unsigned int)((unsigned int)(v_stack_m130))) != -1) goto loc_008463FC;
    v_stack_m1E0 = 1;
    v_stack_m1E8 = v_stack_m1B0 + 280;
    result = CmpAddValueToListEx(*(unsigned __int64 *)(v_stack_m1B0 + 32), (unsigned int)(v_stack_m180), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m1B0 + 280)))), 1);
    if (sign_flag) goto loc_00846736;
loc_00845E1E:
    result = HvUnlockHiveFlusherShared(*(unsigned __int64 *)(v_stack_m1B0 + 32), (unsigned int)(v_stack_m180), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m1B0 + 280)))), 1);
    v_stack_m1C6 = 0;
    if (((unsigned int)((unsigned int)(v_stack_m130))) != -1) goto loc_0084649E;
loc_00845E3F:
    *(unsigned int *)(v_stack_m140 + 68) = 4;
    *(unsigned int *)(v_stack_m140 + 92) = (unsigned int)((unsigned int)(v_stack_m180));
    *(unsigned int *)(v_stack_m140 + 72) = (unsigned int)(v_r13);
    result = CmAddLogForAction(v_stack_m140, 1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m1B0 + 280)))), 1);
    if (sign_flag) goto loc_0084670D;
loc_00845E68:
    v_r14 = 0;
    v_stack_m180 = 0xFFFFFFFFULL;
    v_stack_m140 = 0;
    v_stack_m1B8 = 0;
    if (((unsigned __int16)(v_stack_m19E)) >= 2) goto loc_0084654B;
loc_00845E97:
    v_stack_m1E8 = v_stack_m108;
    result = CmpReportNotifyHelper(v_stack_m1A0, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp + (__int16)(v_stack_m19E) * 8 + 112) + 32), v_stack_m128, 4);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp + (__int16)(v_stack_m19E) * 8 + 112) + 32)) != (*(unsigned __int64 *)(v_rip + 7945166))) {
        result = v_stack_m108;
        a4 = 4;
        a3 = v_stack_m128;
        v_stack_m1E8 = result;
        a1 = v_stack_m1A0;
        result = CmpReportNotifyHelper(a1, *(unsigned __int64 *)(v_rip + 7945166), a3, a4);
    }
loc_00845EE7:
loc_00845EEC:
    if (result == 0) goto loc_00845F0B;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m1B0 + 32) + 140)) & (1)) != 0) goto loc_008464AC;
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(v_stack_m1B0 + 32), v_stack_m148, a3, a4);
loc_00845F0B:
loc_00845F11:
loc_00845F17:
    if (((unsigned int)((unsigned int)(v_stack_m180))) != -1) goto loc_0084679A;
loc_00845F28:
    if (v_stack_m140 != 0) goto loc_008467A8;
loc_00845F35:
    if (v_stack_m1B8 != 0) goto loc_008460AD;
loc_00845F40:
    if ((unsigned __int8)(v_stack_m1C6) != 0) goto loc_008467D1;
loc_00845F49:
    result = v_stack_m140;
    if ((unsigned __int8)(v_stack_m1C8) != 0) {
        a1 = v_stack_m1A0;
        result = CmpUnlockKcbStack(a1, (unsigned int)(v_stack_m180), a3, a4);
    }
    a2 = 0;
    result = CmpDrainDelayDerefContext(v_stack_mE0, a2, a3, a4);
    if ((unsigned __int8)(v_stack_m1C7) != 0) {
        result = CmpUnlockRegistry(v_stack_mE0, a2, a3, a4);
    }
    result = v_stack_m108;
    if (v_stack_m108 != v_stack_m108) {
        a1 = v_stack_m108;
        result = CmpSignalDeferredPosts(a1, a2, a3, a4);
    }
    result = CmpDetachFromRegistryProcess(v_stack_m80, a2, a3, a4);
    result = SeReleaseSubjectContext(v_stack_mA0, a2, a3, a4);
    if (sign_flag) goto loc_00845FAA;
loc_00845FAA:
    if (v_stack_mC8 != 0) goto loc_008467DF;
loc_00845FB7:
    if (v_stack_m138 != 0) goto loc_008467EE;
loc_00845FC0:
    if (v_stack_m188 != 0) {
        a1 = v_stack_m188;
        result = CmSiFreeMemory(a1, a2, a3, a4);
    }
    a1 = (v_stack_m50) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (456);
    return result;
loc_00845FF3:
    v_stack_p48 = v_stack_m188;
    *(unsigned __int64 *)(v_stack_m1C6 + 56) = *(unsigned __int64 *)(gs_base + (0 + 392));
    goto loc_00845CC2;
loc_00846018:
    result = 0;
    if (0 > ((unsigned __int16)(v_stack_p6A))) goto loc_00846059;
    v_r12 = (v_stack_m1B0) - (v_stack_p70);
    v_r12 = (v_r12) + (-16);
loc_00846036:
    if (0 >= 2) goto loc_00846318;
loc_00846043:
    result = CmpUnlockKcb(*(unsigned __int64 *)(v_stack_p70), a2, a3, a4);
    v_rdi = (unsigned __int16)((0) + 1);
    v_r15 = (v_stack_p70) + (8);
    if (((unsigned __int16)(v_rdi)) <= ((unsigned __int16)(v_stack_p6A))) goto loc_00846036;
    result = 0;
loc_00846059:
    v_rdi = (unsigned int)(((__int16)((unsigned __int16)(v_stack_p6A))) - (1));
    if (!sign_flag) goto loc_00846520;
loc_00846069:
    if (((unsigned __int16)(v_stack_p6A)) >= 2) goto loc_00846419;
    result = CmpLockKcbExclusive(*(unsigned __int64 *)(v_rsp + (__int16)((unsigned __int16)(v_stack_p6A)) * 8 + 112), a2, a3, a4);
    goto loc_00845A41;
loc_00846091:
    goto loc_00845AF0;
loc_0084609A:
    goto loc_00845A12;
loc_008460A3:
    goto loc_00845CC2;
loc_008460AD:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m1B0 + 284)))) != -1) goto loc_008467C3;
loc_008460BD:
    result = 0;
    *(unsigned int *)(v_stack_m1B0 + 284) = 0xFFFFFFFFULL;
    *(unsigned int *)(v_stack_m1B0 + 280) = 0;
    *(unsigned __int64 *)(v_stack_m1B0 + 288) = 0;
    goto loc_00845F40;
loc_008460DD:
    result = CmpAllocateUnitOfWork(v_stack_p43 + v_stack_m128 * 1, (unsigned int)(*(unsigned int *)(v_stack_m1B0 + 284)), a3, a4);
    v_stack_m140 = result;
    if (result == 0) goto loc_00846763;
    result = CmpTransEnlistUowInKcb(result, v_stack_p58, a3, a4);
    result = CmpTransEnlistUowInCmTrans(result, v_stack_m128, a3, a4);
    if (sign_flag) goto loc_008459D8;
    result = CmpLockIXLockIntent(v_stack_p58 + 248, v_stack_m140, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_008459D3;
    result = CmpLockIXLockExclusive(v_stack_p58 + 264, v_stack_m140, 1, a4);
    if ((unsigned __int8)(result) == 0) goto loc_008459D3;
    result = HvLockHiveFlusherShared(*(unsigned __int64 *)(v_stack_p58 + 32), v_stack_m140, 1, a4);
    result = CmpCloneKCBValueListForTrans(v_stack_p58, v_stack_m128, v_stack_p50, a4);
    if (sign_flag) goto loc_00846186;
    result = HvUnlockHiveFlusherShared(*(unsigned __int64 *)(v_stack_p58 + 32), v_stack_m128, v_stack_p50, a4);
    goto loc_00845B7B;
loc_00846184:
    v_rdi = 0;
loc_00846186:
    goto loc_00845F0B;
loc_00846190:
    goto loc_00845C6D;
loc_00846199:
    result = HvpGetCellPaged(v_stack_p43 + v_stack_m128 * 1, v_stack_m128, v_stack_p50, a4);
    goto loc_00845D24;
loc_008461A3:
    if (1 != -1) goto loc_0084632B;
    v_stack_p38 = (unsigned int)(v_stack_m1B0);
    v_stack_p30 = (unsigned int)((unsigned int)(a5));
    v_stack_p28 = v_stack_m118;
    v_stack_p20 = (unsigned int)((unsigned int)(v_stack_m17C));
    result = CmpSetValueKeyNew(v_stack_p43 + v_stack_m128 * 1, v_stack_p43, v_stack_m158, (unsigned int)(v_stack_m160));
    if (sign_flag) goto loc_00846603;
loc_008461ED:
    result = *(unsigned __int16 *)(v_stack_m158);
    if ((*(unsigned int *)(v_stack_p43 + 60)) < ((unsigned int)(*(unsigned __int16 *)(v_stack_m158)))) {
        *(unsigned int *)(v_stack_p43 + 60) = (unsigned int)(*(unsigned __int16 *)(v_stack_m158));
        result = *(unsigned __int16 *)(v_stack_m158);
        *(unsigned __int16 *)(v_stack_p58 + 178) = (unsigned __int16)(result);
    }
    if ((*(unsigned int *)(v_stack_p43 + 64)) < ((unsigned int)((unsigned int)(a5)))) {
        *(unsigned int *)(v_stack_p43 + 64) = (unsigned int)((unsigned int)(a5));
        *(unsigned int *)(v_stack_p58 + 180) = (unsigned int)((unsigned int)(a5));
    }
    *(unsigned __int64 *)(v_stack_p43 + 4) = v_stack_m138;
    *(unsigned __int64 *)(v_stack_p58 + 168) = v_stack_m138;
    if (((*(unsigned int *)(v_stack_p58 + 184)) & (0x400000ULL)) == 0) goto loc_0084646E;
loc_00846236:
    *(unsigned int *)(v_stack_p58 + 100) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p43 + 40)));
    *(unsigned int *)(v_stack_p58 + 96) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p43 + 36)));
    result = HvUnlockHiveFlusherShared(*(unsigned __int64 *)(v_stack_p58 + 32), v_stack_p43, v_stack_m158, (unsigned int)(v_stack_m160));
    v_r12 = 0;
    goto loc_00845E68;
loc_00846257:
    result = CmpFindNameInListWithStatus(*(unsigned __int64 *)(v_stack_p58 + 32), v_stack_p43 + 36, v_stack_m158, (unsigned int)(v_stack_m160));
    result = (unsigned int)((result) + ((unsigned int)((unsigned int)(0x80000000ULL))));
    if ((((unsigned int)((unsigned int)(0x80000000ULL))) & ((unsigned int)(result))) != 0) goto loc_00845D7A;
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == 0xC0000034ULL) goto loc_00845D7A;
loc_0084627D:
    goto loc_00845EE7;
loc_00846287:
    result = 0;
    if (0 > ((unsigned __int16)(v_stack_p48))) goto loc_008462CC;
    v_r12 = (v_stack_m1B0) - (v_stack_p70);
    v_r12 = (v_r12) + (-16);
loc_008462A5:
    if (0 >= 2) goto loc_0084650F;
loc_008462B2:
    result = CmpUnlockKcb(*(unsigned __int64 *)(v_stack_p70), v_stack_p43 + 36, v_stack_m158, (unsigned int)(v_stack_m160));
    v_rdi = (unsigned __int16)((0) + 1);
    v_r15 = (v_stack_p70) + (8);
    if (((unsigned __int16)(v_rdi)) <= ((unsigned __int16)(v_stack_p48))) goto loc_008462A5;
loc_008462CC:
    result = 0;
    v_stack_p40 = 0;
    a2 = 0;
    result = CmpPromoteKey(v_stack_p68, a2, 1, (unsigned int)(v_stack_m160));
    if (sign_flag) goto loc_00846186;
    v_stack_p43 = 1;
    v_stack_p40 = 1;
    goto loc_00845A41;
loc_00846302:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == 0xC0000034ULL) goto loc_00845D7A;
    goto loc_00845EE7;
loc_00846318:
    goto loc_00846043;
loc_00846321:
    goto loc_00845B9E;
loc_0084632B:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m1B0 + v_stack_p58 + 1 * 1 * 8 - 16) + 140)) & (1)) == 0) goto loc_0084640F;
    result = HvpGetCellFlat(*(unsigned __int64 *)(v_stack_m1B0 + v_stack_p58 + 1 * 1 * 8 - 16), (unsigned int)((unsigned int)(v_stack_p58)), v_stack_m170, (unsigned int)(v_stack_m160));
loc_00846344:
    v_stack_p30 = (unsigned int)(v_stack_m1B0);
    v_stack_p28 = (unsigned int)((unsigned int)(a5));
    v_stack_p20 = v_stack_m118;
    result = CmpSetValueKeyExisting(*(unsigned __int64 *)(v_stack_p58 + 32), (unsigned int)((unsigned int)(v_stack_p58)), result, (unsigned int)(v_stack_m17C));
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_p58 + 32) + 140)) & (1)) != 0) goto loc_008465AB;
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(v_stack_p58 + 32), v_stack_m170, result, (unsigned int)(v_stack_m17C));
loc_00846390:
    if (sign_flag) goto loc_00846747;
    goto loc_008461ED;
loc_008463A4:
    result = (unsigned __int16)((result) - 1);
    goto loc_00845B86;
loc_008463AC:
    result = CmpLockKcbExclusive(*(unsigned __int64 *)(v_stack_m1B0 + v_stack_p48 * 8 - 16), v_stack_m170, result, (unsigned int)(v_stack_m17C));
    goto loc_00845A3D;
loc_008463BB:
    if (*(unsigned __int64 *)((unsigned int)(a5) + 192) == 0) goto loc_00845976;
loc_008463D0:
    if (((unsigned __int16)(v_stack_p48)) >= 2) goto loc_00846627;
    *(unsigned __int64 *)(v_rsp + (__int16)((unsigned __int16)(v_stack_p48)) * 8 + 112) = *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(a5) + 192) + 16);
loc_008463EB:
    v_rsi = (unsigned __int16)((v_stack_p48) - 1);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(a5) + 192) + 24) != 0) goto loc_008463D0;
    goto loc_0084596C;
loc_008463FC:
    result = CmpSwapValueInList(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(a5) + 192) + 16), (__int16)((unsigned __int16)(v_stack_p48)), (unsigned int)((unsigned int)((unsigned int)(v_stack_m160))), *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(a5) + 192) + 24));
    goto loc_00845E1E;
loc_0084640F:
    result = HvpGetCellPaged(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(a5) + 192) + 16), (__int16)((unsigned __int16)(v_stack_p48)), (unsigned int)((unsigned int)((unsigned int)(v_stack_m160))), *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(a5) + 192) + 24));
    goto loc_00846344;
loc_00846419:
    result = CmpLockKcbExclusive(*(unsigned __int64 *)(v_stack_m188 + result * 8 - 16), (__int16)((unsigned __int16)(v_stack_p48)), (unsigned int)((unsigned int)((unsigned int)(v_stack_m160))), *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(a5) + 192) + 24));
    goto loc_00845A41;
loc_00846433:
    a2 = ((unsigned int)((unsigned int)(result))) << (3);
    result = CmpAllocatePool(256, a2, (unsigned int)(0x35364D43ULL), *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(a5) + 192) + 24));
    v_stack_p48 = result;
    if (result != 0) goto loc_00845946;
    v_r15 = 0;
    v_r12 = 0;
    goto loc_00845F11;
loc_0084646E:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p58 + 8)))) & (8)) == 0) goto loc_00846236;
    result = CmpDelayDerefKeyControlBlock(*(unsigned __int64 *)(v_stack_p58 + 104), v_stack_mE0, (unsigned int)(0x35364D43ULL), *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(a5) + 192) + 24));
    *(unsigned __int64 *)(v_stack_p58 + 104) = 0;
    goto loc_00846236;
loc_0084649E:
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_p58 + 104) + 88) = 0;
    goto loc_00845E3F;
loc_008464AC:
    result = HvpReleaseCellFlat(*(unsigned __int64 *)(v_stack_p58 + 104), v_stack_mE0, (unsigned int)(0x35364D43ULL), *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(a5) + 192) + 24));
    goto loc_00845F0B;
loc_008464C0:
    if (((unsigned __int16)(v_stack_p58)) >= 2) goto loc_00846613;
loc_008464D4:
    result = CmpLockKcbShared(*(unsigned __int64 *)(v_rsp + (__int16)((unsigned __int16)(v_stack_p58)) * 8 + 112), v_stack_mE0, (unsigned int)(0x35364D43ULL), *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(a5) + 192) + 24));
    v_r14 = (unsigned __int16)((v_stack_p58) + 1);
    if (((unsigned int)((__int16)((unsigned __int16)(v_r14)))) > ((unsigned int)((unsigned int)(0xC000009AULL)))) goto loc_00845C98;
    goto loc_008464C0;
loc_008464EB:
    v_r15 = 0;
    v_r12 = 0;
    goto loc_00845F11;
loc_008464FF:
    v_r12 = 0;
    goto loc_00845F17;
loc_0084650F:
    goto loc_008462B2;
loc_00846520:
    if (0 >= 2) goto loc_0084661D;
loc_00846534:
    result = CmpLockKcbShared(*(unsigned __int64 *)(v_rsp + (__int16)(0) * 8 + 112), v_stack_mE0, (unsigned int)(0x35364D43ULL), *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(a5) + 192) + 24));
    v_r15 = (unsigned __int16)((v_r15) + 1);
    if (((unsigned int)((__int16)((unsigned __int16)(v_r15)))) > ((unsigned int)((unsigned int)(0xC0000022ULL)))) goto loc_00846069;
    goto loc_00846520;
loc_0084654B:
    goto loc_00845E97;
loc_00846555:
    if (v_stack_m17C != 6) goto loc_008465A1;
    if ((((unsigned __int8)((unsigned int)(a5))) & (1)) != 0) goto loc_008465A1;
    if (((unsigned int)((unsigned int)(a5))) > 0xFFFFULL) goto loc_008465A1;
    if (v_stack_m158 == 0) goto loc_008465A1;
    result = RtlEqualUnicodeString(v_rip + 7943809, v_stack_m158, 1, *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(a5) + 192) + 24));
    if ((unsigned __int8)(result) == 0) goto loc_008465A1;
    result = RtlIsSandboxedToken(v_stack_mA0, v_stack_p60, 1, *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(a5) + 192) + 24));
    if ((unsigned __int8)(result) == 0) goto loc_00845BB9;
loc_008465A1:
    goto loc_00846186;
loc_008465AB:
    result = HvpReleaseCellFlat(v_stack_mA0, v_stack_p60, 1, *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(a5) + 192) + 24));
    goto loc_00846390;
loc_008465B5:
    v_r14 = 0;
    v_r15 = 0;
    v_r12 = 0;
    goto loc_00845F17;
loc_008465CC:
    a3 = 0;
    result = CmpGetSecurityCacheEntryForKcbStack(v_stack_p68, 0, a3, *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(a5) + 192) + 24));
    result = CmpAllocatePool(256, (unsigned int)(*(unsigned int *)(result + 24)), (unsigned int)(0x33414D43ULL), *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(a5) + 192) + 24));
    if (result != 0) goto loc_00846681;
loc_00846603:
    goto loc_00845EE7;
loc_00846613:
    goto loc_008464D4;
loc_0084661D:
    goto loc_00846534;
loc_00846627:
    *(unsigned __int64 *)(result + (unsigned int)(*(unsigned int *)(result + 24)) * 8 - 16) = *(unsigned __int64 *)(result + result * 8 - 16);
    goto loc_008463EB;
loc_00846631:
    result = CmpSnapshotTxOwnerArray(*(unsigned __int64 *)(result + result * 8 - 16), v_stack_m168, v_stack_m120, *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(a5) + 192) + 24));
    if (sign_flag) goto loc_008459D8;
    a2 = 0;
    v_stack_p20 = (unsigned int)((unsigned int)(v_stack_m168));
    result = CmpLogTransactionAbortedWithChildName(v_stack_p42, a2, a2 + 1, *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(a5) + 192) + 24));
    result = CmpUnlockKcbStack(v_stack_p68, a2, a2 + 1, *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(a5) + 192) + 24));
    v_r15 = 0;
    result = CmSiFreeMemory(result, a2, a2 + 1, *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(a5) + 192) + 24));
loc_00846681:
    result = memcpy(result, (unsigned int)((unsigned int)(result)) + 32, (unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)(result)) + 24)), *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(a5) + 192) + 24));
    v_stack_m138 = result;
    if (((unsigned int)(v_stack_p42)) != -1) goto loc_008466EA;
    v_stack_m178 = 0;
    v_stack_m138 = result;
    goto loc_00845D90;
loc_008466B3:
    result = CmSiFreeMemory(result, (unsigned int)((unsigned int)(result)) + 32, (unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)(result)) + 24)), *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(a5) + 192) + 24));
    goto loc_00845AC7;
loc_008466BD:
loc_008466C9:
    v_stack_mF0 = 0xFFFFFFFFFF676980ULL;
    a2 = 0;
    a1 = 0;
    result = KeDelayExecutionThread(a1, a2, v_stack_mF0, *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(a5) + 192) + 24));
    v_stack_m164 = 0;
    goto loc_00845B51;
loc_008466EA:
    result = HvpGetCellFlat(*(unsigned __int64 *)(v_stack_p58 + 32), 0, v_stack_m170, *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(a5) + 192) + 24));
loc_0084670D:
    result = HvpReleaseCellFlat(*(unsigned __int64 *)(v_r14 + 32), v_stack_m148, v_stack_m170, *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(a5) + 192) + 24));
loc_00846736:
    goto loc_00845EEC;
loc_00846747:
    goto loc_00845EEC;
loc_0084675A:
    goto loc_0084627D;
loc_00846763:
    goto loc_008459D8;
loc_0084676D:
    goto loc_008459D8;
loc_00846777:
    v_r12 = 0;
    goto loc_00846788;
loc_00846780:
    v_r12 = 0;
loc_00846788:
    v_rdi = (unsigned int)(0xC0000425ULL);
    if (((*(unsigned __int8 *)(v_r14 + 48)) & (1)) == 0) { v_rdi = (unsigned int)((unsigned int)(0xC000017CULL)); }
    goto loc_00846186;
loc_0084679A:
    result = CmpFreeValue(*(unsigned __int64 *)(0 + 32), v_stack_m148, v_stack_m170, *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(a5) + 192) + 24));
    goto loc_00845F28;
loc_008467A8:
    result = CmpRundownUnitOfWork(result, v_stack_m148, v_stack_m170, *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(a5) + 192) + 24));
    result = ExFreePoolWithTag(v_stack_m140, (unsigned int)(0x77554D43ULL), v_stack_m170, *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(a5) + 192) + 24));
    goto loc_00845F35;
loc_008467C3:
    result = HvFreeCell(*(unsigned __int64 *)(0 + 32), (unsigned int)(0x77554D43ULL), v_stack_m170, *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(a5) + 192) + 24));
    goto loc_008460BD;
loc_008467D1:
    result = HvUnlockHiveFlusherShared(*(unsigned __int64 *)(0 + 32), (unsigned int)(0x77554D43ULL), v_stack_m170, *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(a5) + 192) + 24));
    goto loc_00845F49;
loc_008467DF:
    result = CmpFreePoolWithTag(*(unsigned __int64 *)(0 + 32), (unsigned int)(0x34414D43ULL), v_stack_m170, *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(a5) + 192) + 24));
    goto loc_00845FB7;
loc_008467EE:
    result = CmpFreePoolWithTag((unsigned int)(v_stack_m168), (unsigned int)(0x33414D43ULL), v_stack_m170, *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(a5) + 192) + 24));
    goto loc_00845FC0;
}
```

## 5. (Beta) C Style

```c
int64_t CmSetValueKey(int64_t Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4, uint32_t Arg5, int64_t Arg6, uint8_t Arg7)
{
    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint32_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint64_t v_stack_m148;
    uint64_t v_stack_m158;
    uint32_t v_stack_m160;
    uint32_t v_stack_m164;
    uint32_t v_stack_m168;
    uint64_t v_stack_m170;
    uint32_t v_stack_m178;
    uint32_t v_stack_m17C;
    uint32_t v_stack_m180;
    uint64_t v_stack_m188;
    uint64_t v_stack_m190;
    uint64_t v_stack_m198;
    uint16_t v_stack_m19E;
    uint64_t v_stack_m1A0;
    uint8_t v_stack_m1A8;
    uint64_t v_stack_m1B0;
    uint8_t v_stack_m1B8;
    uint64_t v_stack_m1C0;
    uint8_t v_stack_m1C5;
    uint8_t v_stack_m1C6;
    uint8_t v_stack_m1C7;
    uint8_t v_stack_m1C8;
    uint64_t v_stack_m1D8;
    uint64_t v_stack_m1E0;
    uint32_t v_stack_m1E8;
    uint64_t v_stack_m50;
    uint64_t v_stack_m60;
    uint64_t v_stack_m70;
    uint64_t v_stack_m80;
    uint64_t v_stack_m90;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint32_t v_stack_p20;
    uint64_t v_stack_p28;
    uint32_t v_stack_p30;
    uint32_t v_stack_p38;
    uint8_t v_stack_p40;
    uint8_t v_stack_p42;
    uint8_t v_stack_p43;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint8_t v_stack_p60;
    uint64_t v_stack_p68;
    uint16_t v_stack_p6A;
    uint64_t v_stack_p70;

    local_rsp = (local_rsp) - (456);
    result = (*(uint64_t *)(v_rip + 0x5C4F5D)) ^ (local_rsp);
    v_stack_m50 = result;
    local_r15 = 0;
    v_stack_mE8 = Arg6;
    v_stack_m110 = Arg1;
    v_stack_m100 = v_stack_m108;
    v_stack_m118 = Arg4;
    v_stack_m108 = v_stack_m108;
    v_stack_m17C = Arg3;
    v_stack_m1A0 = v_xmm0;
    v_stack_m19E = (uint16_t)((uint32_t)(0xFFFFFFFFULL));
    v_stack_m158 = Arg2;
    v_stack_m168 = 0;
    v_stack_m120 = 0;
    v_stack_m148 = 0;
    v_stack_m160 = 0;
    v_stack_m170 = 0;
    v_stack_m80 = v_xmm0;
    v_stack_m140 = 0;
    v_stack_m70 = v_xmm0;
    v_stack_m1B8 = 0;
    v_stack_m60 = v_xmm0;
    v_stack_m164 = 0;
    v_stack_mE0 = v_xmm0;
    v_stack_m128 = 0;
    v_stack_m190 = v_xmm0;
    v_stack_m1B0 = 0;
    result = HvpGetCellContextInitialize(v_stack_m148, Arg2, Arg3, Arg4);
    result = HvpGetCellContextInitialize(v_stack_m170, Arg2, Arg3, Arg4);
    result = CmpInitializeDelayDerefContext(v_stack_mE0, Arg2, Arg3, Arg4);
    v_stack_mD0 = v_xmm0;
    v_stack_m130 = 0xFFFFFFFFULL;
    v_stack_mC0 = v_xmm0;
    v_stack_m180 = 0xFFFFFFFFULL;
    v_stack_m138 = 0;
    v_stack_m178 = 0;
    v_stack_m1A8 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    v_stack_mA0 = v_xmm0;
    v_stack_m90 = v_xmm0;
    result = SeCaptureSubjectContext(v_stack_mA0, Arg2, Arg3, Arg4);
    result = CmpAttachToRegistryProcess(v_stack_m80, Arg2, Arg3, Arg4);
loc_008458E2:
    result = CmpIsShutdownRundownActive(v_stack_m80, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) != 0) goto loc_008465B5;
    result = CmpLockRegistry(v_stack_m80, Arg2, Arg3, Arg4);
    v_stack_m1C7 = 1;
    v_stack_m1B0 = *(uint64_t *)(Arg1 + 0x8);
    if (((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x20) + 0xA0)) & (0x100000ULL)) != 0) goto loc_008464EB;
    v_stack_m1C0 = 0;
    if (((uint32_t)((int16_t)(*(uint16_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x42)))) < 2) goto loc_00845946;
    result = (uint32_t)(((uint32_t)((uint32_t)((int16_t)(*(uint16_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x42))))) - (1));
    if (condition_is_not_equal) goto loc_00846433;
loc_00845946:
    v_stack_m1A0 = (uint16_t)((int16_t)(*(uint16_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x42)));
    v_stack_m188 = 0;
    v_stack_m19E = (uint16_t)((int16_t)(*(uint16_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x42)));
    if ((uint16_t)((int16_t)(*(uint16_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x42))) != 0) goto loc_008463BB;
    *(uint64_t *)(local_rsp + (int16_t)(*(uint16_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x42)) * 8 + 0x70) = *(uint64_t *)(Arg1 + 0x8);
loc_0084596C:
    v_stack_m1C0 = v_stack_m188;
loc_00845976:
    if ((*(uint64_t *)(Arg1 + 0x38)) == 0) goto loc_008459E0;
loc_0084597D:
    result = CmpLockKcbStackTopExclusiveRestShared(v_stack_m1A0, Arg2, Arg3, Arg4);
loc_0084598A:
    v_stack_m1C5 = 1;
    v_stack_m1C8 = 1;
    if ((*(uint64_t *)(Arg1 + 0x38)) == 0) goto loc_00845A32;
loc_0084599F:
    Arg2 = 0;
    result = CmpIsKeyDeletedForKeyBody(Arg1, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) != 0) goto loc_00846780;
    result = CmpTransSearchAddTransFromKeyBody(Arg1, v_stack_m128, Arg3, Arg4);
    if (sign_flag) goto loc_008459D8;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x20) + 0xA0)))) & (2)) == 0) goto loc_00845A3D;
loc_008459D3:
loc_008459D8:
    local_r12 = 0;
    goto loc_00846186;
loc_008459E0:
    if ((*(uint64_t *)(Arg1 + 0x40)) != 0) goto loc_0084597D;
    if (1 > ((uint16_t)(v_stack_m19E))) goto loc_00845A2A;
    local_r15 = (v_stack_m188) - (v_stack_m198);
    local_r15 = (local_r15) + (-16);
loc_00845A05:
    if (1 >= 2) goto loc_0084609A;
loc_00845A12:
    result = CmpLockKcbShared(*(uint64_t *)(v_stack_m198), v_stack_m128, Arg3, Arg4);
    local_rdi = (uint16_t)((1) + 1);
    local_r14 = (v_stack_m198) + (8);
    if (((uint16_t)(local_rdi)) <= ((uint16_t)(v_stack_m19E))) goto loc_00845A05;
loc_00845A2A:
    local_r15 = 0;
    goto loc_0084598A;
loc_00845A32:
    if ((*(uint64_t *)(v_stack_m110 + 0x40)) != 0) goto loc_0084599F;
loc_00845A3D:
loc_00845A41:
    result = CmpIsKeyDeletedForKeyBody(v_stack_m110, v_stack_m128, Arg3, Arg4);
    if ((uint8_t)(result) != 0) goto loc_00846777;
    if ((*(uint8_t *)(local_r12 + 0x41)) == 1) goto loc_0084676D;
    if (v_stack_m128 != 0) goto loc_008460DD;
    if ((*(uint32_t *)(local_r12 + 0xF8)) >= ((uint32_t)(v_stack_m128))) goto loc_00845B65;
    result = CmpSnapshotTxOwnerArray(local_r12 + 248, v_stack_m168, v_stack_m120, Arg4);
    if (sign_flag) goto loc_008459D8;
    local_rdi = 0;
    Arg2 = 0;
    v_stack_mB0 = v_xmm0;
    v_stack_mF8 = 0;
    result = RtlInitUnicodeString(v_stack_mB0, Arg2, v_stack_m120, Arg4);
    if (v_stack_mA8 != 0) goto loc_008466B3;
loc_00845AC7:
    if (0 > ((uint16_t)(v_stack_m19E))) goto loc_00845B06;
    local_r15 = (v_stack_m188) - (v_stack_m198);
    local_r15 = (local_r15) + (-16);
loc_00845AE3:
    if (0 >= 2) goto loc_00846091;
loc_00845AF0:
    result = CmpUnlockKcb(*(uint64_t *)(v_stack_m198), Arg2, v_stack_m120, Arg4);
    local_rbx = (uint16_t)((0) + 1);
    local_rdi = (v_stack_m198) + (8);
    if (((uint16_t)(local_rbx)) <= ((uint16_t)(v_stack_m19E))) goto loc_00845AE3;
    local_rdi = 0;
loc_00845B06:
    local_r15 = 0;
    v_stack_m1C8 = 0;
    if (v_stack_m188 != 0) {
        Arg1 = v_stack_m188;
        result = CmSiFreeMemory(Arg1, Arg2, v_stack_m120, Arg4);
    }
    v_stack_m1A0 = v_xmm0;
    v_stack_m19E = (uint16_t)((uint32_t)(0xFFFFFFFFULL));
    v_stack_m190 = v_xmm0;
    result = CmpUnlockRegistry(Arg1, Arg2, v_stack_m120, Arg4);
    if ((uint32_t)((uint32_t)(v_stack_m168)) != 0) goto loc_008466BD;
    result = (uint32_t)(((uint32_t)(v_stack_m164)) + 1);
    v_stack_m164 = (uint32_t)(result);
    if (((uint32_t)(result)) > 10) goto loc_008466C9;
loc_00845B51:
    if (sign_flag) goto loc_008464FF;
    local_r15 = 0;
    goto loc_008458E2;
loc_00845B65:
    if ((*(uint32_t *)(local_r12 + 0x108)) != 0) goto loc_00846631;
loc_00845B7B:
    local_r12 = 0;
    v_stack_m1C6 = 0;
loc_00845B86:
    if (sign_flag) goto loc_00845BB9;
    if (((uint16_t)((uint16_t)(v_stack_m19E))) >= 2) goto loc_00846321;
loc_00845B9E:
    if ((*(uint32_t *)(*(uint64_t *)(local_rsp + (int16_t)((uint16_t)((uint16_t)(v_stack_m19E))) * 8 + 0x70) + 0x28)) == -1) goto loc_008463A4;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp + (int16_t)((uint16_t)((uint16_t)(v_stack_m19E))) * 8 + 0x70) + 0xB8))) >> (20));
    if ((((uint8_t)(result)) & (1)) != 0) goto loc_00846555;
loc_00845BB9:
    if ((*(uint32_t *)(v_stack_m1B0 + 0x28)) == -1) goto loc_00846287;
    if (0 != 0) goto loc_008460A3;
    v_stack_m1E8 = (uint32_t)((uint32_t)(Arg5));
    result = CmpCompareNewValueDataAgainstKCBCache(v_stack_m1B0, v_stack_m158, (uint32_t)(v_stack_m17C), v_stack_m118);
    if (((uint32_t)(result)) == 1) goto loc_00846018;
    if ((uint32_t)(result) == 0) goto loc_00846184;
    v_stack_m1C5 = 1;
    if ((*(uint64_t *)(v_stack_m1B0 + 0x38)) == (*(uint64_t *)(gs_base + (0 + 0x188)))) goto loc_00845CB0;
    if ((*(uint64_t *)(v_stack_m1B0 + 0x38)) == (*(uint64_t *)(gs_base + (0 + 0x188)))) goto loc_00845FF3;
    result = 0;
    v_stack_m1C0 = v_stack_m188;
    if (0 > ((uint16_t)((int16_t)(v_stack_m19E)))) goto loc_00845C89;
    local_r15 = (v_stack_m188) - (v_stack_m198);
    local_r15 = (local_r15) + (-16);
loc_00845C60:
    if (0 >= 2) goto loc_00846190;
loc_00845C6D:
    result = CmpUnlockKcb(*(uint64_t *)(v_stack_m198), v_stack_m158, (uint32_t)(v_stack_m17C), v_stack_m118);
    local_rdi = (uint16_t)((0) + 1);
    local_r14 = (v_stack_m198) + (8);
    if (((uint16_t)(local_rdi)) <= ((uint16_t)((int16_t)(v_stack_m19E)))) goto loc_00845C60;
    result = 0;
loc_00845C89:
    local_rdi = (uint32_t)(((uint32_t)((uint32_t)((int16_t)(v_stack_m19E)))) - (1));
    if (!sign_flag) goto loc_008464C0;
loc_00845C98:
    if (((uint32_t)((int16_t)(v_stack_m19E))) >= 2) goto loc_008463AC;
    result = CmpLockKcbExclusive(*(uint64_t *)(local_rsp + (int16_t)(v_stack_m19E) * 8 + 0x70), v_stack_m158, (uint32_t)(v_stack_m17C), v_stack_m118);
    goto loc_00845A3D;
loc_00845CB0:
    v_stack_m1C0 = v_stack_m188;
loc_00845CC2:
    result = HvLockHiveFlusherShared(*(uint64_t *)(v_stack_m1B0 + 0x20), v_stack_m158, (uint32_t)(v_stack_m17C), v_stack_m118);
    v_stack_m1C6 = 1;
    if (v_stack_m128 != 0) goto loc_00845D02;
    Arg4 = 0;
    Arg3 = 0;
    result = HvpMarkCellDirty(*(uint64_t *)(v_stack_m1B0 + 0x20), (uint32_t)(*(uint32_t *)(v_stack_m1B0 + 0x28)), Arg3, Arg4);
    if (sign_flag) goto loc_00846186;
loc_00845D02:
    if (((*(uint8_t *)(*(uint64_t *)(v_stack_m1B0 + 0x20) + 0x8C)) & (1)) == 0) goto loc_00846199;
    result = HvpGetCellFlat(*(uint64_t *)(v_stack_m1B0 + 0x20), (uint32_t)(*(uint32_t *)(v_stack_m1B0 + 0x28)), v_stack_m148, Arg4);
loc_00845D24:
    result = CmpUpdateKeyNodeAccessBits(*(uint64_t *)(v_stack_m1B0 + 0x20), result, (uint32_t)(*(uint32_t *)(v_stack_m1B0 + 0x28)), Arg4);
    Arg4 = 0;
    v_stack_m1E0 = v_stack_m130;
    v_stack_m1E8 = v_stack_m160;
    if (v_stack_m128 == 0) goto loc_00846257;
    result = CmpFindNameInListWithStatus(*(uint64_t *)(v_stack_m1B0 + 0x20), v_stack_m1B0 + 280, v_stack_m158, Arg4);
    result = (uint32_t)((result) + ((uint32_t)((uint32_t)(0x80000000ULL))));
    if ((((uint32_t)((uint32_t)(0x80000000ULL))) & ((uint32_t)(result))) == 0) goto loc_00846302;
loc_00845D7A:
    if (Arg7 != 0) goto loc_008465CC;
loc_00845D90:
    local_r13 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m1B0 + 0x28))) >> (31));
    if (v_stack_m128 == 0) goto loc_008461A3;
    v_stack_m1D8 = v_stack_m180;
    v_stack_m1E0 = 1;
    v_stack_m1E8 = (uint32_t)((uint32_t)(Arg5));
    result = CmpAddValueKeyNew(*(uint64_t *)(v_stack_m1B0 + 0x20), v_stack_m158, (uint32_t)(v_stack_m17C), v_stack_m118);
    if (sign_flag) goto loc_0084675A;
    if (((uint32_t)((uint32_t)(v_stack_m130))) != -1) goto loc_008463FC;
    v_stack_m1E0 = 1;
    v_stack_m1E8 = v_stack_m1B0 + 280;
    result = CmpAddValueToListEx(*(uint64_t *)(v_stack_m1B0 + 0x20), (uint32_t)(v_stack_m180), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m1B0 + 0x118)))), 1);
    if (sign_flag) goto loc_00846736;
loc_00845E1E:
    result = HvUnlockHiveFlusherShared(*(uint64_t *)(v_stack_m1B0 + 0x20), (uint32_t)(v_stack_m180), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m1B0 + 0x118)))), 1);
    v_stack_m1C6 = 0;
    if (((uint32_t)((uint32_t)(v_stack_m130))) != -1) goto loc_0084649E;
loc_00845E3F:
    *(uint32_t *)(v_stack_m140 + 0x44) = 4;
    *(uint32_t *)(v_stack_m140 + 0x5C) = (uint32_t)((uint32_t)(v_stack_m180));
    *(uint32_t *)(v_stack_m140 + 0x48) = (uint32_t)(local_r13);
    result = CmAddLogForAction(v_stack_m140, 1, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m1B0 + 0x118)))), 1);
    if (sign_flag) goto loc_0084670D;
loc_00845E68:
    local_r14 = 0;
    v_stack_m180 = 0xFFFFFFFFULL;
    v_stack_m140 = 0;
    v_stack_m1B8 = 0;
    if (((uint16_t)(v_stack_m19E)) >= 2) goto loc_0084654B;
loc_00845E97:
    v_stack_m1E8 = v_stack_m108;
    result = CmpReportNotifyHelper(v_stack_m1A0, *(uint64_t *)(*(uint64_t *)(local_rsp + (int16_t)(v_stack_m19E) * 8 + 0x70) + 0x20), v_stack_m128, 4);
    if ((*(uint64_t *)(*(uint64_t *)(local_rsp + (int16_t)(v_stack_m19E) * 8 + 0x70) + 0x20)) != (*(uint64_t *)(v_rip + 0x793BCE))) {
        result = v_stack_m108;
        Arg4 = 4;
        Arg3 = v_stack_m128;
        v_stack_m1E8 = result;
        Arg1 = v_stack_m1A0;
        result = CmpReportNotifyHelper(Arg1, *(uint64_t *)(v_rip + 0x793BCE), Arg3, Arg4);
    }
loc_00845EE7:
loc_00845EEC:
    if (result == 0) goto loc_00845F0B;
    if (((*(uint8_t *)(*(uint64_t *)(v_stack_m1B0 + 0x20) + 0x8C)) & (1)) != 0) goto loc_008464AC;
    result = HvpReleaseCellPaged(*(uint64_t *)(v_stack_m1B0 + 0x20), v_stack_m148, Arg3, Arg4);
loc_00845F0B:
loc_00845F11:
loc_00845F17:
    if (((uint32_t)((uint32_t)(v_stack_m180))) != -1) goto loc_0084679A;
loc_00845F28:
    if (v_stack_m140 != 0) goto loc_008467A8;
loc_00845F35:
    if (v_stack_m1B8 != 0) goto loc_008460AD;
loc_00845F40:
    if ((uint8_t)(v_stack_m1C6) != 0) goto loc_008467D1;
loc_00845F49:
    result = v_stack_m140;
    if ((uint8_t)(v_stack_m1C8) != 0) {
        Arg1 = v_stack_m1A0;
        result = CmpUnlockKcbStack(Arg1, (uint32_t)(v_stack_m180), Arg3, Arg4);
    }
    Arg2 = 0;
    result = CmpDrainDelayDerefContext(v_stack_mE0, Arg2, Arg3, Arg4);
    if ((uint8_t)(v_stack_m1C7) != 0) {
        result = CmpUnlockRegistry(v_stack_mE0, Arg2, Arg3, Arg4);
    }
    result = v_stack_m108;
    if (v_stack_m108 != v_stack_m108) {
        Arg1 = v_stack_m108;
        result = CmpSignalDeferredPosts(Arg1, Arg2, Arg3, Arg4);
    }
    result = CmpDetachFromRegistryProcess(v_stack_m80, Arg2, Arg3, Arg4);
    result = SeReleaseSubjectContext(v_stack_mA0, Arg2, Arg3, Arg4);
    if (sign_flag) goto loc_00845FAA;
loc_00845FAA:
    if (v_stack_mC8 != 0) goto loc_008467DF;
loc_00845FB7:
    if (v_stack_m138 != 0) goto loc_008467EE;
loc_00845FC0:
    if (v_stack_m188 != 0) {
        Arg1 = v_stack_m188;
        result = CmSiFreeMemory(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (v_stack_m50) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (456);
    return result;
loc_00845FF3:
    v_stack_p48 = v_stack_m188;
    *(uint64_t *)(v_stack_m1C6 + 0x38) = *(uint64_t *)(gs_base + (0 + 0x188));
    goto loc_00845CC2;
loc_00846018:
    result = 0;
    if (0 > ((uint16_t)(v_stack_p6A))) goto loc_00846059;
    local_r12 = (v_stack_m1B0) - (v_stack_p70);
    local_r12 = (local_r12) + (-16);
loc_00846036:
    if (0 >= 2) goto loc_00846318;
loc_00846043:
    result = CmpUnlockKcb(*(uint64_t *)(v_stack_p70), Arg2, Arg3, Arg4);
    local_rdi = (uint16_t)((0) + 1);
    local_r15 = (v_stack_p70) + (8);
    if (((uint16_t)(local_rdi)) <= ((uint16_t)(v_stack_p6A))) goto loc_00846036;
    result = 0;
loc_00846059:
    local_rdi = (uint32_t)(((int16_t)((uint16_t)(v_stack_p6A))) - (1));
    if (!sign_flag) goto loc_00846520;
loc_00846069:
    if (((uint16_t)(v_stack_p6A)) >= 2) goto loc_00846419;
    result = CmpLockKcbExclusive(*(uint64_t *)(local_rsp + (int16_t)((uint16_t)(v_stack_p6A)) * 8 + 0x70), Arg2, Arg3, Arg4);
    goto loc_00845A41;
loc_00846091:
    goto loc_00845AF0;
loc_0084609A:
    goto loc_00845A12;
loc_008460A3:
    goto loc_00845CC2;
loc_008460AD:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m1B0 + 0x11C)))) != -1) goto loc_008467C3;
loc_008460BD:
    result = 0;
    *(uint32_t *)(v_stack_m1B0 + 0x11C) = 0xFFFFFFFFULL;
    *(uint32_t *)(v_stack_m1B0 + 0x118) = 0;
    *(uint64_t *)(v_stack_m1B0 + 0x120) = 0;
    goto loc_00845F40;
loc_008460DD:
    result = CmpAllocateUnitOfWork(v_stack_p43 + v_stack_m128 * 1, (uint32_t)(*(uint32_t *)(v_stack_m1B0 + 0x11C)), Arg3, Arg4);
    v_stack_m140 = result;
    if (result == 0) goto loc_00846763;
    result = CmpTransEnlistUowInKcb(result, v_stack_p58, Arg3, Arg4);
    result = CmpTransEnlistUowInCmTrans(result, v_stack_m128, Arg3, Arg4);
    if (sign_flag) goto loc_008459D8;
    result = CmpLockIXLockIntent(v_stack_p58 + 248, v_stack_m140, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_008459D3;
    result = CmpLockIXLockExclusive(v_stack_p58 + 264, v_stack_m140, 1, Arg4);
    if ((uint8_t)(result) == 0) goto loc_008459D3;
    result = HvLockHiveFlusherShared(*(uint64_t *)(v_stack_p58 + 0x20), v_stack_m140, 1, Arg4);
    result = CmpCloneKCBValueListForTrans(v_stack_p58, v_stack_m128, v_stack_p50, Arg4);
    if (sign_flag) goto loc_00846186;
    result = HvUnlockHiveFlusherShared(*(uint64_t *)(v_stack_p58 + 0x20), v_stack_m128, v_stack_p50, Arg4);
    goto loc_00845B7B;
loc_00846184:
    local_rdi = 0;
loc_00846186:
    goto loc_00845F0B;
loc_00846190:
    goto loc_00845C6D;
loc_00846199:
    result = HvpGetCellPaged(v_stack_p43 + v_stack_m128 * 1, v_stack_m128, v_stack_p50, Arg4);
    goto loc_00845D24;
loc_008461A3:
    if (1 != -1) goto loc_0084632B;
    v_stack_p38 = (uint32_t)(v_stack_m1B0);
    v_stack_p30 = (uint32_t)((uint32_t)(Arg5));
    v_stack_p28 = v_stack_m118;
    v_stack_p20 = (uint32_t)((uint32_t)(v_stack_m17C));
    result = CmpSetValueKeyNew(v_stack_p43 + v_stack_m128 * 1, v_stack_p43, v_stack_m158, (uint32_t)(v_stack_m160));
    if (sign_flag) goto loc_00846603;
loc_008461ED:
    result = *(uint16_t *)(v_stack_m158);
    if ((*(uint32_t *)(v_stack_p43 + 0x3C)) < ((uint32_t)(*(uint16_t *)(v_stack_m158)))) {
        *(uint32_t *)(v_stack_p43 + 0x3C) = (uint32_t)(*(uint16_t *)(v_stack_m158));
        result = *(uint16_t *)(v_stack_m158);
        *(uint16_t *)(v_stack_p58 + 0xB2) = (uint16_t)(result);
    }
    if ((*(uint32_t *)(v_stack_p43 + 0x40)) < ((uint32_t)((uint32_t)(Arg5)))) {
        *(uint32_t *)(v_stack_p43 + 0x40) = (uint32_t)((uint32_t)(Arg5));
        *(uint32_t *)(v_stack_p58 + 0xB4) = (uint32_t)((uint32_t)(Arg5));
    }
    *(uint64_t *)(v_stack_p43 + 0x4) = v_stack_m138;
    *(uint64_t *)(v_stack_p58 + 0xA8) = v_stack_m138;
    if (((*(uint32_t *)(v_stack_p58 + 0xB8)) & (0x400000ULL)) == 0) goto loc_0084646E;
loc_00846236:
    *(uint32_t *)(v_stack_p58 + 0x64) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p43 + 0x28)));
    *(uint32_t *)(v_stack_p58 + 0x60) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p43 + 0x24)));
    result = HvUnlockHiveFlusherShared(*(uint64_t *)(v_stack_p58 + 0x20), v_stack_p43, v_stack_m158, (uint32_t)(v_stack_m160));
    local_r12 = 0;
    goto loc_00845E68;
loc_00846257:
    result = CmpFindNameInListWithStatus(*(uint64_t *)(v_stack_p58 + 0x20), v_stack_p43 + 36, v_stack_m158, (uint32_t)(v_stack_m160));
    result = (uint32_t)((result) + ((uint32_t)((uint32_t)(0x80000000ULL))));
    if ((((uint32_t)((uint32_t)(0x80000000ULL))) & ((uint32_t)(result))) != 0) goto loc_00845D7A;
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == 0xC0000034ULL) goto loc_00845D7A;
loc_0084627D:
    goto loc_00845EE7;
loc_00846287:
    result = 0;
    if (0 > ((uint16_t)(v_stack_p48))) goto loc_008462CC;
    local_r12 = (v_stack_m1B0) - (v_stack_p70);
    local_r12 = (local_r12) + (-16);
loc_008462A5:
    if (0 >= 2) goto loc_0084650F;
loc_008462B2:
    result = CmpUnlockKcb(*(uint64_t *)(v_stack_p70), v_stack_p43 + 36, v_stack_m158, (uint32_t)(v_stack_m160));
    local_rdi = (uint16_t)((0) + 1);
    local_r15 = (v_stack_p70) + (8);
    if (((uint16_t)(local_rdi)) <= ((uint16_t)(v_stack_p48))) goto loc_008462A5;
loc_008462CC:
    result = 0;
    v_stack_p40 = 0;
    Arg2 = 0;
    result = CmpPromoteKey(v_stack_p68, Arg2, 1, (uint32_t)(v_stack_m160));
    if (sign_flag) goto loc_00846186;
    v_stack_p43 = 1;
    v_stack_p40 = 1;
    goto loc_00845A41;
loc_00846302:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == 0xC0000034ULL) goto loc_00845D7A;
    goto loc_00845EE7;
loc_00846318:
    goto loc_00846043;
loc_00846321:
    goto loc_00845B9E;
loc_0084632B:
    if (((*(uint8_t *)(*(uint64_t *)(v_stack_m1B0 + v_stack_p58 + 0x1 * 1 * 8 - 0x10) + 0x8C)) & (1)) == 0) goto loc_0084640F;
    result = HvpGetCellFlat(*(uint64_t *)(v_stack_m1B0 + v_stack_p58 + 0x1 * 1 * 8 - 0x10), (uint32_t)((uint32_t)(v_stack_p58)), v_stack_m170, (uint32_t)(v_stack_m160));
loc_00846344:
    v_stack_p30 = (uint32_t)(v_stack_m1B0);
    v_stack_p28 = (uint32_t)((uint32_t)(Arg5));
    v_stack_p20 = v_stack_m118;
    result = CmpSetValueKeyExisting(*(uint64_t *)(v_stack_p58 + 0x20), (uint32_t)((uint32_t)(v_stack_p58)), result, (uint32_t)(v_stack_m17C));
    if (((*(uint8_t *)(*(uint64_t *)(v_stack_p58 + 0x20) + 0x8C)) & (1)) != 0) goto loc_008465AB;
    result = HvpReleaseCellPaged(*(uint64_t *)(v_stack_p58 + 0x20), v_stack_m170, result, (uint32_t)(v_stack_m17C));
loc_00846390:
    if (sign_flag) goto loc_00846747;
    goto loc_008461ED;
loc_008463A4:
    result = (uint16_t)((result) - 1);
    goto loc_00845B86;
loc_008463AC:
    result = CmpLockKcbExclusive(*(uint64_t *)(v_stack_m1B0 + v_stack_p48 * 8 - 0x10), v_stack_m170, result, (uint32_t)(v_stack_m17C));
    goto loc_00845A3D;
loc_008463BB:
    if (*(uint64_t *)((uint32_t)(Arg5) + 0xC0) == 0) goto loc_00845976;
loc_008463D0:
    if (((uint16_t)(v_stack_p48)) >= 2) goto loc_00846627;
    *(uint64_t *)(local_rsp + (int16_t)((uint16_t)(v_stack_p48)) * 8 + 0x70) = *(uint64_t *)(*(uint64_t *)((uint32_t)(Arg5) + 0xC0) + 0x10);
loc_008463EB:
    local_rsi = (uint16_t)((v_stack_p48) - 1);
    if (*(uint64_t *)(*(uint64_t *)((uint32_t)(Arg5) + 0xC0) + 0x18) != 0) goto loc_008463D0;
    goto loc_0084596C;
loc_008463FC:
    result = CmpSwapValueInList(*(uint64_t *)(*(uint64_t *)((uint32_t)(Arg5) + 0xC0) + 0x10), (int16_t)((uint16_t)(v_stack_p48)), (uint32_t)((uint32_t)((uint32_t)(v_stack_m160))), *(uint64_t *)(*(uint64_t *)((uint32_t)(Arg5) + 0xC0) + 0x18));
    goto loc_00845E1E;
loc_0084640F:
    result = HvpGetCellPaged(*(uint64_t *)(*(uint64_t *)((uint32_t)(Arg5) + 0xC0) + 0x10), (int16_t)((uint16_t)(v_stack_p48)), (uint32_t)((uint32_t)((uint32_t)(v_stack_m160))), *(uint64_t *)(*(uint64_t *)((uint32_t)(Arg5) + 0xC0) + 0x18));
    goto loc_00846344;
loc_00846419:
    result = CmpLockKcbExclusive(*(uint64_t *)(v_stack_m188 + result * 8 - 0x10), (int16_t)((uint16_t)(v_stack_p48)), (uint32_t)((uint32_t)((uint32_t)(v_stack_m160))), *(uint64_t *)(*(uint64_t *)((uint32_t)(Arg5) + 0xC0) + 0x18));
    goto loc_00845A41;
loc_00846433:
    Arg2 = ((uint32_t)((uint32_t)(result))) << (3);
    result = CmpAllocatePool(256, Arg2, (uint32_t)(0x35364D43ULL), *(uint64_t *)(*(uint64_t *)((uint32_t)(Arg5) + 0xC0) + 0x18));
    v_stack_p48 = result;
    if (result != 0) goto loc_00845946;
    local_r15 = 0;
    local_r12 = 0;
    goto loc_00845F11;
loc_0084646E:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p58 + 0x8)))) & (8)) == 0) goto loc_00846236;
    result = CmpDelayDerefKeyControlBlock(*(uint64_t *)(v_stack_p58 + 0x68), v_stack_mE0, (uint32_t)(0x35364D43ULL), *(uint64_t *)(*(uint64_t *)((uint32_t)(Arg5) + 0xC0) + 0x18));
    *(uint64_t *)(v_stack_p58 + 0x68) = 0;
    goto loc_00846236;
loc_0084649E:
    *(uint32_t *)(*(uint64_t *)(v_stack_p58 + 0x68) + 0x58) = 0;
    goto loc_00845E3F;
loc_008464AC:
    result = HvpReleaseCellFlat(*(uint64_t *)(v_stack_p58 + 0x68), v_stack_mE0, (uint32_t)(0x35364D43ULL), *(uint64_t *)(*(uint64_t *)((uint32_t)(Arg5) + 0xC0) + 0x18));
    goto loc_00845F0B;
loc_008464C0:
    if (((uint16_t)(v_stack_p58)) >= 2) goto loc_00846613;
loc_008464D4:
    result = CmpLockKcbShared(*(uint64_t *)(local_rsp + (int16_t)((uint16_t)(v_stack_p58)) * 8 + 0x70), v_stack_mE0, (uint32_t)(0x35364D43ULL), *(uint64_t *)(*(uint64_t *)((uint32_t)(Arg5) + 0xC0) + 0x18));
    local_r14 = (uint16_t)((v_stack_p58) + 1);
    if (((uint32_t)((int16_t)((uint16_t)(local_r14)))) > ((uint32_t)((uint32_t)(0xC000009AULL)))) goto loc_00845C98;
    goto loc_008464C0;
loc_008464EB:
    local_r15 = 0;
    local_r12 = 0;
    goto loc_00845F11;
loc_008464FF:
    local_r12 = 0;
    goto loc_00845F17;
loc_0084650F:
    goto loc_008462B2;
loc_00846520:
    if (0 >= 2) goto loc_0084661D;
loc_00846534:
    result = CmpLockKcbShared(*(uint64_t *)(local_rsp + (int16_t)(0) * 8 + 0x70), v_stack_mE0, (uint32_t)(0x35364D43ULL), *(uint64_t *)(*(uint64_t *)((uint32_t)(Arg5) + 0xC0) + 0x18));
    local_r15 = (uint16_t)((local_r15) + 1);
    if (((uint32_t)((int16_t)((uint16_t)(local_r15)))) > ((uint32_t)((uint32_t)(0xC0000022ULL)))) goto loc_00846069;
    goto loc_00846520;
loc_0084654B:
    goto loc_00845E97;
loc_00846555:
    if (v_stack_m17C != 6) goto loc_008465A1;
    if ((((uint8_t)((uint32_t)(Arg5))) & (1)) != 0) goto loc_008465A1;
    if (((uint32_t)((uint32_t)(Arg5))) > 0xFFFFULL) goto loc_008465A1;
    if (v_stack_m158 == 0) goto loc_008465A1;
    result = RtlEqualUnicodeString(v_rip + 7943809, v_stack_m158, 1, *(uint64_t *)(*(uint64_t *)((uint32_t)(Arg5) + 0xC0) + 0x18));
    if ((uint8_t)(result) == 0) goto loc_008465A1;
    result = RtlIsSandboxedToken(v_stack_mA0, v_stack_p60, 1, *(uint64_t *)(*(uint64_t *)((uint32_t)(Arg5) + 0xC0) + 0x18));
    if ((uint8_t)(result) == 0) goto loc_00845BB9;
loc_008465A1:
    goto loc_00846186;
loc_008465AB:
    result = HvpReleaseCellFlat(v_stack_mA0, v_stack_p60, 1, *(uint64_t *)(*(uint64_t *)((uint32_t)(Arg5) + 0xC0) + 0x18));
    goto loc_00846390;
loc_008465B5:
    local_r14 = 0;
    local_r15 = 0;
    local_r12 = 0;
    goto loc_00845F17;
loc_008465CC:
    Arg3 = 0;
    result = CmpGetSecurityCacheEntryForKcbStack(v_stack_p68, 0, Arg3, *(uint64_t *)(*(uint64_t *)((uint32_t)(Arg5) + 0xC0) + 0x18));
    result = CmpAllocatePool(256, (uint32_t)(*(uint32_t *)(result + 0x18)), (uint32_t)(0x33414D43ULL), *(uint64_t *)(*(uint64_t *)((uint32_t)(Arg5) + 0xC0) + 0x18));
    if (result != 0) goto loc_00846681;
loc_00846603:
    goto loc_00845EE7;
loc_00846613:
    goto loc_008464D4;
loc_0084661D:
    goto loc_00846534;
loc_00846627:
    *(uint64_t *)(result + (uint32_t)(*(uint32_t *)(result + 0x18)) * 8 - 0x10) = *(uint64_t *)(result + result * 8 - 0x10);
    goto loc_008463EB;
loc_00846631:
    result = CmpSnapshotTxOwnerArray(*(uint64_t *)(result + result * 8 - 0x10), v_stack_m168, v_stack_m120, *(uint64_t *)(*(uint64_t *)((uint32_t)(Arg5) + 0xC0) + 0x18));
    if (sign_flag) goto loc_008459D8;
    Arg2 = 0;
    v_stack_p20 = (uint32_t)((uint32_t)(v_stack_m168));
    result = CmpLogTransactionAbortedWithChildName(v_stack_p42, Arg2, Arg2 + 1, *(uint64_t *)(*(uint64_t *)((uint32_t)(Arg5) + 0xC0) + 0x18));
    result = CmpUnlockKcbStack(v_stack_p68, Arg2, Arg2 + 1, *(uint64_t *)(*(uint64_t *)((uint32_t)(Arg5) + 0xC0) + 0x18));
    local_r15 = 0;
    result = CmSiFreeMemory(result, Arg2, Arg2 + 1, *(uint64_t *)(*(uint64_t *)((uint32_t)(Arg5) + 0xC0) + 0x18));
loc_00846681:
    result = memcpy(result, (uint32_t)((uint32_t)(result)) + 32, (uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)(result)) + 0x18)), *(uint64_t *)(*(uint64_t *)((uint32_t)(Arg5) + 0xC0) + 0x18));
    v_stack_m138 = result;
    if (((uint32_t)(v_stack_p42)) != -1) goto loc_008466EA;
    v_stack_m178 = 0;
    v_stack_m138 = result;
    goto loc_00845D90;
loc_008466B3:
    result = CmSiFreeMemory(result, (uint32_t)((uint32_t)(result)) + 32, (uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)(result)) + 0x18)), *(uint64_t *)(*(uint64_t *)((uint32_t)(Arg5) + 0xC0) + 0x18));
    goto loc_00845AC7;
loc_008466BD:
loc_008466C9:
    v_stack_mF0 = 0xFFFFFFFFFF676980ULL;
    Arg2 = 0;
    Arg1 = 0;
    result = KeDelayExecutionThread(Arg1, Arg2, v_stack_mF0, *(uint64_t *)(*(uint64_t *)((uint32_t)(Arg5) + 0xC0) + 0x18));
    v_stack_m164 = 0;
    goto loc_00845B51;
loc_008466EA:
    result = HvpGetCellFlat(*(uint64_t *)(v_stack_p58 + 0x20), 0, v_stack_m170, *(uint64_t *)(*(uint64_t *)((uint32_t)(Arg5) + 0xC0) + 0x18));
loc_0084670D:
    result = HvpReleaseCellFlat(*(uint64_t *)(local_r14 + 0x20), v_stack_m148, v_stack_m170, *(uint64_t *)(*(uint64_t *)((uint32_t)(Arg5) + 0xC0) + 0x18));
loc_00846736:
    goto loc_00845EEC;
loc_00846747:
    goto loc_00845EEC;
loc_0084675A:
    goto loc_0084627D;
loc_00846763:
    goto loc_008459D8;
loc_0084676D:
    goto loc_008459D8;
loc_00846777:
    local_r12 = 0;
    goto loc_00846788;
loc_00846780:
    local_r12 = 0;
loc_00846788:
    local_rdi = (uint32_t)(0xC0000425ULL);
    if (((*(uint8_t *)(local_r14 + 0x30)) & (1)) == 0) { local_rdi = (uint32_t)((uint32_t)(0xC000017CULL)); }
    goto loc_00846186;
loc_0084679A:
    result = CmpFreeValue(*(uint64_t *)(0 + 0x20), v_stack_m148, v_stack_m170, *(uint64_t *)(*(uint64_t *)((uint32_t)(Arg5) + 0xC0) + 0x18));
    goto loc_00845F28;
loc_008467A8:
    result = CmpRundownUnitOfWork(result, v_stack_m148, v_stack_m170, *(uint64_t *)(*(uint64_t *)((uint32_t)(Arg5) + 0xC0) + 0x18));
    result = ExFreePoolWithTag(v_stack_m140, (uint32_t)(0x77554D43ULL), v_stack_m170, *(uint64_t *)(*(uint64_t *)((uint32_t)(Arg5) + 0xC0) + 0x18));
    goto loc_00845F35;
loc_008467C3:
    result = HvFreeCell(*(uint64_t *)(0 + 0x20), (uint32_t)(0x77554D43ULL), v_stack_m170, *(uint64_t *)(*(uint64_t *)((uint32_t)(Arg5) + 0xC0) + 0x18));
    goto loc_008460BD;
loc_008467D1:
    result = HvUnlockHiveFlusherShared(*(uint64_t *)(0 + 0x20), (uint32_t)(0x77554D43ULL), v_stack_m170, *(uint64_t *)(*(uint64_t *)((uint32_t)(Arg5) + 0xC0) + 0x18));
    goto loc_00845F49;
loc_008467DF:
    result = CmpFreePoolWithTag(*(uint64_t *)(0 + 0x20), (uint32_t)(0x34414D43ULL), v_stack_m170, *(uint64_t *)(*(uint64_t *)((uint32_t)(Arg5) + 0xC0) + 0x18));
    goto loc_00845FB7;
loc_008467EE:
    result = CmpFreePoolWithTag((uint32_t)(v_stack_m168), (uint32_t)(0x33414D43ULL), v_stack_m170, *(uint64_t *)(*(uint64_t *)((uint32_t)(Arg5) + 0xC0) + 0x18));
    goto loc_00845FC0;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008457C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
