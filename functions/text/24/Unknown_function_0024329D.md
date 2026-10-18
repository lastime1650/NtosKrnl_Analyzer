# sub_0024329D

- RVA: `0x0024329D`–`0x002432BB` (길이 `30` bytes)
- VA: `0x000000014024329D`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00061A64`
- 디코드: `5`개 명령, `30/30` bytes 표시
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
  - `0x002432B5` → [sub_00243448 + 0x1A](Unknown_function_00243448.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0024329D  48 89 AC 24 28 01 00 00         mov qword ptr [rsp + 0x128], rbp
002432A5  48 89 B4 24 30 01 00 00         mov qword ptr [rsp + 0x130], rsi
002432AD  8D 41 FD                        lea eax, [rcx - 3]
002432B0  A9 FC FF FF FF                  test eax, 0xfffffffc
002432B5  0F 84 A7 01 00 00               je 0x140243462
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0024329D(__int64 a1)
{
    unsigned __int64 v_stack_p128;
    unsigned __int64 v_stack_p130;

    v_stack_p128 = v_rbp;
    v_stack_p130 = v_rsi;
}
```

## 5. (Beta) C Style

```c
int64_t sub_0024329D(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    uint64_t v_stack_p128;
    uint64_t v_stack_p130;

    v_stack_p128 = local_rbp;
    v_stack_p130 = local_rsi;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `- 0x3` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0024329D&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0024329D[BB_0024329D]
```
