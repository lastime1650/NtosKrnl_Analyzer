# CmpVolumeContextUnlockExclusive

- RVA: `0x007E8A34`–`0x007E8A64` (길이 `48` bytes)
- VA: `0x00000001407E8A34`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `16`개 명령, `48/48` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x007E8A50` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x007E8A58` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)

### Direct callers
- [CmpVolumeManagerCreateContextsForWellKnownVolumes](../70/CmpVolumeManagerCreateContextsForWellKnownVolumes_function_007023B0.md) at `0x00702414`
- [CmpVolumeContextSendDeviceUsageNotification](CmpVolumeContextSendDeviceUsageNotification_function_007E87DC.md) at `0x007E8824`
- [CmpVolumeContextSendDeviceUsageNotification](CmpVolumeContextSendDeviceUsageNotification_function_007E87DC.md) at `0x007E8884`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x007E8A50` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x007E8A58` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007E8A34  40 53                           push rbx
007E8A36  48 83 EC 20                     sub rsp, 0x20
007E8A3A  48 8D 59 38                     lea rbx, [rcx + 0x38]
007E8A3E  48 83 C8 FF                     or rax, 0xffffffffffffffff
007E8A42  F0 48 0F C1 03                  lock xadd qword ptr [rbx], rax
007E8A47  24 06                           and al, 6
007E8A49  3C 02                           cmp al, 2
007E8A4B  75 08                           jne 0x1407e8a55
007E8A4D  48 8B CB                        mov rcx, rbx
007E8A50  E8 7B D3 A7 FF                  call 0x140265dd0
007E8A55  48 8B CB                        mov rcx, rbx
007E8A58  E8 A3 8B AF FF                  call 0x1402e1600
007E8A5D  48 83 C4 20                     add rsp, 0x20
007E8A61  5B                              pop rbx
007E8A62  C3                              ret
007E8A63  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpVolumeContextUnlockExclusive(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = (result) | (-1);
    result = (unsigned __int8)((result) & (6));
    if (((unsigned __int8)(result)) == 2) {
        a1 = a1 + 56;
        result = ExfTryToWakePushLock(a1, a2, a3, a4);
    }
    result = KeAbPostRelease(a1 + 56, a2, a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CmpVolumeContextUnlockExclusive(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = (result) | (-1);
    result = (uint8_t)((result) & (6));
    if (((uint8_t)(result)) == 2) {
        Arg1 = Arg1 + 56;
        result = ExfTryToWakePushLock(Arg1, a2, a3, a4);
    }
    result = KeAbPostRelease(Arg1 + 56, a2, a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R/W` |
| `Arg1` | `+ 0x38` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007E8A34&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007E8A34[BB_007E8A34]
  bb_007E8A4D[BB_007E8A4D]
  bb_007E8A55[BB_007E8A55]
  bb_007E8A63[BB_007E8A63]
  bb_007E8A34 -->|branch| bb_007E8A55
  bb_007E8A34 -->|fallthrough| bb_007E8A4D
  bb_007E8A4D -->|flow| bb_007E8A55
```
