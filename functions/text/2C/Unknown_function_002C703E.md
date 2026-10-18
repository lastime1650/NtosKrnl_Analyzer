# sub_002C703E

- RVA: `0x002C703E`–`0x002C7057` (길이 `25` bytes)
- VA: `0x00000001402C703E`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006ED08`
- 디코드: `4`개 명령, `25/25` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x002C703E` → RVA `0x00E2F390` (`.data`; read)
- `0x002C704B` → RVA `0x00E2EE85` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x002C7045` → [sub_002C6E36 + 0xEE](Unknown_function_002C6E36.md) (`tail-transfer`)
  - `0x002C7052` → [sub_002C6E36 + 0x102](Unknown_function_002C6E36.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002C703E  48 3B 05 4B 83 B6 00            cmp rax, qword ptr [rip + 0xb6834b]
002C7045  0F 87 D9 FE FF FF               ja 0x1402c6f24
002C704B  0F B6 05 33 7E B6 00            movzx eax, byte ptr [rip + 0xb67e33]
002C7052  E9 E1 FE FF FF                  jmp 0x1402c6f38
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_002C703E(void)
{
}
```

## 5. (Beta) C Style

```c
void sub_002C703E(void)
{
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002C703E&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002C703E[BB_002C703E]
  bb_002C704B[BB_002C704B]
  bb_002C703E -->|fallthrough| bb_002C704B
```
