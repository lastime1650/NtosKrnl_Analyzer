# sub_009A5B7B

- RVA: `0x009A5B7B`–`0x009A5B88` (길이 `13` bytes)
- VA: `0x00000001409A5B7B`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009C6A4`
- 디코드: `4`개 명령, `13/13` bytes 표시
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
  - `0x009A5B7F` → [sub_009A5BBB + 0x9](Unknown_function_009A5BBB.md) (`tail-transfer`)
  - `0x009A5B86` → [sub_009A5B10](Unknown_function_009A5B10.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
009A5B7B  F6 41 02 01                     test byte ptr [rcx + 2], 1
009A5B7F  75 43                           jne 0x1409a5bc4
009A5B81  B8 BB 00 00 C0                  mov eax, 0xc00000bb
009A5B86  EB 88                           jmp 0x1409a5b10
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_009A5B7B(__int64 a1)
{
}
```

## 5. (Beta) C Style

```c
int64_t sub_009A5B7B(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x2` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009A5B7B&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009A5B7B[BB_009A5B7B]
  bb_009A5B81[BB_009A5B81]
  bb_009A5B7B -->|fallthrough| bb_009A5B81
```
