# sub_00B36D5C

- RVA: `0x00B36D5C`–`0x00B36D76` (길이 `26` bytes)
- VA: `0x0000000140B36D5C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A98C8`
- 디코드: `7`개 명령, `26/26` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00B36D5C` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00B36D5C` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x00B36D62` → [PspWow64GetContextThread + 0x191](../A1/PspWow64GetContextThread_function_00A11E90.md) (`tail-transfer`)
  - `0x00B36D6B` → [PspWow64GetContextThread + 0x2E3](../A1/PspWow64GetContextThread_function_00A11E90.md) (`tail-transfer`)
  - `0x00B36D71` → [PspWow64GetContextThread + 0x2A3](../A1/PspWow64GetContextThread_function_00A11E90.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B36D5C  E8 4F 6B 72 FF                  call 0x14025d8b0
00B36D61  90                              nop
00B36D62  E9 BA B2 ED FF                  jmp 0x140a12021
00B36D67  85 C0                           test eax, eax
00B36D69  8B D8                           mov ebx, eax
00B36D6B  0F 88 02 B4 ED FF               js 0x140a12173
00B36D71  E9 BD B3 ED FF                  jmp 0x140a12133
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00B36D5C(void)
{
    __int64 result;

    result = KeLeaveCriticalRegion(a1, a2, a3, a4);
}
```

## 5. (Beta) C Style

```c
void sub_00B36D5C(void)
{
    int64_t result;

    result = KeLeaveCriticalRegion(a1, a2, a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B36D5C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B36D5C[BB_00B36D5C]
  bb_00B36D67[BB_00B36D67]
  bb_00B36D71[BB_00B36D71]
  bb_00B36D67 -->|fallthrough| bb_00B36D71
```
