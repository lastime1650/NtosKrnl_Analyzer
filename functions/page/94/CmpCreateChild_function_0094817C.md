# CmpCreateChild

- RVA: `0x0094817C`–`0x009491B7` (길이 `4,155` bytes)
- VA: `0x000000014094817C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00090C98`
- 디코드: `888`개 명령, `4,155/4,155` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **80**; 고유 호출 대상: **43**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x009481E5` → [HvpGetCellContextInitialize](../85/HvpGetCellContextInitialize_function_00855F10.md) (function, `0x00855F10`)
- `0x009481FB` → [HvpGetCellContextInitialize](../85/HvpGetCellContextInitialize_function_00855F10.md) (function, `0x00855F10`)
- `0x00948210` → [HvpGetCellContextInitialize](../85/HvpGetCellContextInitialize_function_00855F10.md) (function, `0x00855F10`)
- `0x00948250` → [CmpGetKcbAtLayerHeight](CmpGetKcbAtLayerHeight_function_00949210.md) (function, `0x00949210`)
- `0x00948265` → [CmpGetKcbAtLayerHeight](CmpGetKcbAtLayerHeight_function_00949210.md) (function, `0x00949210`)
- `0x009483CF` → [HvLockHiveFlusherShared](../84/HvLockHiveFlusherShared_function_0084F95C.md) (function, `0x0084F95C`)
- `0x0094842E` → [CmpNameSize](../85/CmpNameSize_function_0085ABC4.md) (function, `0x0085ABC4`)
- `0x00948469` → [HvAllocateCell](../85/HvAllocateCell_function_00859C94.md) (function, `0x00859C94`)
- `0x00948494` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0094853F` → [CmpCopyName](../85/CmpCopyName_function_0085AF98.md) (function, `0x0085AF98`)
- `0x0094856F` → [CmLockHiveSecurityExclusive](../84/CmLockHiveSecurityExclusive_function_0084B1A8.md) (function, `0x0084B1A8`)
- `0x009485A5` → [CmpGetSecurityDescriptorNodeEx](CmpGetSecurityDescriptorNodeEx_function_00949268.md) (function, `0x00949268`)
- `0x009485B7` → [CmUnlockHiveSecurity](../../pagecmrc/BC/CmUnlockHiveSecurity_function_00BC99C8.md) (function, `0x00BC99C8`)
- `0x009485D2` → [HvpMarkCellDirty](../85/HvpMarkCellDirty_function_00858080.md) (function, `0x00858080`)
- `0x009485FE` → [CmpAddSubKeyEx](../84/CmpAddSubKeyEx_function_0084C940.md) (function, `0x0084C940`)
- `0x0094865B` → [CmpRebuildKcbCacheFromNode](../84/CmpRebuildKcbCacheFromNode_function_0084C5A8.md) (function, `0x0084C5A8`)
- `0x00948688` → [CmLockHiveSecurityShared](../../pagecmrc/BC/CmLockHiveSecurityShared_function_00BC996C.md) (function, `0x00BC996C`)
- `0x0094869F` → [CmpFindSecurityCellCacheIndex](../../text/42/CmpFindSecurityCellCacheIndex_function_00428060.md) (function, `0x00428060`)
- `0x009486CE` → [CmUnlockHiveSecurity](../../pagecmrc/BC/CmUnlockHiveSecurity_function_00BC99C8.md) (function, `0x00BC99C8`)
- `0x00948702` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x0094871D` → [CmpUpdateKeyNodeAccessBits](../84/CmpUpdateKeyNodeAccessBits_function_0084864C.md) (function, `0x0084864C`)
- `0x00948780` → [CmpCleanUpSubKeyInfo](../84/CmpCleanUpSubKeyInfo_function_0084C6F4.md) (function, `0x0084C6F4`)
- `0x0094878F` → [HvUnlockHiveFlusherShared](../84/HvUnlockHiveFlusherShared_function_00848738.md) (function, `0x00848738`)
- `0x009487AF` → [CmpReportNotifyForKcbStack](../8C/CmpReportNotifyForKcbStack_function_008C718C.md) (function, `0x008C718C`)
- `0x009487CD` → [CmpRecordParseFailure](../85/CmpRecordParseFailure_function_00851280.md) (function, `0x00851280`)
- `0x00948841` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00948880` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x009488DC` → [CmpRecordParseFailure](../85/CmpRecordParseFailure_function_00851280.md) (function, `0x00851280`)
- `0x00948936` → [CmpGetSecurityCacheEntryForKcbStack](../8C/CmpGetSecurityCacheEntryForKcbStack_function_008C7580.md) (function, `0x008C7580`)
- `0x00948976` → [SeAssignSecurity](SeAssignSecurity_function_00949590.md) (function, `0x00949590`)
- `0x009489F3` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x00948A14` → [CmpGetSecurityCacheEntryForKcbStack](../8C/CmpGetSecurityCacheEntryForKcbStack_function_008C7580.md) (function, `0x008C7580`)
- `0x00948A34` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00948A3E` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00948A86` → [HvAllocateCell](../85/HvAllocateCell_function_00859C94.md) (function, `0x00859C94`)
- `0x00948AA6` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00948AC2` → [CmpRecordParseFailure](../85/CmpRecordParseFailure_function_00851280.md) (function, `0x00851280`)
- `0x00948B36` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00948B6E` → [CmAddLogForAction](../84/CmAddLogForAction_function_008445AC.md) (function, `0x008445AC`)
- `0x00948B8F` → [CmpAllocateUnitOfWork](../84/CmpAllocateUnitOfWork_function_00844BB0.md) (function, `0x00844BB0`)
- `0x00948BF4` → [CmpRecordParseFailure](../85/CmpRecordParseFailure_function_00851280.md) (function, `0x00851280`)
- `0x00948C08` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00948C64` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x00948C79` → [CmpNameSize](../85/CmpNameSize_function_0085ABC4.md) (function, `0x0085ABC4`)
- `0x00948C93` → [CmpMarkKeyDirty](../84/CmpMarkKeyDirty_function_0084B1FC.md) (function, `0x0084B1FC`)
- `0x00948CB3` → [HvpMarkCellDirty](../85/HvpMarkCellDirty_function_00858080.md) (function, `0x00858080`)
- `0x00948CD2` → [CmLockHiveSecurityExclusive](../84/CmLockHiveSecurityExclusive_function_0084B1A8.md) (function, `0x0084B1A8`)
- `0x00948D09` → [CmpGetSecurityDescriptorNodeEx](CmpGetSecurityDescriptorNodeEx_function_00949268.md) (function, `0x00949268`)
- `0x00948D1F` → [CmpFreeSecurityDescriptor](../84/CmpFreeSecurityDescriptor_function_00849E44.md) (function, `0x00849E44`)
- `0x00948D2F` → [CmUnlockHiveSecurity](../../pagecmrc/BC/CmUnlockHiveSecurity_function_00BC99C8.md) (function, `0x00BC99C8`)
- `0x00948D59` → [CmpCopyName](../85/CmpCopyName_function_0085AF98.md) (function, `0x0085AF98`)
- `0x00948D9F` → [CmpRebuildKcbCacheFromNode](../84/CmpRebuildKcbCacheFromNode_function_0084C5A8.md) (function, `0x0084C5A8`)
- `0x00948DC4` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x00948E14` → [CmpReportNotifyForKcbStack](../8C/CmpReportNotifyForKcbStack_function_008C718C.md) (function, `0x008C718C`)
- `0x00948E20` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00948E4A` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00948E50` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x00948E5A` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x00948E74` → [CmpRecordParseFailure](../85/CmpRecordParseFailure_function_00851280.md) (function, `0x00851280`)
- `0x00948ED5` → [CmpAttachToRegistryProcess](../../pagecmrc/BC/CmpAttachToRegistryProcess_function_00BC98E0.md) (function, `0x00BC98E0`)
- `0x00948F08` → [CmpIsSystemEntity](../8B/CmpIsSystemEntity_function_008B4E90.md) (function, `0x008B4E90`)
- `0x00948F39` → [CmpIsKeyStackDeleted](../84/CmpIsKeyStackDeleted_function_008426E0.md) (function, `0x008426E0`)
- `0x00948F59` → [CmpUndoDeleteKeyForTrans](CmpUndoDeleteKeyForTrans_function_0094A728.md) (function, `0x0094A728`)
- `0x00948F7F` → [CmpLogUnsupportedOperation](../9A/CmpLogUnsupportedOperation_function_009AEA40.md) (function, `0x009AEA40`)
- `0x00948F8C` → [HvLockHiveFlusherShared](../84/HvLockHiveFlusherShared_function_0084F95C.md) (function, `0x0084F95C`)
- `0x00948FA4` → [CmpLogUnsupportedOperation](../9A/CmpLogUnsupportedOperation_function_009AEA40.md) (function, `0x009AEA40`)
- `0x00948FFE` → [HvAllocateCell](../85/HvAllocateCell_function_00859C94.md) (function, `0x00859C94`)
- `0x0094903D` → [HvUnlockHiveFlusherShared](../84/HvUnlockHiveFlusherShared_function_00848738.md) (function, `0x00848738`)
- `0x00949052` → [CmpTransEnlistUowInKcb](../../text/48/CmpTransEnlistUowInKcb_function_0048F094.md) (function, `0x0048F094`)
- `0x00949067` → [CmpTransEnlistUowInCmTrans](../../text/48/CmpTransEnlistUowInCmTrans_function_0048B330.md) (function, `0x0048B330`)
- `0x00949111` → [CmUnlockHiveSecurity](../../pagecmrc/BC/CmUnlockHiveSecurity_function_00BC99C8.md) (function, `0x00BC99C8`)
- `0x0094911E` → [CmpRundownUnitOfWork](../87/CmpRundownUnitOfWork_function_0087497C.md) (function, `0x0087497C`)
- `0x0094912B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00949138` → [CmpRundownUnitOfWork](../87/CmpRundownUnitOfWork_function_0087497C.md) (function, `0x0087497C`)
- `0x00949145` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00949151` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00949178` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00949185` → [HvFreeCell](../85/HvFreeCell_function_0085A72C.md) (function, `0x0085A72C`)
- `0x009491A0` → [CmpFreeKeyByCell](../84/CmpFreeKeyByCell_function_0084AD70.md) (function, `0x0084AD70`)
- `0x009491AD` → [HvUnlockHiveFlusherShared](../84/HvUnlockHiveFlusherShared_function_00848738.md) (function, `0x00848738`)

### Direct callers
- [CmpDoBuildVirtualStack](../7E/CmpDoBuildVirtualStack_function_007EB4C4.md) at `0x007EB70B`
- [CmpDoParseKey](../85/CmpDoParseKey_function_0085F750.md) at `0x00860CEC`
- [CmpDoParseKey](../85/CmpDoParseKey_function_0085F750.md) at `0x00861403`
- [CmpDoParseKey](../85/CmpDoParseKey_function_0085F750.md) at `0x008616F2`

### Static image references
- `0x009482F2` → RVA `0x00E0ECA0` (`.data`; read)
- `0x009484AC` → RVA `0x00E0EC94` (`.data`; read)
- `0x0094893B` → RVA `0x00FC6AC0` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **16**
  - `0x00948494` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x009485B7` → [CmUnlockHiveSecurity](../../pagecmrc/BC/CmUnlockHiveSecurity_function_00BC99C8.md) (`PAGE` → `PAGECMRC`)
  - `0x00948688` → [CmLockHiveSecurityShared](../../pagecmrc/BC/CmLockHiveSecurityShared_function_00BC996C.md) (`PAGE` → `PAGECMRC`)
  - `0x0094869F` → [CmpFindSecurityCellCacheIndex](../../text/42/CmpFindSecurityCellCacheIndex_function_00428060.md) (`PAGE` → `.text`)
  - `0x009486CE` → [CmUnlockHiveSecurity](../../pagecmrc/BC/CmUnlockHiveSecurity_function_00BC99C8.md) (`PAGE` → `PAGECMRC`)
  - `0x00948AA6` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00948C08` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00948D2F` → [CmUnlockHiveSecurity](../../pagecmrc/BC/CmUnlockHiveSecurity_function_00BC99C8.md) (`PAGE` → `PAGECMRC`)
  - `0x00948E4A` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x00948ED5` → [CmpAttachToRegistryProcess](../../pagecmrc/BC/CmpAttachToRegistryProcess_function_00BC98E0.md) (`PAGE` → `PAGECMRC`)
  - `0x00949052` → [CmpTransEnlistUowInKcb](../../text/48/CmpTransEnlistUowInKcb_function_0048F094.md) (`PAGE` → `.text`)
  - `0x00949067` → [CmpTransEnlistUowInCmTrans](../../text/48/CmpTransEnlistUowInCmTrans_function_0048B330.md) (`PAGE` → `.text`)
  - `0x00949111` → [CmUnlockHiveSecurity](../../pagecmrc/BC/CmUnlockHiveSecurity_function_00BC99C8.md) (`PAGE` → `PAGECMRC`)
  - `0x0094912B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00949145` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00949151` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **11**
  - `0x009487E3` → [sub_00B258D8 + 0x2FB](../B2/Unknown_function_00B258D8.md) (`tail-transfer`)
  - `0x00948EC9` → [sub_00B258D8](../B2/Unknown_function_00B258D8.md) (`tail-transfer`)
  - `0x00948F40` → [sub_00B258D8 + 0x33](../B2/Unknown_function_00B258D8.md) (`tail-transfer`)
  - `0x00949007` → [sub_00B258D8 + 0x40](../B2/Unknown_function_00B258D8.md) (`tail-transfer`)
  - `0x00949070` → [sub_00B258D8 + 0xE4](../B2/Unknown_function_00B258D8.md) (`tail-transfer`)
  - `0x0094908B` → [sub_00B258D8 + 0x1BD](../B2/Unknown_function_00B258D8.md) (`tail-transfer`)
  - `0x009490A9` → [sub_00B258D8 + 0x210](../B2/Unknown_function_00B258D8.md) (`tail-transfer`)
  - `0x009490DA` → [sub_00B258D8 + 0x25C](../B2/Unknown_function_00B258D8.md) (`tail-transfer`)
  - `0x009490F8` → [sub_00B258D8 + 0x2A5](../B2/Unknown_function_00B258D8.md) (`tail-transfer`)
  - `0x00949172` → [sub_00B258D8 + 0x34F](../B2/Unknown_function_00B258D8.md) (`tail-transfer`)
  - `0x00949197` → [sub_00B258D8 + 0x35A](../B2/Unknown_function_00B258D8.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0094817C  4C 8B DC                        mov r11, rsp
0094817F  4D 89 4B 20                     mov qword ptr [r11 + 0x20], r9
00948183  4D 89 43 18                     mov qword ptr [r11 + 0x18], r8
00948187  49 89 53 10                     mov qword ptr [r11 + 0x10], rdx
0094818B  49 89 4B 08                     mov qword ptr [r11 + 8], rcx
0094818F  53                              push rbx
00948190  56                              push rsi
00948191  57                              push rdi
00948192  41 54                           push r12
00948194  41 55                           push r13
00948196  41 56                           push r14
00948198  41 57                           push r15
0094819A  48 81 EC E0 00 00 00            sub rsp, 0xe0
009481A1  4C 8B C2                        mov r8, rdx
009481A4  4C 8B C9                        mov r9, rcx
009481A7  48 8B B4 24 40 01 00 00         mov rsi, qword ptr [rsp + 0x140]
009481AF  33 FF                           xor edi, edi
009481B1  49 89 7B 90                     mov qword ptr [r11 - 0x70], rdi
009481B5  48 89 7C 24 70                  mov qword ptr [rsp + 0x70], rdi
009481BA  49 89 7B 80                     mov qword ptr [r11 - 0x80], rdi
009481BE  40 8A C7                        mov al, dil
009481C1  88 44 24 45                     mov byte ptr [rsp + 0x45], al
009481C5  88 44 24 41                     mov byte ptr [rsp + 0x41], al
009481C9  88 44 24 43                     mov byte ptr [rsp + 0x43], al
009481CD  40 88 7C 24 44                  mov byte ptr [rsp + 0x44], dil
009481D2  44 8B EF                        mov r13d, edi
009481D5  48 89 7C 24 60                  mov qword ptr [rsp + 0x60], rdi
009481DA  83 CA FF                        or edx, 0xffffffff
009481DD  89 54 24 4C                     mov dword ptr [rsp + 0x4c], edx
009481E1  49 8D 4B 90                     lea rcx, [r11 - 0x70]
009481E5  E8 26 DD F0 FF                  call 0x140855f10
009481EA  48 89 BC 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rdi
009481F2  89 54 24 50                     mov dword ptr [rsp + 0x50], edx
009481F6  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
009481FB  E8 10 DD F0 FF                  call 0x140855f10
00948200  48 89 BC 24 90 00 00 00         mov qword ptr [rsp + 0x90], rdi
00948208  48 8D 8C 24 98 00 00 00         lea rcx, [rsp + 0x98]
00948210  E8 FB DC F0 FF                  call 0x140855f10
00948215  40 88 7C 24 40                  mov byte ptr [rsp + 0x40], dil
0094821A  48 89 BC 24 88 00 00 00         mov qword ptr [rsp + 0x88], rdi
00948222  89 54 24 6C                     mov dword ptr [rsp + 0x6c], edx
00948226  48 89 BC 24 80 00 00 00         mov qword ptr [rsp + 0x80], rdi
0094822E  48 89 BC 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rdi
00948236  48 89 7C 24 78                  mov qword ptr [rsp + 0x78], rdi
0094823B  48 89 BC 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rdi
00948243  40 88 7C 24 42                  mov byte ptr [rsp + 0x42], dil
00948248  41 0F B7 51 02                  movzx edx, word ptr [r9 + 2]
0094824D  49 8B C9                        mov rcx, r9
00948250  E8 BB 0F 00 00                  call 0x140949210
00948255  48 8B D8                        mov rbx, rax
00948258  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
0094825D  41 0F B7 50 02                  movzx edx, word ptr [r8 + 2]
00948262  49 8B C8                        mov rcx, r8
00948265  E8 A6 0F 00 00                  call 0x140949210
0094826A  4C 8B F8                        mov r15, rax
0094826D  48 89 84 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], rax
00948275  4C 8B 70 20                     mov r14, qword ptr [rax + 0x20]
00948279  4C 89 B4 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], r14
00948281  4C 8B 8C 24 60 01 00 00         mov r9, qword ptr [rsp + 0x160]
00948289  4D 85 C9                        test r9, r9
0094828C  0F 85 2B 09 00 00               jne 0x140948bbd
00948292  F7 84 24 50 01 00 00 FC FF FF FF  test dword ptr [rsp + 0x150], 0xfffffffc
0094829D  0F 85 C1 0B 00 00               jne 0x140948e64
009482A3  41 BC 01 00 00 00               mov r12d, 1
009482A9  44 84 A4 24 50 01 00 00         test byte ptr [rsp + 0x150], r12b
009482B1  0F 85 25 07 00 00               jne 0x1409489dc
009482B7  41 8B 86 10 10 00 00            mov eax, dword ptr [r14 + 0x1010]
009482BE  A8 20                           test al, 0x20
009482C0  0F 85 16 07 00 00               jne 0x1409489dc
009482C6  44 8A D7                        mov r10b, dil
009482C9  8B 43 08                        mov eax, dword ptr [rbx + 8]
009482CC  84 C0                           test al, al
009482CE  0F 88 B0 0B 00 00               js 0x140948e84
009482D4  48 8B 43 20                     mov rax, qword ptr [rbx + 0x20]
009482D8  F7 80 A0 00 00 00 00 00 10 00   test dword ptr [rax + 0xa0], 0x100000
009482E2  0F 85 AC 0B 00 00               jne 0x140948e94
009482E8  44 38 63 41                     cmp byte ptr [rbx + 0x41], r12b
009482EC  0F 84 B2 0B 00 00               je 0x140948ea4
009482F2  40 38 3D A7 69 4C 00            cmp byte ptr [rip + 0x4c69a7], dil
009482F9  0F 84 B3 05 00 00               je 0x1409488b2
009482FF  F7 83 B8 00 00 00 00 00 00 01   test dword ptr [rbx + 0xb8], 0x1000000
00948309  41 8B C4                        mov eax, r12d
0094830C  0F 84 A0 05 00 00               je 0x1409488b2
00948312  BA 00 01 00 00                  mov edx, 0x100
00948317  0F B7 8C 24 48 01 00 00         movzx ecx, word ptr [rsp + 0x148]
0094831F  66 0B CA                        or cx, dx
00948322  85 C0                           test eax, eax
00948324  66 0F 44 8C 24 48 01 00 00      cmove cx, word ptr [rsp + 0x148]
0094832D  41 B8 00 02 00 00               mov r8d, 0x200
00948333  0F B7 D1                        movzx edx, cx
00948336  66 41 0B D0                     or dx, r8w
0094833A  F7 83 B8 00 00 00 00 00 00 02   test dword ptr [rbx + 0xb8], 0x2000000
00948344  66 0F 44 D1                     cmove dx, cx
00948348  66 89 54 24 4A                  mov word ptr [rsp + 0x4a], dx
0094834D  45 84 D2                        test r10b, r10b
00948350  0F 85 63 05 00 00               jne 0x1409488b9
00948356  8B 4E 18                        mov ecx, dword ptr [rsi + 0x18]
00948359  41 23 CC                        and ecx, r12d
0094835C  89 4C 24 68                     mov dword ptr [rsp + 0x68], ecx
00948360  4D 85 C9                        test r9, r9
00948363  0F 85 4B 0B 00 00               jne 0x140948eb4
00948369  8B 43 28                        mov eax, dword ptr [rbx + 0x28]
0094836C  C1 E8 1F                        shr eax, 0x1f
0094836F  41 3B C4                        cmp eax, r12d
00948372  0F 84 D0 06 00 00               je 0x140948a48
00948378  8B 86 A0 00 00 00               mov eax, dword ptr [rsi + 0xa0]
0094837E  41 84 C4                        test r12b, al
00948381  0F 84 47 0B 00 00               je 0x140948ece
00948387  F6 44 24 4A 02                  test byte ptr [rsp + 0x4a], 2
0094838C  0F 84 6B 05 00 00               je 0x1409488fd
00948392  48 8B 84 24 60 01 00 00         mov rax, qword ptr [rsp + 0x160]
0094839A  48 85 C0                        test rax, rax
0094839D  0F 85 8C 0B 00 00               jne 0x140948f2f
009483A3  8B 4C 24 68                     mov ecx, dword ptr [rsp + 0x68]
009483A7  48 85 C0                        test rax, rax
009483AA  41 0F 45 CC                     cmovne ecx, r12d
009483AE  89 8C 24 28 01 00 00            mov dword ptr [rsp + 0x128], ecx
009483B5  41 8B 47 28                     mov eax, dword ptr [r15 + 0x28]
009483B9  83 F8 FF                        cmp eax, -1
009483BC  0F 85 5F 08 00 00               jne 0x140948c21
009483C2  40 38 BC 24 58 01 00 00         cmp byte ptr [rsp + 0x158], dil
009483CA  75 12                           jne 0x1409483de
009483CC  49 8B CE                        mov rcx, r14
009483CF  E8 88 75 F0 FF                  call 0x14084f95c
009483D4  44 88 64 24 41                  mov byte ptr [rsp + 0x41], r12b
009483D9  44 88 64 24 43                  mov byte ptr [rsp + 0x43], r12b
009483DE  48 39 BC 24 60 01 00 00         cmp qword ptr [rsp + 0x160], rdi
009483E6  0F 85 A3 07 00 00               jne 0x140948b8f
009483EC  48 39 BB F0 00 00 00            cmp qword ptr [rbx + 0xf0], rdi
009483F3  0F 85 8A 0C 00 00               jne 0x140949083
009483F9  48 8D 8B F8 00 00 00            lea rcx, [rbx + 0xf8]
00948400  39 39                           cmp dword ptr [rcx], edi
00948402  0F 8C 99 0C 00 00               jl 0x1409490a1
00948408  49 8D 8F F8 00 00 00            lea rcx, [r15 + 0xf8]
0094840F  39 39                           cmp dword ptr [rcx], edi
00948411  0F 85 D9 0C 00 00               jne 0x1409490f0
00948417  49 8D 8F 08 01 00 00            lea rcx, [r15 + 0x108]
0094841E  39 39                           cmp dword ptr [rcx], edi
00948420  0F 85 AC 0C 00 00               jne 0x1409490d2
00948426  48 8B 8C 24 38 01 00 00         mov rcx, qword ptr [rsp + 0x138]
0094842E  E8 91 27 F1 FF                  call 0x14085abc4
00948433  0F B7 C0                        movzx eax, ax
00948436  83 C0 4C                        add eax, 0x4c
00948439  89 44 24 6C                     mov dword ptr [rsp + 0x6c], eax
0094843D  48 8D 8C 24 A8 00 00 00         lea rcx, [rsp + 0xa8]
00948445  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
0094844A  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
0094844F  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00948454  4C 8D 4C 24 4C                  lea r9, [rsp + 0x4c]
00948459  44 8B AC 24 28 01 00 00         mov r13d, dword ptr [rsp + 0x128]
00948461  45 8B C5                        mov r8d, r13d
00948464  8B D0                           mov edx, eax
00948466  49 8B CE                        mov rcx, r14
00948469  E8 26 18 F1 FF                  call 0x140859c94
0094846E  8B D8                           mov ebx, eax
00948470  85 C0                           test eax, eax
00948472  0F 88 71 07 00 00               js 0x140948be9
00948478  0F B7 46 04                     movzx eax, word ptr [rsi + 4]
0094847C  66 85 C0                        test ax, ax
0094847F  0F 85 DD 05 00 00               jne 0x140948a62
00948485  44 8B 44 24 6C                  mov r8d, dword ptr [rsp + 0x6c]
0094848A  33 D2                           xor edx, edx
0094848C  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
00948491  48 8B CB                        mov rcx, rbx
00948494  E8 A7 E7 D7 FF                  call 0x1406c6c40
00948499  0F B7 54 24 4A                  movzx edx, word ptr [rsp + 0x4a]
0094849E  F6 C2 02                        test dl, 2
009484A1  0F 85 83 05 00 00               jne 0x140948a2a
009484A7  66 C7 03 6E 6B                  mov word ptr [rbx], 0x6b6e
009484AC  8A 05 E2 67 4C 00               mov al, byte ptr [rip + 0x4c67e2]
009484B2  88 43 0C                        mov byte ptr [rbx + 0xc], al
009484B5  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
009484BA  80 79 41 03                     cmp byte ptr [rcx + 0x41], 3
009484BE  0F 84 39 05 00 00               je 0x1409489fd
009484C4  80 63 0D FC                     and byte ptr [rbx + 0xd], 0xfc
009484C8  66 89 53 02                     mov word ptr [rbx + 2], dx
009484CC  48 B8 14 00 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000014
009484D6  48 8B 00                        mov rax, qword ptr [rax]
009484D9  4C 8B 6C 24 60                  mov r13, qword ptr [rsp + 0x60]
009484DE  49 89 45 04                     mov qword ptr [r13 + 4], rax
009484E2  8B 41 28                        mov eax, dword ptr [rcx + 0x28]
009484E5  41 89 45 10                     mov dword ptr [r13 + 0x10], eax
009484E9  83 CA FF                        or edx, 0xffffffff
009484EC  41 89 55 1C                     mov dword ptr [r13 + 0x1c], edx
009484F0  41 89 55 20                     mov dword ptr [r13 + 0x20], edx
009484F4  41 89 55 28                     mov dword ptr [r13 + 0x28], edx
009484F8  41 89 55 2C                     mov dword ptr [r13 + 0x2c], edx
009484FC  8B 44 24 50                     mov eax, dword ptr [rsp + 0x50]
00948500  41 89 45 30                     mov dword ptr [r13 + 0x30], eax
00948504  0F B7 46 04                     movzx eax, word ptr [rsi + 4]
00948508  66 41 89 45 4A                  mov word ptr [r13 + 0x4a], ax
0094850D  89 54 24 50                     mov dword ptr [rsp + 0x50], edx
00948511  8B 91 B8 00 00 00               mov edx, dword ptr [rcx + 0xb8]
00948517  84 D2                           test dl, dl
00948519  79 15                           jns 0x140948530
0094851B  41 8B 45 34                     mov eax, dword ptr [r13 + 0x34]
0094851F  C1 E2 10                        shl edx, 0x10
00948522  33 D0                           xor edx, eax
00948524  81 E2 00 00 F0 00               and edx, 0xf00000
0094852A  33 D0                           xor edx, eax
0094852C  41 89 55 34                     mov dword ptr [r13 + 0x34], edx
00948530  49 8D 4D 4C                     lea rcx, [r13 + 0x4c]
00948534  48 8B 9C 24 38 01 00 00         mov rbx, qword ptr [rsp + 0x138]
0094853C  48 8B D3                        mov rdx, rbx
0094853F  E8 54 2A F1 FF                  call 0x14085af98
00948544  66 41 89 45 48                  mov word ptr [r13 + 0x48], ax
00948549  66 3B 03                        cmp ax, word ptr [rbx]
0094854C  73 06                           jae 0x140948554
0094854E  66 41 83 4D 02 20               or word ptr [r13 + 2], 0x20
00948554  0F B7 4C 24 4A                  movzx ecx, word ptr [rsp + 0x4a]
00948559  F6 C1 02                        test cl, 2
0094855C  0F 85 87 03 00 00               jne 0x1409488e9
00948562  44 88 64 24 45                  mov byte ptr [rsp + 0x45], r12b
00948567  F6 C1 02                        test cl, 2
0094856A  75 55                           jne 0x1409485c1
0094856C  49 8B CE                        mov rcx, r14
0094856F  E8 34 2C F0 FF                  call 0x14084b1a8
00948574  44 88 64 24 40                  mov byte ptr [rsp + 0x40], r12b
00948579  49 8D 45 2C                     lea rax, [r13 + 0x2c]
0094857D  8B 54 24 4C                     mov edx, dword ptr [rsp + 0x4c]
00948581  44 8B CA                        mov r9d, edx
00948584  41 C1 E9 1F                     shr r9d, 0x1f
00948588  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0094858D  40 88 7C 24 28                  mov byte ptr [rsp + 0x28], dil
00948592  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
0094859A  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0094859F  4D 8B C5                        mov r8, r13
009485A2  49 8B CE                        mov rcx, r14
009485A5  E8 BE 0C 00 00                  call 0x140949268
009485AA  8B D8                           mov ebx, eax
009485AC  85 C0                           test eax, eax
009485AE  0F 88 35 04 00 00               js 0x1409489e9
009485B4  49 8B CE                        mov rcx, r14
009485B7  E8 0C 14 28 00                  call 0x140bc99c8
009485BC  40 88 7C 24 40                  mov byte ptr [rsp + 0x40], dil
009485C1  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
009485C6  8B 50 28                        mov edx, dword ptr [rax + 0x28]
009485C9  45 33 C9                        xor r9d, r9d
009485CC  45 33 C0                        xor r8d, r8d
009485CF  49 8B CE                        mov rcx, r14
009485D2  E8 A9 FA F0 FF                  call 0x140858080
009485D7  8B D8                           mov ebx, eax
009485D9  85 C0                           test eax, eax
009485DB  0F 88 E1 01 00 00               js 0x1409487c2
009485E1  48 39 BC 24 60 01 00 00         cmp qword ptr [rsp + 0x160], rdi
009485E9  75 22                           jne 0x14094860d
009485EB  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
009485F0  8B 50 28                        mov edx, dword ptr [rax + 0x28]
009485F3  45 33 C9                        xor r9d, r9d
009485F6  44 8B 44 24 4C                  mov r8d, dword ptr [rsp + 0x4c]
009485FB  49 8B CE                        mov rcx, r14
009485FE  E8 3D 43 F0 FF                  call 0x14084c940
00948603  8B D8                           mov ebx, eax
00948605  85 C0                           test eax, eax
00948607  0F 88 D2 05 00 00               js 0x140948bdf
0094860D  44 88 64 24 42                  mov byte ptr [rsp + 0x42], r12b
00948612  8B 44 24 4C                     mov eax, dword ptr [rsp + 0x4c]
00948616  41 89 47 28                     mov dword ptr [r15 + 0x28], eax
0094861A  83 4C 24 4C FF                  or dword ptr [rsp + 0x4c], 0xffffffff
0094861F  48 8B 84 24 60 01 00 00         mov rax, qword ptr [rsp + 0x160]
00948627  49 89 87 F0 00 00 00            mov qword ptr [r15 + 0xf0], rax
0094862E  0F B7 5C 24 4A                  movzx ebx, word ptr [rsp + 0x4a]
00948633  F6 C3 40                        test bl, 0x40
00948636  75 10                           jne 0x140948648
00948638  41 8B 45 24                     mov eax, dword ptr [r13 + 0x24]
0094863C  41 89 47 60                     mov dword ptr [r15 + 0x60], eax
00948640  41 8B 45 28                     mov eax, dword ptr [r13 + 0x28]
00948644  41 89 47 64                     mov dword ptr [r15 + 0x64], eax
00948648  4D 01 A7 30 01 00 00            add qword ptr [r15 + 0x130], r12
0094864F  45 33 C9                        xor r9d, r9d
00948652  45 33 C0                        xor r8d, r8d
00948655  49 8B D5                        mov rdx, r13
00948658  49 8B CF                        mov rcx, r15
0094865B  E8 48 3F F0 FF                  call 0x14084c5a8
00948660  F6 C3 02                        test bl, 2
00948663  75 6E                           jne 0x1409486d3
00948665  41 8B 5D 2C                     mov ebx, dword ptr [r13 + 0x2c]
00948669  89 BC 24 28 01 00 00            mov dword ptr [rsp + 0x128], edi
00948670  83 FB FF                        cmp ebx, -1
00948673  0F 84 B1 07 00 00               je 0x140948e2a
00948679  49 8B 47 20                     mov rax, qword ptr [r15 + 0x20]
0094867D  48 89 84 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rax
00948685  48 8B C8                        mov rcx, rax
00948688  E8 DF 12 28 00                  call 0x140bc996c
0094868D  4C 8D 84 24 28 01 00 00         lea r8, [rsp + 0x128]
00948695  8B D3                           mov edx, ebx
00948697  48 8B 8C 24 B0 00 00 00         mov rcx, qword ptr [rsp + 0xb0]
0094869F  E8 BC F9 AD FF                  call 0x140428060
009486A4  84 C0                           test al, al
009486A6  0F 84 87 07 00 00               je 0x140948e33
009486AC  8B 94 24 28 01 00 00            mov edx, dword ptr [rsp + 0x128]
009486B3  48 03 D2                        add rdx, rdx
009486B6  48 8B 8C 24 B0 00 00 00         mov rcx, qword ptr [rsp + 0xb0]
009486BE  48 8B 81 60 07 00 00            mov rax, qword ptr [rcx + 0x760]
009486C5  48 8B 54 D0 08                  mov rdx, qword ptr [rax + rdx*8 + 8]
009486CA  49 89 57 58                     mov qword ptr [r15 + 0x58], rdx
009486CE  E8 F5 12 28 00                  call 0x140bc99c8
009486D3  48 39 BC 24 60 01 00 00         cmp qword ptr [rsp + 0x160], rdi
009486DB  0F 85 67 04 00 00               jne 0x140948b48
009486E1  48 8B 5C 24 58                  mov rbx, qword ptr [rsp + 0x58]
009486E6  8B 53 28                        mov edx, dword ptr [rbx + 0x28]
009486E9  48 8B 4B 20                     mov rcx, qword ptr [rbx + 0x20]
009486ED  4C 8D 84 24 98 00 00 00         lea r8, [rsp + 0x98]
009486F5  44 84 A1 8C 00 00 00            test byte ptr [rcx + 0x8c], r12b
009486FC  0F 84 F1 02 00 00               je 0x1409489f3
00948702  E8 59 C5 F0 FF                  call 0x140854c60
00948707  4C 8B E8                        mov r13, rax
0094870A  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
00948712  44 8B 43 28                     mov r8d, dword ptr [rbx + 0x28]
00948716  48 8B D0                        mov rdx, rax
00948719  48 8B 4B 20                     mov rcx, qword ptr [rbx + 0x20]
0094871D  E8 2A FF EF FF                  call 0x14084864c
00948722  48 B8 14 00 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000014
0094872C  48 8B 00                        mov rax, qword ptr [rax]
0094872F  49 89 45 04                     mov qword ptr [r13 + 4], rax
00948733  48 8B 94 24 38 01 00 00         mov rdx, qword ptr [rsp + 0x138]
0094873B  0F B7 12                        movzx edx, word ptr [rdx]
0094873E  41 8B 45 34                     mov eax, dword ptr [r13 + 0x34]
00948742  0F B7 C8                        movzx ecx, ax
00948745  3B CA                           cmp ecx, edx
00948747  73 05                           jae 0x14094874e
00948749  66 41 89 55 34                  mov word ptr [r13 + 0x34], dx
0094874E  0F B7 46 04                     movzx eax, word ptr [rsi + 4]
00948752  41 39 45 38                     cmp dword ptr [r13 + 0x38], eax
00948756  0F 82 6D 09 00 00               jb 0x1409490c9
0094875C  4C 01 A3 30 01 00 00            add qword ptr [rbx + 0x130], r12
00948763  41 0F B7 45 34                  movzx eax, word ptr [r13 + 0x34]
00948768  66 89 83 B0 00 00 00            mov word ptr [rbx + 0xb0], ax
0094876F  49 8B 45 04                     mov rax, qword ptr [r13 + 4]
00948773  48 89 83 A8 00 00 00            mov qword ptr [rbx + 0xa8], rax
0094877A  41 8A D4                        mov dl, r12b
0094877D  48 8B CB                        mov rcx, rbx
00948780  E8 6F 3F F0 FF                  call 0x14084c6f4
00948785  40 38 7C 24 41                  cmp byte ptr [rsp + 0x41], dil
0094878A  74 0D                           je 0x140948799
0094878C  49 8B CE                        mov rcx, r14
0094878F  E8 A4 FF EF FF                  call 0x140848738
00948794  40 88 7C 24 41                  mov byte ptr [rsp + 0x41], dil
00948799  45 33 C9                        xor r9d, r9d
0094879C  45 8B C4                        mov r8d, r12d
0094879F  48 8B 94 24 60 01 00 00         mov rdx, qword ptr [rsp + 0x160]
009487A7  48 8B 8C 24 20 01 00 00         mov rcx, qword ptr [rsp + 0x120]
009487AF  E8 D8 E9 F7 FF                  call 0x1408c718c
009487B4  8B DF                           mov ebx, edi
009487B6  40 88 7C 24 42                  mov byte ptr [rsp + 0x42], dil
009487BB  4C 8B 6C 24 60                  mov r13, qword ptr [rsp + 0x60]
009487C0  EB 10                           jmp 0x1409487d2
009487C2  BA 00 22 04 00                  mov edx, 0x42200
009487C7  44 8B C0                        mov r8d, eax
009487CA  48 8B CE                        mov rcx, rsi
009487CD  E8 AE 8A F0 FF                  call 0x140851280
009487D2  8A 44 24 40                     mov al, byte ptr [rsp + 0x40]
009487D6  84 C0                           test al, al
009487D8  0F 85 30 09 00 00               jne 0x14094910e
009487DE  40 38 7C 24 42                  cmp byte ptr [rsp + 0x42], dil
009487E3  0F 85 EA D3 1D 00               jne 0x140b25bd3
009487E9  4C 8B 7C 24 78                  mov r15, qword ptr [rsp + 0x78]
009487EE  4D 85 FF                        test r15, r15
009487F1  0F 85 24 09 00 00               jne 0x14094911b
009487F7  4C 8B BC 24 80 00 00 00         mov r15, qword ptr [rsp + 0x80]
009487FF  4D 85 FF                        test r15, r15
00948802  0F 85 2D 09 00 00               jne 0x140949135
00948808  4C 8B BC 24 88 00 00 00         mov r15, qword ptr [rsp + 0x88]
00948810  4D 85 FF                        test r15, r15
00948813  0F 85 76 01 00 00               jne 0x14094898f
00948819  48 39 BC 24 90 00 00 00         cmp qword ptr [rsp + 0x90], rdi
00948821  74 23                           je 0x140948846
00948823  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
00948828  48 8B 48 20                     mov rcx, qword ptr [rax + 0x20]
0094882C  48 8D 94 24 98 00 00 00         lea rdx, [rsp + 0x98]
00948834  44 84 A1 8C 00 00 00            test byte ptr [rcx + 0x8c], r12b
0094883B  0F 85 F3 01 00 00               jne 0x140948a34
00948841  E8 FA D6 F0 FF                  call 0x140855f40
00948846  48 39 BC 24 A0 00 00 00         cmp qword ptr [rsp + 0xa0], rdi
0094884E  0F 85 0F 09 00 00               jne 0x140949163
00948854  8B 54 24 50                     mov edx, dword ptr [rsp + 0x50]
00948858  83 CE FF                        or esi, 0xffffffff
0094885B  3B D6                           cmp edx, esi
0094885D  0F 85 1F 09 00 00               jne 0x140949182
00948863  4D 85 ED                        test r13, r13
00948866  74 1D                           je 0x140948885
00948868  48 8D 94 24 A8 00 00 00         lea rdx, [rsp + 0xa8]
00948870  49 8B CE                        mov rcx, r14
00948873  45 84 A6 8C 00 00 00            test byte ptr [r14 + 0x8c], r12b
0094887A  0F 85 BE 01 00 00               jne 0x140948a3e
00948880  E8 BB D6 F0 FF                  call 0x140855f40
00948885  8B 54 24 4C                     mov edx, dword ptr [rsp + 0x4c]
00948889  3B D6                           cmp edx, esi
0094888B  0F 85 FE 08 00 00               jne 0x14094918f
00948891  40 38 7C 24 41                  cmp byte ptr [rsp + 0x41], dil
00948896  0F 85 0E 09 00 00               jne 0x1409491aa
0094889C  8B C3                           mov eax, ebx
0094889E  48 81 C4 E0 00 00 00            add rsp, 0xe0
009488A5  41 5F                           pop r15
009488A7  41 5E                           pop r14
009488A9  41 5D                           pop r13
009488AB  41 5C                           pop r12
009488AD  5F                              pop rdi
009488AE  5E                              pop rsi
009488AF  5B                              pop rbx
009488B0  C3                              ret
009488B1  CC                              int3
009488B2  8B C7                           mov eax, edi
009488B4  E9 59 FA FF FF                  jmp 0x140948312
009488B9  48 8B 84 24 30 01 00 00         mov rax, qword ptr [rsp + 0x130]
009488C1  48 39 78 40                     cmp qword ptr [rax + 0x40], rdi
009488C5  0F 84 8B FA FF FF               je 0x140948356
009488CB  41 B8 22 00 00 C0               mov r8d, 0xc0000022
009488D1  BA 00 05 04 00                  mov edx, 0x40500
009488D6  41 8B D8                        mov ebx, r8d
009488D9  48 8B CE                        mov rcx, rsi
009488DC  E8 9F 89 F0 FF                  call 0x140851280
009488E1  40 8A C7                        mov al, dil
009488E4  E9 ED FE FF FF                  jmp 0x1409487d6
009488E9  48 8B 46 30                     mov rax, qword ptr [rsi + 0x30]
009488ED  49 89 45 24                     mov qword ptr [r13 + 0x24], rax
009488F1  8B 46 28                        mov eax, dword ptr [rsi + 0x28]
009488F4  41 89 45 1C                     mov dword ptr [r13 + 0x1c], eax
009488F8  E9 65 FC FF FF                  jmp 0x140948562
009488FD  45 84 D2                        test r10b, r10b
00948900  0F 85 00 01 00 00               jne 0x140948a06
00948906  41 F7 87 B8 00 00 00 00 00 00 02  test dword ptr [r15 + 0xb8], 0x2000000
00948911  0F 85 DC 05 00 00               jne 0x140948ef3
00948917  48 8B 84 24 30 01 00 00         mov rax, qword ptr [rsp + 0x130]
0094891F  48 8B 58 40                     mov rbx, qword ptr [rax + 0x40]
00948923  45 33 C0                        xor r8d, r8d
00948926  48 8B 94 24 60 01 00 00         mov rdx, qword ptr [rsp + 0x160]
0094892E  48 8B 8C 24 20 01 00 00         mov rcx, qword ptr [rsp + 0x120]
00948936  E8 45 EC F7 FF                  call 0x1408c7580
0094893B  4C 8B 05 7E E1 67 00            mov r8, qword ptr [rip + 0x67e17e]
00948942  4D 8D 48 4C                     lea r9, [r8 + 0x4c]
00948946  4C 8B 94 24 30 01 00 00         mov r10, qword ptr [rsp + 0x130]
0094894E  49 83 C2 20                     add r10, 0x20
00948952  48 8D 48 20                     lea rcx, [rax + 0x20]
00948956  41 8B 40 64                     mov eax, dword ptr [r8 + 0x64]
0094895A  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
0094895E  4C 89 4C 24 28                  mov qword ptr [rsp + 0x28], r9
00948963  4C 89 54 24 20                  mov qword ptr [rsp + 0x20], r10
00948968  45 8A CC                        mov r9b, r12b
0094896B  4C 8D 84 24 88 00 00 00         lea r8, [rsp + 0x88]
00948973  48 8B D3                        mov rdx, rbx
00948976  E8 15 0C 00 00                  call 0x140949590
0094897B  8B D8                           mov ebx, eax
0094897D  85 C0                           test eax, eax
0094897F  0F 88 9D 05 00 00               js 0x140948f22
00948985  48 8B 5C 24 58                  mov rbx, qword ptr [rsp + 0x58]
0094898A  E9 03 FA FF FF                  jmp 0x140948392
0094898F  40 38 7C 24 44                  cmp byte ptr [rsp + 0x44], dil
00948994  0F 85 7F FE FF FF               jne 0x140948819
0094899A  8B 06                           mov eax, dword ptr [rsi]
0094899C  41 84 C4                        test r12b, al
0094899F  74 0B                           je 0x1409489ac
009489A1  8B 46 18                        mov eax, dword ptr [rsi + 0x18]
009489A4  A8 04                           test al, 4
009489A6  0F 85 57 02 00 00               jne 0x140948c03
009489AC  48 8B 94 24 30 01 00 00         mov rdx, qword ptr [rsp + 0x130]
009489B4  48 8B 72 48                     mov rsi, qword ptr [rdx + 0x48]
009489B8  F7 42 0C 00 00 00 04            test dword ptr [rdx + 0xc], 0x4000000
009489BF  75 0D                           jne 0x1409489ce
009489C1  48 8B 4E 30                     mov rcx, qword ptr [rsi + 0x30]
009489C5  48 85 C9                        test rcx, rcx
009489C8  0F 85 81 07 00 00               jne 0x14094914f
009489CE  0F BA 72 0C 1A                  btr dword ptr [rdx + 0xc], 0x1a
009489D3  4C 89 7E 30                     mov qword ptr [rsi + 0x30], r15
009489D7  E9 3D FE FF FF                  jmp 0x140948819
009489DC  45 8A D4                        mov r10b, r12b
009489DF  44 88 64 24 44                  mov byte ptr [rsp + 0x44], r12b
009489E4  E9 E0 F8 FF FF                  jmp 0x1409482c9
009489E9  BA 00 21 04 00                  mov edx, 0x42100
009489EE  E9 D4 FD FF FF                  jmp 0x1409487c7
009489F3  E8 B8 C2 F0 FF                  call 0x140854cb0
009489F8  E9 0A FD FF FF                  jmp 0x140948707
009489FD  80 4B 0D 03                     or byte ptr [rbx + 0xd], 3
00948A01  E9 C2 FA FF FF                  jmp 0x1409484c8
00948A06  45 33 C0                        xor r8d, r8d
00948A09  49 8B D1                        mov rdx, r9
00948A0C  48 8B 8C 24 20 01 00 00         mov rcx, qword ptr [rsp + 0x120]
00948A14  E8 67 EB F7 FF                  call 0x1408c7580
00948A19  48 83 C0 20                     add rax, 0x20
00948A1D  48 89 84 24 88 00 00 00         mov qword ptr [rsp + 0x88], rax
00948A25  E9 68 F9 FF FF                  jmp 0x140948392
00948A2A  66 C7 03 6C 6B                  mov word ptr [rbx], 0x6b6c
00948A2F  E9 78 FA FF FF                  jmp 0x1409484ac
00948A34  E8 E7 41 F1 FF                  call 0x14085cc20
00948A39  E9 08 FE FF FF                  jmp 0x140948846
00948A3E  E8 DD 41 F1 FF                  call 0x14085cc20
00948A43  E9 3D FE FF FF                  jmp 0x140948885
00948A48  85 C9                           test ecx, ecx
00948A4A  0F 85 28 F9 FF FF               jne 0x140948378
00948A50  BB 81 01 00 C0                  mov ebx, 0xc0000181
00948A55  44 8B C3                        mov r8d, ebx
00948A58  BA 00 06 04 00                  mov edx, 0x40600
00948A5D  E9 77 FE FF FF                  jmp 0x1409488d9
00948A62  8B D0                           mov edx, eax
00948A64  48 8D 44 24 70                  lea rax, [rsp + 0x70]
00948A69  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00948A6E  48 8D 84 24 A0 00 00 00         lea rax, [rsp + 0xa0]
00948A76  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00948A7B  4C 8D 4C 24 50                  lea r9, [rsp + 0x50]
00948A80  45 8B C5                        mov r8d, r13d
00948A83  49 8B CE                        mov rcx, r14
00948A86  E8 09 12 F1 FF                  call 0x140859c94
00948A8B  8B D8                           mov ebx, eax
00948A8D  85 C0                           test eax, eax
00948A8F  0F 88 85 01 00 00               js 0x140948c1a
00948A95  44 0F B7 46 04                  movzx r8d, word ptr [rsi + 4]
00948A9A  48 8B 56 08                     mov rdx, qword ptr [rsi + 8]
00948A9E  48 8B 8C 24 A0 00 00 00         mov rcx, qword ptr [rsp + 0xa0]
00948AA6  E8 95 DD D7 FF                  call 0x1406c6840
00948AAB  EB 74                           jmp 0x140948b21
00948AAD  8B D8                           mov ebx, eax
00948AAF  44 8B C0                        mov r8d, eax
00948AB2  BA 00 20 04 00                  mov edx, 0x42000
00948AB7  48 8B B4 24 40 01 00 00         mov rsi, qword ptr [rsp + 0x140]
00948ABF  48 8B CE                        mov rcx, rsi
00948AC2  E8 B9 87 F0 FF                  call 0x140851280
00948AC7  33 FF                           xor edi, edi
00948AC9  44 8D 67 01                     lea r12d, [rdi + 1]
00948ACD  4C 8B BC 24 C8 00 00 00         mov r15, qword ptr [rsp + 0xc8]
00948AD5  4C 8B B4 24 D0 00 00 00         mov r14, qword ptr [rsp + 0xd0]
00948ADD  4C 8B 6C 24 60                  mov r13, qword ptr [rsp + 0x60]
00948AE2  40 88 7C 24 45                  mov byte ptr [rsp + 0x45], dil
00948AE7  48 89 BC 24 90 00 00 00         mov qword ptr [rsp + 0x90], rdi
00948AEF  8A 44 24 43                     mov al, byte ptr [rsp + 0x43]
00948AF3  88 44 24 41                     mov byte ptr [rsp + 0x41], al
00948AF7  48 8B 84 24 B8 00 00 00         mov rax, qword ptr [rsp + 0xb8]
00948AFF  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
00948B07  48 8B 84 24 C0 00 00 00         mov rax, qword ptr [rsp + 0xc0]
00948B0F  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
00948B14  40 88 7C 24 42                  mov byte ptr [rsp + 0x42], dil
00948B19  40 8A C7                        mov al, dil
00948B1C  E9 B5 FC FF FF                  jmp 0x1409487d6
00948B21  48 8D 54 24 70                  lea rdx, [rsp + 0x70]
00948B26  49 8B CE                        mov rcx, r14
00948B29  45 84 A6 8C 00 00 00            test byte ptr [r14 + 0x8c], r12b
00948B30  0F 85 EA 02 00 00               jne 0x140948e20
00948B36  E8 05 D4 F0 FF                  call 0x140855f40
00948B3B  48 89 BC 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rdi
00948B43  E9 3D F9 FF FF                  jmp 0x140948485
00948B48  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
00948B4D  89 79 44                        mov dword ptr [rcx + 0x44], edi
00948B50  8B 44 24 68                     mov eax, dword ptr [rsp + 0x68]
00948B54  89 41 48                        mov dword ptr [rcx + 0x48], eax
00948B57  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
00948B5F  48 89 41 50                     mov qword ptr [rcx + 0x50], rax
00948B63  44 89 60 44                     mov dword ptr [rax + 0x44], r12d
00948B67  4C 89 78 58                     mov qword ptr [rax + 0x58], r15
00948B6B  41 8B D4                        mov edx, r12d
00948B6E  E8 39 BA EF FF                  call 0x1408445ac
00948B73  8B D8                           mov ebx, eax
00948B75  85 C0                           test eax, eax
00948B77  0F 88 42 05 00 00               js 0x1409490bf
00948B7D  48 89 7C 24 78                  mov qword ptr [rsp + 0x78], rdi
00948B82  48 89 BC 24 80 00 00 00         mov qword ptr [rsp + 0x80], rdi
00948B8A  E9 52 FB FF FF                  jmp 0x1409486e1
00948B8F  E8 1C C0 EF FF                  call 0x140844bb0
00948B94  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
00948B9C  48 89 84 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rax
00948BA4  48 85 C0                        test rax, rax
00948BA7  0F 85 9F 04 00 00               jne 0x14094904c
00948BAD  41 B8 9A 00 00 C0               mov r8d, 0xc000009a
00948BB3  BA 00 0F 04 00                  mov edx, 0x40f00
00948BB8  E9 19 FD FF FF                  jmp 0x1409488d6
00948BBD  41 8B 86 A0 00 00 00            mov eax, dword ptr [r14 + 0xa0]
00948BC4  A8 02                           test al, 2
00948BC6  0F 84 C6 F6 FF FF               je 0x140948292
00948BCC  41 B8 01 00 19 C0               mov r8d, 0xc0190001
00948BD2  41 8B D8                        mov ebx, r8d
00948BD5  BA 00 01 04 00                  mov edx, 0x40100
00948BDA  E9 92 02 00 00                  jmp 0x140948e71
00948BDF  BA 00 23 04 00                  mov edx, 0x42300
00948BE4  E9 DE FB FF FF                  jmp 0x1409487c7
00948BE9  BA 00 1E 04 00                  mov edx, 0x41e00
00948BEE  44 8B C0                        mov r8d, eax
00948BF1  48 8B CE                        mov rcx, rsi
00948BF4  E8 87 86 F0 FF                  call 0x140851280
00948BF9  4C 8B 6C 24 60                  mov r13, qword ptr [rsp + 0x60]
00948BFE  E9 DE FC FF FF                  jmp 0x1409488e1
00948C03  33 D2                           xor edx, edx
00948C05  49 8B CF                        mov rcx, r15
00948C08  E8 63 9C 23 00                  call 0x140b82870
00948C0D  48 89 BC 24 88 00 00 00         mov qword ptr [rsp + 0x88], rdi
00948C15  E9 FF FB FF FF                  jmp 0x140948819
00948C1A  BA 00 1F 04 00                  mov edx, 0x41f00
00948C1F  EB CD                           jmp 0x140948bee
00948C21  C1 E8 1F                        shr eax, 0x1f
00948C24  3B C8                           cmp ecx, eax
00948C26  0F 85 4E 03 00 00               jne 0x140948f7a
00948C2C  41 8B 47 28                     mov eax, dword ptr [r15 + 0x28]
00948C30  C1 E8 1F                        shr eax, 0x1f
00948C33  89 84 24 60 01 00 00            mov dword ptr [rsp + 0x160], eax
00948C3A  40 38 BC 24 58 01 00 00         cmp byte ptr [rsp + 0x158], dil
00948C42  0F 84 41 03 00 00               je 0x140948f89
00948C48  41 8B 57 28                     mov edx, dword ptr [r15 + 0x28]
00948C4C  4C 8D 84 24 A8 00 00 00         lea r8, [rsp + 0xa8]
00948C54  49 8B CE                        mov rcx, r14
00948C57  45 84 A6 8C 00 00 00            test byte ptr [r14 + 0x8c], r12b
00948C5E  0F 84 EC 01 00 00               je 0x140948e50
00948C64  E8 F7 BF F0 FF                  call 0x140854c60
00948C69  4C 8B E8                        mov r13, rax
00948C6C  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00948C71  48 8B 8C 24 38 01 00 00         mov rcx, qword ptr [rsp + 0x138]
00948C79  E8 46 1F F1 FF                  call 0x14085abc4
00948C7E  66 41 3B 45 48                  cmp ax, word ptr [r13 + 0x48]
00948C83  0F 85 18 03 00 00               jne 0x140948fa1
00948C89  45 33 C0                        xor r8d, r8d
00948C8C  41 8B 57 28                     mov edx, dword ptr [r15 + 0x28]
00948C90  49 8B CE                        mov rcx, r14
00948C93  E8 64 25 F0 FF                  call 0x14084b1fc
00948C98  8B D8                           mov ebx, eax
00948C9A  85 C0                           test eax, eax
00948C9C  0F 88 19 03 00 00               js 0x140948fbb
00948CA2  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
00948CA7  8B 52 28                        mov edx, dword ptr [rdx + 0x28]
00948CAA  45 33 C9                        xor r9d, r9d
00948CAD  45 33 C0                        xor r8d, r8d
00948CB0  49 8B CE                        mov rcx, r14
00948CB3  E8 C8 F3 F0 FF                  call 0x140858080
00948CB8  8B D8                           mov ebx, eax
00948CBA  85 C0                           test eax, eax
00948CBC  0F 88 06 03 00 00               js 0x140948fc8
00948CC2  0F B7 46 04                     movzx eax, word ptr [rsi + 4]
00948CC6  66 85 C0                        test ax, ax
00948CC9  0F 85 06 03 00 00               jne 0x140948fd5
00948CCF  49 8B CE                        mov rcx, r14
00948CD2  E8 D1 24 F0 FF                  call 0x14084b1a8
00948CD7  44 88 64 24 40                  mov byte ptr [rsp + 0x40], r12b
00948CDC  41 8B 57 28                     mov edx, dword ptr [r15 + 0x28]
00948CE0  44 8B CA                        mov r9d, edx
00948CE3  41 C1 E9 1F                     shr r9d, 0x1f
00948CE7  48 8D 44 24 6C                  lea rax, [rsp + 0x6c]
00948CEC  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00948CF1  44 88 64 24 28                  mov byte ptr [rsp + 0x28], r12b
00948CF6  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
00948CFE  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00948D03  4D 8B C5                        mov r8, r13
00948D06  49 8B CE                        mov rcx, r14
00948D09  E8 5A 05 00 00                  call 0x140949268
00948D0E  8B D8                           mov ebx, eax
00948D10  85 C0                           test eax, eax
00948D12  0F 88 02 03 00 00               js 0x14094901a
00948D18  41 8B 57 28                     mov edx, dword ptr [r15 + 0x28]
00948D1C  49 8B CE                        mov rcx, r14
00948D1F  E8 20 11 F0 FF                  call 0x140849e44
00948D24  8B 44 24 6C                     mov eax, dword ptr [rsp + 0x6c]
00948D28  41 89 45 2C                     mov dword ptr [r13 + 0x2c], eax
00948D2C  49 8B CE                        mov rcx, r14
00948D2F  E8 94 0C 28 00                  call 0x140bc99c8
00948D34  8B 44 24 50                     mov eax, dword ptr [rsp + 0x50]
00948D38  41 89 45 30                     mov dword ptr [r13 + 0x30], eax
00948D3C  0F B7 46 04                     movzx eax, word ptr [rsi + 4]
00948D40  66 41 89 45 4A                  mov word ptr [r13 + 0x4a], ax
00948D45  83 4C 24 50 FF                  or dword ptr [rsp + 0x50], 0xffffffff
00948D4A  49 8D 4D 4C                     lea rcx, [r13 + 0x4c]
00948D4E  48 8B 9C 24 38 01 00 00         mov rbx, qword ptr [rsp + 0x138]
00948D56  48 8B D3                        mov rdx, rbx
00948D59  E8 3A 22 F1 FF                  call 0x14085af98
00948D5E  41 80 4D 0D 03                  or byte ptr [r13 + 0xd], 3
00948D63  0F B7 4C 24 4A                  movzx ecx, word ptr [rsp + 0x4a]
00948D68  66 41 89 4D 02                  mov word ptr [r13 + 2], cx
00948D6D  0F B7 03                        movzx eax, word ptr [rbx]
00948D70  66 41 39 45 48                  cmp word ptr [r13 + 0x48], ax
00948D75  0F 82 A9 02 00 00               jb 0x140949024
00948D7B  48 B8 14 00 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000014
00948D85  48 8B 18                        mov rbx, qword ptr [rax]
00948D88  49 89 5D 04                     mov qword ptr [r13 + 4], rbx
00948D8C  4D 01 A7 30 01 00 00            add qword ptr [r15 + 0x130], r12
00948D93  45 33 C9                        xor r9d, r9d
00948D96  45 33 C0                        xor r8d, r8d
00948D99  49 8B D5                        mov rdx, r13
00948D9C  49 8B CF                        mov rcx, r15
00948D9F  E8 04 38 F0 FF                  call 0x14084c5a8
00948DA4  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
00948DA9  8B 50 28                        mov edx, dword ptr [rax + 0x28]
00948DAC  4C 8D 84 24 98 00 00 00         lea r8, [rsp + 0x98]
00948DB4  49 8B CE                        mov rcx, r14
00948DB7  45 84 A6 8C 00 00 00            test byte ptr [r14 + 0x8c], r12b
00948DBE  0F 84 96 00 00 00               je 0x140948e5a
00948DC4  E8 97 BE F0 FF                  call 0x140854c60
00948DC9  48 8B C8                        mov rcx, rax
00948DCC  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
00948DD4  48 89 58 04                     mov qword ptr [rax + 4], rbx
00948DD8  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
00948DDD  48 89 98 A8 00 00 00            mov qword ptr [rax + 0xa8], rbx
00948DE4  4C 01 A0 30 01 00 00            add qword ptr [rax + 0x130], r12
00948DEB  41 0F B7 45 4A                  movzx eax, word ptr [r13 + 0x4a]
00948DF0  39 41 38                        cmp dword ptr [rcx + 0x38], eax
00948DF3  0F 82 39 02 00 00               jb 0x140949032
00948DF9  40 38 7C 24 41                  cmp byte ptr [rsp + 0x41], dil
00948DFE  0F 85 36 02 00 00               jne 0x14094903a
00948E04  45 33 C9                        xor r9d, r9d
00948E07  45 8B C4                        mov r8d, r12d
00948E0A  33 D2                           xor edx, edx
00948E0C  48 8B 8C 24 20 01 00 00         mov rcx, qword ptr [rsp + 0x120]
00948E14  E8 73 E3 F7 FF                  call 0x1408c718c
00948E19  8B DF                           mov ebx, edi
00948E1B  E9 D9 FD FF FF                  jmp 0x140948bf9
00948E20  E8 FB 3D F1 FF                  call 0x14085cc20
00948E25  E9 11 FD FF FF                  jmp 0x140948b3b
00948E2A  49 89 7F 58                     mov qword ptr [r15 + 0x58], rdi
00948E2E  E9 A0 F8 FF FF                  jmp 0x1409486d3
00948E33  49 89 7F 58                     mov qword ptr [r15 + 0x58], rdi
00948E37  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00948E3C  4D 8B CF                        mov r9, r15
00948E3F  4D 8B C4                        mov r8, r12
00948E42  BA 04 00 00 00                  mov edx, 4
00948E47  8D 4A 4D                        lea ecx, [rdx + 0x4d]
00948E4A  E8 11 48 BB FF                  call 0x1404fd660
00948E4F  CC                              int3
00948E50  E8 5B BE F0 FF                  call 0x140854cb0
00948E55  E9 0F FE FF FF                  jmp 0x140948c69
00948E5A  E8 51 BE F0 FF                  call 0x140854cb0
00948E5F  E9 65 FF FF FF                  jmp 0x140948dc9
00948E64  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00948E69  44 8B C3                        mov r8d, ebx
00948E6C  BA 80 01 04 00                  mov edx, 0x40180
00948E71  48 8B CE                        mov rcx, rsi
00948E74  E8 07 84 F0 FF                  call 0x140851280
00948E79  41 BC 01 00 00 00               mov r12d, 1
00948E7F  E9 5D FA FF FF                  jmp 0x1409488e1
00948E84  41 B8 22 00 00 C0               mov r8d, 0xc0000022
00948E8A  BA 00 02 04 00                  mov edx, 0x40200
00948E8F  E9 42 FA FF FF                  jmp 0x1409488d6
00948E94  41 B8 22 00 00 C0               mov r8d, 0xc0000022
00948E9A  BA 00 03 04 00                  mov edx, 0x40300
00948E9F  E9 32 FA FF FF                  jmp 0x1409488d6
00948EA4  41 B8 22 00 00 C0               mov r8d, 0xc0000022
00948EAA  BA 00 04 04 00                  mov edx, 0x40400
00948EAF  E9 22 FA FF FF                  jmp 0x1409488d6
00948EB4  48 39 BB F0 00 00 00            cmp qword ptr [rbx + 0xf0], rdi
00948EBB  0F 84 A8 F4 FF FF               je 0x140948369
00948EC1  48 89 BC 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], rdi
00948EC9  E9 0A CA 1D 00                  jmp 0x140b258d8
00948ECE  48 8D 8E A8 00 00 00            lea rcx, [rsi + 0xa8]
00948ED5  E8 06 0A 28 00                  call 0x140bc98e0
00948EDA  44 09 A6 A0 00 00 00            or dword ptr [rsi + 0xa0], r12d
00948EE1  4C 8B 8C 24 60 01 00 00         mov r9, qword ptr [rsp + 0x160]
00948EE9  44 8A 54 24 44                  mov r10b, byte ptr [rsp + 0x44]
00948EEE  E9 94 F4 FF FF                  jmp 0x140948387
00948EF3  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00948EFC  8A 88 32 02 00 00               mov cl, byte ptr [rax + 0x232]
00948F02  4C 8D 46 10                     lea r8, [rsi + 0x10]
00948F06  33 D2                           xor edx, edx
00948F08  E8 83 BF F6 FF                  call 0x1408b4e90
00948F0D  4C 8B 6C 24 60                  mov r13, qword ptr [rsp + 0x60]
00948F12  84 C0                           test al, al
00948F14  0F 85 FD F9 FF FF               jne 0x140948917
00948F1A  48 8B DF                        mov rbx, rdi
00948F1D  E9 01 FA FF FF                  jmp 0x140948923
00948F22  44 8B C0                        mov r8d, eax
00948F25  BA 00 08 04 00                  mov edx, 0x40800
00948F2A  E9 AA F9 FF FF                  jmp 0x1409488d9
00948F2F  33 D2                           xor edx, edx
00948F31  48 8B 8C 24 28 01 00 00         mov rcx, qword ptr [rsp + 0x128]
00948F39  E8 A2 97 EF FF                  call 0x1408426e0
00948F3E  84 C0                           test al, al
00948F40  0F 85 C5 C9 1D 00               jne 0x140b2590b
00948F46  4C 8B 84 24 88 00 00 00         mov r8, qword ptr [rsp + 0x88]
00948F4E  48 8B 94 24 60 01 00 00         mov rdx, qword ptr [rsp + 0x160]
00948F56  49 8B CF                        mov rcx, r15
00948F59  E8 CA 17 00 00                  call 0x14094a728
00948F5E  8B D8                           mov ebx, eax
00948F60  85 C0                           test eax, eax
00948F62  0F 89 79 F9 FF FF               jns 0x1409488e1
00948F68  BB 34 00 00 C0                  mov ebx, 0xc0000034
00948F6D  44 8B C3                        mov r8d, ebx
00948F70  BA 00 07 04 00                  mov edx, 0x40700
00948F75  E9 5F F9 FF FF                  jmp 0x1409488d9
00948F7A  B9 02 00 00 00                  mov ecx, 2
00948F7F  E8 BC 5A 06 00                  call 0x1409aea40
00948F84  E9 A3 FC FF FF                  jmp 0x140948c2c
00948F89  49 8B CE                        mov rcx, r14
00948F8C  E8 CB 69 F0 FF                  call 0x14084f95c
00948F91  41 8A C4                        mov al, r12b
00948F94  88 44 24 41                     mov byte ptr [rsp + 0x41], al
00948F98  88 44 24 43                     mov byte ptr [rsp + 0x43], al
00948F9C  E9 A7 FC FF FF                  jmp 0x140948c48
00948FA1  41 8B CC                        mov ecx, r12d
00948FA4  E8 97 5A 06 00                  call 0x1409aea40
00948FA9  BB 02 00 00 C0                  mov ebx, 0xc0000002
00948FAE  44 8B C3                        mov r8d, ebx
00948FB1  BA 00 09 04 00                  mov edx, 0x40900
00948FB6  E9 1E F9 FF FF                  jmp 0x1409488d9
00948FBB  44 8B C0                        mov r8d, eax
00948FBE  BA 00 0A 04 00                  mov edx, 0x40a00
00948FC3  E9 11 F9 FF FF                  jmp 0x1409488d9
00948FC8  44 8B C0                        mov r8d, eax
00948FCB  BA 00 0B 04 00                  mov edx, 0x40b00
00948FD0  E9 04 F9 FF FF                  jmp 0x1409488d9
00948FD5  8B D0                           mov edx, eax
00948FD7  48 8D 44 24 70                  lea rax, [rsp + 0x70]
00948FDC  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00948FE1  48 8D 84 24 A0 00 00 00         lea rax, [rsp + 0xa0]
00948FE9  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00948FEE  4C 8D 4C 24 50                  lea r9, [rsp + 0x50]
00948FF3  44 8B 84 24 60 01 00 00         mov r8d, dword ptr [rsp + 0x160]
00948FFB  49 8B CE                        mov rcx, r14
00948FFE  E8 91 0C F1 FF                  call 0x140859c94
00949003  8B D8                           mov ebx, eax
00949005  85 C0                           test eax, eax
00949007  0F 89 0B C9 1D 00               jns 0x140b25918
0094900D  44 8B C0                        mov r8d, eax
00949010  BA 00 0C 04 00                  mov edx, 0x40c00
00949015  E9 BF F8 FF FF                  jmp 0x1409488d9
0094901A  BA 00 0E 04 00                  mov edx, 0x40e00
0094901F  E9 A3 F7 FF FF                  jmp 0x1409487c7
00949024  66 83 C9 20                     or cx, 0x20
00949028  66 41 89 4D 02                  mov word ptr [r13 + 2], cx
0094902D  E9 49 FD FF FF                  jmp 0x140948d7b
00949032  89 41 38                        mov dword ptr [rcx + 0x38], eax
00949035  E9 BF FD FF FF                  jmp 0x140948df9
0094903A  49 8B CE                        mov rcx, r14
0094903D  E8 F6 F6 EF FF                  call 0x140848738
00949042  40 88 7C 24 41                  mov byte ptr [rsp + 0x41], dil
00949047  E9 B8 FD FF FF                  jmp 0x140948e04
0094904C  48 8B D3                        mov rdx, rbx
0094904F  48 8B C8                        mov rcx, rax
00949052  E8 3D 60 B4 FF                  call 0x14048f094
00949057  48 8B 94 24 60 01 00 00         mov rdx, qword ptr [rsp + 0x160]
0094905F  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
00949067  E8 C4 22 B4 FF                  call 0x14048b330
0094906C  8B D8                           mov ebx, eax
0094906E  85 C0                           test eax, eax
00949070  0F 89 46 C9 1D 00               jns 0x140b259bc
00949076  44 8B C0                        mov r8d, eax
00949079  BA 00 10 04 00                  mov edx, 0x41000
0094907E  E9 56 F8 FF FF                  jmp 0x1409488d9
00949083  F6 84 24 50 01 00 00 02         test byte ptr [rsp + 0x150], 2
0094908B  0F 84 04 CA 1D 00               je 0x140b25a95
00949091  41 B8 01 00 19 C0               mov r8d, 0xc0190001
00949097  BA 80 15 04 00                  mov edx, 0x41580
0094909C  E9 35 F8 FF FF                  jmp 0x1409488d6
009490A1  F6 84 24 50 01 00 00 02         test byte ptr [rsp + 0x150], 2
009490A9  0F 84 39 CA 1D 00               je 0x140b25ae8
009490AF  41 B8 01 00 19 C0               mov r8d, 0xc0190001
009490B5  BA 80 17 04 00                  mov edx, 0x41780
009490BA  E9 17 F8 FF FF                  jmp 0x1409488d6
009490BF  BA 00 24 04 00                  mov edx, 0x42400
009490C4  E9 FE F6 FF FF                  jmp 0x1409487c7
009490C9  41 89 45 38                     mov dword ptr [r13 + 0x38], eax
009490CD  E9 8A F6 FF FF                  jmp 0x14094875c
009490D2  F6 84 24 50 01 00 00 02         test byte ptr [rsp + 0x150], 2
009490DA  0F 84 54 CA 1D 00               je 0x140b25b34
009490E0  41 B8 01 00 19 C0               mov r8d, 0xc0190001
009490E6  BA 80 1B 04 00                  mov edx, 0x41b80
009490EB  E9 E6 F7 FF FF                  jmp 0x1409488d6
009490F0  F6 84 24 50 01 00 00 02         test byte ptr [rsp + 0x150], 2
009490F8  0F 84 7F CA 1D 00               je 0x140b25b7d
009490FE  41 B8 01 00 19 C0               mov r8d, 0xc0190001
00949104  BA 80 19 04 00                  mov edx, 0x41980
00949109  E9 C8 F7 FF FF                  jmp 0x1409488d6
0094910E  49 8B CE                        mov rcx, r14
00949111  E8 B2 08 28 00                  call 0x140bc99c8
00949116  E9 C3 F6 FF FF                  jmp 0x1409487de
0094911B  49 8B CF                        mov rcx, r15
0094911E  E8 59 B8 F2 FF                  call 0x14087497c
00949123  BA 43 4D 55 77                  mov edx, 0x77554d43
00949128  49 8B CF                        mov rcx, r15
0094912B  E8 40 97 23 00                  call 0x140b82870
00949130  E9 C2 F6 FF FF                  jmp 0x1409487f7
00949135  49 8B CF                        mov rcx, r15
00949138  E8 3F B8 F2 FF                  call 0x14087497c
0094913D  BA 43 4D 55 77                  mov edx, 0x77554d43
00949142  49 8B CF                        mov rcx, r15
00949145  E8 26 97 23 00                  call 0x140b82870
0094914A  E9 B9 F6 FF FF                  jmp 0x140948808
0094914F  33 D2                           xor edx, edx
00949151  E8 1A 97 23 00                  call 0x140b82870
00949156  48 8B 94 24 30 01 00 00         mov rdx, qword ptr [rsp + 0x130]
0094915E  E9 6B F8 FF FF                  jmp 0x1409489ce
00949163  48 8D 54 24 70                  lea rdx, [rsp + 0x70]
00949168  49 8B CE                        mov rcx, r14
0094916B  45 84 A6 8C 00 00 00            test byte ptr [r14 + 0x8c], r12b
00949172  0F 84 AF CA 1D 00               je 0x140b25c27
00949178  E8 A3 3A F1 FF                  call 0x14085cc20
0094917D  E9 D2 F6 FF FF                  jmp 0x140948854
00949182  49 8B CE                        mov rcx, r14
00949185  E8 A2 15 F1 FF                  call 0x14085a72c
0094918A  E9 D4 F6 FF FF                  jmp 0x140948863
0094918F  49 8B CE                        mov rcx, r14
00949192  40 38 7C 24 45                  cmp byte ptr [rsp + 0x45], dil
00949197  0F 84 95 CA 1D 00               je 0x140b25c32
0094919D  45 33 C0                        xor r8d, r8d
009491A0  E8 CB 1B F0 FF                  call 0x14084ad70
009491A5  E9 E7 F6 FF FF                  jmp 0x140948891
009491AA  49 8B CE                        mov rcx, r14
009491AD  E8 86 F5 EF FF                  call 0x140848738
009491B2  E9 E5 F6 FF FF                  jmp 0x14094889c
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpCreateChild(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, unsigned __int16 a6, unsigned __int8 a7, unsigned __int8 a8, unsigned int a9)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned int v_stack_mAC;
    unsigned int v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned int v_stack_mC8;
    unsigned int v_stack_mCC;
    unsigned __int16 v_stack_mCE;
    unsigned __int8 v_stack_mD3;
    unsigned __int8 v_stack_mD4;
    unsigned __int8 v_stack_mD5;
    unsigned __int8 v_stack_mD6;
    unsigned __int8 v_stack_mD7;
    unsigned __int8 v_stack_mD8;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned int v_stack_p10;
    unsigned __int64 v_stack_p120;
    unsigned __int64 v_stack_p128;
    unsigned __int64 v_stack_p130;
    unsigned __int64 v_stack_p138;
    unsigned __int64 v_stack_p140;
    unsigned int v_stack_p160;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned int v_stack_p30;
    unsigned __int8 v_stack_p38;
    unsigned __int8 v_stack_p40;
    unsigned __int8 v_stack_p41;
    unsigned __int8 v_stack_p42;
    unsigned __int8 v_stack_p43;
    unsigned __int8 v_stack_p44;
    unsigned __int8 v_stack_p45;
    unsigned __int16 v_stack_p4A;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned int v_stack_p68;
    unsigned __int64 v_stack_p6C;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;
    unsigned __int64 v_stack_p8;
    unsigned __int64 v_stack_p80;
    unsigned __int64 v_stack_p88;
    unsigned __int64 v_stack_p90;
    unsigned __int64 v_stack_p98;
    unsigned __int64 v_stack_pA0;
    unsigned __int64 v_stack_pA8;
    unsigned __int64 v_stack_pB8;
    unsigned __int64 v_stack_pC0;
    unsigned __int64 v_stack_pC8;
    unsigned __int64 v_stack_pD0;
    unsigned __int64 v_stack_pD8;

    *(unsigned __int64 *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (224);
    v_rdi = 0;
    *(unsigned __int64 *)(v_rsp - 112) = 0;
    v_stack_mA8 = 0;
    *(unsigned __int64 *)(v_rsp - 128) = 0;
    v_stack_mD3 = 0;
    v_stack_mD7 = 0;
    v_stack_mD5 = 0;
    v_stack_mD4 = 0;
    v_stack_mB8 = 0;
    a2 = (unsigned int)((a2) | (0xFFFFFFFFULL));
    v_stack_mCC = (unsigned int)(a2);
    result = HvpGetCellContextInitialize(v_rsp - 112, a2, a2, a1);
    v_stack_m78 = 0;
    v_stack_mC8 = (unsigned int)(a2);
    result = HvpGetCellContextInitialize(v_stack_mA8, a2, a2, a1);
    v_stack_m88 = 0;
    result = HvpGetCellContextInitialize(v_stack_m80, a2, a2, a1);
    v_stack_mD8 = 0;
    v_stack_m90 = 0;
    v_stack_mAC = (unsigned int)(a2);
    v_stack_m98 = 0;
    v_stack_m60 = 0;
    v_stack_mA0 = 0;
    v_stack_m58 = 0;
    v_stack_mD6 = 0;
    result = CmpGetKcbAtLayerHeight(a1, *(unsigned __int16 *)(a1 + 2), a2, a1);
    v_stack_mC0 = result;
    result = CmpGetKcbAtLayerHeight(a2, *(unsigned __int16 *)(a2 + 2), a2, a1);
    v_stack_m50 = result;
    v_stack_m48 = *(unsigned __int64 *)(result + 32);
    if (a9 != 0) goto loc_00948BBD;
loc_00948292:
    if (((a7) & (0xFFFFFFFCULL)) != 0) goto loc_00948E64;
    if (((v_stack_p38) & (1)) != 0) goto loc_009489DC;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 32) + 4112)))) & (32)) != 0) goto loc_009489DC;
loc_009482C9:
    if (sign_flag) goto loc_00948E84;
    if (((*(unsigned int *)(*(unsigned __int64 *)(result + 32) + 160)) & (0x100000ULL)) != 0) goto loc_00948E94;
    if ((*(unsigned __int8 *)(result + 65)) == 1) goto loc_00948EA4;
    if ((*(unsigned __int8 *)(v_rip + 5007783)) == 0) goto loc_009488B2;
    if (((*(unsigned int *)(result + 184)) & (0x1000000ULL)) == 0) goto loc_009488B2;
loc_00948312:
    a1 = (unsigned __int16)((a6) | (256));
    if (1 == 0) { a1 = a6; }
    a2 = (unsigned __int16)(((unsigned __int16)(a1)) | (512));
    if (((*(unsigned int *)(result + 184)) & (0x2000000ULL)) == 0) { a2 = (unsigned __int16)(a1); }
    v_stack_mCE = (unsigned __int16)(a2);
    if (0 != 0) goto loc_009488B9;
loc_00948356:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a5 + 24))) & (1));
    v_stack_mB0 = (unsigned int)(a1);
    if (a9 != 0) goto loc_00948EB4;
loc_00948369:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 40))) >> (31));
    if (((unsigned int)(result)) == 1) goto loc_00948A48;
loc_00948378:
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(a5 + 160))))) == 0) goto loc_00948ECE;
loc_00948387:
    if (((v_stack_mCE) & (2)) == 0) goto loc_009488FD;
loc_00948392:
    if (a9 != 0) goto loc_00948F2F;
    a1 = (unsigned int)(v_stack_mB0);
    if (a9 != 0) { a1 = 1; }
    v_stack_p10 = (unsigned int)(a1);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result + 40)))) != -1) goto loc_00948C21;
    result = (unsigned int)(*(unsigned int *)(result + 40));
    if (a8 == 0) {
        a1 = *(unsigned __int64 *)(result + 32);
        result = HvLockHiveFlusherShared(a1, a2, 512, a9);
        v_stack_mD7 = 1;
        v_stack_mD5 = 1;
    }
    if (a9 != 0) goto loc_00948B8F;
    if ((*(unsigned __int64 *)(result + 240)) != 0) goto loc_00949083;
    if ((*(unsigned int *)(result + 248)) < 0) goto loc_009490A1;
    if ((*(unsigned int *)(result + 248)) != 0) goto loc_009490F0;
    if ((*(unsigned int *)(result + 264)) != 0) goto loc_009490D2;
    result = CmpNameSize(v_stack_p20, a2, 512, a9);
    result = (unsigned int)(((unsigned __int16)(result)) + (76));
    v_stack_mAC = (unsigned int)(result);
    v_stack_mF0 = v_stack_m70;
    v_stack_mF8 = v_stack_mB8;
    result = HvAllocateCell(*(unsigned __int64 *)(result + 32), (unsigned int)((unsigned int)(result)), (unsigned int)((unsigned int)((unsigned int)(v_stack_p10))), v_stack_mCC);
    if (sign_flag) goto loc_00948BE9;
    if ((unsigned __int16)(*(unsigned __int16 *)(a5 + 4)) != 0) goto loc_00948A62;
loc_00948485:
    a2 = 0;
    result = memset(v_stack_mB8, a2, (unsigned int)(v_stack_mAC), v_stack_mCC);
    if ((((unsigned __int8)(v_stack_mCE)) & (2)) != 0) goto loc_00948A2A;
    *(unsigned __int16 *)(v_stack_mB8) = 0x6B6EULL;
loc_009484AC:
    *(unsigned __int8 *)(v_stack_mB8 + 12) = (unsigned __int8)(*(unsigned __int8 *)(v_rip + 5007330));
    if ((*(unsigned __int8 *)(v_stack_mC0 + 65)) == 3) goto loc_009489FD;
loc_009484C8:
    *(unsigned __int16 *)(v_stack_mB8 + 2) = (unsigned __int16)(v_stack_mCE);
    *(unsigned __int64 *)(v_stack_mB8 + 4) = *(unsigned __int64 *)(*(unsigned __int8 *)(v_rip + 5007330));
    *(unsigned int *)(v_stack_mB8 + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mC0 + 40)));
    a2 = (unsigned int)((v_stack_mCE) | (0xFFFFFFFFULL));
    *(unsigned int *)(v_stack_mB8 + 28) = (unsigned int)(a2);
    *(unsigned int *)(v_stack_mB8 + 32) = (unsigned int)(a2);
    *(unsigned int *)(v_stack_mB8 + 40) = (unsigned int)(a2);
    *(unsigned int *)(v_stack_mB8 + 44) = (unsigned int)(a2);
    *(unsigned int *)(v_stack_mB8 + 48) = (unsigned int)((unsigned int)(v_stack_mC8));
    *(unsigned __int16 *)(v_stack_mB8 + 74) = (unsigned __int16)(*(unsigned __int16 *)(a5 + 4));
    v_stack_mC8 = (unsigned int)(a2);
    result = *(unsigned __int16 *)(a5 + 4);
    if (sign_flag) {
        result = *(unsigned int *)(v_stack_mB8 + 52);
        a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_mC0 + 184))) << (16));
        a2 = (unsigned int)((a2) ^ ((unsigned int)(result)));
        a2 = (unsigned int)((a2) & (0xF00000ULL));
        a2 = (unsigned int)((a2) ^ ((unsigned int)(result)));
        *(unsigned int *)(v_stack_mB8 + 52) = (unsigned int)(a2);
    }
    result = CmpCopyName(v_stack_mB8 + 76, v_stack_p20, (unsigned int)(v_stack_mAC), v_stack_mCC);
    *(unsigned __int16 *)(v_stack_mB8 + 72) = (unsigned __int16)(result);
    if (((unsigned __int16)(result)) < (*(unsigned __int16 *)(v_stack_p20))) {
    }
    if ((((unsigned __int8)(v_stack_mCE)) & (2)) != 0) goto loc_009488E9;
loc_00948562:
    v_stack_mD3 = 1;
    if ((((unsigned __int8)(v_stack_mCE)) & (2)) != 0) goto loc_009485C1;
    result = CmLockHiveSecurityExclusive(*(unsigned __int64 *)(result + 32), v_stack_p20, (unsigned int)(v_stack_mAC), v_stack_mCC);
    v_stack_mD8 = 1;
    a4 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_mCC)))) >> (31));
    v_stack_mE8 = v_stack_mB8 + 44;
    v_stack_mF0 = 0;
    v_stack_mF8 = v_stack_m90;
    result = CmpGetSecurityDescriptorNodeEx(*(unsigned __int64 *)(result + 32), (unsigned int)(v_stack_mCC), v_stack_mB8, a4);
    if (sign_flag) goto loc_009489E9;
    result = CmUnlockHiveSecurity(*(unsigned __int64 *)(result + 32), (unsigned int)(v_stack_mCC), v_stack_mB8, a4);
    v_stack_mD8 = 0;
loc_009485C1:
    a4 = 0;
    a3 = 0;
    result = HvpMarkCellDirty(*(unsigned __int64 *)(result + 32), (unsigned int)(*(unsigned int *)(v_stack_mC0 + 40)), a3, a4);
    if (sign_flag) goto loc_009487C2;
    if (a9 != 0) goto loc_0094860D;
    a4 = 0;
    result = CmpAddSubKeyEx(*(unsigned __int64 *)(result + 32), (unsigned int)(*(unsigned int *)(v_stack_mC0 + 40)), (unsigned int)(v_stack_mCC), a4);
    if (sign_flag) goto loc_00948BDF;
loc_0094860D:
    v_stack_mD6 = 1;
    *(unsigned int *)(result + 40) = (unsigned int)((unsigned int)(v_stack_mCC));
    *(unsigned __int64 *)(result + 240) = a9;
    result = a9;
    if ((((unsigned __int8)(v_stack_mCE)) & (64)) == 0) {
        result = *(unsigned int *)(v_stack_mB8 + 36);
        *(unsigned int *)(result + 96) = (unsigned int)(result);
        result = *(unsigned int *)(v_stack_mB8 + 40);
        *(unsigned int *)(result + 100) = (unsigned int)(result);
    }
    a4 = 0;
    a3 = 0;
    result = CmpRebuildKcbCacheFromNode(result, v_stack_mB8, a3, a4);
    if ((((unsigned __int8)(v_stack_mCE)) & (2)) != 0) goto loc_009486D3;
    v_stack_p10 = 0;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mB8 + 44)))) == -1) goto loc_00948E2A;
    v_stack_m68 = *(unsigned __int64 *)(result + 32);
    result = CmLockHiveSecurityShared(*(unsigned __int64 *)(result + 32), v_stack_mB8, a3, a4);
    result = CmpFindSecurityCellCacheIndex(v_stack_m68, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mB8 + 44)))), v_stack_p10, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00948E33;
    a2 = ((unsigned int)(v_stack_p10)) + ((unsigned int)(v_stack_p10));
    *(unsigned __int64 *)(result + 88) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m68 + 1888) + a2 * 8 + 8);
    result = CmUnlockHiveSecurity(v_stack_m68, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m68 + 1888) + a2 * 8 + 8), v_stack_p10, a4);
loc_009486D3:
    if (a9 != 0) goto loc_00948B48;
loc_009486E1:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_mC0 + 32) + 140)) & (1)) == 0) goto loc_009489F3;
    result = HvpGetCellFlat(*(unsigned __int64 *)(v_stack_mC0 + 32), (unsigned int)(*(unsigned int *)(v_stack_mC0 + 40)), v_stack_m80, a4);
loc_00948707:
    v_stack_m88 = result;
    result = CmpUpdateKeyNodeAccessBits(*(unsigned __int64 *)(v_stack_mC0 + 32), result, (unsigned int)(*(unsigned int *)(v_stack_mC0 + 40)), a4);
    *(unsigned __int64 *)(result + 4) = *(unsigned __int64 *)(result);
    if (((unsigned int)((unsigned __int16)((unsigned int)(*(unsigned int *)(result + 52))))) < ((unsigned int)(*(unsigned __int16 *)(v_stack_p20)))) {
        *(unsigned __int16 *)(result + 52) = (unsigned __int16)(*(unsigned __int16 *)(v_stack_p20));
    }
    if ((*(unsigned int *)(result + 56)) < ((unsigned int)(*(unsigned __int16 *)(a5 + 4)))) goto loc_009490C9;
loc_0094875C:
    *(unsigned __int16 *)(v_stack_mC0 + 176) = (unsigned __int16)(*(unsigned __int16 *)(result + 52));
    *(unsigned __int64 *)(v_stack_mC0 + 168) = *(unsigned __int64 *)(result + 4);
    result = CmpCleanUpSubKeyInfo(v_stack_mC0, 1, (unsigned int)(*(unsigned int *)(v_stack_mC0 + 40)), a4);
    if (v_stack_mD7 != 0) {
        a1 = *(unsigned __int64 *)(result + 32);
        result = HvUnlockHiveFlusherShared(a1, 1, (unsigned int)(*(unsigned int *)(v_stack_mC0 + 40)), a4);
        v_stack_mD7 = 0;
    }
    a4 = 0;
    result = CmpReportNotifyForKcbStack(v_stack_p8, a9, 1, a4);
    v_stack_mD6 = 0;
    goto loc_009487D2;
loc_009487C2:
loc_009487C7:
    result = CmpRecordParseFailure(a5, (unsigned int)(0x42200ULL), (unsigned int)((unsigned int)(result)), a4);
loc_009487D2:
loc_009487D6:
    if ((unsigned __int8)(v_stack_mD8) != 0) goto loc_0094910E;
loc_009487DE:
    if (v_stack_mA0 != 0) goto loc_0094911B;
loc_009487F7:
    if (v_stack_m98 != 0) goto loc_00949135;
loc_00948808:
    if (v_stack_m90 != 0) goto loc_0094898F;
loc_00948819:
    if (v_stack_m88 == 0) goto loc_00948846;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_mC0 + 32) + 140)) & (1)) != 0) goto loc_00948A34;
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(v_stack_mC0 + 32), v_stack_m80, (unsigned int)((unsigned int)(result)), a4);
loc_00948846:
    if (v_stack_m78 != 0) goto loc_00949163;
loc_00948854:
    v_rsi = (unsigned int)((a5) | (0xFFFFFFFFULL));
    if (((unsigned int)((unsigned int)(v_stack_mC8))) != ((unsigned int)(v_rsi))) goto loc_00949182;
loc_00948863:
    if (v_stack_mB8 == 0) goto loc_00948885;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(result + 32) + 140)) & (1)) != 0) goto loc_00948A3E;
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(result + 32), v_stack_m70, (unsigned int)((unsigned int)(result)), a4);
loc_00948885:
    if (((unsigned int)((unsigned int)(v_stack_mCC))) != ((unsigned int)(v_rsi))) goto loc_0094918F;
loc_00948891:
    if (v_stack_mD7 != 0) goto loc_009491AA;
loc_0094889C:
    v_rsp = (v_rsp) + (224);
    return 0;
loc_009488B2:
    goto loc_00948312;
loc_009488B9:
    if ((*(unsigned __int64 *)(v_stack_p130 + 64)) == 0) goto loc_00948356;
loc_009488D6:
loc_009488D9:
    result = CmpRecordParseFailure(v_rsi, (unsigned int)(0x40500ULL), (unsigned int)(0xC0000022ULL), a4);
loc_009488E1:
    goto loc_009487D6;
loc_009488E9:
    *(unsigned __int64 *)(v_stack_mB8 + 36) = *(unsigned __int64 *)(v_rsi + 48);
    *(unsigned int *)(v_stack_mB8 + 28) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsi + 40)));
    goto loc_00948562;
loc_009488FD:
    if (0 != 0) goto loc_00948A06;
    if (((*(unsigned int *)(v_stack_m90 + 184)) & (0x2000000ULL)) != 0) goto loc_00948EF3;
loc_00948917:
loc_00948923:
    a3 = 0;
    result = CmpGetSecurityCacheEntryForKcbStack(v_stack_p120, a9, a3, a4);
    v_r10 = (v_stack_p130) + (32);
    v_stack_p30 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 6807934) + 100)));
    v_stack_p28 = *(unsigned __int64 *)(v_rip + 6807934) + 76;
    v_stack_p20 = v_r10;
    result = SeAssignSecurity(result + 32, *(unsigned __int64 *)(v_stack_p130 + 64), v_stack_p88, 1);
    if (sign_flag) goto loc_00948F22;
    goto loc_00948392;
loc_0094898F:
    if (v_stack_p44 != 0) goto loc_00948819;
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsi))))) == 0) goto loc_009489AC;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsi + 24)))) & (4)) != 0) goto loc_00948C03;
loc_009489AC:
    if (((*(unsigned int *)(v_stack_p130 + 12)) & (0x4000000ULL)) != 0) goto loc_009489CE;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p130 + 72) + 48) != 0) goto loc_0094914F;
loc_009489CE:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p130 + 72) + 48) = v_stack_m90;
    goto loc_00948819;
loc_009489DC:
    v_stack_p44 = 1;
    goto loc_009482C9;
loc_009489E9:
    goto loc_009487C7;
loc_009489F3:
    result = HvpGetCellPaged(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p130 + 72) + 48), (unsigned int)(0x42100ULL), v_stack_p88, 1);
    goto loc_00948707;
loc_009489FD:
    goto loc_009484C8;
loc_00948A06:
    a3 = 0;
    result = CmpGetSecurityCacheEntryForKcbStack(v_stack_p120, 1, a3, 1);
    result = (result) + (32);
    v_stack_p88 = result;
    goto loc_00948392;
loc_00948A2A:
    *(unsigned __int16 *)(v_stack_p58) = 0x6B6CULL;
    goto loc_009484AC;
loc_00948A34:
    result = HvpReleaseCellFlat(v_stack_p120, 1, a3, 1);
    goto loc_00948846;
loc_00948A3E:
    result = HvpReleaseCellFlat(v_stack_p120, 1, a3, 1);
    goto loc_00948885;
loc_00948A48:
    if ((unsigned int)(v_stack_p120) != 0) goto loc_00948378;
    goto loc_009488D9;
loc_00948A62:
    v_stack_p28 = v_stack_p70;
    v_stack_p20 = v_stack_pA0;
    result = HvAllocateCell(*(unsigned __int64 *)(result + 32), (unsigned int)((unsigned int)(result)), (unsigned int)((unsigned int)(v_stack_mB8)), v_stack_p50);
    if (sign_flag) goto loc_00948C1A;
    result = memcpy(v_stack_pA0, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p130 + 72) + 8), *(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p130 + 72) + 4), v_stack_p50);
    goto loc_00948B21;
loc_00948B21:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(result + 32) + 140)) & (1)) != 0) goto loc_00948E20;
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(result + 32), v_stack_p70, *(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p130 + 72) + 4), v_stack_p50);
loc_00948B3B:
    v_stack_pA0 = 0;
    goto loc_00948485;
loc_00948B48:
    *(unsigned int *)(v_stack_p78 + 68) = 0;
    *(unsigned int *)(v_stack_p78 + 72) = (unsigned int)((unsigned int)(v_stack_p68));
    *(unsigned __int64 *)(v_stack_p78 + 80) = v_stack_p80;
    *(unsigned int *)(v_stack_p80 + 68) = 1;
    *(unsigned __int64 *)(v_stack_p80 + 88) = v_stack_m90;
    result = CmAddLogForAction(v_stack_p78, 1, *(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p130 + 72) + 4), v_stack_p50);
    if (sign_flag) goto loc_009490BF;
    v_stack_p78 = 0;
    v_stack_p80 = 0;
    goto loc_009486E1;
loc_00948B8F:
    result = CmpAllocateUnitOfWork(v_stack_p78, 1, *(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p130 + 72) + 4), v_stack_p50);
    v_stack_p80 = result;
    v_stack_pB8 = result;
    if (result != 0) goto loc_0094904C;
    goto loc_009488D6;
loc_00948BBD:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 32) + 160)))) & (2)) == 0) goto loc_00948292;
    goto loc_00948E71;
loc_00948BDF:
    goto loc_009487C7;
loc_00948BE9:
loc_00948BEE:
    result = CmpRecordParseFailure(*(unsigned __int64 *)(v_stack_p130 + 72), (unsigned int)(0x41E00ULL), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 32) + 160)))), v_stack_p50);
loc_00948BF9:
    goto loc_009488E1;
loc_00948C03:
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m90, a2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 32) + 160)))), v_stack_p50);
    v_stack_p88 = 0;
    goto loc_00948819;
loc_00948C1A:
    goto loc_00948BEE;
loc_00948C21:
    result = (unsigned int)((result) >> (31));
    if (((unsigned int)(v_stack_m90)) != ((unsigned int)(result))) goto loc_00948F7A;
loc_00948C2C:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m90 + 40))) >> (31));
    v_stack_p160 = (unsigned int)(result);
    if (a8 == 0) goto loc_00948F89;
loc_00948C48:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(result + 32) + 140)) & (1)) == 0) goto loc_00948E50;
    result = HvpGetCellFlat(*(unsigned __int64 *)(result + 32), (unsigned int)(*(unsigned int *)(v_stack_m90 + 40)), v_stack_pA8, v_stack_p50);
loc_00948C69:
    v_stack_p60 = result;
    result = CmpNameSize(v_stack_p138, (unsigned int)(*(unsigned int *)(v_stack_m90 + 40)), v_stack_pA8, v_stack_p50);
    if (((unsigned __int16)(result)) != (*(unsigned __int16 *)(result + 72))) goto loc_00948FA1;
    a3 = 0;
    result = CmpMarkKeyDirty(*(unsigned __int64 *)(result + 32), (unsigned int)(*(unsigned int *)(v_stack_m90 + 40)), a3, v_stack_p50);
    if (sign_flag) goto loc_00948FBB;
    a4 = 0;
    a3 = 0;
    result = HvpMarkCellDirty(*(unsigned __int64 *)(result + 32), (unsigned int)(*(unsigned int *)(v_stack_p58 + 40)), a3, a4);
    if (sign_flag) goto loc_00948FC8;
    if ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p130 + 72) + 4)) != 0) goto loc_00948FD5;
    result = CmLockHiveSecurityExclusive(*(unsigned __int64 *)(result + 32), (unsigned int)(*(unsigned int *)(v_stack_p58 + 40)), a3, a4);
    v_stack_p40 = 1;
    a4 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m90 + 40))))) >> (31));
    v_stack_p30 = v_stack_p6C;
    v_stack_p28 = 1;
    v_stack_p20 = v_stack_p88;
    result = CmpGetSecurityDescriptorNodeEx(*(unsigned __int64 *)(result + 32), (unsigned int)(*(unsigned int *)(v_stack_m90 + 40)), result, a4);
    if (sign_flag) goto loc_0094901A;
    result = CmpFreeSecurityDescriptor(*(unsigned __int64 *)(result + 32), (unsigned int)(*(unsigned int *)(v_stack_m90 + 40)), result, a4);
    *(unsigned int *)(result + 44) = (unsigned int)((unsigned int)(v_stack_p6C));
    result = CmUnlockHiveSecurity(*(unsigned __int64 *)(result + 32), (unsigned int)(*(unsigned int *)(v_stack_m90 + 40)), result, a4);
    *(unsigned int *)(result + 48) = (unsigned int)((unsigned int)(v_stack_p50));
    *(unsigned __int16 *)(result + 74) = (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p130 + 72) + 4));
    result = CmpCopyName(result + 76, v_stack_p138, result, a4);
    *(unsigned __int16 *)(result + 2) = (unsigned __int16)(v_stack_p4A);
    if ((*(unsigned __int16 *)(result + 72)) < ((unsigned __int16)(*(unsigned __int16 *)(v_stack_p138)))) goto loc_00949024;
loc_00948D7B:
    *(unsigned __int64 *)(result + 4) = *(unsigned __int64 *)(*(unsigned __int16 *)(v_stack_p138));
    a4 = 0;
    a3 = 0;
    result = CmpRebuildKcbCacheFromNode(v_stack_m90, result, a3, a4);
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(result + 32) + 140)) & (1)) == 0) goto loc_00948E5A;
    result = HvpGetCellFlat(*(unsigned __int64 *)(result + 32), (unsigned int)(*(unsigned int *)(v_stack_p58 + 40)), v_stack_p98, a4);
loc_00948DC9:
    v_stack_p90 = result;
    *(unsigned __int64 *)(result + 4) = *(unsigned __int64 *)(*(unsigned __int16 *)(v_stack_p138));
    *(unsigned __int64 *)(v_stack_p58 + 168) = *(unsigned __int64 *)(*(unsigned __int16 *)(v_stack_p138));
    if ((*(unsigned int *)(result + 56)) < ((unsigned int)(*(unsigned __int16 *)(result + 74)))) goto loc_00949032;
loc_00948DF9:
    if (v_stack_p41 != 0) goto loc_0094903A;
loc_00948E04:
    a4 = 0;
    a2 = 0;
    result = CmpReportNotifyForKcbStack(v_stack_p120, a2, 1, a4);
    goto loc_00948BF9;
loc_00948E20:
    result = HvpReleaseCellFlat(v_stack_p120, a2, 1, a4);
    goto loc_00948B3B;
loc_00948E2A:
    *(unsigned __int64 *)(v_stack_m90 + 88) = 0;
    goto loc_009486D3;
loc_00948E33:
    *(unsigned __int64 *)(v_stack_m90 + 88) = 0;
    v_stack_p20 = 0;
    result = KeBugCheckEx(4 + 77, 4, 1, v_stack_m90);
loc_00948E50:
    result = HvpGetCellPaged(4 + 77, 4, 1, v_stack_m90);
    goto loc_00948C69;
loc_00948E5A:
    result = HvpGetCellPaged(4 + 77, 4, 1, v_stack_m90);
    goto loc_00948DC9;
loc_00948E64:
loc_00948E71:
    result = CmpRecordParseFailure(*(unsigned __int64 *)(v_stack_p130 + 72), (unsigned int)(0x40180ULL), (unsigned int)((unsigned int)((unsigned int)(0xC000000DULL))), v_stack_m90);
    goto loc_009488E1;
loc_00948E84:
    goto loc_009488D6;
loc_00948E94:
    goto loc_009488D6;
loc_00948EA4:
    goto loc_009488D6;
loc_00948EB4:
    if ((*(unsigned __int64 *)((unsigned int)(0xC000000DULL) + 240)) == 0) goto loc_00948369;
    v_stack_pD8 = 0;
loc_00948ECE:
    result = CmpAttachToRegistryProcess(*(unsigned __int64 *)(v_stack_p130 + 72) + 168, (unsigned int)(0x40400ULL), (unsigned int)(0xC0000022ULL), v_stack_m90);
    goto loc_00948387;
loc_00948EF3:
    a2 = 0;
    result = CmpIsSystemEntity(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562), a2, *(unsigned __int64 *)(v_stack_p130 + 72) + 16, a9);
    if ((unsigned __int8)(result) != 0) goto loc_00948917;
    goto loc_00948923;
loc_00948F22:
    goto loc_009488D9;
loc_00948F2F:
    a2 = 0;
    result = CmpIsKeyStackDeleted(v_stack_p128, a2, (unsigned int)((unsigned int)(result)), a9);
    result = CmpUndoDeleteKeyForTrans(v_stack_m90, a9, v_stack_p88, a9);
    if (!sign_flag) goto loc_009488E1;
    goto loc_009488D9;
loc_00948F7A:
    result = CmpLogUnsupportedOperation(2, (unsigned int)(0x40700ULL), (unsigned int)((unsigned int)((unsigned int)(0xC0000034ULL))), a9);
    goto loc_00948C2C;
loc_00948F89:
    result = HvLockHiveFlusherShared(*(unsigned __int64 *)(result + 32), (unsigned int)(0x40700ULL), (unsigned int)((unsigned int)((unsigned int)(0xC0000034ULL))), a9);
    v_stack_p41 = 1;
    v_stack_p43 = 1;
    goto loc_00948C48;
loc_00948FA1:
    result = CmpLogUnsupportedOperation(1, (unsigned int)(0x40700ULL), (unsigned int)((unsigned int)((unsigned int)(0xC0000034ULL))), a9);
    goto loc_009488D9;
loc_00948FBB:
    goto loc_009488D9;
loc_00948FC8:
    goto loc_009488D9;
loc_00948FD5:
    v_stack_p28 = v_stack_p70;
    v_stack_p20 = v_stack_pA0;
    result = HvAllocateCell(*(unsigned __int64 *)(result + 32), (unsigned int)((unsigned int)(result)), (unsigned int)(a9), v_stack_p50);
    goto loc_009488D9;
loc_0094901A:
    goto loc_009487C7;
loc_00949024:
    a1 = (unsigned __int16)((*(unsigned __int64 *)(result + 32)) | (32));
    *(unsigned __int16 *)(v_stack_p60 + 2) = (unsigned __int16)(a1);
    goto loc_00948D7B;
loc_00949032:
    *(unsigned int *)(a1 + 56) = (unsigned int)(result);
    goto loc_00948DF9;
loc_0094903A:
    result = HvUnlockHiveFlusherShared(*(unsigned __int64 *)(result + 32), (unsigned int)(0x40E00ULL), (unsigned int)((unsigned int)(result)), v_stack_p50);
    v_stack_p41 = 0;
    goto loc_00948E04;
loc_0094904C:
    result = CmpTransEnlistUowInKcb(result, (unsigned int)((unsigned int)(result)), (unsigned int)((unsigned int)(result)), v_stack_p50);
    result = CmpTransEnlistUowInCmTrans(v_stack_p80, a9, (unsigned int)((unsigned int)(result)), v_stack_p50);
    goto loc_009488D9;
loc_00949083:
    goto loc_009488D6;
loc_009490A1:
    goto loc_009488D6;
loc_009490BF:
    goto loc_009487C7;
loc_009490C9:
    *(unsigned int *)(v_stack_p60 + 56) = (unsigned int)(result);
    goto loc_0094875C;
loc_009490D2:
    goto loc_009488D6;
loc_009490F0:
    goto loc_009488D6;
loc_0094910E:
    result = CmUnlockHiveSecurity(*(unsigned __int64 *)(result + 32), (unsigned int)(0x41980ULL), (unsigned int)(0xC0190001ULL), v_stack_p50);
    goto loc_009487DE;
loc_0094911B:
    result = CmpRundownUnitOfWork(v_stack_m90, (unsigned int)(0x41980ULL), (unsigned int)(0xC0190001ULL), v_stack_p50);
    result = ExFreePoolWithTag(v_stack_m90, (unsigned int)(0x77554D43ULL), (unsigned int)(0xC0190001ULL), v_stack_p50);
    goto loc_009487F7;
loc_00949135:
    result = CmpRundownUnitOfWork(v_stack_m90, (unsigned int)(0x77554D43ULL), (unsigned int)(0xC0190001ULL), v_stack_p50);
    result = ExFreePoolWithTag(v_stack_m90, (unsigned int)(0x77554D43ULL), (unsigned int)(0xC0190001ULL), v_stack_p50);
    goto loc_00948808;
loc_0094914F:
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m90, a2, (unsigned int)(0xC0190001ULL), v_stack_p50);
    goto loc_009489CE;
loc_00949163:
    result = HvpReleaseCellFlat(*(unsigned __int64 *)(result + 32), v_stack_p70, (unsigned int)(0xC0190001ULL), v_stack_p50);
    goto loc_00948854;
loc_00949182:
    result = HvFreeCell(*(unsigned __int64 *)(result + 32), v_stack_p70, (unsigned int)(0xC0190001ULL), v_stack_p50);
    goto loc_00948863;
loc_0094918F:
    a3 = 0;
    result = CmpFreeKeyByCell(*(unsigned __int64 *)(result + 32), v_stack_p70, a3, v_stack_p50);
    goto loc_00948891;
loc_009491AA:
    result = HvUnlockHiveFlusherShared(*(unsigned __int64 *)(result + 32), v_stack_p70, a3, v_stack_p50);
    goto loc_0094889C;
}
```

## 5. (Beta) C Style

```c
int64_t CmpCreateChild(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, void *Arg5, uint16_t Arg6, uint8_t Arg7, uint8_t Arg8, uint32_t Arg9)
{
    uint8_t *arg5 = (uint8_t *)Arg5;

    int64_t result;
    int64_t local_r10;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint32_t v_stack_mAC;
    uint32_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint32_t v_stack_mC8;
    uint32_t v_stack_mCC;
    uint16_t v_stack_mCE;
    uint8_t v_stack_mD3;
    uint8_t v_stack_mD4;
    uint8_t v_stack_mD5;
    uint8_t v_stack_mD6;
    uint8_t v_stack_mD7;
    uint8_t v_stack_mD8;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint32_t v_stack_p10;
    uint64_t v_stack_p120;
    uint64_t v_stack_p128;
    uint64_t v_stack_p130;
    uint64_t v_stack_p138;
    uint64_t v_stack_p140;
    uint32_t v_stack_p160;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint32_t v_stack_p30;
    uint8_t v_stack_p38;
    uint8_t v_stack_p40;
    uint8_t v_stack_p41;
    uint8_t v_stack_p42;
    uint8_t v_stack_p43;
    uint8_t v_stack_p44;
    uint8_t v_stack_p45;
    uint16_t v_stack_p4A;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint32_t v_stack_p68;
    uint64_t v_stack_p6C;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;
    uint64_t v_stack_p8;
    uint64_t v_stack_p80;
    uint64_t v_stack_p88;
    uint64_t v_stack_p90;
    uint64_t v_stack_p98;
    uint64_t v_stack_pA0;
    uint64_t v_stack_pA8;
    uint64_t v_stack_pB8;
    uint64_t v_stack_pC0;
    uint64_t v_stack_pC8;
    uint64_t v_stack_pD0;
    uint64_t v_stack_pD8;

    *(uint64_t *)(local_rsp + 0x20) = Arg4;
    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (224);
    local_rdi = 0;
    *(uint64_t *)(local_rsp - 0x70) = 0;
    v_stack_mA8 = 0;
    *(uint64_t *)(local_rsp - 0x80) = 0;
    v_stack_mD3 = 0;
    v_stack_mD7 = 0;
    v_stack_mD5 = 0;
    v_stack_mD4 = 0;
    v_stack_mB8 = 0;
    Arg2 = (uint32_t)((Arg2) | (0xFFFFFFFFULL));
    v_stack_mCC = (uint32_t)(Arg2);
    result = HvpGetCellContextInitialize(local_rsp - 112, Arg2, Arg2, Arg1);
    v_stack_m78 = 0;
    v_stack_mC8 = (uint32_t)(Arg2);
    result = HvpGetCellContextInitialize(v_stack_mA8, Arg2, Arg2, Arg1);
    v_stack_m88 = 0;
    result = HvpGetCellContextInitialize(v_stack_m80, Arg2, Arg2, Arg1);
    v_stack_mD8 = 0;
    v_stack_m90 = 0;
    v_stack_mAC = (uint32_t)(Arg2);
    v_stack_m98 = 0;
    v_stack_m60 = 0;
    v_stack_mA0 = 0;
    v_stack_m58 = 0;
    v_stack_mD6 = 0;
    result = CmpGetKcbAtLayerHeight(Arg1, *(uint16_t *)(Arg1 + 0x2), Arg2, Arg1);
    v_stack_mC0 = result;
    result = CmpGetKcbAtLayerHeight(Arg2, *(uint16_t *)(Arg2 + 0x2), Arg2, Arg1);
    v_stack_m50 = result;
    v_stack_m48 = *(uint64_t *)(result + 0x20);
    if (Arg9 != 0) goto loc_00948BBD;
loc_00948292:
    if (((Arg7) & (0xFFFFFFFCULL)) != 0) goto loc_00948E64;
    if (((v_stack_p38) & (1)) != 0) goto loc_009489DC;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x20) + 0x1010)))) & (32)) != 0) goto loc_009489DC;
loc_009482C9:
    if (sign_flag) goto loc_00948E84;
    if (((*(uint32_t *)(*(uint64_t *)(result + 0x20) + 0xA0)) & (0x100000ULL)) != 0) goto loc_00948E94;
    if ((*(uint8_t *)(result + 0x41)) == 1) goto loc_00948EA4;
    if ((*(uint8_t *)(v_rip + 0x4C69A7)) == 0) goto loc_009488B2;
    if (((*(uint32_t *)(result + 0xB8)) & (0x1000000ULL)) == 0) goto loc_009488B2;
loc_00948312:
    Arg1 = (uint16_t)((Arg6) | (256));
    if (1 == 0) { Arg1 = Arg6; }
    Arg2 = (uint16_t)(((uint16_t)(Arg1)) | (512));
    if (((*(uint32_t *)(result + 0xB8)) & (0x2000000ULL)) == 0) { Arg2 = (uint16_t)(Arg1); }
    v_stack_mCE = (uint16_t)(Arg2);
    if (0 != 0) goto loc_009488B9;
loc_00948356:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg5 + 0x18))) & (1));
    v_stack_mB0 = (uint32_t)(Arg1);
    if (Arg9 != 0) goto loc_00948EB4;
loc_00948369:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x28))) >> (31));
    if (((uint32_t)(result)) == 1) goto loc_00948A48;
loc_00948378:
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(arg5 + 0xA0))))) == 0) goto loc_00948ECE;
loc_00948387:
    if (((v_stack_mCE) & (2)) == 0) goto loc_009488FD;
loc_00948392:
    if (Arg9 != 0) goto loc_00948F2F;
    Arg1 = (uint32_t)(v_stack_mB0);
    if (Arg9 != 0) { Arg1 = 1; }
    v_stack_p10 = (uint32_t)(Arg1);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x28)))) != -1) goto loc_00948C21;
    result = (uint32_t)(*(uint32_t *)(result + 0x28));
    if (Arg8 == 0) {
        Arg1 = *(uint64_t *)(result + 0x20);
        result = HvLockHiveFlusherShared(Arg1, Arg2, 512, Arg9);
        v_stack_mD7 = 1;
        v_stack_mD5 = 1;
    }
    if (Arg9 != 0) goto loc_00948B8F;
    if ((*(uint64_t *)(result + 0xF0)) != 0) goto loc_00949083;
    if ((*(uint32_t *)(result + 0xF8)) < 0) goto loc_009490A1;
    if ((*(uint32_t *)(result + 0xF8)) != 0) goto loc_009490F0;
    if ((*(uint32_t *)(result + 0x108)) != 0) goto loc_009490D2;
    result = CmpNameSize(v_stack_p20, Arg2, 512, Arg9);
    result = (uint32_t)(((uint16_t)(result)) + (76));
    v_stack_mAC = (uint32_t)(result);
    v_stack_mF0 = v_stack_m70;
    v_stack_mF8 = v_stack_mB8;
    result = HvAllocateCell(*(uint64_t *)(result + 0x20), (uint32_t)((uint32_t)(result)), (uint32_t)((uint32_t)((uint32_t)(v_stack_p10))), v_stack_mCC);
    if (sign_flag) goto loc_00948BE9;
    if ((uint16_t)(*(uint16_t *)(arg5 + 0x4)) != 0) goto loc_00948A62;
loc_00948485:
    Arg2 = 0;
    result = memset(v_stack_mB8, Arg2, (uint32_t)(v_stack_mAC), v_stack_mCC);
    if ((((uint8_t)(v_stack_mCE)) & (2)) != 0) goto loc_00948A2A;
    *(uint16_t *)(v_stack_mB8) = 0x6B6EULL;
loc_009484AC:
    *(uint8_t *)(v_stack_mB8 + 0xC) = (uint8_t)(*(uint8_t *)(v_rip + 0x4C67E2));
    if ((*(uint8_t *)(v_stack_mC0 + 0x41)) == 3) goto loc_009489FD;
loc_009484C8:
    *(uint16_t *)(v_stack_mB8 + 0x2) = (uint16_t)(v_stack_mCE);
    *(uint64_t *)(v_stack_mB8 + 0x4) = *(uint64_t *)(*(uint8_t *)(v_rip + 0x4C67E2));
    *(uint32_t *)(v_stack_mB8 + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mC0 + 0x28)));
    Arg2 = (uint32_t)((v_stack_mCE) | (0xFFFFFFFFULL));
    *(uint32_t *)(v_stack_mB8 + 0x1C) = (uint32_t)(Arg2);
    *(uint32_t *)(v_stack_mB8 + 0x20) = (uint32_t)(Arg2);
    *(uint32_t *)(v_stack_mB8 + 0x28) = (uint32_t)(Arg2);
    *(uint32_t *)(v_stack_mB8 + 0x2C) = (uint32_t)(Arg2);
    *(uint32_t *)(v_stack_mB8 + 0x30) = (uint32_t)((uint32_t)(v_stack_mC8));
    *(uint16_t *)(v_stack_mB8 + 0x4A) = (uint16_t)(*(uint16_t *)(arg5 + 0x4));
    v_stack_mC8 = (uint32_t)(Arg2);
    result = *(uint16_t *)(arg5 + 0x4);
    if (sign_flag) {
        result = *(uint32_t *)(v_stack_mB8 + 0x34);
        Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_mC0 + 0xB8))) << (16));
        Arg2 = (uint32_t)((Arg2) ^ ((uint32_t)(result)));
        Arg2 = (uint32_t)((Arg2) & (0xF00000ULL));
        Arg2 = (uint32_t)((Arg2) ^ ((uint32_t)(result)));
        *(uint32_t *)(v_stack_mB8 + 0x34) = (uint32_t)(Arg2);
    }
    result = CmpCopyName(v_stack_mB8 + 76, v_stack_p20, (uint32_t)(v_stack_mAC), v_stack_mCC);
    *(uint16_t *)(v_stack_mB8 + 0x48) = (uint16_t)(result);
    if (((uint16_t)(result)) < (*(uint16_t *)(v_stack_p20))) {
    }
    if ((((uint8_t)(v_stack_mCE)) & (2)) != 0) goto loc_009488E9;
loc_00948562:
    v_stack_mD3 = 1;
    if ((((uint8_t)(v_stack_mCE)) & (2)) != 0) goto loc_009485C1;
    result = CmLockHiveSecurityExclusive(*(uint64_t *)(result + 0x20), v_stack_p20, (uint32_t)(v_stack_mAC), v_stack_mCC);
    v_stack_mD8 = 1;
    Arg4 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_mCC)))) >> (31));
    v_stack_mE8 = v_stack_mB8 + 44;
    v_stack_mF0 = 0;
    v_stack_mF8 = v_stack_m90;
    result = CmpGetSecurityDescriptorNodeEx(*(uint64_t *)(result + 0x20), (uint32_t)(v_stack_mCC), v_stack_mB8, Arg4);
    if (sign_flag) goto loc_009489E9;
    result = CmUnlockHiveSecurity(*(uint64_t *)(result + 0x20), (uint32_t)(v_stack_mCC), v_stack_mB8, Arg4);
    v_stack_mD8 = 0;
loc_009485C1:
    Arg4 = 0;
    Arg3 = 0;
    result = HvpMarkCellDirty(*(uint64_t *)(result + 0x20), (uint32_t)(*(uint32_t *)(v_stack_mC0 + 0x28)), Arg3, Arg4);
    if (sign_flag) goto loc_009487C2;
    if (Arg9 != 0) goto loc_0094860D;
    Arg4 = 0;
    result = CmpAddSubKeyEx(*(uint64_t *)(result + 0x20), (uint32_t)(*(uint32_t *)(v_stack_mC0 + 0x28)), (uint32_t)(v_stack_mCC), Arg4);
    if (sign_flag) goto loc_00948BDF;
loc_0094860D:
    v_stack_mD6 = 1;
    *(uint32_t *)(result + 0x28) = (uint32_t)((uint32_t)(v_stack_mCC));
    *(uint64_t *)(result + 0xF0) = Arg9;
    result = Arg9;
    if ((((uint8_t)(v_stack_mCE)) & (64)) == 0) {
        result = *(uint32_t *)(v_stack_mB8 + 0x24);
        *(uint32_t *)(result + 0x60) = (uint32_t)(result);
        result = *(uint32_t *)(v_stack_mB8 + 0x28);
        *(uint32_t *)(result + 0x64) = (uint32_t)(result);
    }
    Arg4 = 0;
    Arg3 = 0;
    result = CmpRebuildKcbCacheFromNode(result, v_stack_mB8, Arg3, Arg4);
    if ((((uint8_t)(v_stack_mCE)) & (2)) != 0) goto loc_009486D3;
    v_stack_p10 = 0;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mB8 + 0x2C)))) == -1) goto loc_00948E2A;
    v_stack_m68 = *(uint64_t *)(result + 0x20);
    result = CmLockHiveSecurityShared(*(uint64_t *)(result + 0x20), v_stack_mB8, Arg3, Arg4);
    result = CmpFindSecurityCellCacheIndex(v_stack_m68, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mB8 + 0x2C)))), v_stack_p10, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00948E33;
    Arg2 = ((uint32_t)(v_stack_p10)) + ((uint32_t)(v_stack_p10));
    *(uint64_t *)(result + 0x58) = *(uint64_t *)(*(uint64_t *)(v_stack_m68 + 0x760) + Arg2 * 8 + 0x8);
    result = CmUnlockHiveSecurity(v_stack_m68, *(uint64_t *)(*(uint64_t *)(v_stack_m68 + 0x760) + Arg2 * 8 + 0x8), v_stack_p10, Arg4);
loc_009486D3:
    if (Arg9 != 0) goto loc_00948B48;
loc_009486E1:
    if (((*(uint8_t *)(*(uint64_t *)(v_stack_mC0 + 0x20) + 0x8C)) & (1)) == 0) goto loc_009489F3;
    result = HvpGetCellFlat(*(uint64_t *)(v_stack_mC0 + 0x20), (uint32_t)(*(uint32_t *)(v_stack_mC0 + 0x28)), v_stack_m80, Arg4);
loc_00948707:
    v_stack_m88 = result;
    result = CmpUpdateKeyNodeAccessBits(*(uint64_t *)(v_stack_mC0 + 0x20), result, (uint32_t)(*(uint32_t *)(v_stack_mC0 + 0x28)), Arg4);
    *(uint64_t *)(result + 0x4) = *(uint64_t *)(result);
    if (((uint32_t)((uint16_t)((uint32_t)(*(uint32_t *)(result + 0x34))))) < ((uint32_t)(*(uint16_t *)(v_stack_p20)))) {
        *(uint16_t *)(result + 0x34) = (uint16_t)(*(uint16_t *)(v_stack_p20));
    }
    if ((*(uint32_t *)(result + 0x38)) < ((uint32_t)(*(uint16_t *)(arg5 + 0x4)))) goto loc_009490C9;
loc_0094875C:
    *(uint16_t *)(v_stack_mC0 + 0xB0) = (uint16_t)(*(uint16_t *)(result + 0x34));
    *(uint64_t *)(v_stack_mC0 + 0xA8) = *(uint64_t *)(result + 0x4);
    result = CmpCleanUpSubKeyInfo(v_stack_mC0, 1, (uint32_t)(*(uint32_t *)(v_stack_mC0 + 0x28)), Arg4);
    if (v_stack_mD7 != 0) {
        Arg1 = *(uint64_t *)(result + 0x20);
        result = HvUnlockHiveFlusherShared(Arg1, 1, (uint32_t)(*(uint32_t *)(v_stack_mC0 + 0x28)), Arg4);
        v_stack_mD7 = 0;
    }
    Arg4 = 0;
    result = CmpReportNotifyForKcbStack(v_stack_p8, Arg9, 1, Arg4);
    v_stack_mD6 = 0;
    goto loc_009487D2;
loc_009487C2:
loc_009487C7:
    result = CmpRecordParseFailure(Arg5, (uint32_t)(0x42200ULL), (uint32_t)((uint32_t)(result)), Arg4);
loc_009487D2:
loc_009487D6:
    if ((uint8_t)(v_stack_mD8) != 0) goto loc_0094910E;
loc_009487DE:
    if (v_stack_mA0 != 0) goto loc_0094911B;
loc_009487F7:
    if (v_stack_m98 != 0) goto loc_00949135;
loc_00948808:
    if (v_stack_m90 != 0) goto loc_0094898F;
loc_00948819:
    if (v_stack_m88 == 0) goto loc_00948846;
    if (((*(uint8_t *)(*(uint64_t *)(v_stack_mC0 + 0x20) + 0x8C)) & (1)) != 0) goto loc_00948A34;
    result = HvpReleaseCellPaged(*(uint64_t *)(v_stack_mC0 + 0x20), v_stack_m80, (uint32_t)((uint32_t)(result)), Arg4);
loc_00948846:
    if (v_stack_m78 != 0) goto loc_00949163;
loc_00948854:
    local_rsi = (uint32_t)((Arg5) | (0xFFFFFFFFULL));
    if (((uint32_t)((uint32_t)(v_stack_mC8))) != ((uint32_t)(local_rsi))) goto loc_00949182;
loc_00948863:
    if (v_stack_mB8 == 0) goto loc_00948885;
    if (((*(uint8_t *)(*(uint64_t *)(result + 0x20) + 0x8C)) & (1)) != 0) goto loc_00948A3E;
    result = HvpReleaseCellPaged(*(uint64_t *)(result + 0x20), v_stack_m70, (uint32_t)((uint32_t)(result)), Arg4);
loc_00948885:
    if (((uint32_t)((uint32_t)(v_stack_mCC))) != ((uint32_t)(local_rsi))) goto loc_0094918F;
loc_00948891:
    if (v_stack_mD7 != 0) goto loc_009491AA;
loc_0094889C:
    local_rsp = (local_rsp) + (224);
    return 0;
loc_009488B2:
    goto loc_00948312;
loc_009488B9:
    if ((*(uint64_t *)(v_stack_p130 + 0x40)) == 0) goto loc_00948356;
loc_009488D6:
loc_009488D9:
    result = CmpRecordParseFailure(local_rsi, (uint32_t)(0x40500ULL), (uint32_t)(0xC0000022ULL), Arg4);
loc_009488E1:
    goto loc_009487D6;
loc_009488E9:
    *(uint64_t *)(v_stack_mB8 + 0x24) = *(uint64_t *)(local_rsi + 0x30);
    *(uint32_t *)(v_stack_mB8 + 0x1C) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x28)));
    goto loc_00948562;
loc_009488FD:
    if (0 != 0) goto loc_00948A06;
    if (((*(uint32_t *)(v_stack_m90 + 0xB8)) & (0x2000000ULL)) != 0) goto loc_00948EF3;
loc_00948917:
loc_00948923:
    Arg3 = 0;
    result = CmpGetSecurityCacheEntryForKcbStack(v_stack_p120, Arg9, Arg3, Arg4);
    local_r10 = (v_stack_p130) + (32);
    v_stack_p30 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x67E17E) + 0x64)));
    v_stack_p28 = *(uint64_t *)(v_rip + 0x67E17E) + 76;
    v_stack_p20 = local_r10;
    result = SeAssignSecurity(result + 32, *(uint64_t *)(v_stack_p130 + 0x40), v_stack_p88, 1);
    if (sign_flag) goto loc_00948F22;
    goto loc_00948392;
loc_0094898F:
    if (v_stack_p44 != 0) goto loc_00948819;
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(local_rsi))))) == 0) goto loc_009489AC;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x18)))) & (4)) != 0) goto loc_00948C03;
loc_009489AC:
    if (((*(uint32_t *)(v_stack_p130 + 0xC)) & (0x4000000ULL)) != 0) goto loc_009489CE;
    if (*(uint64_t *)(*(uint64_t *)(v_stack_p130 + 0x48) + 0x30) != 0) goto loc_0094914F;
loc_009489CE:
    *(uint64_t *)(*(uint64_t *)(v_stack_p130 + 0x48) + 0x30) = v_stack_m90;
    goto loc_00948819;
loc_009489DC:
    v_stack_p44 = 1;
    goto loc_009482C9;
loc_009489E9:
    goto loc_009487C7;
loc_009489F3:
    result = HvpGetCellPaged(*(uint64_t *)(*(uint64_t *)(v_stack_p130 + 0x48) + 0x30), (uint32_t)(0x42100ULL), v_stack_p88, 1);
    goto loc_00948707;
loc_009489FD:
    goto loc_009484C8;
loc_00948A06:
    Arg3 = 0;
    result = CmpGetSecurityCacheEntryForKcbStack(v_stack_p120, 1, Arg3, 1);
    result = (result) + (32);
    v_stack_p88 = result;
    goto loc_00948392;
loc_00948A2A:
    *(uint16_t *)(v_stack_p58) = 0x6B6CULL;
    goto loc_009484AC;
loc_00948A34:
    result = HvpReleaseCellFlat(v_stack_p120, 1, Arg3, 1);
    goto loc_00948846;
loc_00948A3E:
    result = HvpReleaseCellFlat(v_stack_p120, 1, Arg3, 1);
    goto loc_00948885;
loc_00948A48:
    if ((uint32_t)(v_stack_p120) != 0) goto loc_00948378;
    goto loc_009488D9;
loc_00948A62:
    v_stack_p28 = v_stack_p70;
    v_stack_p20 = v_stack_pA0;
    result = HvAllocateCell(*(uint64_t *)(result + 0x20), (uint32_t)((uint32_t)(result)), (uint32_t)((uint32_t)(v_stack_mB8)), v_stack_p50);
    if (sign_flag) goto loc_00948C1A;
    result = memcpy(v_stack_pA0, *(uint64_t *)(*(uint64_t *)(v_stack_p130 + 0x48) + 0x8), *(uint16_t *)(*(uint64_t *)(v_stack_p130 + 0x48) + 0x4), v_stack_p50);
    goto loc_00948B21;
loc_00948B21:
    if (((*(uint8_t *)(*(uint64_t *)(result + 0x20) + 0x8C)) & (1)) != 0) goto loc_00948E20;
    result = HvpReleaseCellPaged(*(uint64_t *)(result + 0x20), v_stack_p70, *(uint16_t *)(*(uint64_t *)(v_stack_p130 + 0x48) + 0x4), v_stack_p50);
loc_00948B3B:
    v_stack_pA0 = 0;
    goto loc_00948485;
loc_00948B48:
    *(uint32_t *)(v_stack_p78 + 0x44) = 0;
    *(uint32_t *)(v_stack_p78 + 0x48) = (uint32_t)((uint32_t)(v_stack_p68));
    *(uint64_t *)(v_stack_p78 + 0x50) = v_stack_p80;
    *(uint32_t *)(v_stack_p80 + 0x44) = 1;
    *(uint64_t *)(v_stack_p80 + 0x58) = v_stack_m90;
    result = CmAddLogForAction(v_stack_p78, 1, *(uint16_t *)(*(uint64_t *)(v_stack_p130 + 0x48) + 0x4), v_stack_p50);
    if (sign_flag) goto loc_009490BF;
    v_stack_p78 = 0;
    v_stack_p80 = 0;
    goto loc_009486E1;
loc_00948B8F:
    result = CmpAllocateUnitOfWork(v_stack_p78, 1, *(uint16_t *)(*(uint64_t *)(v_stack_p130 + 0x48) + 0x4), v_stack_p50);
    v_stack_p80 = result;
    v_stack_pB8 = result;
    if (result != 0) goto loc_0094904C;
    goto loc_009488D6;
loc_00948BBD:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x20) + 0xA0)))) & (2)) == 0) goto loc_00948292;
    goto loc_00948E71;
loc_00948BDF:
    goto loc_009487C7;
loc_00948BE9:
loc_00948BEE:
    result = CmpRecordParseFailure(*(uint64_t *)(v_stack_p130 + 0x48), (uint32_t)(0x41E00ULL), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x20) + 0xA0)))), v_stack_p50);
loc_00948BF9:
    goto loc_009488E1;
loc_00948C03:
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m90, Arg2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x20) + 0xA0)))), v_stack_p50);
    v_stack_p88 = 0;
    goto loc_00948819;
loc_00948C1A:
    goto loc_00948BEE;
loc_00948C21:
    result = (uint32_t)((result) >> (31));
    if (((uint32_t)(v_stack_m90)) != ((uint32_t)(result))) goto loc_00948F7A;
loc_00948C2C:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m90 + 0x28))) >> (31));
    v_stack_p160 = (uint32_t)(result);
    if (Arg8 == 0) goto loc_00948F89;
loc_00948C48:
    if (((*(uint8_t *)(*(uint64_t *)(result + 0x20) + 0x8C)) & (1)) == 0) goto loc_00948E50;
    result = HvpGetCellFlat(*(uint64_t *)(result + 0x20), (uint32_t)(*(uint32_t *)(v_stack_m90 + 0x28)), v_stack_pA8, v_stack_p50);
loc_00948C69:
    v_stack_p60 = result;
    result = CmpNameSize(v_stack_p138, (uint32_t)(*(uint32_t *)(v_stack_m90 + 0x28)), v_stack_pA8, v_stack_p50);
    if (((uint16_t)(result)) != (*(uint16_t *)(result + 0x48))) goto loc_00948FA1;
    Arg3 = 0;
    result = CmpMarkKeyDirty(*(uint64_t *)(result + 0x20), (uint32_t)(*(uint32_t *)(v_stack_m90 + 0x28)), Arg3, v_stack_p50);
    if (sign_flag) goto loc_00948FBB;
    Arg4 = 0;
    Arg3 = 0;
    result = HvpMarkCellDirty(*(uint64_t *)(result + 0x20), (uint32_t)(*(uint32_t *)(v_stack_p58 + 0x28)), Arg3, Arg4);
    if (sign_flag) goto loc_00948FC8;
    if ((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_stack_p130 + 0x48) + 0x4)) != 0) goto loc_00948FD5;
    result = CmLockHiveSecurityExclusive(*(uint64_t *)(result + 0x20), (uint32_t)(*(uint32_t *)(v_stack_p58 + 0x28)), Arg3, Arg4);
    v_stack_p40 = 1;
    Arg4 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m90 + 0x28))))) >> (31));
    v_stack_p30 = v_stack_p6C;
    v_stack_p28 = 1;
    v_stack_p20 = v_stack_p88;
    result = CmpGetSecurityDescriptorNodeEx(*(uint64_t *)(result + 0x20), (uint32_t)(*(uint32_t *)(v_stack_m90 + 0x28)), result, Arg4);
    if (sign_flag) goto loc_0094901A;
    result = CmpFreeSecurityDescriptor(*(uint64_t *)(result + 0x20), (uint32_t)(*(uint32_t *)(v_stack_m90 + 0x28)), result, Arg4);
    *(uint32_t *)(result + 0x2C) = (uint32_t)((uint32_t)(v_stack_p6C));
    result = CmUnlockHiveSecurity(*(uint64_t *)(result + 0x20), (uint32_t)(*(uint32_t *)(v_stack_m90 + 0x28)), result, Arg4);
    *(uint32_t *)(result + 0x30) = (uint32_t)((uint32_t)(v_stack_p50));
    *(uint16_t *)(result + 0x4A) = (uint16_t)(*(uint16_t *)(*(uint64_t *)(v_stack_p130 + 0x48) + 0x4));
    result = CmpCopyName(result + 76, v_stack_p138, result, Arg4);
    *(uint16_t *)(result + 0x2) = (uint16_t)(v_stack_p4A);
    if ((*(uint16_t *)(result + 0x48)) < ((uint16_t)(*(uint16_t *)(v_stack_p138)))) goto loc_00949024;
loc_00948D7B:
    *(uint64_t *)(result + 0x4) = *(uint64_t *)(*(uint16_t *)(v_stack_p138));
    Arg4 = 0;
    Arg3 = 0;
    result = CmpRebuildKcbCacheFromNode(v_stack_m90, result, Arg3, Arg4);
    if (((*(uint8_t *)(*(uint64_t *)(result + 0x20) + 0x8C)) & (1)) == 0) goto loc_00948E5A;
    result = HvpGetCellFlat(*(uint64_t *)(result + 0x20), (uint32_t)(*(uint32_t *)(v_stack_p58 + 0x28)), v_stack_p98, Arg4);
loc_00948DC9:
    v_stack_p90 = result;
    *(uint64_t *)(result + 0x4) = *(uint64_t *)(*(uint16_t *)(v_stack_p138));
    *(uint64_t *)(v_stack_p58 + 0xA8) = *(uint64_t *)(*(uint16_t *)(v_stack_p138));
    if ((*(uint32_t *)(result + 0x38)) < ((uint32_t)(*(uint16_t *)(result + 0x4A)))) goto loc_00949032;
loc_00948DF9:
    if (v_stack_p41 != 0) goto loc_0094903A;
loc_00948E04:
    Arg4 = 0;
    Arg2 = 0;
    result = CmpReportNotifyForKcbStack(v_stack_p120, Arg2, 1, Arg4);
    goto loc_00948BF9;
loc_00948E20:
    result = HvpReleaseCellFlat(v_stack_p120, Arg2, 1, Arg4);
    goto loc_00948B3B;
loc_00948E2A:
    *(uint64_t *)(v_stack_m90 + 0x58) = 0;
    goto loc_009486D3;
loc_00948E33:
    *(uint64_t *)(v_stack_m90 + 0x58) = 0;
    v_stack_p20 = 0;
    result = KeBugCheckEx(4 + 77, 4, 1, v_stack_m90);
loc_00948E50:
    result = HvpGetCellPaged(4 + 77, 4, 1, v_stack_m90);
    goto loc_00948C69;
loc_00948E5A:
    result = HvpGetCellPaged(4 + 77, 4, 1, v_stack_m90);
    goto loc_00948DC9;
loc_00948E64:
loc_00948E71:
    result = CmpRecordParseFailure(*(uint64_t *)(v_stack_p130 + 0x48), (uint32_t)(0x40180ULL), (uint32_t)((uint32_t)((uint32_t)(0xC000000DULL))), v_stack_m90);
    goto loc_009488E1;
loc_00948E84:
    goto loc_009488D6;
loc_00948E94:
    goto loc_009488D6;
loc_00948EA4:
    goto loc_009488D6;
loc_00948EB4:
    if ((*(uint64_t *)((uint32_t)(0xC000000DULL) + 0xF0)) == 0) goto loc_00948369;
    v_stack_pD8 = 0;
loc_00948ECE:
    result = CmpAttachToRegistryProcess(*(uint64_t *)(v_stack_p130 + 0x48) + 168, (uint32_t)(0x40400ULL), (uint32_t)(0xC0000022ULL), v_stack_m90);
    goto loc_00948387;
loc_00948EF3:
    Arg2 = 0;
    result = CmpIsSystemEntity(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232), Arg2, *(uint64_t *)(v_stack_p130 + 0x48) + 16, Arg9);
    if ((uint8_t)(result) != 0) goto loc_00948917;
    goto loc_00948923;
loc_00948F22:
    goto loc_009488D9;
loc_00948F2F:
    Arg2 = 0;
    result = CmpIsKeyStackDeleted(v_stack_p128, Arg2, (uint32_t)((uint32_t)(result)), Arg9);
    result = CmpUndoDeleteKeyForTrans(v_stack_m90, Arg9, v_stack_p88, Arg9);
    if (!sign_flag) goto loc_009488E1;
    goto loc_009488D9;
loc_00948F7A:
    result = CmpLogUnsupportedOperation(2, (uint32_t)(0x40700ULL), (uint32_t)((uint32_t)((uint32_t)(0xC0000034ULL))), Arg9);
    goto loc_00948C2C;
loc_00948F89:
    result = HvLockHiveFlusherShared(*(uint64_t *)(result + 0x20), (uint32_t)(0x40700ULL), (uint32_t)((uint32_t)((uint32_t)(0xC0000034ULL))), Arg9);
    v_stack_p41 = 1;
    v_stack_p43 = 1;
    goto loc_00948C48;
loc_00948FA1:
    result = CmpLogUnsupportedOperation(1, (uint32_t)(0x40700ULL), (uint32_t)((uint32_t)((uint32_t)(0xC0000034ULL))), Arg9);
    goto loc_009488D9;
loc_00948FBB:
    goto loc_009488D9;
loc_00948FC8:
    goto loc_009488D9;
loc_00948FD5:
    v_stack_p28 = v_stack_p70;
    v_stack_p20 = v_stack_pA0;
    result = HvAllocateCell(*(uint64_t *)(result + 0x20), (uint32_t)((uint32_t)(result)), (uint32_t)(Arg9), v_stack_p50);
    goto loc_009488D9;
loc_0094901A:
    goto loc_009487C7;
loc_00949024:
    Arg1 = (uint16_t)((*(uint64_t *)(result + 0x20)) | (32));
    *(uint16_t *)(v_stack_p60 + 0x2) = (uint16_t)(Arg1);
    goto loc_00948D7B;
loc_00949032:
    *(uint32_t *)(Arg1 + 0x38) = (uint32_t)(result);
    goto loc_00948DF9;
loc_0094903A:
    result = HvUnlockHiveFlusherShared(*(uint64_t *)(result + 0x20), (uint32_t)(0x40E00ULL), (uint32_t)((uint32_t)(result)), v_stack_p50);
    v_stack_p41 = 0;
    goto loc_00948E04;
loc_0094904C:
    result = CmpTransEnlistUowInKcb(result, (uint32_t)((uint32_t)(result)), (uint32_t)((uint32_t)(result)), v_stack_p50);
    result = CmpTransEnlistUowInCmTrans(v_stack_p80, Arg9, (uint32_t)((uint32_t)(result)), v_stack_p50);
    goto loc_009488D9;
loc_00949083:
    goto loc_009488D6;
loc_009490A1:
    goto loc_009488D6;
loc_009490BF:
    goto loc_009487C7;
loc_009490C9:
    *(uint32_t *)(v_stack_p60 + 0x38) = (uint32_t)(result);
    goto loc_0094875C;
loc_009490D2:
    goto loc_009488D6;
loc_009490F0:
    goto loc_009488D6;
loc_0094910E:
    result = CmUnlockHiveSecurity(*(uint64_t *)(result + 0x20), (uint32_t)(0x41980ULL), (uint32_t)(0xC0190001ULL), v_stack_p50);
    goto loc_009487DE;
loc_0094911B:
    result = CmpRundownUnitOfWork(v_stack_m90, (uint32_t)(0x41980ULL), (uint32_t)(0xC0190001ULL), v_stack_p50);
    result = ExFreePoolWithTag(v_stack_m90, (uint32_t)(0x77554D43ULL), (uint32_t)(0xC0190001ULL), v_stack_p50);
    goto loc_009487F7;
loc_00949135:
    result = CmpRundownUnitOfWork(v_stack_m90, (uint32_t)(0x77554D43ULL), (uint32_t)(0xC0190001ULL), v_stack_p50);
    result = ExFreePoolWithTag(v_stack_m90, (uint32_t)(0x77554D43ULL), (uint32_t)(0xC0190001ULL), v_stack_p50);
    goto loc_00948808;
loc_0094914F:
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m90, Arg2, (uint32_t)(0xC0190001ULL), v_stack_p50);
    goto loc_009489CE;
loc_00949163:
    result = HvpReleaseCellFlat(*(uint64_t *)(result + 0x20), v_stack_p70, (uint32_t)(0xC0190001ULL), v_stack_p50);
    goto loc_00948854;
loc_00949182:
    result = HvFreeCell(*(uint64_t *)(result + 0x20), v_stack_p70, (uint32_t)(0xC0190001ULL), v_stack_p50);
    goto loc_00948863;
loc_0094918F:
    Arg3 = 0;
    result = CmpFreeKeyByCell(*(uint64_t *)(result + 0x20), v_stack_p70, Arg3, v_stack_p50);
    goto loc_00948891;
loc_009491AA:
    result = HvUnlockHiveFlusherShared(*(uint64_t *)(result + 0x20), v_stack_p70, Arg3, v_stack_p50);
    goto loc_0094889C;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg5` | `+ 0x0` | `32` | `R` |
| `Arg5` | `+ 0x4` | `16` | `R` |
| `Arg5` | `+ 0x8` | `64` | `R` |
| `Arg5` | `+ 0x10` | `64` | `R` |
| `Arg5` | `+ 0x18` | `32` | `R` |
| `Arg5` | `+ 0x28` | `32` | `R` |
| `Arg5` | `+ 0x30` | `64` | `R` |
| `Arg5` | `+ 0xA0` | `32` | `R` |
| `Arg5` | `+ 0xA0` | `32` | `R/W` |
| `Arg5` | `+ 0xA8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0094817C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
