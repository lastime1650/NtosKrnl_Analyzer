# sub_003DD85C

- RVA: `0x003DD85C`–`0x003DD86B` (길이 `15` bytes)
- VA: `0x00000001403DD85C`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000943C0`
- 디코드: `6`개 명령, `15/15` bytes 표시
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
  - `0x003DD862` → [sub_003DD808 + 0x36](Unknown_function_003DD808.md) (`tail-transfer`)
  - `0x003DD867` → [sub_003DD808 + 0x36](Unknown_function_003DD808.md) (`tail-transfer`)
  - `0x003DD869` → [sub_003DD808 + 0x33](Unknown_function_003DD808.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003DD85C  41 FF C3                        inc r11d
003DD85F  83 F9 01                        cmp ecx, 1
003DD862  76 DA                           jbe 0x1403dd83e
003DD864  41 85 EE                        test r14d, ebp
003DD867  74 D5                           je 0x1403dd83e
003DD869  EB D0                           jmp 0x1403dd83b
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_003DD85C(int a1)
{
    __int64 v_r11;

    v_r11 = (unsigned int)((v_r11) + 1);
}
```

## 5. (Beta) C Style

```c
void sub_003DD85C(int32_t Arg1)
{
    int64_t local_r11;

    local_r11 = (uint32_t)((local_r11) + 1);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003DD85C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003DD85C[BB_003DD85C]
  bb_003DD864[BB_003DD864]
  bb_003DD869[BB_003DD869]
  bb_003DD85C -->|fallthrough| bb_003DD864
  bb_003DD864 -->|fallthrough| bb_003DD869
```
