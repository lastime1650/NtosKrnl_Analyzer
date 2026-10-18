# CmpAttachToRegistryProcess

- RVA: `0x00BC98E0`–`0x00BC9910` (길이 `48` bytes)
- VA: `0x0000000140BC98E0`
- 실행 섹션: `PAGECMRC`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007A1AC`
- 디코드: `12`개 명령, `48/48` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **75**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00BC98F3` → [KeStackAttachProcess](../../text/21/KeStackAttachProcess_function_00216800.md) (function, `0x00216800`)

### Direct callers
- [CmpDoQueryKeyName](../../text/45/CmpDoQueryKeyName_function_00456664.md) at `0x004567EE`
- [CmpLoadKeyCommon](../../text/46/CmpLoadKeyCommon_function_0046E9F8.md) at `0x0046ECEB`
- [CmpLoadKeyCommon](../../text/46/CmpLoadKeyCommon_function_0046E9F8.md) at `0x0046ED9C`
- [CmpLoadKeyCommon](../../text/46/CmpLoadKeyCommon_function_0046E9F8.md) at `0x0046EDD0`
- [CmShutdownSystem1](../../text/66/CmShutdownSystem1_function_0066A5B0.md) at `0x0066A5EF`
- [CmShutdownSystem2](../../text/66/CmShutdownSystem2_function_0066A7FC.md) at `0x0066A888`
- [CmpSaveBootControlSet](../../page/7D/CmpSaveBootControlSet_function_007DC744.md) at `0x007DCACC`
- [CmpHandlePageFileOpenNotification](../../page/7D/CmpHandlePageFileOpenNotification_function_007DF640.md) at `0x007DF6CF`
- [NtCompressKey](../../page/7D/NtCompressKey_function_007DF9D0.md) at `0x007DFB16`
- [NtFreezeRegistry](../../page/7D/NtFreezeRegistry_function_007DFBD0.md) at `0x007DFC4C`
- [NtQueryOpenSubKeys](../../page/7D/NtQueryOpenSubKeys_function_007DFF80.md) at `0x007E00CC`
- [NtQueryOpenSubKeysEx](../../page/7E/NtQueryOpenSubKeysEx_function_007E0190.md) at `0x007E03A4`
- [NtRenameKey](../../page/7E/NtRenameKey_function_007E04B0.md) at `0x007E084A`
- [NtRestoreKey](../../page/7E/NtRestoreKey_function_007E0CC0.md) at `0x007E0E7C`
- [NtRollbackRegistryTransaction](../../page/7E/NtRollbackRegistryTransaction_function_007E0F30.md) at `0x007E0FE4`
- [NtSaveMergedKeys](../../page/7E/NtSaveMergedKeys_function_007E1070.md) at `0x007E12BD`
- [NtThawRegistry](../../page/7E/NtThawRegistry_function_007E1320.md) at `0x007E138B`
- [CmpFreeAllMemory](../../page/7E/CmpFreeAllMemory_function_007E51D0.md) at `0x007E5271`
- [CmReconcileAndValidateAllHives](../../page/7E/CmReconcileAndValidateAllHives_function_007E7D90.md) at `0x007E7DDC`
- [CmReplaceKey](../../page/7E/CmReplaceKey_function_007EA1C8.md) at `0x007EA28F`
- [CmReplaceKey](../../page/7E/CmReplaceKey_function_007EA1C8.md) at `0x007EA40C`
- [CmpDoBuildVirtualStack](../../page/7E/CmpDoBuildVirtualStack_function_007EB4C4.md) at `0x007EB59A`
- [CmpFlushBackupHive](../../page/7E/CmpFlushBackupHive_function_007EC1A8.md) at `0x007EC31B`
- [CmpFlushBackupHive](../../page/7E/CmpFlushBackupHive_function_007EC1A8.md) at `0x007EC439`
- [CmpRmUnDoPhase](../../page/7F/CmpRmUnDoPhase_function_007F0968.md) at `0x007F0A67`
- [CmpRmUnDoPhase](../../page/7F/CmpRmUnDoPhase_function_007F0968.md) at `0x007F0A83`
- [CmpHiveCachePnpNotificationCallback](../../page/7F/CmpHiveCachePnpNotificationCallback_function_007F5D80.md) at `0x007F5DF7`
- [CmpCleanupTransactionState](../../page/84/CmpCleanupTransactionState_function_008428E0.md) at `0x0084291E`
- [CmSetLastWriteTimeKey](../../page/84/CmSetLastWriteTimeKey_function_00843368.md) at `0x008433D9`
- [CmKeyBodyReplicateToVirtual](../../page/84/CmKeyBodyReplicateToVirtual_function_00843FE4.md) at `0x008440DE`
- [CmSetValueKey](../../page/84/CmSetValueKey_function_008457C0.md) at `0x008458DD`
- [CmDeleteValueKey](../../page/84/CmDeleteValueKey_function_008476E8.md) at `0x008477D4`
- [CmDeleteKey](../../page/84/CmDeleteKey_function_00848E5C.md) at `0x00848F63`
- [sub_0084D0A2](../../page/84/Unknown_function_0084D0A2.md) at `0x0084D140`
- [sub_0084E4B5](../../page/84/Unknown_function_0084E4B5.md) at `0x0084E531`
- [sub_008515D5](../../page/85/Unknown_function_008515D5.md) at `0x00851636`
- [CmpCreateKeyControlBlock](../../page/85/CmpCreateKeyControlBlock_function_00851DB0.md) at `0x00852369`
- [CmpWalkOneLevel](../../page/85/CmpWalkOneLevel_function_00852BA0.md) at `0x00852DCC`
- [sub_00855118](../../page/85/Unknown_function_00855118.md) at `0x0085518D`
- [CmpGetSymbolicLinkTarget](../../page/85/CmpGetSymbolicLinkTarget_function_008570A0.md) at `0x00857664`
- [CmQueryKey](../../page/85/CmQueryKey_function_00858240.md) at `0x008582F4`
- [CmpDoParseKey](../../page/85/CmpDoParseKey_function_0085F750.md) at `0x00860516`
- [CmpDoParseKey](../../page/85/CmpDoParseKey_function_0085F750.md) at `0x00860E0D`
- [CmpDoParseKey](../../page/85/CmpDoParseKey_function_0085F750.md) at `0x00861ACD`
- [CmpDoParseKey](../../page/85/CmpDoParseKey_function_0085F750.md) at `0x00861BF3`
- [CmpDoParseKey](../../page/85/CmpDoParseKey_function_0085F750.md) at `0x00861E26`
- [sub_00861F68](../../page/86/Unknown_function_00861F68.md) at `0x00861F8C`
- [CmpCommitDiscardReplacePost](../../page/86/CmpCommitDiscardReplacePost_function_008624D4.md) at `0x00862607`
- [sub_00862CD4](../../page/86/Unknown_function_00862CD4.md) at `0x00862D00`
- [CmLoadAppKey](../../page/87/CmLoadAppKey_function_00876FFC.md) at `0x00877A2C`
- [CmpLinkHiveToMaster](../../page/87/CmpLinkHiveToMaster_function_00877D6C.md) at `0x00877F55`
- [sub_00878374](../../page/87/Unknown_function_00878374.md) at `0x00878378`
- [CmLoadKey](../../page/87/CmLoadKey_function_008787CC.md) at `0x00879055`
- [CmpInitHiveFromFile](../../page/87/CmpInitHiveFromFile_function_008794D4.md) at `0x008799DC`
- [CmpCreateHive](../../page/87/CmpCreateHive_function_00879DF0.md) at `0x00879FCD`
- [NtQueryMultipleValueKey](../../page/8B/NtQueryMultipleValueKey_function_008B13B0.md) at `0x008B1724`
- [NtEnumerateValueKey](../../page/8B/NtEnumerateValueKey_function_008B3B50.md) at `0x008B3F30`
- [NtEnumerateValueKey](../../page/8B/NtEnumerateValueKey_function_008B3B50.md) at `0x008B45C7`
- [sub_008B4B26](../../page/8B/Unknown_function_008B4B26.md) at `0x008B4B4D`
- [CmpCreateChild](../../page/94/CmpCreateChild_function_0094817C.md) at `0x00948ED5`
- [CmpSetKeySecurity](../../page/94/CmpSetKeySecurity_function_0094A124.md) at `0x0094A1E0`
- [sub_0094AD50](../../page/94/Unknown_function_0094AD50.md) at `0x0094AD91`
- [CmpTransMgrCommit](../../page/9A/CmpTransMgrCommit_function_009AE8AC.md) at `0x009AE900`
- [NtCommitRegistryTransaction](../../page/9A/NtCommitRegistryTransaction_function_009AEAF0.md) at `0x009AEBDF`
- [CmSetKeyFlags](../../page/9A/CmSetKeyFlags_function_009AEEA4.md) at `0x009AEF1C`
- [CmpPerformUnloadKey](../../page/9A/CmpPerformUnloadKey_function_009AFA28.md) at `0x009AFCB6`
- [CmpCleanUpKCBCacheTable](../../page/9B/CmpCleanUpKCBCacheTable_function_009B0478.md) at `0x009B04C2`
- [CmpCleanupLightWeightTransaction](../../page/9B/CmpCleanupLightWeightTransaction_function_009B1340.md) at `0x009B1375`
- [CmpTransMgrPrepare](../../page/9B/CmpTransMgrPrepare_function_009B175C.md) at `0x009B17CF`
- [CmpLateUnloadHiveWorker](../../page/9B/CmpLateUnloadHiveWorker_function_009B20D0.md) at `0x009B21D4`
- [CmpDelayCloseWorker](../../page/9D/CmpDelayCloseWorker_function_009DB8E0.md) at `0x009DB949`
- [sub_009DC2FF](../../page/9D/Unknown_function_009DC2FF.md) at `0x009DC3A0`
- [CmpVEExecuteCreateLogic](../../page/A2/CmpVEExecuteCreateLogic_function_00A26F28.md) at `0x00A26FE1`
- [CmpSearchKeyControlBlockTreeEx](../../page/A6/CmpSearchKeyControlBlockTreeEx_function_00A65548.md) at `0x00A655AD`
- [CmpPublishEventForPcaResolver](../../page/A6/CmpPublishEventForPcaResolver_function_00A66AC0.md) at `0x00A66BF2`
- [CmpForceFlushWorker](../../page/A6/CmpForceFlushWorker_function_00A6B030.md) at `0x00A6B0A4`
- [CmEtwRunDown](../../page/A8/CmEtwRunDown_function_00A85AC0.md) at `0x00A85B75`
- [NtFlushKey](../../page/A8/NtFlushKey_function_00A8A030.md) at `0x00A8A1BF`
- [NtFlushKey](../../page/A8/NtFlushKey_function_00A8A030.md) at `0x00A8A276`
- [CmRmFinalizeRecovery](../../page/AB/CmRmFinalizeRecovery_function_00ABEB68.md) at `0x00ABEBF1`
- [CmKeyBodyRemapToVirtual](../../page/AC/CmKeyBodyRemapToVirtual_function_00AC9494.md) at `0x00AC959C`
- [sub_00B169F2](../../page/B1/Unknown_function_00B169F2.md) at `0x00B16A49`
- [sub_00B44216](../../page/B4/Unknown_function_00B44216.md) at `0x00B442B1`
- [CmSaveKeyToBuffer](CmSaveKeyToBuffer_function_00BC9010.md) at `0x00BC90BB`
- [CmInitSystem1](../../init/C5/CmInitSystem1_function_00C559CC.md) at `0x00C55D0D`
- [CmGetSystemDriverList](../../init/C7/CmGetSystemDriverList_function_00C7380C.md) at `0x00C73AB3`

### Static image references
- `0x00BC98E7` → RVA `0x00EF7208` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00BC98F3` → [KeStackAttachProcess](../../text/21/KeStackAttachProcess_function_00216800.md) (`PAGECMRC` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BC98E0  48 83 EC 28                     sub rsp, 0x28
00BC98E4  48 8B D1                        mov rdx, rcx
00BC98E7  48 8B 0D 1A D9 32 00            mov rcx, qword ptr [rip + 0x32d91a]
00BC98EE  48 85 C9                        test rcx, rcx
00BC98F1  74 0B                           je 0x140bc98fe
00BC98F3  E8 08 CF 64 FF                  call 0x140216800
00BC98F8  48 83 C4 28                     add rsp, 0x28
00BC98FC  C3                              ret
00BC98FD  CC                              int3
00BC98FE  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00BC9907  48 8B 89 B8 00 00 00            mov rcx, qword ptr [rcx + 0xb8]
00BC990E  EB E3                           jmp 0x140bc98f3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpAttachToRegistryProcess(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (*(unsigned __int64 *)(v_rip + 3332378) == 0) goto loc_00BC98FE;
loc_00BC98F3:
    result = KeStackAttachProcess(*(unsigned __int64 *)(v_rip + 3332378), a1, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
loc_00BC98FE:
    goto loc_00BC98F3;
}
```

## 5. (Beta) C Style

```c
int64_t CmpAttachToRegistryProcess(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (*(uint64_t *)(v_rip + 0x32D91A) == 0) goto loc_00BC98FE;
loc_00BC98F3:
    result = KeStackAttachProcess(*(uint64_t *)(v_rip + 0x32D91A), Arg1, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
loc_00BC98FE:
    goto loc_00BC98F3;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagecmrc&rva=0x00BC98E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BC98E0[BB_00BC98E0]
  bb_00BC98F3[BB_00BC98F3]
  bb_00BC98FD[BB_00BC98FD]
  bb_00BC98FE[BB_00BC98FE]
  bb_00BC98E0 -->|branch| bb_00BC98FE
  bb_00BC98E0 -->|fallthrough| bb_00BC98F3
  bb_00BC98FD -->|flow| bb_00BC98FE
  bb_00BC98FE -->|branch| bb_00BC98F3
```
