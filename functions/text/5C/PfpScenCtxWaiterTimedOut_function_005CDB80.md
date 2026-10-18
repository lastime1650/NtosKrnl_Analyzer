# PfpScenCtxWaiterTimedOut

- RVA: `0x005CDB80`–`0x005CDBA9` (길이 `41` bytes)
- VA: `0x00000001405CDB80`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `14`개 명령, `41/41` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x005CDB9E` → [KeSetEvent](../33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)

### Direct callers
- [PfpScenCtxPrefetchWait](../../pagelk/B6/PfpScenCtxPrefetchWait_function_00B6B5B0.md) at `0x00B6B789`
- [PfpScenCtxScenarioSet](../../pagelk/B7/PfpScenCtxScenarioSet_function_00B7CFF0.md) at `0x00B7D0AA`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005CDB80  48 83 EC 28                     sub rsp, 0x28
005CDB84  8B 41 08                        mov eax, dword ptr [rcx + 8]
005CDB87  83 E0 FB                        and eax, 0xfffffffb
005CDB8A  83 C8 08                        or eax, 8
005CDB8D  89 41 08                        mov dword ptr [rcx + 8], eax
005CDB90  48 8B 49 28                     mov rcx, qword ptr [rcx + 0x28]
005CDB94  48 85 C9                        test rcx, rcx
005CDB97  74 0A                           je 0x1405cdba3
005CDB99  45 33 C0                        xor r8d, r8d
005CDB9C  33 D2                           xor edx, edx
005CDB9E  E8 6D 17 D7 FF                  call 0x14033f310
005CDBA3  48 83 C4 28                     add rsp, 0x28
005CDBA7  C3                              ret
005CDBA8  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PfpScenCtxWaiterTimedOut(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 8))) & (0xFFFFFFFBULL));
    result = (unsigned int)((result) | (8));
    *(unsigned int *)(a1 + 8) = (unsigned int)(result);
    if (*(unsigned __int64 *)(a1 + 40) != 0) {
        a3 = 0;
        a2 = 0;
        result = KeSetEvent(*(unsigned __int64 *)(a1 + 40), a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PfpScenCtxWaiterTimedOut(void *Arg1, int32_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x8))) & (0xFFFFFFFBULL));
    result = (uint32_t)((result) | (8));
    *(uint32_t *)(arg1 + 0x8) = (uint32_t)(result);
    if (*(uint64_t *)(arg1 + 0x28) != 0) {
        Arg3 = 0;
        Arg2 = 0;
        result = KeSetEvent(*(uint64_t *)(arg1 + 0x28), Arg2, Arg3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `32` | `R` |
| `Arg1` | `+ 0x8` | `32` | `W` |
| `Arg1` | `+ 0x28` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005CDB80&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005CDB80[BB_005CDB80]
  bb_005CDB99[BB_005CDB99]
  bb_005CDBA3[BB_005CDBA3]
  bb_005CDBA8[BB_005CDBA8]
  bb_005CDB80 -->|branch| bb_005CDBA3
  bb_005CDB80 -->|fallthrough| bb_005CDB99
  bb_005CDB99 -->|flow| bb_005CDBA3
```
