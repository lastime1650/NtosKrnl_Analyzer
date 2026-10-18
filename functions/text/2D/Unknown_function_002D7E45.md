# sub_002D7E45

- RVA: `0x002D7E45`–`0x002D7E61` (길이 `28` bytes)
- VA: `0x00000001402D7E45`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000700D4`
- 디코드: `5`개 명령, `28/28` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x002D7E45` → RVA `0x00FC6BA8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x002D7E56` → [sub_002D7CF9](Unknown_function_002D7CF9.md) (`tail-transfer`)
  - `0x002D7E5C` → [sub_006DDC62](../6D/Unknown_function_006DDC62.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002D7E45  48 8B 1D 5C ED CE 00            mov rbx, qword ptr [rip + 0xceed5c]
002D7E4C  48 8D 35 55 ED CE 00            lea rsi, [rip + 0xceed55]
002D7E53  48 3B DE                        cmp rbx, rsi
002D7E56  0F 84 9D FE FF FF               je 0x1402d7cf9
002D7E5C  E9 01 5E 40 00                  jmp 0x1406ddc62
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_002D7E45(void)
{
}
```

## 5. (Beta) C Style

```c
void sub_002D7E45(void)
{
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002D7E45&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002D7E45[BB_002D7E45]
  bb_002D7E5C[BB_002D7E5C]
  bb_002D7E45 -->|fallthrough| bb_002D7E5C
```
