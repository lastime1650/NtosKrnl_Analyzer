# sub_002D899F

- RVA: `0x002D899F`–`0x002D89CB` (길이 `44` bytes)
- VA: `0x00000001402D899F`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007024C`
- 디코드: `12`개 명령, `44/44` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x002D89C6` → [KiIntSteerCalculatePriorityDistribution + 0xBC](KiIntSteerCalculatePriorityDistribution_function_002D8760.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002D899F  8B 11                           mov edx, dword ptr [rcx]
002D89A1  8B C2                           mov eax, edx
002D89A3  83 E0 3F                        and eax, 0x3f
002D89A6  83 E2 3F                        and edx, 0x3f
002D89A9  48 0F B3 C5                     btr rbp, rax
002D89AD  49 0F B3 C4                     btr r12, rax
002D89B1  48 89 6C 24 30                  mov qword ptr [rsp + 0x30], rbp
002D89B6  8B C2                           mov eax, edx
002D89B8  49 0F B3 C5                     btr r13, rax
002D89BC  4C 89 64 24 40                  mov qword ptr [rsp + 0x40], r12
002D89C1  4C 89 6C 24 50                  mov qword ptr [rsp + 0x50], r13
002D89C6  E9 51 FE FF FF                  jmp 0x1402d881c
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_002D899F(__int64 a1)
{
    __int64 result;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p50;

    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1))))) & (63));
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1))) & (63));
    v_stack_p30 = v_rbp;
    v_stack_p40 = v_r12;
    v_stack_p50 = v_r13;
}
```

## 5. (Beta) C Style

```c
int64_t sub_002D899F(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    uint64_t v_stack_p30;
    uint64_t v_stack_p40;
    uint64_t v_stack_p50;

    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1))))) & (63));
    a2 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1))) & (63));
    v_stack_p30 = local_rbp;
    v_stack_p40 = local_r12;
    v_stack_p50 = local_r13;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002D899F&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002D899F[BB_002D899F]
```
