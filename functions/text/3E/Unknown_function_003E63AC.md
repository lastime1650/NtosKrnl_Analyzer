# sub_003E63AC

- RVA: `0x003E63AC`–`0x003E63D6` (길이 `42` bytes)
- VA: `0x00000001403E63AC`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000953EC`
- 디코드: `8`개 명령, `42/42` bytes 표시
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
- call이 아닌 외부 분기/꼬리 이동: **4**
  - `0x003E63B1` → [sub_003E6192 + 0x33](Unknown_function_003E6192.md) (`tail-transfer`)
  - `0x003E63BB` → [sub_003E6192 + 0x27](Unknown_function_003E6192.md) (`tail-transfer`)
  - `0x003E63C7` → [sub_003E6192 + 0x33](Unknown_function_003E6192.md) (`tail-transfer`)
  - `0x003E63D1` → [sub_003E6192 + 0x33](Unknown_function_003E6192.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003E63AC  41 0F BA EF 0A                  bts r15d, 0xa
003E63B1  E9 0F FE FF FF                  jmp 0x1403e61c5
003E63B6  41 0F BA EF 13                  bts r15d, 0x13
003E63BB  E9 F9 FD FF FF                  jmp 0x1403e61b9
003E63C0  41 81 CF 00 07 00 00            or r15d, 0x700
003E63C7  E9 F9 FD FF FF                  jmp 0x1403e61c5
003E63CC  41 0F BA EF 09                  bts r15d, 9
003E63D1  E9 EF FD FF FF                  jmp 0x1403e61c5
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_003E63AC(void)
{
}
```

## 5. (Beta) C Style

```c
void sub_003E63AC(void)
{
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003E63AC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003E63AC[BB_003E63AC]
  bb_003E63B6[BB_003E63B6]
  bb_003E63C0[BB_003E63C0]
  bb_003E63CC[BB_003E63CC]
```
