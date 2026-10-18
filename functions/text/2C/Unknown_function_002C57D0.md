# sub_002C57D0

- RVA: `0x002C57D0`–`0x002C57E7` (길이 `23` bytes)
- VA: `0x00000001402C57D0`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006EB30`
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
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x002C57D8` → [sub_002C56D7](Unknown_function_002C56D7.md) (`tail-transfer`)
  - `0x002C57E2` → [sub_002C56D7](Unknown_function_002C56D7.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002C57D0  40 80 E6 05                     and sil, 5
002C57D4  40 80 FE 04                     cmp sil, 4
002C57D8  0F 85 F9 FE FF FF               jne 0x1402c56d7
002C57DE  48 83 CB 42                     or rbx, 0x42
002C57E2  E9 F0 FE FF FF                  jmp 0x1402c56d7
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_002C57D0(void)
{
    __int64 v_rbx;
    __int64 v_rsi;

    v_rsi = (unsigned __int8)((v_rsi) & (5));
    v_rbx = (v_rbx) | (66);
}
```

## 5. (Beta) C Style

```c
void sub_002C57D0(void)
{
    int64_t local_rbx;
    int64_t local_rsi;

    local_rsi = (uint8_t)((local_rsi) & (5));
    local_rbx = (local_rbx) | (66);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002C57D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002C57D0[BB_002C57D0]
  bb_002C57DE[BB_002C57DE]
  bb_002C57D0 -->|fallthrough| bb_002C57DE
```
