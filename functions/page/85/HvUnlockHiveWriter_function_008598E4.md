# HvUnlockHiveWriter

- RVA: `0x008598E4`–`0x00859914` (길이 `48` bytes)
- VA: `0x00000001408598E4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `16`개 명령, `48/48` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **25**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00859900` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x00859908` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)

### Direct callers
- [CmpLoadHiveThread](../7D/CmpLoadHiveThread_function_007DB040.md) at `0x007DB7EB`
- [CmpMountPreloadedHives](../7D/CmpMountPreloadedHives_function_007DBE18.md) at `0x007DC271`
- [CmpMountPreloadedHives](../7D/CmpMountPreloadedHives_function_007DBE18.md) at `0x007DC2C2`
- [CmpRefreshHive](../7D/CmpRefreshHive_function_007DEAD0.md) at `0x007DEBDF`
- [CmpRefreshHive](../7D/CmpRefreshHive_function_007DEAD0.md) at `0x007DEBF4`
- [CmFreezeRegistry](../7E/CmFreezeRegistry_function_007E834C.md) at `0x007E842F`
- [CmThawRegistry](../7E/CmThawRegistry_function_007E8510.md) at `0x007E85D2`
- [CmpRecoverFlushProtocolStateFromFiles](../7E/CmpRecoverFlushProtocolStateFromFiles_function_007EE4B0.md) at `0x007EE50D`
- [HvIsRangeDirty](../7F/HvIsRangeDirty_function_007F39BC.md) at `0x007F39FC`
- [sub_008581ED](Unknown_function_008581ED.md) at `0x00858226`
- [HvMarkCellDirty](HvMarkCellDirty_function_00859758.md) at `0x0085981F`
- [HvMarkCellDirty](HvMarkCellDirty_function_00859758.md) at `0x00859885`
- [HvAllocateCell](HvAllocateCell_function_00859C94.md) at `0x00859DBE`
- [HvAllocateCell](HvAllocateCell_function_00859C94.md) at `0x00859E94`
- [sub_00859FB9](Unknown_function_00859FB9.md) at `0x0085A0D0`
- [sub_0085A1B4](Unknown_function_0085A1B4.md) at `0x0085A1B7`
- [HvFreeCell](HvFreeCell_function_0085A72C.md) at `0x0085A8F5`
- [CmpCreateHive](../87/CmpCreateHive_function_00879DF0.md) at `0x0087A226`
- [CmpReorganizeHive](../87/CmpReorganizeHive_function_0087B92C.md) at `0x0087BAFD`
- [CmpInitCmRM](../87/CmpInitCmRM_function_0087C700.md) at `0x0087CE77`
- [CmpTransMgrSyncHive](../9B/CmpTransMgrSyncHive_function_009B07C4.md) at `0x009B083C`
- [CmpTransMgrPrepare](../9B/CmpTransMgrPrepare_function_009B175C.md) at `0x009B191F`
- [CmpFlushHive](../9B/CmpFlushHive_function_009B3DC0.md) at `0x009B44A2`
- [CmpFlushHive](../9B/CmpFlushHive_function_009B3DC0.md) at `0x009B4852`
- [CmpDoLocalizeNextHive](../9B/CmpDoLocalizeNextHive_function_009B7400.md) at `0x009B7453`
- [HvFoldBackDirtyData](../A4/HvFoldBackDirtyData_function_00A463B8.md) at `0x00A46440`
- [CmpTrimHive](../A4/CmpTrimHive_function_00A4F2FC.md) at `0x00A4F360`
- [CmpMarkEntireIndexDirty](../AA/CmpMarkEntireIndexDirty_function_00AA24B4.md) at `0x00AA251E`
- [CmpCreateHiveRootCell](../AB/CmpCreateHiveRootCell_function_00ABF568.md) at `0x00ABF763`
- [sub_00B1845C](../B1/Unknown_function_00B1845C.md) at `0x00B186F3`
- [sub_00B1845C](../B1/Unknown_function_00B1845C.md) at `0x00B187EB`
- [sub_00B1845C](../B1/Unknown_function_00B1845C.md) at `0x00B18908`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00859900` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x00859908` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008598E4  40 53                           push rbx
008598E6  48 83 EC 20                     sub rsp, 0x20
008598EA  48 8D 59 50                     lea rbx, [rcx + 0x50]
008598EE  48 83 C8 FF                     or rax, 0xffffffffffffffff
008598F2  F0 48 0F C1 03                  lock xadd qword ptr [rbx], rax
008598F7  24 06                           and al, 6
008598F9  3C 02                           cmp al, 2
008598FB  75 08                           jne 0x140859905
008598FD  48 8B CB                        mov rcx, rbx
00859900  E8 CB C4 A0 FF                  call 0x140265dd0
00859905  48 8B CB                        mov rcx, rbx
00859908  E8 F3 7C A8 FF                  call 0x1402e1600
0085990D  48 83 C4 20                     add rsp, 0x20
00859911  5B                              pop rbx
00859912  C3                              ret
00859913  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HvUnlockHiveWriter(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = (result) | (-1);
    result = (unsigned __int8)((result) & (6));
    if (((unsigned __int8)(result)) == 2) {
        a1 = a1 + 80;
        result = ExfTryToWakePushLock(a1, a2, a3, a4);
    }
    result = KeAbPostRelease(a1 + 80, a2, a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HvUnlockHiveWriter(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = (result) | (-1);
    result = (uint8_t)((result) & (6));
    if (((uint8_t)(result)) == 2) {
        Arg1 = Arg1 + 80;
        result = ExfTryToWakePushLock(Arg1, a2, a3, a4);
    }
    result = KeAbPostRelease(Arg1 + 80, a2, a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R/W` |
| `Arg1` | `+ 0x50` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008598E4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008598E4[BB_008598E4]
  bb_008598FD[BB_008598FD]
  bb_00859905[BB_00859905]
  bb_00859913[BB_00859913]
  bb_008598E4 -->|branch| bb_00859905
  bb_008598E4 -->|fallthrough| bb_008598FD
  bb_008598FD -->|flow| bb_00859905
```
