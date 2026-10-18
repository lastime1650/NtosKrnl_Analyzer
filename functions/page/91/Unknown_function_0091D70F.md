# sub_0091D70F

- RVA: `0x0091D70F`–`0x0091D72D` (길이 `30` bytes)
- VA: `0x000000014091D70F`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008B274`
- 디코드: `7`개 명령, `30/30` bytes 표시
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
  - `0x0091D71E` → [sub_0091D785](Unknown_function_0091D785.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0091D70F  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
0091D714  48 8B B9 50 03 00 00            mov rdi, qword ptr [rcx + 0x350]
0091D71B  48 85 FF                        test rdi, rdi
0091D71E  74 65                           je 0x14091d785
0091D720  0F B7 57 02                     movzx edx, word ptr [rdi + 2]
0091D724  B9 40 00 00 00                  mov ecx, 0x40
0091D729  48 83 C2 10                     add rdx, 0x10
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_0091D70F(__int64 a1)
{
    unsigned __int64 v_stack_p38;

    v_stack_p38 = v_rdi;
    a2 = (*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 848) + 2)) + (16);
    return;
}
```

## 5. (Beta) C Style

```c
void sub_0091D70F(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    uint64_t v_stack_p38;

    v_stack_p38 = local_rdi;
    a2 = (*(uint16_t *)(*(uint64_t *)(arg1 + 0x350) + 0x2)) + (16);
    return;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x350` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0091D70F&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0091D70F[BB_0091D70F]
  bb_0091D720[BB_0091D720]
  bb_0091D70F -->|fallthrough| bb_0091D720
```
