# CmpDrainDelayDerefContext

- RVA: `0x0041B9A0`–`0x0041B9B6` (길이 `22` bytes)
- VA: `0x000000014041B9A0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009D540`
- 디코드: `7`개 명령, `22/22` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **28**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [CmDeleteLayeredKey](CmDeleteLayeredKey_function_0041B598.md) at `0x0041B8E4`
- [CmpSaveBootControlSet](../../page/7D/CmpSaveBootControlSet_function_007DC744.md) at `0x007DCB44`
- [CmRestoreKey](../../page/7D/CmRestoreKey_function_007DCF04.md) at `0x007DD500`
- [CmRestoreKey](../../page/7D/CmRestoreKey_function_007DCF04.md) at `0x007DD555`
- [CmRestoreKey](../../page/7D/CmRestoreKey_function_007DCF04.md) at `0x007DDA77`
- [CmRestoreKey](../../page/7D/CmRestoreKey_function_007DCF04.md) at `0x007DDB13`
- [CmpRefreshHive](../../page/7D/CmpRefreshHive_function_007DEAD0.md) at `0x007DED47`
- [CmpCloneHwProfile](../../page/7E/CmpCloneHwProfile_function_007E303C.md) at `0x007E37C4`
- [CmRenameKey](../../page/7E/CmRenameKey_function_007E8F48.md) at `0x007E9613`
- [CmRenameKey](../../page/7E/CmRenameKey_function_007E8F48.md) at `0x007E967C`
- [CmRenameKey](../../page/7E/CmRenameKey_function_007E8F48.md) at `0x007EA160`
- [CmpUnfreezeHive](../../page/7E/CmpUnfreezeHive_function_007EA778.md) at `0x007EA7C2`
- [CmpPrepareDiscardAndReplaceKcbAndUnbackedHigherLayers](../../page/7F/CmpPrepareDiscardAndReplaceKcbAndUnbackedHigherLayers_function_007F1610.md) at `0x007F168F`
- [CmpPrepareToInvalidateAllHigherLayerKcbs](../../page/7F/CmpPrepareToInvalidateAllHigherLayerKcbs_function_007F174C.md) at `0x007F17AF`
- [CmKeyBodyReplicateToVirtual](../../page/84/CmKeyBodyReplicateToVirtual_function_00843FE4.md) at `0x00844243`
- [CmSetValueKey](../../page/84/CmSetValueKey_function_008457C0.md) at `0x00845F5E`
- [CmDeleteValueKey](../../page/84/CmDeleteValueKey_function_008476E8.md) at `0x00847C8D`
- [CmDeleteKey](../../page/84/CmDeleteKey_function_00848E5C.md) at `0x00849370`
- [CmDeleteKey](../../page/84/CmDeleteKey_function_00848E5C.md) at `0x0084942C`
- [CmDeleteKey](../../page/84/CmDeleteKey_function_00848E5C.md) at `0x00849679`
- [sub_0084E786](../../page/84/Unknown_function_0084E786.md) at `0x0084E794`
- [CmpPerformCompleteKcbCacheLookup](../../page/84/CmpPerformCompleteKcbCacheLookup_function_0084FD20.md) at `0x00850773`
- [CmpPerformCompleteKcbCacheLookup](../../page/84/CmpPerformCompleteKcbCacheLookup_function_0084FD20.md) at `0x00850F97`
- [sub_008515D5](../../page/85/Unknown_function_008515D5.md) at `0x00851937`
- [CmQueryKey](../../page/85/CmQueryKey_function_00858240.md) at `0x00858BF5`
- [CmpDoParseKey](../../page/85/CmpDoParseKey_function_0085F750.md) at `0x00860B24`
- [sub_0086560A](../../page/86/Unknown_function_0086560A.md) at `0x00865A24`
- [CmpTransMgrFreeVolatileData](../../page/87/CmpTransMgrFreeVolatileData_function_00874BDC.md) at `0x00874CD9`
- [CmpEnumerateLayeredKey](../../page/94/CmpEnumerateLayeredKey_function_00945E58.md) at `0x0094625B`
- [CmpPerformUnloadKey](../../page/9A/CmpPerformUnloadKey_function_009AFA28.md) at `0x009AFC62`
- [CmpCleanUpKCBCacheTable](../../page/9B/CmpCleanUpKCBCacheTable_function_009B0478.md) at `0x009B0548`
- [CmpCommitLightWeightTransaction](../../page/9B/CmpCommitLightWeightTransaction_function_009B0868.md) at `0x009B091E`
- [CmpCommitLightWeightTransaction](../../page/9B/CmpCommitLightWeightTransaction_function_009B0868.md) at `0x009B0A00`
- [CmpCompleteUnloadKey](../../page/9B/CmpCompleteUnloadKey_function_009B32FC.md) at `0x009B3408`
- [CmpDelayCloseWorker](../../page/9D/CmpDelayCloseWorker_function_009DB8E0.md) at `0x009DBC39`
- [CmQueryKey$fin$0](../../page/B0/CmQueryKey_fin_0_function_00B0E530.md) at `0x00B0E572`
- [sub_00B17CEE](../../page/B1/Unknown_function_00B17CEE.md) at `0x00B17D06`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x0041B9B0` → [sub_0041BA73](Unknown_function_0041BA73.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0041B9A0  40 56                           push rsi
0041B9A2  57                              push rdi
0041B9A3  48 83 EC 28                     sub rsp, 0x28
0041B9A7  0F B6 F2                        movzx esi, dl
0041B9AA  48 8B F9                        mov rdi, rcx
0041B9AD  48 39 09                        cmp qword ptr [rcx], rcx
0041B9B0  0F 84 BD 00 00 00               je 0x14041ba73
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall CmpDrainDelayDerefContext(__int64 a1, unsigned __int8 a2)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
}
```

## 5. (Beta) C Style

```c
void CmpDrainDelayDerefContext(void *Arg1, uint8_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0041B9A0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0041B9A0[BB_0041B9A0]
```
