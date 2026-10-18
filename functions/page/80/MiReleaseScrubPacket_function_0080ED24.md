# MiReleaseScrubPacket

- RVA: `0x0080ED24`–`0x0080ED50` (길이 `44` bytes)
- VA: `0x000000014080ED24`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `14`개 명령, `44/44` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0080ED31` → [MiDeleteUltraThreadContext](../../text/32/MiDeleteUltraThreadContext_function_00322C90.md) (function, `0x00322C90`)
- `0x0080ED44` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [MiInitializeScrubPacket](MiInitializeScrubPacket_function_0080EA10.md) at `0x0080EAB7`
- [MiScrubMemoryWorker](MiScrubMemoryWorker_function_0080EE00.md) at `0x0080EE2B`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x0080ED31` → [MiDeleteUltraThreadContext](../../text/32/MiDeleteUltraThreadContext_function_00322C90.md) (`PAGE` → `.text`)
  - `0x0080ED44` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0080ED24  40 53                           push rbx
0080ED26  48 83 EC 20                     sub rsp, 0x20
0080ED2A  48 8B D9                        mov rbx, rcx
0080ED2D  48 83 C1 30                     add rcx, 0x30
0080ED31  E8 5A 3F B1 FF                  call 0x140322c90
0080ED36  48 8B 8B B0 00 00 00            mov rcx, qword ptr [rbx + 0xb0]
0080ED3D  48 85 C9                        test rcx, rcx
0080ED40  74 07                           je 0x14080ed49
0080ED42  33 D2                           xor edx, edx
0080ED44  E8 27 3B 37 00                  call 0x140b82870
0080ED49  48 83 C4 20                     add rsp, 0x20
0080ED4D  5B                              pop rbx
0080ED4E  C3                              ret
0080ED4F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiReleaseScrubPacket(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    a1 = (a1) + (48);
    result = MiDeleteUltraThreadContext(a1, a2, a3, a4);
    if (*(unsigned __int64 *)(a1 + 176) != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(a1 + 176), a2, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiReleaseScrubPacket(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    Arg1 = (Arg1) + (48);
    result = MiDeleteUltraThreadContext(Arg1, Arg2, a3, a4);
    if (*(uint64_t *)(arg1 + 0xB0) != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(arg1 + 0xB0), Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xB0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0080ED24&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0080ED24[BB_0080ED24]
  bb_0080ED42[BB_0080ED42]
  bb_0080ED49[BB_0080ED49]
  bb_0080ED4F[BB_0080ED4F]
  bb_0080ED24 -->|branch| bb_0080ED49
  bb_0080ED24 -->|fallthrough| bb_0080ED42
  bb_0080ED42 -->|flow| bb_0080ED49
```
