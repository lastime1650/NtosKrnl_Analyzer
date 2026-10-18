# PopGenericEventHandler

- RVA: `0x00A69650`–`0x00A69676` (길이 `38` bytes)
- VA: `0x0000000140A69650`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000704D0`
- 디코드: `14`개 명령, `38/38` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A69666` → [PopIsPlatformAoAcCapable](../../text/49/PopIsPlatformAoAcCapable_function_0049BF40.md) (function, `0x0049BF40`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00A69666` → [PopIsPlatformAoAcCapable](../../text/49/PopIsPlatformAoAcCapable_function_0049BF40.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A69650  48 83 EC 28                     sub rsp, 0x28
00A69654  84 C9                           test cl, cl
00A69656  74 0E                           je 0x140a69666
00A69658  C7 02 01 00 00 00               mov dword ptr [rdx], 1
00A6965E  33 C0                           xor eax, eax
00A69660  48 83 C4 28                     add rsp, 0x28
00A69664  C3                              ret
00A69665  CC                              int3
00A69666  E8 D5 28 A3 FF                  call 0x14049bf40
00A6966B  F6 D8                           neg al
00A6966D  1B C9                           sbb ecx, ecx
00A6966F  83 E1 03                        and ecx, 3
00A69672  89 0A                           mov dword ptr [rdx], ecx
00A69674  EB E8                           jmp 0x140a6965e
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopGenericEventHandler(int a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if ((unsigned __int8)(a1) == 0) goto loc_00A69666;
    *(unsigned int *)(a2) = 1;
loc_00A6965E:
    result = 0;
    v_rsp = (v_rsp) + (40);
    return result;
loc_00A69666:
    result = PopIsPlatformAoAcCapable(a1, a2, a3, a4);
    result = (unsigned __int8)(-(result));
    a1 = (unsigned int)((a1) & (3));
    *(unsigned int *)(a2) = a1;
    goto loc_00A6965E;
}
```

## 5. (Beta) C Style

```c
int64_t PopGenericEventHandler(int32_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if ((uint8_t)(Arg1) == 0) goto loc_00A69666;
    *(uint32_t *)(arg2) = 1;
loc_00A6965E:
    result = 0;
    local_rsp = (local_rsp) + (40);
    return result;
loc_00A69666:
    result = PopIsPlatformAoAcCapable(Arg1, Arg2, a3, a4);
    result = (uint8_t)(-(result));
    Arg1 = (uint32_t)((Arg1) & (3));
    *(uint32_t *)(arg2) = Arg1;
    goto loc_00A6965E;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A69650&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A69650[BB_00A69650]
  bb_00A69658[BB_00A69658]
  bb_00A6965E[BB_00A6965E]
  bb_00A69665[BB_00A69665]
  bb_00A69666[BB_00A69666]
  bb_00A69650 -->|branch| bb_00A69666
  bb_00A69650 -->|fallthrough| bb_00A69658
  bb_00A69658 -->|flow| bb_00A6965E
  bb_00A69665 -->|flow| bb_00A69666
  bb_00A69666 -->|branch| bb_00A6965E
```
