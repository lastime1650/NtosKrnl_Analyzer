# sub_002579C3

- RVA: `0x002579C3`–`0x002579D5` (길이 `18` bytes)
- VA: `0x00000001402579C3`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00063B90`
- 디코드: `5`개 명령, `18/18` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x002579C9` → [KiQueryEffectivePriorityThread](KiQueryEffectivePriorityThread_function_00257BA0.md) (function, `0x00257BA0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x002579D0` → [sub_002578AE + 0x28](Unknown_function_002578AE.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002579C3  48 8B D6                        mov rdx, rsi
002579C6  48 8B CF                        mov rcx, rdi
002579C9  E8 D2 01 00 00                  call 0x140257ba0
002579CE  32 C3                           xor al, bl
002579D0  E9 01 FF FF FF                  jmp 0x1402578d6
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_002579C3(void)
{
    __int64 result;

    result = KiQueryEffectivePriorityThread(v_rdi, v_rsi, a3, a4);
    result = (unsigned __int8)((result) ^ ((unsigned __int8)(v_rbx)));
}
```

## 5. (Beta) C Style

```c
void sub_002579C3(void)
{
    int64_t result;

    result = KiQueryEffectivePriorityThread(local_rdi, local_rsi, a3, a4);
    result = (uint8_t)((result) ^ ((uint8_t)(local_rbx)));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002579C3&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002579C3[BB_002579C3]
```
