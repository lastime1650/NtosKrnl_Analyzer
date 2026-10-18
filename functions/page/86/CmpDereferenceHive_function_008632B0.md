# CmpDereferenceHive

- RVA: `0x008632B0`–`0x008632D1` (길이 `33` bytes)
- VA: `0x00000001408632B0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `9`개 명령, `33/33` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **18**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x008632C6` → [CmpDeleteHive](CmpDeleteHive_function_0086450C.md) (function, `0x0086450C`)

### Direct callers
- [CmpDoFlushAll](../../text/34/CmpDoFlushAll_function_00349A9C.md) at `0x00349B1C`
- [CmpUnblockTwoHiveWrites](../84/CmpUnblockTwoHiveWrites_function_0084A38C.md) at `0x0084A3BB`
- [CmpUnblockTwoHiveWrites](../84/CmpUnblockTwoHiveWrites_function_0084A38C.md) at `0x0084A3C8`
- [CmpVEExecuteRealStoreParseLogic](../84/CmpVEExecuteRealStoreParseLogic_function_0084CCD4.md) at `0x0084CDAD`
- [CmpVEExecuteRealStoreParseLogic](../84/CmpVEExecuteRealStoreParseLogic_function_0084CCD4.md) at `0x0084CE4B`
- [CmpVEExecuteRealStoreParseLogic](../84/CmpVEExecuteRealStoreParseLogic_function_0084CCD4.md) at `0x0084CED6`
- [CmpBlockHiveWrites](../84/CmpBlockHiveWrites_function_0084CF94.md) at `0x0084D02E`
- [CmpPerformCompleteKcbCacheLookup](../84/CmpPerformCompleteKcbCacheLookup_function_0084FD20.md) at `0x00850BB9`
- [CmpPerformCompleteKcbCacheLookup](../84/CmpPerformCompleteKcbCacheLookup_function_0084FD20.md) at `0x00851216`
- [sub_00851B91](../85/Unknown_function_00851B91.md) at `0x00851D14`
- [CmpUnlockHashEntryByIndex](CmpUnlockHashEntryByIndex_function_00862460.md) at `0x008624BB`
- [sub_008631CA](Unknown_function_008631CA.md) at `0x00863220`
- [CmLoadAppKey](../87/CmLoadAppKey_function_00876FFC.md) at `0x00877366`
- [CmLoadAppKey](../87/CmLoadAppKey_function_00876FFC.md) at `0x00877840`
- [CmLoadAppKey](../87/CmLoadAppKey_function_00876FFC.md) at `0x00877A84`
- [CmLoadAppKey](../87/CmLoadAppKey_function_00876FFC.md) at `0x00877AF4`
- [CmLoadAppKey](../87/CmLoadAppKey_function_00876FFC.md) at `0x00877B30`
- [CmLoadAppKey](../87/CmLoadAppKey_function_00876FFC.md) at `0x00877B47`
- [CmLoadAppKey](../87/CmLoadAppKey_function_00876FFC.md) at `0x00877C5B`
- [CmpDestroyHive](../9B/CmpDestroyHive_function_009B1708.md) at `0x009B174A`
- [CmpLateUnloadHiveWorker](../9B/CmpLateUnloadHiveWorker_function_009B20D0.md) at `0x009B224E`
- [CmpUnlockDeletedHashEntryByKcb](../9B/CmpUnlockDeletedHashEntryByKcb_function_009B3100.md) at `0x009B31B5`
- [CmpUnblockHiveWrites](../A5/CmpUnblockHiveWrites_function_00A5E4B0.md) at `0x00A5E4D4`
- [CmpQuitNextHive](../A7/CmpQuitNextHive_function_00A76990.md) at `0x00A76994`
- [sub_00B168BC](../B1/Unknown_function_00B168BC.md) at `0x00B168CF`
- [sub_00B16988](../B1/Unknown_function_00B16988.md) at `0x00B16988`
- [sub_00B179DA](../B1/Unknown_function_00B179DA.md) at `0x00B17AA3`
- [sub_00B3DFC6](../B3/Unknown_function_00B3DFC6.md) at `0x00B3DFF2`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008632B0  48 83 EC 28                     sub rsp, 0x28
008632B4  B8 FF FF FF FF                  mov eax, 0xffffffff
008632B9  F0 0F C1 81 88 10 00 00         lock xadd dword ptr [rcx + 0x1088], eax
008632C1  83 F8 01                        cmp eax, 1
008632C4  75 05                           jne 0x1408632cb
008632C6  E8 41 12 00 00                  call 0x14086450c
008632CB  48 83 C4 28                     add rsp, 0x28
008632CF  C3                              ret
008632D0  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpDereferenceHive(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = (unsigned int)(0xFFFFFFFFULL);
    if (((unsigned int)((unsigned int)(0xFFFFFFFFULL))) == 1) {
        result = CmpDeleteHive(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CmpDereferenceHive(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = (uint32_t)(0xFFFFFFFFULL);
    if (((uint32_t)((uint32_t)(0xFFFFFFFFULL))) == 1) {
        result = CmpDeleteHive(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x1088` | `32` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008632B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008632B0[BB_008632B0]
  bb_008632C6[BB_008632C6]
  bb_008632CB[BB_008632CB]
  bb_008632D0[BB_008632D0]
  bb_008632B0 -->|branch| bb_008632CB
  bb_008632B0 -->|fallthrough| bb_008632C6
  bb_008632C6 -->|flow| bb_008632CB
```
