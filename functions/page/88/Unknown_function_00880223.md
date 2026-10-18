# sub_00880223

- RVA: `0x00880223`–`0x0088023C` (길이 `25` bytes)
- VA: `0x0000000140880223`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007C468`
- 디코드: `5`개 명령, `25/25` bytes 표시
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
  - `0x00880227` → [sub_0088018D + 0xE](Unknown_function_0088018D.md) (`tail-transfer`)
  - `0x00880231` → [sub_0088018D + 0xE](Unknown_function_0088018D.md) (`tail-transfer`)
  - `0x00880237` → [sub_0087FFB4 + 0x55](../87/Unknown_function_0087FFB4.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00880223  0F BA E6 10                     bt esi, 0x10
00880227  0F 83 6E FF FF FF               jae 0x14088019b
0088022D  0F BA E6 0E                     bt esi, 0xe
00880231  0F 82 64 FF FF FF               jb 0x14088019b
00880237  E9 CD FD FF FF                  jmp 0x140880009
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_00880223(void)
{
}
```

## 5. (Beta) C Style

```c
void sub_00880223(void)
{
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00880223&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00880223[BB_00880223]
  bb_0088022D[BB_0088022D]
  bb_00880237[BB_00880237]
  bb_00880223 -->|fallthrough| bb_0088022D
  bb_0088022D -->|fallthrough| bb_00880237
```
