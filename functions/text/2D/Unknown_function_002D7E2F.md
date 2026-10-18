# sub_002D7E2F

- RVA: `0x002D7E2F`–`0x002D7E45` (길이 `22` bytes)
- VA: `0x00000001402D7E2F`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000700AC`
- 디코드: `5`개 명령, `22/22` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x002D7E38` → [HvlGetReferenceTime](HvlGetReferenceTime_function_002DDB88.md) (function, `0x002DDB88`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x002D7E32` → [sub_006DDC2E](../6D/Unknown_function_006DDC2E.md) (`tail-transfer`)
  - `0x002D7E40` → [sub_006DDC2E](../6D/Unknown_function_006DDC2E.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002D7E2F  4D 85 ED                        test r13, r13
002D7E32  0F 85 F6 5D 40 00               jne 0x1406ddc2e
002D7E38  E8 4B 5D 00 00                  call 0x1402ddb88
002D7E3D  4C 8B E8                        mov r13, rax
002D7E40  E9 E9 5D 40 00                  jmp 0x1406ddc2e
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_002D7E2F(void)
{
    __int64 result;

    result = HvlGetReferenceTime(a1, a2, a3, a4);
}
```

## 5. (Beta) C Style

```c
void sub_002D7E2F(void)
{
    int64_t result;

    result = HvlGetReferenceTime(a1, a2, a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002D7E2F&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002D7E2F[BB_002D7E2F]
  bb_002D7E38[BB_002D7E38]
  bb_002D7E2F -->|fallthrough| bb_002D7E38
```
