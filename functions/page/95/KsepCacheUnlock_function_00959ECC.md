# KsepCacheUnlock

- RVA: `0x00959ECC`–`0x00959EFD` (길이 `49` bytes)
- VA: `0x0000000140959ECC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `16`개 명령, `49/49` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00959EE4` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x00959EEC` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00959EF1` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)

### Direct callers
- [KsepDbCacheInsertDevice](../74/KsepDbCacheInsertDevice_function_00748C64.md) at `0x00748CDB`
- [KseLookupHardwareId](../74/KseLookupHardwareId_function_0074A62C.md) at `0x0074A70B`
- [KseAddHardwareId](KseAddHardwareId_function_00959254.md) at `0x009592D7`
- [KseQueryDeviceDataList](KseQueryDeviceDataList_function_00959390.md) at `0x00959480`
- [KseResetDeviceCache](KseResetDeviceCache_function_00959CDC.md) at `0x00959D0A`
- [KsepDbCacheQueryDevice](KsepDbCacheQueryDevice_function_00959D20.md) at `0x00959D9B`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00959EE4` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x00959EEC` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00959EF1` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00959ECC  40 53                           push rbx
00959ECE  48 83 EC 20                     sub rsp, 0x20
00959ED2  48 8B D9                        mov rbx, rcx
00959ED5  48 83 C8 FF                     or rax, 0xffffffffffffffff
00959ED9  F0 48 0F C1 01                  lock xadd qword ptr [rcx], rax
00959EDE  24 06                           and al, 6
00959EE0  3C 02                           cmp al, 2
00959EE2  75 05                           jne 0x140959ee9
00959EE4  E8 E7 BE 90 FF                  call 0x140265dd0
00959EE9  48 8B CB                        mov rcx, rbx
00959EEC  E8 0F 77 98 FF                  call 0x1402e1600
00959EF1  E8 BA 39 90 FF                  call 0x14025d8b0
00959EF6  48 83 C4 20                     add rsp, 0x20
00959EFA  5B                              pop rbx
00959EFB  C3                              ret
00959EFC  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KsepCacheUnlock(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = (result) | (-1);
    result = (unsigned __int8)((result) & (6));
    if (((unsigned __int8)(result)) == 2) {
        result = ExfTryToWakePushLock(a1, a2, a3, a4);
    }
    result = KeAbPostRelease(a1, a2, a3, a4);
    result = KeLeaveCriticalRegion(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KsepCacheUnlock(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = (result) | (-1);
    result = (uint8_t)((result) & (6));
    if (((uint8_t)(result)) == 2) {
        result = ExfTryToWakePushLock(Arg1, a2, a3, a4);
    }
    result = KeAbPostRelease(Arg1, a2, a3, a4);
    result = KeLeaveCriticalRegion(Arg1, a2, a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00959ECC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00959ECC[BB_00959ECC]
  bb_00959EE4[BB_00959EE4]
  bb_00959EE9[BB_00959EE9]
  bb_00959EFC[BB_00959EFC]
  bb_00959ECC -->|branch| bb_00959EE9
  bb_00959ECC -->|fallthrough| bb_00959EE4
  bb_00959EE4 -->|flow| bb_00959EE9
```
