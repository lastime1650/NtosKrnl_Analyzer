# ViIovIoBuildDeviceIoControlRequest_Exit

- RVA: `0x006AAD70`–`0x006AAD88` (길이 `24` bytes)
- VA: `0x00000001406AAD70`
- 실행 섹션: `.text`
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
- `0x006AAD7D` → [ViSetIoBuildRequestFlag](ViSetIoBuildRequestFlag_function_006AAE00.md) (function, `0x006AAE00`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006AAD70  48 83 EC 28                     sub rsp, 0x28
006AAD74  48 8B 49 50                     mov rcx, qword ptr [rcx + 0x50]
006AAD78  48 85 C9                        test rcx, rcx
006AAD7B  74 05                           je 0x1406aad82
006AAD7D  E8 7E 00 00 00                  call 0x1406aae00
006AAD82  48 83 C4 28                     add rsp, 0x28
006AAD86  C3                              ret
006AAD87  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ViIovIoBuildDeviceIoControlRequest_Exit(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (*(unsigned __int64 *)(a1 + 80) != 0) {
        result = ViSetIoBuildRequestFlag(*(unsigned __int64 *)(a1 + 80), a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ViIovIoBuildDeviceIoControlRequest_Exit(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (*(uint64_t *)(arg1 + 0x50) != 0) {
        result = ViSetIoBuildRequestFlag(*(uint64_t *)(arg1 + 0x50), a2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x50` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006AAD70&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006AAD70[BB_006AAD70]
  bb_006AAD7D[BB_006AAD7D]
  bb_006AAD82[BB_006AAD82]
  bb_006AAD87[BB_006AAD87]
  bb_006AAD70 -->|branch| bb_006AAD82
  bb_006AAD70 -->|fallthrough| bb_006AAD7D
  bb_006AAD7D -->|flow| bb_006AAD82
```
