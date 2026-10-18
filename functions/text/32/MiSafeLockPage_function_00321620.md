# MiSafeLockPage

- RVA: `0x00321620`–`0x00321636` (길이 `22` bytes)
- VA: `0x0000000140321620`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000756EC`
- 디코드: `5`개 명령, `22/22` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **40**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MiCopySinglePage](../22/MiCopySinglePage_function_00228FA4.md) at `0x0022911A`
- [MiReleaseArbitraryPage](../22/MiReleaseArbitraryPage_function_0022A28C.md) at `0x0022A2C4`
- [MiMapArbitraryPage](../22/MiMapArbitraryPage_function_0022A44C.md) at `0x0022A4A1`
- [MiLockPageAndSetDirty](../28/MiLockPageAndSetDirty_function_002857A0.md) at `0x002858CA`
- [MiTradeTransitionPage](../28/MiTradeTransitionPage_function_0028B9AC.md) at `0x0028BB53`
- [MiTradePage](../28/MiTradePage_function_0028D160.md) at `0x0028D1E5`
- [MiCheckProtoPtePageState](../31/MiCheckProtoPtePageState_function_003183E0.md) at `0x0031847C`
- [MiPfnsWorthTrying](../31/MiPfnsWorthTrying_function_0031B0C0.md) at `0x0031B58B`
- [MiActivePageClaimCandidate](../31/MiActivePageClaimCandidate_function_0031BB00.md) at `0x0031BFAF`
- [MmSetPfnListInfo](../31/MmSetPfnListInfo_function_0031D61C.md) at `0x0031D6C7`
- [sub_0031EA17](../31/Unknown_function_0031EA17.md) at `0x0031EA6D`
- [sub_0031F8A6](../31/Unknown_function_0031F8A6.md) at `0x0031F95A`
- [MiLockProtoPoolPageForce](MiLockProtoPoolPageForce_function_00320E10.md) at `0x00320EDE`
- [MiUpdatePfnForPrefetchByPte](MiUpdatePfnForPrefetchByPte_function_00321210.md) at `0x0032127B`
- [MiComputeCombineHash](MiComputeCombineHash_function_003227C0.md) at `0x00322869`
- [MiInPageSingleKernelStack](../36/MiInPageSingleKernelStack_function_0036A3E8.md) at `0x0036A630`
- [MiProcessLargeCoalesceBitmapCandidates](../37/MiProcessLargeCoalesceBitmapCandidates_function_0037A3F0.md) at `0x0037A4A7`
- [MiGatherMappedPages](../40/MiGatherMappedPages_function_00404E80.md) at `0x00404F21`
- [MiAddToReservationCluster](../40/MiAddToReservationCluster_function_00405474.md) at `0x00405507`
- [MiLockTransitionLeafPageEx](../40/MiLockTransitionLeafPageEx_function_00405884.md) at `0x00405A8E`
- [MiFillNoReservationCluster](../40/MiFillNoReservationCluster_function_00405B40.md) at `0x00405BB9`
- [MiFillNoReservationCluster](../40/MiFillNoReservationCluster_function_00405B40.md) at `0x00405CEE`
- [MiBuildReservationCluster](../40/MiBuildReservationCluster_function_004071A0.md) at `0x0040725A`
- [MiSetPageZeroInProgress](../43/MiSetPageZeroInProgress_function_0043B980.md) at `0x0043BBB3`
- [MiCapturePfnVm](../46/MiCapturePfnVm_function_00465570.md) at `0x004655F3`
- [MiGetPfnPageSizeIndexUnsynchronized](../46/MiGetPfnPageSizeIndexUnsynchronized_function_0046C008.md) at `0x0046C111`
- [MiMakePageBad](../48/MiMakePageBad_function_00486F04.md) at `0x00486F50`
- [MiMapSystemCachePage](../4D/MiMapSystemCachePage_function_004D3588.md) at `0x004D35E4`
- [MiFreeModifiedReservations](../4F/MiFreeModifiedReservations_function_004FA318.md) at `0x004FA3A3`
- [MiReferencePagePartition](../67/MiReferencePagePartition_function_00679304.md) at `0x00679371`
- [MiRemoveBadPages](../67/MiRemoveBadPages_function_00679F6C.md) at `0x00679FE1`
- [MiUnlinkBadPages](../67/MiUnlinkBadPages_function_0067A6FC.md) at `0x0067A77D`
- [MiUpdateBadPfnIdentity](../67/MiUpdateBadPfnIdentity_function_0067A890.md) at `0x0067A939`
- [MmGetPageBadStatus](../67/MmGetPageBadStatus_function_0067A9B0.md) at `0x0067A9E0`
- [MmMarkPhysicalMemoryAsBad](../67/MmMarkPhysicalMemoryAsBad_function_0067AA50.md) at `0x0067AB5F`
- [MmMarkPhysicalMemoryAsBad](../67/MmMarkPhysicalMemoryAsBad_function_0067AA50.md) at `0x0067ABFF`
- [MmMarkPhysicalMemoryAsBad](../67/MmMarkPhysicalMemoryAsBad_function_0067AA50.md) at `0x0067AE62`
- [MiLocateSharedPageViews](../67/MiLocateSharedPageViews_function_0067F1E4.md) at `0x0067F221`
- [MiMarkFileOnlyPfnBad](../68/MiMarkFileOnlyPfnBad_function_006815C4.md) at `0x0068161D`
- [MiMoveModifiedPagesToCompressList](../69/MiMoveModifiedPagesToCompressList_function_006925D8.md) at `0x0069261F`
- [MiScrubLargePage](../69/MiScrubLargePage_function_006942E8.md) at `0x006943E9`
- [MiScrubLargePage](../69/MiScrubLargePage_function_006942E8.md) at `0x00694723`
- [MiScrubLargePage](../69/MiScrubLargePage_function_006942E8.md) at `0x006947D8`
- [MiScanPagefileSpace](../../page/80/MiScanPagefileSpace_function_00800440.md) at `0x00800558`
- [MmIsMdlPageLocked](../../pagevrfy/BB/MmIsMdlPageLocked_function_00BB46E8.md) at `0x00BB472B`

### Static image references
- `0x00321626` → RVA `0x00E2DCE0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00321630` → [sub_003216BB](Unknown_function_003216BB.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00321620  40 57                           push rdi
00321622  48 83 EC 20                     sub rsp, 0x20
00321626  48 3B 0D B3 C6 B0 00            cmp rcx, qword ptr [rip + 0xb0c6b3]
0032162D  48 8B F9                        mov rdi, rcx
00321630  0F 87 85 00 00 00               ja 0x1403216bb
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall MiSafeLockPage(__int64 a1)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
}
```

## 5. (Beta) C Style

```c
void MiSafeLockPage(int64_t Arg1)
{
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00321620&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00321620[BB_00321620]
```
