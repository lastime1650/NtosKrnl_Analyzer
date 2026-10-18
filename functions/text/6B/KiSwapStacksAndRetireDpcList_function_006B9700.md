# KiSwapStacksAndRetireDpcList

- RVA: `0x006B9700`–`0x006B9714` (길이 `20` bytes)
- VA: `0x00000001406B9700`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C2320`
- 디코드: `9`개 명령, `20/20` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [KiDispatchInterrupt](../21/KiDispatchInterrupt_function_0021B7F0.md) at `0x0021B850`
- [KiSearchForNewThreadsWithinSearchContext](../35/KiSearchForNewThreadsWithinSearchContext_function_00353B30.md) at `0x00353CE0`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006B970C` → [KxSwapStacksAndRetireDpcList](KxSwapStacksAndRetireDpcList_function_006B9720.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006B9700  48 55                           push rbp
006B9702  48 8B EC                        mov rbp, rsp
006B9705  48 89 62 40                     mov qword ptr [rdx + 0x40], rsp
006B9709  48 8B E2                        mov rsp, rdx
006B970C  EB 12                           jmp 0x1406b9720
006B970E  CC                              int3
006B970F  48 8B E5                        mov rsp, rbp
006B9712  5D                              pop rbp
006B9713  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall KiSwapStacksAndRetireDpcList(__int64 a1, __int64 a2)
{
    *(unsigned __int64 *)(a2 + 64) = v_rsp;
}
```

## 5. (Beta) C Style

```c
void KiSwapStacksAndRetireDpcList(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    *(uint64_t *)(arg2 + 0x40) = local_rsp;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x40` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006B9700&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006B9700[BB_006B9700]
  bb_006B970E[BB_006B970E]
```
