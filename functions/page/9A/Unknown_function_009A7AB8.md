# sub_009A7AB8

- RVA: `0x009A7AB8`–`0x009A7ACF` (길이 `23` bytes)
- VA: `0x00000001409A7AB8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009CC34`
- 디코드: `5`개 명령, `23/23` bytes 표시
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
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x009A7AC4` → [sub_00B2D740](../B2/Unknown_function_00B2D740.md) (`tail-transfer`)
  - `0x009A7ACA` → [sub_00B2D740 + 0x15](../B2/Unknown_function_00B2D740.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
009A7AB8  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
009A7ABD  48 8D 79 10                     lea rdi, [rcx + 0x10]
009A7AC1  48 85 C0                        test rax, rax
009A7AC4  0F 85 76 5C 18 00               jne 0x140b2d740
009A7ACA  E9 86 5C 18 00                  jmp 0x140b2d755
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_009A7AB8(__int64 a1)
{
    unsigned __int64 v_stack_p30;

    v_stack_p30 = v_rdi;
}
```

## 5. (Beta) C Style

```c
void sub_009A7AB8(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    uint64_t v_stack_p30;

    v_stack_p30 = local_rdi;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x10` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009A7AB8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009A7AB8[BB_009A7AB8]
  bb_009A7ACA[BB_009A7ACA]
  bb_009A7AB8 -->|fallthrough| bb_009A7ACA
```
