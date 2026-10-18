# sub_0085EB76

- RVA: `0x0085EB76`–`0x0085EBA1` (길이 `43` bytes)
- VA: `0x000000014085EB76`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006B25C`
- 디코드: `9`개 명령, `43/43` bytes 표시
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
  - `0x0085EB9B` → [sub_0085EF76](Unknown_function_0085EF76.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0085EB76  4C 89 74 24 70                  mov qword ptr [rsp + 0x70], r14
0085EB7B  4C 8D B1 88 00 00 00            lea r14, [rcx + 0x88]
0085EB82  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
0085EB87  41 0F 0D 0E                     prefetchw byte ptr [r14]
0085EB8B  49 8B 06                        mov rax, qword ptr [r14]
0085EB8E  48 83 E0 FE                     and rax, 0xfffffffffffffffe
0085EB92  48 8D 48 02                     lea rcx, [rax + 2]
0085EB96  F0 49 0F B1 0E                  lock cmpxchg qword ptr [r14], rcx
0085EB9B  0F 85 D5 03 00 00               jne 0x14085ef76
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0085EB76(__int64 a1)
{
    __int64 result;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p70;

    v_stack_p70 = v_r14;
    v_stack_p30 = a1 + 136;
    result = (*(unsigned __int64 *)(a1 + 136)) & (-2);
}
```

## 5. (Beta) C Style

```c
int64_t sub_0085EB76(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    uint64_t v_stack_p30;
    uint64_t v_stack_p70;

    v_stack_p70 = local_r14;
    v_stack_p30 = Arg1 + 136;
    result = (*(uint64_t *)(arg1 + 0x88)) & (-2);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `8` | `R` |
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x88` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0085EB76&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0085EB76[BB_0085EB76]
```
