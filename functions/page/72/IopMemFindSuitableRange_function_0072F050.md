# IopMemFindSuitableRange

- RVA: `0x0072F050`–`0x0072F071` (길이 `33` bytes)
- VA: `0x000000014072F050`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `10`개 명령, `33/33` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0072F066` → [ArbFindSuitableRange](../70/ArbFindSuitableRange_function_0070E9D0.md) (function, `0x0070E9D0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0072F050  48 83 EC 28                     sub rsp, 0x28
0072F054  48 8B 42 20                     mov rax, qword ptr [rdx + 0x20]
0072F058  44 8B 40 2C                     mov r8d, dword ptr [rax + 0x2c]
0072F05C  41 F6 C0 01                     test r8b, 1
0072F060  74 04                           je 0x14072f066
0072F062  80 4A 43 01                     or byte ptr [rdx + 0x43], 1
0072F066  E8 65 F9 FD FF                  call 0x14070e9d0
0072F06B  48 83 C4 28                     add rsp, 0x28
0072F06F  C3                              ret
0072F070  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopMemFindSuitableRange(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 32) + 44)))) & (1)) != 0) {
    }
    result = ArbFindSuitableRange(a1, a2, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 32) + 44)), a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t IopMemFindSuitableRange(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x20) + 0x2C)))) & (1)) != 0) {
    }
    result = ArbFindSuitableRange(Arg1, Arg2, (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x20) + 0x2C)), a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x20` | `64` | `R` |
| `Arg2` | `+ 0x43` | `8` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0072F050&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0072F050[BB_0072F050]
  bb_0072F062[BB_0072F062]
  bb_0072F066[BB_0072F066]
  bb_0072F070[BB_0072F070]
  bb_0072F050 -->|branch| bb_0072F066
  bb_0072F050 -->|fallthrough| bb_0072F062
  bb_0072F062 -->|flow| bb_0072F066
```
