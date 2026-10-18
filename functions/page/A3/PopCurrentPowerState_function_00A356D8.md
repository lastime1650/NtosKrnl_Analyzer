# PopCurrentPowerState

- RVA: `0x00A356D8`–`0x00A35715` (길이 `61` bytes)
- VA: `0x0000000140A356D8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `15`개 명령, `61/61` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **8**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00A356E8` → [PopAcquireRwLockShared](../../text/2D/PopAcquireRwLockShared_function_002D9A40.md) (function, `0x002D9A40`)
- `0x00A35709` → [PopReleaseRwLock](../../text/2D/PopReleaseRwLock_function_002DFBBC.md) (function, `0x002DFBBC`)

### Direct callers
- [PopCalculateCsSummary](../../text/43/PopCalculateCsSummary_function_0043A1B0.md) at `0x0043A225`
- [PopUpdateAcDcState](../../text/4B/PopUpdateAcDcState_function_004B8C68.md) at `0x004B8CBE`
- [PopEsUpdateState](../../text/5D/PopEsUpdateState_function_005DA018.md) at `0x005DA052`
- [PopPowerAggregatorHandleModernStandbyIntent](../76/PopPowerAggregatorHandleModernStandbyIntent_function_007649F0.md) at `0x00764A6A`
- [NtPowerInformation](../95/NtPowerInformation_function_00955D80.md) at `0x00956259`
- [PopCurrentPowerStatePrecise](PopCurrentPowerStatePrecise_function_00A35624.md) at `0x00A3563E`
- [PopDiagTraceGracefulShutdown](../../pagelk/B7/PopDiagTraceGracefulShutdown_function_00B71334.md) at `0x00B71351`
- [PopTransitionSystemPowerStateEx](../../pagelk/B7/PopTransitionSystemPowerStateEx_function_00B7E8C0.md) at `0x00B7F030`
- [PopTransitionSystemPowerStateEx](../../pagelk/B7/PopTransitionSystemPowerStateEx_function_00B7E8C0.md) at `0x00B7F8F4`

### Static image references
- `0x00A356E1` → RVA `0x00F0C238` (`.data`; read)
- `0x00A356ED` → RVA `0x00F0C248` (`.data`; read)
- `0x00A356FE` → RVA `0x00F0C258` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00A356E8` → [PopAcquireRwLockShared](../../text/2D/PopAcquireRwLockShared_function_002D9A40.md) (`PAGE` → `.text`)
  - `0x00A35709` → [PopReleaseRwLock](../../text/2D/PopReleaseRwLock_function_002DFBBC.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A356D8  40 53                           push rbx
00A356DA  48 83 EC 20                     sub rsp, 0x20
00A356DE  48 8B D9                        mov rbx, rcx
00A356E1  48 8D 0D 50 6B 4D 00            lea rcx, [rip + 0x4d6b50]
00A356E8  E8 53 43 8A FF                  call 0x1402d9a40
00A356ED  0F 10 05 54 6B 4D 00            movups xmm0, xmmword ptr [rip + 0x4d6b54]
00A356F4  48 8D 0D 3D 6B 4D 00            lea rcx, [rip + 0x4d6b3d]
00A356FB  0F 11 03                        movups xmmword ptr [rbx], xmm0
00A356FE  0F 10 0D 53 6B 4D 00            movups xmm1, xmmword ptr [rip + 0x4d6b53]
00A35705  0F 11 4B 10                     movups xmmword ptr [rbx + 0x10], xmm1
00A35709  E8 AE A4 8A FF                  call 0x1402dfbbc
00A3570E  48 83 C4 20                     add rsp, 0x20
00A35712  5B                              pop rbx
00A35713  C3                              ret
00A35714  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopCurrentPowerState(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = PopAcquireRwLockShared(v_rip + 5073744, a2, a3, a4);
    *(unsigned __int64 *)(a1) = v_xmm0;
    *(unsigned __int64 *)(a1 + 16) = v_xmm1;
    result = PopReleaseRwLock(v_rip + 5073725, a2, a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopCurrentPowerState(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = PopAcquireRwLockShared(v_rip + 5073744, a2, a3, a4);
    *(uint64_t *)(arg1) = v_xmm0;
    *(uint64_t *)(arg1 + 0x10) = v_xmm1;
    result = PopReleaseRwLock(v_rip + 5073725, a2, a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `128` | `R` |
| `Arg1` | `+ 0x10` | `128` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A356D8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A356D8[BB_00A356D8]
  bb_00A35714[BB_00A35714]
```
