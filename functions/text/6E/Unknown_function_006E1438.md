# sub_006E1438

- RVA: `0x006E1438`–`0x006E144E` (길이 `22` bytes)
- VA: `0x00000001406E1438`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00074D9C`
- 디코드: `4`개 명령, `22/22` bytes 표시
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
- `0x006E1438` → RVA `0x00EF5438` (`.data`; read/write)
- `0x006E1443` → RVA `0x00EF52BC` (`.data`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x006E143E` → [MiActivePageClaimCandidate + 0x261](../31/MiActivePageClaimCandidate_function_0031BB00.md) (`tail-transfer`)
  - `0x006E1449` → [MiActivePageClaimCandidate + 0x261](../31/MiActivePageClaimCandidate_function_0031BB00.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006E1438  FF 05 FA 3F 81 00               inc dword ptr [rip + 0x813ffa]
006E143E  E9 1E A9 C3 FF                  jmp 0x14031bd61
006E1443  FF 05 73 3E 81 00               inc dword ptr [rip + 0x813e73]
006E1449  E9 13 A9 C3 FF                  jmp 0x14031bd61
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_006E1438(void)
{
}
```

## 5. (Beta) C Style

```c
void sub_006E1438(void)
{
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006E1438&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006E1438[BB_006E1438]
  bb_006E1443[BB_006E1443]
```
