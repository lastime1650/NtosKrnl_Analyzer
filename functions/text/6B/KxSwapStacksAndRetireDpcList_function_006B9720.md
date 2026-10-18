# KxSwapStacksAndRetireDpcList

- RVA: `0x006B9720`–`0x006B9729` (길이 `9` bytes)
- VA: `0x00000001406B9720`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C2334`
- 디코드: `4`개 명령, `9/9` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006B9720` → [KiRetireDpcList](../21/KiRetireDpcList_function_0021A0B0.md) (function, `0x0021A0B0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006B9725` → [KiSwapStacksAndRetireDpcList + 0xF](KiSwapStacksAndRetireDpcList_function_006B9700.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006B9720  E8 8B 09 B6 FF                  call 0x14021a0b0
006B9725  EB E8                           jmp 0x1406b970f
006B9727  CC                              int3
006B9728  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KxSwapStacksAndRetireDpcList(void)
{
    __int64 result;

    result = KiRetireDpcList(a1, a2, a3, a4);
}
```

## 5. (Beta) C Style

```c
void KxSwapStacksAndRetireDpcList(void)
{
    int64_t result;

    result = KiRetireDpcList(a1, a2, a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006B9720&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006B9720[BB_006B9720]
  bb_006B9727[BB_006B9727]
```
