# sub_003DE6AD

- RVA: `0x003DE6AD`–`0x003DE6C1` (길이 `20` bytes)
- VA: `0x00000001403DE6AD`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00094554`
- 디코드: `4`개 명령, `20/20` bytes 표시
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
  - `0x003DE6B4` → [sub_003DE542 + 0x4D](Unknown_function_003DE542.md) (`tail-transfer`)
  - `0x003DE6BC` → [sub_003DE542 + 0x4F](Unknown_function_003DE542.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003DE6AD  80 B9 BD 01 00 00 00            cmp byte ptr [rcx + 0x1bd], 0
003DE6B4  0F 85 D5 FE FF FF               jne 0x1403de58f
003DE6BA  B3 01                           mov bl, 1
003DE6BC  E9 D0 FE FF FF                  jmp 0x1403de591
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_003DE6AD(__int64 a1)
{
}
```

## 5. (Beta) C Style

```c
void sub_003DE6AD(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x1BD` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003DE6AD&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003DE6AD[BB_003DE6AD]
  bb_003DE6BA[BB_003DE6BA]
  bb_003DE6AD -->|fallthrough| bb_003DE6BA
```
