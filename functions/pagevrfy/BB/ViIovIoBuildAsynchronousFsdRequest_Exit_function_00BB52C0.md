# ViIovIoBuildAsynchronousFsdRequest_Exit

- RVA: `0x00BB52C0`–`0x00BB52D8` (길이 `24` bytes)
- VA: `0x0000000140BB52C0`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `8`개 명령, `24/24` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00BB52CD` → [ViSetIoBuildRequestFlag](../../text/6A/ViSetIoBuildRequestFlag_function_006AAE00.md) (function, `0x006AAE00`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00BB52CD` → [ViSetIoBuildRequestFlag](../../text/6A/ViSetIoBuildRequestFlag_function_006AAE00.md) (`PAGEVRFY` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BB52C0  48 83 EC 28                     sub rsp, 0x28
00BB52C4  48 8B 49 40                     mov rcx, qword ptr [rcx + 0x40]
00BB52C8  48 85 C9                        test rcx, rcx
00BB52CB  74 05                           je 0x140bb52d2
00BB52CD  E8 2E 5B AF FF                  call 0x1406aae00
00BB52D2  48 83 C4 28                     add rsp, 0x28
00BB52D6  C3                              ret
00BB52D7  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ViIovIoBuildAsynchronousFsdRequest_Exit(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (*(unsigned __int64 *)(a1 + 64) != 0) {
        result = ViSetIoBuildRequestFlag(*(unsigned __int64 *)(a1 + 64), a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ViIovIoBuildAsynchronousFsdRequest_Exit(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (*(uint64_t *)(arg1 + 0x40) != 0) {
        result = ViSetIoBuildRequestFlag(*(uint64_t *)(arg1 + 0x40), a2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x40` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00BB52C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BB52C0[BB_00BB52C0]
  bb_00BB52CD[BB_00BB52CD]
  bb_00BB52D2[BB_00BB52D2]
  bb_00BB52D7[BB_00BB52D7]
  bb_00BB52C0 -->|branch| bb_00BB52D2
  bb_00BB52C0 -->|fallthrough| bb_00BB52CD
  bb_00BB52CD -->|flow| bb_00BB52D2
```
