# sub_002466AA

- RVA: `0x002466AA`–`0x002466C1` (길이 `23` bytes)
- VA: `0x00000001402466AA`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00062034`
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
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x002466AD` → [sub_00246508 + 0x45](Unknown_function_00246508.md) (`tail-transfer`)
  - `0x002466B6` → [sub_00246311 + 0x4C](Unknown_function_00246311.md) (`tail-transfer`)
  - `0x002466BC` → [sub_00246508 + 0xD](Unknown_function_00246508.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002466AA  48 8B D1                        mov rdx, rcx
002466AD  E9 9B FE FF FF                  jmp 0x14024654d
002466B2  F6 43 23 20                     test byte ptr [rbx + 0x23], 0x20
002466B6  0F 84 A1 FC FF FF               je 0x14024635d
002466BC  E9 54 FE FF FF                  jmp 0x140246515
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_002466AA(__int64 a1)
{
}
```

## 5. (Beta) C Style

```c
void sub_002466AA(int64_t Arg1)
{
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002466AA&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002466AA[BB_002466AA]
  bb_002466B2[BB_002466B2]
  bb_002466BC[BB_002466BC]
  bb_002466B2 -->|fallthrough| bb_002466BC
```
