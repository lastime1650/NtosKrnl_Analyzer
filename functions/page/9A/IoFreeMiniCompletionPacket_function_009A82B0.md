# IoFreeMiniCompletionPacket

- RVA: `0x009A82B0`–`0x009A82C4` (길이 `20` bytes)
- VA: `0x00000001409A82B0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `6`개 명령, `20/20` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x009A82B9` → [IopFreeMiniCompletionPacket](IopFreeMiniCompletionPacket_function_009A82D0.md) (function, `0x009A82D0`)

### Direct callers
- [ExpWorkerFactoryCompletionPacketRoutine](../../text/34/ExpWorkerFactoryCompletionPacketRoutine_function_00344810.md) at `0x00344935`
- [AlpcpLookasidePacketCallbackRoutine](../../text/41/AlpcpLookasidePacketCallbackRoutine_function_00419D50.md) at `0x00419EBB`
- [AlpcpDeferredFreeCompletionPacketLookaside](../../text/47/AlpcpDeferredFreeCompletionPacketLookaside_function_0047BC14.md) at `0x0047BC31`
- [ExpDeleteWorkerFactory](../../text/48/ExpDeleteWorkerFactory_function_00486880.md) at `0x004868FF`
- [PspJobDelete](../../text/4B/PspJobDelete_function_004BF8F0.md) at `0x004BFB41`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009A82B0  48 83 EC 28                     sub rsp, 0x28
009A82B4  48 83 61 38 00                  and qword ptr [rcx + 0x38], 0
009A82B9  E8 12 00 00 00                  call 0x1409a82d0
009A82BE  48 83 C4 28                     add rsp, 0x28
009A82C2  C3                              ret
009A82C3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IoFreeMiniCompletionPacket(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = IopFreeMiniCompletionPacket(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t IoFreeMiniCompletionPacket(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = IopFreeMiniCompletionPacket(Arg1, a2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x38` | `64` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009A82B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009A82B0[BB_009A82B0]
  bb_009A82C3[BB_009A82C3]
```
