# sub_0023FF9D

- RVA: `0x0023FF9D`–`0x0023FFB5` (길이 `24` bytes)
- VA: `0x000000014023FF9D`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00061694`
- 디코드: `6`개 명령, `24/24` bytes 표시
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
  - `0x0023FFAE` → [sub_0023FFC8](Unknown_function_0023FFC8.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0023FF9D  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
0023FFA2  48 8B 3C C2                     mov rdi, qword ptr [rdx + rax*8]
0023FFA6  8B 87 3C 04 00 00               mov eax, dword ptr [rdi + 0x43c]
0023FFAC  85 C0                           test eax, eax
0023FFAE  75 18                           jne 0x14023ffc8
0023FFB0  48 8B 7C 24 30                  mov rdi, qword ptr [rsp + 0x30]
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0023FF9D(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6)
{
    unsigned __int64 v_stack_p30;

    v_stack_p30 = v_rdi;
    return (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + result * 8) + 1084));
}
```

## 5. (Beta) C Style

```c
int64_t sub_0023FF9D(int64_t Arg1, void *Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, int64_t Arg6)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    uint64_t v_stack_p30;

    v_stack_p30 = local_rdi;
    return (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + result * 8) + 0x43C));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0 + rax*8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0023FF9D&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0023FF9D[BB_0023FF9D]
  bb_0023FFB0[BB_0023FFB0]
  bb_0023FF9D -->|fallthrough| bb_0023FFB0
```
