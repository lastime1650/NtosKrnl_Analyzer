# CmpReleaseShutdownRundown

- RVA: `0x00BC9880`–`0x00BC98C7` (길이 `71` bytes)
- VA: `0x0000000140BC9880`
- 실행 섹션: `PAGECMRC`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00064C74`
- 디코드: `15`개 명령, `71/71` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **50**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00BC98AE` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x00BC98C0` → [ExfReleaseRundownProtection](../../text/34/ExfReleaseRundownProtection_function_00349EB0.md) (function, `0x00349EB0`)

### Direct callers
- [CmpLoadHiveThread](../../page/7D/CmpLoadHiveThread_function_007DB040.md) at `0x007DBB9D`
- [CmpSaveBootControlSet](../../page/7D/CmpSaveBootControlSet_function_007DC744.md) at `0x007DCBA9`
- [CmOpenKeyForBugCheckRecovery](../../page/7D/CmOpenKeyForBugCheckRecovery_function_007DF3C0.md) at `0x007DF542`
- [CmpAcceptBoot](../../page/7D/CmpAcceptBoot_function_007DF574.md) at `0x007DF625`
- [CmpHandlePageFileOpenNotification](../../page/7D/CmpHandlePageFileOpenNotification_function_007DF640.md) at `0x007DF6FA`
- [NtCompactKeys](../../page/7D/NtCompactKeys_function_007DF730.md) at `0x007DF967`
- [NtCompressKey](../../page/7D/NtCompressKey_function_007DF9D0.md) at `0x007DFB7C`
- [NtLockRegistryKey](../../page/7D/NtLockRegistryKey_function_007DFD60.md) at `0x007DFDFD`
- [NtOpenRegistryTransaction](../../page/7D/NtOpenRegistryTransaction_function_007DFE40.md) at `0x007DFF4A`
- [NtQueryOpenSubKeys](../../page/7D/NtQueryOpenSubKeys_function_007DFF80.md) at `0x007E0137`
- [NtQueryOpenSubKeysEx](../../page/7E/NtQueryOpenSubKeysEx_function_007E0190.md) at `0x007E044F`
- [NtRenameKey](../../page/7E/NtRenameKey_function_007E04B0.md) at `0x007E091B`
- [NtRestoreKey](../../page/7E/NtRestoreKey_function_007E0CC0.md) at `0x007E0EEB`
- [NtRollbackRegistryTransaction](../../page/7E/NtRollbackRegistryTransaction_function_007E0F30.md) at `0x007E100E`
- [NtSaveMergedKeys](../../page/7E/NtSaveMergedKeys_function_007E1070.md) at `0x007E1158`
- [CmReconcileAndValidateAllHives](../../page/7E/CmReconcileAndValidateAllHives_function_007E7D90.md) at `0x007E7DF5`
- [CmFreezeRegistry](../../page/7E/CmFreezeRegistry_function_007E834C.md) at `0x007E84F1`
- [CmThawRegistry](../../page/7E/CmThawRegistry_function_007E8510.md) at `0x007E8652`
- [CmpAssignKeySecurity](../../page/7E/CmpAssignKeySecurity_function_007EC8B0.md) at `0x007ECA45`
- [NtSetInformationKey](../../page/84/NtSetInformationKey_function_00843720.md) at `0x00843B96`
- [NtSetValueKey](../../page/84/NtSetValueKey_function_00844EA0.md) at `0x008455FC`
- [NtDeleteValueKey](../../page/84/NtDeleteValueKey_function_00848770.md) at `0x00848C05`
- [NtDeleteKey](../../page/84/NtDeleteKey_function_00849920.md) at `0x00849C41`
- [sub_0084D18D](../../page/84/Unknown_function_0084D18D.md) at `0x0084D2DC`
- [CmpConstructNameWithStatus](../../page/85/CmpConstructNameWithStatus_function_008562A0.md) at `0x008563A7`
- [CmpConstructName](../../page/85/CmpConstructName_function_00856BE0.md) at `0x00856CDB`
- [NtQueryKey](../../page/86/NtQueryKey_function_008676E0.md) at `0x00867BA7`
- [CmpSecurityMethod](../../page/87/CmpSecurityMethod_function_00870CC0.md) at `0x00870FD6`
- [NtOpenKeyTransactedEx](../../page/87/NtOpenKeyTransactedEx_function_00874EC0.md) at `0x00874FDB`
- [CmCreateKey](../../page/87/CmCreateKey_function_00875020.md) at `0x0087547F`
- [CmOpenKey](../../page/87/CmOpenKey_function_00876350.md) at `0x0087662D`
- [CmOpenKey](../../page/87/CmOpenKey_function_00876350.md) at `0x00876791`
- [CmpCreateHive](../../page/87/CmpCreateHive_function_00879DF0.md) at `0x0087A265`
- [CmpCreateHive](../../page/87/CmpCreateHive_function_00879DF0.md) at `0x0087A51B`
- [CmpReorganizeHive](../../page/87/CmpReorganizeHive_function_0087B92C.md) at `0x0087BA33`
- [NtQueryMultipleValueKey](../../page/8B/NtQueryMultipleValueKey_function_008B13B0.md) at `0x008B18E9`
- [NtEnumerateKey](../../page/8B/NtEnumerateKey_function_008B1F70.md) at `0x008B2363`
- [NtQueryValueKey](../../page/8B/NtQueryValueKey_function_008B2A00.md) at `0x008B2F85`
- [NtEnumerateValueKey](../../page/8B/NtEnumerateValueKey_function_008B3B50.md) at `0x008B4229`
- [CmpSetKeySecurity](../../page/94/CmpSetKeySecurity_function_0094A124.md) at `0x0094A47F`
- [CmpSetKeySecurity](../../page/94/CmpSetKeySecurity_function_0094A124.md) at `0x0094A526`
- [CmpSetKeySecurity](../../page/94/CmpSetKeySecurity_function_0094A124.md) at `0x0094A58A`
- [NtCommitRegistryTransaction](../../page/9A/NtCommitRegistryTransaction_function_009AEAF0.md) at `0x009AEBA5`
- [CmpCloseLightWeightTransaction](../../page/9B/CmpCloseLightWeightTransaction_function_009B1100.md) at `0x009B114A`
- [CmpDoLocalizeNextHive](../../page/9B/CmpDoLocalizeNextHive_function_009B7400.md) at `0x009B7478`
- [NtNotifyChangeMultipleKeys](../../page/9D/NtNotifyChangeMultipleKeys_function_009DC6B0.md) at `0x009DC8A6`
- [NtNotifyChangeMultipleKeys](../../page/9D/NtNotifyChangeMultipleKeys_function_009DC6B0.md) at `0x009DC8D7`
- [NtNotifyChangeMultipleKeys](../../page/9D/NtNotifyChangeMultipleKeys_function_009DC6B0.md) at `0x009DCEBB`
- [NtNotifyChangeMultipleKeys](../../page/9D/NtNotifyChangeMultipleKeys_function_009DC6B0.md) at `0x009DD2CA`
- [NtCreateRegistryTransaction](../../page/A6/NtCreateRegistryTransaction_function_00A61370.md) at `0x00A614D1`
- [CmpForceFlushWorker](../../page/A6/CmpForceFlushWorker_function_00A6B030.md) at `0x00A6B0BA`
- [NtSaveKeyEx](../../page/A8/NtSaveKeyEx_function_00A853C0.md) at `0x00A854C7`
- [NtFlushKey](../../page/A8/NtFlushKey_function_00A8A030.md) at `0x00A8A261`
- [NtCreateKeyTransacted](../../page/AA/NtCreateKeyTransacted_function_00AAF830.md) at `0x00AAF98D`
- [sub_00B25E36](../../page/B2/Unknown_function_00B25E36.md) at `0x00B25E5A`
- [CmSaveKeyToBuffer](CmSaveKeyToBuffer_function_00BC9010.md) at `0x00BC90F7`
- [CmGetSystemDriverList](../../init/C7/CmGetSystemDriverList_function_00C7380C.md) at `0x00C73CB2`

### Static image references
- `0x00BC9884` → RVA `0x00EF7B20` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00BC98AE` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGECMRC` → `.text`)
  - `0x00BC98C0` → [ExfReleaseRundownProtection](../../text/34/ExfReleaseRundownProtection_function_00349EB0.md) (`PAGECMRC` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BC9880  48 83 EC 28                     sub rsp, 0x28
00BC9884  0F 0D 0D 95 E2 32 00            prefetchw byte ptr [rip + 0x32e295]
00BC988B  48 8B 05 8E E2 32 00            mov rax, qword ptr [rip + 0x32e28e]
00BC9892  48 83 E0 FE                     and rax, 0xfffffffffffffffe
00BC9896  48 8D 48 FE                     lea rcx, [rax - 2]
00BC989A  F0 48 0F B1 0D 7D E2 32 00      lock cmpxchg qword ptr [rip + 0x32e27d], rcx
00BC98A3  75 14                           jne 0x140bc98b9
00BC98A5  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00BC98AE  E8 3D 57 69 FF                  call 0x14025eff0
00BC98B3  48 83 C4 28                     add rsp, 0x28
00BC98B7  C3                              ret
00BC98B8  CC                              int3
00BC98B9  48 8D 0D 60 E2 32 00            lea rcx, [rip + 0x32e260]
00BC98C0  E8 EB 05 78 FF                  call 0x140349eb0
00BC98C5  EB DE                           jmp 0x140bc98a5
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpReleaseShutdownRundown(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = (*(unsigned __int64 *)(v_rip + 3334798)) & (-2);
    if (condition_is_not_equal) goto loc_00BC98B9;
loc_00BC98A5:
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
loc_00BC98B9:
    result = ExfReleaseRundownProtection(v_rip + 3334752, a2, a3, a4);
    goto loc_00BC98A5;
}
```

## 5. (Beta) C Style

```c
void CmpReleaseShutdownRundown(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = (*(uint64_t *)(v_rip + 0x32E28E)) & (-2);
    if (condition_is_not_equal) goto loc_00BC98B9;
loc_00BC98A5:
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), a2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
loc_00BC98B9:
    result = ExfReleaseRundownProtection(v_rip + 3334752, a2, a3, a4);
    goto loc_00BC98A5;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagecmrc&rva=0x00BC9880&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BC9880[BB_00BC9880]
  bb_00BC98A5[BB_00BC98A5]
  bb_00BC98B8[BB_00BC98B8]
  bb_00BC98B9[BB_00BC98B9]
  bb_00BC9880 -->|branch| bb_00BC98B9
  bb_00BC9880 -->|fallthrough| bb_00BC98A5
  bb_00BC98B8 -->|flow| bb_00BC98B9
  bb_00BC98B9 -->|branch| bb_00BC98A5
```
