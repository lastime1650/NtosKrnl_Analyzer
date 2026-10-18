# CmDeleteKey

- RVA: `0x00848E5C`–`0x0084977A` (길이 `2,334` bytes)
- VA: `0x0000000140848E5C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000693E4`
- 디코드: `558`개 명령, `2,334/2,334` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **75**; 고유 호출 대상: **44**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00848F28` → [HvpGetCellContextInitialize](../85/HvpGetCellContextInitialize_function_00855F10.md) (function, `0x00855F10`)
- `0x00848F32` → [HvpGetCellContextInitialize](../85/HvpGetCellContextInitialize_function_00855F10.md) (function, `0x00855F10`)
- `0x00848F5A` → [CmpInitializeDelayDerefContext](../../text/42/CmpInitializeDelayDerefContext_function_0042A7F0.md) (function, `0x0042A7F0`)
- `0x00848F63` → [CmpAttachToRegistryProcess](../../pagecmrc/BC/CmpAttachToRegistryProcess_function_00BC98E0.md) (function, `0x00BC98E0`)
- `0x00848F6D` → [CmpIsShutdownRundownActive](../../pagecmrc/BC/CmpIsShutdownRundownActive_function_00BC9C20.md) (function, `0x00BC9C20`)
- `0x00848F83` → [CmpLockRegistry](../../pagecmrc/BC/CmpLockRegistry_function_00BC9B34.md) (function, `0x00BC9B34`)
- `0x00848FC4` → [CmpStartKcbStackForTopLayerKcb](CmpStartKcbStackForTopLayerKcb_function_00848390.md) (function, `0x00848390`)
- `0x00848FDC` → [CmpStartKcbStackForTopLayerKcb](CmpStartKcbStackForTopLayerKcb_function_00848390.md) (function, `0x00848390`)
- `0x00848FF5` → [CmpLockHashEntryExclusiveByKcb](CmpLockHashEntryExclusiveByKcb_function_00849780.md) (function, `0x00849780`)
- `0x00849004` → [CmpLockKcbStackTopExclusiveRestShared](CmpLockKcbStackTopExclusiveRestShared_function_00846B04.md) (function, `0x00846B04`)
- `0x00849041` → [CmpLockKcbExclusive](../86/CmpLockKcbExclusive_function_00861EB0.md) (function, `0x00861EB0`)
- `0x0084906B` → [CmpIsKeyDeletedForKeyBody](../../pagecmrc/BC/CmpIsKeyDeletedForKeyBody_function_00BC9480.md) (function, `0x00BC9480`)
- `0x0084908F` → [CmpTransSearchAddTransFromKeyBody](../87/CmpTransSearchAddTransFromKeyBody_function_008736B8.md) (function, `0x008736B8`)
- `0x008490BF` → [CmpIsKeyDeletedForKeyBody](../../pagecmrc/BC/CmpIsKeyDeletedForKeyBody_function_00BC9480.md) (function, `0x00BC9480`)
- `0x00849141` → [HvLockHiveFlusherShared](HvLockHiveFlusherShared_function_0084F95C.md) (function, `0x0084F95C`)
- `0x00849159` → [CmpGetKeyNodeForKcb](../85/CmpGetKeyNodeForKcb_function_00856480.md) (function, `0x00856480`)
- `0x0084916E` → [CmGetVisibleSubkeyCount](CmGetVisibleSubkeyCount_function_00849D74.md) (function, `0x00849D74`)
- `0x0084919D` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x008491FA` → [CmpReportNotifyHelper](../8C/CmpReportNotifyHelper_function_008C7230.md) (function, `0x008C7230`)
- `0x00849223` → [CmpReportNotifyHelper](../8C/CmpReportNotifyHelper_function_008C7230.md) (function, `0x008C7230`)
- `0x00849235` → [CmpFreeKeyByCell](CmpFreeKeyByCell_function_0084AD70.md) (function, `0x0084AD70`)
- `0x00849253` → [CmpFlushNotifiesOnKeyBodyList](../9B/CmpFlushNotifiesOnKeyBodyList_function_009B3594.md) (function, `0x009B3594`)
- `0x00849264` → [CmpCleanUpSubKeyInfo](CmpCleanUpSubKeyInfo_function_0084C6F4.md) (function, `0x0084C6F4`)
- `0x00849275` → [CmpGetKeyNodeForKcb](../85/CmpGetKeyNodeForKcb_function_00856480.md) (function, `0x00856480`)
- `0x008492BD` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x008492CA` → [CmpMarkKeyUnbacked](../9B/CmpMarkKeyUnbacked_function_009B3C4C.md) (function, `0x009B3C4C`)
- `0x008492D2` → [CmpDiscardKcb](../9B/CmpDiscardKcb_function_009B2F34.md) (function, `0x009B2F34`)
- `0x00849307` → [HvUnlockHiveFlusherShared](HvUnlockHiveFlusherShared_function_00848738.md) (function, `0x00848738`)
- `0x0084932F` → [CmpUnlockKcbStack](CmpUnlockKcbStack_function_00848460.md) (function, `0x00848460`)
- `0x00849339` → [CmpUnlockKcbStack](CmpUnlockKcbStack_function_00848460.md) (function, `0x00848460`)
- `0x00849348` → [CmpUnlockHashEntryByKcb](../86/CmpUnlockHashEntryByKcb_function_00864370.md) (function, `0x00864370`)
- `0x00849356` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (function, `0x00475D80`)
- `0x00849364` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (function, `0x00475D80`)
- `0x00849370` → [CmpDrainDelayDerefContext](../../text/41/CmpDrainDelayDerefContext_function_0041B9A0.md) (function, `0x0041B9A0`)
- `0x0084937A` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x00849383` → [CmpDetachFromRegistryProcess](../../pagecmrc/BC/CmpDetachFromRegistryProcess_function_00BC9920.md) (function, `0x00BC9920`)
- `0x00849396` → [CmpSignalDeferredPosts](CmpSignalDeferredPosts_function_008484B0.md) (function, `0x008484B0`)
- `0x008493A4` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x008493D5` → [CmpLockRegistryExclusive](CmpLockRegistryExclusive_function_0084F9B4.md) (function, `0x0084F9B4`)
- `0x008493E8` → [CmpSnapshotTxOwnerArray](CmpSnapshotTxOwnerArray_function_00846808.md) (function, `0x00846808`)
- `0x008493FF` → [CmpUnlockKcbStack](CmpUnlockKcbStack_function_00848460.md) (function, `0x00848460`)
- `0x00849409` → [CmpUnlockKcbStack](CmpUnlockKcbStack_function_00848460.md) (function, `0x00848460`)
- `0x0084941B` → [CmpUnlockHashEntryByKcb](../86/CmpUnlockHashEntryByKcb_function_00864370.md) (function, `0x00864370`)
- `0x0084942C` → [CmpDrainDelayDerefContext](../../text/41/CmpDrainDelayDerefContext_function_0041B9A0.md) (function, `0x0041B9A0`)
- `0x00849431` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x00849443` → [CmpRollbackTransactionArray](../94/CmpRollbackTransactionArray_function_0094B3AC.md) (function, `0x0094B3AC`)
- `0x0084946A` → [CmDeleteLayeredKey](../../text/41/CmDeleteLayeredKey_function_0041B598.md) (function, `0x0041B598`)
- `0x0084948F` → [CmpAllocateUnitOfWork](CmpAllocateUnitOfWork_function_00844BB0.md) (function, `0x00844BB0`)
- `0x008494A0` → [CmpAllocateUnitOfWork](CmpAllocateUnitOfWork_function_00844BB0.md) (function, `0x00844BB0`)
- `0x008494B8` → [CmpTransEnlistUowInKcb](../../text/48/CmpTransEnlistUowInKcb_function_0048F094.md) (function, `0x0048F094`)
- `0x008494C3` → [CmpTransEnlistUowInCmTrans](../../text/48/CmpTransEnlistUowInCmTrans_function_0048B330.md) (function, `0x0048B330`)
- `0x008494D8` → [CmpTransEnlistUowInKcb](../../text/48/CmpTransEnlistUowInKcb_function_0048F094.md) (function, `0x0048F094`)
- `0x008494E3` → [CmpTransEnlistUowInCmTrans](../../text/48/CmpTransEnlistUowInCmTrans_function_0048B330.md) (function, `0x0048B330`)
- `0x00849500` → [CmpLockIXLockIntent](CmpLockIXLockIntent_function_00844C08.md) (function, `0x00844C08`)
- `0x00849518` → [CmpLockIXLockExclusive](CmpLockIXLockExclusive_function_00844CB4.md) (function, `0x00844CB4`)
- `0x0084952F` → [CmpLockIXLockExclusive](CmpLockIXLockExclusive_function_00844CB4.md) (function, `0x00844CB4`)
- `0x00849563` → [HvUnlockHiveFlusherShared](HvUnlockHiveFlusherShared_function_00848738.md) (function, `0x00848738`)
- `0x00849575` → [CmAddLogForAction](CmAddLogForAction_function_008445AC.md) (function, `0x008445AC`)
- `0x008495C1` → [CmpReportNotifyHelper](../8C/CmpReportNotifyHelper_function_008C7230.md) (function, `0x008C7230`)
- `0x008495EC` → [CmpReportNotifyHelper](../8C/CmpReportNotifyHelper_function_008C7230.md) (function, `0x008C7230`)
- `0x00849608` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00849612` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00849631` → [CmpSnapshotTxOwnerArray](CmpSnapshotTxOwnerArray_function_00846808.md) (function, `0x00846808`)
- `0x0084964C` → [CmpUnlockKcbStack](CmpUnlockKcbStack_function_00848460.md) (function, `0x00848460`)
- `0x00849656` → [CmpUnlockKcbStack](CmpUnlockKcbStack_function_00848460.md) (function, `0x00848460`)
- `0x00849668` → [CmpUnlockHashEntryByKcb](../86/CmpUnlockHashEntryByKcb_function_00864370.md) (function, `0x00864370`)
- `0x00849679` → [CmpDrainDelayDerefContext](../../text/41/CmpDrainDelayDerefContext_function_0041B9A0.md) (function, `0x0041B9A0`)
- `0x0084967E` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x00849690` → [CmpRollbackTransactionArray](../94/CmpRollbackTransactionArray_function_0094B3AC.md) (function, `0x0094B3AC`)
- `0x008496F6` → [CmEqualTrans](CmEqualTrans_function_0084BF60.md) (function, `0x0084BF60`)
- `0x00849742` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x0084974F` → [CmpRundownUnitOfWork](../87/CmpRundownUnitOfWork_function_0087497C.md) (function, `0x0087497C`)
- `0x00849759` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00849766` → [CmpRundownUnitOfWork](../87/CmpRundownUnitOfWork_function_0087497C.md) (function, `0x0087497C`)
- `0x00849770` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [NtDeleteKey](NtDeleteKey_function_00849920.md) at `0x00849B7A`

### Static image references
- `0x00848E7F` → RVA `0x00E0A740` (`.data`; read)
- `0x008491FF` → RVA `0x00FD9A90` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **23**
  - `0x00848F5A` → [CmpInitializeDelayDerefContext](../../text/42/CmpInitializeDelayDerefContext_function_0042A7F0.md) (`PAGE` → `.text`)
  - `0x00848F63` → [CmpAttachToRegistryProcess](../../pagecmrc/BC/CmpAttachToRegistryProcess_function_00BC98E0.md) (`PAGE` → `PAGECMRC`)
  - `0x00848F6D` → [CmpIsShutdownRundownActive](../../pagecmrc/BC/CmpIsShutdownRundownActive_function_00BC9C20.md) (`PAGE` → `PAGECMRC`)
  - `0x00848F83` → [CmpLockRegistry](../../pagecmrc/BC/CmpLockRegistry_function_00BC9B34.md) (`PAGE` → `PAGECMRC`)
  - `0x0084906B` → [CmpIsKeyDeletedForKeyBody](../../pagecmrc/BC/CmpIsKeyDeletedForKeyBody_function_00BC9480.md) (`PAGE` → `PAGECMRC`)
  - `0x008490BF` → [CmpIsKeyDeletedForKeyBody](../../pagecmrc/BC/CmpIsKeyDeletedForKeyBody_function_00BC9480.md) (`PAGE` → `PAGECMRC`)
  - `0x00849356` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (`PAGE` → `.text`)
  - `0x00849364` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (`PAGE` → `.text`)
  - `0x00849370` → [CmpDrainDelayDerefContext](../../text/41/CmpDrainDelayDerefContext_function_0041B9A0.md) (`PAGE` → `.text`)
  - `0x0084937A` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x00849383` → [CmpDetachFromRegistryProcess](../../pagecmrc/BC/CmpDetachFromRegistryProcess_function_00BC9920.md) (`PAGE` → `PAGECMRC`)
  - `0x008493A4` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x0084942C` → [CmpDrainDelayDerefContext](../../text/41/CmpDrainDelayDerefContext_function_0041B9A0.md) (`PAGE` → `.text`)
  - `0x00849431` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x0084946A` → [CmDeleteLayeredKey](../../text/41/CmDeleteLayeredKey_function_0041B598.md) (`PAGE` → `.text`)
  - `0x008494B8` → [CmpTransEnlistUowInKcb](../../text/48/CmpTransEnlistUowInKcb_function_0048F094.md) (`PAGE` → `.text`)
  - `0x008494C3` → [CmpTransEnlistUowInCmTrans](../../text/48/CmpTransEnlistUowInCmTrans_function_0048B330.md) (`PAGE` → `.text`)
  - `0x008494D8` → [CmpTransEnlistUowInKcb](../../text/48/CmpTransEnlistUowInKcb_function_0048F094.md) (`PAGE` → `.text`)
  - `0x008494E3` → [CmpTransEnlistUowInCmTrans](../../text/48/CmpTransEnlistUowInCmTrans_function_0048B330.md) (`PAGE` → `.text`)
  - `0x00849679` → [CmpDrainDelayDerefContext](../../text/41/CmpDrainDelayDerefContext_function_0041B9A0.md) (`PAGE` → `.text`)
  - `0x0084967E` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x00849759` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00849770` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **4**
  - `0x008490DD` → [sub_00B16440](../B1/Unknown_function_00B16440.md) (`tail-transfer`)
  - `0x008491BB` → [sub_00B16440 + 0x97](../B1/Unknown_function_00B16440.md) (`tail-transfer`)
  - `0x008492EB` → [sub_00B16440 + 0x19F](../B1/Unknown_function_00B16440.md) (`tail-transfer`)
  - `0x0084973C` → [sub_00B16440 + 0x1FE](../B1/Unknown_function_00B16440.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00848E5C  48 8B C4                        mov rax, rsp
00848E5F  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00848E63  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
00848E67  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
00848E6B  55                              push rbp
00848E6C  41 54                           push r12
00848E6E  41 55                           push r13
00848E70  41 56                           push r14
00848E72  41 57                           push r15
00848E74  48 8D 68 88                     lea rbp, [rax - 0x78]
00848E78  48 81 EC 50 01 00 00            sub rsp, 0x150
00848E7F  48 8B 05 BA 18 5C 00            mov rax, qword ptr [rip + 0x5c18ba]
00848E86  48 33 C4                        xor rax, rsp
00848E89  48 89 45 40                     mov qword ptr [rbp + 0x40], rax
00848E8D  33 FF                           xor edi, edi
00848E8F  48 89 4D 08                     mov qword ptr [rbp + 8], rcx
00848E93  0F 57 C0                        xorps xmm0, xmm0
00848E96  48 89 7D 98                     mov qword ptr [rbp - 0x68], rdi
00848E9A  48 8D 45 A0                     lea rax, [rbp - 0x60]
00848E9E  48 89 7C 24 58                  mov qword ptr [rsp + 0x58], rdi
00848EA3  48 89 45 A8                     mov qword ptr [rbp - 0x58], rax
00848EA7  4C 8B F1                        mov r14, rcx
00848EAA  48 8D 45 A0                     lea rax, [rbp - 0x60]
00848EAE  48 89 7D 90                     mov qword ptr [rbp - 0x70], rdi
00848EB2  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
00848EB6  48 8D 4D 98                     lea rcx, [rbp - 0x68]
00848EBA  83 C8 FF                        or eax, 0xffffffff
00848EBD  89 7C 24 44                     mov dword ptr [rsp + 0x44], edi
00848EC1  0F 11 45 10                     movups xmmword ptr [rbp + 0x10], xmm0
00848EC5  48 BB 14 00 00 00 80 F7 FF FF   movabs rbx, 0xfffff78000000014
00848ECF  44 8A FF                        mov r15b, dil
00848ED2  0F 11 45 20                     movups xmmword ptr [rbp + 0x20], xmm0
00848ED6  40 88 7C 24 42                  mov byte ptr [rsp + 0x42], dil
00848EDB  44 8A E7                        mov r12b, dil
00848EDE  0F 11 45 30                     movups xmmword ptr [rbp + 0x30], xmm0
00848EE2  40 88 7C 24 41                  mov byte ptr [rsp + 0x41], dil
00848EE7  44 8B EF                        mov r13d, edi
00848EEA  0F 11 44 24 60                  movups xmmword ptr [rsp + 0x60], xmm0
00848EEF  48 8B 1B                        mov rbx, qword ptr [rbx]
00848EF2  8B F7                           mov esi, edi
00848EF4  0F 11 44 24 70                  movups xmmword ptr [rsp + 0x70], xmm0
00848EF9  66 89 44 24 72                  mov word ptr [rsp + 0x72], ax
00848EFE  0F 11 45 B8                     movups xmmword ptr [rbp - 0x48], xmm0
00848F02  66 89 45 BA                     mov word ptr [rbp - 0x46], ax
00848F06  40 88 7C 24 43                  mov byte ptr [rsp + 0x43], dil
00848F0B  0F 11 45 80                     movups xmmword ptr [rbp - 0x80], xmm0
00848F0F  48 89 7D B0                     mov qword ptr [rbp - 0x50], rdi
00848F13  0F 11 45 C8                     movups xmmword ptr [rbp - 0x38], xmm0
00848F17  89 7C 24 50                     mov dword ptr [rsp + 0x50], edi
00848F1B  48 89 7C 24 48                  mov qword ptr [rsp + 0x48], rdi
00848F20  48 89 7D 00                     mov qword ptr [rbp], rdi
00848F24  48 89 7D F8                     mov qword ptr [rbp - 8], rdi
00848F28  E8 E3 CF 00 00                  call 0x140855f10
00848F2D  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
00848F32  E8 D9 CF 00 00                  call 0x140855f10
00848F37  48 8D 45 E8                     lea rax, [rbp - 0x18]
00848F3B  48 89 7D D8                     mov qword ptr [rbp - 0x28], rdi
00848F3F  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00848F43  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
00848F48  48 8D 45 E8                     lea rax, [rbp - 0x18]
00848F4C  89 7D E4                        mov dword ptr [rbp - 0x1c], edi
00848F4F  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
00848F53  C7 45 E0 01 00 00 C0            mov dword ptr [rbp - 0x20], 0xc0000001
00848F5A  E8 91 18 BE FF                  call 0x14042a7f0
00848F5F  48 8D 4D 10                     lea rcx, [rbp + 0x10]
00848F63  E8 78 09 38 00                  call 0x140bc98e0
00848F68  BA 01 00 00 00                  mov edx, 1
00848F6D  E8 AE 0C 38 00                  call 0x140bc9c20
00848F72  84 C0                           test al, al
00848F74  0F 85 7C 06 00 00               jne 0x1408495f6
00848F7A  45 84 FF                        test r15b, r15b
00848F7D  0F 85 52 04 00 00               jne 0x1408493d5
00848F83  E8 AC 0B 38 00                  call 0x140bc9b34
00848F88  49 8B 76 08                     mov rsi, qword ptr [r14 + 8]
00848F8C  BA 01 00 00 00                  mov edx, 1
00848F91  88 54 24 40                     mov byte ptr [rsp + 0x40], dl
00848F95  48 8B 46 20                     mov rax, qword ptr [rsi + 0x20]
00848F99  F7 80 A0 00 00 00 00 00 10 00   test dword ptr [rax + 0xa0], 0x100000
00848FA3  0F 85 DC 04 00 00               jne 0x140849485
00848FA9  48 39 7E 48                     cmp qword ptr [rsi + 0x48], rdi
00848FAD  0F 84 6C 07 00 00               je 0x14084971f
00848FB3  66 39 7E 42                     cmp word ptr [rsi + 0x42], di
00848FB7  0F 85 A1 04 00 00               jne 0x14084945e
00848FBD  48 8B D6                        mov rdx, rsi
00848FC0  48 8D 4D B8                     lea rcx, [rbp - 0x48]
00848FC4  E8 C7 F3 FF FF                  call 0x140848390
00848FC9  8B F8                           mov edi, eax
00848FCB  85 C0                           test eax, eax
00848FCD  0F 88 9E 04 00 00               js 0x140849471
00848FD3  48 8B 56 48                     mov rdx, qword ptr [rsi + 0x48]
00848FD7  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
00848FDC  E8 AF F3 FF FF                  call 0x140848390
00848FE1  8B F8                           mov edi, eax
00848FE3  85 C0                           test eax, eax
00848FE5  0F 88 86 04 00 00               js 0x140849471
00848FEB  33 FF                           xor edi, edi
00848FED  45 84 FF                        test r15b, r15b
00848FF0  75 74                           jne 0x140849066
00848FF2  48 8B CE                        mov rcx, rsi
00848FF5  E8 86 07 00 00                  call 0x140849780
00848FFA  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
00848FFF  C6 44 24 41 01                  mov byte ptr [rsp + 0x41], 1
00849004  E8 FB DA FF FF                  call 0x140846b04
00849009  44 0F B7 65 BA                  movzx r12d, word ptr [rbp - 0x46]
0084900E  44 0F B7 F7                     movzx r14d, di
00849012  66 41 3B FC                     cmp di, r12w
00849016  0F 8F AF 03 00 00               jg 0x1408493cb
0084901C  4C 8B 7D D0                     mov r15, qword ptr [rbp - 0x30]
00849020  48 8D 45 C0                     lea rax, [rbp - 0x40]
00849024  4C 2B F8                        sub r15, rax
00849027  48 8D 7D C0                     lea rdi, [rbp - 0x40]
0084902B  41 BD 02 00 00 00               mov r13d, 2
00849031  66 45 3B F5                     cmp r14w, r13w
00849035  0F 8D E1 05 00 00               jge 0x14084961c
0084903B  48 8B CF                        mov rcx, rdi
0084903E  48 8B 09                        mov rcx, qword ptr [rcx]
00849041  E8 6A 8E 01 00                  call 0x140861eb0
00849046  B8 01 00 00 00                  mov eax, 1
0084904B  48 83 C7 08                     add rdi, 8
0084904F  66 44 03 F0                     add r14w, ax
00849053  66 45 3B F4                     cmp r14w, r12w
00849057  7E D8                           jle 0x140849031
00849059  4C 8B 6D 00                     mov r13, qword ptr [rbp]
0084905D  33 FF                           xor edi, edi
0084905F  4C 8B 75 08                     mov r14, qword ptr [rbp + 8]
00849063  44 8A E0                        mov r12b, al
00849066  33 D2                           xor edx, edx
00849068  49 8B CE                        mov rcx, r14
0084906B  E8 10 04 38 00                  call 0x140bc9480
00849070  84 C0                           test al, al
00849072  0F 85 F9 03 00 00               jne 0x140849471
00849078  49 39 7E 38                     cmp qword ptr [r14 + 0x38], rdi
0084907C  75 0A                           jne 0x140849088
0084907E  49 39 7E 40                     cmp qword ptr [r14 + 0x40], rdi
00849082  0F 84 62 06 00 00               je 0x1408496ea
00849088  48 8D 55 B0                     lea rdx, [rbp - 0x50]
0084908C  49 8B CE                        mov rcx, r14
0084908F  E8 24 A6 02 00                  call 0x1408736b8
00849094  8B F8                           mov edi, eax
00849096  85 C0                           test eax, eax
00849098  0F 88 D3 03 00 00               js 0x140849471
0084909E  48 8B 46 20                     mov rax, qword ptr [rsi + 0x20]
008490A2  8B 88 A0 00 00 00               mov ecx, dword ptr [rax + 0xa0]
008490A8  B8 02 00 00 00                  mov eax, 2
008490AD  84 C8                           test al, cl
008490AF  0F 85 60 06 00 00               jne 0x140849715
008490B5  4C 8B 7D B0                     mov r15, qword ptr [rbp - 0x50]
008490B9  49 8B CE                        mov rcx, r14
008490BC  49 8B D7                        mov rdx, r15
008490BF  E8 BC 03 38 00                  call 0x140bc9480
008490C4  33 FF                           xor edi, edi
008490C6  84 C0                           test al, al
008490C8  0F 85 3F 06 00 00               jne 0x14084970d
008490CE  4D 85 FF                        test r15, r15
008490D1  75 10                           jne 0x1408490e3
008490D3  48 8B 86 C0 00 00 00            mov rax, qword ptr [rsi + 0xc0]
008490DA  48 85 C0                        test rax, rax
008490DD  0F 85 5D D3 2C 00               jne 0x140b16440
008490E3  48 8B 96 F0 00 00 00            mov rdx, qword ptr [rsi + 0xf0]
008490EA  48 85 D2                        test rdx, rdx
008490ED  0F 85 00 06 00 00               jne 0x1408496f3
008490F3  4D 85 FF                        test r15, r15
008490F6  0F 85 93 03 00 00               jne 0x14084948f
008490FC  48 8B 4E 48                     mov rcx, qword ptr [rsi + 0x48]
00849100  48 81 C1 F8 00 00 00            add rcx, 0xf8
00849107  39 39                           cmp dword ptr [rcx], edi
00849109  0F 8C D0 02 00 00               jl 0x1408493df
0084910F  48 8D 8E F8 00 00 00            lea rcx, [rsi + 0xf8]
00849116  39 39                           cmp dword ptr [rcx], edi
00849118  0F 85 0A 05 00 00               jne 0x140849628
0084911E  48 8D 8E 08 01 00 00            lea rcx, [rsi + 0x108]
00849125  39 39                           cmp dword ptr [rcx], edi
00849127  0F 85 FB 04 00 00               jne 0x140849628
0084912D  4C 8B 74 24 48                  mov r14, qword ptr [rsp + 0x48]
00849132  40 38 7C 24 42                  cmp byte ptr [rsp + 0x42], dil
00849137  0F 85 A3 05 00 00               jne 0x1408496e0
0084913D  48 8B 4E 20                     mov rcx, qword ptr [rsi + 0x20]
00849141  E8 16 68 00 00                  call 0x14084f95c
00849146  B8 01 00 00 00                  mov eax, 1
0084914B  88 44 24 43                     mov byte ptr [rsp + 0x43], al
0084914F  44 8A C0                        mov r8b, al
00849152  48 8D 55 98                     lea rdx, [rbp - 0x68]
00849156  48 8B CE                        mov rcx, rsi
00849159  E8 22 D3 00 00                  call 0x140856480
0084915E  4D 8B C7                        mov r8, r15
00849161  48 89 45 F8                     mov qword ptr [rbp - 8], rax
00849165  48 8B D0                        mov rdx, rax
00849168  48 8B CE                        mov rcx, rsi
0084916B  48 8B F8                        mov rdi, rax
0084916E  E8 01 0C 00 00                  call 0x140849d74
00849173  85 C0                           test eax, eax
00849175  0F 85 3D 05 00 00               jne 0x1408496b8
0084917B  F6 47 02 08                     test byte ptr [rdi + 2], 8
0084917F  0F 85 33 05 00 00               jne 0x1408496b8
00849185  48 8B 4E 20                     mov rcx, qword ptr [rsi + 0x20]
00849189  8D 78 01                        lea edi, [rax + 1]
0084918C  48 8D 55 98                     lea rdx, [rbp - 0x68]
00849190  40 84 B9 8C 00 00 00            test byte ptr [rcx + 0x8c], dil
00849197  0F 85 6B 04 00 00               jne 0x140849608
0084919D  E8 9E CD 00 00                  call 0x140855f40
008491A2  33 C0                           xor eax, eax
008491A4  48 89 45 F8                     mov qword ptr [rbp - 8], rax
008491A8  4D 85 FF                        test r15, r15
008491AB  0F 85 95 03 00 00               jne 0x140849546
008491B1  48 8B 86 C0 00 00 00            mov rax, qword ptr [rsi + 0xc0]
008491B8  48 85 C0                        test rax, rax
008491BB  0F 85 16 D3 2C 00               jne 0x140b164d7
008491C1  B8 02 00 00 00                  mov eax, 2
008491C6  66 39 44 24 72                  cmp word ptr [rsp + 0x72], ax
008491CB  0F AE E8                        lfence
008491CE  0F 8D D0 04 00 00               jge 0x1408496a4
008491D4  48 0F BF 44 24 72               movsx rax, word ptr [rsp + 0x72]
008491DA  48 8B 7C C4 78                  mov rdi, qword ptr [rsp + rax*8 + 0x78]
008491DF  48 8B 57 20                     mov rdx, qword ptr [rdi + 0x20]
008491E3  48 8D 45 A0                     lea rax, [rbp - 0x60]
008491E7  41 B9 01 00 00 00               mov r9d, 1
008491ED  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008491F2  45 33 C0                        xor r8d, r8d
008491F5  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
008491FA  E8 31 E0 07 00                  call 0x1408c7230
008491FF  48 8B 15 8A 08 79 00            mov rdx, qword ptr [rip + 0x79088a]
00849206  48 39 57 20                     cmp qword ptr [rdi + 0x20], rdx
0084920A  74 1C                           je 0x140849228
0084920C  48 8D 45 A0                     lea rax, [rbp - 0x60]
00849210  41 B9 01 00 00 00               mov r9d, 1
00849216  45 33 C0                        xor r8d, r8d
00849219  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0084921E  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
00849223  E8 08 E0 07 00                  call 0x1408c7230
00849228  8B 56 28                        mov edx, dword ptr [rsi + 0x28]
0084922B  41 B8 01 00 00 00               mov r8d, 1
00849231  48 8B 4E 20                     mov rcx, qword ptr [rsi + 0x20]
00849235  E8 36 1B 00 00                  call 0x14084ad70
0084923A  8B F8                           mov edi, eax
0084923C  85 C0                           test eax, eax
0084923E  0F 88 96 00 00 00               js 0x1408492da
00849244  45 33 C9                        xor r9d, r9d
00849247  4C 8D 44 24 60                  lea r8, [rsp + 0x60]
0084924C  48 8B CE                        mov rcx, rsi
0084924F  41 8D 51 08                     lea edx, [r9 + 8]
00849253  E8 3C A3 16 00                  call 0x1409b3594
00849258  48 8B 4E 48                     mov rcx, qword ptr [rsi + 0x48]
0084925C  BF 01 00 00 00                  mov edi, 1
00849261  40 8A D7                        mov dl, dil
00849264  E8 8B 34 00 00                  call 0x14084c6f4
00849269  48 8B 4E 48                     mov rcx, qword ptr [rsi + 0x48]
0084926D  48 8D 54 24 58                  lea rdx, [rsp + 0x58]
00849272  44 8A C7                        mov r8b, dil
00849275  E8 06 D2 00 00                  call 0x140856480
0084927A  48 8B 56 48                     mov rdx, qword ptr [rsi + 0x48]
0084927E  0F B7 48 34                     movzx ecx, word ptr [rax + 0x34]
00849282  66 89 8A B0 00 00 00            mov word ptr [rdx + 0xb0], cx
00849289  48 8D 54 24 58                  lea rdx, [rsp + 0x58]
0084928E  48 8B 4E 48                     mov rcx, qword ptr [rsi + 0x48]
00849292  48 01 B9 30 01 00 00            add qword ptr [rcx + 0x130], rdi
00849299  48 89 58 04                     mov qword ptr [rax + 4], rbx
0084929D  48 8B 46 48                     mov rax, qword ptr [rsi + 0x48]
008492A1  48 89 98 A8 00 00 00            mov qword ptr [rax + 0xa8], rbx
008492A8  48 8B 46 48                     mov rax, qword ptr [rsi + 0x48]
008492AC  48 8B 48 20                     mov rcx, qword ptr [rax + 0x20]
008492B0  40 84 B9 8C 00 00 00            test byte ptr [rcx + 0x8c], dil
008492B7  0F 85 55 03 00 00               jne 0x140849612
008492BD  E8 7E CC 00 00                  call 0x140855f40
008492C2  48 8D 54 24 60                  lea rdx, [rsp + 0x60]
008492C7  48 8B CE                        mov rcx, rsi
008492CA  E8 7D A9 16 00                  call 0x1409b3c4c
008492CF  48 8B CE                        mov rcx, rsi
008492D2  E8 5D 9C 16 00                  call 0x1409b2f34
008492D7  41 8B FF                        mov edi, r15d
008492DA  44 8A 7C 24 40                  mov r15b, byte ptr [rsp + 0x40]
008492DF  BA 01 00 00 00                  mov edx, 1
008492E4  48 8B 4D D8                     mov rcx, qword ptr [rbp - 0x28]
008492E8  48 85 C9                        test rcx, rcx
008492EB  0F 85 EE D2 2C 00               jne 0x140b165df
008492F1  48 83 7D F8 00                  cmp qword ptr [rbp - 8], 0
008492F6  0F 85 2D 04 00 00               jne 0x140849729
008492FC  80 7C 24 43 00                  cmp byte ptr [rsp + 0x43], 0
00849301  74 09                           je 0x14084930c
00849303  48 8B 4E 20                     mov rcx, qword ptr [rsi + 0x20]
00849307  E8 2C F4 FF FF                  call 0x140848738
0084930C  BB 43 4D 55 77                  mov ebx, 0x77554d43
00849311  4D 85 ED                        test r13, r13
00849314  0F 85 32 04 00 00               jne 0x14084974c
0084931A  45 33 ED                        xor r13d, r13d
0084931D  4D 85 F6                        test r14, r14
00849320  0F 85 3D 04 00 00               jne 0x140849763
00849326  45 84 E4                        test r12b, r12b
00849329  74 13                           je 0x14084933e
0084932B  48 8D 4D B8                     lea rcx, [rbp - 0x48]
0084932F  E8 2C F1 FF FF                  call 0x140848460
00849334  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
00849339  E8 22 F1 FF FF                  call 0x140848460
0084933E  44 38 6C 24 41                  cmp byte ptr [rsp + 0x41], r13b
00849343  74 08                           je 0x14084934d
00849345  48 8B CE                        mov rcx, rsi
00849348  E8 23 B0 01 00                  call 0x140864370
0084934D  48 8B 4D D0                     mov rcx, qword ptr [rbp - 0x30]
00849351  48 85 C9                        test rcx, rcx
00849354  74 05                           je 0x14084935b
00849356  E8 25 CA C2 FF                  call 0x140475d80
0084935B  48 8B 4D 88                     mov rcx, qword ptr [rbp - 0x78]
0084935F  48 85 C9                        test rcx, rcx
00849362  74 05                           je 0x140849369
00849364  E8 17 CA C2 FF                  call 0x140475d80
00849369  33 D2                           xor edx, edx
0084936B  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
00849370  E8 2B 26 BD FF                  call 0x14041b9a0
00849375  45 84 FF                        test r15b, r15b
00849378  74 05                           je 0x14084937f
0084937A  E8 05 07 38 00                  call 0x140bc9a84
0084937F  48 8D 4D 10                     lea rcx, [rbp + 0x10]
00849383  E8 98 05 38 00                  call 0x140bc9920
00849388  48 8D 45 A0                     lea rax, [rbp - 0x60]
0084938C  48 39 45 A0                     cmp qword ptr [rbp - 0x60], rax
00849390  74 09                           je 0x14084939b
00849392  48 8D 4D A0                     lea rcx, [rbp - 0x60]
00849396  E8 15 F1 FF FF                  call 0x1408484b0
0084939B  8B C7                           mov eax, edi
0084939D  48 8B 4D 40                     mov rcx, qword ptr [rbp + 0x40]
008493A1  48 33 CC                        xor rcx, rsp
008493A4  E8 97 32 E6 FF                  call 0x1406ac640
008493A9  4C 8D 9C 24 50 01 00 00         lea r11, [rsp + 0x150]
008493B1  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
008493B5  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
008493B9  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
008493BD  49 8B E3                        mov rsp, r11
008493C0  41 5F                           pop r15
008493C2  41 5E                           pop r14
008493C4  41 5D                           pop r13
008493C6  41 5C                           pop r12
008493C8  5D                              pop rbp
008493C9  C3                              ret
008493CA  CC                              int3
008493CB  B8 01 00 00 00                  mov eax, 1
008493D0  E9 8A FC FF FF                  jmp 0x14084905f
008493D5  E8 DA 65 00 00                  call 0x14084f9b4
008493DA  E9 A9 FB FF FF                  jmp 0x140848f88
008493DF  4C 8D 45 90                     lea r8, [rbp - 0x70]
008493E3  48 8D 54 24 44                  lea rdx, [rsp + 0x44]
008493E8  E8 1B D4 FF FF                  call 0x140846808
008493ED  45 33 FF                        xor r15d, r15d
008493F0  8B F8                           mov edi, eax
008493F2  85 C0                           test eax, eax
008493F4  78 7B                           js 0x140849471
008493F6  45 84 E4                        test r12b, r12b
008493F9  74 16                           je 0x140849411
008493FB  48 8D 4D B8                     lea rcx, [rbp - 0x48]
008493FF  E8 5C F0 FF FF                  call 0x140848460
00849404  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
00849409  E8 52 F0 FF FF                  call 0x140848460
0084940E  45 8A E7                        mov r12b, r15b
00849411  44 38 7C 24 41                  cmp byte ptr [rsp + 0x41], r15b
00849416  74 0D                           je 0x140849425
00849418  48 8B CE                        mov rcx, rsi
0084941B  E8 50 AF 01 00                  call 0x140864370
00849420  44 88 7C 24 41                  mov byte ptr [rsp + 0x41], r15b
00849425  33 D2                           xor edx, edx
00849427  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
0084942C  E8 6F 25 BD FF                  call 0x14041b9a0
00849431  E8 4E 06 38 00                  call 0x140bc9a84
00849436  48 8B 55 90                     mov rdx, qword ptr [rbp - 0x70]
0084943A  4C 8D 4C 24 50                  lea r9, [rsp + 0x50]
0084943F  8B 4C 24 44                     mov ecx, dword ptr [rsp + 0x44]
00849443  E8 64 1F 10 00                  call 0x14094b3ac
00849448  8B F8                           mov edi, eax
0084944A  85 C0                           test eax, eax
0084944C  0F 88 B1 01 00 00               js 0x140849603
00849452  44 8A 7C 24 42                  mov r15b, byte ptr [rsp + 0x42]
00849457  33 FF                           xor edi, edi
00849459  E9 0A FB FF FF                  jmp 0x140848f68
0084945E  4C 8D 44 24 60                  lea r8, [rsp + 0x60]
00849463  49 8B CE                        mov rcx, r14
00849466  48 8D 55 A0                     lea rdx, [rbp - 0x60]
0084946A  E8 29 21 BD FF                  call 0x14041b598
0084946F  8B F8                           mov edi, eax
00849471  44 8A 7C 24 40                  mov r15b, byte ptr [rsp + 0x40]
00849476  BA 01 00 00 00                  mov edx, 1
0084947B  4C 8B 74 24 48                  mov r14, qword ptr [rsp + 0x48]
00849480  E9 5F FE FF FF                  jmp 0x1408492e4
00849485  BF 22 00 00 C0                  mov edi, 0xc0000022
0084948A  44 8A FA                        mov r15b, dl
0084948D  EB EC                           jmp 0x14084947b
0084948F  E8 1C B7 FF FF                  call 0x140844bb0
00849494  4C 8B F0                        mov r14, rax
00849497  48 85 C0                        test rax, rax
0084949A  0F 84 22 02 00 00               je 0x1408496c2
008494A0  E8 0B B7 FF FF                  call 0x140844bb0
008494A5  4C 8B E8                        mov r13, rax
008494A8  48 85 C0                        test rax, rax
008494AB  0F 84 11 02 00 00               je 0x1408496c2
008494B1  48 8B 56 48                     mov rdx, qword ptr [rsi + 0x48]
008494B5  49 8B CE                        mov rcx, r14
008494B8  E8 D7 5B C4 FF                  call 0x14048f094
008494BD  49 8B D7                        mov rdx, r15
008494C0  49 8B CE                        mov rcx, r14
008494C3  E8 68 1E C4 FF                  call 0x14048b330
008494C8  8B F8                           mov edi, eax
008494CA  85 C0                           test eax, eax
008494CC  0F 88 08 FE FF FF               js 0x1408492da
008494D2  48 8B D6                        mov rdx, rsi
008494D5  49 8B CD                        mov rcx, r13
008494D8  E8 B7 5B C4 FF                  call 0x14048f094
008494DD  49 8B D7                        mov rdx, r15
008494E0  49 8B CD                        mov rcx, r13
008494E3  E8 48 1E C4 FF                  call 0x14048b330
008494E8  8B F8                           mov edi, eax
008494EA  85 C0                           test eax, eax
008494EC  0F 88 E8 FD FF FF               js 0x1408492da
008494F2  48 8B 4E 48                     mov rcx, qword ptr [rsi + 0x48]
008494F6  49 8B D6                        mov rdx, r14
008494F9  48 81 C1 F8 00 00 00            add rcx, 0xf8
00849500  E8 03 B7 FF FF                  call 0x140844c08
00849505  33 FF                           xor edi, edi
00849507  84 C0                           test al, al
00849509  74 31                           je 0x14084953c
0084950B  48 8D 8E F8 00 00 00            lea rcx, [rsi + 0xf8]
00849512  45 33 C0                        xor r8d, r8d
00849515  49 8B D5                        mov rdx, r13
00849518  E8 97 B7 FF FF                  call 0x140844cb4
0084951D  84 C0                           test al, al
0084951F  74 1B                           je 0x14084953c
00849521  48 8D 8E 08 01 00 00            lea rcx, [rsi + 0x108]
00849528  49 8B D5                        mov rdx, r13
0084952B  44 8D 47 01                     lea r8d, [rdi + 1]
0084952F  E8 80 B7 FF FF                  call 0x140844cb4
00849534  84 C0                           test al, al
00849536  0F 85 F6 FB FF FF               jne 0x140849132
0084953C  BF 01 00 19 C0                  mov edi, 0xc0190001
00849541  E9 94 FD FF FF                  jmp 0x1408492da
00849546  41 C7 46 44 03 00 00 00         mov dword ptr [r14 + 0x44], 3
0084954E  BB 02 00 00 00                  mov ebx, 2
00849553  49 89 76 58                     mov qword ptr [r14 + 0x58], rsi
00849557  41 89 5D 44                     mov dword ptr [r13 + 0x44], ebx
0084955B  4D 89 75 50                     mov qword ptr [r13 + 0x50], r14
0084955F  48 8B 4E 20                     mov rcx, qword ptr [rsi + 0x20]
00849563  E8 D0 F1 FF FF                  call 0x140848738
00849568  45 33 FF                        xor r15d, r15d
0084956B  8B D7                           mov edx, edi
0084956D  49 8B CD                        mov rcx, r13
00849570  44 88 7C 24 43                  mov byte ptr [rsp + 0x43], r15b
00849575  E8 32 B0 FF FF                  call 0x1408445ac
0084957A  8B F8                           mov edi, eax
0084957C  85 C0                           test eax, eax
0084957E  0F 88 56 FD FF FF               js 0x1408492da
00849584  66 39 5C 24 72                  cmp word ptr [rsp + 0x72], bx
00849589  45 8B EF                        mov r13d, r15d
0084958C  45 8B F7                        mov r14d, r15d
0084958F  0F AE E8                        lfence
00849592  0F 8D 34 01 00 00               jge 0x1408496cc
00849598  48 0F BF 44 24 72               movsx rax, word ptr [rsp + 0x72]
0084959E  48 8B 5C C4 78                  mov rbx, qword ptr [rsp + rax*8 + 0x78]
008495A3  4C 8B 45 B0                     mov r8, qword ptr [rbp - 0x50]
008495A7  48 8D 45 A0                     lea rax, [rbp - 0x60]
008495AB  48 8B 53 20                     mov rdx, qword ptr [rbx + 0x20]
008495AF  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
008495B4  BF 01 00 00 00                  mov edi, 1
008495B9  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008495BE  44 8B CF                        mov r9d, edi
008495C1  E8 6A DC 07 00                  call 0x1408c7230
008495C6  48 8B 15 C3 04 79 00            mov rdx, qword ptr [rip + 0x7904c3]
008495CD  48 39 53 20                     cmp qword ptr [rbx + 0x20], rdx
008495D1  0F 84 00 FD FF FF               je 0x1408492d7
008495D7  4C 8B 45 B0                     mov r8, qword ptr [rbp - 0x50]
008495DB  48 8D 45 A0                     lea rax, [rbp - 0x60]
008495DF  44 8B CF                        mov r9d, edi
008495E2  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008495E7  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
008495EC  E8 3F DC 07 00                  call 0x1408c7230
008495F1  E9 E1 FC FF FF                  jmp 0x1408492d7
008495F6  BF 89 01 00 C0                  mov edi, 0xc0000189
008495FB  45 32 FF                        xor r15b, r15b
008495FE  E9 78 FE FF FF                  jmp 0x14084947b
00849603  E9 6E FE FF FF                  jmp 0x140849476
00849608  E8 13 36 01 00                  call 0x14085cc20
0084960D  E9 90 FB FF FF                  jmp 0x1408491a2
00849612  E8 09 36 01 00                  call 0x14085cc20
00849617  E9 A6 FC FF FF                  jmp 0x1408492c2
0084961C  49 8D 4F F0                     lea rcx, [r15 - 0x10]
00849620  48 03 CF                        add rcx, rdi
00849623  E9 16 FA FF FF                  jmp 0x14084903e
00849628  4C 8D 45 90                     lea r8, [rbp - 0x70]
0084962C  48 8D 54 24 44                  lea rdx, [rsp + 0x44]
00849631  E8 D2 D1 FF FF                  call 0x140846808
00849636  45 33 FF                        xor r15d, r15d
00849639  8B F8                           mov edi, eax
0084963B  85 C0                           test eax, eax
0084963D  0F 88 2E FE FF FF               js 0x140849471
00849643  45 84 E4                        test r12b, r12b
00849646  74 16                           je 0x14084965e
00849648  48 8D 4D B8                     lea rcx, [rbp - 0x48]
0084964C  E8 0F EE FF FF                  call 0x140848460
00849651  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
00849656  E8 05 EE FF FF                  call 0x140848460
0084965B  45 8A E7                        mov r12b, r15b
0084965E  44 38 7C 24 41                  cmp byte ptr [rsp + 0x41], r15b
00849663  74 0D                           je 0x140849672
00849665  48 8B CE                        mov rcx, rsi
00849668  E8 03 AD 01 00                  call 0x140864370
0084966D  44 88 7C 24 41                  mov byte ptr [rsp + 0x41], r15b
00849672  33 D2                           xor edx, edx
00849674  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
00849679  E8 22 23 BD FF                  call 0x14041b9a0
0084967E  E8 01 04 38 00                  call 0x140bc9a84
00849683  48 8B 55 90                     mov rdx, qword ptr [rbp - 0x70]
00849687  4C 8D 4C 24 50                  lea r9, [rsp + 0x50]
0084968C  8B 4C 24 44                     mov ecx, dword ptr [rsp + 0x44]
00849690  E8 17 1D 10 00                  call 0x14094b3ac
00849695  8B F8                           mov edi, eax
00849697  85 C0                           test eax, eax
00849699  0F 89 B3 FD FF FF               jns 0x140849452
0084969F  E9 D2 FD FF FF                  jmp 0x140849476
008496A4  48 0F BF 4C 24 72               movsx rcx, word ptr [rsp + 0x72]
008496AA  48 8B 45 88                     mov rax, qword ptr [rbp - 0x78]
008496AE  48 8B 7C C8 F0                  mov rdi, qword ptr [rax + rcx*8 - 0x10]
008496B3  E9 27 FB FF FF                  jmp 0x1408491df
008496B8  BF 21 01 00 C0                  mov edi, 0xc0000121
008496BD  E9 18 FC FF FF                  jmp 0x1408492da
008496C2  BF 9A 00 00 C0                  mov edi, 0xc000009a
008496C7  E9 0E FC FF FF                  jmp 0x1408492da
008496CC  48 0F BF 4C 24 72               movsx rcx, word ptr [rsp + 0x72]
008496D2  48 8B 45 88                     mov rax, qword ptr [rbp - 0x78]
008496D6  48 8B 5C C8 F0                  mov rbx, qword ptr [rax + rcx*8 - 0x10]
008496DB  E9 C3 FE FF FF                  jmp 0x1408495a3
008496E0  B8 01 00 00 00                  mov eax, 1
008496E5  E9 65 FA FF FF                  jmp 0x14084914f
008496EA  4C 8B 7D B0                     mov r15, qword ptr [rbp - 0x50]
008496EE  E9 E0 F9 FF FF                  jmp 0x1408490d3
008496F3  49 8B CF                        mov rcx, r15
008496F6  E8 65 28 00 00                  call 0x14084bf60
008496FB  84 C0                           test al, al
008496FD  0F 85 F0 F9 FF FF               jne 0x1408490f3
00849703  BF 21 01 00 C0                  mov edi, 0xc0000121
00849708  E9 64 FD FF FF                  jmp 0x140849471
0084970D  4C 8B F7                        mov r14, rdi
00849710  E9 C5 FB FF FF                  jmp 0x1408492da
00849715  BF 01 00 19 C0                  mov edi, 0xc0190001
0084971A  E9 52 FD FF FF                  jmp 0x140849471
0084971F  BF 21 01 00 C0                  mov edi, 0xc0000121
00849724  E9 61 FD FF FF                  jmp 0x14084948a
00849729  48 8B 4E 20                     mov rcx, qword ptr [rsi + 0x20]
0084972D  BA 01 00 00 00                  mov edx, 1
00849732  84 91 8C 00 00 00               test byte ptr [rcx + 0x8c], dl
00849738  48 8D 55 98                     lea rdx, [rbp - 0x68]
0084973C  0F 84 FC CE 2C 00               je 0x140b1663e
00849742  E8 D9 34 01 00                  call 0x14085cc20
00849747  E9 B0 FB FF FF                  jmp 0x1408492fc
0084974C  49 8B CD                        mov rcx, r13
0084974F  E8 28 B2 02 00                  call 0x14087497c
00849754  8B D3                           mov edx, ebx
00849756  49 8B CD                        mov rcx, r13
00849759  E8 12 91 33 00                  call 0x140b82870
0084975E  E9 B7 FB FF FF                  jmp 0x14084931a
00849763  49 8B CE                        mov rcx, r14
00849766  E8 11 B2 02 00                  call 0x14087497c
0084976B  8B D3                           mov edx, ebx
0084976D  49 8B CE                        mov rcx, r14
00849770  E8 FB 90 33 00                  call 0x140b82870
00849775  E9 AC FB FF FF                  jmp 0x140849326
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmDeleteKey(__int64 a1)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int16 v_stack_m106;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m10C;
    unsigned __int8 v_stack_m10D;
    unsigned __int8 v_stack_m10E;
    unsigned __int8 v_stack_m10F;
    unsigned __int8 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned int v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned int v_stack_m134;
    unsigned __int8 v_stack_m135;
    unsigned __int8 v_stack_m136;
    unsigned __int8 v_stack_m137;
    unsigned __int8 v_stack_m138;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m28;
    unsigned __int16 v_stack_mDE;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mF0;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (336);
    result = (*(unsigned __int64 *)(v_rip + 6035642)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 120 + 64) = result;
    v_rdi = 0;
    *(unsigned __int64 *)(v_rsp - 120 + 8) = a1;
    *(unsigned __int64 *)(v_rsp - 120 - 104) = 0;
    v_stack_m120 = 0;
    *(unsigned __int64 *)(v_rsp - 120 - 88) = v_rsp - 120 - 96;
    *(unsigned __int64 *)(v_rsp - 120 - 112) = 0;
    *(unsigned __int64 *)(v_rsp - 120 - 96) = v_rsp - 120 - 96;
    result = (unsigned int)((v_rsp - 120 - 96) | (0xFFFFFFFFULL));
    v_stack_m134 = 0;
    *(unsigned __int64 *)(v_rsp - 120 + 16) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 120 + 32) = v_xmm0;
    v_stack_m136 = 0;
    *(unsigned __int64 *)(v_rsp - 120 + 48) = v_xmm0;
    v_stack_m137 = 0;
    v_stack_m118 = v_xmm0;
    v_stack_m108 = v_xmm0;
    v_stack_m106 = (unsigned __int16)(result);
    *(unsigned __int64 *)(v_rsp - 120 - 72) = v_xmm0;
    *(unsigned __int16 *)(v_rsp - 120 - 70) = (unsigned __int16)(result);
    v_stack_m135 = 0;
    *(unsigned __int64 *)(v_rsp - 120 - 128) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 120 - 80) = 0;
    *(unsigned __int64 *)(v_rsp - 120 - 56) = v_xmm0;
    v_stack_m128 = 0;
    v_stack_m130 = 0;
    *(unsigned __int64 *)(v_rsp - 120) = 0;
    *(unsigned __int64 *)(v_rsp - 120 - 8) = 0;
    result = HvpGetCellContextInitialize(v_rsp - 120 - 104, a2, a3, a4);
    result = HvpGetCellContextInitialize(v_stack_m120, a2, a3, a4);
    *(unsigned __int64 *)(v_rsp - 120 - 40) = 0;
    *(unsigned __int64 *)(v_rsp - 120 - 16) = v_rsp - 120 - 24;
    *(unsigned int *)(v_rsp - 120 - 28) = 0;
    *(unsigned __int64 *)(v_rsp - 120 - 24) = v_rsp - 120 - 24;
    *(unsigned int *)(v_rsp - 120 - 32) = 0xC0000001ULL;
    result = CmpInitializeDelayDerefContext(v_stack_m118, a2, a3, a4);
    result = CmpAttachToRegistryProcess(v_rsp - 120 + 16, a2, a3, a4);
loc_00848F68:
    result = CmpIsShutdownRundownActive(v_rsp - 120 + 16, 1, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_008495F6;
    if (0 != 0) goto loc_008493D5;
    result = CmpLockRegistry(v_rsp - 120 + 16, 1, a3, a4);
loc_00848F88:
    v_stack_m138 = 1;
    if (((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 160)) & (0x100000ULL)) != 0) goto loc_00849485;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 72)) == 0) goto loc_0084971F;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 66)) != 0) goto loc_0084945E;
    result = CmpStartKcbStackForTopLayerKcb(v_rsp - 120 - 72, *(unsigned __int64 *)(a1 + 8), a3, a4);
    if (sign_flag) goto loc_00849471;
    result = CmpStartKcbStackForTopLayerKcb(v_stack_m108, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 72), a3, a4);
    if (sign_flag) goto loc_00849471;
    v_rdi = 0;
    if (0 != 0) goto loc_00849066;
    result = CmpLockHashEntryExclusiveByKcb(*(unsigned __int64 *)(a1 + 8), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 72), a3, a4);
    v_stack_m137 = 1;
    result = CmpLockKcbStackTopExclusiveRestShared(v_stack_m108, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 72), a3, a4);
    if (0 > ((unsigned __int16)(*(unsigned __int16 *)(v_rsp - 120 - 70)))) goto loc_008493CB;
    v_r15 = (*(unsigned __int64 *)(v_rsp - 120 - 48)) - (v_rsp - 120 - 64);
loc_00849031:
    if (0 >= 2) goto loc_0084961C;
loc_0084903E:
    result = CmpLockKcbExclusive(*(unsigned __int64 *)(v_rsp - 120 - 64), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 72), a3, a4);
    v_rdi = (v_rsp - 120 - 64) + (8);
    v_r14 = (unsigned __int16)((0) + (1));
    if (((unsigned __int16)(v_r14)) <= ((unsigned __int16)(*(unsigned __int16 *)(v_rsp - 120 - 70)))) goto loc_00849031;
    v_rdi = 0;
loc_0084905F:
loc_00849066:
    a2 = 0;
    result = CmpIsKeyDeletedForKeyBody(*(unsigned __int64 *)(v_rsp - 120 + 8), a2, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00849471;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 120 + 8) + 56)) != 0) goto loc_00849088;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 120 + 8) + 64)) == 0) goto loc_008496EA;
loc_00849088:
    result = CmpTransSearchAddTransFromKeyBody(*(unsigned __int64 *)(v_rsp - 120 + 8), v_rsp - 120 - 80, a3, a4);
    if (sign_flag) goto loc_00849471;
    if (((2) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 160))))) != 0) goto loc_00849715;
    result = CmpIsKeyDeletedForKeyBody(*(unsigned __int64 *)(v_rsp - 120 + 8), *(unsigned __int64 *)(v_rsp - 120 - 80), a3, a4);
    v_rdi = 0;
    if ((unsigned __int8)(result) != 0) goto loc_0084970D;
    if (*(unsigned __int64 *)(v_rsp - 120 - 80) != 0) goto loc_008490E3;
loc_008490D3:
loc_008490E3:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 240) != 0) goto loc_008496F3;
loc_008490F3:
    if (*(unsigned __int64 *)(v_rsp - 120 - 80) != 0) goto loc_0084948F;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 72)) + (248);
    if ((*(unsigned int *)(a1)) < 0) goto loc_008493DF;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 248)) != 0) goto loc_00849628;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 264)) != 0) goto loc_00849628;
loc_00849132:
    if (v_stack_m136 != 0) goto loc_008496E0;
    result = HvLockHiveFlusherShared(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 240), a3, a4);
    v_stack_m135 = 1;
loc_0084914F:
    result = CmpGetKeyNodeForKcb(*(unsigned __int64 *)(a1 + 8), v_rsp - 120 - 104, 1, a4);
    *(unsigned __int64 *)(v_rsp - 120 - 8) = result;
    result = CmGetVisibleSubkeyCount(*(unsigned __int64 *)(a1 + 8), result, *(unsigned __int64 *)(v_rsp - 120 - 80), a4);
    if ((unsigned int)(result) != 0) goto loc_008496B8;
    if (((*(unsigned __int8 *)(result + 2)) & (8)) != 0) goto loc_008496B8;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 140)) & ((unsigned __int8)(result + 1))) != 0) goto loc_00849608;
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), v_rsp - 120 - 104, *(unsigned __int64 *)(v_rsp - 120 - 80), a4);
loc_008491A2:
    result = 0;
    *(unsigned __int64 *)(v_rsp - 120 - 8) = 0;
    if (*(unsigned __int64 *)(v_rsp - 120 - 80) != 0) goto loc_00849546;
    if (v_stack_m106 >= 2) goto loc_008496A4;
loc_008491DF:
    v_stack_m158 = v_rsp - 120 - 96;
    a3 = 0;
    result = CmpReportNotifyHelper(v_stack_m108, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp + (__int16)(v_stack_m106) * 8 + 120) + 32), a3, 1);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp + (__int16)(v_stack_m106) * 8 + 120) + 32)) != (*(unsigned __int64 *)(v_rip + 7932042))) {
        result = v_rsp - 120 - 96;
        a4 = 1;
        a3 = 0;
        v_stack_m158 = result;
        a1 = v_stack_m108;
        result = CmpReportNotifyHelper(a1, *(unsigned __int64 *)(v_rip + 7932042), a3, a4);
    }
    result = CmpFreeKeyByCell(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 40)), 1, a4);
    if (sign_flag) goto loc_008492DA;
    a4 = 0;
    result = CmpFlushNotifiesOnKeyBodyList(*(unsigned __int64 *)(a1 + 8), a4 + 8, v_stack_m118, a4);
    result = CmpCleanUpSubKeyInfo(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 72), 1, v_stack_m118, a4);
    result = CmpGetKeyNodeForKcb(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 72), v_stack_m120, 1, a4);
    *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 72) + 176) = (unsigned __int16)(*(unsigned __int16 *)(result + 52));
    *(unsigned __int64 *)(result + 4) = *(unsigned __int64 *)(v_rbx);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 72) + 168) = *(unsigned __int64 *)(v_rbx);
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 72) + 32) + 140)) & (1)) != 0) goto loc_00849612;
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 72) + 32), v_stack_m120, 1, a4);
loc_008492C2:
    result = CmpMarkKeyUnbacked(*(unsigned __int64 *)(a1 + 8), v_stack_m118, 1, a4);
    result = CmpDiscardKcb(*(unsigned __int64 *)(a1 + 8), v_stack_m118, 1, a4);
loc_008492D7:
loc_008492DA:
loc_008492E4:
    if ((*(unsigned __int64 *)(v_rsp - 120 - 8)) != 0) goto loc_00849729;
loc_008492FC:
    if (v_stack_m135 != 0) {
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32);
        result = HvUnlockHiveFlusherShared(a1, 1, 1, a4);
    }
    if (*(unsigned __int64 *)(v_rsp - 120) != 0) goto loc_0084974C;
loc_0084931A:
    v_r13 = 0;
    if (v_stack_m130 != 0) goto loc_00849763;
loc_00849326:
    if (1 != 0) {
        a1 = v_rsp - 120 - 72;
        result = CmpUnlockKcbStack(a1, 1, 1, a4);
        a1 = v_stack_m108;
        result = CmpUnlockKcbStack(a1, 1, 1, a4);
    }
    if (v_stack_m137 != 0) {
        a1 = *(unsigned __int64 *)(a1 + 8);
        result = CmpUnlockHashEntryByKcb(a1, 1, 1, a4);
    }
    if (*(unsigned __int64 *)(v_rsp - 120 - 48) != 0) {
        result = CmSiFreeMemory(*(unsigned __int64 *)(v_rsp - 120 - 48), 1, 1, a4);
    }
    if (*(unsigned __int64 *)(v_rsp - 120 - 120) != 0) {
        result = CmSiFreeMemory(*(unsigned __int64 *)(v_rsp - 120 - 120), 1, 1, a4);
    }
    a2 = 0;
    result = CmpDrainDelayDerefContext(v_stack_m118, a2, 1, a4);
    if ((unsigned __int8)(v_stack_m138) != 0) {
        result = CmpUnlockRegistry(v_stack_m118, a2, 1, a4);
    }
    result = CmpDetachFromRegistryProcess(v_rsp - 120 + 16, a2, 1, a4);
    result = v_rsp - 120 - 96;
    if ((*(unsigned __int64 *)(v_rsp - 120 - 96)) != (v_rsp - 120 - 96)) {
        a1 = v_rsp - 120 - 96;
        result = CmpSignalDeferredPosts(a1, a2, 1, a4);
    }
    a1 = (*(unsigned __int64 *)(v_rsp - 120 + 64)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, 1, a4);
    return result;
loc_008493CB:
    goto loc_0084905F;
loc_008493D5:
    result = CmpLockRegistryExclusive(a1, a2, 1, a4);
    goto loc_00848F88;
loc_008493DF:
    result = CmpSnapshotTxOwnerArray(a1, v_stack_m10C, v_rsp - 120 - 112, a4);
    v_r15 = 0;
    if (sign_flag) goto loc_00849471;
    v_r12 = 1;
    if (1 != 0) {
        a1 = v_rsp - 120 - 72;
        result = CmpUnlockKcbStack(a1, v_stack_m10C, v_rsp - 120 - 112, a4);
        a1 = v_stack_mE0;
        result = CmpUnlockKcbStack(a1, v_stack_m10C, v_rsp - 120 - 112, a4);
        v_r12 = 0;
    }
    if (v_stack_m10F != 0) {
        a1 = *(unsigned __int64 *)(v_stack_m28 + 64);
        result = CmpUnlockHashEntryByKcb(a1, v_stack_m10C, v_rsp - 120 - 112, a4);
        v_stack_m10F = 0;
    }
    a2 = 0;
    result = CmpDrainDelayDerefContext(v_stack_mF0, a2, v_rsp - 120 - 112, a4);
    result = CmpUnlockRegistry(v_stack_mF0, a2, v_rsp - 120 - 112, a4);
    result = CmpRollbackTransactionArray((unsigned int)(v_stack_m10C), *(unsigned __int64 *)(v_rsp - 120 - 112), v_rsp - 120 - 112, v_stack_m100);
    if (sign_flag) goto loc_00849603;
loc_00849452:
    v_rdi = 0;
    goto loc_00848F68;
loc_0084945E:
    result = CmDeleteLayeredKey(v_stack_m130, v_rsp - 120 - 96, v_stack_mF0, v_stack_m100);
loc_00849471:
loc_00849476:
loc_0084947B:
    goto loc_008492E4;
loc_00849485:
loc_0084948A:
    goto loc_0084947B;
loc_0084948F:
    result = CmpAllocateUnitOfWork(v_stack_m130, 1, v_stack_mF0, v_stack_m100);
    if (result == 0) goto loc_008496C2;
    result = CmpAllocateUnitOfWork(v_stack_m130, 1, v_stack_mF0, v_stack_m100);
    if (result == 0) goto loc_008496C2;
    result = CmpTransEnlistUowInKcb(result, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 72), v_stack_mF0, v_stack_m100);
    result = CmpTransEnlistUowInCmTrans(result, 1, v_stack_mF0, v_stack_m100);
    if (sign_flag) goto loc_008492DA;
    result = CmpTransEnlistUowInKcb(result, *(unsigned __int64 *)(v_stack_m28 + 64), v_stack_mF0, v_stack_m100);
    result = CmpTransEnlistUowInCmTrans(result, 1, v_stack_mF0, v_stack_m100);
    if (sign_flag) goto loc_008492DA;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 72)) + (248);
    result = CmpLockIXLockIntent(a1, result, v_stack_mF0, v_stack_m100);
    v_rdi = 0;
    if ((unsigned __int8)(result) == 0) goto loc_0084953C;
    a3 = 0;
    result = CmpLockIXLockExclusive(*(unsigned __int64 *)(v_stack_m28 + 64) + 248, result, a3, v_stack_m100);
    if ((unsigned __int8)(result) == 0) goto loc_0084953C;
    result = CmpLockIXLockExclusive(*(unsigned __int64 *)(v_stack_m28 + 64) + 264, result, v_rdi + 1, v_stack_m100);
    if ((unsigned __int8)(result) != 0) goto loc_00849132;
loc_0084953C:
    goto loc_008492DA;
loc_00849546:
    *(unsigned int *)(result + 68) = 3;
    *(unsigned __int64 *)(result + 88) = *(unsigned __int64 *)(v_stack_m28 + 64);
    *(unsigned int *)(result + 68) = 2;
    *(unsigned __int64 *)(result + 80) = result;
    result = HvUnlockHiveFlusherShared(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 32), result, v_rdi + 1, v_stack_m100);
    v_r15 = 0;
    v_stack_m10D = 0;
    result = CmAddLogForAction(result, (unsigned int)((unsigned int)((unsigned int)(0xC0190001ULL))), v_rdi + 1, v_stack_m100);
    if (sign_flag) goto loc_008492DA;
    if (v_stack_mDE >= 2) goto loc_008496CC;
loc_008495A3:
    v_stack_m130 = v_rsp - 120 - 96;
    result = CmpReportNotifyHelper(v_stack_mE0, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + (__int16)(v_stack_mDE) * 8 + 120) + 32), *(unsigned __int64 *)(v_rsp - 120 - 80), 1);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + (__int16)(v_stack_mDE) * 8 + 120) + 32)) == (*(unsigned __int64 *)(v_rip + 7931075))) goto loc_008492D7;
    v_stack_m130 = v_rsp - 120 - 96;
    result = CmpReportNotifyHelper(v_stack_mE0, *(unsigned __int64 *)(v_rip + 7931075), *(unsigned __int64 *)(v_rsp - 120 - 80), 1);
    goto loc_008492D7;
loc_008495F6:
    v_r15 = 0;
    goto loc_0084947B;
loc_00849603:
    goto loc_00849476;
loc_00849608:
    result = HvpReleaseCellFlat(v_stack_mE0, *(unsigned __int64 *)(v_rip + 7931075), *(unsigned __int64 *)(v_rsp - 120 - 80), 1);
    goto loc_008491A2;
loc_00849612:
    result = HvpReleaseCellFlat(v_stack_mE0, *(unsigned __int64 *)(v_rip + 7931075), *(unsigned __int64 *)(v_rsp - 120 - 80), 1);
    goto loc_008492C2;
loc_0084961C:
    a1 = (v_r15 - 16) + ((unsigned int)(0xC0000189ULL));
    goto loc_0084903E;
loc_00849628:
    result = CmpSnapshotTxOwnerArray(a1, v_stack_m10C, v_rsp - 120 - 112, 1);
    v_r15 = 0;
    if (sign_flag) goto loc_00849471;
    if ((unsigned __int8)(v_r12) != 0) {
        a1 = v_rsp - 120 - 72;
        result = CmpUnlockKcbStack(a1, v_stack_m10C, v_rsp - 120 - 112, 1);
        a1 = v_stack_mE0;
        result = CmpUnlockKcbStack(a1, v_stack_m10C, v_rsp - 120 - 112, 1);
        v_r12 = 0;
    }
    if (v_stack_m10F != 0) {
        a1 = *(unsigned __int64 *)(v_stack_m28 + 64);
        result = CmpUnlockHashEntryByKcb(a1, v_stack_m10C, v_rsp - 120 - 112, 1);
        v_stack_m10F = 0;
    }
    a2 = 0;
    result = CmpDrainDelayDerefContext(v_stack_mF0, a2, v_rsp - 120 - 112, 1);
    result = CmpUnlockRegistry(v_stack_mF0, a2, v_rsp - 120 - 112, 1);
    result = CmpRollbackTransactionArray((unsigned int)(v_stack_m10C), *(unsigned __int64 *)(v_rsp - 120 - 112), v_rsp - 120 - 112, v_stack_m100);
    if (!sign_flag) goto loc_00849452;
    goto loc_00849476;
loc_008496A4:
    goto loc_008491DF;
loc_008496B8:
    goto loc_008492DA;
loc_008496C2:
    goto loc_008492DA;
loc_008496CC:
    goto loc_008495A3;
loc_008496E0:
    goto loc_0084914F;
loc_008496EA:
    goto loc_008490D3;
loc_008496F3:
    result = CmEqualTrans(*(unsigned __int64 *)(v_rsp - 120 - 80), *(unsigned __int64 *)(v_rsp - 120 - 112), v_rsp - 120 - 112, v_stack_m100);
    if ((unsigned __int8)(result) != 0) goto loc_008490F3;
    goto loc_00849471;
loc_0084970D:
    goto loc_008492DA;
loc_00849715:
    goto loc_00849471;
loc_0084971F:
    goto loc_0084948A;
loc_00849729:
    result = HvpReleaseCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 32), v_rsp - 120 - 104, v_rsp - 120 - 112, v_stack_m100);
    goto loc_008492FC;
loc_0084974C:
    result = CmpRundownUnitOfWork(0, v_rsp - 120 - 104, v_rsp - 120 - 112, v_stack_m100);
    result = ExFreePoolWithTag(0, (unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 120 - 120) + (__int16)(v_stack_mDE) * 8 - 16))), v_rsp - 120 - 112, v_stack_m100);
    goto loc_0084931A;
loc_00849763:
    result = CmpRundownUnitOfWork((unsigned int)(0xC0000121ULL), (unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 120 - 120) + (__int16)(v_stack_mDE) * 8 - 16))), v_rsp - 120 - 112, v_stack_m100);
    result = ExFreePoolWithTag((unsigned int)(0xC0000121ULL), (unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 120 - 120) + (__int16)(v_stack_mDE) * 8 - 16))), v_rsp - 120 - 112, v_stack_m100);
    goto loc_00849326;
}
```

## 5. (Beta) C Style

```c
int64_t CmDeleteKey(int64_t Arg1)
{
    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint16_t v_stack_m106;
    uint64_t v_stack_m108;
    uint64_t v_stack_m10C;
    uint8_t v_stack_m10D;
    uint8_t v_stack_m10E;
    uint8_t v_stack_m10F;
    uint8_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint32_t v_stack_m128;
    uint64_t v_stack_m130;
    uint32_t v_stack_m134;
    uint8_t v_stack_m135;
    uint8_t v_stack_m136;
    uint8_t v_stack_m137;
    uint8_t v_stack_m138;
    uint64_t v_stack_m158;
    uint64_t v_stack_m28;
    uint16_t v_stack_mDE;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mF0;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (336);
    result = (*(uint64_t *)(v_rip + 0x5C18BA)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x78 + 0x40) = result;
    local_rdi = 0;
    *(uint64_t *)(local_rsp - 0x78 + 0x8) = Arg1;
    *(uint64_t *)(local_rsp - 0x78 - 0x68) = 0;
    v_stack_m120 = 0;
    *(uint64_t *)(local_rsp - 0x78 - 0x58) = local_rsp - 120 - 96;
    *(uint64_t *)(local_rsp - 0x78 - 0x70) = 0;
    *(uint64_t *)(local_rsp - 0x78 - 0x60) = local_rsp - 120 - 96;
    result = (uint32_t)((local_rsp - 120 - 96) | (0xFFFFFFFFULL));
    v_stack_m134 = 0;
    *(uint64_t *)(local_rsp - 0x78 + 0x10) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x78 + 0x20) = v_xmm0;
    v_stack_m136 = 0;
    *(uint64_t *)(local_rsp - 0x78 + 0x30) = v_xmm0;
    v_stack_m137 = 0;
    v_stack_m118 = v_xmm0;
    v_stack_m108 = v_xmm0;
    v_stack_m106 = (uint16_t)(result);
    *(uint64_t *)(local_rsp - 0x78 - 0x48) = v_xmm0;
    *(uint16_t *)(local_rsp - 0x78 - 0x46) = (uint16_t)(result);
    v_stack_m135 = 0;
    *(uint64_t *)(local_rsp - 0x78 - 0x80) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x78 - 0x50) = 0;
    *(uint64_t *)(local_rsp - 0x78 - 0x38) = v_xmm0;
    v_stack_m128 = 0;
    v_stack_m130 = 0;
    *(uint64_t *)(local_rsp - 0x78) = 0;
    *(uint64_t *)(local_rsp - 0x78 - 0x8) = 0;
    result = HvpGetCellContextInitialize(local_rsp - 120 - 104, a2, a3, a4);
    result = HvpGetCellContextInitialize(v_stack_m120, a2, a3, a4);
    *(uint64_t *)(local_rsp - 0x78 - 0x28) = 0;
    *(uint64_t *)(local_rsp - 0x78 - 0x10) = local_rsp - 120 - 24;
    *(uint32_t *)(local_rsp - 0x78 - 0x1C) = 0;
    *(uint64_t *)(local_rsp - 0x78 - 0x18) = local_rsp - 120 - 24;
    *(uint32_t *)(local_rsp - 0x78 - 0x20) = 0xC0000001ULL;
    result = CmpInitializeDelayDerefContext(v_stack_m118, a2, a3, a4);
    result = CmpAttachToRegistryProcess(local_rsp - 120 + 16, a2, a3, a4);
loc_00848F68:
    result = CmpIsShutdownRundownActive(local_rsp - 120 + 16, 1, a3, a4);
    if ((uint8_t)(result) != 0) goto loc_008495F6;
    if (0 != 0) goto loc_008493D5;
    result = CmpLockRegistry(local_rsp - 120 + 16, 1, a3, a4);
loc_00848F88:
    v_stack_m138 = 1;
    if (((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x20) + 0xA0)) & (0x100000ULL)) != 0) goto loc_00849485;
    if ((*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x48)) == 0) goto loc_0084971F;
    if ((*(uint16_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x42)) != 0) goto loc_0084945E;
    result = CmpStartKcbStackForTopLayerKcb(local_rsp - 120 - 72, *(uint64_t *)(Arg1 + 0x8), a3, a4);
    if (sign_flag) goto loc_00849471;
    result = CmpStartKcbStackForTopLayerKcb(v_stack_m108, *(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x48), a3, a4);
    if (sign_flag) goto loc_00849471;
    local_rdi = 0;
    if (0 != 0) goto loc_00849066;
    result = CmpLockHashEntryExclusiveByKcb(*(uint64_t *)(Arg1 + 0x8), *(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x48), a3, a4);
    v_stack_m137 = 1;
    result = CmpLockKcbStackTopExclusiveRestShared(v_stack_m108, *(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x48), a3, a4);
    if (0 > ((uint16_t)(*(uint16_t *)(local_rsp - 0x78 - 0x46)))) goto loc_008493CB;
    local_r15 = (*(uint64_t *)(local_rsp - 0x78 - 0x30)) - (local_rsp - 120 - 64);
loc_00849031:
    if (0 >= 2) goto loc_0084961C;
loc_0084903E:
    result = CmpLockKcbExclusive(*(uint64_t *)(local_rsp - 0x78 - 0x40), *(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x48), a3, a4);
    local_rdi = (local_rsp - 120 - 64) + (8);
    local_r14 = (uint16_t)((0) + (1));
    if (((uint16_t)(local_r14)) <= ((uint16_t)(*(uint16_t *)(local_rsp - 0x78 - 0x46)))) goto loc_00849031;
    local_rdi = 0;
loc_0084905F:
loc_00849066:
    a2 = 0;
    result = CmpIsKeyDeletedForKeyBody(*(uint64_t *)(local_rsp - 0x78 + 0x8), a2, a3, a4);
    if ((uint8_t)(result) != 0) goto loc_00849471;
    if ((*(uint64_t *)(*(uint64_t *)(local_rsp - 0x78 + 0x8) + 0x38)) != 0) goto loc_00849088;
    if ((*(uint64_t *)(*(uint64_t *)(local_rsp - 0x78 + 0x8) + 0x40)) == 0) goto loc_008496EA;
loc_00849088:
    result = CmpTransSearchAddTransFromKeyBody(*(uint64_t *)(local_rsp - 0x78 + 0x8), local_rsp - 120 - 80, a3, a4);
    if (sign_flag) goto loc_00849471;
    if (((2) & ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x20) + 0xA0))))) != 0) goto loc_00849715;
    result = CmpIsKeyDeletedForKeyBody(*(uint64_t *)(local_rsp - 0x78 + 0x8), *(uint64_t *)(local_rsp - 0x78 - 0x50), a3, a4);
    local_rdi = 0;
    if ((uint8_t)(result) != 0) goto loc_0084970D;
    if (*(uint64_t *)(local_rsp - 0x78 - 0x50) != 0) goto loc_008490E3;
loc_008490D3:
loc_008490E3:
    if (*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0xF0) != 0) goto loc_008496F3;
loc_008490F3:
    if (*(uint64_t *)(local_rsp - 0x78 - 0x50) != 0) goto loc_0084948F;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x48)) + (248);
    if ((*(uint32_t *)(Arg1)) < 0) goto loc_008493DF;
    if ((*(uint32_t *)(*(uint64_t *)(Arg1 + 0x8) + 0xF8)) != 0) goto loc_00849628;
    if ((*(uint32_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x108)) != 0) goto loc_00849628;
loc_00849132:
    if (v_stack_m136 != 0) goto loc_008496E0;
    result = HvLockHiveFlusherShared(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x20), *(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0xF0), a3, a4);
    v_stack_m135 = 1;
loc_0084914F:
    result = CmpGetKeyNodeForKcb(*(uint64_t *)(Arg1 + 0x8), local_rsp - 120 - 104, 1, a4);
    *(uint64_t *)(local_rsp - 0x78 - 0x8) = result;
    result = CmGetVisibleSubkeyCount(*(uint64_t *)(Arg1 + 0x8), result, *(uint64_t *)(local_rsp - 0x78 - 0x50), a4);
    if ((uint32_t)(result) != 0) goto loc_008496B8;
    if (((*(uint8_t *)(result + 0x2)) & (8)) != 0) goto loc_008496B8;
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x20) + 0x8C)) & ((uint8_t)(result + 1))) != 0) goto loc_00849608;
    result = HvpReleaseCellPaged(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x20), local_rsp - 120 - 104, *(uint64_t *)(local_rsp - 0x78 - 0x50), a4);
loc_008491A2:
    result = 0;
    *(uint64_t *)(local_rsp - 0x78 - 0x8) = 0;
    if (*(uint64_t *)(local_rsp - 0x78 - 0x50) != 0) goto loc_00849546;
    if (v_stack_m106 >= 2) goto loc_008496A4;
loc_008491DF:
    v_stack_m158 = local_rsp - 120 - 96;
    a3 = 0;
    result = CmpReportNotifyHelper(v_stack_m108, *(uint64_t *)(*(uint64_t *)(local_rsp + (int16_t)(v_stack_m106) * 8 + 0x78) + 0x20), a3, 1);
    if ((*(uint64_t *)(*(uint64_t *)(local_rsp + (int16_t)(v_stack_m106) * 8 + 0x78) + 0x20)) != (*(uint64_t *)(v_rip + 0x79088A))) {
        result = local_rsp - 120 - 96;
        a4 = 1;
        a3 = 0;
        v_stack_m158 = result;
        Arg1 = v_stack_m108;
        result = CmpReportNotifyHelper(Arg1, *(uint64_t *)(v_rip + 0x79088A), a3, a4);
    }
    result = CmpFreeKeyByCell(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x20), (uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x28)), 1, a4);
    if (sign_flag) goto loc_008492DA;
    a4 = 0;
    result = CmpFlushNotifiesOnKeyBodyList(*(uint64_t *)(Arg1 + 0x8), a4 + 8, v_stack_m118, a4);
    result = CmpCleanUpSubKeyInfo(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x48), 1, v_stack_m118, a4);
    result = CmpGetKeyNodeForKcb(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x48), v_stack_m120, 1, a4);
    *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x48) + 0xB0) = (uint16_t)(*(uint16_t *)(result + 0x34));
    *(uint64_t *)(result + 0x4) = *(uint64_t *)(local_rbx);
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x48) + 0xA8) = *(uint64_t *)(local_rbx);
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x48) + 0x20) + 0x8C)) & (1)) != 0) goto loc_00849612;
    result = HvpReleaseCellPaged(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x48) + 0x20), v_stack_m120, 1, a4);
loc_008492C2:
    result = CmpMarkKeyUnbacked(*(uint64_t *)(Arg1 + 0x8), v_stack_m118, 1, a4);
    result = CmpDiscardKcb(*(uint64_t *)(Arg1 + 0x8), v_stack_m118, 1, a4);
loc_008492D7:
loc_008492DA:
loc_008492E4:
    if ((*(uint64_t *)(local_rsp - 0x78 - 0x8)) != 0) goto loc_00849729;
loc_008492FC:
    if (v_stack_m135 != 0) {
        Arg1 = *(uint64_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x20);
        result = HvUnlockHiveFlusherShared(Arg1, 1, 1, a4);
    }
    if (*(uint64_t *)(local_rsp - 0x78) != 0) goto loc_0084974C;
loc_0084931A:
    local_r13 = 0;
    if (v_stack_m130 != 0) goto loc_00849763;
loc_00849326:
    if (1 != 0) {
        Arg1 = local_rsp - 120 - 72;
        result = CmpUnlockKcbStack(Arg1, 1, 1, a4);
        Arg1 = v_stack_m108;
        result = CmpUnlockKcbStack(Arg1, 1, 1, a4);
    }
    if (v_stack_m137 != 0) {
        Arg1 = *(uint64_t *)(Arg1 + 0x8);
        result = CmpUnlockHashEntryByKcb(Arg1, 1, 1, a4);
    }
    if (*(uint64_t *)(local_rsp - 0x78 - 0x30) != 0) {
        result = CmSiFreeMemory(*(uint64_t *)(local_rsp - 0x78 - 0x30), 1, 1, a4);
    }
    if (*(uint64_t *)(local_rsp - 0x78 - 0x78) != 0) {
        result = CmSiFreeMemory(*(uint64_t *)(local_rsp - 0x78 - 0x78), 1, 1, a4);
    }
    a2 = 0;
    result = CmpDrainDelayDerefContext(v_stack_m118, a2, 1, a4);
    if ((uint8_t)(v_stack_m138) != 0) {
        result = CmpUnlockRegistry(v_stack_m118, a2, 1, a4);
    }
    result = CmpDetachFromRegistryProcess(local_rsp - 120 + 16, a2, 1, a4);
    result = local_rsp - 120 - 96;
    if ((*(uint64_t *)(local_rsp - 0x78 - 0x60)) != (local_rsp - 120 - 96)) {
        Arg1 = local_rsp - 120 - 96;
        result = CmpSignalDeferredPosts(Arg1, a2, 1, a4);
    }
    Arg1 = (*(uint64_t *)(local_rsp - 0x78 + 0x40)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, a2, 1, a4);
    return result;
loc_008493CB:
    goto loc_0084905F;
loc_008493D5:
    result = CmpLockRegistryExclusive(Arg1, a2, 1, a4);
    goto loc_00848F88;
loc_008493DF:
    result = CmpSnapshotTxOwnerArray(Arg1, v_stack_m10C, local_rsp - 120 - 112, a4);
    local_r15 = 0;
    if (sign_flag) goto loc_00849471;
    local_r12 = 1;
    if (1 != 0) {
        Arg1 = local_rsp - 120 - 72;
        result = CmpUnlockKcbStack(Arg1, v_stack_m10C, local_rsp - 120 - 112, a4);
        Arg1 = v_stack_mE0;
        result = CmpUnlockKcbStack(Arg1, v_stack_m10C, local_rsp - 120 - 112, a4);
        local_r12 = 0;
    }
    if (v_stack_m10F != 0) {
        Arg1 = *(uint64_t *)(v_stack_m28 + 0x40);
        result = CmpUnlockHashEntryByKcb(Arg1, v_stack_m10C, local_rsp - 120 - 112, a4);
        v_stack_m10F = 0;
    }
    a2 = 0;
    result = CmpDrainDelayDerefContext(v_stack_mF0, a2, local_rsp - 120 - 112, a4);
    result = CmpUnlockRegistry(v_stack_mF0, a2, local_rsp - 120 - 112, a4);
    result = CmpRollbackTransactionArray((uint32_t)(v_stack_m10C), *(uint64_t *)(local_rsp - 0x78 - 0x70), local_rsp - 120 - 112, v_stack_m100);
    if (sign_flag) goto loc_00849603;
loc_00849452:
    local_rdi = 0;
    goto loc_00848F68;
loc_0084945E:
    result = CmDeleteLayeredKey(v_stack_m130, local_rsp - 120 - 96, v_stack_mF0, v_stack_m100);
loc_00849471:
loc_00849476:
loc_0084947B:
    goto loc_008492E4;
loc_00849485:
loc_0084948A:
    goto loc_0084947B;
loc_0084948F:
    result = CmpAllocateUnitOfWork(v_stack_m130, 1, v_stack_mF0, v_stack_m100);
    if (result == 0) goto loc_008496C2;
    result = CmpAllocateUnitOfWork(v_stack_m130, 1, v_stack_mF0, v_stack_m100);
    if (result == 0) goto loc_008496C2;
    result = CmpTransEnlistUowInKcb(result, *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x48), v_stack_mF0, v_stack_m100);
    result = CmpTransEnlistUowInCmTrans(result, 1, v_stack_mF0, v_stack_m100);
    if (sign_flag) goto loc_008492DA;
    result = CmpTransEnlistUowInKcb(result, *(uint64_t *)(v_stack_m28 + 0x40), v_stack_mF0, v_stack_m100);
    result = CmpTransEnlistUowInCmTrans(result, 1, v_stack_mF0, v_stack_m100);
    if (sign_flag) goto loc_008492DA;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x48)) + (248);
    result = CmpLockIXLockIntent(Arg1, result, v_stack_mF0, v_stack_m100);
    local_rdi = 0;
    if ((uint8_t)(result) == 0) goto loc_0084953C;
    a3 = 0;
    result = CmpLockIXLockExclusive(*(uint64_t *)(v_stack_m28 + 0x40) + 248, result, a3, v_stack_m100);
    if ((uint8_t)(result) == 0) goto loc_0084953C;
    result = CmpLockIXLockExclusive(*(uint64_t *)(v_stack_m28 + 0x40) + 264, result, local_rdi + 1, v_stack_m100);
    if ((uint8_t)(result) != 0) goto loc_00849132;
loc_0084953C:
    goto loc_008492DA;
loc_00849546:
    *(uint32_t *)(result + 0x44) = 3;
    *(uint64_t *)(result + 0x58) = *(uint64_t *)(v_stack_m28 + 0x40);
    *(uint32_t *)(result + 0x44) = 2;
    *(uint64_t *)(result + 0x50) = result;
    result = HvUnlockHiveFlusherShared(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x20), result, local_rdi + 1, v_stack_m100);
    local_r15 = 0;
    v_stack_m10D = 0;
    result = CmAddLogForAction(result, (uint32_t)((uint32_t)((uint32_t)(0xC0190001ULL))), local_rdi + 1, v_stack_m100);
    if (sign_flag) goto loc_008492DA;
    if (v_stack_mDE >= 2) goto loc_008496CC;
loc_008495A3:
    v_stack_m130 = local_rsp - 120 - 96;
    result = CmpReportNotifyHelper(v_stack_mE0, *(uint64_t *)(*(uint64_t *)(v_stack_m28 + (int16_t)(v_stack_mDE) * 8 + 0x78) + 0x20), *(uint64_t *)(local_rsp - 0x78 - 0x50), 1);
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m28 + (int16_t)(v_stack_mDE) * 8 + 0x78) + 0x20)) == (*(uint64_t *)(v_rip + 0x7904C3))) goto loc_008492D7;
    v_stack_m130 = local_rsp - 120 - 96;
    result = CmpReportNotifyHelper(v_stack_mE0, *(uint64_t *)(v_rip + 0x7904C3), *(uint64_t *)(local_rsp - 0x78 - 0x50), 1);
    goto loc_008492D7;
loc_008495F6:
    local_r15 = 0;
    goto loc_0084947B;
loc_00849603:
    goto loc_00849476;
loc_00849608:
    result = HvpReleaseCellFlat(v_stack_mE0, *(uint64_t *)(v_rip + 0x7904C3), *(uint64_t *)(local_rsp - 0x78 - 0x50), 1);
    goto loc_008491A2;
loc_00849612:
    result = HvpReleaseCellFlat(v_stack_mE0, *(uint64_t *)(v_rip + 0x7904C3), *(uint64_t *)(local_rsp - 0x78 - 0x50), 1);
    goto loc_008492C2;
loc_0084961C:
    Arg1 = (local_r15 - 16) + ((uint32_t)(0xC0000189ULL));
    goto loc_0084903E;
loc_00849628:
    result = CmpSnapshotTxOwnerArray(Arg1, v_stack_m10C, local_rsp - 120 - 112, 1);
    local_r15 = 0;
    if (sign_flag) goto loc_00849471;
    if ((uint8_t)(local_r12) != 0) {
        Arg1 = local_rsp - 120 - 72;
        result = CmpUnlockKcbStack(Arg1, v_stack_m10C, local_rsp - 120 - 112, 1);
        Arg1 = v_stack_mE0;
        result = CmpUnlockKcbStack(Arg1, v_stack_m10C, local_rsp - 120 - 112, 1);
        local_r12 = 0;
    }
    if (v_stack_m10F != 0) {
        Arg1 = *(uint64_t *)(v_stack_m28 + 0x40);
        result = CmpUnlockHashEntryByKcb(Arg1, v_stack_m10C, local_rsp - 120 - 112, 1);
        v_stack_m10F = 0;
    }
    a2 = 0;
    result = CmpDrainDelayDerefContext(v_stack_mF0, a2, local_rsp - 120 - 112, 1);
    result = CmpUnlockRegistry(v_stack_mF0, a2, local_rsp - 120 - 112, 1);
    result = CmpRollbackTransactionArray((uint32_t)(v_stack_m10C), *(uint64_t *)(local_rsp - 0x78 - 0x70), local_rsp - 120 - 112, v_stack_m100);
    if (!sign_flag) goto loc_00849452;
    goto loc_00849476;
loc_008496A4:
    goto loc_008491DF;
loc_008496B8:
    goto loc_008492DA;
loc_008496C2:
    goto loc_008492DA;
loc_008496CC:
    goto loc_008495A3;
loc_008496E0:
    goto loc_0084914F;
loc_008496EA:
    goto loc_008490D3;
loc_008496F3:
    result = CmEqualTrans(*(uint64_t *)(local_rsp - 0x78 - 0x50), *(uint64_t *)(local_rsp - 0x78 - 0x70), local_rsp - 120 - 112, v_stack_m100);
    if ((uint8_t)(result) != 0) goto loc_008490F3;
    goto loc_00849471;
loc_0084970D:
    goto loc_008492DA;
loc_00849715:
    goto loc_00849471;
loc_0084971F:
    goto loc_0084948A;
loc_00849729:
    result = HvpReleaseCellFlat(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x20), local_rsp - 120 - 104, local_rsp - 120 - 112, v_stack_m100);
    goto loc_008492FC;
loc_0084974C:
    result = CmpRundownUnitOfWork(0, local_rsp - 120 - 104, local_rsp - 120 - 112, v_stack_m100);
    result = ExFreePoolWithTag(0, (uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x78 - 0x78) + (int16_t)(v_stack_mDE) * 8 - 0x10))), local_rsp - 120 - 112, v_stack_m100);
    goto loc_0084931A;
loc_00849763:
    result = CmpRundownUnitOfWork((uint32_t)(0xC0000121ULL), (uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x78 - 0x78) + (int16_t)(v_stack_mDE) * 8 - 0x10))), local_rsp - 120 - 112, v_stack_m100);
    result = ExFreePoolWithTag((uint32_t)(0xC0000121ULL), (uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x78 - 0x78) + (int16_t)(v_stack_mDE) * 8 - 0x10))), local_rsp - 120 - 112, v_stack_m100);
    goto loc_00849326;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00848E5C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
