# PopDirectedDripsDiagGetOrCreateDeviceDiagnostic

- RVA: `0x00705170`–`0x0070518B` (길이 `27` bytes)
- VA: `0x0000000140705170`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `8`개 명령, `27/27` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00705180` → [PopDirectedDripsDiagCreateDeviceDiagnostic](../77/PopDirectedDripsDiagCreateDeviceDiagnostic_function_007710D4.md) (function, `0x007710D4`)

### Direct callers
- [PopDirectedDripsDiagBroadcastTreeBegin](../A9/PopDirectedDripsDiagBroadcastTreeBegin_function_00A955E8.md) at `0x00A9564B`
- [PopDirectedDripsDiagTraceMarkDevice](../A9/PopDirectedDripsDiagTraceMarkDevice_function_00A97DE0.md) at `0x00A97E39`
- [PopDirectedDripsDiagTraceBroadcastVisit](../AC/PopDirectedDripsDiagTraceBroadcastVisit_function_00ACA95C.md) at `0x00ACA9E4`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00705170  48 83 EC 28                     sub rsp, 0x28
00705174  48 8B 81 08 03 00 00            mov rax, qword ptr [rcx + 0x308]
0070517B  48 85 C0                        test rax, rax
0070517E  75 05                           jne 0x140705185
00705180  E8 4F BF 06 00                  call 0x1407710d4
00705185  48 83 C4 28                     add rsp, 0x28
00705189  C3                              ret
0070518A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopDirectedDripsDiagGetOrCreateDeviceDiagnostic(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = *(unsigned __int64 *)(a1 + 776);
    if (*(unsigned __int64 *)(a1 + 776) == 0) {
        result = PopDirectedDripsDiagCreateDeviceDiagnostic(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopDirectedDripsDiagGetOrCreateDeviceDiagnostic(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = *(uint64_t *)(arg1 + 0x308);
    if (*(uint64_t *)(arg1 + 0x308) == 0) {
        result = PopDirectedDripsDiagCreateDeviceDiagnostic(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x308` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00705170&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00705170[BB_00705170]
  bb_00705180[BB_00705180]
  bb_00705185[BB_00705185]
  bb_0070518A[BB_0070518A]
  bb_00705170 -->|branch| bb_00705185
  bb_00705170 -->|fallthrough| bb_00705180
  bb_00705180 -->|flow| bb_00705185
```
